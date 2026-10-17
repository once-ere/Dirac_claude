

def emit() -> None:
    for name, block in generated_blocks().items():
        print(f"% {name}")
        print(block)


# ---------------------------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------------------------

def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def report_checks(key: str) -> dict[str, str]:
    data = load(REPORTS[key])
    return {item["name"]: str(item["verdict"]).upper() for item in data["checks"]}


def report_count(key: str) -> tuple[int, int]:
    """(passed, total) of a report, read from its own summary fields."""
    data = load(REPORTS[key])
    if key in ("algebra-wolfram", "theory-wolfram", "pairing-wolfram", "scope-wolfram", "t3-wolfram", "t3c-wolfram"):
        return data["summary"]["passed"], data["summary"]["total"]
    if key == "lead-u1":
        return data["summary"]["passed"], data["summary"]["total"]
    if key in ("algebra-python", "theory-python", "scope-python", "ks-source", "ks-source-a4", "ks-crosscheck",
               "fock-quartic"):
        return data["summary"]["pass"], data["summary"]["checks"]
    if key == "a4-wolfram":
        return data["checkCount"] - data["failedCount"], data["checkCount"]
    if key == "a4-python":
        return data["passCount"], data["checkCount"]
    if key in ("pairing-python", "t3-python", "t3c-python"):
        counts = data["counts"]
        return counts["pass"], counts["pass"] + counts["fail"] + counts["pending"]
    if key.startswith("ds-"):
        return data["summary"]["pass"], data["summary"]["total"]
    raise KeyError(key)


QUOTED_COUNTS = {
    "algebra-wolfram": "Wolfram: {p} of {t} checks pass",
    "algebra-python": "sympy: {p} of {t} checks pass",
    "theory-wolfram": "Wolfram: {p} of {t} checks pass",
    "theory-python": "sympy: {p} of {t} checks pass",
    "a4-wolfram": "Wolfram: {p} of {t} checks pass",
    "a4-python": "sympy: {p} of {t} checks pass",
    "pairing-wolfram": "Wolfram: {p} of {t} checks pass",
    "pairing-python": "sympy: {p} of {t} checks pass",
    "scope-wolfram": "Wolfram: {p} of {t} checks pass",
    "scope-python": "sympy: {p} of {t} checks pass",
    "t3-wolfram": "Wolfram: {p} of {t} checks pass",
    "t3-python": "sympy: {p} of {t} checks pass",
    "ks-source": "Python: {p} of {t} checks pass",
    "ks-source-a4": "Python: {p} of {t} checks pass",
    "t3c-wolfram": "Wolfram: {p} of {t} checks pass",
    "t3c-python": "sympy: {p} of {t} checks pass",
    "ks-crosscheck": "`Revision/kohn_sham/reports/ks-crosscheck.json`: {p} of {t} checks pass",
    "ds-derivation": "derivation: {p} of {t} checks pass",
    "ds-ks-history": "Kohn-Sham history: {p} of {t} checks pass",
    "ds-eos": "equation of state: {p} of {t} checks pass",
    "ds-independent": "independent: {p} of {t} checks pass",
    "fock-quartic": "no Wolfram counterpart): {p} of {t} checks pass",
    "lead-u1": "lead checks: {p} of {t} checks pass",
}


def markdown_text() -> str:
    return MARKDOWN.read_text(encoding="utf-8")


def code_spans_outside_fences(text: str) -> list[str]:
    spans = []
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        spans.extend(re.findall(r"`([^`\n]+)`", line))
    return spans


def is_path_or_command(span: str) -> bool:
    return ("/" in span or " " in span or "\\" in span
            or re.search(r"\.(json|md|py|wls|wl|tex|pdf|csv|rs|toml|nb)$", span) is not None)


def wl_to_sympy(text: str) -> sp.Expr:
    """Parse a Wolfram InputForm expression of field-theory.json (no field symbols)."""
    t = _wl_metric_symbols(text)
    for name in ("Sin", "Cos", "Tan", "Cot", "Sec", "Csc", "Abs"):
        t = t.replace(name + "[", name.lower() + "(")
    t = t.replace("[", "(").replace("]", ")").replace("^", "**")
    local = {"E": sp.E, "a4": _a4, "z": _z, "H": _H, "A1": _A1, "A2": _A2, "b4": _b4, "B1": _B1,
             "B2": _B2, "sqrt": sp.sqrt, "sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "cot": sp.cot,
             "sec": sp.sec, "csc": sp.csc, "abs": sp.Abs, "rftSig": sp.sign(sp.cot(_z))}
    return sp.sympify(t, locals=local)


