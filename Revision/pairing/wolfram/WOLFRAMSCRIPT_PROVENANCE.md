# WolframScript provenance: the pairing verifier (`Revision/pairing/wolfram/`)

This file tells you what the WolframScript set in this folder is, which files it reads and writes,
exactly how to run it on your own computer (even if you have never used Wolfram software), what you
should see when it works, what it changes on your disk, and how it was tested. Everything you need to
run it is written out here; you do not have to look anything up in another file.

## 1. What this set is and what it computes

### 1.1 In plain words

The theory studied in this repository has a field `Psi` with 16 complex components living in an
8-dimensional space-time with four space directions and four time directions (signature (4,4)). The
eight coordinates are named `x1 ... x8`: `x1, x2, x3` are ordinary space, `x4` is ordinary time,
`x5, x6, x7` are three extra time directions that deflate exponentially, and `x8` is a hidden space
direction (with `z = 6 H x8`). The field comes in two versions, and every statement below is checked
for both:

* `dirac16complex`: the components of `Psi` are Grassmann numbers (they anticommute, as for fermions);
* `dirac16complex00`: the components of `Psi` are ordinary commuting complex numbers.

The script `verify_pairing.wls` proves, by exact computer algebra (symbols, exact integers and
fractions, never floating-point numbers; every check ends in `True` or `False`), three groups of
statements called the pairing theorems:

* **T1, the chirality pairing.** The 16 x 16 matrix `Gamma = diag(-1, ..., -1, +1, ..., +1)` (eight
  of each) maps a field `Psi` of mass `m` and self-coupling `lambda` to the field `Gamma Psi` of
  mass `-m` and coupling `-lambda`: the Lagrangian changes sign,
  `L_(m,lambda)[Gamma Psi] = -L_(-m,-lambda)[Psi]`; solutions go to solutions; the energy-momentum
  tensor `T_mu nu` and the current `J^mu` change sign, so the pair (`Psi` with `(m, lambda)`,
  `Gamma Psi` with `(-m, -lambda)`) has total energy-momentum zero and total charge zero, as classical
  quantities in a fixed gravitational field.
* **T2, the mirror pairing.** `Gamma` combined with the reflection `P_n = Gamma gamma^n` of one
  space-like frame direction `n` (an element of the group Pin(4,4) of "character -1") maps
  `(m, lambda)` to `(-m, lambda)` with `L -> +L`; the mirror partner has the SAME (not the opposite)
  energy-momentum and charge. In the author's metric this reflection is the mirror image across the
  surface `z = pi/2` of the hidden coordinate (an ASSUMED Z2 construction).
* **Q, the quantum-level reading.** After quantisation the image `Gamma Psi` carries the indefinite
  ("Krein") metric `-B` instead of `B`; its own energy, momentum and charge are the same operators as
  those of `Psi` (it is the same quantum system relabelled, not a second universe); an independently
  quantised `(-m, -lambda)` universe cannot be identified with `Gamma Psi`, and the generators of two
  independent universes add without cancelling; the one-particle energy spectra of `+m` and `-m` are
  identical; in flat space every real-frequency eigenspace has Krein inertia (4 positive, 4 negative)
  and every imaginary- or zero-frequency eigenspace is Krein-neutral.

Every map tested in this set is a 16 x 16 MATRIX acting on the field (`Psi -> M Psi`,
`Psi^dagger -> Psi^dagger M^dagger`, with `M` one of `Gamma`, `gamma^n`, `P_n = Gamma gamma^n`);
none of them is a complex conjugation `Psi -> Psi*`. Charge conjugation itself is not the subject of
this set; where the theory needs it, it too is a matrix operation (for a real field, plain complex
conjugation changes nothing, so it cannot be charge conjugation).

The statements are checked in four gravitational fields: the author's metric of the primordial
universe on the patch `0 < z < pi/2` ("primordial"), the same metric on the mirror patch
`pi/2 < z < pi` ("mirror_patch"), a general diagonal field with eight arbitrary functions of all eight
coordinates ("diagonal8"), and a general non-diagonal field at one point with exact rational numbers
("pointwise"); in addition a linearity argument covers every field. The script runs 101 checks.

What the set does NOT establish is written into its own output file (`pairing-theory.json`, key
`not_established`, nine items). In short: it describes no creation process of universes, no rate or
amplitude, and no dynamical necessity for the partner to exist; T1 changes the parameters and the
sign of the action, so it is not a symmetry of one theory; the vanishing total energy-momentum holds
for classical bilinears (and inside one quantum system), not for two independently quantised
universes; the gravitational field is a fixed test field (no back-reaction); the Z2 brane at
`z = pi/2` is assumed; a positive-norm Fock space is not established; the Kohn-Sham level (T3) is a
separate set.

### 1.2 The checks, by group (101 in total)

| group | what is checked | checks |
| --- | --- | --- |
| A. fixture | the gamma matrices read from the input file satisfy the Clifford relation; `C`, `Gamma`, `B`, `S^ab` re-derived; basic properties of `Gamma`, `C`, `B` | 4 |
| B. T1 kernels | `Gamma C Gamma = C`, `Gamma C gamma^a Gamma = -C gamma^a`, the 512 connection kernels, the field-equation kernels, the linearity argument (every field) | 5 |
| C. T2 kernels | `P_n` is in Pin(4,4), covers the reflection `R_n`, its character is `-eta_nn`, `Gamma P_n = gamma^n`, the kernel signs | 5 |
| D. fields | the primordial vielbein gives the author's metric, the pointwise field is generic, the spin connection of each of the four fields is antisymmetric and satisfies the vielbein postulate | 6 |
| E. T1 explicitly | in the primordial, diagonal8 and pointwise fields, both statistics: scalar and kinetic term, Lagrangian, negative controls, field-equation covariance, Euler-Lagrange expressions (primordial, diagonal8), energy-momentum, current; an arbitrary potential `U(S)` (primordial, commuting) | 45 |
| F. T2 | frame reflection of each of the 8 directions in the pointwise field, both statistics (16); the mirror is an isometry (1); mirror Lagrangian, energy-momentum and current, Euler-Lagrange, both statistics (6) | 23 |
| G. Q | Krein metric of the images, symplectic kernels, generators of the image, flat dispersion, one-particle maps, Krein signatures, the proof for every real frequency, Krein-neutral complex and zero frequencies, a general field, no identification of independent universes | 12 |
| H. output | the theory file generated twice in one run is identical, LF only | 1 |

### 1.3 Documents that cite these results

