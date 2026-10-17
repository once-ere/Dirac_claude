"""The result tables of KOHN_SHAM_DEFLATING_FIELD.md for the corrected record (version 2), in the format that the
publication test re-generates from Revision/kohn_sham/results (one function per table)."""
import csv
import json
from pathlib import Path

KS = Path(r"D:\Developer\github\Dirac_claude\Revision\kohn_sham")
RESULTS = KS / "results"
SLICES = ("a00", "a05", "a10", "a15", "a20")
NS = (8, 592, 2352)
NMID = 592


def rows(rel):
    with open(RESULTS / rel, encoding="utf-8", newline="") as h:
        return list(csv.DictReader(h))


def by_id(rel):
    return {r["id"]: r for r in rows(rel)}


def g7(v):
    return format(float(v), ".7g")


def g4(v):
    return format(float(v), ".4g")


def g3(v):
    return format(float(v), ".3g")


def couplings():
    p = json.loads((RESULTS / "parameters.json").read_text(encoding="utf-8"))
    out = ["| N | strength per unit lambda_hat | lambda_1 | lambda_2 |", "| --- | --- | --- | --- |"]
    out += [f"| {int(v['N'])} | {g7(v['strengthPerLambda'])} | {v['lambda1']} | {v['lambda2']} |"
            for v in p["couplingCalibration"]["values"]]
    return "\n".join(out)


def ground_excited():
    g, e = by_id("ground/summary.csv"), by_id("excited/summary.csv")
    out = ["| lambda_hat | a4,0 | E_KS | KS gap | Delta-SCF |", "| --- | --- | --- | --- | --- |"]
    for tag in ("lam0", "lamp1", "lamm1", "lamp2", "lamm2"):
        for s in ("a00", "a10", "a20"):
            a, b = g[f"N{NMID}_{tag}_{s}"], e[f"N{NMID}_{tag}_{s}"]
            out.append(f"| {g7(a['lambda'])} | {g7(a['a4'])} | {g7(a['E_KS'])} | {g7(a['KS_gap'])} | {g7(b['delta_SCF'])} |")
    return "\n".join(out)


def gaps():
    g = by_id("ground/summary.csv")
    out = ["| N | a4,0 = 0 | a4,0 = 0.5 | a4,0 = 1 | a4,0 = 1.5 | a4,0 = 2 |", "| --- | --- | --- | --- | --- | --- |"]
    out += [f"| {n} | " + " | ".join(g7(g[f'N{n}_lam0_{s}']['KS_gap']) for s in SLICES) + " |" for n in NS]
    return "\n".join(out)


def adiabaticity():
    a = by_id("adiabatic/adiabaticity.csv")
    out = ["| N | a4,0 | Q_max | delta eps of the pair | dE/da4 (EMT) | dE/da4 (differences) |",
           "| --- | --- | --- | --- | --- | --- |"]
    for n in (NMID, 2352):
        for s in SLICES:
            r = a[f"N{n}_lam0_{s}"]
            out.append(f"| {n} | {g7(r['a4'])} | {g7(r['Q_max'])} | {g7(r['Q_max_delta_eps'])} | {g7(r['dE_da4_emt'])} | "
                       f"{g7(r['dE_da4_finite_difference'])} |")
    return "\n".join(out)


def crossing():
    out = ["| a4,0 | occupied set as at a4,0 = 0 | open shell | E aufbau | E adiabatically continued | difference |",
           "| --- | --- | --- | --- | --- | --- |"]
    out += [f"| {g7(r['a4'])} | {r['occupied_set_equal_to_a4_0']} | {r['open_shell']} | {g7(r['E_aufbau'])} | "
            f"{g7(r['E_adiabatically_continued'])} | {g7(r['difference'])} |" for r in rows("adiabatic/crossing-demo.csv")]
    return "\n".join(out)


def thermo():
    t = by_id("thermo/thermodynamics.csv")
    out = ["| a4,0 | T | mu | E | entropy | Omega | sea holes / N |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for s in ("a00", "a20"):
        for tt in ("T10", "T20", "T50"):
            r = t[f"N{NMID}_lam0_{s}_{tt}"]
            out.append(f"| {g7(r['a4'])} | {g7(r['T'])} | {g7(r['mu'])} | {g7(r['E'])} | {g7(r['entropy'])} | "
                       f"{g7(r['Omega_direct'])} | {g3(r['sea_holes_over_N'])} |")
    return "\n".join(out)


def emt():
    m = by_id("ground/emt-integrals.csv")
    out = ["| N | a4,0 | int rho | int p3 | int p_t | int p0 |", "| --- | --- | --- | --- | --- | --- |"]
    for n in (NMID, 2352):
        for s in SLICES:
            r = m[f"N{n}_lam0_{s}"]
            out.append(f"| {n} | {g7(r['a4'])} | {g7(r['int_rho'])} | {g7(r['int_p3'])} | {g7(r['int_p_t'])} | {g7(r['int_p0'])} |")
    return "\n".join(out)


def rescaling():
    r = by_id("rescaling/rescaling.csv")
    out = ["| a4,0 | partner Delta k | partner v_t | partner H | partner L | max delta eps | relative delta E | partner E_KS |",
           "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for s in SLICES[1:]:
        x = r[f"N{NMID}_lamp1_{s}"]
        out.append(f"| {g7(x['a4'])} | {g7(x['partner_dk'])} | {g7(x['partner_v_t'])} | {g7(x['partner_H'])} | "
                   f"{g7(x['partner_L'])} | {g4(x['max_abs_delta_eps'])} | {g4(x['rel_delta_E'])} | {g7(x['partner_E_KS'])} |")
    return "\n".join(out)


TABLES = {"@@T_COUPLINGS@@": couplings, "@@T_GROUND@@": ground_excited, "@@T_GAPS@@": gaps,
          "@@T_ADIABATIC@@": adiabaticity, "@@T_CROSSING@@": crossing, "@@T_THERMO@@": thermo, "@@T_EMT@@": emt,
          "@@T_RESCALING@@": rescaling}

if __name__ == "__main__":
    for k, f in TABLES.items():
        print(k)
        print(f())
        print()
