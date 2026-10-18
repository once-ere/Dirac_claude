#!/usr/bin/env python3
"""UM-2 Kohn-Sham jobs: dirac16complex on the stabilised block, coupled to the Standard-Model fields (portal mean
fields) and to gravity (block feedback).  Every job is a separate calculation (each well under 423 s).

Jobs:
  validate   the independent solver reproduces the record's reference states (Revision/kohn_sham/reference) at a4 = 0
  spectrum   the free spectrum at the static block f* (exact formulas vs solver): fold band, dark-matter level, bulk
  ground     interacting ground states N = 8 (the k = 0 fold zero modes) and N = 592 (a fold-band gas) with
             lambda = +-lambda_rec f*^4 (the record's dimensionless coupling lambda/Vol7), EMT, conservation
  darkmatter 8 dark-matter quanta (lowest odd level, k = 0) on the N = 8 ground state: energy, w, hidden pressure,
             the hidden-pressure identity p0/rho = -d ln eps_DM / d ln f
  portals    linear response of the dark-matter level and of the fold band to the portal mean fields (vector P1/P2,
             derivative-scalar P6, gauge-kinetic P5, Z portal P4 at the tip); Hellmann-Feynman check
  feedback   the block response to the Kohn-Sham hidden pressure and the self-consistent loop with the fermion masses
Writes outputs/ks/<job>.json and reports/ks-checks-<job>.json.
"""
import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import OUT, Report, read_json, write_json  # noqa: E402
from um2_constants import ETA, M_PSI_OVER_H  # noqa: E402
from um2_kohnsham import Cell, KSState  # noqa: E402

KSDIR = os.path.join(OUT, 'ks')
os.makedirs(KSDIR, exist_ok=True)
H = 1.0
L = ETA / H
DK = 0.25
VT = 1.0
LAM_B = 7.0e-5        # benchmark self-coupling (units H^-6): mean fields below 5 % of m in the densest benchmark state


def fstar():
    return read_json(os.path.join(OUT, 'background.json'))['casimir_type']['f_star']


def vol7(f):
    return (2 * math.pi / DK) ** 3 * VT * f ** 4


def fixed_dm(nq_per_j=4):
    """Occupy the k = 0 fold zero modes (j = +-1, even, 4 + 4) and the lowest odd particle level of j = +-1 at k = 0."""
    def sel(secs):
        out = []
        for si, s in enumerate(secs):
            if s['n2'] != 0:
                continue
            if s['parity'] == 'even':
                out.append((si, s['nneg'], s['g']))          # zero mode (rank 0)
            else:
                out.append((si, s['nneg'], nq_per_j))         # lowest odd level, nq_per_j quanta
        return out
    return sel


def job_validate(rep):
    out = {}
    refs = {
        'N8_lamp1_a00': (8, 157.7, 16, -3.778668292317285e-02, -9.410183271484769e-03, 2.405774163364885e-01, -8.860537548434820e-02),
        'N592_lamp1_a00': (592, 2.131, 64, 3.583010464478709e+02, 7.810583066786898e-01, 8.196428960117140e-01, -6.769141510811459e+00),
    }
    for name, (N, lam, n2max, E_ref, h_ref, l_ref, p0_ref) in refs.items():
        res = []
        for nb in (60, 120):
            c = Cell(f=1.0, L=3.0, H=1.0, m=1.0, nb=nb, nq=10 * nb)
            st = KSState(c, dk=0.25, N=N, lam=lam, n2max=n2max).scf(tol=1e-13, mix=0.7)
            E, _, _ = st.energy()
            hh, ll = st.homo_lumo()
            p0 = st.integrate(st.emt()['p0'])
            res.append((E, hh, ll, p0))
        E, hh, ll = res[1][:3]
        p0x = res[1][3] + (res[1][3] - res[0][3]) / 7.0          # Richardson, order 3 in nb
        out[name] = {'E': E, 'E_ref': E_ref, 'HOMO': hh, 'HOMO_ref': h_ref, 'LUMO': ll, 'LUMO_ref': l_ref,
                     'p0_richardson': p0x, 'p0_ref': p0_ref}
        rep.check('validate_' + name, abs(E - E_ref) < 1e-10 * max(1, abs(E_ref)) and abs(hh - h_ref) < 1e-10 and abs(ll - l_ref) < 1e-10
                  and abs(p0x - p0_ref) < 1e-8 * max(1, abs(p0_ref)),
                  'reference state of the record reproduced by the independent free-basis Galerkin solver: E_KS %.13e (ref %.13e), HOMO %.2e, '
                  'LUMO %.2e off, integrated p0 %.10e (ref %.10e)' % (E, E_ref, hh - h_ref, ll - l_ref, p0x, p0_ref))
    return out


