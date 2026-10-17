#!/usr/bin/env python3
"""Revision/universe_model/solution/ks_coupled.py - step [4] of UM-1: the Kohn-Sham solution for the dirac16complex field
Psi, coupled to the Standard-Model fields through the portal mean fields (FIELD_EQUATIONS.md section 6) and to gravity
through the block (vacua.py part 5), at the late-time vacuum slice f = k0^{-1/2} (k0 = 8).

Conventions and units: those of the Kohn-Sham record (Revision/kohn_sham/ks-theory.json: H = m = 1, L = 3, dk = 0.25,
v_t = 1, b4(0) = 1, history parameter beta = 4/3, so f = e^{(beta/2 - 1) a4} = e^{-a4/3} and the vacuum slice is
a4_vac = 3 ln(8)/2).  The reference solver Revision/kohn_sham/reference/ks_fd.py is used UNCHANGED, with the record's
coefficients (run_reference.theory_coefficients, make_phys).  The portal mean fields enter as external potentials:

    M_eff -> M_eff + eD P_fold(y) + eS P_tip(y),        v_v -> v_v + eV P_fold(y),

with P_fold(y) = e^{2 c_e y/L} the shape of the electron zero-mode density (c_e from masses.fit, the Standard-Model
fermions sit at the fold) and P_tip(y) = e^{-(y + L)/w}/(w (1 - e^{-L/w})), w = 0.1, a unit-weight stand-in for
delta_tip.  eV = g_V sum_f q_f n_f, eD = g_D sum_f m_f s_f, eS = g_S sum_f s_f are the portal amplitudes in units of m
(P1, P5 and P2 of MODEL.md).  The sector matrices are built by the record's sector_arrays with the total potentials
(wrapped for the grid of the state only; the label sets are built from the free problem without portals, the record's
convention), and the energy-momentum tensor uses the total potentials in p0 (observables_ext).

Jobs (each below the 423 s limit; outputs in solution/outputs/ks/<job>.json):
  spectrum   the free spectrum at a4 = 0 (cross-check with the record's bulk edge) and at the vacuum slice on three grids
             (Richardson): the fold zero modes, the fold-band slope, the number g_F of massless fold-band states per
             3-momentum (particles and antiparticles), the lowest odd-parity bulk level (the dark-matter mass) and the
             lowest even bulk level
  portal8_lam0, portal8_lam1, portal592_lam0, portal592_lam1   ground states N = 8 and N = 592 (lambda = 0 and lambda_1 of the record) with each portal:
             the Hellmann-Feynman check dE_KS/de = int (dM/de S + dv/de n) (Richardson differences, fixed occupations),
             the y-exchange identity [e^{3Hy} p0] - 3H int e^{3Hy} p_t = -int e^{3Hy} (M_ext' S + v_ext' n) at e = 0.02,
             and the linear response of the dark-matter level, the fold band and the sources
  dm_lam0, dm_lam1   the N = 8 ground state plus 8 dark-matter quanta in the lowest odd levels (k = 0, j = +-1): the cold
             dark-matter equation of state p3/rho, its hidden pressure p0/rho
  loop       the coupled self-consistency Psi <-> Standard Model <-> block: KS state with the vector portal of the
             electron density -> hidden pressure -> block shift dk = sigma p0_bar/3 -> f -> c_f, m_KK -> portal profile and
             Standard-Model masses -> KS ..., to |dk change| < 1e-12, for two coupling strengths sigma = kappa/H^2 (units of
             the KS densities)

Usage: python ks_coupled.py JOB [JOB ...]   (python ks_coupled.py all runs every job in sequence)"""
from __future__ import annotations

import contextlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REV = HERE.parents[1]
sys.path.insert(0, str(REV / "kohn_sham" / "reference"))
sys.path.insert(0, str(HERE))
import ks_fd as K            # noqa: E402
import run_reference as R    # noqa: E402
import masses as MS          # noqa: E402

