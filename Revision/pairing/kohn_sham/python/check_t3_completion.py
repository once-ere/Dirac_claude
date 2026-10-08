#!/usr/bin/env python3
"""Revision/pairing/kohn_sham/python/check_t3_completion.py - independent exact sympy verification of the completion of
theorem T3 (Revision/SPEC.md section 9, the Kohn-Sham level of the pairing of universes of masses {+m, -m}).

The completion (Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls, record t3-completion.json) adds three exact
checks to T3 (t3-theory.json, unchanged): the Kohn-Sham potentials read from ks-theory.json, the filling convention
carried onto the -M member, and the 16-component expectation-value (Krein) rule (statement S6: every component of the
energy-momentum tensor and the current are equal for the pair).  This script re-derives the three anew in sympy (no
code shared with the Wolfram script), confirms that the T3 reports still pass, reads the numerical demonstrations of
Revision/pairing/kohn_sham/numerics as data (not a proof) and compares with the Wolfram completion record.

Inputs: Revision/kohn_sham/ks-theory.json, Revision/algebra/gammas.json; as data: Revision/pairing/kohn_sham/
t3-theory.json, t3-completion.json, reports/wolfram-t3.json, python-t3.json, wolfram-t3-completion.json,
t3-rust-demo.json, t3-reference-demo.json.  Writes Revision/pairing/kohn_sham/reports/python-t3-completion.json
(deterministic, LF).  Exit 0 iff every check passes.
Run order: verify_t3.wls, check_t3.py, verify_t3_completion.wls, numerics/t3_rust_demo.py,
numerics/t3_reference_demo.py, then this script.

Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra
times; x8 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0] (brane y = 0, tip y = -L).  The Kohn-Sham history
a4 = A H x4 used by the demonstrations is a PRESCRIBED BACKGROUND (ks-theory.json adiabaticity.historyStatus).
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
REPORTS = T3DIR / "reports"
OUT = REPORTS / "python-t3-completion.json"
T0 = time.time()
CHECKS = []

s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)
y = sp.Symbol("y", real=True)


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print("[%6.1fs] %s %s" % (time.time() - T0, "PASS" if ok else "FAIL", name), flush=True)


def tip(theta):
    return sp.cos(theta) * s3 + sp.sin(theta) * s2


def cmat(x):
    if isinstance(x, dict):
        return sp.Matrix(x["re"]) + sp.I * sp.Matrix(x["im"])
    return sp.Matrix(x)


def load(p):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def main():
    ks = json.loads(KS_THEORY.read_text(encoding="utf-8"))

    # 1. the Kohn-Sham potentials of ks-theory.json
    pots = ks["exchange"]["kohnShamPotentials"]
    cM, cV = sp.Rational(pots["Meff_coefficient_of_lambda_S"]), sp.Rational(pots["vv_coefficient_of_lambda_n"])
    m, lam, S, n = sp.symbols("m lambda S n", real=True)
    meff = lambda mm, ll, ss: mm + cM * ll * ss
    vv = lambda ll, nn: cV * ll * nn
    eint = sp.Rational(15, 32) * lam * S**2 - sp.Rational(1, 32) * lam * n**2
    ok = (cM, cV) == (sp.Rational(15, 16), sp.Rational(-1, 16))
    ok = ok and "(15/32) lambda S^2 - (1/32) lambda n^2" in pots["e_int"] and "m + (15/16) lambda S(y)" in pots["Meff"] \
        and "-lambda n(y)/16" in pots["vv"]
    ok = ok and sp.expand(sp.diff(eint, S) - (meff(m, lam, S) - m)) == 0 and sp.expand(sp.diff(eint, n) - vv(lam, n)) == 0
    ok = ok and sp.expand(meff(-m, lam, -S) + meff(m, lam, S)) == 0 and sp.expand(eint.subs(S, -S) - eint) == 0 \
        and not vv(lam, n).has(S)
    ctl = sp.expand(meff(-m, -lam, -S) + meff(m, lam, S)) != 0
    check("T3C.mean_field_coefficients_from_ks_theory", ok and ctl,
          "read from ks-theory.json exchange.kohnShamPotentials: M_eff = m + %s lambda S, v_v = %s lambda n, e_int = (15/32) "
          "lambda S^2 - (1/32) lambda n^2; M_eff - m = d e_int/dS, v_v = d e_int/dn; M_eff[-m, +lambda, -S] = "
          "-M_eff[m, lambda, S], e_int even in S, v_v free of S; control: (-m, -lambda) does not give -M_eff" % (cM, cV))

    # 2. the filling convention on the image
    M = sp.Symbol("M", positive=True)
    L = sp.Symbol("L", positive=True)
    z0 = sp.Matrix([sp.exp(M * y), 0])
    zI = s2 * z0
    h0 = lambda jj, MM, c: jj * (-sp.I * s1 * c.diff(y) + MM * s2 * c)
    zero = sp.zeros(2, 1)
    ok = zI == sp.Matrix([0, sp.I * sp.exp(M * y)])
    ok = ok and all(h0(jj, M, z0).applyfunc(sp.simplify) == zero and h0(-jj, -M, zI).applyfunc(sp.simplify) == zero
                    for jj in (1, -1))
    ok = ok and z0[1] == 0 and zI[0] == 0
    ok = ok and ((I2 - tip(0)) * z0.subs(y, -L)).applyfunc(sp.simplify) == zero
    ok = ok and ((I2 - tip(sp.pi)) * zI.subs(y, -L)).applyfunc(sp.simplify) == zero
    ctl = ((I2 - tip(0)) * zI.subs(y, -L)).applyfunc(sp.simplify) != zero
    ok = ok and sp.simplify((zI.H * zI)[0, 0] - sp.exp(2 * M * y)) == 0
    # the continuation in lambda: S1 at every coupling lambda' and any S(y)
    lp, m0, k = sp.symbols("lambda_p m0 k", real=True)
    Sf, kap, v = sp.Function("S")(y), sp.Function("kappa")(y), sp.Function("v")(y)
    chi = sp.Matrix([sp.Function("c1")(y), sp.Function("c2")(y)])
    hB = lambda jj, MM, c: jj * (-sp.I * s1 * c.diff(y) + MM * s2 * c + kap * k * s3 * c) + v * c
    Mp = m0 + cM * lp * Sf
    path = all((hB(-jj, -Mp, s2 * chi) - s2 * hB(jj, Mp, chi)).applyfunc(sp.expand) == zero for jj in (1, -1))
    check("T3C.filling_convention_mapped", ok and ctl and path,
          "the filling CONVENTION (H5: positive lambda = 0 branch plus the k = 0 brane zero modes, followed continuously in "
          "lambda) is carried onto the image: sigma2 h_j(m + (15/16) lambda' S) = h_(-j)(-(m + (15/16) lambda' S)) sigma2 "
          "for every lambda' and any S(y) (both j), so eps > 0 at lambda = 0 is kept and the map commutes with the "
          "continuation; the zero mode (e^(M y), 0) of (M, j, even, theta = 0) maps to (0, i e^(M y)), a zero mode of "
          "h_(-j)(-M) with odd parity (a(0) = 0) and the transformed tip theta = pi (a(-L) = 0), brane-localised "
          "(|chi|^2 = e^(2 M y)); control: it violates the untransformed tip")

    # 3. the 16-component expectation-value (Krein) rule
    g = json.loads(GAMMAS.read_text(encoding="utf-8"))
    G = [cmat(x) for x in g["gamma"]]
    Gam, Bm, Cm = cmat(g["Gamma"]), cmat(g["B"]), cmat(g["C"])
    I16 = sp.eye(16)
    Sab = [[(G[a] * G[b] - G[b] * G[a]) / 4 for b in range(8)] for a in range(8)]
    conj = lambda X: Gam * X * Gam
    gen = Gam * Gam == I16 and conj(Bm) == -Bm and conj(Cm) == Cm and all(conj(G[a]) == -G[a] for a in range(8)) and \
        all(conj(Sab[a][b]) == Sab[a][b] for a in range(8) for b in range(8))
    u = sp.Matrix(sp.symbols("u0:16"))
    ub = sp.Matrix(sp.symbols("ub0:16")).T
    rho_ok = ((Gam * u) * (ub * Gam) * Bm + Gam * (u * ub) * Bm * Gam).applyfunc(sp.expand) == sp.zeros(16, 16)

    def sign(X):
        Y = -conj(X)
        return 1 if Y == X else (-1 if Y == -X else 0)
    sig = sign(Bm) == 1 and sign(Cm) == -1 and sign(Bm * G[7]) == -1 and all(sign(Cm * G[a]) == 1 for a in range(8))
    sig = sig and all(sign(Cm * G[a] * Sab[b][c]) == 1 for a in range(8) for b in range(8) for c in range(8))
    rule = "rho = sum_occ f u u^dagger B" in ks["exchange"]["expectationRule"]
    check("T3C.krein_rule_16_component", gen and rho_ok and sig and rule,
          "gammas.json gamma^(x1..x8), B, C, Gamma and the expectation rule rho = sum f u u^dagger B (ks-theory.json "
          "exchange.expectationRule): Gamma^2 = 1, Gamma B Gamma = -B, Gamma C Gamma = C, Gamma gamma^a Gamma = -gamma^a, "
          "Gamma S^ab Gamma = S^ab; (Gamma u)(Gamma u)^dagger B = -Gamma (u u^dagger B) Gamma for a general u, so <X>' = "
          "-Tr(Gamma X Gamma rho): n = <B> even, S = <C> and Q = <B gamma^(x8)> odd, the kinetic bilinears C gamma^a and "
          "C gamma^a S^bc (8 + 512) even: with (m, lambda) -> (-m, +lambda) every component of the 16-component "
          "energy-momentum tensor and the current are unchanged (S6)")

    # 4. the T3 reports themselves (data)
    wt, pt, th = load(REPORTS / "wolfram-t3.json"), load(REPORTS / "python-t3.json"), load(T3DIR / "t3-theory.json")
    ok = wt is not None and pt is not None and th is not None
    ok = ok and wt["summary"]["failed"] == 0 and wt["summary"]["passed"] == wt["summary"]["total"] == 10
    ok = ok and pt["counts"]["fail"] == 0 and pt["counts"]["pending"] == 0 and pt["counts"]["pass"] == 13
    ok = ok and th["status"] == "all checks of the report passed" and th["verification"] == [c["name"] for c in wt["checks"]]
    check("T3C.t3_reports_pass", ok,
          "theorem T3 itself: reports/wolfram-t3.json %s/%s PASS, reports/python-t3.json %s/13 PASS, t3-theory.json status "
          "'%s' with the 10 Wolfram check names; the completion adds to T3 and changes none of its files"
          % (wt["summary"]["passed"] if wt else "-", wt["summary"]["total"] if wt else "-",
             pt["counts"]["pass"] if pt else "-", th["status"] if th else "-"))

    # 5. the numerical demonstrations (data, not a proof)
    for fname, label, need in (
            ("t3-rust-demo.json", "T3C.rust_demo_numerical_demonstration",
             ("t3_equal_ground_states", "t3_equal_thermal_states", "negative_control_untransformed_tip",
              "negative_control_lambda_sign", "plus_reproduces_canonical_matrix", "history_is_a_prescribed_background")),
            ("t3-reference-demo.json", "T3C.reference_demo_numerical_demonstration",
             ("image_frame_theta_pi", "t3_equal_ground_states", "t3_equal_thermal_states",
              "negative_control_untransformed_tip", "reference_image_equals_rust_image", "history_is_a_prescribed_background"))):
        dm = load(REPORTS / fname)
        if dm is None:
            CHECKS.append({"name": label, "verdict": "pending", "detail": "reports/%s does not exist yet" % fname})
            continue
        names = {c["name"]: c["verdict"] for c in dm.get("checks", [])}
        ok = dm["summary"]["fail"] == 0 and all(names.get(x) == "PASS" for x in need) and \
            "PRESCRIBED BACKGROUND" in dm.get("background", "")
        check(label, ok,
              "Revision/pairing/kohn_sham/reports/%s (%d states): %d/%d checks PASS, including %s; the slices belong to "
              "the PRESCRIBED BACKGROUND history a4 = A H x4; a numerical demonstration of T3 (+M universe (m, lambda, "
              "tip 0) = -M universe (-m, +lambda, tip pi), the untransformed tip as negative control), not a proof"
              % (fname, dm.get("states", 0), dm["summary"]["pass"], dm["summary"]["checks"], ", ".join(need)))

    # 6. comparison with the Wolfram completion record
    rec, wr = load(T3DIR / "t3-completion.json"), load(REPORTS / "wolfram-t3-completion.json")
    if rec is None or wr is None:
        CHECKS.append({"name": "compare.t3_completion", "verdict": "pending",
                       "detail": "run Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls first"})
    else:
        pairs = [("T3C_mean_field_coefficients_from_ks_theory", "T3C.mean_field_coefficients_from_ks_theory"),
                 ("T3C_filling_convention_mapped", "T3C.filling_convention_mapped"),
                 ("T3C_krein_rule_16_component", "T3C.krein_rule_16_component")]
        passed = {c["name"] for c in CHECKS if c["verdict"] == "PASS"}
        ok = rec["status"] == "all checks of the report passed" and wr["summary"]["failed"] == 0
        ok = ok and rec["verification"] == [p[0] for p in pairs] and all(p[1] in passed for p in pairs)
        ok = ok and any(s.startswith("S6:") for s in rec["statement"]) and "PRESCRIBED BACKGROUND" in rec["background"]
        ne = " ".join(rec["not_established"]).lower()
        topics = ["creation process", "prescribed background", "assumed", "convention", "independently quantised",
                  "not as a proof"]
        ok = ok and all(t in ne for t in topics)
        check("compare.t3_completion", ok,
              "the Wolfram completion record Revision/pairing/kohn_sham/t3-completion.json (status '%s', %d/%d checks of "
              "reports/wolfram-t3-completion.json) states S6 and the PRESCRIBED BACKGROUND; each Wolfram check has an "
              "independent passing sympy counterpart here: %s; its list of what is not established covers: %s"
              % (rec["status"], wr["summary"]["passed"], wr["summary"]["total"],
                 ", ".join("%s <-> %s" % p for p in pairs), ", ".join(topics)))

    n_pass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
    n_fail = sum(1 for c in CHECKS if c["verdict"] == "FAIL")
    report = {
        "report": "Revision/pairing/kohn_sham/reports/python-t3-completion.json",
        "producer": "Revision/pairing/kohn_sham/python/check_t3_completion.py",
        "spec": "Revision/SPEC.md section 9, theorem T3 (the Kohn-Sham level): completion",
        "independence": "sympy only; no code shared with Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls",
        "background": "T3 holds slice by slice; the history a4 = A H x4 of the numerical demonstrations (extra times x5, "
                      "x6, x7 deflating) is a PRESCRIBED BACKGROUND (ks-theory.json adiabaticity.historyStatus; "
                      "Revision/field_equations_a4/reports/ks-source-conditions.json)",
        "counts": {"pass": n_pass, "fail": n_fail, "pending": sum(1 for c in CHECKS if c["verdict"] == "pending")},
        "checks": CHECKS,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes((json.dumps(report, indent=2, ensure_ascii=True) + "\n").encode("utf-8"))
    print("pass %d fail %d; %.1fs; wrote %s" % (n_pass, n_fail, time.time() - T0, OUT), flush=True)
    return 0 if n_fail == 0 and n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