def job_spectrum(rep):
    f = fstar()
    c = Cell(f=f, L=L, H=H, m=M_PSI_OVER_H, nb=60, nq=600)
    st = KSState(c, dk=DK, N=8, lam=0.0, n2max=36, vol7=vol7(f)).scf()
    fL = f * L
    m = M_PSI_OVER_H
    from scipy.optimize import brentq
    podd = brentq(lambda p: math.sin(p * fL) * m + p * math.cos(p * fL), (0.5 * math.pi + 1e-12) / fL, (math.pi - 1e-12) / fL, xtol=1e-15)
    eps_dm = math.sqrt(m * m + podd * podd)
    eps_even = math.sqrt(m * m + (math.pi / fL) ** 2)
    # solver levels at k = 0
    k0 = {}
    for s in st.secs:
        if s['n2'] == 0:
            k0[(s['j'], s['parity'])] = s['eps'][s['nneg']:s['nneg'] + 3]
    ok = abs(k0[(1, 'odd')][0] - eps_dm) < 1e-12 and abs(k0[(1, 'even')][1] - eps_even) < 1e-12 and abs(k0[(1, 'even')][0]) < 1e-12
    rep.check('spectrum_exact_k0', ok, 'at k = 0: fold zero mode eps = 0, lowest odd (dark-matter) level eps = sqrt(m^2 + p^2), tan(p f L) = -p/m, '
              '= %.12f m, lowest even bulk level sqrt(m^2 + (pi/(f L))^2) = %.12f m (solver = exact to 1e-12)' % (eps_dm, eps_even))
    # fold band slope at the smallest shells
    slopes = []
    for s in st.secs:
        if s['parity'] == 'even' and s['j'] == 1 and 0 < s['n2'] <= 9:
            slopes.append(s['eps'][s['nneg']] / s['K'])
    rep.check('fold_band_massless', max(abs(x - 1) for x in slopes) < 1e-12,
              'the fold band eps = |k| exactly (physical momentum): massless 4D quanta (max deviation of eps/|k| from 1: %.1e)' % max(abs(x - 1) for x in slopes))
    # j-mirror symmetry and the 4 r3 degeneracy (structure)
    mir = max(abs(np.sort(s1['eps']) + np.sort(s2['eps'])[::-1]).max() for s1 in st.secs for s2 in st.secs
              if s1['n2'] == 0 and s2['n2'] == 0 and s1['parity'] == s2['parity'] and s1['j'] == 1 and s2['j'] == -1)
    rep.check('j_mirror_k0', mir < 1e-10, 'at k = 0 and v = 0 the spectrum of h_{-1} is minus that of h_{+1} (max deviation %.1e)' % mir)
    out = {'f': f, 'fL': fL, 'c_psi': fL * m, 'eps_dm': eps_dm, 'p_dm': podd, 'eps_even_bulk': eps_even,
           'levels_k0': {('%d_%s' % k): [float(x) for x in v] for k, v in k0.items()},
           'gap_3H_over_2f': 1.5 * H / f}
    # dark-matter level as a function of f (for the hidden-pressure identity)
    def edm(ff):
        fl = ff * L
        p = brentq(lambda pp: math.sin(pp * fl) * m + pp * math.cos(pp * fl), (0.5 * math.pi + 1e-12) / fl, (math.pi - 1e-12) / fl, xtol=1e-15)
        return math.sqrt(m * m + p * p)
    h = 1e-5
    out['dln_eps_dm_dln_f'] = (math.log(edm(f * (1 + h))) - math.log(edm(f * (1 - h)))) / (math.log(1 + h) - math.log(1 - h))
    out['x0_momentum_fraction_dm'] = podd ** 2 / eps_dm ** 2
    return out


