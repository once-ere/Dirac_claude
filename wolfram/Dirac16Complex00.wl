(* ::Package:: *)

(* ::Title:: *)
(* Dirac16Complex00.wl *)

(* ::Text:: *)
(* Stage 5 of dirac16complex: the exact classical theory of dirac16complex00, the
   16-component Pin(4,4) spinor field whose components are COMMUTING complex scalar
   fields (the analogue of Dirac's original 4-component wave function), side by side
   with the second-quantized, anticommuting (Grassmann) field dirac16complex of
   Stages 1-4 wherever the statistics matters.

   Binding conventions: handoff/specs/STAGE5_SPEC.md sections 1-3, CONTRACT.md (with
   errata section 11), STAGE2_SPEC.md, STAGE4_SPEC.md (errata sections 7-9): counting
   from 0, x = {x0..x7}, x4 = time, eta = diag(+1,+1,+1,+1,-1,-1,-1,-1),
   gamma^a = notebook T16^A[a] (exact fixture artifacts/dirac16complex/arbitrary-field/
   algebra-fixture.json), C = sigma16, Psibar = Psi^dagger C, B = -i C gamma^4,
   gamma^8 = diag(-I8, +I8), Omega_mu = (1/8) omega_{mu ab}[gamma^a, gamma^b] with
   omega_{mu ab} = eta_{ac} omega_mu^c_b, D_mu Psi = d_mu Psi + Omega_mu Psi.

     L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi)
                   - m Psibar Psi - U(Psibar Psi) ]                         (L1)

   Reused exact machinery (read only, never modified):
     wolfram/Dirac16ComplexGeometry.wl   (Stage 1: order-1 jets of the geometry, the
        Lagrangian/EMT jets, the on-shell jet solver, the Grassmann algebra with jet
        coefficients, the test geometries G1 (general non-diagonal vielbein), G2
        (primordial field, arbitrary a4) and G3 (Bianchi-I minisuperspace));
     wolfram/Dirac16ComplexPrimordial.wl (Stage 2: the primordial field in the
        notebook chart z = 6 H x0, t = H x4, its exact ring zero test);
     wolfram/Dirac16ComplexKohnSham.wl   (Stage 4: the static warped y chart, the
        exact 2x2 block basis);
     artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json (Stage-4 export).
   Private functions of these packages are called by their full context names; their
   files are hashed into the report (sourceSha256) by the verifier.

   Exactness: every decision is an exact zero test of integers, rationals, Gaussian
   rationals, elements of Q(cos z) (G2), polynomials in independent symbols (field
   jets, U(S0), U'(S0), U''(S0)) or of the exact rings of the Stage-2/Stage-4 packages.
   No floating point number is used for any decision.

   Check-name prefix C00_; groups:
     fixture, algebra      gamma^8, C, B, S^{ab} facts; Pin(4,4) module; Spin_0 invariance
     lagrangian, massTerm  (L1) for commuting components: reality, the explicit mass term
                           (commuting spinors and Grassmann elements), the dispersion
     realRestriction       the notebook-type Lagrangian Psi^T sigma16 T16^a D_a Psi
                           (+ H M Psi^T sigma16 Psi): non-trivial for real commuting Psi,
                           a pure divergence with vanishing mass term for real Grassmann
                           Psi; the exact relation to (L1)
     connection            non-trivial coupling to the spin connection and to gravity
     EL                    Euler-Lagrange equations for commuting components
     EMT, current          vielbein variation (full, off-diagonal), symmetry, reality,
                           conservation, trace, current, observer splits, KE/PE, EoS
     charge, energy        the commuting field: indefinite charge density, classical
                           energy unbounded below (explicit exact solutions)
     primordial, static    the Stage-2 primordial field and the Stage-4 static warped form

   Public entry point: D16C00Run[repoRoot] -> <|"checks", "measurements", "theory"|>.

   License: GPL-3.0-or-later (same as the dirac-main reference implementation). *)

(* the reused packages must be loaded before this package is parsed *)
Module[{dir = DirectoryName[$InputFileName]},
  If[! MemberQ[$Packages, "Dirac16Complex`Geometry`"], Get[FileNameJoin[{dir, "Dirac16ComplexGeometry.wl"}]]];
  If[! MemberQ[$Packages, "Dirac16ComplexPrimordial`"], Get[FileNameJoin[{dir, "Dirac16ComplexPrimordial.wl"}]]];
  If[! MemberQ[$Packages, "Dirac16ComplexKohnSham`"], Get[FileNameJoin[{dir, "Dirac16ComplexKohnSham.wl"}]]];
];

BeginPackage["Dirac16Complex00`", {"Dirac16Complex`Geometry`"}];

D16C00Run::usage = "D16C00Run[repoRoot] runs every exact Stage-5 check of dirac16complex00 (commuting components) side by side with dirac16complex (Grassmann components) and returns <|\"checks\" -> <|name -> True|False|>, \"measurements\" -> <|...|>, \"theory\" -> <|...|>|>.";

Begin["`Private`"];

(* ========================================================================= *)
(* 0. bookkeeping, exact printers                                            *)
(* ========================================================================= *)

$checks = <||>; $meas = <||>; $theory = <||>;
addCheck[name_String, val_] := Module[{v = TrueQ[val]},
  $checks[name] = v;
  If[! v, Print["  CHECK FAILED: ", name]];
  v];
addMeas[name_String, val_] := ($meas[name] = val);
logT[msg__] := Print["[", DateString[{"Hour", ":", "Minute", ":", "Second"}], "] ", msg];
toStr[e_] := Block[{$Context = "Dirac16Complex00`Private`", $ContextPath = {"System`", "Dirac16Complex00`Private`"}},
  ToString[e, InputForm, PageWidth -> Infinity]];
boolS[b_] := If[TrueQ[b], "true", "false"];

(* exact JSON printers: rationals as "n" or "n/d", complex numbers as [re, im] *)
ratStr[x_Integer] := ToString[x];
ratStr[x_Rational] := ToString[Numerator[x]] <> "/" <> ToString[Denominator[x]];
ratStr[x_] := toStr[x];
gq[x_] := With[{c = Expand[x]}, If[ExactNumberQ[c] && (IntegerQ[Re[c]] || Head[Re[c]] === Rational) && (IntegerQ[Im[c]] || Head[Im[c]] === Rational),
    {ratStr[Re[c]], ratStr[Im[c]]}, {toStr[c], "non-Gaussian-rational"}]];
gqVec[v_List] := gq /@ v;
gqMat[m_List] := Map[gq, m, {2}];
ratMat[m_List] := Map[ratStr, m, {2}];

