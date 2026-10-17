"""Fill PAIR.draft.md and write Revision/docs/PAIR_CREATION_PROOFS.md.

The generated parts (reflection table, one-particle samples, signs of P_n, per-theorem check tables, count table) are
made from the Revision records; the parts that need the W5/W6 records are read from the text files next to this script
(pair_ks_theory.md, pair_ks_source.md, pair_demos.md, pair_runs.md) and must exist.
"""
import json
import re
import sys
from pathlib import Path

SP = Path(__file__).resolve().parent
ROOT = Path(r"D:\Developer\github\Dirac_claude")
REV = ROOT / "Revision"

COUNTED = (
    "Revision/pairing/reports/wolfram-pairing.json",
    "Revision/pairing/reports/python-pairing.json",
    "Revision/pairing/kohn_sham/reports/wolfram-t3.json",
    "Revision/pairing/kohn_sham/reports/python-t3.json",
    "Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json",
    "Revision/pairing/kohn_sham/reports/t3-rust-demo.json",
    "Revision/pairing/kohn_sham/reports/t3-reference-demo.json",
    "Revision/pairing/kohn_sham/reports/python-t3-completion.json",
    "Revision/algebra/reports/wolfram-algebra.json",
    "Revision/algebra/reports/python-algebra.json",
    "Revision/theory/reports/wolfram-field-theory.json",
    "Revision/theory/reports/python-field-theory.json",
    "Revision/theory/reports/wolfram-scope.json",
    "Revision/theory/reports/python-scope.json",
    "Revision/field_equations_a4/reports/wolfram-a4-report.json",
    "Revision/field_equations_a4/reports/python-a4-report.json",
    "Revision/field_equations_a4/ks_source/reports/ks-source-a4.json",
    "Revision/kohn_sham/reports/ks-theory-wolfram.json",
    "Revision/kohn_sham/reports/ks-theory-python.json",
    "Revision/kohn_sham/reports/ks-rust-solver.json",
)


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def count_table():
    rows = ["| report | checks | PASS | FAIL |", "| --- | --- | --- | --- |"]
    for rel in COUNTED:
        checks = load(rel)["checks"]
        p = sum(1 for c in checks if str(c["verdict"]).upper() == "PASS")
        f = sum(1 for c in checks if str(c["verdict"]).upper() == "FAIL")
        assert f == 0 and p == len(checks), rel
        rows.append(f"| `{rel}` | {len(checks)} | {p} | {f} |")
    return "\n".join(rows)


THEORY = load("Revision/pairing/pairing-theory.json")


def reflection_table():
    rows = [r"| direction | $\eta_{nn}$ | character of $P_n$ | $S$ under $\gamma^n$ | kinetic term | map |",
            "| --- | --- | --- | --- | --- | --- |"]
    for r in THEORY["data"]["reflections"]:
        d = r["direction"][1:]
        if r["eta_nn"] == 1:
            assert "(T2)" in r["mass_coupling_map"]
            rows.append(f"| $x_{d}$ | $+1$ | $-1$ | $-S$ | $+K$ | " + r"$(-m,\lambda)$, $+\mathcal{L}$ (T2) |")
        else:
            assert "T1-type" in r["mass_coupling_map"]
            rows.append(f"| $x_{d}$ | $-1$ | $+1$ | $+S$ | $-K$ | " + r"$(-m,-\lambda)$, $-\mathcal{L}$ (T1-type) |")
    return "\n".join(rows)


def pn_signs():
    signs = ["+1" if r["P_n_equals_sign_times_product_of_other_seven"] > 0 else "-1" for r in THEORY["data"]["reflections"]]
    return "$" + ", ".join(signs) + "$"


def sample_table():
    rows = [r"| $m$ | momentum $(k_0, \dots, k_7)$ | $w$ | dimensions of the $+w$ and $-w$ eigenspaces | Krein inertia on $+w$ and on $-w$ |",
            "| --- | --- | --- | --- | --- |"]
    for s in THEORY["data"]["one_particle_flat"]["samples"]:
        assert (s["dim_plus_w"], s["dim_minus_w"]) == (8, 8) and s["B_inertia_plus_w"] == [4, 4] == s["B_inertia_minus_w"]
        w = re.sub(r"Sqrt\[(\d+)\]", r"\\sqrt{\1}", s["w"])
        k = ", ".join(str(v) for v in s["k"])
        rows.append(f"| ${s['m']}$ | ({k}) | ${w}$ | 8 and 8 | (4,4) and (4,4) |")
    return "\n".join(rows)


def grid(title, names):
    rows = [f"**{title}** ({len(names)} checks):", "", "| check | check | check |", "| --- | --- | --- |"]
    for k in range(0, len(names), 3):
        cells = [f"`{n}`" for n in names[k:k + 3]] + [""] * (3 - len(names[k:k + 3]))
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(rows)


def check_tables():
    wolfram = [c["name"] for c in load("Revision/pairing/reports/wolfram-pairing.json")["checks"]]
    python = [c["name"] for c in load("Revision/pairing/reports/python-pairing.json")["checks"]]
    ver = {t["id"]: t["verification"] for t in THEORY["theorems"]}
    for tid in ver:
        assert all(n in wolfram for n in ver[tid]), tid
    used = set(ver["T1"]) | set(ver["T2"]) | set(ver["Q"])
    common_w = [n for n in wolfram if n not in used]
    t1p = [n for n in python if n.startswith("T1.")]
    t2p = [n for n in python if n.startswith("T2.") or n in ("geometry.fold_degenerate", "geometry.mirror_isometry")]
    qp = [n for n in python if n.startswith("Q.")]
    common_p = [n for n in python if n not in t1p + t2p + qp]
    assert len(t1p) + len(t2p) + len(qp) + len(common_p) == len(python)
    assert len(ver["T1"]) + len(ver["T2"]) + len(ver["Q"]) + len(common_w) == len(wolfram)
    blocks = [grid("T1, Wolfram", ver["T1"]), grid("T1, sympy", t1p), grid("T2, Wolfram", ver["T2"]),
              grid("T2, sympy", t2p), grid("Q, Wolfram", ver["Q"]), grid("Q, sympy", qp),
              grid("Common checks (gammas, geometry, comparison with the Wolfram record), sympy", common_p),
              grid("Common checks (fixture, test fields, connections, determinism), Wolfram", common_w)]
    return "\n\n".join(blocks), len(wolfram), len(python)


def main():
    text = (SP / "PAIR.draft.md").read_text(encoding="utf-8")
    tables, nw, np_ = check_tables()
    blocks = {"@@COUNT_TABLE@@": count_table(), "@@REFLECTION_TABLE@@": reflection_table(), "@@PN_SIGNS@@": pn_signs(),
              "@@SAMPLE_TABLE@@": sample_table(), "@@CHECK_TABLES@@": tables, "@@NW@@": str(nw), "@@NP@@": str(np_)}
    for name in ("KS_THEORY_INGREDIENTS", "KS_SOURCE_PARAGRAPH", "DEMOS", "RUNS"):
        part = SP / f"pair_{name.lower()}.md"
        if not part.exists():
            sys.exit(f"missing {part.name}")
        blocks[f"@@{name}@@"] = part.read_text(encoding="utf-8").strip("\n")
    for key, value in blocks.items():
        assert text.count(key) == 1, key
        text = text.replace(key, value)
    assert "@@" not in text
    (REV / "docs" / "PAIR_CREATION_PROOFS.md").write_text(text, encoding="utf-8", newline="\n")
    print("written", len(text))


if __name__ == "__main__":
    main()
