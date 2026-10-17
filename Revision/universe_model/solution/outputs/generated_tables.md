### 9.1 Generated tables (from `solution/solve_model.py`; every number below is from the run)

**Vacuum and block (vacua.py).**

| weights $w$ | $k_0$ | $\Lambda_0/H^2$ | $G(k_0)$ | 4D gravity | block mode $\lambda^2/H^2$ |
| --- | --- | --- | --- | --- | --- |
| (1, 1/32, 1/1152) | 8 | -24 | -1 | repulsive | -2 (stable (oscillatory)) |
| (1, 1/32, 1/768) | 8 | -24 | 1 | attractive | 2 (unstable (real eigenvalue)) |

**Mass spectrum (masses.py; $\eta = HL = 3$, $f = k_0^{-1/2}$).**

| quantity | value |
| --- | --- |
| $m_{KK}$ (first photon/gluon/graviton KK level, fitted to $\rho_0 - 1$) | $1.212 \times 10^{5}$ GeV |
| $H$ | $23421$ GeV |
| proper half-cell $fL$ | $8.936 \times 10^{-21}$ m |
| period of $x_0$, $\pi/(6H)$ | $2.236 \times 10^{-5}$ GeV$^{-1}$ = $4.411 \times 10^{-21}$ m |
| largest $m_W$ of a positive tip term | $0.01824\, m_{KK}$ (so $m_{KK} \geq 4407$ GeV) |
| $\beta_W$, $\beta_Z$ (tip Robin parameters) | $0.01194$, $0.01537$ |
| $m_Z$ predicted (from $m_W$, on-shell $\cos^2\theta_W$) | $91.17068$ GeV (observed 91.188; difference $-0.01732$ GeV) |
| $\rho - 1$ (tree) | $3.800 \times 10^{-4}$ |
| W: bulk hidden-momentum part / tip part of $m_W^2$ | $0.001322$ / $0.9987$ |
| first W KK level | $1.212 \times 10^{5}$ GeV |
| photon, gluon, graviton | $\Lambda_0 = 0$: massless |

| fermion | $m_f$ (GeV) | $m_f/m_{KK} = \zeta(c_f)^2$ | $c_f = f\mu_f L$ | $\mu_f/H$ |
| --- | --- | --- | --- | --- |
| nu | $5.000 \times 10^{-11}$ | $4.126 \times 10^{-16}$ | 19.54 | 18.43 |
| e | $5.110 \times 10^{-4}$ | $4.217 \times 10^{-9}$ | 11.2 | 10.56 |
| u | $0.00216$ | $1.782 \times 10^{-8}$ | 10.44 | 9.844 |
| d | $0.0047$ | $3.878 \times 10^{-8}$ | 10.03 | 9.458 |

| fermion | width $\Delta t$ | $\Delta s$ (m) | $\hbar c/(2\Delta s)$ (GeV) | $m_f$ / Heisenberg estimate |
| --- | --- | --- | --- | --- |
| nu | 0.02558 | $2.286 \times 10^{-22}$ | $4.316 \times 10^{5}$ | $1.159 \times 10^{-16}$ |
| e | 0.04466 | $3.991 \times 10^{-22}$ | $2.472 \times 10^{5}$ | $2.067 \times 10^{-9}$ |
| u | 0.04789 | $4.280 \times 10^{-22}$ | $2.305 \times 10^{5}$ | $9.369 \times 10^{-9}$ |
| d | 0.04984 | $4.454 \times 10^{-22}$ | $2.215 \times 10^{5}$ | $2.122 \times 10^{-8}$ |

**dirac16complex, Kohn-Sham (ks_coupled.py; units $m = H$).**

| quantity | value |
| --- | --- |
| vacuum slice $a_{4} = 3\ln 8/2$, $f$, $\kappa = e^{-a_4}$ | 3.119, 0.3536, 0.04419 |
| fold zero modes; fold band | 8 at $k = 0$; $\varepsilon = \kappa|k|$ exactly (massless), $g_F = 8$ |
| lowest odd bulk level (dark matter) | $2.17492\,m$ = $50939$ GeV |
| lowest even bulk level | $3.126177\,m$ |
| dark matter ($\lambda$ = 0): energy per 8 quanta, $w = p_3/\rho$, $p_0/\rho$ | $17.39936$, $0$, $0.6575$ |
| dark matter ($\lambda$ = 157.7): energy per 8 quanta, $w = p_3/\rho$, $p_0/\rho$ | $17.4307$, $0.001817$, $0.6567$ |

