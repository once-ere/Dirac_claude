"""Unit tests of the Stage-5 gate tools (standard library only).

  * scripts/verify_stage5_pair_creation_audit.py: the same / rust-run /
    rust-outputs / report / reference-quick / reference-reproduce /
    tree-same / snapshot / unchanged / fresh / wolfram-log subcommands, each
    with a negative control (rust-run with stand-in subcommand scripts run by
    this Python, including pairs, --refined and --quick; reference-reproduce
    with a stand-in reference runner in a temporary directory).
  * scripts/verify_stage5_pair_creation.{ps1,sh}: both twins list the same
    steps in the same order with the same expected wall times (their
    --dry-run / -DryRun output), launch the same Rust jobs (concurrent by
    default, --sequential-rust / -SequentialRust), select steps with
    --steps / -Steps, end with the same final lines, are LF-only, check
    Wolfram logs for "Failed to open file", and refuse to start while another
    gate holds build/stage5.lock (run on a copy of the gate in a temporary
    directory, never on this repository's build/), releasing their own lock
    when a step fails.

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_stage5_gate.py" -v
Nothing here runs the gate on the repository, a solver, a Rust run, the
reference runner or a Wolfram kernel.
"""

import copy
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIT_PATH = os.path.join(REPO, "scripts", "verify_stage5_pair_creation_audit.py")
GATE_PS1 = os.path.join(REPO, "scripts", "verify_stage5_pair_creation.ps1")
GATE_SH = os.path.join(REPO, "scripts", "verify_stage5_pair_creation.sh")
STEP_COUNT = 30


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


audit = load_module("verify_stage5_pair_creation_audit", AUDIT_PATH)


def write_json(path, document):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(document, indent=2) + "\n")


