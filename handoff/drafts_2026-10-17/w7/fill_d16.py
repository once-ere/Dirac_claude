"""Fill D16.draft.md and write Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md.

The generated blocks come from the renderers of the publication test (one source of truth); the sources table from
the report counts; the parts that need the W5/W6 records are read from the files d16_ks_source_13.md,
d16_dark_verdict_15.md and d16_index_ks_rows.md next to this script (with --provisional, placeholder text is used to
check the layout only; such a document is never committed).
"""
import importlib.util
import sys
from pathlib import Path

SP = Path(__file__).resolve().parent
ROOT = Path(r"D:\Developer\github\Dirac_claude")
REV = ROOT / "Revision"
spec = importlib.util.spec_from_file_location("t16", REV / "tests" / "test_dirac16complex_field_theory_publication.py")
T = importlib.util.module_from_spec(spec)
sys.path.insert(0, str(ROOT))
spec.loader.exec_module(T)

ROWS = (
    ("algebra (SPEC section 2)", ("algebra-wolfram", "algebra-python"),
     "`Revision/algebra/reports/wolfram-algebra.json`, `Revision/algebra/reports/python-algebra.json`"),
    ("field theory (SPEC sections 1, 3, 4, 6; the corrected metric)", ("theory-wolfram", "theory-python"),
     "`Revision/theory/field-theory.json`, `Revision/theory/reports/wolfram-field-theory.json`, `Revision/theory/reports/python-field-theory.json`"),
    ("field equations for $a_4$ and $b_4$ (SPEC section 5)", ("a4-wolfram", "a4-python"),
     "`Revision/field_equations_a4/a4-equations.json`, `Revision/field_equations_a4/reports/wolfram-a4-report.json`, `Revision/field_equations_a4/reports/python-a4-report.json`"),
    ("pairing (SPEC section 9)", ("pairing-wolfram", "pairing-python"),
     "`Revision/pairing/pairing-theory.json`, `Revision/pairing/reports/wolfram-pairing.json`, `Revision/pairing/reports/python-pairing.json`"),
    ("scope of the statements (frame dependence, boundary terms, growth, sign of the energy)", ("scope-wolfram", "scope-python"),
     "`Revision/theory/reports/wolfram-scope.json`, `Revision/theory/reports/python-scope.json`"),
    ("Kohn-Sham pairing T3 (SPEC section 9)", ("t3-wolfram", "t3-python"),
     "`Revision/pairing/kohn_sham/t3-theory.json`, `Revision/pairing/kohn_sham/reports/wolfram-t3.json`, `Revision/pairing/kohn_sham/reports/python-t3.json`"),
    ("the Kohn-Sham states as a source of the $a_4$ and $b_4$ equations", ("ks-source",),
     "`Revision/field_equations_a4/reports/ks-source-conditions.json`"),
    ("the $a_4$ and $b_4$ equations with the Kohn-Sham source", ("ks-source-a4",),
     "`Revision/field_equations_a4/ks_source/reports/ks-source-a4.json`"),
    ("completion of T3 (2026-10-08)", ("t3c-wolfram", "t3c-python"),
     "`Revision/pairing/kohn_sham/t3-completion.json`, `Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json`, `Revision/pairing/kohn_sham/reports/python-t3-completion.json`"),
    ("the energy-momentum tensor operator for $\\lambda \\neq 0$ in a finite Fock model (SPEC sections 4, 6; 2026-10-08)", ("fock-quartic",),
     "`Revision/theory/fock_quartic/reports/fock-quartic.json`"),
    ("the lead's checks of the charge and the U(1) current", ("lead-u1",),
     "`Revision/lead_checks/reports/charge-conjugation-and-u1.json`"),
    ("dark sector, Hypothesis (SPEC section 8)", ("ds-derivation", "ds-ks-history", "ds-eos", "ds-independent"),
     "`Revision/dark_sector/dirac16complex/reports/derivation-checks.json`, `Revision/dark_sector/dirac16complex/reports/ks-history-run.json`, `Revision/dark_sector/dirac16complex/reports/eos-checks.json`, `Revision/dark_sector/dirac16complex/reports/independent-checks.json`"),
)
PREFIX = {"fock-quartic": "Python (sympy and its own exact engine for the anticommutation relations; "}


def sources_table():
    lines = ["| part | files | checks |", "| --- | --- | --- |"]
    for part, keys, files in ROWS:
        cells = []
        for key in keys:
            p, t = T.report_count(key)
            assert p == t, key
            cells.append(PREFIX.get(key, "") + T.QUOTED_COUNTS[key].format(p=p, t=t))
        lines.append(f"| {part} | {files} | {'; '.join(cells)} |")
    return "\n".join(lines)


def main():
    provisional = "--provisional" in sys.argv
    text = (SP / "D16.draft.md").read_text(encoding="utf-8")
    blocks = T.generated_blocks()
    lovelock = "\n\n".join("$$\n" + blocks[f"lovelock_E{k}_{c}"] + "\n$$" for k in (1, 2, 3) for c in ("x0x0", "x1x1", "x4x4"))
    p, t = T.report_count("ks-crosscheck")
    fills = {
        "@@SOURCES_TABLE@@": sources_table(),
        "@@KS_CROSSCHECK@@": T.QUOTED_COUNTS["ks-crosscheck"].format(p=p, t=t),
        "@@COMPONENTS_1@@": blocks["components_1"],
        "@@COMPONENTS_2@@": blocks["components_2"],
        "@@LOVELOCK_BLOCKS@@": lovelock,
        "@@EINSTEIN_BLOCK@@": blocks["einstein"],
        "@@HISTORY_BLOCK@@": blocks["history"],
    }
    for name, key in (("d16_ks_source_13.md", "@@KS_SOURCE_13@@"), ("d16_dark_verdict_15.md", "@@DARK_VERDICT_15@@"),
                      ("d16_index_ks_rows.md", "@@INDEX_KS_ROWS@@")):
        part = SP / name
        if part.exists():
            fills[key] = part.read_text(encoding="utf-8").strip("\n")
        elif provisional:
            fills[key] = {"@@KS_SOURCE_13@@": "Provisional paragraph for the layout test only.",
                          "@@DARK_VERDICT_15@@": "- Provisional item for the layout test only.",
                          "@@INDEX_KS_ROWS@@": "| provisional | 13 | | |"}[key]
        else:
            sys.exit(f"missing {name}")
    for key, value in fills.items():
        assert text.count(key) == 1, key
        text = text.replace(key, value)
    assert "@@" not in text
    out = REV / "docs" / ("DIRAC16COMPLEX_FIELD_THEORY.provisional.md" if provisional else "DIRAC16COMPLEX_FIELD_THEORY.md")
    out.write_text(text, encoding="utf-8", newline="\n")
    print("written", out.name, len(text))


if __name__ == "__main__":
    main()
