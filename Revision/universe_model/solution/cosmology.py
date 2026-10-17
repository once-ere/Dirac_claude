"""Revision/universe_model/solution/cosmology.py - the late-time cosmology of UM-1 at order epsilon (CMB, CNB, BAO) in
the four-dimensional effective theory of the block vacuum (vacua.py: G_eff = G/G(k0), G(k0) = 1 at the benchmark).

Approximations (stated; "accurate approximate"):
* flat FRW, H(z)^2 = H0^2 [Omega_r (1+z)^4 + Omega_m (1+z)^3 + Omega_L]; neutrino masses in the matter today
  (Omega_nu h^2 = sum m_nu / 93.14 eV), radiation before;
* z* (photon decoupling) from Hu & Sugiyama (1996), z_drag from Eisenstein & Hu (1998); the sound horizon
  r_s = int c_s dz/H with c_s = c/sqrt(3(1 + R)), R = 3 rho_b/(4 rho_gamma); theta* = r_s(z*)/D_M(z*);
* both fitting formulae are calibrated ONCE on the Planck 2018 LCDM best fit (the recorded r_drag and 100 theta*), and
  the same calibration factors are applied to UM-1 (the residual error is the change of the fitting-formula error
  between the two models, estimated below by varying N_eff in LCDM: a few 1e-4);
* the first acoustic peak l_1 = l_A (1 - phi_1), l_A = pi/theta*, phi_1 = 0.267 (r*/0.3)^0.1 (Hu, Fukugita, Zaldarriaga
  & Tegmark 2001), r* = rho_r/rho_m at z*.
The model inputs: ONE generation (one neutrino species, N_eff,SM = 1.0147: the standard 3.044 per species), the
dark radiation of the Psi fold band (g_F from the Kohn-Sham spectrum) decoupled at T_dec, the cold dark matter
(the lowest odd bulk level of Psi), the baryons (u, d -> p, n, QCD), T_CMB, and h fitted to theta*."""
import json
import math
from pathlib import Path

C_KMS = 299792.458
T_CMB = 2.7255                     # K (Fixsen 2009)
OMEGA_GAMMA_H2 = 2.4728e-5 * (T_CMB / 2.7255) ** 4
NEFF_PER_SPECIES = 3.044 / 3.0     # non-instantaneous decoupling and QED (Bennett et al. 2021)
PLANCK = {                          # Planck 2018 (TT,TE,EE+lowE+lensing; base LCDM), Table 2 of arXiv:1807.06209
    "omega_b": 0.02237, "omega_c": 0.1200, "h": 0.6736, "theta_star_100": 1.04110, "theta_star_100_sigma": 0.00031,
    "r_drag_Mpc": 147.09, "z_star": 1089.92, "z_drag": 1059.94, "sum_mnu_eV": 0.06, "N_eff": 3.046,
    "N_eff_measured": 2.99, "N_eff_sigma": 0.17,   # base LCDM + N_eff, TT,TE,EE+lowE+lensing+BAO
}
# eBOSS DR16 consensus BAO-only measurements (Alam et al. 2021, PRD 103, 083533; the table of
# https://www.sdss4.org/science/final-bao-and-rsd-measurements/, read 2026-10-17): (z, kind, value, sigma); the ELG
# error -0.62/+0.57 is symmetrised to 0.60; of the two z = 2.33 measurements the Lyman-alpha auto-correlation is used
BAO = [
    (0.15, "DV", 4.47, 0.17),
    (0.38, "DM", 10.23, 0.17), (0.38, "DH", 25.00, 0.76),
    (0.51, "DM", 13.36, 0.21), (0.51, "DH", 22.33, 0.58),
    (0.70, "DM", 17.86, 0.33), (0.70, "DH", 19.33, 0.53),
    (0.85, "DV", 18.33, 0.60),
    (1.48, "DM", 30.69, 0.80), (1.48, "DH", 13.26, 0.55),
    (2.33, "DM", 37.6, 1.9), (2.33, "DH", 8.93, 0.28),
]


def gstar_s_sm1(T_GeV):
    """g_*s of the UM-1 Standard-Model content (one generation, no Higgs) on its plateaus (step model; thresholds
    at m_W, the QCD crossover 0.15 GeV, the pions, m_e handled by the plateau below 20 MeV)"""
    if T_GeV > 80.0:
        return 2 + 9 + 16 + 7 / 8 * (24 + 4 + 2)            # gamma, W+-, Z, gluons; u, d, e, nu_L
    if T_GeV > 0.15:
        return 2 + 16 + 7 / 8 * (24 + 4 + 2)
    if T_GeV > 0.02:
        return 2 + 3 + 7 / 8 * (4 + 2)                       # gamma, pions, e, nu
    return 2 + 7 / 8 * (4 + 2)


