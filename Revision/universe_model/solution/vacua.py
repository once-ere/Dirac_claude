"""Revision/universe_model/solution/vacua.py - the late-time vacua of UM-1, their stability and the slow deflation of
the block, from the record's full Einstein-Lovelock background equations
(Revision/field_equations_a4/a4-equations.json, generalSource) with general weights alpha_k = w_k H^(2-2k), w1 = 1.

The static-block slicing: a4' = A (constant), a4'' = 0, u = b4'/b4 = 2A (h4 = u/2 - a4' = 0, so k = e^{2a4}/b4 is
constant), v = u' = 0.  Then (exact, part 1) the three components are
    F4 = -3 G(k) A^2 + 6 H^2 k (1 - 2 w2 k) + Lambda + kappa rho,      G(k) = 1 - 24 w2 k + 72 w3 k^2,
    F1 = the same with -kappa p3 in place of kappa rho,
    F0 = 6 (12 w2 k - 1) A^2 - 12 (w2 - 18 w3 k) A^4/H^2 + 3 H^2 k + Lambda - kappa p0,
so G(k) is the ratio of the effective four-dimensional Newton constant to that of Einstein gravity (G = 1 for
w2 = w3 = 0): G > 0 attractive gravity, G < 0 repulsive (the x4 constraint reads 3 G A^2 = Lambda_eff + kappa rho).

Parts: 1 the exact static-block forms; 2 the static vacuum (rho = p3 = p0 = 0): k0 = 1/(4 w2), Lambda0 = -3H^2/(4 w2)
and G(k0) = -5 + 9 w3/(2 w2^2); 3 the linear stability for GENERAL weights: the characteristic polynomial and the
block mode lambda^2 = k0 G(k0) H^2/4 (a theorem of the homogeneous reduction: attractive gravity <=> exponentially
unstable block); 4 the author's weights (1, 1/32, 1/1152) and the benchmark (1, 1/32, 1/768); 5 the de Sitter family
near the vacuum and the quasi-static tracking of the block (its slow deflation)."""
import json
from pathlib import Path

import sympy as sp

REV = Path(__file__).resolve().parents[2]
ad1, ad2, uu, vv, kk, H, Lam, kappa, rho, p3, p0 = sp.symbols("ad1 ad2 uu vv kk H Lam kappa rho p3 p0", real=True)
a1, a2, a3 = sp.symbols("alpha1 alpha2 alpha3", real=True)
LOC = {"ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk, "H": H, "Lam": Lam, "kappa": kappa, "rho": rho, "p3": p3,
       "p0": p0, "alpha1": a1, "alpha2": a2, "alpha3": a3}
W2, W3, A, K = sp.symbols("w2 w3 A k", real=True)
AUTHOR = (sp.Rational(1, 32), sp.Rational(1, 1152))
BENCHMARK = (sp.Rational(1, 32), sp.Rational(1, 768))      # w3 = 4 w2^2/3: G(k0) = 1


def raw_components():
    """(F4, F1, F0) = lhs - rhs of the x4 constraint, the x1 and the x0 components of the record (alpha_k symbolic)"""
    gs = json.loads((REV / "field_equations_a4" / "a4-equations.json").read_text(encoding="utf-8"))["generalSource"]
    out = []
    for key in ("constraint_x4", "space_x1_eq_x2_eq_x3", "hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7"):
        lhs, rhs = gs[key]["input"].replace("^", "**").split("==")
        out.append(sp.expand(sp.sympify(lhs, locals=LOC) - sp.sympify(rhs, locals=LOC)))
    return out


def weights(w2, w3):
    return {a1: 1, a2: w2 / H ** 2, a3: w3 / H ** 4}


def components(w2=AUTHOR[0], w3=AUTHOR[1]):
    return [sp.expand(F.subs(weights(w2, w3))) for F in raw_components()]


def gfac(k, w2, w3):
    return 1 - 24 * w2 * k + 72 * w3 * k ** 2


