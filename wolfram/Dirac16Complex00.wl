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
