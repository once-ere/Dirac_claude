#!/usr/bin/env python3
"""Audit the structure and the executed state of the dirac16complex notebook.

Origin and licence
------------------
Adapted from planet_Mercury/notebook/check_notebook.py of the rustSolveIt
engine (https://github.com/once-ere/rustSolveIt_Win11_SUNDIALS_7_8_0 at
commit a8fdff459adfe181573d7924b18bffbdf378fdb3; author: once-ere;
BSD-3-Clause, as declared in the rustSolveIt Cargo manifests).  See NOTICE,
section 2d.  Kept: rules R1-R4 and R6 of the original (how-to-run needles,
no cross-references, >= 80-character markdown lead-in before every code
cell, required headings, executed counts).  Changed: the needles and
headings are this notebook's; the original R5 (tkinter save cell) is
replaced by a headless rule (this notebook must run under run_notebook.py
AND nbconvert, so no interactive or input() cell); new rules R7-R11 audit
the executed outputs (no error, gauntlet passed), the figures (every hash
printed by the notebook matches the PNG on disk), the kernel, the
determinism settings and nbformat validity; --also audits a second executed
copy (the nbconvert one) and compares its gauntlet and figure hashes; and
--report writes artifacts/dirac16complex/numerics/notebook-report.json.

Rules:
  R1  the how-to-run instructions are present (needles below)
  R2  no cross-references ("see ... notebook", another *.ipynb named in markdown)
  R3  every code cell is preceded by a markdown cell of >= 80 characters
  R4  the required section headings exist
  R5  headless: no cell tagged "interactive", no input(); driver needles present
  R6  every code cell carries an execution_count, numbered 1..n in order
  R7  no error output; the gauntlet printed only PASS lines and ALL CHECKS PASSED
  R8  every "figure <name> sha256 <hex>" line matches the PNG on disk; the
      required figures are all there, each embedded as an image output
  R9  kernel: Python 3 (ipykernel), name python3
  R10 determinism settings: Agg backend, no software stamp, fixed dpi
  R11 the file validates against the nbformat schema (if nbformat is installed)

Usage:
  python notebooks/check_notebook.py notebooks/dirac16complex_dark_sector.ipynb
      [--also build/nbconvert/dirac16complex_dark_sector.ipynb]
      [--report artifacts/dirac16complex/numerics/notebook-report.json]
Exit 0 only if every rule passes for every audited file.  Standard library
only (nbformat optional).
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

NEEDLES_R1 = [
    "scripts/setup_solver.ps1",
    "scripts/setup_solver.sh",
    "cargo build --release",
    "python notebooks/run_notebook.py notebooks/dirac16complex_dark_sector.ipynb",
    "python -m nbconvert --to notebook --execute",
    "jupyter lab",
    "Shift+Enter",
    "Python 3 (ipykernel)",
    "DIRAC16_BIN",
]
HEADINGS_R4 = [
    "## 1. What this notebook computes",
    "## 2. How to run this notebook",
    "## 3. The words and symbols used in this notebook",
    "## 4. The physics",
    "### 4.1 The dirac16complex field",
    "### 4.2 Lagrangian",
    "### 4.3 Field equations",
    "### 4.4 Energy-momentum tensor",
    "### 4.5 Kinetic and potential energy: two exact splits",
    "### 4.6 Mode equation, norms and the expectation-value rule",
    "### 4.7 The five first-order systems exactly as handed to CVODE",
    "## 5. How this notebook talks to the simulator",
    "## 6. EXP-1",
    "## 7. EXP-2",
    "## 8. EXP-3",
    "## 9. EXP-4",
    "## 10. EXP-5",
    "## 11. The verification gauntlet",
    "## 12. Conclusions: dark matter and dark energy",
    "## 13. What we learned",
]
NEEDLES_R5 = ["def find_binary", "def run(", 'lines[-1] != "SUCCESS"', "def gauntlet", "DIRAC16_BIN"]
NEEDLES_R10 = ['matplotlib.use("Agg")', 'metadata={"Software": None}', "dpi=DPI", "DPI = "]
REQUIRED_FIGURES = [
    "exp1_frozen_observables.png", "exp1_einstein_requirement.png", "exp2_hubble.png",
    "exp2_volume_density.png", "exp2_eos_constraint.png", "exp3_w_of_a.png", "exp3_rho_psi.png",
    "exp3_ke_pe.png", "exp3_distance_modulus.png", "exp3_w0wa_plane.png", "exp4_thermal_scaling.png",
    "exp4_thermal_w.png", "exp4_thermal_split.png", "exp4_pair_spectra.png", "exp4_pair_density.png",
    "exp5_growth.png", "exp5_krein.png",
]
FIGURE_LINE = re.compile(r"^figure (\S+\.png) sha256 ([0-9a-f]{64})$")
GAUNTLET_LINE = re.compile(r"^(PASS|FAIL) - ([A-Za-z0-9_\-]+): (.*)$")


def _text(output):
    text = output.get("text", "")
    return "".join(text) if isinstance(text, list) else text


def audit(path: Path):
    """Return (problems, facts) for one notebook file."""
    problems, facts = [], {}
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"unreadable notebook JSON: {exc!r}"], facts
    cells = nb.get("cells", [])
    md_cells = [c for c in cells if c.get("cell_type") == "markdown"]
    code_cells = [c for c in cells if c.get("cell_type") == "code"]
    all_md = "\n".join("".join(c.get("source", [])) for c in md_cells)
    all_text = "\n".join("".join(c.get("source", [])) for c in cells)
    facts.update(cells=len(cells), markdownCells=len(md_cells), codeCells=len(code_cells))

    # R1
    for needle in NEEDLES_R1:
        if needle not in all_text:
            problems.append(f"R1: missing how-to-run needle {needle!r}")
    # R2
    if re.search(r"see\s+(?:the\s+)?[\w\- ]*notebook\b", all_md, re.IGNORECASE):
        problems.append("R2: markdown refers the reader to another notebook")
    for name in re.findall(r"\b[\w\-]+\.ipynb\b", all_md):
        if name != path.name and name != "dirac16complex_dark_sector.ipynb":
            problems.append(f"R2: markdown names another notebook file: {name}")
    # R3, R5 (tags), R6
    prev = None
    counts = []
    for i, cell in enumerate(cells):
        if cell.get("cell_type") == "code":
            if prev is None or prev.get("cell_type") != "markdown" or len(
                    "".join(prev.get("source", [])).strip()) < 80:
                problems.append(f"R3: code cell {i} lacks a >=80-char markdown lead-in")
            if "interactive" in cell.get("metadata", {}).get("tags", []):
                problems.append(f"R5: code cell {i} is tagged interactive (the notebook must run headless)")
            if re.search(r"(?<![\w.])input\(", "".join(cell.get("source", []))):
                problems.append(f"R5: code cell {i} calls input()")
            counts.append(cell.get("execution_count"))
        prev = cell
    if any(c is None for c in counts):
        problems.append(f"R6: {sum(c is None for c in counts)} code cell(s) never executed")
    elif counts != list(range(1, len(counts) + 1)):
        problems.append(f"R6: execution counts are not 1..{len(counts)} in order: {counts}")
    facts["executedCodeCells"] = sum(c is not None for c in counts)
    # R4
    for heading in HEADINGS_R4:
        if not re.search(r"^" + re.escape(heading), all_md, re.MULTILINE):
            problems.append(f"R4: missing heading {heading!r}")
    # R5 needles
    for needle in NEEDLES_R5:
        if needle not in all_text:
            problems.append(f"R5: missing driver needle {needle!r}")
    # R7, R8 - outputs
    gauntlet, figures, images, all_passed_line = [], {}, 0, False
    for i, cell in enumerate(code_cells):
        for out in cell.get("outputs", []):
            kind = out.get("output_type")
            if kind == "error":
                problems.append(f"R7: code cell {i} has an error output ({out.get('ename')})")
            if kind == "stream" and out.get("name") == "stderr" and "Traceback" in _text(out):
                problems.append(f"R7: code cell {i} printed a traceback on stderr")
            if kind in ("display_data", "execute_result") and "image/png" in out.get("data", {}):
                images += 1
            if kind == "stream":
                for line in _text(out).splitlines():
                    m = FIGURE_LINE.match(line.strip())
                    if m:
                        figures[m.group(1)] = m.group(2)
                    g = GAUNTLET_LINE.match(line.strip())
                    if g and "def gauntlet" in "".join(cell.get("source", [])):
                        gauntlet.append({"name": g.group(2), "passed": g.group(1) == "PASS",
                                         "detail": g.group(3)})
                    if line.strip() == "ALL CHECKS PASSED":
                        all_passed_line = True
    if not gauntlet:
        problems.append("R7: no gauntlet output found")
    if any(not g["passed"] for g in gauntlet):
        problems.append("R7: gauntlet has FAIL lines: " + ", ".join(g["name"] for g in gauntlet if not g["passed"]))
    if not all_passed_line:
        problems.append("R7: the gauntlet did not print ALL CHECKS PASSED")
    missing = sorted(set(REQUIRED_FIGURES) - set(figures))
    if missing:
        problems.append(f"R8: figures not produced: {missing}")
    fig_dir = REPO / "artifacts" / "dirac16complex" / "numerics" / "figures"
    fig_records = []
    for name in sorted(figures):
        png = fig_dir / name
        if not png.is_file():
            problems.append(f"R8: figure file missing on disk: {name}")
            continue
        digest = hashlib.sha256(png.read_bytes()).hexdigest()
        if digest != figures[name]:
            problems.append(f"R8: {name} on disk ({digest[:12]}) differs from the notebook's hash ({figures[name][:12]})")
        fig_records.append({"file": png.relative_to(REPO).as_posix(), "sha256": digest,
                            "bytes": png.stat().st_size})
    if images != len(figures):
        problems.append(f"R8: {images} embedded images for {len(figures)} figures")
    # R9
    ks = nb.get("metadata", {}).get("kernelspec", {})
    if ks.get("name") != "python3" or ks.get("display_name") != "Python 3 (ipykernel)":
        problems.append(f"R9: kernelspec is {ks!r}")
    # R10
    for needle in NEEDLES_R10:
        if needle not in all_text:
            problems.append(f"R10: missing determinism needle {needle!r}")
    # R11
    try:
        import nbformat  # noqa: PLC0415 - optional dependency
        try:
            nbformat.validate(nbformat.reads(path.read_text(encoding="utf-8"), as_version=4))
            facts["nbformatValid"] = True
        except Exception as exc:  # noqa: BLE001
            problems.append(f"R11: nbformat validation failed: {exc}")
            facts["nbformatValid"] = False
    except ImportError:
        facts["nbformatValid"] = None
    facts.update(gauntlet=gauntlet, figures=fig_records, figureHashes=figures, embeddedImages=images)
    return problems, facts


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO).as_posix()
    except ValueError:
        return path.name


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("notebook")
    parser.add_argument("--also", help="a second executed copy (e.g. the nbconvert output) to audit and compare")
    parser.add_argument("--report", help="write the notebook report JSON here")
    args = parser.parse_args()

    main_path = Path(args.notebook)
    audited = [("notebooks/run_notebook.py (standard-library exec, writes back only if every cell passes)", main_path)]
    if args.also:
        audited.append(("python -m nbconvert --to notebook --execute (Jupyter kernel python3)", Path(args.also)))
    results, bad = [], 0
    for runner, path in audited:
        problems, facts = audit(path)
        results.append((runner, path, problems, facts))
        if problems:
            bad += 1
            print(f"FAIL {path}:")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print(f"ok {path}: all structure and execution rules pass "
                  f"({facts['cells']} cells, {facts['codeCells']} code cells, "
                  f"{len(facts['gauntlet'])} gauntlet checks, {len(facts['figures'])} figures)")
    cross = []
    if len(results) == 2:
        (_, _, _, fa), (_, _, _, fb) = results
        if fa.get("figureHashes") != fb.get("figureHashes"):
            cross.append("figure hashes differ between the two executions")
        if [(g["name"], g["passed"], g["detail"]) for g in fa.get("gauntlet", [])] != \
                [(g["name"], g["passed"], g["detail"]) for g in fb.get("gauntlet", [])]:
            cross.append("gauntlet results differ between the two executions")
        for problem in cross:
            print(f"FAIL cross-check: {problem}")
        if not cross:
            print("ok cross-check: both executions printed identical gauntlet results and figure hashes")
    ok = bad == 0 and not cross

    if args.report:
        runner0, path0, problems0, f0 = results[0]
        report = {
            "schemaVersion": 1,
            "producer": "notebooks/check_notebook.py",
            "notebook": rel(path0),
            "builder": "notebooks/build_dirac16complex_notebook.py",
            "adaptedFrom": "rustSolveIt planet_Mercury/notebook (build_notebook.py, run_notebook.py, "
                           "check_notebook.py) at a8fdff459adfe181573d7924b18bffbdf378fdb3, BSD-3-Clause, once-ere",
            "kernel": "python3 (Python 3 (ipykernel))",
            "cells": f0.get("cells"),
            "markdownCells": f0.get("markdownCells"),
            "codeCells": f0.get("codeCells"),
            "executedCodeCells": f0.get("executedCodeCells"),
            "rules": ["R1 how-to-run needles", "R2 no cross-references", "R3 markdown lead-in >= 80 chars",
                      "R4 required headings", "R5 headless", "R6 executed counts 1..n",
                      "R7 no errors, gauntlet passed", "R8 figure hashes match disk",
                      "R9 kernel python3", "R10 determinism settings", "R11 nbformat schema"],
            "executions": [
                {"runner": runner, "notebook": rel(path), "problems": problems,
                 "rulesPassed": not problems, "gauntletChecks": len(facts.get("gauntlet", [])),
                 "gauntletPassed": bool(facts.get("gauntlet")) and all(g["passed"] for g in facts["gauntlet"]),
                 "nbformatValid": facts.get("nbformatValid")}
                for runner, path, problems, facts in results
            ],
            "crossExecution": {"compared": len(results) == 2, "problems": cross,
                               "identicalGauntletAndFigures": len(results) == 2 and not cross},
            "figures": f0.get("figures", []),
            "gauntlet": {
                "count": len(f0.get("gauntlet", [])),
                "passed": sum(g["passed"] for g in f0.get("gauntlet", [])),
                "failed": sum(not g["passed"] for g in f0.get("gauntlet", [])),
                "results": f0.get("gauntlet", []),
            },
            "verdict": "SUCCESS" if ok else "FAILURE",
        }
        out = Path(args.report)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {rel(out)} (verdict {report['verdict']})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
