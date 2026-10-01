"""Revision theory (sympy side): a small exact CAR (Krein) Fock evaluator for the expectation-value rule.

Modes n = 0..N-1 with metric eps_n = +-1:  {b_n, b_m^dagger} = eps_n delta_nm, {b_n, b_m} = 0, b_n |0> = 0.
A word is a tuple of (n, dagger) pairs; vev(word) = <0| word |0>, computed by anticommuting the
leftmost annihilator to the right (exact, recursive)."""

from functools import lru_cache


def make_vev(eps):
    eps = tuple(eps)

    @lru_cache(maxsize=None)
    def vev(word):
        if not word:
            return 1
        if word[-1][1] is False:  # an annihilator at the right end kills |0>
            return 0
        if word[0][1] is True:  # a creator at the left end is killed by <0|
            return 0
        # word[0] is an annihilator b_n: anticommute it to the right end, where it kills |0>
        n = word[0][0]
        rest = word[1:]
        total = 0
        sign = 1
        for j, (mm, dag) in enumerate(rest):
            if dag and mm == n:
                total += sign * eps[n] * vev(rest[:j] + rest[j + 1:])
            sign = -sign
        return total

    return vev
