#!/usr/bin/env python3
"""um3_neutrino.py - the flavour evolution of the three Dirac neutrinos of UM-3 (FIELD_EQUATIONS.md, FE-48 to FE-53).

The neutrinos live on the fold with the flavour structure of the Standard Model (three Dirac neutrinos, U_PMNS); the
action of UM-3 adds two things: the flavour-blind potential V_Psi of the current portal (FE-49) and the local value
v_loc of the Higgs field, which the Higgs portal and the ad hoc vacuum can change (all masses scale with v_loc/v, the
Fermi constant with (v/v_loc)^2).  Computed and checked:
  N1  (FE-48, FE-49) a potential proportional to the unit matrix leaves the flavour evolution unchanged (exact, with a
      random Hamiltonian); rescaling v -> v_loc in the Yukawa mass matrices leaves |U_PMNS| and the Jarlskog invariant
      unchanged and scales every mass by v_loc/v; the resonance density scales as (v_loc/v)^4; the shift of v_loc by
      the local dark matter, Delta v^2/v^2 = g_hchi rho_chi/(lambda v^3 omega_b), is of order 1e-50;
  N2  (FE-50) the mixing angle in matter from the exact diagonalisation of the two-flavour Hamiltonian equals the
      formula; theta_m = 45 degrees at the resonance density; the Landau-Zener probability equals the jump probability
      from an exact integration of the Schroedinger equation through a linear density profile;
  N3  (FE-51) the fast flavour instability: for axially symmetric electron-lepton-number distributions without an
      angular crossing every eigenfrequency of the linearised equations (azimuthal modes m = 0 and 1) is real (the
      matrix is similar to a symmetric one); with a crossing an exponentially growing mode exists; the growth rate is
      converged in the number of angular nodes;
  N4  (FE-52) the equipartition map conserves the electron lepton number and the numbers of neutrinos and
      antineutrinos exactly, keeps every occupation number in [0, 1], and equilibrates the less abundant of nu_e and
      anti-nu_e with the heavy-lepton flavours whenever the Pauli bound is inactive;
  N5  (FE-53, FE-58, FE-62) the CNB today: T_nu = (4/11)^(1/3) T_gamma, n_nu = 3 zeta(3)/(2 pi^2) T_nu^3 per flavour,
      N_eff = 3 for instantaneous decoupling, the density parameter of massive neutrinos, Delta N_eff of three
      right-handed neutrinos that decouple above the electroweak scale.
Writes outputs/neutrino.json and reports/neutrino_checks.json.
Usage: python universe_model_3/code/um3_neutrino.py
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import numpy as np
import scipy.linalg as sla
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent

# constants (PDG 2024 values; natural units hbar = c = 1)
HBARC_GEV_CM = 1.973269804e-14       # GeV cm
KB_GEV_PER_K = 8.617333262e-14       # GeV / K
GF = 1.1663788e-5                    # GeV^-2
V_EW = (math.sqrt(2.0) * GF) ** -0.5  # 246.22 GeV
MH = 125.25                          # GeV
LAMBDA_H = MH ** 2 / (2.0 * V_EW ** 2)
T_GAMMA0_K = 2.7255                  # K
ZETA3 = 1.2020569031595942
RHO_C_OVER_H2_GEV_CM3 = 1.05375e-5   # GeV / cm^3


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


def random_hermitian(rng, n):
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (a + a.conj().T) / 2


def evolve(H, rho0, t):
    U = sla.expm(-1j * H * t)
    return U @ rho0 @ U.conj().T


def pmns_from_yukawas(Ye, Ynu, v):
    """(v/sqrt 2) Y = U_L diag(m) U_R^dagger (singular value decomposition, masses ascending); U_PMNS = U_eL^dagger U_nuL."""
    def left(Y):
        U, m, Vh = np.linalg.svd(v / math.sqrt(2.0) * Y)
        order = np.argsort(m)
        return U[:, order], m[order]
    UeL, me = left(Ye)
    UnL, mn = left(Ynu)
    return UeL.conj().T @ UnL, me, mn


def jarlskog(U):
    return float(np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])))


def two_flavour_h(Delta, th, V):
    """Two-flavour Hamiltonian (traceless part) in the flavour basis (e, x): vacuum term Delta = dm^2/(2E), the
    charged-current potential V in the electron flavour."""
    c, s = math.cos(2 * th), math.sin(2 * th)
    return np.array([[(-Delta * c + V) / 2, Delta * s / 2], [Delta * s / 2, (Delta * c - V) / 2]])


def jump_probability(Delta, th, Vp, L):
    """Exact integration of i d psi/dr = H(r) psi through the linear profile V = V_res + Vp r, r in [-L, L], starting in
    the upper eigenstate of matter; returns the probability of ending in the lower one (the jump)."""
    Vres = Delta * math.cos(2 * th)

    def rhs(r, y):
        p = y[:2] + 1j * y[2:]
        dp = -1j * two_flavour_h(Delta, th, Vres + Vp * r) @ p
        return np.concatenate([dp.real, dp.imag])
    _, U0 = np.linalg.eigh(two_flavour_h(Delta, th, Vres - Vp * L))
    psi0 = U0[:, 1].astype(complex)
    sol = solve_ivp(rhs, (-L, L), np.concatenate([psi0.real, psi0.imag]), rtol=1e-10, atol=1e-12, method='DOP853')
    p = sol.y[:2, -1] + 1j * sol.y[2:, -1]
    _, U1 = np.linalg.eigh(two_flavour_h(Delta, th, Vres + Vp * L))
    return 1.0 - abs(np.vdot(U1[:, 1], p)) ** 2


def ffi_growth(G, mu, w, Ks, m):
    """Largest imaginary part of the eigenfrequencies of the linearised fast-flavour equations (FE-51) for an axially
    symmetric ELN distribution G(mu), wave vector K along the axis, azimuthal mode m (0 or 1):
        Omega Q_i = K mu_i Q_i - sum_j w_j G_j k_m(i, j) Q_j,
        k_0 = 2 pi (1 - mu_i mu_j),  k_1 = -pi sqrt(1 - mu_i^2) sqrt(1 - mu_j^2)."""
    s = np.sqrt(1 - mu ** 2)
    best, arg = 0.0, None
    for K in Ks:
        if m == 0:
            A = K * np.diag(mu) - 2 * np.pi * (w * G)[None, :] * (1 - np.outer(mu, mu))
        else:
            A = K * np.diag(mu) + np.pi * (w * G)[None, :] * np.outer(s, s)
        g = float(np.linalg.eigvals(A).imag.max())
        if g > best:
            best, arg = g, float(K)
    return best, arg


def equipartition(Fe, Fb, Fx):
    """FE-52: the flavour equipartition with conservation of the electron lepton number and of the numbers of neutrinos
    and antineutrinos, the four heavy-lepton species equal, and the Pauli bound."""
    delta = np.maximum(2.0 / 3.0 * (np.minimum(Fe, Fb) - Fx), np.maximum(Fe, Fb) - 1.0)
    return Fe - delta, Fb - delta, Fx + delta / 2.0, delta


def main():
    t0 = time.time()
    rep = Report()
    out = {'constants': {'G_F': GF, 'v': V_EW, 'lambda': LAMBDA_H, 'T_gamma0_K': T_GAMMA0_K}}
    rng = np.random.default_rng(20261024)

    # ---------------- N1: flavour blindness of V_Psi; invariance of the mixing under v_loc
    H = random_hermitian(rng, 3)
    rho0 = random_hermitian(rng, 3)
    rho0 = rho0 @ rho0  # a positive matrix
    dev = max(np.abs(evolve(H + Vs * np.eye(3), rho0, t) - evolve(H, rho0, t)).max()
              for Vs in (0.3, -2.0, 17.0) for t in (0.5, 3.0, 40.0))
    Ye = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Ynu = 1e-12 * (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
    U1, me1, mn1 = pmns_from_yukawas(Ye, Ynu, V_EW)
    vloc = 1.37 * V_EW
    U2, me2, mn2 = pmns_from_yukawas(Ye, Ynu, vloc)
    dU = float(np.abs(np.abs(U1) - np.abs(U2)).max())
    dJ = abs(jarlskog(U1) - jarlskog(U2))
    ratio = np.concatenate([me2 / me1, mn2 / mn1])
    dm2, E, th = 2.5e-21, 1e-2, 0.15        # GeV^2, GeV (10 MeV), rad
    nres = lambda dm2_, GF_: dm2_ * math.cos(2 * th) / (2 * math.sqrt(2.0) * GF_ * E)
    scale = nres(dm2 * (vloc / V_EW) ** 2, GF * (V_EW / vloc) ** 2) / nres(dm2, GF)
    rho_chi = 0.3 * HBARC_GEV_CM ** 3        # 0.3 GeV/cm^3 in GeV^4
    shift = rho_chi / (LAMBDA_H * V_EW ** 3 * 100.0)   # per unit g_hchi, omega_b = 100 GeV
    out['N1'] = {'max_deviation_with_V_Psi': float(dev), 'max_delta_abs_U': dU, 'delta_Jarlskog': dJ,
                 'mass_ratios': ratio.tolist(), 'resonance_density_scale': scale, 'expected_scale': (vloc / V_EW) ** 4,
                 'dv2_over_v2_per_g_hchi': shift}
    rep.check('N1_flavour_blindness_and_v_loc',
              dev < 1e-10 and dU < 1e-12 and dJ < 1e-12 and np.allclose(ratio, vloc / V_EW, rtol=1e-12)
              and abs(scale / (vloc / V_EW) ** 4 - 1) < 1e-12 and 1e-51 < shift < 1e-49,
              'V_Psi * 1 changes rho(t) by at most %.1e (exact: it commutes); v -> 1.37 v leaves |U_PMNS| (max change %.1e) and '
              'the Jarlskog invariant (change %.1e) unchanged and scales all six masses by %.6f; resonance density scales by %.6f '
              '= (v_loc/v)^4; Delta v^2/v^2 = %.2e g_hchi for 0.3 GeV/cm^3 and omega_b = 100 GeV' % (
                  dev, dU, dJ, float(ratio.mean()), scale, shift))

    # ---------------- N2: matter-enhanced conversion
    Delta = dm2 / (2 * E)
    err_angle = 0.0
    for V in np.linspace(0.0, 3.0 * Delta, 13):
        e, U = np.linalg.eigh(two_flavour_h(Delta, th, V))
        # the heavier eigenstate (column 1) is (sin theta_m, cos theta_m) in (e, x) up to sign
        thm_num = math.atan2(abs(U[0, 1]), abs(U[1, 1]))
        thm_formula = 0.5 * math.atan2(math.sin(2 * th), math.cos(2 * th) - V / Delta)
        err_angle = max(err_angle, abs(thm_num - thm_formula))
    Vres = Delta * math.cos(2 * th)
    e, U = np.linalg.eigh(two_flavour_h(Delta, th, Vres))
    thm_res = math.degrees(math.atan2(abs(U[0, 1]), abs(U[1, 1])))
    lz = []
    for (D_, th_, Vp_) in [(1.0, 0.15, 0.05), (1.0, 0.1, 0.02), (2.0, 0.3, 0.5)]:
        gam = D_ ** 2 * math.sin(2 * th_) ** 2 / abs(Vp_)
        # FE-50 form: gamma = dm^2 sin^2 2theta / (2E cos 2theta) * |d ln n_e/dr|^-1 at the resonance
        gam_fe50 = D_ * math.sin(2 * th_) ** 2 / math.cos(2 * th_) * (D_ * math.cos(2 * th_)) / abs(Vp_)
        P = math.exp(-math.pi / 2 * gam_fe50)
        Pnum = jump_probability(D_, th_, Vp_, 400 * D_ * math.sin(2 * th_) / Vp_)
        lz.append({'Delta': D_, 'theta': th_, 'dV/dr': Vp_, 'gamma': gam, 'P_LZ': P, 'P_numeric': Pnum})
    out['N2'] = {'max_error_matter_angle_rad': err_angle, 'theta_m_at_resonance_deg': thm_res, 'landau_zener': lz}
    rep.check('N2_msw_and_landau_zener',
              err_angle < 1e-12 and abs(thm_res - 45.0) < 1e-9 and all(abs(x['P_numeric'] / x['P_LZ'] - 1) < 1e-4 for x in lz),
              'tan 2theta_m formula vs exact diagonalisation: max error %.1e rad; theta_m = %.9f deg at n_e,res; Landau-Zener '
              'vs exact integration through a linear profile: %s' % (
                  err_angle, thm_res, ', '.join('%.6f/%.6f' % (x['P_LZ'], x['P_numeric']) for x in lz)))

    # ---------------- N3: the crossing criterion of the fast instability
    Ks = np.linspace(-3, 3, 241)
    dists = {'no crossing, forward nu_e excess': lambda mu: 1.0 + 0.6 * mu,
             'no crossing, peaked': lambda mu: 0.3 * np.exp(2 * mu),
             'no crossing, anti-nu_e excess': lambda mu: -(0.5 + 0.4 * mu ** 2),
             'crossing, linear': lambda mu: mu - 0.3,
             'crossing, forward peak': lambda mu: 2.0 * np.exp(3 * (mu - 1)) - 0.15,
             'crossing, nu_e vs anti-nu_e': lambda mu: 0.6 * np.exp(2 * (mu - 1)) - 0.5 * np.exp(1.2 * (mu - 1))}
    res = []
    for nn in (80, 160):
        mu, w = np.polynomial.legendre.leggauss(nn)
        for name, f in dists.items():
            G = f(mu)
            g0, k0 = ffi_growth(G, mu, w, Ks, 0)
            g1, k1 = ffi_growth(G, mu, w, Ks, 1)
            res.append({'nodes': nn, 'distribution': name, 'crossing': bool(G.max() > 0 > G.min()),
                        'growth_m0': g0, 'K_m0': k0, 'growth_m1': g1, 'K_m1': k1})
    ok_no = all(max(r['growth_m0'], r['growth_m1']) < 1e-10 for r in res if not r['crossing'])
    ok_yes = all(max(r['growth_m0'], r['growth_m1']) > 1e-2 for r in res if r['crossing'])
    conv = []
    for name in dists:
        a = [r for r in res if r['distribution'] == name and r['nodes'] == 80][0]
        b = [r for r in res if r['distribution'] == name and r['nodes'] == 160][0]
        if a['crossing']:
            conv.append(abs(max(a['growth_m0'], a['growth_m1']) / max(b['growth_m0'], b['growth_m1']) - 1))
    out['N3'] = res
    rep.check('N3_fast_instability_crossing', ok_no and ok_yes and max(conv) < 1e-2,
              'without an angular crossing all eigenfrequencies are real (max imaginary part %.1e); with a crossing the growth '
              'rates are %s (units of the ELN scale); change from 80 to 160 angular nodes at most %.1e' % (
                  max(max(r['growth_m0'], r['growth_m1']) for r in res if not r['crossing']),
                  ', '.join('%.3f' % max(r['growth_m0'], r['growth_m1']) for r in res if r['crossing'] and r['nodes'] == 160),
                  max(conv)))

    # ---------------- N4: the equipartition map FE-52
    F = rng.uniform(0, 1, size=(3, 200000))
    Fe, Fb, Fx = F
    Fe2, Fb2, Fx2, d = equipartition(Fe, Fb, Fx)
    eln = np.abs((Fe2 - Fb2) - (Fe - Fb)).max()
    nnu = np.abs((Fe2 + 2 * Fx2) - (Fe + 2 * Fx)).max()
    nnb = np.abs((Fb2 + 2 * Fx2) - (Fb + 2 * Fx)).max()
    inside = bool(((Fe2 >= -1e-15) & (Fe2 <= 1 + 1e-15) & (Fb2 >= -1e-15) & (Fb2 <= 1 + 1e-15)
                   & (Fx2 >= -1e-15) & (Fx2 <= 1 + 1e-15)).all())
    free = 2.0 / 3.0 * (np.minimum(Fe, Fb) - Fx) >= np.maximum(Fe, Fb) - 1.0
    less = np.where(Fe <= Fb, Fe2, Fb2)
    equi = float(np.abs(less[free] - Fx2[free]).max())
    out['N4'] = {'samples': int(F.shape[1]), 'max_change_ELN': float(eln), 'max_change_number_nu': float(nnu),
                 'max_change_number_nubar': float(nnb), 'all_in_unit_interval': inside,
                 'fraction_pauli_bound_active': float(1 - free.mean()), 'max_equipartition_error': equi}
    rep.check('N4_equipartition_conservation', max(eln, nnu, nnb) < 1e-14 and inside and equi < 1e-14,
              '%d random (F_e, Fbar_e, F_x) in [0,1]^3: ELN, number of nu and of anti-nu conserved to %.1e; every occupation in '
              '[0, 1]; the less abundant of nu_e, anti-nu_e equals the heavy flavours (error %.1e) where the Pauli bound is '
              'inactive (it is active in %.1f%% of the samples)' % (F.shape[1], max(eln, nnu, nnb), equi, 100 * (1 - free.mean())))

    # ---------------- N5: the CNB
    Tnu0 = (4.0 / 11.0) ** (1.0 / 3.0) * T_GAMMA0_K
    T_cm = Tnu0 * KB_GEV_PER_K / HBARC_GEV_CM          # 1/cm
    n_nu = 3 * ZETA3 / (2 * math.pi ** 2) * T_cm ** 3  # per flavour, nu + anti-nu
    Neff_inst = 8 / 7 * (11 / 4) ** (4 / 3) * (3 * 7 / 8 * (4 / 11) ** (4 / 3))
    denom_inst = RHO_C_OVER_H2_GEV_CM3 * 1e9 / n_nu     # eV: Omega_nu h^2 = sum m / denom
    dNeff_ew = 3 * (10.75 / 106.75) ** (4 / 3)
    out['N5'] = {'T_nu0_K': Tnu0, 'n_nu0_per_cm3_per_flavour': n_nu, 'N_eff_instantaneous': Neff_inst,
                 'Omega_nu_h2_denominator_instantaneous_eV': denom_inst, 'Omega_nu_h2_denominator_used_eV': 93.14,
                 'Delta_N_eff_nuR_decoupled_above_EW': dNeff_ew}
    rep.check('N5_cnb', abs(Tnu0 - 1.9454) < 1e-3 and abs(n_nu - 112.0) < 0.5 and abs(Neff_inst - 3) < 1e-12
              and 0.005 < denom_inst / 93.14 - 1 < 0.015 and abs(dNeff_ew - 0.141) < 0.002,
              'T_nu0 = %.4f K; n_nu0 = %.2f /cm^3 per flavour; N_eff = %.3f for instantaneous decoupling; Omega_nu h^2 = sum m/(%.2f eV) '
              'for instantaneous decoupling, 1.0%% above the 93.14 eV that includes the non-thermal heating of the neutrinos; '
              'Delta N_eff = %.3f for three nu_R decoupling above the electroweak scale' % (Tnu0, n_nu, Neff_inst, denom_inst, dNeff_ew))

    out['runtime_s'] = round(time.time() - t0, 1)
    (UM3 / 'outputs' / 'neutrino.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_neutrino.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    (UM3 / 'reports' / 'neutrino_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
