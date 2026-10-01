"""Revision theory (sympy side): coefficient rings, the author's metric (SPEC section 1), diagonal vielbein,
Christoffel symbols, the canonical spin connection, Riemann tensor - for an arbitrary DIAGONAL vielbein
e^a_mu = f_a delta^a_mu given together with a coordinate-derivative operator on coefficients.

Coordinates x1..x8 are indexed 0..7.  Frame metric eta = diag(+1,+1,+1,-1,-1,-1,-1,+1).
"""

import sympy as sp

ETA = [1, 1, 1, -1, -1, -1, -1, 1]
X4, X8 = 3, 7  # array indices of the time x4 and the hidden direction x8

# ---------------------------------------------------------------- the author's metric as a coefficient ring
# E = e^{a4(x4)}, A1..A4 = a4', a4'', a4''', a4'''' ; s = sin(z)^(1/6), c = cos(z), z = 6 H x8 in (0, pi/2)
E, s, c = sp.symbols("E s c", positive=True)
A1, A2, A3, A4, A5 = sp.symbols("A1 A2 A3 A4 A5", real=True)
H = sp.symbols("H", positive=True)
m, lam = sp.symbols("m lambda", real=True)
_ACHAIN = [(A1, A2), (A2, A3), (A3, A4), (A4, A5)]


def cd_author(expr, mu):
    """Explicit coordinate derivative of a coefficient in the author's metric ring."""
    if mu == X4:
        r = sp.diff(expr, E) * E * A1
        for a, b in _ACHAIN:
            r += sp.diff(expr, a) * b
        return r
    if mu == X8:
        return sp.diff(expr, s) * H * c / s**5 + sp.diff(expr, c) * (-6 * H * s**6)
    return sp.Integer(0)


def f_author():
    """Diagonal vielbein f_a = sqrt|g_aa| of SPEC section 1."""
    return [E * s, E * s, E * s, sp.Integer(1), s / E, s / E, s / E, c / s**6]


def zero_author(expr):
    """Exact zero test in the author's ring: clear denominators, reduce c^2 -> 1 - s^12."""
    expr = sp.sympify(expr)
    if expr == 0:
        return True
    num, _ = sp.fraction(sp.together(expr))
    num = sp.expand(num)
    if num == 0:
        return True
    red = sp.rem(sp.Poly(num, c), sp.Poly(c**2 - 1 + s**12, c))
    return sp.expand(red.as_expr()) == 0


def canon_author(expr):
    """A canonical form (for display and comparison): reduce c^2 -> 1 - s^12 in the numerator."""
    expr = sp.sympify(expr)
    num, den = sp.fraction(sp.together(expr))
    num = sp.expand(num)
    if num.has(c):
        num = sp.expand(sp.rem(sp.Poly(num, c), sp.Poly(c**2 - 1 + s**12, c)).as_expr())
    return sp.factor(num) / sp.factor(den)


def to_physical(expr):
    """Rewrite a ring expression in the author's functions: E = e^{a4}, s = sin(6 H x8)^(1/6), c = cos(6 H x8)."""
    x4, x8 = sp.symbols("x4 x8", real=True)
    a4 = sp.Function("a4")(x4)
    z = 6 * H * x8
    return sp.sympify(expr).subs({E: sp.exp(a4), s: sp.sin(z) ** sp.Rational(1, 6), c: sp.cos(z),
                                  A2: sp.Derivative(a4, (x4, 2)), A1: sp.Derivative(a4, x4)})


# ---------------------------------------------------------------- a general diagonal vielbein (jet symbols)
def generic_ring():
    F = [sp.Symbol(f"F{a+1}", positive=True) for a in range(8)]
    dF = [[sp.Symbol(f"F{a+1}_{n+1}", real=True) for n in range(8)] for a in range(8)]
    ddF = [[[sp.Symbol(f"F{a+1}_{min(n, r)+1}{max(n, r)+1}", real=True) for r in range(8)] for n in range(8)]
           for a in range(8)]

    def cd(expr, mu):
        r = sp.Integer(0)
        fs = expr.free_symbols
        for a in range(8):
            if F[a] in fs:
                r += sp.diff(expr, F[a]) * dF[a][mu]
            for n in range(8):
                if dF[a][n] in fs:
                    r += sp.diff(expr, dF[a][n]) * ddF[a][n][mu]
        return r

    return F, dF, ddF, cd


