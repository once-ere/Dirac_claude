(* ::Package:: *)

(* FieldEquationsA4.wl

   Revision/SPEC.md section 5: the Einstein-Lovelock field equations for a4[x4] in the author's
   primordial metric (section 1), with a general homogeneous source and with the two fields of
   section 3 as sources.  Revision code only: nothing is imported from the old stages.

   Contents (all definitions carry the prefix FE; the physical symbols are Global`):
     metric, vielbein, Christoffel symbols, Riemann tensor R^{ab}_{cd} (MTW), Ricci, Einstein;
     GKD (generalized Kronecker delta as the determinant of the delta matrix, the author's kdelta);
     the Lovelock tensors P_(k)^h_j = GKD[{h,h1..h2k},{j,j1..j2k}] R^{j1j2}_{h1h2} ... computed here
     directly (k = 1, 2, 3), and the same tensors rebuilt from the exact monomial lists of
     Revision/gkd_lovelock/results/lovelock-tensors.json;
     the gamma matrices: the author's real 16 x 16 matrices T16 (SPEC section 2), read from the Revision
     fixture Revision/algebra/gammas.json (order x1..x8) with strict parsing, are the PRIMARY
     representation (FEGammaFrame, FEC, FESab, FEOmega, FEGammaCoord); a second real 16 x 16
     representation of Cl(4,4) built here (Cl(1,1)^(x)4, FEGammaFrameComparison, FECComparison) is kept
     ONLY as a comparison representation (exact equivalence and representation independence checks);
     the canonical spin connection and the bilinear (kinetic) matrices used for the field-specific sources.

   A missing or malformed gammas.json stops the run at once with a line "ERROR  ..." and exit code 1
   (never a fallback to another representation).

   Notation of the outputs: ad1 = a4'[x4], ad2 = a4''[x4], cc = Cot[6 H x8] (> 0 on the patch
   0 < 6 H x8 < Pi/2), coordinates x1..x8 indexed 1..8.
*)

FECoords = {x1, x2, x3, x4, x5, x6, x7, x8};
FEDim = 8;

FEMetricDiag = {E^(2 a4[x4]) Sin[6 H x8]^(1/3), E^(2 a4[x4]) Sin[6 H x8]^(1/3),
   E^(2 a4[x4]) Sin[6 H x8]^(1/3), -1, -E^(-2 a4[x4]) Sin[6 H x8]^(1/3),
   -E^(-2 a4[x4]) Sin[6 H x8]^(1/3), -E^(-2 a4[x4]) Sin[6 H x8]^(1/3), Cot[6 H x8]^2};
FEMetric = DiagonalMatrix[FEMetricDiag];
FEMetricInv = DiagonalMatrix[1/FEMetricDiag];

(* the patch 0 < z < Pi/2, z = 6 H x8: every trigonometric function written through cc = Cot[z] > 0 *)
FETrigToCC = {Sin[6 H x8] -> 1/Sqrt[1 + cc^2], Cos[6 H x8] -> cc/Sqrt[1 + cc^2],
   Cot[6 H x8] -> cc, Tan[6 H x8] -> 1/cc, Csc[6 H x8] -> Sqrt[1 + cc^2],
   Sec[6 H x8] -> Sqrt[1 + cc^2]/cc};
FEDerivToSym = {Derivative[1][a4][x4] -> ad1, Derivative[2][a4][x4] -> ad2,
   Derivative[3][a4][x4] -> ad3, Derivative[4][a4][x4] -> ad4};
FENormal[e_] := Module[{r},
  r = e /. FEDerivToSym /. FETrigToCC;
  r = PowerExpand[r, Assumptions -> cc > 0 && H > 0];
  Together[Expand[r]]];
FEZeroQ[e_] := Module[{r = FENormal[e]}, r === 0 || Simplify[r, cc > 0 && H > 0] === 0];

(* ---------- Christoffel symbols, Riemann, Ricci, Einstein ---------- *)
FEChristoffel = Table[
   (1/2) Sum[FEMetricInv[[a, d]] (D[FEMetric[[d, c]], FECoords[[b]]] + D[FEMetric[[d, b]], FECoords[[c]]] -
        D[FEMetric[[b, c]], FECoords[[d]]]), {d, FEDim}],
   {a, FEDim}, {b, FEDim}, {c, FEDim}];

(* MTW: R^a_{bcd} = d_c Gamma^a_{bd} - d_d Gamma^a_{bc} + Gamma^a_{ce} Gamma^e_{bd} - Gamma^a_{de} Gamma^e_{bc} *)
FERiemann1 = Table[
   D[FEChristoffel[[a, b, d]], FECoords[[c]]] - D[FEChristoffel[[a, b, c]], FECoords[[d]]] +
    Sum[FEChristoffel[[a, c, e]] FEChristoffel[[e, b, d]] - FEChristoffel[[a, d, e]] FEChristoffel[[e, b, c]], {e, FEDim}],
   {a, FEDim}, {b, FEDim}, {c, FEDim}, {d, FEDim}];

(* R^{ab}_{cd} = g^{be} R^a_{ecd}, normalised (free of Sin^(1/3) if the warp cancels) *)
FERiemannUU = Table[FENormal[Sum[FEMetricInv[[b, e]] FERiemann1[[a, e, c, d]], {e, FEDim}]],
   {a, FEDim}, {b, FEDim}, {c, FEDim}, {d, FEDim}];

FERicci = Table[Sum[FERiemann1[[a, b, a, d]], {a, FEDim}], {b, FEDim}, {d, FEDim}];
FERicciMixed = Table[FENormal[Sum[FEMetricInv[[h, b]] FERicci[[b, j]], {b, FEDim}]], {h, FEDim}, {j, FEDim}];
FERicciScalar = FENormal[Tr[FERicciMixed]];
FEEinsteinMixed = Table[FENormal[FERicciMixed[[h, j]] - (1/2) KroneckerDelta[h, j] FERicciScalar], {h, FEDim}, {j, FEDim}];

(* ---------- GKD and the Lovelock tensors computed directly ---------- *)
FEGKD[up_List, low_List] /; Length[up] == Length[low] := Det[Outer[KroneckerDelta, up, low]];

(* the nonzero R^{ab}_{cd} with a < b and c < d; GKD is antisymmetric in each index pair, so every
   factor of the full sum over ordered pairs is 4 times the sum over these *)
FERiemannPairs = Module[{l = {}},
   Do[If[FERiemannUU[[a, b, c, d]] =!= 0, AppendTo[l, {a, b, c, d, FERiemannUU[[a, b, c, d]]}]],
    {a, FEDim}, {b, a + 1, FEDim}, {c, FEDim}, {d, c + 1, FEDim}];
   l];

(* P_(k)^h_j = sum GKD[{h, h1, ..., h2k}, {j, j1, ..., j2k}] R^{j1 j2}_{h1 h2} ... *)
FELovelockDirect[k_Integer] := Module[{acc = ConstantArray[0, {FEDim, FEDim}], tuples, up, low, val, U, L, hs, js},
   tuples = Tuples[FERiemannPairs, k];
   Do[
    low = Flatten[#[[1 ;; 2]] & /@ t];          (* the R upper indices: GKD lower list j1..j2k *)
    up = Flatten[#[[3 ;; 4]] & /@ t];           (* the R lower indices: GKD upper list h1..h2k *)
    If[DuplicateFreeQ[low] && DuplicateFreeQ[up],
     val = 4^k Times @@ (#[[5]] & /@ t);
     U = Complement[Range[FEDim], up]; L = Complement[Range[FEDim], low];
     Do[If[MemberQ[U, h] && MemberQ[L, j],
       acc[[h, j]] += FEGKD[Prepend[up, h], Prepend[low, j]] val], {h, U}, {j, L}]],
    {t, tuples}];
   Map[FENormal, acc, {2}]];

FELovelockScalarDirect[k_Integer] := Module[{acc = 0, up, low},
   Do[
    low = Flatten[#[[1 ;; 2]] & /@ t]; up = Flatten[#[[3 ;; 4]] & /@ t];
    If[DuplicateFreeQ[low] && DuplicateFreeQ[up] && Sort[low] === Sort[up],
     acc += FEGKD[up, low] 4^k Times @@ (#[[5]] & /@ t)],
    {t, Tuples[FERiemannPairs, k]}];
   FENormal[acc]];

(* ---------- the tensors rebuilt from the GKD branch's monomial lists ---------- *)
(* exponent order of a monomial (Revision/gkd_lovelock/code/src/poly.rs):
   H, a4', a4'', a4''', a4'''', E = e^{a4}, S = Sin[6 H x8]^(1/3), C = Cot[6 H x8] *)
FEMonomialVars = {H, ad1, ad2, ad3, ad4, Exp[a0], sthird, cc};
FEFromMonomials[mons_List] := Module[{e},
   e = Total[(#[[1]]/#[[2]]) Times @@ (FEMonomialVars^#[[3]]) & /@ mons];
   (* S = Sin^(1/3): on the patch Sin = 1/Sqrt[1 + cc^2] *)
   Together[Expand[PowerExpand[e /. sthird -> (1 + cc^2)^(-1/6), Assumptions -> cc > 0]]]];
FERebuildMixed[json_Association, key_String] := Table[
   FEFromMonomials[json[key][ToString[FECoords[[h]]] <> "," <> ToString[FECoords[[j]]]]["monomials"]],
   {h, FEDim}, {j, FEDim}];
FERebuildScalar[json_Association, key_String] := FENormal[ToExpression[json[key]]];

(* ---------- covariant divergence of a mixed tensor T^mu_nu (coordinate functions of x4, x8) ---------- *)
(* the input is expressed with a4[x4] (not ad1) so that it can be differentiated *)
FESymToDeriv = {ad1 -> Derivative[1][a4][x4], ad2 -> Derivative[2][a4][x4], ad3 -> Derivative[3][a4][x4],
   ad4 -> Derivative[4][a4][x4], cc -> Cot[6 H x8]};
FEDivergence[T_] := Table[
   Sum[D[T[[m, n]], FECoords[[m]]], {m, FEDim}] +
    Sum[FEChristoffel[[m, m, l]] T[[l, n]], {m, FEDim}, {l, FEDim}] -
    Sum[FEChristoffel[[l, m, n]] T[[m, l]], {m, FEDim}, {l, FEDim}],
   {n, FEDim}];

(* ---------- the PRIMARY representation: the author's T16, read from Revision/algebra/gammas.json ---------- *)
(* The fixture's documented encoding (its "encoding" field; writer RAFixtureString and reader RADecodeFixture of
   Revision/algebra/wolfram/RevisionAlgebra.wl): every matrix is a list of rows; an exact rational is a JSON
   integer when it is an integer and otherwise a JSON string "p/q" in lowest terms with q > 0 (so a string has
   q > 1); a complex matrix is {"re": ..., "im": ...}; indices
   0..7 of gamma, eta and S stand for x1..x8.  Parsing is strict: anything else (a float, a boolean, a string that
   is not "p/q" in lowest terms, a wrong shape, a missing key, a file that is not a JSON object, a missing file)
   prints one line "ERROR  ..." and exits with code 1. *)
FEFixtureError[msg_String] := (Print["ERROR  ", msg]; Exit[1]);
FEParseRationalString[s_String] := Module[{p, v},
   p = StringCases[s, RegularExpression["^(-?)([0-9]+)/([0-9]+)$"] -> {"$1", "$2", "$3"}];
   If[Length[p] != 1 || FromDigits[p[[1, 3]]] == 0, Return[$Failed, Module]];
   v = If[p[[1, 1]] === "-", -1, 1] FromDigits[p[[1, 2]]]/FromDigits[p[[1, 3]]];
   (* lowest terms, q > 1: the value written back in the same encoding is the same string *)
   If[Head[v] === Rational && (If[v < 0, "-", ""] <> ToString[Abs[Numerator[v]]] <> "/" <> ToString[Denominator[v]]) === s,
    v, $Failed]];
FEBadEntry[q_, where_String] := FEFixtureError[FEFixturePath <> ": " <> where <> " = " <> ToString[q, InputForm] <>
    " is not an exact rational in the fixture encoding (a JSON integer, or a string \"p/q\" in lowest terms with q > 1)"];
FEDecodeEntry[q_Integer, _String] := q;
FEDecodeEntry[q_String, where_String] := Module[{v = FEParseRationalString[q]}, If[v === $Failed, FEBadEntry[q, where], v]];
FEDecodeEntry[q_, where_String] := FEBadEntry[q, where];
FEDecodeVector[l_, n_Integer, where_String] := (
   If[!(ListQ[l] && Length[l] == n), FEFixtureError[FEFixturePath <> ": " <> where <> " is not a list of " <> ToString[n] <> " entries"]];
   MapIndexed[FEDecodeEntry[#1, where <> "[" <> ToString[#2[[1]] - 1] <> "]"] &, l]);
FEDecodeMatrix[m_, where_String] := (
   If[!(ListQ[m] && Length[m] == 16 && AllTrue[m, ListQ[#] && Length[#] == 16 &]),
    FEFixtureError[FEFixturePath <> ": " <> where <> " is not a list of 16 rows of 16 entries"]];
   MapIndexed[FEDecodeEntry[#1, where <> "[" <> ToString[#2[[1]] - 1] <> "][" <> ToString[#2[[2]] - 1] <> "]"] &, m, {2}]);
FEDecodeMatrixList[l_, n_Integer, where_String] := (
   If[!(ListQ[l] && Length[l] == n), FEFixtureError[FEFixturePath <> ": " <> where <> " is not a list of " <> ToString[n] <> " matrices"]];
   Table[FEDecodeMatrix[l[[a]], where <> "[" <> ToString[a - 1] <> "]"], {a, n}]);
FEReadFixture[path_String] := Module[{j, keys = {"coordinates", "notebookFrameIndex", "eta", "gamma", "C", "Gamma", "B", "S"}, missing},
   If[!FileExistsQ[path], FEFixtureError[path <> ": input file not found"]];
   j = Quiet[Check[Import[path, "RawJSON"], $Failed]];
   If[!AssociationQ[j], FEFixtureError[path <> ": not a JSON object (Import[..., \"RawJSON\"] failed)"]];
   missing = Complement[keys, Keys[j]];
   If[missing =!= {}, FEFixtureError[path <> ": missing keys " <> StringRiffle[missing, ", "]]];
   If[!(ListQ[j["coordinates"]] && Length[j["coordinates"]] == 8 && AllTrue[j["coordinates"], StringQ]),
    FEFixtureError[path <> ": coordinates is not a list of 8 strings"]];
   If[!(ListQ[j["notebookFrameIndex"]] && Length[j["notebookFrameIndex"]] == 8 && AllTrue[j["notebookFrameIndex"], IntegerQ]),
    FEFixtureError[path <> ": notebookFrameIndex is not a list of 8 integers"]];
   If[!(AssociationQ[j["B"]] && Sort[Keys[j["B"]]] === {"im", "re"}), FEFixtureError[path <> ": B is not an object {\"re\": ..., \"im\": ...}"]];
   If[!(ListQ[j["S"]] && Length[j["S"]] == 8), FEFixtureError[path <> ": S is not a list of 8 lists of matrices"]];
   <|"path" -> path, "sha256" -> IntegerString[FileHash[path, "SHA256"], 16, 64],
    "coordinates" -> j["coordinates"], "notebookFrameIndex" -> j["notebookFrameIndex"],
    "eta" -> FEDecodeVector[j["eta"], 8, "eta"],
    "gamma" -> FEDecodeMatrixList[j["gamma"], 8, "gamma"],
    "C" -> FEDecodeMatrix[j["C"], "C"],
    "Gamma" -> FEDecodeMatrix[j["Gamma"], "Gamma"],
    "B" -> FEDecodeMatrix[j["B"]["re"], "B.re"] + I FEDecodeMatrix[j["B"]["im"], "B.im"],
    "S" -> Table[FEDecodeMatrixList[j["S"][[a]], 8, "S[" <> ToString[a - 1] <> "]"], {a, 8}]|>];

FEFixturePath = FileNameJoin[{FileNameDrop[DirectoryName[$InputFileName], -2], "algebra", "gammas.json"}];
FEFixture = FEReadFixture[FEFixturePath];
(* gamma^(x1..x8) = the fixture's gamma[0..7] = T16[1..7], T16[0] (SPEC section 2) *)
FEGammaFrame = FEFixture["gamma"];
FEEta = DiagonalMatrix[{1, 1, 1, -1, -1, -1, -1, 1}];
FEC = FEGammaFrame[[8]] . FEGammaFrame[[1]] . FEGammaFrame[[2]] . FEGammaFrame[[3]];
FESabOf[g_List] := Table[(1/4) (g[[a]] . g[[b]] - g[[b]] . g[[a]]), {a, FEDim}, {b, FEDim}];
FESab = FESabOf[FEGammaFrame];

(* ---------- COMPARISON representation only (not used for any result): Cl(1,1)^(x)4, built here ---------- *)
FEsig1 = {{0, 1}, {1, 0}}; FEeps = {{0, 1}, {-1, 0}}; FEomg = FEsig1 . FEeps; FEid2 = IdentityMatrix[2];
FEKron[l_List] := Fold[KroneckerProduct, First[l], Rest[l]];
FEGen[k_Integer, blk_] := FEKron[Join[ConstantArray[FEomg, k - 1], {blk}, ConstantArray[FEid2, 4 - k]]];
(* space-like generators (square +1) on x1, x2, x3, x8; time-like (square -1) on x4, x5, x6, x7 *)
FEGammaFrameComparison = Module[{plus = Table[FEGen[k, FEsig1], {k, 4}], minus = Table[FEGen[k, FEeps], {k, 4}]},
   {plus[[1]], plus[[2]], plus[[3]], minus[[1]], minus[[2]], minus[[3]], minus[[4]], plus[[4]]}];
FECComparison = FEGammaFrameComparison[[8]] . FEGammaFrameComparison[[1]] . FEGammaFrameComparison[[2]] . FEGammaFrameComparison[[3]];

(* intertwiners: a basis of {X : X . from[[k]] == to[[k]] . X for all k}, exact (NullSpace over the rationals);
   row-major vec(X): vec(T . X - X . F) = (KroneckerProduct[T, I] - KroneckerProduct[I, Transpose[F]]) . vec(X) *)
FEIntertwinerBasis[from_List, to_List] /; Length[from] == Length[to] := Module[{n = Length[First[from]], sys},
   sys = Join @@ MapThread[
      SparseArray[KroneckerProduct[SparseArray[#2], IdentityMatrix[n, SparseArray]] -
        KroneckerProduct[IdentityMatrix[n, SparseArray], SparseArray[Transpose[#1]]]] &, {from, to}];
   Partition[#, n] & /@ (Normal /@ NullSpace[sys])];

(* diagonal vielbein e^a_mu = Sqrt|g_mumu| delta^a_mu; inverse e_a^mu *)
FEVielbeinPos = DiagonalMatrix[{E^(a4[x4]) Sin[6 H x8]^(1/6), E^(a4[x4]) Sin[6 H x8]^(1/6), E^(a4[x4]) Sin[6 H x8]^(1/6), 1,
    E^(-a4[x4]) Sin[6 H x8]^(1/6), E^(-a4[x4]) Sin[6 H x8]^(1/6), E^(-a4[x4]) Sin[6 H x8]^(1/6), Cot[6 H x8]}];
FEVielbeinInv = Inverse[FEVielbeinPos];
(* omega_mu^a_b = e^a_nu (d_mu e_b^nu + Gamma^nu_{mu lambda} e_b^lambda) *)
FESpinConnMixed = Table[
   Sum[FEVielbeinPos[[a, n]] (D[FEVielbeinInv[[n, b]], FECoords[[mu]]] +
       Sum[FEChristoffel[[n, mu, l]] FEVielbeinInv[[l, b]], {l, FEDim}]), {n, FEDim}],
   {mu, FEDim}, {a, FEDim}, {b, FEDim}];
FESpinConnLow = Table[Sum[FEEta[[a, c]] FESpinConnMixed[[mu, c, b]], {c, FEDim}], {mu, FEDim}, {a, FEDim}, {b, FEDim}];
(* Omega_mu and gamma^mu in a representation g (list of the 8 frame gammas, order x1..x8) *)
FEOmegaOf[g_List] := Module[{s = FESabOf[g]},
   Table[(1/2) Sum[FESpinConnLow[[mu, a, b]] s[[a, b]], {a, FEDim}, {b, FEDim}], {mu, FEDim}]];
FEGammaCoordOf[g_List] := Table[Sum[FEVielbeinInv[[mu, a]] g[[a]], {a, FEDim}], {mu, FEDim}];
(* in the primary representation (the author's T16) *)
FEOmega = FEOmegaOf[FEGammaFrame];
FEGammaCoord = FEGammaCoordOf[FEGammaFrame];
