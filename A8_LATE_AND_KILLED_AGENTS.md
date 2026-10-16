# A8 follow-up: the 23 agents that finished late and the 16 that were killed (2026-10-16)

This file answers the user's order of 2026-10-16 about section A8 of `claude_failures.md` (the agent jobs of
the four workflows of 2026-10-14 that ran longer than 423 s). The order, verbatim:

> Regarding only the 23 agents that finished late (### A8. Agent jobs of the four workflows that ran longer
> than 423 s; 39 of 56 agents exceeded 423 s (16 of them were killed unfinished at ~12:05; the others finished
> late). ), suspend the 423 s runtime limit for these only 23 agents, and allow them to correctly contribute to
> this project. Regarding the 16 of them that were killed unfinished, I will have to perform their tasks by hand
> after receiving a correct mathematical formulation for each task, and then update you with these data.

Part 1 lists the 23 late agents, what each one produced, and how it enters the project. Part 2 gives one task
formulation for each of the 16 killed agents. Each formulation says which objects are involved, which
statements must be checked and the exact criterion for each, so that the task can be done by hand. Nothing in
this file was computed by a new agent job. Every check below was made by Claude, one bounded command at a
time.

The sources are:

- the four workflow journals of session 837d3989, `subagents/workflows/<run>/journal.jsonl`, which hold every
  returned result;
- the scripts of the four workflows. These are `book-continuation-2026-10-14`, `book-final-lens-reviews-2026-10-14`,
  `stage5-docs-prep-2026-10-14` and `errata-e51-first-edition`. The first three are in
  `Revision/workflows/completion_2026_10_14/` (`book_continuation.js`, `book_final_lens_reviews.js`,
  `stage5_docs_prep.js`, byte-identical to the scripts that ran). The errata script is quoted in K10;
- the list of book items that the book-continuation round worked on. This is
  `Revision/workflows/completion_2026_10_14/book_items.json`, 35 items in 15 chapters;
- commit 254ff1b, "State at the kill ... UNVERIFIED partial edits". It and the earlier automatic snapshots
  b13373c and ad962b5 hold every file edit the agents made.

## Part 1. The 23 agents that finished late

### 1.1 What "contribute correctly" means here, and the method

The 423 s limit is suspended for these 23 agents only, as ordered. Their work is therefore accepted as a
contribution, but only after it has been checked against the current files and the current record. That check
is needed for three reasons:

1. Their edits were committed at the kill as UNVERIFIED (254ff1b).
2. The textbook was relabelled to the author's coordinates x0..x7 after they ran (2026-10-14/15).
3. Since 2026-10-15 every chapter is being moved to the metric with b4(x4) (HANDOFF 0.9, phase 9).

So for each agent:

- (a) its returned result was read from the journal;
- (b) its file edits were found in the current repository by their wording;
- (c) everything it reported as still wrong (verifier findings) or left for the lead (open items) was
  re-checked against the current files;
- (d) each item that still holds is applied in phase 9, in the chapter it concerns, and checked like every
  other edit (nbkit build and check, the walk-through checks, `check_chapter.py`).

The table in 1.3 records where each item is done. The 23 agents are:

| # | workflow | agent | seconds | what it produced |
|---|---|---|---|---|
| L1 | stage5-docs-prep | docA:part1 | 1543 | sections 1-6 of `provenance/DIRAC16COMPLEX00_FIELD_THEORY.md` (old Stage 5, document A), 671 lines |
| L2 | stage5-docs-prep | docB:part1 | 1301 | sections 1-4 of `provenance/DIRAC16COMPLEX_PAIR_CREATION.md` (old Stage 5, document B), 499 lines |
| L3-L16 | book-continuation | fix:05, 07, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21 | 425-1251 | the fixes of the 2026-10-08 book-review items of 14 chapters (the textbook "Universes in Pairs") |
| L17-L23 | book-continuation | verify:00, 09, 10, 12, 13, 16, 20 | 552-969 | adversarial verifications of the fixes of chapters 00, 09, 10, 12, 13, 16 and 20 |

(fix:00 finished within 423 s and is not one of the 23. It is included in 1.2 because verify:00 checks it.)

### 1.2 The fixes (L3-L16): present in the current chapters

Every edit that the 14 late fixers reported as FIXED is in the current chapters. Their wording was found with
`grep` on 2026-10-16:

