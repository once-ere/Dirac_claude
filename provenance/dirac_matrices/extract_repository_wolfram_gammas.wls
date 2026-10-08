#!/usr/bin/env wolframscript
(* ::Package:: *)

(* extract_repository_wolfram_gammas.wls

   Loads every Wolfram package of the repository that BUILDS (or holds) its own copy of a real 16 x 16
   Clifford basis, instead of only reading a JSON fixture, and writes the matrices it holds, so that
   build_dirac_matrices_md.py can compare them with the matrices evaluated from the author's notebook
   (entry by entry, or, for a different basis, through an exact intertwiner).  The packages are only
   loaded (Get); no verifier is run and nothing is written except the output file below.

     Revision/field_equations_a4/wolfram/FieldEquationsA4.wl (Revision, the a4 field-equation engine;
                                                       loaded FIRST, while the Global` context is clean,
                                                       because it defines its symbols in Global`)
     Revision/algebra/wolfram/RevisionAlgebra.wl       (Revision; producer of Revision/algebra/gammas.json)
     wolfram/Dirac16ComplexAlgebra.wl                  (earlier stages; also two OTHER bases, comparison only)
     wolfram/Dirac16ComplexGeometry.wl                 (earlier stages)
     wolfram/Dirac16ComplexPrimordial.wl               (earlier stages, private construction gamL)
     wolfram/Dirac16ComplexKohnSham.wl                 (earlier stages, private construction gamL)
     wolfram/Dirac16ComplexPairing.wl                  (earlier stages, private construction gamL)
     wolfram/Dirac16ComplexMatterAntimatter.wl         (earlier stages, private construction gamL)
     wolfram/Dirac16Complex00.wl                       (earlier stages; takes its gammas from Geometry)

   For the a4 engine the file records the basis FEGammaFrame that the engine's results are built from,
   the comparison basis FEGammaFrameComparison when the engine defines one (null otherwise), and three
   exact tests that FEC, FESab, FEGammaCoord and FEOmega are built from FEGammaFrame.  Nothing about the
   engine is assumed here: the builder decides from these matrices whether they are the author's.

   Rational matrices are written multiplied by 4 (S) or 2 (projectors) so every entry is an integer;
   the complex matrix B is written as its real and imaginary parts.

   Output (deterministic, the same bytes on every operating system: UTF-8, LF line endings, no time
   stamps; $Version is recorded): provenance/dirac_matrices/repository_wolfram_gammas.json
   Usage (from the repository root):
     wolframscript -file provenance/dirac_matrices/extract_repository_wolfram_gammas.wls
*)

$yRoot = FileNameJoin[{DirectoryName[$InputFileName], "..", ".."}];
$yLoaded = {};
$yGet[rel_] := Module[{f = FileNameJoin[Prepend[FileNameSplit[rel], $yRoot]]},
  If[!FileExistsQ[f], Print["ERROR: package not found: ", rel]; Exit[1]];
  Get[f]; AppendTo[$yLoaded, rel]; Print["loaded ", rel]];
$yInt[m_] := If[AllTrue[Flatten[{m}], IntegerQ], m, Print["ERROR: non-integer matrix"]; Exit[1]];
$yIntOrNull[m_] := If[m === Null, Null, $yInt[m]];

