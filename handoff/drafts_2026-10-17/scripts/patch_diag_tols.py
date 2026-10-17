"""Diagnostic build only (scratchpad/w5diag, never committed): the canonical numerics of the Rust solver read the RK4
step count, the root tolerance and the SCF tolerance from KS_DIAG_G, KS_DIAG_ROOT_TOL and KS_DIAG_SCF_TOL (defaults =
the committed values)."""
import sys
from pathlib import Path

p = Path(sys.argv[1]) / "src" / "model.rs"
t = p.read_text(encoding="utf-8")
for a, b in (("            g: 900,\n", '            g: std::env::var("KS_DIAG_G").ok().and_then(|s| s.parse().ok()).unwrap_or(900),\n'),
             ("            root_tol: 1e-13,\n", '            root_tol: std::env::var("KS_DIAG_ROOT_TOL").ok().and_then(|s| s.parse().ok()).unwrap_or(1e-13),\n'),
             ("            scf_tol: 1e-11,\n", '            scf_tol: std::env::var("KS_DIAG_SCF_TOL").ok().and_then(|s| s.parse().ok()).unwrap_or(1e-11),\n')):
    assert t.count(a) == 1, a
    t = t.replace(a, b)
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