| chapter | item (book_items.json) | fixer verdict | found now |
|---|---|---|---|
| 00 | residual 0: the label of ledger row 2 (OPEN; the field-equations record ASSUMES it) | ALREADY FIXED (fix:00) | 0.18 row 2 and its remark |
| 00 | residual 1: the reference solver ran for two states at L = 3 and 4 | ALREADY FIXED (fix:00) | 0.18 and the 00c walk-through |
| 00 | residual 2: the count of the README reports | ALREADY FIXED (fix:00) | now "50 counts ... 47 different reports, three of which stand there twice" |
| 05 | book_review 0: "proves numerically" in 05a | FIXED | 05a builder: "checks again with its own code ... (COMPUTED ...)" |
| 05 | book_review 1: time-like case of 5.23 (I) | FIXED | 5.23 (I): three stages for a time-like v |
| 07 | book_review 0: normal ordering adds no sign | FIXED | 7.29: "adds no sign" |
| 07 | book_review 1: "self-consistent" undefined | FIXED | 7.23: "What 'self-consistent' means", senses (i)-(vi) |
| 09 | residual 0, 1: n quanta | ALREADY FIXED | 9.13, 9.31 |
| 09 | book_review 0: the record does compute the observer equation of state | FIXED | line 20, 9.19, 9.31 |
| 10 | residual 0: the T-hat row cites its checks | ALREADY FIXED | 10.21 |
| 10 | residual 1: the set-up heading | FIXED in the chapter | 10a In [1] walk-through |
| 11 | book_review 0: every 11.20 value worked out | FIXED | 11.20 "Every component checked by hand" |
| 12 | book_review 0: the G^{x5}_{x5} sum | FIXED | 12.6 "The extra-time component." |
| 13 | book_review 0: Wick's theorem, basis change and thermal case | FIXED | 13.4 "A thermal ensemble" |
| 14 | residual 0, 1: the tip angle | ALREADY FIXED | 14.20, 14.32, builder 14c |
| 14 | book_review 0: brane parity versus T2 gluing | FIXED | 14 "brane parity conditions"; 14b glossary |
| 15 | residual 0-2: the rule revision, the unbroken run, the noise floor | ALREADY FIXED | 15.2 |
| 15 | residual 3: the factor 28 | FIXED | 15.2, 15.15, 15.31 |
| 15 | book_review 0: "Conservation law" | FIXED | 15b word list, chapter 15.15 |
| 16 | residual 0, 1: the scope of the tip study | FIXED | 16.25, 16.26 |
| 17 | residual 0: the 17.23 OPEN list | ALREADY FIXED | 17.23 |
| 17 | book_review 0: 75 ground states, 135 thermal | FIXED | 17 (5 places), builders 17a, 17b |
| 18 | book_review 0: normal ordering adds no sign | FIXED | 18 "T1 and charge conjugation" |
| 18 | book_review 1: hypotheses of Q | FIXED | 18 introduction |
| 18 | book_review 2: T2 Step 7 and Lemma 1 written out | FIXED | 18.15 Step 7, Lemma 1 |
| 20 | book_review 0, 2: no-flux condition | FIXED | 20.25, 20.26 |
| 20 | book_review 1: the three lists of the record | FIXED | 20.24 |
| 20 | book_review 3 | refuted by a skeptic, not applied | (correct) |
| 21 | book_review 0: definition of a charge-conjugation matrix | FIXED | 21.8 "The wish", "Why the definition is the condition and not the wish"; builders 21a, 21c |

The fixes of chapters 05, 07, 11, 15, 17, 18 and 21 had no finished verifier. Those of 05, 07, 11, 15, 17 and 18
are tasks K11 to K16 of Part 2. For chapter 21, see 1.4.

### 1.3 The verifiers (L17-L23) and the fixers' open items: what was still to do

The late verifiers reported 9 problems that remained after the fixes. The fixers listed 14 items for the lead.
None of these had been applied before 2026-10-16 (checked by `grep` on the current files). Each one is
re-checked and, where it still holds, applied in phase 9 together with the chapter it concerns:

