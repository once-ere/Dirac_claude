## 0. How to use this book; installing the software; the honesty ledger

This chapter is the map of the book. It says what the book teaches and, just as important, what the equations of the book prove and what they do not prove. It explains how every statement is labelled, so that you always know whether it is proved, computed, assumed, a hypothesis or an open question. It installs the software on Windows, macOS or Linux, explains how the notebooks of the book are built and checked, and ends with the honesty ledger: the table of the main statements of the book with their labels and the files that verify them. The chapter has four worked examples, each a complete notebook: Notebook 00a checks that your computer is ready; Notebook 00b takes a first look, with numbers and pictures, at the eight directions of the author's universe and at the author's metric; Notebook 00c reads the verifier reports of the Revision record and checks the honesty ledger; Notebook 00d shows why every run of a notebook gives exactly the same bytes.

### 0.1 What this book teaches

The book is about a model of the very early universe proposed by the author. The universe of the model has eight directions instead of the four of everyday space and time. They are named $x_1$ to $x_8$, as the author names them. Three of them, $x_1$, $x_2$ and $x_3$, are the directions of ordinary space. One, $x_4$, is the time in which everything evolves. Three more, $x_5$, $x_6$ and $x_7$, behave like time as well; they are called the **extra times**. The last one, $x_8$, is a **hidden** direction of space. The author's **metric** (the rule that gives the length of a small step in each direction; Section 0.14 introduces it from zero) makes ordinary space grow (**inflate**) and the three extra times shrink (**deflate**) exponentially as the time $x_4$ runs.

Two fields live in this universe. A **field** is a rule that attaches numbers to every point of space and time: the temperature in a room attaches one number to every point, the wind three. The field **dirac16complex** attaches sixteen complex numbers of a special kind (anticommuting numbers, defined in Chapter 7) to every point; the field **dirac16complex00** attaches sixteen ordinary complex numbers. The book sets up the mathematics of both fields from zero, derives their equations and the equations of the gravitational field that they produce, introduces the density-functional (DFT) approximation, and solves the equations as far as present knowledge allows. Then it asks two questions and answers them honestly: do the equations prove that the big bang creates universes in pairs, and does the theory solve the puzzle of matter and antimatter? Section 0.2 gives the short answers; Part V of the book gives the complete proofs of what is proved and a precise list of what is not.

Every formula and every number of the book comes from the **Revision record**, the computations stored in the folder `Revision` of the repository Dirac_claude, or from the book's own notebooks, which reproduce the Revision record wherever the two overlap. (A **repository** is a folder of files whose history is kept by the program Git; Section 0.8 installs it.)

The book is written for a student who knows school algebra and the calculus of one variable (derivatives and integrals of functions of one variable), and nothing else. It is written in a way that we call a **deep dive**:

- every notion is defined, in plain words, before it is used;
- every derivation is written out line by line, and each line is followed by the rule that produced it from the line before; no step is left to "it can be shown";
- every worked example is a complete Jupyter notebook, a file of text and Python code that you run on your own computer, and the book prints it in full;
- just before each notebook the book prints the complete instructions for running it, on Windows, macOS and Linux, without sending you anywhere else;
- just after each notebook the book explains every line of its code in a section "Line-by-line walk-through";
- every number in the text names the notebook cell that computes it and, where it reproduces the Revision record, the record file and the check;
- every chapter ends with the section "What we proved, what we computed, what we assumed" and with at least five exercises with complete worked answers.

Read the chapters in order. Run each notebook when you reach it: reading a computation and doing it are different things, and the notebook lets you change a number and see what happens. Do each exercise before you read its answer.

### 0.2 The request, and what the equations prove and do not prove

The book answers a request of the author (2026-10-02) for a teaching book that describes every step of the formalism, derives the field equations, introduces and derives approximations of the DFT type, solves the equations as far as possible, and proves "that the ‘big bang’ creates universes in pairs" and that "this theory solves matter anti-matter mysteries". The first four parts of the request are carried out in Parts I to IV of the book. The last two cannot be delivered as they are worded, because the equations do not prove them, and a book that wrote them as established would teach something false. The book therefore follows one rule above every other, the **honesty rule**: it teaches exactly what the Revision record proves and computes, with every assumption, and it never writes "proved" for a statement that is not proved. The author was told this on 2026-10-02. Here is what the equations give, in plain words; the words that are new here (mass, self-coupling, energy-momentum tensor, charge) are defined from zero in later chapters.

**Pairs of universes.** Each field has a **mass** $m$ (a number that enters its equations) and a **self-coupling** $\lambda$ (the strength with which the field acts on itself). The Revision record proves exact maps between the solutions of the equations with mass $+m$ and those with mass $-m$:

- **T1** (both fields, every gravitational field): a fixed $16 \times 16$ matrix $\Gamma$, the **chirality**, turns every solution with $(m, \lambda)$ into a solution with $(-m, -\lambda)$; the Lagrangian (the function from which the equations follow) changes as $L_{m,\lambda}[\Gamma\Psi] = -L_{-m,-\lambda}[\Psi]$, the energy-momentum tensor $T$ (the table of the energy and momentum that the field carries) changes into $-T$, and the charge current $J$ into $-J$;
- **T2** (both fields): $\Gamma$ combined with a reflection of the group Pin(4,4) and with the Z2 mirror (a choice of boundary condition at the edge $z = \pi/2$ of the hidden direction, which is ASSUMED, not derived) turns $(m, \lambda)$ into $(-m, \lambda)$ with the same energy-momentum tensor;
- **Q** (dirac16complex): the quantum reading of T1; the image field carries the indefinite (Krein) metric $-B$, and there is no cancellation between two universes that are quantised independently of each other;
- **T3** (dirac16complex, the Kohn-Sham level, with the ASSUMED Z2 mirror): the Kohn-Sham universes of mass $+M$ and $-M$ have equal energies and equal energy-momentum tensors;
- **C1** (a consequence of T1): a T1 pair taken as the complete classical source of the author's metric is a zero source, and Einstein's equations then have no solution for $H > 0$.

