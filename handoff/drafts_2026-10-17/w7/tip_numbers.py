"""The numbers of the tip-cutoff study (Revision/kohn_sham/tip_convergence/) that KOHN_SHAM_DEFLATING_FIELD.md quotes,
derived from tip-convergence.json and its two CSV files (the publication test repeats this derivation)."""
import csv
import json
import math
from pathlib import Path

TIP = Path(r"D:\Developer\github\Dirac_claude\Revision\kohn_sham\tip_convergence")
rec = json.loads((TIP / "tip-convergence.json").read_text(encoding="utf-8"))
with (TIP / "tip-convergence-extrapolation.csv").open(encoding="utf-8", newline="") as h:
    extra = {(r["protocol"], r["id"], r["quantity"]): r for r in csv.DictReader(h)}
with (TIP / "tip-convergence-table.csv").open(encoding="utf-8", newline="") as h:
    rows = list(csv.DictReader(h))
table = {(r["id"], float(r["L"])): r for r in rows
         if r["protocol"] == "fixed" and r["status"] == "ok" and int(r["G"]) == round(300 * float(r["L"]))}
grid = rec["Lvalues"]
print("L grid", grid, "checks", rec["summary"])
# 1. free fold-band states: L-independence of E_KS, HOMO, LUMO, KS_gap
free = sorted({s for (s, L) in table if "lam0" in s and "_T" not in s})
worst = 0.0
for s in free:
    if s == "N2352_lam0_a00":
        continue
    for q in ("E_KS", "HOMO", "LUMO", "KS_gap"):
        v = [float(table[(s, L)][q]) for L in grid if (s, L) in table]
        sc = max(max(abs(x) for x in v), 1e-300)
        worst = max(worst, (max(v) - min(v)) / sc)
print("free states", free, "worst relative change over L", worst)
# 2. N = 2352 at a4,0 = 0
s = "N2352_lam0_a00"
print("N2352 a00: E_KS(3), E_KS(6)", table[(s, 3.0)]["E_KS"], table[(s, 6.0)]["E_KS"],
      "gap(3)", table[(s, 3.0)]["KS_gap"], "first L with gap 0",
      min(L for (t, L), r in table.items() if t == s and float(r["KS_gap"]) == 0.0))
# 3. bulk edge
be = rec["k0Spectrum"]["bulkEdge_odd_l0_of_L"]
print("bulk edge", {k: round(v, 4) for k, v in be.items()})
# 4. fold values: 1/(1 - e^{-2 f m L}) - 1 at L = 3, f = e^{-a/3}
for a in (0.0, 1.0, 2.0):
    f = math.exp(-a / 3)
    print("fold excess a4 =", a, 100 * (1 / (1 - math.exp(-2 * f * 3)) - 1), "%")
# check against the table: rho_brane(L=3)/rho_brane(L=6) for the free N = 592 states
for a in ("a00", "a10", "a20"):
    sid = f"N592_lam0_{a}"
    r3, r6 = float(table[(sid, 3.0)]["rho_brane"]), float(table[(sid, 6.0)]["rho_brane"])
    f = math.exp(-int(a[1:]) / 30)
    exact = (1 - math.exp(-2 * f * 6)) / (1 - math.exp(-2 * f * 3))
    print("  ", sid, "rho_brane(3)/rho_brane(6)", r3 / r6, "exact", exact, "dev", abs(r3 / r6 / exact - 1))
# 5. N = 8 interaction energies
for a in ("a00", "a10", "a20"):
    for tag in ("lamp1", "lamm1"):
        e = extra[("fixed", f"N8_{tag}_{a}", "E_KS")]
        print("N8", tag, a, "L3", e["value_L3"], "Linf", e["extrapolated_Linf"], "ratio",
              float(e["value_L3"]) / float(e["extrapolated_Linf"]) if e["extrapolated_Linf"] else None, e["verdict"][:60],
              "failed", e["first_failed_L"])
# 6. interacting states: converged / failed
inter = [r for (p, sid, q), r in extra.items() if p == "fixed" and q == "E_KS" and "lam0" not in sid]
conv = [r for r in inter if r["verdict"].startswith("converg")]
fail = [(r["id"], r["first_failed_L"]) for r in inter if r["first_failed_L"]]
print("interacting", len(inter), "converged", len(conv), "failing", fail)
print("verdicts", sorted({r["verdict"][:40] for r in inter}))
# 7. interaction shifts at a4 = 2 (N = 592, 2352): (E(+-) - E(0)) at large L over at L = 3
for n in (592, 2352):
    for tag in ("lamp1", "lamm1"):
        e = extra[("fixed", f"N{n}_{tag}_a20", "E_KS")]
        e0 = extra[("fixed", f"N{n}_lam0_a20", "E_KS")]
        big = float(e["extrapolated_Linf"]) - float(e0["extrapolated_Linf"])
        small = float(e["value_L3"]) - float(e0["value_L3"])
        print("shift ratio", n, tag, big / small)
# 8. lambda_1(L) decay
lam = rec["couplings"]["recalibrated_lambda1_of_L"]
for n, d in lam.items():
    Ls = sorted(float(k) for k in d)
    ys = [math.log(d[f"{L:.15e}"]) for L in Ls]
    mx, my = sum(Ls) / len(Ls), sum(ys) / len(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(Ls, ys)) / sum((x - mx) ** 2 for x in Ls)
    last = (ys[-1] - ys[-3]) / (Ls[-1] - Ls[-3])
    print("lambda1(L)", n, "slope", slope, "last-two-step slope", last, "values", d[f"{3.0:.15e}"], d[f"{6.0:.15e}"])
# 9. reference comparison
print("reference", [(c["L"], c.get("pass")) for c in rec["reference"]["comparisons"]][:4], len(rec["reference"]["comparisons"]))
print([c["name"] for c in rec["checks"]])
for c in rec["checks"]:
    print(c["name"], c["detail"][:300])
