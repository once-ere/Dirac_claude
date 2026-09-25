"""Independent checker of EXP-3 (4D-effective dirac16complex dark energy).

numpy + standard library only.  The gamma matrices are rebuilt from the
algebra fixture; every physical quantity is recomputed from the CSV *state*
columns (N, H0t, D_C, u_re_*, u_im_*, ln_sigma) and the physics of
NUMERICS_CONTRACT.md EXP-3; the derived CSV columns are only compared
against these recomputations, never used as truth.

Physics (units H0 = 1, densities in units of 3 H0^2/kappa_4, N = ln a):
  E^2 = Omega_r a^-4 + Omega_m a^-3 + rho_psi,  A = Omega_psi/(1 + x0),
  rho_psi = A sigma (1 + x0 sigma),  p_psi = A x0 sigma^2,
  w = x0 sigma/(1 + x0 sigma),  sigma = a^-3 s(u)/s(u0),  s(u) = u^dag(-i g4)u,
  du/dN = -i (M_eff/H0)(-i g4) u / E,  M_eff/H0 = mu (1 + 2 x0 sigma)/(1 + 2 x0),
  dH0t/dN = 1/E,  dD_C/dN = -1/(a E),  d ln sigma/dN = -3.

Checks (check_<name>=true/false):
  provenance / algebra / parametersMatchContract / structure*
  closureE0            Omega_r + Omega_m + Omega_psi = 1 and E(N=0) = 1
  initialEigenvector   u0: h(1) u0 = mu u0, B u0 = u0, s(u0) = 1
  columnsRecomputed    every derived column vs the recomputation from state
  sigmaSpinor          a^3 sigma_spinor = 1 (<= 1e-8); sigmaState exp(ln sigma)
  rhoClosedForm        rho_psi(a) vs A a^-3 (1 + x0 a^-3) (scaled, <= 1e-8)
  wClosedForm          w(a) vs x0 a^-3/(1 + x0 a^-3) (condition-scaled)
  energySplitClosedForm KE_L, PE_L closed forms; KE_H = 0; PE_H = rho
  kineticDefinitionFD  KE_L vs (A/2) n_hat E (-Im u^dag du/dN)/(m/H0) with du/dN
                       by finite differences (the definition K_4/2, not on-shell)
  muIndependence       mu = 3 vs 7 rho, p, w, sigma agree (<= 1e-8)
  fdResidual           five-point FD residuals of all four ODE blocks, bounded by
                       a Richardson estimate (h vs 2h stencils) + 1e-7 scale
  decelerationFD       q vs -1 - d ln E/dN (FD of the recomputed E)
  referenceTimeDistance H0t, D_C vs Gauss-Legendre quadrature of 1/E, 1/(aE)
  referenceSpinorPhase u vs exp(-i Phi) u0, Phi = int (M_eff/H0)/E dN (quadrature)
  bounceAndStop        bounce a_b from numpy.roots of the cubic (Omega_m + A)a^3
                       + Omega_r a^2 + A x0; backward stop at N_b + margin
  rhoZeroLocation      data zero of rho vs |x0|^(1/3)
  phantomCrossing      data zero of rho + p vs (2|x0|)^(1/3)
  decelerationRoots    data sign changes of q vs numpy.roots of the q numerator
  tangentCPL           w0 = x0/(1+x0), wa = 3x0/(1+x0)^2 (analytic, FD, summary)
  summaryConsistent    Rust summary vs the recomputation
  optional --repeat DIR (byte identity) / --refined DIR (convergence).

Usage: python scripts/check_dirac16complex_exp3.py [--output ROOT]
       [--fixture PATH] [--binary PATH] [--repeat DIR] [--refined DIR]
Writes <ROOT>/exp3/python-check-report.json; exits 1 on any failed check.
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
EXPERIMENT = "exp3"
ETA = np.array([1, 1, 1, 1, -1, -1, -1, -1], dtype=float)

# Contract values (NUMERICS_CONTRACT EXP-3).
OMEGA_R, OMEGA_M, OMEGA_PSI = 0.00009, 0.305, 0.69491
X0_CONTRACT = [-0.462654, -0.433107, -0.3, -0.2, 0.0]
MU_CONTRACT = [3.0, 7.0]
A_MIN, A_MAX = 1.0 / 3.5, 2.0

CLOSURE_LIMIT = 1e-14
EIGEN_LIMIT = 1e-12
COLUMN_LIMIT = 1e-12
SIGMA_LIMIT = 1e-8
SIGMA_STATE_LIMIT = 1e-12
CLOSED_LIMIT = 1e-8
MU_LIMIT = 1e-8
KINETIC_LIMIT = 1e-6
FD_TOL = 1e-7
REF_TIME_LIMIT = 1e-8
REF_SPINOR_LIMIT = 1e-7
ROOT_LIMIT = 1e-7
WA_LIMIT = 1e-5
GL_NODES, GL_WEIGHTS = np.polynomial.legendre.leggauss(8)


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
    header = ["N", "a", "z", "branch", "H0t", "D_C"]
    header += ["u_re_%d" % i for i in range(16)] + ["u_im_%d" % i for i in range(16)]
    return header + ["ln_sigma", "E", "q", "rho_psi", "p_psi", "w", "KE_L", "PE_L", "KE_H",
                     "PE_H", "Omega_psi", "Omega_m", "cs2", "M_eff_over_H0", "s_u",
                     "sigma_spinor", "sigma_state", "sigma_analytic", "norm_hilbert",
                     "norm_krein", "eigen_leak", "rho_closed", "p_closed", "w_closed", "d_L",
                     "mu_H0free"]


class Model:
    """Closed forms of the 4D-effective model (sigma = a^-3 unless given)."""

    def __init__(self, x0, mu):
        self.x0, self.mu = x0, mu
        self.amp = OMEGA_PSI / (1.0 + x0)

    def rho(self, sigma):
        return self.amp * sigma * (1.0 + self.x0 * sigma)

    def p(self, sigma):
        return self.amp * self.x0 * sigma ** 2

    def e2(self, n, sigma=None):
        s = np.exp(-3.0 * n) if sigma is None else sigma
        return OMEGA_R * np.exp(-4.0 * n) + OMEGA_M * np.exp(-3.0 * n) + self.rho(s)

    def omega(self, n, sigma=None):
        """(M_eff/H0)/E: the spinor phase rate dPhi/dN."""
        s = np.exp(-3.0 * n) if sigma is None else sigma
        meff = self.mu * (1.0 + 2.0 * self.x0 * s) / (1.0 + 2.0 * self.x0)
        return meff / np.sqrt(self.e2(n, s))

    def bounce(self):
        """Real root in (0, 1) of (Omega_m + A) a^3 + Omega_r a^2 + A x0 (numpy.roots)."""
        if self.x0 >= 0.0:
            return None
        roots = np.roots([OMEGA_M + self.amp, OMEGA_R, 0.0, self.amp * self.x0])
        real = [r.real for r in roots if abs(r.imag) < 1e-12 and 0.0 < r.real < 1.0]
        return real[0] if len(real) == 1 else float("nan")

    def q_roots(self, a_lo, a_hi):
        """a where q = 0: 2 Omega_r a^2 + (Omega_m + A) a^3 + 4 A x0 = 0 (times a^6)."""
        roots = np.roots([OMEGA_M + self.amp, 2.0 * OMEGA_R, 0.0, 4.0 * self.amp * self.x0])
        return sorted(r.real for r in roots
                      if abs(r.imag) < 1e-12 and a_lo < r.real < a_hi and self.x0 != 0.0)


def cumulative_quadrature(f, nodes):
    """I_k = int_{nodes[0]}^{nodes[k]} f, composite 8-point Gauss-Legendre per interval."""
    left, right = nodes[:-1], nodes[1:]
    half, mid = 0.5 * (right - left), 0.5 * (right + left)
    points = mid[:, None] + half[:, None] * GL_NODES[None, :]
    panel = half * (f(points) @ GL_WEIGHTS)
    return np.concatenate([[0.0], np.cumsum(panel)])


def fd5(values, h):
    """Five-point central derivative (interior points 2..n-3), axis 0."""
    return (values[:-4] - 8.0 * values[1:-3] + 8.0 * values[3:-1] - values[4:]) / (12.0 * h)


def richardson_residual(values, rhs, h, scale):
    """max over interior points of |D_h - f| / (3 |D_h - D_2h| / 15 + FD_TOL scale).

    D_h, D_2h: five-point stencils with steps h and 2h (points i +- 4 needed).
    A CSV that solves a different ODE gives |D_h - f| = O(1) with D_h ~ D_2h."""
    n = len(values)
    if n < 9:
        return 0.0
    d_h = fd5(values, h)[2:-2]
    d_2h = (values[:-8] - 8.0 * values[2:-6] + 8.0 * values[6:-2] - values[8:]) / (24.0 * h)
    f = rhs[4:-4]
    sc = scale[4:-4]
    if values.ndim == 1:
        err = np.abs(d_h - f)
        est = np.abs(d_h - d_2h) / 15.0
    else:
        err = np.linalg.norm(d_h - f, axis=1)
        est = np.linalg.norm(d_h - d_2h, axis=1) / 15.0
    return float(np.max(err / (3.0 * est + FD_TOL * sc)))


def interpolated_roots(ns, values):
    """Sign changes of values(ns) refined on the local cubic through 4 points."""
    roots = []
    count = len(ns)
    for i in range(count - 1):
        if values[i] == 0.0:
            roots.append(ns[i])
            continue
        if values[i] * values[i + 1] > 0.0:
            continue
        start = min(max(i - 1, 0), count - 4)
        x, y = ns[start:start + 4], values[start:start + 4]
        centre = x.mean()
        coefficients = np.polyfit(x - centre, y, 3)
        cand = [r.real + centre for r in np.roots(coefficients)
                if abs(r.imag) < 1e-9 and ns[i] - 1e-12 <= r.real + centre <= ns[i + 1] + 1e-12]
        roots.append(cand[0] if cand else float("nan"))
    return roots


class Run:
    """One CSV recomputed from its state columns."""

    def __init__(self, directory, run, gammas):
        self.meta = run
        self.header, self.data = read_csv(os.path.join(directory, run["file"]))
        self.col = {name: index for index, name in enumerate(self.header)}
        d = self.data
        self.model = Model(run["x0"], run["mu"])
        self.n = d[:, 0]
        self.branch = d[:, 3]
        self.t = d[:, 4]
        self.dc = d[:, 5]
        self.u = d[:, 6:22] + 1j * d[:, 22:38]
        self.ln_sigma = d[:, 38]
        g4 = gammas[4].astype(complex)
        self.o = -1j * g4
        charge = gammas[0] @ gammas[1] @ gammas[2] @ gammas[3]
        self.b = -1j * (charge @ gammas[4])
        m = self.model
        self.a = np.exp(self.n)
        self.z = np.exp(-self.n) - 1.0
        self.a3 = np.exp(-3.0 * self.n)
        self.s = np.einsum("ni,ij,nj->n", self.u.conj(), self.o, self.u).real
        self.i0 = int(np.flatnonzero(self.n == 0.0)[0]) if np.any(self.n == 0.0) else -1
        self.s0 = self.s[self.i0]
        self.sigma = self.a3 * self.s / self.s0
        self.e2 = m.e2(self.n, self.sigma)
        self.e = np.sqrt(self.e2)
        self.meff_m = 1.0 + 2.0 * m.x0 * self.sigma
        self.mass_h0 = m.mu / (1.0 + 2.0 * m.x0)
        eps_hat = np.einsum("ni,ij,nj->n", self.u.conj(), self.o, self.u).real * self.meff_m
        n_hat = self.a3 / self.s0
        self.rho = m.amp * (n_hat * eps_hat - m.x0 * self.sigma ** 2)
        self.p = m.amp * m.x0 * self.sigma ** 2
        self.w = self.p / self.rho
        self.ke_l = 0.5 * m.amp * n_hat * eps_hat
        self.pe_l = self.rho - self.ke_l
        self.pe_h = m.amp * (self.sigma + m.x0 * self.sigma ** 2)
        self.q = (2.0 * OMEGA_R * np.exp(-4.0 * self.n) + OMEGA_M * self.a3 + self.rho
                  + 3.0 * self.p) / (2.0 * self.e2)
        self.cs2 = 2.0 * m.x0 * self.sigma / (1.0 + 2.0 * m.x0 * self.sigma)
        self.hilbert = np.einsum("ni,ni->n", self.u.conj(), self.u).real
        self.krein = np.einsum("ni,ij,nj->n", self.u.conj(), self.b, self.u).real
        ou = self.u @ self.o.T
        self.leak = 0.5 * np.linalg.norm(self.u - ou, axis=1) / np.sqrt(self.hilbert)
        self.dl = (1.0 + self.z) * self.dc
        with np.errstate(divide="ignore", invalid="ignore"):
            self.mu_mod = np.where((self.z > 0) & (self.dl > 0),
                                   5.0 * np.log10(np.where(self.dl > 0, self.dl, 1.0)), np.nan)
        # closed forms with sigma = a^-3
        self.rho_cf = m.rho(self.a3)
        self.p_cf = m.p(self.a3)
        self.w_cf = m.x0 * self.a3 / (1.0 + m.x0 * self.a3)
        self.scale = m.amp * self.a3 * (1.0 + abs(m.x0) * self.a3)
        self.w_cond = np.abs(1.0 + m.x0 * self.a3) / np.maximum(np.abs(self.w_cf), 1.0)
        self.du = -(self.meff_m * self.mass_h0 / self.e)[:, None] * (self.u @ g4.T)

    def column(self, name):
        return self.data[:, self.col[name]]

    def branches(self):
        """(indices ascending in N, step) for the backward and the forward branch."""
        back = np.flatnonzero(self.branch <= 0.0)
        fwd = np.flatnonzero(self.branch >= 0.0)
        return [(back, (self.n[back[-1]] - self.n[back[0]]) / (len(back) - 1)),
                (fwd, (self.n[fwd[-1]] - self.n[fwd[0]]) / (len(fwd) - 1))]


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
    checks["provenanceSchema"] = summary["schemaVersion"] == 1 and summary["experiment"] == EXPERIMENT
    gammas = load_gammas(fixture_path)
    identity = np.eye(16)
    charge = gammas[0] @ gammas[1] @ gammas[2] @ gammas[3]
    b_matrix = -1j * (charge @ gammas[4])
    checks["algebraFromFixture"] = (
        all(np.array_equal(gammas[a] @ gammas[b] + gammas[b] @ gammas[a],
                           (2.0 * ETA[a] if a == b else 0.0) * identity)
            for a in range(8) for b in range(8))
        and np.array_equal(b_matrix, b_matrix.conj().T) and np.allclose(b_matrix @ b_matrix, identity)
        and np.array_equal(gammas[4] @ gammas[4], -identity))

    par = summary["parameters"]
    checks["parametersMatchContract"] = (
        par["OmegaR"] == OMEGA_R and par["OmegaM"] == OMEGA_M and par["OmegaPsi"] == OMEGA_PSI
        and par["x0Values"] == X0_CONTRACT and par["muValues"] == MU_CONTRACT
        and abs(par["aMin"] - A_MIN) <= 1e-16 and par["aMax"] == A_MAX
        and abs(par["nMin"] + math.log(3.5)) <= 1e-15 and abs(par["nMax"] - math.log(2.0)) <= 1e-15
        and len(summary["runs"]) == len(X0_CONTRACT) * len(MU_CONTRACT))
    checks["structureFilesPresent"] = all(os.path.exists(os.path.join(directory, f))
                                          for f in summary["files"])
    closure = abs(OMEGA_R + OMEGA_M + OMEGA_PSI - 1.0)

    runs = [Run(directory, run, gammas) for run in summary["runs"]]
    header_ok = grid_ok = finite_ok = True
    e0_dev = eigen_dev = 0.0
    column_dev = 0.0
    sigma_dev = sigma_state_dev = 0.0
    rho_dev = p_dev = w_dev = split_dev = 0.0
    kinetic_dev = 0.0
    fd_ratio = decel_ratio = 0.0
    ref_t = ref_dc = ref_u = 0.0
    bounce_ok = True
    bounce_dev = 0.0
    zero_dev = cross_dev = qroot_dev = 0.0
    w0_dev = wa_dev = wa_fd_dev = 0.0
    summary_dev = 0.0
    margin = par["bounceMargin"]
    n_min, n_max = -math.log(3.5), math.log(2.0)
    for r in runs:
        m = r.model
        header_ok &= r.header == expected_header()
        # --- structure: grid, branches, N = 0 once, finiteness
        n_back = par["backwardIntervals"]
        n_fwd = par["forwardIntervals"]
        back_idx = np.flatnonzero(r.branch < 0.0)[::-1]
        fwd_idx = np.flatnonzero(r.branch > 0.0)
        k_back = np.arange(1, len(back_idx) + 1)
        grid_ok &= (r.i0 >= 0 and int(np.sum(r.n == 0.0)) == 1 and r.branch[r.i0] == 0.0
                    and bool(np.all(np.diff(r.n) > 0.0))
                    and bool(np.all(np.abs(r.n[back_idx] - n_min * k_back / n_back) <= 1e-15))
                    and len(fwd_idx) == n_fwd
                    and bool(np.all(np.abs(r.n[fwd_idx] - n_max * np.arange(1, n_fwd + 1) / n_fwd)
                                    <= 1e-15)))
        states = np.concatenate([r.data[:, :r.col["mu_H0free"]]], axis=1)
        finite_ok &= bool(np.all(np.isfinite(states)))
        past = r.z > 0.0
        finite_ok &= bool(np.all(np.isfinite(r.column("mu_H0free")[past])))
        finite_ok &= bool(np.all(np.isnan(r.column("mu_H0free")[~past])))

        # --- closure and initial eigenvector
        e0_dev = max(e0_dev, abs(r.e[r.i0] - 1.0), abs(m.e2(0.0) - 1.0))
        u0 = r.u[r.i0]
        h0 = m.mu * r.o
        eigen_dev = max(eigen_dev, float(np.max(np.abs(h0 @ u0 - m.mu * u0))),
                        float(np.max(np.abs(r.b @ u0 - u0))), abs(r.s0 - 1.0),
                        abs(np.vdot(u0, u0).real - 1.0))

        # --- derived columns vs recomputation
        comparisons = [
            ("a", r.a, r.a), ("z", r.z, np.maximum(np.abs(r.z), 1.0)),
            ("E", r.e, r.e), ("q", r.q, np.maximum(np.abs(r.q), 1.0)),
            ("rho_psi", r.rho, r.scale), ("p_psi", r.p, r.scale),
            ("w", r.w, 1.0 / r.w_cond),
            ("KE_L", r.ke_l, r.scale), ("PE_L", r.pe_l, r.scale), ("KE_H", 0.0 * r.n, r.scale),
            ("PE_H", r.pe_h, r.scale), ("Omega_psi", r.rho / r.e2, r.scale / r.e2),
            ("Omega_m", OMEGA_M * r.a3 / r.e2, OMEGA_M * r.a3 / r.e2),
            ("cs2", r.cs2, np.maximum(np.abs(r.cs2), 1.0) / np.abs(1.0 + 2.0 * m.x0 * r.a3)
             if m.x0 != 0.0 else 1.0),
            ("M_eff_over_H0", m.mu * r.meff_m / (1.0 + 2.0 * m.x0), m.mu * (1.0 + 2 * abs(m.x0) * r.a3)),
            ("s_u", r.s, 1.0), ("sigma_spinor", r.sigma, r.a3), ("sigma_state", np.exp(r.ln_sigma), r.a3),
            ("sigma_analytic", r.a3, r.a3), ("norm_hilbert", r.hilbert, 1.0),
            ("norm_krein", r.krein, 1.0), ("eigen_leak", r.leak, 1.0),
            ("rho_closed", r.rho_cf, r.scale), ("p_closed", r.p_cf, r.scale),
            ("w_closed", r.w_cf, 1.0 / r.w_cond), ("d_L", r.dl, np.maximum(np.abs(r.dl), 1.0)),
        ]
        for name, values, scale in comparisons:
            column_dev = max(column_dev, float(np.max(np.abs(r.column(name) - values) / scale)))
        column_dev = max(column_dev, float(np.max(np.abs(r.column("mu_H0free")[past]
                                                          - r.mu_mod[past]))))

        # --- sigma, closed forms, energy split
        sigma_dev = max(sigma_dev, float(np.max(np.abs(r.sigma / r.a3 - 1.0))))
        sigma_state_dev = max(sigma_state_dev, float(np.max(np.abs(np.exp(r.ln_sigma) / r.a3 - 1.0))))
        rho_dev = max(rho_dev, float(np.max(np.abs(r.rho - r.rho_cf) / r.scale)))
        p_dev = max(p_dev, float(np.max(np.abs(r.p - r.p_cf) / r.scale)))
        w_dev = max(w_dev, float(np.max(np.abs(r.w - r.w_cf) * r.w_cond)))
        ke_cf = 0.5 * OMEGA_PSI * r.a3 * (1.0 + 2.0 * m.x0 * r.a3) / (1.0 + m.x0)
        pe_cf = 0.5 * OMEGA_PSI * r.a3 / (1.0 + m.x0)
        split_dev = max(split_dev, float(np.max((np.abs(r.ke_l - ke_cf) + np.abs(r.pe_l - pe_cf)
                                                 + np.abs(r.pe_h - r.rho_cf)
                                                 + np.abs(r.ke_l + r.pe_l - r.rho)
                                                 + np.abs(r.ke_l - r.pe_l - r.p)) / r.scale)))

        # --- FD residuals, kinetic definition, deceleration, references
        for idx, h in r.branches():
            nn = r.n[idx]
            e = r.e[idx]
            a = r.a[idx]
            one = np.ones(len(idx))
            fd_ratio = max(fd_ratio,
                           richardson_residual(r.t[idx], 1.0 / e, h, 1.0 / e),
                           richardson_residual(r.dc[idx], -1.0 / (a * e), h, 1.0 / (a * e)),
                           richardson_residual(r.ln_sigma[idx], -3.0 * one, h, 3.0 * one),
                           richardson_residual(r.u[idx], r.du[idx], h,
                                               np.linalg.norm(r.du[idx], axis=1) + 1.0))
            decel = -1.0 - fd5(np.log(e), h)
            ln_e_ratio = richardson_residual(np.log(e), -1.0 - r.q[idx], h, np.abs(r.q[idx]) + 1.0)
            decel_ratio = max(decel_ratio, ln_e_ratio)
            # kinetic term by definition: KE_L = K_4/2, K_4 = -Im(u^dag du/dt) per mode,
            # du/dt = E du/dN with du/dN from the h and 2h five-point stencils;
            # ratio to the Richardson bound (as in fdResidual).
            if len(idx) >= 9:
                uu = r.u[idx]
                inner = idx[4:-4]
                d_h = fd5(uu, h)[2:-2]
                d_2h = (uu[:-8] - 8.0 * uu[2:-6] + 8.0 * uu[6:-2] - uu[8:]) / (24.0 * h)
                factor = 0.5 * m.amp * (r.a3[inner] / r.s0) * r.e[inner] / r.mass_h0
                ke_h = -factor * np.einsum("ni,ni->n", r.u[inner].conj(), d_h).imag
                ke_2h = -factor * np.einsum("ni,ni->n", r.u[inner].conj(), d_2h).imag
                bound = 3.0 * np.abs(ke_h - ke_2h) / 15.0 + KINETIC_LIMIT * r.scale[inner]
                kinetic_dev = max(kinetic_dev, float(np.max(np.abs(ke_h - r.ke_l[inner]) / bound)))
            del decel
            # references by quadrature (closed-form E, sigma = a^-3), cumulative from N = 0
            order = idx if nn[0] == 0.0 else idx[::-1]
            nodes = r.n[order]
            t_ref = cumulative_quadrature(lambda x: 1.0 / np.sqrt(m.e2(x)), nodes)
            dc_ref = cumulative_quadrature(lambda x: -1.0 / (np.exp(x) * np.sqrt(m.e2(x))), nodes)
            phi = cumulative_quadrature(lambda x: m.omega(x), nodes)
            ref_t = max(ref_t, float(np.max(np.abs(r.t[order] - t_ref))))
            ref_dc = max(ref_dc, float(np.max(np.abs(r.dc[order] - dc_ref))))
            u_ref = np.exp(-1j * phi)[:, None] * u0[None, :]
            ref_u = max(ref_u, float(np.max(np.linalg.norm(r.u[order] - u_ref, axis=1))))

        # --- bounce and backward stop
        a_b = m.bounce()
        model_meta = next(x for x in summary["models"] if x["x0"] == m.x0)
        back_step = abs(n_min) / par["backwardIntervals"]
        n_end = r.n[0]
        if a_b is None:
            bounce_ok &= model_meta["aBounce"] is None and n_end == r.n[0] and \
                abs(n_end - n_min) <= 1e-15 and len(back_idx) == n_back
        else:
            n_b = math.log(a_b)
            gap = n_end - n_b
            bounce_ok &= (margin - 1e-13 <= gap < margin + back_step) and bool(np.all(r.e2 > 0.0))
            bounce_ok &= abs(m.e2(n_b)) <= 1e-12 and model_meta["contractBackwardRangeReachable"] is False
            bounce_dev = max(bounce_dev, abs(model_meta["aBounce"] - a_b) / a_b)

        # --- roots from the recomputed data vs analytic
        zeros = interpolated_roots(r.n, r.rho)
        crosses = interpolated_roots(r.n, r.rho + r.p)
        qzeros = interpolated_roots(r.n, r.q)
        if m.x0 < 0.0:
            a0 = abs(m.x0) ** (1.0 / 3.0)
            ac = (2.0 * abs(m.x0)) ** (1.0 / 3.0)
            zero_dev = max(zero_dev, abs(math.exp(zeros[0]) - a0) / a0 if len(zeros) == 1 else math.inf)
            cross_dev = max(cross_dev, abs(math.exp(crosses[0]) - ac) / ac if len(crosses) == 1 else math.inf)
        else:
            zero_dev = max(zero_dev, 0.0 if not zeros else math.inf)
            cross_dev = max(cross_dev, 0.0 if not crosses else math.inf)
        q_expected = m.q_roots(r.a[0], r.a[-1])
        if len(q_expected) != len(qzeros):
            qroot_dev = math.inf
        else:
            for got, want in zip(qzeros, q_expected):
                qroot_dev = max(qroot_dev, abs(math.exp(got) - want) / want)
        measured = r.meta["measured"]
        summary_roots = [x["a"] for x in measured["decelerationSignChanges"]]
        if len(summary_roots) != len(q_expected):
            summary_dev = math.inf
        else:
            summary_dev = max([summary_dev] + [abs(x - y) / y for x, y in zip(summary_roots, q_expected)])

        # --- tangent CPL
        w0 = m.x0 / (1.0 + m.x0)
        wa = 3.0 * m.x0 / (1.0 + m.x0) ** 2
        window = slice(r.i0 - 2, r.i0 + 3)
        coefficients = np.polyfit(r.n[window], r.w[window], 4)
        wa_fd = -np.polyval(np.polyder(coefficients), 0.0)
        w0_dev = max(w0_dev, abs(r.w[r.i0] - w0), abs(measured["w0"] - w0), abs(model_meta["w0"] - w0))
        wa_fd_dev = max(wa_fd_dev, abs(wa_fd - wa) / max(abs(wa), 1.0))
        wa_dev = max(wa_dev, abs(model_meta["waTangent"] - wa) / max(abs(wa), 1.0),
                     abs(measured["waTangent"] - wa) / max(abs(wa), 1.0))
        dev = r.meta["maxDeviation"]
        summary_dev = max(summary_dev,
                          abs(dev["sigmaSpinorVsAnalytic"] - float(np.max(np.abs(r.sigma / r.a3 - 1.0)))),
                          abs(r.meta["massOverH0"] - r.mass_h0) / r.mass_h0,
                          abs(model_meta["q0"] - r.q[r.i0]),
                          abs(model_meta["cs2Today"] - r.cs2[r.i0]))
        if a_b is not None:
            summary_dev = max(summary_dev, abs(model_meta["zBounce"] - (1.0 / a_b - 1.0)),
                              abs(model_meta["aZero"] - abs(m.x0) ** (1.0 / 3.0)),
                              abs(model_meta["aPhantomCrossing"] - (2.0 * abs(m.x0)) ** (1.0 / 3.0)))

    # --- mu independence
    mu_rho = mu_p = mu_w = mu_sigma = 0.0
    mu_grid_ok = True
    for x0 in X0_CONTRACT:
        pair = [r for r in runs if r.model.x0 == x0]
        mu_grid_ok &= len(pair) == 2 and sorted(r.model.mu for r in pair) == MU_CONTRACT
        if len(pair) != 2 or len(pair[0].n) != len(pair[1].n):
            mu_grid_ok = False
            continue
        r1, r2 = pair
        mu_grid_ok &= bool(np.array_equal(r1.n, r2.n))
        mu_rho = max(mu_rho, float(np.max(np.abs(r1.rho - r2.rho) / r1.scale)))
        mu_p = max(mu_p, float(np.max(np.abs(r1.p - r2.p) / r1.scale)))
        mu_w = max(mu_w, float(np.max(np.abs(r1.w - r2.w) * r1.w_cond)))
        mu_sigma = max(mu_sigma, float(np.max(np.abs(r1.sigma - r2.sigma) / r1.a3)))
    summary_dev = max(summary_dev, abs(summary["measurements"]["maxMuDiffRho"] - mu_rho),
                      abs(summary["measurements"]["maxMuDiffSigma"] - mu_sigma))

    # --- fits.json of scripts/analyze_dirac16complex_exp3.py (checked when present)
    fits_path = os.path.join(directory, "fits.json")
    if os.path.exists(fits_path):
        with open(fits_path, "r", encoding="utf-8") as handle:
            fits = json.load(handle)
        fits_ok = fits["verdict"] == "SUCCESS" and all(fits["validation"]["checks"].values())
        fits_dev = 0.0
        for block in fits["models"]:
            meta = next(x for x in summary["models"] if x["x0"] == block["x0"])
            fits_dev = max(fits_dev, abs(block["tangentCPL"]["w0"] - meta["w0"]),
                           abs(block["tangentCPL"]["wa"] - meta["waTangent"]))
            fits_ok &= (block["aBounce"] is None) == (meta["aBounce"] is None)
            if meta["aBounce"] is not None:
                fits_dev = max(fits_dev, abs(block["aBounce"] - meta["aBounce"]),
                               abs(block["aZero"] - meta["aZero"]))
            pole_inside = meta["aZero"] is not None and meta["aZero"] >= 1.0 / 3.26
            bounce_inside = meta["aBounce"] is not None and meta["aBounce"] >= 1.0 / 3.26
            fits_ok &= (block["wFitRequested"]["status"] == "undefined") == pole_inside
            fits_ok &= (block["muFitRequested"]["status"] == "undefined") == bounce_inside
        gv = fits["gammaVariant"]
        x0g = -0.861 / (1.0 + 0.861)
        n_g = -0.60 * (1.0 + x0g) ** 2 / x0g
        fits_dev = max(fits_dev, abs(gv["x0"] - x0g), abs(gv["n"] - n_g), abs(gv["gamma"] - (1.0 - n_g / 3.0)))
        checks["fitsConsistent"] = fits_ok and fits_dev <= 1e-12
        measurements["fitsMaxDeviation"] = fits_dev

    checks["structureHeaders"] = header_ok
    checks["structureGrid"] = grid_ok
    checks["structureFinite"] = finite_ok
    checks["closureE0"] = closure <= CLOSURE_LIMIT and e0_dev <= CLOSURE_LIMIT
    checks["initialEigenvector"] = eigen_dev <= EIGEN_LIMIT
    checks["columnsRecomputed"] = column_dev <= COLUMN_LIMIT
    checks["sigmaSpinorVsAnalytic"] = sigma_dev <= SIGMA_LIMIT
    checks["sigmaStateVsAnalytic"] = sigma_state_dev <= SIGMA_STATE_LIMIT
    checks["rhoClosedForm"] = rho_dev <= CLOSED_LIMIT and p_dev <= CLOSED_LIMIT
    checks["wClosedForm"] = w_dev <= CLOSED_LIMIT
    checks["energySplitClosedForm"] = split_dev <= CLOSED_LIMIT
    checks["kineticDefinitionFD"] = kinetic_dev <= 1.0
    checks["muIndependence"] = mu_grid_ok and max(mu_rho, mu_p, mu_w, mu_sigma) <= MU_LIMIT
    checks["fdResidual"] = fd_ratio <= 1.0
    checks["decelerationFD"] = decel_ratio <= 1.0
    checks["referenceTimeDistance"] = ref_t <= REF_TIME_LIMIT and ref_dc <= REF_TIME_LIMIT
    checks["referenceSpinorPhase"] = ref_u <= REF_SPINOR_LIMIT
    checks["bounceAndStop"] = bounce_ok and bounce_dev <= 1e-12
    checks["rhoZeroLocation"] = zero_dev <= ROOT_LIMIT
    checks["phantomCrossing"] = cross_dev <= ROOT_LIMIT
    checks["decelerationRoots"] = qroot_dev <= ROOT_LIMIT
    checks["tangentCPL"] = w0_dev <= 1e-9 and wa_dev <= 1e-12 + WA_LIMIT and wa_fd_dev <= WA_LIMIT
    checks["summaryConsistent"] = (summary["verdict"] == "SUCCESS" and all(summary["checks"].values())
                                   and summary_dev <= 1e-6)
    measurements.update({
        "closureDefect": closure,
        "maxE0Deviation": e0_dev,
        "initialEigenResidual": eigen_dev,
        "columnMaxScaledDeviation": column_dev,
        "sigmaSpinorMaxRelDeviation": sigma_dev,
        "sigmaStateMaxRelDeviation": sigma_state_dev,
        "rhoClosedFormMaxScaledDeviation": rho_dev,
        "pClosedFormMaxScaledDeviation": p_dev,
        "wClosedFormMaxConditionScaledDeviation": w_dev,
        "energySplitMaxScaledDeviation": split_dev,
        "kineticDefinitionWorstRatioToBound": kinetic_dev,
        "muIndependenceRho": mu_rho,
        "muIndependenceP": mu_p,
        "muIndependenceW": mu_w,
        "muIndependenceSigma": mu_sigma,
        "fdResidualWorstRatioToBound": fd_ratio,
        "decelerationFdWorstRatioToBound": decel_ratio,
        "referenceTimeMaxAbsError": ref_t,
        "referenceDistanceMaxAbsError": ref_dc,
        "referenceSpinorMaxError": ref_u,
        "bounceRelDeviation": bounce_dev,
        "rhoZeroMaxRelError": zero_dev,
        "phantomCrossingMaxRelError": cross_dev,
        "decelerationRootMaxRelError": qroot_dev,
        "w0MaxDeviation": w0_dev,
        "waSummaryMaxRelDeviation": wa_dev,
        "waFiniteDifferenceMaxRelDeviation": wa_fd_dev,
        "summaryMaxDeviation": summary_dev,
    })
    return checks, measurements, summary, runs


def compare_repeat(root, repeat_root, summary):
    for name in summary["files"]:
        right = os.path.join(repeat_root, EXPERIMENT, name)
        if not os.path.exists(right):
            return False
        with open(os.path.join(root, EXPERIMENT, name), "rb") as a, open(right, "rb") as b:
            if a.read() != b.read():
                return False
    return True


def reference_errors(run):
    """Max spinor and time errors of one Run against the quadrature references."""
    m = run.model
    u0 = run.u[run.i0]
    err_u = err_t = 0.0
    for idx, _ in run.branches():
        order = idx if run.n[idx][0] == 0.0 else idx[::-1]
        nodes = run.n[order]
        phi = cumulative_quadrature(lambda x: m.omega(x), nodes)
        t_ref = cumulative_quadrature(lambda x: 1.0 / np.sqrt(m.e2(x)), nodes)
        u_ref = np.exp(-1j * phi)[:, None] * u0[None, :]
        err_u = max(err_u, float(np.max(np.linalg.norm(run.u[order] - u_ref, axis=1))))
        err_t = max(err_t, float(np.max(np.abs(run.t[order] - t_ref))))
    return err_u, err_t


def refined_convergence(root, refined_root, summary, runs, fixture_path):
    with open(os.path.join(refined_root, EXPERIMENT, "summary.json"), "r", encoding="utf-8") as h:
        refined = json.load(h)
    ok = refined["refined"] is True and refined["verdict"] == "SUCCESS"
    ok &= abs(refined["tolerances"]["rtol"] - summary["tolerances"]["rtol"] / 10.0) <= 1e-30
    gammas = load_gammas(fixture_path)
    worst_c = worst_r = worst_diff = worst_sigma_c = worst_sigma_r = 0.0
    improved = True
    for run, meta in zip(runs, summary["runs"]):
        fine = Run(os.path.join(refined_root, EXPERIMENT), meta, gammas)
        err_c, _ = reference_errors(run)
        err_r, _ = reference_errors(fine)
        sig_c = float(np.max(np.abs(run.sigma / run.a3 - 1.0)))
        sig_r = float(np.max(np.abs(fine.sigma / fine.a3 - 1.0)))
        improved &= err_r < err_c and sig_r < sig_c
        worst_c, worst_r = max(worst_c, err_c), max(worst_r, err_r)
        worst_sigma_c, worst_sigma_r = max(worst_sigma_c, sig_c), max(worst_sigma_r, sig_r)
        ok &= np.array_equal(run.n, fine.n)
        worst_diff = max(worst_diff, float(np.max(np.linalg.norm(run.u - fine.u, axis=1))))
    ok &= improved and worst_diff <= 2.0 * worst_c
    return ok, worst_diff, worst_c, worst_r, worst_sigma_c, worst_sigma_r


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=DEFAULT_ROOT)
    parser.add_argument("--fixture", default=DEFAULT_FIXTURE)
    parser.add_argument("--binary", default=DEFAULT_BINARY)
    parser.add_argument("--repeat")
    parser.add_argument("--refined")
    arguments = parser.parse_args(argv)
    root = os.path.abspath(arguments.output)
    checks, measurements, summary, runs = verify(root, arguments.fixture)
    if arguments.repeat:
        ran = run_binary(arguments.binary, [EXPERIMENT, "--output", os.path.abspath(arguments.repeat)])
        checks["repeatByteIdentity"] = ran and compare_repeat(root, os.path.abspath(arguments.repeat),
                                                              summary)
    if arguments.refined:
        refined_root = os.path.abspath(arguments.refined)
        ran = run_binary(arguments.binary, [EXPERIMENT, "--refined", "--output", refined_root])
        result = (False,) + (float("nan"),) * 5
        if ran:
            result = refined_convergence(root, refined_root, summary, runs, arguments.fixture)
        checks["refinedConvergence"] = result[0]
        measurements["refinedMaxSpinorDifference"] = result[1]
        measurements["canonicalMaxSpinorError"] = result[2]
        measurements["refinedMaxSpinorError"] = result[3]
        measurements["canonicalMaxSigmaDeviation"] = result[4]
        measurements["refinedMaxSigmaDeviation"] = result[5]
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
        "checker": "scripts/check_dirac16complex_exp3.py",
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
