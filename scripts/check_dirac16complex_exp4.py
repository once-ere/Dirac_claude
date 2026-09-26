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
    The kinetic theory is also evaluated without the momentum cut (on
    [0, 60 T_i]) to measure what the k_max = 12 T_i truncation of the grid
    removes (rho and p at a = 1 and at a_end, w at a_end).
(b) pair creation: a = e^t (t < 0), (1 + 2t)^{1/2} (t > 0);
    n a^3 = (16/(2 pi^2)) int k^2 |beta_k|^2 dk with the final |beta_k|^2 in the
    first-order adiabatic basis (the instantaneous-basis integrals are the
    literal definition and are recomputed as well), plus the analytic kink tail
    (m k/(4 E^4))^2 beyond k_max, integrated here by composite Gauss-Legendre
    in u = k_max/k.
Independent references: classical RK4 of the full 16-component mode equation
(numpy, step c/max(E, H), c = 0.004, Richardson-checked with c = 0.008) for two
thermal modes (a <= 3) and four pair modes (t0 -> kink -> third radiation
sample); and, over the full thermal range a in [1, 100], a fourth-order Magnus
integration of the exact two-level reduction h = (m sigma_z + K sigma_x) (x) I_8
for five thermal nodes (step c/E with c = 0.05, checked against c = 0.1),
compared through the representation-independent overlap <u(t_i)|u(t)>, which
carries the phase.  The same two-level Magnus integration samples |beta(t)|^2
of every thermal node densely on [t_i, 2 t_i] (the CSV samples do not resolve
the first half-oscillation of the sudden-start wave), and integrates EVERY pair
mode (c = 0.025) from t0 to a_end twice: in the sudden background (an
independent re-integration of the committed spectrum) and in the smooth
comparison background (c) of the Rust program, 1/H = 1 + tau ln(1 + e^{2t/tau})
(-Hdot/H^2 = 1 + tanh(t/tau)), with ln a computed here by composite
Gauss-Legendre quadrature (and in closed form beyond t = 20 tau); the kink
formula (m k/(4 E^4))^2 is integrated over all k by the checker's own quadrature.

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
MAGNUS_NODES = (0, 2, 16, 30, 47)
MAGNUS_C = 0.05
MAGNUS_SELF_LIMIT = 1.0e-8        # |overlap(c) - overlap(2c)|: the reference is converged
MAGNUS_FULL_RANGE_LIMIT = 1.0e-5  # |overlap_CSV - overlap_Magnus| over a in [1, 100]
UNTRUNCATED_K_FACTOR = 60.0       # kinetic theory without the grid's cut: k in [0, 60 T_i]
PAIR_REFERENCE_MODES = ((0.1, 33), (0.5, 30), (1.0, 36), (2.0, 39))
PAIR_REFERENCE_SAMPLES = 4  # t0, kink, first two radiation samples
PAIR_MAGNUS_C = 0.025             # two-level Magnus step c/E for every pair mode, sudden and smooth
PAIR_MAGNUS_SELF_NODES = (16, 32, 40, 48)  # smooth-run nodes re-integrated with 2c
PAIR_SPECTRUM_HEADER = ["m", "node", "k", "t0", "a_end", "beta2_initial", "beta2_kink",
                        "beta2_adiabatic_kink", "beta2_end", "beta2_adiabatic_end",
                        "beta2_kink_tail_theory", "a_end_smooth", "beta2_end_smooth",
                        "beta2_adiabatic_end_smooth"]


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


def magnus_overlap(mass, k, t_i, times, c):
    """<e_+(t_i)|U(t, t_i)|e_+(t_i)> of the two-level reduction h = m sigma_z + K sigma_x,
    K = k (t_i/t)^{1/2} (radiation era), at every t of `times` (times[0] = t_i).

    Fourth-order Magnus with the two Gauss points: over a step h,
    Omega = -i (h m sigma_z + h (K1 + K2)/2 sigma_x + (sqrt3/6) h^2 m (K1 - K2) sigma_y),
    exp(Omega) exactly (a 2 x 2 SU(2) matrix).  In each output interval the steps are
    uniform with h <= c/E(interval start) (E decreases with t), the step matrices are
    built at once and multiplied by a pairwise (tree) product."""
    g1, g2 = 0.5 - math.sqrt(3.0) / 6.0, 0.5 + math.sqrt(3.0) / 6.0
    theta = math.atan2(k, mass)
    e_plus = np.array([math.cos(0.5 * theta), math.sin(0.5 * theta)], dtype=complex)
    state = e_plus.copy()
    out = [complex(np.vdot(e_plus, state))]
    for left, right in zip(times[:-1], times[1:]):
        energy_left = math.sqrt(mass * mass + k * k * t_i / left)
        steps = max(1, int(math.ceil((right - left) * energy_left / c)))
        h = (right - left) / steps
        starts = left + h * np.arange(steps)
        k1 = k * np.sqrt(t_i / (starts + g1 * h))
        k2 = k * np.sqrt(t_i / (starts + g2 * h))
        bz = np.full(steps, h * mass)
        bx = 0.5 * h * (k1 + k2)
        by = (math.sqrt(3.0) / 6.0) * h * h * mass * (k1 - k2)
        norm = np.sqrt(bx * bx + by * by + bz * bz)
        cs, sn = np.cos(norm), np.sin(norm) / norm
        # exp(-i b.sigma) = cos|b| - i sin|b| (b.sigma)/|b|
        mats = np.empty((steps, 2, 2), dtype=complex)
        mats[:, 0, 0] = cs - 1j * sn * bz
        mats[:, 0, 1] = -1j * sn * (bx - 1j * by)
        mats[:, 1, 0] = -1j * sn * (bx + 1j * by)
        mats[:, 1, 1] = cs + 1j * sn * bz
        while len(mats) > 1:
            if len(mats) % 2 == 1:
                mats = np.concatenate([mats, np.eye(2, dtype=complex)[None, :, :]])
            mats = np.einsum("nij,njk->nik", mats[1::2], mats[0::2])
        state = mats[0] @ state
        out.append(complex(np.vdot(e_plus, state)))
    return np.array(out)


