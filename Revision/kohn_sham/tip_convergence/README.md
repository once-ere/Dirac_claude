# Tip-cutoff convergence of the Revision Kohn-Sham record

The Kohn-Sham record (`Revision/kohn_sham/`) replaces the tip $z \to 0$ ($y \to -\infty$) of the author's hidden
coordinate $y = \ln(\sin z)/(6H)$ by a CHOSEN regular-tip condition $b(-L) = 0$ ($\theta = 0$) at the cutoff
$y = -L$, $L = 3$. This folder measures how the recorded results depend on $L$ and whether they converge as $L$
grows ($L = 3, 3.5, \dots, 6$). The author's coordinates {x0, ..., x7}: x0 = the hidden direction
($z = 6Hx_0$), x1..x3 = 3-space, x4 = time, x5..x7 = the three extra times, which DEFLATE EXPONENTIALLY (scale factor
$e^{-a_4} b_4^{1/2}\sin^{1/6}z$); p0 = $T^{x_0}{}_{x_0}$ is the hidden-direction pressure (named p8 before the relabel of 2026-10-14).
The record is that of the author's metric with $b_4(x_4)$ (b4 a function of x4, never 1) on the history $a_4 = Hx_4$,
$b_4 = b_4(0)e^{(4/3)Hx_4}$ (since 2026-10-16; densities per $\mathrm{Vol}_7(a_{4,0}) = \ell^3 v_t e^{2a_{4,0}}$, coupling
$\hat\lambda$; solver README, "The metric with b4(x4)"). This study was rerun on 2026-10-16 for that record (section 9).

## Answer in brief

* **Free states with $k \neq 0$ converge, faster than exponentially.** The tip suppression of an orbital is
  $\exp(-|k|e^{L - a_{4,0}}/H)$; the successive differences fit $\ln|d| = a - c\,e^{L}$ (double exponential) and
  reject a pure exponential. The recorded $L = 3$ values are low by up to 1.4% in $E_{KS}$ and 12% in the
  $y$-pressure integral at $a_{4,0} = 2$ (the redshifted brane band reaches the tip).
* **The $k = 0$ bulk levels converge only algebraically**, $\varepsilon - m \approx (n\pi)^2/(2mL^2)$ (exact law,
  verified to 1.4e-10 m). The bulk edge 1.2923 that defines $N = 688$ is an $L = 3$ value (1.0977 at $L = 6$, $m$ as
  $L \to \infty$). The $N = 688$, $a_{4,0} = 0$ ground state changes its occupied set from $L = 3.5$ on (k = 0 bulk
  levels drop below the top brane-band shell, the KS gap 0.0452 closes) and its energy does NOT converge up to
  $L = 6$.
* **The interacting brane zero modes (every $N$ fills them) depend strongly on $L$.** Their density per proper
  volume grows toward the tip like $e^{(6H - 2m)|y|} = e^{4|y|}$ (exact, verified), so with the recorded couplings
  the first-order interaction energy grows like $e^{2L}$ and the first-order tip potential like $e^{4L}$. The
  self-consistent solution saturates instead: for $N = 8$, $\lambda = \pm\lambda_1$, $a_{4,0} = 0$, $E_{KS}$ goes from
  $\mp 9.868\times10^{-4}$ ($L = 3$) to $\mp 3.007\times10^{-3}$ (extrapolated, $U = 6\times10^{-6}$); the recorded
  value is one third of the large-$L$ value. With $b_4$ the effective coupling falls like $e^{-2a_{4,0}}$, so the
  $N = 8$ energies differ between the slices ($\mp 1.342\times10^{-4}$ at $a_{4,0} = 1$ and $\mp 1.816\times10^{-5}$ at
  $a_{4,0} = 2$ for $L = 3$, against $\mp 1.105\times10^{-3}$ and $\mp 4.06\times10^{-4}$ at large $L$: the recorded late
  values are 8 and 22 times smaller than the large-$L$ ones). The self-consistent iteration of the solver FAILS at
  larger $L$ for 14 of the 19 interacting states studied (from $L = 5$ to $6$ for five $N = 8$ states, from $L = 5$
  to $6$ for five $N = 136$ states and the thermal state, from $L = 3.5$, $4$ or $6$ for three $N = 688$ states). For
  8 of these 14 the converged $L$ values still give a geometric tail (the five $N = 8$ states, N136_lamm1_a00,
  N136_lamm1_a10, N688_lamp1_a10); for the other 6 the limit of $E_{KS}$ is not established here (4 NOT CONVERGED,
  2 with fewer than three converged $L$ values; `tip-convergence-extrapolation.csv`).
