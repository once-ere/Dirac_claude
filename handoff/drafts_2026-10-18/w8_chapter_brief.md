# Brief for a W8 chapter agent (the textbook "Universes in Pairs", corrected metric)

You update ONE chapter of the textbook `Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK` (repository
`/home/claude/dirac_claude`, branch main) and its notebooks to the CURRENT physics of the Revision record: the corrected
metric of 2026-10-16 (version 2). You do not commit; the lead reviews your files and commits them.

## Read first (in chunks of at most 300 lines)

1. `Revision/textbook/TEXTBOOK_SPEC.md` (all of it: rules R0-R6, the deep-dive technique of section 1, notebooks section
   2, run instructions section 3, files section 4, the chapter plan section 5 for your chapter).
2. `Revision/textbook/tools/README.md` (the notebook builders, nbkit, placing notebooks, the Markdown subset, the
   character pairs that must not appear in prose, check_chapter.py).
3. `Revision/SPEC.md` section 1 (the corrected metric; everything after "The metric of 2026-10-14 (withdrawn ...)" is
   history only).
4. The Revision sources of your chapter (the list in your task), especially the documents in `Revision/docs/`, which
   were rewritten for the corrected metric on 2026-10-17/18 and are current, and the JSON reports and results they cite.
5. Your chapter `Revision/textbook/chapters/NN-*.md` and the builders `Revision/textbook/notebooks/src/NN*.py` of its
   notebooks, with the stored notebooks `Revision/textbook/notebooks/NN*.ipynb` and their `.PROVENANCE.md` files.

## The current physics in one paragraph (binding; the Revision record is the authority)

Coordinates are always the author's X = {x0, x1, ..., x7}: x0 the hidden SPACE-LIKE direction, listed first, z = 6 H x0
taking every real value; x1, x2, x3 ordinary 3-space; x4 the time; x5, x6, x7 the three extra times (time-like), which
DEFLATE exponentially. The metric is g = diag(e^{-2a4} b4 cot^2 z, e^{2a4}, e^{2a4}, e^{2a4}, -1,
-e^{-2a4} b4 (sin^2 z)^{1/6} (three times)), with two functions a4(x4) and b4(x4) > 0 of the time (b4 is never 1);
(sin^2 z)^{1/6} is the positive branch. Signature (4,4) wherever sin z cos z != 0; sqrt|g| = e^{-a4} b4^2 |cot z|
(sin^2 z)^{1/4}; vielbein f0 = e^{-a4} b4^{1/2} cot z, f1 = f2 = f3 = e^{a4}, f4 = 1, f5 = f6 = f7 =
e^{-a4} b4^{1/2} (sin^2 z)^{1/12}. 3-space has NO warp. With y = ln|sin z|/(6H) the block (x0, x5, x6, x7) is
e^{-2a4} b4 (dy^2 - e^{2Hy}(dx5^2 + dx6^2 + dx7^2)), a space of constant curvature -H^2: the hidden direction shrinks
together with the extra times. The fold cos z = 0 (z = pi/2, y = 0) joins the two halves z < pi/2 and z > pi/2 of a
cell; there is NO Z2 orbifold, NO brane, NO mirror copy carrying -m (those belonged to the WITHDRAWN metric of
2026-10-14, as did the warp sin^{1/3} z of 3-space, the factor cos z in sqrt|g| and the off-diagonal Lovelock
components). In the corrected metric every Lovelock tensor E_(1), E_(2), E_(3) is diagonal and x0-independent, with
E^x0_x0 = E^xt_xt; there is no mixed Riemann component. Gravity term of the Dirac operator: gamma^mu Omega_mu =
(3/2) H e^{a4} b4^{-1/2} gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4). The history used by every Revision calculation is
the PRESCRIBED background a4 = A H x4, b4 = b4(0) e^{(4/3) A H x4} (A = 1, b4(0) = 1, H = 1), on which the hidden
scale is f = e^{-a4} b4^{1/2} = e^{-a4/3}; it needs a diagonal conserved source with p0 = p_t
(`Revision/metric_warped/results/warped-metric.json`, key history_source). Kohn-Sham (W5): the ansatz
Psi = e^{ik.x} e^{-(3/2)Hy} e^{a4/2} b4^{-1} chi(y, x4) gives eight 2x2 blocks h_j = j[-(i/f) sigma_1 d/dy +
M_eff sigma_2 + kappa k sigma_3] + v_v with kappa = e^{-a4} (constant in y); both fold conditions chi2(0) = 0 and
chi1(0) = 0 are solved and filled (ASSUMED); regular tip at y = -L, L = 3; the free states are exact fold-band gases
(eps = kappa |k|, orbital (e^{f M y}, 0)); N = 8, 592, 2352; Vol_7 = l^3 v_t e^{(5/3) a4}. Pairing: T1, T2 (the
reflection z -> pi - z across the fold between the two halves), Q, T3 (statements S1-S4; the statement S5 of the
mirror copy is removed). Never write "complex conjugation is charge conjugation" (rule R5).