def two_level_step_matrices(mass, h, k1, k2):
    """Fourth-order Magnus step matrices exp(Omega_n) of h = m sigma_z + K sigma_x for
    steps of length h (array) with K at the two Gauss points (k1, k2)."""
    bz = h * mass
    bx = 0.5 * h * (k1 + k2)
    by = (math.sqrt(3.0) / 6.0) * h * h * mass * (k1 - k2)
    norm = np.sqrt(bx * bx + by * by + bz * bz)
    safe = np.where(norm > 0.0, norm, 1.0)
    cs, sn = np.cos(norm), np.where(norm > 0.0, np.sin(norm) / safe, 1.0)
    mats = np.empty((len(h), 2, 2), dtype=complex)
    mats[:, 0, 0] = cs - 1j * sn * bz
    mats[:, 0, 1] = -1j * sn * (bx - 1j * by)
    mats[:, 1, 0] = -1j * sn * (bx + 1j * by)
    mats[:, 1, 1] = cs + 1j * sn * bz
    return mats


def tree_product(mats):
    """M_{n-1} ... M_1 M_0 by a pairwise product."""
    while len(mats) > 1:
        if len(mats) % 2 == 1:
            mats = np.concatenate([mats, np.eye(2, dtype=complex)[None, :, :]])
        mats = np.einsum("nij,njk->nik", mats[1::2], mats[0::2])
    return mats[0]


def prefix_products(mats):
    """P_j = M_j ... M_0 for every j (Hillis-Steele scan, log2(n) vectorised passes)."""
    prods = mats.copy()
    shift = 1
    while shift < len(prods):
        prods[shift:] = np.einsum("nij,njk->nik", prods[shift:], prods[:-shift].copy())
        shift *= 2
    return prods


def two_level_eigenvectors(mass, kk):
    """e_+ and e_- of m sigma_z + K sigma_x (theta = atan(K/m)), arrays over K."""
    theta = np.arctan2(kk, mass)
    cos_h, sin_h = np.cos(0.5 * theta), np.sin(0.5 * theta)
    return (np.stack([cos_h, sin_h], axis=-1).astype(complex),
            np.stack([-sin_h, cos_h], axis=-1).astype(complex))


def two_level_beta2(mass, kk, hub, u):
    """(first-order adiabatic |beta|^2, instantaneous |beta|^2) of a two-level state:
    beta_ad = <e_-|u> - i c <e_+|u>, c = m K H/(4 E^3) (the dressing of the
    first-order adiabatic positive-frequency state e_+ + i c e_-)."""
    energy = math.sqrt(mass * mass + kk * kk)
    e_plus, e_minus = two_level_eigenvectors(mass, kk)
    c = mass * kk * hub / (4.0 * energy ** 3)
    amp = np.vdot(e_minus, u) - 1j * c * np.vdot(e_plus, u)
    norm = np.vdot(u, u).real
    return abs(amp) ** 2 / norm, abs(np.vdot(e_minus, u)) ** 2 / norm


def smooth_hubble(t, tau):
    """Checker's own smooth background: 1/H = 1 + tau ln(1 + exp(2t/tau)) (H_inf = 1),
    i.e. -Hdot/H^2 = 1 + tanh(t/tau)."""
    x = 2.0 * np.asarray(t, dtype=float) / tau
    return 1.0 / (1.0 + tau * (np.maximum(x, 0.0) + np.log1p(np.exp(-np.abs(x)))))