* **The recorded calibration rule has no non-trivial limit:** applied at each $L$ it gives $\lambda_1(L)$ falling like
  $e^{-4L}$ for $N = 8$ and $N = 136$ (0.01946 and 0.01206 at $L = 3$, $1.2\times10^{-7}$ at $L = 6$; $N = 688$ in
  section 4.4), so the interaction switches off as $L \to \infty$.

## 1. How the solver gets L (and how L is varied without changing it)

* `results/parameters.json` is an OUTPUT of the solver. The solver does not read it; `--root` only locates
  `ks-theory.json`, `gammas.json` and the 40-digit Mermin fixture. $L = 3$ is the literal `l: 3.0` in `base_phys()`
  (`solver/src/runs.rs`), and the RK4 step count $G = 900$ the literal `g: 900` in `Numerics::canonical()`
  (`solver/src/model.rs`). A scratch root with a modified `parameters.json` is therefore ignored.
* The committed source is NOT changed. `tip_convergence.py` copies the crate into the work directory and applies
  two one-line patches (each must match exactly once): `l` and `g` are read from the environment variables
  `KS_TIP_L` and `KS_RK4_STEPS`, with the defaults 3 and 900. The SHA-256 of every committed source file and of
  the two patched files are recorded in `tip-convergence.json` (`committedSolverSourceSha256`, `patches`).
* **Control (byte for byte).** With `KS_TIP_L=3 KS_RK4_STEPS=900` the patched copy runs `all` and writes all 244
  files of `Revision/kohn_sham/results/` byte-identical to the committed record (SHA-256 against
  `results/manifest.json`, and `manifest.json` itself). Every `single` run of this study at $L = 3$ is
  byte-identical (JSON and profile) between the committed binary and the patched copy (30 states), and equals the
  committed matrix (`ground/summary.csv`, `ground/emt-integrals.csv`, `thermo/thermodynamics.csv`): 357
  comparisons, 342 bit-identical, worst relative difference 4.4e-16.
* **Step size.** $G = 300L$, i.e. the step $h = L/G = 1/300$ of the record is kept (the solver's own analytic
  test at $L = 2$ scales $G$ the same way, `spectrum.rs`). Fixed $h$ keeps the RK4 truncation error per unit
  length of the record; the new tip region is evanescent for $k \neq 0$, with $h\kappa|k| \le 1.6$ at $L = 6$
  (inside the RK4 stability interval). Every run is repeated with $G = 600L$; the $h$-error is
  $U_h = (16/15)|x(600L) - x(300L)|$ (RK4, order 4). $U_h \le 5\times10^{-9}$ for every quantity (largest: int_p0 of N688_lam0_a00), far below the $L$ differences
  discussed.

## 2. What was computed

* **States** (canonical labels of the record): $N \in \{8, 136, 688\}$, $\lambda \in \{0, +\lambda_1, -\lambda_1\}$,
  $a_{4,0} \in \{0, 1, 2\}$ (27 ground states, aufbau, label-set margin $0.25 + 2\sigma$ as in the matrix), the
  thermal states N136_lam0_a20_T50 and N136_lamp1_a10_T20 (margin $0.2 + 2\sigma$), and a free $N = 8$,
  $a_{4,0} = 0$ run with margin 1.2 for the $k = 0$ spectrum. $L \in \{3, 3.5, 4, 4.5, 5, 5.5, 6\}$, each with
  $G = 300L$ and $600L$.