def zero_generic(expr):
    expr = sp.sympify(expr)
    if expr == 0:
        return True
    num, _ = sp.fraction(sp.together(expr))
    return sp.expand(num) == 0


# ---------------------------------------------------------------- geometry of a diagonal vielbein
class Geometry:
    def __init__(self, f, cd, simplify=sp.expand):
        self.f = f
        self.cd = cd
        n = 8
        self.g = [ETA[a] * f[a] ** 2 for a in range(n)]
        self.ginv = [sp.Integer(ETA[a]) / f[a] ** 2 for a in range(n)]
        self.sqrtg = sp.Mul(*f)
        g, gi = self.g, self.ginv
        dg = [[cd(g[l], mu) for mu in range(n)] for l in range(n)]
        Gam = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
        for l in range(n):
            for a in range(n):
                for b in range(n):
                    v = 0
                    if l == b:
                        v += dg[l][a]
                    if l == a:
                        v += dg[l][b]
                    if a == b:
                        v -= dg[a][l]
                    if v != 0:
                        Gam[l][a][b] = simplify(gi[l] * v / 2)
        self.Gam = Gam
        # canonical spin connection omega_mu^a_b = e^a_nu (d_mu E_b^nu + Gam^nu_{mu lam} E_b^lam)
        om_mixed = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
        for mu in range(n):
            for a in range(n):
                for b in range(n):
                    v = Gam[a][mu][b] / f[b]
                    if a == b:
                        v += cd(1 / f[b], mu)
                    om_mixed[mu][a][b] = simplify(f[a] * v)
        self.om_mixed = om_mixed
        self.om = [[[simplify(ETA[a] * om_mixed[mu][a][b]) for b in range(n)] for a in range(n)] for mu in range(n)]

    def spin_matrices(self, S):
        """Omega_mu = (1/2) omega_mu ab S^ab."""
        n = 8
        Om = []
        for mu in range(n):
            M = sp.zeros(16, 16)
            for a in range(n):
                for b in range(n):
                    if self.om[mu][a][b] != 0:
                        M += self.om[mu][a][b] * S[a][b] / 2
            Om.append(M.applyfunc(sp.expand))
        self.Om = Om
        return Om

    def curved_gammas(self, G):
        self.gam = [(G[a] / self.f[a]) for a in range(8)]
        return self.gam

    def riemann(self, simplify=sp.expand):
        """R^rho_{sigma mu nu} = d_mu Gam^rho_{nu sigma} - d_nu Gam^rho_{mu sigma} + Gam Gam - Gam Gam."""
        n = 8
        Gm, cd = self.Gam, self.cd
        R = {}
        for r in range(n):
            for sg in range(n):
                for mu in range(n):
                    for nu in range(mu + 1, n):
                        v = cd(Gm[r][nu][sg], mu) - cd(Gm[r][mu][sg], nu)
                        for l in range(n):
                            v += Gm[r][mu][l] * Gm[l][nu][sg] - Gm[r][nu][l] * Gm[l][mu][sg]
                        v = simplify(v)
                        if v != 0:
                            R[(r, sg, mu, nu)] = v
                            R[(r, sg, nu, mu)] = -v
        self.R = R
        ric = [[sp.Integer(0)] * n for _ in range(n)]
        for (r, sg, mu, nu), v in R.items():
            if r == mu:
                ric[sg][nu] += v
        self.ricci = [[simplify(x) for x in row] for row in ric]
        self.Rscalar = simplify(sum(self.ginv[a] * self.ricci[a][a] for a in range(n)))
        return R
