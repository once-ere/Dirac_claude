"""Generate the Rust constants of studies/dirac16complex_cosmology from the
exact dirac16complex algebra fixture (standard library only).

Input  (default): artifacts/dirac16complex/arbitrary-field/algebra-fixture.json
Output (default): studies/dirac16complex_cosmology/src/generated.rs

What the script does
--------------------
1. Builds the notebook split-octonion gamma matrices independently, in exact
   integer arithmetic, from the definition in CONTRACT.md section 1
   (Qa[h,p,q] = Signature[{h,p,q,4}], Qb = d_{p4} d_{qh} - d_{ph} d_{q4},
   s4 = Qa - Qb, t4 = Qa + Qb, tau, taubar = sigma tau^T sigma,
   gamma^a = [[0, taubar[a]], [tau[a], 0]]).  All indices are zero-based;
   the notebook's 1-based h, p, q appear only inside Qa/Qb.
2. If the fixture exists it is read and its "gamma" (8 integer 16x16
   matrices), "C", "chirality" and "B" entries are compared EXACTLY with the
   independent construction.  Any disagreement makes the script refuse:
   it prints the mismatch and exits with status 1 without writing anything.
3. Verifies exactly (integer arithmetic):
     {gamma^a, gamma^b} = 2 eta^{ab} I16, eta = diag(1,1,1,1,-1,-1,-1,-1);
     C = gamma^0 gamma^1 gamma^2 gamma^3, C symmetric, C^2 = I;
     (C gamma^a)^T = -C gamma^a for a = 0..7;
     chirality gamma^0 ... gamma^7 = diag(-I8, +I8);
     B = -i C gamma^4 Hermitian (<=> C gamma^4 antisymmetric) and
     B^2 = I (<=> (C gamma^4)^2 = -I).
   Any failure exits with status 1.
4. Writes generated.rs (LF line endings, deterministic) with the fixture's
   SHA-256 embedded.  If the fixture is absent the script falls back to the
   contract construction, records FIXTURE_SOURCE = "contract-fallback" and
   FIXTURE_SHA256 = "absent", and says so on stdout (use --require-fixture to
   make an absent fixture an error instead).

Options: --fixture PATH, --output PATH, --require-fixture,
--check (compare the would-be output with the existing file; exit 1 if it
differs; nothing is written).
"""

import argparse
import hashlib
import json
import os
import sys

REPOSITORY_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_FIXTURE = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex",
                               "arbitrary-field", "algebra-fixture.json")
DEFAULT_OUTPUT = os.path.join(REPOSITORY_ROOT, "studies", "dirac16complex_cosmology",
                              "src", "generated.rs")
FIXTURE_RELATIVE = "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json"
GENERATOR = "scripts/generate_dirac16complex_constants.py"

ETA_DIAGONAL = (1, 1, 1, 1, -1, -1, -1, -1)
N16 = 16


# ---------------------------------------------------------------------------
# exact integer matrices (lists of lists of int)
# ---------------------------------------------------------------------------

def zeros(n, m=None):
    m = n if m is None else m
    return [[0] * m for _ in range(n)]


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def mat_mul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    out = zeros(n, m)
    for i in range(n):
        row = out[i]
        for p in range(k):
            aip = a[i][p]
            if aip:
                bp = b[p]
                for j in range(m):
                    if bp[j]:
                        row[j] += aip * bp[j]
    return out


def mat_add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mat_neg(a):
    return [[-x for x in row] for row in a]


def mat_scale(s, a):
    return [[s * x for x in row] for row in a]


def transpose(a):
    return [list(col) for col in zip(*a)]


def block2(a, b, c, d):
    """[[a, b], [c, d]] with equally sized square blocks."""
    top = [ra + rb for ra, rb in zip(a, b)]
    bottom = [rc + rd for rc, rd in zip(c, d)]
    return top + bottom


def signature(sequence):
    """Mathematica Signature: 0 on repeated entries, else the permutation sign."""
    items = list(sequence)
    if len(set(items)) != len(items):
        return 0
    inversions = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] > items[j]:
                inversions += 1
    return -1 if inversions % 2 else 1


def qa(h, p, q):
    return signature((h, p, q, 4))


def qb(h, p, q):
    return (1 if p == 4 and q == h else 0) - (1 if p == h and q == 4 else 0)


def contract_gammas():
    """gamma^0..gamma^7 from CONTRACT.md section 1 (independent construction)."""
    def s4(h):
        return [[qa(h, p, q) - qb(h, p, q) for q in range(1, 5)] for p in range(1, 5)]

    def t4(h):
        return [[qa(h, p, q) + qb(h, p, q) for q in range(1, 5)] for p in range(1, 5)]

    z4 = zeros(4)
    tau = [None] * 8
    tau[0] = eye(8)
    for h in (1, 2, 3):
        tau[h] = block2(z4, s4(h), s4(h), z4)
        tau[7 - h] = block2(z4, t4(h), mat_neg(t4(h)), z4)
    product = eye(8)
    for a in range(1, 7):
        product = mat_mul(product, tau[a])
    tau[7] = product
    sigma = block2(z4, eye(4), eye(4), z4)
    taubar = [eye(8)] + [mat_mul(mat_mul(sigma, transpose(tau[a])), sigma)
                         for a in range(1, 8)]
    z8 = zeros(8)
    return [block2(z8, taubar[a], tau[a], z8) for a in range(8)]


