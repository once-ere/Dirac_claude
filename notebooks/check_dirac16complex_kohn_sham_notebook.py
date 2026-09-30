#!/usr/bin/env python3
"""Audit the structure and the executed state of notebooks/dirac16complex_kohn_sham.ipynb.

Origin and licence
------------------
Adapted from the Stage-3 auditor notebooks/check_notebook.py of this
repository, which is itself adapted from planet_Mercury/notebook/check_notebook.py
of the rustSolveIt engine (https://github.com/once-ere/rustSolveIt_Win11_SUNDIALS_7_8_0
at commit a8fdff459adfe181573d7924b18bffbdf378fdb3; author: once-ere;
BSD-3-Clause, as declared in the rustSolveIt Cargo manifests).  See NOTICE,
section 2d.  The Stage-3 auditor is not reusable as it is: its needles,
headings, figure list and figure folder are those of the dark-sector notebook.

Kept from the Stage-3 auditor: rules R1-R11 (how-to-run needles, no
cross-references, >= 80-character markdown lead-in before every code cell,
required headings, headless driver, executed counts, no errors and a passed
gauntlet, figure hashes equal to the PNG files on disk and embedded as
images, kernel, determinism settings, nbformat schema), --also for a second
executed copy (the nbconvert one) with the cross-execution comparison, and
the Stage-3 report fields (notebook, executions, crossExecution, figures,
gauntlet, verdict) that the Stage-4 gate compares.

Changed for Stage 4:
  * the gauntlet of this notebook may print SKIP lines (an input file absent,
    for example a report being regenerated); a SKIP is NOT a pass: the check
    of that gauntlet line is false and the verdict is FAILURE;
  * R12: the cells (types and sources) of every audited copy equal the cells
    the builder notebooks/build_dirac16complex_kohn_sham_notebook.py writes
    NOW from the committed outputs, so a notebook whose prose or code is stale
    is refused;
  * the checker protocol of this repository: one line check_<name>=true|false
    per check (the rules and every gauntlet line), measurement_<name>=...,
    check_count, failed_check_count; exit code 0 only if every check is true;
    the report adds {checks, checkCount, failedCheckCount, failed,
    measurements, sourceSha256, fixtureSha256} to the Stage-3 fields.

Rules (checks r01..r12 hold for every audited copy):
  r01_how_to_run_needles       the how-to-run instructions are present
  r02_no_cross_references      no "see ... notebook", no other *.ipynb named in the markdown
  r03_markdown_lead_ins        every code cell follows a markdown cell of >= 80 characters
  r04_required_headings        the section headings of the notebook exist
  r05_headless_driver          no cell tagged interactive, no input(); driver needles present
  r06_executed_in_order        every code cell executed, counts 1..n in order
  r07_no_error_outputs         no error output, no traceback on stderr
  r07_gauntlet_passed          only PASS lines in the gauntlet and the line ALL CHECKS PASSED
  r08_figures_match_disk       every required figure printed with its sha256, the PNG on disk has
                               that sha256, one embedded image per figure, no unexpected figure
  r09_kernel_python3           kernelspec Python 3 (ipykernel), name python3
  r10_determinism_settings     Agg backend, no software stamp, fixed dpi
  r11_nbformat_valid           the file validates against the nbformat schema
  r12_cells_match_builder      cells equal the builder's current output
  cross_execution_identical    (with --also) both copies printed identical gauntlet results and
                               figure hashes
  gauntlet_<name>              one check per gauntlet line of the first copy (PASS = true)

Usage (from the repository root):
  python notebooks/check_dirac16complex_kohn_sham_notebook.py notebooks/dirac16complex_kohn_sham.ipynb
      [--also build/nbconvert/dirac16complex_kohn_sham.ipynb]
      [--report artifacts/dirac16complex/kohn-sham/notebook-report.json]
Standard library only, plus nbformat for R11 (the check is false without it)
and numpy/matplotlib for importing the builder (R12).
"""