These are PROVED: by two independent verifiers each, in `Revision/pairing/reports/wolfram-pairing.json` and `Revision/pairing/reports/python-pairing.json` (T1, T2, Q), in `Revision/pairing/kohn_sham/reports/wolfram-t3.json` and `Revision/pairing/kohn_sham/reports/python-t3.json` (T3), and, for C1, by T1 together with the checks `einstein_no_vacuum_solution` of `Revision/field_equations_a4/reports/wolfram-a4-report.json` and `einstein_no_vacuum` of `Revision/field_equations_a4/reports/python-a4-report.json`. They are exact **maps between solution sets**: if one solution exists, its partner exists too. What is NOT proved is that any universe is **created**, in pairs or otherwise: no creation process, no rate, no probability amplitude and no dynamics of a big bang follows from these equations, and a single universe of mass $+m$ is an equally valid solution without its partner. The pairing record says so itself: the report `Revision/pairing/reports/python-pairing.json` holds, under its key `not_established`, a list of twelve things that the theorems do not establish, and Notebook 00c prints all twelve. Chapters 18 to 20 give the complete proofs and the complete list. In the honesty ledger (Section 0.18) the statement "the big bang creates universes in pairs" is therefore labelled OPEN, with the note "not proved".

**Matter and antimatter.** The universe we observe contains matter but almost no antimatter. In 1967 Sakharov showed that an excess of matter can grow from an equal start only if three conditions hold: there are processes that change the number of baryons (the particles of ordinary matter, such as the proton); the symmetries called C and CP are violated; and the universe departs from thermal equilibrium. Chapter 21 explains all of this from zero, with the measured size of the excess (the baryon-to-photon ratio). What this theory proves is: the charge $Q$ of each field is exactly conserved (an exact U(1) symmetry), so no net charge can be generated inside one universe; the charge conjugations of the theory are two matrices, $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$; and a T1 partner carries the opposite charge, so a pair $\{+m, -m\}$ has total charge zero. Pairs of this kind belong to the class of ideas in which our universe has a partner of opposite charge (an "anti-universe"); one published example of the class is Boyle, Finn and Turok, Phys. Rev. Lett. 121, 251301 (2018). The theory as built does NOT solve the matter-antimatter problem: it has no baryons, no process that changes the number of baryons, no violation of CP, and no computation of a departure from equilibrium. To solve it, the theory would need all of these, and a computation of the excess that agrees with the measured one. That our universe actually has such a partner is a HYPOTHESIS, and every scenario built on it is labelled HYPOTHESIS.

**Charge conjugation is a matrix.** The author's gamma matrices are real (they contain only real numbers). For a field whose components are real numbers, plain complex conjugation changes nothing at all: it is the identity map, and it cannot be what charge conjugation means here. The charge conjugations of the theory are the matrices $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$ derived in Chapter 5 and Chapter 21 (PROVED: `Revision/lead_checks/reports/charge-conjugation-and-u1.json`, the checks `charge_conjugation_matrix_plus`, `charge_conjugation_matrix_minus` and `real_fields_charge_conjugation`; Notebook 00c opens this report and prints three of its details).

**A prescribed background.** The Kohn-Sham chapters let $a_4$ grow in proportion to the time, $a_4 = A H x_4$. This history is ASSUMED, a **prescribed background**: the computed Kohn-Sham states cannot be its source in the field equations (`Revision/field_equations_a4/reports/ks-source-conditions.json`).

### 0.3 The five labels of every statement

Every statement of the book that matters carries one of five labels, so that you always know how much it is worth:

| label | meaning |
| --- | --- |
| PROVED | exact; the book gives the complete proof, and an exact computer check confirms it (the report file and the name of the check are given) |
| COMPUTED | a number from a numerical computation, with its measured uncertainty and the file that holds it |
| ASSUMED | a starting point that the book does not derive (a convention, a physical input or an approximation); everything that depends on it says so |
| HYPOTHESIS | an idea that is stated and examined but not established |
| OPEN | a question that is not answered, in this book or anywhere else |

A statement can be PROVED in three ways. (1) A statement about finitely many definite objects, such as "these eight matrices of whole numbers satisfy these 64 equations", is proved by an exact computation of every case. (2) A statement in which the computer keeps the unknown quantities as symbols, such as "for every function $a_4$ the determinant of the metric is $\cos^2 z$", is proved by an exact symbolic computation, which holds for every value of the symbols, like a derivation by hand. (3) A statement about infinitely many cases that the computer cannot hold as symbols, such as "in every gravitational field", is proved by a general derivation in the book; an exact check at a few test points then confirms the derivation (and would catch many errors), but it is not the proof.

Examples from this chapter. "The determinant of the author's metric is $\cos^2 z$" is PROVED (way 2; Section 0.14). "The ground-state energies of the canonical and the refined run of the Revision record's Kohn-Sham solver differ by at most $1.901 \times 10^{-12}$ (relative)" is COMPUTED (Notebook 00d). "The Z2 mirror at the edge of the hidden direction" is ASSUMED. "Our universe has a partner of opposite charge" is a HYPOTHESIS. "The big bang creates universes in pairs" was proposed by the author as a hypothesis; as a question of this book it is OPEN, and the ledger says why: it is not proved.

### 0.4 How to check a statement yourself

You can check a statement at three levels.

**Level 1, the derivation.** Follow it line by line in the book. If a line does not follow from the line before it, you have found either a gap in your understanding or an error in the book; both are worth finding.

**Level 2, the report.** Every exact verifier of the Revision record writes its results into a **report**, a JSON file (a plain text file of names, numbers and lists that Python reads directly). A report lists its **checks**; each check has a name, a **verdict** (PASS or FAIL) and a detail text that says exactly what was verified. You can read a report yourself. Open a terminal, activate the Python environment of the book and go into the repository folder (Section 0.8 shows how), type `python` and press Enter. Python shows its prompt, three greater-than signs, at the start of each input line. Type the text after each prompt (the lines that start with three dots are the second line of the loop; press Enter once more on the empty line after them):

```text
>>> import json
>>> path = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
>>> report = json.load(open(path, encoding="utf-8"))
>>> report["summary"]["passed"], report["summary"]["total"]
(12, 12)
>>> for check in report["checks"][:3]:
...     print(check["verdict"], check["name"])
...
PASS representation_real
PASS B_imaginary_hermitian
PASS intertwiners_same_mass
>>> exit()
```

