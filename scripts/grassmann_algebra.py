#!/usr/bin/env python3
"""A small exact Grassmann-algebra implementation.

An element is a dict ``{sorted tuple of generator indices: coefficient}``;
monomials are stored in increasing generator order and every reordering
contributes the sign of the permutation (theta_i theta_j = - theta_j theta_i,
theta_i^2 = 0).  Coefficients may be any exact commutative ring elements that
support ``+ - *`` and ``== 0`` (Python ints, ``fractions.Fraction``, gmpy2
``mpq``, sympy field elements, or the ``GaussianRational`` class below).

Operations
----------
* product, sum, scalar multiples;
* left derivative  d_L/d theta_k (theta_k is brought to the far left first);
* right derivative d_R/d theta_k;
* even derivations (e.g. the total derivative d_mu acting on field-jet
  generators, theta_{a;alpha} -> theta_{a;alpha+mu});
* complex conjugation with an involution on the generators and the
  convention (theta_1 theta_2)^* = theta_2^* theta_1^* (order reversal), so
  that (A B)^* = B^* A^* for all elements;
* grading helpers.

``JetSpace`` enumerates generators for field jets
``Psi_{s,a;alpha}`` (species s, component a, sorted derivative multi-index alpha).
"""

from __future__ import annotations

import itertools
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

Monomial = Tuple[int, ...]


def _merge(m1: Monomial, m2: Monomial) -> Tuple[int, Optional[Monomial]]:
    """Sign and sorted monomial of the product m1*m2 (0, None if a generator repeats)."""
    i = j = 0
    n1, n2 = len(m1), len(m2)
    inv = 0
    out: List[int] = []
    while i < n1 and j < n2:
        a = m1[i]
        b = m2[j]
        if a < b:
            out.append(a)
            i += 1
        elif a > b:
            out.append(b)
            j += 1
            inv += n1 - i
        else:
            return 0, None
    if i < n1:
        out.extend(m1[i:])
    if j < n2:
        out.extend(m2[j:])
    return (-1 if inv & 1 else 1), tuple(out)


def sort_with_sign(seq: Sequence[int]) -> Tuple[int, Optional[Monomial]]:
    """Sign of the permutation sorting ``seq`` (0 if an entry repeats)."""
    lst = list(seq)
    if len(set(lst)) != len(lst):
        return 0, None
    inv = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                inv += 1
    return (-1 if inv & 1 else 1), tuple(sorted(lst))


def _is_zero_coeff(c) -> bool:
    return c == 0


