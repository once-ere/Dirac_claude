#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Generate the Rust constants of studies/dirac16complex_kohn_sham from the
exact dirac16complex algebra fixture (standard library only).

Input  (default): artifacts/dirac16complex/arbitrary-field/algebra-fixture.json
Output (default): studies/dirac16complex_kohn_sham/src/generated.rs
Report (default): artifacts/dirac16complex/kohn-sham/rust/generator-report.json

Origin.  The gamma-matrix part (independent CONTRACT.md section 1
construction in exact integer arithmetic, comparison with the fixture, the
Clifford / C / chirality / B identities, the rendering of GAMMA, CHARGE,
CHIRALITY and B_IMAG) is imported from scripts/generate_dirac16complex_constants.py
of the Stage-3 crate (same repository, same licence); it is not duplicated.

New in Stage 4: the EXACT 2x2 block reduction of the Kohn-Sham equation.

  The reduced equation of STAGE4_SPEC section 2 is
      chi' = [ M_eff(y) A0 - i kappa(y) k A1 + i eps A4 ] chi,
      A0 = gamma^0,  A1 = gamma^0 gamma^1,  A4 = gamma^0 gamma^4.
  A0, A1, A4 generate a Clifford algebra Cl(2,1) (A0^2 = 1, A1^2 = -1,
  A4^2 = 1, pairwise anticommuting) whose centre contains
      J = A0 A1 A4 = gamma^0 gamma^1 gamma^4      (real symmetric, J^2 = 1, trace 0).
  The operators K1 = gamma^2 gamma^3 and K2 = gamma^5 gamma^6 (real
  antisymmetric, squares -1) commute with A0, A1, A4, J, C, B and with each
  other.  For every label (s, c1, c2) in {+1,-1}^3 the product
      P = (1 + s J)/2 (1 + c1 i K1)/2 (1 + c2 i K2)/2 (1 + A0)/2
  is an exact rank-1 projector; v = 16 P e_j (first j with P e_j != 0) is a
  Gaussian-integer vector of squared norm 32, and w = A1 v completes the
  block.  In the orthonormal basis (v, w)/sqrt(32) of the eight blocks,
  ordered by label as (s, c1, c2) = (+,+,+), (+,+,-), (+,-,+), (+,-,-),
  (-,+,+), (-,+,-), (-,-,+), (-,-,-), the matrices are block-diagonal with
  the 2x2 blocks (sigma_x, sigma_y, sigma_z the Pauli matrices)
      A0 -> sigma_z,        A1 -> [[0,-1],[1,0]] = -i sigma_y,
      A4 -> -s sigma_x,     gamma^4 = A0 A4 -> -i s sigma_y,
      C  -> -c1 sigma_y,    B = -i C gamma^4 -> (c1 s) I_2,
      B C -> -s sigma_y,    gamma^4 gamma^1 -> s sigma_z,
      B C gamma^0 -> -i s sigma_x.
  Everything is verified EXACTLY here (Gaussian rationals with denominator
  32) and again numerically (to 1e-14) by the crate from the projectors.

The basis is written as Gaussian integers in units of sqrt(2)/8:
BLOCK_BASIS_RE[b][c][i] + i BLOCK_BASIS_IM[b][c][i] times sqrt(2)/8 is the
i-th component of column c (0 = v, 1 = w) of block b.