The answer `(12, 12)` says that 12 of the 12 checks of this report passed; the loop prints the verdict and the name of its first three checks. Notebook 00c does exactly this, for every report of the Revision record at once.

**Level 3, the computation.** Run the verifier again and compare its new report with the stored one. The verifiers need Wolfram Mathematica (which the notebooks of this book never need) or Rust, and some run for hours; Chapter 23 lists every command.

### 0.5 Conventions used everywhere

These conventions hold on every page. They are choices, not results (ASSUMED).

- **The names of the coordinates** are the author's: $x_1, x_2, \ldots, x_8$. In Python lists and arrays the entries are counted from 0, so the entry of $x_1$ has the index 0 and that of $x_8$ the index 7. The book never uses the numbering $x_0, \ldots, x_7$ of older documents.
- **The roles of the coordinates.** $x_1, x_2, x_3$: ordinary space, which inflates; $x_4$: the time; $x_5, x_6, x_7$: the three extra times, which deflate exponentially; $x_8$: the hidden direction of space, through the variable $z = 6 H x_8$ with $0 < z < \pi/2$, where $H > 0$ is a constant of the author.
- **The signs of the directions** are $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in the order $x_1, \ldots, x_8$: the directions $x_1, x_2, x_3, x_8$ are space-like and $x_4, x_5, x_6, x_7$ time-like; the **signature** is (4,4). (Section 0.14 explains these words; the Revision record states the signs in the file `Revision/algebra/gammas.json`, and its Wolfram verifier checks them: `Revision/algebra/reports/wolfram-algebra.json`, check `eta_in_author_order`.)
- **Units.** The formulas of the Revision record contain no speed of light and no Planck constant: they are written in units in which both are 1, as is usual in this kind of physics. A chapter that computes numbers says in which unit it measures them (for example in units of the mass $m$).
- **Files** are named by their path in the repository, written with `/` and starting at the repository folder, for example `Revision/README.md`; the book prints such names in typewriter type.

### 0.6 The map of the book

The book has five parts and an appendix. Each chapter uses only what earlier chapters have built.

Part I, getting ready.

- Chapter 0 (this chapter): how to use the book, the software, how the notebooks are built, the honesty ledger.
- Chapter 1: mathematics from zero, part I: numbers, complex numbers, vectors, matrices, index notation, determinants, the generalized Kronecker delta.
- Chapter 2: mathematics from zero, part II: functions of several variables, partial derivatives, differential equations and how a computer solves them, the shooting method.
- Chapter 3: the geometry of space and time: the metric, the signature (4,4), the author's metric, curvature.

Part II, spinors and fields.

- Chapter 4: the Clifford algebra and the author's sixteen gamma matrices T16.
- Chapter 5: the matrices $C$, $\Gamma$ and $B$, the groups Pin(4,4) and Spin(4,4), and the charge-conjugation matrices.
- Chapter 6: spinors in the curved 4+4 space: the vielbein, the spin connection, the covariant derivative.
- Chapter 7: the two fields and their Lagrangians; Grassmann numbers; the field equations.
- Chapter 8: what non-triviality means exactly, and the growth of the extra-time modes.
- Chapter 9: the energy-momentum tensor: energy density, pressures, equations of state, conservation.
- Chapter 10: canonical quantisation in 4+4 dimensions and the Krein space.

Part III, the field equations of gravity.

- Chapter 11: the generalized Kronecker delta and the Lovelock tensors.
- Chapter 12: the field equations for $a_4$.

Part IV, density functional theory.

- Chapter 13: many-body quantum mechanics and density functional theory from zero.
- Chapter 14: the Kohn-Sham model of dirac16complex in the deflating field.
- Chapter 15: solving the Kohn-Sham equations with the Rust solver.
- Chapter 16: checking the solution with an independent solver.
- Chapter 17: why the Kohn-Sham history of $a_4$ is a prescribed background.

Part V, pairs of universes, matter and antimatter.

- Chapter 18: the pairing theorems T1, T2 and Q with complete proofs.
- Chapter 19: T3, the Kohn-Sham universes of mass $+M$ and $-M$.
- Chapter 20: do universes come in pairs? What the equations prove, and what they do not.
- Chapter 21: matter and antimatter from zero, and what this theory does and does not contribute.
- Chapter 22: open problems, and how a student could attack each.

Appendix.

- Chapter 23: reproducing everything; the glossary; the index of the checks and of the notebooks.

### 0.7 Every example is a notebook

Every worked example of the book is a **Jupyter notebook**: a file (with the ending `.ipynb`) that holds text and Python code in **cells**, together with everything the code printed and drew when it ran. A **markdown cell** holds text; a **code cell** holds Python code. The **kernel** is the running Python program that executes the code cells one after the other. The notebooks are numbered by chapter and letter: Notebook 00a is the first notebook of Chapter 0, Notebook 00b the second, and so on. The book prints every notebook in full, in three parts:

- a section "How to run Notebook NNx" (NN is the number of the chapter and x the letter), which gives the complete instructions for running the notebook on Windows, macOS and Linux;
- a section "Notebook NNx: complete text", which prints every cell in order, with what each code cell printed and every figure it drew;
- a section "Line-by-line walk-through of Notebook NNx", which explains every line of every code cell.

Every notebook has the same numbered sections: (1) what it computes; (2) how to run it, the same complete instructions again; (3) the words it uses; (4) the physical and mathematical situation; then the computation in small steps, each code cell preceded by a text cell that says what it does; and last, what it showed. The first code cell, the **set-up cell**, repeats the instructions as comment lines and prepares the helpers that every notebook uses.

Every computation is followed by **checks**: statements that must be true. When a check is true, the notebook prints a line that starts with PASS and names the check. When a check reproduces a number or a verdict of the Revision record, a second line starting with "reproduces" names the record file and the check in it. When a check is false, the notebook stops with an error that names the check. Lines that start with RESULT print the key numbers. The last line of every notebook says how many checks passed, for example ALL 9 CHECKS PASSED (notebook 00a).

