"""Write the exact dirac16complex algebra fixture (standard library only).

Output (default):
    artifacts/dirac16complex/arbitrary-field/algebra-fixture.json

The document is produced deterministically: ``json.dumps(indent=2,
sort_keys=False, ensure_ascii=True) + "\\n"``, UTF-8, LF line endings.
Exact rationals are JSON integers or strings "p/q"; matrices are nested
row-major lists; every index is zero-based.
"""

import argparse
import os
import sys

try:
    from scripts import d16c_exact as X
except ModuleNotFoundError:  # executed as "python scripts/build_...py"
    import d16c_exact as X

REPOSITORY_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OUTPUT = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex",
                              "arbitrary-field", "algebra-fixture.json")
PRODUCER = "scripts/build_dirac16complex_fixture.py"

CONVENTIONS = {
    "eta": "diag(1,1,1,1,-1,-1,-1,-1); frame indices 0..3 positive norm, 4..7 negative norm; x4 is the evolution time",
    "gamma": "gamma^a = notebook T16^A[a] = [[0, taubar[a]], [tau[a], 0]] (split-octonion block basis), {gamma^a, gamma^b} = 2 eta^ab I16",
    "tau": "tau[0]=I8, tau[h]=[[0,s4[h]],[s4[h],0]], tau[7-h]=[[0,t4[h]],[-t4[h],0]] (h=1,2,3), tau[7]=tau[1]...tau[6]; s4/t4 = Qa -/+ Qb with Qa[h,p,q]=Signature[{h,p,q,4}], Qb=d_{p4}d_{qh}-d_{ph}d_{q4} (notebook 1-based h,p,q)",
    "taubar": "taubar[0]=I8, taubar[A]=sigma tau[A]^T sigma, sigma=[[0,I4],[I4,0]]",
    "C": "C = sigma16 = gamma^0 gamma^1 gamma^2 gamma^3 = blockdiag(-sigma, sigma); Psibar = Psi^dagger C",
    "chirality": "gamma^8 = gamma^0 gamma^1 ... gamma^7 = diag(-I8, +I8)",
    "S": "S^{ab} = (1/4)[gamma^a, gamma^b] for a < b (lexicographic)",
    "B": "B = -i C gamma^4, stored as real and imaginary integer parts",
    "K_clifford": "unique (up to scale) K with gammaHat^a K = K gamma^a, gammaHat = dirac-main tensor gammas (gp1..gp4, gm1..gm4); primitive integer, first nonzero entry in row-major order positive",
    "K_octonion": "unique (up to scale) K with gamma^a K = K Gamma^a (intertwiner from the octonion picture to the notebook picture), Gamma(e_a) = [[0, L_conj(e_a)], [L_e_a, 0]] (Zorn split octonions); primitive integer, first nonzero entry in row-major order positive",
    "rationals": "JSON integers or strings p/q",
}


def construct_objects():
    """Exact in-memory objects (Fraction matrices) that the fixture records."""
    tau = X.notebook_tau()
    taubar = X.notebook_taubar(tau)
    gammas = X.notebook_gammas()
    tensor = X.tensor_gammas()
    octonion = X.octonion_gammas()
    k_dimension, k_clifford = X.primitive_intertwiner(tensor, gammas)
    o_dimension, k_octonion = X.primitive_intertwiner(gammas, octonion)
    if k_dimension != 1 or o_dimension != 1:
        raise ArithmeticError("intertwiner spaces are not one-dimensional")
    b_real, b_imag = X.charge_form_b(gammas)
    return {
        "eta": X.eta(),
        "sigma8": X.sigma8(),
        "tau": tau,
        "taubar": taubar,
        "gamma": gammas,
        "C": X.charge_matrix(gammas),
        "chirality": X.chirality(gammas),
        "S": X.spin_generators(gammas),
        "B": (b_real, b_imag),
        "gammaClifford": tensor,
        "gammaOctonion": octonion,
        "K_clifford": k_clifford,
        "K_octonion": k_octonion,
    }


def fixture_document(objects=None):
    objects = construct_objects() if objects is None else objects
    m = X.matrix_to_json
    return {
        "schemaVersion": 1,
        "producer": PRODUCER,
        "indexing": "zero-based",
        "conventions": dict(CONVENTIONS),
        "eta": m(objects["eta"]),
        "sigma8": m(objects["sigma8"]),
        "tau": [m(matrix) for matrix in objects["tau"]],
        "taubar": [m(matrix) for matrix in objects["taubar"]],
        "gamma": [m(matrix) for matrix in objects["gamma"]],
        "C": m(objects["C"]),
        "chirality": m(objects["chirality"]),
        "S": [{"a": a, "b": b, "matrix": m(matrix)}
              for (a, b), matrix in objects["S"].items()],
        "B": {"real": m(objects["B"][0]), "imag": m(objects["B"][1])},
        "gammaClifford": [m(matrix) for matrix in objects["gammaClifford"]],
        "gammaOctonion": [m(matrix) for matrix in objects["gammaOctonion"]],
        "K_clifford": m(objects["K_clifford"]),
        "K_octonion": m(objects["K_octonion"]),
    }


def fixture_bytes(objects=None):
    return X.canonical_json_bytes(fixture_document(objects))


def write_fixture(path=DEFAULT_OUTPUT, objects=None):
    data = fixture_bytes(objects)
    directory = os.path.dirname(os.path.abspath(path))
    os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    return data


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    arguments = parser.parse_args(argv)
    data = write_fixture(arguments.output)
    print("output=%s" % os.path.abspath(arguments.output).replace("\\", "/"))
    print("output_bytes=%d" % len(data))
    print("output_sha256=%s" % X.sha256_bytes(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
