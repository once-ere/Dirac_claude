# SPDX-License-Identifier: GPL-3.0-or-later
"""Tests of the Stage-3 provenance document (dirac16complex dark-sector numerics).

Run from the repository root:
    python -m unittest tests.test_d16c_numerics_publication -v

The document provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md is built with
    python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md
into provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.{tex,pdf}; the edition
dirac16complex-dark-sector-numerics is registered in provenance/pdf-specifications.json.
pdflatex runs with the repository root as working directory, because the 25
figures are included by root-relative paths.

The tests pin the sha256 of the Markdown and of the LaTeX file, require that the
committed .tex is exactly the builder's output for the committed .md (with every
figure file checked on disk), that the registered PDF edition matches the committed
PDF, that the title, subtitle, sections and required phrases are present, that the
embedded figures are exactly the 17 notebook figures (with the sha256 recorded in
notebook-report.json) and the 8 Mathematica figures (as listed in
mathematica-report.json), and that the numbers, check counts and hashes the
document quotes agree with the committed Stage-3 outputs:
artifacts/dirac16complex/numerics/{exp1..exp5}/summary.json, the checker reports
python-check-report.json, exp3/fits.json, numerics-summary.json,
notebook-report.json and mathematica-report.json.

After an intended edit of the document: rebuild and register it with
    python scripts/build_provenance_pdf.py --register provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md
and update MARKDOWN_SHA256 and TEX_SHA256 below.  If the Stage-3 outputs change,
the agreement tests below name every quoted number that no longer matches.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
import unittest
import zlib
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import build_dissertation_tex as builder  # noqa: E402
from scripts import check_dissertation_pdf  # noqa: E402
from scripts import check_provenance_pdf  # noqa: E402

PROVENANCE = REPOSITORY_ROOT / "provenance"
MARKDOWN = PROVENANCE / "DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md"
TEX = PROVENANCE / "DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.tex"
PDF = PROVENANCE / "DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.pdf"
EDITION = "dirac16complex-dark-sector-numerics"
NUMERICS = REPOSITORY_ROOT / "artifacts" / "dirac16complex" / "numerics"
FIXTURE = REPOSITORY_ROOT / "artifacts" / "dirac16complex" / "arbitrary-field" / "algebra-fixture.json"
GENERATED_RS = REPOSITORY_ROOT / "studies" / "dirac16complex_cosmology" / "src" / "generated.rs"

MARKDOWN_SHA256 = "f17d42d373a850cf85ce8360f0599ebad203b86e358f3c9443a95147a5157b8e"
TEX_SHA256 = "81e3e416f26065e52e80a9f7b6a9038d3906124688e24b5d6ec6e74e44c1930d"

TITLE = ("dirac16complex and the dark sector: pressure, energy density and equation of "
         "state from numerical solutions")
SUBTITLE = ("Five CVODE experiments, their independent verification, and whether the "
            "framework is connected to dark matter or dark energy")
REQUIRED_SECTIONS = (
    "Abstract",
    "1. The question and the short answer",
    "2. Scope and non-claims",
    "3. Notation and conventions",
    "4. The framework",
    "5. Numerical method, software and verification strategy",
    "6. EXP-1: the frozen field in the primordial pair-creation background",
    "7. EXP-2: self-consistent 8-dimensional Einstein cosmology",
    "8. EXP-3: the condensate as late-time dark energy",
    "9. EXP-4: dirac16complex quanta as dark matter",
    "10. EXP-5: the extra-time instability",
    "11. Independent cross-checks: the Jupyter and Mathematica notebooks",
    "12. Synthesis: pressure, energy density, dark matter and dark energy",
    "13. Verification summary",
    "14. Files and hashes",
    "15. Reproduction",
    "16. Limitations",
)
EXPERIMENT_SUBSECTIONS = (
    "Purpose",
    "Equations solved",
    "Initial data and parameters",
    "Solver settings and statistics",
    "Results",
    "Verification",
    "Physical interpretation",
)
SYNTHESIS_SUBSECTIONS = (
    "12.1 How pressure and energy density behave and change",
    "12.2 Dark matter",
    "12.3 Dark energy: which mechanisms give negative pressure or $w<-1/3$",
    "12.4 Quantitative comparison with Unite",
    "12.5 Where the model fails",
    "12.6 The answer",
)
REQUIRED_PHRASES = (
    "CVODE",
    "pure-Rust SUNDIALS 7.8.0",
    "Unite",
    "Chevallier-Polarski-Linder",
    "thawing means $w_a<0$, freezing means $w_a>0$.",
    "The PDF's table of thawing and freezing models writes the opposite: "
    "thawing \"($w_a>0$)\" and freezing \"($w_a<0$)\".",
    "**None of the three rustSolveIt repositories (Win11 a8fdff45, macOS 5360157f, "
    "Linux 6f58e02e) contains a Mathematica notebook (.nb, .wl or .wls)**: this was "
    "verified by listing their full git trees, and each has 294 Jupyter notebooks.",
    "adapted from rustSolveIt planet_Mercury/notebook",
    "BSD-3-Clause per the rustSolveIt Cargo manifests; author once-ere",
    "modelled on dirac-main's notebooks/DiracTriality.nb",
    "RunProcess plus Import of CSV and RawJSON",
    "expectation-value rule",
    "Krein",
    "Lagrangian split",
    "Hamiltonian split",
    "sound speed",
    "gradient instability",
    "8D energy bound",
    "lunar-laser-ranging",
    "4D energy conservation",
    "Homogeneous mean field only.",
    "No perturbations and no data likelihood.",
    "**Dark matter: a qualified yes.**",
    "**Dark energy: no, within everything computed.**",
    "The framework reproduces neither Unite's $(w_0,w_a)$ nor $w=-0.764$ consistently.",
    "an approximate one-sigma band inferred from the PDF's statement",
    "the PDF gives no error bars for $(w_0,w_a)$",
    "is not a constant-$w$ projection of the Unite CPL curve",
    "The 4D-effective Friedmann equation with stabilised extra dimensions is an "
    "assumption of this experiment, not a consequence of the 8D equations",
)
MAIN_FIGURES = (
    "exp1_frozen_observables", "exp1_einstein_requirement",
    "exp2_hubble", "exp2_volume_density", "exp2_eos_constraint",
    "exp3_w_of_a", "exp3_rho_psi", "exp3_ke_pe", "exp3_distance_modulus", "exp3_w0wa_plane",
    "exp4_thermal_w", "exp4_thermal_scaling", "exp4_thermal_split",
    "exp4_pair_spectra", "exp4_pair_density",
    "exp5_growth", "exp5_krein",
)
MATHEMATICA_FIGURES = (
    "exp1_mixed_state_rho_p0", "exp1_einstein_requirement",
    "exp2_anisotropy_fractions", "exp3_equation_of_state",
    "exp4_thermal_equation_of_state", "exp4_pair_spectrum",
    "exp5_hilbert_norm_growth", "cross_check_deviations",
)
FIGURE_ORDER = (
    "exp1_frozen_observables", "exp1_einstein_requirement",
    "mathematica/exp1_mixed_state_rho_p0", "mathematica/exp1_einstein_requirement",
    "exp2_hubble", "exp2_volume_density", "exp2_eos_constraint",
    "mathematica/exp2_anisotropy_fractions",
    "exp3_w_of_a", "exp3_rho_psi", "exp3_ke_pe", "exp3_distance_modulus", "exp3_w0wa_plane",
    "mathematica/exp3_equation_of_state",
    "exp4_thermal_w", "exp4_thermal_scaling", "exp4_thermal_split",
    "exp4_pair_spectra", "exp4_pair_density",
    "mathematica/exp4_thermal_equation_of_state", "mathematica/exp4_pair_spectrum",
    "exp5_growth", "exp5_krein", "mathematica/exp5_hilbert_norm_growth",
    "mathematica/cross_check_deviations",
)
FIGURE_PREFIX = "artifacts/dirac16complex/numerics/figures/"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def markdown_text() -> str:
    return MARKDOWN.read_text(encoding="utf-8")


def prose_lines(text: str) -> list[str]:
    """The lines outside fenced code."""
    lines, inside = [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            inside = not inside
            continue
        if not inside:
            lines.append(line)
    return lines


# ----------------------------------------------------------------- formatting --
# The document writes numbers in these forms; the formatters reproduce them from
# the unrounded report values.

def sci(value: float, decimals: int) -> str:
    """6.245e-9 -> '6.25\\times10^{-9}' (mantissa with the given decimals)."""
    exponent = math.floor(math.log10(abs(value)))
    mantissa = f"{value / 10 ** exponent:.{decimals}f}"
    if abs(float(mantissa)) >= 10:
        exponent += 1
        mantissa = f"{value / 10 ** exponent:.{decimals}f}"
    return f"{mantissa}\\times10^{{{exponent}}}"


def S0(value):
    return sci(value, 0)


def S1(value):
    return sci(value, 1)


def S2(value):
    return sci(value, 2)


def S3(value):
    return sci(value, 3)


def F(decimals):
    return lambda value: f"{value:.{decimals}f}"


def G(digits):
    return lambda value: f"{value:.{digits}g}"


def I(value):
    return str(int(round(value)))


def PERCENT(value):
    return f"{100 * value:.1f}%"


# (report, path, formatter, template): the formatted value replaces "@" in the
# template, and the result must occur in the Markdown.  A path element "key=value"
# selects the one list entry whose field key has that value.
QUOTED_NUMBERS = (
    # ---- abstract and synthesis
    ("ns", ["totals", "rustChecks"], I, "All @ self-checks of the Rust program pass"),
    ("ns", ["totals", "pythonChecks"], I, "all @ checks of five independent numpy checkers"),
    ("ns", ["totals", "analysisChecks"], I, "all @ checks of the EXP-3 analysis"),
    ("nb", ["gauntlet", "count"], I, "all @ assertions of a Jupyter notebook"),
    ("mm", ["checkCount"], I, "all @ checks of a Mathematica notebook"),
    ("e4", ["thermal", "wAtA1"], F(4), "Their gas has $w=@$ at temperature $T=10m$"),
    ("e4", ["thermal", "wAtAEnd"], F(4), "and $w=@$ after the scale factor has grown a hundredfold"),
    ("e4", ["pair", "masses", "m=0.1", "nA3"], S2, "(comoving number $na^3$ between $@$"),
    ("e4", ["pair", "masses", "m=0.5", "nA3"], S2, "and $@$ in units of $H_{\\mathrm{inf}}^3$)"),
    ("e3", ["models", 0, "waTangent"], F(2), "the condensate has $w_a=@$, crosses $w=-1$"),
    ("e3", ["models", 0, "zPhantomCrossing"], F(3), "crosses $w=-1$ at redshift $z=@$"),
    ("e3", ["models", 0, "zZero"], F(3), "has negative energy density beyond $z=@$"),
    ("e3", ["models", 0, "zBounce"], F(3), "a bounce ($H=0$) at $z=@$"),
    ("e3", ["models", 0, "cs2Today"], F(1), "its adiabatic sound speed squared today is $@$"),
    ("fits", ["gammaVariant", "objections", "id=newtonConstant", "value"], F(2),
     "imply $\\dot G/G=@\\,H_0$"),
    # ---- EXP-1
    ("e1", ["parameters", "lambdaSelfConsistentMass"], F(14), "$M_\\ast=@$. In total 26 runs."),
    ("e1", ["solverTotals", "steps"], I, "@ steps and"),
    ("e1", ["solverTotals", "rhsEvaluations"], I, "@ right-hand-side evaluations over the 26 runs"),
    ("e1", ["measurements", "maxRhoDrift"], S2, "(maximum drift $@$)"),
    ("p1", ["measurements", "eigenstatePressureOrSMaxDrift"], S2,
     "constant for energy eigenstates (drift $@$)"),
    ("e1", ["measurements", "mixedStatePressureRange"], F(3), "the range of $p_0$ is @ for $K=2$"),
    ("e1", ["runs", "id=A1_K0p5_mix", "pressureRange"], F(3), "and @ for $K=0.5$"),
    ("p1", ["measurements", "mixedStateRangeDeviationFromExact"], S1,
     "reproduces the range to $@$"),
    ("e1", ["runs", "id=A1_K0p5_pos_Bp", "initial", "rho"], F(4), "For $K=0.5$: $\\rho=E=@$"),
    ("e1", ["runs", "id=A1_K0p5_pos_Bp", "initial", "p", 0], F(4), "$p_0=K^2/E=@$"),
    ("e1", ["runs", "id=A1_K0p5_pos_Bp", "initial", "w"], F(5), "$w=K^2/(7E^2)=@$"),
    ("e1", ["runs", "id=A1_K2_pos_Bp", "initial", "rho"], F(4), "For $K=2$: $\\rho=@$"),
    ("e1", ["runs", "id=A1_K2_pos_Bp", "initial", "p", 0], F(4), "$p_0=@$, $w=0.11429$"),
    ("e1", ["runs", "id=A1_K2_pos_Bp", "initial", "w"], F(5), "$p_0=1.7889$, $w=@$"),
    ("e1", ["runs", "id=A1_K0p5_pos_Bp_lambda0p5", "initial", "rho"], F(4),
     "The $\\lambda=0.5$ run has $\\rho=@$"),
    ("e1", ["runs", "id=A1_K0p5_pos_Bp_lambda0p5", "initial", "pMean"], F(4), "$\\bar p=@$"),
    ("e1", ["runs", "id=A1_K0p5_pos_Bp_lambda0p5", "initial", "w"], F(4), "$w=@$, $\\mathrm{KE}_L"),
    ("e1", ["runs", "id=A1_K0p5_pos_Bp_lambda0p5", "initial", "KE_L"], F(4), "$\\mathrm{KE}_L=@$ and"),
    ("e1", ["runs", "id=A1_K0p5_pos_Bp_lambda0p5", "initial", "PE_L"], F(4), "$\\mathrm{PE}_L=@$; the six"),
    ("e1", ["runs", "id=A1_K0p5_pos_Bp_lambda0p5", "initial", "p", 1], F(4),
     "equal $\\tfrac\\lambda2S^2=@$"),
    ("e1", ["measurements", "maxLambdaMeffDrift"], S1, "stays at $M_\\ast$ to $@$"),
    ("e1", ["backgrounds", "profile=A1", "rhoReqMin"], F(1), "$\\rho_{\\mathrm{req}}$ lies in $[@,-21.0]$ for $A=1$"),
    ("e1", ["backgrounds", "profile=A2", "rhoReqMin"], F(1), "and in $[@,-21.0]$ for $A=2$"),
    ("e1", ["measurements", "maxRhoReq"], F(12), "its maximum is $@<0$"),
    ("e1", ["backgrounds", "profile=A1", "wReqMax"], F(3), "lies in $[-0.714,@]$ for $A=1$"),
    ("e1", ["backgrounds", "profile=A2", "wReqMax"], F(3), "and in $[-0.714,@]$ for $A=2$"),
    ("e1", ["backgrounds", "profile=A2", "wReqMin"], F(3), "in $[@,-0.091]$ for $A=2$"),
    ("e1", ["backgrounds", "profile=A1", "a4Final"], F(1), "$a_4$ reaches @ ($A=1$)"),
    ("e1", ["backgrounds", "profile=A2", "a4Final"], F(1), "and 10.0 ($A=2$)"),
    ("e1", ["measurements", "maxVolumeDefect"], S1, "$V/V_0-1$ stays at $@$"),
    ("p1", ["measurements", "backgroundMaxDeviation"], S1, "by its own quadrature ($@$)"),
    ("p1", ["measurements", "derivedMaxDeviation"], S1, "from the raw spinor ($@$)"),
    ("p1", ["measurements", "fdResidualWorstRatioToBound"], F(2), "worst ratio to the truncation bound @)"),
    ("p1", ["measurements", "kineticFdWorstRatioToBound"], F(2), "from the time derivative (@)"),
    ("p1", ["measurements", "exactMaxError"], S2, "(maximum error $@$, limit $10^{-7}$)"),
    ("p1", ["measurements", "eigenmodeLawMaxDeviation"], S1, "the eigenmode laws ($@$)"),
    ("p1", ["measurements", "normMaxDrift"], S2, "the norms (drift $@$)"),
    ("p1", ["measurements", "refinedMaxDifference"], S2, "refined-minus-canonical difference $@$"),
    ("mm", ["exp1", "ndsolve", "maxAbsStateDeviationVsRust"], S2, "maximum state deviation from Rust $@$"),
    ("mm", ["exp1", "ndsolve", "maxExactErrorNDSolve"], S1, "its own exact error $@$ against Rust's"),
    ("mm", ["exp1", "finiteDifference", "maxRelativeResidual"], S2, "residual test ($@$ relative over"),
    ("mm", ["exp1", "finiteDifference", "resolvedRows"], I, "over @ resolved rows"),
    ("mm", ["exp1", "finiteDifference", "negativeControlFlippedMassMaxRelativeResidual"], F(2),
     "fails as it should (@)."),
    # ---- EXP-2
    ("e2", ["runs", "id=x0_0", "exact", "singularityTime"], F(4), "| 0.77, 0.22 | $@$ |"),
    ("e2", ["runs", "id=x0_m0p4", "exact", "singularityTime"], F(4), "| 1.2833, 0.3667 | $@$ |"),
    ("e2", ["runs", "id=x0_0p5", "exact", "singularityTime"], F(4), "| 0.5133, 0.1467 | $@$ |"),
    ("e2", ["runs", "id=x0_m0p4", "lambda"], F(4), "| 2.2, $@$ |"),
    ("e2", ["runs", "id=x0_0p5", "lambda"], F(4), "| 0.88, @ |"),
    ("e2", ["runs", "id=x0_0", "grid", "tEnd"], F(1), "$t_{\\mathrm{end}}=@$"),
    ("e2", ["runs", "id=x0_m0p4", "grid", "tEnd"], F(1), "11855.5$, @ and"),
    ("e2", ["runs", "id=x0_0p5", "grid", "tEnd"], F(1), "9183.5 and @."),
    ("e2", ["solverTotals", "steps"], I, "@ steps and 1781396"),
    ("e2", ["solverTotals", "rhsEvaluations"], I, "and @ right-hand-side evaluations. The step cap"),
    ("e2", ["runs", "id=x0_0", "measurements", "finalAnisotropy"], S1, "$7\\max|H_i-H_j|/\\Theta$ is $@$"),
    ("e2", ["runs", "id=x0_m0p4", "measurements", "finalAnisotropy"], S1, "$4.6\\times10^{-4}$, $@$ and"),
    ("e2", ["runs", "id=x0_0p5", "measurements", "finalAnisotropy"], S1, "and $@$, $H_it$ approaches"),
    ("e2", ["runs", "id=x0_0", "measurements", "finalWeff"], F(5), "$w_{\\mathrm{eff}}=@$, 1.33288"),
    ("e2", ["runs", "id=x0_m0p4", "measurements", "finalWeff"], F(5), ", @ and 1.33261"),
    ("e2", ["runs", "id=x0_0p5", "measurements", "finalWeff"], F(5), "and @ approaches $4/3$"),
    ("e2", ["runs", "id=x0_0", "exact", "extraTimeTurnTime"], F(4), "$t=0.2/\\beta=@$"),
    ("e2", ["runs", "id=x0_m0p4", "exact", "extraTimeTurnTime"], F(4), "0.9091$, @ and 1.3636"),
    ("e2", ["runs", "id=x0_0p5", "exact", "extraTimeTurnTime"], F(4), "and @ (measured on the output grid"),
    ("e2", ["runs", "id=x0_0", "measurements", "extraTimeTurnTimeMeasured"], F(4),
     "measured on the output grid: @,"),
    ("e2", ["runs", "id=x0_m0p4", "measurements", "extraTimeTurnTimeMeasured"], F(4), "0.9095, @,"),
    ("e2", ["runs", "id=x0_0p5", "measurements", "extraTimeTurnTimeMeasured"], F(4), "0.5457, @)."),
    ("e2", ["runs", "id=x0_0", "exact", "kasnerExponents", 0], F(6), "$(@,0.544271,-0.188746)$"),
    ("e2", ["runs", "id=x0_0", "exact", "kasnerExponents", 1], F(6), "$(-0.066576,@,-0.188746)$"),
    ("e2", ["runs", "id=x0_0", "exact", "kasnerExponents", 2], F(6), "$(-0.066576,0.544271,@)$"),
    ("e2", ["runs", "id=x0_m0p4", "exact", "kasnerExponents", 0], F(6), "$(@,0.972978,-0.542895)$"),
    ("e2", ["runs", "id=x0_m0p4", "exact", "kasnerExponents", 1], F(6), "$(-0.290250,@,-0.542895)$"),
    ("e2", ["runs", "id=x0_m0p4", "exact", "kasnerExponents", 2], F(6), "$(-0.290250,0.972978,@)$"),
    ("e2", ["runs", "id=x0_0p5", "exact", "kasnerExponents", 0], F(6), "$(@,0.484182,-0.139107)$"),
    ("e2", ["runs", "id=x0_0p5", "exact", "kasnerExponents", 1], F(6), "$(-0.035225,@,-0.139107)$"),
    ("e2", ["runs", "id=x0_0p5", "exact", "kasnerExponents", 2], F(6), "$(-0.035225,0.484182,@)$"),
    ("e2", ["runs", "id=x0_m0p4", "exact", "kasnerSumSquares"], F(5), "$\\sum p_i^2=@$ for $x_0=-0.4$"),
    ("e2", ["runs", "id=x0_0p5", "exact", "kasnerSumSquares"], F(5), "$\\sum p_i^2=@$ for $x_0=+0.5$"),
    ("e2", ["measurements", "maxKasnerDeviation"], S1, "reproduces them to $@$"),
    ("e2", ["runs", "id=x0_m0p4", "measurements", "phantomRows"], I, "(@ output rows, measured volume range"),
    ("e2", ["runs", "id=x0_m0p4", "measurements", "phantomVolumeMin"], F(3), "measured volume range @ to 0.779"),
    ("e2", ["runs", "id=x0_m0p4", "measurements", "phantomVolumeMax"], F(3), "0.407 to @)"),
    ("e2", ["runs", "id=x0_m0p4", "measurements", "negativeEnergyRows"], I, "for $V/V_0<0.4$ (@ rows)"),
    ("e2", ["runs", "id=x0_m0p4", "measurements", "minRho"], S2, "down to $\\rho=@$ at $V=e^{-7}$"),
    ("e2", ["measurements", "dustMinWeff"], F(5), "the minimum measured $w_{\\mathrm{eff}}$ is $@>-1+1/\\sqrt3=-0.42265$"),
    ("e2", ["measurements", "minThetaOver3HaPositiveEnergy"], F(5), "over rows with $\\rho>0$ is @."),
    ("p2", ["measurements", "thetaOver3HaMinAllRows"], F(3), "$\\Theta/(3H_a)$ falls to @, while"),
    ("e2", ["measurements", "minBound"], S1, "(minimum $@$)"),
    ("e2", ["measurements", "maxConstraintRelative"], S2, "Relative constraint residual at most $@$"),
    ("e2", ["measurements", "maxScalarDensityDrift"], S2, "$|SV/(S_0V_0)-1|$ at most $@$"),
    ("e2", ["measurements", "maxAnisotropyVolumeDrift"], S1, "is conserved (drift $@$)"),
    ("p2", ["measurements", "exactMaxRelativeError"], S1, "exact volume at most $@$"),
    ("p2", ["measurements", "continuityFdMaxRelative"], S1, "residuals of continuity $@$"),
    ("p2", ["measurements", "evolutionFdMaxRelative"], S1, "of the Einstein evolution $@$"),
    ("p2", ["measurements", "diracFdMaxRelative"], S1, "of the Dirac equation $@$ (559 rows)"),
    ("p2", ["measurements", "diracFdRows"], I, "(@ rows)"),
    ("p2", ["measurements", "einsteinTensorMaxRelative"], S1, "computed from the metric agrees to $@$"),
    ("p2", ["measurements", "spinorShapeMaxError"], S1, "its shape error (phase invariant) is $@$"),
    ("p2", ["measurements", "spinorPhaseMaxError"], S2, "its phase error of $@$ at $t\\sim10^4$"),
    ("e2", ["measurements", "maxSpinorPhaseRoundingBound"], S2, "\\mathrm{ulp}(t_{\\mathrm{end}})/2=@$"),
    ("p2", ["measurements", "refined_spinorPhaseRefined"], S2, "in the refined run ($@$)"),
    ("p2", ["measurements", "refined_spinorShapeRefined"], S1, "the shape error shrinks to $@$"),
    ("p2", ["measurements", "refined_gravityCanonical"], S1, "the gravity error from $@$"),
    ("p2", ["measurements", "refined_gravityRefined"], S1, "to $@$. The checker confirms"),
    ("p2", ["measurements", "phaseDriftBinadeMaxRelativeDeviation"], PERCENT, "prediction to @ over 21 binades"),
    ("p2", ["measurements", "phaseDriftBinadesTested"], I, "over @ binades"),
    ("mm", ["exp2", "ndsolve", "lnScaleMaxAbsDeviation"], S2, "NDSolve agrees with Rust to $@$ in $\\ln h_i$"),
    ("mm", ["exp2", "ndsolve", "hubbleMaxDeviationOverTheta"], S2, "and $@$ in $H_i/\\Theta$"),
    ("mm", ["exp2", "ndsolve", "rustLnScaleVsExactAmplificationNormalised"], S1,
     "Rust's error against the closed form is $@$"),
    ("mm", ["exp2", "ndsolve", "ndsolveLnScaleVsExact"], S1, "NDSolve's own error against the closed form is $@$"),
    ("mm", ["exp2", "ndsolve", "spinorMaxAbsDeviation"], S2, "The spinor agrees to $@$ raw"),
    ("mm", ["exp2", "ndsolve", "spinorMaxPhaseAlignedDeviation"], S1, "and $@$ after phase alignment"),
    ("mm", ["exp2", "ndsolve", "rustSpinorVsExactMinusRustReported"], S0, "exact-spinor error to $@$"),
    # ---- EXP-3
    ("e3", ["parameters", "OmegaR"], F(5), "$\\Omega_r=@$"),
    ("e3", ["parameters", "OmegaM"], F(3), "$\\Omega_m=@$"),
    ("e3", ["parameters", "OmegaPsi"], F(5), "$\\Omega_\\psi=@$ (flat)"),
    ("e3", ["solverTotals", "steps"], I, "@ steps and 10115"),
    ("e3", ["solverTotals", "rhsEvaluations"], I, "and @ right-hand-side evaluations over 20 integrations"),
    ("e3", ["models", 0, "cs2Today"], F(2), "| $-0.861$ | $-4.807$ | $@$ |"),
    ("e3", ["models", 1, "cs2Today"], F(2), "| $-0.764$ | $-4.043$ | $@$ |"),
    ("e3", ["models", 2, "cs2Today"], F(2), "| $-0.4286$ | $-1.837$ | $@$ |"),
    ("e3", ["models", 3, "cs2Today"], F(3), "| $-0.25$ | $-0.9375$ | $@$ |"),
    ("e3", ["models", 0, "waTangent"], F(3), "| $-0.462654$ | $-0.861$ | $@$ |"),
    ("e3", ["models", 1, "waTangent"], F(3), "| $-0.433107$ | $-0.764$ | $@$ |"),
    ("e3", ["models", 2, "waTangent"], F(3), "| $-0.3$ | $-0.4286$ | $@$ |"),
    ("e3", ["models", 3, "waTangent"], F(4), "| $-0.2$ | $-0.25$ | $@$ |"),
    ("e3", ["models", 1, "w0"], F(3), "| $-0.433107$ | $@$ |"),
    ("e3", ["models", 2, "w0"], F(4), "| $-0.3$ | $@$ |"),
    ("e3", ["models", 0, "q0"], F(3), "| $-0.462654$ | $@$ | $z=-0.126$, $a=1.144$ |"),
    ("e3", ["models", 1, "q0"], F(3), "| $-0.433107$ | $@$ | $z=-0.103$, $a=1.115$ |"),
    ("e3", ["models", 2, "q0"], F(4), "| $-0.3$ | @ | $z=0.0290$, $a=0.972$ |"),
    ("e3", ["models", 3, "q0"], F(3), "| $-0.2$ | @ | $z=0.191$, $a=0.840$ |"),
    ("e3", ["models", 4, "q0"], F(3), "| 0 | @ | none | 3, 7 |"),
    ("e3", ["runs", "id=x0_m0p462654_mu3", "massOverH0"], F(1), "| @, 93.7 |"),
    ("e3", ["runs", "id=x0_m0p462654_mu7", "massOverH0"], F(1), "| 40.2, @ |"),
    ("e3", ["runs", "id=x0_m0p433107_mu3", "massOverH0"], F(1), "| @, 52.3 |"),
    ("e3", ["runs", "id=x0_m0p433107_mu7", "massOverH0"], F(1), "| 22.4, @ |"),
    ("e3", ["runs", "id=x0_m0p2_mu7", "massOverH0"], F(1), "| 5.0, @ |"),
    ("e3", ["measurements", "maxMuDiffRho"], S2, "give the same $\\rho$ ($@$)"),
    ("e3", ["measurements", "maxMuDiffP"], S2, "$p$ ($@$)"),
    ("e3", ["measurements", "maxMuDiffW"], S2, "$w$ ($@$, condition-scaled)"),
    ("p3", ["measurements", "sigmaSpinorMaxRelDeviation"], S2, "agrees with $a^{-3}$ to $@$"),
    ("p3", ["measurements", "refinedMaxSigmaDeviation"], S2, "(refined: $@$)"),
    ("p3", ["measurements", "sigmaStateMaxRelDeviation"], S2, "$\\exp(\\ln\\sigma)$ to $@$"),
    ("p3", ["measurements", "referenceTimeMaxAbsError"], S2, "independent quadratures to $@$ and"),
    ("p3", ["measurements", "referenceDistanceMaxAbsError"], S2, "and $@$, the spinor with its exact phase"),
    ("p3", ["measurements", "referenceSpinorMaxError"], S2, "with its exact phase to $@$"),
    ("p3", ["measurements", "refinedMaxSpinorError"], S2, "(refined $@$). The roots"),
    ("p3", ["measurements", "rhoZeroMaxRelError"], S1, "reproduced to $@$ ($\\rho_\\psi=0$)"),
    ("p3", ["measurements", "phantomCrossingMaxRelError"], S1, "$@$ ($w=-1$)"),
    ("p3", ["measurements", "decelerationRootMaxRelError"], S1, "$@$ ($q_{\\mathrm{dec}}=0$)"),
    ("p3", ["measurements", "waSummaryMaxRelDeviation"], S1, "the tangent $w_a$ to $@$ relative"),
    ("p3", ["measurements", "bounceRelDeviation"], S1, "the bounce stop to $@$"),
    ("fits", ["validation", "measurements", "nmSyntheticCplError"], S1, "curves to $@$ and"),
    ("fits", ["validation", "measurements", "nmSyntheticWconstError"], S1, "and $@$; Rust distances"),
    ("fits", ["validation", "measurements", "rustDistanceVsQuadrature"], S1,
     "match an independent quadrature to $@$"),
    ("mm", ["exp3", "ndsolve", "spinorMaxAbsDeviation"], S2, "NDSolve agrees to $@$ in the spinor"),
    ("mm", ["exp3", "ndsolve", "spinorMaxPhaseAlignedDeviation"], S2, "($@$ phase aligned)"),
    ("mm", ["exp3", "ndsolve", "lnSigmaMaxAbsDeviation"], S2, "and to $@$ in $\\ln\\sigma$"),
    ("mm", ["exp3", "ndsolve", "ndsolveSpinorVsExact"], S1, "its exact spinor error is $@$"),
    ("mm", ["exp3", "finiteDifference", "negativeControlFlippedMassMaxRelativeResidual"], F(1),
     "fails as it should (@). The 4D-effective"),
    ("fits", ["scan", "x0CriticalWFit"], F(6), "For $x_0<@$ the $w(a)$ fit does not exist"),
    ("fits", ["scan", "x0CriticalMuFit"], F(6), "for $x_0<@$ the $\\mathrm{DM}(z)$ fits do not exist"),
    ("fits", ["scan", "count"], I, "(@ models, fits_scan.csv)"),
    ("fits", ["scan", "x0ForUniteW0"], F(7), "finds $x_0=@$ for $w_0=-0.861$"),
    ("fits", ["scan", "tangentWaAtUniteW0"], F(3), "with tangent $w_a=@$, and"),
    ("fits", ["scan", "x0ForConstantW0764"], F(7), "and $x_0=@$ for $w_0=-0.764$"),
    ("fits", ["unite", "w0PlusWa"], F(3), "For the Unite CPL, $w_0+w_a=@$"),
    ("fits", ["unite", "phantomCrossingA"], F(3), "and $w=-1$ at $a=@$."),
    ("fits", ["unite", "constantWProjectionOffsetProfiled", "w"], F(4),
     "| best constant $w$ for the Unite CPL distances | none | $@$ |"),
    ("fits", ["unite", "constantWProjectionOffsetZero", "w"], F(4),
     "| the same with the offset fixed at 0 | none | $@$ |"),
    ("fits", ["unite", "constantWProjectionLogGridOffsetProfiled", "w"], F(4),
     "| the same on a log-uniform $z$ grid | none | $@$ |"),
    ("fits", ["unite", "constantWProjectionOffsetProfiled", "w"], F(3), "the CPL distances is $@$ (uniform $z$)"),
    ("fits", ["unite", "constantWProjectionOffsetZero", "w"], F(3), "$@$ (offset zero)"),
    ("fits", ["unite", "constantWProjectionLogGridOffsetProfiled", "w"], F(3), "or $@$ (log-uniform $z$)"),
    ("fits", ["gammaVariant", "gamma"], F(6), "$\\gamma=@$ ($n=0.374457$"),
    ("fits", ["gammaVariant", "n"], F(6), "($n=@$, $x_0=-0.4626545$)"),
    ("fits", ["gammaVariant", "x0"], F(7), "$x_0=@$) reproduces the Unite tangent"),
    ("fits", ["gammaVariant", "tangentCPLofEffectiveW", "w0"], F(4), "| $(@,-0.0749)$ | none |"),
    ("fits", ["gammaVariant", "tangentCPLofEffectiveW", "wa"], F(4), "with tangent $(-0.9827,@)$"),
    ("fits", ["gammaVariant", "effectiveWFitRequested", "w0"], F(3), "fit | $(@,-0.247)$ | none |"),
    ("fits", ["gammaVariant", "effectiveWFitRequested", "wa"], F(3), "fit | $(-0.955,@)$ | none |"),
    ("fits", ["gammaVariant", "model", "muFitRequested", "cplOffsetProfiled", "w0"], F(4),
     "fits | $(@,-0.1611)$ | $-1.0159$ |"),
    ("fits", ["gammaVariant", "model", "muFitRequested", "cplOffsetProfiled", "wa"], F(4),
     "fits | $(-0.9707,@)$ | $-1.0159$ |"),
    ("fits", ["gammaVariant", "model", "muFitRequested", "wConstantOffsetProfiled", "w"], F(4),
     "| $(-0.9707,-0.1611)$ | $@$ |"),
    ("fits", ["gammaVariant", "model", "muVsUniteCPL", "maxAbsDifferenceMag"], F(3),
     "($\\max|\\Delta\\mathrm{DM}|=@$ mag"),
    ("fits", ["gammaVariant", "model", "muVsUniteCPL", "maxAbsDifferenceOffsetProfiledMag"], F(3),
     "@ mag with the offset profiled)"),
    ("fits", ["gammaVariant", "objections", "id=continuity", "value"], F(3),
     "$d\\rho/dN+3(\\rho+p)=@$ today"),
    ("fits", ["gammaVariant", "objections", "id=newtonConstant", "value"], F(2), "$\\dot G/G=3\\gamma H_0=@H_0$"),
    ("fits", ["gammaVariant", "objections", "id=newtonConstant", "gdotPerYear"], S1, "about $@$ per year"),
    ("fits", ["gammaVariant", "objections", "id=einstein8D", "value"], F(3), "=@H_a^2$ for $\\gamma=0.875$"),
    # ---- EXP-4
    ("e4", ["parameters", "thermal", "nodes"], I, "@ Gauss-Legendre nodes on $[0,k_{\\max}]$"),
    ("e4", ["parameters", "thermal", "kMax"], I, "$k_{\\max}=12T_i=@$"),
    ("e4", ["parameters", "pair", "nodes"], I, "@ Gauss-Legendre nodes in $\\ln k$"),
    ("e4", ["solverTotals", "steps"], I, "; @ steps and"),
    ("e4", ["solverTotals", "rhsEvaluations"], I, "and @ right-hand-side evaluations. Adams was selected"),
    ("e4", ["methodSelection", "trials", 0, "maxErrorVsReference"], S2, "Adams had error $@$ with 1370"),
    ("e4", ["methodSelection", "trials", 0, "rhsEvals"], I, "with @ evaluations against BDF's"),
    ("e4", ["methodSelection", "trials", 1, "maxErrorVsReference"], S2, "against BDF's $@$ with 4730"),
    ("e4", ["methodSelection", "trials", 1, "rhsEvals"], I, "with @ (plus 2464 for the Jacobian)"),
    ("e4", ["methodSelection", "trials", 1, "linRhsEvals"], I, "(plus @ for the Jacobian)"),
    ("e4", ["methodSelection", "trials", 2, "maxErrorVsReference"], S2, "$k=119.93$) $@$ with 88979"),
    ("e4", ["methodSelection", "trials", 2, "rhsEvals"], I, "with @ against"),
    ("e4", ["methodSelection", "trials", 3, "maxErrorVsReference"], S2, "against $@$ with 313247"),
    ("e4", ["methodSelection", "trials", 3, "rhsEvals"], I, "with @ (plus 164384)"),
    ("e4", ["methodSelection", "trials", 3, "linRhsEvals"], I, "(plus @)."),
    ("e4", ["methodSelection", "trials", 2, "k"], F(2), "for node 47 ($k=@$)"),
    ("e4", ["methodSelection", "trials", 0, "k"], F(4), "for node 2 ($k=@$)"),
    ("e4", ["thermal", "wAtA1"], F(10), "$w=@$ at $a=1$ (kinetic theory: the same to ten digits)"),
    ("e4", ["thermal", "wKineticAtA1"], F(10), "$w=@$ at $a=1$"),
    ("e4", ["thermal", "wAtAEnd"], F(7), "$w=@$ at $a=100$"),
    ("e4", ["thermal", "wKineticAtAEnd"], F(7), "(kinetic theory @)"),
    ("e4", ["thermal", "maxRelDevRho"], S2, "$\\rho$ agrees to $@$. $p$ deviates"),
    ("e4", ["thermal", "maxRelDevP"], S2, "$p$ deviates by up to $@$"),
    ("e4", ["thermal", "pressureEnvelopeMaxRatio"], F(2), "interference envelope (ratio @)"),
    ("e4", ["thermal", "instantaneousStartMaxRelPressureDevSameNodes"], F(2), "deviation from @ to 0.12 relative"),
    ("e4", ["thermal", "adiabaticVacuumMaxRelPressureDev"], F(2), "from 1.78 to @ relative"),
    ("e4", ["thermal", "maxBeta2GasWeighted"], S1, "The occupation-weighted $|\\beta|^2$ is $@$"),
    ("e4", ["thermal", "adiabaticVacuumLateBeta2"], S1, "the adiabatic-vacuum runs end at $@$"),
    ("e4", ["thermal", "maxBeta2PerMode"], S2, "The largest single-mode value, $@$ at"),
    ("e4", ["thermal", "maxBeta2PerModeK"], F(3), "at $k=@$, is"),
    ("p4", ["measurements", "thermalBeta2PerModeMaxOver4c2"], F(3), "is @ times $4|c|^2$"),
    ("p4", ["measurements", "thermalKmaxTruncationRhoAtA1"], S1, "misses $@$ of $\\rho$ at $a=1$"),
    ("e4", ["pair", "masses", "m=0.0", "nA3"], S1, "| 0 | $@$ | $8.5\\times10^{-25}$ |"),
    ("e4", ["pair", "masses", "m=0.0", "maxBeta2"], S1, "| 0 | $1.8\\times10^{-24}$ | $@$ |"),
    ("e4", ["pair", "masses", "m=0.1", "nA3"], S3, "| 0.1 | $@$ | 0.348 |"),
    ("e4", ["pair", "masses", "m=0.5", "nA3"], S3, "| 0.5 | $@$ | 0.0640 |"),
    ("e4", ["pair", "masses", "m=1.0", "nA3"], S3, "| 1 | $@$ | 0.0138 |"),
    ("e4", ["pair", "masses", "m=2.0", "nA3"], S3, "| 2 | $@$ | 0.00265 |"),
    ("e4", ["pair", "masses", "m=0.1", "maxBeta2"], F(3), "$1.455\\times10^{-3}$ | @ |"),
    ("e4", ["pair", "masses", "m=0.5", "maxBeta2"], F(4), "$4.991\\times10^{-3}$ | @ |"),
    ("e4", ["pair", "masses", "m=1.0", "maxBeta2"], F(4), "$4.414\\times10^{-3}$ | @ |"),
    ("e4", ["pair", "masses", "m=2.0", "maxBeta2"], F(5), "$2.422\\times10^{-3}$ | @ |"),
    ("e4", ["pair", "masses", "m=0.1", "wFrozenSpectrumAtA1"], F(4), "| 0.1 | @ | $3.09\\times10^{-4}$ |"),
    ("e4", ["pair", "masses", "m=0.5", "wFrozenSpectrumAtA1"], F(4), "| 0.5 | @ | $1.28\\times10^{-4}$ |"),
    ("e4", ["pair", "masses", "m=1.0", "wFrozenSpectrumAtA1"], F(4), "| 1 | @ | $1.70\\times10^{-4}$ |"),
    ("e4", ["pair", "masses", "m=2.0", "wFrozenSpectrumAtA1"], F(4), "| 2 | @ | $3.09\\times10^{-4}$ |"),
    ("e4", ["pair", "masses", "m=0.1", "wEnd"], S2, "| 0.3095 | $@$ |"),
    ("e4", ["pair", "masses", "m=0.5", "wEnd"], S2, "| 0.2544 | $@$ |"),
    ("e4", ["pair", "masses", "m=1.0", "wEnd"], S2, "| 0.2390 | $@$ |"),
    ("e4", ["pair", "masses", "m=2.0", "wEnd"], S2, "| 0.2397 | $@$ |"),
    ("e4", ["pair", "masses", "m=0.0", "rhoA3End"], S1, "| $1/3$ | $1/3$ | $@$ |"),
    ("e4", ["pair", "masses", "m=0.1", "rhoA3End"], S3, "| $3.09\\times10^{-4}$ | $@$ |"),
    ("e4", ["pair", "masses", "m=0.5", "rhoA3End"], S3, "| $1.28\\times10^{-4}$ | $@$ |"),
    ("e4", ["pair", "masses", "m=1.0", "rhoA3End"], S3, "| $1.70\\times10^{-4}$ | $@$ |"),
    ("e4", ["pair", "masses", "m=2.0", "rhoA3End"], S3, "| 0.2397 | $3.09\\times10^{-4}$ | $@$ |"),
    ("e4", ["pair", "masses", "m=1.0", "rhoA3End"], S3, "(for $m=1$: $@$ against"),
    ("e4", ["pair", "masses", "m=1.0", "nA3"], S3, "against $na^3=@$)"),
    ("e4", ["pair", "tailMaxRelDev"], PERCENT, "follows the kink prediction to @ (limit 35%)"),
    ("p4", ["measurements", "pairMasslessMaxBeta2"], S1, "the measured $|\\beta|^2$ ($@$) is roundoff"),
    ("p4", ["measurements", "thermalGL48QuadratureErrorRho"], S1, "(quadrature error $@$ in $\\rho$)"),
    ("p4", ["measurements", "thermalMaxUnitarityDev"], S1, "checks unitarity ($@$ thermal"),
    ("p4", ["measurements", "pairMaxUnitarityDev"], S1, "thermal, $@$ pair)"),
    ("p4", ["measurements", "thermalReferenceMaxError"], S2, "Richardson estimate ($@$ thermal"),
    ("p4", ["measurements", "pairReferenceMaxError"], S1, "thermal, $@$ pair) because"),
    ("p4", ["measurements", "refinedThermalRhoRelDiff"], S1, "change by $@$ and"),
    ("p4", ["measurements", "refinedThermalPressureRelDiff"], S1, "and $@$ relative, unitarity"),
    ("p4", ["measurements", "refinedThermalUnitarityRefined"], S1, "to $@$, pair $|\\beta|^2$"),
    ("p4", ["measurements", "refinedPairBeta2RelDiff"], S1, "changes by $@$ relative)"),
    ("mm", ["exp4", "thermal", "maxAbsDeviation"], S2, "(thermal: $@$ raw"),
    ("mm", ["exp4", "thermal", "maxPhaseAlignedDeviation"], S1, "raw, $@$ phase aligned;"),
    ("mm", ["exp4", "thermal", "ndsolveAdamsVsRungeKuttaNode2"], S1, "Runge-Kutta on node 2: $@$"),
    ("mm", ["exp4", "pair", "maxPhaseAlignedDeviation"], S1, "pair: $@$ phase aligned"),
    ("mm", ["exp4", "pair", "maxBeta2RelativeDeviation"], S1, "and $@$ relative in $|\\beta|^2$"),
    ("mm", ["exp4", "kineticTheory", "rhoModeSumMaxRelativeDeviation"], S2, "($\\rho$: $@$"),
    ("mm", ["exp4", "kineticTheory", "pModeSumMaxRelativeDeviation"], S2, "$p$: $@$, the free-wave"),
    ("mm", ["exp4", "thermal", "oneIntervalMaxAbsDeviation"], S1, "propagation instead ($@$)"),
    # ---- EXP-5
    ("e5", ["runs", "id=q0p05_Cp", "tStar"], F(5), "so $t_\\ast=@$ and 2.30259"),
    ("e5", ["runs", "id=q0p1_Cp", "tStar"], F(5), "2.99573$ and @; integration"),
    ("e5", ["runs", "id=q0p05_Cp", "energy0"], F(6), "$E_0=\\sqrt{m^2-q^2}=@$ and"),
    ("e5", ["runs", "id=q0p1_Cp", "energy0"], F(6), "0.998749$ and @)"),
    ("e5", ["runs", "id=q0p05_Cp", "finalNormHilbert"], S3, "$u^\\dagger u$ reaches $@$ ($q=0.05$)"),
    ("e5", ["runs", "id=q0p1_Cp", "finalNormHilbert"], S3, "and $@$ ($q=0.1$)"),
    ("e5", ["runs", "id=q0p05_Cp", "rateEarly"], F(2), "rises from @ ($q=0.05$)"),
    ("e5", ["runs", "id=q0p1_Cp", "rateEarly"], F(2), "and @ ($q=0.1$) early"),
    ("e5", ["runs", "id=q0p05_Cp", "rateLate"], F(1), "early to @ late"),
    ("e5", ["runs", "id=q0p1_Cp", "rateLate"], F(1), "early to @ late"),
    ("e5", ["runs", "id=q0p05_Cp", "wkb", "gammaNumeric"], F(4), "$\\Delta\\ln(u^\\dagger u)=@$ against"),
    ("e5", ["runs", "id=q0p05_Cp", "wkb", "gammaLeading"], F(4), "the leading WKB value @ (relative"),
    ("e5", ["runs", "id=q0p05_Cp", "wkb", "gammaFirstOrder"], F(5), "the first-order value @ ("),
    ("e5", ["runs", "id=q0p1_Cp", "wkb", "gammaNumeric"], F(4), "; @ against 30.9770"),
    ("e5", ["runs", "id=q0p1_Cp", "wkb", "gammaLeading"], F(4), "against @ and 30.9530"),
    ("e5", ["runs", "id=q0p1_Cp", "wkb", "gammaFirstOrder"], F(4), "and @ for $q=0.1$"),
    ("e5", ["measurements", "maxRelDevWkbLeading"], S2, "(relative deviation $@$)"),
    ("e5", ["measurements", "maxRelDevWkbFirstOrder"], S2, "30.99986 ($@$)"),
    ("p5", ["measurements", "wkbLateRateMaxRelDev"], S1, "matches $2\\varkappa-m^2/\\varkappa^2$ to $@$"),
    ("e5", ["measurements", "maxKreinDriftNormalized"], S2, "normalised drift at most $@$"),
    ("e5", ["measurements", "maxKreinDriftBeforeTStar"], S2, "up to $t_\\ast$ at most $@$"),
    ("e5", ["measurements", "maxKreinDriftAbs"], F(3), "the absolute drift is @ because"),
    ("e5", ["solverTotals", "steps"], I, "@ steps and 4800"),
    ("e5", ["solverTotals", "rhsEvaluations"], I, "and @ right-hand-side evaluations.\n\n### 10.5"),
    ("p5", ["measurements", "fdResidualWorstRatioToBound"], F(2), "(finite-difference residual ratio @;"),
    ("p5", ["measurements", "referenceMaxRelativeError"], S2, "RK4 reference $@$ relative"),
    ("p5", ["measurements", "refinedMaxRelativeError"], S2, "relative, refined $@$;"),
    ("p5", ["measurements", "wkbClosedFormVsQuadrature"], S1, "against quadrature $@$;"),
    ("mm", ["exp5", "ndsolve", "maxRelativeStateDeviation"], S2, "NDSolve agrees to $@$ relative"),
    ("mm", ["exp5", "ndsolve", "ndsolveSelfRelativeError"], S1, "with machine precision to $@$"),
    # ---- Mathematica table of Section 11.2
    ("mm", ["exp1", "ndsolve", "maxAbsStateDeviationVsRust"], S2, "| EXP-1 spinor state | $@$ |"),
    ("mm", ["exp1", "ndsolve", "maxExactErrorRust"], S2, "| EXP-1 exact-propagator error, Rust | $@$ |"),
    ("mm", ["exp1", "ndsolve", "maxExactErrorNDSolve"], S1, "| EXP-1 exact-propagator error, NDSolve | $@$ |"),
    ("mm", ["exp2", "ndsolve", "lnScaleMaxAbsDeviation"], S2, "| EXP-2 $\\ln h_i$ | $@$ |"),
    ("mm", ["exp2", "ndsolve", "hubbleMaxDeviationOverTheta"], S2, "| EXP-2 $H_i/\\Theta$ | $@$ |"),
    ("mm", ["exp2", "ndsolve", "ndsolveLnScaleVsExact"], S1,
     "| EXP-2 $\\ln h_i$ against the closed form, NDSolve | $@$ |"),
    ("mm", ["exp2", "ndsolve", "spinorMaxAbsDeviation"], S2, "| EXP-2 spinor, raw | $@$ |"),
    ("mm", ["exp2", "ndsolve", "spinorMaxPhaseAlignedDeviation"], S1, "| EXP-2 spinor, phase aligned | $@$ |"),
    ("mm", ["exp2", "ndsolve", "rustSpinorVsExact"], S2, "| EXP-2 spinor against the exact solution, Rust | $@$ |"),
    ("mm", ["exp2", "ndsolve", "ndsolveSpinorVsExact"], S1, "| EXP-2 the same, NDSolve | $@$ |"),
    ("mm", ["exp3", "ndsolve", "spinorMaxAbsDeviation"], S2, "| EXP-3 spinor | $@$ |"),
    ("mm", ["exp3", "ndsolve", "lnSigmaMaxAbsDeviation"], S2, "| EXP-3 $\\ln\\sigma$ | $@$ |"),
    ("mm", ["exp3", "ndsolve", "rustSpinorVsExact"], S2, "| EXP-3 spinor against the exact solution, Rust | $@$ |"),
    ("mm", ["exp3", "ndsolve", "ndsolveSpinorVsExact"], S1, "| EXP-3 the same, NDSolve | $@$ |"),
    ("mm", ["exp4", "thermal", "maxAbsDeviation"], S2, "| EXP-4 thermal modes, raw | $@$ |"),
    ("mm", ["exp4", "thermal", "maxPhaseAlignedDeviation"], S1, "| EXP-4 thermal modes, phase aligned | $@$ |"),
    ("mm", ["exp4", "thermal", "ndsolveAdamsVsRungeKuttaNode2"], S1,
     "| EXP-4 NDSolve Adams against Runge-Kutta | $@$ |"),
    ("mm", ["exp4", "kineticTheory", "rhoModeSumMaxRelativeDeviation"], S2,
     "| EXP-4 kinetic theory, $\\rho$ (relative) | $@$ |"),
    ("mm", ["exp4", "kineticTheory", "pModeSumMaxRelativeDeviation"], S2,
     "| EXP-4 kinetic theory, $p$ (relative) | $@$ |"),
    ("mm", ["exp4", "pair", "maxPhaseAlignedDeviation"], S1, "| EXP-4 pair modes, phase aligned | $@$ |"),
    ("mm", ["exp4", "pair", "maxBeta2RelativeDeviation"], S1,
     "| EXP-4 pair $\\lvert\\beta\\rvert^2$ (relative) | $@$ |"),
    ("mm", ["exp5", "ndsolve", "maxRelativeStateDeviation"], S2, "| EXP-5 state (relative) | $@$ |"),
    ("mm", ["exp5", "ndsolve", "ndsolveSelfRelativeError"], S1,
     "| EXP-5 machine against 32-digit precision | $@$ |"),
    # ---- notebook
    ("nb", ["cells"], I, "The notebook has @ cells"),
    ("nb", ["markdownCells"], I, "(@ markdown, 8 code; kernel python3)"),
    ("nb", ["codeCells"], I, "(15 markdown, @ code; kernel python3)"),
    ("nb", ["gauntlet", "count"], I, "A gauntlet of @ assertions"),
)

# Rows of the restricted-fit tables of Section 12.4, from fits.json models 0..4.
FIT_ROWS = (
    ("| $-0.462654$ |", 0), ("| $-0.433107$ |", 1), ("| $-0.3$ |", 2), ("| $-0.2$ |", 3),
)


def get(document, path):
    node = document
    for key in path:
        if isinstance(key, str) and "=" in key and isinstance(node, list):
            field, value = key.split("=", 1)
            matches = [item for item in node if str(item.get(field)) == value]
            if len(matches) != 1:
                raise KeyError(f"{key}: {len(matches)} matches")
            node = matches[0]
        else:
            node = node[key]
    return node


def load_reports() -> dict[str, dict]:
    reports = {
        "ns": load_json(NUMERICS / "numerics-summary.json"),
        "nb": load_json(NUMERICS / "notebook-report.json"),
        "mm": load_json(NUMERICS / "mathematica-report.json"),
        "fits": load_json(NUMERICS / "exp3" / "fits.json"),
    }
    for number in range(1, 6):
        reports[f"e{number}"] = load_json(NUMERICS / f"exp{number}" / "summary.json")
        reports[f"p{number}"] = load_json(NUMERICS / f"exp{number}" / "python-check-report.json")
    return reports


class PinTests(unittest.TestCase):

    def test_markdown_sha256_pin(self):
        self.assertEqual(sha256_file(MARKDOWN), MARKDOWN_SHA256)

    def test_tex_sha256_pin(self):
        self.assertEqual(sha256_file(TEX), TEX_SHA256)

    def test_markdown_is_lf_only_utf8(self):
        content = MARKDOWN.read_bytes()
        self.assertNotIn(b"\r", content)
        content.decode("utf-8")
        self.assertIsNone(re.search(rb"[\x00-\x09\x0b-\x1f]", content))

    def test_tex_is_the_builder_output_of_the_markdown(self):
        latex = builder.convert(markdown_text(), strip_heading_numbers=True,
                                image_root=REPOSITORY_ROOT)
        self.assertEqual(latex.encode("utf-8"), TEX.read_bytes())
        self.assertIn("\\usepackage{graphicx}\n", latex)
        self.assertEqual(latex.count("\\begin{figure}[htbp]"), len(FIGURE_ORDER))

    def test_registered_edition_matches_the_committed_pdf(self):
        registry = check_provenance_pdf.load_specifications(
            check_provenance_pdf.DEFAULT_SPECIFICATIONS_PATH)
        self.assertIn(EDITION, registry)
        entry = registry[EDITION]
        self.assertEqual(entry["path"], "provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.pdf")
        content = PDF.read_bytes()
        self.assertEqual(entry["sha256"], hashlib.sha256(content).hexdigest())
        self.assertEqual(entry["pages"], len(check_dissertation_pdf.PAGE_PATTERN.findall(content)))
        self.assertTrue(content.startswith(b"%PDF-"))
        self.assertTrue(content.rstrip().endswith(b"%%EOF"))
        self.assertEqual(check_dissertation_pdf.parse_media_boxes(content), [(0.0, 0.0, 612.0, 792.0)])


class ContentTests(unittest.TestCase):

    def test_title_and_subtitle(self):
        lines = markdown_text().split("\n")
        self.assertEqual(lines[0], "# " + TITLE)
        self.assertEqual(lines[2], "## " + SUBTITLE)
        self.assertEqual(sum(1 for line in lines if line.startswith("# ")), 1)

    def test_required_sections_in_order(self):
        headings = [line[3:] for line in markdown_text().split("\n") if line.startswith("## ")]
        self.assertEqual(headings[0], SUBTITLE)
        self.assertEqual(headings[1:], list(REQUIRED_SECTIONS))

    def test_every_experiment_has_the_seven_subsections(self):
        lines = markdown_text().split("\n")
        for section in range(6, 11):
            with self.subTest(section=section):
                sub = [line[4:] for line in lines if line.startswith(f"### {section}.")]
                self.assertEqual(sub, [f"{section}.{n} {name}" for n, name in
                                       enumerate(EXPERIMENT_SUBSECTIONS, start=1)])
        synthesis = [line[4:] for line in lines if line.startswith("### 12.")]
        self.assertEqual(synthesis, list(SYNTHESIS_SUBSECTIONS))

    def test_required_phrases(self):
        text = markdown_text()
        for phrase in REQUIRED_PHRASES:
            with self.subTest(phrase=phrase[:60]):
                self.assertIn(phrase, text)

    def test_no_placeholders_or_todo_and_no_other_provenance_markdown(self):
        text = markdown_text()
        self.assertIsNone(re.search(r"@@[A-Z0-9_]+@@", text))
        self.assertNotIn("TODO", text)
        self.assertNotIn("FIXME", text)
        self.assertIsNone(re.search(r"provenance/[A-Za-z0-9_]+\.md", text.replace(
            "provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md", "")))

    def test_every_fenced_code_line_fits(self):
        inside = False
        for line in markdown_text().split("\n"):
            if line.startswith("```"):
                inside = not inside
                continue
            if inside:
                self.assertLessEqual(len(line), builder.MAX_CODE_LINE_LENGTH, line)
                self.assertNotIn("`", line)
        self.assertFalse(inside)

    def test_no_double_hyphen_or_stray_asterisk_in_prose(self):
        """-- would become an en dash, and a lone * would open an emphasis."""
        for line in prose_lines(markdown_text()):
            if re.fullmatch(r"\|( --- \|)+", line):
                continue
            with self.subTest(line=line[:60]):
                self.assertNotIn("--", line)
                self.assertEqual(line.replace("**", "").count("*") % 2, 0)

    def test_tables_have_at_most_four_columns(self):
        """Five or more p-columns of 0.92/n linewidth overflow the text block."""
        for line in prose_lines(markdown_text()):
            if line.startswith("|"):
                self.assertLessEqual(len(builder.split_table_row(line)), 4, line)


class FigureTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.text = markdown_text()
        cls.paths = builder.figure_paths(cls.text)
        cls.notebook = load_json(NUMERICS / "notebook-report.json")
        cls.mathematica = load_json(NUMERICS / "mathematica-report.json")

    def test_figures_in_order(self):
        self.assertEqual(self.paths, [FIGURE_PREFIX + name + ".png" for name in FIGURE_ORDER])
        self.assertEqual(len(set(self.paths)), len(self.paths))

    def test_every_figure_is_an_existing_png(self):
        for path in self.paths:
            with self.subTest(path=path):
                builder.validate_figure_path(path, 0)
                builder.check_figure_file(path, REPOSITORY_ROOT, 0)

    def test_main_figures_are_the_notebook_figures_with_recorded_hashes(self):
        recorded = {entry["file"]: entry for entry in self.notebook["figures"]}
        expected = {FIGURE_PREFIX + name + ".png" for name in MAIN_FIGURES}
        self.assertEqual(set(recorded), expected)
        for path, entry in recorded.items():
            with self.subTest(path=path):
                data = (REPOSITORY_ROOT / path).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), entry["sha256"])
                self.assertEqual(len(data), entry["bytes"])
        self.assertEqual(expected, {p for p in self.paths if "/mathematica/" not in p})

    def test_mathematica_figures_are_the_reported_ones(self):
        listed = set(self.mathematica["figures"])
        self.assertEqual(listed, {FIGURE_PREFIX + "mathematica/" + name + ".png"
                                  for name in MATHEMATICA_FIGURES})
        self.assertEqual(listed, {p for p in self.paths if "/mathematica/" in p})
        self.assertTrue(self.mathematica["checks"]["figuresExported"])

    def test_every_figure_has_a_caption_of_substance(self):
        for line in self.text.split("\n"):
            figure = builder.figure_line(line.strip())
            if figure is not None:
                self.assertGreaterEqual(len(figure[0]), 60, figure[1])


class AgreementWithArtifactsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.text = markdown_text()
        cls.reports = load_reports()

    def test_quoted_numbers_match_the_reports(self):
        for source, path, formatter, template in QUOTED_NUMBERS:
            value = get(self.reports[source], path)
            expected = template.replace("@", formatter(value))
            with self.subTest(source=source, path="/".join(map(str, path))):
                self.assertIn(expected, self.text)

    def test_derived_numbers_match_the_reports(self):
        """Numbers the text derives by one arithmetic step from the reports."""
        runs = {run["id"]: run for run in self.reports["e5"]["runs"]}
        ratios = [runs[name]["rateLate"] / runs[name]["rateEarly"] for name in ("q0p05_Cp", "q0p1_Cp")]
        self.assertIn(f"ratios {ratios[0]:.1f} and {ratios[1]:.1f}: super-exponential growth", self.text)
        model = self.reports["e3"]["models"][0]
        unite = self.reports["fits"]["unite"]
        self.assertEqual(round(model["waTangent"] / unite["wa"]), 8)
        self.assertIn("evolves about eight times faster than the Unite fit", self.text)
        self.assertIn("evolves eight times too fast", self.text)
        thermal = self.reports["e4"]["thermal"]
        self.assertIn(f"$\\mathrm{{KE}}_H/\\rho=3w$ falls from 1 to about {3 * thermal['wAtAEnd']:.2f}",
                      self.text)
        self.assertEqual(f"{3 * thermal['wAtA1']:.2f}", "1.00")
        gamma = self.reports["fits"]["gammaVariant"]
        self.assertAlmostEqual(3 * gamma["gamma"],
                               [o for o in gamma["objections"] if o["id"] == "newtonConstant"][0]["value"])
        pair = {m["m"]: m for m in self.reports["e4"]["pair"]["masses"]}
        self.assertEqual(max(pair, key=lambda m: pair[m]["nA3"]), 0.5)
        self.assertIn("largest near $m=0.5H_{\\mathrm{inf}}$", self.text)
        self.assertTrue(all(pair[m]["maxBeta2"] <= 1 and pair[m]["maxBeta2Adiabatic"] <= 1 for m in pair))
        self.assertTrue(all(pair[m]["wEnd"] < 1e-3 for m in pair if m > 0))

    def test_restricted_fit_tables_match_fits_json(self):
        models = self.reports["fits"]["models"]
        for label, index in FIT_ROWS:
            model = models[index]
            wfit = model["wFitRestricted"]
            mufit = model["muFitRestricted"]
            cpl, wconst = mufit["cplOffsetProfiled"], mufit["wConstantOffsetProfiled"]
            rows = (
                f"{label} ${model['tangentCPL']['w0']:.4g}$ | ${model['tangentCPL']['wa']:.4g}$ | undefined |",
                f"{label} $[{wfit['range'][0]:.3f},1]$ | ${wfit['w0']:.3f}$ | ${wfit['wa']:.4g}$ |",
                f"{label} $[0.01,{mufit['range'][1]:.3f}]$ | $({cpl['w0']:.3f},{cpl['wa']:.4g})$ | "
                f"{cpl['rmsResidualMag']:.3f} mag |",
                f"{label} ${wconst['w']:.3f}$ | {wconst['rmsResidualMag']:.3f} mag | "
                f"{model['muVsUniteCPL']['maxAbsDifferenceMag']:.3f} mag |",
            )
            for row in rows:
                row = row.replace("| $0.130$ |", "| 0.130 |")
                with self.subTest(row=row):
                    self.assertIn(row, self.text)
            self.assertEqual(model["wFitRequested"]["status"], "undefined")
            self.assertEqual(model["muFitRequested"]["status"], "undefined")
        dust = models[4]
        self.assertEqual(dust["wFitRequested"]["status"], "ok")
        self.assertEqual(dust["muFitRequested"]["status"], "ok")
        self.assertIn("| 0 | 0 | 0 | $(0,0)$ and $w=0$ |", self.text)
        self.assertLess(abs(dust["muFitRequested"]["cplOffsetProfiled"]["w0"]), 1e-9)
        self.assertLess(abs(dust["muFitRequested"]["wConstantOffsetProfiled"]["w"]), 1e-9)
        self.assertIn(f"| 0 | 0 | 0 | {dust['muVsUniteCPL']['maxAbsDifferenceMag']:.3f} mag |",
                      self.text)

    def test_epoch_tables_match_the_exp3_summary(self):
        for model in self.reports["e3"]["models"][:4]:
            label = f"{model['x0']:g}"
            row = (f"| ${label}$ | $z={model['zZero']:.3f}$, $a={model['aZero']:.3f}$ | "
                   f"$z={model['zPhantomCrossing']:#.3g}$, $a={model['aPhantomCrossing']:.3f}$ | "
                   f"$z={model['zBounce']:.3f}$, $a={model['aBounce']:.3f}$ |")
            with self.subTest(x0=model["x0"]):
                self.assertIn(row, self.text)
                self.assertFalse(model["contractBackwardRangeReachable"])
        runs = {run["id"]: run for run in self.reports["e3"]["runs"]}
        for name in ("x0_m0p462654_mu3", "x0_m0p433107_mu3", "x0_m0p3_mu3", "x0_m0p2_mu3"):
            change = runs[name]["measured"]["decelerationSignChanges"]
            self.assertEqual(len(change), 1)
            self.assertIn(f"$z={change[0]['z']:#.3g}$, $a={change[0]['a']:.3f}$", self.text)
        self.assertEqual(runs["x0_0_mu3"]["measured"]["decelerationSignChanges"], [])

    def test_unite_values_match_fits_json(self):
        unite = self.reports["fits"]["unite"]
        self.assertEqual((unite["w0"], unite["wa"], unite["wConstantBenchmark"]), (-0.861, -0.6, -0.764))
        self.assertIn("$(w_0,w_a)=(-0.861,-0.60)$", self.text)
        self.assertIn("$w=-0.764$", self.text)
        self.assertIn("| Unite CPL (PDF) | $(-0.861,-0.60)$ | none |", self.text)
        self.assertIn("| Unite wCDM (PDF) | none | $-0.764$ |", self.text)
        gamma = self.reports["fits"]["gammaVariant"]
        self.assertEqual((round(gamma["tangentCPLofPressureRatio"]["w0"], 12),
                          round(gamma["tangentCPLofPressureRatio"]["wa"], 12)), (-0.861, -0.6))
        self.assertIn("| deflation variant, $p/\\rho$ | $(-0.861,-0.60)$ | none |", self.text)
        newton = [o for o in gamma["objections"] if o["id"] == "newtonConstant"][0]
        self.assertEqual(f"{2 ** (-3 * gamma['gamma']):.3f}", "0.162")
        self.assertIn("$G_N(z=1)/G_N(0)=0.162$", self.text)
        self.assertEqual(round(newton["ratioToBound"], -2), 1800)
        self.assertIn("some 1800 times", self.text)
        self.assertIn("about 1800 times faster", self.text)
        einstein = [o for o in gamma["objections"] if o["id"] == "einstein8D"][0]
        self.assertIn("(0.382, 2.618)", einstein["statement"])
        self.assertIn("$(3-\\sqrt5)/2=0.382$ and $(3+\\sqrt5)/2=2.618$", self.text)

    def test_check_counts_match_the_reports(self):
        summary = self.reports["ns"]
        self.assertEqual(summary["verdict"], "SUCCESS")
        totals = summary["totals"]
        self.assertEqual((totals["rustFailed"], totals["pythonFailed"], totals["analysisFailed"]), (0, 0, 0))
        mathematica = self.reports["mm"]
        self.assertEqual(mathematica["verdict"], "SUCCESS")
        self.assertTrue(all(value is True for value in mathematica["checks"].values()))
        self.assertEqual(len(mathematica["checks"]), mathematica["checkCount"])
        groups = {}
        for name in mathematica["checks"]:
            key = re.match(r"(exp[1-5]|algebra|rustConstants|engine)", name)
            groups[key.group(1) if key else name] = groups.get(key.group(1) if key else name, 0) + 1
        self.assertEqual((groups["algebra"], groups["rustConstants"], groups["engine"]), (10, 7, 6))
        self.assertEqual(groups["textParametersMatchSummaries"], 1)
        self.assertEqual(groups["figuresExported"], 1)
        per_experiment = [groups[f"exp{n}"] for n in range(1, 6)]
        rust_total = python_total = 0
        for number, experiment in enumerate(summary["experiments"], start=1):
            rust, python = experiment["rust"], experiment["python"]
            self.assertEqual(experiment["experiment"], f"exp{number}")
            self.assertEqual(rust["failedCount"] + python["failedCount"], 0)
            self.assertTrue(python["repeatByteIdentity"] and python["refinedConvergence"])
            self.assertEqual(self.reports[f"p{number}"]["checkCount"], python["checkCount"])
            self.assertEqual(self.reports[f"e{number}"]["verdict"], "SUCCESS")
            row = (f"| EXP-{number} | {rust['checkCount']} of {rust['checkCount']} | "
                   f"{python['checkCount']} of {python['checkCount']} | "
                   f"{per_experiment[number - 1]} of {per_experiment[number - 1]} |")
            with self.subTest(experiment=number):
                self.assertIn(row, self.text)
                self.assertIn(f"passes {rust['checkCount']} of {rust['checkCount']} self-checks", self.text)
                self.assertIn(f" {python['checkCount']} of {python['checkCount']}", self.text)
            rust_total += rust["checkCount"]
            python_total += python["checkCount"]
        self.assertEqual((rust_total, python_total), (totals["rustChecks"], totals["pythonChecks"]))
        self.assertIn(f"| total | {rust_total} of {rust_total} | {python_total} of {python_total} | "
                      f"{sum(per_experiment)} of {sum(per_experiment)} |", self.text)
        self.assertIn(f"the remaining {mathematica['checkCount'] - sum(per_experiment)} of the "
                      f"Mathematica notebook's {mathematica['checkCount']} checks", self.text)
        analysis = summary["experiments"][2]["analysis"]
        self.assertEqual((analysis["checkCount"], analysis["failedCount"]), (9, 0))
        self.assertIn("the analysis 9 of 9", self.text)
        self.assertIn(f"Totals: {totals['rustChecks']} of {totals['rustChecks']} Rust self-checks, "
                      f"{totals['pythonChecks']} of {totals['pythonChecks']} checker checks and "
                      f"{totals['analysisChecks']} of {totals['analysisChecks']} analysis checks true; "
                      "verdict SUCCESS.", self.text)
        steps = f"{totals['solverSteps'] / 1e8:.3f}\\times10^8"
        evaluations = f"{totals['rhsEvaluations'] / 1e8:.3f}\\times10^8"
        self.assertIn(f"${steps}$ steps and ${evaluations}$ right-hand-side evaluations", self.text)

    def test_notebook_statements_match_the_notebook_report(self):
        notebook = self.reports["nb"]
        self.assertEqual(notebook["verdict"], "SUCCESS")
        results = {entry["name"]: entry for entry in notebook["gauntlet"]["results"]}
        self.assertTrue(all(entry["passed"] for entry in results.values()))
        self.assertEqual(notebook["gauntlet"]["passed"], notebook["gauntlet"]["count"])
        self.assertTrue(all(run["gauntletPassed"] for run in notebook["executions"]))
        self.assertEqual(len(notebook["executions"]), 2)
        self.assertTrue(notebook["crossExecution"]["identicalGauntletAndFigures"])
        fresh = results["fresh_outputs_byte_identical"]["detail"]
        counts = [(label, int(a), int(b)) for label, a, b in re.findall(r"(exp[\w-]*) (\d+)/(\d+)", fresh)]
        self.assertTrue(all(a == b for _, a, b in counts))
        total = sum(a for _, a, _ in counts)
        analysis = sum(a for label, a, _ in counts if label == "exp3-analysis")
        self.assertIn(f"all {total} written files ({total - analysis} from the program, "
                      f"{analysis} from the EXP-3 analysis)", self.text)
        self.assertIn(f"{total} of {total} freshly written files", self.text)
        stage1 = re.search(r"(\d+)/(\d+) checks", results["stage1_physics_verified"]["detail"])
        self.assertIn(f"the Stage-1 results ({stage1.group(1)} of {stage1.group(2)} checks)", self.text)
        quoted = re.search(r"(\d+) numbers quoted", results["prose_numbers_match_reports"]["detail"])
        self.assertIn(f"the {quoted.group(1)} numbers quoted in its markdown", self.text)
        propagator = re.search(r"= ([0-9.e+-]+) <=", results["exp1_exact_propagator"]["detail"])
        self.assertIn(f"propagator (${sci(float(propagator.group(1)), 2)}$)", self.text)
        quadrature = re.search(r": ([0-9.e+-]+)$", results["exp3_distance_quadrature"]["detail"])
        self.assertIn(f"comoving distance (${sci(float(quadrature.group(1)), 1)}$ from CVODE)", self.text)
        massless = re.search(r"at the end ([0-9.e+-]+)", results["exp4_massless_no_production"]["detail"])
        self.assertIn(f"$|\\beta_k|^2\\le{sci(float(massless.group(1)), 1)}$ (no production)", self.text)
        self.assertIn("a8fdff459adfe181573d7924b18bffbdf378fdb3", notebook["adaptedFrom"])
        self.assertIn("BSD-3-Clause", notebook["adaptedFrom"])
        self.assertIn("planet_Mercury/notebook", notebook["adaptedFrom"])

    def test_mathematica_provenance_statement(self):
        provenance = self.reports["mm"]["provenance"]
        for fragment in ("none of the three rustSolveIt repositories", "Win11 a8fdff45",
                         "macOS 5360157f", "Linux 6f58e02e", "294 Jupyter notebooks",
                         "DiracTriality.nb"):
            self.assertIn(fragment, provenance)
        engine = self.reports["mm"]["engine"]
        self.assertEqual((engine["command"], engine["exitCode"], engine["lastLine"]),
                         ("print-config", 0, "SUCCESS"))

    def test_pinned_solver_commits_match_the_setup_scripts(self):
        shell = (REPOSITORY_ROOT / "scripts" / "setup_solver.sh").read_text(encoding="utf-8")
        powershell = (REPOSITORY_ROOT / "scripts" / "setup_solver.ps1").read_text(encoding="utf-8")
        for name, commit in (("rustSolveIt_Win11_SUNDIALS_7_8_0", "a8fdff459adfe181573d7924b18bffbdf378fdb3"),
                             ("rustSolveIt_macos-silicon_SUNDIALS_7_8_0", "5360157f4f6160978f66400566c31b2ae25dd44d"),
                             ("rustSolveIt_linux_SUNDIALS_7_8_0", "6f58e02e53717a51375bd4bc5918edc57088d922")):
            with self.subTest(name=name):
                self.assertIn(f"https://github.com/once-ere/{name}\n  {commit}\n", self.text)
                for script in (shell, powershell):
                    self.assertIn(name, script)
                    self.assertIn(commit, script)

    def test_solver_settings_quoted_match_the_summaries(self):
        expectations = {
            1: ("BDF + Newton + dense linear solver, rtol $10^{-12}$, atol $10^{-14}$, max_step 0.02",
                "CVODE BDF + Newton + dense direct linear solver (DQ Jacobian)"),
            2: ("Adams + fixed point, rtol $10^{-12}$, atol $10^{-15}$, max_step 0.02",
                "CVODE Adams-Moulton + fixed-point (functional) iteration"),
            3: ("Adams + fixed point, rtol $10^{-11}$, atol $10^{-13}$, max_step 0.01 in $N$",
                "CVODE Adams-Moulton + fixed-point (functional) iteration"),
            4: ("Adams + fixed point, rtol $10^{-13}$, atol $10^{-14}$, max_step 2.0",
                "CVODE Adams-Moulton + fixed-point (functional) iteration"),
            5: ("Adams + fixed point, rtol $10^{-10}$, atol $10^{-12}$, max_step 0.02",
                "CVODE Adams-Moulton + fixed-point (functional) iteration"),
        }
        for number, (phrase, solver) in expectations.items():
            summary = self.reports[f"e{number}"]
            tolerances = summary["tolerances"]
            with self.subTest(experiment=number):
                self.assertEqual(summary["solver"], solver)
                self.assertFalse(summary["refined"])
                self.assertIn(phrase, self.text)
                rtol = re.search(r"rtol \$10\^\{(-\d+)\}\$", phrase).group(1)
                atol = re.search(r"atol \$10\^\{(-\d+)\}\$", phrase).group(1)
                step = re.search(r"max_step ([0-9.]+)", phrase).group(1)
                self.assertEqual(tolerances["rtol"], float("1e" + rtol))
                self.assertEqual(tolerances["atol"], float("1e" + atol))
                self.assertEqual(tolerances["maxStep"], float(step))

    def test_recorded_hashes_match_the_files_and_the_summary(self):
        summary = self.reports["ns"]
        fixture = summary["fixture"]["sha256"]
        self.assertEqual(sha256_file(FIXTURE), fixture)
        self.assertIn(f'FIXTURE_SHA256: &str = "{fixture}"', GENERATED_RS.read_text(encoding="utf-8"))
        for source in ("e1", "e2", "e3", "e4", "e5", "p1", "p2", "p3", "p4", "p5"):
            key = "fixture" if source.startswith("e") else "fixtureSha256"
            value = self.reports[source][key]
            self.assertEqual(value["sha256"] if isinstance(value, dict) else value, fixture)
        self.assertEqual(self.reports["mm"]["fixtureSha256"], fixture)
        expected = {
            "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json": fixture,
            "studies/dirac16complex_cosmology/src/generated.rs": sha256_file(GENERATED_RS),
        }
        for experiment in summary["experiments"]:
            for source in experiment["sources"]:
                path = "artifacts/dirac16complex/numerics/" + source["path"]
                self.assertEqual(sha256_file(REPOSITORY_ROOT / path), source["sha256"], path)
                expected[path] = source["sha256"]
        self.assertEqual(len(expected), 13)
        for path, digest in expected.items():
            with self.subTest(path=path):
                self.assertIn(path + "\n  " + digest + "\n", self.text)


def pdf_font_charsets(content: bytes) -> dict[str, set[str]]:
    """FontName -> set of glyph names in its /CharSet (object streams inflated)."""
    chunks = [content]
    for match in re.finditer(rb"stream\r?\n", content):
        start = match.end()
        end = content.find(b"endstream", start)
        try:
            chunks.append(zlib.decompress(content[start:end]))
        except zlib.error:
            pass
    text = b"\n".join(chunks)
    fonts = {}
    pattern = re.compile(rb"/FontName\s*/([A-Z]{6}\+[A-Za-z0-9-]+)(?:(?!/FontName).){0,600}?/CharSet\s*\(([^)]*)\)",
                         re.S)
    for match in pattern.finditer(text):
        fonts[match.group(1).decode()] = set(match.group(2).decode().strip("/").split("/"))
    return fonts


class PdfTests(unittest.TestCase):
    """pdflatex does not warn about these glyph substitutions, so the PDF itself is checked:
    no \\mathbb 1 (msbm slot 49 is 'notforces'), no '--' en-dash ligature and no curly
    left quote for a backtick in the typewriter font; and the 25 figures are embedded."""

    @classmethod
    def setUpClass(cls):
        cls.content = PDF.read_bytes()

    def test_no_notforces_endash_or_quoteleft_substitutions(self):
        fonts = pdf_font_charsets(self.content)
        mono = [name for name in fonts if "LMMono" in name]
        self.assertTrue(mono, sorted(fonts))
        for name in mono:
            self.assertNotIn("endash", fonts[name], name)
            self.assertNotIn("quoteleft", fonts[name], name)
        for name in fonts:
            if "MSBM" in name:
                self.assertNotIn("notforces", fonts[name], name)

    def test_figures_are_embedded_without_timestamps(self):
        images = re.findall(rb"/Subtype\s*/Image", self.content)
        self.assertGreaterEqual(len(images), len(FIGURE_ORDER))
        for marker in (b"/CreationDate", b"/ModDate", b"PTEX.", b"C:/Users", b"C:\\\\Users"):
            self.assertNotIn(marker, self.content)


if __name__ == "__main__":
    unittest.main()