| source | item | where it is done |
|---|---|---|
| verify:00 | none (0 findings) | - |
| verify:09 | 9.19: the PROVED condensate statement must cite its checks (`condensate_w_eff`, `condensate_rho_p_w`, `observer_N1_weff_identity`, `observer_N2_weff_identity`) | chapter 09, phase 9 |
| verify:10 | 10.50 "Proved" table and the 10.39 row: name the checks of the deflating-history row | chapter 10, phase 9 |
| verify:12 | none (0 findings) | - |
| verify:13 | (1) 13.4: chemical potential, Gibbs state and weight are used before Section 13.26 defines them, and the ensemble must be called grand canonical; (2) the code-cell counts of 13a and 13b in the walk-through openings; (3) the glossary entry "Thermal ensemble" | chapter 13 and chapter 23, phase 9 |
| verify:16 | two consequences in chapter 15: the N = 8 number is E_KS, not the interaction energy (15.31); the OPEN parenthesis on the large-L limit is incomplete (15.31) | chapter 15, phase 9 (against the tip-cutoff study of the record with b4) |
| verify:20 | (1) 20.25: the conclusion of the classical route must carry the same conditions as its premise; (2) 20.25: the sentence after the photon-analogy table needs the no-flux condition and the brane-flow alternative | chapter 20, phase 9 |
| fix:00 open | chapter 23 and 23a: the counts of reports and checks | chapter 23 (regenerated last) |
| fix:07 open | glossary: "self-consistent" in the field-equation sense, "Lichnerowicz identity" | chapter 23; the Lichnerowicz entry exists |
| fix:07 open | chapter 00 word list: "self-consistent" only in the Kohn-Sham sense | chapter 00, phase 9 |
| fix:07 open | chapter 08: point to 7.23 (i)-(vi) for the self-consistency part of the requirement | chapter 08, phase 9 (in progress) |
| fix:10 open | `tools/nbkit.py` set-up heading "the same in every notebook of this book" is not true (the Rust notebooks add two imports and `rust_program`); chapters 05, 13, 22 repeat it | the tool and every notebook (rebuild), phase 9 |
| fix:13 open | glossary "Thermal ensemble" | chapter 23 |
| fix:14 open | glossary "Z2 brane", "Z2 mirror": only the Kohn-Sham record's Z2 mirror imposes a parity condition | the defining sentences in chapters 00, 14, 18, 20, then chapter 23 |
| fix:15 open | glossary "Conservation law" | already regenerated (chapter 23 has the new entry) |
| fix:17 open | chapters 22 and 00: "no recorded Kohn-Sham state is an admissible source" needs "ground state" (the record tests the 75 ground states, the only states whose profiles it stores; 135 thermal states store none) | chapters 22, 00, phase 9 |
| fix:18 open | chapter 20 Section 20.4: "each kinetic term of T_{mu nu} is unchanged in the same way" - write it out or point to 18.15 Step 7 | chapter 20, phase 9 |
| fix:21 open | chapter 20 (charge conjugation item) and builder 07c purpose: "every matrix that maps solutions to solutions" must be "every matrix that obeys the intertwiner condition" | chapters 20 and 07 (07c), phase 9 |
| fix:20 open, fix:05, 13, 17 open | the assembled book still has the old texts | the book is reassembled at the end of phase 9 |

### 1.4 Chapter 21

fix:21 finished late. Its verifier verify:21 ran only 189 s, so it was not over the limit, but it was killed
unfinished at 12:05. It is therefore not one of the 16 tasks of Part 2. Claude does its verification in phase 9,
when chapter 21 is moved to b4. The same applies to verify:14 (359 s, killed): Claude verifies the chapter-14
fixes in phase 9.

### 1.5 The two old-Stage-5 documents (L1, L2)

docA:part1 and docB:part1 wrote the first parts of the two old-Stage-5 documents. These belong to the first
edition (`provenance/`), which stays unchanged by the b4 order ("You must NOT mix old with new"). Their text is
in the repository unchanged since 254ff1b. What they rest on:

- every number comes from the committed Stage-5 exact reports. These are `wolfram-dirac16complex00-report.json`
  (46/46), `python-dirac16complex00-report.json` (49/49) and `dirac16complex00-theory.json`; for document B,
  `wolfram-pairing-report.json` (141/141), `python-pairing-report.json` (172/172) and `pairing-theory.json`;
- the agents report that every cited check name exists in those reports. Claude re-checks this mechanically
  (section 1.6).

Their parts 2 (docA:part2 and docB:part2) were killed within 423 s and are not among the 16 tasks; the review
of document A never ran. The old Stage 5 also lacks its long numerics. The Rust pairs run is estimated at 3 to
5 h and the reference pairs runs at hours, both beyond the 423 s rule, so the stage cannot be completed by
Claude under the current rules. Task K1 states what remains.

### 1.6 Status log (updated as the items are done)

- 2026-10-16: Parts 1 and 2 written; the fixes of 1.2 found in the current chapters; the items of 1.3 found
  still open.

## Part 2. The 16 killed tasks: formulations for the user

Notation used throughout:

- The author's coordinates are x0, ..., x7: x0 is the hidden direction with z = 6 H x0 and 0 < z < pi/2;
  x1, x2, x3 are 3-space; x4 is the time; x5, x6, x7 are the extra times.
