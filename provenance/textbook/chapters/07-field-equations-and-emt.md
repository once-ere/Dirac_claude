## 7. Field equations, energy–momentum tensor and equations of state

### 7.1 What this chapter does

Chapter 6 wrote down one Lagrangian for two fields, dirac16complex (complex Grassmann components) and dirac16complex00 (complex commuting components):

$$
\mathcal L=\sqrt{|g|}\,\bigl[K-mS-U(S)\bigr],\qquad K=\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr),\qquad S=\bar\Psi\Psi .
$$

This chapter derives everything that the physics needs from it, in an arbitrary gravitational field and for both fields:

- the **field equations**, from the principle of stationary action of Chapter 5 (Sections 7.2 to 7.4);
- the **conserved current** and the **charge**, from the phase symmetry (Section 7.5);
- the **energy–momentum tensor**, from the response of the action to a change of the gravitational field, with its symmetry, reality, trace and conservation (Sections 7.6 to 7.8);
- the **energy density**, the **pressures**, two definitions of **kinetic and potential energy**, and the **equations of state** (Section 7.9).

Then it specializes these results to the situations used later in the book: homogeneous backgrounds (Section 7.10), plane waves in flat space, where the commuting field shows an indefinite charge and an energy without lower bound (Section 7.11), and the notebook's primordial field, including an exact classical dirac16complex00 source of its static member (Section 7.12). Section 7.13 derives how the chirality map $\gamma^8$ of Section 6.11 acts on all of these.

**Sources.** The Stage-1 document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md` (its §8, §9 and §10.9) with its reports in `artifacts/dirac16complex/arbitrary-field/`; the Stage-5 specification `handoff/specs/STAGE5_SPEC.md` (its §2 and §3); the exact Stage-5 reports on dirac16complex00, `wolfram-dirac16complex00-report.json` (46 of 46 checks) and `python-dirac16complex00-report.json` (49 of 49), with `dirac16complex00-theory.json`, all in `artifacts/dirac16complex/pair-creation/`; the pairing reports in the same folder (141 of 141 and 172 of 172 checks); and Theorem M1 of the matter–antimatter document `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md` (its §4). The prefixes of the check names are those of Section 6.1: `C00_` for the Wolfram dirac16complex00 report, `PAIR_` for the Wolfram pairing report `wolfram-pairing-report.json`, and `S5_` for both independent Python reports. The Python twin of a `C00_` check is the `S5_` check with the same ending in `python-dirac16complex00-report.json`, and the Python twin of a `PAIR_` check is the `S5_` check with the same ending in `python-pairing-report.json`; an `S5_` name cited on its own in this chapter is a check of `python-dirac16complex00-report.json`. `MA_` marks the matter–antimatter reports, and the Stage-1 checks have no prefix of this kind. The Stage-5 prose documents had not been written when this chapter was written; the chapter cites the committed reports.

**Notation used throughout** (Chapter 6): $\bar\Psi=\Psi^\dagger C$; $\gamma^\mu=e_a{}^\mu\gamma^a$; $D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi$ and $D_\mu\bar\Psi=\partial_\mu\bar\Psi-\bar\Psi\Omega_\mu$; $\mathcal L_s=\mathcal L/\sqrt{|g|}=K-mS-U(S)$; $M_{\mathrm{eff}}=m+U'(S)$; and the default potential $U=\tfrac\lambda2S^2$, for which $M_{\mathrm{eff}}=m+\lambda S$. The facts (B1) to (B6) of Section 6.3 are used without further comment; the most important are that $C\gamma^\mu$ is real and antisymmetric and the divergence identity $\partial_\mu(\sqrt{|g|}\,\gamma^\mu)=\sqrt{|g|}\,[\gamma^\mu,\Omega_\mu]$.

### 7.2 The Euler–Lagrange equations of dirac16complex00

For commuting components we vary $\Psi_a$ and $\Psi_a^\ast$ as if they were independent, as justified in Section 5.6. We first need the Lagrangian written so that the dependence on $\Psi^\ast$ and on its derivatives is visible. Using $D_\mu\bar\Psi=\partial_\mu\Psi^\dagger C-\Psi^\dagger C\Omega_\mu$,

$$
\frac{\mathcal L}{\sqrt{|g|}}=\tfrac12\,\Psi^\dagger C\gamma^\mu D_\mu\Psi-\tfrac12\,(\partial_\mu\Psi^\dagger)\,C\gamma^\mu\Psi+\tfrac12\,\Psi^\dagger C\Omega_\mu\gamma^\mu\Psi-m\,\Psi^\dagger C\Psi-U(\Psi^\dagger C\Psi).
$$

**Step 1 (derivative with respect to $\Psi_a^\ast$).** Every term except the second contains $\Psi^\dagger$ undifferentiated, as the left factor of a row–matrix–column product; the derivative of $\Psi^\dagger Y$ with respect to $\Psi_a^\ast$ is the entry $a$ of the column $Y$. For the potential, the chain rule and $\partial S/\partial\Psi_a^\ast=(C\Psi)_a$ give $U'(S)(C\Psi)_a$. So

$$
\frac{\partial\mathcal L}{\partial\Psi_a^\ast}=\sqrt{|g|}\,\Bigl(\tfrac12\,C\gamma^\mu D_\mu\Psi+\tfrac12\,C\Omega_\mu\gamma^\mu\Psi-\bigl(m+U'(S)\bigr)C\Psi\Bigr)_a .
$$

**Step 2 (derivative with respect to $\partial_\mu\Psi_a^\ast$).** Only the second term contains it:

$$
\frac{\partial\mathcal L}{\partial(\partial_\mu\Psi_a^\ast)}=-\tfrac12\sqrt{|g|}\,\bigl(C\gamma^\mu\Psi\bigr)_a .
$$

**Step 3 (the Euler–Lagrange expression).** By Section 5.3, $\mathcal E=\partial\mathcal L/\partial\Psi^\ast-\partial_\mu\bigl(\partial\mathcal L/\partial(\partial_\mu\Psi^\ast)\bigr)$, a column of 16 entries:

$$
\mathcal E=\sqrt{|g|}\,C\Bigl(\tfrac12\gamma^\mu D_\mu\Psi+\tfrac12\Omega_\mu\gamma^\mu\Psi-M_{\mathrm{eff}}\Psi\Bigr)+\tfrac12\,\partial_\mu\bigl(\sqrt{|g|}\,C\gamma^\mu\Psi\bigr).
$$

**Step 4 (the divergence identity).** $C$ is constant, so by the product rule and (B6)

$$
\partial_\mu\bigl(\sqrt{|g|}\,C\gamma^\mu\Psi\bigr)=C\,\partial_\mu\bigl(\sqrt{|g|}\,\gamma^\mu\bigr)\Psi+\sqrt{|g|}\,C\gamma^\mu\partial_\mu\Psi=\sqrt{|g|}\,C\bigl(\gamma^\mu\Omega_\mu\Psi-\Omega_\mu\gamma^\mu\Psi+\gamma^\mu\partial_\mu\Psi\bigr).
$$

**Step 5 (collect).** Inserting Step 4 into Step 3, the two terms $\pm\tfrac12\Omega_\mu\gamma^\mu\Psi$ cancel, and $\tfrac12\gamma^\mu\Omega_\mu\Psi+\tfrac12\gamma^\mu\partial_\mu\Psi=\tfrac12\gamma^\mu D_\mu\Psi$:

$$
\mathcal E=\sqrt{|g|}\,C\bigl(\gamma^\mu D_\mu\Psi-M_{\mathrm{eff}}\Psi\bigr).
$$

**Step 6 (the equation).** $\sqrt{|g|}\ne0$ and $C$ is invertible ($C^2=1$), so $\mathcal E=0$ is equivalent to

$$
\gamma^\mu D_\mu\Psi=\bigl(m+U'(S)\bigr)\Psi .
$$

**The equation for $\bar\Psi$.** Varying $\Psi_b$ in the same way: the terms that contain $\Psi$ undifferentiated give $\partial\mathcal L/\partial\Psi_b=\sqrt{|g|}\bigl(\tfrac12\bar\Psi\gamma^\mu\Omega_\mu-\tfrac12(D_\mu\bar\Psi)\gamma^\mu-M_{\mathrm{eff}}\bar\Psi\bigr)_b$, and $\partial\mathcal L/\partial(\partial_\mu\Psi_b)=\tfrac12\sqrt{|g|}\,(\bar\Psi\gamma^\mu)_b$. The Euler–Lagrange expression is

$$
\sqrt{|g|}\Bigl(\tfrac12\bar\Psi\gamma^\mu\Omega_\mu-\tfrac12(D_\mu\bar\Psi)\gamma^\mu-M_{\mathrm{eff}}\bar\Psi\Bigr)-\tfrac12(\partial_\mu\bar\Psi)\sqrt{|g|}\gamma^\mu-\tfrac12\bar\Psi\,\partial_\mu\bigl(\sqrt{|g|}\gamma^\mu\bigr)=-\sqrt{|g|}\Bigl((D_\mu\bar\Psi)\gamma^\mu+M_{\mathrm{eff}}\bar\Psi\Bigr),
$$

where the last step used (B6) once more. So the second field equation is

$$
(D_\mu\bar\Psi)\gamma^\mu=-\bigl(m+U'(S)\bigr)\bar\Psi .
$$

The Stage-5 verifiers derive both Euler–Lagrange expressions for commuting components in two independent ways (directly and from the momenta $\partial\mathcal L/\partial(\partial_\mu\Psi^\ast)=-\tfrac12\sqrt{|g|}\,C\gamma^\mu\Psi$), in flat space, at the three points of the general test geometry G1 and at three points of the primordial field G2, with $\lambda\ne0$ and also with an abstract smooth $U$ (checks `C00_EL_commutingFlat`, `C00_EL_commutingCurved`, `C00_EL_commutingGeneralSmoothU` and their `S5_` twins; the Lagrangian has 1304 terms at each G1 point).

### 7.3 The same equations for dirac16complex

For Grassmann components the derivatives must be taken with the rules of Section 5.10: the left derivative for $\Psi^\ast$ and the right derivative for $\Psi$. In every term of $\mathcal L$ the factor $\Psi^\dagger$ (or $\partial_\mu\Psi^\dagger$) already stands on the far left and the factor $\Psi$ (or $\partial_\mu\Psi$) on the far right, so moving the varied generator to the left, respectively to the right, passes no other odd factor and costs no sign. For the potential, $S$ is even and commutes with everything, so the left derivative of $S^k$ with respect to $\Psi_a^\ast$ is $kS^{k-1}(C\Psi)_a$, and hence that of $U(S)$ is $U'(S)(C\Psi)_a$, exactly as for commuting numbers. Steps 1 to 6 of Section 7.2 therefore go through word for word, and the two field equations are the same:

$$
\gamma^\mu D_\mu\Psi=\bigl(m+U'(S)\bigr)\Psi,\qquad (D_\mu\bar\Psi)\gamma^\mu=-\bigl(m+U'(S)\bigr)\bar\Psi .
$$

(If the derivative with respect to $\Psi$ is taken from the left instead, the second expression changes its overall sign, by Proposition 5.3; the equation is the same.)

Stage 1 verified these expressions in a genuine Grassmann algebra at the G1 and G2 points with $\lambda\ne0$. Stage 5 repeated the computation at the point G1 p1 in its own Grassmann algebra, where the Lagrangian has 1288 monomials, and recorded that the two statistics give identical equations. The checks are

```
Stage 1:  LAG_eulerLagrangePsibar_G1   LAG_eulerLagrangePsibar_G2
          LAG_eulerLagrangePsi_G1      LAG_eulerLagrangePsi_G2
          GR_complexQuarticEL          GR_complexPsiEquation
Stage 5:  S5_EL_grassmannCurved
          C00_EL_identicalFormBothStatistics   S5_EL_identicalFormBothStatistics
