# WolframScript provenance: reading the author's notebook `Generalized _Kronecker_Delta_4+4.nb`

Set: the folder `Revision/gkd_lovelock/notebook_reading/`, which holds two WolframScript scripts,
`lovelock_extract_nb_inputs.wls` and `lovelock_export_nb_image.wls`, and one small Python helper,
`lovelock_digest_nb_inputs.py`, that turns the text written by the first script into the committed digest.

At a glance (verified on 2026-10-02 at commits `45d47343ae480df46e06689ed822b8f9a88a8030` and
`c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, and verified again on 2026-10-07 at commits
`a4c5eda1df069a43a55ff8b57148f5de8edd1670`, `8cbd03a02f7771bce9e199f5d48cd41a979f1f06` and
`5e4654e5a99f5857f7ba332bcdadb1c8ce2c29f2`; Windows 11, Wolfram 15.0.1, WolframScript 1.14.0, Python 3.14.5):

* EXECUTES OK: all three scripts end with exit code 0 and write nothing to standard error.
  The extraction prints `input cells written: 58`, the digest prints `58 input cells`, and the image export prints
  `{1372, 435}` and `28229 bytes (117 bytes of text/time chunks removed)`.
* Both committed outputs, `Revision/gkd_lovelock/results/notebook-input-cells.txt` and
  `Revision/gkd_lovelock/results/notebook-in68-image.png`, were reproduced BYTE FOR BYTE in thirteen runs from
  eight fresh clones: seven runs from four clones on 2026-10-02 (three in the first verification, four more in a
  re-verification after an independent review) and six runs from four more clones on 2026-10-07 (three in a
  verification after a restart, three more in a re-verification after a second independent review; part 6).
  After every run `git status` shows no change.
* The uncommitted full text `build/lovelock_nb_inputs.txt` was byte-identical in every run.
* Run time on a shared 24-core machine: on 2026-10-02 extraction 3.5 s and 4.9 s, digest 0.4 s and 0.7 s, image
  export 5.9 s and 6.6 s (runs 1 and 2); on 2026-10-07, while other jobs kept the processor busy (up to 100 %),
  extraction 3.7 to 8.7 s, digest 0.2 to 0.7 s, image export 9.3 to 11.4 s (runs 8 to 13). The whole set takes
  about 10 to 25 seconds (part 4.4).
* No fix was needed and no file of the set was changed. No scientific discrepancy is open. Two notes for
  students (part 5): the image export makes Wolfram 15.0.1 try to fetch an add-on from the internet, and it prints
  the harmless message `RegisterFormat::interr: ... ImageMetadataTools could not be installed.`.

This file is written for a student who has never used the Wolfram Language, WolframScript or Python. It
contains every instruction you need to run the set.

---

## 1. What this set is and what it computes

### 1.1 In plain words

The author of this project wrote a Mathematica notebook, `Generalized _Kronecker_Delta_4+4.nb`. The name
contains a space between `Generalized` and `_Kronecker`. The notebook is stored in the top folder of the
repository. A notebook is a file of "cells":

* **input cells** hold what the author typed (definitions, commands);
* **output cells** hold what Mathematica answered.

The later calculations in `Revision/gkd_lovelock/` had to be done WITHOUT looking at the author's answers,
so the author's results could not steer them. This set was written to read the notebook in the most
limited way that was still useful:

1. **`lovelock_extract_nb_inputs.wls`** opens the notebook file as data. It does not run the notebook. It
   picks out ONLY the input cells (58 of them). It turns each one into plain text (Wolfram "InputForm"),
   wrapped in `HoldForm[...]` so that nothing in it is evaluated, and writes all 58 texts to
   `build/lovelock_nb_inputs.txt`. That file is about 9.9 MB, almost all of it the pixels of one picture, and
   it is not committed. Output cells are never converted, printed or used.
2. **`lovelock_digest_nb_inputs.py`** reads that 9.9 MB text and writes a short summary, the "digest"
   `Revision/gkd_lovelock/results/notebook-input-cells.txt`, which is committed. For every input cell, in file
   order, the digest gives the cell's label as stored in the file (for example `In[87]:=`), the length of its
   text in characters, and its first 160 characters.
3. **`lovelock_export_nb_image.wls`** opens the notebook again and takes the input cell labelled `In[101]:=`.
   That cell holds no formula. It is a PICTURE of equation (4.38) of Lovelock and Rund (the Lovelock
   tensors), which the author pasted into the notebook. The author calls this cell `In[68]`. The script saves
   that picture as `Revision/gkd_lovelock/results/notebook-in68-image.png` (1372 x 435 pixels). It removes the
   date and text "chunks" that Wolfram's PNG writer adds, so that every run gives exactly the same bytes.

Two facts were taken from what this set shows:

* The cell labelled `In[87]:=` in the file (the author's `In[54]`) is the author's definition of the
  generalized Kronecker delta:
  `kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]`.
* The cell labelled `In[101]:=` (the author's `In[68]`) is the image of Lovelock's equation (4.38). The
  Lovelock tensors computed in `Revision/gkd_lovelock/code` are those of that equation, read from the PNG.

The set computes no physics and has no pass/fail checks of its own. What it produces is evidence: what was
read from the author's notebook and in what form. Its "verdict" is the counts it prints (58 cells, a
1372 x 435 image of 28229 bytes) together with the byte identity of its two committed outputs.

### 1.2 Documents that cite its results

* `Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md`, section "What was read from the author's
  notebook" and the note dated 2026-10-01. It names both scripts and both committed outputs, quotes the `kδ`
  definition found in `In[87]:=`, and gives the three commands of part 3.5.
* `Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls`, check `definition_is_the_authors_verbatim`. It
  requires the exact `kδ` text recorded in `PROVENANCE_OF_THE_COMPUTATION.md`, which is the text this set
  extracted.
* `Revision/gkd_lovelock/code/src/lovelock.rs` ("The Lovelock tensors of equation (4.38) (the author's
  In[68])"), with `lib.rs` and `main.rs` of the same crate: they compute the tensors of the equation shown by
  `notebook-in68-image.png`.
* `Revision/workflows/wave1_review_and_fix.json`, review findings 23 and 24 and their fixes. Finding 23: the PNG
  was not deterministic; fixed by stripping the text and time chunks. Finding 24: the digest had no producer;
  fixed by adding `lovelock_digest_nb_inputs.py` and the `$LOVELOCK_NB_INPUTS` / `build/` output of the extraction.
* `HANDOFF.md`, section 0.4b, which describes the GKD and Lovelock task and the image cell `In[68]`.
* `Revision/textbook/notebooks/src/01c_generalized_delta.py`, the notebook
  `Revision/textbook/notebooks/01c_generalized_delta.ipynb` built from it, and its
  `01c_generalized_delta.PROVENANCE.md`. These three files were first committed on 2026-10-02 (commit `3f0a577`,
  07:35 local time, after this set's verification of that day), in a snapshot of work IN PROGRESS, and were last
  changed on 2026-10-07; the notebook's own provenance file records that its `nbkit check` PASSED (on 2026-10-07
  in the version verified here). That notebook belongs to the textbook and is not part of this set; it was not
  verified here. The notebook READS the digest `notebook-input-cells.txt` and quotes its cells `In[29]:=` (the
  declaration of the author's metric with the signature (4,4)), `In[32]:=` (the product of two Levi-Civita
  tensors) and `In[87]:=` (the `kδ` definition). It does not use the PNG.

---

## 2. The files

### 2.1 The scripts of the set

| file | lines | bytes | sha256 |
| --- | --- | --- | --- |
| `Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls` | 22 | 1611 | `53fea71f0a641bdcf0446eeff0ef5c971cb415f6c342d17a94cdf7968bc41a0c` |
| `Revision/gkd_lovelock/notebook_reading/lovelock_digest_nb_inputs.py` | 63 | 2593 | `6fa65b733a502a50c1a88fa7bf4cd506843375fa66a645104c9a693ed016bf6d` |
| `Revision/gkd_lovelock/notebook_reading/lovelock_export_nb_image.wls` | 27 | 1869 | `cff8aafe735667c5464531a9ef80ea83a4dcb87dcb2b228db172f3b1ebb2e6b3` |

The scripts load no package and need no other script. All three were last changed in commit `70fab64` (2026-10-01).

### 2.2 Inputs it reads

| input | read by | sha256 |
| --- | --- | --- |
| `Generalized _Kronecker_Delta_4+4.nb` (repository root; 1,915,427 bytes, 53,277 lines) | both `.wls` scripts | `23bb4e0c70943e766d9b081a3a399ef29664889aad088041329ce2e065b80afb` |
| `build/lovelock_nb_inputs.txt` (written by the extraction; see 2.3) | the digest | depends on the line endings of your system (2.3) |
| environment variable `LOVELOCK_NB_INPUTS` (optional) | the extraction and the digest | - |

The notebook is only READ. Neither script writes to it, and its sha256 was unchanged after every verification
run. The digest reads its input from the first command-line argument if one is given. Otherwise it reads
`$LOVELOCK_NB_INPUTS` if that variable is set, and otherwise `build/lovelock_nb_inputs.txt` under the
repository root. The digest finds the repository root from its own location, so it works from any current folder.

### 2.3 Outputs it writes

| output | written by | committed? | bytes | sha256 |
| --- | --- | --- | --- | --- |
| `build/lovelock_nb_inputs.txt` (or the path in `$LOVELOCK_NB_INPUTS`) | extraction | no; the folder `build/` is ignored by `.gitignore` (rule `/build/`) | 9,923,611 on Windows | `52f611d470c75faaec02b4e3695329f454e127077b92068b3b460942f49276a6` on Windows |
| `Revision/gkd_lovelock/results/notebook-input-cells.txt` (or the path after `--out`) | digest | yes; OVERWRITTEN by a run | 6,153 (65 lines, UTF-8, LF) | `1a889643b1b69f8ee5cdc822b2dd8478229ee32b89a1d394440c7d4e5c1418ce` |
| `Revision/gkd_lovelock/results/notebook-in68-image.png` | image export | yes; OVERWRITTEN by a run | 28,229 | `0e7a7e6c89d5fd918c699a74d12455be3c52a30367fa9cabae6f91b5594a0ab8` |

About `build/lovelock_nb_inputs.txt`. It holds 58 blocks, one per input cell, each written as
`=== <label>`, then the text on one line, then an empty line: 174 lines in all. The extraction writes "new line"
in the way your operating system does it. On Windows every line ends in CR LF, giving the 9,923,611 bytes above.
On macOS and Linux lines end in LF only, so the file should be 174 bytes shorter: 9,923,437 bytes with sha256
`f4aa92fd72b4781bff5364da83637662e372085047dd549f850b2d5842f0317e`. That figure was obtained by converting the
Windows file, not by a run on macOS or Linux. The digest is the same either way. Python reads both line endings
alike, and the digest made from the LF version was byte-identical to the committed one.

About the PNG. Its chunks are `IHDR pHYs IDAT IDAT IDAT IDAT IEND` (1372 x 435 pixels, 8-bit RGB). The
uncompressed pixel bytes (1,790,460 bytes = 1372 x 435 x 3) have sha256
`4efe457deb90302eb2cc564798964305a07291bf194715dab8368cbf7c78a198`. The decompressed image data stream
(the IDAT data with its filter bytes, 1,790,895 bytes) has sha256
`8bb2905c8a73e13152e0688348acc73493cb15e86c562813cfdfdd47a6cb1c98`. Its first 16 hex digits, `8bb2905c8a73e131`,
are the pixel digest recorded for the first rendering in `Revision/workflows/wave1_review_and_fix.json` (finding
23). So the picture itself has not changed since it was first read.

---

## 3. How to run it (complete instructions)

You need four things:

* git;
* a Wolfram kernel with WolframScript;
* Python 3;
* a copy of the repository.

About 1 GB of free memory is plenty: the Wolfram kernel peaked at about 0.2 GB. You also need about 1 GB of
disk for the repository (a fresh clone measured 751 MB on 2026-10-07, of which 233 MB is git's own folder
`.git`; the repository grows as the project grows) and 10 MB for `build/lovelock_nb_inputs.txt`.

### 3.1 Install git

* Windows: install "Git for Windows" from https://git-scm.com/download/win and accept the defaults. Or, in
  PowerShell, run `winget install --id Git.Git -e`. Close and reopen PowerShell afterwards.
* macOS: in Terminal run `xcode-select --install`.
* Linux (Debian or Ubuntu): `sudo apt update` then `sudo apt install git`. On Fedora: `sudo dnf install git`.

Check: `git --version` prints a version.

### 3.2 Install a Wolfram kernel and WolframScript

Either of the two options below works. The verification used Wolfram 15.0.1 with WolframScript 1.14.0.

* **The free Wolfram Engine for Developers.** Downloading it, getting its free licence, installing it and
  activating it are separate steps, done in this order.
  1. **Download.** Open https://www.wolfram.com/engine/ in a browser. The page detects your system and shows the
     latest version (15.0 on 2026-10-02). Click "Start Download". No sign-in is needed for the download itself.
     What you receive (checked on 2026-10-02):
     * Windows: `WolframEngine_15_WIN_DLM.exe`. This is a small "download manager" (DLM). Run it and follow its
       steps; it fetches the full installer. To get the full installer directly as one file instead, open
       `https://account.wolfram.com/dl/WolframEngine?version=15.0&platform=Windows&downloadManager=false&includesDocumentation=false`
       in the browser: it gives `WolframEngine_15_WIN.zip`. Extract that file (right-click it, "Extract All")
       and run the setup program it contains.
     * macOS: `WolframEngine_15_MAC_DLM.dmg` (a download manager). The full installer as one file,
       `WolframEngine_15_MAC.dmg`, comes from the same link with `platform=Mac` in place of `platform=Windows`.
     * Linux: `WolframEngine_15_LIN.sh` (the full installer).
  2. **Get the free licence.** After the download starts, the page shows "Next Step: To get your free license,
     sign in and accept the terms of use" and a button "Get your license". Click it, sign in with your Wolfram ID
     (if you have none, the page lets you create one; it is free) and accept the terms of use. Do this BEFORE
     step 5: without it, `wolframscript -activate` cannot activate the engine.
  3. **Install.**
     * Windows: run the installer (from the download manager or from the extracted `.zip`) and accept the
       defaults. WolframScript is installed with it and put on the PATH. Alternatively, the page lists the
       package manager command `winget install WolframEngine` (on 2026-10-02 winget listed the package
       `WolframResearch.WolframEngine`, version 15.0.0).
     * macOS: open the `.dmg` and follow its instructions. Alternatively, with Homebrew:
       `brew install --cask wolfram-engine`.
     * Linux: in a terminal, in the folder where the file was saved, run `sudo bash WolframEngine_15_LIN.sh`
       and accept the defaults. Alternatively, on Debian or Ubuntu the page lists
       `cd /tmp && wget https://wolfr.am/wolfram-engine.deb && sudo apt install ./wolfram-engine.deb`.
  4. If `wolframscript` is still not found afterwards (in a NEW terminal window), download the separate
     WolframScript installer for your system from https://www.wolfram.com/wolframscript/ and run it.
  5. **Activate** the engine once. This needs the internet. Run `wolframscript -activate`, then type your
     Wolfram ID (an e-mail address) and password when asked.

  The download links above were checked on 2026-10-02 by following the page's links (HTTP redirects only;
  nothing was downloaded or installed). They were checked again on 2026-10-07 with HTTP `HEAD` requests (nothing
  downloaded): the `account.wolfram.com/dl/WolframEngine?...` link redirects to `WolframEngine_15_WIN.zip`
  (`platform=Windows`), `WolframEngine_15_MAC.dmg` (`platform=Mac`) and `WolframEngine_15_LIN.sh`
  (`platform=Linux`), and with `downloadManager=true` to `WolframEngine_15_WIN_DLM.exe`; `wolfr.am/wolfram-engine.deb`
  redirects to `wolfram-engine_15.0.0_amd64.deb`. All of them lie in folders named `15.0.0.0` on Wolfram's
  download server, so the free Engine you download is version 15.0.0, not the 15.0.1 used in this verification
  (see part 6 about other versions). The installers themselves were not run during this verification, because
  Wolfram 15.0.1 was already installed on the verification machine.
