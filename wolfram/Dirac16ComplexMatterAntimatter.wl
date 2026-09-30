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
   charge flip j -> -j under gamma^8 and the pair totals; the Krein-level mapping is taken
   from the Stage-5 pairing report if that report is present and final, otherwise it is
   recorded as OPEN), and M5 (the implication H1 & H2 & H3 => total charge of the pair
   vanishes, with H1-H3 recorded as unproved hypotheses).

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