(* ---- the a4 engine first (Global` symbols) *)
$yGet["Revision/field_equations_a4/wolfram/FieldEquationsA4.wl"];
$yFEZero[x_] := AllTrue[Flatten[{x}], TrueQ[Simplify[#] == 0] &];
$yFE = <|
  "frame" -> "coordinates x1..x8",
  "symbols" -> "FEGammaFrame, FEC, FESab, FEGammaCoord, FEOmega, FEGammaFrameComparison, FECComparison",
  "gamma" -> $yInt[FEGammaFrame],
  "C" -> $yInt[FEC],
  "C_is_gamma_x8_x1_x2_x3" -> (FEC === FEGammaFrame[[8]] . FEGammaFrame[[1]] . FEGammaFrame[[2]] . FEGammaFrame[[3]]),
  "Sab_from_gamma" -> (FESab === Table[(1/4) (FEGammaFrame[[a]] . FEGammaFrame[[b]] - FEGammaFrame[[b]] . FEGammaFrame[[a]]),
      {a, 8}, {b, 8}]),
  "GammaCoord_from_gamma" -> $yFEZero[FEGammaCoord - Table[Sum[FEVielbeinInv[[mu, a]] FEGammaFrame[[a]], {a, 8}], {mu, 8}]],
  "Omega_from_Sab" -> $yFEZero[FEOmega - Table[(1/2) Sum[FESpinConnLow[[mu, a, b]] FESab[[a, b]], {a, 8}, {b, 8}], {mu, 8}]],
  "comparison_gamma" -> $yIntOrNull[If[ValueQ[FEGammaFrameComparison], FEGammaFrameComparison, Null]],
  "comparison_C" -> $yIntOrNull[If[ValueQ[FECComparison], FECComparison, Null]]|>;

$yGet["Revision/algebra/wolfram/RevisionAlgebra.wl"];
$yGet["wolfram/Dirac16ComplexAlgebra.wl"];
$yGet["wolfram/Dirac16ComplexGeometry.wl"];
$yGet["wolfram/Dirac16ComplexPrimordial.wl"];
$yGet["wolfram/Dirac16ComplexKohnSham.wl"];
$yGet["wolfram/Dirac16ComplexPairing.wl"];
$yGet["wolfram/Dirac16ComplexMatterAntimatter.wl"];
$yGet["wolfram/Dirac16Complex00.wl"];

$yPrivate[ctx_] := <|
  "frame" -> "notebook frame A = 0..7",
  "symbols" -> "Private`gamL, Private`C16, Private`g8, Private`Bm",
  "gamma" -> $yInt[Symbol[ctx <> "Private`gamL"]],
  "C" -> $yInt[Symbol[ctx <> "Private`C16"]],
  "chirality" -> $yInt[Symbol[ctx <> "Private`g8"]],
  "B_re" -> $yInt[Re[Symbol[ctx <> "Private`Bm"]]],
  "B_im" -> $yInt[Im[Symbol[ctx <> "Private`Bm"]]]|>;

(* the same bytes on every operating system: UTF-8 JSON with LF line endings, written byte for byte *)
$yWriteJSON[file_String, data_Association] := Module[{s = ExportString[data, "JSON", "Compact" -> 2], st},
  If[!StringQ[s] || Max[ToCharacterCode[s]] > 255 || MemberQ[ToCharacterCode[s], 13],
    Print["ERROR: ExportString did not return UTF-8 bytes with LF line endings"]; Exit[1]];
  st = OpenWrite[file, BinaryFormat -> True];
  BinaryWrite[st, Append[ToCharacterCode[s], 10]];
  Close[st]];

$yOut = FileNameJoin[{DirectoryName[$InputFileName], "repository_wolfram_gammas.json"}];
$yWriteJSON[$yOut, <|
  "producer" -> "provenance/dirac_matrices/extract_repository_wolfram_gammas.wls",
  "wolfram_version" -> $Version,
  "packages_loaded" -> $yLoaded,
  "Revision/field_equations_a4/wolfram/FieldEquationsA4.wl" -> $yFE,
  "Revision/algebra/wolfram/RevisionAlgebra.wl" -> <|
    "frame" -> "coordinates x1..x8 (gamma, eta, S); notebook frame A = 0..8 (T16, tau, taubar)",
    "symbols" -> "RAEta4488, RASigma8, RATau, RATauBar, RAT16, RANotebookFrame, RAEta, RAGamma, RAC, RAChirality, RAB, RAS, RAPL, RAPR",
    "eta4488" -> $yInt[RevisionAlgebra`RAEta4488],
    "sigma8" -> $yInt[RevisionAlgebra`RASigma8],
    "tau" -> $yInt[Table[RevisionAlgebra`RATau[k], {k, 0, 7}]],
    "taubar" -> $yInt[Table[RevisionAlgebra`RATauBar[k], {k, 0, 7}]],
    "T16" -> $yInt[Table[RevisionAlgebra`RAT16[k], {k, 0, 8}]],
    "notebookFrame" -> RevisionAlgebra`RANotebookFrame,
    "eta" -> $yInt[RevisionAlgebra`RAEta],
    "gamma" -> $yInt[RevisionAlgebra`RAGamma],
    "C" -> $yInt[RevisionAlgebra`RAC],
    "Gamma" -> $yInt[RevisionAlgebra`RAChirality],
    "B_re" -> $yInt[Re[RevisionAlgebra`RAB]],
    "B_im" -> $yInt[Im[RevisionAlgebra`RAB]],
    "four_S" -> $yInt[4 RevisionAlgebra`RAS],
    "twice_PL" -> $yInt[2 RevisionAlgebra`RAPL],
    "twice_PR" -> $yInt[2 RevisionAlgebra`RAPR]|>,
  "wolfram/Dirac16ComplexAlgebra.wl" -> <|
    "frame" -> "notebook frame A = 0..7",
    "symbols" -> "D16Eta, D16Sigma8, D16Tau, D16TauBar, D16Gammas, D16C, D16Chirality, D16Spin, D16B, D16ProjMinus, D16ProjPlus",
    "eta" -> $yInt[Dirac16Complex`Algebra`D16Eta],
    "sigma8" -> $yInt[Dirac16Complex`Algebra`D16Sigma8],
    "tau" -> $yInt[Dirac16Complex`Algebra`D16Tau],
    "taubar" -> $yInt[Dirac16Complex`Algebra`D16TauBar],
    "gamma" -> $yInt[Dirac16Complex`Algebra`D16Gammas],
    "C" -> $yInt[Dirac16Complex`Algebra`D16C],
    "chirality" -> $yInt[Dirac16Complex`Algebra`D16Chirality],
    "four_S" -> $yInt[Table[4 Dirac16Complex`Algebra`D16Spin[a, b], {a, 0, 7}, {b, 0, 7}]],
    "B_re" -> $yInt[Re[Dirac16Complex`Algebra`D16B]],
    "B_im" -> $yInt[Im[Dirac16Complex`Algebra`D16B]],
    "twice_Pminus" -> $yInt[2 Dirac16Complex`Algebra`D16ProjMinus],
    "twice_Pplus" -> $yInt[2 Dirac16Complex`Algebra`D16ProjPlus]|>,
  "wolfram/Dirac16ComplexAlgebra.wl (comparison-only bases)" -> <|
    "frame" -> "frame 0..7",
    "symbols" -> "D16CliffordPictureGammas, D16KClifford (gammaHat^a K == K gamma^a), D16OctonionGammas, D16KOctonion (gamma^a K == K Gamma(e_a))",
    "clifford_gamma" -> $yInt[Dirac16Complex`Algebra`D16CliffordPictureGammas],
    "K_clifford" -> $yInt[Dirac16Complex`Algebra`D16KClifford],
    "octonion_gamma" -> $yInt[Dirac16Complex`Algebra`D16OctonionGammas],
    "K_octonion" -> $yInt[Dirac16Complex`Algebra`D16KOctonion]|>,
  "wolfram/Dirac16ComplexGeometry.wl" -> <|
    "frame" -> "notebook frame A = 0..7",
    "symbols" -> "D16GeoEta, D16GeoGammas, D16GeoC, D16GeoChirality, D16GeoSpin",
    "eta" -> $yInt[Dirac16Complex`Geometry`D16GeoEta],
    "gamma" -> $yInt[Dirac16Complex`Geometry`D16GeoGammas],
    "C" -> $yInt[Dirac16Complex`Geometry`D16GeoC],
    "chirality" -> $yInt[Dirac16Complex`Geometry`D16GeoChirality],
    "four_S" -> $yInt[4 Dirac16Complex`Geometry`D16GeoSpin]|>,
  "wolfram/Dirac16ComplexPrimordial.wl" -> $yPrivate["Dirac16ComplexPrimordial`"],
  "wolfram/Dirac16ComplexKohnSham.wl" -> $yPrivate["Dirac16ComplexKohnSham`"],
  "wolfram/Dirac16ComplexPairing.wl" -> $yPrivate["Dirac16ComplexPairing`"],
  "wolfram/Dirac16ComplexMatterAntimatter.wl" -> $yPrivate["Dirac16ComplexMatterAntimatter`"],
  "wolfram/Dirac16Complex00.wl" -> <|
    "frame" -> "notebook frame A = 0..7",
    "symbols" -> "Private`gam, Private`Cm, Private`chi8, Private`Bm",
    "gamma" -> $yInt[Dirac16Complex00`Private`gam],
    "C" -> $yInt[Dirac16Complex00`Private`Cm],
    "chirality" -> $yInt[Dirac16Complex00`Private`chi8],
    "B_re" -> $yInt[Re[Dirac16Complex00`Private`Bm]],
    "B_im" -> $yInt[Im[Dirac16Complex00`Private`Bm]]|>
|>];
Print["wrote ", $yOut];
