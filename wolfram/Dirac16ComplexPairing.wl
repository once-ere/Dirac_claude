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
     PAIR_T1primordial T1 in the Stage-2 primordial field (notebook chart, arbitrary
                      a4(t), generic spinor fields of all eight coordinates): L, the Dirac
                      operator, all 64 components of T_mu nu, j^mu.
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

(* ================================================================== *)
(* 2. PAIR_T1generic: T1 as a polynomial identity in generic symbols   *)
(* ================================================================== *)

(* Every quantity is written with INDEPENDENT symbols: eu[a,mu] = e_a^mu (for gamma^mu),
   el[mu,a] = e_mu^a (for gamma_mu), om[mu,a,b] = omega_{mu ab} (a < b, antisymmetric
   extension), gg[mu,nu] = g_{mu nu}, and the field jets ps[i] = Psi_i, pb[i] =
   Psi^dagger_i, dps[mu,i], dpb[mu,i].  An identity that holds as a polynomial identity in
   these symbols holds a fortiori for the constrained values (e_a^mu the inverse of
   e_mu^a, omega the Levi-Civita spin connection, g = e eta e^T) of EVERY gravitational
   field, at every point, off shell.  The bilinears keep the order Psi^dagger ... Psi, so
   the same identities hold for Grassmann-odd components (the only quartic term, S^2, is
   checked in PAIR_T1grassmann). *)
