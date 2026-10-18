#!/usr/bin/env python3
"""UM-2 Kohn-Sham solver for dirac16complex on the x0 cell (independent implementation).

Method: Galerkin in the EXACT eigenbasis of the free block operator (constant mass m, v = 0, k = 0) with the same
boundary conditions.  Real form chi = (a, i b):
    H_real = [[ j K + v,  j (d_y/f + M) ], [ j (-d_y/f + M),  -j K + v ]],   K = kappa |k| (physical momentum)
free eigenfunctions on [-L, 0] (tip b(-L) = 0):
  even fold (b(0) = 0):  zero mode (e^{f m y}, 0), eps = 0;  q_n = n pi/(f L), eps = +-sqrt(m^2 + q_n^2),
                         a = cos(f q y) + (m/q) sin(f q y),  b = j (eps/q) sin(f q y)
  odd fold (a(0) = 0):   tan(p f L) = -p/m, eps = +-sqrt(m^2 + p^2),  a = sin(f p y),  b = j (m sin(f p y) - p cos(f p y))/eps
The Kohn-Sham matrix H_mn = eps_n delta_mn + int [a_m (jK + v) a_n + j dM (a_m b_n + b_m a_n) + b_m (-jK + v) b_n] dy
(dM = M_eff - m) is exact in the complete basis; truncation converges spectrally (checked by doubling the basis).

Kohn-Sham functional (contact interaction U = (lambda/2) S^2, Hartree plus the exact local exchange of the gas):
  M_eff = m + (15/16) lambda S(y) + (portal mean fields),  v = -(1/16) lambda n(y) + (portal mean fields)
  n = sum w g f P (a^2 + b^2),  S = sum w g f P j 2ab,  P = e^{-3Hy}/Vol7,  w = 1/2 (both fold conditions, each
  orbital normalised on one half of the cell), g = 4 r3(n2) per level of h_j(|k|)
  E_KS = sum g f eps - 2 Vol7 int e^{3Hy} e_int dy,  e_int = (15/32) lambda S^2 - (1/32) lambda n^2
Energy-momentum tensor (per point):  rho = sum w g f eps n_o - e_int,  p3 = sum w g f (K/3) t_o + e_int,  p_t = e_int,
  p0 = sum w g f [(eps - v) n_o - M_eff s_o - K t_o] + e_int,  t_o = P j (a^2 - b^2), s_o = P j 2ab, n_o = P (a^2 + b^2).
Particle convention: particle levels are the positive branch of the lambda = 0 problem plus the k = 0 fold zero modes.
"""
import math
import os
import sys
import time

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def r3_table(n2max):
    """r3(n2): number of integer vectors with |n|^2 = n2."""
    r = np.zeros(n2max + 1, dtype=int)
    m = int(math.isqrt(n2max)) + 1
    for i in range(-m, m + 1):
        for j in range(-m, m + 1):
            for k in range(-m, m + 1):
                s = i * i + j * j + k * k
                if s <= n2max:
                    r[s] += 1
    return r


