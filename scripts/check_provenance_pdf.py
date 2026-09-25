#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Origin: scripts/check_provenance_pdf.py of https://github.com/once-ere/dirac
# (GPL-3.0-or-later), copied into this repository on 2026-09-25 and modified.
#
# Changes relative to the origin:
#   * The hard-coded dirac-main SPECIFICATIONS are replaced by an EMPTY
#     built-in registry plus the JSON side file
#     provenance/pdf-specifications.json, loaded at run time, of the form
#         {"<edition>": {"path": "<repository-relative .pdf>",
#                        "pages": <int>, "sha256": "<64 hex>"}, ...}
#     so later stages register editions (normally with
#     scripts/build_provenance_pdf.py --register) without editing Python.
#     Entries are validated strictly (edition names, keys, types, paths).
#   * --specifications and --repository-root options (defaults: the side file
#     above and the repository containing this script); a registered path is
#     resolved against the repository root, an explicit PDF argument against
#     the current directory, as before.
#   * An unregistered edition is a usage error (exit 2) naming the registry.
#   * Unchanged: --edition (required) and --repeat semantics, the checks
#     (header, endMarker, pageCount, mediaBox 612x792, canonicalHash,
#     repeatByteIdentity) of check_dissertation_pdf.verify_pdf, the output
#     lines and the exit status 1 on any failed check.
"""Check deterministic provenance PDFs against the registered editions."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath

try:
    from scripts import check_dissertation_pdf
except ModuleNotFoundError:
    import check_dissertation_pdf


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SPECIFICATIONS_PATH = (
    REPOSITORY_ROOT / "provenance" / "pdf-specifications.json"
)
# Built-in registry.  Intentionally empty: every edition of this repository
# lives in the JSON side file.
SPECIFICATIONS: dict[str, dict[str, object]] = {}
EDITION_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
SHA256_PATTERN = re.compile(r"[0-9a-f]{64}")
SPECIFICATION_KEYS = ("path", "pages", "sha256")
LETTER_WIDTH = 612.0
LETTER_HEIGHT = 792.0


class SpecificationError(ValueError):
    """The registry file or one of its entries is malformed."""


def validate_specification(edition: str, raw: object) -> dict[str, object]:
    if not isinstance(edition, str) or not EDITION_PATTERN.fullmatch(edition):
        raise SpecificationError(
            f"edition name {edition!r} must match {EDITION_PATTERN.pattern}"
        )
    if not isinstance(raw, dict):
        raise SpecificationError(f"edition {edition}: entry must be an object")
    if sorted(raw) != sorted(SPECIFICATION_KEYS):
        raise SpecificationError(
            f"edition {edition}: keys must be exactly "
            f"{list(SPECIFICATION_KEYS)}, found {sorted(raw)}"
        )
    path = raw["path"]
    if (
        not isinstance(path, str)
        or not path.endswith(".pdf")
        or "\\" in path
        or PurePosixPath(path).is_absolute()
        or ":" in path
        or ".." in PurePosixPath(path).parts
    ):
        raise SpecificationError(
            f"edition {edition}: path {path!r} must be a relative POSIX "
            "path to a .pdf inside the repository"
        )
    pages = raw["pages"]
    if isinstance(pages, bool) or not isinstance(pages, int) or pages < 1:
        raise SpecificationError(
            f"edition {edition}: pages must be a positive integer"
        )
    sha256 = raw["sha256"]
    if not isinstance(sha256, str) or not SHA256_PATTERN.fullmatch(sha256):
        raise SpecificationError(
            f"edition {edition}: sha256 must be 64 lowercase hex digits"
        )
    return {"path": path, "pages": pages, "sha256": sha256}


def read_registry_file(path: Path) -> dict[str, dict[str, object]]:
    """Return the validated entries of the side file ({} if it is absent)."""
    if not path.exists():
        return {}

    def reject_duplicates(pairs: list[tuple[str, object]]) -> dict:
        keys = [key for key, _ in pairs]
        duplicates = sorted({key for key in keys if keys.count(key) > 1})
        if duplicates:
            raise SpecificationError(f"{path}: duplicate keys {duplicates}")
        return dict(pairs)

    try:
        data = json.loads(
            path.read_bytes().decode("utf-8"),
            object_pairs_hook=reject_duplicates,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise SpecificationError(f"{path}: not valid UTF-8 JSON: {error}")
    if not isinstance(data, dict):
        raise SpecificationError(f"{path}: top level must be an object")
    return {
        edition: validate_specification(edition, raw)
        for edition, raw in data.items()
    }


def load_specifications(
    path: Path = DEFAULT_SPECIFICATIONS_PATH,
) -> dict[str, dict[str, object]]:
    """Merge the built-in registry with the JSON side file."""
    registry = {
        edition: validate_specification(edition, raw)
        for edition, raw in SPECIFICATIONS.items()
    }
    for edition, specification in read_registry_file(path).items():
        if edition in registry:
            raise SpecificationError(
                f"edition {edition} is both built in and in {path}"
            )
        registry[edition] = specification
    return registry


def dump_specifications(registry: dict[str, dict[str, object]]) -> str:
    """Deterministic JSON text: editions sorted, keys path, pages, sha256."""
    ordered = {
        edition: {
            key: validate_specification(edition, registry[edition])[key]
            for key in SPECIFICATION_KEYS
        }
        for edition in sorted(registry)
    }
    text = json.dumps(ordered, indent=2, sort_keys=False, ensure_ascii=True)
    return text + "\n"


def register_edition(
    path: Path, edition: str, pdf_path: str, pages: int, sha256: str
) -> dict[str, object]:
    """Add or replace one edition in the side file and return its entry."""
    specification = validate_specification(
        edition, {"path": pdf_path, "pages": pages, "sha256": sha256}
    )
    if edition in SPECIFICATIONS:
        raise SpecificationError(f"edition {edition} is built in")
    registry = read_registry_file(path)
    registry[edition] = specification
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(dump_specifications(registry).encode("utf-8"))
    if read_registry_file(path).get(edition) != specification:
        raise SpecificationError(f"{path}: re-read of {edition} differs")
    return specification


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edition", required=True)
    parser.add_argument("pdf", nargs="?", type=Path)
    parser.add_argument("--repeat", type=Path)
    parser.add_argument(
        "--specifications", type=Path, default=DEFAULT_SPECIFICATIONS_PATH
    )
    parser.add_argument(
        "--repository-root", type=Path, default=REPOSITORY_ROOT
    )
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    try:
        registry = load_specifications(arguments.specifications)
    except SpecificationError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    specification = registry.get(arguments.edition)
    if specification is None:
        registered = ", ".join(sorted(registry)) or "none"
        print(
            f"ERROR: edition {arguments.edition!r} is not registered in "
            f"{arguments.specifications} (registered: {registered}); "
            "register it with scripts/build_provenance_pdf.py --register",
            file=sys.stderr,
        )
        return 2
    if arguments.pdf:
        pdf_path = arguments.pdf.resolve()
    else:
        pdf_path = (
            arguments.repository_root / str(specification["path"])
        ).resolve()
    report = check_dissertation_pdf.verify_pdf(
        pdf_path,
        arguments.repeat.resolve() if arguments.repeat else None,
        int(specification["pages"]),
        LETTER_WIDTH,
        LETTER_HEIGHT,
        str(specification["sha256"]),
    )
    failures = [
        name for name, passed in report["checks"].items() if not passed
    ]
    for name, passed in report["checks"].items():
        print(f"check_{name}={str(passed).lower()}")
    for name, value in report["measurements"].items():
        print(f"measurement_{name}={value}")
    print(f"measurement_edition={arguments.edition}")
    print(f"check_count={len(report['checks'])}")
    print(f"failed_check_count={len(failures)}")
    if failures:
        print(f"failed_checks={','.join(failures)}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
