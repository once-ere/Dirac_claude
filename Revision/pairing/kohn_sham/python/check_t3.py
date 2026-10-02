#!/usr/bin/env python3
"""Revision/pairing/kohn_sham/python/check_t3.py - independent exact sympy verification of theorem T3 of
Revision/SPEC.md section 9 (the Kohn-Sham level of the pairing of universes of masses {+m, -m}).

T3: the block map (chi, j) -> (sigma2 chi, -j) at the same momentum (the chirality Gamma of the 16-component
orbital in the block basis of Revision/kohn_sham/ks-theory.json), together with the transformed boundary
conditions (brane parities exchanged, tip angle theta -> pi - theta), maps every self-consistent instantaneous
Kohn-Sham state with (m, lambda, theta) onto one with (-m, +lambda, pi - theta), with equal levels, occupations,
Kohn-Sham energy, grand potential and energy-momentum profiles; S and Q change sign.

Written anew (sympy only; no code shared with Revision/pairing/kohn_sham/wolfram/verify_t3.wls or with the
Kohn-Sham verifiers).  Reads Revision/kohn_sham/ks-theory.json (the stated formulas and the block basis V),
Revision/algebra/gammas.json, and - at the end, as data - Revision/pairing/kohn_sham/t3-theory.json (the Wolfram
theorem record) and Revision/kohn_sham/reports/ks-rust-solver.json (a numerical confirmation, not a proof).
Writes Revision/pairing/kohn_sham/reports/python-t3.json (deterministic, LF).

Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially
DEFLATING extra times; x8 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0] (brane y = 0, tip y = -L).
"""

import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
T3DIR = HERE.parent
REV = T3DIR.parent.parent
KS_THEORY = REV / "kohn_sham" / "ks-theory.json"
GAMMAS = REV / "algebra" / "gammas.json"
T3_THEORY = T3DIR / "t3-theory.json"
RUST_REPORT = REV / "kohn_sham" / "reports" / "ks-rust-solver.json"
OUT = T3DIR / "reports" / "python-t3.json"
T0 = time.time()
CHECKS = []

s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
I2, Z2 = sp.eye(2), sp.zeros(2, 2)
y = sp.Symbol("y", real=True)
m, lam, k, eps, th = sp.symbols("m lambda k epsilon theta", real=True)


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print("[%6.1fs] %s %s" % (time.time() - T0, "PASS" if ok else "FAIL", name), flush=True)


def vzero(v):
    return all(sp.simplify(sp.expand(x)) == 0 for x in v)


def h_block(j, M, kap, v, chi):
    """h_j = j[-i sigma1 d_y + M sigma2 + kappa k sigma3] + v  (ks-theory.json blockEquation.hamiltonian)."""
    return j * (-sp.I * s1 * chi.diff(y) + M * s2 * chi + kap * k * s3 * chi) + v * chi