OUT = HERE / "outputs" / "ks"
CO = R.theory_coefficients()
BETA = float(CO["beta"])
K0 = 8.0                                   # the static vacuum k0 = 1/(4 w2), w2 = 1/32 (vacua.py)
GRIDS = (300, 600, 1200)
LAM1 = {8: 157.7, 592: 2.131}              # lambda_1 of the record (results/parameters.json couplingCalibration)
W_TIP = 0.1
FD = 1e-3                                  # portal step of the Hellmann-Feynman differences
E_FIN = 0.02                               # finite portal amplitude of the exchange-identity check


def a4_of_f(f):
    return math.log(f) / (0.5 * BETA - 1.0)


A4_VAC = a4_of_f(K0 ** -0.5)
C_E0 = None                                # c_e at the vacuum, from masses.fit (filled lazily)


def c_e0():
    global C_E0
    if C_E0 is None:
        C_E0 = MS.c_for(MS.OBS["e"] / MS.fit_mkk(3.0, MS.OBS["rho0_minus_1"]))
    return C_E0


def phys(**kw):
    return R.make_phys(CO, **kw)


class Portal:
    """external potentials v_ext = eV P_fold, M_ext = eD P_fold + eS P_tip (units of m), on any y array"""

    def __init__(self, c_fold, eV=0.0, eD=0.0, eS=0.0, L=3.0, w=W_TIP):
        self.c, self.eV, self.eD, self.eS, self.L, self.w = c_fold, eV, eD, eS, L, w

    def fold(self, y):
        return np.exp(2.0 * self.c * y / self.L)

    def dfold(self, y):
        return 2.0 * self.c / self.L * self.fold(y)

    def tip(self, y):
        return np.exp(-(y + self.L) / self.w) / (self.w * (-math.expm1(-self.L / self.w)))

    def dtip(self, y):
        return -self.tip(y) / self.w

    def M(self, y):
        return self.eD * self.fold(y) + self.eS * self.tip(y)

    def v(self, y):
        return self.eV * self.fold(y)

    def dM(self, y):
        return self.eD * self.dfold(y) + self.eS * self.dtip(y)

    def dv(self, y):
        return self.eV * self.dfold(y)

    def with_(self, **kw):
        p = Portal(self.c, self.eV, self.eD, self.eS, self.L, self.w)
        for k, v in kw.items():
            setattr(p, k, v)
        return p


@contextlib.contextmanager
def external(portal, grid):
    """add the portal potentials to every sector matrix built on `grid` (the record's sector_arrays, wrapped)"""
    orig = K.sector_arrays
    Mx, vx = portal.M(grid.y), portal.v(grid.y)

    def wrapped(g, ph, sec, M, v, a4=None, wq=None):
        if g is grid:
            return orig(g, ph, sec, M + Mx, v + vx, a4=a4, wq=wq)
        return orig(g, ph, sec, M, v, a4=a4, wq=wq)
    K.sector_arrays = wrapped
    try:
        yield
    finally:
        K.sector_arrays = orig


def solve(grid, ph, ls, portal, mode="aufbau", fixed=None, start=None, guess=None):
    with external(portal, grid):
        if mode == "aufbau":
            free = K.solve_state(grid, ph.copy(lam=0.0), ls, guess=guess)
            if ph.lam == 0.0:
                return free
            return K.solve_state_robust(grid, ph, ls, guess=free.eps)
        return K.solve_state(grid, ph, ls, mode=mode, fixed=fixed, start=start, guess=guess)


