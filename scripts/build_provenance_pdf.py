#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Written for this repository on 2026-09-25.  It packages as one command the
# provenance-PDF procedure that the gates scripts/verify_phase*.ps1 and .sh
# of https://github.com/once-ere/dirac (GPL-3.0-or-later) spell out step by
# step: build the .tex twice, three pdflatex passes into two fresh
# directories, scan the logs for warnings, check byte identity and structure,
# copy the PDF.  New relative to those gates: the edition registry
# provenance/pdf-specifications.json (--register), the two builder runs use
# different PYTHONHASHSEED values, and a JSON report is written.
"""Build one provenance PDF deterministically, then verify or register it.

For a Markdown file D/X.md inside the repository (normally provenance/X.md):

 1. run scripts/build_dissertation_tex.py twice, D/X.tex (PYTHONHASHSEED=0)
    and build/X/X-repeat.tex (PYTHONHASHSEED=1); both must succeed and be
    byte-identical;
 2. run pdflatex -interaction=nonstopmode -halt-on-error -jobname=X three
    times on each: D/X.tex into build/X/pdf-a and build/X/X-repeat.tex into
    build/X/pdf-b (both directories are deleted and recreated first).
    pdflatex always runs with the repository root as working directory and
    is given the .tex and the output directory as root-relative paths.  This
    is what makes figures work: a figure line ![caption](path.png) becomes
    \\includegraphics{path.png} with the path relative to the repository
    root and no \\graphicspath (the builder's header explains why), and TeX
    looks such a path up in the working directory.  The builder is run with
    --image-root <root>, so it checks every figure file before pdflatex
    starts, and each figure's sha256 is recorded in the report's
    sourceSha256;
 3. scan both final pdflatex logs with WARNING_PATTERN (case-insensitive, as
    grep -Ei and Select-String in the dirac-main gates); any match fails;
 4. require the two PDFs to be byte-identical, to start with %PDF- and end
    with %%EOF, to have only US-letter media boxes [0 0 612 792] and at least
    one page;
 5. verify mode (default): the edition (default: X lower-cased, "_" -> "-")
    must be registered in provenance/pdf-specifications.json with this path,
    page count and sha256; --register mode: record path, pages and sha256
    there instead (replacing an older entry of the same edition);
 6. copy build/X/pdf-a/X.pdf to D/X.pdf, only when every earlier check
    passed (in --register mode the copy precedes the registry update).

Prints check_<name>=true|false and measurement_<name>=<value> lines,
check_count and failed_check_count, writes build/X/build-provenance-pdf.json
and exits 1 if any check failed (2 on usage errors).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    from scripts import build_dissertation_tex
    from scripts import check_dissertation_pdf
    from scripts import check_provenance_pdf
except ModuleNotFoundError:
    import build_dissertation_tex
    import check_dissertation_pdf
    import check_provenance_pdf


SCRIPT_DIRECTORY = Path(__file__).resolve().parent
REPOSITORY_ROOT = SCRIPT_DIRECTORY.parent
WARNING_PATTERN = re.compile(
    r"^!|LaTeX Warning|Package .* Warning|Overfull|Underfull|"
    r"Undefined control sequence",
    re.IGNORECASE | re.MULTILINE,
)
PDFLATEX_FALLBACK = Path(
    "C:/Program Files/MiKTeX/miktex/bin/x64/pdflatex.exe"
)
PASSES = 3
HASH_SEEDS = ("0", "1")
PDFLATEX_TIMEOUT_SECONDS = 900
SOURCE_SCRIPTS = (
    "scripts/build_dissertation_tex.py",
    "scripts/build_provenance_pdf.py",
    "scripts/check_dissertation_pdf.py",
    "scripts/check_provenance_pdf.py",
)
COMMON_CHECKS = (
    "texBuildExitCodes",
    "texRepeatByteIdentity",
    "pdflatexExitCodes",
    "logWarningFree",
    "pdfRepeatByteIdentity",
    "pdfHeader",
    "pdfEndMarker",
    "pdfLetterMediaBox",
    "pdfPageCountPositive",
)
VERIFY_CHECKS = (
    "editionRegistered",
    "registeredPath",
    "registeredPageCount",
    "registeredSha256",
    "provenancePdfCopy",
)
REGISTER_CHECKS = ("provenancePdfCopy", "registryUpdated")
TIMEOUT_EXIT_CODE = 124


class UsageError(Exception):
    """The command line names something that cannot be built."""


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--edition")
    parser.add_argument(
        "--register",
        action="store_true",
        help="record pages and sha256 in the registry instead of verifying",
    )
    parser.add_argument(
        "--keep-heading-numbers",
        action="store_true",
        help="do not pass --strip-heading-numbers to the builder",
    )
    parser.add_argument("--developer-layout", action="store_true")
    parser.add_argument(
        "--author", default=build_dissertation_tex.DEFAULT_AUTHOR
    )
    parser.add_argument("--date", default=build_dissertation_tex.DEFAULT_DATE)
    parser.add_argument("--pdflatex")
    parser.add_argument(
        "--repository-root", type=Path, default=REPOSITORY_ROOT
    )
    parser.add_argument(
        "--specifications",
        type=Path,
        help=(
            "registry file "
            "(default: <root>/provenance/pdf-specifications.json)"
        ),
    )
    return parser.parse_args()


def default_edition(stem: str) -> str:
    return stem.lower().replace("_", "-")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find_pdflatex(explicit: str | None) -> str:
    if explicit:
        return explicit
    found = shutil.which("pdflatex")
    if found:
        return found
    if PDFLATEX_FALLBACK.exists():
        return str(PDFLATEX_FALLBACK)
    raise FileNotFoundError("pdflatex was not found on PATH or in MiKTeX")


def scan_log(text: str) -> list[str]:
    """Return, once each, the log lines that match WARNING_PATTERN."""
    lines = []
    seen_starts = set()
    for match in WARNING_PATTERN.finditer(text):
        start = text.rfind("\n", 0, match.start()) + 1
        if start in seen_starts:
            continue
        seen_starts.add(start)
        end = text.find("\n", match.start())
        lines.append(text[start:end if end >= 0 else len(text)].rstrip("\r"))
    return lines


def run_logged(
    command: list[str],
    cwd: Path,
    log_path: Path,
    environment: dict[str, str] | None = None,
    timeout: int | None = None,
) -> int:
    """Run command, store its combined output in log_path, return the code."""
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
        output, code = completed.stdout, completed.returncode
    except subprocess.TimeoutExpired as error:
        output = (error.output or b"") + b"\nTIMEOUT\n"
        code = TIMEOUT_EXIT_CODE
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_bytes(
        ("command=" + " ".join(command) + "\n").encode("utf-8")
        + output.replace(b"\r\n", b"\n")
        + f"\nexit_code={code}\n".encode("utf-8")
    )
    return code


def pdflatex_version(pdflatex: str) -> str:
    try:
        completed = subprocess.run(
            [pdflatex, "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=120,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return "unknown"
    lines = completed.stdout.decode("utf-8", "replace").splitlines()
    return lines[0].strip() if lines else "unknown"


def relative_posix(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root).as_posix()


def build_and_check(arguments: argparse.Namespace) -> tuple[
    dict[str, bool], dict[str, object], dict[str, str], Path
]:
    root = arguments.repository_root.resolve()
    markdown = arguments.markdown.resolve()
    if markdown.suffix != ".md" or not markdown.is_file():
        raise UsageError(f"{markdown} is not an existing .md file")
    try:
        markdown_relative = relative_posix(markdown, root)
    except ValueError:
        raise UsageError(
            f"{markdown} is not inside the repository root {root}"
        )
    stem = markdown.stem
    edition = arguments.edition or default_edition(stem)
    if not check_provenance_pdf.EDITION_PATTERN.fullmatch(edition):
        raise UsageError(
            f"edition name {edition!r} must match "
            f"{check_provenance_pdf.EDITION_PATTERN.pattern} (use --edition)"
        )
    specifications = (
        arguments.specifications.resolve()
        if arguments.specifications
        else root / "provenance" / "pdf-specifications.json"
    )
    tex = markdown.with_suffix(".tex")
    pdf = markdown.with_suffix(".pdf")
    tex_relative = relative_posix(tex, root)
    pdf_relative = relative_posix(pdf, root)
    build_directory = root / "build" / stem
    repeat_tex = build_directory / f"{stem}-repeat.tex"
    logs = build_directory / "logs"
    output_directories = {
        "a": build_directory / "pdf-a",
        "b": build_directory / "pdf-b",
    }
    report_path = build_directory / "build-provenance-pdf.json"

    for stale in (logs, *output_directories.values()):
        shutil.rmtree(stale, ignore_errors=True)
        if stale.exists():
            raise UsageError(f"could not remove {stale} (file in use?)")
    for stale in (repeat_tex, report_path):
        stale.unlink(missing_ok=True)
    for directory in (logs, *output_directories.values()):
        directory.mkdir(parents=True, exist_ok=True)

    mode = "register" if arguments.register else "verify"
    names = COMMON_CHECKS + (
        REGISTER_CHECKS if arguments.register else VERIFY_CHECKS
    )
    checks = {name: False for name in names}
    measurements: dict[str, object] = {
        "mode": mode,
        "edition": edition,
        "markdown": markdown_relative,
        "markdownSha256": sha256_file(markdown),
        "specifications": specifications.as_posix(),
    }
    pdflatex = find_pdflatex(arguments.pdflatex)
    measurements["pdflatexVersion"] = pdflatex_version(pdflatex)

    def finish(stopped_after: str | None) -> tuple[
        dict[str, bool], dict[str, object], dict[str, str], Path
    ]:
        if stopped_after is not None:
            measurements["stoppedAfter"] = stopped_after
        sources = {markdown_relative: sha256_file(markdown)}
        if tex.exists():
            sources[tex_relative] = sha256_file(tex)
        for figure in build_dissertation_tex.figure_paths(
            markdown.read_text(encoding="utf-8", errors="replace")
        ):
            try:
                build_dissertation_tex.validate_figure_path(figure, 0)
            except ValueError:
                continue
            figure_path = root / figure
            if figure_path.is_file():
                sources[figure] = sha256_file(figure_path)
        for script in SOURCE_SCRIPTS:
            script_path = root / script
            if not script_path.exists():
                script_path = SCRIPT_DIRECTORY / Path(script).name
            sources[script] = sha256_file(script_path)
        return checks, measurements, sources, report_path

    # 1. two independent builder runs
    builder = [
        sys.executable,
        str(SCRIPT_DIRECTORY / "build_dissertation_tex.py"),
        "--author",
        arguments.author,
        "--date",
        arguments.date,
        "--image-root",
        str(root),
    ]
    if not arguments.keep_heading_numbers:
        builder.append("--strip-heading-numbers")
    if arguments.developer_layout:
        builder.append("--developer-layout")
    exit_codes = []
    for seed, output in zip(
        HASH_SEEDS, (tex_relative, relative_posix(repeat_tex, root))
    ):
        environment = dict(os.environ, PYTHONHASHSEED=seed)
        exit_codes.append(
            run_logged(
                builder + ["--input", markdown_relative, "--output", output],
                root,
                logs / f"build-tex-seed{seed}.log",
                environment,
            )
        )
    measurements["texBuildExitCodes"] = exit_codes
    checks["texBuildExitCodes"] = exit_codes == [0, 0]
    if not checks["texBuildExitCodes"]:
        return finish("texBuildExitCodes")
    tex_bytes = tex.read_bytes()
    checks["texRepeatByteIdentity"] = tex_bytes == repeat_tex.read_bytes()
    measurements["texSha256"] = hashlib.sha256(tex_bytes).hexdigest()
    measurements["texBytes"] = len(tex_bytes)
    if not checks["texRepeatByteIdentity"]:
        return finish("texRepeatByteIdentity")

    # 2. three pdflatex passes into two fresh directories
    tex_sources = {"a": tex_relative, "b": relative_posix(repeat_tex, root)}
    pdflatex_codes = []
    for label in ("a", "b"):
        for number in range(1, PASSES + 1):
            code = run_logged(
                [
                    pdflatex,
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    f"-jobname={stem}",
                    "-output-directory="
                    + relative_posix(output_directories[label], root),
                    tex_sources[label],
                ],
                root,
                logs / f"pdflatex-{label}{number}.log",
                timeout=PDFLATEX_TIMEOUT_SECONDS,
            )
            pdflatex_codes.append(code)
            if code != 0:
                break
        if pdflatex_codes[-1] != 0:
            break
    measurements["pdflatexExitCodes"] = pdflatex_codes
    checks["pdflatexExitCodes"] = pdflatex_codes == [0] * (2 * PASSES)
    if not checks["pdflatexExitCodes"]:
        return finish("pdflatexExitCodes")

    # 3. warning scan of both final logs
    warnings = []
    for label in ("a", "b"):
        log_text = (output_directories[label] / f"{stem}.log").read_bytes()
        for line in scan_log(log_text.decode("latin-1")):
            warnings.append(f"pdf-{label}: {line}")
    measurements["warningLineCount"] = len(warnings)
    for line in warnings:
        print(f"latex_warning={line}")
    checks["logWarningFree"] = not warnings

    # 4. byte identity and structure
    pdf_a = output_directories["a"] / f"{stem}.pdf"
    pdf_b = output_directories["b"] / f"{stem}.pdf"
    pdf_bytes = pdf_a.read_bytes()
    checks["pdfRepeatByteIdentity"] = pdf_bytes == pdf_b.read_bytes()
    page_count = len(check_dissertation_pdf.PAGE_PATTERN.findall(pdf_bytes))
    media_boxes = check_dissertation_pdf.parse_media_boxes(pdf_bytes)
    pdf_sha256 = check_dissertation_pdf.sha256_bytes(pdf_bytes)
    checks["pdfHeader"] = pdf_bytes.startswith(b"%PDF-")
    checks["pdfEndMarker"] = pdf_bytes.rstrip().endswith(b"%%EOF")
    checks["pdfLetterMediaBox"] = media_boxes == [(0.0, 0.0, 612.0, 792.0)]
    checks["pdfPageCountPositive"] = page_count >= 1
    measurements.update(
        {
            "pdfSha256": pdf_sha256,
            "pdfBytes": len(pdf_bytes),
            "pageCount": page_count,
            "mediaBoxes": media_boxes,
        }
    )
    if not all(checks[name] for name in COMMON_CHECKS):
        return finish("structure")

    if arguments.register:
        # 6. copy, then 5. register
        shutil.copyfile(pdf_a, pdf)
        checks["provenancePdfCopy"] = pdf.read_bytes() == pdf_bytes
        if not checks["provenancePdfCopy"]:
            return finish("provenancePdfCopy")
        entry = check_provenance_pdf.register_edition(
            specifications, edition, pdf_relative, page_count, pdf_sha256
        )
        checks["registryUpdated"] = entry == {
            "path": pdf_relative,
            "pages": page_count,
            "sha256": pdf_sha256,
        }
        measurements["registeredEntry"] = json.dumps(entry, sort_keys=False)
        return finish(None)

    # 5. verify against the registry, then 6. copy
    registry = check_provenance_pdf.load_specifications(specifications)
    specification = registry.get(edition)
    checks["editionRegistered"] = specification is not None
    if specification is None:
        print(
            f"ERROR: edition {edition!r} is not registered in "
            f"{specifications}; build it once with --register",
            file=sys.stderr,
        )
        return finish("editionRegistered")
    measurements["registeredPages"] = specification["pages"]
    measurements["registeredSha256"] = specification["sha256"]
    checks["registeredPath"] = specification["path"] == pdf_relative
    checks["registeredPageCount"] = specification["pages"] == page_count
    checks["registeredSha256"] = specification["sha256"] == pdf_sha256
    if not all(checks[name] for name in names if name != "provenancePdfCopy"):
        return finish("registry")
    shutil.copyfile(pdf_a, pdf)
    checks["provenancePdfCopy"] = pdf.read_bytes() == pdf_bytes
    return finish(None)


def main() -> int:
    arguments = parse_arguments()
    try:
        checks, measurements, sources, report_path = build_and_check(
            arguments
        )
    except (
        UsageError,
        check_provenance_pdf.SpecificationError,
        FileNotFoundError,
    ) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    report = {
        "schemaVersion": 1,
        "producer": "scripts/build_provenance_pdf.py",
        "checks": checks,
        "measurements": measurements,
        "sourceSha256": sources,
    }
    report_path.write_bytes(
        (
            json.dumps(report, indent=2, sort_keys=False, ensure_ascii=True)
            + "\n"
        ).encode("utf-8")
    )
    failures = [name for name, passed in checks.items() if not passed]
    for name, passed in checks.items():
        print(f"check_{name}={str(passed).lower()}")
    for name, value in measurements.items():
        print(f"measurement_{name}={value}")
    print(f"measurement_report={report_path.as_posix()}")
    print(f"check_count={len(checks)}")
    print(f"failed_check_count={len(failures)}")
    if failures:
        print(f"failed_checks={','.join(failures)}")
        return 1
    print("provenance_pdf=OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