class SmoothScaleFactor:
    """ln a(t) of the smooth background with ln a -> t for t -> -inf, computed
    independently of the Rust code: the start offset int_{-inf}^{t0} (H - 1) dt by
    composite Gauss-Legendre in t on [t0 - 40 tau, t0] (400 panels x 8 nodes), then
    8-point Gauss-Legendre increments; for t >= T = 20 tau the closed form
    ln a(T) + (1/2) ln((1 + 2t)/(1 + 2T)) (H = 1/(1 + 2t) there up to e^{-40})."""
    GL_X, GL_W = np.polynomial.legendre.leggauss(8)

    def __init__(self, tau):
        self.tau = tau
        self.switch = 20.0 * tau

    def increments(self, lo, hi):
        lo, hi = np.asarray(lo, dtype=float), np.asarray(hi, dtype=float)
        s = 0.5 * (lo + hi)[..., None] + 0.5 * (hi - lo)[..., None] * self.GL_X
        return 0.5 * (hi - lo) * (smooth_hubble(s, self.tau) @ self.GL_W)

    def start(self, t0):
        edges = np.linspace(t0 - 40.0 * self.tau, t0, 401)
        s = 0.5 * (edges[:-1] + edges[1:])[:, None] + 0.5 * np.diff(edges)[:, None] * self.GL_X
        offset = float(np.sum(0.5 * np.diff(edges) * ((smooth_hubble(s, self.tau) - 1.0)
                                                     @ self.GL_W)))
        return t0 + offset


def pair_two_level_reference(mass, k, times, tau, c):
    """Final (beta2_adiabatic, beta2, a) of a pair mode by fourth-order Magnus
    integration of the two-level reduction from the first-order adiabatic vacuum at
    times[0] through the sample times.  tau = 0: the sudden background
    (a = e^t, then (1 + 2t)^{1/2}); tau > 0: the smooth background above.  Steps are
    uniform in sub-intervals (length 0.25 before T = 20 tau, resp. before t = 0, and
    growing by 1.5 in 1 + 2t after it) with h <= c/E(sub-interval start)."""
    t0 = float(times[0])
    scale = SmoothScaleFactor(tau) if tau > 0.0 else None
    lna = scale.start(t0) if scale else t0
    hub0 = float(smooth_hubble(t0, tau)) if scale else 1.0
    kk0 = k * math.exp(-lna)
    e0 = math.sqrt(mass * mass + kk0 * kk0)
    e_plus, e_minus = two_level_eigenvectors(mass, kk0)
    u = e_plus + 1j * (mass * kk0 * hub0 / (4.0 * e0 ** 3)) * e_minus
    u = u / math.sqrt(np.vdot(u, u).real)
    early_end = scale.switch if scale else 0.0
    bounds, t = [t0], t0
    for target in times[1:]:
        while t < target:
            t = min(t + 0.25 if t < early_end else 0.75 * (1.0 + 2.0 * t) - 0.5, target)
            bounds.append(t)
    lna_switch = None
    for left, right in zip(bounds[:-1], bounds[1:]):
        if scale is None:
            k_left = k * math.exp(-left) if left < 0.0 else k / math.sqrt(1.0 + 2.0 * left)
        else:
            k_left = k * math.exp(-lna)
        steps = max(1, int(math.ceil((right - left) * math.sqrt(mass * mass + k_left ** 2) / c)))
        h = (right - left) / steps
        starts = left + h * np.arange(steps)
        g1, g2 = starts + (0.5 - math.sqrt(3.0) / 6.0) * h, starts + (0.5 + math.sqrt(3.0) / 6.0) * h
        if scale is None:
            def kk_of(tt):
                return np.where(tt < 0.0, k * np.exp(-np.minimum(tt, 0.0)),
                                k / np.sqrt(1.0 + 2.0 * np.maximum(tt, 0.0)))
            k1, k2 = kk_of(g1), kk_of(g2)
        elif left >= scale.switch:
            if lna_switch is None:
                lna_switch = (lna, left)
            base, t_sw = lna_switch
            k1 = k * np.exp(-(base + 0.5 * np.log((1.0 + 2.0 * g1) / (1.0 + 2.0 * t_sw))))
            k2 = k * np.exp(-(base + 0.5 * np.log((1.0 + 2.0 * g2) / (1.0 + 2.0 * t_sw))))
            lna = base + 0.5 * math.log((1.0 + 2.0 * right) / (1.0 + 2.0 * t_sw))
        else:
            inc = scale.increments(starts, starts + h)
            at_start = lna + np.concatenate([[0.0], np.cumsum(inc)[:-1]])
            k1 = k * np.exp(-(at_start + scale.increments(starts, g1)))
            k2 = k * np.exp(-(at_start + scale.increments(starts, g2)))
            lna = lna + float(np.sum(inc))
        u = tree_product(two_level_step_matrices(mass, np.full(steps, h), k1, k2)) @ u
    t_end = float(times[-1])
    if scale is None:
        a_end, hub = math.sqrt(1.0 + 2.0 * t_end), 1.0 / (1.0 + 2.0 * t_end)
    else:
        a_end, hub = math.exp(lna), float(smooth_hubble(t_end, tau))
    beta_ad, beta = two_level_beta2(mass, k / a_end, hub, u)
    return beta_ad, beta, a_end


