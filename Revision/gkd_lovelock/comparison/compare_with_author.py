#!/usr/bin/env python3
"""Compare the Revision's curvature and Lovelock results with the author's OWN stored outputs.

Revision/gkd_lovelock/comparison/compare_with_author.py

Inputs (all read only):
  * author-curvature-outputs.json (next to this script), written by extract_author_curvature_outputs.wls
    from the author's notebook Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb
    (stored OUTPUT cells converted to exact InputForm without evaluating anything);
  * Revision/gkd_lovelock/results/curvature.json and lovelock-tensors.json (the Revision results);
  * Revision/SPEC.md section 1 (the binding statement of the metric);
  * the notebook file itself, only to recompute its sha256.

Method: every expression string is parsed EXACTLY (a small parser for the Mathematica InputForm subset
used by these files; integers and rationals only, no floating-point numbers), the stated coordinate and
function mapping is applied to the author's expressions, the stated normalisations are applied, and the
difference is reduced with sympy (expand, then simplify if expand does not give 0). A check is PASS only
when the difference is exactly 0. Nothing is fitted: every factor is fixed by a definition stated below
before any comparison is made.

Output: author-comparison-report.json next to this script (or --output). Deterministic, LF, ASCII.
Exit code 0 when no check FAILs (NOT-AVAILABLE is not a failure), 1 otherwise.
"""

import argparse
import hashlib
import json
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
NOTEBOOK = "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb"
AUTHOR_JSON = os.path.join(HERE, "author-curvature-outputs.json")
CURVATURE_JSON = os.path.join(ROOT, "Revision", "gkd_lovelock", "results", "curvature.json")
LOVELOCK_JSON = os.path.join(ROOT, "Revision", "gkd_lovelock", "results", "lovelock-tensors.json")
SPEC_MD = os.path.join(ROOT, "Revision", "SPEC.md")

# ----------------------------------------------------------------------------------------------
# The mapping (stated BEFORE any comparison; it is a definition, not a fit)
# ----------------------------------------------------------------------------------------------
# Author (notebook In[26]: X = {x0, x1, ..., x7}; In[79]/In[82]: MatrixMetric44 with
# beta3 = Exp[2 a4[H x4]], beta1 = Sin[6 H x0]^(1/3), beta2 = Cot[6 H x0]^2):
#   array position 1 = x0 (the hidden direction), positions 2..8 = x1..x7.
# Revision (SPEC section 1): x1, x2, x3 space, x4 time, x5, x6, x7 the deflating extra times,
#   x8 hidden; array positions 1..8 = x1..x8.
# Coordinate mapping: author x0 -> Revision x8; author xk -> Revision xk for k = 1..7.
# Function mapping: the author's a4 is a function of the argument H*x4, the Revision's a4 of x4:
#   a4_Revision(x4) := a4_author(H*x4), hence by the chain rule
#   a4_author^(n)(H*x4) = H^(-n) * a4_Revision^(n)(x4)   (n = 0, 1, 2).
AUTHOR_POSITION_TO_REVISION = ["x8", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
REVISION_ORDER = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]

MAPPING_TEXT = {
    "coordinates": "author array position 1 (x0, hidden) -> Revision x8; author positions 2..8 "
                   "(x1..x7) -> Revision x1..x7 (same names); tensor components are permuted accordingly",
    "function": "a4_Revision(x4) := a4_author(H*x4); therefore a4_author^(n)(H*x4) = H^(-n) a4_Revision^(n)(x4) "
                "(chain rule; n = 0, 1, 2); only the argument H*x4 occurs in the author's outputs (checked)",
    "constant": "H is the same constant on both sides",
    "status": "a definition fixed before the comparison and checked on the metric first; nothing is fitted",
}