* `Revision/docs/PAIR_CREATION_PROOFS.md` (and its `.tex` and `.pdf`): theorems T1, T2 and Q, the
  count table row "`Revision/pairing/reports/wolfram-pairing.json` | 101 | 101 | 0", the samples of
  `pairing-theory.json`, the reproduction command.
* `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` (and its `.tex` and `.pdf`): "Wolfram: 101 of 101
  checks pass" for the pairing, and the reproduction command.
* `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` (and its `.tex` and `.pdf`): the count
  "wolfram-pairing 101", check names cited one by one, and the reproduction command.
* The publication tests `Revision/tests/test_pair_creation_proofs_publication.py`,
  `Revision/tests/test_dirac16complex_field_theory_publication.py` and
  `Revision/tests/test_dirac16complex00_field_theory_publication.py` re-read `wolfram-pairing.json`
  and confirm the cited check names, verdicts and counts.
* The independent sympy checker `Revision/pairing/python/check_pairing.py` compares its own results
  with `pairing-theory.json` at its end (so this Wolfram verifier runs before it).
* `provenance/dirac matrices.md` (the proof that the author's eight real 16 x 16 Dirac matrices are
  the ones used): it lists `verify_pairing.wls` and `RevisionPairing.wl` among the programs that read
  the gamma matrices from `Revision/algebra/gammas.json`.
* `Revision/algebra/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` (the set that writes `gammas.json`) names
  `verify_pairing.wls` as a reader of `gammas.json`;
  `Revision/pairing/kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` (the T3 set) points to this set and
  to `pairing-theory.json`; `provenance/wolframscript/verify_dirac16complex_pairing.PROVENANCE.md`
  (the OLD Stage-5 pairing set `scripts/verify_dirac16complex_pairing.wls`) says that this newer set is
  a different one and must not be confused with it.
* The textbook "Universes in Pairs" that is being written under `Revision/textbook/` (work in
  progress, not yet verified; as found at commit `b8a695d` of 2026-10-07): the chapter
  `00-how-to-use-this-book.md` names `wolfram-pairing.json` as one of the two independent verifier
  records of T1, T2 and Q; the chapter `10-canonical-quantisation-krein-space.md` cites the checks
  `Q_one_particle_flat_dispersion` and `Q_one_particle_maps` of `wolfram-pairing.json` and the data
  `one_particle_flat` of `pairing-theory.json`. Notebooks under `Revision/textbook/notebooks/` (each
  with its Python source in `src/`) read the outputs: `00c_honesty_ledger.ipynb` counts the checks of
  `wolfram-pairing.json`; `10a_krein_spectra.ipynb` reproduces four checks of `wolfram-pairing.json`
  (`Q_one_particle_flat_dispersion`, `Q_one_particle_maps`, `Q_one_particle_Krein_signatures`,
  `Q_one_particle_complex_and_zero_frequencies_Krein_neutral`) and the
  data `one_particle_flat` of `pairing-theory.json`; `10b_canonical_krein.ipynb` reproduces the data
  `Krein_signs_M_B_Mdagger` of `pairing-theory.json`; the sources of the notebooks `10g`, `18a`,
  `18b`, `18c`, `20a`, `20b`, `20c`, `21b` and `21c` also read `wolfram-pairing.json`,
  `pairing-theory.json` or both.

## 2. The files

| file | role | sha256 | lines | bytes |
| --- | --- | --- | --- | --- |
| `Revision/pairing/wolfram/verify_pairing.wls` | the script you run (the driver: all 101 checks, writes both outputs) | `ce7efca01e73105a8bb934181e91600edf720ee047411c22ecc0c518e95c9fbd` | 501 | 52611 |
| `Revision/pairing/wolfram/RevisionPairing.wl` | the package the script loads (field algebra for both statistics, spin connection, bilinears, Euler-Lagrange expressions) | `a1806b50705c729767795cff2c5382390e9763feaebca051a68951d99b6b8222` | 234 | 14469 |
| `Revision/algebra/gammas.json` | INPUT, only read (the 16 x 16 gamma matrices `gamma^(x1..x8)`, `eta`, `C`, `Gamma`, `B`, `S^ab`; written by the algebra set `Revision/algebra/wolfram/verify_algebra.wls`, which you do NOT need to run first) | `95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01` | 1405 | 76968 |
| `Revision/pairing/reports/wolfram-pairing.json` | OUTPUT, overwritten by every run (every check with its name, verdict `PASS` or `FAIL` and detail; the summary counts) | `4ea0fa709ed595b9279b04f1d45d2dce64b759ef0d60c57d15207bba02352990` | 112 | 40151 |
| `Revision/pairing/pairing-theory.json` | OUTPUT, overwritten by every run (the theorems T1, T2, Q with hypotheses, statements, proofs, the names of the checks verifying them, data tables, and what is not established) | `aaf104a92a64d7a50ef590207201798ddfe08affbf4df371441eba157517c2ce` | 420 | 22430 |

The hashes are those of the committed files (unchanged from commit `70fab64` up to commit `b8a695d`,
the head of `main` in the evening of 2026-10-07, where they were checked again); a successful run
reproduces both outputs byte for byte.
Nothing else is read: no other file of the repository, no network resource, no command-line argument.
The script finds its package, its input and its output folders relative to its own location, so these
files must keep their places in the repository.

## 3. How to run it

### 3.1 What you need

* A computer with Windows 10 or 11, macOS or Linux, about 1 GB of free memory (the Wolfram kernel
  used at most 247 MB here), about 1 GB of free disk space for the repository, and a few minutes
  (about 2 to 5 minutes on the verification machine, depending on how busy it was; a slower or
  busier computer can take longer).
* Git, to download the repository.
* The Wolfram Engine (free for developers) or Mathematica / Wolfram, with the command-line program
  `wolframscript`. `wolframscript` starts a Wolfram "kernel" (the computing engine) without any
  window, runs a script file in it and prints what the script prints. The set was verified with
  WolframScript 1.14.0 and Wolfram 15.0.1; other versions were not tested.
* An internet connection for installing and activating the software and for downloading the
  repository. The script itself needs no network.

### 3.2 Install Git

* Windows: download "Git for Windows" from https://git-scm.com/download/win, run the installer and
  accept the default choices.
* macOS: open the Terminal application and type `git --version`; if Git is missing, macOS offers to
  install the "command line developer tools": accept.
* Linux: install the package `git` with your distribution's package manager, for example
  `sudo apt install git` (Debian, Ubuntu) or `sudo dnf install git` (Fedora).

Check it in a NEW terminal window: `git --version` prints a version number.

### 3.3 Install the Wolfram Engine and activate `wolframscript`

Use ONE of the two options.

