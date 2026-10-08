#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 00c, "The honesty ledger: reading and checking the Revision record"
(textbook "Universes in Pairs", chapter 00).

The notebook Revision/textbook/notebooks/00c_honesty_ledger.ipynb is BUILT from this file
by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/00c_honesty_ledger.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/00c_honesty_ledger.py

It opens every verifier report of the Revision record (27 JSON files), counts their
checks in each of the three layouts that occur, compares the counts with the reports' own
summaries, with the table of Revision/README.md and with the counts quoted by the
Kohn-Sham cross-check, assigns every report to one row of the honesty ledger (the
statuses of TEXTBOOK_SPEC rule R3), prints the list of what the pairing record itself
says is NOT established, and compares the 24 sha256 fingerprints that the reports record
for their input files with the files of today.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

# The 27 verifier reports of the Revision record, grouped by folder, each with the engine
# that did its computation (Wolfram Language, Python, Rust, or the lead's independent
# Python checks). The notebook prints this list in its cell In [5].
REPORT_GROUPS = [
    ("the gammas, C, Gamma, B, Pin(4,4) and Spin(4,4)", [
        ("Revision/algebra/reports/wolfram-algebra.json", "Wolfram"),
        ("Revision/algebra/reports/python-algebra.json", "Python")]),
    ("the Lagrangians, field equations, EMT, quantisation; the scope", [
        ("Revision/theory/reports/wolfram-field-theory.json", "Wolfram"),
        ("Revision/theory/reports/python-field-theory.json", "Python"),
        ("Revision/theory/reports/wolfram-scope.json", "Wolfram"),
        ("Revision/theory/reports/python-scope.json", "Python")]),
    ("the field equations for a4; the Kohn-Sham states as a source", [
        ("Revision/field_equations_a4/reports/wolfram-a4-report.json", "Wolfram"),
        ("Revision/field_equations_a4/reports/python-a4-report.json", "Python"),
        ("Revision/field_equations_a4/reports/ks-source-conditions.json", "Python")]),
    ("GKD and the Lovelock tensors", [
        ("Revision/gkd_lovelock/results/lovelock-report.json", "Rust"),
        ("Revision/gkd_lovelock/results/gkd-selftest.json", "Rust"),
        ("Revision/gkd_lovelock/results/wolfram-gkd-report.json", "Wolfram"),
        ("Revision/gkd_lovelock/results/python-lovelock-report.json", "Python")]),
    ("the Kohn-Sham theory, solvers and comparisons", [
        ("Revision/kohn_sham/reports/ks-theory-wolfram.json", "Wolfram"),
        ("Revision/kohn_sham/reports/ks-theory-python.json", "Python"),
        ("Revision/kohn_sham/reports/ks-rust-solver.json", "Rust"),
        ("Revision/kohn_sham/reports/ks-rust-determinism.json", "Python"),
        ("Revision/kohn_sham/reports/ks-rust-mermin-roots.json", "Python"),
        ("Revision/kohn_sham/reports/ks-reference.json", "Python"),
        ("Revision/kohn_sham/reports/ks-crosscheck.json", "Python")]),
    ("the pairing theorems T1, T2, Q and T3", [
        ("Revision/pairing/reports/wolfram-pairing.json", "Wolfram"),
        ("Revision/pairing/reports/python-pairing.json", "Python"),
        ("Revision/pairing/kohn_sham/reports/wolfram-t3.json", "Wolfram"),
        ("Revision/pairing/kohn_sham/reports/python-t3.json", "Python")]),
    ("the lead's independent checks", [
        ("Revision/lead_checks/reports/charge-conjugation-and-u1.json", "lead"),
        ("Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json", "lead"),
        ("Revision/lead_checks/reports/emt-divergence-and-spin-connection.json",
         "lead")]),
]
REPORTS = [path for _, group in REPORT_GROUPS for path, _ in group]
# The list as lines of the code cell In [5]: a comment line before each group, then one
# line per report (indented by 4 in the notebook, so each line has at most 85 characters).
REPORT_LINES = []
for _subject, _group in REPORT_GROUPS:
    REPORT_LINES.append(f"# {_subject}")
    for _path, _engine in _group:
        REPORT_LINES.append(f'("{_path}", "{_engine}"),')
assert max(len(_line) for _line in REPORT_LINES) <= 85, "a line of REPORTS is too long"


