#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_algebra.wls

   Driver for Revision/algebra/wolfram/RevisionAlgebra.wl (Revision/SPEC.md, section 2).
   Writes, deterministically (LF line endings, no time stamps):
     Revision/algebra/gammas.json                    the fixture (gamma, C, Gamma, B, S; order x1..x8)
     Revision/algebra/reports/wolfram-algebra.json   every check with name, verdict, detail
   Usage:  wolframscript -file Revision/algebra/wolfram/verify_algebra.wls
   Every check is exact (integer / Gaussian-rational arithmetic, NullSpace and MatrixRank over the
   rationals); nothing is floating point.  Exit code 0 if every check passes, 1 otherwise.
*)

$here = DirectoryName[$InputFileName];
$algebraDir = FileNameJoin[{$here, ".."}];
Get[FileNameJoin[{$here, "RevisionAlgebra.wl"}]];

t0 = AbsoluteTime[];
checks = {};
addCheck[name_String, ok_, detail_String] :=
  AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];

coords = RACoordinates;
g = RAGamma; eta = RAEta;
id16 = IdentityMatrix[16]; id8 = IdentityMatrix[8];
zero16 = ConstantArray[0, {16, 16}];
spaceLike = {1, 2, 3, 8}; timeLike = {4, 5, 6, 7};
anti[a_, b_] := a . b + b . a;
comm[a_, b_] := a . b - b . a;