Every figure is saved as a PNG picture file in the folder `Revision/textbook/figures`, named after the notebook, its number and a short name (for example `00a_1_parabola_tangent.png`), and the book prints it with a caption that says what is plotted, what the axes and their units are, and what you should see. The book refers to it as Figure 00a.1.

Next to every notebook lies its **provenance file**, with the same name and the ending `.PROVENANCE.md` (for example `Revision/textbook/notebooks/00a_check_installation.PROVENANCE.md`). It records what the notebook computes and from which Revision records; the complete instructions for running it; the expected output (every PASS line, every RESULT line, every figure with its caption); every file it writes; its run time and peak memory; the computer and the versions of the programs with which it was run; the sha256 fingerprints of the notebook and of every file it writes (Section 0.18 explains fingerprints); and the date and result of its last check.

### 0.8 Installing the software

The complete installation commands are printed in the section "How to run" before every notebook, for the first time in Section 0.11; you follow them once per computer, and later notebooks need only the steps that start JupyterLab. This section explains what each piece of software is and why it is needed, and adds the installation of Rust, which only seven notebooks need.

**A terminal** is the window in which you type commands: on Windows the app Windows PowerShell (or Terminal), on macOS the app Terminal (it runs the shell zsh), on Linux any terminal (it runs the shell bash). A command is typed exactly as printed and sent with the Enter key. The commands are printed in framed blocks, one command per line; where they differ between the systems, the block is labelled with the system.

**Git** is the program that downloads the repository and keeps track of the versions of its files. On Windows it is installed from https://git-scm.com/download/win; on macOS it comes with the developer tools (the command `xcode-select` with the option install, printed in the instructions); on Linux it is a package of the system.

**Python** is the programming language of the notebooks. The book needs Python 3.12 or newer; it was built with Python 3.14.5. A **version number** such as 3.14.5 names one release of a program: the first number changes rarely, the second for new features, the third for corrections.

**The repository** is downloaded with one command,

```text
git clone https://github.com/once-ere/Dirac_claude.git
```

which creates the folder Dirac_claude (a few hundred megabytes; the folder then needs up to about 1 GB of disk space). To get a newer version later, run `git pull` inside that folder.

**A private Python environment** is a folder with its own copy of Python and of the packages, so that installing the packages changes nothing else on your computer. The instructions create it in the folder dirac-book-env inside your home folder and **activate** it: from then on, in this terminal, the commands `python` and `jupyter` are those of the environment, and the prompt starts with (dirac-book-env). An environment must be activated again in every new terminal. On Windows, PowerShell refuses to run the activation script until the command with `Set-ExecutionPolicy` allows it for the one window in which it is typed; it changes nothing permanently.

**The nine packages** are installed with Python's installer pip at fixed (**pinned**) versions, the versions with which the book was built: numpy 2.4.6 (arrays of numbers, matrices), sympy 1.14.0 (exact algebra and calculus with symbols), mpmath 1.3.0 (numbers with as many digits as we ask for), matplotlib 3.11.0 (plots), and jupyterlab 4.4.10, nbformat 5.10.4, nbclient 0.10.2, ipykernel 7.1.0 and nbconvert 7.16.6 (the programs that show, store and run notebooks). Another version of a package may print slightly different last digits or draw slightly different pictures; Notebook 00a checks that every package has its pinned version. The pins of these nine packages and of the 93 packages they need in turn are listed in the file `Revision/textbook/requirements.txt`; with the environment active, the command below, run in the repository folder, installs all of them at once at the exact versions of the book (the commands in the run instructions install the nine and let pip choose the others):

```text
python -m pip install -r Revision/textbook/requirements.txt
```

**JupyterLab** shows a notebook in your web browser and runs it: with the environment active, in the folder `Revision/textbook/notebooks`, the command `jupyter lab` followed by the name of the notebook file opens it, and the menu Run > Run All Cells runs every cell from the top. A notebook can also be run without a browser (**headless**) with `jupyter nbconvert`; the run instructions print the exact command.

**Rust** is a second programming language. The longest computations of the Revision record (the generalized Kronecker delta and the Lovelock tensors, and the Kohn-Sham solver) are Rust programs, and seven notebooks run them: 11a and 11b, 15a, 15b and 15d, 16a and 19a. Their run instructions include the following installation, which you do once per computer. **cargo** is Rust's program that turns the Rust code of a program into a program that the computer can run (it **builds** it). On Windows, download `rustup-init.exe` from https://rustup.rs, run it and accept the default choices; if it reports that the Visual Studio C++ Build Tools are missing, let it install them (or install the workload "Desktop development with C++" from https://visualstudio.microsoft.com/visual-cpp-build-tools/ and run `rustup-init.exe` again). On macOS and Linux, run the command below and accept the default choice (on Linux first run `sudo apt install build-essential`, which provides the linker that Rust needs):

