#!/usr/bin/env python3
"""Tests for the Revision gate Revision/verify_revision.sh and its twin Revision/verify_revision.ps1.

Run from the repository root:
    python -m unittest Revision/tests/test_revision_gate.py -v

Static checks (always, a few seconds):
  * both twins embed the same step table and the same audit program, byte for byte, and end with the same
    final lines (revision_verification=OK / =FAILED / =NOT-RUN);
  * the header comment of each twin lists exactly the steps of the table, in order, with their expected wall
    times and the "long" (skipped by --fast) and "always" marks;
  * the table is well formed: unique step names, positive expected times, the long steps are those
    documented as longer than 5 minutes (or needing such a step), every other step at most 5 minutes;
  * every step's command names existing files (the program and every repository path it reads) and every
    listed output and report exists; the steps that run a built Rust program come after its build step;
  * every Revision WolframScript (.wls, outside textbook/ and workflows/) and every Revision Python checker
    (outside textbook/, workflows/ and tests/) is run by some step; the library modules that are not run
    directly are listed below with the step script that imports them;
  * --dry-run of the bash twin (and of the PowerShell twin when pwsh is available) runs nothing and prints
    the same plan; an unknown step name is rejected with exit code 2.
With REVISION_GATE_FULL=1 the gate itself runs with --fast (about an hour on the development machine;
REVISION_GATE_TWIN=pwsh runs the PowerShell twin instead of the bash twin) and must end with
revision_verification=OK.  The gate removes REVISION_GATE_FULL before its own unit-test step, so it never
runs itself recursively.
"""
import os
import re
import shutil
import subprocess
import sys
import unittest

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
BASH_TWIN = os.path.join(ROOT, "Revision", "verify_revision.sh")
PWSH_TWIN = os.path.join(ROOT, "Revision", "verify_revision.ps1")
FULL = os.environ.get("REVISION_GATE_FULL") == "1"
LONG_SECONDS = 300

# Python files under Revision/ that are libraries of a step script, not programs run by a step.
LIBRARY_MODULES = {
    "Revision/theory/python/compare_wolfram.py": "Revision/theory/python/check_field_theory.py",
    "Revision/theory/python/emt_vielbein.py": "Revision/theory/python/check_field_theory.py",
    "Revision/theory/python/fields.py": "Revision/theory/python/check_field_theory.py",
    "Revision/theory/python/gammas_io.py": "Revision/theory/python/check_field_theory.py",
    "Revision/theory/python/geometry.py": "Revision/theory/python/check_field_theory.py",
    "Revision/theory/python/grassmann_solution.py": "Revision/theory/python/check_field_theory.py",
    "Revision/theory/python/quantum.py": "Revision/theory/python/check_field_theory.py",
    "Revision/theory/python/superalg.py": "Revision/theory/python/check_field_theory.py",
    "Revision/kohn_sham/reference/ks_fd.py": "Revision/kohn_sham/reference/run_reference.py",
}
# Notebook builders Revision/notebooks/src/<name>.py are run by notebooks-check (build_notebooks.py check).
NOTEBOOK_SOURCES = "Revision/notebooks/src/"
# Steps that are marked long although they are short themselves, with the long step they need.
LONG_BY_DEPENDENCY = {"ks-rust-determinism": "ks-rust-refined"}
OUTPUT_FLAGS = {"--out", "--report", "--output", "--work"}
EXCLUDED_TREES = ("Revision/textbook/", "Revision/workflows/")


def read(path):
    with open(path, encoding="utf-8", newline="") as handle:
        return handle.read()


def block(text, start, end):
    """The lines strictly between the line `start` and the next line `end`."""
    lines = text.split("\n")
    first = lines.index(start)
    last = lines.index(end, first + 1)
    return "\n".join(lines[first + 1:last])


def parse_table(text):
    steps = []
    for line in text.split("\n"):
        fields = line.split("|")
        assert len(fields) == 7, line
        name, seconds, kind, fresh, outputs, reports, command = fields
        steps.append({
            "name": name, "seconds": int(seconds), "kind": kind, "fresh": fresh,
            "outputs": [] if outputs == "-" else outputs.split(","),
            "reports": [] if reports == "-" else reports.split(","),
            "command": command,
        })
    return steps


def revision_files(suffix, excluded=EXCLUDED_TREES):
    found = []
    for directory, subdirectories, files in os.walk(os.path.join(ROOT, "Revision")):
        subdirectories[:] = [d for d in subdirectories if d not in ("target", "__pycache__", ".ipynb_checkpoints")]
        for name in files:
            if name.endswith(suffix):
                path = os.path.relpath(os.path.join(directory, name), ROOT).replace("\\", "/")
                if not path.startswith(excluded):
                    found.append(path)
    return sorted(found)


class StaticGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bash = read(BASH_TWIN)
        cls.pwsh = read(PWSH_TWIN)
        cls.bash_table = block(cls.bash, "cat >\"$steps_file\" <<'REVISION_GATE_STEPS'", "REVISION_GATE_STEPS")
        cls.pwsh_table = block(cls.pwsh, "$stepsTable = @'", "'@")
        cls.bash_audit = block(cls.bash, "cat >\"$audit_script\" <<'REVISION_GATE_AUDIT_PY'",
                               "REVISION_GATE_AUDIT_PY")
        cls.pwsh_audit = block(cls.pwsh, "$auditSource = @'", "'@")
        cls.steps = parse_table(cls.bash_table)
        cls.commands = " ".join(step["command"] for step in cls.steps)

    def test_lf_only(self):
        for text in (self.bash, self.pwsh):
            self.assertNotIn("\r", text)

    def test_twins_share_table_and_audit(self):
        self.assertEqual(self.bash_table, self.pwsh_table)
        self.assertEqual(self.bash_audit, self.pwsh_audit)
        compile(self.bash_audit, "gate_audit.py", "exec")

    def test_final_lines(self):
        for text in (self.bash, self.pwsh):
            self.assertIn("revision_verification=OK", text)
            self.assertIn("revision_verification=FAILED", text)
            self.assertIn("revision_verification=NOT-RUN (dry run: nothing was executed)", text)
            self.assertIn("revision_failed_step=", text)
        self.assertTrue(self.bash.rstrip("\n").endswith("exit 0"))
        self.assertTrue(self.pwsh.rstrip("\n").endswith('Write-Output "revision_verification=OK"'))

    def test_header_lists_every_step_with_its_time(self):
        expected = ["#   %-34s %5d s%s" % (step["name"], step["seconds"],
                                          {"0": "", "1": "  long", "A": "  always"}[step["kind"]])
                    for step in self.steps]
        for text in (self.bash, self.pwsh):
            header = [line for line in text.split("\n") if re.match(r"#   \S+ +\d+ s", line)]
            self.assertEqual(header, expected)

    def test_table_is_well_formed(self):
        names = [step["name"] for step in self.steps]
        self.assertEqual(len(names), len(set(names)))
        for step in self.steps:
            with self.subTest(step=step["name"]):
                self.assertRegex(step["name"], r"^[a-z0-9][a-z0-9-]*$")
                self.assertGreater(step["seconds"], 0)
                self.assertIn(step["kind"], ("0", "1", "A"))
                if step["kind"] == "1":
                    needed = LONG_BY_DEPENDENCY.get(step["name"])
                    if needed:
                        self.assertEqual(self.steps[names.index(needed)]["kind"], "1")
                        self.assertLess(names.index(needed), names.index(step["name"]))
                    else:
                        self.assertGreater(step["seconds"], LONG_SECONDS)
                else:
                    self.assertLessEqual(step["seconds"], LONG_SECONDS)
                if step["fresh"] != "-":
                    self.assertTrue(step["fresh"].startswith("build/revision/"))
        self.assertEqual([step["name"] for step in self.steps if step["kind"] == "A"],
                         ["committed-unchanged", "reports-pass"])
        self.assertEqual(names[-3:], ["committed-unchanged", "reports-pass", "unit-tests"])

    def test_commands_name_existing_files(self):
        for step in self.steps:
            with self.subTest(step=step["name"]):
                tokens = step["command"].split(" ")
                self.assertTrue(tokens[0].startswith("{"), tokens[0])
                programs = [t for t in tokens if t.endswith((".py", ".wls", ".toml", ".md"))]
                if tokens[0] in ("{python}", "{wolframscript}", "{cargo}"):
                    self.assertTrue(programs, step["command"])
                for index, token in enumerate(tokens):
                    if not token.startswith(("Revision/", "scripts/")):
                        continue
                    if index > 0 and tokens[index - 1] in OUTPUT_FLAGS and token.startswith("build/"):
                        continue
                    self.assertTrue(os.path.exists(os.path.join(ROOT, token)), token)
                for path in step["outputs"] + step["reports"]:
                    self.assertTrue(os.path.exists(os.path.join(ROOT, path)), path)
                    self.assertTrue(path.startswith("Revision/"), path)
                for path in step["reports"]:
                    self.assertTrue(path.endswith(".json"), path)

    def test_built_programs_follow_their_build(self):
        names = [step["name"] for step in self.steps]
        for placeholder, build in (("{ks_solver}", "ks-rust-build"), ("{gkd_exe}", "gkd-rust-build")):
            users = [step["name"] for step in self.steps if placeholder in step["command"]]
            self.assertTrue(users)
            for user in users:
                self.assertLess(names.index(build), names.index(user), user)

    def test_every_wolframscript_is_run(self):
        scripts = revision_files(".wls")
        self.assertTrue(scripts)
        for path in scripts:
            with self.subTest(script=path):
                self.assertIn(" " + path, self.commands)

    def test_every_python_checker_is_run(self):
        scripts = revision_files(".py", EXCLUDED_TREES + ("Revision/tests/",))
        self.assertTrue(scripts)
        for path in scripts:
            with self.subTest(script=path):
                if path in LIBRARY_MODULES:
                    importer = read(os.path.join(ROOT, LIBRARY_MODULES[path]))
                    module = os.path.splitext(os.path.basename(path))[0]
                    self.assertRegex(importer, r"(import|from) +%s\b" % re.escape(module))
                    self.assertIn(" " + LIBRARY_MODULES[path], self.commands)
                elif path.startswith(NOTEBOOK_SOURCES):
                    self.assertIn("notebooks Revision/notebooks/tools/build_notebooks.py", self.commands)
                else:
                    self.assertIn(" " + path, self.commands)
        for path in LIBRARY_MODULES:
            self.assertTrue(os.path.exists(os.path.join(ROOT, path)), path)

    def test_documents_and_unit_tests_covered(self):
        documents = sorted(os.path.splitext(name)[0] for name in os.listdir(os.path.join(ROOT, "Revision", "docs"))
                           if name.endswith(".md"))
        self.assertEqual(len(documents), 6)
        for document in documents:
            self.assertIn("scripts/build_provenance_pdf.py Revision/docs/%s.md --developer-layout "
                          "--specifications Revision/pdf-specifications.json" % document, self.commands)
        self.assertIn("unittest Revision/tests test_universes_in_pairs_textbook", self.commands)
        self.assertNotIn("--register", self.commands)


