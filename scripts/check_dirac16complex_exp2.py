"""Independent checker of EXP-2 (self-consistent 8D Einstein - dirac16complex cosmology).

numpy + standard library only.  Nothing the Rust program derived is taken as
truth: the gamma matrices are rebuilt from the algebra fixture, S_0 and lambda
are re-derived from the constraint, every physical quantity is recomputed from
the CSV *state* columns (ln_b, ln_a, ln_c, H_b, H_a, H_c, u_re_*, u_im_*) and
the physics of NUMERICS_CONTRACT.md, and the derived CSV columns are only
compared against these recomputations.

Physics re-derived here (kappa = kappa_8 = 1, m = 1):
  metric   ds^2 = -dt^2 + b^2 dx0^2 + a^2 dx_{1..3}^2 - c^2 dx_{5..7}^2
  matter   S = S_0 (V_0/V) s(u), s(u) = u^dag (-i gamma^4) u, M_eff = m + lambda S,
           n = S_0 V_0 / V, rho = n u^dag h u - lambda S^2/2, p = lambda S^2/2,
           h = -i M_eff gamma^4, KE_L = n u^dag h u / 2, PE_L = rho - KE_L,
           KE_H = 0 (k = 0), PE_H = m S + lambda S^2 / 2.
  Einstein G^mu_nu = kappa T^mu_nu computed HERE from the diagonal metric
           (Christoffels, Ricci tensor, Einstein tensor for the (4,4)
           signature) -- not from the reduced equations of the contract.

Checks (each printed as check_<name>=true/false):
  provenance*, algebraFromFixture, parametersMatchContract, structure*
  initialState            u(0) = joint (h = +M_eff, B = +1) eigenvector, s = 1,
                          initial H's, ln h = 0
  constraintSolve         S_0 = C_0 / (kappa m s0 (1 + x0 s0)) with C_0 summed over
                          the 21 direction pairs; lambda = 2 m x0 / S_0; matches summary
  derivedColumnsRecomputed  every derived CSV column recomputed from the state
  contractIdentities      rho = KE_L + PE_L, p = KE_L - PE_L, KE_L = S M_eff / 2,
                          PE_L = m S / 2, rho = KE_H + PE_H, rho - p = m S
  constraintPreserved     |sum_{i<j} H_iH_j - kappa rho| / (sum |H_iH_j| + kappa|rho|) < 1e-9
  anisotropyTimesVolume   (H_i - H_j) V constant (relative 1e-9)
  scalarDensityTimesVolume  S V = S_0 V_0 (s(u) conserved, 1e-9), spinor norms
  continuityFd            rho' + Theta (rho + p) = 0, rho' by 9-point finite
                          differences (Fornberg weights in nu = ln V_exact(t), a smooth
                          clock on both branches; d/dt = (dnu/dt) d/dnu)
  einsteinEvolutionFd     (ln h_i)' = H_i and H_i' = -H_i Theta + kappa (rho - p)/6 by FD
  einsteinRoutineKnownMetrics  the curvature routine reproduces known Einstein tensors
                          (8D dust; a 3-direction power law in eta = +1 and eta = -1
                          directions)
  einsteinTensorFromMetric  G^mu_nu - kappa T^mu_nu from the metric with H' by FD
  diracEquationFd         gamma^4 u' = M_eff u and KE_L = (n/2)(-Im u^dag u') by FD,
                          on rows where the output grid resolves the spinor phase
  boundNonnegative        Theta^2 - 3H_a^2 - 2 kappa rho >= 0 and = H_b^2 + 3H_c^2 + 2 res
  closedFormVerified      the closed form (V quadratic, H_i V linear, ln h_i with J)
                          satisfies the ODEs (FD) and J matches Gauss-Legendre quadrature
  exactSolution           CSV states vs the closed form (relative, per 1 + |t_s|/(t - t_s))
  spinorShape             u(t) stays on the ray of u(0): |u - (u0^dag u) u0| +
                          ||u0^dag u| - 1| <= 1e-9 (phase-invariant part of the exact
                          solution u(t) = exp(-i (m t + lambda S_0 s0 J(t))) u(0))
  spinorPhaseWithinTimeRounding  |arg(u0^dag u) + m t + lambda S_0 s0 J(t)| <=
                          max|M_eff| N_steps ulp(t_end)/2 + 1e-9: the phase error is the
                          rounding of CVODE's internal time t_n += h (systematic for the
                          capped constant step), not truncation
  phaseDriftIsTimeRounding  in every binade [2^k, 2^(k+1)) (k = 7..13) of the forward
                          branch the measured drift rate d(phase error)/dt equals the exact
                          prediction M_eff e_k / h, e_k = fl(t_n + h) - (t_n + h) for
                          t_n in that binade and h = fl(max_step) (Fraction arithmetic),
                          within 5 %
  lateTimeDust            at t_end: 7 max|H_i - H_j|/Theta, |7 H_i t/2 - 1|, |w|,
                          |w_eff - 4/3| <= 1e-3; anisotropy decreasing forward
  extraTimesExpand        H_c(0) < 0 < H_c(t_end), crossing near -H_c0/beta
  thetaBoundPositiveEnergy  Theta/(3 H_a) > 1/sqrt 3 where rho > 0; dust w_eff > -1 + 1/sqrt 3
  kasnerExponents         H_i/Theta extrapolated to V = 0 vs (H_i0 + beta t_s)/sqrt D and
                          sum p^2 = 1 - 2 kappa m x0 S_0 s0^2 / D
  phantomStructure        w < -1 <=> KE_L < 0 (rho > 0); x0 = -0.4: phantom exactly for
                          0.4 < V < 0.8 (M_eff < 0 < rho), rho < 0 exactly for V < 0.4
  summaryConsistent       Rust verdict/measurements agree with the recomputation
  optional: --repeat DIR  rerun the binary into DIR, byte-compare every file;
            --refined DIR rerun with --refined: the truncation-controlled errors vs
                          the closed form (gravity, spinor shape) improve (or stay at
                          the floor), the runs agree, and both spinor phase errors
                          stay within their time-rounding bounds.

Usage: python scripts/check_dirac16complex_exp2.py [--output ROOT]
       [--fixture PATH] [--binary PATH] [--repeat DIR] [--refined DIR]
Writes <ROOT>/exp2/python-check-report.json; exits 1 on any failed check.
"""

import argparse
from fractions import Fraction
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
EXPERIMENT = "exp2"
ETA = np.array([1, 1, 1, 1, -1, -1, -1, -1], dtype=float)
TRANSVERSE = [0, 1, 2, 3, 5, 6, 7]
GROUP_OF_FRAME = {0: 0, 1: 1, 2: 1, 3: 1, 5: 2, 6: 2, 7: 2}   # b, a, c

# NUMERICS_CONTRACT EXP-2
KAPPA = 1.0
MASS = 1.0
HUBBLE0 = (0.0, 1.0, -0.2)   # H_b, H_a, H_c
X0_VALUES = [0.0, -0.4, 0.5]