NORMALISATIONS = [
    "Ricci scalar: both are scalars; no factor (the author's RS = Tr[ginv . Ric] with Ric_{mu nu} = "
    "R^a_{mu a nu}; the Revision's R in the MTW convention).",
    "Einstein tensor: the author's EinsteinG = Ric - (1/2) g RS has both indices DOWN (rt[] of In[214]); the "
    "Revision's einsteinMixed is G^mu_nu. The author's tensor is converted with the author's own (mapped) "
    "inverse metric: G^mu_nu = sum_s g^{mu s} G_{s nu}. No other factor.",
    "Lovelock k = 1: the Revision's normalisationNote states E_(k) = -P_(k)/2^(k+1), E_(1) = G, hence "
    "P_(1)^h_j = -4 G^h_j; compared with -4 times the author's G^mu_nu.",
    "Lovelock scalar k = 1: L_(1) = delta^{j1 j2}_{h1 h2} R^{h1 h2}_{j1 j2} = 2 R (identity of the generalized "
    "Kronecker delta); compared with 2 times the author's RS.",
]


class ParseError(Exception):
    pass


class MappingError(Exception):
    pass


# ----------------------------------------------------------------------------------------------
# Exact parser for the Mathematica InputForm subset of these files
# ----------------------------------------------------------------------------------------------
TOKEN_RE = re.compile(r"\s*(?:(\d+)|([A-Za-z][A-Za-z0-9]*)|(.))")
FUNCTIONS = {"Sin": sp.sin, "Cos": sp.cos, "Tan": sp.tan, "Cot": sp.cot, "Sec": sp.sec, "Csc": sp.csc,
             "Exp": sp.exp, "Log": sp.log, "Sqrt": sp.sqrt}
CONSTANTS = {"E": sp.E, "Pi": sp.pi}
SYMBOLS = {}


def sym(name):
    if name not in SYMBOLS:
        SYMBOLS[name] = sp.Symbol(name)
    return SYMBOLS[name]


def a4_function(order):
    """Undefined function standing for the n-th derivative of a parsed a4, before any mapping."""
    return sp.Function("a4_parsed_d%d" % order)


def tokenize(s):
    toks = []
    pos = 0
    s = s.strip()
    while pos < len(s):
        m = TOKEN_RE.match(s, pos)
        if m is None or m.end() == pos:
            raise ParseError("cannot tokenize at %d: %r" % (pos, s[pos:pos + 20]))
        num, ident, op = m.groups()
        if num is not None:
            toks.append(("num", num))
        elif ident is not None:
            toks.append(("id", ident))
        elif op is not None:
            if op.isspace():
                pass
            elif op in "+-*/^()[]{},":
                toks.append(("op", op))
            else:
                raise ParseError("unsupported character %r in %r" % (op, s[:80]))
        pos = m.end()
    return toks