```text
curl --proto "=https" --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Then open a new terminal and check the version of cargo; it must print 1.91.1 or a newer version. The two Rust programs are built with these commands, in the repository folder (the same commands on all three systems):

```text
cargo --version
cargo build --release --manifest-path Revision/gkd_lovelock/code/Cargo.toml
cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
```

A build writes the folder `target` next to the file `Cargo.toml` of its program (git ignores it). The two programs use no package from the internet, so cargo downloads nothing. A notebook that needs a program runs the same build command itself before it uses it.

**Removing everything** again is simple: delete the folders dirac-book-env and Dirac_claude in your home folder; nothing else was changed. Rust removes itself with the command `rustup self uninstall`.

### 0.9 How the notebooks are built and checked

You do not need this section to run the notebooks; it explains why you can trust that the printed notebooks are exactly what the code produces.

No notebook of the book is edited by hand. Each one is made by a **builder**, a Python file in the folder `Revision/textbook/notebooks/src` with the same name as the notebook (for example `Revision/textbook/notebooks/src/00a_check_installation.py`), which lists the notebook's cells and its facts: its title, the Revision records it reads, the packages it needs, the files it writes, its expected run time and its last printed lines. The book's tool **nbkit** (the file `Revision/textbook/tools/nbkit.py`) turns a builder into a notebook in two steps.

**Build.** nbkit inserts the run instructions and the set-up cell, executes the notebook with the kernel python3 in the folder `Revision/textbook/notebooks`, with the hash seed `PYTHONHASHSEED` set to 0 (Section 0.22 explains what it is), checks every output against the rules of the book, removes everything that differs from run to run without meaning anything (time stamps and timing data), and stores the executed notebook, its figures and its captions.

**Check.** nbkit executes the notebook a second time, now with the hash seed 1 and with every file written into a scratch folder instead of the repository (the environment variable `TEXTBOOK_OUTPUT_ROOT` of the set-up cell names that folder), and compares everything byte for byte: the notebook, every file it wrote, and the provenance file regenerated from its record. Only when everything is identical does the check print PASSED; the result and its date are stored in the provenance file. The rules that a build and a check enforce include: no error and nothing printed on the error channel; every printed line at most 89 characters of plain ASCII text (the width of a page of the book); no memory address and no folder of the build computer in the output; every figure saved at 150 dots per inch, without the name of the program that made it, and at most 1.25 times as high as it is wide; and exactly the files that the builder lists are written.

From the repository folder, with the environment active, the check of one notebook is the command

```text
python Revision/textbook/notebooks/src/00a_check_installation.py check
```

(it prints `check_00a=PASSED` at the end; the scratch folder is a folder in the system's temporary folder). Because the comparison is byte for byte, it is meant for the computer on which the book was built: on another computer a figure may differ in a few bytes (for example through another version of a font library), which is harmless for the student but fails a byte-for-byte comparison. Notebook 00d shows, with small experiments, what else could make two runs differ, and how the book prevents it.

### 0.10 Example: checking the installation

The first notebook computes no physics. It checks that Python and the packages are installed at the right versions, prints the version of cargo when Rust is installed, does one small computation with each of numpy, sympy and mpmath, and draws two teaching plots. Run it first: if it ends with the line ALL 9 CHECKS PASSED (notebook 00a), every notebook of the book that needs no Rust can run on your computer.

The two plots illustrate two facts that the book uses again and again. We derive both here, line by line.

**The tangent line of a parabola.** The parabola is $y = x^2$, and we want the straight line that touches it at the point $(1, 1)$. The slope of the parabola at $x$ is the derivative

$$
\frac{d}{dx} x^2 = 2x
$$

(the power rule $\frac{d}{dx} x^n = n x^{n-1}$ with $n = 2$). At $x = 1$ the slope is $2 \cdot 1 = 2$ (substitution of $x = 1$). The line through the point $(1, 1)$ with slope 2 is

$$
y = 1 + 2(x - 1)
$$

(the point-slope form $y = y_0 + s(x - x_0)$ of a straight line with $x_0 = 1$, $y_0 = 1$, $s = 2$), that is

$$
y = 2x - 1
$$

(multiply out the bracket, $2(x - 1) = 2x - 2$, and add $1 - 2 = -1$). The gap between the parabola and the line is

$$
x^2 - (2x - 1) = x^2 - 2x + 1
$$

(remove the bracket: a minus sign in front of a bracket changes the sign of every term in it), and

$$
x^2 - 2x + 1 = (x - 1)^2
$$

(the binomial formula $(a - b)^2 = a^2 - 2ab + b^2$ with $a = x$, $b = 1$). A square is never negative and is zero only when the number squared is zero, so the gap is never negative and is zero only at $x = 1$: the line touches the parabola at the single point $(1, 1)$ and lies below it everywhere else. Status: PROVED (above, by school algebra); Notebook 00a confirms it at 401 points (COMPUTED, Figure 00a.1).

**A growing and a shrinking exponential.** For every number $t$,

$$
e^{t} \, e^{-t} = e^{t + (-t)}
$$

(the law of exponents $e^{u} e^{v} = e^{u + v}$), and

$$
e^{t + (-t)} = e^{0} = 1
$$

(the exponent is $t - t = 0$, and $e^{0} = 1$ because any nonzero number to the power 0 is 1). So $e^{-t} = 1/e^{t}$: when $e^{t}$ grows, $e^{-t}$ shrinks by exactly the same factor. The author's metric has this pattern (Section 0.14): lengths along ordinary space carry the factor $e^{a_4}$ and lengths along the extra times the factor $e^{-a_4}$, so when $a_4$ grows, ordinary space inflates while the extra times deflate. Status: PROVED; Notebook 00a confirms it at 401 points (COMPUTED, Figure 00a.2).

<!-- NOTEBOOK 00a -->

### 0.13 Line-by-line walk-through of Notebook 00a

The notebook has ten code cells, In [1] to In [10]. This section explains every line of every one of them. (The label In [k] is the number that Jupyter gives a code cell when it runs it; Out [k] is what that cell printed.)

**In [1], the set-up cell.** Its first part repeats the complete run instructions of Section 0.11 as **comment lines**: every line that starts with `#` is a comment, which Python skips. They are there so that the notebook file carries its own instructions, even when it is copied without the book. The code starts after the line THE SET-UP between two lines of `=` signs. The set-up cell is the same in every notebook of the book, except for the one line that names the notebook.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module** (a part of Python or of a package) so that the code can use it; the text after `#` on each line is a comment. `json`, `os`, `textwrap` and `pathlib` come with Python itself. `from pathlib import Path` takes the single name `Path` out of the module `pathlib`; a `Path` is the address of a file or folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

These lines load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python code), which show a picture file below a cell.

```python
NOTEBOOK_ID = "00a"  # this notebook: chapter 00, example a
```

A **variable** is a name for a value; this line gives the name `NOTEBOOK_ID` to the text `"00a"` (a text in quotes is called a **string**). It is the only line of the set-up code that differs from notebook to notebook; the figure files and the last printed line are named after it.

```python
def find_repository_root():
    """Return the repository folder (Dirac_claude).

    Jupyter runs a notebook in the folder that holds it.  Starting there, go up one
    folder at a time until a folder contains Revision/textbook/requirements.txt (the
    list of the book's packages); that folder is the repository."""
    here = Path.cwd().resolve()  # the folder in which this notebook runs
    for folder in [here, *here.parents]:  # this folder, its parent, its grandparent ...
        if (folder / "Revision" / "textbook" / "requirements.txt").is_file():
            return folder
    raise FileNotFoundError(
        "The repository folder was not found: open this notebook inside the folder "
        "Revision/textbook/notebooks of the repository Dirac_claude")
```