* **Mathematica / Wolfram (the desktop product).** If it is installed and activated, WolframScript comes with
  it. On Windows it is on the PATH
  (`C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe`). On macOS, if `wolframscript` is not
  found, install it from https://www.wolfram.com/wolframscript/.

Check, in a NEW terminal window (Windows: PowerShell; macOS: Terminal; Linux: any shell):

```text
wolframscript -version
wolframscript -code '$Version'
```

The first command prints, for example, `WolframScript 1.14.0 for Microsoft Windows (64-bit)`. The second prints,
for example, `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. Keep the single quotes around
`$Version`: in PowerShell and in bash they stop the shell from treating `$Version` as one of its own variables.

### 3.3 Install Python 3

The digest script uses only Python's standard library, so no `pip install` is needed and no private
environment has to be created. It was verified, byte for byte, with Python 3.11.15, 3.12.13, 3.13.13, 3.14.4 and
3.14.5. Older versions were not tested.

* Windows:
  1. Download the "Windows installer (64-bit)" of Python 3.11 or newer from https://www.python.org/downloads/.
  2. Run it, and on its FIRST screen tick "Add python.exe to PATH". Then click "Install Now".
  3. Open a new PowerShell. The command is `python`.
* macOS: download the macOS installer of Python 3.11 or newer from https://www.python.org/downloads/ and run it.
  The command is `python3`.
* Linux: Ubuntu 24.04 and Fedora already contain a suitable `python3`. If it is missing, run
  `sudo apt install python3` (Debian/Ubuntu) or `sudo dnf install python3` (Fedora). The command is `python3`.

Check: `python --version` (Windows) or `python3 --version` (macOS, Linux) prints `Python 3.11` or newer.

### 3.4 Get the repository

Windows (PowerShell). A short folder such as `C:\work` avoids the Windows limit on path length.

```powershell
New-Item -ItemType Directory -Force C:\work
Set-Location C:\work
git clone https://github.com/once-ere/Dirac_claude.git
Set-Location C:\work\Dirac_claude
```

macOS and Linux:

```bash
mkdir -p ~/work
cd ~/work
git clone https://github.com/once-ere/Dirac_claude.git
cd ~/work/Dirac_claude
```

You are now in the **repository root**: the folder that contains `Revision` and the notebook
`Generalized _Kronecker_Delta_4+4.nb`. Every command below is typed there.

The scripts find the notebook through the CURRENT folder, so they must be started from the repository root.
The repository's `.gitattributes` file (`* -text`) makes git check out every file byte for byte, so
your git settings for line endings do not matter.

### 3.5 Run the set

Run the three commands in this order. The second needs the file written by the first. The third does not
depend on the other two.

Windows PowerShell (from the repository root):

```powershell
wolframscript -file Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls
$LASTEXITCODE
python Revision/gkd_lovelock/notebook_reading/lovelock_digest_nb_inputs.py
$LASTEXITCODE
wolframscript -file Revision/gkd_lovelock/notebook_reading/lovelock_export_nb_image.wls
$LASTEXITCODE
git status --porcelain
```

macOS and Linux (from the repository root):

```bash
wolframscript -file Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls
echo $?
python3 Revision/gkd_lovelock/notebook_reading/lovelock_digest_nb_inputs.py
echo $?
wolframscript -file Revision/gkd_lovelock/notebook_reading/lovelock_export_nb_image.wls
echo $?
git status --porcelain
```

Forward slashes work on Windows too. The lines `$LASTEXITCODE` and `echo $?` print the exit code of the
command before them, and `0` means it succeeded. The last line, `git status --porcelain`, must print NOTHING:
that means both committed outputs were rewritten with exactly the committed bytes.

What you see (times measured on the verification machine; they are longer on a busy or slower computer):

* the extraction prints NOTHING while it works. Its only `Print` is its last statement, so its one line appears
  when it has finished, after about 2 to 9 seconds, and the command ends right after it;
* the Python command ends within a second;
* the image export prints `{1372, 435}` once it has read the notebook (after about 4 to 6 seconds on
  2026-10-07), then nothing for a few more seconds while it writes the PNG, then its remaining lines, and ends
  (after about 5 to 12 seconds in all).

Part 4 shows the exact output.

Optional settings (none is needed for the normal run):

| setting | effect |
| --- | --- |
| environment variable `LOVELOCK_NB_INPUTS` | the extraction writes the full text to this path instead of `build/lovelock_nb_inputs.txt`, and the digest reads it from there |
| `python ... lovelock_digest_nb_inputs.py <INPUT>` | the digest reads `<INPUT>` instead |
| `python ... lovelock_digest_nb_inputs.py --out <PATH>` | the digest writes to `<PATH>` instead of the committed `notebook-input-cells.txt`, which is then left untouched |

To run the extraction and the digest WITHOUT touching the repository at all, write both files to your
temporary folder. Windows PowerShell:

```powershell
$env:LOVELOCK_NB_INPUTS = "$env:TEMP\lovelock_nb_inputs.txt"
wolframscript -file Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls
python Revision/gkd_lovelock/notebook_reading/lovelock_digest_nb_inputs.py --out "$env:TEMP\notebook-input-cells.txt"
Remove-Item Env:LOVELOCK_NB_INPUTS
(Get-FileHash -Algorithm SHA256 "$env:TEMP\notebook-input-cells.txt").Hash
```

macOS and Linux:

```bash
LOVELOCK_NB_INPUTS=/tmp/lovelock_nb_inputs.txt wolframscript -file Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls
LOVELOCK_NB_INPUTS=/tmp/lovelock_nb_inputs.txt python3 Revision/gkd_lovelock/notebook_reading/lovelock_digest_nb_inputs.py --out /tmp/notebook-input-cells.txt
shasum -a 256 /tmp/notebook-input-cells.txt
```

On Linux, `sha256sum` can be used instead of `shasum -a 256`. The hash printed must be the digest's sha256 of
part 2.3. PowerShell prints it in capital letters (`1A889643...`). This way was verified on Windows: the file
was byte-identical to the committed digest.

This way leaves two files in your temporary folder: `lovelock_nb_inputs.txt` (about 9.9 MB) and
`notebook-input-cells.txt` (6,153 bytes). Delete them when you are done.

Windows PowerShell:

```powershell
Remove-Item "$env:TEMP\lovelock_nb_inputs.txt", "$env:TEMP\notebook-input-cells.txt"
```

macOS and Linux:

```bash
rm /tmp/lovelock_nb_inputs.txt /tmp/notebook-input-cells.txt
```

The image export has no such option. It always writes the committed path.

### 3.6 If it fails

| what you see | likely cause | what to do |
| --- | --- | --- |
| `wolframscript` is "not recognized" / "command not found" | WolframScript is not installed or not on the PATH | install it (part 3.2), then open a NEW terminal. Or call it by its full path, for example `& "C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe" -file ...` in PowerShell |
| a request to activate, or a licence error | the Wolfram Engine is not activated | run `wolframscript -activate` and sign in with your Wolfram ID |
| `python` opens the Microsoft Store, or is "not recognized" (Windows) | Python is not installed, or "Add python.exe to PATH" was not ticked | install Python (part 3.3), or use `py -3` in place of `python` |
| `Failed to open file at path: Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls` (or `..._export_nb_image.wls`), exit code still `0`; and for the digest a line that begins with the path of Python and continues `can't open file '...lovelock_digest_nb_inputs.py': [Errno 2] No such file or directory` (observed on Windows, started from the subfolder `Revision` of `C:\work\Dirac_claude`; Python writes the path inside the quotes with every backslash doubled: `C:\Python314\python.exe: can't open file 'C:\\work\\Dirac_claude\\Revision\\Revision\\gkd_lovelock\\notebook_reading\\lovelock_digest_nb_inputs.py': [Errno 2] No such file or directory`), exit code `2` | the terminal is not in the repository root (for example you are still in `C:\work`, or in a subfolder such as `Revision`), so the commands of part 3.5, which name the scripts relative to the repository root, do not find the script files. Nothing is run and nothing is written | go to the folder that contains `Revision` and the `.nb` file (part 3.4: `Set-Location C:\work\Dirac_claude` or `cd ~/work/Dirac_claude`) and run again |
| `Get::noopen: Cannot open ...\Generalized _Kronecker_Delta_4+4.nb.` followed by `input cells written: 0 -> ...`, exit code still 0 | the extraction script WAS found, because it was called by another path (for example its full path), but the terminal was not in the repository root. The script looks for the notebook in the CURRENT folder, does not find it, and writes an EMPTY file `build/lovelock_nb_inputs.txt` in the current folder | go to the repository root (part 3.4) and run the commands exactly as in part 3.5. Delete the stray `build` folder with its empty file that appeared in the wrong folder |
| `Get::noopen ...`, then `First::nofirst` (twice), `ToExpression::notstrbox`, `ImageDimensions::imginv`, the printed line `ImageDimensions[First[{}]]` (in place of `{1372, 435}`), `RegisterFormat::interr`, `OpenWrite::noopen`, `BinaryWrite::stream`, `Close::stream`, and a misleading `wrote ...` line with a wrong size (observed: `1371 bytes`), exit code still 0 | the image export script was called by another path (for example its full path) while the terminal was not in the repository root; nothing was written | go to the repository root and run again. Never trust the `wrote` line unless it says `28229 bytes` |
| `FileNotFoundError: [Errno 2] No such file or directory: '...lovelock_nb_inputs.txt'`, exit code 1 | the digest ran before the extraction, or `LOVELOCK_NB_INPUTS` points to a file that does not exist | run the extraction first (part 3.5), with the same `LOVELOCK_NB_INPUTS` setting |
| `RegisterFormat::interr: An internal error occurred: ImageMetadataTools could not be installed.` | normal with Wolfram 15.0.1 when the kernel cannot download an optional add-on (part 5) | nothing; the PNG is still written correctly. Check the `wrote ...: 28229 bytes` line and `git status` |
| `ERROR: not a PNG`, exit code 2 | Wolfram's PNG writer returned something that is not a PNG file (never seen; would point to a broken installation) | run `wolframscript -code '$Version'`, reinstall or update Wolfram, and run again |
| `git status --porcelain` lists `notebook-in68-image.png` | you use another Wolfram version, or the add-on of part 5 was installed and changed the file's bytes | compare the PICTURE instead of the bytes, with the pixel check of part 4.3. Then restore the committed file (part 5) |
| `git status --porcelain` lists `notebook-input-cells.txt` | another Wolfram version formats InputForm text differently, or the notebook file was changed | see the differences with `git diff -- Revision/gkd_lovelock/results/notebook-input-cells.txt`. Check the notebook's sha256 (part 2.2) and restore with `git checkout` (part 5) |

---

## 4. Expected output

### 4.1 Standard output

The lines below are what you see when the repository root is `C:\work\Dirac_claude`. Your own folder appears
in place of it. On macOS and Linux the paths use `/`, for example `/home/you/work/Dirac_claude/build/lovelock_nb_inputs.txt`.

Extraction:

```text
input cells written: 58 -> C:\work\Dirac_claude\build\lovelock_nb_inputs.txt
```

Digest:

```text
58 input cells -> C:\work\Dirac_claude\Revision\gkd_lovelock\results\notebook-input-cells.txt
```

Image export (the empty second line is printed by Wolfram before every message):

```text
{1372, 435}

