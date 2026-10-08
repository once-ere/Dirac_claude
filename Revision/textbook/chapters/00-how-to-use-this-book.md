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
- **T2** (both fields): $\Gamma$ combined with the reflection of one space-like direction (an element of the group Pin(4,4)) turns $(m, \lambda)$ into $(-m, \lambda)$, with the same self-coupling; in the author's universe the reflection is the Z2 mirror across the edge $z = \pi/2$ of the hidden direction (a choice of boundary condition, which is ASSUMED, not derived), and the energy-momentum tensor of the image is equal to that of the original (reflected across the mirror), not opposite to it;
- **Q** (dirac16complex): the quantum reading of T1; the image field carries the indefinite (Krein) metric $-B$ and is the same quantum system written in other variables, and there is no cancellation between two universes that are quantised independently of each other;
- **T3** (dirac16complex, the Kohn-Sham level, with the ASSUMED Z2 mirror and the correspondingly transformed boundary conditions): every self-consistent Kohn-Sham universe with $(M, \lambda)$ has a partner with $(-M, \lambda)$, and the two have equal energies and equal energy-momentum tensors;
- **C1** (a consequence of T1): a T1 pair taken as the complete classical source of the author's metric is a zero source, and Einstein's equations then have no solution for $H > 0$.

These are PROVED, each by two independent verifiers, whose reports are:

- for T1, T2 and Q: `Revision/pairing/reports/wolfram-pairing.json` and `Revision/pairing/reports/python-pairing.json`;
- for T3: `Revision/pairing/kohn_sham/reports/wolfram-t3.json` and `Revision/pairing/kohn_sham/reports/python-t3.json`;
- for C1: T1 together with the check `einstein_no_vacuum_solution` of `Revision/field_equations_a4/reports/wolfram-a4-report.json` and the check `einstein_no_vacuum` of `Revision/field_equations_a4/reports/python-a4-report.json`.

They are exact **maps between solution sets**: if one solution exists, its partner exists too. What is NOT proved is that any universe is **created**, in pairs or otherwise: no creation process, no rate, no probability amplitude and no dynamics of a big bang follows from these equations, and a single universe of mass $+m$ is an equally valid solution without its partner. The pairing record says so itself: the report `Revision/pairing/reports/python-pairing.json` holds, under its key `not_established`, a list of twelve things that the theorems do not establish, and Notebook 00c prints all twelve. Chapters 18 to 20 give the complete proofs and the complete list. In the honesty ledger (Section 0.18) the statement "the big bang creates universes in pairs" is therefore labelled OPEN, with the note "not proved".

**Matter and antimatter.** The universe we observe contains matter but almost no antimatter. In 1967 Sakharov showed that an excess of matter can grow from an equal start only if three conditions hold: there are processes that change the number of baryons (the particles of ordinary matter, such as the proton); the symmetries called C and CP are violated; and the universe departs from thermal equilibrium. Chapter 21 explains all of this from zero, with the measured size of the excess (the baryon-to-photon ratio). What this theory proves is: the charge $Q$ of each field is exactly conserved (an exact U(1) symmetry), so no net charge can be generated inside one universe; the discrete symmetries of the theory are derived exactly (Chapter 21), among them its two charge conjugations, which are matrices, $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$; and a T1 partner (mass $-m$, self-coupling $-\lambda$) carries the opposite charge, so a T1 pair $\{+m, -m\}$ has total charge zero as classical fields (for two universes that are quantised independently of each other there is no such cancellation; this is part of Q). The idea that our universe has a partner of opposite charge (an "anti-universe") belongs to a class of ideas of which one published example is Boyle, Finn and Turok, Phys. Rev. Lett. 121, 251301 (2018). The theory as built does NOT solve the matter-antimatter problem: it has no baryons, no process that changes the number of baryons, no violation of CP, and no computation of a departure from equilibrium. To solve it, the theory would need all of these, and a computation of the excess that agrees with the measured one. That our universe actually has such a partner is a HYPOTHESIS, and every scenario built on it is labelled HYPOTHESIS.

**Charge conjugation is a matrix.** The author's gamma matrices are real (they contain only real numbers). For a field whose components are real numbers, plain complex conjugation changes nothing at all: it is the identity map, and it cannot be what charge conjugation means here. The charge conjugations of the theory are two matrices, derived in Chapter 5 and Chapter 21: $\mathcal{C}_+ = C$, which keeps the mass, and $\mathcal{C}_- = \Gamma C$, which reverses it. For a real commuting field the charge current $J$ is zero and $\mathcal{C}_+$ acts as the identity (a real field is its own conjugate); for real fields the map between matter and antimatter is the real matrix $\Gamma$ together with the reversal of the mass, which is T1. (PROVED: `Revision/lead_checks/reports/charge-conjugation-and-u1.json`, the checks `charge_conjugation_matrix_plus`, `charge_conjugation_matrix_minus` and `real_fields_charge_conjugation`; Notebook 00c opens this report and prints three of its details.)

**A prescribed background.** The Kohn-Sham chapters let $a_4$ grow in proportion to the time, $a_4 = A H x_4$. This history is ASSUMED, a **prescribed background**: the computed Kohn-Sham states cannot be its source in the field equations (`Revision/field_equations_a4/reports/ks-source-conditions.json`).

### 0.3 The five labels of every statement

Every statement of the book that matters carries one of five labels, so that you always know how much it is worth:

| label | meaning |
| --- | --- |
| PROVED | exact; the book gives the complete proof and, where the Revision record contains an exact computer check of the statement, names it (the report file and the name of the check) |
| COMPUTED | a number from a numerical computation, with its measured uncertainty and the file that holds it |
| ASSUMED | a starting point that the book does not derive (a convention, a physical input or an approximation); everything that depends on it says so |
| HYPOTHESIS | an idea that is stated and examined but not established |
| OPEN | a question that neither the Revision record nor this book answers |

A statement can be PROVED in three ways. (1) A statement about finitely many definite objects, such as "these eight matrices of whole numbers satisfy these 64 equations", is proved by an exact computation of every case. (2) A statement in which the computer keeps the unknown quantities as symbols, such as "for every function $a_4$ the determinant of the metric is $\cos^2 z$", is proved by an exact symbolic computation, which holds for every value of the symbols, like a derivation by hand. (3) A statement about infinitely many cases that the computer cannot hold as symbols, such as "in every gravitational field", is proved by a general derivation in the book; an exact check at a few test points then confirms the derivation (and would catch many errors), but it is not the proof.

Examples from this chapter. "The determinant of the author's metric is $\cos^2 z$" is PROVED (way 2; Section 0.14). "The ground-state energies of the canonical and the refined run of the Revision record's Kohn-Sham solver differ by at most $1.901 \times 10^{-12}$ (relative)" is COMPUTED (`Revision/kohn_sham/reports/ks-rust-determinism.json`, check `refined_ground_energies`; Notebook 00d reads it, Section 0.22). "The Z2 mirror at the edge of the hidden direction" is ASSUMED. "Our universe has a partner of opposite charge" is a HYPOTHESIS. "The big bang creates universes in pairs" was proposed by the author as a hypothesis; as a question of this book it is OPEN, and the ledger says why: it is not proved.

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

**Build.** nbkit inserts the run instructions and the set-up cell, executes the notebook with the kernel python3 in the folder `Revision/textbook/notebooks`, with the hash seed `PYTHONHASHSEED` set to 0 (Section 0.22 explains what it is), checks every output against the rules of the book, removes everything that differs from run to run without meaning anything (time stamps and timing data), and stores the executed notebook, its figures and its captions. A build ends with the check described next, and only when that check passes does it write the provenance file.

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

### 0.14 The eight directions and the author's metric

Every later chapter lives in the author's universe, so we take a first look at it now, with nothing but school algebra. Chapter 3 returns to it with the full mathematics of curved space; here we need only four facts: which directions are like space and which are like time, how lengths along each direction change as the time runs, why ordinary space inflates while the extra times deflate, and why the volume does not change.

**Steps and their sizes.** On a flat sheet of paper with the coordinates $x$ and $y$, a small step $dx$ to the right and $dy$ upwards has a length $ds$ with $ds^2 = dx^2 + dy^2$: this is the theorem of Pythagoras for the right-angled triangle with the sides $dx$ and $dy$. In ordinary space with the coordinates $x_1$, $x_2$, $x_3$ the same theorem, used twice, gives $ds^2 = dx_1^2 + dx_2^2 + dx_3^2$. A **metric** is a rule of this kind: it turns the small steps $dx_1, dx_2, \ldots, dx_8$ along the eight coordinates into one number $ds^2$, the squared size of the step. The rules of this book are **diagonal**: each squared step is multiplied by its own number $g_{ii}$, called the entry of the metric for the direction $x_i$, and the results are added:

$$
ds^2 = g_{11}\, dx_1^2 + g_{22}\, dx_2^2 + \cdots + g_{88}\, dx_8^2 .
$$

The entries $g_{11}, \ldots, g_{88}$ may change from place to place and from time to time; that is what can make a space curved (Chapter 3).

**Space-like and time-like.** In 1905 Einstein found that a step in space and time must be measured with a minus sign in front of the time step: in units in which the speed of light is 1, the squared size of a step is $dx_1^2 + dx_2^2 + dx_3^2 - dx_4^2$ when $x_4$ is the time. A direction whose entry is positive is called **space-like** (a step along it is measured like a distance); a direction whose entry is negative is called **time-like** (a step along it is measured like a duration). The list of the signs of the eight directions is called $\eta$ (the Greek letter eta), and the numbers of plus and minus signs form the **signature**. In the author's universe

$$
\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)
$$

in the order $x_1, \ldots, x_8$: the four directions $x_1$, $x_2$, $x_3$ and $x_8$ are space-like, the four directions $x_4$, $x_5$, $x_6$ and $x_7$ are time-like, and the signature is (4,4). Here $\mathrm{diag}(\ldots)$ is the square table of numbers (a **matrix**, Chapter 1) that has the listed numbers on its diagonal, from the top left to the bottom right, and zeros everywhere else.

**The author's metric.** The author gave the metric of his primordial universe as an $8 \times 8$ diagonal matrix (`Revision/SPEC.md`, section 1). Its eight entries are

$$
g_{11} = g_{22} = g_{33} = e^{2 a_4} \sin^{1/3} z , \qquad g_{44} = -1 ,
$$

$$
g_{55} = g_{66} = g_{77} = -e^{-2 a_4} \sin^{1/3} z , \qquad g_{88} = \cot^2 z ,
$$

where $z = 6 H x_8$, $H > 0$ is a constant of the author, and $a_4$ is a function of the time $x_4$ alone, the **metric function** (its own field equations are the subject of Chapter 12). The hidden coordinate is restricted so that $0 < z < \pi/2$; this interval is called the **patch**. Here $\sin^{1/3} z$ means $(\sin z)^{1/3}$, the cube root of $\sin z$, and $\cot z = \cos z / \sin z$. Status: ASSUMED. The metric is the author's input; the book does not derive it, and Chapter 12 asks which source it would need.

We now derive the four facts. Each line of a derivation is followed, in brackets, by the rule that produced it from the line before.

**Fact 1: the signs.** Take any point of the patch, $0 < z < \pi/2$, and any value of $a_4$.

$$
\sin z > 0 \quad \text{and} \quad \cos z > 0
$$

(the sine and the cosine of an angle between 0 and a right angle are positive),

$$
\sin^{1/3} z > 0
$$

(the cube root of a positive number is positive),

$$
e^{2 a_4} > 0 \quad \text{and} \quad e^{-2 a_4} > 0
$$

(the exponential function $e^{u}$ is positive for every number $u$),

$$
g_{11} = e^{2 a_4} \sin^{1/3} z > 0 \quad \text{and} \quad g_{55} = -e^{-2 a_4} \sin^{1/3} z < 0
$$

(a product of two positive numbers is positive, and a positive number with a minus sign in front is negative),

$$
\cot z = \frac{\cos z}{\sin z} > 0 , \quad \text{so} \quad g_{88} = \cot^2 z > 0
$$

(a quotient of two positive numbers is positive, and the square of a nonzero number is positive). Together with $g_{44} = -1 < 0$ the signs of the eight entries are $(+, +, +, -, -, -, -, +)$, exactly the list $\eta$, at every point of the patch and for every value of $a_4$. Status: PROVED (by the school algebra above). The Revision record states the signs in the file `Revision/algebra/gammas.json`, and its Wolfram verifier checks them (`Revision/algebra/reports/wolfram-algebra.json`, check `eta_in_author_order`); Notebook 00b confirms the signs of the eight entries at 4819 points (COMPUTED).

**Fact 2: the length factors.** A step $dx_1$ along $x_1$ alone (all other steps zero) has $ds^2 = g_{11}\, dx_1^2$, so its size is $|ds| = \sqrt{|g_{11}|}\, |dx_1|$. The number $f_i = \sqrt{|g_{ii}|}$ is called the **length factor** (or scale factor) of the direction $x_i$: it converts a step of the coordinate into a length. For $x_1$:

$$
f_1 = \sqrt{e^{2 a_4} \sin^{1/3} z}
$$

(the definition, with $|g_{11}| = g_{11}$ because $g_{11} > 0$ by Fact 1),

$$
f_1 = \sqrt{e^{2 a_4}}\, \sqrt{\sin^{1/3} z}
$$

(the square root of a product of two nonnegative numbers is the product of their square roots),

$$
f_1 = e^{a_4} \sin^{1/6} z
$$

(first, $\sqrt{e^{2 a_4}} = e^{a_4}$, because $e^{a_4}$ is positive and its square is $e^{a_4} e^{a_4} = e^{2 a_4}$; second, $\sqrt{u^{1/3}} = (u^{1/3})^{1/2} = u^{1/6}$ by the power rule $(u^p)^q = u^{pq}$). The same three lines give $f_2 = f_3 = e^{a_4} \sin^{1/6} z$. For the extra times, $|g_{55}| = e^{-2 a_4} \sin^{1/3} z$ (a minus sign in front of a positive number is removed by the absolute value), and the same steps give

$$
f_5 = f_6 = f_7 = e^{-a_4} \sin^{1/6} z .
$$

Finally $f_4 = \sqrt{|-1|} = 1$, and $f_8 = \sqrt{\cot^2 z} = |\cot z| = \cot z$ (the square root of a square is the absolute value, and $\cot z > 0$ on the patch). Status: PROVED.

**Fact 3: ordinary space inflates, the extra times deflate.** Fix the hidden coordinate, so that $\sin^{1/6} z$ is a fixed positive number. When $a_4$ grows, $e^{a_4}$ grows and $e^{-a_4} = 1/e^{a_4}$ shrinks (Section 0.10): the length factors of $x_1$, $x_2$, $x_3$ grow (ordinary space **inflates**) and those of $x_5$, $x_6$, $x_7$ shrink (the extra times **deflate**). The simplest history is $a_4 = A H x_4$ with a positive constant $A$. It is the history that the Kohn-Sham chapters use, where it is ASSUMED as a **prescribed background** (`Revision/field_equations_a4/reports/ks-source-conditions.json`, check `ks_history_is_a_prescribed_background`), and Chapter 12 shows that the sign of $A$ is a choice: with $-A$ in place of $A$ the roles of growth and shrinking are exchanged. Along this history

$$
f_5 = e^{-A H x_4} \sin^{1/6} z
$$

(substitution of $a_4 = A H x_4$ into Fact 2),

$$
\frac{d f_5}{d x_4} = -A H\, e^{-A H x_4} \sin^{1/6} z
$$

(the chain rule: the derivative of $e^{u}$ with respect to $x_4$ is $e^{u}\, du/dx_4$, here with $u = -A H x_4$ and $du/dx_4 = -A H$; the constant factor $\sin^{1/6} z$ stays in front),

$$
\frac{d f_5}{d x_4} = -A H\, f_5
$$

(the previous line contains $f_5$ itself, by the first line). A quantity whose rate of change is a fixed negative multiple of itself decreases **exponentially**: in every interval of time of length $1/(AH)$ it is multiplied by the same factor $e^{-1} = 0.3679$. The same steps give $d f_1 / d x_4 = +A H\, f_1$: ordinary space inflates exponentially. Status: PROVED (for the ASSUMED history). In every history the product of an inflating and a deflating factor is constant in time:

$$
f_1 f_5 = e^{a_4} e^{-a_4} \sin^{1/6} z \, \sin^{1/6} z = \sin^{1/3} z
$$

(the law of exponents $e^{u} e^{v} = e^{u + v}$ gives $e^{a_4 - a_4} = e^{0} = 1$, and $u^{1/6} u^{1/6} = u^{1/3}$).

**Fact 4: the determinant and the volume factor.** The **determinant** is one number computed from a square matrix (Chapter 1 defines it in general); for a diagonal matrix it is the product of the diagonal entries (a fact proved in Chapter 1 and used here). For the author's metric:

$$
\det g = \left(e^{2 a_4} \sin^{1/3} z\right)^3 \cdot (-1) \cdot \left(-e^{-2 a_4} \sin^{1/3} z\right)^3 \cdot \cot^2 z
$$

(the product of the eight entries, the three equal entries of ordinary space and the three equal entries of the extra times collected as cubes),

$$
\left(e^{2 a_4} \sin^{1/3} z\right)^3 = e^{6 a_4} \sin z
$$

(the rule $(uv)^3 = u^3 v^3$, then $(e^{2 a_4})^3 = e^{6 a_4}$ and $(\sin^{1/3} z)^3 = \sin z$, both by the power rule $(u^p)^q = u^{pq}$),

$$
\left(-e^{-2 a_4} \sin^{1/3} z\right)^3 = (-1)^3\, e^{-6 a_4} \sin z = -e^{-6 a_4} \sin z
$$

(the same rules, and $(-1)^3 = -1$),

$$
\det g = e^{6 a_4} \sin z \cdot (-1) \cdot \left(-e^{-6 a_4} \sin z\right) \cdot \cot^2 z
$$

(substitution of the two cubes into the first line),

$$
\det g = e^{6 a_4} e^{-6 a_4} \cdot (-1)(-1) \cdot \sin^2 z \cot^2 z
$$

(the factors of a product may be taken in any order),

$$
\det g = \sin^2 z \cot^2 z
$$

($e^{6 a_4} e^{-6 a_4} = e^{0} = 1$ by the law of exponents, and $(-1)(-1) = 1$),

$$
\det g = \sin^2 z \cdot \frac{\cos^2 z}{\sin^2 z} = \cos^2 z
$$

(the definition $\cot z = \cos z / \sin z$, then cancelling $\sin^2 z$, which is not zero on the patch). The determinant does not contain $a_4$. Its square root is

$$
\sqrt{|\det g|} = \sqrt{\cos^2 z} = \cos z
$$

(the determinant is positive, and the square root of a square is the absolute value, $|\cos z| = \cos z$ on the patch). This number is the **volume factor**: a small box with the coordinate sides $dx_1, \ldots, dx_8$ has the sides $f_1\, dx_1, \ldots, f_8\, dx_8$ in length, so its volume is $f_1 f_2 \cdots f_8 \, dx_1 \cdots dx_8$, and the product of the length factors is $f_1 \cdots f_8 = \sqrt{|g_{11}| \cdots |g_{88}|} = \sqrt{|\det g|}$ (a product of square roots is the square root of the product). Written with the length factors of Fact 2, $f_1 f_2 f_3 f_5 f_6 f_7 = (f_1 f_5)^3 = \sin z$ by Fact 3, and $f_4 f_8 = \cot z$, so the volume factor is $\sin z \cot z = \cos z$ once more. The inflation of the three directions of ordinary space and the deflation of the three extra times cancel exactly in the volume. Status: PROVED, by the derivation above and by three exact symbolic computations of the Revision record that hold for every function $a_4$:

- the Wolfram verifier of the field theory, in its report `Revision/theory/reports/wolfram-field-theory.json`, check `sqrt_det_g_is_cos_z`;
- the Python verifier of the field theory, in its report `Revision/theory/reports/python-field-theory.json`, check `sqrt_det_g_equals_cos_z`;
- the Wolfram verifier of the field equations for $a_4$, in its report `Revision/field_equations_a4/reports/wolfram-a4-report.json`, check `sqrt_abs_det_g_is_cos_z`.

**Numbers to check by hand.** At $z = \pi/4$ we have $\sin(\pi/4) = 1/\sqrt{2} = 2^{-1/2}$, so $\sin^{1/6}(\pi/4) = 2^{-1/12} = 0.9439$, and $\cot(\pi/4) = 1$, $\cos(\pi/4) = 0.7071$. With $a_4 = 0.5$ the factor of ordinary space is $e^{0.5} \cdot 0.9439 = 1.6487 \cdot 0.9439 = 1.5562$ and that of an extra time $e^{-0.5} \cdot 0.9439 = 0.6065 \cdot 0.9439 = 0.5725$; with $a_4 = 1$ they are $2.7183 \cdot 0.9439 = 2.5657$ and $0.3679 \cdot 0.9439 = 0.3472$. In every case the product of the eight factors is $\cos(\pi/4) = 0.7071$. Notebook 00b prints exactly these numbers.

**Example: the eight directions in numbers and pictures.** Notebook 00b reads the names and the signs of the eight coordinates from the Revision record, writes the author's metric with the package sympy and compares its eight entries, one by one, with the formulas that the Revision verifier recorded, checks the signs of the entries at 4819 points, computes the determinant exactly, prints the table of the length factors above, and draws four figures: the signs as a picture, the growing and the shrinking factor, the eight length factors as bars, and the volume factor. It checks every fact of this section and ends with ALL 14 CHECKS PASSED (notebook 00b).

<!-- NOTEBOOK 00b -->

### 0.17 Line-by-line walk-through of Notebook 00b

The notebook has ten code cells, In [1] to In [10]. This section explains every line of each of them.

**In [1], the set-up cell.** It is the set-up cell of Notebook 00a, word for word, except for two things: its comment lines hold the run instructions of Notebook 00b (Section 0.15), and the line `NOTEBOOK_ID = "00b"` names this notebook, so that its figures are called `00b_1_eta_heat_map.png` and so on and its captions file is `Revision/textbook/figures/00b.captions.json`. Every line of its code is explained in Section 0.13. It prints one line, Set-up of notebook 00b complete: repository folder found, helpers defined.

**In [2], the eight coordinates in the Revision record.**

```python
import sys  # sys.stdout is the channel through which the notebook prints

import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols
```

The module `sys` of Python gives access to the running Python itself; the notebook needs its `sys.stdout`, the channel through which `print` writes. numpy and sympy are loaded under their usual short names `np` and `sp`, as in Notebook 00a.

