"""Revision Kohn-Sham REFERENCE solver: staggered finite differences in the hidden coordinate y.

Independent of the Rust solver (Revision/kohn_sham/solver): no code is shared and the discretisation is
different (global symmetric tridiagonal matrices instead of shooting with RK4).  Only the formulas of
Revision/kohn_sham/ks-theory.json are used.

Coordinates as the author names them: x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time;
x5, x6, x7 = the three EXTRA TIMES, which DEFLATE EXPONENTIALLY (scale factor e^{-a4} sin^{1/6} z, a4
increasing); x8 = hidden direction, y = ln(sin z)/(6H) in [-L, 0] (brane y = 0, tip cutoff y = -L).

Block equation (ks-theory.json blockEquation): h_j = j[-i sigma1 d_y + M sigma2 + K sigma3] + v,
K = kappa(y) |k|, kappa = e^{-Hy - a4,0}.  With chi = (a, i b) (a, b real) h_j is the real symmetric
operator
    [ jK + v        j(d_y + M) ]
    [ j(-d_y + M)   -jK + v    ]      acting on (a, b), inner product int (a^2 + b^2) dy.
Boundary conditions: regular tip b(-L) = 0 (theta_tip = 0); ASSUMED Z2 brane: even b(0) = 0, odd a(0) = 0.

Rotated frame (exact, makes both parities Dirichlet in the second component at both ends):
chi = e^{i phi(y) sigma1} psi, psi = (u, i w), i.e. a = cos(phi) u - sin(phi) w, b = sin(phi) u + cos(phi) w.
Then h' = j[-i sigma1 d_y + phi' + m2 sigma2 + k2 sigma3] + v with m2 = M cos 2phi - K sin 2phi,
k2 = M sin 2phi + K cos 2phi.  even parity: phi = 0; odd parity: phi = j (pi/2)(y + L)/L, so that
w(-L) = 0 <=> b(-L) = 0 and w(0) = 0 <=> a(0) = 0.  The choice phi_j = j phi keeps the exact k = 0
symmetry j -> -j as the sign flip w -> -w of the discrete problem.

Discretisation: G cells of width h = L/G; u at the half nodes y_{p+1/2}, w at the interior nodes y_i
(w_0 = w_G = 0).  Interleaved unknowns (u_{1/2}, w_1, u_{3/2}, ..., u_{G-1/2}) give a real symmetric
TRIDIAGONAL matrix of size n = 2G - 1 with centred second-order differences and averages; its errors
have an expansion in even powers of h (verified numerically by the reference report), so results on
G, 2G, 4G are combined by Richardson extrapolation.

Eigenvalues: Sturm counts (number of eigenvalues below x) + bisection give every level by its index in
the sector (no level can be missed); refinement and eigenvectors by the twisted factorisation
(Rayleigh-quotient steps), verified by Sturm counts.  The Sturm index minus the index of the lowest
particle level (CONVENTION of ks-theory.json: positive lambda = 0 levels plus the k = 0 brane zero modes)
is the rank of a level in its sector; it equals the Rust solver's label - label_min.
"""

from __future__ import annotations

import math

import numpy as np

PI = math.pi
TAU_ZERO = 1e-9          # zero-mode threshold of the particle convention (k = 0 brane zero modes at eps = 0)
PIVMIN = 1e-290           # replacement of an exact zero pivot in the Sturm / twisted recurrences
DEG_TOL = 1e-9            # degeneracy groups for the aufbau and HOMO/LUMO

def _extrap_weights(npts):
    """Lagrange weights extrapolating to x = 0 from x = 1/2, 3/2, ..., npts - 1/2 (units of h)."""
    x = np.arange(npts) + 0.5
    w = np.ones(npts)
    for i in range(npts):
        for k in range(npts):
            if k != i:
                w[i] *= (0.0 - x[k]) / (x[i] - x[k])
    return w


EXTRAP = _extrap_weights(6)   # quintic extrapolation of u to the tip / brane (error O(h^6))

SECTOR_ORDER = ((1, 0), (1, 1), (-1, 0), (-1, 1))      # (j, odd): (+1 even), (+1 odd), (-1 even), (-1 odd)


# ------------------------------------------------------------------------------------------------
# physics and grid
# ------------------------------------------------------------------------------------------------
class Phys:
    """Physical parameters (units H = 1, m = 1 canonical)."""

    def __init__(self, H=1.0, m=1.0, L=3.0, dk=0.25, vt=1.0, a4=0.0, lam=0.0, N=8.0, T=0.0,
                 cM=15.0 / 16.0, cV=-1.0 / 16.0, cS2=15.0 / 32.0, cN2=-1.0 / 32.0):
        self.H, self.m, self.L, self.dk, self.vt = H, m, L, dk, vt
        self.a4, self.lam, self.N, self.T = a4, lam, N, T
        # functional coefficients (ks-theory.json exchange.kohnShamPotentials): M_eff = m + cM lam S,
        # v_v = cV lam n, e_int = lam (cS2 S^2 + cN2 n^2)
        self.cM, self.cV, self.cS2, self.cN2 = cM, cV, cS2, cN2

    def copy(self, **kw):
        p = Phys(self.H, self.m, self.L, self.dk, self.vt, self.a4, self.lam, self.N, self.T,
                 self.cM, self.cV, self.cS2, self.cN2)
        for k, v in kw.items():
            setattr(p, k, v)
        return p

    @property
    def ell(self):
        return 2.0 * PI / self.dk

    @property
    def vol7(self):
        return self.ell ** 3 * self.vt


