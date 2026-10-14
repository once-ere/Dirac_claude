# dirac16complex and dirac16complex00: Lagrangians, field equations, energy-momentum tensors and equations of state in an arbitrary and in the primordial gravitational field

## Stage 5, document A: the second-quantized Grassmann field and the classical commuting Pin(4,4) spinor field side by side, with exact verification records

## 1. Summary

### 1.1 What is defined

This document treats two fields on an 8-dimensional manifold with a metric of signature (4,4). Both are maps $\Psi: M^8\to\mathbb C^{16}$ whose 16 components transform together as the irreducible complex Pin(4,4) spinor of the earlier stages; they differ only in the statistics of the components.

- **dirac16complex** is the second-quantized field of Stages 1-4: its components are Grassmann-odd (anticommuting), and canonical quantization with respect to the time $x_4$ gives the equal-time anticommutator $\{\Psi,\Psi^\dagger\}=B\,\delta^7/\sqrt{|g|}$ with the indefinite (Krein) matrix $B=-iC\gamma^4$ (Section 3.1).
- **dirac16complex00** is new in Stage 5: its 16 components are commuting complex numbers (c-number fields). It is the classical analogue of Dirac's 1928 wave function, not a quantum field (Section 3.2).

Both fields get the same Lagrangian (L1) with the canonical spin connection, an explicit mass term $-m\sqrt{|g|}\,\bar\Psi\Psi$ and an interaction $U(\bar\Psi\Psi)$, default $U=\tfrac\lambda2(\bar\Psi\Psi)^2$ (Section 4). Sections 5 and 6 give the Euler-Lagrange equations, the energy-momentum tensor (an operator for dirac16complex, a c-number field for dirac16complex00), the conserved current, the energy density, the pressures, two kinetic/potential splits and the equations of state, all in an arbitrary gravitational field. Part 2 of this document (Sections 7-11) contains the statistics-dependent statements (indefinite charge and unbounded classical energy of dirac16complex00), the primordial field, the verification records, the reproduction commands and the limitations.

### 1.2 What is proved

Every statement below is an exact identity verified by two independent implementations: the Wolfram verifier `scripts/verify_dirac16complex00.wls` (package `wolfram/Dirac16Complex00.wl`, Wolfram Language 15.0.1; report `artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json`, 46 of 46 checks true, formulas in `artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json`) and the independent sympy checker `scripts/check_dirac16complex00.py` (report `artifacts/dirac16complex/pair-creation/python-dirac16complex00-report.json`, 49 of 49 checks true). The Python checker compares 89 items with the Wolfram report (exact values, formulas and statements); none fails (check S5_agreesWithWolfram). Where a statement holds for all metrics, it is verified at exact points of explicit test geometries (Section 2.4), not as a symbolic identity in an arbitrary metric; the proofs given in the text are general.

1. The 16 commuting components of dirac16complex00 carry exactly the Pin(4,4) representation of the 16 Grassmann components of dirac16complex (Section 3.2).
2. The notebook's real Lagrangian Lg[] is a pure divergence with empty field equations for a real Grassmann field (Stage 1, re-verified), but non-trivial for a real commuting field, where its Euler-Lagrange equation is the Dirac equation with $m=-HM$; (L1) for commuting components is the complexification of Lg[] (Section 3.3).
3. (L1) is real for commuting components and Hermitian for Grassmann components, by one argument (Section 4.1).
4. The mass term is linear in $m$, quadratic in the components, nonzero for both statistics, and changes the field equation and the dispersion relation (Section 4.2).
5. The coupling to the spin connection and to gravity is non-trivial: $\gamma^\mu\Omega_\mu\ne0$, the spin curvature is nonzero, the Lichnerowicz formula holds with $c=-\tfrac14$, and the connection term of the field equation is nonzero in all 16 components at the curved test points (Section 4.4).
6. The Euler-Lagrange equations of the commuting field have exactly the form derived in Stage 1 for the Grassmann field, for the quartic and for every smooth $U$ (Section 5).
7. The tensor $T_{\mu\nu}$ of Section 6 is the symmetric part of the exact vielbein variation of the action, off shell, at general non-diagonal frames; it is symmetric, real, conserved on shell, with on-shell trace $-mS+7SU'-8U$; the current is conserved; the observer identities and the homogeneous equations of state hold (Section 6).

The pairing theorems T1-T3 (the chirality map $\Psi\to\gamma^8\Psi$, the mirror map, the Kohn-Sham block map) and the Wick sign of the interaction are the subject of document B, `provenance/DIRAC16COMPLEX_PAIR_CREATION.md` (reports `wolfram-pairing-report.json`, 141 of 141 checks true, and `python-pairing-report.json`, 172 of 172 checks true, in the same directory). Erratum E5.1 of `handoff/specs/STAGE5_SPEC.md` binds this document as well: the cancellation $T^{\rm pair}_{\mu\nu}=0$ of the T1 corollary is a statement about classical fields (commuting c-number fields, or two independent classical fields in the correlated configuration $\Psi_-=\gamma^8\Psi_+$); for the quantized field dirac16complex no reading gives a cancellation between two independent, consistently quantised universes. Nothing in this document concerns the creation of universes: no creation process, rate, amplitude or wave function is derived here.

### 1.3 Where each result is verified

Check names starting with C00_ are in the Wolfram report, those starting with S5_ in the Python report. "Stage 1" means a cited check of the committed Stage-1 reports (Section 2.5).