```python
GAMMAS_FILE = "Revision/algebra/gammas.json"  # coordinates, signs and gammas
gammas_record = json.loads(repository_file(GAMMAS_FILE).read_text(encoding="utf-8"))
coordinates = gammas_record["coordinates"]  # the names x1 ... x8, in order
eta = gammas_record["eta"]  # the sign of each direction: +1 or -1
```

The first line names the record file. In the second line, `repository_file(GAMMAS_FILE)` is its full path (Section 0.13), `.read_text(encoding="utf-8")` reads the whole file as one string, and `json.loads` turns that JSON text into Python's dictionaries and lists. The file is one big dictionary; `gammas_record["coordinates"]` takes the value stored under the key `coordinates`, the list of the eight names `["x1", ..., "x8"]`, and `gammas_record["eta"]` the list of the eight signs `[1, 1, 1, -1, -1, -1, -1, 1]`. (The same file also holds the gamma matrices of Chapter 4.)

```python
ROLES = {  # the role of each coordinate in the author's universe
    "x1": "ordinary space (inflates)",
    "x2": "ordinary space (inflates)",
    "x3": "ordinary space (inflates)",
    "x4": "the time",
    "x5": "extra time (deflates)",
    "x6": "extra time (deflates)",
    "x7": "extra time (deflates)",
    "x8": "hidden direction of space",
}
```

A dictionary from each coordinate name to a short description of its role, written by the author of the notebook from Section 0.5 (the record holds the names and the signs, not the roles).

```python
say("coordinate  sign  kind        role")
for name, sign in zip(coordinates, eta):
    kind = "space-like" if sign > 0 else "time-like"
    # {sign:+d} writes the sign of a whole number (+1 or -1) in front of it.
    say(f"{name:10}  {sign:+d}    {kind:10}  {ROLES[name]}")
```

The first line prints the header of a table. `zip(coordinates, eta)` pairs the two lists entry by entry: `("x1", 1)`, `("x2", 1)`, and so on; the loop names the two parts of each pair `name` and `sign`. The **conditional expression** `"space-like" if sign > 0 else "time-like"` has the first value when the condition holds and the second otherwise. In the f-string, `{name:10}` pads the name to 10 characters, `{sign:+d}` writes the whole number with its sign (`+1` or `-1`), `{kind:10}` pads the kind, and `{ROLES[name]}` looks up the role. The eight lines of the table are the first eight lines of Out [2].

```python
def recorded_check(path, name):
    """The verdict (PASS or FAIL) and the detail text that the Revision report
    path recorded for its check called name."""
    data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for entry in data["checks"]:  # every check of the report, one after the other
        if entry["name"] == name:
            return entry["verdict"].upper(), entry["detail"]
    raise KeyError(f"{path} has no check {name}")
```

A function that looks up one named check in a report of the Revision record. It reads the report as in the lines above; `data["checks"]` is the list of its checks, each a dictionary with the keys `name`, `verdict` and `detail`. The loop compares each name with the wanted one; at the first match, `return` hands back two values at once, the verdict written in capitals (`.upper()`, because some reports write `pass` in small letters) and the detail text. If no check has that name, `raise KeyError(...)` stops the notebook with a message that names the report and the check.

```python
def check_reproduces(condition, name, record):
    """check(condition, name, record=record), after sending the waiting output."""
    sys.stdout.flush()  # send every printed line that is still waiting
    check(condition, name, record=record)
```

The helper for a check that reproduces a Revision record. Python collects printed text and sends it to Jupyter in pieces; `sys.stdout.flush()` sends everything that is still waiting, so that the PASS line and the line reproduces ... that `check` prints just after it arrive together, in one piece of output, and the book's tools read them as one. Then it calls the helper `check` of the set-up cell with the record.

```python
ALGEBRA_REPORT = "Revision/algebra/reports/wolfram-algebra.json"
verdict, detail = recorded_check(ALGEBRA_REPORT, "eta_in_author_order")
say(f"The Wolfram verifier recorded for eta_in_author_order: {verdict}")
```

These lines read what the Wolfram verifier of the algebra recorded for its check `eta_in_author_order` (that the signs are $(+, +, +, -, -, -, -, +)$ in the order $x_1, \ldots, x_8$). The two returned values are named `verdict` and `detail`, and the verdict is printed: PASS (Out [2], ninth line).

```python
check(coordinates == ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"],
      "the record names the eight coordinates x1 to x8 in this order")
check(eta == [1, 1, 1, -1, -1, -1, -1, 1],
      "the record gives the signs (+,+,+,-,-,-,-,+) in the order x1..x8")
check(eta.count(1) == 4 and eta.count(-1) == 4,
      "four space-like and four time-like directions: the signature is (4,4)")
check(verdict == "PASS",
      "the Wolfram verifier recorded PASS for these signs (eta_in_author_order)")
```

Four checks. Two lists are equal (`==`) when they have the same entries in the same order; so the first check confirms the names and their order, the second the signs. `eta.count(1)` counts the entries equal to 1; the third check requires four of each sign, the signature (4,4). The fourth requires the recorded verdict PASS. The four PASS lines end Out [2].

**In [3], the signs as a heat map.**

```python
from matplotlib.colors import ListedColormap  # a colour map made of a few colours
from matplotlib.patches import Patch  # a coloured square for the legend
```

Two tools of matplotlib: a **colour map** made of a short list of colours, and a coloured square for a legend.

```python
eta_matrix = np.diag(eta)  # 8 x 8: the signs on the diagonal, 0 elsewhere
BLUE, GREY, RED = "#2a78d6", "#f0efec", "#e34948"
colour_map = ListedColormap([BLUE, GREY, RED])  # three colours for -1, 0, +1
```

`np.diag(eta)` makes the $8 \times 8$ matrix $\eta$ of Section 0.14 from the list of its diagonal entries. The colours are written as **hexadecimal colour codes**: after `#`, three pairs of hexadecimal digits give the amounts of red, green and blue (from 00, none, to ff, 255). The colour map has three colours, in the order in which they are used for small, middle and large numbers.

```python
fig, ax = plt.subplots(figsize=(6.4, 5.4))
# vmin and vmax split the numbers into three bands: -1, 0 and +1.
ax.imshow(eta_matrix, cmap=colour_map, vmin=-1.5, vmax=1.5)
```

A figure 6.4 inches wide and 5.4 inches high. `ax.imshow` draws the matrix as a grid of coloured squares, row 1 at the top. The colour map divides the interval from `vmin` $= -1.5$ to `vmax` $= 1.5$ into three equal bands, $[-1.5, -0.5]$, $[-0.5, 0.5]$ and $[0.5, 1.5]$, and gives them the three colours in order: $-1$ is blue, $0$ grey and $+1$ red.

```python
for row in range(8):
    for column in range(8):
        value = int(eta_matrix[row, column])
        text = "0" if value == 0 else f"{value:+d}"
        colour = "#52514e" if value == 0 else "white"  # readable on each colour
        ax.text(column, row, text, ha="center", va="center", color=colour,
                fontsize=9)
```

Two loops, one inside the other, visit all 64 squares; `range(8)` gives the numbers 0 to 7. `eta_matrix[row, column]` is the entry in that row and column (counted from 0), turned into a whole number with `int`. The text is `0`, or the entry with its sign. Dark grey letters are used on the light grey squares and white letters on the coloured ones. `ax.text(column, row, ...)` writes the text centred (`ha` and `va`: horizontal and vertical alignment) in the square; the horizontal position comes first, so the column comes before the row.

```python
ax.set_xticks(range(8), labels=coordinates)  # label the columns x1 ... x8
ax.set_yticks(range(8), labels=coordinates)  # label the rows x1 ... x8
ax.grid(False)  # no grid lines across the squares
ax.set_title(r"The signs $\eta$ of the eight directions (signature (4,4))")
legend_squares = [Patch(color=RED, label="+1: space-like"),
                  Patch(color=BLUE, label="-1: time-like"),
                  Patch(color=GREY, label="0: off the diagonal")]
ax.legend(handles=legend_squares, loc="upper left", bbox_to_anchor=(1.02, 1.0))
```

The columns and rows are labelled with the coordinate names, the grid of the set-up cell is switched off for this picture, and the title is set. A string written with `r` in front (a **raw string**) keeps every backslash as it is, so that matplotlib receives the mathematics `$\eta$`. The legend is made of three coloured squares; `bbox_to_anchor=(1.02, 1.0)` puts its upper left corner just to the right of the picture, so that it covers no square.

```python
save_figure(fig, "eta_heat_map",
            r"The signs of the author's eight directions drawn as a heat map: the "
            r"8 by 8 diagonal matrix $\eta$ with the sign of each coordinate on its "
            r"diagonal and 0 everywhere else; rows and columns are labelled by the "
            r"coordinates $x_1$ to $x_8$, and the entries are pure numbers. Red "
            r"squares are $+1$ (space-like: $x_1$, $x_2$, $x_3$, $x_8$), blue "
            r"squares $-1$ (time-like: the time $x_4$ and the extra times $x_5$, "
            r"$x_6$, $x_7$), grey squares 0. Four entries are $+1$ and four are "
            r"$-1$: the signature is (4,4).")
```

The figure is saved as `00b_1_eta_heat_map.png` with this caption (the raw strings written next to each other are joined into one) and shown; Out [3] is the figure and the line Figure 00b.1 saved as .... What Figure 00b.1 shows: the diagonal of the matrix, from the top left, has three red squares, four blue squares and a last red square, the pattern $(+, +, +, -, -, -, -, +)$ of Fact 1 of Section 0.14.

**In [4], the author's metric written with sympy.**

```python
x4, x8, H = sp.symbols("x4 x8 H", positive=True)  # time, hidden coordinate, H
a4 = sp.Function("a4")(x4)  # the metric function a4, an unknown function of x4
z = 6 * H * x8  # the combination z = 6 H x8
third = sp.Rational(1, 3)  # the exact fraction 1/3
```

`sp.symbols` makes three symbols at once; `positive=True` tells sympy that they stand for positive numbers, which lets it simplify more. `sp.Function("a4")` makes an unknown function called `a4`, and `(x4)` makes it a function of $x_4$: sympy knows nothing about it except that it depends on $x_4$, so every result below holds for every history $a_4(x_4)$. `z` is the expression $6 H x_8$. `sp.Rational(1, 3)` is the exact fraction $1/3$; the decimal number 0.3333 would be rounded and not exact.

```python
grow = sp.exp(2 * a4) * sp.sin(z) ** third  # e^(2 a4) sin^(1/3) z
shrink = sp.exp(-2 * a4) * sp.sin(z) ** third  # e^(-2 a4) sin^(1/3) z
g = sp.diag(grow, grow, grow, -1, -shrink, -shrink, -shrink, sp.cot(z) ** 2)
```

The two kinds of entry of the metric, and the diagonal $8 \times 8$ matrix `g` with the eight entries of Section 0.14 in the order $x_1, \ldots, x_8$.

```python
THEORY_REPORT = "Revision/theory/reports/python-field-theory.json"
verdict, detail = recorded_check(THEORY_REPORT, "metric_from_vielbein_equals_SPEC")
formulas = detail.split("exactly: ", 1)[1].split("; ")  # the 8 texts "g_.. = ..."
```

The Python verifier of the field theory recorded, in the detail of its check `metric_from_vielbein_equals_SPEC`, the eight entries of the metric that it rebuilt from its own construction (the vielbein of Chapter 6). The detail is a sentence that ends with `exactly:` followed by the eight formulas separated by a semicolon and a blank. `detail.split("exactly: ", 1)` cuts the text at the first `exactly: ` into two pieces; `[1]` keeps the second piece (Python counts from 0), and `.split("; ")` cuts it into the list of the eight texts such as `g_x1x1 = exp(2*a4(x4))*sin(6*H*x8)**(1/3)`.

```python
# How sympify must read the letters of the formulas: a4 is a function, x4, x8 and
# H are our symbols.
letters = {"a4": sp.Function("a4"), "x4": x4, "x8": x8, "H": H}
labels = []  # the names g_x1x1, g_x2x2, ... in the order of the record
different = []  # the entries whose difference from ours is not zero
```

A dictionary that tells sympy what each name in the recorded formulas means, and two empty lists to be filled by the loop.

```python
for k, text in enumerate(formulas):
    label, formula = text.split(" = ")  # "g_x1x1" and its formula
    labels.append(label)
    recorded = sp.sympify(formula, locals=letters)  # the text as a sympy formula
    if sp.simplify(recorded - g[k, k]) != 0:
        different.append(label)
    say(f"recorded {label} = {formula}")
```

`enumerate(formulas)` gives each text together with its position `k` = 0, 1, ..., 7. Each text is cut at ` = ` into the name and the formula. `sp.sympify` turns the formula text into a sympy expression, reading the names with the dictionary `letters`. `g[k, k]` is our diagonal entry number `k`; `sp.simplify` simplifies the difference of the two, and if it is not exactly zero, the name is noted in `different`. The loop prints each recorded formula: the eight lines recorded g_x1x1 = ... of Out [4]. (In the printed formulas `**` is the power and `*` the product.)

```python
in_order = [f"g_x{k}x{k}" for k in range(1, 9)]  # g_x1x1, ..., g_x8x8
check_reproduces(
    verdict == "PASS" and labels == in_order and different == [],
    "our eight entries equal the eight entries recorded by the Revision verifier",
    f"{THEORY_REPORT}, check metric_from_vielbein_equals_SPEC")
```

`range(1, 9)` gives 1 to 8, so `in_order` is the list of the names `g_x1x1` to `g_x8x8`. The check requires the recorded verdict PASS, the names in the order $x_1, \ldots, x_8$, and no difference; it names the record it reproduces, and Out [4] ends with the PASS line and the line reproduces Revision/theory/reports/python-field-theory.json, check metric_from_vielbein_equals_SPEC.

**In [5], the signs at 4819 points.**

```python
a, zeta = sp.symbols("a zeta", real=True)  # plain numbers for a4 and for 6 H x8
# x8 = zeta / (6 H) makes 6 H x8 = zeta; sympy cancels the 6 H automatically.
entries = [g[k, k].subs(a4, a).subs(x8, zeta / (6 * H)) for k in range(8)]
# entry_functions[k](a, zeta) computes the entry g_kk with numpy.
entry_functions = [sp.lambdify((a, zeta), entry, "numpy") for entry in entries]
```

Two new symbols, $a$ for a value of the metric function and $\zeta$ (zeta) for a value of $z$. `.subs(a4, a)` replaces the function $a_4(x_4)$ by the plain symbol $a$, and `.subs(x8, zeta / (6 * H))` replaces $x_8$ by $\zeta/(6H)$, so that $z = 6 H x_8$ becomes $\zeta$. The list `entries` holds the eight diagonal entries as formulas in $a$ and $\zeta$ alone. `sp.lambdify((a, zeta), entry, "numpy")` turns a formula into an ordinary Python function of two numbers that computes it with numpy, fast and for whole arrays at once.

```python
# Two arrays of shape 79 x 61: every combination of the 61 values of a and the 79
# values of zeta.
a_grid, zeta_grid = np.meshgrid(np.linspace(-3.0, 3.0, 61),
                                np.linspace(0.01, np.pi / 2 - 0.01, 79))
wrong_signs = 0  # the number of (point, entry) pairs with a wrong sign
```

`np.linspace(-3.0, 3.0, 61)` gives 61 equally spaced values of $a$ from $-3$ to $3$ (steps of 0.1) and the second `np.linspace` 79 values of $\zeta$ inside the patch, from 0.01 to $\pi/2 - 0.01$. `np.meshgrid` makes two tables of 79 rows and 61 columns: in `a_grid` every row is the list of the 61 values of $a$, in `zeta_grid` every column is the list of the 79 values of $\zeta$; read together, the two tables list all $61 \cdot 79 = 4819$ pairs $(a, \zeta)$. The counter of wrong signs starts at 0.

```python
for k in range(8):
    # np.full_like makes an array of the grid's shape; a constant entry such as
    # -1 is then repeated at every point.
    values = np.full_like(a_grid, 1.0) * entry_functions[k](a_grid, zeta_grid)
    wrong_signs += int(np.sum(np.sign(values) != eta[k]))
```

For each entry $k$, `entry_functions[k](a_grid, zeta_grid)` computes the entry at all 4819 points at once. For the constant entry $g_{44} = -1$ the function returns the single number $-1$; multiplying by `np.full_like(a_grid, 1.0)`, a table of the grid's shape filled with 1.0, makes every result a table of 4819 values. `np.sign` gives $+1$ for a positive and $-1$ for a negative number; `!= eta[k]` compares each sign with the recorded sign of the direction, giving a table of `True` (wrong) and `False` (right); `np.sum` counts the `True` entries, and `+=` adds the count to the counter.

```python
report("points of the grid", a_grid.size)
report("(point, entry) pairs with a sign different from eta", wrong_signs)
check_reproduces(
    wrong_signs == 0,
    "every entry has the recorded sign at all 4819 points: (+,+,+,-,-,-,-,+)",
    f"{ALGEBRA_REPORT}, check eta_in_author_order")
```

`a_grid.size` is the number of entries of the table, 4819. Out [5] prints this number, then 0 wrong signs, then the PASS line, which reproduces the Wolfram check `eta_in_author_order`. This is the COMPUTED confirmation of Fact 1 of Section 0.14.

**In [6], the determinant.**

```python
determinant = g.det()  # the product of the eight diagonal entries
determinant_zeta = determinant.subs(x8, zeta / (6 * H))  # 6 H x8 replaced by zeta
say(f"det g = {determinant_zeta}")
say(f"    = {sp.trigsimp(determinant_zeta)}   (zeta stands for z = 6 H x8)")
```

`g.det()` computes the determinant of the sympy matrix exactly; sympy multiplies the eight entries and cancels $e^{6 a_4} e^{-6 a_4}$ by itself, as in Fact 4 of Section 0.14. For a short printout $6 H x_8$ is replaced by $\zeta$; sympy prints `sin(zeta)**2*cot(zeta)**2`, and `sp.trigsimp` (simplification with the rules of trigonometry) turns it into `cos(zeta)**2`. These are the first two lines of Out [6], the last two lines of the derivation of Fact 4.

```python
WOLFRAM_THEORY = "Revision/theory/reports/wolfram-field-theory.json"
verdict, detail = recorded_check(WOLFRAM_THEORY, "sqrt_det_g_is_cos_z")
say(f"The Wolfram verifier recorded for sqrt_det_g_is_cos_z: {verdict}")
check_reproduces(
    sp.simplify(determinant - sp.cos(z) ** 2) == 0 and verdict == "PASS",
    "det g = cos^2 z exactly, so sqrt|det g| = cos z on 0 < z < pi/2",
    f"{WOLFRAM_THEORY}, check sqrt_det_g_is_cos_z")
```

The verdict of the Wolfram verifier for the same statement is read and printed (PASS). The check requires that the difference between our determinant and $\cos^2 z$, written with $x_8$ and $H$, simplifies to exactly 0, and that the Wolfram verifier recorded PASS.

```python
check(sp.diff(determinant, x4) == 0,
      "det g does not depend on the time x4: no a4 in the volume factor")
verdict, detail = recorded_check(
    "Revision/field_equations_a4/reports/wolfram-a4-report.json",
    "metric_is_SPEC_section_1")
check(verdict == "PASS",
      "the field-equation verifier recorded PASS for metric_is_SPEC_section_1")
```

`sp.diff(determinant, x4)` is the derivative of the determinant with respect to the time; it is exactly zero, although the entries contain the unknown function $a_4(x_4)$. The last check reads the verdict that the Wolfram verifier of the field equations for $a_4$ recorded for its check that it used exactly this metric. Out [6] ends with three PASS lines.

**In [7], inflation and deflation.**

```python
a4_values = np.linspace(0.0, 3.0, 301)  # 301 values of a4 from 0 to 3
growing = np.exp(a4_values)  # the 3-space factor e^(a4)
shrinking = np.exp(-a4_values)  # the extra-time factor e^(-a4)
six_factors = growing ** 3 * shrinking ** 3  # three of each: e^(3 a4) e^(-3 a4)
```

301 values of $a_4$ from 0 to 3 in steps of 0.01; at each, the factor $e^{a_4}$ of a direction of ordinary space and the factor $e^{-a_4}$ of an extra time (both divided by the common number $\sin^{1/6} z$), and the product of three of each.

```python
ORANGE = "#eb6834"
fig, ax = plt.subplots()
ax.plot(a4_values, growing, color=BLUE, linewidth=2,
        label=r"$e^{a_4}$: ordinary space $x_1, x_2, x_3$ (inflates)")
ax.plot(a4_values, shrinking, color=ORANGE, linewidth=2, linestyle="--",
        label=r"$e^{-a_4}$: extra times $x_5, x_6, x_7$ (deflate)")
ax.plot(a4_values, six_factors, color="black", linewidth=1.5, linestyle=":",
        label=r"product of all six: $e^{3 a_4} e^{-3 a_4} = 1$")
```

A new colour, a new figure, and three curves: a solid blue line, a dashed orange line (the line style of two hyphens) and a dotted black line; `linewidth` is the thickness of a line in points.

```python
ax.set_yscale("log")  # a logarithmic vertical axis
ax.set_xlabel(r"the metric function $a_4$ (a pure number)")
ax.set_ylabel(r"length factor divided by $\sin^{1/6} z$")
ax.set_title("As $a_4$ grows, ordinary space inflates and the extra times deflate")
```

`ax.set_yscale("log")` makes the vertical axis **logarithmic**: equal distances on it mean equal factors (0.1, 1, 10, 100). On such an axis the height of the point of $e^{a_4}$ is proportional to $\ln e^{a_4} = a_4$, so the curve is a straight line rising with slope 1 (per factor $e$), and $e^{-a_4}$ is a straight line falling with slope $-1$. The other lines label the axes and set the title.

```python
# Direct labels at the right ends of the two lines (the numbers at a4 = 3).
ax.annotate(f"{growing[-1]:.2f}", (3.0, growing[-1]), xytext=(4, 0),
            textcoords="offset points", va="center")
ax.annotate(f"{shrinking[-1]:.4f}", (3.0, shrinking[-1]), xytext=(4, 0),
            textcoords="offset points", va="center")
ax.set_xlim(-0.1, 3.5)  # room on the right for the two numbers
ax.set_ylim(0.02, 150.0)  # room at the top for the legend
ax.legend(loc="upper left")
```

`growing[-1]` is the last entry of the array, the value at $a_4 = 3$ (a negative index counts from the end). `ax.annotate` writes the number next to the point $(3, e^{3})$, shifted 4 points to the right (`xytext=(4, 0)` with `textcoords="offset points"`); likewise for $e^{-3}$. The limits of the axes leave room for these numbers and for the legend.

