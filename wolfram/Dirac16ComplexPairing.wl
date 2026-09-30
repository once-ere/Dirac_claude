(* ::Package:: *)

(* ::Title:: *)
(* Dirac16ComplexPairing.wl *)

(* ::Text:: *)
(* Stage 5 of dirac16complex: the exact {+M, -M} pairing theorems T1, T2, T3 of
   STAGE5_SPEC section 5 and the statistics sign of section 4, for BOTH fields:
   dirac16complex (anticommuting, Grassmann-odd components, second quantised in a
   Krein space) and dirac16complex00 (commuting, classical c-number components).

   Conventions: CONTRACT.md with errata (zero-based indices, x4 = time,
   eta = diag(+,+,+,+,-,-,-,-), gamma^a = [[0, taubar_a],[tau_a, 0]] of the exact
   fixture, C = sigma16 = gamma^0 gamma^1 gamma^2 gamma^3, Psibar = Psi^dagger C,
   B = -i C gamma^4, gamma^8 = gamma^0 ... gamma^7 = diag(-I8, +I8),
   Omega_mu = (1/8) omega_{mu ab}[gamma^a, gamma^b]); STAGE4_SPEC with errata E4.3-E4.12
   (the static primordial field in the proper coordinate y, the eight 2x2 blocks,
   the expectation-value rule <Psi^dagger X Psi> = u^dagger B X u).

   Sections (check-name prefixes):
     PAIR_algebra     fixture, gamma^8 / C / B facts, the parities of every bilinear
                      matrix that occurs in L, the field equations, T_mu nu and j^mu.
     PAIR_T1generic   T1 as a polynomial identity in COMPLETELY GENERIC independent
                      symbols for the vielbein, the spin connection, the metric and
                      the field jets (hence for every gravitational field): L, both
                      field equations, all 36 components of T_mu nu, the current.
     PAIR_T1grassmann T1 for Grassmann-odd components (a Grassmann algebra with 288
                      odd generators) at a point of the general non-diagonal test
                      vielbein G1: L, the Dirac operator (with the cubic term), T_mu nu,
                      j^mu; gamma^8 acts as the chirality-sign automorphism.
     PAIR_T1jets      T1 with the Stage-1 exact jet geometry (G1, three points):
                      L, T_mu nu, j^mu, the field equations as order-1 jets, on-shell
                      solutions and their images, conservation, T^pair = 0; the
                      equivalent form "vielbein sign flip e -> -e"; the exact symmetry
                      (gamma^8, e -> -e).
     PAIR_T1krein     the Krein metric B -> -B: canonical anticommutator of the image
                      field, an exact finite-mode Krein-Fock model (expectation rule
                      for particles and holes, the image field, the independently
                      quantised -m theory), the normal-ordered Hamiltonian.
     PAIR_T2frame     Pin(4,4) reflections u: characters chi(u) = -n(u), the twisted
                      and untwisted frame reflections of the vielbein (G1 jets), the
                      maps of L, T_mu nu, j, S; the reflections of character -1 give
                      (m, lambda) -> (-m, lambda) with L -> +L; gamma^8 x untwisted.
     PAIR_T2z2        the coordinate action in the Z2 primordial field (static,
                      y chart, generic spinor fields of all eight coordinates):
                      Psi'(y) = gamma^0 Psi(-y) maps mass m(y) to -m(-y) with the same
                      lambda; EMT pull-back; "Z2 symmetric iff the mass function is
                      odd"; P_B = i gamma^0 gamma^8 flips lambda at the field level.
     PAIR_T3block     the maps on the exact 2x2 block basis of kohn-sham-theory.json:
                      gamma^8 = c sigma2 between blocks (j,s2,s3) and (-j,s2,s3),
                      gamma^1 = c sigma1 inside each block, gamma^0 = sigma3; the maps
                      of the block ODE, the block Hamiltonian, the parity conditions,
                      the bag angle, the current and density matrices, the potentials.
     PAIR_T3ks        the Kohn-Sham level: equivariance of the discretised KS
                      operator and invariance of the Mermin functional (both
                      statistics, symbolic statistics sign), the image rule (T1:
                      E -> -E, T -> -T), exact k = 0 spectra, the untransformed-BC
                      control (tip zero mode, first-order splitting c(-M) != c(M)).
     PAIR_T3emt       the 16-component energy-momentum tensor of a KS orbital in the
                      static primordial field: gamma^8 X_{mu nu}(-m, -M_eff) gamma^8 =
                      -X_{mu nu}(m, M_eff) for all 64 components; standard rule -> +T,
                      image rule -> -T; cross-check with the Stage-4 formulas.
     PAIR_stat        the Wick sign: exact fermionic Fock space (pure and mixed
                      quasi-free states), exact bosonic thermal moments, exact
                      classical Gaussian moments, the random-phase deviation; E_HF for
                      both statistics, filled shell, uniform gas, LDA potentials,
                      M_eff^00 = m + (17/16) lambda S_p; positivity of the implied
                      covariance.
     PAIR_totals      the pair totals (field level and KS level, both pair types).

   Exactness: integer, rational and Gaussian-rational arithmetic and exact symbolic
   algebra; zero tests are exact (Expand / Together, numerator identically zero).
   No floating point decides any check.

   Reused machinery (read only): wolfram/Dirac16ComplexGeometry.wl (public API:
   D16GeoFrameJet, D16GeoJetGeometry, D16GeoFieldJets, D16GeoLagrangianJets,
   D16GeoEMTJets, D16GeoEMTDivergence, D16GeoSolveOnShell, D16GeoG1Frame,
   D16GeoRandomRationals); the exact fixture algebra-fixture.json; the exact Stage-4
   block basis in artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json.

   Public entry point: D16PairRun[repoRoot] returns an Association with keys
   "checks", "measurements" and "theory" (exported to pairing-theory.json). *)