class Parser:
    """expr := sum; sum := term (('+'|'-') term)*; term := unary (('*'|'/'|juxtaposition) unary)*;
    unary := '-' unary | power; power := postfix ['^' unary]; postfix := primary ('[' args ']')*;
    primary := integer | identifier | '(' expr ')' | '{' args '}'.  Juxtaposition is multiplication,
    as in Mathematica (needed for the SPEC's 'E^(2 a4[x4]) Sin[6 H x8]^(1/3)')."""

    def __init__(self, text):
        self.toks = tokenize(text)
        self.i = 0
        self.text = text

    def peek(self):
        return self.toks[self.i] if self.i < len(self.toks) else (None, None)

    def take(self, kind=None, value=None):
        t = self.peek()
        if t[0] is None or (kind and t[0] != kind) or (value and t[1] != value):
            raise ParseError("expected %s %s at token %d of %r" % (kind, value, self.i, self.text[:80]))
        self.i += 1
        return t

    def parse(self):
        e = self.sum()
        if self.i != len(self.toks):
            raise ParseError("trailing tokens in %r" % self.text[:80])
        return e

    def sum(self):
        e = self.term()
        while self.peek() in (("op", "+"), ("op", "-")):
            op = self.take()[1]
            r = self.term()
            e = e + r if op == "+" else e - r
        return e

    def starts_primary(self):
        k, v = self.peek()
        return k in ("num", "id") or (k == "op" and v in ("(", "{"))

    def term(self):
        e = self.unary()
        while True:
            t = self.peek()
            if t == ("op", "*"):
                self.take()
                e = e * self.unary()
            elif t == ("op", "/"):
                self.take()
                e = e / self.unary()
            elif self.starts_primary():
                e = e * self.unary()
            else:
                return e

    def unary(self):
        if self.peek() == ("op", "-"):
            self.take()
            return -self.unary()
        return self.power()

    def power(self):
        b = self.postfix()
        if self.peek() == ("op", "^"):
            self.take()
            return sp.Pow(b, self.unary())
        return b

    def args(self, close):
        out = []
        if self.peek() == ("op", close):
            self.take()
            return out
        while True:
            out.append(self.sum())
            if self.peek() == ("op", ","):
                self.take()
                continue
            self.take("op", close)
            return out

    def postfix(self):
        k, v = self.peek()
        if k == "id" and v == "Derivative":
            # Derivative[n][a4][arg]
            self.take()
            self.take("op", "[")
            n = self.args("]")
            self.take("op", "[")
            f = self.take("id")[1]
            self.take("op", "]")
            self.take("op", "[")
            a = self.args("]")
            if len(n) != 1 or not n[0].is_Integer or f != "a4" or len(a) != 1:
                raise ParseError("unsupported Derivative form in %r" % self.text[:80])
            return a4_function(int(n[0]))(a[0])
        if k == "id" and self.i + 1 < len(self.toks) and self.toks[self.i + 1] == ("op", "["):
            name = self.take()[1]
            self.take("op", "[")
            a = self.args("]")
            if name == "a4":
                if len(a) != 1:
                    raise ParseError("a4 with %d arguments" % len(a))
                return a4_function(0)(a[0])
            if name in FUNCTIONS:
                if len(a) != 1:
                    raise ParseError("%s with %d arguments" % (name, len(a)))
                return FUNCTIONS[name](a[0])
            raise ParseError("unknown function %s in %r" % (name, self.text[:80]))
        return self.primary()

    def primary(self):
        k, v = self.take()
        if k == "num":
            return sp.Integer(v)
        if k == "id":
            return CONSTANTS[v] if v in CONSTANTS else sym(v)
        if (k, v) == ("op", "("):
            e = self.sum()
            self.take("op", ")")
            return e
        if (k, v) == ("op", "{"):
            return ListValue(self.args("}"))
        raise ParseError("unexpected token %r in %r" % (v, self.text[:80]))


class ListValue(list):
    """A parsed Mathematica list (kept as a Python list of sympy expressions or lists)."""


def parse(text):
    s = text.strip()
    if s.startswith("HoldForm[") and s.endswith("]"):
        s = s[len("HoldForm["):-1]
    return Parser(s).parse()


# ----------------------------------------------------------------------------------------------
# Mappings
# ----------------------------------------------------------------------------------------------
x4, H = sym("x4"), sym("H")
REV = [sp.Function("a4_rev_d%d" % n) for n in range(3)]  # a4_Revision^(n), functions of x4


def map_parsed_a4(expr, expected_arg, scale):
    """Replace a4_parsed_d<n>(u) by scale^(-n) * a4_rev_d<n>(x4), requiring u == expected_arg exactly."""
    def is_a4(e):
        return isinstance(e, sp.core.function.AppliedUndef) and e.func.__name__.startswith("a4_parsed_d")

    def repl(e):
        n = int(e.func.__name__[len("a4_parsed_d"):])
        if sp.expand(e.args[0] - expected_arg) != 0:
            raise MappingError("a4 argument %s is not %s" % (e.args[0], expected_arg))
        return scale ** (-n) * REV[n](x4)
    return expr.replace(is_a4, repl)