class Cell:
    def __init__(self, f, L, H=1.0, m=1.0, nb=80, nq=800):
        self.f, self.L, self.H, self.m, self.nb, self.nq = f, L, H, m, nb, nq
        xg, wg = np.polynomial.legendre.leggauss(nq)
        self.y = -L / 2 + L / 2 * xg            # on [-L, 0]
        self.wq = wg * L / 2
        self.basis = {}
        for j in (1, -1):
            for parity in ('even', 'odd'):
                self.basis[(j, parity)] = self._build(j, parity)

    def _odd_roots(self, n):
        fL, m = self.f * self.L, self.m
        roots = []
        for k in range(n):
            # tan(p fL) = -p/m has one root in ((k + 1/2) pi, (k + 1) pi)/fL
            lo = ((k + 0.5) * math.pi + 1e-12) / fL
            hi = ((k + 1.0) * math.pi - 1e-12) / fL
            g = lambda p: math.sin(p * fL) * m + p * math.cos(p * fL)
            roots.append(brentq(g, lo, hi, xtol=1e-15, rtol=1e-15, maxiter=200))
        return np.array(roots)

    def _build(self, j, parity):
        f, L, m, y = self.f, self.L, self.m, self.y
        A, B, E = [], [], []
        if parity == 'even':
            A.append(np.exp(f * m * y))
            B.append(np.zeros_like(y))
            E.append(0.0)
            for n in range(1, self.nb + 1):
                q = n * math.pi / (f * L)
                for s in (1, -1):
                    eps = s * math.sqrt(m * m + q * q)
                    A.append(np.cos(f * q * y) + (m / q) * np.sin(f * q * y))
                    B.append(j * (eps / q) * np.sin(f * q * y))
                    E.append(eps)
        else:
            for p in self._odd_roots(self.nb):
                for s in (1, -1):
                    eps = s * math.sqrt(m * m + p * p)
                    A.append(np.sin(f * p * y))
                    B.append(j * (m * np.sin(f * p * y) - p * np.cos(f * p * y)) / eps)
                    E.append(eps)
        A = np.array(A)
        B = np.array(B)
        E = np.array(E)
        nrm = np.sqrt((A ** 2 + B ** 2) @ self.wq)
        A /= nrm[:, None]
        B /= nrm[:, None]
        order = np.argsort(E, kind='stable')
        A, B, E = A[order], B[order], E[order]
        W = self.wq
        Aov = (A * W) @ A.T
        Bov = (B * W) @ B.T
        return {'A': A, 'B': B, 'E': E, 'Aov': Aov, 'Bov': Bov, 'nneg': int(np.sum(E < -1e-12))}

    def eval_at(self, j, parity, yv):
        """Basis functions (normalised, same order as self.basis) at the points yv."""
        f, L, m = self.f, self.L, self.m
        yv = np.atleast_1d(np.asarray(yv, dtype=float))
        A, B, E = [], [], []
        if parity == 'even':
            A.append(np.exp(f * m * yv))
            B.append(np.zeros_like(yv))
            E.append(0.0)
            for n in range(1, self.nb + 1):
                q = n * math.pi / (f * L)
                for s in (1, -1):
                    eps = s * math.sqrt(m * m + q * q)
                    A.append(np.cos(f * q * yv) + (m / q) * np.sin(f * q * yv))
                    B.append(j * (eps / q) * np.sin(f * q * yv))
                    E.append(eps)
        else:
            for p in self._odd_roots(self.nb):
                for s in (1, -1):
                    eps = s * math.sqrt(m * m + p * p)
                    A.append(np.sin(f * p * yv))
                    B.append(j * (m * np.sin(f * p * yv) - p * np.cos(f * p * yv)) / eps)
                    E.append(eps)
        A, B, E = np.array(A), np.array(B), np.array(E)
        # same normalisation and order as the quadrature basis (norms from the unnormalised functions at the nodes)
        Afull, Bfull, Efull = self._raw(j, parity)
        nrm = np.sqrt((Afull ** 2 + Bfull ** 2) @ self.wq)
        order = np.argsort(Efull, kind='stable')
        A = (A / nrm[:, None])[order]
        B = (B / nrm[:, None])[order]
        return A, B

    def _raw(self, j, parity):
        f, L, m, y = self.f, self.L, self.m, self.y
        A, B, E = [], [], []
        if parity == 'even':
            A.append(np.exp(f * m * y)); B.append(np.zeros_like(y)); E.append(0.0)
            for n in range(1, self.nb + 1):
                q = n * math.pi / (f * L)
                for s in (1, -1):
                    eps = s * math.sqrt(m * m + q * q)
                    A.append(np.cos(f * q * y) + (m / q) * np.sin(f * q * y)); B.append(j * (eps / q) * np.sin(f * q * y)); E.append(eps)
        else:
            for p in self._odd_roots(self.nb):
                for s in (1, -1):
                    eps = s * math.sqrt(m * m + p * p)
                    A.append(np.sin(f * p * y)); B.append(j * (m * np.sin(f * p * y) - p * np.cos(f * p * y)) / eps); E.append(eps)
        return np.array(A), np.array(B), np.array(E)

    def orthonormality_error(self):
        err = 0.0
        for key, bs in self.basis.items():
            G = bs['Aov'] + bs['Bov']
            err = max(err, float(np.max(np.abs(G - np.eye(len(G))))))
        return err