RegisterFormat::interr: An internal error occurred: ImageMetadataTools could not be installed.
wrote C:\work\Dirac_claude\Revision\gkd_lovelock\results\notebook-in68-image.png: 28229 bytes (117 bytes of text/time chunks removed)
```

`{1372, 435}` is the width and height of the picture in pixels. "117 bytes of text/time chunks removed" is the
date and text that Wolfram's PNG writer added and the script removed. The `RegisterFormat::interr` line is
explained in part 5. On a computer where the Wolfram kernel can download that add-on, the line may be
missing; this was not tested.

Nothing is written to standard error. The numbers to check are `58`, `58`, `{1372, 435}` and `28229 bytes`.

### 4.2 Exit codes

All three commands end with exit code `0`. The image export ends with `2` only after printing
`ERROR: not a PNG`. A Python error inside the digest (for example a missing input file) gives `1`. If Python
cannot find the digest script itself (terminal not in the repository root), it exits with `2`.

The two `wolframscript` commands end with `0` even when something is wrong: when the notebook cannot be
found, and also when `wolframscript` cannot find the SCRIPT file itself (it then prints only
`Failed to open file at path: ...`). Both cases are in part 3.6. So always check the printed counts, not only
the exit code.

### 4.3 The output files, and how to check them

1. **Byte identity with the committed files.** `git status --porcelain` prints nothing. To see the folder
   `build/`, which git ignores, use `git status --porcelain --ignored`. It prints exactly one line,
   `!! build/`, if `build/` did not exist before.
2. **sha256 of the outputs.** These must equal part 2.3.
   * Windows PowerShell:
     `Get-FileHash -Algorithm SHA256 Revision/gkd_lovelock/results/notebook-input-cells.txt, Revision/gkd_lovelock/results/notebook-in68-image.png`
     (it prints the hashes in capital letters).
   * macOS: `shasum -a 256 Revision/gkd_lovelock/results/notebook-input-cells.txt Revision/gkd_lovelock/results/notebook-in68-image.png`.
   * Linux: `sha256sum Revision/gkd_lovelock/results/notebook-input-cells.txt Revision/gkd_lovelock/results/notebook-in68-image.png`.
3. **The full text has 58 cells.**
   * PowerShell: `(Select-String -Pattern '^=== ' -Path build/lovelock_nb_inputs.txt).Count`.
   * bash: `grep -c '^=== ' build/lovelock_nb_inputs.txt`.

   Both print `58`.
4. **The digest's content.** Open `Revision/gkd_lovelock/results/notebook-input-cells.txt` in any text
   editor. Its first 6 lines describe the file. Line 7 is empty. Lines 8 to 65 are the 58 cells, one per line.
   Two lines to look for:

   ```text
   In[87]:=             108  'HoldForm[Clear[kδ]; kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]]'
   In[101]:=        9918543  'HoldForm[Image[NumericArray[{{{255, 255, 255}, {255, 255, 255}, ...
   ```

   The first is the author's `kδ` definition, 108 characters long. The second is the picture cell: 9,918,543
   characters, almost all of the 9.9 MB file. Its line in the digest is cut at 160 characters.
5. **The picture.** Open `Revision/gkd_lovelock/results/notebook-in68-image.png` in any image viewer. It shows
   Lovelock's equation (4.38) as the author pasted it.
6. **Pixel check, for another Wolfram version.** This compares the picture itself, whatever the bytes of the
   file are. Run from the repository root:
   * bash, and PowerShell 7.3 or newer:

     ```text
     wolframscript -code 'Hash[ByteArray[Flatten[ImageData[Import["Revision/gkd_lovelock/results/notebook-in68-image.png"], "Byte"]]], "SHA256", "HexString"]'
     ```

   * Windows PowerShell 5.1, and PowerShell 7.0, 7.1 and 7.2 (they pass arguments to programs the old way,
     which strips the inner double quotes, so they must be written `\"`):

     ```text
     wolframscript -code 'Hash[ByteArray[Flatten[ImageData[Import[\"Revision/gkd_lovelock/results/notebook-in68-image.png\"], \"Byte\"]]], \"SHA256\", \"HexString\"]'
     ```

   Type `$PSVersionTable.PSVersion` to see which PowerShell you have. PowerShell 7.3 changed the way
   arguments with double quotes are passed to programs, which is why the version matters. Use the command for
   YOUR version; the other one fails:
   * the first command in PowerShell 5.1 or 7.0 to 7.2 prints `Import::chtype`, `ImageData::imginv`,
     `Hash::invhash: SHA256 is not a valid Hash specification.` and no hash;
   * the second command in PowerShell 7.3 or newer prints `ToExpression::sntx: Invalid syntax ...` and
     `$Failed`.

   The right command prints `4efe457deb90302eb2cc564798964305a07291bf194715dab8368cbf7c78a198`. It may come
   after the `RegisterFormat::interr` message, because reading a PNG triggers the same add-on lookup. Verified
   on Windows: the first command in PowerShell 7.6.6 and in Git Bash, the second in Windows PowerShell
   5.1.26100.9444 and in PowerShell 7.6.6 switched to the old way of passing arguments
   (`$PSNativeCommandArgumentPassing = 'Legacy'`, the behaviour of PowerShell 7.0 to 7.2).

