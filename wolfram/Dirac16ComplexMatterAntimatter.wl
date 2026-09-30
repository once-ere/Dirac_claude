(* ::Package:: *)

(* ::Title:: *)
(* Dirac16ComplexMatterAntimatter.wl *)

(* ::Text:: *)
(* Exact matter-antimatter analysis of the dirac16complex theory (MATTER_ANTIMATTER_SPEC,
   theorems M1-M4 and the exact implication of M5), for BOTH statistics:
   dirac16complex (Grassmann-odd components) and dirac16complex00 (commuting components).

   HONESTY RULE (binding).  The statement "the theory solves the matter-antimatter problem"
   is NOT proved here and cannot be: the Lagrangian L1 of STAGE5_SPEC is exactly U(1)
   invariant for every potential U(S), so the charge Q is conserved in every gravitational
   field (M1).  This package proves what CAN be proved: M1 (U(1), Noether current, its
   conservation, charge conservation), M2 (the complete exact classification of the
   discrete maps built from constant 16x16 matrices and coordinate/frame reflections:
   charge conjugations Psi -> M Psi^* and M Psibar^T, Pin(4,4) reflections, time
   reversals, CPT-like combinations, and their action on L), M3 (the exact classification
   of the Spin(4,4)- and Pin(4,4)-invariant Majorana-type bilinears Psi^T M Psi and
   Psi^T M gamma^a d_a Psi, which survive for which statistics, their U(1) charge), M4 (the
   charge flip j -> -j under gamma^8 and the classical pair totals; the one-particle Krein
   facts including the canonical generators of the image field; the Fock-level mapping is
   cited from the Stage-5 pairing report as PROVISIONAL while Stage 5 has not passed its
   gate, and as OPEN if that report is absent or not all true), and M5 (the classical-level
   implication H1 & H2 & H3 => total charge of the pair vanishes, with H1-H3 recorded as
   unproved hypotheses; at the quantum level no reading gives a cancellation between two
   independent universes).

   Conventions: CONTRACT.md with errata section 11 (zero-based indices, x4 = time,
   eta = diag(+,+,+,+,-,-,-,-), gamma^a = [[0, taubar_a],[tau_a, 0]] of the exact fixture
   artifacts/dirac16complex/arbitrary-field/algebra-fixture.json, C = sigma16 =
   gamma^0 gamma^1 gamma^2 gamma^3, Psibar = Psi^dagger C, B = -i C gamma^4,
   gamma^8 = gamma^0 ... gamma^7 = diag(-I8, +I8), Omega_mu = (1/2) omega_{mu ab} S^{ab}),
   STAGE5_SPEC (L1):
     L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi)
                   - m Psibar Psi - U(Psibar Psi) ],   default U = (lambda/2) S^2.
   The current is j^mu = Psibar gamma^mu Psi (spec normalization); the Hermitian Stage-1
   current is J^mu = -i j^mu, and in Gaussian normal gauge J^4 = Psi^dagger B Psi.

   Statistics.  Commuting components are ordinary exact symbols.  Grassmann components
   are generators of an exact Grassmann algebra implemented in this package (section 2):
   ids 1..16 Psi^dagger_a, 17..32 Psi_a, 33..160 d_mu Psi^dagger_a, 161..288 d_mu Psi_a,
   289..864 and 865..1440 the second derivatives (symmetric in mu, nu).  All generators
   are odd and anticommute; products are order preserving; a linear or antilinear
   substitution of the field is an order-preserving algebra homomorphism (the classical
   image of a unitary or antiunitary operator acting by conjugation), so the reordering
   signs are computed by the algebra and never inserted by hand.

   Exactness: integers, rationals, Gaussian rationals and exact symbolic algebra; every zero
   test is Expand[...] === 0 (or Together for rational functions).  No floating point
   number decides any check, with one labelled exception: MA_M1_ksFixedNetNumberRecorded
   reads the recorded floating-point Stage-4 Kohn-Sham runs (a data check, not a proof).
   (The reused Stage-1 geometry package fixes the branch sqrt|g| = |det e| from the sign of
   the exact rational det e at the evaluation point.)

   Reused machinery (read only): wolfram/Dirac16ComplexGeometry.wl (public API:
   D16GeoFrameJet, D16GeoJetGeometry, D16GeoFieldJets, D16GeoLagrangianJets, D16GeoEMTJets,
   D16GeoSolveOnShell, D16GeoG1Frame, D16GeoRandomRationals), the exact fixture.

   Public entry point: D16MARun[repoRoot] -> <|"checks" -> <|name -> True|False|>,
   "measurements" -> <|...|>, "theory" -> <|...|>|> (theory -> matter-antimatter-theory.json).

   License: GPL-3.0-or-later. *)

If[! MemberQ[$Packages, "Dirac16Complex`Geometry`"],
  Get[FileNameJoin[{DirectoryName[$InputFileName], "Dirac16ComplexGeometry.wl"}]]];

BeginPackage["Dirac16ComplexMatterAntimatter`"];

D16MARun::usage = "D16MARun[repoRoot] runs every exact matter-antimatter check (M1-M5) and returns <|\"checks\" -> ..., \"measurements\" -> ..., \"theory\" -> ...|>.";
D16MAExpectedCheckCount::usage = "D16MAExpectedCheckCount is the fixed number of checks produced by D16MARun.";

Begin["`Private`"];

(* ================================================================== *)
(* 0. bookkeeping                                                      *)
(* ================================================================== *)

$checks = <||>; $meas = <||>; $theory = <||>;
addCheck[name_String, val_] := Module[{v = TrueQ[val]},
  $checks[name] = v;
  Print["  ", name, " = ", v];
  v];
addMeas[name_String, val_] := ($meas[name] = val);
logT[msg__] := Print["[", DateString[{"Hour", ":", "Minute", ":", "Second"}], "] ", msg];

toStr[e_] := Block[{$Context = "Dirac16ComplexMatterAntimatter`Private`",
    $ContextPath = {"System`", "Dirac16ComplexMatterAntimatter`Private`"}},
  ToString[e, InputForm, PageWidth -> Infinity]];