def thermal_dense_beta2(mass, k, t_i, t_hi, c):
    """|beta(t)|^2 = |<e_-(t)|u(t)>|^2 of a thermal mode started on e_+(t_i), densely
    sampled (every Magnus step of length <= c/E(t_i)) on [t_i, t_hi], K = k (t_i/t)^{1/2}."""
    energy = math.sqrt(mass * mass + k * k)
    steps = max(1, int(math.ceil((t_hi - t_i) * energy / c)))
    h = (t_hi - t_i) / steps
    starts = t_i + h * np.arange(steps)
    g1 = starts + (0.5 - math.sqrt(3.0) / 6.0) * h
    g2 = starts + (0.5 + math.sqrt(3.0) / 6.0) * h
    mats = two_level_step_matrices(mass, np.full(steps, h), k * np.sqrt(t_i / g1),
                                   k * np.sqrt(t_i / g2))
    e_plus0, _ = two_level_eigenvectors(mass, k)
    states = prefix_products(mats) @ e_plus0
    ends = starts + h
    _, e_minus = two_level_eigenvectors(mass, k * np.sqrt(t_i / ends))
    beta2 = np.abs(np.einsum("ni,ni->n", e_minus.conj(), states)) ** 2
    return ends, beta2 / np.einsum("ni,ni->n", states.conj(), states).real


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

    # kinetic theory without the grid's momentum cut (k in [0, 60 T_i]): what the
    # truncation at k_max = 12 T_i removes from rho, p and w (the mode sum and the
    # kinetic comparison above share the cut, so that comparison cannot see it)
    def untruncated(ai):
        k_hi = UNTRUNCATED_K_FACTOR * temp

        def occupation(q):
            return q ** 2 / (np.exp(np.sqrt(mass ** 2 + q ** 2) / temp) + 1.0)
        r = composite_gl(lambda q: occupation(q) * np.sqrt(mass ** 2 + (q / ai) ** 2),
                         0, k_hi, panels=300)
        pp = composite_gl(lambda q: occupation(q) * (q / ai) ** 2
                          / (3.0 * np.sqrt(mass ** 2 + (q / ai) ** 2)), 0, k_hi, panels=300)
        return deg / (2 * math.pi ** 2 * ai ** 3) * r, deg / (2 * math.pi ** 2 * ai ** 3) * pp
    rho_full_1, p_full_1 = untruncated(a[0])
    rho_full_end, p_full_end = untruncated(a[-1])
    measurements["thermalKmaxTruncationPressureAtA1"] = 1.0 - p_kin[0] / p_full_1
    measurements["thermalKmaxTruncationRhoAtAEnd"] = 1.0 - rho_kin[-1] / rho_full_end
    measurements["thermalKmaxTruncationPressureAtAEnd"] = 1.0 - p_kin[-1] / p_full_end
    measurements["thermalKineticUntruncatedWAtA1"] = p_full_1 / rho_full_1
    measurements["thermalKineticUntruncatedWAtAEnd"] = p_full_end / rho_full_end

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
    measurements["thermalBeta2PerModeMaxOver4c2K"] = float(
        k[compare][int(np.argmax(beta.max(axis=1)[compare] / (4 * c2[compare])))])
    # the mode with the largest sampled |beta|^2: its sampled maximum against 4|c|^2 and
    # against the checked envelope (1.1 |c| + beta_ad(t))^2
    max_node = int(np.argmax(beta.max(axis=1)))
    measurements["thermalBeta2PerModeMaxModeOver4c2"] = float(
        beta[max_node].max() / (4 * c2[max_node]))
    measurements["thermalBeta2PerModeMaxModeOverBound"] = float(
        np.max(beta[max_node] / inst_bound[max_node]))
    # The CSV samples (61 per mode, first spacing about 1.7 in t) do not resolve the
    # first half-oscillation of the sudden-start wave: sample |beta(t)|^2 densely
    # (every Magnus step, c = MAGNUS_C/2) on [t_i, 2 t_i] for every node.
    dense_max = np.zeros(len(k))
    dense_ratio = 0.0
    for node in range(len(k)):
        t_dense, b_dense = thermal_dense_beta2(mass, k[node], t_i, 2.0 * t_i, 0.5 * MAGNUS_C)
        kk_dense = k[node] * np.sqrt(t_i / t_dense)
        e_dense = np.sqrt(mass ** 2 + kk_dense ** 2)
        ad_dense = mass * kk_dense * (0.5 / t_dense) / (4.0 * e_dense ** 3)
        bound_dense = (math.sqrt(c2[node]) * (1 + SUDDEN_START_LIMIT) + ad_dense) ** 2 + BETA_FLOOR
        dense_max[node] = float(np.max(b_dense))
        dense_ratio = max(dense_ratio, float(np.max(b_dense / bound_dense)))
    dense_node = int(np.argmax(dense_max))
    measurements["thermalBeta2DenseMax"] = float(dense_max[dense_node])
    measurements["thermalBeta2DenseMaxK"] = float(k[dense_node])
    measurements["thermalBeta2DenseMaxOver4c2"] = float(dense_max[dense_node] / (4 * c2[dense_node]))
    measurements["thermalBeta2DenseMaxOfSampledMaxMode"] = float(dense_max[max_node])
    measurements["thermalBeta2DenseMaxOfSampledMaxModeOver4c2"] = float(
        dense_max[max_node] / (4 * c2[max_node]))
    measurements["thermalBeta2DenseBoundRatio"] = dense_ratio
    checks["thermalBetaPerModeIsSuddenStartWave"] = (checks["thermalBetaPerModeIsSuddenStartWave"]
                                                     and dense_ratio <= 1.0)
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
    # full-range reference (a in [1, a_end]): fourth-order Magnus of the exact
    # two-level reduction, compared through the overlap <u(t_i)|u(t)> (phase included)
    magnus_dev = magnus_self = magnus_phase = 0.0
    magnus_nodes = {}
    for node in MAGNUS_NODES:
        o = main[node]
        overlap = o["u"] @ o["u"][0].conj()
        fine = magnus_overlap(mass, k[node], t_i, o["t"], MAGNUS_C)
        coarse = magnus_overlap(mass, k[node], t_i, o["t"], 2.0 * MAGNUS_C)
        dev = float(np.max(np.abs(overlap - fine)))
        phase = float(np.angle(overlap[-1] / fine[-1]))
        magnus_dev = max(magnus_dev, dev)
        magnus_self = max(magnus_self, float(np.max(np.abs(fine - coarse))))
        magnus_phase = max(magnus_phase, abs(phase))
        magnus_nodes[node] = {"k": float(k[node]), "maxOverlapDev": dev, "finalPhaseError": phase,
                              "reference": fine}
    checks["thermalReferenceSolution"] = (ref_err <= REFERENCE_LIMIT
                                          and richardson <= 1e-2 * REFERENCE_LIMIT
                                          and magnus_self <= MAGNUS_SELF_LIMIT
                                          and magnus_dev <= MAGNUS_FULL_RANGE_LIMIT)
    measurements["thermalReferenceMaxError"] = ref_err
    measurements["thermalReferenceRichardson"] = richardson
    measurements["thermalMagnusFullRangeMaxOverlapDev"] = magnus_dev
    measurements["thermalMagnusFullRangeMaxFinalPhaseError"] = magnus_phase
    measurements["thermalMagnusSelfConvergence"] = magnus_self
    for node, entry in magnus_nodes.items():
        measurements["thermalMagnusFinalPhaseError_node%d" % node] = entry["finalPhaseError"]

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

    loaded["thermal"] = {"rho": rho, "p": p, "beta": beta, "norm": norm, "main": main,
                         "magnus": magnus_nodes}
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
    spectrum_header, spectrum = read_csv(os.path.join(directory, "pair_spectrum.csv"))
    _, eos = read_csv(os.path.join(directory, "pair_eos.csv"))
    _, history = read_csv(os.path.join(directory, "pair_history.csv"))
    pref = 16.0 / (2.0 * math.pi ** 2)
    spec_dev = eos_dev = hist_dev = 0.0
    tail_dev = 0.0
    eos_ok = True
    n_a3 = {}
    quad_dev = 0.0
    summary_masses = {m["m"]: m for m in summary["pair"]["masses"]}
    k_max = par["kMax"]

    def tail_moments(m, a_value):
        """Analytic kink tail beyond k_max, independent composite Gauss-Legendre in
        u = k_max/k (40 panels x 16 nodes): (n a^3, rho a^3, p a^3)."""
        if m == 0.0:
            return 0.0, 0.0, 0.0

        def weight(u):
            kq = k_max / u
            e1 = m * m + kq * kq
            return pref * (k_max / u ** 2) * kq ** 2 * (m * kq / (4.0 * e1 * e1)) ** 2

        def energy(u):
            return np.sqrt(m * m + (k_max / (u * a_value)) ** 2)
        n_t = composite_gl(weight, 0.0, 1.0, panels=40)
        rho_t = composite_gl(lambda u: weight(u) * energy(u), 0.0, 1.0, panels=40)
        p_t = composite_gl(lambda u: weight(u) * (k_max / (u * a_value)) ** 2 / (3.0 * energy(u)),
                           0.0, 1.0, panels=40)
        return n_t, rho_t, p_t

    n_a3_inst = {}
    for m in masses:
        runs = by_mass[m]
        beta_end = np.array([o["beta2"][-1] for o in runs])
        beta_ad_end = np.array([o["beta2_adiabatic"][-1] for o in runs])
        # the produced gas: final |beta_k|^2 in the first-order adiabatic basis
        n_a3[m] = pref * np.sum(wln * k ** 3 * beta_ad_end)
        n_a3_inst[m] = pref * np.sum(wln * k ** 3 * beta_end)
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
            trap = pref * np.trapezoid(k ** 3 * beta_ad_end, lnk)
            quad_dev = max(quad_dev, abs(trap / n_a3[m] - 1.0))
        a2_end = 1.0 / (par["hubbleEndOverMass"] * m) if m > 0 else par["masslessA2End"]
        a_end = math.sqrt(a2_end)
        e_rows = eos[eos[:, 0] == m]
        kk = k[None, :] / e_rows[:, 1][:, None]
        energy = np.sqrt(m * m + kk ** 2)

        def eos_of(occupation):
            rho_o = energy @ occupation
            pres_o = (kk ** 2 / (3.0 * energy)) @ occupation
            return rho_o, pres_o

        def w_of(rho_o, pres_o):
            return np.where(rho_o > 0, pres_o / np.where(rho_o > 0, rho_o, 1.0), 0.0)
        rho, pres = eos_of(pref * wln * k ** 3 * beta_ad_end)
        rho_inst, pres_inst = eos_of(pref * wln * k ** 3 * beta_end)
        tails = np.array([tail_moments(m, a_value) for a_value in e_rows[:, 1]])
        rho_tc, pres_tc = rho + tails[:, 1], pres + tails[:, 2]
        w_eos, w_tc, w_inst = w_of(rho, pres), w_of(rho_tc, pres_tc), w_of(rho_inst, pres_inst)
        n_pts = summary["parameters"]["pair"]["eosPoints"]
        a_grid = np.exp(math.log(a_end) * np.arange(n_pts + 1) / n_pts)
        a_grid[-1] = a_end

        def rdev(column, reference):
            return float(np.max(np.abs(e_rows[:, column] - reference)
                                / np.maximum(np.abs(reference), 1e-300)))
        eos_dev = max(eos_dev, rel(e_rows[:, 1], a_grid),
                      abs(e_rows[0, 2] - n_a3[m]) / max(n_a3[m], 1e-300),
                      rdev(3, rho), rdev(4, pres), float(np.max(np.abs(e_rows[:, 5] - w_eos))),
                      rdev(6, np.full(len(e_rows), n_a3[m] + tails[0, 0])),
                      rdev(7, rho_tc), rdev(8, pres_tc), float(np.max(np.abs(e_rows[:, 9] - w_tc))),
                      rdev(10, rho_inst), rdev(11, pres_inst),
                      float(np.max(np.abs(e_rows[:, 12] - w_inst))))
        if m > 0:
            eos_ok &= bool(np.all(np.diff(w_eos) <= 0.0)) and w_eos[-1] <= PAIR_W_LATE_MAX                 and w_eos[0] > w_eos[-1] and bool(np.all(np.diff(w_tc) <= 0.0))
            measurements["pairWAtA1_m%s" % m] = float(w_eos[0])
            measurements["pairWEnd_m%s" % m] = float(w_eos[-1])
            measurements["pairWAtA1TailCorrected_m%s" % m] = float(w_tc[0])
            measurements["pairWAtA1Instantaneous_m%s" % m] = float(w_inst[0])
            measurements["pairWEndInstantaneous_m%s" % m] = float(w_inst[-1])
            measurements["pairTailNA3Fraction_m%s" % m] = float(tails[0, 0] / n_a3[m])
            measurements["pairTailRhoFractionAtA1_m%s" % m] = float(tails[0, 1] / rho[0])
            measurements["pairTailPressureFractionAtA1_m%s" % m] = float(tails[0, 2] / pres[0])
        h_rows = history[history[:, 0] == m]
        for row in h_rows:
            sample = int(row[1])
            values = np.array([o["beta2"][sample] for o in runs])
            values_ad = np.array([o["beta2_adiabatic"][sample] for o in runs])
            recomputed = pref * np.sum(wln * k ** 3 * values)
            recomputed_ad = pref * np.sum(wln * k ** 3 * values_ad)
            hist_dev = max(hist_dev, abs(row[4] - recomputed) / (1e-10 * recomputed + 1e-20),
                           abs(row[5] - recomputed_ad) / (1e-10 * recomputed_ad + 1e-20))
        sm = summary_masses[m]
        spec_dev = max(spec_dev, abs(sm["nA3"] - n_a3[m]) / (1e-10 * n_a3[m] + 1e-20),
                       abs(sm["nA3Instantaneous"] - n_a3_inst[m]) / (1e-10 * n_a3_inst[m] + 1e-20),
                       abs(sm["nA3KinkTailBeyondKMax"] - tails[0, 0]) / (1e-10 * tails[0, 0] + 1e-30),
                       abs(sm["wEnd"] - w_eos[-1]) / 1e-12,
                       abs(sm["wFrozenSpectrumAtA1TailCorrected"] - w_tc[0]) / 1e-12)
        measurements["pairNA3_m%s" % m] = float(n_a3[m])
        measurements["pairNA3Instantaneous_m%s" % m] = float(n_a3_inst[m])
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

    # Fourth-order Magnus integration of the exact two-level reduction for EVERY
    # (m, k) of the grid, from t0 to a_end: (i) the sudden background (an independent
    # re-integration of the committed spectrum), (ii) the smooth comparison background
    # (c), -Hdot/H^2 = 1 + tanh(t/tau), with the checker's own ln a.
    checks["pairSpectrumHeader"] = spectrum_header == PAIR_SPECTRUM_HEADER
    tau = summary["pair"]["smoothTransition"]["tau"]
    col = {name: index for index, name in enumerate(spectrum_header)}
    sudden_dev = smooth_dev = a_smooth_dev = self_conv = 0.0
    number_dev = kink_dev = 0.0
    massless_smooth = 0.0
    for m in masses:
        rows = spectrum[spectrum[:, 0] == m]
        rows = rows[np.argsort(rows[:, 1])]
        a2_end = 1.0 / (par["hubbleEndOverMass"] * m) if m > 0 else par["masslessA2End"]
        jj = np.arange(1, n_s + 1)
        a2 = np.exp(math.log(a2_end) * jj / n_s)
        a2[-1] = a2_end
        ref = {"sudden": np.zeros((n_k, 3)), "smooth": np.zeros((n_k, 3))}
        for node in range(n_k):
            times = np.concatenate([[t0[node], 0.0], (a2 - 1.0) / 2.0])
            ref["sudden"][node] = pair_two_level_reference(m, k[node], times, 0.0, PAIR_MAGNUS_C)
            ref["smooth"][node] = pair_two_level_reference(m, k[node], times, tau, PAIR_MAGNUS_C)
            if node in PAIR_MAGNUS_SELF_NODES and m > 0:
                coarse = pair_two_level_reference(m, k[node], times, tau, 2.0 * PAIR_MAGNUS_C)
                self_conv = max(self_conv, abs(coarse[0] - ref["smooth"][node][0])
                                / (1e-6 * ref["smooth"][node][0] + 1e-12))

        def dev(values, reference):
            return float(np.max(np.abs(values - reference) / (1e-6 * np.abs(reference) + 1e-12)))
        sudden_dev = max(sudden_dev, dev(rows[:, col["beta2_adiabatic_end"]], ref["sudden"][:, 0]),
                         dev(rows[:, col["beta2_end"]], ref["sudden"][:, 1]))
        smooth_dev = max(smooth_dev,
                         dev(rows[:, col["beta2_adiabatic_end_smooth"]], ref["smooth"][:, 0]),
                         dev(rows[:, col["beta2_end_smooth"]], ref["smooth"][:, 1]))
        a_smooth_dev = max(a_smooth_dev, rel(rows[:, col["a_end_smooth"]], ref["smooth"][:, 2]))
        sm = summary_masses[m]
        n_sudden_ref = pref * np.sum(wln * k ** 3 * ref["sudden"][:, 0])
        n_smooth_ref = pref * np.sum(wln * k ** 3 * ref["smooth"][:, 0])
        n_smooth_col = pref * np.sum(wln * k ** 3 * rows[:, col["beta2_adiabatic_end_smooth"]])
        n_smooth_inst = pref * np.sum(wln * k ** 3 * rows[:, col["beta2_end_smooth"]])
        # the kink formula over all k by the checker's own quadrature (k in [0, 60 m]
        # by composite Gauss-Legendre, the tail beyond it in u = 60 m/k)
        if m > 0:
            def kink_integrand(q, m=m):
                e2 = m * m + q * q
                return pref * q ** 2 * (m * q / (4.0 * e2 * e2)) ** 2

            def kink_tail_integrand(u, m=m):
                q = 60.0 * m / u
                return kink_integrand(q) * 60.0 * m / u ** 2
            kink_all = (composite_gl(kink_integrand, 0.0, 60.0 * m, panels=200)
                        + composite_gl(kink_tail_integrand, 0.0, 1.0, panels=40))
            number_dev = max(number_dev,
                             abs(sm["nA3"] / n_sudden_ref - 1.0) / 1e-6,
                             abs(sm["nA3Smooth"] / n_smooth_ref - 1.0) / 1e-6,
                             abs(sm["nA3Smooth"] / n_smooth_col - 1.0) / 1e-10,
                             abs(sm["nA3SmoothInstantaneous"] / n_smooth_inst - 1.0) / 1e-10,
                             abs(sm["nA3SuddenOverSmooth"] - sm["nA3"] / sm["nA3Smooth"]) / 1e-12)
            kink_dev = max(kink_dev, abs(sm["nA3KinkFormulaAllK"] / kink_all - 1.0),
                           abs(sm["nA3OverKinkFormulaAllK"] - sm["nA3"] / kink_all) / sm["nA3"])
            measurements["pairNA3Smooth_m%s" % m] = float(n_smooth_ref)
            measurements["pairNA3SuddenOverSmooth_m%s" % m] = float(sm["nA3"] / n_smooth_ref)
            measurements["pairNA3KinkFormulaAllK_m%s" % m] = float(kink_all)
            measurements["pairNA3OverKinkFormulaAllK_m%s" % m] = float(sm["nA3"] / kink_all)
        else:
            massless_smooth = max(float(np.max(ref["smooth"][:, :2])),
                                  float(np.max(rows[:, [col["beta2_end_smooth"],
                                                        col["beta2_adiabatic_end_smooth"]]])))
            kink_dev = max(kink_dev, abs(sm["nA3KinkFormulaAllK"]))
        max_ad_end = float(np.max(rows[:, col["beta2_adiabatic_end"]]))
        max_ad_end_smooth = float(np.max(rows[:, col["beta2_adiabatic_end_smooth"]]))
        number_dev = max(number_dev,
                         abs(sm["maxBeta2AdiabaticEnd"] - max_ad_end) / (1e-12 * max_ad_end + 1e-30),
                         abs(sm["maxBeta2AdiabaticEndSmooth"] - max_ad_end_smooth)
                         / (1e-12 * max_ad_end_smooth + 1e-30),
                         abs(sm["aEndSmooth"] / rows[0, col["a_end_smooth"]] - 1.0) / 1e-12)
        measurements["pairMaxBeta2AdiabaticEnd_m%s" % m] = max_ad_end
        measurements["pairMaxBeta2AdiabaticEndSmooth_m%s" % m] = max_ad_end_smooth
    checks["pairSuddenSpectrumMagnusReference"] = sudden_dev <= 1.0
    checks["pairSmoothTransitionReference"] = (
        smooth_dev <= 1.0 and a_smooth_dev <= 1e-10 and self_conv <= 1.0 and number_dev <= 1.0
        and kink_dev <= 1e-10 and massless_smooth <= MASSLESS_BETA_LIMIT
        and summary["pair"]["smoothTransition"]["maxUnitarityDev"] <= UNITARITY_LIMIT
        and summary["pair"]["smoothTransition"]["maxKreinDrift"] <= KREIN_LIMIT
        and par["smoothTransitionTauHubbleInflation"] == tau == 1.0)
    measurements["pairMagnusSuddenMaxDevRel1e-6"] = sudden_dev
    measurements["pairMagnusSmoothMaxDevRel1e-6"] = smooth_dev
    measurements["pairMagnusSmoothSelfConvergenceRel1e-6"] = self_conv
    measurements["pairSmoothAEndMaxRelDev"] = a_smooth_dev
    measurements["pairSmoothNumberAndKinkMaxDev"] = number_dev
    measurements["pairKinkFormulaAllKMaxRelDev"] = kink_dev
    measurements["pairSmoothMasslessMaxBeta2"] = massless_smooth
    loaded["pair"] = {"by_mass": by_mass, "spectrum": spectrum, "spectrumColumns": col}
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
    # smooth comparison runs: final |beta_k|^2 (adiabatic basis) of every (m, k)
    _, spectrum_refined = read_csv(os.path.join(directory, "pair_spectrum.csv"))
    col = loaded["pair"]["spectrumColumns"]
    spectrum_canonical = loaded["pair"]["spectrum"]
    smooth_c = spectrum_canonical[:, col["beta2_adiabatic_end_smooth"]]
    smooth_r = spectrum_refined[:, col["beta2_adiabatic_end_smooth"]]
    same_rows = bool(np.array_equal(spectrum_canonical[:, :3], spectrum_refined[:, :3]))
    d_smooth = float(np.max(np.abs(smooth_r - smooth_c)))
    large = smooth_c >= 1e-6
    d_smooth_rel = float(np.max(np.abs(smooth_r[large] - smooth_c[large]) / smooth_c[large]))
    measurements["refinedPairSmoothBeta2AbsDiff"] = d_smooth
    measurements["refinedPairSmoothBeta2RelDiff"] = d_smooth_rel
    ok &= same_rows and d_smooth <= 1e-9 and d_smooth_rel <= 1e-6
    # the thermal phase error against the full-range Magnus reference: the refined run
    # does not reduce it (it is not a truncation error; the observables are phase invariant)
    measurements["refinedThermalMagnusMaxOverlapDev"] = sub_meas["thermalMagnusFullRangeMaxOverlapDev"]
    measurements["refinedThermalMagnusMaxFinalPhaseError"] = sub_meas[
        "thermalMagnusFullRangeMaxFinalPhaseError"]
    measurements["refinedThermalMaxRawStateDiffMagnusNodes"] = max(
        float(np.max(np.linalg.norm(ref["main"][node]["u"] - canonical["main"][node]["u"], axis=1)))
        for node in MAGNUS_NODES)
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