If[! MemberQ[$Packages, "Dirac16Complex`Geometry`"],
  Get[FileNameJoin[{DirectoryName[$InputFileName], "Dirac16ComplexGeometry.wl"}]]];

BeginPackage["Dirac16ComplexPairing`"];

D16PairRun::usage = "D16PairRun[repoRoot] runs every Stage-5 exact pairing check. It returns an Association with keys \"checks\" (name -> True|False), \"measurements\" (name -> value) and \"theory\" (exact data for pairing-theory.json).";
D16PairGammas::usage = "D16PairGammas[] returns the eight 16x16 gamma matrices gamma^0..gamma^7 (notebook split-octonion basis).";

Begin["`Private`"];

(* ================================================================== *)
(* 0. bookkeeping                                                      *)
(* ================================================================== *)

$checks = <||>; $meas = <||>; $theory = <||>;
addCheck[name_String, val_] := Module[{v = TrueQ[val]},
  $checks[name] = v;
  If[! v, Print["  CHECK FAILED: ", name]];
  v];
addMeas[name_String, val_] := ($meas[name] = val);
logT[msg__] := Print["[", DateString[{"Hour", ":", "Minute", ":", "Second"}], "] ", msg];
toStr[e_] := Block[{$Context = "Dirac16ComplexPairing`Private`",
    $ContextPath = {"System`", "Dirac16ComplexPairing`Private`"}},
  ToString[e, InputForm, PageWidth -> Infinity]];