ratStr[x_Integer] := ToString[x];
ratStr[x_Rational] := ToString[Numerator[x]] <> "/" <> ToString[Denominator[x]];
(* exact number -> JSON value: integer, "p/q", or {"re", "im"} for Gaussian rationals *)
jnum[x_Integer] := x;
jnum[x_Rational] := ratStr[x];
jnum[Complex[a_, b_]] := {ratStr[a], ratStr[b]};
jnum[x_] := toStr[x];
jmat[m_List] := Map[jnum, m, {-1}];
zeroE[x_] := AllTrue[Flatten[{x}], (Expand[#] === 0) &];
zeroT[x_] := AllTrue[Flatten[{x}], (Together[#] === 0) &];
sameE[a_, b_] := Dimensions[a] === Dimensions[b] && zeroE[a - b];

(* aliases of the public Stage-1 geometry API (context Dirac16Complex`Geometry`) *)
geoFrameJet = Dirac16Complex`Geometry`D16GeoFrameJet;
geoJetGeometry = Dirac16Complex`Geometry`D16GeoJetGeometry;
geoFieldJets = Dirac16Complex`Geometry`D16GeoFieldJets;
geoLagJets = Dirac16Complex`Geometry`D16GeoLagrangianJets;
geoEMTJets = Dirac16Complex`Geometry`D16GeoEMTJets;
geoSolveOnShell = Dirac16Complex`Geometry`D16GeoSolveOnShell;
geoG1Frame = Dirac16Complex`Geometry`D16GeoG1Frame;
geoRandom = Dirac16Complex`Geometry`D16GeoRandomRationals;
geoGammas = Dirac16Complex`Geometry`D16GeoGammas;

(* ================================================================== *)
(* 1. gamma matrices (CONTRACT section 1), own construction            *)
(* ================================================================== *)

id4 = IdentityMatrix[4]; id8 = IdentityMatrix[8]; id16 = IdentityMatrix[16];
zero16 = ConstantArray[0, {16, 16}];
etaD = {1, 1, 1, 1, -1, -1, -1, -1}; etaM = DiagonalMatrix[etaD];
qa[h_, p_, q_] := Signature[{h, p, q, 4}];
qb[h_, p_, q_] := id4[[p, 4]] id4[[q, h]] - id4[[p, h]] id4[[q, 4]];
s4m[h_] := Table[qa[h, p, q] - qb[h, p, q], {p, 4}, {q, 4}];
t4m[h_] := Table[qa[h, p, q] + qb[h, p, q], {p, 4}, {q, 4}];
sig8 = ArrayFlatten[{{0, id4}, {id4, 0}}];
tauL = Module[{tt = ConstantArray[0, 8]},
  tt[[1]] = id8;
  Do[tt[[h + 1]] = ArrayFlatten[{{0, s4m[h]}, {s4m[h], 0}}], {h, 1, 3}];
  Do[tt[[7 - h + 1]] = ArrayFlatten[{{0, t4m[h]}, {-t4m[h], 0}}], {h, 1, 3}];
  tt[[8]] = tt[[2]].tt[[3]].tt[[4]].tt[[5]].tt[[6]].tt[[7]];
  tt];
taubL = Join[{id8}, Table[sig8.Transpose[tauL[[A + 1]]].sig8, {A, 1, 7}]];
gamL = Table[ArrayFlatten[{{0, taubL[[A + 1]]}, {tauL[[A + 1]], 0}}], {A, 0, 7}];
G[a_Integer] := gamL[[a + 1]];
C16 = ArrayFlatten[{{-sig8, 0}, {0, sig8}}];
Sab[a_Integer, b_Integer] := Sab[a, b] = (G[a].G[b] - G[b].G[a])/4;
pairsAB = Flatten[Table[{a, b}, {a, 0, 6}, {b, a + 1, 7}], 1];
spinGens = Sab @@@ pairsAB;
g8 = Fold[Dot, id16, gamL];
Pm = (id16 - g8)/2; Pp = (id16 + g8)/2;
Bm = -I C16.G[4];
herm[m_] := ConjugateTranspose[m];
(* Clifford monomial Gamma_A = gamma^{a1} ... gamma^{ak}, a1 < ... < ak (A a subset of 0..7) *)
monoOf[A_List] := Fold[Dot, id16, gamL[[# + 1]] & /@ Sort[A]];
allSubsets = Subsets[Range[0, 7]];
monomials = monoOf /@ allSubsets;
isSpacelike[a_] := a <= 3;

checkAlgebra[fixFile_] := Module[{fx, Bfx, Sfx, ok, cliff, facts},
  fx = Import[fixFile, "RawJSON"];
  Bfx = fx["B"]["real"] + I fx["B"]["imag"];
  Sfx = Association[Table[{s["a"], s["b"]} -> Map[If[StringQ[#], ToExpression[#], #] &, s["matrix"], {2}], {s, fx["S"]}]];
  ok = fx["gamma"] === gamL && fx["C"] === C16 && fx["chirality"] === g8 && Bfx === Bm && fx["eta"] === etaM &&
    Length[Sfx] === 28 && AllTrue[pairsAB, KeyExistsQ[Sfx, #] && Sfx[#] === Sab @@ # &] && geoGammas === gamL;
  addMeas["algebra_fixtureComparedMatrices", "eta, gamma^0..gamma^7, C, gamma^8, the 28 S^{ab} (a<b), B, and the Stage-1 geometry package gammas"];
  addCheck["MA_algebra_fixtureMatches", ok];
  cliff = AllTrue[Flatten[Table[G[a].G[b] + G[b].G[a] === 2 etaM[[a + 1, b + 1]] id16, {a, 0, 7}, {b, 0, 7}]], TrueQ];
  facts = <|
    "clifford" -> cliff,
    "gammasRealSignedPermutations" -> AllTrue[gamL, Function[gm, AllTrue[Flatten[gm], IntegerQ] &&
        AllTrue[gm, Function[row, Count[row, x_ /; x =!= 0] === 1]] && Union[Flatten[Abs[gm]]] === {0, 1}]],
    "Csymmetric" -> (Transpose[C16] === C16 && C16.C16 === id16 && C16 === G[0].G[1].G[2].G[3]),
    "CgammaAntisymmetric" -> AllTrue[Range[0, 7], Transpose[C16.G[#]] === -C16.G[#] &],
    "gammaTransposeC" -> AllTrue[Range[0, 7], Transpose[G[#]].C16 === -C16.G[#] &],
    "gamma8" -> (g8 === DiagonalMatrix[Join[ConstantArray[-1, 8], ConstantArray[1, 8]]] &&
        AllTrue[Range[0, 7], g8.G[#] === -G[#].g8 &] && g8.C16 === C16.g8 && AllTrue[spinGens, g8.# === #.g8 &]),
    "BHermitianInvolution" -> (herm[Bm] === Bm && Bm.Bm === id16 && Transpose[Bm] === -Bm && Conjugate[Bm] === -Bm),
    "spinGeneratorsReal" -> AllTrue[spinGens, FreeQ[#, Complex] &]|>;
  addMeas["algebra_facts", facts];
  addCheck["MA_algebra_basicFacts", AllTrue[Values[facts], TrueQ]];
];

(* ================================================================== *)
(* 2. exact Grassmann algebra (own implementation)                     *)
(* ================================================================== *)
(* element: Association  sortedIdList -> coefficient.  The coefficient is an exact scalar
   (possibly a polynomial in symbols such as m, lambda, a phase ph) or, only for elements
   that are later differentiated with gTotalD, an order-1 jet {value, d_0, ..., d_7} of its
   explicit x-dependence at the evaluation point. *)

idQ0[a_] := a + 1; idP0[a_] := 17 + a;
idQ1[mu_, a_] := 33 + 16 mu + a; idP1[mu_, a_] := 161 + 16 mu + a;
pairIdx[mu_, nu_] := With[{i = Min[mu, nu], j = Max[mu, nu]}, 8 i - i (i - 1)/2 + (j - i)];
idQ2[mu_, nu_, a_] := 289 + 16 pairIdx[mu, nu] + a; idP2[mu_, nu_, a_] := 865 + 16 pairIdx[mu, nu] + a;
pTypeQ[id_] := (17 <= id <= 32) || (161 <= id <= 288) || (865 <= id <= 1440);
dmap[id_, lam_] := Which[
  id <= 16, idQ1[lam, id - 1], id <= 32, idP1[lam, id - 17],
  id <= 160, idQ2[lam, Quotient[id - 33, 16], Mod[id - 33, 16]],
  id <= 288, idP2[lam, Quotient[id - 161, 16], Mod[id - 161, 16]],
  True, Throw[{"second derivative generator differentiated", id}, d16maErr]];

coefZeroQ[c_List] := AllTrue[c, Expand[#] === 0 &];
coefZeroQ[c_] := Expand[c] === 0;
coefNorm[c_List] := Expand /@ c;
coefNorm[c_] := Expand[c];
gClean[x_Association] := Select[coefNorm /@ x, ! coefZeroQ[#] &];
gFromPairs[pairs_List] := If[pairs === {}, <||>, gClean[GroupBy[pairs, First -> Last, Total]]];
gPairs[x_Association] := KeyValueMap[List, x];
gAdd[list_List] := gFromPairs[Flatten[gPairs /@ list, 1]];
gNeg[x_Association] := Map[-# &, x];
gScale[c_, x_Association] := If[Expand[c] === 0, <||>, gClean[Map[c # &, x]]];
gGen[id_Integer] := <|{id} -> 1|>;
gZeroQ[x_Association] := Length[gClean[x]] === 0;
gEqualQ[x_Association, y_Association] := gZeroQ[gAdd[{x, gNeg[y]}]];
gMul[x_Association, y_Association] := Module[{kx = Keys[x], vx = Values[x], ky = Keys[y], vy = Values[y], acc},
  If[kx === {} || ky === {}, Return[<||>]];
  acc = Reap[Do[
      If[DisjointQ[kx[[i]], ky[[j]]],
        With[{mm = Join[kx[[i]], ky[[j]]]}, Sow[{Sort[mm], Signature[mm] vx[[i]] vy[[j]]}]]],
      {i, Length[kx]}, {j, Length[ky]}]][[2]];
  If[acc === {}, <||>, gFromPairs[First[acc]]]];
gMulList[list_List] := Fold[gMul, <|{} -> 1|>, list];
(* vectors of elements *)
gVecGen[f_] := Table[gGen[f[a]], {a, 0, 15}];
gMatVec[m_, v_List] := Table[gAdd[Table[If[m[[i, j]] =!= 0, gScale[m[[i, j]], v[[j]]], Nothing], {j, Length[v]}]], {i, Length[m]}];
gRowMat[v_List, m_] := Table[gAdd[Table[If[m[[i, j]] =!= 0, gScale[m[[i, j]], v[[i]]], Nothing], {i, Length[v]}]], {j, Length[First[m]]}];
gDot[u_List, v_List] := gAdd[MapThread[gMul, {u, v}]];
gBil[u_List, m_, v_List] := gDot[gRowMat[u, m], v];
gVecAdd[u_List, v_List] := MapThread[gAdd[{#1, #2}] &, {u, v}];
gVecNeg[u_List] := gNeg /@ u;
gVecScale[c_, u_List] := gScale[c, #] & /@ u;
(* derivatives: left and right Grassmann derivatives with respect to one generator *)
gLeftD[x_Association, id_] := gFromPairs[KeyValueMap[Function[{key, c},
    With[{pos = FirstPosition[key, id]}, If[MissingQ[pos], Nothing, {Delete[key, pos[[1]]], (-1)^(pos[[1]] - 1) c}]]], x]];
gRightD[x_Association, id_] := gFromPairs[KeyValueMap[Function[{key, c},
    With[{pos = FirstPosition[key, id]}, If[MissingQ[pos], Nothing, {Delete[key, pos[[1]]], (-1)^(Length[key] - pos[[1]]) c}]]], x]];
(* total derivative d_lam (lam = 0..7) at the point: acts on the generators (d/dx^lam of an odd
   generator is the next-order odd generator, an even derivation) and, for jet coefficients,
   on the explicit x-dependence; the result carries value coefficients *)
gTotalD[x_Association, lam_Integer] := gFromPairs[Flatten[KeyValueMap[Function[{key, c},
    With[{c0 = If[ListQ[c], c[[1]], c]},
      Join[
        If[ListQ[c] && Expand[c[[lam + 2]]] =!= 0, {{key, c[[lam + 2]]}}, {}],
        Table[With[{new = ReplacePart[key, p -> dmap[key[[p]], lam]]},
            If[DuplicateFreeQ[new], {Sort[new], Signature[new] c0}, Nothing]], {p, Length[key]}]]]], x], 1]];
(* order-preserving homomorphism defined on generators: f[id] is an element *)
gSubst[x_Association, f_] := gAdd[KeyValueMap[Function[{key, c}, gScale[c, gMulList[f /@ key]]], x]];
(* U(1) charge of a monomial: (# Psi-type generators) - (# Psi^dagger-type generators) *)
qTypeQ[id_] := ! pTypeQ[id];
gCharges[x_Association] := Union[(Count[#, _?pTypeQ] - Count[#, _?qTypeQ]) & /@ Keys[x]];
(* bilinear with a jet coefficient matrix:  sum_ij A_ij(x) u_i v_j  for single generators *)
gBilJet[aJet_, uIds_List, vIds_List] := Module[{a0 = aJet[[1]], ad = aJet[[2]]},
  gFromPairs[Flatten[Table[
      With[{cj = Prepend[ad[[All, i, j]], a0[[i, j]]]},
        If[coefZeroQ[cj], Nothing, With[{mm = {uIds[[i]], vIds[[j]]}}, {Sort[mm], Signature[mm] cj}]]],
      {i, Length[uIds]}, {j, Length[vIds]}], 1]]];

(* ================================================================== *)
(* 3. geometry at the points of the general test vielbein G1          *)
(* ================================================================== *)
(* G1 (Stage 1): e_mu^a = delta + P(x), a general non-diagonal polynomial vielbein with
   space-space, space-time and time-time mixing; three exact rational points.  All
   geometric objects are exact order-1 jets from the Stage-1 geometry package. *)

xs = Table[Symbol["Dirac16ComplexMatterAntimatter`Private`x" <> ToString[k]], {k, 0, 7}];
g1Pts = {
  {1/7, -2/9, 1/5, 3/11, -1/13, 2/17, -3/19, 1/23},
  {-1/3, 1/4, 2/7, -1/5, 1/6, -2/11, 1/9, 3/13},
  {2/9, 1/8, -1/7, 1/10, -3/14, 1/12, 2/15, -1/16}};
(* frame reflection e_mu^a -> e_mu^b R_b^a with R = diag(rdiag): the same metric g *)
geoCache = <||>;
geoAt[k_Integer, rdiag_List : {1, 1, 1, 1, 1, 1, 1, 1}] := Module[{key = {k, rdiag}, fr, fj},
  If[KeyExistsQ[geoCache, key], Return[geoCache[key]]];
  fr = geoG1Frame[xs].DiagonalMatrix[rdiag];
  fj = geoFrameJet[fr, xs, Thread[xs -> g1Pts[[k]]]];
  geoCache[key] = geoJetGeometry[fj, "Curvature" -> False]];
(* point values used by the Lagrangian builders *)
geoVals[geo_Association, omKey_String : "Omega"] := <|"sq" -> geo["sqrtg"][[1]], "gam" -> geo["gamma"][[1]],
  "Om" -> geo[omKey][[1]], "gamLow" -> geo["gammaLower"][[1]], "g" -> geo["g"][[1]]|>;
flatVals = <|"sq" -> 1, "gam" -> gamL, "Om" -> ConstantArray[zero16, 8],
  "gamLow" -> Table[etaD[[a]] gamL[[a]], {a, 8}], "g" -> etaM|>;

(* ================================================================== *)
(* 4. the Lagrangian L1 for both statistics at a point                 *)
(* ================================================================== *)
(* commuting components: p = Psi (16), dp[[mu]] = d_mu Psi, q = Psi^dagger (row), dq[[mu]]
   = d_mu Psi^dagger; ordinary exact symbols (q is the complex conjugate of p; every
   manipulation below is a polynomial identity in independent p, q, which is stronger). *)
cParts[v_Association, p_List, dp_List, q_List, dq_List] := Module[{bar, Dpsi, Dbar, S, kin},
  bar = q.C16;
  Dpsi = Table[dp[[mu]] + v["Om"][[mu]].p, {mu, 8}];
  Dbar = Table[dq[[mu]].C16 - bar.v["Om"][[mu]], {mu, 8}];
  S = Expand[bar.p];
  kin = Expand[(1/2) Sum[bar.v["gam"][[mu]].Dpsi[[mu]] - Dbar[[mu]].v["gam"][[mu]].p, {mu, 8}]];
  <|"bar" -> bar, "Dpsi" -> Dpsi, "Dbar" -> Dbar, "S" -> S, "K" -> kin, "psi" -> p|>];
(* L_s = K - m S - U(S); uFun is either a function of S or the symbol "generic" (an undefined U) *)
cLs[parts_Association, m_, uFun_] := parts["K"] - m parts["S"] - uFun[parts["S"]];
uQuartic[lam_][s_] := (lam/2) s^2;
uQuarticCubic[lam_, c3_][s_] := (lam/2) s^2 + (c3/3) s^3;

(* Grassmann components: the same with elements of the Grassmann algebra *)
gParts[v_Association, p_List, dp_List, q_List, dq_List] := Module[{bar, Dpsi, Dbar, S, kin},
  bar = gRowMat[q, C16];
  Dpsi = Table[gVecAdd[dp[[mu]], gMatVec[v["Om"][[mu]], p]], {mu, 8}];
  Dbar = Table[gVecAdd[gRowMat[dq[[mu]], C16], gVecNeg[gRowMat[bar, v["Om"][[mu]]]]], {mu, 8}];
  S = gDot[bar, p];
  kin = gScale[1/2, gAdd[Table[gAdd[{gDot[bar, gMatVec[v["gam"][[mu]], Dpsi[[mu]]]],
      gNeg[gDot[gRowMat[Dbar[[mu]], v["gam"][[mu]]], p]]}], {mu, 8}]]];
  <|"bar" -> bar, "Dpsi" -> Dpsi, "Dbar" -> Dbar, "S" -> S, "K" -> kin, "psi" -> p|>];
(* U = (lambda/2) S^2 + (c3/3) S^3 (every Grassmann U is a polynomial of degree <= 16 in S) *)
gLs[parts_Association, m_, lam_, c3_] := Module[{S = parts["S"], S2},
  S2 = gMul[S, S];
  gAdd[{parts["K"], gScale[-m, S], gScale[-lam/2, S2], If[c3 === 0, <||>, gScale[-c3/3, gMul[S2, S]]]}]];

(* field data *)
pSym = Table[Symbol["Dirac16ComplexMatterAntimatter`Private`pp" <> ToString[a]], {a, 0, 15}];
qSym = Table[Symbol["Dirac16ComplexMatterAntimatter`Private`qq" <> ToString[a]], {a, 0, 15}];
dpSym = Table[Symbol["Dirac16ComplexMatterAntimatter`Private`dpp" <> ToString[mu] <> "x" <> ToString[a]], {mu, 0, 7}, {a, 0, 15}];
dqSym = Table[Symbol["Dirac16ComplexMatterAntimatter`Private`dqq" <> ToString[mu] <> "x" <> ToString[a]], {mu, 0, 7}, {a, 0, 15}];
gP = gVecGen[idP0]; gQ = gVecGen[idQ0];
gDP = Table[gVecGen[idP1[mu, #] &], {mu, 0, 7}];
gDQ = Table[gVecGen[idQ1[mu, #] &], {mu, 0, 7}];
(* symbolic parameters *)
{mS, lamS, c3S, phS} = Table[Symbol["Dirac16ComplexMatterAntimatter`Private`" <> s], {s, {"mass", "lambda", "cubic", "phase"}}];
aMu = Table[Symbol["Dirac16ComplexMatterAntimatter`Private`alphaDer" <> ToString[mu]], {mu, 0, 7}];
uGen = Symbol["Dirac16ComplexMatterAntimatter`Private`Ugeneric"];
uGenPrime = Symbol["Dirac16ComplexMatterAntimatter`Private`UgenericPrime"];

(* ================================================================== *)
(* 5. M1: exact U(1), Noether current, conservation, charge            *)
(* ================================================================== *)

(* jets of sqrt|g| C gamma^mu (value, d_lam) for the Noether identity *)
sqCgamJet[geo_Association, mu_Integer] := Module[{sq = geo["sqrtg"], gm = geo["gamma"]},
  {sq[[1]] C16.gm[[1, mu]], Table[sq[[2, lam]] C16.gm[[1, mu]] + sq[[1]] C16.gm[[2, lam, mu]], {lam, 8}]}];

checkM1Invariance[] := Module[{resFlat, resG1, phaseMap, grassRes, grassPhase, pw, S, powOK, counts, coefAbs,
    parts, ls, lsP},
  (* commuting components, an ARBITRARY function U: S is exactly invariant, hence so is U(S) *)
  phaseMap[v_] := Module[{a, b, dl},
    a = cParts[v, pSym, dpSym, qSym, dqSym];
    b = cParts[v, phS pSym, phS dpSym, qSym/phS, dqSym/phS];
    dl = Together[cLs[b, mS, uGen] - cLs[a, mS, uGen]];
    <|"S" -> (Expand[b["S"]] === Expand[a["S"]]), "K" -> (Expand[b["K"] - a["K"]] === 0),
      "L" -> (dl === 0), "genericUArgumentIdentical" -> (Expand[b["S"] - a["S"]] === 0)|>];
  resFlat = phaseMap[flatVals];
  addMeas["M1_u1CommutingFlat", resFlat];
  addCheck["MA_M1_u1InvarianceCommutingGenericU_flat", AllTrue[Values[resFlat], TrueQ]];
  resG1 = Table[phaseMap[geoVals[geoAt[k]]], {k, 3}];
  addMeas["M1_u1CommutingG1", resG1];
  addCheck["MA_M1_u1InvarianceCommutingGenericU_G1", AllTrue[Flatten[Values /@ resG1], TrueQ]];
  (* Grassmann components: every admissible U is a polynomial of degree <= 16 in S (S^17 = 0);
     the phase acts as the automorphism Psi -> ph Psi, Psi^dagger -> Psi^dagger / ph *)
  grassRes = Table[
    parts = gParts[geoVals[geoAt[k]], gP, gDP, gQ, gDQ];
    ls = gLs[parts, mS, lamS, c3S];
    <|"point" -> k, "monomials" -> Length[ls], "charges" -> gCharges[ls]|>, {k, 3}];
  parts = gParts[geoVals[geoAt[1]], gP, gDP, gQ, gDQ];
  ls = gLs[parts, mS, lamS, c3S];
  lsP = gSubst[ls, Function[id, gScale[If[pTypeQ[id], phS, 1/phS], gGen[id]]]];
  grassPhase = gEqualQ[lsP, ls];
  addMeas["M1_u1GrassmannG1", grassRes];
  addMeas["M1_u1GrassmannG1_explicitPhaseAutomorphismPoint1", grassPhase];
  addCheck["MA_M1_u1InvarianceGrassmann_G1", AllTrue[grassRes, #["charges"] === {0} &] && grassPhase];
  S = gDot[gRowMat[gQ, C16], gP];
  pw = NestList[gMul[#, S] &, S, 16];
  counts = Length /@ pw;
  coefAbs = Table[Union[Abs[Values[pw[[k]]]]], {k, 1, 16}];
  powOK = counts === Append[Binomial[16, Range[16]], 0] && coefAbs === Table[{k!}, {k, 1, 16}] &&
    AllTrue[pw[[1 ;; 16]], gCharges[#] === {0} &] && pw[[17]] === <||>;
  addMeas["M1_grassmannPowersOfS_monomialCounts_k1to17", counts];
  addMeas["M1_grassmannPowersOfS_statement", "(Psibar Psi)^k has binomial(16,k) monomials with coefficients +-k!, every monomial has U(1) charge 0 (k Psi and k Psi^dagger generators), (Psibar Psi)^17 = 0: every Grassmann potential U is a polynomial of degree <= 16 in S and is U(1) invariant"];
  addCheck["MA_M1_grassmannPotentialsPolynomialAndNeutral", powOK];
];

(* E and Ebar (Grassmann) for U = (lambda/2) S^2 + (c3/3) S^3, U' = lambda S + c3 S^2 *)
gFieldEqs[v_Association, parts_Association, m_, lam_, c3_] := Module[{S = parts["S"], S2, uPart, E, Eb},
  S2 = gMul[S, S];
  uPart[x_] := gAdd[{gScale[m, x], gScale[lam, gMul[S, x]], gScale[c3, gMul[S2, x]]}];
  E = gVecAdd[gAdd /@ Transpose[Table[gMatVec[v["gam"][[mu]], parts["Dpsi"][[mu]]], {mu, 8}]], gVecNeg[uPart /@ parts["psi"]]];
  Eb = gVecAdd[gAdd /@ Transpose[Table[gRowMat[parts["Dbar"][[mu]], v["gam"][[mu]]], {mu, 8}]], uPart /@ parts["bar"]];
  <|"E" -> E, "Ebar" -> Eb, "uPart" -> uPart|>];
(* the same for commuting components with a generic U' *)
cFieldEqs[v_Association, parts_Association, m_, uPrime_] := <|
  "E" -> Sum[v["gam"][[mu]].parts["Dpsi"][[mu]], {mu, 8}] - (m + uPrime[parts["S"]]) parts["psi"],
  "Ebar" -> Sum[parts["Dbar"][[mu]].v["gam"][[mu]], {mu, 8}] + (m + uPrime[parts["S"]]) parts["bar"]|>;
(* d_mu (sqrt|g| q C gamma^mu p) for commuting data *)
cDivCurrent[geo_Association, p_, dp_, q_, dq_] := With[{v = geoVals[geo]},
  Sum[q.(sqCgamJet[geo, mu][[2, mu]]).p + v["sq"] (dq[[mu]].C16.v["gam"][[mu]].p + q.C16.v["gam"][[mu]].dp[[mu]]), {mu, 8}]];

checkM1Noether[] := Module[{locC, locG, frmC, frmG, idG, idC, ctrl, v, geo, cp, cpA, ls, jmu, parts, L, Lp,
    f, jn, lhs, rhs, fe},
  (* (a) local phase: Psi -> e^{i alpha(x)} Psi at a point with alpha = 0, d_mu alpha = aMu:
     L' - L = i sqrt|g| aMu_mu j^mu, j^mu = Psibar gamma^mu Psi *)
  locC = Table[
    v = geoVals[geoAt[k]];
    cp = cParts[v, pSym, dpSym, qSym, dqSym];
    cpA = cParts[v, pSym, Table[dpSym[[mu]] + I aMu[[mu]] pSym, {mu, 8}], qSym, Table[dqSym[[mu]] - I aMu[[mu]] qSym, {mu, 8}]];
    jmu = Table[Expand[qSym.C16.v["gam"][[mu]].pSym], {mu, 8}];
    Expand[v["sq"] (cLs[cpA, mS, uGen] - cLs[cp, mS, uGen]) - I v["sq"] aMu.jmu] === 0, {k, 3}];
  addMeas["M1_localPhaseCommutingG1", locC];
  addCheck["MA_M1_noetherCurrentLocalPhase_commuting_G1", And @@ locC];
  locG = Table[
    v = geoVals[geoAt[k]];
    parts = gParts[v, gP, gDP, gQ, gDQ];
    L = gScale[v["sq"], gLs[parts, mS, lamS, c3S]];
    f = Function[id, Which[
      161 <= id <= 288, gAdd[{gGen[id], gScale[I aMu[[Quotient[id - 161, 16] + 1]], gGen[idP0[Mod[id - 161, 16]]]]}],
      33 <= id <= 160, gAdd[{gGen[id], gScale[-I aMu[[Quotient[id - 33, 16] + 1]], gGen[idQ0[Mod[id - 33, 16]]]]}],
      True, gGen[id]]];
    Lp = gSubst[L, f];
    jmu = Table[gBil[gQ, C16.v["gam"][[mu]], gP], {mu, 8}];
    gEqualQ[gAdd[{Lp, gNeg[L]}], gAdd[Table[gScale[I v["sq"] aMu[[mu]], jmu[[mu]]], {mu, 8}]]], {k, 3}];
  addMeas["M1_localPhaseGrassmannG1", locG];
  addCheck["MA_M1_noetherCurrentLocalPhase_grassmann_G1", And @@ locG];
  (* (b) the Noether formula J^mu = (dL/d(d_mu Psi_a)) (i Psi_a) + (-i Psi^dagger_a)(dL/d(d_mu Psi^dagger_a));
     Grassmann: right derivative for Psi, left derivative for Psi^dagger *)
  frmG = Table[
    v = geoVals[geoAt[k]];
    parts = gParts[v, gP, gDP, gQ, gDQ];
    L = gScale[v["sq"], gLs[parts, mS, lamS, c3S]];
    AllTrue[Range[0, 7], Function[mu,
      jn = gAdd[Flatten[Table[{gMul[gRightD[L, idP1[mu, a]], gScale[I, gGen[idP0[a]]]],
          gMul[gScale[-I, gGen[idQ0[a]]], gLeftD[L, idQ1[mu, a]]]}, {a, 0, 15}]]];
      gEqualQ[jn, gScale[I v["sq"], gBil[gQ, C16.v["gam"][[mu + 1]], gP]]]]], {k, 3}];
  addMeas["M1_noetherFormulaGrassmannG1", frmG];
  addCheck["MA_M1_noetherCurrentFormula_grassmann_G1", And @@ frmG];
  frmC = Table[
    v = geoVals[geoAt[k]];
    cp = cParts[v, pSym, dpSym, qSym, dqSym];
    ls = v["sq"] cLs[cp, mS, uGen];
    AllTrue[Range[8], Function[mu, Expand[Sum[D[ls, dpSym[[mu, a]]] (I pSym[[a]]) + (-I qSym[[a]]) D[ls, dqSym[[mu, a]]], {a, 16}] -
        I v["sq"] qSym.C16.v["gam"][[mu]].pSym] === 0]], {k, 3}];
  addMeas["M1_noetherFormulaCommutingG1", frmC];
  addCheck["MA_M1_noetherCurrentFormula_commuting_G1", And @@ frmC];
  (* (c) off-shell Noether identity  d_mu(sqrt|g| j^mu) = sqrt|g| (Ebar Psi + Psibar E),
     E = gamma^mu D_mu Psi - (m + U'(S)) Psi,  Ebar = (D_mu Psibar) gamma^mu + (m + U'(S)) Psibar *)
  idG = Table[
    geo = geoAt[k]; v = geoVals[geo];
    parts = gParts[v, gP, gDP, gQ, gDQ];
    fe = gFieldEqs[v, parts, mS, lamS, c3S];
    lhs = gAdd[Table[gTotalD[gBilJet[sqCgamJet[geo, mu], idQ0 /@ Range[0, 15], idP0 /@ Range[0, 15]], mu - 1], {mu, 8}]];
    rhs = gScale[v["sq"], gAdd[{gDot[fe["Ebar"], gP], gDot[parts["bar"], fe["E"]]}]];
    <|"identity" -> gEqualQ[lhs, rhs], "lhsMonomials" -> Length[lhs],
      "potentialTermsCancel" -> gZeroQ[gAdd[{gDot[fe["uPart"] /@ parts["bar"], gP], gNeg[gDot[parts["bar"], fe["uPart"] /@ gP]]}]]|>, {k, 3}];
  addMeas["M1_noetherIdentityGrassmannG1", idG];
  addCheck["MA_M1_noetherIdentity_grassmann_G1", AllTrue[idG, #["identity"] && #["potentialTermsCancel"] && #["lhsMonomials"] > 0 &]];
  idC = Table[
    geo = geoAt[k]; v = geoVals[geo];
    cp = cParts[v, pSym, dpSym, qSym, dqSym];
    fe = cFieldEqs[v, cp, mS, uGenPrime];
    lhs = cDivCurrent[geo, pSym, dpSym, qSym, dqSym];
    rhs = v["sq"] (fe["Ebar"].pSym + cp["bar"].fe["E"]);
    <|"identity" -> (Expand[lhs - rhs] === 0), "lhsNonzero" -> (Expand[lhs] =!= 0)|>, {k, 3}];
  addMeas["M1_noetherIdentityCommutingG1_genericUprime", idC];
  addCheck["MA_M1_noetherIdentity_commuting_G1", AllTrue[idC, #["identity"] && #["lhsNonzero"] &]];
  (* (d) negative control: with the notebook contraction Omega_NB (Stage-1 section 5.6) the
     identity fails, because the divergence identity fails for it *)
  ctrl = Table[
    geo = geoAt[k]; v = geoVals[geo, "OmegaNotebook"];
    cp = cParts[v, pSym, dpSym, qSym, dqSym];
    fe = cFieldEqs[v, cp, mS, uGenPrime];
    lhs = cDivCurrent[geo, pSym, dpSym, qSym, dqSym];
    rhs = v["sq"] (fe["Ebar"].pSym + cp["bar"].fe["E"]);
    Expand[lhs - rhs] =!= 0, {k, 3}];
  addMeas["M1_negativeControlNotebookConnectionIdentityFails", ctrl];
  addCheck["MA_M1_negativeControlNotebookConnection", And @@ ctrl];
];

(* on-shell conservation with exact on-shell jets (Stage-1 solver, commuting evaluation) *)
randomSym2[seed_Integer] := Module[{r = geoRandom[seed, 36*16], c = 0, arr = ConstantArray[0, {8, 8, 16}]},
  Do[With[{vv = r[[16 c + 1 ;; 16 c + 16]]}, arr[[i, j]] = vv; arr[[j, i]] = vv; c++], {i, 8}, {j, i, 8}];
  arr];
randomFree[seed_Integer] := {geoRandom[seed, 16], Partition[geoRandom[seed + 1, 128], 16], randomSym2[seed + 2],
  geoRandom[seed + 3, 16], Partition[geoRandom[seed + 4, 128], 16], randomSym2[seed + 5]};
mList = {3/7, -2/5, 5/9}; lamList = {5/11, 7/13, -3/8};

checkM1OnShell[] := Module[{res},
  res = Table[Module[{geo = geoAt[k], v, free, sol, ok, p0, p1, p2, q0, q1, q2, parts, fe, div, divFree},
      v = geoVals[geo];
      free = randomFree[4100 + 10 k];
      {sol, ok} = geoSolveOnShell[geo, free, mList[[k]], lamList[[k]]];
      {p0, p1, p2, q0, q1, q2} = sol;
      parts = cParts[v, p0, p1, q0, q1];
      fe = cFieldEqs[v, parts, mList[[k]], (lamList[[k]] #) &];
      div = cDivCurrent[geo, p0, p1, q0, q1];
      divFree = cDivCurrent[geo, free[[1]], free[[2]], free[[4]], free[[5]]];
      <|"point" -> k, "m" -> jnum[mList[[k]]], "lambda" -> jnum[lamList[[k]]], "solverResidualZero" -> ok,
        "fieldEquationsZeroAtPoint" -> (zeroE[fe["E"]] && zeroE[fe["Ebar"]]),
        "divergenceOnShellIsZero" -> (Expand[div] === 0),
        "divergenceOffShellIsNonzero" -> (Expand[divFree] =!= 0)|>], {k, 3}];
  addMeas["M1_onShellConservationG1", res];
  addCheck["MA_M1_onShellConservation_G1", AllTrue[res, #["solverResidualZero"] && #["fieldEquationsZeroAtPoint"] &&
      #["divergenceOnShellIsZero"] && #["divergenceOffShellIsNonzero"] &]];
];

(* the charge density: Gaussian normal gauge and a general frame *)
checkM1Charge[] := Module[{x, ee, gx4, hermR, cp, ok},
  hermR[m_] := Transpose[m] /. Complex[a_, b_] :> Complex[a, -b];   (* all symbols real *)
  ee = Table[Symbol["Dirac16ComplexMatterAntimatter`Private`ev" <> ToString[a]], {a, 0, 7}];
  gx4 = Sum[ee[[a + 1]] G[a], {a, 0, 7}];                   (* gamma^{x4} = e_a^4 gamma^a *)
  cp = Expand[CharacteristicPolynomial[Bm, x]];
  ok = <|
    "j4MatrixIsIB" -> (C16.G[4] === I Bm),
    "J4MatrixIsB" -> (-I C16.G[4] === Bm),
    "BHermitian" -> (herm[Bm] === Bm),
    "BSpectrum" -> (cp === Expand[(x - 1)^8 (x + 1)^8]),
    "BTraceless" -> (Tr[Bm] === 0),
    "generalFrameChargeMatrixHermitian" -> zeroE[hermR[-I C16.gx4] - (-I C16.gx4)]|>;
  addMeas["M1_chargeDensity", <|"checks" -> ok,
    "statement" -> "sqrt|g| j^{x4} = sqrt|g| Psibar gamma^{x4} Psi; in Gaussian normal gauge gamma^{x4} = gamma^4 and J^4 = -i j^4 = Psi^dagger B Psi with B Hermitian, B^2 = 1, spectrum (+1)^8 (-1)^8: the conserved charge density is an indefinite (8,8) form (Krein structure, Stage 1 Theorem 10.1). Q = integral over the slice x4 = const of sqrt|g| J^{x4} d^7x.",
    "chargeConservation" -> "derived: integrating the exact local identity d_mu(sqrt|g| j^mu) = 0 (on shell) over a slab between two slices x4 = t1, t2 and applying the divergence theorem in the slice coordinates gives Q(t2) - Q(t1) = - (flux through the lateral boundary), which vanishes for fields with compact support on the slices (or sufficient fall-off, or periodic identifications). The divergence theorem is pure calculus and holds for the indefinite slice metric as well. Not a separate machine check.",
    "consequence" -> "no solution of the field equations of L1 (either statistics, any U, any gravitational field with g^44 != 0) changes Q inside one universe"|>];
  addCheck["MA_M1_chargeDensityMatrix", AllTrue[Values[ok], TrueQ]];
];

(* the Stage-1 checks this analysis builds on (read from the committed Stage-1 reports) *)
checkM1Stage1[root_String] := Module[{files, need, rows, ok},
  files = <|"wolfram-geometry" -> "wolfram-geometry-report.json", "wolfram-algebra" -> "wolfram-algebra-report.json",
    "grassmann-demo" -> "grassmann-demo-report.json"|>;
  need = <|"wolfram-geometry" -> {"GEO_divergenceIdentity_G1", "GEO_divergenceIdentity_G2", "LAG_eulerLagrangePsibar_G1",
      "LAG_eulerLagrangePsibar_G2", "LAG_eulerLagrangePsi_G1", "LAG_eulerLagrangePsi_G2", "LAG_localSpinInvariance_G1",
      "LAG_localSpinInvariance_G2", "EMT_conservation_G1", "EMT_conservation_G2"},
    "wolfram-algebra" -> {"QNT_currentHermiticity", "ALG_gamma8Map", "ALG_pinLiftCharacter", "ALG_invariantForms", "ALG_chargeFormB"},
    "grassmann-demo" -> {"GR_currentHermitian"}|>;
  rows = Association[KeyValueMap[Function[{key, fname}, Module[{f = FileNameJoin[{root, "artifacts", "dirac16complex", "arbitrary-field", fname}], d},
      d = If[FileExistsQ[f], Quiet[Import[f, "RawJSON"]], $Failed];
      key -> <|"file" -> fname, "sha256" -> If[FileExistsQ[f], ToLowerCase[FileHash[f, "SHA256", All, "HexString"]], "missing"],
        "checks" -> If[AssociationQ[d] && AssociationQ[d["checks"]], Association[(# -> Lookup[d["checks"], #, "absent"]) & /@ need[key]], "unreadable"]|>]], files]];
  ok = AllTrue[Values[rows], AssociationQ[#["checks"]] && AllTrue[Values[#["checks"]], TrueQ] &];
  addMeas["M1_stage1ChecksCited", <|"reports" -> rows,
    "role" -> "Stage-1 results used here: the Euler-Lagrange equations of L1 (both variations, lambda != 0, genuine Grassmann algebra), the divergence identity d_mu(sqrt|g| gamma^mu) = sqrt|g| [gamma^mu, Omega_mu], local Spin invariance, EMT conservation, Hermiticity of the current, the chirality map, the Pin characters, the invariant forms and the charge form B; M1 re-verifies the U(1) and current statements independently in this package"|>];
  addCheck["MA_M1_stage1ChecksCited", ok];
];

(* recorded Stage-4 Kohn-Sham runs: the net occupation equals the imposed N (data, not a proof) *)
checkM1KS[root_String] := Module[{refFiles, rustFiles, refRows, rustRows, tol, theoryFile, theory, defn, rowsOK, constraintInFunctional},
  tol[n_] := 10^-9 Max[1, Abs[n]];
  refFiles = Sort[FileNames["run.json", FileNameJoin[{root, "artifacts", "dirac16complex", "kohn-sham", "reference"}], 2]];
  rustFiles = Sort[FileNames["run.json", FileNameJoin[{root, "artifacts", "dirac16complex", "kohn-sham", "rust", "scf"}], 2]];
  refRows = Map[Function[f, Module[{d = Quiet[Import[f, "RawJSON"]], nn, lv},
      If[! AssociationQ[d], Return[<|"file" -> f, "parsed" -> False|>, Module]];
      nn = d["params"]["N"];
      lv = If[ListQ[d["levels"]], d["levels"], {}];
      <|"parsed" -> True, "N" -> nn, "levels" -> Length[lv],
        "maxAbsDeviation" -> If[lv === {}, Missing[], Max[Abs[#["energies"]["nTotal"] - nn] & /@ lv]],
        "ok" -> (lv =!= {} && AllTrue[lv, Abs[#["energies"]["nTotal"] - nn] <= tol[nn] &])|>]], refFiles];
  rustRows = Map[Function[f, Module[{d = Quiet[Import[f, "RawJSON"]], nn},
      If[! AssociationQ[d], Return[<|"file" -> f, "parsed" -> False|>, Module]];
      nn = d["parameters"]["N"];
      <|"parsed" -> True, "N" -> nn, "maxAbsDeviation" -> Abs[d["nTotal"] - nn], "ok" -> (Abs[d["nTotal"] - nn] <= tol[nn])|>]], rustFiles];
  theoryFile = FileNameJoin[{root, "artifacts", "dirac16complex", "kohn-sham", "kohn-sham-theory.json"}];
  theory = Quiet[Import[theoryFile, "RawJSON"]];
  defn = If[AssociationQ[theory], theory["functional"]["definition"], ""];
  constraintInFunctional = StringQ[defn] && StringContainsQ[defn, "sum_n f_n = N"];
  rowsOK = Length[refRows] > 0 && Length[rustRows] > 0 && AllTrue[Join[refRows, rustRows], TrueQ[#["parsed"]] && TrueQ[#["ok"]] &];
  addMeas["M1_ksFixedNetNumber", <|
    "status" -> "recorded floating-point data (not an exact proof): the Stage-4 Mermin functional constrains sum_n f_n = N with the chemical potential mu as Lagrange multiplier, and in the no-sea convention the net occupation nTotal (particle occupations minus sea holes) is the Kohn-Sham image of the U(1) charge; every recorded run has nTotal = N to 1e-9 relative",
    "functionalContainsConstraint" -> constraintInFunctional,
    "referenceRunFiles" -> Length[refFiles], "referenceLevelsChecked" -> Total[Lookup[refRows, "levels", 0]],
    "rustRunFiles" -> Length[rustFiles],
    "maxAbsDeviationReference" -> If[refRows === {}, Missing[], N[Max[DeleteMissing[Lookup[refRows, "maxAbsDeviation", Missing[]]]]]],
    "maxAbsDeviationRust" -> If[rustRows === {}, Missing[], N[Max[DeleteMissing[Lookup[rustRows, "maxAbsDeviation", Missing[]]]]]]|>];
  addCheck["MA_M1_ksFixedNetNumberRecorded", rowsOK && constraintInFunctional];
];

(* ================================================================== *)
(* 6. M2: discrete maps (C, P, T and combinations), both statistics    *)
(* ================================================================== *)
(* A discrete map is a triple (M, R, type): R a subset of the frame/coordinate directions
   0..7 that are reflected (Lambda = diag(rd), rd_a = -1 for a in R), M a constant 16x16
   matrix, type "linear" (Psi'(x) = M Psi(Rx)) or "antilinear" (Psi'(x) = M Psi^*(Rx)).
   In a curved field the same map acts on the frame, e_mu^a -> e_mu^b Lambda_b^a (same
   metric), without a coordinate change; a coordinate reflection is then a diffeomorphism,
   under which L is a scalar density. *)

signOf[x_, y_] := Which[zeroE[x - y], 1, zeroE[x + y], -1, True, 0];
gSignOf[x_Association, y_Association] := Which[gEqualQ[x, y], 1, gEqualQ[x, gNeg[y]], -1, True, 0];
rDiag[R_List] := Table[If[MemberQ[R, a], -1, 1], {a, 0, 7}];
sCount[R_List] := Count[R, _?(# <= 3 &)];
tCount[R_List] := Length[R] - sCount[R];
constSign[list_List] := If[Length[Union[list]] === 1 && MemberQ[{1, -1}, First[list]], First[list], 0];
(* M^{-1} gamma^a M rd_a = eps gamma^a for all a *)
epsOf[M_, rd_] := With[{Mi = Inverse[M]}, constSign[Table[signOf[Mi.G[a].M rd[[a + 1]], G[a]], {a, 0, 7}]]];
(* M^dagger C gamma^a M rd_a = kappaLin C gamma^a for all a;  M^dagger C M = sigmaLin C *)
kappaLinOf[M_, rd_] := constSign[Table[signOf[herm[M].C16.G[a].M rd[[a + 1]], C16.G[a]], {a, 0, 7}]];
sigmaLinOf[M_] := signOf[herm[M].C16.M, C16];
(* the image of L_{m,lambda}: kappa L_{sigma kappa m, kappa lambda} *)
lMapString[k_, s_] := Which[
  k === 1 && s === 1, "L_{m,lambda} (exact symmetry)",
  k === 1 && s === -1, "L_{-m,lambda}",
  k === -1 && s === 1, "-L_{-m,-lambda}",
  k === -1 && s === -1, "-L_{m,-lambda}",
  True, "undefined"];

(* X -> A.X - s X.B on row-major vec(X) *)
opAXsXB[a_, b_, s_] := KroneckerProduct[a, IdentityMatrix[Length[b]]] - s KroneckerProduct[IdentityMatrix[Length[a]], Transpose[b]];
nullBasis[rows_] := Module[{mat = SparseArray[rows], ns}, ns = Normal /@ NullSpace[mat]; Partition[#, 16] & /@ ns];
primitive[m_] := Module[{flat = Flatten[m], nz, sc, g, f},
  nz = Select[flat, # =!= 0 &];
  If[nz === {}, Return[m]];
  sc = (LCM @@ (Denominator /@ (Flatten[{Re[#], Im[#]} & /@ nz]))) m;
  f = First[Select[Flatten[sc], # =!= 0 &]];
  sc/f];

monoPrim := monoPrim = primitive /@ monomials;
monoIndex[x_] := With[{px = primitive[x]}, SelectFirst[Range[256], monoPrim[[#]] === px &, 0]];

checkM2Intertwiners[] := Module[{sol, solT, okC, okT, pats, patOK, comm, eachDim, explicit, explicitOK},
  (* Psi -> M Psi^*: the Dirac operator maps to eta times itself iff gamma^a M = eta M gamma^{a*} (all a) *)
  sol = Association[Table[eta -> nullBasis[Join @@ Table[opAXsXB[G[a], Conjugate[G[a]], eta], {a, 0, 7}]], {eta, {1, -1}}]];
  okC = Length[sol[1]] === 1 && Length[sol[-1]] === 1 &&
    primitive[First[sol[1]]] === id16 && primitive[First[sol[-1]]] === primitive[g8] &&
    AllTrue[Join[sol[1], sol[-1]], Function[x, AllTrue[spinGens, zeroE[#.x - x.#] &]]];
  addMeas["M2_conjugationIntertwiners", <|
    "condition" -> "gamma^a M = eta M conj(gamma^a) for a = 0..7 (the gammas are real)",
    "dimensionEtaPlus" -> Length[sol[1]], "dimensionEtaMinus" -> Length[sol[-1]],
    "basisEtaPlus" -> "I16", "basisEtaMinus" -> "gamma^8",
    "commuteWithEverySab" -> AllTrue[Join[sol[1], sol[-1]], Function[x, AllTrue[spinGens, zeroE[#.x - x.#] &]]],
    "meaning" -> "the only constant charge conjugations Psi -> M Psi^* compatible with the Dirac operator are M = z I (eta = +1: same sign of the kinetic operator) and M = z gamma^8 (eta = -1); both commute with every Omega_mu, so the statement holds in every gravitational field (real vielbein, real Omega)"|>];
  addCheck["MA_M2_conjugationIntertwiners", okC];
  (* Psi -> M Psibar^T = M C Psi^*: condition gamma^a M = zeta M gamma^{aT} *)
  solT = Association[Table[zeta -> nullBasis[Join @@ Table[opAXsXB[G[a], Transpose[G[a]], zeta], {a, 0, 7}]], {zeta, {1, -1}}]];
  okT = Length[solT[1]] === 1 && Length[solT[-1]] === 1 &&
    primitive[First[solT[-1]]] === primitive[C16] && primitive[First[solT[1]]] === primitive[g8.C16] &&
    primitive[First[solT[-1]].C16] === id16 && primitive[First[solT[1]].C16] === primitive[g8];
  addMeas["M2_transposeIntertwiners", <|
    "condition" -> "gamma^a M = zeta M gamma^{aT} (a = 0..7)",
    "dimensionZetaPlus" -> Length[solT[1]], "dimensionZetaMinus" -> Length[solT[-1]],
    "basisZetaMinus" -> "C (Psi -> C Psibar^T = Psi^*)", "basisZetaPlus" -> "gamma^8 C (Psi -> gamma^8 C Psibar^T = gamma^8 Psi^*)",
    "meaning" -> "the Psibar^T forms are the same two maps: M Psibar^T = (M C) Psi^*"|>];
  addCheck["MA_M2_transposeIntertwiners", okT];
  (* all sign patterns: M gamma^a M^{-1} = eps_a gamma^a *)
  pats = Table[Table[signOf[monomials[[i]].G[a].Inverse[monomials[[i]]], G[a]], {a, 0, 7}], {i, 256}];
  comm = nullBasis[Join @@ Table[opAXsXB[G[a], G[a], 1], {a, 0, 7}]];
  patOK = Sort[pats] === Sort[Tuples[{-1, 1}, 8]] && Length[comm] === 1 && primitive[First[comm]] === id16;
  (* explicit exact null spaces for the patterns of the single reflections, of the 3-space, 4-space,
     time and full reflections (both signs) *)
  explicit = Table[Module[{rd = rDiag[Rset], ns},
      Table[ns = nullBasis[Join @@ Table[opAXsXB[G[a], G[a], eps rd[[a + 1]]], {a, 0, 7}]];
        <|"R" -> Rset, "eps" -> eps, "dimension" -> Length[ns],
          "monomial" -> If[Length[ns] === 1, With[{i = monoIndex[First[ns]]}, If[i === 0, "none", allSubsets[[i]]]], "none"]|>, {eps, {1, -1}}]],
    {Rset, Join[Table[{b}, {b, 0, 7}], {{1, 2, 3}, {0, 1, 2, 3}, {4, 5, 6, 7}, {1, 2, 3, 4}, Range[0, 7], {}}]}];
  explicit = Flatten[explicit, 1];
  explicitOK = AllTrue[explicit, #["dimension"] === 1 &&
      (#["monomial"] === #["R"] && #["eps"] === (-1)^Length[#["R"]] || #["monomial"] === Complement[Range[0, 7], #["R"]] && #["eps"] === -(-1)^Length[#["R"]]) &];
  addMeas["M2_signPatternClassification", <|
    "statement" -> "the 256 Clifford monomials Gamma_A realise the 256 sign patterns M gamma^a M^{-1} = eps_a gamma^a bijectively; since the commutant of the gammas is one-dimensional, the solution space of every pattern is exactly one-dimensional, spanned by its monomial. For the map (M, R): M^{-1} gamma^a M rd_a = eps gamma^a has exactly the two solutions M = Gamma_R (eps = (-1)^|R|) and M = Gamma_{R^c} (eps = -(-1)^|R|), up to a scalar.",
    "patternsDistinct" -> (Length[Union[pats]] === 256), "commutantDimension" -> Length[comm],
    "explicitNullSpaces" -> explicit|>];
  addCheck["MA_M2_signPatternClassification", patOK && explicitOK];
];

(* statistics sign of the antilinear substitution: (M conj(Psi))^dagger X (M conj(Psi)) = s Psi^dagger (M^dagger X M)^T Psi *)
checkM2StatisticsSign[] := Module[{Y, gr, co, sG, sC},
  Y = Partition[geoRandom[777, 256], 16] + I Partition[geoRandom[778, 256], 16];
  gr = gBil[gP, Y, gQ];                         (* sum_ij Y_ij Psi_i Psi^dagger_j *)
  sG = gSignOf[gr, gBil[gQ, Transpose[Y], gP]];
  sC = signOf[Expand[pSym.Y.qSym], Expand[qSym.Transpose[Y].pSym]];
  addMeas["M2_statisticsSign", <|"grassmann" -> sG, "commuting" -> sC,
    "statement" -> "Psi^T Y Psi^* = s Psi^dagger Y^T Psi for every matrix Y (tested with an exact random Gaussian-rational Y): s = -1 for Grassmann components, s = +1 for commuting components"|>];
  addCheck["MA_M2_statisticsSign", sG === -1 && sC === 1];
];

(* the matrix-level classification of all 256 x 2 maps (M, R) and both types, both statistics *)
classifyRow[R_List, which_String] := Module[{rd = rDiag[R], A, M, eps, kl, sl, rho, rhoL, entries},
  A = If[which === "GammaR", R, Complement[Range[0, 7], R]];
  M = monoOf[A];
  eps = epsOf[M, rd]; kl = kappaLinOf[M, rd]; sl = sigmaLinOf[M];
  rho = signOf[M.Bm.herm[M], Bm]; rhoL = signOf[herm[M].Bm.M, Bm];
  entries = Association[Flatten[Table[
      With[{sg = If[type === "antilinear", st[[2]], 1]},
        (type <> "/" <> st[[1]]) -> <|"kappa" -> sg kl, "sigma" -> sg sl, "Lmap" -> lMapString[sg kl, sg sl],
          "exact" -> (sg kl === 1 && sg sl === 1), "exactAtMassZero" -> (sg kl === 1),
          "currentSigns" -> If[type === "linear", kl rd, -st[[2]] kl rd]|>],
      {type, {"linear", "antilinear"}}, {st, {{"commuting", 1}, {"grassmann", -1}}}]]];
  <|"R" -> R, "sR" -> sCount[R], "tR" -> tCount[R], "M" -> which, "monomial" -> A, "eps" -> eps,
    "kappaLin" -> kl, "sigmaLin" -> sl, "MBMdaggerSign" -> rho, "MdaggerBMSign" -> rhoL, "maps" -> entries|>];

checkM2Classification[] := Module[{rows, wellDefined, epsRule, sigmaRule, kappaRule, linRule, antiRuleC, antiRuleG, bRule, byR},
  rows = Flatten[Table[classifyRow[R, w], {R, allSubsets}, {w, {"GammaR", "GammaRc"}}], 1];
  $theory["M2_classificationRows"] = rows;
  wellDefined = AllTrue[rows, MemberQ[{1, -1}, #["eps"]] && MemberQ[{1, -1}, #["kappaLin"]] && MemberQ[{1, -1}, #["sigmaLin"]] &];
  epsRule = AllTrue[rows, #["eps"] === If[#["M"] === "GammaR", 1, -1] (-1)^Length[#["R"]] &];
  sigmaRule = AllTrue[rows, #["sigmaLin"] === (-1)^#["sR"] &];
  kappaRule = AllTrue[rows, #["kappaLin"] === #["sigmaLin"] #["eps"] &];
  byR = GroupBy[rows, #["R"] &];
  linRule = AllTrue[Keys[byR], Function[R, AnyTrue[byR[R], #["maps"]["linear/commuting"]["exact"] &] === EvenQ[sCount[R]] &&
      AnyTrue[byR[R], #["maps"]["linear/grassmann"]["exact"] &] === EvenQ[sCount[R]]]];
  antiRuleC = AllTrue[Keys[byR], Function[R, AnyTrue[byR[R], #["maps"]["antilinear/commuting"]["exact"] &] === EvenQ[sCount[R]]]];
  antiRuleG = AllTrue[Keys[byR], Function[R, AnyTrue[byR[R], #["maps"]["antilinear/grassmann"]["exact"] &] === OddQ[sCount[R]]]];
  (* for an exact linear symmetry the x4 component of the kinetic term forces M^dagger B M = rd_4 B *)
  bRule = AllTrue[Select[rows, #["maps"]["linear/commuting"]["exact"] &], #["MdaggerBMSign"] === rDiag[#["R"]][[5]] &];
  addMeas["M2_classificationSummary", <|
    "rows" -> Length[rows],
    "rule_eps" -> "eps(Gamma_R) = (-1)^|R|, eps(Gamma_{R^c}) = -(-1)^|R|", "rule_epsVerified" -> epsRule,
    "rule_sigma" -> "M^dagger C M = (-1)^{s_R} C for both M (s_R = number of reflected space-like directions 0..3)", "rule_sigmaVerified" -> sigmaRule,
    "rule_kappa" -> "kappaLin = sigmaLin eps", "rule_kappaVerified" -> kappaRule,
    "rule_linear" -> "an exact linear symmetry (L -> L) with reflected set R exists iff s_R is even (both statistics; any number of time-like reflections)", "rule_linearVerified" -> linRule,
    "rule_antilinearCommuting" -> "an exact antilinear symmetry exists iff s_R is even (commuting components)", "rule_antilinearCommutingVerified" -> antiRuleC,
    "rule_antilinearGrassmann" -> "an exact antilinear symmetry exists iff s_R is odd (Grassmann components)", "rule_antilinearGrassmannVerified" -> antiRuleG,
    "rule_general" -> "for every map: L_{m,lambda}[T Psi] = kappa L_{sigma kappa m, kappa lambda}[Psi] (up to the reflection of the arguments), with (kappa, sigma) = (kappaLin, sigmaLin) for linear maps and s (kappaLin, sigmaLin) for antilinear maps, s the statistics sign",
    "rule_BUnderExactLinear" -> "M^dagger B M = rd_4 B for every exact linear symmetry", "rule_BUnderExactLinearVerified" -> bRule|>];
  addCheck["MA_M2_matrixClassification", wellDefined && epsRule && sigmaRule && kappaRule && linRule && antiRuleC && antiRuleG && bRule && Length[rows] === 512];
  rows];

(* transformed field data. coord = True: flat coordinate reflection Psi'(x) = M Psi(Rx) (the
   derivatives pick up rd_mu); coord = False: frame reflection in a curved field (no
   coordinate change). *)
cTransform[M_, rd_, type_, coord_] := Module[{f = If[coord, rd, ConstantArray[1, 8]], Md = herm[M]},
  If[type === "linear",
    {M.pSym, Table[f[[mu]] M.dpSym[[mu]], {mu, 8}], qSym.Md, Table[f[[mu]] dqSym[[mu]].Md, {mu, 8}]},
    {M.qSym, Table[f[[mu]] M.dqSym[[mu]], {mu, 8}], pSym.Md, Table[f[[mu]] dpSym[[mu]].Md, {mu, 8}]}]];
gTransform[M_, rd_, type_, coord_] := Module[{f = If[coord, rd, ConstantArray[1, 8]], Md = herm[M]},
  If[type === "linear",
    {gMatVec[M, gP], Table[gVecScale[f[[mu]], gMatVec[M, gDP[[mu]]]], {mu, 8}], gRowMat[gQ, Md], Table[gVecScale[f[[mu]], gRowMat[gDQ[[mu]], Md]], {mu, 8}]},
    {gMatVec[M, gQ], Table[gVecScale[f[[mu]], gMatVec[M, gDQ[[mu]]]], {mu, 8}], gRowMat[gP, Md], Table[gVecScale[f[[mu]], gRowMat[gDP[[mu]], Md]], {mu, 8}]}]];

(* measure (kappa, sigma, current signs) and verify L' = kappa L_{sigma kappa m, kappa lambda} *)
verifyMapC[vO_, vN_, orig_, M_, rd_, type_, coord_] := Module[{tr, new, kS, sS, jS, lOK},
  tr = cTransform[M, rd, type, coord];
  new = cParts[vN, Sequence @@ tr];
  kS = signOf[new["K"], orig["K"]]; sS = signOf[new["S"], orig["S"]];
  jS = Table[signOf[Expand[tr[[3]].C16.vN["gam"][[mu]].tr[[1]]], Expand[qSym.C16.vO["gam"][[mu]].pSym]], {mu, 8}];
  lOK = MemberQ[{1, -1}, kS] && MemberQ[{1, -1}, sS] &&
    zeroE[cLs[new, mS, uQuartic[lamS]] - kS cLs[orig, sS kS mS, uQuartic[kS lamS]]];
  <|"kappa" -> kS, "sigma" -> sS, "currentSigns" -> jS, "LmapHolds" -> lOK|>];
verifyMapG[vO_, vN_, orig_, origL_, M_, rd_, type_, coord_] := Module[{tr, new, kS, sS, jS, lOK},
  tr = gTransform[M, rd, type, coord];
  new = gParts[vN, Sequence @@ tr];
  kS = gSignOf[new["K"], orig["K"]]; sS = gSignOf[new["S"], orig["S"]];
  jS = Table[gSignOf[gBil[tr[[3]], C16.vN["gam"][[mu]], tr[[1]]], gBil[gQ, C16.vO["gam"][[mu]], gP]], {mu, 8}];
  lOK = MemberQ[{1, -1}, kS] && MemberQ[{1, -1}, sS] &&
    gEqualQ[gLs[new, mS, lamS, 0], gScale[kS, gLs[orig, sS kS mS, kS lamS, 0]]];
  <|"kappa" -> kS, "sigma" -> sS, "currentSigns" -> jS, "LmapHolds" -> lOK|>];
predicted[row_, type_, stat_, coord_] := With[{e = row["maps"][type <> "/" <> stat]},
  <|"kappa" -> e["kappa"], "sigma" -> e["sigma"],
    "currentSigns" -> If[coord, e["currentSigns"], e["currentSigns"] rDiag[row["R"]]], "LmapHolds" -> True|>];

checkM2FlatAll[rows_List] := Module[{origC, origG, origGL, resC, resG, badC, badG},
  origC = cParts[flatVals, pSym, dpSym, qSym, dqSym];
  origG = gParts[flatVals, gP, gDP, gQ, gDQ];
  origGL = gLs[origG, mS, lamS, 0];
  badC = {}; badG = {};
  Do[With[{M = monoOf[row["monomial"]], rd = rDiag[row["R"]]},
      Do[
        If[verifyMapC[flatVals, flatVals, origC, M, rd, type, True] =!= predicted[row, type, "commuting", True],
          AppendTo[badC, {row["R"], row["M"], type}]];
        If[verifyMapG[flatVals, flatVals, origG, origGL, M, rd, type, True] =!= predicted[row, type, "grassmann", True],
          AppendTo[badG, {row["R"], row["M"], type}]],
        {type, {"linear", "antilinear"}}]],
    {row, rows}];
  addMeas["M2_lagrangianLevelFlat", <|"mapsPerStatistics" -> 2 Length[rows],
    "statement" -> "for all 512 (M, R) and both types (1024 maps) the transformed Lagrangian density, computed from the transformed jets (commuting symbols, respectively the Grassmann algebra), equals kappa L_{sigma kappa m, kappa lambda} of the original jets at the reflected point, with (kappa, sigma) and the eight current signs exactly as predicted by the matrix classification",
    "mismatchesCommuting" -> badC, "mismatchesGrassmann" -> badG|>];
  addCheck["MA_M2_lagrangianFlatCommuting_all", badC === {} && Length[rows] === 512];
  addCheck["MA_M2_lagrangianFlatGrassmann_all", badG === {} && Length[rows] === 512];
];

(* named maps: (label, R, which monomial, type, expected Lmap commuting, expected Lmap Grassmann) derived by hand *)
namedMaps = {
  {"C: Psi -> conj(Psi) (= C Psibar^T)", {}, "GammaR", "antilinear", "L_{m,lambda} (exact symmetry)", "-L_{m,-lambda}"},
  {"C8: Psi -> gamma^8 conj(Psi) (= gamma^8 C Psibar^T)", {}, "GammaRc", "antilinear", "-L_{-m,-lambda}", "L_{-m,lambda}"},
  {"chirality map Psi -> gamma^8 Psi (Stage-5 T1)", {}, "GammaRc", "linear", "-L_{-m,-lambda}", "-L_{-m,-lambda}"},
  {"P_0 twisted lift: u = gamma^0, x0 -> -x0", {0}, "GammaR", "linear", "L_{-m,lambda}", "L_{-m,lambda}"},
  {"P_4 twisted lift: u = gamma^4, x4 -> -x4", {4}, "GammaR", "linear", "-L_{-m,-lambda}", "-L_{-m,-lambda}"},
  {"P_u untwisted lift, u = gamma^0 (all directions but x0 reflected)", Complement[Range[0, 7], {0}], "GammaRc", "linear", "-L_{m,-lambda}", "-L_{m,-lambda}"},
  {"P_u untwisted lift, u = gamma^5 (all directions but x5 reflected)", Complement[Range[0, 7], {5}], "GammaRc", "linear", "L_{m,lambda} (exact symmetry)", "L_{m,lambda} (exact symmetry)"},
  {"P3: M = gamma^1 gamma^2 gamma^3, (x1,x2,x3) reflected", {1, 2, 3}, "GammaR", "linear", "L_{-m,lambda}", "L_{-m,lambda}"},
  {"P3': M = Gamma_{0,4,5,6,7}, (x1,x2,x3) reflected", {1, 2, 3}, "GammaRc", "linear", "-L_{m,-lambda}", "-L_{m,-lambda}"},
  {"C8 P3: antilinear, M = Gamma_{0,4,5,6,7}, (x1,x2,x3) reflected", {1, 2, 3}, "GammaRc", "antilinear", "-L_{m,-lambda}", "L_{m,lambda} (exact symmetry)"},
  {"C P3: antilinear, M = gamma^1 gamma^2 gamma^3, (x1,x2,x3) reflected", {1, 2, 3}, "GammaR", "antilinear", "L_{-m,lambda}", "-L_{-m,-lambda}"},
  {"C8 P_0: antilinear, M = Gamma_{1..7}, x0 reflected", {0}, "GammaRc", "antilinear", "-L_{m,-lambda}", "L_{m,lambda} (exact symmetry)"},
  {"P4: M = C = gamma^0 gamma^1 gamma^2 gamma^3, (x0..x3) reflected", {0, 1, 2, 3}, "GammaR", "linear", "L_{m,lambda} (exact symmetry)", "L_{m,lambda} (exact symmetry)"},
  {"T linear: M = Gamma_{0,1,2,3,5,6,7}, x4 reflected", {4}, "GammaRc", "linear", "L_{m,lambda} (exact symmetry)", "L_{m,lambda} (exact symmetry)"},
  {"T antilinear: M = Gamma_{0,1,2,3,5,6,7}, x4 reflected", {4}, "GammaRc", "antilinear", "L_{m,lambda} (exact symmetry)", "-L_{m,-lambda}"},
  {"T' antilinear: M = gamma^4, x4 reflected", {4}, "GammaR", "antilinear", "-L_{-m,-lambda}", "L_{-m,lambda}"},
  {"all-time reversal: M = gamma^4 gamma^5 gamma^6 gamma^7, (x4..x7) reflected", {4, 5, 6, 7}, "GammaR", "linear", "L_{m,lambda} (exact symmetry)", "L_{m,lambda} (exact symmetry)"},
  {"full inversion: M = gamma^8 (a Spin_0(4,4) element), all x reflected", Range[0, 7], "GammaR", "linear", "L_{m,lambda} (exact symmetry)", "L_{m,lambda} (exact symmetry)"},
  {"CPT (full): antilinear, M = gamma^8, all x reflected", Range[0, 7], "GammaR", "antilinear", "L_{m,lambda} (exact symmetry)", "-L_{m,-lambda}"},
  {"CPT (full) with M = I: antilinear, all x reflected", Range[0, 7], "GammaRc", "antilinear", "-L_{-m,-lambda}", "L_{-m,lambda}"},
  {"CP3T: antilinear, M = gamma^1 gamma^2 gamma^3 gamma^4, (x1..x4) reflected", {1, 2, 3, 4}, "GammaR", "antilinear", "-L_{m,-lambda}", "L_{m,lambda} (exact symmetry)"}};

checkM2Named[rows_List] := Module[{rowOf, named, handOK, g1C, g1G, g1Res, vO, origC, origG, origGL, vN},
  rowOf[R_, w_] := SelectFirst[rows, #["R"] === Sort[R] && #["M"] === w &];
  named = Table[With[{row = rowOf[nm[[2]], nm[[3]]]},
      <|"label" -> nm[[1]], "R" -> Sort[nm[[2]]], "sR" -> row["sR"], "tR" -> row["tR"], "monomial" -> row["monomial"], "type" -> nm[[4]],
        "commuting" -> row["maps"][nm[[4]] <> "/commuting"]["Lmap"], "grassmann" -> row["maps"][nm[[4]] <> "/grassmann"]["Lmap"],
        "currentSignsCommuting" -> row["maps"][nm[[4]] <> "/commuting"]["currentSigns"],
        "currentSignsGrassmann" -> row["maps"][nm[[4]] <> "/grassmann"]["currentSigns"],
        "handDerivedCommuting" -> nm[[5]], "handDerivedGrassmann" -> nm[[6]]|>], {nm, namedMaps}];
  handOK = AllTrue[named, #["commuting"] === #["handDerivedCommuting"] && #["grassmann"] === #["handDerivedGrassmann"] &];
  $theory["M2_namedMaps"] = named;
  addCheck["MA_M2_namedTransformations", handOK];
  (* the same maps as frame reflections in the general curved field G1 (point 1 for all maps,
     points 2 and 3 for C, C8, C8 P3, T linear and the chirality map) *)
  g1Res = Flatten[Table[
      vO = geoVals[geoAt[k]];
      origC = cParts[vO, pSym, dpSym, qSym, dqSym];
      origG = gParts[vO, gP, gDP, gQ, gDQ]; origGL = gLs[origG, mS, lamS, 0];
      Table[If[k > 1 && ! MemberQ[{1, 2, 3, 10, 14}, i], Nothing,
        Module[{nm = namedMaps[[i]], row, M, rd, rc, rg},
          row = rowOf[nm[[2]], nm[[3]]]; M = monoOf[row["monomial"]]; rd = rDiag[row["R"]];
          vN = geoVals[geoAt[k, rd]];
          rc = verifyMapC[vO, vN, origC, M, rd, nm[[4]], False];
          rg = verifyMapG[vO, vN, origG, origGL, M, rd, nm[[4]], False];
          <|"point" -> k, "label" -> nm[[1]],
            "commutingAgrees" -> (rc === predicted[row, nm[[4]], "commuting", False]),
            "grassmannAgrees" -> (rg === predicted[row, nm[[4]], "grassmann", False]),
            "commuting" -> rc, "grassmann" -> rg|>]], {i, Length[namedMaps]}], {k, 3}], 1];
  addMeas["M2_frameLevelG1", g1Res];
  addCheck["MA_M2_frameLevelG1_commuting", AllTrue[g1Res, #["commutingAgrees"] &] && Length[g1Res] === Length[namedMaps] + 10];
  addCheck["MA_M2_frameLevelG1_grassmann", AllTrue[g1Res, #["grassmannAgrees"] &] && Length[g1Res] === Length[namedMaps] + 10];
  named];

(* symmetry summary and the canonical structure of the Grassmann (quantum) field *)
checkM2Summary[rows_List] := Module[{exists, single, summary, qRev, canon, cUnitary, needRho, canonOK, qRevOK},
  exists[pred_, key_, flag_: "exact"] := AnyTrue[Select[rows, pred], #["maps"][key][flag] &];
  single = (Length[#["R"]] === 1 && #["sR"] === 1) &;
  summary = Association[Table[stat -> <|
      "C (R empty, antilinear) exact" -> exists[#["R"] === {} &, "antilinear/" <> stat],
      "C exact at m = 0" -> exists[#["R"] === {} &, "antilinear/" <> stat, "exactAtMassZero"],
      "P (one space-like reflection, linear) exact" -> exists[single, "linear/" <> stat],
      "P exact at m = 0" -> exists[single, "linear/" <> stat, "exactAtMassZero"],
      "CP (one space-like reflection, antilinear) exact" -> exists[single, "antilinear/" <> stat],
      "P3 (x1,x2,x3, linear) exact" -> exists[#["R"] === {1, 2, 3} &, "linear/" <> stat],
      "CP3 (x1,x2,x3, antilinear) exact" -> exists[#["R"] === {1, 2, 3} &, "antilinear/" <> stat],
      "T (x4, linear) exact" -> exists[#["R"] === {4} &, "linear/" <> stat],
      "T (x4, antilinear) exact" -> exists[#["R"] === {4} &, "antilinear/" <> stat],
      "CPT (all x, antilinear) exact" -> exists[#["R"] === Range[0, 7] &, "antilinear/" <> stat],
      "CP3T (x1..x4, antilinear) exact" -> exists[#["R"] === {1, 2, 3, 4} &, "antilinear/" <> stat]|>,
    {stat, {"commuting", "grassmann"}}]];
  (* exact symmetries that preserve the time orientation (x4 not reflected) and reverse j^4 *)
  qRev = Association[Table[stat -> Flatten[Table[
        Select[rows, #["maps"][type <> "/" <> stat]["exact"] && ! MemberQ[#["R"], 4] &&
            #["maps"][type <> "/" <> stat]["currentSigns"][[5]] === -1 &] /. r_Association :> {type, r["R"], r["monomial"]},
        {type, {"linear", "antilinear"}}], 1], {stat, {"commuting", "grassmann"}}]];
  qRevOK = MemberQ[qRev["commuting"], {"antilinear", {}, {}}] && MemberQ[qRev["grassmann"], {"antilinear", {1, 2, 3}, {0, 4, 5, 6, 7}}] &&
    ! MemberQ[qRev["grassmann"], {"antilinear", {}, _}];
  $theory["M2_symmetrySummary"] = summary;
  $theory["M2_chargeReversingExactSymmetriesPreservingTimeOrientation"] = <|
    "definition" -> "exact symmetries (L -> L) with x4 not reflected and j^4 -> -j^4 (classical substitution rule); entries {type, reflected directions R, monomial A of M = Gamma_A}",
    "commuting" -> qRev["commuting"], "grassmann" -> qRev["grassmann"]|>;
  addMeas["M2_symmetrySummary", summary];
  addCheck["MA_M2_symmetrySummaryAndChargeReversal", qRevOK &&
    summary["commuting"]["C (R empty, antilinear) exact"] && ! summary["grassmann"]["C (R empty, antilinear) exact"] &&
    summary["grassmann"]["C exact at m = 0"] && ! summary["commuting"]["P (one space-like reflection, linear) exact"] &&
    ! summary["grassmann"]["P (one space-like reflection, linear) exact"] && summary["grassmann"]["CP (one space-like reflection, antilinear) exact"] &&
    ! summary["commuting"]["CP (one space-like reflection, antilinear) exact"] && summary["grassmann"]["CP3 (x1,x2,x3, antilinear) exact"] &&
    summary["commuting"]["T (x4, linear) exact"] && summary["grassmann"]["T (x4, linear) exact"]];
  (* canonical anticommutator {Psi, Psi^dagger} = B (Gaussian normal gauge, flat).  A unitary operator
     with U Psi U^-1 = M Psi^{dagger T} preserves it iff M B^T M^dagger = B; with U Psi U^-1 = M Psi
     iff M B M^dagger = B; an antiunitary one iff the same products equal conj(B) = -B. *)
  cUnitary = <|"M=I" -> signOf[id16.Transpose[Bm].herm[id16], Bm], "M=gamma8" -> signOf[g8.Transpose[Bm].herm[g8], Bm]|>;
  needRho[type_, rd4_] := If[type === "linear", rd4, -rd4];
  canon = Flatten[Table[Select[rows, #["maps"][type <> "/grassmann"]["exact"] &] /.
      r_Association :> (r["MBMdaggerSign"] === needRho[type, rDiag[r["R"]][[5]]]), {type, {"linear", "antilinear"}}]];
  canonOK = AllTrue[canon, TrueQ] && Length[canon] > 0 && cUnitary === <|"M=I" -> -1, "M=gamma8" -> 1|>;
  addMeas["M2_canonicalStructure", <|
    "unitaryChargeConjugation" -> "M B^T M^dagger = B holds for M = gamma^8 and fails (= -B) for M = I: the charge conjugation of the quantised Grassmann field that preserves the canonical anticommutator as a linear (unitary-type) automorphism is C8 (Psi -> gamma^8 Psi^{dagger T}), which maps L_{m,lambda} -> L_{-m,lambda}",
    "signs M B^T M^dagger / B" -> cUnitary,
    "exactSymmetriesImplementable" -> "every exact symmetry of the Grassmann theory preserves the canonical anticommutator: as a linear (unitary-type) automorphism if it preserves x4 and as an antilinear (antiunitary-type) one if it reverses x4 (checked for all exact maps); whether a unitary or antiunitary operator on the positive (J = B) Fock space implements it is not decided here",
    "exactGrassmannSymmetriesChecked" -> Length[canon]|>];
  addCheck["MA_M2_canonicalStructure", canonOK];
];

(* ================================================================== *)
(* 7. M3: Spin(4,4)- and Pin(4,4)-invariant Majorana-type bilinears    *)
(* ================================================================== *)
(* Psi^T M Psi and Psi^T M gamma^a d_a Psi (U(1) charge +2).  Invariance under the identity
   component Spin_0(4,4) is the Lie-algebra condition S^{ab T} M + M S^{ab} = 0 (28
   generators); the other components and Pin(4,4) act through characters. *)

formOpT[x_] := KroneckerProduct[Transpose[x], id16] + KroneckerProduct[id16, Transpose[x]];   (* M -> X^T M + M X *)
kinOpT[x_, a_] := KroneckerProduct[Transpose[x], Transpose[G[a]]] +                          (* X^T M gamma^a *)
  KroneckerProduct[id16, Transpose[G[a].x]] +                                                 (* M gamma^a X *)
  KroneckerProduct[id16, Transpose[x.G[a] - G[a].x]];                                         (* M [X, gamma^a] *)
transposeOp = Module[{perm = Flatten[Table[16 (j - 1) + i, {i, 16}, {j, 16}]]}, IdentityMatrix[256][[perm]]];  (* vec(M) -> vec(M^T) *)
spanEqualQ[basis_List, target_List] := MatrixRank[Flatten /@ basis] === Length[target] &&
  MatrixRank[Join[Flatten /@ basis, Flatten /@ target]] === Length[target];

{al, be} = {Symbol["Dirac16ComplexMatterAntimatter`Private`alphaCoef"], Symbol["Dirac16ComplexMatterAntimatter`Private`betaCoef"]};
checkM3Forms[] := Module[{rows, basis, sym, anti, spanOK, chars, charRes, charOK, u1, v1, extra, spinComp, kin, kinOK, gen,
    symSol, antiSol, cg8},
  cg8 = C16.g8;
  rows = Join @@ (formOpT /@ spinGens);
  basis = nullBasis[rows];
  spanOK = Length[basis] === 2 && spanEqualQ[basis, {C16.Pm, C16.Pp}];
  sym = nullBasis[Join[rows, transposeOp - IdentityMatrix[256]]];
  anti = nullBasis[Join[rows, transposeOp + IdentityMatrix[256]]];
  addMeas["M3_spinInvariantMassForms", <|"dimension" -> Length[basis], "basis" -> "C P_-, C P_+ (C P_- = diag(-sigma, 0), C P_+ = diag(0, sigma))",
    "symmetricSubspaceDimension" -> Length[sym], "antisymmetricSubspaceDimension" -> Length[anti],
    "statement" -> "every Spin_0(4,4)-invariant bilinear form Psi^T M Psi has M = alpha C P_- + beta C P_+; all of them are symmetric, none is antisymmetric"|>];
  addCheck["MA_M3_spinInvariantForms", spanOK && Length[sym] === 2 && Length[anti] === 0 &&
    AllTrue[{C16.Pm, C16.Pp}, Function[m, Transpose[m] === m && AllTrue[spinGens, zeroE[Transpose[#].m + m.#] &]]]];
  (* discrete components of Spin(4,4): gamma^a gamma^b with a space-like, b time-like has spinor norm -1 *)
  spinComp = Table[signOf[Transpose[G[a].G[b]].(C16.Pm).(G[a].G[b]), C16.Pm] === -1 &&
      signOf[Transpose[G[a].G[b]].(C16.Pp).(G[a].G[b]), C16.Pp] === -1, {a, 0, 3}, {b, 4, 7}];
  (* Pin(4,4) characters chi = (value on space-like, value on time-like unit vectors) *)
  chars = {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}};
  charRes = Table[Module[{eqs, ns},
      eqs = Join[rows, Join @@ Table[KroneckerProduct[Transpose[G[a]], Transpose[G[a]]] - If[a <= 3, ch[[1]], ch[[2]]] IdentityMatrix[256], {a, 0, 7}]];
      ns = nullBasis[eqs];
      <|"character" -> ch, "dimension" -> Length[ns],
        "basis" -> Which[ns === {}, "none", Length[ns] === 1 && primitive[First[ns]] === primitive[C16], "C",
          Length[ns] === 1 && primitive[First[ns]] === primitive[cg8], "C gamma^8", True, "other"]|>], {ch, chars}];
  charOK = (Lookup[#, "basis"] & /@ charRes) === {"none", "C", "C gamma^8", "none"};
  (* non-basis unit vectors *)
  u1 = G[0] + G[1] + G[4]; v1 = G[0] + G[4] + G[5];
  extra = {signOf[Transpose[u1].C16.u1, C16], signOf[Transpose[v1].C16.v1, C16], signOf[Transpose[u1].cg8.u1, cg8], signOf[Transpose[v1].cg8.v1, cg8]};
  addMeas["M3_pinCharacterForms", <|"characters" -> charRes,
    "statement" -> "u^T M u = chi(u) M for every unit vector u: M = C has chi(u) = -n(u) (the character of Psibar Psi), M = C gamma^8 has chi(u) = +n(u); the trivial and the determinant characters admit no invariant form",
    "nonBasisUnitVectors" -> <|"u = gamma0+gamma1+gamma4 (n = +1): C, C gamma^8" -> extra[[{1, 3}]], "v = gamma0+gamma4+gamma5 (n = -1): C, C gamma^8" -> extra[[{2, 4}]]|>,
    "otherComponentOfSpin44" -> "g = gamma^a gamma^b (a space-like, b time-like, spinor norm -1): g^T (C P_+-) g = -C P_+-: Spin(4,4) acts on the invariant forms through the spinor norm", "otherComponentVerified" -> (And @@ Flatten[spinComp])|>];
  addCheck["MA_M3_pinCharacterForms", charOK && extra === {-1, 1, 1, -1} && And @@ Flatten[spinComp]];
  (* kinetic type Psi^T M gamma^a d_a Psi *)
  kin = nullBasis[Join @@ Flatten[Table[kinOpT[x, a], {x, spinGens}, {a, 0, 7}], 1]];
  gen = al C16.Pm + be C16.Pp;
  symSol = Solve[Thread[DeleteCases[Union[Flatten[Table[Transpose[gen.G[a]] - gen.G[a], {a, 0, 7}]]], 0] == 0], {be}];
  antiSol = Solve[Thread[DeleteCases[Union[Flatten[Table[Transpose[gen.G[a]] + gen.G[a], {a, 0, 7}]]], 0] == 0], {be}];
  kinOK = Length[kin] === 2 && spanEqualQ[kin, {C16.Pm, C16.Pp}] &&
    zeroE[(gen /. First[symSol] /. {al -> -1, be -> 1}) - cg8] && zeroE[(gen /. First[antiSol] /. {al -> 1, be -> 1}) - C16] &&
    AllTrue[Range[0, 7], Transpose[cg8.G[#]] === cg8.G[#] && Transpose[C16.G[#]] === -C16.G[#] &];
  addMeas["M3_kineticInvariantForms", <|"dimension" -> Length[kin], "basis" -> "C P_-, C P_+ (same space as the mass type)",
    "symmetricForAllA" -> "M gamma^a symmetric for every a iff M is proportional to C gamma^8 = C P_+ - C P_-",
    "antisymmetricForAllA" -> "M gamma^a antisymmetric for every a iff M is proportional to C = C P_- + C P_+",
    "solveSymmetric" -> toStr[symSol], "solveAntisymmetric" -> toStr[antiSol]|>];
  addCheck["MA_M3_kineticInvariantForms", kinOK];
];

(* commuting total derivative on polynomials of p (value) and dp (first derivatives) *)
cTotalD[expr_, a_Integer] := Sum[dpSym[[a, c]] D[expr, pSym[[c]]], {c, 16}] + If[FreeQ[expr, Alternatives @@ Flatten[dpSym]], 0,
  Throw["cTotalD: second derivatives not needed here", d16maErr]];
gDerivation[x_Association, f_] := gFromPairs[Flatten[KeyValueMap[Function[{key, c},
    Flatten[Table[With[{img = f[key[[p]]]},
        KeyValueMap[Function[{k1, c1}, With[{new = ReplacePart[key, p -> First[k1]]},
            If[DuplicateFreeQ[new], {Sort[new], Signature[new] c c1}, Nothing]]], img]], {p, Length[key]}], 1]], x], 1]];

checkM3Survival[] := Module[{massG, massC, ctrlG, kinG, kinC, elG, elC, tdC, tdG, lk, u1G, u1C, res, cg8},
  cg8 = C16.g8;
  (* mass type *)
  massG = <|"C P_-" -> gZeroQ[gBil[gP, C16.Pm, gP]], "C P_+" -> gZeroQ[gBil[gP, C16.Pp, gP]],
    "C" -> gZeroQ[gBil[gP, C16, gP]], "C gamma^8" -> gZeroQ[gBil[gP, cg8, gP]]|>;
  ctrlG = Length[gBil[gP, C16.Sab[0, 1], gP]];         (* an antisymmetric (non-invariant) matrix: nonzero *)
  massC = <|"C P_-" -> MatrixRank[C16.Pm], "C P_+" -> MatrixRank[C16.Pp], "C" -> MatrixRank[C16], "C gamma^8" -> MatrixRank[cg8],
    "nonzeroPolynomials" -> AllTrue[{C16.Pm, C16.Pp, C16, cg8}, Expand[pSym.#.pSym] =!= 0 &]|>;
  (* kinetic type: Grassmann EL (left derivatives) and total-derivative test *)
  elG[m_] := Module[{L = gAdd[Table[gBil[gP, m.G[a], gDP[[a + 1]]], {a, 0, 7}]]},
    Table[gAdd[{gLeftD[L, idP0[c]], gNeg[gAdd[Table[gTotalD[gLeftD[L, idP1[a, c]], a], {a, 0, 7}]]]}], {c, 0, 15}]];
  kinG = <|"C gamma^8: Euler-Lagrange nonzero" -> ! AllTrue[elG[cg8], gZeroQ],
    "C gamma^8: EL = 2 C gamma^8 gamma^a d_a Psi" -> AllTrue[Range[16], Function[c, gEqualQ[elG[cg8][[c]],
        gScale[2, gAdd[Table[gMatVec[cg8.G[a], gDP[[a + 1]]][[c]], {a, 0, 7}]]]]]],
    "C: Euler-Lagrange identically zero" -> AllTrue[elG[C16], gZeroQ],
    "C: equals (1/2) d_a(Psi^T C gamma^a Psi)" -> gEqualQ[gAdd[Table[gBil[gP, C16.G[a], gDP[[a + 1]]], {a, 0, 7}]],
        gScale[1/2, gAdd[Table[gTotalD[gBil[gP, C16.G[a], gP], a], {a, 0, 7}]]]]|>;
  (* commuting EL *)
  elC[m_] := Module[{L = Expand[Sum[pSym.(m.G[a]).dpSym[[a + 1]], {a, 0, 7}]]},
    Table[Expand[D[L, pSym[[c]]] - Sum[cTotalD[D[L, dpSym[[a + 1, c]]], a + 1], {a, 0, 7}]], {c, 16}]];
  kinC = <|"C: Euler-Lagrange nonzero" -> ! zeroE[elC[C16]],
    "C: EL = 2 C gamma^a d_a Psi" -> zeroE[elC[C16] - 2 Sum[C16.G[a].dpSym[[a + 1]], {a, 0, 7}]],
    "C gamma^8: Euler-Lagrange identically zero" -> zeroE[elC[cg8]],
    "C gamma^8: equals (1/2) d_a(Psi^T C gamma^8 gamma^a Psi)" -> zeroE[Sum[pSym.(cg8.G[a]).dpSym[[a + 1]], {a, 0, 7}] -
        (1/2) Sum[cTotalD[pSym.(cg8.G[a]).pSym, a + 1], {a, 0, 7}]]|>;
  (* U(1) charge +2 *)
  lk = gAdd[Table[gBil[gP, cg8.G[a], gDP[[a + 1]]], {a, 0, 7}]];
  u1G = gCharges[lk] === {2};
  u1C = Expand[(phS pSym).C16.(phS pSym) - phS^2 pSym.C16.pSym] === 0 &&
    Expand[Sum[(phS pSym).(C16.G[a]).(phS dpSym[[a + 1]]), {a, 0, 7}] - phS^2 Sum[pSym.(C16.G[a]).dpSym[[a + 1]], {a, 0, 7}]] === 0;
  res = <|"grassmannMassTypeVanishes" -> massG, "grassmannControlAntisymmetricNonzeroMonomials" -> ctrlG,
    "commutingMassTypeRanks" -> massC, "grassmannKinetic" -> kinG, "commutingKinetic" -> kinC,
    "u1ChargeGrassmannKinetic" -> gCharges[lk], "u1ChargeCommutingIsTwo" -> u1C,
    "conclusion" -> "Grassmann components: no Spin_0(4,4)-invariant Majorana mass term exists (every invariant M is symmetric, so Psi^T M Psi = 0); the only invariant Majorana-type kinetic term is Psi^T C gamma^8 gamma^a d_a Psi (Psi^T C gamma^a d_a Psi is a total derivative). Commuting components: the two chiral Majorana mass terms Psi^T C P_+- Psi (equivalently C and C gamma^8) survive and the kinetic term Psi^T C gamma^a d_a Psi (the notebook Lg[] form) survives, Psi^T C gamma^8 gamma^a d_a Psi is a total derivative. Every such term has U(1) charge 2 (it is not invariant under Psi -> e^{i alpha} Psi) and is absent from L1."|>;
  addMeas["M3_survival", res];
  addCheck["MA_M3_grassmannSurvival", AllTrue[Values[massG], TrueQ] && ctrlG > 0 && AllTrue[Values[kinG], TrueQ]];
  addCheck["MA_M3_commutingSurvival", massC["C P_-"] === 8 && massC["C P_+"] === 8 && massC["C"] === 16 && massC["C gamma^8"] === 16 &&
    massC["nonzeroPolynomials"] && AllTrue[Values[kinC], TrueQ]];
  addCheck["MA_M3_u1Charge", u1G && u1C && gCharges[gBil[gP, C16.Sab[0, 1], gP]] === {2}];
];

(* Pin(4,4) characters of the surviving Majorana-type terms, flat coordinate action
   Psi'(x) = u Psi(Rx), u = gamma^b, with the twisted (R = {b}) and untwisted (R = all but b) lifts *)
checkM3PinKinetic[] := Module[{cg8, tab, ok},
  cg8 = C16.g8;
  tab = Table[With[{u = G[b], rdT = rDiag[{b}], rdU = rDiag[Complement[Range[0, 7], {b}]]},
      <|"b" -> b, "n" -> etaD[[b + 1]],
        "massC" -> signOf[Transpose[u].C16.u, C16], "massCgamma8" -> signOf[Transpose[u].cg8.u, cg8],
        "kinCTwisted" -> constSign[Table[signOf[Transpose[u].C16.G[a].u rdT[[a + 1]], C16.G[a]], {a, 0, 7}]],
        "kinCUntwisted" -> constSign[Table[signOf[Transpose[u].C16.G[a].u rdU[[a + 1]], C16.G[a]], {a, 0, 7}]],
        "kinCgamma8Twisted" -> constSign[Table[signOf[Transpose[u].cg8.G[a].u rdT[[a + 1]], cg8.G[a]], {a, 0, 7}]],
        "kinCgamma8Untwisted" -> constSign[Table[signOf[Transpose[u].cg8.G[a].u rdU[[a + 1]], cg8.G[a]], {a, 0, 7}]]|>], {b, 0, 7}];
  (* expected: C-type mass and untwisted kinetic -n(u) (as Psibar Psi and the Dirac kinetic term);
     C gamma^8-type mass and untwisted kinetic +n(u); twisted kinetic = - untwisted *)
  ok = AllTrue[tab, #["massC"] === -#["n"] && #["kinCUntwisted"] === -#["n"] && #["kinCTwisted"] === #["n"] &&
      #["massCgamma8"] === #["n"] && #["kinCgamma8Untwisted"] === #["n"] && #["kinCgamma8Twisted"] === -#["n"] &];
  addMeas["M3_pinCharactersMajoranaTerms", <|"table" -> tab,
    "statement" -> "Psi -> u Psi (u = gamma^b, n = eta_bb): Psi^T C Psi and (untwisted lift) Psi^T C gamma^a d_a Psi pick up -n(u); Psi^T C gamma^8 Psi and (untwisted) Psi^T C gamma^8 gamma^a d_a Psi pick up +n(u); with the twisted lift the kinetic sign is reversed"|>];
  addCheck["MA_M3_pinCharactersMajoranaTerms", ok];
];

(* the notebook Lg[] = sqrt g [Psi^T sigma16 T16^a D_a Psi + H M Psi^T sigma16 Psi] is of Majorana type *)
checkM3NotebookLg[] := Module[{inSpan, ok},
  inSpan = spanEqualQ[{C16.Pm, C16.Pp}, {C16.Pm, C16.Pp}] && MatrixRank[{Flatten[C16.Pm], Flatten[C16.Pp], Flatten[C16]}] === 2;
  ok = <|"sigma16EqualsC" -> (C16 === G[0].G[1].G[2].G[3]),
    "kineticMatrixIsCgamma" -> AllTrue[Range[0, 7], C16.G[#] === C16.G[#] &],
    "CInInvariantSpan" -> inSpan,
    "chargeTwoForComplexPsi" -> (Expand[(phS pSym).C16.(phS pSym) - phS^2 pSym.C16.pSym] === 0 && Expand[pSym.C16.pSym] =!= 0),
    "survivesForCommuting" -> TrueQ[$checks["MA_M3_commutingSurvival"]],
    "trivialForGrassmann" -> TrueQ[$checks["MA_M3_grassmannSurvival"]]|>;
  addMeas["M3_notebookLg", <|"checks" -> ok,
    "statement" -> "the notebook Lagrangian Lg[] uses Transpose[Psi16] (not ConjugateTranspose): its kinetic matrix sigma16 T16^a = C gamma^a and its mass matrix sigma16 = C belong to the classified Spin_0-invariant Majorana-type family M = C (Pin character -n(u)). For a complex commuting Psi it has U(1) charge 2; for a real commuting Psi (Stage-5 real restriction) it is non-trivial; for a Grassmann Psi it is a total derivative with vanishing mass term (Stage 1). dirac16complex00 uses the charge-0 Lagrangian L1 instead."|>];
  addCheck["MA_M3_notebookLgIsMajoranaType", AllTrue[Values[ok], TrueQ]];
];

(* EXTRA (beyond the spec's bilinears): a non-vanishing Spin_0-invariant charge-4 quartic of the
   Grassmann field.  omega_+-^{ab} = Psi^T C P_+- S^{ab} Psi (C P_+- S^{ab} antisymmetric, so these
   survive for Grassmann components); Q4 = sum_{a<b} eta_aa eta_bb omega_-^{ab} omega_+^{ab}. *)
checkM3Quartic[] := Module[{wm, wp, q4, qmm, qpp, gensOp, inv, ctrl, antisym},
  antisym = AllTrue[pairsAB, Transpose[C16.Pm.(Sab @@ #)] === -C16.Pm.(Sab @@ #) && Transpose[C16.Pp.(Sab @@ #)] === -C16.Pp.(Sab @@ #) &];
  wm = Association[Table[ab -> gBil[gP, C16.Pm.(Sab @@ ab), gP], {ab, pairsAB}]];
  wp = Association[Table[ab -> gBil[gP, C16.Pp.(Sab @@ ab), gP], {ab, pairsAB}]];
  q4 = gAdd[Table[gScale[etaD[[ab[[1]] + 1]] etaD[[ab[[2]] + 1]], gMul[wm[ab], wp[ab]]], {ab, pairsAB}]];
  qmm = gAdd[Table[gScale[etaD[[ab[[1]] + 1]] etaD[[ab[[2]] + 1]], gMul[wm[ab], wm[ab]]], {ab, pairsAB}]];
  qpp = gAdd[Table[gScale[etaD[[ab[[1]] + 1]] etaD[[ab[[2]] + 1]], gMul[wp[ab], wp[ab]]], {ab, pairsAB}]];
  (* infinitesimal Spin_0 action: the even derivation Psi_i -> sum_j X_ij Psi_j *)
  gensOp[x_] := Function[id, gAdd[Table[If[x[[id - 16, j + 1]] =!= 0, gScale[x[[id - 16, j + 1]], gGen[idP0[j]]], Nothing], {j, 0, 15}]]];
  inv = AllTrue[spinGens, Function[x, gZeroQ[gDerivation[q4, gensOp[x]]]]];
  ctrl = ! gZeroQ[gDerivation[gMul[wm[{0, 1}], wp[{0, 1}]], gensOp[Sab[0, 2]]]];
  addMeas["M3_extraGrassmannQuartic", <|
    "definition" -> "Q4 = sum_{a<b} eta_aa eta_bb (Psi^T C P_- S^{ab} Psi)(Psi^T C P_+ S^{ab} Psi)",
    "omegaMatricesAntisymmetric" -> antisym, "omegaNonzero" -> AllTrue[Join[Values[wm], Values[wp]], ! gZeroQ[#] &],
    "Q4Monomials" -> Length[q4], "Q4Charges" -> gCharges[q4], "Q4InvariantUnderAll28Generators" -> inv,
    "controlSingleTermNotInvariant" -> ctrl, "chiralOnlyQuarticsVanish" -> (gZeroQ[qmm] && gZeroQ[qpp]),
    "status" -> "EXTRA, not required by the spec: a non-vanishing Spin_0(4,4)-invariant local quartic term of U(1) charge 4 exists for the Grassmann field (no bilinear Majorana mass term does). No classification of higher-order terms is attempted; nothing here says such a term is present, natural, or sufficient for baryogenesis."|>];
  addCheck["MA_M3_extraGrassmannQuarticCharge4", antisym && Length[q4] > 0 && gCharges[q4] === {4} && inv && ctrl && gZeroQ[qmm] && gZeroQ[qpp]];
];

(* ================================================================== *)
(* 8. M4: the charge flip under gamma^8 and the pair totals           *)
(* ================================================================== *)

imageData[{p0_, p1_, p2_, q0_, q1_, q2_}] := {g8.p0, (g8.#) & /@ p1, Map[g8.# &, p2, {2}], q0.g8, (#.g8) & /@ q1, Map[#.g8 &, q2, {2}]};
currentValueAndDerivatives[geo_, p0_, p1_, q0_, q1_] := Module[{gm = geo["gamma"]},
  Table[{q0.C16.gm[[1, mu]].p0, Table[q1[[lam]].C16.gm[[1, mu]].p0 + q0.C16.gm[[2, lam, mu]].p0 + q0.C16.gm[[1, mu]].p1[[lam]], {lam, 8}]}, {mu, 8}]];

checkM4[] := Module[{mat, jG, emtC, emtG, v, geo, parts, partsI, tr, free, sol, ok, solI, okI, fld, fldI, lag, lagI, T, TI, jv, jvI, feI},
  mat = <|"currentMatricesOdd" -> AllTrue[Range[0, 7], g8.C16.G[#].g8 === -C16.G[#] &], "massMatrixEven" -> (g8.C16.g8 === C16),
    "PsibarMapsToPsibarGamma8" -> (Transpose[g8].C16 === C16.g8), "kreinMetricFlips" -> (g8.Bm.g8 === -Bm)|>;
  addMeas["M4_matrixFacts", mat];
  addCheck["MA_M4_currentFlipMatrix", AllTrue[Values[mat], TrueQ]];
  (* curved field G1, Grassmann: j^mu[gamma^8 Psi] = -j^mu[Psi] *)
  jG = Table[v = geoVals[geoAt[k]];
    tr = gTransform[g8, ConstantArray[1, 8], "linear", False];
    AllTrue[Range[8], gEqualQ[gBil[tr[[3]], C16.v["gam"][[#]], tr[[1]]], gNeg[gBil[gQ, C16.v["gam"][[#]], gP]]] &], {k, 3}];
  addMeas["M4_currentFlipGrassmannG1", jG];
  addCheck["MA_M4_currentFlipG1_grassmann", And @@ jG];
  (* commuting jets: T_{mu nu} and j^mu of the pair (off shell), the image of an on-shell solution *)
  emtC = Table[geo = geoAt[k];
    free = randomFree[5200 + 10 k];
    fld = geoFieldJets @@ free; fldI = geoFieldJets @@ imageData[free];
    lag = geoLagJets[geo, fld, mList[[k]], lamList[[k]]]; lagI = geoLagJets[geo, fldI, -mList[[k]], -lamList[[k]]];
    T = geoEMTJets[geo, lag]; TI = geoEMTJets[geo, lagI];
    jv = currentValueAndDerivatives[geo, free[[1]], free[[2]], free[[4]], free[[5]]];
    jvI = currentValueAndDerivatives[geo, Sequence @@ imageData[free][[{1, 2, 4, 5}]]];
    {sol, ok} = geoSolveOnShell[geo, randomFree[5300 + 10 k], mList[[k]], lamList[[k]]];
    {solI, okI} = geoSolveOnShell[geo, imageData[sol], -mList[[k]], -lamList[[k]]];
    feI = cFieldEqs[geoVals[geo], cParts[geoVals[geo], Sequence @@ imageData[sol][[{1, 2, 4, 5}]]], -mList[[k]], (-lamList[[k]] #) &];
    <|"point" -> k, "pairEMTJetsVanish" -> zeroE[T + TI], "EMTNonzero" -> ! zeroE[T],
      "pairCurrentJetsVanish" -> zeroE[jv + jvI], "currentNonzero" -> ! zeroE[jv],
      "imageOfSolutionSolvesMinusMMinusLambda" -> (ok && okI && zeroE[solI - imageData[sol]] && zeroE[feI["E"]] && zeroE[feI["Ebar"]])|>, {k, 3}];
  addMeas["M4_pairTotalsCommutingG1", emtC];
  addCheck["MA_M4_pairEMTAndCurrentG1_commuting", AllTrue[emtC, AllTrue[Values[KeyDrop[#, "point"]], TrueQ] &]];
  (* Grassmann: the pair energy-momentum tensor at G1 point 1, all 64 components *)
  emtG = Module[{gEMT, v1 = geoVals[geoAt[1]], TG, TGI, pI},
    gEMT[vv_, pr_, m_, lam_] := Module[{A, Bq, ls = gLs[pr, m, lam, 0]},
      A = Table[gDot[pr["bar"], gMatVec[vv["gamLow"][[mu]], pr["Dpsi"][[nu]]]], {mu, 8}, {nu, 8}];
      Bq = Table[gDot[gRowMat[pr["Dbar"][[mu]], vv["gamLow"][[nu]]], pr["psi"]], {mu, 8}, {nu, 8}];
      Table[gAdd[{gScale[-1/4, gAdd[{A[[mu, nu]], A[[nu, mu]], gNeg[Bq[[mu, nu]]], gNeg[Bq[[nu, mu]]]}]], gScale[vv["g"][[mu, nu]], ls]}], {mu, 8}, {nu, 8}]];
    parts = gParts[v1, gP, gDP, gQ, gDQ];
    tr = gTransform[g8, ConstantArray[1, 8], "linear", False];
    pI = gParts[v1, Sequence @@ tr];
    TG = gEMT[v1, parts, mS, lamS]; TGI = gEMT[v1, pI, -mS, -lamS];
    <|"pairEMTVanishesAll64" -> AllTrue[Flatten[MapThread[gZeroQ[gAdd[{#1, #2}]] &, {TG, TGI}, 2]], TrueQ],
      "EMTNonzeroComponents" -> Count[Flatten[Map[gZeroQ, TG, {2}]], False],
      "symmetric" -> AllTrue[Flatten[Table[gEqualQ[TG[[mu, nu]], TG[[nu, mu]]], {mu, 8}, {nu, 8}]], TrueQ]|>];
  addMeas["M4_pairEMTGrassmannG1point1", emtG];
  addCheck["MA_M4_pairEMTG1_grassmann", emtG["pairEMTVanishesAll64"] && emtG["EMTNonzeroComponents"] === 64 && emtG["symmetric"]];
];

(* exact inertia of a Hermitian matrix (all eigenvalues real: Descartes' rule is exact) *)
hermInertia[m_] := Module[{x, cl, cln, ch},
  ch[l_] := Count[Partition[Sign[l], 2, 1], {s1_, s2_} /; s1 =!= s2];
  cl = Select[CoefficientList[Expand[CharacteristicPolynomial[m, x]], x], # =!= 0 &];
  cln = Select[CoefficientList[Expand[CharacteristicPolynomial[m, x] /. x -> -x], x], # =!= 0 &];
  {ch[cl], ch[cln], Length[m] - ch[cl] - ch[cln]}];

(* one-particle level of the good sector (flat, k5 = k6 = k7 = 0), Stage-1 section 10.6 *)
checkM4Krein[] := Module[{ks, h, hermR, En, proj, ok, ePlus, ePlusM, gramP, gramPM, gramImg, imgSpan},
  ks = Table[Symbol["Dirac16ComplexMatterAntimatter`Private`k" <> ToString[j]], {j, 0, 3}];
  En = Symbol["Dirac16ComplexMatterAntimatter`Private`energyE"];
  hermR[m_] := Transpose[m] /. Complex[a_, b_] :> Complex[a, -b];
  h[m_] := -I m G[4] - G[4].Sum[ks[[j + 1]] G[j], {j, 0, 3}];
  proj[m_, s_] := (id16 + s h[m]/En)/2;
  ePlus = NullSpace[(h[1] /. Thread[ks -> 0]) - id16]; ePlusM = NullSpace[(h[-1] /. Thread[ks -> 0]) - id16];
  gramP = Conjugate[ePlus].Bm.Transpose[ePlus]; gramPM = Conjugate[ePlusM].Bm.Transpose[ePlusM];
  gramImg = Conjugate[ePlus.g8].Bm.Transpose[ePlus.g8];
  imgSpan = MatrixRank[ePlusM] === 8 && MatrixRank[Join[ePlusM, (g8.#) & /@ ePlus]] === 8;
  ok = <|
    "gamma8 h_k(m) gamma8 = h_k(-m)" -> zeroE[g8.h[mS].g8 - h[-mS]],
    "h_k(m)^2 = (m^2 + k^2) I" -> zeroE[h[mS].h[mS] - (mS^2 + ks.ks) id16],
    "h_k(m) Hermitian (real m, k)" -> zeroE[hermR[h[mS]] - h[mS]],
    "[h_k(m), B] = 0" -> zeroE[h[mS].Bm - Bm.h[mS]],
    "gamma8 P_+-(m) gamma8 = P_+-(-m) (E^2 = m^2 + k^2)" -> (zeroE[g8.proj[mS, 1].g8 - proj[-mS, 1]] && zeroE[g8.proj[mS, -1].g8 - proj[-mS, -1]]),
    "gamma8 B gamma8 = -B (Krein norm of the image = - Krein norm)" -> (g8.Bm.g8 === -Bm),
    "rest: gamma8 E_+(m=1) = E_+(m=-1)" -> imgSpan,
    "rest: B-form on E_+(1) has signature (4,4)" -> (hermInertia[gramP] === {4, 4, 0}),
    "rest: B-form on E_+(-1) has signature (4,4)" -> (hermInertia[gramPM] === {4, 4, 0}),
    "rest: Gram(gamma8 E_+(1)) = - Gram(E_+(1))" -> zeroE[gramImg + gramP],
    (* canonical generators: for {Psi, Psi^dagger} = G one has [Psi, Psi^dagger X Psi] = G X Psi *)
    "plus field, G = B: B.(B h_k(m)) = h_k(m) and B.B = 1 (H_+ and Q_+ generate x4-evolution and the phase)" ->
      (zeroE[Bm.Bm.h[mS] - h[mS]] && zeroE[Bm.Bm - id16]),
    "image field, G = -B: (-B).(B h_k(-m)) = -h_k(-m) (H[Psi_-; -m] generates the reversed x4-evolution)" ->
      zeroE[(-Bm).(Bm.h[-mS]) + h[-mS]],
    "image field, G = -B: (-B).B = -1 (Q[Psi_-] generates the inverse phase)" -> zeroE[(-Bm).Bm + id16],
    "gamma8 (B h_k(-m)) gamma8 = -B h_k(m) (H[gamma8 Psi; -m] = -H[Psi; m], so -H[Psi_-; -m] = +H_+)" ->
      zeroE[g8.Bm.h[-mS].g8 + Bm.h[mS]]|>;
  addMeas["M4_kreinOneParticle", <|"checks" -> ok,
    "statement" -> "one-particle level of the good sector: gamma^8 maps the positive- (negative-) energy eigenspace of h_k(m) onto the positive- (negative-) energy eigenspace of h_k(-m) (energy sign preserved) and reverses the Krein norm u^dagger B u of every vector; the charge density Psi^dagger B Psi of the image configuration is minus that of the original. Canonical generators (matrix level): with the image anticommutator -B, the L_{-m,-lambda} Hamiltonian H[Psi_-; -m] generates the reversed x4-evolution and Q[Psi_-] the inverse phase, so the image field's own x4-generator is -H[Psi_-; -m] = +H_+ and its own U(1) generator is -Q[Psi_-] = +Q_+: the image field is the same quantum system as Psi_+, with the same energy and charge. The Fock-level statements are cited from the Stage-5 pairing report (PAIR_T1krein) as PROVISIONAL (Stage 5 not gated)."|>];
  addCheck["MA_M4_kreinOneParticle", AllTrue[Values[ok], TrueQ]];
];

(* the Krein-level particle/antiparticle mapping of Stage 5 (read only; cited as PROVISIONAL while Stage 5 is not gated) *)
stage5Krein[root_String] := Module[{fRep, fTh, rep, th, checks, kreinChecks, final, pick, sha},
  fRep = FileNameJoin[{root, "artifacts", "dirac16complex", "pair-creation", "wolfram-pairing-report.json"}];
  fTh = FileNameJoin[{root, "artifacts", "dirac16complex", "pair-creation", "pairing-theory.json"}];
  sha[f_] := ToLowerCase[FileHash[f, "SHA256", All, "HexString"]];
  If[! FileExistsQ[fRep] || ! FileExistsQ[fTh],
    Return[<|"status" -> "OPEN", "reason" -> "the Stage-5 pairing report (artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json and pairing-theory.json) is not present; only the field-level result (M4: j -> -j, pair charge 0, pair T_{mu nu} = 0) is stated",
      "reportPresent" -> FileExistsQ[fRep], "theoryPresent" -> FileExistsQ[fTh]|>]];
  rep = Quiet[Import[fRep, "RawJSON"]]; th = Quiet[Import[fTh, "RawJSON"]];
  If[! AssociationQ[rep] || ! AssociationQ[th] || ! AssociationQ[rep["checks"]],
    Return[<|"status" -> "OPEN", "reason" -> "the Stage-5 pairing files are present but not parseable"|>]];
  checks = rep["checks"];
  kreinChecks = KeySelect[checks, StringStartsQ[#, "PAIR_T1krein"] &];
  final = Length[checks] > 0 && AllTrue[Values[checks], TrueQ] && Length[kreinChecks] > 0;
  pick = Association[Flatten[Join[
      KeyValueMap[If[StringContainsQ[#1, "krein", IgnoreCase -> True], {#1 -> #2}, {}] &, th],
      KeyValueMap[Function[{k1, v1}, If[AssociationQ[v1], KeyValueMap[If[StringContainsQ[#1, "krein", IgnoreCase -> True], {(k1 <> "." <> #1) -> #2}, {}] &, v1], {}]], th]]]];
  If[! final,
    Return[<|"status" -> "OPEN", "reason" -> "the Stage-5 pairing report is present but not final (not every check true, or no PAIR_T1krein checks)",
      "failedChecks" -> Keys[Select[checks, ! TrueQ[#] &]], "kreinCheckCount" -> Length[kreinChecks],
      "reportSha256" -> sha[fRep], "theorySha256" -> sha[fTh]|>]];
  <|"status" -> "PROVISIONAL: cited from the Stage-5 pairing report (all of its checks true); OPEN until the Stage-5 gate passes (the files carry no finality flag)",
    "kreinChecks" -> kreinChecks, "kreinTheory" -> pick, "reportSha256" -> sha[fRep], "theorySha256" -> sha[fTh],
    "reportProducer" -> rep["producer"]|>];

(* ================================================================== *)
(* 9. M5: the conditional scenario (hypotheses H1-H3) and its exact implication *)
(* ================================================================== *)
checkM5[stage5_Association] := Module[{t, qp, qm, rules, total, dqm, ok, kreinNote},
  t = Symbol["Dirac16ComplexMatterAntimatter`Private`time"];
  qp = Symbol["Dirac16ComplexMatterAntimatter`Private`Qplus"];
  (* H1 with M4: the partner universe is the gamma^8 image, whose charge is minus the charge at every x4 *)
  qm = Function[s, -qp[s]];
  (* M1: dQ_+/dx4 = 0 *)
  rules = {Derivative[1][qp][t] -> 0};
  total = Simplify[qp[t] + qm[t]];
  dqm = D[qm[t], t] /. rules;
  ok = total === 0 && dqm === 0 && TrueQ[$checks["MA_M4_pairEMTAndCurrentG1_commuting"]] && TrueQ[$checks["MA_M4_currentFlipG1_grassmann"]] &&
    TrueQ[$checks["MA_M1_noetherIdentity_grassmann_G1"]] && TrueQ[$checks["MA_M1_noetherIdentity_commuting_G1"]];
  kreinNote = If[KeyExistsQ[stage5, "kreinTheory"] && AssociationQ[stage5["kreinTheory"]["T1krein"]],
    <|"source" -> "Stage-5 pairing report (PAIR_T1krein, all Stage-5 checks true)",
      "imageField" -> Lookup[stage5["kreinTheory"]["T1krein"], "imageField", "absent"],
      "independentQuantisation" -> Lookup[stage5["kreinTheory"]["T1krein"], "independentQuantisation", "absent"],
      "consequenceForM5" -> "the charge cancellation Q_+ + Q_- = 0 of the implication holds for the pair (Psi_+, Psi_- = gamma^8 Psi_+) in which the second member is the gamma^8 image field, which carries the Krein metric -B (it is canonically a field of -L_{-m,-lambda}; energy -|eps| and charge -1 per quantum). If instead the -M universe is quantised independently with its own positive (J = B) structure, its quanta carry charge +1 and energy +|eps|: the cancellation is then NOT automatic and would require an additional assumption on the state of the -M universe. H1 must therefore be read in the first (image-field) sense."|>,
    <|"source" -> "none: the Stage-5 Krein-level result is OPEN", "consequenceForM5" -> "only the field-level statement is used; which Fock states of the -M universe the image corresponds to is OPEN"|>];
  addMeas["M5_implication", <|
    "hypotheses" -> <|
      "H1" -> "ASSUMPTION (not derived): our universe is one member of a gamma^8 pair (Psi_+ with (m, lambda), Psi_- = gamma^8 Psi_+ with (-m, -lambda)) created together; no creation process, rate or amplitude is computed anywhere in this repository",
      "H2" -> "ASSUMPTION (not derived): the creation assigns Q_+ = -Q_- != 0; the relation Q_- = -Q_+ follows from H1 and M4, the value Q_+ != 0 is not computed",
      "H3" -> "ASSUMPTION (not derivable): the dirac16complex U(1) charge is identified with baryon number B (or B - L); the theory contains no Standard-Model baryons, quarks or leptons"|>,
    "implication" -> "IF H1, H2, H3 THEN Q_+(x4) + Q_-(x4) = 0 at every x4 (M4 pointwise: sqrt|g| j^4[gamma^8 Psi] = - sqrt|g| j^4[Psi]), each Q_+- is separately conserved (M1), and the excess B_+ = Q_+ seen in one member is exactly compensated by B_- = -Q_+ in the other: a global symmetry with local asymmetry. The pair also carries T^pair_{mu nu} = 0 (M4, classical bilinears).",
    "symbolicCheck" -> <|"Q_+ + Q_- simplifies to" -> toStr[total], "dQ_-/dx4 given dQ_+/dx4 = 0" -> toStr[dqm]|>,
    "notPredicted" -> "the observed baryon-to-photon ratio eta ~ 6e-10 is NOT predicted; nothing here computes the magnitude or the sign of Q_+",
    "kreinLevelCaveat" -> kreinNote,
    "status" -> "the implication is proved (it is elementary given M1 and M4); the scenario itself is a hypothesis, not a result"|>];
  addCheck["MA_M5_implication", ok];
];

(* ================================================================== *)
(* 10. theory export and entry point                                   *)
(* ================================================================== *)

(* JSON-ready form: exact rationals as "p/q", Gaussian rationals as {"re", "im"}, recorded
   floating-point data kept as numbers, anything symbolic as its InputForm string *)
jsonReady[x_Association] := Association[KeyValueMap[(If[StringQ[#1], #1, toStr[#1]] -> jsonReady[#2]) &, x]];
jsonReady[x_List] := jsonReady /@ x;
jsonReady[x_Integer] := x;
jsonReady[x_Real] := x;
jsonReady[x_String] := x;
jsonReady[True] := True;
jsonReady[False] := False;
jsonReady[x_Rational] := ratStr[x];
jsonReady[Complex[a_, b_]] := {jsonReady[a], jsonReady[b]};
jsonReady[x_Missing] := "missing";
jsonReady[x_] := toStr[x];

buildTheory[stage5_Association] := Module[{sum = $theory["M2_symmetrySummary"], rows = $theory["M2_classificationRows"], th},
  th = <|
    "schemaVersion" -> 1,
    "producer" -> "wolfram/Dirac16ComplexMatterAntimatter.wl (D16MARun) via scripts/verify_dirac16complex_matter_antimatter.wls",
    "title" -> "Matter and antimatter in the dirac16complex theory: what can be proved (exact Wolfram results, M1-M5)",
    "honestyRule" -> "The statement 'the theory solves the matter-antimatter problem' is NOT proved and cannot be proved: within the theory as built the Lagrangian L1 is exactly U(1) invariant for every U (both statistics), the charge Q is conserved in every gravitational field, so no dynamics of the theory creates a net charge inside one universe (Sakharov's first condition fails for this charge). Everything below is either an exact theorem with machine checks or an explicitly labelled hypothesis.",
    "conventions" -> <|"indices" -> "zero-based; x4 = evolution time; eta = diag(+1,+1,+1,+1,-1,-1,-1,-1)",
      "gammas" -> "gamma^a = notebook T16^A[a] (exact fixture algebra-fixture.json), real signed permutation matrices",
      "C" -> "C = sigma16 = gamma^0 gamma^1 gamma^2 gamma^3 (real symmetric); Psibar = Psi^dagger C", "B" -> "B = -i C gamma^4",
      "chirality" -> "gamma^8 = gamma^0 ... gamma^7 = diag(-I8, +I8); P_-+ = (1 -+ gamma^8)/2",
      "lagrangian" -> "L1 = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m Psibar Psi - U(Psibar Psi) ], U = (lambda/2) S^2 by default",
      "current" -> "j^mu = Psibar gamma^mu Psi (spec normalization); Hermitian current J^mu = -i j^mu; Gaussian normal gauge J^4 = Psi^dagger B Psi",
      "statistics" -> "dirac16complex: Grassmann-odd components (exact Grassmann algebra of this package); dirac16complex00: commuting components (exact symbols)",
      "discreteMaps" -> "(M, R, type): Psi'(x) = M Psi(Rx) (linear) or M conj(Psi)(Rx) (antilinear), R = the set of reflected directions; in a curved field the frame e_mu^a -> e_mu^b R_b^a is reflected instead (same metric)"|>,
    "M1" -> <|
      "theorem" -> "For both statistics and every potential U(S) (commuting: any function; Grassmann: any polynomial, S^17 = 0), L1 is invariant under Psi -> e^{i alpha} Psi. Noether current: j^mu = Psibar gamma^mu Psi (L[e^{i alpha(x)} Psi] - L[Psi] = i sqrt|g| d_mu alpha j^mu). Off shell, in every gravitational field: d_mu(sqrt|g| j^mu) = sqrt|g| (Ebar Psi + Psibar E), E = gamma^mu D_mu Psi - (m + U') Psi, Ebar = (D_mu Psibar) gamma^mu + (m + U') Psibar; hence nabla_mu j^mu = 0 on shell and Q = integral sqrt|g| J^{x4} d^7x is conserved.",
      "consequence" -> "no process described by L1 changes Q inside one universe; the Kohn-Sham states of Stages 4/5 carry the fixed net number N imposed through the chemical potential",
      "chargeMatrixB" -> jmat[Bm],
      "machineChecks" -> {"MA_M1_u1InvarianceCommutingGenericU_flat", "MA_M1_u1InvarianceCommutingGenericU_G1", "MA_M1_u1InvarianceGrassmann_G1",
        "MA_M1_grassmannPotentialsPolynomialAndNeutral", "MA_M1_noetherCurrentLocalPhase_commuting_G1", "MA_M1_noetherCurrentLocalPhase_grassmann_G1",
        "MA_M1_noetherCurrentFormula_grassmann_G1", "MA_M1_noetherCurrentFormula_commuting_G1", "MA_M1_noetherIdentity_grassmann_G1",
        "MA_M1_noetherIdentity_commuting_G1", "MA_M1_negativeControlNotebookConnection", "MA_M1_onShellConservation_G1",
        "MA_M1_chargeDensityMatrix", "MA_M1_ksFixedNetNumberRecorded", "MA_M1_stage1ChecksCited"},
      "stage1Checks" -> $meas["M1_stage1ChecksCited"]|>,
    "M2" -> <|
      "conjugationIntertwiners" -> <|"condition" -> "gamma^a M = eta M conj(gamma^a)", "etaPlus" -> jmat[id16], "etaMinus" -> jmat[g8]|>,
      "transposeIntertwiners" -> <|"condition" -> "gamma^a M = zeta M gamma^{aT} (Psi -> M Psibar^T)", "zetaMinus" -> jmat[C16], "zetaPlus" -> jmat[g8.C16]|>,
      "statisticsSign" -> $meas["M2_statisticsSign"],
      "rules" -> $meas["M2_classificationSummary"],
      "classificationRows" -> rows,
      "namedMaps" -> $theory["M2_namedMaps"],
      "symmetrySummary" -> sum,
      "chargeReversingExactSymmetriesPreservingTimeOrientation" -> $theory["M2_chargeReversingExactSymmetriesPreservingTimeOrientation"],
      "canonicalStructure" -> $meas["M2_canonicalStructure"],
      "answer" -> <|
        "commuting (dirac16complex00)" -> "C (Psi -> conj(Psi)) is an exact symmetry of L1 and reverses j; no P with a single space-like reflection and no CP of that type is exact for m != 0; T (x4) is exact (linear and antilinear); the full-inversion CPT is exact",
        "grassmann (dirac16complex)" -> "no constant C is an exact symmetry for m != 0 (the canonical unitary C8: Psi -> gamma^8 Psi^{dagger T} maps L_{m,lambda} -> L_{-m,lambda}, the mirror theory); P with one space-like reflection maps m -> -m or L -> -L_{m,-lambda}; CP (C8 P_b for b = 0..3, C8 P3) is an exact unitary symmetry that reverses the charge; T (x4, linear substitution, antiunitary implementation) is exact; the full-inversion antilinear CPT is not, CP3T (x1..x4) is",
        "sakharov2" -> "for both statistics there is an exact symmetry that reverses the charge and preserves the time orientation (commuting: C; Grassmann: CP): Sakharov's second condition (C and CP violation) fails"|>|>,
    "M3" -> <|
      "invariantMassForms" -> <|"CPminus" -> jmat[C16.Pm], "CPplus" -> jmat[C16.Pp], "statement" -> $meas["M3_spinInvariantMassForms"]["statement"]|>,
      "pinCovariantForms" -> <|"C" -> <|"matrix" -> jmat[C16], "character" -> "-n(u)"|>, "Cgamma8" -> <|"matrix" -> jmat[C16.g8], "character" -> "+n(u)"|>,
        "characters" -> $meas["M3_pinCharacterForms"]["characters"]|>,
      "kineticForms" -> $meas["M3_kineticInvariantForms"],
      "survival" -> $meas["M3_survival"],
      "pinCharactersMajoranaTerms" -> $meas["M3_pinCharactersMajoranaTerms"],
      "notebookLg" -> $meas["M3_notebookLg"],
      "extraGrassmannQuartic" -> $meas["M3_extraGrassmannQuartic"],
      "classificationStatement" -> "This is a classification of the U(1)-violating (charge 2) local terms allowed by Spin_0(4,4) and Pin(4,4); it is what the theory would need to ADD to meet Sakharov's first condition. None of these terms is present in L1, and nothing here claims that such a term is present, natural or sufficient."|>,
    "M4" -> <|
      "fieldLevel" -> "Psi -> gamma^8 Psi: j^mu -> -j^mu in every gravitational field (both statistics); for Psi_- = gamma^8 Psi_+ with (-m, -lambda): Q_+ + Q_- = 0 and T^pair_{mu nu} = 0 (classical bilinears); gamma^8 maps solutions of EL_{m,lambda} to solutions of EL_{-m,-lambda}",
      "matrixFacts" -> $meas["M4_matrixFacts"],
      "kreinOneParticle" -> $meas["M4_kreinOneParticle"],
      "kreinLevelStage5" -> stage5|>,
    "M5" -> $meas["M5_implication"],
    "sakharovInputs" -> <|
      "condition1 (B violation)" -> <|"status" -> "fails in the theory as built: L1 is exactly U(1) invariant and Q is conserved (M1)",
        "wouldNeed" -> "a U(1)-violating term (M3): commuting components: Psi^T C P_+- Psi, Psi^T C gamma^a d_a Psi; Grassmann components: no bilinear mass term exists, Psi^T C gamma^8 gamma^a d_a Psi or a quartic such as Q4 (charge 4)"|>,
      "condition2 (C and CP violation)" -> <|"commuting" -> If[TrueQ[sum["commuting"]["C (R empty, antilinear) exact"]], "fails: C is exact", "C not exact"],
        "grassmann" -> If[TrueQ[sum["grassmann"]["CP (one space-like reflection, antilinear) exact"]], "fails: CP (C8 P_b, C8 P3) is exact", "CP not exact"]|>,
      "condition3 (departure from equilibrium)" -> "not addressed by any theorem here; with conditions 1 and 2 failing exactly, a departure from equilibrium cannot generate a net charge inside one universe"|>|>;
  th];

D16MAExpectedCheckCount = 44;

D16MARun[root_String] := Module[{rows, stage5, res},
  $checks = <||>; $meas = <||>; $theory = <||>; geoCache = <||>;
  res = Catch[
    logT["algebra and fixture"];
    checkAlgebra[FileNameJoin[{root, "artifacts", "dirac16complex", "arbitrary-field", "algebra-fixture.json"}]];
    logT["M1: U(1) invariance"]; checkM1Invariance[];
    logT["M1: Noether current and identity"]; checkM1Noether[];
    logT["M1: on-shell conservation"]; checkM1OnShell[];
    logT["M1: charge"]; checkM1Charge[]; checkM1KS[root]; checkM1Stage1[root];
    logT["M2: intertwiners"]; checkM2Intertwiners[]; checkM2StatisticsSign[];
    logT["M2: classification"]; rows = checkM2Classification[];
    logT["M2: all maps at the Lagrangian level (flat)"]; checkM2FlatAll[rows];
    logT["M2: named maps and the curved field G1"]; checkM2Named[rows];
    logT["M2: summary and canonical structure"]; checkM2Summary[rows];
    logT["M3: invariant forms"]; checkM3Forms[]; checkM3Survival[]; checkM3PinKinetic[]; checkM3NotebookLg[];
    logT["M3: extra quartic"]; checkM3Quartic[];
    logT["M4"]; checkM4[]; checkM4Krein[];
    stage5 = stage5Krein[root];
    addMeas["M4_kreinLevelStatus", stage5["status"]];
    addMeas["M4_kreinLevelConsistency", If[KeyExistsQ[stage5, "kreinChecks"],
      <|"stage5ImageAnticommutatorMinusB" -> Lookup[stage5["kreinChecks"], "PAIR_T1krein_imageAnticommutatorMinusB", "absent"],
        "thisPackageGamma8BGamma8MinusB" -> TrueQ[$meas["M4_kreinOneParticle"]["checks"]["gamma8 B gamma8 = -B (Krein norm of the image = - Krein norm)"]],
        "thisPackageEnergySignPreserved" -> TrueQ[$meas["M4_kreinOneParticle"]["checks"]["gamma8 P_+-(m) gamma8 = P_+-(-m) (E^2 = m^2 + k^2)"]]|>,
      "not compared (Stage-5 Krein-level result OPEN)"]];
    logT["M5"]; checkM5[stage5];
    "ok", d16maErr];
  If[res =!= "ok", addMeas["internalError", toStr[res]]; addCheck["MA_internalError", False]];
  If[Length[$checks] =!= D16MAExpectedCheckCount, addMeas["checkCountMismatch", {Length[$checks], D16MAExpectedCheckCount}]];
  <|"checks" -> $checks, "measurements" -> jsonReady[$meas], "theory" -> jsonReady[If[res === "ok", buildTheory[stage5], <||>]]|>];

End[];
EndPackage[];