def map_author(expr):
    """The stated mapping applied to one author expression: x0 -> x8, a4_author^(n)(H x4) -> H^-n a4^(n)(x4)."""
    e = expr.subs(sym("x0"), sym("x8"), simultaneous=True)
    return map_parsed_a4(e, H * x4, H)


def map_revision(expr):
    return map_parsed_a4(expr, x4, sp.Integer(1))


def exact_zero(diff):
    d = sp.expand(diff)
    if d == 0:
        return True, "expand"
    d = sp.simplify(d)
    return (d == 0), ("simplify" if d == 0 else "nonzero: " + sp.sstr(d))


def matrix_from_list(lv):
    if not (isinstance(lv, list) and len(lv) == 8 and all(isinstance(r, list) and len(r) == 8 for r in lv)):
        raise ParseError("not an 8 x 8 list")
    return [[lv[i][j] for j in range(8)] for i in range(8)]


def author_to_revision_matrix(m):
    """Permute the author's 8 x 8 component array to the Revision order (x1..x8) and map each entry."""
    pos = {name: p for p, name in enumerate(AUTHOR_POSITION_TO_REVISION)}
    return {(a, b): map_author(m[pos[a]][pos[b]]) for a in REVISION_ORDER for b in REVISION_ORDER}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def spec_metric():
    with open(SPEC_MD, encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"## 1\. The primordial gravitational field.*?```text\n(.*?)```", text, re.S)
    if not m:
        raise ParseError("SPEC section 1 metric block not found")
    block = " ".join(line.strip() for line in m.group(1).splitlines())
    if not block.startswith("g = "):
        raise ParseError("SPEC metric block does not start with 'g = '")
    return matrix_from_list(parse(block[len("g = "):]))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--output", default=os.path.join(HERE, "author-comparison-report.json"))
    args = ap.parse_args()

    with open(AUTHOR_JSON, encoding="utf-8") as f:
        author = json.load(f)
    with open(CURVATURE_JSON, encoding="utf-8") as f:
        curv = json.load(f)
    with open(LOVELOCK_JSON, encoding="utf-8") as f:
        love = json.load(f)

    outs = {o["label"]: o for o in author["outputCells"]}
    ins = {o["label"]: o for o in author["inputCells"]}
    checks = []

    def add(name, verdict, detail):
        checks.append({"name": name, "verdict": verdict, "detail": detail})

    # 0. the extraction belongs to the notebook in this working tree
    nb_sha = sha256_file(os.path.join(ROOT, NOTEBOOK))
    add("author-json-matches-notebook", "PASS" if nb_sha == author["notebookSha256"] else "FAIL",
        {"notebookSha256Recomputed": nb_sha, "notebookSha256InJson": author["notebookSha256"]})

    # 1. control: the two stored prints of the author's metric agree
    same = outs["Out[235]="]["inputForm"] == outs["Out[245]="]["inputForm"]
    add("author-metric-outputs-agree", "PASS" if same else "FAIL",
        {"compared": "Out[235] (gtry = MatrixMetric44) and Out[245] (MatrixMetric44): identical InputForm strings",
         "identical": same})

    # 2. Revision metric: SPEC section 1 versus curvature.json (diagonal list, off-diagonal zero)
    rev_g = {}
    for i, a in enumerate(REVISION_ORDER):
        for j, b in enumerate(REVISION_ORDER):
            rev_g[(a, b)] = map_revision(parse(curv["metricDiagonal"][i])) if i == j else sp.Integer(0)
    spec = spec_metric()
    bad = []
    for i, a in enumerate(REVISION_ORDER):
        for j, b in enumerate(REVISION_ORDER):
            ok, how = exact_zero(map_revision(spec[i][j]) - rev_g[(a, b)])
            if not ok:
                bad.append("%s,%s: %s" % (a, b, how))
    add("revision-metric-spec-vs-curvature-json", "PASS" if not bad else "FAIL",
        {"compared": "Revision/SPEC.md section 1 matrix vs curvature.json metricDiagonal (off-diagonal 0), "
                     "64 components", "mismatches": bad})

    # 3. FIRST the mapping on the metric itself
    a_g_list = parse(outs["Out[235]="]["inputForm"])
    try:
        a_g = author_to_revision_matrix(matrix_from_list(a_g_list))
        bad = []
        comps = {}
        for a in REVISION_ORDER:
            for b in REVISION_ORDER:
                ok, how = exact_zero(a_g[(a, b)] - rev_g[(a, b)])
                if a == b:
                    comps["%s,%s" % (a, b)] = {"authorMapped": sp.sstr(a_g[(a, b)]),
                                               "revision": sp.sstr(rev_g[(a, b)]), "exactlyEqual": ok}
                if not ok:
                    bad.append("%s,%s: %s" % (a, b, how))
        metric_ok = not bad
        add("metric-mapping-author-Out235-vs-revision", "PASS" if metric_ok else "FAIL",
            {"compared": "all 64 components of the author's Out[235] (mapped) vs the Revision metric",
             "diagonal": comps, "offDiagonal": "all 56 off-diagonal components are 0 on both sides" if metric_ok
             else "see mismatches", "mismatches": bad})
    except (MappingError, ParseError) as exc:
        add("metric-mapping-author-Out235-vs-revision", "FAIL", {"error": str(exc)})
        return finish(checks, ins, args, stopped="the mapping failed on the metric; nothing else compared")

    # inverse of the author's (mapped) metric, exactly (it is diagonal; checked)
    offdiag_zero = all(a_g[(a, b)] == 0 for a in REVISION_ORDER for b in REVISION_ORDER if a != b)
    if not (metric_ok and offdiag_zero):
        return finish(checks, ins, args, stopped="the metric check failed; nothing else compared")
    a_ginv = {a: 1 / a_g[(a, a)] for a in REVISION_ORDER}

    # 4. Ricci scalar
    a_rs = map_author(parse(outs["Out[535]="]["inputForm"]))
    r_rs = map_revision(parse(curv["ricciScalar"]))
    ok, how = exact_zero(a_rs - r_rs)
    add("ricci-scalar-author-Out535-vs-curvature-json", "PASS" if ok else "FAIL",
        {"author": outs["Out[535]="]["inputForm"], "authorMapped": sp.sstr(sp.expand(a_rs)),
         "revision": curv["ricciScalar"], "method": how})

    # 5. Einstein tensor, every component G^mu_nu
    a_G = author_to_revision_matrix(matrix_from_list(parse(outs["Out[536]="]["inputForm"])))
    a_Gmixed = {}
    for a in REVISION_ORDER:
        for b in REVISION_ORDER:
            a_Gmixed[(a, b)] = sp.expand(a_ginv[a] * a_G[(a, b)])
    for a in REVISION_ORDER:
        for b in REVISION_ORDER:
            key = "%s,%s" % (a, b)
            r = map_revision(parse(curv["einsteinMixed"][key]["mathematica"]))
            ok, how = exact_zero(a_Gmixed[(a, b)] - r)
            add("einstein-mixed-%s" % key, "PASS" if ok else "FAIL",
                {"authorLowerMapped": sp.sstr(a_G[(a, b)]), "authorMixed": sp.sstr(a_Gmixed[(a, b)]),
                 "revision": curv["einsteinMixed"][key]["mathematica"], "method": how})

    # 6. Lovelock k = 1: P_(1) = -4 G (all 64 components) and L_(1) = 2 R
    bad = []
    for a in REVISION_ORDER:
        for b in REVISION_ORDER:
            key = "%s,%s" % (a, b)
            r = map_revision(parse(love["P1_mixed_up_h_down_j"][key]["mathematica"]))
            ok, how = exact_zero(-4 * a_Gmixed[(a, b)] - r)
            if not ok:
                bad.append("%s: %s" % (key, how))
    add("lovelock-P1-vs-minus4-author-EinsteinG", "PASS" if not bad else "FAIL",
        {"compared": "lovelock-tensors.json P1_mixed_up_h_down_j (64 components) vs -4 x the author's G^mu_nu "
                     "(Out[536], mapped, index raised)", "mismatches": bad})
    r_l1 = map_revision(parse(love["L1"]))
    ok, how = exact_zero(2 * a_rs - r_l1)
    add("lovelock-L1-vs-2-author-RS", "PASS" if ok else "FAIL",
        {"revision": love["L1"], "twiceAuthorMapped": sp.sstr(sp.expand(2 * a_rs)), "method": how})

    # 7. what has no stored author output
    scan = {s["file"]: s for s in author["keywordScan"]}
    evidence = {
        s["file"]: {"cellsContainingLovelock": len(s["cellsContainingLovelock"]),
                    "outputCellsContainingLovelock": s["outputCellsContainingLovelock"],
                    "outputCellsContainingLovelockThatAreOnlyStrings":
                        sum(1 for c in s["cellsContainingLovelock"] if c["outputIsOnlyStrings"] is True)}
        for s in scan.values()}
    for k in (2, 3):
        add("lovelock-k%d-P%d-and-L%d" % (k, k, k), "NOT-AVAILABLE",
            {"reason": "no stored output of the k = %d Lovelock tensor or scalar was found in either notebook" % k,
             "keywordScan": evidence})
    return finish(checks, ins, args, stopped=None)