# a-priori limits
DERIVED_LIMIT = 1.0e-12       # recomputation vs CSV (relative to the row scale)
IDENTITY_LIMIT = 1.0e-12      # contract identities (relative)
CONSTRAINT_LIMIT = 1.0e-9     # task: constraint preserved < 1e-9 relative
CONSERVATION_LIMIT = 1.0e-9   # (H_i - H_j) V, S V, norms
FD_LIMIT = 1.0e-8             # 9-point FD residuals of the gravitational sector, relative
                              # (truncation ~ dnu^8/630 |f^(9)| ~ 1e-11, solver noise
                              # amplified by sum|w|/dnu ~ 1e2: ~1e-10)
EINSTEIN_LIMIT = 1.0e-8       # G - kappa T with H' by 9-point FD, relative
DIRAC_FD_LIMIT = 1.0e-6       # 7-point spinor FD where resolved (phase step <= 0.1 per
                              # interval: truncation ~ 0.1^6/140 ~ 1e-8)
GRAVITY_HALF = 4              # 9-point stencils
SPINOR_HALF = 3               # 7-point stencils
PHASE_STEP_MAX = 0.1
EXACT_LIMIT = 1.0e-9          # relative, per amplification 1 + |t_s|/(t - t_s)
SPINOR_SHAPE_LIMIT = 1.0e-9
PHASE_TRUNCATION_ALLOWANCE = 1.0e-9
CLOSED_FORM_LIMIT = 1.0e-7    # FD residual of the closed form itself
QUADRATURE_LIMIT = 1.0e-13
LATE_TIME_LIMIT = 1.0e-3
KASNER_LIMIT = 1.0e-6
SUMMARY_LIMIT = 1.0e-12


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def load_fixture_algebra(path):
    with open(path, "r", encoding="utf-8") as handle:
        document = json.load(handle)
    return [np.array(g, dtype=float) for g in document["gamma"]]


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
          and np.array_equal(b_matrix @ b_matrix, identity.astype(complex)))
    return ok, charge, b_matrix


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


def bilinear(u, m):
    """row-wise u^dag M u for u of shape (n, 16)."""
    return np.einsum("ni,ij,nj->n", u.conj(), m, u)


def fornberg_weights(z, x, order):
    """Finite-difference weights (Fornberg 1988) for derivatives 0..order at z."""
    n = len(x)
    c = np.zeros((n, order + 1))
    c1 = 1.0
    c4 = x[0] - z
    c[0, 0] = 1.0
    for i in range(1, n):
        mn = min(i, order)
        c2 = 1.0
        c5 = c4
        c4 = x[i] - z
        for j in range(i):
            c3 = x[i] - x[j]
            c2 *= c3
            if j == i - 1:
                for k in range(mn, 0, -1):
                    c[i, k] = c1 * (k * c[i - 1, k - 1] - c5 * c[i - 1, k]) / c2
                c[i, 0] = -c1 * c5 * c[i - 1, 0] / c2
            for k in range(mn, 0, -1):
                c[j, k] = (c4 * c[j, k] - k * c[j, k - 1]) / c3
            c[j, 0] = c4 * c[j, 0] / c3
        c1 = c2
    return c


def fd_derivative(nu, values, half=3):
    """d(values)/d(nu) at interior nodes half..N-1-half with (2 half + 1)-point
    Fornberg stencils; values may be (N,) or (N, k).  Returns (indices, derivative)."""
    n = len(nu)
    indices = np.arange(half, n - half)
    out = []
    for i in indices:
        stencil = slice(i - half, i + half + 1)
        weights = fornberg_weights(0.0, nu[stencil] - nu[i], 1)[:, 1]
        out.append(np.tensordot(weights, values[stencil], axes=(0, 0)))
    return indices, np.array(out)


class Background:
    """Closed-form solution, re-derived here: rho - p = m S and S V = S_0 s0 give
    (H_i V)' = V (H_i' + H_i Theta) = kappa m S_0 s0 / 6 =: beta and, summing over
    the 7 directions, V'' = (Theta V)' = 7 beta.  Hence V = 1 + Theta_0 t + alpha t^2
    (alpha = 7 beta / 2), H_i = (H_i0 + beta t) / V and, integrating H_i,
    ln h_i = ln V / 7 + (H_i0 - Theta_0 / 7) J(t), J = int_0^t dt'/V (partial
    fractions over the roots r_near = t_s, r_far of V).  closedFormVerified
    re-checks all of this by finite differences and J by quadrature."""

    def __init__(self, theta0, source):
        self.theta0 = theta0
        self.beta = KAPPA * source / 6.0
        self.alpha = 7.0 * self.beta / 2.0
        self.disc = theta0 * theta0 - 4.0 * self.alpha
        root = math.sqrt(self.disc)
        self.r_near = -2.0 / (theta0 + root)
        self.r_far = -(theta0 + root) / (2.0 * self.alpha)

    def volume(self, t):
        return self.alpha * (t - self.r_near) * (t - self.r_far)

    def dnu_dt(self, t):
        return 1.0 / (t - self.r_near) + 1.0 / (t - self.r_far)

    def j_integral(self, t):
        return (np.log1p(-t / self.r_near) - np.log1p(-t / self.r_far)) / math.sqrt(self.disc)

    def hubble(self, h0, t):
        return (h0 + self.beta * t) / self.volume(t)

    def ln_scale(self, h0, t):
        return np.log(self.volume(t)) / 7.0 + (h0 - self.theta0 / 7.0) * self.j_integral(t)

    def kasner(self, h0):
        return (h0 + self.beta * self.r_near) / math.sqrt(self.disc)


def j_quadrature(background, t):
    """int_0^t dt'/V(t') by composite Gauss-Legendre in the variable
    x = ln(t' - t_s) (smooth near the singularity)."""
    nodes, weights = np.polynomial.legendre.leggauss(30)
    x0 = math.log(0.0 - background.r_near)
    x1 = math.log(t - background.r_near)
    panels = max(4, int(math.ceil(abs(x1 - x0) / 0.1)))
    edges = np.linspace(x0, x1, panels + 1)
    total = 0.0
    for left, right in zip(edges[:-1], edges[1:]):
        half = 0.5 * (right - left)
        mid = 0.5 * (right + left)
        x = mid + half * nodes
        tt = background.r_near + np.exp(x)
        total += half * np.dot(weights, np.exp(x) / background.volume(tt))
    return total


def rounding_drift_rate(h, k):
    """Exact per-unit-time drift of t_n += h for t_n in [2^k, 2^(k+1)): each
    step rounds t_n + h to the nearest multiple of ulp = 2^(k-52) (t_n itself is
    such a multiple), which adds e_k = round(r) - r, r = h mod ulp."""
    ulp = Fraction(2) ** (k - 52)
    step = Fraction(h)
    remainder = step % ulp
    error = (ulp - remainder) if remainder > ulp / 2 else -remainder
    return float(error / step)


def phase_drift_binade_test(t, phase_error, m_eff, h, t_end):
    """Max relative deviation of the measured phase-drift rate from the
    time-rounding prediction over the binades [2^k, 2^(k+1)), k = 7..13,
    covered by at least 10 % inside the forward branch; returns (deviation, count)."""
    worst = 0.0
    count = 0
    for k in range(7, 14):
        low, high = 2.0 ** k * 1.01, min(2.0 ** (k + 1) * 0.99, t_end)
        if high - low < 0.1 * 2.0 ** k:
            continue
        inside = np.where((t >= low) & (t <= high))[0]
        if len(inside) < 2:
            continue
        a, b = inside[0], inside[-1]
        measured = (phase_error[b] - phase_error[a]) / (t[b] - t[a])
        predicted = float(np.mean(m_eff[a:b + 1])) * rounding_drift_rate(h, k)
        worst = max(worst, abs(measured - predicted) / abs(predicted))
        count += 1
    return worst, count


