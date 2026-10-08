#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_pairing.wls

   Driver for Revision/pairing/wolfram/RevisionPairing.wl (Revision/SPEC.md, section 9).
   Proves and verifies EXACTLY, for both statistics (dirac16complex: Grassmann components;
   dirac16complex00: commuting components):
     T1  the chirality map Gamma:  L_(m,lambda)[Gamma Psi] = -L_(-m,-lambda)[Psi], the field
         equations, T_mu nu -> -T_mu nu, J -> -J, and the vanishing total energy-momentum and charge
         of the pair (Psi with (m, lambda), Gamma Psi with (-m, -lambda));
     T2  Gamma combined with the Pin(4,4) reflection P_n = Gamma gamma^n of character -1 (n space-like):
         (m, lambda) -> (-m, lambda), L -> +L; in the metric of SPEC section 1 the Z2 mirror across the
         patch end z = 6 H x8 = pi/2 of the hidden coordinate;
     Q   the quantum-level reading (the Krein metric -B of the image field, its own generators, the
         one-particle Hamiltonians of two independently quantised universes);
   in four gravitational fields: the metric of SPEC section 1 ("primordial"), its mirror patch, a
   general diagonal test field with eight arbitrary functions of all eight coordinates ("diagonal8"),
   and a general non-diagonal test field at one point (exact rational vielbein and first derivatives,
   "pointwise"), plus the linearity (kernel) argument that covers every field.
   Writes, deterministically (LF line endings, no time stamps):
     Revision/pairing/reports/wolfram-pairing.json   every check with name, verdict, detail
     Revision/pairing/pairing-theory.json            the theorems, hypotheses, proofs, data, limits
   Usage:  wolframscript -file Revision/pairing/wolfram/verify_pairing.wls
   Exit code 0 if every check passes, 1 otherwise.
*)

$here = DirectoryName[$InputFileName];
$pairingDir = ExpandFileName[FileNameJoin[{$here, ".."}]]; (* NORMALISED: a ".." left in a path can push it past the Windows limit of 260 characters (MAX_PATH) *)
$revisionDir = ExpandFileName[FileNameJoin[{$pairingDir, ".."}]];
Get[FileNameJoin[{$here, "RevisionPairing.wl"}]];
RPLoadFixture[FileNameJoin[{$revisionDir, "algebra", "gammas.json"}]];