class Grid:
    def __init__(self, phys: Phys, G: int):
        L, H = phys.L, phys.H
        self.G = G
        self.h = L / G
        self.n = 2 * G - 1
        k = np.arange(self.n)
        self.y = -L + (k + 1) * self.h / 2.0              # interior positions (u at even k, w at odd k)
        self.is_u = (k % 2 == 0)
        self.yext = -L + np.arange(self.n + 2) * self.h / 2.0   # with the ends: ext index e = k + 1
        self.e6 = np.exp(6.0 * H * self.y)
        self.e6ext = np.exp(6.0 * H * self.yext)
        self.phi0 = 0.5 * PI * (self.y + L) / L
        phi0e = 0.5 * PI * (self.yext + L) / L
        self.cos0e = np.cos(phi0e)
        self.sin0e = np.sin(phi0e)
        self.cos0e[0], self.sin0e[0] = 1.0, 0.0
        self.cos0e[-1], self.sin0e[-1] = 0.0, 1.0          # phi0 = pi/2 exactly at the brane
        kk = np.arange(self.n - 1)
        self.bu = np.where(kk % 2 == 0, kk, kk + 1)       # u index of the coupling k <-> k+1
        self.bs = np.where(kk % 2 == 0, 1.0, -1.0) / self.h
        self.uidx = np.arange(0, self.n, 2)                # u positions (half nodes), midpoint rule
        self.ext_u = self.uidx + 1                         # their ext indices

    def midpoint(self, f_ext):
        """int_{-L}^{0} f dy by the midpoint rule on the half nodes (f given on the ext grid)."""
        return self.h * float(np.sum(f_ext[self.ext_u]))

    def report_indices(self, npts=151):
        """ext indices of y = -L + i L/(npts-1), i = 0..npts-1 (requires G divisible by (npts-1)/2)."""
        step = 2 * self.G // (npts - 1)
        assert step * (npts - 1) == 2 * self.G
        return np.arange(npts) * step


# ------------------------------------------------------------------------------------------------
# lattice of 3-space momenta
# ------------------------------------------------------------------------------------------------
_R3_CACHE: dict = {}


def shells(n2max: int):
    """[(n2, r3)] for every n2 <= n2max with r3(n2) > 0 (lattice points of Z^3 on the sphere n2)."""
    if n2max in _R3_CACHE:
        return _R3_CACHE[n2max]
    R = int(math.isqrt(n2max)) + 1
    a = np.arange(-R, R + 1)
    s = (a[:, None, None] ** 2 + a[None, :, None] ** 2 + a[None, None, :] ** 2).ravel()
    s = s[s <= n2max]
    cnt = np.bincount(s, minlength=n2max + 1)
    out = [(int(i), int(c)) for i, c in enumerate(cnt) if c > 0]
    _R3_CACHE[n2max] = out
    return out


class Sectors:
    """A list of sectors (n2, r3, j, odd) with |k| = dk sqrt(n2)."""

    def __init__(self, items):
        self.items = list(items)
        self.n2 = np.array([s[0] for s in self.items], dtype=np.int64)
        self.r3 = np.array([s[1] for s in self.items], dtype=np.int64)
        self.j = np.array([s[2] for s in self.items], dtype=float)
        self.odd = np.array([s[3] for s in self.items], dtype=bool)

    def __len__(self):
        return len(self.items)

    def kmag(self, dk):
        return dk * np.sqrt(self.n2.astype(float))

    def deg(self):
        return 4.0 * self.r3.astype(float)

    def subset(self, idx):
        return Sectors([self.items[int(i)] for i in idx])


def shell_sectors(shell_list):
    return Sectors([(n2, r3, j, odd) for (n2, r3) in shell_list for (j, odd) in SECTOR_ORDER])