def charge_matrix(gammas):
    return mat_mul(mat_mul(gammas[0], gammas[1]), mat_mul(gammas[2], gammas[3]))


def chirality_matrix(gammas):
    product = eye(N16)
    for gamma in gammas:
        product = mat_mul(product, gamma)
    return product


# ---------------------------------------------------------------------------
# fixture reading
# ---------------------------------------------------------------------------

def integer_matrix(rows, name):
    if not isinstance(rows, list) or len(rows) != N16:
        raise ValueError("%s is not a 16-row matrix" % name)
    out = []
    for row in rows:
        if not isinstance(row, list) or len(row) != N16:
            raise ValueError("%s has a row that is not of length 16" % name)
        converted = []
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError("%s has a non-integer entry %r" % (name, value))
            converted.append(value)
        out.append(converted)
    return out


def read_fixture(path):
    with open(path, "rb") as handle:
        data = handle.read()
    document = json.loads(data.decode("utf-8"))
    gammas = document.get("gamma")
    if not isinstance(gammas, list) or len(gammas) != 8:
        raise ValueError("fixture key 'gamma' must hold 8 matrices")
    fixture = {"gamma": [integer_matrix(g, "gamma[%d]" % a) for a, g in enumerate(gammas)]}
    if "C" in document:
        fixture["C"] = integer_matrix(document["C"], "C")
    if "chirality" in document:
        fixture["chirality"] = integer_matrix(document["chirality"], "chirality")
    if isinstance(document.get("B"), dict):
        fixture["B_real"] = integer_matrix(document["B"]["real"], "B.real")
        fixture["B_imag"] = integer_matrix(document["B"]["imag"], "B.imag")
    return data, fixture


# ---------------------------------------------------------------------------
# verification
# ---------------------------------------------------------------------------

def verify(gammas):
    checks = []
    identity = eye(N16)
    clifford = True
    for a in range(8):
        for b in range(8):
            anti = mat_add(mat_mul(gammas[a], gammas[b]), mat_mul(gammas[b], gammas[a]))
            expected = mat_scale(2 * ETA_DIAGONAL[a] if a == b else 0, identity)
            if anti != expected:
                clifford = False
    checks.append(("clifford_relations", clifford))
    symmetry = all(
        (transpose(gammas[a]) == gammas[a]) if a < 4 else (transpose(gammas[a]) == mat_neg(gammas[a]))
        for a in range(8))
    checks.append(("gamma_symmetric_space_antisymmetric_time", symmetry))
    c = charge_matrix(gammas)
    checks.append(("C_symmetric", transpose(c) == c))
    checks.append(("C_squared_identity", mat_mul(c, c) == identity))
    expected_c = block2(mat_neg(block2(zeros(4), eye(4), eye(4), zeros(4))), zeros(8),
                        zeros(8), block2(zeros(4), eye(4), eye(4), zeros(4)))
    checks.append(("C_equals_blockdiag_minus_sigma_sigma", c == expected_c))
    adjoint = all(transpose(mat_mul(c, gammas[a])) == mat_neg(mat_mul(c, gammas[a]))
                  for a in range(8))
    checks.append(("C_gamma_antisymmetric_all_a", adjoint))
    chir = chirality_matrix(gammas)
    expected_chir = [[(-1 if i < 8 else 1) if i == j else 0 for j in range(N16)]
                     for i in range(N16)]
    checks.append(("chirality_diag_minus_plus", chir == expected_chir))
    c_g4 = mat_mul(c, gammas[4])
    # B = -i C gamma^4: real part 0, imaginary part -C gamma^4 (real integer).
    checks.append(("B_hermitian", transpose(c_g4) == mat_neg(c_g4)))
    checks.append(("B_squared_identity", mat_mul(c_g4, c_g4) == mat_neg(identity)))
    return checks, c, chir, mat_neg(c_g4)


# ---------------------------------------------------------------------------
# rendering
# ---------------------------------------------------------------------------

def render_value(value):
    return "%d.0" % value


def render_matrix_rows(matrix, indent):
    lines = []
    for row in matrix:
        lines.append("%s[%s]," % (indent, ", ".join(render_value(v) for v in row)))
    return lines


