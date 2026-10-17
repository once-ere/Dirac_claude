# Tip-cutoff convergence of the Revision Kohn-Sham record

The Kohn-Sham record (`Revision/kohn_sham/`) replaces the tip $z \to 0$ ($y \to -\infty$) of the author's hidden
coordinate $y = \ln|\sin z|/(6H)$ by a CHOSEN regular-tip condition $b(-L) = 0$ ($\theta = 0$) at the cutoff
$y = -L$, $L = 3$. This folder measures how the recorded results depend on $L$ and whether they converge as $L$
grows ($L = 3, 3.5, \dots, 6$). The author's coordinates {x0, ..., x7}: x0 = the hidden direction
($z = 6Hx_0$ real), x1..x3 = 3-space (scale factor $e^{a_4}$), x4 = time, x5..x7 = the three extra times, which DEFLATE
EXPONENTIALLY (scale factor $e^{-a_4} b_4^{1/2}(\sin^2 z)^{1/12}$); p0 = $T^{x_0}{}_{x_0}$ is the hidden-direction
pressure. The record is that of the corrected primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md` section 1)
on the history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$: the hidden direction carries the scale $f = e^{-a_4} b_4^{1/2}$
($= e^{-a_4/3}$ on the history), the momentum weight $\kappa = e^{-a_4}$ is CONSTANT in $y$, the densities carry
$P = e^{-3Hy}/\mathrm{Vol}_7$, $\mathrm{Vol}_7(a_{4,0}) = \ell^3 v_t e^{(5/3)a_{4,0}}$ (solver README, "The corrected
metric"). Units $m = H = 1$, $\Delta k = 0.25$. This study was rewritten and rerun for that record on 2026-10-17
(section 9).

## Answer in brief

* **The free states are exact fold-band gases and do not depend on $L$** (except $N = 2352$ at $a_{4,0} = 0$). With
  $\kappa$ constant in $y$ every occupied orbital is the fold-band orbital $(e^{fmy}, 0)$ with $\varepsilon = \kappa|k|$
  at every $L$: $E_{KS}$, HOMO, LUMO and the KS gap of every free state with $N = 8$ and $592$ (all slices) and of
  $N = 2352$ at $a_{4,0} = 1, 2$ are the same at every $L$ to rounding (largest relative change $1.4\times10^{-17}$,
  both step sizes). The former double-exponential
  tip suppression of the metric of 2026-10-14 is gone. Only the values at the fold depend on $L$, through the
  normalisation of the fold-band orbital: $\rho(0; L) = \rho(0; \infty)/(1 - e^{-2fmL})$ exactly (to $1.4\times10^{-14}$);
  the recorded $L = 3$ fold values are high by 0.25%, 1.38% and 4.8% at $a_{4,0} = 0, 1, 2$.
* **The $k = 0$ bulk levels converge only algebraically**, like the levels of a box of proper length $fL$:
  $\varepsilon - m \approx (l\pi)^2/(2m(fL)^2)$ (exact law, verified to $1.4\times10^{-10}$ m). The bulk edge 1.2923 that
  defines $N_{large} = 2352$ is an $L = 3$ value (1.0977 at $L = 6$, $m$ as $L \to \infty$). The free $N = 2352$,
  $a_{4,0} = 0$ ground state changes its occupied set from $L = 3.5$ on (the KS gap 0.01754 closes) and its energy does
  NOT converge up to $L = 6$ (2288.388 at $L = 3$, 2245.486 at $L = 6$).
* **The interacting zero modes depend on $L$, the more the later the slice.** Their density per proper volume grows
  toward the tip like $e^{(3H - 2fm)|y|}$ (verified in the free runs at $a_{4,0} = 0, 1, 2$), so the first-order
  interaction energy $\propto \int e^{(4fm - 3H)y}dy$ is finite as $L \to \infty$ only for $f > 3H/(4m) = 3/4$, i.e.
  $a_{4,0} < 3\ln(4/3) = 0.863$ on the history. At $a_{4,0} = 0$ first order holds at every $L$ (the solved $E_{KS}$ is
  0.996 to 0.976 of it) and the recorded $E_{KS}$ of $N = 8$, $\mp 3.7787\times10^{-2}$, is 2.3% below the large-$L$
  value $\mp 3.8688\times10^{-2}$. At $a_{4,0} = 1$ and 2 the first-order energy grows like $e^{0.134L}$ and
  $e^{0.946L}$; the self-consistent solution saturates and converges, but the recorded values are 67% and 22% of the
  large-$L$ values for $N = 8$ ($\mp 1.4571\times10^{-2}$ against $\mp 2.1622\times10^{-2}$, $\mp 6.980\times10^{-3}$
  against $\mp 3.239\times10^{-2}$), and the interaction shifts $E_{KS}(\pm\lambda_1) - E_{KS}(0)$ of $N = 592$ and
  $2352$ at $a_{4,0} = 2$ are 4.6 to 4.7 times smaller at $L = 3$ than at large $L$. 17 of the 19 interacting states
  converge at every $L$ (geometric tails); the SCF iteration fails only for $N = 2352$ at $a_{4,0} = 0$ (from
  $L = 3.5$ for $+\lambda_1$, from $L = 4.5$ for $-\lambda_1$), where $k = 0$ bulk levels are occupied.
* **The recorded calibration rule has no non-trivial limit:** applied at each $L$ it gives $\lambda_1(L)$ falling like
  $e^{-1.97L}$ for $N = 8$ and $592$ (the rate $3H - 2fm$ of the zero-mode density at $a_{4,0} = 2$ is 1.973) and about
  like $e^{-2.9L}$ for $N = 2352$; the interaction switches off as $L \to \infty$ (section 4.4).

## 1. How the solver gets L (and how L is varied without changing it)

* `results/parameters.json` is an OUTPUT of the solver. The solver does not read it; `--root` only locates
  `ks-theory.json`, `gammas.json` and the 40-digit Mermin fixture. $L = 3$ is the literal `l: 3.0` in `base_phys()`
  (`solver/src/runs.rs`), and the RK4 step count $G = 900$ the literal `g: 900` in `Numerics::canonical()`
  (`solver/src/model.rs`). A scratch root with a modified `parameters.json` is therefore ignored.
* The committed source is NOT changed. `tip_convergence.py` copies the crate into the work directory and applies
  two one-line patches (each must match exactly once): `l` and `g` are read from the environment variables
  `KS_TIP_L` and `KS_RK4_STEPS`, with the defaults 3 and 900. The SHA-256 of every committed source file and of
  the two patched files are recorded in `tip-convergence.json` (`committedSolverSourceSha256`, `patches`).
* **Controls (byte for byte).** With `KS_TIP_L=3 KS_RK4_STEPS=900` the patched copy and the committed binary run the
  quick matrix (`all --quick`: every code path of the canonical matrix: ground states with their neighbours,
  Delta-SCF, rescaling partners, exact-Fock variants, thermal states, history, T3 self-test) and write byte-identical
  outputs and reports (the full matrix takes about 285 s and no longer fits into one time-limited step; it is computed
  in parts by the gate). Every `single` run of this study at $L = 3$ is byte-identical (JSON and profile) between the
  committed binary and the patched copy, and equals the committed matrix (`ground/summary.csv`,
  `ground/emt-integrals.csv`, `thermo/thermodynamics.csv`) within $10^{-12}\max(1, |x|)$. This run: 74 of 74
  quick-matrix files identical, 30 of 30 singles identical, 357 comparisons with the committed matrix (340
  bit-identical, worst $2.3\times10^{-16}$ relative).
* **Step size.** $G = 300L$, i.e. the step $h = L/G = 1/300$ of the record is kept (the solver's own analytic
  test at $L = 2$ scales $G$ the same way, `spectrum.rs`). Every run is repeated with $G = 600L$; the $h$-error is
  $U_h = (16/15)|x(600L) - x(300L)|$ (RK4, order 4). The largest $U_h$ of the study is $7.8\times10^{-11}\max(1, |x|)$
  (int_p0 of the recalibrated N2352_lamp1_a20 at $L = 5$): the step limits no result.

## 2. What was computed

* **States** (canonical labels of the record): $N \in \{8, N_{mid}, N_{large}\} = \{8, 592, 2352\}$,
  $\lambda \in \{0, +\lambda_1, -\lambda_1\}$, $a_{4,0} \in \{0, 1, 2\}$ (27 ground states, aufbau, label-set margin
  $0.25 + 2\sigma$ as in the matrix), the thermal states N592_lam0_a20_T50 ($T = 0.05$) and N592_lamp1_a10_T20
  ($T = 0.02$; margin $0.2 + 2\sigma$), and a free $N = 8$, $a_{4,0} = 0$ run with margin 1.2 for the $k = 0$ spectrum.
  $L \in \{3, 3.5, 4, 4.5, 5, 5.5, 6\}$, each with $G = 300L$ and $600L$.
* **Coupling protocols.** FIXED: the recorded constants $\lambda_1$ = 157.7 ($N = 8$), 2.131 ($N = 592$), 0.5363
  ($N = 2352$) ("lambda is a constant of the theory"). RECALIBRATED: the record's calibration rule (0.1 m divided by
  the largest first-order mean-field potential per unit $\hat\lambda$ of the free ground states over the five slices,
  4 digits) applied at each $L$ (18 states $\pm\lambda_1(L)$).
* **Quantities.** $E_{KS}$, $E_{int}$, HOMO, LUMO, KS gap, the zero-mode level, the EMT integrals
  $2\mathrm{Vol}_7\int e^{3Hy}(\rho, p_3, p_t, p_0, n)\,dy$, the fold values $\rho, p_3, p_t, p_0, n$ at $y = 0$ (CSV names
  `*_brane`, kept from the earlier records); thermal: $E$, $\mu$, $S$; diagnostics: $n(-L)$, $\max|v_v|$,
  $\max|M_{eff} - m|$, iterations, residual.
* **Independent check.** The reference solver (`reference/ks_fd.py`, staggered finite differences, Richardson over
  three grids $G = 300, 600, 1200$ scaled by $L/3$) at $L = 3$ and $L = 4$ for N8_lamp1_a00 and N592_lam0_a20.

## 3. Analysis rules (fixed before the comparison; one revision, see History)

* Successive differences $d_i = x(L_{i+1}) - x(L_i)$ over the contiguous range of $L$ from 3 at which the SCF
  converged; $d_i$ is *resolved* if $|d_i| > \nu(L_i) + \nu(L_{i+1})$, $\nu = U_h + 10^{-11}\max(1, |x|)$.
* *Converged within the noise from $L_c$*: all differences from $L_c$ on are unresolved; $x_\infty = x(L_{max})$,
  $U = |d_{last}| + \nu$.
* *Converging (geometric tail)*: the last two ratios $d_{i+1}/d_i$ both lie in $(0, 0.5)$; $x_\infty = x(L_{max}) +
  d_{last}\,r/(1 - r)$ with the last ratio $r$, $U = |\text{tail}| + \nu$ (for decreasing ratios the true tail lies
  between 0 and the geometric tail). An algebraic tail $d \sim L^{-p}$ has ratios $(L/(L + 0.5))^p > 0.5$ for
  $p < 8$ at $L \ge 5$ and is rejected.
* Otherwise NOT CONVERGED (no extrapolation); with fewer than 3 converged $L$ values NOT ESTABLISHED.
* *Exponential vs double exponential* (at least 3 resolved differences): least-squares fits of $\ln|d|$ linear in
  $L$ and linear in $e^L$, with the maximum log residual; "consistent with exponential" if the exponential fit has
  max residual $\le \ln 2$ and all $|r| < 1$; "faster than exponential" if all ratios are positive and decrease and
  the exponential fit is rejected.

## 4. Results

### 4.1 Exact L dependence (theory, verified)

* $k = 0$, $a_{4,0} = 0$ ($f = 1$), constant $M = m$, $v = 0$, $\theta = 0$: even $\varepsilon = 0$ (zero mode
  $\chi = (e^{fmy}, 0)$) and $\pm\sqrt{m^2 + (l\pi/(fL))^2}$; odd $\pm\sqrt{m^2 + p^2}$, $\tan(pfL) = -p/m$. All 84
  $k = 0$ levels of the scan agree to $1.42\times10^{-10}$ m. Every nonzero level tends to $\pm m$ like
  $(l\pi)^2/(2m(fL)^2)$: algebraic. Bulk edge (odd, $l = 0$): 1.2923 (L = 3), 1.2319 (3.5), 1.1887 (4), 1.1566 (4.5),
  1.1321 (5), 1.1130 (5.5), 1.0977 (6).
* Zero-mode density per proper volume ($N = 8$, free): $n(0) = 8/(\mathrm{Vol}_7(1 - e^{-2mL}))$, converging
  exponentially to $8/\mathrm{Vol}_7 = 5.0393\times10^{-4}$, and $n(-L) = n(0)\,e^{(3H - 2m)L} = n(0)\,e^{L}$, diverging;
  both verified to $1.1\times10^{-11}$ at every $L$ (check `zero_mode_density_exact`). At the later slices the free
  runs give $n(-L)/n(0) = e^{(3H - 2fm)L}$ with $f = e^{-a_{4,0}/3}$ (rates 1.567 and 1.973 at $a_{4,0} = 1, 2$; at
  $L = 6$: 403, $1.21\times10^4$, $1.39\times10^5$ at $a_{4,0} = 0, 1, 2$).
* Fold values of the free fold-band gas: the orbital $(e^{fmy}, 0)$ normalised on $[-L, 0]$ gives
  $\rho(0; L) = \rho(0; \infty)/(1 - e^{-2fmL})$; the free states N592_lam0 and N2352_lam0 ($a_{4,0} = 1, 2$; N592
  also at 0) follow it to $1.4\times10^{-14}$. The convergence is exponential with the rate $2fm$ = 2, 1.433, 1.027
  at $a_{4,0} = 0, 1, 2$ (ratios $e^{-fm}$ = 0.368, 0.488, 0.598 per step 0.5).
* First-order interaction energy of the 8 zero modes ($S = 0$ by the $j = \pm1$ cancellation), $a_{4,0} = 0$:
  $E^{(1)}_{int} = -(4\lambda m^2/\mathrm{Vol}_7)(1 - e^{-(4m - 3H)L})/((4m - 3H)(1 - e^{-2mL})^2) =
  -(4\lambda/\mathrm{Vol}_7)(1 - e^{-L})/(1 - e^{-2L})^2$ for $m = H = 1$, finite as $L \to \infty$
  ($-4\lambda/\mathrm{Vol}_7 = -0.039735$ for $\lambda_1 = 157.7$); tip potential $|v_v(-L)| = (\lambda/16)\,n(-L) \propto
  e^{L}$: 0.1000 m at $L = 3$ (the calibration), 0.2713 at 4, 0.7372 at 5, 2.004 at 6. The solved
  $E_{KS}/E^{(1)}_{int}$ is 0.9958, 0.9922, 0.9877, 0.9833, 0.9799, 0.9775, 0.9760 at $L = 3, \dots, 6$, and the
  self-consistent $\max|v_v|$ grows from 0.093 m to 0.280 m. With the hidden scale the integrand is
  $e^{(4fm - 3H)y}$: at $a_{4,0} = 1$ and 2 ($f = 0.7165$, 0.5134) the first-order energy grows like $e^{0.134L}$ and
  $e^{0.946L}$ (from the verified profile; not a separate check).

### 4.2 Free states ($\lambda = 0$)

$x(3)$ is the recorded value, $x_\infty$ the extrapolated or limiting value with uncertainty $U$.

| state | quantity | x(3) | x_inf | U | status |
| --- | --- | --- | --- | --- | --- |
| N8, all slices | E_KS, HOMO | 0 | 0 | 1e-11 | exact zero modes |
| N8_lam0_a00 / a10 / a20 | KS gap = LUMO | 0.25 / 0.09196986 / 0.03383382 | the same | 1e-11 | L-independent: $\kappa\Delta k = 0.25e^{-a_{4,0}}$ |
| N592_lam0_a00 | E_KS, HOMO, LUMO | 361.1161438, 0.7905694, 0.8291562 | the same | 4e-9, 1e-11 | L-independent ($0.25\sqrt{10}$, $0.25\sqrt{11}$) |
| N592_lam0_a10 / a20 | E_KS | 132.8472 / 48.87176 | the same | 1e-9 / 5e-10 | L-independent |
| N2352_lam0_a10 / a20 | E_KS | 841.851 / 309.6997 | the same | 8e-9 / 3e-9 | L-independent |
| N592_lam0_a00 / a10 / a20 | rho at the fold | 0.02280369 / 0.001148106 / 5.909939e-5 | 0.02274717 / 0.001132515 / 5.6385e-5 (exact law) | 1.4e-7 / 2.1e-7 / - | geometric / geometric / NOT CONVERGED by the rule (ratio 0.596 > 0.5; the exact law holds) |
| N2352_lam0_a00 | E_KS | 2288.388233 | - | - | NOT CONVERGED (2245.485568 at L = 6; ratios 5.3, 1.37, 1.09, 0.948, 0.908) |
| N2352_lam0_a00 | KS gap | 0.01753795 | 0 from L = 3.5 | - | occupied set changes: open shell |
| N592_lam0_a20_T50 | E / mu / S | 96.58454649 / 0.0395948113 / 2112.110999 | - | - | NOT CONVERGED by the rule: changes of 1.2e-8 / 2.5e-9 / 1.2e-8 relative up to L = 6 that grow with L |

N2352_lam0_a00 in detail: at $L = 3$ the last filled level is the fold-band shell $|k| = 0.25\sqrt{26}$
($\varepsilon = 1.2747549$) and the LUMO is the bulk edge 1.2922928. From $L = 3.5$ the bulk edge (1.2319) lies below
that shell: the aufbau fills $k = 0$ bulk levels and the shell is open (HOMO = LUMO = 1.2747549 at $L = 3.5$ and 4);
at $L = 4.5$ and 5 the HOMO is a $k = 0$ bulk level (1.2600514, 1.2376094), from $L = 5.5$ the shell $0.25\sqrt{24}$
(1.2247449). $E_{KS}$: 2288.388, 2287.193, 2280.848, 2272.131, 2262.645, 2253.651, 2245.486. As $L \to \infty$ every
bulk level tends to $m = 1$, below the upper fold-band shells, so the large-$L$ ground state of $N = 2352$ at
$a_{4,0} = 0$ is a different state; its limit is not established. At $a_{4,0} = 1, 2$ the fold band is redshifted
($\varepsilon = e^{-a_{4,0}}|k|$, Fermi level 0.469 and 0.173) far below the bulk edge, and nothing depends on $L$
except the fold values.

The thermal state N592_lam0_a20_T50 is a fold-band gas as well; its small $L$ dependence (successive differences
growing by about 2 per step) is consistent with the thermal occupation, about $e^{-(m - \mu)/T} = e^{-19}$, of the
$k = 0$ bulk levels, whose number below a fixed energy grows with $L$ (not tested separately). Its fold values follow
the exact law above.

### 4.3 Interacting states with the recorded couplings (FIXED protocol)

| state | quantity | x(3) | x_inf (U) or last value | status |
| --- | --- | --- | --- | --- |
| N8_lamp1_a00 / lamm1_a00 | E_KS | $\mp$3.778668292e-2 | $\mp$3.8687933e-2 (6.6e-7) | geometric tail; x(3) = 0.977 x_inf |
| N8_lamp1_a00 / lamm1_a00 | HOMO (zero-mode level) | $\mp$9.410183271e-3 | $\mp$9.5624889e-3 (4.0e-9) | geometric tail |
| N8_lamp1_a00 / lamm1_a00 | int_p0 | $\mp$8.860537549e-2 | $\mp$9.776237e-2 (2.6e-6) | geometric tail |
| N8_lamp1_a10 / lamm1_a10 | E_KS | $\mp$1.457144423e-2 | $\mp$2.162235e-2 (1.3e-5) | geometric tail; x(3) = 0.674 x_inf |
| N8_lamp1_a20 / lamm1_a20 | E_KS | $\mp$6.979530633e-3 | $\mp$3.239442e-2 (2.1e-4) | geometric tail; x(3) = 0.215 x_inf |
| N8_lamp1_a20 / lamm1_a20 | int_p0 | $\mp$2.559878524e-2 | $\mp$1.652668e-1 (3.2e-4) | geometric tail; x(3) = 0.155 x_inf |
| N592_lamp1_a00 / lamm1_a00 | E_KS | 358.3010464 / 363.8955078 | 358.218078 (6.0e-5) / 363.950623 (4.0e-5) | geometric tail |
| N592_lamp1_a10 / lamm1_a10 | E_KS | 131.765178 / 133.9217556 | 131.214808 (1.0e-3) / 134.417476 (9.5e-4) | geometric tail |
| N592_lamp1_a20 / lamm1_a20 | E_KS | 48.35502444 / 49.3879563 | 46.446869 (0.016) / 51.241910 (0.016) | geometric tail |
| N2352_lamp1_a00 | E_KS | 2277.155326 | - | NOT ESTABLISHED (SCF fails from L = 3.5) |
| N2352_lamm1_a00 | E_KS | 2299.392909 | 2217.950101 at L = 4 | NOT CONVERGED (2299.428 at 3.5), SCF fails from 4.5 (and at L = 4 with G = 2400) |
| N2352_lamp1_a10 / lamm1_a10 | E_KS | 837.5436096 / 846.1109795 | 835.284128 (4.2e-3) / 848.023085 (3.7e-3) | geometric tail |
| N2352_lamp1_a20 / lamm1_a20 | E_KS | 307.6463658 / 311.749613 | 299.999298 (0.063) / 319.053133 (0.062) | geometric tail |
| N592_lamp1_a10_T20 | E / mu / S | 135.5651078 / 0.2929430552 / 387.8116964 | 135.015539 (1.0e-3) / 0.29159221 (5.6e-8) / 387.895573 (1.3e-4) | geometric tail |

* The interaction shift grows with $L$ at $a_{4,0} = 2$: $E_{KS}(\pm\lambda_1) - E_{KS}(0)$ is $-0.517$ / $+0.516$
  ($N = 592$) and $-2.053$ / $+2.050$ ($N = 2352$) at $L = 3$, and $-2.425$ / $+2.370$ and $-9.700$ / $+9.354$ as
  $L \to \infty$; at $a_{4,0} = 0$ it changes by 3% ($N = 592$: $-2.815$ at $L = 3$, $-2.898$ as $L \to \infty$).
* The successive differences of the late slices first grow ($a_{4,0} = 2$: ratios 1.5 and 1.2, the first-order growth
  of section 4.1) and then fall after the saturation; in every interacting state the last ratios approach 0.25
  (about $e^{-2.8\cdot0.5}$).
* The $\pm\lambda_1$ partners of $N = 8$ are negatives of each other: 166 of 168 comparisons ($E_{KS}$ and HOMO, both
  protocols, both step sizes, every $L$) exact, the worst $1.2\times10^{-11}$ relative.
* SCF failures (21 of the 420 fixed-protocol runs, all of $N = 2352$ at $a_{4,0} = 0$): "SCF not converged in 400
  iterations" for $+\lambda_1$ from $L = 3.5$, "potentials left the physical range" for $-\lambda_1$ at $L = 4$ with
  $G = 2400$ and from $L = 4.5$. They coincide with the open-shell occupation of $k = 0$ bulk levels of section 4.2.
  These are failures of the solver's iteration, not proofs that no self-consistent state exists.
* Per-state details, every quantity and every failure message: `tip-convergence.json` (`analysis.fixed`) and
  `tip-convergence-extrapolation.csv`.

### 4.4 RECALIBRATED protocol

$\lambda_1(L)$ from the record's rule (strength = largest first-order potential per unit $\lambda$ over the five
slices):

| L | 3 | 3.5 | 4 | 4.5 | 5 | 5.5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| N = 8 | 157.7 | 88.75 | 44.35 | 20.29 | 8.382 | 3.344 | 1.249 |
| N = 592 | 2.131 | 1.199 | 0.5993 | 0.2742 | 0.1133 | 0.04519 | 0.01687 |
| N = 2352 | 0.5363 | 0.05215 | 0.003946 | 0.0008284 | 0.0001562 | 4.378e-5 | 1.03e-5 |

For $N = 8$ and 592 the last step falls by 2.68, the rate 1.97 per unit $L$ of the zero-mode density at $a_{4,0} = 2$
($3H - 2fm = 1.973$). For $N = 2352$ the strength jumps by a factor 10 from $L = 3$ to $3.5$, when $k = 0$ bulk levels
become occupied at $a_{4,0} = 0$ (section 4.2), and then falls by about $e^{-2.9L}$. All 18 recalibrated states
converge at every $L$ except N2352_lamp1_a00 at $L = 4$ (both step sizes, "SCF not converged in 400 iterations"), and
for all 18 $|E_{KS}(\lambda_1(L)) - E_{KS}(0)|$ is smaller at $L = 6$ than at $L = 3$ (figure 4; e.g. N592_lamp1_a20:
0.517 and 0.0675, N8_lamp1_a00: 0.0378 and $3.1\times10^{-4}$): the large-$L$ values approach the free values of
section 4.2, so the calibration rule does not define an interacting $L \to \infty$ limit.

### 4.5 Type of convergence (the exponential hypothesis tested)

* Free states: no $L$ dependence at all except the fold values, which converge exponentially with the exact rate
  $2fm$ (section 4.1); at $a_{4,0} = 2$ the ratio $e^{-fm} = 0.598$ exceeds the rule's 0.5, so the rule leaves them
  NOT CONVERGED although the law is exact.
* Interacting states: $E_{KS}$ is "consistent with exponential convergence" at $a_{4,0} = 0$ and 1 (exponential fits
  with rates 1.7 to 2.3 per unit $L$) and "faster than exponential" at $a_{4,0} = 2$, where the saturation sets in at
  larger $L$; HOMO and int_p0 are "faster than exponential" from $a_{4,0} = 1$ on (all but int_p0 of N2352_lamm1_a10,
  "consistent with exponential").
* $k = 0$ bulk levels and N2352_lam0_a00: algebraic; not converged.

### 4.6 Independent reference

Reference and Rust agree at $L = 3$ and $L = 4$ in all 28 comparisons ($E_{KS}$, $E_{int}$, HOMO, LUMO, int_p0,
int_rho of N8_lamp1_a00 and N592_lam0_a20), worst |diff|/tolerance 0.006. The $L$ differences agree:
$E_{KS}(4) - E_{KS}(3) = -7.658252309\times10^{-4}$ (Rust) and $-7.658252252\times10^{-4}$ (reference) for
N8_lamp1_a00, int_p0 $-8.069695434\times10^{-3}$ and $-8.069695436\times10^{-3}$; for the fold-band gas N592_lam0_a20
both solvers give the same $E_{KS}$, HOMO, LUMO at $L = 3$ and 4.

## 5. Checks (`tip-convergence.json`, 7 checks, all PASS)

Each check is `{name, criterion, verdict, detail}` with `verdict` PASS or FAIL; `summary` is `{passed, total}`.

| check | criterion | measured (verdict PASS) |
| --- | --- | --- |
| `control_quick_matrix_byte_identical` | patched copy and committed binary, L = 3, G = 900: `all --quick` writes byte-identical outputs and reports | 74/74 identical |
| `control_single_byte_identical` | every `single` run at L = 3: committed binary = patched copy (JSON and profile) | 30/30 |
| `control_single_vs_committed_matrix` | single values = committed CSVs within 1e-12 max(1, abs x) | 357 comparisons, 340 bit-identical, worst 2.3e-16 |
| `calibration_rule_reproduced_at_L3` | the rule as evaluated here gives the recorded lambda_1 (4 digits) at L = 3 | 157.7, 2.131, 0.5363 (strengths to 3.4e-16 relative) |
| `k0_spectrum_exact_L_dependence` | k = 0 levels = exact law within 5e-9 m | 84 levels, 1.42e-10 m |
| `zero_mode_density_exact` | n(0), n(-L) of the free zero modes within 1e-8 relative | 1.1e-11 |
| `reference_solver_at_two_L` | abs(Rust - ref) <= 10 (U_ref + U_Rust) + 1e-9 max(1, abs x) | 28 comparisons, worst 0.006 |

## 6. What is established and what is not

Established (numerically, two solvers at two $L$, controls byte for byte):
* the exact $L$ laws of section 4.1 (k = 0 spectrum, zero-mode density, fold values of the free fold-band gas,
  first-order zero-mode energy at $a_{4,0} = 0$);
* that the free states are $L$-independent except N2352_lam0_a00 and the fold values (which follow the exact law);
* $L \to \infty$ values with uncertainties for 17 of the 19 interacting states, and the size of the $L = 3$ error for
  each of them: at $a_{4,0} = 0$ at most 2.3% in $E_{KS}$ (N8) and 9.4% in int_p0; at $a_{4,0} = 2$ the recorded
  $N = 8$ energy is 0.215 of the large-$L$ value and the interaction shifts of $N = 592$ and 2352 are 4.6 to 4.7 times
  smaller than at large $L$.

NOT established:
* any $L \to \infty$ value for N2352_lam0_a00 (algebraic, the occupied set keeps changing), N2352_lamp1_a00 (SCF fails
  from $L = 3.5$) and N2352_lamm1_a00 (not converged before the SCF fails at $L = 4.5$);
* the convergence of the thermal free state N592_lam0_a20_T50 by the rule (changes of about $10^{-8}$ relative that
  grow with $L$);
* whether self-consistent states exist where the solver's iteration fails;
* $\lambda_2$ states, the slices 0.5 and 1.5, $T = 0.01$ and the other thermal states, the excited states and
  the adiabaticity measure at $L \ne 3$ (not computed); $L > 6$ (not computed);
* a choice of $N$ by the record's rule at large $L$: the bulk edge tends to $m$.

## 7. Files

| file | content |
| --- | --- |
| `tip_convergence.py` | the study (deterministic; writes only into this folder; scratch in `--work`) |
| `tip-convergence.json` | method, patches and source hashes, couplings, exact laws, per-state analysis, reference, checks |
| `tip-convergence-table.csv` | every run: protocol, state, L, G, status and all quantities (672 rows) |
| `tip-convergence-extrapolation.csv` | per protocol, state and quantity: x(3), last converged L, first failed L, x_inf, U, verdict, fit class |
| `fig-differences-EKS.png` | abs successive differences of E_KS vs L, fixed couplings, failures marked |
| `fig-zero-modes-fixed-lambda.png` | N = 8 interacting energy and tip potential vs the first-order laws |
| `fig-k0-spectrum.png` | k = 0 levels vs L (exact law and solver), the HOMO of N = 2352 at a4,0 = 0 |
| `fig-recalibrated-interaction.png` | abs(E_KS(lambda_1(L)) - E_KS(0)) in the recalibrated protocol |

## 8. Run (from the repository root)

```
python Revision/kohn_sham/tip_convergence/tip_convergence.py --work <scratch>/tip --jobs 22                          # one invocation
```

In stages and parts, each within a time limit (the way the record was made; no single calculation may take longer
than 423 s):

```
python Revision/kohn_sham/tip_convergence/tip_convergence.py --work <scratch>/tip --jobs 22 --stage scan --part i/6    # i = 1..6
python Revision/kohn_sham/tip_convergence/tip_convergence.py --work <scratch>/tip --jobs 22 --stage recal --part i/3   # i = 1..3
python Revision/kohn_sham/tip_convergence/tip_convergence.py --work <scratch>/tip --jobs 22 --stage final
```

Every `single` run is stored in the work directory with a status file (written last) and reused by later
invocations (the runs are deterministic); `scan` holds the control singles, the fixed-lambda scan and the calibration
runs, `recal` the recalibrated scan (it needs every calibration run), `final` anything still missing, the quick-matrix
control, the reference, the analysis and the outputs. Needs `cargo` (the patched copy is built in
`<work>/solver_tipL` and reused while its source hashes are the committed ones), the committed binary
`Revision/kohn_sham/solver/target/release/revision_ks_solver.exe` (control singles and the quick matrix) and Python
with numpy and matplotlib (no scipy). At most `--jobs` (capped at 22; the outputs do not depend on it) solver processes
or threads run at a time. Prints every check as `PASS/FAIL - name: detail` on stderr and SUCCESS/FAILURE last on stdout
(exit 0/1).

Run of 2026-10-17 (the corrected metric; 22 workers, each invocation under `timeout -k 5 423`): scan parts 198.3,
214.4, 106.1, 175.7, 94.4 and 85.1 s; recal parts 149.7, 7.0 and 20.8 s; final 32.9 s (quick-matrix control 23.7 s,
reference 4.9 s, report and figures 2.3 s); 1085 s in all, 7 of 7 checks PASS. The patched copy was built once
(14.3 s) and reused. The longest single run is N2352_lamp1_a00 at $L = 6$, $G = 3600$: 254.8 s (SCF fails); the parts
are balanced so that none comes near the limit. A second invocation of the final stage (from the stored singles,
with the quick-matrix control and the reference recomputed) wrote all 7 output files byte-identical.

## 9. History

* First complete run (2026-10-08, the metric b4 = 1): the calibration strength was taken as the maximum of the 151 profile
  samples; the check `calibration_rule_reproduced_at_L3` FAILED for N = 136 (the sampled maximum missed the interior
  maximum by 6.3e-4 relative). The method was corrected (largest sample refined by the quartic through the 5 nearest
  samples; end-point maxima as they are), the criterion unchanged.
* The first analysis accepted a geometric extrapolation when the last ratio was below 0.9. N688_lam0_a00 then got an
  extrapolated value although its ratios 0.77-0.79 are those of an algebraic L^-3 tail. The rule was made stricter (the
  last two ratios in (0, 0.5), section 3); this only removes extrapolations.
* The check records use the key `verdict` (not `result`) and the summary `{passed, total}`, the format of the other
  Revision reports.
* 2026-10-14: the author's coordinates x0..x7 (p8 -> p0, `int_p0`, `p0_brane`); 2026-10-16: the record of the metric with
  b4(x4) (`Vol7AtA4Zero`); both reruns, and their results (N = 136 and 688, the double-exponential tip suppression of
  the free states, the zero-mode density growing like e^{4L}), are in the git history of this file.
* 2026-10-16/17, the corrected metric (`HANDOFF.md` 0.10, phase W5): the study was rewritten for the corrected record.
  kappa = e^{-a4} is constant in y, so nothing suppresses an orbital toward the tip (the former double-exponential tip
  suppression exp(-|k| e^{L - a4}/H) is gone) and the free fold-band states do not depend on L; the zero-mode density
  per proper volume is n(-L) = n(0) e^{(3H - 2fm)L} (before e^{4L}); the first-order zero-mode energy at a4,0 = 0 is
  -(4 lambda/Vol_7)(1 - e^{-L})/(1 - e^{-2L})^2, finite as L -> infinity (before it grew like e^{2L}); the tip potential
  grows like e^{L}; the particle numbers are 8, 592, 2352; the full-matrix control (about 285 s) no longer fits into one
  time-limited step and is replaced by the quick matrix of both binaries, byte for byte; the study runs in stages and
  parts (`--stage scan|recal|final`, `--part i/n`, every `single` run stored with a status file).