def sector_arrays(grid: Grid, phys: Phys, sec: Sectors, M, v, a4=None):
    """Diagonal alpha (n, S) and off-diagonal beta (n-1, S) of every sector matrix.
    M, v: potentials at the n interior positions."""
    a4 = phys.a4 if a4 is None else a4
    kap = np.exp(-phys.H * grid.y - a4)
    K = kap[:, None] * sec.kmag(phys.dk)[None, :]
    j = sec.j[None, :]
    phi = np.where(sec.odd[None, :], j * grid.phi0[:, None], 0.0)
    c2 = np.where(sec.odd[None, :], np.cos(2.0 * phi), 1.0)
    s2 = np.where(sec.odd[None, :], np.sin(2.0 * phi), 0.0)
    dphi = np.where(sec.odd, sec.j * PI / (2.0 * phys.L), 0.0)[None, :]
    m2 = M[:, None] * c2 - K * s2
    k2 = M[:, None] * s2 + K * c2
    alpha = np.where(grid.is_u[:, None], j * (dphi + k2), j * (dphi - k2)) + v[:, None]
    beta = j * (grid.bs[:, None] + 0.5 * m2[grid.bu, :])
    return alpha, beta


def sector_derivative_arrays(grid: Grid, phys: Phys, sec: Sectors, dM, dv):
    """d alpha / d a4 and d beta / d a4: frozen part (dK/da4 = -K) plus the self-consistent part dM, dv."""
    kap = np.exp(-phys.H * grid.y - phys.a4)
    K = kap[:, None] * sec.kmag(phys.dk)[None, :]
    j = sec.j[None, :]
    phi = np.where(sec.odd[None, :], j * grid.phi0[:, None], 0.0)
    c2 = np.where(sec.odd[None, :], np.cos(2.0 * phi), 1.0)
    s2 = np.where(sec.odd[None, :], np.sin(2.0 * phi), 0.0)
    dm2 = dM[:, None] * c2 + K * s2
    dk2 = dM[:, None] * s2 - K * c2
    dalpha = np.where(grid.is_u[:, None], j * dk2, -j * dk2) + dv[:, None]
    dbeta = j * 0.5 * dm2[grid.bu, :]
    return dalpha, dbeta


# ------------------------------------------------------------------------------------------------
# tridiagonal eigen-solver (vectorised over a batch of matrices)
# ------------------------------------------------------------------------------------------------
def sturm_count(aT, b2T, x):
    """Number of eigenvalues < x of each batch matrix (aT: (n, B) diagonals, b2T: (n-1, B) squared
    off-diagonals, x: (B,))."""
    n = aT.shape[0]
    q = aT[0] - x
    q = np.where(np.abs(q) < PIVMIN, -PIVMIN, q)
    cnt = (q < 0).astype(np.int64)
    for i in range(1, n):
        q = aT[i] - x - b2T[i - 1] / q
        q = np.where(np.abs(q) < PIVMIN, -PIVMIN, q)
        cnt += q < 0
    return cnt


def gershgorin(aT, bT):
    ab = np.abs(bT)
    rad = np.zeros_like(aT)
    rad[:-1] += ab
    rad[1:] += ab
    return (aT - rad).min(axis=0) - 1.0, (aT + rad).max(axis=0) + 1.0


def bisect(aT, b2T, idx, lo, hi, tol):
    """Bisection for eigenvalue number idx (0-based, ascending); requires count(lo) <= idx < count(hi)."""
    lo = lo.copy()
    hi = hi.copy()
    while np.any(hi - lo > tol):
        mid = 0.5 * (lo + hi)
        c = sturm_count(aT, b2T, mid)
        up = c <= idx
        lo = np.where(up, mid, lo)
        hi = np.where(up, hi, mid)
    return lo, hi


def twisted(aT, bT, b2T, sigma):
    """Twisted factorisation of T - sigma: eigenvector estimate z (Euclidean norm 1) and the Rayleigh
    quotient sigma + gamma_r / |z|^2 (one Rayleigh-quotient step)."""
    n, B = aT.shape
    a = aT - sigma
    Dp = np.empty_like(a)
    Dm = np.empty_like(a)
    d = a[0]
    d = np.where(np.abs(d) < PIVMIN, -PIVMIN, d)
    Dp[0] = d
    for i in range(1, n):
        d = a[i] - b2T[i - 1] / d
        d = np.where(np.abs(d) < PIVMIN, -PIVMIN, d)
        Dp[i] = d
    d = a[n - 1]
    d = np.where(np.abs(d) < PIVMIN, -PIVMIN, d)
    Dm[n - 1] = d
    for i in range(n - 2, -1, -1):
        d = a[i] - b2T[i] / d
        d = np.where(np.abs(d) < PIVMIN, -PIVMIN, d)
        Dm[i] = d
    gam = Dp + Dm - a
    r = np.argmin(np.abs(gam), axis=0)
    cols = np.arange(B)
    gr = gam[r, cols]
    z = np.zeros_like(a)
    z[r, cols] = 1.0
    for i in range(n - 2, -1, -1):
        z[i] = np.where(i < r, -bT[i] * z[i + 1] / Dp[i], z[i])
    for i in range(1, n):
        z[i] = np.where(i > r, -bT[i - 1] * z[i - 1] / Dm[i], z[i])
    nrm2 = np.einsum("ij,ij->j", z, z)
    lam = sigma + gr / nrm2
    return lam, z / np.sqrt(nrm2)