class Grassmann:
    """Element of the Grassmann algebra with exact coefficients."""

    __slots__ = ("terms",)

    def __init__(self, terms: Optional[Dict[Monomial, object]] = None):
        self.terms: Dict[Monomial, object] = {} if terms is None else terms

    # -- constructors -------------------------------------------------------
    @staticmethod
    def gen(i: int, coeff=1) -> "Grassmann":
        return Grassmann({(i,): coeff}) if not _is_zero_coeff(coeff) else Grassmann()

    @staticmethod
    def scalar(c) -> "Grassmann":
        return Grassmann({(): c}) if not _is_zero_coeff(c) else Grassmann()

    @staticmethod
    def from_monomial(m: Sequence[int], coeff=1) -> "Grassmann":
        s, mm = sort_with_sign(m)
        if s == 0 or _is_zero_coeff(coeff):
            return Grassmann()
        return Grassmann({mm: coeff if s > 0 else -coeff})

    # -- ring structure -----------------------------------------------------
    def copy(self) -> "Grassmann":
        return Grassmann(dict(self.terms))

    def _iadd_term(self, m: Monomial, c) -> None:
        if m in self.terms:
            v = self.terms[m] + c
            if _is_zero_coeff(v):
                del self.terms[m]
            else:
                self.terms[m] = v
        elif not _is_zero_coeff(c):
            self.terms[m] = c

    def __add__(self, other) -> "Grassmann":
        if not isinstance(other, Grassmann):
            other = Grassmann.scalar(other)
        r = self.copy()
        for m, c in other.terms.items():
            r._iadd_term(m, c)
        return r

    __radd__ = __add__

    def __neg__(self) -> "Grassmann":
        return Grassmann({m: -c for m, c in self.terms.items()})

    def __sub__(self, other) -> "Grassmann":
        if not isinstance(other, Grassmann):
            other = Grassmann.scalar(other)
        return self + (-other)

    def __rsub__(self, other) -> "Grassmann":
        return (-self) + other

    def scale(self, s) -> "Grassmann":
        out: Dict[Monomial, object] = {}
        for m, c in self.terms.items():
            v = c * s
            if not _is_zero_coeff(v):
                out[m] = v
        return Grassmann(out)

    def __mul__(self, other) -> "Grassmann":
        if not isinstance(other, Grassmann):
            return self.scale(other)
        r = Grassmann()
        for m1, c1 in self.terms.items():
            for m2, c2 in other.terms.items():
                s, m = _merge(m1, m2)
                if s == 0:
                    continue
                v = c1 * c2
                r._iadd_term(m, v if s > 0 else -v)
        return r

    def __rmul__(self, other) -> "Grassmann":
        # scalars commute with everything
        return self.scale(other)

    def __pow__(self, k: int) -> "Grassmann":
        r = Grassmann.scalar(1)
        for _ in range(k):
            r = r * self
        return r

    def is_zero(self, zero_test: Optional[Callable] = None) -> bool:
        if zero_test is None:
            return len(self.terms) == 0
        return all(zero_test(c) for c in self.terms.values())

    def __eq__(self, other) -> bool:  # exact equality
        if not isinstance(other, Grassmann):
            other = Grassmann.scalar(other)
        return (self - other).is_zero()

    def __hash__(self):  # pragma: no cover - elements are mutable-ish
        raise TypeError("Grassmann elements are not hashable")

    def nterms(self) -> int:
        return len(self.terms)

    def degrees(self) -> set:
        return {len(m) for m in self.terms}

    def generators(self) -> set:
        s = set()
        for m in self.terms:
            s.update(m)
        return s

    def is_even(self) -> bool:
        return all(len(m) % 2 == 0 for m in self.terms)

    def is_odd(self) -> bool:
        return all(len(m) % 2 == 1 for m in self.terms)

    # -- derivatives --------------------------------------------------------
    def left_derivative(self, k: int) -> "Grassmann":
        """d_L/d theta_k: bring theta_k to the far left (sign (-1)^position), then drop it."""
        out = Grassmann()
        for m, c in self.terms.items():
            if k in m:
                pos = m.index(k)
                mm = m[:pos] + m[pos + 1:]
                out._iadd_term(mm, c if pos % 2 == 0 else -c)
        return out

    def right_derivative(self, k: int) -> "Grassmann":
        out = Grassmann()
        for m, c in self.terms.items():
            if k in m:
                pos = m.index(k)
                after = len(m) - 1 - pos
                mm = m[:pos] + m[pos + 1:]
                out._iadd_term(mm, c if after % 2 == 0 else -c)
        return out

    def apply_even_derivation(self, image: Callable[[int], Optional["Grassmann"]]) -> "Grassmann":
        """D(theta_1...theta_n) = sum_k theta_1..D(theta_k)..theta_n for an EVEN derivation D
        (D maps generators to odd elements, no signs from passing D through)."""
        out = Grassmann()
        for m, c in self.terms.items():
            for pos, g in enumerate(m):
                img = image(g)
                if img is None or img.nterms() == 0:
                    continue
                left = Grassmann({m[:pos]: 1})
                right = Grassmann({m[pos + 1:]: 1})
                term = (left * img * right).scale(c)
                for mm, cc in term.terms.items():
                    out._iadd_term(mm, cc)
        return out

    def apply_generator_map_derivation(self, gmap: Callable[[int], Optional[int]]) -> "Grassmann":
        """Fast even derivation whose image of every generator is a single generator (or 0)."""
        out = Grassmann()
        for m, c in self.terms.items():
            for pos, g in enumerate(m):
                h = gmap(g)
                if h is None:
                    continue
                s, mm = sort_with_sign(m[:pos] + (h,) + m[pos + 1:])
                if s == 0:
                    continue
                out._iadd_term(mm, c if s > 0 else -c)
        return out

    # -- conjugation --------------------------------------------------------
    def conjugate(self, gconj: Callable[[int], int], cconj: Callable = None) -> "Grassmann":
        """(c theta_i1 ... theta_in)^* = c^* theta_in^* ... theta_i1^*."""
        if cconj is None:
            cconj = default_coeff_conj
        out = Grassmann()
        for m, c in self.terms.items():
            rev = [gconj(g) for g in reversed(m)]
            s, mm = sort_with_sign(rev)
            if s == 0:
                raise ValueError("generator conjugation map is not injective")
            cc = cconj(c)
            out._iadd_term(mm, cc if s > 0 else -cc)
        return out

    def __repr__(self) -> str:
        if not self.terms:
            return "Grassmann(0)"
        items = sorted(self.terms.items())
        return "Grassmann(" + " + ".join("(%s)*%s" % (c, list(m)) for m, c in items[:8]) + \
            (" + ..." if len(items) > 8 else "") + ")"