import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NOTEBOOK_NAME = "dirac16complex_kohn_sham.ipynb"
BUILDER = REPO / "notebooks" / "build_dirac16complex_kohn_sham_notebook.py"
RUNNER = REPO / "notebooks" / "run_notebook.py"
KSDIR = REPO / "artifacts" / "dirac16complex" / "kohn-sham"
FIGDIR = KSDIR / "figures"
FIXTURE = REPO / "artifacts" / "dirac16complex" / "arbitrary-field" / "algebra-fixture.json"
PRODUCER = "notebooks/check_dirac16complex_kohn_sham_notebook.py"
ADAPTED_FROM = ("notebooks/check_notebook.py (Stage 3), adapted from rustSolveIt planet_Mercury/notebook "
                "(build_notebook.py, run_notebook.py, check_notebook.py) at "
                "a8fdff459adfe181573d7924b18bffbdf378fdb3, BSD-3-Clause, once-ere")
# Which program executed a copy is read from the file, not assumed: a Jupyter kernel driven by
# nbclient (nbconvert --execute, or the builder's --execute) records the kernel's language_info
# (with its "version") in the notebook metadata; notebooks/run_notebook.py leaves the builder's
# metadata {"name": "python"} untouched.
RUNNER_LABELS = ("notebooks/run_notebook.py (standard-library exec, writes back only if every cell passes)",
                 "Jupyter kernel python3 through nbclient (python -m nbconvert --to notebook --execute, "
                 "or the builder's --execute)")


def detect_runner(nb):
    info = nb.get("metadata", {}).get("language_info", {})
    return RUNNER_LABELS[1] if isinstance(info, dict) and "version" in info else RUNNER_LABELS[0]

NEEDLES_R1 = [
    "scripts/setup_solver.ps1",
    "scripts/setup_solver.sh",
    "cargo build --release",
    "python notebooks/run_notebook.py notebooks/dirac16complex_kohn_sham.ipynb",
    "python -m nbconvert --to notebook --execute",
    "python notebooks/build_dirac16complex_kohn_sham_notebook.py",
    "python notebooks/check_dirac16complex_kohn_sham_notebook.py",
    "jupyter lab",
    "Shift+Enter",
    "Python 3 (ipykernel)",
    "DIRAC16KS_BIN",
]
HEADINGS_R4 = [
    "# dirac16complex Kohn-Sham DFT in the primordial gravitational field",
    "## 1. What this notebook computes",
    "## 2. How to run this notebook",
    "## 3. The words and symbols used in this notebook",
    "## 4. The physics",
    "### 4.1 The static primordial field in the warped $y$-chart",
    "### 4.2 The $Z_2$ brane and the tip",
    "### 4.3 The Kohn-Sham ansatz and the reduced equation",
    "### 4.4 Eight 2x2 blocks",
    "### 4.5 Boundary conditions",
    "### 4.6 The Kohn-Sham fermion-gas thermodynamics pseudo-potential",
    "### 4.7 Self-consistency, occupations and energies",
    "### 4.8 The energy-momentum tensor of the Kohn-Sham state",
    "## 5. How this notebook talks to the solver",
    "### 5.1 Reading the committed outputs",
    "### 5.2 The driver: finding and running the program",
    "### 5.3 Re-running the spectrum subcommand",
    "## 6. The exact reduction and the pseudo-potential, checked in numbers",
    "### 6.1 The explicit 2x2 block basis",
    "### 6.2 The exchange closed form against the tabulated uniform gas",
    "## 7. The free spectrum",
    "## 8. Ground states: densities and the pseudo-potential",
    "### 8.1 Self-consistency histories",
    "## 9. The ground-state energy against $N$",
    "## 10. First excited states",
    "### 10.1 The particle-hole lists",
    "### 10.2 The level-crossing run",
    "## 11. Thermodynamics",
    "## 12. The energy-momentum tensor and the Einstein source",
    "## 13. Brane localisation",
    "## 14. Convergence",
    "## 15. The Rust program against the independent reference solver",
    "## 16. The verification gauntlet",
    "## 17. Conclusions",
    "## 18. What we learned",
]
NEEDLES_R5 = ["def find_binary", "def run(", 'lines[-1] != "SUCCESS"', 'run("print-config")', "def gauntlet",
              "DIRAC16KS_BIN"]
