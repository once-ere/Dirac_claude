## 12. The field equations for a4 and b4: Einstein and Einstein-Lovelock

The corrected metric of the author contains two unknown functions of the time, $a_4(x_4)$ and $b_4(x_4)$. This chapter derives, step by step, the equations that gravity imposes on them: first by hand, as far as the algebra stays short, and then completely with four notebooks. We will find that the equations reduce to one constraint and two equations of second order; that flat space is an empty universe of this form, while in Einstein gravity and with the author's weights no exponential history is empty; that the exponential history of the Revision record needs a source of an unusual kind, which grows in time; that the equations do not care whether 3-space inflates or deflates; and that the exact condensates of the commuting field dirac16complex00 that the record has found are the source of none of the histories on which they live.

### 12.1 What this chapter does, and why

In Chapter 3 we met the corrected metric: a rule that turns small steps $dx_0, \dots, dx_7$ into squared lengths. Three of its directions, $x_1, x_2, x_3$, are ordinary 3-space; $x_4$ is the time; $x_5, x_6, x_7$ are the three **extra times**, which behave like time; $x_0$ is the **hidden** space direction. Lengths along 3-space are multiplied by $e^{a_4}$, and lengths along the hidden direction and the extra times by $e^{-a_4}b_4^{1/2}$ (times a fixed function of $x_0$). When this second factor shrinks, the hidden direction and the extra times **deflate**. That is the author's picture of the primordial universe.

A metric is not free. Einstein's great idea is that matter tells space how to curve: the curvature of the metric, collected into a tensor, equals a constant times the energy and momentum of the matter. The equations that say this are the **field equations of gravity**. For the corrected metric they become equations for the two functions $a_4(x_4)$ and $b_4(x_4)$, and they answer questions such as:

- Can the corrected metric exist with no matter at all? (Yes, as flat space; but in Einstein gravity and with the author's weights no exponential history is empty: Section 12.11 and Notebook 12b.)
- If $a_4$ and $b_4$ are given, what matter must be present? (The **required source**: Sections 12.8, 12.11 and 12.12.)
- If the matter is given, how do $a_4$ and $b_4$ evolve? (Two equations of second order and a constraint: Sections 12.9 and 12.21.)
- Do the equations prefer one direction of time? (No; the sign of the rate is a choice: Section 12.12.)
- Can a field of this theory be the required source exactly? (The record: no condensate can be the source of the record history; this book: the record's exact condensates are the source of none of their own histories; the general question is OPEN: Section 12.26.)

We use the most general gravity theory that keeps the field equations of second order in eight dimensions, **Einstein-Lovelock gravity**, and its special case, Einstein gravity. Every formula comes from the Revision record (the folders `Revision/field_equations_a4`, `Revision/metric_warped`, `Revision/theory`, `Revision/gkd_lovelock` and `Revision/lead_checks` of the repository) or from the book's own notebooks, which reproduce the record wherever the two overlap and say so in a PASS line. The four notebooks of the chapter are: Notebook 12a, which derives all the equations from the metric with exact computer algebra; Notebook 12b, which computes the source that the exponential histories require; Notebook 12c, which integrates the equations for prescribed sources; and Notebook 12d, which builds the record's exact condensates of the field dirac16complex00 with the author's eight real 16 by 16 gamma matrices and puts them into the field equations.

An earlier version of this chapter was written for the metric of 2026-10-14, withdrawn on 2026-10-16; none of its formulas is used here.

### 12.2 The words and symbols of this chapter

Each word below is defined in plain terms; the later sections make every definition precise with formulas.

- **Coordinates** $x_0, \dots, x_7$: the eight numbers that name a point, in the author's order. $x_0$: the hidden direction, space-like, listed first. $x_1, x_2, x_3$: ordinary 3-space. $x_4$: the time. $x_5, x_6, x_7$: the three extra times (time-like). In the Python code the positions 0 to 7 of a list stand for $x_0$ to $x_7$: position $k$ is $x_k$.
- **Hidden angle** $z = 6Hx_0$: the metric depends on $x_0$ only through $z$, which may take every real value (the metric contains $\cot^2 z$ and $(\sin^2 z)^{1/6}$, both defined wherever $\sin z \ne 0$). $H > 0$ is a constant of the metric with the unit of an inverse length.
- **Prime**: $a_4' = da_4/dx_4$, $a_4'' = d^2a_4/dx_4^2$, and so on. The code writes them as `ad1`, `ad2`, `ad3`.
- **The record's variables**: $u = b_4'/b_4$ (the rate of $\ln b_4$, code `uu`), $v = u'$ (code `vv`), $k = e^{2a_4}/b_4$ (code `kk`), and the **block rate** $h_4 = \tfrac12u - a_4'$ (the record's `hh`). In this chapter we write $h$ for $h_4$.
- **Metric** $g_{\mu\nu}$: the table of numbers that turns coordinate steps into squared lengths, $ds^2 = \sum_{\mu,\nu} g_{\mu\nu}\,dx_\mu dx_\nu$. The corrected metric is **diagonal**: only $g_{00}, g_{11}, \dots, g_{77}$ are not zero. Its inverse $g^{\mu\nu}$ is then diagonal too, with $g^{\mu\mu} = 1/g_{\mu\mu}$.
- **Signature**: the signs of the diagonal entries, here $(+,+,+,+,-,-,-,-)$ in the order $x_0, \dots, x_7$: four space-like and four time-like directions, written (4,4).
- **Scale factor**: the number by which lengths along a direction are multiplied; for a diagonal metric it is $\sqrt{|g_{\mu\mu}|}$.
- **Block**: the four directions $x_0, x_5, x_6, x_7$, which share the scale factor $e^{-a_4}b_4^{1/2} = k^{-1/2}$; its logarithm changes at the rate $h$.
- **Index up, index down**: a tensor is a table of numbers labelled by indices; an upper index and a lower index transform in opposite ways. $T^\mu{}_\nu$ has one of each and is called **mixed**. The diagonal metric moves an index up or down by multiplying by $g^{\mu\mu}$ or $g_{\mu\mu}$.
- **Sum convention**: in this chapter a sum is always written out with $\sum$ or said in words, except in the definitions of Section 12.7 and in the formulas quoted from the record, where an index that appears once up and once down is summed over its eight values; "no sum" marks the exceptions.
- **Christoffel symbol** $\Gamma^a{}_{bc}$: a combination of first derivatives of the metric that says how the coordinate directions turn from point to point.
- **Riemann tensor** $R^{ab}{}_{mn}$: the curvature, built from the Christoffel symbols and their derivatives. **Sectional curvature** $K_{ab} = R^{ab}{}_{ab}$ (no sum): the curvature of the plane spanned by the directions $x_a$ and $x_b$.
- **Ricci tensor** $R^h{}_j$, **Ricci scalar** $R$, **Einstein tensor** $G^h{}_j$: sums of Riemann components defined in Section 12.6.
- **Generalized Kronecker delta** (GKD): a sign, $+1$, $-1$ or $0$, attached to two lists of indices (Section 12.7). **Lovelock tensors** $E_{(1)}, E_{(2)}, E_{(3)}$: the three curvature tensors built with the GKD; $E_{(1)}$ is the Einstein tensor and $E_{(2)}$ the **Gauss-Bonnet** tensor.
- **Couplings**: $\alpha_1, \alpha_2, \alpha_3$ weigh the three Lovelock tensors; $\Lambda$ is the **cosmological constant**; $\kappa > 0$ measures the strength of gravity. **Einstein gravity**: $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$. **Einstein-Gauss-Bonnet gravity**: $\alpha_1 = 1$, $\alpha_3 = 0$. **The author's weights**: $\alpha_k = w_k/H^{2k}$ with $w = (1, 1/32, 1/1152)$ and $\Lambda = -10$ in units $H = 1$ (record `Revision/field_equations_a4/a4-equations.json`, key `exponentialHistory/authorWeights`, which names the author's notebook as their origin).
- **Energy-momentum tensor** $T^\mu{}_\nu$, also called the **source**: the energy and momentum of the matter. Its parts are the **energy density** $\rho = -T^{x_4}{}_{x_4}$, the **pressures** $p_3$ (3-space), $p_0$ (hidden direction), $p_t$ (extra times), and the **mixed components** such as $q_{40} = T^{x_4}{}_{x_0}$ and $q_{04} = T^{x_0}{}_{x_4}$.
- **Anisotropic**: with different pressures in different directions.
- **Field equations**: the equations of gravity, $\sum_k \alpha_k E_{(k)}{}^\mu{}_\nu + \Lambda\delta^\mu_\nu = \kappa T^\mu{}_\nu$ (Section 12.8). Their three independent parts are the **constraint** (time, $x_4$), the **3-space equation** and the **block equation** (one equation for the hidden direction and the extra times together).
- **Jacobian** $J$: the 2 by 2 table of the coefficients of $a_4''$ and $v$ in the 3-space and block equations; where $\det J \ne 0$ the two equations can be solved for $a_4''$ and $v$.
- **Divergence** $\nabla_\mu T^\mu{}_\nu$: the curved-space form of "the change of a quantity in time plus its outflow"; zero divergence means **conservation**. The **Bianchi identity** says that the left-hand side of the field equations has zero divergence for every metric.
- **Vacuum**: no matter, $T^\mu{}_\nu = 0$.
- **Null vector**: a direction of zero length, such as the frame direction $x_4 + x_1$ or $x_4 + x_0$ (time-like plus space-like). The **null energy conditions** along them are $\rho + p_3 \ge 0$ and $\rho + p_0 \ge 0$; ordinary matter satisfies both.
- **Exponential history**: $a_4 = AHx_4 + a_0$, $b_4 = b_4(0)\,e^{\beta AHx_4}$ with constants $A$ (the **slope**), $\beta$, $a_0$ and $b_4(0) > 0$. Then $a_4' = AH$, $u = \beta AH$, $h = (\tfrac12\beta - 1)AH$, and $k = k(0)\,e^{(2 - \beta)AHx_4}$.
- **Record history**: the exponential history with $A = 1$, $\beta = 4/3$, $a_0 = 0$, $b_4(0) = 1$, so $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ and $k = e^{(2/3)Hx_4}$. The record uses it as a PRESCRIBED background (key `exponentialHistory/authorWeights/statement` of `a4-equations.json`): it is ASSUMED, not derived from a source.
- **Prescribed source**: a source chosen by hand to see what the equations do. It is ASSUMED, not derived from a field.
- **Condensate**: a solution of a field equation that depends on the time $x_4$ only. **Witness**: an explicit example that proves that something exists.
- **Status labels**: PROVED (exact, with the verifier file and check name), COMPUTED (numerical, with the output it comes from and its measured accuracy), ASSUMED, HYPOTHESIS, OPEN.
- **Report**, **check**: every verifier of the Revision record writes a report file, a list of checks, each with a name and a verdict (PASS or FAIL). The reports that this chapter cites most often get short names:

| short name | report file | what it verifies |
| --- | --- | --- |
| sympy report | `Revision/field_equations_a4/reports/python-a4-report.json` | the field equations, derived with sympy |
| Wolfram report | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | the field equations, derived in the Wolfram Language |
| metric report | `Revision/metric_warped/reports/python-warped-metric-report.json` | the corrected metric and the source of the record history |
| field-theory report | `Revision/theory/reports/wolfram-field-theory.json` | the geometry and the field theory in the corrected metric |
| lead's Einstein report | `Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json` | independent checks of the Einstein and Gauss-Bonnet tensors |
| lead's divergence report | `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json` | independent checks of the conservation law and the spin connection |

### 12.3 The corrected metric, its determinant and the volume

The corrected metric (version 2 of 2026-10-16) is diagonal. In the order $x_0, \dots, x_7$ its eight diagonal entries are

$$
g = \mathrm{diag}\Big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4},\ e^{2a_4},\ e^{2a_4},\ -1,\ -e^{-2a_4}b_4\,w_z^2,\ -e^{-2a_4}b_4\,w_z^2,\ -e^{-2a_4}b_4\,w_z^2\Big),
$$

with $z = 6Hx_0$ and the abbreviation $w_z = (\sin^2 z)^{1/12} > 0$, so that $w_z^2 = (\sin^2 z)^{1/6}$ (record `Revision/field_equations_a4/a4-equations.json`, key `conventions/metric`; checked in Notebook 12a, In [4], against the check `corrected_metric_entries` of the metric report). The scale factors are

- $e^{a_4}$ for each 3-space direction: 3-space has no factor that depends on $x_0$;
- $1$ for the time;
- $e^{-a_4}b_4^{1/2}\,|\cot z|$ for the hidden direction;
- $e^{-a_4}b_4^{1/2}\,w_z$ for each extra time.

The hidden direction and the extra times share the factor $e^{-a_4}b_4^{1/2}$; the record says that the block $(x_0, x_5, x_6, x_7)$ is $e^{-2a_4}b_4$ times a space of constant curvature $-H^2$ (key `conventions/coordinates`). Since $e^{-a_4}b_4^{1/2} = (e^{2a_4}/b_4)^{-1/2} = k^{-1/2}$, the block shrinks exactly when $k$ grows. Its logarithm, $-a_4 + \tfrac12\ln b_4$, changes at the rate

$$
\frac{d}{dx_4}\Big(-a_4 + \tfrac12\ln b_4\Big) = -a_4' + \tfrac12\,\frac{b_4'}{b_4} = \tfrac12u - a_4' = h
$$

(the derivative of a sum is the sum of the derivatives; the chain rule gives $(\ln b_4)' = b_4'/b_4 = u$). On the record history $h = \tfrac12\cdot\tfrac43H - H = -\tfrac13H$: 3-space inflates as $e^{Hx_4}$ and the block deflates as $e^{-Hx_4/3}$.

The **determinant** of the metric measures volume. We compute it line by line; after each line we name the rule that produced it.

$$
\det g = g_{00}\,g_{11}\,g_{22}\,g_{33}\,g_{44}\,g_{55}\,g_{66}\,g_{77}
$$

(the determinant of a diagonal matrix is the product of its diagonal entries)

$$
= e^{-2a_4}b_4\cot^2 z\cdot\big(e^{2a_4}\big)^3\cdot(-1)\cdot\big(-e^{-2a_4}b_4w_z^2\big)^3
$$

(the entries inserted; three equal factors written as a cube)

$$
= (-1)(-1)^3\; e^{-2a_4}e^{6a_4}e^{-6a_4}\; b_4\,b_4^3\; \cot^2 z\; w_z^6
$$

(the power of a product is the product of the powers, $(xy)^3 = x^3y^3$, and $(e^{y})^3 = e^{3y}$)

$$
= e^{-2a_4}\,b_4^4\,\cot^2 z\,(\sin^2 z)^{1/2}
$$

($(-1)(-1)^3 = (-1)^4 = 1$; the exponents add, $-2 + 6 - 6 = -2$; $w_z^6 = (\sin^2 z)^{6/12}$). Notebook 12a prints it as `bb**4*w**6/(ea**2*t**2)` with `ea` $= e^{a_4}$, `bb` $= b_4$, `t` $= \tan z$ and `w` $= w_z$ (In [4]). The determinant is positive, so $|\det g| = \det g$ and

$$
\sqrt{|\det g|} = e^{-a_4}\,b_4^2\,|\cot z|\,(\sin^2 z)^{1/4}
$$

(the square root of a product is the product of the square roots, $\sqrt{\cot^2 z} = |\cot z|$ and $\sqrt{(\sin^2 z)^{1/2}} = (\sin^2 z)^{1/4}$). This is PROVED (Wolfram report, check `sqrt_abs_det_g`; Notebook 12a, In [4]).

**The volume changes.** At a fixed $x_0$ the logarithm of the volume factor changes at the rate

$$
\frac{d}{dx_4}\ln\sqrt{|\det g|} = \frac{d}{dx_4}\big(-a_4 + 2\ln b_4\big) = 2u - a_4'
$$

($\ln$ turns the product into a sum, and the factors with $z$ do not depend on $x_4$; then the chain rule). The same rate is the sum of the rates of the seven directions other than the time: $3a_4'$ from 3-space and $4h$ from the block, and indeed

$$
3a_4' + 4h = 3a_4' + 4\big(\tfrac12u - a_4'\big) = 2u - a_4'
$$

(the definition of $h$ inserted and the terms collected). This is PROVED (field-theory report, check `sqrt_det_g`; Notebook 12a, In [4]). On the record history the rate is $2\cdot\tfrac43H - H = \tfrac53H > 0$: what the block loses, 3-space more than gains. In the corrected metric the volume factor is constant only on histories with $2u = a_4'$, that is $b_4 \propto e^{a_4/2}$. (As dated history: in the metric of 2026-10-14, withdrawn on 2026-10-16, the volume factor was $b_4^{3/2}\cos z$, which did not contain $a_4$; `Revision/SPEC.md`, section 1.)

### 12.4 The Christoffel symbols of the corrected metric

**Definition.** For any metric the Christoffel symbols are

$$
\Gamma^a{}_{bc} = \frac12\sum_{d} g^{ad}\big(\partial_b g_{dc} + \partial_c g_{db} - \partial_d g_{bc}\big),
$$

where $\partial_b$ is the partial derivative with respect to the coordinate $x_b$ and $d$ runs over the eight directions. They are symmetric in the two lower indices, $\Gamma^a{}_{bc} = \Gamma^a{}_{cb}$, because exchanging $b$ and $c$ exchanges the first two terms in the bracket.

**The formula for a diagonal metric.** We simplify the definition for our metric, line by line.

$$
\Gamma^a{}_{bc} = \frac{1}{2g_{aa}}\big(\partial_b g_{ac} + \partial_c g_{ab} - \partial_a g_{bc}\big)
$$

(the inverse metric is diagonal, so in the sum over $d$ only $d = a$ survives, and $g^{aa} = 1/g_{aa}$; no sum over $a$)

$$
\Gamma^a{}_{bc} = \frac{1}{2g_{aa}}\big(\delta_{ac}\,\partial_b g_{aa} + \delta_{ab}\,\partial_c g_{aa} - \delta_{bc}\,\partial_a g_{bb}\big)
$$

(an entry $g_{ac}$ of a diagonal matrix is $g_{aa}$ when $c = a$ and 0 otherwise; the Kronecker delta $\delta_{ac}$ is 1 when $a = c$ and 0 otherwise). This is the formula that Notebook 12a programs in In [5].

**The derivatives of the metric.** The metric depends on $x_4$ (through $a_4$ and $b_4$) and on $x_0$ (through $z$) only; every other partial derivative is zero. By the chain rule $\partial_0 = (dz/dx_0)\,\partial_z = 6H\,\partial_z$. It is easiest to differentiate logarithms, $\partial\,g_{aa} = g_{aa}\,\partial\ln|g_{aa}|$:

- $\partial_4\ln g_{11} = \partial_4(2a_4) = 2a_4'$; the same for $g_{22}, g_{33}$.
- $\partial_4\ln g_{00} = \partial_4\big(-2a_4 + \ln b_4\big) = -2a_4' + u = 2h$, and in the same way $\partial_4\ln|g_{55}| = 2h$; the same for $g_{66}, g_{77}$.
- $\partial_0\ln g_{00} = 6H\,\partial_z\ln\cot^2 z = 6H\cdot\dfrac{2\cdot(-1/\sin^2 z)}{\cot z} = -\dfrac{12H}{\sin z\cos z}$ (chain rule, with $d\cot z/dz = -1/\sin^2 z$ and $\sin^2 z\cot z = \sin z\cos z$).
- $\partial_0\ln|g_{55}| = 6H\,\partial_z\tfrac16\ln\sin^2 z = 6H\cdot\tfrac16\cdot 2\cot z = 2H\cot z$; the same for $g_{66}, g_{77}$.
- $g_{11}$ does not depend on $x_0$, and $g_{44} = -1$ is constant.

**The symbols.** Inserting these into the diagonal formula, with $t$ for an extra time ($x_5$, $x_6$ or $x_7$) and $i$ for a 3-space direction:

- $\Gamma^{x_0}{}_{x_0x_0} = \tfrac12\partial_0\ln g_{00} = -\dfrac{6H}{\sin z\cos z}$ (all three terms have $a = b = c = x_0$; sympy prints `-6*H*(t**2 + 1)/t` with $t = \tan z$, because $(1 + \tan^2 z)/\tan z = 1/(\sin z\cos z)$).
- $\Gamma^{x_0}{}_{x_0x_4} = \Gamma^{x_0}{}_{x_4x_0} = \tfrac12\partial_4\ln g_{00} = h$ (the term with $\delta_{ac}$, $a = c = x_0$, $b = x_4$; printed `-(2*ad1 - uu)/2`).
- $\Gamma^{x_0}{}_{tt} = -\dfrac{\partial_0 g_{tt}}{2g_{00}} = -\dfrac{2H\cot z\,g_{tt}}{2g_{00}} = H\tan z\,w_z^2$ (the term with $\delta_{bc}$; $g_{tt}/g_{00} = -w_z^2/\cot^2 z$ and $\cot z/\cot^2 z = \tan z$; printed `H*t*w**2`).
- $\Gamma^{i}{}_{ix_4} = \Gamma^{i}{}_{x_4i} = \tfrac12\partial_4\ln g_{ii} = a_4'$.
- $\Gamma^{x_4}{}_{x_0x_0} = -\dfrac{\partial_4 g_{00}}{2g_{44}} = \tfrac12\partial_4 g_{00} = h\,g_{00} = h\,e^{-2a_4}b_4\cot^2 z$ (the term with $\delta_{bc}$ and $g_{44} = -1$).
- $\Gamma^{x_4}{}_{ii} = \tfrac12\partial_4 g_{ii} = a_4'\,e^{2a_4}$.
- $\Gamma^{x_4}{}_{tt} = \tfrac12\partial_4 g_{tt} = h\,g_{tt} = -h\,e^{-2a_4}b_4w_z^2$.
- $\Gamma^{t}{}_{x_0t} = \Gamma^{t}{}_{tx_0} = \tfrac12\partial_0\ln|g_{tt}| = H\cot z$ (printed `H/t`).
- $\Gamma^{t}{}_{x_4t} = \Gamma^{t}{}_{tx_4} = \tfrac12\partial_4\ln|g_{tt}| = h$.

**Counting.** With $b \le c$ there are $1 + 1 + 3 + 3 + 1 + 3 + 3 + 3 + 3 = 21$ different symbols (the nine lines above, the last eight counted for each 3-space direction or each extra time where they carry an $i$ or a $t$). Ten of them have $b \ne c$ ($\Gamma^{x_0}{}_{x_0x_4}$, the three $\Gamma^i{}_{ix_4}$, the three $\Gamma^t{}_{x_0t}$ and the three $\Gamma^t{}_{x_4t}$) and appear twice among the 512 symbols, so 31 of the 512 are not zero. Every other symbol is zero; for example $\Gamma^{e}{}_{x_4x_4} = 0$ for every $e$, because $g_{44}$ is constant, and $\Gamma^{x_0}{}_{ii} = \Gamma^i{}_{ix_0} = 0$, because 3-space has no factor that depends on $x_0$. This is PROVED (field-theory report, check `christoffel_count`; Notebook 12a, In [5], which also checks the symmetry, and In [6], which prints the 21 symbols).

The symbols already show the structure of the metric: the hidden direction and the extra times carry the same rate $h$ in every symbol with an index $x_4$, exactly as the three 3-space directions carry the rate $a_4'$.

### 12.5 The curvature computed by hand

**Definition (the convention of Misner, Thorne and Wheeler, MTW).**

$$
R^a{}_{bmn} = \partial_m\Gamma^a{}_{bn} - \partial_n\Gamma^a{}_{bm} + \sum_{e}\Gamma^a{}_{me}\Gamma^e{}_{bn} - \sum_{e}\Gamma^a{}_{ne}\Gamma^e{}_{bm},
\qquad R^{ab}{}_{mn} = g^{bb}\,R^a{}_{bmn}\ \ (\text{no sum}).
$$

The tensor $R^{ab}{}_{mn}$ changes sign when $a$ and $b$ are exchanged, and when $m$ and $n$ are exchanged (sympy report, check `riemann_pair_antisymmetry`). So it is zero when $a = b$ or $m = n$, and the **sectional curvature** $K_{ab} = R^{ab}{}_{ab}$ (no sum) is symmetric, $K_{ba} = R^{ba}{}_{ba} = (-1)(-1)R^{ab}{}_{ab} = K_{ab}$. The eight directions form $8\cdot 7/2 = 28$ planes. We compute six sectional curvatures by hand.

**A 3-space direction and the time.** Take $a = m = x_1$ and $b = n = x_4$:

$$
R^{x_1}{}_{x_4x_1x_4} = \partial_1\Gamma^{x_1}{}_{x_4x_4} - \partial_4\Gamma^{x_1}{}_{x_4x_1} + \sum_e\Gamma^{x_1}{}_{x_1e}\Gamma^e{}_{x_4x_4} - \sum_e\Gamma^{x_1}{}_{x_4e}\Gamma^e{}_{x_4x_1}
$$

(the definition with these indices)

$$
= 0 - a_4'' + 0 - a_4'\cdot a_4'
$$

(nothing depends on $x_1$; $\Gamma^{x_1}{}_{x_4x_1} = a_4'$ has the derivative $a_4''$; every $\Gamma^e{}_{x_4x_4}$ is zero; in the last sum only $e = x_1$ survives, with $\Gamma^{x_1}{}_{x_4x_1} = a_4'$ twice)

$$
K_{x_1x_4} = g^{44}\,R^{x_1}{}_{x_4x_1x_4} = (-1)\big(-a_4'' - (a_4')^2\big) = a_4'' + (a_4')^2
$$

(raise the index $x_4$ with $g^{44} = 1/g_{44} = -1$).

**Two 3-space directions.** With $a = m = x_1$ and $b = n = x_2$ the two derivative terms vanish ($\Gamma^{x_1}{}_{x_2x_2} = \Gamma^{x_1}{}_{x_2x_1} = 0$), and so does the last sum (every $\Gamma^{x_1}{}_{x_2e}$ is zero):

$$
R^{x_1}{}_{x_2x_1x_2} = \Gamma^{x_1}{}_{x_1x_4}\,\Gamma^{x_4}{}_{x_2x_2} = a_4'\cdot a_4'\,g_{22}
$$

(the only $e$ for which $\Gamma^{x_1}{}_{x_1e}$ is not zero is $e = x_4$; then the symbols of Section 12.4), so $K_{x_1x_2} = g^{22}R^{x_1}{}_{x_2x_1x_2} = (a_4')^2$.

**A 3-space direction and a block direction.** With $b = n = x_5$ the same single term remains:

$$
R^{x_1}{}_{x_5x_1x_5} = \Gamma^{x_1}{}_{x_1x_4}\,\Gamma^{x_4}{}_{x_5x_5} = a_4'\cdot h\,g_{55}
$$

(Section 12.4: $\Gamma^{x_4}{}_{x_5x_5} = h\,g_{55}$), so $K_{x_1x_5} = g^{55}R^{x_1}{}_{x_5x_1x_5} = a_4'h$. With $b = n = x_0$ instead, $\Gamma^{x_4}{}_{x_0x_0} = h\,g_{00}$ gives in the same way $K_{x_1x_0} = a_4'h$: towards 3-space the hidden direction behaves exactly like an extra time.

**The time and an extra time.** Take $a = m = x_4$ and $b = n = x_5$:

$$
R^{x_4}{}_{x_5x_4x_5} = \partial_4\Gamma^{x_4}{}_{x_5x_5} - \partial_5\Gamma^{x_4}{}_{x_5x_4} + \sum_e\Gamma^{x_4}{}_{x_4e}\Gamma^e{}_{x_5x_5} - \sum_e\Gamma^{x_4}{}_{x_5e}\Gamma^e{}_{x_5x_4}
$$

(the definition)

$$
= \partial_4\big(h\,g_{55}\big) - 0 + 0 - \Gamma^{x_4}{}_{x_5x_5}\,\Gamma^{x_5}{}_{x_5x_4}
$$

(nothing depends on $x_5$; every $\Gamma^{x_4}{}_{x_4e}$ is zero because $g_{44}$ is constant; in the last sum only $e = x_5$ survives)

$$
= h'\,g_{55} + h\cdot 2h\,g_{55} - h\,g_{55}\cdot h = \big(h' + h^2\big)\,g_{55}
$$

(product rule, with $\partial_4 g_{55} = 2h\,g_{55}$ from Section 12.4; then $\Gamma^{x_4}{}_{x_5x_5} = h\,g_{55}$ and $\Gamma^{x_5}{}_{x_5x_4} = h$), so $K_{x_4x_5} = g^{55}R^{x_4}{}_{x_5x_4x_5} = h' + h^2$. The same steps with $x_0$ in place of $x_5$ give $K_{x_4x_0} = h' + h^2$. This is the formula of the 3-space plane, $a_4'' + (a_4')^2$, with the rate $a_4'$ replaced by the block rate $h$.

**Two extra times.** With $a = m = x_5$ and $b = n = x_6$ the derivative terms and the last sum vanish, and two values of $e$ remain:

$$
R^{x_5}{}_{x_6x_5x_6} = \Gamma^{x_5}{}_{x_5x_0}\Gamma^{x_0}{}_{x_6x_6} + \Gamma^{x_5}{}_{x_5x_4}\Gamma^{x_4}{}_{x_6x_6}
$$

(the two values $e = x_0$ and $e = x_4$ for which $\Gamma^{x_5}{}_{x_5e}$ is not zero)

$$
= H\cot z\cdot H\tan z\,w_z^2 + h\cdot h\,g_{66} = H^2w_z^2 + h^2g_{66}
$$

(the symbols of Section 12.4, and $\cot z\tan z = 1$)

$$
K_{x_5x_6} = g^{66}R^{x_5}{}_{x_6x_5x_6} = \frac{H^2w_z^2}{-e^{-2a_4}b_4w_z^2} + h^2 = h^2 - H^2\,\frac{e^{2a_4}}{b_4} = h^2 - H^2k
$$

(raise with $g^{66} = 1/g_{66}$; $w_z^2$ cancels; the definition of $k$). The angle $z$ has disappeared. The term $-H^2k$ is the curvature of the block itself: a space of curvature $-H^2$, multiplied by the squared scale factor $e^{-2a_4}b_4 = 1/k$, has curvature $-H^2k$. The term $h^2$ comes from the change of the block in time, like $(a_4')^2$ for 3-space. A longer computation of the same kind gives $K_{x_0x_5} = h^2 - H^2k$ too (Exercise 2).

**All 28 planes.** The computation of Notebook 12a (In [9]) confirms these values and gives the rest. The 28 sectional curvatures fall into five groups:

| the plane | number of planes | sectional curvature $K$ | as printed by Notebook 12a |
| --- | --- | --- | --- |
| two 3-space directions | 3 | $(a_4')^2$ | `ad1**2` |
| a 3-space direction and the time | 3 | $a_4'' + (a_4')^2$ | `ad1**2 + ad2` |
| a 3-space direction and a block direction | 12 | $a_4'h$ | `-ad1*(2*ad1 - uu)/2` |
| the time and a block direction | 4 | $h' + h^2$ | `(4*ad1**2 - 4*ad1*uu - 4*ad2 + uu**2 + 2*vv)/4` |
| two block directions | 6 | $h^2 - H^2k$ | `-(4*H**2*kk - 4*ad1**2 + 4*ad1*uu - uu**2)/4` |

The last column is the same value in the record's variables: with $h = \tfrac12u - a_4'$ and $h' = \tfrac12v - a_4''$, for example $h' + h^2 = \tfrac12v - a_4'' + (a_4')^2 - a_4'u + \tfrac14u^2$, which is the printed fraction.

**No mixed component.** Besides these $4\times 28 = 112$ components (each sectional curvature appears with its four orderings $R^{ab}{}_{ab}$, $R^{ba}{}_{ab}$, $R^{ab}{}_{ba}$, $R^{ba}{}_{ba}$) the Riemann tensor has no nonzero component: every $R^{ab}{}_{mn}$ with $\{a, b\} \ne \{m, n\}$ vanishes. Two examples show why. In $R^{x_1}{}_{x_4x_1x_0}$ every term contains $\Gamma^{x_1}{}_{x_4x_0}$, $\partial_0\Gamma^{x_1}{}_{x_4x_1} = \partial_0a_4'$, $\Gamma^{x_4}{}_{x_4x_0}$ or $\Gamma^{x_1}{}_{x_0e}$, and all of them are zero, because 3-space has no factor that depends on $x_0$. In $R^{x_5}{}_{x_4x_5x_0}$ two terms survive and cancel:

$$
R^{x_5}{}_{x_4x_5x_0} = \Gamma^{x_5}{}_{x_5x_0}\Gamma^{x_0}{}_{x_4x_0} - \Gamma^{x_5}{}_{x_0x_5}\Gamma^{x_5}{}_{x_4x_5} = H\cot z\cdot h - H\cot z\cdot h = 0
$$

(the definition, keeping only the nonzero symbols; $\Gamma^{x_5}{}_{x_4x_5} = h$ does not depend on $x_0$, so $\partial_0\Gamma^{x_5}{}_{x_4x_5} = 0$). The cancellation happens because the hidden direction changes in time at the same rate $h$ as the extra times. So the curvature consists of the 28 sectional curvatures alone, none of which depends on $x_0$, and each is a polynomial in $H$, $a_4'$, $a_4''$, $u$, $v$ and $k$. All of this is PROVED: sympy report, checks `mixed_riemann_free_of_x0`, `mixed_riemann_only_sectional`, `riemann_entries_polynomial` and `riemann_pair_antisymmetry`; Wolfram report, check `mixed_riemann_free_of_x0`; metric report, check `corrected_mixed_riemann_vanish`; Notebook 12a reproduces them in In [7] and In [8].

### 12.6 The Ricci tensor, the Ricci scalar and the Einstein tensor by hand

**Definitions.**

$$
R^h{}_j = \sum_{a} R^{ah}{}_{aj},\qquad R = \sum_h R^h{}_h,\qquad G^h{}_j = R^h{}_j - \tfrac12\,\delta^h_j\,R .
$$

**Diagonal.** A component $R^{ah}{}_{aj}$ with $h \ne j$ would be a mixed Riemann component (its two pairs $\{a, h\}$ and $\{a, j\}$ differ), and Section 12.5 showed that all of these vanish. So $R^h{}_j = 0$ and $G^h{}_j = 0$ for $h \ne j$: the Einstein tensor is diagonal.

**A rule for the diagonal.** For $h = j$ the definition gives $R^h{}_h = \sum_a R^{ah}{}_{ah} = \sum_{a \ne h} K_{ah}$: the sum of the sectional curvatures of the seven planes that contain $x_h$. Summing over $h$ counts every plane twice (once from each of its two directions), so $R = 2\sum_{\text{planes}} K$. Therefore

$$
G^h{}_h = \sum_{\text{planes containing } x_h} K - \sum_{\text{all 28 planes}} K = -\sum_{\text{planes not containing } x_h} K
$$

(the definition of $G$ with the two sums inserted; the planes that contain $x_h$ cancel). With the table of Section 12.5 everything follows by counting.

**The Ricci scalar.** Adding the five groups, each with its number of planes:

$$
\sum_{\text{planes}} K = 3(a_4')^2 + 3\big(a_4'' + (a_4')^2\big) + 12\,a_4'h + 4\big(h' + h^2\big) + 6\big(h^2 - H^2k\big)
$$

(the table, row by row)

$$
= 6(a_4')^2 + 3a_4'' + 12a_4'h + 4h' + 10h^2 - 6H^2k
$$

(collect the terms with $(a_4')^2$, with $h^2$ and with $H^2k$), so $R = 12(a_4')^2 + 6a_4'' + 24a_4'h + 8h' + 20h^2 - 12H^2k$.

**The time component.** The planes that do not contain $x_4$ are the 3-space planes, the 3-space and block planes and the block planes:

$$
G^{x_4}{}_{x_4} = -\Big[3(a_4')^2 + 12\,a_4'h + 6\big(h^2 - H^2k\big)\Big] = -3(a_4')^2 - 12a_4'h - 6h^2 + 6H^2k
$$

(the rule; then the bracket multiplied out).

**The 3-space component.** The planes without $x_1$: one plane of two 3-space directions ($x_2x_3$), two of a 3-space direction and the time ($x_2x_4$, $x_3x_4$), $2\times 4 = 8$ of a 3-space direction ($x_2$ or $x_3$) and a block direction, the four planes of the time and a block direction, and the six block planes:

$$
G^{x_1}{}_{x_1} = -\Big[(a_4')^2 + 2\big(a_4'' + (a_4')^2\big) + 8a_4'h + 4\big(h' + h^2\big) + 6\big(h^2 - H^2k\big)\Big]
$$

(the rule)

$$
= -3(a_4')^2 - 2a_4'' - 8a_4'h - 4h' - 10h^2 + 6H^2k
$$

(the bracket multiplied out: $1 + 2 = 3$ times $(a_4')^2$ and $4 + 6 = 10$ times $h^2$).

**The block component.** The planes without $x_0$: the three 3-space planes, the three planes of 3-space and the time, $3\times 3 = 9$ planes of a 3-space direction and an extra time, the three planes of the time and an extra time, and the three planes of two extra times:

$$
G^{x_0}{}_{x_0} = -\Big[3(a_4')^2 + 3\big(a_4'' + (a_4')^2\big) + 9a_4'h + 3\big(h' + h^2\big) + 3\big(h^2 - H^2k\big)\Big]
$$

(the rule)

$$
= -6(a_4')^2 - 3a_4'' - 9a_4'h - 3h' - 6h^2 + 3H^2k
$$

(the bracket multiplied out). For $x_5$ the count is the same: the planes without $x_5$ are again 3 + 3 + 9 + 3 + 3 planes of the same five kinds, because $x_5$, like $x_0$, forms 3 planes with 3-space, one with the time and three with the other block directions. So $G^{x_5}{}_{x_5} = G^{x_0}{}_{x_0}$, and likewise for $x_6, x_7$; and $G^{x_2}{}_{x_2} = G^{x_3}{}_{x_3} = G^{x_1}{}_{x_1}$.

**In the record's variables.** The record writes these components with $u$ and $v$. We convert the time component, line by line:

$$
h = \tfrac12u - a_4',\qquad h^2 = \tfrac14u^2 - a_4'u + (a_4')^2,\qquad a_4'h = \tfrac12a_4'u - (a_4')^2
$$

(the definition of $h$; the square of a difference; the product with $a_4'$)

$$
G^{x_4}{}_{x_4} = -3(a_4')^2 - 12\big(\tfrac12a_4'u - (a_4')^2\big) - 6\big(\tfrac14u^2 - a_4'u + (a_4')^2\big) + 6H^2k
$$

(the three lines inserted)

$$
= (-3 + 12 - 6)(a_4')^2 + (-6 + 6)\,a_4'u - \tfrac32u^2 + 6H^2k = 3(a_4')^2 - \tfrac32u^2 + 6H^2k
$$

(collect the terms with $(a_4')^2$, with $a_4'u$ and with $u^2$). The same substitution, with $h' = \tfrac12v - a_4''$ in addition, turns the other two into the record's form:

$$
\begin{aligned}
G^{x_4}{}_{x_4} &= 3(a_4')^2 + 6H^2k - \tfrac32u^2, \\
G^{x_1}{}_{x_1} &= -5(a_4')^2 + 6a_4'u + 2a_4'' - \tfrac52u^2 - 2v + 6H^2k, \\
G^{x_0}{}_{x_0} &= -3(a_4')^2 + \tfrac32a_4'u - \tfrac32u^2 - \tfrac32v + 3H^2k,
\end{aligned}
$$

and $R = -12H^2k + 8(a_4')^2 - 2a_4'' - 8a_4'u + 5u^2 + 4v$. These are PROVED: sympy report, check `einstein_components`; lead's Einstein report, checks `einstein_off_diagonal_vanish`, `einstein_isotropy` and `einstein_diagonal_x0_independent`; field-theory report, check `ricci_scalar`; Notebook 12a reproduces all of them in In [11] and In [12].

**The record history.** With $a_4' = H$, $a_4'' = 0$, $u = \tfrac43H$, $v = 0$:

$$
G^{x_4}{}_{x_4} = 3H^2 + 6H^2k - \tfrac32\cdot\tfrac{16}{9}H^2 = \big(3 - \tfrac83\big)H^2 + 6H^2k = \tfrac13H^2 + 6H^2k
$$

(the values inserted; $\tfrac32\cdot\tfrac{16}{9} = \tfrac83$), and in the same way $G^{x_1}{}_{x_1} = -5H^2 + 8H^2 - \tfrac{40}{9}H^2 + 6H^2k = -\tfrac{13}{9}H^2 + 6H^2k$ and $G^{x_0}{}_{x_0} = -3H^2 + 2H^2 - \tfrac83H^2 + 3H^2k = -\tfrac{11}{3}H^2 + 3H^2k$. With $H = 1$ these are the three lines `(18*kk + 1)/3`, `(54*kk - 13)/9` and `(9*kk - 11)/3` of Notebook 12a, In [13]. They grow with $k = e^{(2/3)Hx_4}$, that is, as the block shrinks.

### 12.7 The Lovelock tensors: the Einstein tensor and its two companions

**The generalized Kronecker delta.** For two lists of $n$ indices, $\delta^{h_1\dots h_n}_{j_1\dots j_n}$ is the determinant of the $n$ by $n$ matrix whose entry in row $r$ and column $c$ is the ordinary Kronecker delta $\delta^{h_r}_{j_c}$. Two equal upper indices give two equal rows and the determinant 0. Otherwise it is $+1$ if the lower list is an even rearrangement of the upper list (an even number of exchanges turns one into the other), $-1$ if it is an odd one, and $0$ if the two lists do not hold the same indices (Chapter 1 and Chapter 11 prove this).

**The Lovelock tensors** (formula (4.38) of the book by Lovelock and Rund, as programmed in the record, with a sum over every repeated index):

$$
P_{(k)}{}^h{}_j = \delta^{h\,h_1\dots h_{2k}}_{j\,j_1\dots j_{2k}}\;R^{j_1j_2}{}_{h_1h_2}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}},\qquad
E_{(k)}{}^h{}_j = -\frac{P_{(k)}{}^h{}_j}{2^{k+1}} .
$$

**Only $k = 1, 2, 3$.** For $k = 4$ the delta has $2k + 1 = 9$ upper indices taking only 8 values; two must be equal, so $P_{(4)} = 0$ (PROVED: Wolfram report, check `P4_vanishes_pigeonhole`; Notebook 12a, In [14]). In eight dimensions there are exactly three Lovelock tensors.

**The sum collapses for the corrected metric.** Section 12.5 showed that every nonzero Riemann component is sectional: $R^{j_1j_2}{}_{h_1h_2}$ vanishes unless $\{j_1, j_2\} = \{h_1, h_2\}$. We use this to evaluate $P_{(k)}$ in general, line by line.

$$
P_{(k)}{}^h{}_j = \sum \delta^{h\,h_1\dots h_{2k}}_{j\,j_1\dots j_{2k}}\;R^{j_1j_2}{}_{h_1h_2}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}}
$$

(the definition, with the sum over all $h_1, \dots, h_{2k}$ and $j_1, \dots, j_{2k}$ written out). A term is nonzero only when every factor is sectional, so $\{j_{2r-1}, j_{2r}\} = \{h_{2r-1}, h_{2r}\}$ for $r = 1, \dots, k$, and only when the upper list $h, h_1, \dots, h_{2k}$ has no repeated index (otherwise the delta is 0).

$$
\{j_1, \dots, j_{2k}\} = \{h_1, \dots, h_{2k}\}\quad\Longrightarrow\quad j = h
$$

(the lower list must be a rearrangement of the upper list; its last $2k$ entries already use up $h_1, \dots, h_{2k}$, so the first must be $h$). So $P_{(k)}{}^h{}_j = 0$ for $h \ne j$: **every Lovelock tensor of the corrected metric is diagonal.** For $h = j$ each factor has two orders of its lower pair: $(j_{2r-1}, j_{2r}) = (h_{2r-1}, h_{2r})$, with the value $K_{h_{2r-1}h_{2r}}$, or the exchanged pair, with the value $-K$ and one more exchange in the delta (sign $-1$); both orders give the same contribution $+K$.

$$
P_{(k)}{}^h{}_h = \sum_{h_1, \dots, h_{2k}} 2^k\,K_{h_1h_2}K_{h_3h_4}\cdots K_{h_{2k-1}h_{2k}}
$$

(the factor $2^k$ counts the two orders of each of the $k$ lower pairs; with the lower list equal to the upper list the delta is $+1$; the sum runs over the ordered lists of $2k$ different indices, all different from $h$). The same set of $k$ planes appears in $k!$ orders of the planes, and each plane in 2 orders of its two indices:

$$
P_{(k)}{}^h{}_h = k!\,2^k\cdot 2^k\sum_{\text{sets of } k \text{ disjoint planes without } x_h}\ \prod K = k!\,4^k\sum\prod K
$$

(every unordered set of $k$ disjoint planes, none containing $x_h$, counted $k!\,2^k$ times; "disjoint" means that no two planes share a direction). Dividing by $-2^{k+1}$:

$$
E_{(k)}{}^h{}_h = -\frac{k!\,4^k}{2^{k+1}}\sum\prod K = -k!\,2^{k-1}\sum_{\text{sets of } k \text{ disjoint planes without } x_h}\ \prod K
$$

(the definition of $E_{(k)}$; $4^k/2^{k+1} = 2^{2k - k - 1} = 2^{k-1}$). For $k = 1$ this is $E_{(1)}{}^h{}_h = -\sum K$ over the planes without $x_h$: the rule of Section 12.6 for $G^h{}_h$. So $E_{(1)} = G$, the Einstein tensor (PROVED: sympy report, check `P1_equals_minus_4_Einstein`; Wolfram report, check `P1_direct_equals_minus_4_Einstein`; Notebook 12a, In [16], which also checks the formula for $k = 1, 2, 3$ in all eight diagonal components). For $k = 2$ the prefactor is $-2!\,2 = -4$, for $k = 3$ it is $-3!\,4 = -24$.

**An example by hand: $E_{(2)}{}^{x_4}{}_{x_4}$.** The planes without $x_4$ are built from the seven directions $x_1, x_2, x_3$ (call this set $S$) and $x_0, x_5, x_6, x_7$ (the block, set $T$). With the table of Section 12.5 they are of three kinds: $SS$ (3 planes, $K = (a_4')^2$), $ST$ (12 planes, $K = a_4'h$) and $TT$ (6 planes, $K = D$ with the abbreviation $D = h^2 - H^2k$). We count the unordered pairs of disjoint planes of each combination.

| the two planes | how many pairs | product of the two $K$ |
| --- | --- | --- |
| $SS$ and $ST$ | $3\cdot 1\cdot 4 = 12$ | $(a_4')^2\cdot a_4'h$ |
| $SS$ and $TT$ | $3\cdot 6 = 18$ | $(a_4')^2 D$ |
| $ST$ and $ST$ | $3\cdot 4\cdot 3 = 36$ | $(a_4'h)^2$ |
| $ST$ and $TT$ | $3\cdot 4\cdot 3 = 36$ | $a_4'h\,D$ |
| $TT$ and $TT$ | $3$ | $D^2$ |

(For $SS$ and $ST$: the $SS$ plane uses two of the three 3-space directions, the $ST$ plane must use the third one and any of the 4 block directions. Two disjoint $SS$ planes would need four 3-space directions, so that row is absent. For two $ST$ planes: choose the two 3-space directions, 3 ways, and give them two different block directions, $4\cdot 3$ ways. For $ST$ and $TT$: the $ST$ plane, $3\cdot 4$ ways, and a $TT$ plane from the 3 remaining block directions, 3 ways. Two disjoint $TT$ planes split the four block directions into two pairs, 3 ways.) The counts add up to $12 + 18 + 36 + 36 + 3 = 105$, the number of unordered pairs of disjoint planes among seven directions, $\binom72\binom52/2 = 21\cdot 10/2 = 105$. With the prefactor $-4$:

$$
E_{(2)}{}^{x_4}{}_{x_4} = -4\Big[12(a_4')^3h + 18(a_4')^2D + 36(a_4')^2h^2 + 36\,a_4'h\,D + 3D^2\Big]
$$

(the collapsed formula with the table). On the record history $a_4' = H$, $u = \tfrac43H$, so $h = \tfrac23H - H = -\tfrac13H$ and $D = \tfrac19H^2 - H^2k$. With $H = 1$ the five terms are

$$
\begin{aligned}
&12\cdot\big(-\tfrac13\big) = -4,\qquad 18\big(\tfrac19 - k\big) = 2 - 18k,\qquad 36\cdot\tfrac19 = 4,\\
&36\cdot\big(-\tfrac13\big)\big(\tfrac19 - k\big) = -\tfrac43 + 12k,\qquad 3\big(\tfrac19 - k\big)^2 = \tfrac1{27} - \tfrac23k + 3k^2
\end{aligned}
$$

(each value inserted and multiplied out; $(\tfrac19 - k)^2 = \tfrac1{81} - \tfrac29k + k^2$). Their sum is

$$
\Big(-4 + 2 + 4 - \tfrac43 + \tfrac1{27}\Big) + \Big(-18 + 12 - \tfrac23\Big)k + 3k^2 = \tfrac{19}{27} - \tfrac{20}{3}k + 3k^2
$$

(the constants and the multiples of $k$ collected; $2 - \tfrac43 + \tfrac1{27} = \tfrac{54 - 36 + 1}{27}$), so

$$
E_{(2)}{}^{x_4}{}_{x_4} = -4\Big(\tfrac{19}{27} - \tfrac{20}{3}k + 3k^2\Big) = -12k^2 + \tfrac{80}{3}k - \tfrac{76}{27}
$$

(multiplied by $-4$). This equals the record's general component (below) on the record history. The same counting for $k = 3$ uses the 105 sets of three disjoint planes without $x_4$ (Exercise 4): it gives $E_{(3)}{}^{x_4}{}_{x_4} = -216k^2 - 144k + 40$ on the record history.

**The record's components.** Written out in the record's variables (record `Revision/field_equations_a4/a4-equations.json`, key `lovelockTensors`; $x_2, x_3$ equal to $x_1$; $x_5, x_6, x_7$ equal to $x_0$; every off-diagonal component zero), $E_{(1)}$ is the Einstein tensor of Section 12.6, and

$$
\begin{aligned}
E_{(2)}{}^{x_4}{}_{x_4} &= -36 (a_4')^4-48 (a_4')^2 H^2 k+36 (a_4')^2 u^2+48 a_4' H^2 k u-12 a_4' u^3-12 H^4 k^2+6 H^2 k u^2-\tfrac{3}{4}u^4, \\
E_{(2)}{}^{x_1}{}_{x_1} &= 28 (a_4')^4-48 (a_4')^3 u-48 (a_4')^2 a_4''+48 (a_4')^2 H^2 k+20 (a_4')^2 u^2+16 (a_4')^2 v+32 a_4' a_4'' u \\
&\quad -24 a_4' H^2 k u+6 a_4' u^3-12 H^4 k^2+18 H^2 k u^2+24 H^2 k v-\tfrac{15}{4}u^4-6 u^2 v, \\
E_{(2)}{}^{x_0}{}_{x_0} &= 12 (a_4')^4-12 (a_4')^3 u+48 (a_4')^2 H^2 k+18 (a_4')^2 u^2+12 (a_4')^2 v+24 a_4' a_4'' u+6 a_4' H^2 k u \\
&\quad -\tfrac{15}{2}a_4' u^3-12 a_4' u v+24 a_4'' H^2 k-6 a_4'' u^2+3 H^2 k u^2+6 H^2 k v-\tfrac{3}{4}u^4-\tfrac{3}{2}u^2 v,
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_4}{}_{x_4} &= 360 (a_4')^6+432 (a_4')^4 H^2 k-540 (a_4')^4 u^2-864 (a_4')^3 H^2 k u+360 (a_4')^3 u^3 \\
&\quad -216 (a_4')^2 H^4 k^2+324 (a_4')^2 H^2 k u^2-\tfrac{135}{2}(a_4')^2 u^4, \\
E_{(3)}{}^{x_1}{}_{x_1} &= -216 (a_4')^6+432 (a_4')^5 u+720 (a_4')^4 a_4''-144 (a_4')^4 H^2 k-180 (a_4')^4 u^2 \\
&\quad -144 (a_4')^4 v-576 (a_4')^3 a_4'' u+144 (a_4')^3 H^2 k u-108 (a_4')^3 u^3-216 (a_4')^2 H^4 k^2 \\
&\quad -180 (a_4')^2 H^2 k u^2-144 (a_4')^2 H^2 k v+\tfrac{189}{2}(a_4')^2 u^4+108 (a_4')^2 u^2 v \\
&\quad -288 a_4' a_4'' H^2 k u+72 a_4' a_4'' u^3+72 a_4' H^2 k u^3+144 a_4' H^2 k u v-18 a_4' u^5 \\
&\quad -36 a_4' u^3 v-144 a_4'' H^4 k^2+72 a_4'' H^2 k u^2-9 a_4'' u^4, \\
E_{(3)}{}^{x_0}{}_{x_0} &= -72 (a_4')^6+108 (a_4')^5 u-216 (a_4')^4 H^2 k-216 (a_4')^4 u^2-108 (a_4')^4 v \\
&\quad -432 (a_4')^3 a_4'' u+108 (a_4')^3 H^2 k u+171 (a_4')^3 u^3+216 (a_4')^3 u v \\
&\quad -432 (a_4')^2 a_4'' H^2 k+324 (a_4')^2 a_4'' u^2+54 (a_4')^2 H^2 k u^2+108 (a_4')^2 H^2 k v \\
&\quad -\tfrac{81}{2}(a_4')^2 u^4-81 (a_4')^2 u^2 v+216 a_4' a_4'' H^2 k u-54 a_4' a_4'' u^3 .
\end{aligned}
$$

Inserting $a_4' = 1$, $u = \tfrac43$, $a_4'' = v = 0$ ($H = 1$) into the first line gives $-36 - 48k + 64 + 64k - \tfrac{256}{9} - 12k^2 + \tfrac{32}{3}k - \tfrac{64}{27}$, which collects to $-12k^2 + \tfrac{80}{3}k - \tfrac{76}{27}$, the hand result above. All of this is PROVED: the components computed from the curvature equal the Rust GKD record monomial by monomial (sympy report, checks `P1_equals_gkd_branch_monomials` to `P3_equals_gkd_branch_monomials`; Wolfram report, checks `P1_direct_equals_gkd_branch_monomials` to `P3_direct_equals_gkd_branch_monomials`); each $E_{(k)}$ is diagonal, free of $x_0$, equal in $x_1, x_2, x_3$ and equal in $x_0, x_5, x_6, x_7$ (checks `P1_structure` to `P3_structure` in both reports); each has zero divergence (checks `E1_divergence_free` to `E3_divergence_free` in both reports); and $E_{(2)}$ equals the classical Gauss-Bonnet tensor of Lanczos, which uses no GKD (Notebook 12a, In [18], for every $a_4$ and $b_4$; on the exponential histories also the lead's Einstein report, check `gauss_bonnet_diagonal`). Notebook 12a reproduces every one of these checks in In [16] to In [19]. That every divergence-free tensor built from the metric and its first and second derivatives is a combination of these tensors and $\delta^\mu_\nu$ is Lovelock's theorem (D. Lovelock, J. Math. Phys. 12, 498 (1971)), which this book quotes and does not prove.

Two structural facts can be read off at once. First, no component contains $a_4$, $b_4$ or $z$ themselves: only the rates $a_4'$, $u$, their derivatives $a_4''$, $v$, and $k = e^{2a_4}/b_4$, which enters with $H^2$ through the block curvature $-H^2k$. Second, $E^{x_0}{}_{x_0} = E^{x_5}{}_{x_5}$ for every order: towards every other direction the hidden direction behaves exactly like an extra time (the table of Section 12.5, where $x_0$ sits in the same rows as $x_5$, $x_6$, $x_7$).

### 12.8 The source and the independent field equations

**The field equations of Einstein-Lovelock gravity** are

$$
\sum_{k=1}^{3}\alpha_k\,E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu ,
$$

64 equations, one for each pair $(\mu, \nu)$. The left-hand side is built from the metric; the right-hand side is the source. We allow a general source with a diagonal part and the two mixed components of the time and the hidden direction:

$$
T^\mu{}_\nu = \mathrm{diag}\big(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t\big) + q_{40}\ (\mu = x_4, \nu = x_0) + q_{04}\ (\mu = x_0, \nu = x_4)
$$

(in the order $x_0, \dots, x_7$). The minus sign in $T^{x_4}{}_{x_4} = -\rho$ comes from $g^{44} = -1$: the energy density is the component $T_{44}$ with both indices down, and raising the first index multiplies it by $g^{44}$ (the convention of the record, key `conventions/source`; the pressures are $p_\mu = T^\mu{}_\mu$, no sum).

**Reduction.** Three facts of Section 12.7 reduce the 64 equations.

1. Every off-diagonal left-hand side is zero. So the off-diagonal equations read $0 = \kappa T^\mu{}_\nu$: the source must have $q_{40} = q_{04} = 0$ and no other mixed component.
2. The left-hand sides of $x_1, x_2, x_3$ are equal, and those of $x_0, x_5, x_6, x_7$ are equal. So the source must have one pressure for 3-space and ONE pressure for the hidden direction and the extra times together: $p_0 = p_t$.
3. No left-hand side depends on $x_0$. So no part of the source may depend on $x_0$.

What remains are three equations. With the abbreviations $e_{hh} = \sum_k \alpha_k E_{(k)}{}^h{}_h$ (no $\Lambda$; Notebook 12a calls them `e44`, `e11`, `e00`):

$$
\begin{aligned}
&\text{constraint } (x_4): & e_{44} + \Lambda &= -\kappa\rho, \\
&\text{3-space } (x_1 = x_2 = x_3): & e_{11} + \Lambda &= \kappa p_3, \\
&\text{block } (x_0 = x_5 = x_6 = x_7): & e_{00} + \Lambda &= \kappa p_0 = \kappa p_t .
\end{aligned}
$$

This is PROVED (Wolfram report, check `independent_components`; sympy report, check `independent_components`; record `a4-equations.json`, keys `generalSource/hiddenEqualsExtraTimes`, `generalSource/offDiagonal` and `generalSource/x0_dependence`; reproduced in Notebook 12a, In [21]). As dated history: the metric of 2026-10-14, withdrawn on 2026-10-16, had an off-diagonal component $E_{(k)}{}^{x_4}{}_{x_0}$ proportional to $\cot z\,b_4'/b_4$ at every order, which forced a mixed source component unless $b_4$ was constant (`Revision/SPEC.md`, section 1); removing it was the reason for the corrected metric.

### 12.9 The constraint and the two equations of second order

**Einstein gravity first.** With $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$ the three abbreviations are the Einstein components of Section 12.6:

$$
\begin{aligned}
e_{44} &= 3(a_4')^2 + 6H^2k - \tfrac32u^2,\\
e_{11} &= -5(a_4')^2 + 6a_4'u + 2a_4'' - \tfrac52u^2 - 2v + 6H^2k,\\
e_{00} &= -3(a_4')^2 + \tfrac32a_4'u - \tfrac32u^2 - \tfrac32v + 3H^2k .
\end{aligned}
$$

The time component contains the rates $a_4'$ and $u$ but no $a_4''$ and no $v$: it is a **constraint**, a condition on the first derivatives at each moment. The other two contain $a_4''$ and $v$, each to the first power. We write them as

$$
e_{11} = 2a_4'' - 2v + R_1,\qquad e_{00} = -\tfrac32v + R_0,
$$

with the parts without second derivatives $R_1 = -5(a_4')^2 + 6a_4'u - \tfrac52u^2 + 6H^2k$ and $R_0 = -3(a_4')^2 + \tfrac32a_4'u - \tfrac32u^2 + 3H^2k$ (the terms sorted). The block equation $e_{00} + \Lambda = \kappa p_0$ then gives $v$, line by line:

$$
-\tfrac32v + R_0 + \Lambda = \kappa p_0
$$

(the block equation with $e_{00}$ inserted)

$$
v = -\tfrac23\big(\kappa p_0 - \Lambda - R_0\big)
$$

($R_0 + \Lambda$ moved to the right, then both sides multiplied by $-\tfrac23$). The 3-space equation gives $a_4''$:

$$
2a_4'' - 2v + R_1 + \Lambda = \kappa p_3 \quad\Longrightarrow\quad a_4'' = v + \tfrac12\big(\kappa p_3 - \Lambda - R_1\big)
$$

($2v - R_1 - \Lambda$ moved to the right, then divided by 2). So, given the pressures and the first derivatives at one moment, the two equations give the second derivatives $a_4''$ and $v = (b_4'/b_4)'$ at that moment: they are **two equations of second order**, and with starting values of $a_4$, $a_4'$, $b_4$ and $u$ they determine the future (Section 12.21). In matrix form,

$$
J\begin{pmatrix}a_4''\\ v\end{pmatrix} = \begin{pmatrix}\kappa p_3 - \Lambda - R_1\\ \kappa p_0 - \Lambda - R_0\end{pmatrix},\qquad
J = \begin{pmatrix}2 & -2\\ 0 & -\tfrac32\end{pmatrix},\qquad \det J = 2\cdot\big(-\tfrac32\big) - (-2)\cdot 0 = -3
$$

(the **Jacobian** $J$ holds the coefficients of $a_4''$ and $v$; the determinant of a 2 by 2 matrix is the product of the diagonal minus the product of the other two entries). Because $v = b_4''/b_4 - u^2$, the coefficients with respect to $b_4''$ instead of $v$ are those of the second column divided by $b_4$: $\begin{pmatrix}2 & -2/b_4\\ 0 & -3/(2b_4)\end{pmatrix}$. All of this is PROVED (sympy report, checks `einstein_components` and `constraint_first_order`; Wolfram report, checks `second_order_system_a4pp_vv` and `einstein_second_order_system`; Notebook 12a, In [12] and In [22]).

**Einstein-Lovelock gravity.** The same structure holds for every coupling (record `a4-equations.json`, key `generalSource/secondOrderSystem`): $e_{44}$ contains no $a_4''$ and no $v$, and $e_{11}$, $e_{00}$ are linear in $(a_4'', v)$, with a Jacobian whose entries depend on $a_4'$, $u$, $k$ and the couplings. For Einstein-Gauss-Bonnet gravity ($\alpha_1 = 1$, $\alpha_3 = 0$) the record's Jacobian (key `generalSource/secondOrderJacobian`) is

$$
J = \begin{pmatrix} 2 - 48\alpha_2(a_4')^2 + 32\alpha_2a_4'u & -2\big(1 - 8\alpha_2(a_4')^2 - 12\alpha_2H^2k + 3\alpha_2u^2\big)\\
6\alpha_2\big(4H^2k + 4a_4'u - u^2\big) & -\tfrac32\big(1 - 8\alpha_2(a_4')^2 - 4\alpha_2H^2k + 8\alpha_2a_4'u + \alpha_2u^2\big)\end{pmatrix}.
$$

On the record history ($a_4' = 1$, $u = \tfrac43$, $H = 1$) the four entries are

$$
J_{11} = 2 - \tfrac{16}3\alpha_2,\quad J_{12} = -2\big(1 - \tfrac83\alpha_2 - 12\alpha_2k\big),\quad J_{21} = \alpha_2\big(24k + \tfrac{64}3\big),\quad J_{22} = -\tfrac32\big(1 + \tfrac{40}9\alpha_2 - 4\alpha_2k\big)
$$

(the values inserted: $-48 + \tfrac{128}3 = -\tfrac{16}3$; $-8 + \tfrac{16}3 = -\tfrac83$; $6(\tfrac{16}3 - \tfrac{16}9) = \tfrac{64}3$; $-8 + \tfrac{32}3 + \tfrac{16}9 = \tfrac{40}9$). Multiplying out $J_{11}J_{22} - J_{12}J_{21}$ and collecting the powers of $\alpha_2$ gives

$$
\begin{aligned}
\det J &= -3 + \big(60k + \tfrac{112}3\big)\alpha_2 - \big(576k^2 + 672k + \tfrac{704}9\big)\alpha_2^2\\
&= -\tfrac19\Big[27 - (540k + 336)\alpha_2 + (5184k^2 + 6048k + 704)\alpha_2^2\Big]
\end{aligned}
$$

(the product $J_{11}J_{22} = -3 - \tfrac{16}3\alpha_2 + 12k\alpha_2 - \tfrac{576k - 640}{18}\alpha_2^2$, the product $J_{12}J_{21} = -(48k + \tfrac{128}3)\alpha_2 + 2(288k^2 + 320k + \tfrac{512}9)\alpha_2^2$, and their difference; then $-\tfrac19$ taken out). The bracket is a quadratic polynomial in $\alpha_2$; it has a real zero only if its discriminant is not negative:

$$
(540k + 336)^2 - 4\cdot 27\,(5184k^2 + 6048k + 704) = 144\,\big(256 - 2016k - 1863k^2\big)
$$

(the discriminant $b^2 - 4ac$ of $a\alpha_2^2 + b\alpha_2 + c$, multiplied out: $291600k^2 + 362880k + 112896 - 559872k^2 - 653184k - 76032$, and 144 taken out). For $k \ge 1$ (the whole record history, where $k = e^{2x_4/3} \ge 1$ for $x_4 \ge 0$) the bracket $256 - 2016k - 1863k^2$ is at most $256 - 2016 - 1863 < 0$. So on the record history $\det J$ never vanishes, for any Gauss-Bonnet coupling, and since it is $-3 < 0$ at $\alpha_2 = 0$ it is always negative. Notebook 12a prints these two polynomials and checks the conclusion (In [24]); it also draws $\det J$ for Einstein gravity, for $\alpha_2H^2 = 0.01$ and $1/32$ and for the author's weights (figure 12a.4): all stay negative along the history. Where $\det J = 0$ on some other history the two equations could not be solved for $a_4''$ and $v$; Notebook 12c meets such a point for a gas of massless particles (Section 12.21).

**What each equation does.** Given $a_4'$, $u$ and $k$ at one moment, the constraint fixes the energy density $\rho$ at that moment. Given the pressures $p_3$ and $p_0 = p_t$, the two equations of second order fix $a_4''$ and $v$, and so the future of $a_4$ and $b_4$. The record names the third combination: the 3-space equation minus the block equation, $e_{11} - e_{00} = \kappa(p_3 - p_0)$, in which $\Lambda$ cancels; in Einstein gravity it reads $2a_4'' - \tfrac12v - 2(a_4')^2 + \tfrac92a_4'u - u^2 + 3H^2k = \kappa(p_3 - p_0)$ (the two components of Section 12.6 subtracted): the anisotropic stress $p_3 - p_0$ drives the difference between the evolution of 3-space and that of the block.

### 12.10 The Bianchi identity and the conservation law

**The identity.** Each Lovelock tensor has zero divergence for every metric (PROVED for the corrected metric with arbitrary $a_4$ and $b_4$: checks `E1_divergence_free` to `E3_divergence_free` in both reports; Notebook 12a, In [19]). Since $\Lambda\delta^\mu_\nu$ has zero divergence too, the field equations can hold only if the source has zero divergence.

**The divergence of a diagonal tensor.** The covariant divergence of a mixed tensor is

$$
\nabla_\mu T^\mu{}_\nu = \sum_\mu \partial_\mu T^\mu{}_\nu + \sum_{\mu,\lambda}\Gamma^\mu{}_{\mu\lambda}T^\lambda{}_\nu - \sum_{\mu,\lambda}\Gamma^\lambda{}_{\mu\nu}T^\mu{}_\lambda .
$$

For a diagonal $T$ whose entries depend on $x_4$ only, we simplify line by line:

$$
\nabla_\mu T^\mu{}_\nu = \partial_\nu T^\nu{}_\nu + \sum_\mu\Gamma^\mu{}_{\mu\nu}T^\nu{}_\nu - \sum_\mu\Gamma^\mu{}_{\mu\nu}T^\mu{}_\mu
$$

(in the first sum only $\mu = \nu$ survives, because $T$ is diagonal; in the second only $\lambda = \nu$; in the third only $\lambda = \mu$, which turns $\Gamma^\lambda{}_{\mu\nu}$ into $\Gamma^\mu{}_{\mu\nu}$)

$$
\nabla_\mu T^\mu{}_\nu = \partial_\nu T^\nu{}_\nu + \sum_\mu \Gamma^\mu{}_{\mu\nu}\big(T^\nu{}_\nu - T^\mu{}_\mu\big)\qquad(\text{no sum over } \nu)
$$

(the two sums combined). For $\nu = x_4$ the Christoffel symbols of Section 12.4 give $\Gamma^{x_i}{}_{x_ix_4} = a_4'$ for the three 3-space directions, $\Gamma^{\mu}{}_{\mu x_4} = h$ for the four block directions and $0$ for $\mu = x_4$:

$$
\nabla_\mu T^\mu{}_{x_4} = \partial_4T^{x_4}{}_{x_4} + 3a_4'\big(T^{x_4}{}_{x_4} - T^{x_1}{}_{x_1}\big) + 4h\big(T^{x_4}{}_{x_4} - T^{x_0}{}_{x_0}\big)
$$

(the block directions grouped, using $T^{x_0}{}_{x_0} = T^{x_5}{}_{x_5}$). For $\nu = x_0$ the symbols are $\Gamma^{x_0}{}_{x_0x_0}$ (which multiplies $T^{x_0}{}_{x_0} - T^{x_0}{}_{x_0} = 0$) and $\Gamma^{x_t}{}_{x_tx_0} = H\cot z$ for the three extra times, so $\nabla_\mu T^\mu{}_{x_0} = 3H\cot z\,(T^{x_0}{}_{x_0} - T^{x_5}{}_{x_5})$ when nothing depends on $x_0$; for every other $\nu$ the divergence is identically zero.

**For the left-hand side** ($T^\mu{}_\nu \to e^\mu{}_\nu$, with $e_{00} = e_{55}$) the $x_0$ line vanishes identically, and the $x_4$ line set to zero reads

$$
\frac{d}{dx_4}e_{44} = 3a_4'\,\big(e_{11} - e_{44}\big) + 4h\,\big(e_{00} - e_{44}\big)
$$

(the divergence of the left-hand side is zero; the terms $3a_4'(e_{44} - e_{11})$ and $4h(e_{44} - e_{00})$ moved to the right). This is an identity for every $a_4$, $b_4$ and every coupling (PROVED: sympy report, check `bianchi_x4`; Wolfram report, check `constraint_propagation_bianchi`; Notebook 12a, In [23]).

**For the source** $T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ with $p_0 = p_t$ and no dependence on $x_0$ the $x_4$ line gives

$$
-\partial_4\rho + 3a_4'(-\rho - p_3) + 4h(-\rho - p_0) = 0
\quad\Longrightarrow\quad
\partial_4\rho + 3a_4'(\rho + p_3) + 4h(\rho + p_0) = 0
$$

(the entries inserted; then multiplied by $-1$): the **energy exchange** of the record (key `generalSource/energyExchange`). Energy flows between 3-space (rate $a_4'$) and the block (rate $h$); there is no other loss. The $x_0$ line holds automatically, because $p_0 = p_t$. For a general source, with $x_0$-dependence and mixed components $q_{40}$, $q_{04}$, the record gives (key `generalSource`, entries `conservation_x4` and `conservation_x0`; $\partial_0$ is the derivative with respect to $x_0$)

$$
\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'(\rho + p_3) - 3h(\rho + p_t) - h(\rho + p_0) + \partial_0 q_{04} - 3H(\cot z + 2\tan z)\,q_{04},
$$
$$
\nabla_\mu T^\mu{}_{x_0} = \partial_0 p_0 + 3H\cot z\,(p_0 - p_t) + \partial_4 q_{40} + \tfrac32u\,q_{40} - h\cot^2 z\,q_{04}/k .
$$

Notebook 12a computes both for six arbitrary functions of $x_4$ and $z$ and compares them with the record and, without the mixed components, with the lead's formulas (PROVED: sympy report, check `json_conservation`; lead's divergence report, checks `divergence_x4_component`, `divergence_x0_component` and `divergence_other_components_zero`; In [25]).

**The constraint propagates.** Let $C = e_{44} + \Lambda + \kappa\rho$ be the amount by which the constraint fails. Suppose the two equations of second order hold at every time and the source obeys the energy exchange. Then, line by line:

$$
\frac{dC}{dx_4} = \frac{de_{44}}{dx_4} + \kappa\,\partial_4\rho = 3a_4'(e_{11} - e_{44}) + 4h(e_{00} - e_{44}) - 3a_4'\kappa(\rho + p_3) - 4h\kappa(\rho + p_0)
$$

($\Lambda$ is constant; the Bianchi identity for the first term, the energy exchange for the second)

$$
e_{11} - e_{44} = (\kappa p_3 - \Lambda) - (C - \Lambda - \kappa\rho) = \kappa(\rho + p_3) - C,\qquad e_{00} - e_{44} = \kappa(\rho + p_0) - C
$$

(the 3-space and block equations give $e_{11}$ and $e_{00}$; the definition of $C$ gives $e_{44} = C - \Lambda - \kappa\rho$)

$$
\frac{dC}{dx_4} = 3a_4'\big(\kappa(\rho + p_3) - C\big) + 4h\big(\kappa(\rho + p_0) - C\big) - 3a_4'\kappa(\rho + p_3) - 4h\kappa(\rho + p_0) = -(3a_4' + 4h)\,C
$$

(inserted; the terms with $\kappa$ cancel in pairs). This is a linear equation for $C$ without a source term: if $C = 0$ at one time, then $C = 0$ at every time (its solution is $C(x_4) = C(0)\exp(-\int_0^{x_4}(3a_4' + 4h))$, which is zero for $C(0) = 0$). Since $3a_4' + 4h = 2u - a_4'$ is the rate of $\ln\sqrt{|\det g|}$ (Section 12.3), the product $C\sqrt{|\det g|}$ is constant. So the constraint need only be imposed at the start; Notebook 12c checks numerically that it then holds along every solution (Section 12.21).

### 12.11 Einstein gravity: a flat vacuum, no exponential vacuum, and the null energy conditions

**A flat vacuum.** Take $a_4 = 0$ and $b_4 = H^2(x_4 - c)^2$ with a constant $c$ (for $x_4 > c$). Then

$$
a_4' = a_4'' = 0,\qquad u = \frac{b_4'}{b_4} = \frac{2H^2(x_4 - c)}{H^2(x_4 - c)^2} = \frac{2}{x_4 - c},\qquad v = u' = -\frac{2}{(x_4 - c)^2},\qquad k = \frac{1}{H^2(x_4 - c)^2}
$$

(the derivative of $(x_4 - c)^2$ is $2(x_4 - c)$; the derivative of $2(x_4 - c)^{-1}$ is $-2(x_4 - c)^{-2}$; $k = e^0/b_4$). Inserting into the three Einstein components, with $s = 1/(x_4 - c)^2$:

$$
e_{44} = 0 + 6s - \tfrac32\cdot 4s = 0,\qquad
e_{11} = 0 - \tfrac52\cdot 4s - 2(-2s) + 6s = 0,\qquad
e_{00} = -\tfrac32\cdot 4s - \tfrac32(-2s) + 3s = 0
$$

($H^2k = s$, $u^2 = 4s$, $v = -2s$; then $6 - 6 = 0$, $-10 + 4 + 6 = 0$, $-6 + 3 + 3 = 0$). So this history solves the vacuum equations with $\Lambda = 0$. In fact every curvature component vanishes (PROVED: Wolfram report, check `flat_member`; sympy report, check `einstein_flat_vacuum`; Notebook 12a, In [26]): this history is flat 8-dimensional space written in unusual coordinates, of the same kind as the coordinates of Milne for ordinary flat space, in which a block of constant curvature is multiplied by the square of the time $x_4 - c$. This vacuum has a still 3-space and a growing block ($e^{-a_4}b_4^{1/2} = H(x_4 - c)$), not a deflating one.

**No exponential vacuum.** On an exponential history $a_4' = AH$, $u = \beta AH$ and $a_4'' = v = 0$. A vacuum needs $e_{44} + \Lambda = e_{11} + \Lambda = e_{00} + \Lambda = 0$, so the two differences must vanish whatever $\Lambda$ is. The first:

$$
e_{44} - e_{11} = \Big(3A^2H^2 + 6H^2k - \tfrac32\beta^2A^2H^2\Big) - \Big(-5A^2H^2 + 6\beta A^2H^2 - \tfrac52\beta^2A^2H^2 + 6H^2k\Big)
$$

(the components with the history inserted)

$$
= \big(8 - 6\beta + \beta^2\big)A^2H^2 = (\beta - 2)(\beta - 4)\,A^2H^2
$$

(the terms with $k$ cancel; $3 + 5 = 8$, $-\tfrac32 + \tfrac52 = 1$; the quadratic factorised). The second:

$$
e_{44} - e_{00} = \Big(3 - \tfrac32\beta^2\Big)A^2H^2 + 6H^2k - \Big(-3 + \tfrac32\beta - \tfrac32\beta^2\Big)A^2H^2 - 3H^2k = \Big(6 - \tfrac32\beta\Big)A^2H^2 + 3H^2k
$$

(inserted and collected). Setting it to zero gives $k = \tfrac12(\beta - 4)A^2$ (divided by $3H^2$). The first difference vanishes only for $\beta = 2$, $\beta = 4$ or $A = 0$, and then the second gives $k = -A^2$, $k = 0$ or $k = 0$. But $k = e^{2a_4}/b_4 > 0$ always. So in Einstein gravity no exponential history is a vacuum, for any $\Lambda$ (PROVED: sympy report, check `einstein_no_exponential_vacuum`; Wolfram report, check `einstein_no_exponential_vacuum`; Notebook 12a, In [26] and figure 12a.5). With the author's weights there is none either (record key `exponentialHistory/authorWeights/vacuum`; Notebook 12b), while Einstein-Gauss-Bonnet gravity has exponential vacua, but only with constant $k$ (record key `exponentialHistory/einsteinGaussBonnetVacuum`; Notebook 12b).

**The null energy conditions.** A **null vector** has zero length. In the frame of Chapter 6 (unit vectors along the eight directions, with $\eta = \mathrm{diag}(+,+,+,+,-,-,-,-)$) the vector $n = e_{(x_4)} + e_{(x_0)}$ has the length $\eta_{44} + \eta_{00} = -1 + 1 = 0$. The **null energy condition** along $n$ asks $\sum_{a,b} T_{(a)(b)}\,n^an^b \ge 0$; for our diagonal source

$$
T_{(a)(b)}n^an^b = T_{(4)(4)} + T_{(0)(0)} = \eta_{44}T^{x_4}{}_{x_4} + \eta_{00}T^{x_0}{}_{x_0} = (-1)(-\rho) + p_0 = \rho + p_0
$$

(only the components with $a, b \in \{x_4, x_0\}$ survive and the mixed ones are zero; lowering the first index multiplies by $\eta_{aa}$; for a diagonal metric the frame components of a mixed tensor equal its coordinate components). In the same way the condition along $e_{(x_4)} + e_{(x_1)}$ is $\rho + p_3 \ge 0$. Ordinary matter, such as a gas or radiation, satisfies both. In the field equations, subtracting the constraint from the block and the 3-space equations removes $\Lambda$:

$$
\kappa(\rho + p_0) = e_{00} - e_{44},\qquad \kappa(\rho + p_3) = e_{11} - e_{44}
$$

(block equation minus constraint, $(e_{00} + \Lambda) - (e_{44} + \Lambda) = \kappa p_0 + \kappa\rho$; the same for 3-space). In Einstein gravity, with the components above,

$$
\kappa(\rho + p_0) = -6(a_4')^2 + \tfrac32a_4'u - \tfrac32v - 3H^2k = -\tfrac32\big(2H^2k + 4(a_4')^2 - a_4'u + v\big),
$$
$$
\kappa(\rho + p_3) = -8(a_4')^2 + 6a_4'u + 2a_4'' - u^2 - 2v
$$

(the differences collected: $-3 - 3 = -6$, $-\tfrac32 + \tfrac32 = 0$ for $u^2$, $3 - 6 = -3$ for $H^2k$; and $-5 - 3 = -8$, $-\tfrac52 + \tfrac32 = -1$, $6 - 6 = 0$). These are the record's null combinations (PROVED: sympy report, check `einstein_null_combinations`; Notebook 12a, In [26]). On the record history ($a_4' = H$, $u = \tfrac43H$, $a_4'' = v = 0$, units $H = 1$):

$$
\kappa(\rho + p_0) = -\tfrac32\big(2k + 4 - \tfrac43\big) = -3k - 4 < 0,\qquad \kappa(\rho + p_3) = -8 + 8 - \tfrac{16}9 = -\tfrac{16}9 < 0
$$

(inserted; $4 - \tfrac43 = \tfrac83$). For $\kappa > 0$ the source of the record history violates both null energy conditions in Einstein gravity, along $x_4 + x_0$ ever more strongly as $k$ grows (Notebook 12a, In [26]; Notebook 12b, figure 12b.5, shows that no exponential history satisfies both in Einstein gravity).

### 12.12 The exponential histories: the extra times deflate by a choice of sign

**The histories.** An **exponential history** is $a_4 = AHx_4 + a_0$, $b_4 = b_4(0)\,e^{\beta AHx_4}$ with constants $A$ (the slope), $\beta$, $a_0$ and $b_4(0) > 0$. Then

$$
a_4' = AH,\quad a_4'' = 0,\quad u = \beta AH,\quad v = 0,\quad h = \big(\tfrac12\beta - 1\big)AH,\quad k = \frac{e^{2a_0}}{b_4(0)}\,e^{(2 - \beta)AHx_4}
$$

(the derivatives of linear and exponential functions; $k = e^{2a_4}/b_4$ with the exponents subtracted). 3-space grows like $e^{AHx_4}$ and the block like $e^{hx_4}$: for $A > 0$ and $\beta < 2$ 3-space inflates while the hidden direction and the extra times deflate. The record history is $A = 1$, $\beta = \tfrac43$, $a_0 = 0$, $b_4(0) = 1$, with $h = -\tfrac13H$ and $k = e^{(2/3)Hx_4}$ (record `a4-equations.json`, key `exponentialHistory/history`).

**The required source.** On such a history every component of the field equations is a polynomial in $k$ (the components of Section 12.7 contain $k$ and $k^2$, no higher power), so the required source is

$$
\kappa\rho = -\big(e_{44} + \Lambda\big),\qquad \kappa p_3 = e_{11} + \Lambda,\qquad \kappa p_0 = \kappa p_t = e_{00} + \Lambda,
$$

a polynomial of degree at most 2 in $k$, which changes in time unless $\beta = 2$ or $A = 0$ (PROVED: sympy report, check `exponential_history_required_source`; Notebook 12a, In [28]). In Einstein gravity, inserting the history into the components of Section 12.9:

$$
\begin{aligned}
\kappa\rho &= \tfrac32A^2H^2(\beta^2 - 2) - 6H^2k - \Lambda,\\
\kappa p_3 &= -\tfrac12A^2H^2(5\beta^2 - 12\beta + 10) + 6H^2k + \Lambda,\\
\kappa p_0 &= -\tfrac32A^2H^2(\beta^2 - \beta + 2) + 3H^2k + \Lambda
\end{aligned}
$$

($-e_{44} = -3A^2H^2 + \tfrac32\beta^2A^2H^2 - 6H^2k$; $e_{11} = (-5 + 6\beta - \tfrac52\beta^2)A^2H^2 + 6H^2k$; $e_{00} = (-3 + \tfrac32\beta - \tfrac32\beta^2)A^2H^2 + 3H^2k$; the brackets factorised; record key `exponentialHistory/einstein`). On the record history with $\Lambda = 0$ and $H = 1$ this is $\kappa\rho = -6k - \tfrac13$, $\kappa p_3 = 6k - \tfrac{13}9$ and $\kappa p_0 = 3k - \tfrac{11}3$ (with $\beta^2 = \tfrac{16}9$: $\tfrac32(\tfrac{16}9 - 2) = -\tfrac13$, $-\tfrac12(\tfrac{80}9 - 16 + 10) = -\tfrac{13}9$, $-\tfrac32(\tfrac{16}9 - \tfrac43 + 2) = -\tfrac{11}3$): a negative energy density that grows in size like $k$, and $p_3 \ne p_0$. This is the source that Section 12.6 already met as $G$ along the history.

**The record history with the author's weights.** With $\alpha_k = w_k/H^{2k}$, $w = (1, \tfrac1{32}, \tfrac1{1152})$ and $H = 1$ the constraint needs $e_{44} = E_{(1)}{}^{x_4}{}_{x_4} + \tfrac1{32}E_{(2)}{}^{x_4}{}_{x_4} + \tfrac1{1152}E_{(3)}{}^{x_4}{}_{x_4}$ on the history. The three values were found in Sections 12.6 and 12.7: $6k + \tfrac13$, $-12k^2 + \tfrac{80}3k - \tfrac{76}{27}$ and $-216k^2 - 144k + 40$. So

$$
e_{44} = 6k + \tfrac13 + \tfrac1{32}\Big(-12k^2 + \tfrac{80}3k - \tfrac{76}{27}\Big) + \tfrac1{1152}\big(-216k^2 - 144k + 40\big)
$$

(the weighted sum)

$$
= \Big(-\tfrac38 - \tfrac3{16}\Big)k^2 + \Big(6 + \tfrac56 - \tfrac18\Big)k + \Big(\tfrac13 - \tfrac{19}{216} + \tfrac5{144}\Big)
$$

(each power of $k$ collected: $\tfrac{12}{32} = \tfrac38$, $\tfrac{216}{1152} = \tfrac3{16}$, $\tfrac{80}{96} = \tfrac56$, $\tfrac{144}{1152} = \tfrac18$, $\tfrac{76}{864} = \tfrac{19}{216}$, $\tfrac{40}{1152} = \tfrac5{144}$)

$$
= -\tfrac9{16}k^2 + \tfrac{161}{24}k + \tfrac{121}{432}
$$

(common denominators: $\tfrac{6 + 3}{16}$; $\tfrac{144 + 20 - 3}{24}$; $\tfrac{144 - 38 + 15}{432}$). This is the record's $-\kappa\rho - \Lambda$ (key `exponentialHistory/authorWeights/historySource_kappaT_minus_Lam`, entry `minus_rho`). The other two entries are $\kappa p_3 - \Lambda = -\tfrac9{16}k^2 + \tfrac{1601}{216}k - \tfrac{5359}{3888}$ and $\kappa p_0 - \Lambda = \kappa p_t - \Lambda = \tfrac{79}{16}k - \tfrac{497}{144}$; Notebook 12a computes all three from its own tensors and checks them against the record (PROVED: sympy report, check `author_weights_history_source`; In [29]) and checks that this source obeys the energy exchange (metric report, check `history_source_conserved`). The history needs this diagonal source, which grows like $k^2$; the record does not derive it from any field and uses the history as a PRESCRIBED background (key `exponentialHistory/authorWeights/statement`).

**The sign of $A$ is a choice.** Under the exchange $(a_4', u) \to (-a_4', -u)$, with $a_4''$, $v$ and $k$ kept, every sectional curvature of the table of Section 12.5 keeps its value: $(a_4')^2$ and $a_4'' + (a_4')^2$ obviously; $a_4'h \to (-a_4')(-h) = a_4'h$, because $h = \tfrac12u - a_4'$ changes sign; $h' + h^2$ and $h^2 - H^2k$, because $h' = \tfrac12v - a_4''$ is kept and $h^2$ is a square. Every Lovelock tensor is a sum of products of sectional curvatures (Section 12.7), so it keeps its value too (Chapter 11 states the same symmetry). Two consequences:

1. On exponential histories $A \to -A$ is exactly this exchange ($a_4' = AH$, $u = \beta AH$). So, written as a function of $k$, the required source contains $A$ only through $A^2$: the histories with slopes $A$ and $-A$ need the same source at the same value of $k$ (PROVED: Notebook 12a, In [28]; Notebook 12b, In [4] and In [7]).
2. Reversing the time, $x_4 \to -x_4$, turns $a_4(x_4)$ into $a_4(-x_4)$, whose rate is $-a_4'$, and $u$ into $-u$, while $a_4''$, $v$ and $k$ keep their values (two sign changes in a second derivative). So if a history with a source solves the field equations, the time-reversed history with the time-reversed source solves them too.

On the exponential histories the history with $-A$ is the time reverse of the history with $A$: where one deflates the block, the other inflates it. The field equations therefore do not select deflation; whether the extra times deflate is decided by the source and the starting values (an initial condition), not by the equations of gravity (PROVED, as stated; Notebook 12b draws it in figure 12b.2).

### 12.13 Example: the field equations derived by computer algebra

The first notebook repeats everything of Sections 12.3 to 12.12 with exact computer algebra, starting from nothing but the metric, and compares every result with the Revision record. It computes the 31 nonzero Christoffel symbols (21 distinct), the 112 nonzero Riemann components (28 with $a < b$, $m < n$, all sectional), the Einstein tensor and the three Lovelock tensors with its own GKD (28, 420 and 2520 lists of index pairs contribute for $k = 1, 2, 3$), checks them against the Rust program of the GKD record in all 64 components and against the classical Gauss-Bonnet formula, writes and reduces the field equations, checks the Bianchi identity and the conservation law, and specialises to Einstein gravity and to the exponential histories. It prints 72 PASS lines and draws five figures. It needs no Rust and runs in about half a minute.

<!-- NOTEBOOK 12a -->

### 12.16 Line-by-line walk-through of Notebook 12a

The notebook has 30 code cells, In [1] to In [30]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted, then explained. A line that starts with `#`, and the part of a line after `#`, is a **comment**, which Python skips; it is there for the reader. Inside a function the text in triple quotes below the `def` line is its **docstring**, a description that Python stores but does not run; to keep the quotations short, docstrings are left out of them (each explanation says what the function does), and a long figure caption passed to `save_figure` is shortened to its first line followed by `...)` (the full caption is printed under the figure in Section 12.15). Because Notebook 12a is the first notebook of this chapter, its set-up cell is explained here in full; the walk-throughs of Notebooks 12b, 12c and 12d refer back to this explanation.

**In [1], the set-up cell.** Its first part, down to the heading THE SET-UP between two lines of `=` signs, consists of comment lines that repeat the complete run instructions of Section 12.14, so that the notebook file carries its own instructions. The code below the heading computes no physics; it is the same in every notebook of the book except for the line that names the notebook (the notebooks that run a Rust program have two more imports and one more helper; the four notebooks of this chapter run none).


```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module**, a part of Python or of a package, so that the code can use it. `json`, `os`, `textwrap` and `pathlib` come with Python. `from pathlib import Path` takes the one name `Path` out of `pathlib`; a `Path` is the address of a file or folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

These load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python), which show a picture file below a cell.

```python
NOTEBOOK_ID = "12a"  # this notebook: chapter 12, example a
```

A **variable** is a name for a value; this line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"12a"`. The figure files are named after it.

```python
def find_repository_root():
    here = Path.cwd().resolve()  # the folder in which this notebook runs
    for folder in [here, *here.parents]:  # this folder, its parent, its grandparent ...
        if (folder / "Revision" / "textbook" / "requirements.txt").is_file():
            return folder
    raise FileNotFoundError(
        "The repository folder was not found: open this notebook inside the folder "
        "Revision/textbook/notebooks of the repository Dirac_claude")
```

`def` defines a **function**, a named piece of code that runs when it is called. (In the notebook the function also has a **docstring**, the text in triple quotes under the `def` line, which says what it does; it is left out here.) `Path.cwd()` is the folder in which Jupyter runs the notebook and `.resolve()` writes it as a complete address. `here.parents` is the list of the folders above it; `[here, *here.parents]` is the list that starts with `here` and continues with them (the star unpacks a list into another list). The `for` loop visits these folders one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that contains `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If none does, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
REPO = find_repository_root()
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The first line calls the function and names its result `REPO`; it is never printed, because it differs from computer to computer while the printed output of a notebook must not. The second line chooses where files are written: `os.environ` holds the **environment variables** of the program (named texts it receives from the computer), and `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and `str(REPO)` otherwise. When you run the notebook it is not set, so files go into the repository; the book's checking tool sets it to a scratch folder.

```python
def repository_file(relative):
    return REPO / relative


def output_file(relative):
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

Two small functions (docstrings left out). `repository_file` gives the full path of a repository file, for reading a Revision record. `output_file` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates its folder and any missing folder above it, and does nothing if it exists.

```python
def say(text):
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters (the width of a page of the book); `textwrap.fill` breaks the text at blanks and starts every line after the first with four blanks.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns to the built-in settings, so that the figures are the same on every computer. `plt.rcParams.update({...})` sets the size of a figure (7.0 by 4.2 inches), the size of its letters (10 points) and a faint grid (`grid.alpha` 0.3 means 30 per cent opaque). The braces make a **dictionary**: pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: a name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/12a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty JSON dictionary and a line end into the captions file (the comment lines above it in the notebook say so); `encoding="utf-8"` fixes how letters are stored and `newline="\n"` stores the same line end on every system.

```python
def save_figure(fig, name, caption):
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
    fig.savefig(output_file(relative), dpi=150, bbox_inches="tight",
                metadata={"Software": None})
    plt.close(fig)  # forget the figure, so that Jupyter does not draw it a second time
    CAPTIONS[file_name] = caption
    output_file(CAPTION_FILE).write_text(
        json.dumps(CAPTIONS, indent=1, sort_keys=True) + "\n", encoding="utf-8",
        newline="\n")
    display(Image(filename=str(output_file(relative))),
            metadata={"textbook_figure": file_name})  # the saved picture itself
    say(f"Figure {NOTEBOOK_ID}.{number} saved as {relative}")
```

(Shown without its docstring and its three comment lines.) `setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far: the figures are numbered 1, 2, 3, and a cell run twice keeps its number. The file name is the notebook id, the number and the name, for example `12a_1_pair_curvatures.png`. `fig.savefig` writes a PNG file with 150 dots per inch, cuts away the empty margin and stores no program name, so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time. The caption is stored, the whole dictionary is written to the captions file (`json.dumps` turns it into JSON text with sorted keys), `display(Image(...))` shows the saved picture, and the last line prints where it was saved.

```python
PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")
```

`PASSED` is an empty **list** (an ordered collection in square brackets). `check` is the function behind every check: if `condition` is false (`False`), `raise AssertionError(...)` stops the notebook with an error naming the check (an `if` is used instead of the statement `assert`, because Python started with the option that optimises skips every `assert`); otherwise the name is appended to `PASSED` and the line PASS name is printed, followed by a second line naming the Revision record when `record` is given. `record=None` makes that argument optional.

```python
def report(label, value, unit=""):
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a line that starts with RESULT; `(f" {unit}" if unit else "")` adds the unit when one is given. `all_checks_passed` prints the last line of the notebook; `len(PASSED)` is the number of checks that passed. The last statement prints the one output line of In [1].

**In [2], the Revision records.** The cell names the record files, defines three helpers and checks that every report it uses has passed all its checks.

```python
import contextlib  # redirect_stdout: send printed lines into a buffer
import io  # StringIO: a text buffer in memory
```

Two modules of Python: `contextlib` provides `redirect_stdout`, which sends everything that `print` writes into another place, and `io` provides `StringIO`, a text buffer held in memory.

```python
PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
WARPED = "Revision/metric_warped/reports/python-warped-metric-report.json"
FIELD = "Revision/theory/reports/wolfram-field-theory.json"  # field theory
LEAD = "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json"  # lead check
EMT = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the equations
LOVELOCK = "Revision/gkd_lovelock/results/lovelock-tensors.json"  # Rust GKD output
METRIC_RESULTS = "Revision/metric_warped/results/warped-metric.json"
```

Nine short names for the nine record files the notebook reads: the sympy and Wolfram reports of the field equations, the metric report, the field-theory report, the lead's two reports (`LEAD`, the Einstein and Gauss-Bonnet checks; `EMT`, the divergence and spin-connection checks), the equations themselves (`a4-equations.json`, written by the Wolfram verifier), the Lovelock tensors written by the Rust program `lovelock_gkd` of the GKD record, and the results file of the corrected metric (`warped-metric.json`, which holds the record's Einstein tensor and the source of the record history). Section 12.2 lists the reports.

```python
def read_json(relative):
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))
```

`read_json` reads a file of the repository as text (`repository_file` of In [1] gives its full path) and turns it into Python dictionaries and lists with `json.loads`.

```python
def record_verdict(report_file, name):
    for entry in read_json(report_file)["checks"]:
        if entry["name"] == name:
            return entry["verdict"]
    return None
```

Every report holds a list under the key `"checks"`; each entry is a dictionary with a `"name"`, a `"verdict"` and a `"detail"`. `record_verdict` walks through that list and returns the verdict of the check with the given name, or `None` if there is no such check.

```python
def reproduces(condition, name, report_file, record_name):
    found = record_verdict(report_file, record_name) == "PASS"
    lines = io.StringIO()  # a text buffer
    with contextlib.redirect_stdout(lines):  # print() now writes into the buffer
        check(condition and found, name, record=f"{report_file}, check {record_name}")
    print(lines.getvalue(), end="")  # all lines at once
```

`reproduces` is a check that passes only when two things are true: the notebook's own result (`condition`) and the record's verdict PASS for the named check (`found`). `with contextlib.redirect_stdout(lines):` makes every `print` inside the indented block write into the buffer `lines` instead of the screen; after the block, `print(lines.getvalue(), end="")` prints the collected PASS and reproduces lines with one call (`end=""` adds no extra line end), so the two lines always stay together. If the condition fails, `check` stops the notebook with its error before anything is printed.

```python
for report_file in (PY, WL, WARPED, FIELD, LEAD, EMT):
    verdicts = [entry["verdict"] for entry in read_json(report_file)["checks"]]
    passed = verdicts.count("PASS")  # how many checks of the record passed
    say(f"{report_file}: {passed} of {len(verdicts)} checks PASS")
    check(len(verdicts) > 0 and passed == len(verdicts),
          f"every check of the record {Path(report_file).name} passed")
```

For each of the six reports, a **list comprehension** (a list built by a `for` inside square brackets) collects the verdicts of all its checks, `.count("PASS")` counts the PASS verdicts, and `say` prints this count together with the number of checks of the report. `check` then requires that the report has at least one check and that every one of them passed; `Path(report_file).name` is the last part of the path, the file name, which names the report in the PASS line. Out [2] shows 69 of 69 (sympy report), 57 of 57 (Wolfram report), 14 of 14 (metric report), 86 of 86 (field-theory report), 12 of 12 (lead's Einstein report) and 10 of 10 (lead's divergence report), each followed by its PASS line. A record may gain checks when it is extended; the cell prints the counts instead of assuming them.

**In [3], the metric.**

```python
import itertools  # loops over all combinations of indices
```

`itertools` (part of Python) produces combinations of indices, for example all triples $(a, b, c)$ with each index from 0 to 7.

```python
import numpy as np  # arrays of numbers, used for the plots
import sympy as sp  # exact algebra with symbols
```

`numpy` (as `np`) computes with arrays of floating-point numbers and is used only for the plots; `sympy` (as `sp`) computes exactly with symbols.

```python
H = sp.symbols("H", positive=True)  # the constant H of the metric, H > 0
t = sp.symbols("t", real=True, nonzero=True)  # t = tan z, z = 6 H x0 real
w = sp.symbols("w", positive=True)  # w = (sin(z)^2)^(1/12) > 0
ea, bb = sp.symbols("ea bb", positive=True)  # ea = e^(a4), bb = b4 > 0
ad1, ad2, ad3 = sp.symbols("ad1 ad2 ad3", real=True)  # derivatives 1, 2, 3 of a4
bd1, bd2, bd3 = sp.symbols("bd1 bd2 bd3", real=True)  # derivatives 1, 2, 3 of b4
```

`sp.symbols` makes symbols, letters that stand for numbers; the options tell sympy what kind of number, which lets it simplify safely (for example $\sqrt{H^2} = H$ because $H > 0$). The hidden angle enters through two symbols: `t` for $\tan z$, real and not zero, and `w` for $(\sin^2 z)^{1/12}$, positive. Together they describe every real $z$ with $\sin z\cos z \ne 0$, with no assumption about the signs of $\sin z$ and $\cos z$. The functions of the time enter as **jet variables**: `ea` for $e^{a_4}$ and `bb` for $b_4$ (both positive), `ad1`, `ad2`, `ad3` for $a_4'$, $a_4''$, $a_4'''$, and `bd1`, `bd2`, `bd3` for $b_4'$, $b_4''$, $b_4'''$. The notebook never needs $a_4$ itself, only $e^{a_4}$ and the derivatives.

```python
NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # positions 0..7
N = 8  # the number of dimensions
g = ([bb / (ea ** 2 * t ** 2)]  # g00 = e^(-2 a4) b4 cot(z)^2: the hidden direction
     + [ea ** 2] * 3  # g11 = g22 = g33 = e^(2 a4): 3-space, no warp
     + [sp.Integer(-1)]  # g44 = -1: the time x4
     + [-bb * w ** 2 / ea ** 2] * 3)  # g55 = g66 = g77: the extra times
```

`NAMES` lists the coordinates in the author's order; `N = 8`. The metric is a Python list `g` of its eight diagonal entries, built by joining lists with `+`; `[ea ** 2] * 3` is a list holding the same entry three times. Position 0 is $g_{00} = b_4/(e^{2a_4}\tan^2 z) = e^{-2a_4}b_4\cot^2 z$; positions 1 to 3 are $e^{2a_4}$ (3-space has no factor that depends on $x_0$); position 4 is the exact integer $-1$ (`sp.Integer(-1)`); positions 5 to 7 are $-b_4w^2/e^{2a_4} = -e^{-2a_4}b_4(\sin^2 z)^{1/6}$. `**` means "to the power".

```python
for name, entry in zip(NAMES, g):
    say(f"g[{name},{name}] = {entry}")
```

`zip(NAMES, g)` pairs each name with its entry, and the loop prints the eight entries (Out [3]): `bb/(ea**2*t**2)`, three times `ea**2`, `-1` and three times `-bb*w**2/ea**2`.

**In [4], signature, determinant and volume.**

```python
point = {t: 1, w: 1, ea: 1, bb: 1}  # any point gives the same signs
signs = [int(sp.sign(entry.subs(point))) for entry in g]
say(f"signs of the diagonal entries: {signs}")
check(signs == [1, 1, 1, 1, -1, -1, -1, -1],
      "the signature is (4,4): eta = diag(+,+,+,+,-,-,-,-) in the order x0..x7")
det_g = sp.Mul(*g)  # the product of the eight diagonal entries
```

`point` is a dictionary that gives each symbol the value 1; `entry.subs(point)` inserts these values, `sp.sign` gives the sign $+1$ or $-1$, and `int` turns sympy's integer into a Python integer. The signs cannot depend on the point, because $b_4$, $e^{a_4}$ and $w$ are positive and $t$ appears squared. The cell prints them, `[1, 1, 1, 1, -1, -1, -1, -1]`, and checks the signature (4,4). `sp.Mul(*g)` multiplies the eight entries (the star hands the list over as eight separate factors): the determinant of a diagonal matrix.

```python
say(f"det g = {sp.simplify(det_g)}")
reproduces(sp.simplify(det_g - bb ** 4 * w ** 6 / (ea ** 2 * t ** 2)) == 0,
           "det g = e^(-2 a4) b4^4 cot(z)^2 (sin(z)^2)^(1/2) for every real z",
           WL, "sqrt_abs_det_g")
log_rate = sp.cancel(ad1 * ea * sp.diff(sp.log(bb ** 2 * w ** 3 / ea), ea)
                     + bd1 * sp.diff(sp.log(bb ** 2 * w ** 3 / ea), bb))
```

`sp.simplify` brings the product to its simplest form, printed as `bb**4*w**6/(ea**2*t**2)`: $e^{-2a_4}b_4^4\cot^2 z\,(\sin^2 z)^{1/2}$, as derived in Section 12.3. The first `reproduces` checks that the difference from this form is zero and that the Wolfram report lists `sqrt_abs_det_g` as passed. Then the cell computes the rate of change of $\ln\sqrt{|\det g|}$ in time. $\sqrt{|\det g|} = b_4^2w^3/(e^{a_4}|t|)$, and $|t|$ does not depend on $x_4$, so it is left out of the logarithm. By the chain rule $\partial_4 = a_4'e^{a_4}\,\partial/\partial e^{a_4} + b_4'\,\partial/\partial b_4$ on such an expression, which is what `ad1 * ea * sp.diff(..., ea) + bd1 * sp.diff(..., bb)` computes; `sp.cancel` writes the result as one fraction.

```python
reproduces(sp.cancel(log_rate - (2 * bd1 / bb - ad1)) == 0,
           "sqrt|g| = e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4) changes at the rate "
           "2 u - a4'", FIELD, "sqrt_det_g")
reproduces(g[0] == bb / (ea ** 2 * t ** 2) and g[1] == ea ** 2
           and g[5] == -bb * w ** 2 / ea ** 2,
           "the entries are those of the corrected metric", WARPED,
           "corrected_metric_entries")
```

The rate must be $2b_4'/b_4 - a_4' = 2u - a_4'$ (Section 12.3), as the field-theory report says (check `sqrt_det_g`). The last check compares three entries of `g` with the corrected metric and requires the check `corrected_metric_entries` of the metric report. Out [4] shows the signs, the determinant and four PASS lines.

**In [5], derivatives and the Christoffel symbols.**

```python
X4, Z = sp.symbols("X4 Z", real=True)  # explicit dependence (the source only)
RATE = {ea: ea * ad1, bb: bd1, ad1: ad2, ad2: ad3, bd1: bd2, bd2: bd3}
```

`X4` and `Z` are symbols for an explicit dependence on the time and on the hidden angle; only the general source of In [25] uses them. `RATE` is a dictionary that says what the time derivative of each jet variable is: $\partial_4e^{a_4} = a_4'e^{a_4}$, $\partial_4b_4 = b_4'$, $\partial_4a_4' = a_4''$, $\partial_4a_4'' = a_4'''$, $\partial_4b_4' = b_4''$, $\partial_4b_4'' = b_4'''$.

```python
def d(expr, mu):
    if mu == 4:
        return (sum(sp.diff(expr, symbol) * rate for symbol, rate in RATE.items())
                + sp.diff(expr, X4))
    if mu == 0:
        return (6 * H * (1 + t ** 2) * sp.diff(expr, t) + H * w / t * sp.diff(expr, w)
                + 6 * H * sp.diff(expr, Z))
    return sp.Integer(0)  # nothing depends on x1, x2, x3, x5, x6, x7
```

`d(expr, mu)` is the partial derivative with respect to the coordinate at position `mu`. For $x_4$ it uses the chain rule: the sum over the symbols of (the derivative of `expr` with respect to the symbol) times (the symbol's rate from `RATE`), plus the derivative with respect to an explicit `X4`. For $x_0$ it uses $\partial_0 = 6H\,\partial_z$ with $\partial_z\tan z = 1 + \tan^2 z$ and $\partial_z w = \tfrac16 w\cot z$ (because $\ln w = \tfrac1{12}\ln\sin^2 z$ has the derivative $\tfrac1{12}\cdot 2\cot z$), so $\partial_0 t = 6H(1 + t^2)$ and $\partial_0 w = Hw/t$; an explicit `Z` gets the factor $6H$. Nothing depends on the other six coordinates, so their derivatives are zero.

```python
Gamma = [[[sp.Integer(0)] * N for _ in range(N)] for _ in range(N)]  # 512 zeros
for a, b, c in itertools.product(range(N), repeat=3):  # every index triple
    value = 0
    if a == c:
        value += d(g[a], b)
    if a == b:
        value += d(g[a], c)
    if b == c:
        value -= d(g[b], a)
    Gamma[a][b][c] = sp.cancel(value / (2 * g[a]))  # Gamma^a_bc, diagonal metric
```

`Gamma` starts as an 8 by 8 by 8 nested list of zeros: `[...] * N` repeats a list, and the comprehension `for _ in range(N)` builds independent copies (`_` is a name for a loop variable that is not used). The loop visits all 512 index triples and applies the formula of Section 12.4 for a diagonal metric: the term $\partial_b g_{aa}$ when $a = c$, the term $\partial_c g_{aa}$ when $a = b$, minus $\partial_a g_{bb}$ when $b = c$, all divided by $2g_{aa}$. `sp.cancel` writes each symbol as one fraction in lowest terms, so that a zero is recognised as zero.

```python
nonzero = [(a, b, c) for a, b, c in itertools.product(range(N), repeat=3)
           if Gamma[a][b][c] != 0]
distinct = [(a, b, c) for a, b, c in nonzero if b <= c]
say(f"{len(nonzero)} of the 512 Christoffel symbols are not zero, "
    f"{len(distinct)} of them distinct")
check(len(nonzero) == 31, "31 nonzero Christoffel symbols (10 of them twice)")
```

`nonzero` lists the triples whose symbol is not zero, `distinct` those with $b \le c$ (each pair $\Gamma^a{}_{bc} = \Gamma^a{}_{cb}$ once). The cell prints 31 of 512 and 21 distinct, and checks the 31.

```python
check(all(Gamma[a][b][c] == Gamma[a][c][b] for a, b, c in nonzero),
      "Gamma^a_bc = Gamma^a_cb (symmetric in the two lower indices)")
reproduces(len(distinct) == 21, "21 distinct nonzero Christoffel symbols",
           FIELD, "christoffel_count")
```

The symmetry in the two lower indices is checked for every nonzero symbol, and the count 21 against the field-theory report (check `christoffel_count`). Out [5] shows the counts and three PASS lines.

**In [6], the 21 Christoffel symbols.**

```python
uu, vv, vd = sp.symbols("uu vv vd", real=True)  # u = b4'/b4, v = u', vd = v'
kk = sp.symbols("kk", real=True)  # k = e^(2 a4)/b4
for a, b, c in distinct:
    readable = sp.factor(sp.cancel(Gamma[a][b][c].subs(bd1, uu * bb)))
    say(f"Gamma^{NAMES[a]}_{NAMES[b]}{NAMES[c]} = {readable}")
```

Three new symbols for the record's variables: `uu` for $u = b_4'/b_4$, `vv` for $v = u'$, `vd` for $v'$, and `kk` for $k = e^{2a_4}/b_4$. For each distinct symbol, `.subs(bd1, uu * bb)` writes $b_4'$ as $u\,b_4$, `sp.factor` writes the result as a product, and `say` prints it. Out [6] lists the 21 symbols of Section 12.4: for example `Gamma^x0_x0x0 = -6*H*(t**2 + 1)/t` ($= -6H/(\sin z\cos z)$), `Gamma^x0_x0x4 = -(2*ad1 - uu)/2` ($= h$), `Gamma^x5_x0x5 = H/t` ($= H\cot z$) and `Gamma^x4_x5x5 = bb*w**2*(2*ad1 - uu)/(2*ea**2)` ($= h\,g_{55}$, since $g_{55} = -b_4w^2/e^{2a_4}$ and $-(2a_4' - u)/2 = h$).

**In [7], the Riemann tensor.**

```python
kp = sp.symbols("kp", positive=True)  # k as a positive symbol, used for the root
TO_RECORD = {bd2: (vv + uu ** 2) * bb, bd1: uu * bb}  # b4'' and b4' through u, v
```

`kp` is $k$ as a positive symbol: with it sympy may simplify $\sqrt{k\,b_4}^{\,2} = k\,b_4$. `TO_RECORD` replaces $b_4''$ by $(v + u^2)b_4$ (because $v = u' = b_4''/b_4 - u^2$) and $b_4'$ by $u\,b_4$.

```python
def record_form(expr):
    expr = sp.cancel(expr.subs(TO_RECORD))
    expr = sp.cancel(expr.subs(ea, sp.sqrt(kp * bb)))  # e^(a4) = (k b4)^(1/2)
    return sp.expand(expr).subs(kp, kk)
```

`record_form` writes an expression in the record's variables: first $b_4''$ and $b_4'$ are replaced, then $e^{a_4}$ by $\sqrt{k\,b_4}$ (from $k = e^{2a_4}/b_4$), each step followed by `sp.cancel`; finally the positive `kp` is renamed to the real symbol `kk`. If $b_4$ does not drop out, the result still contains `bb`; the next cell checks that it never does.

```python
R = {}  # R[(a, b, m, n)] = R^{ab}_{mn}; only the components that are not zero
for a, b, m, n in itertools.product(range(N), repeat=4):
    if a == b or m == n:
        continue  # antisymmetry: zero when the two indices of a pair are equal
    value = (d(Gamma[a][b][n], m) - d(Gamma[a][b][m], n)
             + sum(Gamma[a][m][e] * Gamma[e][b][n] - Gamma[a][n][e] * Gamma[e][b][m]
                   for e in range(N)))  # R^a_bmn in the MTW convention
    if value != 0:
        value = sp.cancel(value / g[b])  # raise the index b: multiply by g^bb
        if value != 0:
            R[(a, b, m, n)] = record_form(value)
```

`R` is a dictionary that will hold only the components that are not zero, with the key `(a, b, m, n)` for $R^{ab}{}_{mn}$. The loop visits all $8^4 = 4096$ index lists; `continue` skips the lists with $a = b$ or $m = n$, which are zero by antisymmetry. The value is the MTW formula of Section 12.5: two derivatives of Christoffel symbols and the two sums over $e$ of products. If it is not zero, dividing by $g_{bb}$ (that is, multiplying by $g^{bb}$) raises the second index, and the component is stored in the record's variables.

```python
ordered = {key: value for key, value in R.items()
           if key[0] < key[1] and key[2] < key[3]}  # a < b and m < n
report("nonzero components R^ab_mn of the 4096", len(R))
report("nonzero components with a < b and m < n", len(ordered))
```

`ordered` keeps the components with $a < b$ and $m < n$, one for each set of four orderings. `report` prints both counts (Out [7]): 112 and 28.

**In [8], the curvature checks.**

```python
free = all(not value.has(t) and not value.has(w) and not value.has(bb)
           for value in R.values())
reproduces(len(R) == 112 and free,
           "112 nonzero components R^ab_mn of the 4096, all free of x0",
           PY, "mixed_riemann_free_of_x0")
reproduces(len(ordered) == 28 and free,
           "28 nonzero components with a < b and m < n, all free of x0",
           WL, "mixed_riemann_free_of_x0")
```

`value.has(t)` is true when the expression contains the symbol `t`. `free` is true when no component contains $t$, $w$ or $b_4$: the curvature is free of $x_0$ at every real $z$, and $b_4$ enters only through $u$, $v$ and $k$. The two checks compare the counts 112 and 28 with the sympy and Wolfram reports (both name the check `mixed_riemann_free_of_x0`).

```python
sectional = all(set(key[:2]) == set(key[2:]) for key in R)
reproduces(sectional, "every nonzero R^ab_mn is sectional: no mixed component",
           PY, "mixed_riemann_only_sectional")
reproduces(sectional and len(ordered) == 28,
           "the 28 nonzero components are all of the form R^ab_ab",
           WARPED, "corrected_mixed_riemann_vanish")
```

`key[:2]` is the pair $(a, b)$ and `key[2:]` the pair $(m, n)$; `set` forgets their order. `sectional` is true when every nonzero component has $\{m, n\} = \{a, b\}$: no mixed component. The two checks reproduce the sympy report (`mixed_riemann_only_sectional`) and the metric report (`corrected_mixed_riemann_vanish`).

```python
polynomial = all(value.is_polynomial(H, ad1, ad2, uu, vv, kk) for value in R.values())
reproduces(polynomial, "every R^ab_mn is a polynomial in H, a4', a4'', u, v, k",
           PY, "riemann_entries_polynomial")
antisymmetric = all(R.get((b, a, m, n)) == -v and R.get((a, b, n, m)) == -v
                    for (a, b, m, n), v in R.items())
reproduces(antisymmetric, "R^ab_mn = -R^ba_mn = -R^ab_nm",
           PY, "riemann_pair_antisymmetry")
```

`is_polynomial(H, ad1, ad2, uu, vv, kk)` is true when the expression is a polynomial in these six symbols (no division by them, no roots). The antisymmetry check looks up, for each stored component, the components with $a, b$ exchanged and with $m, n$ exchanged (`R.get` returns `None` for a missing key, which would fail the comparison) and requires both to be its negative. Out [8] shows six PASS lines, each with the record it reproduces.

**In [9], the five groups of sectional curvatures.**

```python
groups = {}  # printed value -> the planes that have it
for (a, b, m, n), value in ordered.items():
    groups.setdefault(str(sp.factor(value)), []).append(NAMES[a] + NAMES[b])
for value, members in groups.items():
    say(f"{value} ({len(members)}): " + " ".join(members))
```

`groups` is a dictionary from the printed value to the list of planes that have it; `setdefault(key, [])` returns the list stored under the key, creating an empty one the first time, and `.append` adds the plane, written as `x1x2` for the plane of $x_1$ and $x_2$. Out [9] prints five lines, in the order in which the values first appear: `-ad1*(2*ad1 - uu)/2` for 12 planes ($a_4'h$: a 3-space direction with a block direction), `(4*ad1**2 - 4*ad1*uu - 4*ad2 + uu**2 + 2*vv)/4` for 4 planes ($h' + h^2$: the time with a block direction), `-(4*H**2*kk - 4*ad1**2 + 4*ad1*uu - uu**2)/4` for 6 planes ($h^2 - H^2k$: two block directions), `ad1**2` for 3 planes and `ad1**2 + ad2` for 3 planes: the table of Section 12.5.

**In [10], figure 12a.1: the curvature as two tables.**

```python
SAMPLE = {H: 1, ad1: sp.Rational(3, 5), ad2: sp.Rational(3, 10), uu: sp.Rational(4, 5),
          vv: sp.Rational(1, 10), kk: sp.Rational(3, 2)}  # the sample point
pairs = np.zeros((N, N))  # the sectional curvatures K_ab
for (a, b, m, n), value in ordered.items():
    pairs[a, b] = pairs[b, a] = float(value.subs(SAMPLE))
PAIRS28 = [(a, b) for a in range(N) for b in range(a + 1, N)]  # the 28 planes
```

`SAMPLE` is the sample point $H = 1$, $a_4' = 0.6$, $a_4'' = 0.3$, $u = 0.8$, $v = 0.1$, $k = 1.5$, written with exact fractions. `pairs` is an 8 by 8 array of zeros (`np.zeros`); the loop puts each sectional curvature, evaluated at the sample point and turned into a floating-point number with `float`, at the positions $(a, b)$ and $(b, a)$. At this point $h = 0.4 - 0.6 = -0.2$, so the five values are $(a_4')^2 = 0.36$, $a_4'' + (a_4')^2 = 0.66$, $a_4'h = -0.12$, $h' + h^2 = 0.05 - 0.3 + 0.04 = -0.21$ and $h^2 - H^2k = 0.04 - 1.5 = -1.46$. `PAIRS28` lists the 28 planes $(a, b)$ with $a < b$.

```python
table = np.zeros((28, 28))
for i, (a, b) in enumerate(PAIRS28):
    for j, (m, n) in enumerate(PAIRS28):
        if (a, b, m, n) in R:
            table[i, j] = float(R[(a, b, m, n)].subs(SAMPLE))
limit = np.abs(table).max()  # one colour scale for both panels
```

`table` is the 28 by 28 array of all components $R^{ab}{}_{mn}$ with $a < b$ (row) and $m < n$ (column); a component missing from `R` stays zero. `limit` is the largest absolute value, 1.46, used as the colour scale of both panels.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(12.0, 5.6))
left.imshow(pairs, cmap="RdBu_r", vmin=-limit, vmax=limit)
for a in range(N):
    for b in range(N):
        if a != b:  # the value in each cell off the diagonal
            ink = "white" if abs(pairs[a, b]) > 0.6 * limit else "black"
            left.text(b, a, f"{pairs[a, b]:.2f}", ha="center", va="center",
                      fontsize=6, color=ink)
```

`plt.subplots(1, 2, figsize=(12.0, 5.6))` makes a figure with two panels side by side, 12 by 5.6 inches. `imshow` draws the array `pairs` as coloured squares, with the colour map `"RdBu_r"` (red for positive, blue for negative, white for zero) on the symmetric scale from `-limit` to `limit`. The double loop writes each value off the diagonal into its square with two decimals (`f"{...:.2f}"`), in white on a dark square and in black otherwise.

```python
left.set_xticks(range(N))
left.set_xticklabels(NAMES, fontsize=7)
left.set_yticks(range(N))
left.set_yticklabels(NAMES, fontsize=7)
left.grid(False)
left.set_title("sectional curvatures $K_{ab} = R^{ab}{}_{ab}$", fontsize=10)
```

Tick marks at the eight positions, labelled with the names of the coordinates, no grid lines over the squares, and the title of the left panel.

```python
image = right.imshow(table, cmap="RdBu_r", vmin=-limit, vmax=limit)
labels = [NAMES[a] + NAMES[b] for a, b in PAIRS28]
right.set_xticks(range(28))
right.set_xticklabels(labels, rotation=90, fontsize=5)
right.set_yticks(range(28))
right.set_yticklabels(labels, fontsize=5)
```

The right panel draws `table` on the same scale; `image` keeps the drawing for the colour bar. Its 28 rows and columns are labelled with the planes, the column labels turned by 90 degrees and printed small.

```python
right.grid(False)
right.set_title("all $R^{ab}{}_{mn}$, $a<b$, $m<n$", fontsize=10)
fig.colorbar(image, ax=right, shrink=0.8, label="value (units of $H^2$)")
save_figure(fig, "pair_curvatures",
            "The curvature of the corrected metric at the sample point $H = 1$, "
...)
```

No grid, a title, and `fig.colorbar` adds the colour bar with its label. `save_figure` (In [1]) saves the figure as `12a_1_pair_curvatures.png`, records the caption, shows the picture and prints Figure 12a.1 saved as Revision/textbook/figures/12a_1_pair_curvatures.png (Out [10]). In the figure the left panel shows the five groups as blocks of equal colour, and the right panel is coloured only on its diagonal: there is no mixed curvature component.

**In [11], the Ricci tensor, the Ricci scalar and the Einstein tensor.**

```python
Ricci = [[sp.expand(sum(R.get((a, h, a, j), 0) for a in range(N)))
          for j in range(N)] for h in range(N)]  # R^h_j
ricci_scalar = sp.expand(sum(Ricci[h][h] for h in range(N)))
G = [[sp.expand(Ricci[h][j] - (ricci_scalar / 2 if h == j else 0))
      for j in range(N)] for h in range(N)]  # G^h_j
report("Ricci scalar R", ricci_scalar)
for h in range(N):
    say(f"G^{NAMES[h]}_{NAMES[h]} = {G[h][h]}")
```

`Ricci[h][j]` is $R^h{}_j = \sum_a R^{ah}{}_{aj}$; `R.get(key, 0)` returns 0 for a component that is not stored. `ricci_scalar` is the sum of the diagonal, and `G` is $G^h{}_j = R^h{}_j - \tfrac12\delta^h_jR$ (the conditional expression `ricci_scalar / 2 if h == j else 0` is the Kronecker delta at work). `sp.expand` multiplies everything out, so that equal expressions are recognised as equal. Out [11] prints `RESULT Ricci scalar R = -12*H**2*kk + 8*ad1**2 - 8*ad1*uu - 2*ad2 + 5*uu**2 + 4*vv` and the eight diagonal components of $G$: three different expressions, those of Section 12.6.

**In [12], the Einstein tensor against the records.**

```python
reproduces(all(G[h][j] == 0 for h in range(N) for j in range(N) if h != j),
           "G^h_j is diagonal: every off-diagonal component vanishes",
           LEAD, "einstein_off_diagonal_vanish")
reproduces(G[1][1] == G[2][2] == G[3][3] and G[0][0] == G[5][5] == G[6][6] == G[7][7],
           "G^x1_x1 = G^x2_x2 = G^x3_x3 and G^x0_x0 = G^x5_x5 = G^x6_x6 = G^x7_x7",
           LEAD, "einstein_isotropy")
```

The first check requires every off-diagonal component to vanish, the second the equalities $G^{x_1}{}_{x_1} = G^{x_2}{}_{x_2} = G^{x_3}{}_{x_3}$ and $G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5} = G^{x_6}{}_{x_6} = G^{x_7}{}_{x_7}$ (Python allows a chain of `==`); both against the lead's Einstein report.

```python
reproduces(all(G[h][h].is_polynomial(H, ad1, ad2, uu, vv, kk) for h in range(N)),
           "every component of G is free of x0, a polynomial in a4', a4'', u, v, k",
           LEAD, "einstein_diagonal_x0_independent")
expected = {4: 3 * ad1 ** 2 + 6 * H ** 2 * kk - sp.Rational(3, 2) * uu ** 2,
            1: (-5 * ad1 ** 2 + 6 * ad1 * uu + 2 * ad2 - sp.Rational(5, 2) * uu ** 2
                - 2 * vv + 6 * H ** 2 * kk),
            0: (-3 * ad1 ** 2 + sp.Rational(3, 2) * (ad1 * uu - uu ** 2 - vv)
                + 3 * H ** 2 * kk)}
```

Every diagonal component must be a polynomial in the six record variables, hence free of $x_0$ (lead's Einstein report, `einstein_diagonal_x0_independent`). `expected` holds the three components of Section 12.6, keyed by their positions 4, 1 and 0.

```python
reproduces(all(sp.expand(G[i][i] - v) == 0 for i, v in expected.items()),
           "the three Einstein components agree with the record",
           PY, "einstein_components")
EA, bd1_r, bd2_r = sp.symbols("EA bd1 bd2", real=True)  # the names of the file
metric_record = read_json(METRIC_RESULTS)["einstein_diagonal"]
same = True
```

The three components must equal the expected ones (sympy report, `einstein_components`). The next lines prepare the comparison with the record of the corrected metric, whose file writes $e^{a_4}$ as `EA`, $b_4$ as `bb` and $b_4'$, $b_4''$ as `bd1`, `bd2`: three symbols with these names, the dictionary `einstein_diagonal` of the file, and a truth value `same` that starts as `True`.

```python
for key, position in (("x0", 0), ("x1", 1), ("x4", 4), ("x5", 5)):
    text = metric_record[key]
    mine = sp.sympify(text, locals={"EA": EA, "H": H, "ad1": ad1, "ad2": ad2,
                                    "bb": bb, "bd1": bd1_r, "bd2": bd2_r})
    mine = mine.subs({bd2_r: (vv + uu ** 2) * bb, bd1_r: uu * bb, EA: sp.sqrt(kp * bb)})
    same = same and sp.expand(sp.cancel(mine).subs(kp, kk) - G[position][position]) == 0
```

For the four stored components, `sp.sympify` turns the text of the record into a sympy expression (the dictionary `locals` says which symbol each name means); the substitutions express it in $u$, $v$ and $k$; and `same` stays true only if every difference from $G$ is zero (`same and ...` is false as soon as one comparison fails).

```python
reproduces(same, "G equals the record of the corrected metric (einstein_diagonal)",
           PY, "einstein_equals_metric_warped_record")
scalar = (-12 * H ** 2 * kk + 8 * ad1 ** 2 - 2 * ad2 - 8 * ad1 * uu
          + 4 * (vv + uu ** 2) + uu ** 2)  # the record: 4 b4''/b4 + u^2
reproduces(sp.expand(ricci_scalar - scalar) == 0 and Ricci[0][0] == Ricci[5][5]
           and all(Ricci[h][j] == 0 for h in range(N) for j in range(N) if h != j),
           "R = -12 H^2 k + 8 a4'^2 - 2 a4'' - 8 a4' u + 4 b4''/b4 + u^2; Ricci "
           "diagonal", FIELD, "ricci_scalar")
```

The comparison is reported against the sympy report, which made the same comparison (`einstein_equals_metric_warped_record`). Then the Ricci scalar is compared with the field-theory record's form $-12H^2k + 8(a_4')^2 - 2a_4'' - 8a_4'u + 4b_4''/b_4 + u^2$, where $4b_4''/b_4 = 4(v + u^2)$, together with $R^{x_0}{}_{x_0} = R^{x_5}{}_{x_5}$ and a diagonal Ricci tensor. Out [12] shows six PASS lines.

**In [13], figure 12a.2: the Einstein tensor along the record history.**

```python
HISTORY = {ad1: H, ad2: 0, uu: sp.Rational(4, 3) * H, vv: 0}  # the record history
g_history = {i: sp.expand(G[i][i].subs(HISTORY).subs(H, 1)) for i in (4, 1, 0)}
for i, value in g_history.items():
    say(f"on the record history: G^{NAMES[i]}_{NAMES[i]} = {sp.factor(value)}")
x_axis = np.linspace(0.0, 3.0, 301)  # the time x4 in units 1/H
k_axis = np.exp(2.0 * x_axis / 3.0)  # k = e^(2 x4/3)
```

`HISTORY` inserts the record history: $a_4' = H$, $a_4'' = 0$, $u = \tfrac43H$, $v = 0$. `g_history` is a dictionary comprehension that evaluates the components at positions 4, 1 and 0 there, with $H = 1$; the loop prints them factorised (Out [13]): `(18*kk + 1)/3`, `(54*kk - 13)/9` and `(9*kk - 11)/3`, the values of Section 12.6. `np.linspace(0.0, 3.0, 301)` makes 301 equally spaced times from 0 to 3, and `k_axis` the values $k = e^{2x_4/3}$ there.

```python
fig, ax = plt.subplots()
styles = {4: ("-", "$G^{x_4}{}_{x_4}$ (constraint)"),
          1: ("--", "$G^{x_1}{}_{x_1}$ (3-space)"),
          0: (":", "$G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5}$ (block)")}
for i, (style, label) in styles.items():
    function = sp.lambdify(kk, g_history[i], "numpy")
    ax.plot(x_axis, function(k_axis) * np.ones_like(x_axis), style, label=label)
```

`styles` gives each component a line style and a legend text. `sp.lambdify(kk, expression, "numpy")` turns a sympy expression in `kk` into a fast numpy function; it is evaluated on all 301 values at once. The factor `np.ones_like(x_axis)` (an array of ones) makes the result an array of the right length even when the expression is a constant.

```python
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("time $x_4$ (units $1/H$)")
ax.set_ylabel("component of $G^\\mu{}_\\nu$ (units of $H^2$)")
ax.set_title("The Einstein tensor along the record history")
ax.legend(fontsize=8)
save_figure(fig, "einstein_components",
            "The three distinct components of the Einstein tensor of the corrected "
...)
```

A black line at zero, the axis labels, the title, the legend and `save_figure` (the caption is printed under figure 12a.2 in Section 12.15). All three curves rise with $k$; the 3-space and block components differ at every time.

**In [14], the generalized Kronecker delta.**

```python
def gkd(upper, lower):
    if len(set(upper)) != len(upper) or sorted(upper) != sorted(lower):
        return 0
    position = [upper.index(index) for index in lower]  # where each one sits
    inversions = sum(1 for i in range(len(position))
                     for j in range(i + 1, len(position))
                     if position[i] > position[j])
    return -1 if inversions % 2 else 1
```

`gkd(upper, lower)` returns 0 when an upper index repeats (`set` removes repetitions, so the lengths differ) or when the two lists do not hold the same indices (`sorted` lists differ). Otherwise `position` records, for each lower index, where it sits in the upper list; this is a rearrangement of $0, 1, \dots, n - 1$. Its **inversions** are the pairs of positions $i < j$ with `position[i] > position[j]`; the generator expression inside `sum` counts them. An even number of inversions means an even rearrangement (sign $+1$), an odd number an odd one (sign $-1$); `inversions % 2` is the remainder after division by 2.

```python
say(f"gkd([1, 2], [1, 2]) = {gkd([1, 2], [1, 2])}, gkd([1, 2], [2, 1]) = "
    f"{gkd([1, 2], [2, 1])}, gkd([1, 1], [1, 1]) = {gkd([1, 1], [1, 1])}")
nine = list(range(8)) + [0]  # nine indices from eight values: one repeats
reproduces(gkd(nine, nine) == 0 and gkd(list(range(8)), list(range(8))) == 1,
           "a GKD of 9 indices in 8 dimensions is 0: P_(4) = 0",
           WL, "P4_vanishes_pigeonhole")
```

Three small examples are printed (Out [14]): `gkd([1, 2], [1, 2]) = 1`, `gkd([1, 2], [2, 1]) = -1` and `gkd([1, 1], [1, 1]) = 0`. `nine` is the list $0, 1, \dots, 7, 0$: nine indices from eight values, so one repeats and the delta is 0, while eight different indices in the same order give $+1$. The check reproduces the Wolfram report's `P4_vanishes_pigeonhole`: there is no fourth Lovelock tensor.

**In [15], the three Lovelock tensors.**

```python
GENERATORS = (H, ad1, ad2, uu, vv, kk)
FACTORS = [(key, sp.Poly(value, *GENERATORS)) for key, value in ordered.items()]
```

`GENERATORS` are the six symbols in which every curvature component is a polynomial. `FACTORS` pairs each of the 28 components with $a < b$, $m < n$ with its value as a `sp.Poly`, sympy's fast form of a polynomial.

```python
def lovelock(k):
    zero = sp.Poly(0, *GENERATORS)
    P = [[zero] * N for _ in range(N)]
    L = zero
    terms = 0
    for factors in itertools.product(FACTORS, repeat=k):
        lower = [i for key, _ in factors for i in key[0:2]]  # upper indices of R
        upper = [i for key, _ in factors for i in key[2:4]]  # lower indices of R
        if len(set(lower)) < 2 * k or len(set(upper)) < 2 * k:
            continue  # a repeated index: the GKD is zero
        terms += 1
        product = sp.Poly(4 ** k, *GENERATORS)  # the factor 4^k
        for _, poly in factors:
            product = product * poly
        L = L + gkd(upper, lower) * product
        for h, j in itertools.product(range(N), repeat=2):
            sign = gkd([h] + upper, [j] + lower)
            if sign:
                P[h][j] = P[h][j] + sign * product
    P = [[sp.expand(P[h][j].as_expr()) for j in range(N)] for h in range(N)]
    return P, sp.expand(L.as_expr()), terms
```

`lovelock(k)` computes $P_{(k)}$, the Lovelock scalar $L_{(k)}$ and the number of contributing index lists. `zero` is the zero polynomial; `P` starts as an 8 by 8 table of zeros. `itertools.product(FACTORS, repeat=k)` visits every ordered list of $k$ components. In $P_{(k)}{}^h{}_j$ the curvature factor $R^{j_1j_2}{}_{h_1h_2}$ gives its upper indices to the LOWER list of the delta and its lower indices to the UPPER list; hence the names: `lower` collects `key[0:2]` (the pairs $a, b$) of every factor and `upper` collects `key[2:4]` (the pairs $m, n$). A list with a repeated index gives a delta of 0 and is skipped. The sum runs only over components with $a < b$, $m < n$; each also appears in the full sum in four orders (exchanging $a, b$ or $m, n$ changes the sign of $R$ and of the delta together), so every product is multiplied by $4^k$. Each product adds to $L_{(k)}$ with the delta of the two lists, and to each $P_{(k)}{}^h{}_j$ with the delta of the lists extended by $h$ and $j$. At the end the polynomials are turned back into expanded expressions (`as_expr`).

```python
P, Lscalar, E = {}, {}, {}
for k in (1, 2, 3):
    P[k], Lscalar[k], terms = lovelock(k)
    E[k] = [[sp.expand(-P[k][h][j] / 2 ** (k + 1)) for j in range(N)]
            for h in range(N)]  # E_(k) = -P_(k)/2^(k+1)
    say(f"k = {k}: {terms} lists of index pairs contribute; L_({k}) has "
        f"{len(Lscalar[k].args)} terms")
say(f"L_(1) = {Lscalar[1]}")
```

For $k = 1, 2, 3$ the cell computes $P_{(k)}$ and $L_{(k)}$ and forms $E_{(k)} = -P_{(k)}/2^{k+1}$ in all 64 components. It prints the number of contributing lists and the number of terms of $L_{(k)}$ (`.args` of a sum are its terms), and $L_{(1)}$ itself. Out [15]: 28, 420 and 2520 lists contribute. These numbers count ordered lists of disjoint planes: 28 planes; $28\cdot 15 = 420$ (a second plane must avoid the two directions of the first, which leaves $\binom62 = 15$ planes); $420\cdot 6 = 2520$ (a third plane has $\binom42 = 6$ choices). $L_{(1)}$ = `-24*H**2*kk + 16*ad1**2 - 16*ad1*uu - 4*ad2 + 10*uu**2 + 8*vv`, which is $-2R$. This cell takes about ten seconds.

**In [16], the Lovelock tensors against the records.**

```python
reproduces(all(sp.expand(E[1][h][j] - G[h][j]) == 0
               for h in range(N) for j in range(N)),
           "E_(1) = G in all 64 components (P_(1) = -4 G)",
           PY, "P1_equals_minus_4_Einstein")
lovelock_json = read_json(LOVELOCK)
```

$E_{(1)}$ must equal $G$ in all 64 components (sympy report, `P1_equals_minus_4_Einstein`). `lovelock_json` holds the output of the Rust program of the GKD record.

```python
def from_mathematica(text):
    for old, new in (("Derivative[2][b4][x4]", "((vv + uu**2)*bb)"),
                     ("Derivative[1][b4][x4]", "(uu*bb)"),
                     ("Derivative[2][a4][x4]", "ad2"),
                     ("Derivative[1][a4][x4]", "ad1"),
                     ("E^(4*a4[x4])", "(kk*bb)**2"), ("E^(2*a4[x4])", "(kk*bb)"),
                     ("b4[x4]", "bb"), ("^", "**")):
        text = text.replace(old, new)
    names = {"H": H, "ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk, "bb": bb}
    return sp.expand(sp.sympify(text, locals=names))
```

The Rust record stores the scalars $L_{(k)}$ as texts in the Wolfram Language, with `b4[x4]`, `Derivative[1][b4][x4]` for $b_4'$, `E^(2*a4[x4])` for $e^{2a_4}$ and `^` for a power. `from_mathematica` replaces these pieces, in an order that keeps the longer names from being cut by the shorter ones, by expressions in $u$, $v$, $k$ and $b_4$ ($b_4'' = (v + u^2)b_4$, $b_4' = u\,b_4$, $e^{2a_4} = k\,b_4$), and turns the text into an expanded sympy expression.

```python
for k in (1, 2, 3):
    Ek = E[k]
    structure = (all(Ek[h][j] == 0 for h in range(N) for j in range(N) if h != j)
                 and Ek[1][1] == Ek[2][2] == Ek[3][3]
                 and Ek[0][0] == Ek[5][5] == Ek[6][6] == Ek[7][7]
                 and all(Ek[h][h].is_polynomial(*GENERATORS) for h in range(N)))
    reproduces(structure, f"E_({k}) diagonal, x1 = x2 = x3, x0 = x5 = x6 = x7",
               PY, f"P{k}_structure")
    trace = sp.expand(sum(P[k][h][h] for h in range(N)) - (8 - 2 * k) * Lscalar[k])
    reproduces(trace == 0, f"trace identity sum_h P_({k})^h_h = (8 - {2 * k}) L_({k})",
               PY, f"P{k}_trace_identity")
    rust = from_mathematica(lovelock_json[f"L{k}"])
    reproduces(sp.expand(rust - Lscalar[k]) == 0,
               f"L_({k}) equals the Rust GKD program", PY, f"L{k}_equals_gkd_branch")
```

For each order the loop checks the structure (all off-diagonal components zero; equal in $x_1, x_2, x_3$; equal in $x_0, x_5, x_6, x_7$; polynomials), the trace identity $\sum_hP_{(k)}{}^h{}_h = (8 - 2k)L_{(k)}$, and that the Rust scalar minus ours is zero. Each check names its sympy-report counterpart, built with an f-string: `P{k}_structure`, `P{k}_trace_identity`, `L{k}_equals_gkd_branch`.

```python
K_plane = {(a, b): value for (a, b, m, n), value in ordered.items()}  # K_ab, a < b
counting = True
for k, h in itertools.product((1, 2, 3), range(N)):
    planes = [plane for plane in K_plane if h not in plane]  # the planes without h
    total = sum((sp.Mul(*[K_plane[plane] for plane in chosen])
                 for chosen in itertools.combinations(planes, k)
                 if len({i for plane in chosen for i in plane}) == 2 * k), 0)
    counting = counting and sp.expand(-sp.factorial(k) * 2 ** (k - 1) * total
                                      - E[k][h][h]) == 0
```

`K_plane` maps each plane $(a, b)$ to its sectional curvature (the entries of `ordered` have $m = a$, $n = b$). For every order $k$ and every direction $h$ the loop lists the planes without $h$, and sums the products of the curvatures over all sets of $k$ of them (`itertools.combinations` gives unordered sets) whose $2k$ indices are all different, that is, sets of disjoint planes. `counting` stays true only if $-k!\,2^{k-1}$ times this sum equals $E_{(k)}{}^h{}_h$, the collapsed formula of Section 12.7.

```python
check(counting, "E_(k)^h_h = -k! 2^(k-1) x the sum over k disjoint planes without h "
      "of the products of their K (k = 1, 2, 3)")
```

The check of that formula. Out [16] shows ten PASS lines: $E_{(1)} = G$, then structure, trace identity and Rust scalar for each of the three orders, and the collapsed formula.

**In [17], all components against the Rust program and the Wolfram record.**

```python
Q = sp.symbols("Q", positive=True)  # Q = b4^(1/2)
```

`Q` is $b_4^{1/2}$, positive.

```python
def from_monomials(monomials):
    total = sp.Integer(0)
    for numerator, denominator, exponents in monomials:
        if any(exponents[i] for i in (3, 4, 6, 7, 11, 12, 13)):
            raise ValueError(f"unexpected exponents {exponents}")
        term = sp.Rational(numerator, denominator)
        term *= H ** exponents[0] * ad1 ** exponents[1] * ad2 ** exponents[2]
        term *= (sp.sqrt(kp) * Q) ** exponents[5] * Q ** exponents[8]
        term *= (uu * Q ** 2) ** exponents[9]  # b4' = u b4
        term *= ((vv + uu ** 2) * Q ** 2) ** exponents[10]  # b4'' = (v + u^2) b4
        total += term
    return sp.expand(total).subs(kp, kk)
```

The Rust record stores every component of $P_{(k)}{}^h{}_j$ as a list of monomials: a numerator, a denominator and 14 exponents, of $H$, $a_4'$, $a_4''$, $a_4'''$, $a_4''''$, $E = e^{a_4}$, $W = (\sin^2 z)^{1/12}$, $C = \cot z$, $Q = b_4^{1/2}$, $b_4'$, $b_4''$, $b_4'''$, $b_4''''$ and the sign of $\cot z$, in this order. `from_monomials` stops with an error if a monomial contains $a_4'''$, $a_4''''$, $W$, $C$, the sign, $b_4'''$ or $b_4''''$ (positions 3, 4, 6, 7, 11, 12, 13), because the components must not. It builds each term from the fraction and the powers, with $E = \sqrt{k}\,Q$, $b_4' = uQ^2$ and $b_4'' = (v + u^2)Q^2$, adds the terms, expands, and renames `kp` to `kk`. If the powers of $Q$ did not cancel, the comparison below would fail.

```python
for k in (1, 2, 3):
    block = lovelock_json[f"P{k}_mixed_up_h_down_j"]
    same = all(sp.expand(from_monomials(block[f"{NAMES[h]},{NAMES[j]}"]["monomials"])
                         - P[k][h][j]) == 0 for h in range(N) for j in range(N))
    reproduces(same, f"all 64 components of P_({k}) equal the Rust GKD record",
               PY, f"P{k}_equals_gkd_branch_monomials")
equations_json = read_json(EQUATIONS)
LOCALS = {"ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk, "H": H}
```

For each order the stored block `P{k}_mixed_up_h_down_j` holds the 64 components under keys such as `"x0,x4"`; each is rebuilt and compared with the notebook's (sympy report, checks `P1_equals_gkd_branch_monomials` to `P3_equals_gkd_branch_monomials`). Then the equations of the Wolfram record are read, and `LOCALS` says which symbol each name of the record means.

```python
def parse(text, names=None):
    return sp.sympify(text.replace("^", "**"), locals=names or LOCALS)
```

`parse` turns a Wolfram text of the record into a sympy expression: `^` becomes `**`, and the names are those of `LOCALS` unless another dictionary is given (`names or LOCALS` uses `LOCALS` when `names` is `None`).

```python
POSITIONS = {"x0x0": 0, "x1x1": 1, "x4x4": 4, "x5x5": 5}
same = all(sp.expand(parse(equations_json["lovelockTensors"][f"E{k}"][key]["input"])
                     - E[k][i][i]) == 0
           for k in (1, 2, 3) for key, i in POSITIONS.items())
reproduces(same, "E_(1), E_(2), E_(3) equal the Wolfram record a4-equations.json",
           PY, "json_lovelock_components")
```

The record stores four components of each $E_{(k)}$, under the keys `x0x0`, `x1x1`, `x4x4` and `x5x5`; `POSITIONS` gives their positions. All twelve must equal the notebook's (sympy report, `json_lovelock_components`). Out [17] shows four PASS lines.

**In [18], an independent route to $E_{(2)}$: the Gauss-Bonnet tensor of Lanczos.**

```python
def contract(mu, nu):
    term_a = ricci_scalar * Ricci[mu][nu]
    term_b = sum(Ricci[mu][a] * Ricci[a][nu] for a in range(N))
    term_c = sum(R.get((mu, a, nu, b), 0) * Ricci[b][a]
                 for a in range(N) for b in range(N))
    term_d = sum(R.get((mu, a, b, c), 0) * R.get((b, c, nu, a), 0)
                 for a in range(N) for b in range(N) for c in range(N))
    return 2 * (term_a - 2 * term_b - 2 * term_c + term_d)
```

`contract(mu, nu)` computes the bracket of the Lanczos formula of the notebook's text: $R\,R^\mu{}_\nu$, then $\sum_aR^\mu{}_aR^a{}_\nu$, then $\sum_{a,b}R^{\mu a}{}_{\nu b}R^b{}_a$, then $\sum_{a,b,c}R^{\mu a}{}_{bc}R^{bc}{}_{\nu a}$, and returns twice the combination with the coefficients $1, -2, -2, 1$.

```python
gauss_bonnet_scalar = (ricci_scalar ** 2
                       - 4 * sum(Ricci[a][b] * Ricci[b][a]
                                 for a in range(N) for b in range(N))
                       + sum(v * R.get((m, n, a, b), 0)
                             for (a, b, m, n), v in R.items()))
lanczos = [[sp.expand(contract(mu, nu)
                      - (gauss_bonnet_scalar / 2 if mu == nu else 0))
            for nu in range(N)] for mu in range(N)]
```

The Gauss-Bonnet scalar $R^2 - 4R^a{}_bR^b{}_a + R^{ab}{}_{mn}R^{mn}{}_{ab}$: the last sum runs over the stored components and multiplies each by its partner with the pairs exchanged. `lanczos` is then the Lanczos tensor, the bracket minus half the scalar on the diagonal.

```python
check(all(sp.expand(lanczos[h][j] - E[2][h][j]) == 0
          for h in range(N) for j in range(N)),
      "E_(2) (GKD) equals the classical Gauss-Bonnet tensor for every a4 and b4")
A, beta = sp.symbols("A beta", real=True)  # the exponential history
EXPONENTIAL = {ad1: A * H, ad2: 0, uu: beta * A * H, vv: 0}
lead_formula = (-3 * H ** 4 * (A ** 4 * beta ** 4 + 16 * A ** 4 * beta ** 3
                               - 48 * A ** 4 * beta ** 2 + 48 * A ** 4
                               - 8 * A ** 2 * beta ** 2 * kk - 64 * A ** 2 * beta * kk
                               + 64 * A ** 2 * kk + 16 * kk ** 2) / 4)
```

The Lanczos tensor must equal $E_{(2)}$ in all 64 components, for every $a_4$ and $b_4$: two completely different computations of the same tensor (no GKD in the second). Then the exponential history is defined as a substitution, $a_4' = AH$, $u = \beta AH$, $a_4'' = v = 0$, and `lead_formula` is the lead's formula for its time component.

```python
reproduces(sp.expand(lanczos[4][4].subs(EXPONENTIAL) - lead_formula) == 0,
           "exponential history: H^x4_x4 equals the lead's formula",
           LEAD, "gauss_bonnet_diagonal")
alpha2 = sp.symbols("alpha2", real=True)
required = equations_json["exponentialHistory"]["requiredSource"]
names_exp = {"AA": A, "be": beta, "H": H, "kk": kk, "alpha2": alpha2}
```

On the exponential histories the time component of the Lanczos tensor must equal the lead's formula (lead's Einstein report, `gauss_bonnet_diagonal`). `required` is the record's source of the exponential histories, and `names_exp` says which symbol each of its names means (`AA` for $A$, `be` for $\beta$).

```python
parts = {key: sp.diff(sp.sympify(required[key]["input"].replace("^", "**"),
                                 locals=dict(names_exp, kappa=sp.Integer(1))), alpha2)
         for key in ("rho", "p3", "p0", "pt")}
signs = {"rho": (4, -1), "p3": (1, 1), "p0": (0, 1), "pt": (5, 1)}
reproduces(all(sp.expand(parts[key] - sign * lanczos[i][i].subs(EXPONENTIAL)) == 0
               for key, (i, sign) in signs.items()),
           "the alpha2 parts of the required source are -H^x4_x4, H^x1_x1, H^x0_x0",
           LEAD, "gauss_bonnet_source_alpha2")
```

`sp.diff(..., alpha2)` takes the part of each required source that is multiplied by $\alpha_2$ (with $\kappa = 1$). Since $\kappa\rho = -(e_{44} + \Lambda)$ and $\kappa p = e_{hh} + \Lambda$, these parts must be $-H^{x_4}{}_{x_4}$ for $\rho$ and $+H^{x_1}{}_{x_1}$, $+H^{x_0}{}_{x_0}$, $+H^{x_5}{}_{x_5}$ for $p_3$, $p_0$, $p_t$; `signs` holds the position and the sign for each. Out [18] shows three PASS lines.

**In [19], the Bianchi identity.**

```python
RATE_RECORD = {ad1: ad2, ad2: ad3, uu: vv, vv: vd, kk: kk * (2 * ad1 - uu)}
```

`RATE_RECORD` gives the time derivative of each record variable: $a_4' \to a_4''$, $a_4'' \to a_4'''$, $u \to v$, $v \to v'$ (`vd`) and $k \to k(2a_4' - u)$, because $\ln k = 2a_4 - \ln b_4$ has the derivative $2a_4' - u$.

```python
def d4_record(expr):
    return sp.expand(sum(sp.diff(expr, s) * r for s, r in RATE_RECORD.items()))
```

`d4_record` is the chain rule with these rates, for an expression in the record's variables.

```python
trace_gamma = [record_form(sum(Gamma[m][m][nu] for m in range(N))) for nu in range(N)]
say(f"sum_mu Gamma^mu_mu x4 = {trace_gamma[4]}, sum_mu Gamma^mu_mu x0 = "
    f"{trace_gamma[0]}")
```

`trace_gamma` holds $\sum_\mu\Gamma^\mu{}_{\mu\nu}$ for every $\nu$, in the record's variables; the cell prints the two that are not zero (Out [19]): `-ad1 + 2*uu` for $\nu = x_4$ ($3a_4' + 4h = 2u - a_4'$, the rate of the volume of Section 12.3) and `-6*H*t - 3*H/t` for $\nu = x_0$ ($\Gamma^{x_0}{}_{x_0x_0} + 3H\cot z$).

```python
def divergence_diagonal(T):
    values = []
    for nu in range(N):
        value = d4_record(T[4][4]) if nu == 4 else 0
        value += sum(record_form(Gamma[m][m][nu]) * (T[nu][nu] - T[m][m])
                     for m in range(N))
        values.append(sp.expand(value))
    return values
```

`divergence_diagonal(T)` is the formula of Section 12.10 for a diagonal tensor that depends on $x_4$ only: for each $\nu$, the derivative $\partial_4T^{x_4}{}_{x_4}$ when $\nu = x_4$ (zero otherwise), plus the sum over $m$ of $\Gamma^m{}_{m\nu}(T^\nu{}_\nu - T^m{}_m)$.

```python
for k in (1, 2, 3):
    reproduces(all(value == 0 for value in divergence_diagonal(E[k])),
               f"nabla_mu E_({k})^mu_nu = 0 for nu = x0..x7",
               PY, f"E{k}_divergence_free")
```

All eight divergences of each $E_{(k)}$ must vanish identically (sympy report, `E1_divergence_free` to `E3_divergence_free`). Out [19] shows three PASS lines after the printed sums.

**In [20], figure 12a.3: the three Lovelock tensors as heat maps.**

```python
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.4))
for ax, k in zip(axes, (1, 2, 3)):
    values = np.array([[float(E[k][h][j].subs(SAMPLE)) for j in range(N)]
                       for h in range(N)])
    scale = np.abs(values).max()
    ax.imshow(values, cmap="RdBu_r", vmin=-scale, vmax=scale)
    for h in range(N):  # write each diagonal value into its cell
        value = values[h, h]
        ink = "white" if abs(value) > 0.6 * scale else "black"  # readable on dark
        ax.text(h, h, f"{value:.2f}", ha="center", va="center", fontsize=6.5,
                color=ink)
    ax.set_xticks(range(N))
    ax.set_xticklabels(NAMES, fontsize=7)
    ax.set_yticks(range(N))
    ax.set_yticklabels(NAMES, fontsize=7)
    ax.grid(False)
    ax.set_title(f"$E_{{({k})}}{{}}^h{{}}_j$")
```

Three panels side by side. For each order the 64 components are evaluated at the sample point of In [10] into an 8 by 8 array, drawn with their own symmetric colour scale (`scale` is the largest absolute value of that panel), and the eight diagonal values are written into their squares with two decimals; then the tick labels, no grid, and a title such as $E_{(1)}{}^h{}_j$ (the doubled braces in the f-string produce single braces).

```python
fig.suptitle("The three Lovelock tensors at the sample point (row $h$, column $j$)")
save_figure(fig, "lovelock_heat_maps",
            "The three Lovelock tensors $E_{(1)}$ (the Einstein tensor), $E_{(2)}$ "
...)
```

A title over the three panels and `save_figure` (the caption is printed under figure 12a.3 in Section 12.15). Each panel is coloured only on its diagonal, with three different values: 3-space, the time, and the block.

**In [21], the field equations and their independent components.**

```python
alpha1, alpha3 = sp.symbols("alpha1 alpha3", real=True)  # alpha2 is defined above
Lam, kappa = sp.symbols("Lam kappa", real=True)  # Lambda and kappa
rho, p3, pt, p0 = sp.symbols("rho p3 pt p0", real=True)  # the source
ALPHA = {1: alpha1, 2: alpha2, 3: alpha3}
LHS = [[sp.expand(sum(ALPHA[k] * E[k][h][j] for k in (1, 2, 3))
                  + (Lam if h == j else 0)) for j in range(N)] for h in range(N)]
```

Symbols for the couplings $\alpha_1$, $\alpha_3$ (`alpha2` was made in In [18]), for $\Lambda$ (`Lam`) and $\kappa$, and for the source. `LHS` is the left-hand side $\sum_k\alpha_kE_{(k)}{}^h{}_j + \Lambda\delta^h_j$ in all 64 components.

```python
off_diagonal_zero = all(LHS[h][j] == 0 for h in range(N) for j in range(N)
                        if h != j)
groups_equal = (LHS[1][1] == LHS[2][2] == LHS[3][3]
                and LHS[0][0] == LHS[5][5] == LHS[6][6] == LHS[7][7])
reproduces(off_diagonal_zero and groups_equal,
           "every off-diagonal left-hand side is 0; three independent components",
           WL, "independent_components")
```

Every off-diagonal left-hand side must be zero and the two groups must be equal; then three independent components remain (Wolfram report, `independent_components`).

```python
e44, e11, e00 = (sp.expand(LHS[i][i] - Lam) for i in (4, 1, 0))
reproduces(LHS[0][0] == LHS[5][5],
           "hidden and extra-time components are one expression: p0 = p_t",
           PY, "independent_components")
say(f"Einstein part of the constraint: {e44.coeff(alpha1)}")
```

`e44`, `e11`, `e00` are the three independent components without $\Lambda$, as in Section 12.8. The hidden and extra-time components are one expression, so the source needs $p_0 = p_t$ (sympy report, `independent_components`). The last line prints the Einstein part of the constraint, the coefficient of $\alpha_1$ (Out [21]): `6*H**2*kk + 3*ad1**2 - 3*uu**2/2`.

**In [22], the constraint and the system of second order.**

```python
reproduces(not e44.has(ad2) and not e44.has(vv),
           "the x4 component contains a4', u and k but no a4'' and no v",
           PY, "constraint_first_order")
J = sp.Matrix([[sp.diff(e11, ad2), sp.diff(e11, vv)],
               [sp.diff(e00, ad2), sp.diff(e00, vv)]])
linear = all(sp.diff(e, x, y) == 0 for e in (e11, e00)
             for x in (ad2, vv) for y in (ad2, vv))
```

The constraint `e44` contains neither $a_4''$ nor $v$ (sympy report, `constraint_first_order`). `J` is the Jacobian, the 2 by 2 matrix (`sp.Matrix`) of the derivatives of `e11` and `e00` with respect to $a_4''$ and $v$. `linear` is true when every second derivative with respect to these two symbols vanishes: the equations are linear in them.

```python
det_J = sp.expand(J.det())
EINSTEIN = {alpha1: 1, alpha2: 0, alpha3: 0}
report("det J in Einstein gravity", det_J.subs(EINSTEIN))
reproduces(linear and det_J.subs(EINSTEIN) == -3,
           "x1 and x0 components linear in (a4'', v), Einstein det J = -3",
           WL, "second_order_system_a4pp_vv")
```

`J.det()` is the determinant, expanded. `EINSTEIN` is the substitution $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$; the cell prints `RESULT det J in Einstein gravity = -3` and checks it together with the linearity (Wolfram report, `second_order_system_a4pp_vv`).

```python
J_b = sp.Matrix([[J[0, 0], J[0, 1] / bb], [J[1, 0], J[1, 1] / bb]]).subs(EINSTEIN)
reproduces(J_b == sp.Matrix([[2, -2 / bb], [0, -sp.Rational(3, 2) / bb]]),
           "Einstein: Jacobian with respect to (a4'', b4'') is {{2, -2/b4}, "
           "{0, -3/(2 b4)}}", WL, "einstein_second_order_system")
general = equations_json["generalSource"]
NAMES_RECORD = {"ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk, "H": H,
                "alpha1": alpha1, "alpha2": alpha2, "alpha3": alpha3, "Lam": Lam,
                "kappa": kappa, "rho": rho, "p3": p3, "pt": pt, "p0": p0}
```

`J_b` is the Jacobian with respect to $(a_4'', b_4'')$: since $v = b_4''/b_4 - u^2$, the coefficient of $b_4''$ is that of $v$ divided by $b_4$. In Einstein gravity it must be $\begin{pmatrix}2 & -2/b_4\\ 0 & -3/(2b_4)\end{pmatrix}$ (Wolfram report, `einstein_second_order_system`). `general` is the record's key `generalSource`, and `NAMES_RECORD` lists the names its equations use.

```python
def parse_equation(text):
    left, right = text.split(" == ")
    return sp.expand(parse(left, NAMES_RECORD) - parse(right, NAMES_RECORD))
```

The record writes each equation as a text `left == right`; `parse_equation` splits it at ` == ` and returns left minus right as an expanded expression, which is zero exactly when the equation is satisfied identically.

```python
mine = {"constraint_x4": e44 + Lam + kappa * rho,
        "space_x1_eq_x2_eq_x3": e11 + Lam - kappa * p3,
        "hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7": e00 + Lam - kappa * p0}
same = all(sp.expand(parse_equation(general[key]["input"]) - value) == 0
           for key, value in mine.items())
J_text = general["secondOrderJacobian"]["input"].replace("{", "[").replace("}", "]")
```

`mine` holds the notebook's three equations in the same form (left minus right). They must equal the record's (the differences of the differences vanish). `J_text` turns the record's Jacobian, written with braces in the Wolfram Language, into the bracket form that sympy reads as a nested list.

```python
same = (same and sp.expand(sp.Matrix(parse(J_text, NAMES_RECORD)) - J)
        == sp.zeros(2, 2)
        and sp.expand(parse(general["secondOrderJacobianDet"]["input"], NAMES_RECORD)
                      - det_J) == 0)
reproduces(same, "the three equations, J and det J equal the record",
           PY, "json_general_source_equations")
```

The record's Jacobian and its determinant must equal the notebook's too (`sp.zeros(2, 2)` is the zero matrix), and the whole comparison reproduces the sympy report's `json_general_source_equations`. Out [22] shows four PASS lines and the RESULT line.

**In [23], the constraint propagates.**

```python
h4 = uu / 2 - ad1  # the rate of the block (x0, x5, x6, x7)
reproduces(sp.expand(d4_record(e44) - 3 * ad1 * (e11 - e44) - 4 * h4 * (e00 - e44))
           == 0, "d/dx4 e44 = 3 a4' (e11 - e44) + 4 h4 (e00 - e44)",
           PY, "bianchi_x4")
```

`h4` is the block rate $h = \tfrac12u - a_4'$. The check is the identity of Section 12.10, $\frac{d}{dx_4}e_{44} = 3a_4'(e_{11} - e_{44}) + 4h(e_{00} - e_{44})$, for every coupling (sympy report, `bianchi_x4`; Out [23]).

**In [24], figure 12a.4: $\det J$ along the record history.**

```python
on_history = {ad1: 1, uu: sp.Rational(4, 3), H: 1}  # the record history, H = 1
AUTHOR = {alpha1: 1, alpha2: sp.Rational(1, 32), alpha3: sp.Rational(1, 1152)}
cases = [("Einstein", EINSTEIN, "-"),
         ("Gauss-Bonnet $\\alpha_2H^2 = 0.01$",
          {alpha1: 1, alpha2: sp.Rational(1, 100), alpha3: 0}, "--"),
         ("Gauss-Bonnet $\\alpha_2H^2 = 1/32$",
          {alpha1: 1, alpha2: sp.Rational(1, 32), alpha3: 0}, "-."),
         ("author's weights", AUTHOR, ":")]
```

`on_history` inserts the record history with $H = 1$ ($a_4''$ and $v$ do not occur in $J$). `AUTHOR` holds the author's weights at $H = 1$, and `cases` lists the four couplings with their legend texts and line styles.

```python
fig, ax = plt.subplots()
negative = True
for label, couplings, style in cases:
    value = sp.expand(det_J.subs(couplings).subs(on_history))
    function = sp.lambdify(kk, value, "numpy")
    curve = function(k_axis) * np.ones_like(k_axis)
    negative = negative and bool(np.all(curve < 0))
    ax.plot(x_axis, curve, style, label=label)
```

For each case the determinant on the history is a polynomial in $k$, evaluated on the 301 values of `k_axis` of In [13] and drawn against the time. `negative` stays true only if every value of every curve is below zero (`np.all` of a comparison; `bool` turns numpy's truth value into Python's).

```python
check(negative, "det J < 0 along the record history for the four couplings")
gauss_bonnet = sp.expand(det_J.subs({alpha1: 1, alpha3: 0}).subs(on_history))
polynomial_a2 = sp.Poly(sp.expand(-9 * gauss_bonnet), alpha2)
c2, c1, c0 = polynomial_a2.all_coeffs()  # in alpha2: c2 a2^2 + c1 a2 + c0
discriminant = sp.Poly(sp.expand((c1 ** 2 - 4 * c2 * c0) / 144), kk)
leading, middle, constant = discriminant.all_coeffs()  # 256 - 2016 k - 1863 k^2
```

The check that all four curves stay negative. Then the Gauss-Bonnet case is taken symbolically: `polynomial_a2` is $-9\det J$ as a polynomial in $\alpha_2$, `all_coeffs` gives its three coefficients, and `discriminant` is $(c_1^2 - 4c_2c_0)/144$ as a polynomial in $k$, whose three coefficients are named `leading`, `middle` and `constant`.

```python
say(f"Gauss-Bonnet on the history: det J = -(1/9) ({polynomial_a2.as_expr()})")
say(f"its discriminant in alpha2 is 144 ({discriminant.as_expr()})")
check(discriminant.eval(1) < 0 and leading < 0 and middle < 0,
      "Gauss-Bonnet: det J has no real zero in alpha2 for k >= 1 (no breakdown)")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("time $x_4$ (units $1/H$)")
```

The two polynomials are printed (Out [24]): $\det J = -\tfrac19\big(\alpha_2^2(5184k^2 + 6048k + 704) + \alpha_2(-540k - 336) + 27\big)$ and the discriminant $144(-1863k^2 - 2016k + 256)$, the results derived by hand in Section 12.9. The check: the discriminant is negative at $k = 1$, and its two coefficients of $k$ and $k^2$ are negative, so it decreases for $k > 1$; hence it is negative for every $k \ge 1$, and $\det J$ has no real zero in $\alpha_2$ on the history. Then the axis line and labels.

```python
ax.set_ylabel("$\\det J$")
ax.set_title("The Jacobian of the second-order system along the record history")
ax.legend(fontsize=8)
save_figure(fig, "jacobian_determinant",
            "The determinant of the Jacobian $J$ with which $a_4^{\\prime\\prime}$ "
...)
```

The labels, the title, the legend and `save_figure` (the caption is printed under figure 12a.4 in Section 12.15). Einstein gravity gives the horizontal line $-3$; the other three curves bend down as $k$ grows, all below zero.

**In [25], the conservation law of a general source.**

```python
source = {name: sp.Function(name)(X4, Z)
          for name in ("rho", "p3", "pt", "p0", "q40", "q04")}  # f(x4, z)
T = [[sp.Integer(0)] * N for _ in range(N)]
for i, name in enumerate(["p0", "p3", "p3", "p3", "rho", "pt", "pt", "pt"]):
    T[i][i] = source[name]
T[4][4] = -source["rho"]  # T^x4_x4 = -rho
T[4][0], T[0][4] = source["q40"], source["q04"]
```

`sp.Function(name)(X4, Z)` makes an unknown function of the time and of the hidden angle for each of the six parts of the source. `T` is the mixed tensor of Section 12.8: the diagonal in the order $x_0, \dots, x_7$, then $T^{x_4}{}_{x_4} = -\rho$, and the two mixed components $q_{40} = T^{x_4}{}_{x_0}$ and $q_{04} = T^{x_0}{}_{x_4}$.

```python
def divergence(T):
    return [record_form(sp.cancel(
                sum(d(T[m][n], m) for m in range(N))
                + sum(Gamma[m][m][l] * T[l][n] for m in range(N) for l in range(N))
                - sum(Gamma[l][m][n] * T[m][l] for m in range(N) for l in range(N))))
            for n in range(N)]
```

`divergence(T)` computes $\nabla_\mu T^\mu{}_\nu$ for all eight $\nu$ from the general definition of Section 12.10: the derivatives $\sum_m\partial_mT^m{}_n$ (with the function `d` of In [5], which now also differentiates the explicit `X4` and `Z`), plus $\sum\Gamma^m{}_{ml}T^l{}_n$, minus $\sum\Gamma^l{}_{mn}T^m{}_l$, each brought to one fraction and written in the record's variables.

```python
divT = divergence(T)
MAP = {"d0q04": 6 * H * sp.diff(source["q04"], Z), "d4rho": sp.diff(source["rho"], X4),
       "d0p0": 6 * H * sp.diff(source["p0"], Z), "d4q40": sp.diff(source["q40"], X4),
       "cc": 1 / t, "tt": t, "ad1": ad1, "uu": uu, "kk": kk, "H": H}
MAP.update(source)
record_x4, record_x0 = (sp.sympify(general[key]["input"].split(" == ")[0]
                                   .replace("^", "**"), locals=MAP)
                        for key in ("conservation_x4", "conservation_x0"))
```

`MAP` tells sympy what the record's names mean: `d0q04` is $\partial_0q_{04} = 6H\,\partial_zq_{04}$, `d4rho` is $\partial_4\rho$, and so on; `cc` is $\cot z = 1/t$ and `tt` is $\tan z = t$; `MAP.update(source)` adds the six functions under their names. The record's two equations are read without their right-hand side `== 0`.

```python
reproduces(sp.simplify(divT[4] - record_x4) == 0
           and sp.simplify(divT[0] - record_x0) == 0,
           "nabla_mu T^mu_x4 and nabla_mu T^mu_x0 as in the record",
           PY, "json_conservation")
no_mixed = {source["q40"]: 0, source["q04"]: 0}
lead_x4 = (-sp.diff(source["rho"], X4) - 3 * ad1 * (source["rho"] + source["p3"])
           - 3 * h4 * (source["rho"] + source["pt"]) - h4 * (source["rho"]
                                                           + source["p0"]))
```

Both divergences must equal the record's (sympy report, `json_conservation`); `sp.simplify` is needed because the functions and their derivatives appear in fractions. `no_mixed` sets the two mixed components to zero, and `lead_x4` is the lead's formula for the time component.

```python
lead_x0 = 6 * H * sp.diff(source["p0"], Z) + 3 * H / t * (source["p0"] - source["pt"])
reproduces(sp.simplify(divT[4].subs(no_mixed).doit() - lead_x4) == 0,
           "diagonal source: nabla_mu T^mu_x4 as in the lead's record",
           EMT, "divergence_x4_component")
reproduces(sp.simplify(divT[0].subs(no_mixed).doit() - lead_x0) == 0,
           "diagonal source: nabla_mu T^mu_x0 = d0 p0 + 3 H cot z (p0 - p_t)",
           EMT, "divergence_x0_component")
```

`lead_x0` is the lead's formula $\partial_0p_0 + 3H\cot z\,(p_0 - p_t)$. Without mixed components the two divergences must equal the lead's formulas (`.doit()` carries out the derivatives of the substituted zeros); both checks reproduce the lead's divergence report.

```python
reproduces(all(divT[n] == 0 for n in (1, 2, 3, 5, 6, 7)),
           "nabla_mu T^mu_nu = 0 identically for the six other nu",
           EMT, "divergence_other_components_zero")
```

The six other components of the divergence vanish identically. Out [25] shows four PASS lines.

**In [26], Einstein gravity: a flat vacuum, no exponential vacuum, the null combinations.**

```python
c, x4 = sp.symbols("c x4", real=True)
FLAT = {ad1: 0, ad2: 0, uu: 2 / (x4 - c), vv: -2 / (x4 - c) ** 2,
        kk: 1 / (H ** 2 * (x4 - c) ** 2)}
flat_riemann = all(sp.simplify(value.subs(FLAT)) == 0 for value in R.values())
reproduces(flat_riemann, "flat member: every R^ab_mn vanishes",
           WL, "flat_member")
```

`FLAT` inserts the flat member $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ with the values of $u$, $v$ and $k$ derived in Section 12.11. Every curvature component must vanish (Wolfram report, `flat_member`).

```python
reproduces(all(sp.simplify(G[i][i].subs(FLAT)) == 0 for i in range(N)),
           "Einstein: the flat member is a vacuum with Lambda = 0",
           PY, "einstein_flat_vacuum")
difference_x1 = sp.factor(sp.expand((e44 - e11).subs(EINSTEIN).subs(EXPONENTIAL)))
k_vacuum = sp.solve(sp.expand((e44 - e00).subs(EINSTEIN).subs(EXPONENTIAL)), kk)
say(f"exponential vacuum: e44 - e11 = {difference_x1}, e44 = e00 needs k = {k_vacuum}")
```

The Einstein tensor vanishes too: a vacuum with $\Lambda = 0$ (sympy report, `einstein_flat_vacuum`). `difference_x1` is $e_{44} - e_{11}$ on the exponential histories in Einstein gravity, factorised, and `k_vacuum` the value of $k$ at which $e_{44} = e_{00}$ (`sp.solve` returns a list of solutions). The cell prints both (Out [26]): `A**2*H**2*(beta - 4)*(beta - 2)` and `[A**2*(beta - 4)/2]`.

```python
roots = sp.solve(difference_x1 / (A ** 2 * H ** 2), beta)  # beta = 2 or 4
k_values = [sp.factor(k_vacuum[0].subs(beta, root)) for root in roots]
reproduces(sorted(roots) == [2, 4] and k_values == [-A ** 2, 0]
           and sp.factor(k_vacuum[0].subs(A, 0)) == 0,
           "Einstein: no exponential history is a vacuum (k would be -A^2 or 0)",
           PY, "einstein_no_exponential_vacuum")
```

`roots` are the values of $\beta$ at which the first difference vanishes for $A \ne 0$: 2 and 4. At these the required $k$ is $-A^2$ and $0$, and at $A = 0$ it is 0; the check requires exactly this, so no exponential history (where $k > 0$) is a vacuum (sympy report, `einstein_no_exponential_vacuum`).

```python
null_x0 = sp.factor((e00 - e44).subs(EINSTEIN))  # kappa (rho + p0)
null_x1 = sp.expand((e11 - e44).subs(EINSTEIN))  # kappa (rho + p3)
report("Einstein: kappa (rho + p0)", null_x0)
report("Einstein: kappa (rho + p3)", null_x1)
reproduces(sp.expand(null_x0 + sp.Rational(3, 2) * (2 * H ** 2 * kk + 4 * ad1 ** 2
                                                     - ad1 * uu + vv)) == 0
           and sp.expand(null_x1 - (2 * ad2 - 8 * ad1 ** 2 + 6 * ad1 * uu - uu ** 2
                                    - 2 * vv)) == 0,
           "Einstein: the two null combinations as in the record",
           PY, "einstein_null_combinations")
```

The two null combinations of Section 12.11, $\kappa(\rho + p_0) = e_{00} - e_{44}$ and $\kappa(\rho + p_3) = e_{11} - e_{44}$ in Einstein gravity, printed as RESULT lines and compared with the record's formulas (sympy report, `einstein_null_combinations`).

```python
null_history = sp.expand(null_x0.subs(HISTORY).subs(H, 1))
report("record history: kappa (rho + p0)", null_history)
check(null_history == -3 * kk - 4, "record history: kappa (rho + p0) = -3 k - 4 < 0")
einstein_record = equations_json["einstein"]
mine_einstein = {"constraint_x4": (e44 + Lam).subs(EINSTEIN) + kappa * rho,
                 "space_x1": (e11 + Lam).subs(EINSTEIN) - kappa * p3,
                 "hidden_x0": (e00 + Lam).subs(EINSTEIN) - kappa * p0}
```

On the record history the first combination is `-3*kk - 4` (printed and checked): negative at every time. `einstein_record` is the record's key `einstein`; `mine_einstein` holds the notebook's three Einstein equations as left minus right.

```python
same = all(sp.expand(parse_equation(einstein_record[key]["input"]) - value) == 0
           for key, value in mine_einstein.items())
reproduces(same, "the Einstein equations equal the record", PY, "json_einstein")
```

They must equal the record's (sympy report, `json_einstein`). Out [26] shows seven PASS lines, two printed lines and three RESULT lines.

**In [27], figure 12a.5: why no exponential history is an Einstein vacuum.**

```python
beta_axis = np.linspace(0.0, 6.0, 301)
fig, ax = plt.subplots()
ax.axhspan(-3.0, 0.0, color="grey", alpha=0.25, label="$k \\leq 0$: no history")
ax.plot(beta_axis, (beta_axis - 4.0) / 2.0, color="tab:blue",
        label="hidden equation: $k/A^2 = (\\beta - 4)/2$")
for position in (2.0, 4.0):
    ax.axvline(position, color="tab:red", linestyle="--")
```

`beta_axis` holds 301 values of $\beta$ from 0 to 6. `axhspan` shades the region $k \le 0$ (between $-3$ and 0 on the vertical axis), where no history lies; the blue line is the hidden equation's condition $k/A^2 = (\beta - 4)/2$; the red dashed vertical lines are the 3-space equation's conditions $\beta = 2$ and $\beta = 4$.

```python
ax.plot([], [], color="tab:red", linestyle="--",
        label="3-space equation: $\\beta = 2$ or $\\beta = 4$")
ax.plot([2.0, 4.0], [-1.0, 0.0], "o", color="black", label="where both hold")
ax.axvline(4.0 / 3.0, color="black", linestyle=":", label="record history "
           "$\\beta = 4/3$")
ax.set_xlim(0.0, 6.0)
```

`ax.plot([], [], ...)` draws nothing but adds one legend entry for the two red lines. The black points mark where both conditions hold, $(2, -1)$ and $(4, 0)$; the dotted line marks the record history $\beta = 4/3$; `set_xlim` fixes the horizontal range.

```python
ax.set_ylim(-3.0, 3.0)
ax.set_xlabel("$\\beta = (b_4'/b_4)/a_4'$")
ax.set_ylabel("$k/A^2$")
ax.set_title("Einstein gravity: the vacuum conditions on exponential histories")
ax.legend(fontsize=7.5, loc="upper left")
save_figure(fig, "exponential_vacuum",
            "Why no exponential history $a_4 = AHx_4 + a_0$, $b_4 = b_4(0)"
...)
```

The vertical range, the labels, the title, the legend in the upper left corner and `save_figure` (the caption is printed under figure 12a.5 in Section 12.15).

**In [28], the exponential histories.**

```python
required_mine = {"rho": sp.expand(-(e44 + Lam).subs(EXPONENTIAL) / kappa),
                 "p3": sp.expand((e11 + Lam).subs(EXPONENTIAL) / kappa),
                 "p0": sp.expand((e00 + Lam).subs(EXPONENTIAL) / kappa)}
degrees = [sp.Poly(kappa * value, kk).degree() for value in required_mine.values()]
say(f"degrees in k of kappa rho, kappa p3, kappa p0: {degrees}")
reproduces(max(degrees) <= 2 and required_mine["p0"].has(kk),
           "exponential history: rho, p3, p0 = p_t polynomials of degree <= 2 in k",
           PY, "exponential_history_required_source")
```

`required_mine` holds the required source of every exponential history, for general couplings: $\kappa\rho = -(e_{44} + \Lambda)$, $\kappa p_3 = e_{11} + \Lambda$ and $\kappa p_0 = e_{00} + \Lambda$, each divided by $\kappa$. `sp.Poly(..., kk).degree()` is the highest power of $k$: the cell prints `[2, 2, 1]` and checks that no degree exceeds 2 and that $p_0$ does depend on $k$ (sympy report, `exponential_history_required_source`).

```python
names_all = dict(names_exp, alpha1=alpha1, alpha2=alpha2, alpha3=alpha3, Lam=Lam,
                 kappa=kappa)
same = all(sp.expand(sp.sympify(required[key]["input"].replace("^", "**"),
                                locals=names_all) - required_mine[name]) == 0
           for key, name in (("rho", "rho"), ("p3", "p3"), ("p0", "p0"),
                             ("pt", "p0")))
```

`names_all` adds the couplings, $\Lambda$ and $\kappa$ to the names of In [18]; `same` compares the record's four required components with the notebook's (the record's `pt` with the notebook's $p_0$).

```python
reproduces(same, "the required source equals the record (exponentialHistory)",
           PY, "json_exponential_history")
check(all(sp.expand(value.subs(A, -A) - value) == 0
          for value in required_mine.values()),
      "as functions of k the required source contains A only through A^2")
```

The comparison reproduces the sympy report's `json_exponential_history`. The last check replaces $A$ by $-A$ and requires every component to stay the same: as functions of $k$ the required source contains $A$ only through $A^2$ (Section 12.12). Out [28] shows the degrees and three PASS lines.

**In [29], the source of the record history.**

```python
HISTORY_EXP = {A: 1, beta: sp.Rational(4, 3), H: 1}  # A = 1, beta = 4/3, H = 1
AUTHOR_H = {alpha1: 1, alpha2: sp.Rational(1, 32) / H ** 2,
            alpha3: sp.Rational(1, 1152) / H ** 4}  # alpha_k = w_k/H^(2k)
needed = {name: sp.expand(value.subs(AUTHOR_H).subs(EXPONENTIAL).subs(HISTORY_EXP))
          for name, value in (("minus_rho", e44), ("p3", e11), ("p0", e00))}
for name, value in needed.items():
    say(f"author's weights, record history: kappa T - Lambda ({name}) = {value}")
```

`HISTORY_EXP` is the record history $A = 1$, $\beta = \tfrac43$, $H = 1$; `AUTHOR_H` the author's weights $\alpha_k = w_k/H^{2k}$. `needed` holds $-\kappa\rho - \Lambda = e_{44}$, $\kappa p_3 - \Lambda = e_{11}$ and $\kappa p_0 - \Lambda = e_{00}$ on the history; they are printed (Out [29]): `-9*kk**2/16 + 161*kk/24 + 121/432`, `-9*kk**2/16 + 1601*kk/216 - 5359/3888` and `79*kk/16 - 497/144`, the source of Section 12.12.

```python
stored = equations_json["exponentialHistory"]["authorWeights"]
stored = stored["historySource_kappaT_minus_Lam"]
same = all(sp.expand(parse(stored[key]["input"]) - needed[name]) == 0
           for key, name in (("minus_rho", "minus_rho"), ("p3", "p3"),
                             ("p0", "p0"), ("pt", "p0")))
reproduces(same, "the author's weights: the source of the record history",
           PY, "author_weights_history_source")
```

The record stores the same source under `exponentialHistory/authorWeights/historySource_kappaT_minus_Lam`; the comparison reproduces the sympy report's `author_weights_history_source`.

```python
x4s = sp.symbols("x4", real=True)
metric_history = read_json(METRIC_RESULTS)["history_source"]
exp_names = {"H": sp.Integer(1), "x4": x4s, "exp": sp.exp}
as_k = sp.Rational(3, 2) * sp.log(kp)  # x4 = (3/2) ln k, so e^(2 x4/3) = k
einstein_needed = {name: sp.expand(value.subs(EINSTEIN).subs(EXPONENTIAL)
                                   .subs(HISTORY_EXP))
                   for name, value in (("-rho", e44), ("p3", e11), ("p0", e00),
                                       ("p_t", e00))}
```

The results file of the corrected metric writes this source as functions of the time with `exp(2*H*x4/3)`. `as_k` is the time at which $e^{2x_4/3} = k$, namely $x_4 = \tfrac32\ln k$; inserting it turns the file's formulas into polynomials in $k$. `einstein_needed` holds the Einstein source of the same history, which the file also stores.

```python
same = True
for block, values in (("author_weights_A1_beta43",
                       {"-rho": needed["minus_rho"], "p3": needed["p3"],
                        "p0": needed["p0"], "p_t": needed["p0"]}),
                      ("einstein_A1_beta43", einstein_needed)):
    for key, value in values.items():
        text = sp.sympify(metric_history[block][key], locals=exp_names)
        in_k = sp.expand(sp.expand(text.subs(x4s, as_k)).subs(kp, kk))
        same = same and sp.expand(in_k - value) == 0
```

For both blocks of the file (the author's weights and Einstein gravity, both at $A = 1$, $\beta = \tfrac43$) every stored component is read, rewritten in $k$, and compared with the notebook's.

```python
conserved = sp.expand((d4_record(-e44) + 3 * ad1 * (-e44 + e11)
                       + 4 * h4 * (-e44 + e00)).subs(AUTHOR_H).subs(HISTORY)
                      .subs(H, 1))
reproduces(same and conserved == 0,
           "the history source of the corrected-metric record, conserved",
           WARPED, "history_source_conserved")
```

`conserved` is the energy exchange $\kappa\big[\partial_4\rho + 3a_4'(\rho + p_3) + 4h(\rho + p_0)\big]$ of this source, written with the components ($\kappa\rho = -e_{44} - \Lambda$ and so on; $\Lambda$ cancels in every bracket). It must vanish: by the Bianchi identity of In [23] the source that any history requires is automatically conserved. The check reproduces the metric report's `history_source_conserved`. Out [29] shows three printed lines and two PASS lines.

**In [30], the last check.**

```python
figure_names = ["12a_1_pair_curvatures.png", "12a_2_einstein_components.png",
                "12a_3_lovelock_heat_maps.png", "12a_4_jacobian_determinant.png",
                "12a_5_exponential_vacuum.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all five figure files exist")
all_checks_passed()
```

`figure_names` lists the five figure files; `output_file(...).is_file()` is true when a file exists where the notebook wrote it. The check requires all five, and `all_checks_passed()` prints the last line (Out [30]): ALL 72 CHECKS PASSED (notebook 12a).

### 12.17 Example: the source that the exponential histories require

The second notebook takes the Lovelock components from the record (Section 12.7) and explores the required source of Section 12.12 for every slope $A$, every ratio $\beta$, every cosmological constant and every coupling. It checks that the source is a polynomial of degree at most 2 in $k$ and contains $A$ only through $A^2$; follows the source of the record history in Einstein gravity ($\kappa\rho = -6k - \tfrac13$, negative at every time, with $\Lambda = 0$) and with the author's weights (where, with $\Lambda = -10$, the energy density starts at $\kappa\rho = 3.57407$ and changes sign at $x_4 = 0.785131$); shows that in Einstein gravity no exponential history satisfies both null energy conditions; finds the Einstein-Gauss-Bonnet vacua (only for constant $k$) and shows that the author's weights allow none; and states what a source with equal pressures, such as a homogeneous condensate of dirac16complex00, would need. It prints 23 PASS lines, draws eight figures and runs in about fifteen seconds.

<!-- NOTEBOOK 12b -->

### 12.20 Line-by-line walk-through of Notebook 12b

The notebook has 19 code cells, In [1] to In [19]. As in Section 12.16, every line or small group of lines is quoted and explained; docstrings are left out, and long captions are shortened to their first line and `...)` (they are printed in full under the figures in Section 12.19).

**In [1], the set-up cell.** It is the set-up cell of Notebook 12a, explained line by line in Section 12.16 under In [1], with two differences: its comment lines are the run instructions of Notebook 12b (Section 12.18), and its line `NOTEBOOK_ID = "12b"  # this notebook: chapter 12, example b` names this notebook, so the figures are saved as `12b_<k>_<name>.png` and their captions in `12b.captions.json`. It prints Set-up of notebook 12b complete: repository folder found, helpers defined.

**In [2], the Revision records.** The cell defines the helpers of Notebook 12a and one more, and reads the equations.

```python
import contextlib  # redirect_stdout: send printed lines into a buffer
import io  # StringIO: a text buffer in memory
```

The two modules for the text buffer of `reproduces`, as in Notebook 12a (Section 12.16, In [2]).

```python
PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
LEAD = "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json"  # lead check
EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the equations
METRIC_RESULTS = "Revision/metric_warped/results/warped-metric.json"
METRIC_WL = "Revision/metric_warped/reports/wolfram-warped-metric-report.json"
KS = "Revision/field_equations_a4/reports/ks-source-conditions.json"
KS_A4 = "Revision/field_equations_a4/ks_source/reports/ks-source-a4.json"
EOS = "Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json"
```

Short names for the files the notebook reads: the sympy and Wolfram reports, the lead's Einstein report, the equations `a4-equations.json`, the results file of the corrected metric and its Wolfram report (`METRIC_WL`), the report of the source conditions on the Kohn-Sham states (`KS`, Section 12.21 explains it), the report of the Kohn-Sham states as a source of the field equations (`KS_A4`), and the report of the dark-sector record on the commuting field (`EOS`), which contains the record's statement about condensates as sources of the record history.

```python
def read_json(relative):
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))
```

`read_json` reads a record, as in Notebook 12a.

```python
def record_verdict(report_file, name):
    for entry in read_json(report_file)["checks"]:
        if entry["name"] == name:
            return entry["verdict"]
    return None
```

`record_verdict` returns the verdict of a named check, as in Notebook 12a.

```python
def record_detail(report_file, name):
    for entry in read_json(report_file)["checks"]:
        if entry["name"] == name:
            return entry["detail"]
    return ""
```

`record_detail` returns the detail text of a named check (the sentence in which the record states its result), or an empty text. The notebook compares some of its numbers with numbers written in these texts.

```python
def reproduces(condition, name, report_file, record_name):
    found = record_verdict(report_file, record_name) == "PASS"
    lines = io.StringIO()  # a text buffer
    with contextlib.redirect_stdout(lines):  # print() now writes into the buffer
        check(condition and found, name, record=f"{report_file}, check {record_name}")
    print(lines.getvalue(), end="")  # all lines at once
```

`reproduces`, as in Notebook 12a: a check that also requires the named record check to have passed, printing its two lines together.

```python
record = read_json(EQUATIONS)
title = record["title"]  # the title stored in the record
say(f"read {EQUATIONS}: {title}")
```

The equations are read into `record`, and the title stored in the record is printed (Out [2]): the Einstein-Lovelock field equations for $a_4$ and $b_4$ in the corrected primordial metric of 2026-10-16 (version 2), for general functions and every real $z$. The title shows that the notebook works with the current record.

**In [3], the required source of the exponential histories.**

```python
import numpy as np  # arrays of numbers for the plots
import sympy as sp  # exact algebra with symbols
```

`numpy` for the plots and `sympy` for the exact algebra.

```python
H = sp.symbols("H", positive=True)  # the constant H of the metric
A, beta = sp.symbols("A beta", real=True)  # the exponential history
ad1, ad2, uu, vv, kk = sp.symbols("ad1 ad2 uu vv kk", real=True)
alpha1, alpha2, alpha3 = sp.symbols("alpha1 alpha2 alpha3", real=True)
Lam, kappa = sp.symbols("Lam kappa", real=True)  # Lambda and kappa
NAMES = {"ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk, "H": H, "AA": A,
         "be": beta, "alpha1": alpha1, "alpha2": alpha2, "alpha3": alpha3,
         "Lam": Lam, "kappa": kappa}
```

The symbols: $H > 0$; the slope `A` and the ratio `beta` of the exponential history; the record's variables `ad1`, `ad2`, `uu`, `vv`, `kk`; the couplings; `Lam` and `kappa`. `NAMES` says which symbol each name of the record means (the record writes `AA` for $A$ and `be` for $\beta$).

```python
def parse(text):
    return sp.sympify(text.replace("^", "**"), locals=NAMES)
```

`parse` turns a Wolfram text of the record into a sympy expression (`^` becomes `**`).

```python
ALPHA = {1: alpha1, 2: alpha2, 3: alpha3}
lovelock = record["lovelockTensors"]
side = {key: sum(ALPHA[k] * parse(lovelock[f"E{k}"][key]["input"]) for k in (1, 2, 3))
        for key in ("x0x0", "x1x1", "x4x4", "x5x5")}  # sum_k alpha_k E_(k)
EXPONENTIAL = {ad1: A * H, ad2: 0, uu: beta * A * H, vv: 0}
kappa_rho = sp.expand(-(side["x4x4"] + Lam).subs(EXPONENTIAL))
```

`side` holds the four stored components of $\sum_k\alpha_kE_{(k)}$: for each key the sum over the three orders of the coupling times the parsed component. `EXPONENTIAL` inserts $a_4' = AH$, $a_4'' = 0$, $u = \beta AH$, $v = 0$, and `kappa_rho` is $\kappa\rho = -\big(\sum_k\alpha_kE^{x_4}{}_{x_4} + \Lambda\big)$ on the history, expanded.

```python
kappa_p3 = sp.expand((side["x1x1"] + Lam).subs(EXPONENTIAL))
kappa_p0 = sp.expand((side["x0x0"] + Lam).subs(EXPONENTIAL))
kappa_pt = sp.expand((side["x5x5"] + Lam).subs(EXPONENTIAL))
say(f"Einstein part of kappa rho: {sp.factor(kappa_rho.coeff(alpha1))}")
say(f"Einstein part of kappa p3: {sp.factor(kappa_p3.coeff(alpha1))}")
say(f"Einstein part of kappa p0: {sp.factor(kappa_p0.coeff(alpha1))}")
```

In the same way $\kappa p_3$, $\kappa p_0$ and $\kappa p_t$ (from the components $x_1$, $x_0$ and $x_5$). `.coeff(alpha1)` takes the part multiplied by $\alpha_1$, the Einstein part, which is printed factorised (Out [3]): `3*H**2*(A**2*beta**2 - 2*A**2 - 4*kk)/2` for $\kappa\rho$, and the corresponding forms for $\kappa p_3$ and $\kappa p_0$: the Einstein source of Section 12.12 without $\Lambda$.

**In [4], five properties of the required source.**

```python
reproduces(sp.expand(kappa_pt - kappa_p0) == 0,
           "the hidden and the extra-time pressures are equal: p0 = p_t",
           WL, "independent_components")
degrees = [sp.Poly(value, kk).degree() for value in (kappa_rho, kappa_p3, kappa_p0)]
x4 = sp.symbols("x4", real=True)
k_rate = sp.diff(sp.exp((2 - beta) * A * H * x4), x4) / sp.exp((2 - beta) * A * H * x4)
```

(1) The hidden and the extra-time pressures are one expression (Wolfram report, `independent_components`). `degrees` holds the highest power of $k$ in each component. For the rate of $k$ the cell differentiates $e^{(2 - \beta)AHx_4}$ with respect to a symbol `x4` and divides by the function itself.

```python
say(f"degrees in k: {degrees}; dk/dx4 = ({sp.factor(sp.simplify(k_rate))}) k")
reproduces(max(degrees) <= 2 and sp.factor(sp.simplify(k_rate)) == -A * H * (beta - 2),
           "the source is a polynomial of degree <= 2 in k; constant iff beta = 2 or "
           "A = 0", PY, "exponential_history_required_source")
required = record["exponentialHistory"]["requiredSource"]
same = all(sp.expand(kappa * parse(required[key]["input"]) - value) == 0
           for key, value in (("rho", kappa_rho), ("p3", kappa_p3), ("p0", kappa_p0),
                              ("pt", kappa_pt)))
```

The cell prints (Out [4]) `degrees in k: [2, 2, 1]; dk/dx4 = (-A*H*(beta - 2)) k`. (2) No degree exceeds 2, and the rate of $k$ is $-(\beta - 2)AH$, zero only for $\beta = 2$ or $A = 0$ (sympy report, `exponential_history_required_source`). Then the record's required source is read; it is stored divided by $\kappa$, so it is multiplied by `kappa` before the comparison.

```python
reproduces(same, "kappa rho, kappa p3, kappa p0, kappa p_t equal the record",
           PY, "json_exponential_history")
check(all(sp.expand(value.subs(A, -A) - value) == 0
          for value in (kappa_rho, kappa_p3, kappa_p0)),
      "as functions of k the source contains A only through A^2")
stored = read_json(METRIC_RESULTS)["history_source"]["einstein_kappaT_minus_Lambda"]
```

(3) The four components equal the record (sympy report, `json_exponential_history`). (4) Replacing $A$ by $-A$ changes no component. Then the Einstein source of the exponential histories is read from the results file of the corrected metric, where it is written as a function of the time.

```python
names_e = {"A": A, "beta": beta, "H": H, "x4": x4, "exp": sp.exp}
k_of_x4 = sp.exp((2 - beta) * A * H * x4)  # k at b4(0) = 1, a0 = 0
mine = {"-rho": -kappa_rho.coeff(alpha1), "p3": kappa_p3.coeff(alpha1),
        "p0": kappa_p0.coeff(alpha1), "p_t": kappa_pt.coeff(alpha1)}
same = all(sp.simplify(sp.sympify(stored[key], locals=names_e)
                       - (value.subs(Lam, 0)).subs(kk, k_of_x4)) == 0
           for key, value in mine.items())
```

`names_e` says which symbol each name of that file means; `k_of_x4` is $k$ at $b_4(0) = 1$, $a_0 = 0$. `mine` holds the Einstein parts (coefficients of $\alpha_1$), with the sign of $-\rho$ as the file stores it. Each stored text minus the notebook's part with $\Lambda = 0$ and $k = e^{(2 - \beta)AHx_4}$ must simplify to zero.

```python
reproduces(same, "the alpha1 parts equal the Einstein source of the metric record",
           LEAD, "einstein_exponential_source_alpha1")
```

(5) The comparison reproduces the lead's Einstein report, `einstein_exponential_source_alpha1`. Out [4] shows five PASS lines.

**In [5], Einstein gravity and the record history.**

```python
EINSTEIN = {alpha1: 1, alpha2: 0, alpha3: 0}
rho_e, p3_e, p0_e = (sp.expand(value.subs(EINSTEIN))
                     for value in (kappa_rho, kappa_p3, kappa_p0))
report("Einstein: kappa rho", sp.factor(rho_e))
einstein_record = record["exponentialHistory"]["einstein"]
same = all(sp.expand(kappa * parse(einstein_record[key]["input"]) - value) == 0
           for key, value in (("rho", rho_e), ("p3", p3_e), ("p0", p0_e)))
```

`EINSTEIN` sets $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$; `rho_e`, `p3_e`, `p0_e` are the Einstein sources, and $\kappa\rho$ is printed (Out [5]): `(3*A**2*H**2*beta**2 - 6*A**2*H**2 - 12*H**2*kk - 2*Lam)/2`, that is $\tfrac32A^2H^2(\beta^2 - 2) - 6H^2k - \Lambda$. `same` compares the three with the record's key `exponentialHistory/einstein`.

```python
reproduces(same, "Einstein: the required source equals the record",
           WL, "exponential_history_required_source")
HISTORY = {A: 1, beta: sp.Rational(4, 3), H: 1, Lam: 0}  # record history, Lambda = 0
history = {name: sp.expand(value.subs(HISTORY))
           for name, value in (("rho", rho_e), ("p3", p3_e), ("p0", p0_e))}
for name, value in history.items():
    report(f"record history, Einstein, Lambda = 0: kappa {name}", value)
```

The three agree, as the Wolfram report found (its check `exponential_history_required_source`). Then `HISTORY` inserts the record history with $\Lambda = 0$ and $H = 1$, and the three components are printed as RESULT lines: `-6*kk - 1/3`, `6*kk - 13/9` and `3*kk - 11/3`, the values derived in Section 12.12.

```python
at_start = {name: value.subs(kk, 1) for name, value in history.items()}
report("at x4 = 0: kappa rho, kappa p3, kappa p0",
       f"{at_start['rho']}, {at_start['p3']}, {at_start['p0']}")
check(at_start == {"rho": sp.Rational(-19, 3), "p3": sp.Rational(41, 9),
                   "p0": sp.Rational(-2, 3)},
      "record history at x4 = 0: kappa rho = -19/3, kappa p3 = 41/9, kappa p0 = -2/3")
```

At $x_4 = 0$ we have $k = 1$; the three values are printed, `-19/3, 41/9, -2/3`, and checked: $-6 - \tfrac13 = -\tfrac{19}3$, $6 - \tfrac{13}9 = \tfrac{41}9$, $3 - \tfrac{11}3 = -\tfrac23$.

```python
stored = read_json(METRIC_RESULTS)["history_source"]["einstein_A1_beta43_mathematica"]
k_of_t = sp.exp(sp.Rational(2, 3) * x4)
names_m = {"H": sp.Integer(1), "x4": x4}
```

The results file of the corrected metric also stores this source as written by its Wolfram verifier, with `Exp[(2/3)*H*x4]` for $k$. `k_of_t` is $e^{2x_4/3}$; `names_m` sets $H = 1$.

```python
def from_wolfram(text):
    text = text.replace("Exp[", "exp(").replace("]", ")").replace("^", "**")
    return sp.sympify(text, locals=names_m)
```

`from_wolfram` turns such a text into sympy: `Exp[` becomes `exp(`, every `]` becomes `)`, and `^` becomes `**`.

```python
same = all(sp.simplify(from_wolfram(stored[key]) - value.subs(kk, k_of_t)) == 0
           for key, value in (("-rho", -history["rho"]), ("p3", history["p3"]),
                              ("p0", history["p0"]), ("p_t", history["p0"])))
reproduces(same, "the source of the record history equals the Wolfram record",
           METRIC_WL, "history_source_equals_sympy")
```

The four stored components (with $p_t$ equal to $p_0$) must equal the notebook's, with $k = e^{2x_4/3}$ (Wolfram report of the corrected metric, `history_source_equals_sympy`). Out [5] shows four RESULT lines and three PASS lines.

**In [6], figure 12b.1: the Einstein source of the record history.**

```python
x_axis = np.linspace(0.0, 3.0, 301)  # the time x4 in units 1/H
k_axis = np.exp(2.0 * x_axis / 3.0)  # k on the record history
curves = {name: sp.lambdify(kk, value, "numpy")(k_axis) * np.ones_like(k_axis)
          for name, value in history.items()}
check(bool(np.all(curves["rho"] < 0)),
      "Einstein, Lambda = 0: the energy density of the record history is negative")
```

301 times from 0 to 3, the values of $k$ there, and the three components evaluated on them (`sp.lambdify` as in Notebook 12a; the dictionary comprehension builds one array per component). The check: with $\Lambda = 0$ the energy density is negative at every plotted time (it is $-6k - \tfrac13 < 0$ for every $k > 0$).

```python
fig, ax = plt.subplots()
ax.plot(x_axis, curves["rho"], label="$\\kappa\\rho = -6k - 1/3$")
ax.plot(x_axis, curves["p3"], "--", label="$\\kappa p_3 = 6k - 13/9$")
ax.plot(x_axis, curves["p0"], ":", label="$\\kappa p_0 = \\kappa p_t = 3k - 11/3$")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("time $x_4$ (units $1/H$)")
```

Three curves with different line styles and legend texts, a black line at zero, and the label of the time axis.

```python
ax.set_ylabel("required source (units of $H^2/\\kappa$)")
ax.set_title("Einstein gravity, $\\Lambda = 0$: the source of the record history")
ax.legend(fontsize=8)
save_figure(fig, "einstein_source",
            "The source that the record history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ "
...)
```

The vertical label, the title, the legend and `save_figure` (the caption is printed under figure 12b.1 in Section 12.19). All three components grow with $k$; $p_3$ and $p_0$ differ, so the source is anisotropic.

**In [7], figure 12b.2: the sign of $A$ is a choice.**

```python
rho_43 = sp.expand(rho_e.subs({beta: sp.Rational(4, 3), H: 1, Lam: 0}))
k_time = {slope: sp.exp(sp.Rational(2, 3) * slope * x4) for slope in (1, -1)}
rho_time = {slope: rho_43.subs(A, slope).subs(kk, k_time[slope]) for slope in (1, -1)}
check(sp.expand(rho_43.subs(A, 1) - rho_43.subs(A, -1)) == 0
      and sp.simplify(rho_time[-1] - rho_time[1].subs(x4, -x4)) == 0,
      "A and -A: the same source at the same k, mirror images in time")
```

`rho_43` is the Einstein energy density at $\beta = \tfrac43$, $H = 1$, $\Lambda = 0$, as a function of $A$ and $k$. `k_time` gives $k = e^{(2/3)Ax_4}$ for the slopes $A = 1$ and $A = -1$, and `rho_time` the energy density of each as a function of the time. The check: at equal $k$ the two energy densities are equal, and the energy density of $-A$ at the time $x_4$ is that of $A$ at $-x_4$ (Section 12.12).

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
k_values = np.linspace(0.2, 5.0, 200)
times = np.linspace(-3.0, 3.0, 301)
for slope, style in ((1, "-"), (-1, "--")):
    rho_k = sp.lambdify(kk, rho_43.subs(A, slope), "numpy")
    left.plot(k_values, rho_k(k_values), style, label=f"$A = {slope}$")
    rho_t = sp.lambdify(x4, rho_time[slope], "numpy")
    right.plot(times, rho_t(times), style, label=f"$A = {slope}$")
```

Two panels; 200 values of $k$ from 0.2 to 5, and 301 times from $-3$ to 3. For each slope the left panel draws the energy density against $k$, the right panel against the time.

```python
left.set_xlabel("$k = e^{2a_4}/b_4$")
left.set_ylabel("$\\kappa\\rho$ (units $H^2$)")
left.set_title("against $k$: the same curve")
left.legend(fontsize=8)
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("$\\kappa\\rho$ (units $H^2$)")
```

The labels of the two axes of the left panel, its title and legend, and the labels of the right panel.

```python
right.set_title("against the time: mirror images")
right.legend(fontsize=8)
save_figure(fig, "sign_symmetry",
            "Einstein gravity, $\\beta = 4/3$, $\\Lambda = 0$: the energy density "
...)
```

The title and legend of the right panel and `save_figure` (caption under figure 12b.2). On the left the two curves lie on top of each other; on the right they are mirror images under $x_4 \to -x_4$.

**In [8], figure 12b.3: the role of $\beta$.**

```python
scan = {name: sp.expand(value.subs({A: 1, H: 1, Lam: 0, kk: 1}))
        for name, value in (("rho", rho_e), ("p3", p3_e), ("p0", p0_e))}
positive = sp.solve_univariate_inequality(scan["rho"] > 0, beta, relational=False)
say(f"k = 1, A = 1, Lambda = 0: kappa rho = {scan['rho']} > 0 for beta in {positive}")
check(positive == sp.Union(sp.Interval.open(-sp.oo, -sp.sqrt(6)),
                           sp.Interval.open(sp.sqrt(6), sp.oo)),
      "k = 1: the Einstein energy density is positive exactly for |beta| > sqrt(6)")
```

`scan` evaluates the three Einstein components at $A = 1$, $H = 1$, $\Lambda = 0$ and $k = 1$ (on the record history: at $x_4 = 0$), leaving $\beta$ free. `sp.solve_univariate_inequality(..., relational=False)` finds the set of $\beta$ on which the energy density is positive and returns it as a set of intervals. The cell prints (Out [8]) `kappa rho = 3*beta**2/2 - 9 > 0 for beta in Union(Interval.open(-oo, -sqrt(6)), Interval.open(sqrt(6), oo))`: $\tfrac32\beta^2 - 9 > 0$ exactly when $\beta^2 > 6$. The check compares the set with $(-\infty, -\sqrt6) \cup (\sqrt6, \infty)$.

```python
beta_axis = np.linspace(0.0, 4.0, 401)
fig, ax = plt.subplots()
for (name, value), style, label in zip(scan.items(), ("-", "--", ":"),
                                       ("$\\kappa\\rho$", "$\\kappa p_3$",
                                        "$\\kappa p_0 = \\kappa p_t$")):
    ax.plot(beta_axis, sp.lambdify(beta, value, "numpy")(beta_axis), style,
            label=label)
```

401 values of $\beta$ from 0 to 4, one figure, and a loop over the three components with their line styles and legend texts (`zip` walks through the three lists together).

```python
ax.axvline(4.0 / 3.0, color="black", linestyle=":", linewidth=0.8)
ax.axvline(2.0, color="grey", linestyle="--", linewidth=0.8)
ax.text(4.0 / 3.0 + 0.03, 4.5, "record $\\beta = 4/3$", fontsize=8)
ax.text(2.03, -9.5, "$\\beta = 2$: block constant", fontsize=8)
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("$\\beta = u/a_4'$")
```

Two vertical lines, dotted at the record value $\beta = \tfrac43$ and dashed at $\beta = 2$, each with a short text; a line at zero; the horizontal label.

```python
ax.set_ylabel("required source at $k = 1$ (units $H^2$)")
ax.set_title("Einstein gravity, $A = 1$, $\\Lambda = 0$: the source against $\\beta$")
ax.legend(fontsize=8, loc="lower left")
save_figure(fig, "beta_scan",
            "Einstein gravity with $A = 1$ and $\\Lambda = 0$: the source that an "
...)
```

The vertical label, the title, the legend in the lower left corner and `save_figure` (caption under figure 12b.3). The energy density is negative for all $\beta$ shown up to 2.45; at $\beta = 2$ the block does not shrink and the source is constant in time.

**In [9], the author's weights on the record history.**

```python
import re  # regular expressions: find numbers in a text
```

`re`, the module of **regular expressions**, patterns that find pieces of a text; it is used to read numbers out of a detail text of the record.

```python
AUTHOR = {alpha1: 1, alpha2: sp.Rational(1, 32) / H ** 2,
          alpha3: sp.Rational(1, 1152) / H ** 4}
RECORD_HISTORY = {A: 1, beta: sp.Rational(4, 3), H: 1}
shifted = {name: sp.expand(value.subs(AUTHOR).subs(RECORD_HISTORY))
           for name, value in (("minus_rho", -kappa_rho - Lam), ("p3", kappa_p3 - Lam),
                               ("p0", kappa_p0 - Lam))}  # kappa T - Lambda
```

`AUTHOR` holds the author's weights $\alpha_k = w_k/H^{2k}$, and `RECORD_HISTORY` the history $A = 1$, $\beta = \tfrac43$ with $H = 1$. `shifted` holds $\kappa T - \Lambda$ on this history: $-\kappa\rho - \Lambda$, $\kappa p_3 - \Lambda$ and $\kappa p_0 - \Lambda$, which do not depend on $\Lambda$.

```python
stored = record["exponentialHistory"]["authorWeights"]["historySource_kappaT_minus_Lam"]
same = all(sp.expand(parse(stored[key]["input"]) - shifted[name]) == 0
           for key, name in (("minus_rho", "minus_rho"), ("p3", "p3"), ("p0", "p0"),
                             ("pt", "p0")))
reproduces(same, "the author's weights: kappa T - Lambda of the record history",
           PY, "author_weights_history_source")
```

They must equal the record (key `historySource_kappaT_minus_Lam`, with the record's `pt` compared with $p_0$; sympy report, `author_weights_history_source`).

```python
LAMBDA = -10  # the record's Lambda for the author's weights
author = {"rho": sp.expand(-shifted["minus_rho"] - LAMBDA),
          "p3": sp.expand(shifted["p3"] + LAMBDA),
          "p0": sp.expand(shifted["p0"] + LAMBDA)}
for name, value in author.items():
    report(f"author's weights, Lambda = -10: kappa {name}", value)
```

With the record's $\Lambda = -10$ the cell forms $\kappa\rho = -(-\kappa\rho - \Lambda) - \Lambda$, $\kappa p_3 = (\kappa p_3 - \Lambda) + \Lambda$ and $\kappa p_0$ in the same way, and prints them (Out [9]): $\kappa\rho = \tfrac9{16}k^2 - \tfrac{161}{24}k + \tfrac{4199}{432}$, $\kappa p_3 = -\tfrac9{16}k^2 + \tfrac{1601}{216}k - \tfrac{44239}{3888}$ and $\kappa p_0 = \tfrac{79}{16}k - \tfrac{1937}{144}$.

```python
anisotropy = sp.expand(author["p3"] - author["p0"])
report("kappa (p3 - p0)", anisotropy)
eos_text = record_detail(EOS, "condensate_cannot_source_history")
reproduces(sp.expand(anisotropy - (-sp.Rational(9, 16) * kk ** 2
                                   + sp.Rational(1069, 432) * kk
                                   + sp.Rational(2015, 972))) == 0
           and "-9*kk**2/16 + 1069*kk/432 + 2015/972" in eos_text,
           "the history needs kappa (p3 - p0) = -9 k^2/16 + 1069 k/432 + 2015/972",
           EOS, "condensate_cannot_source_history")
```

The anisotropy $\kappa(p_3 - p_0)$ is printed, `-9*kk**2/16 + 1069*kk/432 + 2015/972`: a polynomial in $k$ that is not zero, so a source with equal pressures cannot drive this history. The check requires this polynomial and the same text in the detail of the dark-sector record's check `condensate_cannot_source_history`, which states that no condensate is the source of the record history.

```python
roots = [r for r in sp.Poly(author["rho"], kk).nroots() if r.is_real and r > 0]
k_zero = min(roots)  # the value of k where kappa rho changes sign
x_zero = 1.5 * float(sp.log(k_zero))  # k = e^(2 x4/3)
report("kappa rho changes sign at k, x4", f"{float(k_zero):.6f}, {x_zero:.6f}")
gas_text = record_detail(KS_A4, "C3_record_history_not_sourced_by_the_gas")
reproduces(0.75 < x_zero < 0.8
           and "changes sign between the dense slices a4 = 0.75 and 0.8" in gas_text,
           "kappa rho changes sign between a4 = 0.75 and a4 = 0.8",
           KS_A4, "C3_record_history_not_sourced_by_the_gas")
```

`nroots` computes the roots of the polynomial $\kappa\rho$ in $k$ numerically; the comprehension keeps the real positive ones, and `k_zero` is the smallest. On the history $k = e^{2x_4/3}$, so the time is $x_4 = \tfrac32\ln k$. The cell prints `kappa rho changes sign at k, x4 = 1.687791, 0.785131`. The record of the Kohn-Sham source states that this energy density changes sign between the slices $a_4 = 0.75$ and $0.8$ (on the history $a_4 = x_4$); the check requires both the notebook's time inside that interval and this sentence in the record.

```python
slices = [0.0, 0.5, 1.0, 1.5, 2.0]
values = [float(author["rho"].subs(kk, np.exp(2.0 * a / 3.0))) for a in slices]
printed = [f"{value:.6g}" for value in values]
say("kappa rho at a4 = 0, 0.5, 1, 1.5, 2: " + ", ".join(printed))
ks_text = record_detail(KS, "ks_history_is_a_prescribed_background")
stated = re.findall(r"kappa rho = (\S+?),", ks_text)
```

The five slices $a_4 = 0, 0.5, 1, 1.5, 2$ of the Kohn-Sham record: `values` holds $\kappa\rho$ at each ($k = e^{2a_4/3}$), and `printed` the values with six significant digits (`.6g`). The cell prints `3.57407, 1.45327, -1.2122, -4.35889, -7.63383`. `re.findall` collects every number that follows `kappa rho = ` and ends before a comma in the detail text of the record of the source conditions (the pattern `\S+?` takes the shortest run of characters that are not blanks).

```python
reproduces(stated == printed,
           "the five energy densities equal the record of the source conditions",
           KS, "ks_history_is_a_prescribed_background")
```

The record's five numbers must be exactly the printed ones (record of the source conditions, `ks_history_is_a_prescribed_background`). Out [9] shows three PASS lines among the printed lines.

**In [10], figure 12b.4: the source with the author's weights.**

```python
fig, ax = plt.subplots()
for name, style, label in (("rho", "-", "$\\kappa\\rho$"), ("p3", "--", "$\\kappa p_3$"),
                           ("p0", ":", "$\\kappa p_0 = \\kappa p_t$")):
    function = sp.lambdify(kk, author[name], "numpy")
    ax.plot(x_axis, function(k_axis) * np.ones_like(k_axis), style, label=label)
ax.plot(slices, values, "o", color="black", markersize=4,
        label="the five slices of the record")
```

The three components with the author's weights, drawn against the time with three line styles, and the energy densities at the five slices as black dots.

```python
ax.axvline(x_zero, color="grey", linewidth=0.8)
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("time $x_4$ (units $1/H$)")
ax.set_ylabel("required source (units $H^2/\\kappa$)")
ax.set_title("The author's weights, $\\Lambda = -10$: the source of the record history")
ax.legend(fontsize=8)
```

A grey vertical line at the time where $\kappa\rho$ changes sign, a black line at zero, labels, title and legend.

```python
save_figure(fig, "author_weights_source",
            "The source that the record history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ "
...)
```

`save_figure` (caption under figure 12b.4). The energy density falls from 3.57407 through zero at $x_4 = 0.785$; a source whose energy density changes sign is not ordinary matter.

**In [11], the two null energy conditions.**

```python
null_record = record["generalSource"]["nullCombinations"]
null_x0 = sp.expand((kappa_rho + kappa_p0).subs(EINSTEIN))
null_x1 = sp.expand((kappa_rho + kappa_p3).subs(EINSTEIN))
same = all(sp.expand(parse(null_record[key]["input"]).subs(EINSTEIN)
                     .subs(EXPONENTIAL) - value) == 0
           for key, value in (("kappa(rho+p0)", null_x0), ("kappa(rho+p3)", null_x1)))
```

`null_record` is the record's key `generalSource/nullCombinations`, which stores $\kappa(\rho + p_0)$ and $\kappa(\rho + p_3)$ for general couplings and histories. `null_x0` and `null_x1` are the notebook's Einstein combinations on the exponential histories, and `same` compares them with the record's after inserting Einstein gravity and the exponential history.

```python
reproduces(same and sp.expand(null_x0 + sp.Rational(3, 2) * H ** 2
                              * (2 * kk + A ** 2 * (4 - beta))) == 0
           and sp.expand(null_x1 + A ** 2 * H ** 2 * (beta - 2) * (beta - 4)) == 0,
           "Einstein, exponential: the two null combinations of the record",
           PY, "json_required_source_and_null_combinations")
range_x1 = sp.solve_univariate_inequality(-(beta - 2) * (beta - 4) >= 0, beta,
                                          relational=False)
```

The check also requires the forms of Section 12.11: $\kappa(\rho + p_0) = -\tfrac32H^2(2k + A^2(4 - \beta))$ and $\kappa(\rho + p_3) = -A^2H^2(\beta - 2)(\beta - 4)$ (sympy report, `json_required_source_and_null_combinations`). `range_x1` is the set of $\beta$ where $-(\beta - 2)(\beta - 4) \ge 0$.

```python
kp, Ap = sp.symbols("kp Ap", positive=True)  # k > 0 and A^2 > 0
beta_edge = sp.solve(2 * kp + Ap ** 2 * (4 - beta), beta)[0]  # rho + p0 = 0
say(f"rho + p3 >= 0 for beta in {range_x1}; rho + p0 >= 0 needs beta >= {beta_edge}")
check(range_x1 == sp.Interval(2, 4) and sp.simplify(beta_edge - 4) == 2 * kp / Ap ** 2,
      "Einstein: no exponential history satisfies both null energy conditions")
author_null = {name: sp.expand(author["rho"] + author[name]) for name in ("p0", "p3")}
```

For the second condition, `kp` stands for $k > 0$ and `Ap` for $|A| > 0$; `beta_edge` is the $\beta$ at which $\rho + p_0 = 0$. The cell prints (Out [11]) `rho + p3 >= 0 for beta in Interval(2, 4); rho + p0 >= 0 needs beta >= 4 + 2*kp/Ap**2`. The check: the first range is $[2, 4]$ and the second starts beyond 4, so they do not meet. `author_null` holds the two combinations with the author's weights on the record history.

```python
report("author's weights: kappa (rho + p0)", author_null["p0"])
report("author's weights: kappa (rho + p3)", author_null["p3"])
```

They are printed as RESULT lines: $\kappa(\rho + p_0) = \tfrac9{16}k^2 - \tfrac{85}{48}k - \tfrac{403}{108}$ and $\kappa(\rho + p_3) = \tfrac{19}{27}k - \tfrac{403}{243}$. At $k = 1$ (the start, $x_4 = 0$) both are negative: $\tfrac9{16} - \tfrac{85}{48} - \tfrac{403}{108} = -\tfrac{1067}{216}$ and $\tfrac{19}{27} - \tfrac{403}{243} = -\tfrac{232}{243}$. The second becomes positive for $k > \tfrac{403}{243}\cdot\tfrac{27}{19} = \tfrac{403}{171} = 2.357$ (at $x_4 = 1.29$), the first for $k > \tfrac{124}{27} = 4.593$ (the positive root of the quadratic; at $x_4 = 2.29$): with the author's weights the source of the record history violates both null energy conditions at early times.

**In [12], figure 12b.5: the null energy map of Einstein gravity.**

```python
b_grid, k_grid = np.meshgrid(np.linspace(0.0, 7.0, 351), np.linspace(-2.0, 3.0, 251))
nec_x0 = (2 * k_grid + (4 - b_grid)) <= 0  # A = 1
nec_x1 = (b_grid - 2) * (b_grid - 4) <= 0
region = np.where(nec_x0 & nec_x1, 3, np.where(nec_x0, 2, np.where(nec_x1, 1, 0)))
fig, ax = plt.subplots()
colours = matplotlib.colors.ListedColormap(["#f7f7f7", "#d1e5f0", "#fddbc7",
                                            "#b2182b"])
```

`np.meshgrid` makes two 251 by 351 arrays holding the $\beta$ and the $k/A^2$ value of every point of a grid. `nec_x0` and `nec_x1` are arrays of truth values: where each condition holds (with $A = 1$). `np.where(condition, a, b)` takes `a` where the condition is true and `b` elsewhere; the nested calls give 3 where both hold, 2 where only the condition along $x_4 + x_0$ holds, 1 where only the one along $x_4 + x_1$ holds, and 0 where none does. `ListedColormap` makes a colour map of four colours: light grey, light blue, pink and dark red.

```python
ax.pcolormesh(b_grid, k_grid, region, cmap=colours, vmin=-0.5, vmax=3.5,
              shading="auto")
ax.plot(b_grid[0], (b_grid[0] - 4.0) / 2.0, color="black",
        label="$\\rho + p_0 = 0$: $k/A^2 = (\\beta - 4)/2$")
ax.axhline(0.0, color="black", linewidth=1.2)
ax.axvline(4.0 / 3.0, color="black", linestyle=":", label="record history")
```

`pcolormesh` colours the grid by `region`; the limits from $-0.5$ to $3.5$ put each of the values 0, 1, 2, 3 in the middle of one colour. The black line is $\rho + p_0 = 0$, the thick horizontal line is $k = 0$, and the dotted line marks the record history.

```python
ax.text(3.0, 2.3, "$\\rho + p_3 \\geq 0$", ha="center", fontsize=9)
ax.text(5.8, -1.2, "$\\rho + p_0 \\geq 0$", ha="center", fontsize=9)
ax.text(1.0, 2.3, "both violated", ha="center", fontsize=9)
ax.set_xlabel("$\\beta$")
ax.set_ylabel("$k/A^2$")
ax.set_title("Einstein gravity: the two null energy conditions")
```

Three texts name the regions; then the labels and the title.

```python
ax.legend(fontsize=8, loc="lower right")
save_figure(fig, "null_energy_map",
            "Einstein gravity on the exponential histories: the plane of $\\beta$ "
...)
```

The legend and `save_figure` (caption under figure 12b.5). Above $k = 0$, where every history lies, the blue band and the pink region do not overlap; the dark red region where both hold lies entirely below $k = 0$.

**In [13], Einstein-Gauss-Bonnet vacua.**

```python
GAUSS_BONNET = {alpha1: 1, alpha3: 0, H: 1}
coefficients = []
for value in (kappa_rho, kappa_p3, kappa_p0):
    polynomial = sp.Poly(sp.expand(value.subs(GAUSS_BONNET)), kk)
    coefficients += [c for c in polynomial.all_coeffs() if c != 0]
basis = sp.groebner(coefficients, A, beta, alpha2, Lam, order="lex")
```

`GAUSS_BONNET` sets $\alpha_1 = 1$, $\alpha_3 = 0$, $H = 1$. For each of the three components the cell writes the source as a polynomial in $k$ and collects its coefficients that are not zero: where $k$ changes in time, a vacuum needs every coefficient to vanish. `sp.groebner` computes a **Groebner basis** of these polynomial equations in $A$, $\beta$, $\alpha_2$ and $\Lambda$: a systematic elimination that produces an equivalent set of equations; the basis `[1]` means the equation $1 = 0$, so the equations have no common solution at all (not even a complex one).

```python
say(f"Gauss-Bonnet, k varies: {len(coefficients)} coefficient equations, "
    f"Groebner basis {list(basis.exprs)}")
reproduces(list(basis.exprs) == [1],
           "Einstein-Gauss-Bonnet: no vacuum exponential history where k varies",
           PY, "egb_no_vacuum_where_k_varies")
k0 = sp.symbols("k0", positive=True)  # the constant k on beta = 2
```

The cell prints (Out [13]) `Gauss-Bonnet, k varies: 8 coefficient equations, Groebner basis [1]` and checks the basis (sympy report, `egb_no_vacuum_where_k_varies`). `k0` is the constant $k$ on the histories with $\beta = 2$.

```python
CONSTANT = {beta: 2, kk: k0}
time_eq, space_eq, hidden_eq = (sp.expand(value.subs(GAUSS_BONNET).subs(CONSTANT))
                                for value in (kappa_rho, kappa_p3, kappa_p0))
branch = sp.solve([time_eq, hidden_eq], [alpha2, Lam], dict=True)[0]
say(f"beta = 2: alpha2 = {sp.factor(branch[alpha2])}, Lambda = {sp.factor(branch[Lam])}")
reproduces(sp.simplify(branch[alpha2] + 1 / (4 * (A ** 2 - k0))) == 0
           and sp.simplify(branch[Lam] - 3 * (A ** 4 + 3 * A ** 2 * k0 + k0 ** 2)
                           / (A ** 2 - k0)) == 0
           and sp.simplify(space_eq.subs(branch)) == 0,
           "Einstein-Gauss-Bonnet vacua on constant k: alpha2 and Lambda as recorded",
           PY, "egb_exponential_vacuum_branches")
```

`CONSTANT` inserts $\beta = 2$ and $k = k_0$. `sp.solve` solves the time and the hidden equations for $\alpha_2$ and $\Lambda$ (`dict=True` returns the solution as a dictionary); the cell prints `alpha2 = 1/(4*(-A**2 + k0))` and `Lambda = -3*(A**4 + 3*A**2*k0 + k0**2)/(-A**2 + k0)`, which are the forms $-1/(4H^2(A^2 - k_0))$ and $3H^2(A^4 + 3A^2k_0 + k_0^2)/(A^2 - k_0)$ of Notebook 12b's text with $H = 1$. The check also requires that the 3-space equation then holds (sympy report, `egb_exponential_vacuum_branches`).

**In [14], figure 12b.6: the Gauss-Bonnet vacua.**

```python
alpha2_f = sp.lambdify(k0, branch[alpha2].subs(A, 1), "numpy")
lambda_f = sp.lambdify(k0, branch[Lam].subs(A, 1), "numpy")
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
for low, high in ((0.05, 0.9), (1.1, 4.0)):
    k_part = np.linspace(low, high, 200)
    left.plot(k_part, alpha2_f(k_part), color="tab:blue")
    right.plot(k_part, lambda_f(k_part), color="tab:orange")
```

The two solutions at $A = 1$ as numpy functions of $k_0$, and two panels. Each is drawn on two pieces, $0.05 \le k_0 \le 0.9$ and $1.1 \le k_0 \le 4$, leaving out the neighbourhood of $k_0 = 1 = A^2$, where both diverge.

```python
for ax in (left, right):
    ax.axvline(1.0, color="grey", linestyle="--", linewidth=0.8)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("$k_0/A^2$")
left.set_ylim(-3.0, 3.0)
right.set_ylim(-80.0, 80.0)
```

In both panels a dashed line at $k_0 = 1$, a line at zero and the horizontal label; then the vertical ranges.

```python
left.set_ylabel("$\\alpha_2 H^2$ of the vacuum")
right.set_ylabel("$\\Lambda/H^2$ of the vacuum")
fig.suptitle("Einstein-Gauss-Bonnet gravity: the vacua on constant $k$ ($A = 1$)")
save_figure(fig, "gauss_bonnet_vacuum",
            "The vacuum solutions of Einstein-Gauss-Bonnet gravity ($\\alpha_1 = 1$, "
...)
```

The vertical labels, a title over both panels and `save_figure` (caption under figure 12b.6). The coupling $\alpha_2H^2$ is negative for $k_0 < 1$ and positive for $k_0 > 1$; on these histories the block does not shrink.

**In [15], the author's weights allow no exponential vacuum.**

```python
AUTHOR_VACUUM = {alpha1: 1, alpha2: sp.Rational(1, 32), alpha3: sp.Rational(1, 1152),
                 Lam: LAMBDA, H: 1}
s = sp.symbols("s")  # 1 - s A (beta - 2) = 0 makes A != 0 and beta != 2
coefficients = []
for value in (kappa_rho, kappa_p3, kappa_p0):
    polynomial = sp.Poly(sp.expand(value.subs(AUTHOR_VACUUM)), kk)
    coefficients += [c for c in polynomial.all_coeffs() if c != 0]
```

`AUTHOR_VACUUM` holds the author's weights, $\Lambda = -10$ and $H = 1$. The coefficients of the powers of $k$ of the three components are collected as in In [13]. `s` is an extra symbol: the equation $1 - sA(\beta - 2) = 0$ can hold only if $A \ne 0$ and $\beta \ne 2$ (otherwise its left side is 1), so adding it restricts the elimination to the histories where $k$ changes.

```python
basis = sp.groebner(coefficients + [1 - s * A * (beta - 2)], s, A, beta, order="lex")
A2 = sp.symbols("A2", real=True)  # A^2
time_k0 = sp.expand(16 * kappa_rho.subs(AUTHOR_VACUUM).subs(CONSTANT)).subs(A ** 2, A2)
space_k0 = sp.expand(16 * kappa_p3.subs(AUTHOR_VACUUM).subs(CONSTANT)).subs(A ** 2, A2)
hidden_k0 = sp.expand(16 * kappa_p0.subs(AUTHOR_VACUUM).subs(CONSTANT))
hidden_k0 = hidden_k0.subs(A ** 4, A2 ** 2).subs(A ** 2, A2)
```

The Groebner basis of the coefficients together with that equation. `A2` stands for $A^2$. On $\beta = 2$ with $k = k_0$ the three components, multiplied by 16 to clear fractions, become polynomials in $A^2$ and $k_0$; the hidden one also contains $A^4$, which is replaced first.

```python
resultant = sp.factor(sp.resultant(time_k0, hidden_k0, A2))
shared = []  # (k0, the common root A^2) at every real zero k0 > 0 of the resultant
for root in sp.Poly(resultant, k0).nroots():
    if root.is_real and root > 0:
        common = sp.solve(time_k0.subs(k0, root), A2)
        shared.append((float(root), float(common[0])))
```

The **resultant** of two polynomials in $A^2$ is a polynomial in $k_0$ that vanishes exactly where the two have a common root; `sp.factor` writes it as a product. For each real positive zero of the resultant (found numerically with `nroots`), the cell solves the time equation for the common root $A^2$ and stores the pair.

```python
static = sp.solve([sp.expand(kappa_rho.subs(AUTHOR_VACUUM).subs(A, 0)),
                   sp.expand(kappa_p0.subs(AUTHOR_VACUUM).subs(A, 0))], kk)
say(f"k varies: Groebner basis {list(basis.exprs)}")
say("beta = 2, resultant in k0: " + str(resultant))
say("its positive zeros k0 and the shared root A^2: "
    + ", ".join(f"({k_value:.4f}, {a_value:.4f})" for k_value, a_value in
                sorted(set((round(a, 6), round(b, 6)) for a, b in shared))))
```

`static` solves the time and the hidden equations on the static histories $A = 0$ for $k$; the empty list means no solution. The cell prints (Out [15]) the basis `[1]`, the resultant `-12*(3*k0**2 - 80*k0 + 112)*(3*k0**3 - 42*k0**2 + 144*k0 - 160)`, and the pairs $(k_0, A^2)$: $(1.4824, -25.1843)$, $(9.5644, -9.5644)$, $(25.1843, -1.4824)$ (`round` and `set` remove repeated pairs, `sorted` orders them).

```python
reproduces(list(basis.exprs) == [1] and sp.expand(time_k0 + space_k0) == 0
           and all(a_value < 0 for _, a_value in shared) and static == [],
           "the author's weights: no exponential history is a vacuum",
           PY, "author_weights_no_exponential_vacuum")
```

The check: no solution where $k$ varies; on $\beta = 2$ the time and 3-space equations coincide (their sum vanishes identically, because the constraint does not change in time there: $h = 0$ in the Bianchi identity of Section 12.10 gives $e_{11} = e_{44}$); every common root $A^2$ is negative, so $A$ is not real; and the static histories give nothing (sympy report, `author_weights_no_exponential_vacuum`).

**In [16], figure 12b.7: no real vacuum with the author's weights.**

```python
k_grid, a_grid = np.meshgrid(np.linspace(0.05, 30.0, 600), np.linspace(-40.0, 40.0, 600))
time_f = sp.lambdify((k0, A2), time_k0, "numpy")
hidden_f = sp.lambdify((k0, A2), hidden_k0, "numpy")
fig, ax = plt.subplots()
ax.axhspan(-40.0, 0.0, color="grey", alpha=0.25)
ax.contour(k_grid, a_grid, time_f(k_grid, a_grid), levels=[0.0], colors="tab:blue")
```

A 600 by 600 grid of $k_0$ (0.05 to 30) and $A^2$ ($-40$ to 40), the two polynomials as numpy functions, a grey band for $A^2 < 0$, and `contour(..., levels=[0.0])`, which draws the curve where the time equation vanishes.

```python
ax.contour(k_grid, a_grid, hidden_f(k_grid, a_grid), levels=[0.0],
           colors="tab:red", linestyles="--")
ax.plot([], [], color="tab:blue", label="time (and 3-space) equation: $\\rho = 0$")
ax.plot([], [], color="tab:red", linestyle="--", label="hidden equation: $p_0 = 0$")
ax.plot([k for k, _ in shared], [a for _, a in shared], "o", color="black",
        markersize=4, label="where both hold ($A^2 < 0$)")
```

The curve of the hidden equation, dashed; two empty plots for the legend entries; and the shared points of In [15] as black dots.

```python
ax.set_xlabel("$k_0 = e^{2a_4}/b_4$ (constant)")
ax.set_ylabel("$A^2$")
ax.set_title("The author's weights, $\\beta = 2$: no real vacuum")
ax.legend(fontsize=8, loc="upper right")
save_figure(fig, "author_weights_no_vacuum",
            "The author's weights ($\\alpha_k = w_k/H^{2k}$, $w = (1, 1/32, 1/1152)$, "
...)
```

Labels, title, legend and `save_figure` (caption under figure 12b.7). The two curves meet only in the grey region.

**In [17], a source with equal pressures.**

```python
equal = sp.expand((kappa_p3 - kappa_p0) / (H ** 2))  # must vanish
einstein_equal = sp.factor(sp.expand(equal.subs(EINSTEIN)))
k_needed = sp.solve(einstein_equal, kk)[0]
say(f"Einstein: p3 = p0 needs k = {sp.factor(k_needed)}")
reproduces(sp.expand(3 * k_needed - A ** 2 * (beta - 4) * (beta - sp.Rational(1, 2)))
           == 0 and sp.expand(k_needed.subs(beta, 2) + A ** 2) == 0,
           "Einstein: equal pressures on an exponential history need k = -A^2 or 0",
           PY, "condensate_source_equal_pressures")
```

`equal` is $\kappa(p_3 - p_0)/H^2$, which must vanish for a source with equal pressures such as a homogeneous condensate (Section 12.26). In Einstein gravity it vanishes at one $k$, which the cell prints (Out [17]): `A**2*(beta - 4)*(2*beta - 1)/6`, that is $\tfrac13A^2(\beta - 4)(\beta - \tfrac12)$. The check: three times it equals $A^2(\beta - 4)(\beta - \tfrac12)$, and at $\beta = 2$ (the only $\beta$ with constant $k$ when $A \ne 0$) it is $-A^2 < 0$ (sympy report, `condensate_source_equal_pressures`).

```python
author_equal = sp.expand(equal.subs(AUTHOR).subs(H, 1))
k_coefficients = [c for c in sp.Poly(author_equal, kk).all_coeffs() if c != 0]
varying = sp.groebner(k_coefficients + [1 - s * A * (beta - 2)], s, A, beta,
                      order="lex")
on_beta2 = sp.solve(sp.factor(author_equal.subs({beta: 2, kk: k0})), k0)
static_k = sp.solve(author_equal.subs({A: 0}), kk)
```

With the author's weights ($H = 1$), the coefficients of the powers of $k$ are collected and eliminated together with $1 - sA(\beta - 2) = 0$ (no solution where $k$ varies); on $\beta = 2$ the condition is solved for $k_0$, and on $A = 0$ for $k$.

```python
say(f"author's weights, beta = 2: k0 = {on_beta2}; A = 0: k = {static_k}")
reproduces(list(varying.exprs) == [1]
           and any(sp.simplify(r - (16 + 2 * A ** 2) / (2 + A ** 2)) == 0
                   for r in on_beta2) and 8 in static_k,
           "the author's weights: equal pressures only for constant k",
           WL, "condensate_source_equal_pressures")
```

The cell prints `k0 = [2*(A**2 + 8)/(A**2 + 2)]` and `k = [0, 8]`, and checks the Groebner basis `[1]`, the solution $k_0 = (16 + 2A^2)/(2 + A^2)$ and the static solution $k = 8$ (Wolfram report, `condensate_source_equal_pressures`). Out [17] shows two printed lines and two PASS lines.

**In [18], figure 12b.8: when a source with equal pressures fits.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
beta_axis = np.linspace(-1.0, 6.0, 351)
left.axhspan(-6.0, 0.0, color="grey", alpha=0.25, label="$k \\leq 0$")
left.plot(beta_axis, (beta_axis - 4.0) * (beta_axis - 0.5) / 3.0,
          label="$k/A^2 = (\\beta - 4)(\\beta - 1/2)/3$")
left.axvline(2.0, color="black", linestyle="--", linewidth=0.8,
             label="$\\beta = 2$: $k$ constant")
```

Two panels. Left: the grey band $k \le 0$, the curve $k/A^2 = (\beta - 4)(\beta - \tfrac12)/3$ on which the Einstein pressures would be equal at one moment, and the dashed line $\beta = 2$, where $k$ is constant.

```python
left.plot([2.0], [-1.0], "o", color="black")
left.set_ylim(-6.0, 8.0)
left.set_xlabel("$\\beta$")
left.set_ylabel("$k/A^2$")
left.set_title("Einstein gravity")
left.legend(fontsize=8)
```

The black point where the curve crosses $\beta = 2$, at $k/A^2 = -1$; the range, labels, title and legend of the left panel.

```python
slopes = np.linspace(0.0, 4.0, 200)
right.plot(slopes, (16 + 2 * slopes ** 2) / (2 + slopes ** 2))
right.set_xlabel("slope $A$")
right.set_ylabel("$k_0$ with equal pressures")
right.set_title("the author's weights, $\\beta = 2$")
save_figure(fig, "condensate_conditions",
            "When can a source with equal pressures, such as a homogeneous condensate "
...)
```

Right: the constant values $k_0 = (16 + 2A^2)/(2 + A^2)$ of the author's weights against the slope $A$ from 0 to 4 (they fall from 8 towards 2); labels, title, and `save_figure` (caption under figure 12b.8).

**In [19], the last check.**

```python
figure_names = ["einstein_source", "sign_symmetry", "beta_scan",
                "author_weights_source", "null_energy_map", "gauss_bonnet_vacuum",
                "author_weights_no_vacuum", "condensate_conditions"]
paths = [output_file(f"{FIGURE_FOLDER}/12b_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths), "all eight figure files exist")
all_checks_passed()
```

The eight figure names, the paths of the files `12b_1_einstein_source.png` to `12b_8_condensate_conditions.png` (`enumerate(..., 1)` numbers them from 1), the check that all exist, and the last line, ALL 23 CHECKS PASSED (notebook 12b).

### 12.21 Solving the two equations of second order for a prescribed source

**The initial value problem.** Section 12.9 showed that, given the pressures, the 3-space and block equations fix $a_4''$ and $v = u'$ wherever $\det J \ne 0$. Together with $a_4' = da_4/dx_4$ and $u = d\ln b_4/dx_4$ they form a system of **ordinary differential equations** (equations for unknown functions of one variable that contain their derivatives) for the four numbers

$$
a_4,\quad a_4',\quad \ln b_4,\quad u .
$$

We use $\ln b_4$ instead of $b_4$ because $b_4 > 0$ grows or shrinks exponentially; its logarithm changes smoothly, and $b_4 = e^{\ln b_4}$ is positive automatically. Given the four starting values at $x_4 = 0$ and the pressures $\kappa p_3$ and $\kappa p_0 = \kappa p_t$ as functions of the time (or of the state), the system determines the future: an **initial value problem**. Chapter 2 taught the fourth-order Runge-Kutta method (RK4) for such problems; Notebook 12c uses it. Every source in this section is **prescribed** (chosen by hand to see what the equations do): its status is ASSUMED, and nothing here says that a field of the theory produces it.

**The energy density.** The constraint gives $\kappa\rho = -(e_{44} + \Lambda)$ at every moment. Notebook 12c computes it once, at the start, and then carries $\kappa\rho$ along with the energy exchange of Section 12.10,

$$
\frac{d}{dx_4}(\kappa\rho) = -3a_4'\,\kappa(\rho + p_3) - 4h\,\kappa(\rho + p_0),\qquad h = \tfrac12u - a_4' .
$$

So the solver advances five numbers, $y = (a_4, a_4', \ln b_4, u, \kappa\rho)$. Section 12.10 proved that the constraint then stays satisfied ($C = 0$ at every time if $C = 0$ at the start). Along a numerical solution the difference between the carried $\kappa\rho$ and $-(e_{44} + \Lambda)$, the **constraint gap**, therefore measures the numerical error; Notebook 12c checks that it stays at the level of $10^{-8}$ (COMPUTED).

**Tests with exact solutions.** Three prescribed sources have known solutions.

1. No source, Einstein gravity: the flat member of Section 12.11 with $c = -1/H$, which starts at $a_4 = a_4' = 0$, $b_4 = 1$, $u = 2H$ and has $\ln b_4 = 2\ln(1 + Hx_4)$, $u = 2H/(1 + Hx_4)$. Its constraint gives $\kappa\rho(0) = -(0 + 6 - \tfrac32\cdot 4) = 0$ (units $H = 1$), as a vacuum needs.
2. The source of the record history, as a function of the time (Section 12.12): in Einstein gravity with $\Lambda = 0$, $\kappa p_3 = 6k - \tfrac{13}9$ and $\kappa p_0 = 3k - \tfrac{11}3$ with $k = e^{2x_4/3}$; with the author's weights the record's formulas with $\Lambda = -10$. Started on the history ($a_4 = 0$, $a_4' = 1$, $b_4 = 1$, $u = \tfrac43$), the solver must stay on it.
3. A history chosen first: its source is computed from the field equations and then integrated; the solver must return the chosen history. Notebook 12c uses a **pulse** in the rate, $a_4' = 1 + \tfrac12\big(\mathrm{erf}((x_4 - 3)/0.5) + \mathrm{erf}(6)\big)$ with $b_4 = e^{(4/3)a_4}$, which rises from $H$ to almost exactly $2H$ around $x_4 = 3$ (the **error function** erf rises smoothly from $-1$ to $1$ and is odd, $\mathrm{erf}(-s) = -\mathrm{erf}(s)$; the added $\mathrm{erf}(6)$ makes $a_4'(0) = 1$ exactly, and long after the pulse the rate is $1 + \tfrac12(1 + \mathrm{erf}\,6)$, which differs from 2 by about $10^{-17}$). Before the pulse it is the record history; after it, the exponential history with $A = 2$, $\beta = \tfrac43$, whose Einstein source has constant terms four times larger: $(\kappa\rho, \kappa p_3, \kappa p_0) = (-6k - \tfrac43, 6k - \tfrac{52}9, 3k - \tfrac{44}3)$, the formulas of Section 12.12 with $A^2 = 4$.

The same source with other starting values gives other histories: the source does not select the history, the starting values do. Notebook 12c shows this by starting the source of the record history with $a_4'(0) = 1.05$ and $0.95$.

**A gas of massless particles.** Now a source that depends on the state: particles without mass that move only in 3-space, with $p_3 = \tfrac13\rho$ and $p_0 = p_t = 0$. Its energy exchange gives, line by line,

$$
\partial_4\rho = -3a_4'\big(\rho + \tfrac13\rho\big) - 4h\,(\rho + 0) = -4a_4'\rho - 4\big(\tfrac12u - a_4'\big)\rho
$$

(the energy exchange of Section 12.10 with $p_3 = \rho/3$ and $p_0 = 0$; then $h$ inserted)

$$
\partial_4\rho = -2u\,\rho = -2\frac{b_4'}{b_4}\rho \quad\Longrightarrow\quad \frac{d}{dx_4}\ln\rho = -2\frac{d}{dx_4}\ln b_4 \quad\Longrightarrow\quad \rho = \sigma_0\,b_4^{-2}
$$

(the terms with $a_4'$ cancel; divided by $\rho$; integrated, with the constant $\sigma_0$). So this gas conserves its energy on every history automatically. The record identifies it as the Kohn-Sham states without interaction, averaged over the hidden direction (record `Revision/field_equations_a4/ks_source/reports/ks-source-a4.json`, checks `A5_free_fold_band_gas_conserves_energy` and `D0_free_gas_average_exact`; Chapter 17 treats this source). With the author's weights and the starting values of the record history the constraint fixes

$$
\kappa\sigma_0 = -\big(e_{44} + \Lambda\big)\Big|_{a_4' = 1,\ u = 4/3,\ k = 1} = -\Big(-\tfrac9{16} + \tfrac{161}{24} + \tfrac{121}{432} - 10\Big) = 10 - \tfrac{2776}{432} = \tfrac{193}{54} = 3.57407
$$

(the record's constraint of Section 12.12 at $k = 1$; common denominator 432: $-243 + 2898 + 121 = 2776$). Integrated forward, the rates leave the record history and the determinant of the Jacobian falls to zero: there $a_4''$ and $v$ grow without bound and the system has no smooth continuation. The record finds this point at $x_4 = 0.428813$, with $a_4 = 0.361572$ and $b_4 = 0.862627$ (record `ks-source-a4.json`, check `D2_author_weights_from_the_record_history`); Notebook 12c finds the sign change of $\det J$ just after $x_4 = 0.428800$ with its fixed step $2\times10^{-5}$ (COMPUTED; Figure 12c.7).

**Which sources are real? The Kohn-Sham states.** The only many-particle states that the Revision record has computed are the Kohn-Sham states of dirac16complex (Chapters 14 and 15). The record asks whether they can be the source of the corrected metric (`Revision/field_equations_a4/reports/ks-source-conditions.json`, 5 checks, all PASS). A source must satisfy three conditions of Section 12.8: (C1) no component depends on $x_0$; (C2) $p_0 = p_t$; (C3) no off-diagonal component. The record finds: C1 fails for every one of the 70 states (of 75) whose energy-momentum tensor is not zero, because their energy density varies along the hidden direction; C2 holds exactly for the states without interaction ($\lambda = 0$) and fails for every state with $\lambda \ne 0$; C3 holds for every state. In addition (C4), the ratios $p_3/\rho$, $p_0/\rho$, $p_t/\rho$ of every state differ from those that the record history needs with the author's weights by at least 1.3733 (closest: the state `N592_lamp2_a15`). Conclusion of the record: no recorded Kohn-Sham state is an admissible source, and the record history is a PRESCRIBED background without back-reaction. Notebook 12c recomputes the counts and the smallest distance from the record's table of the integrated energy-momentum tensors (`Revision/kohn_sham/results/ground/emt-integrals.csv`, In [18]).

### 12.22 Example: prescribed sources integrated with RK4

The third notebook writes the solver of Section 12.21 with the record's Lovelock components, tests RK4 on $y' = -y$, integrates the flat member, the record history with its own source (Einstein gravity and the author's weights), the same source from other starting rates, the pulse history and its source, measures the convergence order of RK4 on the flat member, integrates the gas of massless particles with the author's weights to the point where $\det J$ changes sign, and recomputes the record's numbers on the Kohn-Sham states. It prints 21 PASS lines, draws seven figures and runs in about twenty seconds.

<!-- NOTEBOOK 12c -->

### 12.25 Line-by-line walk-through of Notebook 12c

The notebook has 19 code cells, In [1] to In [19]. As in Section 12.16, every line or small group of lines is quoted and explained; docstrings are left out, and long captions are shortened to their first line and `...)` (they are printed in full under the figures in Section 12.24).

**In [1], the set-up cell.** It is the set-up cell of Notebook 12a, explained line by line in Section 12.16 under In [1], with two differences: its comment lines are the run instructions of Notebook 12c (Section 12.23), and its line `NOTEBOOK_ID = "12c"  # this notebook: chapter 12, example c` names this notebook. It prints Set-up of notebook 12c complete: repository folder found, helpers defined.

**In [2], the records and the system.** The cell reads the record's Lovelock components and turns them into seven fast numerical functions that give the whole system.

```python
import contextlib  # redirect_stdout: send printed lines into a buffer
import io  # StringIO: a text buffer in memory
import math  # the error function erf, for an exact solution
```

`contextlib` and `io` for the helper `reproduces`; `math`, Python's module of mathematical functions, for $e^x$, $\ln$ and the error function `math.erf` on single numbers.

```python
import matplotlib.ticker  # control of the tick labels of an axis
import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra, used here only to read the record formulas
```

`matplotlib.ticker` controls the labels of the axis ticks (used in In [15]); `numpy` for arrays; `sympy` only to read the record's formulas and differentiate them once.

```python
PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the equations
KS_A4 = "Revision/field_equations_a4/ks_source/reports/ks-source-a4.json"
KS = "Revision/field_equations_a4/reports/ks-source-conditions.json"
```

Short names for the sympy and Wolfram reports, the equations, the record of the Kohn-Sham source (`KS_A4`) and the record of the source conditions (`KS`).

```python
def read_json(relative):
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))
```

`read_json`, as in Notebook 12a.

```python
def record_verdict(report_file, name):
    for entry in read_json(report_file)["checks"]:
        if entry["name"] == name:
            return entry["verdict"]
    return None
```

`record_verdict`, as in Notebook 12a.

```python
def reproduces(condition, name, report_file, record_name):
    found = record_verdict(report_file, record_name) == "PASS"
    lines = io.StringIO()  # a text buffer
    with contextlib.redirect_stdout(lines):  # print() now writes into the buffer
        check(condition and found, name, record=f"{report_file}, check {record_name}")
    print(lines.getvalue(), end="")  # all lines at once
```

`reproduces`, as in Notebook 12a.

```python
record = read_json(EQUATIONS)
H, ad1, ad2, uu, vv, kk = sp.symbols("H ad1 ad2 uu vv kk", real=True)
a1, a2, a3 = sp.symbols("alpha1 alpha2 alpha3", real=True)
LOCALS = {"H": H, "ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk}
```

The equations are read; the symbols are made (`a1`, `a2`, `a3` for the couplings); `LOCALS` says which symbol each name of the record means.

```python
def from_record(text):
    return sp.sympify(text.replace("^", "**"), locals=LOCALS).subs(H, 1)
```

`from_record` turns a Wolfram text of the record into a sympy expression and sets $H = 1$ (the units of the notebook).

```python
lovelock = record["lovelockTensors"]
weights = {1: a1, 2: a2, 3: a3}
side = {key: sp.expand(sum(weights[k] * from_record(lovelock[f"E{k}"][key]["input"])
                           for k in (1, 2, 3)))
        for key in ("x4x4", "x1x1", "x0x0")}  # sum_k alpha_k E_(k), H = 1
ARGS = (ad1, uu, kk, a1, a2, a3)
```

`side` holds the three components $\sum_k\alpha_kE_{(k)}{}^h{}_h$ for $h = x_4, x_1, x_0$, with the couplings as symbols. `ARGS` lists the arguments of the numerical functions below: $a_4'$, $u$, $k$ and the three couplings.

```python
zero_second = {ad2: 0, vv: 0}
e44 = sp.lambdify(ARGS, side["x4x4"], "numpy")  # the constraint, no a4'' or v
rest1 = sp.lambdify(ARGS, side["x1x1"].subs(zero_second), "numpy")
rest0 = sp.lambdify(ARGS, side["x0x0"].subs(zero_second), "numpy")
J11 = sp.lambdify(ARGS, sp.diff(side["x1x1"], ad2), "numpy")
J12 = sp.lambdify(ARGS, sp.diff(side["x1x1"], vv), "numpy")
```

`zero_second` sets $a_4'' = v = 0$. `sp.lambdify(ARGS, ...)` turns a formula into a numpy function of these six arguments. `e44` is the constraint (it contains no $a_4''$ or $v$), `rest1` and `rest0` are the parts $R_1$, $R_0$ of the 3-space and block components without second derivatives (Section 12.9), and `J11`, `J12` are the entries of the first row of the Jacobian, the derivatives of the 3-space component with respect to $a_4''$ and $v$.

```python
J21 = sp.lambdify(ARGS, sp.diff(side["x0x0"], ad2), "numpy")
J22 = sp.lambdify(ARGS, sp.diff(side["x0x0"], vv), "numpy")
linear = all(sp.diff(side[key], x, y) == 0 for key in ("x1x1", "x0x0")
             for x in (ad2, vv) for y in (ad2, vv))
say(f"the 3-space and hidden components are linear in (a4'', v): {linear}")
EINSTEIN = (1.0, 0.0, 0.0)  # alpha1, alpha2, alpha3 of Einstein gravity
```

`J21`, `J22` are the second row. `linear` checks that the two components contain $a_4''$ and $v$ only to the first power (all second derivatives with respect to them vanish); then the seven functions give the system exactly. The cell prints (Out [2]) that the 3-space and hidden components are linear in $(a_4'', v)$: `True`. `EINSTEIN` is the tuple of couplings $(1, 0, 0)$.

```python
AUTHOR = (1.0, 1.0 / 32.0, 1.0 / 1152.0)  # the author's weights, H = 1
```

`AUTHOR` holds the author's weights at $H = 1$: $(1, \tfrac1{32}, \tfrac1{1152})$.

**In [3], a test of the functions.**

```python
points = np.array([[-2.0, 0.5, 1.0], [-0.5, 1.0, 0.3], [0.0, 2.0, 2.0],
                   [1.0, 4.0 / 3.0, 1.0], [3.0, -1.0, 5.0]])  # (a4', u, k)
a_p, u_p, k_p = points.T
ok = (np.allclose(J11(a_p, u_p, k_p, *EINSTEIN), 2.0)
      and np.allclose(J12(a_p, u_p, k_p, *EINSTEIN), -2.0)
      and np.allclose(J21(a_p, u_p, k_p, *EINSTEIN), 0.0)
      and np.allclose(J22(a_p, u_p, k_p, *EINSTEIN), -1.5)
      and np.allclose(e44(a_p, u_p, k_p, *EINSTEIN), 3 * a_p ** 2 + 6 * k_p
                      - 1.5 * u_p ** 2)
      and np.allclose(rest1(a_p, u_p, k_p, *EINSTEIN), -5 * a_p ** 2 + 6 * a_p * u_p
                      + 6 * k_p - 2.5 * u_p ** 2)
      and np.allclose(rest0(a_p, u_p, k_p, *EINSTEIN), -3 * a_p ** 2 + 1.5 * a_p * u_p
                      + 3 * k_p - 1.5 * u_p ** 2))
```

Five sample points $(a_4', u, k)$ in an array; `.T` (the transpose) splits its three columns into the arrays `a_p`, `u_p`, `k_p`. `np.allclose(a, b)` is true when the two agree to rounding at every point. For Einstein gravity the Jacobian must be $\begin{pmatrix}2 & -2\\ 0 & -\tfrac32\end{pmatrix}$ and the three functions $e_{44}$, $R_1$, $R_0$ those of Section 12.9 with $H = 1$; the star in `*EINSTEIN` hands the three couplings over as separate arguments.

```python
reproduces(ok, "Einstein: J = {{2, -2}, {0, -3/2}} and the three components (H = 1)",
           PY, "einstein_components")
```

The check reproduces the sympy report's `einstein_components` (Out [3]).

**In [4], the Runge-Kutta method.**

```python
def rk4(rhs, y0, h, steps, stop=None):
    xs = [0.0]
    ys = [np.array(y0, dtype=float)]
    for n in range(steps):
        x, y = xs[-1], ys[-1]
        k1 = rhs(x, y)
        k2 = rhs(x + h / 2, y + h / 2 * k1)
        k3 = rhs(x + h / 2, y + h / 2 * k2)
        k4 = rhs(x + h, y + h * k3)
        new = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if stop is not None and stop(y, new):
            break
        xs.append((n + 1) * h)  # (n + 1) h avoids adding up rounding errors
        ys.append(new)
    return np.array(xs), np.array(ys)
```

`rk4(rhs, y0, h, steps, stop)` solves $dy/dx = $ `rhs(x, y)` from $x = 0$, $y = y_0$ with at most `steps` steps of size `h`. `xs` and `ys` are lists of the times and the states; `np.array(y0, dtype=float)` turns the starting values into an array of floating-point numbers, so that the arithmetic below works on whole arrays. Each step computes the four slopes $k_1$ to $k_4$ and the new state $y + \tfrac h6(k_1 + 2k_2 + 2k_3 + k_4)$ (Section 12.21; Chapter 2). If a function `stop` is given and returns True for the old and the new state, `break` ends the loop before the new state is stored. The time is stored as $(n + 1)h$ rather than by adding $h$ again and again, which would add up rounding errors. The function returns the times and the states as arrays (one row per time).

```python
x_test, y_test = rk4(lambda x, y: -y, [1.0], 0.05, 20)
error_test = abs(y_test[-1, 0] - math.exp(-1.0))
say(f"y' = -y: RK4 with h = 0.05 gives y(1) = {y_test[-1, 0]:.10f}; "
    f"exact {math.exp(-1.0):.10f}")
check(error_test < 1e-7, "RK4 solves y' = -y to better than 1e-7 with 20 steps")
```

A test: $y' = -y$ with $y(0) = 1$ and 20 steps of $h = 0.05$ (the `lambda` makes a small nameless function). `y_test[-1, 0]` is the first number of the last row. The cell prints (Out [4]) `y(1) = 0.3678794611; exact 0.3678794412`: the error is $2\times10^{-8}$, and the check requires less than $10^{-7}$.

**In [5], the system for $a_4$ and $b_4$.** The cell defines three functions and prints nothing.

```python
def history(p3, p0, start, h, steps, couplings=EINSTEIN, Lam=0.0, stop=None):
    def rhs(x, y):
        a4, rate, log_b4, u, kappa_rho = y
        k = math.exp(2.0 * a4 - log_b4)  # k = e^(2 a4)/b4
        jacobian = np.array([
            [J11(rate, u, k, *couplings), J12(rate, u, k, *couplings)],
            [J21(rate, u, k, *couplings), J22(rate, u, k, *couplings)]])
        pressure3, pressure0 = p3(x, y), p0(x, y)
        right = np.array([pressure3 - Lam - rest1(rate, u, k, *couplings),
                          pressure0 - Lam - rest0(rate, u, k, *couplings)])
        second, v = np.linalg.solve(jacobian, right)  # a4'' and v = u'
        h4 = u / 2.0 - rate
        change = (-3.0 * rate * (kappa_rho + pressure3)
                  - 4.0 * h4 * (kappa_rho + pressure0))  # the conservation law
        return np.array([rate, second, u, v, change])
```

`history(p3, p0, start, h, steps, couplings, Lam, stop)` integrates the system for two pressure functions `p3(x, y)` and `p0(x, y)` (which give $\kappa p_3$ and $\kappa p_0$ and may depend on the time and the state). Inside it, `rhs` is the right-hand side: it unpacks the state into $a_4$, $a_4'$ (`rate`), $\ln b_4$, $u$ and $\kappa\rho$; computes $k = e^{2a_4 - \ln b_4}$; fills the 2 by 2 Jacobian; computes the two right-hand sides $\kappa p_3 - \Lambda - R_1$ and $\kappa p_0 - \Lambda - R_0$; solves the linear system with `np.linalg.solve` for $a_4''$ (`second`) and $v$; and computes the change of $\kappa\rho$ from the energy exchange. It returns the five derivatives $(a_4', a_4'', u, v, d(\kappa\rho)/dx_4)$ in the order of the state.

```python
    a4, rate, log_b4, u = start
    kappa_rho0 = -(e44(rate, u, math.exp(2.0 * a4 - log_b4), *couplings) + Lam)
    return rk4(rhs, [a4, rate, log_b4, u, kappa_rho0], h, steps, stop)
```

The rest of `history` (indented under its `def`): it unpacks the four starting values, computes $\kappa\rho(0) = -(e_{44} + \Lambda)$ from the constraint, and calls `rk4` with the five starting numbers.

```python
def constraint_gap(ys, couplings=EINSTEIN, Lam=0.0):
    k = np.exp(2.0 * ys[:, 0] - ys[:, 2])
    return float(np.max(np.abs(ys[:, 4] + e44(ys[:, 1], ys[:, 3], k, *couplings) + Lam)))
```

`constraint_gap` evaluates, at every stored time of a solution, the carried $\kappa\rho$ plus $e_{44} + \Lambda$ (which should be zero), and returns the largest absolute value. `ys[:, 0]` is the column of all $a_4$ values, and so on.

```python
def no_pressure(x, y):
    return 0.0  # a vacuum: p3 = p0 = 0
```

`no_pressure` returns 0 for every time and state: the pressure function of a vacuum.

**In [6], the flat member.**

```python
x_flat, y_flat = history(no_pressure, no_pressure, (0.0, 0.0, 0.0, 2.0), 0.01, 300)
error_log_b4 = np.max(np.abs(y_flat[:, 2] - 2.0 * np.log(1.0 + x_flat)))
error_u = np.max(np.abs(y_flat[:, 3] - 2.0 / (1.0 + x_flat)))
say(f"largest error: ln b4 {error_log_b4:.0e}, u {error_u:.0e}, a4 "
    f"{np.max(np.abs(y_flat[:, 0])):.0e}")
reproduces(error_log_b4 < 1e-8 and error_u < 1e-8
           and np.max(np.abs(y_flat[:, 0])) < 1e-8 and np.max(np.abs(y_flat[:, 4])) == 0,
           "the flat member a4 = 0, b4 = (1 + x4)^2 solves the vacuum equations",
           PY, "einstein_flat_vacuum")
check(constraint_gap(y_flat) < 1e-8, "flat member: the constraint holds along x4")
```

The vacuum is integrated in Einstein gravity from $(a_4, a_4', \ln b_4, u) = (0, 0, 0, 2)$ with 300 steps of $h = 0.01$, up to $x_4 = 3$. The errors of $\ln b_4$ and $u$ against the exact $2\ln(1 + x_4)$ and $2/(1 + x_4)$, and the largest $|a_4|$, are printed with one significant digit (`.0e`): Out [6] shows `ln b4 4e-10, u 9e-10, a4 1e-10`. The check requires all three below $10^{-8}$ and the carried energy density to stay exactly zero (with no pressure and $\kappa\rho = 0$ at the start, its rate is exactly zero); it reproduces the sympy report's `einstein_flat_vacuum`. The last check: the constraint gap stays below $10^{-8}$.

**In [7], figure 12c.1: the flat member.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
every = slice(0, None, 20)  # every 20th point for the numerical markers
left.plot(x_flat, 1.0 + x_flat, color="black", label="exact $1 + x_4$")
left.plot(x_flat[every], np.exp(y_flat[every, 2] / 2.0), "o", markersize=4,
          label="RK4: $b_4^{1/2}$")
left.plot(x_flat, np.exp(y_flat[:, 0]), "--", label="3-space $e^{a_4} = 1$")
```

Two panels. `slice(0, None, 20)` selects every 20th point, for markers that do not crowd. Left: the exact $1 + x_4$ as a black line, the numerical $b_4^{1/2} = e^{\ln b_4/2}$ as dots, and the 3-space factor $e^{a_4}$ dashed.

```python
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("scale factor")
left.set_title("the block grows linearly, 3-space is still")
left.legend(fontsize=8)
right.plot(x_flat, 2.0 / (1.0 + x_flat), color="black", label="exact $2/(1 + x_4)$")
right.plot(x_flat[every], y_flat[every, 3], "o", markersize=4, label="RK4: $u$")
```

Labels, title and legend of the left panel; on the right the exact rate $2/(1 + x_4)$ and the numerical $u$ as dots.

```python
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("$u = b_4'/b_4$ (units $H$)")
right.set_title("the rate $u$")
right.legend(fontsize=8)
save_figure(fig, "flat_member",
            "Einstein gravity without a source: the flat member $a_4 = 0$, "
...)
```

Labels, title and legend of the right panel, and `save_figure` (the caption is printed under figure 12c.1 in Section 12.24). The dots lie on the lines: the block grows linearly ($e^{-a_4}b_4^{1/2} = 1 + x_4$) while 3-space stays still.

**In [8], the record history with its own source.**

```python
def einstein_p3(x, y):
    return 6.0 * math.exp(2.0 * x / 3.0) - 13.0 / 9.0  # kappa p3, Lambda = 0
```

`einstein_p3` returns the Einstein pressure $\kappa p_3 = 6e^{2x_4/3} - \tfrac{13}9$ of the record history ($\Lambda = 0$), a function of the time only (the argument `y` is not used).

```python
def einstein_p0(x, y):
    return 3.0 * math.exp(2.0 * x / 3.0) - 11.0 / 3.0  # kappa p0 = kappa p_t
```

`einstein_p0` returns $\kappa p_0 = \kappa p_t = 3e^{2x_4/3} - \tfrac{11}3$.

```python
AUTHOR_LAMBDA = -10.0  # the record's Lambda for the author's weights
```

The record's $\Lambda$ for the author's weights.

```python
def author_p3(x, y):
    k = math.exp(2.0 * x / 3.0)
    return -9.0 / 16.0 * k ** 2 + 1601.0 / 216.0 * k - 5359.0 / 3888.0 + AUTHOR_LAMBDA
```

`author_p3` returns the author's-weights pressure: the record's $\kappa p_3 - \Lambda$ plus $\Lambda = -10$.

```python
def author_p0(x, y):
    k = math.exp(2.0 * x / 3.0)
    return 79.0 / 16.0 * k - 497.0 / 144.0 + AUTHOR_LAMBDA
```

`author_p0` returns $\kappa p_0 - \Lambda = \tfrac{79}{16}k - \tfrac{497}{144}$ plus $\Lambda$.

```python
START = (0.0, 1.0, 0.0, 4.0 / 3.0)  # a4, a4', ln b4, u of the record history
record_runs = {"Einstein": history(einstein_p3, einstein_p0, START, 0.01, 300),
               "author's weights": history(author_p3, author_p0, START, 0.01, 300,
                                           AUTHOR, AUTHOR_LAMBDA)}
gaps = []
for name, (xs, ys) in record_runs.items():
    couplings, Lam = (EINSTEIN, 0.0) if name == "Einstein" else (AUTHOR, AUTHOR_LAMBDA)
    error_a4 = np.max(np.abs(ys[:, 0] - xs))  # exact a4 = x4
    error_log_b4 = np.max(np.abs(ys[:, 2] - 4.0 * xs / 3.0))  # exact ln b4 = 4 x4/3
    gaps.append(constraint_gap(ys, couplings, Lam))
    say(f"{name}: largest error a4 {error_a4:.0e}, ln b4 {error_log_b4:.0e}; "
        f"constraint gap {gaps[-1]:.0e}")
    check(error_a4 < 1e-9 and error_log_b4 < 1e-9,
          f"{name}: the solver reproduces the record history")
```

`START` holds the starting values of the record history. `record_runs` is a dictionary of the two integrations (Einstein gravity, and the author's weights with their $\Lambda$), each 300 steps of $h = 0.01$. For each run the loop picks the matching couplings and $\Lambda$ (a conditional expression), measures the largest deviation of $a_4$ from the exact $x_4$ and of $\ln b_4$ from $\tfrac43x_4$, and the constraint gap, prints them and checks that the solver stays on the history to better than $10^{-9}$. Out [8]: errors of $10^{-14}$, and gaps of $5\times10^{-9}$ (Einstein) and $7\times10^{-9}$ (the author's weights).

```python
reproduces(max(gaps) < 1e-8,
           "the energy density from conservation equals the constraint along x4",
           WL, "constraint_propagation_bianchi")
```

Both gaps below $10^{-8}$: the energy density carried by the conservation law equals the one the constraint gives, as the Bianchi identity requires (Wolfram report, `constraint_propagation_bianchi`).

**In [9], figure 12c.2: the record history recovered.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
xs = record_runs["Einstein"][0]
left.plot(xs, xs, color="black", label="exact $a_4 = x_4$")
left.plot(xs, 4.0 * xs / 3.0, color="grey", label="exact $\\ln b_4 = 4x_4/3$")
for (name, (x_run, y_run)), marker in zip(record_runs.items(), ("o", "s")):
    left.plot(x_run[every], y_run[every, 0], marker, markersize=4, fillstyle="none",
              label=f"$a_4$, {name}")
    left.plot(x_run[every], y_run[every, 2], marker, markersize=4,
              label=f"$\\ln b_4$, {name}")
```

Two panels. Left: the exact lines $a_4 = x_4$ (black) and $\ln b_4 = \tfrac43x_4$ (grey); for each run every 20th numerical value of $a_4$ (open markers, `fillstyle="none"`) and of $\ln b_4$ (filled markers), circles for Einstein gravity and squares for the author's weights (`zip` pairs each run with its marker).

```python
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("$a_4$ and $\\ln b_4$")
left.set_title("RK4 reproduces the record history")
left.legend(fontsize=7)
x_run, y_run = record_runs["author's weights"]
right.semilogy(x_run, np.exp(y_run[:, 0]), label="3-space $e^{a_4}$ (inflates)")
```

Labels, title and legend of the left panel. Right, for the author's weights: `semilogy` draws on a logarithmic vertical axis, on which an exponential is a straight line; first the 3-space factor $e^{a_4}$.

```python
right.semilogy(x_run, np.exp(-y_run[:, 0] + y_run[:, 2] / 2.0), "--",
               label="block $e^{-a_4}b_4^{1/2}$ (deflates)")
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("scale factor")
right.set_title("the scale factors (author's weights)")
right.legend(fontsize=8)
```

Then the block factor $e^{-a_4}b_4^{1/2} = e^{-a_4 + \ln b_4/2}$, dashed; labels, title, legend.

```python
save_figure(fig, "record_history",
            "The record history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ integrated with "
...)
```

`save_figure` (caption under figure 12c.2). The 3-space factor rises as $e^{x_4}$, the block factor falls as $e^{-x_4/3}$.

**In [10], the same source, other starting rates.**

```python
perturbed = {}  # (theory, starting rate) -> (x4, solution)
for name, (p3, p0, couplings, Lam) in {
        "Einstein": (einstein_p3, einstein_p0, EINSTEIN, 0.0),
        "author's weights": (author_p3, author_p0, AUTHOR, AUTHOR_LAMBDA)}.items():
    for rate0 in (1.05, 0.95):
        xs, ys = history(p3, p0, (0.0, rate0, 0.0, 4.0 / 3.0), 0.01, 300, couplings, Lam)
        perturbed[(name, rate0)] = (xs, ys)
        check(constraint_gap(ys, couplings, Lam) < 1e-7,
              f"{name}, a4'(0) = {rate0}: the constraint holds along the solution")
        say(f"{name}, a4'(0) = {rate0}: at x4 = 3, a4' - 1 = {ys[-1, 1] - 1:+.4f}, "
            f"u - 4/3 = {ys[-1, 3] - 4 / 3:+.4f}")
```

The outer loop runs over a dictionary of the two theories, each with its pressure functions, couplings and $\Lambda$ (`.items()` gives the name and the tuple, which is unpacked in the `for` line); the inner loop over the starting rates 1.05 and 0.95, with $u(0) = \tfrac43$ and $b_4(0) = 1$. Each solution is stored under the pair (theory, rate); the constraint gap must stay below $10^{-7}$; and the differences $a_4' - 1$ and $u - \tfrac43$ at $x_4 = 3$ are printed with a sign (`+.4f`). Out [10]: in Einstein gravity $-0.0313$ and $+0.0419$ for 1.05, $+0.0342$ and $-0.0445$ for 0.95; with the author's weights $+0.0357$ and $+0.0727$, $-0.0417$ and $-0.0858$. The differences do not die out.

**In [11], figure 12c.3: the differences from the record history.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
for ax, name in ((left, "Einstein"), (right, "author's weights")):
    for rate0, colour in ((1.05, "tab:blue"), (0.95, "tab:orange")):
        xs, ys = perturbed[(name, rate0)]
        ax.plot(xs, ys[:, 1] - 1.0, color=colour,
                label=f"$a_4' - 1$, $a_4'(0) = {rate0}$")
        ax.plot(xs, ys[:, 3] - 4.0 / 3.0, "--", color=colour,
                label=f"$u - 4/3$, $a_4'(0) = {rate0}$")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("time $x_4$ (units $1/H$)")
    ax.set_ylabel("difference from the record history (units $H$)")
    ax.set_title(name)
    ax.legend(fontsize=7)
```

Two panels, Einstein gravity on the left and the author's weights on the right; in each, for the two starting rates (blue and orange), the difference $a_4' - 1$ as a solid line and $u - \tfrac43$ dashed, a line at zero, labels, the title (the theory's name) and the legend.

```python
save_figure(fig, "starting_rate",
            "The source of the record history used with other starting rates: the "
...)
```

`save_figure` (caption under figure 12c.3): the source does not select the history; the starting values do.

**In [12], a pulse in the rate: from the history to the source and back.**

```python
X_C, WIDTH = 3.0, 0.5  # the centre and the width of the pulse
einstein_side = {key: sp.lambdify((ad1, ad2, uu, vv, kk),
                                  side[key].subs({a1: 1, a2: 0, a3: 0}), "numpy")
                 for key in ("x4x4", "x1x1", "x0x0")}
```

The centre $x_c = 3$ and the width $0.5$ of the pulse. `einstein_side` holds the three Einstein components ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$) as numpy functions of $(a_4', a_4'', u, v, k)$, now with the second derivatives, because the source of a chosen history needs them.

```python
def pulse_history(x):
    t, t0 = (x - X_C) / WIDTH, -X_C / WIDTH  # the argument now and at x4 = 0
```

`pulse_history(x)` returns the exact $a_4$, $a_4'$ and $a_4''$ of the pulse history at the time $x$. `t` is the argument $(x - x_c)/w$ of the error function now, and `t0` its value at $x_4 = 0$.

```python
    def antiderivative(s):  # an antiderivative of erf
        return s * math.erf(s) + math.exp(-s * s) / math.sqrt(math.pi)
```

Inside `pulse_history`, a small function: an antiderivative of erf, $F(s) = s\,\mathrm{erf}(s) + e^{-s^2}/\sqrt\pi$ (its derivative is $\mathrm{erf}(s) + s\cdot\tfrac2{\sqrt\pi}e^{-s^2} - \tfrac{2s}{\sqrt\pi}e^{-s^2} = \mathrm{erf}(s)$, by the product rule and $\mathrm{erf}'(s) = \tfrac2{\sqrt\pi}e^{-s^2}$).

```python
    rate = 1.0 + 0.5 * (math.erf(t) + math.erf(X_C / WIDTH))
    second = math.exp(-t * t) / (WIDTH * math.sqrt(math.pi))  # the derivative
    a4 = x + 0.5 * (WIDTH * (antiderivative(t) - antiderivative(t0))
                    + x * math.erf(X_C / WIDTH))
    return a4, rate, second
```

The rate $a_4' = 1 + \tfrac12(\mathrm{erf}\,t + \mathrm{erf}(x_c/w))$; its derivative $a_4'' = \tfrac12\cdot\tfrac2{\sqrt\pi}e^{-t^2}\cdot\tfrac1w = e^{-t^2}/(w\sqrt\pi)$ (chain rule); and $a_4$ itself, the integral of the rate from 0: $x + \tfrac12\big(w(F(t) - F(t_0)) + x\,\mathrm{erf}(x_c/w)\big)$, because $\int\mathrm{erf}((x - x_c)/w)\,dx = w\,F((x - x_c)/w)$.

```python
def pulse_source(x):
    a4, rate, second = pulse_history(x)
    values = (rate, second, 4.0 * rate / 3.0, 4.0 * second / 3.0,
              math.exp(2.0 * a4 / 3.0))
    return (-einstein_side["x4x4"](*values), einstein_side["x1x1"](*values),
            einstein_side["x0x0"](*values))
```

`pulse_source(x)` returns the Einstein source of the pulse history at the time $x$: with $b_4 = e^{(4/3)a_4}$ we have $u = \tfrac43a_4'$, $v = \tfrac43a_4''$ and $k = e^{2a_4}/b_4 = e^{(2/3)a_4}$; then $\kappa\rho = -e_{44}$, $\kappa p_3 = e_{11}$ and $\kappa p_0 = e_{00}$ ($\Lambda = 0$).

```python
x_pulse, y_pulse = history(lambda x, y: pulse_source(x)[1],
                           lambda x, y: pulse_source(x)[2],
                           (0.0, 1.0, 0.0, 4.0 / 3.0), 0.01, 800)
exact = np.array([pulse_history(x) for x in x_pulse])  # columns: a4, a4', a4''
needed_rho = np.array([pulse_source(x)[0] for x in x_pulse])
error_a4 = np.max(np.abs(y_pulse[:, 0] - exact[:, 0]))
```

The integration: the pressures are the second and third entries of `pulse_source` (two `lambda` functions of the time), the starting values those of the record history, 800 steps of $h = 0.01$ up to $x_4 = 8$. `exact` holds the exact $a_4$, $a_4'$, $a_4''$ at every stored time, and `needed_rho` the energy density the history needs; `error_a4` is the largest deviation of $a_4$.

```python
error_rate = np.max(np.abs(y_pulse[:, 1] - exact[:, 1]))
error_rho = np.max(np.abs(y_pulse[:, 4] - needed_rho) / np.abs(needed_rho))
say(f"largest error: a4 {error_a4:.0e}, a4' {error_rate:.0e}, ln b4 "
    f"{np.max(np.abs(y_pulse[:, 2] - 4.0 * exact[:, 0] / 3.0)):.0e}; relative error "
    f"of kappa rho {error_rho:.0e}")
check(error_a4 < 1e-8 and error_rate < 1e-6 and error_rho < 1e-8,
      "pulse: RK4 (h = 0.01) gets the history back from its source")
```

The deviations of $a_4'$ and the relative deviation of the carried $\kappa\rho$ are computed, and all errors printed (Out [12]): `a4 1e-09, a4' 4e-08, ln b4 3e-09; relative error of kappa rho 4e-09`. The check: the solver returns the chosen history.

```python
report("rate a4'/H after the pulse (x4 = 8)", f"{y_pulse[-1, 1]:.8f}")
check(abs(y_pulse[-1, 1] - 2.0) < 1e-6 and np.min(y_pulse[:, 1]) > 1.0 - 1e-6,
      "after the pulse a4' = 2 H; the rate never falls below H")
```

The rate at $x_4 = 8$ is printed, `1.99999999`, and checked to be $2H$ to $10^{-6}$, with the rate never below $H$.

**In [13], figure 12c.4: the pulse history.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
marks = slice(0, None, 40)  # every 40th point for the exact markers
left.plot(x_pulse, y_pulse[:, 1], label="RK4: $a_4'$")
left.plot(x_pulse, y_pulse[:, 3], label="RK4: $u$")
left.plot(x_pulse[marks], exact[marks, 1], "o", color="black", markersize=3,
          label="exact")
```

Two panels; every 40th point for the exact markers. Left: the numerical $a_4'$ and $u$ as lines and the exact $a_4'$ as black dots.

```python
left.plot(x_pulse[marks], 4.0 * exact[marks, 1] / 3.0, "o", color="black",
          markersize=3)
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("rate (units $H$)")
left.set_title("the rates rise in the pulse")
left.legend(fontsize=8)
```

The exact $u = \tfrac43a_4'$ as black dots; labels, title, legend.

```python
right.semilogy(x_pulse, np.exp(y_pulse[:, 0]), label="3-space $e^{a_4}$")
right.semilogy(x_pulse, np.exp(-y_pulse[:, 0] + y_pulse[:, 2] / 2.0), "--",
               label="block $e^{-a_4}b_4^{1/2}$")
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("scale factor")
right.set_title("the scale factors")
```

Right, on a logarithmic axis: the 3-space factor $e^{a_4}$ and the block factor $e^{-a_4}b_4^{1/2} = e^{-a_4/3}$; labels and title.

```python
right.legend(fontsize=8)
save_figure(fig, "pulse_history",
            "A history whose rate rises in a pulse, recovered by RK4 (step "
...)
```

The legend and `save_figure` (caption under figure 12c.4). The rates rise from 1 and $\tfrac43$ to 2 and $\tfrac83$ around $x_4 = 3$; the block deflates at every time, twice as fast after the pulse.

**In [14], figure 12c.5: the source of the pulse history.**

```python
sources = np.array([pulse_source(x) for x in x_pulse])  # kappa rho, p3, p0
k_pulse = np.exp(2.0 * exact[:, 0] / 3.0)
scaled = sources / k_pulse[:, None]
say("kappa (rho, p3, p0)/k at x4 = 0: " + ", ".join(f"{v:.4f}" for v in scaled[0])
    + "; at x4 = 8: " + ", ".join(f"{v:.4f}" for v in scaled[-1]))
k0, k8 = k_pulse[0], k_pulse[-1]
```

`sources` holds the three components at every stored time; `k_pulse` the values of $k = e^{(2/3)a_4}$; `scaled` the components divided by $k$ (`k_pulse[:, None]` makes a column, so that each row is divided by its own $k$). The cell prints the scaled values at the two ends (Out [14]): `-6.3333, 4.5556, -0.6667` at $x_4 = 0$ (where $k = 1$: $-6 - \tfrac13$, $6 - \tfrac{13}9$, $3 - \tfrac{11}3$) and `-6.0002, 5.9990, 2.9975` at $x_4 = 8$.

```python
before = np.array([-6 * k0 - 1 / 3, 6 * k0 - 13 / 9, 3 * k0 - 11 / 3])  # A = 1
after = np.array([-6 * k8 - 4 / 3, 6 * k8 - 52 / 9, 3 * k8 - 44 / 3])  # A = 2
check(np.allclose(sources[0], before, rtol=1e-12, atol=1e-12)
      and np.allclose(sources[-1], after, rtol=1e-9, atol=0.0),
      "before the pulse the source of A = 1, after it the source of A = 2")
fig, ax = plt.subplots()
```

`before` is the Einstein source of the exponential history with $A = 1$ at the first $k$, `after` that with $A = 2$ at the last $k$ (Section 12.21); the check compares them with the computed source to $10^{-12}$ and $10^{-9}$. Then a new figure.

```python
for column, style, label in ((0, "-", "$\\kappa\\rho/k$"), (1, "--", "$\\kappa p_3/k$"),
                             (2, ":", "$\\kappa p_0/k = \\kappa p_t/k$")):
    ax.plot(x_pulse, scaled[:, column], style, label=label)
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("time $x_4$ (units $1/H$)")
ax.set_ylabel("required source divided by $k$ (units $H^2$)")
```

The three scaled components against the time with three line styles, a line at zero, the labels.

```python
ax.set_title("The Einstein source of the pulse history")
ax.legend(fontsize=8)
save_figure(fig, "pulse_source",
            "The source that the pulse history needs in Einstein gravity with "
...)
```

Title, legend and `save_figure` (caption under figure 12c.5). Divided by $k$, the components approach $-6$, $6$ and $3$ as $k$ grows; during the pulse the 3-space and the block pressures move apart.

**In [15], figure 12c.6: the convergence order of RK4.**

```python
steps_list = [15, 30, 60, 120, 240]  # h = 3/steps = 0.2, 0.1, 0.05, 0.025, 0.0125
sizes, errors = [], []
for steps in steps_list:
    xs, ys = history(no_pressure, no_pressure, (0.0, 0.0, 0.0, 2.0), 3.0 / steps, steps)
    sizes.append(3.0 / steps)
    errors.append(abs(ys[-1, 2] - 2.0 * math.log(4.0)))
```

Five integrations of the flat member up to $x_4 = 3$ with 15, 30, 60, 120 and 240 steps ($h = 0.2$ down to $0.0125$); for each the step size and the error of $\ln b_4(3)$ against $2\ln 4$ are stored.

```python
orders = [math.log2(errors[i] / errors[i + 1]) for i in range(len(errors) - 1)]
for i, (size, error) in enumerate(zip(sizes, errors)):
    order = f"{orders[i - 1]:.2f}" if i > 0 else "-"
    say(f"h = {size:<7} error of ln b4(3) = {error:.2e}   measured order {order}")
check(all(3.7 < q < 4.5 for q in orders),
      "RK4 converges with order 4 (measured orders between 3.7 and 4.5)")
```

The measured order between two neighbouring step sizes is $\log_2$ of the ratio of their errors (halving $h$ divides an error $Ch^q$ by $2^q$). The table is printed (Out [15]), one line per step size with its error and the order measured from the previous one (`f"{size:<7}"` pads the number to seven characters on the left side): errors $2.24\times10^{-5}$, $1.09\times10^{-6}$, $6.05\times10^{-8}$, $3.57\times10^{-9}$, $2.17\times10^{-10}$ and orders 4.36, 4.17, 4.08, 4.04. The check requires every order between 3.7 and 4.5.

```python
fig, ax = plt.subplots()
ax.loglog(sizes, errors, "o-", label="error of $\\ln b_4(3)$")
reference = errors[-1] * (np.array(sizes) / sizes[-1]) ** 4
ax.loglog(sizes, reference, "--", color="black", label="slope 4: $C h^4$")
ax.set_xticks(sizes)  # one tick at each step size used
ax.set_xticklabels([f"{size:g}" for size in sizes])
```

A figure on logarithmic axes (`loglog`): the errors against the step sizes, and the reference line $Ch^4$ through the last point, $C h^4 = e_{\text{last}}(h/h_{\text{last}})^4$. One tick at each step size used, labelled with the shortest form of the number (`:g`).

```python
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())  # no extra labels
ax.set_xlabel("step size $h$ (units $1/H$)")
ax.set_ylabel("absolute error")
ax.set_title("RK4 on the flat member: fourth-order convergence")
ax.legend(fontsize=8)
save_figure(fig, "rk4_convergence",
            "The error of the RK4 value of $\\ln b_4$ at $x_4 = 3/H$ for the flat "
...)
```

`NullFormatter` removes the labels of the small ticks between the main ones; labels, title, legend and `save_figure` (caption under figure 12c.6). The points follow the line of slope 4.

**In [16], the gas of massless particles with the author's weights.**

```python
import re  # regular expressions: find numbers in a text
```

`re` for reading numbers out of a detail text of the record.

```python
def determinant(rate, u, k, couplings):
    return (J11(rate, u, k, *couplings) * J22(rate, u, k, *couplings)
            - J12(rate, u, k, *couplings) * J21(rate, u, k, *couplings))
```

`determinant` is $\det J = J_{11}J_{22} - J_{12}J_{21}$ for given rates, $k$ and couplings.

```python
sigma0 = -(e44(1.0, 4.0 / 3.0, 1.0, *AUTHOR) + AUTHOR_LAMBDA)  # kappa rho(0)
report("kappa sigma0 from the constraint", f"{sigma0:.6g}")
```

`sigma0` is $\kappa\sigma_0 = -(e_{44} + \Lambda)$ at the start of the record history with the author's weights, printed with six significant digits: `3.57407` (Section 12.21).

```python
def gas_p3(x, y):
    return sigma0 * math.exp(-2.0 * y[2]) / 3.0  # kappa p3 = kappa rho/3
```

`gas_p3` returns the pressure of the gas, $\kappa p_3 = \tfrac13\kappa\sigma_0b_4^{-2} = \tfrac13\kappa\sigma_0e^{-2\ln b_4}$, computed from the state (`y[2]` is $\ln b_4$); the hidden pressure is `no_pressure`.

```python
def sign_change(old, new):
    dets = [determinant(s[1], s[3], math.exp(2.0 * s[0] - s[2]), AUTHOR)
            for s in (old, new)]
    return dets[0] * dets[1] <= 0.0
```

`sign_change` evaluates $\det J$ at the old and the new state (`s[1]` is $a_4'$, `s[3]` is $u$, and $k = e^{2a_4 - \ln b_4}$) and returns True when the product is not positive: the determinant has changed sign or reached zero within the step.

```python
x_gas, y_gas = history(gas_p3, no_pressure, START, 2e-5, 30000, AUTHOR, AUTHOR_LAMBDA,
                       stop=sign_change)
end = y_gas[-1]
say(f"det J changes sign after x4 = {x_gas[-1]:.6f}: a4 = {end[0]:.6f}, "
    f"b4 = {math.exp(end[2]):.6f}, a4' = {end[1]:.4f}, u = {end[3]:.4f}")
check(np.max(np.abs(y_gas[:, 4] - sigma0 * np.exp(-2.0 * y_gas[:, 2]))
             / (sigma0 * np.exp(-2.0 * y_gas[:, 2]))) < 1e-10,
      "the gas conserves its energy: kappa rho = kappa sigma0 b4^(-2) along x4")
```

The integration with the author's weights from the record history, with steps of $h = 2\times10^{-5}$ (at most 30000 of them, up to $x_4 = 0.6$), stopped by `sign_change`. `end` is the last stored state; the cell prints (Out [16]) `det J changes sign after x4 = 0.428800: a4 = 0.361560, b4 = 0.862655, a4' = 0.9693, u = -2.6032`. The check: the carried energy density equals $\kappa\sigma_0b_4^{-2}$ to $10^{-10}$ at every step, so the gas conserves its energy as derived in Section 12.21.

```python
text = [entry["detail"] for entry in read_json(KS_A4)["checks"]
        if entry["name"] == "D2_author_weights_from_the_record_history"][0]
numbers = re.search(r"singular_second_order_system at x4 = (\S+) \(a4 = (\S+?), "
                    r"b4 = (\S+?), a4'/H = (\S+?), u/H = (\S+?)\)", text)
recorded = [float(value) for value in numbers.groups()]
say("record: x4 = {}, a4 = {}, b4 = {}, a4' = {}, u = {}".format(*numbers.groups()))
```

The detail of the record's check `D2_author_weights_from_the_record_history` is found (a list comprehension with a condition, and `[0]` takes its first element). `re.search` looks for the sentence of the record that starts with the outcome `singular_second_order_system` and gives, in parentheses, the time, $a_4$, $b_4$ and the two rates; each pair of parentheses of the pattern captures one of the five numbers, while the escaped parentheses (with a backslash) stand for the parenthesis characters of the sentence itself. They are printed: `x4 = 0.428813, a4 = 0.361572, b4 = 0.862627, a4' = 0.978369, u = -2.60176`.

```python
reproduces(f"{sigma0:.6g}" in text and abs(x_gas[-1] - recorded[0]) < 1e-3
           and abs(end[0] - recorded[1]) < 1e-3
           and abs(math.exp(end[2]) - recorded[2]) < 1e-3
           and abs(end[1] - recorded[3]) < 0.05 and abs(end[3] - recorded[4]) < 0.05,
           "the system becomes singular where the record finds it",
           KS_A4, "D2_author_weights_from_the_record_history")
```

The check: the record's detail contains the same $\kappa\sigma_0$ with six digits; the time, $a_4$ and $b_4$ agree to $10^{-3}$; the rates, which change fast near the singular point, to 0.05. It reproduces the record's check `D2_author_weights_from_the_record_history`.

**In [17], figure 12c.7: the breakdown.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
left.plot(x_gas, y_gas[:, 1], label="$a_4'$ with the gas")
left.plot(x_gas, y_gas[:, 3], "--", label="$u$ with the gas")
left.axhline(1.0, color="black", linestyle=":", linewidth=0.8,
             label="record history: $a_4' = 1$, $u = 4/3$")
left.axhline(4.0 / 3.0, color="black", linestyle=":", linewidth=0.8)
```

Two panels. Left: the rates $a_4'$ and $u$ with the gas, and dotted lines at the record values 1 and $\tfrac43$ (one legend entry for both).

```python
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("rate (units $H$)")
left.set_title("the rates leave the record history")
left.legend(fontsize=8)
k_gas = np.exp(2.0 * y_gas[:, 0] - y_gas[:, 2])
right.plot(x_gas, determinant(y_gas[:, 1], y_gas[:, 3], k_gas, AUTHOR))
```

Labels, title and legend of the left panel. Right: $\det J$ along the solution, computed at every stored state at once (the functions of In [2] accept arrays).

```python
right.axhline(0.0, color="black", linewidth=0.8)
right.axvline(x_gas[-1], color="grey", linestyle="--", linewidth=0.8)
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("$\\det J$")
right.set_title("the Jacobian reaches zero")
save_figure(fig, "gas_breakdown",
            "The author's weights ($\\Lambda = -10$) with a gas of massless particles "
...)
```

A line at zero, a dashed line at the last time, labels, title and `save_figure` (caption under figure 12c.7). The rate $u$ falls and turns negative, and $\det J$ falls to zero at $x_4 = 0.4288$.

**In [18], the record on the Kohn-Sham states.**

```python
import csv  # reads tables of comma-separated values
```

`csv`, Python's module for tables of comma-separated values.

```python
ks = read_json(KS)
detail = {entry["name"]: entry["detail"] for entry in ks["checks"]}
verdicts = [entry["verdict"] for entry in ks["checks"]]
say(f"{KS}: {verdicts.count('PASS')} of {len(verdicts)} checks PASS")
check(len(verdicts) > 0 and verdicts.count("PASS") == len(verdicts)
      == ks["summary"]["checks"],
      "record: no Kohn-Sham state is an admissible source (every check PASS)")
```

The record of the source conditions is read; `detail` maps each check's name to its detail text. The count of PASS verdicts is printed (Out [18]: 5 of 5), and the check requires every check to have passed and the count to equal the record's summary.

```python
TABLE = "Revision/kohn_sham/results/ground/emt-integrals.csv"
with repository_file(TABLE).open(encoding="utf-8", newline="") as handle:
    table = {row["id"]: row for row in csv.DictReader(handle)}
INTEGRALS = ("int_rho", "int_p3", "int_p_t", "int_p0")
zero = sorted(name for name, row in table.items()
              if all(float(row[column]) == 0.0 for column in INTEGRALS))
```

The table `emt-integrals.csv` of the Kohn-Sham record holds one row per recorded ground state: its name in the column `id` (for example `N592_lam0_a10`: $N = 592$ particles, coupling $\lambda = 0$, slice $a_{4,0} = 1$), the slice in the column `a4`, and the integrals over the hidden direction of the energy density and of the three pressures. `csv.DictReader` reads each row as a dictionary from the column names to the texts; `table` maps each state's name to its row. `zero` is the sorted list of the states whose four integrals are all zero.

```python
nonzero = [name for name in table if name not in zero]
report("Kohn-Sham states in the table, with a nonzero tensor",
       f"{len(table)}, {len(nonzero)}")
counted = re.search(r"(\d+) ground-state profiles .*?\((\d+) with a nonzero",
                    detail["ks_profiles_depend_on_x0"])
listed = re.search(r"\(zero source\): (.*?) \(the",
                   detail["ks_zero_source_states_listed"]).group(1)
```

`nonzero` lists the other states; the counts are printed: `75, 70`. From the detail texts of two checks of the record, `re.search` reads the record's own counts (`\d+` is a run of digits, `.*?` any text, as short as possible) and the list of the states with a zero source.

```python
reproduces(counted is not None and counted.groups() == (str(len(table)),
                                                        str(len(nonzero)))
           and sorted(listed.split(", ")) == zero,
           f"{len(nonzero)} of the {len(table)} states have a nonzero tensor",
           KS, "ks_zero_source_states_listed")
kq = sp.symbols("kq", positive=True)
```

The check: the record's counts equal the table's, and the record's list of zero states equals the table's (record check `ks_zero_source_states_listed`). `kq` is $k$ as a positive symbol.

```python
shifted = record["exponentialHistory"]["authorWeights"]["historySource_kappaT_minus_Lam"]
need = {key: sp.sympify(shifted[key]["input"].replace("^", "**"), locals={"kk": kq})
        for key in ("minus_rho", "p3", "p0", "pt")}
kappa_rho = -(need["minus_rho"] + AUTHOR_LAMBDA)
distance = {}
for name in nonzero:
    row = table[name]
    if float(row["int_rho"]) == 0.0:
        continue
    k_value = math.exp(2.0 * float(row["a4"]) / 3.0)
    needed = [float(((need[key] + AUTHOR_LAMBDA) / kappa_rho).subs(kq, k_value))
              for key in ("p3", "p0", "pt")]
    mine = [float(row[column]) / float(row["int_rho"])
            for column in ("int_p3", "int_p0", "int_p_t")]
    distance[name] = max(abs(a - b) for a, b in zip(mine, needed))
```

`need` holds the record's source of the record history with the author's weights, $\kappa T - \Lambda$, as functions of $k$; `kappa_rho` is $\kappa\rho = -(-\kappa\rho - \Lambda) - \Lambda$. For every state with a nonzero energy density the loop computes $k = e^{2a_{4,0}/3}$ at its slice, the ratios $p_3/\rho$, $p_0/\rho$, $p_t/\rho$ that the history needs there ($\kappa$ cancels in each ratio), the state's own ratios (the ratios of the integrals: averages over the hidden direction per proper volume), and the largest difference between the two sets.

```python
closest = min(distance, key=distance.get)
report("smallest distance of the ratios, and its state",
       f"{distance[closest]:.6g}, {closest}")
reproduces(f"by at least {distance[closest]:.6g} (closest: {closest})"
           in detail["ks_history_is_a_prescribed_background"],
           "the ratios of every state differ from the needed ones, as recorded",
           KS, "ks_history_is_a_prescribed_background")
```

`min(distance, key=distance.get)` is the state with the smallest such difference; the cell prints `1.3733, N592_lamp2_a15`. The check requires the record's detail to contain exactly the sentence `by at least 1.3733 (closest: N592_lamp2_a15)` (record check `ks_history_is_a_prescribed_background`). Out [18] shows two RESULT lines and three PASS lines.

**In [19], the last check.**

```python
figure_names = ["flat_member", "record_history", "starting_rate", "pulse_history",
                "pulse_source", "rk4_convergence", "gas_breakdown"]
paths = [output_file(f"{FIGURE_FOLDER}/12c_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths), "all seven figure files exist")
all_checks_passed()
```

The seven figure files must exist; the last line is ALL 21 CHECKS PASSED (notebook 12c).

### 12.26 A condensate of dirac16complex00 as a source

The sources of Section 12.21 were chosen by hand. Can a field of the theory BE the source, exactly? We ask this for the simplest configurations of the commuting field dirac16complex00 (Chapter 7): those that depend on the time only.

**The field equation.** For a spinor field $\Phi$ (a column of 16 complex numbers at every point) the Euler-Lagrange equation of the record is $\gamma^\mu D_\mu\Phi = (m + U'(S))\Phi$, with $D_\mu = \partial_\mu + \Omega_\mu$, the curved-space gammas $\gamma^\mu = \gamma^{(\mu)}/E_\mu$ (no sum; $E_\mu$ the vielbein of Chapter 6), the density $S = \bar\Phi\Phi$, $\bar\Phi = \Phi^\dagger C$ and the potential $U(S)$; we write $M = m + U'(S)$, the **effective mass**. Chapter 6 derived the gravity term of the corrected metric (record `a4-equations.json`, key `fields/lemmas/gravityTerm`):

$$
\gamma^\mu\Omega_\mu = c\,\gamma^{(x_0)} + \big(u - \tfrac12a_4'\big)\gamma^{(x_4)},\qquad c = \tfrac32He^{a_4}b_4^{-1/2} .
$$

**The condensate equation.** A **homogeneous condensate** is a solution $\Phi(x_4)$ that depends on the time only. Then only the derivative along $x_4$ survives, and $\gamma^{x_4} = \gamma^{(x_4)}$ because $E_4 = 1$:

$$
\gamma^{(x_4)}\Phi' + c\,\gamma^{(x_0)}\Phi + \big(u - \tfrac12a_4'\big)\gamma^{(x_4)}\Phi = M\Phi
$$

(the field equation with $\partial_\mu\Phi = 0$ for $\mu \ne x_4$, and the gravity term inserted).

$$
\gamma^{(x_4)}\Phi' = M\Phi - c\,\gamma^{(x_0)}\Phi - \big(u - \tfrac12a_4'\big)\gamma^{(x_4)}\Phi
$$

(the two gravity terms moved to the right).

$$
\Phi' = -M\gamma^{(x_4)}\Phi + c\,\gamma^{(x_4)}\gamma^{(x_0)}\Phi - \big(u - \tfrac12a_4'\big)\Phi
$$

(both sides multiplied on the left by $-\gamma^{(x_4)}$: on the left $-(\gamma^{(x_4)})^2 = 1$ by the Clifford relation with $\eta_{44} = -1$; on the right $-\gamma^{(x_4)}\cdot(-c\gamma^{(x_0)}) = c\gamma^{(x_4)}\gamma^{(x_0)}$ and $-\gamma^{(x_4)}\cdot\big(-(u - \tfrac12a_4')\gamma^{(x_4)}\big) = (u - \tfrac12a_4')(\gamma^{(x_4)})^2 = -(u - \tfrac12a_4')$). So

$$
\Phi' = \mathcal{A}\Phi,\qquad \mathcal{A} = \mathcal{B} - \big(u - \tfrac12a_4'\big)1,\qquad \mathcal{B} = -M\gamma^{(x_4)} + c\,\gamma^{(x_4)}\gamma^{(x_0)} .
$$

The matrix $\mathcal{A}$ contains no $z$: the equation is consistent for every $x_0$ (PROVED: sympy report, check `authorT16_condensate_equation`; Wolfram report, check `condensate_equation_x0_consistent`).

**The square of $\mathcal{B}$.** Line by line:

$$
\mathcal{B}^2 = M^2\big(\gamma^{(x_4)}\big)^2 - Mc\big(\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_0)} + \gamma^{(x_4)}\gamma^{(x_0)}\gamma^{(x_4)}\big) + c^2\gamma^{(x_4)}\gamma^{(x_0)}\gamma^{(x_4)}\gamma^{(x_0)}
$$

(the square of a sum of two matrices, keeping their order)

$$
= -M^2 - Mc\big(-\gamma^{(x_0)} + \gamma^{(x_0)}\big) + c^2
$$

($(\gamma^{(x_4)})^2 = -1$; $\gamma^{(x_0)}\gamma^{(x_4)} = -\gamma^{(x_4)}\gamma^{(x_0)}$, so $\gamma^{(x_4)}\gamma^{(x_0)}\gamma^{(x_4)} = -(\gamma^{(x_4)})^2\gamma^{(x_0)} = \gamma^{(x_0)}$; and $\gamma^{(x_4)}\gamma^{(x_0)}\gamma^{(x_4)}\gamma^{(x_0)} = -(\gamma^{(x_4)})^2(\gamma^{(x_0)})^2 = 1$)

$$
\mathcal{B}^2 = (c^2 - M^2)\,1
$$

(the middle terms cancel). So where $c^2 < M^2$ the eigenvalues of $\mathcal{B}$ are $\pm i\sqrt{M^2 - c^2}$ and the condensate oscillates with the local frequency $w = \sqrt{M^2 - c^2}$; where $c^2 > M^2$ they are real and it grows or decays. On the record history $c = \tfrac32He^{a_4}b_4^{-1/2} = \tfrac32He^{Hx_4/3}$ grows, so every condensate stops oscillating at $x_4 = (3/H)\ln(2|M|/(3H))$ (Notebook 12d, figure 12d.1): the hidden direction shrinks, and its term in the field equation grows.

**The density law.** The part $-(u - \tfrac12a_4')1$ of $\mathcal{A}$ is a multiple of the unit matrix; writing $\Phi = e^{a_4/2}b_4^{-1}\chi$ removes it, because the derivative of the prefactor is $(\tfrac12a_4' - u)$ times the prefactor, so $\chi' = \mathcal{B}\chi$. For the density, with real $M$ and $c$ the matrix $\mathcal{A}$ is real:

$$
S' = \big(\Phi^\dagger C\Phi\big)' = \Phi^\dagger\big(\mathcal{A}^TC + C\mathcal{A}\big)\Phi = -2\big(u - \tfrac12a_4'\big)S = \big(a_4' - 2u\big)S
$$

(the product rule, $\Phi'^\dagger = \Phi^\dagger\mathcal{A}^T$ for a real $\mathcal{A}$; then $C\mathcal{B} + \mathcal{B}^TC = 0$, which follows from $C$ symmetric and every $C\gamma^{(a)}$ antisymmetric, so that only the unit part contributes $-2(u - \tfrac12a_4')C$). Integrating, $\ln S = a_4 - 2\ln b_4 + \text{const}$, so

$$
S = e^{a_4}b_4^{-2}S_0
$$

for every solution and every history (PROVED: sympy report, check `authorT16_condensate_S_law`; Wolfram report, check `condensate_S_law`). On the record history $S \propto e^{a_4 - (8/3)a_4} = e^{-(5/3)a_4}$ decays, while the required source grows like $k^2$.

**Its energy-momentum tensor.** For a configuration that depends on $x_4$ only, the diagonal kinetic components $K^\mu{}_\mu$ with $\mu \ne x_4$ vanish (they contain no spin connection, record lemma `diagonalKinetic`, and no derivative), and $K^{x_4}{}_{x_4} = MS$ (record check `condensate_kinetic_tensor_diagonal`). With the record's convention $T^\mu{}_\nu = \sigma_T(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu L)$, $\sigma_T = +1$ (ASSUMED, the convention of the record), and the on-shell Lagrangian $L = \sum_\mu K^\mu{}_\mu - mS - U = MS - mS - U = SU'(S) - U(S)$:

$$
\rho = -T^{x_4}{}_{x_4} = MS - L = mS + U(S),\qquad p_3 = p_t = p_0 = L = SU'(S) - U(S)
$$

(the definitions with $K^{x_4}{}_{x_4} = MS$ and $K^\mu{}_\mu = 0$ otherwise; $M - U' = m$). So a homogeneous condensate has **equal pressures**. Notebook 12b showed what that costs: in Einstein gravity no exponential history allows equal pressures, and with the author's weights only histories with constant $k$, on which the block does not shrink (record checks `condensate_source_equal_pressures` of both reports); and the record history needs $\kappa(p_3 - p_0) \ne 0$, so no condensate is its source (dark-sector record, check `condensate_cannot_source_history`).

**The off-diagonal components: 24 bilinears.** The off-diagonal kinetic components of a condensate do not vanish automatically. The record lists them (key `fields/dirac16complex00/offDiagonalKinetic`: 36 ordered pairs $(\mu, \nu)$) and shows that each is a combination of the **three-gamma bilinears** $B_{abc} = \bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$ with

$$
\{a, b, c\} = \{x_0, i, x_4\}\ (3),\quad \{x_0, i, t\}\ (9),\quad \{i, x_4, t\}\ (9),\quad \{x_0, x_4, t\}\ (3),
$$

with $i$ a 3-space direction and $t$ an extra time: $3 + 9 + 9 + 3 = 24$ bilinears (key `fields/dirac16complex00/offDiagonalConditions`; Wolfram report, check `condensate_offdiagonal_are_three_gamma_bilinears`; sympy report, check `authorT16_condensate_offdiagonal_three_gamma`). Since the off-diagonal field equations read $0 = \kappa T^\mu{}_\nu$ (Section 12.8), all 24 must vanish. The current record says 24 in every place (the equations, both verifier reports, the summary and the document `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md`), and Notebook 12d counts 24 distinct bilinears in the record's list of 36 components (In [11]). One sentence of `Revision/field_equations_a4/README.md` speaks of "the 15 three-gamma bilinears"; it belongs to the README's account of the witnesses of an earlier version of the record (it cites the check `condensate_diagonal_witness_exact`, which the current Wolfram report no longer contains), not to the corrected metric.

**The witnesses.** On the histories with constant $k = e^{2a_4}/b_4 = k_0$, that is $b_4 = e^{2a_4}/k_0$ with any $a_4(x_4)$, the coefficient $c = \tfrac32H\sqrt{k_0}$ is constant and $\mathcal{B}$ is a constant matrix. The record finds exact condensates with all 24 bilinears zero and $S \ne 0$ there (key `fields/dirac16complex00/offDiagonalWitness`; Wolfram report, check `condensate_witness_constant_k_exact`; sympy report, check `authorT16_condensate_witness`): $\Phi = e^{a_4/2}b_4^{-1}e^{-iwx_4}\Phi_0$ with $w = \sqrt{M^2 - c^2}$ and $\Phi_0 = v_1 + c_{12}v_2$, where $v_1$ and $v_2$ are eigenvectors of $\mathcal{B}$ for the eigenvalue $-iw$ on which $\gamma^{(x_1)}\gamma^{(x_5)} = \gamma^{(x_2)}\gamma^{(x_6)} = \gamma^{(x_3)}\gamma^{(x_7)}$ equals $-1$ and $+1$, and $c_{12} = \overline{v_1^\dagger Cv_2}$; checked exactly at $(M, H, k_0) = (5, 1, 4)$, $(5, \tfrac43, 4)$ and $(-5, 1, 4)$. An example that proves that something exists is called a **witness**. For $k$ not constant the record does not decide whether such condensates exist. The record also states, in `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md`, that it "contains no check that combines a witness with the field equations for definite kappa, Lambda, m, lambda and a history".

**What the textbook adds (PROVED here; a computation of this book, not a Revision record).** Notebook 12d makes that combination. On the family $b_4 = e^{2a_4}/k_0$ we have $u = 2a_4'$, $v = 2a_4''$ and $h = \tfrac12u - a_4' = 0$: the hidden direction and the extra times keep the constant size $e^{-a_4}b_4^{1/2} = k_0^{-1/2}$. A witness has a constant $M$; its density $S = e^{a_4}b_4^{-2}S_0 = k_0^2e^{-3a_4}S_0$ changes if $a_4$ changes, so $U' = M - m$ must be constant on the range of $S$, $U = (M - m)S + U_0$, and then $p = SU' - U = -U_0$ and $\rho = mS + U = MS + U_0$. The constant $U_0$ acts exactly like a change of $\Lambda$ by $\kappa U_0$. So, up to a change of $\Lambda$, a witness is a pressureless source (like dust) with $\rho = MS$ and no off-diagonal component, and it is conserved on the family ($\partial_4\rho + 3a_4'\rho = 0$ with $h = 0$). The field equations on the family then read

$$
e_{44} + \Lambda = -\kappa MS,\qquad e_{11} + \Lambda = 0,\qquad e_{00} + \Lambda = 0 .
$$

*Einstein gravity.* With $u = 2a_4'$, $v = 2a_4''$, $k = k_0$ the components of Section 12.9 become

$$
e_{11} = -5(a_4')^2 + 12(a_4')^2 + 2a_4'' - 10(a_4')^2 - 4a_4'' + 6H^2k_0 = -3(a_4')^2 - 2a_4'' + 6H^2k_0,
$$
$$
e_{00} = -3(a_4')^2 + 3(a_4')^2 - 6(a_4')^2 - 3a_4'' + 3H^2k_0 = -6(a_4')^2 - 3a_4'' + 3H^2k_0
$$

(inserted term by term: $6a_4'u = 12(a_4')^2$, $\tfrac52u^2 = 10(a_4')^2$, $2v = 4a_4''$; $\tfrac32a_4'u = 3(a_4')^2$, $\tfrac32u^2 = 6(a_4')^2$, $\tfrac32v = 3a_4''$). Three times the 3-space equation minus twice the block equation removes $a_4''$:

$$
3\big(-3(a_4')^2 - 2a_4'' + 6H^2k_0 + \Lambda\big) - 2\big(-6(a_4')^2 - 3a_4'' + 3H^2k_0 + \Lambda\big) = 3(a_4')^2 + 12H^2k_0 + \Lambda = 0
$$

($-9 + 12 = 3$; $-6 + 6 = 0$; $18 - 6 = 12$; $3 - 2 = 1$). So $(a_4')^2$ is constant and $a_4'' = 0$. The 3-space equation then gives $\Lambda = 3(a_4')^2 - 6H^2k_0$, and inserting this above, $3(a_4')^2 + 12H^2k_0 + 3(a_4')^2 - 6H^2k_0 = 0$, that is $(a_4')^2 = -H^2k_0 < 0$ (and $\Lambda = -9H^2k_0$). No real history of the family has zero pressures: in Einstein gravity no witness, of any density, is the source of a history of its family.

*The author's couplings*, with any $\Lambda$. The 3-space and block equations are linear in $a_4''$. Their combination without $a_4''$ (the 3-space equation times the coefficient of $a_4''$ in the block equation, minus the block equation times the coefficient of $a_4''$ in the 3-space equation) is a polynomial $P = c_4(a_4')^4 + c_2(a_4')^2 + c_0$ that must vanish at every time. If $P$ is not the zero polynomial, $a_4'$ can take only its finitely many roots; being continuous, it is constant, so $a_4'' = 0$. There $e_{44} = e_{11}$ (Notebook 12d checks it for both theories; with $h = 0$ and a constant $e_{44}$ the Bianchi identity of Section 12.10 gives $0 = 3a_4'(e_{11} - e_{44})$), and the difference of the first two equations gives $-\kappa MS = e_{44} - e_{11} = 0$. If $P$ is the zero polynomial, $c_4 = c_2 = c_0 = 0$: Notebook 12d finds that this happens only at $k_0 = 6 \pm 2\sqrt5$ with $\Lambda = -\tfrac32H^2(k_0 + 4)$, where $e_{44} + \Lambda = 0$ for every $a_4$, so again $\kappa MS = 0$. In both cases $S = 0$ (the recipe needs $M^2 > c^2 > 0$, so $M \ne 0$): **a witness with nonzero density is the source of no history of its family**, in Einstein gravity and with the author's couplings for every $\Lambda$. A by-product: at $k_0 = 6 \pm 2\sqrt5$ with that $\Lambda$ the time and 3-space equations hold on every history of the family, so the family contains vacua that are not exponential (with the author's $\Lambda = -10$ they do not occur, since $-\tfrac32(10 \pm 2\sqrt5)$ is $-21.7$ or $-8.3$).

**What stays OPEN.** Condensates on histories whose $k$ is not constant (the record: not decided), and so whether any field of the theory drives the deflation of the extra times exactly. The condensate sources that the record allows with the author's weights on $\beta = 2$ need $M = 0$, where the recipe of the witnesses does not apply; whether their 24 bilinears can vanish is not decided. Nothing here concerns the quantised field dirac16complex, stability, or the creation of universes.

### 12.27 Example: the record's witnesses and the field equations

The fourth notebook rebuilds, with exact arithmetic and the author's eight real 16 by 16 gamma matrices, the spin connection of the corrected metric for general $a_4$ and $b_4$, the gravity term, the condensate equation and the density law; draws where the condensate stops oscillating on the record history; builds the record's witnesses as a one-parameter family whose 24 bilinears vanish for every value of the parameter; computes their complete energy-momentum tensor for an arbitrary $a_4$ on the family $b_4 = e^{2a_4}/4$; and proves the two statements of Section 12.26 with the record's Lovelock components. It prints 31 PASS lines, draws six figures and runs in about forty seconds.

<!-- NOTEBOOK 12d -->

### 12.30 Line-by-line walk-through of Notebook 12d

The notebook has 18 code cells, In [1] to In [18]. As in Section 12.16, every line or small group of lines is quoted and explained; docstrings are left out, and long captions are shortened to their first line and `...)` (they are printed in full under the figures in Section 12.29).

**In [1], the set-up cell.** It is the set-up cell of Notebook 12a, explained line by line in Section 12.16 under In [1], with two differences: its comment lines are the run instructions of Notebook 12d (Section 12.28), and its line `NOTEBOOK_ID = "12d"  # this notebook: chapter 12, example d` names this notebook. It prints Set-up of notebook 12d complete: repository folder found, helpers defined.

**In [2], the records and the open question.**

```python
import contextlib  # redirect_stdout: send printed lines into a buffer
import io  # StringIO: a text buffer in memory
```

The two modules for the text buffer of `reproduces`.

```python
GAMMAS = "Revision/algebra/gammas.json"  # the author's gamma matrices
EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the a4, b4 equations
PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
EMT = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
DOC = "Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md"  # the record's document
```

Short names for the files: the author's gamma matrices (`gammas.json` of the algebra record), the equations, the sympy and Wolfram reports, the lead's divergence report, and the record's document on the commuting field.

```python
def read_json(relative):
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))
```

`read_json`, as in Notebook 12a.

```python
def record_verdict(report_file, name):
    for entry in read_json(report_file)["checks"]:
        if entry["name"] == name:
            return entry["verdict"]
    return None
```

`record_verdict`, as in Notebook 12a.

```python
def reproduces(condition, name, report_file, record_name):
    found = record_verdict(report_file, record_name) == "PASS"
    lines = io.StringIO()  # a text buffer
    with contextlib.redirect_stdout(lines):  # print() now writes into the buffer
        check(condition and found, name, record=f"{report_file}, check {record_name}")
    print(lines.getvalue(), end="")  # all lines at once
```

`reproduces`, as in Notebook 12a.

```python
OPEN_SENTENCE = ("this record contains no check that combines a witness with the "
                 "field equations for definite")
document = repository_file(DOC).read_text(encoding="utf-8")
say(f"{DOC} says: \"... {OPEN_SENTENCE} kappa, Lambda, m, lambda and a history.\"")
check(OPEN_SENTENCE in document, "the record leaves this combination open")
```

`OPEN_SENTENCE` is the beginning of the sentence of the record's document that says what the record does not contain (two strings written next to each other inside parentheses are joined into one). The document is read as text and the sentence is printed with its end (`\"` is a quotation mark inside the f-string); the check requires the sentence to be in the document (Out [2]). If the record were extended with such a check, this line would fail and the notebook would have to be revised.

**In [3], the author's gamma matrices and the matrix $C$.**

```python
import itertools  # loops over all combinations of indices
```

`itertools` for loops over index combinations.

```python
import numpy as np  # floating-point arrays, used only for the plots
import sympy as sp  # exact algebra
```

`numpy` only for the plots; `sympy` for the exact algebra.

```python
NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # positions 0..7
ETA = [1, 1, 1, 1, -1, -1, -1, -1]  # the frame metric eta, x0..x7
I16, Z16 = sp.eye(16), sp.zeros(16, 16)  # the 16 by 16 unit and zero matrices
fixture = read_json(GAMMAS)
gamma = [sp.Matrix([[sp.Rational(x) for x in row] for row in matrix])
         for matrix in fixture["gamma"]]  # gamma[a] = gamma^(xa)
```

`NAMES` and the frame metric `ETA` $= (+,+,+,+,-,-,-,-)$ in the order $x_0, \dots, x_7$; `sp.eye(16)` and `sp.zeros(16, 16)` are the 16 by 16 unit and zero matrices. The record stores each gamma matrix as a list of rows of texts (integers or fractions); `sp.Rational(x)` turns each text into an exact number, and `gamma[a]` is $\gamma^{(x_a)}$.

```python
clifford = all(gamma[a] * gamma[b] + gamma[b] * gamma[a]
               == 2 * ETA[a] * (1 if a == b else 0) * I16
               for a in range(8) for b in range(8))
reproduces(clifford, "the author's gammas satisfy the Clifford relation",
           PY, "authorT16_clifford")
C = gamma[0] * gamma[1] * gamma[2] * gamma[3]  # C = g^(x0) g^(x1) g^(x2) g^(x3)
```

`clifford` checks $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}1$ for all 64 pairs (sympy report, `authorT16_clifford`). `C` is the product $\gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$.

```python
stored_C = sp.Matrix([[sp.Rational(x) for x in row] for row in fixture["C"]])
properties = (C == stored_C and C == C.T and C * C == I16
              and all((C * g).T == -(C * g) for g in gamma))
reproduces(properties, "C is the record's C, real symmetric, C^2 = 1, C gamma "
           "antisymmetric", PY, "authorT16_C_properties")
```

The record also stores $C$; the check compares the two and requires the three properties the adjoint $\bar\Phi = \Phi^\dagger C$ needs: $C$ is symmetric (`C.T` is the transpose), $C^2 = 1$, and every $C\gamma^{(a)}$ is antisymmetric (sympy report, `authorT16_C_properties`). Out [3] shows two PASS lines.

**In [4], the spin connection of the corrected metric.**

```python
H = sp.symbols("H", positive=True)  # the constant H of the metric
t = sp.symbols("t", real=True, nonzero=True)  # t = tan z, z = 6 H x0 real
wz = sp.symbols("wz", positive=True)  # wz = (sin(z)^2)^(1/12)
ea, q = sp.symbols("ea q", positive=True)  # ea = e^(a4), q = b4^(1/2)
ad1, ad2, uu, vv = sp.symbols("ad1 ad2 uu vv", real=True)  # a4', a4'', u, v
E = [q / (ea * t)] + [ea] * 3 + [sp.Integer(1)] + [q * wz / ea] * 3  # the vielbein
g = [ETA[a] * E[a] ** 2 for a in range(8)]  # g_aa = eta_aa E_a^2
RATE = {ea: ea * ad1, q: q * uu / 2, ad1: ad2, uu: vv}  # d/dx4 of each symbol
```

The symbols, as in Notebook 12a, except that `q` stands for $b_4^{1/2}$ and `wz` for $(\sin^2 z)^{1/12}$. `E` is the vielbein of Chapter 6, $E_0 = b_4^{1/2}/(e^{a_4}\tan z) = e^{-a_4}b_4^{1/2}\cot z$ (with the sign of $\cot z$), $E_i = e^{a_4}$, $E_4 = 1$, $E_t = b_4^{1/2}w_z/e^{a_4}$; the metric follows as $g_{aa} = \eta_{aa}E_a^2$. `RATE` gives the time derivatives: $\partial_4e^{a_4} = a_4'e^{a_4}$, $\partial_4b_4^{1/2} = \tfrac12u\,b_4^{1/2}$, $\partial_4a_4' = a_4''$, $\partial_4u = v$.

```python
def d(expr, mu):
    if mu == 4:
        return sum(sp.diff(expr, symbol) * rate for symbol, rate in RATE.items())
    if mu == 0:
        return 6 * H * (1 + t ** 2) * sp.diff(expr, t) + H * wz / t * sp.diff(expr, wz)
    return sp.Integer(0)  # nothing depends on x1, x2, x3, x5, x6, x7
```

`d(expr, mu)`, the partial derivative, as in Notebook 12a (without the explicit `X4`, `Z`).

```python
Gamma = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
for a, b, c in itertools.product(range(8), repeat=3):  # diagonal-metric formula
    value = 0
    if a == c:
        value += d(g[a], b)
    if a == b:
        value += d(g[a], c)
    if b == c:
        value -= d(g[b], a)
    Gamma[a][b][c] = sp.cancel(value / (2 * g[a]))
```

The Christoffel symbols of the diagonal metric, with the formula of Section 12.4, exactly as in Notebook 12a, In [5].

```python
S_ab = [[(gamma[a] * gamma[b] - gamma[b] * gamma[a]) / 4 for b in range(8)]
        for a in range(8)]
omega = [[[sp.cancel(ETA[a] * E[a] * Gamma[a][mu][b] / E[b]) if a != b else 0
           for b in range(8)] for a in range(8)] for mu in range(8)]
antisymmetric = all(sp.cancel(omega[mu][a][b] + omega[mu][b][a]) == 0
                    for mu in range(8) for a in range(8) for b in range(8))
```

`S_ab[a][b]` is $S^{ab} = \tfrac14[\gamma^{(a)}, \gamma^{(b)}]$. `omega[mu][a][b]` is the canonical spin connection $\omega_{\mu\,ab} = \eta_{aa}(E_a/E_b)\Gamma^a{}_{\mu b}$ for $a \ne b$ and 0 for $a = b$ (the formula of the notebook's text, from the vielbein postulate of Chapter 6). `antisymmetric` checks $\omega_{\mu\,ab} = -\omega_{\mu\,ba}$ for all 512 index lists.

```python
reproduces(antisymmetric, "omega_mu ab = -omega_mu ba (canonical spin connection)",
           WL, "spin_connection_antisymmetric")
Omega = [sum((omega[mu][a][b] * S_ab[a][b] / 2 for a in range(8) for b in range(8)
              if omega[mu][a][b] != 0), Z16) for mu in range(8)]
for mu in range(8):
    terms = sum(1 for a in range(8) for b in range(8) if omega[mu][a][b] != 0)
    say(f"Omega_{NAMES[mu]}: {terms} nonzero entries omega_mu ab")
```

The check reproduces the Wolfram report's `spin_connection_antisymmetric`. `Omega[mu]` is $\Omega_\mu = \tfrac12\sum_{a,b}\omega_{\mu\,ab}S^{ab}$, summed only over the entries that are not zero, starting from the zero matrix (the second argument of `sum`). The loop prints how many entries $\omega_{\mu\,ab}$ are not zero for each $\mu$ (Out [4]): 2 for $x_0$ (the pair $x_0x_4$, from $\Gamma^{x_4}{}_{x_0x_0}$ and $\Gamma^{x_0}{}_{x_0x_4}$), 2 for each 3-space direction (the pair $x_ix_4$), 0 for $x_4$, and 4 for each extra time (the pairs $x_0x_t$ and $x_4x_t$).

**In [5], the gravity term.**

```python
gamma_curved = [gamma[mu] / E[mu] for mu in range(8)]  # gamma^mu = gamma^(mu)/E_mu
h4 = uu / 2 - ad1  # the rate of the block (x0, x5, x6, x7)
expected_x0 = (q / (2 * t * ea)) * h4 * gamma[0] * gamma[4]
reproduces(Omega[4] == Z16
           and (Omega[0] - expected_x0).applyfunc(sp.cancel) == Z16,
           "Omega_x4 = 0, Omega_x0 = (1/2) cot z e^(-a4) b4^(1/2) h4 g^(x0) g^(x4)",
           PY, "authorT16_Omega_x4_zero_Omega_x0")
```

`gamma_curved[mu]` is $\gamma^\mu = \gamma^{(\mu)}/E_\mu$. The first check: $\Omega_{x_4} = 0$ and $\Omega_{x_0} = \tfrac12\cot z\,e^{-a_4}b_4^{1/2}h\,\gamma^{(x_0)}\gamma^{(x_4)}$ with $h = \tfrac12u - a_4'$ (`applyfunc(sp.cancel)` simplifies every entry of a matrix; sympy report, `authorT16_Omega_x4_zero_Omega_x0`).

```python
anticommute = all((gamma_curved[mu] * Omega[mu] + Omega[mu] * gamma_curved[mu])
                  .applyfunc(sp.cancel) == Z16 for mu in range(8))
reproduces(anticommute, "{gamma^mu, Omega_mu} = 0 for each mu (no sum)",
           PY, "authorT16_anticommutator_no_sum")
gravity_term = sum((gamma_curved[mu] * Omega[mu] for mu in range(8)), Z16)
gravity_term = gravity_term.applyfunc(sp.cancel)
```

For each $\mu$ separately the anticommutator $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu$ must vanish (sympy report, `authorT16_anticommutator_no_sum`). `gravity_term` is the sum $\sum_\mu\gamma^\mu\Omega_\mu$, simplified entry by entry.

```python
c_gravity = sp.Rational(3, 2) * H * ea / q  # (3/2) H e^(a4) b4^(-1/2)
expected = c_gravity * gamma[0] + (uu - ad1 / 2) * gamma[4]
same = (gravity_term - expected).applyfunc(sp.cancel) == Z16
reproduces(same, "gamma^mu Omega_mu = (3/2) H e^(a4) b4^(-1/2) g^(x0) + (u - a4'/2) "
           "g^(x4)", PY, "authorT16_gravity_term")
reproduces(same, "the same, the lead's independent check",
           EMT, "gamma_Omega_equals_hidden_block_terms")
```

`c_gravity` is $c = \tfrac32He^{a_4}b_4^{-1/2}$; the gravity term must equal $c\,\gamma^{(x_0)} + (u - \tfrac12a_4')\gamma^{(x_4)}$, which contains no $z$: the $\cot z$ of $\Omega_{x_0}$ and the $1/E_0$ of $\gamma^{x_0}$ combine into a constant. The comparison reproduces the sympy report's `authorT16_gravity_term` and the lead's independent check `gamma_Omega_equals_hidden_block_terms`. Out [5] shows four PASS lines.

**In [6], the condensate equation and the density law.**

```python
MM = sp.symbols("M", real=True)  # the effective mass M = m + U'(S)
B_sym = -MM * gamma[4] + c_gravity * gamma[4] * gamma[0]
A_sym = B_sym - (uu - ad1 / 2) * I16
reduced = (gamma[4] * A_sym + gravity_term - MM * I16).applyfunc(sp.cancel)
reproduces(reduced == Z16 and not A_sym.has(t) and not A_sym.has(wz),
           "gamma^(x4) A + gamma^mu Omega_mu = M: the equation is Phi' = A Phi",
           PY, "authorT16_condensate_equation")
```

`MM` is the effective mass $M$; `B_sym` and `A_sym` are $\mathcal{B}$ and $\mathcal{A}$ of Section 12.26. The check: $\gamma^{(x_4)}\mathcal{A} + \sum_\mu\gamma^\mu\Omega_\mu - M = 0$, which is the field equation for $\Phi' = \mathcal{A}\Phi$ (multiply $\Phi' = \mathcal{A}\Phi$ by $\gamma^{(x_4)}$ and compare), and $\mathcal{A}$ contains no $t$ and no $w_z$ (sympy report, `authorT16_condensate_equation`).

```python
check((B_sym * B_sym - (c_gravity ** 2 - MM ** 2) * I16).applyfunc(sp.cancel) == Z16,
      "B^2 = (c^2 - M^2), c = (3/2) H e^(a4) b4^(-1/2)")
reproduces((C * A_sym + A_sym.T * C + 2 * (uu - ad1 / 2) * C).applyfunc(sp.expand)
           == Z16, "C A + A^T C = -2 (u - a4'/2) C: S = e^(a4) b4^(-2) S0",
           PY, "authorT16_condensate_S_law")
```

$\mathcal{B}^2 = (c^2 - M^2)1$, derived by hand in Section 12.26; and $C\mathcal{A} + \mathcal{A}^TC = -2(u - \tfrac12a_4')C$, which gives the density law $S = e^{a_4}b_4^{-2}S_0$ (sympy report, `authorT16_condensate_S_law`). Out [6] shows three PASS lines.

**In [7], figure 12d.1: the condensate stops oscillating.**

```python
times = np.linspace(0.0, 6.0, 601)  # x4 in units 1/H
c_history = 1.5 * np.exp(times / 3.0)  # c on the record history, H = 1
B_numeric = sp.lambdify((MM, ea, q), B_sym.subs(H, 1), "numpy")
deviations, counts = [], []
for x_value in (0.0, 1.0, 2.0, 3.0, 4.0, 5.0):
    matrix = np.array(B_numeric(5.0, np.exp(x_value), np.exp(2.0 * x_value / 3.0)),
                      dtype=float)  # e^(a4) = e^(x4), b4^(1/2) = e^(2 x4/3)
    eigenvalues = np.linalg.eigvals(matrix)
    c_value = 1.5 * np.exp(x_value / 3.0)
    squared = c_value ** 2 - 25.0  # c^2 - M^2: each eigenvalue squared
    deviations.append(np.max(np.abs(eigenvalues ** 2 - squared)))
    counts.append(int(np.sum(eigenvalues.imag > 1e-9) + np.sum(eigenvalues.real > 1e-9)))
```

601 times from 0 to 6 and the values of $c = \tfrac32e^{x_4/3}$ on the record history ($H = 1$). `B_numeric` is $\mathcal{B}$ as a numpy function of $M$, $e^{a_4}$ and $b_4^{1/2}$. For $M = 5$ at six times the loop builds the numerical matrix (on the record history $e^{a_4} = e^{x_4}$ and $b_4^{1/2} = e^{2x_4/3}$), computes its 16 eigenvalues with `np.linalg.eigvals`, and stores the largest deviation of an eigenvalue squared from $c^2 - M^2$ and the number of eigenvalues "on the positive side" (positive imaginary part or positive real part).

```python
say(f"largest deviation of an eigenvalue squared from c^2 - M^2: {max(deviations):.0e}")
say(f"eigenvalues on the positive side, at x4 = 0, 1, ..., 5: {counts}")
check(max(deviations) < 1e-9 and counts == [8] * 6,
      "M = 5: the 16 eigenvalues of B are +-sqrt(c^2 - M^2), eight of each sign")
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
left.plot(times, c_history, color="black", label="$c = \\frac{3}{2}e^{x_4/3}$")
```

The cell prints (Out [7]) the largest deviation, `8e-14`, and the counts `[8, 8, 8, 8, 8, 8]`; the check requires deviations below $10^{-9}$ and eight eigenvalues on each side at every time: $\pm i\sqrt{M^2 - c^2}$ before the threshold, $\pm\sqrt{c^2 - M^2}$ after it. Then the figure: two panels, $c$ against the time on the left.

```python
for mass, style in ((3.0, ":"), (5.0, "--"), (7.0, "-.")):
    left.axhline(mass, linestyle=style, color="tab:blue", label=f"$|M| = {mass:g}$")
    frequency = np.sqrt(np.maximum(mass ** 2 - c_history ** 2, 0.0))
    right.plot(times, frequency, style, label=f"$|M| = {mass:g}$")
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("$c$ and $|M|$ (units $H$)")
```

For $|M| = 3$, 5 and 7 a horizontal line on the left and, on the right, the local frequency $\sqrt{M^2 - c^2}$ (`np.maximum(..., 0.0)` replaces negative values by 0 before the root); labels of the left panel.

```python
left.set_title("the hidden-direction coefficient grows")
left.legend(fontsize=8)
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("local frequency $\\sqrt{M^2 - c^2}$ (units $H$)")
right.set_title("the condensate stops oscillating")
right.legend(fontsize=8)
```

Titles, labels and legends.

```python
save_figure(fig, "oscillation_threshold",
            "A homogeneous condensate of dirac16complex00 on the record history "
...)
```

`save_figure` (the caption is printed under figure 12d.1 in Section 12.29). The frequency falls to zero where $c$ reaches $|M|$, at $x_4 = 3\ln(2|M|/3)$: 2.08, 3.61 and 4.62 for $|M| = 3$, 5, 7.

**In [8], the witnesses.**

```python
s = sp.symbols("s", real=True)  # the free real parameter of the family
TRIPLES = list(itertools.combinations(range(8), 3))  # all 56 sets {a, b, c}
NEEDED = sorted({tuple(sorted((0, i, 4))) for i in (1, 2, 3)}
                | {tuple(sorted((0, i, j))) for i in (1, 2, 3) for j in (5, 6, 7)}
                | {tuple(sorted((i, 4, j))) for i in (1, 2, 3) for j in (5, 6, 7)}
                | {tuple(sorted((0, 4, j))) for j in (5, 6, 7)})
```

`s` is the real parameter of the family. `TRIPLES` lists all 56 sets of three different directions, as sorted triples. `NEEDED` collects, as a set union (`|`) of four set comprehensions, the 24 triples whose bilinears the off-diagonal field equations need to vanish: $\{x_0, i, x_4\}$, $\{x_0, i, t\}$, $\{i, x_4, t\}$, $\{x_0, x_4, t\}$; each triple is sorted so that it matches the form in `TRIPLES`.

```python
def witness_parts(M_value, c_value=3):
    w_value = sp.sqrt(M_value ** 2 - c_value ** 2)
    B_value = -M_value * gamma[4] + c_value * gamma[4] * gamma[0]
    spaces = []
    for sign in (-1, 1):  # the value of g^(x1)g^(x5) = g^(x2)g^(x6) = g^(x3)g^(x7)
        stack = sp.Matrix.vstack(B_value + sp.I * w_value * I16,
                                 gamma[1] * gamma[5] - sign * I16,
                                 gamma[2] * gamma[6] - sign * I16,
                                 gamma[3] * gamma[7] - sign * I16)
        spaces.append(stack.nullspace())  # all solutions of stack * v = 0
    v1, v2 = spaces[0][0], spaces[1][0]
    c12 = sp.conjugate(sp.expand((v1.H * C * v2)[0]))  # conj(v1^dagger C v2)
    return spaces, v1, v2, c12, w_value, B_value
```

`witness_parts(M_value, c_value)` follows the record's recipe for a constant $c$ (the default 3 is $k_0 = 4$ at $H = 1$). `w_value` is $w = \sqrt{M^2 - c^2}$ and `B_value` the matrix $\mathcal{B}$. For each value $\mp1$ of the three products $\gamma^{(x_1)}\gamma^{(x_5)}$, $\gamma^{(x_2)}\gamma^{(x_6)}$, $\gamma^{(x_3)}\gamma^{(x_7)}$ the cell stacks four 16 by 16 matrices on top of each other (`vstack`); a spinor $v$ with `stack * v = 0` satisfies $\mathcal{B}v = -iwv$ and has the required value of each product. `nullspace()` returns a basis of all such spinors. $v_1$ and $v_2$ are the first basis vectors, and `c12` is $\overline{v_1^\dagger Cv_2}$ (`.H` is the conjugate transpose, `sp.conjugate` the complex conjugate). The function returns everything the cells below need.

```python
def bilinear(phi, matrix):
    return sp.expand((phi.H * C * matrix * phi)[0])
```

`bilinear(phi, matrix)` is $\bar\Phi X\Phi = \Phi^\dagger CX\Phi$, a 1 by 1 matrix whose entry `[0]` is taken and expanded.

```python
def three_gamma(triple):
    a, b, c = triple
    return gamma[a] * gamma[b] * gamma[c]
```

`three_gamma(triple)` is the product $\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}$.

```python
spaces, v1, v2, c12, w_minus, B_minus = witness_parts(-5)
phi_s = (v1 + s * c12 * v2).applyfunc(sp.expand)  # the family Phi_0(s)
check([len(space) for space in spaces] == [1, 1],
      "the two null spaces are one-dimensional (v1 and v2 are unique)")
report("frequency w at M = -5 H, k0 = 4", w_minus, "H")
check((B_minus * phi_s + sp.I * w_minus * phi_s).applyfunc(sp.expand)
      == sp.zeros(16, 1), "B Phi_0(s) = -i w Phi_0(s) for every s")
needed_values = [bilinear(phi_s, three_gamma(triple)) for triple in NEEDED]
check(len(NEEDED) == 24 and all(value == 0 for value in needed_values),
      "the 24 three-gamma bilinears vanish for every real s")
```

The recipe at $M = -5$ (with $c = 3$). `phi_s` is the family $\Phi_0(s) = v_1 + s\,c_{12}v_2$. The checks: both null spaces are one-dimensional, so $v_1$ and $v_2$ are unique up to a factor; the frequency is printed (`RESULT frequency w at M = -5 H, k0 = 4 = 4 H`); $\Phi_0(s)$ has the eigenvalue $-iw$ for every $s$; and the 24 needed bilinears vanish for every real $s$, with $s$ kept as a symbol. Out [8] shows three PASS lines and one RESULT line.

**In [9], the density of the family and the record's case $M = +5$.**

```python
S0_s = bilinear(phi_s, I16)  # Phi_0(s)^dagger C Phi_0(s)
cross = sp.expand((v1.H * C * v2)[0])  # v1^dagger C v2
report("v1^dagger C v2", cross)
report("Phi_0(s)^dagger C Phi_0(s)", S0_s)
check(bilinear(v1, I16) == 0 and bilinear(v2, I16) == 0
      and sp.expand(S0_s - 2 * s * cross * sp.conjugate(cross)) == 0,
      "Phi_0(s)^dagger C Phi_0(s) = 2 s |v1^dagger C v2|^2: every real density")
```

`S0_s` is $\Phi_0(s)^\dagger C\Phi_0(s)$ and `cross` is $v_1^\dagger Cv_2$; both are printed (Out [9]): `-128/25 - 96*I/25` and `2048*s/25`. The check: $v_1^\dagger Cv_1 = v_2^\dagger Cv_2 = 0$, so only the two cross terms remain, and $\Phi_0^\dagger C\Phi_0 = 2s|v_1^\dagger Cv_2|^2$ ($|{-\tfrac{128}{25}} - \tfrac{96}{25}i|^2 = \tfrac{128^2 + 96^2}{625} = \tfrac{25600}{625} = \tfrac{1024}{25}$, and $2s\cdot\tfrac{1024}{25} = \tfrac{2048}{25}s$): the family contains condensates of every real density.

```python
_, u1, u2, c_plus, w_plus, B_plus = witness_parts(5)  # the record's M = +5
phi_plus = (u1 + c_plus * u2).applyfunc(sp.expand)  # s = 1
S_plus = bilinear(phi_plus, I16)
ok_plus = ((B_plus * phi_plus + sp.I * w_plus * phi_plus).applyfunc(sp.expand)
           == sp.zeros(16, 1)
           and all(bilinear(phi_plus, three_gamma(tr)) == 0 for tr in NEEDED)
           and S_plus != 0 and sp.im(S_plus) == 0)
```

The same recipe at $M = +5$, where the record ran it, with $s = 1$ (the underscore `_` receives the null spaces, which are not needed). `ok_plus` requires the eigenvalue $-iw$, the 24 bilinears zero, and $S$ real and not zero (`sp.im` is the imaginary part).

```python
report("M = +5: Phi_0^dagger C Phi_0 with this normalisation", S_plus)
reproduces(ok_plus, "M = +5, k0 = 4: a witness with S real, not 0, 24 bilinears 0",
           PY, "authorT16_condensate_witness")
reproduces(ok_plus and sp.im(S0_s) == 0 and S0_s.subs(s, 1) != 0,
           "M = -5 and M = +5 at k0 = 4, H = 1 (s = 1): exact witnesses",
           WL, "condensate_witness_constant_k_exact")
```

The density with this normalisation is printed, `2048/25`; its size depends on the arbitrary normalisation of the null vectors and so on the representation (the record says the same). The two checks reproduce the sympy report's `authorT16_condensate_witness` and the Wolfram report's `condensate_witness_constant_k_exact`.

**In [10], figure 12d.2: the 56 three-gamma bilinears.**

```python
phi_one = phi_s.subs(s, 1)  # Phi_0(1)
all_values = [bilinear(phi_one, three_gamma(triple)) for triple in TRIPLES]
check(all(sp.im(value) == 0 for value in all_values),
      "all 56 three-gamma bilinears of Phi_0(1) are real numbers")
nonzero = [triple for triple, value in zip(TRIPLES, all_values) if value != 0]
say("nonzero bilinears: " + ", ".join(
    "".join(NAMES[i][1] for i in triple) for triple in nonzero))
```

`phi_one` is $\Phi_0(1)$. All 56 bilinears are computed and must be real numbers. `nonzero` lists the triples with a nonzero bilinear, printed with the digits of their directions (`NAMES[i][1]` is the second character of `"x5"`, the digit): Out [10] shows `123, 127, 136, 167, 235, 257, 356, 567`.

```python
check(all(4 not in triple and 0 not in triple for triple in nonzero),
      "every nonzero one avoids x4 and x0")
labels = ["".join(NAMES[i][1] for i in triple) for triple in TRIPLES]
numbers = np.array([float(value) for value in all_values])
is_needed = np.array([triple in NEEDED for triple in TRIPLES])
fig, ax = plt.subplots(figsize=(11.0, 4.2))
```

Every nonzero one avoids $x_4$ and $x_0$: they are built from 3-space directions and extra times only, and no field equation asks them to vanish. For the plot: the labels, the 56 values as floating-point numbers, and a truth array that marks the 24 needed triples; a wide figure.

```python
positions = np.arange(len(TRIPLES))
ax.bar(positions[~is_needed], numbers[~is_needed], color="tab:blue",
       label="other bilinears")
ax.plot(positions[is_needed], numbers[is_needed], "x", color="tab:red",
        markersize=8, label="the 24 the field equations need to vanish")
ax.axhline(0.0, color="black", linewidth=0.8)
```

`np.arange(56)` gives the positions 0 to 55. `ax.bar` draws the other 32 bilinears as blue bars (`~is_needed` is the negation of the truth array, used to select array entries), and the 24 needed ones as red crosses; a line at zero.

```python
ax.set_xticks(positions)
ax.set_xticklabels(labels, rotation=90, fontsize=6.5)
ax.set_xlabel("directions $abc$ of $\\bar\\Phi\\gamma^{(a)}\\gamma^{(b)}"
              "\\gamma^{(c)}\\Phi$ (digit $k$ for $x_k$)")
ax.set_ylabel("value of the bilinear")
ax.set_title("The 56 three-gamma bilinears of the witness $\\Phi_0(1)$, $M = -5H$")
```

The 56 labels turned by 90 degrees, the axis labels and the title.

```python
ax.legend(fontsize=8)
save_figure(fig, "three_gamma_bilinears",
            "The 56 three-gamma bilinears $\\bar\\Phi\\gamma^{(a)}\\gamma^{(b)}"
...)
```

The legend and `save_figure` (caption under figure 12d.2). All red crosses lie on the zero line.

**In [11], the complete energy-momentum tensor of a witness.**

```python
ON_FAMILY = {q: ea / 2, uu: 2 * ad1, vv: 2 * ad2, H: 1}  # b4 = e^(2 a4)/4
Omega_w = [matrix.subs(ON_FAMILY) for matrix in Omega]
gamma_w = [matrix.subs(ON_FAMILY) for matrix in gamma_curved]
g_w = [entry.subs(ON_FAMILY) for entry in g]
A_w = B_minus - sp.Rational(3, 2) * ad1 * I16  # A = B - (u - a4'/2), u = 2 a4'
factor = 16 / ea ** 3  # f^2 = (e^(a4/2)/b4)^2 = 16 e^(-3 a4)
```

`ON_FAMILY` inserts the family $b_4 = e^{2a_4}/4$: $b_4^{1/2} = e^{a_4}/2$, $u = 2a_4'$, $v = 2a_4''$, and $H = 1$. The connection, the curved gammas and the metric are evaluated there. `A_w` is $\mathcal{A} = \mathcal{B} - (u - \tfrac12a_4')1 = \mathcal{B} - \tfrac32a_4'1$ with the constant $\mathcal{B}$ at $M = -5$. `factor` is $f^2 = (e^{a_4/2}/b_4)^2 = 16e^{-3a_4}$: every bilinear of $\Phi = f\,e^{-iwx_4}\Phi_0$ carries it (the phase cancels between $\Phi^\dagger$ and $\Phi$).

```python
def D_phi(nu):
    return (A_w if nu == 4 else Z16) + Omega_w[nu]
```

`D_phi(nu)` is the matrix that gives $D_\nu\Phi$ from $\Phi$: $\mathcal{A} + \Omega_{x_4}$ for $\nu = x_4$ (because $\Phi' = \mathcal{A}\Phi$) and $\Omega_\nu$ otherwise.

```python
def D_phibar(nu):
    return (A_w.T * C if nu == 4 else Z16) - C * Omega_w[nu]
```

`D_phibar(nu)` is the matrix that gives the row $D_\nu\bar\Phi$ from the row $\Phi^\dagger$: $\bar\Phi' = \Phi'^\dagger C = \Phi^\dagger\mathcal{A}^TC$ for $\nu = x_4$, and the covariant derivative of the adjoint subtracts $C\Omega_\nu$.

```python
K = [[factor * (phi_s.H * ((C * gamma_w[mu] * D_phi(nu) - D_phibar(nu) * gamma_w[mu])
                           / 2) * phi_s)[0] for nu in range(8)] for mu in range(8)]
K_sym = [[sp.cancel(sp.expand((K[mu][nu] + (g_w[nu] / g_w[mu]) * K[nu][mu]) / 2))
          for nu in range(8)] for mu in range(8)]
S_family = sp.expand(factor * S0_s)  # S = 16 e^(-3 a4) Phi_0^dagger C Phi_0
off_diagonal = all(K_sym[mu][nu] == 0 for mu in range(8) for nu in range(8)
                   if mu != nu)
```

`K[mu][nu]` is $K^\mu{}_\nu = \tfrac12(\bar\Phi\gamma^\mu D_\nu\Phi - D_\nu\bar\Phi\,\gamma^\mu\Phi)$ for all 64 pairs, computed as $f^2\,\Phi_0^\dagger N^\mu{}_\nu\Phi_0$ with the 16 by 16 matrix $N^\mu{}_\nu$ of the notebook's text, for the whole family (symbol $s$), every $a_4$, $a_4'$ and every $z$. `K_sym` is the symmetrised tensor $\tfrac12\big(K^\mu{}_\nu + (g_{\nu\nu}/g_{\mu\mu})K^\nu{}_\mu\big)$ (lowering and raising the indices of the transposed component with the diagonal metric). `S_family` is $S = 16e^{-3a_4}\Phi_0^\dagger C\Phi_0$; `off_diagonal` is true when every off-diagonal component vanishes.

```python
diagonal = [K_sym[mu][mu] for mu in range(8)]
say(f"diagonal of K: {diagonal}")
reproduces(off_diagonal and all(diagonal[mu] == 0 for mu in range(8) if mu != 4)
           and sp.expand(diagonal[4] - (-5) * S_family) == 0,
           "witness: K^x4_x4 = M S, every other component of K is 0 (every a4, z)",
           PY, "authorT16_condensate_kinetic_diagonal")
```

The diagonal is printed (Out [11]): `[0, 0, 0, 0, -32768*s/(5*ea**3), 0, 0, 0]`. The check: every off-diagonal component is zero, every diagonal component except $x_4$ is zero, and $K^{x_4}{}_{x_4} = MS$ with $M = -5$ ($-5\cdot 16e^{-3a_4}\cdot\tfrac{2048}{25}s = -\tfrac{32768}{5}se^{-3a_4}$); sympy report, `authorT16_condensate_kinetic_diagonal`.

```python
offdiagonal_record = read_json(EQUATIONS)["fields"]["dirac16complex00"]
offdiagonal_record = offdiagonal_record["offDiagonalKinetic"]
bilinear_names = sorted({term["bilinear"] for entry in offdiagonal_record
                         for term in entry["terms"]})
report("record: off-diagonal kinetic components, distinct bilinears",
       f"{len(offdiagonal_record)}, {len(bilinear_names)}")
```

The record's list of the off-diagonal kinetic components of a general condensate is read; `bilinear_names` collects, as a set (no repetitions), every bilinear named in its terms, sorted. The two counts are printed: `36, 24`.

```python
reproduces(len(offdiagonal_record) == 36 and len(bilinear_names) == 24,
           "a general condensate: 36 off-diagonal components, 24 bilinears",
           WL, "condensate_offdiagonal_are_three_gamma_bilinears")
```

The check: 36 ordered pairs and 24 distinct bilinears, as the Wolfram report's `condensate_offdiagonal_are_three_gamma_bilinears` states. Out [11] shows two PASS lines.

**In [12], the witness is pressureless.**

```python
m = sp.symbols("m", real=True)  # the mass; with U = 0, m = M = -5 here
L_witness = sp.expand(sum(diagonal) - m * S_family)  # L = trace K - m S - U, U = 0
T_witness = [[sp.expand(-K_sym[mu][nu] + (L_witness if mu == nu else 0))
              for nu in range(8)] for mu in range(8)]
on_shell = {m: -5}  # M = m for U = 0
rho_witness = sp.expand(-T_witness[4][4].subs(on_shell))
```

`m` is the mass. With $U = 0$ the Lagrangian is $L = \sum_\mu K^\mu{}_\mu - mS$; `T_witness` is $T^\mu{}_\nu = -K^{(\mu}{}_{\nu)} + \delta^\mu_\nu L$ ($\sigma_T = +1$). On shell with $U = 0$ the effective mass is the mass, $m = M = -5$; `rho_witness` is $\rho = -T^{x_4}{}_{x_4}$.

```python
pressures = [sp.expand(T_witness[mu][mu].subs(on_shell)) for mu in range(8) if mu != 4]
check(sp.expand(sum(diagonal) - (-5) * S_family) == 0
      and sp.expand(rho_witness - (-5) * S_family) == 0
      and all(p == 0 for p in pressures),
      "witness: trace K = M S, rho = M S, all seven pressures 0 (pressureless)")
check(sp.expand(d(rho_witness, 4) + 3 * ad1 * rho_witness) == 0,
      "witness: d4 rho + 3 a4' rho = 0, the source is conserved on the family")
```

`pressures` lists the seven diagonal components other than $x_4$. The check: the trace of $K$ is $MS$, $\rho = MS$, and all seven pressures vanish: a pressureless source. The second check: $\partial_4\rho + 3a_4'\rho = 0$ (the function `d` of In [4] differentiates the symbol `ea` with its rate); this is the energy exchange of Section 12.10 with zero pressures and $h = 0$, so the source is conserved on every history of the family. Out [12] shows two PASS lines.

**In [13], can a witness be the source of a history of its family?**

```python
record = read_json(EQUATIONS)
kk, k0, Lam, y = sp.symbols("kk k0 Lam y", real=True)  # y stands for a4'^2
a1, a2, a3 = sp.symbols("alpha1 alpha2 alpha3", real=True)
LOCALS = {"H": H, "ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk}
lovelock = record["lovelockTensors"]
weights = {1: a1, 2: a2, 3: a3}
```

The equations are read again; new symbols: `kk`, the constant `k0`, `Lam`, and `y`, which stands for $(a_4')^2$; the couplings `a1`, `a2`, `a3`; the names of the record's variables.

```python
side = {key: sum(weights[k] * sp.sympify(lovelock[f"E{k}"][key]["input"]
                                         .replace("^", "**"), locals=LOCALS)
                 for k in (1, 2, 3)) for key in ("x4x4", "x1x1", "x0x0")}
FAMILY = {uu: 2 * ad1, vv: 2 * ad2, kk: k0}  # b4 = e^(2 a4)/k0
EINSTEIN = {a1: 1, a2: 0, a3: 0}
AUTHOR = {a1: 1, a2: sp.Rational(1, 32) / H ** 2, a3: sp.Rational(1, 1152) / H ** 4}
```

`side` holds the three components $\sum_k\alpha_kE_{(k)}$ from the record. `FAMILY` inserts $u = 2a_4'$, $v = 2a_4''$, $k = k_0$; `EINSTEIN` and `AUTHOR` are the two sets of couplings (the author's with $H$ kept as a symbol).

```python
def on_family(key, couplings):
    return sp.expand(side[key].subs(FAMILY).subs(couplings))
```

`on_family(key, couplings)` is a component on the family for given couplings.

```python
def eliminant(couplings):
    x1_eq = on_family("x1x1", couplings) + Lam
    x0_eq = on_family("x0x0", couplings) + Lam
    return sp.expand(sp.diff(x0_eq, ad2) * x1_eq - sp.diff(x1_eq, ad2) * x0_eq)
```

`eliminant(couplings)` is the polynomial $P$ of Section 12.26: the 3-space equation $e_{11} + \Lambda$ times the coefficient of $a_4''$ in the block equation, minus the block equation times the coefficient of $a_4''$ in the 3-space equation; $a_4''$ drops out.

```python
e44, e11, e00 = (on_family(key, EINSTEIN) for key in ("x4x4", "x1x1", "x0x0"))
say(f"Einstein on the family: e44 = {e44}, e11 = {e11}, e00 = {e00}")
P_einstein = eliminant(EINSTEIN)
y_value = sp.solve(P_einstein.subs(ad1 ** 2, y), y)[0]  # a4'^2: a constant
Lam_value = sp.solve((e11 + Lam).subs({ad2: 0, ad1 ** 2: y_value}), Lam)[0]
final = sp.expand(y_value.subs(Lam, Lam_value))
```

The three Einstein components on the family are printed (Out [13]): $e_{44} = 6H^2k_0 - 3(a_4')^2$, $e_{11} = 6H^2k_0 - 3(a_4')^2 - 2a_4''$, $e_{00} = 3H^2k_0 - 6(a_4')^2 - 3a_4''$. `P_einstein` is the eliminant, `y_value` the value of $(a_4')^2$ at which it vanishes (sympy solves for `y` after `ad1**2` is replaced by `y`), `Lam_value` the $\Lambda$ at which the 3-space equation then holds with $a_4'' = 0$, and `final` the value of $(a_4')^2$ with that $\Lambda$.

```python
say(f"Einstein: P = {P_einstein}, so a4'^2 = {y_value} is constant and a4'' = 0; "
    f"the 3-space equation then needs Lambda = {Lam_value}, and a4'^2 = {final}")
check(not P_einstein.has(ad2) and final == -H ** 2 * k0,
      "Einstein: no history b4 = e^(2 a4)/k0 has zero pressures (a4'^2 = -H^2 k0)")
P_author = eliminant(AUTHOR)
c4, c2, c0 = (P_author.coeff(ad1, n) for n in (4, 2, 0))
```

The cell prints the eliminant `P = -12*H**2*k0 - Lam - 3*ad1**2`, the constant value `-4*H**2*k0 - Lam/3` of $(a_4')^2$ (so $a_4'' = 0$), the value `Lambda = -9*H**2*k0` that the 3-space equation then needs, and the resulting $(a_4')^2$ = `-H**2*k0`: the hand computation of Section 12.26. The check requires the last value. Then the author's couplings: `P_author` and its coefficients of $(a_4')^4$, $(a_4')^2$ and $(a_4')^0$.

```python
shape = (not P_author.has(ad2) and sp.Poly(P_author, ad1).degree() == 4
         and P_author.coeff(ad1, 3) == 0 and P_author.coeff(ad1, 1) == 0)
say(f"the author's couplings: c4 = {sp.factor(c4)}")
say(f"c2 = {sp.factor(c2)}")
say(f"c0 = {sp.factor(c0)}")
zeros_c4 = sp.solve(c4, k0)
```

`shape` checks that $P$ contains no $a_4''$ and is a polynomial of degree 4 in $a_4'$ with no odd powers. The three coefficients are printed factorised: $c_4 = -3(k_0 - 2)(k_0^2 - 12k_0 + 16)/(256H^2)$, and $c_2$, $c_0$, which contain $\Lambda$. `zeros_c4` are the values of $k_0$ at which $c_4 = 0$.

```python
say(f"c4 = 0 at k0 = {zeros_c4}")
degenerate = len(zeros_c4) == 3
for root in zeros_c4:
    c2_root = sp.simplify(c2.subs(k0, root))
    if not c2_root.has(Lam):
        say(f"k0 = {root}: c2 = {c2_root}, so P is not the zero polynomial")
        degenerate = degenerate and c2_root != 0
        continue
    Lam_root = sp.radsimp(sp.solve(c2_root, Lam)[0])  # c2 = 0 fixes Lambda
    c0_root = sp.simplify(sp.expand(c0.subs({k0: root, Lam: Lam_root})))
    time_eq = sp.simplify(sp.expand(on_family("x4x4", AUTHOR).subs(k0, root)
                                    + Lam_root))
    space_eq = sp.simplify(sp.expand(on_family("x1x1", AUTHOR).subs(k0, root)
                                     + Lam_root))
    say(f"k0 = {root}: c2 = 0 needs Lambda = {Lam_root}; there c0 = {c0_root}, "
        f"e44 + Lambda = {time_eq}, e11 + Lambda = {space_eq}")
    degenerate = (degenerate and c0_root == 0 and time_eq == 0 and space_eq == 0
                  and sp.simplify(Lam_root + sp.Rational(3, 2) * H ** 2 * (root + 4))
                  == 0)
```

They are printed: `[2, 6 - 2*sqrt(5), 2*sqrt(5) + 6]` (the roots of $k_0^2 - 12k_0 + 16$ are $6 \pm\sqrt{36 - 16} = 6 \pm 2\sqrt5$). For each root: if $c_2$ does not contain $\Lambda$ there, $P$ cannot be the zero polynomial unless $c_2 = 0$ (at $k_0 = 2$ the cell prints $c_2 = 3/16$); otherwise $c_2 = 0$ fixes $\Lambda$ (`sp.radsimp` removes roots from denominators), and the cell computes $c_0$, $e_{44} + \Lambda$ and $e_{11} + \Lambda$ there and prints them: at $k_0 = 6 \mp 2\sqrt5$, $\Lambda = (-15 \pm 3\sqrt5)H^2$, and all three vanish. `degenerate` collects these findings and also requires $\Lambda = -\tfrac32H^2(k_0 + 4)$.

```python
check(shape and degenerate, "the author's couplings: P = 0 identically only at "
      "k0 = 6 +- 2 sqrt 5, Lambda = -(3/2) H^2 (k0 + 4), where e44 + Lambda = 0")
equal = all(sp.expand((on_family("x4x4", couplings) - on_family("x1x1", couplings))
                      .subs(ad2, 0)) == 0 for couplings in (EINSTEIN, AUTHOR))
check(equal, "Einstein and the author's couplings: e44 = e11 where a4'' = 0 on the "
      "family (beta = 2 or static), so kappa M S = 0 there")
```

The two checks: $P$ vanishes identically only at $k_0 = 6 \pm 2\sqrt5$ with $\Lambda = -\tfrac32H^2(k_0 + 4)$, where $e_{44} + \Lambda = 0$; and in both theories $e_{44} = e_{11}$ where $a_4'' = 0$ on the family, so the difference of the time and the 3-space equations gives $\kappa MS = 0$ there. Together they prove the statement of Section 12.26. Out [13] shows the printed lines and three PASS lines.

**In [14], figure 12d.3: a witness in time.**

```python
phi_numbers = np.array([complex(entry) for entry in phi_one])
C_numbers = np.array(C.tolist(), dtype=float)
biggest = int(np.argmax(np.abs(phi_numbers)))  # the largest component (first one)
times = np.linspace(0.0, 3.0, 601)  # x4 in units 1/H
S0_one = float(S0_s.subs(s, 1))
density = []
```

The 16 entries of $\Phi_0(1)$ as complex floating-point numbers, $C$ as a numpy array, the index of the largest entry (`np.argmax` of the absolute values; it is the first entry), 601 times from 0 to 3, and $\Phi_0^\dagger C\Phi_0$ at $s = 1$ as a number.

```python
for x_value in times:  # S from the numbers, at every time
    phi_x = 4.0 * np.exp(-1.5 * x_value) * np.exp(-4j * x_value) * phi_numbers
    density.append((phi_x.conj() @ C_numbers @ phi_x).real)
density = np.array(density)
check(np.allclose(density, 16.0 * np.exp(-3.0 * times) * S0_one, rtol=1e-12,
                  atol=0.0), "witness on a4 = x4: S(x4) = 16 e^(-3 x4) S0 numerically")
```

For every time the spinor $\Phi(x_4) = 4e^{-3x_4/2}e^{-4ix_4}\Phi_0(1)$ on the history $a_4 = x_4$, $b_4 = e^{2x_4}/4$ (then $e^{a_4/2}b_4^{-1} = 4e^{-3x_4/2}$; `4j` is the imaginary number $4i$), and its density $\Phi^\dagger C\Phi$ (`@` is the matrix product, `.conj()` the complex conjugate). The check: the density equals $16e^{-3x_4}\Phi_0^\dagger C\Phi_0$ to rounding at all 601 times.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
component = 4.0 * np.exp(-1.5 * times) * np.exp(-4j * times) * phi_numbers[biggest]
left.plot(times, component.real, label=f"Re $\\Phi_{{{biggest + 1}}}$")
left.plot(times, component.imag, "--", label=f"Im $\\Phi_{{{biggest + 1}}}$")
left.plot(times, density / abs(S0_one), color="black", linewidth=2.0,
          label="$S/|\\Phi_0^\\dagger C\\Phi_0|$")
```

Two panels. Left: the real and imaginary parts of the largest component (the label `Phi_{1}` is built with doubled braces in the f-string) and the density divided by $|\Phi_0^\dagger C\Phi_0|$, thick and black.

```python
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("value")
left.set_title("the witness oscillates and decays")
left.legend(fontsize=8)
right.semilogy(times, np.exp(times), color="tab:orange", label="3-space $e^{a_4}$")
right.semilogy(times, 0.5 * np.ones_like(times), "--", color="tab:blue",
               label="block $e^{-a_4}b_4^{1/2} = 1/2$")
```

Labels, title and legend of the left panel; on the right, on a logarithmic axis, the 3-space factor $e^{x_4}$ and the constant block factor $\tfrac12$.

```python
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("scale factor")
right.set_title("on its history the block does not shrink")
right.legend(fontsize=8)
save_figure(fig, "witness_in_time",
            "A witness of the record on the history $a_4 = Hx_4$, "
...)
```

Labels, title and legend of the right panel, and `save_figure` (caption under figure 12d.3). The components oscillate with the period $2\pi/4$ and decay like $e^{-3x_4/2}$; the block does not shrink.

**In [15], figure 12d.4: the field equations fail.**

```python
member = {ad1: 1, ad2: 0, H: 1, k0: 4}  # a4 = x4 on the family with k0 = 4
G_member = {key: sp.expand(side[key].subs(FAMILY).subs(EINSTEIN).subs(member))
            for key in ("x4x4", "x1x1", "x0x0")}
LAMBDA_MEMBER = -21  # makes the 3-space equation hold
G_diag = [G_member["x0x0"]] + [G_member["x1x1"]] * 3 + [G_member["x4x4"]] \
    + [G_member["x0x0"]] * 3
```

`member` is the history $a_4 = x_4$ ($a_4' = 1$, $a_4'' = 0$) on the family with $k_0 = 4$ and $H = 1$. `G_member` holds the three Einstein components there: $e_{44} = 3 + 24 - 6 = 21$, $e_{11} = -3 + 24 = 21$, $e_{00} = -6 + 12 = 6$. $\Lambda = -21$ makes the 3-space equation hold. `G_diag` lists the eight diagonal entries in the order $x_0, \dots, x_7$ (the backslash continues the statement on the next line).

```python
left_side = np.array([[float(G_diag[mu] + LAMBDA_MEMBER) if mu == nu else 0.0
                       for nu in range(8)] for mu in range(8)])
right_side = np.zeros((8, 8))  # p3 = p0 = p_t = 0 for a witness
right_side[4, 4] = -1.0  # -kappa rho with kappa M S = 1 at the moment drawn
difference = left_side - right_side
say(f"G + Lambda on the diagonal: {[float(v) for v in np.diag(left_side)]}")
```

`left_side` is the 8 by 8 array of $G^\mu{}_\nu + \Lambda\delta^\mu_\nu$; `right_side` is $\kappa T^\mu{}_\nu$ of a witness, pressureless, with $-\kappa\rho = -\kappa MS$ drawn as $-1$ at the moment shown; `difference` is their difference. The diagonal of the left side is printed (Out [15]): `[-15.0, 0.0, 0.0, 0.0, 0.0, -15.0, -15.0, -15.0]`.

```python
check(np.allclose(np.diag(difference)[[0, 5, 6, 7]], -15.0)
      and np.allclose(np.diag(difference)[[1, 2, 3]], 0.0),
      "a4 = x4, k0 = 4, Lambda = -21: the block components miss by -15")
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.4))
scale = 22.0
panels = ((left_side, "$G^\\mu{}_\\nu + \\Lambda\\delta^\\mu_\\nu$"),
          (right_side, "$\\kappa T^\\mu{}_\\nu$ of a witness"),
          (difference, "difference"))
```

The check: the four block components miss by $-15$, the 3-space components agree. Then a figure of three panels, a common colour scale of $\pm22$, and the three arrays with their titles.

```python
for ax, (values, title) in zip(axes, panels):
    ax.imshow(values, cmap="RdBu_r", vmin=-scale, vmax=scale)
    for mu in range(8):
        value = values[mu, mu]
        ink = "white" if abs(value) > 0.6 * scale else "black"  # readable on dark
        ax.text(mu, mu, f"{value:.0f}", ha="center", va="center", fontsize=7,
                color=ink)
    ax.set_xticks(range(8))
    ax.set_xticklabels(NAMES, fontsize=7)
    ax.set_yticks(range(8))
    ax.set_yticklabels(NAMES, fontsize=7)
    ax.grid(False)
    ax.set_title(title, fontsize=9)
```

For each panel the array is drawn as a heat map with the diagonal values written into their squares (no decimals, `:.0f`), and the tick labels, no grid and the title are set, as in figure 12a.3.

```python
fig.suptitle("Einstein gravity, $a_4 = Hx_4$, $b_4 = e^{2Hx_4}/4$: a witness is not "
             "the source")
save_figure(fig, "tensor_mismatch",
            "Einstein gravity on the member $a_4 = Hx_4$, $b_4 = e^{2Hx_4}/4$ of the "
...)
```

A title over the panels and `save_figure` (caption under figure 12d.4). The time component would need $\kappa MS = 0$, and the block components cannot be matched at all.

**In [16], figure 12d.5: what the history needs and what a witness supplies.**

```python
required_rho = float(-(G_member["x4x4"] + LAMBDA_MEMBER))
required_p0 = float(G_member["x0x0"] + LAMBDA_MEMBER)
report("member a4 = x4, k0 = 4, Lambda = -21: required kappa rho, kappa p0",
       f"{required_rho:g}, {required_p0:g}")
fig, ax = plt.subplots()
ax.plot(times, required_rho * np.ones_like(times), color="black",
        label=f"required $\\kappa\\rho = {required_rho:g}$ (constant)")
```

The energy density the member requires, $\kappa\rho = -(e_{44} + \Lambda) = 0$, and the block pressure, $\kappa p_0 = e_{00} + \Lambda = -15$, are printed as a RESULT line (Out [16]): `0, -15`. A figure with the required energy density as a black horizontal line.

```python
for scale_value, style in ((1.0, "--"), (5.0, ":")):
    ax.plot(times, scale_value * np.exp(-3.0 * times), style, color="tab:blue",
            label=f"witness $\\kappa\\rho = \\kappa MS$, "
            f"$\\kappa MS(0) = {scale_value:g}$")
ax.plot(times, required_p0 * np.ones_like(times) / 5.0, "-.", color="tab:red",
        label="required $\\kappa p_0/5 = -3$ (witness: $0$)")
```

A witness supplies $\kappa\rho = \kappa MS \propto e^{-3x_4}$, drawn for two starting values (dashed and dotted); the required block pressure, divided by 5 to fit the scale, as a red dash-dotted line.

```python
ax.axhline(0.0, color="grey", linewidth=0.8)
ax.set_xlabel("time $x_4$ (units $1/H$)")
ax.set_ylabel("units $H^2$")
ax.set_title("What the history needs and what a witness supplies")
ax.legend(fontsize=8)
save_figure(fig, "witness_versus_required",
            "Einstein gravity on the member $a_4 = Hx_4$, $b_4 = e^{2Hx_4}/4$ of the "
...)
```

A line at zero, labels, title, legend and `save_figure` (caption under figure 12d.5). A constant requirement and a falling supply can agree at most at one moment.

**In [17], figure 12d.6: where witnesses of the record's form exist.**

```python
more = []  # (M, c, k0, w, the witness works)
for M_value, c_value in ((5, 4), (13, 5), (13, 12)):
    spaces_m, p1, p2, c_m, w_m, B_m = witness_parts(M_value, c_value)
    phi_m = (p1 + c_m * p2).applyfunc(sp.expand)
    works = ([len(space) for space in spaces_m] == [1, 1]
             and (B_m * phi_m + sp.I * w_m * phi_m).applyfunc(sp.expand)
             == sp.zeros(16, 1)
             and all(bilinear(phi_m, three_gamma(tr)) == 0 for tr in NEEDED)
             and bilinear(phi_m, I16) != 0)
    k0_m = sp.Rational(4, 9) * c_value ** 2  # c = (3/2) sqrt(k0) at H = 1
    more.append((M_value, c_value, k0_m, w_m, works))
    say(f"M = {M_value}, c = {c_value} (k0 = {k0_m}): w = {w_m}, witness: {works}")
```

The recipe of In [8] at three more pairs $(M, c) = (5, 4)$, $(13, 5)$ and $(13, 12)$, chosen so that $w = \sqrt{M^2 - c^2}$ is an integer (3, 12 and 5) and the arithmetic stays exact. For each, `works` requires one-dimensional null spaces, the eigenvalue $-iw$, the 24 bilinears zero and $S \ne 0$; `k0_m` is $k_0 = \tfrac49c^2$ (from $c = \tfrac32\sqrt{k_0}$ at $H = 1$). The cell prints (Out [17]) `M = 5, c = 4 (k0 = 64/9): w = 3, witness: True` and the two other lines.

```python
check(all(entry[4] for entry in more),
      "(M, c) = (5, 4), (13, 5), (13, 12): witnesses, 24 bilinears 0, S not 0")
k_values = np.linspace(0.0, 80.0, 801)
fig, ax = plt.subplots()
for mass, style in ((3.75, ":"), (5.0, "-"), (13.0, "--")):
    frequency = np.sqrt(np.maximum(mass ** 2 - 2.25 * k_values, 0.0))
    ax.plot(k_values, frequency, style, label=f"$|M| = {mass:g}H$")
```

The check that all three work. Then the figure: for $|M| = 3.75$, 5 and 13 the frequency $w = \sqrt{M^2 - \tfrac94k_0}$ against $k_0$ from 0 to 80 (zero where $M^2 \le \tfrac94k_0$).

```python
ax.plot([4.0, 4.0], [4.0, 2.25], "o", color="black", label="the record's witnesses")
ax.plot([float(entry[2]) for entry in more], [float(entry[3]) for entry in more],
        "s", color="tab:red", label="witnesses of this notebook")
ax.set_xlabel("$k_0 = e^{2a_4}/b_4$ (constant)")
ax.set_ylabel("frequency $w$ (units $H$)")
ax.set_title("Where witnesses of the record's form exist")
```

The record's witnesses as black points at $k_0 = 4$ ($w = 4$ for $|M| = 5$; $w = 2.25$ for $M = 3.75$, which is the record's $(M, H) = (5, \tfrac43)$ in units of $H$); the three new witnesses as red squares; labels and title.

```python
ax.legend(fontsize=8)
save_figure(fig, "witness_frequency",
            "The frequency $w = \\sqrt{M^2 - \\frac{9}{4}H^2k_0}$ of the condensates "
...)
```

The legend and `save_figure` (caption under figure 12d.6). Every one of these histories keeps the block at the constant size $k_0^{-1/2}$.

**In [18], the last check.**

```python
figure_names = ["oscillation_threshold", "three_gamma_bilinears", "witness_in_time",
                "tensor_mismatch", "witness_versus_required", "witness_frequency"]
paths = [output_file(f"{FIGURE_FOLDER}/12d_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths), "all six figure files exist")
all_checks_passed()
```

The six figure files must exist; the last line is ALL 31 CHECKS PASSED (notebook 12d).

### 12.31 What we proved, what we computed, what we assumed

**PROVED** (exact). The table names, for each statement, the checks of the Revision record that verify it (short names of the reports as in Section 12.2) and the notebook cells of this chapter that reproduce them.

| statement | where it is verified |
| --- | --- |
| $\det g = e^{-2a_4}b_4^4\cot^2 z\,(\sin^2 z)^{1/2}$; $\sqrt{\lvert\det g\rvert}$ changes at the rate $2u - a_4'$ | Wolfram report, `sqrt_abs_det_g`; field-theory report, `sqrt_det_g`; Notebook 12a, In [4] |
| 31 nonzero Christoffel symbols, 21 distinct | field-theory report, `christoffel_count`; Notebook 12a, In [5] and In [6] |
| 112 nonzero Riemann components (28 with $a < b$, $m < n$), all sectional, free of $x_0$, polynomials in $H, a_4', a_4'', u, v, k$ | sympy report, `mixed_riemann_free_of_x0`, `mixed_riemann_only_sectional`, `riemann_entries_polynomial`; metric report, `corrected_mixed_riemann_vanish`; Notebook 12a, In [8] |
| the Einstein tensor is diagonal, with the three components of Section 12.6 | lead's Einstein report, `einstein_off_diagonal_vanish`, `einstein_isotropy`, `einstein_diagonal_x0_independent`; sympy report, `einstein_components`; Notebook 12a, In [12] |
| only three Lovelock tensors in 8 dimensions; $E_{(1)} = G$; each $E_{(k)}$ diagonal, free of $x_0$, with $E^{x_0}{}_{x_0} = E^{x_t}{}_{x_t}$, equal to the Rust GKD record; $E_{(k)}{}^h{}_h = -k!\,2^{k-1}\sum\prod K$ | Wolfram report, `P4_vanishes_pigeonhole`; sympy report, `P1_equals_minus_4_Einstein`, `P1_structure` to `P3_structure`, `P1_equals_gkd_branch_monomials` to `P3_equals_gkd_branch_monomials`; Notebook 12a, In [14] to In [17] |
| $E_{(2)}$ equals the Gauss-Bonnet tensor of Lanczos; every $E_{(k)}$ has zero divergence | Notebook 12a, In [18]; lead's Einstein report, `gauss_bonnet_diagonal`; sympy report, `E1_divergence_free` to `E3_divergence_free`; In [19] |
| the field equations have three independent components; a source must be diagonal, with $p_0 = p_t$, free of $x_0$ | Wolfram report and sympy report, `independent_components`; Notebook 12a, In [21] |
| the constraint contains no $a_4''$ and no $v$; the other two equations are linear in $(a_4'', v)$; Einstein $\det J = -3$ | sympy report, `constraint_first_order`; Wolfram report, `second_order_system_a4pp_vv`, `einstein_second_order_system`; Notebook 12a, In [22] |
| Einstein-Gauss-Bonnet: on the record history $\det J < 0$ for every $\alpha_2$ (a computation of this book) | Notebook 12a, In [24] |
| the Bianchi identity $\frac{d}{dx_4}e_{44} = 3a_4'(e_{11} - e_{44}) + 4h(e_{00} - e_{44})$; the constraint propagates; the conservation law of a general source | sympy report, `bianchi_x4`, `json_conservation`; lead's divergence report, `divergence_x4_component`, `divergence_x0_component`, `divergence_other_components_zero`; Notebook 12a, In [23] and In [25] |
| Einstein gravity: the flat member is a vacuum; no exponential history is a vacuum; the null combinations; the source of the record history violates both null energy conditions | Wolfram report, `flat_member`; sympy report, `einstein_flat_vacuum`, `einstein_no_exponential_vacuum`, `einstein_null_combinations`; Notebook 12a, In [26] |
| on exponential histories the required source is a polynomial of degree at most 2 in $k$ and contains $A$ only through $A^2$; the field equations are invariant under $x_4 \to -x_4$ | sympy report, `exponential_history_required_source`, `json_exponential_history`; Notebook 12a, In [28]; Notebook 12b, In [4] and In [7] |
| the source of the record history with the author's weights, conserved | sympy report, `author_weights_history_source`; metric report, `history_source_conserved`; Notebook 12a, In [29]; Notebook 12b, In [9] |
| Einstein gravity: no exponential history satisfies both null energy conditions (derived here from the record's null combinations) | sympy report, `json_required_source_and_null_combinations`; Notebook 12b, In [11] |
| Einstein-Gauss-Bonnet: exponential vacua only for constant $k$, with $\alpha_2 = -1/(4H^2(A^2 - k_0))$; the author's weights: none | sympy report, `egb_no_vacuum_where_k_varies`, `egb_exponential_vacuum_branches`, `author_weights_no_exponential_vacuum`; Notebook 12b, In [13] and In [15] |
| a source with equal pressures fits no exponential history in Einstein gravity, and with the author's weights only constant $k$; no condensate is the source of the record history | sympy and Wolfram reports, `condensate_source_equal_pressures`; dark-sector record, `condensate_cannot_source_history`; Notebook 12b, In [9] and In [17] |
| the gravity term, the condensate equation, $\mathcal{B}^2 = (c^2 - M^2)1$, the density law $S = e^{a_4}b_4^{-2}S_0$, the diagonal kinetic tensor, the 24 bilinears, the witnesses at $k_0 = 4$ | sympy report, `authorT16_gravity_term`, `authorT16_condensate_equation`, `authorT16_condensate_S_law`, `authorT16_condensate_kinetic_diagonal`, `authorT16_condensate_witness`; Wolfram report, `condensate_offdiagonal_are_three_gamma_bilinears`, `condensate_witness_constant_k_exact`; Notebook 12d, In [5], In [6], In [8], In [9], In [11] |
| a witness is, up to a change of $\Lambda$, a pressureless conserved source; with $S \ne 0$ it is the source of no history of its family, in Einstein gravity and with the author's couplings for every $\Lambda$ (a computation of this book, not a Revision record) | Notebook 12d, In [12] and In [13] |

**COMPUTED** (numerical, with the measured accuracy). RK4 integrations of the two equations of second order (Notebook 12c): the flat member and the record history are reproduced to $10^{-9}$ and $10^{-14}$, the constraint gap stays below $7\times10^{-9}$, and the measured convergence orders are 4.36, 4.17, 4.08 and 4.04 (In [6], In [8], In [15]); the pulse history is recovered from its source to $10^{-8}$ (In [12]); the gas of massless particles with the author's weights reaches $\det J = 0$ just after $x_4 = 0.428800$, where the record finds $0.428813$ (In [16]). The time $x_4 = 0.785131$ at which the energy density of the record history with the author's weights changes sign is the numerical root of an exact quadratic (Notebook 12b, In [9]). The smallest distance 1.3733 between the pressure ratios of the Kohn-Sham states and those of the required source is recomputed from the record's table (Notebook 12c, In [18]).

**ASSUMED.** The Einstein-Lovelock form of the field equations, with the couplings as parameters; the author's weights $w = (1, \tfrac1{32}, \tfrac1{1152})$ and $\Lambda = -10$ are the author's choice, quoted from the record. The record history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ is a PRESCRIBED background, not a solution with a known source. Every source of Notebook 12c is a prescribed test input. The sign convention $\sigma_T = +1$ of the energy-momentum tensor, the classical commuting field dirac16complex00 in Notebook 12d, and $U = 0$ for the witnesses (which costs only a change of $\Lambda$). Lovelock's theorem is quoted, not proved.

**HYPOTHESIS.** None in this chapter.

**OPEN.** Whether any field of the theory supplies, exactly, the source of a history in which the hidden direction and the extra times deflate; condensates on histories whose $k$ is not constant; the condensate sources with $M = 0$ that the author's weights allow on $\beta = 2$; the operator form of the on-shell trace identity for the quantised field dirac16complex on a whole slice (ASSUMED by the record, key `fields/dirac16complex/statement`); which couplings $\alpha_2$, $\alpha_3$ nature has, and which sign of $A$ is realised. The Kohn-Sham states of the record are not admissible sources (record `ks-source-conditions.json`; Section 12.21), so the history on which Chapters 14 to 17 compute them stays a prescribed background.

### 12.32 Exercises

**Exercise 1.** Compute $\Gamma^{x_5}{}_{x_5x_0}$, $\Gamma^{x_0}{}_{x_5x_5}$ and $\Gamma^{x_4}{}_{x_0x_0}$ by hand from the diagonal formula of Section 12.4.

*Answer.* $g_{55} = -e^{-2a_4}b_4w_z^2$ with $w_z^2 = (\sin^2 z)^{1/6}$, so $\partial_0\ln|g_{55}| = 6H\cdot\tfrac16\,\partial_z\ln\sin^2 z = 6H\cdot\tfrac16\cdot 2\cot z = 2H\cot z$ and $\partial_0 g_{55} = 2H\cot z\,g_{55}$. First symbol ($a = c = x_5$, $b = x_0$, the term with $\delta_{ac}$): $\Gamma^{x_5}{}_{x_5x_0} = \partial_0 g_{55}/(2g_{55}) = H\cot z$. Second ($b = c = x_5$, $a = x_0$, the term with $\delta_{bc}$): $\Gamma^{x_0}{}_{x_5x_5} = -\partial_0 g_{55}/(2g_{00}) = -H\cot z\,g_{55}/g_{00}$; with $g_{55}/g_{00} = -w_z^2/\cot^2 z$ this is $H\cot z\,w_z^2/\cot^2 z = H\tan z\,w_z^2$. Third ($b = c = x_0$, $a = x_4$): $\Gamma^{x_4}{}_{x_0x_0} = -\partial_4 g_{00}/(2g_{44}) = \tfrac12\partial_4 g_{00}$, and $\partial_4\ln g_{00} = -2a_4' + u = 2h$, so $\Gamma^{x_4}{}_{x_0x_0} = h\,g_{00} = h\,e^{-2a_4}b_4\cot^2 z$. Notebook 12a prints them as `H/t`, `H*t*w**2` and `-bb*(2*ad1 - uu)/(2*ea**2*t**2)` (In [6]).

**Exercise 2.** Show by hand that the sectional curvature of the plane of the hidden direction and an extra time is $K_{x_0x_5} = h^2 - H^2k$, the same as that of two extra times.

*Answer.* The definition of Section 12.5 with $a = m = x_0$, $b = n = x_5$:

$$
R^{x_0}{}_{x_5x_0x_5} = \partial_0\Gamma^{x_0}{}_{x_5x_5} - \partial_5\Gamma^{x_0}{}_{x_5x_0} + \sum_e\Gamma^{x_0}{}_{x_0e}\Gamma^e{}_{x_5x_5} - \sum_e\Gamma^{x_0}{}_{x_5e}\Gamma^e{}_{x_5x_0} .
$$

First term: $\Gamma^{x_0}{}_{x_5x_5} = H\tan z\,w_z^2$ (Exercise 1), and with $\partial_z\tan z = 1/\cos^2 z$ and $\partial_z w_z^2 = \tfrac13\cot z\,w_z^2$ the product rule gives $\partial_0\Gamma^{x_0}{}_{x_5x_5} = 6H\cdot H\big(w_z^2/\cos^2 z + \tan z\cdot\tfrac13\cot z\,w_z^2\big) = 6H^2w_z^2/\cos^2 z + 2H^2w_z^2$. Second term: 0 (nothing depends on $x_5$). Third: only $e = x_0$ and $e = x_4$ contribute, $\Gamma^{x_0}{}_{x_0x_0}\Gamma^{x_0}{}_{x_5x_5} = -\tfrac{6H}{\sin z\cos z}\cdot H\tan z\,w_z^2 = -6H^2w_z^2/\cos^2 z$ and $\Gamma^{x_0}{}_{x_0x_4}\Gamma^{x_4}{}_{x_5x_5} = h\cdot h\,g_{55}$. Fourth: only $e = x_5$, $\Gamma^{x_0}{}_{x_5x_5}\Gamma^{x_5}{}_{x_5x_0} = H\tan z\,w_z^2\cdot H\cot z = H^2w_z^2$, with the minus sign. Adding: the terms with $1/\cos^2 z$ cancel, and

$$
R^{x_0}{}_{x_5x_0x_5} = 2H^2w_z^2 + h^2g_{55} - H^2w_z^2 = H^2w_z^2 + h^2g_{55} .
$$

Raising with $g^{55} = 1/g_{55} = -e^{2a_4}/(b_4w_z^2)$: $K_{x_0x_5} = H^2w_z^2/g_{55} + h^2 = -H^2e^{2a_4}/b_4 + h^2 = h^2 - H^2k$. The angle $z$ has disappeared, as in the plane of two extra times (Section 12.5): the hidden direction belongs to the block of constant curvature $-H^2$.

**Exercise 3.** (a) Show that the Einstein energy density required by the exponential history with slope $-A$ at the time $x_4$ equals that required by the slope $A$ at the time $-x_4$ (with $a_0 = 0$, $b_4(0) = 1$). (b) Show that the energy exchange keeps its form when the time is reversed.

*Answer.* (a) By Section 12.12, $\kappa\rho = \tfrac32A^2H^2(\beta^2 - 2) - 6H^2k - \Lambda$ with $k = e^{(2 - \beta)AHx_4}$. Replacing $A$ by $-A$ and $x_4$ by $-x_4$ leaves $A^2$ unchanged and $k = e^{(2 - \beta)(-A)H(-x_4)} = e^{(2 - \beta)AHx_4}$ unchanged, so the value is the same; the same holds for $p_3$ and $p_0$. (b) Let $\tilde\rho(x_4) = \rho(-x_4)$ and likewise for the pressures, and let the reversed history have the rates $\tilde a_4'(x_4) = -a_4'(-x_4)$ and $\tilde h(x_4) = -h(-x_4)$ (each rate is a first derivative, which changes sign). Then $\partial_4\tilde\rho(x_4) = -(\partial_4\rho)(-x_4)$, and $\partial_4\tilde\rho + 3\tilde a_4'(\tilde\rho + \tilde p_3) + 4\tilde h(\tilde\rho + \tilde p_0) = -\big[\partial_4\rho + 3a_4'(\rho + p_3) + 4h(\rho + p_0)\big](-x_4) = 0$. The reversed source is conserved on the reversed history.

**Exercise 4.** Compute $E_{(3)}{}^{x_4}{}_{x_4}$ on the record history by counting, as Section 12.7 did for $E_{(2)}$.

*Answer.* $E_{(3)}{}^{x_4}{}_{x_4} = -24\sum\prod K$ over the sets of three disjoint planes among the seven directions $S = \{x_1, x_2, x_3\}$ and $T = \{x_0, x_5, x_6, x_7\}$ (six of the seven directions are used). The possible kinds, with $K = (a_4')^2$ for $SS$, $a_4'h$ for $ST$ and $D = h^2 - H^2k$ for $TT$: $SS + ST + TT$: $3\cdot 4\cdot 3 = 36$ sets (the $SS$ plane, the last 3-space direction with one of 4 block directions, and a $TT$ plane from the 3 remaining block directions); $SS + TT + TT$: $3\cdot 3 = 9$ (the $SS$ plane and a split of the four block directions into two pairs); $ST + ST + ST$: $4\cdot 3\cdot 2 = 24$ (each 3-space direction with its own block direction); $ST + ST + TT$: $3\cdot(4\cdot 3)\cdot 1 = 36$ (two 3-space directions with two block directions, and the remaining two block directions as a pair). Every other combination needs more than three 3-space or four block directions. Check: $36 + 9 + 24 + 36 = 105 = 7!/(1!\,(2!)^3\,3!)$. So

$$
E_{(3)}{}^{x_4}{}_{x_4} = -24\Big[36(a_4')^2\,a_4'h\,D + 9(a_4')^2D^2 + 24(a_4'h)^3 + 36(a_4'h)^2D\Big].
$$

On the record history ($H = 1$): $a_4' = 1$, $a_4'h = -\tfrac13$, $D = \tfrac19 - k$. The four terms are $36\cdot(-\tfrac13)(\tfrac19 - k) = -\tfrac43 + 12k$, $9(\tfrac19 - k)^2 = \tfrac19 - 2k + 9k^2$, $24\cdot(-\tfrac1{27}) = -\tfrac89$ and $36\cdot\tfrac19(\tfrac19 - k) = \tfrac49 - 4k$. Their sum is $(-\tfrac{12}9 + \tfrac19 - \tfrac89 + \tfrac49) + (12 - 2 - 4)k + 9k^2 = -\tfrac53 + 6k + 9k^2$, and times $-24$: $E_{(3)}{}^{x_4}{}_{x_4} = 40 - 144k - 216k^2$, as used in Section 12.12.

**Exercise 5.** A gas of massless particles in 3-space ($p_3 = \rho/3$, $p_0 = p_t = 0$) is started in Einstein gravity with $\Lambda = 0$ at the rates of the record history ($a_4' = H$, $u = \tfrac43H$, $b_4 = 1$, $a_4 = 0$). What energy density does the constraint require? Can it be ordinary matter?

*Answer.* The constraint gives $\kappa\rho = -(e_{44} + \Lambda) = -\big(3(a_4')^2 + 6H^2k - \tfrac32u^2\big) = -\big(3 + 6 - \tfrac32\cdot\tfrac{16}9\big)H^2 = -\big(9 - \tfrac83\big)H^2 = -\tfrac{19}3H^2$ (with $k = e^0/1 = 1$). For $\kappa > 0$ the energy density is negative, so in Einstein gravity with $\Lambda = 0$ a gas of ordinary (positive) energy cannot start with these rates; with the author's weights and $\Lambda = -10$ the same constraint gives the positive $\kappa\sigma_0 = \tfrac{193}{54}$ (Section 12.21). By Section 12.21 the gas then keeps $\rho = \sigma_0b_4^{-2}$ on every history.

**Exercise 6.** Show that in Einstein gravity no exponential history allows a source with equal pressures $p_3 = p_0$, such as a homogeneous condensate.

*Answer.* $\kappa(p_3 - p_0) = e_{11} - e_{00}$; on the history ($a_4' = AH$, $u = \beta AH$, $a_4'' = v = 0$) the components of Section 12.9 give $\big(-5 + 6\beta - \tfrac52\beta^2\big)A^2H^2 + 6H^2k - \big(-3 + \tfrac32\beta - \tfrac32\beta^2\big)A^2H^2 - 3H^2k = \big(-2 + \tfrac92\beta - \beta^2\big)A^2H^2 + 3H^2k$. It vanishes when $3k = \big(\beta^2 - \tfrac92\beta + 2\big)A^2 = (\beta - 4)(\beta - \tfrac12)A^2$. A source with equal pressures at every time needs this at every time; where $k$ changes ($\beta \ne 2$ and $A \ne 0$) that is impossible, because the left side changes and the right side does not. So $k$ is constant: either $\beta = 2$, and then $3k = (-2)(\tfrac32)A^2 = -3A^2$, $k = -A^2 < 0$; or $A = 0$, and then $k = 0$. Both contradict $k = e^{2a_4}/b_4 > 0$ (record checks `condensate_source_equal_pressures`; Notebook 12b, In [17]).

**Exercise 7.** On the family of histories $b_4 = e^{2a_4}/k_0$ with constant $k_0$ and any $a_4(x_4)$: (a) show that the block keeps a constant size; (b) show that a condensate there has $S = k_0^2e^{-3a_4}S_0$; (c) show that a pressureless source $\rho = MS$ obeys the energy exchange.

*Answer.* (a) $u = b_4'/b_4 = 2a_4'$, so $h = \tfrac12u - a_4' = 0$, and the block factor $e^{-a_4}b_4^{1/2} = e^{-a_4}e^{a_4}k_0^{-1/2} = k_0^{-1/2}$ is constant. (b) The density law of Section 12.26 gives $S = e^{a_4}b_4^{-2}S_0 = e^{a_4}k_0^2e^{-4a_4}S_0 = k_0^2e^{-3a_4}S_0$. (c) With zero pressures and $h = 0$ the energy exchange reads $\partial_4\rho + 3a_4'\rho = 0$; for $\rho = MS$ with constant $M$, $\partial_4\rho = M\partial_4S = M(-3a_4')S = -3a_4'\rho$, so it holds (Notebook 12d, In [12]).

**Exercise 8.** Evaluate the determinant of the Jacobian of Einstein-Gauss-Bonnet gravity at the start of the record history ($k = 1$) for $\alpha_2H^2 = \tfrac1{32}$, and say what its sign means.

*Answer.* With the formula of Section 12.9 at $k = 1$: $\det J = -\tfrac19\big[27 - 876\alpha_2 + 11936\alpha_2^2\big]$ ($540 + 336 = 876$; $5184 + 6048 + 704 = 11936$). With $\alpha_2 = \tfrac1{32}$: $876/32 = \tfrac{219}8$ and $11936/1024 = \tfrac{373}{32}$, so the bracket is $\tfrac{864 - 876 + 373}{32} = \tfrac{361}{32}$ and $\det J = -\tfrac{361}{288} = -1.2535$. It is negative, as the whole dash-dotted curve of figure 12a.4: the two equations of second order can be solved for $a_4''$ and $v$, and they could not where $\det J = 0$.
