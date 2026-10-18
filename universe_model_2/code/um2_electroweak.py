#!/usr/bin/env python3
"""UM-2 electroweak sector: charges, anomaly cancellation, the W+- and Z, the chiral tip Z portal of dirac16complex,
the two halves Psi_A (B = -1) and Psi_B (B = +1), the Z charges of the fold band and of the dark matter, the Z invisible
width with three neutrinos, the fate of the chiral tip Z portal (dropped), and the Z widths of the three generations.
(N_eff and the cosmic neutrino background of the three neutrino flavours are computed in um2_neutrino.py.)

E1  Charges Q = T3 + Y of the zero-mode spectrum (three generations, version of 2026-10-18); W+- = (W1 -+ i W2)/sqrt2
    carry Q = +-1 ([T3, T+-] = +-T+-); photon coupling e = g g'/sqrt(g^2 + g'^2) to the charged fermions and to W+W-.
E2  Gauge anomalies of the 4D zero-mode spectrum (three generations of Q, u_R, d_R, L, e_R, nu_R; Psi is a gauge singlet):
    SU(3)^3, SU(3)^2 U(1), SU(2)^2 U(1), U(1)^3, grav^2 U(1) vanish generation by generation; SU(2) Witten anomaly: even number
    of doublets (12).  For comparison: three lepton generations with one quark generation would leave SU(2)^2 U(1) and U(1)^3.
E3  Algebra of the chiral projector P_+ = (1 + Gamma4)/2, Gamma4 = i g1 g2 g3 g4: Hermitian, commutes with the 4D
    Lorentz generators and with C gamma^mu (mu = x1..x4), so Psibar gamma^mu P_+ Psi is a 4D vector current; in the block
    basis P_+ = (1 - B sigma3)/2 with B = j s2; B commutes with the 4D Lorentz generators and with C (Psibar Psi does not
    mix the halves B = +-1); the halves Psi_A (B = -1) and Psi_B (B = +1) are 4D-Lorentz-invariant subspaces.
E4  Chiral charge densities u^dagger P_+ u at the regular tip (b(-L) = 0 for every orbital), i.e. what a chiral tip Z portal
    would couple to (UM-2 has none since the three-generation version, E5): P_+ selects the a-component in Psi_A, the
    b-component (zero at the tip) in Psi_B.  The Psi_A fold band (2 Weyl species, Gamma4 = +1) and the Psi_A odd states have
    non-zero densities; the Psi_B fold band and the Psi_B dark matter have zero density AND zero transition current, exactly.
E5  Z invisible width with the three neutrinos and a possible Z coupling of the Psi_A fold band: N_nu = 3 + 2 r^2,
    r = g_Z(Psi_A)/g_Z(nu); the PDG 2025 value N_nu = 2.9963 +- 0.0074 bounds r^2.  The chiral tip Z portal I9 of the
    one-generation version (even part c_Z, oriented part c'_Z) would thermalise the Psi_A fold band and add Delta N_eff = 2 (c_Z
    at the N_nu bound) or 0.10-0.13 (c'_Z); UM-2 drops I9 (c_Z = c'_Z = 0).  The Z widths of the three generations at tree level.
Writes outputs/electroweak.json and reports/electroweak-checks.json.
"""
import math
import os
import sys
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import OUT, ROOT, Report, read_json, write_json  # noqa: E402
from um2_constants import ETA, INPUTS, M_PSI_OVER_H, val  # noqa: E402

I = sp.I
LABELS = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]


