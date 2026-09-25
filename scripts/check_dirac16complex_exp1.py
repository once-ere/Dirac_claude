"""Independent checker of EXP-1 (primordial field, frozen dirac16complex).

numpy + standard library only.  Nothing the Rust program derived is taken as
truth: the gamma matrices are rebuilt from the algebra fixture, every
physical quantity is recomputed from the CSV *state* columns (u_re_*, u_im_*)
and the physics of NUMERICS_CONTRACT.md, and the derived CSV columns are only
compared against these recomputations.

Checks (each printed as check_<name>=true/false):
  provenance     fixture hash in summary.json == sha256(fixture) == generated.rs
  algebra        Clifford relations, C, B from the fixture
  structure      files present, headers, uniform grid, finite values
  background     a4 (numerical quadrature of a4'), a4'', scale factors, V,
                 Einstein requirement rho_req < 0 and p_req recomputed
  initial        the initial spinors are the claimed joint (h, B) eigenvectors
  derived        rho, p_j, S, KE/PE, w, norms recomputed from u
  fdResidual     five-point finite-difference residual of i du/dt = h u and of
                 the literal reduced equation gamma^4 du/dt = (M_eff - i K gamma^0) u,
                 bounded by 1.5 (dt^4/30) E^5 + 1e-6 (truncation estimate)
  kinetic        KE_L column vs (S0/2)(-Im u^dag du/dt) with du/dt by finite
                 differences (the definition K_4, not the on-shell formula)
  exact          u(t) vs exp(-i h t) u0 via numpy.linalg.eigh
  frozen         rho frozen for all runs, p_j and S for eigenstates;
                 mixed-state pressure oscillation equals the exact prediction
  eigenmodeLaws  p_0 = +-K^2/E, s = +-M/E on eigenmodes, K=0 dust (w = 0)
  norms          u^dag u and u^dag B u conserved
  profile        A=1 and A=2 spinor columns identical (<= 1e-12)
  lambdaRun      self-consistent M* (bisection) and M_eff(t) constant
  summary        Rust summary verdict/measurements consistent with the above
  optional       --repeat DIR: rerun the binary into DIR, byte-compare files;
                 --refined DIR: rerun with --refined, errors improve,
                 difference bounded.

Usage: python scripts/check_dirac16complex_exp1.py [--output ROOT]
       [--fixture PATH] [--binary PATH] [--repeat DIR] [--refined DIR]
Writes <ROOT>/exp1/python-check-report.json; exits 1 on any failed check.
"""

import argparse
import hashlib
import json
import math
import os
import subprocess
import sys

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_ROOT = os.path.join(REPO, "artifacts", "dirac16complex", "numerics")
DEFAULT_FIXTURE = os.path.join(REPO, "artifacts", "dirac16complex", "arbitrary-field",
                               "algebra-fixture.json")
GENERATED_RS = os.path.join(REPO, "studies", "dirac16complex_cosmology", "src", "generated.rs")
BINARY_NAME = "dirac16complex_cosmology" + (".exe" if os.name == "nt" else "")
DEFAULT_BINARY = os.path.join(REPO, "studies", "dirac16complex_cosmology", "target", "release",
                              BINARY_NAME)
EXPERIMENT = "exp1"
TRANSVERSE = [0, 1, 2, 3, 5, 6, 7]
ETA = np.array([1, 1, 1, 1, -1, -1, -1, -1], dtype=float)

# a-priori limits (same numbers the Rust program states, re-applied here)
EXACT_LIMIT = 1.0e-7
FROZEN_LIMIT = 1.0e-8
NORM_LIMIT = 1.0e-8
PROFILE_LIMIT = 1.0e-12
DERIVED_LIMIT = 1.0e-12     # recomputation vs CSV derived columns (absolute, O(1) values)
BACKGROUND_LIMIT = 1.0e-11  # quadrature a4 vs CSV a4
EIGEN_LIMIT = 1.0e-12


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def load_fixture_algebra(path):
    with open(path, "r", encoding="utf-8") as handle:
        document = json.load(handle)
    gammas = [np.array(g, dtype=float) for g in document["gamma"]]
    return gammas


