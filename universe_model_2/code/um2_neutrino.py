#!/usr/bin/env python3
"""UM-2 neutrinos: three flavours, their mixing and their flavour conversion (version of 2026-10-18).

The neutrino masses m_1 < m_2 < m_3 (normal ordering, exact x0 eigenvalues: um2_spectra.py) and the PMNS matrix U (the neutrino
tip matrix: um2_flavour.py) define the flavour evolution of a neutrino of momentum p,
    i d psi_alpha/dx4 = [U diag(m_i^2) U^dagger/(2p) + V(x)]_{alpha beta} psi_beta,      V = diag(V_CC, 0, 0) + V_NC 1,
V_CC = sqrt2 G_F n_e (charged current on electrons), V_NC flavour universal; antineutrinos: U -> U*, V -> -V.  In a dense
neutrino gas the density matrices rho_p obey i (d_t + v.grad) rho_p = [Omega_p + V + V_nunu(rho), rho_p] + i C[rho] with
V_nunu = sqrt2 G_F int d^3q/(2pi)^3 (1 - v_p.v_q)(rho_q - rho_bar_q).  Units: eV, km, MeV as stated.

N1  Vacuum oscillations: the exact evolution operator equals the analytic sum formula; unitarity, CPT, the T-odd
    difference P(mu->e) - P(e->mu) = -16 J sin D21 sin D31 sin D32 (D_ij = dm2_ij L/(4E)); reactor, accelerator and
    atmospheric examples.
N2  Matter of constant density: exact evolution, the MSW resonance of the 1-3 sector and the 1-2 sector; DUNE, NOvA, T2K
    appearance probabilities for neutrinos and antineutrinos (delta = 212 deg, normal ordering).
N3  The Sun: the adiabatic survival probability P_ee(E) and the numerical three-flavour evolution through the solar
    electron density (piecewise-constant layers, exact matrix exponentials), averaged over the decoherent mass eigenstates
    on the way to the Earth.
N4  The early Universe: the thermal potential that suppresses mixing above a few MeV, the temperatures at which the
    atmospheric and solar oscillations become active; neutrino decoupling and N_eff for three flavours (momentum-averaged
    temperature equations with Fermi-Dirac energy-transfer rates for massless electrons, the e+- plasma with its mass and the
    finite-temperature QED corrections at O(e^2) and O(e^3)), with separate nu_e and nu_mu,tau temperatures (no oscillations)
    and with one common temperature (efficient oscillations); validated against the published values of the same method.
N5  The cosmic neutrino background today: three mass eigenstates (not flavours), densities, energy densities, velocities,
    flavour content, Omega_nu h^2.
N6  Supernovae: the MSW resonances in the stellar envelope (densities, adiabaticity, Landau-Zener), the flavour survival
    probabilities at the Earth for normal ordering, the observed spectra; the fast flavour instability of the neutrino gas
    near the neutrinosphere (the dispersion relation of the linearised equations; the homogeneous-mode criterion and growth
    rate, checked against the eigenvalues of the discretised linear equations; growth for k != 0 when the homogeneous mode is
    stable; no instability without an ELN crossing), its time and length scales, and the effect of flavour equipartition on
    the charged-current heating behind the shock (schematic; the explosion study of Gogilashvili and Tamborra 2026 is cited for
    the dynamical consequences).
Writes outputs/neutrino.json, figures/fig_neutrino_*.png and reports/neutrino-checks.json.
"""
import cmath
import math
import os
import sys

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import FIG, OUT, Report, read_json, write_json  # noqa: E402
from um2_constants import NEFF_SM, NUFIT60_NO, SUM_MNU_BOUND_EV, val  # noqa: E402
from um2_flavour import mixing_matrix  # noqa: E402

HBARC_EV_M = val('hbar_c_GeV_m') * 1e9          # eV m
HBARC_EV_CM = HBARC_EV_M * 100.0                # eV cm
GF_EV = val('G_F_GeV-2') * 1e-18                # eV^-2
NA = val('N_A')
SQ2GF_CM3 = math.sqrt(2) * GF_EV * HBARC_EV_CM ** 3   # V = SQ2GF_CM3 * n[cm^-3]  (eV)
KM_TO_INV_EV = 1e3 / HBARC_EV_M                 # 1 km in eV^-1


# ----------------------------------------------------------------------------------------------------------------------
# flavour evolution
def hamiltonian(U, m2, E, V):
    """H = U diag(m2) U^dagger/(2E) + diag(V, 0, 0), E in eV, m2 in eV^2, V in eV (neutrinos)."""
    return U @ np.diag(m2) @ U.conj().T / (2 * E) + np.diag([V, 0.0, 0.0])


def evolve_const(H, L_inv_eV):
    """exp(-i H L) for a Hermitian H (L in eV^-1)."""
    w, Q = np.linalg.eigh(H)
    return Q @ np.diag(np.exp(-1j * w * L_inv_eV)) @ Q.conj().T


def prob_matrix(S):
    """P[beta, alpha] = |S_beta alpha|^2 = P(nu_alpha -> nu_beta)."""
    return np.abs(S) ** 2


def p_vac_formula(U, m2, E, L_inv_eV, a, b):
    """Analytic vacuum probability P(a -> b) = |sum_i U_bi U*_ai exp(-i m_i^2 L/2E)|^2."""
    amp = sum(U[b, i] * np.conj(U[a, i]) * cmath.exp(-1j * m2[i] * L_inv_eV / (2 * E)) for i in range(3))
    return abs(amp) ** 2


def evolve_layers(U, m2, E, V_list, dx_inv_eV):
    """Product of exact layer propagators (piecewise-constant potential), batched eigendecomposition."""
    n = len(V_list)
    H = np.broadcast_to(U @ np.diag(m2) @ U.conj().T / (2 * E), (n, 3, 3)).copy()
    H[:, 0, 0] += V_list
    w, Q = np.linalg.eigh(H)
    ph = np.exp(-1j * w * dx_inv_eV[:, None])
    S_layers = np.einsum('nij,nj,nkj->nik', Q, ph, Q.conj())
    # multiply in order (first layer acts first): S = S_n ... S_2 S_1, by pairwise reduction
    mats = list(S_layers)
    while len(mats) > 1:
        nxt = []
        for k in range(0, len(mats) - 1, 2):
            nxt.append(mats[k + 1] @ mats[k])
        if len(mats) % 2:
            nxt.append(mats[-1])
        mats = nxt
    return mats[0]


# ----------------------------------------------------------------------------------------------------------------------
# early-Universe thermodynamics
ALPHA = 1 / val('alpha_inv_0')
E2 = 4 * math.pi * ALPHA
ME = val('m_e_MeV')                     # MeV
MPL = val('M_Pl_GeV') * 1e3             # MeV


def _panels(umax):
    """Gauss-Legendre nodes and weights on [0, umax] in panels (u = p/T)."""
    edges = [0.0, 2.0, 6.0, 15.0, 30.0, umax]
    xs, ws = [], []
    x0, w0 = np.polynomial.legendre.leggauss(80)
    for a, b in zip(edges[:-1], edges[1:]):
        xs.append(0.5 * (b - a) * x0 + 0.5 * (b + a))
        ws.append(0.5 * (b - a) * w0)
    return np.concatenate(xs), np.concatenate(ws)


