#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Stage 1 summary of the dirac16complex arbitrary-field verification.

Reads the five Stage 1 reports in artifacts/dirac16complex/arbitrary-field/

    wolfram-algebra-report.json   (scripts/verify_dirac16complex_algebra.wls)
    wolfram-geometry-report.json  (scripts/verify_dirac16complex_geometry.wls)
    python-algebra-report.json    (scripts/check_dirac16complex_algebra.py)
    python-geometry-report.json   (scripts/check_dirac16complex_geometry.py)
    grassmann-demo-report.json    (scripts/demo_grassmann_lagrangians.py)

and the exact fixture algebra-fixture.json, and writes stage1-summary.json with

    schemaVersion, reports (path, sha256, producer), checks (the union of all checks,
    each name prefixed by its producer), counts per producer, the cross-implementation
    comparison tables (ALG_wolframAgreement, GEO_wolframAgreement), the agreed key
    measurements (each value read from every report that computes it and compared here
    again), the items that agree only after a notation conversion (stated, not computed),
    and the list of disagreements (empty on success).

It computes nothing new about the physics: every value comes from a report, and every
"agreed" entry is re-compared across the reports by this script.  Exit status 0 only if
every check of every report is true, both agreement checks are present and true, and no
key measurement disagrees.  Standard library only; deterministic LF output.