def dry_run(command):
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
                            env={**os.environ, "PYTHONUTF8": "1"}, timeout=600)
    lines = [line for line in result.stdout.splitlines() if not line.startswith("revision_tool_python=")]
    return result.returncode, lines


class DryRunTests(unittest.TestCase):
    def test_bash_and_pwsh_dry_runs(self):
        bash = shutil.which("bash")
        if not bash:
            self.skipTest("bash not found")
        code, lines = dry_run([bash, "Revision/verify_revision.sh", "--dry-run"])
        self.assertEqual(code, 0, "\n".join(lines))
        self.assertEqual(lines[-1], "revision_verification=NOT-RUN (dry run: nothing was executed)")
        steps = [line for line in lines if line.startswith("revision_dry_run_step=")]
        table = parse_table(block(read(BASH_TWIN), "cat >\"$steps_file\" <<'REVISION_GATE_STEPS'",
                                  "REVISION_GATE_STEPS"))
        self.assertEqual(len(steps), len(table))
        code_fast, lines_fast = dry_run([bash, "Revision/verify_revision.sh", "--dry-run", "--fast"])
        self.assertEqual(code_fast, 0)
        skipped = [line for line in lines_fast if line.startswith("revision_skipped_step=")]
        self.assertEqual(len(skipped), sum(step["kind"] == "1" for step in table))
        code_bad, lines_bad = dry_run([bash, "Revision/verify_revision.sh", "--dry-run", "--steps", "no-such-step"])
        self.assertEqual(code_bad, 2)
        self.assertIn("revision_unknown_steps=no-such-step", lines_bad)
        self.assertEqual(lines_bad[-1], "revision_verification=FAILED")
        pwsh = shutil.which("pwsh")
        if pwsh:
            for options, expected in (([], lines), (["--fast"], lines_fast)):
                code_ps, lines_ps = dry_run([pwsh, "-NoProfile", "-File", "Revision/verify_revision.ps1",
                                             "--dry-run"] + options)
                self.assertEqual(code_ps, 0)
                self.assertEqual(lines_ps, expected)


@unittest.skipUnless(FULL, "set REVISION_GATE_FULL=1 to run the gate with --fast (about an hour)")
class FullGateTest(unittest.TestCase):
    def test_gate_fast(self):
        if os.environ.get("REVISION_GATE_TWIN") == "pwsh":
            command = [shutil.which("pwsh") or "pwsh", "-NoProfile", "-File", "Revision/verify_revision.ps1", "--fast"]
        else:
            command = [shutil.which("bash") or "bash", "Revision/verify_revision.sh", "--fast"]
        environment = {key: value for key, value in os.environ.items() if key != "REVISION_GATE_FULL"}
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
                                errors="replace", env=environment)
        last = result.stdout.rstrip("\n").split("\n")[-1]
        self.assertEqual(last, "revision_verification=OK", result.stdout[-4000:])
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
