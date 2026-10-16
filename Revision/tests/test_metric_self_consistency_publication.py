#!/usr/bin/env python3
"""Publication test for Revision/docs/METRIC_SELF_CONSISTENCY.{md,tex,pdf}.

The document answers the user's order of 2026-10-16: the issue (a diagonal metric is self-consistent only if every
off-diagonal component of the sources vanishes), why the metric of 2026-10-14 is not self-consistent with diagonal
sources, the remedy (version 2 of 2026-10-16: the corrected metric
diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3)), z = 6 H x0 real; the time-warped
metric of version 1, g44 = -Sin[z]^(1/3), is withdrawn because its lapse oscillates), its field equations and what it
changes for the fields.  It is built and registered with

    python scripts/build_provenance_pdf.py Revision/docs/METRIC_SELF_CONSISTENCY.md \
        --developer-layout --specifications Revision/pdf-specifications.json [--register]

Run from the repository root:
    python -m unittest Revision/tests/test_metric_self_consistency_publication.py -v

What is tested
  * the committed .tex is exactly the builder's output for the committed .md, both files are UTF-8 with LF line
    endings, and their sha256 are pinned;
  * the PDF is registered in Revision/pdf-specifications.json (edition metric-self-consistency) and is structurally
    sound;
  * title, sections and the last section; the key statements (x0 space-like, x4 the time, z real, the positive
    branch of (Sin^2)^(1/6), version 1 withdrawn); the wording of version 1 that the author flagged is absent; z is
    defined before section 2 and y before its first use; the author's notebook is described as read only;
  * every check name the document cites exists in the two reports of Revision/metric_warped with the verdict PASS,
    every check of the two reports is listed, and the counts quoted are the reports' counts;
  * the formulas quoted (the corrected metric, the volume factor, the mixed curvature of the family, the Einstein
    tensor, the history's source, the gravity term of the Dirac operator) equal the values of
    Revision/metric_warped/results/warped-metric.json;
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

MARKDOWN_SHA256 = "f822b44cfc635700c272e02b008cf8110cbaa23f3310195a5018e4f238a9bcf3"
TEX_SHA256 = "e77eddc5a4284b8d10a4fa3ab7e47315bed776c5e7c37aa43704be61dbca0029"

MW = REVISION / "metric_warped"
PY_REPORT = MW / "reports" / "python-warped-metric-report.json"
WL_REPORT = MW / "reports" / "wolfram-warped-metric-report.json"
RESULTS = MW / "results" / "warped-metric.json"

TITLE = "The self-consistency of the primordial metric with diagonal sources"
SECTIONS = (
    "## Abstract",
    "## 1. The issue",
    "## 2. Where off-diagonal terms come from",
    "## 3. The remedy: the corrected metric",
    "## 4. The field equations of the corrected metric",
    "## 5. What the corrected metric changes for the fields",
    "## 6. Consequences for the Revision record",
    "## 7. What is proved, computed, assumed and open",
    "## 8. Reproduction",
    "## 9. Verification records",
)
KEY_STATEMENTS = (
    "none of its definitions or conventions is used in the Revision record",
    "- $x_0$ is the hidden direction, a hypothetical space-like coordinate;",
    "- $x_4$ is the time;",
    r"z = 6Hx_0,\qquad -\infty < z < \infty",
    r"The author's factor $\sin^{1/3}z$ means $(\sin^2 z)^{1/6} \ge 0$, the positive branch",
    r"No assumption on the sign of $\sin z$ or $\cos z$ is made.",
    "Version 1 is withdrawn. Every metric below keeps $g_{44} = -1$.",
    "No diagonal metric removes them",
    "The history remains a PRESCRIBED background: no field of the record is shown to be its source.",
    "At this commit that condition is OPEN for the corrected metric.",
    "The choice between the corrected metric (the hidden direction shrinks with the extra times) and alternative K "
    "(it expands with 3-space) is the author's.",
)
# the wording of version 1 that the author flagged on 2026-10-16 must not come back
WITHDRAWN_WORDING = (
    "the time direction, which may depend on $x_0$. The family",
    r"z = 6Hx_0 \in (0, \pi/2)",
    "This is the **warped metric** of 2026-10-16.",
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

    def test_withdrawn_wording_absent(self):
        for wording in WITHDRAWN_WORDING:
            self.assertNotIn(wording, self.text, wording)

    def test_z_and_y_defined_before_use(self):
        # z is defined in section 1.2, before the formulas in z of sections 2 and 3; y is defined in section 3.4,
        # before its first use after section 3.1 (which only names the fault of version 1)
        z_def = self.text.index(r"z = 6Hx_0,\qquad -\infty < z < \infty")
        self.assertLess(z_def, self.text.index("## 2. Where off-diagonal terms come from"))
        y_def = self.text.index(r"y = \frac{\ln|\sin z|}{6H} \le 0")
        start = self.text.index("### 3.2 ")
        first_y = min(self.text.index(marker, start) for marker in ("$y$", "dy^2"))
        self.assertLessEqual(y_def, first_y)
        self.assertEqual(self.text[:start].count("$y$"), 1)

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
        allowed = {"history_source", "einstein_diagonal", "ricci_scalar_mathematica",
                   "commuting_T_x4x0_homogeneous", "spin_connection_in_the_energy_momentum_tensor",
                   "condensate_cannot_source_branch"}
        for name in names - cited:
            if "_" in name and not name.endswith((".py", ".json", ".wls")):
                self.assertIn(name, allowed, name)

    def test_counts(self):
        for path, label in ((PY_REPORT, "14 of 14 PASS"), (WL_REPORT, "13 of 13 PASS")):
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
        self.assertEqual(
            self.res["metric_corrected"],
            "diag(E^(-2 a4[x4]) b4[x4] Cot[6 H x0]^2, E^(2 a4[x4]), E^(2 a4[x4]), E^(2 a4[x4]), -1, "
            "-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6), -E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6), "
            "-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6))")
        self.assertIn("real (-Infinity < z < Infinity)", self.res["coordinates"])
        self.assertIn("(Sin[6 H x0]^2)^(1/6) > 0", self.res["coordinates"])
        self.assertIn(r"ds^2 = {} & e^{-2a_4}\,b_4\cot^2 z\,dx_0^2 + e^{2a_4}\big(dx_1^2 + dx_2^2 + dx_3^2\big) - dx_4^2",
                      self.text)
        self.assertIn(r"& - e^{-2a_4}\,b_4\,(\sin^2 z)^{1/6}\big(dx_5^2 + dx_6^2 + dx_7^2\big) .", self.text)
        self.assertEqual(self.res["sqrt_det_g_corrected"], "E^(-a4) b4^2 |Cot[6 H x0]| (Sin[6 H x0]^2)^(1/4)")
        self.assertIn(r"$\sqrt{|g|} = e^{-a_4}b_4^2\,|\cot z|\,(\sin^2 z)^{1/4}$", self.text)

    def test_family(self):
        fam = self.res["family_mixed_curvature"]
        self.assertEqual(fam["space"], "alpha ((q - 1) a4' + p b4'/b4)")
        self.assertEqual(fam["extra_times"], "beta ((q + 1) a4' + (p - 1/2) b4'/b4)")
        self.assertIn(r"\alpha\big((q-1)a_4' + p\,u\big)", self.text)
        self.assertIn(r"\beta\big((q+1)a_4' + (p - \tfrac12)\,u\big)", self.text)

    def test_einstein_diagonal(self):
        e = self.res["einstein_diagonal"]
        self.assertEqual(e["x4"], "3*(4*EA**2*H**2*bb + 2*ad1**2*bb**2 - bd1**2)/(2*bb**2)")
        self.assertEqual(e["x0"], e["x5"])
        self.assertIn(r"E_{(1)}{}^{x_4}{}_{x_4} &= 6C + 3a_4'^2 - \tfrac32 u^2", self.text)

    def test_history_source(self):
        h = self.res["history_source"]
        self.assertEqual(h["einstein_A1_beta43"], {"-rho": "H**2*(18*exp(2*H*x4/3) + 1)/3",
                                                    "p0": "H**2*(9*exp(2*H*x4/3) - 11)/3",
                                                    "p3": "H**2*(54*exp(2*H*x4/3) - 13)/9",
                                                    "p_t": "H**2*(9*exp(2*H*x4/3) - 11)/3"})
        self.assertEqual(h["author_weights_A1_beta43"], {
            "-rho": "-9*exp(4*H*x4/3)/16 + 161*exp(2*H*x4/3)/24 + 121/432",
            "p0": "79*exp(2*H*x4/3)/16 - 497/144",
            "p3": "-9*exp(4*H*x4/3)/16 + 1601*exp(2*H*x4/3)/216 - 5359/3888",
            "p_t": "79*exp(2*H*x4/3)/16 - 497/144"})
        for row in (r"| $\mu = x_4$: $-\kappa\rho - \Lambda$ | $\frac13 H^2\big(18e^{2Hx_4/3} + 1\big)$ |",
                    r"| $\mu = x_1, x_2, x_3$: $\kappa p_3 - \Lambda$ | $\frac19 H^2\big(54e^{2Hx_4/3} - 13\big)$ |",
                    r"| $\mu = x_0$: $\kappa p_0 - \Lambda$ | $\frac13 H^2\big(9e^{2Hx_4/3} - 11\big)$ |",
                    r"-\kappa\rho - \Lambda &= -\tfrac{9}{16}e^{4Hx_4/3} + \tfrac{161}{24}e^{2Hx_4/3} + \tfrac{121}{432}",
                    r"\kappa p_3 - \Lambda &= -\tfrac{9}{16}e^{4Hx_4/3} + \tfrac{1601}{216}e^{2Hx_4/3} - \tfrac{5359}{3888}",
                    r"\kappa p_0 - \Lambda = \kappa p_t - \Lambda &= \tfrac{79}{16}e^{2Hx_4/3} - \tfrac{497}{144}"):
            self.assertIn(row, self.text)

    def test_dirac_gravity_term(self):
        self.assertEqual(self.res["dirac_gravity_term"],
                         "(3/2) H E^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4)")
        self.assertIn(r"\gamma^\mu\Omega_\mu = \frac32\,H\,e^{a_4}b_4^{-1/2}\,\gamma^{(x_0)}", self.text)


if __name__ == "__main__":
    unittest.main()
