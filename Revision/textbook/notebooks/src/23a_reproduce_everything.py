#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 23a, "Reproducing everything: every notebook, every check, the gate"
(textbook "Universes in Pairs", chapter 23, "Reproducing everything").

The notebook Revision/textbook/notebooks/23a_reproduce_everything.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/23a_reproduce_everything.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/23a_reproduce_everything.py

By default the notebook READS the recorded nbkit check of every other notebook of the
book (the nbkit-record line of each provenance file) and does not re-run them; it
tabulates them, draws the run times, reads the step table of the Revision gate
Revision/verify_revision.sh, and builds the index of every check of every report of the
Revision record with the chapters that cite it.  With the environment variable
BOOK_RERUN_ALL=1 it also runs "nbkit.py check" on every other builder, in parallel, into
a scratch folder in the system's temporary folder, and tabulates the fresh results.

Because it reads the provenance files of the other notebooks and the chapter texts, this
notebook must be rebuilt after any other notebook is rebuilt or re-checked with --record
and after any chapter moves a notebook marker or changes a citation of a check.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "23a_1_check_time_per_notebook",
    "23a_2_cumulative_check_time",
    "23a_3_checks_per_chapter",
    "23a_4_figures_per_chapter",
    "23a_5_check_time_per_chapter",
    "23a_6_gate_step_times",
]

REPORT_FILES = [
    "Revision/algebra/reports/python-algebra.json",
    "Revision/algebra/reports/wolfram-algebra.json",
    "Revision/dark_sector/dirac16complex/reports/derivation-checks.json",
    "Revision/dark_sector/dirac16complex/reports/eos-checks.json",
    "Revision/dark_sector/dirac16complex/reports/independent-checks.json",
    "Revision/dark_sector/dirac16complex/reports/ks-history-run.json",
    "Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json",
    "Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json",
    "Revision/field_equations_a4/ks_source/reports/ks-source-a4.json",
    "Revision/field_equations_a4/reports/ks-source-conditions.json",
    "Revision/field_equations_a4/reports/python-a4-report.json",
    "Revision/field_equations_a4/reports/wolfram-a4-report.json",
    "Revision/gkd_lovelock/comparison/author-comparison-report.json",
    "Revision/gkd_lovelock/results/gkd-selftest.json",
    "Revision/gkd_lovelock/results/lovelock-report.json",
    "Revision/gkd_lovelock/results/python-lovelock-report.json",
    "Revision/gkd_lovelock/results/wolfram-gkd-report.json",
    "Revision/kohn_sham/reports/ks-crosscheck.json",
    "Revision/kohn_sham/reports/ks-reference.json",
    "Revision/kohn_sham/reports/ks-rust-determinism.json",
    "Revision/kohn_sham/reports/ks-rust-mermin-roots.json",
    "Revision/kohn_sham/reports/ks-rust-solver.json",
    "Revision/kohn_sham/reports/ks-theory-python.json",
    "Revision/kohn_sham/reports/ks-theory-wolfram.json",
    "Revision/lead_checks/reports/charge-conjugation-and-u1.json",
    "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json",
    "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json",
    "Revision/pairing/kohn_sham/reports/python-t3-completion.json",
    "Revision/pairing/kohn_sham/reports/python-t3.json",
    "Revision/pairing/kohn_sham/reports/t3-reference-demo.json",
    "Revision/pairing/kohn_sham/reports/t3-rust-demo.json",
    "Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json",
    "Revision/pairing/kohn_sham/reports/wolfram-t3.json",
    "Revision/pairing/reports/python-pairing.json",
    "Revision/pairing/reports/wolfram-pairing.json",
    "Revision/theory/reports/python-field-theory.json",
    "Revision/theory/reports/python-scope.json",
    "Revision/theory/reports/wolfram-field-theory.json",
    "Revision/theory/reports/wolfram-scope.json",
]