def write_text(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def run_audit(*arguments):
    completed = subprocess.run([sys.executable, AUDIT_PATH, *arguments], capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=120)
    return completed.returncode, completed.stdout + completed.stderr


FAKE_SUBCOMMAND = (
    "import os, sys, time\n"
    "args = sys.argv[1:]\n"
    "out = args[args.index('--output') + 1]\n"
    "name = os.path.basename(sys.argv[0])\n"
    "os.makedirs(os.path.join(out, name), exist_ok=True)\n"
    "time.sleep(float(os.environ.get('FAKE_SLEEP_' + name, '0.2')))\n"
    "mode = 'refined' if '--refined' in args else ('quick' if '--quick' in args else 'canonical')\n"
    "with open(os.path.join(out, name, 'mode.txt'), 'w') as handle:\n"
    "    handle.write(mode)\n"
    "code = int(os.environ.get('FAKE_EXIT_' + name, '0'))\n"
    "print('SUCCESS' if code == 0 else 'FAILURE')\n"
    "sys.exit(code)\n")

# A stand-in for scripts/ks_reference_pairs.py: writes the requested run
# directories and a summary from the files of ./template (as the committed
# tree), optionally changing one byte (FAKE_REFERENCE_DRIFT).
FAKE_REFERENCE_RUNNER = (
    "import json, os, shutil, sys\n"
    "args = sys.argv[1:]\n"
    "labels = args[args.index('--runs') + 1].split(',')\n"
    "out = args[args.index('--output') + 1]\n"
    "summary = json.load(open(os.path.join('template', 'reference-pairs-summary.json'), encoding='utf-8'))\n"
    "for label in labels:\n"
    "    shutil.copytree(os.path.join('template', label), os.path.join(out, label), dirs_exist_ok=True)\n"
    "if os.environ.get('FAKE_REFERENCE_DRIFT'):\n"
    "    with open(os.path.join(out, labels[0], 'spectrum.csv'), 'a') as handle:\n"
    "        handle.write('drift\\n')\n"
    "summary['runs'] = [r for r in summary['runs'] if r['label'] in labels]\n"
    "with open(os.path.join(out, 'reference-pairs-summary.json'), 'w', encoding='utf-8') as handle:\n"
    "    json.dump(summary, handle)\n"
    "print('wrote', len(labels))\n")


class AuditTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.mkdtemp(prefix="d16c_s5_audit_")
        self.cwd = os.getcwd()
        os.chdir(self.temp)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.temp, ignore_errors=True)

    def test_same_bytes_values_and_negative_controls(self):
        write_json("a/x.json", {"v": 1.0, "s": "t"})
        write_json("b/x.json", {"v": 1.0, "s": "t"})
        self.assertEqual(run_audit("same", "--pair", "a/x.json", "b/x.json")[0], 0)
        write_json("b/x.json", {"v": 1.0 + 1e-12, "s": "t"})
        self.assertEqual(run_audit("same", "--pair", "a/x.json", "b/x.json")[0], 1)
        code, text = run_audit("same", "--rtol", "1e-9", "--atol", "1e-12", "--pair", "a/x.json", "b/x.json")
        self.assertEqual(code, 0, text)
        self.assertIn("value by value", text)
        write_json("b/x.json", {"v": 1.0 + 1e-6, "s": "t"})
        self.assertEqual(run_audit("same", "--rtol", "1e-9", "--pair", "a/x.json", "b/x.json")[0], 1)
        write_json("b/x.json", {"v": 1.0, "s": "u"})
        self.assertEqual(run_audit("same", "--rtol", "1e-9", "--pair", "a/x.json", "b/x.json")[0], 1)
        self.assertEqual(run_audit("same", "--pair", "a/x.json", "b/missing.json")[0], 1)

    @staticmethod
    def make_pairs_tree(root):
        write_text(os.path.join(root, "pairs", "d16c_m1_L3_N8_lam0_T0", "plusM", "levels.csv"), "eps\n1.0\n")
        write_text(os.path.join(root, "pairs", "pairs-summary.csv"), "label\nx\n")
        write_json(os.path.join(root, "pairs", "summary.json"),
                   {"files": ["d16c_m1_L3_N8_lam0_T0/plusM/levels.csv", "pairs-summary.csv", "summary.json"]})

    def test_rust_outputs_pairs(self):
        self.make_pairs_tree("committed")
        self.make_pairs_tree("run")
        code, text = run_audit("rust-outputs", "--committed", "committed", "--run", "run", "--sub", "pairs")
        self.assertEqual(code, 0, text)
        write_text("run/pairs/d16c_m1_L3_N8_lam0_T0/plusM/levels.csv", "eps\n1.0000001\n")
        code, text = run_audit("rust-outputs", "--committed", "committed", "--run", "run", "--sub", "pairs")
        self.assertEqual(code, 1)
        self.assertIn("pairs: 1 file(s) differ", text)
        self.make_pairs_tree("run")
        write_text("run/pairs/stray.csv", "x\n")
        self.assertEqual(run_audit("rust-outputs", "--committed", "committed", "--run", "run", "--sub", "pairs")[0], 1)
        os.remove("run/pairs/stray.csv")
        write_text("committed/pairs/unlisted.csv", "x\n")
        self.assertEqual(run_audit("rust-outputs", "--committed", "committed", "--run", "run", "--sub", "pairs")[0], 1)
        os.remove("committed/pairs/unlisted.csv")
        shutil.rmtree("run/pairs")
        self.assertEqual(run_audit("rust-outputs", "--committed", "committed", "--run", "run", "--sub", "pairs")[0], 1)

    def test_rust_run_modes_concurrency_and_failures(self):
        # the "binary" is this Python; the subcommand names are small scripts in the
        # working directory, so "<python> pairs [--refined|--quick] --output DIR" runs a stand-in
        for sub in ("pairs", "spectrum", "scf", "excited"):
            write_text(sub, FAKE_SUBCOMMAND)
        jobs = ["--job", "pairs", "run-a", "canonical", "--job", "pairs", "refined", "refined",
                "--job", "spectrum", "ident", "canonical", "--job", "scf", "ident", "quick",
                "--job", "excited", "ident", "quick"]
        code, text = run_audit("rust-run", "--binary", sys.executable, "--log-prefix", "logs/r", *jobs)
        self.assertEqual(code, 0, text)
        self.assertIn("concurrent (5 processes)", text)
        self.assertEqual(text.count("exit=0 last=SUCCESS"), 5)
        for path, mode in ((("refined", "pairs"), "refined"), (("run-a", "pairs"), "canonical"),
                           (("ident", "scf"), "quick"), (("ident", "spectrum"), "canonical")):
            with open(os.path.join(*path, "mode.txt"), encoding="utf-8") as handle:
                self.assertEqual(handle.read(), mode)
        self.assertTrue(os.path.isfile(os.path.join("logs", "r-quick-excited.log")))
        code, text = run_audit("rust-run", "--sequential", "--binary", sys.executable, "--log-prefix", "logs/s", *jobs)
        self.assertEqual(code, 0, text)
        self.assertIn("stage5_rust_run_mode=sequential", text)
        os.environ["FAKE_EXIT_pairs"] = "1"
        os.environ["FAKE_SLEEP_scf"] = "60"
        try:
            started = time.monotonic()
            code, text = run_audit("rust-run", "--binary", sys.executable, "--log-prefix", "logs/f",
                                   "--job", "pairs", "run-a", "canonical", "--job", "scf", "ident", "quick")
            self.assertLess(time.monotonic() - started, 50.0)
            self.assertEqual(code, 1)
            self.assertIn("canonical pairs exited 1 with last line 'FAILURE'", text)
            self.assertIn("quick scf STOPPED", text)
            code, text = run_audit("rust-run", "--sequential", "--binary", sys.executable, "--log-prefix", "logs/g",
                                   "--job", "pairs", "run-a", "canonical", "--job", "excited", "ident", "quick")
            self.assertEqual(code, 1)
            self.assertIn("quick excited NOT STARTED", text)
        finally:
            del os.environ["FAKE_EXIT_pairs"]
            del os.environ["FAKE_SLEEP_scf"]
        write_text("pairs", "print('SUCCESS')\nprint('trailing output')\n")
        code, text = run_audit("rust-run", "--binary", sys.executable, "--log-prefix", "logs/h",
                               "--job", "pairs", "run-a", "canonical")
        self.assertEqual(code, 1, text)
        self.assertEqual(run_audit("rust-run", "--binary", "missing.exe", "--log-prefix", "logs/m",
                                   "--job", "pairs", "run-a", "canonical")[0], 1)
        self.assertEqual(run_audit("rust-run", "--binary", sys.executable, "--log-prefix", "logs/b",
                                   "--job", "pairs", "run-a", "fast")[0], 1)

    def test_report(self):
        checks = {"a": True, "rust_repeat_byte_identity": True, "rust_refined_convergence": True}
        committed = {"checks": checks, "checkCount": 3, "failedCheckCount": 0, "comparisonsNotRun": ["x"]}
        write_json("committed.json", committed)
        write_json("fresh.json", committed)
        required = ("--require-check", "rust_repeat_byte_identity", "--require-check", "rust_refined_convergence")
        code, text = run_audit("report", "--fresh", "fresh.json", "--committed", "committed.json", *required)
        self.assertEqual(code, 0, text)
        self.assertIn("stage5_report_byte_identical_to_committed=yes", text)
        fresh = copy.deepcopy(committed)
        del fresh["checks"]["rust_refined_convergence"]
        fresh["checkCount"] = 2
        write_json("fresh.json", fresh)
        self.assertEqual(run_audit("report", "--fresh", "fresh.json", "--committed", "committed.json",
                                   *required)[0], 1)
        fresh = copy.deepcopy(committed)
        fresh["checks"]["a"] = False
        fresh["failedCheckCount"] = 1
        write_json("fresh.json", fresh)
        self.assertEqual(run_audit("report", "--fresh", "fresh.json")[0], 1)
        fresh = copy.deepcopy(committed)
        fresh["comparisonsNotRun"] = []
        write_json("fresh.json", fresh)
        self.assertEqual(run_audit("report", "--fresh", "fresh.json", "--committed", "committed.json")[0], 1)
        fresh["checkCount"] = 4
        write_json("fresh.json", fresh)
        self.assertEqual(run_audit("report", "--fresh", "fresh.json")[0], 1)
        write_json("fresh.json", committed)
        self.assertEqual(run_audit("report", "--fresh", "fresh.json", "--committed", "absent.json")[0], 1)
        code, text = run_audit("report", "--fresh", "fresh.json", "--committed", "absent.json", "--committed-optional")
        self.assertEqual(code, 0, text)
        self.assertIn("stage5_report_committed=ABSENT", text)
        write_json("fresh.json", {"checks": {}})
        self.assertEqual(run_audit("report", "--fresh", "fresh.json")[0], 1)

    def test_reference_quick(self):
        summary = {"quick": True, "complete": True, "runs": [{"label": "a", "converged": True}],
                   "pending": [], "failedOther": [], "failedControl": ["c"]}
        write_json("ref/reference-pairs-summary.json", summary)
        self.assertEqual(run_audit("reference-quick", "--summary", "ref/reference-pairs-summary.json")[0], 0)
        for key, value in (("complete", False), ("quick", False), ("failedOther", ["b"]), ("pending", ["p"]),
                           ("runs", [])):
            broken = dict(summary, **{key: value})
            write_json("ref/reference-pairs-summary.json", broken)
            self.assertEqual(run_audit("reference-quick", "--summary", "ref/reference-pairs-summary.json")[0], 1,
                             key)

    @staticmethod
    def make_reference_template(converged_m1=True):
        runs = []
        for field in ("d16c", "d16c00"):
            for config in ("m1_L3_N8_lam0_T0", "m3_L3_N8_lam0_T0"):
                for universe in ("plusM", "minusM", "minusM_control"):
                    label = f"{field}_{config}/{universe}"
                    write_text(os.path.join("template", label, "spectrum.csv"), f"{label}\n")
                    write_json(os.path.join("template", label, "run.json"), {"label": label})
                    ok = converged_m1 or config.startswith("m3")
                    runs.append({"label": label, "converged": ok, "E": 1.0})
        write_json(os.path.join("template", "reference-pairs-summary.json"), {"runs": runs})
        return runs

    def test_select_reproduction(self):
        runs = self.make_reference_template()
        records = {r["label"]: r for r in runs}
        self.assertEqual(audit.select_reproduction(records, 2),
                         ["d16c_m1_L3_N8_lam0_T0/plusM", "d16c_m1_L3_N8_lam0_T0/minusM",
                          "d16c00_m1_L3_N8_lam0_T0/plusM", "d16c00_m1_L3_N8_lam0_T0/minusM"])
        records["d16c_m1_L3_N8_lam0_T0/minusM"]["converged"] = False
        records["d16c00_m1_L3_N8_lam0_T0/plusM"]["failed"] = "x"
        self.assertEqual(audit.select_reproduction(records, 2),
                         ["d16c_m3_L3_N8_lam0_T0/plusM", "d16c_m3_L3_N8_lam0_T0/minusM",
                          "d16c00_m3_L3_N8_lam0_T0/plusM", "d16c00_m3_L3_N8_lam0_T0/minusM"])
        self.assertEqual(len(audit.select_reproduction(records, 1)), 2)
        self.assertEqual(audit.select_reproduction({}, 2), [])

    def test_reference_reproduce_with_a_stand_in_runner(self):
        self.make_reference_template()
        write_text(os.path.join("scripts", "ks_reference_pairs.py"), FAKE_REFERENCE_RUNNER)
        code, text = run_audit("reference-reproduce", "--committed", "template", "--output", "out")
        self.assertEqual(code, 0, text)
        self.assertIn("8 committed files compared in 4 run directories", text)
        os.environ["FAKE_REFERENCE_DRIFT"] = "1"
        try:
            shutil.rmtree("out")
            code, text = run_audit("reference-reproduce", "--committed", "template", "--output", "out")
            self.assertEqual(code, 1, text)
            self.assertIn("1 file(s) differ from the committed run", text)
        finally:
            del os.environ["FAKE_REFERENCE_DRIFT"]
        # a summary record that differs, and a file the fresh run did not write
        shutil.rmtree("out")
        with open(os.path.join("template", "reference-pairs-summary.json"), encoding="utf-8") as handle:
            summary = json.load(handle)
        shutil.copytree("template", "committed")
        summary["runs"][0]["E"] = 2.0
        write_json(os.path.join("committed", "reference-pairs-summary.json"), summary)
        write_text(os.path.join("committed", "d16c00_m1_L3_N8_lam0_T0", "minusM", "extra.csv"), "x\n")
        code, text = run_audit("reference-reproduce", "--committed", "committed", "--output", "out")
        self.assertEqual(code, 1, text)
        self.assertIn("the fresh summary record differs", text)
        self.assertIn("holds other files", text)
        # a failing runner
        write_text(os.path.join("scripts", "ks_reference_pairs.py"), "import sys\nsys.exit(1)\n")
        shutil.rmtree("out")
        code, text = run_audit("reference-reproduce", "--committed", "template", "--output", "out")
        self.assertEqual(code, 1, text)
        # no converged pair at all
        write_json(os.path.join("template", "reference-pairs-summary.json"), {"runs": []})
        code, text = run_audit("reference-reproduce", "--committed", "template", "--output", "out2")
        self.assertEqual(code, 1, text)
        self.assertIn("has no converged plusM/minusM pair", text)

    def test_tree_same(self):
        write_text("committed/fig/a.png", "a")
        write_text("committed/b.json", "{}\n")
        shutil.copytree("committed", "fresh")
        self.assertEqual(run_audit("tree-same", "--committed", "committed", "--fresh", "fresh")[0], 0)
        write_text("fresh/fig/a.png", "b")
        self.assertEqual(run_audit("tree-same", "--committed", "committed", "--fresh", "fresh")[0], 1)
        write_text("fresh/fig/a.png", "a")
        write_text("fresh/extra.png", "x")
        self.assertEqual(run_audit("tree-same", "--committed", "committed", "--fresh", "fresh")[0], 1)
        self.assertEqual(run_audit("tree-same", "--committed", "committed", "--fresh", "absent")[0], 1)
        self.assertEqual(run_audit("tree-same", "--committed", "absent", "--fresh", "fresh")[0], 1)

    def test_snapshot_unchanged_fresh(self):
        write_text("tree/a.txt", "a\n")
        write_json("tree/b.json", {"engine": {"binary": "x"}, "v": 1})
        self.assertEqual(run_audit("snapshot", "--into", "snap", "tree")[0], 0)
        self.assertEqual(run_audit("unchanged", "--snapshot", "snap", "tree")[0], 0)
        write_json("tree/b.json", {"engine": {"binary": "y"}, "v": 1})
        self.assertEqual(run_audit("unchanged", "--snapshot", "snap", "tree")[0], 1)
        self.assertEqual(run_audit("unchanged", "--snapshot", "snap", "--ignore-json-key", "engine.binary", "tree")[0], 0)
        write_text("tree/c.txt", "new\n")
        self.assertEqual(run_audit("unchanged", "--snapshot", "snap", "--ignore-json-key", "engine.binary", "tree")[0], 1)
        os.remove("tree/a.txt")
        os.remove("tree/c.txt")
        self.assertEqual(run_audit("unchanged", "--snapshot", "snap", "--ignore-json-key", "engine.binary", "tree")[0], 1)
        self.assertEqual(run_audit("snapshot", "--into", "snap2", "tree/missing.txt")[0], 1)
        write_text("tree/c.txt", "new\n")
        since = int(time.time()) - 5
        self.assertEqual(run_audit("fresh", "--since", str(since), "tree/c.txt")[0], 0)
        self.assertEqual(run_audit("fresh", "--since", str(since + 3600), "tree/c.txt")[0], 1)
        self.assertEqual(run_audit("fresh", "--since", str(since), "tree/missing.txt")[0], 1)

    def test_wolfram_log(self):
        write_text("ok.log", "started_utc=x\ncheck_count=45\nfailed_check_count=0\nexit_code=0\n")
        self.assertEqual(run_audit("wolfram-log", "--log", "ok.log")[0], 0)
        write_text("bad.log", "started_utc=x\nFailed to open file scripts/x.wls\nexit_code=0\n")
        code, text = run_audit("wolfram-log", "--log", "bad.log")
        self.assertEqual(code, 1)
        self.assertIn("Failed to open file scripts/x.wls", text)
        self.assertEqual(run_audit("wolfram-log", "--log", "absent.log")[0], 1)