def main():
    ks = json.loads(KS_THEORY.read_text(encoding="utf-8"))
    M = sp.Function("M")(y)
    kap = sp.Function("kappa")(y)
    v = sp.Function("v")(y)
    c1, c2 = sp.Function("c1")(y), sp.Function("c2")(y)
    chi = sp.Matrix([c1, c2])
    # stated formulas are those of the Kohn-Sham record
    stated = ks["blockEquation"]["hamiltonian"].replace(" ", "")
    ok_stated = "h_j=j[-isigma1d/dy+M_eff(y)sigma2+kappa(y)ksigma3]+v_v(y)" in stated

    # 1. block Hamiltonian
    ok = True
    for j in (1, -1):
        lhs = h_block(-j, -M, kap, v, s2 * chi)
        rhs = s2 * h_block(j, M, kap, v, chi)
        ok = ok and vzero(lhs - rhs)
    ctl = not vzero(h_block(-1, M, kap, v, s2 * chi) - s2 * h_block(1, M, kap, v, chi))
    check("T3.block_hamiltonian_map", ok and ctl and ok_stated,
          "with the block Hamiltonian of ks-theory.json blockEquation (h_j = j[-i sigma1 d_y + M_eff sigma2 + kappa k "
          "sigma3] + v_v, stated there and re-typed here), general M(y), kappa(y), v(y), k: h_(-j)(-M) (sigma2 chi) = "
          "sigma2 h_j(M) chi for j = +-1 and arbitrary chi(y): equal level eps, same k and v; control: without M -> -M "
          "the identity fails")

    # 2. ODE matrix
    vv = sp.Symbol("v_v", real=True)
    kp = sp.Symbol("kappa", positive=True)
    Ms = sp.Symbol("M", real=True)
    j_ = sp.Symbol("j", real=True)
    N = lambda jj, MM: MM * s3 - kp * k * s2 + sp.I * jj * (eps - vv) * s1
    check("T3.ode_map", (s2 * N(j_, Ms) * s2 - N(-j_, -Ms)).applyfunc(sp.expand) == Z2,
          "chi' = N chi, N = M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1 (ks-theory.json blockEquation.ode): "
          "sigma2 N_j(M) sigma2 = N_(-j)(-M) exactly")

    # 3. tip condition
    Q = lambda t: sp.cos(t) * s3 + sp.sin(t) * s2
    tip = (s2 * Q(th) * s2 - Q(sp.pi - th)).applyfunc(sp.simplify) == Z2
    e1 = sp.Matrix([1, 0])
    ctl = (I2 - Q(0)) * e1 == sp.zeros(2, 1) and (I2 - Q(0)) * (s2 * e1) != sp.zeros(2, 1) and \
        (I2 - Q(sp.pi)) * (s2 * e1) == sp.zeros(2, 1)
    check("T3.tip_condition_map", tip and ctl,
          "tip (1 - Q(theta)) chi(-L) = 0, Q = cos(theta) sigma3 + sin(theta) sigma2: sigma2 Q(theta) sigma2 = "
          "Q(pi - theta); the canonical theta = 0 goes to theta = pi; control: the image of the theta = 0 solution "
          "(1, 0) violates the untransformed condition and satisfies the transformed one")

    # 4. brane parities, current, norm
    a = sp.symbols("a1:9", real=True)
    ph = sp.Matrix([a[0] + sp.I * a[1], a[2] + sp.I * a[3]])
    ch = sp.Matrix([a[4] + sp.I * a[5], a[6] + sp.I * a[7]])
    cur = lambda jj, p, c: (-sp.I * jj * p.H * s1 * c)[0, 0]
    par = (s2 * (I2 - s3) * s2 - (I2 + s3)) == Z2 and (s2 * e1)[0] == 0 and (s2 * sp.Matrix([0, 1]))[1] == 0
    curok = all(sp.expand(cur(-jj, s2 * ph, s2 * ch) - cur(jj, ph, ch)) == 0 for jj in (1, -1))
    normok = sp.expand(((s2 * ch).H * (s2 * ch))[0, 0] - (ch.H * ch)[0, 0]) == 0
    check("T3.brane_parities_exchanged", par and curok and normok,
          "brane (ASSUMED Z2 orbifold of ks-theory.json): even chi2(0) = 0, odd chi1(0) = 0, i.e. (1 -+ sigma3) "
          "chi(0) = 0; sigma2 (1 - sigma3) sigma2 = 1 + sigma3: the map exchanges the parities (both are part of the "
          "problem); the boundary current -i j phi^dagger sigma1 chi and the norm are invariant under (chi, j) -> "
          "(sigma2 chi, -j), so self-adjointness and the orbital normalisation carry over")

    # 5. per-orbital densities
    def dens(jj, c):
        return [sp.expand((c.H * c)[0, 0]), sp.expand(jj * (c.H * s2 * c)[0, 0]), sp.expand(jj * (c.H * s3 * c)[0, 0]),
                sp.expand((c.H * s3 * c)[0, 0]), sp.expand(jj * (c.H * s1 * c)[0, 0])]
    ok = True
    for jj in (1, -1):
        d0, d1 = dens(jj, ch), dens(-jj, s2 * ch)
        ok = ok and all(sp.expand(d1[i] - sg * d0[i]) == 0 for i, sg in enumerate((1, -1, 1, -1, 1)))
    check("T3.orbital_densities", ok,
          "n_o = chi^dagger chi, s_o = chi^dagger j sigma2 chi, t_o = chi^dagger j sigma3 chi, q_o = chi^dagger "
          "sigma3 chi, c_o = chi^dagger j sigma1 chi (ks-theory.json densities.perOrbital, the common factor P "
          "omitted): under (chi, j) -> (sigma2 chi, -j) n_o, t_o, c_o are invariant and s_o, q_o change sign, for "
          "arbitrary complex chi and both j")

    # 6. mean field
    S, n = sp.symbols("S n", real=True)
    pots = ks["exchange"]["kohnShamPotentials"]
    cM = sp.Rational(pots["Meff_coefficient_of_lambda_S"])
    cV = sp.Rational(pots["vv_coefficient_of_lambda_n"])
    meff = lambda mm, ll, ss: mm + cM * ll * ss
    vvf = lambda ll, nn: cV * ll * nn
    eint = lambda ll, nn, ss: sp.Rational(15, 32) * ll * ss**2 - sp.Rational(1, 32) * ll * nn**2
    ok_e = "(15/32) lambda S^2 - (1/32) lambda n^2" in pots["e_int"]
    ok = sp.expand(meff(-m, lam, -S) + meff(m, lam, S)) == 0 and sp.expand(eint(lam, n, -S) - eint(lam, n, S)) == 0 \
        and sp.expand(sp.diff(eint(lam, n, S), S) - (meff(m, lam, S) - m)) == 0 \
        and sp.expand(sp.diff(eint(lam, n, S), n) - vvf(lam, n)) == 0 and ok_e
    ctl = sp.expand(meff(-m, -lam, -S) + meff(m, lam, S)) != 0
    check("T3.mean_field_map", ok and ctl and (cM, cV) == (sp.Rational(15, 16), sp.Rational(-1, 16)),
          "Kohn-Sham potentials read from ks-theory.json: M_eff = m + %s lambda S, v_v = %s lambda n, e_int = (15/32) "
          "lambda S^2 - (1/32) lambda n^2 (consistent: M_eff - m = d e_int/dS, v_v = d e_int/dn); with S -> -S, n -> n: "
          "M_eff[-m, +lambda, -S] = -M_eff[m, lambda, S], v_v and e_int unchanged; with (-m, -lambda) instead the map "
          "fails (control)" % (cM, cV))

    # 7. energies and energy-momentum profiles for general orbitals of both block types
    w, kap0, T = sp.symbols("w kappa T", positive=True)
    orbs = []
    for o, jj in ((1, 1), (2, -1), (3, 1)):
        r = sp.symbols("r%d_1:5" % o, real=True)
        orbs.append({"j": jj, "chi": sp.Matrix([r[0] + sp.I * r[1], r[2] + sp.I * r[3]]),
                     "eps": sp.Symbol("eps%d" % o, real=True), "f": sp.Symbol("f%d" % o, positive=True),
                     "g": sp.Symbol("g%d" % o, positive=True), "k": sp.Symbol("k%d" % o, positive=True)})
    image = [dict(o, j=-o["j"], chi=s2 * o["chi"]) for o in orbs]

    def profiles(os_, mm, ll):
        nn = sum(w * o["g"] * o["f"] * dens(o["j"], o["chi"])[0] for o in os_)
        ss = sum(w * o["g"] * o["f"] * dens(o["j"], o["chi"])[1] for o in os_)
        qq = sum(w * o["g"] * o["f"] * dens(o["j"], o["chi"])[3] for o in os_)
        me, ve, ei = meff(mm, ll, ss), vvf(ll, nn), eint(ll, nn, ss)
        rho = sum(w * o["g"] * o["f"] * o["eps"] * dens(o["j"], o["chi"])[0] for o in os_) - ei
        p3 = sum(w * o["g"] * o["f"] * kap0 * o["k"] / 3 * dens(o["j"], o["chi"])[2] for o in os_) + ei
        pt = ei
        p8 = sum(w * o["g"] * o["f"] * ((o["eps"] - ve) * dens(o["j"], o["chi"])[0] - me * dens(o["j"], o["chi"])[1]
                                        - kap0 * o["k"] * dens(o["j"], o["chi"])[2]) for o in os_) + ei
        eks = sum(o["g"] * o["f"] * o["eps"] for o in os_) - ei
        ent = sum(-o["g"] * (o["f"] * sp.log(o["f"]) + (1 - o["f"]) * sp.log(1 - o["f"])) for o in os_)
        exx = ei + ll * qq**2 / 32
        return [rho, p3, pt, p8, eks, ent, exx], ss, qq
    pO, SO, QO = profiles(orbs, m, lam)
    pI, SI, QI = profiles(image, -m, lam)
    pC, _, _ = profiles(image, -m, -lam)
    ok = all(sp.expand(a_ - b_) == 0 for a_, b_ in zip(pI, pO)) and sp.expand(SI + SO) == 0 and sp.expand(QI + QO) == 0
    ok = ok and sp.expand(pC[4] - pO[4]) != 0
    check("T3.energies_and_emt_profiles_equal", ok,
          "three general occupied orbitals (blocks j = +1, -1, +1; arbitrary complex chi, level eps, occupation f, "
          "degeneracy g, momentum |k|, weight w): rho = sum w g f eps n_o - e_int, p3 = sum w g f (kappa |k|/3) t_o + "
          "e_int, p_t = e_int, p8 = sum w g f [(eps - v_v) n_o - M_eff s_o - kappa |k| t_o] + e_int (ks-theory.json emt), "
          "the E_KS density sum g f eps - e_int, the entropy and the exact-Fock diagnostic e_int + (lambda/32) Q^2 are "
          "equal for the image with (-m, +lambda) while S and Q change sign; with (-m, -lambda) the E_KS density differs "
          "(control). Equal levels and occupations give equal mu, N, Omega and F")

    # 8. exact k = 0 spectra
    MM, L, yy = sp.symbols("M L yy", positive=True)
    p = sp.sqrt(MM**2 - eps**2)

    def prop(jj, Mv):
        Nk = Mv * s3 + sp.I * jj * eps * s1
        return sp.cosh(p * yy) * I2 + sp.sinh(p * yy) / p * Nk

    e2v = sp.Matrix([0, 1])
    ok = True
    for jj in (1, -1):
        dEven0 = (prop(jj, MM) * e1)[1].subs(yy, -L)
        dOddPi = (prop(-jj, -MM) * e2v)[0].subs(yy, -L)
        dOdd0 = (prop(jj, MM) * e2v)[1].subs(yy, -L)
        dEvenPi = (prop(-jj, -MM) * e1)[0].subs(yy, -L)
        ok = ok and sp.simplify(dEven0 + dOddPi) == 0 and sp.simplify(dOdd0 - dEvenPi) == 0
    dCtl = (prop(-1, -MM) * e2v)[1].subs(yy, -L)
    dE = (prop(1, MM) * e1)[1].subs(yy, -L)
    ctl = sp.simplify(dCtl - dE) != 0 and sp.simplify(dCtl + dE) != 0
    zm = sp.Matrix([0, sp.I * sp.exp(MM * y)])
    zero_mode = (zm.diff(y) - (-MM * s3) * zm).applyfunc(sp.simplify) == sp.zeros(2, 1) and s2 * sp.Matrix([sp.exp(MM * y), 0]) == zm
    check("T3.exact_k0_spectra", ok and ctl and zero_mode,
          "k = 0, v = 0, constant M (ks-theory.json boundaryConditions.exactK0Spectra), chi(y) = exp(N y) chi(0), N^2 = "
          "(M^2 - eps^2) I: the characteristic function of (M, j, even, theta = 0) is minus that of (-M, -j, odd, theta "
          "= pi), that of (M, j, odd, theta = 0) equals that of (-M, -j, even, theta = pi), identically in eps, M, L, "
          "both j: equal spectra level by level; the zero mode (e^(M y), 0) maps to (0, i e^(M y)), the zero mode of "
          "the image; control: with the untransformed tip the image's characteristic function differs")

    # 9. the 16-component chirality
    g = json.loads(GAMMAS.read_text(encoding="utf-8"))

    def mat(x):
        if isinstance(x, dict):
            return sp.Matrix(x["re"]) + sp.I * sp.Matrix(x["im"])
        return sp.Matrix(x)
    G = [mat(x) for x in g["gamma"]]
    Gam = mat(g["Gamma"])
    rows = ks["blockBasis"]["unnormalisedColumns2Sqrt2V"]          # rows = spinor components (ks-theory.json rowsAre)
    V = sp.Matrix([[sp.sympify(rows[r][cc]) for cc in range(16)] for r in range(16)]) / (2 * sp.sqrt(2))
    labels = [tuple(int(x) for x in l) for l in ks["blockBasis"]["labels"]]
    unit = (V.H * V).applyfunc(sp.simplify) == sp.eye(16)
    ok = unit and Gam == sp.diag(*([-1] * 8 + [1] * 8))
    for b, (jj, s2v, s3v) in enumerate(labels):
        bp = labels.index((-jj, s2v, s3v))
        Vb, Vbp = V[:, 2 * b:2 * b + 2], V[:, 2 * bp:2 * bp + 2]
        ok = ok and (Gam * Vb - Vbp * (s2v * s2)).applyfunc(sp.simplify) == sp.zeros(16, 2)
        ok = ok and (Vb.H * G[7] * Vb).applyfunc(sp.simplify) == s3 and (Vb.H * G[7] * G[3] * Vb).applyfunc(sp.simplify) == jj * s1
    check("T3.Gamma_is_the_block_map", ok,
          "block basis V of ks-theory.json (unitary; rows = spinor components) and the chirality Gamma = diag(-I8, I8) "
          "of gammas.json: Gamma V_(j,s2,s3) = V_(-j,s2,s3) (s2 sigma2) for all 8 blocks, with gamma^(x8) = sigma3 and "
          "gamma^(x8) gamma^(x4) = j sigma1 in every block: the 2 x 2 map of T3 is the chirality of the 16-component "
          "Kohn-Sham orbital (up to the phase s2)")

    # 10. the ASSUMED Z2 mirror P_A
    u1, u2 = sp.Function("u1"), sp.Function("u2")
    chiY = sp.Matrix([u1(y), u2(y)])
    Mf, kf, vf = sp.Function("M"), sp.Function("kappa"), sp.Function("v")
    hP = lambda Mv, Kv, Vv, c: (-sp.I * s1 * c.diff(y) + Mv * s2 * c + Kv * k * s3 * c) + Vv * c
    lhs = hP(-Mf(-y), kf(-y), vf(-y), s3 * chiY.subs(y, -y))
    rhs = (s3 * hP(Mf(y), kf(y), vf(y), chiY)).subs(y, -y)
    pa_ok = vzero(lhs - rhs)
    odd = sp.expand(meff(-m, lam, -S) + meff(m, lam, S)) == 0
    n_even = sp.expand(dens(1, s3 * ch)[0] - dens(1, ch)[0]) == 0 and sp.expand(dens(1, s3 * ch)[1] + dens(1, ch)[1]) == 0
    check("T3.z2_mirror_copy_carries_minus_m_plus_lambda", pa_ok and odd and n_even,
          "ASSUMED Z2 orbifold: P_A chi(y) = sigma3 chi(-y) gives h(-M(-y), kappa(-y), v(-y)) P_A chi = P_A h(M, kappa, v) "
          "chi for general functions; n_o is even and s_o odd under sigma3; so the doubled problem is P_A-symmetric "
          "iff M_eff is odd, i.e. iff the mirror copy carries (-m, +lambda)")

    # 11. numerical confirmation (data, not a proof)
    rust = json.loads(RUST_REPORT.read_text(encoding="utf-8"))
    rc = next((c for c in rust.get("checks", []) if c.get("name") == "t3_block_map_solver_selftest"), None)
    rok = rc is not None and str(rc.get("verdict", rc.get("passed"))).upper() in ("PASS", "TRUE") and \
        "tip theta = pi" in rc.get("detail", "") and "NOT a proof" in rc.get("detail", "")
    check("T3.rust_selftest_numerical_confirmation", rok,
          "Revision/kohn_sham/reports/ks-rust-solver.json records t3_block_map_solver_selftest as passing: (m, lambda, "
          "theta = 0) and (-m, lambda, theta = pi) solved independently give equal levels, occupations, E_KS and "
          "energy-momentum integrals and opposite S, with a failing negative control for the untransformed tip; this is "
          "a numerical confirmation of the transformed boundary condition theta -> pi - theta, not part of the proof")

    # 12. comparison with the Wolfram theorem record (read only)
    if T3_THEORY.exists():
        thr = json.loads(T3_THEORY.read_text(encoding="utf-8"))
        names = {c["name"] for c in CHECKS if c["verdict"] == "PASS"}
        pairs = [("T3_block_hamiltonian_map", "T3.block_hamiltonian_map"), ("T3_ode_map", "T3.ode_map"),
                 ("T3_tip_condition_map", "T3.tip_condition_map"),
                 ("T3_brane_parities_exchanged", "T3.brane_parities_exchanged"),
                 ("T3_orbital_densities", "T3.orbital_densities"), ("T3_mean_field_map", "T3.mean_field_map"),
                 ("T3_energies_and_emt_profiles_equal", "T3.energies_and_emt_profiles_equal"),
                 ("T3_exact_k0_spectra", "T3.exact_k0_spectra"), ("T3_Gamma_is_the_block_map", "T3.Gamma_is_the_block_map"),
                 ("T3_z2_mirror_copy_carries_minus_m_plus_lambda", "T3.z2_mirror_copy_carries_minus_m_plus_lambda")]
        ver = thr.get("verification", [])
        ok = "all checks" in thr.get("status", "") and all(wn in ver and sn in names for wn, sn in pairs) and len(ver) == len(pairs)
        st = " ".join(thr.get("statement", []))
        ok = ok and "(-m, +lambda, Pi - theta)" in st and "EQUAL Kohn-Sham levels" in st and "S -> -S" in st
        check("compare.t3_theory.theorem", ok,
              "the Wolfram record Revision/pairing/kohn_sham/t3-theory.json states T3 for (m, lambda, theta) -> (-m, "
              "+lambda, pi - theta) with equal levels and energies and S -> -S, status '%s'; each of its %d verification "
              "checks has an independent passing sympy counterpart here: %s"
              % (thr.get("status"), len(ver), ", ".join("%s <-> %s" % p_ for p_ in pairs)))
        ne = " ".join(thr.get("not_established", [])).lower()
        topics = ["creation process", "time-dependent", "assumed", "correlation", "independently quantised", "back-reaction"]
        check("compare.t3_theory.not_established", all(t_ in ne for t_ in topics),
              "the Wolfram record's list of what T3 does not establish covers: " + ", ".join(topics))
    else:
        CHECKS.append({"name": "compare.t3_theory", "verdict": "pending",
                       "detail": "Revision/pairing/kohn_sham/t3-theory.json does not exist yet; run the Wolfram verifier first"})

    n_pass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
    n_fail = sum(1 for c in CHECKS if c["verdict"] == "FAIL")
    report = {
        "report": "Revision/pairing/kohn_sham/reports/python-t3.json",
        "producer": "Revision/pairing/kohn_sham/python/check_t3.py",
        "spec": "Revision/SPEC.md section 9, theorem T3 (the Kohn-Sham level)",
        "independence": "sympy only; no code shared with Revision/pairing/kohn_sham/wolfram/verify_t3.wls or with the "
                        "Kohn-Sham verifiers; ks-theory.json is read for its stated formulas and block basis",
        "inputs": ["Revision/kohn_sham/ks-theory.json", "Revision/algebra/gammas.json",
                   "Revision/pairing/kohn_sham/t3-theory.json (comparison, read only)",
                   "Revision/kohn_sham/reports/ks-rust-solver.json (numerical confirmation, read only)"],
        "theorem": "T3: (chi, j) -> (sigma2 chi, -j) (Psi_16 -> Gamma Psi_16) with brane parities exchanged and tip "
                   "angle theta -> pi - theta maps every self-consistent instantaneous Kohn-Sham state with (m, lambda, "
                   "theta) onto one with (-m, +lambda, pi - theta): equal levels, occupations, E_KS, Omega, F and "
                   "energy-momentum profiles; S -> -S, Q -> -Q. Hypotheses: those of t3-theory.json (Kohn-Sham problem "
                   "and functional of ks-theory.json, ASSUMED Z2 brane, chosen tip, Mermin occupations with the filling "
                   "convention, same remaining data)",
        "counts": {"pass": n_pass, "fail": n_fail, "pending": sum(1 for c in CHECKS if c["verdict"] == "pending")},
        "checks": CHECKS,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes((json.dumps(report, indent=2, ensure_ascii=True) + "\n").encode("utf-8"))
    print("pass %d fail %d; %.1fs; wrote %s" % (n_pass, n_fail, time.time() - T0, OUT), flush=True)
    return 0 if n_fail == 0 and n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