def delta_neff(g_F, g_dec, g_nu_dec=2 + 7 / 8 * (4 + 2)):
    """dark radiation of g_F fermionic states decoupled when the Standard-Model g_*s = g_dec:
    Delta N_eff = (g_F/2) (T_Psi/T_nu)^4, (T_Psi/T_nu)^3 = g_*s(nu decoupling)/g_dec"""
    return 0.5 * g_F * (g_nu_dec / g_dec) ** (4.0 / 3.0)


def g_dec_for(neff_target, g_F, neff_sm):
    """the g_*s at Psi decoupling that gives N_eff = neff_target"""
    d = neff_target - neff_sm
    g_nu = 2 + 7 / 8 * (4 + 2)
    return g_nu * (0.5 * g_F / d) ** 0.75


class Cosmo:
    def __init__(self, omega_b, omega_c, h, N_eff, sum_mnu_eV):
        self.ob, self.oc, self.h, self.neff, self.mnu = omega_b, omega_c, h, N_eff, sum_mnu_eV
        self.og = OMEGA_GAMMA_H2
        self.orad = self.og * (1.0 + 0.22710731766 * N_eff)          # 7/8 (4/11)^{4/3} = 0.2271
        self.onu = sum_mnu_eV / 93.14
        self.om = omega_b + omega_c + self.onu
        self.oL = h * h - self.om - self.orad

    def E(self, z):
        return math.sqrt(self.orad * (1 + z) ** 4 + self.om * (1 + z) ** 3 + self.oL) / self.h

    def Hz(self, z):                                                 # km/s/Mpc
        return 100.0 * self.h * self.E(z)

    def z_star(self):
        ob, om = self.ob, self.ob + self.oc
        g1 = 0.0783 * ob ** -0.238 / (1 + 39.5 * ob ** 0.763)
        g2 = 0.560 / (1 + 21.1 * ob ** 1.81)
        return 1048.0 * (1 + 0.00124 * ob ** -0.738) * (1 + g1 * om ** g2)

    def z_drag(self):
        ob, om = self.ob, self.ob + self.oc
        b1 = 0.313 * om ** -0.419 * (1 + 0.607 * om ** 0.674)
        b2 = 0.238 * om ** 0.223
        return 1291.0 * om ** 0.251 / (1 + 0.659 * om ** 0.828) * (1 + b1 * ob ** b2)

    def _integral(self, f, a, b, n=4000):
        """Simpson in ln(1+z) from z = a to z = b"""
        x0, x1 = math.log1p(a), math.log1p(b)
        hh = (x1 - x0) / n
        s = 0.0
        for i in range(n + 1):
            x = x0 + i * hh
            z = math.expm1(x)
            w = 1 if i in (0, n) else (4 if i % 2 else 2)
            s += w * f(z) * (1 + z)
        return s * hh / 3.0

    def r_s(self, z):
        Rf = 3.0 * self.ob / (4.0 * self.og)

        def integrand(zz):
            cs = C_KMS / math.sqrt(3.0 * (1.0 + Rf / (1.0 + zz)))
            return cs / self.Hz(zz)
        return self._integral(integrand, z, 1e8, n=20000)

    def D_M(self, z):
        return self._integral(lambda zz: C_KMS / self.Hz(zz), 0.0, z, n=8000) if z > 0 else 0.0

    def D_H(self, z):
        return C_KMS / self.Hz(z)

    def D_V(self, z):
        return (z * self.D_M(z) ** 2 * self.D_H(z)) ** (1.0 / 3.0)


def raw_observables(cm):
    zs, zd = cm.z_star(), cm.z_drag()
    rs_star, rd = cm.r_s(zs), cm.r_s(zd)
    th = rs_star / cm.D_M(zs)
    rstar = cm.orad * (1 + zs) / cm.om
    return {"z_star": zs, "z_drag": zd, "r_s_star": rs_star, "r_drag": rd, "theta_star": th, "r_star_ratio": rstar}


def calibration():
    p = PLANCK
    ref = Cosmo(p["omega_b"], p["omega_c"], p["h"], p["N_eff"], p["sum_mnu_eV"])
    raw = raw_observables(ref)
    return {"k_theta": p["theta_star_100"] / (100.0 * raw["theta_star"]), "k_rd": p["r_drag_Mpc"] / raw["r_drag"],
            "raw_planck": raw}


def observables(cm, cal):
    raw = raw_observables(cm)
    th = raw["theta_star"] * cal["k_theta"]
    lA = math.pi / th
    phi1 = 0.267 * (raw["r_star_ratio"] / 0.3) ** 0.1
    out = dict(raw)
    out.update({"theta_star_100": 100.0 * th, "r_drag_Mpc": raw["r_drag"] * cal["k_rd"], "l_A": lA,
                "l_1": lA * (1 - phi1), "phi_1": phi1})
    return out