- eta = diag(+1, +1, +1, +1, -1, -1, -1, -1) in this order.
- gamma^(a) are the author's real 16 x 16 gammas, with gamma^(a) gamma^(b) + gamma^(b) gamma^(a) = 2 eta^{ab} 1.
- Gamma = gamma^(x0) ... gamma^(x7); C = gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3); B = -i C gamma^(x4).
- The metric is g = diag(cot^2 z, e^{2 a4} s, e^{2 a4} s, e^{2 a4} s, -1, -b4 e^{-2 a4} s, -b4 e^{-2 a4} s,
  -b4 e^{-2 a4} s) with s = sin^{1/3} z and b4(x4) > 0.
- "Chapter n" means `Revision/textbook/chapters/nn-*.md`.

For each task the original assignment is quoted in one line, followed by what exists now, the formulation and
what to send back.

### K1. gate (stage5-docs-prep): the gate of the old Stage 5

Original task: write the Stage-5 gate twins `scripts/verify_stage5_pair_creation.ps1` and `.sh` (and their
audit helper and test), following the Stage-3/4 gate pattern.

What exists:

- The twins, `scripts/verify_stage5_pair_creation_audit.py` and `tests/test_d16c_stage5_gate.py` were
  written by the killed agent. Claude filled their 5 empty time placeholders on 2026-10-15 (0025743).
- The test passes 13 of 13.
- `--dry-run` lists 30 steps, stage5-00 to stage5-29.

Formulation. The gate is the conjunction G = P_00 and P_01 and ... and P_29 of the step predicates. Each P_s
is "the command of step s exits 0 and prints its OK line". The task by hand is to establish, for every step s,
one of three facts:

- (i) P_s holds now, by running the step;
- (ii) P_s cannot hold now, with the missing input named;
- (iii) the predicate is wrong (it can pass while its claim is false, or fail while its claim is true).

The claims are:

- **Theory (steps 01-05).** The four exact verifiers reproduce their committed reports byte for byte. The
  totals are Wolfram 00 46/46, Wolfram pairing 141/141, sympy 00 49/49 and sympy pairing 172/172; step 05 is
  `tree-same` of the fresh against the committed reports.
- **Rust (06-10).** `cargo fmt --check`, `cargo clippy -D warnings`, `cargo test` and `cargo build --release`
  pass, and `print-config` equals the committed configuration.
- **Stage-4 identity (11-13).** The Stage-4 spectrum, scf and excited runs are reproduced, and the identity
  report equals the committed one.
- **Pairs (14-17).** For every member j of the T1/T2 pair families, the Rust results of run-a and of the
  refined grid equal the committed ones. Determinism means byte identity of the canonical and repeat
  summaries; convergence means the refined-grid differences are within the grid-error terms of erratum E5.2.
- **Reference (18-20).** The quick run satisfies its summary checks, and the reproduce mode equals the
  committed reference within the tolerances of `ks_reference_pairs.py`.
- **Pairs checker (21-22).** `python-pairs-check-report.json` equals the committed report, and it contains
  the passing checks `rust_repeat_byte_identity` and `rust_refined_convergence`.
- **Figures (23-24)** are byte-identical; **PDFs (25-26)** build in verify mode; **unchanged (27)** means no
  committed path changed; **unit tests (28)** pass; **fresh outputs (29)**: every output was written by this
  run.

Known now (dry run, 2026-10-16): steps 15, 17, 21-24 cannot pass. Their committed inputs do not exist:

- `artifacts/dirac16complex/pair-creation/rust/pairs/summary.json`;
- `rust/determinism-report.json`;
- `python-pairs-check-report.json`;
- `scripts/build_dirac16complex_pairs_figures.py`;
- the folder `artifacts/dirac16complex/pair-creation/figures`.

These need the old-Stage-5 numerics killed on 2026-10-14 (A2, A3, A4), each longer than 423 s. Steps 25-26
need parts 2 of documents A and B.

Send back: for each step, (i), (ii) with the missing input, or (iii) with the reason.

### K2-K9. review:references and review:notebooks, chapter groups 00-05, 06-11, 12-17, 18-23

Original task: an adversarial review of the whole textbook with two lenses, references and notebooks, in four
chapter groups. Each finding was to be refuted or confirmed by two skeptics. The review was for findings only,
with no edits.

When to do it: after phase 9 is complete (Claude notifies the user). Until then the chapters change.

**References lens (K2 = 00-05, K3 = 06-11, K4 = 12-17, K5 = 18-23).** Let c be a chapter of the group and r a
reference in c of one of these kinds:

- "Section n.m";
- "Chapter n";
- "Figure NNx.k";
- "Notebook NNx";
- "In [k]" (of a named notebook);
- "Exercise n.m";
- a record file path;
- a record check name.