* **Coupling protocols.** FIXED: the recorded constants $\lambda_1 = 0.01946, 0.01206, 0.006645$ ("lambda is a
  constant of the theory"). RECALIBRATED: the record's calibration rule (0.1 m divided by the largest first-order
  mean-field potential per unit $\lambda$ of the free ground states over the five slices, 4 digits) applied at each
  $L$ (18 states $\pm\lambda_1(L)$).
* **Quantities.** $E_{KS}$, $E_{int}$, HOMO, LUMO, KS gap, the zero-mode level, the EMT integrals
  $2\mathrm{Vol}_7\int e^{6Hy}(\rho, p_3, p_t, p_8, n)\,dy$, the brane values $\rho, p_3, p_t, p_8, n$ at $y = 0$;
  thermal: $E$, $\mu$, $S$; diagnostics: $n(-L)$, $\max|v_v|$, $\max|M_{eff} - m|$, iterations, residual.
* **Independent check.** The reference solver (`reference/ks_fd.py`, staggered finite differences, Richardson over
  three grids $G = 300, 600, 1200$ scaled by $L/3$) at $L = 3$ and $L = 4$ for N8_lamp1_a00 and N136_lam0_a20.

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

* $k = 0$, constant $M = m$, $v = 0$, $\theta = 0$: even $\varepsilon = 0$ (zero mode $\chi = (e^{my}, 0)$) and
  $\pm\sqrt{m^2 + (n\pi/L)^2}$; odd $\pm\sqrt{m^2 + p^2}$, $\tan(pL) = -p/m$. All 84 $k = 0$ levels of the scan
  agree to 1.42e-10 m. Every nonzero level tends to $\pm m$ like $(n\pi)^2/(2mL^2)$: algebraic. Bulk edge (odd,
  $n = 0$): 1.2923 (L = 3), 1.2319 (3.5), 1.1887 (4), 1.1566 (4.5), 1.1321 (5), 1.1130 (5.5), 1.0977 (6).
* Zero-mode density per proper volume ($N = 8$, free): $n(0) = 8/(\mathrm{Vol}_7(1 - e^{-2mL}))$, converging
  exponentially to $8/\mathrm{Vol}_7 = 5.03930\times10^{-4}$, and $n(-L) = n(0)\,e^{(6H - 2m)L}$, diverging; both
  verified to 1.1e-11 at every $L$.
* First-order interaction energy of the 8 zero modes ($S = 0$ by the $j = \pm1$ cancellation):
  $E^{(1)}_{int} = -(2\lambda/\mathrm{Vol}_7)\,e^{2L}/(1 - e^{-2L})$ for $m = H = 1$ (in general $\propto
  e^{(6H - 4m)L}$, finite as $L \to \infty$ only for $m > 3H/2$); tip potential $|v_v(-L)| = (\lambda/16)\,n(-L)
  \propto e^{4L}$ (0.1 m at $L = 3$ by the calibration, 5.4 m at $L = 4$, 297 m at $L = 5$, 1.6e4 m at $L = 6$),
  all at $a_{4,0} = 0$ (at $a_{4,0}$ both carry the factor $e^{-2a_{4,0}}$ of the effective coupling).
  The solved $E_{KS}/E^{(1)}_{int}$ is 0.995, 0.851, 0.402, 0.151 at $L = 3, 3.5, 4, 4.5$: first order holds only at
  $L = 3$; the self-consistent $\max|v_v|$ saturates at about 0.91 m.

### 4.2 Free states ($\lambda = 0$)

$x(3)$ is the recorded value, $x_\infty$ the extrapolated value with uncertainty $U$, "rel" $= |x(3) - x_\infty|/|x_\infty|$.

