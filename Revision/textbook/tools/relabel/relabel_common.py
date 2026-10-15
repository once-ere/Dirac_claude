"""Shared helpers for relabelling the Revision documents to the author's coordinates x0..x7 (2026-10-14)."""
import glob
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]  # the repository folder

# check names whose relabelled form is not a plain x8 -> x0 (the order of the pair follows the author's order)
NAME_MAP = {
    "Omega_x4_Omega_x8_vanish": "Omega_x0_Omega_x4_vanish",
    "Omega_x4_and_Omega_x8_vanish": "Omega_x0_and_Omega_x4_vanish",
    "ownrep_Omega_x4_x8_zero": "ownrep_Omega_x0_x4_zero",
    "authorT16_Omega_x4_x8_zero": "authorT16_Omega_x0_x4_zero",
    "off_diagonal_entries_x4_x8_only": "off_diagonal_entries_x0_x4_only",
    "gamma_Omega_equals_3H_gamma8": "gamma_Omega_equals_3H_gamma0",
}


def known_names():
    """Every check name of a Revision report and every key of a Revision JSON file (outside textbook/workflows)."""
    names = set()

    def keys(v):
        if isinstance(v, dict):
            for k, x in v.items():
                names.add(k)
                keys(x)
        elif isinstance(v, list):
            for x in v:
                keys(x)

    for f in glob.glob(str(REPO / "Revision" / "**" / "*.json"), recursive=True):
        if "textbook" in f or "workflows" in f or "\\target\\" in f:
            continue
        try:
            d = json.loads(Path(f).read_text(encoding="utf-8"))
        except Exception:
            continue
        keys(d)
        ch = d.get("checks") if isinstance(d, dict) else None
        if isinstance(ch, list):
            for c in ch:
                if isinstance(c, dict) and "name" in c:
                    names.add(c["name"])
    return names


def relabel_code_spans(text, known, extra=None):
    """In every inline code span: apply NAME_MAP (and `extra`), then x8 -> x0 / p8 -> p0 inside identifier-like spans.
    Returns the text and the list of relabelled spans that are not known names (for review)."""
    extra = extra or {}
    unknown = []

    def fix(m):
        span = m.group(1)
        new = extra.get(span, NAME_MAP.get(span, span))
        if new == span and re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.*,\-]*", span) and re.search(r"x8|p8|P8|w8", span):
            new = re.sub(r"x8", "x0", span)
            new = re.sub(r"(?<![A-Za-z0-9])p8(?![0-9])", "p0", new)
            new = re.sub(r"(?<=_)p8(?![0-9])", "p0", new)
            new = re.sub(r"(?<![A-Za-z0-9])P8(?![0-9])", "P0", new)
        if new != span and new not in known:
            unknown.append((span, new))
        return "`" + new + "`"

    return re.sub(r"`([^`\n]+)`", fix, text), unknown


def strict_replace(text, pairs, label="doc"):
    for a, b, *cnt in pairs:
        n = text.count(a)
        want = cnt[0] if cnt else 1
        if want == "any":
            if n == 0:
                sys.exit(f"{label}: not found: {a[:120]!r}")
        elif n != want:
            sys.exit(f"{label}: expected {want}, found {n}: {a[:120]!r}")
        text = text.replace(a, b)
    return text


def leftovers(text, pattern=r"x_8|x8|g_\{88\}|p_8|\\gamma\^8|\^\{8\}|_\{8\}|R_8|P_8|\\partial_8|\btau\^8"):
    return [l for l in text.split("\n") if re.search(pattern, l)]
