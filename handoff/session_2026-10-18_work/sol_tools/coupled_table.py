#!/usr/bin/env python3
"""Write sol_parts/01_coupled.md: "The coupled system" of SOLUTION (version 4), with the tables of the interaction terms
(IN-n) and of the field equations (FE-n) of the inventory, their fields and the steps of the solution that solve or use them.
Usage: python3 coupled_table.py OUT.md"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import names as nm  # noqa: E402

REPO = Path('/home/claude/dirac_claude/universe_model_2')

# step assignment: internal name -> steps (the first is the step that solves it)
STEPS = {
    'el': '1 (order 0), 6 (order 1), 10', 'tmn_def': '1', 't_total': '1, 8', 't_stab': '1', 't_psi': '3', 't_f': '8',
    't_gauge': '8', 't_tip': '4 (part of the rest energies)', 't_portal': '8', 't_i12': '8', 'conservation': '1',
    'dirac16': '2 (spectrum), 3 (Kohn-Sham)', 'gomega': '1 (check), 3', 'dirac_Q': '2', 'dirac_uR': '2', 'dirac_dR': '2',
    'dirac_l': '2', 'dirac_eR': '2', 'dirac_nuR': '2', 'currents': '4', 'geff': '8', 'ym_gluon': '2 (massless gluons), 4',
    'ym_su2': '2 (masses), 4', 'ym_b': '2 (masses), 4', 'ym_lin': '2, 4', 'sigma_eq': '4', 'bc_boson': '2',
    'bc_psi': '2, 3', 'bc_sm': '2', 'bc_tip': '2', 'bg_metric': '1', 'bg_ychart': '1', 'sectional': '1', 'lov_pair': '1',
    'lov_E1': '1', 'lov_E2': '1', 'lov_E3': '1', 'bg_x4': '1', 'bg_x1': '1', 'bg_x0': '1', 'bg_cons': '1', 'static': '1',
    'stabiliser': '1', 'radion': '1, 10', 'response': '1', 'response_coeffs': '1', 'adiabatic': '1, 3, 8',
    'reduction': '1', 'einstein4': '1, 6', 'x0_boson': '2, 10', 'x0_boson_bc': '2, 10', 'x0_boson_eig': '2',
    'kk_tower': '2 (first level), 10', 'kk_potential': '10', 'wz_fit': '2', 'ferm_red': '2, 3', 'ferm_zero': '2',
    'ferm_k0': '2', 'ferm_1gen': '2', 'ferm_3gen': '2', 'pmns': '2, 5', 'psi_spectrum': '2', 'ks': '3, 8',
    'ks_mean': '3, 8', 'ks_dens': '3', 'ks_energy': '3', 'ks_tmn': '3', 'ks_id': '3', 'ks_bc': '3', 'contact4d': '8, 9',
    'i12dm': '3, 7, 8', 'levelshift': '3, 8', 'levelshift_env': '8', 'gluon_cond': '8', 'qcd_measure': '8',
    'vector_cond': '8', 'running': '8, 9 (couplings at $2M_{\\mathrm{DM}}$)', 'ew_cond': '8', 'dm_on_sm': '8', 'coupled_block': '8, 10',
    'pbar_hidden': '8', 'dlnalpha': '8', 'nucleon': '8', 'qcd_thresholds': '8', 'fermion_sens': '8', 'env': '8',
    'series': '10 (scheme)', 'newton8': '6, 10', 'newton4': '6', 'pert_einstein': '6', 'pert_dm': '6', 'pert_baryon': '6',
    'pert_photon': '6', 'pert_photon_hier': '6', 'pert_pol': '6', 'pert_nu': '6', 'pert_bg': '6', 'phi_rms': '6, 10',
    'sigma8': '6', 'nu_masses': '5', 'fourfermion': '5', 'gf': '4, 5', 'potentials': '5', 'flavour_ham': '5',
    'vacuum_prob': '5', 'msw': '5', 'pee': '5', 'adiabaticity': '5', 'thermal_pot': '5', 'qke': '5', 'decoupling': '5',
    'transfer': '5', 'qed_pressure': '5', 'qed_integrals': '5', 'neff': '5', 'ffi_eln': '5', 'ffi_disp': '5',
    'ffi_branches': '5', 'ffi_homog': '5', 'cnb': '5', 'idealgas': '9', 'dof': '9', 'crossover': '9', 'boltz': '9 (7)',
    'thermal_avg': '9 (7)', 'relic': '9 (7)', 'xsec': '7, 9', 'unitarity': '7, 9', 'freezein': '9', 'neff_fold': '9',
    'nuR_BL': '9', 'nuR_el': '9', 'deltaneff': '9, 4', 'nuR_I11': '9', 'selfint': '9', 'selfint_energy': '9',
}
IN_STEPS = {
    'The action of UM-2': 'written out above', 'Einstein-Lovelock gravity': '1', 'The Lovelock densities': '1',
    'The block stabiliser': '1', 'The dirac16complex field': '3', 'The Clifford algebra': '3, 4',
    'The canonical spin connection': '3', 'The gauge fields of SU(3)': '2, 4', 'The field strengths': '4',
    'The physical electroweak fields': '2, 4', 'The Standard-Model fermions': '2', 'The covariant derivative of a Standard': '4',
    'The tip sigma field': '2, 4', 'The covariant derivative of the sigma': '4', 'The tip mass term': '2, 4',
    'Portal I11': '3, 8, 9', 'Portal I12': '3, 7, 8, 9', 'Portal I13': '3, 8, 9',
}

TEXT_MATH = [(r'\bPsi_A\b', r'$\\Psi_A$'), (r'\bPsi_B\b', r'$\\Psi_B$'), (r'\bPsi\b', r'$\\Psi$'),
             (r'\bmetric g\b', r'metric $g_{MN}$'), (r'\bW\+', r'$W^+$'), (r'\bW-', r'$W^-$'), (r'\bnu_R\b', r'$\\nu_R$'),
             (r'\bu_R\b', r'$u_R$'), (r'\bd_R\b', r'$d_R$'), (r'\be_R\b', r'$e_R$'), (r'\bnu_1, nu_2, nu_3\b',
             r'$\\nu_1$, $\\nu_2$, $\\nu_3$'), (r'\bSigma\b', r'$\\Sigma$'), (r'\bW\^3\b', r'$W^3$'), (r'\bphoton A\b', 'photon'),
             (r'\bgluons G\b', 'gluons'), (r'\bSU\(2\) fields W\b', r'$SU(2)$ fields'), (r'\bhypercharge field B\b',
             'hypercharge field'), (r'\(a4, b4\)', r'($a_4$, $b_4$)'), (r'\bQ, ', r'$Q$, '), (r'\bl, ', r'$\\ell$, ')]


FIELD_MAP = {'W': '$SU(2)$ fields', 'B': 'hypercharge field', 'Z': '$Z$', 'sources with x0 profiles': 'sources with $x_0$ profiles',
             'metric g (block scale f)': 'metric $g_{MN}$ (block scale $f$)'}


def fields_text(fl):
    s = '; '.join(FIELD_MAP.get(x, x) for x in fl)
    for a, b in TEXT_MATH:
        s = re.sub(a, b, s)
    s = s.replace('$$', '')
    return s


def main():
    out = Path(sys.argv[1])
    inv = json.loads((REPO / 'docs_src' / 'equations.json').read_text(encoding='utf-8'))
    nmap, order = nm.mapping()
    id2name = {eid: name for eid, title, name in order if name}
    lines = []
    lines.append('# The coupled system')
    lines.append('')
    lines.append(
        'The fields of UM-2 are the metric $g_{MN}$ of Einstein-Lovelock gravity; the dirac16complex field $\\Psi$; the gauge '
        'fields of $SU(3)_c\\times SU(2)_L\\times U(1)_Y$ (gluons; $W^+$, $W^-$, $Z$ and the photon); the quarks and leptons of '
        'three generations (with the three left-handed neutrino flavours, the left-handed electrons, the singlet right-handed '
        'electrons and right-handed neutrinos); and the tip sigma field $\\Sigma$ (no Higgs particle). They are coupled: gravity to '
        'everything (the canonical spin connection for $\\Psi$ and the fermions, the metric in every kinetic term, the '
        'stabiliser); $\\Psi$ to gravity, to itself (the self-coupling $\\lambda$), to the fermion currents (I11), to the gauge-field '
        'invariants (I12) and, with its $x_0$-chiral current, to the baryon-number current (I13); the fermions to the gauge fields, '
        'to $\\Sigma$ at the tip (through the tip matrices, which carry the flavour mixing) and to $\\Psi$ (I11, and I13 for the '
        'quarks); the gauge fields to the fermions, to $\\Sigma$ at the tip and to $\\Psi$ (I12, a field-dependent coupling).')
    lines.append('')
    nin = sum(1 for q in inv if q['id'].startswith('IN'))
    nfe = sum(1 for q in inv if q['id'].startswith('FE'))
    lines.append('The action consists of %d interaction terms (IN-1 to IN-%d); varying it gives the %d field equations FE-1 to '
                 'FE-%d, which include their exact reductions on the static block and the equations of the four-dimensional '
                 'effective theory. Every one is written out, with its symbols, in the steps listed. The action is the sum of '
                 'the interaction terms:' % (nin, nin, nfe, nfe))
    lines.append('')
    lines.append('@@IN-1@@')
    lines.append('')
    lines.append('| term | interaction | fields | steps |')
    lines.append('|:---------|:--------------------------------|:---------------------------|:--------|')
    for q in inv:
        if not q['id'].startswith('IN'):
            continue
        st = 'all'
        for pre, v in IN_STEPS.items():
            if q['title'].startswith(pre):
                st = v
        lines.append('| %s | %s | %s | %s |' % (q['id'], q['title'], fields_text(q['fields']), st))
    lines.append('')
    lines.append('| equation | field equation | fields | solved (used) in step |')
    lines.append('|:---------|:--------------------------------|:---------------------------|:--------|')
    missing = []
    for q in inv:
        if not q['id'].startswith('FE'):
            continue
        name = id2name.get(q['id'])
        st = STEPS.get(name)
        if st is None:
            missing.append((q['id'], name, q['title']))
            st = '?'
        lines.append('| %s | %s | %s | %s |' % (q['id'], q['title'], fields_text(q['fields']), st))
    lines.append('')
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    for m in missing:
        print('NO STEP for', m)
    print('IN %d, FE %d' % (nin, nfe))


if __name__ == '__main__':
    main()