def pair_sum_generic(rates7):
    """sum_{i<j} H_i H_j over the 7 transverse directions (rates7: (N, 7))."""
    total = np.zeros(rates7.shape[0])
    for i in range(7):
        for j in range(i + 1, 7):
            total += rates7[:, i] * rates7[:, j]
    return total


def pair_abs_sum_generic(rates7):
    total = np.zeros(rates7.shape[0])
    for i in range(7):
        for j in range(i + 1, 7):
            total += np.abs(rates7[:, i] * rates7[:, j])
    return total


def expand_groups(group_values):
    """(N, 3) group values (b, a, c) -> (N, 7) for the directions 0,1,2,3,5,6,7."""
    return group_values[:, [GROUP_OF_FRAME[j] for j in TRANSVERSE]]


def einstein_tensor(h, rate, rate_dot):
    """Mixed Einstein tensor G^mu_nu (N, 8, 8) of g = diag(eta_mu h_mu(t)^2), t = x4,
    h_4 = 1, from h, H = h'/h and H' (all (N, 8), column 4 ignored)."""
    n = h.shape[0]
    g = ETA[None, :] * h ** 2
    g[:, 4] = -1.0
    dg = 2.0 * ETA[None, :] * h ** 2 * rate
    ddg = 2.0 * ETA[None, :] * h ** 2 * (rate_dot + 2.0 * rate ** 2)
    dg[:, 4] = 0.0
    ddg[:, 4] = 0.0
    ginv = 1.0 / g
    dginv = -dg / g ** 2
    # P[n, s, m, v] = d_s g_mv (only s = 4); dP = d_4 P
    P = np.zeros((n, 8, 8, 8))
    dP = np.zeros((n, 8, 8, 8))
    for mu in range(8):
        P[:, 4, mu, mu] = dg[:, mu]
        dP[:, 4, mu, mu] = ddg[:, mu]
    # Gamma^l_mv = (1/2) g^ll (d_m g_lv + d_v g_lm - d_l g_mv)
    comb = (np.transpose(P, (0, 2, 1, 3)) + np.transpose(P, (0, 2, 3, 1)) - P)  # [n, l, m, v]
    dcomb = (np.transpose(dP, (0, 2, 1, 3)) + np.transpose(dP, (0, 2, 3, 1)) - dP)
    gamma = 0.5 * ginv[:, :, None, None] * comb
    dgamma = 0.5 * (dginv[:, :, None, None] * comb + ginv[:, :, None, None] * dcomb)  # d_4
    # R_mv = d_l G^l_mv - d_v G^l_lm + G^l_ls G^s_mv - G^l_vs G^s_lm
    ricci = dgamma[:, 4, :, :].copy()
    trace_d = np.einsum("nllm->nm", dgamma)          # d_4 Gamma^l_lm
    ricci[:, :, 4] -= trace_d
    ricci += np.einsum("nlls,nsmv->nmv", gamma, gamma)
    ricci -= np.einsum("nlvs,nsml->nmv", gamma, gamma)
    mixed = ginv[:, :, None] * ricci                 # R^m_v
    scalar = np.einsum("nmm->n", mixed)
    return mixed - 0.5 * scalar[:, None, None] * np.eye(8)[None, :, :]


def einstein_self_test():
    """The curvature routine on metrics with known Einstein tensors: 8D
    isotropic dust h = t^(2/7) (G^4_4 = -21 H^2, G^i_i = 0) and a 3-direction
    power law h = t^0.7 placed once in directions 1..3 (eta = +1) and once in
    5..7 (eta = -1): G^4_4 = -3H^2, G^j_j = -(2H' + 3H^2) in the expanding
    directions, -(3H' + 6H^2) in the static ones -- identical for both
    signatures.  Returns the largest deviation."""
    t = np.array([0.5, 1.0, 3.0])
    worst = 0.0
    h = np.ones((3, 8))
    r = np.zeros((3, 8))
    rd = np.zeros((3, 8))
    rate, rate_dot = 2.0 / (7.0 * t), -2.0 / (7.0 * t ** 2)
    for j in TRANSVERSE:
        h[:, j], r[:, j], rd[:, j] = t ** (2.0 / 7.0), rate, rate_dot
    g = einstein_tensor(h, r, rd)
    expected = np.zeros_like(g)
    expected[:, 4, 4] = -21.0 * rate ** 2
    worst = max(worst, float(np.max(np.abs(g - expected))))
    rate, rate_dot = 0.7 / t, -0.7 / t ** 2
    for block in ((1, 2, 3), (5, 6, 7)):
        h = np.ones((3, 8))
        r = np.zeros((3, 8))
        rd = np.zeros((3, 8))
        for j in block:
            h[:, j], r[:, j], rd[:, j] = t ** 0.7, rate, rate_dot
        g = einstein_tensor(h, r, rd)
        expected = np.zeros_like(g)
        for j in TRANSVERSE:
            expected[:, j, j] = (-(2.0 * rate_dot + 3.0 * rate ** 2) if j in block
                                 else -(3.0 * rate_dot + 6.0 * rate ** 2))
        expected[:, 4, 4] = -3.0 * rate ** 2
        worst = max(worst, float(np.max(np.abs(g - expected))))
    return worst


# ---------------------------------------------------------------------------
# verification
# ---------------------------------------------------------------------------

def run_header():
    header = ["t", "ln_b", "ln_a", "ln_c", "H_b", "H_a", "H_c"]
    header += ["u_re_%d" % i for i in range(16)] + ["u_im_%d" % i for i in range(16)]
    header += ["V", "Theta", "s_u", "S", "M_eff", "energy_mode", "rho", "p", "w", "KE_L", "PE_L",
               "KE_H", "PE_H", "constraint_residual", "constraint_relative", "bound", "w_eff",
               "norm_hilbert", "norm_krein"]
    return header