**Option A: the free Wolfram Engine for Developers.**

1. Open https://www.wolfram.com/engine/ in a web browser, choose your operating system and start the
   download of the Wolfram Engine. To use it you need a free Wolfram ID (an account at Wolfram) and a
   free licence: on the page that appears after the download starts, click "Get Your License", sign
   in with your Wolfram ID (create it yourself on the Wolfram web site if you have none), read the
   licence terms and accept them yourself, and click "Get License".
2. Install it. Close every other Wolfram program first.
   * **Windows:** go to your Downloads folder. If the download is a `.zip` file, right-click it,
     choose "Extract All", open the extracted folder and double-click `setup.exe`; if the download is
     an `.exe` file, double-click it. Click "Next" on each screen (the default folders are fine),
     then "Install", wait, and click "Finish". `wolframscript` is installed together with the engine.
   * **macOS:** double-click the downloaded `.dmg` file in your Downloads folder; the Wolfram Engine
     setup window opens. (a) Drag the "Wolfram Engine" icon onto the "Applications" folder icon in
     that window. (b) In the SAME window, double-click `wolframscript.pkg` and click through its
     installer ("Continue", then "Install"; type your Mac login password if macOS asks for it; then
     "Close"). This second step is what installs the `wolframscript` command: without it, the
     Terminal does not know `wolframscript`. (c) Open the "Applications" folder and double-click
     "Wolfram Engine": this starts `wolframscript` and asks for your Wolfram ID and password (the
     activation of step 3).
   * **Linux:** open a terminal, go to the download folder (for example `cd ~/Downloads`) and run
     `sudo bash <name of the downloaded .sh file>` (type your own Linux password when `sudo` asks for
     it). Press Enter to accept the proposed installation folder and again to accept the proposed
     folder for the scripts (`/usr/local/bin`); `wolframscript` is installed there.
3. Activate it. Open a NEW terminal window (Windows: "PowerShell" from the Start menu; macOS:
   "Terminal" from Applications, Utilities; Linux: your terminal) and type `wolframscript`. The first
   time, it asks you to activate the engine with your Wolfram ID (e-mail address) and password; type
   them yourself. When the prompt `In[1]:=` appears, the engine is active: type `Quit[]` and press
   Enter. (On Windows the installer may already have opened such an activation window by itself, and
   on macOS step 2 (c) does the same; if you activated there, `wolframscript` shows `In[1]:=` at
   once. If the activation does not start by itself, run `wolframscript -activate`.)

**Option B: Mathematica (or the "Wolfram" desktop product) is already installed and activated.**
On Windows `wolframscript` is installed together with it. On macOS and Linux it may not be on your
command path: if `wolframscript -version` (next step) is not found, download the stand-alone
WolframScript installer for your system from https://www.wolfram.com/wolframscript/ and install it;
it finds the installed Mathematica / Wolfram by itself.

**Check the installation** in a new terminal window (the same three commands work in PowerShell,
macOS Terminal and Linux):

```text
wolframscript -version
wolframscript -code "1+1"
wolframscript -code '$Version'
```

The first command prints a line such as `WolframScript 1.14.0 for Microsoft Windows (64-bit)`, the
second prints `2`, the third prints the kernel version, such as
`15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. If the second command asks for activation or
prints a licence error, repeat step 3 of option A.

### 3.4 Download the repository

In the terminal, go to a folder where you want the repository (for example your home folder) and run:

```text
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

`git clone` creates the folder `Dirac_claude` (at commit `b8a695d` of 2026-10-07 about 240 MB were
downloaded and about 750 MB were used on disk; the repository grows over time, so this takes a while)
and `cd Dirac_claude` makes it the current folder. This folder is the
"repository root": it contains the folder `Revision`. Every command below is typed in this folder.

### 3.5 Run the script

**Windows (PowerShell):**

```powershell
wolframscript -file Revision/pairing/wolfram/verify_pairing.wls; "exit code: $LASTEXITCODE"
```

**macOS (Terminal) and Linux (bash or zsh):**

```bash
wolframscript -file Revision/pairing/wolfram/verify_pairing.wls; echo "exit code: $?"
```

Type the command on one line and press Enter. For a few seconds nothing is printed while the kernel
starts and reads the input; then one line per check appears as each check finishes, with pauses of
several seconds at the heavier checks. The whole run takes a few minutes: on the verification
machine between about 2 and 4.6 minutes, the longer times while dozens of other Wolfram programs ran
on it at the same time (section 4.4). These times are examples, not limits: a slower or busier
computer takes longer. Do not close the window while it runs (an interrupted run leaves temporary
files behind, section 5). Wait for the line `101/101 checks passed; time ... s` and then the line
`exit code: 0`.

### 3.6 If it fails

