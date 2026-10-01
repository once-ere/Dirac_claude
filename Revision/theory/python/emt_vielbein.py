"""Revision theory (sympy side): the energy-momentum tensor by a GENERAL first-order vielbein variation
e^a_mu = f_a delta^a_mu + h^a_mu(x) around the author's metric (all 64 components h^a_mu, off-diagonal ones
included).  Every quantity is carried as a pair (background, first order in h).

delta S = int sqrt|g| T^mu_a delta e^a_mu,  T^mu_nu = T^mu_a e^a_nu,  equivalent to
delta S = (1/2) int sqrt|g| T^{mu nu} delta g_mu nu  (the convention giving rho = -T^x4_x4 = m S + U)."""

import sympy as sp

from geometry import ETA, cd_author
from superalg import Alg


def linear_variation_T(sps, geo, G, Smat):
    """Return Tvar[mu][nu] (Alg) = (f_nu / sqrt|g|) delta S / delta h^nu_mu evaluated on the background."""
    n = 8
    f = geo.f
    h = [[sp.Symbol(f"h_{a}_{mu}", real=True) for mu in range(n)] for a in range(n)]
    hd = [[[sp.Symbol(f"h_{a}_{mu}_d{nu}", real=True) for nu in range(n)] for mu in range(n)] for a in range(n)]
    hset = {h[a][mu]: (a, mu) for a in range(n) for mu in range(n)}

    def cd1(expr, lam_):
        """derivative of a first-order coefficient: background part + h -> hd."""
        r = cd_author(expr, lam_)
        for sym in expr.free_symbols:
            if sym in hset:
                a, mu = hset[sym]
                r += sp.diff(expr, sym) * hd[a][mu][lam_]
        return r

    E0 = [sp.Integer(1) / f[a] for a in range(n)]          # E0^mu_a = delta / f_a
    # E1^mu_a = -E0^mu_mu h^mu... : (E1)[mu][a] = -E0[mu] h[mu][a]?  E = e^{-1}; E1 = -E0 e1 E0 with e1[a][mu] = h[a][mu]
    E1 = [[-E0[mu] * h[mu][a] * E0[a] for a in range(n)] for mu in range(n)]  # E1[mu][a]
    g0 = geo.g
    g0i = geo.ginv
    g1 = [[ETA[nu] * f[nu] * h[nu][mu] + ETA[mu] * f[mu] * h[mu][nu] for nu in range(n)] for mu in range(n)]
    g1i = [[-g0i[l] * g1[l][k] * g0i[k] for k in range(n)] for l in range(n)]
    dg0 = [[cd_author(g0[k], lm) for lm in range(n)] for k in range(n)]  # diagonal
    dg1 = [[[cd1(g1[k][nu], lm) for lm in range(n)] for nu in range(n)] for k in range(n)]

    def dg0f(k, nu, lm):
        return dg0[k][lm] if k == nu else 0

    Gam0 = geo.Gam
    Gam1 = [[[None] * n for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for mu in range(n):
            for nu in range(n):
                v = g0i[l] * (dg1[l][nu][mu] + dg1[l][mu][nu] - dg1[mu][nu][l]) / 2
                for k in range(n):
                    if g1i[l][k] != 0:
                        w = dg0f(k, nu, mu) + dg0f(k, mu, nu) - dg0f(mu, nu, k)
                        if w != 0:
                            v += g1i[l][k] * w / 2
                Gam1[l][mu][nu] = sp.expand(v)
    # omega1_mu^a_b = e1^a_nu (d_mu E0_b^nu + Gam0^nu_{mu l} E0_b^l) + e0^a_nu (d_mu E1_b^nu + Gam1^nu_{mu l} E0_b^l
    #                 + Gam0^nu_{mu l} E1_b^l)
    Om1 = []
    for mu in range(n):
        M = sp.zeros(16, 16)
        for a in range(n):
            for b in range(n):
                v = 0
                for nu in range(n):
                    t0 = (cd_author(E0[b], mu) if nu == b else 0) + Gam0[nu][mu][b] * E0[b]
                    if t0 != 0:
                        v += h[a][nu] * t0
                t = cd1(E1[a][b], mu) + Gam1[a][mu][b] * E0[b]
                for l in range(n):
                    if Gam0[a][mu][l] != 0:
                        t += Gam0[a][mu][l] * E1[l][b]
                v += f[a] * t
                v = sp.expand(ETA[a] * v)
                if v != 0:
                    M += v * Smat[a][b] / 2
        Om1.append(M.applyfunc(sp.expand))
    gam1 = []
    for mu in range(n):
        M = sp.zeros(16, 16)
        for a in range(n):
            if E1[mu][a] != 0:
                M += E1[mu][a] * G[a]
        gam1.append(M)
    sq0 = geo.sqrtg
    sq1 = sp.expand(sq0 * sum(h[a][a] / f[a] for a in range(n)))
    K0, V = sps.lagrangian_parts()
    pb, ps = sps.psibar(), sps.psi()
    K1 = sps.zero()
    for mu in range(n):
        K1 = K1 + sps.dot(pb, sps.matvec(gam1[mu], sps.Dpsi(mu)))
        K1 = K1 - sps.dot(sps.vecmat(sps.Dpsibar(mu), gam1[mu]), ps)
        K1 = K1 + sps.dot(pb, sps.matvec(geo.gam[mu] * Om1[mu] + Om1[mu] * geo.gam[mu], ps))
    K1 = K1.scale(sp.Rational(1, 2))
    L1 = ((K0 - V).scale(sq1) + K1.scale(sq0)).expand()
    Tvar = [[None] * n for _ in range(n)]
    for a in range(n):
        for mu in range(n):
            var = L1.map_coeffs(lambda v: sp.diff(v, h[a][mu]))
            for nu in range(n):
                dv = L1.map_coeffs(lambda v: sp.diff(v, hd[a][mu][nu]))
                if len(dv):
                    var = var - dv.total(nu, cd_author)
            # T^mu_a = var / sqrt|g|;  T^mu_nu = T^mu_a e^a_nu  (e^a_nu = f_a delta)
            Tvar[mu][a] = var.scale(f[a] / sq0).expand()
    return Tvar