(* ---------- 0. the author's building blocks ---------- *)
addCheck["s4_t4_entries_from_Signature_and_deltas",
  And @@ Flatten[Table[
    {RAs4[h][[p, q]] == Signature[{h, p, q, 4}] - (KroneckerDelta[p, 4] KroneckerDelta[q, h] - KroneckerDelta[p, h] KroneckerDelta[q, 4]),
     RAt4[h][[p, q]] == Signature[{h, p, q, 4}] + (KroneckerDelta[p, 4] KroneckerDelta[q, h] - KroneckerDelta[p, h] KroneckerDelta[q, 4])},
    {h, 3}, {p, 4}, {q, 4}]],
  "s4[h]_pq = Signature[{h,p,q,4}] - (d_p4 d_qh - d_ph d_q4), t4[h]_pq = Signature[{h,p,q,4}] + (d_p4 d_qh - d_ph d_q4), h = 1..3, p, q = 1..4 (the author's Qa -+ Qb), re-checked entry by entry with KroneckerDelta"];

eps4 = LeviCivitaTensor[4, List];
dual[m_] := Table[(1/2) Sum[eps4[[p, q, j1, j2]] m[[j1, j2]], {j1, 4}, {j2, 4}], {p, 4}, {q, 4}];
addCheck["s4_self_dual_t4_anti_self_dual",
  And @@ Table[dual[RAs4[h]] == RAs4[h] && dual[RAt4[h]] == -RAt4[h], {h, 3}],
  "(1/2) eps_pqrs s4[h]_rs = s4[h] and (1/2) eps_pqrs t4[h]_rs = -t4[h] for h = 1, 2, 3 (the notebook's SelfDualAntiSymmetric / AntiSelfDualAntiSymmetric)"];

addCheck["s4_t4_quaternion_algebras",
  And @@ Flatten[Table[
    {anti[RAs4[h], RAs4[k]] == -2 KroneckerDelta[h, k] IdentityMatrix[4],
     anti[RAt4[h], RAt4[k]] == -2 KroneckerDelta[h, k] IdentityMatrix[4],
     comm[RAs4[h], RAt4[k]] == ConstantArray[0, {4, 4}],
     Transpose[RAs4[h]] == -RAs4[h], Transpose[RAt4[h]] == -RAt4[h]}, {h, 3}, {k, 3}]],
  "{s4[h], s4[k]} = {t4[h], t4[k]} = -2 delta_hk I4, [s4[h], t4[k]] = 0, all six antisymmetric: two commuting copies of the imaginary quaternions"];

addCheck["sigma8_involution",
  RASigma8 . RASigma8 == id8 && Tr[RASigma8] == 0 && Transpose[RASigma8] == RASigma8,
  "sigma = {{0, I4}, {I4, 0}}: sigma^2 = I8, Tr sigma = 0, sigma symmetric"];

addCheck["tau_taubar_Clifford_relation",
  And @@ Flatten[Table[
    RATau[A] . RATauBar[B] + RATau[B] . RATauBar[A] == 2 RAEta4488[[A + 1, B + 1]] id8 &&
    RATauBar[A] . RATau[B] + RATauBar[B] . RATau[A] == 2 RAEta4488[[A + 1, B + 1]] id8, {A, 0, 7}, {B, 0, 7}]],
  "tau[A] taubar[B] + tau[B] taubar[A] = taubar[A] tau[B] + taubar[B] tau[A] = 2 eta4488_AB I8 for A, B = 0..7, eta4488 = diag(1,1,1,1,-1,-1,-1,-1) (the notebook's frame order)"];

addCheck["tau7_and_sigma_identities",
  RASigma8 == RATau[1] . RATau[2] . RATau[3] && RASigma8 == RATau[4] . RATau[5] . RATau[6] . RATau[7] &&
  And @@ Table[RASigma8 . RATauBar[A] == Transpose[RASigma8 . RATau[A]], {A, 0, 7}],
  "sigma = tau[1] tau[2] tau[3] = tau[4] tau[5] tau[6] tau[7] and sigma taubar[A] = (sigma tau[A])^T, A = 0..7 (identities stated in the notebook, re-verified)"];

addCheck["T16_block_form",
  And @@ Table[RAT16[A][[1 ;; 8, 1 ;; 8]] == ConstantArray[0, {8, 8}] &&
    RAT16[A][[9 ;; 16, 9 ;; 16]] == ConstantArray[0, {8, 8}] &&
    RAT16[A][[1 ;; 8, 9 ;; 16]] == RATauBar[A] && RAT16[A][[9 ;; 16, 1 ;; 8]] == RATau[A], {A, 0, 7}],
  "T16[A] = {{0, taubar[A]}, {tau[A], 0}}, A = 0..7"];

(* ---------- 1. Clifford relation in the author's order x1..x8 ---------- *)
addCheck["coordinate_map",
  RANotebookFrame == {1, 2, 3, 4, 5, 6, 7, 0} && And @@ Table[g[[a]] == RAT16[RANotebookFrame[[a]]], {a, 8}],
  "gamma^(x1..x3) = T16[1..3], gamma^(x4) = T16[4], gamma^(x5..x7) = T16[5..7], gamma^(x8) = T16[0] (SPEC section 2)"];

addCheck["eta_in_author_order",
  eta == DiagonalMatrix[{1, 1, 1, -1, -1, -1, -1, 1}],
  "eta = diag(+1,+1,+1,-1,-1,-1,-1,+1) in the order x1..x8 (read off from the notebook's eta4488 through the frame map): space-like x1, x2, x3, x8; time-like x4, x5, x6, x7"];

cliffordTable = Table[anti[g[[a]], g[[b]]] == 2 eta[[a, b]] id16, {a, 8}, {b, 8}];
addCheck["Clifford_relation",
  And @@ Flatten[cliffordTable],
  "{gamma^a, gamma^b} = 2 eta^ab I16 for all 64 pairs a, b in x1..x8 (exact integer arithmetic); " <>
  "squares: " <> StringRiffle[Table[coords[[a]] <> ":" <> ToString[eta[[a, a]]], {a, 8}], ", "]];

addCheck["reality",
  And @@ (MatrixQ[#, IntegerQ] & /@ g) && Union[Flatten[g]] == {-1, 0, 1},
  "every gamma^a is a real 16 x 16 matrix with entries in {-1, 0, 1}"];

addCheck["signed_permutation_matrices",
  And @@ Table[Sort[Total[Abs[g[[a]]], {1}]] == ConstantArray[1, 16] && Sort[Total[Abs[g[[a]]], {2}]] == ConstantArray[1, 16], {a, 8}],
  "every gamma^a has exactly one nonzero entry (+-1) in each row and each column (a signed permutation matrix, hence orthogonal)"];

symPattern = Table[If[Transpose[g[[a]]] == g[[a]], "symmetric", If[Transpose[g[[a]]] == -g[[a]], "antisymmetric", "neither"]], {a, 8}];
addCheck["symmetry_pattern",
  And @@ Table[symPattern[[a]] == If[MemberQ[spaceLike, a], "symmetric", "antisymmetric"], {a, 8}],
  "gamma^T = eta gamma (no sum): " <> StringRiffle[Table[coords[[a]] <> " " <> symPattern[[a]], {a, 8}], ", "] <>
  " (the space-like gammas symmetric, the time-like antisymmetric)"];

(* ---------- 2. C, Gamma, B ---------- *)
C16 = RAC;
addCheck["C_definition",
  C16 == g[[8]] . g[[1]] . g[[2]] . g[[3]] && C16 == RAT16[0] . RAT16[1] . RAT16[2] . RAT16[3],
  "C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3) = the notebook's sigma16 = T16[0] T16[1] T16[2] T16[3]"];
addCheck["C_real_symmetric",
  MatrixQ[C16, IntegerQ] && Transpose[C16] == C16,
  "C is a real (integer) symmetric matrix"];
addCheck["C_squared_identity", C16 . C16 == id16, "C^2 = I16"];
cGammaPattern = Table[Transpose[C16 . g[[a]]] == -(C16 . g[[a]]) && MatrixQ[C16 . g[[a]], IntegerQ], {a, 8}];
addCheck["C_gamma_real_antisymmetric",
  And @@ cGammaPattern,
  "C gamma^a is real and antisymmetric for every a in x1..x8 (so Psibar gamma^a Psi = Psi^dagger C gamma^a Psi; for real commuting spinors it vanishes)"];
addCheck["C_gamma_C_inverse",
  And @@ Table[C16 . g[[a]] . C16 == -Transpose[g[[a]]], {a, 8}],
  "C gamma^a C^-1 = -(gamma^a)^T for every a (equivalent statement)"];

Gam = RAChirality;
addCheck["Gamma_definition",
  Gam == Dot @@ g[[{8, 1, 2, 3, 4, 5, 6, 7}]] && Gam == RAT16[8],
  "Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) = the notebook's T16[8] = T16[0] ... T16[7]"];
addCheck["Gamma_diag",
  Gam == ArrayFlatten[{{-id8, 0}, {0, id8}}],
  "Gamma = diag(-I8, I8)"];
addCheck["Gamma_anticommutes_with_gammas",
  And @@ Table[anti[Gam, g[[a]]] == zero16, {a, 8}] && Gam . Gam == id16,
  "{Gamma, gamma^a} = 0 for all a, Gamma^2 = I16"];
addCheck["Gamma_commutes_with_C",
  comm[Gam, C16] == zero16,
  "[Gamma, C] = 0 (C is a product of an even number of gammas)"];
addCheck["notebook_product_identity",
  (Dot @@ Table[RAT16[A], {A, 0, 8}]) == id16,
  "T16[0] T16[1] ... T16[7] T16[8] = I16 (an identity stated in the notebook; it is Gamma^2 = I16)"];

Bm = RAB;
addCheck["B_definition", Bm == -I C16 . g[[4]], "B = -i C gamma^(x4)"];
addCheck["B_Hermitian", ConjugateTranspose[Bm] == Bm, "B^dagger = B"];
addCheck["B_squared_identity", Bm . Bm == id16, "B^2 = I16"];
bEig = Eigenvalues[Bm];
addCheck["B_signature_8_8",
  Count[bEig, 1] == 8 && Count[bEig, -1] == 8 && Tr[Bm] == 0,
  "the exact eigenvalues of B are +1 (multiplicity " <> ToString[Count[bEig, 1]] <> ") and -1 (multiplicity " <>
  ToString[Count[bEig, -1]] <> "), Tr B = " <> ToString[Tr[Bm]] <> ": the Hermitian form Psi^dagger B Psi has signature (8, 8)"];
addCheck["B_purely_imaginary",
  Re[Bm] == zero16 && MatrixQ[Im[Bm], IntegerQ] && Transpose[Im[Bm]] == -Im[Bm],
  "B = i K with K = -C gamma^(x4) a real antisymmetric integer matrix"];

(* ---------- 3. S^ab ---------- *)
S = RAS;
addCheck["S_antisymmetric_in_ab",
  And @@ Flatten[Table[S[[a, b]] == -S[[b, a]], {a, 8}, {b, 8}]] && And @@ Table[S[[a, a]] == zero16, {a, 8}],
  "S^ab = -S^ba, S^aa = 0"];
addCheck["S_half_product",
  And @@ Flatten[Table[If[a != b, S[[a, b]] == (1/2) g[[a]] . g[[b]], True], {a, 8}, {b, 8}]],
  "S^ab = (1/2) gamma^a gamma^b for a != b"];
addCheck["S_real_entries_in_half_integers",
  And @@ Flatten[Table[MatrixQ[2 S[[a, b]], IntegerQ], {a, 8}, {b, 8}]] && Union[Flatten[S]] == {-1/2, 0, 1/2},
  "every S^ab is real with entries in {-1/2, 0, 1/2}"];
addCheck["S_gamma_commutator",
  And @@ Flatten[Table[comm[S[[a, b]], g[[c]]] == eta[[b, c]] g[[a]] - eta[[a, c]] g[[b]], {a, 8}, {b, 8}, {c, 8}]],
  "[S^ab, gamma^c] = eta^bc gamma^a - eta^ac gamma^b for all 512 triples (gamma^a is a vector under the generators S^ab)"];
addCheck["S_Lorentz_algebra",
  And @@ Flatten[Table[comm[S[[a, b]], S[[c, d]]] ==
    eta[[b, c]] S[[a, d]] - eta[[a, c]] S[[b, d]] - eta[[b, d]] S[[a, c]] + eta[[a, d]] S[[b, c]],
    {a, 8}, {b, a + 1, 8}, {c, 8}, {d, c + 1, 8}]],
  "[S^ab, S^cd] = eta^bc S^ad - eta^ac S^bd - eta^bd S^ac + eta^ad S^bc for all a < b, c < d: the Lie algebra so(4,4)"];
addCheck["S_preserves_C",
  And @@ Flatten[Table[Transpose[S[[a, b]]] . C16 + C16 . S[[a, b]] == zero16, {a, 8}, {b, 8}]],
  "S^T C + C S = 0 (equivalently S^dagger C + C S = 0, S real) for every S^ab: Psibar Psi = Psi^dagger C Psi is Spin(4,4) invariant"];
bInvPairs = Flatten[Table[If[ConjugateTranspose[S[[a, b]]] . Bm + Bm . S[[a, b]] == zero16, Nothing, {a, b}], {a, 8}, {b, a + 1, 8}], 1];
addCheck["S_preserves_B_only_off_x4",
  Sort[bInvPairs] == Sort[Flatten[Table[If[a == 4 || b == 4, {a, b}, Nothing], {a, 8}, {b, a + 1, 8}], 1]] &&
  And @@ Table[If[b == 4, True,
    ConjugateTranspose[S[[4, b]]] . Bm + Bm . S[[4, b]] == I C16 . g[[b]]], {b, 8}],
  "S^dagger B + B S = 0 holds exactly for the 21 generators S^ab with a, b != x4; for the 7 generators S^(x4 b) it equals i C gamma^b != 0 (exact): " <>
  "the Hermitian form Psi^dagger B Psi (signature (8,8)) is invariant under the Spin(4,3) that fixes the x4 direction, " <>
  "not under all of Spin(4,4) (B = -i C gamma^(x4) singles out the time x4, like Psi^dagger Psi in Minkowski space); " <>
  "the Spin(4,4)-invariant form is Psibar Psi = Psi^dagger C Psi"];
addCheck["S_commutes_with_Gamma",
  And @@ Flatten[Table[comm[S[[a, b]], Gam] == zero16, {a, 8}, {b, 8}]],
  "[S^ab, Gamma] = 0: every S^ab is block diagonal in the chiral halves (Gamma = -1: rows 1..8, Gamma = +1: rows 9..16)"];

(* ---------- 4. irreducibility under Pin(4,4), splitting under Spin(4,4) ---------- *)
basisAll = Join @@ Table[Last /@ RACliffordBasis[k], {k, 0, 8}];
spanAll = RASpanDimension[basisAll];
spanEven = RASpanDimension[Join @@ Table[Last /@ RACliffordBasis[k], {k, 0, 8, 2}]];
addCheck["Clifford_basis_spans_full_matrix_algebra",
  Length[basisAll] == 256 && spanAll == 256,
  "the 256 ordered products gamma^(a1)...gamma^(ak) (a1 < ... < ak, k = 0..8) are linearly independent: span dimension " <>
  ToString[spanAll] <> " = 16^2, so the gammas generate all of Mat(16, R) (and Mat(16, C) over C)"];
addCheck["even_subalgebra_dimension",
  spanEven == 128,
  "the even products (k = 0, 2, 4, 6, 8) span a space of dimension " <> ToString[spanEven] <>
  " = 2 x 8^2: Mat(8) + Mat(8), the even Clifford algebra generated by Spin(4,4)"];

commPin = RACommutantBasis[g];
addCheck["Pin44_irreducible_commutant_dim_1",
  Length[commPin] == 1 && MatrixRank[{Flatten[First[commPin]], Flatten[id16]}] == 1,
  "the commutant {X : X gamma^a = gamma^a X, a = x1..x8} has dimension " <> ToString[Length[commPin]] <>
  " and is spanned by I16 (exact NullSpace over Q; the gammas are rational, so the complex commutant has the same dimension). " <>
  "Pin(4,4) is generated by the unit vectors v^a gamma_a and its linear span is the whole Clifford algebra, so its commutant is this one: " <>
  "the 16-dimensional representation is irreducible under Pin(4,4) (Schur, over C)"];

sGen = Flatten[Table[S[[a, b]], {a, 8}, {b, a + 1, 8}], 1];
commSpin = RACommutantBasis[sGen];
PL = RAPL; PR = RAPR;
addCheck["Spin44_commutant_dim_2_chiral_projectors",
  Length[commSpin] == 2 && MatrixRank[Join[Flatten /@ commSpin, {Flatten[PL], Flatten[PR]}]] == 2 &&
  PL + PR == id16 && PL . PL == PL && PR . PR == PR && PL . PR == zero16 && Tr[PL] == 8 && Tr[PR] == 8,
  "the commutant of the 28 generators S^ab (a < b) has dimension " <> ToString[Length[commSpin]] <>
  " and is spanned by the chiral projectors P_L = (I - Gamma)/2, P_R = (I + Gamma)/2 (rank 8 each, P_L + P_R = I, P_L P_R = 0); " <>
  "the S^ab generate the Lie algebra of Spin(4,4), whose identity component is generated by exp of it"];

sL = (#[[1 ;; 8, 1 ;; 8]]) & /@ sGen;
sR = (#[[9 ;; 16, 9 ;; 16]]) & /@ sGen;
offOK = And @@ ((#[[1 ;; 8, 9 ;; 16]] == ConstantArray[0, {8, 8}] && #[[9 ;; 16, 1 ;; 8]] == ConstantArray[0, {8, 8}]) & /@ sGen);
commL = RACommutantBasis[sL]; commR = RACommutantBasis[sR];
addCheck["chiral_halves_irreducible",
  offOK && Length[commL] == 1 && Length[commR] == 1,
  "the S^ab restricted to the Gamma = -1 half (rows 1..8) and to the Gamma = +1 half (rows 9..16): commutant dimensions " <>
  ToString[Length[commL]] <> " and " <> ToString[Length[commR]] <> ": each 8-dimensional half is irreducible"];
interLR = RAIntertwinerBasis[sL, sR];
interRL = RAIntertwinerBasis[sR, sL];
addCheck["chiral_halves_inequivalent_intertwiners_0",
  Length[interLR] == 0 && Length[interRL] == 0,
  "the spaces of intertwiners {X : X S_L^ab = S_R^ab X} and {X : X S_R^ab = S_L^ab X} (all a < b) have dimensions " <>
  ToString[Length[interLR]] <> " and " <> ToString[Length[interRL]] <>
  ": the two 8-dimensional irreducible representations of Spin(4,4) are inequivalent"];

addCheck["Spin_Pin_reflection_swaps_halves",
  And @@ Table[g[[a]][[1 ;; 8, 1 ;; 8]] == ConstantArray[0, {8, 8}] && g[[a]][[9 ;; 16, 9 ;; 16]] == ConstantArray[0, {8, 8}], {a, 8}],
  "every gamma^a (a reflection in Pin(4,4) of determinant -1) is block off-diagonal: it exchanges the two chiral halves, which is how the inequivalent halves combine into one Pin(4,4) irrep"];

(* ---------- 5. the fixture ---------- *)
fixture = RAFixtureString[];
fixture2 = RAFixtureString[];
fixturePath = FileNameJoin[{$algebraDir, "gammas.json"}];
writeLF[path_, text_String] := Module[{s = OpenWrite[path, BinaryFormat -> True, CharacterEncoding -> "UTF-8"]},
  BinaryWrite[s, ToCharacterCode[text, "UTF-8"]]; Close[s]];
writeLF[fixturePath, fixture];
decoded = RADecodeFixture[Import[fixturePath, "RawJSON"]];
addCheck["fixture_written_deterministically",
  fixture === fixture2 && !StringContainsQ[fixture, "\r"],
  "gammas.json text generated twice in this run is identical (no time stamps), LF line endings only, " <>
  ToString[StringLength[fixture]] <> " characters"];
addCheck["fixture_round_trip",
  decoded["gamma"] == g && decoded["C"] == C16 && decoded["Gamma"] == Gam && decoded["B"] == Bm &&
  decoded["S"] == S && decoded["eta"] == eta,
  "gammas.json re-imported and decoded reproduces gamma, C, Gamma, B, S and eta exactly"];

(* ---------- report ---------- *)
jstr[s_String] := "\"" <> StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\""}] <> "\"";
nPass = Count[checks, c_ /; c["verdict"] == "PASS"];
nTot = Length[checks];
report = StringJoin[
  "{\n",
  "  \"report\": ", jstr["Revision algebra (SPEC section 2): the author's T16 gamma matrices re-constructed and verified in WolframScript"], ",\n",
  "  \"producer\": ", jstr["Revision/algebra/wolfram/verify_algebra.wls"], ",\n",
  "  \"package\": ", jstr["Revision/algebra/wolfram/RevisionAlgebra.wl"], ",\n",
  "  \"fixture\": ", jstr["Revision/algebra/gammas.json"], ",\n",
  "  \"coordinates\": ", jstr["x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; x8 = the hidden direction"], ",\n",
  "  \"summary\": {\"passed\": ", ToString[nPass], ", \"failed\": ", ToString[nTot - nPass], ", \"total\": ", ToString[nTot], "},\n",
  "  \"checks\": [\n",
  StringRiffle[("    {\"name\": " <> jstr[#["name"]] <> ", \"verdict\": " <> jstr[#["verdict"]] <> ", \"detail\": " <> jstr[#["detail"]] <> "}") & /@ checks, ",\n"],
  "\n  ]\n}\n"];
reportDir = FileNameJoin[{$algebraDir, "reports"}];
If[!DirectoryQ[reportDir], CreateDirectory[reportDir]];
writeLF[FileNameJoin[{reportDir, "wolfram-algebra.json"}], report];

Scan[Print[#["verdict"], "  ", #["name"]] &, checks];
Print[nPass, "/", nTot, " checks passed; time ", Round[AbsoluteTime[] - t0, 0.01], " s"];
Exit[If[nPass == nTot, 0, 1]];