| state | quantity | x(3) | x_inf | U | rel | status |
| --- | --- | --- | --- | --- | --- | --- |
| N8, all slices | E_KS, HOMO | 0 | 0 | 1e-11 | 0 | exact zero modes |
| N8_lam0_a00 | LUMO | 0.4307336786 | 0.4307456266 | 1e-11 | 2.8e-5 | converged from L = 4 |
| N8_lam0_a10 | LUMO | 0.1703492513 | 0.1711546277 | 1e-11 | 4.7e-3 | converged from L = 5 |
| N8_lam0_a20 | LUMO | 0.06415941073 | 0.06563459278 | 1e-11 | 2.2e-2 | geometric tail |
| N136_lam0_a00 | E_KS | 80.28222169 | 80.28253097 | 1e-9 | 3.9e-6 | converged from L = 4 |
| N136_lam0_a10 | E_KS | 32.38411569 | 32.42752401 | 4e-10 | 1.3e-3 | converged from L = 5 |
| N136_lam0_a20 | E_KS | 12.44506958 | 12.62207048 | 2e-10 | 1.4e-2 | geometric tail |
| N136_lam0_a20 | HOMO / LUMO | 0.1267657 / 0.1412225 | 0.1279669 / 0.1422925 | 1e-11 | 9.4e-3 / 7.5e-3 | converged from L = 5.5 / 5 |
| N136_lam0_a20 | int_p0 | 8.47270252 | 9.638387084 | 4e-10 | 0.12 | geometric tail |
| N136_lam0_a20 | rho / p0 at the brane (per Vol_7(a4,0)) | 1.448355e-5 / 6.793090e-6 | 1.467622e-5 / 6.992652e-6 | 1e-11 | 1.3e-2 / 2.9e-2 | converged from L = 5 |
| N688_lam0_a00 | E_KS | 680.4412466 | - | - | - | NOT CONVERGED (678.2997 at L = 6; ratios 0.77-0.79, algebraic) |
| N688_lam0_a00 | KS gap | 0.04518028744 | 0 from L = 3.5 | - | - | occupied set changes: open shell |
| N688_lam0_a10 | E_KS | 279.4248865 | 279.4766394 | 3e-9 | 1.9e-4 | converged from L = 5 |
| N688_lam0_a20 | E_KS | 110.386667 | 110.98129 | 1e-9 | 5.4e-3 | geometric tail |
| N688_lam0_a20 | HOMO / LUMO | 0.2057597 / 0.2143699 | 0.2062890 / 0.2148429 | 1e-11 | 2.6e-3 / 2.2e-3 | converged from L = 5 |
| N136_lam0_a20_T50 | E / mu / S | 23.38444701 / 0.05801333 / 464.13946 | 23.57644348 / 0.05876001 / 465.81375 | 3e-10 / 2e-11 / 6e-9 | 8.1e-3 / 1.3e-2 / 3.6e-3 | geometric / from 5.5 / geometric |

N688_lam0_a00 in detail: at $L = 3.5$ the odd $k = 0$ level (1.2319) lies below the top brane-band shell
($n^2 = 11$, 1.24711): 8 particles move into $k = 0$ bulk levels and the $n^2 = 11$ shell is open (11/12 filled);
from $L = 4.5$ the even $n = 1$ level enters as well (10/12 filled). $E_{KS}$: 680.441, 680.320, 679.974, 679.497,
678.993, 678.605, 678.300. As $L \to \infty$ every bulk level tends to $m = 1$, below the upper brane-band shells,
so the large-$L$ ground state of $N = 688$ at $a_{4,0} = 0$ is a different state; its limit is not established.

### 4.3 Interacting states with the recorded couplings (FIXED protocol)

