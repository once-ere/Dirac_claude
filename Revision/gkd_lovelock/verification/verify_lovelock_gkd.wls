#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_lovelock_gkd.wls

   Wolfram Language check that GKD (the pure-Rust function of Revision/gkd_lovelock/code/src/gkd.rs)
   is the author's generalized Kronecker delta

     k\[Delta][lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]

   (re-typed verbatim in Revision/gkd_lovelock/verification/LovelockGKDCheck.wl; delta = KroneckerDelta on coordinate
   labels), and that the Lovelock tensors P_(k)^h_j and A_(k)^{lh} (k = 1, 2, 3) of
   Revision/gkd_lovelock/results/lovelock-tensors.json are what the verbatim k\[Delta] gives with a
   curvature computed here, independently, by Mathematica.

   Steps (each one prints a time_<step>=<seconds> line; the times are NOT stored in the report,
   so that two runs give byte-identical reports):

   1. The definition.  The kernel's definition of k\[Delta] (printed in InputForm) must be the
      text re-typed below, and that text must be the one recorded in
      Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md.

   2. GKD values from the Rust crate itself.  The script writes a tiny Rust program (the source
      is the string exporterMainRs below; it calls lovelock_gkd::gkd::GKD from the UNCHANGED crate
      Revision/gkd_lovelock/code as a path dependency) into the export directory, builds it with cargo
      and runs it.  It writes binary records (signed bytes) p, lower_1..lower_p, upper_1..upper_p,
      GKD: every pair of index lists of length 1, 2, 3 over the labels 0..7 (64, 4096 and 262144
      pairs, in the order of Tuples[Range[0, 7], 2 p]) and 20000 pseudo-random pairs of each
      length 4, 5, 6, 7 (half of them permutations, where GKD is +1 or -1).  The script then calls
      the verbatim k\[Delta] on every pair and compares.  The GKD rule is NOT re-implemented in
      Wolfram Language: the values come from the compiled Rust function.

   3. The curvature of the author's metric, from scratch (LGKDCurvature), compared with
      Revision/gkd_lovelock/results/curvature.json (the Rust program's R^{ab}_{cd}).

   4. The Lovelock sums with the verbatim k\[Delta]:
        k = 1, 2: every k-tuple of the 156 nonzero R^{ab}_{cd}, every one of the 64 components
                  (9,984 and 1,557,504 calls of k\[Delta]); no shortcut;
        k = 3:    all 64 components with index lists that repeat a label in a row skipped (the
                  matrix Outer[delta, lower, upper] then has two equal rows or columns, so
                  k\[Delta] = 0), k\[Delta] called on every list that is left (1,128,960 calls);
                  and, only with LOVELOCK_GKD_K3_UNPRUNED=diagonal, the 8 diagonal components again
                  with NO skip at all (156^3 = 3,796,416 calls of k\[Delta] each).  The committed
                  report is the default run (LOVELOCK_GKD_K3_UNPRUNED=none, 29 checks; 67 s on the
                  workstation of 2026-10-01).
      No faster equivalent of k\[Delta] (Signature, permutation sign, ...) is used anywhere.

   5. Exact comparison with Revision/gkd_lovelock/results/lovelock-tensors.json, rebuilt from its exact
      monomial lists: FullSimplify[wolfram - rust] must be 0 for every component of P_(k) and of
      A_(k) (A on the domain 0 < 6 H x8 < Pi/2 where sqrt(det g) = Cos[6 H x8]); plus
      P_(1) = -4 G (the Einstein tensor from the Ricci tensor), the traces against L_(k), and the
      numbers of nonzero k\[Delta] terms against the counters of lovelock-report.json.

   Files read: Revision/gkd_lovelock/verification/LovelockGKDCheck.wl, Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md,
   Revision/gkd_lovelock/results/curvature.json, Revision/gkd_lovelock/results/lovelock-tensors.json,
   Revision/gkd_lovelock/results/lovelock-report.json, Revision/gkd_lovelock/code (compiled by cargo), and the
   exporter's own output.  NOT read: any Mathematica notebook (.nb file) of the author, the file
   Generalized_Kronecker_Delta.txt, or any other file with the author's answers.

   Output: the JSON report and the lines
     check_<name>=true|false, check_count=N, failed_check_count=K, report=<path>
   Exit status 1 if a check failed or the number of checks is not the expected one, 2 on a
   load, build or IO error.

   Usage (from the repository root; the report path is a plain positional argument):
     wolframscript -file Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls Revision/gkd_lovelock/results/wolfram-gkd-report.json

   Do NOT put "--" before the path: WolframScript 1.14 drops "--" and every argument after it.
   Environment: LOVELOCK_GKD_WOLFRAM_REPORT (report path if no argument is given),
   LOVELOCK_GKD_EXPORT_DIR (where the exporter crate is written and built; default
   Revision/gkd_lovelock/code/target/wolfram_gkd_export, git-ignored), LOVELOCK_GKD_K3_UNPRUNED (none (default) or diagonal; the committed report is the default run).
   Requires cargo (Rust >= 1.87) on PATH.

   The JSON text is produced by ExportString[..., "RawJSON"] with "\r\n" -> "\n" and "\/" -> "/",
   and written as UTF-8 bytes with a trailing newline.

   License: GPL-3.0-or-later. *)

