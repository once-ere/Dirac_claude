#!/usr/bin/env python3
"""Revision/pairing/kohn_sham/numerics/t3_rust_demo.py - numerical demonstration of theorem T3 (SPEC section 9,
the Kohn-Sham level of the pairing of universes of masses {+m, -m}) with the Revision Rust Kohn-Sham solver.

A demonstration, NOT a proof: T3 is proved exactly by Revision/pairing/kohn_sham/wolfram/verify_t3.wls and
independently by Revision/pairing/kohn_sham/python/check_t3.py.  This script solves, with the `single` subcommand of
the Rust solver (Revision/kohn_sham/solver), for every state of the canonical matrix of Revision/kohn_sham:

  plus     the +M universe:  (m, lambda), tip theta = 0           (the canonical boundary conditions)
  image    the -M universe:  (-m, +lambda), tip theta = pi        (the T3 image: transformed tip, brane parities
                                                                    exchanged by the map, solved independently)
  control  negative control: (-m, +lambda), tip theta = 0          (the UNtransformed boundary condition)

and compares them: T3 predicts EQUAL levels (sector (n2, j, parity) of plus <-> sector (n2, -j, other parity) of
image), occupations, Kohn-Sham energy, chemical potential, entropy, grand potential, free energy, energy-momentum
integrals and profiles, with S, Q and M_eff changing sign; the control must differ.  A second control compares plus
with the image of the opposite coupling, (-m, -lambda, pi) (the T1 parameter map): it must differ too.

States: the slices a4,0 in {0, 0.5, 1, 1.5, 2} of the history a4 = A H x4 (A = 1) with the extra times x5, x6, x7
DEFLATING exponentially (scale factor e^{-a4} sin^{1/6} z).  This history is a PRESCRIBED BACKGROUND
(ks-theory.json adiabaticity.historyStatus): the Kohn-Sham states violate the a4 source conditions
(Revision/field_equations_a4/reports/ks-source-conditions.json), so the gas is a test field without back-reaction.
T3 holds slice by slice; it does not use the history.  N and lambda are those of the canonical matrix
(Revision/kohn_sham/results/parameters.json): 75 ground states and 135 thermal (Mermin) states.

Usage (from the repository root; the solver built from the committed sources, e.g.
  cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml):
  python Revision/pairing/kohn_sham/numerics/t3_rust_demo.py --solver <path to revision_ks_solver> --work <scratch>
         [--jobs 10]
Writes (deterministic, LF): Revision/pairing/kohn_sham/numerics/results/t3-rust-states.csv and
Revision/pairing/kohn_sham/reports/t3-rust-demo.json.  Exit 0 iff every check passes.
Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra
times; x8 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0] (brane y = 0, tip y = -L).
"""

import argparse
import concurrent.futures as cf
import csv
import hashlib
import io
import json
import math
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
T3DIR = HERE.parent
REV = T3DIR.parent.parent
REPO = REV.parent
KS = REV / "kohn_sham"
OUT_CSV = HERE / "results" / "t3-rust-states.csv"
OUT_REPORT = T3DIR / "reports" / "t3-rust-demo.json"

SLICES = (0.0, 0.5, 1.0, 1.5, 2.0)
TEMPS = (0.01, 0.02, 0.05)
GROUND_TAGS = ("lam0", "lamp1", "lamm1", "lamp2", "lamm2")
THERMO_TAGS = ("lam0", "lamp1", "lamm1")
OPPOSITE = {"lam0": "lam0", "lamp1": "lamm1", "lamm1": "lamp1", "lamp2": "lamm2", "lamm2": "lamp2"}
TOL = 1e-9          # T3 equality tolerance (relative, floor 1; profiles relative to the column maximum)
CTRL_MIN = 1e-6     # a negative control must differ by more than this (1000 x TOL)
CANON_TOL = 1e-9    # plus member against the committed canonical matrix
EVEN = ("n", "v_v", "e_int", "rho", "p3", "p_t", "p8")
ODD = ("S", "Q", "M_eff")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def run_id(n, tag, a4, t=None):
    s = "N%d_%s_a%02d" % (int(n), tag, int(round(10 * a4)))
    return s + ("_T%d" % int(round(1000 * t)) if t else "")


