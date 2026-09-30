#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Written for this repository on 2026-09-30.
"""Run a report producer with its JSON report written to another path.

Usage (from the repository root):

    python scripts/run_with_report_path.py REPORT_PATH SCRIPT [ARG ...]

SCRIPT is one of the Stage 1 producers that write their report to the fixed
path held in the module constant REPORT_PATH (a pathlib.Path) and have no
--output option:

    scripts/check_dirac16complex_geometry.py   (main(argv) takes ARG ...)
    scripts/demo_grassmann_lagrangians.py      (main() takes no arguments)

The public-clone mode of scripts/verify_stage1_arbitrary_field.{sh,ps1} uses
this to write their reports into build/stage1/ instead of over the committed
reports.  An --output option is deliberately NOT added to the two scripts:
their own sha256 is recorded in the committed reports (sourceSha256) and
quoted in provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md, so any edit of them
would change the committed evidence.

SCRIPT is imported under its own module name (not as __main__, so its
"if __name__ == '__main__'" block does not run), REPORT_PATH is replaced by
the absolute REPORT_PATH given here, and SCRIPT's main() is called; nothing
else is changed, so the code that computes the report is exactly the
committed code.  The exit status is main()'s return value.  Before main() is
called an existing file at REPORT_PATH is removed, and afterwards the file
must exist; otherwise the exit status is 2 (also for usage errors).
Standard library only.
"""

from __future__ import annotations

import importlib.util
import inspect
import sys
from pathlib import Path


def fail(message: str) -> int:
    print("run_with_report_path_error=%s" % message)
    return 2


def main(argv=None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if len(arguments) < 2 or arguments[0] in ("-h", "--help"):
        print("usage: python scripts/run_with_report_path.py REPORT_PATH SCRIPT [ARG ...]")
        return 0 if arguments[:1] in (["-h"], ["--help"]) else 2
    report_path = Path(arguments[0]).resolve()
    script = Path(arguments[1]).resolve()
    rest = arguments[2:]
    if not script.is_file() or script.suffix != ".py":
        return fail("%s is not a Python file" % arguments[1])

    spec = importlib.util.spec_from_file_location(script.stem, script)
    if spec is None or spec.loader is None:
        return fail("cannot import %s" % script)
    module = importlib.util.module_from_spec(spec)
    sys.modules[script.stem] = module
    spec.loader.exec_module(module)

    original = getattr(module, "REPORT_PATH", None)
    if not isinstance(original, Path):
        return fail("%s has no pathlib.Path REPORT_PATH" % script.name)
    entry = getattr(module, "main", None)
    if not callable(entry):
        return fail("%s has no main()" % script.name)
    takes_arguments = bool(inspect.signature(entry).parameters)
    if rest and not takes_arguments:
        return fail("%s main() takes no arguments, got %s" % (script.name, " ".join(rest)))

    if report_path == original.resolve():
        return fail("REPORT_PATH is already %s" % report_path)
    if report_path.exists():
        report_path.unlink()
    module.REPORT_PATH = report_path
    sys.argv = [str(script)] + rest
    print("report_path_redirect=%s -> %s" % (original.as_posix(), report_path.as_posix()),
          flush=True)
    code = entry(rest) if takes_arguments else entry()
    if not report_path.is_file():
        return fail("%s did not write %s" % (script.name, report_path))
    return code


if __name__ == "__main__":
    sys.exit(main())
