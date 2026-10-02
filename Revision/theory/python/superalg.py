"""Revision theory (sympy side): a small exact jet super-algebra for BOTH statistics.

Written anew for Revision/theory/python (no shared code with the Wolfram side or the old stages).

Generators are field components and their coordinate derivatives on the jet space:
    key = (kind, A, deriv)   kind 0 = chi (= Psi^dagger component, i.e. the complex conjugate of psi),
                             kind 1 = psi, kind 2 = theta (a REAL field, used only for the negative control);
                             A = 0..15 the spinor index; deriv = sorted tuple of coordinate indices 0..7
                             (0..7 stand for x1..x8).
An element is a dict  monomial -> sympy coefficient, a monomial being a sorted tuple of keys.

stat = "grassmann": every generator is odd (anticommuting) - dirac16complex;
stat = "commuting": every generator is even - dirac16complex00.

Complex conjugation reverses the order of a product, (a b)^* = b^* a^*, maps psi <-> chi and theta -> theta
and conjugates the coefficient (all symbols are real; I -> -I).
"""

import sympy as sp

CHI, PSI, THETA = 0, 1, 2


def gen(kind, A, deriv=()):
    return (kind, A, tuple(sorted(deriv)))


def _sort_sign(lst, odd):
    """Sort a list of keys; return (sorted tuple, sign) with the Grassmann sign if odd; None if a repeated
    odd generator makes the product vanish."""
    a = list(lst)
    sign = 1
    # insertion sort counting transpositions (lists are short)
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            sign = -sign
            j -= 1
    if odd:
        for i in range(1, len(a)):
            if a[i] == a[i - 1]:
                return None, 0
        return tuple(a), sign
    return tuple(a), 1


class Alg:
    __slots__ = ("stat", "t")

    def __init__(self, stat, terms=None):
        assert stat in ("grassmann", "commuting")
        self.stat = stat
        self.t = dict(terms) if terms else {}

    @property
    def odd(self):
        return self.stat == "grassmann"

    # ---- construction
    @staticmethod
    def scalar(stat, c):
        return Alg(stat, {(): sp.sympify(c)}) if c != 0 else Alg(stat)

    @staticmethod
    def g(stat, key, c=1):
        return Alg(stat, {(key,): sp.sympify(c)})

    def copy(self):
        return Alg(self.stat, self.t)

    # ---- arithmetic
    def _addterm(self, mono, c):
        if c == 0:
            return
        v = self.t.get(mono)
        if v is None:
            self.t[mono] = c
        else:
            s = v + c
            if s == 0:
                del self.t[mono]
            else:
                self.t[mono] = s

    def __add__(self, o):
        r = self.copy()
        for k, v in o.t.items():
            r._addterm(k, v)
        return r

    def __neg__(self):
        return Alg(self.stat, {k: -v for k, v in self.t.items()})

    def __sub__(self, o):
        return self + (-o)

    def scale(self, c):
        c = sp.sympify(c)
        if c == 0:
            return Alg(self.stat)
        return Alg(self.stat, {k: c * v for k, v in self.t.items()})

    def __mul__(self, o):
        if not isinstance(o, Alg):
            return self.scale(o)
        r = Alg(self.stat)
        for k1, v1 in self.t.items():
            for k2, v2 in o.t.items():
                mono, sgn = _sort_sign(k1 + k2, self.odd)
                if mono is None:
                    continue
                r._addterm(mono, sgn * v1 * v2)
        return r

    def map_coeffs(self, f):
        r = Alg(self.stat)
        for k, v in self.t.items():
            r._addterm(k, f(v))
        return r

    def expand(self):
        return self.map_coeffs(sp.expand)

    # ---- conjugation
    def conj(self):
        r = Alg(self.stat)
        for k, v in self.t.items():
            lst = []
            for (kind, A, d) in reversed(k):
                nk = {CHI: PSI, PSI: CHI, THETA: THETA}[kind]
                lst.append((nk, A, d))
            mono, sgn = _sort_sign(lst, self.odd)
            if mono is None:
                continue
            r._addterm(mono, sgn * v.subs(sp.I, -sp.I))
        return r

    # ---- derivatives with respect to a generator
    def lderiv(self, key):
        r = Alg(self.stat)
        for k, v in self.t.items():
            if self.odd:
                if key in k:
                    i = k.index(key)
                    r._addterm(k[:i] + k[i + 1:], (-1) ** i * v)
            else:
                n = k.count(key)
                if n:
                    i = k.index(key)
                    r._addterm(k[:i] + k[i + 1:], n * v)
        return r

    def rderiv(self, key):
        if not self.odd:
            return self.lderiv(key)
        r = Alg(self.stat)
        for k, v in self.t.items():
            if key in k:
                i = k.index(key)
                r._addterm(k[:i] + k[i + 1:], (-1) ** (len(k) - 1 - i) * v)
        return r

    # ---- total derivative d/dx_mu on the jet space; cd(coeff, mu) differentiates the explicit coefficient
    def total(self, mu, cd):
        r = Alg(self.stat)
        for k, v in self.t.items():
            dv = cd(v, mu)
            if dv != 0:
                r._addterm(k, dv)
            for i, (kind, A, d) in enumerate(k):
                nk = (kind, A, tuple(sorted(d + (mu,))))
                mono, sgn = _sort_sign(k[:i] + (nk,) + k[i + 1:], self.odd)
                if mono is None:
                    continue
                r._addterm(mono, sgn * v)
        return r

    # ---- substitution of generators by elements (rule(key) -> Alg or None)
    def subst(self, rule):
        r = Alg(self.stat)
        for k, v in self.t.items():
            if not any(rule(g) is not None for g in k):
                r._addterm(k, v)
                continue
            prod = Alg.scalar(self.stat, v)
            for g in k:
                rg = rule(g)
                prod = prod * (rg if rg is not None else Alg.g(self.stat, g))
            for kk, vv in prod.t.items():
                r._addterm(kk, vv)
        return r

    def generators(self):
        s = set()
        for k in self.t:
            s.update(k)
        return s

    def is_zero(self, zero_test):
        """True iff every coefficient is exactly zero (zero_test decides one coefficient)."""
        bad = [k for k, v in self.t.items() if not zero_test(v)]
        return len(bad) == 0, bad

    def __len__(self):
        return len(self.t)
