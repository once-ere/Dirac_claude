"""Shared containers for the UM-2 version-4 registry (core.json) and inventory (equations.json)."""
import re

REG = {}
EQS = []


UNIT = re.compile(r'(GeV|eV|length|cm|m|K)\^(\(([^)]*)\)|-?\d+)')


def fmt_units(u):
    """Write powers of units as math: GeV^-6 -> $\\mathrm{GeV}^{-6}$, 1/length^(2p) -> 1/$\\mathrm{length}^{2p}$."""
    u = UNIT.sub(lambda m: r'$\mathrm{%s}^{%s}$' % (m.group(1), m.group(3) if m.group(3) is not None else m.group(2)), u)
    return u.replace('hbar = 1', r'$\hbar = 1$').replace('hbar = c = 1', r'$\hbar = c = 1$')


def R(key, tex, atoms, meaning, units='', value=None, status=None):
    """One registry entry: key -> {tex, atoms, meaning, units, value, status}."""
    if key in REG:
        raise SystemExit('duplicate registry key ' + key)
    e = {'tex': tex, 'atoms': list(atoms), 'meaning': ' '.join(meaning.split()), 'units': fmt_units(units)}
    if value:
        e['value'] = value
    if status:
        e['status'] = status
    REG[key] = e


def E(kind, title, latex, status, fields, solved, name=None):
    """One inventory entry; kind 'IN' (interaction term of the action) or 'FE' (field equation); the id and the tag are
    assigned by build.py in the order of the calls."""
    EQS.append({'kind': kind, 'title': title, 'latex': latex.strip('\n'), 'status': status, 'fields': fields,
                'solved_in': ' '.join(solved.split()), 'name': name})