Define target(r):

- the heading "### n.m" of chapter n;
- the chapter file;
- the figure `figures/NNx_k_*.png` with its caption in `figures/NNx.captions.json`;
- the notebook `notebooks/NNx_*.ipynb`;
- its k-th code cell;
- the exercise heading;
- the file;
- the check entry with that name in the named report.

The task is to verify, for every r:

- (R1) target(r) exists;
- (R2) target(r) states what the sentence containing r attributes to it.

For a check name, R2 also requires the verdict PASS and that the detail text contains the quoted values. R1
can be done mechanically:
`python Revision/textbook/tools/assemble_textbook.py --allow-missing --output <scratch>/book.md` prints every
unresolved book reference. R2 needs reading.

Send back: the list of r with R1 or R2 false, and for each the quoted sentence, the target and what it says.

**Notebooks lens (K6 = 00-05, K7 = 06-11, K8 = 12-17, K9 = 18-22).** For every chapter c of the group:

- (N1) every notebook NNx named in c exists, together with its builder `notebooks/src/NNx_*.py` and its
  `notebooks/NNx_*.PROVENANCE.md`;
- (N2) before each notebook the chapter has a complete run-instruction paragraph (never "see Section ..."),
  and after it a walk-through of every code cell;
- (N3) c has at least 4 figures (chapter 00 excepted);
- (N4) every figure NNx.k is referenced in the text, and its caption in the chapter equals the entry k of
  `figures/NNx.captions.json`;
- (N5) `python Revision/textbook/tools/audit/walkthrough_diff.py <chapter> <notebook> <id>` reports nothing
  except the known conventions;
- (N6) `python Revision/textbook/tools/nbkit.py lint <builder>` prints `nbkit=OK`.

The known conventions of N5 are:

- the set-up cell In [1] is explained by reference;
- figure captions are shortened with `...)`;
- docstrings are omitted.

Send back: each (c, notebook, Nk) that fails, with the evidence.

### K10. errata-writer: the E5.1 entries of the first-edition errata list

Original task: add a section "(g) The quantum reading of the T1 corollary (Stage-5 erratum E5.1)" to
`provenance/ERRATA_FIRST_EDITION_TEXTBOOK.md`. Each entry quotes the first edition exactly. The test
`tests/test_d16c_textbook_publication.py` must pass.

What exists: nothing. The errata list has sections (a) to (f) only; the agent made no edit.

The mathematics of E5.1 (`handoff/specs/STAGE5_SPEC.md`, section 9):

- Let Psi_- = gamma^8 Psi_+, where gamma^8 means Gamma. Classically, for c-number fields, the T1 corollary
  holds: T[Psi_-; -m, -lambda] = -T[Psi_+; m, lambda] and Q[Psi_-] = -Q[Psi_+].
- So the configuration Psi_+ together with Psi_- has total energy, charge and energy-momentum tensor zero:
  X + (-X) = 0.
- For the quantised field with {Psi(x), Psi^dagger(y)} = B delta(x - y), the same relations hold as operator
  identities. But the image field has the anticommutator -B and is the same quantum system:
  - [Psi_-, H[Psi_-; -m]] = -h(-m) Psi_-;
  - [Psi_-, Q[Psi_-]] = -Psi_-.
- So the generators of the image field are +H_+, +Q_+ and +T_+.
- The values -|eps| and -1 per quantum are the values of the formulas L_{-m,-lambda}, not the energy and
  charge of the image field's own quanta.
- No reading gives a cancellation between two independent, consistently quantised universes.

The task:

- (E1) Find every statement S of the first edition (`provenance/DIRAC16COMPLEX_TEXTBOOK.md`; the reviewer named
  its chapters 15, 16, 17, 19 and 20) that asserts any of the following:
  - quanta of the image field with energy -|eps| or charge -1 as their own;
  - cancellation of the pair's energy or charge at the quantum level;
  - pairs of universes with zero total energy as quantum objects.

  Search terms: "-|", "charge -1", "cancel", "total energy", "pair of universes", "Krein", "image".
- (E2) For each S (or a tight group), write an entry in the format of sections (a)-(f):
  - the location: chapter file, section, line of the assembled book;
  - the old statement, quoted character for character from that line;
  - the correction, stating E5.1 as above and nothing more;
  - the kind: CONTRADICTED, OUT OF DATE, INCOMPLETE or AGREES;
  - the sources: STAGE5_SPEC E5.1; `artifacts/dirac16complex/pair-creation/pairing-theory.json` keys
    `T1krein` and `T1.corollaryPair`; `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md` section 7.3;
    `Revision/docs/PAIR_CREATION_PROOFS.md` section 11.3; and the successor book's sections that state the
    corrected reading (Chapter 18, "T1 and charge conjugation" and the corollary; Chapter 20, the answer in
    brief, item 3).
