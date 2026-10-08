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
Failure paths (each twin copied into a temporary folder, a few seconds; nothing of this repository is run
or written):
  * a failing step ends the gate with revision_failed_step, revision_failed_log, revision_gate_seconds and
    the last line revision_verification=FAILED, with the step's exit code;
  * a selected step whose output path already differs from HEAD (in a temporary git repository) stops the
    gate at the precheck with exit code 3 and the reason that names this cause;
  * a Wolfram step whose wolframscript prints 'Failed to open file' and exits with 0 (a fake wolframscript
    first on PATH) fails the gate with revision_wolfram_open_failure and is not retried.
Line endings: every file tracked under Revision/ is stored with LF only (Revision/SPEC.md section 0;
git ls-files --eol shows no i/crlf or i/mixed).
With REVISION_GATE_FULL=1 the gate itself runs with --fast (measured on the development machine on
2026-10-08: about 20 min; REVISION_GATE_TWIN=pwsh runs the PowerShell twin instead of the bash twin)
and must end with revision_verification=OK.  The gate removes REVISION_GATE_FULL before its own unit-test
step, so it never runs itself recursively.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
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

    def test_revision_files_are_stored_with_lf(self):
        # Revision/SPEC.md section 0 requires LF line endings for every file under Revision/.  The root
        # .gitattributes ('* -text') stores every file byte for byte, so a CRLF written on Windows would be
        # committed as CRLF; this test names such a file.
        git = shutil.which("git")
        if not git or not os.path.exists(os.path.join(ROOT, ".git")):
            self.skipTest("git or the repository's .git not found")
        result = subprocess.run([git, "ls-files", "--eol", "--", "Revision"], cwd=ROOT, capture_output=True,
                                text=True, encoding="utf-8", check=True)
        bad = [line.split("\t", 1)[-1] for line in result.stdout.splitlines()
               if line.split()[0] in ("i/crlf", "i/mixed")]
        self.assertEqual(bad, [])

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


def twin_commands():
    """(label, command prefix, twin file name) of every twin that can run here."""
    found = []
    bash = shutil.which("bash")
    if bash:
        found.append(("bash", [bash, "Revision/verify_revision.sh"], "verify_revision.sh"))
    pwsh = shutil.which("pwsh")
    if pwsh:
        found.append(("pwsh", [pwsh, "-NoProfile", "-File", "Revision/verify_revision.ps1"], "verify_revision.ps1"))
    return found


def run_twin_in(root, command, extra_environment=None):
    environment = {key: value for key, value in os.environ.items()
                   if key != "REVISION_GATE_FULL" and not key.startswith("GIT_")}
    environment["PYTHONUTF8"] = "1"
    environment.update(extra_environment or {})
    result = subprocess.run(command, cwd=root, capture_output=True, text=True, encoding="utf-8",
                            errors="replace", env=environment, timeout=600)
    return result.returncode, result.stdout.splitlines()


def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


