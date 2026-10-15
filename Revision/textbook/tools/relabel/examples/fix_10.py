"""Chapter 10 builders: the gammas and the momenta are keyed by the direction; with the
author's coordinates x0..x7 the key is the position in gammas.json (no "- 1"), the hidden
direction is key 0 (formerly 8), and the record's momentum lists are in the order k0..k7."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO  # noqa: E402

SRC = REPO / "Revision/textbook/notebooks/src"
GENERIC = [
    (r'fixture\["gamma"\]\[a - 1\]', 'fixture["gamma"][a]'),
    (r'fixture\["eta"\]\[a - 1\]', 'fixture["eta"][a]'),
    (r"range\(1, 9\)", "range(8)"),
    (r"\b(gamma|g|k_sym|k_reflected|k_symbol|d|d_conj)\[8\]", r"\1[0]"),
    (r"\(1, 2, 3, 5, 6, 7, 8\)", "(0, 1, 2, 3, 5, 6, 7)"),
    (r"k_list\[a - 1\]", "k_list[a]"),
    (r"\{1: 2, 8: 2\}", "{0: 2, 1: 2}"),
    (r"\{1: 1, 2: 2, 8: 4\}", "{0: 4, 1: 1, 2: 2}"),
    (r"\{1: 0\.3, 2: -1\.1, 3: 0\.7, 5: 0\.4, 6: 0\.2, 7: -0\.9, 8: 1\.3\}",
     "{0: 1.3, 1: 0.3, 2: -1.1, 3: 0.7, 5: 0.4, 6: 0.2, 7: -0.9}"),
    (r"\{1: 0\.4, 2: -0\.7, 3: 0\.2, 5: 0\.9, 6: -0\.3, 7: 0\.5, 8: 1\.1\}",
     "{0: 1.1, 1: 0.4, 2: -0.7, 3: 0.2, 5: 0.9, 6: -0.3, 7: 0.5}"),
    (r"\bk1 = 2, k8 = 2\b", "k0 = 2, k1 = 2"),
    (r"k1\^2 \+ k2\^2 \+ k3\^2 \+ k8\^2", "k0^2 + k1^2 + k2^2 + k3^2"),
    (r"k_1\^2 \+ k_2\^2 \+ k_3\^2 \+ k_0\^2", "k_0^2 + k_1^2 + k_2^2 + k_3^2"),
    (r"\$k = \(1, 2, 0, 4\)\$", "$(k_0, k_1, k_2, k_3) = (4, 1, 2, 0)$"),
    (r"R_8: k8 -> -k8", "R_0: k0 -> -k0"),
    (r"\bk8\b", "k0"),
    (r"\bk_8\b", "k_0"),
    (r"\bR_8\b", "R_0"),
    (r"\bgamma8\b", "gamma0"),
    (r"\bM8\b", "M0"),
    (r"\bM_8\b", "M_0"),
    (r"\bG48\b", "G40"),
    (r"\bG48_numbers\b", "G40_numbers"),
    (r"\bd8\b", "d0"),
    (r"\(1, 2\), \(1, 3\), \.\.\., \(7, 8\)", "(0, 1), (0, 2), ..., (6, 7)"),
]
for builder in sorted(SRC.glob("10*.py")):
    text = builder.read_text(encoding="utf-8")
    new = text
    for pattern, replacement in GENERIC:
        new = re.sub(pattern, replacement, new)
    if builder.name.startswith("10c"):  # the bar positions of eight waves, not directions
        new = new.replace("axes[0].bar(range(8), classical,", "axes[0].bar(range(1, 9), classical,")
        new = new.replace("axes[0].set_xticks(range(8))", "axes[0].set_xticks(range(1, 9))")
    if new != text:
        builder.write_bytes(new.encode("utf-8"))
    left = [f"{i + 1}: {l.strip()}" for i, l in enumerate(new.splitlines())
            if re.search(r"\[8\]|a - 1\]|\b8: |gamma\[7\] @ gamma\[1\]", l)]
    print(builder.name, "changed" if new != text else "unchanged", left[:6])
