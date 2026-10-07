# Provenance: the Stage-5 pairing verifier `scripts/verify_dirac16complex_pairing.wls`

This file describes one **WolframScript set** of the repository
<https://github.com/once-ere/Dirac_claude>: the script
`scripts/verify_dirac16complex_pairing.wls` together with the Wolfram package it loads,
`wolfram/Dirac16ComplexPairing.wl` (which in turn loads `wolfram/Dirac16ComplexGeometry.wl`).
In the project history it is the exact verifier of **Stage 5** (the "{+M, -M} pairing"
stage). It is written for a student who has never used Wolfram or a command line before.
Everything needed to run the set is in this file; you do not have to open any other file.

The file has six parts: (1) what the set is and what it computes, (2) its files,
(3) complete instructions to run it, (4) the expected output, (5) the side effects,
(6) the verification record (what was actually run on 2026-10-02, and what came out).

---

## 1. What the set is and what it computes

### 1.1 In plain words

The project studies a 16-component complex spinor field in an eight-dimensional spacetime
with four "space-like" and four "time-like" directions (signature (4,4); the coordinate
x4 is the time). There are two versions of the field:

* **dirac16complex**: the components are *anticommuting* (Grassmann) numbers, as for
  electrons; this is the quantum field (it is quantised in a so-called Krein space).
* **dirac16complex00**: the components are ordinary *commuting* complex numbers (a
  classical field).

The question behind Stage 5 is whether a universe of mass **+M** and a universe of mass
**-M** can be created *as a pair* (for example at x4 = 0, "the big bang"), so that the
pair as a whole carries no energy, no momentum and no charge. The set does not simulate
anything. It **proves exact algebraic identities** (theorems) by computer algebra and
records, for each identity, `true` or `false`. No floating-point (decimal) number ever
decides a check: all arithmetic is with integers, fractions, complex fractions and exact
symbolic expressions, and a check is true only if an expression is *exactly* zero.

The theorems that are checked:

* **T1, the chirality map.** Multiply the field by the 16 x 16 matrix gamma^8 (the
  product of all eight gamma matrices) and at the same time reverse the sign of the mass
  m and of the self-coupling lambda. Then the Lagrangian, the field equation, the
  energy-momentum tensor T_{mu nu} (all components) and the current j^mu all change sign.
  Hence the pair "field with (m, lambda)" plus "its gamma^8 image with (-m, -lambda)" has
  total T_{mu nu} = 0 and total charge 0, in **every** gravitational field. This is
  checked (a) as a polynomial identity in completely general symbols, (b) with exact
  numbers at three points of a general curved geometry, including the field equations
  on shell and energy-momentum conservation, (c) for anticommuting components with an
  exact Grassmann algebra of 288 generators, and (d) in the primordial gravitational field
  of the project with an arbitrary function a4(t).
* **T1 at the quantum (Fock-space) level** (checks `PAIR_T1krein_*`): an exact finite
  model with four fermionic modes shows that the gamma^8 image of the quantum field has
  the reversed canonical anticommutator (-B instead of B, "Krein metric reversed").
* **T2, the mirror map.** A reflection of one space-like frame direction (a Pin(4,4)
  element of "character -1") maps (m, lambda) to (-m, lambda) with the *same* lambda; here
  the energy-momentum is the *same* for both members, so in this pair it doubles instead
  of cancelling. Also checked: the reflection y -> -y of the hidden coordinate in the
  Z2-symmetric primordial field (checks `PAIR_T2z2_*`).
* **T3, the Kohn-Sham level.** The same maps for the "DFT-type" mean-field (Kohn-Sham)
  model of Stage 4: the maps on the eight 2 x 2 blocks, the Kohn-Sham equations and the
  energy functional, exact zero-mode spectra, how the boundary conditions must transform,
  and a control showing that the pairing fails if the boundary conditions are *not*
  transformed.
* **Statistics** (checks `PAIR_stat_*`): changing from anticommuting to commuting
  components changes only the sign of the exchange term; the effective mass is
  M_eff = m + (15/16) lambda S for dirac16complex and m + (17/16) lambda S for
  dirac16complex00.
* **Pair totals** (checks `PAIR_totals_*`): the totals of both kinds of pairs, at the field
  level and at the Kohn-Sham level.

The run ends with **141 checks**. Grouped by the first part of their names:

| Group (check-name prefix) | Checks | What it covers |
| --- | ---: | --- |
| `PAIR_algebra_` | 10 | the gamma matrices, gamma^8, C and B and their properties |
| `PAIR_T1generic_` | 9 | T1 as an identity in generic symbols (every gravitational field) |
| `PAIR_T1grassmann_` | 7 | T1 for anticommuting (Grassmann-odd) components |
| `PAIR_T1jets_` | 13 | T1 with exact numbers in a general curved geometry |
| `PAIR_T1krein_` | 12 | T1 at the quantum level (exact four-mode Fock model) |
| `PAIR_T2frame_` | 12 | T2: frame reflections |
| `PAIR_T2z2_` | 11 | T2: the reflection y -> -y in the primordial field |
| `PAIR_T1primordial_` | 6 | T1 in the primordial field |
| `PAIR_T3block_` | 18 | T3: the maps on the 2 x 2 blocks of Stage 4 |
| `PAIR_T3ks_` | 19 | T3: Kohn-Sham functional, spectra, the control |
| `PAIR_T3emt_` | 6 | T3: the energy-momentum tensor of a Kohn-Sham orbital |
| `PAIR_stat_` | 13 | the statistics sign of the exchange term |
| `PAIR_totals_` | 4 | the pair totals |
| `PAIR_internal_` | 1 | no internal error occurred |
| **total** | **141** | |

What the set does **not** do (stated in its own output file `pairing-theory.json`,
key `notProved`): it derives no rate, amplitude or probability of pair creation and no
wave function of the universe; it shows that such a pair is *consistent* with every
conservation law, not that it *is* created.

