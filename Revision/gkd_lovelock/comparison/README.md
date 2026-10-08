# Comparison of the Revision's curvature and Lovelock results with the author's own stored outputs

`Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md` (written when the Revision results were first
committed, commit 3e81eeb, 2026-10-01) announces that "the comparison with the author's own answers is done
afterwards, in a separate, later commit". This folder carries out and records that comparison (2026-10-08).
It does not change any file of `results/`, `code/`, `verification/` or `notebook_reading/`.

## 1. Result

`author-comparison-report.json`: 78 checks, PASS 73, FAIL 0, NOT-AVAILABLE 5.

* The author's metric (stored output `Out[235]`, `gtry = MatrixMetric44`) equals the Revision metric exactly
  under the mapping of section 3, all 64 components (checked FIRST).
* The author's Ricci scalar (stored output `Out[535]`, `RS`) equals the Revision's `ricciScalar` of
  `curvature.json` exactly: R = 6 (a4')^2 - 42 H^2 in the Revision's variables.
* Every one of the 64 components of the author's Einstein tensor (stored output `Out[536]`, `EinsteinG`,
  indices down, raised with the author's own metric) equals the Revision's `einsteinMixed` component exactly
  (64 checks, one per component).
* Lovelock k = 1: the Revision's `P1_mixed_up_h_down_j` of `lovelock-tensors.json` equals -4 times the author's
  G^mu_nu in all 64 components, and the Revision's `L1` equals 2 times the author's RS (normalisations of
  section 4).
* NOT-AVAILABLE (nothing stored by the author to compare with): the Lovelock tensors and scalars of order
  k = 2 and k = 3, and the Christoffel symbols, the Riemann tensor and the Ricci tensor (section 5).
* Two controls show that the comparison is not vacuous: omitting the chain-rule factor of the mapping, or
  omitting the index raising of the Einstein tensor, gives a nonzero difference (both detected).

No disagreement was found. The interpretation is limited by section 6.

## 2. What was read, and how

* The author's notebook `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb`
  (repository root, sha256 `5ee5cb2a95146136ee65636a4aef174f303b6c41da130d2c57e4684f9c8ff69f`), READ ONLY:
  `Get` of the file returns the inert `Notebook[...]` expression; no front end, no `NotebookOpen`, nothing
  is saved. The cells are enumerated as `Cases[nb, Cell[_, _String, ___], Infinity]` (2127 cells: 996 Input,
  805 Output); `cellIndex` is the 1-based position in that list.
* Stored OUTPUT boxes are converted with `ToExpression[boxes, StandardForm, HoldComplete]` (MakeExpression
  inside `HoldComplete`), in a private context: the parsed expression is never evaluated, and none of the
  notebook's definitions is evaluated (no input cell is run). The exact `InputForm` of the held expression is
  written.
* The cells used (label, cellIndex):

| cell | cellIndex | what it is |
| --- | --- | --- |
| `In[79]` | 191 | `beta3 = Exp[2 a4[H x4]]`, `beta1 = Sin[6 H x0]^(1/3)`, `beta2 = Cot[6 H x0]^2` |
| `In[82]` | 193 | `MatrixMetric44 = diag(beta2, beta1 beta3 (3 times), -1, -beta1/beta3 (3 times))` |
| `In[214]` | 338 | the definition of `rt[g]`: inverse metric, Christoffel symbols, Riemann tensor, Ricci tensor, `RS`, `G` |
| `In[235]` / `Out[235]` | 354 / 355 | `gtry = MatrixMetric44` and its stored value (8 x 8) |
| `In[238]` | 360 | `result = {ginv, Gamma, RicciGamma, RieGamma, RS, EinsteinG} = rt[gtry];` (output suppressed) |
| `In[245]` / `Out[245]` | 374 / 375 | `MatrixMetric44` printed again (control: identical to `Out[235]`) |
| `In[535]` / `Out[535]` | 887 / 888 | `RS` and its stored value |
| `In[536]` / `Out[536]` | 889 / 890 | `EinsteinG` and its stored value (8 x 8) |

* Provenance of `Out[535]` and `Out[536]` (an inference from the file, labelled as such): the cell labels form
  one increasing sequence, and among all 996 input cells (held, never evaluated) only `In[238]` assigns the
  global symbols `RS` and `EinsteinG` (`In[214]` assigns the `Module`-local `RS` of `rt`; `In[237]` and
  `In[239]` only unprotect and protect them). The stored values are therefore read as the values returned by
  `rt[gtry]` at `In[238]`. The notebook was not re-run; its outputs are taken as stored.
* A keyword scan of the box strings of every cell of this notebook and of `Generalized _Kronecker_Delta_4+4.nb`
  (sha256 `23bb4e0c70943e766d9b081a3a399ef29664889aad088041329ce2e065b80afb`; this is a later reading than the
  one recorded in `results/PROVENANCE_OF_THE_COMPUTATION.md`, which opened its input cells only): cells
  containing the word "Lovelock" (any case), and cells containing the tokens `P2`, `P3`, `P4`, `LovelockP`,
  `kd` or `k\[Delta]`. Main notebook: 20 cells contain the word; the 4 Output cells among them (`Out[10]`,
  `Out[16]`, `Out[17]`, `Out[18]`) hold only strings (file names); the other 16 are 6 heading and text cells
  (cellIndex 6, 14, 15, 24, 25, 28; they name the Einstein-Lovelock field equations, and cell 15 says that the
  Einstein-Lovelock tensors are calculated "in other included notebooks"), 5 input cells (cellIndex 1795, 1824,
  2023, 2024, 2026) and 5 `Print` cells (1803, 1831, 2018, 2020, 2022) whose only mention is the name of a
  `.mx` file named after the notebook; no cell contains one of the tokens. Kronecker-delta notebook: 3 cells contain the word, all Text cells (cellIndex 135, 139, 146, which
  hold expressions named `Lovelock1`, `Lovelock2`, `Lovelock3` as text, not as evaluated input), none an
  Output cell; the 14 cells with the token `k\[Delta]` are Input and Text cells (the `kδ` definition and its
  tests), none an Output cell.
* The Revision side: `Revision/gkd_lovelock/results/curvature.json` (metric diagonal, Ricci scalar,
  `einsteinMixed`), `Revision/gkd_lovelock/results/lovelock-tensors.json` (`P1_mixed_up_h_down_j`, `L1`) and
  the metric of `Revision/SPEC.md` section 1 (checked against `curvature.json`, 64 components).

## 3. The mapping (stated before the comparison; a definition, not a fit)

* Coordinates. The author's `X = {x0, x1, ..., x7}` (`In[26]`): array position 1 is `x0`, the hidden
  direction (`g00 = Cot[6 H x0]^2`), positions 2 to 8 are `x1` ... `x7`. The Revision (SPEC section 1) uses
  x1, x2, x3 (space), x4 (time), x5, x6, x7 (the extra times, which deflate exponentially, scale factor
  e^{-a4} sin^{1/6} z with a4 increasing) and x8 (hidden). Mapping: author `x0` -> Revision `x8`; author `xk`
  -> Revision `xk` for k = 1 ... 7; tensor components are permuted accordingly.
* The function. The author's `a4` is a function of the argument `H x4` (`In[79]`), the Revision's of `x4`:
  a4_Revision(x4) := a4_author(H x4); by the chain rule a4_author^(n)(H x4) = H^(-n) a4_Revision^(n)(x4)
  (n = 0, 1, 2). The program checks that no other argument of `a4` occurs in the author's outputs.
* H is the same constant on both sides.
* Check on the metric first: under this mapping `Out[235]` equals the Revision metric in all 64 components
  (`metric-mapping-author-Out235-vs-revision`, PASS); only then are the curvature outputs compared.

## 4. Conventions and normalisations (every factor stated and applied, none fitted)

* The author's `rt[g]` (`In[214]`): Gamma^i_jk = (1/2) g^is (d_k g_sj + d_j g_sk - d_s g_jk);
  R^mu_(nu alpha beta) = d_alpha Gamma^mu_(nu beta) - d_beta Gamma^mu_(nu alpha) + Gamma^mu_(s alpha) Gamma^s_(nu beta)
  - Gamma^mu_(s beta) Gamma^s_(nu alpha) (named `RicciGamma` in the notebook); Ric_(mu nu) = R^alpha_(mu alpha nu)
  (named `RieGamma`); `RS = Tr[ginv . Ric]`; `G = Ric - (1/2) g RS`, indices DOWN. The Revision uses the MTW
  convention (`lovelock-components.md`); the two agree, as the comparison of the scalar shows.
* Ricci scalar: no factor.
* Einstein tensor: G^mu_nu = sum_s g^(mu s) G_(s nu) with the author's own (mapped) inverse metric; no other
  factor. The metric and both tensors are diagonal, so the order of the two indices in the Revision's key does
  not affect the result.
* Lovelock k = 1: E_(k) = -P_(k)/2^(k+1) and E_(1) = G (the `normalisationNote` of `lovelock-tensors.json`), so
  P_(1) = -4 G; L_(1) = delta^(j1 j2)_(h1 h2) R^(h1 h2)_(j1 j2) = 2 R (identity of the generalized Kronecker delta).

## 5. What has no author output (NOT-AVAILABLE)

* The Lovelock tensors P_(2), P_(3) and the scalars L_(2), L_(3): no stored output of them was found in either
  notebook (section 2, keyword scan). The re-check confirms the earlier survey of this task.
* The Christoffel symbols, the Riemann tensor and the Ricci tensor: `rt[gtry]` computes them, but `In[238]`
  ends with `;`, so no value is stored there, and no other stored output of their values was taken.

## 6. What this comparison does NOT establish

* Nothing about k = 2 and k = 3: the Gauss-Bonnet and cubic Lovelock tensors of this record are compared with
  no output of the author, because none exists in the files read.
* The agreement is one between two computations of the same objects for this one metric, on the patch
  0 < 6 H x8 < pi/2; it is not an independent check of conventions beyond those stated in section 4.
* The k = 1 Lovelock comparison carries no information beyond the Einstein-tensor comparison together with the
  Revision's own identity P_(1) = -4 G (already a check of the Rust program).
* The author's outputs are taken as stored in the file; the notebook was not re-run, and that the stored
  values come from `In[238]` is the inference stated in section 2.
* The keyword scan finds Lovelock tensors by name; a value stored under an unrelated name would not be found
  by it. Only the two notebooks of the repository were read; the main notebook's text says that the
  Einstein-Lovelock tensors are calculated in other notebooks of the author, and no such notebook was read
  (the repository holds no other notebook of the author; the two notebooks under `notebooks/` are built by
  scripts of the earlier stages).
* Nothing about field equations, sources, solutions or physical interpretation.

## 7. Commands, run times, determinism

From the repository root (Wolfram Language 15.0.1 with WolframScript; Python 3 with sympy 1.14.0):

```text
wolframscript -file Revision/gkd_lovelock/comparison/extract_author_curvature_outputs.wls
python Revision/gkd_lovelock/comparison/compare_with_author.py
```

* The extractor prints the cell count, `inputs parsed: 8/8`, `outputs parsed: 4/4`, the output dimensions, the
  keyword-scan counts and the input cells that mention `RS` or `EinsteinG`, and writes
  `author-curvature-outputs.json` (or the path in the environment variable `AUTHOR_CURVATURE_OUTPUTS`); exit
  code 0, 1 when the notebook is missing or the file cannot be written. Run time 4.4 to 6.0 s (seven runs,
  2026-10-08, shared 24-core Windows 11 machine with other jobs running).
* The comparison prints `checks: 78; PASS 73, FAIL 0, NOT-AVAILABLE 5` and writes
  `author-comparison-report.json` (or `--output <path>`); exit code 0 when no check fails, 1 otherwise. Run
  time 0.7 to 0.9 s.
* Each program was run three times (two runs into a scratch folder, one into this folder): the outputs are
  byte-identical (LF line endings, ASCII). The outputs contain no date or time; they contain the Wolfram
  version string and the sympy version.

| file | sha256 |
| --- | --- |
| `extract_author_curvature_outputs.wls` | `ca446244b7bcfc4573ec603898bddaf2b34e49ca980ee5043b6772cdaa466891` |
| `compare_with_author.py` | `f5e7ca1e2e5b16d2cf45f27e299f7c17884464bf07f08406800aed8864aeeab3` |
| `author-curvature-outputs.json` | `7433675c15aab19ea322c22377cfa8d71c2171f175aa143ee64e35ae8834ed1c` |
| `author-comparison-report.json` | `ed830d8cee677c14b08eabb34863e38844d0a5009587263c71ba444fcdb3c02c` |

## 8. Side effects

* The extractor reads the two notebooks and writes only its JSON file; it never writes a notebook (the
  comparison recomputes the notebook's sha256 and checks it against the one recorded by the extractor,
  `author-json-matches-notebook`). No network access, no package is loaded, no parallel kernels.
* WolframScript, on Windows, creates two files in
  `C:\Users\<you>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary\`: an empty `tmp_<10 letters>`
  at the start and a second `tmp_<10 letters>` that holds a copy of what the script prints (observed for one
  run on 2026-10-08: 566 bytes); a normal exit removes both. An interrupted run leaves both behind; they are
  harmless and can be deleted when no other `wolframscript` runs. During that observation, files of other
  `wolframscript` runs of parallel jobs were in the same folder. Like every kernel start, the kernel may update
  its own settings and caches under the Wolfram user folders.
* The comparison reads the files of section 2 and writes only its report.