def recompute(gammas, b_matrix, data, s0_density, lam):
    """All derived quantities from the state columns (independent formulas)."""
    t = data[:, 0]
    ln_h = data[:, 1:4]
    rates = data[:, 4:7]
    u = data[:, 7:23] + 1j * data[:, 23:39]
    rates7 = expand_groups(rates)
    ln_v = ln_h[:, 0] + 3.0 * ln_h[:, 1] + 3.0 * ln_h[:, 2]
    volume = np.exp(ln_v)
    theta = rates7.sum(axis=1)
    minus_i_g4 = -1j * gammas[4]
    s_mode = bilinear(u, minus_i_g4).real
    n = s0_density / volume
    big_s = n * s_mode
    m_eff = MASS + lam * big_s
    energy_mode = np.array([np.vdot(u[k], (-1j * m_eff[k] * gammas[4]) @ u[k]).real
                            for k in range(len(t))])
    lagrangian = 0.5 * lam * big_s ** 2
    # p_j(u) = -(k_j/h_j) u^dag gamma^4 gamma^j u = 0 for k = 0 (kept explicit)
    kh = np.zeros(8)
    gradient = sum(-kh[j] * bilinear(u, gammas[4] @ gammas[j]).real for j in TRANSVERSE)
    rho = n * energy_mode - lagrangian
    p = n * gradient / 7.0 + lagrangian
    ke_l = 0.5 * n * energy_mode
    pe_l = rho - ke_l
    ke_h = n * gradient
    pe_h = MASS * big_s + 0.5 * lam * big_s ** 2
    pairs = pair_sum_generic(rates7)
    pairs_abs = pair_abs_sum_generic(rates7)
    residual = pairs - KAPPA * rho
    relative = np.abs(residual) / (pairs_abs + KAPPA * np.abs(rho))
    bound = theta ** 2 - 3.0 * rates[:, 1] ** 2 - 2.0 * KAPPA * rho
    w = p / rho
    w_eff = -1.0 + theta * (1.0 + w) / (3.0 * rates[:, 1])
    hilbert = np.einsum("ni,ni->n", u.conj(), u).real
    krein = bilinear(u, b_matrix).real
    return dict(t=t, ln_h=ln_h, rates=rates, rates7=rates7, u=u, V=volume, Theta=theta,
                s_u=s_mode, n=n, S=big_s, M_eff=m_eff, energy_mode=energy_mode, rho=rho, p=p,
                w=w, KE_L=ke_l, PE_L=pe_l, KE_H=ke_h, PE_H=pe_h, constraint_residual=residual,
                constraint_relative=relative, bound=bound, w_eff=w_eff, norm_hilbert=hilbert,
                norm_krein=krein, pairs_abs=pairs_abs)


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

    parameters = summary["parameters"]
    checks["parametersMatchContract"] = (
        parameters["kappa"] == KAPPA and parameters["m"] == MASS
        and (parameters["hubbleB0"], parameters["hubbleA0"], parameters["hubbleC0"]) == HUBBLE0
        and parameters["x0Values"] == X0_VALUES
        and sorted(run["x0"] for run in summary["runs"]) == sorted(X0_VALUES))
    checks["structureFilesPresent"] = all(os.path.exists(os.path.join(directory, name))
                                          for name in summary["files"])

    # the 21 direction pairs at t = 0 (generic sum, not the grouped formula)
    rates7_0 = expand_groups(np.array([HUBBLE0]))
    c0 = float(pair_sum_generic(rates7_0)[0])
    theta0 = float(rates7_0.sum())
    measurements["constraintLhs0"] = c0

    header_ok = grid_ok = finite_ok = initial_ok = solve_ok = True
    derived_dev = identity_dev = constraint_max = 0.0
    anis_dev = sv_dev = norm_dev = 0.0
    continuity_fd = evolution_fd = einstein_dev = dirac_fd = kinetic_fd = 0.0
    dirac_rows = 0
    bound_min = math.inf
    bound_identity = 0.0
    closed_fd = quad_dev = 0.0
    exact_dev = spinor_dev = shape_dev = phase_dev = 0.0
    phase_ok = True
    binade_dev = 0.0
    binade_count = 0
    late_dev = 0.0
    anis_monotone = True
    turn_ok = True
    theta_ratio_min = math.inf
    theta_ratio_min_all = math.inf
    dust_w_eff_min = math.inf
    kasner_dev = 0.0
    phantom_ok = True
    summary_dev = 0.0
    run_reports = {}
    for run in summary["runs"]:
        x0 = run["x0"]
        header, data = read_csv(os.path.join(directory, run["file"]))
        header_ok &= header == run_header()
        finite_ok &= bool(np.all(np.isfinite(data)))
        t = data[:, 0]
        grid_ok &= bool(np.all(np.diff(t) > 0.0))
        zero = np.where(t == 0.0)[0]
        grid_ok &= len(zero) == 1
        i0 = int(zero[0]) if len(zero) == 1 else 0
        u = data[:, 7:23] + 1j * data[:, 23:39]
        u0 = u[i0]

        # initial state ----------------------------------------------------
        s0 = float(np.vdot(u0, (-1j * gammas[4]) @ u0).real)
        s0_density = c0 / (KAPPA * MASS * s0 * (1.0 + x0 * s0))
        lam = 2.0 * MASS * x0 / s0_density
        m_eff0 = MASS + lam * s0_density * s0
        h0 = -1j * m_eff0 * gammas[4]
        initial_ok &= bool(np.all(data[i0, 1:4] == 0.0)) and tuple(data[i0, 4:7]) == HUBBLE0
        initial_ok &= m_eff0 > 0.0 and abs(np.vdot(u0, u0).real - 1.0) <= 1e-14
        initial_ok &= abs(s0 - 1.0) <= 1e-14
        initial_ok &= float(np.max(np.abs(h0 @ u0 - m_eff0 * u0))) <= 1e-12
        initial_ok &= float(np.max(np.abs(b_matrix @ u0 - u0))) <= 1e-12
        solve_ok &= (abs(run["S0"] - s0_density) <= 1e-14 * s0_density
                     and abs(run["lambda"] - lam) <= 1e-14 * max(1.0, abs(lam))
                     and abs(s0_density - c0 / (1.0 + x0)) <= 1e-13
                     and abs(run["constraintLhs0"] - c0) <= 1e-15)

        # derived columns --------------------------------------------------
        q = recompute(gammas, b_matrix, data, s0_density, lam)
        scale2 = q["Theta"] ** 2 + np.sum(q["rates7"] ** 2, axis=1) + KAPPA * (np.abs(q["rho"]) + np.abs(q["p"]))
        matter_scale = np.abs(q["rho"]) + np.abs(q["p"]) + MASS * np.abs(q["S"])
        column_scale = {
            "V": np.abs(q["V"]), "Theta": np.abs(q["Theta"]) + np.sum(np.abs(q["rates7"]), axis=1),
            "s_u": np.ones_like(t), "S": np.abs(q["S"]),
            "M_eff": np.abs(q["M_eff"]) + MASS, "energy_mode": np.abs(q["M_eff"]) + MASS,
            "rho": matter_scale, "p": matter_scale, "w": 1.0 + np.abs(q["w"]),
            "KE_L": matter_scale, "PE_L": matter_scale, "KE_H": matter_scale, "PE_H": matter_scale,
            "constraint_residual": q["pairs_abs"] + KAPPA * np.abs(q["rho"]),
            "constraint_relative": np.ones_like(t) * 1e-3,
            "bound": q["Theta"] ** 2, "w_eff": 1.0 + np.abs(q["w_eff"]),
            "norm_hilbert": np.ones_like(t), "norm_krein": np.ones_like(t),
        }
        for name, scale in column_scale.items():
            column = data[:, header.index(name)]
            derived_dev = max(derived_dev, float(np.max(np.abs(column - q[name]) / scale)))

        # contract identities (homogeneous isotropic condensate) ------------
        big_s, m_eff, rho, p = q["S"], q["M_eff"], q["rho"], q["p"]
        identity_terms = [
            rho - (q["KE_L"] + q["PE_L"]),
            p - (q["KE_L"] - q["PE_L"]),
            q["KE_L"] - 0.5 * big_s * m_eff,
            q["PE_L"] - 0.5 * MASS * big_s,
            rho - (q["KE_H"] + q["PE_H"]),
            rho - (MASS * big_s + 0.5 * lam * big_s ** 2),
            p - 0.5 * lam * big_s ** 2,
            (rho - p) - MASS * big_s,
        ]
        identity_dev = max(identity_dev, max(float(np.max(np.abs(x) / matter_scale))
                                             for x in identity_terms))

        # constraint and conserved quantities ------------------------------
        constraint_max = max(constraint_max, float(np.max(q["constraint_relative"])))
        rates = q["rates"]
        initial_diff = [HUBBLE0[1] - HUBBLE0[0], HUBBLE0[2] - HUBBLE0[0], HUBBLE0[1] - HUBBLE0[2]]
        biggest = max(abs(d) for d in initial_diff)
        for (i, j), d0 in zip([(1, 0), (2, 0), (1, 2)], initial_diff):
            anis_dev = max(anis_dev, float(np.max(np.abs((rates[:, i] - rates[:, j]) * q["V"] - d0)))
                           / biggest)
        sv_dev = max(sv_dev, float(np.max(np.abs(q["S"] * q["V"] / (s0_density * s0) - 1.0))))
        norm_dev = max(norm_dev, float(np.max(np.abs(q["norm_hilbert"] - 1.0))),
                       float(np.max(np.abs(q["norm_krein"] - q["norm_krein"][i0]))))

        # finite differences in nu = ln V_exact(t) ---------------------------
        bg = Background(theta0, MASS * s0_density * s0)
        nu = np.log(bg.volume(t))
        dnu = bg.dnu_dt(t)
        idx, d_ln_h = fd_derivative(nu, q["ln_h"], GRAVITY_HALF)
        _, d_rates = fd_derivative(nu, rates, GRAVITY_HALF)
        _, d_rho = fd_derivative(nu, rho, GRAVITY_HALF)
        d_ln_h = d_ln_h * dnu[idx, None]
        d_rates = d_rates * dnu[idx, None]
        d_rho = d_rho * dnu[idx]
        theta = q["Theta"]
        cont = np.abs(d_rho + theta[idx] * (rho[idx] + p[idx])) / (np.abs(theta[idx]) * (np.abs(rho[idx]) + np.abs(p[idx])))
        continuity_fd = max(continuity_fd, float(np.max(cont)))
        rate_scale = np.sum(np.abs(q["rates7"][idx]), axis=1)
        evo1 = np.max(np.abs(d_ln_h - rates[idx]), axis=1) / rate_scale
        source = KAPPA * (rho[idx] - p[idx]) / 6.0
        evo2 = np.max(np.abs(d_rates + rates[idx] * theta[idx, None] - source[:, None]), axis=1) / scale2[idx]
        evolution_fd = max(evolution_fd, float(np.max(evo1)), float(np.max(evo2)))

        # Einstein tensor from the metric --------------------------------
        h8 = np.ones((len(idx), 8))
        r8 = np.zeros((len(idx), 8))
        rd8 = np.zeros((len(idx), 8))
        for j in TRANSVERSE:
            g = GROUP_OF_FRAME[j]
            h8[:, j] = np.exp(q["ln_h"][idx, g])
            r8[:, j] = rates[idx, g]
            rd8[:, j] = d_rates[:, g]
        einstein = einstein_tensor(h8, r8, rd8)
        stress = np.zeros_like(einstein)
        for j in TRANSVERSE:
            stress[:, j, j] = p[idx]
        stress[:, 4, 4] = -rho[idx]
        e_scale = scale2[idx] + np.sum(np.abs(rd8), axis=1)
        einstein_dev = max(einstein_dev, float(np.max(np.abs(einstein - KAPPA * stress).reshape(len(idx), -1).max(axis=1) / e_scale)))

        # Dirac equation and KE_L definition where the grid resolves the phase
        phase_step = np.abs(m_eff) / np.abs(dnu) * np.max(np.abs(np.diff(nu)))
        sidx, d_u = fd_derivative(nu, u, SPINOR_HALF)
        resolved = np.array([bool(np.all(phase_step[k - SPINOR_HALF:k + SPINOR_HALF + 1]
                                         <= PHASE_STEP_MAX)) for k in sidx])
        d_u = d_u * dnu[sidx, None]
        lhs = d_u @ gammas[4].T
        rhs = m_eff[sidx, None] * u[sidx]
        dirac_res = np.linalg.norm(lhs - rhs, axis=1) / (np.abs(m_eff[sidx]) + np.abs(theta[sidx]))
        k4 = -np.einsum("ni,ni->n", u[sidx].conj(), d_u).imag
        kin_res = np.abs(q["KE_L"][sidx] - 0.5 * q["n"][sidx] * k4) / matter_scale[sidx]
        if np.any(resolved):
            dirac_fd = max(dirac_fd, float(np.max(dirac_res[resolved])))
            kinetic_fd = max(kinetic_fd, float(np.max(kin_res[resolved])))
            dirac_rows += int(np.sum(resolved))

        # bound ----------------------------------------------------------
        bound_min = min(bound_min, float(np.min(q["bound"])))
        bound_identity = max(bound_identity, float(np.max(np.abs(
            q["bound"] - (rates[:, 0] ** 2 + 3.0 * rates[:, 2] ** 2 + 2.0 * q["constraint_residual"]))
            / theta ** 2)))

        # closed form: verify it solves the equations, J by quadrature ------
        exact_ln = np.stack([bg.ln_scale(h, t) for h in HUBBLE0], axis=1)
        exact_rates = np.stack([bg.hubble(h, t) for h in HUBBLE0], axis=1)
        exact_v = bg.volume(t)
        _, e_dln = fd_derivative(nu, exact_ln, GRAVITY_HALF)
        _, e_drate = fd_derivative(nu, exact_rates, GRAVITY_HALF)
        e_dln = e_dln * dnu[idx, None]
        e_drate = e_drate * dnu[idx, None]
        e7 = expand_groups(exact_rates)
        e_theta = e7.sum(axis=1)
        e_s = s0_density * s0 / exact_v
        e_rho = MASS * e_s + 0.5 * lam * e_s ** 2
        e_p = 0.5 * lam * e_s ** 2
        e_scale2 = e_theta[idx] ** 2 + np.sum(e7[idx] ** 2, axis=1) + KAPPA * (np.abs(e_rho[idx]) + np.abs(e_p[idx]))
        closed_fd = max(
            closed_fd,
            float(np.max(np.max(np.abs(e_dln - exact_rates[idx]), axis=1) / np.sum(np.abs(e7[idx]), axis=1))),
            float(np.max(np.max(np.abs(e_drate + exact_rates[idx] * e_theta[idx, None]
                                       - KAPPA * (e_rho[idx] - e_p[idx])[:, None] / 6.0), axis=1) / e_scale2)),
            float(np.max(np.abs(np.log(exact_v) - (exact_ln[:, 0] + 3 * exact_ln[:, 1] + 3 * exact_ln[:, 2])))),
            float(np.max(np.abs(pair_sum_generic(e7) - KAPPA * e_rho) / (pair_abs_sum_generic(e7) + KAPPA * np.abs(e_rho)))))
        for tt in [t[0], t[i0 // 2], t[min(len(t) - 1, i0 + 30)], t[-1]]:
            if tt != 0.0:
                j_quad = j_quadrature(bg, tt)
                quad_dev = max(quad_dev, abs(bg.j_integral(tt) - j_quad) / max(1.0, abs(j_quad)))

        # exact solution vs CSV -------------------------------------------
        amplification = 1.0 + abs(bg.r_near) / (t - bg.r_near)
        dev_v = np.abs(q["V"] / exact_v - 1.0) / amplification
        rate_scale_exact = np.sum(np.abs(e7), axis=1)
        dev_h = np.max(np.abs(rates - exact_rates), axis=1) / rate_scale_exact / amplification
        dev_l = np.max(np.abs(q["ln_h"] - exact_ln) / (1.0 + np.abs(exact_ln)), axis=1) / amplification
        exact_dev = max(exact_dev, float(np.max(dev_v)), float(np.max(dev_h)), float(np.max(dev_l)))
        phase = MASS * t + lam * s0_density * s0 * bg.j_integral(t)
        u_exact = np.exp(-1j * phase)[:, None] * u0[None, :]
        spinor_err = np.linalg.norm(u - u_exact, axis=1)
        spinor_dev = max(spinor_dev, float(np.max(spinor_err)))
        overlap = u @ u0.conj()
        shape = (np.linalg.norm(u - overlap[:, None] * u0[None, :], axis=1)
                 + np.abs(np.abs(overlap) - 1.0))
        shape_dev = max(shape_dev, float(np.max(shape)))
        phase_error = np.angle(overlap * np.exp(1j * phase))
        forward_rows = t >= 0.0
        steps_f = run["solver"]["forward"]["steps"]
        steps_b = run["solver"]["backward"]["steps"]
        bound = (float(np.max(np.abs(m_eff[forward_rows]))) * steps_f * float(np.spacing(t[-1])) / 2.0
                 + float(np.max(np.abs(m_eff[~forward_rows]))) * steps_b * float(np.spacing(abs(t[0]))) / 2.0)
        phase_dev = max(phase_dev, float(np.max(np.abs(phase_error))))
        phase_ok &= float(np.max(np.abs(phase_error))) <= bound + PHASE_TRUNCATION_ALLOWANCE
        # signature of time rounding: per-binade drift rate vs exact prediction
        deviation, count = phase_drift_binade_test(t, phase_error, m_eff, summary["tolerances"]["maxStep"],
                                                   t[-1])
        binade_dev = max(binade_dev, deviation)
        binade_count += count

        # late time ------------------------------------------------------
        last = len(t) - 1
        spread = np.max(np.abs(expand_groups(rates)[:, :, None] - expand_groups(rates)[:, None, :]), axis=(1, 2))
        anisotropy = 7.0 * spread / theta
        forward = slice(i0, len(t))
        anis_monotone &= bool(np.all(np.diff(anisotropy[forward]) < 0.0))
        late = max(anisotropy[last],
                   float(np.max(np.abs(3.5 * rates[last] * t[last] - 1.0))),
                   abs(q["w"][last]), abs(q["w_eff"][last] - 4.0 / 3.0))
        late_dev = max(late_dev, late)
        crossing = np.where((rates[:-1, 2] < 0.0) & (rates[1:, 2] >= 0.0))[0]
        turn_time = -HUBBLE0[2] / bg.beta
        if len(crossing) == 1 and rates[i0, 2] < 0.0 < rates[last, 2]:
            k = int(crossing[0])
            t_cross = t[k] + (t[k + 1] - t[k]) * (-rates[k, 2]) / (rates[k + 1, 2] - rates[k, 2])
            turn_ok &= abs(t_cross - turn_time) <= 1e-2 * turn_time
        else:
            turn_ok = False
            t_cross = float("nan")

        # Theta > sqrt 3 H_a where rho > 0 (dust: w_eff > -1 + 1/sqrt 3) ---
        positive = (rho > 0.0) & (rates[:, 1] > 0.0)
        ratio = theta / (3.0 * rates[:, 1])
        theta_ratio_min = min(theta_ratio_min, float(np.min(ratio[positive])))
        theta_ratio_min_all = min(theta_ratio_min_all, float(np.min(ratio)))
        if x0 == 0.0:
            dust_w_eff_min = float(np.min(q["w_eff"][positive]))

        # Kasner exponents: extrapolate H_i/Theta to V = 0 (3 smallest V) ---
        order = np.argsort(q["V"])[:3]
        vv = q["V"][order]
        kasner = np.zeros(3)
        for kk in range(3):
            weight = 1.0
            for jj in range(3):
                if jj != kk:
                    weight *= (0.0 - vv[jj]) / (vv[kk] - vv[jj])
            kasner += weight * rates[order[kk]] / theta[order[kk]]
        kasner_exact = np.array([bg.kasner(h) for h in HUBBLE0])
        sum_sq = kasner[0] ** 2 + 3 * kasner[1] ** 2 + 3 * kasner[2] ** 2
        sum_sq_exact = 1.0 - 2.0 * KAPPA * MASS * x0 * s0_density * s0 * s0 / bg.disc
        kasner_sum = kasner[0] + 3 * kasner[1] + 3 * kasner[2]
        kasner_dev = max(kasner_dev, float(np.max(np.abs(kasner - kasner_exact))),
                         abs(sum_sq - sum_sq_exact) / sum_sq_exact, abs(kasner_sum - 1.0),
                         abs(kasner_exact[0] + 3 * kasner_exact[1] + 3 * kasner_exact[2] - 1.0))

        # phantom / negative-energy structure -------------------------------
        phantom = (q["w"] < -1.0) & (rho > 0.0)
        phantom_ok &= bool(np.all(phantom == ((q["KE_L"] < 0.0) & (rho > 0.0))))
        volume = q["V"]
        if x0 < 0.0:
            expected_phantom = (volume > -x0 * s0) & (volume < -2.0 * x0 * s0)
            expected_negative = volume < -x0 * s0
            phantom_ok &= bool(np.any(phantom)) and bool(np.all(phantom == expected_phantom))
            phantom_ok &= bool(np.all((rho < 0.0) == expected_negative))
            phantom_ok &= bool(np.all((m_eff < 0.0) == (volume < -2.0 * x0 * s0)))
        else:
            phantom_ok &= not bool(np.any(phantom)) and bool(np.all(rho > 0.0))

        # Rust per-run measurements vs recomputation -------------------------
        rust = run["measurements"]
        summary_dev = max(summary_dev,
                          abs(rust["maxConstraintRelative"] - float(np.max(q["constraint_relative"]))),
                          abs(rust["maxScalarDensityDrift"] - float(np.max(np.abs(q["s_u"] - s0)))),
                          abs(rust["minBound"] - float(np.min(q["bound"]))) / float(np.max(theta ** 2)),
                          abs(rust["maxExactSpinorError"] - float(np.max(spinor_err))),
                          float(np.max(np.abs(np.array(rust["kasnerExtrapolated"]) - kasner))),
                          abs(run["exact"]["singularityTime"] - bg.r_near),
                          abs(run["exact"]["discriminant"] - bg.disc))
        run_reports[run["id"]] = {
            "S0": s0_density, "lambda": lam, "mEff0": m_eff0, "singularityTime": bg.r_near,
            "tBack": float(t[0]), "tEnd": float(t[-1]), "VBack": float(q["V"][0]),
            "VEnd": float(q["V"][-1]), "kasnerExtrapolated": kasner.tolist(),
            "kasnerExact": kasner_exact.tolist(), "kasnerSumSquares": sum_sq,
            "kasnerSumSquaresExact": sum_sq_exact, "finalAnisotropy": float(anisotropy[last]),
            "finalHubbleTimesT": (rates[last] * t[last]).tolist(), "finalWeff": float(q["w_eff"][last]),
            "extraTimeTurnTime": float(t_cross), "extraTimeTurnTimeExact": turn_time,
            "minThetaOver3Ha": float(np.min(ratio)), "phantomRows": int(np.sum(phantom)),
            "negativeEnergyRows": int(np.sum(rho < 0.0)), "diracFdRows": int(np.sum(resolved)),
        }

    checks["structureHeaders"] = header_ok
    checks["structureGrid"] = grid_ok
    checks["structureFinite"] = finite_ok
    checks["initialState"] = initial_ok
    checks["constraintSolve"] = solve_ok
    checks["derivedColumnsRecomputed"] = derived_dev <= DERIVED_LIMIT
    checks["contractIdentities"] = identity_dev <= IDENTITY_LIMIT
    checks["constraintPreserved"] = constraint_max < CONSTRAINT_LIMIT
    checks["anisotropyTimesVolumeConstant"] = anis_dev <= CONSERVATION_LIMIT
    checks["scalarDensityTimesVolumeConstant"] = sv_dev <= CONSERVATION_LIMIT and norm_dev <= CONSERVATION_LIMIT
    checks["continuityFd"] = continuity_fd <= FD_LIMIT
    checks["einsteinEvolutionFd"] = evolution_fd <= FD_LIMIT
    self_test = einstein_self_test()
    measurements["einsteinRoutineSelfTestDeviation"] = self_test
    checks["einsteinRoutineKnownMetrics"] = self_test <= 1e-12
    checks["einsteinTensorFromMetric"] = einstein_dev <= EINSTEIN_LIMIT
    checks["diracEquationFd"] = dirac_rows > 0 and dirac_fd <= DIRAC_FD_LIMIT and kinetic_fd <= DIRAC_FD_LIMIT
    checks["boundNonnegative"] = bound_min >= 0.0 and bound_identity <= IDENTITY_LIMIT
    checks["closedFormVerified"] = closed_fd <= CLOSED_FORM_LIMIT and quad_dev <= QUADRATURE_LIMIT
    checks["exactSolution"] = exact_dev <= EXACT_LIMIT
    checks["spinorShape"] = shape_dev <= SPINOR_SHAPE_LIMIT
    checks["spinorPhaseWithinTimeRounding"] = phase_ok
    checks["phaseDriftIsTimeRounding"] = binade_count >= 15 and binade_dev <= 0.05
    checks["lateTimeDust"] = late_dev <= LATE_TIME_LIMIT and anis_monotone
    checks["extraTimesExpand"] = turn_ok
    checks["thetaBoundPositiveEnergy"] = (theta_ratio_min > 1.0 / math.sqrt(3.0)
                                          and dust_w_eff_min > -1.0 + 1.0 / math.sqrt(3.0))
    checks["kasnerExponents"] = kasner_dev <= KASNER_LIMIT
    checks["phantomStructure"] = phantom_ok
    rust = summary["measurements"]
    checks["summaryConsistent"] = (
        summary["verdict"] == "SUCCESS" and all(summary["checks"].values())
        and summary_dev <= SUMMARY_LIMIT
        and abs(rust["maxConstraintRelative"] - constraint_max) <= SUMMARY_LIMIT)
    measurements["fdGravityStencilPoints"] = 2 * GRAVITY_HALF + 1
    measurements["fdSpinorStencilPoints"] = 2 * SPINOR_HALF + 1
    measurements.update({
        "derivedMaxDeviation": derived_dev,
        "identityMaxDeviation": identity_dev,
        "constraintRelativeMax": constraint_max,
        "anisotropyVolumeMaxDrift": anis_dev,
        "scalarDensityVolumeMaxDrift": sv_dev,
        "normMaxDrift": norm_dev,
        "continuityFdMaxRelative": continuity_fd,
        "evolutionFdMaxRelative": evolution_fd,
        "einsteinTensorMaxRelative": einstein_dev,
        "diracFdMaxRelative": dirac_fd,
        "kineticFdMaxRelative": kinetic_fd,
        "diracFdRows": dirac_rows,
        "boundMin": bound_min,
        "boundIdentityMaxDeviation": bound_identity,
        "closedFormFdMaxRelative": closed_fd,
        "jQuadratureMaxDeviation": quad_dev,
        "exactMaxRelativeError": exact_dev,
        "spinorExactMaxError": spinor_dev,
        "spinorShapeMaxError": shape_dev,
        "spinorPhaseMaxError": phase_dev,
        "phaseDriftBinadeMaxRelativeDeviation": binade_dev,
        "phaseDriftBinadesTested": binade_count,
        "lateTimeMaxDeviation": late_dev,
        "thetaOver3HaMinPositiveEnergy": theta_ratio_min,
        "thetaOver3HaMinAllRows": theta_ratio_min_all,
        "dustMinWeff": dust_w_eff_min,
        "kasnerMaxDeviation": kasner_dev,
        "summaryMaxDeviation": summary_dev,
    })
    return checks, measurements, summary, run_reports


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


def run_errors(directory, run, gammas, b_matrix):
    """Errors of one run's CSV against the closed form: gravity (relative, per
    amplification), spinor shape (phase-invariant), spinor phase and its
    time-rounding bound (from the run's own step counts)."""
    header, data = read_csv(os.path.join(directory, run["file"]))
    t = data[:, 0]
    i0 = int(np.where(t == 0.0)[0][0])
    u = data[:, 7:23] + 1j * data[:, 23:39]
    s0 = float(np.vdot(u[i0], (-1j * gammas[4]) @ u[i0]).real)
    rates7_0 = expand_groups(np.array([HUBBLE0]))
    c0 = float(pair_sum_generic(rates7_0)[0])
    s0_density = c0 / (KAPPA * MASS * s0 * (1.0 + run["x0"] * s0))
    lam = 2.0 * MASS * run["x0"] / s0_density
    bg = Background(float(rates7_0.sum()), MASS * s0_density * s0)
    amplification = 1.0 + abs(bg.r_near) / (t - bg.r_near)
    exact_rates = np.stack([bg.hubble(h, t) for h in HUBBLE0], axis=1)
    exact_ln = np.stack([bg.ln_scale(h, t) for h in HUBBLE0], axis=1)
    scale = np.sum(np.abs(expand_groups(exact_rates)), axis=1)
    gravity = max(float(np.max(np.max(np.abs(data[:, 4:7] - exact_rates), axis=1) / scale / amplification)),
                  float(np.max(np.max(np.abs(data[:, 1:4] - exact_ln) / (1.0 + np.abs(exact_ln)), axis=1)
                               / amplification)))
    phase = MASS * t + lam * s0_density * s0 * bg.j_integral(t)
    overlap = u @ u[i0].conj()
    shape = float(np.max(np.linalg.norm(u - overlap[:, None] * u[i0][None, :], axis=1)
                         + np.abs(np.abs(overlap) - 1.0)))
    phase_series = np.angle(overlap * np.exp(1j * phase))
    phase_error = float(np.max(np.abs(phase_series)))
    q = recompute(gammas, b_matrix, data, s0_density, lam)
    forward_rows = t >= 0.0
    bound = (float(np.max(np.abs(q["M_eff"][forward_rows]))) * run["solver"]["forward"]["steps"]
             * float(np.spacing(t[-1])) / 2.0
             + float(np.max(np.abs(q["M_eff"][~forward_rows]))) * run["solver"]["backward"]["steps"]
             * float(np.spacing(abs(t[0]))) / 2.0)
    return gravity, shape, phase_error, bound, data, amplification, phase_series, q["M_eff"]


def refined_convergence(root, refined_root, summary, fixture_path):
    gammas = load_fixture_algebra(fixture_path)
    _, _, b_matrix = algebra_checks(gammas)
    with open(os.path.join(refined_root, EXPERIMENT, "summary.json"), "r", encoding="utf-8") as h:
        refined = json.load(h)
    ok = refined["refined"] is True and refined["verdict"] == "SUCCESS"
    tol, rtol = summary["tolerances"], refined["tolerances"]
    ok &= (abs(rtol["rtol"] - tol["rtol"] / 10.0) <= 1e-30
           and abs(rtol["atol"] - tol["atol"] / 10.0) <= 1e-33
           and abs(rtol["maxStep"] - tol["maxStep"] / 2.0) <= 1e-18)
    refined_runs = {run["id"]: run for run in refined["runs"]}
    report = {"gravityCanonical": 0.0, "gravityRefined": 0.0, "gravityDifference": 0.0,
              "spinorShapeCanonical": 0.0, "spinorShapeRefined": 0.0,
              "spinorPhaseCanonical": 0.0, "spinorPhaseRefined": 0.0,
              "spinorPhaseBoundCanonical": 0.0, "spinorPhaseBoundRefined": 0.0,
              "spinorPhaseDifference": 0.0, "spinorModulusDifference": 0.0,
              "refinedPhaseDriftBinadeDeviation": 0.0}
    phase_ok = True
    binades = 0
    for run in summary["runs"]:
        run_r = refined_runs.get(run["id"])
        if run_r is None:
            return False, report
        g_c, sh_c, ph_c, b_c, data_c, amp, _, _ = run_errors(os.path.join(root, EXPERIMENT), run,
                                                             gammas, b_matrix)
        g_r, sh_r, ph_r, b_r, data_r, _, series_r, m_eff_r = run_errors(
            os.path.join(refined_root, EXPERIMENT), run_r, gammas, b_matrix)
        deviation, count = phase_drift_binade_test(data_r[:, 0], series_r, m_eff_r,
                                                   refined["tolerances"]["maxStep"], data_r[-1, 0])
        report["refinedPhaseDriftBinadeDeviation"] = max(report["refinedPhaseDriftBinadeDeviation"], deviation)
        binades += count
        ok &= data_c.shape == data_r.shape and bool(np.all(data_c[:, 0] == data_r[:, 0]))
        for key, value in (("gravityCanonical", g_c), ("gravityRefined", g_r),
                           ("spinorShapeCanonical", sh_c), ("spinorShapeRefined", sh_r),
                           ("spinorPhaseCanonical", ph_c), ("spinorPhaseRefined", ph_r),
                           ("spinorPhaseBoundCanonical", b_c), ("spinorPhaseBoundRefined", b_r)):
            report[key] = max(report[key], value)
        phase_ok &= ph_c <= b_c + PHASE_TRUNCATION_ALLOWANCE and ph_r <= b_r + PHASE_TRUNCATION_ALLOWANCE
        diff_rates = np.max(np.abs(data_c[:, 4:7] - data_r[:, 4:7]), axis=1)
        scale = np.sum(np.abs(expand_groups(data_c[:, 4:7])), axis=1)
        report["gravityDifference"] = max(report["gravityDifference"],
                                          float(np.max(diff_rates / scale / amp)))
        uc = data_c[:, 7:23] + 1j * data_c[:, 23:39]
        ur = data_r[:, 7:23] + 1j * data_r[:, 23:39]
        cross = np.einsum("ni,ni->n", uc.conj(), ur)
        report["spinorPhaseDifference"] = max(report["spinorPhaseDifference"],
                                              float(np.max(np.abs(np.angle(cross)))))
        report["spinorModulusDifference"] = max(report["spinorModulusDifference"],
                                                float(np.max(np.abs(np.abs(cross) - 1.0))))
    floor = 1.0e-12
    # Truncation-controlled errors (gravity, spinor shape) must improve (or
    # sit at the floor) and the runs must agree to within the canonical error.
    # The spinor phase error is time-rounding dominated (it does not shrink
    # with more steps); both runs must stay within their own rounding bound,
    # and so must their phase difference.
    ok &= report["gravityRefined"] <= max(report["gravityCanonical"], floor)
    ok &= report["spinorShapeRefined"] <= max(report["spinorShapeCanonical"], floor)
    ok &= report["gravityDifference"] <= 2.0 * report["gravityCanonical"] + floor
    ok &= report["spinorModulusDifference"] <= 2.0 * report["spinorShapeCanonical"] + floor
    ok &= phase_ok and binades >= 15 and report["refinedPhaseDriftBinadeDeviation"] <= 0.05
    ok &= report["spinorPhaseDifference"] <= (report["spinorPhaseBoundCanonical"]
                                              + report["spinorPhaseBoundRefined"]
                                              + 2.0 * PHASE_TRUNCATION_ALLOWANCE)
    return ok, report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=DEFAULT_ROOT)
    parser.add_argument("--fixture", default=DEFAULT_FIXTURE)
    parser.add_argument("--binary", default=DEFAULT_BINARY)
    parser.add_argument("--repeat")
    parser.add_argument("--refined")
    arguments = parser.parse_args(argv)
    root = os.path.abspath(arguments.output)
    checks, measurements, summary, run_reports = verify(root, arguments.fixture)
    if arguments.repeat:
        ran, _ = run_binary(arguments.binary, [EXPERIMENT, "--output", os.path.abspath(arguments.repeat)])
        checks["repeatByteIdentity"] = ran and compare_repeat(root, os.path.abspath(arguments.repeat), summary)
    if arguments.refined:
        refined_root = os.path.abspath(arguments.refined)
        ran, _ = run_binary(arguments.binary, [EXPERIMENT, "--refined", "--output", refined_root])
        ok, report = (False, {})
        if ran:
            ok, report = refined_convergence(root, refined_root, summary, arguments.fixture)
        checks["refinedConvergence"] = ok
        for name, value in report.items():
            measurements["refined_" + name] = value
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
        "checker": "scripts/check_dirac16complex_exp2.py",
        "experiment": EXPERIMENT,
        "fixtureSha256": sha256_file(arguments.fixture),
        "checks": checks,
        "measurements": measurements,
        "runs": run_reports,
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