| result | section | Wolfram check | Python check |
| --- | --- | --- | --- |
| exact fixture: $\gamma^a$, $C$, $\gamma^8$, $B$, the 28 $S^{ab}$ | 2.2 | C00_fixture_matchesStage1Construction | S5_fixture_matchesContractConstruction |
| facts about $\gamma^8$, $C$, $B$ | 2.3 | C00_algebra_leadFacts | S5_algebra_leadFacts |
| only $\omega_{[cab]}$ enters the symmetrized kinetic term | 2.3, 4.4 | C00_algebra_anticommutatorTotallyAntisymmetric | S5_algebra_anticommutatorTotallyAntisymmetric |
| same Pin(4,4) module for both statistics | 3.2 | C00_algebra_pinModuleAndSpinInvariance | S5_algebra_pinModuleAndSpinInvariance |
| real restriction trivial for Grassmann components | 3.3 | C00_realRestriction_grassmannFlatTrivial, C00_realRestriction_grassmannCurvedTrivial, C00_realRestriction_grassmannComplexDecomposition | S5_realRestriction_grassmannFlatTrivial, S5_realRestriction_grassmannCurvedTrivial, S5_realRestriction_grassmannComplexDecomposition |
| real restriction non-trivial for commuting components | 3.3 | C00_realRestriction_commutingNonTrivial, C00_realRestriction_commutingNotebookContraction, C00_realRestriction_commutingFlatDecomposition | S5_realRestriction_commutingNonTrivial, S5_realRestriction_commutingNotebookContraction, S5_realRestriction_commutingFlatDecomposition |
| (L1) is the complexification of Lg[] | 3.3 | C00_realRestriction_relationToL1 | S5_realRestriction_relationToL1 |
| reality / Hermiticity of (L1) | 4.1 | C00_lagrangian_realCommuting, C00_lagrangian_coefficientHermiticity, C00_lagrangian_grassmannFlatHermitianAndEL | S5_lagrangian_realCommuting, S5_lagrangian_coefficientHermiticity, S5_lagrangian_grassmannFlatHermitianAndEL |
| mass term nonzero, commuting | 4.2 | C00_massTerm_commutingExplicitSpinors | S5_massTerm_commutingExplicitSpinors |
| mass term nonzero, Grassmann | 4.2 | C00_massTerm_grassmannNonzero | S5_massTerm_grassmannNonzero |
| mass enters the dispersion | 4.2 | C00_massTerm_dispersionFlat | S5_massTerm_dispersionFlat |
| coupling to the spin connection and gravity | 4.4 | C00_connection_nonTrivialCoupling, C00_geometry_G4Generic | S5_connection_nonTrivialCoupling, S5_geometry_G4Generic |
| connection term in the field equation | 4.4 | C00_connection_OmegaTermInFieldEquation | S5_connection_OmegaTermInFieldEquation |
| Euler-Lagrange equations, commuting | 5 | C00_EL_commutingFlat, C00_EL_commutingCurved | S5_EL_commutingFlat, S5_EL_commutingCurved |
| Euler-Lagrange equations, smooth $U$ | 5 | C00_EL_commutingGeneralSmoothU | S5_EL_commutingGeneralSmoothU |
| identical form for both statistics | 5 | C00_EL_identicalFormBothStatistics (Grassmann curved: Stage 1) | S5_EL_identicalFormBothStatistics, S5_EL_grassmannCurved |
| $T_{\mu\nu}$ from the vielbein variation | 6.1 | C00_EMT_vielbeinVariation | S5_EMT_vielbeinVariation |
| symmetric and real | 6.2 | C00_EMT_symmetricAndReal | S5_EMT_symmetricAndReal |
| conservation on shell | 6.2 | C00_EMT_conservationOnShell | S5_EMT_conservationOnShell |
| trace on shell | 6.2 | C00_EMT_traceOnShell | S5_EMT_traceOnShell |
| conservation and reality for every smooth $U$ | 6.2 | C00_EMT_generalSmoothU | S5_EMT_generalSmoothU |
| current | 6.3 | C00_current_conservationAndReality | S5_current_conservationAndReality |
| observer identities (Gaussian normal time) | 6.4 | C00_EMT_observerSplitGaussianNormal | S5_EMT_observerSplitGaussianNormal |
| homogeneous equations of state | 6.5 | C00_EMT_homogeneousEquationsOfState | S5_EMT_homogeneousEquationsOfState |
| indefinite charge density (dirac16complex00) | 7 | C00_charge_indefinite | S5_charge_indefinite |
| classical energy unbounded below (dirac16complex00) | 7 | C00_energy_unboundedBelow | S5_energy_unboundedBelow |
| primordial field, Stage-2 chart | 8 | C00_primordial_geometryMatchesStage2, C00_primordial_ELcommuting, C00_primordial_homogeneousState, C00_primordial_staticFieldSourcedExactly | S5_primordial_geometryMatchesStage2, S5_primordial_ELcommuting, S5_primordial_homogeneousState, S5_primordial_staticFieldSourcedExactly, S5_static_sourceProperChart |
| static warped form, Stage-4 blocks | 8 | C00_static_geometryAndReducedEquation, C00_static_blocksFromStage4Theory, C00_static_classicalModeIsKreinWeightedKS, C00_static_classicalEnergyKreinSigned, C00_static_KSorbitalEnergySplit | S5_static_geometryAndReducedEquation, S5_static_blocksFromStage4Theory, S5_static_classicalModeIsKreinWeightedKS, S5_static_classicalEnergyKreinSigned, S5_static_KSorbitalEnergySplit, S5_static_meanFieldOneBodyEMT |
| cited Stage 1-4 reports are true and current | 2.5 | C00_citation_stage1to4ReportsMatchSources | S5_citation_pythonStage1to4ReportsMatchSources |
| bookkeeping and agreement | 9 | C00_internal_noException, C00_verifier_expectedCheckCount | S5_internal_noException, S5_agreesWithWolfram |

### 1.4 Scope relative to the Revision record

This is the old Stage-5 record. It works in the frame of Stages 2 and 4: coordinates counted from 0, $x=(x_0,\dots,x_7)$, with $x_0$ the hidden space direction, $x_1,x_2,x_3$ ordinary space, $x_4$ the time and $x_5,x_6,x_7$ the extra times; in the Stage-2 chart $z=6Hx_0$ and the extra-time scale factor is $\sin^{1/6}z\,e^{-a_4(t)}$ with an arbitrary function $a_4$, and the Kohn-Sham model of Stage 4 (Section 8, document B) uses the static member $a_4=$ const, in which the extra times are frozen. The later Revision record (binding `Revision/SPEC.md`) uses the author's coordinates $x_1,\dots,x_8$, with $x_8$ the hidden space direction ($z=6Hx_8$) and the extra times $x_5,x_6,x_7$ deflating exponentially (scale factor $e^{-a_4}\sin^{1/6}z$ with $a_4$ increasing), and derives the field equations for $a_4(x_4)$; its record for the commuting field is `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md`, and its answer to the pair-creation request is `Revision/docs/PAIR_CREATION_PROOFS.md` Section 11.3. The arbitrary-field statements of Sections 2-6 below do not depend on the chart. Where a statement here refers to the Stage-2 chart or to the static Stage-4 form, it is a statement about that old frame, not about the author's deflating geometry, and it does not replace the Revision record. The two records agree where they overlap (the classical energy of dirac16complex00 is unbounded below, its charge density is indefinite, and the T1 cancellation is classical only, as in `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md` Section 7.3).

