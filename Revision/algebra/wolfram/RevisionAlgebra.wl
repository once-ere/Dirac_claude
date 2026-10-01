(* ::Package:: *)

(* RevisionAlgebra.wl

   The Clifford algebra of the Revision record (Revision/SPEC.md, section 2), built anew from the
   author's own formulas.  Context RevisionAlgebra`.  Driven by Revision/algebra/wolfram/verify_algebra.wls,
   which writes the fixture Revision/algebra/gammas.json and the report
   Revision/algebra/reports/wolfram-algebra.json.

   Nothing in this file is taken from an earlier stage of the repository (artifacts/, provenance/,
   studies/, scripts/, wolfram/, notebooks/).  The formulas below were re-typed from the INPUT cells
   of the author's notebook Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb
   (the cells labelled In[45] (eta4488), In[46] (sigma), In[294] (Qa, Qb), In[300], In[301] (s4by4,
   t4by4), In[338] (tau), In[351] (taubar), In[370] (sigma16), In[371], In[372] (T16) in the notebook
   as saved; the notebook itself is never modified and never loaded by this package).

   1. The 4 x 4 blocks (indices p, q = 1..4 and h = 1..3, 1-based as in the notebook):

        Qa[h, p, q] = Signature[{h, p, q, 4}]
        Qb[h, p, q] = delta[p, 4] delta[q, h] - delta[p, h] delta[q, 4]
        s4[h][[p, q]] = Qa[h, p, q] - Qb[h, p, q]      (the notebook's SelfDualAntiSymmetric)
        t4[h][[p, q]] = Qa[h, p, q] + Qb[h, p, q]      (the notebook's AntiSelfDualAntiSymmetric)

   2. The 8 x 8 matrices (blocks of 4 + 4):

        sigma    = {{0, I4}, {I4, 0}}
        tau[0]   = I8
        tau[h]   = {{0, s4[h]}, {s4[h], 0}}            h = 1, 2, 3
        tau[7-h] = {{0, t4[h]}, {-t4[h], 0}}           h = 1, 2, 3   (so tau[6], tau[5], tau[4])
        tau[7]   = tau[1] . tau[2] . tau[3] . tau[4] . tau[5] . tau[6]
        taubar[0] = I8,   taubar[A] = sigma . Transpose[tau[A]] . sigma   A = 1..7

   3. The 16 x 16 matrices (blocks of 8 + 8), in the notebook's frame order A = 0..7
      (0 = hidden direction, 1-3 = 3-space, 4 = time, 5-7 = extra times), with the notebook's
      frame metric eta4488 = diag(1, 1, 1, 1, -1, -1, -1, -1):

        T16[A] = {{0, taubar[A]}, {tau[A], 0}}           A = 0..7
        T16[8] = T16[0] . T16[1] . ... . T16[7]

   4. The author's coordinate order x1..x8 (SPEC section 2): x1, x2, x3 = 3-space, x4 = time,
      x5, x6, x7 = the exponentially deflating extra times, x8 = the hidden direction:

        gamma^(x1..x3) = T16[1..3],  gamma^(x4) = T16[4],  gamma^(x5..x7) = T16[5..7],  gamma^(x8) = T16[0]
        eta = diag(+1, +1, +1, -1, -1, -1, -1, +1)       (order x1..x8)

      and from them (SPEC section 2):

        C     = gamma^(x8) . gamma^(x1) . gamma^(x2) . gamma^(x3)       (the notebook's sigma16)
        Gamma = gamma^(x8) . gamma^(x1) . ... . gamma^(x7)              (the notebook's T16[8])
        B     = -I C . gamma^(x4)
        S^ab  = (1/4) (gamma^a . gamma^b - gamma^b . gamma^a)

   5. Exact linear algebra used by the verifier: the commutant of a list of matrices (all X with
      M . X = X . M for every M of the list), the intertwiners between two lists (all X with
      X . F_k = T_k . X), and the dimension of the linear span of a list of matrices.  Every one is
      computed with NullSpace / MatrixRank on exact rational matrices (no floating point).  The
      matrix identity behind the commutant is, for the row-major flattening vec(X) = Flatten[X],

        vec(M . X - X . M) = (KroneckerProduct[M, I] - KroneckerProduct[I, Transpose[M]]) . vec(X).

   6. The fixture format of gammas.json (writer RAFixtureString, reader RADecodeFixture).  Every
      matrix is a list of rows; an exact rational is written as a JSON integer when it is an
      integer and otherwise as the JSON string "p/q" (lowest terms, q > 0); a complex matrix is the
      object {"re": ..., "im": ...} of its real and imaginary parts.
*)

BeginPackage["RevisionAlgebra`"];

RAQa::usage = "RAQa[h, p, q] = Signature[{h, p, q, 4}] (the author's Qa).";
RAQb::usage = "RAQb[h, p, q] = delta[p,4] delta[q,h] - delta[p,h] delta[q,4] (the author's Qb).";
RAs4::usage = "RAs4[h] (h = 1, 2, 3): the 4 x 4 block Qa - Qb (the author's s4by4[h]).";
RAt4::usage = "RAt4[h] (h = 1, 2, 3): the 4 x 4 block Qa + Qb (the author's t4by4[h]).";
RASigma8::usage = "RASigma8 = {{0, I4}, {I4, 0}} (the author's 8 x 8 sigma).";
RAEta4488::usage = "RAEta4488 = diag(1,1,1,1,-1,-1,-1,-1): the notebook's frame metric, frame order 0..7.";
RATau::usage = "RATau[A] (A = 0..7): the author's 8 x 8 tau matrices.";
RATauBar::usage = "RATauBar[A] (A = 0..7): taubar = sigma . tau^T . sigma (taubar[0] = I8).";
RAT16::usage = "RAT16[A] (A = 0..8): the author's 16 x 16 matrices in the notebook frame order; RAT16[8] = T16[0]...T16[7].";
RACoordinates::usage = "RACoordinates = {\"x1\", ..., \"x8\"}.";
RANotebookFrame::usage = "RANotebookFrame = {1, 2, 3, 4, 5, 6, 7, 0}: the notebook frame index A of T16[A] used for x1..x8.";
RAEta::usage = "RAEta = diag(+1,+1,+1,-1,-1,-1,-1,+1): the frame metric in the order x1..x8, read off from RAEta4488 through RANotebookFrame.";
RAGamma::usage = "RAGamma = {gamma^(x1), ..., gamma^(x8)}: the 16 x 16 gamma matrices in the order x1..x8.";
RAC::usage = "RAC = gamma^(x8).gamma^(x1).gamma^(x2).gamma^(x3) (the charge matrix of SPEC section 2).";
RAChirality::usage = "RAChirality = gamma^(x8).gamma^(x1).....gamma^(x7) (Gamma of SPEC section 2).";
RAB::usage = "RAB = -I RAC.gamma^(x4).";
RAS::usage = "RAS[[a, b]] = (1/4)(gamma^a.gamma^b - gamma^b.gamma^a), a, b = 1..8 in the order x1..x8.";
RAPL::usage = "RAPL = (I16 - Gamma)/2 (the notebook's P_L; the Gamma = -1 half, rows/columns 1..8).";
RAPR::usage = "RAPR = (I16 + Gamma)/2 (the notebook's P_R; the Gamma = +1 half, rows/columns 9..16).";
RACliffordBasis::usage = "RACliffordBasis[k] gives the list of {indices, product} for all increasing index lists of length k (indices 1..8 = x1..x8); k = 0 gives the identity.";
RACommutantBasis::usage = "RACommutantBasis[mats] gives a basis (n x n matrices) of {X : M.X == X.M for all M in mats}.";
RAIntertwinerBasis::usage = "RAIntertwinerBasis[from, to] gives a basis of {X : X.from[[k]] == to[[k]].X for all k}.";
RASpanDimension::usage = "RASpanDimension[mats] is the dimension of the linear span of the matrices mats (exact rank).";
RAMetricDiagonal::usage = "RAMetricDiagonal: the diagonal of the author's metric g (SPEC section 1) in the order x1..x8.";
RAMetricAssumptions::usage = "RAMetricAssumptions: {a4[x4] real, H > 0, 0 < 6 H x8 < Pi/2}.";
RAJSONRational::usage = "RAJSONRational[q] writes an exact rational as JSON: an integer, or the string \"p/q\".";
RAJSONMatrixLines::usage = "RAJSONMatrixLines[m, indent] writes a real exact matrix as a JSON list of rows, one row per line.";
RAFixtureString::usage = "RAFixtureString[] gives the full text of gammas.json (LF line endings, deterministic).";
RADecodeFixture::usage = "RADecodeFixture[assoc] turns the Import[..., \"RawJSON\"] of gammas.json back into exact matrices: an Association with keys gamma, C, Gamma, B, S, eta.";

Begin["`Private`"];

id4 = IdentityMatrix[4];
id8 = IdentityMatrix[8];
id16 = IdentityMatrix[16];
zero4 = ConstantArray[0, {4, 4}];

(* 1. the 4 x 4 blocks, re-typed from the author's input cells In[294], In[300], In[301] *)
RAQa[h_Integer, p_Integer, q_Integer] := Signature[{h, p, q, 4}];
RAQb[h_Integer, p_Integer, q_Integer] := id4[[p, 4]] id4[[q, h]] - id4[[p, h]] id4[[q, 4]];
RAs4[h_Integer /; 1 <= h <= 3] := RAs4[h] = Table[RAQa[h, p, q] - RAQb[h, p, q], {p, 4}, {q, 4}];
RAt4[h_Integer /; 1 <= h <= 3] := RAt4[h] = Table[RAQa[h, p, q] + RAQb[h, p, q], {p, 4}, {q, 4}];

(* 2. the 8 x 8 matrices: sigma (In[46]), eta4488 (In[45]), tau (In[338]), taubar (In[351]) *)
RASigma8 = ArrayFlatten[{{zero4, id4}, {id4, zero4}}];
RAEta4488 = ArrayFlatten[{{IdentityMatrix[4], 0}, {0, -IdentityMatrix[4]}}];

tauTable = Module[{t = Association[]},
  t[0] = id8;
  Do[t[7 - h] = ArrayFlatten[{{0, RAt4[h]}, {-RAt4[h], 0}}], {h, 1, 3}];
  Do[t[h] = ArrayFlatten[{{0, RAs4[h]}, {RAs4[h], 0}}], {h, 1, 3}];
  t[7] = t[1] . t[2] . t[3] . t[4] . t[5] . t[6];
  t];
RATau[a_Integer /; 0 <= a <= 7] := tauTable[a];

tauBarTable = Association[Join[{0 -> id8},
  Table[a -> RASigma8 . Transpose[tauTable[a]] . RASigma8, {a, 1, 7}]]];
RATauBar[a_Integer /; 0 <= a <= 7] := tauBarTable[a];

(* 3. the 16 x 16 matrices T16 (In[371], In[372]) *)
t16Table = Module[{t = Association[]},
  Do[t[a] = ArrayFlatten[{{0, tauBarTable[a]}, {tauTable[a], 0}}], {a, 0, 7}];
  t[8] = Dot @@ Table[t[a], {a, 0, 7}];
  t];
RAT16[a_Integer /; 0 <= a <= 8] := t16Table[a];

(* 4. the author's coordinate order (SPEC section 2) *)
RACoordinates = {"x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"};
RANotebookFrame = {1, 2, 3, 4, 5, 6, 7, 0};
RAEta = DiagonalMatrix[Table[RAEta4488[[f + 1, f + 1]], {f, RANotebookFrame}]];
RAGamma = Table[t16Table[f], {f, RANotebookFrame}];

RAC = RAGamma[[8]] . RAGamma[[1]] . RAGamma[[2]] . RAGamma[[3]];
RAChirality = Dot @@ RAGamma[[{8, 1, 2, 3, 4, 5, 6, 7}]];
RAB = -I RAC . RAGamma[[4]];
RAS = Table[(1/4) (RAGamma[[a]] . RAGamma[[b]] - RAGamma[[b]] . RAGamma[[a]]), {a, 8}, {b, 8}];
RAPL = (id16 - RAChirality)/2;
RAPR = (id16 + RAChirality)/2;

RACliffordBasis[k_Integer /; 0 <= k <= 8] :=
  Table[{s, If[s === {}, id16, Dot @@ RAGamma[[s]]]}, {s, Subsets[Range[8], {k}]}];

(* the author's metric (SPEC section 1), diagonal, order x1..x8 *)
RAMetricDiagonal = {
  E^(2 Global`a4[Global`x4]) Sin[6 Global`H Global`x8]^(1/3),
  E^(2 Global`a4[Global`x4]) Sin[6 Global`H Global`x8]^(1/3),
  E^(2 Global`a4[Global`x4]) Sin[6 Global`H Global`x8]^(1/3),
  -1,
  -E^(-2 Global`a4[Global`x4]) Sin[6 Global`H Global`x8]^(1/3),
  -E^(-2 Global`a4[Global`x4]) Sin[6 Global`H Global`x8]^(1/3),
  -E^(-2 Global`a4[Global`x4]) Sin[6 Global`H Global`x8]^(1/3),
  Cot[6 Global`H Global`x8]^2};
RAMetricAssumptions = {Element[Global`a4[Global`x4], Reals], Global`H > 0,
  0 < 6 Global`H Global`x8 < Pi/2};

(* 5. exact linear algebra *)
commutatorOperator[m_] := Module[{n = Length[m], idn},
  idn = IdentityMatrix[n, SparseArray];
  SparseArray[KroneckerProduct[SparseArray[m], idn] - KroneckerProduct[idn, SparseArray[Transpose[m]]]]];

RACommutantBasis[mats_List] := Module[{n = Length[First[mats]], sys, ns},
  sys = Join @@ (commutatorOperator /@ mats);
  ns = Normal /@ NullSpace[sys];
  Partition[#, n] & /@ ns];

(* X maps the "from" space (dimension nf) to the "to" space (dimension nt): X is nt x nf,
   vec(T.X - X.F) = (KroneckerProduct[T, I_nf] - KroneckerProduct[I_nt, Transpose[F]]) . vec(X) *)
RAIntertwinerBasis[from_List, to_List] /; Length[from] == Length[to] :=
  Module[{nf = Length[First[from]], nt = Length[First[to]], sys, ns},
  sys = Join @@ MapThread[
    SparseArray[KroneckerProduct[SparseArray[#2], IdentityMatrix[nf, SparseArray]] -
      KroneckerProduct[IdentityMatrix[nt, SparseArray], SparseArray[Transpose[#1]]]] &, {from, to}];
  ns = Normal /@ NullSpace[sys];
  Partition[#, nf] & /@ ns];

RASpanDimension[mats_List] := MatrixRank[SparseArray[Flatten /@ mats]];

(* 6. the fixture writer and reader *)
RAJSONRational[q_Integer] := ToString[q];
RAJSONRational[q_Rational] := "\"" <> ToString[Numerator[q]] <> "/" <> ToString[Denominator[q]] <> "\"";
RAJSONRational[q_] := (Message[RAJSONRational::nonrat, q]; Abort[]);
RAJSONRational::nonrat = "`1` is not an exact rational number.";

RAJSONMatrixLines[m_?MatrixQ, indent_String] :=
  "[\n" <> StringRiffle[
    (indent <> "  [" <> StringRiffle[RAJSONRational /@ #, ", "] <> "]") & /@ m, ",\n"] <>
  "\n" <> indent <> "]";

jsonComplexMatrix[m_?MatrixQ, indent_String] :=
  "{\n" <> indent <> "  \"re\": " <> RAJSONMatrixLines[Re[m], indent <> "  "] <> ",\n" <>
  indent <> "  \"im\": " <> RAJSONMatrixLines[Im[m], indent <> "  "] <> "\n" <> indent <> "}";

jsonString[s_String] := "\"" <> StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\""}] <> "\"";

jsonMatrixList[ms_List, indent_String] :=
  "[\n" <> StringRiffle[(indent <> "  " <> RAJSONMatrixLines[#, indent <> "  "]) & /@ ms, ",\n"] <>
  "\n" <> indent <> "]";

RAFixtureString[] := StringJoin[
  "{\n",
  "  \"description\": ", jsonString[
    "The real 16 x 16 gamma matrices of the author's notebook (T16, built from the tau matrices), " <>
    "re-constructed from the author's formulas by Revision/algebra/wolfram/RevisionAlgebra.wl and " <>
    "mapped to the author's coordinate order x1..x8 (SPEC section 2): gamma^(x8) = T16[0], " <>
    "gamma^(x1..x3) = T16[1..3], gamma^(x4) = T16[4], gamma^(x5..x7) = T16[5..7]. " <>
    "x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; x8 = the hidden direction."], ",\n",
  "  \"producer\": ", jsonString["Revision/algebra/wolfram/verify_algebra.wls"], ",\n",
  "  \"encoding\": ", jsonString[
    "Every matrix is a list of rows (row index first). An exact rational is a JSON integer when it is an integer " <>
    "and otherwise a JSON string \"p/q\" in lowest terms with q > 0. A complex matrix is an object " <>
    "{\"re\": real part, \"im\": imaginary part}. Indices a, b = 0..7 of gamma, eta and S stand for x1..x8."], ",\n",
  "  \"definitions\": {\n",
  "    \"gamma\": ", jsonString["gamma[a] = gamma^(x_(a+1)); {gamma^a, gamma^b} = 2 eta^ab I16"], ",\n",
  "    \"C\": ", jsonString["C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3) (the notebook's sigma16); Dirac adjoint Psibar = Psi^dagger C"], ",\n",
  "    \"Gamma\": ", jsonString["Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) (the notebook's T16[8]) = diag(-I8, I8)"], ",\n",
  "    \"B\": ", jsonString["B = -i C gamma^(x4)"], ",\n",
  "    \"S\": ", jsonString["S[a][b] = S^ab = (1/4)(gamma^a gamma^b - gamma^b gamma^a)"], "\n",
  "  },\n",
  "  \"coordinates\": [", StringRiffle[jsonString /@ RACoordinates, ", "], "],\n",
  "  \"notebookFrameIndex\": [", StringRiffle[ToString /@ RANotebookFrame, ", "], "],\n",
  "  \"eta\": [", StringRiffle[RAJSONRational /@ Diagonal[RAEta], ", "], "],\n",
  "  \"gamma\": ", jsonMatrixList[RAGamma, "  "], ",\n",
  "  \"C\": ", RAJSONMatrixLines[RAC, "  "], ",\n",
  "  \"Gamma\": ", RAJSONMatrixLines[RAChirality, "  "], ",\n",
  "  \"B\": ", jsonComplexMatrix[RAB, "  "], ",\n",
  "  \"S\": [\n",
  StringRiffle[(  "    " <> jsonMatrixList[#, "    "]) & /@ RAS, ",\n"], "\n",
  "  ]\n",
  "}\n"];

decodeRational[q_Integer] := q;
decodeRational[q_String] := Module[{neg = StringStartsQ[q, "-"], body, parts},
  body = If[neg, StringDrop[q, 1], q];
  If[!StringMatchQ[body, RegularExpression["[0-9]+/[0-9]+"]],
    Message[RADecodeFixture::badrat, q]; Abort[]];
  parts = StringSplit[body, "/"];
  If[neg, -1, 1] FromDigits[parts[[1]]] / FromDigits[parts[[2]]]];
decodeRational[q_] := (Message[RADecodeFixture::badrat, q]; Abort[]);
RADecodeFixture::badrat = "`1` is not an encoded exact rational.";
decodeMatrix[m_List] := Map[decodeRational, m, {2}];

RADecodeFixture[a_Association] := Association[
  "eta" -> DiagonalMatrix[decodeRational /@ a["eta"]],
  "gamma" -> (decodeMatrix /@ a["gamma"]),
  "C" -> decodeMatrix[a["C"]],
  "Gamma" -> decodeMatrix[a["Gamma"]],
  "B" -> decodeMatrix[a["B"]["re"]] + I decodeMatrix[a["B"]["im"]],
  "S" -> Map[decodeMatrix, a["S"], {2}]];

End[];

EndPackage[];