```

### 7.4 What the field equations say

**The two equations are one.** The second equation is the conjugate of the first. Take the conjugate transpose of $\gamma^\mu D_\mu\Psi$ and multiply by $C$ on the right: $(\gamma^\mu D_\mu\Psi)^\dagger C=(D_\mu\Psi)^\dagger(\gamma^\mu)^TC=-(D_\mu\Psi)^\dagger C\gamma^\mu=-(D_\mu\bar\Psi)\gamma^\mu$, using $(\gamma^\mu)^TC=-C\gamma^\mu$ and $(D_\mu\Psi)^\dagger C=D_\mu\bar\Psi$. And $(M_{\mathrm{eff}}\Psi)^\dagger C=M_{\mathrm{eff}}\bar\Psi$ because $M_{\mathrm{eff}}$ is real. So the conjugate of the first equation is the second. For commuting components this means that one complex equation of 16 components is the whole content.

**Written out** (Stage-1 document, §8.3): with $\Omega_\mu=\tfrac18\omega_{\mu bc}[\gamma^b,\gamma^c]$,

$$
\sum_{\mu=0}^7\sum_{a=0}^7\sum_{k=0}^{15}e_a{}^\mu(\gamma^a)_{jk}\Bigl(\partial_\mu\Psi_k+\sum_{l=0}^{15}(\Omega_\mu)_{kl}\Psi_l\Bigr)=\bigl(m+U'(S)\bigr)\Psi_j\qquad(j=0,\dots,15).
$$

**First order in time.** Suppose the frame's time direction is aligned with $x_4$, $\gamma^{x_4}=\gamma^4$ (this holds in the backgrounds that the book uses for physics: the homogeneous frames, the primordial field and its static member). Multiplying the equation by $-\gamma^4$ and using $(\gamma^4)^2=-1$ gives

$$
D_4\Psi=-\gamma^4\Bigl(M_{\mathrm{eff}}\Psi-\sum_{\mu\ne4}\gamma^\mu D_\mu\Psi\Bigr):
$$

the time derivative of $\Psi$ is fixed by $\Psi$ and its derivatives along the slice. As for the first-order oscillators of Section 5.6, the initial values of $\Psi$ alone determine the evolution; no initial velocities are needed.

**The on-shell value of $K$ and of $\mathcal L_s$.** Multiply the first equation by $\bar\Psi$ from the left: $\bar\Psi\gamma^\mu D_\mu\Psi=M_{\mathrm{eff}}S$. Multiply the second by $\Psi$ from the right: $(D_\mu\bar\Psi)\gamma^\mu\Psi=-M_{\mathrm{eff}}S$. (For Grassmann components $M_{\mathrm{eff}}=m+U'(S)$ is even and commutes with every component, so it may be moved out.) Hence on every solution

$$
K=M_{\mathrm{eff}}\,S,\qquad \mathcal L_s=K-mS-U=S\,U'(S)-U(S),
$$

and for the default potential $\mathcal L_s=\tfrac\lambda2S^2$ on shell (Stage-1 document, §9.2; checks `EMT_onshellLagrangianSUprimeMinusU_G1` and `_G2`).

**The mass shell in a curved field.** Let $U=0$. Apply the operator $\gamma^\nu D_\nu$ to both sides of $\gamma^\mu D_\mu\Psi=m\Psi$; since $m$ is a constant, $(\gamma^\nu D_\nu)^2\Psi=m\,\gamma^\nu D_\nu\Psi=m^2\Psi$. The Lichnerowicz formula of Section 4.13 rewrites the left side, so every solution satisfies the second-order equation

$$
g^{\mu\nu}\bigl(D_\mu D_\nu\Psi-\Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi\bigr)-\tfrac14R\,\Psi=m^2\Psi .
$$

In flat space ($R=0$, $\Omega=0$, $\Gamma=0$) each component obeys $\eta^{ab}\partial_a\partial_b\Psi_k=m^2\Psi_k$, the ultrahyperbolic equation of Section 5.5, which gives the dispersion relation of Section 6.6. In a curved field the scalar curvature appears explicitly. The Stage-5 verifier confirms the second-order form on shell at seven test points with $R\ne0$ (measurement `onShellSecondOrder` of check `C00_connection_nonTrivialCoupling`).

**The connection term.** The equation reads $\gamma^\mu\partial_\mu\Psi+(\gamma^\mu\Omega_\mu)\Psi=M_{\mathrm{eff}}\Psi$. Section 6.8 showed that for a diagonal vielbein $\gamma^\mu\Omega_\mu=\frac1{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\,\gamma^\mu)$. Two cases used later:

- a homogeneous diagonal background, $ds^2=-dx_4^2+\sum_{i\ne4}\eta_{ii}h_i(x_4)^2dx_i^2$, with $\sqrt{|g|}=V:=\prod_{i\ne4}h_i$, the curved gammas $\gamma^{x_4}=\gamma^4$ and $\gamma^{x_i}=\gamma^i/h_i(x_4)$. Nothing depends on the coordinates $x_i$ with $i\ne4$, so in $\partial_\mu(\sqrt{|g|}\,\gamma^\mu)$ the terms with $\mu=i$ vanish, and the term with $\mu=4$ is $\partial_4(V\gamma^4)=(\partial_4V)\,\gamma^4$ because $\gamma^4$ is a constant matrix. Hence $\gamma^\mu\Omega_\mu=\frac{\partial_4V}{2V}\gamma^4=\tfrac12\Theta\,\gamma^4$ with the total expansion rate $\Theta=\partial_4\ln V=\sum_{i\ne4}H_i$, $H_i=\partial_4h_i/h_i$ (the last equality is the derivative of the logarithm of a product; Chapter 11 uses the same formula);
- the notebook's primordial field: $\gamma^\mu\Omega_\mu=3H\gamma^0$, independent of the free function $a_4$ (Sections 4.12 and 9.13).

**Worked example (flat space, at rest).** Let $U=0$, $m>0$, and look for solutions that depend on $x_4$ only, $\Psi=e^{-i\omega x_4}u$. The equation is $\gamma^4(-i\omega)u=mu$, that is $-i\gamma^4u=(m/\omega)u$. The matrix $-i\gamma^4$ is Hermitian (Section 8.9) with square $1$, so its eigenvalues are $\pm1$: the solutions have $\omega=+m$ with $-i\gamma^4u=u$, or $\omega=-m$ with $-i\gamma^4u=-u$. The column $u_+=\tfrac12(e_0-e_4-ie_9-ie_{13})$ of Section 8.8 is of the first kind. Check with the tables of Section 2.8: $(\gamma^4u_+)_0=-(u_+)_{13}=\tfrac i2$, so $(-i\gamma^4u_+)_0=\tfrac12=(u_+)_0$, and in the same way for the components 4, 9 and 13.

### 7.5 The conserved current and the charge

**Theorem 7.1 (the current identity).** For both kinds of components, every potential and every vielbein, and for every field configuration (not only solutions), with $E:=\gamma^\mu D_\mu\Psi-M_{\mathrm{eff}}\Psi$ and $\bar E:=(D_\mu\bar\Psi)\gamma^\mu+M_{\mathrm{eff}}\bar\Psi$,

$$
\partial_\mu\bigl(\sqrt{|g|}\,\bar\Psi\gamma^\mu\Psi\bigr)=\sqrt{|g|}\,\bigl((D_\mu\bar\Psi)\gamma^\mu\Psi+\bar\Psi\gamma^\mu D_\mu\Psi\bigr)=\sqrt{|g|}\,\bigl(\bar E\,\Psi+\bar\Psi\,E\bigr).
$$

*Proof.* The product rule gives $\partial_\mu(\sqrt{|g|}\,\bar\Psi\gamma^\mu\Psi)=\sqrt{|g|}(\partial_\mu\bar\Psi)\gamma^\mu\Psi+\bar\Psi\,\partial_\mu(\sqrt{|g|}\gamma^\mu)\,\Psi+\sqrt{|g|}\,\bar\Psi\gamma^\mu\partial_\mu\Psi$. By (B6) the middle term is $\sqrt{|g|}\,\bar\Psi(\gamma^\mu\Omega_\mu-\Omega_\mu\gamma^\mu)\Psi$. Collecting, $(\partial_\mu\bar\Psi-\bar\Psi\Omega_\mu)\gamma^\mu\Psi+\bar\Psi\gamma^\mu(\partial_\mu\Psi+\Omega_\mu\Psi)$, which is the first equality. For the second, $\bar E\Psi+\bar\Psi E=(D_\mu\bar\Psi)\gamma^\mu\Psi+M_{\mathrm{eff}}S+\bar\Psi\gamma^\mu D_\mu\Psi-M_{\mathrm{eff}}S$ ($M_{\mathrm{eff}}$ commutes with the components). No factor was reordered, so the proof holds for both statistics. $\square$

(Theorem M1 of the matter–antimatter document, §4.1, item 3; checks `MA_M1_noetherIdentity_commuting_G1` and `MA_M1_noetherIdentity_grassmann_G1`, the latter with 1088 monomials at each G1 point; and, as a negative control, the identity fails with the notebook's contraction of the spin connection, because the divergence identity fails for it, check `MA_M1_negativeControlNotebookConnection`.) The first equality is also the identity used in Section 6.5 to show that the unsymmetrized kinetic term differs from $K$ by an imaginary total derivative.

**The Hermitian current.** The vector $\bar\Psi\gamma^\mu\Psi=\Psi^\dagger(C\gamma^\mu)\Psi$ has an anti-Hermitian matrix, so for commuting components it is purely imaginary (Lemma 6.1). The project therefore uses

$$
J^\mu:=-i\,\bar\Psi\gamma^\mu\Psi,
$$

whose matrices $-iC\gamma^\mu$ are Hermitian: $(-iC\gamma^\mu)^\dagger=i(C\gamma^\mu)^T=-iC\gamma^\mu$. $J^\mu$ is real for commuting components and Hermitian for Grassmann components (checks `QNT_currentHermiticity`, `GR_currentHermitian`; `C00_current_conservationAndReality`, which records that $\bar\Psi\gamma^\mu\Psi$ is purely imaginary for commuting fields).

**Conservation.** On every solution $E=\bar E=0$, so Theorem 7.1 gives $\partial_\mu(\sqrt{|g|}\,J^\mu)=0$, which is $\nabla_\mu J^\mu=0$ because $\nabla_\mu J^\mu=\partial_\mu J^\mu+\Gamma^\mu{}_{\mu\lambda}J^\lambda$ and $\Gamma^\mu{}_{\mu\lambda}=\partial_\lambda\ln\sqrt{|g|}$ (Section 5.8). The current is the Noether current of the phase symmetry of Section 6.9: with $\Delta\Psi=i\Psi$ and $\Delta\Psi^\ast=-i\Psi^\ast$, the formula of Theorem 5.2 and the momenta of Section 7.2 give $\tfrac12\sqrt{|g|}\bar\Psi\gamma^\mu(i\Psi)+(-i\Psi^\dagger)\bigl(-\tfrac12\sqrt{|g|}C\gamma^\mu\Psi\bigr)=i\sqrt{|g|}\,\bar\Psi\gamma^\mu\Psi=-\sqrt{|g|}\,J^\mu$: the same current up to the constant factor $-1$, whose sign is a convention (Section 5.7). The Stage-5 verifiers find $\partial_\mu(\sqrt{|g|}J^\mu)=0$ on shell and $\ne0$ off shell at all test points, also for an arbitrary smooth $U$ (checks `C00_current_conservationAndReality`, `C00_EMT_generalSmoothU`, and their `S5_` twins).

**The charge.** For a slice $x_4=\text{const}$ define

$$
Q(x_4)=\int\sqrt{|g|}\,J^{x_4}\,d^7x .
$$

The argument is the one of Section 5.7, with $\sqrt{|g|}\,J^\mu$ in place of $j^\mu$. Differentiate under the integral sign and use the conservation law $\partial_4(\sqrt{|g|}J^{x_4})=-\sum_{j\ne4}\partial_j(\sqrt{|g|}J^{x_j})$:

$$
\frac{dQ}{dx_4}=\int\partial_4\bigl(\sqrt{|g|}\,J^{x_4}\bigr)\,d^7x=-\sum_{j\ne4}\int\partial_j\bigl(\sqrt{|g|}\,J^{x_j}\bigr)\,d^7x=0 .
$$

Each of the seven integrals on the right vanishes by the divergence theorem of Section 5.3, applied on the seven-dimensional slice (do the $x_j$ integral first, by the fundamental theorem of calculus), provided the current vanishes far away; if instead the slice is closed up periodically, the two end values in that integral are equal and cancel. So $Q$ does not change with $x_4$. In a frame with $\gamma^{x_4}=\gamma^4$, the density is

$$
J^4=-i\,\Psi^\dagger C\gamma^4\Psi=\Psi^\dagger B\Psi,\qquad B=-iC\gamma^4 ,
$$

the matrix of Section 2.12, Hermitian with eight eigenvalues $+1$ and eight $-1$.

**The charge of dirac16complex00 has no sign.** For commuting components $J^4$ is an ordinary number that can be positive, negative or zero. Two exact examples from the report: for $\Psi=i\,e_6+e_{15}$, $J^4=+2=\Psi^\dagger\Psi$; for $\Psi=-i\,e_6+e_{15}$, $J^4=-2=-\Psi^\dagger\Psi$ (check `C00_charge_indefinite`). With the table of $B$ in Section 2.9, $(Bu)_6=i\,u_{15}$ and $(Bu)_{15}=-i\,u_6$, so for $\Psi=c_6e_6+c_{15}e_{15}$ one gets $J^4=c_6^\ast\,i\,c_{15}-c_{15}^\ast\,i\,c_6$; for $c_6=i$, $c_{15}=1$ this is $(-i)(i)-(1)(i)(i)=1+1=2$. This is not an accident of the choice $B$: Section 8.8 shows that every candidate charge density built from a Spin(4,4)-invariant form has as many negative as positive eigenvalues. So the reading of Dirac's 1928 theory, in which the time component of the conserved current is a probability density, **fails for dirac16complex00 in signature (4,4)** (`dirac16complex00-theory.json`, key `commutingFieldSpecifics.chargeIndefinite`). For the quantized dirac16complex the same indefinite $B$ is the matrix of the canonical anticommutator (Section 8.6). Chapter 8 then restricts to the **good sector**, the fields that do not depend on the three extra times $x_5,x_6,x_7$ (Section 8.10). There the field is expanded in operators $b$ that annihilate particles and $d$ that annihilate antiparticles, with $b^\ast$, $d^\ast$ creating them, and after **normal ordering** (the prescription that removes the constant contribution of the filled sea of negative-energy states, the "Dirac sea") the charge becomes $Q=\sum(b^\ast b-d^\ast d)$, summed over all modes: each particle carries $+1$ and each antiparticle $-1$ (Section 8.12). This paragraph is a preview; Chapter 8 derives it.

### 7.6 The energy–momentum tensor: what is varied

**The definition.** Section 5.8 defined the energy–momentum tensor by the response of the action to a small change of the metric,

$$
T_{\mu\nu}:=-\frac{2}{\sqrt{|g|}}\,\frac{\delta\mathcal S}{\delta g^{\mu\nu}},
$$

with the sign chosen so that $T_{44}$ is the energy density; here $\mathcal S=\int\mathcal L\,d^8x$ is the action (we write $\mathcal S$ to keep the letter $S$ for the scalar density $\bar\Psi\Psi$). It is the source in Einstein's equations (Chapter 4). For a spinor field there is a difficulty: the action depends on the vielbein, not only on the metric, and the spinor components are measured in the frame of the vielbein. We therefore change the vielbein, in a way that changes the metric by the prescribed amount and does not turn the frame.

**Every change of the vielbein.** Any small change of the vielbein can be written as

$$
\delta e_\mu{}^c=X^c{}_d(x)\,e_\mu{}^d,\qquad X^c{}_d:=\delta e_\mu{}^c\,e_d{}^\mu ,
$$

with a matrix $X(x)$ of small numbers; we lower its first index with $\eta$, $X_{cd}:=\eta_{ce}X^e{}_d$. The metric $g_{\mu\nu}=e_\mu{}^c\eta_{cd}e_\nu{}^d$ changes by

$$
\delta g_{\mu\nu}=X^c{}_{c'}e_\mu{}^{c'}\eta_{cd}e_\nu{}^d+e_\mu{}^c\eta_{cd}X^d{}_{d'}e_\nu{}^{d'}=e_\mu{}^c\,e_\nu{}^d\,\bigl(X_{cd}+X_{dc}\bigr).
$$

Only the symmetric part of $X$ changes the metric. The antisymmetric part is an infinitesimal frame rotation: a matrix $\Lambda=1+X$ satisfies $\Lambda^T\eta\Lambda=\eta$ to first order exactly when $\eta X+(\eta X)^T=0$ (Section 4.10). For a prescribed $\delta g_{\mu\nu}$ there is exactly one **symmetric** $X$, namely $X_{cd}=\tfrac12e_c{}^\mu e_d{}^\nu\,\delta g_{\mu\nu}$. The energy–momentum tensor is computed with this symmetric change and with the spinor components held fixed. (This is the rule $\delta e_a{}^\mu=\tfrac12e_{a\nu}\,\delta g^{\mu\nu}$ of the Stage-1 document, §9.1, written for the vielbein instead of its inverse.)

**What has to be computed.** From $\delta g^{\mu\nu}=-g^{\mu\alpha}g^{\nu\beta}\delta g_{\alpha\beta}$ (vary $g^{\mu\alpha}g_{\alpha\nu}=\delta^\mu{}_\nu$ as in Section 5.8), the definition is the same as $\delta\mathcal S=\tfrac12\int\sqrt{|g|}\,T^{\mu\nu}\delta g_{\mu\nu}\,d^8x$. Inserting $\delta g_{\mu\nu}=2e_\mu{}^ce_\nu{}^dX_{cd}$ for symmetric $X$,

$$
\delta\mathcal S=\int\sqrt{|g|}\;T^{cd}\,X_{cd}\;d^8x,\qquad T^{cd}:=e_\mu{}^c\,e_\nu{}^d\,T^{\mu\nu}\ \ (\text{the frame components}).
$$

So we must compute the first-order change of $\sqrt{|g|}\,\mathcal L_s$ when the vielbein changes by a symmetric $X$ and $\Psi$ is held fixed, and read off the coefficient of $X_{cd}$.

### 7.7 The energy–momentum tensor: the derivation

We write $\partial_a:=e_a{}^\mu\partial_\mu$ and $D_a:=e_a{}^\mu D_\mu$ for derivatives along the frame directions, raise frame indices with $\eta$ ($D^a=\eta^{ab}D_b$, $\gamma_a=\eta_{ab}\gamma^b$), and put $e_{\nu a}:=\eta_{ad}\,e_\nu{}^d$.

**Step 1 (volume and inverse vielbein).** $\sqrt{|g|}=|\det e|$ (Section 4.10). Jacobi's formula of Section 5.8 gives $\delta\ln|\det e|=e_a{}^\mu\,\delta e_\mu{}^a=e_a{}^\mu X^a{}_de_\mu{}^d=X^a{}_a$, so

$$
\delta\sqrt{|g|}=\sqrt{|g|}\,X^a{}_a=\sqrt{|g|}\,\eta^{cd}X_{cd}.
$$

Varying $e_c{}^\mu e_\mu{}^b=\delta_c{}^b$ gives $\delta e_c{}^\mu=-X^d{}_c\,e_d{}^\mu$.

**Step 2 (what depends on the vielbein).** Split the kinetic term into its derivative part and its connection part (Theorem 6.4),

$$
K=K_\partial+K_\Omega,\qquad K_\partial=\tfrac12\,e_a{}^\mu\bigl(\bar\Psi\gamma^a\partial_\mu\Psi-\partial_\mu\bar\Psi\,\gamma^a\Psi\bigr),\qquad K_\Omega=\tfrac14\,\omega_{cab}\,A^{cab},
$$

where $\omega_{cab}=e_c{}^\mu\omega_{\mu ab}$ and $A^{cab}:=\bar\Psi\{\gamma^c,S^{ab}\}\Psi$. By Lemma 6.3, $A^{cab}$ vanishes unless $c,a,b$ are distinct and is then $\bar\Psi\gamma^c\gamma^a\gamma^b\Psi$: it is **totally antisymmetric** in its three indices, and it contains no vielbein. Neither do $S$ and $U(S)$. So

$$
\delta\bigl(\sqrt{|g|}\,\mathcal L_s\bigr)=\sqrt{|g|}\,\bigl(\eta^{cd}X_{cd}\,\mathcal L_s+\delta K_\partial+\delta K_\Omega\bigr).
$$

**Step 3 (the derivative part).** Only the explicit inverse vielbein changes: $\delta K_\partial=-X^d{}_a\cdot\tfrac12\bigl(\bar\Psi\gamma^a\partial_d\Psi-\partial_d\bar\Psi\,\gamma^a\Psi\bigr)$. Write $X^d{}_a=\eta^{de}X_{ea}$ and use the symmetry of $X$ to replace the coefficient of $X_{ea}$ by its symmetric part:

$$
\delta K_\partial=-\tfrac14\,X_{ea}\Bigl(\bar\Psi\gamma^a\partial^e\Psi+\bar\Psi\gamma^e\partial^a\Psi-\partial^e\bar\Psi\,\gamma^a\Psi-\partial^a\bar\Psi\,\gamma^e\Psi\Bigr).
$$

**Step 4 (the connection in terms of the vielbein).** Define

$$
F_{cab}:=e_c{}^\mu\,e_b{}^\nu\,\partial_\mu e_{\nu a},
$$

the derivative of the vielbein along the frame direction $c$, with its two indices converted to frame indices $a$ and $b$.

**Lemma 7.2.** (i) For every totally antisymmetric $A^{cab}$, $A^{cab}\omega_{cab}=-A^{cab}F_{cab}$. (ii) For all $d,c,f$,

$$
\omega_{dcf}=\tfrac12\bigl(-F_{dcf}+F_{dfc}+F_{fcd}+F_{fdc}-F_{cfd}-F_{cdf}\bigr).
$$

*Proof.* Section 4.11 wrote the canonical connection as $\omega_{\mu ab}=e_a{}^\sigma e_b{}^\nu\,\Gamma_{\sigma\mu\nu}-e_b{}^\nu\,\partial_\mu e_{\nu a}$, with $\Gamma_{\sigma\mu\nu}=g_{\sigma\rho}\Gamma^\rho{}_{\mu\nu}$. Contracting with $e_c{}^\mu$,

$$
\omega_{cab}=G_{cab}-F_{cab},\qquad G_{cab}:=e_c{}^\mu e_a{}^\sigma e_b{}^\nu\,\Gamma_{\sigma\mu\nu}.
$$

(i) $\Gamma_{\sigma\mu\nu}$ is symmetric in $\mu,\nu$, so $G_{cab}$ is symmetric in $c,b$, and its contraction with $A^{cab}$, which is antisymmetric in $c,b$, vanishes. (ii) We express $G$ through $F$. From $g_{\nu\sigma}=e_\nu{}^be_{\sigma b}$ and the product rule, $\partial_\mu g_{\nu\sigma}=(\partial_\mu e_{\nu b})e_\sigma{}^b+e_\nu{}^b\,\partial_\mu e_{\sigma b}$. Contracting with $e_x{}^\mu e_y{}^\nu e_z{}^\sigma$ and using $e_z{}^\sigma e_\sigma{}^b=\delta_z{}^b$,

$$
e_x{}^\mu e_y{}^\nu e_z{}^\sigma\,\partial_\mu g_{\nu\sigma}=F_{xzy}+F_{xyz}.
$$

Now $\Gamma_{\sigma\mu\nu}=\tfrac12(\partial_\mu g_{\nu\sigma}+\partial_\nu g_{\mu\sigma}-\partial_\sigma g_{\mu\nu})$ (Section 4.5). Contract with $e_d{}^\mu e_c{}^\sigma e_f{}^\nu$ and apply the last formula to each of the three terms (derivative directions $d$, $f$, $c$ respectively):

$$
G_{dcf}=\tfrac12\bigl(F_{dcf}+F_{dfc}+F_{fcd}+F_{fdc}-F_{cfd}-F_{cdf}\bigr),
$$

and $\omega_{dcf}=G_{dcf}-F_{dcf}$ is the claim. $\square$

**Corollary 7.3.** If $A^{acf}$ is antisymmetric in $c,f$, then $\omega_{dcf}A^{acf}=-\bigl(F_{dcf}+F_{cfd}+F_{cdf}\bigr)A^{acf}$.

*Proof.* Group the six terms of Lemma 7.2 (ii) as $\tfrac12\bigl[(F_{dfc}-F_{dcf})+(F_{fcd}-F_{cfd})+(F_{fdc}-F_{cdf})\bigr]$. In each pair the first term is the second with $c$ and $f$ exchanged. After contraction with $A^{acf}$ and renaming the summation indices $c\leftrightarrow f$ in the first term, $A^{afc}=-A^{acf}$ turns each pair into twice the negative of its second term. $\square$

**Step 5 (the connection part).** $K_\Omega=\tfrac14A^{cab}\omega_{cab}=-\tfrac14A^{cab}F_{cab}$ by Lemma 7.2 (i), and $A$ does not change, so $\delta K_\Omega=-\tfrac14A^{cab}\,\delta F_{cab}$. Vary the three factors of $F_{cab}$, using Step 1 and $\delta e_{\nu a}=X_{ad}\,e_\nu{}^d$:

$$
\begin{aligned}
\delta F_{cab}&=\delta e_c{}^\mu\,e_b{}^\nu\,\partial_\mu e_{\nu a}+e_c{}^\mu\,\delta e_b{}^\nu\,\partial_\mu e_{\nu a}+e_c{}^\mu e_b{}^\nu\,\partial_\mu\bigl(X_{ad}\,e_\nu{}^d\bigr)\\
&=-X^d{}_c\,F_{dab}-X^d{}_b\,F_{cad}+\partial_cX_{ab}+X_a{}^d\,F_{cdb}.
\end{aligned}
$$

(In the last term, $X_{ad}\,e_c{}^\mu e_b{}^\nu\partial_\mu e_\nu{}^d=X_{ad}\eta^{de}F_{ceb}$.) The term $\partial_cX_{ab}$, the only one with a derivative of $X$, is symmetric in $a,b$; contracted with $A^{cab}$, which is antisymmetric in $a,b$, it vanishes. In the remaining three terms we rename the summation indices so that $X$ always carries the first index of $A^{acf}$. A summation index is a dummy: it may be given any letter not used elsewhere in the term. We treat the three terms one at a time.

- First term. Rename $c\to a$, $a\to c$, $b\to f$ (all three at once):

$$
-A^{cab}X^d{}_c\,F_{dab}=-A^{acf}X^d{}_a\,F_{dcf} .
$$

- Second term. Rename $b\to a$, $a\to f$ and keep $c$; then use that $A$ does not change under the cyclic shift of its three indices, $A^{cfa}=A^{acf}$ (a cyclic shift is two exchanges, each of which costs a sign):

$$
-A^{cab}X^d{}_b\,F_{cad}=-A^{cfa}X^d{}_a\,F_{cfd}=-A^{acf}X^d{}_a\,F_{cfd} .
$$

- Third term. Exchange the first two indices of $A$, $A^{cab}=-A^{acb}$; rename $b\to f$; and use $X_a{}^d=\eta^{de}X_{ae}=\eta^{de}X_{ea}=X^d{}_a$ for symmetric $X$:

$$
+A^{cab}X_a{}^d\,F_{cdb}=-A^{acb}X_a{}^d\,F_{cdb}=-A^{acf}X^d{}_a\,F_{cdf} .
$$

Adding the three lines and using Corollary 7.3 (with $A^{acf}$ antisymmetric in $c,f$),

$$
A^{cab}\,\delta F_{cab}=-X^d{}_a\,A^{acf}\bigl(F_{dcf}+F_{cfd}+F_{cdf}\bigr)=X^d{}_a\,\omega_{dcf}\,A^{acf} .
$$

Hence

$$
\delta K_\Omega=-\tfrac14\,X^d{}_a\,\omega_{dcf}\,A^{acf}.
$$

Finally we write this with the spinor connection. The frame component $\Omega_d:=e_d{}^\mu\Omega_\mu=\tfrac12\omega_{dcf}S^{cf}$ gives $\bar\Psi\{\gamma^a,\Omega_d\}\Psi=\tfrac12\omega_{dcf}A^{acf}$, so $\delta K_\Omega=-\tfrac12X^d{}_a\bar\Psi\{\gamma^a,\Omega_d\}\Psi$. With $X^d{}_a=\eta^{de}X_{ea}$, $\Omega^e=\eta^{ed}\Omega_d$ and the symmetry of $X$,

$$
\delta K_\Omega=-\tfrac14\,X_{ea}\Bigl(\bar\Psi\gamma^a\Omega^e\Psi+\bar\Psi\Omega^e\gamma^a\Psi+\bar\Psi\gamma^e\Omega^a\Psi+\bar\Psi\Omega^a\gamma^e\Psi\Bigr).
$$

**Step 6 (collect).** Adding Steps 3 and 5, the connection terms complete the derivatives to covariant ones: $\bar\Psi\gamma^a(\partial^e+\Omega^e)\Psi=\bar\Psi\gamma^aD^e\Psi$ and $-(\partial^e\bar\Psi-\bar\Psi\Omega^e)\gamma^a\Psi=-(D^e\bar\Psi)\gamma^a\Psi$. So

$$
\delta\bigl(\sqrt{|g|}\,\mathcal L_s\bigr)=\sqrt{|g|}\,X_{ea}\Bigl[\eta^{ea}\mathcal L_s-\tfrac14\bigl(\bar\Psi\gamma^aD^e\Psi+\bar\Psi\gamma^eD^a\Psi-(D^e\bar\Psi)\gamma^a\Psi-(D^a\bar\Psi)\gamma^e\Psi\bigr)\Bigr].
$$

No integration by parts was needed: the derivatives of $X$ dropped out in Step 5, so this holds at every point. The bracket is symmetric in $e,a$, so by Section 7.6 it is $T^{ea}$. Converting to coordinate indices with $T_{\mu\nu}=e_{\mu c}e_{\nu d}T^{cd}$, where $e_{\mu c}\gamma^c=\gamma_\mu=g_{\mu\nu}\gamma^\nu$ and $e_{\nu d}D^d=D_\nu$:

**Theorem 7.4 (the energy–momentum tensor).** For both fields, in every gravitational field,

$$
T_{\mu\nu}=-\tfrac14\Bigl[\bar\Psi\gamma_\mu D_\nu\Psi+\bar\Psi\gamma_\nu D_\mu\Psi-(D_\mu\bar\Psi)\gamma_\nu\Psi-(D_\nu\bar\Psi)\gamma_\mu\Psi\Bigr]+g_{\mu\nu}\,\mathcal L_s .
$$

This is the formula of the Stage-1 document (§9.2) and of `handoff/specs/CONTRACT.md` (§7). For dirac16complex every step above is a statement about bilinears in which $\Psi^\dagger$ stays to the left of $\Psi$, so the same tensor results with Grassmann components; after quantization it is an operator, normal-ordered with respect to the Dirac sea as in Chapter 8. For dirac16complex00 it is an ordinary real symmetric tensor field.

**How the repository checks it.** Stage 1 carried out the metric variation explicitly for diagonal frames (checks `EMT_variation_G3` and `EMT_variation`). Stage 5 computed the full functional derivative $\delta\mathcal S/\delta e_\mu{}^a$, including the change of the spin connection, exactly at points of two general non-diagonal frames (G1, and a further integer frame G4) and of a homogeneous frame: its symmetric part equals $\sqrt{|g|}\,T^{\mu\nu}$ of Theorem 7.4 in all 36 independent components **off shell**, its antisymmetric part (the frame-rotation part) is nonzero off shell and vanishes on shell. The derivative with respect to the derivatives of the vielbein was computed in closed form and compared with an exact linearisation in all 512 directions at each point; the Wolfram verifier also recomputed the functional derivative independently by a generic jet identity, for all 64 entries at the G4 point and for three spot entries at the point G1 p1 (at the homogeneous point it lists no spot entries) (checks `C00_EMT_vielbeinVariation` and `S5_EMT_vielbeinVariation`; measurement `jetIdentitySpotEntries` of the Wolfram report). The report notes that this lifts a limitation of Stage 1, which had not varied the off-diagonal components explicitly.

### 7.8 Properties of the energy–momentum tensor

**Symmetric.** $T_{\mu\nu}=T_{\nu\mu}$: the formula is visibly unchanged when $\mu$ and $\nu$ are exchanged.

**Real (Hermitian).** Group the bracket as $\bigl[\bar\Psi\gamma_\mu D_\nu\Psi-(D_\nu\bar\Psi)\gamma_\mu\Psi\bigr]+\bigl[\bar\Psi\gamma_\nu D_\mu\Psi-(D_\mu\bar\Psi)\gamma_\nu\Psi\bigr]$. Exactly as for $K$ in Theorem 6.2, the conjugate of $\bar\Psi\gamma_\mu D_\nu\Psi=\Psi^\dagger(C\gamma_\mu)D_\nu\Psi$ is $-(D_\nu\bar\Psi)\gamma_\mu\Psi$, because $C\gamma_\mu$ is real and antisymmetric; so each bracket is of the form $Y+Y^\ast$. And $\mathcal L_s$ is real (Theorem 6.2). (Checks `EMT_symmetricHermitian_G1`, `EMT_symmetricHermitian_G2`, `GR_emtHermitian`, `C00_EMT_symmetricAndReal`, `S5_EMT_symmetricAndReal`.)

**Trace.** Contract with $g^{\mu\nu}$: $g^{\mu\nu}\gamma_\mu=\gamma^\nu$, so the bracket becomes $2\bar\Psi\gamma^\nu D_\nu\Psi-2(D_\nu\bar\Psi)\gamma^\nu\Psi=4K$, and $g^{\mu\nu}g_{\mu\nu}=8$. Therefore, off shell and on shell,

$$
T^\mu{}_\mu=-K+8\,\mathcal L_s,\qquad\text{and on shell}\qquad T^\mu{}_\mu=-M_{\mathrm{eff}}S+8\bigl(SU'-U\bigr)=-mS+7SU'(S)-8U(S),
$$

which is $-mS+3\lambda S^2$ for the default potential. (Checks `EMT_traceOffShellIdentity_G1`, `EMT_trace_G1`, `EMT_trace_G2` of Stage 1; `C00_EMT_traceOnShell` and `S5_EMT_traceOnShell`, whose recorded on-shell values include $923549/26880$ at the Wolfram point G1 p1; for a general smooth $U$ in `C00_EMT_generalSmoothU`.)

**Theorem 7.5 (conservation).** On every solution of the field equations, for both fields, $\nabla_\mu T^{\mu\nu}=0$.

The proof uses the fact that the action does not depend on the coordinates. We give it in five steps.

*Step 1 (a change of coordinates changes the fields).* Let $\xi^\mu(x)$ be a small vector field that vanishes near the boundary of the region, and introduce new coordinates $x'^\mu=x^\mu-\xi^\mu(x)$. By the transformation rule of covectors (Section 4.3), the vielbein in the new coordinates is $e'_\mu{}^a(x')=\frac{\partial x^\nu}{\partial x'^\mu}e_\nu{}^a(x)$, and the spinor components, which refer to the frame and not to the coordinates, are unchanged: $\Psi'(x')=\Psi(x)$. To first order $x=x'+\xi(x')$ and $\partial x^\nu/\partial x'^\mu=\delta^\nu{}_\mu+\partial_\mu\xi^\nu$, so, as functions of their argument,

$$
e'_\mu{}^a=e_\mu{}^a+\delta_\xi e_\mu{}^a,\quad \delta_\xi e_\mu{}^a=\xi^\lambda\partial_\lambda e_\mu{}^a+e_\lambda{}^a\,\partial_\mu\xi^\lambda;\qquad \Psi'=\Psi+\delta_\xi\Psi,\quad \delta_\xi\Psi=\xi^\lambda\partial_\lambda\Psi .
$$

The action is the same integral written in other coordinates ($\mathcal L_s$ is a scalar and $\sqrt{|g|}\,d^8x$ is invariant, Section 6.9), and the region is mapped onto itself because $\xi$ vanishes near its boundary. Renaming the integration variable, $\mathcal S[e',\Psi']=\mathcal S[e,\Psi]$, so the first-order change vanishes: $\delta_\xi\mathcal S=0$.

*Step 2 (split the change of the vielbein).* Insert the vielbein postulate of Section 4.11, $\partial_\lambda e_\mu{}^c=\Gamma^\rho{}_{\lambda\mu}e_\rho{}^c-\omega_\lambda{}^c{}_d\,e_\mu{}^d$:

$$
\delta_\xi e_\mu{}^c=e_\rho{}^c\bigl(\partial_\mu\xi^\rho+\Gamma^\rho{}_{\mu\lambda}\xi^\lambda\bigr)-\xi^\lambda\omega_\lambda{}^c{}_d\,e_\mu{}^d=e_\rho{}^c\,\nabla_\mu\xi^\rho-\xi^\lambda\omega_\lambda{}^c{}_d\,e_\mu{}^d .
$$

In the notation of Section 7.6, $X_{cd}=e_c{}^\sigma e_d{}^\mu\,\nabla_\mu\xi_\sigma-\xi^\lambda\omega_{\lambda cd}$ (with $\xi_\sigma=g_{\sigma\rho}\xi^\rho$). Its symmetric part is $X^{\mathrm S}_{cd}=\tfrac12e_c{}^\sigma e_d{}^\mu(\nabla_\mu\xi_\sigma+\nabla_\sigma\xi_\mu)$, and its antisymmetric part $\varepsilon_{cd}$ is the rest (it contains the whole $\omega$ term, because $\omega_{\lambda cd}$ is antisymmetric).

*Step 3 (three changes).* To first order, changes add. So the change $(\delta_\xi e,\delta_\xi\Psi)$ is the sum of: (1) the symmetric change $X^{\mathrm S}$ of the vielbein with $\Psi$ fixed; (2) the frame rotation $\varepsilon$ of the vielbein together with the spin rotation $\delta\Psi=\tfrac12\varepsilon_{cd}S^{cd}\Psi$ that covers it (by Section 4.13, $[\tfrac12\varepsilon_{cd}S^{cd},\gamma^a]=-\varepsilon^a{}_b\gamma^b$, the infinitesimal form of the covering relation); (3) the change $\delta_3\Psi=\xi^\lambda\partial_\lambda\Psi-\tfrac12\varepsilon_{cd}S^{cd}\Psi$ of the field alone. The change (1) contributes $\int\sqrt{|g|}\,T^{cd}X^{\mathrm S}_{cd}\,d^8x=\int\sqrt{|g|}\,T^{\sigma\mu}\nabla_\mu\xi_\sigma\,d^8x$ (Section 7.6, and $T$ is symmetric). The change (2) contributes nothing: it is an infinitesimal local frame rotation, under which $\mathcal L$ is invariant (Section 6.9, differentiated at zero rotation angle). The change (3) is a change of the field alone that vanishes near the boundary; by Sections 5.3 and 5.10 it changes the action by the integral of the Euler–Lagrange expressions times the change, which is zero on a solution.

*Step 4 (the result of Steps 1 to 3).* On every solution, for every small $\xi$ vanishing near the boundary,

$$
0=\int\sqrt{|g|}\;T^{\sigma\mu}\,\nabla_\mu\xi_\sigma\;d^8x .
$$

*Step 5 (integrate by parts).* By the product rule, $T^{\sigma\mu}\nabla_\mu\xi_\sigma=\nabla_\mu(T^{\sigma\mu}\xi_\sigma)-(\nabla_\mu T^{\sigma\mu})\,\xi_\sigma$. For any vector field $V^\mu$, $\sqrt{|g|}\,\nabla_\mu V^\mu=\partial_\mu(\sqrt{|g|}\,V^\mu)$ (the computation used for the current in Section 7.5), so the first term integrates to zero by the divergence theorem. Hence $\int\sqrt{|g|}\,(\nabla_\mu T^{\sigma\mu})\,\xi_\sigma\,d^8x=0$ for every $\xi$, and the fundamental lemma of Section 5.2 (applied to each component) gives $\nabla_\mu T^{\sigma\mu}=0$. $\square$

For Grassmann components the same proof applies: the changes (1) and (2) involve only ordinary functions multiplying bilinears in the fixed order, and the first-order change of the action under the change (3) of the odd field is again the integral of the Euler–Lagrange expressions times the change (Section 5.10). The repository verifies the conservation with exact on-shell field data at the three G1 points and at three points of the primordial field, and checks that the divergence is not zero for data that do not satisfy the field equations (checks `EMT_conservation_G1` and `EMT_conservation_G2` of Stage 1; `C00_EMT_conservationOnShell` and `S5_EMT_conservationOnShell`, including a general smooth $U$).

### 7.9 Energy density, pressures, kinetic and potential energy, equations of state

**The observer.** From here on the time is **Gaussian normal**: $g_{44}=-1$ and $g_{4i}=0$ for $i\ne4$, and the frame's time direction is aligned with $x_4$, so $\gamma^{x_4}=\gamma^4$ and $\gamma_4=g_{44}\gamma^{x_4}=-\gamma^4$ (the homogeneous frames, the primordial field and its static member have this form; Section 4.6 defines it). The observer at rest in these coordinates has the 8-velocity $u=\partial_4$, a unit time-like vector.

**Definitions** (Stage-1 document, §9.4). The energy density, the pressure along each of the seven transverse directions, their mean, and the equation-of-state parameters are

$$
\begin{aligned}
&\rho:=T_{\mu\nu}u^\mu u^\nu=T_{44}=-T^4{}_4,\qquad p_{(i)}:=T^i{}_i\ \ (\text{no sum},\ i\ne4),\\
&\bar p=\tfrac17\sum_{i\ne4}p_{(i)},\qquad w_{(i)}=\frac{p_{(i)}}\rho,\qquad \bar w=\frac{\bar p}\rho .
\end{aligned}
$$

When all seven pressures are equal we write $p$ and $w=p/\rho$. Four of the transverse directions are space-like ($i=0,1,2,3$) and three are time-like ($i=5,6,7$). For the space-like ones, $T^i{}_i$ is the flux of momentum along $i$ through a surface of constant $x_i$, the usual pressure; for a scalar field in the homogeneous case it is $\tfrac12\dot\phi^2-V$ (Section 5.8). For the time-like transverse directions the same formula is used by definition; there is no everyday meaning of a pressure along a time.

**The energy density.** Use $\gamma_4=-\gamma^4$ and $g_{44}=-1$ in Theorem 7.4 with $\mu=\nu=4$:

$$
\rho=T_{44}=-\tfrac14\bigl[2\bar\Psi\gamma_4D_4\Psi-2(D_4\bar\Psi)\gamma_4\Psi\bigr]-\mathcal L_s=K_4-\mathcal L_s,
$$

with the time part and the transverse part of the kinetic term

$$
K_4:=\tfrac12\bigl(\bar\Psi\gamma^4D_4\Psi-(D_4\bar\Psi)\gamma^4\Psi\bigr),\qquad K_\perp:=\tfrac12\sum_{\mu\ne4}\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr),\qquad K=K_4+K_\perp .
$$

Since $\mathcal L_s=K_4+K_\perp-mS-U$,

$$
\rho=T_{44}=-K_\perp+mS+U(S)\qquad\text{identically (off shell)}.
$$

**The time part is the oscillator of Section 5.6.** With $C\gamma^4=iB$ (from $B=-iC\gamma^4$), $\bar\Psi\gamma^4=i\Psi^\dagger B$ and $(D_4\bar\Psi)\gamma^4=i(D_4\Psi)^\dagger B$, so

$$
K_4=\tfrac i2\Bigl(\Psi^\dagger B\,D_4\Psi-(D_4\Psi)^\dagger B\,\Psi\Bigr).
$$

With $B$ replaced by $1$ this is exactly the time part $\tfrac i2(\psi^\ast\dot\psi-\dot\psi^\ast\psi)$ of the complex oscillator of Section 5.6. The indefinite matrix $B$ is where signature (4,4) enters.

**Two splits into kinetic and potential energy** (Stage-1 document, §9.5; `handoff/specs/CONTRACT.md`, §7).

- **(A) Lagrangian split:** $\mathrm{KE}_L:=\tfrac12K_4$ and $\mathrm{PE}_L:=\rho-\mathrm{KE}_L$. This imitates the scalar field, whose kinetic energy $\tfrac12\dot\phi^2$ is half of the time-derivative term $\dot\phi\,\partial\mathcal L/\partial\dot\phi$ of its Lagrangian; by definition $\rho=\mathrm{KE}_L+\mathrm{PE}_L$.
- **(B) Hamiltonian split:** $\mathrm{KE}_H:=-K_\perp$ (the energy of gradients and of the transverse connection) and $\mathrm{PE}_H:=mS+U(S)$ (rest energy and interaction). Then $\rho=\mathrm{KE}_H+\mathrm{PE}_H$ holds identically, by the formula above. The time derivatives do not appear in split (B): for a first-order field they carry no energy, as for the oscillator of Exercise 5.4.

The Stage-5 verifiers confirm $\rho=\mathrm{KE}_H+\mathrm{PE}_H$ and $\rho=K_4-\mathcal L_s$ off shell, with arbitrary field data, at three points of the primordial field (check `C00_EMT_observerSplitGaussianNormal` and its `S5_` twin; measurements `rhoEqualsKEHplusPEH_offShell` and `rhoEqualsK4minusLs_offShell`).

### 7.10 Homogeneous backgrounds

**The setting.** Take a homogeneous diagonal background (a Bianchi-I metric, as in Chapter 11),

$$
ds^2=-dx_4^2+\sum_{i\ne4}\eta_{ii}\,h_i(x_4)^2\,dx_i^2,
$$

with the Hubble rates $H_i=\partial_4h_i/h_i$, the 7-volume $V=\prod_{i\ne4}h_i=\sqrt{|g|}$ and $\Theta=\sum_{i\ne4}H_i=\partial_4\ln V$, and a field that depends on $x_4$ only, $\Psi=\Psi(x_4)$. The vielbein is diagonal with $h_4=1$, and by Section 4.11 the only nonzero connection components are $\omega_{i\,i4}=-\omega_{i\,4i}=\eta_{ii}\,\partial_4h_i$ (the pair $(i,4)$ for $\mu=i$). So $\Omega_4=0$ and $\Omega_i=\omega_{i\,i4}S^{i4}$ (both orders of the pair give equal terms, which cancels the factor $\tfrac12$).

**The transverse pressures.** For $i\ne4$ the field does not depend on $x_i$, so $D_i\Psi=\Omega_i\Psi$ and $D_i\bar\Psi=-\bar\Psi\Omega_i$. Then

$$
T_{ii}=-\tfrac14\bigl[2\bar\Psi\gamma_i\Omega_i\Psi+2\bar\Psi\Omega_i\gamma_i\Psi\bigr]+g_{ii}\mathcal L_s=-\tfrac12\bar\Psi\{\gamma_i,\Omega_i\}\Psi+g_{ii}\mathcal L_s .
$$

$\gamma_i$ is a multiple of $\gamma^i$, and $\{\gamma^i,S^{i4}\}=0$ by Lemma 6.3 (the index $i$ belongs to the pair). So $T^i{}_i=g^{ii}T_{ii}=\mathcal L_s$ for all seven transverse directions, off shell.

**The energy density.** $K_\perp=\tfrac12\sum_{i\ne4}\bar\Psi\{\gamma^{x_i},\Omega_i\}\Psi=0$ for the same reason, so $\rho=mS+U$, off shell.

**On shell** $\mathcal L_s=SU'-U$ and $K=K_4=M_{\mathrm{eff}}S$ (Section 7.4). Collecting:

$$
\begin{aligned}
&\rho=mS+U,\qquad p_{(i)}=p=SU'(S)-U(S)\ \ \text{for all seven }i\ne4,\qquad w=\frac{SU'-U}{mS+U},\\
&\mathrm{KE}_L=\tfrac12S\bigl(m+U'\bigr),\qquad \mathrm{PE}_L=\tfrac12\bigl(mS+2U-SU'\bigr),\qquad \mathrm{KE}_H=0,\qquad \mathrm{PE}_H=\rho,
\end{aligned}
$$

and therefore $\rho+p=2\,\mathrm{KE}_L=S\,M_{\mathrm{eff}}$ and $p=\mathrm{KE}_L-\mathrm{PE}_L$, so $w=(\mathrm{KE}_L-\mathrm{PE}_L)/(\mathrm{KE}_L+\mathrm{PE}_L)$, the same formula as for the scalar field. The pressure is the same in all seven directions although the scale factors $h_i$ differ. For the free field ($U=0$) $p=0$ and $w=0$: dust. For the default potential,

$$
\rho=mS+\tfrac\lambda2S^2,\qquad p=\tfrac\lambda2S^2,\qquad w=\frac{\lambda S}{2m+\lambda S},\qquad \mathrm{KE}_L=\tfrac12S(m+\lambda S),\qquad \mathrm{PE}_L=\tfrac12mS .
$$

**The off-diagonal components.** For $i\ne j$, both $\ne4$, the same computation gives $T_{ij}=-\tfrac14\bar\Psi\bigl(\{\gamma_i,\Omega_j\}+\{\gamma_j,\Omega_i\}\bigr)\Psi$. With $\gamma_i=\eta_{ii}h_i\gamma^i$, $\Omega_j=\eta_{jj}H_jh_j\cdot\tfrac12\gamma^j\gamma^4$ and $\{\gamma^i,\gamma^j\gamma^4\}=2\gamma^i\gamma^j\gamma^4$ for three distinct indices,

$$
T_{ij}=\tfrac14\,\eta_{ii}\eta_{jj}\,h_ih_j\,(H_i-H_j)\,\bar\Psi\gamma^i\gamma^j\gamma^4\Psi ,
$$

a three-gamma bilinear that vanishes when the two directions expand at the same rate. For $T_{4i}$: $T_{4i}=-\tfrac14\bigl[\bar\Psi\{\gamma_4,\Omega_i\}\Psi+\bar\Psi\gamma_i\partial_4\Psi-\partial_4\bar\Psi\,\gamma_i\Psi\bigr]$, and $\{\gamma^4,S^{i4}\}=0$, so $T_{4i}=-\tfrac14\bigl(\bar\Psi\gamma_i\partial_4\Psi-\partial_4\bar\Psi\,\gamma_i\Psi\bigr)$ off shell. On shell $\gamma^4\partial_4\Psi+\tfrac12\Theta\gamma^4\Psi=M_{\mathrm{eff}}\Psi$ (Section 7.4), that is $\partial_4\Psi=-M_{\mathrm{eff}}\gamma^4\Psi-\tfrac12\Theta\Psi$ and, conjugating, $\partial_4\bar\Psi=M_{\mathrm{eff}}\bar\Psi\gamma^4-\tfrac12\Theta\bar\Psi$. Inserting, the $\Theta$ terms cancel and what remains is $-M_{\mathrm{eff}}\bar\Psi\{\gamma_i,\gamma^4\}\Psi=0$: **$T_{4i}=0$ on shell.** (Stage-1 document, §9.7; checks `EMT_homogeneousReduction_G3`, `EMT_homogeneousReduction`, `EMT_homogeneousTimeSpaceVanishesOnShell_G3`; for dirac16complex00 with the default and with a general smooth $U$, checks `C00_EMT_homogeneousEquationsOfState` and `S5_EMT_homogeneousEquationsOfState`, at three times of the frame $h_i=1+x_4^2/(i+2)$.)

**Energy conservation and dilution.** The tensor is not diagonal in general: the $T_{ij}$ above are nonzero for generic states when the rates differ. Nevertheless the component $\nu=4$ of $\nabla_\mu T^\mu{}_\nu=0$ contains only diagonal components. Write it out with the rule of Section 4.5 for the covariant derivative of a tensor (one term $+\Gamma$ for the upper index, one term $-\Gamma$ for the lower index), contracted over $\mu$:

$$
\nabla_\mu T^\mu{}_4=\partial_\mu T^\mu{}_4+\Gamma^\mu{}_{\mu\lambda}T^\lambda{}_4-\Gamma^\lambda{}_{\mu4}T^\mu{}_\lambda .
$$

Three facts reduce it. (a) On shell $T_{4i}=0$, so $T^i{}_4=g^{ii}T_{i4}=0$ and only $T^4{}_4=g^{44}T_{44}=-\rho$ remains in the first two terms. (b) Nothing depends on $x_i$, so $\partial_\mu T^\mu{}_4=\partial_4T^4{}_4=-\partial_4\rho$, and $\Gamma^\mu{}_{\mu4}=\partial_4\ln\sqrt{|g|}=\Theta$ (Section 5.8). (c) The only Christoffel symbols with a lower index 4 are $\Gamma^i{}_{i4}=\Gamma^i{}_{4i}=H_i$ (no sum; $\Gamma^4{}_{44}=\Gamma^4{}_{4i}=0$ because $g_{44}=-1$ is constant and $g_{4i}=0$), so the last term is $-\sum_{i\ne4}H_i\,T^i{}_i=-\sum_{i\ne4}H_i\,p_{(i)}$: the off-diagonal $T^i{}_j$ ($i\ne j$) would need $\Gamma^j{}_{i4}$ with $i\ne j$, which vanishes. Altogether $-\partial_4\rho-\Theta\rho-\sum_iH_ip_{(i)}=0$, that is

$$
\partial_4\rho+\sum_{i\ne4}H_i\,\bigl(\rho+p_{(i)}\bigr)=0 .
$$

With $\rho=mS+U$ and $\rho+p=S(m+U')$ this is $(m+U')\bigl(\partial_4S+\Theta S\bigr)=0$. Wherever $M_{\mathrm{eff}}\ne0$, $\partial_4(VS)=V(\partial_4S+\Theta S)=0$: **$S$ dilutes as the inverse 7-volume**, $S\,V=\text{constant}$ (Stage-1 document, §9.6, derived there; Chapter 11 derives the same law from the mode equation). For $U=0$ the energy density $mS$ then falls like $1/V$, as dust does.

**Beyond the scalar field.** Unlike $\tfrac12\dot\phi^2\ge0$, the quantity $\mathrm{KE}_L=\tfrac12SM_{\mathrm{eff}}$ has no fixed sign, because $S$ can have either sign (Section 6.6). Two consequences, both at the level of these classical formulas (Stage-1 document, §9.6): for $\rho>0$, $w<-1$ ("phantom") exactly when $\mathrm{KE}_L<0$, and $w>1$ exactly when $\mathrm{PE}_L<0$. Whether such states are physical is a separate question (Chapter 11 discusses it for dirac16complex).

| quantity | homogeneous scalar field (Section 5.8) | homogeneous dirac16complex or dirac16complex00 |
| --- | --- | --- |
| Lagrangian | $\tfrac12\dot\phi^2-V$ | $\mathcal L_s=K-mS-U$ |
| energy density | $\tfrac12\dot\phi^2+V$ | $mS+U$ |
| pressure | $\tfrac12\dot\phi^2-V$ | $SU'-U$ (all seven directions) |
| kinetic energy | $\tfrac12\dot\phi^2\ge0$ | $\mathrm{KE}_L=\tfrac12S(m+U')$, either sign |
| potential energy | $V$ | $\mathrm{PE}_L=\tfrac12(mS+2U-SU')$ |
| $\rho=\mathrm{KE}+\mathrm{PE}$, $p=\mathrm{KE}-\mathrm{PE}$ | yes | yes (split A) |

**Worked example with exact numbers.** The Stage-5 report records three exact on-shell states in the frame above. At $x_4=3/7$ with $m=5/9$, $\lambda=-3/8$ and $S=-83/15$ (`dirac16complex00-theory.json`, key `exactValues.homogeneousG3.G3t3`):

$$
\begin{aligned}
&mS=-\tfrac{83}{27},\qquad \tfrac\lambda2S^2=-\tfrac3{16}\cdot\tfrac{6889}{225}=-\tfrac{6889}{1200},\qquad \rho=-\tfrac{83}{27}-\tfrac{6889}{1200}=-\tfrac{95201}{10800},\qquad p=-\tfrac{6889}{1200},\\
&w=\frac{p}{\rho}=\frac{6889\cdot9}{95201}=\frac{747}{1147},\qquad \mathrm{KE}_L=\tfrac12S\bigl(m+\lambda S\bigr)=-\tfrac{78601}{10800},\qquad \mathrm{PE}_L=\tfrac12mS=-\tfrac{83}{54}.
\end{aligned}
$$

Here both the energy density and the pressure are negative, which the classical formulas allow because $S<0$ while $m>0$. The first recorded state ($x_4=1/3$, $m=3/7$, $\lambda=5/11$, $S=5617/567$) has $\rho=187781927/7072758$, $p=157753445/7072758$ and $w=28085/33431$, all positive. Stage 1 recorded a state with $w=75899/24059\approx3.155>1$ ($m=4$, $\lambda=7/6$, $S=-75899/7560$, $\mathrm{PE}_L=-75899/3780<0$; Stage-1 document, Result 9.3).

### 7.11 Plane waves: the charge and the energy of dirac16complex00 have no sign

**Theorem 7.6 (a Gordon-type identity).** Let $\Psi=u\exp\bigl(i\sum_ak_ax_a\bigr)$ be a plane-wave solution of the flat-space equation $\gamma^a\partial_a\Psi=M\Psi$ with a constant $M\ne0$ (for example the free field, $M=m$). Then

$$
J^a=\frac{k^a}{M}\,S\qquad(k^a:=\eta^{ab}k_b),\qquad\text{in particular}\qquad S=\frac{M}{\omega}\,J^4\ \ \text{with}\ \ \omega:=k^4=-k_4 .
$$

*Proof.* With $\gamma(k)=\sum_ak_a\gamma^a$ the equation is $i\gamma(k)u=Mu$, so $\gamma(k)u=-iMu$. For the adjoint, $\bar\Psi$ carries the factor $\exp(-i\sum k_ax_a)$, so the second field equation gives $-i\,\bar u\gamma(k)=-M\bar u$, that is $\bar u\gamma(k)=-iM\bar u$ ($\bar u=u^\dagger C$). The Clifford relation gives $\gamma^a\gamma(k)+\gamma(k)\gamma^a=2k^a$. Sandwich it: $\bar u\gamma^a\gamma(k)u+\bar u\gamma(k)\gamma^au=-iM\,\bar u\gamma^au-iM\,\bar u\gamma^au=2k^a\,\bar uu$. Hence $\bar u\gamma^au=i(k^a/M)\,\bar uu$ and $J^a=-i\bar u\gamma^au=(k^a/M)S$. For $a=4$: $k^4=\eta^{44}k_4=-k_4=\omega$, the frequency of $e^{-i\omega x_4}$. $\square$

**The energy density of a free plane wave.** Let $U=0$. On shell $\mathcal L_s=0$ (Section 7.4), and $\partial_4\Psi=-i\omega\Psi$ gives $K_4=\tfrac i2(-i\omega-i\omega)\Psi^\dagger B\Psi=\omega\,J^4$. So

$$
\rho=K_4-\mathcal L_s=\omega\,J^4=\frac{\omega^2}{m}\,S .
$$

For a given momentum and frequency the solutions form an 8-dimensional space (Section 6.6), and on it the Hermitian form $J^4=u^\dagger Bu$ has four positive and four negative directions: the space has a basis of eight solutions, orthogonal for this form, on four of which $u^\dagger Bu>0$ and on four $u^\dagger Bu<0$. The pair of numbers (4,4) is called the **signature** of the form; Chapter 8 calls the indefinite inner product $f^\dagger Bh$ the **Krein** form, so the statement is the "Krein signature (4,4)" of check `QNT_kreinSignature`. This book proves it only at rest (Section 8.8; the worked example below exhibits one rest solution of each sign); for moving waves it is taken from the check. So there are solutions of positive frequency with negative energy density.

**Worked example (at rest).** Take $m>0$ and the two positive-frequency rest solutions $\Psi_\pm=e^{-imx_4}u_\pm$ with $u_+=\tfrac12(e_0-e_4-ie_9-ie_{13})$ and $u_-=\tfrac12(e_0+e_4+ie_9-ie_{13})$ of Section 8.8. Both satisfy $-i\gamma^4u_\pm=u_\pm$, so both solve the field equation with $\omega=m$ (Section 7.4). With the table of $C$: $(Cu)_0=-u_4$, $(Cu)_4=-u_0$, $(Cu)_9=u_{13}$, $(Cu)_{13}=u_9$, so $Cu_+=u_+$ and $Cu_-=-u_-$. Hence $S=u_\pm^\dagger Cu_\pm=\pm1$, $J^4=u_\pm^\dagger Bu_\pm=u_\pm^\dagger C(-i\gamma^4)u_\pm=u_\pm^\dagger Cu_\pm=\pm1$, and

$$
\rho(\Psi_+)=+m,\qquad \rho(\Psi_-)=-m .
$$

Both are solutions of positive frequency and unit norm $u^\dagger u=1$; the second has negative energy density. Multiplying a solution by a number $c$ multiplies $\rho$ by $|c|^2$, so the energy density of solutions of the free dirac16complex00 field takes every real value: **the classical energy of dirac16complex00 is not bounded below.** The report exhibits the same with moving plane waves ($m=1$, $k=(1,1,2,3)$, $\omega=\pm4$: $\rho=\omega J^4$ with both signs of $J^4$ on each frequency), and with the interaction: for $\lambda=-1$ ($m=1$) exact homogeneous rest states with $S=1,10,100$ have $\rho=mS+\tfrac\lambda2S^2=\tfrac12,-40,-4900$, and for $\lambda=+1$ a family of exact self-consistent plane waves has $\rho=-56/75,\,-1512/845,\dots$, decreasing without bound (check `C00_energy_unboundedBelow` and its `S5_` twin; `dirac16complex00-theory.json`, key `commutingFieldSpecifics.energyStatement`).

**The contrast with dirac16complex.** For the Grassmann field the classical "energy" is not a number at all but an element of the Grassmann algebra; the physical energy exists only after quantization. There the same indefinite $B$ becomes the matrix of the canonical anticommutator, and in the good sector (the fields independent of $x_5,x_6,x_7$, Section 7.5) the filled Dirac sea and normal ordering give a Hamiltonian that is not negative (a preview of Section 8.10, derived in the Stage-1 document, §10.7, not a machine check). This mechanism needs the anticommutators of Fermi statistics; the classical commuting field has no counterpart of it.

### 7.12 The primordial field

**The field equation in the notebook's chart.** In the primordial field of Chapter 9, with $z=6Hx_0$, $s=\sin z$ and the diagonal vielbein $h=(\cot z,\ s^{1/6}e^{a_4}\,(\times3),\ 1,\ s^{1/6}e^{-a_4}\,(\times3))$, the curved gammas are $\gamma^{x_0}=\tan z\,\gamma^0$, $\gamma^{x_i}=s^{-1/6}e^{-a_4}\gamma^i$ ($i=1,2,3$), $\gamma^{x_4}=\gamma^4$ and $\gamma^{x_j}=s^{-1/6}e^{a_4}\gamma^j$ ($j=5,6,7$), and $\gamma^\mu\Omega_\mu=3H\gamma^0$ (Section 4.12). The field equation of Section 7.2 becomes, for both fields,

$$
\tan z\,\gamma^0\partial_0\Psi+s^{-1/6}e^{-a_4}\sum_{i=1}^3\gamma^i\partial_i\Psi+\gamma^4\partial_4\Psi+s^{-1/6}e^{a_4}\sum_{j=5}^7\gamma^j\partial_j\Psi+3H\gamma^0\Psi=M_{\mathrm{eff}}\,\Psi
$$

(the Stage-2 component equations; checks `C00_primordial_ELcommuting`, `C00_primordial_geometryMatchesStage2` and their `S5_` twins). Chapter 9 studies it in detail.

**An exact homogeneous solution for every $a_4$.** Look for a field that depends on $x_4$ only, $\Psi=u(x_4)$ (in the language of Chapter 9 it is the plane wave in the hidden coordinate with the imaginary wave number $K=-3iH$). All derivatives except $\partial_4$ vanish, and the equation becomes $\gamma^4\partial_4u+3H\gamma^0u=M_{\mathrm{eff}}u$. Multiplying by $-\gamma^4$:

$$
\partial_4u=N\,u,\qquad N:=-\gamma^4\bigl(M_{\mathrm{eff}}-3H\gamma^0\bigr)=-M_{\mathrm{eff}}\gamma^4+3H\gamma^4\gamma^0 .
$$

**$S$ is constant.** $N$ is real, so for commuting $u$, $\partial_4(u^\dagger Cu)=u^\dagger(N^TC+CN)u$. Now $N^T=M_{\mathrm{eff}}\gamma^4+3H\gamma^4\gamma^0$ (transpose with $(\gamma^4)^T=-\gamma^4$, $(\gamma^0)^T=\gamma^0$, and $\gamma^0\gamma^4=-\gamma^4\gamma^0$), and with $\gamma^4C=C\gamma^4$, $\gamma^0C=-C\gamma^0$:

$$
N^TC+CN=M_{\mathrm{eff}}\bigl(\gamma^4C-C\gamma^4\bigr)+3H\bigl(\gamma^4\gamma^0C+C\gamma^4\gamma^0\bigr)=0+3H\bigl(-C\gamma^4\gamma^0+C\gamma^4\gamma^0\bigr)=0 .
$$

So $S=u^\dagger Cu$ is constant, hence $M_{\mathrm{eff}}=m+U'(S)$ is constant, and $u(x_4)=\exp(Nx_4)\,u(0)$ solves the nonlinear equation exactly, for every potential $U$ and every function $a_4$: the free function does not appear (checks `C00_primordial_homogeneousState` and `S5_primordial_homogeneousState`). For dirac16complex00 this is an exact classical solution; for dirac16complex the same formulas are the mean-field reading in which the bilinears are replaced by numbers.

**Its energy–momentum tensor.** For $\mu=0$: $\Omega_0=0$ (Section 4.12) and $\partial_0u=0$, so $D_0\Psi=0$ and $T^0{}_0=\mathcal L_s$. For the six directions $p\in\{1,2,3,5,6,7\}$: $T^p{}_p=\mathcal L_s$, by the argument of Section 7.10 ($\Omega_p$ is a combination of $S^{0p}$ and $S^{4p}$, and $\{\gamma^p,S^{0p}\}=\{\gamma^p,S^{4p}\}=0$; Proposition 9.2). $K_\perp=\tfrac12\bar\Psi\{\gamma^\mu,\Omega_\mu\}\Psi=0$ for the diagonal vielbein, so $\rho=mS+U$. On shell, therefore,

$$
\begin{aligned}
&\rho=mS+U,\qquad p_{(\mu)}=SU'-U\ \ (\text{all seven }\mu\ne4),\\
&\mathrm{KE}_L=\tfrac12SM_{\mathrm{eff}},\qquad \mathrm{PE}_L=\tfrac12(mS+2U-SU'),\qquad \mathrm{KE}_H=0,
\end{aligned}
$$

independent of $a_4$: the same equation of state as in Section 7.10.

**An exact dirac16complex00 source of the static field.** Now take the static member of the primordial field, $a_4=a_{4,0}$ constant (Section 9.15). Its Einstein tensor is diagonal, $G^\mu{}_\nu=\mathrm{diag}(15,15,15,15,21,15,15,15)H^2$ in the coordinate order $x_0,\dots,x_7$ (Chapter 9). So the Einstein equations $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ ($\kappa$ is the gravitational coupling) say two things: every off-diagonal component of $T$ vanishes, and the diagonal components take the prescribed values. Proposition 9.4 with the slope $c=0$ states the result: the state $\Psi=u(x_4)$ satisfies all 64 components **if and only if** (1) the six bilinears $V_p:=\bar\Psi\gamma^0\gamma^p\gamma^4\Psi$ ($p=1,2,3,5,6,7$) vanish, (2) $mS=-36H^2/\kappa$ and (3) $\lambda S^2=30H^2/\kappa$. Condition (1) does **not** say that all three-gamma bilinears vanish; only these six enter. We derive all three conditions for this state.

*The off-diagonal components.* For $a_4'=0$ Section 9.13 gives $\Omega_0=\Omega_4=0$ and $\Omega_p=-\eta_{pp}H\,h_p\,S^{0p}$ for $p\in\{1,2,3,5,6,7\}$, with the scale factors $h_p=s^{1/6}e^{a_{4,0}}$ for $p\le3$ and $h_p=s^{1/6}e^{-a_{4,0}}$ for $p\ge5$. The lowered curved gammas are $\gamma_\mu=g_{\mu\mu}\gamma^{x_\mu}=\eta_{\mu\mu}h_\mu\gamma^\mu$ (no sum), in particular $\gamma_0=\cot z\,\gamma^0$, $\gamma_4=-\gamma^4$ and $\gamma_p=\eta_{pp}h_p\gamma^p$. For the state on shell, $D_0\Psi=0$, $D_p\Psi=\Omega_p\Psi$ and $D_4\Psi=N\Psi$; and $D_0\bar\Psi=0$, $D_p\bar\Psi=-\bar\Psi\Omega_p$ and $D_4\bar\Psi=(N\Psi)^\dagger C=\Psi^\dagger N^TC=-\bar\Psi N$, the last step by $N^TC=-CN$ (shown above). Insert these into Theorem 7.4, where $g_{\mu\nu}=0$ for $\mu\ne\nu$:

- $T_{0p}=-\tfrac14\bar\Psi\{\gamma_0,\Omega_p\}\Psi=0$, because $\{\gamma^0,S^{0p}\}=0$ (Lemma 6.3: the index 0 belongs to the pair).
- $T_{04}=-\tfrac14\bar\Psi\{\gamma_0,N\}\Psi=0$, because $\{\gamma^0,\gamma^4\}=0$ and $\{\gamma^0,\gamma^4\gamma^0\}=\gamma^0\gamma^4\gamma^0+\gamma^4\gamma^0\gamma^0=-\gamma^4+\gamma^4=0$.
- For two different transverse directions $p\ne q$, $T_{pq}=-\tfrac14\bar\Psi\bigl(\{\gamma_p,\Omega_q\}+\{\gamma_q,\Omega_p\}\bigr)\Psi=\tfrac14H\eta_{pp}\eta_{qq}h_ph_q\,\bar\Psi\bigl(\gamma^p\gamma^0\gamma^q+\gamma^q\gamma^0\gamma^p\bigr)\Psi=0$, by Lemma 6.3 and because reversing the order of three distinct anticommuting gammas costs three signs.
- $T_{p4}=-\tfrac14\bigl[\bar\Psi\{\gamma_p,N\}\Psi+\bar\Psi\{\gamma_4,\Omega_p\}\Psi\bigr]$. In the first term $\{\gamma^p,\gamma^4\}=0$, while $\gamma^p$ commutes with the pair $\gamma^4\gamma^0$ (it passes two gammas), so $\{\gamma_p,N\}=3H\eta_{pp}h_p\cdot2\gamma^p\gamma^4\gamma^0=6H\eta_{pp}h_p\,\gamma^0\gamma^p\gamma^4$. In the second, the two minus signs of $\gamma_4$ and $\Omega_p$ cancel and Lemma 6.3 gives $\{\gamma_4,\Omega_p\}=\eta_{pp}Hh_p\,\gamma^4\gamma^0\gamma^p=\eta_{pp}Hh_p\,\gamma^0\gamma^p\gamma^4$ (move $\gamma^4$ two places to the right). Hence

$$
T_{p4}=T_{4p}=-\tfrac74\,\eta_{pp}\,H\,h_p\,V_p\qquad(p=1,2,3,5,6,7).
$$

Since $H\ne0$ and $h_p\ne0$, the off-diagonal Einstein equations hold exactly when all six $V_p$ vanish: condition (1). (For $p\le3$ the coefficient is $-\tfrac74Hs^{1/6}e^{a_{4,0}}$, the entry of the Stage-2 table of these bilinears, `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md` §13. For a slope $c\ne0$ nine further bilinears $\bar\Psi\gamma^i\gamma^4\gamma^j\Psi$ appear, with coefficients proportional to $c$; that is why Proposition 9.4 needs 15 bilinears in general and only these 6 here.)

*The diagonal components.* On shell $T^0{}_0=T^p{}_p=\mathcal L_s=SU'-U=\tfrac\lambda2S^2$ and $T^4{}_4=g^{44}T_{44}=-\rho=-(mS+\tfrac\lambda2S^2)$. The seven equations with $\mu=\nu\ne4$ read $15H^2=\tfrac\kappa2\lambda S^2$, which is condition (3). The equation $G^4{}_4=\kappa T^4{}_4$ reads $21H^2=-\kappa mS-\tfrac\kappa2\lambda S^2=-\kappa mS-15H^2$, so $\kappa mS=-36H^2$, which is condition (2).

*The example.* The Stage-5 report exhibits such a state for dirac16complex00 (`dirac16complex00-theory.json`, key `primordial.staticSourceExample`). Units $H=\kappa=1$; parameters

$$
m=-30,\qquad \lambda=\tfrac{125}6,\qquad S=\tfrac65,\qquad M_{\mathrm{eff}}=m+\lambda S=-30+25=-5 .
$$

Conditions (2) and (3) hold: $mS=-36$ and $\lambda S^2=\tfrac{125}6\cdot\tfrac{36}{25}=30$. The matrix $N=5\gamma^4+3\gamma^4\gamma^0$ satisfies $N^2=25(\gamma^4)^2+9(\gamma^4\gamma^0)^2+15(\gamma^4\gamma^4\gamma^0+\gamma^4\gamma^0\gamma^4)=-25+9+0=-16$, so its eigenvalues are $\pm4i$; the column

$$
v=(1,\,3i,\,0,\,0,\,1,\,-3i,\,0,\,0,\,-3,\,-i,\,0,\,0,\,-3,\,i,\,0,\,0)^T
$$

satisfies $Nv=4i\,v$ and $v^\dagger Cv=32$ (Exercises 7.13 and 7.10). Condition (1) holds as well. The column $v$ is nonzero only in the eight places $\{0,1,4,5,8,9,12,13\}$; call this set $I$. Because $C$ and $\gamma^0$ are real and symmetric, $v^\dagger C\gamma^0=\bigl((C\gamma^0)^Tv\bigr)^\dagger=(\gamma^0Cv)^\dagger$, so

$$
V_p(v)=v^\dagger C\gamma^0\gamma^p\gamma^4v=a^\dagger\gamma^pb,\qquad a:=\gamma^0Cv,\quad b:=\gamma^4v .
$$

With the tables of Sections 2.8 and 2.9 both $a$ and $b$ are again nonzero only on $I$ (Exercise 7.13 lists them). For $p=1,2,5,6$ the rows $0,1,4,5,8,9,12,13$ of $\gamma^p$ all point to columns outside $I$ (for $\gamma^1$ they are $15,14,11,10,7,6,3,2$), so $\gamma^pb$ vanishes on $I$, and every term $a_k^\ast(\gamma^pb)_k$ of $a^\dagger\gamma^pb$ contains a zero factor: $V_1=V_2=V_5=V_6=0$. For $p=3$ and $p=7$ the rows of $I$ point into $I$, and the eight terms cancel in pairs (Exercise 7.13): $V_3=V_7=0$. Other three-gamma bilinears of $v$ need not vanish and do not, for example $\bar v\gamma^1\gamma^2\gamma^3v=24$; they do not enter $T$ for this state. So $\Psi=e^{i\omega x_4}u_0$ with $\omega=4=\sqrt{M_{\mathrm{eff}}^2-9H^2}$ and $u_0=\sqrt{S/32}\;v=\sqrt{3/80}\;v$ is an exact solution with $S=6/5$ (the factor $e^{i\omega x_4}$ and its conjugate cancel in every bilinear, and $V_p(u_0)=\tfrac3{80}V_p(v)=0$), and

$$
\begin{aligned}
&\rho=mS+\tfrac\lambda2S^2=-36+15=-21,\qquad p=\tfrac\lambda2S^2=15,\qquad w=-\tfrac57,\\
&\mathrm{KE}_L=\tfrac12SM_{\mathrm{eff}}=-3,\qquad \mathrm{PE}_L=\rho-\mathrm{KE}_L=-18 .
\end{aligned}
$$

These are exactly the required source $\rho_{\mathrm{req}}=-21H^2/\kappa$, $p_{\mathrm{req}}=+15H^2/\kappa$ of Section 9.15. Together with condition (1) this proves $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ in all 64 components, and the verifiers confirm it exactly (checks `C00_primordial_staticFieldSourcedExactly`, `S5_primordial_staticFieldSourcedExactly`, `S5_static_sourceProperChart`). In words: **within eight-dimensional Einstein gravity, the static member of the primordial field is sourced exactly by a homogeneous classical dirac16complex00 field, with negative energy density.** The statement concerns Einstein's equations without the Lovelock terms (which the project does not compute, Section 9.9) and the smooth field of the notebook's chart, which in the proper hidden coordinate $y=\ln(\sin z)/(6H)$ of Section 9.15 is the region $y<0$ (because $0<\sin z<1$ there). Section 9.16 also considers a model in which two copies of this field are glued along the surface $y=0$, one of them reflected (the "Z2 brane"; Z2 names the reflection $y\to-y$). There the slope of the warp factor jumps at $y=0$, and this kink needs an additional source concentrated on the surface, which this state does not supply. Two further limitations are part of the statement. The state has negative energy density, which the classical commuting field allows (Section 7.11) and which is not bounded below; its stability is not examined, and nothing says that such a state is realized. For dirac16complex the same numbers are only the mean-field reading of $\langle\bar\Psi\Psi\rangle=S$; Chapter 13 found that none of the computed Kohn–Sham states meets the two conditions.

**The static warped form (a preview of Chapters 13 and 14).** In the proper hidden coordinate $y$ the static field is $ds^2=dy^2-dx_4^2+e^{2Hy}\bigl[e^{2a_{4,0}}(dx_1^2+dx_2^2+dx_3^2)-e^{-2a_{4,0}}(dx_5^2+dx_6^2+dx_7^2)\bigr]$ with $\sqrt{|g|}=e^{6Hy}$ (Section 9.15). Section 13.3 derives that the stationary ansatz $\Psi=e^{-i\varepsilon x_4}e^{i(k_1x_1+k_2x_2+k_3x_3)}e^{-3Hy}\chi(y)$, with a frequency $\varepsilon$ and a 3-momentum $(k_1,k_2,k_3)$, removes the term $3H\gamma^0$ exactly and gives the reduced equation

$$
\gamma^0\chi'+i\,\xi(y)\sum_{l=1}^3k_l\gamma^l\chi-i\varepsilon\gamma^4\chi=M_{\mathrm{eff}}\,\chi,\qquad \xi(y)=e^{-Hy-a_{4,0}} .
$$

The Greek letter $\xi$ (xi) names the weight with which the momentum enters, as in Chapter 13 (it has nothing to do with the small vector field $\xi^\mu$ of Section 7.8); the letter $\kappa$ stays reserved for the gravitational coupling (the theory files and the Rust code call this weight `kappa`). The field equation is linear in $\Psi$ at fixed $M_{\mathrm{eff}}$, so this reduction is the same for both statistics (checks `C00_static_geometryAndReducedEquation`, `S5_static_geometryAndReducedEquation`, which take the momentum along $x_1$). What differs is the meaning of the energy. Section 13.4 finds a basis of $\mathbb C^{16}$ in which the equation splits into eight separate pairs of components, called **blocks**; each block is labelled by three signs $(j,s_2,s_3)$, each $+1$ or $-1$, and on each block the charge matrix $B$ acts as multiplication by the number $js_2$. This number is the **Krein sign** of the block (the sign of the form $u^\dagger Bu$ of Section 7.11 on that block); four blocks have $+1$ and four $-1$. Chapter 13 describes the quantized dirac16complex in the Kohn–Sham approximation (Chapter 12), in which each quantum occupies an **orbital**, one solution $\chi$ of this equation, and it assigns to each orbital a **one-body** energy–momentum tensor, obtained from the classical formula by replacing $\Psi^\dagger$ with $u^\dagger B$ (the expectation-value rule of Section 8.12). For a classical commuting mode in one block, every component of $T_{\mu\nu}$ equals $js_2$ times this one-body value of the same orbital. So the classical energy density of dirac16complex00 is negative in four of the eight blocks, also in the static primordial field; explicit exact box modes show both signs (checks `C00_static_classicalModeIsKreinWeightedKS`, `C00_static_classicalEnergyKreinSigned` and their `S5_` twins). Chapter 14 builds the Kohn–Sham model of dirac16complex00 on this.

### 7.13 The chirality map of the equations, the current and the energy–momentum tensor

Section 6.11 proved $\mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi]$. The same five facts about $\gamma^8$ act on everything derived in this chapter.

**Theorem 7.7.** For every vielbein, every field configuration and both kinds of components, with $E_{m,\lambda}[\Psi]:=\gamma^\mu D_\mu\Psi-(m+\lambda S)\Psi$:

$$
\begin{aligned}
&E_{-m,-\lambda}[\gamma^8\Psi]=-\gamma^8E_{m,\lambda}[\Psi],\qquad J^\mu[\gamma^8\Psi]=-J^\mu[\Psi],\qquad S[\gamma^8\Psi]=S[\Psi],\\
&T_{\mu\nu}[\gamma^8\Psi;-m,-\lambda]=-T_{\mu\nu}[\Psi;m,\lambda].
\end{aligned}
$$

Hence $\Psi$ solves the field equations with $(m,\lambda)$ exactly when $\gamma^8\Psi$ solves them with $(-m,-\lambda)$.

*Proof.* By (G5) of Section 6.11, $\gamma^\mu D_\mu(\gamma^8\Psi)=\gamma^\mu\gamma^8D_\mu\Psi=-\gamma^8\gamma^\mu D_\mu\Psi$; and $S$ is unchanged, so $(-m-\lambda S)\gamma^8\Psi=-\gamma^8(m+\lambda S)\Psi$. Adding, $E_{-m,-\lambda}[\gamma^8\Psi]=-\gamma^8E_{m,\lambda}[\Psi]$; since $\gamma^8$ is invertible, one vanishes exactly when the other does. The current: $\bar\Psi\gamma^8\gamma^\mu\gamma^8\Psi=-\bar\Psi\gamma^\mu\Psi$. The tensor: the bracket of Theorem 7.4 consists of bilinears with one gamma matrix and one covariant derivative, each of which changes sign exactly like $K$ in Section 6.11; and $\mathcal L_s[\gamma^8\Psi;-m,-\lambda]=-\mathcal L_s[\Psi;m,\lambda]$ by Theorem 6.7 with $(m,\lambda)$ replaced by $(-m,-\lambda)$. $\square$

The pairing reports check the theorem as an identity in completely generic symbols, in a Grassmann algebra, with exact jets of the general vielbein G1, and in the primordial field. The names below are those of `wolfram-pairing-report.json`; each has a Python twin in `python-pairing-report.json` with `S5_` in place of `PAIR_` (for example `S5_T1generic_fieldEquation`):

```
generic symbols:   PAIR_T1generic_fieldEquation  PAIR_T1generic_conjugateFieldEquation
                   PAIR_T1generic_current        PAIR_T1generic_emtAll36