def default_coeff_conj(c):
    if hasattr(c, "conjugate"):
        try:
            return c.conjugate()
        except TypeError:
            return c
    return c


def bilinear(M, left: Sequence[int], right: Sequence[int], zero_test: Callable = _is_zero_coeff) -> Grassmann:
    """sum_{a,b} M[a][b] theta_{left[a]} theta_{right[b]}."""
    out = Grassmann()
    n1 = len(left)
    n2 = len(right)
    for a in range(n1):
        for b in range(n2):
            c = M[a][b]
            if zero_test(c):
                continue
            s, m = _merge((left[a],), (right[b],))
            if s == 0:
                continue
            out._iadd_term(m, c if s > 0 else -c)
    return out


def linear(v, gens: Sequence[int]) -> Grassmann:
    """sum_a v[a] theta_{gens[a]}."""
    out = Grassmann()
    for a, g in enumerate(gens):
        c = v[a]
        if not _is_zero_coeff(c):
            out._iadd_term((g,), c)
    return out


# ---------------------------------------------------------------------------
# Gaussian rationals (exact complex coefficients)
# ---------------------------------------------------------------------------


class GaussianRational:
    """a + b i with exact rational a, b (any exact rational type)."""

    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = re
        self.im = im

    @staticmethod
    def _c(x) -> "GaussianRational":
        return x if isinstance(x, GaussianRational) else GaussianRational(x, 0)

    def __add__(self, o):
        o = self._c(o)
        return GaussianRational(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __neg__(self):
        return GaussianRational(-self.re, -self.im)

    def __sub__(self, o):
        o = self._c(o)
        return GaussianRational(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return self._c(o) - self

    def __mul__(self, o):
        o = self._c(o)
        return GaussianRational(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def conjugate(self):
        return GaussianRational(self.re, -self.im)

    def __eq__(self, o):
        o = self._c(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):  # pragma: no cover
        return hash((self.re, self.im))

    def __repr__(self):
        return "(%s%+si)" % (self.re, self.im) if self.im != 0 else str(self.re)


# ---------------------------------------------------------------------------
# jet generators
# ---------------------------------------------------------------------------


class JetSpace:
    """Generators theta_{s,a;alpha}: species s (e.g. 'psi', 'psis' = Psi^*), component a,
    sorted derivative multi-index alpha with |alpha| <= max_deriv."""

    def __init__(self, species: Sequence[str], nfield: int = 16, ncoord: int = 8, max_deriv: int = 2):
        self.species = list(species)
        self.nfield = nfield
        self.ncoord = ncoord
        self.max_deriv = max_deriv
        self.alphas: List[Tuple[int, ...]] = [()]
        for k in range(1, max_deriv + 1):
            self.alphas.extend(itertools.combinations_with_replacement(range(ncoord), k))
        self._index: Dict[Tuple[str, int, Tuple[int, ...]], int] = {}
        self._label: List[Tuple[str, int, Tuple[int, ...]]] = []
        for s in self.species:
            for alpha in self.alphas:
                for a in range(nfield):
                    self._index[(s, a, alpha)] = len(self._label)
                    self._label.append((s, a, alpha))

    @property
    def ngen(self) -> int:
        return len(self._label)

    def idx(self, s: str, a: int, alpha: Sequence[int] = ()) -> int:
        return self._index[(s, a, tuple(sorted(alpha)))]

    def gens(self, s: str, alpha: Sequence[int] = ()) -> List[int]:
        return [self.idx(s, a, alpha) for a in range(self.nfield)]

    def label(self, i: int) -> Tuple[str, int, Tuple[int, ...]]:
        return self._label[i]

    def deriv_order(self, i: int) -> int:
        return len(self._label[i][2])

    def total_derivative_map(self, mu: int) -> Callable[[int], Optional[int]]:
        def f(i: int) -> Optional[int]:
            s, a, alpha = self._label[i]
            if len(alpha) >= self.max_deriv:
                raise ValueError("jet space too small for this total derivative")
            return self._index[(s, a, tuple(sorted(alpha + (mu,))))]
        return f

    def total_derivative(self, F: Grassmann, mu: int) -> Grassmann:
        """d_mu on a constant-coefficient element (even derivation on the jet generators)."""
        return F.apply_generator_map_derivation(self.total_derivative_map(mu))

    def conj_map(self, pairs: Dict[str, str]) -> Callable[[int], int]:
        def f(i: int) -> int:
            s, a, alpha = self._label[i]
            return self._index[(pairs[s], a, alpha)]
        return f


# ---------------------------------------------------------------------------
# jet-valued Grassmann elements (coefficients carrying explicit x-dependence)
# ---------------------------------------------------------------------------


class JetGrassmann:
    """F(x) = F0 + sum_l dx^l F_l + ...: a Grassmann element whose coefficients are order-1
    Taylor data at the evaluation point (explicit x-dependence of the coefficient functions).
    ``parts`` maps () and (l,) to Grassmann elements."""

    __slots__ = ("parts",)

    def __init__(self, parts: Dict[Tuple[int, ...], Grassmann]):
        self.parts = parts

    def __add__(self, other: "JetGrassmann") -> "JetGrassmann":
        keys = set(self.parts) | set(other.parts)
        return JetGrassmann({k: self.parts.get(k, Grassmann()) + other.parts.get(k, Grassmann()) for k in keys})

    def __sub__(self, other: "JetGrassmann") -> "JetGrassmann":
        keys = set(self.parts) | set(other.parts)
        return JetGrassmann({k: self.parts.get(k, Grassmann()) - other.parts.get(k, Grassmann()) for k in keys})

    def scale(self, s) -> "JetGrassmann":
        return JetGrassmann({k: v.scale(s) for k, v in self.parts.items()})

    def map(self, f: Callable[[Grassmann], Grassmann]) -> "JetGrassmann":
        return JetGrassmann({k: f(v) for k, v in self.parts.items()})

    def value(self) -> Grassmann:
        return self.parts.get((), Grassmann())

    def left_derivative(self, k: int) -> "JetGrassmann":
        return self.map(lambda v: v.left_derivative(k))

    def total_derivative_at_point(self, js: JetSpace, mu: int) -> Grassmann:
        """(d_mu F)(p) = explicit coefficient derivative + derivation on the field jets."""
        return self.parts.get((mu,), Grassmann()) + js.total_derivative(self.value(), mu)


def euler_lagrange(L: JetGrassmann, js: JetSpace, s: str, a: int) -> Grassmann:
    """E_a = d_L L / d theta_{s,a} - sum_mu d_mu ( d_L L / d theta_{s,a;mu} ), at the point."""
    E = L.value().left_derivative(js.idx(s, a))
    for mu in range(js.ncoord):
        Pi = L.left_derivative(js.idx(s, a, (mu,)))
        E = E - Pi.total_derivative_at_point(js, mu)
    return E


def all_left_derivatives(F: Grassmann) -> Dict[int, Grassmann]:
    """{k: d_L F / d theta_k} for every generator k occurring in F (one pass over F)."""
    out: Dict[int, Grassmann] = {}
    for m, c in F.terms.items():
        for pos, g in enumerate(m):
            d = out.get(g)
            if d is None:
                d = Grassmann()
                out[g] = d
            d._iadd_term(m[:pos] + m[pos + 1:], c if pos % 2 == 0 else -c)
    return out


def euler_lagrange_all(L: JetGrassmann, js: JetSpace, s: str) -> List[Grassmann]:
    """[E_a for a in range(nfield)], identical to ``euler_lagrange`` but with one pass per jet part."""
    dv = {k: all_left_derivatives(v) for k, v in L.parts.items()}
    empty = Grassmann()
    res = []
    for a in range(js.nfield):
        E = dv[()].get(js.idx(s, a), empty).copy()
        for mu in range(js.ncoord):
            g = js.idx(s, a, (mu,))
            pi_val = dv[()].get(g, empty)
            pi_mu = dv.get((mu,), {}).get(g, empty)
            E = E - (pi_mu + js.total_derivative(pi_val, mu))
        res.append(E)
    return res