### 4.4 Measured run time and memory (verification machine)

Machine: 24 logical cores (Intel Core Ultra 9 275HX), 191 GB RAM, Windows 11. Other verification jobs were
running at the same time, so the times vary from run to run.

On 2026-10-02:

| script | run 1 (fresh clone) | run 2 (same clone) | later runs | peak memory (working set) |
| --- | --- | --- | --- | --- |
| extraction | 3.49 s | 4.85 s | 1.85 s, 2.22 s | Wolfram kernel 168 MB; `wolframscript` 16.5 MB |
| digest | 0.37 s | 0.72 s | - | Python 60 MB |
| image export | 5.85 s | 6.56 s | 5.27 s, 6.18 s | Wolfram kernel 204 to 210 MB; `wolframscript` 16.5 MB |

On 2026-10-07 (about 18 Wolfram kernels of other jobs were running at the same time, the likely reason for the
longer times of the image export):

| script | run 8 (fresh clone) | run 9 (same clone) | run 10 (another fresh clone) | peak memory (working set) |
| --- | --- | --- | --- | --- |
| extraction | 3.74 s | 5.78 s | 5.07 s | Wolfram kernel 167.6 to 168.1 MB; `wolframscript` 16.5 MB |
| digest | 0.69 s | 0.70 s | 0.36 s | Python 63.7 MB |
| image export | 9.28 s | 11.26 s | 10.94 s | Wolfram kernel 210.2 to 210.4 MB; `wolframscript` 16.5 MB; licence query (part 5) 49.7 to 53.6 MB |