# Exact test points in four quarters of z (every real z; no sign of sin z or cos z is assumed).
TEST_POINTS = [
    {_a4: sp.Rational(3, 7), _z: sp.Rational(5, 9), _H: sp.Rational(2, 3), _A1: sp.Rational(-4, 5),
     _A2: sp.Rational(7, 11), _b4: sp.Rational(5, 3), _B1: sp.Rational(-2, 7), _B2: sp.Rational(3, 5)},
    {_a4: sp.Rational(-1, 3), _z: sp.Rational(11, 5), _H: sp.Rational(3, 2), _A1: sp.Rational(5, 4),
     _A2: sp.Rational(-2, 9), _b4: sp.Rational(7, 2), _B1: sp.Rational(9, 4), _B2: sp.Rational(-1, 6)},
    {_a4: sp.Rational(1, 2), _z: sp.Rational(-13, 4), _H: sp.Rational(1, 3), _A1: sp.Rational(2, 3),
     _A2: sp.Rational(1, 8), _b4: sp.Rational(2, 9), _B1: sp.Rational(-5, 3), _B2: sp.Rational(4, 7)},
    {_a4: sp.Rational(-2, 5), _z: sp.Rational(-7, 5), _H: sp.Rational(5, 4), _A1: sp.Rational(-1, 6),
     _A2: sp.Rational(3, 4), _b4: sp.Rational(11, 6), _B1: sp.Rational(1, 9), _B2: sp.Rational(-7, 8)},
]


def is_zero(expr: sp.Expr) -> bool:
    """Exact simplification first, then a 50-digit check at the four test points (a nonzero
    expression is detected at a generic point; the points lie in four different quarters of z)."""
    expr = sp.sympify(expr)
    if sp.simplify(expr) == 0:
        return True
    return all(abs(sp.N(expr.subs(point), 50)) < sp.Float("1e-40") for point in TEST_POINTS)


# ---------------------------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------------------------

class DocumentFilesTest(unittest.TestCase):
    def test_markdown_is_lf_only_utf8(self):
        data = MARKDOWN.read_bytes()
        self.assertNotIn(b"\r", data)
        data.decode("utf-8")
        self.assertTrue(data.endswith(b"\n"))

    def test_title_subtitle_and_sections(self):
        lines = markdown_text().splitlines()
        self.assertEqual(lines[0], "# " + TITLE)
        self.assertIn("## " + SUBTITLE, lines)
        headings = [line[3:] for line in lines if line.startswith("## ")][1:]
        self.assertEqual(headings, SECTIONS)

    def test_tex_is_the_builder_output_of_the_markdown(self):
        latex = builder.convert(
            markdown_text(),
            strip_heading_numbers=True,
            developer_layout=True,
            author=builder.DEFAULT_AUTHOR,
            date=builder.DEFAULT_DATE,
            image_root=ROOT,
        )
        self.assertEqual(TEX.read_bytes(), latex.encode("utf-8"))

    def test_registered_edition_matches_the_pdf_file(self):
        registry = load(REGISTRY)
        self.assertIn(EDITION, registry)
        entry = registry[EDITION]
        pdf_bytes = PDF.read_bytes()
        self.assertEqual(entry["path"], PDF_RELATIVE)
        self.assertEqual(entry["sha256"], hashlib.sha256(pdf_bytes).hexdigest())
        self.assertEqual(entry["pages"], len(check_dissertation_pdf.PAGE_PATTERN.findall(pdf_bytes)))
        self.assertTrue(pdf_bytes.startswith(b"%PDF-"))
        self.assertTrue(pdf_bytes.rstrip().endswith(b"%%EOF"))
        self.assertEqual(check_dissertation_pdf.parse_media_boxes(pdf_bytes), [(0.0, 0.0, 612.0, 792.0)])

    def test_required_phrases_present_and_no_placeholders(self):
        text = markdown_text()
        for phrase in REQUIRED_PHRASES:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)
        for placeholder in PLACEHOLDERS:
            with self.subTest(placeholder=placeholder):
                self.assertNotIn(placeholder, text)
        for phrase in STALE_PHRASES:
            with self.subTest(stale=phrase):
                self.assertNotIn(phrase, text)

    def test_no_old_stage_paths_are_cited(self):
        text = markdown_text()
        for old in ("artifacts/", "provenance/", "studies/", "notebooks/", "dirac-main", "vendor/"):
            with self.subTest(old=old):
                self.assertNotIn(old, text)