**Known open issue in the wording of one output entry.** All twelve `PAIR_T1krein_*`
checks are true, but the physical reading written into the entries
`T1krein.imageField` and `T1krein.consequence` of `pairing-theory.json` ("the image
universe carries energy -|eps| and charge -1 per quantum", "T^pair = 0 at the operator
level") was found to be wrong by the later matter-antimatter analysis: under the image
field's own anticommutator (-B) those operators are *minus* its energy and *minus* its
charge. The repository's hand-over notes (`HANDOFF.md`, section 0.4, item C) record that
this text must be corrected in `wolfram/Dirac16ComplexPairing.wl` (and in the independent
Python checker) before the Stage-5 documents are written, and the textbook cites the
result as provisional. This is a matter of interpretation, not of execution: the
committed files are reproduced exactly as they are (Part 6).

This set is the *old* Stage-5 verifier. The revised project has a separate, newer pairing
set (`Revision/pairing/wolfram/verify_pairing.wls`, outputs under `Revision/pairing/`);
the two must not be confused.

### 1.2 Which documents and programs use its results

Documents that cite its check counts, its results or its files:

* `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (and `.tex`, `.pdf`), assembled from
  `provenance/textbook/chapters/`: mainly Chapter 15 "The pairing theorems", Chapter 16
  "Does the big bang create universes in pairs?", Chapter 19 "Reproducing everything"
  (Section 19.10, the table "141 of 141" and the re-run commands) and Chapter 20 (the
  index of every check); also Chapters 0, 6, 7, 9, 13, 14, 17 and 18.
* `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md` (and `.tex`, `.pdf`): Section 7.3,
  Section 11.4 "Stage-5 inputs", Section 11.5 (which records the sha256 of both output
  files) and Section 12 (reproduction).
* `handoff/specs/STAGE5_SPEC.md` (the specification of Stage 5) and `HANDOFF.md`.
* `handoff/specs/MATTER_ANTIMATTER_SPEC.md` (line 54: `pairing-theory.json`, checks
  `PAIR_T1krein`) and `studies/dirac16complex_kohn_sham/README.md` (lines 330 and 352:
  `pairing-theory.json`, entries `statistics.hartreeFock` and `T3.numericsPrescription`).
* In comments only (these programs cite formulas of `pairing-theory.json` but do not open
  the file): `scripts/ks_reference_solver.py`,
  `studies/dirac16complex_kohn_sham/src/exchange.rs` and
  `studies/dirac16complex_kohn_sham/src/shooting.rs`.

(The files under `Revision/` that mention a `pairing-theory.json`, among them the
textbook notebooks `Revision/textbook/notebooks/10a_krein_spectra`, `10b_canonical_krein`
and `src/18a_pairing_matrices.py`, refer to the different file
`Revision/pairing/pairing-theory.json` of the newer set, not to the output of this set.)

Programs and tests that **read** the output files (so the outputs must stay exactly as
committed):

* `scripts/check_dirac16complex_pairing.py` (the independent sympy checker; it compares
  its own results with `pairing-theory.json` and `wolfram-pairing-report.json`),
  `scripts/check_dirac16complex_pairs.py`, `scripts/ks_reference_pairs.py`,
  `studies/dirac16complex_kohn_sham/src/pairs.rs` (the Rust solver's `pairs` subcommand).
* `scripts/verify_dirac16complex_matter_antimatter.wls` with
  `wolfram/Dirac16ComplexMatterAntimatter.wl`, and
  `scripts/check_dirac16complex_matter_antimatter.py`.
* The unit tests `tests/test_d16c_stage5_pairing.py` (lines 245-273: it opens both
  committed outputs, compares them with the independent sympy checker and checks that a
  changed copy is detected) and `tests/test_d16c_stage5_pairs.py` (line 32 names
  `pairing-theory.json`; lines 283-284 read it).
* The sha256 values of both outputs are pinned in
  `artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json`,
  `wolfram-matter-antimatter-report.json`, `python-matter-antimatter-report.json`,
  `artifacts/dirac16complex/pair-creation/python-pairing-report.json`,
  `artifacts/dirac16complex/pair-creation/reference/reference-pairs-summary.json`,
  `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md`,
  `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.tex` and the provenance file of the
  matter-antimatter set, `provenance/wolframscript/verify_dirac16complex_matter_antimatter.PROVENANCE.md`
  (apart from this provenance file, these eight files are exactly the files of the
  repository that contain either sha256 value; `git grep` at the verified commit of
  Part 6); the unit tests
  `tests/test_d16c_matter_antimatter_publication.py` and
  `tests/test_d16c_textbook_publication.py` (which pins the count 141) check them.

---

## 2. The files of the set

All paths are relative to the root folder of the repository (the folder that contains
`README.md`). Line counts are the number of line-feed characters; every file uses LF
line endings only (the repository's `.gitattributes` line `* -text` keeps every file
byte for byte as committed, on every operating system).

### 2.1 Programs

| File | Role | Lines | Bytes | sha256 |
| --- | --- | ---: | ---: | --- |
| `scripts/verify_dirac16complex_pairing.wls` | the script you run; reads the command line, loads the package, writes the two JSON files, prints the verdict, sets the exit code | 76 | 4969 | `92f9864281d9b11c54ce3c9a053ff28dc2b604fbe775e998018fb844a16b3bbb` |
| `wolfram/Dirac16ComplexPairing.wl` | the package with every check (function `D16PairRun`) | 1236 | 125941 | `d2192ed8ea39e7fb3a2c74f4b62de647fa92c6ba8c91ee60df566282bbca1462` |
| `wolfram/Dirac16ComplexGeometry.wl` | the Stage-1 exact geometry package (curved-space geometry, Lagrangian, energy-momentum tensor as exact "jets"; reproducible exact random numbers from a fixed 64-bit generator), loaded by the package above; it reads and writes no file | 997 | 71636 | `f5b674665eee4000750161e6ab6312c38bfac9da7a17450a2b3bdd88ef292af2` |

### 2.2 Inputs (read, never changed)

| File | Produced by | Lines | Bytes | sha256 |
| --- | --- | ---: | ---: | --- |
| `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` | `scripts/build_dirac16complex_fixture.py` (Stage 1): the exact gamma matrices, C, B, the chirality matrix and the spin matrices | 18440 | 213133 | `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b` |
| `artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json` | `scripts/verify_dirac16complex_kohn_sham.wls` (Stage 4): the exact 2 x 2 block basis of the Kohn-Sham problem | 4537 | 72176 | `5b150b36e13b903c32b86e8debbaeda48798e0beb0bc6a216e416d2671f4e01a` |

The report written by the run records the sha256 of the two programs above, of the
geometry package and of these two inputs (key `sourceSha256`), so you can always see
which files produced it.

### 2.3 Outputs (written by every run)

With the command of Part 3 the two outputs are written over the committed files, also
when checks fail (only the two `FATAL` cases of Section 4.2 write nothing):

| File | Content | Lines | Bytes | sha256 of the committed file |
| --- | --- | ---: | ---: | --- |
| `artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json` | the report: `schemaVersion`, `producer`, `checks` (141 names, each `true` or `false`), `measurements` (19 values), `sourceSha256` | 184 | 8141 | `735534de950c7fb0327370c33caa275cf805aa91a41dee903e4eaec7a6fa0de8` |
| `artifacts/dirac16complex/pair-creation/pairing-theory.json` | the exact theory: every map, formula, statement and proof sketch (keys `conventions`, `algebra`, `T1krein`, `T2frameTable`, `T2z2`, `T3blockMaps`, `statistics`, `T1`, `T2`, `T3`, `pairTotals`, `notProved`, `notebookHypothesis`), read by the other programs listed in Section 1.2 | 851 | 57027 | `5a267bd696391b131134577ccdcf7766b83f96f3eb32b9b8de60c9175b1ebf6a` |

Both files are plain ASCII JSON with LF line endings and a final line feed, indented with
tab characters, and contain no time stamps, so two runs give the same bytes. The script
always writes `pairing-theory.json` into the **same folder** as the report, whatever report
path you give.

---

## 3. Complete instructions to run the set

### 3.1 What you need

* A computer with Windows 10 or 11, macOS, or Linux (64-bit).
* About 1 GB of free memory (RAM; the kernel's measured peak, Part 4.5, is below
  700 MiB, that is about 0.7 GB) and about 1 GB of free disk space (the clone of the repository is about
  660 MiB in total: about 465 MiB of files plus about 195 MiB of git history in the
  hidden folder `.git`, which is also about the size of the download; measured on a
  fresh clone of the verified commit of Part 6: 691,412,010 bytes = 659.4 MiB, of which
  `.git` is 204,159,619 bytes = 194.7 MiB; the repository grows with every commit, so a
  later clone is larger).
* An internet connection for the installation and for downloading the repository. The run
  itself needs no network.
* About 5 to 10 minutes of time for one run (Part 4.5 gives the measured times: 4 to 8
  minutes).
* The Wolfram Language: either the **free Wolfram Engine for Developers** or an installed
  **Mathematica / Wolfram** desktop product. Both contain the command-line program
  `wolframscript`, which is what you use.
* `git`, to download the repository.

### 3.2 Install the Wolfram Language and activate `wolframscript`

**Option A: the free Wolfram Engine for Developers.**

1. Open <https://www.wolfram.com/engine/> in a web browser and click the download button.
   You need a free Wolfram ID (an account at <https://account.wolfram.com>); create one if
   you do not have one, and accept the licence terms of the free Wolfram Engine for
   Developers (<https://www.wolfram.com/developer-license>; the free licence is for
   non-production use such as learning).
2. Install it:
   * **Windows**: run the downloaded `.exe` installer and accept the defaults. It installs
     the Wolfram Engine and WolframScript and adds `wolframscript` to the PATH (normally
     `C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe`). Close and re-open
     PowerShell afterwards so that the new PATH is used.
   * **macOS**: open the downloaded `.dmg`, drag the Wolfram Engine application into
     `Applications`, and open it once from `Applications`; this normally makes
     `wolframscript` available in the Terminal. If a new Terminal window still answers
     `wolframscript: command not found`, use the full path of the program inside the
     application instead of the word `wolframscript`, for example
     `"/Applications/Wolfram Engine.app/Contents/MacOS/wolframscript"` (look in
     `Applications` for the exact name of the application of your version).
   * **Linux**: in a terminal, in the download folder, run
     `sudo bash WolframEngine_*_LINUX.sh` (use the exact file name you downloaded) and
     accept the defaults; it installs `wolframscript` (normally `/usr/local/bin/wolframscript`).
3. Activate it once. Open a terminal (Windows: "PowerShell"; macOS: "Terminal"; Linux: any
   terminal) and type

   ```
   wolframscript
   ```

   The first time, it asks for your Wolfram ID (e-mail address) and password and
   activates the engine on this computer (this needs the internet). When the prompt
   `In[1]:=` appears, type `Quit[]` and press Enter. (Instead you can type
   `wolframscript -activate`.)

**Option B: Mathematica or the Wolfram desktop application** (if you or your university
already have it). The installer includes `wolframscript` and activates it with the
product: on Windows it is `C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe`;
on macOS it is inside the application, for example
`/Applications/Wolfram.app/Contents/MacOS/wolframscript` (older versions:
`/Applications/Mathematica.app/Contents/MacOS/wolframscript`); on Linux it is in the
`Executables` folder of the installation (the installer normally also links it into
`/usr/local/bin`). If typing `wolframscript` in a terminal gives "not found", use this full
path instead of the word `wolframscript` in every command below.

**Test the installation.** In the terminal type (the single quotes are needed in
PowerShell and in macOS/Linux shells alike):

```
wolframscript -code '1+1'
wolframscript -code '$Version'
```

The first prints `2`. The second prints the version, for example
`15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)` (the set was verified with
15.0.1; see Part 4.6 about other versions).

### 3.3 Install git and download (clone) the repository

1. Install git:
   * **Windows**: download and install "Git for Windows" from <https://git-scm.com/download/win>
     (accept the defaults).
   * **macOS**: in Terminal run `xcode-select --install` (or, with Homebrew, `brew install git`).
   * **Linux**: `sudo apt install git` (Debian, Ubuntu) or `sudo dnf install git` (Fedora).
2. Download the repository into a folder with a **short path**. Some file paths inside
   the repository are up to 117 characters long, and Windows by default refuses paths
   longer than 260 characters, so on Windows use a folder like `C:\src` and also run the
   first command below once.

   **Windows PowerShell:**

   ```
   git config --global core.longpaths true
   New-Item -ItemType Directory -Force C:\src
   cd C:\src
   git clone https://github.com/once-ere/Dirac_claude.git
   cd Dirac_claude
   ```

   **macOS and Linux (Terminal):**

   ```
   mkdir -p ~/src
   cd ~/src
   git clone https://github.com/once-ere/Dirac_claude.git
   cd Dirac_claude
   ```

   You are now in the **repository root**. Every command below is typed there.
   The newest version of the repository can differ from the one verified in Part 6.
   To get exactly the verified version, also type

   ```
   git checkout a4c5eda1df069a43a55ff8b57148f5de8edd1670
   ```

   (git then says it is in a "detached HEAD" state; that is harmless for running the
   set). With a newer version, first compare the sha256 of the five files of Sections 2.1
   and 2.2 with the tables (commands in Section 4.3); if they differ, the set was changed
   after this record and the expected output may differ.

### 3.4 Run the set

The command is one line and the same in every shell (type it in the repository root,
press Enter, and wait until it ends); the line after it prints the exit code:

**Windows PowerShell:**

```
wolframscript -file scripts/verify_dirac16complex_pairing.wls artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json
$LASTEXITCODE
```

**macOS and Linux (bash or zsh):**

```
wolframscript -file scripts/verify_dirac16complex_pairing.wls artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json
echo $?
```

The second line prints the **exit code** of the run: `0` means every check is true.

What the words mean: `wolframscript` starts a Wolfram kernel without a graphical
interface; `-file scripts/verify_dirac16complex_pairing.wls` tells it which program to run;
the last word is the path of the report to write (`pairing-theory.json` is written next to
it). Forward slashes `/` work in PowerShell too. A relative report path is taken relative
to the **repository root** (the script finds the root from its own location), not relative
to the folder you are in.

While it runs, the progress lines of Section 4.1 appear one after another; some steps
take a few minutes without printing anything, so be patient and wait until the prompt
returns. (If you send the output into a file with `>`: in PowerShell 7 (`pwsh`) the
file may stay empty until the run ends; Windows PowerShell 5.1 (the "Windows PowerShell"
that comes with Windows 10 and 11) fills it while the run proceeds but writes it in
UTF-16 (two bytes per character; open it with a text editor, not with tools that expect
ASCII); in bash it fills while the run proceeds. On Windows every printed line ends in
the two characters CR LF, in every shell.)

**Variant that leaves the committed files untouched.** Give a report path in the folder
`build/`, which git ignores; the folder is created if it does not exist:

```
wolframscript -file scripts/verify_dirac16complex_pairing.wls build/old-pairing/wolfram-pairing-report.json
```

This writes `build/old-pairing/wolfram-pairing-report.json` and
`build/old-pairing/pairing-theory.json`. Compare them with the committed files (both
commands print nothing and end with exit code 0 when the files are byte-identical; this
works in PowerShell and in macOS/Linux shells):

```
git diff --no-index --stat artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json build/old-pairing/wolfram-pairing-report.json
git diff --no-index --stat artifacts/dirac16complex/pair-creation/pairing-theory.json build/old-pairing/pairing-theory.json
```

**Do not put `--` before the report path.** WolframScript 1.14 drops `--` and everything
after it; the script then uses its default report path, which is the committed file.

### 3.5 If it fails

| What you see | Cause | What to do |
| --- | --- | --- |
| `wolframscript : The term 'wolframscript' is not recognized` (PowerShell) or `wolframscript: command not found` (macOS/Linux) | `wolframscript` is not installed or not on the PATH | re-open the terminal after installing; otherwise use the full path of Section 3.2, for example `& "C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe" -file ...` in PowerShell |
| a request for a Wolfram ID or password, or a message that the kernel could not be started or that no valid licence was found | the engine is not activated (or the activation expired) | run `wolframscript -activate` (Section 3.2) with an internet connection, then run again |
| within seconds: `Get::noopen: Cannot open ...\wolfram\Dirac16ComplexPairing.wl.`, then `FATAL: module failed to load: ...`, `check_count=0`, `failed_check_count=1`, exit code 1 (this exact output was produced on purpose during both verifications of Part 6, with the package renamed or moved out of the clone) | the package `wolfram/Dirac16ComplexPairing.wl` is missing | make sure the clone is complete: `git status` must print `nothing to commit, working tree clean` (`git status --porcelain` prints nothing); a line `deleted: <file>` names a missing file. Restore it with `git checkout -- <file>` or clone again. In this case the script stops before it writes anything, so the two output files are unchanged |
| at the start `Get::noopen: Cannot open ...\wolfram\Dirac16ComplexGeometry.wl.`, then very long Wolfram error messages (`Part::pkspec1`, `Part::partw`, `Set::shape`, ..., `General::stop`), many lines `CHECK FAILED: <name>`, after the line `done in <n> s` (just before the list of `check_` lines) `FileHash::noopen`, at the end `check_count=141`, `failed_check_count=29`, exit code 1 (measured during both verifications of Part 6 with this file moved away: 2.5 to 5 minutes, about 820 kB of printed text) | the geometry package `wolfram/Dirac16ComplexGeometry.wl` is missing (a damaged copy gives other error messages and false checks) | `git status` (it shows `deleted: wolfram/Dirac16ComplexGeometry.wl`), then `git checkout -- wolfram/Dirac16ComplexGeometry.wl`. The run has also overwritten the two output files with a failing report; restore them with `git checkout -- artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json artifacts/dirac16complex/pair-creation/pairing-theory.json` |
| Wolfram error messages that name `algebra-fixture.json` or `kohn-sham-theory.json` (`Import::nffil: File ... not found during Import.` and, after the line `done in <n> s`, `FileHash::noopen: Cannot open ...`), checks `false`, exit code 1. Measured during both verifications of Part 6: without `algebra-fixture.json` one line `CHECK FAILED: PAIR_algebra_fixtureMatches`, `check_count=141`, `failed_check_count=1`; without `kohn-sham-theory.json` a very long line `INTERNAL ERROR: ...`, `check_count=98` (the run stops checking after the step `T3 block maps`, so fewer than 141 checks are listed) and `failed_check_count=4` | an input file of Section 2.2 is missing or changed | `git status`, then `git checkout -- <file>` to restore it; compare its sha256 with Section 2.2. The run has also overwritten the two output files with a failing report; restore them with `git checkout -- artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json artifacts/dirac16complex/pair-creation/pairing-theory.json` (with the `build/` variant of Section 3.4 the failing report went to `build/old-pairing/` instead, and the committed files are unchanged) |
| lines `CHECK FAILED: <name>` and `failed_check_count=` larger than 0, exit code 1 | a check is false: either a file was changed or the Wolfram version computes something differently | compare the sha256 of the five files of Sections 2.1-2.2 with the tables; note your `$Version` and the names of the failed checks. The run has also overwritten the two output files with a failing report; restore them with `git checkout -- artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json artifacts/dirac16complex/pair-creation/pairing-theory.json` (not needed with the `build/` variant) |
| `error: unable to create file ...: Filename too long` during `git clone` (Windows) | the clone folder path is too long | run `git config --global core.longpaths true`, delete the partial clone, clone again into `C:\src` |
| the run stops with a message about memory, or the computer becomes very slow | not enough free memory | close other programs; Part 4.5 gives the measured peak memory |
| the report path you typed after `--` was ignored and the committed files were overwritten | WolframScript 1.14 drops `--` and what follows | give the path without `--`; restore with `git checkout -- artifacts/dirac16complex/pair-creation/` (Part 5) |
| everything is true but `git status` shows the two output files as modified | your Wolfram version writes the JSON slightly differently (for example the number formatting), or a source file differs | see Part 4.6; restore the committed files with the command of Part 5 |

---

## 4. Expected output

### 4.1 What is printed

The run prints 191 lines, in four blocks, and nothing on the error stream:

1. **26 progress lines**, each starting with the clock time `[hh:mm:ss]`: the name of each
   step when it starts and, for most steps, its duration (`... seconds: <n>`), ending with
   `done in <n> s`. Only these times and durations differ from run to run.
2. **141 check lines** `check_<name>=true`, one per check, in the same order as in the
   report. A check that fails prints `=false` here and, earlier, a line
   `  CHECK FAILED: <name>`.
3. **19 measurement lines** `measurement_<name>=<value>`; their values are exact and the
   same in every run.
4. **5 final lines**: `check_count=141`, `failed_check_count=0`,
   `elapsed_seconds=<n>` (the elapsed clock time of the checks, measured inside the
   kernel, in whole seconds) and the absolute paths of the two files written (with
   backslashes `\` on Windows and slashes `/` on macOS and Linux).

This is the complete expected output; `<n>` stands for a number of seconds and
`[hh:mm:ss]` for the clock time, which differ in every run; every other character is
exactly what the verification runs printed:

```
[hh:mm:ss] algebra
[hh:mm:ss] T1 generic symbols
[hh:mm:ss] T1generic seconds: <n>
[hh:mm:ss] T1 jets (G1) and Grassmann
[hh:mm:ss] T1jets seconds: <n>
[hh:mm:ss] T1 Krein-Fock model
[hh:mm:ss] T1krein seconds: <n>
[hh:mm:ss] T2 frame reflections (G1)
[hh:mm:ss] T2frame seconds: <n>
[hh:mm:ss] T2 Z2 coordinate action
[hh:mm:ss] T2z2 seconds: <n>
[hh:mm:ss] T1 in the Stage-2 primordial field
[hh:mm:ss] T1primordial seconds: <n>
[hh:mm:ss] T3 block maps
[hh:mm:ss] T3 KS functional
[hh:mm:ss] T3ks_functional seconds: <n>
[hh:mm:ss] T3 spectra and control
[hh:mm:ss] T3ks_spectra seconds: <n>
[hh:mm:ss] T3 EMT
[hh:mm:ss] T3emt seconds: <n>
[hh:mm:ss] statistics
[hh:mm:ss] stat seconds: <n>
[hh:mm:ss] pair totals
[hh:mm:ss] totals seconds: <n>
[hh:mm:ss] theory export
[hh:mm:ss] done in <n> s
check_PAIR_algebra_fixtureMatches=true
check_PAIR_algebra_clifford=true
check_PAIR_algebra_gamma8Properties=true
check_PAIR_algebra_CProperties=true
check_PAIR_algebra_BProperties=true
check_PAIR_algebra_gamma8InIdentityComponent=true
check_PAIR_algebra_gammaDaggerC=true
check_PAIR_algebra_bilinearParities=true
check_PAIR_algebra_chiralBlockStructure=true
check_PAIR_algebra_kreinUnderBasicReflections=true
check_PAIR_T1generic_nontrivial=true
check_PAIR_T1generic_scalarInvariantKineticOdd=true
check_PAIR_T1generic_lagrangian=true
check_PAIR_T1generic_naiveFixedLambdaFails=true
check_PAIR_T1generic_fieldEquation=true
check_PAIR_T1generic_conjugateFieldEquation=true
check_PAIR_T1generic_emtAll36=true
check_PAIR_T1generic_current=true
check_PAIR_T1generic_connectionCommutesWithGamma8=true
check_PAIR_T1grassmann_nontrivial=true
check_PAIR_T1grassmann_scalarEvenKineticOdd=true
check_PAIR_T1grassmann_lagrangian=true
check_PAIR_T1grassmann_naiveFixedLambdaFails=true
check_PAIR_T1grassmann_diracOperator=true
check_PAIR_T1grassmann_emt=true
check_PAIR_T1grassmann_current=true
check_PAIR_T1jets_lagrangian=true
check_PAIR_T1jets_scalarEvenKineticOdd=true
check_PAIR_T1jets_naiveFixedLambdaFails=true
check_PAIR_T1jets_emt=true
check_PAIR_T1jets_current=true
check_PAIR_T1jets_fieldEquations=true
check_PAIR_T1jets_connectionCommutes=true
check_PAIR_T1jets_onShellImage=true
check_PAIR_T1jets_conservationBoth=true
check_PAIR_T1jets_pairEMTAndCurrentVanish=true
check_PAIR_T1jets_vielbeinSignFlipGeometry=true
check_PAIR_T1jets_vielbeinSignFlipIsT1=true
check_PAIR_T1jets_gamma8WithFrameSignIsSymmetry=true
check_PAIR_T1krein_restHamiltonians=true
check_PAIR_T1krein_modes=true
check_PAIR_T1krein_fieldCAR=true
check_PAIR_T1krein_statesNormalised=true
check_PAIR_T1krein_expectationRule=true
check_PAIR_T1krein_positiveExcitations=true
check_PAIR_T1krein_imageAnticommutatorMinusB=true
check_PAIR_T1krein_imageOperatorIdentities=true
check_PAIR_T1krein_imageExpectationValues=true
check_PAIR_T1krein_minusMModes=true
check_PAIR_T1krein_independentCARPlusB=true
check_PAIR_T1krein_independentExpectationValues=true
check_PAIR_T2frame_unitVectors=true
check_PAIR_T2frame_characterIsMinusNorm=true
check_PAIR_T2frame_untwistedAdjointIsMinusReflection=true
check_PAIR_T2frame_frameReflectionsGeometry=true
check_PAIR_T2frame_scalarAndCurrentSigns=true
check_PAIR_T2frame_twistedSpacelikeMapsToMinusMSameLambda=true
check_PAIR_T2frame_untwistedSpacelikeContractE3=true
check_PAIR_T2frame_gamma8TimesUntwistedSpacelike=true
check_PAIR_T2frame_twistedTimelike=true
check_PAIR_T2frame_untwistedTimelikeSymmetry=true
check_PAIR_T2frame_gamma8TimesUntwistedTimelike=true
check_PAIR_T2z2_geometry=true
check_PAIR_T2z2_diracOperator=true
check_PAIR_T2z2_sameMassFails=true
check_PAIR_T2z2_scalarOdd=true
check_PAIR_T2z2_lagrangianEven=true
check_PAIR_T2z2_emtPullback=true
check_PAIR_T2z2_currentPullback=true
check_PAIR_T2z2_massFunctionMap=true
check_PAIR_T2z2_symmetricIffOddMass=true
check_PAIR_T2z2_PBfieldLevelFlipsLambda=true
check_PAIR_T2z2_ruleParities=true
check_PAIR_T1primordial_nontrivialCoupling=true
check_PAIR_T1primordial_scalarAndKinetic=true
check_PAIR_T1primordial_lagrangian=true
check_PAIR_T1primordial_diracOperator=true
check_PAIR_T1primordial_emt64=true
check_PAIR_T1primordial_current=true
check_PAIR_T3block_basisFromStage4=true
check_PAIR_T3block_gamma8IsSigma2BetweenPartnerBlocks=true
check_PAIR_T3block_gamma1IsSigma1InEveryBlock=true
check_PAIR_T3block_sigma2MapsBlockODE=true
check_PAIR_T3block_sigma1MapsBlockODE=true
check_PAIR_T3block_sigma3ReflectionMapsBlockODE=true
check_PAIR_T3block_antiunitaryMaps=true
check_PAIR_T3block_hamiltonianSigma2=true
check_PAIR_T3block_hamiltonianSigma1=true
check_PAIR_T3block_hamiltonianSigma3Reflection=true
check_PAIR_T3block_parityMap=true
check_PAIR_T3block_bagAngleMap=true
check_PAIR_T3block_sigma2IsRustSwap=true
check_PAIR_T3block_densityAndCurrentMaps=true
check_PAIR_T3block_potentialsStandardRule=true
check_PAIR_T3block_potentialsImageRule=true
check_PAIR_T3block_statisticsCoefficients=true
check_PAIR_T3block_orbitalEMTFormulas=true
check_PAIR_T3ks_modelHermitian=true
check_PAIR_T3ks_stationarityBothStatistics=true
check_PAIR_T3ks_sigma2FunctionalInvariant=true
check_PAIR_T3ks_sigma2Densities=true
check_PAIR_T3ks_sigma2KSOperatorEquivariant=true
check_PAIR_T3ks_sigma1FunctionalInvariant=true
check_PAIR_T3ks_imageRuleEnergyOdd=true
check_PAIR_T3ks_occupationsAndTemperature=true
check_PAIR_totals_ksKreinImagePair=true
check_PAIR_totals_ksMirrorPair=true
check_PAIR_T3ks_zeroModePlusM=true
check_PAIR_T3ks_zeroModeImage=true
check_PAIR_T3ks_zeroModeUntransformedControl=true
check_PAIR_T3ks_zeroModeSplittingMapsExactly=true
check_PAIR_T3ks_controlSplittingClosedForm=true
check_PAIR_T3ks_controlDiffersFromPairedProblem=true
check_PAIR_T3ks_controlZeroModeAtTip=true
check_PAIR_T3ks_massiveLevelsMap=true
check_PAIR_T3ks_mixedSectorSolutions=true
check_PAIR_T3ks_controlMixedSectorLevelsDisjoint=true
check_PAIR_T3ks_controlSubGapBoundState=true
check_PAIR_T3emt_phasesCancel=true
check_PAIR_T3emt_bilinearExtraction=true
check_PAIR_T3emt_stage4CrossCheck=true
check_PAIR_T3emt_gamma8OperatorIdentity64=true
check_PAIR_T3emt_standardRulePlusT=true
check_PAIR_T3emt_imageRuleMinusT=true
check_PAIR_stat_testUnitaries=true
check_PAIR_stat_fermionQuasiFreeStates=true
check_PAIR_stat_fermionWickMinus=true
check_PAIR_stat_singleModeMoments=true
check_PAIR_stat_bosonThermalWickPlus=true
check_PAIR_stat_classicalGaussianWickPlus=true
check_PAIR_stat_fixedAmplitudePhasesDeviate=true
check_PAIR_stat_expectationRuleTraces=true
check_PAIR_stat_filledShellExchangeRatio=true
check_PAIR_stat_uniformGasExchange=true
check_PAIR_stat_ldaPotentials=true
check_PAIR_stat_T0TotalDerivative=true
check_PAIR_stat_expectationRuleCovarianceIndefinite=true
check_PAIR_totals_fieldLevelChiralPair=true
check_PAIR_T2frame_onShellImage=true
check_PAIR_totals_fieldLevelMirrorPair=true
check_PAIR_internal_noException=true
measurement_algebra_oddBilinearMatrixCount=456
measurement_algebra_uBudagger_sign_for_u_gamma0to7=[1,1,1,1,1,-1,-1,-1]
measurement_T1generic_kineticMonomials=23552
measurement_T1generic_connectionMonomials=21504
measurement_T1jets.p1.Svalue=-1991/2160
measurement_T1grassmann_monomials_Ls=1288
measurement_T1grassmann_monomials_S2=120
measurement_T1krein_scalarDensity_particle1_particle2_hole3_hole4={1, 1, 1, 1}
measurement_T3block_gamma8_phases_per_target_block={1, 1, -1, -1, 1, 1, -1, -1}
measurement_T3block_gamma1_phases={-1, -1, -1, -1, -1, -1, -1, -1}
measurement_T3block_otherGammas_targetBlocks=<|"gamma^2" -> {{6}, {7}, {4}, {5}, {2}, {3}, {0}, {1}}, "gamma^3" -> {{6}, {7}, {4}, {5}, {2}, {3}, {0}, {1}}, "gamma^5" -> {{5}, {4}, {7}, {6}, {1}, {0}, {3}, {2}}, "gamma^6" -> {{5}, {4}, {7}, {6}, {1}, {0}, {3}, {2}}, "gamma^7" -> {{4}, {5}, {6}, {7}, {0}, {1}, {2}, {3}}|>
measurement_T3block_densitySigns_sigma2={1, -1, 1, 1}
measurement_T3block_densitySigns_sigma1={1, -1, -1, 1}
measurement_T3block_densitySigns_sigma3={1, -1, 1, -1}
measurement_T3ks_zeroModeSplitting_c_plusM=(2*(1 - E^(LL*(H - 2*Mz)))*Mz)/(E^a4c*(1 - E^(-2*LL*Mz))*(-H + 2*Mz))
measurement_T3ks_zeroModeSplitting_c_minusM_untransformedBC=(2*(-1 + E^(LL*(H + 2*Mz)))*Mz)/(E^a4c*(-1 + E^(2*LL*Mz))*(H + 2*Mz))
measurement_T3ks_c_values_M1_H1_L3_a0_decimal_label_float={1.90514825364486643824230369645649559722`17., 13.42197519757682301453825187090231339885`17.}
measurement_stat_filledShellRatio=1/8
measurement_stat_restShellCovarianceEigenvalues={-1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1}
check_count=141
failed_check_count=0
elapsed_seconds=<n>
report=<absolute path of the report file>
theory=<absolute path of pairing-theory.json, in the same folder>
```

The **verdict** is the pair of lines

```
check_count=141
failed_check_count=0
```

### 4.2 Exit code

`0` when every check is true (`failed_check_count=0` and `check_count` larger than 0);
`1` when any check is false, when the package cannot be loaded (`FATAL: module failed to
load: ...`) or when the package does not return a result (`FATAL: D16PairRun did not
return ...`).

### 4.3 The files written and how to check them

| File | Expected size | Expected sha256 |
| --- | ---: | --- |
| `wolfram-pairing-report.json` | 8141 bytes, 184 lines | `735534de950c7fb0327370c33caa275cf805aa91a41dee903e4eaec7a6fa0de8` |
| `pairing-theory.json` | 57027 bytes, 851 lines | `5a267bd696391b131134577ccdcf7766b83f96f3eb32b9b8de60c9175b1ebf6a` |

Both are written into the folder of the report path you gave (with the command of Section
3.4: `artifacts/dirac16complex/pair-creation/`). Ways to check them, from the repository
root:

* **Simplest (after the command of Section 3.4):** `git status` must print
  `nothing to commit, working tree clean` (or `git status --porcelain` prints nothing): the
  rewritten files are byte-identical to the committed ones.
* **sha256** (compare with the table):
  * PowerShell: `Get-FileHash artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json -Algorithm SHA256`
    (it prints the hash in capital letters; that is the same value);
  * macOS: `shasum -a 256 artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json`;
  * Linux: `sha256sum artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json`;
  * and the same for `pairing-theory.json`.
* **Count the true checks in the report** (must print `141`):
  * PowerShell: `(Select-String -Path artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json -Pattern '"PAIR_[A-Za-z0-9_]*":true').Count`
  * macOS/Linux: `grep -c '"PAIR_[A-Za-z0-9_]*":true' artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json`
  * The same with `":false` instead of `":true` must print `0`.
* **Read the report**: open it in any text editor. The key `checks` lists the 141 checks,
  `measurements` the 19 values printed above, and `sourceSha256` the sha256 of the five
  files of Sections 2.1 and 2.2 (they must equal the tables there).
* **Read the theory file**: `pairing-theory.json` is ordinary text. The entries `T1`,
  `T2` and `T3` contain the statements of the theorems (for `T3`: `theoremStandardRule`
  and `theoremImageRule`), their proofs or the maps they consist of, and a list `checks`
  with the names of the checks that verify them, each with the value `true`; the entry
  `notProved` lists what is not claimed.

### 4.4 The measurements in plain words

* `algebra_oddBilinearMatrixCount=456`: the number of 16 x 16 matrices that occur in the
  bilinears of the Lagrangian, field equation, energy-momentum tensor and current and that
  change sign under gamma^8.
* `algebra_uBudagger_sign_for_u_gamma0to7=[1,1,1,1,1,-1,-1,-1]`: for u = gamma^0 ...
  gamma^7, whether u B u^dagger equals +B or -B.
* `T1generic_kineticMonomials=23552`, `T1generic_connectionMonomials=21504`: the number
  of terms (monomials) of the kinetic term written with generic symbols, and how many of
  them contain the spin connection (the identity is far from trivial).
* `T1jets.p1.Svalue=-1991/2160`: the exact value of the scalar S = Psibar Psi at the first
  test point.
* `T1grassmann_monomials_Ls=1288`, `T1grassmann_monomials_S2=120`: the sizes of the
  Grassmann-algebra Lagrangian and of S^2.
* `T1krein_scalarDensity_particle1_particle2_hole3_hole4={1, 1, 1, 1}`: the normal-ordered
  scalar density in the four states with one particle (modes 1, 2) or one hole (modes 3,
  4) of the four-mode Fock model.
* `T3block_*`: the phases and target blocks of the gamma matrices in the 2 x 2 block basis
  and the signs of the densities (n, s, t, c) under the three maps.
* `T3ks_zeroModeSplitting_c_plusM` and `..._c_minusM_untransformedBC`: the exact
  closed forms of the first-order k-splitting of the zero mode for the paired problem and
  for the control (Mz = M, LL = L, a4c = a_4, E^x = e^x).
* `T3ks_c_values_M1_H1_L3_a0_decimal_label_float`: the same two numbers evaluated at
  M = H = 1, L = 3, a_4 = 0 (about 1.905 and 13.42); this is the only decimal number, and it
  is only a label: no check uses it.
* `stat_filledShellRatio=1/8`: the exchange energy of a filled shell is 1/8 of the Hartree
  energy (with the statistics sign).
* `stat_restShellCovarianceEigenvalues`: eigenvalues (-1)^4, 0^8, (+1)^4: the covariance
  implied by the expectation rule is indefinite.

### 4.5 Run time and memory (measured)

On the verification computer (Intel Core Ultra 9 275HX, 24 logical processors, Windows 11,
Wolfram 15.0.1). Other jobs were running on the same computer during every run (about a
dozen other Wolfram kernels on 2026-10-07, about eight on 2026-10-02), so the times are
upper values; an otherwise idle computer is faster. Runs 3 to 7 of 2026-10-07 ran at the
same time as each other.

Runs of 2026-10-07 (Part 6.2) that ran the complete set with every file present:

| Run | Shell | Report path | Elapsed (wall clock) | `elapsed_seconds` printed | Kernel peak working set | Kernel largest private memory (sampled) | Kernel processor time |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | PowerShell 7.6.6 | committed path | 392.9 s | 388 | 449.7 MiB | 671.2 MiB | not recorded |
| 2 | PowerShell 7.6.6 | committed path | 360.6 s | 355 | 452.9 MiB | 674.0 MiB | 334.5 s (last sample, under 1 s before the end) |
| 3 | Windows PowerShell 5.1, output into a file with `>` | `build/old-pairing/` | 468.0 s | 458 | not measured | not measured | not measured |

Duration of the steps in seconds, as printed by runs 1, 2 and 3 of 2026-10-07 and, for
comparison, by runs 1 to 4 of the first verification of 2026-10-02 (Part 6.3):

| Step | Run 1 | Run 2 | Run 3 | 10-02 run 1 | 10-02 run 2 | 10-02 run 3 | 10-02 run 4 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `T1generic` | 93 | 74 | 104 | 57 | 69 | 64 | 52 |
| `T1jets` | 64 | 61 | 67 | 50 | 56 | 52 | 45 |
| `T1krein` | 2 | 2 | 2 | 2 | 2 | 2 | 1 |
| `T2frame` | 187 | 177 | 228 | 143 | 150 | 158 | 116 |
| `T2z2` | 2 | 2 | 3 | 3 | 2 | 2 | 1 |
| `T1primordial` | 15 | 12 | 19 | 16 | 13 | 13 | 8 |
| `T3ks_functional` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `T3ks_spectra` | 4 | 5 | 5 | 3 | 4 | 3 | 2 |
| `T3emt` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `stat` | 4 | 3 | 4 | 3 | 4 | 3 | 2 |
| `totals` | 16 | 17 | 22 | 14 | 17 | 16 | 11 |
| total (`done in`) | 388 | 355 | 458 | 292 | 318 | 313 | 240 |

The wall-clock times of the first verification were 295.9 s, 321.9 s, 317.4 s and
244.5 s, with kernel peak working sets of 435.6 and 437.1 MiB and peak private memory of
657.5 and 658.3 MiB (runs 1 and 2; not measured in runs 3 and 4).

The kernel works essentially on one processor core (in run 2 its processor time was
334.5 s after about 360 s of elapsed time); the longest steps are `T2 frame reflections`
(2 to 4 minutes), `T1 generic symbols` and `T1 jets` (about one to 1.5 minutes each). The
wall-clock time is a few seconds longer than `elapsed_seconds`, because it includes the
start of the kernel, the loading of the packages and the writing of the files. Expect
roughly 4 to 8 minutes on a similar computer, and more on a slower one.

### 4.6 Other Wolfram versions and other operating systems

The byte-identical reproduction of Part 6 was measured with Wolfram 15.0.1 on Windows.
The checks are exact algebra and should be true with any recent Wolfram version on any
operating system, but the *bytes* of the two JSON files can depend on the version: the
JSON writer (`ExportString[..., "RawJSON"]`) and the printed form of expressions (for
example the 17-digit decimal label `T3ks_c_values_M1_H1_L3_a0_decimal_label_float`, or
the order in which terms of a formula are printed) may differ. If you see
`failed_check_count=0` but `git status` reports the two output files as modified, the
theorems are still verified; the difference is in formatting. Look at it with
`git diff`, then restore the committed files (Part 5). If a check is `false`, that is a
real discrepancy: record your `$Version` and the failed names.

---

## 5. Side effects

**Files in the repository.**

* With the command of Section 3.4 the run **overwrites two committed files**:
  `artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json` and
  `artifacts/dirac16complex/pair-creation/pairing-theory.json`. When the run reproduces
  them byte for byte (as in every verification run of Part 6), git sees no change:
  `git status` prints `nothing to commit, working tree clean` (and
  `git status --porcelain` prints nothing); only the files' modification times change.
* A run that ends with false checks (exit code 1, lines `CHECK FAILED: ...`), for
  example because an input file is missing, **still writes both output files** (the
  script writes them before it counts the false checks). With the command of Section 3.4
  it therefore overwrites the committed files with a failing report; restore them with
  the `git checkout` command at the end of this part. Only the two `FATAL` cases of
  Section 4.2 (the package cannot be loaded, or it returns no result) write no output
  file: the script stops before it writes anything.
* With a report path elsewhere (for example the `build/` variant of Section 3.4) the run
  creates the folder of the report if it does not exist (including missing parent
  folders: in a fresh clone, where there is no folder `build/`, it creates both `build/`
  and `build/old-pairing/`) and writes the report and `pairing-theory.json` there; the
  committed files are not touched. `build/` is ignored by git, so `git status` still
  prints `nothing to commit, working tree clean` (and `git status --porcelain` prints
  nothing). `git status --ignored` lists the folder as `build/`;
  `git status --porcelain --untracked-files=all --ignored` lists the two files
  `build/old-pairing/pairing-theory.json` and
  `build/old-pairing/wolfram-pairing-report.json`.
* No other file in the repository is created, changed or deleted (verified with
  `git status --porcelain --untracked-files=all --ignored` after every run of both
  verifications of Part 6: after the runs with every file present it listed nothing, or
  only the two files under `build/old-pairing/` for the `build/` variant; after the
  runs that had a file removed on purpose it listed only that removed file and, except
  for the `FATAL` case, the two overwritten outputs).

**Files outside the repository** (observed on Windows; the corresponding folders on macOS
and Linux were not inspected):

* WolframScript keeps temporary files named `tmp_` followed by ten random letters and
  digits in `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\` (that is
  `C:\Users\<you>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary\`); one of them
  collects the printed lines while the run is in progress. In the verification of
  2026-10-07 the folder was read again and again (with a pause of 0.7 seconds) while runs
  3 to 7 were made, with a reader that does not block the writer: every file that held printed output of this
  set (five files, one for each of those runs, created within 7 seconds of the start of
  its run, up to 884 kB for the failing runs) was deleted when its run ended. Other
  files of the folder could not be attributed with certainty, because about a dozen other
  WolframScript jobs were writing there at the same time; in run 2 the two files created
  in the same second as the run started (one empty, one of 206 bytes) and one created
  three seconds later were gone after the run. The first verification (2026-10-02, with
  fewer other jobs) saw two such files per run, an empty one at the start and, about three
  seconds later, the one that collects the printed lines, both deleted at the end of every
  run in which this was checked, including the failing runs. If a run is interrupted they
  may be left behind (not tested); they can then be deleted by hand.
* WolframScript rewrites its own small settings file
  `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` (238 bytes) at the end of every run
  (seen in runs 1 and 2 of both verifications; on 2026-10-02 only its modification time
  was seen to change).
* Nothing else was seen to change in `%APPDATA%\Wolfram`, `%LOCALAPPDATA%\Wolfram` or at
  the top level of `%TEMP%` that could be attributed to the run (snapshots of these
  folders before and after runs 1 and 2 of 2026-10-07; on 2026-10-02 also
  `C:\ProgramData\Wolfram`). Other programs that ran at the same time changed some entries
  there: during run 1 of 2026-10-07 a Wolfram front end of another job (its process was not
  one of the processes of the run) wrote `%LOCALAPPDATA%\Wolfram\Logs\FrontEnd\system.log`
  and a cache file; during run 2 nothing besides `WolframScript.conf` and the temporary
  folder changed there. The package itself writes no temporary file.

**Processes.** `wolframscript` (about 17 MiB of memory) starts **one** Wolfram kernel (a
process named `wolfram.exe` on Windows, started with the options `-runfirst ...
-linkmode Connect -linkname ... -mathlink`; on macOS and Linux it is named
`WolframKernel` or `wolfram`) and waits for it. A second, short-lived `wolfram.exe`
process was also seen in runs 1 and 2 of 2026-10-07 (in run 2 it ended before its
options could be read; on 2026-10-02 they were read as `-wlbanner -licenseinfo`, a query
of the licence). No parallel kernels are launched. All processes end with the run. The
kernel's peak memory is given in Part 4.5.

**Network.** None needed and none used. All network endpoints owned by `wolframscript`
and by its kernels were listed again and again (with a pause of 0.5 seconds between two
listings) during run 2 of 2026-10-07 and during runs 1 and 2 of 2026-10-02. In run 2 of 2026-10-07 the kernel held one TCP connection
between two local ports of `127.0.0.1` (54552 and 54553, a link inside the same computer)
and a socket bound to the local port 54553 (state `Bound`, no remote end); on 2026-10-02
the kernel held two such pairs of `127.0.0.1` connections in run 1 and no endpoint at all
in run 2. No connection to any other computer and no UDP endpoint was seen in any of these
runs.

**How to restore the committed state.** From the repository root, in any shell:

```
git checkout -- artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json artifacts/dirac16complex/pair-creation/pairing-theory.json
```

and, if you used the `build/` variant, delete its folder
(PowerShell: `Remove-Item -Recurse -Force build/old-pairing`; macOS/Linux:
`rm -r build/old-pairing`). If the folder `build/` did not exist before the run (it does
not in a fresh clone), delete it too, because the run created it and it is now empty
(PowerShell: `Remove-Item -Recurse -Force build`; macOS/Linux: `rm -r build`); git does
not show an empty folder, so `git status` will not remind you of it. Afterwards
`git status` prints `nothing to commit, working tree clean` (and
`git status --porcelain --untracked-files=all --ignored` prints nothing).

**Why the outputs must not change.** The sha256 values of both output files are recorded
in several other committed files and checked by unit tests (Section 1.2). If your run
writes different bytes (for example with another Wolfram version, Part 4.6), do not
commit them; restore the committed files with the command above.

---

## 6. Verification record

* **Date:** 2026-10-02.
* **Commit verified:** `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, the head of branch `main`
  of <https://github.com/once-ere/Dirac_claude.git> when the clones were made. The files of
  the set were last changed in commit `ba7b170` (2026-09-30) and the two outputs were last
  committed in commit `eac67e6` (2026-09-30). The sha256 values of every file of the set at
  the verified commit are those of Part 2, and they equal the values recorded in the
  committed report (`sourceSha256`).