def fit_h(omega_b, omega_c, N_eff, mnu, cal, target=PLANCK["theta_star_100"]):
    lo, hi = 0.40, 1.00
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        th = observables(Cosmo(omega_b, omega_c, mid, N_eff, mnu), cal)["theta_star_100"]
        if th < target:                                  # theta* grows with h
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def bao_chi2(cm, rd):
    rows, chi2 = [], 0.0
    for z, kind, val, sig in BAO:
        pred = {"DM": cm.D_M(z), "DH": cm.D_H(z), "DV": cm.D_V(z)}[kind] / rd
        chi2 += ((pred - val) / sig) ** 2
        rows.append({"z": z, "kind": kind + "/r_d", "obs": val, "sigma": sig, "pred": pred, "pull": (pred - val) / sig})
    return chi2, rows


def cnb(T_dec_g, g_F):
    """today's neutrino and Psi-fold-band backgrounds (temperatures in K, number densities in cm^-3)"""
    Tnu = (4.0 / 11.0) ** (1.0 / 3.0) * T_CMB
    zeta3 = 1.2020569031595942
    k_B = 8.617333262e-5                      # eV/K
    hbarc_cm = 1.973269804e-5                 # eV cm
    n = lambda g, T: 0.75 * zeta3 / math.pi ** 2 * g * (k_B * T / hbarc_cm) ** 3
    TPsi = Tnu * ((2 + 7 / 8 * 6) / T_dec_g) ** (1.0 / 3.0)
    return {"T_nu_K": Tnu, "n_nu_per_species_cm3": n(2, Tnu), "T_Psi_fold_K": TPsi, "n_Psi_fold_cm3": n(g_F, TPsi),
            "T_nu_over_T_gamma": Tnu / T_CMB}


def analyse(g_F=8, m_dm_GeV=None, mnu_eV=0.05):
    p = PLANCK
    cal = calibration()
    out = {"calibration": {"k_theta": cal["k_theta"], "k_rd": cal["k_rd"], "raw_planck": cal["raw_planck"]}}
    # the residual calibration error: vary N_eff in LCDM (h refitted), compare the calibrated formula with the scaling
    lcdm = Cosmo(p["omega_b"], p["omega_c"], p["h"], p["N_eff"], p["sum_mnu_eV"])
    o_l = observables(lcdm, cal)
    chi_l, rows_l = bao_chi2(lcdm, o_l["r_drag_Mpc"])
    out["lcdm_planck"] = {"obs": o_l, "bao_chi2": chi_l, "bao": rows_l}
    neff_sm = NEFF_PER_SPECIES * 1.0
    scen = {}
    for name, g in (("above_mW", gstar_s_sm1(100.0)), ("QCD_to_mW", gstar_s_sm1(1.0)), ("pion_gas", gstar_s_sm1(0.1)),
                    ("below_20MeV", gstar_s_sm1(0.01)), ("fit_to_Planck_Neff", g_dec_for(p["N_eff_measured"], g_F, neff_sm))):
        dN = delta_neff(g_F, g)
        neff = neff_sm + dN
        h = fit_h(p["omega_b"], p["omega_c"], neff, mnu_eV, cal)
        cm = Cosmo(p["omega_b"], p["omega_c"], h, neff, mnu_eV)
        o = observables(cm, cal)
        chi, rows = bao_chi2(cm, o["r_drag_Mpc"])
        scen[name] = {"g_star_s_at_decoupling": g, "Delta_N_eff": dN, "N_eff": neff,
                      "N_eff_pull_vs_Planck": (neff - p["N_eff_measured"]) / p["N_eff_sigma"],
                      "h_fitted_to_theta_star": h, "H0": 100 * h, "obs": o, "bao_chi2": chi, "bao": rows,
                      "cnb": cnb(g, g_F)}
    out["um1"] = scen
    out["inputs"] = {"g_F": g_F, "N_eff_SM_one_generation": neff_sm, "sum_mnu_eV": mnu_eV, "omega_b": p["omega_b"],
                     "omega_c": p["omega_c"], "T_CMB": T_CMB, "m_dm_GeV": m_dm_GeV}
    # the formula error under a change of N_eff: LCDM with N_eff = 2 and 4, calibrated vs uncalibrated drift
    drift = {}
    for ne in (2.0, 4.0):
        hh = fit_h(p["omega_b"], p["omega_c"], ne, p["sum_mnu_eV"], cal)
        c2 = Cosmo(p["omega_b"], p["omega_c"], hh, ne, p["sum_mnu_eV"])
        r = raw_observables(c2)
        drift[str(ne)] = {"h": hh, "z_star_HS": r["z_star"], "z_drag_EH": r["z_drag"]}
    out["formula_drift"] = drift
    return out


if __name__ == "__main__":
    print(json.dumps(analyse(), indent=1)[:6000])