```python
save_figure(fig, "scale_factors",
            r"The length factors of the author's metric at a fixed hidden "
            r"coordinate, divided by $\sin^{1/6} z$, against the metric function "
            r"$a_4$ from 0 to 3 (horizontal axis, a pure number; vertical axis "
            r"logarithmic, a pure number). Solid blue: $e^{a_4}$, the factor of "
            r"each direction of ordinary space, which grows to $e^3 = 20.09$; "
            r"dashed orange: $e^{-a_4}$, the factor of each extra time, which "
            r"shrinks to $e^{-3} = 0.0498$; dotted black: the product of the three "
            r"space factors and the three extra-time factors, which stays exactly "
            r"1. On the logarithmic axis both exponentials are straight lines.")
report("e^(a4) at a4 = 3", f"{growing[-1]:.4f}")
report("e^(-a4) at a4 = 3", f"{shrinking[-1]:.6f}")
```

The figure is saved as `00b_2_scale_factors.png`, and the two values at $a_4 = 3$ are printed: $e^{3} = 20.0855$ and $e^{-3} = 0.049787$ (Out [7]). What Figure 00b.2 shows: two straight lines on the logarithmic axis, one rising and one falling at the same rate, mirror images of each other in the horizontal line at 1, and the flat dotted product at 1. This is Fact 3 of Section 0.14 in a picture: whatever ordinary space gains, the extra times lose.

```python
check(np.max(np.abs(six_factors - 1.0)) < 1e-12,
      "the product of the three inflating and three deflating factors is 1")
check(np.max(np.abs(np.log(growing) - a4_values)) < 1e-12
      and np.max(np.abs(np.log(shrinking) + a4_values)) < 1e-12,
      "on a logarithmic axis e^(a4) and e^(-a4) are straight lines of slope +1, -1")
```

The first check requires the product to be 1 at all 301 points up to $10^{-12}$ (rounding). The second uses `np.log`, the natural logarithm: $\ln e^{a_4} = a_4$ and $\ln e^{-a_4} = -a_4$ at all points, which is exactly the statement that the two curves are straight lines on the logarithmic axis.

**In [8], the eight length factors.**

```python
AQUA = "#1baf7a"
z_fixed = np.pi / 4  # the hidden coordinate z = pi/4
a4_choices = [0.0, 0.5, 1.0]
factors = {}  # a4 -> the list of the eight length factors f1 ... f8
for a4_value in a4_choices:
    factors[a4_value] = [float(np.sqrt(abs(entry_functions[k](a4_value, z_fixed))))
                         for k in range(8)]
```

A third colour, the fixed hidden coordinate $z = \pi/4$, and three values of $a_4$. For each value the list of the eight length factors $f_i = \sqrt{|g_{ii}|}$ of Fact 2 is computed with the numpy functions of In [5] (`abs` is the absolute value, `np.sqrt` the square root, `float` makes a plain Python number) and stored in the dictionary `factors` under the value of $a_4$.

```python
say("a4    " + "  ".join(f"{name:>6}" for name in coordinates) + "  product")
for a4_value in a4_choices:
    row = "  ".join(f"{value:6.4f}" for value in factors[a4_value])
    say(f"{a4_value:<4}  {row}  {np.prod(factors[a4_value]):.4f}")
```

The table of Out [8]. `"  ".join(...)` joins texts with two blanks between them; `{name:>6}` writes a name right-aligned in 6 characters, `{value:6.4f}` a number with 4 decimals in 6 characters, and `{a4_value:<4}` the value of $a_4$ left-aligned in 4 characters. `np.prod` multiplies all entries of a list. The printed rows are the numbers of Section 0.14: 0.9439 for every direction except $x_4$ and $x_8$ at $a_4 = 0$; 1.5562 and 0.5725 at $a_4 = 0.5$; 2.5657 and 0.3472 at $a_4 = 1$; the factors of $x_4$ and $x_8$ are 1.0000, and the product is 0.7071 in each row.

```python
fig, ax = plt.subplots()
positions = np.arange(8)  # one group of bars per direction
width = 0.26  # the width of one bar; three bars side by side in each group
for shift, a4_value, colour in zip((-1, 0, 1), a4_choices, (BLUE, ORANGE, AQUA)):
    # edgecolor="white" with linewidth 1.5 leaves a thin gap between the bars.
    ax.bar(positions + shift * width, factors[a4_value], width, color=colour,
           edgecolor="white", linewidth=1.5, label=f"$a_4 = {a4_value:g}$")
```

A bar chart. `np.arange(8)` is the array 0, 1, ..., 7, one position per direction. For each value of $a_4$ the bars are shifted by $-1$, 0 or $+1$ bar widths, so that the three bars of a direction stand side by side. `ax.bar(positions, heights, width, ...)` draws one bar per position; `{a4_value:g}` writes the number in its shortest form (0, 0.5, 1).

```python
ax.set_xticks(positions, labels=coordinates)
ax.set_xlabel("direction")
ax.set_ylabel(r"length factor $f_i = \sqrt{|g_{ii}|}$ (pure number)")
ax.set_title(r"The eight length factors at $z = \pi/4$ for three values of $a_4$")
ax.legend(loc="upper center")
save_figure(fig, "length_factors",
            r"The eight length factors $f_i = \sqrt{|g_{ii}|}$ of the author's "
            r"metric at the hidden coordinate $z = \pi/4$ for $a_4 = 0$ (blue), "
            r"$a_4 = 0.5$ (orange) and $a_4 = 1$ (aqua); horizontal axis the "
            r"directions $x_1$ to $x_8$, vertical axis the factor (a pure number). "
            r"The factors of ordinary space $x_1$, $x_2$, $x_3$ grow from 0.94 to "
            r"2.57 as $a_4$ grows from 0 to 1, those of the extra times $x_5$, "
            r"$x_6$, $x_7$ shrink from 0.94 to 0.35, and those of the time $x_4$ "
            r"and of the hidden direction $x_8$ stay 1. The product of the eight "
            r"factors is $\cos(\pi/4) = 0.7071$ in all three cases.")
```

Labels, title, legend, and the figure `00b_3_length_factors.png`. What Figure 00b.3 shows: over $x_1$, $x_2$, $x_3$ the bars rise from blue to orange to aqua; over $x_5$, $x_6$, $x_7$ they fall; over $x_4$ and $x_8$ all three bars have the height 1.

```python
products = [float(np.prod(factors[a4_value])) for a4_value in a4_choices]
A4_REPORT = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
verdict, detail = recorded_check(A4_REPORT, "sqrt_abs_det_g_is_cos_z")
check_reproduces(
    all(abs(p - np.cos(z_fixed)) < 1e-12 for p in products) and verdict == "PASS",
    "the product of the eight factors is cos(pi/4) = 0.7071 for a4 = 0, 0.5, 1",
    f"{A4_REPORT}, check sqrt_abs_det_g_is_cos_z")
```

The three products, and the verdict of the Wolfram check `sqrt_abs_det_g_is_cos_z` of the field equations for $a_4$. `all(...)` is true when the condition holds for every product: each must equal $\cos(\pi/4)$ up to $10^{-12}$. Out [8] ends with the PASS line and the record it reproduces.

**In [9], the volume factor for three values of $a_4$.**

```python
z_values = np.linspace(0.005, np.pi / 2 - 0.005, 200)  # 200 values inside (0, pi/2)
volume = {}  # a4 -> the product of the eight factors at every z
for a4_value in (0.0, 1.0, 2.0):
    product = np.ones_like(z_values)
    for k in range(8):
        values = np.full_like(z_values, 1.0) * entry_functions[k](a4_value, z_values)
        product = product * np.sqrt(np.abs(values))
    volume[a4_value] = product
```

200 values of $z$ inside the patch. For each of $a_4 = 0$, 1 and 2, `product` starts as an array of 200 ones (`np.ones_like`) and is multiplied in turn by the eight length factors, computed at all 200 values of $z$ at once (the factor 1.0-array again makes the constant entry an array). The result, the volume factor $f_1 \cdots f_8$ at every $z$, is stored under the value of $a_4$.

```python
fig, ax = plt.subplots()
ax.plot(z_values, np.cos(z_values), color="black", linewidth=1.5,
        label=r"$\cos z$")
markers = {0.0: ("o", BLUE), 1.0: ("s", ORANGE), 2.0: ("^", AQUA)}
for start, a4_value in enumerate((0.0, 1.0, 2.0)):
    marker, colour = markers[a4_value]
    chosen = slice(4 * start, None, 12)  # every 12th point, shifted by 4
    ax.plot(z_values[chosen], volume[a4_value][chosen], marker, color=colour,
            markersize=6, label=rf"$f_1 \cdots f_8$ for $a_4 = {a4_value:g}$")
```

The black curve $\cos z$, then the computed points. The dictionary `markers` gives each value of $a_4$ a marker shape (`"o"` circles, `"s"` squares, `"^"` triangles) and a colour. `slice(4 * start, None, 12)` selects the entries number `4 * start`, `4 * start + 12`, `4 * start + 24`, and so on to the end: every 12th point, starting at 0, 4 or 8, so that the three sets of markers do not hide each other. A string with both `r` and `f` in front is a raw f-string.

```python
ax.set_xlabel(r"hidden coordinate $z = 6 H x_8$ (radians)")
ax.set_ylabel(r"volume factor $\sqrt{|\det g|}$ (pure number)")
ax.set_title(r"The volume factor is $\cos z$ for every value of $a_4$")
ax.legend()
save_figure(fig, "volume_factor",
            r"The volume factor $\sqrt{|\det g|} = f_1 f_2 \cdots f_8$ of the "
            r"author's metric against the hidden coordinate $z = 6 H x_8$ from 0 to "
            r"$\pi/2$ (horizontal axis, in radians; vertical axis a pure number), "
            r"computed from the eight entries for $a_4 = 0$ (blue circles), "
            r"$a_4 = 1$ (orange squares) and $a_4 = 2$ (aqua triangles), with the "
            r"curve $\cos z$ (black line). All three sets of points lie on the "
            r"curve: the volume factor does not depend on $a_4$, because the "
            r"inflation of ordinary space and the deflation of the extra times "
            r"cancel; it falls from 1 at $z = 0$ to 0 at $z = \pi/2$.")
```

Labels, title, legend and the figure `00b_4_volume_factor.png`. What Figure 00b.4 shows: circles, squares and triangles all sit on the one black curve $\cos z$, although the three values of $a_4$ stretch ordinary space by the factors 1, $e = 2.72$ and $e^2 = 7.39$; this is Fact 4 of Section 0.14.

```python
largest = max(float(np.max(np.abs(volume[v] - np.cos(z_values)))) for v in volume)
report("largest difference from cos z", f"{largest:.1e}")
verdict, detail = recorded_check(THEORY_REPORT, "sqrt_det_g_equals_cos_z")
check_reproduces(
    largest < 1e-12 and verdict == "PASS",
    "the volume factor equals cos z at 200 points for a4 = 0, 1 and 2",
    f"{THEORY_REPORT}, check sqrt_det_g_equals_cos_z")
```

For each value of $a_4$ the largest distance of the 200 computed values from $\cos z$; `max(...)` takes the largest of the three. Out [9] prints $8.9 \times 10^{-16}$, four times the machine epsilon of Section 0.22: only rounding. The check also reads the verdict of the Python verifier's check `sqrt_det_g_equals_cos_z`.

**In [10], the last check.**

```python
figure_names = ["00b_1_eta_heat_map.png", "00b_2_scale_factors.png",
                "00b_3_length_factors.png", "00b_4_volume_factor.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "the four figure files of this notebook exist")
all_checks_passed()
```

The four figure files must exist in the folder of the figures (in a check run of nbkit, in its scratch folder, which `output_file` points to). The last line prints ALL 14 CHECKS PASSED (notebook 00b): four checks in In [2], one in In [4], one in In [5], three in In [6], two in In [7], one each in In [8], In [9] and In [10].

### 0.18 The honesty ledger, and how a report is tied to its files

The **honesty ledger** is the table of the main statements of the book, each with its label (Section 0.3), a short note where one is needed, and the reports of the Revision record that verify it. It is the book's promise in one page: whatever a later chapter says, its label is the one given here, and every reader can open the named reports and read the verdicts (Section 0.4, level 2). The ledger below has sixteen rows. Every one of the verifier reports of the Revision record belongs to exactly one row, and the four rows labelled HYPOTHESIS or OPEN have no report at all, because nothing in the record establishes them. Notebook 00c checks all of this and counts the checks of each row; the ledger describes the record on the date of the notebook's last verified run, which its provenance file records. (Reports in the folder `Revision/kohn_sham/reports` are written below with the short folder name `kohn_sham/reports`, and so on; every path starts in the folder `Revision`.)

| statement (with its row number) | label | verified in (folder Revision) |
| --- | --- | --- |
| (1) the gamma matrices, $C$, $\Gamma$, $B$; Pin(4,4) and Spin(4,4) (Chapters 4 and 5) | PROVED | `algebra/reports/wolfram-algebra.json`, `algebra/reports/python-algebra.json` |
| (2) the Lagrangians, field equations, energy-momentum tensor and quantisation of both fields (Chapters 7, 9 and 10) | PROVED | `theory/reports/wolfram-field-theory.json`, `theory/reports/python-field-theory.json` |
| (3) the exact scope of the non-triviality (Chapter 8) | PROVED | `theory/reports/wolfram-scope.json`, `theory/reports/python-scope.json` |
| (4) the conservation identities of the energy-momentum tensor; the spin connection (Chapters 6 and 9) | PROVED | `lead_checks/reports/emt-divergence-and-spin-connection.json` |
| (5) the field equations for $a_4$ (Chapter 12) | PROVED | `field_equations_a4/reports/wolfram-a4-report.json`, `field_equations_a4/reports/python-a4-report.json`, `lead_checks/reports/einstein-gauss-bonnet-a4.json` |
| (6) the generalized Kronecker delta (GKD) and the three Lovelock tensors (Chapter 11) | PROVED | `gkd_lovelock/results/lovelock-report.json`, `gkd_lovelock/results/gkd-selftest.json`, `gkd_lovelock/results/wolfram-gkd-report.json`, `gkd_lovelock/results/python-lovelock-report.json` |
| (7) the Kohn-Sham theory: the blocks, the rescaling, the exact exchange (Chapter 14) | PROVED | `kohn_sham/reports/ks-theory-wolfram.json`, `kohn_sham/reports/ks-theory-python.json` |
| (8) the Kohn-Sham states along the deflating history (Chapters 15 and 16) | COMPUTED | `kohn_sham/reports/ks-rust-solver.json`, `kohn_sham/reports/ks-reference.json`, `kohn_sham/reports/ks-crosscheck.json`, `kohn_sham/reports/ks-rust-determinism.json`, `kohn_sham/reports/ks-rust-mermin-roots.json` |
| (9) the Kohn-Sham history of $a_4$ is a prescribed background (Chapter 17) | ASSUMED | `field_equations_a4/reports/ks-source-conditions.json` |
| (10) the pairing theorems T1, T2 (with the Z2 mirror ASSUMED) and Q (Chapter 18) | PROVED | `pairing/reports/wolfram-pairing.json`, `pairing/reports/python-pairing.json` |
| (11) T3 (with the Z2 mirror ASSUMED): the Kohn-Sham universes of mass $+M$ and $-M$ (Chapter 19) | PROVED | `pairing/kohn_sham/reports/wolfram-t3.json`, `pairing/kohn_sham/reports/python-t3.json` |
| (12) the charge-conjugation matrices $C$ and $\Gamma C$; the conserved U(1) charge (Chapters 5 and 21) | PROVED | `lead_checks/reports/charge-conjugation-and-u1.json` |
| (13) a time-varying dark sector from the fields (Chapter 22) | HYPOTHESIS: to be investigated; no result yet | no report |
| (14) our universe has a partner of opposite charge (Chapters 20 and 21) | HYPOTHESIS: the T1 maps exist; that a partner exists is not shown | no report |
| (15) the big bang creates universes in pairs (Chapter 20) | OPEN: not proved; no creation process, rate or amplitude | no report |
| (16) the theory explains the excess of matter over antimatter (Chapter 21) | OPEN: the theory as built does not explain it | no report |

Five remarks make the table exact.

- Rows 10 and 11 are PROVED theorems with an ASSUMED ingredient in their statement: T2 and T3 hold with the Z2 mirror, a choice of boundary condition at the edge of the hidden direction that the equations do not derive. A proved theorem with an assumption means: if the assumption holds, the conclusion holds.
- Row 9 is labelled ASSUMED although five checks belong to it. Those checks show that the computed Kohn-Sham states cannot be the source of the history $a_4 = A H x_4$ in the field equations (their energy-momentum tensor depends on $x_8$, and it violates an algebraic condition of the field equations); so the history cannot be derived from them and is assumed.
- Corollary C1 of Section 0.2 has no row of its own: it is T1 (row 10) combined with the checks `einstein_no_vacuum_solution` of `Revision/field_equations_a4/reports/wolfram-a4-report.json` and `einstein_no_vacuum` of `Revision/field_equations_a4/reports/python-a4-report.json` (row 5).
- Row 14 is a HYPOTHESIS and not a theorem, although T1 is proved. T1 says: if a universe with mass $+m$ is a solution, its image with mass $-m$ is a solution too, with the opposite charge. It does not say that the image exists alongside ours; a single universe is an equally valid solution without its partner, and for universes quantised independently of each other there is no cancellation of the charges (Q).
- Row 15 is OPEN, not a HYPOTHESIS, because the book examines it as a question and finds that the record does not answer it: no equation of the record describes the creation of anything. The pairing record says so itself, in the list of twelve things that it does not establish (Notebook 00c prints the list).

The ledger is the state of the record when this chapter was written. The Revision record is still growing (for example, the dark-sector hypothesis of row 13 is being investigated, and verifier reports may gain checks), and the final ledger of the book is completed when the book is assembled; Notebook 00c is the tool that keeps the table honest, because it fails when a new report appears that no row claims.

**Two independent verifiers.** For eight subjects (rows 1 to 3, 5 to 7, 10 and 11) the exact statements were checked twice: by a verifier written in the Wolfram Language and by an independent one written in Python with sympy, sharing no code. The two do not check exactly the same list of statements, but where they overlap, an error would have to be made twice, in two languages, by two separate programs, to go unnoticed. The Kohn-Sham numbers (row 8) were computed twice in the same spirit, by the Rust solver and by an independent Python reference solver, and compared with tolerances fixed in advance (Chapter 16).

**Fingerprints.** A report is worth something only for the exact files it was computed from. To tie the two together, a report writes down a **fingerprint** of each file it read. The fingerprint used here is **sha256**: a fixed recipe that turns the bytes of a file, however many there are, into a number of 256 binary digits, written as 64 **hexadecimal** characters. Hexadecimal digits are the sixteen symbols 0 to 9 and a to f, standing for the numbers 0 to 15; each one carries 4 binary digits, and $64 \cdot 4 = 256$. The recipe has three properties that matter here:

- it is deterministic: the same bytes always give the same fingerprint, on every computer;
- a change of a single byte changes the fingerprint completely, not just in one place;
- nobody knows how to construct two different files with the same fingerprint, and nobody has ever found such a pair.

The first property is a fact of the recipe. The second is what Notebook 00c measures (below). The third is believed by everyone who uses sha256 but is not proved mathematically; the book relies on it, and so it is ASSUMED.

How much should a fingerprint change? Suppose the new fingerprint behaves like a string of 64 hexadecimal characters chosen at random. One character of it equals the corresponding character of the old fingerprint with probability

$$
p_{\mathrm{same}} = \frac{1}{16}
$$

(the new character is one of 16 equally likely symbols, and exactly one of them is the old one), so it differs with probability

$$
p_{\mathrm{differ}} = 1 - \frac{1}{16} = \frac{15}{16}
$$

(the probabilities of an event and of its opposite add up to 1). The expected number of differing characters among the 64 is

$$
64 \cdot \frac{15}{16} = 4 \cdot 15 = 60
$$

(the expected number of differing characters is the sum, over the 64 characters, of the probability that the character differs; and $64/16 = 4$). Notebook 00c changes each character of a sentence of 115 characters in turn and finds that between 54 and 64 characters of the fingerprint change, 60.03 on average (COMPUTED): exactly what a random string would do.

A report of the Revision record records the fingerprints of its input files in one of two ways: in dedicated keys (the Wolfram check of the Lovelock tensors lists 15 files in its keys `inputSha256` and `sourceSha256`), or inside the detail text of a check, written as (sha256 followed by the 64 characters, or only their first 16). When the fingerprint of today's file equals the recorded one, the report was computed from exactly today's file, byte for byte. Notebook 00c compares 24 recorded fingerprints with today's files, and Notebook 00d compares 582 more (Section 0.22).

**Example: the ledger checked by the computer.** Notebook 00c does at level 2 (Section 0.4) what a careful reader would do by hand, but for every report at once. It opens the charge-conjugation report and reads its twelve checks; writes one function that counts the checks of a report in each of the three layouts that occur in the record; searches the whole folder `Revision` for reports and finds exactly the 27 of its list; confirms that every check has the verdict PASS and that the counts agree with what the reports say about themselves, with the table of `Revision/README.md` and with the Kohn-Sham cross-check; builds the ledger above and checks that every report belongs to exactly one row; prints the twelve sentences of the pairing record about what it does not establish; and compares fingerprints. It draws four figures and ends with ALL 14 CHECKS PASSED (notebook 00c).

<!-- NOTEBOOK 00c -->

### 0.21 Line-by-line walk-through of Notebook 00c

The notebook has fourteen code cells, In [1] to In [14]. This section explains every line of each of them.

**In [1], the set-up cell.** It is the set-up cell of Notebook 00a, word for word, except that its comment lines hold the run instructions of Notebook 00c (Section 0.19) and the line `NOTEBOOK_ID = "00c"` names this notebook. Every line of its code is explained in Section 0.13. It prints Set-up of notebook 00c complete: repository folder found, helpers defined.

**In [2], one report opened by hand.**

```python
import hashlib  # computes sha256 fingerprints
import re  # finds patterns in texts ("regular expressions")
import sys  # sys.stdout is the channel through which the notebook prints

import numpy as np  # arrays of numbers
```

Three modules of Python itself: `hashlib` computes fingerprints, `re` finds patterns in texts (In [6] explains them), `sys` gives the printing channel; and numpy.