FACTS = {
    "id": "23a",
    "name": "23a_reproduce_everything",
    "title": "Reproducing everything: every notebook, every check, the gate",
    "purpose": (
        "It reads the recorded nbkit check of every other notebook of the book from its "
        "provenance file (by default it does NOT re-run the other notebooks), prints a "
        "table of every notebook with its title, number of checks, number of figures, "
        "the date, result and seconds of its last recorded check and the section of the "
        "book where it is printed, and draws the run times; it reads the step table of "
        "the Revision gate with the expected wall time of every step; and it builds the "
        "index of every check of every report of the Revision record, with its verdict "
        "and the chapters that cite it, written to a data file. With the environment "
        "variable BOOK_RERUN_ALL set to 1 it also runs the nbkit check of every other "
        "notebook, several at a time, into a scratch folder in the system temporary "
        "folder, and tabulates the fresh results."
    ),
    "records": [
        ["Revision/verify_revision.sh",
         "the step table of the Revision gate: every step, its expected wall time, "
         "whether it is long, its command and the reports it writes"],
    ] + [[path, "a report of the Revision record: the name and verdict of each of its "
                "checks are indexed"] for path in REPORT_FILES],
    "packages": ["matplotlib"],
    "needs_rust": [],
    "expected_seconds": 10,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/23a.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES]
    + ["Revision/textbook/data/23a_notebooks.csv",
       "Revision/textbook/data/23a_check_index.csv"],
    "final_lines": [
        "PASS every file this notebook writes exists",
        "ALL 10 CHECKS PASSED (notebook 23a)",
    ],
    "troubleshooting": [
        ["The last section prints that no other notebook was re-run",
         "that is the default. To re-run every other notebook, set the environment "
         "variable BOOK_RERUN_ALL to 1 in the terminal, start JupyterLab or the headless "
         "run from that same terminal, and run the notebook again. Unset it afterwards.",
         ["$env:BOOK_RERUN_ALL = \"1\"      (Windows PowerShell)",
          "export BOOK_RERUN_ALL=1          (macOS zsh, Linux bash)"]],
        ["With BOOK_RERUN_ALL set to 1, the notebooks that run a Rust program fail",
         "install Rust from https://rustup.rs, open a new terminal, activate the "
         "environment and run the notebook again; the first build of each Rust program "
         "takes a few minutes."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    This book has one executed notebook for every worked example. Each notebook has a
    provenance file next to it, and the last line of that file records the most recent
    verified check of the notebook: the tool `nbkit` executed the notebook a second time
    into a scratch folder and compared everything it produced, byte for byte, with the
    stored copy. This notebook collects those records and the check reports of the
    Revision record into the tables of the last chapter:

    - a table of every other notebook of the book: its id, title, number of checks,
      number of figures, the date, result and seconds of its last RECORDED check, and
      the section of the book where its run instructions are printed;
    - the totals per chapter, and five figures of the counts and the run times;
    - the step table of the Revision gate `Revision/verify_revision.sh` (the script that
      re-runs every verifier of the Revision record), with the expected wall time of
      every step, and a sixth figure;
    - the index of the checks: every check of every report of the Revision record, its
      verdict and the chapters that cite it, written to a data file.

    By DEFAULT this notebook does NOT re-run the other notebooks: it reads what their
    provenance files record. Only when the environment variable `BOOK_RERUN_ALL` is set
    to `1` does its last computing section run the check of every other notebook
    again, several at a time, and print the fresh results. Notebook 23a does not list
    itself: its own record changes every time it is built.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Builder**: the Python file `Revision/textbook/notebooks/src/NNx_name.py` that
      defines the cells of notebook NNx; the tool `nbkit` builds the notebook from it.
    - **nbkit check**: the command `python Revision/textbook/tools/nbkit.py check
      BUILDER`. It executes the notebook again into a scratch folder and compares the
      notebook, every file it writes and its provenance file byte for byte with the
      stored ones; it prints `check_NNx=PASSED` or `check_NNx=FAILED`.
    - **Provenance file**: `NNx_name.PROVENANCE.md`, next to each notebook; its last line,
      an HTML comment that starts with the word `nbkit-record`, holds the measured facts
      of the last verified run, written in JSON.
    - **JSON**: a text format for numbers, strings, lists and tables of named values.
    - **CSV**: a text table, one row per line, the cells separated by commas.
    - **Wall time**: the time on a clock on the wall, from start to finish, in seconds.
    - **Report**: a JSON file of the Revision record that holds a list (or table) of named
      checks, each with a verdict such as PASS.
    - **Gate**: the script `Revision/verify_revision.sh` (and its twin
      `Revision/verify_revision.ps1`) that re-runs every verifier and checker of the
      Revision record in dependency order.
    - **Cite**: a chapter cites a check when one paragraph of the chapter, or the output
      of one code cell of one of the chapter's notebooks, names both the check and the
      file name of its report.
    - **Environment variable**: a named text value that a terminal hands to every
      program it starts; `BOOK_RERUN_ALL` is one.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    Nothing in this notebook is physics: it is bookkeeping, and every number it prints is
    COUNTED from files of the repository. The seconds are those MEASURED by nbkit on the
    development machine (Windows 11, 24 threads) and recorded in the provenance files;
    the gate's times are the EXPECTED wall times written in its step table. On another
    computer the times differ, but the counts, the verdicts and the results do not.
    """),
    md(r"""
    ## 5. The provenance record of every notebook

    The next cell reads every provenance file of the folder of notebooks, except the
    one of this notebook. From each it takes the title, the number of checks (from the
    line `ALL n CHECKS PASSED`) and the recorded check; from the notebook's caption file
    it counts the figures. It then checks that builders and provenance files match one
    to one, that every recorded check passed, and that every figure file exists.
    """),
    code(r'''
    import csv  # reads and writes comma-separated tables
    import re  # regular expressions: patterns that find pieces of text

    NOTEBOOKS = repository_file("Revision/textbook/notebooks")  # notebooks and records
    RECORD = re.compile(r"nbkit-record (\{.*\}) -->")  # the record line
    ALL_LINE = re.compile(r"ALL (\d+) CHECKS PASSED")  # the last line of a notebook
    TITLE = re.compile(r"^# Provenance of Notebook \w+: (.+)$", re.MULTILINE)


    def by_name(paths):
        """Sort paths by their repository-relative name, the same on every system."""
        return sorted(paths, key=lambda path: path.relative_to(REPO).as_posix())


    ROWS = []  # one dictionary per notebook
    for path in by_name(NOTEBOOKS.glob("*.PROVENANCE.md")):
        name = path.name.removesuffix(".PROVENANCE.md")  # e.g. 00a_check_installation
        if name.startswith(NOTEBOOK_ID):
            continue  # this notebook's own record changes whenever it is built
        text = path.read_text(encoding="utf-8")
        record = json.loads(RECORD.search(text).group(1))
        captions = json.loads(repository_file(
            f"{FIGURE_FOLDER}/{name[:3]}.captions.json").read_text(encoding="utf-8"))
        ROWS.append({"id": name[:3], "chapter": int(name[:2]), "name": name,
                     "title": TITLE.search(text).group(1),
                     "checks": int(ALL_LINE.search(text).group(1)),
                     "figures": len(captions), "figure_files": sorted(captions),
                     "date": record["check"]["date"],
                     "result": record["check"]["result"],
                     "seconds": record["check"]["seconds"],
                     "builder": f"Revision/textbook/notebooks/src/{name}.py"})

    builders = [path.stem for path in by_name(NOTEBOOKS.glob("src/*.py"))
                if not path.stem.startswith(NOTEBOOK_ID)]
    say(f"{len(ROWS)} provenance files read, {len(builders)} builders found.")
    check([row["name"] for row in ROWS] == builders,
          "every builder has a provenance file and every provenance file a builder")
    check(all(row["result"] == "passed" for row in ROWS),
          "the last recorded nbkit check of every notebook passed")
    check(all(repository_file(f"{FIGURE_FOLDER}/{figure}").is_file()
              for row in ROWS for figure in row["figure_files"]),
          "every figure named in a caption file exists")
    '''),
    md(r"""
    ## 6. Where each notebook is printed in the book

    A notebook is placed in its chapter by a marker line: an HTML comment that holds the
    word `NOTEBOOK` and the notebook's id, such as `NOTEBOOK 03b`. The book's assembler replaces the marker by two new sections: the run instructions,
    numbered one more than the last section heading `### N.M` before the marker, and
    then the complete text of the notebook. The next cell reads every chapter, finds
    every marker and the heading before it, and checks that every notebook is placed
    exactly once, in the chapter of its own number.
    """),
    code(r'''
    CHAPTERS = by_name(repository_file("Revision/textbook/chapters").glob("[0-9][0-9]-*.md"))
    HEADING = re.compile(r"^### (\d+)\.(\d+) ")  # a section heading such as ### 3.4
    MARKER = re.compile(r"^<!-{2} NOTEBOOK (\w+) -->$")  # a notebook marker line
    PLACED = {}  # notebook id -> list of (chapter file name, section of its instructions)
    for chapter in CHAPTERS:
        section = None
        for line in chapter.read_text(encoding="utf-8").splitlines():
            if HEADING.match(line):
                section = HEADING.match(line).groups()  # e.g. ("3", "4")
            elif MARKER.match(line):
                number = f"{section[0]}.{int(section[1]) + 1}"  # the next section
                PLACED.setdefault(MARKER.match(line).group(1), []).append(
                    (chapter.name, number))

    for row in ROWS:
        places = PLACED.get(row["id"], [])
        row["section"] = places[0][1] if len(places) == 1 else "?"
    say(f"{len(CHAPTERS)} chapter files read, {len(PLACED)} notebook markers found.")
    check(all(len(PLACED.get(row["id"], [])) == 1
              and PLACED[row["id"]][0][0].startswith(row["id"][:2] + "-")
              for row in ROWS),
          "every notebook is placed exactly once, in the chapter of its number")
    '''),
    md(r"""
    ## 7. The table of every notebook

    The next cell defines a function that prints the rows of a range of chapters as a
    table, and prints chapters 0 to 10. The columns: the id; the title (cut to 34
    characters, with `...` when it is longer); the number of checks; the number of
    figures; the date of the last recorded check; its result; its wall time in seconds;
    and the section of the book that holds the notebook's run instructions (the
    notebook's complete text is the section after it).
    """),
    code(r'''
    def show_table(first, last):
        """Print the notebooks of the chapters first to last as a table."""
        print("id  title                              checks figs checked    result "
              "   sec section")
        for row in ROWS:
            if first <= row["chapter"] <= last:
                title = row["title"]
                if len(title) > 34:
                    title = title[:31] + "..."
                print(f"{row["id"]:3} {title:34} {row["checks"]:6d} {row["figures"]:4d} "
                      f"{row["date"]:10} {row["result"]:6} {row["seconds"]:6.1f} "
                      f"{row["section"]:>7}")


    show_table(0, 10)
    '''),
    md(r"""
    The next cell prints chapters 11 to 22 and writes the complete table, with the full
    titles and the builders, to the data file
    `Revision/textbook/data/23a_notebooks.csv`.
    """),
    code(r'''
    show_table(11, 22)
    COLUMNS = ["id", "chapter", "title", "checks", "figures", "date", "result",
               "seconds", "section", "builder"]
    NOTEBOOK_TABLE = "Revision/textbook/data/23a_notebooks.csv"
    with output_file(NOTEBOOK_TABLE).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(COLUMNS)
        writer.writerows([row[column] for column in COLUMNS] for row in ROWS)
    say(f"The table of {len(ROWS)} notebooks was written to {NOTEBOOK_TABLE}.")
    '''),
    md(r"""
    ## 8. The totals per chapter

    The next cell adds up, for each chapter, the number of notebooks, checks and figures
    and the recorded check seconds, prints them, and reports the totals of the book.
    """),
    code(r'''
    PER_CHAPTER = {}  # chapter number -> its totals
    for row in ROWS:
        total = PER_CHAPTER.setdefault(row["chapter"], {"notebooks": 0, "checks": 0,
                                                        "figures": 0, "seconds": 0.0})
        total["notebooks"] += 1
        total["checks"] += row["checks"]
        total["figures"] += row["figures"]
        total["seconds"] += row["seconds"]

    print("chapter notebooks checks figures  seconds")
    for chapter, total in sorted(PER_CHAPTER.items()):
        print(f"{chapter:7d} {total["notebooks"]:9d} {total["checks"]:6d} "
              f"{total["figures"]:7d} {total["seconds"]:8.1f}")
    ALL_SECONDS = sum(row["seconds"] for row in ROWS)
    report("notebooks (without 23a)", len(ROWS))
    report("checks in these notebooks", sum(row["checks"] for row in ROWS))
    report("figures of these notebooks", sum(row["figures"] for row in ROWS))
    report("recorded check time, one after the other", f"{ALL_SECONDS:.1f}", "s")
    check(sorted(PER_CHAPTER) == list(range(23)),
          "every chapter 0 to 22 has at least one notebook")
    '''),
    md(r"""
    ## 9. Two figures of the run times

    The next cell draws the recorded check time of every notebook as a bar (on a
    logarithmic axis, because the times range from about a second to minutes), and the
    share of the total time taken by the slowest notebooks, adding them up from the
    slowest down.
    """),
    code(r'''
    ids = [row["id"] for row in ROWS]
    seconds = [row["seconds"] for row in ROWS]
    fig, ax = plt.subplots(figsize=(12, 4.5))
    ax.bar(range(len(ROWS)), seconds, color="#2a78d6")
    ax.set_yscale("log")  # equal steps on the axis are equal factors
    ax.set_xticks(range(len(ROWS)), ids, rotation=90, fontsize=6)
    ax.set_xlim(-1, len(ROWS))
    ax.set_xlabel("notebook")
    ax.set_ylabel("recorded nbkit check time (s)")
    ax.grid(axis="y", which="both", alpha=0.3)
    save_figure(fig, "check_time_per_notebook",
                "The wall time in seconds of the last recorded nbkit check of every "
                "notebook of chapters 0 to 22 (one bar each, in book order), on a "
                "logarithmic vertical axis. Most notebooks take a few seconds; a few, "
                "which run the Rust programs or long numerical scans, take minutes.")

    slowest = sorted(seconds, reverse=True)
    shares = [100 * sum(slowest[:k]) / ALL_SECONDS for k in range(len(slowest) + 1)]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(range(len(shares)), shares, color="#eb6834", marker="o", markersize=3)
    ax.set_xlabel("number of notebooks, slowest first")
    ax.set_ylabel("share of the total check time (%)")
    ax.grid(alpha=0.3)
    save_figure(fig, "cumulative_check_time",
                "The share in percent of the total recorded check time taken by the "
                "slowest notebooks: the curve adds the check times up from the slowest "
                "notebook down. It rises steeply at first, because a few slow notebooks "
                "take a large part of the time, and then flattens.")
    report("share of the three slowest notebooks", f"{shares[3]:.1f}", "%")
    '''),
    md(r"""
    ## 10. Checks, figures and run time per chapter

    The next cell draws three bar charts with one bar per chapter: the number of checks,
    the number of figures and the recorded check time of its notebooks.
    """),
    code(r'''
    chapters = sorted(PER_CHAPTER)
    for key, name, label, colour, caption in [
            ("checks", "checks_per_chapter", "checks", "#1baf7a",
             "The number of checks of the notebooks of each chapter (the sum of the "
             "numbers n in their last lines ALL n CHECKS PASSED); horizontal axis the "
             "chapter, vertical axis the number of checks."),
            ("figures", "figures_per_chapter", "figures", "#eda100",
             "The number of figures drawn by the notebooks of each chapter (the "
             "entries of their caption files); horizontal axis the chapter, vertical "
             "axis the number of figures."),
            ("seconds", "check_time_per_chapter", "recorded check time (s)", "#4a3aa7",
             "The recorded nbkit check time in seconds of the notebooks of each "
             "chapter, added up; horizontal axis the chapter, vertical axis the "
             "seconds. This is the time one command per chapter needs on the "
             "development machine.")]:
        fig, ax = plt.subplots(figsize=(8, 3.6))
        ax.bar(chapters, [PER_CHAPTER[chapter][key] for chapter in chapters],
               color=colour)
        ax.set_xticks(chapters)
        ax.set_xlabel("chapter")
        ax.set_ylabel(label)
        ax.grid(axis="y", alpha=0.3)
        save_figure(fig, name, caption)
    '''),
    md(r"""
    ## 11. The steps of the Revision gate

    The gate `Revision/verify_revision.sh` holds its steps as a table between the first
    and the second appearance of the word `REVISION_GATE_STEPS`. Each line of it has
    seven fields separated by `|`: the step name, the expected wall time in seconds, the
    kind (`1` = long, skipped by the option `--fast`; `A` = an audit that always runs;
    `0` = any other step), a work folder, the output files, the reports and the command.
    The next cell reads the table, prints every step with its time and a short form of
    its command, and adds up the expected time of the full gate and of `--fast`.
    """),
    code(r'''
    gate = repository_file("Revision/verify_revision.sh").read_text(encoding="utf-8")
    table = gate.split("REVISION_GATE_STEPS")[1]  # the text between the two marks
    STEPS = [line.split("|") for line in table.splitlines() if line.count("|") == 6]


    def short_command(command):
        """The first two words of a step command that are not options, as file names."""
        words = [word.strip("{}").rsplit("/", 1)[-1] for word in command.split()
                 if not word.startswith("-")]
        return " ".join(words[:2])


    print(f"{"step":33} {"sec":>5} {"kind":4} command")
    for name, expected, kind, _, _, _, command in STEPS:
        mark = {"1": "long", "A": "all"}.get(kind, "")
        print(f"{name:33} {int(expected):5d} {mark:4} {short_command(command)}")
    FULL = sum(int(step[1]) for step in STEPS)
    FAST = sum(int(step[1]) for step in STEPS if step[2] != "1")
    report("gate steps", len(STEPS))
    report("long steps (skipped by --fast)", sum(step[2] == "1" for step in STEPS))
    report("expected wall time of the full gate", f"{FULL} s = {FULL / 3600:.2f} h")
    report("expected wall time with --fast", f"{FAST} s = {FAST / 60:.1f} min")
    '''),
    md(r"""
    The next cell draws the expected wall time of every step of the gate, in the order
    in which the gate runs them; the long steps are drawn in a second colour.
    """),
    code(r'''
    fig, ax = plt.subplots(figsize=(12, 5))
    colours = ["#e34948" if step[2] == "1" else "#2a78d6" for step in STEPS]
    ax.bar(range(len(STEPS)), [int(step[1]) for step in STEPS], color=colours)
    ax.set_yscale("log")
    ax.set_xticks(range(len(STEPS)), [step[0] for step in STEPS], rotation=90,
                  fontsize=6)
    ax.set_xlim(-1, len(STEPS))
    ax.set_ylabel("expected wall time (s)")
    ax.grid(axis="y", which="both", alpha=0.3)
    save_figure(fig, "gate_step_times",
                "The expected wall time in seconds of every step of the Revision gate, "
                "in the order the gate runs them, on a logarithmic vertical axis; red "
                "bars are the long steps that the option fast skips, blue bars all "
                "others. A few long Wolfram and Kohn-Sham steps take most of the time.")
    '''),
    md(r"""
    ## 12. The index of the checks of the Revision record

    A report is any JSON file of the Revision record (outside the textbook folder and
    the Rust build folders) whose top level holds a list `checks` of named checks with
    verdicts, a table `checks` of named checks (each `true` or a table with `passed` or
    a verdict), or, for the GKD self-test, a list `results` of cases each with a number
    of `mismatches`. This is the rule of the gate's step `reports-pass`. The next cell
    defines a function that turns one such file into a list of (check name, verdict),
    reads every JSON file of the record, and keeps the reports.
    """),
    code(r'''
    def check_list(document):
        """The (name, verdict) pairs of a report, or [] if it is not a report."""
        if not isinstance(document, dict):
            return []
        checks, results = document.get("checks"), document.get("results")
        if isinstance(checks, list):
            return [(item["name"], str(item["verdict"]).upper()) for item in checks]
        if isinstance(checks, dict) and all(isinstance(item, (bool, dict))
                                            for item in checks.values()):
            return [(name, "PASS" if item is True or (isinstance(item, dict) and (
                item.get("passed") is True or
                str(item.get("verdict", "")).upper() == "PASS")) else "FAIL")
                for name, item in checks.items()]
        if isinstance(results, list) and results and all(
                isinstance(item, dict) and "mismatches" in item for item in results):
            return [(", ".join(f"{key}={value}" for key, value in item.items()
                               if key != "mismatches"),
                     "PASS" if item["mismatches"] == 0 else "FAIL") for item in results]
        return []


    REPORTS = {}  # report path -> list of (check name, verdict)
    for path in by_name(repository_file("Revision").rglob("*.json")):
        relative = path.relative_to(REPO).as_posix()
        if relative.startswith("Revision/textbook/") or "/target/" in relative:
            continue
        pairs = check_list(json.loads(path.read_text(encoding="utf-8")))
        if pairs:
            REPORTS[relative] = pairs
    gate_reports = {path for step in STEPS for path in step[5].split(",") if path != "-"}
    say(f"{len(REPORTS)} reports found with {sum(map(len, REPORTS.values()))} checks; "
        f"the gate's step table names {len(gate_reports)} reports.")
    check(gate_reports <= set(REPORTS),
          "every report named in the gate's step table is in the index")
    check(all(verdict in ("PASS", "NOT-AVAILABLE")
              for pairs in REPORTS.values() for _, verdict in pairs),
          "every check of every report is PASS or NOT-AVAILABLE")
    '''),
    md(r"""
    The next cell finds the chapters that cite each check. It cuts every chapter of
    chapters 0 to 22 into paragraphs (blocks of lines between empty lines), adds the
    output of every code cell of the chapter's notebooks as further blocks, and marks a
    check as cited by the chapter when one block contains both the file name of the
    check's report and the check's name as a whole word.
    """),
    code(r'''
    BLOCKS = {}  # chapter number -> its paragraphs and the outputs of its notebooks
    for chapter in CHAPTERS:
        number = int(chapter.name[:2])
        if number > 22:
            continue  # chapter 23 itself is left out
        text = chapter.read_text(encoding="utf-8")
        blocks = [block for block in re.split(r"\n\s*\n", text) if block.strip()]
        for row in ROWS:
            if row["chapter"] == number:
                notebook = json.loads((NOTEBOOKS / f"{row['name']}.ipynb").read_text(
                    encoding="utf-8"))
                for cell in notebook["cells"]:
                    outputs = [output.get("text", "") for output in cell.get("outputs", [])]
                    blocks.append("".join("".join(item) for item in outputs))
        BLOCKS[number] = blocks

    CITED = {}  # (report, check name) -> set of chapter numbers
    for number, blocks in BLOCKS.items():
        for block in blocks:
            for report_path, pairs in REPORTS.items():
                if report_path.rsplit("/", 1)[1] not in block:
                    continue
                for check_name, _ in pairs:
                    word = r"(?<![\w.-])" + re.escape(check_name) + r"(?![\w-])"
                    if re.search(word, block):
                        CITED.setdefault((report_path, check_name), set()).add(number)
    say(f"{len(CITED)} (report, check) pairs are cited by at least one chapter.")
    '''),
    md(r"""
    The next cell prints one line per report: its path (under `Revision/`, without
    `.json`), its number of checks, how many are PASS, how many NOT-AVAILABLE, and how
    many are cited by at least one chapter. It then writes the complete index, one row
    per check, to the data file `Revision/textbook/data/23a_check_index.csv`, reads the
    file back and checks that it has one row per check.
    """),
    code(r'''
    print(f"{"report (under Revision/, without .json)":63} {"checks":>6} {"PASS":>4} "
          f"{"N/A":>3} {"cited":>5}")
    INDEX = []  # one row per check: report, check, verdict, citing chapters
    for report_path, pairs in REPORTS.items():
        for check_name, verdict in pairs:
            chapters = sorted(CITED.get((report_path, check_name), set()))
            INDEX.append([report_path, check_name, verdict,
                          " ".join(str(chapter) for chapter in chapters)])
        short = report_path.removeprefix("Revision/").removesuffix(".json")
        print(f"{short:63} {len(pairs):6d} "
              f"{sum(verdict == "PASS" for _, verdict in pairs):4d} "
              f"{sum(verdict == "NOT-AVAILABLE" for _, verdict in pairs):3d} "
              f"{sum((report_path, name) in CITED for name, _ in pairs):5d}")

    CHECK_INDEX = "Revision/textbook/data/23a_check_index.csv"
    with output_file(CHECK_INDEX).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["report", "check", "verdict", "cited_by_chapters"])
        writer.writerows(INDEX)
    with output_file(CHECK_INDEX).open(encoding="utf-8", newline="") as handle:
        read_back = list(csv.reader(handle))
    report("reports", len(REPORTS))
    report("checks in the index", len(INDEX))
    report("checks cited by at least one chapter", sum(bool(row[3]) for row in INDEX))
    check(read_back[1:] == INDEX, "the index file holds exactly one row per check")
    '''),
    md(r"""
    As an example of the index, the next cell prints the rows of one report: the twelve
    checks of the charge-conjugation matrices and the local U(1) law,
    `Revision/lead_checks/reports/charge-conjugation-and-u1.json`, with the chapters
    that cite each check.
    """),
    code(r'''
    EXAMPLE = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
    print(f"{"check":44} {"verdict":7} cited by chapters")
    for report_path, check_name, verdict, chapters in INDEX:
        if report_path == EXAMPLE:
            print(f"{check_name:44} {verdict:7} {chapters or "-"}")
    check(sum(row[0] == EXAMPLE for row in INDEX) == 12,
          "the example report holds 12 checks",
          record=f"{EXAMPLE}, all checks")
    '''),
    md(r"""
    ## 13. Re-running every notebook (only with BOOK_RERUN_ALL=1)

    The next cell does nothing but print one sentence, unless the environment variable
    `BOOK_RERUN_ALL` is `1`. Then it runs `nbkit check` on the builder of every other
    notebook, at most 8 at a time (half the processor threads, when that is fewer),
    the slowest first, into a new scratch folder in the system's temporary folder. It
    never changes a file of the repository. It prints, per chapter, how many notebooks
    passed and their fresh and recorded seconds, every notebook that failed, the wall
    time of the whole re-run, and writes the fresh results to `fresh_results.csv` in the
    scratch folder; it stops with an error if any notebook failed. The figures above
    keep showing the RECORDED times.
    """),
    code(r'''
    RERUN = os.environ.get("BOOK_RERUN_ALL") == "1"  # the switch of this section
    if not RERUN:
        say("BOOK_RERUN_ALL is not set to 1, so no other notebook was re-run: every "
            "table and figure above shows the RECORDED results of the provenance files.")
    else:
        import subprocess  # starts other programs
        import sys  # sys.executable is the Python program of this notebook
        import tempfile  # makes a new folder in the system's temporary folder
        import time  # a clock, for the wall time of the re-run
        from concurrent.futures import ThreadPoolExecutor  # several at a time

        scratch = Path(tempfile.mkdtemp(prefix="book_rerun_"))
        environment = {key: value for key, value in os.environ.items()
                       if key not in ("BOOK_RERUN_ALL", "TEXTBOOK_OUTPUT_ROOT")}
        nbkit = str(repository_file("Revision/textbook/tools/nbkit.py"))

        def rerun(row):
            """Run nbkit check on the builder of one notebook; keep its key lines."""
            done = subprocess.run(
                [sys.executable, nbkit, "check", str(repository_file(row["builder"])),
                 "--scratch", str(scratch)], capture_output=True, text=True,
                encoding="utf-8", errors="replace", cwd=REPO, env=environment)
            values = dict(line.split("=", 1) for line in done.stdout.splitlines()
                          if "=" in line)
            fresh = values.get(f"check_{row["id"]}_seconds", "")
            return {"id": row["id"], "chapter": row["chapter"],
                    "result": values.get(f"check_{row["id"]}", "FAILED"),
                    "seconds": float(fresh) if fresh[:1].isdigit() else 0.0,
                    "recorded": row["seconds"]}

        workers = max(1, min(8, (os.cpu_count() or 2) // 2))
        start = time.perf_counter()
        with ThreadPoolExecutor(max_workers=workers) as pool:
            FRESH = list(pool.map(rerun, sorted(ROWS, key=lambda row: -row["seconds"])))
        wall = time.perf_counter() - start
        FRESH.sort(key=lambda item: item["id"])
        print("chapter notebooks passed  fresh s recorded s")
        for chapter in sorted(PER_CHAPTER):
            items = [item for item in FRESH if item["chapter"] == chapter]
            print(f"{chapter:7d} {len(items):9d} "
                  f"{sum(item["result"] == "PASSED" for item in items):6d} "
                  f"{sum(item["seconds"] for item in items):8.1f} "
                  f"{sum(item["recorded"] for item in items):10.1f}")
        failed = [item["id"] for item in FRESH if item["result"] != "PASSED"]
        for item_id in failed:
            say(f"FAILED {item_id}: run its nbkit check alone to see the problem lines")
        with (scratch / "fresh_results.csv").open("w", encoding="utf-8",
                                                  newline="") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            writer.writerow(["id", "chapter", "result", "seconds", "recorded"])
            writer.writerows([item[key] for key in ("id", "chapter", "result",
                                                    "seconds", "recorded")]
                             for item in FRESH)
        say(f"Re-run of {len(FRESH)} notebooks with {workers} at a time: wall time "
            f"{wall:.0f} s; fresh results in {scratch / "fresh_results.csv"}")
        assert not failed, f"nbkit check failed for {failed}"
        say(f"RERUN all {len(FRESH)} other notebooks passed their nbkit check.")
    '''),
    md(r"""
    ## 14. The last check

    The last cell checks that every file this notebook writes exists and prints the
    number of checks that passed.
    """),
    code(r'''
    check(all(output_file(path).is_file() for path in
              [f"{FIGURE_FOLDER}/{name}" for name in CAPTIONS]
              + [NOTEBOOK_TABLE, CHECK_INDEX, CAPTION_FILE]),
          "every file this notebook writes exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 15. What this notebook showed

    - Every other notebook of the book has a builder and a provenance file, is placed
      exactly once in its own chapter, and its last RECORDED nbkit check passed; the
      table gives, for each, its checks, figures, check date, result, seconds and
      section, and the data file `Revision/textbook/data/23a_notebooks.csv` holds it.
    - The totals per chapter and the six figures show where the checks, the figures
      and the run time of the book are.
    - The gate of the Revision record has the steps printed in Section 11, with their
      expected wall times; the full gate and the option `--fast` are added up.
    - Every check of every report of the Revision record is PASS or NOT-AVAILABLE; the
      index of all of them, with the chapters that cite each, is in
      `Revision/textbook/data/23a_check_index.csv`.
    - By default nothing was re-run: the results are the RECORDED ones. With
      `BOOK_RERUN_ALL=1` the last computing section re-runs every other notebook.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