def plasma_terms(T, m=ME):
    """e+ e- thermodynamics (g = 4, zero chemical potential) and the finite-temperature QED corrections to the pressure of the
    e+ e- gamma plasma (Bennett et al., arXiv:1911.04504, eqs. 4.7, 4.24-4.25):
        P2 = -(e^2 T^2/(12 pi^2)) J1 - (e^2/(8 pi^4)) J1^2 + (e^2 m^2/(16 pi^4)) J2,      P3 = (e^3 T/(12 pi^4)) I^{3/2},
        J1 = int dp p^2/E n_D,  J2 = int int dp dq (p q/(E_p E_q)) ln|(p+q)/(p-q)| n_D(p) n_D(q),  I = int dp (p^2 + E^2)/E n_D,
    n_D = 2/(e^{E/T} + 1).  J2 = 2 int dp f(p) int_0^1 ds 2 s p f(p(1 - s^2)) ln((2 - s^2)/s^2), f(p) = p n_D(p)/E_p (q = p(1 - s^2)).
    Returns rho_e, p_e, d rho_e/dT, P2, P3 (MeV units)."""
    x = m / T
    u, w = _panels(60.0 + 10.0 * x)
    E = np.sqrt(u * u + x * x)                      # in units of T
    ex = np.exp(-E)
    nF = ex / (1.0 + ex)                            # 1/(e^E + 1), overflow-safe
    g = 4.0
    rho = g / (2 * math.pi ** 2) * T ** 4 * np.sum(w * u * u * E * nF)
    pre = g / (6 * math.pi ** 2) * T ** 4 * np.sum(w * u ** 4 / E * nF)
    drho = g / (2 * math.pi ** 2) * T ** 3 * np.sum(w * u * u * E * E * nF * (1 - nF))
    nD = 2 * nF
    J1 = T * T * np.sum(w * u * u / E * nD)
    Ii = T * T * np.sum(w * (u * u + E * E) / E * nD)
    s0, ws0 = np.polynomial.legendre.leggauss(200)
    sv = 0.5 * (s0 + 1)
    wsv = 0.5 * ws0
    q = u[:, None] * (1 - sv[None, :] ** 2)
    Eq = np.sqrt(q * q + x * x)
    eq = np.exp(-Eq)
    fq = q / Eq * 2 * eq / (1 + eq)
    inner = np.sum(wsv[None, :] * fq * np.log((2 - sv[None, :] ** 2) / sv[None, :] ** 2) * 2 * sv[None, :] * u[:, None], axis=1)
    fp = u / E * nD
    J2 = 2 * T * T * np.sum(w * fp * inner)
    P2 = -E2 * T * T / (12 * math.pi ** 2) * J1 - E2 / (8 * math.pi ** 4) * J1 ** 2 + E2 * m * m / (16 * math.pi ** 4) * J2
    P3 = E2 ** 1.5 * T / (12 * math.pi ** 4) * Ii ** 1.5
    return float(rho), float(pre), float(drho), float(P2), float(P3)


class Plasma:
    """Tabulated e+- thermodynamics and the QED pressure corrections on a grid in ln T (MeV); spline derivatives.
    qed_order: 0 (none), 2 (O(e^2)), 3 (O(e^2) + O(e^3))."""

    def __init__(self, table, qed_order=3):
        lnT, rows = table
        self.rho_e = CubicSpline(lnT, np.log(rows[:, 0]))
        self.p_e = CubicSpline(lnT, np.log(rows[:, 1]))
        self.drho_e = CubicSpline(lnT, np.log(rows[:, 2]))
        self.qed_order = qed_order
        T = np.exp(lnT)
        if qed_order:
            Pint = rows[:, 3] + (rows[:, 4] if qed_order == 3 else 0.0)
            self.phi = CubicSpline(lnT, Pint / T ** 4)      # P_int = T^4 phi(ln T)

    def e_state(self, T):
        x = math.log(T)
        return math.exp(self.rho_e(x)), math.exp(self.p_e(x)), math.exp(self.drho_e(x))

    def qed(self, T):
        """P_int, dP_int/dT, d2P_int/dT2, rho_int = -P_int + T dP_int/dT."""
        if not self.qed_order:
            return 0.0, 0.0, 0.0, 0.0
        x = math.log(T)
        ph, d1, d2 = float(self.phi(x)), float(self.phi(x, 1)), float(self.phi(x, 2))
        P = T ** 4 * ph
        dP = T ** 3 * (4 * ph + d1)
        d2P = T ** 2 * (12 * ph + 7 * d1 + d2)
        return P, dP, d2P, -P + T * dP


def plasma_table(Tmin=0.002, Tmax=30.0, n=400):
    lnT = np.linspace(math.log(Tmin), math.log(Tmax), n)
    rows = np.array([plasma_terms(math.exp(t)) for t in lnT])
    return lnT, rows


def F_rate(T1, T2, fa=0.884, fs=0.829):
    """Escudero's energy-transfer kernel F(T1, T2) = 32 f_a (T1^9 - T2^9) + 56 f_s T1^4 T2^4 (T1 - T2) (FD factors f_a, f_s)."""
    return 32 * fa * (T1 ** 9 - T2 ** 9) + 56 * fs * T1 ** 4 * T2 ** 4 * (T1 - T2)