| state | quantity | x(3) | x_inf (U) or last value | status |
| --- | --- | --- | --- | --- |
| N8_lamp1_a00 / lamm1_a00 | E_KS | $\mp$9.868426191e-4 | $\mp$3.007259560e-3 (6.1e-6) | geometric tail, SCF fails from L = 5 |
| N8_lamp1_a00 / lamm1_a00 | HOMO (zero-mode level) | $\mp$2.455627077e-4 | $\mp$5.635259024e-4 (1.0e-8) | geometric tail |
| N8_lamp1_a10 / lamm1_a10 | E_KS | $\mp$1.341747940e-4 | $\mp$1.1057147e-3 (2.2e-6) / $\pm$1.1047351e-3 (6.8e-8) | geometric tail, SCF fails from L = 5.5 / 6 |
| N8_lamp1_a20 / lamm1_a20 | E_KS | $\mp$1.816014714e-5 | $\mp$4.066894e-4 (8.2e-7) / $\pm$4.0632895e-4 (2.5e-8) | geometric tail; lamp1 fails at 6, lamm1 converges at every L |
| N136_lamm1_a00 | E_KS | 80.26317502 | 80.26504198 (3.2e-7) | geometric tail, SCF fails from 5.5 |
| N136_lamp1_a00 | E_KS | 80.30152249 | 80.29988865 at L = 4.5 | NOT CONVERGED (ratios 1.03, 0.118), SCF fails from 5 |
| N136_lamp1_a10 | E_KS | 32.39983783 | 32.44747737 at L = 5 | NOT CONVERGED (sign change), SCF fails from 5.5 |
| N136_lamm1_a10 / a20 | E_KS | 32.36933673 / 12.44454435 | 32.40853811 (1.3e-7) / 12.60426502 (6.4e-8) | geometric tail; a10 fails at 6 |
| N136_lamp1_a20 | E_KS | 12.44557782 | 12.64785276 at L = 5.5 | NOT CONVERGED (sign change), SCF fails at 6 |
| N688_lamp1_a00 / lamm1_a00 | E_KS | 680.5684588 / 680.3157256 | - | NOT ESTABLISHED (fewer than 3 converged L values: SCF fails at L = 3.5 / 4) |
| N688_lamm1_a10 / a20 | E_KS | 279.3207651 / 110.3499850 | 279.3677497 (1.3e-8) / 110.8737488 (1.4e-7) | geometric tail |
| N688_lamp1_a10 / a20 | E_KS | 279.5338971 / 110.4250785 | 279.5909364 (2.2e-7) / 111.1294009 (7.1e-8) | geometric tail; a10 fails at 6 |
| N136_lamp1_a10_T20 | E / mu / S | 33.32682377 / 0.3247437533 / 86.58220634 | 33.37620936 / 0.3248452047 / 86.74522151 at L = 5 | NOT CONVERGED, SCF fails from 5.5 |

* The interaction shift itself grows with $L$ at $a_{4,0} = 2$: $E_{KS}(\pm\lambda_1) - E_{KS}(0)$ of N136_a20 is
  $+5.1\times10^{-4}$ / $-5.3\times10^{-4}$ at $L = 3$, and $+2.58\times10^{-2}$ ($L = 5.5$) / $-1.78\times10^{-2}$
  ($L \to \infty$): the recorded $L = 3$ interaction effects at the late slice are 34-51 times smaller than at large $L$.
* The $\pm\lambda$ partners of $N = 8$ are negatives of each other to $3.7\times10^{-14}$ relative in $E_{KS}$ and
  $3.9\times10^{-13}$ in HOMO at every $L$ where both converge (fixed protocol, step $h = 1/300$: 15 pairs, 14 of
  them exact negatives; in the recalibrated protocol exact negatives in 21 of 21 pairs; `tip-convergence-table.csv`).
* SCF failures (14 of 19 interacting states at some $L$; none in the recalibrated protocol): "potentials left the
  physical range" in the direct iteration and in the coupling continuation (the free start has the first-order tip
  potential, $10^2$-$10^4$ m at $L \ge 5$), and for N688_lamp1_a00 at $L = 3.5$ "SCF not converged in 400
  iterations" (the open-shell level crossing of section 4.2). These are failures of the solver's iteration, not
  proofs that no self-consistent state exists: N8_lamm1_a20, the same zero-mode problem at the weakest effective
  coupling, converges at every $L$.