* **Environment:** Windows 11 Pro for Workstations, version 10.0.26200 (build
  26200.9457), 24 logical processors; WolframScript 1.14.0; Wolfram 15.0.1 for Microsoft
  Windows (64-bit) (July 2, 2026), Professional licence; PowerShell 7.6.6; Windows
  PowerShell 5.1.26100.9444 (second verification only); Git Bash (GNU bash 5.2.37) with
  git 2.51.2.windows.1. Other jobs, including about eight other Wolfram kernels, were
  running on the computer at the same time.
* **Clones:** three fresh clones (`git clone https://github.com/once-ere/Dirac_claude.git`)
  in a scratch folder about 135 characters deep; nothing was copied into them from any
  other working copy (the set needs no uncommitted file). Each clone was used for one run.
* **Runs** (all from the repository root of their clone, with the exact command shown):

  | Run | Clone | Shell | Command | Exit code | Started | Elapsed |
  | --- | --- | --- | --- | ---: | --- | ---: |
  | 1 | 1 | PowerShell 7.6.6 | `wolframscript -file scripts/verify_dirac16complex_pairing.wls artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json` | 0 | 2026-10-02T06:02:20 | 295.9 s |
  | 2 | 2 | Git Bash | the same command | 0 | 2026-10-02T06:07:22 | 321.9 s |
  | 3 | 3 | PowerShell 7.6.6 | `wolframscript -file scripts/verify_dirac16complex_pairing.wls build/old-pairing/wolfram-pairing-report.json` | 0 | 2026-10-02T06:04:07 | 317.4 s |

  Runs 1 and 2 are the two runs of the command of the script's own usage header (which
  overwrites the committed outputs in the clone); run 3 checks the `build/` variant of
  Section 3.4. Runs 1 and 3 overlapped in time; run 2 started after run 1 had ended. The
  start times are local time (UTC-7). Every run printed `check_count=141` and
  `failed_check_count=0`. For comparison, the textbook (Section 19.10) records an earlier
  run of the same command at commit `1f2dd69`: 338 s, 141 of 141 checks, both outputs
  byte-identical.

