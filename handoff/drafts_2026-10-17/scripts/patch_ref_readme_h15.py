"""H15: the static texts of Revision/kohn_sham/reference/README.md (the SCF tolerance of every state, the sea-hole list,
the runs on the way).  The timings section is rewritten separately from the logs of the H15 rerun."""
from pathlib import Path

p = Path(r"D:\Developer\github\Dirac_claude\Revision\kohn_sham\reference\README.md")
t = p.read_text(encoding="utf-8")


def rep(a, b):
    global t
    assert t.count(a) == 1, (t.count(a), a[:80])
    t = t.replace(a, b)


rep('''  u from the six nearest half nodes. Anderson mixing of the potentials runs to max |residual| <= 1e-12 m.''',
    '''  u from the six nearest half nodes. Anderson mixing of the potentials runs to max |residual| <= 1e-14 m for every
  state (`ks_fd.SCF_TOL`; before 1e-12 m: the SCF stopping error enters E_band - E_int and p0 at first order, because
  they use the output densities with the levels of the input potential, and it is not part of the Richardson
  uncertainty, being nearly the same on the three grids; at 1e-12 m it reached 4e-11 in int_p0 of N = 2352,
  `claude_failures.md` H15).''')
rep('''  neighbours at a4 +- delta and +- 2 delta (delta = 2e-3), solved to the tighter SCF tolerance 1e-14 m (their energies
  enter the finite difference with weights of about 1.5/delta, so the canonical 1e-12 m would put a noise of ~1e-9
  into dE/da4, above the Richardson uncertainty of the strongest couplings; `claude_failures.md` H12, check
  `ground_a4_neighbours_tight`).''',
    '''  neighbours at a4 +- delta and +- 2 delta (delta = 2e-3), solved to the SCF tolerance 1e-14 m (their energies enter
  the finite difference with weights of about 1.5/delta, so the former tolerance 1e-12 m put a noise of ~1e-9 into
  dE/da4, above the Richardson uncertainty of the strongest couplings; `claude_failures.md` H12, check
  `ground_a4_neighbours_tight`).''')
rep('''  0.05} m. Each comes with four temperature neighbours and the sea-hole diagnostic.''',
    '''  0.05} m. Each comes with four temperature neighbours and the sea-hole diagnostic, evaluated over the shells of the
  thermal label set and max(5, 10% of them) more shells (before 5: the Rust thermal label sets, whose window rule
  differs, reached about 50 shells further at a4,0 = 2, where the fold band is dense; H15).''')
rep('''  the a4 neighbours at the SCF tolerance 1e-14 m (H12).''',
    '''  the a4 neighbours at the SCF tolerance 1e-14 m (H12) and, since H15, every state; the sea-hole list longer by
  max(5, 10%) shells (H15).''')
rep('''  was redone with the tighter neighbour tolerance; a stale docstring of `sea_brane_levels` (eps ~ -c kappa |k|) was
  corrected before the record run, which rebuilt the cache once more.''',
    '''  was redone with the tighter neighbour tolerance; a stale docstring of `sea_brane_levels` (eps ~ -c kappa |k|) was
  corrected before the record run, which rebuilt the cache once more; the cross-check of that record failed 3 of 31
  checks (H15: the SCF stopping errors of both solvers at the 1e-10 level in int_p0 and in the exact-Fock first-order
  difference, and the sea-hole coverage), so every state is now solved to 1e-14 m and the sea-hole list is longer; the
  record and both job caches were rebuilt.''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
