#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_t3_completion.wls

   Completion of theorem T3 of Revision/SPEC.md section 9 (the Kohn-Sham level of the pairing of universes of masses
   {+m, -m}) after the adversarial verification of 2026-10-08 of Revision/pairing/kohn_sham/wolfram/verify_t3.wls
   (10 checks) and Revision/pairing/kohn_sham/python/check_t3.py (13 checks).  T3 itself (statements S1-S5 of
   Revision/pairing/kohn_sham/t3-theory.json) is unchanged; this script adds three exact checks that close the gaps
   found there and records the statement S6:

   T3C_mean_field_coefficients_from_ks_theory  the Kohn-Sham potentials are READ from ks-theory.json (verify_t3.wls
                                              writes them into the script, and its v_v clause is a tautology)
   T3C_filling_convention_mapped              the filling CONVENTION (hypothesis H5) of the +M member is carried onto
                                              the -M member in its own boundary conditions
   T3C_krein_rule_16_component                the 16-component expectation-value (Krein) rule: every component of the
                                              energy-momentum tensor and of the current is equal for the pair (S6)

   Writes (deterministic, LF): Revision/pairing/kohn_sham/t3-completion.json and
   Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json.
   Usage: wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls     Exit 0 iff all checks pass.
   Written anew; no code shared with Revision/pairing/kohn_sham/python/check_t3_completion.py.

   Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially
   DEFLATING extra times; x8 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0] (brane y = 0, tip y = -L).
*)