## 2. Conventions

### 2.1 Inherited conventions

All conventions are those of `handoff/specs/CONTRACT.md` (with its errata, Section 11) and of Stages 1-4; this document changes none of them.

- Counting from 0: coordinates $x=(x_0,\dots,x_7)$, $x_4$ the evolution time, frame indices $a,b,c=0..7$, curved indices $\mu,\nu=0..7$, spinor indices $0..15$.
- Tangent metric $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$: directions 0..3 space-like, 4..7 time-like.
- Vielbein $e_\mu{}^a$, inverse $e_a{}^\mu$, $g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b$, curved gammas $\gamma^\mu=e_a{}^\mu\gamma^a$, $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$.
- Canonical spin connection from the vielbein postulate, $\omega_\mu{}^a{}_b=e_b{}^\nu(\Gamma^\rho{}_{\mu\nu}e_\rho{}^a-\partial_\mu e_\nu{}^a)$, $\omega_{\mu ab}=\eta_{ac}\,\omega_\mu{}^c{}_b$, and

$$
\Omega_\mu=\tfrac12\,\omega_{\mu ab}S^{ab}=\tfrac18\,\omega_{\mu ab}[\gamma^a,\gamma^b],\qquad D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi,\qquad D_\mu\bar\Psi=\partial_\mu\bar\Psi-\bar\Psi\,\Omega_\mu .
$$

- Adjoint and Krein matrix: $C=\sigma_{16}=\gamma^0\gamma^1\gamma^2\gamma^3$, $\bar\Psi=\Psi^\dagger C$, $S:=\bar\Psi\Psi$, $B=-iC\gamma^4$; chirality $\gamma^8=\gamma^0\gamma^1\cdots\gamma^7=\mathrm{diag}(-I_8,+I_8)$.
- Energy-momentum tensor: $T_{\mu\nu}=-\frac{2}{\sqrt{|g|}}\frac{\delta\mathcal S}{\delta g^{\mu\nu}}$; in Gaussian normal time ($g_{44}=-1$, $g_{4i}=0$) the energy density is $\rho=T_{44}$, so $T^4{}_4=-\rho$, and the pressures are $p_{(i)}=T^i{}_i$ (no sum, $i\ne4$). This is the Stage-1 convention, kept unchanged.

### 2.2 The exact fixture

The gamma matrices are the notebook's $\gamma^a=T16^A[a]$ (16x16, real, integer), stored with $C$, $\gamma^8$, $B$ and the 28 generators $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$ in `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` (SHA-256 8b4f1546...e02653b, recorded in both reports). The Wolfram verifier compares every entry with the Stage-1 construction, and the Python checker rebuilds the same objects from CONTRACT Section 1 (module `scripts/d16c_exact.py`) and compares them with the fixture: $\gamma^a$, $C$, the chirality, $B$ and all 28 $S^{ab}$ agree exactly.

```
checks
  C00_fixture_matchesStage1Construction: wolfram-dirac16complex00
  S5_fixture_matchesContractConstruction: python-dirac16complex00
```

### 2.3 Facts about gamma^8, C and B used below

**Result 2.1** (exact, both implementations).

1. $\{\gamma^a,\gamma^b\}=2\eta^{ab}I_{16}$; $\gamma^a$ is symmetric for $a<4$ and antisymmetric for $a\ge4$ (Python: clifford, gammaSymmetryPattern).
2. $C$ is real symmetric, $C^2=I_{16}$, $C=\gamma^0\gamma^1\gamma^2\gamma^3=\mathrm{diag}(-\sigma,\sigma)$ with $\sigma=\begin{pmatrix}0&I_4\\ I_4&0\end{pmatrix}$; its characteristic polynomial is $(x-1)^8(x+1)^8$, so the Hermitian form $\Psi^\dagger C\Psi$ has signature (8,8).
3. $C\gamma^a$ and $CS^{ab}$ are real antisymmetric (hence anti-Hermitian) for every $a,b$.
4. $B=-iC\gamma^4$ is Hermitian, $B^2=I_{16}$, its eigenvalues are $+1$ and $-1$ eight times each, $[B,C]=0$, $BC=-i\gamma^4$, and $C\gamma^4=iB$.
5. $\gamma^8$ is Hermitian, $(\gamma^8)^2=I_{16}$, $\gamma^8=\mathrm{diag}(-I_8,+I_8)$; it anticommutes with every $\gamma^a$ and commutes with $C$, with every bivector and with every $S^{ab}$ (hence with every $\Omega_\mu$); $\gamma^8B\gamma^8=-B$ and $\gamma^8(C\gamma^a)\gamma^8=-C\gamma^a$.
6. $\{\gamma^c,S^{ab}\}=\gamma^c\gamma^a\gamma^b$ for distinct $c,a,b$ and $0$ for $c\in\{a,b\}$; $C\{\gamma^c,S^{ab}\}$ is symmetric and $C[\gamma^c,S^{ab}]$ antisymmetric; $[S^{ab},\gamma^c]=\eta^{bc}\gamma^a-\eta^{ac}\gamma^b$. Consequently
$$
\tfrac12\,\bar\Psi\{\gamma^\mu,\Omega_\mu\}\Psi=\tfrac14\,\omega_{[cab]}\,\bar\Psi\gamma^c\gamma^a\gamma^b\Psi,\qquad \omega_{cab}=e_c{}^\mu\omega_{\mu ab}:
$$
only the totally antisymmetric part of the connection enters the symmetrized kinetic term.

Items 4 and 5 are used in Section 3.1 (Krein structure) and in document B (the chirality map). Item 6 is used in Section 4.4.

```
checks
  C00_algebra_leadFacts, C00_algebra_anticommutatorTotallyAntisymmetric:
      wolfram-dirac16complex00
  S5_algebra_leadFacts, S5_algebra_anticommutatorTotallyAntisymmetric:
      python-dirac16complex00
```

### 2.4 Test geometries

