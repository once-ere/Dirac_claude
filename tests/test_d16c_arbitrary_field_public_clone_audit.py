# SPDX-License-Identifier: GPL-3.0-or-later
"""Tests of the public-clone mode helpers of the Stage 1 gate (standard library only).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_arbitrary_field_public_clone_audit.py" -v

scripts/verify_stage1_public_clone_audit.py compares the files the Stage 1 gate
regenerates into build/stage1/ without dirac-main with the committed ones; these
tests build small committed/regenerated trees in temporary directories and check
that exactly the differences a missing dirac-main causes are allowed and that every
other difference fails.  One test derives the no-dirac-main versions of the real
committed Stage 1 reports.  scripts/run_with_report_path.py is tested with small
producer modules written into a temporary directory.  Nothing is written outside
tempfile directories.
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import verify_stage1_public_clone_audit as audit  # noqa: E402

COMMITTED = "artifacts/dirac16complex/arbitrary-field"
REGENERATED = "build/stage1"
ARTIFACTS = REPOSITORY_ROOT / COMMITTED
RUNNER = REPOSITORY_ROOT / "scripts" / "run_with_report_path.py"
SEED = "dirac-main/artifacts/exact/cl44-seed.json"
HEX_A = "a" * 64
HEX_B = "b" * 64
# The cross-checks that a run without dirac-main records as "not-run" (a fresh public
# clone on 2026-09-30): seven of the Wolfram algebra report and three of the Python
# algebra report.  ALG_cliffordPictureIntertwiner.diracMainVolumeEqualsGGGG mentions
# dirac-main but needs none of its files and stays true.
DIRAC_MAIN_CROSS_CHECKS = (
    "ALG_cliffordPictureIntertwiner.matchesDiracMainCl44SeedGenerators",
    "ALG_cliffordPictureIntertwiner.matchesDiracMainCl44SeedVolumeElement",
    "ALG_octonionPictureIntertwiner.matchesDiracMainSplitOctonionMultiplicationTensor",
    "ALG_octonionPictureIntertwiner.gammasFromDiracMainSplitOctonionJsonEqualRebuilt",
    "ALG_octonionPictureIntertwiner.matchesDiracMainTriality44OctonionCliffordGenerators",
    "ALG_octonionPictureIntertwiner.diracMainCanonicalIntertwinerEqualsPrimitiveKcliffordKoctonion",
    "ALG_octonionPictureIntertwiner.diracMainCanonicalIntertwinerVerified",
    "ALG_octonionGammasEqualDiracMainTriality44Json",
    "ALG_KcliffordKoctonionEqualsDiracMainCanonicalIntertwiner",
    "ALG_zornProductEqualsDiracMainSplitOctonionJson",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encode(document, indent=2) -> bytes:
    return (json.dumps(document, indent=indent) + "\n").encode("utf-8")


def committed_path(name):
    return "%s/%s" % (COMMITTED, name)


def regenerated_path(name):
    return "%s/%s" % (REGENERATED, name)


def build_case(root: Path, public_clone=True, tweak=None):
    """Write a small committed tree and its regeneration into root.

    With public_clone the regeneration differs exactly as a run without dirac-main
    does; tweak(side, name, document) may change a document (side "committed" or
    "regenerated") before it is written and before its hash enters later files.
    """
    tweak = tweak or (lambda side, name, document: None)
    trees = {}
    for side in ("committed", "regenerated"):
        missing = public_clone and side == "regenerated"
        location = (lambda name: committed_path(name)) if side == "committed" else (
            (lambda name: regenerated_path(name)) if public_clone else (lambda name: committed_path(name)))
        files = {}

        def put(name, document, indent=2):
            tweak(side, name, document)
            files[name] = encode(document, indent)

        put("algebra-fixture.json", {"K": [[1, 0], [0, 1]]})
        fixture_sha = sha256(files["algebra-fixture.json"])
        dirac_main_value = "not-run" if missing else True
        wolfram_algebra = {
            "schemaVersion": 1,
            "checks": {"ALG_clifford": True, "ALG_fixtureAgreement": True},
            "measurements": {
                "ALG_x.matchesDiracMainCl44SeedGenerators": dirac_main_value,
                "ALG_x.diracMainCanonicalIntertwinerVerified": dirac_main_value,
                "ALG_x.rank": 16,
                "ALG_x.ratio": 0.5,
                "ALG_x.intertwinerEquation": "K maps to the dirac-main picture",
                "fixtureAgreement.path": committed_path("algebra-fixture.json"),
                "referenceFilesPresent": {SEED: not missing, committed_path("algebra-fixture.json"): True},
            },
            "sourceSha256": {"wolfram/A.wl": HEX_A, SEED: HEX_B,
                             committed_path("algebra-fixture.json"): fixture_sha},
        }
        if missing:
            del wolfram_algebra["sourceSha256"][SEED]
        put("wolfram-algebra-report.json", wolfram_algebra, indent="\t")
        wolfram_algebra_sha = sha256(files["wolfram-algebra-report.json"])
        put("wolfram-geometry-report.json", {"schemaVersion": 1, "checks": {"GEO_a": True},
                                             "measurements": {"G1.p1.detFrame": "3/2"}})
        wolfram_geometry_sha = sha256(files["wolfram-geometry-report.json"])
        put("grassmann-demo-report.json", {"schemaVersion": 1, "checks": {"GR_a": True},
                                           "measurements": {"GR_k": [16, 120, 0]}})
        put("python-geometry-report.json", {"schemaVersion": 1, "checks": {"GEO_wolframAgreement": True},
                                            "measurements": {"GEO_wolframReportSha256": wolfram_geometry_sha}})
        python_algebra = {
            "schemaVersion": 1,
            "checks": {"ALG_fixtureAgreement": True, "ALG_wolframAgreement": True},
            "measurements": {
                "ALG_octonionGammasEqualDiracMainTriality44Json": dirac_main_value,
                "wolframReportSha256": wolfram_algebra_sha,
                "wolframSharedMeasurements": [
                    {"measurement": "ALG_x.matchesDiracMainCl44SeedGenerators <-> ALG_y",
                     "agree": True, "wolfram": dirac_main_value, "python": dirac_main_value},
                    {"measurement": "ALG_x.rank <-> ALG_rank", "agree": True, "wolfram": 16, "python": 16},
                    {"measurement": "ALG_z <-> ALG_zz", "agree": True, "wolfram": True, "python": True},
                ],
            },
            "inputSha256": {committed_path("algebra-fixture.json"): fixture_sha,
                            location("wolfram-algebra-report.json"): wolfram_algebra_sha},
        }
        put("python-algebra-report.json", python_algebra)
        python_algebra_sha = sha256(files["python-algebra-report.json"])
        summary = {
            "schemaVersion": 1,
            "reports": {
                "wolfram-algebra": {"path": location("wolfram-algebra-report.json"),
                                    "sha256": wolfram_algebra_sha},
                "wolfram-geometry": {"path": location("wolfram-geometry-report.json"),
                                     "sha256": wolfram_geometry_sha},
                "python-algebra": {"path": location("python-algebra-report.json"),
                                   "sha256": python_algebra_sha},
            },
            "fixture": {"path": location("algebra-fixture.json"), "sha256": fixture_sha},
            "crossImplementationComparisons": {"algebra": {"wolframReportSha256": wolfram_algebra_sha}},
            "counts": {"total": {"checks": 9, "passed": 9, "failed": 0}},
        }
        put("stage1-summary.json", summary)
        trees[side] = files
    for side, directory in (("committed", COMMITTED), ("regenerated", REGENERATED)):
        target = root / directory
        target.mkdir(parents=True, exist_ok=True)
        for name, data in trees[side].items():
            (target / name).write_bytes(data)


def run_audit(root: Path):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        code = audit.main(["--repository-root", str(root)])
    return code, output.getvalue().splitlines()


def dump(value) -> str:
    """Serialize a tree parsed by audit.parse, numbers with their literal text."""
    if isinstance(value, audit.Obj):
        return "{" + ", ".join(json.dumps(key) + ": " + dump(item) for key, item in value.pairs) + "}"
    if isinstance(value, list):
        return "[" + ", ".join(dump(item) for item in value) + "]"
    if isinstance(value, audit.Number):
        return value.text
    return json.dumps(value)


def transform(value, function):
    """Rebuild a parsed tree; function(key, value, parent) returns the new value of an object member."""
    if isinstance(value, audit.Obj):
        return audit.Obj([(key, function(key, transform(item, function), value)) for key, item in value.pairs])
    if isinstance(value, list):
        return [transform(item, function) for item in value]
    return value


class AuditTestCase(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)

    def tearDown(self):
        self.directory.cleanup()

    def assertAudit(self, expected_ok, **options):
        build_case(self.root, **options)
        code, lines = run_audit(self.root)
        self.assertEqual(lines[-1], "stage1_public_clone_audit=%s" % ("OK" if expected_ok else "FAILED"),
                         "\n".join(lines))
        self.assertEqual(code, 0 if expected_ok else 1)
        return lines


class AllowedDifferencesTests(AuditTestCase):
    def test_identical_trees_pass(self):
        lines = self.assertAudit(True, public_clone=False)
        self.assertEqual(sum(1 for line in lines if " identical sha256=" in line), 7)
        self.assertFalse([line for line in lines if line.startswith("stage1_audit_allowed=")])

    def test_missing_dirac_main_differences_pass(self):
        lines = self.assertAudit(True)
        allowed = [line for line in lines if line.startswith("stage1_audit_allowed=")]
        kinds = {}
        for line in allowed:
            for kind in ("not-run", "reference", "source-hash", "hash of wolfram-algebra-report.json",
                         "hash of python-algebra-report.json", "relocated"):
                if " %s: " % kind in line:
                    kinds[kind] = kinds.get(kind, 0) + 1
        self.assertEqual(kinds, {
            # 2 in the Wolfram report, 1 measurement and 2 row entries in the Python report
            "not-run": 5,
            "reference": 1,
            "source-hash": 1,
            # wolframReportSha256 and inputSha256 (Python), reports and comparisons (summary)
            "hash of wolfram-algebra-report.json": 4,
            "hash of python-algebra-report.json": 1,
            # inputSha256 key (Python); 3 report paths and the fixture path (summary)
            "relocated": 5,
        })
        self.assertEqual(len(allowed), 17)
        not_run = [line for line in lines if line.startswith("stage1_audit_not_run=")]
        self.assertIn("stage1_audit_not_run=python-algebra-report.json:"
                      "/measurements/wolframSharedMeasurements[0]/wolfram", not_run)
        self.assertEqual(len(not_run), 5)
        for name in ("algebra-fixture.json", "wolfram-geometry-report.json", "grassmann-demo-report.json",
                     "python-geometry-report.json"):
            self.assertTrue(any(line.startswith("stage1_audit_file=%s identical" % name) for line in lines))
        for name in ("wolfram-algebra-report.json", "python-algebra-report.json", "stage1-summary.json"):
            self.assertTrue(any(line.startswith("stage1_audit_file=%s allowed-differences=" % name)
                                for line in lines))

    def test_real_committed_reports_without_dirac_main_pass(self):
        """The no-dirac-main versions of the committed reports, derived as the verifiers write them."""
        source = {name: (ARTIFACTS / name).read_bytes() for name in audit.FILES}
        target = self.root / REGENERATED
        target.mkdir(parents=True)
        (self.root / COMMITTED).mkdir(parents=True)
        for name, data in source.items():
            (self.root / COMMITTED / name).write_bytes(data)
            (target / name).write_bytes(data)

        def without_dirac_main(key, value, parent):
            if value is True and key in DIRAC_MAIN_CROSS_CHECKS:
                return "not-run"
            measurement = parent.get("measurement")
            if (value is True and key in ("wolfram", "python") and isinstance(measurement, str)
                    and any(name in measurement.split(" <-> ") for name in DIRAC_MAIN_CROSS_CHECKS)):
                return "not-run"
            if key == "referenceFilesPresent":
                return audit.Obj([(k, False if k.startswith("dirac-main/") else v) for k, v in value.pairs])
            if key == "sourceSha256":
                return audit.Obj([(k, v) for k, v in value.pairs if not k.startswith("dirac-main/")])
            return value

        wolfram = transform(audit.parse(source["wolfram-algebra-report.json"]), without_dirac_main)
        wolfram_bytes = (dump(wolfram) + "\n").encode("utf-8")
        old_wolfram, new_wolfram = sha256(source["wolfram-algebra-report.json"]), sha256(wolfram_bytes)
        self.assertEqual(wolfram.get("measurements").get("referenceFilesPresent").get(
            "dirac-main/artifacts/exact/triality44.json"), False)

        def relocate_and_rehash(mapping, relocated):
            def function(key, value, parent):
                if isinstance(value, str) and value in mapping:
                    return mapping[value]
                if isinstance(value, str) and value in relocated:
                    return regenerated_path(value.rsplit("/", 1)[1])
                if isinstance(value, audit.Obj):
                    return audit.Obj([(regenerated_path(k.rsplit("/", 1)[1]) if k in relocated else k, v)
                                      for k, v in value.pairs])
                return value
            return function

        python = transform(audit.parse(source["python-algebra-report.json"]), without_dirac_main)
        python = transform(python, relocate_and_rehash({old_wolfram: new_wolfram},
                                                       {committed_path("wolfram-algebra-report.json")}))
        python_bytes = (dump(python) + "\n").encode("utf-8")
        old_python, new_python = sha256(source["python-algebra-report.json"]), sha256(python_bytes)
        summary = transform(audit.parse(source["stage1-summary.json"]), relocate_and_rehash(
            {old_wolfram: new_wolfram, old_python: new_python},
            {committed_path(name) for name in audit.FILES}))
        (target / "wolfram-algebra-report.json").write_bytes(wolfram_bytes)
        (target / "python-algebra-report.json").write_bytes(python_bytes)
        (target / "stage1-summary.json").write_bytes((dump(summary) + "\n").encode("utf-8"))

        code, lines = run_audit(self.root)
        self.assertEqual(lines[-1], "stage1_public_clone_audit=OK", "\n".join(lines))
        self.assertEqual(code, 0)
        not_run = [line for line in lines if line.startswith("stage1_audit_not_run=")]
        # the ten dirac-main cross-checks of the two algebra reports (Wolfram 7, Python 3),
        # and the Python comparison rows of the three shared ones (wolfram and python entries)
        self.assertEqual(len([line for line in not_run if "wolfram-algebra" in line]), 7)
        self.assertEqual(len([line for line in not_run if "python-algebra" in line]), 3 + 2 * 3)

    def test_committed_reports_against_themselves(self):
        target = self.root / REGENERATED
        shutil.copytree(ARTIFACTS, self.root / COMMITTED)
        shutil.copytree(ARTIFACTS, target)
        code, lines = run_audit(self.root)
        self.assertEqual((code, lines[-1]), (0, "stage1_public_clone_audit=OK"))


class ForbiddenDifferencesTests(AuditTestCase):
    def tweak(self, side, name, function):
        def hook(this_side, this_name, document):
            if this_side == side and this_name == name:
                function(document)
        return hook

    def test_not_run_of_a_check_not_about_dirac_main(self):
        lines = self.assertAudit(False, tweak=self.tweak(
            "regenerated", "wolfram-algebra-report.json",
            lambda d: d["checks"].__setitem__("ALG_clifford", "not-run")))
        self.assertIn("stage1_audit_forbidden=wolfram-algebra-report.json /checks/ALG_clifford "
                      'true -> "not-run"', lines)

    def test_dirac_main_check_false_instead_of_not_run(self):
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "wolfram-algebra-report.json",
            lambda d: d["measurements"].__setitem__("ALG_x.matchesDiracMainCl44SeedGenerators", False)))

    def test_dirac_main_check_committed_not_run(self):
        # committed "not-run", regenerated true: only true -> "not-run" is allowed
        self.assertAudit(False, public_clone=False, tweak=self.tweak(
            "committed", "wolfram-algebra-report.json",
            lambda d: d["measurements"].__setitem__("ALG_x.diracMainCanonicalIntertwinerVerified", "not-run")))

    def test_not_run_in_a_row_not_about_dirac_main(self):
        def change(document):
            document["measurements"]["wolframSharedMeasurements"][2]["wolfram"] = "not-run"
        self.assertAudit(False, tweak=self.tweak("regenerated", "python-algebra-report.json", change))

    def test_dirac_main_in_a_value_does_not_allow_not_run(self):
        # "ALG_x.intertwinerEquation" mentions dirac-main only in its value
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "wolfram-algebra-report.json",
            lambda d: d["measurements"].__setitem__("ALG_x.intertwinerEquation", "not-run")))

    def test_unexplained_hash(self):
        lines = self.assertAudit(False, tweak=self.tweak(
            "regenerated", "python-algebra-report.json",
            lambda d: d["measurements"].__setitem__("wolframReportSha256", "0" * 64)))
        self.assertTrue(any("/measurements/wolframReportSha256" in line for line in lines
                            if line.startswith("stage1_audit_forbidden=")))

    def test_hash_of_an_unchanged_file(self):
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "stage1-summary.json",
            lambda d: d["reports"]["wolfram-geometry"].__setitem__("sha256", HEX_A)))

    def test_hash_of_a_file_with_a_forbidden_difference(self):
        # the Wolfram algebra report fails, so the hashes of it in later files are not explained
        lines = self.assertAudit(False, tweak=self.tweak(
            "regenerated", "wolfram-algebra-report.json",
            lambda d: d["measurements"].__setitem__("ALG_x.rank", 17)))
        self.assertTrue(any(line.startswith("stage1_audit_file=python-algebra-report.json FAILED")
                            for line in lines))
        self.assertTrue(any(line.startswith("stage1_audit_file=stage1-summary.json FAILED") for line in lines))

    def test_removal_of_a_source_hash_not_of_dirac_main(self):
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "wolfram-algebra-report.json", lambda d: d["sourceSha256"].pop("wolfram/A.wl")))

    def test_changed_dirac_main_source_hash(self):
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "wolfram-algebra-report.json", lambda d: d["sourceSha256"].__setitem__(SEED, HEX_A)))

    def test_reference_file_not_of_dirac_main(self):
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "wolfram-algebra-report.json",
            lambda d: d["measurements"]["referenceFilesPresent"].__setitem__(
                committed_path("algebra-fixture.json"), False)))

    def test_dirac_main_present_allows_nothing(self):
        for name in audit.DIRAC_MAIN_FILES:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"{}\n")
        lines = self.assertAudit(False)
        self.assertIn("stage1_audit_dirac_main=present", lines)
        self.assertFalse([line for line in lines if line.startswith("stage1_audit_not_run=")])

    def test_number_literal(self):
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "wolfram-algebra-report.json",
            lambda d: d["measurements"].__setitem__("ALG_x.rank", 16.0)))

    def test_type_change_true_to_one(self):
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "wolfram-algebra-report.json", lambda d: d["checks"].__setitem__("ALG_clifford", 1)))

    def test_key_order(self):
        def reorder(document):
            items = list(document["measurements"].items())
            document["measurements"].clear()
            document["measurements"].update(reversed(items))
        self.assertAudit(False, tweak=self.tweak("regenerated", "wolfram-algebra-report.json", reorder))

    def test_extra_key(self):
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "wolfram-algebra-report.json", lambda d: d["measurements"].__setitem__("extra", 1)))

    def test_array_length(self):
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "grassmann-demo-report.json", lambda d: d["measurements"]["GR_k"].append(0)))

    def test_formatting_only_difference(self):
        build_case(self.root)
        path = self.root / REGENERATED / "wolfram-geometry-report.json"
        path.write_bytes(encode(json.loads(path.read_bytes()), indent=4))
        code, lines = run_audit(self.root)
        self.assertEqual(code, 1)
        self.assertIn("stage1_audit_forbidden=wolfram-geometry-report.json / the bytes differ but no value "
                      "does (formatting-only difference)", lines)

    def test_changed_fixture(self):
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "algebra-fixture.json", lambda d: d.__setitem__("K", [[1, 0], [0, -1]])))

    def test_missing_regenerated_file(self):
        build_case(self.root)
        (self.root / REGENERATED / "grassmann-demo-report.json").unlink()
        code, lines = run_audit(self.root)
        self.assertEqual((code, lines[-1]), (1, "stage1_public_clone_audit=FAILED"))
        self.assertTrue(any("regenerated file build/stage1/grassmann-demo-report.json is missing" in line
                            for line in lines))

    def test_relocation_only_of_the_stage1_files(self):
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "stage1-summary.json",
            lambda d: d["fixture"].__setitem__("path", regenerated_path("other-fixture.json"))))

    def test_relocation_must_match_the_committed_path(self):
        # a relocated path where the committed report has a different file
        self.assertAudit(False, tweak=self.tweak(
            "regenerated", "stage1-summary.json",
            lambda d: d["fixture"].__setitem__("path", regenerated_path("stage1-summary.json"))))

    def test_invalid_json(self):
        build_case(self.root)
        path = self.root / REGENERATED / "python-geometry-report.json"
        path.write_bytes(path.read_bytes()[:-3])
        code, lines = run_audit(self.root)
        self.assertEqual(code, 1)
        self.assertTrue(any("not UTF-8 JSON" in line for line in lines))

    def test_usage_errors(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = audit.main(["--repository-root", str(self.root), "--regenerated",
                               str(self.root / "nowhere")])
        self.assertEqual(code, 2)
        self.assertIn("stage1_public_clone_audit=FAILED", output.getvalue())


PRODUCER = '''
import json
import sys
from pathlib import Path

REPORT_PATH = Path(__file__).resolve().parent / "default-report.json"


def main(%s):
    REPORT_PATH.write_text(json.dumps({"argv": %s, "sys_argv": sys.argv[1:]}))
    return %d
'''


class RunWithReportPathTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)

    def tearDown(self):
        self.directory.cleanup()

    def producer(self, name, text):
        path = self.root / name
        path.write_text(text)
        return path

    def run_runner(self, *arguments):
        return subprocess.run([sys.executable, str(RUNNER)] + [str(a) for a in arguments],
                              capture_output=True, text=True, cwd=str(self.root))

    def test_report_is_written_to_the_given_path(self):
        script = self.producer("producer_a.py", PRODUCER % ("argv=None", "argv", 0))
        report = self.root / "out" / "report.json"
        report.parent.mkdir()
        result = self.run_runner(report, script, "--wolfram-report", "x.json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(report.read_text()),
                         {"argv": ["--wolfram-report", "x.json"], "sys_argv": ["--wolfram-report", "x.json"]})
        self.assertFalse((self.root / "default-report.json").exists())

    def test_main_without_parameters(self):
        script = self.producer("producer_b.py", PRODUCER % ("", "None", 0))
        report = self.root / "report.json"
        self.assertEqual(self.run_runner(report, script).returncode, 0)
        self.assertEqual(json.loads(report.read_text()), {"argv": None, "sys_argv": []})
        result = self.run_runner(report, script, "--unexpected")
        self.assertEqual(result.returncode, 2)
        self.assertIn("takes no arguments", result.stdout)

    def test_exit_status_is_passed_on(self):
        script = self.producer("producer_c.py", PRODUCER % ("argv=None", "argv", 1))
        self.assertEqual(self.run_runner(self.root / "report.json", script).returncode, 1)

    def test_refusals(self):
        script = self.producer("producer_d.py", "def main():\n    return 0\n")
        result = self.run_runner(self.root / "report.json", script)
        self.assertEqual(result.returncode, 2)
        self.assertIn("has no pathlib.Path REPORT_PATH", result.stdout)
        script = self.producer("producer_e.py", PRODUCER % ("argv=None", "argv", 0))
        result = self.run_runner(self.root / "default-report.json", script)
        self.assertEqual(result.returncode, 2)
        self.assertIn("REPORT_PATH is already", result.stdout)
        script = self.producer("producer_f.py", PRODUCER.replace("REPORT_PATH.write_text", "print") % (
            "argv=None", "argv", 0))
        result = self.run_runner(self.root / "report.json", script)
        self.assertEqual(result.returncode, 2)
        self.assertIn("did not write", result.stdout)
        self.assertEqual(self.run_runner(self.root / "report.json").returncode, 2)

    def test_stage1_producers_have_the_expected_interface(self):
        """The two Stage 1 scripts the gate runs through the runner keep REPORT_PATH and main()."""
        for name, takes_arguments in (("check_dirac16complex_geometry.py", True),
                                      ("demo_grassmann_lagrangians.py", False)):
            text = (REPOSITORY_ROOT / "scripts" / name).read_text(encoding="utf-8")
            self.assertIn('REPORT_PATH = ROOT / "artifacts" / "dirac16complex" / "arbitrary-field" / ', text)
            self.assertIn("REPORT_PATH.write_bytes(", text)
            self.assertIn("def main(argv=None) -> int:" if takes_arguments else "def main() -> int:", text)


if __name__ == "__main__":
    unittest.main()