def eigen(aT, bT, idx, guess=None, rqi_steps=3, verify_eps=1e-9):
    """Eigenvalue number idx (and the normalised eigenvector) of every batch matrix.
    With a guess: Rayleigh-quotient iteration from the guess, verified by Sturm counts; elements that
    fail the verification (or without a guess) are bracketed globally and bisected first."""
    b2T = bT * bT
    B = aT.shape[1]
    lam = np.empty(B)
    Z = np.empty_like(aT)
    todo = np.ones(B, dtype=bool)
    if guess is not None:
        s = np.array(guess, dtype=float)
        for _ in range(rqi_steps):
            s, z = twisted(aT, bT, b2T, s)
        ok = (sturm_count(aT, b2T, s - verify_eps) == idx) & (sturm_count(aT, b2T, s + verify_eps) == idx + 1)
        lam[ok] = s[ok]
        Z[:, ok] = z[:, ok]
        todo = ~ok
    if np.any(todo):
        sel = np.nonzero(todo)[0]
        a2, b2, bb2 = aT[:, sel], bT[:, sel], b2T[:, sel]
        lo, hi = gershgorin(a2, b2)
        lo, hi = bisect(a2, bb2, idx[sel], lo, hi, 1e-9)
        s = 0.5 * (lo + hi)
        for _ in range(2):
            s1, z = twisted(a2, b2, bb2, s)
            # keep the Rayleigh quotient only inside the bisection bracket (safety)
            s = np.where((s1 >= lo - 1e-12) & (s1 <= hi + 1e-12), s1, s)
        ok = (sturm_count(a2, bb2, s - verify_eps) == idx[sel]) & (sturm_count(a2, bb2, s + verify_eps) == idx[sel] + 1)
        if not np.all(ok):
            raise RuntimeError(f"eigen: {int(np.sum(~ok))} levels failed the Sturm verification after bisection")
        lam[sel] = s
        Z[:, sel] = z
    return lam, Z


# ------------------------------------------------------------------------------------------------
# orbitals on the ext grid and densities
# ------------------------------------------------------------------------------------------------
def orbitals_ext(grid: Grid, Z, j, odd):
    """(a, b) of the orbitals on the ext grid (n + 2 points incl. the tip and the brane), normalised
    int (a^2 + b^2) dy = 1 in the discrete staggered norm.  Z: (n, B) Euclidean-normalised eigenvectors."""
    n = grid.n
    zp = Z / math.sqrt(grid.h)
    B = Z.shape[1]
    U = np.empty((n + 2, B))
    W = np.zeros((n + 2, B))
    U[1:n + 1:2] = zp[0::2]                                   # half nodes
    U[2:n + 1:2] = 0.5 * (zp[0:n - 1:2] + zp[2::2])           # interior nodes: average
    U[0] = EXTRAP @ zp[0:11:2]                                # tip (half nodes 1/2 ... 11/2)
    U[n + 1] = EXTRAP @ zp[n - 1:n - 12:-2]                   # brane
    W[2:n + 1:2] = zp[1::2]                                   # interior nodes
    zpad = np.zeros((n + 2, B))
    zpad[1:n + 1] = zp
    W[1:n + 1:2] = 0.5 * (zpad[0:n:2] + zpad[2:n + 2:2])      # half nodes: average (w_0 = w_G = 0)
    c = np.where(odd[None, :], grid.cos0e[:, None], 1.0)
    s = np.where(odd[None, :], j[None, :] * grid.sin0e[:, None], 0.0)
    a = c * U - s * W
    b = s * U + c * W
    return a, b


class Dens:
    """Proper densities (per proper 7-volume) on the ext grid."""

    def __init__(self, grid: Grid, phys: Phys, a, b, wgf, j, kmag, eps):
        P = np.exp(-6.0 * phys.H * grid.yext) / phys.vol7
        kap = np.exp(-phys.H * grid.yext - phys.a4)
        nn = a * a + b * b
        qq = a * a - b * b
        ss = 2.0 * a * b
        self.n = P * (nn @ wgf)
        self.S = P * (ss @ (wgf * j))
        self.Q = P * (qq @ wgf)
        self.tk = P * kap * (qq @ (wgf * j * kmag))           # sum w g f kappa |k| t_o
        self.k4 = P * (nn @ (wgf * eps))                      # sum w g f eps n_o
        self.P = P
        self.kap = kap


# ------------------------------------------------------------------------------------------------
# occupations
# ------------------------------------------------------------------------------------------------
def groups(eps, order_key):
    """Degenerate groups (sorted by energy, ties by order_key): list of index arrays."""
    order = np.lexsort((order_key, eps))
    out = []
    cur = [order[0]]
    e0 = eps[order[0]]
    for i in order[1:]:
        if eps[i] - e0 <= DEG_TOL:
            cur.append(i)
        else:
            out.append(np.array(cur))
            cur = [i]
            e0 = eps[i]
    out.append(np.array(cur))
    return out


