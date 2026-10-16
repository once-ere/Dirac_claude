#!/usr/bin/env python3
"""Publication test for Revision/docs/METRIC_SELF_CONSISTENCY.{md,tex,pdf}.

The document answers the user's order of 2026-10-16: the issue (a diagonal metric is self-consistent only if every
off-diagonal component of the sources vanishes), why the metric of 2026-10-14 is not self-consistent with diagonal
sources, the simplest remedy (the warped metric, g44 = -Sin[6 H x0]^(1/3)), its field equations, its exact solutions
and what it changes for the fields.  It is built and registered with

    python scripts/build_provenance_pdf.py Revision/docs/METRIC_SELF_CONSISTENCY.md \
        --developer-layout --specifications Revision/pdf-specifications.json [--register]

Run from the repository root:
    python -m unittest Revision/tests/test_metric_self_consistency_publication.py -v

What is tested
  * the committed .tex is exactly the builder's output for the committed .md, both files are UTF-8 with LF line
    endings, and their sha256 are pinned;
  * the PDF is registered in Revision/pdf-specifications.json (edition metric-self-consistency) and is structurally
    sound;
  * title, sections and the last section; the key statements; the author's notebook is described as read only;
  * every check name the document cites exists in the two reports of Revision/metric_warped with the verdict PASS,
    every check of the two reports is listed, and the counts quoted are the reports' counts;
  * the formulas quoted (the warped metric, the layer coefficients, the effective couplings, the Kasner exponents,
    the history's source) equal the values of Revision/metric_warped/results/warped-metric.json;
  * OPTIONAL (REVISION_PDF_REBUILD=1; needs pdflatex, about 10 s): the PDF is rebuilt in verify mode.
After an intended edit: rebuild until warning-free, register (--register), update MARKDOWN_SHA256 and TEX_SHA256.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

REVISION = Path(__file__).resolve().parents[1]
ROOT = REVISION.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import build_dissertation_tex as builder  # noqa: E402
from scripts import check_dissertation_pdf  # noqa: E402
from scripts import check_provenance_pdf  # noqa: E402

DOCS = REVISION / "docs"
MARKDOWN = DOCS / "METRIC_SELF_CONSISTENCY.md"
TEX = DOCS / "METRIC_SELF_CONSISTENCY.tex"
PDF = DOCS / "METRIC_SELF_CONSISTENCY.pdf"
EDITION = "metric-self-consistency"
REGISTRY = REVISION / "pdf-specifications.json"
REBUILD = os.environ.get("REVISION_PDF_REBUILD") == "1"

MARKDOWN_SHA256 = "b405546bc209a2c796cc6e9c7d8127d45011ae358097e02e060eb937a270ef2c"
TEX_SHA256 = "238aec69581e4ba97f5a596b8b22db44addac94dc3fb5aef1540b6f66af5a236"

MW = REVISION / "metric_warped"
PY_REPORT = MW / "reports" / "python-warped-metric-report.json"
WL_REPORT = MW / "reports" / "wolfram-warped-metric-report.json"
RESULTS = MW / "results" / "warped-metric.json"

TITLE = "The self-consistency of the primordial metric with diagonal sources"
SECTIONS = (
    "## Abstract",
    "## 1. The issue",
    "## 2. Where off-diagonal terms come from",
    "## 3. The simplest remedy: the warped metric",
    "## 4. The field equations of the warped metric",
    "## 5. What the warped metric changes for the fields",
    "## 6. Consequences for the Revision record",
    "## 7. What is proved, computed, assumed and open",
    "## 8. Reproduction",
    "## 9. Verification records",
)
KEY_STATEMENTS = (
    "none of its definitions or conventions is used in the Revision record",
    "It differs from the metric of 2026-10-14 in one entry, $g_{44} = -1 \\to -\\sin^{1/3}z$",
    "No diagonal metric removes them",
    "The history remains a PRESCRIBED background: no field of the record is shown to be its source.",
    "At this commit that condition is OPEN for the warped metric.",
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def markdown_text() -> str:
    return MARKDOWN.read_text(encoding="utf-8")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def report_names(path: Path) -> dict:
    return {check["name"]: check["verdict"] for check in load_json(path)["checks"]}


class Files(unittest.TestCase):
    def test_tex_is_builder_output(self):
        expected = builder.convert(markdown_text(), strip_heading_numbers=True, developer_layout=True,
                                   image_root=ROOT)
        self.assertEqual(TEX.read_text(encoding="utf-8"), expected)

    def test_utf8_lf_and_pinned_sha256(self):
        for path in (MARKDOWN, TEX):
            data = path.read_bytes()
            data.decode("utf-8")
            self.assertNotIn(b"\r", data, path.name)
            self.assertNotIn(b"\t", data, path.name)
        self.assertEqual(sha256_file(MARKDOWN), MARKDOWN_SHA256)
        self.assertEqual(sha256_file(TEX), TEX_SHA256)


class RegisteredPdf(unittest.TestCase):
    def test_registered_in_the_revision_registry(self):
        registry = check_provenance_pdf.load_specifications(REGISTRY)
        self.assertIn(EDITION, registry)
        entry = registry[EDITION]
        pdf_bytes = PDF.read_bytes()
        self.assertEqual(entry["path"], "Revision/docs/METRIC_SELF_CONSISTENCY.pdf")
        self.assertEqual(entry["sha256"], hashlib.sha256(pdf_bytes).hexdigest())
        self.assertEqual(entry["pages"], len(check_dissertation_pdf.PAGE_PATTERN.findall(pdf_bytes)))

    def test_pdf_structure(self):
        pdf_bytes = PDF.read_bytes()
        self.assertTrue(pdf_bytes.startswith(b"%PDF-"))
        self.assertTrue(pdf_bytes.rstrip().endswith(b"%%EOF"))
        self.assertEqual(check_dissertation_pdf.parse_media_boxes(pdf_bytes), [(0.0, 0.0, 612.0, 792.0)])

    @unittest.skipUnless(REBUILD, "set REVISION_PDF_REBUILD=1 to rebuild the PDF in verify mode")
    def test_rebuild_in_verify_mode(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_provenance_pdf.py"), str(MARKDOWN.relative_to(ROOT)),
             "--developer-layout", "--specifications", str(REGISTRY.relative_to(ROOT))],
            cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False, timeout=1800)
        output = completed.stdout.decode("utf-8", "replace")
        self.assertEqual(completed.returncode, 0, output[-3000:])
        self.assertIn("check_logWarningFree=true", output)
        self.assertIn("provenance_pdf=OK", output)


class Content(unittest.TestCase):
    def setUp(self):
        self.text = markdown_text()

    def test_title_and_sections(self):
        lines = self.text.split("\n")
        self.assertEqual(lines[0], "# " + TITLE)
        positions = []
        for heading in SECTIONS:
            self.assertIn("\n" + heading + "\n", self.text, heading)
            positions.append(self.text.index("\n" + heading + "\n"))
        self.assertEqual(positions, sorted(positions))
        level2 = [line for line in lines if line.startswith("## ")]
        self.assertEqual(level2[-1], "## 9. Verification records")
        for sub in ("### 7.1 Proved", "### 7.2 Computed", "### 7.3 Assumed", "### 7.4 Open"):
            self.assertIn("\n" + sub, self.text, sub)

    def test_key_statements(self):
        for statement in KEY_STATEMENTS:
            self.assertIn(statement, self.text, statement)

    def test_no_material_of_the_earlier_stages(self):
        for marker in ("artifacts/", "provenance/", "studies/", "dirac-main", "vendor/", "Gmail"):
            self.assertNotIn(marker, self.text, marker)

    def test_cited_checks_exist_and_pass(self):
        py = report_names(PY_REPORT)
        wl = report_names(WL_REPORT)
        names = set(re.findall(r"`([a-z][a-z0-9_]+)`", self.text))
        cited = {n for n in names if n in py or n in wl}
        # every check of both reports is cited, and every cited check passes
        self.assertEqual(set(py) | set(wl), cited)
        for name in cited:
            for verdicts in (py, wl):
                if name in verdicts:
                    self.assertEqual(verdicts[name], "PASS", name)
        # a name that looks like a check but is not one of the reports must be a known record key
        allowed = {"history_source", "fiber_lovelock_tensors", "fiber_lovelock_scalars",
                   "commuting_T_x4x0_homogeneous", "spin_connection_in_the_energy_momentum_tensor",
                   "condensate_cannot_source_branch"}
        for name in names - cited:
            if "_" in name and not name.endswith((".py", ".json", ".wls")):
                self.assertIn(name, allowed, name)

    def test_counts(self):
        for path, label in ((PY_REPORT, "16 of 16 PASS"), (WL_REPORT, "11 of 11 PASS")):
            checks = load_json(path)["checks"]
            n = len(checks)
            self.assertTrue(all(c["verdict"] == "PASS" for c in checks))
            self.assertEqual(label, f"{n} of {n} PASS")
            self.assertIn(f"| `{path.relative_to(ROOT).as_posix()}` | {label} |", self.text)

    def test_negative_control_counts(self):
        n = len(load_json(PY_REPORT)["checks"])
        self.assertNotIn(f"{n + 1} of {n + 1} PASS", self.text)


class Values(unittest.TestCase):
    def setUp(self):
        self.text = markdown_text()
        self.res = load_json(RESULTS)

    def test_metric(self):
        g = self.res["metric_warped"]
        self.assertEqual(g[4], "-sin(6*H*x0)**(1/3)")
        self.assertEqual(self.res["metric_of_2026_10_14"][4], "-1")
        self.assertEqual(g[:4] + g[5:], self.res["metric_of_2026_10_14"][:4] + self.res["metric_of_2026_10_14"][5:])
        self.assertEqual(self.res["sqrt_det_g"], "b4^(3/2) Cos[6 H x0] Sin[6 H x0]^(1/6)")
        self.assertIn(r"$\sqrt{|g|} = b_4^{3/2}\cos z\,\sin^{1/6}z$", self.text)

    def test_layer_coefficients(self):
        c = self.res["layer_coefficients_c_kj"]
        self.assertEqual(c, {"10": 21, "11": 1, "20": -420, "21": -40, "22": 1, "30": 2520, "31": 360, "32": -18,
                             "33": 1})
        self.assertIn("$c_{10} = 21$, $c_{11} = 1$; $c_{20} = -420$, $c_{21} = -40$, $c_{22} = 1$; $c_{30} = 2520$, "
                      "$c_{31} = 360$, $c_{32} = -18$, $c_{33} = 1$", self.text)

    def test_effective_couplings(self):
        b = self.res["effective_couplings_author_weights"]
        self.assertEqual(b, {"beta0": "Lam + 161/16", "beta1": "1/(16*H**2)", "beta2": "1/(64*H**4)",
                             "beta3": "1/(1152*H**6)"})
        self.assertIn("$\\beta_0 = 161/16 + \\Lambda$", self.text)
        self.assertIn("$\\beta_1 = 1/(16H^2)$, $\\beta_2 = 1/(64H^4)$, $\\beta_3 = 1/(1152H^6)$", self.text)

    def test_kasner(self):
        k = self.res["einstein_vacuum_kasner"]
        self.assertEqual(k["Lambda"], "-21 H^2")
        self.assertEqual(k["solutions"][0]["b4"], "x4^(2/3)")
        self.assertEqual(k["solutions"][0]["space_scale"], "x4^(1/6 + sqrt(5)/6)")
        self.assertEqual(k["solutions"][0]["extra_time_scale"], "x4^(1/6 - sqrt(5)/6)")
        self.assertIn("p_s = \\frac{1 + \\sqrt5}{6}", self.text)

    def test_history_source(self):
        h = self.res["history_source"]
        self.assertEqual(h["einstein_A1_beta43"], {"-rho": "-H**2*W/3 + 21*H**2", "p0": "-11*H**2*W/3 + 21*H**2",
                                                    "p3": "-5*H**2*W/3 + 21*H**2", "p_t": "-13*H**2*W/3 + 21*H**2"})
        self.assertEqual(h["author_weights_A1_beta43"]["-rho"], "5*W**3/432 + W**2/48 - W/48 + 161/16")
        self.assertEqual(h["author_weights_A1_beta43"]["p3"], "W**3/432 + 17*W**2/432 - 5*W/48 + 161/16")
        self.assertEqual(h["author_weights_A1_beta43"]["p_t"], "-7*W**3/432 + 11*W**2/144 - 13*W/48 + 161/16")
        self.assertEqual(h["author_weights_A1_beta43"]["p0"], "-13*W**3/432 + 53*W**2/432 - 11*W/48 + 161/16")
        for row in ("| $\\mu = x_4$: $-\\kappa\\rho - \\Lambda$ | $21H^2 - \\frac13 H^2 W$ | $\\frac{161}{16} - "
                    "\\frac{W}{48} + \\frac{W^2}{48} + \\frac{5W^3}{432}$ |",
                    "| $\\mu = x_0$: $\\kappa p_0 - \\Lambda$ | $21H^2 - \\frac{11}{3}H^2 W$ | $\\frac{161}{16} - "
                    "\\frac{11W}{48} + \\frac{53W^2}{432} - \\frac{13W^3}{432}$ |"):
            self.assertIn(row, self.text)

    def test_dirac_gravity_term(self):
        self.assertEqual(self.res["dirac_gravity_term"],
                         "(7/2) H gamma^(x0) + (3/4) (b4'/b4) Sin[6 H x0]^(-1/6) gamma^(x4)")


if __name__ == "__main__":
    unittest.main()