The times are wall-clock seconds from start to exit, including the start of the Wolfram kernel. In the
2026-10-07 table "MB" means 2^20 bytes. The memory of the Wolfram processes was sampled every 0.2 s (2026-10-02)
or 0.1 s (2026-10-07), over `wolframscript` and every process it started. The digest finishes too quickly for
sampling (the 0.1 s samples caught only 12 to 30 MB), so on 2026-10-07 its peak was read by the Python process
itself at its end: a small wrapper ran the digest (with `--out` to a scratch file) and then asked Windows
(`GetProcessMemoryInfo`, `PeakWorkingSetSize`). It gave 63.7 MB in each of three runs; the work inside Python
took 0.13 to 0.16 s, and the rest of the 0.4 to 0.7 s is the start of Python.

---

## 5. Side effects

What a run of the three commands of part 3.5 creates, overwrites or starts.

* **In the repository.**
  * The digest OVERWRITES `Revision/gkd_lovelock/results/notebook-input-cells.txt`.
  * The image export OVERWRITES `Revision/gkd_lovelock/results/notebook-in68-image.png`.
  * Both are committed files. With Wolfram 15.0.1 the new bytes are identical, so git reports no change.
  * The extraction creates the folder `build/` if it does not exist, and writes or OVERWRITES
    `build/lovelock_nb_inputs.txt` (about 9.9 MB). This folder is ignored by git.
  * Nothing else changes. After every verification run, `git status --porcelain --ignored` in the clone printed
    only `!! build/`. The notebook `Generalized _Kronecker_Delta_4+4.nb` is read, never written. Python writes
    no `__pycache__` folder, because the digest is run as a script and not imported.