def observables_ext(st, portal):
    """the record's observables with the total potentials in p0, the portal energy and the y-exchange identity"""
    o, prof = K.observables(st)
    g, ph, d = st.grid, st.phys, st.dens
    Me, ve = portal.M(g.yext), portal.v(g.yext)
    p0 = prof["p0"] - ve * d.n - Me * d.S
    vol2 = 2.0 * ph.vol7
    e3 = g.e3ext

    def I(f):
        return vol2 * g.midpoint(e3 * f)
    o["int_p0"] = I(p0)
    o["E_portal"] = I(Me * d.S + ve * d.n)
    o["ycons_jump"] = float(e3[-1] * p0[-1] - e3[0] * p0[0])
    o["ycons_force"] = -g.midpoint(e3 * (portal.dM(g.yext) * d.S + portal.dv(g.yext) * d.n))
    o["ycons_residual"] = o["ycons_jump"] - o["ycons_integral"] - o["ycons_force"]
    o["ycons_scale"] = max(abs(o["ycons_jump"]), abs(o["ycons_integral"]), abs(o["ycons_force"]), 1e-300)
    o.pop("dE_da4_emt", None)            # the history identity of the record does not hold with external fields
    for nm in ("rho", "p3", "p_t", "p0"):
        o.pop(nm + "_brane", None)
        o.pop(nm + "_tip", None)
    prof["p0"] = p0
    # x0 averages per proper cell volume (B1 of ks_source_a4: X_bar = int_X / (2 Vol_7 W), W = int e^{3Hy} dy)
    W = (-math.expm1(-3.0 * ph.H * ph.L)) / (3.0 * ph.H)
    for nm in ("rho", "p3", "p_t", "p0", "n"):
        o[nm + "_bar"] = o["int_" + nm] / (vol2 * W)
    # the scalar density seen by the Standard-Model fermions (the back-reaction on their masses)
    o["S_at_fold_profile"] = float(g.midpoint(portal.fold(g.yext) * d.S * e3) / g.midpoint(portal.fold(g.yext) * e3))
    o["S_at_tip_profile"] = float(g.midpoint(portal.tip(g.yext) * d.S * e3) / g.midpoint(portal.tip(g.yext) * e3))
    return o, prof


def level(st, key):
    keys = st.ls.keys()
    for i, k in enumerate(keys):
        if k == key:
            return float(st.eps[i])
    return float("nan")


def window(grid, ph, N):
    lsw, info = K.build_window(grid, ph.copy(N=N), 0.1, pad_ranks=R.PAD_RANKS)
    return lsw, info


def dump(name, obj):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / (name + ".json")).write_text(json.dumps(R.jsonable(obj), indent=1, sort_keys=True) + "\n", encoding="utf-8",
                                        newline="\n")