def find_executable(*names):
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    return None


class GateTwinTests(unittest.TestCase):

    def test_both_twins_are_lf_only_and_end_alike(self):
        for path in (GATE_PS1, GATE_SH, AUDIT_PATH):
            with open(path, "rb") as handle:
                data = handle.read()
            self.assertNotIn(b"\r", data, path)
            self.assertTrue(data.endswith(b"\n"), path)
            self.assertFalse(b"@@" in data, "%s holds an unfilled @@ placeholder" % path)
        for path in (GATE_PS1, GATE_SH):
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
            for needle in ("stage5_pair_creation_verification=OK", "stage5_pair_creation_verification=FAILED",
                           "stage5_pair_creation_verification=PARTIAL", "stage5_pair_creation_verification=DRY-RUN",
                           "scripts/verify_stage5_pair_creation_audit.py", "run_logged", "wolfram-log",
                           "build/stage5.lock", "Failed to open file", 'test_d16c_stage5*.py',
                           "scripts/build_dirac16complex_pairs_figures.py"):
                self.assertIn(needle, text, "%s lacks %s" % (path, needle))

    @staticmethod
    def steps_of(output):
        names = []
        for line in output.splitlines():
            for prefix in ("stage5_dry_run_step=", "stage5_skipped_step=", "stage5_step_not_selected="):
                if line.startswith(prefix):
                    names.append(line[len(prefix):].split(" ")[0])
        return names

    @staticmethod
    def expected_of(output):
        """(step, expected wall time) of every dry-run line."""
        pairs = []
        for line in output.splitlines():
            if line.startswith("stage5_dry_run_step="):
                name, _, rest = line[len("stage5_dry_run_step="):].partition(" expected=[")
                pairs.append((name, rest[:-1] if rest.endswith("]") else rest))
        return pairs

    @staticmethod
    def run_twin(command, cwd=REPO):
        completed = subprocess.run(command, cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                                   errors="replace", timeout=300)
        return completed.returncode, completed.stdout + completed.stderr

    def twins(self):
        bash = find_executable("bash")
        pwsh = find_executable("pwsh")
        if not bash or not pwsh:
            self.skipTest("bash and pwsh are both needed to compare the twins")
        return bash, pwsh

    def test_dry_runs_list_the_same_steps(self):
        bash, pwsh = self.twins()
        code_sh, out_sh = self.run_twin([bash, GATE_SH, "--dry-run"])
        code_ps, out_ps = self.run_twin([pwsh, "-NoProfile", "-File", GATE_PS1, "-DryRun"])
        if "stage5_failed_step=tools" in out_sh + out_ps:
            self.skipTest("a required tool is missing on this machine")
        self.assertEqual(code_sh, 0, out_sh[-2000:])
        self.assertEqual(code_ps, 0, out_ps[-2000:])
        steps_sh, steps_ps = self.steps_of(out_sh), self.steps_of(out_ps)
        self.assertEqual(steps_sh, steps_ps)
        self.assertEqual(len(steps_sh), STEP_COUNT)
        self.assertEqual([name[7:9] for name in steps_sh], ["%02d" % n for n in range(STEP_COUNT)])
        for name in ("stage5-14-rust-pairs", "stage5-20-reference-reproduce", "stage5-23-figures",
                     "stage5-28-unit-tests"):
            self.assertIn(name, steps_sh)
        self.assertEqual(self.expected_of(out_sh), self.expected_of(out_ps))
        self.assertFalse("@@" in out_sh + out_ps, "an expected wall time is an unfilled @@ placeholder")
        self.assertTrue(out_sh.rstrip().endswith("stage5_pair_creation_verification=DRY-RUN"))
        self.assertTrue(out_ps.rstrip().endswith("stage5_pair_creation_verification=DRY-RUN"))
        for output in (out_sh, out_ps):
            commands = [line for line in output.splitlines() if "rust-run --binary" in line]
            self.assertEqual(len(commands), 2)
            self.assertEqual([c.count("--job") for c in commands], [3, 2])
            self.assertIn("--job pairs build/stage5/run-a canonical --job pairs build/stage5/refined refined",
                          commands[1])
            self.assertNotIn("--sequential", output)
            self.assertIn("ks_reference_pairs.py --quick --output build/stage5/reference-quick", output)
            self.assertIn("build_dirac16complex_pairs_figures.py --output build/stage5/figures", output)
            self.assertIn("--require-check rust_repeat_byte_identity --require-check rust_refined_convergence",
                          output)
        code_sh, out_sh = self.run_twin([bash, GATE_SH, "--dry-run", "--sequential-rust", "--steps", "11,14"])
        code_ps, out_ps = self.run_twin([pwsh, "-NoProfile", "-File", GATE_PS1, "-DryRun", "-SequentialRust",
                                         "-Steps", "11,14"])
        for output in (out_sh, out_ps):
            commands = [line for line in output.splitlines() if "rust-run --binary" in line]
            self.assertEqual(len(commands), 2)
            self.assertTrue(all("--sequential" in c for c in commands))
        self.assertEqual(self.expected_of(out_sh), self.expected_of(out_ps))
        code_sh, out_sh = self.run_twin([bash, GATE_SH, "--dry-run", "--steps", "05,stage5-13-stage4-identity-audit"])
        code_ps, out_ps = self.run_twin([pwsh, "-NoProfile", "-File", GATE_PS1, "-DryRun", "-Steps",
                                         "05,stage5-13-stage4-identity-audit"])
        for output in (out_sh, out_ps):
            selected = [line.split("=")[1].split(" ")[0] for line in output.splitlines()
                        if line.startswith("stage5_dry_run_step=")]
            self.assertEqual(selected, ["stage5-05-theory-same", "stage5-13-stage4-identity-audit"])

    def test_lock_refuses_a_second_gate_and_is_released_on_failure(self):
        bash, pwsh = self.twins()
        temp = tempfile.mkdtemp(prefix="d16c_s5_gate_")
        try:
            os.makedirs(os.path.join(temp, "scripts"))
            for name in ("verify_stage5_pair_creation.sh", "verify_stage5_pair_creation.ps1",
                         "verify_stage5_pair_creation_audit.py", "run_logged.sh", "run_logged.ps1"):
                shutil.copyfile(os.path.join(REPO, "scripts", name), os.path.join(temp, "scripts", name))
            lock = os.path.join(temp, "build", "stage5.lock")
            for command in ([bash, os.path.join(temp, "scripts", "verify_stage5_pair_creation.sh"), "--steps", "19"],
                            [pwsh, "-NoProfile", "-File", os.path.join(temp, "scripts", "verify_stage5_pair_creation.ps1"),
                             "-Steps", "19"]):
                write_text(os.path.join(lock, "owner"), "pid=1 twin=test\n")
                code, output = self.run_twin(command, cwd=temp)
                if "stage5_failed_step=tools" in output:
                    self.skipTest("a required tool is missing on this machine")
                self.assertEqual(code, 1, output[-2000:])
                self.assertIn("stage5_failed_step=lock", output)
                self.assertIn("pid=1 twin=test", output)
                self.assertTrue(output.rstrip().endswith("stage5_pair_creation_verification=FAILED"))
                self.assertTrue(os.path.isdir(lock), "a refused gate must not remove another gate's lock")
                shutil.rmtree(lock)
                # step 19 audits a reference summary that does not exist here: the step fails,
                # and the gate releases its own lock
                code, output = self.run_twin(command, cwd=temp)
                self.assertEqual(code, 1, output[-2000:])
                self.assertIn("stage5_failed_step=stage5-19-reference-quick-audit", output)
                self.assertIn("stage5_failed_log=build/logs/stage5-19-reference-quick-audit", output)
                self.assertFalse(os.path.exists(lock), "the gate kept its lock after a failed step")
        finally:
            shutil.rmtree(temp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