```python
def read_report(path):
    """The content of the JSON file path of the repository (dictionaries, lists)."""
    return json.loads(repository_file(path).read_text(encoding="utf-8"))


def check_reproduces(condition, name, record):
    """check(condition, name, record=record), after sending the waiting output."""
    sys.stdout.flush()  # send every printed line that is still waiting
    check(condition, name, record=record)
```

`read_report` reads a JSON file of the repository into dictionaries and lists, as explained for In [2] of Notebook 00b (Section 0.17). `check_reproduces` is the same helper as there: it sends the waiting printed text first, so that a PASS line and its line reproduces ... arrive together.

```python
CC_REPORT = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
cc = read_report(CC_REPORT)  # a dictionary with the keys producer, summary, checks
producer = cc["producer"]
say(f"producer: {producer}")
```

The report of the lead's independent check of the charge-conjugation matrices and of the conservation of the charge (row 12 of the ledger) is read. Its key `producer` names the program that wrote it; the first two lines of Out [2] print it: `Revision/lead_checks/charge_conjugation_and_u1.py`, a short independent Python program that imports no other Revision code.

```python
for entry in cc["checks"]:  # each entry is a dictionary: name, verdict, detail
    verdict, name = entry["verdict"], entry["name"]
    say(f"  {verdict}  {name}")
```

The loop prints the verdict and the name of each of its checks, the next twelve lines of Out [2]: from `representation_real` to `u1_noether_matrix_identity`, all PASS. (The line `verdict, name = a, b` gives two names at once.)

```python
stated = cc["summary"]  # what the report says about itself: passed and total
stated_passed, stated_total = stated["passed"], stated["total"]
say(f"the report states: {stated_passed} passed of {stated_total}")
passed = sum(1 for entry in cc["checks"] if entry["verdict"] == "PASS")
number_of_checks = len(cc["checks"])
report("checks with the verdict PASS, counted", f"{passed} of {number_of_checks}")
check_reproduces(passed == stated["passed"] == stated["total"] == 12,
                 "12 of 12 checks of the charge-conjugation report are PASS",
                 f"{CC_REPORT}, its summary")
```

A report also states its own totals, under the key `summary`; they are printed. Then the notebook counts for itself: `sum(1 for entry in ... if ...)` adds 1 for every check whose verdict is PASS, and `len` is the number of checks. Python allows a chain of comparisons, `a == b == c == 12`, which is true only when every neighbouring pair is equal. The check requires that our count, the stated number of passed checks and the stated total are all 12. This is level 2 of Section 0.4, done by the computer.

**In [3], three details of the same report.**

```python
for wanted in ("representation_real", "charge_conjugation_matrix_minus",
               "u1_noether_matrix_identity"):
    detail = next(entry["detail"] for entry in cc["checks"]
                  if entry["name"] == wanted)  # the first (and only) such check
    if wanted == "u1_noether_matrix_identity":
        # This detail is long; its last part, after the last "; ", is the result.
        detail = detail.rsplit("; ", 1)[-1]
    say(f"{wanted}:")
    say("    " + detail)
```

For three check names, `next(... for entry in ... if ...)` returns the detail of the first check with that name. The third detail is long; `rsplit("; ", 1)` cuts it once, at the last semicolon (the `r` means: search from the right), and `[-1]` keeps the last piece. Out [3] prints, in the report's own words: that the gammas, $C$ and $S^{ab}$ are real, so that plain complex conjugation is the identity on a real field; that $\mathcal{C}_- = \Gamma C$ satisfies $\mathcal{C}_-^{-1} \gamma^a \mathcal{C}_- = +(\gamma^a)^T$ and that the conjugate field $\Gamma \Psi^*$ solves the field equation in which the term $V$ that holds the mass has the opposite sign (the report writes $V \to -V$); and that the charge $Q = \int \cos z \, \Psi^\dagger B \Psi \, d^7x$ is conserved when the field equations hold. These are the statements of Section 0.2 about charge conjugation, with their record; Chapters 5 and 21 derive them.

**In [4], one counting function for three layouts.**

```python
def count_checks(data):
    """(number of passed checks, number of checks), counted from the checks."""
    if isinstance(data.get("checks"), list):  # layout A
        verdicts = [entry["verdict"].upper() == "PASS" for entry in data["checks"]]
    elif isinstance(data.get("checks"), dict):  # layout B
        verdicts = [entry["passed"] is True for entry in data["checks"].values()]
    else:  # layout C: a self-test passes when it found no mismatch
        verdicts = [entry["mismatches"] == 0 for entry in data["results"]]
    # True counts as 1 and False as 0 when added.
    return sum(verdicts), len(verdicts)
```

The reports were written by different programs and store their checks in three layouts. `data.get("checks")` returns the value under the key `checks`, or `None` if there is none (where `data["checks"]` would stop with an error). `isinstance(value, list)` asks whether the value is a list. In layout A the checks are a list of dictionaries with a verdict; in layout B a dictionary from each name to a dictionary with the entry `passed` (`.values()` gives the inner dictionaries, and `is True` asks for the value `True` itself); in layout C (the self-test of the Rust GKD program) a list `results` of tests, each passing when its count of `mismatches` is 0. In each case `verdicts` is a list of `True` and `False`, and the function returns the number of `True` entries and the length of the list.

```python
def stated_summary(data):
    """(passed, total) as the report states them itself; None if it states none."""
    summary = data.get("summary")
    if isinstance(summary, dict):  # {"passed": n, "total": n} or {"pass", "checks"}
        return (summary.get("passed", summary.get("pass")),
                summary.get("total", summary.get("checks")))
    counts = data.get("counts")
    if isinstance(counts, dict) and "pass" in counts:  # {"pass", "fail", "pending"}
        return counts["pass"], counts["pass"] + counts["fail"] + counts["pending"]
    if "checkCount" in data:  # a total and a number of failed checks
        failed = data.get("failCount", data.get("failedCount",
                                                 data.get("failedCheckCount")))
        return data["checkCount"] - failed, data["checkCount"]
    return None
```

The totals that a report states about itself are written in different words: a dictionary `summary` with `passed` and `total` (or `pass` and `checks`); a dictionary `counts` with the numbers of passed, failed and pending checks; or a total `checkCount` with a number of failed checks under one of three names. `.get(key, default)` returns the default when the key is missing, so the nested `.get` calls try the names one after the other. The function returns the pair (passed, total), or `None` when the report states no totals.

```python
EXAMPLES = [("A", "Revision/pairing/reports/wolfram-pairing.json"),
            ("B", "Revision/gkd_lovelock/results/lovelock-report.json"),
            ("C", "Revision/gkd_lovelock/results/gkd-selftest.json")]
for layout, path in EXAMPLES:
    data = read_report(path)
    passed, total = count_checks(data)
    say(f"layout {layout}: {path}")
    say(f"    counted {passed} of {total}; stated {stated_summary(data)}")
```

One report of each layout, counted and compared with what it states: Out [4] shows the counts of the Wolfram pairing report, of the Rust Lovelock report and of the GKD self-test, which states no totals (`None`) but only its verdict.

**In [5], every report of the Revision record.**

```python
def is_report(path):
    """True if the JSON file path (a Path) is a verifier report."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return False
    results = data.get("results")
    self_test = (isinstance(results, list) and len(results) > 0
                 and isinstance(results[0], dict) and "mismatches" in results[0])
    return "checks" in data or self_test
```

A JSON file is a verifier report when it is a dictionary that has a key `checks`, or, like the GKD self-test, a non-empty list `results` whose first entry is a dictionary with the key `mismatches`. `"checks" in data` asks whether the dictionary has that key. The conditions joined by `and` are tested from the left and the testing stops at the first false one, so `results[0]` is never read from an empty or missing list.

```python
found_reports = []  # every report found in the folder Revision, as a relative path
for path in sorted(repository_file("Revision").rglob("*.json")):
    relative = path.relative_to(REPO).as_posix()  # e.g. "Revision/algebra/..."
    if relative.startswith("Revision/textbook/") or "/target/" in relative:
        continue  # this book's own files, and the Rust build folders
    if is_report(path):
        found_reports.append(relative)
report("verifier reports found in the folder Revision", len(found_reports))
```

`rglob("*.json")` lists every file ending in `.json` in the folder `Revision` and in all its sub-folders, and `sorted` puts the list in a fixed order. `path.relative_to(REPO)` is the path from the repository folder on, and `.as_posix()` writes it with `/` on every operating system. `continue` skips the rest of the loop for this file: the book's own files and the build folders of the Rust programs are not part of the record. Every other report is collected. Out [5] begins with the number found, 27.

```python
REPORTS = [  # (report, engine)
    ("Revision/algebra/reports/wolfram-algebra.json",
     "Wolfram"),
    ("Revision/algebra/reports/python-algebra.json",
     "Python"),
```

The list `REPORTS` holds the 27 reports of the record, each with the **engine** that did its computation: `"Wolfram"` (Wolfram Language), `"Python"`, `"Rust"`, or `"lead"` for the lead's short independent Python checks. Its 54 lines all have the form of these four; in order they name the two algebra reports, the four theory reports (field theory and scope, Wolfram and Python each), the three reports of the field equations for $a_4$ (Wolfram, Python and the Kohn-Sham source conditions), the four reports of GKD and the Lovelock tensors (two Rust, one Wolfram, one Python), the seven Kohn-Sham reports (theory in Wolfram and Python, the Rust solver, determinism, the roots of the Mermin equation, the reference solver and the cross-check), the four pairing reports (T1, T2 and Q; T3) and the three reports of the lead's checks. Section 0.20 prints the whole list, and the table of Out [5] repeats it.

```python
check(found_reports == sorted(path for path, _ in REPORTS),
      f"the search finds exactly the {len(REPORTS)} reports of the list")
```

The search must find exactly the reports of the list: no report is missing from the list, and so from the ledger. (In `for path, _ in REPORTS` the name `_` takes the engine, which is not needed here.) When a new report is added to the record, this check fails until the new report gets its place in the list and in the ledger.

```python
counted = {}  # report -> (passed, total)
header = "report (in the folder Revision)"
say(f"{header:59} engine   passed of all")
for path, engine in REPORTS:
    data = read_report(path)
    counted[path] = count_checks(data)
    passed, total = counted[path]
    short = path.removeprefix("Revision/")
    say(f"{short:59} {engine:8} {passed:6d} of {total:3d}")
```

Every report is read and counted; the pair (passed, total) is stored in the dictionary `counted` under its path. `removeprefix` removes `Revision/` from the front of the path to keep the table narrow, and `{passed:6d}` writes a whole number right-aligned in 6 characters. The 27 lines of the table in Out [5] are printed here.

```python
all_checks = sum(total for _, total in counted.values())
all_passed = sum(passed for passed, _ in counted.values())
report("reports", len(REPORTS))
report("checks in all reports", all_checks)
engine_totals = {}  # engine -> the number of its checks
for engine in ("Wolfram", "Python", "Rust", "lead"):
    engine_totals[engine] = sum(counted[path][1] for path, e in REPORTS
                                if e == engine)
    report(f"checks done with the engine {engine}", engine_totals[engine])
```

The totals over all reports, and the total per engine: for each engine the numbers of checks of its reports are added (`counted[path][1]` is the total of a report). These are the RESULT lines of Out [5]. The numbers are not written into the notebook: they are counted from the record each time, so they follow the record. On the day the notebook was last checked for this chapter they were 940 checks in all: 377 done with the Wolfram Language, 456 with Python, 70 with Rust and 37 by the lead's checks.

```python
check(all_passed == all_checks and sum(engine_totals.values()) == all_checks,
      f"all {all_checks} checks of the {len(REPORTS)} reports have the verdict PASS")
```

Every check of every report must have passed, and the four engine totals must add up to the total (each report has exactly one engine).

```python
disagree = []  # reports whose own summary differs from our count
for path, _ in REPORTS:
    data = read_report(path)
    stated = stated_summary(data)
    if stated is None:  # layout C: the self-test states only its verdict
        stated = counted[path] if data["verdict"] == "SUCCESS" else None
    if stated != counted[path]:
        disagree.append(path)
check(disagree == [], "each report states the same totals that we counted")
```

For every report our count must equal what the report states about itself. The GKD self-test states no totals; for it the stated verdict SUCCESS is required instead. Out [5] ends with this PASS line.

**In [6], two other places that quote the counts.**

```python
R = "Revision/"
README_ORDER = [  # the reports whose counts the README table quotes, in its order
    R + "gkd_lovelock/results/lovelock-report.json",  # row gkd_lovelock/
    R + "gkd_lovelock/results/python-lovelock-report.json",
```

`R + "..."` joins two strings. The list `README_ORDER` names, in the order in which they appear in the table of the file `Revision/README.md`, the 16 reports whose counts that table quotes: the three of GKD and the Lovelock tensors, the two of the algebra, the four of the theory, the three of the field equations for $a_4$ and the four of the pairing (its 16 entries, one per line, have the form of the two shown).

```python
readme_lines = repository_file("Revision/README.md").read_text(
    encoding="utf-8").split("\n")
table = "\n".join(line for line in readme_lines if line.startswith("| `"))
quoted_readme = [(int(p), int(t)) for p, t in re.findall(r"(\d+)/(\d+)", table)]
say("the README quotes: " + ", ".join(f"{p}/{t}" for p, t in quoted_readme))
report("counts quoted in the README table", len(quoted_readme))
```

The file is read and cut into lines; the lines of the table of the folders start with a vertical bar, a blank and a backtick, and they are joined again. A **regular expression** is a pattern that describes a family of texts: in `(\d+)/(\d+)`, `\d` means one digit, `+` means one or more of what stands before it, and the round brackets mark the parts to return. `re.findall` returns every match as a pair of the two marked parts, such as `("19", "19")`; `int` turns them into numbers. Out [6] prints the 16 counts found.

```python
check_reproduces(quoted_readme == [counted[path] for path in README_ORDER],
                 f"the {len(README_ORDER)} counts quoted in the README equal ours",
                 "Revision/README.md, the table of the folders")
```

The 16 quoted counts must equal our counts of the 16 reports, in this order.

```python
CROSS = "Revision/kohn_sham/reports/ks-crosscheck.json"
detail = next(entry["detail"] for entry in read_report(CROSS)["checks"]
              if entry["name"] == "inputs_all_pass")
quoted = re.findall(r"(\d+)/(\d+) PASS", detail)  # [("37", "37"), ("42", "42"), ...]
say("the cross-check quotes: " + ", ".join(f"{p}/{t}" for p, t in quoted))
ours = [counted["Revision/kohn_sham/reports/ks-reference.json"],
        counted["Revision/kohn_sham/reports/ks-rust-solver.json"],
        counted["Revision/kohn_sham/reports/ks-rust-determinism.json"]]
numbers = ", ".join(str(total) for _, total in ours)  # e.g. "37, 42, 14"
check_reproduces([(int(p), int(t)) for p, t in quoted] == ours,
                 f"the cross-check quotes the counts {numbers} that we counted",
                 f"{CROSS}, check inputs_all_pass")
```

The Kohn-Sham cross-check read three other reports before it compared the two solvers, and quoted their counts in the detail of its check `inputs_all_pass`, in the form `37/37 PASS`. The pattern `(\d+)/(\d+) PASS` finds them; they must equal our counts of the reference report, the Rust solver report and the determinism report, in this order. Out [6] ends with the PASS line.

**In [7], a bar for every report.**

```python
from matplotlib.patches import Patch  # a coloured square for the legend

ENGINE_COLOURS = {"Wolfram": "#2a78d6", "Python": "#eb6834", "Rust": "#1baf7a",
                  "lead": "#eda100"}
ENGINE_NAMES = {"Wolfram": "Wolfram Language", "Python": "Python",
                "Rust": "Rust", "lead": "Python, the lead's independent checks"}
```

The coloured squares of the legend (as in In [3] of Notebook 00b), a colour for each engine and its full name for the legend.

```python
fig, ax = plt.subplots(figsize=(6.4, 7.8))
rows = np.arange(len(REPORTS))[::-1]  # the first report at the top
for row, (path, engine) in zip(rows, REPORTS):
    total = counted[path][1]
    ax.barh(row, total, height=0.72, color=ENGINE_COLOURS[engine])
    ax.text(total + 1.5, row, str(total), va="center", fontsize=9)
```

A tall figure, one row per report. `np.arange(27)` is 0 to 26, and `[::-1]` reverses it (a step of $-1$), so that the first report gets the highest row and stands at the top. `ax.barh` draws a horizontal bar of the given length in the given row, coloured by the engine; `ax.text` writes the number just after the end of the bar.

```python
# The name of each report without its folder and without the ending .json:
names = [path.rsplit("/", 1)[1].removesuffix(".json") for path, _ in REPORTS]
ax.set_yticks(rows, labels=names, fontsize=9)
ax.set_xlim(0, 112)
ax.grid(False, axis="y")  # vertical grid lines only
ax.set_xlabel("number of checks in the report (every one has the verdict PASS)")
ax.set_title(f"The {len(REPORTS)} verifier reports of the Revision record: "
             f"{all_checks} checks")
ax.legend(handles=[Patch(color=ENGINE_COLOURS[e], label=ENGINE_NAMES[e])
                   for e in ENGINE_COLOURS], loc="lower right", fontsize=8)
```

`rsplit("/", 1)[1]` keeps the part after the last `/`, the file name, and `removesuffix` removes the ending. The names label the rows; the horizontal axis runs from 0 to 112 (room for the longest bar and its number); only vertical grid lines are drawn; the title contains the total; the legend names the four engines.

```python
# The report with the most checks, and its file name without the folders.
largest = max((path for path, _ in REPORTS), key=lambda path: counted[path][1])
largest_name = largest.rsplit("/", 1)[1]
n_wolfram, n_python, n_rust, n_lead = (engine_totals[engine] for engine in
                                       ("Wolfram", "Python", "Rust", "lead"))
totals_text = (f"{n_wolfram} Wolfram Language, {n_python} Python, {n_rust} Rust "
               f"and {n_lead} lead checks")
```

`max(..., key=...)` returns the path whose value under the key function is largest; `lambda path: counted[path][1]` is a function without a name that gives the total of a report. The four engine totals are unpacked into four names and written into a sentence for the caption, so that the caption always states the counts of the record as it is.

```python
save_figure(fig, "checks_by_report",
            r"The number of checks in each of the 27 verifier reports of the "
            r"Revision record (horizontal axis, a count; one bar per report, "
            r"named on the vertical axis and grouped by folder: algebra, theory, "
            r"field equations for $a_4$, GKD and Lovelock, Kohn-Sham, pairing, "
            r"lead checks). The colour gives the engine: blue Wolfram Language, "
            r"orange Python, aqua Rust, yellow the lead's independent Python "
            f"checks. All {all_checks} checks ({totals_text}) have the verdict "
            f"PASS; the largest report is {largest_name} with "
            f"{counted[largest][1]} checks.")
