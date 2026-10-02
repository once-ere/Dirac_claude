"""Revision theory (sympy side): read Revision/algebra/gammas.json (and, when present,
Revision/algebra/reports/python-gammas.json) into exact sympy matrices."""

import json
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
REV = os.path.normpath(os.path.join(HERE, "..", ".."))
GAMMAS = os.path.join(REV, "algebra", "gammas.json")
PY_GAMMAS = os.path.join(REV, "algebra", "reports", "python-gammas.json")


def _num(x):
    return sp.Rational(x) if isinstance(x, str) else sp.Integer(x)


def _mat(rows):
    if isinstance(rows, dict):
        return _mat(rows["re"]) + sp.I * _mat(rows["im"])
    return sp.Matrix([[_num(x) for x in r] for r in rows])


def load(path=GAMMAS):
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    out = {"eta": [int(x) for x in d["eta"]], "gamma": [_mat(g) for g in d["gamma"]]}
    for k in ("C", "Gamma", "B"):
        if k in d:
            out[k] = _mat(d[k])
    if "S" in d:
        out["S"] = [[_mat(d["S"][a][b]) for b in range(8)] for a in range(8)]
    out["coordinates"] = d.get("coordinates")
    return out