# ------------------------------------------------------------------------------------------------
# job: spectrum
# ------------------------------------------------------------------------------------------------
def job_spectrum():
    res = {"a4_vac": A4_VAC, "f_vac": math.exp((0.5 * BETA - 1.0) * A4_VAC), "kappa_vac": math.exp(-A4_VAC)}
    rec_edge = json.loads((REV / "kohn_sham" / "results" / "parameters.json").read_text(encoding="utf-8"))["particleNumbers"]["bulkEdge"]
    for tag, a4 in (("a4_0", 0.0), ("vacuum", A4_VAC)):
        ph = phys(a4=a4, lam=0.0, N=8.0)
        rows = {}
        for G in GRIDS:
            g = K.Grid(ph, G)
            sec = K.shell_sectors([(0, 1), (1, 6)])
            imin, al, be = K.particle_offsets(g, ph, sec)
            E = np.array([K.eigen(al, be, imin + r)[0] for r in range(-1, 3)])   # ranks -1, 0, 1, 2
            rows[G] = E
        Rr, Ur = R.rich3(rows[GRIDS[0]], rows[GRIDS[1]], rows[GRIDS[2]])
        kap = math.exp(-a4)
        names = [str(s) for s in sec.items]
        lev = {names[s]: {"rank-1": [float(Rr[0, s]), float(Ur[0, s])], "rank0": [float(Rr[1, s]), float(Ur[1, s])],
                          "rank1": [float(Rr[2, s]), float(Ur[2, s])], "rank2": [float(Rr[3, s]), float(Ur[3, s])]}
               for s in range(len(sec))}
        # sectors: 0..3 shell n2 = 0 (j, odd) in SECTOR_ORDER; 4..7 shell n2 = 1
        zero_modes = [s for s in range(4) if abs(Rr[1, s]) < 1e-9]
        kdk = kap * 0.25
        fold_particle = [s for s in range(4, 8) if abs(Rr[1, s] - kdk) < 1e-9]
        fold_antiparticle = [s for s in range(4, 8) if abs(Rr[0, s] + kdk) < 1e-9]
        per_mom = 4                       # deg = 4 r3: 4 states per 3-momentum and sector
        odd0 = min(Rr[1, s] for s in range(4) if sec.items[s][3])
        even1 = min(Rr[2, s] for s in range(4) if not sec.items[s][3])
        res[tag] = {"a4": a4, "f": ph.fh, "kappa": kap, "levels": lev,
                    "zero_mode_sectors": [names[s] for s in zero_modes], "N_zero_modes": per_mom * len(zero_modes),
                    "fold_band_slope_rel_dev": float(max(abs(Rr[1, s] / kdk - 1.0) for s in fold_particle)) if fold_particle else None,
                    "g_F_particles_per_momentum": per_mom * len(fold_particle),
                    "g_F_antiparticles_per_momentum": per_mom * len(fold_antiparticle),
                    "g_F": per_mom * (len(fold_particle) + len(fold_antiparticle)),
                    "lowest_odd_bulk_k0": float(odd0), "lowest_even_bulk_k0": float(even1),
                    "bulk_edge": float(min(odd0, even1))}
        # ks-theory.json exactK0Spectra (k = 0, constant M, proper length f L): the analytic levels
        ao, ae = R._analytic(ph.m, ph.L * ph.fh, True, 0), R._analytic(ph.m, ph.L * ph.fh, False, 1)
        res[tag]["lowest_odd_bulk_analytic"] = ao
        res[tag]["lowest_even_bulk_analytic"] = ae
        res[tag]["analytic_max_rel_dev"] = max(abs(odd0 / ao - 1.0), abs(even1 / ae - 1.0))
    res["a4_0"]["record_bulkEdge"] = rec_edge
    res["a4_0"]["bulk_edge_rel_dev_vs_record"] = abs(res["a4_0"]["bulk_edge"] / rec_edge - 1.0)
    dump("spectrum", res)
    return res


