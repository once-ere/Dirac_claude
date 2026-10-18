"""UM-2 common utilities: paths, deterministic JSON output, check reports.

Every script of universe_model_2 writes its checks through `Report` so that every
verdict is recorded with its name, status and detail, and every output is
deterministic (sorted keys, LF line endings, fixed float formatting).
"""
import json
import os
import platform
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
UM2 = os.path.dirname(HERE)                      # universe_model_2/
ROOT = os.path.dirname(UM2)                      # repository root
OUT = os.path.join(UM2, 'outputs')
REP = os.path.join(UM2, 'reports')
FIG = os.path.join(UM2, 'figures')
for _d in (OUT, REP, FIG):
    os.makedirs(_d, exist_ok=True)


def fmt(v, n=12):
    """Deterministic float formatting (n significant digits)."""
    if isinstance(v, bool) or v is None:
        return v
    if isinstance(v, int):
        return v
    if isinstance(v, float):
        if v != v:
            return 'nan'
        if v in (float('inf'), float('-inf')):
            return 'inf' if v > 0 else '-inf'
        return float('%.*g' % (n, v))
    if isinstance(v, (list, tuple)):
        return [fmt(x, n) for x in v]
    if isinstance(v, dict):
        return {str(k): fmt(x, n) for k, x in v.items()}
    try:
        import numpy as np
        if isinstance(v, np.generic):
            return fmt(v.item(), n)
        if isinstance(v, np.ndarray):
            return fmt(v.tolist(), n)
    except ImportError:
        pass
    return v


def write_json(path, obj, n=12):
    with open(path, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(fmt(obj, n), fh, indent=1, sort_keys=True, ensure_ascii=False)
        fh.write('\n')


def read_json(path):
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


class Report:
    """Collects named checks; writes reports/<name>.json; prints a summary."""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.checks = []
        self.t0 = time.time()

    def check(self, name, passed, detail=''):
        passed = bool(passed)
        self.checks.append({'name': name, 'passed': passed, 'detail': detail})
        print(('PASS ' if passed else 'FAIL ') + name + (': ' + str(detail) if detail else ''))
        sys.stdout.flush()
        return passed

    def write(self, extra=None):
        failed = [c['name'] for c in self.checks if not c['passed']]
        obj = {
            'report': self.name,
            'description': self.description,
            'check_count': len(self.checks),
            'failed_check_count': len(failed),
            'failed': failed,
            'checks': self.checks,
            'environment': {'python': platform.python_version()},
        }
        if extra:
            obj.update(extra)
        write_json(os.path.join(REP, self.name + '.json'), obj)
        print('%s: %d checks, %d failed (%.1f s)' % (self.name, len(self.checks), len(failed),
                                                     time.time() - self.t0))
        return len(failed) == 0