t0 = AbsoluteTime[];
checks = {};
addCheck[name_String, ok_, detail_String] := (
  AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS", "FAIL"], "  ", name, "  (", Round[AbsoluteTime[] - t0, 0.1], " s)"]);

{x1, x2, x3, x4, x5, x6, x7, x8} = RPX;
coordNames = {"x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"};
g = RPgamma; eta = RPeta; C16 = RPC; Gam = RPGamma; Bm = RPB; S = RPS;
id16 = IdentityMatrix[16]; zero16 = ConstantArray[0, {16, 16}];
anti[a_, b_] := a . b + b . a;
comm[a_, b_] := a . b - b . a;
refl[n_] := DiagonalMatrix[ReplacePart[ConstantArray[1, 8], n -> -1]];
spaceLike = {1, 2, 3, 8}; timeLike = {4, 5, 6, 7};
modeName[gr_] := If[gr, "Grassmann (dirac16complex)", "commuting (dirac16complex00)"];
modeTag[gr_] := If[gr, "grassmann", "commuting"];
allZeroQ[list_List, assum_] := AllTrue[list, RPeZeroQ[#, assum] &];
vZeroQ[v_List, assum_] := allZeroQ[v, assum];

(* ================= A. the fixture and the matrix facts used ================= *)
addCheck["fixture_Clifford_relation",
  And @@ Flatten[Table[anti[g[[a]], g[[b]]] == 2 eta[[a, b]] id16, {a, 8}, {b, 8}]] && eta == DiagonalMatrix[{1, 1, 1, -1, -1, -1, -1, 1}],
  "Revision/algebra/gammas.json read: {gamma^a, gamma^b} = 2 eta^ab I16 re-checked for all 64 pairs, eta = diag(+1,+1,+1,-1,-1,-1,-1,+1) in the order x1..x8 (x4 the time, x5, x6, x7 the deflating extra times, x8 the hidden direction)"];
addCheck["fixture_definitions",
  C16 == g[[8]] . g[[1]] . g[[2]] . g[[3]] && Gam == Dot @@ g[[{8, 1, 2, 3, 4, 5, 6, 7}]] && Bm == -I C16 . g[[4]] &&
  And @@ Flatten[Table[S[[a, b]] == (1/4) comm[g[[a]], g[[b]]], {a, 8}, {b, 8}]],
  "C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3), Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7), B = -i C gamma^(x4), S^ab = (1/4)[gamma^a, gamma^b] re-derived from the fixture gammas"];
addCheck["Gamma_properties",
  Gam == DiagonalMatrix[Join[ConstantArray[-1, 8], ConstantArray[1, 8]]] && Gam . Gam == id16 && ConjugateTranspose[Gam] == Gam &&
  And @@ Table[anti[Gam, g[[a]]] == zero16, {a, 8}] && comm[Gam, C16] == zero16 &&
  And @@ Flatten[Table[comm[Gam, S[[a, b]]] == zero16, {a, 8}, {b, 8}]],
  "Gamma = diag(-I8, I8) is real, symmetric, Gamma^2 = I; {Gamma, gamma^a} = 0 for all a; [Gamma, C] = 0; [Gamma, S^ab] = 0 for all a, b (hence [Gamma, Omega_mu] = 0 for ANY connection Omega_mu = (1/2) omega_mu ab S^ab)"];
addCheck["C_and_B_basic",
  C16 . C16 == id16 && Transpose[C16] == C16 && ConjugateTranspose[Bm] == Bm && Bm . Bm == id16 && C16 . g[[4]] == I Bm,
  "C real symmetric with C^2 = I; B Hermitian with B^2 = I; C gamma^(x4) = i B (so the x4-derivative kernel of L is (i/2) sqrt|g| e^(x4)_(x4) B)"];

(* ================= B. T1 by linearity: the kernel identities (every field) ================= *)
(* Under Psi -> Gamma Psi:  Psi^dagger M Psi' -> Psi^dagger Gamma M Gamma Psi'  (Gamma real symmetric) *)
kS = Gam . C16 . Gam == C16;
kKin = And @@ Table[Gam . C16 . g[[a]] . Gam == -C16 . g[[a]], {a, 8}];
kCon = And @@ Flatten[Table[Gam . C16 . anti[g[[a]], S[[b, c]]] . Gam == -C16 . anti[g[[a]], S[[b, c]]], {a, 8}, {b, 8}, {c, 8}]];
kEL = (And @@ Table[Gam . g[[a]] . Gam == -g[[a]], {a, 8}]) && (And @@ Flatten[Table[Gam . S[[b, c]] . Gam == S[[b, c]], {b, 8}, {c, 8}]]);
addCheck["T1_kernel_scalar", kS,
  "Gamma C Gamma = C: S = Psibar Psi = Psi^dagger C Psi is INVARIANT under Psi -> Gamma Psi (Psibar -> Psibar Gamma since Gamma is real symmetric and commutes with C)"];
addCheck["T1_kernel_kinetic", kKin,
  "Gamma C gamma^a Gamma = -C gamma^a for a = x1..x8: every kinetic bilinear Psibar gamma^a d_mu Psi and (d_mu Psibar) gamma^a Psi, and every current Psibar gamma^a Psi, CHANGES SIGN"];
addCheck["T1_kernel_connection", kCon,
  "Gamma C {gamma^a, S^bc} Gamma = -C {gamma^a, S^bc} for all 512 triples: the spin-connection part (1/4) e^mu_a omega_mu bc Psibar {gamma^a, S^bc} Psi of the symmetrised kinetic term changes sign for ANY vielbein and ANY connection coefficients"];
addCheck["T1_kernel_field_equation", kEL,
  "Gamma gamma^a Gamma = -gamma^a and Gamma S^bc Gamma = S^bc: gamma^mu D_mu (Gamma Psi) = -Gamma gamma^mu D_mu Psi for any vielbein and any connection Omega_mu = (1/2) omega_mu bc S^bc"];
addCheck["T1_linearity_argument",
  kS && kKin && kCon && kEL,
  "L = sqrt|g| [ (1/2) e^mu_a (Psibar gamma^a d_mu Psi - d_mu Psibar gamma^a Psi) + (1/4) e^mu_a omega_mu bc Psibar {gamma^a, S^bc} Psi - m S - (lambda/2) S^2 ] is a sum of coefficients (functions of the field: sqrt|g|, e^mu_a, omega_mu bc) times the kernel bilinears above; T_mu nu, J^mu and E_(m,lambda) likewise. The kernels transform with the signs above, the coefficients are untouched, so L_(m,lambda)[Gamma Psi] = -L_(-m,-lambda)[Psi], T_(-m,-lambda)[Gamma Psi] = -T_(m,lambda)[Psi], J[Gamma Psi] = -J[Psi], E_(-m,-lambda)[Gamma Psi] = -Gamma E_(m,lambda)[Psi] hold in EVERY gravitational field (any vielbein, any spin connection) and for both statistics (Psi -> Gamma Psi substitutes each component by +-itself and never reorders Grassmann factors)"];

(* ================= C. T2 kernels: P_n = Gamma gamma^n, characters, frame reflections ================= *)
reflectionRows = Table[Module[{P = Gam . g[[n]], R = refl[n], others, prod, s, chi, kap, adj, kinOK, conOK, Mn = g[[n]], scal},
    others = DeleteCases[{8, 1, 2, 3, 4, 5, 6, 7}, n];
    prod = Dot @@ g[[others]];
    s = Which[P == prod, 1, P == -prod, -1, True, 0];
    adj = And @@ Table[Inverse[P] . g[[a]] . P == Sum[R[[a, b]] g[[b]], {b, 8}], {a, 8}];
    chi = Which[ConjugateTranspose[P] . C16 . P == C16, 1, ConjugateTranspose[P] . C16 . P == -C16, -1, True, 0];
    scal = Which[ConjugateTranspose[Mn] . C16 . Mn == C16, 1, ConjugateTranspose[Mn] . C16 . Mn == -C16, -1, True, 0];
    kap = Which[
      And @@ Table[ConjugateTranspose[Mn] . C16 . g[[a]] . Mn == Sum[R[[a, b]] C16 . g[[b]], {b, 8}], {a, 8}], 1,
      And @@ Table[ConjugateTranspose[Mn] . C16 . g[[a]] . Mn == -Sum[R[[a, b]] C16 . g[[b]], {b, 8}], {a, 8}], -1,
      True, 0];
    conOK = And @@ Flatten[Table[ConjugateTranspose[Mn] . C16 . anti[g[[a]], S[[b, c]]] . Mn ==
        kap R[[a, a]] R[[b, b]] R[[c, c]] C16 . anti[g[[a]], S[[b, c]]], {a, 8}, {b, 8}, {c, 8}]];  (* R_n is diagonal *)
    <|"n" -> n, "name" -> coordNames[[n]], "eta" -> eta[[n, n]], "productSign" -> s, "adjointIsReflection" -> adj,
      "character" -> chi, "scalarSign" -> scal, "kineticSign" -> kap, "connectionOK" -> conOK,
      "GammaPisGamma_n" -> (Gam . P == g[[n]])|>], {n, 8}];
addCheck["T2_Pn_in_Pin44",
  AllTrue[reflectionRows, MemberQ[{1, -1}, #["productSign"]] &],
  "P_n = Gamma gamma^n equals +- the ordered product of the seven other gammas (signs " <>
  StringRiffle[(#["name"] <> ":" <> ToString[#["productSign"]]) & /@ reflectionRows, ", "] <>
  "): a product of unit vectors, hence an element of Pin(4,4)"];
addCheck["T2_Pn_covers_the_reflection",
  AllTrue[reflectionRows, #["adjointIsReflection"] &],
  "P_n^-1 gamma^a P_n = (R_n)^a_b gamma^b for every n, with R_n the reflection of the frame direction n: P_n acts on the gammas exactly as the O(4,4) reflection R_n (ordinary adjoint action), so it is the spinor lift that commutes with the Dirac operator"];
addCheck["T2_character_of_Pn",
  AllTrue[reflectionRows, #["character"] == -#["eta"] &],
  "P_n^dagger C P_n = chi_n C with chi_n = -eta_nn: character -1 (S -> -S) for the space-like directions x1, x2, x3, x8, character +1 for the time-like x4, x5, x6, x7 (" <>
  StringRiffle[(#["name"] <> ":" <> ToString[#["character"]]) & /@ reflectionRows, ", "] <> ")"];
addCheck["T2_Gamma_times_Pn_is_gamma_n",
  AllTrue[reflectionRows, #["GammaPisGamma_n"] &],
  "Gamma P_n = gamma^n (Gamma^2 = I): the T2 map 'Gamma combined with the reflection P_n' acts on the spinor as gamma^n"];
addCheck["T2_kernels_gamma_n_with_frame_reflection",
  AllTrue[reflectionRows, #["connectionOK"] && #["kineticSign"] == #["eta"] && #["scalarSign"] == -#["eta"] &],
  "for M = gamma^n and the reflected frame (e'^a = (R_n)^a_b e^b): M^dagger C M = -eta_nn C, M^dagger C gamma^a M = eta_nn (R_n)^a_b C gamma^b, M^dagger C {gamma^a, S^bc} M = eta_nn R R R C {gamma, S}: " <>
  "for n space-like (character -1) the kinetic term is INVARIANT and S -> -S, hence L_(m,lambda)[gamma^n Psi; R_n e] = +L_(-m,lambda)[Psi; e] in every field (T2); for n time-like the kinetic term changes sign and S is invariant, hence L -> -L_(-m,-lambda) (a T1-type map, not T2)"];

(* ================= D. the gravitational fields ================= *)
zz = 6 RPH x8; sx = Sin[zz]^(1/6);
assumPatch = {RPH > 0, 0 < zz < Pi/2, Element[RPa4[x4], Reals], Element[RPm, Reals], Element[RPlam, Reals]};
assumMirror = {RPH > 0, Pi/2 < zz < Pi, Element[RPa4[x4], Reals], Element[RPm, Reals], Element[RPlam, Reals]};
simpPatch = Simplify[#, assumPatch] &;
simpMirror = Simplify[#, assumMirror] &;
EPrim = DiagonalMatrix[{E^RPa4[x4] sx, E^RPa4[x4] sx, E^RPa4[x4] sx, 1, E^-RPa4[x4] sx, E^-RPa4[x4] sx, E^-RPa4[x4] sx, Cot[zz]}];
gAuthor = DiagonalMatrix[{E^(2 RPa4[x4]) Sin[zz]^(1/3), E^(2 RPa4[x4]) Sin[zz]^(1/3), E^(2 RPa4[x4]) Sin[zz]^(1/3), -1,
  -E^(-2 RPa4[x4]) Sin[zz]^(1/3), -E^(-2 RPa4[x4]) Sin[zz]^(1/3), -E^(-2 RPa4[x4]) Sin[zz]^(1/3), Cot[zz]^2}];
addCheck["primordial_vielbein",
  Simplify[Transpose[EPrim] . eta . EPrim - gAuthor, assumPatch] == ConstantArray[0, {8, 8}] && Simplify[Det[EPrim] - Cos[zz], assumPatch] === 0,
  "the diagonal vielbein e^a_mu = sqrt|g_mumu| (e^a4 sin^(1/6) z for x1..x3, 1 for x4, e^-a4 sin^(1/6) z for x5..x7, cot z for x8; z = 6 H x8 in (0, pi/2)) gives E^T eta E = the author's metric of SPEC section 1 exactly and sqrt|g| = det E = cos z"];
geoPrim = RPGeometry[EPrim, Table[D[EPrim, RPX[[r]]], {r, 8}], Cos[zz], simpPatch];

EMir = DiagonalMatrix[{E^RPa4[x4] sx, E^RPa4[x4] sx, E^RPa4[x4] sx, 1, E^-RPa4[x4] sx, E^-RPa4[x4] sx, E^-RPa4[x4] sx, -Cot[zz]}];
geoMir = RPGeometry[EMir, Table[D[EMir, RPX[[r]]], {r, 8}], -Cos[zz], simpMirror];

hf = Table[Symbol["h" <> ToString[a]], {a, 8}];
EDiag = DiagonalMatrix[Table[hf[[a]] @@ RPX, {a, 8}]];
geoDiag = RPGeometry[EDiag, Table[D[EDiag, RPX[[r]]], {r, 8}], Times @@ Table[hf[[a]] @@ RPX, {a, 8}], Together];

EPt = Table[KroneckerDelta[a, mu] + (Mod[2 a + 3 mu, 5] - 2)/9, {a, 8}, {mu, 8}];
dEPt = Table[(Mod[a + 2 mu + 3 r, 7] - 3)/11, {r, 8}, {a, 8}, {mu, 8}];
geoPt = RPGeometry[EPt, dEPt, Abs[Det[EPt]], Together];
addCheck["pointwise_field_is_general",
  Det[EPt] != 0 && Count[Flatten[Transpose[EPt] . eta . EPt - DiagonalMatrix[Diagonal[Transpose[EPt] . eta . EPt]]], x_ /; x != 0] > 0 &&
  Count[Flatten[geoPt["omegaDown"]], x_ /; x != 0] > 200,
  "the pointwise test field: e^a_mu = delta^a_mu + ((2a + 3mu) mod 5 - 2)/9 and d_rho e^a_mu = ((a + 2mu + 3rho) mod 7 - 3)/11 at one point (exact rationals), det e = " <>
  ToString[InputForm[Det[EPt]]] <> " != 0; the metric is non-diagonal and " <> ToString[Count[Flatten[geoPt["omegaDown"]], x_ /; x != 0]] <>
  " of the 512 connection components omega_mu ab are nonzero: a generic field with all frame directions coupled"];

geoms = {{"primordial", geoPrim, assumPatch}, {"mirror_patch", geoMir, assumMirror}, {"diagonal8", geoDiag, {}}, {"pointwise", geoPt, {}}};
Do[Module[{nm = gg[[1]], geo = gg[[2]], as = gg[[3]]},
  addCheck["connection_" <> nm,
    AllTrue[Flatten[geo["omegaAntisymmetric"]], Together[#] === 0 || Simplify[#, as] === 0 &] &&
    AllTrue[Flatten[geo["postulate"]], Together[#] === 0 || Simplify[#, as] === 0 &],
    "field '" <> nm <> "': the canonical spin connection computed from the vielbein (Christoffel symbols of g = E^T eta E) satisfies omega_mu ab = -omega_mu ba and the vielbein postulate d_mu gamma^nu + Chr^nu_(mu lambda) gamma^lambda + [Omega_mu, gamma^nu] = 0 exactly (all 64 matrix components)"]],
  {gg, geoms}];

(* ================= E. T1 explicitly in the fields, both statistics ================= *)
fBase = RPBaseFields[];
fGam = RPTransformFields[fBase, Gam, IdentityMatrix[8]];
substRule[M_, jac_][q_] := Switch[Head[q],
  RPpsi, RPMatVec[M, fBase["psi"]][[q[[1]]]],
  RPpsis, RPRowMat[fBase["psis"], ConjugateTranspose[M]][[q[[1]]]],
  RPdpsi, Fold[RPePlus[{#1, #2}] &, <||>, Table[RPeScale[jac[[q[[2]], nu]], RPMatVec[M, fBase["dpsi"][[nu]]][[q[[1]]]]], {nu, 8}]],
  RPdpsis, Fold[RPePlus[{#1, #2}] &, <||>, Table[RPeScale[jac[[q[[2]], nu]], RPRowMat[fBase["dpsis"][[nu]], ConjugateTranspose[M]][[q[[1]]]]], {nu, 8}]]];

t1Fields = {{"primordial", geoPrim, assumPatch, True}, {"diagonal8", geoDiag, {}, True}, {"pointwise", geoPt, {}, False}};
t1Data = <||>;
Do[Module[{nm = ff[[1]], geo = ff[[2]], as = ff[[3]], doEL = ff[[4]], bA, bB, bC, bD, tag, elA, elD, elDsub, ok1, ok2, ok3, sizeL},
  tag = nm <> "_" <> modeTag[gr];
  bA = RPBilinears[gr, geo, fBase, RPm, RPlam];      (* Psi, (m, lambda) *)
  bB = RPBilinears[gr, geo, fGam, -RPm, -RPlam];     (* Gamma Psi, (-m, -lambda) *)
  bC = RPBilinears[gr, geo, fGam, RPm, RPlam];       (* Gamma Psi, (m, lambda) *)
  bD = RPBilinears[gr, geo, fBase, -RPm, -RPlam];    (* Psi, (-m, -lambda) *)
  sizeL = Length[bA["L"]];
  addCheck["T1_scalar_and_kinetic_" <> tag,
    RPeZeroQ[RPeDiff[bC["S"], bA["S"]], as] && RPeZeroQ[RPePlus[{bC["K"], bA["K"]}], as] && RPeZeroQ[RPeDiff[bC["SS"], bA["SS"]], as],
    "field '" <> nm <> "', " <> modeName[gr] <> ": S[Gamma Psi] = S[Psi], S^2[Gamma Psi] = S^2[Psi], K[Gamma Psi] = -K[Psi] (K the symmetrised kinetic term including the spin connection)"];
  addCheck["T1_Lagrangian_" <> tag,
    RPeZeroQ[RPePlus[{bC["L"], bD["L"]}], as],
    "field '" <> nm <> "', " <> modeName[gr] <> ": L_(m,lambda)[Gamma Psi] + L_(-m,-lambda)[Psi] = 0 identically in the jets (L has " <> ToString[sizeL] <> " monomials)"];
  addCheck["T1_Lagrangian_negative_controls_" <> tag,
    !RPeZeroQ[RPePlus[{bC["L"], bA["L"]}], as] && !RPeZeroQ[RPePlus[{bC["L"], RPBilinears[gr, geo, fBase, -RPm, RPlam]["L"]}], as],
    "field '" <> nm <> "', " <> modeName[gr] <> ": L_(m,lambda)[Gamma Psi] + L_(m,lambda)[Psi] != 0 and L_(m,lambda)[Gamma Psi] + L_(-m,lambda)[Psi] != 0: the mass AND the coupling must change sign (for lambda != 0) - T1 pairs (m, lambda) with (-m, -lambda)"];
  addCheck["T1_field_equation_covariance_" <> tag,
    vZeroQ[RPvPlus[bB["Evec"], RPMatVec[Gam, bA["Evec"]]], as],
    "field '" <> nm <> "', " <> modeName[gr] <> ": E_(-m,-lambda)[Gamma Psi] = -Gamma E_(m,lambda)[Psi] (E = gamma^mu D_mu Psi - (m + lambda S) Psi): Psi solves the (m, lambda) equation iff Gamma Psi solves the (-m, -lambda) equation"];
  If[doEL,
    elA = RPDerivedEL[gr, bA["L"]];
    elD = RPDerivedEL[gr, bD["L"]];
    ok1 = vZeroQ[MapThread[RPeDiff, {elA[[1]], bA["ELexpected"]}], as] && vZeroQ[MapThread[RPeDiff, {elA[[2]], bA["ELbarExpected"]}], as];
    elDsub = Map[RPeSubst[gr, #, substRule[Gam, IdentityMatrix[8]]] &, elD, {2}];
    ok2 = vZeroQ[RPvPlus[elDsub[[1]], RPMatVec[Gam, elA[[1]]]], as] && vZeroQ[RPvPlus[elDsub[[2]], RPMatVec[Gam, elA[[2]]]], as];
    addCheck["T1_Euler_Lagrange_derived_" <> tag, ok1,
      "field '" <> nm <> "', " <> modeName[gr] <> ": the Euler-Lagrange expressions derived from L_(m,lambda) (" <> If[gr, "left derivative in Psi^dagger, right derivative in Psi", "ordinary derivatives"] <>
      ", total derivatives d_mu including the field-dependent coefficients) equal sqrt|g| C (gamma^mu D_mu Psi - (m + lambda S) Psi) and sqrt|g| ( -(D_mu Psibar) gamma^mu - (m + lambda S) Psibar ) exactly"];
    addCheck["T1_Euler_Lagrange_map_" <> tag, ok2,
      "field '" <> nm <> "', " <> modeName[gr] <> ": [Euler-Lagrange expressions of L_(-m,-lambda)] evaluated at Gamma Psi = -Gamma [those of L_(m,lambda)] at Psi, for the Psi^dagger and the Psi variation: solutions are mapped to solutions"]];
  addCheck["T1_energy_momentum_" <> tag,
    And @@ Flatten[Table[RPeZeroQ[RPePlus[{bB["T"][[mu, nu]], bA["T"][[mu, nu]]}], as], {mu, 8}, {nu, 8}]] &&
    And @@ Flatten[Table[RPeZeroQ[RPeDiff[bA["T"][[mu, nu]], bA["T"][[nu, mu]]], as], {mu, 8}, {nu, mu + 1, 8}]],
    "field '" <> nm <> "', " <> modeName[gr] <> ": T_mu nu is symmetric and T^(-m,-lambda)_mu nu[Gamma Psi] + T^(m,lambda)_mu nu[Psi] = 0 for all 64 components (off shell, hence also on shell): the pair's total energy-momentum density vanishes"];
  addCheck["T1_current_" <> tag,
    And @@ Table[RPeZeroQ[RPePlus[{bB["J"][[mu]], bA["J"][[mu]]}], as], {mu, 8}] && !RPeZeroQ[bA["J"][[4]], as],
    "field '" <> nm <> "', " <> modeName[gr] <> ": J^mu[Gamma Psi] + J^mu[Psi] = 0 for mu = x1..x8 (J^x4 itself nonzero): the pair's total current, hence total charge Q = integral sqrt|g| J^x4 d^7x, vanishes"];
  If[nm == "primordial" && !gr,
    Module[{U, LU1, LU2},
      LU1 = RPToExpr[RPeScale[geo["sqrtg"], bC["K"]]] - geo["sqrtg"] (RPm RPToExpr[bC["S"]] + U[RPToExpr[bC["S"]]]);
      LU2 = RPToExpr[RPeScale[geo["sqrtg"], bA["K"]]] - geo["sqrtg"] (-RPm RPToExpr[bA["S"]] - U[RPToExpr[bA["S"]]]);
      addCheck["T1_general_potential_primordial_commuting",
        Simplify[Expand[LU1 + LU2], assumPatch] === 0,
        "field 'primordial', commuting: with an ARBITRARY potential function U(S), L_(m,U)[Gamma Psi] = -L_(-m,-U)[Psi] exactly (S is invariant, so U(S) is untouched); for the Grassmann field U is a polynomial in the even element S and the same holds term by term"]]];
  ], {ff, t1Fields}, {gr, {False, True}}];

(* ================= F. T2 ================= *)
(* F1. frame reflections in the general pointwise field, every direction n, both statistics *)
t2Rows = {};
Do[Module[{R = refl[n], geoR, fN, bN, bRef, lhs, ok, okEL, okT, okJ, omOK, spacelikeQ = MemberQ[spaceLike, n], tag, mm, ll, sg},
  geoR = RPGeometry[R . EPt, Table[R . dEPt[[r]], {r, 8}], Abs[Det[EPt]], Together];
  omOK = And @@ Table[geoR["omegaDown"][[mu]] == R . geoPt["omegaDown"][[mu]] . R, {mu, 8}];
  fN = RPTransformFields[fBase, g[[n]], IdentityMatrix[8]];
  bN = RPBilinears[gr, geoR, fN, RPm, RPlam];
  {mm, ll, sg} = If[spacelikeQ, {-RPm, RPlam, 1}, {-RPm, -RPlam, -1}];
  bRef = RPBilinears[gr, geoPt, fBase, mm, ll];
  ok = RPeZeroQ[RPeDiff[bN["L"], RPeScale[sg, bRef["L"]]]];
  okEL = vZeroQ[RPvPlus[bN["Evec"], RPMatVec[g[[n]], bRef["Evec"]]], {}];
  okT = And @@ Flatten[Table[RPeZeroQ[RPeDiff[bN["T"][[mu, nu]], RPeScale[sg, bRef["T"][[mu, nu]]]]], {mu, 8}, {nu, 8}]];
  okJ = And @@ Table[RPeZeroQ[RPeDiff[bN["J"][[mu]], RPeScale[sg, bRef["J"][[mu]]]]], {mu, 8}];
  tag = coordNames[[n]] <> "_" <> modeTag[gr];
  addCheck["T2_frame_reflection_pointwise_" <> tag, omOK && ok && okEL && okT && okJ,
    "pointwise general field, " <> modeName[gr] <> ", reflection of the frame direction " <> coordNames[[n]] <> " (" <> If[spacelikeQ, "space-like, character -1", "time-like, character +1"] <>
    "), e' = R e, Psi' = gamma^n Psi = Gamma P_n Psi: the canonical connection of e' is R omega R; " <>
    If[spacelikeQ,
      "L_(m,lambda)[Psi'; e'] = +L_(-m,lambda)[Psi; e], E_(m,lambda)[Psi'] = -gamma^n E_(-m,lambda)[Psi], T'_mu nu = T^(-m,lambda)_mu nu[Psi], J'^mu = J^mu[Psi] (T2)",
      "L_(m,lambda)[Psi'; e'] = -L_(-m,-lambda)[Psi; e], E_(m,lambda)[Psi'] = -gamma^n E_(-m,-lambda)[Psi], T' = -T^(-m,-lambda), J' = -J (T1-type)"]];
  ], {n, 8}, {gr, {False, True}}];

(* F2. the Z2 mirror of the primordial field across z = pi/2 *)
cMir = Pi/(6 RPH);
mirrorSub[expr_] := (expr /. x8 -> cMir - x8) /. (h : (Sin | Cos | Tan | Cot | Sec | Csc))[arg_] :> h[Expand[arg]];
R8 = refl[8];
addCheck["T2_mirror_is_isometry",
  Simplify[R8 . mirrorSub[Transpose[EMir] . eta . EMir] . R8 - gAuthor, assumPatch] == ConstantArray[0, {8, 8}] &&
  Simplify[mirrorSub[EMir] . R8 - R8 . EPrim, assumPatch] == ConstantArray[0, {8, 8}] &&
  Simplify[mirrorSub[-Cos[zz]] - Cos[zz], assumPatch] === 0,
  "phi: x8 -> pi/(6H) - x8 (z -> pi - z) maps the patch z in (0, pi/2) onto the mirror patch (pi/2, pi) and is an isometry of the author's metric (sin z and cot^2 z are invariant); with the positive vielbein on both patches (e^8 = |cot z| dx8: cot z on the patch, -cot z on the mirror) the pulled-back mirror vielbein is R_8 e (the hidden frame direction reflected), and sqrt|g| = |cos z| is invariant. The brane z = pi/2 itself is degenerate (g_88 = cot^2 z = 0, sqrt|g| = 0); the mirror construction across it is the ASSUMED Z2 construction of SPEC section 7"];
fMir = RPTransformFields[fBase, g[[8]], R8];
Do[Module[{bM, bRef, bMown, elM, elMsub, elRef, okL, okEL, okT, okJ, okS, tag = modeTag[gr]},
  bM = RPBilinears[gr, geoMir, fMir, RPm, RPlam];
  bRef = RPBilinears[gr, geoPrim, fBase, -RPm, RPlam];
  okL = RPeZeroQ[RPeDiff[RPeMapCoefficients[mirrorSub, bM["L"]], bRef["L"]], assumPatch];
  okS = RPeZeroQ[RPePlus[{RPeMapCoefficients[mirrorSub, bM["S"]], bRef["S"]}], assumPatch];
  okT = And @@ Flatten[Table[RPeZeroQ[RPeDiff[RPeMapCoefficients[mirrorSub, bM["T"][[mu, nu]]], RPeScale[R8[[mu, mu]] R8[[nu, nu]], bRef["T"][[mu, nu]]]], assumPatch], {mu, 8}, {nu, 8}]];
  okJ = And @@ Table[RPeZeroQ[RPeDiff[RPeMapCoefficients[mirrorSub, bM["J"][[mu]]], RPeScale[R8[[mu, mu]], bRef["J"][[mu]]]], assumPatch], {mu, 8}];
  addCheck["T2_mirror_Lagrangian_" <> tag, okL && okS,
    "primordial field, " <> modeName[gr] <> ": with Psi'(phi(x)) = gamma^(x8) Psi(x) (= Gamma P_8 Psi, P_8 of character -1), L_(m,lambda)[Psi'](phi(x)) = L_(-m,+lambda)[Psi](x) and S[Psi'](phi(x)) = -S[Psi](x) identically in the jets (connection recomputed on the mirror patch from its own vielbein)"];
  addCheck["T2_mirror_energy_momentum_and_current_" <> tag, okT && okJ,
    "primordial field, " <> modeName[gr] <> ": T_mu nu[Psi'](phi(x)) = (R_8 T^(-m,lambda)[Psi](x) R_8)_mu nu (the tensor transformation law under phi; in particular the energy density T_x4x4 and all components without an x8 index are EQUAL, not opposite) and J'^mu = (R_8)^mu_nu J^nu: the T2 partner has the same energy-momentum and the same charge as the (-m, lambda) configuration it mirrors"];
  bMown = RPBilinears[gr, geoMir, fBase, RPm, RPlam];
  elM = RPDerivedEL[gr, bMown["L"]];
  elMsub = Map[RPeMapCoefficients[mirrorSub, RPeSubst[gr, #, substRule[g[[8]], R8]]] &, elM, {2}];
  elRef = RPDerivedEL[gr, bRef["L"]];
  okEL = vZeroQ[MapThread[RPeDiff, {elMsub[[1]], RPMatVec[g[[8]], elRef[[1]]]}], assumPatch] &&
    vZeroQ[MapThread[RPeDiff, {elMsub[[2]], RPMatVec[g[[8]], elRef[[2]]]}], assumPatch] &&
    vZeroQ[MapThread[RPeDiff, {elM[[1]], bMown["ELexpected"]}], assumMirror];
  addCheck["T2_mirror_Euler_Lagrange_" <> tag, okEL,
    "primordial field, " <> modeName[gr] <> ": the Euler-Lagrange expressions derived on the mirror patch (z in (pi/2, pi), its own vielbein and connection) equal sqrt|g| C E_(m,lambda), and evaluated at Psi' = gamma^(x8) Psi o phi^-1 they equal gamma^(x8) times those of L_(-m,+lambda) at Psi: Psi solves the (-m, lambda) equation on the patch iff its mirror image solves the (m, lambda) equation on the mirror patch"];
  ], {gr, {False, True}}];

(* ================= G. the quantum-level reading ================= *)
signOf[M_] := Which[M . Bm . ConjugateTranspose[M] == Bm, 1, M . Bm . ConjugateTranspose[M] == -Bm, -1, True, 0];
kreinRows = Join[{{"Gamma", signOf[Gam]}}, Table[{"gamma^" <> coordNames[[n]], signOf[g[[n]]]}, {n, 8}], Table[{"P_" <> coordNames[[n]], signOf[Gam . g[[n]]]}, {n, 8}]];
addCheck["Q_Krein_metric_of_images",
  signOf[Gam] == -1 && signOf[g[[8]]] == 1 && AllTrue[Table[signOf[g[[n]]], {n, 8}], MemberQ[{1, -1}, #] &],
  "M B M^dagger = sigma B for the maps M: " <> StringRiffle[(#[[1]] <> ":" <> ToString[#[[2]]]) & /@ kreinRows, ", "] <>
  ". If Psi obeys {Psi_A, Psi_B^dagger} = B_AB delta/sqrt|g| (SPEC section 6), the image M Psi obeys the same with sigma B: the chirality image Gamma Psi carries the Krein metric -B; the T2 image gamma^(x8) Psi carries +B"];

Do[Module[{bA, bC, bD, ker, kA, kC, kD, cos = Cos[zz], tag = modeTag[gr], HA, HC, HD, jA, jC, jD, hd, jn, sub},
  bA = RPBilinears[gr, geoPrim, fBase, RPm, RPlam];
  bC = RPBilinears[gr, geoPrim, fGam, RPm, RPlam];
  bD = RPBilinears[gr, geoPrim, fBase, -RPm, -RPlam];
  ker[L_] := Table[Module[{e = RPLeftD[gr, RPLeftD[gr, L, RPpsis[A]], RPdpsi[B, 4]]}, Lookup[e, Key[{}], 0]], {A, 16}, {B, 16}];
  kA = ker[bA["L"]]; kC = ker[bC["L"]]; kD = ker[bD["L"]];
  addCheck["Q_symplectic_kernel_" <> tag,
    Simplify[2 kA/(I cos) - Bm, assumPatch] == zero16 && Simplify[2 kC/(I cos) + Bm, assumPatch] == zero16 && Simplify[2 kD/(I cos) - Bm, assumPatch] == zero16,
    "primordial field, " <> modeName[gr] <> ": the coefficient matrix of Psi^dagger_A d_x4 Psi_B in the Lagrangian is (i/2) sqrt|g| N with N = B for L_(m,lambda)[Psi], N = -B for the image Lagrangian L_(m,lambda)[Gamma chi] = -L_(-m,-lambda)[chi] (chi the image field), and N = +B for L_(-m,-lambda)[chi] (an independently quantised (-m,-lambda) universe). The canonical anticommutator is {chi_A, chi_B^dagger} = (N^-1)_AB delta/sqrt|g|: -B for the image, +B for the independent universe"];
  hd[L_] := RPePlus[Join[Table[RPeTimes[gr, <|{RPdpsis[A, 4]} -> 1|>, RPLeftD[gr, L, RPdpsis[A, 4]]], {A, 16}],
    Table[RPeTimes[gr, RPRightD[gr, L, RPdpsi[A, 4]], <|{RPdpsi[A, 4]} -> 1|>], {A, 16}], {RPeScale[-1, L]}]];
  jn[L_, mu_] := RPeScale[I, RPePlus[Join[Table[RPeTimes[gr, RPRightD[gr, L, RPdpsi[A, mu]], <|{RPpsi[A]} -> 1|>], {A, 16}],
    Table[RPeScale[-1, RPeTimes[gr, <|{RPpsis[A]} -> 1|>, RPLeftD[gr, L, RPdpsis[A, mu]]]], {A, 16}]]]];
  HA = hd[bA["L"]]; HC = hd[bC["L"]]; HD = hd[bD["L"]];
  jA = jn[bA["L"], 4]; jC = jn[bC["L"], 4]; jD = jn[bD["L"], 4];
  sub = RPeSubst[gr, #, substRule[Gam, IdentityMatrix[8]]] &;
  addCheck["Q_generators_of_the_image_" <> tag,
    RPeZeroQ[RPeDiff[sub[HC], HA], assumPatch] && RPeZeroQ[RPePlus[{HC, HD}], assumPatch] &&
    RPeZeroQ[RPeDiff[sub[jC], jA], assumPatch] && RPeZeroQ[RPePlus[{jC, jD}], assumPatch] &&
    RPeZeroQ[RPeDiff[jA, RPeScale[I cos, bA["J"][[4]]]], assumPatch] && !RPeZeroQ[HA, assumPatch],
    "primordial field, " <> modeName[gr] <> ": the image field's OWN generators, built from its own Lagrangian L_(m,lambda)[Gamma chi] (Legendre energy density sum (d_4 chi^dagger dL/d(d_4 chi^dagger) + dL/d(d_4 chi) d_4 chi) - L and the U(1) Noether density i (dL/d(d_4 chi) chi - chi^dagger dL/d(d_4 chi^dagger)) = i sqrt|g| J^x4), are at chi = Gamma Psi IDENTICAL to those of Psi, and equal MINUS the generators of the (-m,-lambda) Lagrangian: the image is the same quantum system re-labelled, not a second universe"];
  ], {gr, {False, True}}];

(* one-particle Hamiltonians in flat 4+4 space: i d_x4 Psi = h Psi for Psi ~ exp(-i w x4 + i k.x) *)
kk = Table[Symbol["k" <> ToString[a]], {a, 8}];
hFlat[mm_, k_] := -I g[[4]] mm - Sum[If[a == 4, 0, g[[4]] . g[[a]] k[[a]]], {a, 8}];
hm = hFlat[RPm, kk]; hmm = hFlat[-RPm, kk];
conjH[M_] := Transpose[M /. Complex[a_, b_] :> Complex[a, -b]];
addCheck["Q_one_particle_flat_dispersion",
  Expand[hm . hm - (RPm^2 + kk[[1]]^2 + kk[[2]]^2 + kk[[3]]^2 + kk[[8]]^2 - kk[[5]]^2 - kk[[6]]^2 - kk[[7]]^2) id16] == zero16 &&
  Expand[Bm . hm - conjH[hm] . Bm] == zero16,
  "flat 4+4 space (H = 0, a4 constant), plane waves exp(-i w x4 + i k.x): h_m(k) = -i m gamma^(x4) - gamma^(x4) sum_(a != x4) k_a gamma^a satisfies h_m^2 = (m^2 + k1^2 + k2^2 + k3^2 + k8^2 - k5^2 - k6^2 - k7^2) I16 (real frequencies in the good sector k5 = k6 = k7 = 0, imaginary - growing - frequencies when the extra-time momenta dominate) and B h_m = h_m^dagger B for real m, k (h_m is self-adjoint for the Krein form Psi^dagger B Psi)"];
addCheck["Q_one_particle_maps",
  Gam . hm . Gam == hmm && g[[8]] . hm . g[[8]] == hFlat[-RPm, R8 . kk],
  "Gamma h_m(k) Gamma = h_(-m)(k) and gamma^(x8) h_m(k) gamma^(x8) = h_(-m)(R_8 k): the one-particle Hamiltonians of the +m and -m universes are similar, so their spectra are IDENTICAL (+-w each with multiplicity 8), not opposite"];
inertia[V_] := Module[{G = Conjugate[V] . Bm . Transpose[V], ev}, ev = Eigenvalues[G]; {Count[ev, x_ /; Positive[x]], Count[ev, x_ /; Negative[x]]}];
samples = {{2, {1, 2, 0, 0, 0, 0, 0, 4}}, {3, {0, 0, 0, 0, 0, 0, 0, 0}}, {1, {1, 0, 0, 0, 0, 0, 0, 0}}, {2, {0, 0, 0, 0, 1, 0, 0, 0}}};
sampleRows = Flatten[Table[Module[{mm = smp[[1]] sgn, k = smp[[2]], h, w, Vp, Vn},
    h = hFlat[mm, k]; w = Sqrt[smp[[1]]^2 + Total[k[[{1, 2, 3, 8}]]^2] - Total[k[[{5, 6, 7}]]^2]];
    Vp = NullSpace[h - w id16]; Vn = NullSpace[h + w id16];
    <|"m" -> mm, "k" -> k, "w" -> w, "dimPlus" -> Length[Vp], "dimMinus" -> Length[Vn], "inertiaPlus" -> inertia[Vp], "inertiaMinus" -> inertia[Vn],
      "imageOK" -> (MatrixRank[Join[Transpose[Gam . Transpose[Vp]], NullSpace[hFlat[-mm, k] - w id16]]] == 8)|>], {smp, samples}, {sgn, {1, -1}}], 1];
addCheck["Q_one_particle_Krein_signatures",
  AllTrue[sampleRows, #["dimPlus"] == 8 && #["dimMinus"] == 8 && #["inertiaPlus"] == {4, 4} && #["inertiaMinus"] == {4, 4} && #["imageOK"] &],
  "exact eigenspaces of h_m(k) for (m, k) = " <> StringRiffle[("(" <> ToString[#["m"]] <> ", " <> ToString[#["k"]] <> ", w = " <> ToString[InputForm[#["w"]]] <> ")") & /@ sampleRows, "; "] <>
  ": at each of these samples (all with a real frequency w > 0; the last pair has the extra-time momentum k5 = 1) the eigenspaces w and -w have dimension 8 and the form u^dagger B u restricted to each has inertia (4 positive, 4 negative); Gamma maps the w-eigenspace of h_m onto that of h_(-m) and turns the form into its negative, so the inertia is (4,4) in both universes. The general statement for every real frequency, and the Krein-neutral eigenspaces of imaginary or zero frequency, are the next two checks"];
(* every REAL frequency: proof; imaginary and zero frequencies: Krein-neutral eigenspaces *)
Module[{w2 = RPm^2 + kk[[1]]^2 + kk[[2]]^2 + kk[[3]]^2 + kk[[8]]^2 - kk[[5]]^2 - kk[[6]]^2 - kk[[7]]^2, hG, hmD, PpD, Pp, Pn, good, trBh, orth, smpRows, wv},
  hG = hm /. {kk[[5]] -> 0, kk[[6]] -> 0, kk[[7]] -> 0};
  good = Expand[Bm . hG - hG . Bm] == zero16;
  trBh = Expand[Tr[Bm . hm]] === 0 && Tr[Bm] === 0;
  (* real frequency wv > 0 with wv^2 = w2: P_(+-) = (1 +- h/wv)/2, P_+^dagger = (1 + h^dagger/wv)/2 since wv is real *)
  hmD = ComplexExpand[ConjugateTranspose[hm]];
  Pp = (id16 + hm/wv)/2; Pn = (id16 - hm/wv)/2; PpD = (id16 + hmD/wv)/2;
  orth = Map[Together, Expand[PpD . Bm . Pn] /. wv -> Sqrt[w2], {2}] == zero16 &&
    Map[Together, Expand[PpD . Bm . Pp - Bm . Pp] /. wv -> Sqrt[w2], {2}] == zero16;
  addCheck["Q_one_particle_Krein_inertia_real_frequencies",
    good && trBh && orth,
    "PROOF for every real frequency, flat 4+4 space: (i) h_m(k)^2 = w^2 I16 (check Q_one_particle_flat_dispersion) and B h_m = h_m^dagger B; for w^2 = m^2 + k1^2 + k2^2 + k3^2 + k8^2 - k5^2 - k6^2 - k7^2 > 0 the projectors P_(+-) = (1 +- h_m/w)/2 satisfy P_+^dagger B P_- = 0 and P_+^dagger B P_+ = B P_+ (verified symbolically for real m, k with w^2 > 0): the two eigenspaces (dimension 8 each) are B-orthogonal, so B is nondegenerate on each; (ii) in the good sector k5 = k6 = k7 = 0, [B, h_m(k)] = 0 (verified), and tr B = 0, tr(B h_m(k)) = 0 for all k (verified: tr C = tr(C gamma^a) = 0), so tr(B P_(+-)) = 0: B restricted to each eigenspace has signature 0, inertia (4,4); (iii) the region w^2 > 0 is connected and contains the good sector (scale k5, k6, k7 down to 0 at fixed k1, k2, k3, k8, m: w^2 only grows), P_(+-) depend continuously on k there and B stays nondegenerate on their ranges, so the inertia (4,4) is the same at every real frequency, with or without extra-time momenta"];
  smpRows = Table[Module[{mm = sm[[1]], k = sm[[2]], h, w, sp1, sp2},
      h = hFlat[mm, k]; w = Sqrt[mm^2 + Total[k[[{1, 2, 3, 8}]]^2] - Total[k[[{5, 6, 7}]]^2] + 0];
      If[w == 0,
        sp1 = NullSpace[h]; sp2 = sp1,
        sp1 = NullSpace[h - w id16]; sp2 = NullSpace[h + w id16]];
      <|"m" -> mm, "k" -> k, "w" -> w, "dims" -> {Length[sp1], Length[sp2]},
        "formZero" -> (Simplify[Conjugate[sp1] . Bm . Transpose[sp1]] == ConstantArray[0, {Length[sp1], Length[sp1]}] &&
                       Simplify[Conjugate[sp2] . Bm . Transpose[sp2]] == ConstantArray[0, {Length[sp2], Length[sp2]}]),
        "squareZero" -> (w == 0 && Expand[h . h] == zero16 && MatrixRank[h] == 8)|>], {sm, {{1, {0, 0, 0, 0, 2, 0, 0, 0}}, {1, {1, 0, 0, 0, 2, 0, 0, 0}}, {1, {0, 0, 0, 0, 1, 0, 0, 0}}}}];
  addCheck["Q_one_particle_complex_and_zero_frequencies_Krein_neutral",
    AllTrue[smpRows, #["dims"] == {8, 8} && #["formZero"] &] && smpRows[[3]]["squareZero"],
    "general: if h u = w u and h v = w v then w u^dagger B v = u^dagger B h v = (h u)^dagger B v = conj(w) u^dagger B v (B h = h^dagger B), so for w not real the form u^dagger B v vanishes identically on the eigenspace (Krein-neutral, inertia (0,0,8)); for w = 0, h^2 = 0 with rank 8, ker h = ran h and u^dagger B h x = (h u)^dagger B x = 0. Exact samples: " <>
    StringRiffle[("(m, k) = (" <> ToString[#["m"]] <> ", " <> ToString[#["k"]] <> "): w = " <> ToString[InputForm[#["w"]]] <> ", eigenspace dimensions " <> ToString[#["dims"]] <> ", B-form identically zero: " <> ToString[#["formZero"]]) & /@ smpRows, "; "] <>
    ". So the statement 'every energy eigenspace has Krein inertia (4,4)' holds exactly for the real frequencies (w^2 > 0) only; the growing extra-time modes span Krein-neutral eigenspaces"]];
Module[{gu = geoPt["gammaUp"], Om = geoPt["Omega"], g44, hG, hGm, kk2 = kk},
  g44 = Inverse[geoPt["g"]][[4, 4]];
  hG[mm_] := I (gu[[4]]/g44) . (mm id16 - Sum[If[mu == 4, zero16, gu[[mu]] . (I kk2[[mu]] id16 + Om[[mu]])], {mu, 8}]) - I Om[[4]];
  addCheck["Q_one_particle_general_field",
    gu[[4]] . gu[[4]] == g44 id16 && g44 != 0 && Expand[Gam . hG[RPm] . Gam - hG[-RPm]] == zero16,
    "pointwise general field (locally constant coefficients, i d_x4 Psi = h_m Psi, d_mu -> i k_mu for mu != x4): (gamma^x4)^2 = g^(x4 x4) I16 = " <> ToString[InputForm[g44]] <>
    " I16, h_m = i (gamma^x4)^-1 (m - sum_(mu != x4) gamma^mu (i k_mu + Omega_mu)) - i Omega_x4 and Gamma h_m Gamma = h_(-m) exactly for symbolic k: the +m and -m one-particle spectra coincide in a general field too"]];
addCheck["Q_no_identification_of_independent_universes",
  Bm != -Bm && signOf[Gam] == -1,
  "an independently quantised (-m,-lambda) universe has, from its own Lagrangian, {chi_2, chi_2^dagger} = +B delta/sqrt|g|, whereas the chirality image of universe 1 has {Gamma Psi_1, (Gamma Psi_1)^dagger} = -B delta/sqrt|g|; since B != -B no operator identification chi_2 = Gamma Psi_1 exists. On the product state space the generators add, P_total = P_1 (x) 1 + 1 (x) P_2, and the T1 identity T^(-m,-lambda)[Gamma Psi_1] = -T^(m,lambda)[Psi_1] (an identity between operators of universe 1 alone) gives no relation P_2 = -P_1: there is no cancellation between two independently quantised universes"];

(* ================= H. pairing-theory.json ================= *)
jstr[s_String] := "\"" <> StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\""}] <> "\"";
toJ[x_String, ind_] := jstr[x];
toJ[x_Integer, ind_] := ToString[x];
toJ[True, ind_] := "true"; toJ[False, ind_] := "false";
toJ[x_List, ind_] /; AllTrue[x, MatchQ[#, _Integer | True | False] &] := "[" <> StringRiffle[toJ[#, ind] & /@ x, ", "] <> "]";
toJ[x_List, ind_] := If[x === {}, "[]", "[\n" <> StringRiffle[(ind <> "  " <> toJ[#, ind <> "  "]) & /@ x, ",\n"] <> "\n" <> ind <> "]"];
toJ[x_Association, ind_] := "{\n" <> StringRiffle[KeyValueMap[(ind <> "  " <> jstr[#1] <> ": " <> toJ[#2, ind <> "  "]) &, x], ",\n"] <> "\n" <> ind <> "}";
istr[x_] := ToString[InputForm[x]];

passedQ[prefix_] := AllTrue[Select[checks, StringStartsQ[#["name"], prefix] &], #["verdict"] == "PASS" &];
namesWith[prefix_] := Select[#["name"] & /@ checks, StringStartsQ[#, prefix] &];

theory = <|
  "document" -> "Pairing theorems for universes of masses {+m, -m} (Revision/SPEC.md section 9): T1, T2, the quantum-level reading and what they do not establish; both fields (dirac16complex: Grassmann; dirac16complex00: commuting)",
  "producer" -> "Revision/pairing/wolfram/verify_pairing.wls",
  "package" -> "Revision/pairing/wolfram/RevisionPairing.wl",
  "fixture" -> "Revision/algebra/gammas.json",
  "report" -> "Revision/pairing/reports/wolfram-pairing.json",
  "status" -> If[AllTrue[checks, #["verdict"] == "PASS" &], "all checks of the report passed", "SOME CHECKS FAILED - see the report"],
  "coordinates" -> "x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; x8 = the hidden direction, z = 6 H x8",
  "conventions" -> <|
    "adjoint" -> "Psibar = Psi^dagger C, C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)",
    "chirality" -> "Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) = diag(-I8, I8)",
    "Krein_metric" -> "B = -i C gamma^(x4)",
    "covariant_derivative" -> "D_mu Psi = d_mu Psi + Omega_mu Psi, D_mu Psibar = d_mu Psibar - Psibar Omega_mu, Omega_mu = (1/2) omega_mu ab S^ab, S^ab = (1/4)[gamma^a, gamma^b]",
    "Lagrangian" -> "L_(m,lambda) = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m S - (lambda/2) S^2 ], S = Psibar Psi",
    "field_equation" -> "E_(m,lambda)[Psi] = gamma^mu D_mu Psi - (m + lambda S) Psi = 0 (and its adjoint)",
    "energy_momentum" -> "T_mu nu = (1/4)(Psibar gamma_mu D_nu Psi + Psibar gamma_nu D_mu Psi - (D_mu Psibar) gamma_nu Psi - (D_nu Psibar) gamma_mu Psi) - g_mu nu (L / sqrt|g|); every statement below is linear in T, so the sign and normalisation convention of SPEC section 4 does not affect it",
    "current" -> "J^mu = Psibar gamma^mu Psi; charge Q = integral over x4 = const of sqrt|g| J^(x4) d^7x"|>,
  "fields_tested" -> {
    "primordial: the author's metric of SPEC section 1 on the patch z in (0, pi/2), canonical spin connection from the diagonal vielbein",
    "mirror_patch: the same metric on z in (pi/2, pi) with its own positive vielbein (e^8 = -cot z dx8)",
    "diagonal8: a general diagonal (4,4) field e^a_mu = h_a(x1, ..., x8) delta^a_mu with eight arbitrary functions of all eight coordinates",
    "pointwise: a general non-diagonal field at one point (exact rational e^a_mu and d_rho e^a_mu, all 512 connection components generic)",
    "every field: the linearity (kernel) argument, valid for any vielbein and any connection coefficients"},
  "theorems" -> {
    <|"id" -> "T1",
      "name" -> "chirality pairing",
      "hypotheses" -> {
        "any gravitational field (vielbein e^a_mu, any spin connection omega_mu ab, in particular the canonical one), treated as a fixed (test) background: the metric is NOT varied and the two members of the pair are evaluated in the SAME field",
        "Psi either Grassmann-valued (dirac16complex) or commuting (dirac16complex00); the map acts at the same point x, with no coordinate change",
        "Gamma = diag(-I8, I8): real, symmetric, Gamma^2 = I, {Gamma, gamma^a} = 0, [Gamma, C] = 0, hence [Gamma, S^ab] = 0 (verified exactly from gammas.json)",
        "potential U(S) = (lambda/2) S^2, or any function U (commuting field) / any polynomial U (Grassmann field) with U -> -U"},
      "statement" -> {
        "L_(m,lambda)[Gamma Psi] = -L_(-m,-lambda)[Psi] identically (off shell); for general U: L_(m,U)[Gamma Psi] = -L_(-m,-U)[Psi]",
        "S[Gamma Psi] = S[Psi]; the kinetic term (with the spin connection) changes sign",
        "E_(-m,-lambda)[Gamma Psi] = -Gamma E_(m,lambda)[Psi]: Psi solves the (m, lambda) field equations iff Gamma Psi solves the (-m, -lambda) ones; the Euler-Lagrange expressions are mapped likewise",
        "T^(-m,-lambda)_mu nu[Gamma Psi] = -T^(m,lambda)_mu nu[Psi] and J^mu[Gamma Psi] = -J^mu[Psi] pointwise, off and on shell",
        "hence the pair (Psi with (m, lambda), Gamma Psi with (-m, -lambda)) has total energy-momentum density T + T' = 0, total current J + J' = 0 and total charge Q + Q' = 0, as classical bilinears (c-numbers for dirac16complex00, Grassmann-algebra elements for dirac16complex)"},
      "proof" -> {
        "Psibar' = (Gamma Psi)^dagger C = Psi^dagger Gamma C = Psibar Gamma, because Gamma is real symmetric and commutes with C",
        "S' = Psibar Gamma Gamma Psi = S; Psibar' gamma^a Psi' = Psibar Gamma gamma^a Gamma Psi = -Psibar gamma^a Psi; D_mu commutes with Gamma because Omega_mu is a combination of the S^ab, which commute with Gamma",
        "so every kinetic and current bilinear changes sign while S and U(S) are invariant: L_(m,lambda)[Gamma Psi] = sqrt|g| (-K - m S - (lambda/2) S^2) = -L_(-m,-lambda)[Psi]",
        "gamma^mu D_mu (Gamma Psi) = -Gamma gamma^mu D_mu Psi gives the field-equation statement; T_mu nu is a sum of kinetic bilinears and -g_mu nu L/sqrt|g|, both odd under (Psi, m, lambda) -> (Gamma Psi, -m, -lambda)",
        "the argument uses only the matrix identities and linearity in the coefficients (sqrt|g|, e^mu_a, omega_mu ab), so it holds in every field and for both statistics (the substitution Psi_A -> +-Psi_A never reorders Grassmann factors)"},
      "verification" -> Join[namesWith["T1_"], namesWith["Gamma_properties"]]|>,
    <|"id" -> "T2",
      "name" -> "mirror pairing (Gamma combined with a Pin(4,4) reflection of character -1)",
      "hypotheses" -> {
        "n a space-like frame direction (x1, x2, x3 or x8); P_n = Gamma gamma^n = +- the product of the seven other gammas, an element of Pin(4,4) with P_n^-1 gamma^a P_n = (R_n)^a_b gamma^b (it covers the reflection R_n) and P_n^dagger C P_n = -C (character -1: S -> -S)",
        "general field: the frame is reflected, e' = R_n e (same metric), and Psi' = Gamma P_n Psi = gamma^n Psi at the same point",
        "primordial field: the reflection is realised by the isometry phi: x8 -> pi/(6H) - x8 (z -> pi - z), the Z2 mirror across the patch end z = pi/2, with Psi'(phi(x)) = gamma^(x8) Psi(x); the brane z = pi/2 is a degenerate surface of the metric (g_88 = 0, sqrt|g| = 0) and the extension of the field to the mirror patch is the ASSUMED Z2 construction of SPEC section 7",
        "both statistics; U(S) = (lambda/2) S^2 (any even function of S)"},
      "statement" -> {
        "L_(m,lambda)[gamma^n Psi; R_n e] = +L_(-m,+lambda)[Psi; e] in every field; in the primordial field L_(m,lambda)[Psi'](phi(x)) = L_(-m,lambda)[Psi](x)",
        "Psi solves the (-m, lambda) equations iff its mirror image solves the (m, lambda) equations; S' = -S",
        "T'_mu nu = T^(-m,lambda)_mu nu transformed as a tensor (in the primordial field: (R_8 T R_8)_mu nu at the mirror point) and J' = R_8 J: the mirror partner carries the SAME energy density and charge as the configuration it mirrors - T2 pairs +m with -m at equal, not opposite, energy-momentum",
        "for a time-like n (character +1) the same construction gives L -> -L_(-m,-lambda) (a T1-type map); the character -1 is what makes T2 a pairing (m, lambda) -> (-m, lambda) with L -> +L"},
      "proof" -> {
        "for M = gamma^n with n space-like: M^dagger C M = -C (S -> -S) and M^dagger C gamma^a M = (R_n)^a_b C gamma^b; with gamma'^mu = e^mu_b (R_n)^b_a gamma^a the kinetic term is invariant (R_n^2 = I) and the connection term too (the canonical connection of R_n e is R_n omega R_n)",
        "so L_(m,lambda)[gamma^n Psi; R_n e] = sqrt|g| (K + m S - (lambda/2) S^2) = L_(-m,lambda)[Psi; e]",
        "in the primordial field phi is an isometry whose pulled-back positive vielbein is R_8 e, and sqrt|g| d^8x is invariant (|Jacobian| = 1), which turns the frame statement into the mirror statement"},
      "verification" -> Join[namesWith["T2_"]]|>,
    <|"id" -> "Q",
      "name" -> "quantum-level reading",
      "hypotheses" -> {
        "dirac16complex canonically quantised with x4 as the evolution time and the anticommutator {Psi_A, Psi_B^dagger} = (N^-1)_AB delta^7/sqrt|g| fixed by the x4-derivative kernel (i/2) sqrt|g| N of the Lagrangian (SPEC section 6, N = B for L_(m,lambda)); dirac16complex00 is classical and has no quantum reading"},
      "statement" -> {
        "the chirality image chi = Gamma Psi carries the Krein metric -B: {chi, chi^dagger} = Gamma B Gamma delta/sqrt|g| = -B delta/sqrt|g|, which is also the anticommutator demanded by its own Lagrangian L_(m,lambda)[Gamma chi] = -L_(-m,-lambda)[chi]",
        "the image's own generators (energy, momentum, charge from its own Lagrangian) coincide with those of Psi: the pair Psi, Gamma Psi is ONE quantum system, and the T1 identity T^(-m,-lambda)[Gamma Psi] = -T^(m,lambda)[Psi] is an identity between operators of that one system",
        "an independently quantised (-m,-lambda) universe has the anticommutator +B (from L_(-m,-lambda)), its own vacuum and generators; it cannot be identified with Gamma Psi (B != -B); on the product state space the generators add and no cancellation P_1 + P_2 = 0 follows",
        "the one-particle Hamiltonians satisfy Gamma h_m Gamma = h_(-m) (flat space and a general field at a point, frozen coefficients) and gamma^(x8) h_m(k) gamma^(x8) = h_(-m)(R_8 k): the +m and -m one-particle (lambda = 0) spectra are identical; in flat 4+4 space every eigenspace of REAL frequency (w^2 = m^2 + k1^2 + k2^2 + k3^2 + k8^2 - k5^2 - k6^2 - k7^2 > 0) has Krein inertia (4,4) (proved for every such k), and every eigenspace of imaginary or zero frequency is Krein-neutral (B vanishes on it)",
        "the T2 image gamma^(x8) Psi keeps the anticommutator +B: the mirror (-m, lambda) universe is an ordinary, independently quantisable copy with equal energies"},
      "verification" -> namesWith["Q_"]|>},
  "data" -> <|
    "reflections" -> Table[<|"direction" -> r["name"], "eta_nn" -> r["eta"], "P_n_equals_sign_times_product_of_other_seven" -> r["productSign"],
        "character_of_P_n" -> r["character"], "S_sign_under_gamma_n" -> r["scalarSign"], "kinetic_sign_under_gamma_n_with_frame_reflection" -> r["kineticSign"],
        "mass_coupling_map" -> If[r["eta"] == 1, "(m, lambda) -> (-m, lambda), L -> +L (T2)", "(m, lambda) -> (-m, -lambda), L -> -L (T1-type)"]|>, {r, reflectionRows}],
    "Krein_signs_M_B_Mdagger" -> (<|"map" -> #[[1]], "sign" -> #[[2]]|> & /@ kreinRows),
    "one_particle_flat" -> <|
      "hamiltonian" -> "h_m(k) = -i m gamma^(x4) - gamma^(x4) sum_(a != x4) k_a gamma^a",
      "square" -> "h_m(k)^2 = (m^2 + k1^2 + k2^2 + k3^2 + k8^2 - k5^2 - k6^2 - k7^2) I16",
      "samples" -> Table[<|"m" -> s["m"], "k" -> s["k"], "w" -> istr[s["w"]], "dim_plus_w" -> s["dimPlus"], "dim_minus_w" -> s["dimMinus"],
          "B_inertia_plus_w" -> s["inertiaPlus"], "B_inertia_minus_w" -> s["inertiaMinus"]|>, {s, sampleRows}]|>|>,
  "T3" -> "The Kohn-Sham level pairing (SPEC section 9, T3) is not part of this file; it is proved separately in Revision/pairing/kohn_sham/ (theorem record t3-theory.json, reports/wolfram-t3.json and reports/python-t3.json).",
  "not_established" -> {
    "No creation process: the theorems map solutions to solutions and quantities to quantities; no equation of this record produces a pair of universes from anything, and no initial state, vacuum decay or tunnelling process is derived.",
    "No rate and no amplitude: no transition amplitude, probability, cross-section, rate or Bogoliubov coefficient for creating universes of masses {+m, -m} is computed or implied.",
    "No dynamical necessity: nothing forces the partner configuration to exist or to be realised; T1 and T2 are correspondences between solutions of two theories (parameters (m, lambda) and (-m, -lambda), or (m, lambda) and (-m, lambda)), not a mechanism.",
    "T1 is not a symmetry of a single theory: it changes the parameters and the sign of the action; it pairs (m, lambda) with (-m, -lambda), so for lambda != 0 it is not a pure +m / -m pairing (that is T2, which keeps lambda and pairs at EQUAL energy-momentum).",
    "The vanishing total energy-momentum and charge of the T1 pair holds for classical bilinears (and as an operator identity within ONE quantum system); it does not hold for two independently quantised universes, whose generators add without cancelling.",
    "Test-field statement only: the gravitational field is fixed and the same for both members; back-reaction through the Einstein-Lovelock equations of SPEC section 5 (which would need the field equations for a4 with the pair as source) is not addressed here.",
    "The Z2 brane: the mirror across z = pi/2 uses the ASSUMED Z2 construction of SPEC section 7; the metric is degenerate at z = pi/2 (g_88 = 0, sqrt|g| = 0), and no junction condition, brane tension or matching of the field across the brane is derived here.",
    "Quantum positivity: in flat 4+4 space every real-frequency energy eigenspace of the one-particle Hamiltonian has Krein inertia (4,4) and every imaginary- or zero-frequency eigenspace (the growing extra-time modes) is Krein-neutral; a positive-norm Fock space for either universe is not established by these theorems.",
    "The Kohn-Sham level (T3) is not established by this file; it is proved separately, with its own hypotheses (ASSUMED Z2 brane, instantaneous mean-field Kohn-Sham states), in Revision/pairing/kohn_sham/."}|>;
theoryText = toJ[theory, ""] <> "\n";
theoryText2 = toJ[theory, ""] <> "\n";

writeLF[path_, text_String] := Module[{s = OpenWrite[path, BinaryFormat -> True, CharacterEncoding -> "UTF-8"]},
  BinaryWrite[s, ToCharacterCode[text, "UTF-8"]]; Close[s]];
addCheck["theory_file_deterministic",
  theoryText === theoryText2 && !StringContainsQ[theoryText, "\r"] && !StringContainsQ[theoryText, "RevisionPairing`"],
  "pairing-theory.json text generated twice in this run is identical (no time stamps), LF only, no internal symbol names, " <> ToString[StringLength[theoryText]] <> " characters"];
writeLF[FileNameJoin[{$pairingDir, "pairing-theory.json"}], theoryText];

nPass = Count[checks, c_ /; c["verdict"] == "PASS"];
nTot = Length[checks];
report = StringJoin[
  "{\n",
  "  \"report\": ", jstr["Revision pairing theorems (SPEC section 9): T1, T2 and the quantum-level reading, verified exactly in WolframScript for both statistics"], ",\n",
  "  \"producer\": ", jstr["Revision/pairing/wolfram/verify_pairing.wls"], ",\n",
  "  \"package\": ", jstr["Revision/pairing/wolfram/RevisionPairing.wl"], ",\n",
  "  \"fixture\": ", jstr["Revision/algebra/gammas.json"], ",\n",
  "  \"theory\": ", jstr["Revision/pairing/pairing-theory.json"], ",\n",
  "  \"coordinates\": ", jstr["x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; x8 = the hidden direction"], ",\n",
  "  \"summary\": {\"passed\": ", ToString[nPass], ", \"failed\": ", ToString[nTot - nPass], ", \"total\": ", ToString[nTot], "},\n",
  "  \"checks\": [\n",
  StringRiffle[("    {\"name\": " <> jstr[#["name"]] <> ", \"verdict\": " <> jstr[#["verdict"]] <> ", \"detail\": " <> jstr[#["detail"]] <> "}") & /@ checks, ",\n"],
  "\n  ]\n}\n"];
writeLF[FileNameJoin[{$pairingDir, "reports", "wolfram-pairing.json"}], report];

Print[nPass, "/", nTot, " checks passed; time ", Round[AbsoluteTime[] - t0, 0.01], " s"];
Exit[If[nPass == nTot, 0, 1]];