# ------------------------------------------------------------------------------------------------
# job: portal (N = 8 or 592)
# ------------------------------------------------------------------------------------------------
def job_portal(N, which, grids=(300, 600)):
    ce = c_e0()
    base = Portal(ce)
    lam = (0.0, LAM1[N])[which]
    out = {"N": N, "lambda": lam, "c_e": ce, "grids": list(grids), "cases": {}}
    t0 = time.time()
    for _ in (0,):
        case = {}
        for G in grids:
            ph = phys(a4=A4_VAC, lam=lam, N=float(N))
            g = K.Grid(ph, G)
            ls, info = window(g, ph, N)
            st0 = solve(g, ph, ls, base)
            o0, prof0 = observables_ext(st0, base)
            rec = {"window": info, "iterations": st0.iters, "residual": st0.res, "E_KS": o0["E_KS"],
                   "dm_level": level(st0, (0, 1, "odd", 0)), "zero_mode": level(st0, (0, 1, "even", 0)),
                   "fold_n2_1": level(st0, (1, 1, "even", 0)), "sources": {k: o0[k] for k in ("rho_bar", "p3_bar", "p_t_bar", "p0_bar", "n_bar")},
                   "ycons_residual_rel_base": abs(o0["ycons_residual"]) / o0["ycons_scale"], "portals": {}}
            for pn in ("eV", "eD", "eS"):
                # Hellmann-Feynman: fixed occupations of the base state, portal +- FD, +- 2 FD
                E, lv = {}, {}
                for s in (1.0, -1.0, 2.0, -2.0):
                    pt = base.with_(**{pn: s * FD})
                    st = solve(g, ph, ls, pt, mode="fixed", fixed=st0.f, start=(st0.dM, st0.v), guess=st0.eps)
                    oo, _ = observables_ext(st, pt)
                    E[s] = oo["E_KS"]
                    lv[s] = (level(st, (0, 1, "odd", 0)), level(st, (1, 1, "even", 0)) - level(st, (0, 1, "even", 0)),
                             oo["p0_bar"], oo["rho_bar"])
                dE = float(R.rich_fd(E[1.0], E[-1.0], E[2.0], E[-2.0], FD))
                unit = base.with_(**{pn: 1.0})
                d = st0.dens
                vol2 = 2.0 * ph.vol7
                hf = vol2 * g.midpoint(g.e3ext * ((unit.M(g.yext) - base.M(g.yext)) * d.S + (unit.v(g.yext) - base.v(g.yext)) * d.n))
                dlev = [float(R.rich_fd(lv[1.0][i], lv[-1.0][i], lv[2.0][i], lv[-2.0][i], FD)) for i in range(4)]
                # finite amplitude: the y-exchange identity and the state
                pf = base.with_(**{pn: E_FIN})
                stf = solve(g, ph, ls, pf, start=None)
                of, _ = observables_ext(stf, pf)
                rec["portals"][pn] = {"dE_de_fd": dE, "dE_de_hf": float(hf), "hf_rel_dev": abs(dE - hf) / max(abs(hf), 1e-300),
                                      "d_dm_level_de": dlev[0], "d_fold_gap_n2_1_de": dlev[1], "d_p0_bar_de": dlev[2],
                                      "d_rho_bar_de": dlev[3],
                                      "finite": {"e": E_FIN, "iterations": stf.iters, "residual": stf.res, "E_KS": of["E_KS"],
                                                 "E_portal": of["E_portal"], "dm_level": level(stf, (0, 1, "odd", 0)),
                                                 "zero_mode": level(stf, (0, 1, "even", 0)),
                                                 "fold_slope_n2_1": (level(stf, (1, 1, "even", 0)) - level(stf, (0, 1, "even", 0))) / (math.exp(-A4_VAC) * 0.25),
                                                 "ycons_jump": of["ycons_jump"], "ycons_integral": of["ycons_integral"],
                                                 "ycons_force": of["ycons_force"],
                                                 "ycons_residual_rel": abs(of["ycons_residual"]) / of["ycons_scale"],
                                                 "S_fold": of["S_at_fold_profile"], "S_tip": of["S_at_tip_profile"],
                                                 "p0_bar": of["p0_bar"], "p_t_bar": of["p_t_bar"], "rho_bar": of["rho_bar"]}}
            case[G] = rec
        out["cases"]["lam%g" % lam] = case
    out["seconds"] = time.time() - t0
    dump("portal%d_lam%d" % (N, which), out)
    return out


# ------------------------------------------------------------------------------------------------
# job: dm
# ------------------------------------------------------------------------------------------------
def job_dm(which, grids=GRIDS):
    out = {"grids": list(grids), "cases": {}}
    base = Portal(c_e0())
    for lam in ((0.0, LAM1[8])[which],):
        per = {}
        for G in grids:
            ph = phys(a4=A4_VAC, lam=lam, N=8.0)
            g = K.Grid(ph, G)
            ls, info = window(g, ph, 8)
            st0 = solve(g, ph, ls, base)
            keys = ls.keys()
            fx = st0.f.copy()
            idx = [i for i, k in enumerate(keys) if k[0] == 0 and k[2] == "odd" and k[3] == 0]
            fx[idx] = 1.0                    # 4 + 4 dark-matter quanta in the lowest odd levels (j = +1, -1)
            ph_dm = ph.copy(N=8.0 + float(np.sum(ls.deg[idx])))
            st = solve(g, ph_dm, ls, base, mode="fixed", fixed=fx, start=(st0.dM, st0.v), guess=st0.eps)
            o0, _ = observables_ext(st0, base)
            o, _ = observables_ext(st, base)
            d = {k: o[k] - o0[k] for k in ("rho_bar", "p3_bar", "p_t_bar", "p0_bar", "n_bar")}
            per[G] = {"N_dm": float(np.sum(ls.deg[idx])), "dm_levels": [float(st.eps[i]) for i in idx],
                      "E_KS_ground": o0["E_KS"], "E_KS_with_dm": o["E_KS"], "dE": o["E_KS"] - o0["E_KS"],
                      "dm_sources": d, "w_dm": d["p3_bar"] / d["rho_bar"], "p0_over_rho_dm": d["p0_bar"] / d["rho_bar"],
                      "pt_over_rho_dm": d["p_t_bar"] / d["rho_bar"], "iterations": st.iters, "residual": st.res}
        if len(grids) == 3:
            rr = {k: R.rich3(*[per[G][k] for G in grids]) for k in ("dE", "w_dm", "p0_over_rho_dm")}
            per["richardson"] = {k: [float(v[0]), float(v[1])] for k, v in rr.items()}
        out["cases"]["lam%g" % lam] = per
    dump("dm_lam%d" % which, out)
    return out