def aufbau(eps, deg, order_key, N):
    f = np.zeros_like(eps)
    left = N
    open_shell = False
    for g in groups(eps, order_key):
        if left <= 1e-12:
            break
        gs = float(np.sum(deg[g]))
        fill = 1.0 if gs <= left + 1e-9 else left / gs
        if fill < 1.0:
            open_shell = True
        f[g] = fill
        left -= fill * gs
        if abs(left) < 1e-9:
            left = 0.0
    if left > 0.0:
        raise RuntimeError(f"aufbau: window holds too few particle states (missing {left})")
    return f, open_shell


def fermi(x):
    ex = np.exp(-np.abs(x))
    return np.where(x > 0, ex / (1.0 + ex), 1.0 / (1.0 + ex))


def mermin(eps, deg, N, T):
    lo = float(eps.min()) - 60.0 * T - 1.0
    hi = float(eps.max()) + 60.0 * T + 1.0
    if float(np.sum(deg)) <= N:
        raise RuntimeError("mermin: window too small")
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if mid <= lo or mid >= hi:
            break
        if float(np.sum(deg * fermi((eps - mid) / T))) < N:
            lo = mid
        else:
            hi = mid
    mu = 0.5 * (lo + hi)
    return fermi((eps - mu) / T), mu


def mermin_sums(eps, deg, mu, T):
    x = (eps - mu) / T
    ax = np.abs(x)
    entropy = float(np.sum(deg * (np.log1p(np.exp(-ax)) + ax * fermi(ax))))
    lg = np.where(x > 0, np.log1p(np.exp(-np.abs(x))), -x + np.log1p(np.exp(-np.abs(x))))
    return entropy, float(np.sum(deg * lg))


# ------------------------------------------------------------------------------------------------
# a Kohn-Sham state on one grid
# ------------------------------------------------------------------------------------------------
class LevelSet:
    """The label set of a run: sectors and, per level, (sector index, Sturm index, rank)."""

    def __init__(self, sec: Sectors, lev_sec, lev_idx, lev_rank, imin):
        self.sec = sec
        self.lev_sec = np.asarray(lev_sec, dtype=np.int64)
        self.lev_idx = np.asarray(lev_idx, dtype=np.int64)
        self.lev_rank = np.asarray(lev_rank, dtype=np.int64)
        self.imin = np.asarray(imin, dtype=np.int64)       # per sector
        self.deg = sec.deg()[self.lev_sec]
        self.j = sec.j[self.lev_sec]
        self.odd = sec.odd[self.lev_sec]
        self.n2 = sec.n2[self.lev_sec]

    def keys(self):
        return [(int(self.n2[i]), int(self.j[i]), "odd" if self.odd[i] else "even", int(self.lev_rank[i]))
                for i in range(len(self.lev_sec))]

    def order_key(self):
        # sort key for ties: (n2, j descending, parity, rank) as an integer
        return ((self.n2 * 2 + (self.j < 0)) * 2 + self.odd) * 1000 + self.lev_rank


class Anderson:
    def __init__(self, depth=8, beta=0.5):
        self.depth, self.beta = depth, beta
        self.X, self.R = [], []

    def step(self, x, r):
        self.X.append(x.copy())
        self.R.append(r.copy())
        if len(self.X) > self.depth + 1:
            self.X.pop(0)
            self.R.pop(0)
        if len(self.X) == 1:
            return x + self.beta * r
        dX = np.array([self.X[i + 1] - self.X[i] for i in range(len(self.X) - 1)]).T
        dR = np.array([self.R[i + 1] - self.R[i] for i in range(len(self.R) - 1)]).T
        g, *_ = np.linalg.lstsq(dR, r, rcond=1e-12)
        return (x - dX @ g) + self.beta * (r - dR @ g)

    def reset(self):
        self.X, self.R = [], []


class State:
    pass