(* exact zero test in the current number field of the Stage-1 geometry package *)
zq[x_] := D16GeoZeroQ[x];
rd[x_] := D16GeoReduce[Expand[x]];
maxAbs[x_] := Module[{flat = Select[Flatten[{rd[x]}], ! TrueQ[Expand[#] === 0] &]},
  If[flat === {}, 0, Max[Abs[N[flat /. {Global`cs -> 0}, 20]]]]];

(* ========================================================================= *)
(* 1. algebra (the Stage-1 construction, compared with the fixture)          *)
(* ========================================================================= *)

id2 = IdentityMatrix[2]; id8 = IdentityMatrix[8]; id16 = IdentityMatrix[16];
z16 = ConstantArray[0, {16, 16}];
eta = D16GeoEta; etaD = Diagonal[eta];
gam = D16GeoGammas; Cm = D16GeoC; chi8 = D16GeoChirality; Sp = D16GeoSpin;
Bm = -I Cm.gam[[5]];
comm[a_, b_] := a.b - b.a; acomm[a_, b_] := a.b + b.a;
hermQ[m_] := ConjugateTranspose[m] === m;
realQ[m_] := FreeQ[m, Complex];
spinPairs = Subsets[Range[0, 7], {2}];

checkFixture[root_] := Module[{fx, okG, okC, okChi, okB, okS, sList, parse},
  fx = Import[FileNameJoin[{root, "artifacts", "dirac16complex", "arbitrary-field", "algebra-fixture.json"}], "RawJSON"];
  parse[v_] := If[StringQ[v], ToExpression[v], v];
  okG = fx["gamma"] === gam; okC = fx["C"] === Cm; okChi = fx["chirality"] === chi8;
  okB = (Map[parse, fx["B"]["real"], {2}] + I Map[parse, fx["B"]["imag"], {2}]) === Bm;
  sList = fx["S"];
  okS = Length[sList] > 0 && AllTrue[sList, Map[parse, #["matrix"], {2}] === Sp[[#["a"] + 1, #["b"] + 1]] &];
  addCheck["C00_fixture_matchesStage1Construction", okG && okC && okChi && okB && okS];
  addMeas["fixture.entriesCompared", <|"gamma" -> okG, "C" -> okC, "chirality" -> okChi, "B" -> okB, "S" -> okS, "SCount" -> Length[sList]|>];
];

checkLeadFacts[] := Module[{f},
  f = <|
    "gamma8Hermitian" -> hermQ[chi8], "gamma8SquaredIsOne" -> (chi8.chi8 === id16),
    "gamma8AnticommutesWithEveryGamma" -> AllTrue[gam, acomm[chi8, #] === z16 &],
    "gamma8CommutesWithC" -> (comm[chi8, Cm] === z16),
    "gamma8CommutesWithEveryBivector" -> AllTrue[Flatten[Table[comm[chi8, gam[[a]].gam[[b]]] === z16, {a, 8}, {b, 8}]], TrueQ],
    "gamma8CommutesWithEverySab" -> AllTrue[Flatten[Table[comm[chi8, Sp[[a, b]]] === z16, {a, 8}, {b, 8}]], TrueQ],
    "gamma8IsDiagMinusI8PlusI8" -> (chi8 === DiagonalMatrix[Join[ConstantArray[-1, 8], ConstantArray[1, 8]]]),
    "CRealSymmetric" -> (realQ[Cm] && Transpose[Cm] === Cm), "CSquaredIsOne" -> (Cm.Cm === id16),
    "CEqualsGamma0123" -> (Cm === gam[[1]].gam[[2]].gam[[3]].gam[[4]]),
    "CgammaRealAntisymmetric" -> AllTrue[gam, realQ[Cm.#] && Transpose[Cm.#] === -Cm.# &],
    "CSabRealAntisymmetric" -> AllTrue[Flatten[Table[realQ[Cm.Sp[[a, b]]] && Transpose[Cm.Sp[[a, b]]] === -Cm.Sp[[a, b]], {a, 8}, {b, 8}]], TrueQ],
    "BHermitian" -> hermQ[Bm], "BSquaredIsOne" -> (Bm.Bm === id16),
    "BEigenvaluesPlusMinusOneEight" -> (Sort[Eigenvalues[Bm]] === Join[ConstantArray[-1, 8], ConstantArray[1, 8]]),
    "BCommutesWithC" -> (comm[Bm, Cm] === z16), "BCEqualsMinusIGamma4" -> (Bm.Cm === -I gam[[5]]),
    "gamma8Bgamma8EqualsMinusB" -> (chi8.Bm.chi8 === -Bm),
    "gamma8CgammaGamma8EqualsMinusCgamma" -> AllTrue[gam, chi8.Cm.#.chi8 === -Cm.# &],
    "Cgamma4EqualsIB" -> (Cm.gam[[5]] === I Bm)|>;
  addCheck["C00_algebra_leadFacts", And @@ Values[f]];
  addMeas["algebra.leadFacts", f];
];

(* {gamma^c, S^{ab}} is the totally antisymmetric product: gamma^c gamma^a gamma^b for distinct c, a, b, 0 if c in {a, b} *)
checkAnticommutatorStructure[] := Module[{okA, okSym, okAnti, okVec},
  okA = AllTrue[Flatten[Table[If[a == b, True,
       acomm[gam[[c]], Sp[[a, b]]] === If[c == a || c == b, z16, gam[[c]].gam[[a]].gam[[b]]]], {c, 8}, {a, 8}, {b, 8}]], TrueQ];
  okSym = AllTrue[Flatten[Table[With[{x = Cm.acomm[gam[[c]], Sp[[a, b]]]}, Transpose[x] === x], {c, 8}, {a, 8}, {b, 8}]], TrueQ];
  okAnti = AllTrue[Flatten[Table[With[{x = Cm.comm[gam[[c]], Sp[[a, b]]]}, Transpose[x] === -x], {c, 8}, {a, 8}, {b, 8}]], TrueQ];
  okVec = AllTrue[Flatten[Table[comm[Sp[[a, b]], gam[[c]]] === eta[[b, c]] gam[[a]] - eta[[a, c]] gam[[b]], {a, 8}, {b, 8}, {c, 8}]], TrueQ];
  addCheck["C00_algebra_anticommutatorTotallyAntisymmetric", okA && okSym && okAnti && okVec];
  addMeas["algebra.anticommutatorStructure", "{gamma^c, S^{ab}} = gamma^c gamma^a gamma^b for c, a, b distinct and 0 for c in {a, b}; C{gamma^c,S^{ab}} symmetric, C[gamma^c,S^{ab}] antisymmetric; [S^{ab}, gamma^c] = eta^{bc} gamma^a - eta^{ac} gamma^b. Consequence: (1/2) Psibar {gamma^mu, Omega_mu} Psi = (1/4) omega_{[cab]} Psibar gamma^c gamma^a gamma^b Psi (only the totally antisymmetric part of omega_{cab} = e_c^mu omega_{mu ab} enters the symmetrized kinetic term)."];
];

(* commutants over Q (rank is field-independent): Pin(4,4) module irreducible, Spin(4,4) splits into the two chiral halves *)
vecOp[a_, b_] := KroneckerProduct[a, IdentityMatrix[Length[b]]] - KroneckerProduct[IdentityMatrix[Length[a]], Transpose[b]];
commutantDim[mats_] := 256 - MatrixRank[SparseArray[Join @@ (vecOp[#, #] & /@ mats)]];
checkPinModule[] := Module[{dPin, dSpin, inv, formRows, dForm},
  dPin = commutantDim[gam];
  dSpin = commutantDim[Sp[[#[[1]] + 1, #[[2]] + 1]] & /@ spinPairs];
  inv = AllTrue[spinPairs, Transpose[Sp[[#[[1]] + 1, #[[2]] + 1]]].Cm + Cm.Sp[[#[[1]] + 1, #[[2]] + 1]] === z16 && realQ[Sp[[#[[1]] + 1, #[[2]] + 1]]] &];
  (* invariant bilinear forms X of Spin(4,4): S^T X + X S = 0 *)
  formRows = Join @@ (Function[s, KroneckerProduct[Transpose[s], id16] + KroneckerProduct[id16, Transpose[s]]] /@ (Sp[[#[[1]] + 1, #[[2]] + 1]] & /@ spinPairs));
  dForm = 256 - MatrixRank[SparseArray[formRows]];
  addCheck["C00_algebra_pinModuleAndSpinInvariance", dPin === 1 && dSpin === 2 && inv && dForm === 2];
  addMeas["algebra.pinModule", <|"commutantOfGammas" -> dPin, "commutantOfSpinGenerators" -> dSpin, "invariantBilinearForms" -> dForm,
    "statement" -> "C^16 is an irreducible complex Pin(4,4) module (commutant 1); under Spin(4,4) it splits into the two chiral halves (commutant 2); every S^{ab} is real with S^T C + C S = 0, so R^T C R = C and R^dagger = R^T for R in Spin_0(4,4): Psi^dagger C Psi is invariant and Psibar gamma^c Psi is a vector. The 16 COMMUTING components of dirac16complex00 therefore carry exactly the Pin(4,4) spinor representation of the 16 Grassmann components of dirac16complex: the two fields differ only in the statistics of the components (the local, curved-space covariance is Stage 1's LAG_localSpinInvariance, a computation with commuting numbers)."|>];
];

(* ========================================================================= *)
(* 2. an exact Grassmann algebra with constant coefficients (flat checks)    *)
(* ========================================================================= *)
(* element: Association  sortedGeneratorList -> exact coefficient; all generators odd *)

gClean[x_Association] := Select[Map[Expand, x], ! TrueQ[# === 0] &];
gCollect[pairs_List] := If[pairs === {}, <||>, gClean[GroupBy[pairs, First -> Last, Total]]];
gGen[id_] := <|{id} -> 1|>;
gAdd[xs___Association] := gCollect[Flatten[KeyValueMap[List, #] & /@ {xs}, 1]];
gScale[c_, x_Association] := If[TrueQ[c === 0], <||>, gClean[Map[c # &, x]]];
gMul[x_Association, y_Association] := Module[{kx = Keys[x], vx = Values[x], ky = Keys[y], vy = Values[y], acc},
  If[kx === {} || ky === {}, Return[<||>, Module]];
  acc = Reap[Do[If[Intersection[kx[[i]], ky[[j]]] === {},
       With[{mm = Join[kx[[i]], ky[[j]]]}, Sow[{Sort[mm], Signature[mm] vx[[i]] vy[[j]]}]]], {i, Length[kx]}, {j, Length[ky]}]][[2]];
  If[acc === {}, <||>, gCollect[First[acc]]]];
gZeroQ[x_Association] := Length[gClean[x]] === 0;
gEqualQ[x_Association, y_Association] := gZeroQ[gAdd[x, gScale[-1, y]]];
(* left derivative with respect to a generator *)
gLeftD[x_Association, id_] := gCollect[KeyValueMap[Function[{key, c},
     With[{p = FirstPosition[key, id]}, If[MissingQ[p], Nothing, {Delete[key, p[[1]]], (-1)^(p[[1]] - 1) c}]]], x]];
(* conjugation: generators mapped by cmap, order reversed (conj(theta1 theta2) = conj(theta2) conj(theta1)), coefficients conjugated *)
gConj[x_Association, cmap_] := gCollect[KeyValueMap[Function[{key, c},
     With[{g = Reverse[cmap /@ key]}, {Sort[g], Signature[g] Conjugate[c]}]], x]];
(* even derivation: each generator id is replaced by dmap[id] (Missing -> 0) *)
gDeriv[x_Association, dmap_] := gCollect[Flatten[KeyValueMap[Function[{key, c},
      Table[With[{new = dmap[key[[p]]]}, If[MissingQ[new], Nothing,
          With[{nk = ReplacePart[key, p -> new]}, If[DuplicateFreeQ[nk], {Sort[nk], Signature[nk] c}, Nothing]]]], {p, Length[key]}]], x], 1]];
gVec[f_] := Table[gGen[f[a]], {a, 0, 15}];
gMatVec[m_, v_List] := Table[gAdd @@ Table[gScale[m[[i, j]], v[[j]]], {j, 16}], {i, 16}];
gDot[u_List, v_List] := gAdd @@ MapThread[gMul, {u, v}];

(* generator ids: complex field  psi_a = 1+a, psi*_a = 17+a, d_mu psi_a = 33+16mu+a, d_mu psi*_a = 161+16mu+a;
   real field r_a = 1+a, d_mu r_a = 17+16mu+a;  real/imaginary parts rho_a = 301+a, iota_a = 317+a *)
cPsi[a_] := 1 + a; cPsb[a_] := 17 + a; cDPsi[mu_, a_] := 33 + 16 mu + a; cDPsb[mu_, a_] := 161 + 16 mu + a;
cConjMap[id_] := Which[id <= 16, id + 16, id <= 32, id - 16, id <= 160, id + 128, id <= 288, id - 128, True, id];
cDMap[mu_][id_] := Which[id <= 16, cDPsi[mu, id - 1], id <= 32, cDPsb[mu, id - 17], True, Missing[]];
rPsi[a_] := 1 + a; rDPsi[mu_, a_] := 17 + 16 mu + a;
rDMap[mu_][id_] := If[id <= 16, rDPsi[mu, id - 1], Missing[]];

checkGrassmannFlat[] := Module[{psi, psb, dpsi, dpsb, bar, dbar, S, S2, S3, kin, kinU, Lf, m = 3/7, lam = 5/11, herm, hermU, ELb, tgt, massEL,
    r, dr, rCr, rCgr, divOK, realL, realEL, rho, iota, psiRI, psbRI, SRI, crossS, okCounts, dir, w},
  psi = gVec[cPsi]; psb = gVec[cPsb];
  dpsi = Table[gVec[cDPsi[mu, #] &], {mu, 0, 7}]; dpsb = Table[gVec[cDPsb[mu, #] &], {mu, 0, 7}];
  (* Psibar = Psi^dagger C as a row of Grassmann elements *)
  bar = Table[gAdd @@ Table[gScale[Cm[[b, a]], psb[[b]]], {b, 16}], {a, 16}];
  dbar = Table[Table[gAdd @@ Table[gScale[Cm[[b, a]], dpsb[[mu, b]]], {b, 16}], {a, 16}], {mu, 8}];
  S = gDot[bar, psi]; S2 = gMul[S, S]; S3 = gMul[S2, S];
  okCounts = {Length[S], Length[S2], Length[S3]} === {16, 120, 560} && Union[Abs[Values[S]]] === {1} && Union[Abs[Values[S2]]] === {2} && Union[Abs[Values[S3]]] === {6};
  addCheck["C00_massTerm_grassmannNonzero", ! gZeroQ[S] && okCounts && gEqualQ[gConj[S, cConjMap], S]];
  addMeas["massTerm.grassmann", <|"SMonomials" -> Length[S], "S2Monomials" -> Length[S2], "S3Monomials" -> Length[S3],
    "note" -> "S = Psibar Psi = Psi^dagger C Psi is a nonzero even element of the Grassmann algebra generated by Psi_a, Psi_a^* (32 odd generators): 16 monomials with coefficients +-1, S^2 has 120 monomials (coefficients +-2), S^3 has 560 (+-6), S is Hermitian (invariant under (theta1 theta2)^* = theta2^* theta1^*). S^17 = 0 because a monomial of S^17 would contain 34 generators out of 32 (Stage 1 Result 7.2 lists all powers). The mass term -m sqrt|g| S of (L1) is therefore a nonzero element, linear in m and quadratic in the components."|>];
  (* flat (L1) in the Grassmann algebra *)
  kin = gScale[1/2, gAdd @@ Table[gAdd[gDot[bar, gMatVec[gam[[mu]], dpsi[[mu]]]], gScale[-1, gDot[gMatVec[Transpose[gam[[mu]]], dbar[[mu]]], psi]]], {mu, 8}]];
  kinU = gAdd @@ Table[gDot[bar, gMatVec[gam[[mu]], dpsi[[mu]]]], {mu, 8}];
  Lf = gAdd[kin, gScale[-m, S], gScale[-lam/2, S2]];
  herm = gEqualQ[gConj[Lf, cConjMap], Lf]; hermU = gEqualQ[gConj[kinU, cConjMap], kinU];
  (* Euler-Lagrange (left derivative w.r.t. Psi^*_a) with constant coefficients:
     dL/dPsi^*_a - sum_mu d_mu (dL/d(d_mu Psi^*_a)), d_mu acting on the generators *)
  ELb = Table[gAdd[gLeftD[Lf, cPsb[a]], gScale[-1, gAdd @@ Table[gDeriv[gLeftD[Lf, cDPsb[mu, a]], cDMap[mu]], {mu, 0, 7}]]], {a, 0, 15}];
  dir = Table[gAdd @@ Table[gMatVec[gam[[mu]], dpsi[[mu]]][[i]], {mu, 8}], {i, 16}];
  w = Table[gAdd[dir[[i]], gScale[-m, psi[[i]]], gScale[-lam, gMul[S, psi[[i]]]]], {i, 16}];
  tgt = gMatVec[Cm, w];
  massEL = Table[gLeftD[gScale[-m, S], cPsb[a]], {a, 0, 15}];
  addCheck["C00_lagrangian_grassmannFlatHermitianAndEL", herm && ! hermU && AllTrue[Range[16], gEqualQ[ELb[[#]], tgt[[#]]] &] &&
    AllTrue[Range[16], gEqualQ[massEL[[#]], gScale[-m, gMatVec[Cm, psi][[#]]]] && ! gZeroQ[massEL[[#]]] &]];
  addMeas["lagrangian.grassmannFlat", "flat (L1) with m = 3/7, lambda = 5/11 in the exact Grassmann algebra (288 odd generators Psi_a, Psi^*_a, d_mu Psi_a, d_mu Psi^*_a): L^* = L (the unsymmetrized Psibar gamma^mu d_mu Psi alone is not Hermitian); the left Euler-Lagrange derivative with respect to Psi^*_a is (C(gamma^mu d_mu Psi - (m + lambda S) Psi))_a; the mass term contributes -m (C Psi)_a != 0."];
  (* real Grassmann field: the notebook-type Lagrangian *)
  r = gVec[rPsi]; dr = Table[gVec[rDPsi[mu, #] &], {mu, 0, 7}];
  rCr = gDot[r, gMatVec[Cm, r]];
  rCgr = Table[gDot[r, gMatVec[Cm.gam[[a]], r]], {a, 8}];
  divOK = AllTrue[Flatten[Table[gEqualQ[gDot[r, gMatVec[Cm.gam[[a]], dr[[mu]]]], gScale[1/2, gDeriv[rCgr[[a]], rDMap[mu - 1]]]], {a, 8}, {mu, 8}]], TrueQ];
  realL = gAdd[gAdd @@ Table[gDot[r, gMatVec[Cm.gam[[mu]], dr[[mu]]]], {mu, 8}], gScale[2/3, rCr]];
  realEL = Table[gAdd[gLeftD[realL, rPsi[a]], gScale[-1, gAdd @@ Table[gDeriv[gLeftD[realL, rDPsi[mu, a]], rDMap[mu]], {mu, 0, 7}]]], {a, 0, 15}];
  addCheck["C00_realRestriction_grassmannFlatTrivial", gZeroQ[rCr] && AllTrue[rCgr, Length[#] === 8 && Union[Abs[Values[#]]] === {2} &] && divOK &&
    AllTrue[realEL, gZeroQ] && ! gZeroQ[realL]];
  addMeas["realRestriction.grassmannFlat", "real Grassmann Psi (generators r_a, d_mu r_a): Psi^T C Psi = 0 identically (C symmetric), each Psi^T C gamma^a Psi has 8 monomials (coefficients +-2), Psi^T C gamma^a d_mu Psi = (1/2) d_mu (Psi^T C gamma^a Psi) for all a, mu, so the flat notebook-type Lagrangian Psi^T C gamma^mu d_mu Psi + (H M) Psi^T C Psi is a nonzero total divergence with identically vanishing Euler-Lagrange expressions (the curved case is Stage 1 Theorem 6.1, re-run below at G1 p1)."];
  (* complex Psi = rho + i iota with real Grassmann rho, iota: S = 2 i rho^T C iota (only the cross term) *)
  rho = Table[gGen[301 + a], {a, 0, 15}]; iota = Table[gGen[317 + a], {a, 0, 15}];
  psiRI = Table[gAdd[rho[[a]], gScale[I, iota[[a]]]], {a, 16}]; psbRI = Table[gAdd[rho[[a]], gScale[-I, iota[[a]]]], {a, 16}];
  SRI = gDot[Table[gAdd @@ Table[gScale[Cm[[b, a]], psbRI[[b]]], {b, 16}], {a, 16}], psiRI];
  crossS = gScale[2 I, gDot[rho, gMatVec[Cm, iota]]];
  addCheck["C00_realRestriction_grassmannComplexDecomposition", gEqualQ[SRI, crossS] && ! gZeroQ[SRI] && gZeroQ[gDot[rho, gMatVec[Cm, rho]]]];
  addMeas["realRestriction.grassmannDecomposition", "Grassmann Psi = rho + i iota (rho, iota real Grassmann 16-vectors): Psibar Psi = 2 i rho^T C iota; the diagonal terms rho^T C rho, iota^T C iota vanish, so the mass term of the complex Grassmann field is a pure cross term between the two real components (a Dirac-type field = two Majorana-type fields coupled by an off-diagonal mass). For COMMUTING components the opposite holds: Psibar Psi = rho^T C rho + iota^T C iota (C00_realRestriction_commutingFlatDecomposition)."];
];

checkCommutingFlat[] := Module[{X, Y, dX, dY, psi, psb, dpsi, dpsb, S, SR, SI, kin, kinR, kinI, m = 3/7, lam = 5/11, L, ELb, tgt, qv, pv},
  X = Array[fX, 16, 0]; Y = Array[fY, 16, 0]; dX = Table[fdX[mu, a], {mu, 0, 7}, {a, 0, 15}]; dY = Table[fdY[mu, a], {mu, 0, 7}, {a, 0, 15}];
  psi = X + I Y; psb = X - I Y; dpsi = dX + I dY; dpsb = dX - I dY;
  S = Expand[psb.Cm.psi]; SR = X.Cm.X; SI = Y.Cm.Y;
  kin = Expand[(1/2) Sum[psb.Cm.gam[[mu]].dpsi[[mu]] - dpsb[[mu]].Cm.gam[[mu]].psi, {mu, 8}]];
  kinR = Expand[Sum[X.Cm.gam[[mu]].dX[[mu]], {mu, 8}]]; kinI = Expand[Sum[Y.Cm.gam[[mu]].dY[[mu]], {mu, 8}]];
  addCheck["C00_realRestriction_commutingFlatDecomposition", Expand[S - SR - SI] === 0 && Expand[kin - kinR - kinI] === 0 &&
    Expand[ComplexExpand[Im[kin - m S - (lam/2) S^2]]] === 0 && ! TrueQ[Expand[SR] === 0] && ! TrueQ[Expand[kinR] === 0]];
  addMeas["realRestriction.commutingFlatDecomposition", "commuting Psi = X + i Y (X, Y real 16-vectors): Psibar Psi = X^T C X + Y^T C Y and the symmetrized kinetic term = X^T C gamma^mu d_mu X + Y^T C gamma^mu d_mu Y exactly (no cross terms); the flat (L1) is real for all real X, Y."];
  (* flat Euler-Lagrange for commuting components (ordinary derivatives, no signs), Psi and Psi^* independent *)
  qv = Array[fQ, 16, 0]; pv = Array[fP, 16, 0];
  L = Expand[(1/2) Sum[qv.Cm.gam[[mu]].Table[fdP[mu - 1, a], {a, 0, 15}] - Table[fdQ[mu - 1, a], {a, 0, 15}].Cm.gam[[mu]].pv, {mu, 8}] -
     m qv.Cm.pv - (lam/2) (qv.Cm.pv)^2];
  (* dL/d(d_mu Psi^*_a) = -(1/2)(C gamma^mu Psi)_a is linear in Psi, so its total derivative is sum_b (d/dPsi_b) * d_mu Psi_b *)
  ELb = Table[D[L, fQ[a]] - Sum[D[D[L, fdQ[mu, a]], fP[b]] fdP[mu, b], {mu, 0, 7}, {b, 0, 15}], {a, 0, 15}];
  tgt = Cm.(Sum[gam[[mu]].Table[fdP[mu - 1, a], {a, 0, 15}], {mu, 8}] - (m + lam qv.Cm.pv) pv);
  addCheck["C00_EL_commutingFlat", Expand[ELb - tgt] === ConstantArray[0, 16] &&
    AllTrue[Flatten[Table[Expand[D[L, fdQ[mu, a]] + (1/2) (Cm.gam[[mu + 1]].pv)[[a + 1]]] === 0, {mu, 0, 7}, {a, 0, 15}]], TrueQ]];
  addMeas["EL.commutingFlat", "flat, constant-coefficient derivation with commuting symbols (Psi, Psi^* independent; dL/d(d_mu Psi^*_a) = -(1/2)(C gamma^mu Psi)_a verified): dL/dPsi^*_a - d_mu(dL/d(d_mu Psi^*_a)) = (C(gamma^mu d_mu Psi - (m + lambda S)Psi))_a, the same expression as the Grassmann left derivative of C00_lagrangian_grassmannFlatHermitianAndEL."];
];

(* explicit commuting spinors for the mass term; flat dispersion *)
checkMassTermCommuting[] := Module[{e, pm, pp, p0, sM, sP, s0, cp, x, kk, gk, disp, onK, ns, m0},
  e[i_] := UnitVector[16, i + 1];
  pm = e[0] + e[4]; pp = e[8] + e[12]; p0 = e[0] + I e[4];
  sM = Conjugate[pm].Cm.pm; sP = Conjugate[pp].Cm.pp; s0 = Conjugate[p0].Cm.p0;
  cp = Factor[CharacteristicPolynomial[Cm, x]];
  addCheck["C00_massTerm_commutingExplicitSpinors", sM === -2 && sP === 2 && s0 === 0 && Expand[cp - (x - 1)^8 (x + 1)^8] === 0];
  addMeas["massTerm.commutingExplicit", <|"PsiMinus" -> "e_0 + e_4", "SMinus" -> sM, "PsiPlus" -> "e_8 + e_12", "SPlus" -> sP, "PsiNull" -> "e_0 + i e_4", "SNull" -> s0,
    "charPolyC" -> toStr[cp],
    "note" -> "Psibar Psi = Psi^dagger C Psi is a Hermitian form of signature (8,8) on C^16 (C real symmetric, C^2 = 1, eigenvalues +-1 eight times): it takes the values -2, +2, 0 on e_0+e_4, e_8+e_12, e_0+i e_4 (e_k the standard basis, k = 0..15). The mass term L_m = -m sqrt|g| Psibar Psi is linear in m and bilinear in (Psi^dagger, Psi)."|>];
  kk = Array[kq, 8, 0];
  gk = Sum[kk[[mu]] gam[[mu]], {mu, 8}];   (* gamma^mu k_mu with covariant k_mu; (gamma^mu k_mu)^2 = eta^{mu nu} k_mu k_nu *)
  disp = Expand[(I gk - m0 id16).(I gk + m0 id16)] === Expand[-(Sum[eta[[mu, mu]] kk[[mu]]^2, {mu, 8}] + m0^2) id16];
  onK = {1, 1, 2, 3, 4, 0, 0, 0};  (* k_4 = 4, m = 1: 16 = 1 + 1 + 1 + 4 + 9 *)
  ns = NullSpace[I (gk /. Thread[kk -> onK]) - id16];
  addCheck["C00_massTerm_dispersionFlat", disp && Length[ns] === 8 && Length[NullSpace[I (gk /. Thread[kk -> {1, 1, 2, 3, 3, 0, 0, 0}]) - id16]] === 0];
  addMeas["massTerm.dispersion", "flat (4,4) space, Psi = u e^{i k_mu x^mu}: gamma^mu d_mu Psi = m Psi reads (i gamma^mu k_mu - m) u = 0; (i gamma.k - m)(i gamma.k + m) = -(eta^{mu nu} k_mu k_nu + m^2) I16, so nonzero u exist iff k_4^2 + k_5^2 + k_6^2 + k_7^2 - k_0^2 - k_1^2 - k_2^2 - k_3^2 = m^2 (x4-frequency omega = |k_4|: omega^2 = m^2 + |k_space|^2 - |k_extra-time|^2); at m = 1, k = (1,1,2,3; 4; 0,0,0) the solution space has dimension 8, off shell (k_4 = 3) it is 0. The mass enters the dispersion as m^2."];
];

(* ========================================================================= *)
(* 3. curved test geometries (Stage 1: G1, G2, G3) and field jets            *)
(* ========================================================================= *)

gp[s_String] := Symbol["Dirac16Complex`Geometry`Private`" <> s];
xsL = Table[Symbol["Dirac16Complex00`Private`x" <> ToString[k]], {k, 0, 7}];
g1Pts = {{1/7, -2/9, 1/5, 3/11, -1/13, 2/17, -3/19, 1/23}, {-1/3, 1/4, 2/7, -1/5, 1/6, -2/11, 1/9, 3/13}, {2/9, 1/8, -1/7, 1/10, -3/14, 1/12, 2/15, -1/16}};
mList = {3/7, -2/5, 5/9}; lamList = {5/11, 7/13, -3/8}; hmList = {2/3, -5/7, 4/9};   (* the Stage-1 parameters *)
(* geometry at a test point; returns <|"fj", "geo", "alg", "label", ...|>; alg = exact number-field spec (list) *)
geoAt["G1", k_, curv_: True] := Module[{fj, geo},
  D16GeoSetAlgebraic[None];
  fj = D16GeoFrameJet[D16GeoG1Frame[xsL], xsL, Thread[xsL -> g1Pts[[k]]]];
  geo = D16GeoJetGeometry[fj, "Curvature" -> curv];
  <|"fj" -> fj, "geo" -> geo, "alg" -> {}, "label" -> "G1p" <> ToString[k], "H" -> Missing[]|>];
geoAt["G2", k_, curv_: True] := Module[{pt = gp["g2Points"][[k]], fj, geo, alg},
  alg = gp["g2Alg"][pt];
  D16GeoSetAlgebraic[alg];
  fj = D16GeoFrameJet[gp["g2FrameSymbolic"][pt["H"]], gp["xs"], gp["g2Rules"][pt]];
  geo = D16GeoJetGeometry[fj, "Curvature" -> curv];
  D16GeoSetAlgebraic[None];
  <|"fj" -> fj, "geo" -> geo, "alg" -> alg, "label" -> "G2p" <> ToString[k], "H" -> pt["H"], "point" -> pt|>];
geoAt["G3", k_, curv_: True] := Module[{t = {1/3, -2/5, 3/7}[[k]], fj, geo},
  D16GeoSetAlgebraic[None];
  fj = D16GeoFrameJet[gp["g3Frame"][xsL], xsL, Thread[xsL -> {0, 0, 0, 0, t, 0, 0, 0}]];
  geo = D16GeoJetGeometry[fj, "Curvature" -> curv];
  <|"fj" -> fj, "geo" -> geo, "alg" -> {}, "label" -> "G3t" <> ToString[k], "H" -> Missing[], "x4" -> t|>];
(* numeric mode: alg as recorded (None for rational points); symbolic mode: the same field with Expand forced *)
numMode[g_] := D16GeoSetAlgebraic[If[g["alg"] === {}, None, g["alg"]]];
symMode[g_] := D16GeoSetAlgebraic[g["alg"]];
numValue[x_] := N[gp["exactValue"][x], 20];

(* exact random field data, the Stage-1 algorithm (64-bit LCG of D16GeoRandomRationals) *)
rr[s_, n_] := D16GeoRandomRationals[s, n];
sym2[seed_] := Module[{r = rr[seed, 36*16], k = 0, arr}, arr = ConstantArray[0, {8, 8, 16}];
  Do[With[{v = r[[16 k + 1 ;; 16 k + 16]]}, arr[[i, j]] = v; arr[[j, i]] = v; k++], {i, 8}, {j, i, 8}]; arr];
fdata[seed_] := {rr[seed, 16], Partition[rr[seed + 1, 128], 16], sym2[seed + 2], rr[seed + 3, 16], Partition[rr[seed + 4, 128], 16], sym2[seed + 5]};
(* complex data with Psi^dagger = conjugate transpose of Psi (for reality statements) *)
cdata[seed_] := Module[{a = fdata[seed], b = fdata[seed + 50]}, {a[[1]] + I b[[1]], a[[2]] + I b[[2]], a[[3]] + I b[[3]], a[[1]] - I b[[1]], a[[2]] - I b[[2]], a[[3]] - I b[[3]]}];
(* symbolic commuting jets *)
symJets[] := {Array[sP0, 16, 0], Table[sP1[mu, a], {mu, 0, 7}, {a, 0, 15}], Table[sP2[Min[l, mu], Max[l, mu], a], {l, 0, 7}, {mu, 0, 7}, {a, 0, 15}],
   Array[sQ0, 16, 0], Table[sQ1[mu, a], {mu, 0, 7}, {a, 0, 15}], Table[sQ2[Min[l, mu], Max[l, mu], a], {l, 0, 7}, {mu, 0, 7}, {a, 0, 15}]};
realJets[h0_, h1_, h2_] := {Array[h0, 16, 0], Table[h1[mu, a], {mu, 0, 7}, {a, 0, 15}], Table[h2[Min[l, mu], Max[l, mu], a], {l, 0, 7}, {mu, 0, 7}, {a, 0, 15}]};
jPt[j_, mu_] := {j[[1, mu]], j[[2, All, mu]]};   (* the jet of the mu-th entry of a list-valued jet *)
jM[f_, a_, b_] := {rd[f[a[[1]], b[[1]]]], Table[rd[f[a[[2, l]], b[[1]]] + f[a[[1]], b[[2, l]]]], {l, 8}]};
jL[f_, a_] := {rd[f[a[[1]]]], rd[f /@ a[[2]]]};
jAdd[a_, b_] := {rd[a[[1]] + b[[1]]], rd[a[[2]] + b[[2]]]};

(* ========================================================================= *)
(* 4. Euler-Lagrange equations of (L1) for COMMUTING components (curved)     *)
(* ========================================================================= *)
(* jet identity (exact for any first-order Lagrangian of commuting variables):
   EL_a = dL/du_a - sum_mu d_mu (dL/du_{mu a}) = 9 dL0/du_a - sum_mu d(d_mu L)/du_{mu a},
   and the direct form with dL/d(d_mu Psi^dagger) = -(1/2) sqrt|g| C gamma^mu Psi, dL/d(d_mu Psi) = (1/2) sqrt|g| Psibar gamma^mu. *)
elCommuting[g_, generalU_] := Module[{geo = g["geo"], fl, fld, lag, sq, S, L0, Ld, ELq, ELp, gm, gJ, tq, tp, meff, pd, pdp, divq, divp, okq, okp, okqd, okpd,
    okpart, massTerm, omTerm, res = <||>},
  symMode[g];
  fl = symJets[]; fld = D16GeoFieldJets @@ fl;
  lag = D16GeoLagrangianJets[geo, fld, mS, If[generalU, 0, lS]];
  sq = geo["sqrtg"]; S = lag["S"];
  L0 = lag["L"][[1]]; Ld = lag["L"][[2]];
  If[generalU,
    L0 = rd[L0 - sq[[1]] uF[S[[1]]]];
    Ld = Table[rd[Ld[[l]] - sq[[2, l]] uF[S[[1]]] - sq[[1]] uF'[S[[1]]] S[[2, l]]], {l, 8}]];
  ELq = Table[rd[9 D[L0, sQ0[a]] - Sum[D[Ld[[mu + 1]], sQ1[mu, a]], {mu, 0, 7}]], {a, 0, 15}];
  ELp = Table[rd[9 D[L0, sP0[a]] - Sum[D[Ld[[mu + 1]], sP1[mu, a]], {mu, 0, 7}]], {a, 0, 15}];
  gm = geo["gamma"][[1]]; gJ = geo["gamma"];
  meff = mS + If[generalU, uF'[S[[1]]], lS S[[1]]];
  tq = rd[sq[[1]] Cm.(Sum[gm[[mu]].lag["Dpsi"][[mu, 1]], {mu, 8}] - meff fl[[1]])];
  tp = rd[-sq[[1]] (Sum[lag["Dbar"][[mu, 1]].gm[[mu]], {mu, 8}] + meff lag["bar"][[1]])];
  okq = zq[ELq - tq]; okp = zq[ELp - tp];
  (* direct form *)
  pd = Table[D[L0, sQ1[mu, a]], {mu, 0, 7}, {a, 0, 15}]; pdp = Table[D[L0, sP1[mu, a]], {mu, 0, 7}, {a, 0, 15}];
  okpart = zq[pd + (1/2) sq[[1]] Table[Cm.gm[[mu]].fl[[1]], {mu, 8}]] && zq[pdp - (1/2) sq[[1]] Table[fl[[4]].Cm.gm[[mu]], {mu, 8}]];
  divq = Sum[-(1/2) (sq[[2, mu]] Cm.gm[[mu]].fl[[1]] + sq[[1]] Cm.gJ[[2, mu, mu]].fl[[1]] + sq[[1]] Cm.gm[[mu]].fl[[2, mu]]), {mu, 8}];
  divp = Sum[(1/2) (sq[[2, mu]] fl[[4]].Cm.gm[[mu]] + sq[[1]] fl[[4]].Cm.gJ[[2, mu, mu]] + sq[[1]] fl[[5, mu]].Cm.gm[[mu]]), {mu, 8}];
  okqd = zq[Table[D[L0, sQ0[a]], {a, 0, 15}] - divq - tq]; okpd = zq[Table[D[L0, sP0[a]], {a, 0, 15}] - divp - tp];
  (* the mass term enters the field equation: dEL/dm = -sqrt|g| C Psi != 0 *)
  massTerm = rd[D[ELq, mS]];
  (* the spin-connection term of the Psi^dagger equation *)
  omTerm = rd[sq[[1]] Cm.Sum[gm[[mu]].geo["Omega"][[1, mu]], {mu, 8}].fl[[1]]];
  res["psiDagger"] = okq; res["psi"] = okp; res["directPsiDagger"] = okqd; res["directPsi"] = okpd; res["momentaForm"] = okpart;
  res["massTermInEquation"] = zq[massTerm + sq[[1]] Cm.fl[[1]]] && ! zq[massTerm];
  res["omegaTermNonzeroComponents"] = Count[omTerm, x_ /; ! zq[x]];
  res["LTerms"] = Length[Expand[L0]]; res["sqrtg"] = sq[[1]];
  D16GeoSetAlgebraic[None];
  res];

checkELCommuting[gs_List] := Module[{r, allOK = True, meas = <||>, omOK = True},
  Do[r = elCommuting[g, False];
    allOK = allOK && r["psiDagger"] && r["psi"] && r["directPsiDagger"] && r["directPsi"] && r["momentaForm"] && r["massTermInEquation"];
    omOK = omOK && r["omegaTermNonzeroComponents"] === 16;
    meas[g["label"]] = KeyDrop[r, {"sqrtg"}], {g, gs}];
  addCheck["C00_EL_commutingCurved", allOK];
  addCheck["C00_connection_OmegaTermInFieldEquation", omOK];
  addMeas["EL.commutingCurved", Join[meas, <|"statement" -> "for commuting components (Psi, Psi^* independent commuting symbols for the value, first and second derivatives at the point; m, lambda symbols): the Euler-Lagrange expression of (L1) with respect to Psi^*_a equals sqrt|g| (C(gamma^mu D_mu Psi - (m + lambda S) Psi))_a and with respect to Psi_a equals -sqrt|g| ((D_mu Psibar) gamma^mu + (m + lambda S) Psibar)_a, computed both from the jet identity and from the explicit momenta dL/d(d_mu Psi^*) = -(1/2) sqrt|g| C gamma^mu Psi, dL/d(d_mu Psi) = (1/2) sqrt|g| Psibar gamma^mu; dEL/dm = -sqrt|g| C Psi. These are the expressions Stage 1 derived for the Grassmann field with the left (Psi^dagger) and right (Psi) derivatives (LAG_eulerLagrangePsibar/Psi): identical form. The spin-connection term sqrt|g| C gamma^mu Omega_mu Psi is nonzero in all 16 components."|>]];
  r = elCommuting[First[gs], True];
  addCheck["C00_EL_commutingGeneralSmoothU", r["psiDagger"] && r["psi"] && r["directPsiDagger"] && r["directPsi"]];
  addMeas["EL.commutingGeneralSmoothU", "at " <> First[gs]["label"] <> " with an abstract smooth U (Mathematica function symbol): EL = sqrt|g| C (gamma^mu D_mu Psi - (m + U'(S)) Psi) and -sqrt|g|((D_mu Psibar) gamma^mu + (m + U'(S)) Psibar). For commuting components U may be any smooth function of S (for the Grassmann field only polynomials exist, S^17 = 0)."];
];

(* reality of (L1) for commuting complex components; coefficient-level Hermiticity (statistics-independent) *)
checkReality[g_] := Module[{geo = g["geo"], X, Y, fl, lag, L0, Ld, imOK, sfl, lagS, L0s, K0, Kmu, Lmu, herm, zeroRules},
  symMode[g];
  X = realJets[rX0, rX1, rX2]; Y = realJets[rY0, rY1, rY2];
  fl = {X[[1]] + I Y[[1]], X[[2]] + I Y[[2]], X[[3]] + I Y[[3]], X[[1]] - I Y[[1]], X[[2]] - I Y[[2]], X[[3]] - I Y[[3]]};
  lag = D16GeoLagrangianJets[geo, D16GeoFieldJets @@ fl, mS, lS];
  L0 = lag["L"][[1]]; Ld = lag["L"][[2]];
  imOK = zq[ComplexExpand[Im[L0]]] && AllTrue[Ld, zq[ComplexExpand[Im[#]]] &] && ! zq[L0];
  (* coefficient level: Ls = Psi^dagger K0 Psi + Psi^dagger K^mu d_mu Psi + d_mu Psi^dagger L^mu Psi (+ quartic) *)
  sfl = symJets[];
  lagS = D16GeoLagrangianJets[geo, D16GeoFieldJets @@ sfl, mS, 0];
  L0s = lagS["L"][[1]];
  zeroRules = Join[Thread[sfl[[1]] -> 0], Thread[sfl[[4]] -> 0], Thread[Flatten[sfl[[2]]] -> 0], Thread[Flatten[sfl[[5]]] -> 0]];
  K0 = Table[rd[D[L0s, sQ0[a], sP0[b]]], {a, 0, 15}, {b, 0, 15}];
  Kmu = Table[rd[D[L0s, sQ0[a], sP1[mu, b]]], {mu, 0, 7}, {a, 0, 15}, {b, 0, 15}];
  Lmu = Table[rd[D[L0s, sQ1[mu, a], sP0[b]]], {mu, 0, 7}, {a, 0, 15}, {b, 0, 15}];
  herm = FreeQ[{K0, Kmu, Lmu}, Complex] && zq[K0 - Transpose[K0]] && zq[Lmu - Map[Transpose, Kmu]] && zq[Kmu - Table[(1/2) geo["sqrtg"][[1]] Cm.geo["gamma"][[1, mu]], {mu, 8}]];
  D16GeoSetAlgebraic[None];
  {imOK, herm}];

checkRealityAll[gs_List] := Module[{res = Association[(#["label"] -> checkReality[#]) & /@ gs], stage1},
  addCheck["C00_lagrangian_realCommuting", AllTrue[Values[res], #[[1]] &]];
  addCheck["C00_lagrangian_coefficientHermiticity", AllTrue[Values[res], #[[2]] &]];
  addMeas["lagrangian.reality", <|"points" -> Keys[res],
    "commuting" -> "Psi = X + i Y with real commuting symbols X, Y (value, first and second derivatives), Psi^dagger = X^T - i Y^T, m and lambda real symbols: Im L = 0 exactly for the value and all eight first-derivative jets of L = sqrt|g| Ls.",
    "coefficientLevel" -> "Ls = Psi^dagger K0 Psi + Psi^dagger K^mu d_mu Psi + d_mu Psi^dagger L^mu Psi - m S - U with K0 real symmetric (Hermitian), K^mu = (1/2) sqrt|g| C gamma^mu and L^mu = (K^mu)^dagger = -(1/2) sqrt|g| C gamma^mu: since conjugation reverses products for commuting numbers trivially and for Grassmann numbers by (theta1 theta2)^* = theta2^* theta1^*, (Psi^dagger X Phi)^* = Phi^dagger X^dagger Psi in BOTH algebras, so these coefficient identities make L real (Hermitian) for commuting and for anticommuting components alike (Stage 1 LAG_hermiticity; C00_lagrangian_grassmannFlatHermitianAndEL in the flat Grassmann algebra)."|>];
];

(* ========================================================================= *)
(* 5. the real restriction (notebook-type Lagrangian) in curved space        *)
(* ========================================================================= *)
(* L_nb[X] = sqrt|g| [ X^T C gamma^mu (d_mu X + Omega'_mu X) + (H M) X^T C X ], X real, Omega' = canonical Omega or the
   notebook contraction; its Euler-Lagrange expression for COMMUTING X is
     2 sqrt|g| C (gamma^mu D_mu X + (H M) X) + sqrt|g| C {gamma^mu, Omega'_mu - Omega_mu} X     (D with canonical Omega). *)
kinRealJ[geo_, Z_, OmJ_] := Module[{zJ = {Z[[1]], Z[[2]]}, rowJ, dz},
  rowJ = jL[#.Cm &, zJ];
  dz[mu_] := {Z[[2, mu]], Z[[3, All, mu]]};
  Fold[jAdd, Table[jM[Dot, jM[Dot, rowJ, jPt[geo["gamma"], mu]], jAdd[dz[mu], jM[Dot, jPt[OmJ, mu], zJ]]], {mu, 8}]]];
massRealJ[Z_] := Module[{zJ = {Z[[1]], Z[[2]]}}, jM[Dot, jL[#.Cm &, zJ], zJ]];

realRestrictionCommuting[g_, useNB_] := Module[{geo = g["geo"], X, OmJ, kin, mass, L, L0, Ld, EL, sq, gm, Om, OmNB, tgt, extra, okEL, massPart, kinPart, res = <||>},
  symMode[g];
  X = realJets[sX0, sX1, sX2];
  OmJ = geo[If[useNB, "OmegaNotebook", "Omega"]];
  kin = kinRealJ[geo, X, OmJ]; mass = massRealJ[X];
  L = jM[Times, geo["sqrtg"], jAdd[kin, jL[hS # &, mass]]];
  L0 = L[[1]]; Ld = L[[2]];
  EL = Table[rd[9 D[L0, sX0[a]] - Sum[D[Ld[[mu + 1]], sX1[mu, a]], {mu, 0, 7}]], {a, 0, 15}];
  sq = geo["sqrtg"][[1]]; gm = geo["gamma"][[1]]; Om = geo["Omega"][[1]]; OmNB = geo["OmegaNotebook"][[1]];
  tgt = rd[2 sq Cm.(Sum[gm[[mu]].(X[[2, mu]] + Om[[mu]].X[[1]]), {mu, 8}] + hS X[[1]])];
  extra = rd[sq Cm.Sum[acomm[gm[[mu]], OmNB[[mu]] - Om[[mu]]], {mu, 8}]];
  okEL = zq[EL - tgt - If[useNB, extra.X[[1]], 0]];
  massPart = rd[D[EL, hS]]; kinPart = rd[EL /. hS -> 0];
  res["EL"] = okEL;
  res["massPartIs2sqrtgCX"] = zq[massPart - 2 sq Cm.X[[1]]] && ! zq[massPart];
  (* coefficient matrix of d_4 X in the kinetic part: d EL_i / d(d_4 X_a) = 2 sqrt|g| (C gamma^{x4})_{ia} *)
  res["kineticNotDivergence"] = ! zq[kinPart] && zq[Transpose[Table[D[kinPart, sX1[4, a]], {a, 0, 15}]] - 2 sq Cm.gm[[5]]] &&
    (* exact invertibility: (C gamma^{x4})(gamma^{x4} C) = g^{44} I16 with g^{44} != 0 *)
    zq[(Cm.gm[[5]]).(gm[[5]].Cm) - geo["ginv"][[1, 5, 5]] id16] && ! zq[geo["ginv"][[1, 5, 5]]] && ! zq[sq];
  res["notebookExtraTermNonzero"] = ! zq[extra];
  res["Lnonzero"] = ! zq[L0];
  D16GeoSetAlgebraic[None];
  res];

(* (L1) for commuting Psi = X + i Y versus the real restriction *)
relationToL1[g_] := Module[{geo = g["geo"], X, Y, fl, lag, L1, kX, kY, sX, sY, exp, ELY, ELX, zeroY, sq, gm, Om, tgtX, okRel, okTrunc, okXeq},
  symMode[g];
  X = realJets[sX0, sX1, sX2]; Y = realJets[sY0, sY1, sY2];
  fl = {X[[1]] + I Y[[1]], X[[2]] + I Y[[2]], X[[3]] + I Y[[3]], X[[1]] - I Y[[1]], X[[2]] - I Y[[2]], X[[3]] - I Y[[3]]};
  lag = D16GeoLagrangianJets[geo, D16GeoFieldJets @@ fl, mS, lS];
  L1 = lag["L"];
  kX = kinRealJ[geo, X, geo["Omega"]]; kY = kinRealJ[geo, Y, geo["Omega"]];
  sX = massRealJ[X]; sY = massRealJ[Y];
  exp = jM[Times, geo["sqrtg"], jAdd[jAdd[kX, kY], jAdd[jL[-mS # &, jAdd[sX, sY]], jL[-(lS/2) # &, jM[Times, jAdd[sX, sY], jAdd[sX, sY]]]]]];
  okRel = zq[L1[[1]] - exp[[1]]] && zq[L1[[2]] - exp[[2]]];
  ELY = Table[rd[9 D[L1[[1]], sY0[a]] - Sum[D[L1[[2, mu + 1]], sY1[mu, a]], {mu, 0, 7}]], {a, 0, 15}];
  ELX = Table[rd[9 D[L1[[1]], sX0[a]] - Sum[D[L1[[2, mu + 1]], sX1[mu, a]], {mu, 0, 7}]], {a, 0, 15}];
  zeroY = Join[Thread[Y[[1]] -> 0], Thread[Flatten[Y[[2]]] -> 0], Thread[Flatten[Y[[3]]] -> 0]];
  sq = geo["sqrtg"][[1]]; gm = geo["gamma"][[1]]; Om = geo["Omega"][[1]];
  tgtX = rd[2 sq Cm.(Sum[gm[[mu]].(X[[2, mu]] + Om[[mu]].X[[1]]), {mu, 8}] - (mS + lS X[[1]].Cm.X[[1]]) X[[1]])];
  okTrunc = zq[ELY /. zeroY]; okXeq = zq[(ELX /. zeroY) - tgtX];
  D16GeoSetAlgebraic[None];
  {okRel, okTrunc, okXeq}];

(* the notebook-type Lagrangian for a REAL GRASSMANN field in curved space, with Stage 1's own Grassmann jet algebra *)
grassmannNotebookLg[g_, hm_] := Module[{geo = g["geo"], gGenVec = gp["gGenVec"], gP0 = gp["gP0"], gP1 = gp["gP1"], gRowMat = gp["gRowMat"],
    gMatVecS = gp["gMatVec"], gVecAdd = gp["gVecAdd"], gSum = gp["gSum"], gDotS = gp["gDot"], gScaleJet = gp["gScaleJet"], gScaleNum = gp["gScaleNum"],
    gAddS = gp["gAdd"], gEL = gp["gEulerLagrange"], gZ = gp["gZeroQ"], gVal = gp["gVal"], jConst = gp["jConst"], jPart = gp["jPart"], cjScalar = gp["cjScalar"],
    psi, dpsi, rowC, rows, inner, mass, Lg, E},
  numMode[g];
  psi = gGenVec[gP0]; dpsi = Table[gGenVec[gP1[mu, #] &], {mu, 0, 7}];
  rowC = gRowMat[psi, jConst[Cm]];
  rows = Table[gMatVecS[jPart[geo["gamma"], al], gVecAdd[dpsi[[al]], gMatVecS[jPart[geo["Omega"], al], psi]]], {al, 8}];
  inner = Table[gSum[Table[rows[[al, a]], {al, 8}]], {a, 16}];
  mass = gDotS[rowC, psi];
  Lg = gScaleJet[cjScalar[geo["sqrtg"]], gAddS[gDotS[rowC, inner], gScaleNum[hm, mass]]];
  E = gEL[Lg, gP0, gP1, "left"];
  D16GeoSetAlgebraic[None];
  <|"massZero" -> gZ[mass], "ELzero" -> AllTrue[E, gZ[gVal[#]] &], "LgMonomials" -> Length[Lg], "LgNonzero" -> Length[Lg] > 0|>];

checkRealRestriction[gs_List, gG_] := Module[{rc, rn, rel, gr, ok1, ok2, meas = <||>},
  ok1 = True; ok2 = True;
  Do[rc = realRestrictionCommuting[g, False]; rn = realRestrictionCommuting[g, True];
    ok1 = ok1 && rc["EL"] && rc["massPartIs2sqrtgCX"] && rc["kineticNotDivergence"] && rc["Lnonzero"];
    ok2 = ok2 && rn["EL"] && If[StringStartsQ[g["label"], "G1"], rn["notebookExtraTermNonzero"], ! rn["notebookExtraTermNonzero"]];
    meas[g["label"]] = <|"canonical" -> rc, "notebookContraction" -> rn|>, {g, gs}];
  addCheck["C00_realRestriction_commutingNonTrivial", ok1];
  addCheck["C00_realRestriction_commutingNotebookContraction", ok2];
  addMeas["realRestriction.commutingCurved", Join[meas, <|"statement" -> "REAL COMMUTING Psi16 = X (value, first and second derivative symbols at the point), L_nb = sqrt|g| [X^T C gamma^mu (d_mu X + Omega_mu X) + (H M) X^T C X] with (H M) a symbol: the Euler-Lagrange expression is exactly 2 sqrt|g| C (gamma^mu D_mu X + (H M) X); its mass part 2 sqrt|g| C X and its kinetic part 2 sqrt|g| C gamma^mu D_mu X (coefficient of d_4 X: 2 sqrt|g| C gamma^4, invertible) are nonzero, so neither term is a total divergence; X^T C X is the nonzero form of signature (8,8). The field equation is the Dirac equation gamma^mu D_mu X = m X with m = -H M. With the notebook contraction Omega^nb the Euler-Lagrange expression acquires sqrt|g| C {gamma^mu, Omega^nb_mu - Omega_mu} X, nonzero at the non-diagonal G1 points and zero at the diagonal G2 points ({gamma^mu, Omega_mu} = 0 for diagonal vielbeins, both contractions)."|>]];
  rel = relationToL1[First[gs]];
  addCheck["C00_realRestriction_relationToL1", And @@ rel];
  addMeas["realRestriction.relationToL1", <|"point" -> First[gs]["label"], "decomposition" -> rel[[1]], "consistentTruncation" -> rel[[2]], "realEquation" -> rel[[3]],
    "statement" -> "dirac16complex00 uses the complex (L1). For commuting Psi = X + i Y (X, Y real): L1[X + i Y] = sqrt|g| [K_R[X] + K_R[Y] - m (S_X + S_Y) - U(S_X + S_Y)] exactly (value and all first-derivative jets), K_R[Z] = Z^T C gamma^mu D_mu Z, S_Z = Z^T C Z; for U = 0 this is L_nb[X] + L_nb[Y] with H M = -m: (L1) is the complexification of the notebook-type real Lagrangian, two copies coupled only through U. Y = 0 is a consistent truncation (the Y equations vanish identically at Y = 0) and the X equation is then 2 sqrt|g| C (gamma^mu D_mu X - (m + lambda S_X) X): the real restriction of dirac16complex00 is exactly the notebook's Lg[] (with the canonical connection), and the notebook's Lg[] is non-trivial for commuting fields."|>];
  gr = grassmannNotebookLg[gG, hmList[[1]]];
  addCheck["C00_realRestriction_grassmannCurvedTrivial", gr["massZero"] && gr["ELzero"] && gr["LgNonzero"]];
  addMeas["realRestriction.grassmannCurved", Join[gr, <|"point" -> gG["label"], "HM" -> ratStr[hmList[[1]]],
    "statement" -> "REAL GRASSMANN Psi16 at the same point, Stage 1's own Grassmann algebra with jet coefficients: the mass term Psi^T C Psi vanishes identically and the Euler-Lagrange expressions of sqrt|g|[Psi^T C gamma^mu D_mu Psi + (H M) Psi^T C Psi] vanish identically (the nonzero Lagrangian is a pure divergence, Stage 1 Theorem 6.1)."|>]];
];

(* ========================================================================= *)
(* 6. non-trivial coupling to the spin connection and to gravity             *)
(* ========================================================================= *)
connectionChecks[g_, seed_] := Module[{geo = g["geo"], gm, dgm, Om, sq, Gv, slash, nzSlash, div, jac, riem, F, RF, e0, einv0, spinFromR, fldOff, off, dsq, box, delta, R, k0, cL,
    on, okOS, fldOn, dsqOn, boxOn, mm = 3/7, cd, bar, bil1, omc, omA, bil2, anti, res = <||>},
  numMode[g];
  gm = geo["gamma"][[1]]; dgm = geo["gamma"][[2]]; Om = geo["Omega"][[1]]; sq = geo["sqrtg"]; Gv = geo["christoffel"][[1]];
  slash = rd[Sum[gm[[mu]].Om[[mu]], {mu, 8}]];
  nzSlash = Count[Flatten[slash], x_ /; ! zq[x]];
  res["gammaOmegaNonzeroEntries"] = nzSlash;
  If[! MissingQ[g["H"]], res["gammaOmegaIs3Hgamma0"] = zq[slash - 3 g["H"] gam[[1]]]];
  div = rd[Sum[sq[[2, mu]] gm[[mu]] + sq[[1]] dgm[[mu, mu]], {mu, 8}] - sq[[1]] Sum[comm[gm[[mu]], Om[[mu]]], {mu, 8}]];
  jac = rd[Table[sq[[2, mu]] - sq[[1]] Sum[Gv[[r, r, mu]], {r, 8}], {mu, 8}]];
  res["divergenceIdentity"] = zq[div] && zq[jac];
  (* curvature of the spin connection: F_{mu nu} = (1/2) R_{mu nu ab} S^{ab} (Stage-1 convention) *)
  riem = geo["riemann"]; e0 = geo["e"][[1]]; einv0 = geo["einv"][[1]];
  F = rd[Table[geo["Omega"][[2, mu, nu]] - geo["Omega"][[2, nu, mu]] + comm[Om[[mu]], Om[[nu]]], {mu, 8}, {nu, 8}]];
  RF = rd[Table[eta.Transpose[e0].riem[[All, All, mu, nu]].Transpose[einv0], {mu, 8}, {nu, 8}]];
  spinFromR[Xm_] := (1/2) Flatten[Xm].Flatten[Sp, 1];
  res["curvature"] = zq[F - Map[spinFromR, RF, {2}]] && ! zq[F];
  (* Lichnerowicz with random commuting data *)
  off = fdata[seed]; fldOff = D16GeoFieldJets @@ off;
  dsq = D16GeoDiracSquared[geo, fldOff]; box = D16GeoSpinorLaplacian[geo, fldOff];
  delta = rd[dsq - box]; R = geo["scalarCurvature"];
  k0 = First[Select[Range[16], off[[1, #]] =!= 0 &]];
  cL = If[zq[R], Indeterminate, rd[delta[[k0]]/(R off[[1, k0]])]];
  res["lichnerowiczC"] = gp["exactString"][cL];
  res["lichnerowicz"] = ! zq[R] && zq[delta + (1/4) R off[[1]]] && cL === -1/4;
  res["scalarCurvatureDecimal"] = ToString[CForm[numValue[R]]];
  (* on shell (U = 0): (gamma^mu D_mu)^2 Psi = m^2 Psi and Box Psi - (R/4) Psi = m^2 Psi *)
  {on, okOS} = D16GeoSolveOnShell[geo, fdata[seed + 10], mm, 0];
  fldOn = D16GeoFieldJets @@ on;
  dsqOn = D16GeoDiracSquared[geo, fldOn]; boxOn = D16GeoSpinorLaplacian[geo, fldOn];
  res["onShellSecondOrder"] = okOS && zq[dsqOn - mm^2 on[[1]]] && zq[boxOn - (1/4) R on[[1]] - mm^2 on[[1]]];
  (* the symmetrized kinetic term contains only the totally antisymmetric omega_[cab] *)
  cd = cdata[seed + 20]; bar = cd[[4]].Cm;
  bil1 = rd[(1/2) bar.Sum[acomm[gm[[mu]], Om[[mu]]], {mu, 8}].cd[[1]]];
  omc = rd[Table[Sum[einv0[[c, mu]] geo["omegaLower"][[1, mu, a, b]], {mu, 8}], {c, 8}, {a, 8}, {b, 8}]];
  omA = rd[Table[(omc[[c, a, b]] - omc[[c, b, a]] + omc[[a, b, c]] - omc[[a, c, b]] + omc[[b, c, a]] - omc[[b, a, c]])/6, {c, 8}, {a, 8}, {b, 8}]];
  bil2 = rd[(1/4) Sum[omA[[c, a, b]] bar.acomm[gam[[c]], Sp[[a, b]]].cd[[1]], {c, 8}, {a, 8}, {b, 8}]];
  anti = rd[Sum[acomm[gm[[mu]], Om[[mu]]], {mu, 8}]];
  res["onlyTotallyAntisymmetricOmega"] = zq[bil1 - bil2];
  res["anticommutatorTermNonzero"] = ! zq[anti];
  D16GeoSetAlgebraic[None];
  res];

checkConnection[gs_List] := Module[{res = Association[MapIndexed[(#1["label"] -> connectionChecks[#1, 60000 + 100 #2[[1]]]) &, gs]], ok},
  ok = AllTrue[Values[res], #["gammaOmegaNonzeroEntries"] > 0 && #["divergenceIdentity"] && #["curvature"] && #["lichnerowicz"] && #["onShellSecondOrder"] &&
       #["onlyTotallyAntisymmetricOmega"] && If[KeyExistsQ[#, "gammaOmegaIs3Hgamma0"], #["gammaOmegaIs3Hgamma0"] && ! #["anticommutatorTermNonzero"], #["anticommutatorTermNonzero"]] &];
  addCheck["C00_connection_nonTrivialCoupling", ok];
  addMeas["connection", Join[res, <|"statement" -> "in a curved field the coupling to the spin connection and to gravity is non-trivial for the commuting field exactly as for the Grassmann field (the operator gamma^mu D_mu does not know the statistics): gamma^mu Omega_mu != 0 (G1: nonzero entries listed; G2: = 3 H gamma^0), d_mu(sqrt|g| gamma^mu) = sqrt|g| [gamma^mu, Omega_mu] and d_mu sqrt|g| = sqrt|g| Gamma^rho_{rho mu}, F_{mu nu} = (1/2) R_{mu nu ab} S^{ab} != 0 (Omega cannot be gauged away), Lichnerowicz (gamma^mu D_mu)^2 Psi = g^{mu nu}(D_mu D_nu - Gamma^l_{mu nu} D_l) Psi + c R Psi with c = -1/4 exactly, and on shell (U = 0): (gamma^mu D_mu)^2 Psi = m^2 Psi and Box Psi - (R/4) Psi = m^2 Psi with R != 0 (the curvature enters the second-order equation). The Omega-part of the symmetrized kinetic term is (1/2) Psibar {gamma^mu, Omega_mu} Psi = (1/4) omega_[cab] Psibar gamma^c gamma^a gamma^b Psi: nonzero for the non-diagonal G1, zero for diagonal vielbeins (G2), where the gravitational coupling of the kinetic term is carried by gamma^mu = e_a^mu gamma^a and sqrt|g| and by gamma^mu Omega_mu in the field equation."|>]];
];

(* ========================================================================= *)
(* 7. EMT from the full vielbein variation (general non-diagonal frames)     *)
(* ========================================================================= *)
(* The action density L = sqrt|g| [ e_a^mu F_mu^a + (1/4) e_c^mu omega_{mu ab} B^{cab} - m S - U(S) ] with
   F_mu^a = (1/2)(Psibar gamma^a d_mu Psi - d_mu Psibar gamma^a Psi), B^{cab} = Psibar {gamma^c, S^{ab}} Psi (this is (L1) exactly;
   verified against D16GeoLagrangianJets).  L depends on the vielbein e_mu^a and on d_nu e_mu^a (through omega, which is
   AFFINE in d e).  The functional derivative at the point is
     E[mu,a] = dL/d e_mu^a - sum_nu d_nu ( dL/d(d_nu e_mu^a) ),
   dL/de_mu^a from the exact linearisation of the geometry in the 64 directions E_(mu a); A^nu[mu,a] = dL/d(d_nu e_mu^a)
   in closed form (Y, W, V, Gt below) and as a jet, whose divergence is taken with the product rule.  The metric EMT
   T^{mu nu} = (2/sqrt|g|) dS/dg_{mu nu} is then the symmetric part of X^{mu nu} = sum_a E[mu,a] e^{a nu} / sqrt|g|
   (delta e_mu^a = (1/2) h_{mu l} g^{l k} e_k^a gives delta g = h); the antisymmetric part is the local-Lorentz identity,
   zero on shell. *)
T3[a_] := Transpose[a, {3, 1, 2}]; T132[a_] := Transpose[a, {1, 3, 2}];
glPart[dgl_] := Table[(dgl[[mu, nu, s]] + dgl[[nu, mu, s]] - dgl[[s, mu, nu]])/2, {s, 8}, {mu, 8}, {nu, 8}];
Mabc = Table[Cm.acomm[gam[[c]], Sp[[a, b]]], {c, 8}, {a, 8}, {b, 8}];
MF = Table[Cm.gam[[a]], {a, 8}];
leanBase[fj_] := Module[{e, de, dde, g, dg, gi, dgi, GL, Gam, einv, deinv, X, om, omL, s, ds, ddgK, dGL, dGam, dX, dom, domL},
  {e, de, dde} = fj;
  g = e.eta.Transpose[e];
  dg = Table[de[[l]].eta.Transpose[e] + e.eta.Transpose[de[[l]]], {l, 8}];
  gi = Inverse[g]; dgi = Table[-gi.dg[[l]].gi, {l, 8}];
  GL = glPart[dg]; Gam = gi.GL;
  ddgK = Table[dde[[l, k]].eta.Transpose[e] + de[[l]].eta.Transpose[de[[k]]] + de[[k]].eta.Transpose[de[[l]]] + e.eta.Transpose[dde[[l, k]]], {k, 8}, {l, 8}];
  dGL = Table[glPart[ddgK[[k]]], {k, 8}]; dGam = Table[dgi[[k]].GL + gi.dGL[[k]], {k, 8}];
  einv = Inverse[e]; deinv = Table[-einv.de[[l]].einv, {l, 8}];
  X = T3[Gam].e - de; dX = Table[T3[dGam[[l]]].e + T3[Gam].de[[l]] - dde[[l]], {l, 8}];
  om = T132[X].Transpose[einv]; dom = Table[T132[dX[[l]]].Transpose[einv] + T132[X].Transpose[deinv[[l]]], {l, 8}];
  omL = Map[eta.# &, om]; domL = Map[eta.# &, dom, {2}];
  s = Abs[Det[e]]; ds = Table[s Tr[einv.de[[l]]], {l, 8}];
  <|"e" -> e, "de" -> de, "g" -> g, "gi" -> gi, "dgi" -> dgi, "GL" -> GL, "Gam" -> Gam, "einv" -> einv, "deinv" -> deinv,
    "X" -> X, "omL" -> omL, "domL" -> domL, "s" -> s, "ds" -> ds|>];
leanBil[{p0_, p1_, p2_, q0_, q1_, q2_}] := Module[{F, dF, Bc, dBc, S0, dS},
  F = Table[(1/2) (q0.MF[[a]].p1[[mu]] - q1[[mu]].MF[[a]].p0), {mu, 8}, {a, 8}];
  dF = Table[(1/2) (q1[[l]].MF[[a]].p1[[mu]] + q0.MF[[a]].p2[[l, mu]] - q2[[l, mu]].MF[[a]].p0 - q1[[mu]].MF[[a]].p1[[l]]), {l, 8}, {mu, 8}, {a, 8}];
  Bc = Map[q0.#.p0 &, Mabc, {3}]; dBc = Table[Map[q1[[l]].#.p0 + q0.#.p1[[l]] &, Mabc, {3}], {l, 8}];
  S0 = q0.Cm.p0; dS = Table[q1[[l]].Cm.p0 + q0.Cm.p1[[l]], {l, 8}];
  <|"F" -> F, "dF" -> dF, "B" -> Bc, "dB" -> dBc, "S" -> S0, "dS" -> dS|>];
leanLs[bs_, b_, m_, lam_] := Total[bs["einv"] Transpose[b["F"]], 2] + (1/4) Flatten[bs["einv"].bs["omL"]].Flatten[b["B"]] - m b["S"] - lam b["S"]^2/2;
leanDLs[bs_, b_, m_, lam_, l_] := Total[bs["deinv"][[l]] Transpose[b["F"]], 2] + Total[bs["einv"] Transpose[b["dF"][[l]]], 2] +
  (1/4) (Flatten[bs["deinv"][[l]].bs["omL"]].Flatten[b["B"]] + Flatten[bs["einv"].bs["domL"][[l]]].Flatten[b["B"]] + Flatten[bs["einv"].bs["omL"]].Flatten[b["dB"][[l]]]) -
  (m + lam b["S"]) b["dS"][[l]];
(* value direction delta e = P (derivatives unchanged): first-order change of the value of L *)
leanValDir[bs_, b_, m_, lam_, P_] := Module[{e = bs["e"], de = bs["de"], dgP, giP, GLP, GamP, einvP, XP, omLP, sP},
  dgP = Table[de[[l]].eta.Transpose[P] + P.eta.Transpose[de[[l]]], {l, 8}];
  giP = -bs["gi"].(P.eta.Transpose[e] + e.eta.Transpose[P]).bs["gi"];
  GLP = glPart[dgP]; GamP = giP.bs["GL"] + bs["gi"].GLP;
  einvP = -bs["einv"].P.bs["einv"];
  XP = T3[GamP].e + T3[bs["Gam"]].P;
  omLP = Map[eta.# &, T132[XP].Transpose[bs["einv"]] + T132[bs["X"]].Transpose[einvP]];
  sP = bs["s"] Tr[bs["einv"].P];
  sP leanLs[bs, b, m, lam] + bs["s"] (Total[einvP Transpose[b["F"]], 2] + (1/4) (Flatten[einvP.bs["omL"]].Flatten[b["B"]] + Flatten[bs["einv"].omLP].Flatten[b["B"]]))];
(* derivative direction delta(d_nu e) = P: first-order change of the VALUE of L (= A^nu . P) *)
leanDerValDir[bs_, b_, nu_, P_] := Module[{e = bs["e"], dgP, GLP, XP, omLP},
  dgP = P.eta.Transpose[e] + e.eta.Transpose[P];
  GLP = glPart[Table[If[l == nu, dgP, ConstantArray[0, {8, 8}]], {l, 8}]];
  XP = T3[bs["gi"].GLP].e - Table[If[l == nu, P, ConstantArray[0, {8, 8}]], {l, 8}];
  omLP = Map[eta.# &, T132[XP].Transpose[bs["einv"]]];
  bs["s"] (1/4) Flatten[bs["einv"].omLP].Flatten[b["B"]]];
(* the generic jet-identity route for one direction: delta(d_nu L) for delta(d_nu e) = P *)
leanDerDir[bs_, b_, m_, lam_, nu_, P_] := Module[{e = bs["e"], de = bs["de"], einv = bs["einv"], gi = bs["gi"], dgP, ddgP, dgiP, GLP, dGLP, GamP, dGamP, XP, dXP,
    deinvP, omLP, domLP, dsP, LsP, dLsP},
  dgP = P.eta.Transpose[e] + e.eta.Transpose[P];
  ddgP = Table[de[[l]].eta.Transpose[P] + P.eta.Transpose[de[[l]]] + If[l == nu, P.eta.Transpose[de[[nu]]] + de[[nu]].eta.Transpose[P], 0], {l, 8}];
  GLP = glPart[Table[If[l == nu, dgP, ConstantArray[0, {8, 8}]], {l, 8}]]; GamP = gi.GLP;
  dgiP = -gi.dgP.gi; dGLP = glPart[ddgP];
  dGamP = dgiP.bs["GL"] + (-gi.(de[[nu]].eta.Transpose[e] + e.eta.Transpose[de[[nu]]]).gi).GLP + gi.dGLP;
  XP = T3[GamP].e - Table[If[l == nu, P, ConstantArray[0, {8, 8}]], {l, 8}];
  dXP = T3[dGamP].e + T3[GamP].de[[nu]] + T3[bs["Gam"]].P;
  deinvP = -einv.P.einv;
  omLP = Map[eta.# &, T132[XP].Transpose[einv]];
  domLP = Map[eta.# &, T132[dXP].Transpose[einv] + T132[XP].Transpose[bs["deinv"][[nu]]] + T132[bs["X"]].Transpose[deinvP]];
  dsP = bs["s"] Tr[einv.P];
  LsP = (1/4) Flatten[einv.omLP].Flatten[b["B"]];
  dLsP = Total[deinvP Transpose[b["F"]], 2] + (1/4) (Flatten[deinvP.bs["omL"]].Flatten[b["B"]] + Flatten[bs["deinv"][[nu]].omLP].Flatten[b["B"]] +
     Flatten[einv.domLP].Flatten[b["B"]] + Flatten[einv.omLP].Flatten[b["dB"][[nu]]]);
  dsP leanLs[bs, b, m, lam] + bs["ds"][[nu]] LsP + bs["s"] dLsP];
basisE = Table[ReplacePart[ConstantArray[0, {8, 8}], {i, j} -> 1], {i, 8}, {j, 8}];
(* closed-form A^nu[mu,a] = dL/d(d_nu e_mu^a) and its jet *)
leanARoute[bs_, b_, m_, lam_] := Module[{s = bs["s"], ds = bs["ds"], einv = bs["einv"], deinv = bs["deinv"], gi = bs["gi"], dgi = bs["dgi"], e = bs["e"], de = bs["de"],
    B0 = b["B"], dB0 = b["dB"], Z, dZ, Y, dY, W, dW, V, dV, Gt, dGt, AG, dAG, Aall, dAall, div, val},
  Z = (s/4) Map[eta.# &, Transpose[einv].B0];
  dZ = Table[(ds[[l]]/4) Map[eta.# &, Transpose[einv].B0] + (s/4) Map[eta.# &, Transpose[deinv[[l]]].B0] + (s/4) Map[eta.# &, Transpose[einv].dB0[[l]]], {l, 8}];
  Y = T132[Z.einv]; dY = Table[T132[dZ[[l]].einv + Z.deinv[[l]]], {l, 8}];
  W = Transpose[Y.Transpose[e], {2, 3, 1}]; dW = Table[Transpose[dY[[l]].Transpose[e] + Y.Transpose[de[[l]]], {2, 3, 1}], {l, 8}];
  V = gi.W; dV = Table[dgi[[l]].W + gi.dW[[l]], {l, 8}];
  Gt = (Transpose[V, {3, 1, 2}] + Transpose[V, {3, 2, 1}] - V)/2;
  dGt = Table[(Transpose[dV[[l]], {3, 1, 2}] + Transpose[dV[[l]], {3, 2, 1}] - dV[[l]])/2, {l, 8}];
  AG = (Gt + T132[Gt]).e.eta;
  dAG = Table[((dGt[[l]] + T132[dGt[[l]]]).e + (Gt + T132[Gt]).de[[l]]).eta, {l, 8}];
  Aall = -Y + AG; dAall = Table[-dY[[l]] + dAG[[l]], {l, 8}];
  div = Sum[dAall[[l, l]], {l, 8}];
  val = Table[leanValDir[bs, b, m, lam, basisE[[i, j]]], {i, 8}, {j, 8}];
  <|"E" -> val - div, "A" -> Aall|>];

vielbeinVariation[g_, seedOff_, seedOn_, m_, lam_, spot_] := Module[{geo = g["geo"], bs, off, on, okOS, bOff, bOn, arOff, arOn, Tof, Ton, Xof, Xon, symOff, antiOff, symOn, antiOn,
    lagOff, valid, aOK, spotOK, res = <||>, Tup},
  numMode[g];
  bs = leanBase[g["fj"]];
  valid = zq[bs["omL"] - geo["omegaLower"][[1]]] && zq[bs["domL"] - geo["omegaLower"][[2]]] && zq[bs["einv"] - geo["einv"][[1]]] &&
    zq[{bs["s"], bs["ds"]} - geo["sqrtg"]];
  off = fdata[seedOff];
  {on, okOS} = D16GeoSolveOnShell[geo, fdata[seedOn], m, lam];
  bOff = leanBil[off]; bOn = leanBil[on];
  lagOff = D16GeoLagrangianJets[geo, D16GeoFieldJets @@ off, m, lam];
  valid = valid && zq[bs["s"] leanLs[bs, bOff, m, lam] - lagOff["L"][[1]]] &&
    zq[Table[bs["ds"][[l]] leanLs[bs, bOff, m, lam] + bs["s"] leanDLs[bs, bOff, m, lam, l], {l, 8}] - lagOff["L"][[2]]];
  arOff = leanARoute[bs, bOff, m, lam]; arOn = leanARoute[bs, bOn, m, lam];
  (* A (value level) equals the direct linearisation in all 512 derivative directions *)
  aOK = AllTrue[Flatten[Table[zq[leanDerValDir[bs, bOff, nu, basisE[[i, j]]] - arOff["A"][[nu, i, j]]], {nu, 8}, {i, 8}, {j, 8}]], TrueQ];
  (* generic jet identity E = 9 dL0/de - sum_nu d(d_nu L)/d(d_nu e) for the spot entries *)
  spotOK = AllTrue[spot, zq[9 leanValDir[bs, bOff, m, lam, basisE[[#[[1]], #[[2]]]]] - Sum[leanDerDir[bs, bOff, m, lam, nu, basisE[[#[[1]], #[[2]]]]], {nu, 8}] -
       arOff["E"][[#[[1]], #[[2]]]]] &];
  Tof = Map[First, D16GeoEMTJets[geo, lagOff], {2}];
  Ton = Map[First, D16GeoEMTJets[geo, D16GeoLagrangianJets[geo, D16GeoFieldJets @@ on, m, lam]], {2}];
  Xof = rd[arOff["E"].(eta.bs["einv"])]; Xon = rd[arOn["E"].(eta.bs["einv"])];
  symOff = zq[(Xof + Transpose[Xof])/2 - bs["s"] bs["gi"].Tof.bs["gi"]]; antiOff = ! zq[(Xof - Transpose[Xof])/2];
  symOn = zq[(Xon + Transpose[Xon])/2 - bs["s"] bs["gi"].Ton.bs["gi"]]; antiOn = zq[(Xon - Transpose[Xon])/2];
  res = <|"leanGeometryAndLagrangianMatchStage1" -> valid, "onShellJetsSolved" -> okOS, "AcoefficientsMatchLinearisation512" -> aOK,
    "jetIdentitySpotEntries" -> spot, "jetIdentitySpotAgree" -> spotOK,
    "symmetricPartEqualsSqrtgTupper_offShell" -> symOff, "antisymmetricPartNonzero_offShell" -> antiOff,
    "symmetricPartEqualsSqrtgTupper_onShell" -> symOn, "antisymmetricPartZero_onShell" -> antiOn,
    "seeds" -> {seedOff, seedOn}, "m" -> ratStr[m], "lambda" -> ratStr[lam]|>;
  If[g["label"] === "G1p1", Tup = rd[bs["gi"].Tof.bs["gi"]];
    res["offShellTlowerExact"] = ratMat[rd[Tof]]; res["offShellS"] = ratStr[bOff["S"]]];
  D16GeoSetAlgebraic[None];
  res];

checkVielbeinVariation[gs_List] := Module[{res, ok},
  res = Association[MapIndexed[(#1["label"] -> vielbeinVariation[#1, 61000 + 100 #2[[1]], 61050 + 100 #2[[1]], 3/7, 5/11,
        If[#2[[1]] === 1, {{1, 1}, {2, 6}, {5, 3}}, {}]]) &, gs]];
  ok = AllTrue[Values[res], #["leanGeometryAndLagrangianMatchStage1"] && #["onShellJetsSolved"] && #["AcoefficientsMatchLinearisation512"] && #["jetIdentitySpotAgree"] &&
     #["symmetricPartEqualsSqrtgTupper_offShell"] && #["antisymmetricPartNonzero_offShell"] && #["symmetricPartEqualsSqrtgTupper_onShell"] && #["antisymmetricPartZero_onShell"] &];
  addCheck["C00_EMT_vielbeinVariation", ok];
  addMeas["EMT.vielbeinVariation", Join[res, <|"statement" -> "exact functional derivative E[mu,a] = delta S/delta e_mu^a of (L1) at general points (G1: non-diagonal vielbein with space-space, space-time and time-time mixing; G3: Bianchi-I), with fixed random field data (commuting components; Psi, Psi^dagger independent): (i) the symmetric part of X^{mu nu} = sum_a E[mu,a] e^{a nu} equals sqrt|g| T^{mu nu} of the formula T_{mu nu} = -(1/4)[Psibar gamma_mu D_nu Psi + Psibar gamma_nu D_mu Psi - (D_mu Psibar) gamma_nu Psi - (D_nu Psibar) gamma_mu Psi] + g_{mu nu} L_s in all 36 components, OFF SHELL (so T_{mu nu} = -(2/sqrt|g|) delta S/delta g^{mu nu} exactly, including the variation of the spin connection); (ii) the antisymmetric part (local Lorentz rotations of the frame) is nonzero off shell and vanishes on shell. dL/d(d_nu e) is computed in closed form (omega is affine in d e) and agrees with the exact linearisation in all 512 directions; for three entries the divergence term was also recomputed by the generic jet identity E = 9 dL0/de - sum_nu d(d_nu L)/d(d_nu e) (exact linearisation of the order-1 jets). The derivation uses only products of the bilinears F, B, S with Psi^dagger to the left of Psi, so it holds verbatim for Grassmann components (it lifts the Stage-1 limitation 'off-diagonal components not varied explicitly')."|>]];
];

(* ========================================================================= *)
(* 8. on-shell jets for a general smooth U: U(S0) = u0, U'(S0) = u1, U''(S0) = u2 independent *)
(* ========================================================================= *)
solveOnShellU[geo_, free_, m_] := Module[{p0, p1, p2, q0, q1, q2, a1, b1, a2, b2, fld, lag, gamJ, Sj, ePsi, eBar, uPsi, uBar, solve, sol1, sol2, sol3, all, resid},
  {p0, p1, p2, q0, q1, q2} = free;
  a1 = Array[ua1, 16]; b1 = Array[ub1, 16]; a2 = Table[Array[ua2[nu, #] &, 16], {nu, 8}]; b2 = Table[Array[ub2[nu, #] &, 16], {nu, 8}];
  p1 = ReplacePart[p1, 5 -> a1]; q1 = ReplacePart[q1, 5 -> b1];
  Do[p2[[5, nu]] = a2[[nu]]; p2[[nu, 5]] = a2[[nu]]; q2[[5, nu]] = b2[[nu]]; q2[[nu, 5]] = b2[[nu]], {nu, 8}];
  fld = D16GeoFieldJets[p0, p1, p2, q0, q1, q2];
  lag = D16GeoLagrangianJets[geo, fld, m, 0];
  gamJ = geo["gamma"]; Sj = lag["S"];
  (* U'(S) Psi as a jet: value u1 Psi, derivative u1 d Psi + u2 dS Psi *)
  uPsi = {rd[uu1 p0], Table[rd[uu1 p1[[l]] + uu2 Sj[[2, l]] p0], {l, 8}]};
  uBar = {rd[uu1 lag["bar"][[1]]], Table[rd[uu1 lag["bar"][[2, l]] + uu2 Sj[[2, l]] lag["bar"][[1]]], {l, 8}]};
  ePsi = Fold[jAdd, Table[jM[Dot, jPt[gamJ, mu], lag["Dpsi"][[mu]]], {mu, 8}]]; ePsi = jAdd[ePsi, jL[-m # &, lag["psi"]]]; ePsi = jAdd[ePsi, jL[-# &, uPsi]];
  eBar = Fold[jAdd, Table[jM[Dot, lag["Dbar"][[mu]], jPt[gamJ, mu]], {mu, 8}]]; eBar = jAdd[eBar, jL[m # &, lag["bar"]]]; eBar = jAdd[eBar, uBar];
  solve[eqs_, vars_] := Module[{ca = CoefficientArrays[eqs, vars]}, If[Length[ca] =!= 2, Throw["nonlinear"]]; Thread[vars -> rd[LinearSolve[Normal[ca[[2]]], -Normal[ca[[1]]]]]]];
  sol1 = solve[Join[ePsi[[1]], eBar[[1]]], Join[a1, b1]];
  sol2 = Join @@ Table[If[nu == 5, {}, solve[rd[Join[ePsi[[2, nu]], eBar[[2, nu]]] /. sol1], Join[a2[[nu]], b2[[nu]]]]], {nu, 8}];
  sol3 = solve[rd[rd[Join[ePsi[[2, 5]], eBar[[2, 5]]] /. sol1] /. sol2], Join[a2[[5]], b2[[5]]]];
  all = Join[sol1, sol2, sol3];
  resid = rd[{ePsi, eBar} /. all];
  {rd[{p0, p1, p2, q0, q1, q2} /. all], zq[resid]}];

(* T jets with a general U: L_s -> L_s(lambda = 0) - U(S), U jet {u0, u1 dS} *)
emtU[geo_, fl_, m_] := Module[{lag = D16GeoLagrangianJets[geo, D16GeoFieldJets @@ fl, m, 0], lagU},
  lagU = lag;
  lagU["Ls"] = {rd[lag["Ls"][[1]] - uu0], Table[rd[lag["Ls"][[2, l]] - uu1 lag["S"][[2, l]]], {l, 8}]};
  <|"T" -> D16GeoEMTJets[geo, lagU], "lag" -> lagU|>];

currentDivergence[geo_, lag_] := Module[{jmu},
  jmu = Table[jM[Times, geo["sqrtg"], jM[Dot, lag["bar"], jM[Dot, jPt[geo["gamma"], mu], lag["psi"]]]], {mu, 8}];
  rd[Sum[jmu[[mu, 2, mu]], {mu, 8}]]];

(* ========================================================================= *)
(* 9. EMT: symmetry, reality, conservation, trace, current, observer splits  *)
(* ========================================================================= *)
emtChecks[g_, seed_, m_, lam_] := Module[{geo = g["geo"], off, on, okOS, lagOff, lagOn, Toff, Ton, divOff, divOn, sym, cd, lagC, Tc, real, jReal, ginv, tr, S0, trExp,
    curOn, curOff, onU, okU, eU, divU, trU, S0U, curU, valid, onL, okL, res = <||>, gauss, rho, K, K4, KEH, PEH, split, pis},
  numMode[g];
  ginv = geo["ginv"][[1]];
  off = fdata[seed]; lagOff = D16GeoLagrangianJets[geo, D16GeoFieldJets @@ off, m, lam];
  Toff = D16GeoEMTJets[geo, lagOff]; divOff = D16GeoEMTDivergence[geo, Toff];
  {on, okOS} = D16GeoSolveOnShell[geo, fdata[seed + 10], m, lam];
  lagOn = D16GeoLagrangianJets[geo, D16GeoFieldJets @@ on, m, lam];
  Ton = D16GeoEMTJets[geo, lagOn]; divOn = D16GeoEMTDivergence[geo, Ton];
  sym = zq[Map[First, Toff, {2}] - Transpose[Map[First, Toff, {2}]]];
  (* reality for Psi^dagger = conjugate(Psi): T real, J^mu = -i Psibar gamma^mu Psi real (j^mu = Psibar gamma^mu Psi imaginary) *)
  cd = cdata[seed + 20]; lagC = D16GeoLagrangianJets[geo, D16GeoFieldJets @@ cd, m, lam];
  Tc = Map[First, D16GeoEMTJets[geo, lagC], {2}];
  real = zq[ComplexExpand[Im[Tc]]] && ! zq[Tc];
  jReal = AllTrue[Range[8], zq[ComplexExpand[Im[-I cd[[4]].Cm.geo["gamma"][[1, #]].cd[[1]]]]] && zq[ComplexExpand[Re[cd[[4]].Cm.geo["gamma"][[1, #]].cd[[1]]]]] &];
  S0 = lagOn["S"][[1]];
  tr = rd[Sum[ginv[[mu, nu]] Ton[[mu, nu, 1]], {mu, 8}, {nu, 8}]]; trExp = rd[-m S0 + 7 S0 (lam S0) - 8 (lam/2) S0^2];
  curOn = currentDivergence[geo, lagOn]; curOff = currentDivergence[geo, lagOff];
  res["symmetricOffShell"] = sym; res["realForConjugateData"] = real; res["currentJReal"] = jReal;
  res["conservationOnShell"] = okOS && zq[divOn]; res["divergenceNonzeroOffShell"] = ! zq[divOff];
  res["traceOnShell"] = zq[tr - trExp] && ! zq[S0]; res["currentConservedOnShell"] = zq[curOn]; res["currentDivergenceNonzeroOffShell"] = ! zq[curOff];
  (* general smooth U: U(S0) = u0, U'(S0) = u1, U''(S0) = u2 independent symbols *)
  symMode[g];
  {onU, okU} = solveOnShellU[geo, fdata[seed + 30], m];
  (* the solver reproduces D16GeoSolveOnShell for U = (lambda/2) S^2 *)
  S0U = rd[onU[[4]].Cm.onU[[1]]];
  {onL, okL} = D16GeoSolveOnShell[geo, fdata[seed + 30], m, lam];
  valid = okL && zq[rd[onU /. {uu1 -> lam S0U, uu2 -> lam, uu0 -> lam S0U^2/2}] - onL];
  eU = emtU[geo, onU, m];
  divU = D16GeoEMTDivergence[geo, eU["T"]];
  trU = rd[Sum[ginv[[mu, nu]] eU["T"][[mu, nu, 1]], {mu, 8}, {nu, 8}]];
  curU = currentDivergence[geo, eU["lag"]];
  res["generalU_onShellSolved"] = okU; res["generalU_solverMatchesStage1ForQuartic"] = valid;
  res["generalU_conservation"] = zq[divU]; res["generalU_trace"] = zq[trU - (-m S0U + 7 S0U uu1 - 8 uu0)]; res["generalU_currentConserved"] = zq[curU];
  numMode[g];
  (* observer split in Gaussian normal time (g_44 = -1, g_4i = 0): rho = T_44 = KE_H + PE_H identically *)
  gauss = zq[geo["g"][[1, 5, 5]] + 1] && zq[Delete[geo["g"][[1, 5]], 5]];
  If[gauss,
    rho = Toff[[5, 5, 1]]; K = lagOff["kinetic"][[1]]; K4 = 2 lagOff["KE"][[1]];
    KEH = rd[-(K - K4)]; PEH = rd[m lagOff["S"][[1]] + (lam/2) lagOff["S"][[1]]^2];
    split = zq[rho - KEH - PEH] && zq[rho - (K4 - lagOff["Ls"][[1]])];
    pis = rd[Table[ginv[[i, i]] Toff[[i, i, 1]], {i, Delete[Range[8], 5]}]];
    res["gaussianNormal"] = True; res["rhoEqualsKEHplusPEH_offShell"] = split,
    res["gaussianNormal"] = False];
  res["traceOnShellValue"] = gp["exactString"][tr];
  D16GeoSetAlgebraic[None];
  res];

checkEMT[gs_List] := Module[{res, ok1, ok2, ok3, ok4, ok5, ok6},
  res = Association[MapIndexed[(#1["label"] -> emtChecks[#1, 62000 + 100 #2[[1]], mList[[Mod[#2[[1]] - 1, 3] + 1]], lamList[[Mod[#2[[1]] - 1, 3] + 1]]]) &, gs]];
  ok1 = AllTrue[Values[res], #["symmetricOffShell"] && #["realForConjugateData"] &];
  ok2 = AllTrue[Values[res], #["conservationOnShell"] && #["divergenceNonzeroOffShell"] &];
  ok3 = AllTrue[Values[res], #["traceOnShell"] &];
  ok4 = AllTrue[Values[res], #["currentConservedOnShell"] && #["currentDivergenceNonzeroOffShell"] && #["currentJReal"] &];
  ok5 = AllTrue[Values[res], #["generalU_onShellSolved"] && #["generalU_solverMatchesStage1ForQuartic"] && #["generalU_conservation"] && #["generalU_trace"] && #["generalU_currentConserved"] &];
  ok6 = AllTrue[Select[Values[res], #["gaussianNormal"] &], #["rhoEqualsKEHplusPEH_offShell"] &] && Count[Values[res], r_ /; r["gaussianNormal"]] > 0;
  addCheck["C00_EMT_symmetricAndReal", ok1];
  addCheck["C00_EMT_conservationOnShell", ok2];
  addCheck["C00_EMT_traceOnShell", ok3];
  addCheck["C00_current_conservationAndReality", ok4];
  addCheck["C00_EMT_generalSmoothU", ok5];
  addCheck["C00_EMT_observerSplitGaussianNormal", ok6];
  addMeas["EMT.properties", Join[res, <|"statement" -> "commuting components, exact jets (G1: general non-diagonal; G2: primordial with arbitrary a4, numbers in Q(cos z)): T_{mu nu} symmetric off shell; real for Psi^dagger = Psi^* (complex Gaussian-rational data); nabla^mu T_{mu nu} = 0 when the field equations and their first derivatives hold (solved exactly at the point for the x4 derivatives), nonzero off shell; T^mu_mu = -m S + 7 S U'(S) - 8 U(S) on shell (= -m S + 3 lambda S^2 for U = (lambda/2) S^2); the current j^mu = Psibar gamma^mu Psi (purely imaginary; J^mu = -i j^mu real) satisfies d_mu(sqrt|g| j^mu) = 0 on shell. For a GENERAL SMOOTH U the values U(S0) = u0, U'(S0) = u1, U''(S0) = u2 are independent symbols: conservation, the trace -m S + 7 S u1 - 8 u0 and current conservation hold identically in u0, u1, u2, i.e. for every smooth U (the solver reproduces Stage 1's for the quartic U). In Gaussian normal time (G2): rho = T_44 = KE_H + PE_H identically, KE_H = -K_perp, PE_H = m S + U, and rho = K_4 - L_s. For dirac16complex (Grassmann) the same formulas hold as operator identities (Stage 1 Section 9; the quartic term there enters through the even element S)."|>]];
];

(* homogeneous (Bianchi-I, G3) on-shell reduction: rho, pressures, KE/PE, EoS; lambda and a general smooth U *)
homogeneousG3[k_, m_, lam_] := Module[{g = geoAt["G3", k, False], geo, base, free, onL, okL, onU, okU, hv, hdv, Hh, trans, fields, out = <||>, eval, homogQ},
  geo = g["geo"];
  hv = Diagonal[g["fj"][[1]]]; hdv = Diagonal[g["fj"][[2, 5]]]; Hh = hdv/hv; trans = Delete[Range[8], 5];
  base = fdata[63000 + 100 k];
  free = {base[[1]], ConstantArray[0, {8, 16}], ConstantArray[0, {8, 8, 16}], base[[4]], ConstantArray[0, {8, 16}], ConstantArray[0, {8, 8, 16}]};
  homogQ[d_] := zq[Delete[d[[2]], 5]] && zq[Delete[d[[5]], 5]] && zq[ReplacePart[d[[3]], {5, 5} -> ConstantArray[0, 16]]] && zq[ReplacePart[d[[6]], {5, 5} -> ConstantArray[0, 16]]];
  eval[data_, lagJ_, TJ_, U0_, U1_] := Module[{ginv = geo["ginv"][[1]], gl = geo["gammaLower"][[1]], gm = geo["gamma"][[1]], S0, rho, pis, KEL, PEL, K, KEH, PEH, Tij, T4i, ok},
    S0 = lagJ["S"][[1]]; rho = TJ[[5, 5, 1]]; pis = rd[Table[ginv[[i, i]] TJ[[i, i, 1]], {i, trans}]];
    KEL = lagJ["KE"][[1]]; PEL = rd[rho - KEL]; K = lagJ["kinetic"][[1]]; KEH = rd[-(K - 2 KEL)]; PEH = rd[m S0 + U0];
    Tij = AllTrue[Flatten[Table[If[i == j, True, zq[TJ[[i, j, 1]] - (1/4) (Hh[[i]] - Hh[[j]]) lagJ["bar"][[1]].gl[[i]].gl[[j]].gm[[5]].lagJ["psi"][[1]]]], {i, trans}, {j, trans}]], TrueQ];
    T4i = zq[Table[TJ[[5, i, 1]], {i, trans}]];
    ok = <|"rho" -> zq[rho - (m S0 + U0)], "pressuresIsotropic" -> zq[pis - ConstantArray[S0 U1 - U0, 7]], "KE_L" -> zq[KEL - (1/2) S0 (m + U1)],
      "PE_L" -> zq[PEL - (1/2) (m S0 + 2 U0 - S0 U1)], "KE_H" -> zq[KEH], "PE_H" -> zq[rho - PEH], "rhoPlusP" -> zq[rho + pis[[1]] - 2 KEL], "pMinus" -> zq[pis[[1]] - (KEL - PEL)],
      "Tij" -> Tij, "T4iZeroOnShell" -> T4i, "TijNonzero" -> AnyTrue[Flatten[Table[If[i == j, False, ! zq[TJ[[i, j, 1]]]], {i, trans}, {j, trans}]], TrueQ]|>;
    <|"ok" -> ok, "rho" -> rho, "p" -> pis[[1]], "KEL" -> KEL, "PEL" -> PEL, "S" -> S0|>];
  numMode[g];
  {onL, okL} = D16GeoSolveOnShell[geo, free, m, lam];
  out["quartic"] = Module[{lagJ = D16GeoLagrangianJets[geo, D16GeoFieldJets @@ onL, m, lam], r},
    r = eval[onL, lagJ, D16GeoEMTJets[geo, lagJ], (lam/2) lagJ["S"][[1]]^2, lam lagJ["S"][[1]]];
    Join[r["ok"], <|"solved" -> okL && homogQ[onL], "rhoExact" -> ratStr[r["rho"]], "pExact" -> ratStr[r["p"]], "KE_LExact" -> ratStr[r["KEL"]], "PE_LExact" -> ratStr[r["PEL"]],
      "wExact" -> ratStr[Together[r["p"]/r["rho"]]], "SExact" -> ratStr[r["S"]], "x4" -> ratStr[g["x4"]], "m" -> ratStr[m], "lambda" -> ratStr[lam]|>]];
  symMode[g];
  {onU, okU} = solveOnShellU[geo, free, m];
  out["generalU"] = Module[{eU = emtU[geo, onU, m], r},
    r = eval[onU, eU["lag"], eU["T"], uu0, uu1];
    Join[r["ok"], <|"solved" -> okU && homogQ[onU]|>]];
  D16GeoSetAlgebraic[None];
  out];

checkHomogeneous[] := Module[{res = Association[Table[("G3t" <> ToString[k]) -> homogeneousG3[k, mList[[k]], lamList[[k]]], {k, 3}]], ok},
  ok = AllTrue[Values[res], Function[r, AllTrue[{"quartic", "generalU"}, Function[key, AllTrue[KeyDrop[r[key], {"rhoExact", "pExact", "KE_LExact", "PE_LExact", "wExact", "SExact", "x4", "m", "lambda"}], TrueQ]]]]];
  addCheck["C00_EMT_homogeneousEquationsOfState", ok];
  addMeas["EMT.homogeneous", Join[res, <|"statement" -> "homogeneous commuting field Psi(x4) in the Bianchi-I frames G3 (ds^2 = -dt^2 + sum eps_i h_i(t)^2 dx_i^2), on shell, for U = (lambda/2) S^2 AND for a general smooth U (u0 = U(S), u1 = U'(S) symbols): rho = T_44 = m S + U, p_(i) = T^i_i = S U' - U in all seven transverse directions (isotropic although the h_i differ), KE_L = (1/2) K_4 = (1/2) S (m + U'), PE_L = rho - KE_L = (1/2)(m S + 2U - S U'), KE_H = 0, PE_H = m S + U = rho, rho + p = 2 KE_L, p = KE_L - PE_L, hence w = p/rho = (S U' - U)/(m S + U) = (KE_L - PE_L)/(KE_L + PE_L); T_ij = (1/4)(H_i - H_j) Psibar gamma_i gamma_j gamma^{x4} Psi (nonzero for generic states), T_4i = 0 on shell. Free field (U = 0): w = 0 (dust); default U: w = lambda S/(2m + lambda S)."|>]];
];

(* ========================================================================= *)
(* 10. dirac16complex00 specifics: indefinite charge, energy unbounded below *)
(* ========================================================================= *)
checkChargeIndefinite[g2_] := Module[{bp, bm, jp, jm, g4x, okG, al, be, c1, c2, cpm, cpp, Hf, hg4, mc, kExp, formOK, eig},
  bp = NullSpace[Bm - id16]; bm = NullSpace[Bm + id16];
  jp = Conjugate[bp[[1]]].Bm.bp[[1]]; jm = Conjugate[bm[[1]]].Bm.bm[[1]];
  (* Gaussian normal gauge of the primordial field: gamma^{x4} = gamma^{a=4}, so J^4 = Psi^dagger B Psi there *)
  numMode[g2]; g4x = g2["geo"]["gamma"][[1, 5]]; okG = zq[g4x - gam[[5]]] && zq[g2["geo"]["ginv"][[1, 5, 5]] + 1]; D16GeoSetAlgebraic[None];
  (* every Spin(4,4)-invariant Hermitian form H = alpha C P_- + beta C P_+ gives Herm(c H gamma^4) traceless with square |k|^2: signature (8,8) *)
  cpm = Cm.(id16 - chi8)/2; cpp = Cm.(id16 + chi8)/2;
  Hf = al cpm + be cpp; hg4 = Hf.gam[[5]];
  mc = ComplexExpand[((c1 + I c2) hg4 + ConjugateTranspose[(c1 + I c2) hg4])/2];
  kExp = ComplexExpand[((c1 - I c2) be - (c1 + I c2) al)/2];
  formOK = Expand[Tr[mc]] === 0 && Expand[ComplexExpand[mc.mc] - ComplexExpand[kExp Conjugate[kExp]] id16] === ConstantArray[0, {16, 16}] &&
    AllTrue[Sp[[#[[1]] + 1, #[[2]] + 1]] & /@ spinPairs, Transpose[#].cpm + cpm.# === z16 && Transpose[#].cpp + cpp.# === z16 &];
  eig = Sort[Eigenvalues[Bm]];
  addCheck["C00_charge_indefinite", Cm.gam[[5]] === I Bm && Length[bp] === 8 && Length[bm] === 8 && jp === Conjugate[bp[[1]]].bp[[1]] && jm === -Conjugate[bm[[1]]].bm[[1]] &&
    jp > 0 && jm < 0 && okG && formOK && hermQ[Bm] && eig === Join[ConstantArray[-1, 8], ConstantArray[1, 8]]];
  addMeas["charge.indefinite", <|"PsiPlus" -> gqVec[bp[[1]]], "J4Plus" -> jp, "normPlus" -> Conjugate[bp[[1]]].bp[[1]], "PsiMinus" -> gqVec[bm[[1]]], "J4Minus" -> jm, "normMinus" -> Conjugate[bm[[1]]].bm[[1]],
    "statement" -> "C gamma^4 = i B, so j^4 = Psibar gamma^4 Psi = i Psi^dagger B Psi and the real Noether charge density J^4 = -i j^4 = Psi^dagger B Psi (Gaussian normal gauge, gamma^{x4} = gamma^{a=4}, verified in the primordial field). B is Hermitian with eigenvalues +1 and -1 eight times each, so J^4 is INDEFINITE on commuting spinors: J^4 = +|Psi|^2 and -|Psi|^2 on the exact eigenvectors listed. Every Spin(4,4)-invariant Hermitian form is H = alpha C P_- + beta C P_+ and every candidate charge density Herm(c H gamma^4) is traceless with square |k|^2 (k = (conj(c) beta - c alpha)/2): eigenvalues +-|k| eight times, so no conserved positive-definite charge density of this type exists. The Dirac probability interpretation of the original 4-component theory fails in (4,4) for the classical field dirac16complex00."|>];
];

checkEnergyUnbounded[] := Module[{m = 1, k = {1, 1, 2, 3}, hh, X = Array[xE, 8, 0], pw, pwb, emt44, fe, cases, res, gordon, rows, homog, fam, famRows, okFam, rhoFam, V0, u0},
  hh[M_, kk_] := -I M gam[[5]] - gam[[5]].Sum[kk[[j]] gam[[j]], {j, 4}];
  pw[u_, w_, kk_] := u Exp[-I w X[[5]] + I Sum[kk[[j]] X[[j]], {j, 4}]];
  pwb[u_, w_, kk_] := Conjugate[u] Exp[I w X[[5]] - I Sum[kk[[j]] X[[j]], {j, 4}]];
  (* flat (4,4): T_44 = -(1/4)[2 Psibar gamma_4 d_4 Psi - 2 d_4 Psibar gamma_4 Psi] + eta_44 L_s, gamma_4 = -gamma^4 *)
  emt44[psi_, psib_, mm_, lam_] := Module[{bar = psib.Cm, dp, db, S, Ls},
    dp = Table[D[psi, X[[mu]]], {mu, 8}]; db = Table[D[bar, X[[mu]]], {mu, 8}]; S = bar.psi;
    Ls = (1/2) Sum[bar.gam[[mu]].dp[[mu]] - db[[mu]].gam[[mu]].psi, {mu, 8}] - mm S - (lam/2) S^2;
    Simplify[-(1/4) (2 bar.(-gam[[5]]).dp[[5]] - 2 db[[5]].(-gam[[5]]).psi) - Ls]];
  fe[psi_, psib_, mm_, lam_] := Simplify[Sum[gam[[mu]].D[psi, X[[mu]]], {mu, 8}] - (mm + lam (psib.Cm.psi)) psi];
  (* (a) U = 0: the four combinations (frequency sign, Krein sign) *)
  cases = Flatten[Table[Module[{V = NullSpace[Join[hh[m, k] - w id16, Bm - b id16]], u, rho, res0},
      u = V[[1]];
      res0 = fe[pw[u, w, k], pwb[u, w, k], m, 0];
      rho = emt44[pw[u, w, k], pwb[u, w, k], m, 0];
      <|"omega" -> w, "kreinSign" -> b, "dim" -> Length[V], "solves" -> (res0 === ConstantArray[0, 16]), "rho" -> rho, "J4" -> Conjugate[u].Bm.u, "norm" -> Conjugate[u].u,
        "rhoIsOmegaJ4" -> (rho === w Conjugate[u].Bm.u), "u" -> gqVec[u]|>], {w, {4, -4}}, {b, {1, -1}}], 1];
  (* Gordon-type identity on every eigenspace: C = (M/omega) B as Hermitian forms *)
  gordon = AllTrue[{{1, {1, 1, 2, 3}, 4}, {1, {1, 1, 2, 3}, -4}, {3/5, {0, 0, 0, 4/5}, 1}, {3/5, {0, 0, 0, 4/5}, -1}}, Module[{V = NullSpace[hh[#[[1]], #[[2]]] - #[[3]] id16]},
      Length[V] === 8 && Simplify[Conjugate[V].Cm.Transpose[V] - (#[[1]]/#[[3]]) Conjugate[V].Bm.Transpose[V]] === ConstantArray[0, {8, 8}]] &];
  (* (b) U = (lambda/2) S^2, lambda < 0: homogeneous rest states, rho = m S + (lambda/2) S^2 -> -infinity *)
  homog = Table[Module[{lam = -1, V, u, Sv, Meff, psi, psib, rho, sol},
      V = NullSpace[Join[-I gam[[5]] - id16, Bm - id16]];   (* -i gamma^4 u = u and B u = u: S = u^dagger C u = u^dagger B u > 0 *)
      u = Sqrt[s0/(Conjugate[V[[1]]].V[[1]])] V[[1]];
      Sv = Simplify[Conjugate[u].Cm.u]; Meff = m + lam Sv;
      psi = u Exp[-I Meff X[[5]]]; psib = Conjugate[u] Exp[I Meff X[[5]]];
      sol = fe[psi, psib, m, lam] === ConstantArray[0, 16];
      rho = emt44[psi, psib, m, lam];
      <|"S" -> Sv, "lambda" -> lam, "solves" -> sol, "rho" -> rho, "rhoFormula" -> (Simplify[rho - (m Sv + (lam/2) Sv^2)] === 0)|>], {s0, {1, 10, 100}}];
  (* (c) lambda = 1 > 0: self-consistent plane waves with omega = 1, M_eff = M in (0, 1), |k| = sqrt(1 - M^2), S = M - 1 < 0:
     rho(M) = m S + (lambda/2) S^2 + |k|^2 S/M -> -infinity as M -> 0+ *)
  fam = {{3/5, 4/5}, {5/13, 12/13}, {7/25, 24/25}, {9/41, 40/41}, {11/61, 60/61}};
  famRows = Table[Module[{M = p[[1]], kx = p[[2]], lam = 1, S0, V, u, J0, a2, psi, psib, rho, sol, kv},
      kv = {0, 0, 0, kx};
      S0 = (M - m)/lam;
      V = NullSpace[Join[hh[M, kv] - id16, Bm + id16]];      (* omega = 1, Krein sign -1 *)
      J0 = Conjugate[V[[1]]].Bm.V[[1]];
      a2 = (S0/M)/J0;                                        (* S = (M/omega) J  =>  J = S/M *)
      u = Sqrt[a2] V[[1]];
      psi = u Exp[-I X[[5]] + I kx X[[4]]]; psib = Conjugate[u] Exp[I X[[5]] - I kx X[[4]]];
      sol = fe[psi, psib, m, lam] === ConstantArray[0, 16];
      rho = emt44[psi, psib, m, lam];
      <|"M" -> M, "k" -> kx, "S" -> Simplify[psib.Cm.psi], "solves" -> sol, "rho" -> rho,
        "rhoFormula" -> (Simplify[rho - (m S0 + (lam/2) S0^2 + kx^2 S0/M)] === 0)|>], {p, fam}];
  rhoFam = #["rho"] & /@ famRows;
  okFam = AllTrue[famRows, #["solves"] && #["rhoFormula"] && #["S"] === #["M"] - 1 &] && And @@ Thread[Differences[rhoFam] < 0] &&
    Limit[(M - 1) + (M - 1)^2/2 + (1 - M^2) (M - 1)/M, M -> 0, Direction -> "FromAbove"] === -Infinity;
  addCheck["C00_energy_unboundedBelow", AllTrue[cases, #["solves"] && #["rhoIsOmegaJ4"] && #["dim"] === 4 &] &&
    Sort[Sign[#["rho"]] & /@ cases] === {-1, -1, 1, 1} && gordon && AllTrue[homog, #["solves"] && #["rhoFormula"] &] &&
    And @@ Thread[Differences[#["rho"] & /@ homog] < 0] && okFam];
  addMeas["energy.unboundedBelow", <|"freePlaneWaves" -> cases, "gordonIdentity" -> gordon, "homogeneousNegativeLambda" -> homog, "selfConsistentPlaneWavesPositiveLambda" -> famRows,
    "statement" -> "flat (4,4), commuting components. (a) U = 0: Psi = u e^{-i omega x4 + i k.x} with m = 1, k = (1,1,2,3,0,0,0), omega = +-4: each eigenspace of h_k (dim 8) splits into Krein signs B = +-1 (dim 4 each); every such plane wave solves the field equation exactly and has energy density rho = T_44 = omega J^4, J^4 = u^dagger B u: rho > 0 for (omega, B) = (+,+), (-,-) and rho < 0 for (+,-), (-,+); rho(c Psi) = |c|^2 rho(Psi), so the classical energy is unbounded below. (b) On every eigenspace C = (M/omega) B as forms (Gordon identity), i.e. S = (M/omega) J^4 for plane waves. (c) U = (lambda/2) S^2, lambda = -1: homogeneous rest states with S = 1, 10, 100 solve the nonlinear equation and have rho = m S + (lambda/2) S^2 = 1/2, -40, -4900. (d) lambda = +1: self-consistent plane waves (omega = 1, M_eff = M, |k|^2 = 1 - M^2, S = M - 1, amplitude fixed by S = (M/omega) J^4) solve the nonlinear equation exactly with rho = m S + (lambda/2) S^2 + |k|^2 S/M, strictly decreasing along M = 3/5, 5/13, 7/25, 9/41, 11/61 and -> -infinity as M -> 0+. So the classical energy of dirac16complex00 is not bounded below for U = 0 and for either sign of lambda. For dirac16complex the same indefinite Krein form B is the canonical anticommutator {Psi, Psi^dagger} = B delta/sqrt|g|; its positive-norm (J = B) quantization gives a normal-ordered Hamiltonian >= 0 in the good sector (Stage 1 Section 10.7, QNT_kreinSignature) - a mechanism that requires the Grassmann (Fermi) statistics and has no classical counterpart."|>];
];

(* ========================================================================= *)
(* 11. the primordial field: Stage-2 chart (arbitrary a4)                    *)
(* ========================================================================= *)
pp[s_String] := Symbol["Dirac16ComplexPrimordial`Private`" <> s];
kp[s_String] := Symbol["Dirac16ComplexKohnSham`Private`" <> s];

checkPrimordialStage2[] := Module[{z = pp["z"], t = pp["t"], H = pp["H"], a4 = pp["a4"], x0 = pp["x0"], x4 = pp["x4"], Yv = pp["Yv"], Ps = pp["Ps"], Pb = pp["Pb"],
    uu = pp["uu"], ub = pp["ub"], mmP = pp["mm"], lamP = pp["lam"], UsP = pp["Us"], MeffP = pp["Meff"], zeroQP = pp["zeroQ"], zeroXQ = pp["zeroXQ"], d1 = pp["d1"],
    elOp = pp["elOp"], emtLower = pp["emtLower"], G = pp["G"], C16P, gUF, OmF, giF, sqrtgF, coordsX, frameX, geoS, okGeo, psi, psib, S0, Dpsi, Dpsib, Lag, ELb, ELp, tgtb, tgtp, okEL,
    uv, ubv, SX, onX, eX, TlowX, TmixX, K4, KEH, okHom, homRes, ex, okEx, exRes},
  pp["buildGeometry"][];
  C16P = pp["C16"]; gUF = pp["gUF"]; OmF = pp["OmF"]; giF = pp["giF"]; sqrtgF = pp["sqrtgF"];
  (* my own symbolic geometry (Stage-1 D16GeoSymbolicGeometry) for the notebook frame in x0..x7 against the Stage-2 package *)
  coordsX = {x0, pp["x1"], pp["x2"], pp["x3"], x4, pp["x5"], pp["x6"], pp["x7"]};
  frameX = DiagonalMatrix[{Cot[6 H x0], Sin[6 H x0]^(1/6) E^a4[H x4], Sin[6 H x0]^(1/6) E^a4[H x4], Sin[6 H x0]^(1/6) E^a4[H x4], 1,
     Sin[6 H x0]^(1/6) E^(-a4[H x4]), Sin[6 H x0]^(1/6) E^(-a4[H x4]), Sin[6 H x0]^(1/6) E^(-a4[H x4])}];
  geoS = D16GeoSymbolicGeometry[frameX, coordsX];
  okGeo = AllTrue[Flatten[geoS["Omega"] - OmF], zeroXQ] && AllTrue[Flatten[geoS["curvedGammas"] - gUF], zeroXQ] && C16P === Cm && pp["gamL"] === gam;
  addCheck["C00_primordial_geometryMatchesStage2", okGeo];
  (* Euler-Lagrange equations for COMMUTING component functions Psi_n(x0..x7) derived from (L1) *)
  psi = Table[Ps[n] @@ Yv, {n, 0, 15}]; psib = Table[Pb[n] @@ Yv, {n, 0, 15}];
  S0 = psib.C16P.psi;
  Dpsi = Table[d1[mu, psi] + OmF[[mu]].psi, {mu, 8}];
  Dpsib = Table[d1[mu, psib.C16P] - psib.C16P.OmF[[mu]], {mu, 8}];
  Lag = sqrtgF ((1/2) Sum[psib.C16P.gUF[[mu]].Dpsi[[mu]] - Dpsib[[mu]].gUF[[mu]].psi, {mu, 8}] - mmP S0 - (lamP/2) S0^2);
  ELb = Table[D[Lag, Pb[a] @@ Yv] - Sum[D[D[Lag, D[Pb[a] @@ Yv, Yv[[k]]]], Yv[[k]]], {k, 8}], {a, 0, 15}];
  tgtb = sqrtgF C16P.(elOp[psi, mmP + lamP S0]);
  ELp = Table[D[Lag, Ps[a] @@ Yv] - Sum[D[D[Lag, D[Ps[a] @@ Yv, Yv[[k]]]], Yv[[k]]], {k, 8}], {a, 0, 15}];
  tgtp = -sqrtgF (Sum[Dpsib[[mu]].gUF[[mu]], {mu, 8}] + (mmP + lamP S0) psib.C16P);
  okEL = AllTrue[Range[16], zeroQP[ELb[[#]] - tgtb[[#]]] &] && AllTrue[Range[16], zeroQP[ELp[[#]] - tgtp[[#]]] &] &&
    AllTrue[Flatten[Sum[gUF[[mu]].OmF[[mu]], {mu, 8}] - 3 H G[0]], zeroQP];
  addCheck["C00_primordial_ELcommuting", okEL];
  addMeas["primordial.EL", "Stage-2 chart (z = 6 H x0, t = H x4, a4(t) arbitrary), 16 COMMUTING component functions Psi_n(x0..x7) and Psi^*_n: the Euler-Lagrange equations of (L1) (U = (lambda/2) S^2) are sqrt|g| C (gamma^mu D_mu Psi - (m + lambda S) Psi) = 0 and -sqrt|g|((D_mu Psibar) gamma^mu + (m + lambda S) Psibar) = 0, i.e. tan z gamma^0 d_0 Psi + s^{-1/6} e^{-a4} gamma^i d_i Psi + gamma^4 d_4 Psi + s^{-1/6} e^{a4} gamma^j d_j Psi + 3 H gamma^0 Psi = (m + lambda S) Psi (i = 1,2,3, j = 5,6,7) with gamma^mu Omega_mu = 3 H gamma^0 (a4-independent): identical to the Stage-2 component equations (DIRAC16COMPLEX_PRIMORDIAL_FIELD Section 7, 16 rows listed there)."];
  (* the x0-independent (homogeneous) state Psi = u(x4): exact classical solution for every U *)
  uv = Table[uu[n][t], {n, 0, 15}]; ubv = Table[ub[n][t], {n, 0, 15}];
  SX = ubv.C16P.uv;
  onX = Join[Table[Derivative[1][uu[n]][t] -> (-(1/H) G[4].(MeffP uv - 3 H G[0].uv))[[n + 1]], {n, 0, 15}],
    Table[Derivative[1][ub[n]][t] -> (-(1/H) G[4].(MeffP ubv - 3 H G[0].ubv))[[n + 1]], {n, 0, 15}]];
  eX = emtLower[uv, ubv, mmP, UsP];
  TlowX = eX["T"] /. onX;
  TmixX = Table[giF[[mu, mu]] TlowX[[mu, nu]], {mu, 8}, {nu, 8}];
  K4 = (1/2) (eX["psibar"].gUF[[5]].eX["Dp"][[5]] - eX["Db"][[5]].gUF[[5]].uv) /. onX;
  KEH = -(1/2) Sum[If[mu == 5, 0, eX["psibar"].gUF[[mu]].eX["Dp"][[mu]] - eX["Db"][[mu]].gUF[[mu]].uv], {mu, 8}] /. onX;
  homRes = <|"solvesExactly" -> (AllTrue[elOp[uv, MeffP] /. onX, zeroQP] && zeroQP[D[SX, t] /. onX]),
    "rho" -> zeroQP[-TmixX[[5, 5]] - (mmP SX + UsP)],
    "pressures" -> AllTrue[{1, 2, 3, 4, 6, 7, 8}, zeroQP[TmixX[[#, #]] - ((MeffP - mmP) SX - UsP)] &],
    "KE_L" -> zeroQP[K4/2 - (1/2) SX MeffP], "PE_L" -> zeroQP[(mmP SX + UsP) - K4/2 - (1/2) (mmP SX + 2 UsP - SX (MeffP - mmP))],
    "KE_H" -> zeroQP[KEH], "rhoEqualsKEHplusPEH" -> zeroQP[-TmixX[[5, 5]] - KEH - (mmP SX + UsP)]|>;
  okHom = AllTrue[Values[homRes], TrueQ];
  addCheck["C00_primordial_homogeneousState", okHom];
  addMeas["primordial.homogeneous", Join[homRes, <|"statement" -> "x0-independent state Psi = u(x4) in the Stage-2 primordial field with arbitrary a4(t) (the Stage-2 'K = -3iH' state), on shell H du/dt = -gamma^4 (M_eff - 3 H gamma^0) u with M_eff = m + U'(S): S = u^dagger C u is constant, so this is an EXACT classical solution of dirac16complex00 for every U (for dirac16complex the same formulas are the mean-field/c-number reading). With U'(S) := M_eff - m: rho = -T^4_4 = m S + U, p_(i) = T^i_i = S U' - U (all seven transverse directions), KE_L = (1/2) K_4 = (1/2) S (m + U'), PE_L = rho - KE_L = (1/2)(m S + 2 U - S U'), KE_H = 0, PE_H = rho, w = (S U' - U)/(m S + U) (a4-independent)."|>]];
  (* the static member (a4' = a4'' = 0) sourced EXACTLY by a homogeneous commuting state, H = kappa = 1:
     m S = -36, lambda S^2 = 30 (STAGE4_SPEC E4.1): S = 6/5, m = -30, lambda = 125/6, M_eff = -5, omega = 4 *)
  ex = <|"m" -> -30, "lam" -> 125/6, "S" -> 6/5, "Meff" -> -5, "omega" -> 4, "v" -> {1, 3 I, 0, 0, 1, -3 I, 0, 0, -3, -I, 0, 0, -3, I, 0, 0}|>;
  exRes = Module[{v = ex["v"], Am, Sv, u0, psiE, psibE, S1, dirac, eE, TmE, Gst, GmixKS, res},
    Am = -G[4].(ex["Meff"] id16 - 3 G[0]);
    Sv = Conjugate[v].C16P.v;
    u0 = Sqrt[ex["S"]/Sv] v;
    psiE = E^(I ex["omega"] t) u0; psibE = E^(-I ex["omega"] t) Conjugate[u0];
    S1 = Simplify[Expand[psibE.C16P.psiE]];
    dirac = AllTrue[Expand[(elOp[psiE, ex["m"] + ex["lam"] S1] /. H -> 1) E^(-I ex["omega"] t)], TrueQ[Simplify[#] === 0] &];
    eE = emtLower[psiE, psibE, ex["m"], (ex["lam"]/2) S1^2];
    TmE = Table[Simplify[(giF[[mu, mu]] eE["T"][[mu, nu]]) /. H -> 1], {mu, 8}, {nu, 8}];
    (* Einstein tensor of the static field: the Stage-2 closed form at a4' = a4'' = 0 and, independently, the Stage-4 package's G^mu_nu in the y chart *)
    Gst = DiagonalMatrix[{-3 (0 - 5), 15, 15, 15, 3 (7 + 0), 15, 15, 15}];
    kp["buildGeometry"][]; GmixKS = kp["GmixF"] /. kp["H"] -> 1;
    res = <|"eigenvectorOfA" -> (Am.v === I ex["omega"] v), "S" -> S1, "solvesExactly" -> dirac,
      "einsteinStage2EqualsStage4" -> (Together[GmixKS - Gst] === ConstantArray[0, {8, 8}]),
      "einsteinEqualsKappaT64" -> (Simplify[Gst - TmE] === ConstantArray[0, {8, 8}]),
      "rho" -> -TmE[[5, 5]], "p" -> TmE[[1, 1]], "w" -> Together[TmE[[1, 1]]/(-TmE[[5, 5]])],
      "KE_L" -> (1/2) S1 ex["Meff"], "PE_L" -> -TmE[[5, 5]] - (1/2) S1 ex["Meff"]|>;
    res];
  okEx = exRes["eigenvectorOfA"] && exRes["S"] === 6/5 && exRes["solvesExactly"] && exRes["einsteinStage2EqualsStage4"] && exRes["einsteinEqualsKappaT64"] &&
    exRes["rho"] === -21 && exRes["p"] === 15 && exRes["w"] === -5/7 && exRes["KE_L"] === -3 && exRes["PE_L"] === -18;
  addCheck["C00_primordial_staticFieldSourcedExactly", okEx];
  addMeas["primordial.staticSource", Join[exRes, <|"parameters" -> "H = kappa = 1, a4 = constant (the static member), m = -30, lambda = 125/6, S = 6/5, M_eff = m + lambda S = -5, omega = sqrt(M_eff^2 - 9 H^2) = 4",
    "state" -> "Psi = e^{i omega x4} u0, u0 = sqrt(S/(v^dagger C v)) v, v = (1, 3i, 0, 0, 1, -3i, 0, 0, -3, -i, 0, 0, -3, i, 0, 0) (the Stage-2 vector of example B), v^dagger C v = " <> ratStr[Conjugate[ex["v"]].Cm.ex["v"]],
    "statement" -> "for the COMMUTING field this homogeneous state is an exact classical solution whose energy-momentum tensor equals the Einstein tensor of the static primordial field in all 64 components, G^mu_nu = kappa T^mu_nu = diag(15,15,15,15,21,15,15,15) (rho = -21 H^2/kappa, p = +15 H^2/kappa in all seven transverse directions, w = -5/7, KE_L = (1/2) S M_eff = -3, PE_L = -18, KE_H = 0, PE_H = rho): the static field is sourced exactly by dirac16complex00 with m S = -36 H^2/kappa, lambda S^2 = 30 H^2/kappa (STAGE4_SPEC E4.1). For dirac16complex the same numbers are the c-number (mean-field) reading of <Psibar Psi> = S; a positive-energy KS orbital has S > 0 for m > 0 (Stage 4 E4.1), so there the source lives in the m < 0 sector."|>]];
];

(* ========================================================================= *)
(* 12. the Stage-4 static warped form (y chart) and the 2x2 blocks           *)
(* ========================================================================= *)
parseGQ[p_List] := ToExpression[p[[1]]] + I ToExpression[p[[2]]];
checkStaticWarped[root_] := Module[{y = kp["y"], x1 = kp["x1"], x4 = kp["x4"], H = kp["H"], a4c = kp["a4c"], kk = kp["kk"], eps = kp["eps"], ch = kp["ch"], cb = kp["cb"],
    MeffK = kp["Meff"], vvK = kp["vv"], mK = kp["m"], zeroQK = kp["zeroQ"], d1 = kp["d1"], Yv = kp["Yv"], emtK = kp["emtLower"], G = kp["G"], Vint, BmK, C16K, gUF, OmF, giF,
    geoS, okGeo, chi, Psi, dirac, red, target, okAns, th, blocksJ, Vjson, okBasis, okBlocks, labels, perBlock, okKrein, box, okBox, ks, okKS, diagB, okN},
  kp["buildGeometry"][]; kp["buildBlockBasis"][];
  Vint = kp["Vint"]; BmK = kp["Bm"]; C16K = kp["C16"]; gUF = kp["gUF"]; OmF = kp["OmF"]; giF = kp["giF"]; diagB = kp["diagBlocks"];
  geoS = D16GeoSymbolicGeometry[DiagonalMatrix[kp["hhF"]], Yv];
  okGeo = AllTrue[Flatten[geoS["Omega"] - OmF], zeroQK] && AllTrue[Flatten[geoS["curvedGammas"] - gUF], zeroQK] && C16K === Cm && kp["gamL"] === gam;
  (* reduced equation: the ansatz W^{-3} removes gamma^mu Omega_mu = 3 H gamma^0 (commuting component functions) *)
  chi = Table[ch[n][y], {n, 0, 15}];
  Psi = E^(-I eps x4) E^(I kk x1) E^(-3 H y) chi;
  dirac = Sum[gUF[[mu]].(d1[mu, Psi] + OmF[[mu]].Psi), {mu, 8}] - MeffK[y] Psi;
  red = Expand[E^(I eps x4) E^(-I kk x1) E^(3 H y) dirac];
  target = G[0].D[chi, y] + I kk E^(-H y - a4c) G[1].chi - I eps G[4].chi - MeffK[y] chi;
  okAns = AllTrue[red - target, zeroQK] && AllTrue[Flatten[Sum[gUF[[mu]].OmF[[mu]], {mu, 8}] - 3 H G[0]], zeroQK];
  addCheck["C00_static_geometryAndReducedEquation", okGeo && okAns];
  addMeas["static.reducedEquation", "static warped chart ds^2 = dy^2 - dx4^2 + e^{2Hy}[e^{2a4}dx_{123}^2 - e^{-2a4}dx_{567}^2] (Stage 4, geometry rebuilt with D16GeoSymbolicGeometry and equal to the Stage-4 package): for commuting components the ansatz Psi = e^{-i eps x4} e^{i k x1} W^{-3} chi(y), W = e^{Hy}, removes gamma^mu Omega_mu = 3 H gamma^0 exactly and gives gamma^0 chi' + i kappa(y) k gamma^1 chi - i eps gamma^4 chi = M_eff chi, kappa = e^{-Hy-a4} (the Stage-4 reduced equation; linear in Psi, statistics-independent)."];
  (* the eight 2x2 blocks from kohn-sham-theory.json *)
  th = Import[FileNameJoin[{root, "artifacts", "dirac16complex", "kohn-sham", "kohn-sham-theory.json"}], "RawJSON"];
  blocksJ = th["reduction"]["blockDiagonalisation"]["blocks"];
  Vjson = Map[parseGQ, th["reduction"]["blockDiagonalisation"]["basisMatrixUnnormalised"], {2}];
  okBasis = Vjson === Vint && Together[ConjugateTranspose[Vjson].Vjson/8] === id16;
  okBlocks = AllTrue[Range[8], Module[{bj = blocksJ[[#]], i = #},
      And @@ MapThread[Function[{key, M16}, Map[parseGQ, bj[key], {2}] === Together[ConjugateTranspose[Vjson[[All, 2 i - 1 ;; 2 i]]].M16.Vjson[[All, 2 i - 1 ;; 2 i]]/8]],
        {{"A0", "A1", "A4", "B", "C", "BC"}, {gam[[1]], gam[[1]].gam[[2]], gam[[1]].gam[[5]], Bm, Cm, Bm.Cm}}] &&
      ToExpression[bj["Beigenvalue"]] === ToExpression[bj["j"]] ToExpression[bj["s2"]]] &] && Length[blocksJ] === 8;
  labels = Table[{ToExpression[b["j"]], ToExpression[b["s2"]], ToExpression[b["s3"]]}, {b, blocksJ}];
  (* the reduced 16-component equation chi' = N chi is block diagonal with the Stage-4 2x2 matrices N_j = Meff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1 *)
  okN = kp["blockDiagQ"][kp["Nfull"]] && AllTrue[Range[8], kp["zeroMatQ"][kp["diagBlocks"][kp["Nfull"]][[#]] - kp["Nblock"][labels[[#, 1]]]] &] &&
    labels === kp["blockLabels"];
  addCheck["C00_static_blocksFromStage4Theory", okBasis && okBlocks && okN && Sort[Times @@@ labels[[All, 1 ;; 2]]] === {-1, -1, -1, -1, 1, 1, 1, 1}];
  (* classical commuting mode versus the Stage-4 Kohn-Sham orbital (expectation rule Psi^dagger -> u^dagger B), per block, off shell *)
  perBlock = Table[Module[{j = labels[[i, 1]], s2 = labels[[i, 2]], v1 = Vint[[All, 2 i - 1]], v2 = Vint[[All, 2 i]], chiB, chibB, PsiB, PsidCl, PsidKS, Tcl, TKS, rel, K4cl, K4ks},
      chiB = v1 ch[0][y] + v2 ch[1][y]; chibB = Conjugate[v1] cb[0][y] + Conjugate[v2] cb[1][y];
      PsiB = E^(-I eps x4) E^(I kk x1) E^(-3 H y) chiB;
      PsidCl = E^(I eps x4) E^(-I kk x1) E^(-3 H y) chibB; PsidKS = E^(I eps x4) E^(-I kk x1) E^(-3 H y) (chibB.BmK);
      Tcl = emtK[PsiB, PsidCl, mK]; TKS = emtK[PsiB, PsidKS, mK];
      rel = AllTrue[Flatten[Tcl["T"] - j s2 TKS["T"]], zeroQK] && ! AllTrue[Flatten[TKS["T"]], zeroQK];
      K4cl = E^(6 H y) (1/2) (Tcl["psibar"].gUF[[5]].Tcl["Dp"][[5]] - Tcl["Db"][[5]].gUF[[5]].PsiB);
      K4ks = E^(6 H y) (1/2) (TKS["psibar"].gUF[[5]].TKS["Dp"][[5]] - TKS["Db"][[5]].gUF[[5]].PsiB);
      <|"block" -> i - 1, "j" -> j, "s2" -> s2, "kreinSign" -> j s2, "classicalEqualsKreinSignTimesKS64" -> rel,
        "K4_KS_equals_eps_n" -> zeroQK[K4ks - 8 eps (cb[0][y] ch[0][y] + cb[1][y] ch[1][y])], "K4_classical_equals_kreinSign_eps_n" -> zeroQK[K4cl - j s2 8 eps (cb[0][y] ch[0][y] + cb[1][y] ch[1][y])]|>], {i, 8}];
  okKrein = AllTrue[perBlock, #["classicalEqualsKreinSignTimesKS64"] && #["K4_KS_equals_eps_n"] && #["K4_classical_equals_kreinSign_eps_n"] &];
  addCheck["C00_static_classicalModeIsKreinWeightedKS", okKrein];
  (* an explicit free box mode (k = 0, M_eff = m = 3, v_v = 0, eps = 5, chi_2 = sin 4y, chi_1 = (3 sin 4y + 4 cos 4y)/(i j 5)) in a block of each Krein sign *)
  box = Table[Module[{i = ib, j = labels[[ib, 1]], s2 = labels[[ib, 2]], c1, c2, chiB, chibB, PsiB, Psid, Tcl, rho, n16, ode},
      c2 = Sin[4 y]; c1 = (3 Sin[4 y] + 4 Cos[4 y])/(I j 5);
      ode = Simplify[D[{c1, c2}, y] - (3 kp["sig3"] + I j 5 kp["sig1"]).{c1, c2}] === {0, 0};
      chiB = Vint[[All, 2 i - 1]] c1 + Vint[[All, 2 i]] c2; chibB = ComplexExpand[Conjugate[chiB]];
      (* the full 16-component reduced equation gamma^0 chi' - i eps gamma^4 chi = M chi (k = 0) *)
      ode = ode && Simplify[G[0].D[chiB, y] - I 5 G[4].chiB - 3 chiB] === ConstantArray[0, 16];
      PsiB = E^(-I 5 x4) E^(-3 H y) chiB; Psid = E^(I 5 x4) E^(-3 H y) chibB;
      Tcl = emtK[PsiB, Psid, 3];
      rho = Simplify[-E^(6 H y) giF[[5, 5]] Tcl["T"][[5, 5]]];
      n16 = Simplify[ComplexExpand[chibB.chiB]];
      <|"block" -> i - 1, "kreinSign" -> j s2, "odeAndBoundary" -> (ode && (c2 /. y -> 0) === 0 && (c2 /. y -> -Pi/4) === 0),
        "rhoTimesW6" -> toStr[rho], "rhoEqualsKreinSignTimesEpsN" -> (Simplify[rho - j s2 5 n16] === 0), "sign" -> j s2|>], {ib, {First[Flatten[Position[Times @@@ labels[[All, 1 ;; 2]], 1]]], First[Flatten[Position[Times @@@ labels[[All, 1 ;; 2]], -1]]]}}];
  okBox = AllTrue[box, #["odeAndBoundary"] && #["rhoEqualsKreinSignTimesEpsN"] &] && Sort[#["sign"] & /@ box] === {-1, 1};
  addCheck["C00_static_classicalEnergyKreinSigned", okBox];
  (* Kohn-Sham orbital (both fields in the Stage-4 treatment): rho = T_44 = -K_perp + m s off shell (one-body part) *)
  ks = Module[{PsiG = E^(-I eps x4) E^(I kk x1) E^(-3 H y) chi, PsidG, e8, Kperp, sS},
    PsidG = E^(I eps x4) E^(-I kk x1) E^(-3 H y) (Table[cb[n][y], {n, 0, 15}].BmK);
    e8 = emtK[PsiG, PsidG, mK];
    Kperp = (1/2) Sum[If[mu == 5, 0, e8["psibar"].gUF[[mu]].e8["Dp"][[mu]] - e8["Db"][[mu]].gUF[[mu]].PsiG], {mu, 8}];
    sS = e8["psibar"].PsiG;
    zeroQK[-giF[[5, 5]] e8["T"][[5, 5]] - (-Kperp + mK sS)]];
  addCheck["C00_static_KSorbitalEnergySplit", TrueQ[ks]];
  addMeas["static.blocksAndModes", <|"blocks" -> perBlock, "boxModes" -> box,
    "statement" -> "the Stage-4 block basis and the 2x2 blocks A0 = gamma^0, A1 = gamma^0 gamma^1, A4 = gamma^0 gamma^4, B, C, BC read from kohn-sham-theory.json are reproduced exactly (V^dagger M V / 8 with the unnormalised Gaussian-integer basis) and the reduced equation chi' = N chi is block diagonal with N_j = M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1 in every block; B = j s2 on block (j, s2, s3): four blocks with Krein sign +1 and four with -1. For a CLASSICAL commuting mode in block beta (Psi = e^{-i eps x4} e^{i k x1} W^{-3} chi, chi in block beta, bilinears Psi^dagger X Psi) every component of T_{mu nu} equals (j s2)_beta times the Stage-4 Kohn-Sham one-body value (expectation rule Psi^dagger -> u^dagger B), identically off shell (64 components, 8 blocks); K_4 = (j s2) eps n classically and eps n for the KS orbital (n = chi^dagger chi e^{-6Hy}/l^3 per unit transverse volume). Explicit free box modes (k = 0, M = m = 3, eps = +5, chi_2(0) = chi_2(-pi/4) = 0) have classical energy density rho e^{6Hy} = (j s2) 5 |chi|^2: positive in blocks with j s2 = +1, NEGATIVE in blocks with j s2 = -1 - the classical energy of dirac16complex00 is also unbounded below in the static primordial field. For the Kohn-Sham orbital (both fields in the Stage-4 treatment) rho = T_44 = -K_perp + m s off shell (KE_H = -K_perp, PE_H = m s + <U>), KE_L = (1/2) eps n.",
    "meanFieldEMT" -> "one-body KS-orbital EMT (Stage 4, statistics-independent): rho^(1) = eps n - (M_eff - m) s - v_v n, p_y^(1) = eps n - m s - kappa k t, p_(1)^(1) = kappa k t + (M_eff - m) s + v_v n, p_(2,3)^(1) = p_(5,6,7)^(1) = (M_eff - m) s + v_v n; the interaction enters as rho = sum_n f_n rho^(1)_n + <U>, p_(i) = sum_n f_n p^(1)_(i),n - <U> (all seven transverse directions); <U> = (lambda/2)[Tr(M rho)^2 -+ Tr(M rho M rho)] with the upper sign for dirac16complex and the lower for dirac16complex00 (STAGE5_SPEC section 4; derived and verified in the pairing module, not here)."|>];
];

(* ========================================================================= *)
(* 13. G4: a generic non-diagonal unimodular integer frame jet               *)
(* ========================================================================= *)
(* e(x) = E0 + x^l E1_l + (1/2) x^l x^k E2_lk at x = 0, E0 = U.L (U, L unitriangular with entries in {-1, 0, 1}, det E0 = 1, so
   g = E0 eta E0^T is an integer matrix of signature (4,4) with integer inverse); E1_l, E2_lk (symmetric in l, k) integer matrices
   with entries in {-1, 0, 1}.  All entries from the 64-bit LCG: v = (numerator of D16GeoRandomRationals) mod 3 - 1. *)
g4Ints[s_, n_] := (Mod[Numerator[#], 3] - 1) & /@ rr[s, n];
g4Jet[k_] := Module[{U, L, E0, E1, E2, r2, c = 0},
  U = id8 + UpperTriangularize[Partition[g4Ints[64000 + 10 k, 64], 8], 1];
  L = id8 + LowerTriangularize[Partition[g4Ints[64001 + 10 k, 64], 8], -1];
  E0 = U.L;
  E1 = Partition[Partition[g4Ints[64002 + 10 k, 512], 8], 8];
  r2 = Partition[Partition[g4Ints[64003 + 10 k, 36*64], 8], 8];
  E2 = ConstantArray[0, {8, 8, 8, 8}];
  Do[c++; E2[[l, kk]] = r2[[c]]; E2[[kk, l]] = r2[[c]], {l, 8}, {kk, l, 8}];
  {E0, E1, E2}];
geoAt["G4", k_, curv_: True] := Module[{fj = g4Jet[k], geo},
  D16GeoSetAlgebraic[None];
  geo = D16GeoJetGeometry[fj, "Curvature" -> curv];
  <|"fj" -> fj, "geo" -> geo, "alg" -> {}, "label" -> "G4p" <> ToString[k], "H" -> Missing[]|>];
checkG4[g_] := Module[{e0 = g["fj"][[1]], gm, inert, x, cl, sc},
  gm = e0.eta.Transpose[e0];
  (* exact signature: the characteristic polynomial of the real symmetric integer matrix g has only real roots, so Descartes' rule
     counts the positive roots exactly (and the negative ones via x -> -x); no zero root since det g = 1 *)
  cl = CoefficientList[CharacteristicPolynomial[gm, x], x];
  sc[l_] := Count[Partition[Sign[Select[l, # =!= 0 &]], 2, 1], {a_, b_} /; a b < 0];
  inert = {sc[cl], sc[MapIndexed[#1 (-1)^(#2[[1]] - 1) &, cl]]};
  addCheck["C00_geometry_G4Generic", Det[e0] === 1 && Det[gm] === 1 && AllTrue[Flatten[Inverse[gm]], IntegerQ] && Count[Flatten[e0 - DiagonalMatrix[Diagonal[e0]]], v_ /; v =!= 0] > 20 &&
    ! zq[g["geo"]["ginv"][[1, 5, 5]]] && ! zq[g["geo"]["scalarCurvature"]] && inert === {4, 4}];
  addMeas["geometry.G4", <|"E0" -> e0, "nonzeroOffDiagonalOfE0" -> Count[Flatten[e0 - DiagonalMatrix[Diagonal[e0]]], v_ /; v =!= 0],
    "gUpper44" -> ratStr[g["geo"]["ginv"][[1, 5, 5]]], "scalarCurvature" -> ratStr[g["geo"]["scalarCurvature"]],
    "definition" -> "e(x) = E0 + x^l E1_l + (1/2) x^l x^k E2_lk at x = 0; E0 = U.L with U, L unitriangular, entries in {-1,0,1}; E1_l, E2_lk (symmetric) entries in {-1,0,1}; values v = (Numerator[D16GeoRandomRationals[seed, n]] mod 3) - 1 with seeds 64000+10k (U), 64001+10k (L), 64002+10k (E1, 512 values, l-major), 64003+10k (E2, 36 matrices for l <= k in row order)"|>];
];

(* ========================================================================= *)
(* 14. citations of the Stage 1-4 reports (checked against the current sources) *)
(* ========================================================================= *)
sha[root_, rel_] := ToLowerCase[FileHash[FileNameJoin[Prepend[FileNameSplit[rel], root]], "SHA256", All, "HexString"]];
checkCitations[root_] := Module[{rep, geoRep, algRep, priRep, ksRep, ksTh, need, ok, detail = <||>, cite},
  rep[rel_] := Import[FileNameJoin[Prepend[FileNameSplit[rel], root]], "RawJSON"];
  cite[name_, r_, srcKey_, keys_] := Module[{hashOK = r["sourceSha256"][srcKey] === sha[root, srcKey], vals = Lookup[r["checks"], keys, Missing[]]},
    detail[name] = <|"source" -> srcKey, "sourceHashMatchesReport" -> hashOK, "checks" -> AssociationThread[keys, vals]|>;
    hashOK && AllTrue[vals, TrueQ]];
  geoRep = rep["artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json"];
  algRep = rep["artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json"];
  priRep = rep["artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json"];
  ksRep = rep["artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json"];
  ksTh = rep["artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json"];
  ok = cite["stage1Geometry", geoRep, "wolfram/Dirac16ComplexGeometry.wl", {"LAG_hermiticity_G1", "LAG_hermiticity_G2", "LAG_eulerLagrangePsibar_G1", "LAG_eulerLagrangePsibar_G2",
       "LAG_eulerLagrangePsi_G1", "LAG_eulerLagrangePsi_G2", "LAG_notebookLgGrassmannTrivial_G1", "LAG_notebookLgGrassmannTrivial_G2", "LAG_localSpinInvariance_G1",
       "LAG_localSpinInvariance_G2", "EMT_conservation_G1", "EMT_conservation_G2", "EMT_trace_G1", "EMT_trace_G2", "EMT_variation_G3", "EMT_homogeneousReduction_G3",
       "EMT_symmetricHermitian_G1", "EMT_symmetricHermitian_G2", "QNT_canonicalMomentum_G1", "QNT_canonicalMomentum_G2"}] &&
    cite["stage1Algebra", algRep, "wolfram/Dirac16ComplexAlgebra.wl", {"ALG_gamma8Map", "ALG_pinLiftCharacter", "ALG_invariantForms", "ALG_chargeFormB", "QNT_kreinSignature",
       "QNT_flatModeHamiltonian", "ALG_pinIrreducibleComplex", "ALG_spinDecomposition"}] &&
    cite["stage2Primordial", priRep, "wolfram/Dirac16ComplexPrimordial.wl", {"P_EL_fromLagrangianPsiDagger", "P_EL_fromLagrangianPsi", "P_source_x0IndependentExactExamples",
       "P_source_x0IndependentDiagonalOnShell", "P_quant_gamma8MapsMtoMinusM", "P_quant_gamma8LagrangianSign"}] &&
    cite["stage4KohnSham", ksRep, "wolfram/Dirac16ComplexKohnSham.wl", {"KS_reduction_ansatzRemoves3H", "KS_reduction_blocksBC", "KS_emt_rho", "KS_boundary_parityA_symmetryIffMassOdd"}] &&
    ksTh["sourceSha256"]["wolfram/Dirac16ComplexKohnSham.wl"] === sha[root, "wolfram/Dirac16ComplexKohnSham.wl"];
  addCheck["C00_citation_stage1to4ReportsMatchSources", ok];
  addMeas["citations", Join[detail, <|"kohnShamTheoryJsonSource" -> ksTh["sourceSha256"]["wolfram/Dirac16ComplexKohnSham.wl"],
    "statement" -> "the Grassmann-side statements cited here (Stage 1: Hermiticity, Euler-Lagrange equations with left/right derivatives, the notebook Lg[] is a pure divergence, local spin invariance, EMT conservation/trace/variation, canonical momentum and the Krein anticommutator; Stage 1 algebra: gamma^8 map, Pin characters, invariant forms, B; Stage 2: the primordial-field EL equations and the exact homogeneous source examples; Stage 4: the reduction and blocks) are true in the committed reports, and each report's recorded SHA-256 of its source equals the SHA-256 of the file in the repository now."|>]];
];

(* ========================================================================= *)
(* 15. driver and the exported theory                                        *)
(* ========================================================================= *)
D16C00Run[root_String] := Module[{t0 = AbsoluteTime[], step, g1s, g2s, g4, g3, res, th},
  $checks = <||>; $meas = <||>; $theory = <||>;
  step[name_, body_] := (logT[name]; body);
  SetAttributes[step, HoldRest];
  res = Catch[Catch[
    step["fixture and algebra", checkFixture[root]; checkLeadFacts[]; checkAnticommutatorStructure[]; checkPinModule[]];
    step["flat: Grassmann algebra, commuting polynomials, mass term, dispersion", checkGrassmannFlat[]; checkCommutingFlat[]; checkMassTermCommuting[]];
    step["test geometries G1 (3 points), G2 (3 points), G4", g1s = Table[geoAt["G1", k], {k, 3}]; g2s = Table[geoAt["G2", k], {k, 3}]; g4 = geoAt["G4", 1]; checkG4[g4]];
    step["Euler-Lagrange equations (commuting, curved)", checkELCommuting[Join[g1s, g2s]]];
    step["reality", checkRealityAll[{g1s[[1]], g2s[[1]], g2s[[2]], g2s[[3]]}]];
    step["real restriction", checkRealRestriction[Join[g1s, {g2s[[1]]}], g1s[[1]]]];
    step["spin connection and gravity", checkConnection[Join[g1s, g2s, {g4}]]];
    step["EMT: vielbein variation (G1p1, G4p1, G3t1)", g3 = geoAt["G3", 1, False]; checkVielbeinVariation[{g1s[[1]], g4, g3}]];
    step["EMT: symmetry, reality, conservation, trace, current, general U", checkEMT[Join[g1s, g2s]]];
    step["EMT: homogeneous equations of state (G3)", checkHomogeneous[]];
    step["commuting field: charge and energy", checkChargeIndefinite[g2s[[1]]]; checkEnergyUnbounded[]];
    step["primordial field (Stage-2 chart)", checkPrimordialStage2[]];
    step["static warped form and 2x2 blocks (Stage 4)", checkStaticWarped[root]];
    step["citations", checkCitations[root]];
    "ok"], _, Function[{v, tag}, {"thrown", tag, v}]];
  If[res =!= "ok", Print["INTERNAL ERROR: ", Short[res, 5]]; addCheck["C00_internal_noException", False], addCheck["C00_internal_noException", True]];
  (* combined statements *)
  addCheck["C00_EL_identicalFormBothStatistics", TrueQ[$checks["C00_EL_commutingCurved"]] && TrueQ[$checks["C00_EL_commutingFlat"]] &&
    TrueQ[$checks["C00_lagrangian_grassmannFlatHermitianAndEL"]] && TrueQ[$checks["C00_citation_stage1to4ReportsMatchSources"]]];
  addMeas["EL.identicalForm", "commuting components (this verifier: C00_EL_commutingCurved at G1 p1-p3 and G2 p1-p3, C00_EL_commutingFlat) and Grassmann components (C00_lagrangian_grassmannFlatHermitianAndEL here; Stage 1 LAG_eulerLagrangePsibar/Psi at six curved points, cited) give the same field equations gamma^mu D_mu Psi = (m + U'(S)) Psi, (D_mu Psibar) gamma^mu = -(m + U'(S)) Psibar: for commuting variables the variation of a product has no signs; for Grassmann variables the left derivative (Psi^dagger) and the right derivative (Psi) absorb them."];
  $theory = buildTheory[root];
  logT["done in ", Round[AbsoluteTime[] - t0], " s"];
  <|"checks" -> $checks, "measurements" -> $meas, "theory" -> $theory|>];

buildTheory[root_] := Module[{pw = Lookup[$meas, "energy.unboundedBelow", <||>], st = Lookup[$meas, "primordial.staticSource", <||>], blocks = Lookup[Lookup[$meas, "static.blocksAndModes", <||>], "blocks", {}]},
  <|
  "conventions" -> <|"indices" -> "zero-based: x = {x0..x7}, x4 = time, frame indices a = 0..7, spinor indices 0..15",
    "metric" -> "eta = diag(+1,+1,+1,+1,-1,-1,-1,-1)", "gammas" -> "gamma^a = notebook T16^A[a] (artifacts/dirac16complex/arbitrary-field/algebra-fixture.json)",
    "adjoint" -> "C = sigma16 = gamma^0 gamma^1 gamma^2 gamma^3, Psibar = Psi^dagger C, B = -i C gamma^4, gamma^8 = gamma^0...gamma^7 = diag(-I8, +I8)",
    "connection" -> "Omega_mu = (1/2) omega_{mu ab} S^{ab} = (1/8) omega_{mu ab}[gamma^a, gamma^b], omega_{mu ab} = eta_{ac} omega_mu^c_b, D_mu Psi = d_mu Psi + Omega_mu Psi, D_mu Psibar = d_mu Psibar - Psibar Omega_mu",
    "emtSign" -> "T_{mu nu} = -(2/sqrt|g|) delta S/delta g^{mu nu}; rho = T_44 (Gaussian normal x4), p_(i) = T^i_i (no sum), T^4_4 = -rho",
    "matrixEntryFormat" -> "complex entries as [re, im] rational strings; real entries as rational strings"|>,
  "fields" -> <|"dirac16complex" -> "Psi: M^8 -> C^16 with Grassmann-odd (anticommuting) components; the second-quantized field of Stages 1-4 (canonical anticommutator {Psi, Psi^dagger} = B delta^7/sqrt|g| at equal x4)",
    "dirac16complex00" -> "Psi: M^8 -> C^16 with COMMUTING complex (c-number) components; the 16 components transform together as the irreducible complex Pin(4,4) spinor (Clifford module C^16, commutant 1), Psi -> R Psi under local Spin(4,4), Psi -> u Psi under Pin(4,4) unit vectors; the classical analogue of Dirac's 4-component wave function",
    "difference" -> "only the statistics of the components: the Lagrangian, field equations, EMT and current are the same formulas; statistics enters (i) the admissible potentials (any smooth U for dirac16complex00, polynomials in S for dirac16complex since S^17 = 0), (ii) the real restriction (non-trivial for commuting, a pure divergence for Grassmann components), (iii) the meaning of the EMT (c-number field versus normal-ordered operator), (iv) positivity: the commuting field's charge and energy are indefinite; the quantized Grassmann field has a positive normal-ordered Hamiltonian in the good sector (Stage 1 Section 10.7), (v) the Wick contraction of the interaction in a quasi-free state (pairing module)."|>,
  "lagrangian" -> <|"tex" -> "\\mathcal L=\\sqrt{|g|}\\Bigl[\\tfrac12\\bigl(\\bar\\Psi\\gamma^\\mu D_\\mu\\Psi-(D_\\mu\\bar\\Psi)\\gamma^\\mu\\Psi\\bigr)-m\\,\\bar\\Psi\\Psi-U(\\bar\\Psi\\Psi)\\Bigr]",
    "massTerm" -> "L_m = -m sqrt|g| Psibar Psi: linear in m, bilinear (quadratic) in the components; nonzero: Psibar Psi = -2, +2, 0 on e_0+e_4, e_8+e_12, e_0+i e_4 (commuting), a nonzero element with 16 monomials (Grassmann)",
    "potential" -> "U(S), S = Psibar Psi; default U = (lambda/2) S^2 for both fields; for dirac16complex00 any smooth U (checks with abstract U(S0), U'(S0), U''(S0))",
    "reality" -> "L real for commuting components (Im L = 0 exactly) and Hermitian for Grassmann components; common reason: K0 Hermitian, K^mu = (1/2) sqrt|g| C gamma^mu, L^mu = (K^mu)^dagger",
    "dispersion" -> "flat: k_4^2 + k_5^2 + k_6^2 + k_7^2 - k_0^2 - k_1^2 - k_2^2 - k_3^2 = m^2; curved (U = 0): (gamma^mu D_mu)^2 Psi = m^2 Psi, Box Psi - (R/4) Psi = m^2 Psi"|>,
  "realRestriction" -> <|"notebookLagrangian" -> "Lg = sqrt|g| [Psi^T sigma16 T16^a D_a Psi + (H M) Psi^T sigma16 Psi]",
    "commuting" -> "non-trivial: Euler-Lagrange expression 2 sqrt|g| C (gamma^mu D_mu Psi + H M Psi) (canonical connection), i.e. the Dirac equation with m = -H M; with the notebook contraction an extra sqrt|g| C {gamma^mu, Omega^nb_mu - Omega_mu} Psi (zero for diagonal vielbeins)",
    "grassmann" -> "trivial: Psi^T C Psi = 0 identically, the Lagrangian is a total divergence, Euler-Lagrange expressions vanish identically (Stage 1 Theorem 6.1)",
    "relationToL1" -> "commuting Psi = X + i Y: L1 = sqrt|g| [K_R[X] + K_R[Y] - m (S_X + S_Y) - U(S_X + S_Y)], K_R[Z] = Z^T C gamma^mu D_mu Z; U = 0: L1 = Lg[X] + Lg[Y] with H M = -m; Y = 0 consistent truncation; for Grassmann Psi = rho + i iota: Psibar Psi = 2 i rho^T C iota (pure cross term)"|>,
  "fieldEquations" -> <|"tex" -> "\\gamma^\\mu D_\\mu\\Psi=\\bigl(m+U'(S)\\bigr)\\Psi,\\qquad (D_\\mu\\bar\\Psi)\\gamma^\\mu=-\\bigl(m+U'(S)\\bigr)\\bar\\Psi",
    "EL" -> "dL/dPsi^* - d_mu dL/d(d_mu Psi^*) = sqrt|g| C (gamma^mu D_mu Psi - (m + U'(S)) Psi); dL/dPsi - d_mu dL/d(d_mu Psi) = -sqrt|g| ((D_mu Psibar) gamma^mu + (m + U'(S)) Psibar) (commuting); the same with left/right Grassmann derivatives (Stage 1)",
    "primordialComponents" -> "tan z gamma^0 d_0 Psi + s^{-1/6} e^{-a4} gamma^i d_i Psi + gamma^4 d_4 Psi + s^{-1/6} e^{a4} gamma^j d_j Psi + 3 H gamma^0 Psi = (m + U'(S)) Psi",
    "staticReduced" -> "Psi = e^{-i eps x4} e^{i k x1} e^{-3Hy} chi(y): gamma^0 chi' + i kappa(y) k gamma^1 chi - i eps gamma^4 chi = M_eff chi; per block chi' = [M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1] chi"|>,
  "emt" -> <|"tex" -> "T_{\\mu\\nu}=-\\tfrac14\\bigl[\\bar\\Psi\\gamma_\\mu D_\\nu\\Psi+\\bar\\Psi\\gamma_\\nu D_\\mu\\Psi-(D_\\mu\\bar\\Psi)\\gamma_\\nu\\Psi-(D_\\nu\\bar\\Psi)\\gamma_\\mu\\Psi\\bigr]+g_{\\mu\\nu}\\mathcal L_s",
    "vielbeinVariation" -> "sym part of delta S/delta e_mu^a e^{a nu} = sqrt|g| T^{mu nu} off shell (all components, general non-diagonal frames G1, G4 and Bianchi-I G3); antisymmetric (local Lorentz) part zero on shell",
    "trace" -> "T^mu_mu = -m S + 7 S U'(S) - 8 U(S) on shell", "conservation" -> "nabla^mu T_{mu nu} = 0 on shell (any smooth U)",
    "current" -> "j^mu = Psibar gamma^mu Psi (imaginary for commuting Psi), J^mu = -i j^mu real, d_mu(sqrt|g| j^mu) = 0 on shell; J^4 = Psi^dagger B Psi in Gaussian normal gauge",
    "operatorVersion" -> "for dirac16complex T_{mu nu} is the same expression in the Grassmann field operators, normal ordered with respect to the free Krein vacuum (Stage 1)"|>,
  "energySplits" -> <|"KE_L" -> "(1/2) K_4, K_4 = (1/2)(Psibar gamma^{x4} D_4 Psi - (D_4 Psibar) gamma^{x4} Psi)", "PE_L" -> "rho - KE_L",
    "KE_H" -> "-K_perp, K_perp = (1/2) sum_{mu != 4} (Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi)", "PE_H" -> "m S + U(S)",
    "identity" -> "rho = T_44 = KE_H + PE_H = K_4 - L_s (Gaussian normal time, off shell)",
    "homogeneous" -> "rho = m S + U, p_(i) = S U' - U (all seven transverse directions), KE_L = (1/2) S (m + U'), PE_L = (1/2)(m S + 2U - S U'), KE_H = 0, PE_H = rho, w = (S U' - U)/(m S + U) = (KE_L - PE_L)/(KE_L + PE_L)",
    "freeAndDefault" -> "U = 0: w = 0 (dust); U = (lambda/2) S^2: rho = m S + (lambda/2) S^2, p = (lambda/2) S^2, w = lambda S/(2m + lambda S)"|>,
  "commutingFieldSpecifics" -> <|"Cgamma4EqualsIB" -> True, "B" -> gqMat[Bm], "C" -> ratMat[Cm], "gamma8" -> ratMat[chi8],
    "chargeIndefinite" -> Lookup[$meas, "charge.indefinite", <||>],
    "energyUnboundedBelow" -> KeyDrop[pw, {"statement"}], "energyStatement" -> Lookup[pw, "statement", ""]|>,
  "primordial" -> <|"stage2Homogeneous" -> Lookup[$meas, "primordial.homogeneous", <||>],
    "staticSourceExample" -> <|"H" -> 1, "kappa" -> 1, "m" -> -30, "lambda" -> "125/6", "S" -> "6/5", "Meff" -> -5, "omega" -> 4,
      "v" -> gqVec[{1, 3 I, 0, 0, 1, -3 I, 0, 0, -3, -I, 0, 0, -3, I, 0, 0}], "vDaggerCv" -> 32, "u0" -> "sqrt(S/(v^dagger C v)) v = sqrt(3/80) v",
      "rho" -> Lookup[st, "rho", Missing[]], "p" -> Lookup[st, "p", Missing[]], "w" -> Lookup[st, "w", Missing[]], "KE_L" -> Lookup[st, "KE_L", Missing[]], "PE_L" -> Lookup[st, "PE_L", Missing[]],
      "einstein" -> "G^mu_nu = diag(15,15,15,15,21,15,15,15) H^2 (coordinate order x0 or y, x1, x2, x3, x4, x5, x6, x7)"|>|>,
  "static" -> <|"blockKreinSigns" -> ((KeyTake[#, {"block", "j", "s2", "kreinSign"}]) & /@ blocks),
    "classicalVersusKohnSham" -> "for a single-block mode: T_{mu nu}^{classical} = (j s2) T_{mu nu}^{KS one-body} identically (Psi^dagger versus the expectation rule u^dagger B); K_4 = (j s2) eps n classically, eps n for the KS orbital",
    "boxModes" -> Lookup[Lookup[$meas, "static.blocksAndModes", <||>], "boxModes", {}],
    "meanFieldEMT" -> Lookup[Lookup[$meas, "static.blocksAndModes", <||>], "meanFieldEMT", ""]|>,
  "testGeometries" -> <|"G1" -> "Stage 1: e_mu^a = delta + P(x), three rational points", "G2" -> "Stage 1: primordial field with arbitrary a4 at three exact points (numbers in Q(cos z))",
    "G3" -> "Stage 1: Bianchi-I h_i = 1 + x4^2/(i+2), x4 in {1/3, -2/5, 3/7}", "G4" -> Lookup[$meas, "geometry.G4", <||>],
    "randomFieldData" -> "Stage-1 LCG: state' = (6364136223846793005 state + 1442695040888963407) mod 2^64, value = (floor(state/2^33) mod 19 - 9)/(floor(state/2^13) mod 9 + 1); fdata[seed] = {R(seed,16), R(seed+1,128) as 8x16, sym(seed+2), R(seed+3,16), R(seed+4,128), sym(seed+5)} (Psi, d Psi, dd Psi, Psi^dagger, d Psi^dagger, dd Psi^dagger), sym(s): 36 blocks of 16 for l <= k; cdata[seed] = fdata[seed] + i fdata[seed+50] with Psi^dagger = conj",
    "seeds" -> "connection 60000+100k, vielbein variation 61000+100k (off shell) and 61050+100k (on-shell free data), EMT 62000+100k (+10 on shell, +20 complex, +30 general U), homogeneous G3 63000+100k"|>,
  "exactValues" -> <|"vielbeinVariationG1p1" -> KeyTake[Lookup[Lookup[$meas, "EMT.vielbeinVariation", <||>], "G1p1", <||>], {"offShellTlowerExact", "offShellS", "seeds", "m", "lambda"}],
    "homogeneousG3" -> Map[KeyTake[#["quartic"], {"rhoExact", "pExact", "KE_LExact", "PE_LExact", "wExact", "SExact", "x4", "m", "lambda"}] &, Lookup[$meas, "EMT.homogeneous", <||>] // KeyDrop[#, {"statement"}] &]|>
  |>];

End[];
EndPackage[];