def static_block_forms():
    """part 1: the components on the static-block slicing with general w2, w3, and the stated closed forms"""
    F = components(W2, W3)
    sub = {ad1: A, uu: 2 * A, vv: 0, ad2: 0, kk: K}
    got = [sp.expand(f.subs(sub)) for f in F]
    G = gfac(K, W2, W3)
    want = [-3 * G * A ** 2 + 6 * H ** 2 * K * (1 - 2 * W2 * K) + Lam + kappa * rho,
            -3 * G * A ** 2 + 6 * H ** 2 * K * (1 - 2 * W2 * K) + Lam - kappa * p3,
            6 * (12 * W2 * K - 1) * A ** 2 - 12 * (W2 - 18 * W3 * K) * A ** 4 / H ** 2 + 3 * H ** 2 * K + Lam - kappa * p0]
    ok = all(sp.simplify(g - w) == 0 for g, w in zip(got, want))
    return ok, got


def block_mode(w2, w3):
    """part 3: linearise the x1 and x0 components (solved for a4'', v) and k' = k (2 a4' - u) about the static vacuum
    in (a4', u, delta k); return the matrix, its characteristic polynomial and the eigenvalues"""
    F4, F1, F0 = components(w2, w3)
    k0, L0 = 1 / (4 * w2), -3 * H ** 2 / (4 * w2)
    e1, e2, e3, eps, lam = sp.symbols("e1 e2 e3 eps lam")
    lin = {ad1: eps * e1, uu: eps * e2, kk: k0 + eps * e3, Lam: L0, rho: 0, p3: 0, p0: 0}
    G1, G0, G4 = [sp.expand(f.subs(lin)) for f in (F1, F0, F4)]
    J = sp.Matrix([[sp.diff(G1, ad2), sp.diff(G1, vv)], [sp.diff(G0, ad2), sp.diff(G0, vv)]]).subs(eps, 0)
    rest = sp.Matrix([sp.diff(G1.subs({ad2: 0, vv: 0}), eps).subs(eps, 0),
                      sp.diff(G0.subs({ad2: 0, vv: 0}), eps).subs(eps, 0)])
    sol = sp.simplify(-J.inv() * rest)
    M = sp.Matrix([[sp.diff(sol[0], x) for x in (e1, e2, e3)], [sp.diff(sol[1], x) for x in (e1, e2, e3)],
                   [2 * k0, -k0, 0]]).applyfunc(sp.simplify)
    cp = sp.factor(M.charpoly(lam).as_expr())
    constraint_lin = sp.simplify(sp.diff(G4, eps).subs(eps, 0))
    return M, cp, lam, constraint_lin, sp.simplify(J.det())