def solve_state(grid: Grid, phys: Phys, ls: LevelSet, mode="aufbau", fixed=None, start=None, guess=None,
                tol=1e-12, maxit=400):
    """Self-consistent Kohn-Sham state on one grid.  mode: 'aufbau' (T = 0), 'fixed' (occupations given
    per level, e.g. Delta-SCF or a4 +- delta), 'mermin' (T > 0).  Potentials (dM, v) at the n interior
    positions are mixed (Anderson); converged when max |output - input| <= tol (units of m)."""
    n = grid.n
    x = np.zeros(2 * n) if (start is None or phys.lam == 0.0) else np.concatenate([start[0], start[1]])
    mix = Anderson()
    lev_j, lev_odd, deg = ls.j, ls.odd, ls.deg
    kmag_l = ls.sec.kmag(phys.dk)[ls.lev_sec]
    okey = ls.order_key()
    used, inv = np.unique(ls.lev_sec, return_inverse=True)
    sec_u = ls.sec.subset(used)
    best = np.inf
    hist = []
    eps_prev = guess
    for it in range(1, maxit + 1):
        dM, v = x[:n], x[n:]
        alpha, beta = sector_arrays(grid, phys, sec_u, phys.m + dM, v)
        aT = alpha[:, inv]
        bT = beta[:, inv]
        del alpha, beta
        eps, Z = eigen(aT, bT, ls.lev_idx, guess=eps_prev)
        eps_prev = eps
        mu = float("nan")
        open_shell = False
        if mode == "aufbau":
            f, open_shell = aufbau(eps, deg, okey, phys.N)
        elif mode == "fixed":
            f = np.asarray(fixed, dtype=float)
        elif mode == "mermin":
            f, mu = mermin(eps, deg, phys.N, phys.T)
        else:
            raise ValueError(mode)
        wgf = 0.5 * deg * f
        occ = wgf > 0.0
        a, b = orbitals_ext(grid, Z[:, occ], lev_j[occ], lev_odd[occ])
        dens = Dens(grid, phys, a, b, wgf[occ], lev_j[occ], kmag_l[occ], eps[occ])
        xo = np.concatenate([phys.lam * phys.cM * dens.S[1:n + 1], phys.lam * phys.cV * dens.n[1:n + 1]])
        r = xo - x
        res = float(np.max(np.abs(r))) if phys.lam != 0.0 else 0.0
        hist.append(res)
        if res <= tol or phys.lam == 0.0:
            st = State()
            st.grid, st.phys, st.ls = grid, phys, ls
            st.eps, st.Z, st.f, st.mu, st.open_shell = eps, Z, f, mu, open_shell
            st.dM, st.v = dM.copy(), v.copy()
            st.dens, st.a, st.b, st.occ = dens, a, b, occ
            st.iters, st.res, st.hist = it, res, hist
            st.kmag_l = kmag_l
            st.sec_u, st.inv = sec_u, inv
            return st
        best = min(best, res)
        if it > 60 and res > 1e3 * best:
            raise RuntimeError(f"SCF diverging (iteration {it}, residual {res:.3e}, best {best:.3e})")
        if res > 10.0 * best:
            mix.reset()
        x = mix.step(x, r)
    raise RuntimeError(f"SCF not converged in {maxit} iterations (residual {hist[-1]:.3e})")


def observables(st: State):
    """Energies, EMT profiles and integrals of a converged state (ks-theory.json thermodynamics, emt)."""
    g, ph, d = st.grid, st.phys, st.dens
    lam = ph.lam
    eint = lam * (ph.cS2 * d.S ** 2 + ph.cN2 * d.n ** 2)
    Mx = ph.m + ph.cM * lam * d.S          # M_eff from the output densities (ext grid incl. the ends)
    vx = ph.cV * lam * d.n
    # p8 bracket: sum w g f [(eps - v) n_o - M s_o - kappa |k| t_o] = k4 - v n - M S - tk
    rho = d.k4 - eint
    p3 = d.tk / 3.0 + eint
    pt = eint.copy()
    p8 = d.k4 - vx * d.n - Mx * d.S - d.tk + eint
    vol2 = 2.0 * ph.vol7
    e6 = g.e6ext
    I = lambda f: vol2 * g.midpoint(e6 * f)
    o = {}
    o["E_band"] = float(np.sum(st.ls.deg * st.f * st.eps))
    o["E_int"] = I(eint)
    o["E_KS"] = o["E_band"] - o["E_int"]
    o["E_variational"] = o["E_band"] - vol2 * g.midpoint(e6 * (st_pot_ext(st, "dM") * d.S + st_pot_ext(st, "v") * d.n)) + o["E_int"]
    o["int_rho"] = I(rho)
    o["int_p3"] = I(p3)
    o["int_p_t"] = I(pt)
    o["int_p8"] = I(p8)
    o["int_n"] = I(d.n)
    o["dE_da4_emt"] = -vol2 * g.midpoint(e6 * d.tk)
    o["deltaE_x_exact_fock"] = lam / 32.0 * I(d.Q ** 2)
    # y-conservation (nabla_mu T^mu_y = 0): [e^{6Hy} p8]_{-L}^{0} = 3H int e^{6Hy}(p3 + p_t) dy
    o["ycons_jump"] = float(e6[-1] * p8[-1] - e6[0] * p8[0])
    o["ycons_integral"] = 3.0 * ph.H * g.midpoint(e6 * (p3 + pt))
    for nm, arr in (("rho", rho), ("p3", p3), ("p_t", pt), ("p8", p8)):
        o[nm + "_brane"] = float(arr[-1])
        o[nm + "_tip"] = float(arr[0])
    o["N_sum"] = float(np.sum(st.ls.deg * st.f))
    prof = {"n": d.n, "S": d.S, "Q": d.Q, "M_eff": Mx, "v_v": vx, "e_int": eint, "rho": rho, "p3": p3,
            "p_t": pt, "p8": p8}
    return o, prof