* **Byte identity of every output:**

  | Output | Committed sha256 | Run 1 | Run 2 | Run 3 | Run 1 = Run 2 |
  | --- | --- | --- | --- | --- | --- |
  | `wolfram-pairing-report.json` | `735534de950c7fb0327370c33caa275cf805aa91a41dee903e4eaec7a6fa0de8` | byte-identical to committed | byte-identical to committed | byte-identical to committed | yes |
  | `pairing-theory.json` | `5a267bd696391b131134577ccdcf7766b83f96f3eb32b9b8de60c9175b1ebf6a` | byte-identical to committed | byte-identical to committed | byte-identical to committed | yes |

* **Printed output:** after replacing the clock times, the durations and the two absolute
  paths by placeholders, the printed output of each of runs 1, 2 and 3 is identical, line
  for line, to the block of Section 4.1 (191 lines); the error stream was empty in each of
  them.
* **Repository state after each run:** `git status --porcelain --untracked-files=all`
  printed nothing in all three clones; with `--ignored` added
  (`git status --porcelain --untracked-files=all --ignored`), clone 3 listed only the two
  files `build/old-pairing/pairing-theory.json` and
  `build/old-pairing/wolfram-pairing-report.json` (`git status --short --ignored`, without
  `--untracked-files=all`, shows them as the folder `build/`).