The WITHDRAWN metrics may appear only as dated history ("the metric of 2026-10-14, withdrawn on 2026-10-16"), never
as current physics. Every number in the chapter must come from a current Revision record or from the chapter's own
notebook outputs; every statement carries its status (PROVED with the verifier file and check name, COMPUTED with the
output file, ASSUMED, HYPOTHESIS, OPEN).

## Environment and commands (run from the repository root)

```text
S=/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad
PY=$S/tb314/bin/python                       # Python 3.14.5 with exactly Revision/textbook/requirements.txt
ZNG=$S/zng/build-2.3.3                       # zlib-ng in compat mode: PNG bytes as on the Windows builds
LD_LIBRARY_PATH=$ZNG nice -n 5 $PY Revision/textbook/tools/nbkit.py lint  Revision/textbook/notebooks/src/NNx_name.py
LD_LIBRARY_PATH=$ZNG nice -n 5 $PY Revision/textbook/tools/nbkit.py build Revision/textbook/notebooks/src/NNx_name.py \
    --date 2026-10-18 --scratch $S/w8/<your folder>
LD_LIBRARY_PATH=$ZNG nice -n 5 $PY Revision/textbook/tools/check_chapter.py Revision/textbook/chapters/NN-name.md \
    --scratch $S/w8/<your folder>
```

Use your own scratch folder `$S/w8/chNN`. Run at most one build at a time (the machine has two cores). A build prints
`build_NNx=OK` when the second execution reproduced everything byte for byte. `check_chapter.py` must end with
`chapter_check=OK` (no `problem=` and no `latex_warning=` lines). Rust notebooks build their crate with cargo (available).

## What to do

1. Builders: bring every builder of the chapter to the corrected metric and to the current Revision records (texts,
   formulas, checks, record names, numbers, captions); keep the notebook layout, the deep-dive comments and at least
   the existing number of figures; remove every statement of a withdrawn metric as current physics; `nbkit lint`, then
   `nbkit build` until `build_NNx=OK`. A builder whose notebook does not depend on the metric and already passes
   `nbkit check` needs no rebuild (keep its verified date).
2. Chapter: rewrite every part that teaches a withdrawn metric or quotes changed numbers: definitions, derivations line by
   line (each line followed by the rule that produced it), the "Line-by-line walk-through" of every code cell of every
   rebuilt notebook (quote the lines; In/Out numbers as in the new notebook), the figure descriptions, the numbers (from
   the new outputs), the status labels, the summary "What we proved, what we computed, what we assumed" and the
   exercises with complete worked answers. Keep the section numbering rule of the tools README (the marker
   `<!-- NOTEBOOK NNx -->` expands to two sections; the next section is the walk-through). Keep references
   ("Chapter N", "Section N.M") resolvable; references to chapters you do not edit must stay true.
3. `check_chapter.py` until `chapter_check=OK`.
4. Do not edit anything outside `Revision/textbook/chapters/NN-*.md`, `Revision/textbook/notebooks/src/NN*.py` and the
   files that nbkit writes for your notebooks (`Revision/textbook/notebooks/NN*.ipynb`, `.PROVENANCE.md`,
   `Revision/textbook/figures/NN*`). Never touch `provenance/` (the first-edition textbook is never changed),
   `dirac-main/`, `vendor/` or private files. No git commands that change the repository (no add, commit, stash,
   checkout, reset).
5. Report at the end: the files changed, the notebooks rebuilt (with their PASS counts and figure counts), the
   check_chapter result, every physics statement you were unsure of, and anything left open.