class CitedChecksTest(unittest.TestCase):
    def test_every_cited_check_exists_and_passes(self):
        verdicts: dict[str, set[str]] = {}
        for key in REPORTS:
            for name, verdict in report_checks(key).items():
                verdicts.setdefault(name, set()).add(verdict)
        cited = set()
        for span in code_spans_outside_fences(markdown_text()):
            if is_path_or_command(span) or span in NON_CHECK_SPANS:
                continue
            cited.add(span)
            with self.subTest(check=span):
                self.assertTrue(span in verdicts, f"cited check {span!r} is in no report")
                self.assertEqual(verdicts.get(span), {"PASS"})
        for name in ESSENTIAL_CHECKS:
            with self.subTest(essential=name):
                self.assertIn(name, cited)

    def test_quoted_counts_match_the_reports(self):
        text = markdown_text()
        for key, pattern in QUOTED_COUNTS.items():
            passed, total = report_count(key)
            with self.subTest(report=key):
                self.assertEqual(passed, total, f"{key}: not every check passes")
                self.assertIn(pattern.format(p=passed, t=total), text)

    def test_quoted_numbers_of_the_second_wave(self):
        text = markdown_text()
        self.assertGreater(len(QUOTED_NUMBERS), 3)
        for key, in_report, in_document in QUOTED_NUMBERS:
            with self.subTest(report=key, number=in_report):
                self.assertIn(in_report, REPORTS[key].read_text(encoding="utf-8"))
                self.assertIn(in_document, text)

    def test_comparison_record_statement_matches_the_theory_reports(self):
        text = markdown_text()
        python_report = load(REPORTS["theory-python"])
        comparison = python_report["comparison_with_wolfram"]
        wolfram_names = list(report_checks("theory-wolfram"))
        referenced = set(comparison["checks"]["wolfram_checks_without_sympy_counterpart"])
        for record in comparison["checks"]["records"]:
            referenced |= set(record["wolfram_checks"])
        uncovered = [name for name in wolfram_names if name not in referenced]
        self.assertEqual(comparison["status"], "agree")
        self.assertEqual(comparison["formulas"]["not_compared"], [])
        self.assertEqual(comparison["formulas"]["agree"], comparison["formulas"]["compared"])
        self.assertEqual(comparison["checks"]["agree"], comparison["checks"]["pairs"])
        wolfram = load(REPORTS["theory-wolfram"])
        self.assertEqual(comparison["wolfram_summary"], wolfram["summary"])
        self.assertIn(f"a Wolfram run of {comparison['wolfram_summary']['total']} checks", text)
        self.assertIn(f"{comparison['formulas']['agree']} of {comparison['formulas']['compared']} formula records", text)
        self.assertIn(f"{comparison['checks']['agree']} of {comparison['checks']['pairs']} check pairs", text)
        self.assertEqual(uncovered, [])
        for name in comparison["checks"]["wolfram_checks_without_sympy_counterpart"]:
            self.assertIn(f"`{name}`", text)
        if not comparison["checks"]["wolfram_checks_without_sympy_counterpart"]:
            total = comparison["wolfram_summary"]["total"]
            self.assertIn(f"every one of the {total} Wolfram checks is paired with a sympy check", text)
            self.assertNotIn("paired with a sympy check except", text)