def algebra_checks(gammas):
    identity = np.eye(16)
    clifford = all(np.array_equal(gammas[a] @ gammas[b] + gammas[b] @ gammas[a],
                                  2.0 * ETA[a] * identity if a == b else 0.0 * identity)
                   for a in range(8) for b in range(8))
    charge = gammas[0] @ gammas[1] @ gammas[2] @ gammas[3]
    b_matrix = -1j * (charge @ gammas[4])
    ok = (clifford and np.array_equal(charge, charge.T)
          and all(np.array_equal((charge @ g).T, -(charge @ g)) for g in gammas)
          and np.array_equal(b_matrix, b_matrix.conj().T)
          and np.allclose(b_matrix @ b_matrix, identity, atol=0.0, rtol=0.0))
    return ok, charge, b_matrix


def hamiltonian(gammas, m_eff, kh):
    """h = -i M gamma^4 - sum_{j != 4} kh[j] gamma^4 gamma^j."""
    h = -1j * m_eff * gammas[4]
    for j in TRANSVERSE:
        if kh[j] != 0.0:
            h = h - kh[j] * (gammas[4] @ gammas[j])
    return h.astype(complex)


def read_csv(path):
    with open(path, "r", encoding="utf-8", newline="") as handle:
        header = handle.readline().rstrip("\n").split(",")
    data = np.loadtxt(path, delimiter=",", skiprows=1, ndmin=2)
    return header, data


def run_binary(binary, arguments):
    completed = subprocess.run([binary] + arguments, cwd=REPO, capture_output=True,
                               text=True, encoding="utf-8")
    lines = completed.stdout.strip().splitlines()
    last = lines[-1] if lines else ""
    return completed.returncode == 0 and last == "SUCCESS", completed


def a4_prime(profile, t):
    amplitude, t1, t2, width = profile
    return amplitude * (1.0 + np.tanh((t - t1) / width)) * (1.0 - np.tanh((t - t2) / width)) / 4.0


def a4_second(profile, t):
    """Derivative of a4' written with sech^2 = 1/cosh^2 (independent form)."""
    amplitude, t1, t2, width = profile
    s1 = 1.0 / np.cosh((t - t1) / width) ** 2
    s2 = 1.0 / np.cosh((t - t2) / width) ** 2
    th1 = np.tanh((t - t1) / width)
    th2 = np.tanh((t - t2) / width)
    return amplitude / (4.0 * width) * (s1 * (1.0 - th2) - (1.0 + th1) * s2)


def a4_quadrature(profile, t):
    """a4(t) = int_{-inf}^t a4' dt' by composite Gauss-Legendre (40 nodes per
    panel of width 0.25) from t_lo = t1 - 40 width (tail < A e^{-80})."""
    amplitude, t1, t2, width = profile
    nodes, weights = np.polynomial.legendre.leggauss(40)
    t_lo = t1 - 40.0 * width
    panels = max(1, int(math.ceil((t - t_lo) / 0.25)))
    edges = np.linspace(t_lo, t, panels + 1)
    total = 0.0
    for left, right in zip(edges[:-1], edges[1:]):
        half = 0.5 * (right - left)
        mid = 0.5 * (right + left)
        total += half * np.dot(weights, a4_prime(profile, mid + half * nodes))
    return total


def einstein_requirement(a4p, a4pp, hubble, kappa):
    h2 = hubble * hubble
    rho = -3.0 * h2 * (7.0 + a4p ** 2) / kappa
    p0 = -3.0 * h2 * (a4p ** 2 - 5.0) / kappa
    ps = h2 * (15.0 - 3.0 * a4p ** 2 + a4pp) / kappa
    pt = h2 * (15.0 - 3.0 * a4p ** 2 - a4pp) / kappa
    return rho, [p0, ps, ps, ps, pt, pt, pt]


def exact_solution(h, u0, times):
    values, vectors = np.linalg.eigh(h)
    coefficients = vectors.conj().T @ u0
    phases = np.exp(-1j * np.outer(times, values))
    return (phases * coefficients[None, :]) @ vectors.T


def bilinear(u, m):
    """row-wise u^dag M u for u of shape (n, 16)."""
    return np.einsum("ni,ij,nj->n", u.conj(), m, u)