def ground_states(f, nb, which, tags):
    res = {}
    N, n2max = {8: (8, 16), 592: (592, 64)}[which]
    lam_s = {8: 157.7, 592: 2.131}[which] * f ** 4          # the record's dimensionless coupling lambda/Vol7 (stress test)
    lams = {'0': 0.0, 'p': LAM_B, 'm': -LAM_B, 'S': lam_s}
    for tag in tags:
        lam = lams[tag]
        c = Cell(f=f, L=L, H=H, m=M_PSI_OVER_H, nb=nb, nq=10 * nb)
        st = KSState(c, dk=DK, N=N, lam=lam, n2max=n2max, vol7=vol7(f)).label_set().scf(tol=1e-13, mix=0.5)
        E, band, Eint = st.energy()
        hh, ll = st.homo_lumo()
        emt = st.emt()
        ends, eint_ends = st.endpoint_p0()
        ints = {k: st.integrate(v) for k, v in emt.items()}
        lhs = ends[0] - math.exp(-3 * H * L) * ends[1]
        rhs = 3 * H * float(np.sum(c.wq * np.exp(3 * H * c.y) * emt['pt']))
        dM, v = st.potentials()
        res[(N, tag)] = {'N': N, 'lambda': lam, 'E_KS': E, 'E_band': band, 'E_int': Eint, 'HOMO': hh, 'LUMO': ll,
                         'int_rho': ints['rho'], 'int_p3': ints['p3'], 'int_pt': ints['pt'], 'int_p0': ints['p0'],
                         'p0_fold': float(ends[0]), 'p0_tip': float(ends[1]), 'cons_residual': lhs - rhs,
                         'cons_scale': abs(rhs) + abs(ends[0]), 'max_abs_dM': float(np.max(np.abs(dM))),
                         'max_abs_v': float(np.max(np.abs(v))), 'iterations': st.iterations}
    return res


def richardson(x1, x2, p):
    """extrapolate x(nb) = x + C nb^-p from nb and 2 nb"""
    return x2 + (x2 - x1) / (2 ** p - 1)


def job_ground(rep, which):
    f = fstar()
    tags = ('0', 'p', 'm', 'S')
    r60 = ground_states(f, 60, which, tags)
    r120 = ground_states(f, 120, which, tags)
    orders = {}
    if which == 8:
        r240 = ground_states(f, 240, which, ('S',))
        a, b, c3 = r60[(8, 'S')], r120[(8, 'S')], r240[(8, 'S')]
        for q in ('E_KS', 'int_p0', 'cons_residual'):
            r = (a[q] - b[q]) / (b[q] - c3[q])
            orders[q] = math.log(abs(r)) / math.log(2)
    pE, pP = 4.0, 3.0                  # conservative orders (observed for the stress state: E about 4.9, p0 about 2.97)
    out = {}
    for key in r120:
        x1, x2 = r60[key], r120[key]
        d = dict(x2)
        d['nb'] = 120
        d['E_KS_richardson'] = richardson(x1['E_KS'], x2['E_KS'], pE)
        d['E_KS_uncertainty'] = abs(x2['E_KS'] - x1['E_KS']) / (2 ** pE - 1)
        d['int_p0_richardson'] = richardson(x1['int_p0'], x2['int_p0'], pP)
        d['int_p0_uncertainty'] = abs(x2['int_p0'] - x1['int_p0']) / (2 ** pP - 1)
        d['cons_residual_richardson'] = richardson(x1['cons_residual'], x2['cons_residual'], pP)
        out['N%d_lam%s' % key] = d
    out['observed_orders_stress_state'] = orders
    nbs = (60, 120)
    unc = max(v['E_KS_uncertainty'] / max(1, abs(v['E_KS'])) for k, v in out.items() if k.startswith('N'))
    rep.check('ground_basis_convergence', unc < 1e-8,
              'Richardson-estimated basis error of E_KS below %.1e (relative) at %d levels per sector; observed orders (N = 8, lambda > 0): '
              'E %.2f, int p0 %.2f, conservation residual %.2f' % (unc, nbs[-1], orders.get('E_KS', float('nan')),
                                                                      orders.get('int_p0', float('nan')), orders.get('cons_residual', float('nan'))))
    cons = max(abs(v['cons_residual_richardson']) / v['cons_scale'] for k, v in out.items() if k.startswith('N') and v['lambda'] != 0)
    rep.check('ground_y_conservation', cons < 1e-6,
              'nabla_M T^M_y = 0 integrated over the half cell, [e^{3Hy} p0]_{-L}^{0} = 3H int e^{3Hy} p_t dy, holds for every interacting '
              'self-consistent state: Richardson-extrapolated relative residual %.1e (the unextrapolated residual falls like nb^-3)' % cons)
    eint = max(abs(v['E_KS'] - v['int_rho']) / max(1, abs(v['E_KS'])) for k, v in out.items() if k.startswith('N'))
    rep.check('ground_energy_equals_integrated_rho', eint < 1e-10, 'E_KS = 2 Vol7 int e^{3Hy} rho dy (max relative deviation %.1e)' % eint)
    if which == 592:
        g0 = out['N592_lam0']
        w0 = g0['int_p3'] / g0['int_rho']
        out['w_free_gas'] = w0
        rep.check('fold_band_gas_radiation', abs(w0 - 1.0 / 3.0) < 1e-12,
                  'free N = 592 state (fold band only): w = int p3/int rho = %.15f = 1/3 (massless 4D radiation)' % w0)
    out['_meta'] = {'f': f, 'vol7': vol7(f), 'dk': DK, 'vt': VT, 'L': L, 'm': M_PSI_OVER_H}
    return out