Prints check_<name>=true|false, measurement_<name>=..., check_count and
failed_check_count; writes the JSON report; exits 1 on any failure and
writes nothing then.  Options: --fixture, --output, --report, --check
(compare with the existing generated.rs, write nothing).
"""

import argparse
import hashlib
import json
import os
import sys

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIRECTORY)

import generate_dirac16complex_constants as stage3  # noqa: E402

REPOSITORY_ROOT = os.path.dirname(SCRIPT_DIRECTORY)
DEFAULT_OUTPUT = os.path.join(REPOSITORY_ROOT, "studies", "dirac16complex_kohn_sham",
                              "src", "generated.rs")
DEFAULT_REPORT = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex",
                              "kohn-sham", "rust", "generator-report.json")
GENERATOR = "scripts/generate_dirac16complex_ks_constants.py"
N16 = 16
LABELS = [(s, c1, c2) for s in (1, -1) for c1 in (1, -1) for c2 in (1, -1)]


# ---------------------------------------------------------------------------
# exact Gaussian-integer matrices: pairs (re, im) of integer matrices
# ---------------------------------------------------------------------------

def creal(a):
    return (a, stage3.zeros(len(a), len(a[0])))


def cmul(x, y):
    xr, xi = x
    yr, yi = y
    re = stage3.mat_add(stage3.mat_mul(xr, yr), stage3.mat_neg(stage3.mat_mul(xi, yi)))
    im = stage3.mat_add(stage3.mat_mul(xr, yi), stage3.mat_mul(xi, yr))
    return (re, im)


def cadd(x, y):
    return (stage3.mat_add(x[0], y[0]), stage3.mat_add(x[1], y[1]))


def cscale(re, im, x):
    """(re + i im) * x for integers re, im."""
    xr, xi = x
    return (stage3.mat_add(stage3.mat_scale(re, xr), stage3.mat_scale(-im, xi)),
            stage3.mat_add(stage3.mat_scale(re, xi), stage3.mat_scale(im, xr)))


def cdagger(x):
    return (stage3.transpose(x[0]), stage3.mat_neg(stage3.transpose(x[1])))


def ceq(x, y):
    return x[0] == y[0] and x[1] == y[1]


def czero(x):
    return x[0] == stage3.zeros(len(x[0]), len(x[0][0])) and x[1] == stage3.zeros(len(x[1]), len(x[1][0]))


def block_form(basis32, x):
    """Y = V^dagger X V with V = basis32 / sqrt(32); returns 32 Y exactly and
    checks that Y is 2x2 block diagonal.  basis32: complex 16x16 (columns)."""
    y32 = cmul(cmul(cdagger(basis32), x), basis32)
    off = all(y32[0][i][j] == 0 and y32[1][i][j] == 0
              for i in range(N16) for j in range(N16) if i // 2 != j // 2)
    blocks = []
    for b in range(8):
        blocks.append([[(y32[0][2 * b + p][2 * b + q], y32[1][2 * b + p][2 * b + q])
                        for q in range(2)] for p in range(2)])
    return off, blocks


def pauli(name, factor_re, factor_im):
    """32 * (factor) * sigma as ((re, im) entries); factor = factor_re + i factor_im."""
    sig = {"x": [[(0, 0), (1, 0)], [(1, 0), (0, 0)]],
           "y": [[(0, 0), (0, -1)], [(0, 1), (0, 0)]],
           "z": [[(1, 0), (0, 0)], [(0, 0), (-1, 0)]],
           "1": [[(1, 0), (0, 0)], [(0, 0), (1, 0)]]}[name]
    out = []
    for row in sig:
        out.append([(32 * (factor_re * e[0] - factor_im * e[1]),
                     32 * (factor_re * e[1] + factor_im * e[0])) for e in row])
    return out


def build_blocks(gammas):
    g = [creal(x) for x in gammas]
    ident = creal(stage3.eye(N16))
    a0 = g[0]
    a1 = cmul(g[0], g[1])
    a4 = cmul(g[0], g[4])
    jmat = cmul(cmul(a0, a1), a4)
    k1 = cmul(g[2], g[3])
    k2 = cmul(g[5], g[6])
    c = cmul(cmul(g[0], g[1]), cmul(g[2], g[3]))
    b = cscale(0, -1, cmul(c, g[4]))
    checks = []
    checks.append(("J_real_symmetric_involution",
                   czero((jmat[1], jmat[1])) and jmat[0] == stage3.transpose(jmat[0])
                   and ceq(cmul(jmat, jmat), ident)))
    checks.append(("J_traceless", sum(jmat[0][i][i] for i in range(N16)) == 0))
    checks.append(("K1_K2_square_minus_one",
                   ceq(cmul(k1, k1), cscale(-1, 0, ident)) and ceq(cmul(k2, k2), cscale(-1, 0, ident))))
    gens = {"A0": a0, "A1": a1, "A4": a4}
    cl = ceq(cmul(a0, a0), ident) and ceq(cmul(a1, a1), cscale(-1, 0, ident)) \
        and ceq(cmul(a4, a4), ident) \
        and czero(cadd(cmul(a0, a1), cmul(a1, a0))) \
        and czero(cadd(cmul(a0, a4), cmul(a4, a0))) \
        and czero(cadd(cmul(a1, a4), cmul(a4, a1)))
    checks.append(("A0_A1_A4_clifford_2_1", cl))
    labels_ops = {"J": jmat, "K1": k1, "K2": k2}
    commuting = all(czero(cadd(cmul(x, y), cscale(-1, 0, cmul(y, x))))
                    for x in list(labels_ops.values()) + [a0]
                    for y in list(labels_ops.values()) + [a0])
    commuting = commuting and all(czero(cadd(cmul(x, y), cscale(-1, 0, cmul(y, x))))
                                  for x in list(gens.values()) + [c, b]
                                  for y in labels_ops.values())
    checks.append(("labels_commute_with_generators_C_B", commuting))
    basis_re = stage3.zeros(N16, N16)
    basis_im = stage3.zeros(N16, N16)
    block_vectors = []
    rank_ok = True
    norm_ok = True
    for index, (s, c1, c2) in enumerate(LABELS):
        p16 = cmul(cmul(cadd(ident, cscale(s, 0, jmat)), cadd(ident, cscale(0, c1, k1))),
                   cmul(cadd(ident, cscale(0, c2, k2)), cadd(ident, a0)))
        # rank 1: every column is a multiple of the first nonzero one; check by
        # P^2 = 16 P (projector) and trace = 16.
        rank_ok = rank_ok and ceq(cmul(p16, p16), cscale(16, 0, p16)) \
            and sum(p16[0][i][i] for i in range(N16)) == 16 \
            and sum(p16[1][i][i] for i in range(N16)) == 0
        col = None
        for j in range(N16):
            if any(p16[0][i][j] != 0 or p16[1][i][j] != 0 for i in range(N16)):
                col = j
                break
        v_re = [p16[0][i][col] for i in range(N16)]
        v_im = [p16[1][i][col] for i in range(N16)]
        norm2 = sum(x * x + y * y for x, y in zip(v_re, v_im))
        norm_ok = norm_ok and norm2 == 32
        w = cmul(a1, ([[x] for x in v_re], [[x] for x in v_im]))
        w_re = [w[0][i][0] for i in range(N16)]
        w_im = [w[1][i][0] for i in range(N16)]
        for i in range(N16):
            basis_re[i][2 * index] = v_re[i]
            basis_im[i][2 * index] = v_im[i]
            basis_re[i][2 * index + 1] = w_re[i]
            basis_im[i][2 * index + 1] = w_im[i]
        block_vectors.append(((v_re, v_im), (w_re, w_im), col))
    checks.append(("projectors_rank_one_trace_16", rank_ok))
    checks.append(("basis_vectors_norm2_32", norm_ok))
    basis32 = (basis_re, basis_im)
    gram = cmul(cdagger(basis32), basis32)
    checks.append(("basis_orthonormal", ceq(gram, cscale(32, 0, ident))))
    expected = {
        "A0": lambda s, c1, c2: pauli("z", 1, 0),
        "A1": lambda s, c1, c2: pauli("y", 0, -1),
        "A4": lambda s, c1, c2: pauli("x", -s, 0),
        "gamma4": lambda s, c1, c2: pauli("y", 0, -s),
        "C": lambda s, c1, c2: pauli("y", -c1, 0),
        "B": lambda s, c1, c2: pauli("1", c1 * s, 0),
        "BC": lambda s, c1, c2: pauli("y", -s, 0),
        "gamma4gamma1": lambda s, c1, c2: pauli("z", s, 0),
        "BCgamma0": lambda s, c1, c2: pauli("x", 0, -s),
    }
    operators = {
        "A0": a0, "A1": a1, "A4": a4, "gamma4": g[4], "C": c, "B": b,
        "BC": cmul(b, c), "gamma4gamma1": cmul(g[4], g[1]), "BCgamma0": cmul(cmul(b, c), g[0]),
    }
    forms = {}
    for name, op in operators.items():
        off, blocks = block_form(basis32, op)
        same = off and all(blocks[i] == expected[name](*LABELS[i]) for i in range(8))
        checks.append(("block_form_%s" % name, same))
        forms[name] = blocks
    return checks, basis32, block_vectors, forms


# ---------------------------------------------------------------------------
# rendering
# ---------------------------------------------------------------------------

def render_stage4(gammas, c, chir, b_imag, sha256, source, block_vectors):
    text = stage3.render(gammas, c, chir, b_imag, sha256, source)
    text = text.replace("// Generated by %s." % stage3.GENERATOR,
                        "// Generated by %s (Stage 4; gamma part via %s)."
                        % (GENERATOR, stage3.GENERATOR))
    lines = [
        "",
        "// Exact 2x2 block reduction of the Kohn-Sham equation (STAGE4_SPEC",
        "// section 2).  Block b has the label (s, c1, c2) = BLOCK_LABELS[b] with",
        "// J = gamma^0 gamma^1 gamma^4 = s, i gamma^2 gamma^3 = c1, i gamma^5 gamma^6 = c2",
        "// on the block.  Column 0 of block b is v = 16 P e_j (P the rank-1 joint",
        "// projector with gamma^0 = +1), column 1 is w = gamma^0 gamma^1 v; both are",
        "// Gaussian integers of squared norm 32, i.e. the orthonormal basis vector",
        "// is (BLOCK_BASIS_RE + i BLOCK_BASIS_IM) * BLOCK_BASIS_UNIT, with",
        "// BLOCK_BASIS_UNIT = sqrt(2)/8 = 1/sqrt(32).",
        "pub const BLOCK_COUNT: usize = 8;",
        "pub const BLOCK_BASIS_UNIT_SQUARED_INVERSE: f64 = 32.0;",
        "#[rustfmt::skip]",
        "pub const BLOCK_LABELS: [[i32; 3]; BLOCK_COUNT] = [%s];"
        % ", ".join("[%d, %d, %d]" % lab for lab in LABELS),
        "#[rustfmt::skip]",
        "pub const BLOCK_SOURCE_COLUMN: [usize; BLOCK_COUNT] = [%s];"
        % ", ".join(str(col) for _, _, col in block_vectors),
    ]
    for part, name in ((0, "BLOCK_BASIS_RE"), (1, "BLOCK_BASIS_IM")):
        lines.append("#[rustfmt::skip]")
        lines.append("pub const %s: [[[f64; SPINOR_DIMENSION]; 2]; BLOCK_COUNT] = [" % name)
        for v, w, _col in block_vectors:
            lines.append("    [")
            for vec in (v, w):
                lines.append("        [%s]," % ", ".join(stage3.render_value(x) for x in vec[part]))
            lines.append("    ],")
        lines.append("];")
    return text + "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--fixture", default=stage3.DEFAULT_FIXTURE)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--report", default=DEFAULT_REPORT)
    parser.add_argument("--check", action="store_true")
    arguments = parser.parse_args(argv)

    gammas = stage3.contract_gammas()
    checks = []
    measurements = {}
    source_sha = {}
    if not os.path.exists(arguments.fixture):
        print("REFUSED: fixture %s is absent (Stage 4 requires it)" % arguments.fixture)
        return 1
    try:
        data, fixture = stage3.read_fixture(arguments.fixture)
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print("REFUSED: cannot read fixture: %s" % error)
        return 1
    sha256 = hashlib.sha256(data).hexdigest()
    source_sha[stage3.FIXTURE_RELATIVE] = sha256
    checks.append(("fixture_gammas_match_contract_construction",
                   all(fixture["gamma"][a] == gammas[a] for a in range(8))))
    stage3_checks, c, chir, b_imag = stage3.verify(gammas)
    checks.extend(("stage3_" + name, passed) for name, passed in stage3_checks)
    if "C" in fixture:
        checks.append(("fixture_C_matches", fixture["C"] == c))
    if "chirality" in fixture:
        checks.append(("fixture_chirality_matches", fixture["chirality"] == chir))
    if "B_imag" in fixture:
        checks.append(("fixture_B_matches", fixture["B_real"] == stage3.zeros(N16)
                       and fixture["B_imag"] == b_imag))
    block_checks, basis32, block_vectors, forms = build_blocks(gammas)
    checks.extend(block_checks)
    measurements["blockLabels"] = [list(lab) for lab in LABELS]
    measurements["basisUnit"] = "sqrt(2)/8"
    measurements["basisSquaredNorm"] = 32
    measurements["blockForms32"] = {
        name: [[[list(e) for e in row] for row in blk] for blk in blocks]
        for name, blocks in forms.items()}
    measurements["blockFormsSymbolic"] = {
        "A0": "sigma_z", "A1": "-i sigma_y = [[0,-1],[1,0]]", "A4": "-s sigma_x",
        "gamma4": "-i s sigma_y", "C": "-c1 sigma_y", "B": "c1 s I_2", "BC": "-s sigma_y",
        "gamma4gamma1": "s sigma_z", "BCgamma0": "-i s sigma_x"}

    failed = 0
    for name, passed in checks:
        print("check_%s=%s" % (name, "true" if passed else "false"))
        failed += 0 if passed else 1
    print("measurement_fixture_sha256=%s" % sha256)
    print("measurement_block_labels=%s" % json.dumps(measurements["blockLabels"]))
    print("check_count=%d" % len(checks))
    print("failed_check_count=%d" % failed)
    if failed:
        print("REFUSED: exact verification failed; nothing written")
        return 1

    text = render_stage4(gammas, c, chir, b_imag, sha256, "fixture", block_vectors)
    payload = text.encode("utf-8")
    if arguments.check:
        existing = b""
        if os.path.exists(arguments.output):
            with open(arguments.output, "rb") as handle:
                existing = handle.read()
        same = existing == payload
        print("generated_up_to_date=%s" % ("true" if same else "false"))
        return 0 if same else 1
    os.makedirs(os.path.dirname(os.path.abspath(arguments.output)), exist_ok=True)
    with open(arguments.output, "wb") as handle:
        handle.write(payload)
    print("output=%s" % os.path.abspath(arguments.output).replace("\\", "/"))
    print("output_sha256=%s" % hashlib.sha256(payload).hexdigest())
    source_sha["studies/dirac16complex_kohn_sham/src/generated.rs"] = hashlib.sha256(payload).hexdigest()
    report = {
        "schemaVersion": 1,
        "producer": GENERATOR,
        "checks": {name: passed for name, passed in checks},
        "measurements": measurements,
        "sourceSha256": source_sha,
    }
    os.makedirs(os.path.dirname(os.path.abspath(arguments.report)), exist_ok=True)
    with open(arguments.report, "wb") as handle:
        handle.write((json.dumps(report, indent=2) + "\n").encode("utf-8"))
    print("report=%s" % os.path.abspath(arguments.report).replace("\\", "/"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