def lambda_of(calib, n, tag):
    if tag == "lam0":
        return 0.0
    c = next(x for x in calib if int(x["N"]) == int(n))
    v = c["lambda1"] if tag[-1] == "1" else c["lambda2"]
    return v if tag[3] == "p" else -v


def solve(job):
    """One `single` run; returns (key, record or None, error text)."""
    key, solver, work, m, lam, a4, n, th, t, reuse = job
    out = work / (key + ".json")
    prof = work / (key + ".csv")
    err = work / (key + ".err")
    if reuse and out.exists() and prof.exists():
        return key, _load(out, prof), ""
    if reuse and err.exists():
        return key, None, err.read_text(encoding="utf-8")
    cmd = [solver, "single", "--root", str(REPO), "--m", repr(m), "--lambda", repr(lam), "--a4", repr(a4),
           "--N", repr(n), "--tip-theta", repr(th), "--out", str(out), "--profiles", str(prof)]
    if t:
        cmd += ["--T", repr(t)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0 or not out.exists():
        msg = "exit %d: %s" % (p.returncode, (p.stderr.strip().splitlines() or [""])[-1][:300])
        err.write_text(msg, encoding="utf-8")
        return key, None, msg
    return key, _load(out, prof), ""


def _load(out, prof):
    rec = json.loads(out.read_text(encoding="utf-8"))
    rows = list(csv.reader(io.StringIO(prof.read_text(encoding="utf-8"))))
    head = rows[0]
    rec["profiles"] = {h: [float(r[i]) for r in rows[1:]] for i, h in enumerate(head)}
    return rec


def omega_of(rec):
    """Omega = -T sum g ln(1 + e^{-(eps - mu)/T}) - E_int and F = Omega + mu N (ks-theory.json thermodynamics)."""
    t = rec["parameters"]["T"]
    mu = rec["mu_or_fermi_level"]
    if t <= 0.0:
        return None, None
    s = 0.0
    for lv in rec["levels_n2_j_parity_label_eps_deg_f"]:
        x = (lv[4] - mu) / t
        s += lv[5] * (max(-x, 0.0) + math.log1p(math.exp(-abs(x))))
    om = -t * s - rec["E_int"]
    return om, om + mu * rec["particleNumber"]


def homo_lumo(rec):
    lv = rec["levels_n2_j_parity_label_eps_deg_f"]
    occ = [x[4] for x in lv if x[6] > 1e-12]
    homo = max(occ) if occ else float("nan")
    emp = [x[4] for x in lv if x[4] > homo + 1e-9 and x[6] < 1.0 - 1e-12]
    lumo = min(emp) if emp else float("nan")
    return homo, lumo


def sectors(rec, image=False):
    """{(n2, j, parity): [(eps, deg, f), ...] sorted by eps}; for the image the key is mapped back by
    (n2, j, parity) -> (n2, -j, other parity)."""
    out = {}
    for n2, j, par, _lab, eps, deg, f in rec["levels_n2_j_parity_label_eps_deg_f"]:
        if image:
            j, par = -j, ("odd" if par == "even" else "even")
        out.setdefault((n2, j, par), []).append((eps, deg, f))
    for k in out:
        out[k].sort()
    return out


def rel(a, b):
    return abs(a - b) / max(1.0, abs(a))


def compare_t3(a, b):
    """T3 comparison of plus (a) and image (b): returns (dict of deviations, problems)."""
    probs = []
    sa, sb = sectors(a), sectors(b, image=True)
    if set(sa) != set(sb):
        probs.append("sector sets differ after the map")
    de = dg = df = 0.0
    for k in set(sa) & set(sb):
        if len(sa[k]) != len(sb[k]):
            probs.append("sector %s: %d vs %d levels" % (k, len(sa[k]), len(sb[k])))
        for x, y in zip(sa[k], sb[k]):
            de, dg, df = max(de, abs(x[0] - y[0])), max(dg, abs(x[1] - y[1])), max(df, abs(x[2] - y[2]))
    d = {"levels_eps": de, "levels_deg": dg, "levels_f": df}
    sc = 0.0
    for nm in ("E_KS", "E_band", "E_int", "mu_or_fermi_level", "entropy", "particleNumber"):
        sc = max(sc, rel(a[nm], b[nm]))
    for nm, x in a["emtIntegrals_2Vol7_int_e6Hy"].items():
        sc = max(sc, rel(x, b["emtIntegrals_2Vol7_int_e6Hy"][nm]))
    d["scalars"] = sc
    oa, fa = omega_of(a)
    ob, fb = omega_of(b)
    d["omega_F"] = max(rel(oa, ob), rel(fa, fb)) if oa is not None else 0.0
    ha, la = homo_lumo(a)
    hb, lb = homo_lumo(b)
    d["homo_lumo_gap"] = max(abs(ha - hb), abs(la - lb), abs((la - ha) - (lb - hb))) if a["parameters"]["T"] == 0.0 else 0.0
    pe = po = 0.0
    for nm in EVEN + ODD:
        xa, xb = a["profiles"][nm], b["profiles"][nm]
        sg = -1.0 if nm in ODD else 1.0
        mx = max(max(abs(v) for v in xa), 1e-300)
        dv = max(abs(u - sg * v) for u, v in zip(xa, xb)) / mx
        if nm in ODD:
            po = max(po, dv)
        else:
            pe = max(pe, dv)
    d["profiles_even"], d["profiles_odd"] = pe, po
    d["worst"] = max(v for v in d.values())
    return d, probs


def control_dev(a, c):
    """How far a control state c lies from plus a (levels sorted globally, energies, EMT integrals, n(y))."""
    la = sorted((x[4], x[5]) for x in a["levels_n2_j_parity_label_eps_deg_f"])
    lc = sorted((x[4], x[5]) for x in c["levels_n2_j_parity_label_eps_deg_f"])
    dl = max((max(abs(x[0] - y[0]), abs(x[1] - y[1])) for x, y in zip(la, lc)), default=0.0)
    ds = rel(a["E_KS"], c["E_KS"])
    for nm, x in a["emtIntegrals_2Vol7_int_e6Hy"].items():
        ds = max(ds, rel(x, c["emtIntegrals_2Vol7_int_e6Hy"][nm]))
    na, nc = a["profiles"]["n"], c["profiles"]["n"]
    dn = max(abs(u - v) for u, v in zip(na, nc)) / max(max(abs(u) for u in na), 1e-300)
    return max(dl, ds, dn), {"levels": dl, "scalars": ds, "n_profile": dn}


def read_csv(p):
    with p.open(encoding="utf-8", newline="") as fh:
        return {r["id"]: r for r in csv.DictReader(fh)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solver", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--jobs", type=int, default=10)
    ap.add_argument("--reuse", action="store_true", help="reuse the single-run outputs already in --work (development)")
    args = ap.parse_args()
    # An absolute path: Windows' CreateProcess does not find a relative path written with '/' separators.
    args.solver = str(Path(args.solver).resolve())
    work = Path(args.work)
    work.mkdir(parents=True, exist_ok=True)
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
        print("%s %s" % ("PASS" if ok else "FAIL", name), flush=True)

    ks = json.loads((KS / "ks-theory.json").read_text(encoding="utf-8"))
    params = json.loads((KS / "results" / "parameters.json").read_text(encoding="utf-8"))
    src = json.loads((REV / "field_equations_a4" / "reports" / "ks-source-conditions.json").read_text(encoding="utf-8"))
    hist = ks["adiabaticity"]["historyStatus"]
    ok = hist.startswith("PRESCRIBED BACKGROUND") and "No Kohn-Sham state" in src["conclusion"] and \
        "prescribed background" in src["conclusion"] and src["summary"]["fail"] == 0
    ok = ok and params["physics"]["slicesA4"] == list(SLICES) and params["physics"]["temperatures"] == list(TEMPS)
    check("history_is_a_prescribed_background", ok,
          "the slices a4,0 = %s of the history a4 = A H x4 (A = %s; extra times x5, x6, x7 deflating as e^{-a4}) are a "
          "PRESCRIBED BACKGROUND: ks-theory.json adiabaticity.historyStatus begins '%s'; "
          "Revision/field_equations_a4/reports/ks-source-conditions.json (%d/%d checks) concludes: %s T3 is a statement "
          "slice by slice and does not use the history"
          % (list(SLICES), params["physics"]["historyA"], hist[:22], src["summary"]["pass"], src["summary"]["checks"],
             src["conclusion"]))

    calib = params["couplingCalibration"]["values"]
    ns = params["particleNumbers"]["values"]
    states = [(n, tag, a4, None) for n in ns for tag in GROUND_TAGS for a4 in SLICES] + \
             [(n, tag, a4, t) for n in ns for tag in THERMO_TAGS for a4 in SLICES for t in TEMPS]
    m0 = float(params["physics"]["m"])
    jobs = []
    for n, tag, a4, t in states:
        lam = lambda_of(calib, n, tag)
        sid = run_id(n, tag, a4, t)
        jobs.append((sid + "__plus", args.solver, work, m0, lam, a4, n, 0.0, t, args.reuse))
        jobs.append((sid + "__image", args.solver, work, -m0, lam, a4, n, math.pi, t, args.reuse))
        jobs.append((sid + "__control", args.solver, work, -m0, lam, a4, n, 0.0, t, args.reuse))
    res, errs = {}, {}
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        for key, rec, err in ex.map(solve, jobs):
            if rec is None:
                errs[key] = err
            else:
                res[key] = rec
    plus_img_ok = all(k.endswith("__control") for k in errs)
    check("plus_and_image_runs_converged", plus_img_ok and len(states) * 2 == sum(1 for k in res if not k.endswith("__control")),
          "%d states (75 ground, 135 thermal) x members plus (m = %s, theta = 0) and image (m = %s, theta = pi): every "
          "`single` run converged (exit 0, SCF residual <= its tolerance)%s"
          % (len(states), m0, -m0, "" if plus_img_ok else "; failures: " + "; ".join("%s %s" % kv for kv in sorted(errs.items()) if not kv[0].endswith("__control"))))

    # plus against the committed canonical matrix (read only)
    gsum = read_csv(KS / "results" / "ground" / "summary.csv")
    tsum = read_csv(KS / "results" / "thermo" / "thermodynamics.csv")
    worst_c, wid = 0.0, ""
    for n, tag, a4, t in states:
        sid = run_id(n, tag, a4, t)
        a = res.get(sid + "__plus")
        if a is None:
            continue
        if t:
            r = tsum[sid]
            om, _ = omega_of(a)
            dv = max(rel(float(r["E"]), a["E_KS"]), abs(float(r["mu"]) - a["mu_or_fermi_level"]),
                     rel(float(r["Omega_direct"]), om), rel(float(r["entropy"]), a["entropy"]))
        else:
            r = gsum[sid]
            dv = rel(float(r["E_KS"]), a["E_KS"])
        if dv > worst_c:
            worst_c, wid = dv, sid
    check("plus_reproduces_canonical_matrix", worst_c <= CANON_TOL,
          "the plus members (m, lambda, theta = 0) solved by `single` reproduce the committed canonical matrix "
          "(Revision/kohn_sham/results/ground/summary.csv E_KS; thermo/thermodynamics.csv E, mu, Omega_direct, entropy): "
          "worst deviation %.3e (%s), tolerance %.0e" % (worst_c, wid or "-", CANON_TOL))

    rows = []
    agg = {"ground": {}, "thermal": {}}
    probs_all = []
    ctrl_min, ctrl_min_id, ctrl_none, ctrl_reason = math.inf, "", [], ""
    part_min = {}
    lsign_min, lsign_min_id = math.inf, ""
    for n, tag, a4, t in states:
        sid = run_id(n, tag, a4, t)
        a, b, c = res.get(sid + "__plus"), res.get(sid + "__image"), res.get(sid + "__control")
        if a is None or b is None:
            continue
        d, probs = compare_t3(a, b)
        probs_all += ["%s: %s" % (sid, p) for p in probs]
        kind = "thermal" if t else "ground"
        for k, v in d.items():
            cur = agg[kind].get(k, (0.0, ""))
            if v >= cur[0]:
                agg[kind][k] = (v, sid) if v > cur[0] or not cur[1] else cur
        if c is None:
            cd, cparts = math.inf, {}
            ctrl_none.append(sid)
            ctrl_reason = ctrl_reason or errs.get(sid + "__control", "")
        else:
            cd, cparts = control_dev(a, c)
            for k_, v_ in cparts.items():
                if v_ < part_min.get(k_, (math.inf, ""))[0]:
                    part_min[k_] = (v_, sid)
        if cd < ctrl_min:
            ctrl_min, ctrl_min_id = cd, sid
        ls = math.nan
        if tag != "lam0":
            o = res.get(run_id(n, OPPOSITE[tag], a4, t) + "__image")
            if o is not None:
                ls, _ = control_dev(a, o)
                if ls < lsign_min:
                    lsign_min, lsign_min_id = ls, sid
        oa, fa = omega_of(a)
        ob, fb = omega_of(b)
        ha, la_ = homo_lumo(a)
        rows.append([sid, int(n), tag, repr(lambda_of(calib, n, tag)), repr(a4), repr(t or 0.0),
                     repr(a["E_KS"]), repr(b["E_KS"]), repr(a["mu_or_fermi_level"]), repr(b["mu_or_fermi_level"]),
                     repr(a["entropy"]), repr(b["entropy"]), repr(oa) if oa is not None else "", repr(ob) if ob is not None else "",
                     repr(a["emtIntegrals_2Vol7_int_e6Hy"]["rho"]), repr(a["emtIntegrals_2Vol7_int_e6Hy"]["p3"]),
                     repr(a["emtIntegrals_2Vol7_int_e6Hy"]["p_t"]), repr(a["emtIntegrals_2Vol7_int_e6Hy"]["p8"]),
                     repr(b["emtIntegrals_2Vol7_int_e6Hy"]["rho"]), repr(b["emtIntegrals_2Vol7_int_e6Hy"]["p3"]),
                     repr(b["emtIntegrals_2Vol7_int_e6Hy"]["p_t"]), repr(b["emtIntegrals_2Vol7_int_e6Hy"]["p8"]),
                     len(a["levels_n2_j_parity_label_eps_deg_f"]), "%.3e" % d["worst"],
                     "%.3e" % d["levels_eps"], "%.3e" % d["scalars"], "%.3e" % d["profiles_even"], "%.3e" % d["profiles_odd"],
                     "no state" if c is None else repr(c["E_KS"]), "no state" if c is None else "%.3e" % cd,
                     "" if tag == "lam0" else "%.3e" % ls])

    def agg_text(kind):
        return ", ".join("%s %.2e (%s)" % (k, v[0], v[1]) for k, v in sorted(agg[kind].items()))

    for kind, nst, what in (("ground", 75, "T = 0 aufbau ground states, N = %s x lambda tags %s x the 5 slices" % (ns, list(GROUND_TAGS))),
                            ("thermal", 135, "Mermin states, N = %s x %s x the 5 slices x T = %s" % (ns, list(THERMO_TAGS), list(TEMPS)))):
        worst = agg[kind].get("worst", (math.inf, ""))[0]
        cnt = sum(1 for r in rows if (r[5] != "0.0") == (kind == "thermal"))
        check("t3_equal_%s_states" % kind, cnt == nst and worst <= TOL and not [p for p in probs_all if (("_T" in p.split(":")[0]) == (kind == "thermal"))],
              "%d %s: the image (-m, +lambda, tip pi) equals the plus state (m, lambda, tip 0) as T3 states: levels label "
              "by label with the sector map (n2, j, parity) -> (n2, -j, other parity) (eps, degeneracy, occupation), "
              "E_KS, E_band, E_int, mu, entropy, N, the EMT integrals 2 Vol_7 int e^(6Hy)(rho, p3, p_t, p8, n) dy, "
              "Omega = -T sum g ln(1 + e^(-(eps - mu)/T)) - E_int and F = Omega + mu N (thermal), HOMO, LUMO and KS "
              "gap (T = 0), the even profiles n, v_v, e_int, rho, p3, p_t, p8 pointwise, and the odd profiles S, Q, M_eff "
              "with opposite sign (relative to each profile's maximum); worst deviation %.3e, tolerance %.0e; per "
              "quantity (worst, state): %s%s"
              % (cnt, what, worst, TOL, agg_text(kind), "" if not probs_all else "; problems: " + "; ".join(probs_all[:10])))

    nmin = part_min.get("n_profile", (0.0, ""))
    check("negative_control_untransformed_tip", ctrl_min > CTRL_MIN and nmin[0] > CTRL_MIN,
          "control (-m, +lambda) with the UNtransformed tip theta = 0 (b(-L) = 0) in all %d states: it is not the T3 "
          "image. The density profile alone, max_y |n_control - n_plus| / max_y |n_plus|, is at least %.3e (%s) in every "
          "state with a control state (with -m and the untransformed tip the k = 0 zero modes (e^(-m y), 0) are localised at "
          "the tip instead of the brane); the combined "
          "measure (max of that, the globally sorted (eps, degeneracy) list, E_KS and the EMT integrals) is at least %.3e "
          "(%s; its level part %.3e is dominated by the shifted degeneracies, its scalar part is %.1e in %s, where E_KS and "
          "the EMT integrals vanish for both); required > %.0e, in the %d states where the solver found a self-consistent control state; "
          "in %d states (%s) the solver found none (SCF diverging, also in its coupling continuation; reason of the first: %s), "
          "which separates them from the converged T3 image as well (it does not show that no such state exists)"
          % (len(states), nmin[0], nmin[1], ctrl_min, ctrl_min_id, part_min.get("levels", (0.0,))[0],
             part_min.get("scalars", (0.0, ""))[0], part_min.get("scalars", (0.0, "-"))[1], CTRL_MIN,
             len(states) - len(ctrl_none), len(ctrl_none),
             ", ".join(ctrl_none) if ctrl_none else "none", ctrl_reason[:200] if ctrl_reason else "-"))
    check("negative_control_lambda_sign", lsign_min > CTRL_MIN,
          "control with the T1 parameter map (-m, -lambda, tip pi) (the image member of the opposite coupling tag) "
          "against the plus state (m, +lambda) in all %d states with lambda != 0: smallest deviation %.3e (%s), "
          "required > %.0e: the Kohn-Sham partner carries +lambda, not -lambda"
          % (sum(1 for s in states if s[1] != "lam0"), lsign_min, lsign_min_id, CTRL_MIN))

    head = ["id", "N", "lambda_tag", "lambda", "a4", "T", "E_KS_plus", "E_KS_image", "mu_plus", "mu_image",
            "entropy_plus", "entropy_image", "Omega_plus", "Omega_image", "int_rho_plus", "int_p3_plus", "int_p_t_plus",
            "int_p8_plus", "int_rho_image", "int_p3_image", "int_p_t_image", "int_p8_image", "levels",
            "t3_worst_dev", "t3_levels_dev", "t3_scalars_dev", "t3_profiles_even_dev", "t3_profiles_odd_dev",
            "E_KS_control_untransformed_tip", "control_tip_dev", "control_lambda_sign_dev"]
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(head)
    w.writerows(rows)
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    OUT_CSV.write_bytes(buf.getvalue().encode("utf-8"))

    srcs = sorted((KS / "solver" / "src").glob("*.rs")) + [KS / "solver" / "Cargo.toml", KS / "solver" / "Cargo.lock"]
    npass = sum(1 for c in checks if c["verdict"] == "PASS")
    rep = {
        "report": "Revision/pairing/kohn_sham/reports/t3-rust-demo.json",
        "producer": "Revision/pairing/kohn_sham/numerics/t3_rust_demo.py",
        "spec": "Revision/SPEC.md section 9, theorem T3 (the Kohn-Sham level): numerical demonstration with the Revision "
                "Rust Kohn-Sham solver (a demonstration, not part of the proof)",
        "members": {"plus": "(m, lambda), tip theta = 0 (canonical boundary conditions)",
                    "image": "(-m, +lambda), tip theta = pi (the T3 image, transformed tip; brane parities exchanged by the map)",
                    "control": "(-m, +lambda), tip theta = 0 (UNtransformed boundary condition: negative control)"},
        "background": "slices a4,0 in {0, 0.5, 1, 1.5, 2} of the PRESCRIBED BACKGROUND history a4 = A H x4 (A = 1; x5, x6, x7 "
                      "deflating as e^{-a4}); the Kohn-Sham states violate the a4 source conditions "
                      "(Revision/field_equations_a4/reports/ks-source-conditions.json): a test field without back-reaction",
        "inputs": {"Revision/kohn_sham/ks-theory.json": sha(KS / "ks-theory.json"),
                   "Revision/kohn_sham/results/parameters.json": sha(KS / "results" / "parameters.json"),
                   "Revision/kohn_sham/results/ground/summary.csv": sha(KS / "results" / "ground" / "summary.csv"),
                   "Revision/kohn_sham/results/thermo/thermodynamics.csv": sha(KS / "results" / "thermo" / "thermodynamics.csv"),
                   "Revision/field_equations_a4/reports/ks-source-conditions.json": sha(REV / "field_equations_a4" / "reports" / "ks-source-conditions.json"),
                   "solver sources (Revision/kohn_sham/solver: src/*.rs, Cargo.toml, Cargo.lock), sha256 of the concatenation":
                       hashlib.sha256(b"".join(p.read_bytes() for p in srcs)).hexdigest()},
        "tolerances": {"t3_equality": TOL, "control_minimum_deviation": CTRL_MIN, "canonical_reproduction": CANON_TOL},
        "states": len(states),
        "table": "Revision/pairing/kohn_sham/numerics/results/t3-rust-states.csv",
        "summary": {"checks": len(checks), "pass": npass, "fail": len(checks) - npass},
        "checks": checks,
        "not_established": "A numerical demonstration on the canonical matrix, not a proof (the proof is exact: "
                           "t3-theory.json). Instantaneous (adiabatic) states on a prescribed background; ASSUMED Z2 brane; "
                           "filling CONVENTION of ks-theory.json; no creation process, rate or amplitude.",
    }
    OUT_REPORT.write_bytes((json.dumps(rep, indent=2, ensure_ascii=True) + "\n").encode("utf-8"))
    print("pass %d fail %d; wrote %s and %s" % (npass, len(checks) - npass, OUT_REPORT, OUT_CSV), flush=True)
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