`def` defines a **function**: a named piece of code that runs when it is called. The text in triple quotes below the `def` line is its **docstring**, a description that Python stores but does not run. `Path.cwd()` is the folder in which the notebook runs, and `.resolve()` writes it as a complete address. `here.parents` lists the parent folder, its parent, and so on up to the top of the disk; `[here, *here.parents]` is the **list** (an ordered collection, written in square brackets) that starts with `here` and continues with all of them. The `for` loop takes the folders of this list one after the other and runs the indented lines for each. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that contains `Revision/textbook/requirements.txt` is the repository, and `return` hands it back and ends the function. If no folder qualifies, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do (two strings written next to each other are joined into one).

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The first code line calls the function and names its result `REPO`. As the comment says, the notebook never prints `REPO`. The last line chooses the folder below which the notebook writes its files. `os.environ` holds the **environment variables** of the running program (named texts that a program receives from the computer when it starts); `.get(name, default)` returns the value of the variable `TEXTBOOK_OUTPUT_ROOT` if it is set and the default `str(REPO)` (the repository folder as a string) otherwise, and `Path(...)` turns the string into a path. When you run the notebook the variable is not set, so the files go into the repository. The checking tool nbkit sets it to a scratch folder (Section 0.9), so that a check never changes the repository.

```python
def repository_file(relative):
    """The path of the repository file relative, for READING (a Revision record)."""
    return REPO / relative


def output_file(relative):
    """The path at which to WRITE the repository file relative (its folder is made)."""
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

Two small functions. `repository_file("Revision/...")` gives the full path of a file of the repository, for reading. `output_file("Revision/...")` gives the full path at which to write a file; `path.parent` is the folder that will hold it, and `.mkdir(parents=True, exist_ok=True)` creates that folder together with any missing folder above it, and does nothing if it exists already.

```python
def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters, so that every printed line fits the width of a page of the book. `str(text)` turns any value into a string; `textwrap.fill` breaks it at blanks into lines of at most 89 characters, every line after the first starting with four blanks; `print` writes the result below the cell.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

matplotlib reads personal settings from a file on your computer if you have one. `matplotlib.rcdefaults()` returns to the built-in settings, so that the figures are the same on every computer. `plt.rcParams.update({...})` then sets four settings for every figure of the notebook: the size of a figure (7.0 inches wide and 4.2 inches high), the size of its letters (10 points), and a faint grid of lines behind the curves (`grid.alpha` 0.3 means 30 per cent opaque). The braces `{...}` make a **dictionary**: pairs of a key and a value, written `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/00a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes the text `{}` and a line end into the captions file: an empty dictionary of captions, which `save_figure` fills. `encoding="utf-8"` fixes how the letters are stored as bytes, and `newline="\n"` stores the same line end on every operating system (Section 0.22 explains why this matters).

```python
def save_figure(fig, name, caption):
    """Save the figure fig as Revision/textbook/figures/<id>_<k>_<name>.png, record its
    caption in CAPTION_FILE, show the saved picture below the cell and close the figure.
    k counts the figures of the notebook 1, 2, 3, ...; a cell run again keeps its k."""
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
    # dpi=150: 150 dots per inch.  bbox_inches="tight": cut away the empty margin.
    # metadata={"Software": None}: no program name is stored in the PNG file, so that
    # every run writes exactly the same bytes.
    fig.savefig(output_file(relative), dpi=150, bbox_inches="tight",
                metadata={"Software": None})
    plt.close(fig)  # forget the figure, so that Jupyter does not draw it a second time
    CAPTIONS[file_name] = caption
    output_file(CAPTION_FILE).write_text(
        json.dumps(CAPTIONS, indent=1, sort_keys=True) + "\n", encoding="utf-8",
        newline="\n")
    display(Image(filename=str(output_file(relative))),
            metadata={"textbook_figure": file_name})  # the saved picture itself
    say(f"Figure {NOTEBOOK_ID}.{number} saved as {relative}")
```

This function saves a figure and shows it. `setdefault(name, value)` returns the number already stored for this figure name, or, for a new name, stores and returns `len(FIGURE_NUMBERS) + 1` (one more than the number of figures so far); so the figures are numbered 1, 2, 3, ... and a cell that you run twice keeps the number of its figure. The file name is made of the notebook id, the number and the name, for example `00a_1_parabola_tangent.png`. `fig.savefig` writes the picture as a PNG file with 150 dots per inch, cuts away the empty margin and, as the comments say, stores no program name in the file, so that two runs write exactly the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time at the end of the cell. The caption is stored in `CAPTIONS`, and the whole dictionary is written into the captions file: `json.dumps` turns it into JSON text with one entry per line (`indent=1`) and the keys in alphabetical order (`sort_keys=True`). `display(Image(...))` shows the saved picture below the cell; the `metadata` entry tells the book's tools which file the picture is. The last line prints where the figure was saved.

```python
PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    """A check.  If condition is False, stop with an AssertionError that names the
    check (an if statement is used instead of assert, because python -O would skip an
    assert).  Otherwise print "PASS <name>" and, when the check reproduces a Revision
    record, a second line naming the record file and its check."""
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")
```

`PASSED` is an empty list. `check` is the function behind every check of the book. `condition` is a statement that is either true (`True`) or false (`False`). If it is false, `raise AssertionError(...)` stops the notebook with an error that names the check. (Python also has a statement `assert` for this; the docstring says why the book does not use it: Python started with its option O, for "optimise", skips every `assert`.) If the condition is true, the name is appended to `PASSED` and a line `PASS name` is printed. `record=None` makes the third argument optional: a check that reproduces a number of the Revision record passes the record's file and check name, and `check` prints them on a second line that starts with five blanks and the word reproduces.

```python
def report(label, value, unit=""):
    """Print a key number as a line "RESULT <label> = <value> <unit>"."""
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    """Print the last line of the notebook: how many checks passed."""
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a line that starts with RESULT; `(f" {unit}" if unit else "")` adds a blank and the unit when a unit is given and nothing otherwise (an empty string counts as false). `all_checks_passed` prints the last line of every notebook; `len(PASSED)` is the number of checks that passed. The last statement prints the one line of Out [1].