class KSState:
    """A Kohn-Sham state of dirac16complex on the cell (static block slice)."""

    def __init__(self, cell, dk, N, lam=0.0, vol7=None, T=0.0, n2max=None, kappa=1.0,
                 ext_M=None, ext_v=None, cM=15.0 / 16.0, cV=-1.0 / 16.0, cS2=15.0 / 32.0, cN2=-1.0 / 32.0,
                 fixed=None):
        self.c, self.dk, self.N, self.lam, self.T, self.kappa = cell, dk, N, lam, T, kappa
        self.vol7 = vol7 if vol7 is not None else (2 * math.pi / dk) ** 3
        self.cM, self.cV, self.cS2, self.cN2 = cM, cV, cS2, cN2
        y = cell.y
        self.Pw = np.exp(-3 * cell.H * y) / self.vol7     # P(y)
        self.ext_M = ext_M if ext_M is not None else np.zeros_like(y)
        self.ext_v = ext_v if ext_v is not None else np.zeros_like(y)
        self.fixed = fixed     # optional list of (sector key, level index, occupation g f) for fixed occupations
        if n2max is None:
            n2max = 64
        r3 = r3_table(n2max)
        self.shells = [(n2, int(r3[n2])) for n2 in range(n2max + 1) if r3[n2] > 0]
        self.n = np.zeros_like(y)
        self.S = np.zeros_like(y)

    def potentials(self):
        dM = self.cM * self.lam * self.S + self.ext_M
        v = self.cV * self.lam * self.n + self.ext_v
        return dM, v

    def diagonalise(self, dM, v):
        c = self.c
        out = []
        for (j, parity), bs in c.basis.items():
            A, B, W = bs['A'], bs['B'], c.wq
            PM = j * (((A * (W * dM)) @ B.T) + ((B * (W * dM)) @ A.T))
            Pv = (A * (W * v)) @ A.T + (B * (W * v)) @ B.T
            base = np.diag(bs['E']) + PM + Pv
            KA = bs['Aov'] - bs['Bov']
            for (n2, r3) in self.shells:
                K = self.kappa * self.dk * math.sqrt(n2)
                Hm = base + j * K * KA
                ev, vec = np.linalg.eigh(Hm)
                nneg = bs['nneg']
                if parity == 'even' and j == -1 and n2 > 0:
                    nneg += 1           # the fold zero mode of j = -1 goes to -K: sea
                out.append({'j': j, 'parity': parity, 'n2': n2, 'r3': r3, 'K': K, 'eps': ev, 'vec': vec,
                            'nneg': nneg, 'g': 4.0 * r3})
        return out

    def occupy(self, secs):
        """Particle levels (positive branch + k = 0 zero modes): aufbau (T = 0) or Mermin (T > 0)."""
        levels = []
        for si, s in enumerate(secs):
            for li in range(s['nneg'], len(s['eps'])):
                levels.append((s['eps'][li], si, li, s['g']))
        levels.sort(key=lambda t: t[0])
        occ = {}
        if self.fixed is not None:
            for (si, li, gf) in self.fixed(secs):
                occ[(si, li)] = gf
            self.mu = None
            return occ
        if self.T == 0:
            left = self.N
            i = 0
            while left > 1e-12 and i < len(levels):
                e0 = levels[i][0]
                grp = [lv for lv in levels[i:] if abs(lv[0] - e0) < 1e-9]
                gs = sum(lv[3] for lv in grp)
                fill = 1.0 if gs <= left + 1e-9 else left / gs
                for lv in grp:
                    occ[(lv[1], lv[2])] = fill * lv[3]
                left -= fill * gs
                i += len(grp)
            if left > 1e-9:
                raise RuntimeError('not enough particle levels in the window')
            self.mu = None
        else:
            eps = np.array([lv[0] for lv in levels])
            deg = np.array([lv[3] for lv in levels])
            lo, hi = eps.min() - 50 * self.T - 1, eps.max() + 50 * self.T + 1
            for _ in range(300):
                mid = 0.5 * (lo + hi)
                fm = 1.0 / (1.0 + np.exp(np.clip((eps - mid) / self.T, -700, 700)))
                if np.sum(deg * fm) < self.N:
                    lo = mid
                else:
                    hi = mid
            self.mu = 0.5 * (lo + hi)
            fm = 1.0 / (1.0 + np.exp(np.clip((eps - self.mu) / self.T, -700, 700)))
            for lv, fo in zip(levels, fm):
                occ[(lv[1], lv[2])] = fo * lv[3]
        return occ

    def densities(self, secs, occ):
        c = self.c
        n = np.zeros_like(c.y)
        S = np.zeros_like(c.y)
        for (si, li), gf in occ.items():
            if gf == 0:
                continue
            s = secs[si]
            bs = c.basis[(s['j'], s['parity'])]
            coef = s['vec'][:, li]
            a = coef @ bs['A']
            b = coef @ bs['B']
            n += 0.5 * gf * (a * a + b * b)
            S += 0.5 * gf * s['j'] * 2 * a * b
        return n * self.Pw, S * self.Pw

    def label_set(self):
        """The occupied label set of the lambda = 0 problem (with the external fields), kept fixed during the SCF: the record's
        convention that every particle level is followed continuously as lambda is switched on."""
        lam = self.lam
        self.lam = 0.0
        dM, v = self.potentials()
        secs = self.diagonalise(dM, v)
        occ = self.occupy(secs)
        self.lam = lam
        labels = [(si, li - secs[si]['nneg'], gf) for (si, li), gf in occ.items()]
        self.fixed = lambda secs2, labels=labels: [(si, secs2[si]['nneg'] + r, gf) for (si, r, gf) in labels]
        return self

    def scf(self, tol=1e-13, maxit=600, mix=0.3, verbose=False, nlinear=3, depth=6):
        """Self-consistent field: linear mixing for the first steps, then regularised Anderson (Pulay) mixing with a
        safeguard (history reset and a linear step whenever the residual grows by more than a factor 2)."""
        hist_in, hist_out = [], []
        last_norm = None
        m = len(self.n)
        for it in range(maxit):
            dM, v = self.potentials()
            secs = self.diagonalise(dM, v)
            occ = self.occupy(secs)
            n_new, S_new = self.densities(secs, occ)
            if self.lam == 0:
                self.n, self.S = n_new, S_new
                break
            xin = np.concatenate([self.n, self.S])
            xout = np.concatenate([n_new, S_new])
            scale = max(1e-300, float(np.max(np.abs(xout))))
            res = (xout - xin) / scale
            err = float(np.max(np.abs(res)))
            if verbose:
                print(it, err)
            if err < tol:
                self.n, self.S = n_new, S_new
                break
            rn = float(np.linalg.norm(res))
            if last_norm is not None and rn > 2.0 * last_norm:
                hist_in, hist_out = [], []
            last_norm = rn
            hist_in.append(xin / scale)
            hist_out.append(xout / scale)
            hist_in, hist_out = hist_in[-depth:], hist_out[-depth:]
            if it < nlinear or len(hist_in) < 2:
                xnew = xin + mix * (xout - xin)
            else:
                R = np.array([o - i for i, o in zip(hist_in, hist_out)])
                k = len(R)
                Mm = R @ R.T
                Mm += 1e-12 * np.trace(Mm) / k * np.eye(k)
                A = np.zeros((k + 1, k + 1))
                A[:k, :k] = Mm
                A[:k, k] = 1.0
                A[k, :k] = 1.0
                rhs = np.zeros(k + 1)
                rhs[k] = 1.0
                try:
                    cf = np.linalg.solve(A, rhs)[:k]
                    if not np.all(np.isfinite(cf)) or np.max(np.abs(cf)) > 1e4:
                        raise np.linalg.LinAlgError
                    xi = cf @ np.array(hist_in)
                    xo = cf @ np.array(hist_out)
                    xnew = (xi + mix * (xo - xi)) * scale
                except np.linalg.LinAlgError:
                    hist_in, hist_out = [], []
                    xnew = xin + mix * (xout - xin)
            self.n, self.S = xnew[:m], xnew[m:]
        else:
            raise RuntimeError('SCF did not converge (last err %.2e)' % err)
        self.iterations = it + 1
        dM, v = self.potentials()
        self.secs = self.diagonalise(dM, v)
        self.occ = self.occupy(self.secs)
        self.n, self.S = self.densities(self.secs, self.occ)
        return self

    # ---------------- observables ----------------
    def e_int(self):
        return self.lam * (self.cS2 * self.S ** 2 + self.cN2 * self.n ** 2)

    def energy(self):
        band = sum(gf * self.secs[si]['eps'][li] for (si, li), gf in self.occ.items())
        eint = self.e_int()
        E_int = 2 * self.vol7 * float(np.sum(self.c.wq * np.exp(3 * self.c.H * self.c.y) * eint))
        return band - E_int, band, E_int

    def emt(self):
        c = self.c
        dM, v = self.potentials()
        Meff = c.m + dM
        rho_k = np.zeros_like(c.y)
        p3_k = np.zeros_like(c.y)
        p0_k = np.zeros_like(c.y)
        for (si, li), gf in self.occ.items():
            if gf == 0:
                continue
            s = self.secs[si]
            bs = c.basis[(s['j'], s['parity'])]
            coef = s['vec'][:, li]
            a = coef @ bs['A']
            b = coef @ bs['B']
            eps = s['eps'][li]
            no = self.Pw * (a * a + b * b)
            so = self.Pw * s['j'] * 2 * a * b
            to = self.Pw * s['j'] * (a * a - b * b)
            rho_k += 0.5 * gf * eps * no
            p3_k += 0.5 * gf * (s['K'] / 3.0) * to
            p0_k += 0.5 * gf * ((eps - v) * no - Meff * so - s['K'] * to)
        ei = self.e_int()
        return {'rho': rho_k - ei, 'p3': p3_k + ei, 'pt': ei, 'p0': p0_k + ei}

    def integrate(self, X):
        return 2 * self.vol7 * float(np.sum(self.c.wq * np.exp(3 * self.c.H * self.c.y) * X))

    def endpoint_p0(self):
        """p0 at the fold (y = 0) and at the tip (y = -L), from the orbital expansions evaluated at the ends.
        Uses the identity (eps - v) n_o - M s_o - K t_o = P (j/f)(a b' - b a') only implicitly: the same formula as emt()."""
        c = self.c
        ends = np.array([0.0, -c.L])
        Pw = np.exp(-3 * c.H * ends) / self.vol7
        # potentials at the ends: interpolate the self-consistent densities by evaluating them at the ends
        nE = np.zeros(2)
        SE = np.zeros(2)
        rows = []
        cache = {}
        for (si, li), gf in self.occ.items():
            if gf == 0:
                continue
            s = self.secs[si]
            key = (s['j'], s['parity'])
            if key not in cache:
                cache[key] = c.eval_at(s['j'], s['parity'], ends)
            Ae, Be = cache[key]
            coef = s['vec'][:, li]
            a = coef @ Ae
            b = coef @ Be
            rows.append((s, li, gf, a, b))
            nE += 0.5 * gf * Pw * (a * a + b * b)
            SE += 0.5 * gf * Pw * s['j'] * 2 * a * b
        dM = self.cM * self.lam * SE + np.interp(ends, c.y, self.ext_M)
        v = self.cV * self.lam * nE + np.interp(ends, c.y, self.ext_v)
        Meff = c.m + dM
        p0 = np.zeros(2)
        for (s, li, gf, a, b) in rows:
            eps = s['eps'][li]
            no = Pw * (a * a + b * b)
            so = Pw * s['j'] * 2 * a * b
            to = Pw * s['j'] * (a * a - b * b)
            p0 += 0.5 * gf * ((eps - v) * no - Meff * so - s['K'] * to)
        ei = self.lam * (self.cS2 * SE ** 2 + self.cN2 * nE ** 2)
        return p0 + ei, ei

    def levels_summary(self):
        lv = []
        for si, s in enumerate(self.secs):
            for li in range(s['nneg'], min(len(s['eps']), s['nneg'] + 4)):
                lv.append((float(s['eps'][li]), s['j'], s['parity'], s['n2'], li - s['nneg'], self.occ.get((si, li), 0.0)))
        lv.sort()
        return lv

    def homo_lumo(self):
        occd = [self.secs[si]['eps'][li] for (si, li), gf in self.occ.items() if gf > 1e-12]
        homo = max(occd)
        cand = []
        for si, s in enumerate(self.secs):
            for li in range(s['nneg'], len(s['eps'])):
                if self.occ.get((si, li), 0.0) < 1e-12 and s['eps'][li] > homo - 1e-12:
                    cand.append(s['eps'][li])
        return homo, min(cand)