def st_pot_ext(st: State, which):
    """Input potentials of the last iteration on the ext grid (ends: nearest interior value; they enter
    only the variational energy form through the midpoint rule, which never uses the ends)."""
    x = st.dM if which == "dM" else st.v
    return np.concatenate([[x[0]], x, [x[-1]]])


def homo_lumo(st: State):
    grs = groups(st.eps, st.ls.order_key())
    homo = -np.inf
    hg = None
    for gidx in grs:
        if np.any(st.f[gidx] > 1e-12):
            e = float(st.eps[gidx[0]])
            if e > homo:
                homo, hg = e, gidx
    lumo = np.inf
    lg = None
    for gidx in grs:
        e = float(st.eps[gidx[0]])
        if e > homo and np.any(st.f[gidx] < 1.0 - 1e-12) and e < lumo:
            lumo, lg = e, gidx
    return homo, lumo, hg, lg


def matrix_elements(st: State, dalpha_sec, dbeta_sec, pairs):
    """<n| d_a h |m> = z_n^T dT z_m for (n, m) level index pairs of the same sector
    (dalpha_sec, dbeta_sec: derivative arrays of the sectors st.sec_u, see sector_derivative_arrays)."""
    Z = st.Z
    out = []
    for (p, q) in pairs:
        s = st.inv[p]
        da, db = dalpha_sec[:, s], dbeta_sec[:, s]
        zn, zm = Z[:, p], Z[:, q]
        out.append(float(np.dot(zn * da, zm) + np.dot(db, zn[:-1] * zm[1:] + zn[1:] * zm[:-1])))
    return np.array(out)


# ------------------------------------------------------------------------------------------------
# label sets (windows)
# ------------------------------------------------------------------------------------------------
def particle_offsets(grid: Grid, phys: Phys, sec: Sectors):
    """Sturm index of the lowest particle level of every sector (free problem lambda = 0 at the same
    slice): the number of free eigenvalues below -TAU_ZERO (the k = 0 brane zero modes at eps = 0 are
    particles by the convention)."""
    n = grid.n
    alpha, beta = sector_arrays(grid, phys, sec, np.full(n, phys.m), np.zeros(n))
    return sturm_count(alpha, beta * beta, np.full(len(sec), -TAU_ZERO)), alpha, beta


def free_levels_below(grid, phys, sec: Sectors, imin, ecut, alpha, beta, extra_ranks=None):
    """Free particle levels with eps < ecut of every sector (and ranks <= extra_ranks[s] where given)."""
    cnt = sturm_count(alpha, beta * beta, np.full(len(sec), float(ecut)))
    ls_sec, ls_idx, ls_rank = [], [], []
    for s in range(len(sec)):
        nr = int(cnt[s] - imin[s])
        if extra_ranks is not None:
            nr = max(nr, int(extra_ranks[s]) + 1)
        for r in range(nr):
            ls_sec.append(s)
            ls_idx.append(int(imin[s]) + r)
            ls_rank.append(r)
    return ls_sec, ls_idx, ls_rank


class ShellScan:
    """Free (lambda = 0) data of the shells n2 = 0, 1, 2, ... at one slice on one grid, computed lazily:
    the particle offsets and the lowest particle level of each of the four sectors."""

    def __init__(self, grid: Grid, phys: Phys, chunk=48):
        self.grid, self.phys, self.chunk = grid, phys.copy(lam=0.0), chunk
        self.all = shells(4096)
        self.sh, self.imin, self.low = [], [], []

    def ensure(self, count):
        while len(self.sh) < count:
            new = self.all[len(self.sh):len(self.sh) + self.chunk]
            if not new:
                raise RuntimeError("shell table exhausted")
            sec = shell_sectors(new)
            imin, al, be = particle_offsets(self.grid, self.phys, sec)
            eps, _ = eigen(al, be, imin)
            for i, s in enumerate(new):
                self.sh.append(s)
                self.imin.append(imin[4 * i:4 * i + 4])
                self.low.append(eps[4 * i:4 * i + 4])

    def shells_below(self, e):
        """Index range [0, c) of the shells whose lowest particle level lies below e, extended until the
        five shells after the range all lie above e (guards against a non-monotone shell minimum)."""
        c = 0
        i = 0
        while True:
            self.ensure(i + 6)
            if float(np.min(self.low[i])) < e:
                c = i + 1
            elif i >= c + 5:
                return c
            i += 1