| what you see | cause | what to do |
| --- | --- | --- |
| a message that the command `wolframscript` does not exist. Its wording depends on the terminal: PowerShell 7 prints `wolframscript: The term 'wolframscript' is not recognized as a name of a cmdlet, function, script file, or executable program.`; Windows PowerShell 5.1 prints `wolframscript : The term 'wolframscript' is not recognized as the name of a cmdlet, function, script file, or operable program.`; zsh (the standard shell of the macOS Terminal) prints `zsh: command not found: wolframscript`; bash prints `bash: wolframscript: command not found` (in the standard Ubuntu terminal: `wolframscript: command not found`) | WolframScript is not installed or not on the command path | do section 3.3, then open a NEW terminal window. On macOS with the Wolfram Engine: install `wolframscript.pkg` from the Wolfram Engine disk image (section 3.3, option A, step 2 (b)), or the stand-alone WolframScript installer from https://www.wolfram.com/wolframscript/. On macOS or Linux with Mathematica: install the stand-alone WolframScript (option B) |
| `Failed to open file at path: ...` | you are not in the repository root, or the path is mistyped | `cd` into the folder `Dirac_claude` that contains the folder `Revision`, and copy the command exactly. NOTE: in this case `wolframscript` still reports exit code 0, so the exit code alone does not prove success; always look for the line `101/101 checks passed` |
| a request for activation, or a message that the engine is not activated or has no valid licence | the Wolfram Engine has not been activated on this computer | run `wolframscript -activate` (internet needed) and enter your Wolfram ID and password yourself |
| within the first seconds: `Import::nffil: File ...\algebra\gammas.json not found during Import.` (on macOS and Linux the path is written with `/`), three `Part::partw: Part ... of $Failed[...] does not exist.` messages and `General::stop: Further output of Part::partw will be suppressed during this calculation.`, the line `FAIL  fixture_Clifford_relation  (<seconds> s)` (for example `(0. s)` or `(0.1 s)`), three `Part::partd: Part specification $Failed[S][[1,1]] is longer than depth of object.` messages (with `[[1,2]]`, `[[1,3]]`) and `General::stop: Further output of Part::partd will be suppressed during this calculation.`, then more `FAIL` lines up to `FAIL  primordial_vielbein`; after that nothing more is printed and the run seems to hang. Wolfram prints all these messages on the normal output (standard output), each after an empty line, not on the error stream | the input `Revision/algebra/gammas.json` is missing (an incomplete download, or only part of the repository was copied) | stop the run with Ctrl+C (if the window does not react, close it); download the repository again with `git clone` (section 3.4) and run again from its root. With the input missing, the run does not end by itself within minutes (the Wolfram kernel keeps computing and its memory grows: 659 MB after 4 minutes on the verification machine), and no output file is written. On Windows the stopped run leaves two files whose names start with `tmp_` in the folder `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` (one empty, one with a copy of the printed lines); delete them by hand as described in section 5 |
| `OpenWrite::noopen: Cannot open ...`, followed by `BinaryWrite::stream` and `Close::stream` messages, just before the last line | an output file or folder cannot be written (a read-only file, or a protected or synchronised folder) | the checks ran, but their result was NOT saved: the old output file stays as it was, and the exit code is still 0 (the script does not test whether its writes succeeded), so these messages are the only sign. Clone the repository into a normal folder of your own (for example your home folder) and run again |
| any line starting with `FAIL`, a last line `N/101 checks passed` with N smaller than 101, and exit code 1 | a check did not pass (this never happened on the verification machine) | do not edit anything; keep the printed output; open `Revision/pairing/reports/wolfram-pairing.json` in a text editor and search for `"FAIL"` to see the failed check and its detail; restore the committed files (section 5) and report the problem together with the output of `wolframscript -version` and `wolframscript -code '$Version'` |
| the run takes much longer than a few minutes, without messages | a slow or busy computer (the whole computation runs in one Wolfram kernel) | wait; on the verification machine, with many other jobs running at the same time, it took up to 4.6 minutes (section 4.4), and a slower or busier computer can take longer |

## 4. Expected output

### 4.1 Printed in the terminal

102 lines, followed by the `exit code:` line of the command. Lines 1 to 101 have the form
`PASS  <check name>  (<seconds since start> s)`, always in the same order: `fixture_Clifford_relation`,
`fixture_definitions`, `Gamma_properties`, `C_and_B_basic`, then the T1 and T2 kernels, the fields, T1
explicitly, T2, Q, and last `theory_file_deterministic`. The seconds differ from run to run and from
computer to computer, and Wolfram prints them in its own way: a whole number of seconds is printed
with a trailing dot, for example `(0. s)` (usually for the first two checks; the next two printed
`(0. s)`, `(0.1 s)` or `(0.2 s)` in the runs here) or `(137. s)`,
and some values are printed with many digits, for example `(9.200000000000001 s)` or
`(4.1000000000000005 s)`. Both are ordinary Wolfram number printing, not an error. The last line is

```text
101/101 checks passed; time <T> s
```

with `<T>` the run time measured by the kernel (between 119.62 s and 266.04 s in the eleven
verification runs of section 6; it may be printed with many digits, for example
`time 200.98000000000002 s`). These times are examples from one machine, not limits. No line starts
with `FAIL`, and nothing is printed on the error stream.

### 4.2 Exit code

`0` when every check passes, `1` when any check fails (shown by the `exit code:` part of the commands
in section 3.5). Remember that a mistyped path also gives `0` (section 3.6): the line
`101/101 checks passed` is the real verdict.

### 4.3 Files written, and how to check them

* `Revision/pairing/reports/wolfram-pairing.json`, 40151 bytes, 112 lines. Its eighth line is the
  summary:

  ```text
    "summary": {"passed": 101, "failed": 0, "total": 101},
  ```

* `Revision/pairing/pairing-theory.json`, 22430 bytes, 420 lines. Its seventh line is:

  ```text
    "status": "all checks of the report passed",
  ```

To see these two lines: in PowerShell

```powershell
Select-String -Path Revision/pairing/reports/wolfram-pairing.json -Pattern '"summary"'
Select-String -Path Revision/pairing/pairing-theory.json -Pattern '"status"'
```

and on macOS and Linux

```bash
grep '"summary"' Revision/pairing/reports/wolfram-pairing.json
grep '"status"' Revision/pairing/pairing-theory.json
```

Both files are written without time stamps and with LF line endings, so a successful run reproduces
the committed files byte for byte. The quickest check is `git status`: it prints
`nothing to commit, working tree clean` (if you have changed nothing else), because the two files were
rewritten with identical contents. To compare the fingerprints (sha256) with the table of section 2:
in PowerShell

```powershell
Get-FileHash -Algorithm SHA256 Revision/pairing/reports/wolfram-pairing.json,Revision/pairing/pairing-theory.json
```

(it prints the hashes in capital letters; compare ignoring case), on macOS

```bash
shasum -a 256 Revision/pairing/reports/wolfram-pairing.json Revision/pairing/pairing-theory.json
```

and on Linux

```bash
sha256sum Revision/pairing/reports/wolfram-pairing.json Revision/pairing/pairing-theory.json
```

### 4.4 Run time and memory on the verification machine

Windows 11 Pro for Workstations, Intel Core Ultra 9 275HX (24 logical processors), 191 GB memory,
while about a dozen other Wolfram kernels and other jobs ran on the same machine (CPU load about
70 %): wall-clock times 122.5 s and 147.6 s for the two measured runs (kernel-measured 119.62 s and
144.34 s); peak memory (working set) of the Wolfram kernel 247 MB in both runs, of `wolframscript`
itself 17 MB. Two more runs, made at the same time as each other, took 168.8 s and 166.9 s. The
two re-verification runs 5 and 6 (section 6), in a fresh clone, took 140.5 s and 188.8 s
(kernel-measured 136.98 s and 185.03 s), with a kernel peak memory of 246.7 MB and 246.8 MB. The
two runs 7 and 8 of the re-verification on 2026-10-07 (section 6), in a new fresh clone, while 14
other Wolfram processes ran and the processor load was 100 %, took 202.5 s and 200.6 s
(kernel-measured 198.79 s and 194.99 s), with a kernel peak memory of 246.3 MB and 246.0 MB. The
four runs of the independent review of this file on 2026-10-07 (processor load 100 %, about ten
other Wolfram kernels) took about 203 s, 214 s, 231 s and 223 s (kernel-measured 195.65 s,
208.55 s, 226.9 s and 217.70 s). The three runs 9, 10 and 11 of the re-verification after the
restart in the evening of 2026-10-07 (section 6), in a new fresh clone, with the processor load at
100 %, took 276.4 s (47 Wolfram processes running on the machine, and four interrupted probe runs
of section 6 at the same time), 221.5 s (38 Wolfram processes) and about 206 s (15 Wolfram kernels)
(kernel-measured 266.04 s, 214.82 s and 200.98 s), with a kernel peak memory of 246.1 MB in runs 9
and 10. The longest run so far therefore took 4.6 minutes; a slower or busier computer can take
longer. An earlier run on the same machine with less load, recorded in the documents of section 1.3,
took about 80 s.