* **Temporary files of WolframScript.** On Windows, each `wolframscript` command creates TWO files
  `tmp_<10 letters>` in the folder
  `C:\Users\<you>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary`:
  * an EMPTY file, within about 0.1 s of the start (observed 0.03 to 0.1 s);
  * a second file, created once the Wolfram kernel is running (observed 2.2 to 4.6 s after the start), which
    receives a COPY of everything the command prints. It grows line by line as the lines are printed, and its
    final content was byte-identical to the printed output (218 bytes for the extraction and 386 bytes for the
    export in the verification clone; the size depends on the length of your folder path, which appears in the
    printed lines). This happened both when the output went to a console window and when it was redirected to
    a file. During the image export, the list of open files (Sysinternals `handle`) showed this file held open
    by the Wolfram kernel process (`wolfram.exe`), not by `wolframscript`.

  Both files are deleted when the command ends (observed within 0.1 s of the exit). The digest (Python) creates
  no such file.
* **WolframScript's settings file.** On Windows, each `wolframscript` command rewrites
  `C:\Users\<you>\AppData\Roaming\Wolfram\WolframScript\WolframScript.conf` at its start (observed 28 to 68 ms
  after the process started). The content stays the same (238 bytes with the same sha256 before and after on
  the verification machine); only the file's modification time changes. So each of the two `.wls` commands of
  the set rewrites it once.
* **Lock files of the Wolfram kernel.** Every Wolfram kernel that starts (not only the kernels of this set)
  creates and deletes small lock files, such as `pacletSiteData_15.lock` and
  `pacletData_15.0.1.0_<number>.pmd3.lock`, in `C:\Users\<you>\AppData\Roaming\Wolfram\Paclets\Temporary`.
  They existed for 0.03 to 0.2 s each, about 0.6 to 1.1 s after a kernel started. Other Wolfram jobs ran on
  the verification machine at the same time, so these lock files could not be tied one by one to the kernels
  of this set; none of them stays behind.
* **Nothing else outside the repository.** A comparison of every file in
  `C:\Users\<you>\AppData\Roaming\Wolfram`, `C:\Users\<you>\AppData\Local\Wolfram`, `C:\ProgramData\Wolfram`
  and the top level of the system's temporary folder, before and after a run of the three commands, found no
  other change that could be attributed to this set (the remaining changes belonged to other Wolfram and
  Python jobs that were running at the same time). All the files above lie outside the repository.
* **The optional variant of part 3.5** ("WITHOUT touching the repository") changes nothing in the repository
  and writes, in your temporary folder, `lovelock_nb_inputs.txt` (9,923,611 bytes on Windows, the same bytes as
  `build/lovelock_nb_inputs.txt`) and `notebook-input-cells.txt` (6,153 bytes, the same bytes as the committed
  digest). They stay there until you delete them with the commands given in part 3.5.
* **Processes started.**
  * Each `wolframscript` command starts one Wolfram kernel for the whole run. With Wolfram 15 on Windows the
    kernel is the process `wolfram.exe`; on other versions and systems its name may differ, for example
    `WolframKernel`. `wolframscript` stops the kernel at the end.
  * Before the kernel, `wolframscript` also starts a second, short-lived process `wolfram.exe -wlbanner -licenseinfo`.
    That is WolframScript asking about the licence. It lives for about 0.1 to 0.5 s and uses about 50 MB of
    memory. On 2026-10-02 it was seen only sometimes, because the processes were sampled more slowly. On
    2026-10-07 it was seen for both commands whose child processes were listed every 0.05 s (one extraction,
    one image export), and in all three image-export runs sampled every 0.1 s; in the extraction runs sampled
    every 0.1 s it ended too quickly to be caught.
  * No parallel subkernels are started.
  * The digest runs one `python` process.
* **Network.**
  * The extraction and the digest use no network. The extraction contains no internet function.
    `wolframscript` and its kernel talk to each other over a shared-memory link (the kernel is started with
    `-linkmode Connect -linkname <5 letters>_shm -mathlink`, and both processes hold the shared-memory section
    of that name); `wolframscript` itself had no network socket at all. The only sockets seen were pairs of
    `127.0.0.1` connections INSIDE the kernel process (both ends owned by the kernel), each with an entry in
    state `Bound` for the same port. No connection to another computer was observed for the extraction.
  * The IMAGE EXPORT makes Wolfram 15.0.1 TRY to reach the internet. This is not something the script
    asks for. Wolfram's PNG writer starts by calling ``Image`Utilities`GetImageMetadataTools[]``, which looks
    for an optional add-on ("paclet") named `ImageMetadataTools`.
  * When that paclet is not installed, the PNG writer asks the Wolfram Cloud for a download link, with
    `CloudGet[CloudObject["https://www.wolframcloud.com/obj/services-admin/imagemetadatatoolsdownloadlink"]]`. A
    trace shows the HTTPS request
    `https://www.wolframcloud.com/files?path=services-admin%2Fimagemetadatatoolsdownloadlink&fields=owner%2Cuuid%2Cpath`.
    It would then install the paclet from that link with `PacletInstall`.
  * On the verification machine the Wolfram kernel could not open the connection
    (`URLRead::invhttp: Failed to connect to www.wolframcloud.com port 443`). So nothing was downloaded or
    installed. The writer printed the message
    `RegisterFormat::interr: An internal error occurred: ImageMetadataTools could not be installed.`
    and wrote the PNG without the add-on. Re-checked on 2026-10-07: the message appeared in every run,
    `PacletFind["ImageMetadataTools"]` returned `{}` (not installed) before and after a PNG export, and a direct
    `URLRead` of the address above from a Wolfram kernel on that machine returned `Failure["ConnectionFailure", ...]`.
    (A `Trace` of the export made on 2026-10-07 did not show the internal calls, so the call path described above
    rests on the trace of 2026-10-02.)
  * The same address did answer from that machine to another program (`curl`). So on a computer where the
    Wolfram kernel CAN reach the internet, the export may download that paclet and install it into your
    Wolfram user folder (`$UserBaseDirectory/Paclets`, on Windows under
    `C:\Users\<you>\AppData\Roaming\Wolfram`). The PNG might then contain different bytes. This was NOT
    tested. If it happens, use the pixel check of part 4.3.
  * Do NOT try to prevent the download by typing `$AllowInternet = False` into Wolfram unless you know how to
    undo it. In Wolfram 15 that assignment is SAVED as a preference and stays in force for every later Wolfram
    session. Undo it with `wolframscript -code '$AllowInternet = True'`. This happened during the verification,
    and the setting was restored (part 6).
* **To restore the committed state** (from the repository root):
  * `git checkout -- Revision/gkd_lovelock/results/notebook-input-cells.txt Revision/gkd_lovelock/results/notebook-in68-image.png`
  * To remove the full text:
    * PowerShell: `Remove-Item build/lovelock_nb_inputs.txt`
    * bash: `rm build/lovelock_nb_inputs.txt`
  * Then remove the folder `build` ONLY if it is now empty:
    * PowerShell: `if (-not (Get-ChildItem build)) { Remove-Item build }`
    * bash: `rmdir build`, which refuses to delete a folder that is not empty.