# ------------------------------------------------------------------------------------------------
# job: loop
# ------------------------------------------------------------------------------------------------
def job_loop(G=300, N=592, eV0=0.01):
    """the coupled fixed point; the Standard-Model densities fixed in the cell, their profile following f"""
    mkk0 = MS.fit_mkk(3.0, MS.OBS["rho0_minus_1"])
    f0 = K0 ** -0.5
    mu = {s: MS.c_for(MS.OBS[s] / mkk0) / f0 for s in ("e", "u", "d", "nu")}     # c_f = f mu_f L (L = 1 in t)
    out = {"G": G, "N": N, "eV0": eV0, "runs": []}
    for sigma in (1e-3, 1e-1):
        dk, hist = 0.0, []
        for it in range(40):
            k = K0 + dk
            f = k ** -0.5
            a4 = a4_of_f(f)
            ph = phys(a4=a4, lam=LAM1[N], N=float(N))
            g = K.Grid(ph, G)
            ls, _ = window(g, ph, N)
            pt = Portal(mu["e"] * f, eV=eV0)
            st = solve(g, ph, ls, pt)
            o, _ = observables_ext(st, pt)
            dk_new = sigma * o["p0_bar"] / 3.0       # vacua part 5: dk = kappa p0/(3 H^2) (A = dLam = 0)
            hist.append({"it": it, "k": k, "f": f, "p0_bar": o["p0_bar"], "dk_new": dk_new, "dm_level": level(st, (0, 1, "odd", 0))})
            if abs(dk_new - dk) < 1e-12:
                dk = dk_new
                break
            dk = dk_new
        f = (K0 + dk) ** -0.5
        mkk = mkk0 * f0 / f
        masses = {s: mkk * MS.zeta2(mu[s] * f) for s in mu}
        out["runs"].append({"sigma": sigma, "converged": abs(hist[-1]["dk_new"] - hist[-2]["dk_new"]) < 1e-12 if len(hist) > 1 else True,
                            "iterations": len(hist), "dk": dk, "df_over_f": f / f0 - 1.0,
                            "dm_KK_over_mKK": mkk / mkk0 - 1.0,
                            "dm_over_m": {s: masses[s] / MS.OBS[s] - 1.0 for s in masses}, "history": hist})
    dump("loop", out)
    return out


JOBS = {"spectrum": job_spectrum, "portal8_lam0": lambda: job_portal(8, 0), "portal8_lam1": lambda: job_portal(8, 1),
        "portal592_lam0": lambda: job_portal(592, 0), "portal592_lam1": lambda: job_portal(592, 1),
        "dm_lam0": lambda: job_dm(0), "dm_lam1": lambda: job_dm(1), "loop": job_loop}

if __name__ == "__main__":
    todo = sys.argv[1:] or ["spectrum"]
    if todo == ["all"]:
        todo = list(JOBS)
    for j in todo:
        t = time.time()
        JOBS[j]()
        print(f"{j}: {time.time() - t:.1f} s", flush=True)