def job_darkmatter(rep):
    f = fstar()
    out = {}
    for lam_tag, lam in [('0', 0.0), ('p', LAM_B)]:
        rr = []
        for nb in (60, 120):
            c = Cell(f=f, L=L, H=H, m=M_PSI_OVER_H, nb=nb, nq=10 * nb)
            base = KSState(c, dk=DK, N=8, lam=lam, n2max=16, vol7=vol7(f)).label_set().scf(tol=1e-13, mix=0.5)
            Eb = base.energy()[0]
            emtb = {k: base.integrate(v) for k, v in base.emt().items()}
            dm = KSState(c, dk=DK, N=16, lam=lam, n2max=16, vol7=vol7(f), fixed=fixed_dm(4)).scf(tol=1e-13, mix=0.5)
            Ed = dm.energy()[0]
            emtd = {k: dm.integrate(v) for k, v in dm.emt().items()}
            rr.append((Eb, Ed, emtb, emtd))
        Eb, Ed, emtb, emtd = rr[1]
        dE = Ed - Eb
        drho = emtd['rho'] - emtb['rho']
        dp3 = emtd['p3'] - emtb['p3']
        dp0_60 = rr[0][3]['p0'] - rr[0][2]['p0']
        dp0_120 = emtd['p0'] - emtb['p0']
        dp0 = dp0_120 + (dp0_120 - dp0_60) / 7.0
        dpt = emtd['pt'] - emtb['pt']
        out[lam_tag] = {'lambda': lam, 'E_ground': Eb, 'E_with_dm': Ed, 'dE': dE, 'drho': drho, 'w_dm': dp3 / drho,
                        'p0_over_rho': dp0 / drho, 'pt_over_rho': dpt / drho}
    sp = read_json(os.path.join(KSDIR, 'spectrum.json'))
    eps_dm = sp['eps_dm']
    rep.check('dm_energy_bookkeeping', abs(out['0']['dE'] - 8 * eps_dm) < 1e-9,
              'lambda = 0: 8 quanta in the lowest odd level add exactly 8 eps_DM = %.12f (computed %.12f)' % (8 * eps_dm, out['0']['dE']))
    rep.check('dm_cold', abs(out['0']['w_dm']) < 1e-12, 'k = 0 dark-matter quanta: w = p3/rho = %.1e (dust) at lambda = 0; %.2e with lambda' % (
        out['0']['w_dm'], out['p']['w_dm']))
    # hidden-pressure identity: the hidden pressure of a quantum is -dE/d ln(proper hidden length): p0/rho = -(1/1) d ln eps/d ln f
    pred = -sp['dln_eps_dm_dln_f']
    rep.check('dm_hidden_pressure_identity', abs(out['0']['p0_over_rho'] - pred) < 1e-6,
              'the Kohn-Sham stress tensor gives p0/rho = %.9f for the dark-matter quanta; the x0 eigenvalue gives -d ln eps_DM/d ln f = %.9f: '
              'two independent computations of the same x0 mass' % (out['0']['p0_over_rho'], pred))
    out['identity_prediction'] = pred
    return out