Usage (from any directory):  python scripts/build_stage1_summary.py [--output PATH]
"""

import argparse
import hashlib
import json
import os
import sys
from fractions import Fraction

REPOSITORY_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACTS = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex", "arbitrary-field")
DEFAULT_OUTPUT = os.path.join(ARTIFACTS, "stage1-summary.json")
PRODUCER = "scripts/build_stage1_summary.py"
REPORTS = (
    ("wolfram-algebra", "wolfram-algebra-report.json"),
    ("wolfram-geometry", "wolfram-geometry-report.json"),
    ("python-algebra", "python-algebra-report.json"),
    ("python-geometry", "python-geometry-report.json"),
    ("grassmann-demo", "grassmann-demo-report.json"),
)
FIXTURE = "algebra-fixture.json"
REQUIRED_AGREEMENT_CHECKS = (
    ("python-algebra", "ALG_wolframAgreement"),
    ("python-geometry", "GEO_wolframAgreement"),
    ("wolfram-algebra", "ALG_fixtureAgreement"),
    ("python-algebra", "ALG_fixtureAgreement"),
)
G1_POINTS = ("p1", "p2", "p3")


def relative(path):
    return os.path.relpath(path, REPOSITORY_ROOT).replace("\\", "/")


def load(path):
    with open(path, "rb") as handle:
        data = handle.read()
    return json.loads(data.decode("utf-8")), hashlib.sha256(data).hexdigest()


def canon(value):
    """Canonical JSON-like value: exact rationals as reduced "p/q" strings or ints, tuples as lists."""
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, Fraction):
        return int(value) if value.denominator == 1 else "%d/%d" % (value.numerator, value.denominator)
    if isinstance(value, str):
        text = value.strip()
        try:
            number = Fraction(text)
        except (ValueError, ZeroDivisionError):
            return text
        return canon(number)
    if isinstance(value, (list, tuple)):
        return [canon(item) for item in value]
    if isinstance(value, dict):
        return {str(key): canon(item) for key, item in value.items()}
    return value


def triple(text):
    return [int(v) for v in str(text).replace("{", " ").replace("}", " ").replace("(", " ")
            .replace(")", " ").replace(",", " ").split()]


def is_true(value):
    return value is True or value == "true"


class Summary:
    def __init__(self):
        self.agreed = []
        self.disagreements = []

    def agree(self, name, sources, statement=None):
        """Record one key measurement; `sources` maps 'report:key' -> value (compared canonically)."""
        values = {label: canon(value) for label, value in sources.items()}
        distinct = []
        for value in values.values():
            if value not in distinct:
                distinct.append(value)
        entry = {"measurement": name, "agree": len(distinct) == 1 and len(values) >= 2,
                 "value": distinct[0] if len(distinct) == 1 else None, "sources": sorted(values)}
        if statement:
            entry["statement"] = statement
        if not entry["agree"]:
            entry["values"] = values
            self.disagreements.append({"measurement": name, "values": values})
        self.agreed.append(entry)


def key_measurements(summary, reports, fixture):
    wa = reports["wolfram-algebra"]["measurements"]
    pa = reports["python-algebra"]["measurements"]
    wg = reports["wolfram-geometry"]["measurements"]
    pg = reports["python-geometry"]["measurements"]
    wgc = reports["wolfram-geometry"]["checks"]
    pgc = reports["python-geometry"]["checks"]
    add = summary.agree

    # --- algebra: intertwiners, chirality, forms, dimensions, signatures -----------------------------
    add("K_clifford (primitive integer solution of gammaHat^a K = K gamma^a)",
        {"wolfram-algebra:K_clifford": wa["K_clifford"], "python-algebra:K_clifford": pa["K_clifford"],
         "algebra-fixture:K_clifford": fixture["K_clifford"]})
    add("K_octonion (primitive integer solution of gamma^a K = K Gamma(e_a))",
        {"wolfram-algebra:K_octonion": wa["K_octonion"], "python-algebra:K_octonion": pa["K_octonion"],
         "algebra-fixture:K_octonion": fixture["K_octonion"]})
    add("intertwiner dimension and rank (K_clifford, K_octonion)",
        {"wolfram-algebra": [wa["ALG_cliffordPictureIntertwiner.intertwinerDimension"],
                             wa["ALG_cliffordPictureIntertwiner.rank"],
                             wa["ALG_octonionPictureIntertwiner.intertwinerDimension"],
                             wa["ALG_octonionPictureIntertwiner.rank"]],
         "python-algebra": [pa["ALG_cliffordIntertwinerDimension"], pa["ALG_cliffordIntertwinerRank"],
                            pa["ALG_octonionIntertwinerDimension"], pa["ALG_octonionIntertwinerRank"]]})
    add("chirality gamma^8 diagonal", {"wolfram-algebra:chiralityDiagonal": wa["chiralityDiagonal"],
                                       "python-algebra:ALG_chiralityDiagonal": pa["ALG_chiralityDiagonal"]})
    add("volume element sign: K gamma^8 K^-1 = (sign) G(x)G(x)G(x)G",
        {"wolfram-algebra:volumeElementSign": wa["volumeElementSign"],
         "python-algebra:ALG_cliffordKChiralityKinvSignVsGGGG": pa["ALG_cliffordKChiralityKinvSignVsGGGG"]})
    add("signature (n+, n-, n0) of C = sigma16",
        {"wolfram-algebra": wa["ALG_chargeMatrix.signature"] + [wa["ALG_chargeMatrix.zeroEigenvalues"]],
         "python-algebra": pa["ALG_chargeMatrixSignature"]})
    add("eigenvalue multiplicities of B = -i C gamma^4",
        {"wolfram-algebra": {"plus1": wa["ALG_chargeFormB.eigenvalues"].count(1),
                             "minus1": wa["ALG_chargeFormB.eigenvalues"].count(-1)},
         "python-algebra": pa["ALG_chargeFormBEigenvalueMultiplicities"]})
    add("Clifford algebra ranks (full, even)",
        {"wolfram-algebra": [wa["ALG_faithful.fullRank"], wa["ALG_faithful.evenRank"]],
         "python-algebra": [pa["ALG_fullAlgebraRank"], pa["ALG_evenAlgebraRank"]]})
    add("commutant dimension of Pin(4,4) on C^16 (irreducible)",
        {"wolfram-algebra": wa["ALG_pinIrreducibleComplex.commutantDimension"],
         "python-algebra": pa["ALG_pinCommutantDimensionQ"]})
    add("commutant dimension of Spin(4,4) on C^16; block commutants; cross intertwiners (C^8_- + C^8_+ inequivalent)",
        {"wolfram-algebra": [wa["ALG_spinDecomposition.spinCommutantDimension"],
                             wa["ALG_spinDecomposition.blockCommutantDimensions"],
                             wa["ALG_spinDecomposition.crossIntertwinerDimensions"]],
         "python-algebra": [pa["ALG_spinCommutantDimensionQ"],
                            [pa["ALG_spinMinusBlockCommutantDimension"], pa["ALG_spinPlusBlockCommutantDimension"]],
                            [pa["ALG_spinCrossIntertwinerDimension"], pa["ALG_spinCrossIntertwinerDimensionReverse"]]]})
    add("dimension of the Spin(4,4)-invariant bilinear forms (spanned by C P-, C P+)",
        {"wolfram-algebra": wa["ALG_invariantForms.invariantBilinearFormDimension"],
         "python-algebra": pa["ALG_invariantFormDimensionQ"]})
    add("B-signature on the +1 and -1 eigenspaces of -i gamma^4 (Krein structure)",
        {"wolfram-algebra": [wa["QNT_kreinSignature.restPositiveFrequency"]["signature"],
                             wa["QNT_kreinSignature.restNegativeFrequency"]["signature"]],
         "python-algebra": [pa["QNT_kreinBSignatureOnPlusEigenspace"], pa["QNT_kreinBSignatureOnMinusEigenspace"]]})
    add("S^ab commuting with B (CONTRACT.md section 11, E1: 13 = so(4)+so(3) and the 4 boosts S^{b4})",
        {"wolfram-algebra": sorted(wa["QNT_unitaryAndKreinSubgroups.generatorsCommutingWithB"]),
         "python-algebra": sorted(pa["QNT_generatorsCommutingWithB"])})
    add("S^ab commuting with B and anti-Hermitian (unitarily implemented Spin(4) x Spin(3))",
        {"wolfram-algebra": sorted(wa["QNT_unitaryAndKreinSubgroups.commutingWithBAndAntiHermitian"]),
         "python-algebra": sorted(pa["QNT_unitaryGenerators"])})
    add("number of Krein-unitary S^ab (a,b != 4) and of Hilbert-anti-Hermitian S^ab",
        {"wolfram-algebra": [wa["QNT_unitaryAndKreinSubgroups.countKreinAntiHermitian"],
                             wa["QNT_unitaryAndKreinSubgroups.countHilbertAntiHermitian"]],
         "python-algebra": [pa["QNT_kreinGeneratorCount"], pa["QNT_antiHermitianGeneratorCount"]]})
    add("literal claim 'exactly 9 S^ab commute with B' (recorded false in both)",
        {"wolfram-algebra": wa["QNT_unitaryAndKreinSubgroups.literalClaimExactlyNineCommuteWithB"],
         "python-algebra": pa["QNT_literalClaimExactlyNineCommuteWithB"]})
    add("gamma^8 map signs (kinetic, mass)",
        {"wolfram-algebra": [sorted(set(wa["ALG_gamma8Map.kineticMatrixSigns"])), wa["ALG_gamma8Map.massMatrixSign"]],
         "python-algebra": [[pa["ALG_gamma8MapKineticSign"]], pa["ALG_gamma8MapMassSign"]]})

    # --- geometry --------------------------------------------------------------------------------------
    lich = {"wolfram-geometry:G1.%s.lichnerowiczC" % p: wg["G1.%s.lichnerowiczC" % p] for p in G1_POINTS}
    lich.update({"wolfram-geometry:G2.%s.lichnerowiczC" % p: wg["G2.%s.lichnerowiczC" % p] for p in G1_POINTS})
    lich.update({"python-geometry:GEO_lichnerowicz_c_G1_%s" % p: pg["GEO_lichnerowicz_c_G1_%s" % p] for p in G1_POINTS})
    lich["python-geometry:GEO_lichnerowicz_c_G2"] = pg["GEO_lichnerowicz_c_G2"]
    add("Lichnerowicz constant c in (gamma^mu D_mu)^2 = g^{mu nu} nabla_mu D_nu + c R", lich,
        "c = -1/4 with {gamma^a, gamma^b} = 2 eta^{ab}, R = g^{sigma nu} R^rho_{sigma rho nu}; c = +1/4 fails")
    curv = {}
    for p in G1_POINTS:
        curv["wolfram-geometry:G1.%s" % p] = [is_true(wg["G1.%s.curvatureCandidate.plusHalfLowered" % p]),
                                              is_true(wg["G1.%s.curvatureCandidate.minusHalfLowered" % p])]
        curv["wolfram-geometry:G2.%s" % p] = [is_true(wg["G2.%s.curvatureCandidate.plusHalfLowered" % p]),
                                              is_true(wg["G2.%s.curvatureCandidate.minusHalfLowered" % p])]
        curv["python-geometry:G1_%s" % p] = [pg["GEO_curvature_spinCurvaturePlusHalfRiemannS_G1_%s" % p],
                                             pg["GEO_curvature_spinCurvatureMinusHalfRiemannS_G1_%s" % p]]
    curv["python-geometry:G2"] = [pg["GEO_curvature_spinCurvaturePlusHalfRiemannS_G2"],
                                  pg["GEO_curvature_spinCurvatureMinusHalfRiemannS_G2"]]
    add("spin curvature F_{mu nu} = +(1/2) R S (holds), -(1/2) R S (fails)", curv,
        "F_{mu nu} = d_mu Omega_nu - d_nu Omega_mu + [Omega_mu, Omega_nu] = +(1/2) eta_ac e_rho^c R^rho_{sigma mu nu} "
        "e_b^sigma S^{ab}")
    formula = "T_{mu nu} = -(2/sqrt|g|) dS/dg^{mu nu}"
    add("EMT sign convention: " + formula + " equals the CONTRACT section 7 covariant formula (T_44 = rho = m S + U)",
        {"wolfram-geometry:emt.signConvention+EMT_variation_G3":
             [formula in wg["emt.signConvention"], wgc["EMT_variation_G3"]],
         "python-geometry:EMT_signConvention+EMT_variation": [formula in pg["EMT_signConvention"], pgc["EMT_variation"]]})
    trace_tokens = ("-mS+7SU'-8U", "-mS+3lamS^2")

    def trace_form(text):
        norm = str(text).replace(" ", "").replace("(S)", "").replace("lambda", "lam")
        return [token in norm for token in trace_tokens]
    add("on-shell EMT trace T^mu_mu = -m S + 7 S U' - 8 U (= -m S + 3 lambda S^2 for U = lambda S^2/2)",
        {"wolfram-geometry:emt.trace+EMT_trace_G1+EMT_trace_G2":
             trace_form(wg["emt.trace"]) + [wgc["EMT_trace_G1"], wgc["EMT_trace_G2"]],
         "python-geometry:EMT_traceStatement+EMT_trace_G1+EMT_trace_G2":
             trace_form(pg["EMT_traceStatement"]) + [pgc["EMT_trace_G1"], pgc["EMT_trace_G2"]]})
    for p in G1_POINTS:
        add("G1 %s: metric inertia, det e, g^44 and R (exact)" % p,
            {"wolfram-geometry": [triple(wg["G1.%s.metricInertia" % p]), wg["G1.%s.detFrame" % p],
                                  wg["G1.%s.inverseMetric44" % p], wg["G1.%s.scalarCurvature" % p]],
             "python-geometry": [triple(pg["GEO_metricSignature_G1_%s" % p]), pg["GEO_detVielbein_G1_%s" % p],
                                 pg["GEO_inverseMetric44_G1_%s" % p], pg["GEO_ricciScalar_G1_%s" % p]]},
            "R decimal (Wolfram report) = %s" % wg["G1.%s.scalarCurvatureDecimal" % p])
    counts = {}
    for p in G1_POINTS:
        counts["wolfram-geometry:G1.%s" % p] = [wg["G1.%s.nonzeroOmegaLower" % p],
                                                wg["G1.%s.nonzeroOmegaMixedSymmetricPart" % p],
                                                wg["G1.%s.notebookDGammaNonzeroEntries" % p]]
        counts["python-geometry:G1_%s" % p] = [pg["GEO_nonzeroOmegaLowComponents_G1_%s" % p],
                                               pg["GEO_nonzeroOmegaMixedSymmetricPart_G1_%s" % p],
                                               pg["GEO_notebookContraction_nonzeroEntries_DmuGammaNu_G1_%s" % p]]
    add("G1 nonzero counts: omega_{mu ab}, symmetric part of omega_mu^a_b, D_mu gamma^nu with the notebook contraction",
        counts)
    counts = {"wolfram-geometry:G2.%s" % p: [wg["G2.%s.nonzeroOmegaLower" % p],
                                             wg["G2.%s.nonzeroOmegaMixedSymmetricPart" % p],
                                             wg["G2.%s.notebookDGammaNonzeroEntries" % p]] for p in G1_POINTS}
    counts["python-geometry:G2"] = [pg["GEO_nonzeroOmegaLowComponents_G2"], pg["GEO_nonzeroOmegaMixedSymmetricPart_G2"],
                                    pg["GEO_notebookContraction_nonzeroEntries_DmuGammaNu_G2"]]
    add("G2 nonzero counts: omega_{mu ab}, symmetric part of omega_mu^a_b, D_mu gamma^nu with the notebook contraction",
        counts)
    # G2: Python symbolic results evaluated at the Wolfram points are compared row by row in
    # GEO_wolframAgreement; here the per-point verdicts are collected.
    rows = {row["measurement"]: row for row in pg.get("GEO_wolframSharedMeasurements", [])}
    for label, statement in (
            ("R", "R = 6 H^2 (a4'^2 - 7) (Python, symbolic) at the three exact Wolfram points"),
            ("sqrt|g|", "sqrt|g| = cos z (Python, symbolic) at the three exact Wolfram points"),
            ("notebook gamma^mu Omega_mu, gamma^0 coefficient", "notebook contraction: gamma^0 coefficient 3H/2"),
            ("notebook gamma^mu Omega_mu, gamma^4 coefficient", "notebook contraction: gamma^4 coefficient 3 H a4'/2")):
        # the exact comparison (radical simplification of the difference) was done by
        # GEO_wolframAgreement; its per-row verdict is required here for all three points
        values = {}
        for p in G1_POINTS:
            row = rows.get("G2.%s %s" % (p, label), {})
            values["G2.%s" % p] = [row.get("wolfram", "missing row"), row.get("python", "missing row")]
        ok = all(rows.get("G2.%s %s" % (p, label), {}).get("agree") is True for p in G1_POINTS)
        entry = {"measurement": "G2 " + label, "agree": ok, "value": {k: v[0] for k, v in values.items()},
                 "sources": ["python-geometry:GEO_wolframSharedMeasurements", "wolfram-geometry"],
                 "statement": statement}
        if not ok:
            entry["values"] = values
            summary.disagreements.append({"measurement": "G2 " + label, "values": values})
        summary.agreed.append(entry)


NOTATION_EQUIVALENCES = (
    {"measurement": "homogeneous Bianchi-I off-diagonal T_ij",
     "wolfram-geometry": "T_ij = (1/4)(H_i - H_j) Psibar gamma_i gamma_j gamma^4 Psi (curved gammas, gamma_i = g_ii gamma^i)",
     "python-geometry": "T_ij = +(1/4) eps_i eps_j h_i h_j (H_i - H_j) Psibar gamma^(i) gamma^(j) gamma^(4) Psi (flat gammas)",
     "conversion": "diagonal e = diag(h), g_ii = eps_i h_i^2, curved gamma^i = gamma^(i)/h_i, so gamma_i = eps_i h_i gamma^(i) "
                   "and gamma^4 = gamma^(4) (h_4 = N = 1): the two forms are identical",
     "method": "notation conversion by hand (both implementations verify their own form exactly)"},
    {"measurement": "homogeneous Bianchi-I T_4i",
     "wolfram-geometry": "T_4i = -(1/4)(Psibar gamma_i d_4 Psi - d_4 Psibar gamma_i Psi) off shell, 0 on shell",
     "python-geometry": "T_4i = -(1/4) eps_i h_i (Psibar gamma^(i) d_4 Psi - d_4 Psibar gamma^(i) Psi), 0 on shell",
     "conversion": "gamma_i = eps_i h_i gamma^(i) as above",
     "method": "notation conversion by hand"},
    {"measurement": "Riemann index placement in F = (1/2) R S",
     "wolfram-geometry": "R_{mu nu a b} := eta_ac e_rho^c R^rho_{sigma mu nu} e_b^sigma",
     "python-geometry": "R_{ab mu nu} = eta_ac e_r^c R^r_{s mu nu} e_b^s",
     "conversion": "the same object with the index groups written in the opposite order",
     "method": "notation comparison by hand; the +1/2 sign agreement is computed (see agreedMeasurements)"},
    {"measurement": "check names for the tetrad variation and the homogeneous reduction",
     "wolfram-geometry": "EMT_variation_G3, EMT_homogeneousReduction_G3",
     "python-geometry": "EMT_variation, EMT_homogeneousReduction (same G3 frame and points)",
     "conversion": "naming only; both verdicts are true",
     "method": "naming"},
)

NOT_COMPARABLE = (
    "Field-dependent values (EMT traces, rho, p, KE, PE at the test points) are not compared: the two "
    "implementations draw independent exact random field jets and parameters (m, lambda) from their own recorded "
    "seeds; they are compared only through the formulas both verify (see agreedMeasurements).",
    "G2 is evaluated by Wolfram at three exact points and by Python at a fully symbolic point; the comparison "
    "evaluates the Python expressions at the Wolfram points.",
)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    arguments = parser.parse_args(argv)

    reports, meta = {}, {}
    for prefix, name in REPORTS:
        path = os.path.join(ARTIFACTS, name)
        if not os.path.exists(path):
            print("error=missing report %s" % relative(path))
            return 2
        document, digest = load(path)
        if document.get("schemaVersion") != 1 or not isinstance(document.get("checks"), dict):
            print("error=%s has no schemaVersion 1 checks object" % relative(path))
            return 2
        reports[prefix] = document
        meta[prefix] = {"path": relative(path), "sha256": digest, "producer": document.get("producer")}
    fixture, fixture_digest = load(os.path.join(ARTIFACTS, FIXTURE))

    checks, counts, failed = {}, {}, []
    for prefix, _ in REPORTS:
        values = reports[prefix]["checks"]
        passed = sum(1 for value in values.values() if value is True)
        counts[prefix] = {"checks": len(values), "passed": passed, "failed": len(values) - passed}
        for name, value in values.items():
            checks["%s:%s" % (prefix, name)] = value is True
            if value is not True:
                failed.append("%s:%s" % (prefix, name))
    missing = ["%s:%s" % pair for pair in REQUIRED_AGREEMENT_CHECKS
               if reports[pair[0]]["checks"].get(pair[1]) is not True]

    summary = Summary()
    try:
        key_measurements(summary, reports, fixture)
    except (KeyError, TypeError, IndexError, AttributeError) as error:
        summary.disagreements.append({"measurement": "key measurement extraction",
                                      "error": "%s: %s" % (type(error).__name__, error)})

    pam, pgm = reports["python-algebra"]["measurements"], reports["python-geometry"]["measurements"]
    comparisons = {
        "algebra (ALG_wolframAgreement, scripts/check_dirac16complex_algebra.py)": {
            "checkVerdict": reports["python-algebra"]["checks"].get("ALG_wolframAgreement"),
            "matrices": pam.get("wolframMatrixAgreement"),
            "sharedCheckNames": len(pam.get("wolframCheckNamesShared", [])),
            "sharedCheckVerdictDisagreements": pam.get("wolframCheckVerdictDisagreements"),
            "sharedMeasurements": pam.get("wolframSharedMeasurementCount"),
            "sharedMeasurementsAgreeing": pam.get("wolframSharedMeasurementsAgreeing"),
            "agreeingMeasurementLabels": [row["measurement"] for row in pam.get("wolframSharedMeasurements", [])
                                          if row.get("agree")],
            "wolframReportSha256": pam.get("wolframReportSha256"),
        },
        "geometry (GEO_wolframAgreement, scripts/check_dirac16complex_geometry.py)": {
            "checkVerdict": reports["python-geometry"]["checks"].get("GEO_wolframAgreement"),
            "sharedCheckNames": len(pgm.get("GEO_wolframCheckNamesShared", [])),
            "sharedCheckVerdictDisagreements": pgm.get("GEO_wolframCheckVerdictDisagreements"),
            "sharedMeasurements": pgm.get("GEO_wolframSharedMeasurementCount"),
            "sharedMeasurementsAgreeing": pgm.get("GEO_wolframSharedMeasurementsAgreeing"),
            "agreeingMeasurementLabels": [row["measurement"] for row in pgm.get("GEO_wolframSharedMeasurements", [])
                                          if row.get("agree")],
            "wolframReportSha256": pgm.get("GEO_wolframReportSha256"),
        },
        "fixture (ALG_fixtureAgreement, scripts/verify_dirac16complex_algebra.wls)":
            reports["wolfram-algebra"]["measurements"].get("fixtureAgreement.summary"),
    }
    hash_links = {
        "python-algebra:wolframReportSha256 == sha256(wolfram-algebra-report.json)":
            pam.get("wolframReportSha256") == meta["wolfram-algebra"]["sha256"],
        "python-geometry:GEO_wolframReportSha256 == sha256(wolfram-geometry-report.json)":
            pgm.get("GEO_wolframReportSha256") == meta["wolfram-geometry"]["sha256"],
        "python-algebra:ALG_fixtureSha256 == sha256(algebra-fixture.json)":
            pam.get("ALG_fixtureSha256") == fixture_digest,
    }
    stale = [name for name, ok in hash_links.items() if not ok]

    document = {
        "schemaVersion": 1,
        "producer": PRODUCER,
        "stage": "Stage 1: dirac16complex in an arbitrary gravitational field",
        "reports": meta,
        "fixture": {"path": relative(os.path.join(ARTIFACTS, FIXTURE)), "sha256": fixture_digest},
        "counts": dict(counts, total={"checks": len(checks), "passed": len(checks) - len(failed),
                                      "failed": len(failed)}),
        "checks": checks,
        "crossImplementationComparisons": comparisons,
        "reportHashLinks": hash_links,
        "agreedMeasurements": summary.agreed,
        "notationEquivalences": list(NOTATION_EQUIVALENCES),
        "notCompared": list(NOT_COMPARABLE),
        "canonicalDecisions": [
            "QNT_unitaryAndKreinSubgroups has one meaning in both implementations (CONTRACT.md section 11, E1): "
            "exactly 13 of the 28 S^ab commute with B (so(4)+so(3) and the 4 Hermitian boosts S^{b4}, b=0..3); "
            "exactly 9 commute with B and are anti-Hermitian (unitarily implemented Spin(4)xSpin(3)); the 21 with "
            "a,b != 4 are Krein-unitary, the 7 S^{4b} are not.  The literal claim 'exactly 9 commute with B' is "
            "recorded as false.",
            "WolframScript 1.14 drops '--' and every argument after it when used with -file; report paths are "
            "passed as plain positional arguments.",
        ],
        "failedChecks": failed,
        "missingAgreementChecks": missing,
        "staleReportLinks": stale,
        "disagreements": summary.disagreements,
    }
    data = (json.dumps(document, indent=2, ensure_ascii=True) + "\n").encode("utf-8")
    os.makedirs(os.path.dirname(os.path.abspath(arguments.output)), exist_ok=True)
    with open(arguments.output, "wb") as handle:
        handle.write(data)

    for prefix, _ in REPORTS:
        print("stage1_summary_%s=%d/%d" % (prefix, counts[prefix]["passed"], counts[prefix]["checks"]))
    print("stage1_summary_total=%d/%d" % (len(checks) - len(failed), len(checks)))
    print("stage1_summary_agreed_measurements=%d/%d" % (sum(1 for e in summary.agreed if e["agree"]),
                                                          len(summary.agreed)))
    for name in failed:
        print("stage1_summary_failed_check=" + name)
    for name in missing:
        print("stage1_summary_missing_agreement_check=" + name)
    for name in stale:
        print("stage1_summary_stale_link=" + name)
    for entry in summary.disagreements:
        print("stage1_summary_disagreement=" + json.dumps(entry, ensure_ascii=True)[:400])
    print("stage1_summary=%s" % relative(arguments.output))
    print("stage1_summary_sha256=%s" % hashlib.sha256(data).hexdigest())
    return 1 if (failed or missing or stale or summary.disagreements) else 0


if __name__ == "__main__":
    sys.exit(main())