def finish(checks, ins, args, stopped):
    in238 = ins["In[238]:="]["inputForm"]
    for obj in ("christoffel", "riemann", "ricci-tensor"):
        add("%s-components" % obj, "NOT-AVAILABLE",
            {"reason": "rt[gtry] computes it, but In[238] suppresses its output (ends with ';'); no stored output "
                       "of its values was taken from the notebook",
             "In[238]": in238, "In238EndsWithSemicolon": in238.rstrip("]").rstrip().endswith(";")})

    counts = {v: sum(1 for c in checks if c["verdict"] == v) for v in ("PASS", "FAIL", "NOT-AVAILABLE")}
    report = {
        "program": "Revision/gkd_lovelock/comparison/compare_with_author.py",
        "sympyVersion": sp.__version__,
        "inputs": [{"path": rel(p), "sha256": sha256_file(p)}
                   for p in (AUTHOR_JSON, CURVATURE_JSON, LOVELOCK_JSON, SPEC_MD, os.path.join(ROOT, NOTEBOOK))],
        "authorConventions": {
            "rt": "In[214]: Gamma^i_{jk} = (1/2) g^{is}(d_k g_{sj} + d_j g_{sk} - d_s g_{jk}); "
                  "R^mu_{nu alpha beta} = d_alpha Gamma^mu_{nu beta} - d_beta Gamma^mu_{nu alpha} + "
                  "Gamma^mu_{s alpha} Gamma^s_{nu beta} - Gamma^mu_{s beta} Gamma^s_{nu alpha} (the notebook calls it "
                  "RicciGamma); Ric_{mu nu} = R^alpha_{mu alpha nu} (called RieGamma); RS = Tr[ginv . Ric]; "
                  "G = Ric - (1/2) g RS (indices down)",
            "storedOutputsUsed": ["Out[235]", "Out[245]", "Out[535]", "Out[536]"],
        },
        "mapping": MAPPING_TEXT,
        "normalisations": NORMALISATIONS,
        "checks": checks,
        "summary": dict(counts, total=len(checks)),
        "stopped": stopped,
    }
    text = json.dumps(report, indent=2, ensure_ascii=True) + "\n"
    with open(args.output, "w", encoding="ascii", newline="\n") as f:
        f.write(text)
    print("checks: %d; PASS %d, FAIL %d, NOT-AVAILABLE %d" % (len(checks), counts["PASS"], counts["FAIL"],
                                                              counts["NOT-AVAILABLE"]))
    for c in checks:
        if c["verdict"] == "FAIL":
            print("FAIL:", c["name"], json.dumps(c["detail"])[:400])
    print("wrote", args.output)
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