Grassmann algebra: PAIR_T1grassmann_diracOperator  PAIR_T1grassmann_emt
                   PAIR_T1grassmann_current
jets of G1:        PAIR_T1jets_fieldEquations  PAIR_T1jets_emt
                   PAIR_T1jets_onShellImage    PAIR_T1jets_conservationBoth
primordial field:  PAIR_T1primordial_emt64
```

**Example.** For the homogeneous state of Section 7.10, $\rho=mS+\tfrac\lambda2S^2$. Its image $\gamma^8\Psi$, a solution with $(-m,-\lambda)$, has the same $S$, hence $\rho=-mS-\tfrac\lambda2S^2$: exactly the negative, as the theorem says.

**What follows, and what does not.** Adding a solution with $(m,\lambda)$ and its image with $(-m,-\lambda)$ in the same gravitational field, the two energy–momentum tensors and the two currents cancel at every point and at every time. Chapter 15 states this as the pair corollary of Theorem T1, with its hypotheses: the image must carry the coupling $-\lambda$ (or $\lambda=0$), and for the quantized dirac16complex the image field carries the opposite Krein metric $-B$. (The Krein metric of a quantized field is the matrix of its equal-time anticommutator, $\{\Psi,\Psi^\dagger\}=B\,\delta^7/\sqrt{|g|}$ for dirac16complex, Section 8.6; for $\gamma^8\Psi$ it is $\gamma^8B\gamma^8=-B$, because $\gamma^8$ anticommutes with $\gamma^4$ and commutes with $C$.) An independently quantized theory with mass $-m$, with its own metric $+B$ and positive energies, does not cancel but doubles (`pairing-theory.json`, keys `T1` and `T1krein`; a preview of Chapter 15). These are statements about conservation laws and constraints. They compute no process that creates such a pair, and Chapter 16 explains exactly what they do and do not establish about the notebook's hypothesis.

### 7.14 How the repository checks all of this

| statement (section) | checks |
| --- | --- |
| field equations, commuting components (flat, G1, G2, general $U$) (7.2) | `C00_EL_commutingFlat`, `C00_EL_commutingCurved`, `C00_EL_commutingGeneralSmoothU` (both) |
| field equations, Grassmann components; same form (7.3) | `LAG_eulerLagrangePsibar_G1`, `LAG_eulerLagrangePsi_G1` (and G2); `S5_EL_grassmannCurved`; `C00_EL_identicalFormBothStatistics` (both) |
| second-order form with $-\tfrac14R$ (7.4) | `GEO_lichnerowicz_G1`, `GEO_lichnerowicz_G2`; `C00_connection_nonTrivialCoupling` (both) |
| current identity, conservation, Hermiticity (7.5) | `MA_M1_noetherIdentity_commuting_G1`, `MA_M1_noetherIdentity_grassmann_G1`; `QNT_currentHermiticity`; `C00_current_conservationAndReality` (both) |
| indefinite charge of dirac16complex00 (7.5) | `C00_charge_indefinite` (both) |
| $T_{\mu\nu}$ from the full vielbein variation (7.7) | `EMT_variation_G3`, `EMT_variation`; `C00_EMT_vielbeinVariation` (both) |
| symmetry, reality, trace, conservation (7.8) | `EMT_symmetricHermitian_G1`, `EMT_trace_G1`, `EMT_conservation_G1` (and G2); `C00_EMT_symmetricAndReal`, `C00_EMT_traceOnShell`, `C00_EMT_conservationOnShell`, `C00_EMT_generalSmoothU` (both) |
| $\rho=K_4-\mathcal L_s=\mathrm{KE}_H+\mathrm{PE}_H$ (7.9) | `C00_EMT_observerSplitGaussianNormal` (both) |
| homogeneous $\rho$, $p$, KE, PE, $w$, $T_{ij}$, $T_{4i}$ (7.10) | `EMT_homogeneousReduction_G3`, `EMT_homogeneousReduction`; `C00_EMT_homogeneousEquationsOfState` (both) |
| energy of dirac16complex00 unbounded below (7.11) | `C00_energy_unboundedBelow` (both); `QNT_kreinSignature` |
| primordial field: equation, homogeneous state, static source (7.12) | `C00_primordial_ELcommuting`, `C00_primordial_homogeneousState`, `C00_primordial_staticFieldSourcedExactly` (both); `S5_static_sourceProperChart` |
| static warped form and block signs (7.12) | `C00_static_geometryAndReducedEquation`, `C00_static_classicalModeIsKreinWeightedKS`, `C00_static_classicalEnergyKreinSigned` (both) |
| $\gamma^8$ map of equations, current and $T_{\mu\nu}$ (7.13) | `PAIR_T1generic_*`, `PAIR_T1grassmann_*`, `PAIR_T1jets_*`, `PAIR_T1primordial_emt64` |

"Both" means the `C00_` check of `wolfram-dirac16complex00-report.json` and the `S5_` check with the same ending in `python-dirac16complex00-report.json`. The `PAIR_` checks are those of `wolfram-pairing-report.json`; each has a twin with the same ending and the prefix `S5_` in `python-pairing-report.json`. The Stage-1 checks are in the reports of `artifacts/dirac16complex/arbitrary-field/`. Chapter 19 lists the commands that rerun the verifiers. The Stage-5 gate script that `handoff/specs/STAGE5_SPEC.md` (§6) plans, `scripts/verify_stage5_pair_creation.ps1` and `.sh`, did not exist yet when this chapter was written, so the Stage-5 reports have not been regenerated from a fresh copy of the repository.

### 7.15 What we proved and what we assumed

**What we proved.** With complete derivations in this chapter: the Euler–Lagrange equations $\gamma^\mu D_\mu\Psi=(m+U'(S))\Psi$ and $(D_\mu\bar\Psi)\gamma^\mu=-(m+U'(S))\bar\Psi$ in every gravitational field, for commuting components (Section 7.2) and for Grassmann components (Section 7.3); that the second is the conjugate of the first, that the equations are of first order in time, that $K=M_{\mathrm{eff}}S$ and $\mathcal L_s=SU'-U$ on shell, and that for $U=0$ every solution obeys the second-order equation with the curvature term $-\tfrac14R$; the off-shell current identity (Theorem 7.1), the Hermiticity and conservation of $J^\mu=-i\bar\Psi\gamma^\mu\Psi$, its relation to the Noether current, the conservation of $Q$ (by the slice argument of Section 5.7) and $J^4=\Psi^\dagger B\Psi$, which is indefinite for dirac16complex00; the energy–momentum tensor of Theorem 7.4 from the symmetric variation of the vielbein, including the change of the spin connection (Lemma 7.2, Corollary 7.3); its symmetry, reality, trace $-mS+7SU'-8U$ on shell, and conservation (Theorem 7.5); $\rho=K_4-\mathcal L_s=\mathrm{KE}_H+\mathrm{PE}_H$ and the oscillator form of $K_4$; the homogeneous formulas $\rho=mS+U$, $p=SU'-U$ in all seven directions, the off-diagonal components, $T_{4i}=0$ on shell and, although $T_{ij}\ne0$ in general, the energy equation with only diagonal components and the dilution $SV=\text{constant}$; the Gordon-type identity (Theorem 7.6), $\rho=\omega J^4$ for free plane waves and the negative energy density of the positive-frequency rest solution $u_-$, so that the classical energy of dirac16complex00 is unbounded below; the exact homogeneous solution in the primordial field for every $a_4$ and every $U$, with its equation of state; for this state in the static field, the off-diagonal components of its energy–momentum tensor ($T_{0p}=T_{04}=T_{pq}=0$ and $T_{p4}=-\tfrac74\eta_{pp}Hh_pV_p$ with the six bilinears $V_p=\bar\Psi\gamma^0\gamma^p\gamma^4\Psi$), hence the three conditions under which it sources the static field in all 64 components (the six $V_p$ vanish, $mS=-36H^2/\kappa$, $\lambda S^2=30H^2/\kappa$: Proposition 9.4 with $c=0$), and the exact classical dirac16complex00 source that meets them ($m=-30$, $\lambda=125/6$, $S=6/5$: $Nv=4iv$, all six $V_p=0$, $\rho=-21$, $p=15$; Exercises 7.10 and 7.13); and the $\gamma^8$ map of the equations, the current and the energy–momentum tensor (Theorem 7.7).

**What we assumed or took from elsewhere.** The Lagrangian and its building blocks (Chapter 6), the geometry of Chapter 4 (the vielbein postulate, the divergence identity, the Lichnerowicz formula, the covariant constancy of the gammas), the variational calculus of Chapter 5 for ordinary and Grassmann variables, and the invariance of the action under changes of coordinates and local frame rotations (Section 6.9). The definition of the energy–momentum tensor by the metric variation with the spinor held fixed, the symmetric (non-rotating) change of the vielbein, the sign convention $\rho=T_{44}$, and the names "pressure" for the time-like transverse directions and "kinetic" and "potential" energy for the two splits are conventions of the project. The Krein signature (4,4) of the moving plane waves is taken from the check `QNT_kreinSignature` (Section 8.8 proves the rest case). For the primordial field we used from Chapter 9 its vielbein, its spinor connection (Section 9.13) and the Einstein tensor of its static member, and from Section 9.15 the required source. The reduction of the static field to $2\times2$ blocks, the block Krein signs and the Kohn–Sham one-body tensor are derived in Chapters 13 and 14 and only previewed here; the statement that a classical mode's $T_{\mu\nu}$ is $js_2$ times the one-body value is quoted from the Stage-5 checks. The formulas for dirac16complex are classical statements about the Grassmann field; their meaning as operator statements needs the quantization of Chapter 8, and the positivity of the quantized energy in the good sector is derived there, not machine-checked. Where the bilinears are replaced by numbers for dirac16complex (Sections 7.10 and 7.12) this is the mean-field approximation. No statement of this chapter says that any of the classical states exists in nature.

### 7.16 Exercises

**Exercise 7.1.** In flat space, for the Lagrangian of one direction only, $\mathcal L=\tfrac12\bigl(\Psi^\dagger C\gamma^1\partial_1\Psi-\partial_1\Psi^\dagger C\gamma^1\Psi\bigr)-m\Psi^\dagger C\Psi$ (commuting components), compute $\partial\mathcal L/\partial\Psi_a^\ast$ and $\partial\mathcal L/\partial(\partial_1\Psi_a^\ast)$ and derive the Euler–Lagrange equation.

**Exercise 7.2.** Show that on shell $\mathcal L_s=\tfrac\lambda2S^2+\tfrac{2\mu}3S^3$ for the commuting field with $U=\tfrac\lambda2S^2+\tfrac\mu3S^3$, and compute the on-shell trace $T^\mu{}_\mu$.

**Exercise 7.3.** Using the table of $B$ in Section 2.9, compute $J^4=\Psi^\dagger B\Psi$ for $\Psi=e_0+e_9$, $\Psi=e_0+i\,e_9$ and $\Psi=e_0-i\,e_9$.

**Exercise 7.4.** Check the claim of Section 7.6 that $\Lambda=1+X$ satisfies $\Lambda^T\eta\Lambda=\eta$ to first order exactly when $\eta X$ is antisymmetric, and give an example of a nonzero $2\times2$ such $X$ for $\eta=\mathrm{diag}(1,-1)$.

**Exercise 7.5.** A homogeneous commuting state with $m=2$, $\lambda=-3$ and $S=1$ is given. Compute $\rho$, $p$, $w$, $\mathrm{KE}_L$ and $\mathrm{PE}_L$. Is it phantom?

**Exercise 7.6.** Verify the Stage-1 example of Section 7.10: $m=4$, $\lambda=7/6$, $S=-75899/7560$. Compute $\mathrm{PE}_L$ and $w$ and confirm $w>1$.

**Exercise 7.7.** In the homogeneous background of Section 7.10 with $U=0$, the 7-volume doubles between two times. What happens to $S$, $\rho$ and $w$?

**Exercise 7.8.** For the rest solutions with negative frequency, $\Psi=e^{+imx_4}u$ with $-i\gamma^4u=-u$, show that $S=-J^4$ and $\rho=-mJ^4=mS$. Which sign of $J^4$ gives a negative energy density now?

**Exercise 7.9.** For a moving plane wave with $m=3$, $k_1=4$ (all other $k$ zero except $k_4$) and positive frequency, find $\omega$ and the ratio $S/J^4$.

**Exercise 7.10.** For the static source of Section 7.12 verify $v^\dagger Cv=32$ with the table of $C$, and compute $\omega$ from $\omega^2=M_{\mathrm{eff}}^2-9H^2$.

**Exercise 7.11.** Show from Theorem 7.7 that for the homogeneous state the image $\gamma^8\Psi$ has the pressure $-p$ and the same $w$.

**Exercise 7.12.** In the proof of Theorem 7.5, take flat space with the vielbein $e_\mu{}^a=\delta_\mu{}^a$ and a small vector field $\xi(x)$ that vanishes near the boundary. Compute $\delta_\xi e_\mu{}^a$, the matrix $X_{cd}$, its symmetric part and its antisymmetric part, and state what the proof gives.

**Exercise 7.13.** For the column $v$ of the static source of Section 7.12 ($H=1$, $M_{\mathrm{eff}}=-5$, so $N=5\gamma^4+3\gamma^4\gamma^0=\gamma^4(5+3\gamma^0)$), use the tables of Sections 2.8 and 2.9 to (a) compute $\gamma^0v$ and verify $Nv=4i\,v$; (b) compute $b=\gamma^4v$ and $a=\gamma^0Cv$; (c) compute $\gamma^3b$ and $\gamma^7b$, and show $V_3(v)=a^\dagger\gamma^3b=0$ and $V_7(v)=a^\dagger\gamma^7b=0$.

### 7.17 Answers to the exercises

**Answer 7.1.** Write $A=C\gamma^1$ (real antisymmetric). $\partial\mathcal L/\partial\Psi_a^\ast=\tfrac12(A\partial_1\Psi)_a-m(C\Psi)_a$ and $\partial\mathcal L/\partial(\partial_1\Psi_a^\ast)=-\tfrac12(A\Psi)_a$. The Euler–Lagrange expression is $\tfrac12A\partial_1\Psi-mC\Psi+\tfrac12A\partial_1\Psi=C(\gamma^1\partial_1\Psi-m\Psi)$, so the equation is $\gamma^1\partial_1\Psi=m\Psi$: Section 7.2 with only one derivative direction and no connection.

**Answer 7.2.** $U'=\lambda S+\mu S^2$, so $SU'-U=\lambda S^2+\mu S^3-\tfrac\lambda2S^2-\tfrac\mu3S^3=\tfrac\lambda2S^2+\tfrac{2\mu}3S^3$. The trace is $-mS+7SU'-8U=-mS+7\lambda S^2+7\mu S^3-4\lambda S^2-\tfrac{8\mu}3S^3=-mS+3\lambda S^2+\tfrac{13\mu}3S^3$.

**Answer 7.3.** From the table, $(Bu)_0=i\,u_9$ and $(Bu)_9=-i\,u_0$. So $J^4=\Psi_0^\ast\,i\,\Psi_9-\Psi_9^\ast\,i\,\Psi_0$. For $e_0+e_9$: $i-i=0$. For $e_0+ie_9$: $i\cdot i-(-i)\,i=-1-1=-2$. For $e_0-ie_9$: $i(-i)-(i)(i)=1+1=2$. All three have $\Psi^\dagger\Psi=2$, yet the charge density is $0$, $-2$ and $+2$.

**Answer 7.4.** $\Lambda^T\eta\Lambda=\eta+X^T\eta+\eta X+O(X^2)$, so the condition is $X^T\eta+\eta X=0$, which says $(\eta X)^T=-\eta X$ because $\eta^T=\eta$. Example: $X=\begin{pmatrix}0&\beta\\ \beta&0\end{pmatrix}$ gives $\eta X=\begin{pmatrix}0&\beta\\-\beta&0\end{pmatrix}$, antisymmetric: an infinitesimal boost, $\Lambda=\begin{pmatrix}1&\beta\\ \beta&1\end{pmatrix}$.

**Answer 7.5.** $\rho=mS+\tfrac\lambda2S^2=2-\tfrac32=\tfrac12$, $p=\tfrac\lambda2S^2=-\tfrac32$, $w=-3$, $\mathrm{KE}_L=\tfrac12S(m+\lambda S)=\tfrac12(2-3)=-\tfrac12$, $\mathrm{PE}_L=\tfrac12mS=1$. Check: $\mathrm{KE}_L+\mathrm{PE}_L=\tfrac12=\rho$ and $\mathrm{KE}_L-\mathrm{PE}_L=-\tfrac32=p$. With $\rho>0$ and $\mathrm{KE}_L<0$ it is phantom ($w<-1$), at the level of these classical formulas.

**Answer 7.6.** $\mathrm{PE}_L=\tfrac12mS=2\cdot(-75899/7560)=-75899/3780<0$. $w=\lambda S/(2m+\lambda S)$ with $\lambda S=\tfrac76\cdot(-\tfrac{75899}{7560})=-\tfrac{531293}{45360}$ and $2m=8=\tfrac{362880}{45360}$, so $2m+\lambda S=-\tfrac{168413}{45360}$ and $w=\tfrac{531293}{168413}=\tfrac{75899}{24059}\approx3.155>1$ (divide numerator and denominator by 7). The energy density is positive, $\rho=mS+\tfrac\lambda2S^2\approx-40.16+58.80\approx18.64$, while $\mathrm{PE}_L<0$: exactly the situation in which Section 7.10 says $w>1$.

**Answer 7.7.** $S\,V$ is constant, so $S$ halves. With $U=0$, $\rho=mS$ halves as well (dust), and $p=0$, $w=0$ throughout.

**Answer 7.8.** $-i\gamma^4u=-u$ gives $J^4=u^\dagger C(-i\gamma^4)u=-u^\dagger Cu=-S$. With $\partial_4\Psi=+im\Psi$, $K_4=\tfrac i2(im+im)\Psi^\dagger B\Psi=-mJ^4$, and $\mathcal L_s=0$ on shell, so $\rho=-mJ^4=mS$. Now a positive $J^4$ (equivalently $S<0$) gives a negative energy density.

**Answer 7.9.** $\omega^2=m^2+k_1^2=9+16=25$, $\omega=5$. Theorem 7.6: $S/J^4=M/\omega=3/5$.

**Answer 7.10.** With $(Cu)_0=-u_4$, $(Cu)_1=-u_5$, $(Cu)_4=-u_0$, $(Cu)_5=-u_1$, $(Cu)_8=u_{12}$, $(Cu)_9=u_{13}$, $(Cu)_{12}=u_8$, $(Cu)_{13}=u_9$: $v^\dagger Cv=-2\,\mathrm{Re}(v_0^\ast v_4)-2\,\mathrm{Re}(v_1^\ast v_5)+2\,\mathrm{Re}(v_8^\ast v_{12})+2\,\mathrm{Re}(v_9^\ast v_{13})=-2(1)-2\,\mathrm{Re}\bigl((-3i)(-3i)\bigr)+2(9)+2\,\mathrm{Re}\bigl((i)(i)\bigr)=-2+18+18-2=32$. And $\omega^2=25-9=16$, $\omega=4$.

**Answer 7.11.** Theorem 7.7 gives $T_{\mu\nu}\to-T_{\mu\nu}$ with $(m,\lambda)\to(-m,-\lambda)$, so $\rho\to-\rho$ and $p\to-p$; directly, $p=\tfrac\lambda2S^2\to-\tfrac\lambda2S^2$ with the same $S$. The ratio $w=p/\rho$ is unchanged.

**Answer 7.12.** In flat space $\Gamma=0$ and $\omega=0$. The vielbein is constant, so $\delta_\xi e_\mu{}^a=\xi^\lambda\partial_\lambda\delta_\mu{}^a+\delta_\lambda{}^a\partial_\mu\xi^\lambda=\partial_\mu\xi^a$. Then $X^c{}_d=\delta_\xi e_\mu{}^c\,e_d{}^\mu=\partial_d\xi^c$ and $X_{cd}=\partial_d\xi_c$ with $\xi_c=\eta_{ca}\xi^a$. Its symmetric part is $\tfrac12(\partial_d\xi_c+\partial_c\xi_d)$ and its antisymmetric part $\varepsilon_{cd}=\tfrac12(\partial_d\xi_c-\partial_c\xi_d)$, an infinitesimal frame rotation that changes from point to point. The field changes by $\xi^\lambda\partial_\lambda\Psi$. The proof then gives $\int T^{\sigma\mu}\partial_\mu\xi_\sigma\,d^8x=0$ on shell for every such $\xi$, and after the integration by parts $\partial_\mu T^{\sigma\mu}=0$: the flat-space conservation law of Section 5.7, now for the symmetric tensor of Theorem 7.4.

**Answer 7.13.** The column is $v=(1,3i,0,0,1,-3i,0,0,-3,-i,0,0,-3,i,0,0)^T$; only the places $I=\{0,1,4,5,8,9,12,13\}$ are nonzero, and every column below is written by its entries in these eight places, in this order (the other eight entries are zero). (a) The table of $\gamma^0$ says $(\gamma^0u)_i=u_{i+8}$ for $i\le7$ and $u_{i-8}$ for $i\ge8$, so $\gamma^0v$ has the entries $(-3,-i,-3,i,1,3i,1,-3i)$. Then $w:=5v+3\gamma^0v$ has the entries $(-4,12i,-4,-12i,-12,4i,-12,-4i)$; for example $5\cdot1+3\cdot(-3)=-4$ and $5\cdot3i+3\cdot(-i)=12i$. The rows of $\gamma^4$ in the places of $I$ read $(\gamma^4u)_0=-u_{13}$, $(\gamma^4u)_1=u_{12}$, $(\gamma^4u)_4=u_9$, $(\gamma^4u)_5=-u_8$, $(\gamma^4u)_8=u_5$, $(\gamma^4u)_9=-u_4$, $(\gamma^4u)_{12}=-u_1$, $(\gamma^4u)_{13}=u_0$, so $Nv=\gamma^4w$ has the entries $(4i,-12,4i,12,-12i,4,-12i,-4)$. And $4iv$ has the same entries: for example $4i\cdot3i=-12$, $4i\cdot(-3i)=12$, $4i\cdot(-3)=-12i$ and $4i\cdot(-i)=4$. (b) With the same rows of $\gamma^4$, $b=\gamma^4v$ has the entries $(-v_{13},v_{12},v_9,-v_8,v_5,-v_4,-v_1,v_0)$, that is $(-i,-3,-i,3,-3i,-1,-3i,1)$. The table of $C$ says $(Cu)_i=-u_{i+4}$ for $i\le3$, $-u_{i-4}$ for $4\le i\le7$, $u_{i+4}$ for $8\le i\le11$ and $u_{i-4}$ for $i\ge12$. So $Cv$ has the entries $(-v_4,-v_5,-v_0,-v_1,v_{12},v_{13},v_8,v_9)$, that is $(-1,3i,-1,-3i,-3,i,-3,-i)$, and then $a=\gamma^0(Cv)$ has the entries $(-3,i,-3,-i,-1,3i,-1,-3i)$. Both $a$ and $b$ vanish outside $I$. (c) The rows of $\gamma^3$ in the places of $I$ read $-13,+12,-9,+8,+5,-4,+1,-0$, so $\gamma^3b$ has the entries $(-b_{13},b_{12},-b_9,b_8,b_5,-b_4,b_1,-b_0)$, that is $(-1,-3i,1,-3i,3,i,-3,i)$. The conjugates of the entries of $a$ are $(-3,-i,-3,i,-1,-3i,-1,3i)$, and the eight products $a_k^\ast(\gamma^3b)_k$ are

$$
3,\quad -3,\quad -3,\quad 3,\quad -3,\quad 3,\quad 3,\quad -3,
$$

whose sum is $V_3(v)=0$. The rows of $\gamma^7$ in the places of $I$ read $+8,+9,-12,-13,-0,-1,+4,+5$, so $\gamma^7b$ has the entries $(b_8,b_9,-b_{12},-b_{13},-b_0,-b_1,b_4,b_5)$, that is $(-3i,-1,3i,-1,i,3,-i,3)$, and the eight products $a_k^\ast(\gamma^7b)_k$ are

$$
9i,\quad i,\quad -9i,\quad -i,\quad -i,\quad -9i,\quad i,\quad 9i,
$$

whose sum is $V_7(v)=0$. Together with the support argument of Section 7.12 for $p=1,2,5,6$, all six $V_p$ vanish. (A computer check with the fixture gammas of `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` gives the same, and finds that the three-gamma bilinears $\bar v\gamma^1\gamma^2\gamma^3v$, $\bar v\gamma^1\gamma^6\gamma^7v$, $\bar v\gamma^2\gamma^5\gamma^7v$ and $\bar v\gamma^3\gamma^5\gamma^6v$ equal $24$, $24$, $-24$ and $24$: these are not among the $V_p$ and do not enter the Einstein equations for this state.)
