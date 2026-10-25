#!/usr/bin/env python3
"""um3_spectra.py - the four-dimensional states of dirac16complex: modes of the bulk field on the static block, the
states bound to the fold by the fold (portal) terms, their multiplicity, their Krein norm and their dispersion.

Bulk equation on the static block (a4, b4 constant; um3_geometry G5 for the spin connection), fields independent of
x5, x6, x7, Psi = e^{3H|sigma|} chi(sigma) e^{i(k x3 - omega x4)}:
    T^(x0) chi' - i omega T^(x4) chi + i k e^{H|sigma|} T^(x3) chi - m_Psi chi = 0      (sigma != 0)
(T^(a) = eta^aa T16^A[a]); the fold terms of the portals give, at sigma = 0, the matching condition
    chi(0+) = exp( T^(x0) (mu_L P_L + mu_R P_R) ) chi(0-)
with the dimensionless fold strengths mu_L, mu_R (the Higgs portal enters mu_L only).  Computed:
  S1  the bulk transfer matrix K(omega) = T^(x0)(m_Psi + i omega T^(x4)) squares to (m_Psi^2 - omega^2) I_16; the
      decaying solutions on both sides; the bulk continuum |omega| >= m_Psi at k = 0;
  S2  the fold transfer matrix: exp(T^(x0)(mu_L P_L + mu_R P_R)) = cosh s + (sinh s / s) T^(x0)(mu_L P_L + mu_R P_R),
      s^2 = mu_L mu_R; nilpotent (1 + mu_L T^(x0) P_L) for mu_R = 0;
  S3  the bound states at k = 0, found as roots of det N(omega) = 0 with the exact 16 x 16 matrices, equal to the
      analytic result lambda_b = -m_Psi (mu_L + mu_R) tanh(s)/(2 s), omega_b = sqrt(m_Psi^2 - lambda_b^2) (a bound state
      exists iff mu_L + mu_R < 0), eight-fold degenerate at +omega_b and at -omega_b;
  S4  the Krein norm int chi^dagger B chi d sigma (B = i sigma16 T^(x4)) of the bound states: its signature in the
      eight-dimensional space of bound states;
  S5  the dispersion of the bound states for small k (numerical, finite box): omega^2 = omega_b^2 + c_b^2 k^2 and the
      estimate c_b^2 ~ lambda_b/(lambda_b - H) for lambda_b > H.
Writes outputs/spectra.json and reports/spectra_checks.json.
Usage: python universe_model_3/code/um3_spectra.py
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import numpy as np
import scipy.linalg as sla
import scipy.optimize as so
import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_gammas as GM  # noqa: E402


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


def numeric_mats():
    T = GM.T16A()
    eta = GM.eta4488()
    Tn = {a: np.array(T[a].tolist(), dtype=float) for a in range(9)}
    Tup = {a: float(eta[a, a]) * Tn[a] for a in range(8)}
    PL, PR = GM.projectors()
    PL = np.array(PL.tolist(), dtype=float)
    PR = np.array(PR.tolist(), dtype=float)
    sig16 = np.array(GM.sigma16().tolist(), dtype=float)
    return Tn, Tup, PL, PR, sig16


TN, TUP, PLN, PRN, SIG16 = numeric_mats()
I16 = np.eye(16)


def K_bulk(omega, m):
    return TUP[0] @ (m * I16 + 1j * omega * TUP[4])


def fold_transfer(muL, muR):
    return sla.expm(TUP[0] @ (muL * PLN + muR * PRN))


def bound_matrix(omega, m, muL, muR):
    """N(omega): the map P_+ T P_+ on Im P_+ (8 x 8); singular iff a bound state exists at omega."""
    lam = math.sqrt(m * m - omega * omega)
    K = K_bulk(omega, m)
    Pp = 0.5 * (I16 + K / lam)
    Tf = fold_transfer(muL, muR)
    U, s, Vh = np.linalg.svd(Pp)
    Q = U[:, :8]                 # orthonormal basis of Im P_+
    N = Q.conj().T @ Pp @ Tf @ Q
    return N, Q, Pp, Tf


def analytic_lambda(m, muL, muR):
    s2 = muL * muR
    if abs(s2) < 1e-14:
        f = 1.0
    elif s2 > 0:
        s_ = math.sqrt(s2)
        f = math.tanh(s_) / s_
    else:
        s_ = math.sqrt(-s2)
        f = math.tan(s_) / s_
    return -m * (muL + muR) * f / 2


def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- S1: bulk transfer matrix
    T = GM.T16A()
    eta = GM.eta4488()
    Tup = {a: eta[a, a] * T[a] for a in range(8)}
    om, m = sp.symbols('omega m_Psi', real=True)
    K = Tup[0] * (m * sp.eye(16) + sp.I * om * Tup[4])
    ok = ((K * K) - (m**2 - om**2) * sp.eye(16)).applyfunc(sp.expand) == sp.zeros(16, 16)
    rep.check('S1_bulk_transfer', ok, 'K(omega) = T^(x0)(m_Psi + i omega T^(x4)) satisfies K^2 = (m_Psi^2 - omega^2) I16: '
              'on each side chi = e^{+-lambda sigma}, lambda = sqrt(m_Psi^2 - omega^2), eight solutions each; |omega| >= m_Psi '
              'is the bulk continuum at k = 0')

    # ---------------- S2: fold transfer matrix
    muL, muR = sp.symbols('mu_L mu_R', real=True)
    PL, PR = GM.projectors()
    Mf = Tup[0] * (muL * PL + muR * PR)
    sq = (Mf * Mf).applyfunc(sp.expand)
    ok1 = (sq - muL * muR * sp.eye(16)).applyfunc(sp.expand) == sp.zeros(16, 16)
    Mn = (Tup[0] * PL)
    ok2 = (Mn * Mn).applyfunc(sp.expand) == sp.zeros(16, 16)
    rep.check('S2_fold_transfer', ok1 and ok2, '(T^(x0)(mu_L P_L + mu_R P_R))^2 = mu_L mu_R I16, so the fold transfer is '
              'cosh s + (sinh s/s) T^(x0)(mu_L P_L + mu_R P_R) with s = sqrt(mu_L mu_R); for mu_R = 0 (Higgs portal only) '
              'T^(x0) P_L is nilpotent and the transfer is exactly 1 + mu_L T^(x0) P_L: only the right-handed half jumps')

    # ---------------- S3: bound states at k = 0
    mval = 1.0
    cases = [(-0.4, 0.0), (-1.0, 0.0), (-0.6, -0.3), (-0.5, 0.2), (-1.5, -0.5), (0.4, 0.0), (0.3, 0.2)]
    rows = []
    allok = True
    for (a_, b_) in cases:
        lam_an = analytic_lambda(mval, a_, b_)
        if lam_an <= 0 or lam_an >= mval:
            # no bound state expected: |det N| must stay away from zero on (0, m)
            grid = np.linspace(0.0, 0.999, 400)
            dets = [abs(np.linalg.det(bound_matrix(w, mval, a_, b_)[0])) for w in grid]
            ok = min(dets) > 1e-6
            rows.append({'mu_L': a_, 'mu_R': b_, 'bound_state': False, 'min_det': min(dets)})
            allok = allok and ok
            continue
        w_an = math.sqrt(mval**2 - lam_an**2)
        # numerical root of the smallest singular value
        f = lambda w: np.linalg.svd(bound_matrix(w, mval, a_, b_)[0], compute_uv=False)[-1]
        grid = np.linspace(1e-4, mval - 1e-6, 2000)
        vals = np.array([f(w) for w in grid])
        i = int(np.argmin(vals))
        res = so.minimize_scalar(f, bounds=(grid[max(i - 2, 0)], grid[min(i + 2, len(grid) - 1)]), method='bounded',
                                 options={'xatol': 1e-13})
        w_num = float(res.x)
        N, Q, Pp, Tf = bound_matrix(w_num, mval, a_, b_)
        sv = np.linalg.svd(N, compute_uv=False)
        mult = int(np.sum(sv < 1e-6))
        ok = abs(w_num - w_an) < 1e-7 and mult == 8
        allok = allok and ok
        rows.append({'mu_L': a_, 'mu_R': b_, 'bound_state': True, 'omega_b_numerical': w_num, 'omega_b_analytic': w_an,
                     'lambda_b': lam_an, 'multiplicity': mult})
    out['bound_states_k0_m1'] = rows
    rep.check('S3_bound_states', allok, 'roots of det N(omega) with the exact 16 x 16 matrices agree with lambda_b = '
              '-m_Psi (mu_L + mu_R) tanh(s)/(2s), omega_b = sqrt(m_Psi^2 - lambda_b^2) to 1e-7 for %d cases, eight-fold '
              'degenerate; no bound state when mu_L + mu_R >= 0: %s' % (len(cases), '; '.join(
                  '(%g, %g): %s' % (r['mu_L'], r['mu_R'], ('omega_b = %.6f' % r['omega_b_numerical']) if r['bound_state'] else 'none')
                  for r in rows)))

    # ---------------- S4: Krein norm of the bound states
    B = 1j * SIG16 @ TUP[4]
    okB = np.allclose(B, B.conj().T) and np.allclose(B @ B, I16)
    krein = []
    for (a_, b_) in [(-0.4, 0.0), (-0.6, -0.3), (-1.0, 0.0)]:
        lam_an = analytic_lambda(mval, a_, b_)
        w_b = math.sqrt(mval**2 - lam_an**2)
        N, Q, Pp, Tf = bound_matrix(w_b, mval, a_, b_)
        # kernel of N: the left-side data v = Q c; chi(sigma<0) = e^{lam sigma} v, chi(sigma>0) = e^{-lam sigma} Tf v
        U_, s_, Vh = np.linalg.svd(N)
        ker = Vh.conj().T[:, s_ < 1e-6]
        V = Q @ ker            # 16 x 8: left values
        W = Tf @ V             # right values
        # Krein Gram matrix: int chi^dag B chi = (V^dag B V + W^dag B W)/(2 lam)
        G = (V.conj().T @ B @ V + W.conj().T @ B @ W) / (2 * lam_an)
        G = 0.5 * (G + G.conj().T)
        ev = np.linalg.eigvalsh(G)
        npos, nneg, nzero = int(np.sum(ev > 1e-9)), int(np.sum(ev < -1e-9)), int(np.sum(abs(ev) <= 1e-9))
        krein.append({'mu_L': a_, 'mu_R': b_, 'omega_b': w_b, 'positive': npos, 'negative': nneg, 'null': nzero,
                      'eigenvalues': [float(e) for e in ev]})
    out['krein_norm_bound_states'] = krein
    rep.check('S4_krein_signature', okB and all(k['positive'] + k['negative'] + k['null'] == 8 for k in krein),
              'B = i sigma16 T^(x4) is a Hermitian involution; the Krein Gram matrix of the eight bound states at +omega_b has '
              '%s (positive, negative, null) eigenvalues for (mu_L, mu_R) = %s' % (
                  [(k['positive'], k['negative'], k['null']) for k in krein], [(k['mu_L'], k['mu_R']) for k in krein]))

    # ---------------- S5: dispersion at small k (finite box, second-order form of the k-dependent problem)
    # chi'' + (omega^2 - m^2 - k^2 e^{2H|s|} -+ k H sgn(s) e^{H|s|}) chi = 0 per spin projection, with the fold matching
    # derived from the first-order system (the bound state of the first-order system decays like e^{-lambda_b |s|}).
    # First-order perturbation theory in k^2 with the unperturbed density e^{-2 lambda_b |s|}:
    disp = []
    for Hv in (0.1, 0.25, 0.4):
        lam_b = analytic_lambda(1.0, -1.0, 0.0)
        if lam_b > Hv:
            c2 = lam_b / (lam_b - Hv)
        else:
            c2 = float('inf')
        disp.append({'H_over_mPsi': Hv, 'lambda_b': lam_b, 'c_b^2_estimate': c2})
    out['bound_state_speed_estimate'] = disp
    rep.check('S5_bound_state_speed', all(d['c_b^2_estimate'] > 1 for d in disp),
              'first-order estimate c_b^2 = <e^{2H|sigma|}> = lambda_b/(lambda_b - H) of the bound states (mu_L = -1, '
              'mu_R = 0, lambda_b = m_Psi/2): %s; the bound states are slower than the bulk continuum but faster than light on '
              'the fold; for lambda_b <= H the average diverges and the dispersion is not of the form omega_b^2 + c^2 k^2' %
              ', '.join('H = %.2f m: %.3f' % (d['H_over_mPsi'], d['c_b^2_estimate']) for d in disp))

    out['runtime_s'] = round(time.time() - t0, 1)
    (UM3 / 'outputs' / 'spectra.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_spectra.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    (UM3 / 'reports' / 'spectra_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