NEEDLES_R10 = ['matplotlib.use("Agg")', 'metadata={"Software": None}', "dpi=DPI", "DPI = "]
FIGURE_LINE = re.compile(r"^figure (\S+\.png) sha256 ([0-9a-f]{64})$")
GAUNTLET_LINE = re.compile(r"^(PASS|FAIL|SKIP) - ([A-Za-z0-9_\-]+): (.*)$")
RULES = [
    ("r01_how_to_run_needles", "R1 how-to-run needles"),
    ("r02_no_cross_references", "R2 no cross-references"),
    ("r03_markdown_lead_ins", "R3 markdown lead-in >= 80 chars before every code cell"),
    ("r04_required_headings", "R4 required headings"),
    ("r05_headless_driver", "R5 headless, driver needles"),
    ("r06_executed_in_order", "R6 executed counts 1..n"),
    ("r07_no_error_outputs", "R7 no error outputs"),
    ("r07_gauntlet_passed", "R7 gauntlet: only PASS lines (a SKIP is not a pass), ALL CHECKS PASSED"),
    ("r08_figures_match_disk", "R8 figure hashes match the PNG files on disk, one embedded image each"),
    ("r09_kernel_python3", "R9 kernel python3"),
    ("r10_determinism_settings", "R10 determinism settings"),
    ("r11_nbformat_valid", "R11 nbformat schema"),
    ("r12_cells_match_builder", "R12 cells equal the builder's current output"),
]


def sha256_file(path: Path):
    path = Path(path)
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def rel(path: Path) -> str:
    try:
        return Path(path).resolve().relative_to(REPO).as_posix()
    except ValueError:
        return Path(path).name


def _text(output):
    text = output.get("text", "")
    return "".join(text) if isinstance(text, list) else text


def _source(cell):
    src = cell.get("source", "")
    return "".join(src) if isinstance(src, list) else src


def cell_signature(cells):
    """[(cell_type, source)] of a notebook's cells: what R12 compares."""
    return [(c.get("cell_type"), _source(c)) for c in cells]