def self_consistent_mass(m, lam, s0, k):
    f = lambda mass: mass - m - lam * s0 * mass / math.sqrt(mass * mass + k * k)
    lo, hi = m - abs(lam * s0) - 1.0, m + abs(lam * s0) + 1.0
    lo = max(lo, 1.0e-12)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if (f(lo) < 0.0) == (f(mid) < 0.0):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# verification
# ---------------------------------------------------------------------------

def run_header():
    header = ["t"] + ["u_re_%d" % i for i in range(16)] + ["u_im_%d" % i for i in range(16)]
    header += ["S", "M_eff", "energy_mode", "rho"] + ["p_%d" % j for j in TRANSVERSE]
    header += ["p_mean", "w", "KE_L", "PE_L", "KE_H", "PE_H", "w_L", "norm_hilbert",
               "norm_krein", "exact_error"]
    return header


BACKGROUND_HEADER = ["t", "a4", "a4_prime", "a4_second", "scale_3space", "scale_extratime",
                     "volume_ratio", "theta", "rho_req", "p_req_0", "p_req_1", "p_req_2",
                     "p_req_3", "p_req_5", "p_req_6", "p_req_7", "p_mean_req", "w_req"]


def load_run(directory, run):
    header, data = read_csv(os.path.join(directory, run["file"]))
    u = data[:, 1:17] + 1j * data[:, 17:33]
    return header, data, u


