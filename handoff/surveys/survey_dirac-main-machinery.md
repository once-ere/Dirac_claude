# dirac-main-machinery

## summary
READ-ONLY survey of C:/Users/nsh/Developer/github/Dirac_claude/dirac-main. I changed nothing there: a before/after file-tree snapshot (size and mtime, excluding backups/) is identical. All scratch output is under C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/survey_tmp2 (called $S below). dirac-main is NOT a git repository: it is an unpacked zip with no .git, and vendor/sundials_rs is an empty directory.

## 1. Markdown to LaTeX builder (scripts/build_dissertation_tex.py, 404 lines, standard library only)

**Flags**
- `--input` (default dissertation/dirac-triality.md) and `--output` (default dissertation/dirac-triality.tex).
- `--strip-heading-numbers` removes the regex `^\d+(?:\.\d+)*\.?\s+` from headings, e.g. "1. ", "1.1 ", "2.3.4. ".
- `--developer-layout` gives raggedright table columns 0.80/n wide, wraps tables in \small, and makes inline code breakable in 8-character chunks with \allowbreak.
- The output is always written UTF-8 with LF. It prints input=, output= and output_bytes=.
- The public function is `convert(markdown, strip_heading_numbers=False, developer_layout=False)`; the tests call it directly.

**Mapping**
- **Title and subtitle:** the first `# ` becomes the title. The first `## ` after it is mandatory and becomes the subtitle; a missing one raises ValueError. Together they form `\title{H1\\[0.5em]\large H2}`. `\author{Reproducible exact-real implementation}` and `\date{September 2026}` are hard-coded. The body always gets `\maketitle`, `\tableofcontents`, `\newpage`.
- **Headings:** `##` becomes \section, `###` becomes \subsection, and `####`–`######` plus any later `#` become \subsubsection. A heading whose text is exactly "Abstract" (any level, after number stripping) opens `\begin{abstract}`, which closes at the next heading.
- **Display math:** a line that is exactly `$$` after strip toggles `\[` / `\]`, and the content passes through raw.
- **Inline markup:** `$…$` passes through raw. Backtick code becomes `\texttt{\detokenize{…}}`. `**x**` becomes \textbf and `*x*` becomes \emph.
- **Fenced code:** any line starting with ``` (after strip) toggles `\begin{Verbatim}[fontsize=\small]` from fancyvrb. The info string is ignored and the content is verbatim.
- **Tables:** a `|` line followed by a separator whose cells all match `:?-{3,}:?` becomes a longtable with booktabs rules and `@{}p{(0.92/n)\linewidth}…@{}` equal-width columns. The header is bold and repeated on each page; alignment colons are ignored.
- **Lists:** `- ` becomes itemize and `N. ` becomes enumerate; single level only.
- **Text:** other lines are joined into paragraphs with spaces. `\ & % # _ { } ~ ^` are escaped, and “ ” – — are mapped to `` '' -- ---.

**Preamble**
- `article[11pt]`; `fontenc[T1]`, `inputenc[utf8]`, lmodern, `geometry[margin=1in]` (US letter, 612x792 pt), amsmath, amssymb, mathtools, booktabs, longtable, array, fancyvrb, `hyperref[hidelinks]`, microtype.
- Determinism primitives: `\pdfobjcompresslevel=0`, `\pdfinfoomitdate=1`, `\pdftrailerid{}`, `\pdfsuppressptexinfo=15`.
- `\parindent 0pt`, `\parskip 0.65em`, `\emergencystretch 3em`.

**Edge-case probe (built and compiled in $S/edge)**
- **Fatal errors:**
  - A Greek letter or math symbol (ψ ω ≤ →) in text or in fenced code.
  - A literal `$`, including `\$`.
  - `%`, an unbalanced `{`/`}`, or a trailing `\` inside backtick code.
  - `#` inside backtick code in a heading.
  - `_` inside backtick code in a heading (fails on the second pass, when the TOC is read).
  - A blank line inside a `$$` block.
  - `\begin{align}` or `equation` inside `$$` ("Erroneous nesting").
  - A table row with more cells than the header, or a `|` inside a code or math cell (e.g. `$|x|$`).
  - An unclosed fence.