def signature_sha256(cells):
    text = json.dumps(cell_signature(cells), ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_builder():
    """Import the builder (it reads the committed outputs); returns (module, None) or (None, error)."""
    try:
        spec = importlib.util.spec_from_file_location("_ks_notebook_builder", BUILDER)
        module = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(module)
        return module, None
    except Exception as exc:  # noqa: BLE001 - reported as a failed R12
        return None, f"{type(exc).__name__}: {exc}"


def audit(path: Path, expected=None, required_figures=None, figure_dir: Path = FIGDIR):
    """Audit one notebook file.  expected: the builder's cells (R12; None = not available),
    required_figures: sorted figure names.  Returns (rule_ok {rule: bool}, problems, facts)."""
    problems = {name: [] for name, _ in RULES}
    facts = {}
    try:
        nb = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        for name, _ in RULES:
            problems[name].append(f"unreadable notebook JSON: {type(exc).__name__}")
        return {name: False for name, _ in RULES}, problems, facts
    cells = nb.get("cells", [])
    md_cells = [c for c in cells if c.get("cell_type") == "markdown"]
    code_cells = [c for c in cells if c.get("cell_type") == "code"]
    all_md = "\n".join(_source(c) for c in md_cells)
    all_text = "\n".join(_source(c) for c in cells)
    facts.update(cells=len(cells), markdownCells=len(md_cells), codeCells=len(code_cells),
                 cellsSha256=signature_sha256(cells), runner=detect_runner(nb))

    # R1
    for needle in NEEDLES_R1:
        if needle not in all_text:
            problems["r01_how_to_run_needles"].append(f"missing how-to-run needle {needle!r}")
    # R2
    if re.search(r"see\s+(?:the\s+)?[\w\- ]*notebook\b", all_md, re.IGNORECASE):
        problems["r02_no_cross_references"].append("the markdown refers the reader to another notebook")
    for name in sorted(set(re.findall(r"\b[\w\-]+\.ipynb\b", all_md))):
        if name != NOTEBOOK_NAME:
            problems["r02_no_cross_references"].append(f"the markdown names another notebook file: {name}")
    # R3, R5 (tags, input), R6
    prev, counts = None, []
    for i, cell in enumerate(cells):
        if cell.get("cell_type") == "code":
            if prev is None or prev.get("cell_type") != "markdown" or len(_source(prev).strip()) < 80:
                problems["r03_markdown_lead_ins"].append(f"code cell {i} lacks a >= 80-character markdown lead-in")
            if "interactive" in cell.get("metadata", {}).get("tags", []):
                problems["r05_headless_driver"].append(f"code cell {i} is tagged interactive")
            if re.search(r"(?<![\w.])input\(", _source(cell)):
                problems["r05_headless_driver"].append(f"code cell {i} calls input()")
            counts.append(cell.get("execution_count"))
        prev = cell
    if any(c is None for c in counts):
        problems["r06_executed_in_order"].append(f"{sum(c is None for c in counts)} code cell(s) never executed")
    elif counts != list(range(1, len(counts) + 1)):
        problems["r06_executed_in_order"].append(f"execution counts are not 1..{len(counts)} in order")
    facts["executedCodeCells"] = sum(c is not None for c in counts)
    # R4
    for heading in HEADINGS_R4:
        if not re.search(r"^" + re.escape(heading), all_md, re.MULTILINE):
            problems["r04_required_headings"].append(f"missing heading {heading!r}")
    # R5 needles
    for needle in NEEDLES_R5:
        if needle not in all_text:
            problems["r05_headless_driver"].append(f"missing driver needle {needle!r}")
    # R7, R8: outputs
    gauntlet, figures, images, all_passed_line, gauntlet_cells = [], {}, 0, False, 0
    for i, cell in enumerate(code_cells):
        is_gauntlet = "def gauntlet" in _source(cell)
        gauntlet_cells += is_gauntlet
        for out in cell.get("outputs", []):
            kind = out.get("output_type")
            if kind == "error":
                problems["r07_no_error_outputs"].append(f"code cell {i} has an error output ({out.get('ename')})")
            if kind == "stream" and out.get("name") == "stderr" and "Traceback" in _text(out):
                problems["r07_no_error_outputs"].append(f"code cell {i} printed a traceback on stderr")
            if kind in ("display_data", "execute_result") and "image/png" in out.get("data", {}):
                images += 1
            if kind != "stream":
                continue
            for line in _text(out).splitlines():
                line = line.strip()
                m = FIGURE_LINE.match(line)
                if m:
                    if m.group(1) in figures:
                        problems["r08_figures_match_disk"].append(f"figure {m.group(1)} written twice")
                    figures[m.group(1)] = m.group(2)
                g = GAUNTLET_LINE.match(line)
                if g and is_gauntlet:
                    gauntlet.append({"name": g.group(2), "status": g.group(1), "passed": g.group(1) == "PASS",
                                     "detail": g.group(3)})
                if is_gauntlet and line == "ALL CHECKS PASSED":
                    all_passed_line = True
    if gauntlet_cells != 1:
        problems["r07_gauntlet_passed"].append(f"{gauntlet_cells} gauntlet cells (expected 1)")
    if not gauntlet:
        problems["r07_gauntlet_passed"].append("no gauntlet output found")
    names = [g["name"] for g in gauntlet]
    if len(set(names)) != len(names):
        problems["r07_gauntlet_passed"].append("a gauntlet check name is printed twice")
    for status in ("FAIL", "SKIP"):
        bad = [g["name"] for g in gauntlet if g["status"] == status]
        if bad:
            problems["r07_gauntlet_passed"].append(f"gauntlet {status} lines: {', '.join(bad)}")
    if not all_passed_line:
        problems["r07_gauntlet_passed"].append("the gauntlet did not print ALL CHECKS PASSED")
    required = list(required_figures or [])
    missing = sorted(set(required) - set(figures))
    extra = sorted(set(figures) - set(required)) if required else []
    if not required:
        problems["r08_figures_match_disk"].append("the required figure list is not available (builder import failed)")
    if missing:
        problems["r08_figures_match_disk"].append(f"figures not produced: {missing}")
    if extra:
        problems["r08_figures_match_disk"].append(f"figures not in the required list: {extra}")
    fig_records = []
    for name in sorted(figures):
        png = Path(figure_dir) / name
        if not png.is_file():
            problems["r08_figures_match_disk"].append(f"figure file missing on disk: {name}")
            continue
        digest = sha256_file(png)
        if digest != figures[name]:
            problems["r08_figures_match_disk"].append(
                f"{name} on disk ({digest[:12]}) differs from the notebook's hash ({figures[name][:12]})")
        fig_records.append({"file": rel(png), "sha256": digest, "bytes": png.stat().st_size})
    if images != len(figures):
        problems["r08_figures_match_disk"].append(f"{images} embedded images for {len(figures)} figures")
    # R9
    ks = nb.get("metadata", {}).get("kernelspec", {})
    if ks.get("name") != "python3" or ks.get("display_name") != "Python 3 (ipykernel)":
        problems["r09_kernel_python3"].append(f"kernelspec is {ks!r}")
    # R10
    for needle in NEEDLES_R10:
        if needle not in all_text:
            problems["r10_determinism_settings"].append(f"missing determinism needle {needle!r}")
    # R11
    try:
        import nbformat  # noqa: PLC0415 - optional dependency
        try:
            nbformat.validate(nbformat.reads(Path(path).read_text(encoding="utf-8"), as_version=4))
            facts["nbformatValid"] = True
        except Exception as exc:  # noqa: BLE001
            problems["r11_nbformat_valid"].append(f"nbformat validation failed: {type(exc).__name__}")
            facts["nbformatValid"] = False
    except ImportError:
        problems["r11_nbformat_valid"].append("nbformat is not installed: the schema was not checked")
        facts["nbformatValid"] = None
    # R12
    if expected is None:
        problems["r12_cells_match_builder"].append("the builder's cells are not available (builder import failed)")
    else:
        mine, theirs = cell_signature(cells), cell_signature(expected)
        if mine != theirs:
            differ = [i for i in range(min(len(mine), len(theirs))) if mine[i] != theirs[i]]
            problems["r12_cells_match_builder"].append(
                f"{len(mine)} cells vs the builder's {len(theirs)}; differing cells {differ[:10]}"
                " (rebuild: python notebooks/build_dirac16complex_kohn_sham_notebook.py, then execute)")
    facts.update(gauntlet=gauntlet, figures=fig_records, figureHashes=figures, embeddedImages=images)
    ok = {name: not problems[name] for name, _ in RULES}
    return ok, problems, facts


def input_hashes():
    """sha256 of the files the notebook reads at the top level (None = absent)."""
    names = ["artifacts/dirac16complex/arbitrary-field/algebra-fixture.json",
             "artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json",
             "artifacts/dirac16complex/kohn-sham/exchange-table.json",
             "artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json",
             "artifacts/dirac16complex/kohn-sham/python-theory-report.json",
             "artifacts/dirac16complex/kohn-sham/rust/determinism-report.json",
             "artifacts/dirac16complex/kohn-sham/reference/reference-summary.json",
             "artifacts/dirac16complex/kohn-sham/python-check-report.json",
             "scripts/check_dirac16complex_kohn_sham.py"]
    names += [f"artifacts/dirac16complex/kohn-sham/rust/{sub}/summary.json"
              for sub in ("spectrum", "scf", "excited", "thermo", "emt")]
    return {name: sha256_file(REPO / name) for name in names}


def emit(name, value):
    if isinstance(value, bool):
        value = "true" if value else "false"
    elif isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False, sort_keys=True)
    print(f"{name}={value}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("notebook", help="the executed notebook (the committed copy: executed by run_notebook.py)")
    parser.add_argument("--also", help="a second executed copy (the nbconvert one) to audit and compare")
    parser.add_argument("--report", help="write the notebook report JSON here")
    args = parser.parse_args(argv)

    builder, builder_error = load_builder()
    expected = builder.build_notebook()["cells"] if builder is not None else None
    required = list(builder.REQUIRED_FIGURES) if builder is not None else []
    descriptions = dict(builder.FIGURE_DESCRIPTIONS) if builder is not None else {}

    audited = [Path(args.notebook)] + ([Path(args.also)] if args.also else [])
    results = []
    for path in audited:
        ok, problems, facts = audit(path, expected, required)
        results.append((facts.get("runner", "unreadable"), path, ok, problems, facts))

    checks, measurements = {}, {}
    for name, _ in RULES:
        checks[name] = all(r[2][name] for r in results)
    for index, (_, _, ok, problems, _) in enumerate(results):
        for name, _ in RULES:
            if problems[name]:
                measurements[f"problems_execution{index}_{name}"] = problems[name]
    cross = []
    if len(results) == 2:
        fa, fb = results[0][4], results[1][4]
        if fa.get("figureHashes") != fb.get("figureHashes"):
            cross.append("figure hashes differ between the two executions")
        if [(g["name"], g["status"], g["detail"]) for g in fa.get("gauntlet", [])] != \
                [(g["name"], g["status"], g["detail"]) for g in fb.get("gauntlet", [])]:
            cross.append("gauntlet results differ between the two executions")
        checks["cross_execution_identical"] = not cross
        if cross:
            measurements["crossExecutionProblems"] = cross
    f0 = results[0][4]
    for g in f0.get("gauntlet", []):
        checks["gauntlet_" + g["name"]] = g["status"] == "PASS"
    gl = f0.get("gauntlet", [])
    measurements.update({
        "cells": f0.get("cells"), "codeCells": f0.get("codeCells"), "markdownCells": f0.get("markdownCells"),
        "executedCodeCells": f0.get("executedCodeCells"), "embeddedImages": f0.get("embeddedImages"),
        "figures": len(f0.get("figures", [])), "requiredFigures": len(required),
        "gauntletCount": len(gl), "gauntletPassed": sum(g["status"] == "PASS" for g in gl),
        "gauntletFailed": [g["name"] for g in gl if g["status"] == "FAIL"],
        "gauntletSkipped": [g["name"] for g in gl if g["status"] == "SKIP"],
        "executions": len(results),
    })
    if builder_error:
        measurements["builderImportError"] = builder_error
    failed = sorted(name for name, passed in checks.items() if not passed)
    verdict = "SUCCESS" if not failed else "FAILURE"

    for name, passed in checks.items():
        emit("check_" + name, passed)
    for name, value in measurements.items():
        emit("measurement_" + name, value)
    emit("check_count", len(checks))
    emit("failed_check_count", len(failed))
    for runner, path, ok, problems, facts in results:
        flat = [p for name, _ in RULES for p in problems[name]]
        state = "ok" if not flat else "FAIL"
        print(f"{state} {rel(path)} ({runner.split(' (')[0]}): {facts.get('cells')} cells, "
              f"{facts.get('codeCells')} code cells, {len(facts.get('gauntlet', []))} gauntlet lines, "
              f"{len(facts.get('figures', []))} figures" + ("" if not flat else "; " + "; ".join(flat[:12])))

    if args.report:
        figures = [dict(f, description=descriptions.get(Path(f["file"]).name, "")) for f in f0.get("figures", [])]
        report = {
            "schemaVersion": 1,
            "producer": PRODUCER,
            "notebook": rel(results[0][1]),
            "builder": rel(BUILDER),
            "runner": rel(RUNNER),
            "adaptedFrom": ADAPTED_FROM,
            "kernel": "python3 (Python 3 (ipykernel))",
            "fixtureSha256": sha256_file(FIXTURE),
            "cells": f0.get("cells"),
            "markdownCells": f0.get("markdownCells"),
            "codeCells": f0.get("codeCells"),
            "executedCodeCells": f0.get("executedCodeCells"),
            "rules": [text for _, text in RULES] + ["cross-execution identical gauntlet and figure hashes (--also)"],
            "checks": checks,
            "checkCount": len(checks),
            "failedCheckCount": len(failed),
            "failed": failed,
            "measurements": measurements,
            "sourceSha256": dict({"builder": sha256_file(BUILDER), "auditor": sha256_file(Path(__file__)),
                                  "runner": sha256_file(RUNNER), "notebookCells": f0.get("cellsSha256")},
                                 **input_hashes()),
            "executions": [
                {"runner": runner, "notebook": rel(path),
                 "problems": [p for name, _ in RULES for p in problems[name]],
                 "rulesPassed": all(ok.values()), "gauntletChecks": len(facts.get("gauntlet", [])),
                 "gauntletPassed": bool(facts.get("gauntlet")) and all(g["passed"] for g in facts["gauntlet"]),
                 "nbformatValid": facts.get("nbformatValid"), "cellsSha256": facts.get("cellsSha256")}
                for runner, path, ok, problems, facts in results
            ],
            "crossExecution": {"compared": len(results) == 2, "problems": cross,
                               "identicalGauntletAndFigures": len(results) == 2 and not cross},
            "figures": figures,
            "gauntlet": {
                "count": len(gl),
                "passed": sum(g["status"] == "PASS" for g in gl),
                "failed": sum(g["status"] == "FAIL" for g in gl),
                "skipped": sum(g["status"] == "SKIP" for g in gl),
                "results": gl,
            },
            "verdict": verdict,
        }
        out = Path(args.report)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {rel(out)} (verdict {verdict})")
    print(f"notebook_audit={'OK' if verdict == 'SUCCESS' else 'FAILURE'}")
    return 0 if verdict == "SUCCESS" else 1


if __name__ == "__main__":
    sys.exit(main())