The curved-space identities are verified exactly at points of four families of vielbeins (descriptions in `dirac16complex00-theory.json`, key testGeometries):

- **G1** (Stage 1): $e_\mu{}^a=\delta+P(x)$ with a polynomial $P$, three rational points p1-p3; general non-diagonal frames.
- **G2** (Stage 1): the Stage-2 primordial field with an arbitrary function $a_4$, three exact points with numbers in $\mathbb Q(\cos z)$ (Python: symbolic $H$ and $a_4'$, $a_4''$).
- **G3** (Stage 1): Bianchi-I frames $h_i=1+x_4^2/(i+2)$ at $x_4\in\{1/3,-2/5,3/7\}$ (Gaussian normal time).
- **G4** (new): a generic integer frame $e(x)=E_0+x^lE_{1,l}+\tfrac12x^lx^kE_{2,lk}$ at $x=0$, with $E_0=UL$ ($U$, $L$ unitriangular with entries in $\{-1,0,1\}$), $\det E_0=1$, 35 nonzero off-diagonal entries of $E_0$, $g^{44}=-49$, signature (4,4) and scalar curvature $R=82754$ (identical in both reports).

Field data at a point (value, first and second derivatives of $\Psi$ and $\Psi^\dagger$) come from the Stage-1 linear congruential generator with recorded seeds (Wolfram); the Python checker reproduces these data exactly (agreement item definitions.randomFieldDataReproduced) and in addition uses its own independent random data for its own checks.

### 2.5 How the checks treat the two statistics

For commuting components the Wolfram verifier treats $\Psi_a$, $\Psi^\ast_a$ and their derivatives at a point as independent commuting symbols; the Python checker does the same ("commuting proxy": $\chi=\Psi^\ast$ independent) and decides reality by the swap symmetry of the real-coefficient polynomial $\mathcal L(\chi,\psi)$ and by exact Gaussian-rational data with $\Psi^\dagger=\overline{\Psi}^T$. Grassmann statements are verified in an exact Grassmann algebra (flat: 288 odd generators $\Psi_a,\Psi^\ast_a,\partial_\mu\Psi_a,\partial_\mu\Psi^\ast_a$ in the Wolfram verifier; Python module `scripts/grassmann_algebra.py`) or cited from Stage 1. Each report checks that every cited Stage 1-4 check is true and that the recorded SHA-256 of its source equals the file in the repository now: the Wolfram verifier cites 20 Stage-1 geometry checks (among them LAG_hermiticity_G1/G2, LAG_eulerLagrangePsibar/Psi_G1/G2, LAG_notebookLgGrassmannTrivial_G1/G2, LAG_localSpinInvariance_G1/G2, EMT_conservation_G1/G2, EMT_trace_G1/G2, EMT_variation_G3, QNT_canonicalMomentum_G1/G2), 8 Stage-1 algebra checks (ALG_gamma8Map, ALG_pinLiftCharacter, ALG_invariantForms, ALG_chargeFormB, QNT_kreinSignature, QNT_flatModeHamiltonian, ALG_pinIrreducibleComplex, ALG_spinDecomposition), 6 Stage-2 checks and 4 Stage-4 checks; the Python checker cites the committed Python geometry, Grassmann-demonstration, algebra, primordial and Kohn-Sham theory reports.

```
checks
  C00_citation_stage1to4ReportsMatchSources: wolfram-dirac16complex00
  S5_citation_pythonStage1to4ReportsMatchSources: python-dirac16complex00
```

## 3. The two fields

### 3.1 dirac16complex: the second-quantized Grassmann field

dirac16complex is the field of Stages 1-4 (`provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md`, cited below as "Stage 1"): $\Psi=(\Psi_0,\dots,\Psi_{15})^T$ with complex Grassmann-odd components, $\Psi_a\Psi_b=-\Psi_b\Psi_a$, $\Psi_a\Psi^\ast_b=-\Psi^\ast_b\Psi_a$, $(\theta_1\theta_2)^\ast=\theta_2^\ast\theta_1^\ast$, a section of the complexified spinor bundle (Stage 1 Section 4). Its quantization with respect to $x_4$ is recalled here because Sections 6 and 7 use it; nothing in it is new.

- **Momenta and constraints** (Stage 1 Sections 10.1-10.2). After adding the total derivative $\tfrac12\partial_4(\sqrt{|g|}\,\bar\Psi\gamma^{x_4}\Psi)$ the Lagrangian is first order, $\Pi=\sqrt{|g|}\,\Psi^\dagger C\gamma^{x_4}$, and the constraints are second class exactly when $g^{44}\ne0$ (checks QNT_canonicalMomentum_G1/G2, cited).
- **Anticommutator** (Stage 1 Section 10.3). At equal $x_4$, $\{\Psi_a(x),\Psi^\dagger_b(y)\}=i[(C\gamma^{x_4})^{-1}]_{ab}\,\delta^7(x-y)/\sqrt{|g|}$, which in Gaussian normal gauge ($g^{44}=-1$, $\gamma^{x_4}=\gamma^4$) is $B_{ab}\,\delta^7(x-y)/\sqrt{|g|}$ with $B=-iC\gamma^4$ (Result 2.1, item 4).
- **Krein space** (Stage 1 Section 10.5, Theorem 10.1). Every Spin(4,4)-invariant Hermitian form on $\mathbb C^{16}$ is even in chirality while $\gamma^4$ is odd, so every candidate charge density built from an invariant form is indefinite of signature (8,8) or vanishes: the canonical state space is a Krein space, intrinsically in signature (4,4). $J=B$ is a fundamental symmetry and the associated positive product is $\Psi^\dagger\Psi$; the $B$-form has signature (4,4) on the positive- and on the negative-frequency spaces (QNT_kreinSignature, cited).
- **Good sector and Fock space** (Stage 1 Sections 10.6-10.7). The flat one-particle Hamiltonian $h_k=-im\gamma^4-\gamma^4\sum_{j\ne4}k_j\gamma^j$ is Hermitian and commutes with $B$ exactly when $k_5=k_6=k_7=0$ (QNT_flatModeHamiltonian, cited). In this reduced (4+1)-dimensional sector the positive ($J=B$) quantization with a filled Dirac sea gives a normal-ordered Hamiltonian $H\ge0$. This last step is derived in Stage 1 Section 10.7 from its Results 10.2, 10.4 and 10.5; it is not a machine check there or here.

The energy-momentum tensor of dirac16complex (Section 6) is the same expression in the field operators, normal ordered with respect to the free Krein vacuum as in Stage 1. Its quantum reading under the chirality map is fixed by erratum E5.1 (Section 1.2): the image field $\gamma^8\Psi$ has the anticommutator $-B$, is the same quantum system, and has its own $x_4$-generator, charge and metric energy-momentum tensor $+H_+$, $+Q_+$, $+T_+$ (document B Section 3; `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md` Section 7.3).

### 3.2 dirac16complex00: the classical commuting Pin(4,4) spinor field

**Definition.** dirac16complex00 is a map $\Psi: M^8\to\mathbb C^{16}$ whose 16 components $\Psi_0,\dots,\Psi_{15}$ are commuting complex-valued functions (c-number fields), transforming together as a Pin(4,4) spinor: $\Psi\to R\Psi$ under a local Spin(4,4) transformation $R(x)$ (with $\Omega_\mu\to R\Omega_\mu R^{-1}-(\partial_\mu R)R^{-1}$), and $\Psi\to u\Psi$ under a Pin(4,4) unit vector $u=u_a\gamma^a$. It is the analogue, in signature (4,4), of the 4-component wave function of Dirac's 1928 equation: a classical spinor-valued field, not an operator.

**Result 3.1** (same representation). $\mathbb C^{16}$ is an irreducible complex Pin(4,4) module: the commutant of the $\gamma^a$ is 1-dimensional. Under Spin(4,4) it splits into the two chiral halves (commutant of the $S^{ab}$: dimension 2). Every $S^{ab}$ is real with $S^TC+CS=0$, so $R^TCR=C$ and $R^\dagger=R^T$ for $R\in\mathrm{Spin}_0(4,4)$; hence $\Psi^\dagger C\Psi$ is invariant and $\bar\Psi\gamma^c\Psi$ is a vector. The invariant bilinear forms ($S^TX+XS=0$ for all $S^{ab}$) form a 2-dimensional space spanned by $CP_-$ and $CP_+$, $P_\mp=\tfrac12(I\mp\gamma^8)$. These are statements about the 16-dimensional module, not about the statistics of the coefficients: the 16 commuting components of dirac16complex00 carry exactly the representation of the 16 Grassmann components of dirac16complex. The local curved-space covariance of (L1) is Stage 1's LAG_localSpinInvariance, which is a computation with commuting numbers.

```
checks
  C00_algebra_pinModuleAndSpinInvariance: wolfram-dirac16complex00
  S5_algebra_pinModuleAndSpinInvariance: python-dirac16complex00
  ALG_pinIrreducibleComplex, ALG_spinDecomposition: wolfram-algebra (Stage 1, cited)
  LAG_localSpinInvariance_G1, LAG_localSpinInvariance_G2: wolfram-geometry (cited)
```

**What dirac16complex00 is not.** It is not a quantum field. A quantum theory whose spinor components commute would conflict with the spin-statistics connection (a theorem of relativistic quantum field theory in 3+1 dimensions; no (4,4) version is proved or used here). In this document dirac16complex00 is never quantized: its energy-momentum tensor, current and energies are c-number functions of a classical solution. Two further differences from Dirac's 1928 wave function are proved in Section 7 (part 2): the conserved charge density $J^4=\Psi^\dagger B\Psi$ is indefinite, so there is no probability interpretation, and the classical energy is not bounded below.

**What differs between the two fields.** The Lagrangian, field equations, energy-momentum tensor and current are the same formulas (Sections 4-6). The statistics enters at five places (dirac16complex00-theory.json, key fields.difference):

1. the admissible potentials: any smooth $U(S)$ for dirac16complex00, polynomials in $S$ for dirac16complex because $S^{17}=0$ (Section 4.3);
2. the real restriction: non-trivial for commuting components, a pure divergence for Grassmann components (Section 3.3);
3. the meaning of the energy-momentum tensor: a c-number field versus a normal-ordered operator (Section 6.6);
4. positivity: the charge and energy of dirac16complex00 are indefinite (Section 7, proved), while for the quantized Grassmann field Stage 1 Section 10.7 derives, without a machine check, a positive normal-ordered Hamiltonian in the good sector;
5. the Wick contraction of the interaction in a quasi-free (Gaussian) state, which enters the Kohn-Sham model (document B, pairing module).

### 3.3 The real restriction and the author's Lg[]

The author's notebook writes, with $\sigma_{16}=C$ and $T16^a=\gamma^a$,

$$
\mathrm{Lg}=\sqrt{|g|}\,\Bigl[\Psi^T\sigma_{16}\,T16^\mu D_\mu\Psi+(HM)\,\Psi^T\sigma_{16}\Psi\Bigr]
$$

for a REAL 16-component $\Psi$ (no complex conjugate appears). Whether this is a usable Lagrangian depends on the statistics, through one elementary fact: for any matrix $A$, a quadratic form $\Psi^TA\Psi$ sees only the symmetric part of $A$ if the components commute and only the antisymmetric part if they anticommute. Here $C$ is symmetric and every $C\gamma^a$ is antisymmetric (Result 2.1, items 2-3).

**Grassmann components (Stage 1 Theorem 6.1, re-verified).** The mass term vanishes identically, $\Psi^TC\Psi=0$. Each $\Psi^TC\gamma^a\Psi$ is a nonzero element with 8 monomials (coefficients $\pm2$), and $\Psi^TC\gamma^a\partial_\mu\Psi=\tfrac12\partial_\mu(\Psi^TC\gamma^a\Psi)$ for all $a,\mu$: the flat Lg[] is a nonzero total divergence with identically vanishing Euler-Lagrange expressions. In curved space the derivative-free remainder cancels by the divergence identity of Section 4.4; at the point G1 p1 with $HM=2/3$ the Lagrangian is a nonzero element of the Grassmann algebra with 544 monomials and both Euler-Lagrange expressions vanish identically (both implementations, canonical connection). With the notebook's own contraction of the connection (one $\eta$ missing, CONTRACT Section 3 item 4), the Python checker finds at G1 p1 a nonzero but derivative-free Euler-Lagrange expression: an algebraic condition on $\Psi$, not a first-order field equation. For the complex Grassmann field $\Psi=\rho+i\iota$ ($\rho,\iota$ real Grassmann 16-vectors) one has $\bar\Psi\Psi=2i\,\rho^TC\iota$: the diagonal terms vanish and the mass term of dirac16complex is a pure cross term between two real (Majorana-type) components.

**Commuting components (proved here).** For a real commuting $X$ the same Lagrangian

$$
\mathcal L_{\rm nb}=\sqrt{|g|}\,\bigl[X^TC\gamma^\mu(\partial_\mu X+\Omega_\mu X)+(HM)\,X^TCX\bigr]
$$

has the Euler-Lagrange expression

$$
\frac{\partial\mathcal L_{\rm nb}}{\partial X}-\partial_\mu\frac{\partial\mathcal L_{\rm nb}}{\partial(\partial_\mu X)}=2\sqrt{|g|}\,C\bigl(\gamma^\mu D_\mu X+(HM)\,X\bigr),
$$

with the canonical connection. Its mass part $2\sqrt{|g|}\,CX$ is nonzero, and its kinetic part $2\sqrt{|g|}\,C\gamma^\mu D_\mu X$ contains $\partial_4X$ with the invertible coefficient $2\sqrt{|g|}\,C\gamma^4$, so neither term is a total divergence; $X^TCX$ is the nonzero form of signature (8,8). The field equation is the Dirac equation $\gamma^\mu D_\mu X=mX$ with $m=-HM$. Reason: $X^TC\gamma^\mu\partial_\mu X$ with an antisymmetric matrix is a first-order (symplectic) kinetic term, not half a derivative of $X^TC\gamma^\mu X$, which vanishes identically for commuting $X$. With the notebook's contraction $\Omega^{\rm nb}_\mu$ the Euler-Lagrange expression acquires the extra term $\sqrt{|g|}\,C\{\gamma^\mu,\Omega^{\rm nb}_\mu-\Omega_\mu\}X$, nonzero at the three non-diagonal G1 points and zero at the diagonal G2 points (and in flat space), where $\{\gamma^\mu,\Omega_\mu\}=0$ for both contractions.

**Relation to (L1) (proved here).** For commuting $\Psi=X+iY$ ($X,Y$ real 16-vectors), $\bar\Psi\Psi=X^TCX+Y^TCY$ and the symmetrized kinetic term of (L1) equals $X^TC\gamma^\mu D_\mu X+Y^TC\gamma^\mu D_\mu Y$, with no cross terms. Hence, exactly (value and all first-derivative jets),

$$
\mathcal L_{(L1)}[X+iY]=\sqrt{|g|}\,\bigl[K_R[X]+K_R[Y]-m\,(S_X+S_Y)-U(S_X+S_Y)\bigr],\qquad K_R[Z]=Z^TC\gamma^\mu D_\mu Z,\quad S_Z=Z^TCZ .
$$

For $U=0$ this is $\mathcal L_{\rm nb}[X]+\mathcal L_{\rm nb}[Y]$ with $HM=-m$: (L1) is the complexification of the notebook-type real Lagrangian, two copies coupled only through $U$. $Y=0$ is a consistent truncation (the $Y$ equations vanish identically at $Y=0$), and the $X$ equation is then $2\sqrt{|g|}\,C(\gamma^\mu D_\mu X-(m+\lambda S_X)X)=0$. So the real restriction of dirac16complex00 is exactly the notebook's Lg[] with the canonical connection, and Lg[] is non-trivial for commuting fields. dirac16complex00 itself uses the complex (L1) of Section 4.

```
checks
  C00_realRestriction_grassmannFlatTrivial, C00_realRestriction_grassmannCurvedTrivial,
  C00_realRestriction_grassmannComplexDecomposition,
  C00_realRestriction_commutingNonTrivial (G1 p1-p3, G2 p1),
  C00_realRestriction_commutingNotebookContraction,
  C00_realRestriction_commutingFlatDecomposition,
  C00_realRestriction_relationToL1 (G1 p1): wolfram-dirac16complex00
  S5_realRestriction_grassmannFlatTrivial, S5_realRestriction_grassmannCurvedTrivial,
  S5_realRestriction_grassmannComplexDecomposition,
  S5_realRestriction_commutingNonTrivial (flat, G1 p1-p3, G2),
  S5_realRestriction_commutingNotebookContraction,
  S5_realRestriction_commutingFlatDecomposition,
  S5_realRestriction_relationToL1 (flat, G1 p1, G2): python-dirac16complex00
  LAG_notebookLgGrassmannTrivial_G1, LAG_notebookLgGrassmannTrivial_G2:
      wolfram-geometry (Stage 1, cited)
```

## 4. The Lagrangians (L1) of both fields

Both fields have the Lagrangian density

$$
\mathcal L=\sqrt{|g|}\,\Bigl[\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)-m\,\bar\Psi\Psi-U(\bar\Psi\Psi)\Bigr],\qquad \bar\Psi=\Psi^\dagger C,\tag{L1}
$$