class FailurePathTests(unittest.TestCase):
    """Each twin runs in a temporary copy that holds only the files the selected step reads."""

    def test_failing_step_ends_with_failed(self):
        twins = twin_commands()
        if not twins:
            self.skipTest("neither bash nor pwsh found")
        for label, command, twin in twins:
            with self.subTest(twin=label), tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as root:
                shutil.copy(os.path.join(ROOT, "Revision", twin), self._revision(root, twin))
                # theory-compare requires comparison_with_wolfram.status == "agree"; this copy says otherwise,
                # and the step has no output path, so the precheck needs no git repository.
                write_text(os.path.join(root, "Revision", "theory", "reports", "python-field-theory.json"),
                           '{"comparison_with_wolfram": {"status": "disagree"}}\n')
                code, lines = run_twin_in(root, command + ["--steps", "theory-compare"])
                text = "\n".join(lines)
                self.assertEqual(code, 1, text)
                self.assertIn("revision_failed_step=theory-compare", lines, text)
                self.assertIn("revision_failed_log=build/logs/revision/theory-compare-%s.log" % label, lines, text)
                self.assertTrue(any(line.startswith("revision_step_seconds=theory-compare ") for line in lines), text)
                self.assertTrue(any(line.startswith("revision_gate_seconds=") for line in lines), text)
                self.assertEqual(lines[-1], "revision_verification=FAILED", text)

    def test_precheck_names_a_preexisting_change(self):
        git = shutil.which("git")
        twins = twin_commands()
        if not git or not twins:
            self.skipTest("git, or both bash and pwsh, not found")
        output = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
        for label, command, twin in twins:
            with self.subTest(twin=label), tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as root:
                shutil.copy(os.path.join(ROOT, "Revision", twin), self._revision(root, twin))
                write_text(os.path.join(root, ".gitignore"), "build/\n")
                write_text(os.path.join(root, output), '{"checks": []}\n')
                identity = ["-c", "user.name=revision-gate-test", "-c", "user.email=revision-gate-test@example.invalid",
                            "-c", "core.autocrlf=false", "-c", "commit.gpgsign=false"]
                for arguments in (["init", "-q"], ["add", "-A"], ["commit", "-q", "-m", "committed record"]):
                    subprocess.run([git] + identity + arguments, cwd=root, check=True, capture_output=True)
                write_text(os.path.join(root, output), '{"checks": [] }\n')
                code, lines = run_twin_in(root, command + ["--steps", "lead-charge-conjugation"])
                text = "\n".join(lines)
                self.assertEqual(code, 3, text)
                self.assertIn("revision_preexisting_change=" + output, lines, text)
                self.assertIn("revision_failed_step=precheck", lines, text)
                self.assertIn("revision_failure_reason=an output path of a selected step already differs from HEAD "
                              "(see the revision_preexisting_change lines)", lines, text)
                self.assertFalse(any(line.startswith("revision_step=") for line in lines), text)
                self.assertEqual(lines[-1], "revision_verification=FAILED", text)

    def test_wolfram_open_failure_fails(self):
        twins = twin_commands()
        if not twins:
            self.skipTest("neither bash nor pwsh found")
        names = ("wolframscript", "wolframscript.exe", "wolframscript.cmd", "wolframscript.bat")
        for label, command, twin in twins:
            with self.subTest(twin=label), tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as root:
                shutil.copy(os.path.join(ROOT, "Revision", twin), self._revision(root, twin))
                # A fake wolframscript (a shell script for bash and for Linux/macOS, a .cmd for PowerShell on
                # Windows) behaves like the real one when the path of its script has 260 or more characters
                # on Windows: it prints 'Failed to open file at path: ...' and exits with 0.  The real
                # wolframscript is taken off PATH.  gkd-notebook-extract has no output path, so the precheck
                # needs no git repository.
                fake = os.path.join(root, "fakebin")
                write_text(os.path.join(fake, "wolframscript"),
                           '#!/bin/sh\necho "Failed to open file at path: $2"\nexit 0\n')
                os.chmod(os.path.join(fake, "wolframscript"), 0o755)
                write_text(os.path.join(fake, "wolframscript.cmd"),
                           "@echo Failed to open file at path: %2\n@exit /b 0\n")
                path = os.pathsep.join([fake] + [
                    entry for entry in os.environ.get("PATH", "").split(os.pathsep)
                    if entry and not any(os.path.isfile(os.path.join(entry, name)) for name in names)])
                code, lines = run_twin_in(root, command + ["--steps", "gkd-notebook-extract"], {"PATH": path})
                text = "\n".join(lines)
                self.assertEqual(code, 1, text)
                self.assertIn("revision_wolfram_open_failure=gkd-notebook-extract wolframscript could not open its "
                              "script file", lines, text)
                self.assertIn("revision_failed_step=gkd-notebook-extract", lines, text)
                self.assertFalse(any(line.startswith("revision_retry=") for line in lines), text)
                self.assertEqual(lines[-1], "revision_verification=FAILED", text)

    @staticmethod
    def _revision(root, twin):
        os.makedirs(os.path.join(root, "Revision"), exist_ok=True)
        return os.path.join(root, "Revision", twin)


@unittest.skipUnless(FULL, "set REVISION_GATE_FULL=1 to run the gate with --fast (about 20 min)")
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
