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
    "maxAbsDeviationReference" -> If[refRows === {}, Missing[], Max[DeleteMissing[Lookup[refRows, "maxAbsDeviation", Missing[]]]]],
    "maxAbsDeviationRust" -> If[rustRows === {}, Missing[], Max[DeleteMissing[Lookup[rustRows, "maxAbsDeviation", Missing[]]]]]|>];
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
