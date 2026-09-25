"""Independent checker of EXP-4 (dirac16complex Fermi gas and pair creation).

numpy + standard library only.  The gamma matrices are rebuilt from the
algebra fixture and every observable is recomputed from the CSV *state*
columns (u_re_*, u_im_*) and the physics of NUMERICS_CONTRACT.md; the Rust
derived columns are only compared against, never used as truth:

  h = -i m gamma^4 - K gamma^4 gamma^1,  K = k/a,  E = sqrt(m^2 + K^2),
  dh/dt = K H gamma^4 gamma^1,
  eps = u^dag h u, p_1 = -K u^dag gamma^4 gamma^1 u, s = u^dag (-i gamma^4) u,
  beta2 = |P_- u|^2/|u|^2, beta2_adiabatic = |P_- u + i/(4E^2) P_- hdot P_+ u|^2/|u|^2.

(a) thermal gas: a = (t/t_i)^{1/2}, t_i = 1/(2 H_i); rho = (16/(2 pi^2 a^3))
    sum w k^2 f eps, p = ... p_1/3; kinetic theory by an independent composite
    Gauss-Legendre quadrature (60 panels x 16 nodes) of the closed-form
    integrands k^2 f E and k^2 f K^2/(3E).
(b) pair creation: a = e^t (t < 0), (1 + 2t)^{1/2} (t > 0);
    n a^3 = (16/(2 pi^2)) int k^2 |beta_k|^2 dk.
Independent references: classical RK4 of the full 16-component mode equation
(numpy, step c/max(E, H), c = 0.004, Richardson-checked with c = 0.008) for two
thermal modes (a <= 3) and four pair modes (t0 -> kink -> third radiation
sample).

Usage: python scripts/check_dirac16complex_exp4.py [--output ROOT]
       [--fixture PATH] [--binary PATH] [--repeat DIR] [--refined DIR]
Writes <ROOT>/exp4/python-check-report.json; exits 1 on any failed check.
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
EXPERIMENT = "exp4"
ETA = np.array([1, 1, 1, 1, -1, -1, -1, -1], dtype=float)

# limits (identical to the a priori limits of src/exp4.rs)
EIGEN_LIMIT = 1.0e-12
UNITARITY_LIMIT = 1.0e-6
KREIN_LIMIT = 1.0e-6
KINETIC_LIMIT = 1.0e-6
SPIN_LIMIT = 1.0e-6
ANTIPARTICLE_LIMIT = 1.0e-6
BETA_LIMIT = 1.0e-6
MASSLESS_BETA_LIMIT = 1.0e-10
SUDDEN_START_LIMIT = 0.1
SUDDEN_START_FLOOR = 1.0e-10
BETA_FLOOR = 1.0e-12
TAIL_LIMIT = 0.35
TAIL_K = 8.0
W_EARLY_LIMIT = 5.0e-3
W_LATE_MAX = 0.05
PAIR_W_LATE_MAX = 1.0e-3
REFERENCE_LIMIT = 1.0e-6
RECOMPUTE_LIMIT = 1.0e-12
RK4_C = 0.004
THERMAL_REFERENCE_NODES = (2, 12)
THERMAL_REFERENCE_A_MAX = 3.0
PAIR_REFERENCE_MODES = ((0.1, 33), (0.5, 30), (1.0, 36), (2.0, 39))
PAIR_REFERENCE_SAMPLES = 4  # t0, kink, first two radiation samples


def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def read_csv(path):
    with open(path, "r", encoding="utf-8", newline="") as handle:
        header = handle.readline().rstrip("\n").split(",")
    return header, np.loadtxt(path, delimiter=",", skiprows=1, ndmin=2)


def run_binary(binary, arguments):
    completed = subprocess.run([binary] + arguments, cwd=REPO, capture_output=True,
                               text=True, encoding="utf-8")
    lines = completed.stdout.strip().splitlines()
    return completed.returncode == 0 and bool(lines) and lines[-1] == "SUCCESS"


def state_columns():
    return ["u_re_%d" % i for i in range(16)] + ["u_im_%d" % i for i in range(16)]


THERMAL_HEADER = (["node", "k", "t", "a", "H", "K"] + state_columns()
                  + ["E", "eps", "p1", "s", "norm_hilbert", "norm_krein", "beta2",
                     "beta2_adiabatic"])
PAIR_HEADER = (["m", "node", "k", "t", "a", "H", "K"] + state_columns()
               + ["E", "eps", "p1", "norm_hilbert", "norm_krein", "beta2", "beta2_adiabatic"])


class Algebra:
    def __init__(self, fixture_path):
        with open(fixture_path, "r", encoding="utf-8") as handle:
            self.gamma = [np.array(g, dtype=float) for g in json.load(handle)["gamma"]]
        g = self.gamma
        self.g4 = g[4]
        self.g41 = g[4] @ g[1]
        self.charge = g[0] @ g[1] @ g[2] @ g[3]
        self.b = -1j * (self.charge @ g[4])

    def clifford_ok(self):
        identity = np.eye(16)
        ok = all(np.array_equal(self.gamma[a] @ self.gamma[b] + self.gamma[b] @ self.gamma[a],
                                (2.0 * ETA[a] if a == b else 0.0) * identity)
                 for a in range(8) for b in range(8))
        return ok and np.array_equal(self.b, self.b.conj().T) and np.allclose(self.b @ self.b,
                                                                               identity)

    def h(self, mass, kk):
        return -1j * mass * self.g4 - kk * self.g41

    def observables(self, u, mass, kk, hubble, sign):
        """Row-wise observables of states u (n, 16); sign = +1 particle
        modes, -1 negative-energy modes (beta = weight on the other sector)."""
        mass = np.broadcast_to(np.asarray(mass, dtype=float), kk.shape)
        energy = np.sqrt(mass ** 2 + kk ** 2)
        g4u = u @ self.g4.T
        g41u = u @ self.g41.T
        hu = -1j * mass[:, None] * g4u - kk[:, None] * g41u
        norm = np.einsum("ni,ni->n", u.conj(), u).real
        eps = np.einsum("ni,ni->n", u.conj(), hu).real
        p1 = -kk * np.einsum("ni,ni->n", u.conj(), g41u).real
        s = np.einsum("ni,ni->n", u.conj(), -1j * g4u).real
        krein = np.einsum("ni,ni->n", u.conj(), u @ self.b.T).real
        other = 0.5 * (u - sign * hu / energy[:, None])
        own = 0.5 * (u + sign * hu / energy[:, None])
        rate_own = (kk * hubble)[:, None] * (own @ self.g41.T)
        h_rate_own = -1j * mass[:, None] * (rate_own @ self.g4.T) - kk[:, None] * (
            rate_own @ self.g41.T)
        projected = 0.5 * (rate_own - sign * h_rate_own / energy[:, None])
        adiabatic = other + 1j / (4.0 * energy ** 2)[:, None] * projected
        return {
            "E": energy, "eps": eps, "p1": p1, "s": s, "norm": norm, "krein": krein,
            "beta2": np.einsum("ni,ni->n", other.conj(), other).real / norm,
            "beta2_adiabatic": np.einsum("ni,ni->n", adiabatic.conj(), adiabatic).real / norm,
            "other": other, "own": own, "hu": hu,
        }


def gauss_legendre_exact(n):
    """Gauss-Legendre nodes/weights on [-1, 1] to full double precision:
    numpy's leggauss nodes as starting values, then Newton iteration on the
    three-term recurrence and w = 2/((1 - x^2) P_n'(x)^2) in 40-digit decimal
    arithmetic (numpy's own weights are only accurate to ~1e-12 relative at
    the end points for n = 48)."""
    from decimal import Decimal, localcontext
    start, _ = np.polynomial.legendre.leggauss(n)
    nodes, weights = [], []
    with localcontext() as context:
        context.prec = 40
        for guess in start:
            z = Decimal(float(guess))
            for _ in range(6):
                p0, p1 = Decimal(1), z
                for j in range(2, n + 1):
                    p0, p1 = p1, ((2 * j - 1) * z * p1 - (j - 1) * p0) / j
                dp = n * (z * p1 - p0) / (z * z - 1)
                z = z - p1 / dp
            p0, p1 = Decimal(1), z
            for j in range(2, n + 1):
                p0, p1 = p1, ((2 * j - 1) * z * p1 - (j - 1) * p0) / j
            dp = n * (z * p1 - p0) / (z * z - 1)
            nodes.append(float(z))
            weights.append(float(2 / ((1 - z * z) * dp * dp)))
    return np.array(nodes), np.array(weights)


def gauss_legendre(n, lo, hi):
    x, w = gauss_legendre_exact(n)
    return x, w, lo + 0.5 * (hi - lo) * (x + 1.0), 0.5 * (hi - lo) * w


def composite_gl(func, lo, hi, panels=60, order=16):
    x, w = np.polynomial.legendre.leggauss(order)
    edges = np.linspace(lo, hi, panels + 1)
    total = 0.0
    for left, right in zip(edges[:-1], edges[1:]):
        half, mid = 0.5 * (right - left), 0.5 * (right + left)
        total += half * np.dot(w, func(mid + half * x))
    return total


def beta_dev(values, reference):
    """max |values - reference| / (1e-9 reference + 1e-20): <= 1 means agreement to
    1e-9 relative (absolute 1e-20 for roundoff-level |beta|^2)."""
    return float(np.max(np.abs(values - reference) / (1e-9 * np.abs(reference) + 1e-20)))


def rel(a, b, floor=0.0):
    return float(np.max(np.abs(np.asarray(a) - np.asarray(b))
                        / np.maximum(np.abs(np.asarray(b)), floor)))


def rk4(alg, mass, kfunc, hfunc, u0, t_points, c):
    """Classical RK4 of i du/dt = h(t) u with step c/max(E, H), landing on
    every point of t_points (t_points[0] = start)."""
    def rhs(t, u):
        return -1j * (alg.h(mass, kfunc(t)) @ u)

    out = [u0.copy()]
    u = u0.copy()
    t = t_points[0]
    for target in t_points[1:]:
        while t < target:
            kk = kfunc(t)
            step = min(c / max(math.sqrt(mass * mass + kk * kk), hfunc(t)), target - t)
            if target - t - step < 1e-12 * max(1.0, abs(target)):
                step = target - t
            k1 = rhs(t, u)
            k2 = rhs(t + 0.5 * step, u + 0.5 * step * k1)
            k3 = rhs(t + 0.5 * step, u + 0.5 * step * k2)
            k4 = rhs(t + step, u + step * k3)
            u = u + (step / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
            t = target if step == target - t else t + step
        out.append(u.copy())
    return np.array(out)


def spinors(data, offset):
    return data[:, offset:offset + 16] + 1j * data[:, offset + 16:offset + 32]


# ============================================================== thermal ==

def verify_thermal(directory, summary, alg, checks, measurements, loaded):
    par = summary["parameters"]["thermal"]
    mass, temp, hubble_i, t_i = par["m"], par["temperature"], par["hubbleInitial"], par["tInitial"]
    a_end, k_max, n_k, n_out = par["aEnd"], par["kMax"], par["nodes"], par["outputIntervals"]
    deg = par["degeneracy"]
    checks["parametersThermal"] = (
        mass == 1.0 and temp == 10.0 and hubble_i == 0.05 and t_i == 1.0 / (2.0 * hubble_i)
        and a_end >= 50.0 and k_max == 12.0 * temp and n_k >= 48 and deg == 16.0
        and par["momentumDirection"] == 1)

    # grid
    header, grid = read_csv(os.path.join(directory, "thermal_grid.csv"))
    x, w, k, wk = gauss_legendre(n_k, 0.0, k_max)
    e_i = np.sqrt(mass ** 2 + k ** 2)
    f = 1.0 / (np.exp(e_i / temp) + 1.0)
    weight = deg / (2.0 * math.pi ** 2) * wk * k ** 2 * f
    c2 = (mass * k * hubble_i / (4.0 * e_i ** 3)) ** 2
    checks["thermalGrid"] = (
        header == ["node", "x", "gl_weight", "k", "weight", "E_i", "f", "mode_weight",
                   "beta2_sudden_start"]
        and float(np.max(np.abs(grid[:, 1] - x))) <= 1e-14
        and float(np.max(np.abs(grid[:, 2] - w))) <= 1e-14
        and rel(grid[:, 3], k, 1e-300) <= 1e-13 and rel(grid[:, 4], wk) <= 1e-13
        and rel(grid[:, 5], e_i) <= 1e-14 and rel(grid[:, 6], f) <= 1e-13
        and rel(grid[:, 7], weight) <= 1e-13 and rel(grid[:, 8], c2) <= 1e-12)
    measurements["thermalGridMaxNodeDev"] = float(np.max(np.abs(grid[:, 1] - x)))

    # time grid
    j = np.arange(1, n_out + 1)
    t_expected = np.concatenate([[t_i], t_i * np.exp(2.0 * math.log(a_end) * j / n_out)])
    t_expected[-1] = t_i * a_end * a_end

    files = {}
    for name in ("thermal_modes.csv", "thermal_spin.csv", "thermal_antiparticle.csv",
                 "thermal_adiabatic_vacuum.csv"):
        head, data = read_csv(os.path.join(directory, name))
        files[name] = (head, data)
    header_ok = all(head == THERMAL_HEADER for head, _ in files.values())
    finite_ok = all(bool(np.all(np.isfinite(d))) for _, d in files.values())
    checks["structureThermalHeaders"] = header_ok
    checks["structureThermalFinite"] = finite_ok

    def runs_of(data):
        out = []
        start = 0
        while start < len(data):
            out.append(data[start:start + n_out + 1])
            start += n_out + 1
        return out

    col_dev = 0.0
    beta_col = 0.0
    grid_ok = True
    obs = {}
    signs = {"thermal_modes.csv": 1.0, "thermal_spin.csv": 1.0,
             "thermal_antiparticle.csv": -1.0, "thermal_adiabatic_vacuum.csv": 1.0}
    for name, (_, data) in files.items():
        obs[name] = []
        for run in runs_of(data):
            node = int(run[0, 0])
            kn = k[node]
            t = run[:, 2]
            grid_ok &= len(run) == n_out + 1 and rel(t, t_expected) <= 1e-14 and \
                float(np.max(np.abs(run[:, 1] / kn - 1.0))) <= 1e-13
            a = np.sqrt(t / t_i)
            kk = kn / a
            hub = 0.5 / t
            u = spinors(run, 6)
            o = alg.observables(u, mass, kk, hub, signs[name])
            o["node"], o["t"], o["a"], o["K"], o["u"] = node, t, a, kk, u
            obs[name].append(o)
            col_dev = max(col_dev, rel(run[:, 3], a), rel(run[:, 4], hub), rel(run[:, 5], kk),
                          rel(run[:, 38], o["E"]))
            scale = o["E"]
            for column, key in ((39, "eps"), (40, "p1")):
                col_dev = max(col_dev, float(np.max(np.abs(run[:, column] - o[key]) / scale)))
            for column, key in ((41, "s"), (42, "norm"), (43, "krein")):
                col_dev = max(col_dev, float(np.max(np.abs(run[:, column] - o[key]))))
            for column, key in ((44, "beta2"), (45, "beta2_adiabatic")):
                beta_col = max(beta_col, beta_dev(run[:, column], o[key]))
    checks["thermalTimeGrid"] = grid_ok
    checks["thermalColumnsRecomputed"] = col_dev <= RECOMPUTE_LIMIT and beta_col <= 1.0
    measurements["thermalColumnMaxDeviation"] = col_dev
    measurements["thermalBetaColumnDeviationRatio"] = beta_col
    main = obs["thermal_modes.csv"]
    checks["structureThermalModeCount"] = len(main) == n_k and [o["node"] for o in main] == \
        list(range(n_k))

    # initial states
    init_ok = True
    eigen_res = 0.0
    for name, runs in obs.items():
        for o in runs:
            u0 = o["u"][0]
            h0 = alg.h(mass, o["K"][0])
            e0 = o["E"][0]
            init_ok &= abs(np.vdot(u0, u0).real - 1.0) <= 1e-14
            if name == "thermal_adiabatic_vacuum.csv":
                own, other = o["own"][0], o["other"][0]
                # e (x) chi + delta: P_+ u0 eigenvector, P_- u0 = -(i/4E^2) P_- hdot P_+ u0
                eigen_res = max(eigen_res, float(np.max(np.abs(h0 @ own - e0 * own))))
                hdot = o["K"][0] * hubble_i * alg.g41
                v = hdot @ own
                delta = -1j / (4.0 * e0 * e0) * 0.5 * (v - h0 @ v / e0)
                eigen_res = max(eigen_res, float(np.max(np.abs(other - delta))))
            else:
                sign = signs[name]
                eigen_res = max(eigen_res, float(np.max(np.abs(h0 @ u0 - sign * e0 * u0))))
            b_expected = -1.0 if name == "thermal_spin.csv" else 1.0
            init_ok &= abs(o["krein"][0] - b_expected) <= 1e-12
    checks["thermalInitialStates"] = init_ok and eigen_res <= EIGEN_LIMIT
    measurements["thermalInitialResidual"] = eigen_res

    # exact algebra behind spin independence and charge conjugation
    sz = -1j * alg.g4
    sx = -alg.g41
    identity = np.eye(16)
    # exact: the entries are small integers (times i)
    structure_ok = (np.array_equal(sz @ sz, identity) and np.array_equal(sx @ sx, identity)
                    and np.array_equal(sz @ sx + sx @ sz, np.zeros((16, 16))))
    htest = alg.h(0.8, 1.7)
    structure_ok &= float(np.max(np.abs(alg.charge @ htest.conj() @ alg.charge + htest))) <= 1e-15
    structure_ok &= float(np.max(np.abs(alg.b @ htest - htest @ alg.b))) <= 1e-15
    checks["thermalExactStructure"] = bool(structure_ok)

    # unitarity, Krein
    all_runs = [o for runs in obs.values() for o in runs]
    unitarity = max(float(np.max(np.abs(o["norm"] - 1.0))) for o in all_runs)
    krein = max(float(np.max(np.abs(o["krein"] - o["krein"][0]))) for o in all_runs)
    checks["thermalUnitarity"] = unitarity <= UNITARITY_LIMIT
    checks["thermalKreinConserved"] = krein <= KREIN_LIMIT
    measurements["thermalMaxUnitarityDev"] = unitarity
    measurements["thermalMaxKreinDrift"] = krein

    # equation of state from the recomputed bilinears
    _, eos = read_csv(os.path.join(directory, "thermal_eos.csv"))
    a = main[0]["a"]
    a3 = a ** 3
    eps = np.array([o["eps"] for o in main])      # (n_k, n_t)
    p1 = np.array([o["p1"] for o in main])
    s = np.array([o["s"] for o in main])
    norm = np.array([o["norm"] for o in main])
    beta = np.array([o["beta2"] for o in main])
    beta_ad = np.array([o["beta2_adiabatic"] for o in main])
    rho = weight @ eps / a3
    p = weight @ p1 / (3.0 * a3)
    ke_h = weight @ p1 / a3
    pe_h = mass * (weight @ s) / a3
    w_eos = p / rho
    fd = wk * k ** 2 * f
    beta_weighted = fd @ beta / np.sum(fd)
    kk = k[:, None] / a[None, :]
    energy = np.sqrt(mass ** 2 + kk ** 2)
    rho_kin_nodes = weight @ energy / a3
    p_kin_nodes = weight @ (kk ** 2 / (3.0 * energy)) / a3
    eos_dev = max(rel(eos[:, 0], a), rel(eos[:, 3], rho), rel(eos[:, 4], p), rel(eos[:, 5], w_eos),
                  rel(eos[:, 6], ke_h), rel(eos[:, 7], pe_h), rel(eos[:, 8], 0.5 * rho),
                  rel(eos[:, 9], 0.5 * rho), rel(eos[:, 10], weight @ norm),
                  rel(eos[:, 11], rho_kin_nodes), rel(eos[:, 12], p_kin_nodes))
    eos_beta = max(beta_dev(eos[:, 16], beta_weighted), beta_dev(eos[:, 17], beta.max(axis=0)),
                   beta_dev(eos[:, 18], beta_ad.max(axis=0)),
                   float(np.max(np.abs(eos[:, 19] - np.max(np.abs(norm - 1.0), axis=0)))) / 1e-15)
    identity_dev = max(rel(ke_h + pe_h, rho), rel(ke_h, 3.0 * p))
    checks["thermalEosRecomputed"] = eos_dev <= 1e-11 and eos_beta <= 1.0 and \
        identity_dev <= 1e-13
    measurements["thermalEosMaxDeviation"] = eos_dev
    measurements["thermalHamiltonianSplitIdentity"] = identity_dev

    # kinetic theory (independent quadrature on [0, k_max]) -- the physics truth
    rho_kin = np.empty_like(a)
    p_kin = np.empty_like(a)
    for index, ai in enumerate(a):
        def integrand_rho(q, ai=ai):
            e = np.sqrt(mass ** 2 + (q / ai) ** 2)
            return q ** 2 / (np.exp(np.sqrt(mass ** 2 + q ** 2) / temp) + 1.0) * e

        def integrand_p(q, ai=ai):
            kq = q / ai
            e = np.sqrt(mass ** 2 + kq ** 2)
            return q ** 2 / (np.exp(np.sqrt(mass ** 2 + q ** 2) / temp) + 1.0) * kq ** 2 / (3 * e)
        rho_kin[index] = deg / (2 * math.pi ** 2 * ai ** 3) * composite_gl(integrand_rho, 0, k_max)
        p_kin[index] = deg / (2 * math.pi ** 2 * ai ** 3) * composite_gl(integrand_p, 0, k_max)
    dev_rho = float(np.max(np.abs(rho / rho_kin - 1.0)))
    dev_p = float(np.max(np.abs(p / p_kin - 1.0)))
    quad_rho = float(np.max(np.abs(rho_kin_nodes / rho_kin - 1.0)))
    quad_p = float(np.max(np.abs(p_kin_nodes / p_kin - 1.0)))
    # free-wave interference envelope (independent re-derivation)
    beta_adiabatic_t = mass * kk * (0.5 / main[0]["t"])[None, :] / (4.0 * energy ** 3)
    bound = np.sqrt(c2)[:, None] * (1.0 + SUDDEN_START_LIMIT) + beta_adiabatic_t
    envelope = weight @ (2.0 * bound * mass * kk / energy + 2.0 * bound ** 2 * kk ** 2 / energy)
    allowed = envelope / (3.0 * a3) + KINETIC_LIMIT * p_kin
    envelope_ratio = float(np.max(np.abs(p - p_kin) / allowed))
    checks["thermalRhoMatchesKineticTheory"] = dev_rho <= KINETIC_LIMIT
    checks["thermalPressureMatchesKineticTheoryPlusFreeWave"] = envelope_ratio <= 1.0
    measurements["thermalMaxRelDevRho"] = dev_rho
    measurements["thermalMaxRelDevPressureLiteral"] = dev_p
    measurements["thermalPressureEnvelopeRatio"] = envelope_ratio
    measurements["thermalGL48QuadratureErrorRho"] = quad_rho
    measurements["thermalGL48QuadratureErrorP"] = quad_p

    def full_rho(ai):
        return deg / (2 * math.pi ** 2 * ai ** 3) * composite_gl(
            lambda q: q ** 2 / (np.exp(np.sqrt(mass ** 2 + q ** 2) / temp) + 1.0)
            * np.sqrt(mass ** 2 + (q / ai) ** 2), 0, 40.0 * temp, panels=200)
    measurements["thermalKmaxTruncationRhoAtA1"] = 1.0 - rho_kin[0] / full_rho(1.0)

    w_kin = p_kin / rho_kin
    checks["thermalWEarlyRadiation"] = (abs(w_eos[0] - 1.0 / 3.0) <= W_EARLY_LIMIT
                                        and w_eos[0] < 1.0 / 3.0
                                        and abs(w_eos[0] - w_kin[0]) <= 1e-6)
    checks["thermalWDecreasesToDust"] = (bool(np.all(np.diff(w_eos) < 0.0))
                                         and 0.0 < w_eos[-1] <= W_LATE_MAX)
    measurements["thermalWAtA1"] = w_eos[0]
    measurements["thermalWKineticAtA1"] = w_kin[0]
    measurements["thermalWAtAEnd"] = w_eos[-1]
    measurements["thermalWKineticAtAEnd"] = w_kin[-1]

    # |beta|^2
    checks["thermalBetaGasWeightedBelow1e-6"] = float(np.max(beta_weighted)) <= BETA_LIMIT
    measurements["thermalBeta2GasWeightedMax"] = float(np.max(beta_weighted))
    late = beta_ad[:, -1]
    compare = c2 >= SUDDEN_START_FLOOR
    sudden_dev = float(np.max(np.abs(late[compare] / c2[compare] - 1.0)))
    bounded = bool(np.all(late[~compare] <= c2[~compare] * (1 + SUDDEN_START_LIMIT) ** 2
                          + BETA_FLOOR))
    inst_bound = (np.sqrt(c2)[:, None] * (1 + SUDDEN_START_LIMIT) + beta_adiabatic_t) ** 2 \
        + BETA_FLOOR
    ratio = float(np.max(beta / inst_bound))
    checks["thermalBetaPerModeIsSuddenStartWave"] = (sudden_dev <= SUDDEN_START_LIMIT and bounded
                                                     and ratio <= 1.0 and compare.any())
    measurements["thermalSuddenStartMaxRelDev"] = sudden_dev
    measurements["thermalSuddenStartBoundRatio"] = ratio
    measurements["thermalBeta2PerModeMax"] = float(np.max(beta))
    measurements["thermalBeta2PerModeMaxK"] = float(k[int(np.argmax(beta.max(axis=1)))])
    measurements["thermalBeta2PerModeMaxOver4c2"] = float(
        np.max(beta.max(axis=1)[compare] / (4 * c2[compare])))
    adv = obs["thermal_adiabatic_vacuum.csv"]
    adv_late = max(float(o["beta2"][-1]) for o in adv)
    adv_max = max(float(np.max(o["beta2_adiabatic"])) for o in adv)
    checks["thermalAdiabaticVacuumBelow1e-6"] = adv_late <= BETA_LIMIT and adv_max <= BETA_LIMIT
    measurements["thermalAdiabaticVacuumLateBeta2"] = adv_late
    measurements["thermalAdiabaticVacuumMaxAdiabaticBeta2"] = adv_max

    def pdev(o):
        kin = o["K"] ** 2 / o["E"]
        return float(np.max(np.abs(o["p1"] - kin) / kin))
    measurements["thermalAdiabaticVacuumPressureDev"] = max(pdev(o) for o in adv)
    measurements["thermalInstantaneousPressureDevSameNodes"] = max(
        pdev(main[o["node"]]) for o in adv)

    # spin independence, antiparticle
    spin_dev = 0.0
    for o in obs["thermal_spin.csv"]:
        m_o = main[o["node"]]
        spin_dev = max(spin_dev, float(np.max(np.abs(o["eps"] - m_o["eps"]) / m_o["E"])),
                       float(np.max(np.abs(o["p1"] - m_o["p1"]) / m_o["E"])),
                       float(np.max(np.abs(o["s"] - m_o["s"]))),
                       float(np.max(np.abs(o["beta2"] - m_o["beta2"]))))
    anti_dev = 0.0
    for o in obs["thermal_antiparticle.csv"]:
        m_o = main[o["node"]]
        anti_dev = max(anti_dev, float(np.max(np.abs(o["eps"] + m_o["eps"]) / m_o["E"])),
                       float(np.max(np.abs(o["p1"] + m_o["p1"]) / m_o["E"])),
                       float(np.max(np.abs(o["s"] + m_o["s"]))),
                       float(np.max(np.abs(o["beta2"] - m_o["beta2"]))))
    checks["thermalSpinIndependence"] = (spin_dev <= SPIN_LIMIT
                                         and len(obs["thermal_spin.csv"]) >= 1)
    checks["thermalAntiparticleSymmetry"] = (anti_dev <= ANTIPARTICLE_LIMIT
                                             and len(obs["thermal_antiparticle.csv"]) == 1)
    measurements["thermalSpinMaxDev"] = spin_dev
    measurements["thermalAntiparticleMaxDev"] = anti_dev

    # independent RK4 reference
    ref_err = 0.0
    richardson = 0.0
    for node in THERMAL_REFERENCE_NODES:
        o = main[node]
        mask = o["a"] <= THERMAL_REFERENCE_A_MAX * (1 + 1e-12)
        t_points = o["t"][mask]
        kn = k[node]
        kfunc = (lambda t, kn=kn: kn / math.sqrt(t / t_i))
        hfunc = (lambda t: 0.5 / t)
        fine = rk4(alg, mass, kfunc, hfunc, o["u"][0], t_points, RK4_C)
        coarse = rk4(alg, mass, kfunc, hfunc, o["u"][0], t_points, 2 * RK4_C)
        ref_err = max(ref_err, float(np.max(np.linalg.norm(o["u"][mask] - fine, axis=1))))
        richardson = max(richardson, float(np.max(np.linalg.norm(coarse - fine, axis=1))) / 15.0)
    checks["thermalReferenceSolution"] = (ref_err <= REFERENCE_LIMIT
                                          and richardson <= 1e-2 * REFERENCE_LIMIT)
    measurements["thermalReferenceMaxError"] = ref_err
    measurements["thermalReferenceRichardson"] = richardson

    # method selection record
    ms = summary["methodSelection"]
    errors = {"adams": 0.0, "bdf": 0.0}
    costs = {"adams": 0, "bdf": 0}
    for trial in ms["trials"]:
        errors[trial["method"]] = max(errors[trial["method"]], trial["maxErrorVsReference"])
        costs[trial["method"]] += trial["rhsEvals"] + trial["linRhsEvals"]
    if errors["adams"] <= 0.5 * errors["bdf"]:
        rule = "adams"
    elif errors["bdf"] <= 0.5 * errors["adams"]:
        rule = "bdf"
    else:
        rule = "adams" if costs["adams"] <= costs["bdf"] else "bdf"
    checks["methodSelectionConsistent"] = (ms["selected"] == rule
                                           and len(ms["trials"]) == 4)
    measurements["methodTestErrorAdams"] = errors["adams"]
    measurements["methodTestErrorBdf"] = errors["bdf"]
    measurements["methodTestCostAdams"] = costs["adams"]
    measurements["methodTestCostBdf"] = costs["bdf"]

    loaded["thermal"] = {"rho": rho, "p": p, "beta": beta, "norm": norm, "main": main}
    return {"maxRelDevRho": dev_rho, "maxBeta2GasWeighted": float(np.max(beta_weighted)),
            "suddenStartMaxRelDev": sudden_dev, "maxUnitarityDev": unitarity}


# ================================================================= pair ==

def pair_background(t):
    t = np.asarray(t, dtype=float)
    a = np.where(t < 0.0, np.exp(np.minimum(t, 0.0)), np.sqrt(1.0 + 2.0 * np.maximum(t, 0.0)))
    hub = np.where(t < 0.0, 1.0, 1.0 / (1.0 + 2.0 * np.maximum(t, 0.0)))
    return a, hub


def verify_pair(directory, summary, alg, checks, measurements, loaded):
    par = summary["parameters"]["pair"]
    masses = par["masses"]
    k0, n_k, n_s = par["kOverAStart"], par["nodes"], par["samples"]
    checks["parametersPair"] = (par["hubbleInflation"] == 1.0 and k0 == 200.0
                                and sorted(masses) == [0.0, 0.1, 0.5, 1.0, 2.0]
                                and par["hubbleEndOverMass"] > 0.0)
    header, grid = read_csv(os.path.join(directory, "pair_grid.csv"))
    x, w, lnk, wln = gauss_legendre(n_k, math.log(par["kMin"]), math.log(par["kMax"]))
    k = np.exp(lnk)
    t0 = np.log(k / k0)
    checks["pairGrid"] = (header == ["node", "x", "gl_weight", "k", "ln_k_weight", "t0"]
                          and float(np.max(np.abs(grid[:, 1] - x))) <= 1e-14
                          and rel(grid[:, 3], k) <= 1e-13 and rel(grid[:, 4], wln) <= 1e-13
                          and float(np.max(np.abs(grid[:, 5] - t0))) <= 1e-13)

    files = {}
    for name in ("pair_modes.csv", "pair_antiparticle.csv"):
        head, data = read_csv(os.path.join(directory, name))
        files[name] = (head, data)
    checks["structurePairHeaders"] = all(h == PAIR_HEADER for h, _ in files.values())
    checks["structurePairFinite"] = all(bool(np.all(np.isfinite(d))) for _, d in files.values())

    rows_per_run = n_s + 2
    obs = {}
    col_dev = 0.0
    beta_col = 0.0
    k_start_dev = 0.0
    grid_ok = True
    init_dev = 0.0
    init_beta = 0.0
    for name, (_, data) in files.items():
        sign = 1.0 if name == "pair_modes.csv" else -1.0
        obs[name] = []
        for start in range(0, len(data), rows_per_run):
            run = data[start:start + rows_per_run]
            mass, node = run[0, 0], int(run[0, 1])
            kn = k[node]
            a2_end = 1.0 / (par["hubbleEndOverMass"] * mass) if mass > 0 else par["masslessA2End"]
            jj = np.arange(1, n_s + 1)
            a2 = np.exp(math.log(a2_end) * jj / n_s)
            a2[-1] = a2_end
            t_expected = np.concatenate([[t0[node], 0.0], (a2 - 1.0) / 2.0])
            t = run[:, 3]
            grid_ok &= float(np.max(np.abs(t - t_expected) / np.maximum(np.abs(t_expected), 1.0))) \
                <= 1e-13 and abs(run[0, 2] / kn - 1.0) <= 1e-13
            a, hub = pair_background(t)
            kk = kn / a
            u = spinors(run, 7)
            o = alg.observables(u, mass, kk, hub, sign)
            o.update({"mass": mass, "node": node, "t": t, "a": a, "K": kk, "u": u,
                      "H": hub})
            obs[name].append(o)
            col_dev = max(col_dev, rel(run[:, 4], a), rel(run[:, 5], hub), rel(run[:, 6], kk),
                          rel(run[:, 39], o["E"]),
                          float(np.max(np.abs(run[:, 40] - o["eps"]) / o["E"])),
                          float(np.max(np.abs(run[:, 41] - o["p1"]) / o["E"])),
                          float(np.max(np.abs(run[:, 42] - o["norm"]))),
                          float(np.max(np.abs(run[:, 43] - o["krein"]))))
            beta_col = max(beta_col, beta_dev(run[:, 44], o["beta2"]),
                           beta_dev(run[:, 45], o["beta2_adiabatic"]))
            # initial first-order adiabatic vacuum
            h0 = alg.h(mass, kk[0])
            e0 = o["E"][0]
            own, other = o["own"][0], o["other"][0]
            k_start_dev = max(k_start_dev, abs(kk[0] / k0 - 1.0))
            init_dev = max(init_dev, float(np.max(np.abs(h0 @ own - sign * e0 * own))),
                           abs(np.vdot(u[0], u[0]).real - 1.0))
            v = kk[0] * hub[0] * (alg.g41 @ own)
            delta = -1j / (4 * e0 * e0) * 0.5 * (v - sign * (h0 @ v) / e0)
            init_dev = max(init_dev, float(np.max(np.abs(other - delta))))
            init_beta = max(init_beta, float(o["beta2"][0]))
    checks["pairTimeGrid"] = grid_ok
    checks["pairColumnsRecomputed"] = col_dev <= RECOMPUTE_LIMIT and beta_col <= 1.0
    measurements["pairColumnMaxDeviation"] = col_dev
    measurements["pairBetaColumnDeviationRatio"] = beta_col
    init_bound = (max(masses) / (4.0 * k0 * k0)) ** 2
    checks["pairInitialAdiabaticVacuum"] = (init_dev <= EIGEN_LIMIT and init_beta <= init_bound
                                            and k_start_dev <= 1e-13)
    measurements["pairInitialResidual"] = init_dev
    measurements["pairInitialBeta2Max"] = init_beta

    main = obs["pair_modes.csv"]
    all_runs = main + obs["pair_antiparticle.csv"]
    unitarity = max(float(np.max(np.abs(o["norm"] - 1.0))) for o in all_runs)
    krein = max(float(np.max(np.abs(o["krein"] - o["krein"][0]))) for o in all_runs)
    checks["pairUnitarity"] = unitarity <= UNITARITY_LIMIT
    checks["pairKreinConserved"] = krein <= KREIN_LIMIT
    measurements["pairMaxUnitarityDev"] = unitarity
    measurements["pairMaxKreinDrift"] = krein
    checks["pairPauli"] = all(bool(np.all((o["beta2"] >= 0) & (o["beta2"] <= 1))) for o in main)

    by_mass = {m: sorted([o for o in main if o["mass"] == m], key=lambda o: o["node"])
               for m in masses}
    checks["structurePairModeCount"] = all(len(v) == n_k for v in by_mass.values())
    massless = by_mass[0.0]
    massless_max = max(max(float(np.max(o["beta2"])), float(np.max(o["beta2_adiabatic"])))
                       for o in massless)
    checks["pairMasslessNoProduction"] = massless_max <= MASSLESS_BETA_LIMIT
    measurements["pairMasslessMaxBeta2"] = massless_max

    # spectrum, number density, EoS, history, tail
    _, spectrum = read_csv(os.path.join(directory, "pair_spectrum.csv"))
    _, eos = read_csv(os.path.join(directory, "pair_eos.csv"))
    _, history = read_csv(os.path.join(directory, "pair_history.csv"))
    pref = 16.0 / (2.0 * math.pi ** 2)
    spec_dev = eos_dev = hist_dev = 0.0
    tail_dev = 0.0
    eos_ok = True
    n_a3 = {}
    quad_dev = 0.0
    summary_masses = {m["m"]: m for m in summary["pair"]["masses"]}
    for m in masses:
        runs = by_mass[m]
        beta_end = np.array([o["beta2"][-1] for o in runs])
        beta_ad_end = np.array([o["beta2_adiabatic"][-1] for o in runs])
        n_a3[m] = pref * np.sum(wln * k ** 3 * beta_end)
        rows = spectrum[spectrum[:, 0] == m]
        e2 = m * m + k * k
        tail = (m * k / (4.0 * e2 * e2)) ** 2
        spec_dev = max(spec_dev, rel(rows[:, 2], k) / 1e-10, rel(rows[:, 3], t0, 1.0) / 1e-10,
                       beta_dev(rows[:, 8], beta_end), beta_dev(rows[:, 9], beta_ad_end),
                       beta_dev(rows[:, 10], tail))
        if m > 0:
            sel = k >= TAIL_K
            tail_dev = max(tail_dev, float(np.max(np.abs(beta_ad_end[sel] / tail[sel] - 1.0))))
        # quadrature sanity: trapezoid rule on the (non-uniform) nodes in ln k
        # versus the Gauss-Legendre sum (a crude, independent estimate)
        if n_a3[m] > 1e-12:
            trap = pref * np.trapezoid(k ** 3 * beta_end, lnk)
            quad_dev = max(quad_dev, abs(trap / n_a3[m] - 1.0))
        a2_end = 1.0 / (par["hubbleEndOverMass"] * m) if m > 0 else par["masslessA2End"]
        a_end = math.sqrt(a2_end)
        e_rows = eos[eos[:, 0] == m]
        occupation = pref * wln * k ** 3 * beta_end
        kk = k[None, :] / e_rows[:, 1][:, None]
        energy = np.sqrt(m * m + kk ** 2)
        rho = energy @ occupation
        pres = (kk ** 2 / (3.0 * energy)) @ occupation
        w_eos = np.where(rho > 0, pres / np.where(rho > 0, rho, 1.0), 0.0)
        n_pts = summary["parameters"]["pair"]["eosPoints"]
        a_grid = np.exp(math.log(a_end) * np.arange(n_pts + 1) / n_pts)
        a_grid[-1] = a_end
        eos_dev = max(eos_dev, rel(e_rows[:, 1], a_grid),
                      abs(e_rows[0, 2] - n_a3[m]) / max(n_a3[m], 1e-300),
                      float(np.max(np.abs(e_rows[:, 3] - rho) / np.maximum(rho, 1e-300))),
                      float(np.max(np.abs(e_rows[:, 4] - pres) / np.maximum(pres, 1e-300))))
        if m > 0:
            eos_ok &= bool(np.all(np.diff(w_eos) <= 0.0)) and w_eos[-1] <= PAIR_W_LATE_MAX \
                and w_eos[0] > w_eos[-1]
            measurements["pairWAtA1_m%s" % m] = float(w_eos[0])
            measurements["pairWEnd_m%s" % m] = float(w_eos[-1])
        h_rows = history[history[:, 0] == m]
        for row in h_rows:
            sample = int(row[1])
            values = np.array([o["beta2"][sample] for o in runs])
            recomputed = pref * np.sum(wln * k ** 3 * values)
            hist_dev = max(hist_dev, abs(row[4] - recomputed) / (1e-10 * recomputed + 1e-20))
        sm = summary_masses[m]
        spec_dev = max(spec_dev, abs(sm["nA3"] - n_a3[m]) / (1e-10 * n_a3[m] + 1e-20))
        measurements["pairNA3_m%s" % m] = float(n_a3[m])
    checks["pairSpectrumAndNumberDensityRecomputed"] = spec_dev <= 1.0
    checks["pairEosRecomputed"] = eos_dev <= 1e-11
    checks["pairHistoryRecomputed"] = hist_dev <= 1.0
    checks["pairEosRelativisticToDust"] = eos_ok
    checks["pairTailMatchesKinkTheory"] = tail_dev <= TAIL_LIMIT
    checks["pairNumberDensityQuadratureSanity"] = quad_dev <= 1e-2
    checks["pairMassiveProduction"] = all(n_a3[m] > 0 for m in masses if m > 0)
    measurements["pairSpectrumMaxDeviation"] = spec_dev
    measurements["pairEosMaxDeviation"] = eos_dev
    measurements["pairTailMaxRelDev"] = tail_dev
    measurements["pairQuadratureTrapezoidVsGL"] = quad_dev

    # antiparticle
    anti_dev = 0.0
    for v in obs["pair_antiparticle.csv"]:
        u = by_mass[v["mass"]][v["node"]]
        anti_dev = max(anti_dev, float(np.max(np.abs(v["beta2"] - u["beta2"]))),
                       float(np.max(np.abs(v["eps"] + u["eps"]) / u["E"])))
    checks["pairAntiparticleSymmetry"] = (anti_dev <= ANTIPARTICLE_LIMIT
                                          and len(obs["pair_antiparticle.csv"]) >= 1)
    measurements["pairAntiparticleMaxDev"] = anti_dev

    # independent RK4 reference over the production epoch
    ref_err = richardson = 0.0
    for m, node in PAIR_REFERENCE_MODES:
        o = by_mass[m][node]
        kn = k[node]
        u0 = o["u"][0]
        t_points = o["t"][:PAIR_REFERENCE_SAMPLES]

        def kfunc(t, kn=kn):
            return kn * math.exp(-t) if t < 0 else kn / math.sqrt(1.0 + 2.0 * t)

        def hfunc(t):
            return 1.0 if t < 0 else 1.0 / (1.0 + 2.0 * t)
        fine = rk4(alg, m, kfunc, hfunc, u0, t_points, RK4_C)
        coarse = rk4(alg, m, kfunc, hfunc, u0, t_points, 2 * RK4_C)
        ref_err = max(ref_err, float(np.max(np.linalg.norm(o["u"][:PAIR_REFERENCE_SAMPLES] - fine,
                                                           axis=1))))
        richardson = max(richardson, float(np.max(np.linalg.norm(coarse - fine, axis=1))) / 15.0)
    checks["pairReferenceSolution"] = (ref_err <= REFERENCE_LIMIT
                                       and richardson <= 1e-2 * REFERENCE_LIMIT)
    measurements["pairReferenceMaxError"] = ref_err
    measurements["pairReferenceRichardson"] = richardson
    loaded["pair"] = {"by_mass": by_mass}
    return {"tailMaxRelDev": tail_dev, "nA3": n_a3}


# =============================================================== driver ==

def verify(root, fixture_path):
    checks, measurements, loaded = {}, {}, {}
    directory = os.path.join(root, EXPERIMENT)
    with open(os.path.join(directory, "summary.json"), "r", encoding="utf-8") as handle:
        summary = json.load(handle)
    fixture_hash = sha256_file(fixture_path)
    with open(GENERATED_RS, "r", encoding="utf-8") as handle:
        generated = handle.read()
    checks["provenanceFixtureHash"] = (summary["fixture"]["sha256"] == fixture_hash
                                       and ('FIXTURE_SHA256: &str = "%s"' % fixture_hash)
                                       in generated)
    checks["provenanceSchema"] = summary["schemaVersion"] == 1 and \
        summary["experiment"] == EXPERIMENT
    checks["structureFilesPresent"] = all(os.path.exists(os.path.join(directory, f))
                                          for f in summary["files"])
    alg = Algebra(fixture_path)
    checks["algebraFromFixture"] = alg.clifford_ok()
    thermal = verify_thermal(directory, summary, alg, checks, measurements, loaded)
    pair = verify_pair(directory, summary, alg, checks, measurements, loaded)
    st, sp = summary["thermal"], summary["pair"]
    consistent = (abs(st["maxUnitarityDev"] - thermal["maxUnitarityDev"]) <= 1e-12
                  and abs(st["maxBeta2GasWeighted"] - thermal["maxBeta2GasWeighted"]) <= 1e-15
                  and abs(st["suddenStartMaxRelDev"] - thermal["suddenStartMaxRelDev"]) <= 1e-9
                  and abs(sp["tailMaxRelDev"] - pair["tailMaxRelDev"]) <= 1e-9)
    checks["summaryConsistent"] = (summary["verdict"] == "SUCCESS"
                                   and all(summary["checks"].values()) and consistent)
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


def refined_convergence(refined_root, summary, loaded, fixture_path, measurements):
    directory = os.path.join(refined_root, EXPERIMENT)
    with open(os.path.join(directory, "summary.json"), "r", encoding="utf-8") as h:
        refined = json.load(h)
    ok = refined["refined"] is True and refined["verdict"] == "SUCCESS"
    ok &= abs(refined["tolerances"]["rtol"] - summary["tolerances"]["rtol"] / 10.0) <= 1e-30
    ok &= abs(refined["tolerances"]["atol"] - summary["tolerances"]["atol"] / 10.0) <= 1e-30
    alg = Algebra(fixture_path)
    sub_checks, sub_meas, sub_loaded = {}, {}, {}
    verify_thermal(directory, refined, alg, sub_checks, sub_meas, sub_loaded)
    canonical = loaded["thermal"]
    ref = sub_loaded["thermal"]
    d_rho = float(np.max(np.abs(ref["rho"] / canonical["rho"] - 1.0)))
    d_p = float(np.max(np.abs(ref["p"] / canonical["p"] - 1.0)))
    d_beta = float(np.max(np.abs(ref["beta"] - canonical["beta"])))
    unit_c = float(np.max(np.abs(canonical["norm"] - 1.0)))
    unit_r = float(np.max(np.abs(ref["norm"] - 1.0)))
    # pair: final |beta|^2 of every (m, k)
    by_mass_c = loaded["pair"]["by_mass"]
    _, data = read_csv(os.path.join(directory, "pair_modes.csv"))
    rows_per_run = refined["parameters"]["pair"]["samples"] + 2
    d_pair = 0.0
    d_pair_rel = 0.0
    for start in range(0, len(data), rows_per_run):
        run = data[start:start + rows_per_run]
        mass, node = run[0, 0], int(run[0, 1])
        t = run[:, 3]
        a, hub = pair_background(t)
        o = alg.observables(spinors(run, 7), mass, run[0, 2] / a, hub, 1.0)
        c = by_mass_c[mass][node]
        diff = abs(o["beta2"][-1] - c["beta2"][-1])
        d_pair = max(d_pair, diff)
        if c["beta2"][-1] >= 1e-6:
            d_pair_rel = max(d_pair_rel, diff / c["beta2"][-1])
    measurements["refinedThermalRhoRelDiff"] = d_rho
    measurements["refinedThermalPressureRelDiff"] = d_p
    measurements["refinedThermalBeta2AbsDiff"] = d_beta
    measurements["refinedThermalUnitarityCanonical"] = unit_c
    measurements["refinedThermalUnitarityRefined"] = unit_r
    measurements["refinedPairBeta2AbsDiff"] = d_pair
    measurements["refinedPairBeta2RelDiff"] = d_pair_rel
    ok &= all(sub_checks.values())
    # canonical-error estimates below the physics limits, refined more unitary
    ok &= d_rho <= KINETIC_LIMIT and d_p <= KINETIC_LIMIT and d_beta <= BETA_FLOOR * 1e3
    ok &= unit_r < unit_c and d_pair <= 1e-9 and d_pair_rel <= 1e-6
    return ok


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
        ran = run_binary(arguments.binary, [EXPERIMENT, "--output",
                                            os.path.abspath(arguments.repeat)])
        checks["repeatByteIdentity"] = ran and compare_repeat(root, os.path.abspath(
            arguments.repeat), summary)
    if arguments.refined:
        refined_root = os.path.abspath(arguments.refined)
        ran = run_binary(arguments.binary, [EXPERIMENT, "--refined", "--output", refined_root])
        checks["refinedConvergence"] = ran and refined_convergence(
            refined_root, summary, loaded, arguments.fixture, measurements)
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
        "checker": "scripts/check_dirac16complex_exp4.py",
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