def render(gammas, c, chir, b_imag, sha256, source):
    lines = [
        "// Generated by %s." % GENERATOR,
        "// Do not edit by hand.",
        "//",
        "// Source: %s" % FIXTURE_RELATIVE,
        "// Gamma matrices gamma^a (a = 0..7) in the notebook split-octonion",
        "// basis, zero-based; eta = diag(1,1,1,1,-1,-1,-1,-1).",
        "// C = gamma^0 gamma^1 gamma^2 gamma^3; CHIRALITY = gamma^0 ... gamma^7;",
        "// B = -i C gamma^4 = i * B_IMAG (its real part is identically zero).",
        "",
        "#[rustfmt::skip]",
        "pub const FIXTURE_SHA256: &str = \"%s\";" % sha256,
        "#[rustfmt::skip]",
        "pub const FIXTURE_SOURCE: &str = \"%s\";" % source,
        "#[rustfmt::skip]",
        "pub const FIXTURE_PATH: &str = \"%s\";" % FIXTURE_RELATIVE,
        "pub const SPINOR_DIMENSION: usize = 16;",
        "pub const FRAME_DIMENSION: usize = 8;",
        "",
        "#[rustfmt::skip]",
        "pub const ETA: [f64; FRAME_DIMENSION] = [%s];" % ", ".join(render_value(v) for v in ETA_DIAGONAL),
        "",
        "#[rustfmt::skip]",
        "pub const GAMMA: [[[f64; SPINOR_DIMENSION]; SPINOR_DIMENSION]; FRAME_DIMENSION] = [",
    ]
    for a, gamma in enumerate(gammas):
        lines.append("    // gamma^%d" % a)
        lines.append("    [")
        lines.extend(render_matrix_rows(gamma, "        "))
        lines.append("    ],")
    lines.append("];")
    for name, matrix, comment in (
            ("CHARGE", c, "C = gamma^0 gamma^1 gamma^2 gamma^3 (Psibar = Psi^dagger C)"),
            ("CHIRALITY", chir, "gamma^8 = gamma^0 ... gamma^7 = diag(-I8, +I8)"),
            ("B_IMAG", b_imag, "B = -i C gamma^4 = i * B_IMAG, B_IMAG = -C gamma^4")):
        lines.append("")
        lines.append("// %s" % comment)
        lines.append("#[rustfmt::skip]")
        lines.append("pub const %s: [[f64; SPINOR_DIMENSION]; SPINOR_DIMENSION] = [" % name)
        lines.extend(render_matrix_rows(matrix, "    "))
        lines.append("];")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--fixture", default=DEFAULT_FIXTURE)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--require-fixture", action="store_true")
    parser.add_argument("--check", action="store_true")
    arguments = parser.parse_args(argv)

    gammas = contract_gammas()
    if os.path.exists(arguments.fixture):
        try:
            data, fixture = read_fixture(arguments.fixture)
        except (ValueError, KeyError, json.JSONDecodeError) as error:
            print("REFUSED: cannot read fixture: %s" % error)
            return 1
        mismatches = [a for a in range(8) if fixture["gamma"][a] != gammas[a]]
        if mismatches:
            print("REFUSED: fixture gamma matrices %s disagree with the CONTRACT.md "
                  "section 1 construction" % mismatches)
            return 1
        sha256 = hashlib.sha256(data).hexdigest()
        source = "fixture"
        print("fixture=%s" % os.path.abspath(arguments.fixture).replace("\\", "/"))
        print("fixture_sha256=%s" % sha256)
    else:
        if arguments.require_fixture:
            print("REFUSED: fixture %s is absent" % arguments.fixture)
            return 1
        fixture = None
        sha256 = "absent"
        source = "contract-fallback"
        print("NOTICE: fixture %s is absent; using the CONTRACT.md section 1 "
              "construction as a fallback" % arguments.fixture)

    checks, c, chir, b_imag = verify(gammas)
    if fixture is not None:
        if "C" in fixture:
            checks.append(("fixture_C_matches", fixture["C"] == c))
        if "chirality" in fixture:
            checks.append(("fixture_chirality_matches", fixture["chirality"] == chir))
        if "B_imag" in fixture:
            checks.append(("fixture_B_matches", fixture["B_real"] == zeros(N16)
                           and fixture["B_imag"] == b_imag))
    failed = 0
    for name, passed in checks:
        print("check_%s=%s" % (name, "true" if passed else "false"))
        failed += 0 if passed else 1
    print("check_count=%d" % len(checks))
    print("failed_check_count=%d" % failed)
    if failed:
        print("REFUSED: exact verification failed; nothing written")
        return 1

    text = render(gammas, c, chir, b_imag, sha256, source)
    data = text.encode("utf-8")
    if arguments.check:
        existing = b""
        if os.path.exists(arguments.output):
            with open(arguments.output, "rb") as handle:
                existing = handle.read()
        same = existing == data
        print("generated_up_to_date=%s" % ("true" if same else "false"))
        return 0 if same else 1
    os.makedirs(os.path.dirname(os.path.abspath(arguments.output)), exist_ok=True)
    with open(arguments.output, "wb") as handle:
        handle.write(data)
    print("output=%s" % os.path.abspath(arguments.output).replace("\\", "/"))
    print("output_sha256=%s" % hashlib.sha256(data).hexdigest())
    print("fixture_source=%s" % source)
    return 0


if __name__ == "__main__":
    sys.exit(main())