def sm_profile(cf, y):
    """Normalised proper-density shape of a Standard-Model zero mode with x0 localisation c_f: |chi|^2 = (2c/L) e^{2c y/L}/(1 - e^{-2c})."""
    return (2 * cf / L) * np.exp(2 * cf * y / L) / (1 - math.exp(-2 * cf))


def job_portals(rep):
    f = fstar()
    masses = read_json(os.path.join(OUT, 'masses.json'))
    ce = masses['fermions']['e']['c']
    cu = masses['fermions']['u']['c']
    out = {}
    nb = 80
    c = Cell(f=f, L=L, H=H, m=M_PSI_OVER_H, nb=nb, nq=10 * nb)
    y = c.y
    # portal mean-field shapes (the amplitude e carries the 8D coupling and the 4D density; shapes from the zero modes and P(y))
    # portal mean-field shapes (the amplitude e carries the 8D coefficient and the 4D density; the shapes are those of the
    # sources: SM zero-mode densities times P(y) ~ e^{-3Hy}, the flat gluon zero mode, a tip-localised Z charge)
    shapes = {
        'I11 vector contact, electron density (v)': ('v', sm_profile(ce, y) * np.exp(-3 * H * y)),
        'I11 vector contact, up-quark density (v)': ('v', sm_profile(cu, y) * np.exp(-3 * H * y)),
        'I12 gluon condensate <G G> (M, uniform)': ('M', np.ones_like(y)),
        'I9 chiral tip Z portal on Psi_A (a-component)': ('va', np.exp(-(y + L) / 0.02) / 0.02 / (1 - math.exp(-L / 0.02))),
    }
    for name, (kind, shp) in shapes.items():
        res = {}
        for e in (0.0, 1e-3, -1e-3):
            ext_M = e * shp if kind == 'M' else None
            ext_v = e * shp if kind == 'v' else None
            ext_va = e * shp if kind == 'va' else None
            st = KSState(c, dk=DK, N=16, lam=0.0, n2max=16, vol7=vol7(f), fixed=fixed_dm(4), ext_M=ext_M, ext_v=ext_v,
                         ext_va=ext_va).scf()
            edm = None
            efold = None
            for s in st.secs:
                if s['n2'] == 0 and s['parity'] == 'odd' and s['j'] == 1:
                    edm = float(s['eps'][s['nneg']])
                if s['n2'] == 1 and s['parity'] == 'even' and s['j'] == 1:
                    efold = float(s['eps'][s['nneg']])
                if s['n2'] == 0 and s['parity'] == 'even' and s['j'] == 1:
                    ezero = float(s['eps'][s['nneg']])
            res[e] = (edm, efold, ezero, st)
        d_dm = (res[1e-3][0] - res[-1e-3][0]) / 2e-3
        d_fold_gap = ((res[1e-3][1] - res[1e-3][2]) - (res[-1e-3][1] - res[-1e-3][2])) / 2e-3
        st0 = res[0.0][3]
        hf = None
        for si, s in enumerate(st0.secs):
            if s['n2'] == 0 and s['parity'] == 'odd' and s['j'] == 1:
                bs = c.basis[(1, 'odd')]
                coef = s['vec'][:, s['nneg']]
                a = coef @ bs['A']
                b = coef @ bs['B']
                if kind == 'v':
                    hf = float(np.sum(c.wq * shp * (a * a + b * b)))
                elif kind == 'va':
                    hf = float(np.sum(c.wq * shp * a * a))
                else:
                    hf = float(np.sum(c.wq * shp * 2 * a * b))      # j = +1: dM enters as j 2ab
        out[name] = {'d_eps_dm_de': d_dm, 'hellmann_feynman': hf, 'd_fold_gap_de': d_fold_gap}
        rep.check('portal_HF ' + name, abs(d_dm - hf) < 1e-6 * max(1, abs(hf)) and abs(d_fold_gap) < 1e-8,
                  'response of the lowest odd level d eps/de = %.9e equals the Hellmann-Feynman expectation %.9e; the fold-band gap at the '
                  'smallest shell changes by %.1e per unit e (the fold band stays massless)' % (d_dm, hf, d_fold_gap))
    # the scalar density of every Psi orbital vanishes at the regular tip (b(-L) = 0): tip scalar portals do not act on Psi
    Ae, Be = c.eval_at(1, 'odd', np.array([-L]))
    rep.check('scalar_density_vanishes_at_tip', float(np.max(np.abs(Be))) < 1e-12,
              'every Psi orbital has b(-L) = 0, hence Psibar Psi = s2 2ab = 0 at the tip: a tip operator built on Psibar Psi does not couple '
              'to dirac16complex; the a-component does not vanish there (the chiral tip Z portal I9 acts on the a-component of Psi_A)')
    out['_meta'] = {'c_e': ce, 'c_u': cu, 'nb': nb}
    return out