* Per-state details, every quantity and every failure message: `tip-convergence.json` (`analysis.fixed`) and
  `tip-convergence-extrapolation.csv`.

### 4.4 RECALIBRATED protocol

$\lambda_1(L)$ from the record's rule (strength = largest first-order potential per unit $\lambda$, set by the
zero-mode density at the tip):

| L | 3 | 3.5 | 4 | 4.5 | 5 | 5.5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| N = 8 | 0.01946 | 0.002638 | 0.0003572 | 4.835e-5 | 6.544e-6 | 8.857e-7 | 1.199e-7 |
| N = 136 | 0.01206 | 0.002638 | 0.0003572 | 4.835e-5 | 6.544e-6 | 8.857e-7 | 1.199e-7 |
| N = 688 | 0.006645 | 2.223e-5 | 1.511e-6 | 3.845e-8 | 2.512e-9 | 1.605e-10 | 1.007e-11 |

With $b_4$ the strength of $N = 136$ is set from $L = 3.5$ on by the zero modes at $a_{4,0} = 0$, as for $N = 8$
(at $L = 3$ by the brane band at $a_{4,0} = 1$). All 18 recalibrated states converge at every $L$ (no SCF failure),
and for all 18 $|E_{KS}(\lambda_1(L)) - E_{KS}(0)|$ is smaller at $L = 6$ than at $L = 3$ (figure 4): their large-$L$
values approach the free values of section 4.2, so the calibration rule does not define an interacting
$L \to \infty$ limit. $N = 688$ at $a_{4,0} = 0$ (both signs): from $L = 3.5$ on its ground state occupies $k = 0$
bulk levels (section 4.2), which have no $\kappa|k|$ suppression, so their proper density grows toward the tip like
$e^{6H|y|}$; the rule then drives $\lambda_1$ down faster (the $N = 688$ row), the first-order potential stays 0.1 m by
construction, and the interaction energy stays near $10^{-2}$ m ($E_{int} = 0.128$ at $L = 3$, $0.0096$ at $L = 6$,
$\lambda_1 = 10^{-11}$). The SCF failures of N688_lamp1_a00 and N688_lamm1_a00 with the recorded couplings (from
$L = 3.5$ and $4$) coincide with this occupation of $k = 0$ bulk levels.

### 4.5 Type of convergence (the exponential hypothesis tested)

* Free $k \neq 0$ quantities: the ratios of successive differences decrease (N136_lam0_a20 $E_{KS}$: 0.29, 0.15,
  0.058, 0.015, 0.0014; N688_lam0_a20 LUMO: 0.049, 0.0066, 0.0002). The exponential fit is rejected (max log
  residual 1.0-2.6); $\ln|d|$ linear in $e^L$ fits (max residual 0.01-0.4). This is the double-exponential tip
  suppression $\exp(-|k|e^{L - a_{4,0}})$, slowest at $a_{4,0} = 2$ and for the smallest $|k|$.
* Interacting zero modes ($N = 8$): after the saturation the successive differences fall geometrically (rate near
  $6H$ per unit $L$, the proper-volume factor $e^{6Hy}$); with the record's range of converged $L$ values the
  classification is "consistent with exponential convergence" for $a_{4,0} = 0$ and "faster than exponential" for the
  later slices, where the saturation sets in at larger $L$ (weaker effective coupling).
* $k = 0$ bulk levels and N688_lam0_a00: algebraic; not converged.

### 4.6 Independent reference

Reference and Rust agree at $L = 3$ and $L = 4$ in all 28 comparisons ($E_{KS}$, $E_{int}$, HOMO, LUMO, int_p0,
int_n, int_rho of N8_lamp1_a00 and N136_lam0_a20), worst |diff|/tolerance 0.005. The $L$ differences agree:
$E_{KS}(4) - E_{KS}(3) = -1.954398469\times10^{-3}$ (both solvers, N8_lamp1_a00, $a_{4,0} = 0$: unchanged by $b_4$) and
$0.1711236020$ (N136_lam0_a20); int_p0: $-0.0165948537$ and $1.10655006$.