$here = DirectoryName[$InputFileName];
$t3Dir = FileNameJoin[{$here, ".."}];
$revDir = FileNameJoin[{$t3Dir, "..", ".."}];
checks = {};
addCheck[name_String, ok_, detail_String] := (
  AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS  ", "FAIL  "], name]);

ks = Import[FileNameJoin[{$revDir, "kohn_sham", "ks-theory.json"}], "RawJSON"];
fx = Import[FileNameJoin[{$revDir, "algebra", "gammas.json"}], "RawJSON"];
s1 = {{0, 1}, {1, 0}}; s2 = {{0, -I}, {I, 0}}; s3 = {{1, 0}, {0, -1}}; id2 = IdentityMatrix[2];
qTip[th_] := Cos[th] s3 + Sin[th] s2;

(* C1: the mean-field coefficients of ks-theory.json *)
pots = ks["exchange"]["kohnShamPotentials"];
cMeff = ToExpression[pots["Meff_coefficient_of_lambda_S"]]; cVv = ToExpression[pots["vv_coefficient_of_lambda_n"]];
meff[mm_, ll_, ss_] := mm + cMeff ll ss; vvf[ll_, nn_] := cVv ll nn; eint[ll_, nn_, ss_] := 15/32 ll ss^2 - 1/32 ll nn^2;
addCheck["T3C_mean_field_coefficients_from_ks_theory",
  cMeff === 15/16 && cVv === -1/16 && StringContainsQ[pots["e_int"], "(15/32) lambda S^2 - (1/32) lambda n^2"] &&
  StringContainsQ[pots["Meff"], "m + (15/16) lambda S(y)"] && StringContainsQ[pots["vv"], "-lambda n(y)/16"] &&
  Simplify[D[eint[lam, n, S], S] - (meff[m, lam, S] - m)] === 0 && Simplify[D[eint[lam, n, S], n] - vvf[lam, n]] === 0 &&
  Simplify[meff[-m, lam, -S] + meff[m, lam, S]] === 0 && Simplify[eint[lam, n, -S] - eint[lam, n, S]] === 0 &&
  FreeQ[vvf[lam, n], S] && Simplify[meff[-m, -lam, -S] + meff[m, lam, S]] =!= 0,
  "the Kohn-Sham potentials READ from ks-theory.json exchange.kohnShamPotentials: M_eff coefficient 15/16, v_v coefficient -1/16, e_int = (15/32) lambda S^2 - (1/32) lambda n^2 (verify_t3.wls writes these numbers into the script and its v_v clause compares vvf[lam, n] with itself; check_t3.py reads them). Consistency: M_eff - m = d e_int/dS and v_v = d e_int/dn. Map: M_eff[-m, +lambda, -S] = -M_eff[m, lambda, S], e_int even in S, v_v free of S; with (-m, -lambda) M_eff is not mapped to -M_eff (control)"];

(* C2: the filling convention carried onto the image *)
zm0 = {E^(MM y), 0}; zmI = s2 . zm0;
hk0[jj_, M_, c_] := jj (-I s1 . D[c, y] + M s2 . c);
fillOk = zmI === {0, I E^(MM y)} &&
  AllTrue[{1, -1}, (Simplify[hk0[#, MM, zm0]] === {0, 0} && Simplify[hk0[-#, -MM, zmI]] === {0, 0}) &] &&
  zm0[[2]] === 0 && zmI[[1]] === 0 &&
  Simplify[(id2 - qTip[0]) . (zm0 /. y -> -LL)] === {0, 0} && Simplify[(id2 - qTip[Pi]) . (zmI /. y -> -LL)] === {0, 0} &&
  ! TrueQ[Simplify[(id2 - qTip[0]) . (zmI /. y -> -LL)] === {0, 0}] &&
  Simplify[ComplexExpand[Conjugate[zmI] . zmI] - E^(2 MM y), MM > 0 && y \[Element] Reals] === 0;
(* S1 for an arbitrary M(y): the map intertwines the block Hamiltonians at every coupling of the continuation *)
hB[j_, M_, chi_] := j (-I s1 . D[chi, y] + M s2 . chi + kap[y] k s3 . chi) + vv[y] chi;
chiG = {c1[y], c2[y]};
pathOk = AllTrue[{1, -1}, Simplify[ComplexExpand[hB[-#, -(mm0 + cMeff lp Sf[y]), s2 . chiG] - s2 . hB[#, mm0 + cMeff lp Sf[y], chiG]]] === {0, 0} &];
addCheck["T3C_filling_convention_mapped",
  fillOk && pathOk,
  "the filling CONVENTION of ks-theory.json thermodynamics (hypothesis H5: particles = the levels with eps > 0 of the lambda = 0 problem plus the k = 0 brane zero modes, each followed continuously in lambda) is carried onto the image problem: (i) for every coupling lambda' of the continuation and any S(y), sigma2 h_j(m + (15/16) lambda' S) = h_(-j)(-(m + (15/16) lambda' S)) sigma2 (both j), so the map sends the lambda = 0 levels with eps > 0 onto the image's lambda = 0 levels with eps > 0 (same eps) and commutes with the continuation in lambda; (ii) the k = 0 brane zero mode (E^(M y), 0) of (M, j, even, theta = 0) (h_j = 0, b(0) = 0, b(-L) = 0) goes to (0, I E^(M y)), a zero mode of h_(-j)(-M) with odd parity (a(0) = 0) and the transformed tip theta = Pi (a(-L) = 0), brane-localised like the original (|chi|^2 = E^(2 M y), M > 0), for both j; it violates the UNtransformed tip theta = 0 (control). Hence the occupied set of the image is the image of the occupied set, with the same occupations (equal levels, degeneracies and N)"];

(* C3: the 16-component expectation-value (Krein) rule *)
num[x_String] := ToExpression[x]; num[x_] := x;
dec[x_Association] := Map[num, x["re"], {2}] + I Map[num, x["im"], {2}];
dec[x_List] := Map[num, x, {2}];
gm = dec /@ fx["gamma"]; chir = dec[fx["Gamma"]]; bK = dec[fx["B"]]; cK = dec[fx["C"]]; id16 = IdentityMatrix[16];
sab = Table[(gm[[a]] . gm[[b]] - gm[[b]] . gm[[a]])/4, {a, 8}, {b, 8}];
uu = Array[uS, 16]; ub = Array[uB, 16];
rhoMap = Simplify[Outer[Times, chir . uu, ub . chir] . bK + chir . Outer[Times, uu, ub] . bK . chir] === ConstantArray[0, {16, 16}];
sgn[x_] := Which[-chir . x . chir == x, 1, -chir . x . chir == -x, -1, True, 0];
gamRel = chir . chir == id16 && chir . bK . chir == -bK && chir . cK . chir == cK &&
  AllTrue[Range[8], chir . gm[[#]] . chir == -gm[[#]] &] &&
  AllTrue[Tuples[Range[8], 2], chir . sab[[#[[1]], #[[2]]]] . chir == sab[[#[[1]], #[[2]]]] &];
signsOk = sgn[bK] == 1 && sgn[cK] == -1 && sgn[bK . gm[[8]]] == -1 && AllTrue[Range[8], sgn[cK . gm[[#]]] == 1 &] &&
  AllTrue[Tuples[Range[8], 3], sgn[cK . gm[[#[[1]]]] . sab[[#[[2]], #[[3]]]]] == 1 &];
ruleOk = StringContainsQ[ks["exchange"]["expectationRule"], "rho = sum_occ f u u^dagger B"];
addCheck["T3C_krein_rule_16_component",
  rhoMap && gamRel && signsOk && ruleOk,
  "16-component level with the expectation rule of the canonical quantisation (SPEC section 6, ks-theory.json exchange.expectationRule: <Psi^dag X Psi> = Tr(X rho), rho = sum f u u^dagger B) and gamma^(x1..x8), B, C, Gamma of gammas.json: Gamma^2 = 1, Gamma B Gamma = -B, Gamma C Gamma = C, Gamma gamma^a Gamma = -gamma^a (a = 1..8), Gamma S^ab Gamma = S^ab (all 64); for a general 16-vector u, (Gamma u)(Gamma u)^dagger B = -Gamma (u u^dagger B) Gamma, so the image state has rho' = -Gamma rho Gamma and <X>' = -Tr(Gamma X Gamma rho). Hence n = <B> is unchanged, S = <C> and Q = <B gamma^(x8)> change sign, and the kinetic bilinears Psibar gamma^a d Psi and Psibar gamma^a S^bc Psi (X = C gamma^a and C gamma^a S^bc, all 8 + 512; the spin connection Omega = (1/2) omega_ab S^ab commutes with Gamma) are unchanged; with m -> -m the mass term m S and U = (lambda/2) S^2 with the same lambda are unchanged: every component of the 16-component energy-momentum tensor (Belinfante form, SPEC section 4) and the current J^a = <C gamma^a> of the image state with (-m, +lambda) equal those of the original state (S6)"];

(* ------------------------------------------------------------------ completion record *)
nPass = Count[checks, c_ /; c["verdict"] == "PASS"]; nTot = Length[checks];
jstr[s_String] := "\"" <> StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\""}] <> "\"";
toJ[x_String, ind_] := jstr[x];
toJ[x_Integer, ind_] := ToString[x];
toJ[x_List, ind_] := If[x === {}, "[]", "[\n" <> StringRiffle[(ind <> "  " <> toJ[#, ind <> "  "]) & /@ x, ",\n"] <> "\n" <> ind <> "]"];
toJ[x_Association, ind_] := "{\n" <> StringRiffle[KeyValueMap[(ind <> "  " <> jstr[#1] <> ": " <> toJ[#2, ind <> "  "]) &, x], ",\n"] <> "\n" <> ind <> "}";
record = <|
  "document" -> "Completion of theorem T3 of Revision/SPEC.md section 9 (the Kohn-Sham level of the pairing of universes of masses {+m, -m} for dirac16complex) after the adversarial verification of 2026-10-08",
  "producer" -> "Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls",
  "report" -> "Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json",
  "independent_check" -> "Revision/pairing/kohn_sham/python/check_t3_completion.py (sympy; reports/python-t3-completion.json)",
  "status" -> If[nPass == nTot, "all checks of the report passed", "SOME CHECKS FAILED - see the report"],
  "completes" -> "Revision/pairing/kohn_sham/t3-theory.json (theorem T3: hypotheses H1-H6, statements S1-S5, proof; reports/wolfram-t3.json 10 checks and reports/python-t3.json 13 checks). T3 and its statements are unchanged; this record adds S6 and closes the gaps listed under adversarial_verification",
  "coordinates" -> "x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; x8 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0] (brane y = 0, tip y = -L)",
  "background" -> "T3 holds at every fixed slice a4,0 = a4(x4) and uses no history. Where states along the Kohn-Sham history a4 = A H x4 (A = 1, the extra times x5, x6, x7 deflating as e^{-a4}) are used (the numerical demonstrations and the solver self-test at a4,0 = 1), that history is a PRESCRIBED BACKGROUND (Revision/kohn_sham/ks-theory.json adiabaticity.historyStatus): the Kohn-Sham states violate the source conditions of the a4 equations (Revision/field_equations_a4/reports/ks-source-conditions.json), so the Kohn-Sham gas is a test field without back-reaction",
  "adversarial_verification" -> {
    "Re-run: verify_t3.wls (10 checks) and check_t3.py (13 checks) pass and reproduce t3-theory.json, reports/wolfram-t3.json and reports/python-t3.json byte for byte; every step of the proof was re-derived by hand (sigma2 h_j(M) sigma2 = h_(-j)(-M); sigma2 Q(theta) sigma2 = Q(Pi - theta); densities n, t even and s, q odd; M_eff odd exactly for (-m, +lambda)). No error was found in the statement or the proof.",
    "Gap 1 (closed by T3C_mean_field_coefficients_from_ks_theory): verify_t3.wls writes the coefficients 15/16, -1/16, 15/32, -1/32 into the script instead of reading ks-theory.json, and its clause vvf[lam, n] === vvf[lam, n] compares an expression with itself (true for any v_v); the sympy checker reads the coefficients. The completion reads them in Wolfram too and replaces the tautology by the consistency M_eff - m = d e_int/dS, v_v = d e_int/dn and the evenness of e_int.",
    "Gap 2 (closed by T3C_filling_convention_mapped): hypothesis H5 (the filling convention) is defined for the canonical member (m > 0, theta = 0); the proof uses it for the image through 'both j and both parities are part of each problem' without showing that the image's particle set is the image of the original's. The completion shows it: eps > 0 at lambda = 0 is kept, the map commutes with the continuation in lambda, and the brane zero mode goes to the brane zero mode of the image in its boundary conditions.",
    "Gap 3 (closed by T3C_krein_rule_16_component): the proof works with the 2 x 2 block densities and the four diagonal components rho, p3, p_t, p8 of ks-theory.json emt. The completion lifts the equality to the 16-component expectation rule of the canonical quantisation: every component of the energy-momentum tensor and the current (S6).",
    "Gap 4 (closed by the numerical demonstrations): the numerical confirmation recorded in t3-theory.json is the solver's self-test of two states. The demonstrations solve the +M and -M universes and the negative controls for the whole canonical matrix (Rust) and a subset (reference), on the slices of the PRESCRIBED BACKGROUND history.",
    "Gap 5 (recorded here): t3-theory.json does not name the history of the demonstrations a PRESCRIBED BACKGROUND; this record does (background). t3-theory.json is left byte-identical because the documents Revision/docs/PAIR_CREATION_PROOFS and DIRAC16COMPLEX_FIELD_THEORY, the publication tests and Revision/pairing/kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md quote its checks, counts and sha256."},
  "statement" -> {
    "S6: at the 16-component level, with the expectation rule rho = sum f u u^dagger B of the canonical quantisation, the T3 image state (Psi_16 -> Gamma Psi_16, (m, lambda, theta) -> (-m, +lambda, Pi - theta)) has rho' = -Gamma rho Gamma: n is unchanged, S and Q change sign, and every component of the energy-momentum tensor and of the current J^a is unchanged",
    "H5 for the pair: the filling convention of the +M member, carried by the map, is the filling convention of the -M member in its own boundary conditions"},
  "verification" -> (#["name"] & /@ checks),
  "numerical_demonstration" -> {
    "Revision/pairing/kohn_sham/reports/t3-rust-demo.json (numerics/t3_rust_demo.py): the Rust Kohn-Sham solver solves the +M universe (m, lambda, tip 0), the -M universe (-m, +lambda, tip Pi) and the negative control (-m, +lambda, untransformed tip 0) independently for all 75 ground and 135 Mermin states of the canonical matrix of Revision/kohn_sham (slices a4,0 = 0, 0.5, 1, 1.5, 2 of the PRESCRIBED BACKGROUND history); second control: the T1 parameters (-m, -lambda, tip Pi). The shooting method is covariant under the map (the Pruefer equation of the image is that of the original with theta -> Pi/2 - theta), so the equality is at the rounding level by construction and tests the solver's handling of both members. A demonstration, not part of the proof",
    "Revision/pairing/kohn_sham/reports/t3-reference-demo.json (numerics/t3_reference_demo.py): the same with the independent reference solver (finite differences, Richardson) on a subset of 18 states, and the -M universe of the two solvers compared; the image's rotated frame is not the discrete image of the plus frame, so the equality appears only after Richardson extrapolation (a discretisation-independent test). A demonstration, not part of the proof"},
  "not_established" -> {
    "No creation process, rate or amplitude: T3 and S6 map self-consistent Kohn-Sham states to self-consistent Kohn-Sham states of a second parameter set; they do not produce a pair of universes and do not force the partner to exist.",
    "Instantaneous (adiabatic) mean-field states only, slice by slice; the time-dependent problem is OPEN; the history a4 = A H x4 of the demonstrations is a PRESCRIBED BACKGROUND without back-reaction.",
    "The Z2 brane is ASSUMED; the tip condition is a choice and T3 needs the transformed tip Pi - theta; the filling convention is a CONVENTION whose justification is OPEN.",
    "S6 is the equality of expectation values in the Kohn-Sham (quasi-free) states with the fixed Krein metric B; it is not a statement about two independently quantised universes, and the pairing is (m, lambda) -> (-m, +lambda), not (-m, -lambda).",
    "The numerical demonstrations show the equalities on the states solved, to their stated tolerances; negative-control states for which a solver found no self-consistent solution are reported as such, not as a proof that none exists."}|>;
writeLF[path_, text_String] := Module[{st = OpenWrite[path, BinaryFormat -> True]}, BinaryWrite[st, ToCharacterCode[text, "UTF-8"]]; Close[st]];
If[! DirectoryQ[FileNameJoin[{$t3Dir, "reports"}]], CreateDirectory[FileNameJoin[{$t3Dir, "reports"}]]];
writeLF[FileNameJoin[{$t3Dir, "t3-completion.json"}], toJ[record, ""] <> "\n"];
report = StringJoin[
  "{\n",
  "  \"report\": ", jstr["Revision pairing theorem T3 (SPEC section 9, the Kohn-Sham level): completion checks, exact, WolframScript"], ",\n",
  "  \"producer\": ", jstr["Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls"], ",\n",
  "  \"record\": ", jstr["Revision/pairing/kohn_sham/t3-completion.json"], ",\n",
  "  \"inputs\": ", jstr["Revision/kohn_sham/ks-theory.json, Revision/algebra/gammas.json"], ",\n",
  "  \"summary\": {\"passed\": ", ToString[nPass], ", \"failed\": ", ToString[nTot - nPass], ", \"total\": ", ToString[nTot], "},\n",
  "  \"checks\": [\n",
  StringRiffle[("    {\"name\": " <> jstr[#["name"]] <> ", \"verdict\": " <> jstr[#["verdict"]] <> ", \"detail\": " <> jstr[#["detail"]] <> "}") & /@ checks, ",\n"],
  "\n  ]\n}\n"];
writeLF[FileNameJoin[{$t3Dir, "reports", "wolfram-t3-completion.json"}], report];
Print[nPass, "/", nTot, " checks passed"];
Exit[If[nPass == nTot, 0, 1]];