- (E3) Update the paragraph "When the first edition was built" if it lists later corrections.
- (E4) `python -m unittest tests/test_d16c_textbook_publication.py -v` passes.

Send back: the list of S with line numbers and the proposed entries, or the edited file.

### K11. verify:05: the fixes of chapter 05

Chapter 05 is final for b4 (commit 4618073). Two items are to be checked.

**(a) Wording.** The purpose text of builder `notebooks/src/05a_c_gamma_b.py` (line 32), the three copies in
`05a_c_gamma_b.ipynb` and lines 10 and 42 of `05a_c_gamma_b.PROVENANCE.md` must not call a numerical check a
proof. Criterion:

- the phrase "proves numerically" occurs nowhere in chapter 05 or its builders and notebooks;
- the new phrase "checks again with its own code ... (COMPUTED here, partly in exact whole-number arithmetic
  and partly in floating-point numbers, while the record proves them exactly)" is true of the code of 05a. That
  is, 05a's checks are integer/sympy-exact or floating-point, and the record's checks of the same properties
  are exact.

**(b) Section 5.23 (I), the time-like case.** Let v be a unit vector with space part sigma (components along
x0..x3) and time part tau (along x4..x7) and |tau|^2 - |sigma|^2 = 1. Use rule (E) of 5.23 for a generator
S^{ab}:

- a boost moves e_a to cosh(theta) e_a - eta_aa sinh(theta) e_b;
- a rotation moves e_a to cos(theta) e_a - eta_aa sin(theta) e_b.

Verify the following:

1. (b1) For the boost in the plane (x4, x0), with a = x4 (eta_aa = -1) and b = x0, Lambda e_x4 =
   cosh(theta) e_x4 + sinh(theta) e_x0. With sinh(theta) = |sigma|, cosh(theta) = sqrt(1 + |sigma|^2) = |tau|.
   This uses |tau| = sqrt(1 + |sigma|^2), which follows from the normalisation, and needs |tau| >= 1.
2. (b2) Three rotations in the planes (x0, x1), (x0, x2), (x0, x3) carry e_x0 to sigma/|sigma| and leave e_x4
   fixed, so |tau| e_x4 + |sigma| e_x0 goes to |tau| e_x4 + sigma. Give the three angles explicitly. Each
   rotation puts the right component on its other axis and keeps the remaining length on e_x0.
3. (b3) Three rotations in (x4, x5), (x4, x6), (x4, x7) carry e_x4 to tau/|tau| and leave the space part
   fixed, giving sigma + tau = v. These rotations are allowed: each of these planes has eta_aa eta_bb = +1, so
   the generator gives circular functions.
4. (b4) With h the product of the at most seven exponentials, h is even, so h gamma^(x4) h^{-1} =
   sum_d Lambda(h)_{d,x4} gamma^d = gamma(v).
5. (b5) If sigma = 0, theta = 0 and the middle stage is empty; the chapter says so.
6. (b6) The same three stages are what notebook 05f checks. Its function `turn_factor('x4', 'x0', tau, sigma)`
   gives arcsinh(|sigma|), and its order of stages is the same. The chapter text and 05f section 4 (I) agree
   word for word in content.

Send back: true or false for (a) and each of b1-b6, with the reason for any false one.

### K12. verify:07: the fixes of chapter 07

Chapter 07 is final for b4 (commit 7d35de1). Two items are to be checked.

**(a) Normal ordering, Section 7.29, the paragraph after the sign table.** Let X be a bilinear operator that
changes under the conjugation as X -> s X + c, with a sign s and a number c (c is the change of the vacuum
value). Let :X: = X - <0|X|0>. Verify:

- :X: -> s :X:, because the number c cancels in the difference. Normal ordering therefore adds no sign.
- The text attributes exactly this to the record: `Revision/lead_checks/reports/charge-conjugation-and-u1.json`,
  check `bilinears_under_charge_conjugation`, detail text "normal ordering adds no sign ...".
- The pointers are correct: Section 5.34 derives both statements; Sections 10.15 and 21.25 derive the second
  (the quantised conjugation Psi -> Gamma Psi^{dagger T} preserves {Psi, Psi^dagger} = B delta and reverses
  the mass); Section 21.26 confirms the first for the charge.

**(b) Section 7.23, "What 'self-consistent' means".** Verify:

