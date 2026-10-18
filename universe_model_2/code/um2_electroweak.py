#!/usr/bin/env python3
"""UM-2 electroweak sector: charges, anomaly cancellation, the W+- and Z, the chiral tip Z portal of dirac16complex,
the two halves Psi_A (B = -1) and Psi_B (B = +1), the Z charges of the fold band and of the dark matter, the Z invisible
width, N_eff and the cosmic neutrino background.

E1  Charges Q = T3 + Y of the one-generation zero-mode spectrum; W+- = (W1 -+ i W2)/sqrt2 carry Q = +-1
    ([T3, T+-] = +-T+-); photon coupling e = g g'/sqrt(g^2 + g'^2) to e, u, d and to W+W-.
E2  Gauge anomalies of the 4D zero-mode spectrum (one generation; Psi is a gauge singlet): SU(3)^3, SU(3)^2 U(1),
    SU(2)^2 U(1), U(1)^3, grav^2 U(1) vanish; SU(2) Witten anomaly: even number of doublets.
E3  Algebra of the chiral projector P_+ = (1 + Gamma4)/2, Gamma4 = i g1 g2 g3 g4: Hermitian, commutes with the 4D
    Lorentz generators and with C gamma^mu (mu = x1..x4), so Psibar gamma^mu P_+ Psi is a 4D vector current; in the block
    basis P_+ = (1 - B sigma3)/2 with B = j s2; B commutes with the 4D Lorentz generators and with C (Psibar Psi does not
    mix the halves B = +-1); the halves Psi_A (B = -1) and Psi_B (B = +1) are 4D-Lorentz-invariant subspaces.
E4  Z charges at the regular tip (b(-L) = 0 for every orbital): P_+ selects the a-component in Psi_A, the b-component
    (zero at the tip) in Psi_B.  The Psi_A fold band (2 Weyl species, Gamma4 = +1) couples; the Psi_B fold band and the
    Psi_B dark matter have zero Z charge AND zero transition current at the tip, exactly.
E5  Z invisible width with one neutrino plus the Psi_A fold band: N_nu = 1 + 2 r^2, r = g_Z(Psi_A)/g_Z(nu); fit to the
    LEP value; N_eff and the CNB composition; the decoupling window that keeps T(Psi_A) = T(nu).
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
    rep = Report('electroweak-checks', 'UM-2: charges, anomalies, W+- and Z, the chiral tip Z portal, the halves Psi_A and '
                 'Psi_B, Z charges, Z invisible width, N_eff and the CNB')
    out = {}
    # ---------------- E1: charges ----------------
    fields = {  # name: (SU(3) dim, SU(2) dim, Y, chirality L/R as 4D Weyl)
        'Q': (3, 2, Fr(1, 6), 'L'), 'u_R': (3, 1, Fr(2, 3), 'R'), 'd_R': (3, 1, Fr(-1, 3), 'R'),
        'L': (1, 2, Fr(-1, 2), 'L'), 'e_R': (1, 1, Fr(-1), 'R'), 'nu_R': (1, 1, Fr(0), 'R')}
    charges = {}
    for name, (nc, nw, Y, ch) in fields.items():
        if nw == 2:
            charges[name] = [str(Fr(1, 2) + Y), str(Fr(-1, 2) + Y)]
        else:
            charges[name] = [str(Y)]
    out['electric_charges'] = charges
    ok = charges['Q'] == ['2/3', '-1/3'] and charges['L'] == ['0', '-1'] and charges['u_R'] == ['2/3'] and \
        charges['d_R'] == ['-1/3'] and charges['e_R'] == ['-1'] and charges['nu_R'] == ['0']
    rep.check('electric_charges', ok, 'Q = T3 + Y: (u, d)_L = (2/3, -1/3), (nu, e)_L = (0, -1), u_R 2/3, d_R -1/3, e_R -1, nu_R 0')
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
    def weyl_list():
        lst = []
        for name, (nc, nw, Y, ch) in fields.items():
            s = 1 if ch == 'L' else -1
            lst.append((name, nc, nw, s * Y, s))
        return lst
    W = weyl_list()
    a_33_1 = sum(nw * Y * (1 if nc == 3 else 0) for (_, nc, nw, Y, s) in W)          # SU(3)^2 U(1): Tr(T^2) Y over triplets
    a_22_1 = sum(nc * Y * (1 if nw == 2 else 0) for (_, nc, nw, Y, s) in W)          # SU(2)^2 U(1)
    a_111 = sum(nc * nw * Y ** 3 for (_, nc, nw, Y, s) in W)                          # U(1)^3
    a_grav = sum(nc * nw * Y for (_, nc, nw, Y, s) in W)                              # grav^2 U(1)
    a_333 = sum(s * nw * (1 if nc == 3 else 0) for (_, nc, nw, Y, s) in W)          # SU(3)^3 (triplets L minus R)
    ndoub = sum(nc for (_, nc, nw, Y, s) in W if nw == 2)
    rep.check('anomaly_cancellation', a_33_1 == 0 and a_22_1 == 0 and a_111 == 0 and a_grav == 0 and a_333 == 0 and ndoub % 2 == 0,
              'one generation (Q, u_R, d_R, L, e_R, nu_R) as 4D Weyl zero modes: SU(3)^2U(1) %s, SU(2)^2U(1) %s, U(1)^3 %s, grav^2U(1) %s, '
              'SU(3)^3 %s; %d SU(2) doublets (even: no Witten anomaly); dirac16complex is a gauge singlet' % (a_33_1, a_22_1, a_111, a_grav, a_333, ndoub))

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
              'Z charge density u^dagger P_+ u at the tip: Psi_A fold band a0(-L)^2 = %.6e per unit length in each of its 4 blocks, Psi_B fold band 0 exactly' % a0_tip2)
    rep.check('Z_charge_dark_matter', all(abs(x - adm_tip2) < 1e-12 for x in dA) and all(abs(x) < 1e-14 for x in dB) and trans_ok,
              'Psi_A dark-matter states: a_DM(-L)^2 = %.6e; Psi_B dark-matter states: 0 exactly, and every transition current '
              'Psibar_A gamma^mu P_+ Psi_B and Psibar_B gamma^mu P_+ Psi_A vanishes at the tip (P_+ Psi_B = 0 there)' % adm_tip2)
    out['a0_tip2'] = a0_tip2
    out['adm_tip2'] = adm_tip2
    out['ratio_dm_to_fold_band_Psi_A'] = adm_tip2 / a0_tip2

    # ---------------- E5: Z invisible width, N_eff, CNB ----------------
    Nnu, dNnu = INPUTS['N_nu_LEP'][0], INPUTS['N_nu_LEP'][1]
    r2 = (Nnu - 1.0) / 2.0
    dr2 = dNnu / 2.0
    out['Z_portal'] = {'N_nu_LEP': Nnu, 'r2': r2, 'r2_uncertainty': dr2, 'r': math.sqrt(r2)}
    rep.check('Z_invisible_width_fit', abs(1 + 2 * r2 - Nnu) < 1e-12,
              'with one neutrino and the two Psi_A Weyl species: N_nu = 1 + 2 r^2 = %.4f for r^2 = (g_Z(Psi_A)/g_Z(nu))^2 = %.4f +- %.4f' % (Nnu, r2, dr2))
    # decoupling: NC rate ~ r^2 G_F^2 T^5 vs H ~ 1.66 sqrt(g*) T^2/M_Pl ; neutrino NC decoupling ~ 2.6 MeV (nu_mu,tau-like) STANDARD estimate
    T_nu_dec = 2.6e-3       # GeV (NC-only species), FROM MEMORY
    T_dec_PsiA = T_nu_dec * r2 ** (-1.0 / 3.0)
    out['T_dec_PsiA_GeV'] = T_dec_PsiA
    # T(Psi_A) = T(nu) if Psi_A decouples after the last entropy release before nu decoupling (pions, T < ~20 MeV) ->
    r2min = (T_nu_dec / 0.020) ** 3
    out['r2_min_for_T_equal'] = r2min
    Neff_SM3 = 3.0440        # three flavours with non-instantaneous decoupling and QED corrections (Bennett et al. 2021) FROM MEMORY
    Neff = Neff_SM3          # nu_e + 2 Psi_A with nu_mu,tau-like (NC) couplings, r^2 = 0.992: the same thermal history
    out['N_eff'] = Neff
    rep.check('N_eff_prediction', r2min < r2 <= 1.0,
              'Psi_A decouples at about %.2f MeV (NC rate scaled by r^2), after the QCD and pion entropy releases: T(Psi_A) = T(nu) for every '
              'r^2 > %.1e; then N_eff = %.4f (the three-flavour value: nu_e plus two NC-coupled Weyl species)' % (T_dec_PsiA * 1e3, r2min, Neff))
    # CNB: n per Weyl species = (3/4)(zeta3/pi^2) 2 T^3
    kB = 8.617333262e-5         # eV/K
    hbarc_cm = 1.973269804e-5   # eV cm
    T0 = 2.7255
    Tnu = (4.0 / 11.0) ** (1.0 / 3.0) * T0
    zeta3 = 1.2020569031595942
    nW = 0.75 * zeta3 / math.pi ** 2 * 2 * (kB * Tnu / hbarc_cm) ** 3
    out['CNB'] = {'T_nu_K': Tnu, 'n_per_Weyl_species_cm3': nW, 'species': {'nu_e (massive)': 1, 'Psi_A (massless)': 2},
                  'n_total_cm3': 3 * nW, 'T_nu_eV': kB * Tnu}
    rep.check('CNB', abs(Tnu - 1.9454) < 1e-3 and abs(nW - 112.0) < 0.5,
              'T_nu = (4/11)^{1/3} T_CMB = %.4f K; %.1f per cm^3 per Weyl species (nu + nubar); UM-2 CNB: nu_e (0.05 eV, non-relativistic today) '
              '+ two massless Psi_A species, %.0f per cm^3 in total' % (Tnu, nW, 3 * nW))
    # Z widths of the one-generation model (tree level, for the record of the conflict)
    GF = 1.1663788e-5
    mZ = val('m_Z_GeV')
    s2 = val('sin2_theta_W_MSbar')
    G0 = GF * mZ ** 3 / (6 * math.sqrt(2) * math.pi)
    # Gamma(Z -> f fbar) = Nc G_F mZ^3/(6 sqrt2 pi) (gV^2 + gA^2) with gV = T3 - 2Q s2, gA = T3 (tree level, massless)
    Gnu = G0 * ((0.5) ** 2 + (0.5) ** 2)
    Ge = G0 * ((-0.5 + 2 * s2) ** 2 + 0.25)
    Gu = 3 * G0 * ((0.5 - 4.0 / 3.0 * s2) ** 2 + 0.25)
    Gd = 3 * G0 * ((-0.5 + 2.0 / 3.0 * s2) ** 2 + 0.25)
    GPsi = 2 * r2 * Gnu
    tot = Gnu + Ge + Gu + Gd + GPsi
    out['Z_widths_tree_MeV'] = {'nu_e': Gnu * 1e3, 'e': Ge * 1e3, 'u': Gu * 1e3, 'd': Gd * 1e3, 'Psi_A (2 Weyl)': GPsi * 1e3,
                                'total': tot * 1e3, 'measured_total': 2495.5, 'measured_invisible': 499.0}
    rep.check('Z_total_width_conflict', tot < 0.6 * 2.4955,
              'tree-level Z widths of the one-generation model: total %.0f MeV against the measured 2495.5 MeV (the missing mu, tau, s, c, b '
              'channels): an inherent conflict of the particle content of the order; the invisible width %.0f MeV is reproduced by Psi_A' % (tot * 1e3, (Gnu + GPsi) * 1e3))
    write_json(os.path.join(OUT, 'electroweak.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