**In [2], Python.**

```python
import importlib.metadata  # reads the version numbers of installed packages
import platform  # reads the version number of Python

python_version = platform.python_version()  # a text such as "3.14.5"
say(f"Python version: {python_version}")
```

`platform.python_version()` returns the version of the running Python as a string; on the computer that built the book it is `"3.14.5"`, which the next line prints (Out [2], first line).

```python
# The first two numbers of the version, as whole numbers: "3.14.5" -> 3 and 14.
major, minor = (int(part) for part in python_version.split(".")[:2])
# Pairs of numbers are compared like words in a dictionary: first the first number,
# then, if they are equal, the second one.
check((major, minor) >= (3, 12), "Python is version 3.12 or newer")
```

`python_version.split(".")` cuts the string at the dots into the list `["3", "14", "5"]`; `[:2]` keeps the first two entries; `int(part)` turns each into a whole number; and `major, minor = ...` names them 3 and 14. Python compares the pairs `(3, 14)` and `(3, 12)` as the comment says: the first numbers are equal, so the second numbers decide, and 14 is at least 12. The condition is true, and the check prints PASS Python is version 3.12 or newer.

**In [3], the packages.**

```python
PINNED = {  # package name -> the version with which the book was built
    "numpy": "2.4.6",
    "sympy": "1.14.0",
    "mpmath": "1.3.0",
    "matplotlib": "3.11.0",
    "jupyterlab": "4.4.10",
    "nbformat": "5.10.4",
    "nbclient": "0.10.2",
    "ipykernel": "7.1.0",
    "nbconvert": "7.16.6",
}
```

The dictionary `PINNED` holds the nine packages of Section 0.8 with their pinned versions.

```python
for package, pinned in PINNED.items():
    installed = importlib.metadata.version(package)  # error if not installed
    # {package:12} pads the name with blanks to 12 characters: aligned columns.
    say(f"{package:12} installed {installed:10} pinned {pinned}")
# The packages whose installed version differs from the pinned one (a list):
different = [p for p, v in PINNED.items() if importlib.metadata.version(p) != v]
check(different == [], "every package has its pinned version")
```

`PINNED.items()` gives the pairs (package, pinned version); the loop names them `package` and `pinned`. `importlib.metadata.version(package)` reads the installed version (and stops with an error if the package is not installed). In the f-string, `{package:12}` writes the name padded with blanks to 12 characters and `{installed:10}` the version padded to 10, so that the printed table of Out [3] has straight columns. The line `different = [...]` is a **list comprehension**: it collects every package `p` whose installed version differs from its pinned version `v` (`!=` means "is not equal to"). The check requires that this list is empty, `[]`.

**In [4], cargo.**

```python
import shutil  # finds a program on the computer
import subprocess  # runs a program and reads what it prints

cargo = shutil.which("cargo")  # where cargo is, or None when it is not installed
if cargo is None:
    say("cargo is not installed; only the notebooks that run the Rust programs of "
        "the repository need it.")
else:
    completed = subprocess.run([cargo, "--version"], capture_output=True, text=True)
    say(f"cargo version: {completed.stdout.strip()}")
```

`shutil.which("cargo")` searches the folders in which the computer looks for programs and returns the path of cargo, or the special value `None` if there is none. `if ... else` runs the first indented block when the condition is true and the second block otherwise. `subprocess.run([...])` runs cargo with the option that asks for its version (the list holds the program and the option, two hyphens followed by the word version); `capture_output=True, text=True` collects what it prints as a string in `completed.stdout`, and `.strip()` removes the line end. On the computer that built the book cargo is installed, and Out [4] shows its version, 1.91.1. This cell prints but checks nothing, because most notebooks do not need cargo.

**In [5], numpy.**

```python
import numpy as np  # arrays of numbers, matrices, linear algebra

matrix = np.array([[1.0, 2.0], [3.0, 4.0]])  # the rows (1, 2) and (3, 4)
determinant = np.linalg.det(matrix)  # 1*4 - 2*3 = -2, up to rounding
report("determinant of the matrix with rows (1, 2) and (3, 4)", f"{determinant:.12f}")
check(abs(determinant - (-2.0)) < 1e-12, "numpy: the determinant is -2")
```

`np.array` makes a matrix from the list of its rows. `np.linalg.det` computes its determinant, $1 \cdot 4 - 2 \cdot 3 = -2$, with floating-point numbers, which keep about 16 significant digits and may be wrong in the last one (Section 0.22). `{determinant:.12f}` prints the number with 12 digits after the decimal point: Out [5] shows −2.000000000000. `abs(...)` is the absolute value, and `1e-12` means $10^{-12}$: the check accepts the result when it differs from $-2$ by less than $10^{-12}$.

**In [6], sympy.**

```python
import sympy as sp  # exact algebra and calculus with symbols

x = sp.symbols("x")  # a symbol: a letter that stands for any number
derivative = sp.diff(sp.sin(x) ** 2, x)  # the derivative of sin(x)^2 with respect to x
say(f"d/dx sin(x)^2 = {derivative}")
check(sp.simplify(derivative - sp.sin(2 * x)) == 0,
      "sympy: the derivative of sin(x)^2 is sin(2x)")
```

`sp.symbols("x")` makes the symbol $x$. In Python `**` means "to the power", so `sp.sin(x) ** 2` is $\sin^2 x$, and `sp.diff(..., x)` differentiates it with respect to $x$; by the chain rule the result is $2 \sin x \cos x$, which sympy prints as `2*sin(x)*cos(x)` (Out [6]). The check asks sympy to simplify $2 \sin x \cos x - \sin 2x$; by the double-angle formula $\sin 2x = 2 \sin x \cos x$ the result is exactly 0, and `== 0` tests that.

**In [7], mpmath.**

