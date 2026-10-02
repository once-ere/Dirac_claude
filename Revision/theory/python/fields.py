"""Revision theory (sympy side): spinor-valued jet elements, the Lagrangian of SPEC section 3, its
Euler-Lagrange expressions, the current and the energy-momentum tensor, for either statistics."""

import sympy as sp

from superalg import Alg, gen, CHI, PSI, THETA


def _nz(M):
    return [(i, j, M[i, j]) for i in range(M.rows) for j in range(M.cols) if M[i, j] != 0]


class Spinors:
    def __init__(self, stat, geom, G, C, m, lam):
        self.stat, self.geo, self.G, self.C = stat, geom, G, C
        self.m, self.lam = m, lam
        self.gam = geom.gam
        self.Om = geom.Om
        self.sqrtg = geom.sqrtg
        self.cd = geom.cd

    # vectors of algebra elements
    def zero(self):
        return Alg(self.stat)

    def psi(self, d=()):
        return [Alg.g(self.stat, gen(PSI, A, d)) for A in range(16)]

    def chi(self, d=()):
        return [Alg.g(self.stat, gen(CHI, A, d)) for A in range(16)]

    def theta(self, d=()):
        return [Alg.g(self.stat, gen(THETA, A, d)) for A in range(16)]

    def matvec(self, M, v):
        out = [self.zero() for _ in range(16)]
        for i, j, x in _nz(M):
            out[i] = out[i] + v[j].scale(x)
        return out

    def vecmat(self, v, M):
        out = [self.zero() for _ in range(16)]
        for i, j, x in _nz(M):
            out[j] = out[j] + v[i].scale(x)
        return out

    def vadd(self, u, v):
        return [a + b for a, b in zip(u, v)]

    def vscale(self, u, x):
        return [a.scale(x) for a in u]

    def dot(self, row, col):
        r = self.zero()
        for a, b in zip(row, col):
            r = r + a * b
        return r

    # field quantities
    def psibar(self, d=()):
        return self.vecmat(self.chi(d), self.C)

    def Dpsi(self, mu):
        return self.vadd(self.psi((mu,)), self.matvec(self.Om[mu], self.psi()))

    def Dpsibar(self, mu):
        return [a - b for a, b in zip(self.psibar((mu,)), self.vecmat(self.psibar(), self.Om[mu]))]

    def S(self):
        return self.dot(self.psibar(), self.psi())

    def lagrangian_parts(self):
        """Return K, V with L = sqrt|g| (K - V); K = (1/2)(Psibar g^mu D Psi - D Psibar g^mu Psi), V = m S + lam/2 S^2."""
        K = self.zero()
        pb = self.psibar()
        ps = self.psi()
        for mu in range(8):
            K = K + self.dot(pb, self.matvec(self.gam[mu], self.Dpsi(mu)))
            K = K - self.dot(self.vecmat(self.Dpsibar(mu), self.gam[mu]), ps)
        K = K.scale(sp.Rational(1, 2)).expand()
        Sx = self.S()
        V = (Sx.scale(self.m) + (Sx * Sx).scale(self.lam / 2)).expand()
        return K, V

    def lagrangian(self):
        K, V = self.lagrangian_parts()
        return (K - V).scale(self.sqrtg).expand()

    def lagrangian_unsym(self):
        K = self.zero()
        pb = self.psibar()
        for mu in range(8):
            K = K + self.dot(pb, self.matvec(self.gam[mu], self.Dpsi(mu)))
        Sx = self.S()
        V = Sx.scale(self.m) + (Sx * Sx).scale(self.lam / 2)
        return (K - V).scale(self.sqrtg).expand()

    def dirac_E(self):
        """E = gamma^mu D_mu Psi - (m + U'(S)) Psi, U' = lam S."""
        out = [self.zero() for _ in range(16)]
        for mu in range(8):
            out = self.vadd(out, self.matvec(self.gam[mu], self.Dpsi(mu)))
        Mp = Alg.scalar(self.stat, self.m) + self.S().scale(self.lam)
        ps = self.psi()
        return [(out[A] - Mp * ps[A]).expand() for A in range(16)]

    def dirac_Ebar(self):
        """Ebar = -( D_mu Psibar gamma^mu + (m + U'(S)) Psibar )."""
        out = [self.zero() for _ in range(16)]
        for mu in range(8):
            out = self.vadd(out, self.vecmat(self.Dpsibar(mu), self.gam[mu]))
        Mp = Alg.scalar(self.stat, self.m) + self.S().scale(self.lam)
        pb = self.psibar()
        return [(-(out[B] + Mp * pb[B])).expand() for B in range(16)]

    def euler_lagrange(self, L):
        """EL_chi[A] = dL/dchi_A - D_mu dL/dchi_{A,mu} (left derivatives);
        EL_psi[B] = dL/dpsi_B - D_mu dL/dpsi_{B,mu} (right derivatives)."""
        elc, elp = [], []
        for A in range(16):
            r = L.lderiv(gen(CHI, A))
            for mu in range(8):
                r = r - L.lderiv(gen(CHI, A, (mu,))).total(mu, self.cd)
            elc.append(r.expand())
            r = L.rderiv(gen(PSI, A))
            for mu in range(8):
                r = r - L.rderiv(gen(PSI, A, (mu,))).total(mu, self.cd)
            elp.append(r.expand())
        return elc, elp

    def current(self):
        """J^mu = -i Psibar gamma^mu Psi."""
        pb, ps = self.psibar(), self.psi()
        return [self.dot(pb, self.matvec(self.gam[mu], ps)).scale(-sp.I).expand() for mu in range(8)]

    def theta_tensor(self):
        """Theta^mu_nu = (1/4)[Psibar g^mu D_nu Psi - D_nu Psibar g^mu Psi + g^{mu mu} g_{nu nu}(mu <-> nu)]
        (diagonal metric; the symmetrised canonical tensor)."""
        pb, ps = self.psibar(), self.psi()
        X = [[None] * 8 for _ in range(8)]
        for mu in range(8):
            for nu in range(8):
                X[mu][nu] = (self.dot(pb, self.matvec(self.gam[mu], self.Dpsi(nu)))
                             - self.dot(self.vecmat(self.Dpsibar(nu), self.gam[mu]), ps))
        g, gi = self.geo.g, self.geo.ginv
        Th = [[None] * 8 for _ in range(8)]
        for mu in range(8):
            for nu in range(8):
                Th[mu][nu] = (X[mu][nu] + X[nu][mu].scale(gi[mu] * g[nu])).scale(sp.Rational(1, 4)).expand()
        return Th

    def emt(self):
        """T^mu_nu = -Theta^mu_nu + delta^mu_nu (K - V); returns T, T_kin, T_pot, K, V."""
        K, V = self.lagrangian_parts()
        Th = self.theta_tensor()
        T, Tk, Tp = [[None] * 8 for _ in range(8)], [[None] * 8 for _ in range(8)], [[None] * 8 for _ in range(8)]
        for mu in range(8):
            for nu in range(8):
                Tk[mu][nu] = -Th[mu][nu] + (K if mu == nu else self.zero())
                Tp[mu][nu] = (-V) if mu == nu else self.zero()
                T[mu][nu] = (Tk[mu][nu] + Tp[mu][nu]).expand()
        return T, Tk, Tp, K, V