class GeneratedBlocksTest(unittest.TestCase):
    def test_generated_blocks_are_in_the_document(self):
        text = markdown_text()
        for name, block in generated_blocks().items():
            with self.subTest(block=name):
                self.assertIn("$$\n" + block + "\n$$", text)

    def test_renderer_detects_a_changed_coefficient(self):
        # negative control: a component with the extra-time factor of the withdrawn metric is refused
        formulas = {item["key"]: item["wl"] for item in load(FIELD_THEORY)["formulas"]}
        text = formulas["field_equation_components"][0].replace("(Sin[6*H*x0]^2)^(1/12)", "Sin[6*H*x0]^(1/6)", 1)
        expr, _ = _parse_component(text)
        derivative = [s for s in expr.free_symbols if s.name.startswith("D_5_") or s.name.startswith("D_6_")
                      or s.name.startswith("D_7_")]
        with self.assertRaises(ValueError):
            for symbol in derivative:
                _sign(expr.coeff(symbol) * (sp.sin(_z) ** 2) ** sp.Rational(1, 12) / sp.sin(_z) ** sp.Rational(1, 6)
                      * sp.Rational(3, 2), EPS_T)

    def test_component_equations_agree_with_the_sympy_report(self):
        sympy_components = load(REPORTS["theory-python"])["formulas"]["dirac_equation_components"]["components"]
        lam, m, x4, x0 = sp.symbols("lam m x4 x0")
        a4f, b4f = sp.Function("a4"), sp.Function("b4")
        for number, wolfram in enumerate(wolfram_component_lhs(), 1):
            text = sympy_components[f"E{number}"]
            t = re.sub(r"psi(\d+)_x(\d)", r"D_\2_\1", text)
            t = re.sub(r"psi(\d+)", r"P_\1", t)
            t = re.sub(r"chi(\d+)", r"C_\1", t)
            t = t.replace("lambda", "lam")
            expr = sp.sympify(t, locals={"lam": lam, "m": m, "H": _H, "x4": x4, "x0": x0, "a4": a4f, "b4": b4f,
                                          "exp": sp.exp, "sin": sp.sin, "cos": sp.cos, "sqrt": sp.sqrt,
                                          "Abs": sp.Abs, "Derivative": sp.Derivative})
            expr = expr.subs(sp.Derivative(b4f(x4), x4), _B1).subs(sp.Derivative(a4f(x4), x4), _A1)
            expr = expr.subs({a4f(x4): _a4, b4f(x4): _b4}).subs(x0, _z / (6 * _H))
            mass = sp.expand(expr).coeff(m)
            linear = sp.expand(expr).subs({lam: 0, m: 0})
            with self.subTest(component=number):
                self.assertEqual(mass, -sp.Symbol(f"P_{number}"))
                self.assertIn(_B1, linear.free_symbols)  # the v_g term is part of every component
                symbols = sorted((linear.free_symbols | wolfram.free_symbols) - {_a4, _z, _H, _b4, _A1, _B1},
                                 key=lambda s: s.name)
                for symbol in symbols:
                    self.assertTrue(is_zero(linear.coeff(symbol) - wolfram.coeff(symbol)), (number, symbol))

    def test_connection_and_curvature_formulas_match_the_formula_file(self):
        """The hand-written formulas of sections 2 and 4 (corrected metric, u = b4'/b4, v = u')."""
        text = markdown_text()
        for formula in DOCUMENT_FORMULAS:
            with self.subTest(formula=formula):
                self.assertIn(formula, text)
        formulas = {item["key"]: item["wl"] for item in load(FIELD_THEORY)["formulas"]}
        e = sp.exp(_a4)
        sb = sp.sqrt(_b4) / e                    # e^{-a4} b4^{1/2}
        w = (sp.sin(_z) ** 2) ** sp.Rational(1, 12)
        u = _B1 / _b4
        h4 = u / 2 - _A1                         # the rate of the block (x0, x5, x6, x7)
        kk = sp.exp(2 * _a4) / _b4
        # vielbein and sqrt|g| (list position k + 1 holds x_k)
        f = re.findall(r"[^{},]+(?:\[[^\]]*\][^{},]*)*", formulas["vielbein_diagonal"])
        expected_f = [sb * sp.cot(_z)] + [e] * 3 + [1] + [sb * w] * 3
        self.assertEqual(len(f), 8)
        for got, want in zip(f, expected_f):
            self.assertTrue(is_zero(wl_to_sympy(got) - want), got)
        sqrt_g = wl_to_sympy(formulas["sqrt_det_g"])
        self.assertTrue(is_zero(sqrt_g - sp.exp(-_a4) * _b4**2 * sp.Abs(sp.cot(_z)) * (sp.sin(_z) ** 2) ** sp.Rational(1, 4)))
        # Christoffel symbols: 21 nonzero
        entries = re.findall(r"\{(\d), (\d), (\d), ([^{}]+)\}", formulas["christoffel_nonzero"])
        P = {k: k + 1 for k in range(8)}
        s3 = (sp.sin(_z) ** 2) ** sp.Rational(1, 6)
        expected = {(P[0], P[0], P[0]): -12 * _H * sp.csc(2 * _z), (P[0], P[0], P[4]): h4,
                    (P[4], P[0], P[0]): sp.exp(-2 * _a4) * _b4 * sp.cot(_z) ** 2 * h4}
        for i in (1, 2, 3):
            expected[(P[i], P[i], P[4])] = _A1
            expected[(P[4], P[i], P[i])] = sp.exp(2 * _a4) * _A1
        for t in (5, 6, 7):
            expected[(P[0], P[t], P[t])] = _H * s3 * sp.tan(_z)
            expected[(P[4], P[t], P[t])] = -sp.exp(-2 * _a4) * _b4 * s3 * h4
            expected[(P[t], P[0], P[t])] = _H * sp.cot(_z)
            expected[(P[t], P[4], P[t])] = h4
        got = {(int(a), int(b), int(c)): wl_to_sympy(v_) for a, b, c, v_ in entries}
        self.assertEqual(len(got), 21)
        self.assertEqual(set(got), set(expected))
        for key, value in got.items():
            with self.subTest(christoffel=key):
                self.assertTrue(is_zero(value - expected[key]))
        # Ricci tensor (diagonal) and scalar, with b4''/b4 = B2/b4
        entries = re.findall(r"\{(\d), (\d), ([^{}]+)\}", formulas["ricci_mixed_nonzero"])
        hidden = -3 * _H**2 * kk + _A1**2 - _A2 - sp.Rational(5, 2) * _A1 * u + _B2 / (2 * _b4) + u**2 / 2
        expected = {(P[0], P[0]): hidden, (P[4], P[4]): 7 * _A1**2 - _A2 - 4 * _A1 * u + 2 * _B2 / _b4 - u**2}
        for i in (1, 2, 3):
            expected[(P[i], P[i])] = -_A1**2 + _A2 + 2 * _A1 * u
        for t in (5, 6, 7):
            expected[(P[t], P[t])] = hidden
        got = {(int(a), int(b)): wl_to_sympy(v_) for a, b, v_ in entries}
        self.assertEqual(set(got), set(expected))
        for key, value in got.items():
            with self.subTest(ricci=key):
                self.assertTrue(is_zero(value - expected[key]))
        self.assertTrue(is_zero(wl_to_sympy(formulas["ricci_scalar"])
                                - (-12 * _H**2 * kk + 8 * _A1**2 - 2 * _A2 - 8 * _A1 * u + 4 * _B2 / _b4 + u**2)))
        # spin connection: 10 nonzero omega_mu,ab (a < b)
        entries = re.findall(r"\{(\d), (\d), (\d), ([^{}]+)\}", formulas["omega_nonzero"])
        expected = {(P[0], P[0], P[4]): h4 * sb * sp.cot(_z)}
        for i in (1, 2, 3):
            expected[(P[i], P[i], P[4])] = _A1 * e
        for t in (5, 6, 7):
            expected[(P[t], P[4], P[t])] = h4 * sb * w
            expected[(P[t], P[0], P[t])] = _H * w
        got = {(int(a), int(b), int(c)): wl_to_sympy(v_) for a, b, c, v_ in entries}
        self.assertEqual(len(got), 10)
        self.assertEqual(set(got), set(expected))
        for key, value in got.items():
            with self.subTest(omega=key):
                self.assertTrue(is_zero(value - expected[key]))
        # gamma^mu Omega_mu per direction: coefficients of gamma^(x4) and gamma^(x0)
        entries = re.findall(r"\{(\d), ([^{},]+), ([^{},]+)\}", formulas["gammaOmega_per_direction"])
        extra = (h4 / 2, _H * e / (2 * sp.sqrt(_b4)))
        want = {P[0]: (h4 / 2, 0), P[1]: (_A1 / 2, 0), P[2]: (_A1 / 2, 0), P[3]: (_A1 / 2, 0),
                P[4]: (0, 0), P[5]: extra, P[6]: extra, P[7]: extra}
        self.assertEqual(len(entries), 8)
        for mu, c4, c0 in entries:
            with self.subTest(direction=mu):
                self.assertTrue(is_zero(wl_to_sympy(c4) - want[int(mu)][0]))
                self.assertTrue(is_zero(wl_to_sympy(c0) - want[int(mu)][1]))
        total = formulas["gammaOmega_total"].replace('gamma["x0"]', "G0").replace('gamma["x4"]', "G4")
        g0, g4 = sp.symbols("G0 G4")
        total = sp.sympify(_wl_metric_symbols(total).replace("^", "**"),
                           locals={"G0": g0, "G4": g4, "H": _H, "b4": _b4, "B1": _B1, "A1": _A1, "a4": _a4,
                                   "E": sp.E, "sqrt": sp.sqrt})
        self.assertEqual(sp.simplify(total - (C_G * g0 + V_G * g4)), 0)