```python
import mpmath  # numbers with as many digits as we ask for

mpmath.mp.dps = 30  # dps = decimal places: work with 30 significant digits
pi_text = mpmath.nstr(mpmath.pi, 30)  # pi written with 30 significant digits
say(f"pi to 30 significant digits: {pi_text}")
check(pi_text == "3.14159265358979323846264338328", "mpmath: pi to 30 digits")
```

`mpmath.mp.dps = 30` tells mpmath to compute with 30 significant decimal digits. `mpmath.nstr(mpmath.pi, 30)` writes $\pi$ as a string with 30 significant digits, correctly rounded (the 30th digit of $\pi$ is a 7 and the 31st a 9, so the 7 is rounded up to 8), and the check compares it with the known value character by character.

**In [8], the parabola and its tangent line.**

```python
x_values = np.linspace(-1.0, 3.0, 401)  # 401 equally spaced numbers from -1 to 3
parabola = x_values ** 2  # y = x^2 at each of these numbers
tangent = 2.0 * x_values - 1.0  # the tangent line y = 1 + 2 (x - 1) = 2x - 1
gap = parabola - tangent  # (x - 1)^2 at each number
```

`np.linspace(-1.0, 3.0, 401)` makes an **array** (numpy's list of numbers) of 401 numbers from $-1$ to $3$ with equal steps of $4/400 = 0.01$. Arithmetic on an array acts on every number in it: `x_values ** 2` is the array of the 401 squares, and `2.0 * x_values - 1.0` the array of the 401 values of the tangent line of Section 0.10. Their difference `gap` is $(x - 1)^2$ at each point.

```python
fig, ax = plt.subplots()  # a new figure with one pair of axes
ax.plot(x_values, parabola, label="parabola $y = x^2$")
ax.plot(x_values, tangent, "--", label="tangent line $y = 2x - 1$")
ax.plot([1.0], [1.0], "o", color="black", label="the point $(1, 1)$")
ax.set_xlabel("$x$")  # the label of the horizontal axis
ax.set_ylabel("$y$")  # the label of the vertical axis
ax.set_title("A parabola and its tangent line at $x = 1$ (slope 2)")
ax.legend()  # the box that names the three curves
```

`plt.subplots()` makes a new figure `fig` with one pair of axes `ax`. `ax.plot(xs, ys)` draws a line through the points with these coordinates; the third argument of the second `ax.plot` line, a string of two hyphens, makes that line dashed, and `"o"` in the third one draws a dot instead of a line; `label=` is the name shown in the legend, and text between dollar signs is typeset as mathematics. The remaining lines label the axes, set the title and draw the legend.

```python
save_figure(fig, "parabola_tangent",
            "The parabola $y = x^2$ (solid line), its tangent line $y = 2x - 1$ at "
            "the point $(1, 1)$ (dashed line) and the point itself (black dot), for "
            "$x$ from $-1$ to $3$; horizontal axis $x$, vertical axis $y$ (pure "
            "numbers, no units). The line touches the parabola only at $(1, 1)$ "
            "and lies below it everywhere else; its slope $2$ is the derivative "
            "$2x$ of $x^2$ at $x = 1$.")
check(gap.min() >= 0.0 and abs(gap[200]) < 1e-15,
      "the tangent line lies below the parabola and touches it at x = 1")
```

`save_figure` saves the figure as `00a_1_parabola_tangent.png` with its caption (Python joins the strings written next to each other into one) and prints Figure 00a.1 saved as ... in Out [8]. The check uses `gap.min()`, the smallest of the 401 numbers of `gap`, which must not be negative, and `gap[200]`, the entry number 200 counted from 0, which belongs to $x = -1 + 200 \cdot 0.01 = 1$ and must be 0 up to $10^{-15}$. What Figure 00a.1 shows: the dashed line touches the solid parabola at the black dot and stays below it on both sides, as derived in Section 0.10.

**In [9], the two exponentials.**

```python
t = np.linspace(-2.0, 2.0, 401)  # 401 equally spaced numbers from -2 to 2
growing = np.exp(t)  # e^t
shrinking = np.exp(-t)  # e^(-t)
product = growing * shrinking  # e^t e^(-t), which is 1
```

`np.exp` is the exponential function, applied to every number of the array. The product of two arrays is taken number by number.

```python
fig, ax = plt.subplots()
ax.plot(t, growing, label="$e^{t}$ (grows)")
ax.plot(t, shrinking, "--", label="$e^{-t}$ (shrinks)")
ax.plot(t, product, ":", color="black", label="the product $e^{t} e^{-t} = 1$")
ax.set_xlabel("$t$")
ax.set_ylabel("value")
ax.set_title("A growing and a shrinking exponential")
ax.legend()
```

The plotting lines work as in In [8]: a solid line for $e^{t}$, a dashed one (two hyphens) for $e^{-t}$, and a dotted black one (`":"`) for their product.

```python
save_figure(fig, "growth_and_decay",
            "The growing exponential $e^{t}$ (solid line), the shrinking "
            "exponential $e^{-t}$ (dashed line) and their product (dotted line) "
            "for $t$ from $-2$ to $2$; horizontal axis $t$, vertical axis the value "
            "(pure numbers, no units). Each of the two curves is the mirror image "
            "of the other in the vertical axis $t = 0$, and their product is "
            "exactly $1$ at every $t$: what one factor gains, the other loses.")
check(np.max(np.abs(product - 1.0)) < 1e-14, "e^t times e^(-t) is 1 at every t")
```

`save_figure` saves the figure as `00a_2_growth_and_decay.png`. The check computes `np.abs(product - 1.0)`, the distance of each of the 401 products from 1, takes the largest with `np.max`, and requires it to be below $10^{-14}$: up to rounding, $e^{t} e^{-t} = 1$. What Figure 00a.2 shows: the two curves are mirror images of each other in the line $t = 0$, and the dotted product stays flat at 1.

**In [10], the last check.**

```python
for name in ("00a_1_parabola_tangent.png", "00a_2_growth_and_decay.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

The loop runs over a **tuple** (a list in round brackets that cannot be changed) of the two figure names and checks that each file exists. `all_checks_passed()` prints the last line, ALL 9 CHECKS PASSED (notebook 00a): one check each in In [2], In [3], In [5], In [6], In [7], In [8] and In [9], and two in In [10].