```

The figure `00c_1_checks_by_report.png` with its caption, partly raw strings and partly f-strings (each piece of the joined caption has its own prefix). What Figure 00c.1 shows: one bar per report, grouped by folder from the algebra at the top to the lead's checks at the bottom; the longest bar belongs to the report that the caption names (the Wolfram pairing report when this chapter was written), and every colour occurs, so every engine contributes.

**In [8], two independent engines.**

```python
SUBJECTS = [  # (subject, Wolfram report, Python report)
    ("the gammas, Pin(4,4), Spin(4,4)", "algebra/reports/wolfram-algebra.json",
     "algebra/reports/python-algebra.json"),
```

The list `SUBJECTS` names eight subjects, each with its Wolfram report and its independent Python report (paths without `Revision/`): the gammas, the field theory, the scope of the non-triviality, the field equations for $a_4$, GKD and the Lovelock tensors, the Kohn-Sham theory, the pairing theorems T1, T2 and Q, and the theorem T3. Its other lines have the form of these two.

```python
say("subject                              Wolfram  Python")
wolfram_numbers, python_numbers = [], []
for subject, wolfram, python in SUBJECTS:
    wolfram_numbers.append(counted["Revision/" + wolfram][1])
    python_numbers.append(counted["Revision/" + python][1])
    say(f"{subject:36} {wolfram_numbers[-1]:7d} {python_numbers[-1]:7d}")
```

For each subject the totals of its two reports are taken from `counted` and printed: the table of Out [8]. `[-1]` is the entry just appended.

```python
fig, ax = plt.subplots(figsize=(7.0, 5.0))
rows = np.arange(len(SUBJECTS))[::-1]
height = 0.38  # two bars in each row
ax.barh(rows + height / 2, wolfram_numbers, height, color="#2a78d6",
        edgecolor="white", linewidth=1.5, label="Wolfram Language verifier")
ax.barh(rows - height / 2, python_numbers, height, color="#eb6834",
        edgecolor="white", linewidth=1.5, label="Python verifier (sympy)")
for row, w, p in zip(rows, wolfram_numbers, python_numbers):
    ax.text(w + 1.5, row + height / 2, str(w), va="center", fontsize=8)
    ax.text(p + 1.5, row - height / 2, str(p), va="center", fontsize=8)
```

Two bars in each row, the Wolfram bar half a bar height above the middle of the row and the Python bar half a bar height below it; the numbers are written after the ends of the bars.

```python
ax.set_yticks(rows, labels=[subject for subject, _, _ in SUBJECTS])
ax.set_xlim(0, 112)
ax.grid(False, axis="y")
ax.set_xlabel("number of checks (every one has the verdict PASS)")
ax.set_title("Eight subjects, each checked by two independent verifiers")
ax.legend(loc="lower right")
save_figure(fig, "two_verifiers",
            r"For each of eight subjects of the Revision record (vertical axis), "
            r"the number of checks of its Wolfram Language verifier (blue, upper "
            r"bar) and of its independent Python verifier (orange, lower bar); "
            r"horizontal axis a count. The two verifiers share no code; each also "
            r"checks statements that the other does not, so the numbers differ. "
            f"Together they hold {sum(wolfram_numbers)} Wolfram and "
            f"{sum(python_numbers)} Python checks, all PASS.")
```

Labels, title, legend and the figure `00c_2_two_verifiers.png`. What Figure 00c.2 shows: every subject has two bars, so every subject was checked twice, in two languages; the bars differ in length because the two verifiers were written independently and test partly different statements.

```python
report("checks of the Wolfram verifiers of the eight subjects", sum(wolfram_numbers))
report("checks of the Python verifiers of the eight subjects", sum(python_numbers))
check(all(w > 0 and p > 0 for w, p in zip(wolfram_numbers, python_numbers)),
      "each of the eight subjects has a Wolfram and a Python verifier")
```

The two sums are printed, and the check requires a nonzero number of checks in both verifiers of every subject.

**In [9], the honesty ledger.**

```python
R = "Revision/"
LEDGER = [  # (statement, label, note, the reports that verify it)
    ("the gammas, C, Gamma, B; Pin(4,4) and Spin(4,4)", "PROVED", "",
     [R + "algebra/reports/wolfram-algebra.json",
      R + "algebra/reports/python-algebra.json"]),
```

The list `LEDGER` holds the sixteen rows of the table of Section 0.18, each as a group of four: the statement, the label, the note (an empty string `""` for the rows that have reports), and the list of the reports. The rows 13 to 16 have an empty list of reports and a note:

```python
    ("a time-varying dark sector from the fields", "HYPOTHESIS",
     "to be investigated; no result yet", []),
    ("our universe has a partner of opposite charge", "HYPOTHESIS",
     "the T1 maps exist; that a partner exists is not shown", []),
    ("the big bang creates universes in pairs", "OPEN",
     "not proved: no creation process, rate or amplitude", []),
    ("the theory explains matter over antimatter", "OPEN",
     "the theory as built does not explain it", []),
]
```

The rows 2 to 12 have the same form as row 1, with the statements, labels and reports of the table of Section 0.18. The four entries without reports are the honest answers of Section 0.2, written as data, so that the computer can check them.

```python
say("row label       passed of all  statement")
row_totals = []
for number, (statement, label, note, paths) in enumerate(LEDGER, 1):
    passed = sum(counted[path][0] for path in paths)
    total = sum(counted[path][1] for path in paths)
    row_totals.append(total)
    say(f"{number:3d} {label:10} {passed:7d} of {total:3d}  {statement}")
```

`enumerate(LEDGER, 1)` numbers the rows from 1. For each row, the passed checks and the checks of its reports are added (a sum over an empty list is 0) and a line of the table of Out [9] is printed.

```python
say("The notes of the rows without a report:")
for number, (statement, label, note, paths) in enumerate(LEDGER, 1):
    if note:  # only the HYPOTHESIS and OPEN rows have a note
        say(f"{number:3d} {label:10} {note}")
```

The notes of the four rows without a report are printed below the table (a non-empty string counts as true in `if`).

```python
used = sorted(path for _, _, _, paths in LEDGER for path in paths)
check(used == sorted(path for path, _ in REPORTS),
      "every one of the 27 reports belongs to exactly one row of the ledger")
```

`used` is the sorted list of all reports named in all rows (a comprehension with two `for` parts runs through the rows and, inside each row, through its reports). It must equal the sorted list of the 27 reports: every report appears, and none twice (a report named twice would appear twice in `used`).

```python
check(all((label in ("HYPOTHESIS", "OPEN")) == (paths == []) == (note != "")
          and all(counted[p][0] == counted[p][1] for p in paths)
          for _, label, note, paths in LEDGER),
      "rows with a report have only PASS checks; OPEN and HYPOTHESIS rows have none")
```

For every row, three statements must be all true or all false: the label is HYPOTHESIS or OPEN; the row has no report; the row has a note. And every report of the row must have only passed checks.

```python
labels = [label for _, label, _, _ in LEDGER]
check([labels.count(name) for name in
       ("PROVED", "COMPUTED", "ASSUMED", "HYPOTHESIS", "OPEN")] == [10, 1, 1, 2, 2],
      "the ledger: 10 PROVED, 1 COMPUTED, 1 ASSUMED, 2 HYPOTHESIS and 2 OPEN rows")
```

The labels are counted: ten rows PROVED, one COMPUTED, one ASSUMED, two HYPOTHESIS and two OPEN. Out [9] ends with three PASS lines.

**In [10], the ledger as a picture.**

```python
LABEL_COLOURS = {"PROVED": "#2a78d6", "COMPUTED": "#eb6834", "ASSUMED": "#1baf7a"}
fig, ax = plt.subplots(figsize=(7.6, 8.0))
rows = np.arange(len(LEDGER))[::-1]  # the first row of the ledger at the top
```

A colour for each label that has reports, a tall figure, and the row positions with the first row at the top.

```python
for number, row, (statement, label, note, paths), total in zip(
        range(1, len(LEDGER) + 1), rows, LEDGER, row_totals):
    # The statement is written just above its bar (va="bottom": the text starts
    # at the given height and extends upwards).
    ax.text(0, row + 0.26, f"{number}. {statement}", va="bottom", fontsize=9.5)
    if total > 0:
        ax.barh(row, total, height=0.42, color=LABEL_COLOURS[label])
        ax.text(total + 2, row, f"{total} checks: {label}", va="center",
                fontsize=9)
    else:  # no report: the label and the note, in grey
        ax.text(0, row, f"{label}: {note}", va="center", fontsize=9,
                color="#52514e")
```

`zip` runs through four lists together: the row numbers 1 to 16, the positions, the rows of the ledger and their totals. For each row the statement is written just above the place of its bar. A row with checks gets a bar of that length in the colour of its label, with the number and the label after it; a row without checks gets its label and its note in grey instead.

```python
ax.set_yticks([])  # the statements are written above the bars instead
ax.set_xlim(0, 232)
ax.set_ylim(-0.6, len(LEDGER) - 0.1)
ax.grid(False, axis="y")
ax.set_xlabel("number of checks in the reports of the row (all PASS)")
ax.set_title("The honesty ledger at a glance")
ax.legend(handles=[Patch(color=colour, label=label_name)
                   for label_name, colour in LABEL_COLOURS.items()],
          loc="lower right", fontsize=9)
```

No labels on the vertical axis (the statements stand above the bars); the limits leave room for the longest bar and its text and for the statement of the top row; the legend names the three colours.

```python
save_figure(fig, "ledger",
            r"The honesty ledger of the book at a glance: one row per main "
            r"statement (written above its bar), the length of its bar the number of "
            r"checks in the reports that verify it (horizontal axis, a count), the "
            r"colour its label: blue PROVED, orange COMPUTED, aqua ASSUMED. The "
            r"ASSUMED row has five checks, which show why the Kohn-Sham history of "
            r"$a_4$ must be assumed. The last four rows have no bar, because no "
            r"check of the record establishes them: two hypotheses (a time-varying "
            r"dark sector, and a partner universe of opposite charge) and two open "
            r"questions (that the big bang creates universes in pairs, which is not "
            r"proved, and the excess of matter over antimatter, which the theory as "
            r"built does not explain).")
```

The figure `00c_3_ledger.png`. What Figure 00c.3 shows: twelve bars, ten blue, one orange (the Kohn-Sham numbers) and one short aqua bar (the prescribed background), and four rows without a bar at the bottom: the two hypotheses and the two open questions. The picture makes the honesty rule visible: a statement without checks is never drawn as if it had them.

**In [11], what the pairing record does not establish.**

```python
PAIRING = "Revision/pairing/reports/python-pairing.json"
not_established = read_report(PAIRING)["not_established"]  # a list of sentences
for number, sentence in enumerate(not_established, 1):
    say(f"{number:2d}. {sentence}")
check_reproduces(len(not_established) == 12
                 and not_established[0].startswith("No creation process"),
                 "the pairing record lists 12 things it does not establish, "
                 "the first: no creation process",
                 f"{PAIRING}, key not_established")
```

The Python pairing report holds, under its key `not_established`, a list of sentences; the loop prints them numbered from 1 (Out [11]). The check requires twelve sentences, the first beginning with No creation process. In plain words, the twelve say: nothing in the equations creates a universe or a pair; no rate, probability or amplitude is derived; no conservation law forces pairing, and a single universe is an equally valid solution; the zero total of a T1 pair is an identity for one field configuration and its image, not a cancellation between two independently quantised universes; T2 does not reverse the energy-momentum tensor; the Z2 mirror is ASSUMED; the back-reaction on gravity is not part of the theorems; nothing forces the partner to exist; T1 pairs $(m, \lambda)$ with $(-m, -\lambda)$, not with $(-m, \lambda)$; a positive-norm quantum state space is not established by the theorems; the edge $z = \pi/2$ is a degenerate surface of the metric with no derived junction condition; and the Kohn-Sham level T3 is proved separately, with its own hypotheses.

**In [12], how a fingerprint reacts to a change.**

```python
def text_fingerprint(text):
    """The sha256 fingerprint of a text (encoded as UTF-8 bytes)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
```

`text.encode("utf-8")` turns the text into its bytes, `hashlib.sha256` computes the fingerprint of the bytes, and `.hexdigest()` writes it as 64 hexadecimal characters.

```python
for text in ("Universes in Pairs", "Universes in pairs"):
    digest = text_fingerprint(text)
    say(f"{text}:")
    say(f"    {digest}")
```

Two texts that differ only in the capital or small letter p. Out [12] shows their fingerprints: they have nothing visible in common.

```python
SENTENCE = ("The rule above every other rule of this book is honesty: it never "
            "writes proved for a statement that is not proved.")
original = text_fingerprint(SENTENCE)
changed_characters = []  # for each position: how many of the 64 characters change
for position in range(len(SENTENCE)):
    letter = SENTENCE[position]
    altered = SENTENCE[:position] + chr(ord(letter) + 1) + SENTENCE[position + 1:]
    new = text_fingerprint(altered)
    changed_characters.append(sum(1 for a, b in zip(original, new) if a != b))
counts = np.array(changed_characters)
```

A sentence of 115 characters and its fingerprint. For every position, `ord(letter)` is the number of the character in the computer's alphabet (for example 97 for a), `chr(... + 1)` is the next character (b), and `SENTENCE[:position] + ... + SENTENCE[position + 1:]` is the sentence with that one character replaced (`[:position]` is the part before it, `[position + 1:]` the part after it). The fingerprint of the altered sentence is compared with the original character by character (`zip` pairs the two strings), and the number of differing characters is stored. `counts` is the array of the 115 numbers.

```python
report("characters of the sentence", len(SENTENCE))
report("changed characters of the fingerprint: smallest, mean, largest",
       f"{counts.min()}, {counts.mean():.2f}, {counts.max()}")
```

Out [12]: 115 characters; the smallest number of changed characters is 54, the mean 60.03, the largest 64. The mean is what Section 0.18 derived for a random string, 60.

```python
values, how_often = np.unique(counts, return_counts=True)  # each count, how often
fig, ax = plt.subplots()
ax.bar(values, how_often, width=0.8, color="#2a78d6", edgecolor="white",
       linewidth=1.5, label="one-character changes of the sentence")
ax.axvline(60, color="black", linewidth=1.2, linestyle=":",
           label="expected for a random fingerprint: 60")
ax.set_xlim(-1, 65)
```

`np.unique(..., return_counts=True)` returns the different values that occur and how often each occurs: a **histogram**. The bars are drawn at those values; `ax.axvline(60, ...)` draws a dotted vertical line at 60; the horizontal axis shows the whole range from 0 to 64, so that the empty left part is visible.

```python
# "\n" inside a string starts a new line of the text.
ax.text(3, 0.55 * how_often.max(), "a fingerprint that changed only a little\n"
        "would give a bar on this side: none did", color="#52514e", fontsize=9)
ax.set_xlabel("number of the 64 characters of the fingerprint that change")
ax.set_ylabel("number of changed sentences")
ax.set_title("Change one character, and the fingerprint changes completely")
ax.legend(loc="upper left")
```

A note written into the empty left part of the picture, the labels, the title and the legend.

```python
save_figure(fig, "fingerprints",
            r"How much a sha256 fingerprint changes when one character of a text "
            r"changes: for each of the 115 characters of one sentence, the "
            r"character was replaced by the next one and the number of the 64 "
            r"hexadecimal characters of the fingerprint that changed was counted; "
            r"horizontal axis that number (0 to 64), vertical axis how many of the "
            r"115 altered sentences gave it. Every change altered between 54 and 64 "
            r"of the 64 characters, on average 60.03, as for a random string "
            r"(dotted line at 60): no small change of a file can leave its "
            r"fingerprint nearly the same.")
check(counts.min() >= 32 and abs(counts.mean() - 60.0) < 1.0,
      "every one-character change alters more than half of the fingerprint")
```

The figure `00c_4_fingerprints.png`, and a check: every change alters at least 32 of the 64 characters, and the mean lies within 1 of 60. What Figure 00c.4 shows: all bars stand close to the dotted line at 60, and the left half of the picture is empty: no one-character change left a fingerprint nearly unchanged.

**In [13], the fingerprints recorded by the reports.**

```python
def file_fingerprint(path):
    """The sha256 fingerprint of the bytes of the repository file path."""
    return hashlib.sha256(repository_file(path).read_bytes()).hexdigest()
```

As `text_fingerprint`, but for the bytes of a file of the repository (`read_bytes` reads them unchanged).

```python
RECORDED = []  # (report, file, recorded fingerprint)
GKD = "Revision/gkd_lovelock/results/wolfram-gkd-report.json"
gkd = read_report(GKD)
for path, value in {**gkd["inputSha256"], **gkd["sourceSha256"]}.items():
    RECORDED.append((GKD, path, value))
LOVELOCK = "Revision/gkd_lovelock/results/python-lovelock-report.json"
for name, value in read_report(LOVELOCK)["inputsSha256"].items():
    RECORDED.append((LOVELOCK, "Revision/gkd_lovelock/results/" + name, value))
```

The list `RECORDED` collects groups of three: the report, the file and the fingerprint the report recorded for it. The Wolfram report of GKD and the Lovelock tensors stores two dictionaries from file paths to fingerprints; `{**a, **b}` makes one dictionary of both, and all 15 entries are collected. The Python Lovelock report stores 2 more, under file names without the folder, which is added in front.

```python
IN_DETAILS = [  # (report, check, the file whose fingerprint the detail holds)
    ("ks-theory-wolfram.json", "fixture_input", "algebra/gammas.json"),
    ("ks-theory-python.json", "fixture_input", "algebra/reports/python-gammas.json"),
    ("ks-reference.json", "theory_input_coefficients", "kohn_sham/ks-theory.json"),
    ("ks-rust-solver.json", "theory_input_coefficients", "kohn_sham/ks-theory.json"),
    ("ks-rust-solver.json", "gamma_fixture_numeric", "algebra/gammas.json"),
    ("ks-rust-solver.json", "thermo_mu_vs_40digit_roots",
     "kohn_sham/solver/tools/mermin-roots-40digit.json"),
    ("ks-crosscheck.json", "problem_definition_identical",
     "kohn_sham/ks-theory.json"),
]
```

Seven more fingerprints are written inside the detail texts of checks of five Kohn-Sham reports; this list names, for each, the report, the check and the file.

```python
for name, check_name, path in IN_DETAILS:
    report_path = "Revision/kohn_sham/reports/" + name
    detail = next(entry["detail"] for entry in read_report(report_path)["checks"]
                  if entry["name"] == check_name)
    value = re.search(r"\(sha256 ([0-9a-f]{16,64})\)", detail).group(1)
    RECORDED.append((report_path, "Revision/" + path, value))
```

For each, the detail of the named check is read, and the regular expression finds the fingerprint in it: `\(` and `\)` are the round brackets themselves (a backslash makes a special character ordinary), `[0-9a-f]` is one hexadecimal character, and `{16,64}` means 16 to 64 of them. `re.search` finds the first match, and `.group(1)` is the part in the inner brackets, the fingerprint (complete, or only its first 16 characters).

```python
changed = []  # files whose fingerprint today differs from the recorded one
for report_path, path, value in RECORDED:
    same = file_fingerprint(path).startswith(value)  # a full or shortened value
    if not same:
        changed.append(path)
    status = "same" if same else "CHANGED"
    short_path = path.removeprefix("Revision/")  # the path without Revision/
    report_name = report_path.rsplit("/", 1)[1]  # the file name of the report
    say(f"{status:7} {short_path:52} {report_name}")
```

For each of the 24, the fingerprint of today's file is computed and must begin with the recorded value (`startswith` accepts a shortened value, and a complete value only if the two are equal). One line per fingerprint is printed: the 24 lines of Out [13], all reading same.

```python
recorded_gammas = next(value for report_path, path, value in RECORDED
                       if report_path.endswith("ks-theory-wolfram.json"))
today_gammas = file_fingerprint("Revision/algebra/gammas.json")
say("Revision/algebra/gammas.json, recorded in ks-theory-wolfram.json and today:")
say(f"    {recorded_gammas}")
say(f"    {today_gammas}")
```

One example printed in full: the fingerprint of the file of the gammas as recorded by the Wolfram Kohn-Sham verifier, and as computed today; the two lines of 64 characters in Out [13] are identical.

```python
report("recorded fingerprints compared", len(RECORDED))
check_reproduces(len(RECORDED) == 24 and changed == [],
                 "the 24 recorded fingerprints equal the files of today",
                 f"{GKD}, keys inputSha256 and sourceSha256, and five further reports")
```

The check requires 24 recorded fingerprints and no changed file. So every one of these reports was computed from exactly the files that are in the repository today.

**In [14], the last check.**

```python
figure_names = ["00c_1_checks_by_report.png", "00c_2_two_verifiers.png",
                "00c_3_ledger.png", "00c_4_fingerprints.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "the four figure files of this notebook exist")
all_checks_passed()
```

As in Notebook 00b: the four figure files must exist, and the last line prints ALL 14 CHECKS PASSED (notebook 00c): one check each in In [2], In [8], In [11], In [12], In [13] and In [14], three in In [5], two in In [6] and three in In [9].

### 0.22 Why every run gives the same bytes

Section 0.9 promised that every notebook of the book, run a second time, gives exactly the same bytes: the same printed text, the same pictures, the same files. The Revision record makes the same promise for its long computations. This section explains why such a promise can be kept at all, and what has to be done to keep it. It also explains why two *different* computations of the same number, for example two solvers, never agree exactly, and why their comparison needs a tolerance.

**A computer is deterministic.** Given the same program and the same input, it performs the same steps and gets the same result. Two runs of a careless notebook can still print different text, for five reasons: (1) it prints the time or the date; (2) it uses random numbers without a fixed starting point; (3) it prints the names of a set, or the files of a folder, in an order that can change from run to run; (4) it adds numbers in an order that depends on the computer, and the order changes the last digits of a sum; (5) it writes files with the line ends of the operating system. The notebooks of the book avoid all five. We now look at each, beginning with the way a computer stores numbers, because reason (4) comes from there.

**Binary fractions.** We write numbers in the decimal system, with the ten digits 0 to 9 and powers of 10. A computer writes them in the **binary** system, with the two digits 0 and 1 (each one a **bit**) and powers of 2: binary 101 means $1 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 = 5$, and binary 0.11 means $1 \cdot \frac{1}{2} + 1 \cdot \frac{1}{4} = \frac{3}{4}$. A binary fraction with finitely many digits is a whole number divided by a power of 2. The number $0.1 = 1/10$ is not of this kind. Suppose it were, $1/10 = n/2^k$ with whole numbers $n$ and $k$:

$$
2^k = 10\, n
$$

(multiply both sides by $10 \cdot 2^k$),

$$
2^{k-1} = 5\, n
$$

(divide both sides by 2, using $10 = 2 \cdot 5$). Then 5 would divide a power of 2, which is impossible, because the only prime number that divides a power of 2 is 2 itself (every whole number is a product of prime numbers in exactly one way; this school fact is used here without proof). So the binary expansion of $1/10$ never ends, just as the decimal expansion $1/3 = 0.333\ldots$ never ends, and the computer has to cut it off.

**Floating-point numbers.** Python's numbers with a fraction part (the type `float`, and numpy's `float64`) are **floating-point numbers**: each is a whole number $m$ of exactly 53 binary digits, that is $2^{52} \le m < 2^{53}$, times a power of two, $x = m \cdot 2^{e}$ (and the same with a minus sign; zero is stored separately). The 53 binary digits correspond to about 16 decimal digits, since $2^{53} = 9007199254740992$ has 16 digits. A number that is not of this form is replaced by the nearest one that is: this is **rounding**. If it lies exactly halfway between two neighbours, the rule is to take the neighbour whose $m$ is even (**round half to even**).

**How 0.1 is stored.** The number 0.1 lies between $2^{-4} = 0.0625$ and $2^{-3} = 0.125$; so it must be written as $m \cdot 2^{-4-52} = m \cdot 2^{-56}$ with a 53-digit $m$:

$$
m = 0.1 \cdot 2^{56} = 7205759403792793.6
$$

(the condition $x = m \cdot 2^{-56}$ solved for $m$; $2^{56} = 72057594037927936$),

$$
m \approx 7205759403792794
$$

(rounding to the nearest whole number; it lies between $2^{52} = 4503599627370496$ and $2^{53}$, as it must),

$$
0.1 \approx \frac{7205759403792794}{2^{56}} = \frac{3602879701896397}{2^{55}} = 0.1000000000000000055511\ldots
$$

(the numerator is even, so numerator and denominator can be divided by 2). The stored number is larger than $1/10$ by about $5.6 \times 10^{-18}$. Notebook 00d prints exactly this fraction and all its decimal digits.

**Why $0.1 + 0.2$ is not $0.3$.** Doubling changes only the power of 2, so 0.2 is stored exactly twice the stored 0.1:

$$
0.2 \approx \frac{3602879701896397}{2^{54}} = \frac{7205759403792794}{2^{55}}
$$

(multiply the stored 0.1 by 2, then write it over $2^{55}$ by multiplying numerator and denominator by 2). The number 0.3 lies between $2^{-2}$ and $2^{-1}$, so it is stored as $m \cdot 2^{-54}$ with $m = 0.3 \cdot 2^{54} = 5404319552844595.2$, rounded:

$$
0.3 \approx \frac{5404319552844595}{2^{54}}
$$

(the same steps as for 0.1). The sum of the two stored numbers is

$$
\frac{3602879701896397}{2^{55}} + \frac{7205759403792794}{2^{55}} = \frac{10808639105689191}{2^{55}}
$$

(fractions with the same denominator are added by adding their numerators). This sum lies between $2^{-2}$ and $2^{-1}$, so it must be stored as $m \cdot 2^{-54}$, with

$$
m = \frac{10808639105689191}{2} = 5404319552844595.5
$$

(the sum written over $2^{54}$: divide the numerator by 2). This lies exactly halfway between 5404319552844595 and 5404319552844596, and round half to even chooses the even one:

$$
0.1 + 0.2 \approx \frac{5404319552844596}{2^{54}}
$$

(round half to even). Comparing with the stored 0.3, the numerators differ by 1, so

$$
(0.1 + 0.2) - 0.3 = \frac{1}{2^{54}} = 2^{-54} = 5.55 \times 10^{-17}
$$

(subtraction of fractions with the same denominator). Python therefore prints $0.1 + 0.2$ as 0.30000000000000004, and the question whether $0.1 + 0.2$ equals 0.3 is answered False. Status: PROVED (by the exact arithmetic above); Notebook 00d checks it.

**Machine epsilon and the gaps between numbers.** The number 1 is stored with $m = 2^{52}$ and $e = -52$; the next larger stored number has $m = 2^{52} + 1$, so it is $1 + 2^{-52}$. The gap

$$
\epsilon = 2^{-52} = 2.22 \times 10^{-16}
$$

is called the **machine epsilon**. The number $1 + \epsilon/2 = 1 + 2^{-53}$ lies exactly halfway between 1 and $1 + \epsilon$; round half to even picks 1 (its $m = 2^{52}$ is even), so $1 + 2^{-53}$ is stored as 1. More generally, every stored number $x$ between $2^{k}$ and $2^{k+1}$ (with $2^k \le x < 2^{k+1}$) has the power $2^{k-52}$, so the gap to the next stored number is $2^{k-52}$. Dividing by $x$:

$$
\frac{\mathrm{gap}}{x} = \frac{2^{k-52}}{x} \le \frac{2^{k-52}}{2^{k}} = 2^{-52} = \epsilon
$$

(a fraction becomes larger or stays equal when its denominator is replaced by a smaller or equal one, here $x \ge 2^k$), and

$$
\frac{\mathrm{gap}}{x} > \frac{2^{k-52}}{2^{k+1}} = 2^{-53} = \frac{\epsilon}{2}
$$

(the same rule with $x < 2^{k+1}$). So every stored number carries the same relative accuracy, between $\epsilon/2$ and $\epsilon$, about 16 significant decimal digits, whatever its size. A difference of one gap is called one **unit in the last place**, one **ulp**.

**The order of a sum changes the last digits.** Every addition rounds its result. Rounding is deterministic, but it depends on the order of the operations. The smallest example:

$$
(1 + 2^{-53}) + 2^{-53} = 1 + 2^{-53} = 1
$$

(the bracket is computed first; it is the halfway case above and is rounded to 1; then the same happens again), while

$$
1 + (2^{-53} + 2^{-53}) = 1 + 2^{-52}
$$

(the bracket is computed first: $2^{-53} + 2^{-53} = 2 \cdot 2^{-53} = 2^{-52}$ exactly, because doubling changes only the power of 2; and $1 + 2^{-52}$ is a stored number). The same three numbers, added in two orders, give two different stored results. In a long sum the effect grows. Notebook 00d adds the million numbers $1/k^2$, $k = 1, \ldots, 10^6$, **forwards** (the largest first) and **backwards** (the smallest first). Forwards, every small term is added to a running total of about 1.6 and is rounded to the gap of that total; backwards, small terms are added to small totals, which loses less. Measured against the exactly rounded sum, the forward sum is wrong by up to 196 ulps and the backward sum by at most 1 ulp; numpy's own way of adding, in pairs and pairs of pairs, by at most 3 ulps (COMPUTED, Notebook 00d). Different computers, or the same computer using several processor cores, may add in different orders; this is why the book always adds in a fixed order.

**The error of the method is a different thing.** The infinite sum $1 + 1/4 + 1/9 + \cdots$ is $\pi^2/6$ (a theorem of Euler, 1734, used here without proof). Stopping after $N$ terms leaves out the tail $\sum_{k > N} 1/k^2$, and this is not a rounding error but an error of the method. Its size follows from comparing each term with an integral. The function $1/x^2$ decreases, so on the interval from $k - 1$ to $k$ it is larger than its value at the right end:

$$
\frac{1}{k^2} < \int_{k-1}^{k} \frac{dx}{x^2}
$$

(the area under a decreasing curve over an interval of length 1 is larger than the curve's smallest value there, $1/k^2$), and on the interval from $k$ to $k + 1$ it is smaller than its value at the left end:

$$
\frac{1}{k^2} > \int_{k}^{k+1} \frac{dx}{x^2}
$$

(the area is smaller than the largest value, $1/k^2$). Adding these inequalities for $k = N + 1, N + 2, \ldots$ joins the intervals into one:

$$
\int_{N+1}^{\infty} \frac{dx}{x^2} < \sum_{k > N} \frac{1}{k^2} < \int_{N}^{\infty} \frac{dx}{x^2}
$$

(sums of inequalities, and integrals over adjacent intervals add up to the integral over their union), and since $\int_a^\infty dx/x^2 = \left[-1/x\right]_a^\infty = 1/a$,

$$
\frac{1}{N+1} < \frac{\pi^2}{6} - \sum_{k=1}^{N} \frac{1}{k^2} < \frac{1}{N}
$$

(the fundamental theorem of calculus with the antiderivative $-1/x$ of $1/x^2$, whose value goes to 0 as $x$ grows). For $N = 10^6$ the method error lies between $9.99999 \times 10^{-7}$ and $10^{-6}$; Notebook 00d measures $9.999995 \times 10^{-7}$, more than $10^{7}$ times larger than even the largest rounding difference of the sums (196 ulps of about $2.2 \times 10^{-16}$ each, that is about $4 \times 10^{-14}$).

**Tolerances.** Two runs of the same program in the same order agree byte for byte. Two *different* computations of the same quantity, such as two solvers, or one solver with two step sizes, agree only up to rounding and up to the errors of their methods. Such a comparison uses a **tolerance**: the largest difference that it accepts as agreement. The tolerance must be fixed *before* the comparison is made; a tolerance chosen after seeing the difference would prove nothing. The Revision record's Kohn-Sham solver was run with its canonical settings and again with refined settings (twice as many integration steps, tighter tolerances of its own, and one equation solved in another, exactly equivalent form that rounds along another path). The tolerances fixed in advance were $10^{-8}$ for energies, levels and thermodynamic quantities and $10^{-6}$ for profiles and derivatives. The eight measured largest differences are below their tolerances by factors (**margins**) between 4.7 and 7692 (COMPUTED: `Revision/kohn_sham/reports/ks-rust-determinism.json`, checks `refined_ground_energies` to `refined_heat_capacity`; the measured values are quoted by `Revision/kohn_sham/reports/ks-crosscheck.json`, key `rust_matrix_wide_uncertainties`).

**A negative control.** A **negative control** is a test that must detect a known error; if it does not, the test is useless. The record contains one that teaches a general lesson. An earlier version of the solver found the chemical potential $\mu$ (Chapter 13) with a method that was wrong by up to about $8 \times 10^{-10}$ in units of the mass $m$ in three thermal states, and it used that method in *both* runs. Both runs made the same rounding error, so their difference was tiny and hid the error. The present refined run finds $\mu$ along another rounding path, and its difference from the old result shows the error in full (`Revision/kohn_sham/reports/ks-rust-determinism.json`, check `refined_mermin_root_path`). Two computations that round the same way can agree with each other and both be wrong: a comparison is only as good as the independence of the two computations.

**Seeds.** A random-number generator of a computer is a formula that produces, step by step, numbers that look random. It starts from a number called the **seed**, and the same seed always gives the same sequence. The notebooks of the book use random numbers only from a generator with a fixed seed, so that every run draws the same numbers.

**The order of a set.** A Python **set** is an unordered collection of different things, written like `{"x1", "x2"}`. When Python prints a set, the order of its members depends on their **hash values**, numbers computed from the names with a secret key that Python chooses anew every time it starts, unless the **environment variable** `PYTHONHASHSEED` (a named setting that a program receives when it starts) fixes the key. The build of a notebook sets it to 0 and the check run to 1 (Section 0.9), so that a notebook that printed a set in its stored order would fail the check. The notebooks therefore sort every set before printing it.

**Line ends.** A text file ends each line with special bytes. Linux and macOS use one byte, LF (line feed, the number 10); Windows traditionally uses two, CR LF (carriage return 13, then line feed 10). The same two lines of text written with LF and with CR LF are different bytes, of different lengths and with different fingerprints. The book and the Revision record write every file with LF, on every operating system.

**Fingerprints of the results.** The two Kohn-Sham solvers of the record wrote, next to their result files, a **manifest**: a file that lists every result file with its sha256 fingerprint (Section 0.18). The record also ran each solver a second time and compared every file of the two runs byte for byte (`Revision/kohn_sham/reports/ks-rust-determinism.json`, check `repeat_byte_identical`; `Revision/kohn_sham/reports/ks-crosscheck.json`, check `reference_repeat_byte_identical`).

**Example: what could make two runs differ.** Notebook 00d shows each of these facts with a small experiment and reproduces the corresponding checks of the record: it prints how 0.1 is stored and checks the two facts derived above; draws the gaps between stored numbers; adds the million numbers $1/k^2$ in three orders; reads the eight tolerances of the Kohn-Sham solver with the measured differences and the negative control, and draws them; makes random walks with fixed seeds; runs Python twelve times with twelve hash seeds and prints the order of a set each time; shows the bytes of LF and CR LF line ends and confirms that no result file of the record has CR LF line ends; and computes 582 fingerprints and compares them with the two manifests. It draws six figures and ends with ALL 22 CHECKS PASSED (notebook 00d).

<!-- NOTEBOOK 00d -->

### 0.25 Line-by-line walk-through of Notebook 00d

The notebook has seventeen code cells, In [1] to In [17]. This section explains every line of each of them.

**In [1], the set-up cell.** It is the set-up cell of Notebook 00a, word for word, except that its comment lines hold the run instructions of Notebook 00d (Section 0.23) and the line `NOTEBOOK_ID = "00d"` names this notebook. Every line of its code is explained in Section 0.13. It prints Set-up of notebook 00d complete: repository folder found, helpers defined.

**In [2], how the computer stores 0.1.**

```python
import sys  # sys.stdout is the channel through which the notebook prints
from decimal import Decimal  # the exact decimal digits of a stored number
from fractions import Fraction  # a stored number as an exact fraction

import numpy as np  # arrays of numbers
```

Two modules of Python itself that look inside a stored number: `Fraction(x)` gives the exact fraction that the computer stores for the floating-point number `x`, and `Decimal(x)` all its decimal digits. Then `sys` and numpy, as before.

```python
def check_reproduces(condition, name, record):
    """check(condition, name, record=record), after sending the waiting output."""
    sys.stdout.flush()  # send every printed line that is still waiting
    check(condition, name, record=record)
```

The helper for checks that reproduce a Revision record, explained in Section 0.17 (In [2] of Notebook 00b).

```python
stored = Fraction(0.1)  # the fraction that the computer really stores for 0.1
say(f"0.1 is stored as the fraction {stored}")
say(f"    = {Decimal(0.1)}")
say(f"0.1 + 0.2 = {0.1 + 0.2!r}")
say(f"0.1 + 0.2 == 0.3 is {0.1 + 0.2 == 0.3}")  # == asks: exactly equal?
```

The first two lines of Out [2] print the stored fraction, 3602879701896397/36028797018963968 (the denominator is $2^{55}$), and its 55 decimal digits after the point, exactly the result of Section 0.22. `!r` inside the braces prints a number with as many digits as Python needs to identify the stored number uniquely: 0.30000000000000004. The fourth line asks whether $0.1 + 0.2$ is exactly equal to 0.3: False.

```python
difference = (0.1 + 0.2) - 0.3
report("(0.1 + 0.2) - 0.3", repr(difference))
check(stored == Fraction(3602879701896397, 2 ** 55),
      "0.1 is stored as 3602879701896397 / 2^55, not exactly as 1/10")
check(0.1 + 0.2 != 0.3 and difference == 2.0 ** -54,
      "0.1 + 0.2 differs from 0.3 by 2^-54 = 5.55e-17, one rounding step")
```

The difference is printed with `repr` (the same as `!r`): 5.551115123125783e-17, which means $5.551115123125783 \times 10^{-17}$. The two checks confirm the two results derived by hand in Section 0.22: the stored 0.1 is $3602879701896397/2^{55}$, and $(0.1 + 0.2) - 0.3$ is exactly $2^{-54}$ (`!=` means "is not equal to").

**In [3], the machine epsilon.**

```python
epsilon = float(np.finfo(np.float64).eps)  # the gap between 1 and the next number
report("machine epsilon", repr(epsilon))
say(f"1 + epsilon     == 1 is {1.0 + epsilon == 1.0}")
say(f"1 + epsilon / 2 == 1 is {1.0 + epsilon / 2 == 1.0}")
check(epsilon == 2.0 ** -52 and 1.0 + epsilon > 1.0 and 1.0 + epsilon / 2 == 1.0,
      "machine epsilon is 2^-52: 1 + 2^-52 is stored, 1 + 2^-53 rounds back to 1")
```

`np.finfo(np.float64)` describes numpy's 64-bit floating-point numbers, and its `.eps` is the machine epsilon, printed as 2.220446049250313e-16. Then $1 + \epsilon$ is not equal to 1 (False), while $1 + \epsilon/2$ is rounded back to 1 (True), the halfway case of Section 0.22. The check confirms all three facts.

**In [4], the gaps between neighbouring numbers.**

```python
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
x_values = np.logspace(-3.0, 6.0, 3000)  # 3000 numbers from 0.001 to 1000000
gaps = np.spacing(x_values)  # the gap from each number to the next larger one
for x in (1.0, 1000.0, 1.0e6):
    say(f"gap above {x:>9g}: {np.spacing(x):.3e}")
```

Four colours. `np.logspace(-3.0, 6.0, 3000)` makes 3000 numbers from $10^{-3}$ to $10^{6}$ whose logarithms are equally spaced, so that they spread evenly over a logarithmic axis. `np.spacing(x)` is the gap from $x$ to the next larger stored number. The loop prints the gaps at 1, 1000 and $10^6$: $2.220 \times 10^{-16}$, $1.137 \times 10^{-13}$ and $1.164 \times 10^{-10}$ (Out [4]). Each is about $\epsilon$ times the number: $1000$ lies between $2^9 = 512$ and $2^{10}$, so its gap is $2^{9-52} = 2^{-43} = 1.137 \times 10^{-13}$.

```python
fig, ax = plt.subplots()
# drawstyle="steps-post" draws each value as a flat step until the next x.
ax.plot(x_values, gaps, color=BLUE, linewidth=1.5, drawstyle="steps-post",
        label="gap to the next stored number")
ax.plot(x_values, epsilon * x_values, color="black", linestyle="--",
        linewidth=1.0, label=r"$\epsilon x$")
ax.plot(x_values, epsilon * x_values / 2, color="black", linestyle=":",
        linewidth=1.0, label=r"$\epsilon x / 2$")
ax.set_xscale("log")  # logarithmic horizontal axis
ax.set_yscale("log")  # logarithmic vertical axis
ax.set_xlabel(r"the number $x$")
ax.set_ylabel("gap to the next stored number")
ax.set_title("The gaps between neighbouring floating-point numbers")
ax.legend(loc="upper left")
```

The gaps are drawn as a staircase (each value as a flat step), together with the two straight lines $\epsilon x$ (dashed) and $\epsilon x/2$ (dotted) that Section 0.22 derived as the upper and lower bounds; both axes are logarithmic.

```python
save_figure(fig, "float_spacing",
            r"The gap between a floating-point number $x$ and the next larger "
            r"stored number (blue staircase) for $x$ from $10^{-3}$ to $10^{6}$, on "
            r"logarithmic axes (both pure numbers), with the lines $\epsilon x$ "
            r"(dashed) and $\epsilon x/2$ (dotted), $\epsilon = 2^{-52}$. The gap is "
            r"constant between two powers of 2 and doubles at each of them, so it "
            r"always lies between the two lines: every stored number carries about "
            r"16 significant digits, whatever its size.")
ratios = gaps / x_values  # the gap relative to the number
check(bool(np.all(ratios > epsilon / 2) and np.all(ratios <= epsilon))
      and np.spacing(1.0) == epsilon,
      "the gap lies between eps x / 2 and eps x at all 3000 points")
```

The figure `00d_1_float_spacing.png`, and the check of the bounds of Section 0.22 at all 3000 points: `np.all` is true when the comparison holds for every entry, and `bool` makes a plain truth value of it. What Figure 00d.1 shows: a staircase that climbs over nine powers of ten while staying between the two parallel lines; each step is flat between two powers of 2 and jumps up by a factor 2 at each of them.

**In [5], one sum in three orders.**

```python
import math  # math.fsum: the exactly rounded sum; math.pi

N_MAX = 10 ** 6
k = np.arange(1, N_MAX + 1, dtype=np.float64)  # 1, 2, ..., 1000000 as floats
terms = 1.0 / (k * k)  # the numbers 1/k^2
forward = np.add.accumulate(terms)  # all forward running totals
```

The module `math` of Python provides `math.fsum`, which adds stored numbers exactly and rounds only once, at the end (the **exactly rounded** sum), and $\pi$. `np.arange(1, N_MAX + 1, ...)` is the array 1, 2, ..., $10^6$ (the end is not included, hence the $+1$), as floating-point numbers; `terms` holds the million numbers $1/k^2$. `np.add.accumulate` adds them one after the other, starting with the first and largest, and returns every running total: `forward[n - 1]` is the forward sum of the first `n` terms.

```python
# 31 values of N, equally spaced on a logarithmic axis from 10 to 10^6.
n_values = np.unique(np.round(np.logspace(1.0, 6.0, 31)).astype(int))
ulps = {"forward": [], "backward": [], "pairwise": []}  # the errors in ulps
```

31 numbers of terms from 10 to $10^6$, rounded to whole numbers (`np.round`, then `.astype(int)`); `np.unique` sorts them and removes repetitions. The dictionary `ulps` will hold the three lists of errors.

```python
for n in n_values:
    exact = math.fsum(terms[:n])  # the exactly rounded sum of the first n numbers
    gap = np.spacing(exact)  # one ulp of the exact sum
    backward = np.add.accumulate(terms[:n][::-1])[-1]  # smallest number first
    ulps["forward"].append(float((forward[n - 1] - exact) / gap))
    ulps["backward"].append(float((backward - exact) / gap))
    ulps["pairwise"].append(float((np.sum(terms[:n]) - exact) / gap))
```

For each number of terms `n`: the exactly rounded sum of the first `n` terms (`terms[:n]`); one ulp of it; the backward sum, which adds the reversed list (`[::-1]`) and keeps the last running total (`[-1]`); and the errors of the three sums, each divided by the ulp, so that they are measured in ulps. `np.sum` adds in pairs, then pairs of pairs, and so on (**pairwise summation**).

```python
# The three sums of all 10^6 numbers, as plain Python floats (float(...)).
forward_million = float(forward[-1])
backward_million = float(np.add.accumulate(terms[::-1])[-1])
pairwise_million = float(np.sum(terms))
exact_million = math.fsum(terms)
say(f"forward  sum of 10^6 numbers: {forward_million!r}")
say(f"backward sum of 10^6 numbers: {backward_million!r}")
say(f"pairwise sum of 10^6 numbers: {pairwise_million!r}")
say(f"exactly rounded sum         : {exact_million!r}")
```

The four sums of all million terms, printed with every digit that identifies them: the forward sum 1.64493306684877, the backward and the pairwise sum 1.6449330668487263, and the exactly rounded sum 1.6449330668487265 (Out [5]). Forwards and backwards, the same numbers give different last digits.

```python
worst_forward = max(abs(u) for u in ulps["forward"])  # the largest size of error
worst_backward = max(abs(u) for u in ulps["backward"])
worst_pairwise = max(abs(u) for u in ulps["pairwise"])
report("largest forward error in ulps", f"{worst_forward:.0f}")
report("largest backward error in ulps", f"{worst_backward:.0f}")
report("largest pairwise error in ulps", f"{worst_pairwise:.0f}")
report("pi^2/6 minus the exact sum of 10^6 numbers",
       f"{math.pi ** 2 / 6 - exact_million:.6e}")
```

The largest size of each error over the 31 values of $N$: 196 ulps forwards, 1 ulp backwards, 3 ulps pairwise. The last RESULT line is the error of the method, $\pi^2/6$ minus the sum, $9.999995 \times 10^{-7}$, inside the bounds $1/(N+1)$ and $1/N$ derived in Section 0.22.

**In [6], the three errors drawn.**

```python
fig, ax = plt.subplots()
ax.plot(n_values, ulps["forward"], "o-", color=BLUE, markersize=4,
        label="forwards (largest number first)")
ax.plot(n_values, ulps["backward"], "s-", color=ORANGE, markersize=4,
        label="backwards (smallest number first)")
ax.plot(n_values, ulps["pairwise"], "^:", color=AQUA, markersize=4,
        label="pairwise (numpy's np.sum)")
ax.axhline(0.0, color="black", linewidth=0.8)  # the exactly rounded sum
ax.set_xscale("log")
ax.set_xlabel(r"number of terms $N$ of the sum $1 + 1/4 + \cdots + 1/N^2$")
ax.set_ylabel("error in units of the last place (ulps)")
ax.set_title("The same numbers added in different orders")
ax.legend(loc="upper left")
```

The three lists of errors against $N$ on a logarithmic horizontal axis: `"o-"` draws circles joined by lines, `"s-"` squares, `"^:"` triangles joined by a dotted line. `ax.axhline(0.0, ...)` draws a horizontal line at 0, the exactly rounded sum.

```python
save_figure(fig, "summation_order",
            r"The rounding error of the sum $1 + 1/4 + 1/9 + \cdots + 1/N^2$ in "
            r"units of the last place (vertical axis, ulps, the gap between "
            r"neighbouring stored numbers at the sum) against the number of terms "
            r"$N$ from 10 to $10^{6}$ (horizontal axis, logarithmic), measured from "
            r"the exactly rounded sum: forwards with the largest term first (blue "
            r"circles), backwards with the smallest term first (orange squares), "
            r"and pairwise as numpy adds (aqua triangles). The forward error grows "
            f"to {worst_forward:.0f} ulps, a relative error of a few times "
            r"$10^{-14}$; the backward error stays within "
            f"{worst_backward:.0f} ulp and the pairwise error within "
            f"{worst_pairwise:.0f} ulps. Same numbers, different order, different "
            r"last digits.")
```

The figure `00d_2_summation_order.png`; its caption takes the three worst errors from the computation. What Figure 00d.2 shows: the blue forward errors wander away from zero as $N$ grows, to almost 200 ulps, while the orange and aqua errors stay on the line at 0 within a few ulps.

```python
relative = max(abs(s - exact_million) for s in
               (forward_million, backward_million, pairwise_million)) / exact_million
report("largest relative difference of the three sums of 10^6 numbers",
       f"{relative:.2e}")
check(forward_million != backward_million,
      "forwards and backwards, the sums of the 10^6 numbers differ in the last digits")
check(worst_backward <= 1.0,
      "the backward sum is within one ulp of the exactly rounded sum for every N")
check(relative < 1e-13,
      "the three sums agree to a relative 1e-13: a tolerance of 1e-12 accepts all")
```

The largest distance of the three sums from the exactly rounded sum, divided by the sum (a **relative** difference): $2.65 \times 10^{-14}$. Three checks: the forward and the backward sum are different stored numbers; the backward sum is never more than 1 ulp off; and all three agree to a relative $10^{-13}$, so a check with a tolerance of $10^{-12}$ would accept each of them.

**In [7], the tolerances of the Revision record.**

```python
import re  # finds patterns in texts ("regular expressions")


def read_json(path):
    """The content of the JSON file path of the repository (dictionaries, lists)."""
    return json.loads(repository_file(path).read_text(encoding="utf-8"))
```

The module of regular expressions (explained in Section 0.21, In [6]) and a function that reads a JSON file of the repository.

```python
DETERMINISM = "Revision/kohn_sham/reports/ks-rust-determinism.json"
CROSS = "Revision/kohn_sham/reports/ks-crosscheck.json"
determinism_checks = {entry["name"]: entry for entry in read_json(DETERMINISM)["checks"]}
measured = read_json(CROSS)["rust_matrix_wide_uncertainties"]  # name -> difference
```

The determinism report of the Kohn-Sham solver and the cross-check report. `{entry["name"]: entry for entry in ...}` is a **dictionary comprehension**: it makes a dictionary from each check's name to the check, so that a check can be looked up by name. `measured` is a dictionary from the name of each of the eight comparisons to its measured largest difference, as the cross-check quotes it.

```python
SHORT_NAMES = {  # the check names of the record -> short names for the table
    "refined_ground_energies": "ground-state energies",
    "refined_ground_homo_lumo_gap": "level gaps",
    "refined_eigenvalues": "all Kohn-Sham levels",
    "refined_delta_scf": "excitation energies",
    "refined_profiles": "profiles",
    "refined_adiabatic_derivatives": "adiabatic derivatives",
    "refined_thermodynamics": "thermodynamics",
    "refined_heat_capacity": "heat capacity",
}
```

The eight checks of the comparison between the canonical and the refined run, each with a short name for the table (the quantities are explained in Chapters 14 and 15; here only their sizes matter).

```python
tolerances, quoted, verdicts = {}, {}, {}
say("quantity                measured   tolerance   margin")
for name, short in SHORT_NAMES.items():
    detail = determinism_checks[name]["detail"]
    verdicts[name] = determinism_checks[name]["verdict"]
    tolerances[name] = float(re.findall(r"tolerance (\S+)", detail)[-1])
    quoted[name] = f"{measured[name]:.3e}" in detail  # the same number in both files
    margin = tolerances[name] / measured[name]
    say(f"{short:22} {measured[name]:9.3e}   {tolerances[name]:9.0e}   {margin:7.1f}")
```

Three empty dictionaries, and a table header. For each comparison: the detail text and the verdict of the record's check; the tolerance, found with the pattern `tolerance (\S+)` (`\S+` is one or more characters that are not blanks, so it catches the number after the word tolerance; `[-1]` takes the last match, and `float` turns the text into a number); whether the measured number, written with four significant digits (`.3e`), occurs in the detail text too, so that both files state the same number; and the **margin**, the tolerance divided by the measured difference. The table of Out [7] shows, for example, the ground-state energies: measured $1.901 \times 10^{-12}$, tolerance $10^{-8}$, margin 5260.4; the smallest margin, 4.7, belongs to all Kohn-Sham levels ($2.135 \times 10^{-9}$ against $10^{-8}$).

```python
smallest = min(tolerances[n] / measured[n] for n in SHORT_NAMES)
report("smallest margin (tolerance / measured difference)", f"{smallest:.1f}")
check_reproduces(
    sorted(measured) == sorted(SHORT_NAMES) and all(quoted.values())
    and all(verdicts[n] == "PASS" and measured[n] < tolerances[n] for n in SHORT_NAMES),
    "each of the eight measured differences of the record is below its tolerance",
    f"{DETERMINISM}, checks refined_ground_energies to refined_heat_capacity")
```

The smallest margin is printed. The check requires that the cross-check quotes exactly these eight comparisons (`sorted` of a dictionary gives its sorted keys), that each measured number appears in its check's detail, and that each check passed with the measured difference below the tolerance.

**In [8], the tolerances drawn.**

```python
fig, ax = plt.subplots(figsize=(7.0, 4.6))
rows = np.arange(len(SHORT_NAMES))[::-1]  # the first quantity at the top
for row, name in zip(rows, SHORT_NAMES):
    ax.plot([measured[name], tolerances[name]], [row, row], color="#b5b3ad",
            linewidth=2.5)  # the margin
```

One row per comparison, the first at the top (as in Section 0.21, In [7]). In each row a thick grey line runs from the measured difference to the tolerance: on a logarithmic axis its length is the logarithm of the margin.

```python
ax.plot([measured[n] for n in SHORT_NAMES], rows, "o", color=BLUE, markersize=7,
        label="largest measured difference")
ax.plot([tolerances[n] for n in SHORT_NAMES], rows, "|", color="black",
        markersize=16, markeredgewidth=2.0, label="tolerance fixed in advance")
ax.set_xscale("log")
ax.set_xlim(1e-13, 1e-4)
ax.set_yticks(rows, labels=list(SHORT_NAMES.values()))
ax.grid(False, axis="y")
ax.set_xlabel("canonical minus refined run (relative, or in units of the mass m)")
ax.set_title("Kohn-Sham solver: measured differences and tolerances")
# The legend below the picture, in two columns, so that it covers no row.
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2)
```

A blue dot at each measured difference and a black vertical bar (the marker `"|"`) at each tolerance; a logarithmic axis from $10^{-13}$ to $10^{-4}$; the short names label the rows; the legend is placed below the picture (`bbox_to_anchor=(0.5, -0.16)`, measured in units of the picture's size) in two columns (`ncol=2`).

```python
margins = [tolerances[n] / measured[n] for n in SHORT_NAMES]  # tolerance / measured
save_figure(fig, "tolerances",
            r"The eight comparisons between the canonical and the refined run of "
            r"the Revision record's Kohn-Sham solver (one row each): the largest "
            r"measured difference (blue dot) and the tolerance fixed before the "
            r"comparison (black bar), on a logarithmic horizontal axis (relative "
            r"differences, or level differences in units of the mass $m$). Every "
            r"dot lies to the left of its bar: the measured differences are "
            f"between {min(margins):.1f} and {max(margins):.0f} times smaller "
            r"than their tolerances. The grey line from a dot to its bar is this "
            r"margin.")
```

The figure `00d_3_tolerances.png`, whose caption quotes the smallest and the largest margin, 4.7 and 7692. What Figure 00d.3 shows: every blue dot lies to the left of its black bar, most of them by two to four powers of ten; the closest pair is that of all Kohn-Sham levels.

**In [9], the negative control.**

```python
root_path = determinism_checks["refined_mermin_root_path"]  # the record's check
CONTROL = (r"(N\w+): direct-count error (\S+) m \(refined run \S+\), "
           r"former measure (\S+), present measure against it (\S+),")
```

The record's check `refined_mermin_root_path` and a regular expression that finds its entries for the three states. `\w+` is one or more letters, digits or underscores (the name of a state, such as N8_lam0_a00_T10), `\S+` a number, and `\(` and `\)` are round brackets themselves; the four bracketed parts are the name of the state, the error of the old method, the **former measure** (the difference between the two runs when both used the old method) and the **present measure** (the difference seen by the present refined run).

```python
control = []  # (state, error of the old root, former measure, present measure)
for state, error, former, present in re.findall(CONTROL, root_path["detail"]):
    control.append((state, abs(float(error)), float(former), float(present)))
say("state              old method error   former measure   present measure")
for state, error, former, present in control:
    say(f"{state:17} {error:12.3e} m   {former:14.3e}   {present:15.3e}")
```

`re.findall` returns, for every match, the four bracketed parts; the numbers are turned into floating-point numbers (the error with `abs`, its size). The table of Out [9] has three rows: the largest error of the old method, $8.267 \times 10^{-10}\,m$ in the state N8_lamm1_a00_T10, was seen by the former comparison as a difference of only $5.829 \times 10^{-16}$, and by the present comparison as $8.271 \times 10^{-10}$.

```python
largest_hidden = max(error for _, error, _, _ in control)
report("largest error that one shared rounding path hid", f"{largest_hidden:.3e}", "m")
check_reproduces(
    root_path["verdict"] == "PASS" and len(control) == 3
    and all(former < error / 2 <= present for _, error, former, present in control),
    f"one shared rounding path hid errors up to {largest_hidden:.1e} m; "
    "two paths show them",
    f"{DETERMINISM}, check refined_mermin_root_path")
```

The largest hidden error is printed with the unit $m$. The check states, as the record does, that in each of the three states the former measure is below half of the error (it hid it), while the present measure is at least half of it (it shows it): a chain comparison `a < b <= c` holds when both comparisons hold.

**In [10], the negative control drawn.**

```python
fig, ax = plt.subplots(figsize=(7.0, 4.0))
rows = np.arange(len(control))[::-1]  # the first state at the top
height = 0.26  # three bars in each row
errors = [error for _, error, _, _ in control]
formers = [former for _, _, former, _ in control]
presents = [present for _, _, _, present in control]
# How many times smaller the former measure is than the error, state by state.
hidden_ratios = [error / former for error, former in zip(errors, formers)]
```

One row per state, three bars in each; the three columns of the table as three lists; and, for the caption, how many times smaller the former measure was than the error in each state.

```python
ax.barh(rows + height, errors, height, color=ORANGE,
        label="error of the old method")
ax.barh(rows, formers, height, color="#b5b3ad",
        label="former comparison (one rounding path in both runs)")
ax.barh(rows - height, presents, height, color=BLUE,
        label="present comparison (two rounding paths)")
ax.set_xscale("log")
ax.set_xlim(1e-17, 1e-8)
ax.set_yticks(rows, labels=[state for state, _, _, _ in control])
ax.grid(False, axis="y")
ax.set_xlabel(r"size of the difference in $\mu$ (units of the mass m)")
ax.set_title("A comparison that rounds the same way twice sees nothing")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=1)
```

The three bars of each state, orange above, grey in the middle and blue below, on a logarithmic axis from $10^{-17}$ to $10^{-8}$; the states label the rows, and the legend stands below the picture.

```python
save_figure(fig, "shared_rounding",
            r"The negative control of the Revision record's Kohn-Sham solver for "
            r"the three thermal states named on the vertical axis: the error of the "
            r"old method for the chemical potential $\mu$ (orange), the difference "
            r"between the two runs when both used that method, and so shared its "
            r"rounding (grey), and the difference seen by the present refined run, "
            r"which rounds along another path (blue); horizontal axis the size of "
            r"the difference in units of the mass $m$, logarithmic. The grey bars "
            f"are between {min(hidden_ratios):.0f} and "
            f"{max(hidden_ratios) / 1e6:.1f} million "
            r"times shorter than the orange ones: two runs with the same rounding "
            f"hid errors up to {largest_hidden:.1e} "
            r"$m$, which the blue bars show in full.")
```

The figure `00d_4_shared_rounding.png`; its caption computes how much shorter the grey bars are. What Figure 00d.4 shows: in each state the orange and the blue bar have almost the same length (the present comparison sees the whole error), while the grey bar is hundreds to more than a million times shorter (the former comparison saw almost nothing). This is the lesson of the negative control of Section 0.22.

**In [11], random walks with seeds.**

```python
walks = {}  # a label -> the 401 positions of the walk (it starts at 0)
for label, seed in (("seed 12345, first run", 12345),
                    ("seed 12345, second run", 12345), ("seed 2026", 2026)):
    generator = np.random.default_rng(seed)  # a new generator from this seed
    steps = generator.choice([-1, 1], size=400)  # 400 random steps of +1 or -1
    walks[label] = np.concatenate([[0], np.cumsum(steps)])  # positions 0 ... 400
    first = " ".join(f"{s:+d}" for s in steps[:10])  # e.g. "+1 -1 +1 ..."
    say(f"{label:23} first steps: {first}")
```

Three new random-number generators, two from the seed 12345 and one from the seed 2026. `generator.choice([-1, 1], size=400)` picks 400 times at random from the list $[-1, 1]$: the steps of a **random walk**. `np.cumsum` gives the running totals, the positions after each step, and `np.concatenate([[0], ...])` puts the starting position 0 in front. The first ten steps of each walk are printed (Out [11]): the two walks of the seed 12345 begin with the same ten steps, the third with others.

```python
fig, ax = plt.subplots()
step_numbers = np.arange(401)
ax.plot(step_numbers, walks["seed 12345, first run"], color=BLUE, linewidth=3.0,
        label="seed 12345, first run")
ax.plot(step_numbers, walks["seed 12345, second run"], color=YELLOW, linewidth=1.2,
        linestyle="--", label="seed 12345, second run (lies on the first)")
ax.plot(step_numbers, walks["seed 2026"], color=ORANGE, linewidth=1.5,
        label="seed 2026")
ax.set_xlabel("step number")
ax.set_ylabel("position (sum of the steps)")
ax.set_title("Random walks: the same seed gives the same walk")
# The legend below the picture, so that it covers no part of the walks.
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=1)
```

The three walks: the first thick and blue, the second thin, dashed and yellow, so that it is visible on top of the first, the third orange.

```python
save_figure(fig, "seeded_walks",
            r"Three random walks of 400 steps of $+1$ or $-1$ (horizontal axis the "
            r"step number, vertical axis the position, the sum of the steps so far; "
            r"pure numbers). The thick blue walk and the dashed yellow walk come from "
            r"two separate generators started with the same seed 12345: they are "
            r"identical, step for step, so the yellow line lies on the blue one. "
            r"The orange walk, from the seed 2026, is different. A fixed seed makes "
            r"random numbers repeat exactly in every run.")
check(np.array_equal(walks["seed 12345, first run"], walks["seed 12345, second run"]),
      "two generators with the same seed give the same 400 steps")
check(not np.array_equal(walks["seed 12345, first run"], walks["seed 2026"]),
      "a generator with another seed gives other steps")
```

The figure `00d_5_seeded_walks.png` and two checks: `np.array_equal` is true when two arrays have the same shape and the same entries. What Figure 00d.5 shows: the yellow dashed walk runs exactly inside the thick blue one for all 400 steps, while the orange walk goes its own way.

**In [12], the order of a set.**

```python
import subprocess  # starts another program and reads what it prints

NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
PROGRAM = "import sys; print(*set(sys.argv[1:]))"  # print the names of a set
```

`subprocess` starts other programs. `PROGRAM` is a complete little Python program in one line: it makes a set of the names it receives as its arguments (`sys.argv` is the list of the arguments of a program, and `[1:]` leaves out the first entry, the program's own name) and prints them separated by blanks (`print(*...)` prints the members one after the other).

```python
def set_order(seed):
    """The order in which a new Python with PYTHONHASHSEED = seed prints the set."""
    environment = dict(os.environ, PYTHONHASHSEED=str(seed))
    completed = subprocess.run([sys.executable, "-c", PROGRAM, *NAMES],
                               capture_output=True, text=True, env=environment,
                               check=True)  # check=True: stop if Python failed
    return completed.stdout.split()  # the printed names, in their printed order
```

`dict(os.environ, PYTHONHASHSEED=str(seed))` is a copy of the environment variables of the notebook with one of them set to the given hash seed. `subprocess.run` starts a new Python (`sys.executable` is the Python program that runs this notebook) with the option `-c`, which tells it to run the program text that follows, and the eight names as arguments; the new Python receives the copied environment (`env=`). Its printed line is collected and cut at the blanks into the list of the names in their printed order.

```python
orders = [set_order(seed) for seed in range(12)]  # the seeds 0, 1, ..., 11
for seed, order in enumerate(orders):
    printed = " ".join(order)  # the eight names separated by blanks
    say(f"PYTHONHASHSEED={seed:<2}  {printed}")
in_order = " ".join(sorted(orders[0]))  # sorted: x1 x2 ... x8
say(f"sorted              {in_order}")
different = len({tuple(order) for order in orders})  # the number of distinct orders
report("distinct orders among the 12 runs", different)
```

Twelve runs with the hash seeds 0 to 11; the order of each is printed (the first twelve lines of Out [12]), then the sorted order. `{tuple(order) for order in orders}` is a set of the twelve orders (a list cannot be a member of a set, a **tuple** can); equal orders count once, so its size is the number of distinct orders: 12, every run printed another order.

```python
check(set_order(0) == orders[0], "the same hash seed gives the same order")
check(different >= 2, "different hash seeds give different orders of the same set")
check(all(sorted(order) == NAMES for order in orders),
      "sorted, the names come in the same order x1 ... x8 in every run")
```

Three checks: a thirteenth run with the seed 0 repeats the order of the first; at least two of the orders differ; and every order, sorted, is $x_1, \ldots, x_8$. This is why the notebooks sort before they print.

**In [13], the twelve orders as a picture.**

```python
table = orders + [sorted(orders[0])]  # 13 rows of 8 names: 12 runs and the sorted
# Each name replaced by its number in NAMES: x1 -> 0, x2 -> 1, ..., x8 -> 7.
numbers = np.array([[NAMES.index(name) for name in row] for row in table])
colours = matplotlib.colormaps["viridis"].resampled(8)  # 8 colours, violet to yellow
```

The twelve orders and, as a thirteenth row, the sorted order. `NAMES.index(name)` is the position of a name in the list `NAMES`, so each name becomes a number from 0 to 7, and `numbers` is a table of 13 rows and 8 columns. The colour map viridis, cut into 8 colours from dark violet to yellow, gives each name its colour.

```python
fig, ax = plt.subplots(figsize=(7.0, 6.0))
# vmin and vmax put each of the numbers 0 ... 7 in the middle of its own colour.
ax.imshow(numbers, cmap=colours, vmin=-0.5, vmax=7.5, aspect="auto")
for row in range(numbers.shape[0]):
    for column in range(8):
        # white letters on the dark colours, black ones on the light colours
        ink = "white" if numbers[row, column] < 5 else "black"
        ax.text(column, row, table[row][column], ha="center", va="center",
                color=ink, fontsize=9)
```

The table drawn as coloured squares (as in Section 0.17, In [3]); `aspect="auto"` lets the squares stretch to fill the figure, and `numbers.shape[0]` is the number of rows, 13. Each square gets the name written into it.

```python
ax.axhline(11.5, color="white", linewidth=4.0)  # a gap before the sorted row
ax.set_xticks(range(8), labels=[str(place) for place in range(1, 9)])
ax.set_yticks(range(13),
              labels=[f"PYTHONHASHSEED={seed}" for seed in range(12)] + ["sorted"])
ax.grid(False)
ax.set_xlabel("place in the printed order")
ax.set_title("The same set of eight names, printed by twelve runs of Python")
```

A thick white line separates the sorted row from the twelve runs; the columns are labelled with the places 1 to 8 and the rows with the hash seeds and the word sorted.

```python
save_figure(fig, "set_orders",
            r"The order in which twelve separate runs of Python print the same set "
            r"of the eight names $x_1, \ldots, x_8$ (one row per run, labelled by "
            r"its hash seed PYTHONHASHSEED from 0 to 11; horizontal axis the place 1 "
            r"to 8 in the printed order; each square coloured by its name, from "
            r"dark violet for $x_1$ to yellow for $x_8$). Every run prints another "
            r"order, so the rows are scrambled differently; the bottom row, the "
            r"sorted order, is the same in every run.")
```

The figure `00d_6_set_orders.png`. What Figure 00d.6 shows: twelve rows of scrambled colours, no two alike, above one row in which the colours run in order from violet to yellow.

**In [14], line ends.**

```python
import hashlib  # computes sha256 fingerprints

TEXT = "x1 x2\nx3 x4\n"  # two lines, each ended by a line end
with_lf = TEXT.encode("utf-8")  # LF line ends: the byte 10
with_crlf = TEXT.replace("\n", "\r\n").encode("utf-8")  # CR LF: the bytes 13, 10
```

In a Python string, `\n` is the line end LF and `\r` the carriage return CR. The same two lines are made into bytes once with LF and once with CR LF (`replace` puts `\r\n` for every `\n`).

```python
for label, data in (("LF   ", with_lf), ("CR LF", with_crlf)):
    say(f"{label} {len(data):2d} bytes: {list(data)}")
    say(f"      sha256 {hashlib.sha256(data).hexdigest()}")
check(len(with_crlf) == len(with_lf) + 2
      and hashlib.sha256(with_lf).digest() != hashlib.sha256(with_crlf).digest(),
      "the same two lines with LF and with CR LF line ends are different bytes")
```

`list(data)` writes the bytes as numbers: the letter x is 120, the digits 1 to 4 are 49 to 52, the blank is 32, LF is 10 and CR is 13. Out [14] shows 12 bytes with LF and 14 with CR LF, and two completely different fingerprints. The check confirms the two extra bytes and the different fingerprints (`.digest()` is the fingerprint as bytes instead of characters).

**In [15], the line ends of the record's result files.**

```python
def files_below(folder):
    """The files in the repository folder and its sub-folders, in sorted order."""
    return sorted(p for p in repository_file(folder).rglob("*") if p.is_file())
```

All files in a folder and its sub-folders (`rglob("*")` lists everything, `is_file` keeps the files), in sorted order.

```python
RUST_RESULTS = "Revision/kohn_sham/results"
REFERENCE_RESULTS = "Revision/kohn_sham/reference/results"
rust_files = files_below(RUST_RESULTS)
rust_crlf = sum(1 for p in rust_files if b"\r\n" in p.read_bytes())
reference_files = files_below(REFERENCE_RESULTS)
reference_crlf = sum(1 for p in reference_files if b"\r\n" in p.read_bytes())
```

The result folders of the Rust solver and of the Python reference solver. For each, the files are listed and the files that contain the two bytes CR LF are counted (`b"\r\n"` is a **bytes** literal, and `in` searches for it in the bytes of the file).

```python
report("Rust result files", len(rust_files))
report("size of the Rust result files", sum(p.stat().st_size for p in rust_files),
       "bytes")
report("Rust result files with CR LF line ends", rust_crlf)
report("reference result files", len(reference_files))
report("size of the reference result files",
       sum(p.stat().st_size for p in reference_files), "bytes")
report("reference result files with CR LF line ends", reference_crlf)
```

The numbers of files, their total sizes (`p.stat().st_size` is the size of a file in bytes) and the numbers of files with CR LF: Out [15] reports 244 Rust result files with 5857791 bytes and 340 reference result files, none with CR LF line ends.

```python
lf_rust = determinism_checks["outputs_lf_only"]  # the record's check (Rust)
check_reproduces(
    rust_crlf == 0 and lf_rust["verdict"] == "PASS"
    and "(offending: none)" in lf_rust["detail"],
    f"none of the {len(rust_files)} Rust result files has CR LF line ends",
    f"{DETERMINISM}, check outputs_lf_only")
cross_checks = {entry["name"]: entry for entry in read_json(CROSS)["checks"]}
lf_reference = cross_checks["reference_outputs_lf_only"]  # the record's check
stated = f"{len(reference_files)} reference result files; files with CRLF: none"
check_reproduces(
    reference_crlf == 0 and lf_reference["verdict"] == "PASS"
    and stated in lf_reference["detail"],
    f"none of the {len(reference_files)} reference result files has CR LF line ends",
    f"{CROSS}, check reference_outputs_lf_only")
```

Two checks, one per solver: today no file has CR LF line ends, and the record's own check found the same when the solver ran (its detail says that no file offended, or states the number of reference files and that none had CRLF).

**In [16], the fingerprints of the result files.**

```python
def file_fingerprint(path):
    """The sha256 fingerprint of the bytes of the file path."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_names(files, folder):
    """The paths of files relative to the repository folder, written with /."""
    root = repository_file(folder)
    return sorted(p.relative_to(root).as_posix() for p in files)
```

The fingerprint of a file (as in Section 0.21, In [13], but for a path that is already complete), and the sorted names of files relative to a folder, written with `/`. (The docstring says "the repository folder"; the names are relative to the folder `folder`, which is what the manifests list.)

```python
# The Rust manifest: a list of entries {"path": ..., "bytes": ..., "sha256": ...}.
rust_manifest = read_json(f"{RUST_RESULTS}/manifest.json")["files"]
rust_listed = {entry["path"]: entry for entry in rust_manifest}  # path -> entry
rust_wrong = []  # the listed files whose size or fingerprint differs today
for path, entry in rust_listed.items():
    today = repository_file(f"{RUST_RESULTS}/{path}")  # the file as it is today
    same_size = today.stat().st_size == entry["bytes"]
    if not same_size or file_fingerprint(today) != entry["sha256"]:
        rust_wrong.append(path)
```

The Rust solver's manifest lists, for every result file, its path, its size and its fingerprint. For each listed file, today's size and today's fingerprint are compared with the listed ones; a file that differs in either is noted.

```python
# The reference manifest: a dictionary path -> fingerprint.
reference_manifest = read_json(f"{REFERENCE_RESULTS}/manifest.json")["files"]
reference_wrong = []
for path, value in reference_manifest.items():
    today = repository_file(f"{REFERENCE_RESULTS}/{path}")
    if file_fingerprint(today) != value:
        reference_wrong.append(path)
```

The reference solver's manifest is a dictionary from each path to its fingerprint; the comparison is the same.

```python
report("Rust results: fingerprints compared", len(rust_listed))
report("Rust results: files that differ", len(rust_wrong))
report("reference results: fingerprints compared", len(reference_manifest))
report("reference results: files that differ", len(reference_wrong))
report("fingerprints compared in all", len(rust_listed) + len(reference_manifest))
```

Out [16] reports 243 Rust and 339 reference fingerprints compared, 582 in all, and no file that differs. (Each folder holds one more file, its manifest, which cannot list its own fingerprint.)

```python
rust_others = [n for n in relative_names(rust_files, RUST_RESULTS)
               if n != "manifest.json"]
reference_others = [n for n in relative_names(reference_files, REFERENCE_RESULTS)
                    if n != "manifest.json"]
check(rust_wrong == [] and sorted(rust_listed) == rust_others,
      f"the {len(rust_listed)} fingerprints of the Rust manifest equal today's files")
```

The files of each folder except the manifest. The check requires that no listed Rust file differs and that the manifest lists exactly the files of the folder: none is missing, none is extra.

```python
manifest_check = cross_checks["reference_manifest"]
stated = f"lists {len(reference_manifest)} files with SHA-256"  # the record's words
check_reproduces(
    reference_wrong == [] and sorted(reference_manifest) == reference_others
    and manifest_check["verdict"] == "PASS" and stated in manifest_check["detail"],
    f"the {len(reference_manifest)} fingerprints of the reference manifest equal "
    "today's files",
    f"{CROSS}, check reference_manifest")
```

The same for the reference folder, together with the record's own check `reference_manifest`, whose detail must state the same number of listed files.

```python
rust_repeat = determinism_checks["repeat_byte_identical"]  # the Rust second run
# The part of its detail that counts, e.g. "244 files (5857791 bytes) compared, ...".
found = re.search(r"(\d+) files \((\d+) bytes\) compared, same file set: (\w+), "
                  r"differing files: (\w+)", rust_repeat["detail"])
say(f"the record (Rust): {found.group(0)}")
rust_bytes = sum(p.stat().st_size for p in rust_files)  # the bytes of today
check_reproduces(
    rust_repeat["verdict"] == "PASS"
    and (int(found.group(1)), int(found.group(2))) == (len(rust_files), rust_bytes)
    and found.group(3) == "True" and found.group(4) == "none",
    f"a second run of the Rust solver gave the same {len(rust_files)} files "
    f"({rust_bytes} bytes)",
    f"{DETERMINISM}, check repeat_byte_identical")
```

The record's comparison of a second run of the Rust solver with the first. The regular expression picks out four parts of its detail: the number of files, the number of bytes, whether the two runs wrote the same set of files, and the differing files. `found.group(0)` is the whole matched text, printed in Out [16]: 244 files (5857791 bytes) compared, same file set: True, differing files: none. The check requires that the record compared as many files and bytes as the folder holds today, with the same file set and no differing file.

```python
repeat = cross_checks["reference_repeat_byte_identical"]  # the reference second run
# The part of its detail that counts the files, e.g. "340 result files, same ...".
found = re.search(r"(\d+) result files, same file set: (\w+), differing files: (\w+)",
                  repeat["detail"])
say(f"the record (reference): {found.group(0)}")
check_reproduces(
    repeat["verdict"] == "PASS" and int(found.group(1)) == len(reference_files)
    and found.group(2) == "True" and found.group(3) == "none",
    f"a second run of the reference solver gave the same {len(reference_files)} "
    "files, byte for byte",
    f"{CROSS}, check reference_repeat_byte_identical")
```

The same for the reference solver: 340 result files, the same file set, no differing file. Out [16] ends with this PASS line and its record.

**In [17], the last check.**

```python
figure_names = ["00d_1_float_spacing.png", "00d_2_summation_order.png",
                "00d_3_tolerances.png", "00d_4_shared_rounding.png",
                "00d_5_seeded_walks.png", "00d_6_set_orders.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "the six figure files of this notebook exist")
all_checks_passed()
```

The six figure files must exist; the last line prints ALL 22 CHECKS PASSED (notebook 00d): two checks in In [2], one in In [3], one in In [4], three in In [6], one in In [7], one in In [9], two in In [11], three in In [12], one in In [14], two in In [15], four in In [16] and one in In [17].

### 0.26 What we proved, what we computed, what we assumed

This chapter is mostly a map; the few results it derives are elementary, but each is derived line by line and checked by a notebook.

**PROVED in this chapter** (by school algebra and one-variable calculus):

- the tangent line of $y = x^2$ at $x = 1$ is $y = 2x - 1$, and it lies below the parabola because $x^2 - (2x - 1) = (x - 1)^2 \ge 0$; and $e^{t} e^{-t} = 1$ for every $t$ (Section 0.10);
- the signs of the eight entries of the author's metric are $(+, +, +, -, -, -, -, +)$ at every point of the patch $0 < z < \pi/2$ and for every $a_4$, so the signature is (4,4) (Section 0.14, Fact 1);
- the length factors are $e^{a_4} \sin^{1/6} z$ for $x_1$, $x_2$, $x_3$, $1$ for $x_4$, $e^{-a_4} \sin^{1/6} z$ for $x_5$, $x_6$, $x_7$ and $\cot z$ for $x_8$ (Fact 2); along the history $a_4 = A H x_4$ the extra-time factors obey $d f_5 / d x_4 = -A H f_5$ (exponential deflation) and the space factors $d f_1/dx_4 = +A H f_1$ (exponential inflation), and $f_1 f_5 = \sin^{1/3} z$ in every history (Fact 3);
- $\det g = \cos^2 z$ and the volume factor $\sqrt{|\det g|} = \cos z$, for every function $a_4$: the inflation and the deflation cancel in the volume (Fact 4; also by the exact symbolic checks `sqrt_det_g_is_cos_z`, `sqrt_det_g_equals_cos_z` and `sqrt_abs_det_g_is_cos_z` of the three Revision reports listed at the end of Fact 4);
- the expected number of changed characters of a random 64-character hexadecimal fingerprint is $64 \cdot 15/16 = 60$ (Section 0.18);
- $1/10$ has no finite binary expansion; the computer stores 0.1 as $3602879701896397/2^{55}$ and computes $0.1 + 0.2$ as $5404319552844596/2^{54}$, which exceeds the stored 0.3 by $2^{-54}$; the machine epsilon is $2^{-52}$, and the gap between neighbouring stored numbers lies between $\epsilon x/2$ and $\epsilon x$; $(1 + 2^{-53}) + 2^{-53} \ne 1 + (2^{-53} + 2^{-53})$ in floating-point arithmetic; and $1/(N+1) < \pi^2/6 - \sum_{k \le N} 1/k^2 < 1/N$ (Section 0.22).

The chapter also states, without proof, the theorems that later chapters prove: T1, T2, Q, T3 and C1 (Section 0.2; Chapters 18 to 20) and the exact conservation of the U(1) charge and the charge-conjugation matrices $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$ (Chapters 5 and 21). Their status, PROVED, is that of the Revision record, given in the ledger with the reports that verify them.

**COMPUTED by the notebooks** (each number in the cell named; where a Revision record is reproduced, the record file and its check):

- Notebook 00a: the installed versions (In [2] to In [4]); the determinant $-2.000000000000$ (In [5]); the derivative $2 \sin x \cos x$ (In [6]); 30 digits of $\pi$ (In [7]); the tangent line and the two exponentials at 401 points each (In [8], In [9]).
- Notebook 00b: the names and the signs of the coordinates (In [2]; reproduces `Revision/algebra/reports/wolfram-algebra.json`, check `eta_in_author_order`); the eight entries of the metric (In [4]; reproduces `Revision/theory/reports/python-field-theory.json`, check `metric_from_vielbein_equals_SPEC`); no wrong sign at 4819 points (In [5]); $\det g = \cos^2 z$ (In [6]; reproduces `Revision/theory/reports/wolfram-field-theory.json`, check `sqrt_det_g_is_cos_z`); $e^{3} = 20.0855$ and $e^{-3} = 0.049787$ (In [7]); the table of the length factors at $z = \pi/4$ with the product 0.7071 (In [8]; reproduces `Revision/field_equations_a4/reports/wolfram-a4-report.json`, check `sqrt_abs_det_g_is_cos_z`); the volume factor equal to $\cos z$ within $8.9 \times 10^{-16}$ at 200 points for three values of $a_4$ (In [9]; reproduces `Revision/theory/reports/python-field-theory.json`, check `sqrt_det_g_equals_cos_z`).
- Notebook 00c: 12 of 12 checks of the charge-conjugation report (In [2]); the 27 reports of the record, all found by the search, every check PASS, and each report's own totals equal to the counted ones (In [5]; the counts follow the record: 940 checks when this chapter was written); the 16 counts of the table of `Revision/README.md` and the 3 counts quoted by `Revision/kohn_sham/reports/ks-crosscheck.json`, check `inputs_all_pass` (In [6]); the ledger with 10 PROVED, 1 COMPUTED, 1 ASSUMED, 2 HYPOTHESIS and 2 OPEN rows, every report in exactly one row (In [9]); the twelve sentences of `Revision/pairing/reports/python-pairing.json`, key `not_established` (In [11]); 54 to 64 changed characters, mean 60.03, for one-character changes (In [12]); 24 recorded fingerprints equal to today's files (In [13]).
- Notebook 00d: the forward, backward and pairwise errors of 196, 1 and 3 ulps, and the method error $9.999995 \times 10^{-7}$ (In [5]); the relative difference $2.65 \times 10^{-14}$ of the three sums (In [6]); the eight measured differences of the Kohn-Sham solver below their tolerances with the margins 4.7 to 7692 (In [7]; reproduces `Revision/kohn_sham/reports/ks-rust-determinism.json`, checks `refined_ground_energies` to `refined_heat_capacity`); the negative control with a hidden error up to $8.267 \times 10^{-10}$ in units of $m$ (In [9]; check `refined_mermin_root_path` of the same report); 12 distinct set orders for 12 hash seeds (In [12]); no CR LF line end in the 244 Rust and the 340 reference result files (In [15]; checks `outputs_lf_only` and `reference_outputs_lf_only`); 582 manifest fingerprints equal to today's files, and the record's repeat runs of both solvers byte-identical (In [16]; checks `reference_manifest`, `repeat_byte_identical` and `reference_repeat_byte_identical`).

**ASSUMED** (used, not derived here):

- the conventions of Section 0.5: the author's names and roles of the coordinates, the signs $\eta$, units with the speed of light and Planck's constant equal to 1;
- the author's metric itself (Section 0.14), and the history $a_4 = A H x_4$ where it is used, a prescribed background (`Revision/field_equations_a4/reports/ks-source-conditions.json`, check `ks_history_is_a_prescribed_background`);
- the Z2 mirror at the edge $z = \pi/2$ of the hidden direction, in T2 and T3;
- school facts used without proof: the determinant of a diagonal matrix is the product of its diagonal entries (proved in Chapter 1); every whole number is a product of primes in exactly one way; Euler's sum $\pi^2/6$; the rules of the floating-point arithmetic (53 binary digits, round half to even), which are a property of the computer;
- that nobody can construct two different files with the same sha256 fingerprint (believed, not proved).

**HYPOTHESIS and OPEN.** The chapter adds no hypothesis of its own; it records the two HYPOTHESIS rows of the ledger (a time-varying dark sector from the fields; a partner universe of opposite charge) and the two OPEN rows (that the big bang creates universes in pairs, which the equations do not prove; and the excess of matter over antimatter, which the theory as built does not explain).

### 0.27 Exercises

**Exercise 1.** Give each statement one of the five labels and one sentence of reason. (a) The author's metric has the signature (4,4). (b) The ground-state energies of the canonical and the refined run of the Revision record's Kohn-Sham solver differ by at most $1.901 \times 10^{-12}$ (relative). (c) The metric function grows in proportion to the time, $a_4 = A H x_4$, in the Kohn-Sham chapters. (d) Our universe has a partner universe of opposite charge. (e) At the big bang, a pair of universes of masses $+M$ and $-M$ was created.

*Answer.* (a) PROVED: Fact 1 of Section 0.14 derives the signs $(+, +, +, -, -, -, -, +)$ at every point of the patch by school algebra, and the Wolfram verifier checks them (`eta_in_author_order`). (The metric itself is ASSUMED, as the author's input; given the metric, its signature is proved.) (b) COMPUTED: it is a number measured by comparing two numerical runs (`Revision/kohn_sham/reports/ks-rust-determinism.json`, check `refined_ground_energies`), reproducible but not exact. (c) ASSUMED: it is a prescribed background; the computed Kohn-Sham states cannot be its source (row 9 of the ledger). (d) HYPOTHESIS: T1 proves that every solution with mass $+m$ has an image with mass $-m$ and opposite charge, but not that such an image exists alongside our universe (row 14). (e) OPEN as a question of this book: the author proposed it, but no equation of the record describes the creation of anything, so it is not proved (row 15).

**Exercise 2.** Notebook 00a checks that Python is version 3.12 or newer by comparing the pairs $(3, 12)$ and (major, minor). Would the pair $(4, 0)$ pass? Would $(3, 9)$?

*Answer.* Pairs are compared like words in a dictionary: first the first numbers, and only when they are equal the second numbers. $(4, 0)$: the first numbers are 4 and 3, and 4 is larger, so $(4, 0) \ge (3, 12)$ and the check passes (the second numbers are not compared). $(3, 9)$: the first numbers are equal, so the second numbers decide; 9 is smaller than 12, so $(3, 9) < (3, 12)$ and the check fails. (Comparing the versions as decimal numbers would be wrong: 3.9 is larger than 3.12 as a decimal number, but version 9 comes before version 12.)

**Exercise 3.** Compute the eight length factors of the author's metric at the hidden coordinate $z = \pi/6$ and at $a_4 = \ln 2$ (so that $e^{a_4} = 2$), and show that their product is $\cos(\pi/6) = \sqrt{3}/2$.

*Answer.* $\sin(\pi/6) = 1/2$, so $\sin^{1/6}(\pi/6) = (1/2)^{1/6} = 2^{-1/6}$; $\cot(\pi/6) = \cos(\pi/6)/\sin(\pi/6) = (\sqrt{3}/2)/(1/2) = \sqrt{3}$. By Fact 2 of Section 0.14: $f_1 = f_2 = f_3 = 2 \cdot 2^{-1/6} = 2^{5/6} = 1.7818$; $f_4 = 1$; $f_5 = f_6 = f_7 = \frac{1}{2} \cdot 2^{-1/6} = 2^{-7/6} = 0.4454$; $f_8 = \sqrt{3} = 1.7321$. The product is $(2^{5/6})^3 \cdot (2^{-7/6})^3 \cdot 1 \cdot \sqrt{3} = 2^{5/2} \cdot 2^{-7/2} \cdot \sqrt{3} = 2^{-1} \sqrt{3} = \sqrt{3}/2$ (power rule, then the law of exponents $2^{5/2 - 7/2} = 2^{-1}$), which is $\cos(\pi/6)$, as Fact 4 says for every $a_4$.

**Exercise 4.** Along the history $a_4 = A H x_4$ with $A = 1$ and $H = 1$, after how much time $x_4$ has the length factor of an extra time fallen to half its value at $x_4 = 0$? After how much time has it fallen to one thousandth? What has the factor of ordinary space done in the same time?

*Answer.* By Fact 3, $f_5(x_4) = e^{-x_4} \sin^{1/6} z$, so $f_5(x_4)/f_5(0) = e^{-x_4}$. Half: $e^{-x_4} = 1/2$, so $-x_4 = \ln(1/2) = -\ln 2$ (take the natural logarithm of both sides), and $x_4 = \ln 2 = 0.6931$. One thousandth: $x_4 = \ln 1000 = 6.9078$. In the same times the factor of ordinary space, $e^{x_4} \sin^{1/6} z$, has grown by the factors 2 and 1000, since $e^{x_4} = 1/e^{-x_4}$. Every interval of length $\ln 2$ halves the extra-time factor again: this is what exponential deflation means.

**Exercise 5.** Is $0.5 + 0.25 == 0.75$ true in Python? Explain with the stored fractions why the answer differs from that for $0.1 + 0.2 == 0.3$.

*Answer.* True. The numbers $0.5 = 1/2$, $0.25 = 1/4$ and $0.75 = 3/4$ are binary fractions with a few digits (binary 0.1, 0.01 and 0.11), so each is stored exactly, without rounding. Their exact sum, $1/2 + 1/4 = 3/4$, is again a stored number, so the addition does not round either, and the result is exactly the stored 0.75. In Section 0.22, by contrast, 0.1, 0.2 and 0.3 are all rounded when they are stored, and the sum is rounded once more; the roundings do not cancel, and the result misses the stored 0.3 by $2^{-54}$.

**Exercise 6.** Above $2^{53} = 9007199254740992$ the gap between neighbouring stored numbers is 2. In floating-point arithmetic, compute $(2^{53} + 1) + 1$ and $2^{53} + (1 + 1)$.

*Answer.* $2^{53}$ is stored with $m = 2^{52}$ and the power $2^{1}$, so the stored numbers just above it are $2^{53} + 2$, $2^{53} + 4$, and so on, with $m = 2^{52} + 1$, $2^{52} + 2$, and so on. First order: $2^{53} + 1$ lies exactly halfway between $2^{53}$ (with the even $m = 2^{52}$) and $2^{53} + 2$ (with the odd $m = 2^{52} + 1$); round half to even gives $2^{53}$. Adding 1 again gives the same halfway case and again $2^{53} = 9007199254740992$. Second order: $1 + 1 = 2$ exactly, and $2^{53} + 2 = 9007199254740994$ is a stored number. The two orders differ by 2, the gap at that size: the same three numbers added in two orders give two different results, as in Section 0.22.

**Exercise 7.** Notebook 00c compares some fingerprints of which the report recorded only the first 16 hexadecimal characters. If fingerprints behave like random strings, what is the probability that a different file has a fingerprint that begins with the same 16 characters?

*Answer.* Each of the 16 characters agrees with probability $1/16$, and for a random string the 16 agreements are independent, so the probability is $(1/16)^{16} = 16^{-16} = (2^4)^{-16} = 2^{-64}$ (the power rule). Since $2^{10} = 1024 \approx 10^3$, $2^{-64} = 2^{-4} \cdot 2^{-60} \approx \frac{1}{16} \cdot 10^{-18}$; exactly, $2^{-64} = 5.42 \times 10^{-20}$. Even a shortened fingerprint ties a report to its file beyond any reasonable doubt.

**Exercise 8.** Theorem T1 is PROVED, and it says that a universe with mass $+m$ and its T1 image with mass $-m$ have opposite charges, so that together they have the total charge zero. (a) Why does this not prove that the big bang creates universes in pairs? (b) Name one calculation that would be needed in addition.

*Answer.* (a) T1 is a map between solution sets: if a solution with $(m, \lambda)$ exists, then a solution with $(-m, -\lambda)$ exists. It says which configurations are allowed, not which configurations occur, when, or how often; a single universe with mass $+m$ is an equally valid solution without its partner. The zero total holds for classical fields; at the quantum level the image is the same quantum system written in other variables, and two independently quantised universes do not cancel (Q). The same situation is familiar from ordinary physics: the conservation of energy, momentum and charge allows two energetic photons to turn into an electron and a positron, but whether this happens, and how often, is computed from the dynamics of the particles, not from the conservation laws. (b) A dynamical calculation: for example a quantum amplitude, or a probability per unit time, for a transition from a state without universes to a state with the pair, or a solution of the coupled equations of the fields and of gravity that evolves from an initial state into the pair. None of these is derived in the Revision record, which is why the ledger labels the statement OPEN (`Revision/pairing/reports/python-pairing.json`, key `not_established`, sentences 1 and 2).
