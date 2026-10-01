# Revision Kohn-Sham reference solver (Python, independent of the Rust solver)

An independent second solver for SPEC section 7 (instantaneous Kohn-Sham states of dirac16complex in the
author's primordial field). It shares no code with the Rust solver (`Revision/kohn_sham/solver`) and uses a
different discretisation. Its only theory input is `Revision/kohn_sham/ks-theory.json`; the functional
coefficients are read from it and checked to be exactly 15/16, -1/16, 15/32 and -1/32. Nothing from the old
stages is used.

Coordinates as the author names them: x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time;
x5, x6, x7 = the three EXTRA TIMES, which DEFLATE EXPONENTIALLY (scale factor e^{-a4} sin^{1/6} z, a4
increasing); x8 = hidden direction, y = ln(sin z)/(6H) in [-L, 0] (brane y = 0, tip cutoff y = -L).

## Run (from the repository root)

```
python Revision/kohn_sham/reference/run_reference.py --timing <scratch>/timing.json            # canonical
python Revision/kohn_sham/reference/run_reference.py --out <scratch>/repeat --report <scratch>/repeat.json   # repeat
```

The run writes `reference/results/` and `reports/ks-reference.json`, and prints every check as
`PASS/FAIL - name: detail` on stderr and `SUCCESS`/`FAILURE` last on stdout (exit 0/1). `--jobs N` (default
min(20, cores - 2)) distributes independent states over processes and does not change any output. The
outputs are deterministic (LF, no timings or paths). The cross-check against Rust is in `../checker/`.

## Method

* **Block equation.** ks-theory.json gives, for chi = (a, i b), the real symmetric operator
  `[[jK + v, j(d_y + M)], [j(-d_y + M), -jK + v]]` on (a, b), with K = e^{-Hy - a4,0} |k|, a regular tip
  b(-L) = 0 (theta = 0), and the ASSUMED Z2 brane: even b(0) = 0, odd a(0) = 0.
* **Rotated frame (exact).** chi = e^{i phi sigma1} psi, psi = (u, i w), turns both parities into the same
  Dirichlet problem w(-L) = w(0) = 0: phi = 0 (even) and phi = j (pi/2)(y + L)/L (odd). The transformed
  operator has the same form, with mass M cos 2phi - K sin 2phi, momentum term M sin 2phi + K cos 2phi and a
  scalar phi'. The choice phi_j = j phi keeps the exact k = 0 symmetry j -> -j as the sign flip w -> -w of the
  discrete problem, so the k = 0 levels of the two block types stay exactly degenerate on every grid.
* **Staggered finite differences.** G cells of width h = L/G; u lives on the half nodes and w on the interior
  nodes. The unknowns (u_1/2, w_1, ..., u_G-1/2) give a real symmetric tridiagonal matrix of size 2G - 1.
  Centred differences and centred averages give second order with an error expansion in even powers of h.
  The staggering avoids the doubling of naive centred Dirac discretisations.
* **Eigenvalues.** Sturm counts and bisection find each level by its index in its sector, so no level can be
  missed. The twisted factorisation then refines the level (Rayleigh-quotient steps) and gives the
  eigenvector. Every level is verified by two Sturm counts. The particle convention of ks-theory.json
  (positive lambda = 0 levels plus the k = 0 brane zero modes, which are exact zero eigenvalues of the
  discrete problem) fixes the lowest particle index of each sector. A level's rank (its index minus that
  offset) equals the Rust label minus label_min.
* **Densities, potentials, integrals.** u and w are averaged onto each other's positions. The proper
  densities n, S, Q, the potentials M_eff = m + (15/16) lambda S and v_v = -(1/16) lambda n, e_int and the EMT
  (rho, p3, p_t, p8 as in ks-theory.json emt) are evaluated at all positions. Integrals use the midpoint rule
  on the half nodes. Brane and tip values use a quintic extrapolation of u from the six nearest half nodes.
  Anderson mixing of the potentials runs to max |residual| <= 1e-12 m.
* **Runs per state.** Each state gets the ground state (aufbau, closed shells), the Delta-SCF state (one
  particle from the HOMO group to the LUMO group, uniform over each group), and the four fixed-occupation
  neighbours at a4 +- delta and +- 2 delta (delta = 2e-3). The neighbours give dE/da4 and the self-consistent
  d_a M_eff and d_a v_v, which enter the exact discrete Hellmann-Feynman matrix elements z_n^T (dT/da4) z_m of
  the adiabaticity measure Q_nm = A H |<n| d_a h |m>| / (eps_n - eps_m)^2 (n occupied, m empty, same sector,
  rank <= 2). Thermal states use the Mermin occupations at T and four neighbours at T(1 +- 0.01),
  T(1 +- 0.02) for C_V = T dS/dT, dE/dT and -dF/dT.
* **Label sets.** The label set comes from the free (lambda = 0) problem at the same slice on the coarsest
  grid. At T = 0 it holds every particle level below max(E_F, LUMO) + 0.25 + 2 sigma, plus ranks 0..2 of every
  sector of an occupied shell. At T > 0 it holds every particle level below mu + T ln(1e13) + 0.2 + 2 sigma.
  Completeness is checked after self-consistency: the lowest excluded level, including the next five shells,
  must lie above the LUMO, or carry an occupation below 2e-13.
* **Richardson extrapolation and uncertainty.** Every quantity is computed on G = 300, 600 and 1200 and
  reported as R = (64 x(1200) - 20 x(600) + x(300))/45, which removes the h^2 and h^4 terms. Its measured
  grid uncertainty is U = |R - (4 x(1200) - x(600))/3| + 2e-12 max(1, |R|): the size of the h^4 term on the
  finest grid, plus a roundoff floor. The report checks the asymptotic ratio
  (x(300) - x(600))/(x(600) - x(1200)) = 4. One state is also solved on G = 2400 to confirm that the
  three-grid value moves by less than U.
* **Re-derived inputs.** N_large and N_mid are re-derived from the free a4,0 = 0 closed shells below the
  bulk edge. lambda_1 and lambda_2 are re-derived as 0.1 m and 0.3 m divided by the coupling strength, rounded
  to 4 significant digits. The strength is max over slices and y of max((15/16)|S|, |n|/16) of the free
  ground states. The reference takes the continuous maximum (quartic interpolation over the nodes), whereas
  the Rust value is a maximum over grid samples; the checker accounts for the difference.