ratStr[x_Integer] := ToString[x];
ratStr[x_Rational] := ToString[Numerator[x]] <> "/" <> ToString[Denominator[x]];
ratStr[x_] := Throw[{"ratStr", x}, d16pairErr];
gq[x_] := {ratStr[Re[x]], ratStr[Im[x]]};
gqMat[m_List] := Map[gq, m, {2}];
gqVec[v_List] := gq /@ v;
allZero[x_] := AllTrue[Flatten[{x}], (# === 0) &];
zeroT[x_] := AllTrue[Flatten[{x}], (Together[#] === 0) &];
zeroE[x_] := AllTrue[Flatten[{x}], (Expand[#] === 0) &];

(* aliases of the public Stage-1 geometry API (context Dirac16Complex`Geometry`) *)
geoFrameJet = Dirac16Complex`Geometry`D16GeoFrameJet;
geoJetGeometry = Dirac16Complex`Geometry`D16GeoJetGeometry;
geoFieldJets = Dirac16Complex`Geometry`D16GeoFieldJets;
geoLagJets = Dirac16Complex`Geometry`D16GeoLagrangianJets;
geoEMTJets = Dirac16Complex`Geometry`D16GeoEMTJets;
geoEMTDiv = Dirac16Complex`Geometry`D16GeoEMTDivergence;
geoSolveOnShell = Dirac16Complex`Geometry`D16GeoSolveOnShell;
geoG1Frame = Dirac16Complex`Geometry`D16GeoG1Frame;
geoRandom = Dirac16Complex`Geometry`D16GeoRandomRationals;
geoGammas = Dirac16Complex`Geometry`D16GeoGammas;

(* ================================================================== *)
(* 1. gamma matrices (CONTRACT section 1) and the facts used           *)
(* ================================================================== *)

id2 = IdentityMatrix[2]; id4 = IdentityMatrix[4]; id8 = IdentityMatrix[8]; id16 = IdentityMatrix[16];
zero16 = ConstantArray[0, {16, 16}]; zero8 = ConstantArray[0, {8, 8}];
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
g8 = Fold[Dot, id16, gamL];
Bm = -I C16.G[4];
BC = Bm.C16;
sig1 = {{0, 1}, {1, 0}}; sig2 = {{0, -I}, {I, 0}}; sig3 = {{1, 0}, {0, -1}};
herm[m_] := ConjugateTranspose[m];
(* conjugate transpose of a matrix whose symbols are all real *)
hermR[m_] := Transpose[m] /. Complex[a_, b_] :> Complex[a, -b];
chiSignOfComponent[a_Integer] := If[a < 8, -1, 1];  (* gamma^8 = diag(-I8, +I8) *)
D16PairGammas[] := gamL;

upperBlock[M_] := M[[1 ;; 8, 1 ;; 8]]; lowerBlock[M_] := M[[9 ;; 16, 9 ;; 16]];
offUpper[M_] := M[[1 ;; 8, 9 ;; 16]]; offLower[M_] := M[[9 ;; 16, 1 ;; 8]];
chiralBlockDiagonalQ[M_] := offUpper[M] === zero8 && offLower[M] === zero8;
chiralOffDiagonalQ[M_] := upperBlock[M] === zero8 && lowerBlock[M] === zero8;

checkAlgebra[fixFile_] := Module[{fx, Bfx, Sfx, oddMats, pairsAB, uBu},
  fx = Import[fixFile, "RawJSON"];
  Bfx = fx["B"]["real"] + I fx["B"]["imag"];
  Sfx = Association[Table[{s["a"], s["b"]} -> Map[If[StringQ[#], ToExpression[#], #] &, s["matrix"], {2}], {s, fx["S"]}]];
  pairsAB = Flatten[Table[{a, b}, {a, 0, 6}, {b, a + 1, 7}], 1];
  addCheck["PAIR_algebra_fixtureMatches", fx["gamma"] === gamL && fx["C"] === C16 && fx["chirality"] === g8 && Bfx === Bm &&
    Length[Sfx] === 28 && AllTrue[pairsAB, KeyExistsQ[Sfx, #] && Sfx[#] === Sab @@ # &] && geoGammas === gamL];
  addCheck["PAIR_algebra_clifford", AllTrue[Flatten[Table[G[a].G[b] + G[b].G[a] === 2 etaM[[a + 1, b + 1]] id16, {a, 0, 7}, {b, 0, 7}]], TrueQ]];
  (* the facts used in every proof below *)
  addCheck["PAIR_algebra_gamma8Properties", g8 === DiagonalMatrix[Join[ConstantArray[-1, 8], ConstantArray[1, 8]]] &&
    herm[g8] === g8 && g8.g8 === id16 && AllTrue[Range[0, 7], g8.G[#] === -G[#].g8 &] && g8.C16 === C16.g8 &&
    AllTrue[pairsAB, g8.(Sab @@ #) === (Sab @@ #).g8 &]];
  addCheck["PAIR_algebra_CProperties", C16 === G[0].G[1].G[2].G[3] && Transpose[C16] === C16 && Conjugate[C16] === C16 && C16.C16 === id16 &&
    AllTrue[Range[0, 7], Transpose[C16.G[#]] === -C16.G[#] && Conjugate[C16.G[#]] === C16.G[#] &]];
  addCheck["PAIR_algebra_BProperties", herm[Bm] === Bm && Bm.Bm === id16 && g8.Bm.g8 === -Bm && C16.Bm === Bm.C16 && BC === -I G[4] &&
    Sort[Eigenvalues[Bm]] === Join[ConstantArray[-1, 8], ConstantArray[1, 8]]];
  (* gamma^dagger C = -C gamma for every frame index (used for Pin elements) *)
  addCheck["PAIR_algebra_gammaDaggerC", AllTrue[Range[0, 7], herm[G[#]].C16 === -C16.G[#] &]];
  (* every bilinear matrix of the kinetic term, of the connection terms, of T_mu nu and of j^mu *)
  oddMats = Join[Table[C16.G[a], {a, 0, 7}],
    Flatten[Table[C16.G[a].(Sab @@ ab), {a, 0, 7}, {ab, pairsAB}], 1],
    Flatten[Table[C16.(Sab @@ ab).G[a], {a, 0, 7}, {ab, pairsAB}], 1]];
  addMeas["algebra_oddBilinearMatrixCount", Length[oddMats]];
  addCheck["PAIR_algebra_bilinearParities", Length[oddMats] === 456 && AllTrue[oddMats, g8.#.g8 === -# &] && g8.C16.g8 === C16 &&
    herm[g8].C16 === C16.g8 && g8.Bm.g8 === -Bm && g8.BC.g8 === -BC];
  (* structural reason: in the notebook basis C and every S^{ab} are chirality-block diagonal, every gamma^a block off-diagonal *)
  addCheck["PAIR_algebra_chiralBlockStructure", chiralBlockDiagonalQ[C16] && AllTrue[pairsAB, chiralBlockDiagonalQ[Sab @@ #] &] &&
    AllTrue[Range[0, 7], chiralOffDiagonalQ[G[#]] &] && chiralOffDiagonalQ[Bm]];
  (* Krein metric under the basic reflections u = gamma^a: {u Psi, (u Psi)^dagger} = u B u^dagger *)
  uBu = Table[Which[G[a].Bm.herm[G[a]] === Bm, 1, G[a].Bm.herm[G[a]] === -Bm, -1, True, 0], {a, 0, 7}];
  addMeas["algebra_uBudagger_sign_for_u_gamma0to7", uBu];
  addCheck["PAIR_algebra_kreinUnderBasicReflections", uBu === {1, 1, 1, 1, 1, -1, -1, -1}];
  $theory["algebra"] = <|
    "facts" -> <|
      "gamma8" -> "gamma^8 = gamma^0 gamma^1 ... gamma^7 = diag(-I8, +I8) is Hermitian, (gamma^8)^2 = 1, anticommutes with every gamma^a, commutes with C and with every S^{ab} (hence with every Omega_mu, in any gravitational field)",
      "C" -> "C = gamma^0 gamma^1 gamma^2 gamma^3 is real symmetric, C^2 = 1; C gamma^a is real antisymmetric (anti-Hermitian) for a = 0..7; gamma^a dagger C = -C gamma^a for every a",
      "B" -> "B = -i C gamma^4 is Hermitian, B^2 = 1, spectrum (+1)^8 (-1)^8, [B, C] = 0, BC = -i gamma^4; gamma^8 B gamma^8 = -B",
      "bilinearParities" -> "gamma^8 X gamma^8 = -X for all 456 matrices X in {C gamma^a, C gamma^a S^{bc}, C S^{bc} gamma^a} (every matrix of the kinetic, connection, energy-momentum and current bilinears) and gamma^8 C gamma^8 = +C (mass term, S)",
      "chiralBlockStructure" -> "in the notebook basis C and every S^{ab} are block diagonal in (Psi_0..Psi_7 | Psi_8..Psi_15) and every gamma^a is block off-diagonal; gamma^8 multiplies the upper components by -1: every kinetic, connection, current and EMT-bilinear monomial pairs an upper with a lower component (sign -1), every monomial of S = Psibar Psi pairs equal chiralities (sign +1). For Grassmann-odd components gamma^8 is therefore the algebra automorphism theta_a -> chi(a) theta_a of the Grassmann algebra (chi = -1 for a < 8, +1 for a >= 8), compatible with all products and with the ordering of odd factors.",
      "kreinUnderReflections" -> "u B u^dagger = +B for u = gamma^0..gamma^4 and -B for u = gamma^5, gamma^6, gamma^7 (measured); gamma^8 B gamma^8 = -B"|>|>;];