def verify(root, fixture_path):
    checks = {}
    measurements = {}
    directory = os.path.join(root, EXPERIMENT)
    with open(os.path.join(directory, "summary.json"), "r", encoding="utf-8") as handle:
        summary = json.load(handle)

    # provenance ------------------------------------------------------------
    fixture_hash = sha256_file(fixture_path)
    with open(GENERATED_RS, "r", encoding="utf-8") as handle:
        generated = handle.read()
    checks["provenanceFixtureHash"] = (summary["fixture"]["sha256"] == fixture_hash
                                       and ('FIXTURE_SHA256: &str = "%s"' % fixture_hash) in generated
                                       and summary["fixture"]["source"] == "fixture")
    checks["provenanceSchema"] = (summary["schemaVersion"] == 1
                                  and summary["study"] == "dirac16complex-cosmology"
                                  and summary["experiment"] == EXPERIMENT)

    # algebra ---------------------------------------------------------------
    gammas = load_fixture_algebra(fixture_path)
    algebra_ok, charge, b_matrix = algebra_checks(gammas)
    checks["algebraFromFixture"] = algebra_ok
    minus_i_g4 = -1j * gammas[4]

    parameters = summary["parameters"]
    hubble, mass, kappa = parameters["H"], parameters["m"], parameters["kappa"]
    # NUMERICS_CONTRACT EXP-1: H = 1, m = 1, two profiles A = 1, 2, K in {0, 0.5, 2},
    # several spinors, lambda = 0 plus one lambda != 0 run (per profile here).
    lambda_runs = [run for run in summary["runs"] if run["lambda"] != 0.0]
    checks["parametersMatchContract"] = (
        hubble == 1.0 and mass == 1.0
        and sorted({run["amplitude"] for run in summary["runs"]}) == [1.0, 2.0]
        and sorted({run["hiddenMomentumK"] for run in summary["runs"] if run["lambda"] == 0.0})
        == [0.0, 0.5, 2.0]
        and len({run["initialSpinor"] for run in summary["runs"]}) >= 3
        and len(lambda_runs) == 2)
    t1, t2, width = parameters["windowT1"], parameters["windowT2"], parameters["windowWidth"]
    grid = summary["grid"]

    # structure -------------------------------------------------------------
    files_ok = all(os.path.exists(os.path.join(directory, name)) for name in summary["files"])
    checks["structureFilesPresent"] = files_ok
    expected_times = grid["tStart"] + (grid["tEnd"] - grid["tStart"]) * np.arange(
        grid["outputIntervals"] + 1) / grid["outputIntervals"]

    # background ------------------------------------------------------------
    background_ok = True
    rho_req_max = -math.inf
    background_dev = 0.0
    header_ok = True
    for entry in summary["backgrounds"]:
        profile = (entry["amplitude"], t1, t2, width)
        header, data = read_csv(os.path.join(directory, entry["file"]))
        header_ok &= header == BACKGROUND_HEADER
        t = data[:, 0]
        a4p = a4_prime(profile, t)
        a4pp = a4_second(profile, t)
        a4 = np.array([a4_quadrature(profile, x) for x in t])
        rho, p = einstein_requirement(a4p, a4pp, hubble, kappa)
        deviations = [
            np.max(np.abs(data[:, 1] - a4)),
            np.max(np.abs(data[:, 2] - a4p)),
            np.max(np.abs(data[:, 3] - a4pp)),
            np.max(np.abs(data[:, 4] / np.exp(a4) - 1.0)),
            np.max(np.abs(data[:, 5] / np.exp(-a4) - 1.0)),
            np.max(np.abs(data[:, 6] - 1.0)),
            np.max(np.abs(data[:, 7])),
            np.max(np.abs(data[:, 8] - rho)),
        ] + [np.max(np.abs(data[:, 9 + i] - p[i])) for i in range(7)]
        background_dev = max(background_dev, max(deviations))
        background_ok &= bool(np.max(np.abs(t - expected_times)) <= 1e-13)
        rho_req_max = max(rho_req_max, float(np.max(rho)))
    checks["backgroundRecomputed"] = background_ok and header_ok and background_dev <= BACKGROUND_LIMIT
    checks["einsteinSourceNegative"] = rho_req_max < 0.0
    measurements["backgroundMaxDeviation"] = background_dev
    measurements["rhoReqMax"] = rho_req_max

    # runs ------------------------------------------------------------------
    header_ok = True
    grid_ok = True
    finite_ok = True
    initial_ok = True
    derived_dev = 0.0
    fd_ok = True
    fd_worst_ratio = 0.0
    exact_max = 0.0
    frozen_rho = 0.0
    frozen_eigen = 0.0
    mixed_range_dev = 0.0
    mixed_range = 0.0
    law_dev = 0.0
    norm_drift = 0.0
    lambda_ok = True
    lambda_meff_drift = 0.0
    kinetic_dev = 0.0
    states = {}
    dt = (grid["tEnd"] - grid["tStart"]) / grid["outputIntervals"]
    for run in summary["runs"]:
        header, data, u = load_run(directory, run)
        header_ok &= header == run_header()
        t = data[:, 0]
        grid_ok &= bool(np.max(np.abs(t - expected_times)) <= 1e-13)
        finite_ok &= bool(np.all(np.isfinite(data)))
        states[run["id"]] = data[:, 1:33]
        k = run["hiddenMomentumK"]
        lam = run["lambda"]
        s0 = run["density"]
        kh = [k, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        u0 = u[0]

        # M_eff from the state (mean field), and the frozen reference Hamiltonian
        s_mode = bilinear(u, minus_i_g4).real
        m_eff_t = mass + lam * s0 * s_mode
        if lam != 0.0:
            m_star = self_consistent_mass(mass, lam, s0, k)
            lambda_ok &= abs(m_star - parameters["lambdaSelfConsistentMass"]) <= 1e-14
            lambda_ok &= abs(m_eff_t[0] - m_star) <= 1e-13
            lambda_meff_drift = max(lambda_meff_drift, float(np.max(np.abs(m_eff_t - m_star))))
            m_ref = m_star
        else:
            m_ref = mass
        h0 = hamiltonian(gammas, m_ref, kh)
        energy = math.sqrt(m_ref * m_ref + k * k)

        # initial eigenvector claims
        initial_ok &= abs(np.vdot(u0, u0).real - 1.0) <= 1e-14
        if run["energySign"] is not None:
            e_sign, b_sign = run["energySign"], run["kreinSign"]
            residual = max(np.max(np.abs(h0 @ u0 - e_sign * energy * u0)),
                           np.max(np.abs(b_matrix @ u0 - b_sign * u0)))
            initial_ok &= residual <= EIGEN_LIMIT

        # derived quantities recomputed from u
        rho_list, p_cols = [], []
        energy_mode = np.empty(len(t))
        p_mode = np.zeros((len(t), 7))
        for n in range(len(t)):
            h = hamiltonian(gammas, m_eff_t[n], kh)
            energy_mode[n] = np.vdot(u[n], h @ u[n]).real
            for slot, j in enumerate(TRANSVERSE):
                p_mode[n, slot] = -kh[j] * np.vdot(u[n], (gammas[4] @ gammas[j]) @ u[n]).real
        big_s = s0 * s_mode
        lagrangian = 0.5 * lam * big_s ** 2
        rho = s0 * energy_mode - lagrangian
        p = s0 * p_mode + lagrangian[:, None]
        p_mean = p.sum(axis=1) / 7.0
        ke_h = s0 * p_mode.sum(axis=1)
        pe_h = mass * big_s + 0.5 * lam * big_s ** 2
        ke_l = 0.5 * s0 * energy_mode
        pe_l = rho - ke_l
        hilbert = np.einsum("ni,ni->n", u.conj(), u).real
        krein = bilinear(u, b_matrix).real
        recomputed = [big_s, m_eff_t, energy_mode, rho] + [p[:, i] for i in range(7)] + [
            p_mean, p_mean / rho, ke_l, pe_l, ke_h, pe_h, (ke_l - pe_l) / (ke_l + pe_l),
            hilbert, krein]
        for column, values in zip(range(33, 33 + len(recomputed)), recomputed):
            derived_dev = max(derived_dev, float(np.max(np.abs(data[:, column] - values))))
        # identity rho = KE_H + PE_H (independent of the Rust split)
        derived_dev = max(derived_dev, float(np.max(np.abs(rho - (ke_h + pe_h)))))

        # five-point finite-difference residual of i du/dt = h u
        fd = (u[:-4] - 8.0 * u[1:-3] + 8.0 * u[3:-1] - u[4:]) / (12.0 * dt)
        rhs = np.array([-1j * (hamiltonian(gammas, m_eff_t[n], kh) @ u[n])
                        for n in range(2, len(t) - 2)])
        residual = np.max(np.linalg.norm(fd - rhs, axis=1))
        bound = 1.5 * dt ** 4 / 30.0 * energy ** 5 + 1.0e-6
        fd_ok &= residual <= bound
        fd_worst_ratio = max(fd_worst_ratio, residual / bound)
        # the literal reduced equation of NUMERICS_CONTRACT EXP-1 (no h used):
        # gamma^4 du/dt = (M_eff - i K gamma^0) u
        inner = slice(2, len(t) - 2)
        lhs = fd @ gammas[4].T
        rhs_reduced = (m_eff_t[inner, None] * u[inner]) - 1j * k * (u[inner] @ gammas[0].T)
        residual_reduced = np.max(np.linalg.norm(lhs - rhs_reduced, axis=1))
        fd_ok &= residual_reduced <= bound
        fd_worst_ratio = max(fd_worst_ratio, residual_reduced / bound)
        # KE_L from its definition (1/2) K_4 with K_4 = <Psi^dag C gamma^4 dPsi/dt + h.c.>/2
        # = -Im(u^dag du/dt) per mode, du/dt by finite differences
        k4_fd = -np.einsum("ni,ni->n", u[inner].conj(), fd).imag
        kinetic_dev = max(kinetic_dev,
                          float(np.max(np.abs(data[inner, header.index("KE_L")] - 0.5 * s0 * k4_fd))) / bound)

        # exact solution
        exact = exact_solution(h0, u0, t - t[0])
        error = np.max(np.linalg.norm(u - exact, axis=1))
        exact_max = max(exact_max, float(error))

        # frozen-ness
        frozen_rho = max(frozen_rho, float(np.max(np.abs(rho - rho[0]))))
        if run["energySign"] is not None:
            frozen_eigen = max(frozen_eigen, float(np.max(np.abs(p - p[0]))),
                               float(np.max(np.abs(big_s - big_s[0]))))
            if lam == 0.0:
                sign = run["energySign"]
                law_dev = max(law_dev,
                              float(np.max(np.abs(p_mode[:, 0] - sign * k * k / energy))),
                              float(np.max(np.abs(s_mode - sign * mass / energy))))
                if k == 0.0 and sign > 0.0:
                    # free massive rest mode: dust, KE_L = PE_L = m S / 2
                    law_dev = max(law_dev, float(np.max(np.abs(rho - mass))),
                                  float(np.max(np.abs(p_mean))),
                                  float(np.max(np.abs(ke_l - pe_l))))
        elif k != 0.0:
            p0_exact = -k * np.einsum("ni,ij,nj->n", exact.conj(), gammas[4] @ gammas[0], exact).real
            p0_num = p[:, 0]
            range_num = float(np.max(p0_num) - np.min(p0_num))
            range_exact = float(np.max(p0_exact) - np.min(p0_exact))
            mixed_range = max(mixed_range, range_num)
            mixed_range_dev = max(mixed_range_dev, abs(range_num - range_exact))
        norm_drift = max(norm_drift, float(np.max(np.abs(hilbert - hilbert[0]))),
                         float(np.max(np.abs(krein - krein[0]))))

    checks["structureHeaders"] = header_ok
    checks["structureGrid"] = grid_ok
    checks["structureFinite"] = finite_ok
    checks["initialJointEigenvectors"] = initial_ok
    checks["derivedColumnsRecomputed"] = derived_dev <= DERIVED_LIMIT
    checks["fdResidual"] = fd_ok
    checks["kineticFromTimeDerivative"] = kinetic_dev <= 1.0
    checks["exactSolution"] = exact_max <= EXACT_LIMIT
    checks["rhoFrozenAllRuns"] = frozen_rho <= FROZEN_LIMIT
    checks["pressuresAndSFrozenEigenstates"] = frozen_eigen <= FROZEN_LIMIT
    checks["mixedStateOscillationMatchesExact"] = mixed_range > 1e-3 and mixed_range_dev <= 1e-7
    checks["eigenmodeLaws"] = law_dev <= FROZEN_LIMIT
    checks["normsConserved"] = norm_drift <= NORM_LIMIT
    checks["lambdaRun"] = lambda_ok and lambda_meff_drift <= FROZEN_LIMIT
    measurements.update({
        "derivedMaxDeviation": derived_dev,
        "fdResidualWorstRatioToBound": fd_worst_ratio,
        "kineticFdWorstRatioToBound": kinetic_dev,
        "exactMaxError": exact_max,
        "rhoMaxDrift": frozen_rho,
        "eigenstatePressureOrSMaxDrift": frozen_eigen,
        "mixedStatePressureRange": mixed_range,
        "mixedStateRangeDeviationFromExact": mixed_range_dev,
        "eigenmodeLawMaxDeviation": law_dev,
        "normMaxDrift": norm_drift,
        "lambdaMeffMaxDrift": lambda_meff_drift,
    })

    # profile independence --------------------------------------------------
    labels = sorted({run["profile"] for run in summary["runs"]})
    profile_dev = 0.0
    pairs = 0
    for run in summary["runs"]:
        if run["profile"] != labels[0]:
            continue
        twin = run["id"].replace(labels[0], labels[1], 1)
        if twin in states:
            profile_dev = max(profile_dev, float(np.max(np.abs(states[run["id"]] - states[twin]))))
            pairs += 1
    checks["a4ProfileIndependence"] = pairs * 2 == len(summary["runs"]) and profile_dev <= PROFILE_LIMIT
    measurements["profileMaxDifference"] = profile_dev

    # Rust summary consistency ---------------------------------------------
    rust = summary["measurements"]
    checks["summaryConsistent"] = (
        summary["verdict"] == "SUCCESS" and all(summary["checks"].values())
        and abs(rust["maxExactError"] - exact_max) <= 1e-12
        and abs(rust["maxRhoDrift"] - frozen_rho) <= 1e-12
        and rust["maxProfileDifference"] == profile_dev)
    return checks, measurements, summary


def compare_repeat(root, repeat_root, summary):
    same = True
    for name in summary["files"]:
        with open(os.path.join(root, EXPERIMENT, name), "rb") as handle:
            left = handle.read()
        right_path = os.path.join(repeat_root, EXPERIMENT, name)
        if not os.path.exists(right_path):
            return False
        with open(right_path, "rb") as handle:
            right = handle.read()
        same &= left == right
    return same


def refined_convergence(root, refined_root, summary, fixture_path):
    gammas = load_fixture_algebra(fixture_path)
    with open(os.path.join(refined_root, EXPERIMENT, "summary.json"), "r", encoding="utf-8") as h:
        refined = json.load(h)
    ok = refined["refined"] is True and refined["verdict"] == "SUCCESS"
    tol, rtol = summary["tolerances"], refined["tolerances"]
    ok &= abs(rtol["rtol"] - tol["rtol"] / 10.0) <= 1e-30 and abs(rtol["maxStep"] - tol["maxStep"] / 2.0) <= 1e-18
    worst_diff = 0.0
    worst_canonical = 0.0
    improved = True
    parameters = summary["parameters"]
    for run in summary["runs"]:
        _, _, u = load_run(os.path.join(root, EXPERIMENT), run)
        _, _, ur = load_run(os.path.join(refined_root, EXPERIMENT), run)
        lam, k = run["lambda"], run["hiddenMomentumK"]
        m_ref = parameters["lambdaSelfConsistentMass"] if lam != 0.0 else parameters["m"]
        h0 = hamiltonian(gammas, m_ref, [k, 0, 0, 0, 0, 0, 0, 0])
        _, data_c = read_csv(os.path.join(root, EXPERIMENT, run["file"]))
        times = data_c[:, 0]
        exact = exact_solution(h0, u[0], times - times[0])
        error_c = float(np.max(np.linalg.norm(u - exact, axis=1)))
        error_r = float(np.max(np.linalg.norm(ur - exact, axis=1)))
        improved &= error_r < error_c
        worst_canonical = max(worst_canonical, error_c)
        worst_diff = max(worst_diff, float(np.max(np.linalg.norm(u - ur, axis=1))))
    ok &= improved and worst_diff <= 2.0 * worst_canonical + 1e-12
    return ok, worst_diff, worst_canonical


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=DEFAULT_ROOT)
    parser.add_argument("--fixture", default=DEFAULT_FIXTURE)
    parser.add_argument("--binary", default=DEFAULT_BINARY)
    parser.add_argument("--repeat")
    parser.add_argument("--refined")
    arguments = parser.parse_args(argv)
    root = os.path.abspath(arguments.output)
    checks, measurements, summary = verify(root, arguments.fixture)
    if arguments.repeat:
        ran, _ = run_binary(arguments.binary, [EXPERIMENT, "--output", os.path.abspath(arguments.repeat)])
        checks["repeatByteIdentity"] = ran and compare_repeat(root, os.path.abspath(arguments.repeat), summary)
    if arguments.refined:
        refined_root = os.path.abspath(arguments.refined)
        ran, _ = run_binary(arguments.binary, [EXPERIMENT, "--refined", "--output", refined_root])
        ok, diff, canonical = (False, float("nan"), float("nan"))
        if ran:
            ok, diff, canonical = refined_convergence(root, refined_root, summary, arguments.fixture)
        checks["refinedConvergence"] = ok
        measurements["refinedMaxDifference"] = diff
        measurements["canonicalMaxExactError"] = canonical
    checks = {name: bool(value) for name, value in checks.items()}
    measurements = {name: float(value) for name, value in measurements.items()}
    failed = [name for name, value in checks.items() if not value]
    for name, value in checks.items():
        print("check_%s=%s" % (name, "true" if value else "false"))
    for name, value in measurements.items():
        print("measurement_%s=%r" % (name, value))
    print("check_count=%d" % len(checks))
    print("failed_check_count=%d" % len(failed))
    report = {
        "schemaVersion": 1,
        "checker": "scripts/check_dirac16complex_exp1.py",
        "experiment": EXPERIMENT,
        "fixtureSha256": sha256_file(arguments.fixture),
        "checks": checks,
        "measurements": measurements,
        "checkCount": len(checks),
        "failedCheckCount": len(failed),
        "verdict": "SUCCESS" if not failed else "FAILURE",
    }
    with open(os.path.join(root, EXPERIMENT, "python-check-report.json"), "w", encoding="utf-8",
              newline="\n") as handle:
        handle.write(json.dumps(report, indent=2) + "\n")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