with the canonical spin connection of Section 2.1 and $\mathcal L_s:=\mathcal L/\sqrt{|g|}$. For dirac16complex the components are Grassmann-odd (Stage 1 Section 7); for dirac16complex00 they are commuting complex numbers. In the notebook's conventions $m\equiv-HM$ reproduces the sign of Lg[]'s $+(HM)\Psi^T\sigma_{16}\Psi$ (CONTRACT Section 5; Section 3.3).

### 4.1 Kinetic term, canonical spin connection and reality

The kinetic term is the symmetrized first-order Dirac term built with $D_\mu=\partial_\mu+\Omega_\mu$ and the curved gammas $\gamma^\mu=e_a{}^\mu\gamma^a$. No factor $i$ appears: $C\gamma^a$ is real antisymmetric, hence anti-Hermitian (Result 2.1).

**Result 4.1** (coefficient form). Writing the density with the coefficients between $\Psi^\dagger$ and $\Psi$,

$$
\mathcal L=\Psi^\dagger K_0\Psi+\Psi^\dagger K^\mu\partial_\mu\Psi+(\partial_\mu\Psi^\dagger)L^\mu\Psi-\sqrt{|g|}\,\bigl(mS+U(S)\bigr),
$$

$$
K_0=\tfrac12\sqrt{|g|}\,C\{\gamma^\mu,\Omega_\mu\},\qquad K^\mu=\tfrac12\sqrt{|g|}\,C\gamma^\mu,\qquad L^\mu=-\tfrac12\sqrt{|g|}\,C\gamma^\mu=(K^\mu)^\dagger,
$$