## 5. Side effects

* **Files overwritten in the repository:** exactly two, both committed files:
  `Revision/pairing/pairing-theory.json` and then `Revision/pairing/reports/wolfram-pairing.json`,
  both written at the very end of the run. After a successful run their contents are identical to the
  committed ones; only their modification times change. If a check fails, both files are still
  written: the report `wolfram-pairing.json` then contains the `FAIL` verdicts and a summary line with
  `"failed"` greater than 0, and `pairing-theory.json` (which holds no verdicts at all, only the
  theorems and the names of the checks) gets the status `SOME CHECKS FAILED - see the report`. That
  status covers checks 1 to 100 only: it is computed before the last check,
  `theory_file_deterministic`, is made, so that check appears only in the report (if it alone failed,
  the theory file would still say `all checks of the report passed` while the report shows 100 of
  101). Either way both files then differ from the committed ones. If the run is stopped before its
  end (Ctrl+C, closing the window), neither file is written. If a file cannot be written (section
  3.6, `OpenWrite::noopen`), it keeps its old contents.
* **Files created in the repository:** none. (`git status --porcelain --ignored` printed nothing
  after every verification run, so no new file appeared, not even one that Git ignores.)
* **Temporary files:** the script itself makes none, but on Windows `wolframscript` writes two
  temporary files for every run into the folder
  `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` (that is
  `C:\Users\<you>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary`), each named `tmp_`
  followed by ten random letters and digits (for example `tmp_HakwYzqdQq`): an EMPTY file, created as
  `wolframscript` starts (0.07 to 0.2 s after the start in the runs here), and a file that the
  Wolfram kernel holds open and that receives a COPY of every line the run prints (with Windows line
  ends; it is created when the first line is printed, and in run 9 it reached 5961 bytes, exactly the
  size of the printed output). When the run ends by itself, `wolframscript` deletes both files; this
  was seen after normal runs (exit code 0), after a probe script ending with exit code 1 and after
  `Failed to open file at path`. When the run is INTERRUPTED (Ctrl+C, closing the window, or stopping
  `wolframscript` by force, as PowerShell's `Stop-Process -Force` does), both files STAY there; they
  hold at most a few kilobytes each and can be deleted by hand when no Wolfram program is running
  (see "Restoring the committed state" below). The folder is shared by every `wolframscript` run of
  your user account, so other `tmp_` files in it may belong to other runs. Eight verification runs
  (1, 2 and 5 to 10 of section 6) were given an empty private temporary folder (`TEMP` and `TMP`),
  and it was still empty after each run; that check does not cover `WolframScriptTemporary`, which
  `wolframscript` uses whatever `TEMP` and `TMP` say. Where `wolframscript` keeps such files on
  macOS and Linux was not checked (no such machine was available).
* **Processes:** `wolframscript` starts two Wolfram processes, one after the other (named
  `wolfram.exe` on the verification machine; the name depends on the version and the system, for
  example `WolframKernel` on macOS and Linux). First a short-lived licence query,
  `wolfram.exe -wlbanner -licenseinfo`, which lasts a fraction of a second (between 0.12 and 0.42 s
  in nine watched runs on the verification machine; on a fully loaded machine it can take longer:
  in run 7 it was still alive 2.8 s after the start); then one Wolfram kernel
  (`wolfram.exe -runfirst ... -linkmode Connect -linkname <name>_shm -mathlink`) that does the whole
  computation and talks to `wolframscript` through a shared-memory link on the same computer. Both
  have exited when the script ends (the script ends with `Exit[0]` or `Exit[1]`). Only one kernel
  computes, so the kernel limit of a licence does not matter.
* **Network:** none. The script reads its package and one input file and writes two files, all in the
  repository. In the re-verification runs 5 and 6 and the missing-input run (section 6) the
  complete TCP and UDP tables of the computer (IPv4 and IPv6) were read about 80 to 120 times per
  second for the whole run, and every entry belonging to `wolframscript`, to the licence query or to
  the kernel was recorded (a control script that opens a socket was recorded this way). The only
  entries were three local connections that the kernel makes to ITSELF while it starts (about 1.8 to
  2.6 s after the start, each lasting about 0.1 to 0.3 s): `127.0.0.1` to `127.0.0.1`, both ends
  owned by the kernel process, the same in every watched run and also in a script that only waits
  (`Pause[6]`). That is communication inside the kernel, not network access. That table reading
  (the Windows functions `GetExtendedTcpTable` and `GetExtendedUdpTable`) lists listening and
  connected TCP sockets, but not sockets in the state `Bound` (a local port taken, neither listening
  nor connected). Run 10 of the re-verification after the restart (2026-10-07) was therefore watched
  in two ways at once. The same table reading, about 87 times per second (9 ms between readings in
  the median, 0.11 s at most), again saw exactly three such connections, 3.7 to 4.3 s after the
  start, each 0.1 to 0.3 s long, all six `Established` ends `127.0.0.1` to `127.0.0.1` and owned by
  the kernel. PowerShell's `Get-NetTCPConnection` and `Get-NetUDPEndpoint`, which also list `Bound`
  sockets but are slow (about 1.4 readings per second), caught one of the three connections in one
  reading: its two `Established` ends (`127.0.0.1:52242` to `127.0.0.1:52243` and back) and, with
  the same port, an entry `0.0.0.0:52243` in the state `Bound` with no remote address
  (`0.0.0.0:0`), all three owned by the kernel; the fast table reading had read that connection 21
  times and never listed the `Bound` entry. The independent review of 2026-10-07 saw the same
  pattern with `Get-NetTCPConnection` (`0.0.0.0:60041` `Bound`, `127.0.0.1:60041` and
  `127.0.0.1:60040` `Established`, all owned by the kernel, 3.39 s after the start). A `Bound` entry
  is a local port that a socket of the kernel holds, not a connection to anything.
  There was no connection to any other address, no listening socket and no UDP endpoint; nothing at
  all was seen for `wolframscript` or for the licence query. A socket that exists for less than about
  13 ms (the time between two readings) could not be seen this way; the licence query lived 0.12 to
  0.42 s, so it was read roughly 13 or more times in each watched run. The earlier runs 1 to 4 had
  only been polled about once a second, which cannot see the licence query or the short local
  connections. In runs 8 and 9 the TCP and UDP tables were read only about once per second (243
  readings in 200 s and 270 readings in 277 s, a coarse watch on a fully loaded machine) and no
  entry of `wolframscript` or of its Wolfram processes was seen; such a coarse watch cannot see the
  short local connections of the kernel start, so it adds nothing to the fine watches of runs 5, 6
  and 10 except that no long-lived connection appeared. The
  Wolfram product itself contacts Wolfram's servers when you activate it (section 3.3); that is not
  part of this computation and cannot change its results.
* **Outside the repository:** the script itself writes nothing there. `wolframscript` writes the two
  temporary files described above (on Windows in `WolframScriptTemporary`; deleted again when the
  run ends by itself, left behind by an interrupted run). The Wolfram software keeps its own per-user
  settings and caches (on Windows under `C:\Users\<you>\AppData\Roaming\Wolfram`), as for any Wolfram
  session.
* **Restoring the committed state** (for example after a failed or interrupted run), from the
  repository root, on every system:

  ```text
  git checkout -- Revision/pairing/reports/wolfram-pairing.json Revision/pairing/pairing-theory.json
  ```

  On Windows, after an INTERRUPTED run, also delete the two temporary files it left behind. First
  end every Wolfram program (every running `wolframscript`, Mathematica, the Wolfram Engine), because
  the folder is shared by all of them; then, in PowerShell, list the files and delete them:

  ```powershell
  Get-ChildItem "$env:LOCALAPPDATA\Wolfram\WolframScript\WolframScriptTemporary" -Filter 'tmp_*'
  Remove-Item "$env:LOCALAPPDATA\Wolfram\WolframScript\WolframScriptTemporary\tmp_*"
  ```

  (Or type `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` into the address bar of
  File Explorer and delete the files whose names start with `tmp_`.) After a run that ended by
  itself there is nothing to delete.

## 6. Verification record

* **Date:** 2026-10-02 (runs 1 to 6 and the probes); re-verified on 2026-10-07 (runs 7 and 8 and a
  repeated wrong-path and missing-input probe), after the verification workflow had been interrupted
  by a session limit and relaunched: the re-verification re-checked every hash, count and output of
  this file instead of trusting the earlier record. Re-verified again in the evening of 2026-10-07
  (runs 9 to 11, interrupt probes and socket watches), after a second pause and restart, to check
  the five findings of an independent review of the 2026-10-07 record; all five were confirmed by
  new measurements and corrected in this file (see "Fixes made").
* **Commit verified:** `45d47343ae480df46e06689ed822b8f9a88a8030` (the head of `main` of
  https://github.com/once-ere/Dirac_claude.git when the fresh clone was made). The files of this set,
  its input and its outputs are identical (same sha256) at the later commit
  `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, used for run 3 and for the re-verification after an
  independent review of this file (runs 5 and 6 and the probes below, in a new fresh clone C of that
  commit), and at the commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670` (the head of `main` on
  2026-10-07), used for runs 7 and 8 in a new fresh clone D, and at the commit
  `b8a695d1faa7abe43b4b51eb666f25d250420fb7` (the head of `main`, locally and on GitHub, in the
  evening of 2026-10-07), used for runs 9 to 11 in a new fresh clone E and for the interrupt probes
  in a fresh clone F. None of the commits between `a4c5eda` and `b8a695d` changed any of the five
  files of section 2; the version of this provenance file written on 2026-10-07 was committed in
  `d806b00` (an earlier partial version in `72fc9ff`). The set's files were last changed in
  commit `70fab64` (2026-10-01). No uncommitted file was copied into the clones: only committed files
  were used.
* **Environment:** Windows 11 Pro for Workstations 10.0.26200 (build 26200.9457) for runs 1 to 6,
  reported as 10.0.26300 (build 26300, update revision 9457) for runs 7 to 11; Intel Core Ultra 9
  275HX, 24 logical processors, 191 GB memory; WolframScript 1.14.0, Wolfram 15.0.1 (July 2, 2026),
  Professional licence; Git 2.51.2.windows.1; PowerShell 7.6.6 and Git Bash (bash 5.2.37), plus
  Windows PowerShell 5.1.26100 for the exit-code and command-not-found probes; Ubuntu 24.04.4 under
  WSL 2 (bash 5.2.21, zsh 5.9) only for the command-not-found messages of bash and zsh.
* **Runs** (each with `wolframscript -file Revision/pairing/wolfram/verify_pairing.wls` from the
  repository root of a fresh `git clone https://github.com/once-ere/Dirac_claude.git`):

  | run | clone and shell | exit code | checks | last line | wall time | kernel peak memory | error stream |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | 1 | clone A (commit 45d4734), PowerShell | 0 | 101 PASS, 0 FAIL | `101/101 checks passed; time 119.62 s` | 122.5 s | 247 MB | empty |
  | 2 | clone A again (second run in the same clone), PowerShell | 0 | 101 PASS, 0 FAIL | `101/101 checks passed; time 144.34 s` | 147.6 s | 247 MB | empty |
  | 3 | clone B (commit c2b33cc) in a folder whose path contains a space; the exact PowerShell command of section 3.5 | 0 | 101 PASS, 0 FAIL | `101/101 checks passed; time 163.88 s` | 168.8 s | not measured | no message (merged into the log) |
  | 4 | clone A, the exact bash command of section 3.5 (Git Bash) | 0 | 101 PASS, 0 FAIL | `101/101 checks passed; time 161.54 s` | 166.9 s | not measured | no message (merged into the log) |
  | 5 | clone C (commit c2b33cc, new fresh clone for the re-verification), started from PowerShell 7 by a watching script (`Start-Process`, standard output and error stream into separate files) | 0 | 101 PASS, 0 FAIL | `101/101 checks passed; time 136.98 s` | 140.5 s | 246.7 MB | empty (0 bytes) |
  | 6 | clone C again (second run in the same clone), as run 5 | 0 | 101 PASS, 0 FAIL | `101/101 checks passed; time 185.03 s` | 188.8 s | 246.8 MB | empty (0 bytes) |
  | 7 | clone D (commit a4c5eda, new fresh clone of 2026-10-07), started from PowerShell 7 by a watching script (`Start-Process`, standard output and error stream into separate files, an empty private `TEMP`) | 0 | 101 PASS, 0 FAIL | `101/101 checks passed; time 198.79 s` | 202.5 s | 246.3 MB | empty (0 bytes) |
  | 8 | clone D again (second run in the same clone), as run 7 | 0 | 101 PASS, 0 FAIL | `101/101 checks passed; time 194.99 s` | 200.6 s | 246.0 MB | empty (0 bytes) |
  | 9 | clone E (commit b8a695d, new fresh clone of the evening of 2026-10-07), started from PowerShell 7 by a watching script (`Start-Process`, standard output and error stream into separate files, an empty private `TEMP` and `TMP`, a watch of `WolframScriptTemporary`) | 0 | 101 PASS, 0 FAIL | `101/101 checks passed; time 266.04 s` | 276.4 s | 246.1 MB | empty (0 bytes) |
  | 10 | clone E again (second run in the same clone), as run 9, with the two socket watches of section 5 | 0 | 101 PASS, 0 FAIL | `101/101 checks passed; time 214.82 s` | 221.5 s | 246.1 MB | empty (0 bytes) |
  | 11 | clone E again (third run), the exact bash command of section 3.5 (Git Bash), standard output and error stream into separate files | 0 | 101 PASS, 0 FAIL | `101/101 checks passed; time 200.98000000000002 s` | about 206 s | not measured | empty (0 bytes) |

  Runs 3 and 4 ran at the same time as each other; run 5 ran at the same time as the missing-input
  run; runs 7 and 8 ran one after the other while 14 other Wolfram processes of other jobs ran on the
  machine (processor load 100 %); runs 9, 10 and 11 ran one after the other while 47, 38 and 15
  Wolfram processes of other jobs ran (processor load 100 %), and run 9 also at the same time as the
  four interrupt probes below. In all eleven runs the 101 check names were printed in the same
  order (the order of the checks in the report), all `PASS`; the standard output of runs 5 to 10 had
  102 lines (run 11: 103, with its `exit code: 0` line), and in runs 7 and 8, and in runs 9 to 11, it
  was identical line by line apart from the times in parentheses. Those times vary: runs 9 and 11
  printed `(0. s)`, `(0. s)`, `(0.2 s)`, `(0.2 s)` for the first four checks, run 10 `(0. s)`,
  `(0. s)`, `(0.1 s)`, `(0.1 s)`.
* **Byte identity of the outputs** (`yes` = identical byte for byte; compared with `cmp` and sha256):

  | comparison | `Revision/pairing/reports/wolfram-pairing.json` | `Revision/pairing/pairing-theory.json` |
  | --- | --- | --- |
  | run 1 = committed | yes | yes |
  | run 2 = committed | yes | yes |
  | run 1 = run 2 | yes | yes |
  | run 3 = committed | yes | yes |
  | run 4 = committed | yes | yes |
  | run 5 = committed | yes | yes |
  | run 6 = committed | yes | yes |
  | run 5 = run 6 | yes | yes |
  | run 7 = committed | yes | yes |
  | run 8 = committed | yes | yes |
  | run 7 = run 8 | yes | yes |
  | run 9 = committed | yes (`git status`) | yes (`git status`) |
  | run 10 = committed | yes | yes |
  | run 11 = committed | yes | yes |
  | run 10 = run 11 | yes | yes |

  `git status --porcelain --ignored` was empty in each clone after each run (with the `* -text` rule
  of the repository's `.gitattributes`, an empty `git status` after a run means that Git found the
  rewritten files identical byte for byte to the committed ones), and `git status` in clones B, C, D
  and E printed `nothing to commit, working tree clean`. After runs 6, 8, 10 and 11 the eighth
  line of the report was `  "summary": {"passed": 101, "failed": 0, "total": 101},`, the seventh line
  of the theory file `  "status": "all checks of the report passed",`, and the sha256 of both files
  those of section 2. The checking commands of section 4.3 (`Select-String`, `Get-FileHash`,
  `git status`) were run in clones B, D and E and printed the summary line, the status line and the
  hashes of section 2. The
  macOS and Linux command of section 3.5 was run in Git Bash on Windows (the same bash syntax); no
  macOS or Linux machine was available for this record.
* **Failure modes tried:** a wrong path (`wolframscript -file verify_pairing.wls` outside the
  repository root) prints `Failed to open file at path: verify_pairing.wls` and gives exit code 0 in
  bash and in PowerShell; a missing input (a copy of the two set files without
  `Revision/algebra/gammas.json`, run twice: once for the first record, and once for the
  re-verification, from the files of commit c2b33cc, with standard output and error stream recorded
  separately) prints, within 4.1 s, 33 lines, all on standard output (the error stream stayed empty,
  0 bytes): the `Import::nffil` message, three `Part::partw` messages and a `General::stop`,
  `FAIL  fixture_Clifford_relation  (0. s)`, three `Part::partd` messages and a `General::stop`, then
  14 more `FAIL` lines up to `FAIL  primordial_vielbein  (0.7000000000000001 s)` (15 `FAIL` lines in
  all); after that it printed nothing more but kept computing (kernel peak working set 659 MB) until
  it was stopped after 240 s, and it wrote no output file; `wolframscript` was made to look missing (a
  `PATH` without it) and PowerShell 7 and Windows PowerShell 5.1 then printed the messages quoted in
  section 3.6, and the bash and zsh messages quoted there were printed by interactive bash and zsh
  shells (through a pseudo-terminal) on Ubuntu; a probe script ending with `Exit[1]` gives exit code 1
  in bash, PowerShell 7 and Windows PowerShell 5.1; the script's own
  file-writing function (copied into a probe script) applied to a read-only file prints
  `OpenWrite::noopen`, `BinaryWrite::stream` and `Close::stream`, leaves the file unchanged and the
  probe still exits with 0. Repeated on 2026-10-07 (commit a4c5eda): the wrong path printed
  `Failed to open file at path: verify_pairing.wls` (bash) and
  `Failed to open file at path: Revision/pairing/wolfram/verify_pairing.wls` (PowerShell 7, outside
  the repository root), both with exit code 0; the missing-input run printed the same 33 lines, all
  on standard output (error stream 0 bytes), the same messages in the same order and 15 `FAIL` lines
  up to `FAIL  primordial_vielbein  (0.8 s)`, its output stopped growing 4.7 s after the start, the
  kernel kept computing (peak working set 255.9 MB) until it was stopped after 60.7 s, and no output
  file was written. Interrupt probes in the evening of 2026-10-07 (fresh clone F of commit b8a695d;
  each run started in its own console window as a student would start it, the folder
  `WolframScriptTemporary` watched, and every new file in it attributed by its creation time and by
  the process holding it open): Ctrl+C after 25.7 s, closing the console window after 20 s, and a
  forced stop of `wolframscript` (`Stop-Process -Force`) after 20 s. In each case `wolframscript` and
  its kernel exited within 0.11 s, no file under `Revision/` was written, and both temporary files
  of the run stayed in `WolframScriptTemporary`: the empty one (created 0.07 to 0.18 s after the
  start) and the copy of the printed output, held open by the run's kernel until it ended (1178, 655
  and 570 bytes, each beginning `PASS  fixture_Clifford_relation  (0. s)`). A missing-input run (the
  two set files without `Revision/algebra/gammas.json`) stopped with Ctrl+C after 15 s ended the same
  way and left its empty file and a 1555-byte copy of its 33 printed lines, beginning with
  `Import::nffil` and containing `FAIL  fixture_Clifford_relation  (0. s)` (the independent review's
  missing-input run printed `(0.1 s)` there). A probe script ending with `Exit[1]` and the wrong-path
  command left nothing: the temporary file of each was deleted when `wolframscript` ended, as were
  both files of runs 9 and 10 (the empty one created 0.13 to 0.2 s after the start, the output copy
  held by the kernel and 5961 and 5860 bytes long). The independent review had found the same: two
  `tmp_` files per run, deleted at the normal end of its run, left behind by its Ctrl+C probe and its
  missing-input probe; the missing-input probe of the 2026-10-07 re-verification had also left two
  such files (its record had looked only at `TEMP` and `TMP`). The files left by the probes of this
  record were deleted afterwards, by name, with `Remove-Item`; the two cleanup commands of section 5
  were tried, in PowerShell 7 and Windows PowerShell 5.1, on a copy of the folder layout (they
  removed the `tmp_` files and kept another file).
* **Process and network probes:** runs 5 and 6, the missing-input run, five probe scripts that only
  wait (`Pause[6]`) and one socket control script (nine watched runs) were watched by a loop that
  listed the `wolfram.exe` processes about 80 to 175 times per second and read the parent and command
  line of every new one at once (through the Windows function `NtQueryInformationProcess`); queries
  of the Windows process list through `Get-CimInstance` take about 0.15 to 0.19 s here and missed the
  licence query in four earlier probes. Every watched run showed the same two children of
  `wolframscript`: the licence query `wolfram.exe -wlbanner -licenseinfo`, first seen 0.04 to 0.16 s
  after the start and gone 0.12 to 0.42 s later, and then the kernel, alive until the end; none was
  left after `wolframscript` exited. The kernel's peak memory (working set) was 246.7 MB in run 5 and
  246.8 MB in run 6. A control script that opens a local server socket (`SocketOpen[48456]`) was
  seen by the same socket-table reading (a listening entry on `127.0.0.1`, owned by its kernel),
  which shows that the reading works. Runs 7 and 8 were watched more coarsely (`Get-CimInstance`
  for the children of `wolframscript`, a few readings per second on the fully loaded machine) and
  showed the same two children: in run 7 the licence query was first seen 0.18 s after the start
  and was still alive at 2.83 s, the kernel was first seen at 0.53 s; in run 8 the licence query was
  seen once, at 0.37 s, and the kernel first at 4.18 s (that watch loop was slower because it also
  read the socket tables); in both runs the kernel stayed until the end and no Wolfram process was
  left after `wolframscript` exited. Runs 9 and 10 were watched the same coarse way (about one
  reading per second): the licence query was seen once (0.02 and 0.03 s after the start), the kernel
  first at 8.88 s and 3.89 s (the machine was fully loaded) and until the end, with a peak working
  set of 246.1 MB in both runs; no Wolfram process was left. The two socket watches of run 10 are
  described in section 5.
* **Fixes made:** none were needed to the set; no script, package, input or output was changed.
  This provenance file itself was corrected after the independent review: the macOS installation of
  the Wolfram Engine now includes `wolframscript.pkg` (as in Wolfram's own instructions,
  https://support.wolfram.com/46070), and the Windows and Linux installation steps follow Wolfram's
  articles 46069 and 46072; the command-not-found messages are given for PowerShell 7, Windows
  PowerShell 5.1, zsh and bash as measured; the missing-input messages now include `Part::partd` and
  `General::stop` and say that they go to standard output; whole-number times such as `(0. s)` are
  explained; the side effects now list the short-lived licence query process, the network
  observation with its exact coverage, and the precise contents of the two output files after a
  failed check. On 2026-10-07 (re-verification after the restart) again no fix to the set was
  needed; this file was updated with the measured truth: the documents and notebooks that now cite
  or read the outputs (section 1.3), the size of the repository download (section 3.4), the run-time
  ranges including runs 7 and 8 (sections 3, 4.1 and 4.4), the longer life of the licence query on
  a fully loaded machine (section 5) and runs 7 and 8 with their byte-identity results (this
  section). In the evening of 2026-10-07 the five findings of the independent review of that
  version were re-measured (runs 9 to 11 and the probes above) and all five confirmed; again no fix
  to the set was needed, and this file was corrected: (1) section 5 no longer says "Temporary
  files: none" but describes the two `tmp_` files that `wolframscript` writes to
  `WolframScriptTemporary` on Windows, deleted at a normal end and left behind by an interrupted
  run, with the cleanup commands (section 5, the missing-input row of section 3.6, and the
  "Outside the repository" item); (2) the run times are given as examples, not limits, with the
  longest measured run (276.4 s) (sections 3.1, 3.5, 3.6, 4.1 and 4.4, including the review's four
  runs); (3) the printed times of the first checks and of the missing-input `FAIL` line vary
  between runs (sections 3.6 and 4.1); (4) the socket entries are described as measured with both
  tools, including the `Bound` entry that only `Get-NetTCPConnection` lists (section 5); (5) the
  statements about commits (sections 2 and 6). Sections 1.3 (the textbook as it stands at
  `b8a695d`) and 3.4 (the size of the clone) were brought up to date at the same time.
* **Known limitation (not changed):** the script does not test whether writing its two output files
  succeeded, so in a read-only folder it ends with exit code 0 although nothing was saved (section
  3.6 says how to recognise this). This never affects a run in a normal, writable clone.
* **Open discrepancies:** none. The counts in the citing documents (101 checks, 101 PASS, 0 FAIL;
  at `b8a695d` also the stored output of the notebook `00c_honesty_ledger.ipynb`, work in progress,
  which prints `101 of 101` for `wolfram-pairing.json`) agree with the reproduced report.