FACTS = {
    "id": "00c",
    "name": "00c_honesty_ledger",
    "title": "The honesty ledger: reading and checking the Revision record",
    "purpose": (
        "It finds the 27 verifier reports of the Revision record, counts their checks "
        "and confirms that every one has the verdict PASS, compares the counts "
        "with the summaries of the reports and with the numbers quoted elsewhere in the "
        "record, assigns every report to its row of the honesty ledger with the labels "
        "PROVED, COMPUTED, ASSUMED, HYPOTHESIS and OPEN, prints what the pairing record "
        "itself says is not established, compares 24 recorded sha256 fingerprints with "
        "the files of today, and draws four teaching plots."
    ),
    "records": (
        [[path, "a verifier report: its checks are counted and compared with its own "
                "summary"] for path in REPORTS]
        + [
            ["Revision/README.md",
             "the check counts printed in its table of the folders"],
            ["Revision/algebra/gammas.json",
             "an input file whose sha256 fingerprint the Kohn-Sham reports record"],
            ["Revision/algebra/reports/python-gammas.json",
             "an input file whose sha256 fingerprint the Kohn-Sham reports record"],
            ["Revision/kohn_sham/ks-theory.json",
             "an input file whose sha256 fingerprint the Kohn-Sham reports record"],
            ["Revision/kohn_sham/solver/tools/mermin-roots-40digit.json",
             "an input file whose sha256 fingerprint the Rust solver report records"],
            ["Revision/gkd_lovelock/results",
             "the input files whose sha256 fingerprints the GKD reports record"],
            ["Revision/gkd_lovelock/code",
             "the Rust sources whose sha256 fingerprints the Wolfram GKD report records"],
            ["Revision/gkd_lovelock/verification",
             "the Wolfram sources whose sha256 fingerprints the Wolfram GKD report "
             "records"],
        ]
    ),
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 10,
    "timeout_seconds": 120,
    "files_written": [
        "Revision/textbook/figures/00c.captions.json",
        "Revision/textbook/figures/00c_1_checks_by_report.png",
        "Revision/textbook/figures/00c_2_two_verifiers.png",
        "Revision/textbook/figures/00c_3_ledger.png",
        "Revision/textbook/figures/00c_4_fingerprints.png",
    ],
    "final_lines": [
        "PASS the four figure files of this notebook exist",
        "ALL 14 CHECKS PASSED (notebook 00c)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" or \"KeyError\" naming a file below the folder Revision",
         "a file of the Revision record is missing or damaged: the repository folder is "
         "incomplete. Delete the folder Dirac_claude, download it again with the git "
         "clone command of Step 3, and open the notebook from the new folder."],
        ["\"AssertionError: check failed: the 24 recorded fingerprints equal the files "
         "of today\"",
         "a file of the Revision record was changed after its report was written; the "
         "table printed just above the error marks it CHANGED. The command below, run in "
         "the repository folder, lists every changed file; restore a changed file with "
         "the second command (write the file name printed in the table, with the folder "
         "Revision in front, instead of FILE).",
         ["git status", "git restore FILE"]],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    This notebook checks the honesty ledger of the book: the table that gives every
    main statement of the book its label (PROVED, COMPUTED, ASSUMED, HYPOTHESIS or
    OPEN) and the place where it is verified. It does what a careful reader would do
    by hand, but for every report at once. It

    - opens one report of the Revision record and reads its checks one by one;
    - writes a function that counts the checks of a report in each of the three
      layouts that occur, searches the whole folder Revision for reports, finds 27,
      and counts the checks of all of them;
    - confirms that every check has the verdict PASS and that the counts agree with
      the summaries that the reports state themselves, with the table of the file
      Revision/README.md and with the counts quoted by the Kohn-Sham cross-check;
    - assigns every report to its row of the ledger, and prints the list of what the
      pairing record itself says is NOT established;
    - computes sha256 fingerprints and compares the 24 fingerprints that the reports
      recorded for their input files with the files of today;
    - draws four teaching plots and prints a PASS line for every check.

    It does not run the verifier programs again (they need Wolfram Mathematica or Rust
    and minutes to hours); it checks what they recorded.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Revision record**: the computations stored in the folder Revision of the
      repository, done anew for the author's metric. Every number of the book comes
      from it or from a notebook of the book.
    - **Verifier, report**: a *verifier* is a program that checks statements; it writes
      its results into a *report*, a JSON file (a plain text file of names, numbers and
      lists).
    - **Check, verdict**: a *check* is one statement tested by a verifier; its *verdict*
      is PASS (true) or FAIL (false). Each check also has a name and a detail text.
    - **Engine**: the program that did the computation: **Wolfram Language** (the
      language of Mathematica, run with wolframscript), **Python** (with the packages
      sympy, numpy and mpmath), or **Rust** (a fast compiled language). The *lead's
      independent checks* are short Python programs that share no code with the other
      verifiers.
    - **Independent**: two verifiers are independent when they share no code; when both
      agree, a programming error in one of them would have to be repeated in the other
      to go unnoticed.
    - **Dictionary, list** (Python): a *list* `[a, b, c]` is an ordered collection; a
      *dictionary* `{"name": value, ...}` stores values under names (*keys*). A JSON
      file is read into dictionaries and lists.
    - **The five labels**: **PROVED** (exact, with a complete proof and a named
      computer-algebra check), **COMPUTED** (a number from a numerical computation, with
      its uncertainty), **ASSUMED** (a starting point that is not derived),
      **HYPOTHESIS** (an idea stated and examined but not established), **OPEN** (a
      question nobody has answered).
    - **Ledger**: the table of the statements, their labels and the reports that
      verify them.
    - **Fingerprint (sha256)**: a number of 64 hexadecimal characters computed from the
      bytes of a file. The same file always gives the same fingerprint; a file that
      differs in a single byte gives a completely different one. **Hexadecimal**: the
      digits 0 to 9 and the letters a to f, sixteen symbols in all.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The rule above every other rule of the book is honesty: it never writes "proved"
    for a statement that is not proved. To make this rule checkable, every statement
    carries one of five labels and names the place where it is verified. A statement
    can be checked at three levels:

    1. **The derivation**: follow it line by line in the book.
    2. **The report**: open the report of the verifier that checked it and read the
       verdict of the named check. This notebook works at this level.
    3. **The computation**: run the verifier again and compare its new report with the
       stored one (the last chapter of the book lists every command).

    Two facts make level 2 trustworthy. First, the exact statements of eight subjects
    were checked by two independent verifiers, one in Wolfram Language and one in
    Python, and the Kohn-Sham numbers by two independent solvers, one in Rust and one
    in Python.
    Second, a report records the sha256 fingerprints of the files it read; when the
    fingerprints of today's files are the same, the report belongs to exactly these
    files.

    A ledger row labelled OPEN or HYPOTHESIS has no report: nothing in the record
    establishes it. In particular the record proves exact maps between the solutions
    of mass $+m$ and those of mass $-m$ (the pairing theorems T1, T2, Q and T3), but it
    does not prove that the big bang creates universes, in pairs or otherwise, and the
    theory as built does not explain the excess of matter over antimatter. The pairing
    record states itself what it does not establish; the notebook prints that list.
    """),
    md(r"""
    ## 5. One report, opened by hand

    The next cell defines the function `read_report`, which reads a JSON file of the
    repository into Python dictionaries and lists, and the helper `check_reproduces`.
    `check_reproduces` is the helper `check` for a check that reproduces a Revision
    record: it first calls `sys.stdout.flush()`, which sends all printed text that is
    still waiting, and then calls `check` with the record. (Jupyter sends printed text
    in pieces; flushing first keeps the PASS line and the line `reproduces ...` below
    it in one piece, so that the book's tools read them together.)

    Then the cell opens the report of the lead's independent check of the
    charge-conjugation matrices and of the conservation of the charge,
    Revision/lead_checks/reports/charge-conjugation-and-u1.json. It prints the program
    that wrote the report (its *producer*), the verdict and name of each of its 12
    checks, and the summary that the report states about itself. The check confirms
    that our count of the verdicts PASS equals that summary.
    """),
    code(r'''
    import hashlib  # computes sha256 fingerprints
    import re  # finds patterns in texts ("regular expressions")
    import sys  # sys.stdout is the channel through which the notebook prints

    import numpy as np  # arrays of numbers


    def read_report(path):
        """The content of the JSON file path of the repository (dictionaries, lists)."""
        return json.loads(repository_file(path).read_text(encoding="utf-8"))


    def check_reproduces(condition, name, record):
        """check(condition, name, record=record), after sending the waiting output."""
        sys.stdout.flush()  # send every printed line that is still waiting
        check(condition, name, record=record)


    CC_REPORT = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
    cc = read_report(CC_REPORT)  # a dictionary with the keys producer, summary, checks
    producer = cc["producer"]
    say(f"producer: {producer}")
    for entry in cc["checks"]:  # each entry is a dictionary: name, verdict, detail
        verdict, name = entry["verdict"], entry["name"]
        say(f"  {verdict}  {name}")
    stated = cc["summary"]  # what the report says about itself: passed and total
    stated_passed, stated_total = stated["passed"], stated["total"]
    say(f"the report states: {stated_passed} passed of {stated_total}")
    passed = sum(1 for entry in cc["checks"] if entry["verdict"] == "PASS")
    number_of_checks = len(cc["checks"])
    report("checks with the verdict PASS, counted", f"{passed} of {number_of_checks}")
    check_reproduces(passed == stated["passed"] == stated["total"] == 12,
                     "12 of 12 checks of the charge-conjugation report are PASS",
                     f"{CC_REPORT}, its summary")
    '''),
    md(r"""
    Every check also has a detail text that says exactly what was verified. The next
    cell prints the details of three checks of the same report. They say, in the
    report's own words, that the author's gamma matrices are real, so that plain
    complex conjugation changes nothing at all in a real field (the charge conjugation
    of the theory is a MATRIX, not plain complex conjugation); that the
    charge-conjugation matrix which reverses the mass is $\Gamma C$; and that the
    charge $Q$ is exactly conserved. (These statements are derived from zero later in
    the book.) The detail of the third check is long; the cell prints only its last
    part, the part after the last semicolon, which states the result. `next(...)`
    returns the first entry that the expression in its brackets produces: here the
    detail of the check with the wanted name.
    """),
    code(r'''
    for wanted in ("representation_real", "charge_conjugation_matrix_minus",
                   "u1_noether_matrix_identity"):
        detail = next(entry["detail"] for entry in cc["checks"]
                      if entry["name"] == wanted)  # the first (and only) such check
        if wanted == "u1_noether_matrix_identity":
            # This detail is long; its last part, after the last "; ", is the result.
            detail = detail.rsplit("; ", 1)[-1]
        say(f"{wanted}:")
        say("    " + detail)
    '''),
    md(r"""
    ## 6. Three layouts of a report, one counting function

    The reports of the Revision record were written by different programs, and their
    checks come in three layouts:

    - **layout A**: `checks` is a list of dictionaries, each with a `name` and a
      `verdict` (written PASS or pass);
    - **layout B**: `checks` is a dictionary from the name of each check to a
      dictionary with the entry `passed` (true or false);
    - **layout C**: the self-test of the Rust function GKD has no `checks` but a list
      `results`, one per test, each with the number of `mismatches` (wrong values).

    The reports also state their own totals in different words (`summary`, `counts`,
    `checkCount`). The next cell defines `count_checks`, which counts the passed checks
    in all three layouts, and `stated_summary`, which reads the totals that a report
    states about itself. It shows one report of each layout.
    """),
    code(r'''
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


    EXAMPLES = [("A", "Revision/pairing/reports/wolfram-pairing.json"),
                ("B", "Revision/gkd_lovelock/results/lovelock-report.json"),
                ("C", "Revision/gkd_lovelock/results/gkd-selftest.json")]
    for layout, path in EXAMPLES:
        data = read_report(path)
        passed, total = count_checks(data)
        say(f"layout {layout}: {path}")
        say(f"    counted {passed} of {total}; stated {stated_summary(data)}")
    '''),
    md(r"""
    ## 7. All 27 reports of the Revision record

    The next cell first searches the whole folder Revision for reports: JSON files
    that hold a key `checks`, or, like the GKD self-test, a list `results` whose
    entries count `mismatches`. It skips three kinds of folders that are not part of
    the record: the folder Revision/textbook of this book, the folder
    Revision/workflows (the records of the programs that organised the work, rewritten
    while they run; the Revision record says itself that no result depends on them),
    and the build folders `target` of the Rust programs. It then lists the 27 verifier
    reports of the Revision record, grouped by folder, each with its engine, counts the
    checks of each with `count_checks`, and prints a table and the totals per engine.
    Three checks follow:

    1. the search finds exactly the 27 reports of the list: no report of the record is
       left out of the count (and so out of the ledger below);
    2. every check of the 27 reports has the verdict PASS;
    3. for every report that states its own totals, our count equals them (the
       self-test of layout C states only its verdict, SUCCESS, which is checked
       instead).

    `folder.rglob("*.json")` lists every JSON file in a folder and in all its
    sub-folders; `path.as_posix()` writes a path with `/`; `path.removeprefix("Revision/")`
    removes the folder name Revision/ from the front of a path, to keep the table
    narrow. Reading every JSON file of the record (a few hundred files) takes about a
    second.
    """),
    code(r'''
    def is_report(path):
        """True if the JSON file path (a Path) is a verifier report."""
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return False
        results = data.get("results")
        self_test = (isinstance(results, list) and len(results) > 0
                     and isinstance(results[0], dict) and "mismatches" in results[0])
        return "checks" in data or self_test


    SKIPPED = ("Revision/textbook/", "Revision/workflows/")  # folders that hold no report
    found_reports = []  # every report found in the folder Revision, as a relative path
    for path in sorted(repository_file("Revision").rglob("*.json")):
        relative = path.relative_to(REPO).as_posix()  # e.g. "Revision/algebra/..."
        if relative.startswith(SKIPPED) or "/target/" in relative:
            continue  # the book, the workflow records and the Rust build folders
        if is_report(path):
            found_reports.append(relative)
    report("verifier reports found in the folder Revision", len(found_reports))

    REPORTS = [  # (report, engine)
        @@REPORTS@@
    ]
    check(found_reports == sorted(path for path, _ in REPORTS),
          f"the search finds exactly the {len(REPORTS)} reports of the list")
    counted = {}  # report -> (passed, total)
    header = "report (in the folder Revision)"
    say(f"{header:59} engine   passed of all")
    for path, engine in REPORTS:
        data = read_report(path)
        counted[path] = count_checks(data)
        passed, total = counted[path]
        short = path.removeprefix("Revision/")
        say(f"{short:59} {engine:8} {passed:6d} of {total:3d}")
    all_checks = sum(total for _, total in counted.values())
    all_passed = sum(passed for passed, _ in counted.values())
    report("reports", len(REPORTS))
    report("checks in all reports", all_checks)
    engine_totals = {}  # engine -> the number of its checks
    for engine in ("Wolfram", "Python", "Rust", "lead"):
        engine_totals[engine] = sum(counted[path][1] for path, e in REPORTS
                                    if e == engine)
        report(f"checks done with the engine {engine}", engine_totals[engine])

    check(all_passed == all_checks and sum(engine_totals.values()) == all_checks,
          f"all {all_checks} checks of the {len(REPORTS)} reports have the verdict PASS")
    disagree = []  # reports whose own summary differs from our count
    for path, _ in REPORTS:
        data = read_report(path)
        stated = stated_summary(data)
        if stated is None:  # layout C: the self-test states only its verdict
            stated = counted[path] if data["verdict"] == "SUCCESS" else None
        if stated != counted[path]:
            disagree.append(path)
    check(disagree == [], "each report states the same totals that we counted")
    '''.replace("@@REPORTS@@", "\n        ".join(REPORT_LINES))),
    md(r"""
    The next cell compares our counts with two other places of the record that quote
    them. First, the table of the file Revision/README.md (its lines that start with
    a vertical bar and a folder name) prints 16 of the counts as "19/19", "49/49" and
    so on. The cell finds them in the order in which they stand there and compares
    them with our counts of the reports that the table names in that order. The
    function `re.findall` of the module `re` finds every piece of a text that matches
    a *pattern*: in the pattern `(\d+)/(\d+)`, `\d+` means one or more digits, and the
    brackets mark the two numbers to return. Second, the Kohn-Sham cross-check
    quotes, in the detail of its check `inputs_all_pass`, the counts of the three
    reports it read ("37/37 PASS" and so on), found with the pattern
    `(\d+)/(\d+) PASS`.
    """),
    code(r'''
    R = "Revision/"
    README_ORDER = [  # the reports whose counts the README table quotes, in its order
        R + "gkd_lovelock/results/lovelock-report.json",  # row gkd_lovelock/
        R + "gkd_lovelock/results/python-lovelock-report.json",
        R + "gkd_lovelock/results/wolfram-gkd-report.json",
        R + "algebra/reports/wolfram-algebra.json",  # row algebra/
        R + "algebra/reports/python-algebra.json",
        R + "theory/reports/wolfram-field-theory.json",  # row theory/
        R + "theory/reports/python-field-theory.json",
        R + "theory/reports/wolfram-scope.json",
        R + "theory/reports/python-scope.json",
        R + "field_equations_a4/reports/wolfram-a4-report.json",  # row field_equations_a4/
        R + "field_equations_a4/reports/python-a4-report.json",
        R + "field_equations_a4/reports/ks-source-conditions.json",
        R + "pairing/reports/wolfram-pairing.json",  # row pairing/
        R + "pairing/reports/python-pairing.json",
        R + "pairing/kohn_sham/reports/wolfram-t3.json",
        R + "pairing/kohn_sham/reports/python-t3.json",
    ]
    readme_lines = repository_file("Revision/README.md").read_text(
        encoding="utf-8").split("\n")
    table = "\n".join(line for line in readme_lines if line.startswith("| `"))
    quoted_readme = [(int(p), int(t)) for p, t in re.findall(r"(\d+)/(\d+)", table)]
    say("the README quotes: " + ", ".join(f"{p}/{t}" for p, t in quoted_readme))
    report("counts quoted in the README table", len(quoted_readme))
    check_reproduces(quoted_readme == [counted[path] for path in README_ORDER],
                     f"the {len(README_ORDER)} counts quoted in the README equal ours",
                     "Revision/README.md, the table of the folders")

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
    '''),
    md(r"""
    The next cell draws the number of checks of every report as a horizontal bar,
    coloured by the engine that did the computation, with the number written at the
    end of each bar.
    """),
    code(r'''
    from matplotlib.patches import Patch  # a coloured square for the legend

    ENGINE_COLOURS = {"Wolfram": "#2a78d6", "Python": "#eb6834", "Rust": "#1baf7a",
                      "lead": "#eda100"}
    ENGINE_NAMES = {"Wolfram": "Wolfram Language", "Python": "Python",
                    "Rust": "Rust", "lead": "Python, the lead's independent checks"}

    # The report with the most checks, and its number of checks.
    largest = max((path for path, _ in REPORTS), key=lambda path: counted[path][1])
    longest = counted[largest][1]
    fig, ax = plt.subplots(figsize=(6.4, 7.8))
    rows = np.arange(len(REPORTS))[::-1]  # the first report at the top
    for row, (path, engine) in zip(rows, REPORTS):
        total = counted[path][1]
        ax.barh(row, total, height=0.72, color=ENGINE_COLOURS[engine])
        ax.text(total + 0.015 * longest, row, str(total), va="center", fontsize=9)
    # The name of each report without its folder and without the ending .json:
    names = [path.rsplit("/", 1)[1].removesuffix(".json") for path, _ in REPORTS]
    ax.set_yticks(rows, labels=names, fontsize=9)
    ax.set_xlim(0, 1.12 * longest)  # room for the longest bar and its number
    ax.grid(False, axis="y")  # vertical grid lines only
    ax.set_xlabel("number of checks in the report (every one has the verdict PASS)")
    ax.set_title(f"The {len(REPORTS)} verifier reports of the Revision record: "
                 f"{all_checks} checks")
    ax.legend(handles=[Patch(color=ENGINE_COLOURS[e], label=ENGINE_NAMES[e])
                       for e in ENGINE_COLOURS], loc="lower right", fontsize=8)
    largest_name = largest.rsplit("/", 1)[1]  # its file name without the folders
    n_wolfram, n_python, n_rust, n_lead = (engine_totals[engine] for engine in
                                           ("Wolfram", "Python", "Rust", "lead"))
    totals_text = (f"{n_wolfram} Wolfram Language, {n_python} Python, {n_rust} Rust "
                   f"and {n_lead} lead checks")
    save_figure(fig, "checks_by_report",
                r"The number of checks in each of the 27 verifier reports of the "
                r"Revision record (horizontal axis, a count; one bar per report, "
                r"named on the vertical axis and grouped by folder: algebra, theory, "
                r"field equations for $a_4$, GKD and Lovelock, Kohn-Sham, pairing, "
                r"lead checks). The colour gives the engine: blue Wolfram Language, "
                r"orange Python, aqua Rust, yellow the lead's independent Python "
                f"checks. All {all_checks} checks ({totals_text}) have the verdict "
                f"PASS; the largest report is {largest_name} with {longest} checks.")
    '''),
    md(r"""
    ## 8. Two independent engines

    For eight subjects the Revision record has two independent verifiers, one in
    Wolfram Language and one in Python. The next cell draws, for each subject, the
    number of checks of the two verifiers side by side. The two verifiers do not
    check exactly the same list of statements (each also checks things the other does
    not), so the numbers differ; the point is that two programs, written separately in
    two different languages, both find the results of each subject correct.
    """),
    code(r'''
    SUBJECTS = [  # (subject, Wolfram report, Python report)
        ("the gammas, Pin(4,4), Spin(4,4)", "algebra/reports/wolfram-algebra.json",
         "algebra/reports/python-algebra.json"),
        ("Lagrangians, field equations, EMT", "theory/reports/wolfram-field-theory.json",
         "theory/reports/python-field-theory.json"),
        ("scope of the non-triviality", "theory/reports/wolfram-scope.json",
         "theory/reports/python-scope.json"),
        ("field equations for a4", "field_equations_a4/reports/wolfram-a4-report.json",
         "field_equations_a4/reports/python-a4-report.json"),
        ("GKD and the Lovelock tensors", "gkd_lovelock/results/wolfram-gkd-report.json",
         "gkd_lovelock/results/python-lovelock-report.json"),
        ("Kohn-Sham theory", "kohn_sham/reports/ks-theory-wolfram.json",
         "kohn_sham/reports/ks-theory-python.json"),
        ("pairing theorems T1, T2, Q", "pairing/reports/wolfram-pairing.json",
         "pairing/reports/python-pairing.json"),
        ("pairing theorem T3", "pairing/kohn_sham/reports/wolfram-t3.json",
         "pairing/kohn_sham/reports/python-t3.json"),
    ]
    say("subject                              Wolfram  Python")
    wolfram_numbers, python_numbers = [], []
    for subject, wolfram, python in SUBJECTS:
        wolfram_numbers.append(counted["Revision/" + wolfram][1])
        python_numbers.append(counted["Revision/" + python][1])
        say(f"{subject:36} {wolfram_numbers[-1]:7d} {python_numbers[-1]:7d}")

    widest = max(wolfram_numbers + python_numbers)  # the longest of the 16 bars
    fig, ax = plt.subplots(figsize=(7.0, 5.0))
    rows = np.arange(len(SUBJECTS))[::-1]
    height = 0.38  # two bars in each row
    ax.barh(rows + height / 2, wolfram_numbers, height, color="#2a78d6",
            edgecolor="white", linewidth=1.5, label="Wolfram Language verifier")
    ax.barh(rows - height / 2, python_numbers, height, color="#eb6834",
            edgecolor="white", linewidth=1.5, label="Python verifier (sympy)")
    for row, w, p in zip(rows, wolfram_numbers, python_numbers):
        ax.text(w + 0.015 * widest, row + height / 2, str(w), va="center", fontsize=8)
        ax.text(p + 0.015 * widest, row - height / 2, str(p), va="center", fontsize=8)
    ax.set_yticks(rows, labels=[subject for subject, _, _ in SUBJECTS])
    ax.set_xlim(0, 1.12 * widest)  # room for the longest bar and its number
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
    report("checks of the Wolfram verifiers of the eight subjects", sum(wolfram_numbers))
    report("checks of the Python verifiers of the eight subjects", sum(python_numbers))
    check(all(w > 0 and p > 0 for w, p in zip(wolfram_numbers, python_numbers)),
          "each of the eight subjects has a Wolfram and a Python verifier")
    '''),
    md(r"""
    ## 9. The honesty ledger

    The next cell writes the ledger: sixteen rows, each with a statement of the book,
    its label, a short note and the reports that verify it. Every one of the 27
    reports belongs to exactly one row. The four rows labelled HYPOTHESIS or OPEN have
    no report: nothing in the record establishes them, and their notes say why. Two
    rows of PROVED theorems name an assumption in their statement: the pairing
    theorems T2 and T3 hold with the Z2 mirror (a choice of boundary condition)
    ASSUMED. The row of the Kohn-Sham history of $a_4$ is labelled ASSUMED although it
    has five checks: those checks show that the computed Kohn-Sham states cannot be
    the source of that history in the field equations, so the history has to be
    assumed (a *prescribed background*).

    Two rows concern pairs of universes and matter and antimatter, and their words
    are chosen with care. PROVED (rows 10 and 11) are exact maps between the solutions
    of mass $+m$ and those of mass $-m$; the map T1 also reverses the charge, so a
    solution and its image carry opposite charges. That our universe actually has
    such a partner is a HYPOTHESIS (row 14: an idea of the universe and anti-universe
    kind, not a result). That the big bang creates universes in pairs is not proved:
    no creation process, rate or amplitude follows from the equations (row 15, OPEN).
    The theory as built has no baryons (the particles of ordinary matter such as the
    proton), no process that changes their number and no violation of the CP symmetry
    (the exchange of particles and antiparticles combined with a mirror reflection; it
    must be violated for matter to win over antimatter), so it does not explain why
    there is more matter than antimatter (row 16, OPEN).

    The cell prints the ledger and the notes of the rows without a report, checks that
    every report is used exactly once, that every row with a report has only passed
    checks, and counts the labels.
    """),
    code(r'''
    R = "Revision/"
    LEDGER = [  # (statement, label, note, the reports that verify it)
        ("the gammas, C, Gamma, B; Pin(4,4) and Spin(4,4)", "PROVED", "",
         [R + "algebra/reports/wolfram-algebra.json",
          R + "algebra/reports/python-algebra.json"]),
        ("Lagrangians, field equations, EMT, quantisation", "PROVED", "",
         [R + "theory/reports/wolfram-field-theory.json",
          R + "theory/reports/python-field-theory.json"]),
        ("the exact scope of the non-triviality", "PROVED", "",
         [R + "theory/reports/wolfram-scope.json",
          R + "theory/reports/python-scope.json"]),
        ("EMT conservation identities; the spin connection", "PROVED", "",
         [R + "lead_checks/reports/emt-divergence-and-spin-connection.json"]),
        ("the field equations for a4", "PROVED", "",
         [R + "field_equations_a4/reports/wolfram-a4-report.json",
          R + "field_equations_a4/reports/python-a4-report.json",
          R + "lead_checks/reports/einstein-gauss-bonnet-a4.json"]),
        ("GKD and the three Lovelock tensors", "PROVED", "",
         [R + "gkd_lovelock/results/lovelock-report.json",
          R + "gkd_lovelock/results/gkd-selftest.json",
          R + "gkd_lovelock/results/wolfram-gkd-report.json",
          R + "gkd_lovelock/results/python-lovelock-report.json"]),
        ("Kohn-Sham theory: blocks, rescaling, exchange", "PROVED", "",
         [R + "kohn_sham/reports/ks-theory-wolfram.json",
          R + "kohn_sham/reports/ks-theory-python.json"]),
        ("Kohn-Sham states along the deflating history", "COMPUTED", "",
         [R + "kohn_sham/reports/ks-rust-solver.json",
          R + "kohn_sham/reports/ks-reference.json",
          R + "kohn_sham/reports/ks-crosscheck.json",
          R + "kohn_sham/reports/ks-rust-determinism.json",
          R + "kohn_sham/reports/ks-rust-mermin-roots.json"]),
        ("the Kohn-Sham history of a4 is a prescribed background", "ASSUMED", "",
         [R + "field_equations_a4/reports/ks-source-conditions.json"]),
        ("pairing T1, T2 (Z2 mirror ASSUMED) and Q", "PROVED", "",
         [R + "pairing/reports/wolfram-pairing.json",
          R + "pairing/reports/python-pairing.json"]),
        ("T3 (Z2 mirror ASSUMED): Kohn-Sham +M and -M", "PROVED", "",
         [R + "pairing/kohn_sham/reports/wolfram-t3.json",
          R + "pairing/kohn_sham/reports/python-t3.json"]),
        ("charge conjugation C, Gamma C; U(1) charge", "PROVED", "",
         [R + "lead_checks/reports/charge-conjugation-and-u1.json"]),
        ("a time-varying dark sector from the fields", "HYPOTHESIS",
         "to be investigated; no result yet", []),
        ("our universe has a partner of opposite charge", "HYPOTHESIS",
         "the T1 maps exist; that a partner exists is not shown", []),
        ("the big bang creates universes in pairs", "OPEN",
         "not proved: no creation process, rate or amplitude", []),
        ("the theory explains matter over antimatter", "OPEN",
         "the theory as built does not explain it", []),
    ]
    say("row label       passed of all  statement")
    row_totals = []
    for number, (statement, label, note, paths) in enumerate(LEDGER, 1):
        passed = sum(counted[path][0] for path in paths)
        total = sum(counted[path][1] for path in paths)
        row_totals.append(total)
        say(f"{number:3d} {label:10} {passed:7d} of {total:3d}  {statement}")
    say("The notes of the rows without a report:")
    for number, (statement, label, note, paths) in enumerate(LEDGER, 1):
        if note:  # only the HYPOTHESIS and OPEN rows have a note
            say(f"{number:3d} {label:10} {note}")
    used = sorted(path for _, _, _, paths in LEDGER for path in paths)
    check(used == sorted(path for path, _ in REPORTS),
          "every one of the 27 reports belongs to exactly one row of the ledger")
    check(all((label in ("HYPOTHESIS", "OPEN")) == (paths == []) == (note != "")
              and all(counted[p][0] == counted[p][1] for p in paths)
              for _, label, note, paths in LEDGER),
          "rows with a report have only PASS checks; OPEN and HYPOTHESIS rows have none")
    labels = [label for _, label, _, _ in LEDGER]
    check([labels.count(name) for name in
           ("PROVED", "COMPUTED", "ASSUMED", "HYPOTHESIS", "OPEN")] == [10, 1, 1, 2, 2],
          "the ledger: 10 PROVED, 1 COMPUTED, 1 ASSUMED, 2 HYPOTHESIS and 2 OPEN rows")
    '''),
    md(r"""
    The next cell draws the ledger: one bar per row, with the row's number and
    statement written just above it, its length the number of checks of the row's
    reports, its colour the label. The rows labelled HYPOTHESIS and OPEN have no bar;
    their label and their note are written where the bar would begin.
    """),
    code(r'''
    LABEL_COLOURS = {"PROVED": "#2a78d6", "COMPUTED": "#eb6834", "ASSUMED": "#1baf7a"}
    widest = max(row_totals)  # the row with the most checks
    fig, ax = plt.subplots(figsize=(7.6, 8.0))
    rows = np.arange(len(LEDGER))[::-1]  # the first row of the ledger at the top
    for number, row, (statement, label, note, paths), total in zip(
            range(1, len(LEDGER) + 1), rows, LEDGER, row_totals):
        # The statement is written just above its bar (va="bottom": the text starts
        # at the given height and extends upwards).
        ax.text(0, row + 0.26, f"{number}. {statement}", va="bottom", fontsize=9.5)
        if total > 0:
            ax.barh(row, total, height=0.42, color=LABEL_COLOURS[label])
            ax.text(total + 0.012 * widest, row, f"{total} checks: {label}",
                    va="center", fontsize=9)
        else:  # no report: the label and the note, in grey
            ax.text(0, row, f"{label}: {note}", va="center", fontsize=9,
                    color="#52514e")
    ax.set_yticks([])  # the statements are written above the bars instead
    ax.set_xlim(0, 1.39 * widest)  # room for the longest bar and the text after it
    ax.set_ylim(-0.6, len(LEDGER) - 0.1)
    ax.grid(False, axis="y")
    ax.set_xlabel("number of checks in the reports of the row (all PASS)")
    ax.set_title("The honesty ledger at a glance")
    ax.legend(handles=[Patch(color=colour, label=label_name)
                       for label_name, colour in LABEL_COLOURS.items()],
              loc="lower right", fontsize=9)
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
    '''),
    md(r"""
    The pairing record states in its own words what the pairing theorems do NOT
    establish: the key `not_established` of the report
    Revision/pairing/reports/python-pairing.json is a list of twelve sentences. The
    next cell prints all twelve. The first says that nothing in the equations creates a
    universe or a pair of universes. This is why the ledger labels the statement "the
    big bang creates universes in pairs" OPEN.
    """),
    code(r'''
    PAIRING = "Revision/pairing/reports/python-pairing.json"
    not_established = read_report(PAIRING)["not_established"]  # a list of sentences
    for number, sentence in enumerate(not_established, 1):
        say(f"{number:2d}. {sentence}")
    check_reproduces(len(not_established) == 12
                     and not_established[0].startswith("No creation process"),
                     "the pairing record lists 12 things it does not establish, "
                     "the first: no creation process",
                     f"{PAIRING}, key not_established")
    '''),
    md(r"""
    ## 10. Fingerprints

    A sha256 fingerprint is computed from the bytes of a file (or of a text) by the
    function `hashlib.sha256`; `.hexdigest()` writes it as 64 hexadecimal characters.
    The next cell computes the fingerprints of two texts that differ only in the case
    of one letter, and shows that the two fingerprints have nothing in common.

    Then it measures this for many changes: it takes one sentence of 115 characters,
    changes each character in turn to the next character of the alphabet of the
    computer (a to b, a blank to an exclamation mark, and so on), and counts how many
    of the 64 characters of the fingerprint change. If the new fingerprint were a
    random string, each of its 64 characters would equal the old one with
    probability $1/16$, so on average $64 \cdot 15/16 = 60$ characters would change.
    The cell draws the 115 counts as a histogram (a bar chart of how often each count
    occurs).
    """),
    code(r'''
    def text_fingerprint(text):
        """The sha256 fingerprint of a text (encoded as UTF-8 bytes)."""
        return hashlib.sha256(text.encode("utf-8")).hexdigest()


    for text in ("Universes in Pairs", "Universes in pairs"):
        digest = text_fingerprint(text)
        say(f"{text}:")
        say(f"    {digest}")

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
    report("characters of the sentence", len(SENTENCE))
    report("changed characters of the fingerprint: smallest, mean, largest",
           f"{counts.min()}, {counts.mean():.2f}, {counts.max()}")

    values, how_often = np.unique(counts, return_counts=True)  # each count, how often
    fig, ax = plt.subplots()
    ax.bar(values, how_often, width=0.8, color="#2a78d6", edgecolor="white",
           linewidth=1.5, label="one-character changes of the sentence")
    ax.axvline(60, color="black", linewidth=1.2, linestyle=":",
               label="expected for a random fingerprint: 60")
    ax.set_xlim(-1, 65)
    # "\n" inside a string starts a new line of the text.
    ax.text(3, 0.55 * how_often.max(), "a fingerprint that changed only a little\n"
            "would give a bar on this side: none did", color="#52514e", fontsize=9)
    ax.set_xlabel("number of the 64 characters of the fingerprint that change")
    ax.set_ylabel("number of changed sentences")
    ax.set_title("Change one character, and the fingerprint changes completely")
    ax.legend(loc="upper left")
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
    '''),
    md(r"""
    The reports of the Revision record write down the fingerprints of the files they
    read. The report of the Wolfram check of GKD and the Lovelock tensors records 15
    (its keys `inputSha256` and `sourceSha256`: the result files, the Rust sources and
    its own Wolfram sources), the Python check of the Lovelock tensors 2 (key
    `inputsSha256`), and five Kohn-Sham reports write 7 more into the details of their
    checks, in the form `(sha256 95d8cbdd...)`, either in full (64 characters) or only
    the first 16 characters. The next cell collects all 24, computes the fingerprints of
    today's files, compares them (a shortened fingerprint with the beginning of
    today's), and prints a table. When all agree, every one of these reports was
    written from exactly the files that are in the repository today.
    """),
    code(r'''
    def file_fingerprint(path):
        """The sha256 fingerprint of the bytes of the repository file path."""
        return hashlib.sha256(repository_file(path).read_bytes()).hexdigest()


    RECORDED = []  # (report, file, recorded fingerprint)
    GKD = "Revision/gkd_lovelock/results/wolfram-gkd-report.json"
    gkd = read_report(GKD)
    for path, value in {**gkd["inputSha256"], **gkd["sourceSha256"]}.items():
        RECORDED.append((GKD, path, value))
    LOVELOCK = "Revision/gkd_lovelock/results/python-lovelock-report.json"
    for name, value in read_report(LOVELOCK)["inputsSha256"].items():
        RECORDED.append((LOVELOCK, "Revision/gkd_lovelock/results/" + name, value))
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
    for name, check_name, path in IN_DETAILS:
        report_path = "Revision/kohn_sham/reports/" + name
        detail = next(entry["detail"] for entry in read_report(report_path)["checks"]
                      if entry["name"] == check_name)
        value = re.search(r"\(sha256 ([0-9a-f]{16,64})\)", detail).group(1)
        RECORDED.append((report_path, "Revision/" + path, value))

    changed = []  # files whose fingerprint today differs from the recorded one
    for report_path, path, value in RECORDED:
        same = file_fingerprint(path).startswith(value)  # a full or shortened value
        if not same:
            changed.append(path)
        status = "same" if same else "CHANGED"
        short_path = path.removeprefix("Revision/")  # the path without Revision/
        report_name = report_path.rsplit("/", 1)[1]  # the file name of the report
        say(f"{status:7} {short_path:52} {report_name}")
    recorded_gammas = next(value for report_path, path, value in RECORDED
                           if report_path.endswith("ks-theory-wolfram.json"))
    today_gammas = file_fingerprint("Revision/algebra/gammas.json")
    say("Revision/algebra/gammas.json, recorded in ks-theory-wolfram.json and today:")
    say(f"    {recorded_gammas}")
    say(f"    {today_gammas}")
    report("recorded fingerprints compared", len(RECORDED))
    check_reproduces(len(RECORDED) == 24 and changed == [],
                     "the 24 recorded fingerprints equal the files of today",
                     f"{GKD}, keys inputSha256 and sourceSha256, and five further reports")
    '''),
    md(r"""
    ## 11. The last check

    The last cell checks that the four figure files of this notebook exist in the
    folder Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["00c_1_checks_by_report.png", "00c_2_two_verifiers.png",
                    "00c_3_ledger.png", "00c_4_fingerprints.png"]
    check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
          "the four figure files of this notebook exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 12. What this notebook showed

    - A search of the whole folder Revision finds 27 verifier reports, the 27 of our
      list. Every one of their checks has the verdict PASS; section 7 prints how many
      there are, in all and per engine (Wolfram Language, Python, Rust and the lead's
      independent Python checks).
    - Each report states the same totals that we counted, and the counts quoted in
      the file Revision/README.md and in the Kohn-Sham cross-check are the same as
      well.
    - Eight subjects are checked by two independent verifiers, one in Wolfram Language
      and one in Python.
    - Every report belongs to exactly one row of the honesty ledger. Twelve rows have
      reports (ten PROVED, one COMPUTED, one ASSUMED). Two rows are HYPOTHESIS (a
      time-varying dark sector; a partner universe of opposite charge) and two are
      OPEN: that the big bang creates universes in pairs is not proved, and the
      theory as built does not explain the excess of matter over antimatter. The
      pairing record itself lists twelve things it does not establish, the first
      being any creation process.
    - A sha256 fingerprint changes completely when one character changes, and the 24
      fingerprints that the reports recorded for their input files equal those of
      today's files.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