def main():
    rep = Report('electroweak-checks', 'UM-2: charges, anomalies (three generations), W+- and Z, the chiral tip Z portal, the halves '
                 'Psi_A and Psi_B, Z charges, Z invisible width with three neutrinos, the Psi_A Z coupling, Z widths of three generations')
    out = {}
    # ---------------- E1: charges ----------------
    generation = {  # name: (SU(3) dim, SU(2) dim, Y, chirality L/R as 4D Weyl)
        'Q': (3, 2, Fr(1, 6), 'L'), 'u_R': (3, 1, Fr(2, 3), 'R'), 'd_R': (3, 1, Fr(-1, 3), 'R'),
        'L': (1, 2, Fr(-1, 2), 'L'), 'e_R': (1, 1, Fr(-1), 'R'), 'nu_R': (1, 1, Fr(0), 'R')}
    fields = generation                    # the charges are the same in every generation
    charges = {}
    for name, (nc, nw, Y, ch) in fields.items():
        if nw == 2:
            charges[name] = [str(Fr(1, 2) + Y), str(Fr(-1, 2) + Y)]
        else:
            charges[name] = [str(Y)]
    out['electric_charges'] = charges
    ok = charges['Q'] == ['2/3', '-1/3'] and charges['L'] == ['0', '-1'] and charges['u_R'] == ['2/3'] and \
        charges['d_R'] == ['-1/3'] and charges['e_R'] == ['-1'] and charges['nu_R'] == ['0']
    rep.check('electric_charges', ok, 'Q = T3 + Y in every generation: (u, d)_L = (2/3, -1/3) [also (c, s), (t, b)], (nu, l)_L = (0, -1) '
              '[l = e, mu, tau], up-type singlets 2/3, down-type -1/3, charged-lepton singlets -1, nu_R 0')
    tp = sp.Matrix([[0, 1], [0, 0]])
    t3 = sp.Matrix([[sp.Rational(1, 2), 0], [0, -sp.Rational(1, 2)]])
    rep.check('W_charges', t3 * tp - tp * t3 == tp and t3 * tp.T - tp.T * t3 == -tp.T,
              '[T3, T+] = +T+, [T3, T-] = -T-: W+ = (W1 - i W2)/sqrt2 carries Q = +1, W- = (W1 + i W2)/sqrt2 carries Q = -1 '
              '(Y(W) = 0); W- is the antiparticle of W+')
    g, gp = sp.symbols('g gprime', positive=True)
    e = g * gp / sp.sqrt(g ** 2 + gp ** 2)
    # photon field A = sin W3 + cos B; coupling of a fermion: g T3 sin + g' Y cos = e (T3 + Y)
    sW = gp / sp.sqrt(g ** 2 + gp ** 2)
    cW = g / sp.sqrt(g ** 2 + gp ** 2)
    T3s, Ys = sp.symbols('T3 Y')
    coup = sp.simplify(g * T3s * sW + gp * Ys * cW - e * (T3s + Ys))
    rep.check('photon_coupling', coup == 0, 'A = sin(theta_W) W3 + cos(theta_W) B couples with g T3 sin + g\' Y cos = e (T3 + Y), '
              'e = g g\'/sqrt(g^2 + g\'^2): e for e-, 2e/3 for u, -e/3 for d, 0 for nu; the W+W-gamma vertex has strength e')
    # Z couplings g_Z = sqrt(g^2+g'^2) (T3 - Q sin^2)
    coupZ = sp.simplify(g * T3s * cW - gp * Ys * sW - sp.sqrt(g ** 2 + gp ** 2) * (T3s - (T3s + Ys) * sW ** 2))
    rep.check('Z_coupling', coupZ == 0, 'Z = cos W3 - sin B couples with sqrt(g^2 + g\'^2)(T3 - Q sin^2 theta_W)')

    # ---------------- E2: anomalies (left-handed Weyl basis: R fields enter with -Y) ----------------
    def weyl_list(content):
        lst = []
        for (name, (nc, nw, Y, ch), copies) in content:
            sgn = 1 if ch == 'L' else -1
            for _ in range(copies):
                lst.append((name, nc, nw, sgn * Y, sgn))
        return lst

    def anomalies(W):
        a_33_1 = sum(nw * Y * (1 if nc == 3 else 0) for (_, nc, nw, Y, s_) in W)        # SU(3)^2 U(1): Tr(T^2) Y over triplets
        a_22_1 = sum(nc * Y * (1 if nw == 2 else 0) for (_, nc, nw, Y, s_) in W)        # SU(2)^2 U(1)
        a_111 = sum(nc * nw * Y ** 3 for (_, nc, nw, Y, s_) in W)                        # U(1)^3
        a_grav = sum(nc * nw * Y for (_, nc, nw, Y, s_) in W)                            # grav^2 U(1)
        a_333 = sum(s_ * nw * (1 if nc == 3 else 0) for (_, nc, nw, Y, s_) in W)        # SU(3)^3 (triplets L minus R)
        ndoub = sum(nc for (_, nc, nw, Y, s_) in W if nw == 2)
        return a_33_1, a_22_1, a_111, a_grav, a_333, ndoub
    W3 = weyl_list([(n, generation[n], 3) for n in generation])
    a3 = anomalies(W3)
    Wcf = weyl_list([(n, generation[n], 1 if n in ('Q', 'u_R', 'd_R') else 3) for n in generation])
    acf = anomalies(Wcf)
    out['anomalies_three_generations'] = [str(x) for x in a3]
    out['anomalies_three_lepton_one_quark_generation'] = [str(x) for x in acf]
    rep.check('anomaly_cancellation', all(x == 0 for x in a3[:5]) and a3[5] % 2 == 0 and (acf[1] != 0 and acf[2] != 0),
              'three generations (Q, u_R, d_R, L, e_R, nu_R) as 4D Weyl zero modes: SU(3)^2U(1) %s, SU(2)^2U(1) %s, U(1)^3 %s, grav^2U(1) %s, '
              'SU(3)^3 %s; %d SU(2) doublets (even: no Witten anomaly); dirac16complex is a gauge singlet. Three lepton generations with ONE '
              'quark generation would leave SU(2)^2U(1) = %s and U(1)^3 = %s: the second and third quark generations are required' % (
                  a3[0], a3[1], a3[2], a3[3], a3[4], a3[5], acf[1], acf[2]))

    # ---------------- E3: chiral projector algebra ----------------
    alg = read_json(os.path.join(OUT, 'algebra.json'))
    gm = [sp.Matrix(alg['gamma'][a]) for a in range(8)]
    C = sp.Matrix(alg['C'])
    I16 = sp.eye(16)
    G4 = I * gm[1] * gm[2] * gm[3] * gm[4]
    Pp = (I16 + G4) / 2
    Bm = -I * C * gm[4]
    lorentz = [gm[a] * gm[b] for a in range(1, 5) for b in range(a + 1, 5)]
    comm = lambda X, Y: (X * Y - Y * X).applyfunc(sp.simplify)
    Z16 = sp.zeros(16, 16)
    rep.check('P_plus_projector_hermitian', (Pp * Pp - Pp).applyfunc(sp.simplify) == Z16 and (Pp.H - Pp).applyfunc(sp.simplify) == Z16,
              'P_+ = (1 + Gamma4)/2 is a Hermitian projector')
    rep.check('P_plus_lorentz_invariant', all(comm(Pp, L) == Z16 for L in lorentz), 'P_+ commutes with every 4D Lorentz generator gamma^a gamma^b (a, b = x1..x4)')
    rep.check('chiral_current_is_vector', all(comm(Pp, C * gm[m]) == Z16 for m in (1, 2, 3, 4)),
              'P_+ commutes with C gamma^mu (mu = x1..x4): Psibar gamma^mu P_+ Psi = (P_+ Psi)^dagger C gamma^mu (P_+ Psi) is the 4D vector current of the Gamma4 = +1 part')
    rep.check('B_lorentz_invariant', all(comm(Bm, L) == Z16 for L in lorentz) and comm(Bm, C) == Z16,
              'B commutes with every 4D Lorentz generator and with C: the halves B = -1 (Psi_A) and B = +1 (Psi_B) are 4D-Lorentz-invariant and '
              'Psibar Psi = S_A + S_B does not mix them')
    rep.check('Gamma4_equals_minus_B_gamma0', (G4 + Bm * gm[0]).applyfunc(sp.simplify) == Z16 and comm(Bm, gm[0]) == Z16,
              'Gamma4 = i g1 g2 g3 g4 = -B gamma^(x0) as 16 x 16 matrices, [B, gamma^(x0)] = 0: P_+ = (1 - B gamma^(x0))/2, i.e. (1 + gamma^(x0))/2 on '
              'Psi_A and (1 - gamma^(x0))/2 on Psi_B, which annihilates Psi_B wherever (1 - gamma^(x0)) Psi = 0 (the regular tip)')
    ks = read_json(os.path.join(ROOT, 'Revision', 'kohn_sham', 'ks-theory.json'))
    cols = ks['blockBasis']['unnormalisedColumns2Sqrt2V']
    V = sp.Matrix(16, 16, lambda r, c: sp.sympify(cols[r][c])) / (2 * sp.sqrt(2))
    s3 = sp.Matrix([[1, 0], [0, -1]])
    target = sp.diag(*[(sp.eye(2) - (j * ss2) * s3) / 2 for (j, ss2, ss3) in LABELS])
    rep.check('P_plus_block_form', (V.H * Pp * V - target).applyfunc(sp.simplify) == Z16,
              'in block (j, s2, s3): P_+ = (1 - B sigma3)/2, B = j s2: the a-component in Psi_A (B = -1), the b-component in Psi_B (B = +1)')
    groupA = [b for b, (j, ss2, ss3) in enumerate(LABELS) if j * ss2 == -1]
    groupB = [b for b, (j, ss2, ss3) in enumerate(LABELS) if j * ss2 == 1]
    sel = read_json(os.path.join(OUT, 'fields.json'))['selected_blocks']
    rep.check('sm_zero_modes_in_psiA_blocks', all(LABELS.index(tuple(s)) in groupA for s in sel),
              'the blocks that carry the Standard-Model zero modes, %s, have B = -1: the visible zero modes live in the B = -1 half' % sel)

    # ---------------- E4: Z charges at the tip ----------------
    bg = read_json(os.path.join(OUT, 'background.json'))
    f = bg['casimir_type']['f_star']
    L = ETA
    m = M_PSI_OVER_H
    fL = f * L
    # fold-band zero mode (even, theta = 0): chi = (e^{f m y}, 0), normalised on [-L, 0]
    n0 = (1 - math.exp(-2 * f * m * L)) / (2 * f * m)
    a0_tip2 = math.exp(-2 * f * m * L) / n0
    # dark-matter (lowest odd) orbital: a = sin(f p y), b = (m sin(f p y) - p cos(f p y))/eps, tan(p f L) = -p/m
    p = brentq(lambda pp: math.sin(pp * fL) * m + pp * math.cos(pp * fL), (0.5 * math.pi + 1e-12) / fL, (math.pi - 1e-12) / fL, xtol=1e-15)
    eps = math.sqrt(m * m + p * p)
    yq, wq = np.polynomial.legendre.leggauss(400)
    yq = -L / 2 + L / 2 * yq
    wq = wq * L / 2
    aq = np.sin(f * p * yq)
    bq = (m * np.sin(f * p * yq) - p * np.cos(f * p * yq)) / eps
    nd = float(np.sum(wq * (aq ** 2 + bq ** 2)))
    adm_tip2 = math.sin(-f * p * L) ** 2 / nd
    bdm_tip = (m * math.sin(-f * p * L) - p * math.cos(-f * p * L)) / eps
    rep.check('tip_condition_b_zero', abs(bdm_tip) < 1e-12, 'the dark-matter orbital satisfies b(-L) = 0 (regular tip): %.1e' % bdm_tip)
    # 16-component check of charges with the record's V: zero-mode/DM spinor at the tip in every block
    charges_zero = {}
    charges_dm = {}
    trans_ok = True
    for b in range(8):
        chi0 = sp.Matrix([math.sqrt(a0_tip2), 0])
        chid = sp.Matrix([math.sqrt(adm_tip2) * (-1 if math.sin(-f * p * L) < 0 else 1), 0])
        u0 = V[:, 2 * b:2 * b + 2] * chi0
        ud = V[:, 2 * b:2 * b + 2] * chid
        q0 = complex(sp.N((u0.H * Pp * u0)[0]))
        qd = complex(sp.N((ud.H * Pp * ud)[0]))
        charges_zero[str(LABELS[b])] = q0.real
        charges_dm[str(LABELS[b])] = qd.real
        if b in groupB:
            # transition currents between this Psi_B state and every Psi_A tip spinor: (P_+ u_B) = 0
            for mm in (1, 2, 3, 4):
                for bb in groupA:
                    uA = V[:, 2 * bb:2 * bb + 2] * sp.Matrix([1, 1])
                    t1 = complex(sp.N((uA.H * C * gm[mm] * Pp * ud)[0]))
                    t2 = complex(sp.N((ud.H * C * gm[mm] * Pp * uA)[0]))
                    if abs(t1) > 1e-12 or abs(t2) > 1e-12:
                        trans_ok = False
    out['tip_charge_zero_mode_by_block'] = charges_zero
    out['tip_charge_dm_by_block'] = charges_dm
    zA = [charges_zero[str(LABELS[b])] for b in groupA]
    zB = [charges_zero[str(LABELS[b])] for b in groupB]
    dA = [charges_dm[str(LABELS[b])] for b in groupA]
    dB = [charges_dm[str(LABELS[b])] for b in groupB]
    rep.check('Z_charge_fold_band', all(abs(x - a0_tip2) < 1e-12 for x in zA) and all(abs(x) < 1e-14 for x in zB),
              'chiral tip charge density u^dagger P_+ u (what a chiral tip Z portal would couple to; UM-2 has none): Psi_A fold band '
              'a0(-L)^2 = %.6e per unit length in each of its 4 blocks, Psi_B fold band 0 exactly' % a0_tip2)
    rep.check('Z_charge_dark_matter', all(abs(x - adm_tip2) < 1e-12 for x in dA) and all(abs(x) < 1e-14 for x in dB) and trans_ok,
              'lowest odd states: Psi_A a_DM(-L)^2 = %.6e; Psi_B 0 exactly, and every transition current '
              'Psibar_A gamma^mu P_+ Psi_B and Psibar_B gamma^mu P_+ Psi_A vanishes at the tip (P_+ Psi_B = 0 there)' % adm_tip2)
    out['a0_tip2'] = a0_tip2
    out['adm_tip2'] = adm_tip2
    out['ratio_dm_to_fold_band_Psi_A'] = adm_tip2 / a0_tip2

    # ---------------- E5: Z invisible width, the Psi_A coupling, Z widths ----------------
    Nnu, dNnu = INPUTS['N_nu'][0], INPUTS['N_nu'][1]
    r2_max = (Nnu + 2 * dNnu - 3.0) / 2.0          # N_nu = 3 + 2 r^2 within two standard deviations
    out['Z_portal'] = {'N_nu': Nnu, 'N_nu_uncertainty': dNnu, 'N_nu_model': 3.0, 'pull_r0': (3.0 - Nnu) / dNnu,
                       'r2_max_Z_width_2sigma': r2_max, 'r2_benchmark': 0.0, 'c_Z_benchmark': 0.0}
    rep.check('Z_invisible_width', abs((3.0 - Nnu) / dNnu) < 1.0 and 0 < r2_max < 0.01,
              'with the three neutrinos and the Psi_A fold band of Z coupling r times the neutrino\'s, N_nu = 3 + 2 r^2; the PDG 2025 value '
              'N_nu = %.4f +- %.4f (Janot and Jadach 2020) is reproduced by r = 0 (pull %.2f) and bounds r^2 < %.4f (two standard deviations); '
              '(the superseded LEP 2006 value 2.9840 +- 0.0082 lies 1.9 standard deviations below 3)' % (Nnu, dNnu, (3.0 - Nnu) / dNnu, r2_max))
    # What the chiral tip Z portal I9 of the one-generation version would do with three generations (ESTIMATES, from the
    # decoupling condition of a species of two Weyl fermions; g_s counts the plasma it decouples from):
    #  (a) even part c_Z: Z coupling r times the neutrino's; below the Z mass its neutral-current rate is r^2 times the neutrino's,
    #      so it decouples at T = 2.6 MeV r^{-2/3} (FROM MEMORY: a species with neutral-current interactions only decouples near
    #      2.6 MeV); at the Z-width bound this is still in the plasma of photons, e+- and three neutrinos (g_s = 10.75);
    #  (b) oriented part c'_Z: Psi_A^odd <-> Psi_A^fold + Z and Psi_A^fold Z -> Psi_A^fold Z (Psi_A^odd exchange) keep the Psi_A
    #      fold band in equilibrium while the heavy odd states or the Z bosons are abundant, i.e. until T ~ M/30 (g_s = 105.75: the
    #      Standard Model without a Higgs particle; right-handed neutrinos never thermalised) or, for c'_Z of the size of the
    #      neutrino's Z coupling, until the Z bosons annihilate near T ~ 15 GeV (g_s = 86.25: t, W, Z gone).
    # Delta N_eff = 2 (10.75/g_s)^{4/3} x F, F = [(T_nu/T_gamma)(11/4)^{1/3}/(1 + heating)]^4 the correction for the non-instantaneous
    # neutrino decoupling (the fold band, decoupled long before, is not heated by e+e- annihilation), from um2_neutrino.py.
    nu = read_json(os.path.join(OUT, 'neutrino.json'))
    run_ = nu['N_eff_runs']['FD_common_NLO']
    Fnon = (run_['Tnu_e_over_Tgamma'] * (11.0 / 4.0) ** (1.0 / 3.0) / (1 + run_['heating_Te_a'])) ** 4
    Neff_sm = nu['N_eff_adopted']['value']

    def dNeff(gs, nweyl=2):
        return nweyl * (10.75 / gs) ** (4.0 / 3.0) * Fnon
    g_s = {'neutrino plasma (photons, e+-, 3 nu)': 10.75, 'just above the QCD crossover (+ gluons, u, d, s, mu)': 61.75,
           'after t, W, Z annihilation (T ~ 15 GeV)': 86.25, 'above the electroweak scale (Standard Model without a Higgs particle)': 105.75}
    T_nu_dec = 2.6e-3
    T_dec_at_bound = T_nu_dec * r2_max ** (-1.0 / 3.0)
    dN_a = dNeff(10.75) if T_dec_at_bound < 0.03 else None
    dN_b = (dNeff(105.75), dNeff(86.25))
    Neff_cmb, dNeff_cmb = val('N_eff_Planck2018'), INPUTS['N_eff_Planck2018'][1]
    Neff_act, dNeff_act = val('N_eff_ACT_DR6'), INPUTS['N_eff_ACT_DR6'][1]
    out['Psi_A_thermalisation'] = {
        'non_instantaneous_factor_F': Fnon, 'g_s_reference_values': g_s,
        'Delta_Neff_two_Weyl_species': {k: dNeff(v) for k, v in g_s.items()},
        'even_part_T_dec_GeV_at_Z_width_bound': T_dec_at_bound, 'even_part_Delta_Neff_at_Z_width_bound': dN_a,
        'oriented_part_Delta_Neff_range': list(dN_b), 'N_eff_with_oriented_part_range': [Neff_sm + dN_b[0], Neff_sm + dN_b[1]],
        'N_eff_Planck2018': [Neff_cmb, dNeff_cmb], 'N_eff_ACT_DR6': [Neff_act, dNeff_act],
        'pull_ACT_DR6_SM': (Neff_sm - Neff_act) / dNeff_act,
        'pull_ACT_DR6_oriented_part': [(Neff_sm + x - Neff_act) / dNeff_act for x in dN_b],
        'decision': 'I9 dropped: c_Z = c\'_Z = 0'}
    out['Z_portal']['I9'] = 'dropped in the three-generation version (c_Z = c\'_Z = 0)'
    rep.check('tip_Z_portal_dropped', dN_a is not None and (Neff_sm + dN_a - Neff_cmb) / dNeff_cmb > 5 and
              (Neff_sm + dN_b[0] - Neff_act) / dNeff_act > 2,
              'the chiral tip Z portal I9 of the one-generation version made the Psi_A fold band stand in for the missing nu_mu, nu_tau. '
              'With three generations: (a) its even part c_Z is bounded by N_nu (r^2 < %.4f); at the bound the fold band would decouple at '
              '%.1f MeV (g_s = 10.75) and add Delta N_eff = %.2f, excluded (N_eff = %.2f +- %.2f, Planck 2018; %.2f +- %.2f, ACT DR6); '
              '(b) its oriented part c\'_Z would keep the fold band in equilibrium through Psi_A^odd <-> Psi_A^fold + Z until T ~ M/30 or '
              'until the Z bosons annihilate (ESTIMATE), adding Delta N_eff = %.4f to %.4f (g_s = 105.75 to 86.25, with the factor %.4f of '
              'non-instantaneous neutrino decoupling): N_eff = %.3f to %.3f, %.1f to %.1f standard deviations above ACT DR6 (the Standard '
              'Model value %.4f: %.1f). UM-2 therefore drops I9 (c_Z = c\'_Z = 0): N_nu = 3 exactly; neither fold band is ever thermalised '
              '(no tip operator, zero scalar density for I12, c_V = 0 for I11); both halves keep an exact fold parity, so the lightest odd '
              'states of Psi_A and of Psi_B are both stable (um2_analysis.py, part B)' % (
                  r2_max, T_dec_at_bound * 1e3, dN_a, Neff_cmb, dNeff_cmb, Neff_act, dNeff_act, dN_b[0], dN_b[1], Fnon,
                  Neff_sm + dN_b[0], Neff_sm + dN_b[1], (Neff_sm + dN_b[0] - Neff_act) / dNeff_act,
                  (Neff_sm + dN_b[1] - Neff_act) / dNeff_act, Neff_sm, (Neff_sm - Neff_act) / dNeff_act))
    # Z widths of three generations (tree level, massless fermions; hadronic channels with the QCD factor 1 + alpha_s/pi for comparison)
    GF = val('G_F_GeV-2')
    mZ = val('m_Z_GeV')
    s2 = val('sin2_theta_W_MSbar')
    G0 = GF * mZ ** 3 / (6 * math.sqrt(2) * math.pi)

    def width(T3, Q, Nc, s2_):
        return Nc * G0 * ((T3 - 2 * Q * s2_) ** 2 + T3 ** 2)
    chans = {'nu (each of 3)': (0.5, 0, 1), 'charged lepton (each of e, mu, tau)': (-0.5, -1, 1),
             'up-type quark (each of u, c)': (0.5, 2.0 / 3.0, 3), 'down-type quark (each of d, s, b)': (-0.5, -1.0 / 3.0, 3)}
    Wd = {k: width(*v, s2) for k, v in chans.items()}
    G_inv = 3 * Wd['nu (each of 3)']
    G_lep = Wd['charged lepton (each of e, mu, tau)']
    G_had = 2 * Wd['up-type quark (each of u, c)'] + 3 * Wd['down-type quark (each of d, s, b)']
    tot = G_inv + 3 * G_lep + G_had
    qcd = 1 + val('alpha_s_mZ') / math.pi
    tot_qcd = G_inv + 3 * G_lep + qcd * G_had
    GZ_meas = val('Gamma_Z_MeV')
    Ginv_meas = val('B_Z_invisible') * GZ_meas
    Rl_meas = val('B_Z_hadrons') / val('B_Z_ll')
    out['Z_widths_tree_MeV'] = {k: v * 1e3 for k, v in Wd.items()}
    out['Z_widths_tree_MeV'].update({'invisible (3 nu)': G_inv * 1e3, 'hadronic': G_had * 1e3, 'total': tot * 1e3,
                                     'hadronic_with_QCD_factor': qcd * G_had * 1e3, 'total_with_QCD_factor': tot_qcd * 1e3,
                                     'R_l_with_QCD_factor': qcd * G_had / G_lep, 'measured_total': GZ_meas, 'measured_invisible': Ginv_meas,
                                     'measured_R_l': Rl_meas, 'Psi_A': 0.0, 'top': 'kinematically closed'})
    # scheme dependence: the tree-level angle of the couplings of the W/Z mass fit instead of the MS-bar value
    s2c = 1 - (val('m_W_GeV') / mZ) ** 2 / (1 + val('rho0_minus_1'))
    Wc = {k: width(*v, s2c) for k, v in chans.items()}
    totc = 3 * Wc['nu (each of 3)'] + 3 * Wc['charged lepton (each of e, mu, tau)'] + 2 * Wc['up-type quark (each of u, c)'] + \
        3 * Wc['down-type quark (each of d, s, b)']
    out['Z_widths_tree_MeV_coupling_angle'] = {'sin2_theta': s2c, 'total': totc * 1e3, 'relative_change_total': totc / tot - 1}
    rep.check('Z_width_scheme', abs(totc / tot - 1) < 0.02,
              'with the tree-level angle of the couplings of the mass fit (sin^2 = %.5f) instead of the MS-bar %.5f the total tree-level width '
              'changes by %+.2f %%: a scheme ambiguity at the per-cent level' % (s2c, s2, 100 * (totc / tot - 1)))
    rep.check('Z_widths_three_generations', abs(tot_qcd * 1e3 / GZ_meas - 1) < 0.01 and abs(G_inv * 1e3 / Ginv_meas - 1) < 0.01 and
              abs(qcd * G_had / G_lep / Rl_meas - 1) < 0.01,
              'tree-level Z widths of the three generations (massless fermions, MS-bar angle): invisible (3 nu) %.1f MeV (measured %.1f, PDG 2025), '
              'each charged lepton %.1f MeV, hadronic %.1f MeV (with the QCD factor 1 + alpha_s/pi: %.1f MeV), total %.1f MeV (%.1f MeV with the '
              'QCD factor; measured %.1f MeV); R_l = %.2f (measured %.2f): the three generations reproduce the Z width to the size of the '
              'electroweak loop corrections that UM-2 does not compute; the one-generation conflict (total 1232 MeV) is gone' % (
                  G_inv * 1e3, Ginv_meas, G_lep * 1e3, G_had * 1e3, qcd * G_had * 1e3, tot * 1e3, tot_qcd * 1e3, GZ_meas,
                  qcd * G_had / G_lep, Rl_meas))
    write_json(os.path.join(OUT, 'electroweak.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
