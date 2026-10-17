"""Revision theory (sympy side): coefficient rings, the author's metric (SPEC section 1), diagonal vielbein,
Christoffel symbols, the canonical spin connection, Riemann tensor - for an arbitrary DIAGONAL vielbein
e^a_mu = f_a delta^a_mu given together with a coordinate-derivative operator on coefficients.

The author's coordinates x0..x7 are indexed 0..7 (index k = xk; x0 = the hidden direction, first).  Frame metric
eta = diag(+1,+1,+1,+1,-1,-1,-1,-1).  (Until 2026-10-14 the withdrawn labels x1..x8, hidden x8 last, were used.)

The metric is the CORRECTED metric of 2026-10-16 (SPEC section 1, version 2; Revision/metric_warped/):
g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 REAL (the user's rules
of 2026-10-16: -infinity < z < infinity, sin^{1/3} z = (sin^2 z)^{1/6}), for GENERAL functions a4(x4) and b4(x4) > 0.
(Until 2026-10-16 this ring described the metric of 2026-10-14 on 0 < z < pi/2, withdrawn; until 2026-10-15 the
metric b4 = 1, withdrawn.)
"""

import sympy as sp

ETA = [1, 1, 1, 1, -1, -1, -1, -1]
X0, X4 = 0, 4  # array indices of the hidden direction x0 and the time x4

# ---------------------------------------------------------------- the author's metric as a coefficient ring
# E = e^{a4(x4)}, A1..A5 = a4', a4'', ..., a4^(5); Q = b4(x4)^(1/2) > 0, B1..B5 = (ln b4)', (ln b4)'', ..., (ln b4)^(5)
# (so b4'/b4 = B1 and b4''/b4 = B2 + B1^2); for EVERY real z = 6 H x0: sv = sin z and c = cos z (signed),
# w = (sin^2 z)^(1/12) > 0 (w^12 = sv^2), sgn = sign(cot z) = +-1 (sqrt|g| = sgn f0...f7; constant between the
# degenerate points z = n pi/2, so its derivatives vanish there)
E, w, Q = sp.symbols("E w Q", positive=True)
sv, c, sgn = sp.symbols("sv c sgn", real=True)
A1, A2, A3, A4, A5 = sp.symbols("A1 A2 A3 A4 A5", real=True)
B1, B2, B3, B4, B5, B6 = sp.symbols("B1 B2 B3 B4 B5 B6", real=True)
H = sp.symbols("H", positive=True)
m, lam = sp.symbols("m lambda", real=True)
_ACHAIN = [(A1, A2), (A2, A3), (A3, A4), (A4, A5), (B1, B2), (B2, B3), (B3, B4), (B4, B5), (B5, B6)]


def cd_author(expr, mu):
    """Explicit coordinate derivative of a coefficient in the author's metric ring (dE/dx4 = E A1,
    dQ/dx4 = Q B1/2, dA_k/dx4 = A_(k+1), dB_k/dx4 = B_(k+1))."""
    if mu == X4:
        r = sp.diff(expr, E) * E * A1 + sp.diff(expr, Q) * Q * B1 / 2
        for a, b in _ACHAIN:
            r += sp.diff(expr, a) * b
        return r
    if mu == X0:
        return sp.diff(expr, sv) * 6 * H * c + sp.diff(expr, c) * (-6 * H * sv) + sp.diff(expr, w) * H * c * w / sv
    return sp.Integer(0)


def f_author():
    """Diagonal vielbein f_a = sqrt|g_aa| of SPEC section 1 (the corrected metric; f0 signed):
    f0 = e^{-a4} b4^(1/2) cot z, f1..3 = e^{a4}, f4 = 1, f5..7 = e^{-a4} b4^(1/2) (sin^2 z)^(1/12)."""
    return [Q * c / (E * sv), E, E, E, sp.Integer(1), Q * w / E, Q * w / E, Q * w / E]


def reduce_author(num):
    """Canonical remainder of a polynomial modulo c^2 + sv^2 - 1, w^12 - sv^2, sgn^2 - 1 (coprime leading terms)."""
    num = sp.expand(num)
    for var, rel in ((c, c**2 - 1 + sv**2), (w, w**12 - sv**2), (sgn, sgn**2 - 1)):
        if num.has(var):
            num = sp.expand(sp.rem(sp.Poly(num, var), sp.Poly(rel, var)).as_expr())
    return num


def zero_author(expr):
    """Exact zero test in the ring of the corrected metric (every real z): clear denominators, reduce the numerator."""
    expr = sp.sympify(expr)
    if expr == 0:
        return True
    num, _ = sp.fraction(sp.together(expr))
    num = sp.expand(num)
    if num == 0:
        return True
    return reduce_author(num) == 0


def canon_author(expr):
    """A canonical form (for display and comparison): the reduced numerator over the factored denominator."""
    expr = sp.sympify(expr)
    num, den = sp.fraction(sp.together(expr))
    return sp.factor(reduce_author(num)) / sp.factor(den)


def to_physical(expr):
    """Rewrite a ring expression in the author's functions: E = e^{a4}, Q = b4^(1/2), sv = sin(6 H x0),
    c = cos(6 H x0), w = (sin(6 H x0)^2)^(1/12), sgn = sign(cot(6 H x0)), A1 = a4', A2 = a4'', B1 = b4'/b4,
    B2 = b4''/b4 - (b4'/b4)^2."""
    x0, x4 = sp.symbols("x0 x4", real=True)
    a4 = sp.Function("a4")(x4)
    b4 = sp.Function("b4")(x4)
    z = 6 * H * x0
    b1 = sp.Derivative(b4, x4) / b4
    return sp.sympify(expr).subs({B2: sp.Derivative(b4, (x4, 2)) / b4 - b1 ** 2, B1: b1}).subs(
        {E: sp.exp(a4), Q: sp.sqrt(b4), w: (sp.sin(z) ** 2) ** sp.Rational(1, 12), sv: sp.sin(z), c: sp.cos(z),
         sgn: sp.sign(sp.cot(z)), A2: sp.Derivative(a4, (x4, 2)), A1: sp.Derivative(a4, x4)})


# ---------------------------------------------------------------- a general diagonal vielbein (jet symbols)
def generic_ring():
    # F{a} = f_a of the coordinate xa (a = 0..7, the author's x0..x7); F{a}_{n} = d f_a / d xn
    F = [sp.Symbol(f"F{a}", positive=True) for a in range(8)]
    dF = [[sp.Symbol(f"F{a}_{n}", real=True) for n in range(8)] for a in range(8)]
    ddF = [[[sp.Symbol(f"F{a}_{min(n, r)}{max(n, r)}", real=True) for r in range(8)] for n in range(8)]
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
    def __init__(self, f, cd, simplify=sp.expand, sign=1):
        """sign: the factor that makes sqrt|g| = sign * f0...f7 (sgn for the corrected metric, whose f0 is signed;
        1 for a positive generic vielbein)."""
        self.f = f
        self.cd = cd
        n = 8
        self.g = [ETA[a] * f[a] ** 2 for a in range(n)]
        self.ginv = [sp.Integer(ETA[a]) / f[a] ** 2 for a in range(n)]
        self.sqrtg = sign * sp.Mul(*f)
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