- (b1) The six senses (i)-(vi) are those of `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md`, section 8.
- (b2) Each sense cites existing PASS checks. These are `adjoint_equation_is_Dirac_conjugate_G`,
  `grassmann_adjoint_equation_is_conjugate`, `evolution_form_G`, `extra_time_growth_rates_unbounded`,
  `Lichnerowicz_identity_G`, `lichnerowicz_identity_on_fields`, `lichnerowicz_contraction`,
  `current_conservation_identity_G`, `grassmann_current_conservation`,
  `Noether_identity_diffeomorphisms_G`, `Noether_identity_local_Lorentz_G`, `conservation_on_shell_general`,
  `exact_solution_x4_x0_G` and `exact_solution_family_x4_x0`, in `Revision/theory/reports/`.
- (b3) The line-by-line integrability argument: gamma^nu D_nu (gamma^mu D_mu Psi) = gamma^nu D_nu (m Psi) =
  m gamma^nu D_nu Psi = m^2 Psi for U = 0, so every solution obeys (gamma^mu D_mu)^2 Psi = m^2 Psi.
- (b4) The scalar curvature quoted with the Lichnerowicz identity is R = 6 a4'^2 - 3 a4' b4'/b4 +
  3 b4''/b4 - 42 H^2. On the history a4 = A H x4, b4 = b4(0) e^{(4/3) A H x4} it gives R = (2/3) H^2
  (11 A^2 - 63), which is -104/3 H^2 at A = 1. Insert a4' = A H, b4'/b4 = (4/3) A H and b4''/b4 = (16/9) A^2 H^2.
- (b5) In flat 4+4 space (D = partial, no Christoffel symbols, R = 0) the identity reduces to
  (gamma^(a) partial_a)^2 = sum_a eta^{aa} partial_a^2.
- (b6) The definition is kept apart from the Kohn-Sham meaning (a fixed point of the density-potential map,
  Chapters 13-15), and the plain-word summary is labelled as the book's own.

Send back: true or false for a and b1-b6.

### K13. verify:11: the fix of chapter 11 (Section 11.20)

The fixer wrote out every diagonal component of E_(1), E_(2), E_(3) at the moment a4' = 2H, a4'' = H^2. The
current values are:

- E_(1): 3, 4, 33, 2;
- E_(2): 684, 548, -1476, 820;
- E_(3): -22392, -14544, 40248, -30240;

each in units H^{2k}, for x0, x1, x4, x5.

When to do it: chapter 11 is moved to b4 in phase 9. The Lovelock tensors then depend also on u = b4'/b4 and
v = u', and the hand computation of 11.20 will be redone for the moment of the history (u = (4/3)H, v = 0) or
stated at constant b4. Claude will update this formulation then.

The formulation as it will apply: for each component, insert the powers of a4' (and of u), multiply out each
coefficient of `Revision/field_equations_a4/results/a4-equations.json` (key `lovelockTensors`), and add. The
criterion is that each written line is arithmetically correct and equals the printed output of Notebook 11b,
In [23].

### K14. verify:15: the fixes of chapter 15 (Section 15.2, 15.15, 15.31; builder 15b)

When to do it: chapter 15 is moved to the Kohn-Sham record with b4 in phase 9. The numbers of the tip-cutoff
study changed with that record (rerun on 2026-10-16), so the checks below are stated against the record files,
not against numbers. The record files are:

- `Revision/kohn_sham/tip_convergence/README.md` (sections 3, 4, 6, 9);
- `tip-convergence.json`;
- `tip-convergence-table.csv`;
- `tip-convergence-extrapolation.csv`.

Let d_i = |x(L_{i+1}) - x(L_i)| on the grid L = 3, 3.5, 4, ...

- (a) The rule of a geometric tail as the chapter states it equals README section 3. That is, the last two
  ratios d_{i+1}/d_i lie in (0, 0.5). The chapter states that this condition was made stricter once, after
  the first analysis, as README section 9 says, and names the state that changed its verdict.
- (b) The series used is the unbroken run of converged L from L = 3 (it ends before the first failure), as in
  `analyse_series` of `tip_convergence.py`. For each state the chapter calls "not established", the table CSV
  shows a failure before three converged values or a run without a geometric tail.
- (c) The noise floor is U(x) = (16/15)|x(h/2) - x(h)| + 1e-11 max(1, |x|), as in `noise()`.
- (d) Every factor "about q times its value at L = 3" in 15.2, 15.15 and 15.31 equals the ratio of the CSV
  values to two digits. Where the limit is not established, the text says "at L = L_max", not "at large L".
- (e) The N = 8 number in 15.31 is named E_KS (the Kohn-Sham energy), not the interaction energy E_int
  (verify:16 finding 1).