* **Check counts:** 141 checks, 141 true, 0 false, in each of runs 1, 2 and 3 (and in
  run 4 below); 19 measurements, all identical to the committed report.
* **Failure-mode test:** after run 3 (and after its repository state had been recorded),
  in clone 3, the package `wolfram/Dirac16ComplexPairing.wl` was renamed on purpose and
  the command with the report path `build/fail-test/wolfram-pairing-report.json` was run.
  It printed `Get::noopen: Cannot open ...`, `FATAL: module failed to load: ...`,
  `check_count=0` and `failed_check_count=1`, ended with exit code 1 after 2 seconds, and
  created only the empty folder `build/fail-test` (no output file). The package was then
  renamed back (its sha256 checked) and the empty folder removed. This is the row
  "FATAL: module failed to load" of Section 3.5.
* **Second verification (after a review of this file), same date, same commit
  `c2b33cc`:** four more fresh clones P, Q, R and S, nothing copied into them. The four
  runs started together at 06:48:48 local time and ran at the same time (with other jobs
  on the computer). Runs 5, 6 and 7 are failure-mode tests: one file of the clone was
  moved out of it before the run, and the command of Section 3.4 (which writes over the
  committed outputs) was used.

  | Run | Clone | Shell | Changed before the run | Report path | Exit code | Elapsed | Printed result |
  | --- | --- | --- | --- | --- | ---: | ---: | --- |
  | 4 | P | Windows PowerShell 5.1.26100.9444, output sent into a file with `>` | nothing | `build/old-pairing/wolfram-pairing-report.json` | 0 | 244.5 s | `check_count=141`, `failed_check_count=0` |
  | 5 | Q | PowerShell 7.6.6, output into a file with `>` | `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` moved away | `artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json` | 1 | 244.4 s | `Import::nffil`, `Table::iterb`, `CHECK FAILED: PAIR_algebra_fixtureMatches`, `FileHash::noopen`, `check_count=141`, `failed_check_count=1` |
  | 6 | S | PowerShell 7.6.6, output into a file with `>` | `artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json` moved away | the same | 1 | 229.7 s | `Import::nffil`, `INTERNAL ERROR: ...` (one line of about 89,000 characters), `FileHash::noopen`, `check_count=98`, `failed_check_count=4` (`PAIR_T3block_basisFromStage4`, `PAIR_T3block_gamma8IsSigma2BetweenPartnerBlocks`, `PAIR_T3block_gamma1IsSigma1InEveryBlock`, `PAIR_internal_noException`); no step after `T3 block maps` was run |
  | 7 | R | Git Bash, output into a file with `>` | `wolfram/Dirac16ComplexGeometry.wl` moved away | the same | 1 | 153.5 s | `Get::noopen`, Wolfram error messages, `FileHash::noopen`, `check_count=141`, `failed_check_count=29` (818,908 bytes of printed text) |

  * Run 4: both outputs byte-identical to the committed files (sha256 as in Part 2); the
    printed output, after the placeholders of Section 4.1, identical line for line to
    the block of Section 4.1 (191 lines); the error stream empty. Before the run the
    clone had no folder `build/`; the run created `build/` and `build/old-pairing/`.
    Afterwards `git status` printed `nothing to commit, working tree clean`,
    `git status --porcelain` printed nothing,
    `git status --porcelain --untracked-files=all --ignored` printed the two files under
    `build/old-pairing/`, and `git status --short --ignored` printed `!! build/`. After
    `Remove-Item -Recurse -Force build/old-pairing` the empty folder `build/` was still
    there, and git listed nothing, even with `--ignored`; after
    `Remove-Item -Recurse -Force build` the clone was exactly as cloned. The same two
    steps with `rm -r` in Git Bash were tested on a re-created copy of the folder.
  * Output sent into a file, sampled every 10 seconds: the file of run 4 (Windows
    PowerShell 5.1) grew while the run proceeded (104 bytes 12 seconds after the start,
    1,450 bytes about three seconds before the end, 17,982 bytes at the end); it is UTF-16
    little-endian with a byte-order mark and with CR LF at the end of each of its 191
    lines. The files of runs 5 and 6 (PowerShell 7) had 0 bytes at every sample until
    their runs had ended; they are ASCII with CR LF line ends. The file of run 7 (Git Bash)
    grew while the run proceeded, also with CR LF line ends (as did the Git Bash file of
    run 2).
  * Runs 5, 6 and 7 each **overwrote both committed output files with a failing report**
    (`git status` showed them as modified, next to the moved input file as deleted). The
    commands `git checkout -- <the moved file>` and
    `git checkout -- artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json artifacts/dirac16complex/pair-creation/pairing-theory.json`
    restored the committed bytes (sha256 checked); `git status` then printed
    `nothing to commit, working tree clean` and
    `git status --porcelain --untracked-files=all --ignored` printed nothing. These are the
    rows of Section 3.5 for a missing geometry package and a missing input file.
  * Size of a fresh clone (clone P before its run): 538,056,938 bytes = 513.1 MiB, of
    which the folder `.git` is 133,534,691 bytes = 127.3 MiB (`git count-objects -vH`:
    size-pack 126.99 MiB) and the checked-out files are 404,522,247 bytes = 385.8 MiB
    (Section 3.1).
* **Fixes made:** none to the set. The set executed correctly as committed; no file of the
  set was changed. After a review, this provenance file itself was corrected (the clone
  size, the text that plain `git status` prints, the empty `build/` folder left after the
  restore of the `build/` variant, the output files that a failing run overwrites, the
  documents and tests that use the outputs, the `--ignored` listing of clone 3, and
  output redirection in Windows PowerShell 5.1). Every corrected statement was checked
  again: by the runs of the second verification above, by `git grep` in fresh clone P
  (the lists of Section 1.2) and in the original clone 3 (its `--ignored` listing, which
  was still the same).
* **Open discrepancies:** none in execution or in the numbers. The open item of
  Section 1.1 (the physical wording of `T1krein.imageField` and `T1krein.consequence` in
  `pairing-theory.json`, to be corrected according to `HANDOFF.md` section 0.4 item C) is
  a matter of interpretation; the checks themselves are true, and the committed outputs
  were left unchanged.