checkT1Generic[] := Module[{p, q, dp, dq, gU, gD, Om, pieces, Ls, Eq, Eqb, Tb, jc, pc0, pc8, lsSum, okT, pairsMN, nKin, nOm, t0},
  t0 = AbsoluteTime[];
  p = Array[ps, 16, 0]; q = Array[pb, 16, 0];
  dp = Table[Array[dps[mu, #] &, 16, 0], {mu, 0, 7}]; dq = Table[Array[dpb[mu, #] &, 16, 0], {mu, 0, 7}];
  gU = Table[Sum[eu[a, mu] G[a], {a, 0, 7}], {mu, 0, 7}];
  gD = Table[Sum[el[mu, a] etaD[[a + 1]] G[a], {a, 0, 7}], {mu, 0, 7}];
  Om = Table[Sum[om[mu, a, b] Sab[a, b], {a, 0, 6}, {b, a + 1, 7}], {mu, 0, 7}];
  pieces[pp_, qq_, dpp_, dqq_] := Module[{bar = qq.C16, Dp, Db},
    Dp = Table[dpp[[mu]] + Om[[mu]].pp, {mu, 8}];
    Db = Table[dqq[[mu]].C16 - bar.Om[[mu]], {mu, 8}];
    <|"psi" -> pp, "bar" -> bar, "Dp" -> Dp, "Db" -> Db, "S" -> Expand[bar.pp],
      "kin" -> Total[Table[Expand[(1/2) bar.gU[[mu]].Dp[[mu]]] - Expand[(1/2) Db[[mu]].gU[[mu]].pp], {mu, 8}]]|>];
  Ls[pc_, mm_, ll_] := pc["kin"] - mm pc["S"] - (ll/2) pc["S"]^2;
  Eq[pc_, mm_, ll_] := Expand[Total[Table[Expand[gU[[mu]].pc["Dp"][[mu]]], {mu, 8}]] - Expand[(mm + ll pc["S"]) pc["psi"]]];
  Eqb[pc_, mm_, ll_] := Expand[Total[Table[Expand[pc["Db"][[mu]].gU[[mu]]], {mu, 8}]] + Expand[(mm + ll pc["S"]) pc["bar"]]];
  Tb[pc_, mu_, nu_] := Expand[-(1/4) pc["bar"].gD[[mu]].pc["Dp"][[nu]]] + Expand[-(1/4) pc["bar"].gD[[nu]].pc["Dp"][[mu]]] +
      Expand[(1/4) pc["Db"][[mu]].gD[[nu]].pc["psi"]] + Expand[(1/4) pc["Db"][[nu]].gD[[mu]].pc["psi"]];
  jc[pc_, mu_] := Expand[pc["bar"].gU[[mu]].pc["psi"]];
  pc0 = pieces[p, q, dp, dq];
  pc8 = pieces[g8.p, q.g8, (g8.#) & /@ dp, (#.g8) & /@ dq];
  nKin = Length[pc0["kin"]]; nOm = Length[Select[List @@ pc0["kin"], ! FreeQ[#, om] &]];
  addMeas["T1generic_kineticMonomials", nKin];
  addMeas["T1generic_connectionMonomials", nOm];
  addCheck["PAIR_T1generic_nontrivial", nOm > 0 && nKin - nOm > 0 && Length[pc0["S"]] === 16 && ! FreeQ[pc0["kin"], dps] &&
    Expand[Sum[gU[[mu]].Om[[mu]], {mu, 8}]] =!= zero16];
  addCheck["PAIR_T1generic_scalarInvariantKineticOdd", Expand[pc8["S"] - pc0["S"]] === 0 && Expand[pc8["kin"] + pc0["kin"]] === 0];
  lsSum = Expand[pc8["kin"] + pc0["kin"]] + Expand[Ls[pc8, m, lam] - pc8["kin"] + Ls[pc0, -m, -lam] - pc0["kin"]];
  addCheck["PAIR_T1generic_lagrangian", lsSum === 0];
  (* the naive form L_m[gamma^8 Psi] = -L_{-m}[Psi] at fixed lambda fails by exactly -lambda S^2 *)
  addCheck["PAIR_T1generic_naiveFixedLambdaFails", Expand[pc8["kin"] + pc0["kin"]] + Expand[Ls[pc8, m, lam] - pc8["kin"] + Ls[pc0, -m, lam] - pc0["kin"] + lam pc0["S"]^2] === 0 && pc0["S"] =!= 0];
  addCheck["PAIR_T1generic_fieldEquation", zeroE[Eq[pc8, -m, -lam] + g8.Eq[pc0, m, lam]] && ! zeroE[Eq[pc0, m, lam]]];
  addCheck["PAIR_T1generic_conjugateFieldEquation", zeroE[Eqb[pc8, -m, -lam] + Eqb[pc0, m, lam].g8]];
  (* T_{mu nu} = Tb_{mu nu} + gg[mu,nu] Ls: the Ls part is lsSum (zero), the bilinear part is checked for all 36 pairs *)
  pairsMN = Flatten[Table[{mu, nu}, {mu, 8}, {nu, mu, 8}], 1];
  okT = AllTrue[pairsMN, (Tb[pc8, #[[1]], #[[2]]] + Tb[pc0, #[[1]], #[[2]]] + gg[#[[1]], #[[2]]] lsSum) === 0 &];
  addCheck["PAIR_T1generic_emtAll36", okT && Length[pairsMN] === 36 && Expand[Tb[pc0, 1, 5]] =!= 0];
  addCheck["PAIR_T1generic_current", AllTrue[Range[8], (jc[pc8, #] + jc[pc0, #]) === 0 &]];
  addCheck["PAIR_T1generic_connectionCommutesWithGamma8", AllTrue[Om, Expand[g8.# - #.g8] === zero16 &] &&
    Expand[g8.Sum[gU[[mu]].Om[[mu]], {mu, 8}] + Sum[gU[[mu]].Om[[mu]], {mu, 8}].g8] === zero16];
  logT["T1generic seconds: ", Round[AbsoluteTime[] - t0]];];

(* ================================================================== *)
(* 3. a small exact Grassmann algebra                                  *)
(* ================================================================== *)

(* element: Association  sortedGeneratorList -> coefficient.  Generator ids:
   Psi_a -> 1 + a, Psi^dagger_a -> 17 + a, d_mu Psi_a -> 33 + 16 mu + a,
   d_mu Psi^dagger_a -> 161 + 16 mu + a  (a = 0..15, mu = 0..7); all odd. *)
gClean[x_Association] := Select[Together /@ x, # =!= 0 &];
gFromPairs[pairs_List] := If[pairs === {}, <||>, gClean[GroupBy[pairs, First -> Last, Total]]];
gAdd[xs___Association] := gFromPairs[Flatten[(KeyValueMap[List, #] &) /@ {xs}, 1]];
gScale[c_, x_Association] := If[c === 0, <||>, gClean[(c #) & /@ x]];
gMul[x_Association, y_Association] := Module[{acc},
  acc = Reap[KeyValueMap[Function[{kx, vx}, KeyValueMap[Function[{ky, vy},
        If[Intersection[kx, ky] === {}, With[{mm = Join[kx, ky]}, Sow[{Sort[mm], Signature[mm] vx vy}]]]], y]], x]][[2]];
  If[acc === {}, <||>, gFromPairs[First[acc]]]];
gGen[id_Integer] := <|{id} -> 1|>;
idPsi[a_] := 1 + a; idPsib[a_] := 17 + a; idDPsi[mu_, a_] := 33 + 16 mu + a; idDPsib[mu_, a_] := 161 + 16 mu + a;
gComponent[id_Integer] := Mod[id - 1, 16];
gBil[rowIds_List, M_, colIds_List] := gFromPairs[Flatten[Table[If[M[[a, b]] === 0, Nothing,
      {Sort[{rowIds[[a]], colIds[[b]]}], Signature[{rowIds[[a]], colIds[[b]]}] M[[a, b]]}], {a, 16}, {b, 16}], 1]];
gLin[M_, colIds_List] := Table[gFromPairs[Table[If[M[[a, b]] === 0, Nothing, {{colIds[[b]]}, M[[a, b]]}], {b, 16}]], {a, 16}];
gAut8[x_Association] := Association[KeyValueMap[#1 -> (Times @@ (chiSignOfComponent[gComponent[#]] & /@ #1)) #2 &, x]];
gZeroQ[x_Association] := Length[gClean[x]] === 0;
gMaxDegree[x_Association] := If[Length[x] === 0, 0, Max[Length /@ Keys[x]]];

(* the complex Lagrangian, the Dirac operator, T_mu nu and j^mu as Grassmann polynomials at a
   point, from the point values gamma^mu (gUv), Omega_mu (Omv), gamma_mu (gLv), g_mu nu (gv) *)
grassTheory[gUv_, Omv_, gLv_, gv_, mm_, ll_] := Module[{rowB, colP, rowDB, colDP, S, kin, Ls, Ed, Tm, jcur, psiBarGD, dBarG},
  rowB = Table[idPsib[a], {a, 0, 15}]; colP = Table[idPsi[a], {a, 0, 15}];
  rowDB = Table[idDPsib[mu, a], {mu, 0, 7}, {a, 0, 15}]; colDP = Table[idDPsi[mu, a], {mu, 0, 7}, {a, 0, 15}];
  S = gBil[rowB, C16, colP];
  kin = gScale[1/2, gAdd @@ Flatten[Table[{gBil[rowB, C16.gUv[[mu]], colDP[[mu]]], gBil[rowB, C16.gUv[[mu]].Omv[[mu]], colP],
        gScale[-1, gBil[rowDB[[mu]], C16.gUv[[mu]], colP]], gBil[rowB, C16.Omv[[mu]].gUv[[mu]], colP]}, {mu, 8}]]];
  Ls = gAdd[kin, gScale[-mm, S], gScale[-ll/2, gMul[S, S]]];
  Ed = Module[{lin = gLin[Sum[gUv[[mu]].Omv[[mu]], {mu, 8}], colP], dlin = Table[gLin[gUv[[mu]], colDP[[mu]]], {mu, 8}]},
    Table[gAdd @@ Join[Table[dlin[[mu, a]], {mu, 8}], {lin[[a]], gScale[-mm, gGen[colP[[a]]]], gScale[-ll, gMul[S, gGen[colP[[a]]]]]}], {a, 16}]];
  (* Psibar gamma_mu D_nu Psi and (D_mu Psibar) gamma_nu Psi *)
  psiBarGD[mu_, nu_] := gAdd[gBil[rowB, C16.gLv[[mu]], colDP[[nu]]], gBil[rowB, C16.gLv[[mu]].Omv[[nu]], colP]];
  dBarG[mu_, nu_] := gAdd[gBil[rowDB[[mu]], C16.gLv[[nu]], colP], gScale[-1, gBil[rowB, C16.Omv[[mu]].gLv[[nu]], colP]]];
  Tm = Table[If[nu < mu, Null, gAdd[gScale[-1/4, gAdd[psiBarGD[mu, nu], psiBarGD[nu, mu], gScale[-1, dBarG[mu, nu]], gScale[-1, dBarG[nu, mu]]]],
       gScale[gv[[mu, nu]], Ls]]], {mu, 8}, {nu, 8}];
  jcur = Table[gBil[rowB, C16.gUv[[mu]], colP], {mu, 8}];
  <|"S" -> S, "kin" -> kin, "Ls" -> Ls, "E" -> Ed, "T" -> Tm, "j" -> jcur|>];

(* ================================================================== *)
(* 4. PAIR_T1jets and PAIR_T1grassmann: the Stage-1 exact jet geometry *)
(* ================================================================== *)

(* test geometry G1 of Stage 1: the general non-diagonal polynomial vielbein
   e_mu^a = delta + P(x) at three rational points; masses and couplings as in Stage 1 *)
xcs = {xc0, xc1, xc2, xc3, xc4, xc5, xc6, xc7};
g1Points = {{1/7, -2/9, 1/5, 3/11, -1/13, 2/17, -3/19, 1/23}, {-1/3, 1/4, 2/7, -1/5, 1/6, -2/11, 1/9, 3/13},
   {2/9, 1/8, -1/7, 1/10, -3/14, 1/12, 2/15, -1/16}};
g1Masses = {3/7, -2/5, 5/9}; g1Couplings = {5/11, 7/13, -3/8};
g1FrameJet[k_Integer] := geoFrameJet[geoG1Frame[xcs], xcs, Thread[xcs -> g1Points[[k]]]];
jetGeo[fj_] := geoJetGeometry[fj, "Curvature" -> False];
negFrameJet[fj_] := {-fj[[1]], -fj[[2]], -fj[[3]]};
transFrameJet[fj_, M_] := {fj[[1]].M, (#.M) & /@ fj[[2]], Map[#.M &, fj[[3]], {2}]};

(* deterministic exact random field jets {Psi, d Psi, dd Psi, Psi^dagger, d Psi^dagger, dd Psi^dagger} *)
randSym2[seed_] := Module[{r = geoRandom[seed, 36*16], k = 0, arr = ConstantArray[0, {8, 8, 16}]},
  Do[With[{v = r[[16 k + 1 ;; 16 k + 16]]}, arr[[i, j]] = v; arr[[j, i]] = v; k++], {i, 8}, {j, i, 8}];
  arr];
randField[seed_] := {geoRandom[seed, 16], Partition[geoRandom[seed + 1, 128], 16], randSym2[seed + 2],
   geoRandom[seed + 3, 16], Partition[geoRandom[seed + 4, 128], 16], randSym2[seed + 5]};
(* Psi -> M Psi, Psi^dagger -> Psi^dagger M^dagger (constant M) on all jets *)
mapField[M_, data_] := {M.data[[1]], (M.#) & /@ data[[2]], Map[M.# &, data[[3]], {2}],
   data[[4]].herm[M], (#.herm[M]) & /@ data[[5]], Map[#.herm[M] &, data[[6]], {2}]};

(* order-1 jets {value, {d_0 value, ..., d_7 value}} *)
jmul[f_, a_, b_] := {f[a[[1]], b[[1]]], Table[f[a[[2, l]], b[[1]]] + f[a[[1]], b[[2, l]]], {l, 8}]};
jpart[jj_, mu_] := {jj[[1, mu]], jj[[2, All, mu]]};
(* E = gamma^mu D_mu Psi - (m + lambda S) Psi and Ebar = (D_mu Psibar) gamma^mu + (m + lambda S) Psibar as jets *)
fieldEqJets[geo_, lag_, mm_, ll_] := Module[{gam = geo["gamma"], e1, e2},
  e1 = Sum[jmul[Dot, jpart[gam, mu], lag["Dpsi"][[mu]]], {mu, 8}] - mm lag["psi"] - ll jmul[Times, lag["S"], lag["psi"]];
  e2 = Sum[jmul[Dot, lag["Dbar"][[mu]], jpart[gam, mu]], {mu, 8}] + mm lag["bar"] + ll jmul[Times, lag["S"], lag["bar"]];
  {e1, e2}];
currentJets[geo_, lag_] := Table[jmul[Dot, jmul[Dot, lag["bar"], jpart[geo["gamma"], mu]], lag["psi"]], {mu, 8}];

checkT1Jets[] := Module[{res = <||>, acc, fj, geo, geoN, mm, ll, data, data8, fld, fld8, lag, lag8, lagMM, lagN, lagN8, T0, T8,
   e1, e2, f1, f2, solData, okS, lagS, lagS8, solData8, TS, TS8, gt, gtM, gtN, pairsUp, t0 = AbsoluteTime[]},
  acc[name_, v_] := (res[name] = TrueQ[Lookup[res, name, True]] && TrueQ[v]);
  pairsUp = Flatten[Table[{mu, nu}, {mu, 8}, {nu, mu, 8}], 1];
  Do[
   fj = g1FrameJet[k]; geo = jetGeo[fj]; mm = g1Masses[[k]]; ll = g1Couplings[[k]];
   data = randField[1000 k + 17]; data8 = mapField[g8, data];
   fld = geoFieldJets @@ data; fld8 = geoFieldJets @@ data8;
   lag = geoLagJets[geo, fld, mm, ll]; lag8 = geoLagJets[geo, fld8, -mm, -ll]; lagMM = geoLagJets[geo, fld, -mm, -ll];
   (* Lagrangian density L = sqrt|g| L_s as an order-1 jet *)
   acc["L", zeroT[lag8["L"] + lag["L"]] && ! zeroT[lag["L"]]];
   acc["S", zeroT[lag8["S"] - lag["S"]] && zeroT[lag8["kinetic"] + lag["kinetic"]] && zeroT[lag8["KE"] + lag["KE"]] && ! zeroT[lag["kinetic"]]];
   acc["naive", ! zeroT[geoLagJets[geo, fld8, -mm, ll]["L"] + lag["L"]]];
   T0 = geoEMTJets[geo, lag]; T8 = geoEMTJets[geo, lag8];
   acc["T", zeroT[T0 + T8] && ! zeroT[T0]];
   acc["j", zeroT[currentJets[geo, lag8] + currentJets[geo, lag]] && ! zeroT[currentJets[geo, lag]]];
   {e1, e2} = fieldEqJets[geo, lag, mm, ll]; {f1, f2} = fieldEqJets[geo, lag8, -mm, -ll];
   acc["E", zeroT[f1[[1]] + g8.e1[[1]]] && zeroT[Table[f1[[2, l]] + g8.e1[[2, l]], {l, 8}]] &&
     zeroT[f2[[1]] + e2[[1]].g8] && zeroT[Table[f2[[2, l]] + e2[[2, l]].g8, {l, 8}]] && ! zeroT[e1[[1]]]];
   acc["Omega", zeroT[Table[g8.geo["Omega"][[1, mu]] - geo["Omega"][[1, mu]].g8, {mu, 8}]] &&
     zeroT[Table[g8.geo["Omega"][[2, l, mu]] - geo["Omega"][[2, l, mu]].g8, {l, 8}, {mu, 8}]] &&
     ! zeroT[Sum[geo["gamma"][[1, mu]].geo["Omega"][[1, mu]], {mu, 8}]]];
   (* on shell: Psi solves EL_{m,lambda} at the point to first order; its image solves EL_{-m,-lambda} *)
   {solData, okS} = geoSolveOnShell[geo, data, mm, ll];
   lagS = geoLagJets[geo, geoFieldJets @@ solData, mm, ll];
   solData8 = mapField[g8, solData];
   lagS8 = geoLagJets[geo, geoFieldJets @@ solData8, -mm, -ll];
   TS = geoEMTJets[geo, lagS]; TS8 = geoEMTJets[geo, lagS8];
   acc["onShell", okS && zeroT[fieldEqJets[geo, lagS, mm, ll]] && zeroT[fieldEqJets[geo, lagS8, -mm, -ll]] &&
     ! zeroT[fieldEqJets[geo, geoLagJets[geo, geoFieldJets @@ solData8, mm, ll], mm, ll]]];
   acc["conservation", zeroT[geoEMTDiv[geo, TS]] && zeroT[geoEMTDiv[geo, TS8]] && ! zeroT[Map[First, TS, {2}]]];
   acc["pair", zeroT[TS + TS8] && zeroT[lagS["L"] + lagS8["L"]] && zeroT[currentJets[geo, lagS] + currentJets[geo, lagS8]]];
   (* the same map as a sign flip of the vielbein: e -> -e leaves g, sqrt|g| and Omega unchanged and flips gamma^mu *)
   geoN = jetGeo[negFrameJet[fj]];
   acc["frameNeg", zeroT[geoN["g"] - geo["g"]] && zeroT[geoN["gamma"] + geo["gamma"]] && zeroT[geoN["Omega"] - geo["Omega"]] &&
     zeroT[geoN["sqrtg"] - geo["sqrtg"]] && zeroT[geoN["gammaLower"] + geo["gammaLower"]]];
   lagN = geoLagJets[geoN, fld, mm, ll];
   acc["negFrameIsT1", zeroT[lagN["L"] + lagMM["L"]] && zeroT[geoEMTJets[geoN, lagN] + geoEMTJets[geo, lagMM]]];
   lagN8 = geoLagJets[geoN, fld8, mm, ll];
   acc["symmetry", zeroT[lagN8["L"] - lag["L"]] && zeroT[geoEMTJets[geoN, lagN8] - T0]];
   If[k === 1,
    addMeas["T1jets.p1.Svalue", toStr[lag["S"][[1]]]];
    (* Grassmann-odd components at the same point (values) *)
    gt = grassTheory[geo["gamma"][[1]], geo["Omega"][[1]], geo["gammaLower"][[1]], geo["g"][[1]], mm, ll];
    gtM = grassTheory[geo["gamma"][[1]], geo["Omega"][[1]], geo["gammaLower"][[1]], geo["g"][[1]], -mm, -ll];
    gtN = grassTheory[geo["gamma"][[1]], geo["Omega"][[1]], geo["gammaLower"][[1]], geo["g"][[1]], -mm, ll];
    addMeas["T1grassmann_monomials_Ls", Length[gt["Ls"]]];
    addMeas["T1grassmann_monomials_S2", Length[gMul[gt["S"], gt["S"]]]];
    addCheck["PAIR_T1grassmann_nontrivial", gMaxDegree[gt["Ls"]] === 4 && Length[gt["kin"]] > 0 && Length[gMul[gt["S"], gt["S"]]] > 0 &&
      AllTrue[gt["E"], gMaxDegree[#] === 3 &] && AllTrue[pairsUp, Length[gt["T"][[#[[1]], #[[2]]]]] > 0 &]];
    addCheck["PAIR_T1grassmann_scalarEvenKineticOdd", gZeroQ[gAdd[gAut8[gt["S"]], gScale[-1, gt["S"]]]] && gZeroQ[gAdd[gAut8[gt["kin"]], gt["kin"]]]];
    addCheck["PAIR_T1grassmann_lagrangian", gZeroQ[gAdd[gAut8[gt["Ls"]], gtM["Ls"]]]];
    addCheck["PAIR_T1grassmann_naiveFixedLambdaFails", ! gZeroQ[gAdd[gAut8[gt["Ls"]], gtN["Ls"]]]];
    addCheck["PAIR_T1grassmann_diracOperator", AllTrue[Range[16], gZeroQ[gAdd[gAut8[gtM["E"][[#]]], gScale[chiSignOfComponent[# - 1], gt["E"][[#]]]]] &]];
    addCheck["PAIR_T1grassmann_emt", AllTrue[pairsUp, gZeroQ[gAdd[gAut8[gt["T"][[#[[1]], #[[2]]]]], gtM["T"][[#[[1]], #[[2]]]]]] &]];
    addCheck["PAIR_T1grassmann_current", AllTrue[Range[8], gZeroQ[gAdd[gAut8[gt["j"][[#]]], gt["j"][[#]]]] &]]],
   {k, 1, 3}];
  addCheck["PAIR_T1jets_lagrangian", res["L"]];
  addCheck["PAIR_T1jets_scalarEvenKineticOdd", res["S"]];
  addCheck["PAIR_T1jets_naiveFixedLambdaFails", res["naive"]];
  addCheck["PAIR_T1jets_emt", res["T"]];
  addCheck["PAIR_T1jets_current", res["j"]];
  addCheck["PAIR_T1jets_fieldEquations", res["E"]];
  addCheck["PAIR_T1jets_connectionCommutes", res["Omega"]];
  addCheck["PAIR_T1jets_onShellImage", res["onShell"]];
  addCheck["PAIR_T1jets_conservationBoth", res["conservation"]];
  addCheck["PAIR_T1jets_pairEMTAndCurrentVanish", res["pair"]];
  addCheck["PAIR_T1jets_vielbeinSignFlipGeometry", res["frameNeg"]];
  addCheck["PAIR_T1jets_vielbeinSignFlipIsT1", res["negFrameIsT1"]];
  addCheck["PAIR_T1jets_gamma8WithFrameSignIsSymmetry", res["symmetry"]];
  logT["T1jets seconds: ", Round[AbsoluteTime[] - t0]];];

(* ================================================================== *)
(* 5. PAIR_T1krein: the Krein metric B -> -B and expectation values    *)
(* ================================================================== *)

(* exact Fock space of d fermionic modes (Jordan-Wigner); the first basis vector is the
   empty state, sm = {{0,1},{0,0}} annihilates *)
jwOps[d_] := Module[{sz = {{1, 0}, {0, -1}}, sm = {{0, 1}, {0, 0}}, i2 = IdentityMatrix[2]},
  Table[KroneckerProduct @@ Join[ConstantArray[sz, a - 1], {sm}, ConstantArray[i2, d - a]], {a, d}]];

(* Finite-mode Krein-Fock model of the flat-space rest sector (m = +1): h(m) = -i m gamma^4
   (the single-particle operator of CONTRACT section 8 at k = 0), [h, B] = 0.  Four modes:
   joint eigenvectors of (h, B) with (eps, beta) = (+1,+1), (+1,-1), (-1,+1), (-1,-1).
   Krein CAR {b_n, b_n^K} = beta_n realised on a Hilbert Fock space: b_n = a_n,
   b_n^K = beta_n a_n^* (a^* the Hilbert adjoint).  Truncated field Psi = sum_n u_n b_n,
   Psi^K = sum_n u_n^* b_n^K, so {Psi_a, Psi^K_b} = (B P)_ab with P = sum_n u_n u_n^dagger.
   Sea: the negative-energy modes 3, 4 filled; normal ordering = subtraction of the sea
   expectation value. *)
checkT1Krein[] := Module[{h0, h0m, cls, us, betas, epss, as, ads, idF, psiOp, psiKOp, P4, car, bilOp, vac, sea, st, ex, noEx, Ms, ruleOK,
   psiI, psiKI, carI, HP, HI, QP, QI, SP, SI, ws, psiJ, psiKJ, P4J, carJ, sval, t0 = AbsoluteTime[]},
  h0 = -I G[4]; h0m = I G[4];
  addCheck["PAIR_T1krein_restHamiltonians", h0.h0 === id16 && herm[h0] === h0 && h0.Bm === Bm.h0 && g8.h0.g8 === h0m && h0m.Bm === Bm.h0m];
  cls = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
  epss = cls[[All, 1]]; betas = cls[[All, 2]];
  us = Table[Module[{P = (id16 + c[[1]] h0).(id16 + c[[2]] Bm)/4, col, v},
     col = SelectFirst[Range[16], P[[All, #]] =!= ConstantArray[0, 16] &]; v = P[[All, col]];
     v/Sqrt[Conjugate[v].v]], {c, cls}];
  addCheck["PAIR_T1krein_modes", AllTrue[Flatten[Table[Together[Conjugate[us[[i]]].us[[j]]] === If[i == j, 1, 0], {i, 4}, {j, 4}]], TrueQ] &&
    AllTrue[Range[4], zeroT[h0.us[[#]] - epss[[#]] us[[#]]] && zeroT[Bm.us[[#]] - betas[[#]] us[[#]]] &]];
  as = jwOps[4]; ads = herm /@ as; idF = IdentityMatrix[16];
  psiOp = Table[Sum[us[[n, a]] as[[n]], {n, 4}], {a, 16}];
  psiKOp = Table[Sum[Conjugate[us[[n, a]]] betas[[n]] ads[[n]], {n, 4}], {a, 16}];
  P4 = Sum[Outer[Times, us[[n]], Conjugate[us[[n]]]], {n, 4}];
  car[p_, pk_, target_] := AllTrue[Flatten[Table[zeroT[p[[a]].pk[[b]] + pk[[b]].p[[a]] - target[[a, b]] idF] && zeroT[p[[a]].p[[b]] + p[[b]].p[[a]]], {a, 16}, {b, 16}]], TrueQ];
  addCheck["PAIR_T1krein_fieldCAR", car[psiOp, psiKOp, Bm.P4] && Together[P4.P4 - P4] === zero16 && Together[Tr[P4]] === 4];
  bilOp[M_, pk_, p_] := Sum[If[M[[a, b]] === 0, 0 idF, M[[a, b]] pk[[a]].p[[b]]], {a, 16}, {b, 16}];
  vac = UnitVector[16, 1];
  sea = ads[[3]].ads[[4]].vac;
  st = <|"particle1" -> ads[[1]].sea, "particle2" -> ads[[2]].sea, "hole3" -> as[[3]].sea, "hole4" -> as[[4]].sea|>;
  addCheck["PAIR_T1krein_statesNormalised", Conjugate[sea].sea === 1 && AllTrue[Values[st], Conjugate[#].# === 1 &] &&
    AllTrue[as[[1 ;; 2]], #.sea === ConstantArray[0, 16] &] && AllTrue[ads[[3 ;; 4]], #.sea === ConstantArray[0, 16] &]];
  ex[s_, X_] := Together[Conjugate[s].X.s];
  noEx[s_, X_] := Together[ex[s, X] - ex[sea, X]];
  (* the expectation-value rule: particle n: <Psi^K M Psi> = u_n^dagger B M u_n; hole n: -u_n^dagger B M u_n *)
  Ms = <|"C" -> C16, "B" -> Bm, "Bh" -> Bm.h0, "Cgamma4" -> C16.G[4], "BC" -> BC|>;
  ruleOK = AllTrue[Keys[Ms], Function[key, Module[{X = bilOp[Ms[key], psiKOp, psiOp]},
       zeroT[noEx[st["particle1"], X] - Conjugate[us[[1]]].Bm.Ms[key].us[[1]]] && zeroT[noEx[st["particle2"], X] - Conjugate[us[[2]]].Bm.Ms[key].us[[2]]] &&
       zeroT[noEx[st["hole3"], X] + Conjugate[us[[3]]].Bm.Ms[key].us[[3]]] && zeroT[noEx[st["hole4"], X] + Conjugate[us[[4]]].Bm.Ms[key].us[[4]]]]]];
  addCheck["PAIR_T1krein_expectationRule", ruleOK];
  (* positivity of the J = B quantisation: every excitation has energy +1 = |eps|, charge (Psi^K B Psi) +1 for particles, -1 for holes *)
  HP = bilOp[Bm.h0, psiKOp, psiOp]; QP = bilOp[Bm, psiKOp, psiOp]; SP = bilOp[C16, psiKOp, psiOp];
  addCheck["PAIR_T1krein_positiveExcitations", AllTrue[Values[st], noEx[#, HP] === 1 &] &&
    noEx[st["particle1"], QP] === 1 && noEx[st["particle2"], QP] === 1 && noEx[st["hole3"], QP] === -1 && noEx[st["hole4"], QP] === -1];
  sval = Table[noEx[st[key], SP], {key, Keys[st]}];
  addMeas["T1krein_scalarDensity_particle1_particle2_hole3_hole4", toStr[sval]];
  (* the gamma^8 image field Psi_- = gamma^8 Psi (same Fock space, same state) *)
  psiI = Table[Sum[g8[[a, b]] psiOp[[b]], {b, 16}], {a, 16}];
  psiKI = Table[Sum[psiKOp[[b]] g8[[b, a]], {b, 16}], {a, 16}];
  addCheck["PAIR_T1krein_imageAnticommutatorMinusB", car[psiI, psiKI, g8.Bm.P4.g8] && Together[g8.Bm.P4.g8 + Bm.(g8.P4.g8)] === zero16];
  HI = bilOp[Bm.h0m, psiKI, psiI]; QI = bilOp[Bm, psiKI, psiI]; SI = bilOp[C16, psiKI, psiI];
  (* operator identities: H[Psi_-; -m] = -H[Psi; m], charge -> -charge, S -> S *)
  addCheck["PAIR_T1krein_imageOperatorIdentities", zeroT[HI + HP] && zeroT[QI + QP] && zeroT[SI - SP] && ! zeroT[HP]];
  addCheck["PAIR_T1krein_imageExpectationValues", AllTrue[Values[st], noEx[#, HI] === -1 &] &&
    noEx[st["particle1"], QI] === -1 && noEx[st["hole3"], QI] === 1 &&
    AllTrue[Keys[Ms], Function[key, zeroT[noEx[st["particle1"], bilOp[Ms[key], psiKI, psiI]] - Conjugate[g8.us[[1]]].(-Bm).Ms[key].(g8.us[[1]])]]]];
  (* the -m theory quantised independently with its own canonical structure (+B): modes w_n = gamma^8 u_n *)
  ws = (g8.#) & /@ us;
  addCheck["PAIR_T1krein_minusMModes", AllTrue[Range[4], zeroT[h0m.ws[[#]] - epss[[#]] ws[[#]]] && zeroT[Bm.ws[[#]] + betas[[#]] ws[[#]]] &]];
  psiJ = Table[Sum[ws[[n, a]] as[[n]], {n, 4}], {a, 16}];
  psiKJ = Table[Sum[Conjugate[ws[[n, a]]] (-betas[[n]]) ads[[n]], {n, 4}], {a, 16}];
  P4J = Sum[Outer[Times, ws[[n]], Conjugate[ws[[n]]]], {n, 4}];
  addCheck["PAIR_T1krein_independentCARPlusB", car[psiJ, psiKJ, Bm.P4J]];
  addCheck["PAIR_T1krein_independentExpectationValues",
    AllTrue[Values[st], noEx[#, bilOp[Bm.h0m, psiKJ, psiJ]] === 1 &] && noEx[st["particle1"], bilOp[Bm, psiKJ, psiJ]] === 1 &&
    zeroT[noEx[st["particle1"], bilOp[C16, psiKJ, psiJ]] + noEx[st["particle1"], SP]] &&
    AllTrue[Keys[Ms], Function[key, zeroT[noEx[st["particle1"], bilOp[Ms[key], psiKJ, psiJ]] - Conjugate[ws[[1]]].Bm.Ms[key].ws[[1]]]]]];
  logT["T1krein seconds: ", Round[AbsoluteTime[] - t0]];
  $theory["T1krein"] = <|
    "canonical" -> "the canonical anticommutator of dirac16complex in the Gaussian-normal gauge is {Psi, Psi^dagger} = B delta^7/sqrt|g| (Stage 1); for the image Psi_- := gamma^8 Psi_+ it is gamma^8 B gamma^8 = -B: the image field is the canonical field of the Lagrangian -L_{-m,-lambda} = L_{m,lambda}[gamma^8 .] (same field equations as L_{-m,-lambda}, opposite overall sign, opposite Krein metric)",
    "fockModel" -> "four modes of the rest sector (m = 1): joint eigenvectors u_n of h = -i m gamma^4 and B with (eps, beta) = (+1,+1), (+1,-1), (-1,+1), (-1,-1); Krein CAR {b_n, b_n^K} = beta_n realised as b_n = a_n, b_n^K = beta_n a_n^*; sea = modes 3, 4 filled; normal ordering = subtraction of the sea expectation value",
    "expectationRule" -> "one particle in mode u: <:Psi^K M Psi:> = u^dagger B M u; one hole in mode u: -u^dagger B M u (verified for M = C, B, B h, C gamma^4, BC); every excitation has energy |eps| > 0 (the J = B positivity)",
    "imageField" -> "Psi_- = gamma^8 Psi on the same Fock space and state: {Psi_-, Psi_-^K} = -B P_-; operator identities H[Psi_-; -m] = -H[Psi; m] (H = Psi^K B h Psi), Q[Psi_-] = -Q[Psi] (Q = Psi^K B Psi = J^4), S[Psi_-] = S[Psi]; expectation values <Psi_-^K M Psi_-> = u_-^dagger (-B) M u_-, u_- = gamma^8 u: the image universe carries the Krein metric -B, energy -|eps| and charge -1 per quantum. Since gamma^8 acts linearly and pointwise, normal ordering (subtraction of the sea value) commutes with the map: :T_{mu nu}[gamma^8 Psi; -m, -lambda]: = -:T_{mu nu}[Psi; m, lambda]: and :H_-: = -:H_+: as operators.",
    "independentQuantisation" -> "if the -m theory L_{-m,-lambda} is quantised independently with its own canonical structure (+B) and the J = B positive-norm Fock space, its modes are w_n = gamma^8 u_n (same eps, Krein sign -beta_n); a quantum in w has energy +|eps|, charge +1 and scalar density -u^dagger B C u: (E, Q, S) -> (E, Q, -S). Its energy-momentum does NOT cancel that of the +m universe.",
    "consequence" -> "T^pair = 0 at the operator level holds for the pair (Psi_+, Psi_- = gamma^8 Psi_+), whose second member carries the Krein metric -B (it is canonically a field of -L_{-m,-lambda}); an independently quantised -m universe with the positive (J = B) structure has the same energy-momentum as the +m universe (this is the T2-type pairing, see T3)."|>;];

(* ================================================================== *)
(* 6. PAIR_T2frame: Pin(4,4) reflections and their frame actions      *)
(* ================================================================== *)

etaIP[x_, y_] := Sum[etaD[[a]] x[[a]] y[[a]], {a, 8}];
vecSlash[v_] := Sum[v[[a + 1]] G[a], {a, 0, 7}];
(* reflection of the basis vector e_A in the hyperplane orthogonal to k: a rational unit vector with n = eta(e_A, e_A) *)
reflUnit[A_Integer, k_List] := UnitVector[8, A + 1] - 2 etaIP[UnitVector[8, A + 1], k]/etaIP[k, k] k;
(* u gamma^a u^{-1} = sum_c Lambda[[c,a]] gamma^c  (untwisted adjoint action) *)
lambdaOf[u_] := Module[{ui = Inverse[u]}, Table[Tr[G[c].(u.G[a].ui)]/(16 etaD[[c + 1]]), {c, 0, 7}, {a, 0, 7}]];
(* the hyperplane reflection R_v x = x - 2 eta(v,x)/eta(v,v) v as a matrix [[c, a]] *)
reflMatrix[v_] := Table[KroneckerDelta[c, a] - 2 v[[c]] etaD[[a]] v[[a]]/etaIP[v, v], {c, 8}, {a, 8}];

(* For a unit vector u = v_a gamma^a (u^2 = n(u) = eta(v,v) = +-1):
   Pin action on the spinor Psi -> u Psi, Psi^dagger -> Psi^dagger u^dagger;
   frame action on the vielbein e_mu^a (rows mu) by the constant matrix
     untwisted: e -> e.(eta Lambda^T eta), then gamma'^mu = u gamma^mu u^{-1};
     twisted:   e -> -e.(eta Lambda^T eta), then gamma'^mu = -u gamma^mu u^{-1};
   (the metric, sqrt|g| and Omega_mu -> u Omega_mu u^{-1} are the same for both);
   character chi(u) := sign with u^dagger C = chi C u^{-1}. *)
checkT2Frame[] := Module[{units, rows = {}, res = <||>, acc, ref, t0 = AbsoluteTime[]},
  acc[name_, v_] := (res[name] = TrueQ[Lookup[res, name, True]] && TrueQ[v]);
  (* u-independent reference data per G1 point (cached) *)
  ref[k_] := ref[k] = Module[{fj = g1FrameJet[k], geo, data, fld, mm = g1Masses[[k]], ll = g1Couplings[[k]], Lp, LmP, LmM, LpM},
     geo = jetGeo[fj]; data = randField[2000 k + 31]; fld = geoFieldJets @@ data;
     Lp = geoLagJets[geo, fld, mm, ll]; LmP = geoLagJets[geo, fld, -mm, ll]; LmM = geoLagJets[geo, fld, -mm, -ll]; LpM = geoLagJets[geo, fld, mm, -ll];
     <|"fj" -> fj, "geo" -> geo, "data" -> data, "Lp" -> Lp, "LmP" -> LmP, "LmM" -> LmM, "LpM" -> LpM,
       "Tp" -> geoEMTJets[geo, Lp], "TmP" -> geoEMTJets[geo, LmP], "TmM" -> geoEMTJets[geo, LmM], "TpM" -> geoEMTJets[geo, LpM]|>];
  units = Join[Table[{"gamma^" <> ToString[A], UnitVector[8, A + 1]}, {A, 0, 7}],
    {{"spacelikeGeneral", reflUnit[0, {1, 2, -1, 1, 3, -1, 2, 1}]}, {"timelikeGeneral", reflUnit[4, {2, 1, 1, -1, 1, 3, -1, 1}]}}];
  Do[Module[{lab = uu[[1]], v = uu[[2]], n, u, ui, chi, Lam, Mun, Mtw, uBu},
     n = etaIP[v, v]; u = vecSlash[v]; ui = u/n;
     chi = Which[herm[u].C16 === C16.ui, 1, herm[u].C16 === -C16.ui, -1, True, 0];
     Lam = lambdaOf[u];
     uBu = Which[u.Bm.herm[u] === Bm, 1, u.Bm.herm[u] === -Bm, -1, True, 0];
     acc["unit", (n === 1 || n === -1) && u.u === n id16 && ui.u === id16];
     acc["character", chi === -n];
     acc["lambda", AllTrue[Range[0, 7], u.G[#].ui === Sum[Lam[[c + 1, # + 1]] G[c], {c, 0, 7}] &] &&
       Transpose[Lam].etaM.Lam === etaM && Det[Lam] === -1 && Lam === -reflMatrix[v]];
     Mun = etaM.Transpose[Lam].etaM; Mtw = -Mun;
     Do[Module[{fj, geo, geoUn, geoTw, mm = g1Masses[[k]], ll = g1Couplings[[k]], data, fld, fldU, fld8U, Lp, LmP, LmM, LpM, Ltw, Lun, L8un,
         Tp, TmP, TmM, TpM},
        fj = ref[k]["fj"]; geo = ref[k]["geo"];
        geoUn = jetGeo[transFrameJet[fj, Mun]]; geoTw = jetGeo[transFrameJet[fj, Mtw]];
        acc["frames", zeroT[geoUn["g"] - geo["g"]] && zeroT[geoTw["g"] - geo["g"]] && zeroT[geoUn["sqrtg"] - geo["sqrtg"]] && zeroT[geoTw["sqrtg"] - geo["sqrtg"]] &&
          zeroT[Table[geoUn["gamma"][[1, mu]] - u.geo["gamma"][[1, mu]].ui, {mu, 8}]] && zeroT[Table[geoTw["gamma"][[1, mu]] + u.geo["gamma"][[1, mu]].ui, {mu, 8}]] &&
          zeroT[Table[geoUn["Omega"][[1, mu]] - u.geo["Omega"][[1, mu]].ui, {mu, 8}]] && zeroT[Table[geoTw["Omega"][[1, mu]] - u.geo["Omega"][[1, mu]].ui, {mu, 8}]] &&
          zeroT[Table[geoTw["Omega"][[2, l, mu]] - u.geo["Omega"][[2, l, mu]].ui, {l, 8}, {mu, 8}]]];
        data = ref[k]["data"];
        fldU = geoFieldJets @@ mapField[u, data]; fld8U = geoFieldJets @@ mapField[g8.u, data];
        Lp = ref[k]["Lp"]; LmP = ref[k]["LmP"]; LmM = ref[k]["LmM"]; LpM = ref[k]["LpM"];
        Tp = ref[k]["Tp"]; TmP = ref[k]["TmP"]; TmM = ref[k]["TmM"]; TpM = ref[k]["TpM"];
        Ltw = geoLagJets[geoTw, fldU, mm, ll]; Lun = geoLagJets[geoUn, fldU, mm, ll]; L8un = geoLagJets[geoUn, fld8U, mm, ll];
        acc["scalarAndCurrent", zeroT[Ltw["S"] - chi Lp["S"]] && zeroT[currentJets[geoTw, Ltw] + chi currentJets[geo, Lp]]];
        If[chi === -1,
         acc["twistedSpacelike", zeroT[Ltw["L"] - LmP["L"]] && zeroT[geoEMTJets[geoTw, Ltw] - TmP] && ! zeroT[Ltw["L"] - Lp["L"]]];
         acc["untwistedSpacelike", zeroT[Lun["L"] + LpM["L"]] && zeroT[geoEMTJets[geoUn, Lun] + TpM] && ! zeroT[Lun["L"] + Lp["L"]]];
         acc["gamma8Untwisted", zeroT[L8un["L"] - LmP["L"]] && zeroT[geoEMTJets[geoUn, L8un] - TmP]],
         acc["twistedTimelike", zeroT[Ltw["L"] + LmM["L"]] && zeroT[geoEMTJets[geoTw, Ltw] + TmM]];
         acc["untwistedTimelike", zeroT[Lun["L"] - Lp["L"]] && zeroT[geoEMTJets[geoUn, Lun] - Tp]];
         acc["gamma8UntwistedTimelike", zeroT[L8un["L"] + LmM["L"]] && zeroT[geoEMTJets[geoUn, L8un] + TmM]]]],
      {k, If[StringStartsQ[lab, "gamma"], {1}, {1, 2}]}];
     AppendTo[rows, <|"u" -> lab, "vector" -> (ratStr /@ v), "norm" -> ratStr[n], "character" -> ratStr[chi], "uBudaggerSign" -> ratStr[uBu],
        "twistedFrameResult" -> If[chi === -1, "L_{m,lambda}[e R_u, u Psi] = +L_{-m,lambda}[e, Psi]; T -> +T; S -> -S; j -> +j", "L_{m,lambda}[e R_u, u Psi] = -L_{-m,-lambda}[e, Psi]; T -> -T; S -> +S; j -> -j"],
        "untwistedFrameResult" -> If[chi === -1, "L_{m,lambda}[-e R_u, u Psi] = -L_{m,-lambda}[e, Psi] (CONTRACT E3)", "L_{m,lambda}[-e R_u, u Psi] = L_{m,lambda}[e, Psi] (exact symmetry)"],
        "gamma8TimesUntwisted" -> If[chi === -1, "L_{m,lambda}[-e R_u, gamma^8 u Psi] = +L_{-m,lambda}[e, Psi]", "L_{m,lambda}[-e R_u, gamma^8 u Psi] = -L_{-m,-lambda}[e, Psi]"]|>]],
   {uu, units}];
  addCheck["PAIR_T2frame_unitVectors", res["unit"]];
  addCheck["PAIR_T2frame_characterIsMinusNorm", res["character"] && Count[rows, r_ /; r["character"] === "-1"] === 5 && Count[rows, r_ /; r["character"] === "1"] === 5];
  addCheck["PAIR_T2frame_untwistedAdjointIsMinusReflection", res["lambda"]];
  addCheck["PAIR_T2frame_frameReflectionsGeometry", res["frames"]];
  addCheck["PAIR_T2frame_scalarAndCurrentSigns", res["scalarAndCurrent"]];
  addCheck["PAIR_T2frame_twistedSpacelikeMapsToMinusMSameLambda", res["twistedSpacelike"]];
  addCheck["PAIR_T2frame_untwistedSpacelikeContractE3", res["untwistedSpacelike"]];
  addCheck["PAIR_T2frame_gamma8TimesUntwistedSpacelike", res["gamma8Untwisted"]];
  addCheck["PAIR_T2frame_twistedTimelike", res["twistedTimelike"]];
  addCheck["PAIR_T2frame_untwistedTimelikeSymmetry", res["untwistedTimelike"]];
  addCheck["PAIR_T2frame_gamma8TimesUntwistedTimelike", res["gamma8UntwistedTimelike"]];
  logT["T2frame seconds: ", Round[AbsoluteTime[] - t0]];
  $theory["T2frameTable"] = rows;];

(* ================================================================== *)
(* 7. PAIR_T2z2: the coordinate action in the Z2 primordial field     *)
(* ================================================================== *)

(* the static primordial field in the proper chart (STAGE4_SPEC section 1, a4 constant):
   y < 0 side: h = (1, W e^{a4} (x3), 1, W e^{-a4} (x3)), W = e^{Hy};  the Z2 mirror side y > 0 has W = e^{-Hy}. *)
yc = {y, x1, x2, x3, x4, x5, x6, x7};
diagGeometry[hh_List] := Module[{g, gi, Gam, ev, ei, omMix, omL, Om, gU},
  g = DiagonalMatrix[hh^2 etaD]; gi = DiagonalMatrix[1/(hh^2 etaD)];
  Gam = Table[Together[(1/2) Sum[gi[[r, s]] (D[g[[s, n]], yc[[mu]]] + D[g[[s, mu]], yc[[n]]] - D[g[[mu, n]], yc[[s]]]), {s, 8}]], {r, 8}, {mu, 8}, {n, 8}];
  ev = DiagonalMatrix[hh]; ei = DiagonalMatrix[1/hh];
  omMix = Table[Together[Sum[ei[[b, n]] (Sum[Gam[[r, mu, n]] ev[[r, a]], {r, 8}] - D[ev[[n, a]], yc[[mu]]]), {n, 8}]], {mu, 8}, {a, 8}, {b, 8}];
  omL = Table[etaD[[a]] omMix[[mu, a, b]], {mu, 8}, {a, 8}, {b, 8}];
  Om = Table[(1/2) Sum[omL[[mu, a, b]] Sab[a - 1, b - 1], {a, 8}, {b, 8}], {mu, 8}];
  gU = Table[Sum[ei[[a, mu]] G[a - 1], {a, 8}], {mu, 8}];
  <|"g" -> g, "gi" -> gi, "Om" -> Om, "gU" -> gU, "gD" -> Table[g[[mu, mu]] gU[[mu]], {mu, 8}], "sqrtg" -> Times @@ hh, "christoffel" -> Gam|>];
hhMinus = {1, E^(H y + a4c), E^(H y + a4c), E^(H y + a4c), 1, E^(H y - a4c), E^(H y - a4c), E^(H y - a4c)};
hhPlus = hhMinus /. H -> -H;

zPieces[gm_, psi_, psid_] := Module[{bar = psid.C16, Dp, Db},
  Dp = Table[D[psi, yc[[mu]]] + gm["Om"][[mu]].psi, {mu, 8}];
  Db = Table[D[bar, yc[[mu]]] - bar.gm["Om"][[mu]], {mu, 8}];
  <|"psi" -> psi, "bar" -> bar, "Dp" -> Dp, "Db" -> Db, "S" -> Expand[bar.psi],
    "kin" -> Total[Table[Expand[(1/2) bar.gm["gU"][[mu]].Dp[[mu]]] - Expand[(1/2) Db[[mu]].gm["gU"][[mu]].psi], {mu, 8}]]|>];
zDirac[gm_, pc_, mass_, ll_] := Expand[Total[Table[Expand[gm["gU"][[mu]].pc["Dp"][[mu]]], {mu, 8}]] - Expand[(mass + ll pc["S"]) pc["psi"]]];
zLs[pc_, mass_, ll_] := Expand[pc["kin"] - mass pc["S"] - (ll/2) pc["S"]^2];
zT[gm_, pc_, mass_, ll_] := Module[{ls = zLs[pc, mass, ll]},
  Table[Expand[-(1/4) pc["bar"].gm["gD"][[mu]].pc["Dp"][[nu]]] + Expand[-(1/4) pc["bar"].gm["gD"][[nu]].pc["Dp"][[mu]]] +
    Expand[(1/4) pc["Db"][[mu]].gm["gD"][[nu]].pc["psi"]] + Expand[(1/4) pc["Db"][[nu]].gm["gD"][[mu]].pc["psi"]] + Expand[gm["g"][[mu, nu]] ls], {mu, 8}, {nu, 8}]];
zCur[gm_, pc_] := Table[Expand[pc["bar"].gm["gU"][[mu]].pc["psi"]], {mu, 8}];
zzero[e_] := AllTrue[Flatten[{e}], Function[x, With[{r = Expand[x]}, r === 0 || Together[r] === 0]]];
flipY[e_] := e /. y -> -y;

checkT2Z2[] := Module[{gM, gP, psiF, psiBF, ycR, psiR, psiBR, pcM, pcP, sgn, PB, pcPB, TP, TM, t0 = AbsoluteTime[]},
  gM = diagGeometry[hhMinus]; gP = diagGeometry[hhPlus];
  addCheck["PAIR_T2z2_geometry", zzero[Sum[gM["gU"][[mu]].gM["Om"][[mu]], {mu, 8}] - 3 H G[0]] && zzero[Sum[gP["gU"][[mu]].gP["Om"][[mu]], {mu, 8}] + 3 H G[0]] &&
    zzero[gM["sqrtg"] - E^(6 H y)] && zzero[flipY[gM["g"]] - gP["g"]]];
  psiF = Table[ff[k] @@ yc, {k, 0, 15}]; psiBF = Table[fb[k] @@ yc, {k, 0, 15}];
  ycR = ReplacePart[yc, 1 -> -y];
  psiR = G[0].Table[ff[k] @@ ycR, {k, 0, 15}]; psiBR = Table[fb[k] @@ ycR, {k, 0, 15}].G[0];
  pcM = zPieces[gM, psiF, psiBF]; pcP = zPieces[gP, psiR, psiBR];
  sgn = {-1, 1, 1, 1, 1, 1, 1, 1};
  (* Psi'(y) = gamma^0 Psi(-y) on the mirror side: Dirac operator, S, L, T, j *)
  addCheck["PAIR_T2z2_diracOperator", zzero[zDirac[gP, pcP, -m, lam] + G[0].flipY[zDirac[gM, pcM, m, lam]]]];
  addCheck["PAIR_T2z2_sameMassFails", ! zzero[zDirac[gP, pcP, m, lam] + G[0].flipY[zDirac[gM, pcM, m, lam]]]];
  addCheck["PAIR_T2z2_scalarOdd", zzero[pcP["S"] + flipY[pcM["S"]]] && pcM["S"] =!= 0];
  addCheck["PAIR_T2z2_lagrangianEven", zzero[zLs[pcP, -m, lam] - flipY[zLs[pcM, m, lam]]] && zzero[gP["sqrtg"] - flipY[gM["sqrtg"]]]];
  TP = zT[gP, pcP, -m, lam]; TM = zT[gM, pcM, m, lam];
  addCheck["PAIR_T2z2_emtPullback", zzero[Table[TP[[mu, nu]] - sgn[[mu]] sgn[[nu]] flipY[TM[[mu, nu]]], {mu, 8}, {nu, 8}]] && ! zzero[TM[[5, 5]]]];
  addCheck["PAIR_T2z2_currentPullback", zzero[zCur[gP, pcP] - sgn flipY[zCur[gM, pcM]]]];
  (* general mass function: m(y) -> -m(-y); a Z2-symmetric configuration obeys one global mass function iff it is odd *)
  addCheck["PAIR_T2z2_massFunctionMap", zzero[zDirac[gP, pcP, -mf[-y], lam] + G[0].flipY[zDirac[gM, pcM, mf[y], lam]]]];
  addCheck["PAIR_T2z2_symmetricIffOddMass", zzero[zDirac[gP, pcP, mf[y], lam] - zDirac[gP, pcP, -mf[-y], lam] + (mf[y] + mf[-y]) pcP["psi"]]];
  (* P_B = i gamma^0 gamma^8 (the Stage-4 even-mass reflection) at the field level: (m, lambda) -> (m, -lambda), L -> -L *)
  PB = I G[0].g8;
  pcPB = zPieces[gP, PB.Table[ff[k] @@ ycR, {k, 0, 15}], Table[fb[k] @@ ycR, {k, 0, 15}].herm[PB]];
  addCheck["PAIR_T2z2_PBfieldLevelFlipsLambda", herm[PB] === PB && PB.PB === id16 &&
    zzero[zDirac[gP, pcPB, m, -lam] - PB.flipY[zDirac[gM, pcM, m, lam]]] && ! zzero[zDirac[gP, pcPB, m, lam] - PB.flipY[zDirac[gM, pcM, m, lam]]] &&
    zzero[pcPB["S"] + flipY[pcM["S"]]] && zzero[zLs[pcPB, m, -lam] + flipY[zLs[pcM, m, lam]]]];
  (* the expectation-rule parities used in Stage 4 (the rule matrix B C): P_A odd, P_B even, because P_B contains gamma^8 which reverses B *)
  addCheck["PAIR_T2z2_ruleParities", G[0].BC.G[0] === -BC && herm[PB].BC.PB === BC && G[0].Bm.G[0] === Bm && herm[PB].Bm.PB === -Bm &&
    herm[PB].C16.PB === -C16 && G[0].C16.G[0] === -C16];
  logT["T2z2 seconds: ", Round[AbsoluteTime[] - t0]];
  $theory["T2z2"] = <|
    "geometry" -> "static primordial field, proper chart y (STAGE4_SPEC section 1): y < 0: W = e^{Hy}; Z2 mirror side y > 0: W = e^{-Hy}; vielbein h = (1, W e^{a4} (x3), 1, W e^{-a4} (x3)); the reflection phi: y -> -y is an isometry of the Z2 geometry whose differential reflects the frame vector e_0",
    "map" -> "Psi'(y, x) = gamma^0 Psi(-y, x), Psi'^dagger(y, x) = Psi^dagger(-y, x) gamma^0 (u = gamma^0: n(u) = +1, character -1, twisted lift = the coordinate reflection of x0 ~ y)",
    "diracOperator" -> "gamma^mu D_mu Psi' = -gamma^0 (gamma^mu D_mu Psi)(-y) and S[Psi'] = -S[Psi](-y), hence E_{-m,lambda}[Psi'](y) = -gamma^0 E_{m,lambda}[Psi](-y): Psi solves the equation with (m, lambda) on y < 0 iff Psi' solves it with (-m, lambda) on y > 0 (the SAME lambda)",
    "massFunction" -> "for a mass function m(y): Psi' solves the equation with -m(-y); a configuration with Psi(-y) = +-gamma^0 Psi(y) satisfies the equation with ONE global mass function m(y) on both sides iff (m(y) + m(-y)) Psi = 0, i.e. iff the mass function is odd: the Z2 mirror universe carries the mass -M (STAGE4_SPEC E4.6); with the Hartree term lambda S the effective mass is odd automatically because S is P_A-odd",
    "lagrangian" -> "L_{-m,lambda}[Psi'](y) = L_{m,lambda}[Psi](-y) (sqrt|g| even)",
    "emt" -> "T'_{mu nu}(y) = s_mu s_nu T_{mu nu}(-y), s = (-1, 1, 1, 1, 1, 1, 1, 1) in the order (y, x1, x2, x3, x4, x5, x6, x7): the pull-back phi^* T; in particular rho'(y) = rho(-y), all pressures even, T'_{y i} = -T_{y i}(-y)",
    "current" -> "j'^mu(y) = s_mu j^mu(-y): the charge density j^4 is even (same charge on both sides)",
    "PB" -> "P_B: Psi'(y) = i gamma^0 gamma^8 Psi(-y) at the field level maps (m, lambda) -> (m, -lambda) with L -> -L and S -> -S (P_B = P_A composed with the gamma^8 map T1); at the Kohn-Sham mean-field level with the standard expectation rule it is the even-mass symmetry with the same lambda (Stage 4), because the rule matrix BC is P_B-even while C is P_B-odd: gamma^8 reverses the Krein metric B",
    "interpretation" -> "the Z2 mirror universe of mass -M is the mirror image (frame reflection of the hidden direction) of the +M universe: same energy density, same pressures, same charge, opposite scalar density. The sign of m relative to the orientation of the frame is not an invariant: the Pin reflections of character -1 map (m, lambda) -> (-m, lambda) with L -> +L."|>;];

(* ================================================================== *)
(* 7b. PAIR_T1primordial: T1 in the Stage-2 primordial field           *)
(* ================================================================== *)

(* the notebook chart of the primordial field (CONTRACT section 9): z = 6 H x0, t = H x4, a4 an ARBITRARY function,
   h = (cot z, s^{1/6} e^{a4(t)} (x3), 1, s^{1/6} e^{-a4(t)} (x3)), s = sin z; generic spinor fields of all eight
   coordinates.  The gamma^8 map does not touch the geometric coefficients, so the identities cancel term by term. *)
checkT1Primordial[] := Module[{xn = {x0, x1, x2, x3, x4, x5, x6, x7}, hh, gm, psiF, psiBF, pc, pc8, TP, T8, t0 = AbsoluteTime[]},
  Block[{yc = {x0, x1, x2, x3, x4, x5, x6, x7}},
   hh = {Cot[6 H x0], Sin[6 H x0]^(1/6) E^(a4f[H x4]), Sin[6 H x0]^(1/6) E^(a4f[H x4]), Sin[6 H x0]^(1/6) E^(a4f[H x4]), 1,
     Sin[6 H x0]^(1/6) E^(-a4f[H x4]), Sin[6 H x0]^(1/6) E^(-a4f[H x4]), Sin[6 H x0]^(1/6) E^(-a4f[H x4])};
   gm = diagGeometry[hh];
   psiF = Table[pf[k] @@ xn, {k, 0, 15}]; psiBF = Table[pfb[k] @@ xn, {k, 0, 15}];
   pc = zPieces[gm, psiF, psiBF]; pc8 = zPieces[gm, g8.psiF, psiBF.g8];
   addCheck["PAIR_T1primordial_nontrivialCoupling", ! zeroE[Sum[gm["gU"][[mu]].gm["Om"][[mu]], {mu, 8}]] && ! FreeQ[gm["Om"], a4f] && pc["S"] =!= 0];
   addCheck["PAIR_T1primordial_scalarAndKinetic", Expand[pc8["S"] - pc["S"]] === 0 && Expand[pc8["kin"] + pc["kin"]] === 0];
   addCheck["PAIR_T1primordial_lagrangian", Expand[zLs[pc8, -m, -lam] + zLs[pc, m, lam]] === 0];
   addCheck["PAIR_T1primordial_diracOperator", zeroE[zDirac[gm, pc8, -m, -lam] + g8.zDirac[gm, pc, m, lam]]];
   TP = zT[gm, pc, m, lam]; T8 = zT[gm, pc8, -m, -lam];
   addCheck["PAIR_T1primordial_emt64", zeroE[TP + T8] && ! zeroE[TP[[5, 5]]] && ! zeroE[TP[[1, 5]]]];
   addCheck["PAIR_T1primordial_current", zeroE[zCur[gm, pc8] + zCur[gm, pc]]]];
  logT["T1primordial seconds: ", Round[AbsoluteTime[] - t0]];];

(* ================================================================== *)
(* 8. PAIR_T3block: the maps on the exact 2x2 block basis of Stage 4  *)
(* ================================================================== *)

toGC[{re_String, im_String}] := ToExpression[re] + I ToExpression[im];
zero2 = ConstantArray[0, {2, 2}];
conjR[e_] := e /. Complex[a_, b_] :> Complex[a, -b];   (* complex conjugation, all symbols real *)
(* the 2x2 block ODE chi' = N chi (STAGE4_SPEC E4.7) and the 16-component reduced operator *)
NB[j_, Mv_, kv_] := Mv sig3 - kap kv sig2 + I j (eps - vv) sig1;
Nfull[Mv_, kv_] := G[0].(Mv id16 - I kap kv G[1] + I (eps - vv) G[4]);
(* the block Hamiltonian h_j = j[-i sigma1 d_y + M sigma2 + kappa k sigma3] + v_v acting on a 2-vector of functions of y *)
hB[jv_, Mf_, kv_, kf_, vf_, c_] := jv (-I sig1.D[c, y] + Mf sig2.c + kf kv sig3.c) + vf c;
bagQ[t_] := Cos[t] sig3 + Sin[t] sig2;
densMats[j_] := <|"n" -> id2, "s" -> j sig2, "t" -> j sig3, "c" -> j sig1|>;

checkT3Block[ksFile_] := Module[{thj, blocks, labs, Vint, blkOf, diagB, blockDiagQ, partner, bb8, bb1, ph8, ph1, okG8, okG1, others, c2v, Pe, Po,
   mapDens, epsS2, epsS1, epsS3, chiR},
  thj = Import[ksFile, "RawJSON"];
  blocks = thj["reduction"]["blockDiagonalisation"]["blocks"];
  labs = Table[ToExpression /@ {b["j"], b["s2"], b["s3"]}, {b, blocks}];
  Vint = Transpose[Flatten[Table[{toGC /@ b["vPlus"], toGC /@ b["vMinus"]}, {b, blocks}], 1]];
  blkOf[M_] := Module[{Y = Together[herm[Vint].M.Vint/8]}, Table[Y[[2 i - 1 ;; 2 i, 2 l - 1 ;; 2 l]], {i, 8}, {l, 8}]];
  diagB[M_] := Module[{bb = blkOf[M]}, Table[bb[[i, i]], {i, 8}]];
  blockDiagQ[M_] := Module[{bb = blkOf[M]}, AllTrue[Flatten[Table[If[i == l, True, bb[[i, l]] === zero2], {i, 8}, {l, 8}]], TrueQ]];
  (* independent re-verification of the Stage-4 basis and block forms *)
  addCheck["PAIR_T3block_basisFromStage4", Length[blocks] === 8 && labs === Flatten[Table[{s1, s2, s3}, {s1, {1, -1}}, {s2, {1, -1}}, {s3, {1, -1}}], 2] &&
    Together[herm[Vint].Vint/8] === id16 && AllTrue[{G[0], G[0].G[1], G[0].G[4], Bm, C16, BC, G[4].G[1]}, blockDiagQ] &&
    diagB[G[0]] === ConstantArray[sig3, 8] && diagB[G[0].G[1]] === ConstantArray[-I sig2, 8] && diagB[G[0].G[4]] === Table[b[[1]] sig1, {b, labs}] &&
    diagB[Bm] === Table[b[[1]] b[[2]] id2, {b, labs}] && diagB[C16] === Table[b[[2]] sig2, {b, labs}] && diagB[BC] === Table[b[[1]] sig2, {b, labs}] &&
    diagB[-G[4].G[1]] === Table[b[[1]] sig3, {b, labs}]];
  (* gamma^8: block (j,s2,s3) <-> (-j,s2,s3), each off-diagonal block a phase times sigma2 *)
  partner[i_] := First[Flatten[Position[labs, {-labs[[i, 1]], labs[[i, 2]], labs[[i, 3]]}]]];
  bb8 = blkOf[g8];
  ph8 = Table[Together[bb8[[i, partner[i]]][[2, 1]]/I], {i, 8}];
  okG8 = AllTrue[Range[8], Function[i, AllTrue[Range[8], Function[l, If[l == partner[i], bb8[[i, l]] === ph8[[i]] sig2, bb8[[i, l]] === zero2]]]]] &&
    AllTrue[ph8, MemberQ[{1, -1, I, -I}, #] &];
  addCheck["PAIR_T3block_gamma8IsSigma2BetweenPartnerBlocks", okG8];
  addMeas["T3block_gamma8_phases_per_target_block", toStr[ph8]];
  (* gamma^1: block diagonal, a phase times sigma1 in every block; gamma^0 = sigma3 *)
  bb1 = blkOf[G[1]];
  ph1 = Table[bb1[[i, i]][[1, 2]], {i, 8}];
  okG1 = blockDiagQ[G[1]] && AllTrue[Range[8], bb1[[#, #]] === ph1[[#]] sig1 &] && AllTrue[ph1, MemberQ[{1, -1, I, -I}, #] &];
  addCheck["PAIR_T3block_gamma1IsSigma1InEveryBlock", okG1 && diagB[G[0]] === ConstantArray[sig3, 8]];
  addMeas["T3block_gamma1_phases", toStr[ph1]];
  (* the block pattern of the other reflections (measured) *)
  others = Association[Table["gamma^" <> ToString[a] -> Table[Flatten[Position[blkOf[G[a]][[i]], x_ /; x =!= zero2, {1}, Heads -> False]] - 1, {i, 8}], {a, {2, 3, 5, 6, 7}}]];
  addMeas["T3block_otherGammas_targetBlocks", toStr[others]];
  (* the ODE maps: sigma2 (gamma^8): (j, M, k) -> (-j, -M, k); sigma1 (gamma^1): (j, M, k) -> (j, -M, -k);
     sigma3 with y -> -y (gamma^0, P_A): M(y) -> -M(-y) (kappa even on the Z2 geometry); antiunitary K: (j, M, k) -> (-j, M, -k) *)
  addCheck["PAIR_T3block_sigma2MapsBlockODE", AllTrue[{1, -1}, zeroE[sig2.NB[#, Mx, kx].sig2 - NB[-#, -Mx, kx]] &] &&
    zeroE[g8.Nfull[Mx, kx].g8 - Nfull[-Mx, kx]]];
  addCheck["PAIR_T3block_sigma1MapsBlockODE", AllTrue[{1, -1}, zeroE[sig1.NB[#, Mx, kx].sig1 - NB[#, -Mx, -kx]] &] &&
    zeroE[G[1].Nfull[Mx, kx].G[1] - Nfull[-Mx, -kx]]];
  addCheck["PAIR_T3block_sigma3ReflectionMapsBlockODE", AllTrue[{1, -1}, zeroE[-sig3.NB[#, Mx, kx].sig3 - NB[#, -Mx, kx]] &] &&
    zeroE[-G[0].Nfull[Mx, kx].G[0] - Nfull[-Mx, kx]]];
  addCheck["PAIR_T3block_antiunitaryMaps", AllTrue[{1, -1}, zeroE[conjR[NB[#, Mx, kx]] - NB[-#, Mx, -kx]] && zeroE[sig2.conjR[NB[#, Mx, kx]].sig2 - NB[#, -Mx, -kx]] &]];
  (* the block Hamiltonians as differential operators on generic chi(y) *)
  c2v = {c1[y], c2[y]};
  addCheck["PAIR_T3block_hamiltonianSigma2", AllTrue[{1, -1}, zeroE[hB[-#, -MF[y], kx, KF[y], VF[y], sig2.c2v] - sig2.hB[#, MF[y], kx, KF[y], VF[y], c2v]] &]];
  addCheck["PAIR_T3block_hamiltonianSigma1", AllTrue[{1, -1}, zeroE[hB[#, -MF[y], -kx, KF[y], VF[y], sig1.c2v] - sig1.hB[#, MF[y], kx, KF[y], VF[y], c2v]] &]];
  chiR = sig3.(c2v /. y -> -y);
  addCheck["PAIR_T3block_hamiltonianSigma3Reflection", AllTrue[{1, -1}, zeroE[hB[#, -MF[-y], kx, KE[y^2], VF[-y], chiR] - sig3.flipY[hB[#, MF[y], kx, KE[y^2], VF[y], c2v]]] &]];
  (* boundary conditions: parity projectors (condition P chi(0) = 0) and the bag family (1 - Q(theta)) chi(-L) = 0 *)
  Pe = (id2 - sig3)/2; Po = (id2 + sig3)/2;
  addCheck["PAIR_T3block_parityMap", Pe.{u1, u2} === {0, u2} && Po.{u1, u2} === {u1, 0} && sig2.Pe.sig2 === Po && sig2.Po.sig2 === Pe &&
    sig1.Pe.sig1 === Po && sig3.Pe.sig3 === Pe];
  addCheck["PAIR_T3block_bagAngleMap", Simplify[sig2.bagQ[tht].sig2 - bagQ[Pi - tht]] === zero2 && Simplify[sig1.bagQ[tht].sig1 - bagQ[tht + Pi]] === zero2 &&
    Simplify[sig3.bagQ[tht].sig3 - bagQ[-tht]] === zero2 && Simplify[sig2.(id2 - bagQ[tht]).sig2 - (id2 - bagQ[Pi - tht])] === zero2 &&
    sig2.bagQ[0].sig2 === bagQ[Pi] && sig1.bagQ[0].sig1 === bagQ[Pi] && bagQ[Pi] === -sig3 &&
    bagQ[Pi - (-Pi/2)] === bagQ[-Pi/2] && bagQ[-Pi/2 + Pi] === bagQ[Pi/2]];
  (* Stage-4/Rust notation chi = (a, i b): sigma2 is the swap (a, b) -> (b, a) *)
  addCheck["PAIR_T3block_sigma2IsRustSwap", sig2.{aa, I bb} === {bb, I aa} && sig1.{aa, I bb} === {I bb, aa}];
  (* densities and current matrices: value of X on the image orbital in the image block *)
  mapDens[U_, jmap_] := Association[Table[key -> Which[Simplify[U.densMats[jmap[jj]][key].U - densMats[jj][key]] === zero2, 1,
        Simplify[U.densMats[jmap[jj]][key].U + densMats[jj][key]] === zero2, -1, True, 0], {key, {"n", "s", "t", "c"}}]];
  epsS2 = mapDens[sig2, -# &]; epsS1 = mapDens[sig1, # &]; epsS3 = mapDens[sig3, # &];
  addMeas["T3block_densitySigns_sigma2", toStr[Values[epsS2]]];
  addMeas["T3block_densitySigns_sigma1", toStr[Values[epsS1]]];
  addMeas["T3block_densitySigns_sigma3", toStr[Values[epsS3]]];
  addCheck["PAIR_T3block_densityAndCurrentMaps", Values[epsS2] === {1, -1, 1, 1} && Values[epsS1] === {1, -1, -1, 1} && Values[epsS3] === {1, -1, 1, -1}];
  (* potentials, both statistics (sg = -1 anticommuting, +1 commuting, kept symbolic) *)
  Module[{Me, vV, vS, eI},
   Me[mv_, lv_, S_] := mv + lv S + sg (lv/16) S; vV[lv_, n_] := sg (lv/16) n; vS[lv_, S_] := sg (lv/16) S;
   eI[lv_, n_, S_] := (lv/2) S^2 + sg (lv/32) (n^2 + S^2);
   addCheck["PAIR_T3block_potentialsStandardRule", zeroE[Me[-m, lam, -Sp] + Me[m, lam, Sp]] && zeroE[vS[lam, -Sp] + vS[lam, Sp]] &&
     zeroE[eI[lam, np, -Sp] - eI[lam, np, Sp]] && ! zeroE[Me[-m, -lam, -Sp] + Me[m, lam, Sp]]];
   addCheck["PAIR_T3block_potentialsImageRule", zeroE[Me[-m, -lam, Sp] + Me[m, lam, Sp]] && zeroE[vV[-lam, -np] - vV[lam, np]] &&
     zeroE[vS[-lam, Sp] + vS[lam, Sp]] && zeroE[eI[-lam, -np, Sp] + eI[lam, np, Sp]]];
   addCheck["PAIR_T3block_statisticsCoefficients", Coefficient[Me[m, lam, Sp] /. sg -> -1, lam Sp] === 15/16 && Coefficient[Me[m, lam, Sp] /. sg -> 1, lam Sp] === 17/16 &&
     (vV[lam, np] /. sg -> -1) === -(lam/16) np && (vV[lam, np] /. sg -> 1) === (lam/16) np]];
  (* per-orbital EMT formulas of Stage 4 (KS_emt): invariant under the sigma2 and sigma1 maps with the standard rule, odd under the image rule *)
  Module[{rho1, py1, p11, pt1},
   rho1[e_, n_, s_, t_, M_, mv_, v_, k_] := e n - (M - mv) s - v n;
   py1[e_, n_, s_, t_, M_, mv_, v_, k_] := e n - mv s - kap k t;
   p11[e_, n_, s_, t_, M_, mv_, v_, k_] := kap k t + (M - mv) s + v n;
   pt1[e_, n_, s_, t_, M_, mv_, v_, k_] := (M - mv) s + v n;
   addCheck["PAIR_T3block_orbitalEMTFormulas", AllTrue[{rho1, py1, p11, pt1}, Function[F,
       zeroE[F[eps, nn, -ss, tt, -Mx, -m, vv, kx] - F[eps, nn, ss, tt, Mx, m, vv, kx]] &&
       zeroE[F[eps, nn, -ss, -tt, -Mx, -m, vv, -kx] - F[eps, nn, ss, tt, Mx, m, vv, kx]] &&
       zeroE[F[eps, -nn, ss, -tt, -Mx, -m, vv, kx] + F[eps, nn, ss, tt, Mx, m, vv, kx]]]]]];
  $theory["T3blockMaps"] = <|
    "basisSource" -> "artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json, reduction.blockDiagonalisation (block order (j,s2,s3) = (1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)); re-verified here",
    "gamma8" -> <|"blockAction" -> "V^dagger gamma^8 V maps block (j,s2,s3) onto block (-j,s2,s3); every nonzero 2x2 block is c sigma2 with a phase c in {+-1, +-i}",
      "phasesByTargetBlock" -> gqVec[ph8], "map" -> "chi -> sigma2 chi (up to the phase), j -> -j, k unchanged"|>,
    "gamma1" -> <|"blockAction" -> "V^dagger gamma^1 V is block diagonal with c sigma1 in every block", "phases" -> gqVec[ph1], "map" -> "chi -> sigma1 chi, j unchanged, k -> -k (reflection of x1)"|>,
    "gamma0" -> "sigma3 in every block (with y -> -y: the Stage-4 reflection P_A)",
    "otherGammas" -> $meas["T3block_otherGammas_targetBlocks"],
    "blockODE" -> "chi' = N_j(M, k) chi, N_j(M, k) = M sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1",
    "odeMaps" -> <|"sigma2" -> "sigma2 N_j(M, k) sigma2 = N_{-j}(-M, k) (16-component: gamma^8 N(M) gamma^8 = N(-M))",
      "sigma1" -> "sigma1 N_j(M, k) sigma1 = N_j(-M, -k) (16-component: gamma^1 N(M, k) gamma^1 = N(-M, -k))",
      "sigma3" -> "-sigma3 N_j(M, k) sigma3 = N_j(-M, k): chi(y) -> sigma3 chi(-y) maps M(y) to -M(-y) when kappa is even (Z2 geometry)",
      "antiunitary" -> "K N_j(M, k) K = N_{-j}(M, -k) (complex conjugation, a symmetry of the same mass); sigma2 K: (j, M, k) -> (j, -M, -k)"|>,
    "hamiltonianMaps" -> "h_j(M, k) = j[-i sigma1 d_y + M sigma2 + kappa k sigma3] + v_v: sigma2 h_j(M, k) = h_{-j}(-M, k) sigma2 and sigma1 h_j(M, k) = h_j(-M, -k) sigma1 as differential operators (v_v unchanged); sigma3 h_j(M(y)) chi(-y) = [h_j(-M(-y)) sigma3 chi(-.)](y) for even kappa and v_v(y) -> v_v(-y)",
    "boundaryConditions" -> <|"parity" -> "even parity chi_2(0) = 0 (P_e = (1 - sigma3)/2) <-> odd parity chi_1(0) = 0 under sigma2 and under sigma1 (p -> -p); unchanged under sigma3",
      "bag" -> "(1 - Q(theta)) chi(-L) = 0, Q = cos(theta) sigma3 + sin(theta) sigma2: sigma2 Q(theta) sigma2 = Q(pi - theta) (theta -> pi - theta), sigma1 Q(theta) sigma1 = Q(theta + pi), sigma3 Q(theta) sigma3 = Q(-theta)",
      "stage4Default" -> "theta = 0 (chi_2(-L) = 0, Rust b(-L) = 0) -> theta = pi (chi_1(-L) = 0, Rust a(-L) = 0) under both sigma2 and sigma1",
      "asymptoticBag" -> "the k-dependent asymptotic prescription theta(k) = -sgn(k) pi/2 is mapped onto itself: sigma2 (same k): pi - (-pi/2) = -pi/2 mod 2 pi; sigma1 (k -> -k): -pi/2 + pi = +pi/2 = theta(-k)",
      "rustNotation" -> "chi = (a, i b): sigma2 (a, i b) = (b, i a), i.e. the swap (a, b) -> (b, a) of the Rust crate (emt.rs header)"|>,
    "densitiesAndCurrents" -> <|"matrices" -> "per block: n = chi^dagger chi, s = j chi^dagger sigma2 chi (= u^dagger B C u), t = j chi^dagger sigma3 chi (k-current), c = j chi^dagger sigma1 chi (y-current, A4 = gamma^0 gamma^4)",
      "sigma2" -> "(n, s, t, c) -> (n, -s, t, c)", "sigma1" -> "(n, s, t, c) -> (n, -s, -t, c)", "sigma3" -> "(n, s, t, c) -> (n, -s, t, -c) (P_A, Stage 4)",
      "imageRule" -> "with the Krein metric -B of the gamma^8 image every one-body expectation value changes sign in addition: sigma2 route (n, s, t, c) -> (-n, s, -t, -c)"|>,
    "potentials" -> <|"definitions" -> "M_eff = m + lambda S_p + v_s, v_s = sg (lambda/16) S_p, v_v = sg (lambda/16) n_p, sg = -1 (dirac16complex, anticommuting), sg = +1 (dirac16complex00, commuting): M_eff = m + (15/16) lambda S_p resp. m + (17/16) lambda S_p",
      "standardRule" -> "(m, lambda, n, S) -> (-m, lambda, n, -S): M_eff -> -M_eff, v_s -> -v_s, v_v -> v_v, e_H + e_x invariant (both statistics); with lambda -> -lambda instead the map FAILS for lambda != 0",
      "imageRule" -> "(m, lambda, n, S) -> (-m, -lambda, -n, S): M_eff -> -M_eff, v_s -> -v_s, v_v -> v_v, e_H + e_x -> -(e_H + e_x) (both statistics)"|>,
    "orbitalEMT" -> "the Stage-4 per-orbital EMT (rho = eps n - (M_eff - m) s - v_v n, p_y = eps n - m s - kappa k t, p_1 = kappa k t + (M_eff - m) s + v_v n, p_2 = p_3 = p_t = (M_eff - m) s + v_v n) is invariant under the sigma2 and sigma1 maps with the standard rule and changes sign under the image rule"|>;];

(* ================================================================== *)
(* 9. PAIR_T3ks: the Kohn-Sham level (functional, spectra, control)   *)
(* ================================================================== *)

(* Discretised block Kohn-Sham model (any discretisation of this structure, in particular the
   finite-difference/Chebyshev reference and the shooting solver): Ny grid points, flat weight,
   real antisymmetric derivative matrix Dm (so -i sigma1 (x) Dm is Hermitian), density factors
   cc[i] = e^{-6Hy_i}/l^3 with volume weights 1/cc[i]; No orbitals with block labels j_n,
   momenta k_n, amplitudes xx[n,p] (conjugates xb[n,p]) and occupations occ[n]; rule sign r
   (+1 the standard expectation rule, -1 the Krein metric -B of the gamma^8 image);
   statistics sign sg (-1 anticommuting, +1 commuting). *)
checkT3KS[] := Module[{Ny = 2, No = 2, dim = 4, Dm, IN, kr, U2, U1, h0, xsV, xbV, jV, kV, nI, SI, Efun, hKS, Sent, xs2, xb2, xs1, xb1,
   E0, E2, E1, Eimg, statOK, statImg, t0 = AbsoluteTime[]},
  Dm = {{0, d12}, {-d12, 0}}; IN = IdentityMatrix[Ny]; kr = KroneckerProduct;
  U2 = kr[IN, sig2]; U1 = kr[IN, sig1];
  h0[jv_, kv_, mv_] := jv (-I kr[Dm, sig1] + mv kr[IN, sig2] + kv kr[DiagonalMatrix[{kp1, kp2}], sig3]);
  xsV = Table[xx[n, p], {n, No}, {p, dim}]; xbV = Table[xb[n, p], {n, No}, {p, dim}];
  jV = {j1, j2}; kV = {k1, k2};
  nI[xs_, xb_, js_, r_] := Table[r cc[i] Sum[occ[n] (xb[[n, 2 i - 1]] xs[[n, 2 i - 1]] + xb[[n, 2 i]] xs[[n, 2 i]]), {n, No}], {i, Ny}];
  SI[xs_, xb_, js_, r_] := Table[r cc[i] Sum[occ[n] js[[n]] ({xb[[n, 2 i - 1]], xb[[n, 2 i]]}.sig2.{xs[[n, 2 i - 1]], xs[[n, 2 i]]}), {n, No}], {i, Ny}];
  Efun[xs_, xb_, js_, ks_, mv_, lv_, r_] := Module[{nn = nI[xs, xb, js, r], SS = SI[xs, xb, js, r]},
    r Sum[occ[n] xb[[n]].h0[js[[n]], ks[[n]], mv].xs[[n]], {n, No}] + Sum[(1/cc[i]) ((lv/2) SS[[i]]^2 + sg (lv/32) (nn[[i]]^2 + SS[[i]]^2)), {i, Ny}]];
  hKS[n_, xs_, xb_, js_, ks_, mv_, lv_, r_] := Module[{nn = nI[xs, xb, js, r], SS = SI[xs, xb, js, r]},
    h0[js[[n]], ks[[n]], mv] + js[[n]] kr[DiagonalMatrix[lv SS + sg (lv/16) SS], sig2] + kr[DiagonalMatrix[sg (lv/16) nn], id2]];
  Sent = -Sum[occ[n] Log[occ[n]] + (1 - occ[n]) Log[1 - occ[n]], {n, No}];
  addCheck["PAIR_T3ks_modelHermitian", Together[hermR[h0[j1, k1, m]] - h0[j1, k1, m]] === ConstantArray[0, {dim, dim}] && U2.U2 === IdentityMatrix[dim] && U1.U1 === IdentityMatrix[dim]];
  (* stationarity: dE/d xb_n = r occ_n hKS_n x_n (the KS equations for both statistics and both rules); dE/d occ_n = r <x_n| hKS_n |x_n> (Janak) *)
  statOK[r_] := AllTrue[Flatten[Table[Together[D[Efun[xsV, xbV, jV, kV, m, lam, r], xb[n, p]] - r occ[n] (hKS[n, xsV, xbV, jV, kV, m, lam, r].xsV[[n]])[[p]]] === 0, {n, No}, {p, dim}]], TrueQ] &&
    AllTrue[Range[No], Together[D[Efun[xsV, xbV, jV, kV, m, lam, r], occ[#]] - r xbV[[#]].hKS[#, xsV, xbV, jV, kV, m, lam, r].xsV[[#]]] === 0 &];
  addCheck["PAIR_T3ks_stationarityBothStatistics", statOK[1] && statOK[-1] && ! FreeQ[hKS[1, xsV, xbV, jV, kV, m, lam, 1], sg]];
  E0 = Efun[xsV, xbV, jV, kV, m, lam, 1];
  (* T2-type map, sigma2 route: chi -> sigma2 chi, j -> -j, k, lambda, occupations unchanged, m -> -m *)
  xs2 = (U2.#) & /@ xsV; xb2 = (#.U2) & /@ xbV;
  E2 = Efun[xs2, xb2, -jV, kV, -m, lam, 1];
  addCheck["PAIR_T3ks_sigma2FunctionalInvariant", Together[E2 - E0] === 0 && Together[Efun[xs2, xb2, -jV, kV, -m, -lam, 1] - E0] =!= 0];
  addCheck["PAIR_T3ks_sigma2Densities", zeroT[nI[xs2, xb2, -jV, 1] - nI[xsV, xbV, jV, 1]] && zeroT[SI[xs2, xb2, -jV, 1] + SI[xsV, xbV, jV, 1]]];
  addCheck["PAIR_T3ks_sigma2KSOperatorEquivariant", AllTrue[Range[No], zeroT[U2.hKS[#, xsV, xbV, jV, kV, m, lam, 1].U2 - hKS[#, xs2, xb2, -jV, kV, -m, lam, 1]] &] &&
    ! zeroT[U2.hKS[1, xsV, xbV, jV, kV, m, lam, 1].U2 - hKS[1, xs2, xb2, -jV, kV, -m, -lam, 1]]];
  (* sigma1 route: chi -> sigma1 chi, j unchanged, k -> -k, m -> -m, lambda unchanged *)
  xs1 = (U1.#) & /@ xsV; xb1 = (#.U1) & /@ xbV;
  E1 = Efun[xs1, xb1, jV, -kV, -m, lam, 1];
  addCheck["PAIR_T3ks_sigma1FunctionalInvariant", Together[E1 - E0] === 0 && zeroT[nI[xs1, xb1, jV, 1] - nI[xsV, xbV, jV, 1]] && zeroT[SI[xs1, xb1, jV, 1] + SI[xsV, xbV, jV, 1]] &&
    AllTrue[Range[No], zeroT[U1.hKS[#, xsV, xbV, jV, kV, m, lam, 1].U1 - hKS[#, xs1, xb1, jV, -kV, -m, lam, 1]] &]];
  (* T1 image (Krein metric -B, rule sign -1): lambda -> -lambda, E -> -E, n -> -n, S -> S, KS operator mapped *)
  Eimg = Efun[xs2, xb2, -jV, kV, -m, -lam, -1];
  addCheck["PAIR_T3ks_imageRuleEnergyOdd", Together[Eimg + E0] === 0 && zeroT[nI[xs2, xb2, -jV, -1] + nI[xsV, xbV, jV, 1]] && zeroT[SI[xs2, xb2, -jV, -1] - SI[xsV, xbV, jV, 1]] &&
    AllTrue[Range[No], zeroT[U2.hKS[#, xsV, xbV, jV, kV, m, lam, 1].U2 - hKS[#, xs2, xb2, -jV, kV, -m, -lam, -1]] &]];
  (* orbital energies (Janak) and temperature: standard rule eps -> eps, F -> F at the same T; image rule eps_energy -> -eps, F(-T) = -F(T) *)
  addCheck["PAIR_T3ks_occupationsAndTemperature", AllTrue[Range[No], Together[D[E2, occ[#]] - D[E0, occ[#]]] === 0 && Together[D[Eimg, occ[#]] + D[E0, occ[#]]] === 0 &] &&
    Together[(E2 - TT Sent) - (E0 - TT Sent)] === 0 && Together[(Eimg - (-TT) Sent) + (E0 - TT Sent)] === 0];
  (* pair totals at the KS level *)
  addCheck["PAIR_totals_ksKreinImagePair", Together[E0 + Eimg] === 0 && zeroT[nI[xsV, xbV, jV, 1] + nI[xs2, xb2, -jV, -1]] &&
    zeroT[SI[xsV, xbV, jV, 1] + SI[xs2, xb2, -jV, -1] - 2 SI[xsV, xbV, jV, 1]]];
  addCheck["PAIR_totals_ksMirrorPair", Together[E0 + E2 - 2 E0] === 0 && zeroT[nI[xsV, xbV, jV, 1] + nI[xs2, xb2, -jV, 1] - 2 nI[xsV, xbV, jV, 1]] &&
    zeroT[SI[xsV, xbV, jV, 1] + SI[xs2, xb2, -jV, 1]]];
  logT["T3ks_functional seconds: ", Round[AbsoluteTime[] - t0]];];

(* exact k = 0 spectra (constant M_eff = M, v_v = 0) and the untransformed-boundary-condition control *)
checkT3Spectra[] := Module[{NB0, chi0, chiI, chiC, cj, dEdk, cM, cMI, cC, cMformula, cCformula, sub, cMY, cCY, kn, en, lev, levI, levC, nb0, nbC, t0 = AbsoluteTime[]},
  NB0[j_, Mv_] := NB[j, Mv, 0] /. {eps -> 0, vv -> 0};
  cj[c_] := conjR[c];
  chi0 = {E^(Mz y), 0}; chiI = sig2.chi0; chiC = {E^(-Mz y), 0};
  addCheck["PAIR_T3ks_zeroModePlusM", AllTrue[{1, -1}, zeroE[D[chi0, y] - NB0[#, Mz].chi0] &] && chi0[[2]] === 0];
  addCheck["PAIR_T3ks_zeroModeImage", AllTrue[{1, -1}, zeroE[D[chiI, y] - NB0[-#, -Mz].chiI] &] && chiI[[1]] === 0 &&
    ((id2 - bagQ[Pi]).(chiI /. y -> -LL)) === {0, 0} && ((id2 + sig3).chiI/2) === {0, 0}];
  addCheck["PAIR_T3ks_zeroModeUntransformedControl", AllTrue[{1, -1}, zeroE[D[chiC, y] - NB0[#, -Mz].chiC] &] && chiC[[2]] === 0 &&
    ((id2 - bagQ[0]).(chiC /. y -> -LL)) === {0, 0}];
  (* first-order k-splitting d eps/dk = j int kappa chi^dagger sigma3 chi / int chi^dagger chi (Hellmann-Feynman), kappa = e^{-Hy-a4} *)
  dEdk[j_, c_] := j Integrate[E^(-H y - a4c) (cj[c].sig3.c), {y, -LL, 0}, Assumptions -> Mz > 0 && H > 0 && LL > 0 && 2 Mz > H]/
     Integrate[cj[c].c, {y, -LL, 0}, Assumptions -> Mz > 0 && LL > 0];
  cM = Simplify[dEdk[1, chi0]]; cMI = Simplify[dEdk[-1, chiI]]; cC = Simplify[dEdk[1, chiC]];
  cMformula = E^(-a4c) (2 Mz/(2 Mz - H)) (1 - E^(-(2 Mz - H) LL))/(1 - E^(-2 Mz LL));
  cCformula = E^(-a4c) (2 Mz/(2 Mz + H)) (E^((2 Mz + H) LL) - 1)/(E^(2 Mz LL) - 1);
  addCheck["PAIR_T3ks_zeroModeSplittingMapsExactly", Simplify[cMI - cM] === 0 && Simplify[cM - cMformula] === 0];
  addCheck["PAIR_T3ks_controlSplittingClosedForm", Simplify[cC - cCformula] === 0];
  (* at M = H = 1, a4 = 0, with Y = e^L > 1: c(M) = 2Y/(Y+1), c_control = (2/3)(Y^2+Y+1)/(Y+1), difference (2/3)(Y-1)^2/(Y+1) > 0 for every L > 0 *)
  sub[e_] := Together[(e /. {H -> 1, Mz -> 1, a4c -> 0}) /. Power[E, ex_] :> Y^Coefficient[Expand[ex], LL]];
  cMY = sub[cMformula]; cCY = sub[cCformula];
  addCheck["PAIR_T3ks_controlDiffersFromPairedProblem", Together[cMY - 2 Y/(Y + 1)] === 0 && Together[cCY - (2/3) (Y^2 + Y + 1)/(Y + 1)] === 0 &&
    Together[cCY - cMY - (2/3) (Y - 1)^2/(Y + 1)] === 0 && Simplify[(2/3) (Y - 1)^2/(Y + 1) > 0, Y > 1] === True];
  addMeas["T3ks_zeroModeSplitting_c_plusM", toStr[cMformula]];
  addMeas["T3ks_zeroModeSplitting_c_minusM_untransformedBC", toStr[cCformula]];
  addMeas["T3ks_c_values_M1_H1_L3_a0_decimal_label_float", ToString[N[{cMY, cCY} /. Y -> E^3, 17], InputForm]];
  (* normalised k = 0 zero-mode densities chi^dagger chi on [-L, 0]: brane-localised versus tip-localised *)
  nb0 = Simplify[(E^(2 Mz y)/Integrate[E^(2 Mz y), {y, -LL, 0}]) /. y -> 0];
  nbC = Simplify[(E^(-2 Mz y)/Integrate[E^(-2 Mz y), {y, -LL, 0}]) /. y -> 0];
  addCheck["PAIR_T3ks_controlZeroModeAtTip", Simplify[nb0 - 2 Mz/(1 - E^(-2 Mz LL))] === 0 && Simplify[nbC - 2 Mz/(E^(2 Mz LL) - 1)] === 0 &&
    Simplify[nbC/nb0 - E^(-2 Mz LL)] === 0];
  (* massive k = 0 levels (Stage 4): eps = sqrt(M^2 + (n pi/L)^2); their sigma2 images solve the -M problem with the transformed BCs;
     the control (-M, even parity, theta = 0) has the same k = 0 energies with M -> -M in the eigenfunction *)
  kn = nn Pi/LL; en = Sqrt[Mz^2 + kn^2];
  lev = {(Mz Sin[kn y] + kn Cos[kn y])/(I j0 en), Sin[kn y]};
  levI = sig2.lev; levC = lev /. Mz -> -Mz;
  addCheck["PAIR_T3ks_massiveLevelsMap", AllTrue[{1, -1}, Function[jj, Simplify[(D[lev, y] - (NB[j0, Mz, 0] /. {eps -> en, vv -> 0}).lev) /. j0 -> jj] === {0, 0} &&
       Simplify[(D[levI, y] - (NB[-j0, -Mz, 0] /. {eps -> en, vv -> 0}).levI) /. j0 -> jj] === {0, 0} &&
       Simplify[(D[levC, y] - (NB[j0, -Mz, 0] /. {eps -> en, vv -> 0}).levC) /. j0 -> jj] === {0, 0}]] &&
    (lev[[2]] /. y -> 0) === 0 && (levI[[1]] /. y -> 0) === 0 && Simplify[(levI[[1]] /. y -> -LL), Element[nn, Integers]] === 0 &&
    (levC[[2]] /. y -> 0) === 0 && Simplify[(levC[[2]] /. y -> -LL), Element[nn, Integers]] === 0];
  logT["T3ks_spectra seconds: ", Round[AbsoluteTime[] - t0]];];

(* ================================================================== *)
(* 10. PAIR_T3emt: the 16-component EMT of a KS orbital               *)
(* ================================================================== *)

bilinearMatrix[expr_] := Table[D[expr, cb[a][y], ch[b][y]], {a, 0, 15}, {b, 0, 15}];
checkT3EMT[] := Module[{gm, chi, chib, Psi, Psid, pc, ls1, Tl, Nf, onRules, Tm, X, X8, ubN, ubBC, ubT, okMat, okStd, okImg, t0 = AbsoluteTime[]},
  gm = diagGeometry[hhMinus];
  chi = Table[ch[n][y], {n, 0, 15}]; chib = Table[cb[n][y], {n, 0, 15}];
  Psi = E^(-I eps x4) E^(I kk x1) E^(-3 H y) chi;
  Psid = E^(I eps x4) E^(-I kk x1) E^(-3 H y) chib;       (* the raw Psi^dagger; the rule matrix is inserted afterwards *)
  pc = zPieces[gm, Psi, Psid];
  ls1 = Expand[pc["kin"] - mm pc["S"]];                    (* one-body part, bare mass mm *)
  Tl = Table[Expand[-(1/4) pc["bar"].gm["gD"][[mu]].pc["Dp"][[nu]]] + Expand[-(1/4) pc["bar"].gm["gD"][[nu]].pc["Dp"][[mu]]] +
     Expand[(1/4) pc["Db"][[mu]].gm["gD"][[nu]].Psi] + Expand[(1/4) pc["Db"][[nu]].gm["gD"][[mu]].Psi] + Expand[gm["g"][[mu, nu]] ls1], {mu, 8}, {nu, 8}];
  Nf = G[0].(MF[y] id16 - I kk E^(-H y - a4c) G[1] + I (eps - VF[y]) G[4]);
  onRules = Join[Table[Derivative[1][ch[n]][y] -> (Nf.chi)[[n + 1]], {n, 0, 15}], Table[Derivative[1][cb[n]][y] -> (chib.hermR[Nf])[[n + 1]], {n, 0, 15}]];
  Tm = Table[Expand[E^(6 H y) gm["gi"][[mu, mu]] Tl[[mu, nu]] /. onRules], {mu, 8}, {nu, 8}];
  addCheck["PAIR_T3emt_phasesCancel", AllTrue[Flatten[Tm], FreeQ[#, x4 | x1] &]];
  X = Map[bilinearMatrix, Tm, {2}];
  addCheck["PAIR_T3emt_bilinearExtraction", AllTrue[Flatten[Table[zzero[Tm[[mu, nu]] - chib.X[[mu, nu]].chi], {mu, 8}, {nu, 8}]], TrueQ]];
  (* cross-check with the Stage-4 formulas (rule matrix B): rho = -T^4_4 = eps n - (M_eff - m) s - v_v n, T^y_y = eps n - m s - kappa k t *)
  ubN = chib.chi; ubBC = chib.BC.chi; ubT = chib.(-G[4].G[1]).chi;
  addCheck["PAIR_T3emt_stage4CrossCheck", zzero[-(chib.Bm.X[[5, 5]].chi) - (eps ubN - (MF[y] - mm) ubBC - VF[y] ubN)] &&
    zzero[chib.Bm.X[[1, 1]].chi - (eps ubN - mm ubBC - E^(-H y - a4c) kk ubT)] && zzero[chib.Bm.X[[3, 3]].chi - ((MF[y] - mm) ubBC + VF[y] ubN)]];
  (* the gamma^8 image: X_{mu nu}(-m, -M_eff) conjugated by gamma^8 equals -X_{mu nu}(m, M_eff), all 64 components *)
  X8 = X /. {mm -> -mm, MF[y] -> -MF[y]};
  okMat = AllTrue[Flatten[Table[zzero[g8.X8[[mu, nu]].g8 + X[[mu, nu]]], {mu, 8}, {nu, 8}]], TrueQ];
  okStd = AllTrue[Flatten[Table[zzero[g8.Bm.X8[[mu, nu]].g8 - Bm.X[[mu, nu]]], {mu, 8}, {nu, 8}]], TrueQ];
  okImg = AllTrue[Flatten[Table[zzero[g8.(-Bm).X8[[mu, nu]].g8 + Bm.X[[mu, nu]]], {mu, 8}, {nu, 8}]], TrueQ];
  addCheck["PAIR_T3emt_gamma8OperatorIdentity64", okMat && ! zzero[X[[5, 5]]]];
  addCheck["PAIR_T3emt_standardRulePlusT", okStd];
  addCheck["PAIR_T3emt_imageRuleMinusT", okImg];
  logT["T3emt seconds: ", Round[AbsoluteTime[] - t0]];];

(* ================================================================== *)
(* 11. PAIR_stat: the statistics sign of the Wick contraction          *)
(* ================================================================== *)

(* single-mode moments <w> of a word w in a (annihilator "a") and a^* (creator "c"), in operator order,
   in the bosonic thermal state p_n = (1 - x) x^n (occupation f = x/(1 - x)): exact series *)
bosonWordMoment[word_List] := bosonWordMoment[word] = Module[{amp = 1, lvl = nq, xw},
  Do[If[op === "a", amp = amp Sqrt[lvl]; lvl = lvl - 1, amp = amp Sqrt[lvl + 1]; lvl = lvl + 1], {op, Reverse[word]}];
  If[Expand[lvl - nq] =!= 0, 0,
   Together[Sum[(1 - xw) xw^nq Expand[amp], {nq, 0, Infinity}] /. xw -> fq/(1 + fq)]]];
(* classical circular Gaussian mode c = r e^{i phi}, <|c|^2> = f: exact moments <cbar^al c^be> from the explicit density *)
gaussMoment[al_Integer, be_Integer] := gaussMoment[al, be] =
  Integrate[Integrate[r^(al + be) E^(I (be - al) ph), {ph, 0, 2 Pi}]/(2 Pi) (2 r/fq) E^(-r^2/fq), {r, 0, Infinity}, Assumptions -> fq > 0];
(* random-phase ensemble with FIXED amplitude r^2 = f: <cbar^al c^be> = delta f^al *)
phaseMoment[al_Integer, be_Integer] := If[al === be, fq^al, 0];

(* four-index moment tensor <b^*_n b^*_p b_q b_r> (normal ordered, template "NO") or <b^*_n b_r b^*_p b_q>
   (the plain product, template "full") of independent modes with occupations fs; modes commute across each other *)
momentTensor[kind_, fs_List] := momentTensor[kind, fs, "NO"];
momentTensor[kind_, fs_List, tmpl_] := Module[{d = Length[fs]},
  Table[Times @@ Table[Module[{w = Select[If[tmpl === "NO", {{n, "c"}, {p, "c"}, {q, "a"}, {rr, "a"}}, {{n, "c"}, {rr, "a"}, {p, "c"}, {q, "a"}}], #[[1]] === md &][[All, 2]], al, be},
       al = Count[w, "c"]; be = Count[w, "a"];
       (Switch[kind, "boson", bosonWordMoment[w], "gauss", gaussMoment[al, be], "phase", phaseMoment[al, be]]) /. fq -> fs[[md]]], {md, d}],
   {n, d}, {p, d}, {q, d}, {rr, d}]];
(* <(Psi^* A Psi)(Psi^* B Psi)> with the normal-ordered (Psi^*_a Psi^*_c Psi_d Psi_b) moments, Psi = U b:
   sum_{n p q r} Mom[n,p,q,r] (U^+ A U)_{n r} (U^+ B U)_{p q} *)
contractNO[Mom_, U_, A_, Bq_] := Module[{At = herm[U].A.U, Bt = herm[U].Bq.U, d = Length[U]},
  Together[Sum[Mom[[n, p, q, rr]] At[[n, rr]] Bt[[p, q]], {n, d}, {p, d}, {q, d}, {rr, d}]]];

checkStatistics[] := Module[{d = 4, cs, cds, dim, Kc1, Kc2, U1c, U2c, Us, fsets, Ah, Bh, okF, okFull, okB, okG, okP, okBG, ferm, rho, Dm, ap, apd,
   hp, Pp, ratio, rho2, SkF, nkF, exkF, dex, Pr, Kr, evs, ex, vvx, vsx, Meffx, rhoR, t0 = AbsoluteTime[]},
  (* exact test matrices *)
  Ah = Module[{X = {{1, (1 + 2 I)/3, -1/2, I/5}, {0, -2/7, (3 - I)/4, 1/3}, {0, 0, 5/6, (-2 + 5 I)/9}, {0, 0, 0, -3/2}}}, X + herm[X]];
  Bh = Module[{X = {{-1/3, 2/5, (1 - I)/2, 0}, {0, 1/4, -I/3, 2/7}, {0, 0, -1, (1 + I)/5}, {0, 0, 0, 2/3}}}, X + herm[X]];
  Kc1 = Module[{X = {{I/3, 1/2 + I/5, -1/4, 0}, {0, -I/2, 1/3, I/7}, {0, 0, 2 I/5, -1/6 + I/3}, {0, 0, 0, I/4}}}, X - herm[X]];
  Kc2 = Module[{X = {{0, 1/3 - I/2, 2/5, -I/3}, {0, I/6, 1/7 + I/4, 1/2}, {0, 0, -I/3, 3/10}, {0, 0, 0, I}}}, X - herm[X]];
  U1c = (IdentityMatrix[d] - Kc1).Inverse[IdentityMatrix[d] + Kc1]; U2c = (IdentityMatrix[d] - Kc2).Inverse[IdentityMatrix[d] + Kc2];
  Us = {IdentityMatrix[d], U1c, U2c};
  addCheck["PAIR_stat_testUnitaries", AllTrue[Us, Together[herm[#].#] === IdentityMatrix[d] &] && herm[Ah] === Ah && herm[Bh] === Bh];
  fsets = {{1, 1, 0, 0}, {1, 0, 1, 1}, {1/3, 2/5, 0, 1}, {1/2, 1/7, 3/4, 2/9}};
  (* (a) anticommuting: exact fermionic Fock space; quasi-free (product) states in the rotated modes *)
  cs = jwOps[d]; cds = herm /@ cs; dim = 2^d;
  ferm = Flatten[Table[Module[{U = Us[[iu]], fs = fsets[[ifs]], D0, rhoF, noF, fullF, SA, SB},
      ap = Table[Sum[Conjugate[U[[a, n]]] cs[[a]], {a, d}], {n, d}]; apd = herm /@ ap;
      D0 = Fold[Dot, IdentityMatrix[dim], Table[(1 - fs[[n]]) ap[[n]].apd[[n]] + fs[[n]] apd[[n]].ap[[n]], {n, d}]];
      rhoF = U.DiagonalMatrix[fs].herm[U];
      SA = Sum[Ah[[a, b]] cds[[a]].cs[[b]], {a, d}, {b, d}]; SB = Sum[Bh[[a, b]] cds[[a]].cs[[b]], {a, d}, {b, d}];
      noF = Together[Tr[D0.Sum[Ah[[a, b]] Bh[[c, e]] cds[[a]].cds[[c]].cs[[e]].cs[[b]], {a, d}, {b, d}, {c, d}, {e, d}]]];
      fullF = Together[Tr[D0.SA.SB]];
      {Together[Tr[D0]] === 1 && AllTrue[Flatten[Table[Together[Tr[D0.cds[[a]].cs[[b]]] - rhoF[[b, a]]] === 0, {a, d}, {b, d}]], TrueQ],
       Together[noF - (Tr[Ah.rhoF] Tr[Bh.rhoF] - Tr[Ah.rhoF.Bh.rhoF])] === 0,
       Together[fullF - (Tr[Ah.rhoF] Tr[Bh.rhoF] - Tr[Ah.rhoF.Bh.rhoF] + Tr[Ah.Bh.rhoF])] === 0}], {iu, 3}, {ifs, 4}], 1];
  addCheck["PAIR_stat_fermionQuasiFreeStates", AllTrue[ferm[[All, 1]], TrueQ]];
  addCheck["PAIR_stat_fermionWickMinus", AllTrue[ferm[[All, 2]], TrueQ] && AllTrue[ferm[[All, 3]], TrueQ] && Length[ferm] === 12];
  (* (b) commuting, quantum bosonic thermal (normal-ordered), (c) classical Gaussian ensemble, (d) fixed-amplitude random phases *)
  addCheck["PAIR_stat_singleModeMoments", bosonWordMoment[{"c", "a"}] === fq && bosonWordMoment[{"c", "c", "a", "a"}] === 2 fq^2 &&
    Together[bosonWordMoment[{"c", "a", "c", "a"}] - (fq + 2 fq^2)] === 0 && gaussMoment[1, 1] === fq && gaussMoment[2, 2] === 2 fq^2 &&
    gaussMoment[2, 1] === 0 && gaussMoment[3, 3] === 6 fq^3 && bosonWordMoment[{"c", "c", "c", "a", "a", "a"}] === 6 fq^3];
  {okB, okG, okP, okBG, okFull} = Transpose[Flatten[Table[Module[{U = Us[[iu]], fs = fsets[[ifs]], MB, MG, MP, rhoB, wick, diag, fullB},
       MB = momentTensor["boson", fs]; MG = momentTensor["gauss", fs]; MP = momentTensor["phase", fs];
       rhoB = U.DiagonalMatrix[fs].herm[U];
       wick = Tr[Ah.rhoB] Tr[Bh.rhoB] + Tr[Ah.rhoB.Bh.rhoB];
       diag = Sum[fs[[n]]^2 (herm[U].Ah.U)[[n, n]] (herm[U].Bh.U)[[n, n]], {n, d}];
       (* the full (not normal-ordered) bosonic product from its own word moments <b^*_n b_r b^*_p b_q> *)
       fullB = contractNO[momentTensor["boson", fs, "full"], U, Ah, Bh];
       {Together[contractNO[MB, U, Ah, Bh] - wick] === 0, Together[contractNO[MG, U, Ah, Bh] - wick] === 0,
        Together[contractNO[MP, U, Ah, Bh] - (wick - diag)] === 0 && If[Max[fs] > 0, Together[diag] =!= 0, True], MB === MG,
        Together[fullB - (wick + Tr[Ah.Bh.rhoB])] === 0}], {iu, 3}, {ifs, 4}], 1]];
  addCheck["PAIR_stat_bosonThermalWickPlus", AllTrue[okB, TrueQ]];
  addCheck["PAIR_stat_classicalGaussianWickPlus", AllTrue[okG, TrueQ] && AllTrue[okBG, TrueQ]];
  addCheck["PAIR_stat_fixedAmplitudePhasesDeviate", AllTrue[okP, TrueQ]];
  (* (e) the Hartree-Fock energy with the expectation rule: two-point function K = rho B (G_ab = <Psi^*_a Psi_b> = (rho B)_ba) *)
  rhoR = Module[{X = Table[(geoRandom[77, 256][[16 (i - 1) + k]]) + I (geoRandom[78, 256][[16 (i - 1) + k]]), {i, 16}, {k, 16}]}, X + herm[X]];
  addCheck["PAIR_stat_expectationRuleTraces", Together[Tr[C16.rhoR.Bm] - Tr[BC.rhoR]] === 0 && Together[Tr[C16.rhoR.Bm.C16.rhoR.Bm] - Tr[BC.rhoR.BC.rhoR]] === 0];
  (* filled shell of 8 positive-energy states at one 4-momentum p (y, x1, x2, x3) *)
  hp = -I m G[4] - G[4].(p0 G[0] + p1 G[1] + p2 G[2] + p3 G[3]);
  Pp = (id16 + hp/Ep)/2;
  ratio = Simplify[(Tr[BC.Pp.BC.Pp]/Tr[BC.Pp]^2) /. Ep -> Sqrt[m^2 + p0^2 + p1^2 + p2^2 + p3^2]];
  addMeas["stat_filledShellRatio", toStr[ratio]];
  addCheck["PAIR_stat_filledShellExchangeRatio", ratio === 1/8 && Simplify[Tr[BC.Pp] - 8 m/Ep] === 0 &&
    Simplify[((lam/2) (Tr[BC.Pp]^2 + sgs Tr[BC.Pp.BC.Pp]) - (lam/2) Tr[BC.Pp]^2 (1 + sgs/8)) /. Ep -> Sqrt[m^2 + p0^2 + p1^2 + p2^2 + p3^2]] === 0];
  (* uniform gas: block form and isotropy (Stage 4), statistics sign sgs *)
  rho2 = (nb id2 + sb sig2 + tb sig3 + cb0 sig1)/2;
  ex = sgs (lam/2) 8 ((nq8/8)^2 + (Sq8/8)^2)/2;
  addCheck["PAIR_stat_uniformGasExchange", Together[Tr[sig2.rho2.sig2.rho2] - (nb^2 + sb^2 - tb^2 - cb0^2)/2] === 0 &&
    Together[ex - sgs (lam/32) (nq8^2 + Sq8^2)] === 0 && Together[(ex /. sgs -> 1) - (lam/32) (nq8^2 + Sq8^2)] === 0 &&
    Together[(ex /. sgs -> -1) + (lam/32) (nq8^2 + Sq8^2)] === 0];
  (* LDA potentials and the effective mass *)
  vvx = D[sgs (lam/32) (nq8^2 + Sq8^2), nq8]; vsx = D[sgs (lam/32) (nq8^2 + Sq8^2), Sq8]; Meffx = m + lam Sq8 + vsx;
  addCheck["PAIR_stat_ldaPotentials", Together[vvx - sgs (lam/16) nq8] === 0 && Together[vsx - sgs (lam/16) Sq8] === 0 &&
    Together[(Meffx /. sgs -> 1) - (m + (17/16) lam Sq8)] === 0 && Together[(Meffx /. sgs -> -1) - (m + (15/16) lam Sq8)] === 0];
  (* T = 0 closed forms (d = 4 spatial dimensions, degeneracy 8) *)
  nkF = kF^4/(4 Pi^2); SkF = (m/(3 Pi^2)) ((kF^2 - 2 m^2) Sqrt[m^2 + kF^2] + 2 m^3);
  exkF = sgs (lam/32) (nkF^2 + SkF^2); dex = D[exkF, kF]/D[nkF, kF];
  addCheck["PAIR_stat_T0TotalDerivative", Simplify[dex - sgs (lam/16) (nkF + SkF m/Sqrt[m^2 + kF^2])] === 0 &&
    Limit[exkF/((lam/2) SkF^2), kF -> 0, Assumptions -> m > 0 && lam > 0] === sgs/8];
  (* positivity: the covariance implied by the expectation rule, K = rho B, is indefinite for a filled shell; a classical
     Gaussian ensemble has positive semidefinite covariance.  With the positive classical covariance K = rho the filled shell
     has zero charge and zero scalar density *)
  Pr = (id16 - I G[4])/2;           (* p = 0, m = 1, E = 1 *)
  Kr = Pr.Bm; evs = Sort[Eigenvalues[Kr]];
  addMeas["stat_restShellCovarianceEigenvalues", toStr[evs]];
  addCheck["PAIR_stat_expectationRuleCovarianceIndefinite", evs === Join[ConstantArray[-1, 4], ConstantArray[0, 8], ConstantArray[1, 4]] &&
    Simplify[Tr[Bm.Pp]] === 0 && Simplify[Tr[C16.Pp]] === 0 && Simplify[Tr[Bm.Bm.Pp]] === 8];
  logT["stat seconds: ", Round[AbsoluteTime[] - t0]];
  $theory["statistics"] = <|
    "wick" -> <|"anticommuting" -> "exact fermionic Fock space (4 modes, Jordan-Wigner), quasi-free states D = prod_n [(1 - f_n) a_n a_n^* + f_n a_n^* a_n] in 3 bases x 4 occupation sets (pure Slater determinants and mixed states): <:(Psi^* A Psi)(Psi^* B Psi):> = Tr(A rho) Tr(B rho) - Tr(A rho B rho), <(Psi^* A Psi)(Psi^* B Psi)> = the same + Tr(A B rho), rho_ba = <Psi^*_a Psi_b>",
      "commutingQuantum" -> "bosonic thermal quasi-free states (exact series): <:(Psi^* A Psi)(Psi^* B Psi):> = Tr(A rho) Tr(B rho) + Tr(A rho B rho); full product + Tr(A B rho)",
      "commutingClassical" -> "classical circular Gaussian ensemble of commuting modes (exact moment integrals <cbar^a c^b> = delta_ab a! f^a): <(Psi^* A Psi)(Psi^* B Psi)> = Tr(A rho) Tr(B rho) + Tr(A rho B rho) with no extra term; the moment tensor equals the bosonic normal-ordered one",
      "fixedAmplitudePhases" -> "a random-phase ensemble with FIXED amplitudes (|c_n|^2 = f_n) gives the Gaussian result minus sum_n f_n^2 (U^+ A U)_nn (U^+ B U)_nn: the + exchange sign of the commuting model requires Gaussian (Rayleigh) amplitudes"|>,
    "hartreeFock" -> <|"rule" -> "two-point function of the expectation rule: G_ab = <Psi^dagger_a Psi_b> = (rho B)_ba (Stage 4), i.e. the Wick formulas with rho -> rho B and A = B = C",
      "formula" -> "E_HF = (lambda/2) [ Tr(BC rho)^2 + sg Tr(BC rho BC rho) ], sg = -1 (dirac16complex), sg = +1 (dirac16complex00)",
      "filledShell" -> "Tr(BC P_+ BC P_+) = Tr(BC P_+)^2/8 (8 states at one momentum): E_x = sg E_H/8, i.e. -E_H/8 (anticommuting), +E_H/8 (commuting)",
      "uniformGas" -> "e_x = sg (lambda/32) (n^2 + S^2) for every T: -(lambda/32)(n^2 + S^2) (dirac16complex), +(lambda/32)(n^2 + S^2) (dirac16complex00)",
      "lda" -> "v_v = sg (lambda/16) n, v_s = sg (lambda/16) S, M_eff = m + lambda S_p + v_s = m + (1 + sg/16) lambda S_p: m + (15/16) lambda S_p (dirac16complex), m + (17/16) lambda S_p (dirac16complex00); v_x = v_v = +(lambda/16) n_p for dirac16complex00",
      "T0" -> "de_x/dn |_{T=0} = sg (lambda/16) [ n + S m/E_F ]; rest-gas limit e_x/e_H -> sg/8",
      "verdict" -> "with the Stage-4 expectation-rule matrices the statement of STAGE5_SPEC section 4 holds exactly: only the sign of the exchange term changes"|>,
    "positivity" -> <|"measured" -> "the covariance implied by the expectation rule, K = rho B, restricted to a filled rest shell has eigenvalues (+1)^4 (-1)^4 (0)^8: it is indefinite, while the covariance of a classical Gaussian ensemble is positive semidefinite",
      "consequence" -> "the dirac16complex00 Kohn-Sham model with the expectation rule is a FORMAL (Krein-signed) Gaussian functional: for modes of Krein sign -1 (4 of the 8 blocks, B = j s2) it does not correspond to a probability distribution of classical fields. With the positive classical covariance K = rho instead, a filled shell has Tr(B P_+) = 0 (zero charge) and Tr(C P_+) = 0 (zero scalar density) at every momentum. The Stage-5 model keeps the expectation rule by prescription (STAGE5_SPEC section 4), so that the two theories differ only in the exchange sign; this is a modelling choice, stated as such.",
      "status" -> "a DFT-motivated mean field of a random-phase (Gaussian) ensemble of classical modes with Fermi-Dirac occupations (Pauli filling imposed by prescription), not a quantum theory of commuting spinors (which would violate the spin-statistics connection)"|>|>;];

(* ================================================================== *)
(* 12. PAIR_totals: explicit pair totals at the field level (G1)       *)
(* ================================================================== *)

checkTotals[] := Module[{fj, geo, mm = g1Masses[[1]], ll = g1Couplings[[1]], sol, okS, fld, fld8, lag, lag8, T, T8, u = G[0], Lam, geoTw, fldU, lagU, TU, t0 = AbsoluteTime[]},
  fj = g1FrameJet[1]; geo = jetGeo[fj];
  {sol, okS} = geoSolveOnShell[geo, randField[5151], mm, ll];
  fld = geoFieldJets @@ sol; fld8 = geoFieldJets @@ mapField[g8, sol];
  lag = geoLagJets[geo, fld, mm, ll]; lag8 = geoLagJets[geo, fld8, -mm, -ll];
  T = geoEMTJets[geo, lag]; T8 = geoEMTJets[geo, lag8];
  (* T1 pair {(m, lambda, Psi), (-m, -lambda, gamma^8 Psi)} in the same gravitational field *)
  addCheck["PAIR_totals_fieldLevelChiralPair", okS && zeroT[T + T8] && zeroT[currentJets[geo, lag] + currentJets[geo, lag8]] &&
    zeroT[lag["L"] + lag8["L"]] && zeroT[lag["S"] + lag8["S"] - 2 lag["S"]] && ! zeroT[lag["S"]] && ! zeroT[Map[First, T, {2}]]];
  (* T2 pair {(m, lambda, e, Psi), (-m, lambda, e R_u, u Psi)} with u = gamma^0 (twisted frame reflection, same metric) *)
  Lam = lambdaOf[u]; geoTw = jetGeo[transFrameJet[fj, -etaM.Transpose[Lam].etaM]];
  fldU = geoFieldJets @@ mapField[u, sol]; lagU = geoLagJets[geoTw, fldU, -mm, ll]; TU = geoEMTJets[geoTw, lagU];
  addCheck["PAIR_T2frame_onShellImage", zeroT[fieldEqJets[geoTw, lagU, -mm, ll]] && ! zeroT[fieldEqJets[geoTw, geoLagJets[geoTw, fldU, mm, ll], mm, ll]]];
  addCheck["PAIR_totals_fieldLevelMirrorPair", zeroT[TU + T - 2 T] && zeroT[currentJets[geoTw, lagU] + currentJets[geo, lag] - 2 currentJets[geo, lag]] &&
    zeroT[lagU["S"] + lag["S"]] && zeroT[lagU["L"] + lag["L"] - 2 lag["L"]]];
  logT["totals seconds: ", Round[AbsoluteTime[] - t0]];];

(* ================================================================== *)
(* 13. theory export (pairing-theory.json)                             *)
(* ================================================================== *)

chk[names__String] := Association[(# -> TrueQ[$checks[#]]) & /@ {names}];

buildTheory[] := Module[{},
  $theory["T1"] = <|
    "name" -> "T1: the chirality map gamma^8 (field level, arbitrary gravitational field, both statistics)",
    "statement" -> "For every vielbein e (hence every metric g = e eta e^T and its Levi-Civita spin connection), every mass m and coupling lambda of U = (lambda/2) S^2, and every field configuration Psi (off shell), with Psi_- := gamma^8 Psi: Psibar_- = Psibar gamma^8, S[Psi_-] = S[Psi], the kinetic term changes sign, j^mu[Psi_-] = -j^mu[Psi], L_{m,lambda}[gamma^8 Psi] = -L_{-m,-lambda}[Psi], E_{-m,-lambda}[gamma^8 Psi] = -gamma^8 E_{m,lambda}[Psi] (field equation) and the conjugate equation likewise, T_{mu nu}[gamma^8 Psi; -m, -lambda] = -T_{mu nu}[Psi; m, lambda] (all 36 components). Hence Psi solves EL_{m,lambda} iff gamma^8 Psi solves EL_{-m,-lambda}. The same identities hold for Grassmann-odd components (dirac16complex) and for commuting components (dirac16complex00).",
    "proof" -> "gamma^8 is Hermitian, (gamma^8)^2 = 1, gamma^8 gamma^a = -gamma^a gamma^8, [gamma^8, C] = 0, [gamma^8, S^{ab}] = 0 (so [gamma^8, Omega_mu] = 0 for every connection). Every term of L, of the field equations, of T_{mu nu} and of j^mu is a bilinear Psi^dagger X Psi with X in {C gamma^a, C gamma^a S^{bc}, C S^{bc} gamma^a} (one gamma: gamma^8 X gamma^8 = -X) or X = C (mass term, S: gamma^8 C gamma^8 = +C), multiplied by geometric coefficients (e_a^mu, omega_{mu ab}, sqrt|g|, g_{mu nu}) that the map does not touch; U = (lambda/2) S^2 is even. The map is linear and keeps the order Psi^dagger ... Psi, so it is compatible with Grassmann-odd components (in the notebook basis it is the automorphism theta_a -> chi(a) theta_a of the Grassmann algebra). QED; verified as a polynomial identity in completely generic independent symbols (PAIR_T1generic_*), with exact jets of the general non-diagonal vielbein G1 at three points (PAIR_T1jets_*) and with a Grassmann algebra of 288 odd generators (PAIR_T1grassmann_*).",
    "fieldsCovered" -> "dirac16complex: Grassmann-odd components (PAIR_T1grassmann_* with 288 odd generators; the generic-symbol identities keep the order Psi^dagger ... Psi); dirac16complex00: commuting components (PAIR_T1generic_*, PAIR_T1jets_* with exact rational field jets, PAIR_T1primordial_* with generic functions of all eight coordinates in the Stage-2 primordial field with an arbitrary a4(t))",
    "primordialField" -> "in the notebook chart of the primordial field (z = 6 H x0, t = H x4, a4 an arbitrary function) the identities L_{m,lambda}[gamma^8 Psi] = -L_{-m,-lambda}[Psi], E_{-m,-lambda}[gamma^8 Psi] = -gamma^8 E_{m,lambda}[Psi], T_{mu nu}[gamma^8 Psi; -m, -lambda] = -T_{mu nu}[Psi; m, lambda] (64 components) and j -> -j hold for generic fields of all eight coordinates (PAIR_T1primordial_*)",
    "vielbeinForm" -> "equivalently, (gamma^8, e -> -e) is an exact symmetry (the frame map -1 lies in SO_0(4,4) and gamma^8 in Spin_0(4,4)), so T1 is the same as reversing the sign of the vielbein at fixed Psi: L_{m,lambda}[-e, Psi] = -L_{-m,-lambda}[e, Psi] (g, sqrt|g| and Omega are unchanged, gamma^mu -> -gamma^mu)",
    "naiveFormFails" -> "at fixed lambda the map gives L_{m,lambda}[gamma^8 Psi] + L_{-m,lambda}[Psi] = -lambda S^2 != 0 (CONTRACT erratum E2)",
    "kreinMetric" -> "gamma^8 B gamma^8 = -B: the image field has the canonical anticommutator -B (it is canonically a field of -L_{-m,-lambda}); see T1krein",
    "checks" -> chk["PAIR_algebra_bilinearParities", "PAIR_T1generic_lagrangian", "PAIR_T1generic_fieldEquation", "PAIR_T1generic_conjugateFieldEquation",
      "PAIR_T1generic_emtAll36", "PAIR_T1generic_current", "PAIR_T1grassmann_lagrangian", "PAIR_T1grassmann_diracOperator", "PAIR_T1grassmann_emt",
      "PAIR_T1grassmann_current", "PAIR_T1jets_lagrangian", "PAIR_T1jets_emt", "PAIR_T1jets_fieldEquations", "PAIR_T1jets_onShellImage",
      "PAIR_T1jets_conservationBoth", "PAIR_T1jets_vielbeinSignFlipIsT1", "PAIR_T1jets_gamma8WithFrameSignIsSymmetry", "PAIR_T1krein_imageAnticommutatorMinusB",
      "PAIR_T1primordial_lagrangian", "PAIR_T1primordial_diracOperator", "PAIR_T1primordial_emt64", "PAIR_T1primordial_current"],
    "corollaryPair" -> <|
      "statement" -> "COROLLARY (pair, proved): for Psi_+ with (m, lambda) and Psi_- = gamma^8 Psi_+ with (-m, -lambda) in the SAME gravitational field: T^pair_{mu nu} = T_{mu nu}[Psi_+; m, lambda] + T_{mu nu}[Psi_-; -m, -lambda] = 0 identically, j^pair = 0 (total charge Q = integral sqrt|g| j^4 d^7x = 0), L^pair = 0 (total action 0), S^pair = 2 S; total energy, momentum and stresses vanish at every point, in any gravitational field, at every x4, in particular at x4 = 0. The Einstein (or Einstein-Lovelock) equations with the pair as source are the source-free equations.",
      "hypotheses" -> "(i) the -M member carries the coupling -lambda (for lambda = 0 both members are the same free field with masses +m and -m); (ii) for the quantum field dirac16complex the -M member is the image field gamma^8 Psi_+ on the same state space, whose canonical anticommutator is -B (Krein metric reversed); an independently quantised -m universe with its own positive (J = B) structure has the SAME energy-momentum as the +m universe and the pair does not cancel (T1krein); (iii) for the classical field dirac16complex00 no further hypothesis is needed (the identity is between c-number fields).",
      "noGoFixedLambda" -> "analytic remark (not machine-checked beyond PAIR_T1generic_naiveFixedLambdaFails): for lambda != 0 no map Psi -> M Psi (M constant, any frame change) gives (m, lambda) -> (-m, lambda) with L -> -L for commuting fields, because the quartic parts would require S_M^2 = -S^2 with the real bilinear S_M = Psi^dagger M^dagger C M Psi; the even interaction forces lambda -> -lambda in every T -> -T map",
      "meaning" -> "a theorem about kinematics and constraints: a {+M, -M} pair of this type carries no net energy-momentum and no net charge, so its appearance from the field-free state is consistent with every conservation law and with the gravitational constraints. It is NOT a computed creation rate or amplitude.",
      "checks" -> chk["PAIR_T1jets_pairEMTAndCurrentVanish", "PAIR_totals_fieldLevelChiralPair", "PAIR_T1generic_emtAll36"]|>|>;
  $theory["T2"] = <|
    "name" -> "T2: the mirror map (Pin(4,4) reflection of character -1), (m, lambda) -> (-m, lambda)",
    "statement" -> "For a unit vector u = v_a gamma^a with n(u) = eta(v, v) = +1 (space-like; character chi(u) = -n(u) = -1, u^dagger C = chi C u^{-1}), the transformation Psi -> u Psi together with the frame reflection e -> e R_u of the vielbein (twisted lift, gamma'^mu = -u gamma^mu u^{-1}; the metric, sqrt|g| and Omega_mu -> u Omega_mu u^{-1} as required) gives L_{m,lambda}[e R_u, u Psi] = L_{-m,lambda}[e, Psi], T_{mu nu}[e R_u, u Psi; m, lambda] = T_{mu nu}[e, Psi; -m, lambda] (same metric, same coordinates: T -> +T), S -> -S, j -> +j. Solutions with (m, lambda) map onto solutions with (-m, lambda) (the SAME lambda). Equivalently: gamma^8 u with the untwisted frame action e -> -e R_u. For time-like u (chi = +1) the twisted action gives -L_{-m,-lambda} (a T1-type map) and the untwisted action is an exact symmetry.",
    "reflectionsThatDoIt" -> "exactly the space-like unit vectors (n(u) = +1): gamma^0 (hidden space x0 ~ y), gamma^1, gamma^2, gamma^3 (3-space) and every space-like combination (verified on a general rational unit vector); the time-like ones gamma^4..gamma^7 do not",
    "table" -> $theory["T2frameTable"],
    "tableKey" -> "per unit vector u: norm n(u) = eta(v, v); character chi(u) (u^dagger C = chi C u^{-1}); uBudaggerSign = +1 if u B u^dagger = B, -1 if = -B, 0 if neither (general vectors mix the two); R_u = the hyperplane reflection (twisted frame action e -> e R_u, realised as e -> -e (eta Lambda^T eta) with u gamma^a u^{-1} = Lambda^c_a gamma^c); the untwisted action is e -> e (eta Lambda^T eta)",
    "coordinateAction" -> $theory["T2z2"],
    "stage4Connection" -> "in the Z2-extended static primordial field the isometry y -> -y realises the frame reflection R_{gamma^0}; T2 with u = gamma^0 is the Stage-4 reflection P_A: Psi(-y) = +-gamma^0 Psi(y); it maps (m(y), lambda) to (-m(-y), lambda), so a Z2-symmetric configuration exists iff the mass function is odd: the Z2 mirror universe of mass -M with the same lambda, the same energy density and pressures (EMT pull-back) and the same charge",
    "remark" -> "the sign of m relative to the frame orientation is not an invariant of the theory; the T2 pair is the +M universe and its mirror image: its energy-momentum doubles (T^pair = 2T), it does not cancel",
    "checks" -> chk["PAIR_T2frame_characterIsMinusNorm", "PAIR_T2frame_frameReflectionsGeometry", "PAIR_T2frame_twistedSpacelikeMapsToMinusMSameLambda",
      "PAIR_T2frame_gamma8TimesUntwistedSpacelike", "PAIR_T2frame_untwistedSpacelikeContractE3", "PAIR_T2frame_twistedTimelike", "PAIR_T2frame_onShellImage",
      "PAIR_T2z2_diracOperator", "PAIR_T2z2_emtPullback", "PAIR_T2z2_symmetricIffOddMass", "PAIR_T2z2_PBfieldLevelFlipsLambda", "PAIR_totals_fieldLevelMirrorPair"]|>;
  $theory["T3"] = <|
    "name" -> "T3: the Kohn-Sham level (static primordial field, eight 2x2 blocks, both statistics)",
    "blockMaps" -> $theory["T3blockMaps"],
    "theoremStandardRule" -> "THEOREM (proved): let the +M universe be the Stage-4 KS problem with (m, lambda, statistics sg, parity p at the brane, tip bag angle theta, occupations by Fermi-Dirac at T, N particles). The -M universe with (-m, the SAME lambda, the same sg, parity -p, bag angle pi - theta) is its exact image under chi -> sigma2 chi in the partner block (j, s2, s3) -> (-j, s2, s3), k unchanged (the block form of gamma^8 with the standard expectation rule). The KS operators are unitarily equivalent (sigma2 h_j(M_eff) sigma2 = h_{-j}(-M_eff), with M_eff -> -M_eff, v_v -> v_v self-consistently), the domains correspond (p -> -p, theta -> pi - theta), the Mermin functional is invariant, so the spectra (with multiplicities), occupations, mu, E, F, S_ent, the KS gap, the particle-hole list and the Delta-SCF energies are identical, n_p(y), t, c and the EMT profiles (rho, p_y, p_3, p_t and their averages) are identical, S_p(y) -> -S_p(y) and M_eff(y) -> -M_eff(y). The SCF iteration map is equivariant, so every iterate, the lambda-continuation branch (lambda is not changed) and hence the KS ground state (STAGE4_SPEC E4.8) and the first excited state (KS gap, particle-hole pairs with the occupation floor, Delta-SCF) map exactly. The sigma1 route (gamma^1: same j, k -> -k, theta -> theta + pi) gives the same result over closed shells {k, -k}.",
    "theoremImageRule" -> "THEOREM (proved): the gamma^8 image of the +M KS state with the Krein metric -B (T1) solves the KS equations of (-m, -lambda) with the same orbitals sigma2 chi, the same eigenvalues (x4-frequencies) and occupations; its one-body densities and energies change sign: n -> -n (charge), S -> +S, t -> -t, c -> -c, E -> -E, T_{mu nu} -> -T_{mu nu}; the orbital energies (Janak) are -eps, so at finite T the image is a stationary state of F_- at temperature -T and chemical potential -mu: F_-(-T) = -F_+(T). The image is therefore obtained from the standard-rule -M run by reversing the sign of every one-body density and energy and of lambda.",
    "stage4Z2Pair" -> "the Stage-4 parity conditions at the brane are the Z2 identification Psi(-y) = +-gamma^0 Psi(y) (P_A); by T2 (PAIR_T2z2_*) a Stage-4 KS state of the +M universe on y < 0 continues across the brane to a universe of mass -M(-y) on y > 0 with the same lambda, the same energy density and pressures (EMT pull-back), the same charge and the opposite scalar density; the brane carries the Israel stress of Stage 4. Every Stage-4 KS state is therefore already a {+M, -M} mirror pair across the brane.",
    "whatMustTransform" -> <|"lambda" -> "unchanged for the ordinary -M universe (standard rule); -lambda for the Krein image (T1); the ordinary KS problem with -lambda does NOT map (PAIR_T3ks_sigma2KSOperatorEquivariant, second part)",
      "parity" -> "p -> -p (even chi_2(0) = 0 <-> odd chi_1(0) = 0)",
      "bagAngle" -> "theta -> pi - theta (sigma2 route, same k); Stage-4 default theta = 0 -> pi; the asymptotic prescription theta(k) = -sgn(k) pi/2 is invariant",
      "blocks" -> "j -> -j (Rust block type s -> -s), s2, s3, k unchanged; orbital (a, b) -> (b, a) in the Rust notation chi = (a, i b)",
      "statistics" -> "unchanged; both statistics signs are covered by the same proof (sg kept symbolic)"|>,
    "untransformedBCControl" -> <|
      "statement" -> "if the -M universe keeps the untransformed boundary conditions (p, theta), it is the image of the +M problem with (-p, pi - theta), NOT of (+M, p, theta): the pairing fails in general",
      "exact" -> "k = 0, constant M, v_v = 0, even parity and theta = 0: the +M problem has the brane zero mode (e^{My}, 0) (eps = 0); the -M problem with the same BCs has the tip-localised zero mode (e^{-My}, 0) (normalised brane density ratio e^{-2ML}); the massive k = 0 levels +-sqrt(M^2 + (n pi/L)^2) coincide, but the first-order k-splitting of the zero-mode band changes from c(M) = e^{-a4} (2M/(2M-H)) (1 - e^{-(2M-H)L})/(1 - e^{-2ML}) to c_ctrl = e^{-a4} (2M/(2M+H)) (e^{(2M+H)L} - 1)/(e^{2ML} - 1); at M = H: c_ctrl - c(M) = (2/3)(Y - 1)^2/(Y + 1) > 0, Y = e^{HL} > 1, for every L; with the transformed BCs (odd parity, theta = pi) the -M zero mode (0, e^{My}) has exactly c(M)",
      "valuesM1H1L3a0_floatLabelled" -> $meas["T3ks_c_values_M1_H1_L3_a0_decimal_label_float"],
      "closedForms" -> <|"cPaired" -> $meas["T3ks_zeroModeSplitting_c_plusM"], "cControl" -> $meas["T3ks_zeroModeSplitting_c_minusM_untransformedBC"]|>,
      "consequence" -> "the k != 0 spectra, hence occupations, energies, densities and the EMT of the untransformed -M universe differ from those of the +M universe; the numerical control must show this",
      "checks" -> chk["PAIR_T3ks_zeroModeUntransformedControl", "PAIR_T3ks_controlSplittingClosedForm", "PAIR_T3ks_controlDiffersFromPairedProblem", "PAIR_T3ks_controlZeroModeAtTip"]|>,
    "pairTotalsKS" -> <|
      "mirrorPair" -> "ordinary -M universe (standard rule, the same lambda): E_pair = 2 E_+, F_pair = 2 F_+, charge N_pair = 2N, S_pair(y) = 0, T_pair = 2 T_+ (rho, p_y, p_3, p_t doubled)",
      "kreinImagePair" -> "Krein image (T1, -lambda, metric -B): E_pair = 0, charge 0, T_pair = 0 pointwise, S_pair = 2 S_+; the image is computed from the ordinary -M run (identical orbitals, eigenvalues, occupations) by reversing the sign of all one-body densities and energies",
      "checks" -> chk["PAIR_totals_ksMirrorPair", "PAIR_totals_ksKreinImagePair", "PAIR_T3ks_imageRuleEnergyOdd", "PAIR_T3ks_occupationsAndTemperature"]|>,
    "numericsPrescription" -> <|
      "plusM" -> "the Stage-4 KS problem (m, lambda, statistics, parity sectors +-, tip bag b(-L) = 0 i.e. theta = 0)",
      "minusMTransformed" -> "m -> -m everywhere (bare mass and M_eff), lambda unchanged, statistics unchanged, parity p -> -p (the + sector b(0) = 0 of the +M run corresponds to the - sector a(0) = 0 of the -M run), tip bag theta = pi (a(-L) = 0), block type s -> -s, same k and N and T",
      "minusMUntransformedControl" -> "m -> -m, everything else as for +M (same parity labels, b(-L) = 0)",
      "expectedIdentities" -> "per k and block pair: eigenvalue lists identical; mu, E, F, S_ent, KS gap, particle-hole list, Delta-SCF identical; n_p(y), rho(y), p_y(y), p_3(y), p_t(y), v_x(y) identical; S_p(y) and M_eff(y) change sign; to solver precision",
      "pairTotalsToReport" -> "mirror pair = (+M run) + (transformed -M run): 2E, 2N, S = 0, 2 <rho>, 2 <p>; Krein image pair = (+M run) - (transformed -M run) for every one-body density and energy (the image carries the Krein metric -B and -lambda): E = 0, charge 0, <rho> = <p> = 0 to solver precision, S = 2 <S_p>",
      "statisticsFormulas" -> "dirac16complex: e_x = -(lambda/32)(n^2 + S^2), M_eff = m + (15/16) lambda S_p, v_x = -(lambda/16) n_p; dirac16complex00: e_x = +(lambda/32)(n^2 + S^2), M_eff = m + (17/16) lambda S_p, v_x = +(lambda/16) n_p"|>,
    "checks" -> chk["PAIR_T3block_gamma8IsSigma2BetweenPartnerBlocks", "PAIR_T3block_gamma1IsSigma1InEveryBlock", "PAIR_T3block_sigma2MapsBlockODE",
      "PAIR_T3block_hamiltonianSigma2", "PAIR_T3block_parityMap", "PAIR_T3block_bagAngleMap", "PAIR_T3block_densityAndCurrentMaps",
      "PAIR_T3block_potentialsStandardRule", "PAIR_T3block_potentialsImageRule", "PAIR_T3ks_stationarityBothStatistics", "PAIR_T3ks_sigma2FunctionalInvariant",
      "PAIR_T3ks_sigma2KSOperatorEquivariant", "PAIR_T3ks_sigma1FunctionalInvariant", "PAIR_T3ks_zeroModeSplittingMapsExactly", "PAIR_T3ks_massiveLevelsMap",
      "PAIR_T3emt_gamma8OperatorIdentity64", "PAIR_T3emt_standardRulePlusT", "PAIR_T3emt_imageRuleMinusT", "PAIR_T3emt_stage4CrossCheck"]|>;
  $theory["pairTotals"] = <|
    "fieldLevel" -> <|"chiralPairT1" -> "{(m, lambda, Psi), (-m, -lambda, gamma^8 Psi)}: T = 0, j = 0, L = 0, S = 2S (PAIR_totals_fieldLevelChiralPair)",
      "mirrorPairT2" -> "{(m, lambda, e, Psi), (-m, lambda, e R_u, u Psi)}, u space-like: T = 2T, j = 2j, L = 2L, S = 0 (PAIR_totals_fieldLevelMirrorPair)"|>,
    "ksLevel" -> $theory["T3"]["pairTotalsKS"]|>;
  $theory["notProved"] = {
    "no dynamical creation rate, amplitude or probability of pair creation is derived; no wave function of the universe",
    "the theorems do not show that pairs ARE created at x4 = 0; T1 shows that a {+M, -M} pair of the chiral type carries zero total energy-momentum, charge and action in every gravitational field at every x4, so its creation is consistent with all conservation laws and constraints",
    "the chiral (cancelling) pair needs lambda -> -lambda (or lambda = 0) and, for the quantum field, the reversed Krein metric -B for the -M member; with the positive (J = B) quantisation of the -M universe as an independent field the pair is the T2-type mirror pair, whose energy-momentum doubles",
    "the Kohn-Sham statements are about the mean-field (Hartree-Fock-LDA, no correlation) model of Stage 4; for dirac16complex00 the model is a formal Krein-signed Gaussian functional with Pauli filling imposed by prescription",
    "the primordial field requires rho_req = -21 H^2/kappa < 0 (Stage 4); the pairing theorems do not change the Stage-4 sourcing analysis"};
  $theory["notebookHypothesis"] = "cells 6, 7, 17 of the author's notebook: 'at time x4 = 0 a pair of universes with masses +-M is created' / 'TODO: prove Universe(s) of masses +-M are created in pairs'. Proved here: T1 (a chiral pair with -lambda has T^pair = 0, j^pair = 0 in every field), T2 (the mirror universe of mass -M with the same lambda is the exact reflection image, equal energy), T3 (both statements at the Kohn-Sham level, exact block maps and boundary conditions). Interpretation, not derived: that such a pair is actually produced.";];

(* ================================================================== *)
(* 14. entry point                                                     *)
(* ================================================================== *)

D16PairRun[repoRoot_String] := Module[{fixFile, ksFile, res, t0 = AbsoluteTime[], step},
  $checks = <||>; $meas = <||>; $theory = <||>;
  fixFile = FileNameJoin[{repoRoot, "artifacts", "dirac16complex", "arbitrary-field", "algebra-fixture.json"}];
  ksFile = FileNameJoin[{repoRoot, "artifacts", "dirac16complex", "kohn-sham", "kohn-sham-theory.json"}];
  step[name_, body_] := (logT[name]; body);
  SetAttributes[step, HoldRest];
  $theory["conventions"] = <|
    "coordinates" -> "x0..x7 zero-based; x4 = time; in the primordial field the proper hidden-space coordinate y = ln(sin z)/(6H) <= 0 (y < 0 the notebook patch, y > 0 the Z2 mirror side)",
    "frame" -> "eta = diag(+1,+1,+1,+1,-1,-1,-1,-1); gamma^a = [[0, taubar_a],[tau_a, 0]] (algebra-fixture.json); C = gamma^0 gamma^1 gamma^2 gamma^3; Psibar = Psi^dagger C; B = -i C gamma^4; gamma^8 = gamma^0...gamma^7 = diag(-I8, +I8); Omega_mu = (1/8) omega_{mu ab} [gamma^a, gamma^b]",
    "lagrangian" -> "L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m Psibar Psi - (lambda/2)(Psibar Psi)^2 ] for both fields (STAGE5_SPEC (L1)); field equation E = gamma^mu D_mu Psi - (m + lambda S) Psi = 0; T_{mu nu} of CONTRACT section 7; j^mu = Psibar gamma^mu Psi",
    "fields" -> "dirac16complex: Grassmann-odd components (second quantised, Krein space); dirac16complex00: commuting classical components",
    "expectationRule" -> "<Psi^dagger X Psi> = u^dagger B X u for a Hilbert-normalised one-particle mode u (NUMERICS_CONTRACT, Stage 4)",
    "statisticsSign" -> "sg = -1 (dirac16complex, anticommuting), sg = +1 (dirac16complex00, commuting)",
    "matrixEntryFormat" -> "matrix and vector entries are [re, im] pairs of exact rational strings",
    "inputFormDictionary" -> "strings copied from Wolfram InputForm use: Mz = M (constant effective mass of the k = 0 box), LL = L (tip cutoff), a4c = a_4, H = H, Y = e^{HL}, E^x = e^x"|>;
  res = Catch[
    step["algebra", checkAlgebra[fixFile]];
    step["T1 generic symbols", checkT1Generic[]];
    step["T1 jets (G1) and Grassmann", checkT1Jets[]];
    step["T1 Krein-Fock model", checkT1Krein[]];
    step["T2 frame reflections (G1)", checkT2Frame[]];
    step["T2 Z2 coordinate action", checkT2Z2[]];
    step["T1 in the Stage-2 primordial field", checkT1Primordial[]];
    step["T3 block maps", checkT3Block[ksFile]];
    step["T3 KS functional", checkT3KS[]];
    step["T3 spectra and control", checkT3Spectra[]];
    step["T3 EMT", checkT3EMT[]];
    step["statistics", checkStatistics[]];
    step["pair totals", checkTotals[]];
    step["theory export", buildTheory[]];
    "ok", d16pairErr];
  If[res =!= "ok", Print["INTERNAL ERROR: ", res]; addCheck["PAIR_internal_noException", False], addCheck["PAIR_internal_noException", True]];
  logT["done in ", Round[AbsoluteTime[] - t0], " s"];
  <|"checks" -> $checks, "measurements" -> $meas, "theory" -> $theory|>];

End[];
EndPackage[];