def neff_run(plasma, couplings, common=False, Tstart=20.0, Tend=0.005, GF=val('G_F_GeV-2') * 1e-6):
    """Neutrino decoupling: dT/dx4 equations (Escudero, arXiv:2001.04466, eqs. 3.2-3.3), MeV units. Returns N_eff and history."""
    geL, geR, gmL, gmR = couplings
    rho_nu1 = lambda T: 7 * math.pi ** 2 / 120 * T ** 4          # one flavour, nu + nubar
    drho_nu1 = lambda T: 7 * math.pi ** 2 / 30 * T ** 3

    def rates(Tg, Te, Tm):
        dre = GF ** 2 / math.pi ** 5 * (4 * (geL ** 2 + geR ** 2) * F_rate(Tg, Te) + 2 * F_rate(Tm, Te))
        drm = GF ** 2 / math.pi ** 5 * (4 * (gmL ** 2 + gmR ** 2) * F_rate(Tg, Tm) - F_rate(Tm, Te))
        return dre, drm

    def rhs(t, y):
        Tg, Te, Tm = math.exp(y[0]), math.exp(y[1]), math.exp(y[2])
        rho_g = math.pi ** 2 / 15 * Tg ** 4
        re, pe, dre_dT = plasma.e_state(Tg)
        P, dP, d2P, rint = plasma.qed(Tg)
        rho = rho_g + re + rint + rho_nu1(Te) + 2 * rho_nu1(Tm)
        Hh = math.sqrt(8 * math.pi * rho / 3) / MPL
        dre, drm = rates(Tg, Te, Tm)
        num = 4 * Hh * rho_g + 3 * Hh * (re + pe) + 3 * Hh * Tg * dP + dre + 2 * drm
        den = 4 * math.pi ** 2 / 15 * Tg ** 3 + dre_dT + Tg * d2P
        dTg = -num / den
        if common:
            dT = -Hh * Te + (dre + 2 * drm) / (3 * drho_nu1(Te))
            dTe = dTm = dT
        else:
            dTe = -Hh * Te + dre / drho_nu1(Te)
            dTm = -Hh * Tm + drm / drho_nu1(Tm)
        return [dTg / Tg, dTe / Te, dTm / Tm, Hh]

    def stop(t, y):
        return y[0] - math.log(Tend)
    stop.terminal = True
    y0 = [math.log(Tstart)] * 3 + [0.0]                         # the last variable is ln a (a = 1 at the start)
    sol = solve_ivp(rhs, (0.0, 1e30), y0, method='LSODA', rtol=1e-11, atol=1e-13, events=stop, dense_output=False,
                    first_step=1e-6, max_step=np.inf)
    Tg, Te, Tm = np.exp(sol.y[:3, -1])
    neff = (11.0 / 4.0) ** (4.0 / 3.0) * ((Te / Tg) ** 4 + 2 * (Tm / Tg) ** 4)
    return {'N_eff': float(neff), 'Tnu_e_over_Tgamma': float(Te / Tg), 'Tnu_mu_over_Tgamma': float(Tm / Tg),
            'Tgamma_end_MeV': float(Tg), 'steps': int(sol.t.size), 'status': int(sol.status),
            'heating_Te_a': float(Te * math.exp(sol.y[3, -1]) / Tstart - 1), 'heating_Tm_a': float(Tm * math.exp(sol.y[3, -1]) / Tstart - 1),
            'history': {'Tgamma': np.exp(sol.y[0][::max(1, sol.t.size // 200)]).tolist(),
                        'Te_a_rel': (np.exp(sol.y[1] + sol.y[3]) / Tstart - 1)[::max(1, sol.t.size // 200)].tolist(),
                        'Tm_a_rel': (np.exp(sol.y[2] + sol.y[3]) / Tstart - 1)[::max(1, sol.t.size // 200)].tolist(),
                        'Te_over_Tg': (np.exp(sol.y[1] - sol.y[0])[::max(1, sol.t.size // 200)]).tolist(),
                        'Tm_over_Tg': (np.exp(sol.y[2] - sol.y[0])[::max(1, sol.t.size // 200)]).tolist()}}


def neff_instantaneous(plasma, Td=2.0, Tend=0.005):
    """Instantaneous decoupling at Td: neutrinos redshift freely; the plasma conserves its entropy
    s = (rho + p)/T with rho_int, p_int = P_int included (QED corrections)."""
    def s_plasma(T):
        re, pe, _ = plasma.e_state(T)
        P, dP, d2P, rint = plasma.qed(T)
        rho_g = math.pi ** 2 / 15 * T ** 4
        return (rho_g + rho_g / 3 + re + pe + rint + P) / T
    # a^3 s = const: (a_end/a_d)^3 = s(Td)/s(Tend); T_nu = Td a_d/a_end
    a_ratio = (s_plasma(Td) / s_plasma(Tend)) ** (1.0 / 3.0)       # a_end/a_d
    Tnu = Td / a_ratio
    return float(3 * (11.0 / 4.0) ** (4.0 / 3.0) * (Tnu / Tend) ** 4)


# ----------------------------------------------------------------------------------------------------------------------
# fast flavour instability (axisymmetric, k along the symmetry axis)
def eln_moments(G, nquad=400):
    u, w = np.polynomial.legendre.leggauss(nquad)
    g = G(u)
    return [float(np.sum(w * g * u ** n) / 2) for n in range(3)]


def homogeneous_growth(G):
    """k = 0 axisymmetric mode: omega^2 - (I2 - I0) omega - (I0 I2 - I1^2) = 0; complex iff (I0 + I2)^2 < 4 I1^2."""
    I0, I1, I2 = eln_moments(G)
    D = (I0 + I2) ** 2 - 4 * I1 ** 2
    return (math.sqrt(-D) / 2 if D < 0 else 0.0), D, (I0, I1, I2)


def homogeneous_growth_matrix(G, n=200):
    """Eigenvalues of the discretised linear equation of the homogeneous axisymmetric mode,
    i dS_u/dx4 = (Lam^0 - u Lam^3) S_u - int du'/2 G(u') (1 - u u') S_u'."""
    u, w = np.polynomial.legendre.leggauss(n)
    g = G(u)
    lam0 = np.sum(w * g) / 2
    lam3 = np.sum(w * g * u) / 2
    A = np.diag(lam0 - u * lam3) - (1 - np.outer(u, u)) * (w * g / 2)[None, :]
    ev = np.linalg.eigvals(A)
    return float(np.max(ev.imag)), ev


def dispersion_axisym(G, omega, k, nquad=600):
    """f(omega) = det of the axisymmetric (0, 3) block of Pi^{mu nu} = eta^{mu nu} + int du/2 G(u) v^mu v^nu/(omega - k u),
    v = (1, u), eta = diag(1, -1): f = (1 + J0)(-1 + J2) - J1^2, J_n = int du/2 G u^n/(omega - k u); and df/domega.
    omega may be an array (vectorised)."""
    u, w = np.polynomial.legendre.leggauss(nquad)
    gw = G(u) * w / 2
    om = np.atleast_1d(np.asarray(omega, dtype=complex))
    den = om[:, None] - k * u[None, :]
    inv = 1.0 / den
    inv2 = inv * inv
    J = [np.sum(gw * u ** n * inv, axis=1) for n in range(3)]
    dJ = [-np.sum(gw * u ** n * inv2, axis=1) for n in range(3)]
    f = (1 + J[0]) * (-1 + J[2]) - J[1] ** 2
    df = dJ[0] * (-1 + J[2]) + (1 + J[0]) * dJ[2] - 2 * J[1] * dJ[1]
    return f, df


def dispersion_nonaxisym(G, omega, k, nquad=600):
    """The azimuthal (non-axisymmetric) branch for k along the axis: Pi^{11} = -1 + int du/2 G (1 - u^2)/2/(omega - k u) = 0; and its
    derivative."""
    u, w = np.polynomial.legendre.leggauss(nquad)
    gw = G(u) * w / 2 * (1 - u * u) / 2
    om = np.atleast_1d(np.asarray(omega, dtype=complex))
    inv = 1.0 / (om[:, None] - k * u[None, :])
    return -1 + np.sum(gw * inv, axis=1), -np.sum(gw * inv * inv, axis=1)


def max_growth_over_k(G, ks, guess_scale, nstart_re=15, im_starts=(0.01, 0.05, 0.2, 0.6), branch=dispersion_axisym):
    """For each real k: vectorised Newton iterations from a grid of complex starting points for the roots of the axisymmetric
    dispersion relation with Im omega > 0; the largest converged growth rate per k and overall."""
    best = (0.0, None, None)
    rows = []
    re0 = np.linspace(-2.0, 2.0, nstart_re) * guess_scale
    starts = np.array([complex(r, i * guess_scale) for r in re0 for i in im_starts])
    for k in ks:
        w = starts.copy()
        alive = np.ones(w.size, dtype=bool)
        conv = np.zeros(w.size, dtype=bool)
        for _ in range(100):
            idx = np.where(alive & ~conv)[0]
            if idx.size == 0:
                break
            f, df = branch(G, w[idx], k)
            step = np.where(df != 0, f / np.where(df != 0, df, 1), 0)
            w[idx] = w[idx] - step
            bad = (w[idx].imag < 1e-10 * guess_scale) | ~np.isfinite(w[idx]) | (np.abs(w[idx]) > 50 * guess_scale + 10 * abs(k))
            alive[idx[bad]] = False
            done = np.abs(step) < 1e-13 * max(guess_scale, 1e-3)
            conv[idx[done & ~bad]] = True
        top, topw = 0.0, None
        if conv.any():
            fz, _ = branch(G, w[conv], k)
            good = np.abs(fz) < 1e-9
            cand = w[conv][good]
            if cand.size:
                j = int(np.argmax(cand.imag))
                top, topw = float(cand[j].imag), complex(cand[j])
        rows.append((float(k), top))
        if top > best[0]:
            best = (top, float(k), topw)
    return best, rows


# ----------------------------------------------------------------------------------------------------------------------
def main():
    rep = Report('neutrino-checks', 'UM-2 neutrinos: three flavours, mixing and flavour conversion (vacuum, matter, the Sun, the early '
                 'Universe and N_eff, the CNB, supernovae and the fast flavour instability)')
    out = {}
    masses = read_json(os.path.join(OUT, 'masses.json'))
    mn = masses['neutrino_masses_eV']
    m = np.array([mn['m1'], mn['m2'], mn['m3']])
    m2 = m ** 2
    nu = {k: v[0] for k, v in NUFIT60_NO.items()}
    s12, s13, s23 = math.sqrt(nu['sin2_theta12']), math.sqrt(nu['sin2_theta13']), math.sqrt(nu['sin2_theta23'])
    dl = math.radians(nu['delta_CP_deg'])
    U = mixing_matrix(s12, s13, s23, dl)
    fl = read_json(os.path.join(OUT, 'flavour.json'))
    J = fl['PMNS']['J']
    out['masses_eV'] = m.tolist()
    out['sum_masses_eV'] = float(m.sum())
    rep.check('masses_and_cosmological_bound', abs((m2[1] - m2[0]) / nu['dm2_21_eV2'] - 1) < 1e-9 and abs((m2[2] - m2[0]) / nu['dm2_31_eV2'] - 1) < 1e-9
              and m.sum() < SUM_MNU_BOUND_EV[0],
              'normal ordering: m = %.4e, %.4e, %.4e eV (m1 chosen), dm2_21 = %.3e, dm2_31 = %.4e eV^2 (NuFIT 6.0); sum = %.4f eV < %.3f eV '
              '(DESI DR2 + CMB, 95 %%)' % (m[0], m[1], m[2], m2[1] - m2[0], m2[2] - m2[0], m.sum(), SUM_MNU_BOUND_EV[0]))

    # ---------------- N1 vacuum ----------------
    worst = 0.0
    unit = 0.0
    cpt = 0.0
    todd = 0.0
    for (Lkm, EMeV) in [(1.65, 4.0), (52.5, 4.0), (295.0, 600.0), (810.0, 2000.0), (1300.0, 2500.0), (12742.0, 10000.0)]:
        E = EMeV * 1e6
        Li = Lkm * KM_TO_INV_EV
        S = evolve_const(hamiltonian(U, m2, E, 0.0), Li)
        Sb = evolve_const(hamiltonian(U.conj(), m2, E, 0.0), Li)
        P = prob_matrix(S)
        Pb = prob_matrix(Sb)
        for a in range(3):
            for b in range(3):
                worst = max(worst, abs(P[b, a] - p_vac_formula(U, m2, E, Li, a, b)))
        unit = max(unit, float(np.max(np.abs(P.sum(axis=0) - 1))), float(np.max(np.abs(P.sum(axis=1) - 1))))
        cpt = max(cpt, float(np.max(np.abs(P - Pb.T))))
        D = [None, (m2[1] - m2[0]) * Li / (4 * E), (m2[2] - m2[0]) * Li / (4 * E), (m2[2] - m2[1]) * Li / (4 * E)]
        todd = max(todd, abs((P[0, 1] - P[1, 0]) - (-16 * J * math.sin(D[1]) * math.sin(D[2]) * math.sin(D[3]))))
    rep.check('vacuum_oscillations', worst < 1e-12 and unit < 1e-12 and cpt < 1e-12 and todd < 1e-12,
              'exact evolution exp(-i H L) against the analytic formula P(a->b) = |sum_i U_bi U*_ai e^{-i m_i^2 L/2E}|^2: %.1e; unitarity '
              '%.1e; CPT P(a->b) = Pbar(b->a): %.1e; T-odd difference P(mu->e) - P(e->mu) = -16 J sin D21 sin D31 sin D32 to %.1e '
              '(reactor, accelerator and atmospheric baselines)' % (worst, unit, cpt, todd))
    E_reac = 4e6
    reac = {}
    for Lkm in (1.65, 52.5, 180.0):
        Li = Lkm * KM_TO_INV_EV
        reac[str(Lkm)] = 1 - 0 + 0
        S = evolve_const(hamiltonian(U.conj(), m2, E_reac, 0.0), Li)
        reac[str(Lkm)] = float(prob_matrix(S)[0, 0])
    out['reactor_antinu_e_survival_4MeV'] = reac
    # atmospheric-scale vacuum nu_mu survival over L/E
    LE = np.linspace(10, 2000, 400)                    # km/GeV
    Pmumu = []
    for le in LE:
        S = evolve_const(hamiltonian(U, m2, 1e9, 0.0), le * KM_TO_INV_EV)
        Pmumu.append(prob_matrix(S)[1, 1])
    out['vacuum_Pmumu_min'] = float(min(Pmumu))
    out['vacuum_Pmumu_LE_at_min_km_per_GeV'] = float(LE[int(np.argmin(Pmumu))])

    # ---------------- N2 constant-density matter ----------------
    def V_of_rho(rho, Ye=0.5):
        return SQ2GF_CM3 * rho * Ye * NA
    lbl = {}
    for name, Lkm, EMeV, rho in [('T2K', 295.0, 600.0, 2.6), ('NOvA', 810.0, 2000.0, 2.84), ('DUNE', 1300.0, 2500.0, 2.848)]:
        E = EMeV * 1e6
        Vm = V_of_rho(rho)
        Li = Lkm * KM_TO_INV_EV
        Pn = prob_matrix(evolve_const(hamiltonian(U, m2, E, Vm), Li))
        Pa = prob_matrix(evolve_const(hamiltonian(U.conj(), m2, E, -Vm), Li))
        Pv = prob_matrix(evolve_const(hamiltonian(U, m2, E, 0.0), Li))
        lbl[name] = {'L_km': Lkm, 'E_MeV': EMeV, 'rho': rho, 'P_mue_nu': float(Pn[0, 1]), 'P_mue_antinu': float(Pa[0, 1]),
                     'P_mue_nu_vacuum': float(Pv[0, 1]), 'P_mumu_nu': float(Pn[1, 1])}
    out['long_baseline'] = lbl
    # MSW resonance energies.  1-3: rotating the flavour basis by R23 (which commutes with diag(V, 0, 0)) leaves, for dm2_21 -> 0, a
    # two-flavour (e, tau') problem with angle theta13 and the full potential V: 2 E V = dm2_31 cos 2theta13; with dm2_21 the
    # effective splitting is dm2_ee = c12^2 dm2_31 + s12^2 dm2_32 = dm2_31 - s12^2 dm2_21.  1-2 (the Sun): after the 1-3 rotation the
    # 1-2 problem sees V c13^2: 2 E V c13^2 = dm2_21 cos 2theta12.  The exact three-flavour resonance is where the heaviest matter
    # eigenstate is half nu_e, |U_e3^m|^2 = 1/2 (root of the exact Hamiltonian).
    Vm = V_of_rho(2.8)
    c2t13 = 1 - 2 * nu['sin2_theta13']
    dm2_ee = nu['dm2_31_eV2'] - nu['sin2_theta12'] * nu['dm2_21_eV2']
    E_res13 = dm2_ee * c2t13 / (2 * Vm)
    E_res13_2fl = nu['dm2_31_eV2'] * c2t13 / (2 * Vm)

    def ue3_matter(E):
        wr_, Qr_ = np.linalg.eigh(hamiltonian(U, m2, E, Vm))
        return abs(Qr_[0, 2]) ** 2
    E_res13_exact = brentq(lambda E: ue3_matter(E) - 0.5, 0.3 * E_res13, 3.0 * E_res13, xtol=1e-6 * E_res13)
    E_res12_sun = nu['dm2_21_eV2'] * (1 - 2 * nu['sin2_theta12']) / (2 * SQ2GF_CM3 * 100 * NA * (1 - nu['sin2_theta13']))
    out['MSW_resonance'] = {'E_res_13_rho2p8_GeV': E_res13 * 1e-9, 'E_res_13_rho2p8_exact_GeV': E_res13_exact * 1e-9,
                            'E_res_13_rho2p8_dm2_31_only_GeV': E_res13_2fl * 1e-9, 'E_res_12_sun_center_MeV': E_res12_sun * 1e-6,
                            'Ue3_matter_at_formula_energy': ue3_matter(E_res13)}
    rep.check('MSW_resonance_13', abs(E_res13 / E_res13_exact - 1) < 1e-3,
              'the 1-3 MSW resonance in matter of rho = 2.8 g/cm^3 (Y_e = 0.5): E_res = dm2_ee cos(2 theta13)/(2 V) = %.3f GeV (dm2_ee = c12^2 dm2_31 '
              '+ s12^2 dm2_32) against the exact three-flavour resonance |U_e3^m|^2 = 1/2 at %.3f GeV (relative %.1e; with dm2_31 alone %.2f GeV); '
              'the 1-2 resonance at the centre of the Sun (2 E V c13^2 = dm2_21 cos 2theta12) lies at %.2f MeV' % (
                  E_res13 * 1e-9, E_res13_exact * 1e-9, E_res13 / E_res13_exact - 1, E_res13_2fl * 1e-9, E_res12_sun * 1e-6))
    rep.check('long_baseline_matter_and_CP', all(abs(v['P_mue_nu'] - v['P_mue_antinu']) > 1e-3 for v in lbl.values()),
              'nu_mu -> nu_e appearance (normal ordering, delta = 212 deg, matter of constant density): ' + '; '.join(
                  '%s %.0f km %.1f GeV: P(nu) = %.4f, P(antinu) = %.4f (vacuum %.4f)' % (k, v['L_km'], v['E_MeV'] / 1e3, v['P_mue_nu'],
                                                                                 v['P_mue_antinu'], v['P_mue_nu_vacuum'])
                  for k, v in lbl.items()))

    # ---------------- N3 the Sun ----------------
    RSUN_KM = 6.957e5

    def ne_sun(x):
        """electron density (cm^-3): Bahcall's exponential fit 245 N_A exp(-10.54 x) outside the core, flat at 100 N_A inside
        (x = r/R_sun) (ASSUMED profile)."""
        return NA * np.minimum(245.0 * np.exp(-10.54 * x), 100.0)
    c13sq = 1 - nu['sin2_theta13']

    def pee_adiabatic(E, x0):
        V0 = SQ2GF_CM3 * ne_sun(x0)
        A = 2 * E * V0 * c13sq / nu['dm2_21_eV2']
        c2 = 1 - 2 * nu['sin2_theta12']
        s2 = math.sqrt(1 - c2 * c2)
        c2m = (c2 - A) / math.sqrt((c2 - A) ** 2 + s2 * s2)
        return c13sq ** 2 * (0.5 + 0.5 * c2 * c2m) + nu['sin2_theta13'] ** 2

    def pee_numeric(E, x0, nl):
        xs = np.linspace(x0, 1.0, nl + 1)
        xm = 0.5 * (xs[1:] + xs[:-1])
        Vl = SQ2GF_CM3 * ne_sun(xm)
        dx = np.diff(xs) * RSUN_KM * KM_TO_INV_EV
        S = evolve_layers(U, m2, E, Vl, dx)
        amp = S[:, 0]                       # state after propagation from nu_e
        p_mass = np.abs(U.conj().T @ amp) ** 2   # probabilities of the vacuum mass eigenstates at the surface
        return float(np.sum(np.abs(U[0, :]) ** 2 * p_mass))
    solar = []
    for EMeV, x0, lab in [(0.3, 0.1, 'pp'), (0.862, 0.06, '7Be'), (1.44, 0.07, 'pep'), (5.0, 0.05, '8B'), (10.0, 0.05, '8B'),
                          (15.0, 0.05, '8B')]:
        E = EMeV * 1e6
        pa = pee_adiabatic(E, x0)
        pn1 = pee_numeric(E, x0, 20000)
        pn2 = pee_numeric(E, x0, 40000)
        solar.append({'E_MeV': EMeV, 'source': lab, 'x_production': x0, 'P_ee_adiabatic': pa, 'P_ee_numeric_20000': pn1,
                      'P_ee_numeric_40000': pn2})
    out['solar'] = solar
    dev = max(abs(s['P_ee_numeric_40000'] - s['P_ee_adiabatic']) for s in solar)
    conv = max(abs(s['P_ee_numeric_40000'] - s['P_ee_numeric_20000']) for s in solar)
    rep.check('solar_MSW', dev < 5e-3 and conv < 1e-4 and solar[0]['P_ee_adiabatic'] > 0.5 and solar[4]['P_ee_adiabatic'] < 0.36,
              'solar nu_e survival (decoherent at the Earth): P_ee = %s; the numerical three-flavour evolution through the solar electron '
              'density (40000 layers) agrees with the adiabatic formula c13^4 (1/2 + 1/2 cos 2theta12 cos 2theta12^m) + s13^4 to %.1e '
              '(layer convergence %.1e): the MSW conversion is adiabatic; vacuum-dominated at low energy, matter-dominated for 8B' % (
                  ', '.join('%.2f MeV (%s) %.4f' % (s['E_MeV'], s['source'], s['P_ee_numeric_40000']) for s in solar), dev, conv))

    # ---------------- N4 the early Universe ----------------
    mW = val('m_W_GeV') * 1e9                       # eV

    def T_onset(dm2, c2):
        """|V_e - V_mu| = (8 sqrt2 G_F p/(3 m_W^2)) rho_{e+-} with rho_{e+-} = (7 pi^2/60) T^4 and p = 3.15 T equal to dm2 cos2/(2p)."""
        coef = 8 * math.sqrt(2) * GF_EV / (3 * mW ** 2) * 7 * math.pi ** 2 / 60
        f = lambda T: coef * 3.15 * T ** 5 - dm2 * c2 / (2 * 3.15 * T)
        return brentq(f, 1e4, 1e9)
    T13 = T_onset(nu['dm2_31_eV2'], 1 - 2 * nu['sin2_theta13'])
    T12 = T_onset(nu['dm2_21_eV2'], 1 - 2 * nu['sin2_theta12'])
    out['oscillation_onset_T_MeV'] = {'atmospheric_13': T13 * 1e-6, 'solar_12': T12 * 1e-6}
    rep.check('early_universe_oscillation_onset', 3.0 < T13 * 1e-6 < 8.0 and 1.5 < T12 * 1e-6 < 4.0,
              'the thermal potential of the e+- plasma, V_e - V_mu = -(8 sqrt2 G_F p/(3 m_W^2)) (7 pi^2/60) T^4 (m_W of the UM-2 fit), suppresses '
              'the mixing until it falls below dm2 cos(2 theta)/(2p) at p = 3.15 T: the atmospheric oscillations start at T = %.2f MeV, the solar ones '
              'at T = %.2f MeV, i.e. around neutrino decoupling: flavour conversion is active while the neutrinos decouple' % (T13 * 1e-6, T12 * 1e-6))
    table = plasma_table()
    plasma = Plasma(table, qed_order=3)
    plasma2 = Plasma(table, qed_order=2)
    plasma0 = Plasma(table, qed_order=0)
    # checks of the plasma integrals: massless limits of the QED terms and of the e+- energy density at high T
    Thi = 30.0
    r_hi = plasma_terms(Thi, m=1e-9)
    lim_ok = abs(r_hi[3] / (-5 * E2 * Thi ** 4 / 288) - 1) < 1e-6 and abs(r_hi[4] / (E2 ** 1.5 * Thi ** 4 / (36 * math.sqrt(3) * math.pi)) - 1) < 1e-6 \
        and abs(r_hi[0] / (7 * math.pi ** 2 / 60 * Thi ** 4) - 1) < 1e-9
    rep.check('plasma_integrals', lim_ok,
              'massless limits: P2 = -5 e^2 T^4/288 to %.1e, P3 = e^3 T^4/(36 sqrt3 pi) to %.1e, rho_e = (7 pi^2/60) T^4 to %.1e '
              '(Gauss-Legendre panels; the logarithmic singularity of J2 removed by q = p(1 - s^2))' % (
                  abs(r_hi[3] / (-5 * E2 * Thi ** 4 / 288) - 1), abs(r_hi[4] / (E2 ** 1.5 * Thi ** 4 / (36 * math.sqrt(3) * math.pi)) - 1),
                  abs(r_hi[0] / (7 * math.pi ** 2 / 60 * Thi ** 4) - 1)))
    # Escudero's effective low-energy couplings with radiative corrections (arXiv:2001.04466, read 2026-10-18): g_eL = 0.727, g_eR = 0.233,
    # g_muL = -0.273, g_muR = 0.233 (the tree-level forms are 1/2 + s^2, s^2, -1/2 + s^2, s^2)
    cE = (0.727, 0.233, -0.273, 0.233)
    s2c = 1 - (val('m_W_GeV') / val('m_Z_GeV')) ** 2 / (1 + val('rho0_minus_1'))      # UM-2 tree-level angle of the couplings
    cU = (0.5 + s2c, s2c, -0.5 + s2c, s2c)
    runs = {}
    runs['instantaneous_noQED'] = neff_instantaneous(plasma0, Td=20.0)
    runs['instantaneous_LO'] = neff_instantaneous(plasma2, Td=20.0)
    runs['instantaneous_NLO'] = neff_instantaneous(plasma, Td=20.0)
    runs['FD_common_noQED'] = neff_run(plasma0, cE, common=True)
    runs['FD_common_NLO'] = neff_run(plasma, cE, common=True)
    runs['FD_common_LO'] = neff_run(plasma2, cE, common=True)
    runs['FD_separate_NLO'] = neff_run(plasma, cE, common=False)
    runs['FD_separate_NLO_UM2_tree_couplings'] = neff_run(plasma, cU, common=False)
    runs['FD_common_NLO_UM2_tree_couplings'] = neff_run(plasma, cU, common=True)
    out['N_eff_runs'] = {k: (v if isinstance(v, float) else {kk: vv for kk, vv in v.items() if kk != 'history'}) for k, v in runs.items()}
    out['N_eff_history_separate'] = runs['FD_separate_NLO']['history']
    ne = {k: (v if isinstance(v, float) else v['N_eff']) for k, v in runs.items()}
    rep.check('N_eff_method_validation', abs(ne['instantaneous_noQED'] - 3.0) < 2e-4 and abs(ne['instantaneous_LO'] - 3.011) < 1.5e-3
              and abs(ne['instantaneous_NLO'] - 3.010) < 1.5e-3 and abs(ne['FD_common_noQED'] - 3.039) < 1.5e-3
              and abs(ne['FD_common_NLO'] - 3.049) < 1.5e-3 and abs(runs['FD_separate_NLO']['N_eff'] - 3.048) < 1.5e-3,
              'the same method as Escudero (arXiv:2001.04466; Table 1 there, read 2026-10-18: instantaneous 3.000, + LO QED 3.011, + NLO QED '
              '3.010, FD collision terms 3.039, + NLO QED 3.049, the same with separate nu_e and nu_mu,tau temperatures 3.048) reproduces: '
              'instantaneous decoupling %.4f, + O(e^2) QED %.4f, + O(e^3) %.4f; FD energy transfer with one neutrino temperature %.4f, '
              '+ O(e^2) %.4f, + O(e^3) %.4f; with separate temperatures and O(e^3) %.4f' % (
                  ne['instantaneous_noQED'], ne['instantaneous_LO'], ne['instantaneous_NLO'], ne['FD_common_noQED'], ne['FD_common_LO'],
                  ne['FD_common_NLO'], runs['FD_separate_NLO']['N_eff']))
    # adopted value: the precision Standard-Model computation applies to UM-2 (same plasma at MeV temperatures, three flavours)
    neff_um2 = runs['FD_separate_NLO']['N_eff']
    out['N_eff_UM2_computed'] = {'separate_temperatures': neff_um2, 'common_temperature': runs['FD_common_NLO']['N_eff'],
                                 'separate_UM2_tree_couplings': runs['FD_separate_NLO_UM2_tree_couplings']['N_eff'],
                                 'common_UM2_tree_couplings': runs['FD_common_NLO_UM2_tree_couplings']['N_eff']}
    out['N_eff_adopted'] = {'value': NEFF_SM[0], 'uncertainty': NEFF_SM[1], 'source': NEFF_SM[2]}
    spread = abs(runs['FD_separate_NLO']['N_eff'] - runs['FD_common_NLO']['N_eff'])
    rep.check('N_eff_three_flavours', abs(neff_um2 - NEFF_SM[0]) < 0.01 and spread < 0.01,
              'UM-2 (three flavours, its tree-level couplings %.4f, or the effective %.4f; no extra radiation: both dirac16complex fold bands '
              'are never thermalised): N_eff = %.4f with separate nu_e and nu_mu,tau temperatures (no oscillations), %.4f with one common '
              'temperature (efficient oscillations); T_nu_e/T_gamma = %.5f, T_nu_mu/T_gamma = %.5f (comoving heating by e+ e- annihilation +%.3f %% '
              'and +%.3f %%); the precision value with oscillations '
              'and the electron mass in the rates, %.4f (%s), is adopted for the cosmology' % (
                  runs['FD_separate_NLO_UM2_tree_couplings']['N_eff'], neff_um2, neff_um2, runs['FD_common_NLO']['N_eff'],
                  runs['FD_separate_NLO']['Tnu_e_over_Tgamma'], runs['FD_separate_NLO']['Tnu_mu_over_Tgamma'],
                  100 * runs['FD_separate_NLO']['heating_Te_a'], 100 * runs['FD_separate_NLO']['heating_Tm_a'], NEFF_SM[0],
                  NEFF_SM[2].split(';')[0]))

    # ---------------- N5 the cosmic neutrino background ----------------
    T0 = val('T_CMB_K')
    kB = val('k_B_eV_per_K')
    Tnu_K = (4.0 / 11.0) ** (1.0 / 3.0) * T0
    Tnu = kB * Tnu_K                                        # eV
    zeta3 = 1.2020569031595942
    n_per_state = 0.75 * zeta3 / math.pi ** 2 * 2 * Tnu ** 3          # nu + nubar of one mass eigenstate (eV^3)
    n_cm3 = n_per_state / HBARC_EV_CM ** 3
    cnb = []
    rho_tot = 0.0
    for i in range(3):
        rho_i = 2 * quad(lambda p: p * p * math.sqrt(p * p + m[i] ** 2) / (math.exp(p / Tnu) + 1), 0, 60 * Tnu)[0] / (2 * math.pi ** 2)
        vmean = quad(lambda p: p * p * (p / math.sqrt(p * p + m[i] ** 2)) / (math.exp(p / Tnu) + 1), 0, 60 * Tnu)[0] / \
            quad(lambda p: p * p / (math.exp(p / Tnu) + 1), 0, 60 * Tnu)[0]
        rho_tot += rho_i
        cnb.append({'mass_eV': float(m[i]), 'n_cm3': n_cm3, 'mean_velocity_over_c': vmean, 'rho_eV4': rho_i,
                    'flavour_content': {'e': float(abs(U[0, i]) ** 2), 'mu': float(abs(U[1, i]) ** 2), 'tau': float(abs(U[2, i]) ** 2)}})
    rho_crit_h2 = 1.87834e-29 * 5.60959e32 * HBARC_EV_CM ** 3 / 1e0      # g/cm^3 -> eV/cm^3 -> eV^4: rho_c/h^2
    # 1.87834e-29 g/cm^3 * (5.60959e32 eV per g) = 1.05368e4 eV/cm^3
    rho_c_eV4 = 1.87834e-29 * 5.60959e32 * HBARC_EV_CM ** 3
    omega_h2 = rho_tot / rho_c_eV4
    out['CNB'] = {'T_nu_K': Tnu_K, 'T_nu_eV': Tnu, 'n_per_mass_state_cm3': n_cm3, 'n_total_cm3': 3 * n_cm3, 'states': cnb,
                  'Omega_nu_h2': omega_h2, 'Omega_nu_h2_from_sum_over_93p14': float(m.sum()) / 93.14,
                  'note': 'an incoherent mixture of the three mass eigenstates (decoherence after decoupling); temperature of instantaneous '
                          'decoupling (the non-instantaneous heating raises the energy density by N_eff/3 - 1 = 1.4 %)'}
    rep.check('CNB_three_mass_states', abs(n_cm3 - 112.0) < 0.5 and abs(omega_h2 / (m.sum() / 93.14) - 1) < 0.03,
              'the CNB of UM-2 is three neutrino MASS eigenstates (decoherent), T_nu = %.4f K, %.1f per cm^3 each (nu + nubar), %.0f per cm^3 in '
              'all; mean velocities %s c today; flavour content of the states e: %s; Omega_nu h^2 = %.3e (sum m/93.14 eV = %.3e); '
              'the dirac16complex fold bands are not part of it' % (
                  Tnu_K, n_cm3, 3 * n_cm3, ', '.join('%.3g' % s['mean_velocity_over_c'] for s in cnb),
                  ', '.join('%.3f' % s['flavour_content']['e'] for s in cnb), omega_h2, m.sum() / 93.14))

    # ---------------- N6 supernovae ----------------
    # (a) MSW resonances in the envelope rho(r) = rho9 (1e9 cm/r)^3, Y_e = 0.5 (ASSUMED profile)
    rho9 = 1e4
    sn = {}
    lz = []
    for EMeV in (10.0, 20.0, 40.0):
        E = EMeV * 1e6
        res = {}
        for lab, dm2, s2t in [('H (1-3)', nu['dm2_31_eV2'], nu['sin2_theta13']), ('L (1-2)', nu['dm2_21_eV2'], nu['sin2_theta12'])]:
            c2 = 1 - 2 * s2t
            sin2_2t = 4 * s2t * (1 - s2t)
            ne_res = dm2 * c2 / (2 * E * SQ2GF_CM3)                  # cm^-3
            rho_res = ne_res / (0.5 * NA)
            r_res = 1e9 * (rho9 / rho_res) ** (1.0 / 3.0)              # cm
            dlnne = 3.0 / r_res                                        # cm^-1
            gamma = dm2 * sin2_2t / (2 * E * c2 * dlnne * HBARC_EV_CM)
            PLZ = math.exp(-math.pi * gamma / 2)
            res[lab] = {'rho_res_g_cm3': rho_res, 'r_res_cm': r_res, 'adiabaticity_gamma': gamma, 'P_LZ': PLZ}
        sn[str(EMeV)] = res
        lz.append(res['H (1-3)']['P_LZ'])
    pee = float(abs(U[0, 2]) ** 2)
    pbar = float(abs(U[0, 0]) ** 2)
    out['supernova_MSW'] = {'profile': 'rho = 1e4 g/cm^3 (1e9 cm/r)^3, Y_e = 0.5 (ASSUMED)', 'resonances': sn,
                            'P_ee_normal_ordering': pee, 'Pbar_ee_normal_ordering': pbar}
    rep.check('supernova_MSW', all(p < 1e-6 for p in lz) and abs(pee - nu['sin2_theta13']) < 1e-15,
              'in the stellar envelope the H (1-3) resonance lies at rho = %.0f g/cm^3 for 20 MeV (r = %.2e km) with adiabaticity gamma = %.0f '
              '(Landau-Zener crossing probability %.1e): adiabatic; for normal ordering a nu_e from the core leaves the star as nu_3, '
              'P(nu_e -> nu_e) = |U_e3|^2 = %.4f, and an antineutrino as nubar_1, Pbar(nu_e -> nu_e) = |U_e1|^2 = %.4f (without collective '
              'effects and Earth matter)' % (sn['20.0']['H (1-3)']['rho_res_g_cm3'], sn['20.0']['H (1-3)']['r_res_cm'] / 1e5,
                                            sn['20.0']['H (1-3)']['adiabaticity_gamma'], sn['20.0']['H (1-3)']['P_LZ'], pee, pbar))
    # observed mean energies with pinched spectra (alpha = 3) of representative accretion-phase neutrinospheres
    spectra = {'nu_e': (6e52, 11.0), 'nubar_e': (6e52, 14.0), 'nu_x': (4e52, 15.5)}     # (luminosity erg/s, mean energy MeV) ASSUMED

    def number_rate(Lum, Em):
        return Lum / Em
    Nn = {k: number_rate(*v) for k, v in spectra.items()}
    obs_e_mean = (pee * Nn['nu_e'] * spectra['nu_e'][1] + (1 - pee) * Nn['nu_x'] * spectra['nu_x'][1]) / (pee * Nn['nu_e'] + (1 - pee) * Nn['nu_x'])
    obs_eb_mean = (pbar * Nn['nubar_e'] * spectra['nubar_e'][1] + (1 - pbar) * Nn['nu_x'] * spectra['nu_x'][1]) / (pbar * Nn['nubar_e'] + (1 - pbar) * Nn['nu_x'])
    out['supernova_observed_mean_energy_MeV'] = {'nu_e': obs_e_mean, 'nubar_e': obs_eb_mean, 'source_spectra': spectra}
    # (b) the fast flavour instability.  ELN angular distribution G(u) = sqrt2 G_F [n_nue g_e(u) - n_nuebar g_ebar(u)] (u = cos theta,
    # int du/2 g = 1), in units of mu = sqrt2 G_F n_nue: G/mu = g_e - alpha g_ebar, alpha = n_nuebar/n_nue.  The physical mode
    # (Omega, K) has omega = Omega - Lambda0, k = K - Lambda, Lambda^mu = int du/2 G v^mu: the homogeneous mode K = 0 is at k = -Lambda3.
    def gauss_shape(sig):
        uq, wq = np.polynomial.legendre.leggauss(400)
        nrm = float(np.sum(wq * np.exp(-(1 - uq) ** 2 / (2 * sig * sig))) / 2)
        return lambda u: np.exp(-(1 - u) ** 2 / (2 * sig * sig)) / nrm
    ge6, gb4 = gauss_shape(0.6), gauss_shape(0.4)
    cases = {'crossing: nu_e broad (sigma 0.6), nubar_e forward (sigma 0.4), alpha 0.8': lambda u: ge6(u) - 0.8 * gb4(u),
             'crossing: linear g_e = 1 + 0.2u, g_ebar = 1 + 0.6u, alpha 0.9': lambda u: (1 + 0.2 * u) - 0.9 * (1 + 0.6 * u),
             'no crossing: nu_e sigma 0.6, nubar_e sigma 0.4, alpha 0.3': lambda u: ge6(u) - 0.3 * gb4(u)}
    ffi = {}
    for name, G in cases.items():
        grK, D, moms = homogeneous_growth(G)                     # analytic: the mode K = Lambda (k = 0)
        grm, _ = homogeneous_growth_matrix(G, n=300)              # the homogeneous mode K = 0 (discretised equations)
        uu = np.linspace(-1, 1, 4001)
        gu = G(uu)
        cross = bool(gu.min() < -1e-12 and gu.max() > 1e-12)     # a strict sign change of the ELN distribution
        gs = max(abs(moms[0]), abs(moms[1]), 0.05)
        b0, _ = max_growth_over_k(G, np.array([0.0]), guess_scale=gs, branch=dispersion_axisym)
        bh, _ = max_growth_over_k(G, np.array([-moms[1]]), guess_scale=gs, branch=dispersion_axisym)
        ks = np.linspace(-1.2, 1.2, 25)
        best, rows = max_growth_over_k(G, ks, guess_scale=gs, branch=dispersion_axisym)
        best2, rows2 = max_growth_over_k(G, ks, guess_scale=gs, branch=dispersion_nonaxisym)
        ffi[name] = {'crossing': cross, 'moments_I0_I1_I2': moms, 'Lambda3': moms[1],
                     'growth_K_eq_Lambda_analytic': grK, 'growth_K_eq_Lambda_dispersion': b0[0],
                     'growth_homogeneous_matrix': grm, 'growth_homogeneous_dispersion': bh[0],
                     'max_growth_any_k': max(best[0], best2[0]), 'k_at_max': best[1] if best[0] >= best2[0] else best2[1],
                     'branch_at_max': 'axisymmetric' if best[0] >= best2[0] else 'azimuthal',
                     'max_growth_axisymmetric': best[0], 'max_growth_azimuthal': best2[0], 'growth_vs_k': rows,
                     'growth_vs_k_azimuthal': rows2}
    out['fast_flavour_instability'] = ffi
    c1, c2_, c3 = list(ffi.values())
    cons = max(max(abs(c['growth_K_eq_Lambda_analytic'] - c['growth_K_eq_Lambda_dispersion']),
                   abs(c['growth_homogeneous_matrix'] - c['growth_homogeneous_dispersion'])) for c in ffi.values())
    rep.check('fast_flavour_solver_consistency', cons < 1e-6,
              'three independent evaluations agree to %.1e (units mu = sqrt2 G_F n_nue): the analytic growth sqrt(4 I1^2 - (I0 + I2)^2)/2 of the '
              'mode K = Lambda (I_n = int du/2 G u^n) and the root of the dispersion relation at k = 0; the eigenvalues of the discretised '
              'homogeneous linear equations i dS_u/dx4 = (Lambda^0 - u Lambda^3) S_u - int du\'/2 G(u\')(1 - u u\') S_u\' and the root at k = -Lambda^3 '
              '(homogeneous growth %.5f, %.5f, %.5f for the three cases)' % (cons, c1['growth_homogeneous_matrix'],
                                                                             c2_['growth_homogeneous_matrix'], c3['growth_homogeneous_matrix']))
    rep.check('fast_flavour_crossing_criterion', c1['crossing'] and c2_['crossing'] and not c3['crossing'] and c1['max_growth_any_k'] > 1e-3
              and c2_['max_growth_any_k'] > 1e-3 and c2_['growth_homogeneous_matrix'] < 1e-9 and c3['max_growth_any_k'] < 1e-9,
              'the dispersion relation det Pi = 0, Pi^{mu nu} = eta^{mu nu} + int du/2 G v^mu v^nu/(omega - k u), both branches (axisymmetric '
              'and azimuthal) for real k along the axis: with an ELN crossing the gas is unstable (forward-peaked antineutrinos: largest growth '
              '%.4f mu at k = %.2f, homogeneous %.4f mu; linear distributions: %.4f mu at k = %.2f although the homogeneous mode is stable); '
              'without a crossing no mode grows (%.1e): flavour conversion needs a crossing, as the general theorem (Morinaga 2022) states' % (
                  c1['max_growth_any_k'], c1['k_at_max'], c1['growth_homogeneous_matrix'], c2_['max_growth_any_k'], c2_['k_at_max'],
                  c3['max_growth_any_k']))
    # physical scales near the neutrinosphere: n_nu_e ~ 1e32 - 1e33 cm^-3 -> mu = sqrt2 G_F n
    scales = {}
    for n in (1e32, 1e33):
        mu = SQ2GF_CM3 * n
        rate = c1['max_growth_any_k'] * mu / (6.582119569e-16)      # s^-1 (hbar = 6.58e-16 eV s)
        scales['%.0e' % n] = {'mu_eV': mu, 'growth_rate_per_s': rate, 'e_fold_time_s': 1 / rate,
                              'e_fold_length_cm': 2.99792458e10 / rate}
    out['fast_flavour_scales'] = scales
    rep.check('fast_flavour_time_scale', all(v['e_fold_time_s'] < 1e-6 for v in scales.values()),
              'near the neutrinosphere (n_nu_e = 1e32 to 1e33 cm^-3, mu = sqrt2 G_F n = %.1e to %.1e eV) the instability grows by e in %.1e to '
              '%.1e s over %.1f to %.2f cm: a million times faster than the hydrodynamics (milliseconds), which is why the explosion models treat '
              'the conversion as instantaneous' % (scales['1e+32']['mu_eV'], scales['1e+33']['mu_eV'], scales['1e+32']['e_fold_time_s'],
                                                   scales['1e+33']['e_fold_time_s'], scales['1e+32']['e_fold_length_cm'],
                                                   scales['1e+33']['e_fold_length_cm']))
    # (c) the effect of flavour equipartition on the charged-current heating (schematic)
    E2fac = 5.0 / 4.0          # <E^2> = (alpha + 2)/(alpha + 1) <E>^2 for alpha = 3
    heat = lambda N, Em: N * E2fac * Em ** 2
    Ne, Nb, Nx = Nn['nu_e'], Nn['nubar_e'], Nn['nu_x']
    Ee, Eb, Ex = spectra['nu_e'][1], spectra['nubar_e'][1], spectra['nu_x'][1]
    q0 = heat(Ne, Ee) + heat(Nb, Eb)
    # full three-flavour equipartition per species (number conserving): N_e' = (N_e + 2 N_x)/3 with <E^2> mixed accordingly
    q_full = (heat(Ne, Ee) + 2 * heat(Nx, Ex)) / 3 + (heat(Nb, Eb) + 2 * heat(Nx, Ex)) / 3
    # pair conversion nu_e nubar_e -> nu_x nubar_x conserving the ELN until the less abundant electron species is equipartitioned
    Delta = (2.0 / 3.0) * (Nb - Nx)
    fe = (Ne - Delta) / Ne
    fb = (Nb - Delta) / Nb
    q_pair = fe * heat(Ne, Ee) + fb * heat(Nb, Eb) + (Delta / Nx) * 0.5 * 0          # the gained nu_x do not heat (no CC)
    q_pair = fe * heat(Ne, Ee) + fb * heat(Nb, Eb)
    out['equipartition_heating_ratio'] = {'full_equipartition': q_full / q0, 'ELN_conserving_pair_conversion': q_pair / q0,
                                          'inputs': spectra, 'note': 'schematic: spectral shapes kept, alpha = 3 pinching, heating ~ N <E^2>'}
    rep.check('equipartition_reduces_heating', q_full / q0 < 1 and q_pair / q0 < 1,
              'schematic charged-current heating behind the shock, proportional to N <E^2> of nu_e and nubar_e, for representative '
              'accretion-phase neutrinospheres (L = 6, 6, 4 x 1e52 erg/s; <E> = 11, 14, 15.5 MeV): flavour equipartition changes it by the factor '
              '%.3f (full three-flavour equipartition) or %.3f (ELN-conserving pair conversion until nubar_e is equipartitioned): the heavy-lepton '
              'neutrinos have higher energies but fewer particles and no charged-current absorption, so the heating falls; Gogilashvili and '
              'Tamborra (2026) find in 195 collapse simulations that this raises the fraction of failed explosions from 25.6 %% to 50.8 - 96.4 %%' % (
                  q_full / q0, q_pair / q0))
    # figures
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(1, 3, figsize=(14, 4))
    Es = np.logspace(-1, 1.3, 80)
    axs[0].semilogx(Es, [pee_adiabatic(E * 1e6, 0.05) for E in Es], 'C0-', label='adiabatic, production at 0.05 R_sun')
    axs[0].semilogx(Es, [pee_adiabatic(E * 1e6, 0.1) for E in Es], 'C1--', label='adiabatic, production at 0.1 R_sun')
    axs[0].semilogx([s['E_MeV'] for s in solar], [s['P_ee_numeric_40000'] for s in solar], 'ko', ms=4, label='numerical (layers)')
    axs[0].set_xlabel('E [MeV]')
    axs[0].set_ylabel('P(nu_e -> nu_e) at the Earth')
    axs[0].set_title('solar neutrinos: MSW conversion')
    axs[0].legend(fontsize=7)
    EE = np.linspace(0.5, 5.0, 200)
    for (rho, st, lab) in [(2.848, '-', 'nu'), (2.848, '--', 'antinu')]:
        P = []
        for E in EE:
            if lab == 'nu':
                P.append(prob_matrix(evolve_const(hamiltonian(U, m2, E * 1e9, V_of_rho(rho)), 1300 * KM_TO_INV_EV))[0, 1])
            else:
                P.append(prob_matrix(evolve_const(hamiltonian(U.conj(), m2, E * 1e9, -V_of_rho(rho)), 1300 * KM_TO_INV_EV))[0, 1])
        axs[1].plot(EE, P, 'C2' + st, label='P(%s_mu -> %s_e)' % (lab, lab))
    axs[1].set_xlabel('E [GeV]')
    axs[1].set_ylabel('appearance probability, 1300 km')
    axs[1].set_title('DUNE baseline, normal ordering, delta = 212 deg')
    axs[1].legend(fontsize=7)
    short = ['crossing, forward-peaked antineutrinos', 'crossing, linear distributions', 'no crossing']
    for (name, v), lab in zip(ffi.items(), short):
        kk = [r[0] for r in v['growth_vs_k']]
        gg = [r[1] for r in v['growth_vs_k']]
        axs[2].plot(kk, gg, label=lab)
    axs[2].set_xlabel('wave number k [mu]')
    axs[2].set_ylabel('growth rate Im omega [mu]')
    axs[2].set_title('fast flavour instability (axisymmetric modes)')
    axs[2].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, 'fig_neutrino_conversion.png'), dpi=130)
    plt.close(fig)
    h = runs['FD_separate_NLO']['history']
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))
    ax = axs[0]
    ax.semilogx(h['Tgamma'], h['Te_over_Tg'], 'C0-', label='T(nu_e)/T(gamma)')
    ax.semilogx(h['Tgamma'], h['Tm_over_Tg'], 'C1--', label='T(nu_mu,tau)/T(gamma)')
    ax.axhline((4 / 11) ** (1 / 3), color='k', lw=0.6, ls=':', label='(4/11)^(1/3)')
    ax.invert_xaxis()
    ax.set_xlabel('T(gamma) [MeV]')
    ax.set_ylabel('temperature ratio')
    ax.set_title('neutrino decoupling in UM-2 (three flavours)')
    ax.legend(fontsize=8)
    ax = axs[1]
    ax.semilogx(h['Tgamma'], 100 * np.array(h['Te_a_rel']), 'C0-', label='nu_e')
    ax.semilogx(h['Tgamma'], 100 * np.array(h['Tm_a_rel']), 'C1--', label='nu_mu, nu_tau')
    ax.invert_xaxis()
    ax.set_xlabel('T(gamma) [MeV]')
    ax.set_ylabel('T_nu a / (T_nu a)_start - 1  [%]')
    ax.set_title('heating of the neutrinos by e+ e- annihilation')
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, 'fig_neutrino_decoupling.png'), dpi=130)
    plt.close(fig)
    write_json(os.path.join(OUT, 'neutrino.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
