#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Written for this repository on 2026-09-30.
"""Audit a public-clone regeneration of the Stage 1 files against the committed ones.

The folder dirac-main/ (the separately published https://github.com/once-ere/dirac,
read here only as a reference input) is git-ignored, so a fresh clone of this
repository does not contain it.  Without it the Stage 1 algebra verifiers still run
every check, but record their cross-checks against dirac-main's three exact fixtures
as "not-run".  The public-clone mode of scripts/verify_stage1_arbitrary_field.{sh,ps1}
therefore regenerates the Stage 1 files into build/stage1/ (leaving the committed
ones untouched) and runs this audit, which compares, in this order,

    algebra-fixture.json, wolfram-algebra-report.json, wolfram-geometry-report.json,
    grassmann-demo-report.json, python-geometry-report.json,
    python-algebra-report.json, stage1-summary.json

of the regenerated directory with the committed directory.  A file passes if it is
byte-identical, or if it is value-for-value equal except for these differences:

  not-run      a value that is true in the committed file and the string "not-run"
               in the regenerated one, whose name refers to dirac-main: its object
               key, prefixed by the "measurement" string of the enclosing object when
               there is one, matches /dirac-?main/ (case-insensitive).  Allowed only
               while at least one of the three dirac-main reference files is absent;
  reference    an entry "dirac-main/..." of an object named referenceFilesPresent
               that is true in the committed file and false in the regenerated one,
               while that file is absent;
  source-hash  an entry "dirac-main/..." of an object named sourceSha256 that is in
               the committed file and missing from the regenerated one (the other
               entries keep their order), while that file is absent;
  hash         a sha256 (64 lower-case hex digits) that differs because it is the hash
               of a Stage 1 file that differs for these reasons: the committed value
               is the sha256 of the committed file F, the regenerated value is the
               sha256 of the regenerated F, and F was audited earlier in this run and
               passed with allowed differences;
  relocated    a string (object key or value) that is exactly
               <regenerated directory>/<one of the seven file names>, relative to the
               repository root, where the committed file has
               <committed directory>/<the same name>: the regenerated reports record
               the path they read their inputs from.

"Value-for-value" is strict: objects must have the same keys in the same order,
arrays the same length, numbers the same literal text (1 and 1.0 differ), and
true/false/null/strings must be equal with the same JSON type.  A file that differs
in its bytes although none of the differences above occurs (a formatting-only
difference) fails.  Every other difference fails.

Prints stage1_audit_file=<name> identical|allowed-differences|FAILED lines, one
stage1_audit_allowed=... line per allowed difference, one stage1_audit_forbidden=...
line per forbidden difference, stage1_audit_not_run=<file>:<path> for every
dirac-main cross-check that did not run, and ends with
stage1_public_clone_audit=OK|FAILED; exits 0 (OK), 1 (FAILED) or 2 (usage error).
Standard library only.

Usage (from any directory):
    python scripts/verify_stage1_public_clone_audit.py [--committed DIR]
        [--regenerated DIR] [--repository-root DIR]
with the defaults <root>/artifacts/dirac16complex/arbitrary-field, <root>/build/stage1
and <root> = the parent of this script's directory.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_COMMITTED = Path("artifacts") / "dirac16complex" / "arbitrary-field"
DEFAULT_REGENERATED = Path("build") / "stage1"
# Audit order: a file's hash may appear in the files after it, never before it.
FILES = (
    "algebra-fixture.json",
    "wolfram-algebra-report.json",
    "wolfram-geometry-report.json",
    "grassmann-demo-report.json",
    "python-geometry-report.json",
    "python-algebra-report.json",
    "stage1-summary.json",
)
DIRAC_MAIN_FILES = (
    "dirac-main/artifacts/exact/cl44-seed.json",
    "dirac-main/artifacts/exact/split-octonion.json",
    "dirac-main/artifacts/exact/triality44.json",
)
DIRAC_MAIN_NAME = re.compile(r"dirac-?main", re.IGNORECASE)
SHA256_TEXT = re.compile(r"[0-9a-f]{64}\Z")
NOT_RUN = "not-run"


class Number:
    """A JSON number kept as its literal text, so that 1, 1.0 and 1e0 all differ."""

    __slots__ = ("text",)

    def __init__(self, text):
        self.text = text

    def __eq__(self, other):
        return isinstance(other, Number) and other.text == self.text

    def __hash__(self):
        return hash(self.text)

    def __repr__(self):
        return self.text


class Obj:
    """A JSON object kept as its ordered list of (key, value) pairs."""

    __slots__ = ("pairs",)

    def __init__(self, pairs):
        self.pairs = list(pairs)

    def keys(self):
        return [key for key, _ in self.pairs]

    def get(self, key, default=None):
        for name, value in self.pairs:
            if name == key:
                return value
        return default


def parse(data: bytes):
    return json.loads(data.decode("utf-8"), object_pairs_hook=Obj, parse_int=Number,
                      parse_float=Number, parse_constant=Number)


def show(value) -> str:
    """Short printable form of a parsed value."""
    if isinstance(value, Obj):
        return "{object with %d keys}" % len(value.pairs)
    if isinstance(value, list):
        return "[array of %d]" % len(value)
    if isinstance(value, Number):
        return value.text
    return json.dumps(value, ensure_ascii=True)


def path_text(path) -> str:
    parts = []
    for token in path:
        parts.append("[%d]" % token if isinstance(token, int) else "/" + token)
    return "".join(parts) or "/"


def leaf_equal(a, b) -> bool:
    return type(a) is type(b) and a == b


def relative_text(path: Path, root: Path) -> str:
    try:
        return os.path.relpath(os.path.abspath(path), os.path.abspath(root)).replace("\\", "/")
    except ValueError:  # another drive on Windows
        return os.path.abspath(path).replace("\\", "/")


class Audit:
    def __init__(self, committed: Path, regenerated: Path, root: Path):
        self.committed = committed
        self.regenerated = regenerated
        self.root = root
        committed_prefix = relative_text(committed, root)
        regenerated_prefix = relative_text(regenerated, root)
        self.relocations = {"%s/%s" % (regenerated_prefix, name): "%s/%s" % (committed_prefix, name)
                            for name in FILES}
        self.dirac_main_incomplete = not all((root / name).is_file() for name in DIRAC_MAIN_FILES)
        self.changed = {}  # file name -> (committed sha256, regenerated sha256), passed with differences
        self.lines = []
        self.failed = False
        self.file = None
        self.file_allowed = []
        self.file_forbidden = []

    # -- recording -----------------------------------------------------------------------------
    def allow(self, path, kind, committed, regenerated):
        self.file_allowed.append((path, kind))
        self.lines.append("stage1_audit_allowed=%s %s %s: %s -> %s" % (
            self.file, path_text(path), kind, committed, regenerated))
        if kind == "not-run":
            self.lines.append("stage1_audit_not_run=%s:%s" % (self.file, path_text(path)))

    def forbid(self, path, reason):
        self.file_forbidden.append((path, reason))
        self.lines.append("stage1_audit_forbidden=%s %s %s" % (self.file, path_text(path), reason))

    # -- rules -----------------------------------------------------------------------------------
    def absent(self, key: str) -> bool:
        return key.startswith("dirac-main/") and not (self.root / key).exists()

    def hash_explained(self, committed, regenerated):
        if not (isinstance(committed, str) and isinstance(regenerated, str)):
            return None
        if not (SHA256_TEXT.match(committed) and SHA256_TEXT.match(regenerated)):
            return None
        for name, (committed_sha, regenerated_sha) in self.changed.items():
            if committed == committed_sha and regenerated == regenerated_sha:
                return name
        return None

    def leaf_rule(self, committed, regenerated, path, parent):
        key = path[-1] if path and isinstance(path[-1], str) else None
        container = path[-2] if len(path) >= 2 and isinstance(path[-2], str) else None
        if key is not None and committed is True and leaf_equal(regenerated, NOT_RUN):
            name = key
            measurement = parent.get("measurement") if isinstance(parent, Obj) else None
            if isinstance(measurement, str):
                name = measurement + " " + key
            if DIRAC_MAIN_NAME.search(name) and self.dirac_main_incomplete:
                return "not-run"
        if (container == "referenceFilesPresent" and key is not None and self.absent(key)
                and committed is True and regenerated is False):
            return "reference"
        source = self.hash_explained(committed, regenerated)
        if source is not None:
            return "hash of %s" % source
        return None

    # -- comparison ------------------------------------------------------------------------------
    def relocate(self, value, path=()):
        if isinstance(value, Obj):
            pairs = []
            for key, item in value.pairs:
                if key in self.relocations:
                    self.allow(path + (key,), "relocated", json.dumps(self.relocations[key]),
                               json.dumps(key))
                    key = self.relocations[key]
                pairs.append((key, self.relocate(item, path + (key,))))
            return Obj(pairs)
        if isinstance(value, list):
            return [self.relocate(item, path + (index,)) for index, item in enumerate(value)]
        if isinstance(value, str) and value in self.relocations:
            self.allow(path, "relocated", json.dumps(self.relocations[value]), json.dumps(value))
            return self.relocations[value]
        return value

    def compare(self, committed, regenerated, path=(), parent=None):
        if isinstance(committed, Obj) and isinstance(regenerated, Obj):
            self.compare_objects(committed, regenerated, path)
            return
        if isinstance(committed, list) and isinstance(regenerated, list):
            if len(committed) != len(regenerated):
                self.forbid(path, "array length %d -> %d" % (len(committed), len(regenerated)))
                return
            for index, (a, b) in enumerate(zip(committed, regenerated)):
                self.compare(a, b, path + (index,), None)
            return
        if leaf_equal(committed, regenerated):
            return
        kind = self.leaf_rule(committed, regenerated, path, parent)
        if kind is None:
            self.forbid(path, "%s -> %s" % (show(committed), show(regenerated)))
        else:
            self.allow(path, kind, show(committed), show(regenerated))

    def compare_objects(self, committed: Obj, regenerated: Obj, path):
        regenerated_keys = regenerated.keys()
        removed = []
        if path and path[-1] == "sourceSha256":
            present = set(regenerated_keys)
            removed = [key for key in committed.keys() if key not in present and self.absent(key)]
        kept = [(key, value) for key, value in committed.pairs if key not in removed]
        kept_keys = [key for key, _ in kept]
        if kept_keys != regenerated_keys:
            missing = [key for key in kept_keys if key not in regenerated_keys]
            extra = [key for key in regenerated_keys if key not in kept_keys]
            if missing or extra:
                reason = "keys differ: missing %s, extra %s" % (
                    json.dumps(missing, ensure_ascii=True), json.dumps(extra, ensure_ascii=True))
            else:
                reason = "same keys in a different order or multiplicity"
            self.forbid(path, reason)
            return
        for key in removed:
            self.allow(path + (key,), "source-hash", show(committed.get(key)), "(absent)")
        for (key, a), (_, b) in zip(kept, regenerated.pairs):
            self.compare(a, b, path + (key,), committed)

    def audit_file(self, name: str) -> None:
        self.file, self.file_allowed, self.file_forbidden = name, [], []
        committed_path, regenerated_path = self.committed / name, self.regenerated / name
        for label, file_path in (("committed", committed_path), ("regenerated", regenerated_path)):
            if not file_path.is_file():
                self.forbid((), "%s file %s is missing" % (label, relative_text(file_path, self.root)))
        if self.file_forbidden:
            self.finish_file(None, None)
            return
        committed_bytes, regenerated_bytes = committed_path.read_bytes(), regenerated_path.read_bytes()
        committed_sha = hashlib.sha256(committed_bytes).hexdigest()
        regenerated_sha = hashlib.sha256(regenerated_bytes).hexdigest()
        if committed_bytes == regenerated_bytes:
            self.finish_file(committed_sha, regenerated_sha)
            return
        try:
            committed_tree, regenerated_tree = parse(committed_bytes), parse(regenerated_bytes)
        except (UnicodeDecodeError, ValueError) as error:
            self.forbid((), "the files differ and one is not UTF-8 JSON: %s" % error)
            self.finish_file(committed_sha, regenerated_sha)
            return
        regenerated_tree = self.relocate(regenerated_tree)
        self.compare(committed_tree, regenerated_tree)
        if not self.file_allowed and not self.file_forbidden:
            self.forbid((), "the bytes differ but no value does (formatting-only difference)")
        self.finish_file(committed_sha, regenerated_sha)

    def finish_file(self, committed_sha, regenerated_sha):
        name = self.file
        if self.file_forbidden:
            self.failed = True
            self.lines.append("stage1_audit_file=%s FAILED (%d forbidden, %d allowed differences)" % (
                name, len(self.file_forbidden), len(self.file_allowed)))
        elif committed_sha == regenerated_sha:
            self.lines.append("stage1_audit_file=%s identical sha256=%s" % (name, committed_sha))
        else:
            self.changed[name] = (committed_sha, regenerated_sha)
            self.lines.append("stage1_audit_file=%s allowed-differences=%d committed_sha256=%s "
                              "regenerated_sha256=%s" % (name, len(self.file_allowed), committed_sha,
                                                         regenerated_sha))

    def run(self):
        self.lines.append("stage1_audit_committed=%s" % relative_text(self.committed, self.root))
        self.lines.append("stage1_audit_regenerated=%s" % relative_text(self.regenerated, self.root))
        self.lines.append("stage1_audit_dirac_main=%s" % ("absent" if self.dirac_main_incomplete
                                                         else "present"))
        for name in FILES:
            self.audit_file(name)
        self.lines.append("stage1_public_clone_audit=%s" % ("FAILED" if self.failed else "OK"))
        return not self.failed


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repository-root", default=str(REPOSITORY_ROOT))
    parser.add_argument("--committed", default=None,
                        help="default: <root>/artifacts/dirac16complex/arbitrary-field")
    parser.add_argument("--regenerated", default=None, help="default: <root>/build/stage1")
    arguments = parser.parse_args(argv)
    root = Path(arguments.repository_root).resolve()
    committed = Path(arguments.committed).resolve() if arguments.committed else root / DEFAULT_COMMITTED
    regenerated = (Path(arguments.regenerated).resolve() if arguments.regenerated
                   else root / DEFAULT_REGENERATED)
    for label, directory in (("repository root", root), ("committed", committed),
                             ("regenerated", regenerated)):
        if not directory.is_dir():
            print("stage1_audit_error=%s directory %s does not exist" % (label, directory))
            print("stage1_public_clone_audit=FAILED")
            return 2
    if committed == regenerated:
        print("stage1_audit_error=the committed and the regenerated directory are the same")
        print("stage1_public_clone_audit=FAILED")
        return 2
    audit = Audit(committed, regenerated, root)
    ok = audit.run()
    for line in audit.lines:
        print(line)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