- (f) The OPEN parenthesis of 15.31 on the large-L limit names every case: the states whose E_KS limit is not
  established, and the quantities other than E_KS that are not converged in further interacting states, as
  README section 6 lists them (verify:16 finding 2).
- (g) The word list of 15b, "Conservation law", is consistent with Section 20.22 (d). It must say:
  nabla_mu T^mu_nu = 0 is a local balance law; the energy of a universe is not conserved in the author's x4-
  and z-dependent metric; constant totals hold only for the momenta along x1, x2, x3, x5, x6, x7 under the
  ASSUMED boundary conditions.

Send back: true or false for a-g with the values used.

### K15. verify:17: the fixes of chapter 17

When to do it: after chapter 17 is moved to b4 in phase 9. Verify:

- (a) The record has 75 ground states (T = 0) and 135 thermal states. This is
  `Revision/kohn_sham/reports/ks-crosscheck.json`, matrix "ground": 75 and "thermal": 135, true on
  2026-10-16.
- (b) Only the ground states store profiles. These are the profile folders of `Revision/kohn_sham/results/`;
  `results/thermo` holds `thermodynamics.csv` only.
- (c) The source-condition checks of `Revision/field_equations_a4/reports/ks-source-conditions.json` use only
  the 75 ground-state profiles.
- (d) Every place of chapter 17 and builders 17a and 17b that speaks of "the recorded states" says "ground
  states", or is covered by the definition in Section 17.7.
- (e) The OPEN list of 17.23 contains the evolution after a turning point and the six 3-momentum series that
  are not integrated (as in 17.17).
- (f) "T" for the temperature is not confused with the energy-momentum tensor T. The text writes "zero
  temperature".

Send back: true or false for a-f.

### K16. verify:18: the fixes of chapter 18

Mathematics, independent of b4. Verify:

**(a) Section "T1 and charge conjugation".** With :X: = X - <0|X|0> and X -> s X + c (K12 a), the quantised
field keeps (S, J) -> (-S, +J) under the same-mass conjugation C_+. Normal ordering adds no sign; the old text
"(S, -J) after normal ordering" is gone. The citations are `charge-conjugation-and-u1.json`, check
`bilinears_under_charge_conjugation`, and Sections 5.34 and 21.26.

**(b) Introduction.** Q is stated with its hypotheses: identical one-particle spectra of the lambda = 0
problem, in flat 4+4 space or with frozen coefficients at a point, as in `PAIR_CREATION_PROOFS.md` section
11.3.

**(c) Lemma 1, the adjoint half.** For Psi-bar = Psi^dagger C and the spinor connection Omega_mu:

- D_mu(Psi-bar Gamma) = partial_mu(Psi-bar Gamma) - Psi-bar Gamma Omega_mu
  = (partial_mu Psi-bar) Gamma - Psi-bar Omega_mu Gamma
  = (D_mu Psi-bar) Gamma.
- The middle step needs Gamma Omega_mu = Omega_mu Gamma. This holds because Omega_mu is a sum of products of
  two gammas and Gamma anticommutes with each gamma.

**(d) T2 Step 7.** From Step 4, gamma^(n) gamma'^rho gamma^(n) = -eta_nn gamma^rho. Multiply by g_{mu rho},
which the reflection leaves unchanged (Step 1), and sum: gamma^(n) gamma'_mu gamma^(n) = -eta_nn gamma_mu.
Then:

- overline(gamma^(n) Psi) gamma'_mu D'_nu (gamma^(n) Psi) = eta_nn Psi-bar gamma_mu D_nu Psi;
- (D'_mu overline(gamma^(n) Psi)) gamma'_nu (gamma^(n) Psi) = eta_nn (D_mu Psi-bar) gamma_nu Psi.

Each line uses three facts: the adjoint of gamma^(n) Psi, the lemma D'_nu(gamma^(n) Psi) = gamma^(n) D_nu Psi,
and the identity above. Inserted, with g', sqrt|g'| and Step 5, into the T_{mu nu} formula of Section 18.4,
they give T'_{mu nu} = T^{(-m, lambda)}_{mu nu}[Psi]. The book's tensor in Section 18.4 is minus that of
Chapter 9; check that the signs are used consistently.

**(e) Grep.** No other place of chapter 18, builders 18a-18c, PROVENANCE files or captions has "(S, -J)
after normal ordering".

Send back: true or false for a-e.

## How the user's results come back

For each task, send the list of "true/false with reason" (or the edited file for K10). Claude then applies
every confirmed correction in the files it concerns, checks it like any other edit, records it in section 1.6,
and commits and pushes.
