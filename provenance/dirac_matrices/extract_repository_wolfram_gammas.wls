#!/usr/bin/env wolframscript
(* ::Package:: *)

(* extract_repository_wolfram_gammas.wls

   Loads every Wolfram package of the repository that BUILDS its own copy of the author's real
   16 x 16 Dirac matrices (instead of reading a JSON fixture) and writes the matrices it builds, so
   that build_dirac_matrices_md.py can compare them entry by entry with the matrices evaluated from
   the author's notebook.  The packages are only loaded (Get); nothing is run, nothing is written
   except the output file below.

     Revision/algebra/wolfram/RevisionAlgebra.wl       (Revision; producer of Revision/algebra/gammas.json)
     wolfram/Dirac16ComplexAlgebra.wl                  (earlier stages)
     wolfram/Dirac16ComplexGeometry.wl                 (earlier stages; also loaded by Dirac16Complex00.wl)
     wolfram/Dirac16ComplexPrimordial.wl               (earlier stages, private construction gamL)
     wolfram/Dirac16ComplexKohnSham.wl                 (earlier stages, private construction gamL)
     wolfram/Dirac16ComplexPairing.wl                  (earlier stages, private construction gamL)
     wolfram/Dirac16ComplexMatterAntimatter.wl         (earlier stages, private construction gamL)

   Rational matrices are written multiplied by 4 (S) or 2 (projectors) so every entry is an integer;
   the complex matrix B is written as its real and imaginary parts.

   Output (deterministic): provenance/dirac_matrices/repository_wolfram_gammas.json
   Usage (from the repository root):
     wolframscript -file provenance/dirac_matrices/extract_repository_wolfram_gammas.wls
*)

$yRoot = FileNameJoin[{DirectoryName[$InputFileName], "..", ".."}];
$yGet[rel_] := Module[{f = FileNameJoin[Prepend[FileNameSplit[rel], $yRoot]]},
  If[!FileExistsQ[f], Print["ERROR: package not found: ", rel]; Exit[1]];
  Get[f]; Print["loaded ", rel]];
$yInt[m_] := If[AllTrue[Flatten[{m}], IntegerQ], m, Print["ERROR: non-integer matrix"]; Exit[1]];

$yGet["Revision/algebra/wolfram/RevisionAlgebra.wl"];
$yGet["wolfram/Dirac16ComplexAlgebra.wl"];
$yGet["wolfram/Dirac16ComplexGeometry.wl"];
$yGet["wolfram/Dirac16ComplexPrimordial.wl"];
$yGet["wolfram/Dirac16ComplexKohnSham.wl"];
$yGet["wolfram/Dirac16ComplexPairing.wl"];
$yGet["wolfram/Dirac16ComplexMatterAntimatter.wl"];

$yPrivate[ctx_] := <|
  "frame" -> "notebook frame A = 0..7",
  "symbols" -> "Private`gamL, Private`C16, Private`g8, Private`Bm",
  "gamma" -> $yInt[Symbol[ctx <> "Private`gamL"]],
  "C" -> $yInt[Symbol[ctx <> "Private`C16"]],
  "chirality" -> $yInt[Symbol[ctx <> "Private`g8"]],
  "B_re" -> $yInt[Re[Symbol[ctx <> "Private`Bm"]]],
  "B_im" -> $yInt[Im[Symbol[ctx <> "Private`Bm"]]]|>;

$yOut = FileNameJoin[{DirectoryName[$InputFileName], "repository_wolfram_gammas.json"}];
Export[$yOut, <|
  "producer" -> "provenance/dirac_matrices/extract_repository_wolfram_gammas.wls",
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
  "wolfram/Dirac16ComplexMatterAntimatter.wl" -> $yPrivate["Dirac16ComplexMatterAntimatter`"]
|>, "JSON", "Compact" -> 2];
Print["wrote ", $yOut];