scriptPath = ExpandFileName[$InputFileName];
scriptDirectory = DirectoryName[scriptPath];
gkdDirectory = ParentDirectory[scriptDirectory];  (* Revision/gkd_lovelock *)
repositoryRoot = ParentDirectory[ParentDirectory[gkdDirectory]];
arguments = Select[Rest[$ScriptCommandLine], # =!= "--" &];
nonEmptyString[value_] := StringQ[value] && value =!= "";
defaultReportPath = FileNameJoin[{gkdDirectory, "results", "wolfram-gkd-report.json"}];
reportPath = ExpandFileName[Which[
  Length[arguments] >= 1, arguments[[1]],
  nonEmptyString[Environment["LOVELOCK_GKD_WOLFRAM_REPORT"]], Environment["LOVELOCK_GKD_WOLFRAM_REPORT"],
  True, defaultReportPath
]];
exportDirectory = ExpandFileName[If[nonEmptyString[Environment["LOVELOCK_GKD_EXPORT_DIR"]],
  Environment["LOVELOCK_GKD_EXPORT_DIR"], FileNameJoin[{gkdDirectory, "code", "target", "wolfram_gkd_export"}]]];
k3UnprunedSetting = If[nonEmptyString[Environment["LOVELOCK_GKD_K3_UNPRUNED"]], ToLowerCase[Environment["LOVELOCK_GKD_K3_UNPRUNED"]], "none"];
If[! MemberQ[{"diagonal", "none"}, k3UnprunedSetting], Print["ERROR: LOVELOCK_GKD_K3_UNPRUNED must be diagonal or none"]; Exit[2]];

packagePath = FileNameJoin[{scriptDirectory, "LovelockGKDCheck.wl"}];
If[! FileExistsQ[packagePath], Print["ERROR: missing package ", packagePath]; Exit[2]];
Check[Get[packagePath], Print["ERROR: package load produced messages: ", packagePath]; Exit[2]];

artifactDirectory = FileNameJoin[{gkdDirectory, "results"}];
provenancePath = FileNameJoin[{artifactDirectory, "PROVENANCE_OF_THE_COMPUTATION.md"}];
curvaturePath = FileNameJoin[{artifactDirectory, "curvature.json"}];
tensorsPath = FileNameJoin[{artifactDirectory, "lovelock-tensors.json"}];
rustReportPath = FileNameJoin[{artifactDirectory, "lovelock-report.json"}];
crateDirectory = FileNameJoin[{gkdDirectory, "code"}];
crateSources = Join[{FileNameJoin[{crateDirectory, "Cargo.toml"}]},
  FileNameJoin[{crateDirectory, "src", #}] & /@ {"geometry.rs", "gkd.rs", "lib.rs", "lovelock.rs", "main.rs", "output.rs", "poly.rs", "rational.rs"}];
Scan[If[! FileExistsQ[#], Print["ERROR: missing input ", #]; Exit[2]] &, Join[{provenancePath, curvaturePath, tensorsPath, rustReportPath}, crateSources]];

expectedCheckCount = If[k3UnprunedSetting === "diagonal", 30, 29];

relativePath[path_String] := Module[{rootText = StringReplace[repositoryRoot, "\\" -> "/"], pathText = StringReplace[path, "\\" -> "/"]},
  If[StringStartsQ[pathText, rootText <> "/", IgnoreCase -> True], StringDrop[pathText, StringLength[rootText] + 1], pathText]
];
sha256[path_String] := ToLowerCase[FileHash[path, "SHA256", All, "HexString"]];
sha256String[text_String] := ToLowerCase[Hash[ByteArray[ToCharacterCode[text, "UTF-8"]], "SHA256", "HexString"]];
readUTF8[path_String] := FromCharacterCode[BinaryReadList[path, "Byte"], "UTF-8"];
(* ExportString[..., "RawJSON"] returns the UTF-8 BYTES of the JSON text as a string of
   character codes 0..255; jsonBytes keeps them as bytes (no second UTF-8 encoding). *)
jsonBytes[expr_] := Module[{s = ExportString[expr, "RawJSON"]},
  If[! StringQ[s] || Max[ToCharacterCode[s]] > 255, Print["ERROR: JSON export failed"]; Exit[2]];
  s = StringReplace[s, {"\r\n" -> "\n", "\\/" -> "/"}];
  If[! StringEndsQ[s, "\n"], s = s <> "\n"];
  ToCharacterCode[s]
];
writeBytes[path_String, codes_List] := Module[{stream},
  If[! DirectoryQ[DirectoryName[path]], CreateDirectory[DirectoryName[path], CreateIntermediateDirectories -> True]];
  stream = OpenWrite[path, BinaryFormat -> True];
  BinaryWrite[stream, codes, "Byte"];
  Close[stream];
];
writeUTF8[path_String, text_String] := writeBytes[path, ToCharacterCode[text, "UTF-8"]];
writeIfChanged[path_String, text_String] := If[! FileExistsQ[path] || readUTF8[path] =!= text, writeUTF8[path, text]];
readJSON[path_String] := Module[{v = Quiet[ImportByteArray[ByteArray[BinaryReadList[path, "Byte"]], "RawJSON"]]},
  If[! AssociationQ[v], Print["ERROR: cannot read JSON ", path]; Exit[2]]; v];

secondsText[t_] := ToString[NumberForm[N[Round[10 t]/10], {9, 1}, NumberPadding -> {"", "0"}]];
stepStart = AbsoluteTime[];
step[name_String] := Module[{now = AbsoluteTime[]},
  Print["time_", name, "=", secondsText[now - stepStart]];
  stepStart = now;
];
runStart = AbsoluteTime[];

checks = <||>;
details = <||>;
addCheck[name_String, passed_, detail_String] := (checks[name] = TrueQ[passed]; details[name] = detail);
measurements = <||>;

coordinateNames = {"x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"};
labelOf[s_String] := First[FirstPosition[coordinateNames, s]];
deltaChar = FromCharacterCode[948];

(* ============================================================================================ *)
(* 1. The definition                                                                            *)
(* ============================================================================================ *)

authorDefinitionText = "k" <> deltaChar <> "[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]";
kernelDefinitionText = LGKDDefinitionText[];
provenanceText = readUTF8[provenancePath];
addCheck["definition_is_the_authors_verbatim",
  kernelDefinitionText === authorDefinitionText && StringContainsQ[provenanceText, "`" <> authorDefinitionText <> "`"],
  "the kernel's definition of k" <> deltaChar <> ", printed in InputForm, is exactly " <> authorDefinitionText <>
    ", the text recorded in PROVENANCE_OF_THE_COMPUTATION.md (from the author's In[54]); delta[a_Integer, b_Integer] := KroneckerDelta[a, b]"];
unequal = k\[Delta][{0}, {0, 1}];
addCheck["definition_unequal_lengths_stay_unevaluated",
  MatchQ[unequal, HoldPattern[k\[Delta][{0}, {0, 1}]]] && k\[Delta][{0, 1}, {1, 0}] === -1 && k\[Delta][{0, 1, 2}, {1, 2, 0}] === 1,
  "k" <> deltaChar <> "[{0}, {0, 1}] stays unevaluated (the condition Length[lower] == Length[upper] fails; GKD refuses unequal lengths); k" <>
    deltaChar <> "[{0, 1}, {1, 0}] = -1, k" <> deltaChar <> "[{0, 1, 2}, {1, 2, 0}] = +1"];
step["definition"];

(* ============================================================================================ *)
(* 2. GKD values from the Rust crate, compared with the verbatim k\[Delta]                      *)
(* ============================================================================================ *)

(* The exporter's source: no string literal, no backslash, so it can live in this string as is. *)
exporterMainRs = StringRiffle[{
"//! lovelock_gkd_export: GKD values for the Wolfram check Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls.",
"//! Calls lovelock_gkd::gkd::GKD (the crate Revision/gkd_lovelock/code, unchanged, as a path",
"//! dependency) and writes binary records of signed bytes:",
"//!     p, lower_1 .. lower_p, upper_1 .. upper_p, GKD(lower, upper)",
"//! labels 0..7.  Section 1: p = 1, 2, 3, every pair of index lists, in the order of the",
"//! Wolfram Language Tuples[Range[0, 7], 2 p] (the first p entries are lower, the last p",
"//! upper).  Section 2: p = 4, 5, 6, 7, 20000 pseudo-random pairs each (xorshift64*,",
"//! seed 0x243F6A8885A308D3 XOR p): even samples have p distinct upper labels and a",
"//! random permutation of them as lower labels, odd samples two arbitrary lists.",
"use lovelock_gkd::gkd::GKD;",
"",
"struct Rng(u64);",
"",
"impl Rng {",
"    fn next(&mut self) -> u64 {",
"        let mut x = self.0;",
"        x ^= x >> 12;",
"        x ^= x << 25;",
"        x ^= x >> 27;",
"        self.0 = x;",
"        x.wrapping_mul(0x2545F4914F6CDD1D)",
"    }",
"    fn below(&mut self, n: usize) -> usize {",
"        (self.next() % n as u64) as usize",
"    }",
"}",
"",
"fn record(out: &mut Vec<u8>, lower: &[usize], upper: &[usize]) {",
"    out.push(lower.len() as u8);",
"    for &x in lower {",
"        out.push(x as u8);",
"    }",
"    for &x in upper {",
"        out.push(x as u8);",
"    }",
"    out.push(GKD(lower, upper) as i8 as u8);",
"}",
"",
"fn main() {",
"    let path = std::env::args().nth(1).unwrap();",
"    let mut out: Vec<u8> = Vec::new();",
"    for p in 1..=3usize {",
"        let total = 8usize.pow(2 * p as u32);",
"        let mut digits = vec![0usize; 2 * p];",
"        for code in 0..total {",
"            let mut c = code;",
"            for i in (0..2 * p).rev() {",
"                digits[i] = c % 8;",
"                c /= 8;",
"            }",
"            record(&mut out, &digits[..p], &digits[p..]);",
"        }",
"    }",
"    for p in 4..=7usize {",
"        let mut rng = Rng(0x243F6A8885A308D3 ^ p as u64);",
"        for s in 0..20000usize {",
"            if s % 2 == 0 {",
"                let mut labels: Vec<usize> = (0..8).collect();",
"                for i in 0..p {",
"                    let j = i + rng.below(8 - i);",
"                    labels.swap(i, j);",
"                }",
"                let upper: Vec<usize> = labels[..p].to_vec();",
"                let mut lower = upper.clone();",
"                for i in (1..p).rev() {",
"                    let j = rng.below(i + 1);",
"                    lower.swap(i, j);",
"                }",
"                record(&mut out, &lower, &upper);",
"            } else {",
"                let upper: Vec<usize> = (0..p).map(|_| rng.below(8)).collect();",
"                let lower: Vec<usize> = (0..p).map(|_| rng.below(8)).collect();",
"                record(&mut out, &lower, &upper);",
"            }",
"        }",
"    }",
"    std::fs::write(path, out).unwrap();",
"}",
""}, "\n"];

exporterCargoToml = StringRiffle[{
"[package]",
"name = \"lovelock_gkd_export\"",
"version = \"0.1.0\"",
"edition = \"2021\"",
"publish = false",
"",
"# Own, empty workspace: built on its own, outside any other workspace.",
"[workspace]",
"",
"[dependencies]",
"lovelock_gkd = { path = \"" <> StringReplace[crateDirectory, "\\" -> "/"] <> "\" }",
"",
"[profile.release]",
"opt-level = 3",
"debug = false",
""}, "\n"];

writeIfChanged[FileNameJoin[{exportDirectory, "Cargo.toml"}], exporterCargoToml];
writeIfChanged[FileNameJoin[{exportDirectory, "src", "main.rs"}], exporterMainRs];
build = RunProcess[{"cargo", "build", "--release", "--quiet", "--manifest-path", FileNameJoin[{exportDirectory, "Cargo.toml"}]}];
If[! AssociationQ[build] || build["ExitCode"] =!= 0,
  Print["ERROR: cargo build of the GKD exporter failed"]; If[AssociationQ[build], Print[build["StandardError"]]]; Exit[2]];
exporterBinary = FileNameJoin[{exportDirectory, "target", "release", "lovelock_gkd_export" <> If[$OperatingSystem === "Windows", ".exe", ""]}];
valuesPath = FileNameJoin[{exportDirectory, "gkd-values.bin"}];
If[FileExistsQ[valuesPath], DeleteFile[valuesPath]];
run = RunProcess[{exporterBinary, valuesPath}];
If[! AssociationQ[run] || run["ExitCode"] =!= 0 || ! FileExistsQ[valuesPath],
  Print["ERROR: the GKD exporter failed"]; If[AssociationQ[run], Print[run["StandardError"]]]; Exit[2]];
step["build_and_run_gkd_exporter"];

(* parse the records: p, lower (p), upper (p), GKD *)
bytes = BinaryReadList[valuesPath, "Integer8"];
records = Module[{pos = 1, len = Length[bytes], p},
  Reap[While[pos <= len,
    p = bytes[[pos]];
    If[! (1 <= p <= 7) || pos + 2 p + 1 > len, Print["ERROR: malformed GKD record at byte ", pos]; Exit[2]];
    Sow[{bytes[[pos + 1 ;; pos + p]], bytes[[pos + p + 1 ;; pos + 2 p]], bytes[[pos + 2 p + 1]]}, p];
    pos += 2 p + 2
  ], Range[7]][[2]]
];
records = If[# === {}, {}, First[#]] & /@ records;  (* records[[p]] = list of {lower, upper, gkd} *)
layoutOK = Length /@ records === {64, 4096, 262144, 20000, 20000, 20000, 20000} &&
  And @@ Table[Join[#[[1]], #[[2]]] & /@ records[[p]] === Tuples[Range[0, 7], 2 p], {p, 3}];
addCheck["gkd_values_file_layout", layoutOK,
  "the exporter wrote 64, 4096, 262144 pairs of lengths 1, 2, 3 (every pair, in the order of Tuples[Range[0, 7], 2 p]) and 20000 pairs of each length 4..7; " <>
    ToString[Length[bytes]] <> " bytes"];
step["read_gkd_values"];

gkdComparison = Table[
  Module[{rs = records[[p]], kd, gkd, mismatches, nonInteger},
    kd = k\[Delta][#[[1]], #[[2]]] & /@ rs;
    gkd = rs[[All, 3]];
    nonInteger = Count[kd, x_ /; ! MemberQ[{-1, 0, 1}, x]];
    mismatches = Count[MapThread[SameQ, {kd, gkd}], False];
    Join[
      <|"p" -> p, "pairs" -> Length[rs], "mismatches" -> mismatches, "valuesOutsideMinus1To1" -> nonInteger,
        "plusOne" -> Count[gkd, 1], "minusOne" -> Count[gkd, -1], "zero" -> Count[gkd, 0],
        (* negative control: the same comparison against -GKD must fail exactly where GKD is nonzero *)
        "mismatchesAgainstMinusGKD" -> Count[MapThread[SameQ, {kd, -gkd}], False]|>,
      If[p >= 4, <|"permutationSamplesNonzero" -> Count[gkd[[1 ;; ;; 2]], 1 | -1]|>, <||>]]
  ], {p, 7}];
Do[
  With[{c = gkdComparison[[p]]},
    addCheck["gkd_equals_kdelta_exhaustive_length_" <> ToString[p], c["mismatches"] === 0 && c["valuesOutsideMinus1To1"] === 0,
      "all " <> ToString[c["pairs"]] <> " pairs of index lists of length " <> ToString[p] <> " over the labels 0..7: verbatim k" <> deltaChar <>
        " = GKD for every pair (" <> ToString[c["mismatches"]] <> " mismatches; +1: " <> ToString[c["plusOne"]] <> ", -1: " <>
        ToString[c["minusOne"]] <> ", 0: " <> ToString[c["zero"]] <> ")"]
  ], {p, 3}];
Do[
  With[{c = gkdComparison[[p]]},
    addCheck["gkd_equals_kdelta_random_length_" <> ToString[p],
      c["mismatches"] === 0 && c["valuesOutsideMinus1To1"] === 0 && c["permutationSamplesNonzero"] === 10000,
      ToString[c["pairs"]] <> " pseudo-random pairs of length " <> ToString[p] <> " (xorshift64*, seed 0x243F6A8885A308D3 XOR " <> ToString[p] <>
        "; the 10000 even samples are permutations, all with GKD = +1 or -1): verbatim k" <> deltaChar <> " = GKD for every pair (" <>
        ToString[c["mismatches"]] <> " mismatches; +1: " <> ToString[c["plusOne"]] <> ", -1: " <> ToString[c["minusOne"]] <> ", 0: " <>
        ToString[c["zero"]] <> ")"]
  ], {p, 4, 7}];
addCheck["negative_control_gkd_comparison_detects_a_sign_flip",
  And @@ ((#["mismatchesAgainstMinusGKD"] === #["plusOne"] + #["minusOne"] && #["plusOne"] + #["minusOne"] > 0) & /@ gkdComparison),
  "negative control: compared with -GKD instead of GKD, the same test reports a mismatch at exactly every pair where GKD is nonzero (" <>
    StringRiffle[("length " <> ToString[#["p"]] <> ": " <> ToString[#["mismatchesAgainstMinusGKD"]]) & /@ gkdComparison, ", "] <>
    "), so the comparison can fail"];
measurements["gkdComparison"] = KeyDrop[#, {"valuesOutsideMinus1To1"}] & /@ gkdComparison;
step["compare_gkd_with_kdelta"];

(* ============================================================================================ *)
(* 3. Curvature from scratch, compared with the Rust curvature                                  *)
(* ============================================================================================ *)

curvature = LGKDCurvature[];
entries = curvature["nonzeroMixed"];
entryValues = entries[[All, 2]];
gInverse = curvature["inverseMetric"];
sqrtG = curvature["sqrtDetG"];
rustCurvature = readJSON[curvaturePath];
rustRiemann = rustCurvature["riemannMixedNonzero"];
rustRiemannIndex = ({labelOf[#["up"][[1]]], labelOf[#["up"][[2]]], labelOf[#["down"][[1]]], labelOf[#["down"][[2]]]} & /@ rustRiemann);
riemannMatch = Length[entries] === 156 && entries[[All, 1]] === rustRiemannIndex &&
  And @@ MapThread[Simplify[#1 - ToExpression[#2]] === 0 &, {entryValues, #["value"] & /@ rustRiemann}];
addCheck["riemann_mixed_equals_rust_curvature", riemannMatch,
  "R^ab_cd computed here (Christoffel and Riemann from the metric with D, Inverse, Simplify; MTW convention) has " <> ToString[Length[entries]] <>
    " nonzero entries, the same index lists and exactly the same values as riemannMixedNonzero of curvature.json"];
addCheck["sqrt_det_g_is_cos", Simplify[sqrtG - Cos[6 H x8]] === 0 && Simplify[Det[curvature["metric"]] - Cos[6 H x8]^2] === 0,
  "det g = Cos[6 H x8]^2 and sqrt(det g) = Cos[6 H x8] on 0 < 6 H x8 < Pi/2 (the Rust program's S^3 C = Sin Cot)"];
step["curvature"];

(* ============================================================================================ *)
(* 4. The Lovelock sums with the verbatim k\[Delta]                                             *)
(* ============================================================================================ *)

components = Tuples[Range[8], 2];  (* {h, j} *)
diagonal = Table[{a, a}, {a, 8}];
lovelockRuns = <||>;
pMatrix = <||>;
runSums[k_, mode_, comps_] := Module[{res},
  res = Association[Map[# -> If[mode === "unpruned", LGKDLovelockUnpruned[k, entries, #], LGKDLovelockPruned[k, entries, #]] &, comps]];
  <|"results" -> res,
    "values" -> Association[KeyValueMap[#1 -> Simplify[LGKDCombine[#2["terms"], entryValues]] &, res]],
    "kDeltaCalls" -> Total[#["kDeltaCalls"] & /@ Values[res]],
    "nonzeroCalls" -> Total[#["nonzeroCalls"] & /@ Values[res]],
    "nonIntegerCalls" -> Total[#["nonIntegerCalls"] & /@ Values[res]]|>
];
lovelockRuns[{1, "unpruned"}] = runSums[1, "unpruned", components]; step["lovelock_k1_unpruned_64_components"];
lovelockRuns[{2, "unpruned"}] = runSums[2, "unpruned", components]; step["lovelock_k2_unpruned_64_components"];
lovelockRuns[{3, "pruned"}] = runSums[3, "pruned", components]; step["lovelock_k3_skip_repeated_64_components"];
If[k3UnprunedSetting === "diagonal",
  Module[{res = <||>, vals = <||>},
    Do[
      Module[{r = runSums[3, "unpruned", {c}]},
        res[c] = r["results"][c];
        vals[c] = r["values"][c]
      ];
      step["lovelock_k3_unpruned_component_x" <> ToString[c[[1]]] <> "_x" <> ToString[c[[2]]]],
      {c, diagonal}];
    lovelockRuns[{3, "unpruned"}] = <|"results" -> res, "values" -> vals,
      "kDeltaCalls" -> Total[#["kDeltaCalls"] & /@ Values[res]],
      "nonzeroCalls" -> Total[#["nonzeroCalls"] & /@ Values[res]],
      "nonIntegerCalls" -> Total[#["nonIntegerCalls"] & /@ Values[res]]|>
  ]
];
pMatrix[1] = Table[lovelockRuns[{1, "unpruned"}]["values"][{h, j}], {h, 8}, {j, 8}];
pMatrix[2] = Table[lovelockRuns[{2, "unpruned"}]["values"][{h, j}], {h, 8}, {j, 8}];
pMatrix[3] = Table[lovelockRuns[{3, "pruned"}]["values"][{h, j}], {h, 8}, {j, 8}];
(* A_(k)^{lh} = sqrt(g) g^{jl} P_(k)^h_j *)
aMatrix = Association[Table[k -> Table[Simplify[sqrtG Sum[gInverse[[j, l]] pMatrix[k][[h, j]], {j, 8}], LGKDDomainAssumption], {l, 8}, {h, 8}], {k, 3}]];

nonIntegerTotal = Total[#["nonIntegerCalls"] & /@ Values[lovelockRuns]];
addCheck["lovelock_kdelta_values_are_integers", nonIntegerTotal === 0,
  "every call of the verbatim k" <> deltaChar <> " in the Lovelock sums returned an integer (" <> ToString[nonIntegerTotal] <> " non-integer values)"];

(* ============================================================================================ *)
(* 5. Exact comparison with the Rust results                                                    *)
(* ============================================================================================ *)

tensors = readJSON[tensorsPath];
rustReport = readJSON[rustReportPath];
key[r_, c_] := coordinateNames[[r]] <> "," <> coordinateNames[[c]];
rustP[k_] := Table[LGKDFromMonomials[tensors["P" <> ToString[k] <> "_mixed_up_h_down_j"][key[h, j]]["monomials"]], {h, 8}, {j, 8}];
rustA[k_] := Table[LGKDFromMonomials[tensors["A" <> ToString[k] <> "_contravariant_l_h"][key[l, h]]["monomials"]], {l, 8}, {h, 8}];
mismatchList[mine_, rust_, assumption_] := Select[Tuples[Range[8], 2],
  FullSimplify[mine[[#[[1]], #[[2]]]] - rust[[#[[1]], #[[2]]]], assumption] =!= 0 &];
nonzeroComponents[m_] := Select[Tuples[Range[8], 2], m[[#[[1]], #[[2]]]] =!= 0 &];
compText[list_] := StringRiffle[key @@@ list, "; "];

modeText = <|1 -> "every 1-tuple of nonzero R entries, no skip, 9984 calls of k" <> deltaChar,
  2 -> "every 2-tuple of nonzero R entries, no skip, 1557504 calls of k" <> deltaChar,
  3 -> "lists repeating a label in a row skipped, k" <> deltaChar <> " on every remaining list, " <>
    ToString[lovelockRuns[{3, "pruned"}]["kDeltaCalls"]] <> " calls"|>;
Do[
  Module[{rp = rustP[k], ra = rustA[k], badP, badA, nz},
    badP = mismatchList[pMatrix[k], rp, True];
    badA = mismatchList[aMatrix[k], ra, LGKDDomainAssumption];
    nz = nonzeroComponents[pMatrix[k]];
    addCheck["k" <> ToString[k] <> "_P_equals_rust_all_64_components", badP === {},
      "P_(" <> ToString[k] <> ")^h_j from the verbatim k" <> deltaChar <> " (" <> modeText[k] <> ") minus the Rust P_(" <> ToString[k] <>
        ") rebuilt from its monomials: FullSimplify gives 0 for all 64 components; nonzero components: " <> compText[nz] <>
        If[badP === {}, "", "; MISMATCH at " <> compText[badP]]];
    addCheck["k" <> ToString[k] <> "_A_equals_rust_all_64_components", badA === {},
      "A_(" <> ToString[k] <> ")^lh = sqrt(g) g^jl P_(" <> ToString[k] <> ")^h_j minus the Rust A_(" <> ToString[k] <>
        ") rebuilt from its monomials: FullSimplify on 0 < 6 H x8 < Pi/2 gives 0 for all 64 components" <>
        If[badA === {}, "", "; MISMATCH at " <> compText[badA]]];
    measurements["k" <> ToString[k] <> "NonzeroComponents"] = key @@@ nz;
  ], {k, 3}];
(* negative control: the same test must flag a change of one P component and of one A component *)
Module[{rp = rustP[2], ra = rustA[3], badP, badA},
  rp[[3, 3]] = rp[[3, 3]] + H^4/1000;
  ra[[8, 8]] = ra[[8, 8]] (1 + 1/1000);
  badP = mismatchList[pMatrix[2], rp, True];
  badA = mismatchList[aMatrix[3], ra, LGKDDomainAssumption];
  addCheck["negative_control_tensor_comparison_detects_a_change", badP === {{3, 3}} && badA === {{8, 8}},
    "negative control: after adding H^4/1000 to the Rust P_(2) x3,x3 and multiplying the Rust A_(3) x8,x8 by 1001/1000, the same FullSimplify test flags exactly " <>
      compText[badP] <> " (P_(2)) and " <> compText[badA] <> " (A_(3)), so the comparison can fail"]
];
step["compare_with_rust_tensors"];

If[k3UnprunedSetting === "diagonal",
  Module[{bad},
    bad = Select[diagonal, Simplify[lovelockRuns[{3, "unpruned"}]["values"][#] - lovelockRuns[{3, "pruned"}]["values"][#]] =!= 0 ||
        lovelockRuns[{3, "unpruned"}]["results"][#]["nonzeroCalls"] =!= lovelockRuns[{3, "pruned"}]["results"][#]["nonzeroCalls"] &];
    addCheck["k3_diagonal_unpruned_equals_skip_sum", bad === {},
      "for the 8 diagonal components x1,x1 .. x8,x8 the literal sum over every 3-tuple of the 156 nonzero R entries (156^3 = 3796416 calls of k" <>
        deltaChar <> " per component, " <> ToString[lovelockRuns[{3, "unpruned"}]["kDeltaCalls"]] <>
        " in all, no skip) gives exactly the same P_(3) and the same number of nonzero k" <> deltaChar <> " terms (" <>
        ToString[lovelockRuns[{3, "unpruned"}]["nonzeroCalls"]] <> ") as the sum with the repeated-label skip" <>
        If[bad === {}, "", "; MISMATCH at " <> compText[bad]]]
  ]
];

einstein = curvature["einsteinMixed"];
addCheck["k1_equals_minus_4_einstein", And @@ Flatten[Table[Simplify[pMatrix[1][[h, j]] + 4 einstein[[h, j]]] === 0, {h, 8}, {j, 8}]],
  "P_(1)^h_j = -4 G^h_j exactly, G^h_j = R^h_j - 1/2 delta^h_j R from the Ricci tensor computed here (an independent route)"];
Do[
  Module[{lRust = ToExpression[tensors["L" <> ToString[k]]], trace = Sum[pMatrix[k][[a, a]], {a, 8}]},
    addCheck["k" <> ToString[k] <> "_trace_equals_" <> ToString[8 - 2 k] <> "_L" <> ToString[k], Simplify[trace - (8 - 2 k) lRust] === 0,
      "sum_h P_(" <> ToString[k] <> ")^h_h computed here = (8 - " <> ToString[2 k] <> ") L_(" <> ToString[k] <> ") with L_(" <> ToString[k] <>
        ") = " <> tensors["L" <> ToString[k]] <> " of lovelock-tensors.json"]
  ], {k, 3}];

rustCounters = Association[#["k"] -> # & /@ rustReport["counters"]];
countersOK = <|
  1 -> lovelockRuns[{1, "unpruned"}]["nonzeroCalls"] === rustCounters[1]["gkdNonzero"] && lovelockRuns[{1, "unpruned"}]["kDeltaCalls"] === 64 156,
  2 -> lovelockRuns[{2, "unpruned"}]["nonzeroCalls"] === rustCounters[2]["gkdNonzero"] && lovelockRuns[{2, "unpruned"}]["kDeltaCalls"] === 64 156^2,
  3 -> lovelockRuns[{3, "pruned"}]["nonzeroCalls"] === rustCounters[3]["gkdNonzero"] && lovelockRuns[{3, "pruned"}]["kDeltaCalls"] === rustCounters[3]["leaves"]|>;
Do[
  addCheck["k" <> ToString[k] <> "_nonzero_kdelta_terms_equal_rust_counter", countersOK[k],
    "number of nonzero k" <> deltaChar <> " terms here: " <> ToString[lovelockRuns[{k, If[k == 3, "pruned", "unpruned"]}]["nonzeroCalls"]] <>
      "; Rust gkdNonzero: " <> ToString[rustCounters[k]["gkdNonzero"]] <> "; calls of k" <> deltaChar <> " here: " <>
      ToString[lovelockRuns[{k, If[k == 3, "pruned", "unpruned"]}]["kDeltaCalls"]] <>
      If[k == 3, " = the Rust leaves counter " <> ToString[rustCounters[3]["leaves"]] <> " (the same skip rule)", " = 64 * 156^" <> ToString[k]]],
  {k, 3}];

Module[{bad = {}},
  Do[
    Do[
      With[{entry = tensors[name][key[r, c]]},
        If[Simplify[ToExpression[entry["mathematica"]] - LGKDFromMonomials[entry["monomials"]], LGKDDomainAssumption] =!= 0,
          AppendTo[bad, name <> " " <> key[r, c]]]],
      {r, 8}, {c, 8}],
    {name, Flatten[Table[{"P" <> ToString[k] <> "_mixed_up_h_down_j", "A" <> ToString[k] <> "_contravariant_l_h"}, {k, 3}]]}];
  addCheck["rust_json_text_equals_its_monomials", bad === {},
    "in lovelock-tensors.json the Mathematica text of every component of P_(k) and A_(k) (k = 1, 2, 3; 384 components) equals the expression rebuilt from its exact monomial list" <>
      If[bad === {}, "", "; MISMATCH at " <> StringRiffle[bad, "; "]]]
];
step["identities_and_counters"];

(* the nonzero components as computed here, for the record *)
measurements["wolframComponents"] = Association[Table[
  ("P" <> ToString[k] <> "_mixed_up_h_down_j") -> Association[(key @@ # -> ToString[Expand[pMatrix[k][[#[[1]], #[[2]]]]], InputForm]) & /@ diagonal],
  {k, 3}]];
measurements["lovelockKDeltaCalls"] = Association[KeyValueMap[
  (ToString[#1[[1]]] <> "_" <> #1[[2]]) -> <|"kDeltaCalls" -> #2["kDeltaCalls"], "nonzeroTerms" -> #2["nonzeroCalls"],
    "components" -> Length[#2["results"]]|> &, lovelockRuns]];

(* ============================================================================================ *)
(* 6. The report                                                                                *)
(* ============================================================================================ *)

failed = Keys[Select[checks, ! TrueQ[#] &]];
If[Length[checks] =!= expectedCheckCount, AppendTo[failed, "expectedCheckCount"]];
report = <|
  "schemaVersion" -> 1,
  "producer" -> "Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls with Revision/gkd_lovelock/verification/LovelockGKDCheck.wl (context LovelockGKDCheck`), Wolfram Language " <> First[StringSplit[$Version]],
  "task" -> "Wolfram check that GKD (Revision/gkd_lovelock/code/src/gkd.rs) is the author's k" <> deltaChar <>
    ", and exact recomputation of the Lovelock tensors P_(k), A_(k), k = 1, 2, 3, of (4.38) for the author's 8D test metric with the verbatim k" <> deltaChar,
  "authorDefinition" -> authorDefinitionText,
  "deltaOnCoordinateLabels" -> "delta[a_Integer, b_Integer] := KroneckerDelta[a, b]",
  "gkdValuesSource" -> <|
    "how" -> "values computed by the compiled Rust function lovelock_gkd::gkd::GKD (crate Revision/gkd_lovelock/code, unchanged, as a path dependency) through the exporter whose source is embedded in this script (exporterMainRs), built with cargo in the export directory ($LOVELOCK_GKD_EXPORT_DIR, default Revision/gkd_lovelock/code/target/wolfram_gkd_export); the GKD rule is not re-implemented in Wolfram Language",
    "exporterMainRsSha256" -> sha256String[exporterMainRs],
    "valuesFile" -> "gkd-values.bin",
    "valuesFileBytes" -> Length[bytes],
    "valuesFileSha256" -> sha256[valuesPath],
    "recordLayout" -> "signed bytes: p, lower_1..lower_p, upper_1..upper_p, GKD(lower, upper); labels 0..7"|>,
  "verbatimKDeltaUse" -> Join[{
    "GKD comparison: the verbatim k" <> deltaChar <> " is called on every one of the 346304 pairs",
    "k = 1: every 1-tuple of the 156 nonzero R^ab_cd for each of the 64 components (9984 calls), no skip",
    "k = 2: every 2-tuple of the 156 nonzero R^ab_cd for each of the 64 components (1557504 calls), no skip",
    "k = 3, all 64 components: an R entry whose upper (lower) index pair repeats a label already in the lower (upper) row of k" <> deltaChar <>
      " is skipped (two equal rows or columns of Outer[delta, lower, upper], so the determinant is 0); the verbatim k" <> deltaChar <>
      " is called on every one of the " <> ToString[lovelockRuns[{3, "pruned"}]["kDeltaCalls"]] <> " index lists that are left"},
    If[k3UnprunedSetting === "diagonal",
      {"k = 3, the 8 diagonal components again: every 3-tuple of the 156 nonzero R^ab_cd (" <> ToString[lovelockRuns[{3, "unpruned"}]["kDeltaCalls"]] <>
        " calls), no skip"}, {}],
    {"no faster equivalent of k" <> deltaChar <> " (Signature, permutation sign, Levi-Civita product) is used anywhere"}],
  "notRead" -> "no Mathematica notebook (.nb file) of the author, not Generalized_Kronecker_Delta.txt, no other file with the author's answers; the definition of k" <>
    deltaChar <> " is re-typed from PROVENANCE_OF_THE_COMPUTATION.md, the metric from the task",
  "timesNote" -> "run times are printed on standard output (time_<step>=<seconds>), not stored here, so that two runs give byte-identical reports",
  "checks" -> KeyValueMap[<|"name" -> #1, "verdict" -> If[TrueQ[#2], "PASS", "FAIL"], "detail" -> details[#1]|> &, checks],
  "measurements" -> measurements,
  "inputSha256" -> Association[(relativePath[#] -> sha256[#]) & /@ Join[{provenancePath, curvaturePath, tensorsPath, rustReportPath}, crateSources]],
  "sourceSha256" -> Association[(relativePath[#] -> sha256[#]) & /@ {packagePath, scriptPath}],
  "checkCount" -> Length[checks],
  "expectedCheckCount" -> expectedCheckCount,
  "failedCheckCount" -> Length[DeleteDuplicates[failed]],
  "verdict" -> If[failed === {}, "SUCCESS", "FAILURE"]
|>;
writeBytes[reportPath, jsonBytes[report]];

Scan[Print["check_" <> #[[1]] <> "=" <> If[TrueQ[#[[2]]], "true", "false"]] &, Normal[checks]];
Print["check_count=", Length[checks]];
Print["failed_check_count=", Length[DeleteDuplicates[failed]]];
Print["time_total=", secondsText[AbsoluteTime[] - runStart]];
Print["report=", relativePath[reportPath]];
If[failed =!= {}, Print["failed_checks=", StringRiffle[DeleteDuplicates[failed], ","]]; Exit[1]];
Exit[0];