## 5. Checks (`tip-convergence.json`, 7 checks, all PASS)

Each check is `{name, criterion, verdict, detail}` with `verdict` PASS or FAIL; `summary` is `{passed, total}`.

| check | criterion | measured (verdict PASS) |
| --- | --- | --- |
| `control_full_matrix_byte_identical` | patched copy, L = 3, G = 900: `all` writes every committed result file byte for byte | 244/244 identical |
| `control_single_byte_identical` | every `single` run at L = 3: committed binary = patched copy (JSON and profile) | 30/30 |
| `control_single_vs_committed_matrix` | single values = committed CSVs within 1e-12 max(1, abs x) | 357 comparisons, worst 4.4e-16 |
| `calibration_rule_reproduced_at_L3` | the rule as evaluated here gives the recorded lambda_1 (4 digits) at L = 3 | 0.01946, 0.01206, 0.006645 (strengths to 5.5e-6 relative) |
| `k0_spectrum_exact_L_dependence` | k = 0 levels = exact law within 5e-9 m | 84 levels, 1.42e-10 m |
| `zero_mode_density_exact` | n(0), n(-L) of the free zero modes within 1e-8 relative | 1.1e-11 |
| `reference_solver_at_two_L` | abs(Rust - ref) <= 10 (U_ref + U_Rust) + 1e-9 max(1, abs x) | 28 comparisons, worst 0.005 |

## 6. What is established and what is not

Established (numerically, two solvers at two $L$, controls byte for byte):
* the exact $L$ laws of section 4.1 (k = 0 spectrum, zero-mode density, first-order zero-mode energy);
* $L \to \infty$ values with uncertainties for the free states except N688_lam0_a00, and for the interacting
  states marked converged or geometric in 4.3; the size of the $L = 3$ error for each of them (largest: $E_{KS}$
  1.4% and int_p0 12% for N136_lam0_a20; $E_{KS}$ of the interacting $N = 8$ states, a factor 3.05 at $a_{4,0} = 0$,
  8.2 at $a_{4,0} = 1$ and 22 at $a_{4,0} = 2$);
* the double-exponential convergence of the free $k \neq 0$ sector and the exponential (rate $6H$) convergence of the
  saturated zero-mode interaction.

NOT established:
* any $L \to \infty$ value for N688_lam0_a00 (algebraic, the occupied set keeps changing), and for the 6
  interacting states whose $E_{KS}$ differences do not meet the geometric-tail rule before the SCF fails
  (N136_lamp1_a00, N136_lamp1_a10, N136_lamp1_a20, N688_lamp1_a00 and N688_lamm1_a00 at $a_{4,0} = 0$, the thermal
  N136_lamp1_a10_T20; `tip-convergence-extrapolation.csv`); the other 8 states whose SCF fails (the five $N = 8$
  states, N136_lamm1_a00, N136_lamm1_a10 and N688_lamp1_a10) have a geometric tail before the failure;
* whether self-consistent states exist where the solver's iteration fails;
* $\lambda_2$ states, the slices 0.5 and 1.5, $T = 0.01$ and the other thermal states, the excited states and
  the adiabaticity measure at $L \ne 3$ (not computed); $L > 6$ (not computed; RK4 at fixed $h$ would leave its
  stability interval near $L = 7$);
* a choice of $N$ by the record's rule at large $L$: the bulk edge tends to $m$.

## 7. Files