with $K_0$ real symmetric (Hermitian, by Result 2.1 item 6) and $K^\mu$ real antisymmetric. The coefficients were read off the symbolic polynomial $\mathcal L$ and compared with these closed forms at the points flat, G1 p1-p3 and G2.

**Theorem 4.1** (reality for both statistics). For real $m$ and a real function (for Grassmann components: a real polynomial) $U$, (L1) is real for commuting components and Hermitian ($\mathcal L^\ast=\mathcal L$) for Grassmann components.

*Proof.* Complex conjugation reverses products: trivially for commuting numbers, and by $(\theta_1\theta_2)^\ast=\theta_2^\ast\theta_1^\ast$ for Grassmann numbers. In both algebras therefore $(\Psi^\dagger X\Phi)^\ast=\Phi^\dagger X^\dagger\Psi$ for any constant matrix $X$. Applied to Result 4.1: $(\Psi^\dagger K_0\Psi)^\ast=\Psi^\dagger K_0^\dagger\Psi=\Psi^\dagger K_0\Psi$, and $(\Psi^\dagger K^\mu\partial_\mu\Psi)^\ast=(\partial_\mu\Psi^\dagger)(K^\mu)^\dagger\Psi=(\partial_\mu\Psi^\dagger)L^\mu\Psi$, so the two derivative terms are exchanged. $S=\Psi^\dagger C\Psi$ is real (Hermitian) because $C$ is Hermitian, and so is $U(S)$. $\square$

