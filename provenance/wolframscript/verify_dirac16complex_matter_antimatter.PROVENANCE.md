# Provenance of the Wolfram set `verify_dirac16complex_matter_antimatter`

This file documents one **wolframscript set**: the Wolfram Language program
`scripts/verify_dirac16complex_matter_antimatter.wls` and the package it loads,
`wolfram/Dirac16ComplexMatterAntimatter.wl`. It says what the set computes, which files it
reads and writes, how a student who has never used Wolfram runs it, what it prints, what it
changes on the disk, and how it was verified on 2026-10-02. Every instruction needed to run
the set is in this file.

**Result of the verification (2026-10-02, commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`,
Windows 11, Wolfram 15.0.1, WolframScript 1.14.0).** The set **executes correctly**: run
from fresh clones, twice as its usage says (once started from PowerShell, once from Git
Bash) and in seven further variants, it printed `check_count=44` and
`failed_check_count=0`, exited with code 0 and wrote a report and a theory file that are
**byte-identical** to the committed files (and therefore identical between the runs). Wall
time 6.9 to 8.5 minutes per run on a shared 24-core machine; peak working set of the Wolfram
kernel 2.4 GiB (about 3 GB of private memory). One environment limitation was found and is
not fixed in the code (Section 6.4): on Windows the folder of the clone must have a path of
at most 155 characters, in PowerShell and in Git Bash alike; with a longer path the run
fails at its end (exit code 1 or 2, Section 3.7, item 3).

## 1. What the set is and what it computes

### 1.1 In plain words

The repository studies a field theory called **dirac16complex**: a field $\Psi$ with 16
components on an 8-dimensional space with 4 space-like and 4 time-like directions
(signature (4,4)). The question behind this set is: *can this theory explain why the
observed universe contains matter but almost no antimatter?* The set answers it with exact
computer algebra: whole numbers, fractions, complex numbers with rational parts and exact
symbols; no rounded number decides any check, with one labelled exception named below. It
treats both kinds of field components that the repository uses: **anticommuting**
(Grassmann) components, the theory called dirac16complex, and **commuting** (ordinary
complex) components, the theory called dirac16complex00.

The program runs 44 **checks**. A check is one exact test whose result is `true` or
`false`. They follow the theorems M1 to M5 of the repository's matter-antimatter analysis:

- **Algebra (2 checks, names beginning with `MA_algebra_`).** The 16 by 16 gamma matrices,
  the matrix $C$, the chirality matrix $\gamma^8$, the 28 generators $S^{ab}$ and the charge
  matrix $B$ are rebuilt from their definitions and compared entry by entry with the
  committed exact fixture.
- **M1, the charge is conserved (15 checks, `MA_M1_`).** The Lagrangian (the function from
  which the field equations follow) does not change when $\Psi$ is multiplied by a constant
  phase $e^{i\alpha}$, for every self-interaction $U$ and in every gravitational field. The
  program verifies this at three exact points of a general curved test geometry, derives
  the conserved current $j^\mu=\bar\Psi\gamma^\mu\Psi$ (Noether's theorem), verifies the
  exact identity that makes it conserved, confirms conservation on exact solutions of the
  field equations, and confirms that every recorded Kohn-Sham run of the repository (56
  reference runs with 168 levels and 33 Rust runs) has the imposed particle number to a
  relative accuracy of $10^{-9}$. This last check, `MA_M1_ksFixedNetNumberRecorded`, is
  the only one that reads floating-point data.
- **M2, discrete symmetries C, P, T and their combinations (12 checks, `MA_M2_`).** It
  classifies exactly every map built from a constant 16 by 16 matrix $M$ and a reflection of
  a set $R$ of the eight directions. For each of the 256 sets $R$ exactly two matrices $M$
  (up to a factor) turn the Dirac operator into plus or minus itself, which gives 512 pairs
  $(M,R)$; each is taken as a linear map and as a map with complex conjugation, so 1024 maps
  for each kind of component. It finds which of them leave the Lagrangian unchanged, and
  which of these reverse the charge.
- **M3, charge-violating terms the symmetry would allow (9 checks, `MA_M3_`).** It
  classifies the "Majorana-type" terms $\Psi^TM\Psi$ and $\Psi^TM\gamma^a\partial_a\Psi$
  that the space-time symmetries Spin(4,4) and Pin(4,4) allow, decides which of them survive
  for each kind of component, and shows that each carries charge 2 (one further quartic term
  carries charge 4). None of these terms is part of the theory.
- **M4, the pair (5 checks, `MA_M4_`).** The chirality matrix $\gamma^8$ reverses the
  current, maps solutions with mass $m$ and coupling $\lambda$ to solutions with $-m$ and
  $-\lambda$, and the pair $(\Psi,\gamma^8\Psi)$ has total charge 0 and total classical
  energy-momentum 0.
- **M5, a labelled hypothesis (1 check, `MA_M5_implication`).** If three stated assumptions
  H1 to H3 hold, the total charge of a pair of universes vanishes. The implication is
  checked; the assumptions are not derived.

The program writes two files: a **report** (the 44 checks, 43 measurements and the sha256
of the programs and inputs) and a **theory file** (the exact results in a form other
programs can read; the independent Python checker of the repository compares its own
results with it).

### 1.2 Charge conjugation in this set is a matrix

Every gamma matrix of this theory is **real** (a signed permutation matrix). For a real
field, plain complex conjugation $\Psi\to\Psi^\ast$ changes nothing, so it cannot by itself
be the charge conjugation. This set does not assume a charge conjugation; it **solves** for
it as a matrix:

- **Form $\Psi\to M\Psi^\ast$.** The program solves exactly (256 unknowns, linear equations
  over the rational numbers) for every constant 16 by 16 matrix $M$ with
  $\gamma^aM=\eta\,M\,(\gamma^a)^\ast$ for $a=0,\dots,7$. It finds exactly two
  one-dimensional solution spaces: $M=I_{16}$ for $\eta=+1$ (the mass is kept) and
  $M=\gamma^8=\gamma^0\gamma^1\cdots\gamma^7$ for $\eta=-1$ (the mass is reversed). Check
  `MA_M2_conjugationIntertwiners`, measurement `M2_conjugationIntertwiners`.
- **Form $\Psi\to M\bar\Psi^T$.** It solves $\gamma^aM=\zeta\,M\,(\gamma^a)^T$ and finds
  $M=C$ for $\zeta=-1$ and $M=\gamma^8C$ for $\zeta=+1$, where
  $C=\gamma^0\gamma^1\gamma^2\gamma^3$ (real, symmetric, $C^2=1$) and
  $\bar\Psi=\Psi^\dagger C$. Because $\bar\Psi^T=C\Psi^\ast$, these are the same two maps:
  $C\bar\Psi^T=\Psi^\ast$ and $\gamma^8C\bar\Psi^T=\gamma^8\Psi^\ast$. Check
  `MA_M2_transposeIntertwiners`, measurement `M2_transposeIntertwiners`.
- The labels "C: Psi -> conj(Psi) (= C Psibar^T)" and "C8: Psi -> gamma^8 conj(Psi)
  (= gamma^8 C Psibar^T)" in the theory file (key `M2.namedMaps`), and the names $C_0$ and
  $C_8$ in the documents that cite this set, are short names for these **matrix** maps:
  $C_0$ is the charge-conjugation matrix $C$ acting on $\bar\Psi^T$ (equivalently
  $M=I_{16}$ acting on $\Psi^\ast$), and $C_8$ is the matrix $\gamma^8C$ acting on
  $\bar\Psi^T$ (equivalently $M=\gamma^8$ acting on $\Psi^\ast$).
- For the **quantised** anticommuting field the program checks which of the two preserves
  the canonical anticommutator $\{\Psi,\Psi^\dagger\}=B$, with $B=-iC\gamma^4$: the
  condition $MB^TM^\dagger=B$ holds for $M=\gamma^8$ and fails, giving $-B$, for
  $M=I_{16}$. Check `MA_M2_canonicalStructure`, measurement `M2_canonicalStructure`.
- This agrees with the independent lead check
  `Revision/lead_checks/charge_conjugation_and_u1.py`, whose committed report
  `Revision/lead_checks/reports/charge-conjugation-and-u1.json` has 12 of 12 checks PASS.
  That program names the directions $x_1,\dots,x_8$. On 2026-10-02 the two fixtures
  (`artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` here,
  `Revision/algebra/gammas.json` there) were compared entry by entry: the Revision matrix
  $\gamma^{(x_8)}$ equals this set's $\gamma^0$, and $\gamma^{(x_k)}$ equals $\gamma^k$ for
  $k=1,\dots,7$. Hence the Revision's
  $\Gamma=\gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)}$ is exactly this set's
  $\gamma^8$, and the two matrices $C$ are the same matrix. The lead check finds the same
  two solution spaces ($I$ and $\Gamma$), the same two charge-conjugation matrices
  ($\mathcal C_+=C$ and $\mathcal C_-=\Gamma C$, acting as $\Psi^c=\mathcal C\bar\Psi^T$),
  and the same canonical result ($M=\Gamma$ preserves $B$; $M=I$ turns it into $-B$).
- **Real fields.** This set treats complex commuting fields and anticommuting fields; it
  does not treat real fields. For a real field the map with $M=I_{16}$ is the identity and
  carries no charge. The lead check shows that for real fields the matter-antimatter map is
  the real matrix $\Gamma$ (this set's $\gamma^8$) together with $m\to-m$ and
  $\lambda\to-\lambda$. That is the map this set uses in M4: $\Psi\to\gamma^8\Psi$ with
  $(m,\lambda)\to(-m,-\lambda)$.

### 1.3 What the set does not establish

The program establishes M1 to M4 and the implication of M5 exactly as stated in its
report. It does **not** establish that the theory solves the matter-antimatter problem:
the exact phase symmetry of M1 conserves the charge inside one universe, and M2 finds exact
symmetries that reverse the charge. The theory file says so in its key `honestyRule`. The
quantum (Fock-level) pairing statements that it quotes from the Stage-5 pairing report are
marked PROVISIONAL in the measurement `M4_kreinLevelStatus`.

### 1.4 Documents that cite its results

- `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md` (with its `.tex` and `.pdf`): sections 4
  to 9 (the theorems), 11 (verification records: the 44 check names and the sha256 of both
  outputs) and 12 (reproduction commands).
- The textbook `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (with `.tex` and `.pdf`), assembled
  from `provenance/textbook/chapters/`: Chapter 17 (matter and antimatter; Section 17.17
  gives rerun commands), Chapter 19 (Section 19.10, a rerun table), Chapter 20 (check
  index), and mentions in Chapters 0, 6, 7, 15, 16 and 18. Chapter 6 cites the `MA_M2_*`
  checks in its check table and names the report folder
  `artifacts/dirac16complex/matter-antimatter/` (the check it names as an example,
  `MA_M2_cpScopeInCurvedFields`, belongs to the independent Python checker, not to this
  set); Chapter 7 cites this set's checks `MA_M1_noetherIdentity_commuting_G1` and
  `MA_M1_noetherIdentity_grassmann_G1`.
- `handoff/specs/MATTER_ANTIMATTER_SPEC.md`, the specification (its section 3 lists the
  deliverables).
- `scripts/check_dirac16complex_matter_antimatter.py`, the independent Python checker,
  compares its own results with `matter-antimatter-theory.json` (check
  `MA_agreesWithWolfram`); its committed report
  `artifacts/dirac16complex/matter-antimatter/python-matter-antimatter-report.json` records
  the sha256 of that theory file.
- `tests/test_d16c_matter_antimatter_publication.py` pins the check counts, numbers and
  sha256 values of both outputs that the matter-antimatter document quotes.
- `HANDOFF.md` (status of the analysis).

## 2. The files

### 2.1 The programs

| File | sha256 | Lines | Bytes |
| --- | --- | --- | --- |
| `scripts/verify_dirac16complex_matter_antimatter.wls` | `5d85f7d8a76a78b0f8853d41af0d2a352b426c553d5eba4569ade2fd5d9fc73f` | 116 | 6262 |
| `wolfram/Dirac16ComplexMatterAntimatter.wl` | `382c34694f91bf2ed68cee42736dd9298171e2abf61d0b388d6228e4d47ef4c5` | 1293 | 105177 |
| `wolfram/Dirac16ComplexGeometry.wl` | `f5b674665eee4000750161e6ab6312c38bfac9da7a17450a2b3bdd88ef292af2` | 997 | 71636 |

- `scripts/verify_dirac16complex_matter_antimatter.wls` is the program you run (the
  verifier). It reads its arguments, loads the package, runs the checks, writes the two
  output files, prints the verdict lines and sets the exit code.
- `wolfram/Dirac16ComplexMatterAntimatter.wl` is the package that contains every check.
  Its entry point is `D16MARun`; `D16MAExpectedCheckCount` is 44.
- `wolfram/Dirac16ComplexGeometry.wl` is the Stage-1 geometry package. The package above
  loads it and uses it read-only (exact curved-space geometry, field equations,
  energy-momentum tensor, and reproducible exact "random" rationals from a fixed 64-bit
  generator, so every run uses the same numbers).

All three files have LF line endings, and the repository's `.gitattributes` (`* -text`)
stops Git from converting them, so a clone on any system gets exactly these bytes.

### 2.2 The inputs it reads

| File | sha256 | Lines | Bytes |
| --- | --- | --- | --- |
| `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` | `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b` | 18440 | 213133 |
| `artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json` | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | 350 | 42018 |
| `artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json` | `d43adeeba580bdd8cec56fac5fa74906b7578c06c8589e52dbe3da1404cd49e7` | 2638 | 49440 |
| `artifacts/dirac16complex/arbitrary-field/grassmann-demo-report.json` | `b83997857ccfc9fb71f05efbcaebe16f29bf36687cc08c16e0823a26a6369f09` | 111 | 4443 |
| `artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json` | `5b150b36e13b903c32b86e8debbaeda48798e0beb0bc6a216e416d2671f4e01a` | 4537 | 72176 |
| `artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json` | `735534de950c7fb0327370c33caa275cf805aa91a41dee903e4eaec7a6fa0de8` | 184 | 8141 |
| `artifacts/dirac16complex/pair-creation/pairing-theory.json` | `5a267bd696391b131134577ccdcf7766b83f96f3eb32b9b8de60c9175b1ebf6a` | 851 | 57027 |

What each input is used for:

- `algebra-fixture.json`: the exact matrices compared by `MA_algebra_fixtureMatches`.
- The three Stage-1 reports `wolfram-geometry-report.json`, `wolfram-algebra-report.json`
  and `grassmann-demo-report.json`: ten, five and one of their checks are cited by
  `MA_M1_stage1ChecksCited`, together with their sha256 (measurement
  `M1_stage1ChecksCited`).
- `kohn-sham-theory.json`: its functional definition must contain the particle-number
  constraint (`MA_M1_ksFixedNetNumberRecorded`).
- The two Stage-5 files `wolfram-pairing-report.json` and `pairing-theory.json`: their
  checks `PAIR_T1krein_*` and their key `T1krein` are quoted as PROVISIONAL (measurements
  `M4_kreinLevelStatus`, `M4_kreinLevelConsistency`, `M5_implication`).

Besides its command-line arguments the program reads one **environment variable**,
`DIRAC16_MATTER_ANTIMATTER_REPORT`: when the program is started without an argument and
this variable is set to a non-empty text, the report is written to the path it names
instead of the default path (Section 3.5). Nothing in the repository sets this variable.

The report and the theory file record, under `sourceSha256`, the sha256 of the three
programs of Section 2.1, of the fixture and of the two Stage-5 files; both also record the
sha256 of the three Stage-1 reports (report: measurement `M1_stage1ChecksCited`; theory
file: key `M1.stage1Checks`). If any of these files changes, the outputs change. The
Kohn-Sham files of Section 2.3 enter the report only through the counts and deviations of
the measurement `M1_ksFixedNetNumber`.

### 2.3 The Kohn-Sham run files it reads

`MA_M1_ksFixedNetNumberRecorded` lists every file named `run.json` one or two folder levels
below `artifacts/dirac16complex/kohn-sham/reference/` (56 files) and
`artifacts/dirac16complex/kohn-sham/rust/scf/` (33 files) and reads each of them. At the
verified commit these are (sha256, then the path below the folder named in the heading
line):

```
artifacts/dirac16complex/kohn-sham/reference/ (56 files)
6140e867f633fbebf6fb09322455df7f6bdd1daa15dad7c6fb1ac603616f1557 L2-free-N8-p+1/run.json
260d73c5a42066367f3d9ae67ff48f56c7b1f4cce328c168ac4ac2b0a7a3a192 L2-free-N8-p-1/run.json
e6c1257149e20264a38b8a4d74f763fc589484ce4c7bce7c7e65185686517610 L3-free-N8-p+1/run.json
2af6fed8036ac12335027b49ac84d45c0cbbd3ac836a33cdfaff9e7774d9b452 L3-free-N8-p-1/run.json
8853806683959b4392465a02995c489303dbb46983ca14632b5bd5a9da938e26 L4-free-N8-p+1/run.json
a6727da8e3c21e07c736c5621bcd0b051404009a69c074ec56712e1ff1304d0f L4-free-N8-p-1/run.json
1361f1233e3ba96c85b58a0d54ac14abf177caf483833cd1226228a035b337d7 m1_L2_N112_lam0_T0/run.json
ae71578e2dd5054ccdaedb13d58f9c83b6f636d10f2aed527390ba57dad8e968 m1_L2_N112_lamp1_T0/run.json
7a8b1d2b42440eb6e65bdf7cc348ebe79242a93f5137ab834594f2b84902a155 m1_L2_N8_lam0_T0/run.json
3aba0292b7e4c67fa6a41b168810d6e383a78bb45987de0bce0813907e72f511 m1_L2_N8_lamp1_T0/run.json
812b88f7d68aad9c3447f8315cf34bf4340afa380316f6ebc261541d349631ff m1_L3_N1016_lam0_T0/run.json
93fd3a9bfe03f29f721e5052963dc2ca984fedaf7dff9bf1f221a5e3d759b790 m1_L3_N1016_lamm1_T0/run.json
98d74954f567e3a3299d13c82a1a89e125bbde0dd58b5aa430657fbbfd5cbe0c m1_L3_N1016_lamm2_T0/run.json
edaa4e2c68b0eb13b909b38686d9e7e65c04e125801557c902414aadae2b13fc m1_L3_N1016_lamp1_T0/run.json
2a79f202efa8b5ebb6d1858d5c7742c245c1725f82441a2e0a4e5202a7b29e3f m1_L3_N1016_lamp2_T0/run.json
b172b4319629f9c726cc55f6e5e0108811904203ec71bd66357ceff56b3a7e74 m1_L3_N112_lam0_T0/run.json
b79797d9a6f7dec19e8368a5ee329c45aaed71835ecde04f5670490ecec9e43f m1_L3_N112_lam0_T0p1/run.json
f544ef26d50132fb41fd1a3635940df8476acb4b6f4e906a5ce5677a30600f2f m1_L3_N112_lam0_T0p3/run.json
5a316bff8a439e324411b10f9edbd0d6e044f16ff67b02fbbd52810cb44372ce m1_L3_N112_lam0_T1/run.json
0594c48399967e1a2de7604041f33b75162e43a37b30e331422496f1fc104400 m1_L3_N112_lamh_T0/run.json
732c2cb51b02ba3081c6e15848d1abf6dcbd0f92ae762912534c38f4df501b57 m1_L3_N112_lamh_T0p1/run.json
67654da548c88c370fb508b0cac42f1a8abf9b04c18ba7e21231121c6ffc773b m1_L3_N112_lamh_T0p3/run.json
39b9902cc50761e3727a1530ebbfb945cc47563322fc32893c64002c0a713a7f m1_L3_N112_lamh_T1/run.json
77c3d9d2fa1f05db5e96951611050b5b5854bfbd7d2628a59379e365f7e5b8ca m1_L3_N112_lamm1_T0/run.json
965a117c8c904fb95e5ac7f066a1b4bf39ba847e4d9a0bf350a6d1b3c2c03d16 m1_L3_N112_lamm2_T0/run.json
d0840c979c9fb3671dc70c93e91ef8986db9c5bc20d0d62e45e3d46cea2bfcd4 m1_L3_N112_lamp1_T0/run.json
ec642fa1a8fdb7dd675e34b269b28732d33e64d23dcf3c39976a07e0f6bc3549 m1_L3_N112_lamp1_T0_a40p5/run.json
40c05314e4d766c4796e6b34fede93d5ec0625b6c91db739c300d9a7670939cd m1_L3_N112_lamp1_T0p1/run.json
c997b4e9f92c31eda070cd2ee8274ab3f5ba7e00f2e81b29dc17d80589d6734f m1_L3_N112_lamp1_T0p3/run.json
c0e6bfc4a8fe5f081b02272a1dfd089add4f4b48d4ccbea932fab3984d0d6b37 m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836/run.json
0ac94ada9e0a43045e6326bd971fad22276213007ef6db148e4f99689e088163 m1_L3_N112_lamp2_T0/run.json
06742924897db1967eeaf83bae9d8459b4deb1635d0aac3bf03c575c58e94169 m1_L3_N896_lamp1_T0_dk0p125/run.json
5c9ad935ca2f5192555d2f72fea9a1aff4bd49d3b492da60f823902c48b58b80 m1_L3_N8_lam0_T0/run.json
5015725561461db7b86801853031943192a8f65c2bfa16a9223af5fb8cdacf03 m1_L3_N8_lam0_T0p1/run.json
10152e291b7f1f3849bcb9ebe0398d8b7d62cac93111194f90ef00e689b46b21 m1_L3_N8_lam0_T0p3/run.json
0a99f04c4ec672ab2f40b93718710975c1fbfa2b2352f7022831e40d6311b660 m1_L3_N8_lam0_T1/run.json
af36ca61146f6c8ef1a82b78dd7ad33f9d0a0cd48146a808845b64b5ddee09d1 m1_L3_N8_lamh_T0/run.json
bda36c713f97a8c26b7184358cf544d1c3f211a1c7668d115b9c1fe6a3e73008 m1_L3_N8_lamh_T0p1/run.json
169a9dbc5cadc794c22c1cafa75152d5f5340d5729cd30b2d9281a46c0e01542 m1_L3_N8_lamh_T0p3/run.json
aa94a82d5d6e13bf261f0d4646d39ca3478df953bdc10de0964f2871b13ef9c7 m1_L3_N8_lamh_T1/run.json
7534524654799f24d04cc1eb7d3c059152572e2e1602235e2b469ba186f1b28e m1_L3_N8_lamm1_T0/run.json
b391b5089f2c356eca80e6ccfe9b5767ed40d4b71b750d97c0059eb24bfacb43 m1_L3_N8_lamm2_T0/run.json
2fa3490bb0ec1e65632fd40aa8581dab15c5de4da7a6fe9e593f23ddc8ab202b m1_L3_N8_lamp1_T0/run.json
916522ce2868c6f1ba092e4c2c623398d36e949cfc534718ea54449e4be84ab4 m1_L3_N8_lamp1_T0p1/run.json
9720fdf513e15dc118e96049bbc3fc54b29d9cb3bf41e41e4a0215b45bd4bcad m1_L3_N8_lamp1_T0p3/run.json
45fd0179d40e54dd345e2680d5cb4deebe853ff1dcb019e3be3d8741673d5d3c m1_L3_N8_lamp2_T0/run.json
43097e33f65e5d61d71f0d778dfa59ced1dd772f94638bb0bea3a6133daee999 m1_L4_N112_lam0_T0/run.json
ed32ef20908a1fc69dd69e75b3d9c8680473d3bae016e6d0940873101b32e151 m1_L4_N112_lamp1_T0/run.json
bf4fa1105d2899b6325f790889c78f37738514e12b9f6dfdddd7ab529d905c29 m1_L4_N8_lam0_T0/run.json
8824ef079c01682c5f756376170cfb9ebac24adf650ded07c79a013ffa9f9b2e m1_L4_N8_lamp1_T0/run.json
bf0b05b1a8adb155210f32369d642d5b2348d1aeed0551cb5f73707cc81655cb m3_L3_N112_lam0_T0/run.json
16d2550c7ad7a6ccdd6e399697497ba63b71f27c4f2e9da09fdd6317c83023c6 m3_L3_N112_lamm1_T0/run.json
5ff4e02e39617ab0a9ffae202ce7d34bdf8f6fcc853685f8d53022d114217eb2 m3_L3_N112_lamp1_T0/run.json
353a6e36fdfc7bb8c14acfb57a773f9c0650082b35dbdbe72a34edcb9a39204b m3_L3_N8_lam0_T0/run.json
e26746a38b32a3b21e9e8dc5467e8efec8408f66cf99703f13501000643f15e0 m3_L3_N8_lamm1_T0/run.json
51944005b2829cabd2600ed742ee65a4634349d6c8d31cce5eb0ceff49ae2517 m3_L3_N8_lamp1_T0/run.json
artifacts/dirac16complex/kohn-sham/rust/scf/ (33 files)
6ddf4dc0678baf8851d40b5b67e4d15422b2d668be3f796ada26e0f98d3e9cd8 m1_L2_N112_lam0_T0/run.json
b32675500262d3414131358b7107e90057edd815ff51d38865dd70693a341406 m1_L2_N112_lamp1_T0/run.json
47106eb0c541615dbc9247f83821bb2753eb87c0b5afc94f7868390cf7d7f085 m1_L2_N8_lam0_T0/run.json
eba140042b8a696731e979aa4fb1cc7428834b25caa0dc5b5db134434aca40a3 m1_L2_N8_lamp1_T0/run.json
f9f72c7ef62c0bbf50c7bb29bbdee1c60f90cb3bc19e04f5ee90170d0a7f5784 m1_L3_N1016_lam0_T0/run.json
2a8858b2394ce3267b988e65f86336fddbdd14b0bd09d02f2d45e3819189372c m1_L3_N1016_lamm1_T0/run.json
85b549ceb7f3af7052118318ab2191407739c3ada8b9b0deffa1ac25ecf23484 m1_L3_N1016_lamm2_T0/run.json
abcaba3c63b72d417f2a4a254ce0d0cd85fda0cb78feeef9db12e6a1ab74ab78 m1_L3_N1016_lamp1_T0/run.json
1eded3454990a8420a71f726285bc1649050a65ec89b5450de43d5ef9a487762 m1_L3_N1016_lamp2_T0/run.json
14d2d3b9155f8c78fd1208d516f7b64fb931b6daca8b2f741721fcb34cdfaf74 m1_L3_N112_lam0_T0/run.json
931d827437b98f5fc74e3e06927aa760ddbfd224fc320d062839717907eeb2e0 m1_L3_N112_lamm1_T0/run.json
a97644cc9257546811aa8af6243b208804371bb5d8a58bdf632766eb4f86df8b m1_L3_N112_lamm2_T0/run.json
68a5940873aec1f956c4b5d0acd632f43ffb10f7e9d83140762f46cb12e514f2 m1_L3_N112_lamp1_T0/run.json
0c65b9378a6e492d97a54c9618bf8198f44b6dcb1b93799f3f3b90544940138a m1_L3_N112_lamp1_T0_a40p5/run.json
f30b4c6f8b372bf79cabd007a30bf2e403a4ef720cd1376d8b1e081a4a77ab1e m1_L3_N112_lamp1_T0_g601/run.json
cd60e7f0daf1a372c3291ea3a71905361bd0186268c2e77d2e6765afb4e1b258 m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836/run.json
2acbd071a51a144319ac9d579bd9cf2cd6a2ea5780ff8f86a868a046bbf24860 m1_L3_N112_lamp2_T0/run.json
d515db63c97bb42cb942f7d833b2394cbdf6a922ed81742a3c633e139aeeb27f m1_L3_N896_lamp1_T0_dk0p125/run.json
9e15994b199bf134b14be57201f2649af8247cf7ec4f66b60932ba879bc95bdf m1_L3_N8_lam0_T0/run.json
45b8f1ff1da30a79f3c6e01c4c63b090145436bd79641c3bc4e07b5c50424aca m1_L3_N8_lamm1_T0/run.json
102cb1f892e62885d8eb806317fa49559a98f2c4ffae46c5f4afce6a5965c037 m1_L3_N8_lamm2_T0/run.json
64624e2efa7b46f11ce37237e8b438faeb6c0d78820276b258a601ee887daac0 m1_L3_N8_lamp1_T0/run.json
7b2155d8e8a9e9eb3551819072b1bb4fe1fcf4efb8463cb01a1b6e514536fcb4 m1_L3_N8_lamp2_T0/run.json
20959886834add90e6a7d9ceff072a18e0c481ca4cec2ec747395430f5ed088d m1_L4_N112_lam0_T0/run.json
7ef948eb6502008ddae257a67354d0089458f542842524373397bc1acbfeb820 m1_L4_N112_lamp1_T0/run.json
a51f9b18524c49a60baa2906cf909bc4e026fe5e81be39985b34a6ba4a9837b3 m1_L4_N8_lam0_T0/run.json
809da901e122fb19fa6277e9666b613318a19d16b3b47c90b69cdbd1607578c1 m1_L4_N8_lamp1_T0/run.json
73d54200a670dd506f7b6778847dd68da299ced0aa0045fca5088778043baac5 m3_L3_N112_lam0_T0/run.json
c238b3958b80e935cfc8ae9e945915cb6986b1a8ecb5588ac2308005c372d65d m3_L3_N112_lamm1_T0/run.json
a79f1fecb3abe6ec852576a4615f27c6e1d2955446db08521a51e64a3eede6ff m3_L3_N112_lamp1_T0/run.json
329315695d965367200c9aaff95b53f0f7ed3bb8b84fa32d50db491af3060273 m3_L3_N8_lam0_T0/run.json
4bfa8490ba02312fd8602d135be6064221a431c17bec970931aaa111b81d2bd2 m3_L3_N8_lamm1_T0/run.json
b2428e72d57f351b49c3e15d03ecb949c2bcef4a034a2655c7a4a18ea1549fc7 m3_L3_N8_lamp1_T0/run.json
```

The two longest paths are
`artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836/run.json`
(103 characters) and the file of the same folder name under `rust/scf/` (102 characters).
They decide the path-length limit on Windows (Sections 3.3 and 6.4).

### 2.4 The outputs it writes

| Output (default path) | sha256 of the committed file | Lines | Bytes |
| --- | --- | --- | --- |
| `artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json` | `ad6b91296034a24c14b2ee08c7bfe8da98aaff2db83544897767e498adeaa269` | 2184 | 48687 |
| `artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json` | `1505a3962938477e5db42f568c0a1afcd21898c4409793178f8311b792638f10` | 52935 | 773184 |

Both are JSON written as UTF-8 with LF line endings and a final newline. The report has
the keys `schemaVersion` (1), `producer`, `checks` (44 entries), `measurements` (43
entries) and `sourceSha256` (6 entries). The theory file has the keys `schemaVersion`,
`producer`, `title`, `honestyRule`, `conventions`, `M1`, `M2`, `M3`, `M4`, `M5`,
`sakharovInputs` and `sourceSha256`. The paths in the table are the defaults; positional
arguments or the environment variable `DIRAC16_MATTER_ANTIMATTER_REPORT` change them
(Section 3.5). Nothing else is written by the program (no log file, no temporary file);
WolframScript itself creates two temporary files outside the repository while the program
runs, one of them a copy of the printed output, and deletes them at the end (Section 5.2).

## 3. How to run it

### 3.1 What you need

- A computer with Windows 10 or 11, macOS or Linux, with at least 3 GB of free
  memory and 1 GB of free disk space (a clone of the repository takes about 520 MB).
- A **Wolfram Language kernel** with the command-line program **WolframScript**: either
  the free **Wolfram Engine for Developers** or **Mathematica**. The verification of
  Section 6 used Wolfram 15.0.1 with WolframScript 1.14.0.
- **Git**, to download (clone) the repository.
- No Python and no internet connection are needed for the run itself (an internet
  connection is needed once, to download and activate Wolfram and to clone the
  repository).

A **terminal** is the window in which you type commands: on Windows open
**PowerShell** (Start menu, type `PowerShell`, press Enter); on macOS open **Terminal**
(Applications, Utilities); on Linux open your terminal program. Type each command below
exactly as shown and press Enter after each line.

### 3.2 Install Wolfram and activate WolframScript

**Option A, the free Wolfram Engine for Developers.**

1. In a web browser open `https://www.wolfram.com/engine/`, choose your operating system
   and download the installer. The page asks you to sign in with a **Wolfram ID** or to
   create one (free; an e-mail address and a password).
2. Run the installer and accept the proposed settings.
3. Open a **new** terminal (an old one does not know the new program yet) and type

   ```
   wolframscript -version
   ```

   It prints a line like `WolframScript 1.14.0 for Microsoft Windows (64-bit)`. If the
   terminal answers that `wolframscript` is not recognised or not found, WolframScript is
   not installed or not on the search path: download and install WolframScript on its own
   from `https://www.wolfram.com/wolframscript/` and open a new terminal again.
4. Activate the engine once (internet needed):

   ```
   wolframscript -activate
   ```

   Enter your Wolfram ID and password when asked. Type them yourself; never put a password
   into a script or a file.
5. Test the kernel:

   ```
   wolframscript -code '$Version'
   ```

   It prints the Wolfram version, for example
   `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. The single quotes are needed in
   both PowerShell and bash, so that the shell does not treat `$Version` as one of its own
   variables.

**Option B, Mathematica.** Install and activate Mathematica as its installer explains.
Mathematica normally installs WolframScript as well. If `wolframscript -version` is not
found in a new terminal, install WolframScript from
`https://www.wolfram.com/wolframscript/`. Then test with `wolframscript -code '$Version'`
as in step 5.

The byte-for-byte reproduction of Section 4 is verified for Wolfram 15.0.1 only. The
report records the version in its `producer` line (`Wolfram Language 15.0.1`), so another
version writes at least that one line differently.

### 3.3 Install Git and download the repository

Install Git: on Windows from `https://git-scm.com/download/win` (accept the proposed
settings); on macOS type `xcode-select --install` in Terminal (or install Git from
`https://git-scm.com/download/mac`); on Debian or Ubuntu Linux type
`sudo apt install git`. Check with `git --version`.

**Windows (PowerShell).** Clone into a folder with a **short path**, for example
`C:\src`:

```
mkdir C:\src
cd C:\src
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
(Get-Location).Path.Length
```

(If `C:\src` already exists, `mkdir` reports an error; ignore it.) The last command prints
the number of characters of the path of the repository folder, here `19`. **It must not be
larger than 155.** The reason: the program lists two Kohn-Sham run files whose path inside
the repository has 103 and 102 characters, and the Wolfram 15.0.1 kernel on Windows cannot
see a file whose full path is longer than 259 characters (Section 3.7, item 3).

**Windows (Git Bash).** The same limit of 155 characters applies when you work in Git Bash
on Windows, because it comes from the Wolfram kernel on Windows, not from the shell. Clone
into a short folder in the same way (`mkdir -p /c/src`, `cd /c/src`, then the `git clone`
and `cd Dirac_claude` lines above) and check the length in the repository root with

```
pwd -W | tr -d "\n" | wc -c
```

which prints the same number as `(Get-Location).Path.Length` in PowerShell (`pwd -W` prints
the Windows form of the path, for example `C:/src/Dirac_claude`, 19 characters).

**macOS and Linux (Terminal).** On macOS and Linux the path length does not matter:

```
cd ~
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The clone took 15 seconds on the verification machine. The folder `Dirac_claude` is the
**repository root**; every command below is typed there.

Optionally confirm that the programs are the verified ones. In PowerShell:

```
Get-FileHash scripts/verify_dirac16complex_matter_antimatter.wls, wolfram/Dirac16ComplexMatterAntimatter.wl, wolfram/Dirac16ComplexGeometry.wl
```

On macOS use `shasum -a 256` and on Linux `sha256sum`, followed by the three file names
separated by spaces. The hashes must equal those of Section 2.1 (PowerShell prints them in
capital letters; that is the same number).

### 3.4 Run it: Windows PowerShell

In the repository root type the command on **one** line:

```
wolframscript -file scripts/verify_dirac16complex_matter_antimatter.wls artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json
```

and after it has finished

```
$LASTEXITCODE
```

which prints the **exit code** of the program (`0` means every check passed).

### 3.5 Run it: macOS and Linux (bash or zsh), and Git Bash on Windows

In the repository root:

```
wolframscript -file scripts/verify_dirac16complex_matter_antimatter.wls artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json
echo $?
```

The second line prints the exit code. In Git Bash on Windows the repository path must have
at most 155 characters, exactly as in PowerShell (check it with
`pwd -W | tr -d "\n" | wc -c`, Section 3.3).

Rules for the command line:

- The report path is a plain **positional argument**. Do not write `--` before it:
  WolframScript 1.14 drops `--` and every argument after it when it is combined with
  `-file`.
- Without any argument the program uses the same default report path,
  `artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json`
  (verified, Section 6, run 3), **unless** the environment variable
  `DIRAC16_MATTER_ANTIMATTER_REPORT` is set to a non-empty text. Then the report is
  written to the path in that variable (a relative path is taken relative to the folder
  you are in) and the theory file next to it (verified, run 8). A positional argument
  always takes precedence over the variable (verified, run 9). Nothing in the repository
  sets the variable, so normally it is not set. To check, type
  `$env:DIRAC16_MATTER_ANTIMATTER_REPORT` in PowerShell (prints nothing when it is not
  set) or `echo "$DIRAC16_MATTER_ANTIMATTER_REPORT"` in bash or zsh (prints an empty line
  when it is not set). To remove it from the current terminal, type
  `Remove-Item Env:DIRAC16_MATTER_ANTIMATTER_REPORT` in PowerShell or
  `unset DIRAC16_MATTER_ANTIMATTER_REPORT` in bash or zsh.
- The theory file is written next to the report, under the name
  `matter-antimatter-theory.json`, unless a second positional argument gives its path.
- A relative path is taken relative to the folder you are in, so run the command from the
  repository root. (The program finds its own package from the location of the script, so
  only the output paths depend on the current folder.)

### 3.6 Run it without touching the committed files

To write the two outputs into the folder `build/ma/` (Git ignores the folder `build/`),
give both paths:

```
wolframscript -file scripts/verify_dirac16complex_matter_antimatter.wls build/ma/wolfram-report.json build/ma/theory.json
```

The folder `build/ma/` is created if it does not exist, and so is the folder `build/`
itself (a fresh clone has no folder `build/`). The two files are byte-identical to the
committed ones (verified, Section 6). Compare them in PowerShell with

```
(Get-FileHash build/ma/wolfram-report.json).Hash -eq (Get-FileHash artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json).Hash
(Get-FileHash build/ma/theory.json).Hash -eq (Get-FileHash artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json).Hash
```

(each line prints `True`), and on macOS and Linux with

```
cmp build/ma/wolfram-report.json artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json && echo IDENTICAL
cmp build/ma/theory.json artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json && echo IDENTICAL
```

(each line prints `IDENTICAL`).

### 3.7 If it fails

The likely problems, what you see, and what to do:

1. **`wolframscript` is not found.** PowerShell says that the term `wolframscript` is not
   recognized; bash or zsh says `command not found`. WolframScript is not installed or the
   terminal was opened before the installation. Install it (Section 3.2) and open a new
   terminal. On Windows the program is normally
   `C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe`.
2. **Wolfram is not activated.** WolframScript prints a message about activation or a
   licence instead of running the program. Run `wolframscript -activate` (Section 3.2,
   step 4) and try again.
3. **The path of the clone is too long (Windows only).** The program reads two Kohn-Sham
   run files with very long names (Section 2.3). The Wolfram 15.0.1 kernel on Windows
   cannot open a file whose full path is longer than 259 characters, even when long paths
   are enabled in Windows (they were enabled on the verification machine, and Git had
   checked the files out). This holds in PowerShell and in Git Bash alike. What you see
   depends on the length $L$ of the path of the repository folder, which
   `(Get-Location).Path.Length` prints in the repository root in PowerShell, and
   `pwd -W | tr -d "\n" | wc -c` in Git Bash:
   - $L\le155$: no problem (verified with $L=153$ and $L=155$).
   - $L=163$ (verified): shortly after the line `MA_M1_chargeDensityMatrix = True` two
     messages appear,
     `General::dirdep: Cannot get deeper in directory tree: ...\m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836.`,
     one for `kohn-sham\reference` and one for `kohn-sham\rust\scf`. The run continues and
     every progress line shows `True`, but after the full run time the program prints
     `ERROR: D16MARun failed or produced messages` and exits with code 2. It writes no
     file, so the committed outputs stay unchanged.
   - $L=159$ (verified): no message appears, but the kernel cannot read the two long files.
     The program ends with `check_count=44`, `failed_check_count=1` and
     `failed_checks=MA_M1_ksFixedNetNumberRecorded` and exits with code 1. It **has
     overwritten** the committed report: `git status` lists
     `artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json` as
     modified, with two changed lines (`"MA_M1_ksFixedNetNumberRecorded":false` and
     `"referenceLevelsChecked":165` instead of `true` and `168`); the theory file is
     unchanged. Restore the report with the command of Section 5.4.
   - Lengths from 156 to 162 were not tried; expect one of the two failures above.

   The fix: delete the clone and clone again into a short folder such as `C:\src`
   (Section 3.3), then check that `(Get-Location).Path.Length` (PowerShell) or
   `pwd -W | tr -d "\n" | wc -c` (Git Bash) prints at most 155. The program itself is not
   changed for this (Section 6.4 explains why).
4. **`ERROR: missing package ...`**, exit code 2. The script looks for its package in the
   folder `wolfram/` next to the folder `scripts/` that contains it. Run the script where it
   is, inside a complete clone; do not copy it elsewhere.
5. **`ERROR: package load produced messages: ...`**, exit code 2. A package file is
   changed or damaged, or the Wolfram version is too old for it. Compare the sha256 of the
   three programs with Section 2.1 (Section 3.3 shows how) and restore them with
   `git checkout -- scripts/verify_dirac16complex_matter_antimatter.wls wolfram/Dirac16ComplexMatterAntimatter.wl wolfram/Dirac16ComplexGeometry.wl`.
6. **`ERROR: D16MARun failed or produced messages`**, exit code 2, for another reason than
   item 3. Every Wolfram message during the run (a line such as `General::...` or
   `Import::...` printed above) makes the program stop without writing its outputs. The
   usual cause is a missing or changed input file of Sections 2.2 and 2.3: `git status`
   lists it. Restore the inputs with `git checkout -- artifacts/` and run again.
7. **A line `failed_checks=<names>` and exit code 1.** At least one check is `false`. In
   this case the program **has written** its report and theory file, and the report
   records the false check. Do not edit anything. Check that the clone is unchanged
   (`git status` may list only the two output files), that the path is short enough
   (item 3) and that the Wolfram version is 15.0.1 (`wolframscript -code '$Version'`).
   Restore the committed outputs with the command of Section 5.4 and report the names of
   the failed checks.
8. **All 44 checks are true, but `git status` lists the report or the theory file as
   modified.** The bytes differ from the committed file. `git diff` shows the changed
   lines. A different Wolfram version changes at least the `producer` line of the report,
   which ends with the version number; a changed program or input changes `sourceSha256`
   (compare with Section 2). Restore with the command of Section 5.4.
9. **The program seems to hang.** The steps `M2: all maps at the Lagrangian level (flat)`
   and `M2: named maps and the curved field G1` print nothing for about 2 and 3 minutes
   on the verification machine. Wait; the whole run takes about 8 minutes there
   (Section 4.4). If you stop it with Ctrl+C before the end, no output file is written;
   the Wolfram kernel ends as well, and WolframScript's two temporary files stay behind
   (Section 5.2 says where they are; you may delete them).
10. **Not enough memory.** The Wolfram kernel needs about 3 GB (Section 4.4). Close other
    programs and run again.
11. **The output went somewhere else.** A relative output path is taken relative to the
    folder you are in, and arguments written after `--` are dropped (then the default path
    is used). Without an argument the report goes to the path in the environment variable
    `DIRAC16_MATTER_ANTIMATTER_REPORT` when that variable is set and not empty
    (Section 3.5 shows how to check and remove it). The two lines `report=` and `theory=`
    at the end of the output name the files that were actually written.

## 4. The expected output

### 4.1 What is printed

Everything is printed on standard output; nothing is printed on standard error. A
successful run prints 149 lines (about 43 KB) in four blocks.

**Block 1, progress (58 lines).** Fourteen progress lines of the form `[HH:MM:SS] <step>`
(the clock time of your computer), each followed by one line `  <check> = True` for every
check of that step. The fourteen steps, in order:

```
algebra and fixture
M1: U(1) invariance
M1: Noether current and identity
M1: on-shell conservation
M1: charge
M2: intertwiners
M2: classification
M2: all maps at the Lagrangian level (flat)
M2: named maps and the curved field G1
M2: summary and canonical structure
M3: invariant forms
M3: extra quartic
M4
M5
```

**Block 2, the 44 verdict lines**, exactly these, in this order:

```
check_MA_algebra_fixtureMatches=true
check_MA_algebra_basicFacts=true
check_MA_M1_u1InvarianceCommutingGenericU_flat=true
check_MA_M1_u1InvarianceCommutingGenericU_G1=true
check_MA_M1_u1InvarianceGrassmann_G1=true
check_MA_M1_grassmannPotentialsPolynomialAndNeutral=true
check_MA_M1_noetherCurrentLocalPhase_commuting_G1=true
check_MA_M1_noetherCurrentLocalPhase_grassmann_G1=true
check_MA_M1_noetherCurrentFormula_grassmann_G1=true
check_MA_M1_noetherCurrentFormula_commuting_G1=true
check_MA_M1_noetherIdentity_grassmann_G1=true
check_MA_M1_noetherIdentity_commuting_G1=true
check_MA_M1_negativeControlNotebookConnection=true
check_MA_M1_onShellConservation_G1=true
check_MA_M1_chargeDensityMatrix=true
check_MA_M1_ksFixedNetNumberRecorded=true
check_MA_M1_stage1ChecksCited=true
check_MA_M2_conjugationIntertwiners=true
check_MA_M2_transposeIntertwiners=true
check_MA_M2_signPatternClassification=true
check_MA_M2_statisticsSign=true
check_MA_M2_matrixClassification=true
check_MA_M2_lagrangianFlatCommuting_all=true
check_MA_M2_lagrangianFlatGrassmann_all=true
check_MA_M2_namedTransformations=true
check_MA_M2_frameLevelG1_commuting=true
check_MA_M2_frameLevelG1_grassmann=true
check_MA_M2_symmetrySummaryAndChargeReversal=true
check_MA_M2_canonicalStructure=true
check_MA_M3_spinInvariantForms=true
check_MA_M3_pinCharacterForms=true
check_MA_M3_kineticInvariantForms=true
check_MA_M3_grassmannSurvival=true
check_MA_M3_commutingSurvival=true
check_MA_M3_u1Charge=true
check_MA_M3_pinCharactersMajoranaTerms=true
check_MA_M3_notebookLgIsMajoranaType=true
check_MA_M3_extraGrassmannQuarticCharge4=true
check_MA_M4_currentFlipMatrix=true
check_MA_M4_currentFlipG1_grassmann=true
check_MA_M4_pairEMTAndCurrentG1_commuting=true
check_MA_M4_pairEMTG1_grassmann=true
check_MA_M4_kreinOneParticle=true
check_MA_M5_implication=true
```

**Block 3, 43 measurement lines** `measurement_<name>=<value>`, one per measurement of the
report, with the value written in Wolfram notation (for example
`measurement_M1_localPhaseCommutingG1={True, True, True}`). Some of these lines are
several thousand characters long (the longest has 11569 characters). They contain no
clock times and are the same in every run.

**Block 4, the final four lines**, exactly:

```
check_count=44
failed_check_count=0
report=artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json
theory=artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json
```

With the command of Section 3.6 the last two lines are `report=build/ma/wolfram-report.json`
and `theory=build/ma/theory.json`. If a check fails, a fifth line
`failed_checks=<names separated by commas>` follows.

### 4.2 The exit code

`0` when all 44 checks are true and there are exactly 44 of them; `1` when a check is
false or the number of checks is not 44; `2` when the package cannot be loaded, when the
run produced a Wolfram message, or when the JSON text could not be produced. In PowerShell
`$LASTEXITCODE` and in bash or zsh `echo $?`, typed right after the run, print it. All
verified runs of Section 6 ended with `0` (except the deliberately long paths of
Section 6.4).

### 4.3 The files written and how to check them

The run rewrites the two files of Section 2.4. When everything is right they are
byte-identical to the committed files, so Git sees no change:

```
git status --porcelain
```

prints **nothing** (in every shell). To see the fingerprints, in PowerShell

```
Get-FileHash artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json, artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json
```

and on macOS `shasum -a 256` (on Linux `sha256sum`) followed by the same two paths
separated by a space. The values must be those of Section 2.4:
`ad6b91296034a24c14b2ee08c7bfe8da98aaff2db83544897767e498adeaa269` for the report and
`1505a3962938477e5db42f568c0a1afcd21898c4409793178f8311b792638f10` for the theory file
(PowerShell prints capital letters).

To count the true checks in the report, in PowerShell:

```
$r = Get-Content artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json -Raw | ConvertFrom-Json
$c = @($r.checks.PSObject.Properties)
"$(@($c | Where-Object { $_.Value -eq $true }).Count) of $($c.Count) checks true"
```

which prints `44 of 44 checks true`; on macOS and Linux:

```
wolframscript -code 'c = Import["artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json", "RawJSON"]["checks"]; {Count[Values[c], True], Length[c]}'
```

which prints `{44, 44}`. The report's line `"producer":...` ends with
`Wolfram Language 15.0.1`, and its key `sourceSha256` lists the six sha256 values of the
three programs (Section 2.1), the fixture and the two Stage-5 files (Section 2.2).

### 4.4 Run time and memory

On the verification machine (24 logical processors, Windows 11, 191 GB of memory, shared
with other programs: about 20 Wolfram kernels of other verification jobs ran at the same
time) one run took between 412.8 s and 508.1 s (6.9 to 8.5 minutes): 491.9 to 508.1 s
for runs 1 to 5 of Section 6.2, which ran at the same time as each other, 412.8 s for
run 6, and 416.6 to 422.9 s for runs 7 to 9, which again ran at the same time as each
other. The longest steps were `M2: named maps and the curved field G1` (about 3 minutes),
`M2: all maps at the Lagrangian level (flat)` (about 2 minutes) and
`M1: Noether current and identity` (about 1.5 minutes). The Wolfram kernel
process (`wolfram.exe`) reached a peak working set of 2.43 to 2.45 GiB (2.6 GB) and peak
private memory of 2.74 to 2.77 GiB (3.0 GB); `wolframscript` itself used 17 MB. The
kernel used about one processor core (its CPU time, read during run 6, was 0.96 of the
elapsed time), so more processors do not make one run faster.

## 5. Side effects

### 5.1 Files in the repository

- **Overwritten:** the run of Sections 3.4 and 3.5 rewrites the two committed files
  `artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json` and
  `artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json`. When
  everything is right the new bytes are the committed bytes (only the modification time of
  the files changes), so `git status --porcelain` prints nothing. If a check fails
  (exit code 1) the files are still rewritten, then with different content.
- **Created:** with the command of Section 3.6 the folder `build/` (when it does not
  exist; a fresh clone has none, because Git ignores the folder and does not store it), the
  folder `build/ma/` (when it does not exist) and the two files
  `build/ma/wolfram-report.json` and `build/ma/theory.json`. The program creates the folder
  of each output file, with any missing parent folders, whenever it does not exist. Git
  ignores `build/` (the line `/build/` of the file `.gitignore`), so
  `git status --porcelain` prints nothing, `git status --porcelain --ignored` prints the
  single line `!! build/` (Git shows an ignored folder as one line), and
  `git status --porcelain --ignored --untracked-files=all` lists the two files:
  `!! build/ma/theory.json` and `!! build/ma/wolfram-report.json`.
- **Nothing else** in the repository is created or changed: after every successful run
  of Section 6.2 `git status --porcelain --untracked-files=all` printed nothing, and
  `git status --porcelain --ignored --untracked-files=all` listed only the output files
  under `build/` named above (runs 7 to 9 and D3 of Section 6.2).
- When the run stops with exit code 2 (Sections 3.7 and 6.4), nothing is written.

### 5.2 Programs started, temporary files, network

- **Processes.** `wolframscript` starts exactly one Wolfram kernel process (on Windows
  `wolfram.exe` of Wolfram 15.0.1); the program starts no further (parallel) kernels. The
  kernel ends when the program ends. While it runs it uses about one processor core and
  about 2.5 GiB of memory (Section 4.4). If `wolframscript` is stopped with Ctrl+C or
  killed, the kernel ends with it (observed with a short test program; no kernel was left
  running).
- **Temporary files.** The program writes no temporary file of its own. WolframScript
  itself creates two **files** (not folders) directly in the folder
  `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` (on Windows, for example
  `C:\Users\<your user name>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary`),
  each named `tmp_` followed by 10 random letters and digits:
  - the first is created when `wolframscript` starts (within 0.1 s) and stays empty
    (0 bytes);
  - the second is created about 2.5 to 3 seconds later, when the Wolfram kernel has started,
    and receives a copy of everything the program prints while it runs, with Windows line
    endings: for this set first the progress lines, and at the end the verdict and
    measurement lines. At the end of a successful run it holds all 149 printed lines,
    43048 bytes for the command of Section 3.6 in PowerShell, byte for byte the printed
    output (it was compared with the output redirected to a file).

  WolframScript deletes both files when the run ends, also when the program ends with
  exit code 1 or 2 (observed: the files of runs 7 to 9 and D3 of Section 6.2 disappeared
  within 0.3 s of the end of the run; those of a short test program ending with exit code
  2 were gone 0.5 s after its end). When `wolframscript` is stopped with Ctrl+C or killed, the two files **stay**
  (observed with a short test program); they are harmless and may be deleted. Other
  `tmp_...` files in that folder belong to other WolframScript runs.
  Wolfram's own bookkeeping files in the Wolfram user folder (on Windows under
  `%APPDATA%\Wolfram`, for example `Paclets\Configuration\managerData_15.0.1.0.pmd2`) may be
  updated by any kernel start; such updates were seen during the verification, while other
  Wolfram programs also ran, so they cannot be attributed to this program, and they do not
  influence its output. The corresponding folders on macOS and Linux were not examined.
- **Network.** The program contains no network access. During runs 1 to 5, D1 and D2 of
  Section 6.2 the process tree was examined every 1.5 seconds: no connection to any other
  computer was seen; in one run the kernel held a connection from `127.0.0.1` to
  `127.0.0.1`, which stays inside the same computer. (The internet is needed once, before,
  to activate Wolfram.)

### 5.3 Effect on other files of the repository

The independent Python checker records the sha256 of the theory file it compared with
(`inputSha256` of `python-matter-antimatter-report.json`), and
`tests/test_d16c_matter_antimatter_publication.py` and the matter-antimatter document quote
the sha256 of both outputs. A run that reproduces the committed bytes leaves all of these
valid. A run that writes different bytes (another Wolfram version, a changed input, a
failed check) makes them disagree until the committed outputs are restored.

### 5.4 Restoring the committed state

From the repository root, in every shell:

```
git checkout -- artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json
```

and, if you used Section 3.6, delete the scratch folder: in PowerShell
`Remove-Item -Recurse -Force build/ma`, on macOS, Linux and in Git Bash `rm -r build/ma`.
If the folder `build/` did not exist before your run (a fresh clone has none), this leaves
an empty folder `build/`. It is harmless (Git does not show an empty folder), or delete it
as well: in PowerShell `Remove-Item -Recurse -Force build`, on macOS, Linux and in Git Bash
`rm -r build`. Delete `build/` itself only if it held nothing of yours before the run.
Afterwards `git status --porcelain --ignored --untracked-files=all` prints nothing in a
clone that was fresh before the run (verified in the clones of runs 7 and D3).

## 6. Verification record

### 6.1 Date, commit and environment

- **Date:** 2026-10-02.
- **Commit verified:** `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (branch `main` of
  `https://github.com/once-ere/Dirac_claude.git`, committed 2026-10-02 06:00:22 -07:00).
  The five files of the set were last changed by these commits (`git log -1 -- <file>`):
  `scripts/verify_dirac16complex_matter_antimatter.wls` by `eac67e6` (2026-09-30
  10:58:51 -07:00), `wolfram/Dirac16ComplexMatterAntimatter.wl` by `de0ee8b` (2026-09-30
  11:30:46 -07:00), `wolfram/Dirac16ComplexGeometry.wl` by `6c0bfad` (2026-09-25
  11:46:19 -07:00), and both committed outputs by `33c07a3` (2026-09-30 11:56:38 -07:00).
  Their sha256 at the verified commit are those of Sections 2.1 and 2.4. No uncommitted
  file was needed or copied: every clone was used exactly as cloned.
- **Machine:** Windows 11 Pro for Workstations 10.0.26200 (build 26200), 24 logical
  processors, 191 GB of memory; Windows long paths enabled (registry value
  `LongPathsEnabled` = 1); Git 2.51.2.windows.1 with `core.longpaths` = true. The machine
  was shared: about 20 Wolfram kernels of other verification jobs ran at the same time.
- **Wolfram:** `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`, licence type
  Professional, WolframScript 1.14.0, kernel
  `C:\Program Files\Wolfram Research\Wolfram\15.0.1\wolfram.exe`.
- **Shells:** PowerShell 7.6.6, Windows PowerShell 5.1.26100.9444 (used for the check
  commands of Sections 3.3 and 4.3), Git Bash with GNU bash 5.2.37.
- **Python** 3.14.5 was used only to list sha256 values and to run the unit test named in
  Section 6.3; the set itself does not use Python.

### 6.2 The runs

Every run used its own fresh clone under the scratch folder of the verification job; the
column "root" gives the number of characters of the path of the clone. "Same" means
byte-identical to the committed file of Section 2.4.

| Run | How it was started (from the repository root) | Root | Exit | Wall time | Checks | Report | Theory |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PowerShell 7.6.6 (`Start-Process` with exactly the arguments of Section 3.4) | 155 | 0 | 504.2 s | 44 of 44 true | same | same |
| 2 | Git Bash: `bash -c "..."` with the command of Section 3.5 | 153 | 0 | 505.8 s | 44 of 44 true | same | same |
| 3 | PowerShell 7.6.6, no argument: `wolframscript -file scripts/verify_dirac16complex_matter_antimatter.wls` | 153 | 0 | 505.0 s | 44 of 44 true | same | same |
| 4 | Git Bash, one argument `build/execprov/wolfram-matter-antimatter-report.json` (theory file written next to it) | 153 | 0 | 508.1 s | 44 of 44 true | same | same |
| 5 | Git Bash, the two arguments of Section 3.6 | 153 | 0 | 491.9 s | 44 of 44 true | same | same |
| 6 | PowerShell 7.6.6 session, the two lines of Section 3.4 as written (`$LASTEXITCODE` printed `0`) | 153 | 0 | 412.8 s | 44 of 44 true | same | same |
| D1 | PowerShell 7.6.6 as run 1, clone folder named `Dirac_claude` (the default name of `git clone`) | 163 | 2 | 505.6 s | no verdict lines | not written | not written |
| D2 | PowerShell 7.6.6 as run 1 | 159 | 1 | 407.4 s | 43 of 44 true | written, different | same |
| 7 | PowerShell 7.6.6, the two arguments of Section 3.6 (`build/ma/...`), temporary folder of WolframScript watched | 141 | 0 | 422.9 s | 44 of 44 true | same | same |
| 8 | PowerShell 7.6.6, no argument, `DIRAC16_MATTER_ANTIMATTER_REPORT` = `build/env/report.json` | 141 | 0 | 417.3 s | 44 of 44 true | same | same |
| 9 | PowerShell 7.6.6, one argument `build/pos/report.json`, `DIRAC16_MATTER_ANTIMATTER_REPORT` = `build/env/report.json` | 141 | 0 | 416.6 s | 44 of 44 true | same | same |
| D3 | Git Bash 5.2.37, the two arguments of Section 3.6 | 159 | 1 | 415.6 s | 43 of 44 true | written, different | same |

Runs 1 and 2 are the two required runs of the documented command. Runs 3 to 6 check the
variants that Section 3 documents (run 6 is the PowerShell command typed exactly as in
Section 3.4). Runs D1 and D2 are the diagnostic runs of Section 6.4. Runs 1 to 5 and D1
were started between 06:04:20 and 06:06:59 (Pacific time) and ran at the same time; runs 6
and D2 ran between 06:15:09 and 06:23:23. The wall times of runs 1 to 5, D1 and D2 were
measured by a stopwatch around the process, that of run 6 from the clock times before and
after the command. Exit codes, peak memory and network connections of runs 1 to 5, D1 and D2 were
recorded by a monitor that examined the process tree every 1.5 seconds.

Runs 7, 8, 9 and D3 were made later on 2026-10-02, after a review of this file, at the
same commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, each in its own fresh clone. They
were started between 07:06:51 and 07:07:34 and ran at the same time (with about 13
Wolfram kernels of other jobs); the wall times were taken from the clock times before and
after the command. Run 7 checks the side effects of Section 3.6 and the temporary files of
Section 5.2 (the folder `WolframScriptTemporary` was listed every 0.25 s during the run).
Runs 8 and 9 check the environment variable of Section 3.5: in run 8 the report and the
theory file were written to `build/env/report.json` and
`build/env/matter-antimatter-theory.json` (the committed outputs were not touched; their
modification times stayed at the time of the clone); in run 9 they were written to
`build/pos/report.json` and `build/pos/matter-antimatter-theory.json`, and no folder
`build/env/` was created, so the argument took precedence over the variable. Run D3
repeats D2 from Git Bash (Section 6.4). In runs 7 to 9 and D3 the printed output and the
standard error were redirected to files; standard error was empty.

### 6.3 Byte identity and further checks

- **Report and theory file:** identical in runs 1 to 9 (same sha256
  `ad6b91296034a24c14b2ee08c7bfe8da98aaff2db83544897767e498adeaa269` and
  `1505a3962938477e5db42f568c0a1afcd21898c4409793178f8311b792638f10`), identical between
  run 1 and run 2, and identical to the committed files. In run D3 the theory file had
  this sha256 as well, and the report had the sha256
  `d6f62b7a4c6601e4425a6380c0908f9e29f60a2604e35a2a6f737ff79e49ca02`, the same bytes as
  the report of run D2.
- **Printed output:** 149 lines in every successful run, standard error empty. After
  removing the clock times of the progress lines, the output of runs 1, 2, 3 and 6 was
  identical; runs 4 and 5 differed from it only in the two lines `report=` and `theory=`.
  The output of runs 7, 8 and 9, with the clock times and the lines `report=` and
  `theory=` removed, was identical between the three runs (43048, 43060 and 43060 bytes
  with the Windows line endings, which differ only in these two lines).
- **Check counts:** `check_count=44`, `failed_check_count=0` and 44 lines `check_...=true`
  in runs 1 to 9.
- **Side effects:** in every clone `git status --porcelain --untracked-files=all` printed
  nothing after runs 1, 2, 3 and 6 (outputs rewritten with identical bytes; their
  modification times showed the end of the run). After runs 4 and 5 the scratch outputs
  lay in the ignored folder `build/`, which `git status --porcelain --ignored` shows as the
  single line `!! build/`. After runs 7, 8, 9 and D3 (none of whose clones had a folder
  `build/` before the run) `git status --porcelain` printed nothing,
  `git status --porcelain --ignored` printed exactly `!! build/`, and
  `git status --porcelain --ignored --untracked-files=all` printed exactly the two output
  files of the run (for run 7 `!! build/ma/theory.json` and
  `!! build/ma/wolfram-report.json`). In the clone of run 7,
  `Remove-Item -Recurse -Force build/ma` left an empty folder `build/` (and
  `git status --porcelain --ignored` printed nothing);
  `Remove-Item -Recurse -Force build` then removed it, after which
  `git status --porcelain --ignored --untracked-files=all` printed nothing. The same was
  found with `rm -r build/ma` and `rm -r build` in Git Bash in the clone of run D3.
- **Temporary files of WolframScript (run 7 and the runs started with it):** each of runs
  7, 8, 9 and D3 created two plain files (no folder) in
  `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary`: an empty one 0.05 to
  0.09 s after the start of `wolframscript` and a second one 2.5 to 2.8 s after the start,
  whose first line was the first progress line (for run 7
  `[07:06:54] algebra and fixture`). At the end the second file held 43048 (run 7), 43060
  (runs 8 and 9) and 43096 (run D3) bytes and was byte-identical to the printed output of
  its run (149, 149, 149 and 150 lines with Windows line endings). Both files of each run
  disappeared at most 0.3 s after the run ended, also for the exit code 1 of run D3. Short
  test programs gave: exit code 2, both files deleted; Ctrl+C (sent to the console of
  `wolframscript`, exit status `0xC000013A`) and killing the process, both files left
  behind (they were then deleted by hand), and the kernel ended in both cases.
- **Check commands:** the commands of Sections 3.3 and 4.3 were run after run 1 in
  PowerShell 7.6.6, in Windows PowerShell 5.1 and (the `wolframscript -code` and
  `sha256sum` commands) in Git Bash; they printed the sha256 values of Sections 2.1 and
  2.4, `44 of 44 checks true` and `{44, 44}`.
- **Dependent test:** `python -m unittest discover -s tests -p "test_d16c_matter_antimatter_publication.py"`
  in the clone of run 1, after the run: 29 tests, OK.

### 6.4 The Windows path-length limitation (open, not fixed in the code)

**Observation.** In a clone whose root path had 163 characters (run D1) the program ran to
the end, printed two `General::dirdep: Cannot get deeper in directory tree: ...` messages
for the folders
`kohn-sham\reference\m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836` and
`kohn-sham\rust\scf\m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836`, ended with
`ERROR: D16MARun failed or produced messages` and exit code 2, and wrote no file. In a
clone with a 159-character root (run D2)
the program listed all files without a message, but the kernel could not read the two long
files (full paths of 263 and 262 characters). It ended after 407.4 s with
`failed_check_count=1`, `failed_checks=MA_M1_ksFixedNetNumberRecorded` and exit code 1,
and it overwrote the committed report with a version that differs in two lines
(`"MA_M1_ksFixedNetNumberRecorded":false` and `"referenceLevelsChecked":165` instead of
`true` and `168`; sha256
`d6f62b7a4c6601e4425a6380c0908f9e29f60a2604e35a2a6f737ff79e49ca02`); the theory file was
byte-identical to the committed one.

**Root cause.** The Wolfram 15.0.1 kernel on Windows does not open files whose full path
is longer than 259 characters, although Windows long paths are enabled on the machine and
Git checked the files out. Measured directly with `FileNames["run.json", <folder>, 2]`,
`FileExistsQ` and `Import`: at root length 155 all 56 and 33 files were listed, and the
longest one (259 characters) exists for the kernel and was read; at root length 159 all
were listed, but for the two long files (263 and 262 characters) `FileExistsQ` returned
`False` and `Import` failed; at root length 163 `FileNames` stopped with `General::dirdep`
and listed 55 and 32 files, and `FileExistsQ` returned `False` for the 267-character
file. The two affected files are the ones named in
Section 2.3 (relative paths of 103 and 102 characters), so the root path may have at most
$259-1-103=155$ characters. Linux and macOS allow much longer paths and are not affected.

**The shell does not matter on Windows.** Run D3 started the program from Git Bash in a
clone with a 159-character root (`pwd -W | tr -d "\n" | wc -c` printed 159, the same as
`(Get-Location).Path.Length` in PowerShell). It ended exactly as run D2: after 415.6 s
with `failed_check_count=1`, `failed_checks=MA_M1_ksFixedNetNumberRecorded` and exit
code 1, no Wolfram message, a report with the sha256 of run D2 and a theory file identical
to the committed one. In the same clone, `wolframscript -code` started from Git Bash
listed all 56 reference files with `FileNames` but returned `False` from `FileExistsQ` for
the 263-character path. The limit therefore applies to Git Bash on Windows as well.

**Why it is not fixed in the code.** Any edit of the script or of the package changes
their sha256, which both committed outputs record under `sourceSha256`, which the Python
report, the unit test `tests/test_d16c_matter_antimatter_publication.py` and the
matter-antimatter document quote. A code fix therefore means new committed outputs and
new pins in other files; it was not made in this verification. The limitation is handled
by the instruction of Section 3.3 (clone into a short folder) and the diagnosis of
Section 3.7, item 3. A possible later fix: let the verifier test the length of the
repository path at the start and stop at once with a clear message, then commit the new
outputs and update every recorded sha256.

**A statement elsewhere that this corrects.** The textbook (Section 17.17 and Section
19.10 of `provenance/DIRAC16COMPLEX_TEXTBOOK.md`, from
`provenance/textbook/chapters/17-matter-and-antimatter.md` and
`19-reproducing-everything.md`) says that in a clone with a very long path the check
`MA_M1_ksFixedNetNumberRecorded` stays true and only three counts of the measurement
`M1_ksFixedNetNumber` change (55, 165 and 32 instead of 56, 168 and 33). With Wolfram
15.0.1 on 2026-10-02 this was not observed: at 163 characters the run stopped with exit
code 2 and wrote nothing, and at 159 characters the check
`MA_M1_ksFixedNetNumberRecorded` became false (exit code 1), with the counts 56, 165
and 33.
Those documents were not changed by this verification.

### 6.5 Fixes and open discrepancies

- **Fixes made:** none to the set. No file of the set was changed; no execution defect in
  the code was found that could be fixed without changing the committed outputs.
- **Corrections of this file after a review (2026-10-02, verified by runs 7 to 9 and D3
  and the tests of Section 6.3):** the temporary files of WolframScript are two plain
  files, one of them a full copy of the printed output, not a small folder (Sections 2.4
  and 5.2); the commits that last changed the five files of the set are `eac67e6`,
  `de0ee8b`, `6c0bfad` and `33c07a3`, not `27794e8` (Section 6.1);
  `git status --porcelain --ignored` prints `!! build/`, and the two files are listed only
  with `--untracked-files=all` (Sections 5.1 and 6.3); the run of Section 3.6 also creates
  the folder `build/` when it is missing, and Section 5.4 now says how to remove it; the
  environment variable `DIRAC16_MATTER_ANTIMATTER_REPORT` is documented (Sections 2.2, 2.4,
  3.5 and 3.7, item 11); the 155-character limit is stated for Git Bash on Windows, with
  its check command (Sections 3.3, 3.5 and 3.7, item 3); and the textbook Chapters 6 and
  7 are added to the documents that cite this set (Section 1.4).
- **Open:** the Windows path-length limitation of Section 6.4 (environment, documented).
- **Scientific discrepancies:** none. Every check is true and both outputs reproduce the
  committed bytes.