class FieldEquationFormulasTest(unittest.TestCase):
    """The rendered components of section 13 add up to the general formulas of a4-equations.json."""

    def setUp(self):
        self.data = load(A4_EQUATIONS)

    def general(self, key: str) -> sp.Expr:
        return _wl_poly(self.data["generalSource"][key]["input"].split("==")[0])

    def test_diagonal_equations_are_the_sums_of_the_rendered_components(self):
        for key, label in (("constraint_x4", "x4x4"), ("space_x1_eq_x2_eq_x3", "x1x1"),
                           ("hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7", "x0x0")):
            rendered = sum(a * lovelock_component(k, label) for k, a in zip((1, 2, 3), _alphas)) + _lam
            with self.subTest(component=key):
                self.assertEqual(sp.expand(rendered - self.general(key)), 0)

    def test_hidden_component_equals_the_extra_time_component(self):
        for k in (1, 2, 3):
            with self.subTest(order=k):
                self.assertEqual(sp.expand(lovelock_component(k, "x0x0") - lovelock_component(k, "x5x5")), 0)
        self.assertIn("p0 = p_t", self.data["generalSource"]["hiddenEqualsExtraTimes"])
        self.assertIn("T^x4_x0 = T^x0_x4 = 0", self.data["generalSource"]["offDiagonal"])

    def test_einstein_is_the_first_order_of_the_general_equations(self):
        einstein = self.data["einstein"]
        for key, label in (("constraint_x4", "x4x4"), ("space_x1", "x1x1"), ("hidden_x0", "x0x0")):
            lhs = _wl_poly(einstein[key]["input"].split("==")[0])
            with self.subTest(component=key):
                self.assertEqual(sp.expand(lhs - lovelock_component(1, label) - _lam), 0)

    def test_background_history_with_the_author_weights(self):
        history = self.data["exponentialHistory"]
        source = history["requiredSource"]
        point = {_AA: 1, _be: sp.Rational(4, 3), _H: 1, _lam: -10, **AUTHOR_WEIGHTS}
        hs = history["authorWeights"]["historySource_kappaT_minus_Lam"]
        expected = {"rho": -_wl_poly(hs["minus_rho"]["input"]) - _lam, "p3": _wl_poly(hs["p3"]["input"]) + _lam,
                    "p0": _wl_poly(hs["p0"]["input"]) + _lam, "pt": _wl_poly(hs["pt"]["input"]) + _lam}
        for key, value in expected.items():
            expr = sp.sympify(source[key]["input"].replace("^", "**"), locals=_A4_LOCALS) * _kappa
            with self.subTest(entry=key):
                self.assertEqual(sp.simplify(expr.subs(point) - value.subs(_lam, -10)), 0)
                # the required source of an exponential history, written in k, is even in A
                self.assertEqual(sp.simplify(expr - expr.subs(_AA, -_AA)), 0)
        anisotropy = sp.expand(_wl_poly(hs["p3"]["input"]) - _wl_poly(hs["p0"]["input"]))
        self.assertEqual(anisotropy, sp.expand(-sp.Rational(9, 16) * _kk**2 + sp.Rational(1069, 432) * _kk
                                               + sp.Rational(2015, 972)))


@unittest.skipUnless(os.environ.get("REVISION_PDF_REBUILD") == "1", "set REVISION_PDF_REBUILD=1 to rebuild the PDF in verify mode")
class PdfRebuildTest(unittest.TestCase):
    def test_verify_mode_reproduces_the_registered_edition(self):
        completed = subprocess.run(
            [sys.executable, "scripts/build_provenance_pdf.py", f"Revision/docs/{STEM}.md",
             "--developer-layout", "--specifications", "Revision/pdf-specifications.json"],
            cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False, timeout=1800,
        )
        output = completed.stdout.decode("utf-8", "replace")
        self.assertEqual(completed.returncode, 0, output[-4000:])
        self.assertIn("provenance_pdf=OK", output)
        self.assertIn("measurement_warningLineCount=0", output)


if __name__ == "__main__":
    if "--emit" in sys.argv:
        emit()
        raise SystemExit(0)
    unittest.main()