The symmetrization is necessary: the unsymmetrized term $\bar\Psi\gamma^\mu\partial_\mu\Psi$ alone is not real for commuting components (nonzero imaginary part on exact complex data) and not Hermitian for Grassmann components.

**Verification.** Wolfram: with $\Psi=X+iY$, $X$, $Y$ real commuting symbols for the value and all first and second derivatives, and $m,\lambda$ real symbols, $\mathrm{Im}\,\mathcal L=0$ exactly for the value and all eight first-derivative jets at G1 p1 and G2 p1-p3. Python: the swap symmetry $\mathcal L(\chi,\psi)=\mathcal L(\psi,\chi)$ of the real-coefficient polynomial (value and jets) at flat, G1 p1-p3 and G2, and $\mathrm{Im}\,\mathcal L=0$ with $\mathcal L\ne0$ on exact Gaussian-rational complex data at flat and G1 p1-p3. Grassmann: in the exact flat Grassmann algebra with $m=3/7$, $\lambda=5/11$, $\mathcal L^\ast=\mathcal L$ (Python: 392 monomials), and Stage 1 LAG_hermiticity_G1/G2 for the curved Grassmann Lagrangian.

```
checks
  C00_lagrangian_realCommuting, C00_lagrangian_coefficientHermiticity,
  C00_lagrangian_grassmannFlatHermitianAndEL: wolfram-dirac16complex00
  S5_lagrangian_realCommuting, S5_lagrangian_coefficientHermiticity,
  S5_lagrangian_grassmannFlatHermitianAndEL: python-dirac16complex00
  LAG_hermiticity_G1, LAG_hermiticity_G2: wolfram-geometry (Stage 1, cited)
```

### 4.2 The explicit mass term

$$
\mathcal L_m=-m\sqrt{|g|}\,\bar\Psi\Psi=-m\sqrt{|g|}\,\Psi^\dagger C\Psi .
$$

It is linear in $m$ and bilinear (quadratic) in the components $(\Psi^\dagger,\Psi)$. It is non-zero and non-trivial for both fields:

**Result 4.2** (commuting components). $\bar\Psi\Psi=\Psi^\dagger C\Psi$ is a Hermitian form of signature (8,8) on $\mathbb C^{16}$ (characteristic polynomial of $C$: $(x-1)^8(x+1)^8$). With $e_k$ the standard basis ($k=0..15$):

| $\Psi$ | $\bar\Psi\Psi$ |
| --- | --- |
| $e_0+e_4$ | $-2$ |
| $e_8+e_{12}$ | $+2$ |
| $e_0+i\,e_4$ | $0$ |

so the mass term takes both signs and vanishes on null vectors; its imaginary part is 0 in each case.

**Result 4.3** (Grassmann components). $S=\Psi^\dagger C\Psi$ is a nonzero even Hermitian element of the Grassmann algebra generated by the 32 odd generators $\Psi_a,\Psi^\ast_a$: 16 monomials with coefficients $\pm1$. Its powers have $\binom{16}{k}$ monomials, $16,120,560,1820,\dots,120,16,1$ for $k=1,\dots,16$ (coefficients $\pm2$ for $S^2$ and $\pm6$ for $S^3$), $S^{16}\ne0$ and $S^{17}=0$, because a monomial of $S^{17}$ would contain 34 of the 32 generators (Stage 1 Section 7.6 lists all powers). The mass term of dirac16complex is therefore a nonzero element, linear in $m$ and quadratic in the components.

**The mass term changes the field equation.** The $m$-derivative of the Euler-Lagrange expression with respect to $\Psi^\ast$ is $-\sqrt{|g|}\,C\Psi\ne0$ (commuting components, all six G1/G2 points); in the flat Grassmann algebra the mass term contributes $-m(C\Psi)_a\ne0$ to the left Euler-Lagrange derivative.

**Result 4.4** (dispersion). In flat (4,4) space, $\Psi=u\,e^{ik_\mu x^\mu}$ solves $\gamma^\mu\partial_\mu\Psi=m\Psi$ iff $(i\gamma^\mu k_\mu-m)u=0$. Since

$$
(i\gamma^\mu k_\mu-m)(i\gamma^\mu k_\mu+m)=-(\eta^{\mu\nu}k_\mu k_\nu+m^2)\,I_{16},
$$

nonzero $u$ exist iff

$$
k_4^2+k_5^2+k_6^2+k_7^2-k_0^2-k_1^2-k_2^2-k_3^2=m^2,
$$

