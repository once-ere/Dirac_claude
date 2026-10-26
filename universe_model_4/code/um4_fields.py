#!/usr/bin/env python3
"""um4_fields.py - exact algebra of the matter sector of UM-4 (with the author's Dirac matrices of 4+4.nb).

F1  Dirac adjoint and hermiticity: a bilinear Psibar M Psi = Psi^dagger (sigma16 M) Psi is real for every Psi iff
    sigma16 M is Hermitian.  Classified: the scalar densities Psibar P_X Psi, the tensor densities i Psibar S^{ab} P_X Psi,
    the vector current i Psibar gamma^a Psi, the chiral current Psibar gamma^a Gamma Psi, the convective chiral currents.
F2  Chirality content: even bilinears (0, 2, 4, ... gamma matrices between Psibar and Psi) keep the chirality (they are
    sums of P_L-P_L and P_R-P_R terms), odd ones exchange it; hence a left-handed coupling of dirac16complex must use an
    even bilinear of P_L Psi, or a convective current, never a single gamma.
F3  The Krein operator B = i sigma16 gamma^(x4): Hermitian involution, commutes with gamma^(x0), gamma^(x1..x3),
    gamma^(x4) and the mass term, anticommutes with Gamma: a chirality-dependent mass mixes the two halves B = +-1.
F4  Four-dimensional chirality Gamma_4 = i T1 T2 T3 T4 and the internal one; Gamma = (sign) Gamma_4 Gamma_int.
F5  Electroweak vacuum with the author's ad hoc upper component: the mass matrix of (W1, W2, W3, B) for
    Phi = (A, v)/sqrt2 (A real): one massless photon, m_W^2 = g^2 (v^2 + A^2)/4 twice, m_Z^2 = (g^2 + g'^2)(v^2 + A^2)/4;
    the photon is a rotated combination; the isospin current of a time-dependent A; the residual of the Higgs equation
    for A = v_A e^{-2 a40 x4}.
F6  Hypercharges, Yukawa invariance and anomaly cancellation of three generations with three right-handed neutrinos.
In UM-4 the gauge fields live in the bulk: g, g' (and g_3) here are the four-dimensional couplings of their zero modes,
g_4^2 = g_7^2/V_* = (3H/2) g_8^2/V_* (um4_bulk.py B2; g_8 the coupling of eight dimensions, V_* the volume of the extra times),
and the masses of F5 are those of the zero modes before their mixing with the massive modes of the bulk
(um4_propagators.py P4: m^2 = m_0^2 (1 - m_0^2/(3 H^2)) - i m_0^5/(3 H^3), a width into the bulk).
Writes outputs/fields.json and reports/fields_checks.json; exit code 0 iff every check passes.
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
UM4 = HERE.parent
sys.path.insert(0, str(HERE))
import um4_gammas as GM  # noqa: E402


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


def is_herm(M):
    return (M - M.H).applyfunc(sp.simplify) == sp.zeros(*M.shape)


def main():
    t0 = time.time()
    rep = Report()
    out = {}
    T = GM.T16A()
    eta = GM.eta4488()
    C = GM.sigma16()
    PL, PR = GM.projectors()
    Gam = T[8]
    S = GM.SAB()
    I16 = sp.eye(16)
    I = sp.I
    gup = {a: eta[a, a] * T[a] for a in range(8)}   # gamma^a (upper frame index)

    # ---------------- F1 hermiticity
    ok_s = is_herm(C * PL) and is_herm(C * PR)
    ok_t = all(is_herm(I * C * S[(a, b)] * P) for a in range(8) for b in range(8) if a < b for P in (PL, PR))
    ok_v = all(is_herm(I * C * gup[a]) for a in range(8))
    ok_a = all(is_herm(C * gup[a] * Gam) for a in range(8))
    ok_nl = all(not is_herm(C * gup[a] * PL) and not is_herm(I * C * gup[a] * PL) for a in range(8))
    rep.check('F1_hermitian_bilinears', ok_s and ok_t and ok_v and ok_a and ok_nl,
              'real (Hermitian) bilinears: Psibar P_X Psi, i Psibar S^{ab} P_X Psi, i Psibar gamma^a Psi, Psibar gamma^a Gamma Psi; '
              'Psibar gamma^a P_L Psi is neither real nor imaginary (no Hermitian left-handed vector current exists)')
    # the convective current j_X^M = i (Psibar P_X d^M Psi - d^M Psibar P_X Psi): Hermitian because sigma16 P_X is real symmetric
    ok = (C * PL).T == C * PL and (C * PR).T == C * PR and all(e.is_real for e in (C * PL))
    rep.check('F1_convective_current', ok, 'sigma16 P_X is real and symmetric, so j_X^M = i(Psibar P_X D^M Psi - (D^M Psibar) P_X Psi) is real')
    # the Lagrangian of the author's form is Hermitian: (sigma16 gamma^a)^T = -sigma16 gamma^a (antisymmetric, real)
    ok = all((C * gup[a]).T == -(C * gup[a]) for a in range(8))
    rep.check('F1_kinetic_term_real', ok, '(sigma16 gamma^a)^T = -sigma16 gamma^a: (1/2)(Psibar gamma^M D_M Psi - (D_M Psibar) gamma^M Psi) is real; no factor i is needed')

    # ---------------- F2 chirality content of bilinears
    def chir_type(M):
        LL = (PL * C * M * PL) != sp.zeros(16, 16)
        RR = (PR * C * M * PR) != sp.zeros(16, 16)
        LR = (PL * C * M * PR) != sp.zeros(16, 16) or (PR * C * M * PL) != sp.zeros(16, 16)
        return LL, RR, LR
    ok = True
    for k in range(9):
        for comb in itertools.combinations(range(8), k):
            M = I16
            for i in comb:
                M = M * T[i]
            LL, RR, LR = chir_type(M)
            if k % 2 == 0 and LR:
                ok = False
            if k % 2 == 1 and (LL or RR):
                ok = False
    rep.check('F2_even_odd_chirality', ok, 'for every one of the 256 products: an even number of gamma matrices gives only P_L-P_L and P_R-P_R terms, an odd number only P_L-P_R terms')
    ok = (C * PL) == PL * C and Gam * C == C * Gam
    rep.check('F2_adjoint_commutes_with_chirality', ok, 'sigma16 commutes with Gamma (sigma16 is a product of four gamma matrices): (P_X Psi)bar = Psibar P_X')

    # ---------------- F3 Krein operator
    B = I * C * gup[4]
    ok = is_herm(B) and (B * B) == I16
    ok2 = all(B * gup[a] == gup[a] * B for a in (0, 1, 2, 3, 4)) and all(B * gup[a] == -gup[a] * B for a in (5, 6, 7))
    ok3 = B * Gam == -Gam * B
    rep.check('F3_krein_operator', ok and ok2 and ok3,
              'B = i sigma16 gamma^(x4) is a Hermitian involution (B^2 = 1, eigenvalues +1 and -1 eight times each); it commutes with gamma^(x0), ..., gamma^(x4) '
              'and the mass term, anticommutes with gamma^(x5), gamma^(x6), gamma^(x7) and with Gamma')
    evB = B.eigenvals()
    rep.check('F3_krein_signature', evB == {1: 8, -1: 8}, 'the conserved charge density i Psibar gamma^(x4) Psi = Psi^dagger B Psi has the signature (8, 8)')
    # the one-particle Hamiltonian of a mode independent of x5, x6, x7: h = i gamma^4 (gamma^0 d_y + kappa gamma^i k_i - M)
    # it commutes with B when M is a multiple of the identity; a term Delta Gamma anticommutes with B
    out['krein'] = 'B = i sigma16 gamma^(x4); [B, gamma^(a)] = 0 (a = 0..4), {B, gamma^(t)} = 0 (t = 5, 6, 7), {B, Gamma} = 0'

    # ---------------- F4 four-dimensional chirality
    G4 = I * T[1] * T[2] * T[3] * T[4]
    ok = is_herm(G4) and G4 * G4 == I16 and all(G4 * T[a] == -T[a] * G4 for a in (1, 2, 3, 4)) and all(G4 * T[a] == T[a] * G4 for a in (0, 5, 6, 7))
    Gint = I * T[0] * T[5] * T[6] * T[7]
    ok2 = Gint * Gint == I16 and G4 * Gint == Gint * G4
    rel = sp.simplify((Gam * (G4 * Gint).inv())[0, 0]) if (G4 * Gint) != sp.zeros(16, 16) else None
    ok3 = rel is not None and Gam == rel * G4 * Gint
    rep.check('F4_four_dimensional_chirality', ok and ok2 and ok3,
              'Gamma_4 = i T1 T2 T3 T4 is a Hermitian involution anticommuting with gamma^(x1..x4) and commuting with gamma^(x0), gamma^(x5..x7); '
              'Gamma_int = i T0 T5 T6 T7 squares to 1; Gamma = %s Gamma_4 Gamma_int' % rel)
    ok = (B * G4 == G4 * B)
    rep.check('F4_krein_and_4d_chirality', ok, 'B commutes with Gamma_4: each half B = +-1 contains both four-dimensional chiralities')
    out['chirality'] = {'Gamma_4': 'i T1 T2 T3 T4', 'Gamma_int': 'i T0 T5 T6 T7', 'Gamma = c Gamma_4 Gamma_int, c': str(rel)}

    # ---------------- F5 electroweak vacuum with the ad hoc upper component
    g, gp, v, Aa = sp.symbols('g gprime v A_ad', positive=True)
    tau = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    Phi0 = sp.Matrix([Aa, v]) / sp.sqrt(2)
    # covariant derivative D Phi = (d - i g W^I tau^I/2 - i g' (1/2) B) Phi ; mass term (D Phi)^dagger (D Phi) for constant fields
    Wv = sp.symbols('W1 W2 W3 Bf', real=True)
    Xm = sum((g * Wv[I_] * tau[I_] / 2 for I_ in range(3)), sp.zeros(2, 2)) + gp * Wv[3] * sp.eye(2) / 2
    quad = sp.expand((Xm * Phi0).H * (Xm * Phi0))[0, 0]
    M2 = sp.Matrix(4, 4, lambda i, j: sp.diff(quad, Wv[i], Wv[j]))  # L_mass = (1/2) V^T M2 V
    xx = sp.Symbol('xx')
    mW2 = g**2 * (v**2 + Aa**2) / 4
    mZ2 = (g**2 + gp**2) * (v**2 + Aa**2) / 4
    charpoly = sp.factor((M2 - xx * sp.eye(4)).det())
    ok = sp.simplify(sp.expand((M2 - xx * sp.eye(4)).det()) - sp.expand(xx * (xx - mW2)**2 * (xx - mZ2))) == 0
    rep.check('F5_gauge_boson_masses', ok, 'for Phi = (A, v)/sqrt 2 (A real): one zero eigenvalue (the photon), m_W^2 = g^2 (v^2 + A^2)/4 (twice), '
              'm_Z^2 = (g^2 + g\'^2)(v^2 + A^2)/4')
    null = (M2).nullspace()
    nvec = sp.simplify(null[0] / null[0][3]) if null else None
    expect = sp.Matrix([-2 * Aa * v * gp / (g * (v**2 + Aa**2)) * (-1), 0, (v**2 - Aa**2) * gp / (g * (v**2 + Aa**2)), 1]) if False else None
    # the unit isovector of the vacuum n^I = Phi0^dagger tau^I Phi0/|Phi0|^2 and the photon A = (g' n^I W^I + g B)/sqrt(g^2 + g'^2) up to sign
    nI = [sp.simplify((Phi0.H * tau[I_] * Phi0)[0, 0] / (Phi0.H * Phi0)[0, 0]) for I_ in range(3)]
    photon = sp.Matrix([-gp * nI[0], -gp * nI[1], -gp * nI[2], g])
    ok = (M2 * photon).applyfunc(sp.simplify) == sp.zeros(4, 1)
    rep.check('F5_photon_direction', ok, 'the photon is A = (g B - g\' n^I W^I)/sqrt(g^2 + g\'^2) with n = (2Av, 0, A^2 - v^2)/(A^2 + v^2): '
              'for A = 0 the usual (g B + g\' W^3)/sqrt(g^2 + g\'^2), for A != 0 rotated towards W^1')
    out['photon_isovector'] = [str(x) for x in nI]
    # isospin current of a time-dependent vacuum: J^I_M = i/2 [Phi^dagger tau^I d_M Phi - (d_M Phi)^dagger tau^I Phi] (gauge current density)
    x4 = sp.Symbol('x4', real=True)
    a40, vA = sp.symbols('a40 v_A', positive=True)
    Af = vA * sp.exp(-2 * a40 * x4)
    Phit = sp.Matrix([Af, v]) / sp.sqrt(2)
    J = [sp.simplify(I / 2 * ((Phit.H * tau[I_] * Phit.diff(x4))[0, 0] - (Phit.diff(x4).H * tau[I_] * Phit)[0, 0])) for I_ in range(3)]
    ok = sp.simplify(J[0]) == 0 and sp.simplify(J[2]) == 0 and sp.simplify(J[1] - a40 * v * Af) == 0
    rep.check('F5_isospin_charge_density', ok, 'the ad hoc vacuum carries the weak-isospin current J^2_{x4} = (i/2)[Phi^dagger tau^2 d_4 Phi - c.c.] = a40 v v_A e^{-2 a40 x4} '
              '(J^1 = J^3 = 0): a uniform charge density of the second isospin direction, which the Gauss law of W^2 must balance')
    out['isospin_charge_density'] = str(J[1])
    # Higgs equation for the upper component on the background: -(A'' + 3 u A') - (mu^2 + lambda (A^2 + v^2)) A = 0 with mu^2 = -lambda v^2
    lam, u = sp.symbols('lambda u', real=True)
    resid = sp.simplify(-(sp.diff(Af, x4, 2) + 3 * u * sp.diff(Af, x4)) - (-lam * v**2 + lam * (Af**2 + v**2)) * Af)
    expect = -(4 * a40**2 - 6 * a40 * u) * Af - lam * Af**3
    ok = sp.simplify(resid - expect) == 0
    rep.check('F5_higgs_residual_upper', ok, 'with mu^2 = -lambda v^2 the upper component A = v_A e^{-2 a40 x4} leaves the residual '
              '-(4 a40^2 - 6 a40 u) A - lambda A^3 in its field equation (u = b4\'/b4): the ad hoc vacuum is an approximate solution, exact only as A -> 0')
    out['higgs_residual_upper'] = str(sp.factor(expect))

    # ---------------- F6 hypercharges, Yukawas, anomalies (three generations with nu_R)
    fields = {  # name: (SU3 dim, SU2 dim, Y, chirality as left-handed Weyl: +1 for left, -1 for right)
        'Q': (3, 2, Fr(1, 6), 1), 'u_R': (3, 1, Fr(2, 3), -1), 'd_R': (3, 1, Fr(-1, 3), -1),
        'l': (1, 2, Fr(-1, 2), 1), 'e_R': (1, 1, Fr(-1), -1), 'nu_R': (1, 1, Fr(0), -1)}
    YPhi = Fr(1, 2)
    yuk = {'Qbar Phitilde u_R': -fields['Q'][2] - YPhi + fields['u_R'][2], 'Qbar Phi d_R': -fields['Q'][2] + YPhi + fields['d_R'][2],
           'lbar Phi e_R': -fields['l'][2] + YPhi + fields['e_R'][2], 'lbar Phitilde nu_R': -fields['l'][2] - YPhi + fields['nu_R'][2]}
    rep.check('F6_yukawa_invariance', all(v_ == 0 for v_ in yuk.values()), 'the four Yukawa terms have total hypercharge 0: %s' % {k: str(v_) for k, v_ in yuk.items()})
    def lh(f):
        n3, n2, Y, ch = fields[f]
        return n3, n2, (Y if ch == 1 else -Y)
    A331 = sum(n2 * Y for f in fields for n3, n2, Y in [lh(f)] if n3 == 3)
    A221 = sum(n3 * Y for f in fields for n3, n2, Y in [lh(f)] if n2 == 2)
    A111 = sum(n3 * n2 * Y**3 for f in fields for n3, n2, Y in [lh(f)])
    Ag = sum(n3 * n2 * Y for f in fields for n3, n2, Y in [lh(f)])
    A333 = sum(fields[f][1] * fields[f][3] for f in fields if fields[f][0] == 3)
    ok = A331 == 0 and A221 == 0 and A111 == 0 and Ag == 0 and A333 == 0
    rep.check('F6_anomalies', ok, 'per generation: SU(3)^2U(1) = %s, SU(2)^2U(1) = %s, U(1)^3 = %s, grav^2U(1) = %s, SU(3)^3 = %s; 3 x 4 = 12 SU(2) doublets (even, no Witten anomaly)'
              % (A331, A221, A111, Ag, A333))
    qem = {f: [str(T3 + fields[f][2]) for T3 in ((Fr(1, 2), Fr(-1, 2)) if fields[f][1] == 2 else (Fr(0),))] for f in fields}
    rep.check('F6_electric_charges', qem == {'Q': ['2/3', '-1/3'], 'u_R': ['2/3'], 'd_R': ['-1/3'], 'l': ['0', '-1'], 'e_R': ['-1'], 'nu_R': ['0']},
              'Q_em = T3 + Y: %s' % qem)
    out['hypercharges'] = {f: str(fields[f][2]) for f in fields}

    out['runtime_s'] = round(time.time() - t0, 1)
    (UM4 / 'outputs').mkdir(exist_ok=True)
    (UM4 / 'reports').mkdir(exist_ok=True)
    (UM4 / 'outputs' / 'fields.json').write_text(json.dumps(out, indent=1, sort_keys=True) + '\n')
    report = {'script': 'universe_model_4/code/um4_fields.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    (UM4 / 'reports' / 'fields_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