| file | content |
| --- | --- |
| `tip_convergence.py` | the study (deterministic; writes only into this folder; scratch in `--work`) |
| `tip-convergence.json` | method, patches and source hashes, couplings, exact laws, per-state analysis, reference, 7 checks |
| `tip-convergence-table.csv` | every run: protocol, state, L, G, status and all quantities (672 rows) |
| `tip-convergence-extrapolation.csv` | per protocol, state and quantity: x(3), last converged L, first failed L, x_inf, U, verdict, fit class |
| `fig-differences-EKS.png` | abs successive differences of E_KS vs L, fixed couplings, failures marked |
| `fig-zero-modes-fixed-lambda.png` | N = 8 interacting energy and tip potential vs the first-order laws |
| `fig-k0-spectrum.png` | k = 0 levels vs L (exact law and solver), the HOMO of N = 688 at a4,0 = 0 |
| `fig-recalibrated-interaction.png` | abs(E_KS(lambda_1(L)) - E_KS(0)) in the recalibrated protocol |

## 8. Run (from the repository root)

```
python Revision/kohn_sham/tip_convergence/tip_convergence.py --work <scratch>/tip --jobs 8
```

Needs `cargo` (the patched copy is built in `<work>/solver_tipL`, about 4-12 s), the committed binary
`Revision/kohn_sham/solver/target/release/revision_ks_solver.exe` (control singles) and Python with numpy and
matplotlib (no scipy). At most `--jobs` (capped at 22 since 2026-10-14, at 8 before; the outputs do not depend on it) solver processes or threads run at a time. Prints every check
as `PASS/FAIL - name: detail` on stderr and SUCCESS/FAILURE last on stdout (exit 0/1).

Measured (2026-10-08, 8 workers, machine shared with other jobs): two complete runs took 541 s and 553 s
(build 7-9 s, control matrix 155-167 s, control singles 6-7 s, fixed-coupling scan 288-302 s with 420 runs,
calibration and recalibrated scans 49-58 s with 357 runs, reference 16 s with 4 processes, figures 4 s). All 7
output files of the two runs are byte-identical (`tip-convergence.json`, both CSV files, the four PNG figures).

Run of 2026-10-14 (the author's coordinates x0..x7; the solver's hidden-direction pressure is named p0, before p8),
22 workers (the cap was raised from 8; the outputs do not depend on it), other jobs of this work on the machine:
196 s in total (build 3 s, control matrix 78 s, control singles 3 s, fixed-coupling scan 88 s, calibration and
recalibrated scans 13 s, reference 9 s, report and figures 2 s); 7 of 7 checks PASS. The four PNG figures are
byte-identical to those of 2026-10-08; `tip-convergence.json` and the two CSV files differ only by the renaming
p8 -> p0 (`int_p0`, `p0_brane`) and, in `tip-convergence.json`, by the sha256 of the four changed solver sources
(`analysis.rs`, `runs.rs`, `scf.rs`, `theory.rs`) and of the patched copy.

Run of 2026-10-16 (the record of the metric with b4(x4); 22 workers, machine otherwise idle, `timeout -k 5 423`):
187 s in total; 7 of 7 checks PASS. The first attempt stopped after the scans (177 s) with `KeyError: 'Vol7'`: the
solver's `parameters.json` now names the cell volume at a4,0 = 0 `Vol7AtA4Zero` (the cell volume depends on a4,0); the
study uses it only at a4,0 = 0 (zero-mode density and the first-order laws of figure 2, labelled "a4,0 = 0").

## 9. History

* First complete run: the calibration strength was taken as the maximum of the 151 profile samples; the check
  `calibration_rule_reproduced_at_L3` FAILED for N = 136 (0.0009304 against the recorded 0.0009298; the sampled
  maximum missed the interior maximum by 6.3e-4 relative). The method was corrected (largest sample refined by the
  quartic through the 5 nearest samples; end-point maxima as they are), the criterion unchanged; it now gives
  0.0009298 (strength 6.3e-7 from the recorded one).
* The first analysis accepted a geometric extrapolation when the last ratio was below 0.9. N688_lam0_a00 then got an
  extrapolated value although its ratios 0.77-0.79 are those of an algebraic $L^{-3}$ tail. The rule was made
  stricter (the last two ratios in $(0, 0.5)$, section 3); this only removes extrapolations.
* The check records use the key `verdict` (not `result`) and the summary `{passed, total}`, the format of the other
  Revision reports (requested by the coordinator).