that is, for the $x_4$-frequency $\omega=|k_4|$: $\omega^2=m^2+|k_{\rm space}|^2-|k_{\rm extra\text{-}time}|^2$. At $m=1$, $k=(1,1,2,3;\,4;\,0,0,0)$ the solution space has dimension 8; off shell ($k_4=3$) it has dimension 0. The mass enters the dispersion as $m^2$. In a curved field with $U=0$ the on-shell second-order form is $(\gamma^\mu D_\mu)^2\Psi=m^2\Psi$, i.e. $\Box\Psi-\tfrac R4\Psi=m^2\Psi$ (Section 4.4).

```
checks
  C00_massTerm_commutingExplicitSpinors, C00_massTerm_grassmannNonzero,
  C00_massTerm_dispersionFlat, C00_EL_commutingCurved (dEL/dm):
      wolfram-dirac16complex00
  S5_massTerm_commutingExplicitSpinors, S5_massTerm_grassmannNonzero,
  S5_massTerm_dispersionFlat: python-dirac16complex00
```

### 4.3 The interaction U(S)

- **dirac16complex.** In a Grassmann algebra only polynomials of the even element $S$ exist, and $S^{17}=0$ (Result 4.3), so $U$ is a polynomial with $U(0)=U'(0)=0$ (CONTRACT Section 5; no cosmological constant). Default: $U=\tfrac\lambda2S^2$, a four-fermion (Thirring/Nambu-Jona-Lasinio type) contact term; $S^2$ is a nonzero element with 120 monomials.
- **dirac16complex00.** For commuting components $S$ is a real number and $U$ may be any smooth function. The default is the same $U=\tfrac\lambda2S^2$, so that with the default the two theories differ ONLY in the statistics of the components.

For a general smooth $U$ the checks of Sections 5 and 6 treat $U(S_0)=u_0$, $U'(S_0)=u_1$, $U''(S_0)=u_2$ at the point as independent symbols (Wolfram: an abstract function symbol at G1 p1; Python: G1 p1 and G2), so nothing beyond smoothness is used. The only place where the statistics changes the value of the interaction energy is the Wick contraction of $\langle U\rangle$ in a quasi-free state, which belongs to the Kohn-Sham model (Section 8 and document B).

```
checks
  C00_EL_commutingGeneralSmoothU, C00_EMT_generalSmoothU: wolfram-dirac16complex00
  S5_EL_commutingGeneralSmoothU, S5_EMT_generalSmoothU: python-dirac16complex00
```

### 4.4 Non-trivial coupling to the spin connection and to gravity

The operator $\gamma^\mu D_\mu$ does not know the statistics of the components, so the following statements hold verbatim for both fields. They are verified with exact jets at the curved points G1 p1-p3 (non-diagonal), G2 (primordial, diagonal) and G4 p1 (generic integer frame).

**Result 4.5.**

1. **Contraction.** $\gamma^\mu\Omega_\mu\ne0$: 128 nonzero entries at G1 p1-p3 and at G4 p1; at G2 it has 16 nonzero entries and equals $3H\gamma^0$ ($a_4$ cancels).
2. **Divergence identity.** $\partial_\mu(\sqrt{|g|}\,\gamma^\mu)=\sqrt{|g|}\,[\gamma^\mu,\Omega_\mu]$ and $\partial_\mu\sqrt{|g|}=\sqrt{|g|}\,\Gamma^\rho{}_{\rho\mu}$; the gammas are covariantly constant (Python: gammaCovariantlyConstant).
3. **Curvature.** $F_{\mu\nu}=\partial_\mu\Omega_\nu-\partial_\nu\Omega_\mu+[\Omega_\mu,\Omega_\nu]=\tfrac12R_{\mu\nu ab}S^{ab}\ne0$, so $\Omega$ cannot be gauged away.
4. **Lichnerowicz.** $(\gamma^\mu D_\mu)^2\Psi=g^{\mu\nu}(D_\mu D_\nu-\Gamma^\lambda{}_{\mu\nu}D_\lambda)\Psi+c\,R\,\Psi$ with $c=-\tfrac14$ exactly; on shell with $U=0$: $(\gamma^\mu D_\mu)^2\Psi=m^2\Psi$ and $\Box\Psi-\tfrac R4\Psi=m^2\Psi$ with $R\ne0$, so the curvature enters the second-order equation.
5. **Kinetic term.** The connection part of the symmetrized kinetic term is $\tfrac12\bar\Psi\{\gamma^\mu,\Omega_\mu\}\Psi=\tfrac14\,\omega_{[cab]}\,\bar\Psi\gamma^c\gamma^a\gamma^b\Psi$ (Result 2.1 item 6): nonzero at the non-diagonal G1 points, zero for diagonal vielbeins (G2). In a diagonal frame the gravitational coupling of the kinetic term is carried by $\gamma^\mu=e_a{}^\mu\gamma^a$ and $\sqrt{|g|}$, and by $\gamma^\mu\Omega_\mu$ in the field equation.
6. **Field equation.** The spin-connection term $\sqrt{|g|}\,C\gamma^\mu\Omega_\mu\Psi$ of the Euler-Lagrange expression (Section 5) is nonzero in all 16 components at G1 p1-p3 and G2.

The scalar curvatures at the test points (decimal forms of the exact values; identical in both reports where both evaluate them):

| point | $R$ |
| --- | --- |
| G1 p1 | $-2.426927426699216826$ |
| G1 p2 | $13.208097893040947037$ |
| G1 p3 | $36.661193034934481057$ |
| G2 p1 | $-18.176870748299319728$ |
| G2 p2 | $-1.6325925925925925926$ |
| G2 p3 | $-17.020408163265306122$ |
| G2 (symbolic, Python) | $6H^2(a_4'^2-7)$ |
| G4 p1 | $82754$ |

```
checks
  C00_connection_nonTrivialCoupling (G1 p1-p3, G2 p1-p3, G4 p1),
  C00_connection_OmegaTermInFieldEquation, C00_geometry_G4Generic,
  C00_algebra_anticommutatorTotallyAntisymmetric: wolfram-dirac16complex00
  S5_connection_nonTrivialCoupling (G1 p1-p3, G2),
  S5_connection_OmegaTermInFieldEquation, S5_geometry_G4Generic,
  S5_algebra_anticommutatorTotallyAntisymmetric: python-dirac16complex00
```

## 5. Euler-Lagrange equations