| state (grid 600) | portal | $dE_{KS}/de$ | Hellmann-Feynman deviation | y-exchange residual ($e = 0.02$) |
| --- | --- | --- | --- | --- |
| N = 8, $\lambda$ = 0 | eD | 0 | null (both zero) | null (all terms zero) |
| N = 8, $\lambda$ = 0 | eS | 0 | null (both zero) | null (all terms zero) |
| N = 8, $\lambda$ = 0 | eV | $0.7865$ | $2.259 \times 10^{-14}$ | $7.609 \times 10^{-5}$ |
| N = 8, $\lambda$ = 157.7 | eD | $4.689 \times 10^{-5}$ | $3.690 \times 10^{-10}$ | $1.700 \times 10^{-6}$ |
| N = 8, $\lambda$ = 157.7 | eS | $4.656 \times 10^{-4}$ | $5.677 \times 10^{-11}$ | $2.986 \times 10^{-7}$ |
| N = 8, $\lambda$ = 157.7 | eV | $0.7865$ | $2.856 \times 10^{-13}$ | $7.149 \times 10^{-5}$ |
| N = 592, $\lambda$ = 0 | eD | 0 | null (both zero) | null (all terms zero) |
| N = 592, $\lambda$ = 0 | eS | 0 | null (both zero) | null (all terms zero) |
| N = 592, $\lambda$ = 0 | eV | $58.2$ | $1.343 \times 10^{-15}$ | $7.609 \times 10^{-5}$ |
| N = 592, $\lambda$ = 2.131 | eD | $0.00347$ | $8.071 \times 10^{-10}$ | $1.701 \times 10^{-6}$ |
| N = 592, $\lambda$ = 2.131 | eS | $0.03446$ | $1.731 \times 10^{-10}$ | $2.985 \times 10^{-7}$ |
| N = 592, $\lambda$ = 2.131 | eV | $58.2$ | $2.998 \times 10^{-13}$ | $7.149 \times 10^{-5}$ |

| state (grid 600) | portal | $d\varepsilon_{DM}/de$ | $d(\varepsilon_{n2=1} - \varepsilon_0)/de$ | $d\bar p_0/de$ |
| --- | --- | --- | --- | --- |
| N = 8, $\lambda$ = 0 | eD | $0.006409$ | below $10^{-14}$ | 0 |
| N = 8, $\lambda$ = 0 | eS | $0.03543$ | below $10^{-14}$ | 0 |
| N = 8, $\lambda$ = 0 | eV | $0.03231$ | below $10^{-14}$ | $-2.564 \times 10^{-7}$ |
| N = 8, $\lambda$ = 157.7 | eD | $0.006414$ | $8.262 \times 10^{-11}$ | $3.432 \times 10^{-11}$ |
| N = 8, $\lambda$ = 157.7 | eS | $0.03571$ | $1.947 \times 10^{-9}$ | $6.440 \times 10^{-10}$ |
| N = 8, $\lambda$ = 157.7 | eV | $0.03266$ | $-3.968 \times 10^{-7}$ | $-2.564 \times 10^{-7}$ |
| N = 592, $\lambda$ = 0 | eD | $0.006409$ | below $10^{-14}$ | 0 |
| N = 592, $\lambda$ = 0 | eS | $0.03543$ | below $10^{-14}$ | 0 |
| N = 592, $\lambda$ = 0 | eV | $0.03231$ | below $10^{-14}$ | $-1.898 \times 10^{-5}$ |
| N = 592, $\lambda$ = 2.131 | eD | $0.006414$ | $8.262 \times 10^{-11}$ | $2.540 \times 10^{-9}$ |
| N = 592, $\lambda$ = 2.131 | eS | $0.03571$ | $1.947 \times 10^{-9}$ | $4.766 \times 10^{-8}$ |
| N = 592, $\lambda$ = 2.131 | eV | $0.03266$ | $-3.968 \times 10^{-7}$ | $-1.898 \times 10^{-5}$ |

