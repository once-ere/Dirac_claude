"""Independent checker of EXP-5 (extra-time sector, ultrahyperbolic instability).

numpy + standard library only.  The gamma matrices are rebuilt from the
algebra fixture; everything is recomputed from the CSV *state* columns and the
physics of NUMERICS_CONTRACT.md:

  h(t) = -i m gamma^4 - Q(t) gamma^4 gamma^5,  Q = q e^{H t},
  E^2 = m^2 - Q^2 < 0 for t > t* = ln(m/q)/H.

Checks (check_<name>=true/false):
  provenance / algebra / structure / parametersMatchContract
  columnsRecomputed   Q, E^2, kappa, W (W by Gauss-Legendre quadrature of
                      sqrt(Q^2 - m^2), not the closed form), norms, drifts
  initialEigenvector  u0 = +E0 eigenvector of h(0) and a C = +-1 eigenvector
  fdResidual          five-point finite-difference residual of i du/dt = h u
  referenceSolution   independent classical RK4 (64 substeps per output
                      interval, Richardson-checked against 32) vs the CSV
  kreinConserved      |d(u^dag B u)| / max(u^dag u, 1) <= 1e-8, and the absolute
                      drift <= 1e-8 up to t*
  superExponential    growth rates on [t*, t*+1], [t*+1, t*+2], [t*+2, t*+3]
                      strictly increasing, late/early > 2, u^dag u > 1e10
  wkbLeading          ln(u^dag u) growth over [t*+1.5, t*+3] vs 2 int kappa,
                      relative deviation <= 1e-2
  wkbFirstOrder       vs 2 int kappa - int m^2/kappa^2, <= 2e-3
  wkbLateRate         d ln(u^dag u)/dt at the last interior point vs
                      2 kappa - m^2/kappa^2, relative <= 5e-3
  summaryConsistent   Rust summary agrees with the recomputation
  optional --repeat DIR / --refined DIR as for EXP-1.

Usage: python scripts/check_dirac16complex_exp5.py [--output ROOT]
       [--fixture PATH] [--binary PATH] [--repeat DIR] [--refined DIR]
Writes <ROOT>/exp5/python-check-report.json; exits 1 on any failed check.
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
EXPERIMENT = "exp5"
ETA = np.array([1, 1, 1, 1, -1, -1, -1, -1], dtype=float)

KREIN_LIMIT = 1.0e-8
WKB0_LIMIT = 1.0e-2
WKB1_LIMIT = 2.0e-3
LATE_RATE_LIMIT = 5.0e-3
REFERENCE_LIMIT = 1.0e-6
EIGEN_LIMIT = 1.0e-12
RK4_SUBSTEPS = 64


def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def load_gammas(path):
    with open(path, "r", encoding="utf-8") as handle:
        return [np.array(g, dtype=float) for g in json.load(handle)["gamma"]]


def read_csv(path):
    with open(path, "r", encoding="utf-8", newline="") as handle:
        header = handle.readline().rstrip("\n").split(",")
    return header, np.loadtxt(path, delimiter=",", skiprows=1, ndmin=2)


def run_binary(binary, arguments):
    completed = subprocess.run([binary] + arguments, cwd=REPO, capture_output=True,
                               text=True, encoding="utf-8")
    lines = completed.stdout.strip().splitlines()
    return completed.returncode == 0 and bool(lines) and lines[-1] == "SUCCESS"


def expected_header():
    header = ["t", "Q", "E2", "kappa", "wkb_W"]
    header += ["u_re_%d" % i for i in range(16)] + ["u_im_%d" % i for i in range(16)]
    return header + ["norm_hilbert", "norm_krein", "ln_norm_hilbert", "krein_drift",
                     "krein_drift_normalized"]


class Model:
    def __init__(self, gammas, mass, hubble, q):
        self.g4 = gammas[4].astype(complex)
        self.g45 = (gammas[4] @ gammas[5]).astype(complex)
        self.mass, self.hubble, self.q = mass, hubble, q

    def big_q(self, t):
        return self.q * np.exp(self.hubble * t)

    def h(self, t):
        return -1j * self.mass * self.g4 - self.big_q(t) * self.g45

    def rhs(self, t, u):
        return -1j * (self.h(t) @ u)


def rk4_reference(model, u0_columns, times, substeps):
    """Classical RK4 with `substeps` equal steps inside every output interval."""
    out = [u0_columns.copy()]
    u = u0_columns.copy()
    for left, right in zip(times[:-1], times[1:]):
        step = (right - left) / substeps
        t = left
        for _ in range(substeps):
            k1 = model.rhs(t, u)
            k2 = model.rhs(t + 0.5 * step, u + 0.5 * step * k1)
            k3 = model.rhs(t + 0.5 * step, u + 0.5 * step * k2)
            k4 = model.rhs(t + step, u + step * k3)
            u = u + (step / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
            t += step
        out.append(u.copy())
    return np.array(out)  # (n_times, 16, n_columns)


def wkb_quadrature(model, t_star, t):
    """int_{t*}^t sqrt(Q^2 - m^2) dt' by Gauss-Legendre in s = sqrt(t' - t*)
    (removes the square-root endpoint singularity), 48 nodes per panel."""
    if t <= t_star:
        return 0.0
    nodes, weights = np.polynomial.legendre.leggauss(48)
    s_max = math.sqrt(t - t_star)
    edges = np.linspace(0.0, s_max, 9)
    total = 0.0
    for left, right in zip(edges[:-1], edges[1:]):
        half, mid = 0.5 * (right - left), 0.5 * (right + left)
        s = mid + half * nodes
        tt = t_star + s * s
        integrand = np.sqrt(np.maximum(model.big_q(tt) ** 2 - model.mass ** 2, 0.0)) * 2.0 * s
        total += half * np.dot(weights, integrand)
    return total


def verify(root, fixture_path):
    checks, measurements = {}, {}
    directory = os.path.join(root, EXPERIMENT)
    with open(os.path.join(directory, "summary.json"), "r", encoding="utf-8") as handle:
        summary = json.load(handle)
    fixture_hash = sha256_file(fixture_path)
    with open(GENERATED_RS, "r", encoding="utf-8") as handle:
        generated = handle.read()
    checks["provenanceFixtureHash"] = (summary["fixture"]["sha256"] == fixture_hash
                                       and ('FIXTURE_SHA256: &str = "%s"' % fixture_hash) in generated)
    checks["provenanceSchema"] = (summary["schemaVersion"] == 1 and summary["experiment"] == EXPERIMENT)
    gammas = load_gammas(fixture_path)
    identity = np.eye(16)
    charge = gammas[0] @ gammas[1] @ gammas[2] @ gammas[3]
    b_matrix = -1j * (charge @ gammas[4])
    checks["algebraFromFixture"] = (
        all(np.array_equal(gammas[a] @ gammas[b] + gammas[b] @ gammas[a],
                           (2.0 * ETA[a] if a == b else 0.0) * identity)
            for a in range(8) for b in range(8))
        and np.array_equal(b_matrix, b_matrix.conj().T) and np.allclose(b_matrix @ b_matrix, identity))

    parameters = summary["parameters"]
    mass, hubble = parameters["m"], parameters["H"]
    checks["parametersMatchContract"] = (
        mass == 1.0 and hubble == 1.0 and sorted(parameters["qValues"]) == [0.05, 0.1]
        and parameters["extraTime"] == 3.0 and parameters["momentumDirection"] == 5)
    checks["structureFilesPresent"] = all(os.path.exists(os.path.join(directory, f))
                                          for f in summary["files"])

    header_ok = finite_ok = grid_ok = True
    column_dev = 0.0
    initial_ok = True
    fd_ok = True
    fd_ratio = 0.0
    krein_norm_max = krein_before_max = 0.0
    growth_ok = True
    dev0_max = dev1_max = late_max = 0.0
    wkb_quad_dev = 0.0
    summary_dev = 0.0
    loaded = {}
    for run in summary["runs"]:
        header, data = read_csv(os.path.join(directory, run["file"]))
        header_ok &= header == expected_header()
        finite_ok &= bool(np.all(np.isfinite(data)))
        loaded[run["id"]] = data
        q = run["q"]
        model = Model(gammas, mass, hubble, q)
        t_star = math.log(mass / q) / hubble
        t_end = t_star + parameters["extraTime"]
        t = data[:, 0]
        n = len(t) - 1
        grid_ok &= n == parameters["outputIntervals"] and abs(t[-1] - t_end) <= 1e-14 and \
            bool(np.max(np.abs(t - t_end * np.arange(n + 1) / n)) <= 1e-13)
        u = data[:, 5:21] + 1j * data[:, 21:37]

        # recomputed columns
        big_q = model.big_q(t)
        e2 = mass ** 2 - big_q ** 2
        kappa = np.sqrt(np.maximum(-e2, 0.0))
        hilbert = np.einsum("ni,ni->n", u.conj(), u).real
        krein = np.einsum("ni,ij,nj->n", u.conj(), b_matrix, u).real
        drift = krein - krein[0]
        normalized = drift / np.maximum(hilbert, 1.0)
        for column, values, scale in ((1, big_q, big_q), (2, e2, np.maximum(np.abs(e2), 1.0)),
                                      (3, kappa, np.maximum(kappa, 1.0)),
                                      (37, hilbert, hilbert), (39, np.log(hilbert), np.maximum(np.abs(np.log(hilbert)), 1.0)),
                                      (40, drift, np.maximum(hilbert, 1.0)),
                                      (41, normalized, 1.0)):
            column_dev = max(column_dev, float(np.max(np.abs(data[:, column] - values) / scale)))
        column_dev = max(column_dev, float(np.max(np.abs(data[:, 38] - krein) / np.maximum(hilbert, 1.0))))
        for index in range(0, n + 1, 25):
            wkb_quad_dev = max(wkb_quad_dev, abs(data[index, 4] - wkb_quadrature(model, t_star, t[index])))
        wkb_quad_dev = max(wkb_quad_dev, abs(data[n, 4] - wkb_quadrature(model, t_star, t[n])))

        # initial eigenvector
        u0 = u[0]
        e0 = math.sqrt(mass ** 2 - q ** 2)
        initial_ok &= abs(np.vdot(u0, u0).real - 1.0) <= 1e-14
        initial_ok &= float(np.max(np.abs(model.h(0.0) @ u0 - e0 * u0))) <= EIGEN_LIMIT
        initial_ok &= float(np.max(np.abs(charge @ u0 - run["cSign"] * u0))) <= EIGEN_LIMIT
        initial_ok &= abs(krein[0] - run["cSign"] * e0 / mass) <= 1e-13

        # five-point finite-difference residual
        dt = t[1] - t[0]
        fd = (u[:-4] - 8.0 * u[1:-3] + 8.0 * u[3:-1] - u[4:]) / (12.0 * dt)
        rhs = np.array([model.rhs(t[i], u[i]) for i in range(2, n - 1)])
        rel = np.linalg.norm(fd - rhs, axis=1) / np.linalg.norm(rhs, axis=1)
        lam = np.sqrt(np.abs(e2[2:n - 1])) + hubble
        bound = 2.0 * (dt * lam) ** 4 / 30.0 + 1e-6
        fd_ok &= bool(np.all(rel <= bound))
        fd_ratio = max(fd_ratio, float(np.max(rel / bound)))

        # Krein conservation
        krein_norm_max = max(krein_norm_max, float(np.max(np.abs(normalized))))
        krein_before_max = max(krein_before_max, float(np.max(np.abs(drift[t <= t_star]))))

        # super-exponential growth
        ln_norm = np.log(hilbert)
        idx = [int(np.argmax(t >= t_star + offset)) for offset in (0.0, 1.0, 2.0)] + [n]
        rates = [(ln_norm[idx[i + 1]] - ln_norm[idx[i]]) / (t[idx[i + 1]] - t[idx[i]])
                 for i in range(3)]
        growth_ok &= rates[0] > 0.0 and rates[0] < rates[1] < rates[2] and rates[2] > 2.0 * rates[0] \
            and hilbert[-1] > 1e10

        # WKB comparison over [t* + 1.5, t_end]
        ia = int(np.argmax(t >= t_star + parameters["wkbWindowStart"]))
        gamma_num = ln_norm[n] - ln_norm[ia]
        w_a = wkb_quadrature(model, t_star, t[ia])
        w_b = wkb_quadrature(model, t_star, t[n])
        gamma0 = 2.0 * (w_b - w_a)
        qa, qb = model.big_q(t[ia]), model.big_q(t[n])
        gamma1 = gamma0 - 0.5 * (math.log(1.0 - mass ** 2 / qb ** 2) - math.log(1.0 - mass ** 2 / qa ** 2)) / hubble
        dev0 = abs(gamma_num - gamma0) / gamma0
        dev1 = abs(gamma_num - gamma1) / gamma1
        dev0_max, dev1_max = max(dev0_max, dev0), max(dev1_max, dev1)
        i_late = n - 2
        rate_fd = (ln_norm[i_late - 2] - 8.0 * ln_norm[i_late - 1] + 8.0 * ln_norm[i_late + 1]
                   - ln_norm[i_late + 2]) / (12.0 * dt)
        k_late = kappa[i_late]
        rate_wkb = 2.0 * k_late - mass ** 2 / k_late ** 2
        late_max = max(late_max, abs(rate_fd - rate_wkb) / rate_wkb)

        wkb = run["wkb"]
        summary_dev = max(summary_dev, abs(wkb["gammaNumeric"] - gamma_num),
                          abs(wkb["gammaLeading"] - gamma0), abs(wkb["gammaFirstOrder"] - gamma1),
                          abs(run["kreinDrift"]["maxNormalized"] - float(np.max(np.abs(normalized)))),
                          abs(run["tStar"] - t_star))

    # independent RK4 reference, batched per q
    reference_err = 0.0
    richardson = 0.0
    for q in sorted({run["q"] for run in summary["runs"]}):
        runs = [run for run in summary["runs"] if run["q"] == q]
        datas = [loaded[run["id"]] for run in runs]
        t = datas[0][:, 0]
        u0 = np.stack([d[0, 5:21] + 1j * d[0, 21:37] for d in datas], axis=1)
        model = Model(gammas, mass, hubble, q)
        ref = rk4_reference(model, u0, t, RK4_SUBSTEPS)
        coarse = rk4_reference(model, u0, t, RK4_SUBSTEPS // 2)
        for column, d in enumerate(datas):
            u = d[:, 5:21] + 1j * d[:, 21:37]
            r = ref[:, :, column]
            scale = np.linalg.norm(r, axis=1)
            reference_err = max(reference_err, float(np.max(np.linalg.norm(u - r, axis=1) / scale)))
            richardson = max(richardson, float(np.max(np.linalg.norm(coarse[:, :, column] - r, axis=1)
                                                      / scale)) / 15.0)

    checks["structureHeaders"] = header_ok
    checks["structureFinite"] = finite_ok
    checks["structureGrid"] = grid_ok
    checks["columnsRecomputed"] = column_dev <= 1e-12 and wkb_quad_dev <= 1e-10
    checks["initialEigenvector"] = initial_ok
    checks["fdResidual"] = fd_ok
    checks["referenceSolution"] = reference_err <= REFERENCE_LIMIT and richardson <= 1e-2 * REFERENCE_LIMIT
    checks["kreinConservedNormalized"] = krein_norm_max <= KREIN_LIMIT
    checks["kreinConservedBeforeTStar"] = krein_before_max <= KREIN_LIMIT
    checks["superExponentialGrowth"] = growth_ok
    checks["wkbLeading"] = dev0_max <= WKB0_LIMIT
    checks["wkbFirstOrder"] = dev1_max <= WKB1_LIMIT
    checks["wkbLateRate"] = late_max <= LATE_RATE_LIMIT
    checks["summaryConsistent"] = (summary["verdict"] == "SUCCESS" and all(summary["checks"].values())
                                   and summary_dev <= 1e-9)
    measurements.update({
        "columnMaxDeviation": column_dev,
        "wkbClosedFormVsQuadrature": wkb_quad_dev,
        "fdResidualWorstRatioToBound": fd_ratio,
        "referenceMaxRelativeError": reference_err,
        "referenceRichardsonEstimate": richardson,
        "kreinMaxNormalizedDrift": krein_norm_max,
        "kreinMaxDriftBeforeTStar": krein_before_max,
        "wkbLeadingMaxRelDev": dev0_max,
        "wkbFirstOrderMaxRelDev": dev1_max,
        "wkbLateRateMaxRelDev": late_max,
        "summaryMaxDeviation": summary_dev,
    })
    return checks, measurements, summary, loaded


def compare_repeat(root, repeat_root, summary):
    for name in summary["files"]:
        right = os.path.join(repeat_root, EXPERIMENT, name)
        if not os.path.exists(right):
            return False
        with open(os.path.join(root, EXPERIMENT, name), "rb") as a, open(right, "rb") as b:
            if a.read() != b.read():
                return False
    return True


def refined_convergence(root, refined_root, summary, loaded, fixture_path):
    with open(os.path.join(refined_root, EXPERIMENT, "summary.json"), "r", encoding="utf-8") as h:
        refined = json.load(h)
    ok = refined["refined"] is True and refined["verdict"] == "SUCCESS"
    ok &= abs(refined["tolerances"]["rtol"] - summary["tolerances"]["rtol"] / 10.0) <= 1e-30
    gammas = load_gammas(fixture_path)
    mass, hubble = summary["parameters"]["m"], summary["parameters"]["H"]
    worst_c = worst_r = worst_diff = 0.0
    improved = True
    for run in summary["runs"]:
        _, dr = read_csv(os.path.join(refined_root, EXPERIMENT, run["file"]))
        dc = loaded[run["id"]]
        t = dc[:, 0]
        model = Model(gammas, mass, hubble, run["q"])
        u0 = (dc[0, 5:21] + 1j * dc[0, 21:37])[:, None]
        ref = rk4_reference(model, u0, t, RK4_SUBSTEPS)[:, :, 0]
        scale = np.linalg.norm(ref, axis=1)
        uc = dc[:, 5:21] + 1j * dc[:, 21:37]
        ur = dr[:, 5:21] + 1j * dr[:, 21:37]
        error_c = float(np.max(np.linalg.norm(uc - ref, axis=1) / scale))
        error_r = float(np.max(np.linalg.norm(ur - ref, axis=1) / scale))
        improved &= error_r < error_c
        worst_c, worst_r = max(worst_c, error_c), max(worst_r, error_r)
        worst_diff = max(worst_diff, float(np.max(np.linalg.norm(uc - ur, axis=1) / scale)))
    ok &= improved and worst_diff <= 2.0 * worst_c
    return ok, worst_diff, worst_c, worst_r


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=DEFAULT_ROOT)
    parser.add_argument("--fixture", default=DEFAULT_FIXTURE)
    parser.add_argument("--binary", default=DEFAULT_BINARY)
    parser.add_argument("--repeat")
    parser.add_argument("--refined")
    arguments = parser.parse_args(argv)
    root = os.path.abspath(arguments.output)
    checks, measurements, summary, loaded = verify(root, arguments.fixture)
    if arguments.repeat:
        ran = run_binary(arguments.binary, [EXPERIMENT, "--output", os.path.abspath(arguments.repeat)])
        checks["repeatByteIdentity"] = ran and compare_repeat(root, os.path.abspath(arguments.repeat), summary)
    if arguments.refined:
        refined_root = os.path.abspath(arguments.refined)
        ran = run_binary(arguments.binary, [EXPERIMENT, "--refined", "--output", refined_root])
        ok, diff, err_c, err_r = False, float("nan"), float("nan"), float("nan")
        if ran:
            ok, diff, err_c, err_r = refined_convergence(root, refined_root, summary, loaded,
                                                         arguments.fixture)
        checks["refinedConvergence"] = ok
        measurements["refinedMaxRelativeDifference"] = diff
        measurements["canonicalMaxRelativeError"] = err_c
        measurements["refinedMaxRelativeError"] = err_r
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
        "checker": "scripts/check_dirac16complex_exp5.py",
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