def analyse():
    res = {}
    ok, forms = static_block_forms()
    res["part1_static_block_forms"] = {"closed_forms_hold": bool(ok), "F4": sp.sstr(sp.collect(forms[0], A)),
                                       "F1": sp.sstr(sp.collect(forms[1], A)), "F0": sp.sstr(sp.collect(forms[2], A))}
    # part 2: static vacuum for general weights
    s = sp.solve([forms[0].subs({A: 0, rho: 0}), forms[2].subs({A: 0, p0: 0})], [K, Lam], dict=True)
    s = [x for x in s if x[K] != 0]
    Gk0 = sp.simplify(gfac(1 / (4 * W2), W2, W3))
    res["part2_static_vacuum"] = {"solutions": [{"k0": sp.sstr(x[K]), "Lambda0": sp.sstr(x[Lam])} for x in s],
                                  "unique_nonzero": len(s) == 1, "G_k0": sp.sstr(Gk0)}
    # part 3: general stability
    M, cp, lam, cl, detJ = block_mode(W2, W3)
    lam2 = sp.solve(sp.expand(cp * 32 * W2 ** 3 / lam), lam ** 2)
    pred = sp.Rational(1, 4) * (1 / (4 * W2)) * Gk0 * H ** 2
    res["part3_block_mode_general"] = {"matrix": sp.sstr(M), "charpoly": sp.sstr(cp), "lambda_squared": sp.sstr(lam2),
                                       "lambda2_equals_k0_G_H2_over_4": bool(len(lam2) == 1 and sp.simplify(lam2[0] - pred) == 0),
                                       "constraint_linearised": sp.sstr(cl), "det_J": sp.sstr(detJ)}
    # part 4: the author's weights and the benchmark
    for tag, (w2, w3) in (("author", AUTHOR), ("benchmark", BENCHMARK)):
        k0 = 1 / (4 * w2)
        Mx, cpx, lamx, clx, _ = block_mode(w2, w3)
        ev = {sp.sstr(k): int(v) for k, v in Mx.eigenvals().items()}
        Gv = gfac(k0, w2, w3)
        res["part4_" + tag] = {"w": ["1", sp.sstr(w2), sp.sstr(w3)], "k0": sp.sstr(k0), "Lambda0": sp.sstr(-3 * H ** 2 * k0),
                               "G_k0": sp.sstr(Gv), "eigenvalues": ev,
                               "gravity": "attractive" if Gv > 0 else ("repulsive" if Gv < 0 else "degenerate"),
                               "block": "unstable (real eigenvalue)" if Gv > 0 else ("stable (oscillatory)" if Gv < 0 else "degenerate")}
    # the band of k with attractive gravity for the author's weights, and the author's Lambda = -10 H^2
    roots = sp.solve(gfac(K, *AUTHOR), K)
    res["part4_author_attractive_band"] = {"G_zeros": [sp.sstr(r) for r in roots], "G_zeros_num": [float(r) for r in roots]}
    kq = sp.solve(forms[2].subs({A: 0, p0: 0, Lam: -10 * H ** 2}), K)[0]
    Leff = sp.simplify((forms[0].subs({A: 0, rho: 0, Lam: -10 * H ** 2, K: kq})).subs({W2: AUTHOR[0], W3: AUTHOR[1]}))
    res["part4_author_Lambda_m10"] = {"k_quasistatic": sp.sstr(kq), "Lambda_eff": sp.sstr(Leff),
                                      "G": sp.sstr(gfac(kq, *AUTHOR))}
    # part 5: near the vacuum with sources, A small: F4 -> 3 G(k0) A^2 = dLam + kappa rho (+ O(dk^2)), F0 -> dk
    dL, dk = sp.symbols("dLam dk", real=True)
    k0 = 1 / (4 * W2)
    near4 = sp.expand(forms[0].subs({K: k0 + dk, Lam: -3 * H ** 2 * k0 + dL}))
    near0 = sp.expand(forms[2].subs({K: k0 + dk, Lam: -3 * H ** 2 * k0 + dL}))
    lin4 = sp.expand(near4.subs(dk, 0)) + sp.diff(near4, dk).subs({dk: 0}) * dk
    dk_qs = sp.solve(sp.expand(near0.subs({A: A}).series(A, 0, 4).removeO()).subs(dk, dk), dk)
    # the A^2 term of F0 at k0 + dk, to first order: 6 (12 w2 k0 - 1) A^2 = 12 A^2
    f0_lin = sp.expand(6 * (12 * W2 * k0 - 1) * A ** 2 + 3 * H ** 2 * (k0 + dk) - 3 * H ** 2 * k0 + dL - kappa * p0)
    dk_track = sp.solve(f0_lin, dk)[0]
    res["part5_near_vacuum"] = {"F4_to_first_order_in_dk": sp.sstr(sp.collect(sp.simplify(lin4), [A, dk])),
                                "dF4_ddk_at_k0": sp.sstr(sp.simplify(sp.diff(near4, dk).subs({dk: 0, A: 0}))),
                                "dk_quasistatic": sp.sstr(dk_track),
                                "deflation": "h4 = -k'/(2k) = -(dk_track)'/(2 k0): with dLam, p0 constant, h4 = (4/k0) A A'/H^2 "
                                             "< 0 while A decreases (the extra times keep deflating, slowly)"}
    return res


if __name__ == "__main__":
    r = analyse()
    print(json.dumps(r, indent=1, default=str))