| coupled fixed point | iterations | contraction | $\delta k$ | $\delta f/f$ | $\delta m_e/m_e$ | $\delta m_\nu/m_\nu$ |
| --- | --- | --- | --- | --- | --- | --- |
| $\sigma$ = 0.1 | 3 | $0$ | $-1.617 \times 10^{-8}$ | $1.011 \times 10^{-9}$ | $-2.263 \times 10^{-8}$ | $-3.950 \times 10^{-8}$ |
| $\sigma$ = 10000 | 5 | $7.472 \times 10^{-4}$ | $-0.001618$ | $1.011 \times 10^{-4}$ | $-0.002262$ | $-0.003946$ |
| $\sigma$ = 1.000 \times 10^{6} | 11 | $0.08263$ | $-0.1755$ | $0.01115$ | $-0.221$ | $-0.3534$ |

**Cosmology (cosmology.py).**

| model | $g_{*s}$ at decoupling | $N_{eff}$ | pull vs Planck | $H_0$ (km/s/Mpc) | BAO $\chi^2$ (12 points) |
| --- | --- | --- | --- | --- | --- |
| Planck LCDM (reference) | - | 3.046 | - | 67.36 | 10.25 |
| UM-1, above mW | 53.25 | 1.295 | -9.97 | 47.33 | 680.7 |
| UM-1, QCD to mW | 44.25 | 1.373 | -9.51 | 48.22 | 614 |
| UM-1, pion gas | 10.25 | 3.536 | 3.21 | 73.11 | 33.77 |
| UM-1, below 20MeV | 7.25 | 5.015 | 11.9 | 90.63 | 390 |
| UM-1, fit to Planck Neff | 12.31 | 2.99 | 0 | 66.75 | 11.64 |
| UM-1, half cell gF over 2 below 20MeV | 7.25 | 3.015 | 0.145 | 67.04 | 10.86 |

| model | $100\theta_*$ | $z_*$ | $r_{drag}$ (Mpc) | $\ell_A$ | $\ell_1$ |
| --- | --- | --- | --- | --- | --- |
| Planck LCDM (reference) | 1.0411 | 1091.85 | 147.09 | 301.76 | 220.7 |
| UM-1, above mW | 1.0411 | 1091.85 | 156.69 | 301.76 | 222.8 |
| UM-1, QCD to mW | 1.0411 | 1091.85 | 156.21 | 301.76 | 222.7 |
| UM-1, pion gas | 1.0411 | 1091.85 | 144.79 | 301.76 | 220.2 |
| UM-1, below 20MeV | 1.0411 | 1091.85 | 138.48 | 301.76 | 218.7 |
| UM-1, fit to Planck Neff | 1.0411 | 1091.85 | 147.39 | 301.76 | 220.7 |
| UM-1, half cell gF over 2 below 20MeV | 1.0411 | 1091.85 | 147.27 | 301.76 | 220.7 |

| background today | value |
| --- | --- |
| $T_\nu = (4/11)^{1/3}T_{CMB}$ | 1.9454 K |
| $n_\nu$ (one species, $\nu + \bar\nu$) | 112 cm$^{-3}$ |
| $T_\Psi$ of the fold band (N_eff fit) | 1.631 K |
| $n_\Psi$ of the fold band ($g_F = 8$) | 264 cm$^{-3}$ |
| $(H_0/H)^2$ | $3.696 \times 10^{-93}$ |
| deflation today $h_4/\dot a_4$ | $-8.857 \times 10^{-94}$ |
| $\delta\Lambda/H^2$ (dark energy) | $7.545 \times 10^{-93}$ |

**Checks** (`solution/reports/solution-checks.json`, 21 of 21 PASS): V1, V2, V3, V4, M1, M2, M3, M4, M5, M6, M7, K1, K2, K3, K4, K5, K6, K7, C1, C2, C3.