---

## 6. Verification record

* **Dates:** 2026-10-02 (first verification and its re-verification after an independent review, runs 1 to 7)
  and 2026-10-07 (verified again after a restart of the verification workflow, runs 8 to 10; see the bullet
  "Verification of 2026-10-07" below).
* **Commits verified:**
  * clone 1 at `45d47343ae480df46e06689ed822b8f9a88a8030` (2026-10-02);
  * clones 2, 3 and 4 at `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (2026-10-02);
  * clone 5 at `a4c5eda1df069a43a55ff8b57148f5de8edd1670` (2026-10-07);
  * clone 6 at `8cbd03a02f7771bce9e199f5d48cd41a979f1f06` (2026-10-07).

  Each was `main` of https://github.com/once-ere/Dirac_claude.git at the time of cloning. The three scripts,
  the notebook and both committed outputs are identical at all four commits (`git diff --stat 45d4734 c2b33cc`
  and `git diff --stat c2b33cc 8cbd03a` over these six paths are empty; between them only this provenance file
  was added, in commit `3f0a577`), and their digests are those of part 2. The three scripts and the PNG
  `notebook-in68-image.png` were last changed in commit `70fab64`, the digest `notebook-input-cells.txt` in
  commit `ad02ebb`, and the notebook `Generalized _Kronecker_Delta_4+4.nb` in commit `eb03ec8` (all on
  2026-10-01).
* **Environment:**
  * Windows 11 Pro for Workstations 10.0.26200 on 2026-10-02 and 10.0.26300 on 2026-10-07, 24 logical cores
    (Intel Core Ultra 9 275HX), 191 GB RAM;
  * WolframScript 1.14.0, Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), Professional licence
    (`$AllowInternet` was `True` at the start of the 2026-10-07 runs);
  * Python 3.14.5 (the digest also with 3.11.15, 3.12.13, 3.13.13 and, on 2026-10-07, 3.14.4);
  * git 2.51.2.windows.1; PowerShell 7.6.6 (some checks also in Windows PowerShell 5.1.26100.9444 and in Git
    Bash, GNU bash 5.2.37).
* **Fresh clones:** two clones made with `git clone https://github.com/once-ere/Dirac_claude.git` into an empty
  scratch folder. No uncommitted file was copied into them: the working tree had no uncommitted change to any
  script of this set, to the notebook or to the two committed outputs.
* **Runs** (each the commands of part 3.5, from the clone root, in the order extraction, digest, image export):

  | run | clone | exit codes | stderr | printed counts | `notebook-input-cells.txt` | `notebook-in68-image.png` | `build/lovelock_nb_inputs.txt` |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | 1 | 1 (fresh, no `build/`) | 0, 0, 0 | empty | 58; 58; {1372, 435}, 28229 bytes | identical to committed | identical to committed | `52f611d4...276a6` |
  | 2 | 1 again | 0, 0, 0 | empty | 58; 58; {1372, 435}, 28229 bytes | identical to committed and to run 1 | identical to committed and to run 1 | identical to run 1 |
  | 3 | 2 (fresh) | 0, 0, 0 | empty | 58; 58; {1372, 435}, 28229 bytes | identical to committed | identical to committed | identical to run 1 |

  The standard output of the image export was identical in all runs, apart from the clone folder in the paths.
  Run 3 also watched the file system and the network connections (part 5).
* **Further checks** (all in the fresh clones or in scratch folders):
  * The extraction with `LOVELOCK_NB_INPUTS` set, followed by the digest with `--out`, both writing to a scratch
    folder, gave a full text identical to run 1 and a digest identical to the committed one.
  * The digest, run with Python 3.11.15, 3.12.13 and 3.13.13, was byte-identical to the committed file.
  * The digest made from an LF-only copy of the full text was byte-identical to the committed file.
  * The extraction, run from Windows PowerShell 5.1, gave the identical full text.
  * The pixel digest `4efe457d...8a198` was computed both by Wolfram (the command of part 4.3) and by an
    independent Python decoder of the PNG, and the two agreed.
  * Running both `.wls` scripts from a wrong folder, and the digest with a missing input, gave the messages of
    part 3.6.