def job_feedback(rep):
    """Static response of the stabilised block to a hidden pressure: (3 H^2 - kappa d p0_b/dk) dk = kappa dp0 at k*."""
    bg = read_json(os.path.join(OUT, 'background.json'))
    ks = bg['casimir_type']['k_star_value']
    krho_b = bg['casimir_type']['kappa_rho_b_over_H2']
    stiff = 3.0 - 4.0 * krho_b / ks          # d/dk [3 H^2 k - kappa p0_b(k)], p0_b = rho_b ~ k^4 (units H = 1)
    gs = dict(read_json(os.path.join(KSDIR, 'ground8.json')))
    gs.update(read_json(os.path.join(KSDIR, 'ground592.json')))
    out = {'k_star': ks, 'stiffness_over_H2': stiff}
    # hidden pressure averaged over the 7-volume of the cell: p0_avg = int_p0 / (2 Vol7 int e^{3Hy} dy)
    f = fstar()
    w = 2 * vol7(f) * (1 - math.exp(-3 * H * L)) / (3 * H)
    for key in ('N8_lamp', 'N592_lamp', 'N592_lam0'):
        p0avg = gs[key]['int_p0_richardson'] / w
        out[key] = {'p0_avg': p0avg, 'dk_per_unit_kappa': p0avg / stiff}
    rep.check('block_response', stiff < 0, 'block stiffness d/dk[3H^2 k - kappa p0_b(k)] = %.6f H^2 < 0 at k*: a positive hidden pressure '
              'dp0 shifts the block by dk = kappa dp0/(%.4f H^2) < 0 (k decreases: the block scale f = k^{-1/2} grows slightly)' % (stiff, stiff))
    # x4 component: its k-derivative vanishes at k* (so the 4D Friedmann equation is unaffected at linear order)
    d4 = 6.0 * (1 - 4 * (1 / 32.0) * ks) + 4.0 * krho_b / ks
    rep.check('friedmann_decoupled_from_block_shift', abs(d4) < 1e-9,
              'd/dk [6 H^2 k (1 - 2 w2 k) + kappa rho_b(k)] = %.1e at k*: a small block shift does not change the 4D cosmological term '
              'at linear order' % d4)
    out['d_F4_dk'] = d4
    return out


def main():
    job = sys.argv[1]
    rep = Report('ks-checks-' + job, 'UM-2 Kohn-Sham job ' + job)
    t0 = time.time()
    fn = {'validate': job_validate, 'spectrum': job_spectrum, 'ground8': lambda r: job_ground(r, 8),
          'ground592': lambda r: job_ground(r, 592), 'darkmatter': job_darkmatter,
          'portals': job_portals, 'feedback': job_feedback}[job]
    out = fn(rep)
    out = {str(k): v for k, v in out.items()}
    out['runtime_s'] = round(time.time() - t0, 1)
    write_json(os.path.join(KSDIR, job + '.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
