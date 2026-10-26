#!/usr/bin/env python3
"""um4_flavour.py - the neutrino flavour evolution of UM-4 solved in the Sun and in core-collapse supernovae
(SOLUTION.md; FE-48 to FE-52 of FIELD_EQUATIONS.md).

UM-4 has the flavour physics of the Standard Model with three Dirac neutrinos wherever the local electroweak vacuum
v_loc equals v (FE-49; um4_neutrino.py, N1): the portal potential V_Psi is the same for all flavours and drops out of
every commutator, and the Higgs-portal shift of v_loc by the dark matter is of order 1e-50.  The flavour evolution is
therefore computed with the measured masses and mixing angles (units: km, eV; hbar c = 1.97327e-10 eV km).  The flavour
equation i d psi/dr = H(r) psi (FE-48 for a single neutrino of energy E along its path, without collisions and without the
neutrino-neutrino potential) is integrated with the fourth-order commutator-free Magnus method (the exponentials of the
Hamiltonian at the two Gauss points of each step, exact for a constant density), whose step propagators are multiplied
pairwise; each result is repeated with half the step and must not change.
  F1  the Sun: the survival probability P_ee(E) of electron neutrinos produced at the radius r_prod of their reaction
      (0.10 R_sun for pp and pep, 0.06 R_sun for 7Be, 0.05 R_sun for 8B), by exact integration through the electron density
      n_e = 245 N_A exp(-10.54 r/R_sun) cm^-3 (two flavours theta12, Delta m^2_21 with the potential c13^2 V_CC, and the
      decoupled theta13: P_ee = c13^4 P_2 + s13^4), with the phases averaged by the size of the production region and the
      distance to the Earth (the probabilities of the mass states at the surface); compared with the adiabatic formula
      P_ee = c13^4 (1/2 + 1/2 cos 2theta12 cos 2theta12_m) + s13^4 (theta12_m at production, FE-50), with the exact
      crossing probability of an exponential profile (Petcov), and with the measurements of Borexino;
  F2  the supernova envelope: the three-flavour evolution through rho = 1e4 g/cm^3 (r/1e9 cm)^-3 (Y_e = 0.5) across the high
      (Delta m^2_31) and low (Delta m^2_21) resonances, both adiabatic (gamma >> 1, P_LZ = 0, FE-50); the probabilities of
      the mass states at the surface and P_ee for the normal and the inverted mass ordering (|U_e3|^2 or |U_e2|^2 for
      neutrinos, |U_e1|^2 or |U_e3|^2 for antineutrinos);
  F3  the fast instability near the neutrinosphere (FE-51): electron neutrinos and antineutrinos emitted half-isotropically
      from spheres of radius R_e = 30 km and R_ebar = 27 km (the antineutrinos decouple deeper and are more forward peaked)
      with the number ratio alpha = n_ebar/n_e, observed at r = 40 km: the electron-lepton-number distribution, its crossing
      (for alpha > (1 - mu_ebar)/(1 - mu_e)), the growth rate of the most unstable mode (axially symmetric m = 0 and m = 1,
      wave vector along the radius), the dispersion relation of FE-51 at that solution, and the growth length for
      L = 5e52 erg/s and <E> = 12 MeV;
  F4  the flavour equipartition FE-52: its conservation laws, its fixed point and the bound 0 <= F <= 1 for random
      occupations, and its effect on the charged-current heating of the gain region (absorption cross-section ~ E^2,
      deposited energy ~ E: heating ~ sum over nu_e and anti-nu_e of the integral of E^3 dN/dE) for typical spectra of the
      accretion phase and of later times (ESTIMATE without the feedback on the cooling and the hydrodynamics).
Writes outputs/flavour.json and reports/flavour_checks.json.
Usage: python universe_model_4/code/um4_flavour.py
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
UM4 = HERE.parent

HBARC_EV_KM = 1.97327e-10
HBARC_EV_CM = 1.97327e-5
SQRT2GF_EV_CM3 = math.sqrt(2.0) * 1.1663788e-23 * HBARC_EV_CM ** 3      # sqrt2 G_F in eV cm^3 (G_F = 1.1663788e-23 eV^-2)
NA = 6.02214076e23
R_SUN_KM = 6.957e5
MU_G = 1.66053907e-24                                                   # the atomic mass unit in g: n_e = Y_e rho/m_u
# measured mixing: the global fit NuFIT 5.2 (November 2022; Esteban, Gonzalez-Garcia, Maltoni, Schwetz, Zhou, JHEP 09 (2020)
# 178 and www.nu-fit.org), normal ordering, best fit without the Super-Kamiokande atmospheric data: sin^2 theta12 = 0.303,
# sin^2 theta13 = 0.02203, sin^2 theta23 = 0.572 (theta12 = 33.40, theta13 = 8.54, theta23 = 49.14 deg), Delta m^2_21 =
# 7.41e-5 eV^2, Delta m^2_31 = 2.511e-3 eV^2; the Dirac phase is set to 0 (ASSUMED).  The inverted ordering, used only for
# the comparison in F2, keeps |Delta m^2_32| = 2.511e-3 eV^2: m_3^2 - m_1^2 = -(DM31 - DM21) = -2.437e-3 eV^2
TH12, TH23, TH13 = (math.asin(math.sqrt(x)) for x in (0.303, 0.572, 0.02203))
DM21, DM31 = 7.41e-5, 2.511e-3                                         # eV^2
# Borexino (Nature 562, 505 (2018)): P_ee with the high-metallicity standard solar model
BOREXINO = [('pp', 0.267, 0.57, 0.09), ('7Be', 0.862, 0.53, 0.05), ('pep', 1.44, 0.43, 0.11), ('8B', 8.1, 0.37, 0.08)]
# fourth-order commutator-free Magnus method
_A1, _A2 = (3 - 2 * math.sqrt(3)) / 12, (3 + 2 * math.sqrt(3)) / 12
_C1, _C2 = 0.5 - math.sqrt(3) / 6, 0.5 + math.sqrt(3) / 6


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''), flush=True)
        return ok


def pmns(th12=TH12, th23=TH23, th13=TH13, delta=0.0):
    c12, s12, c23, s23, c13, s13 = (math.cos(th12), math.sin(th12), math.cos(th23), math.sin(th23), math.cos(th13),
                                    math.sin(th13))
    e = np.exp(-1j * delta)
    R23 = np.array([[1, 0, 0], [0, c23, s23], [0, -s23, c23]], complex)
    U13 = np.array([[c13, 0, s13 * e], [0, 1, 0], [-s13 * np.conj(e), 0, c13]], complex)
    R12 = np.array([[c12, s12, 0], [-s12, c12, 0], [0, 0, 1]], complex)
    return R23 @ U13 @ R12


def k_vac(dm2, E_MeV):
    """dm^2/(2E) in km^-1."""
    return dm2 / (2 * E_MeV * 1e6) / HBARC_EV_KM


def vcc_km(ne_cm3):
    """sqrt2 G_F n_e in km^-1."""
    return SQRT2GF_EV_CM3 * ne_cm3 / HBARC_EV_KM


def _expmh(M, h):
    w, V = np.linalg.eigh(M)
    return (V * np.exp(-1j * h[:, None] * w)[:, None, :]) @ np.conj(np.swapaxes(V, -1, -2))


def _chain(U):
    while len(U) > 1:
        if len(U) % 2:
            U = np.concatenate([U, np.eye(U.shape[-1], dtype=complex)[None]])
        U = U[1::2] @ U[0::2]
    return U[0]


def propagator(Hbatch, nodes, chunk=100000):
    """The evolution operator from nodes[0] to nodes[-1] of i d psi/dr = H(r) psi; Hbatch maps an array of radii to the
    Hermitian matrices H (shape (n, d, d))."""
    P = None
    for s in range(0, len(nodes) - 1, chunk):
        seg = nodes[s:s + chunk + 1]
        a, h = seg[:-1], np.diff(seg)
        H1, H2 = Hbatch(a + _C1 * h), Hbatch(a + _C2 * h)
        Pc = _chain(_expmh(_A1 * H1 + _A2 * H2, h) @ _expmh(_A2 * H1 + _A1 * H2, h))
        P = Pc if P is None else Pc @ P
    return P


def mass_state_probabilities(Hend, psi, Umix):
    """Probabilities of the vacuum mass states at the end of the path: the local eigenvectors of H are matched to the
    columns of the mixing matrix by their overlap (they connect adiabatically to the mass states at zero density)."""
    w, V = np.linalg.eigh(Hend)
    ov = np.abs(Umix.conj().T @ V) ** 2
    pm = np.zeros(len(psi))
    for j in range(len(psi)):
        pm[int(ov[:, j].argmax())] = abs(np.vdot(V[:, j], psi)) ** 2
    return pm, float(ov.max(axis=0).min())


# ---------------------------------------------------------------- F1: the Sun
def ne_sun(r_km):
    return 245 * NA * np.exp(-10.54 * np.asarray(r_km) / R_SUN_KM)


def solar_hamiltonian(E):
    k = k_vac(DM21, E)
    c, s = math.cos(2 * TH12), math.sin(2 * TH12)
    c13sq = math.cos(TH13) ** 2

    def Hb(r):
        V = c13sq * vcc_km(ne_sun(r))
        H = np.empty((len(r), 2, 2))
        H[:, 0, 0] = (-k * c + V) / 2
        H[:, 1, 1] = -H[:, 0, 0]
        H[:, 0, 1] = H[:, 1, 0] = k * s / 2
        return H
    return Hb


def solar_pee_numeric(E, r_prod, N):
    Hb = solar_hamiltonian(E)
    nodes = np.linspace(r_prod, R_SUN_KM, N + 1)
    psi = propagator(Hb, nodes) @ np.array([1, 0], complex)
    U2 = np.array([[math.cos(TH12), math.sin(TH12)], [-math.sin(TH12), math.cos(TH12)]], complex)
    pm, ovmin = mass_state_probabilities(Hb(np.array([R_SUN_KM]))[0], psi, U2)
    P2 = pm[0] * math.cos(TH12) ** 2 + pm[1] * math.sin(TH12) ** 2
    return math.cos(TH13) ** 4 * P2 + math.sin(TH13) ** 4, pm


def solar_pee_adiabatic(E, r_prod, with_crossing=False):
    c13, s13 = math.cos(TH13), math.sin(TH13)
    k = k_vac(DM21, E)
    V = c13 ** 2 * vcc_km(ne_sun(r_prod))
    c2m = (k * math.cos(2 * TH12) - V) / math.hypot(k * math.cos(2 * TH12) - V, k * math.sin(2 * TH12))
    Pc = 0.0
    if with_crossing:
        # exact crossing probability of an exponential profile with the scale height r0 (Petcov 1988)
        r0 = R_SUN_KM / 10.54
        x = 2 * math.pi * r0 * k
        Pc = (math.exp(-x * math.sin(TH12) ** 2) - math.exp(-x)) / (1 - math.exp(-x)) if x < 700 else 0.0
    return c13 ** 4 * (0.5 + (0.5 - Pc) * math.cos(2 * TH12) * c2m) + s13 ** 4, Pc


# ---------------------------------------------------------------- F2: the supernova envelope
def rho_env(r_km):
    return 1e4 * (np.asarray(r_km) * 1e5 / 1e9) ** -3                     # g/cm^3


def ne_env(r_km):
    return 0.5 * rho_env(r_km) / MU_G


def r_resonance(dm2, c2, E):
    ne = dm2 * c2 / (2 * E * 1e6) / SQRT2GF_EV_CM3                         # FE-50
    rho = ne * MU_G / 0.5
    return (1e4 / rho) ** (1 / 3) * 1e9 / 1e5                             # km


def envelope(E, ordering, anti, N):
    U = pmns()
    m2 = np.diag([0.0, DM21, DM31]) if ordering == 'NO' else np.diag([0.0, DM21, DM21 - DM31])
    # flavour Hamiltonian (FE-48): neutrinos U M^2 U^dag/(2E) + diag(V_CC, 0, 0); antineutrinos U* and -V_CC
    Uu = U.conj() if anti else U
    sgnV = -1.0 if anti else 1.0
    Hv = Uu @ (m2 / (2 * E * 1e6) / HBARC_EV_KM) @ Uu.conj().T

    def Hb(r):
        H = np.broadcast_to(Hv, (len(r), 3, 3)).copy()
        H[:, 0, 0] += sgnV * vcc_km(ne_env(r))
        return H
    dm3 = DM31 if ordering == 'NO' else DM31 - DM21                     # |m_3^2 - m_1^2|, the splitting of the H resonance
    rH = r_resonance(dm3, math.cos(2 * TH13), E)
    rL = r_resonance(DM21, math.cos(2 * TH12), E)
    r0, r1 = 0.2 * rH, 5.0 * rL
    nodes = np.geomspace(r0, r1, N + 1)
    psi = propagator(Hb, nodes) @ np.array([1, 0, 0], complex)
    pm, ovmin = mass_state_probabilities(Hb(np.array([r1]))[0], psi, Uu)
    Pee = float(np.sum(pm * np.abs(Uu[0, :]) ** 2))
    # adiabaticity parameters (FE-50) at both resonances: gamma = dm^2 sin^2 2theta/(2E cos 2theta) / |d ln n_e/dr|, n_e ~ r^-3
    gH = k_vac(dm3, E) * math.sin(2 * TH13) ** 2 / math.cos(2 * TH13) * rH / 3
    gL = k_vac(DM21, E) * math.sin(2 * TH12) ** 2 / math.cos(2 * TH12) * rL / 3
    return {'E_MeV': E, 'ordering': ordering, 'antineutrino': anti, 'P_ee': Pee, 'mass_state_probabilities': pm.tolist(),
            'r_start_km': r0, 'r_end_km': r1, 'r_H_km': rH, 'r_L_km': rL, 'gamma_H': gH, 'gamma_L': gL, 'dm2_H_eV2': dm3,
            'P_LZ_H': math.exp(-math.pi / 2 * gH), 'P_LZ_L': math.exp(-math.pi / 2 * gL), 'steps': N,
            'eigenvector_match_min_overlap': ovmin}


# ---------------------------------------------------------------- F3: the fast instability near the neutrinosphere
def ffi(alpha, Re=30.0, Rb=27.0, r=40.0, nodes=200, Ks=np.linspace(-2.0, 2.0, 401)):
    mu, w = np.polynomial.legendre.leggauss(nodes)
    me = math.sqrt(1 - (Re / r) ** 2)
    mb = math.sqrt(1 - (Rb / r) ** 2)
    # number per unit solid angle (normalised to n_e = 1): uniform over mu > mu_min, solid angle 2 pi (1 - mu_min)
    fe = np.where(mu > me, 1.0 / (2 * math.pi * (1 - me)), 0.0)
    fb = np.where(mu > mb, alpha / (2 * math.pi * (1 - mb)), 0.0)
    G = fe - fb                                  # ELN per solid angle in units of sqrt2 G_F n_e (heavy flavours cancel)
    s = np.sqrt(1 - mu ** 2)
    best = (0.0, None, None, None)
    for m in (0, 1):
        for K in Ks:
            if m == 0:
                A = K * np.diag(mu) - 2 * np.pi * (w * G)[None, :] * (1 - np.outer(mu, mu))
            else:
                A = K * np.diag(mu) + np.pi * (w * G)[None, :] * np.outer(s, s)
            ev = np.linalg.eigvals(A)
            j = int(ev.imag.argmax())
            if ev[j].imag > best[0]:
                best = (float(ev[j].imag), m, float(K), complex(ev[j]))
    g, m, K, Om = best
    disp = None
    if m is not None and g > 1e-6:
        # FE-51 at the solution: det[eta^{mu nu} + int d^2v G v^mu v^nu/(Omega - K v_z)] = 0, block (t, z) for m = 0,
        # transverse block (x, x) for m = 1
        I = [2 * math.pi * np.sum(w * G * mu ** n / (Om - K * mu)) for n in range(3)]
        if m == 0:
            disp = abs((1 + I[0]) * (-1 + I[2]) - I[1] ** 2) / (abs(1 + I[0]) * abs(-1 + I[2]) + abs(I[1]) ** 2)
        else:
            Ixx = math.pi * np.sum(w * G * (1 - mu ** 2) / (Om - K * mu))
            disp = abs(-1 + Ixx) / (1 + abs(Ixx))
    return {'alpha': alpha, 'crossing': bool(G.max() > 0 > G.min()), 'growth_rate_units_sqrt2GF_ne': g, 'mode_m': m,
            'K': K, 'Omega': [Om.real, Om.imag] if Om is not None else None, 'dispersion_relation_relative_residual': disp,
            'mu_min_e': me, 'mu_min_ebar': mb, 'alpha_crossing_threshold': (1 - mb) / (1 - me)}


# ---------------------------------------------------------------- F4: equipartition and heating
def fe52(Fe, Fb, Fx):
    d = np.maximum(2 / 3 * (np.minimum(Fe, Fb) - Fx), np.maximum(Fe, Fb) - 1.0)
    return Fe - d, Fb - d, Fx + d / 2, d


def spectrum(E, mean, alpha_fit=3.0):
    """Normalised number spectrum (the alpha fit of Keil, Raffelt and Janka): f ~ E^alpha exp(-(alpha+1) E/<E>)."""
    f = E ** alpha_fit * np.exp(-(alpha_fit + 1) * E / mean)
    return f / np.trapezoid(f, E)


def main():
    t0 = time.time()
    rep = Report()
    out = {'mixing': {'theta12_deg': math.degrees(TH12), 'theta23_deg': math.degrees(TH23), 'theta13_deg': math.degrees(TH13),
                      'source': 'NuFIT 5.2 (November 2022), normal ordering, without the SK atmospheric data', 'dm21_eV2': DM21, 'dm31_eV2': DM31},
           'method': 'fourth-order commutator-free Magnus integration, step propagators multiplied pairwise'}

    # ---------------- F1: the Sun
    rows = []
    cases = [(0.267, 0.10, 'pp'), (0.862, 0.06, '7Be'), (1.44, 0.10, 'pep'), (5.0, 0.05, '8B'), (8.1, 0.05, '8B'),
             (10.0, 0.05, '8B'), (15.0, 0.05, '8B')]
    for E, rp, src in cases:
        r_prod = rp * R_SUN_KM
        pn, pm = solar_pee_numeric(E, r_prod, 200000)
        pn2, _ = solar_pee_numeric(E, r_prod, 400000)
        pa, _ = solar_pee_adiabatic(E, r_prod)
        pc, Pc = solar_pee_adiabatic(E, r_prod, with_crossing=True)
        rows.append({'E_MeV': E, 'source': src, 'r_prod_over_Rsun': rp, 'P_ee_numeric': pn, 'P_ee_numeric_half_step': pn2,
                     'P_ee_adiabatic': pa, 'P_crossing_exponential_profile': Pc, 'mass_state_probabilities': pm.tolist()})
        print('  Sun %-4s E = %6.3f MeV: P_ee numeric %.6f (half step %.6f), adiabatic %.6f, P_c %.2e' % (
            src, E, pn, pn2, pa, Pc), flush=True)
    vac = math.cos(TH13) ** 4 * (1 - 0.5 * math.sin(2 * TH12) ** 2) + math.sin(TH13) ** 4
    msw = math.cos(TH13) ** 4 * math.sin(TH12) ** 2 + math.sin(TH13) ** 4
    meas = []
    for name, E, P, dP in BOREXINO:
        rp = {'pp': 0.10, '7Be': 0.06, 'pep': 0.10, '8B': 0.05}[name]
        pn, _ = solar_pee_numeric(E, rp * R_SUN_KM, 200000)
        meas.append({'source': name, 'E_MeV': E, 'measured': P, 'error': dP, 'UM4': pn, 'pull': (pn - P) / dP})
    out['F1'] = {'rows': rows, 'vacuum_average_limit': vac, 'full_MSW_limit': msw, 'borexino': meas}
    ok1 = (all(abs(r['P_ee_numeric'] - r['P_ee_numeric_half_step']) < 1e-6 for r in rows)
           and all(abs(r['P_ee_numeric'] - r['P_ee_adiabatic']) < 1e-3 for r in rows)
           and all(r['P_crossing_exponential_profile'] < 1e-10 for r in rows)
           and abs(rows[0]['P_ee_numeric'] - vac) < 0.03 and abs(rows[-1]['P_ee_numeric'] - msw) < 0.02
           and all(abs(m['pull']) < 2 for m in meas))
    rep.check('F1_solar_survival', ok1,
              'P_ee(E) from the exact flavour evolution through the Sun: %s (unchanged to 1e-6 with half the step); equal to the '
              'adiabatic formula of FE-50 to 1e-3, the crossing probability of the exponential profile is below 1e-10 (the Sun '
              'is adiabatic); limits: vacuum average %.3f at low energy, full MSW %.3f at high energy; Borexino: %s' % (
                  ', '.join('%s %.3g MeV %.3f' % (r['source'], r['E_MeV'], r['P_ee_numeric']) for r in rows), vac, msw,
                  ', '.join('%s %.2f +- %.2f (UM-4 %.3f)' % (m['source'], m['measured'], m['error'], m['UM4']) for m in meas)))

    # ---------------- F2: the supernova envelope
    env = []
    for ordering in ('NO', 'IO'):
        for anti in (False, True):
            r = envelope(15.0, ordering, anti, 200000)
            r2 = envelope(15.0, ordering, anti, 400000)
            r['P_ee_half_step'] = r2['P_ee']
            env.append(r)
            print('  envelope %s %-4s: P_ee %.6f (half step %.6f), gamma_H %.0f, gamma_L %.0f' % (
                ordering, 'anti' if anti else 'nu', r['P_ee'], r2['P_ee'], r['gamma_H'], r['gamma_L']), flush=True)
    Ue2 = np.abs(pmns()[0, :]) ** 2
    expect = {('NO', False): Ue2[2], ('NO', True): Ue2[0], ('IO', False): Ue2[1], ('IO', True): Ue2[2]}
    out['F2'] = {'rows': env, 'Ue_squared': Ue2.tolist(),
                 'expected_adiabatic': {'%s %s' % (k[0], 'anti' if k[1] else 'nu'): float(v) for k, v in expect.items()}}
    ok2 = all(abs(r['P_ee'] - expect[(r['ordering'], r['antineutrino'])]) < 1e-4 and abs(r['P_ee'] - r['P_ee_half_step']) < 1e-6
              and r['gamma_H'] > 10 and r['gamma_L'] > 10 for r in env)
    rep.check('F2_supernova_envelope', ok2,
              'exact three-flavour evolution at 15 MeV from 0.2 r_H (%.0f km normal, %.0f km inverted ordering) to 5 r_L = %.0f km '
              'through rho = 1e4 (r/1e9 cm)^-3 g/cm^3: %s; the resonances at r_H = %.0f km (normal ordering, |m3^2 - m1^2| = '
              '%.4g eV^2), %.0f km (inverted, %.4g eV^2) and r_L = %.0f km are adiabatic (gamma_H = %.0f and %.0f, gamma_L = %.0f, '
              'P_LZ = 0), so a nu_e leaves as nu_3 (normal ordering, P_ee = |U_e3|^2 = %.4f) or nu_2 (inverted, |U_e2|^2 = %.4f), '
              'an anti-nu_e as anti-nu_1 (|U_e1|^2 = %.4f) or anti-nu_3 (|U_e3|^2); agreement to 1e-4' % (
                  env[0]['r_start_km'], env[2]['r_start_km'], env[0]['r_end_km'],
                  ', '.join('%s %s %.4f' % (r['ordering'], 'anti' if r['antineutrino'] else 'nu', r['P_ee']) for r in env),
                  env[0]['r_H_km'], env[0]['dm2_H_eV2'], env[2]['r_H_km'], env[2]['dm2_H_eV2'], env[0]['r_L_km'],
                  env[0]['gamma_H'], env[2]['gamma_H'], env[0]['gamma_L'], Ue2[2], Ue2[1], Ue2[0]))

    # ---------------- F3: fast instability near the neutrinosphere
    ff = [ffi(a) for a in (0.5, 0.75, 0.8, 0.95, 1.2)]
    L_erg, Emean_erg, Re_cm = 5e52, 12 * 1.602176634e-6, 30e5
    # the number density of nu_e at 40 km for the same half-isotropic emission from the neutrinosphere R_e = 30 km as the
    # angular distribution of ffi: the surface flux L/(4 pi R_e^2 <E>) with the intensity flux/pi inside the cone mu > mu_e
    # gives n_e = L (1 - mu_e)/(2 pi R_e^2 c <E>)
    n_e = L_erg * (1 - ff[0]['mu_min_e']) / (2 * math.pi * Re_cm ** 2 * 2.99792458e10 * Emean_erg)
    mu_cm = SQRT2GF_EV_CM3 * n_e / HBARC_EV_CM                             # sqrt2 G_F n_e in cm^-1
    for f in ff:
        f['sqrt2GF_ne_per_cm'] = mu_cm
        f['growth_length_cm'] = 1.0 / (f['growth_rate_units_sqrt2GF_ne'] * mu_cm) if f['crossing'] else None
        print('  FFI alpha = %.2f: crossing %s, growth %.4g (m = %s, K = %s), dispersion residual %s' % (
            f['alpha'], f['crossing'], f['growth_rate_units_sqrt2GF_ne'], f['mode_m'], f['K'],
            f['dispersion_relation_relative_residual']), flush=True)
    thr = ff[0]['alpha_crossing_threshold']
    out['F3'] = {'rows': ff, 'n_e_per_cm3': n_e, 'alpha_crossing_threshold': thr}
    ok3 = (all(f['crossing'] == (f['alpha'] > thr) for f in ff)
           and all((f['growth_rate_units_sqrt2GF_ne'] > 1e-6) == f['crossing'] for f in ff)
           and all(f['dispersion_relation_relative_residual'] < 1e-8 for f in ff if f['crossing']))
    rep.check('F3_fast_instability_neutrinosphere', ok3,
              'half-isotropic emission from R_e = 30 km and R_ebar = 27 km seen at r = 40 km: the ELN crosses for alpha > '
              '(1 - mu_ebar)/(1 - mu_e) = %.4f; %s; at every unstable solution FE-51 holds (relative residual < 1e-8); '
              'sqrt2 G_F n_e = %.2f /cm for L = 5e52 erg/s, <E> = 12 MeV (n_e = %.2e /cm^3 at 40 km): the instability grows within centimetres wherever '
              'the ELN crosses and not at all without a crossing' % (
                  thr, '; '.join('alpha = %.2f: crossing %s, growth rate %.3g (m = %s)%s' % (
                      f['alpha'], f['crossing'], f['growth_rate_units_sqrt2GF_ne'], f['mode_m'],
                      (', growth length (factor e) %.2g cm' % f['growth_length_cm']) if f['growth_length_cm'] else '') for f in ff),
                  mu_cm, n_e))

    # ---------------- F4: equipartition and heating in the gain region
    rng = np.random.default_rng(52)
    Fe, Fb, Fx = rng.random(100000), rng.random(100000), rng.random(100000)
    Fe2, Fb2, Fx2, d = fe52(Fe, Fb, Fx)
    Fe3, Fb3, Fx3, d3 = fe52(Fe2, Fb2, Fx2)
    algebra = {'ELN': float(np.abs((Fe2 - Fb2) - (Fe - Fb)).max()), 'nu_number': float(np.abs((Fe2 + 2 * Fx2) - (Fe + 2 * Fx)).max()),
               'antinu_number': float(np.abs((Fb2 + 2 * Fx2) - (Fb + 2 * Fx)).max()),
               'min_occupation': float(min(Fe2.min(), Fb2.min(), Fx2.min())), 'max_occupation': float(max(Fe2.max(), Fb2.max(), Fx2.max())),
               'second_application_max_delta': float(np.abs(d3[np.maximum(Fe2, Fb2) < 1 - 1e-12]).max()),
               'fraction_with_pauli_bound_active': float(np.mean(np.maximum(Fe, Fb) - 1.0 > 2 / 3 * (np.minimum(Fe, Fb) - Fx)))}
    E = np.linspace(0.05, 150, 6000)
    sets = [('accretion phase (0.2 s)', (5.0, 5.0, 2.0), (11.0, 14.0, 16.0)),
            ('accretion phase, softer heavy flavours', (5.0, 5.0, 2.0), (11.0, 14.0, 14.0)),
            ('end of accretion', (4.0, 4.0, 2.5), (11.0, 13.0, 15.0)),
            ('cooling phase (comparable luminosities)', (3.0, 3.0, 3.0), (10.0, 12.0, 14.0))]
    heat_rows = []
    for name, (Le, Lb, Lx), (Ee, Eb, Ex) in sets:
        fe, fb, fx = (Le / Ee) * spectrum(E, Ee), (Lb / Eb) * spectrum(E, Eb), (Lx / Ex) * spectrum(E, Ex)
        fe2, fb2, fx2, dd = fe52(fe, fb, fx)       # number per energy bin; occupations << 1 in the gain region
        heat = lambda a, b: float(np.trapezoid((a + b) * E ** 3, E))
        cons = max(abs(float(np.trapezoid((fe2 - fb2) - (fe - fb), E))), abs(float(np.trapezoid((fe2 + 2 * fx2) - (fe + 2 * fx), E))),
                   abs(float(np.trapezoid(((fe2 + fb2 + 4 * fx2) - (fe + fb + 4 * fx)) * E, E))))
        mean = lambda f: float(np.trapezoid(f * E, E) / np.trapezoid(f, E))
        heat_rows.append({'phase': name, 'L_1e52_erg_s': [Le, Lb, Lx], 'mean_E_MeV': [Ee, Eb, Ex],
                          'N_before': [Le / Ee, Lb / Eb, Lx / Ex],
                          'N_after': [float(np.trapezoid(fe2, E)), float(np.trapezoid(fb2, E)), float(np.trapezoid(fx2, E))],
                          'mean_E_after_MeV': [mean(fe2), mean(fb2), mean(fx2)],
                          'heating_ratio': heat(fe2, fb2) / heat(fe, fb),
                          'conservation_residual': cons})
        print('  equipartition %-40s heating ratio %.3f' % (name, heat_rows[-1]['heating_ratio']), flush=True)
    out['F4'] = {'algebra_random_occupations': algebra, 'gain_region': heat_rows}
    ratios = [r['heating_ratio'] for r in heat_rows]
    ok4 = (max(algebra['ELN'], algebra['nu_number'], algebra['antinu_number']) < 1e-14 and algebra['min_occupation'] >= 0
           and algebra['max_occupation'] <= 1 and algebra['second_application_max_delta'] < 1e-14
           and algebra['fraction_with_pauli_bound_active'] > 0 and max(r['conservation_residual'] for r in heat_rows) < 1e-9
           and min(ratios) < 1 < max(ratios))
    rep.check('F4_equipartition_heating', ok4,
              'FE-52 on 1e5 random occupations: the electron lepton number and the numbers of neutrinos and antineutrinos are '
              'conserved to %.1e, every occupation stays in [%.3f, %.3f], a second application changes nothing (%.1e), the Pauli '
              'bound is active in %.1f%% of the cases; in the gain region (number and energy conserved in every energy bin to '
              '%.1e) the charged-current heating changes by the factor %s (ESTIMATE): equipartition removes absorbable nu_e and '
              'anti-nu_e and hardens their spectra, so it lowers the heating when the heavy-lepton luminosity is well below the '
              'electron-flavour one (accretion phase) and raises it when they are comparable; the sign depends on the spectra, '
              'as in the transport simulations of Gogilashvili and Tamborra, where flavour conversion enhances or suppresses '
              'the explodability and on the whole reduces the energy deposited behind the shock' % (
                  max(algebra['ELN'], algebra['nu_number'], algebra['antinu_number']), algebra['min_occupation'],
                  algebra['max_occupation'], algebra['second_application_max_delta'],
                  100 * algebra['fraction_with_pauli_bound_active'], max(r['conservation_residual'] for r in heat_rows),
                  ', '.join('%.2f (%s)' % (r['heating_ratio'], r['phase']) for r in heat_rows)))

    out['runtime_s'] = round(time.time() - t0, 1)
    (UM4 / 'outputs' / 'flavour.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_4/code/um4_flavour.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    (UM4 / 'reports' / 'flavour_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