* **Re-verification after an independent review** (2026-10-02, about 07:00 to 07:12 local time). An
  independent verifier reported eight inaccuracies in this file (none in the scripts). Each was re-checked in
  two NEW fresh clones of `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, into which no file was copied:
  * Four more runs of the three commands of part 3.5 (run 4 in clone 3, fresh; run 5 in clone 3 again; run 6
    in clone 4, fresh, with the output going to a console window; run 7 in clone 4 again). All exit codes `0`,
    standard error empty, the printed counts as in part 4.1, `git status --porcelain --ignored` printed only
    `!! build/`, and the two committed outputs and `build/lovelock_nb_inputs.txt` (`52f611d4...276a6`) were
    byte-identical to the committed files and to runs 1 to 3. Times (extraction, digest, export), measured
    while file, process, network and handle watchers were running: run 4 4.22 s, 0.21 s, 9.75 s; run 5
    4.66 s, 0.16 s, 8.72 s; run 6 3.86 s, 0.19 s, 6.93 s; run 7 3.75 s, 0.16 s, 7.27 s.
  * The temporary files, the rewrite of `WolframScript.conf`, the lock files in `Paclets\Temporary`, the
    shared-memory link and the sockets described in part 5 were observed in runs 5 to 7 and in one more run of
    the two `.wls` commands in clone 4 (folders polled every 5 to 10 ms; open files listed with Sysinternals
    `handle`; sockets listed with `Get-NetTCPConnection` and `Get-NetUDPEndpoint` every 50 ms).
  * The messages and exit codes of the new first row of the table in part 3.6 were reproduced in PowerShell
    7.6.6 from an empty folder and from the subfolder `Revision`.
  * The two pixel-check commands of part 4.3 were run in PowerShell 7.6.6 in both argument modes, in Windows
    PowerShell 5.1.26100.9444 and in Git Bash (GNU bash 5.2.37); each printed `4efe457d...8a198` where part 4.3
    says it should, and the errors quoted there where it should not.
  * The optional variant of part 3.5 was run literally in PowerShell 7.6.6 (with `TEMP` pointed to a scratch
    folder): it printed the digest hash `1A889643...1418CE`, left the clone unchanged, and the two files it left
    were removed by the cleanup command given there.
  * The Wolfram Engine download links of part 3.2 were followed on 2026-10-02 (redirects only, nothing
    downloaded); the last commits of the six files were read with `git log -1` in the fresh clone.
* **Verification of 2026-10-07** (after the verification workflow was interrupted by a session limit and
  restarted; this file, written on 2026-10-02, was not trusted but checked again). Two NEW fresh clones were
  made with `git clone https://github.com/once-ere/Dirac_claude.git` into an empty scratch folder (clone 5 at
  `a4c5eda`, clone 6 at `8cbd03a`). No file was copied into them: `git status --porcelain` in the working
  repository showed no uncommitted change to any file of the set, to the notebook or to the two outputs. Each
  command was started from the clone root exactly as in part 3.5, with its standard output and standard error
  captured to separate files, its wall time measured and its processes sampled every 0.1 s.

  | run | clone | exit codes | stderr | printed counts | time (extraction, digest, export) | `notebook-input-cells.txt` | `notebook-in68-image.png` | `build/lovelock_nb_inputs.txt` |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 8 | 5 (fresh, no `build/`) | 0, 0, 0 | empty | 58; 58; {1372, 435}, 28229 bytes, 117 removed | 3.74 s, 0.69 s, 9.28 s | identical to committed | identical to committed | `52f611d4...276a6`, 9,923,611 bytes |
  | 9 | 5 again | 0, 0, 0 | empty | the same | 5.78 s, 0.70 s, 11.26 s | identical to committed and to run 8 | identical to committed and to run 8 | identical to run 8 |
  | 10 | 6 (fresh) | 0, 0, 0 | empty | the same | 5.07 s, 0.36 s, 10.94 s | identical to committed | identical to committed | identical to run 8 |

  * The printed output of every command (218, 235 and 386 bytes) was byte-identical in runs 8 and 9, and in
    run 10 apart from the clone folder name in the paths. After each run `git status --porcelain --ignored` in
    the clone printed only `!! build/`, so no committed file changed, no `__pycache__` appeared, and the
    notebook kept its sha256 `23bb4e0c...b80afb`.
  * The PNG was decoded independently in Python: chunks `IHDR pHYs IDAT IDAT IDAT IDAT IEND` with valid CRCs,
    1372 x 435 pixels, 8-bit RGB; the decompressed stream `8bb2905c...cb1c98` and the pixel bytes
    `4efe457d...8a198` of part 2.3. The pixel check of part 4.3 printed `4efe457d...8a198` in PowerShell 7.6.6
    (first command) and in Windows PowerShell 5.1.26100.9444 (second command).
  * The full text has 174 lines and 174 CR LF line ends; its LF-only version has 9,923,437 bytes and the sha256
    `f4aa92fd...2f0317e` of part 2.3, and the digest made from it equals the committed digest. The digest run with
    Python 3.11.15, 3.12.13, 3.13.13 and 3.14.4 also equals the committed digest.
  * The optional variant of part 3.5 was run literally in PowerShell 7.6.6 (with `TEMP` pointed to a scratch
    folder): it printed `1A889643...1418CE`, wrote the full text `52f611d4...276a6`, left the clone unchanged,
    and its cleanup command removed both files.
  * From the subfolder `Revision`, the three commands of part 3.5 gave `Failed to open file at path: ...` (exit
    `0`), Python's `can't open file ... [Errno 2]` (exit `2`) and again `Failed to open file at path: ...` (exit
    `0`). Called by their full paths from an empty folder, the extraction printed `Get::noopen` and
    `input cells written: 0` and left an empty `build/lovelock_nb_inputs.txt` in that folder, and the export
    printed the messages listed in part 3.6 and `wrote ...: 1371 bytes`, both with exit code `0`. The digest
    with a missing input ended with `FileNotFoundError` and exit code `1`. These are the rows of part 3.6.
  * Part 5 was checked again where the other jobs running on the machine allowed it. Every `wolframscript`
    command started the licence query `wolfram.exe -wlbanner -licenseinfo` and then one kernel, with the command
    line of part 5 (`-linkmode Connect -linkname <5 letters>_shm -mathlink`). WolframScript's temporary folder,
    polled every 5 ms, showed for the extraction an empty `tmp_...` file from 0.05 s until the exit (5.41 s) and a
    second one from 4.42 s, 218 bytes at the end (the printed output), deleted at the exit; and for the export
    the same pair (0.06 s and 4.62 s, 386 bytes, both deleted at the exit at 11.31 s). Other `tmp_...` files in
    that folder belonged to the other jobs (about 18 `wolframscript` commands of other jobs were running).
    `WolframScript.conf` kept its content (238 bytes, same sha256) but got a new modification time; with the
    other jobs running, that rewrite could not be tied to the commands of this set. Not repeated on 2026-10-07:
    the lock files, the open-handle and socket listings and the comparison of the Wolfram folders.
  * Network: see part 5 (re-checked: no paclet installed, the kernel could not connect).
  * The download links of part 3.2 were checked again with `HEAD` requests (nothing downloaded).
  * Peak memory: part 4.4.
* **Check counts:** the set has no internal pass/fail checks. Expected and found in every run (runs 1 to 10):
  58 input cells written, 58 digest rows, an image of 1372 x 435 pixels, a PNG of 28229 bytes with 117 bytes of
  chunks removed, and 2 of 2 committed outputs byte-identical (and the uncommitted full text byte-identical).
* **Fixes made:** none to the set, on 2026-10-02 or on 2026-10-07. The set executed correctly as committed,
  and no script, input or output of the set was changed. On 2026-10-07 this provenance file was brought up to
  date: the summary at the top, part 1.2 (the textbook notebook `01c_generalized_delta`, which reads the digest),
  part 3.2 (links checked again; the free Engine download is 15.0.0), part 3.3 (Python 3.14.4), part 3.6 (the
  complete list of messages of the image export started from a wrong folder), part 4.4 (times and memory of
  2026-10-07), part 5 (the licence query process; the re-check of the network behaviour) and part 6. On
  2026-10-02 it had been corrected after the review: part 3.2 (download, free
  licence and install steps of the Wolfram Engine 15.0), part 3.5 (cleanup of the optional variant), part 3.6
  (new row for a terminal that is not in the repository root; the `Get::noopen` rows now say when they occur),
  part 4.2 (exit codes when a script file is not found), part 4.3 (PowerShell 7.3 or newer for the first
  pixel-check command; 5.1 and 7.0 to 7.2 for the second), part 5 (two temporary files per command, the
  rewrite of `WolframScript.conf`, the kernel's lock files, the files of the optional variant, the
  shared-memory link and the sockets inside the kernel) and part 6 (the last commit of each file).
* **A setting changed during the verification and restored.** To test the image export without internet,
  `$AllowInternet = False` was assigned in two Wolfram sessions, at about 06:14 local time (UTC-7). Wolfram 15 saved
  this as a preference, so later Wolfram sessions on the verification machine saw `$AllowInternet = False`.
  It was noticed at 06:20 and restored with `wolframscript -code '$AllowInternet = True'`; a new session then
  showed `True`, the value seen at 06:01 before the test. The verification runs 1 to 3 were made before the
  change. A repeat of the image export after the restore gave the identical PNG. The PNG made with
  `$AllowInternet = False` was also identical, because the kernel could not connect in either case.
* **Open discrepancies:** none. Notes for other installations:
  * Byte identity of the PNG and of the digest was verified on Wolfram 15.0.1 on Windows only. Another
    Wolfram version, including the free Wolfram Engine 15.0.0 offered for download on 2026-10-07 (part 3.2),
    may compress the PNG or format InputForm text differently; use the pixel check of part 4.3.
  * The two `.wls` scripts find the notebook through the CURRENT folder and end with exit code `0` even when
    it is not found (part 3.6). That is not a defect when they are run as their usage says (from the repository
    root), so they were left unchanged; check the printed counts.
  * The behaviour of the image export on a computer whose Wolfram kernel can reach the internet (download of
    the `ImageMetadataTools` paclet, part 5) was not tested.
  * The macOS and Linux commands are the same command lines as on Windows (with `python3`). Only Windows was
    available for this verification.