def build_window(grid: Grid, phys: Phys, sigma: float, scan: ShellScan = None, pad_ranks=2):
    """Label set of a run from the free (lambda = 0) problem at the same slice (computed on `grid`):
    T = 0: every particle level with free eps < max(E_F, LUMO) + 0.25 + 2 sigma, plus the ranks
    0..pad_ranks of every sector of an occupied shell (the pairs of the adiabaticity measure);
    T > 0: every particle level with free eps < mu + T ln(1e13) + 0.2 + 2 sigma (Mermin at T).
    sigma = the calibrated first-order mean-field potential (0, 0.1 or 0.3 m).  Returns
    (LevelSet, info)."""
    scan = scan or ShellScan(grid, phys)
    N, T = phys.N, phys.T
    Ec = 0.5
    while True:
        c = scan.shells_below(Ec)
        sl = scan.sh[:c]
        sec = shell_sectors(sl)
        imin, al, be = particle_offsets(grid, phys.copy(lam=0.0), sec)
        ls_sec, ls_idx, ls_rank = free_levels_below(grid, phys, sec, imin, Ec, al, be)
        degs = sec.deg()[np.array(ls_sec, dtype=np.int64)] if ls_sec else np.zeros(0)
        if float(np.sum(degs)) < N + 1.0:
            Ec += 0.5
            continue
        ls_sec = np.array(ls_sec)
        eps, _ = eigen(al[:, ls_sec], be[:, ls_sec], np.array(ls_idx))
        ls = LevelSet(sec, ls_sec, ls_idx, ls_rank, imin)
        if T == 0.0:
            f, _ = aufbau(eps, degs, ls.order_key(), N)
            ef = float(np.max(eps[f > 0]))
            above = eps[eps > ef + DEG_TOL]
            if above.size == 0:
                Ec += 0.5
                continue
            lumo = float(np.min(above))
            need = max(ef, lumo) + 0.25 + 2.0 * sigma
            info = {"E_F_free": ef, "LUMO_free": lumo}
        else:
            f, mu = mermin(eps, degs, N, T)
            need = mu + T * math.log(1e13) + 0.2 + 2.0 * sigma
            info = {"mu_free": mu}
        if need > Ec + 1e-12:
            Ec = need + (0.0 if T == 0.0 else 0.05)
            continue
        break
    # final label set at the cut Ec
    extra = None
    if T == 0.0:
        occ_shells = set(int(ls.n2[i]) for i in range(len(eps)) if f[i] > 0)
        extra = np.array([pad_ranks if int(sec.n2[s]) in occ_shells else -1 for s in range(len(sec))])
    ls_sec, ls_idx, ls_rank = free_levels_below(grid, phys, sec, imin, Ec, al, be, extra_ranks=extra)
    ls = LevelSet(sec, ls_sec, ls_idx, ls_rank, imin)
    info["window_cut"] = Ec
    info["shells"] = c
    return ls, info


def particle_offsets_chunked(grid: Grid, phys: Phys, sec: Sectors, chunk=256):
    out = []
    for c0 in range(0, len(sec), chunk):
        sub = sec.subset(range(c0, min(c0 + chunk, len(sec))))
        im, _, _ = particle_offsets(grid, phys, sub)
        out.append(im)
    return np.concatenate(out) if out else np.zeros(0, dtype=np.int64)


def relabel(grid: Grid, phys: Phys, ls0: LevelSet):
    """The same label set (sectors and ranks) on another grid: recompute the particle offsets."""
    imin = particle_offsets_chunked(grid, phys.copy(lam=0.0), ls0.sec)
    return LevelSet(ls0.sec, ls0.lev_sec, imin[ls0.lev_sec] + ls0.lev_rank, ls0.lev_rank, imin)


def lowest_excluded(grid: Grid, phys: Phys, ls: LevelSet, dM, v, nbeyond=5, chunk=256):
    """Lowest level outside the label set in the given potentials: the next rank of every sector of the
    window shells and the lowest particle level of the next `nbeyond` shells."""
    nsec = len(ls.sec)
    nxt = ls.imin.copy()
    for s in range(nsec):
        sel = ls.lev_idx[ls.lev_sec == s]
        if sel.size:
            nxt[s] = int(sel.max()) + 1
    maxn2 = int(ls.sec.n2.max())
    beyond = [s for s in shells(maxn2 + 400) if s[0] > maxn2][:nbeyond]
    sec_b = shell_sectors(beyond)
    imin_b, _, _ = particle_offsets(grid, phys.copy(lam=0.0), sec_b)
    sec_all = Sectors(ls.sec.items + sec_b.items)
    idx = np.concatenate([nxt, imin_b])
    emin = np.inf
    for c0 in range(0, len(sec_all), chunk):
        sel = np.arange(c0, min(c0 + chunk, len(sec_all)))
        al, be = sector_arrays(grid, phys, sec_all.subset(sel), phys.m + dM, v)
        eps, _ = eigen(al, be, idx[sel])
        emin = min(emin, float(eps.min()))
    return emin