- **Warnings that the repository's gate treats as failures:**
  - Math in a heading gives hyperref "Token not allowed in a PDF string".
  - Skipping heading levels (## then ####, or a second H1) gives hyperref "Difference (2) between bookmark levels".
  - A fenced-code line of 90 characters or more gives Overfull \hbox; 89 is the maximum.
  - A long unbreakable inline code token in a paragraph gives Underfull; in a table cell it gives Overfull.
  - Single-line `$$ x $$` gives "\textbackslash invalid in math mode" and garbled output.
- **Silently wrong output (compiles, renders incorrectly):**
  - `#` in inline code prints as `##`.
  - Control words in inline code get a space inserted: `\alpha+1` prints as `\alpha +1`, and `scripts\verify_x` as `\verify _x`.
  - `\(x\)` prints literally.
  - `[text](url)` links print literally.
  - `* ` bullets become emphasis.
  - Nested lists are flattened.
  - `>` quote markers print literally.
  - `---` becomes an em dash.
  - A separator with only two dashes (`|--|`) is not a table and prints as pipe text.
  - A paragraph line starting with "2026. " becomes a list item.
  - A stray `*` in text before a `*` inside later math on the same paragraph breaks.
  - `_x_` prints literal underscores.
- **Work fine:**
  - Latin-1 accents (ö é ï), ’ ‘ quotes, `< > | ~ ^` in text.
  - `$HOME` and `~/.x^2` in code.
  - `(4,4)` in a heading's code span.
  - `aligned` inside `$$`.
  - Multi-line `$$` blocks.
  - Indented `$$` fences.
  - List continuation lines.
  - `**bold `code`**` and `*emph $x$*`.

**Run on EINSTEIN_SPINOR_44.md**
- The regenerated .tex is byte-identical to the committed provenance/EINSTEIN_SPINOR_44.tex (33802 bytes).
- Three pdflatex passes into $S/pdf-a (built from the scratch .tex) and $S/pdf-b (built from provenance/…tex) all exited 0.
- The warning regex found nothing in either .log.
- Both PDFs are 21 pages, 356174 bytes, sha256 3bb9fb215135852f4f2f8f444686de69665ee28ea5198705104d2b46c4801251, identical to the committed PDF. So the output does not depend on the input or output path.
- Toolchain: MiKTeX-pdfTeX 4.27 (MiKTeX 26.5) at C:/Program Files/MiKTeX/miktex/bin/x64/pdflatex.exe, already on PATH.

## 2. PDF checkers

**What check_dissertation_pdf.verify_pdf checks (six checks)**
1. `header`: starts with `%PDF-`.
2. `endMarker`: ends with `%%EOF`.
3. `pageCount`: the number of regex matches of `/Type\s*/Page(?!s)\b`.
4. `mediaBox`: the set of `/MediaBox [...]` values must be exactly `[(0,0,W,H)]`.
5. `canonicalHash`: sha256 of the file equals the pin.
6. `repeatByteIdentity`: `--repeat` bytes are identical.

The page and MediaBox regexes only work because `\pdfobjcompresslevel=0` keeps page objects out of object streams.

**Pins and CLI**
- check_dissertation_pdf.py `PDF_SPECIFICATIONS`: editions `original` and `learn`. It also accepts `--expected-pages`, `--expected-sha256`, `--expected-width` and `--expected-height` overrides, so an ad-hoc edition can be checked without editing the file.
- check_provenance_pdf.py `SPECIFICATIONS`: developer-summary, curved-spin-bundle, einstein-spinor-44, weitzenbock-spinor-44, einstein-spinor-44-components-x0-x7, einstein-spinor-44-numerics-x0-x7. Each entry has `{path, pages, sha256}`. The `--edition` choices come from `sorted(SPECIFICATIONS)`; width and height are fixed at 612 and 792.

**Determinism**
- SOURCE_DATE_EPOCH and FORCE_SOURCE_DATE are not used anywhere. Determinism comes from the pdfTeX primitives plus three clean passes into fresh build directories.
- The hash pins implicitly depend on the MiKTeX and package versions.

**To register a new edition**
1. Build the PDF.
2. Measure its pages and sha256.
3. Add `"new-edition": {"path": Path("provenance/X.pdf"), "pages": N, "sha256": "…"}` to SPECIFICATIONS.
4. Add a DOCUMENTS entry in tests/test_curved_spin_publications.py: stem, markdown_sha256, tex_sha256, and required phrases (matched after collapsing whitespace).
5. Know what those tests enforce:
   - convert(strip_heading_numbers=True) must equal the committed .tex.
   - No TODO or FIXME in the Markdown.
   - Any `provenance/*.md` reference inside the Markdown must point to itself.
   - test_pdf_checker_rejects_mutated_bytes iterates every SPECIFICATIONS entry, so each PDF must be committed.
6. Add .gitattributes lines: `provenance/X.md text eol=crlf` (existing convention), `provenance/*.tex text eol=lf`, `provenance/*.pdf binary`.
7. Copy the gate script pattern from scripts/verify_phase5_curved_spin_gravity.ps1:
   - Build .tex twice.
   - Run three pdflatex passes into build/<phase>/<label>-pdf-a and -pdf-b.
   - Run check_provenance_pdf --edition … --repeat.
   - Compare SHA256 pairs.
   - Scan logs with `^!|LaTeX Warning|Package .* Warning|Overfull|Underfull|Undefined control sequence`.
   - Copy the -pdf-a result into provenance/.

## 3. Rust studies

**Layout**
- Root Cargo.toml: workspace resolver 2; members studies/{einstein_spinor_44, spinor_cosmology, triality_transport, weitzenbock_spinor_44}; exclude vendor/sundials_rs; `workspace.package` version 0.1.0, edition 2021, license GPL-3.0-or-later; `profile.release` opt-level 3.
- .cargo/config.toml sets `rustflags=["-C","target-feature=+fma"]`. The pinned numbers depend on this.
- Each study's Cargo.toml has path dependencies `sundials_core` and `cvode_rs` at ../../vendor/sundials_rs/crates/{sundials_core,cvode_rs}.
- Each study has src/generated.rs (generated), lib.rs (physics, integrate, tests) and main.rs (CLI and writers).
- lib.rs carries `#![forbid(unsafe_code)] #![deny(warnings)]` and `use cvode_rs::prelude::*;`.
- It uses `sundials_core::sundials_libm::{exp, log}` for deterministic elementary functions. The available set is exp, log, expm1, log1p, sin, cos, atan, asin, acos, sinh, cosh, acosh; there is no pow or tanh, so pow is written as exp(b*log(x)).

**Solver setup (integrate_branch)**
```rust
SUNContext_Create(SUN_COMM_NULL, &mut ctx_opt);
N_VNew_Serial(N as i64, &ctx);
N_VGetArrayPointer(&v).unwrap().copy_from_slice(&y0);
// abstol vector filled with config.absolute_tolerance
let cvode = CVodeCreate(CV_BDF, &ctx)?;
CVodeInit(&cvode, rhs, 0.0, &y);
CVodeSVtolerances(&cvode, rtol, &abstol_vec);
let m = SUNDenseMatrix(N, N, &ctx)?;
let ls = SUNLinSol_Dense(&y, &m, &ctx)?;
CVodeSetLinearSolver(&cvode, &ls, Some(&m));
CVodeSetMaxNumSteps(&cvode, 1_000_000);
CVodeSetMaxStep(&cvode, hmax);
CVodeSetStopTime(&cvode, tfinal);
// loop over targets
CVode(&cvode, target, &y, &mut t, CV_NORMAL); // flag < 0 is an error
CVodeGetNumSteps(&cvode, &mut i64);
CVodeGetNumRhsEvals(&cvode, &mut i64);
// cleanup
CVodeFree(&mut Some(cvode)); SUNLinSolFree(Some(ls)); SUNMatDestroy(m);
N_VDestroy(v); SUNContext_Free(&mut Some(ctx));
```
- There is no user Jacobian (the internal dense difference-quotient Jacobian is used) and the default Newton nonlinear solver.
- Defaults: rtol 1e-11, atol 1e-13, hmax 0.002. Refined run: 1e-12, 1e-14, 0.001.
- Two branches both start at t=0: backward to T_MIN=-0.2 (20 outputs) and forward to T_MAX=1.5 (150 outputs). The backward branch is reversed and joined, giving 171 samples.
- Other signatures in the port: `CVodeSStolerances(&mem, rtol, atol)`, `CVodeSetJacFn(&mem, Option<CVLsJacFn>)`, `CVodeRootInit(&mem, n, Option<CVRootFn>)`, `CVodeGetDky`, `CVodeReInit`, `CVodeSetUserData(&mem, Option<Box<dyn Any>>)`. Constants: CV_BDF=2, CV_NORMAL=1, CV_ONE_STEP=2, CV_SUCCESS=0, CV_TSTOP_RETURN=1.

**RHS signature**
- `fn rhs(_t: f64, y: &N_Vector, ydot: &N_Vector, _ud: &mut Option<Box<dyn Any>>) -> i32`. It returns 0 on success, 1 for a recoverable error (non-finite state or domain error), -1 when N_VGetArrayPointer returns None.
- `N_VGetArrayPointer(&N_Vector) -> Option<RefMut<Vec<f64>>>` is a RefCell borrow. The RHS copies y into a local `[f64; N]` inside a block so the borrow drops, computes `rhs_values(&state) -> Result<State, String>`, then writes `ydot[..N].copy_from_slice(&d)`.
- Physics (`rhs_values`):
```rust
d[0] = a*H;
d[1] = -KAPPA_8/(7-1)*(rho+p);
d[2+r] = -0.5*7*H*psi[r] - V'(S)*sum_c TIME_GAMMA[r][c]*psi[c];
// S = psi^T C psi (SPINOR_BILINEAR)
// V = S/20 + (19/20) S^(1/5)
// p = (n-1)*(19/20) S^n, with n = 1/5 (SELF_EXPONENT); n-1 = -4/5
```

**Outputs**
- CSV: every value goes through `sundials_core::sundials_utils::fmt_e(v, 17)` (C `%.17e`), comma-joined, with a header row, LF line endings and a trailing newline. It is written with `fs::write`.
- summary.json is hand-built with `format!(concat!(…))`: fixed key order, two-space indent, floats via fmt_e(…,17), integers plain, and a verdict field. It embeds the fixture SHA-256s. main.rs also prints PASS/FAIL lines and exits 1 on failure.

**Constants generation**
- `scripts/generate_*_constants.py` reads the JSON fixtures (artifacts/exact/cl44-seed.json and artifacts/curved-spin-geometry/geometry.json).
- It verifies exact integer identities: C symmetric, C² = I, γ_t² = −I, γ_tᵀC = −Cγ_t, and C equal to geometry.spinorBilinear.matrix.
- It emits `// Generated … Do not edit by hand.` followed by `#[rustfmt::skip] pub const …`. Integers render as `N.0`; rationals render as `(n.0 / d.0)` in the triality generator. SHA-256 strings of the fixture files are embedded. Output is written LF.
- C = γ1γ2γ3γ4 (the first four generators) and TIME_GAMMA = generators[4].

## 4. Semantic checker pattern (scripts/check_einstein_spinor_44.py)
- `verify_output()` returns `{checks: {name: bool}, measurements}`.
- The script prints `check_<name>=true/false`, `measurement_…`, `check_count` and `failed_check_count`. It asserts the check count equals EXPECTED_CHECK_COUNT (22) plus 1 for `--repeat` plus 1 for `--refined`.
- It recomputes everything in independent float Python from the fixtures.

Check categories:
- **Provenance:** files present, schema version, study name and dimensions, fixture hashes against the actual fixture files, parameters.
- **Structure:** CSV header, sample count 171, time grid (T_MIN + i·0.01 to 1e-13), present epoch appears exactly once, all values finite, initial data at row 20.
- **Re-derivation:** recorded derived values (S, ρ, p, w, fractions, acceleration) and recorded errors recomputed, positive-condensate domain, analytic error limits ≤ 1e-8, summary errors match the recomputed maxima.
- **Physics:** acceleration transition time and scale checked against the closed form a*=(5m/((2−7n)λ))^(1/(7(1−n))) and bounded in (0.8, 0.9). Here m = MASS_COEFFICIENT = 1/20, λ = SELF_COEFFICIENT = 19/20, n = SELF_EXPONENT = 1/5.
- **Finite differences:** five-point central differences of all 18 components against an independent RHS (RMS < 1e-3), and the spatial Einstein equation 6Ḣ+21H²+κp from finite differences (< 1e-6). The dust plus negative-pressure fractions sum to 1.
- **Hash pins:** canonical history and summary hashes, and solver steps/RHS evaluations pinned at 1372/1486.
- **Optional:** repeatByteIdentity; refinedConvergence (same linked fields, refined tolerances, pinned 2294/2422 steps/evaluations, every error strictly improved, maximum state difference < 2e-9, refined errors < 3e-9).

The exact geometry and model checkers (check_curved_spin_geometry.py, 16 checks; check_einstein_spinor_model.py, 4 checks) use `fractions.Fraction` exact arithmetic with the standard library only.

## 5. Wolfram conventions (wolfram/CurvedSpinGeometry.wl)
- Package ``Dirac`CurvedSpinGeometry` ``, which needs ``Dirac`Cl44` `` loaded first.
- `eta = Cl44Metric = diag(1,1,1,1,-1,-1,-1,-1)`; `gamma = Cl44Generators`, 8 real 16×16 matrices.
- Coordinates `{x0,x1,x2,x3,t,y1,y2,y3}` with `timeIndex=5` (1-based; index 4 zero-based in the docs).
- `frame[[mu,a]] = e_mu^a = DiagonalMatrix` with a[t] everywhere except 1 at t. `inverseFrame[[a,mu]] = e_a^mu`.
- Metric `g = frame.eta.frame^T`, i.e. g_{μν} = e_μ^a η_ab e_ν^b.
- `christoffel[[rho,mu,nu]] = Γ^ρ_{μν} = ½ g^{ρσ}(∂_μ g_{νσ} + ∂_ν g_{μσ} − ∂_σ g_{μν})`.
- `spinConnectionRaised[[mu,a,b]] = ω_μ^a_b = e_b^ν(Γ^ρ_{μν} e_ρ^a − ∂_μ e_ν^a)`.
- `spinConnection[[mu,a,b]] = ω_{μab} = η_ac ω_μ^c_b`.
- Vielbein postulate checked: ∂_μ e_ν^a − Γ^ρ_{μν} e_ρ^a + ω_μ^a_b e_ν^b = 0.
- `spinMatrices[[mu]] = 1/8 Σ_{a,b} ω_{μab}[γ^a,γ^b]` summed over all ordered pairs (1/4 if only a<b), so D_μ = ∂_μ + spinMatrices[[μ]].
- `curvedGamma[[mu]] = e_a^μ γ^a`. The slash connection equals (7/2)(ȧ/a)γ^t.
- Charge C = γ1·γ2·γ3·γ4 is symmetric, an involution, has signature (8,8), and satisfies γ^T C = −Cγ. The connection commutes with the volume element.
- The report returns 11 checks plus measurements: 21 nonzero Christoffel entries and 14 nonzero spin-connection entries.
- scripts/verify_curved_spin_geometry.wls does `Get` on both packages, calls the report, prints check_ lines, expects 11 checks, and exports RawJSON `{schemaVersion, sourceSha256{Cl44.wl, CurvedSpinGeometry.wl}, checks, measurements}`. Export writes CRLF and tabs. Invocation: `wolframscript -file scripts/verify_curved_spin_geometry.wls -- <out.json>`.
- I ran it with WolframScript 1.14.0 in 3.2 s: all 11 checks true. The output differs from the committed report only in the two source hashes, because of line endings (see pitfalls).

**Tests**
- tests/test_*.py are flat unittest modules with no __init__.py in tests/ or scripts/. They are discovered by `python -m unittest discover -s tests -v` run from the repository root; the root lands on sys.path through `python -m`, so `from scripts import X` works as a namespace package.
- Scripts that import each other use `try: from scripts import X / except ModuleNotFoundError: import X`.
- Tests call the verify_*() functions directly and write only to tempfile directories.

## 6. Notebooks
- **build_jupyter_notebook.py:** writes an nbformat 4.5 notebook as plain JSON, with fixed cell ids, empty outputs, execution_count None, `metadata.dirac.inputSha256`, and python3 kernelspec. Serialized as `json.dumps(indent=1, ensure_ascii=True)+"\n"` with LF.
- **run_jupyter_notebook.py:** no Jupyter CLI involved.
  - It calls `nbformat.read(...)`, sets `os.environ["PYTHONHASHSEED"]="0"`, then runs `nbclient.NotebookClient(nb, timeout=600, kernel_name="python3", resources={"metadata":{"path": repo_root}}, allow_errors=False).execute()`.
  - The kernel's working directory is the repository root.
  - It filters a zmq Proactor RuntimeWarning.
  - Afterwards it coalesces adjacent stream outputs, pops `cell.metadata.execution` (timestamps), normalizes kernelspec and language_info, and writes the same JSON form.
  - The kernel comes from the user kernelspec C:\Users\nsh\AppData\Roaming\Python\share\jupyter\kernels\python3, whose argv is `python -m ipykernel_launcher -f {connection_file}`; `python` resolves to C:\Python314\python.exe.
  - A probe notebook ran in 6.4 s and executed from the dirac-main working directory.
- **check_jupyter_notebook.py:** checks format 4.5, 10 cells / 5 code cells, unique ids, execution counts 1..5, no errors, final checks visible, jupyter-report.json with 6 checks and input hashes, canonical hash, repeat identity.
- **build_mathematica_notebook.wls:** builds `Cell[BoxData[ToBoxes[Unevaluated[expr], StandardForm]], "Input"]` from code strings via `ToExpression[code, InputForm, HoldComplete]`. It creates `Notebook[cells, WindowTitle, StyleDefinitions -> "Default.nb", TaggingRules -> <|GeneratedBy, SchemaVersion -> 2|>]`, writes it with `Put`, re-imports it as Text, strips trailing spaces and tabs before newlines, and writes it back with BinaryWrite in UTF-8.
- **verify_mathematica_notebook.wls:** imports the .nb as "Notebook" and extracts the Input BoxData (expects 20 cells). It evaluates each cell with `ReleaseHold[ToExpression[boxes, StandardForm, HoldComplete]]` inside `Block[{$DiracRepositoryRoot = root, $MessageList = {}}]`, collecting messages. It fails on any $Failed result, any message, a count other than 9 for `notebookChecks`, or any false check. Notebook cells locate the repository through `If[ValueQ[$DiracRepositoryRoot], $DiracRepositoryRoot, ParentDirectory[NotebookDirectory[]]]`.

## 7. Python environment
- Interpreter: C:\Python314\python.exe, Python 3.14.5 (MSC v.1944, AMD64).
- Packages (all in the user site, C:\Users\nsh\AppData\Roaming\Python\Python314\site-packages): numpy 2.4.6, matplotlib 3.11.0, nbformat 5.10.4, nbclient 0.10.2, ipykernel 7.1.0, jupyter_client 8.6.3, jupyter_core 5.9.1, sympy 1.14.0, mpmath 1.3.0, pyzmq 27.1.0, nbconvert 7.16.6, IPython 9.7.0, jupyterlab 4.4.10, notebook 7.4.7, jupyter_server 2.17.0.
- **scipy is NOT installed.**
- `python -m jupyter --version` works, but `python -m jupyter kernelspec list` fails ("Jupyter command `jupyter-kernelspec` not found") because C:\Users\nsh\AppData\Roaming\Python\Python314\Scripts is not on PATH. `python -m jupyter_client.kernelspecapp list` works and shows python3.

## 8. Solver vendor and cargo
- vendor/sundials_rs is empty. .gitmodules points at https://github.com/once-ere/SUNDIALS_7_8_Rust_port_for_Windows11.git, and the pin is d1836e6a279d63a90fe2839a0020123245487e76 (checked by verify_phase5/6/7).
- `cargo build --release -p einstein_spinor_44 --offline --target-dir $S/target` in dirac-main fails immediately (exit 101): it cannot read vendor/sundials_rs/crates/cvode_rs/Cargo.toml.
- The pinned commit is absent from every local clone: SUNDIALS_7_8_Rust_port, _for_AppleSilicon_macos, _for_Linux, _for_Linux_on_ubuntu and _for_Windows11.
- The local C:/Users/nsh/Developer/github/SUNDIALS_7_8_Rust_port_for_Windows11 clone is clean at HEAD 7cdc6bffbe5c06cea796409eb71e0b52bcca4324 (2026-08-11) and has crates arkode_rs, cvode_rs, cvodes_rs, ida_rs, idas_rs, kinsol_rs, sundials_core.
- **Workaround that works:**
  - Setup: a scratch workspace $S/ws containing a copy of the study, root Cargo.toml and .cargo/config.toml (+fma), and Cargo.lock, with the dependency paths rewritten to the absolute Windows11 clone crates.
  - Build: offline release build in 3.9 s with toolchain cargo/rustc 1.91.1.
  - Run:
    - Output: 0.04 s, 1372 steps / 1486 RHS evaluations. history.csv sha256 9553b36f… and summary.json 6b15d084… are byte-identical to the committed artifacts.
    - Refined run: 2294/2422 steps/evaluations.
  - Tooling: cargo test gives 4/4 passing; clippy `-D warnings` and `fmt --check` are clean.
  - Checker: check_einstein_spinor_44.py with --repeat and --refined passes 24/24 once given a CRLF-normalized cl44 fixture.

Full unittest run in dirac-main: 47 tests in 33.5 s, 10 failures and 3 errors. Causes:
- **Line endings (10 failures):** the LF working copy versus CRLF-pinned hashes. Affected tests: test_cl44_fixture, test_split_octonion_fixture, test_triality44_fixture, test_curved_spin_geometry, test_weitzenbock_spin_geometry, test_einstein_spinor_44_output, test_spinor_cosmology_output, test_triality_transport_output, test_weitzenbock_spinor_44_output, test_developer_summary.
- **Missing vendor source (3 errors):** the three test_phase7_x0_x7_refinement errors read vendor/sundials_rs/crates/cvode_rs/src/cvode.rs.
- **Passing:** all publication, PDF and builder tests.

## key_files
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/build_dissertation_tex.py :: Markdown-subset to LaTeX converter (convert() API, --strip-heading-numbers/--developer-layout, deterministic pdfTeX preamble)
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/check_provenance_pdf.py :: Edition registry SPECIFICATIONS {path,pages,sha256}; --edition/--repeat; fixed 612x792
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/check_dissertation_pdf.py :: verify_pdf(): header/EOF/pageCount/mediaBox/canonicalHash/repeatByteIdentity; CLI overrides --expected-pages/--expected-sha256/--expected-width/--expected-height
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/verify_phase5_curved_spin_gravity.ps1 :: Template gate: vendor pin check, backups, logged steps, 3-pass pdflatex A/B, PDF check, hash pairs, LaTeX warning regex, copy to provenance
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/run_logged.ps1 :: Runs a command string, tees output to a log with started/finished/exit_code lines
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/tests/test_curved_spin_publications.py :: DOCUMENTS registry: md/tex sha256 pins, required phrases, no TODO/FIXME, self-reference rule, PDF spec checks, mutation test over all SPECIFICATIONS
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/studies/einstein_spinor_44/src/lib.rs :: CVODE BDF + dense linear solver setup, RHS callback, two-branch integration, unit tests
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/studies/einstein_spinor_44/src/main.rs :: CLI (--output/--relative-tolerance/--absolute-tolerance/--maximum-step), deterministic CSV/JSON writers via fmt_e(v,17), PASS/FAIL prints
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/studies/einstein_spinor_44/Cargo.toml :: Study crate with path deps on vendor/sundials_rs/crates/{sundials_core,cvode_rs}
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/Cargo.toml :: Workspace (4 study members, excludes vendor/sundials_rs, workspace.package, release opt-level 3)
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/.cargo/config.toml :: rustflags -C target-feature=+fma (affects pinned numerical hashes)
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/.gitattributes :: eol pins for hash-sensitive files (provenance md crlf, tex lf, pdf binary, artifacts csv/json lf, wolfram-report.json crlf)
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/generate_einstein_spinor_constants.py :: Fixture JSON -> generated.rs constants with exact-integer validation and embedded fixture sha256
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/generate_triality_transport_constants.py :: Same pattern with rational literals rendered as (n.0 / d.0)
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/check_einstein_spinor_44.py :: Independent semantic verifier of study output (22 checks + repeat + refined)
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/check_curved_spin_geometry.py :: Exact Fraction-based geometry checker (16 checks) cross-checking Wolfram report
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/build_curved_spin_geometry.py :: Exact Python builder of geometry.json (json.dumps indent=2, ensure_ascii)
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/wolfram/CurvedSpinGeometry.wl :: Exact Wolfram frame/Christoffel/spin-connection/spin-matrix derivation and 11-check report
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/wolfram/Cl44.wl :: Cl(4,4) metric diag(1,1,1,1,-1,-1,-1,-1), 8 real 16x16 generators, volume element
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/verify_curved_spin_geometry.wls :: WolframScript driver: loads packages, prints check_ lines, exports RawJSON with source sha256
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/build_jupyter_notebook.py :: Deterministic nbformat-4.5 JSON notebook generator with fixed cell ids
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/run_jupyter_notebook.py :: Executes ipynb via nbclient.NotebookClient (no jupyter CLI), normalizes output
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/check_jupyter_notebook.py :: Executed-notebook checker (cells, execution counts, report, canonical hash, repeat)
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/build_mathematica_notebook.wls :: Builds .nb from code strings via ToBoxes, strips trailing whitespace, binary UTF-8 write
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/verify_mathematica_notebook.wls :: Headless evaluation of all Input cells with $DiracRepositoryRoot, message/failed-check gating
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/provenance/EINSTEIN_SPINOR_44.md :: Reference provenance Markdown that compiles warning-free (model for new documents)
- C:/Users/nsh/Developer/github/SUNDIALS_7_8_Rust_port_for_Windows11/crates :: Local solver clone (HEAD 7cdc6bf, not the pinned d1836e6a) that builds offline and reproduces canonical outputs
- C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/survey_tmp2/ws :: Scratch workspace copy of einstein_spinor_44 with path deps pointed at the local Windows11 clone (working template)
- C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/survey_tmp2/edge/run_edges2.py :: Markdown edge-case probe harness (builder + 2-pass pdflatex + warning regex)

## commands
- python scripts/build_dissertation_tex.py --strip-heading-numbers --input provenance/EINSTEIN_SPINOR_44.md --output $S/EINSTEIN_SPINOR_44.tex   (run from dirac-main; output byte-identical to committed .tex, 33802 bytes)
- for p in 1 2 3; do pdflatex -interaction=nonstopmode -halt-on-error -jobname=EINSTEIN_SPINOR_44 -output-directory=$S/pdf-a $S/EINSTEIN_SPINOR_44.tex; done   (all exit 0; same for -output-directory=$S/pdf-b with provenance/EINSTEIN_SPINOR_44.tex)
- grep -nE "^!|LaTeX Warning|Package .* Warning|Overfull|Underfull|Undefined control sequence" $S/pdf-a/EINSTEIN_SPINOR_44.log $S/pdf-b/EINSTEIN_SPINOR_44.log   (no matches = warning-free, the repo gate's regex)
- python scripts/check_provenance_pdf.py --edition einstein-spinor-44 $S/pdf-a/EINSTEIN_SPINOR_44.pdf --repeat $S/pdf-b/EINSTEIN_SPINOR_44.pdf   (6/6 checks, 21 pages, sha256 3bb9fb21..., identical to committed)
- python scripts/check_dissertation_pdf.py <pdf> --expected-pages N --expected-sha256 <hex> [--repeat <pdf2>]   (ad-hoc check without registering an edition)
- cargo build --release -p einstein_spinor_44 --offline --target-dir $S/target   (in dirac-main: FAILS exit 101, vendor/sundials_rs empty)
- cd $S/ws && cargo build --release -p einstein_spinor_44 --offline --target-dir $S/target   (scratch copy w/ deps -> C:/Users/nsh/Developer/github/SUNDIALS_7_8_Rust_port_for_Windows11/crates/{sundials_core,cvode_rs}; 3.9 s)
- $S/target/release/einstein_spinor_44.exe --output $S/es44-out   (history.csv/summary.json byte-identical to committed; 1372 steps / 1486 rhs)
- $S/target/release/einstein_spinor_44.exe --output $S/es44-refined --relative-tolerance 1e-12 --absolute-tolerance 1e-14 --maximum-step 0.001   (2294/2422)
- cd $S/ws && cargo test -p einstein_spinor_44 --offline --target-dir $S/target ; cargo fmt -p einstein_spinor_44 -- --check ; cargo clippy -p einstein_spinor_44 --all-targets --offline --target-dir $S/target -- -D warnings   (4/4 tests, clean)
- python -B scripts/check_einstein_spinor_44.py --output $S/es44-out --repeat $S/es44-repeat --refined $S/es44-refined --clifford-fixture $S/cl44-seed-crlf.json   (24/24; without the CRLF fixture, fixtureHashes fails)
- wolframscript -file scripts/verify_curved_spin_geometry.wls -- $S/wolfram-report.json   (WolframScript 1.14.0; 11/11 checks, 3.2 s)
- PYTHONDONTWRITEBYTECODE=1 python -B -m unittest discover -s tests -v   (from dirac-main: 47 tests, 10 failures + 3 errors all due to LF-vs-CRLF hash drift or empty vendor dir)
- python scripts/run_jupyter_notebook.py <in.ipynb> --output <out.ipynb>   (nbclient; kernel python3 -> C:\Python314\python.exe; cwd = repo root)
- python -m jupyter_client.kernelspecapp list   (works; 'python -m jupyter kernelspec list' does NOT because user Scripts dir not on PATH)
- python -c "import numpy, matplotlib, nbformat, nbclient, ipykernel, sympy, mpmath"   (all import; scipy missing)

## reusable_code
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/build_dissertation_tex.py :: Markdown-subset to deterministic LaTeX converter :: Copy verbatim, or import convert(markdown, strip_heading_numbers=True). \author and \date are hard-coded, so edit them if the new repo needs other values; if you do, pin new tex/pdf hashes. Keep the 4 pdfTeX determinism primitives and \pdfobjcompresslevel=0, which the PDF checker's regexes need.
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/check_dissertation_pdf.py + scripts/check_provenance_pdf.py :: PDF structural and hash verifier with an edition registry :: Copy both; check_provenance_pdf imports check_dissertation_pdf with a try/except fallback. Register a new edition by adding {path, pages, sha256} to SPECIFICATIONS after the first clean 3-pass build.
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/verify_phase5_curved_spin_gravity.ps1 (+ .sh twin, run_logged.ps1/.sh, resolve_wolframscript.sh) :: Complete reproducibility gate template :: Copy the structure: vendor-commit check, then logged steps, then 3-pass pdflatex into clean A/B build directories, then check_provenance_pdf --repeat, then SHA256 pair comparison, then LaTeX-warning regex scan, then copy the A PDF into provenance/.
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/studies/einstein_spinor_44/src/lib.rs::integrate_branch/rhs :: Working CVODE (BDF, SVtolerances, dense SUNMatrix and SUNLinSol_Dense, max step, stop time, CV_NORMAL output loop, stats, cleanup) and RHS callback idiom :: Copy integrate_branch and rhs. Change STATE_DIMENSION, initial_state and rhs_values. Keep the scoped N_VGetArrayPointer borrows (they are RefCell RefMut). Use sundials_libm exp/log for transcendental functions.
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/studies/einstein_spinor_44/src/main.rs::write_csv/write_summary :: Deterministic CSV/JSON writers using sundials_core::sundials_utils::fmt_e(v,17) :: Copy and adapt the headings and keys. Keep the fixed key order, LF line endings and trailing newline.
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/generate_einstein_spinor_constants.py :: Fixture JSON to generated.rs with integer/rational literals, #[rustfmt::skip], and embedded fixture hashes :: Copy render_array (and rational_literal from generate_triality_transport_constants.py). Write with newline='\n'.
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/check_einstein_spinor_44.py :: Semantic verifier pattern: checks and measurements dicts, check-count assertion, five-point finite-difference residuals, analytic laws, repeat and refined convergence :: Copy the skeleton (verify_output returns a dict; main prints check_/measurement_ lines, verifies EXPECTED_CHECK_COUNT and exits 1 on failure). Reimplement the RHS independently in Python.
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/wolfram/CurvedSpinGeometry.wl + scripts/verify_curved_spin_geometry.wls :: Exact curved-spin-geometry package and WolframScript JSON-report driver :: Copy them and keep the index conventions: frame[[mu,a]]=e_mu^a, omega[[mu,a,b]] lowered, the 1/8 all-ordered-pairs commutator. Requires wolfram/Cl44.wl loaded first.
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/run_jupyter_notebook.py + build_jupyter_notebook.py + check_jupyter_notebook.py :: Deterministic notebook build, execute and normalize pipeline without a Jupyter CLI :: Copy them. Only nbformat, nbclient and a registered python3 kernel are needed, and all are present.
- C:/Users/nsh/Developer/github/Dirac_claude/dirac-main/scripts/build_mathematica_notebook.wls + verify_mathematica_notebook.wls :: Generated Mathematica notebook plus headless evaluation gate :: Copy them. Update the cell list, expectedInputCount (20) and the expected notebookChecks count (9).
- C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/survey_tmp2/edge/run_edges2.py :: Harness that compiles Markdown snippets through the builder and pdflatex and reports errors or warnings :: Adapt the cases dict to pre-flight new provenance Markdown for LaTeX-breaking constructs.

## pitfalls
- dirac-main is not a git repo and vendor/sundials_rs is empty. The cargo build fails immediately, the verify_phase5/6/7 gates throw 'solver submodule commit mismatch' (they run git -C vendor/sundials_rs rev-parse HEAD), and test_phase7 errors on missing vendor/.../cvode.rs.
- The pinned solver commit d1836e6a279d63a90fe2839a0020123245487e76 is absent from all 5 local SUNDIALS clones. The local Windows11 clone at 7cdc6bf does reproduce einstein_spinor_44 byte-identically, but the new repo must choose which commit to pin (fetching d1836e6a needs network).
- Line-ending drift: in this working copy artifacts/exact/*.json and wolfram/*.wl(s) are LF, while the pinned hashes (cl44 0660e436..., wolfram sourceSha256) were computed on CRLF checkouts. This causes 10 unittest failures and fixtureHashes=false. .gitattributes does not pin eol for artifacts/exact/ or wolfram/. In a new repo, pin eol explicitly for every hashed input.
- The builder breaks (fatal) on: non-Latin-1 Unicode (Greek, math symbols, arrows) in text or code fences; a literal $ or \$ in prose; %, unbalanced braces or a trailing backslash inside backtick code; # or _ inside backtick code in headings; a blank line inside a $$ block; align or equation environments inside $$ (use aligned/gathered/split); a | inside table cells, including $|x|$ and code; rows with more cells than the header; an unclosed ``` fence.
- Gate-failing warnings: math in headings (hyperref 'Token not allowed in a PDF string'), skipped heading levels (## to #### or a second H1), fenced-code lines of 90 characters or more (limit 89 at \small, 11pt, 1in margins), and long unbreakable inline code (Underfull in a paragraph, Overfull in a table; --developer-layout mitigates this).
- Silent mis-rendering: # in inline code prints doubled (a##b); control words in inline code get a trailing space (\alpha +1); \(..\), links, blockquotes, * bullets, nested lists, _emph_ and single-line $$..$$ are unsupported; a line starting with '2026. ' becomes a list item; --- becomes an em dash; a stray * in text before a * inside later math breaks.
- $$ must be alone on its own line (leading and trailing whitespace allowed). Display math is always unnumbered \[ \], so there are no \label/\eqref.
- The H1 title and a following H2 subtitle are mandatory, otherwise ValueError. The heading text 'Abstract' opens the abstract environment. \author and \date ('September 2026') are hard-coded.
- PDF determinism relies on \pdfinfoomitdate, \pdftrailerid{}, \pdfsuppressptexinfo=15 and \pdfobjcompresslevel=0 (not SOURCE_DATE_EPOCH). The hash pins are tied to MiKTeX 26.5 / pdfTeX 4.27 and the installed package versions. Always use three clean passes (TOC and longtable) into fresh output directories.
- check_provenance_pdf hard-codes 612x792 (letter). The page and MediaBox regexes require uncompressed objects (\pdfobjcompresslevel=0).
- tests/test_curved_spin_publications.py test_pdf_checker_rejects_mutated_bytes iterates ALL SPECIFICATIONS, so a registered edition needs its PDF committed. The DOCUMENTS test also requires the builder output to byte-match the committed .tex, and forbids TODO/FIXME and references to other provenance/*.md files.
- Numerical hashes depend on .cargo/config.toml '-C target-feature=+fma' and on the solver commit. Copy both into the new repo.
- N_VGetArrayPointer returns Option<RefMut<Vec<f64>>>. Never hold the borrow across CVode calls or while borrowing the same vector again; copy into a local array inside a block, as rhs() does.
- sundials_libm provides only exp, log, expm1, log1p, sin, cos, atan, asin, acos, sinh, cosh and acosh (no pow or tanh). The study writes pow as exp(b*log(x)).
- scipy is NOT installed. numpy 2.4.6, matplotlib 3.11.0 and sympy 1.14.0 are. Existing checkers deliberately use only the standard library (fractions.Fraction, math).
- User-site Python Scripts dir (C:\Users\nsh\AppData\Roaming\Python\Python314\Scripts) is not on PATH, so 'jupyter <sub>' and 'python -m jupyter kernelspec' fail. Use the nbclient API or 'python -m jupyter_client.kernelspecapp'.
- The kernelspec argv is plain 'python', resolved via PATH, currently to C:\Python314\python.exe; a different PATH order (e.g. the hermes venv) would change the kernel interpreter.
- Wolfram Export RawJSON on Windows writes CRLF plus tabs; wolfram-report.json is pinned eol=crlf.
- The provenance .md files are CRLF by .gitattributes convention; the builder handles this via splitlines() and always writes LF .tex.
- Git Bash grep -c $'\r' reported 0 CRs on CRLF files; use Python byte counts to check line endings.

## open_questions
- Pin the new repository's solver submodule to d1836e6a (requires a GitHub fetch; not verified offline) or to the locally available 7cdc6bf? The local commit reproduces einstein_spinor_44 outputs byte-identically.
- Should the new repository fix the line-ending policy for hashed inputs (e.g. force LF for artifacts/exact and wolfram/*.wl) instead of inheriting the dirac-main CRLF-derived pins?
- Should the builder's hard-coded \author{Reproducible exact-real implementation} and \date{September 2026} be parameterized for the new provenance documents? Doing so changes the pinned tex/pdf hashes.
- Will the new numerical study need scipy (not installed) for any cross-check, or stay within the numpy, sympy and mpmath standard-library style of the existing checkers?
- Not surveyed in detail: the Bash twins of the gates (scripts/verify_*.sh) and check_developer_summary.py, which pins repository-wide artifact and publication hashes and would need updating if the new work lands in dirac-main itself.
