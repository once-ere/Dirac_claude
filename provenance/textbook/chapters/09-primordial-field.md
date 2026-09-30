## 9. The primordial gravitational field of the notebook

### 9.1 What this chapter does

The author's notebook opens with a hypothesis. In the notebook's words (cell 6, quoted through the survey `handoff/surveys/survey_notebook-physics.md`), if superluminal inflation or deflation exists in Einstein or Einstein–Lovelock gravity, then at the time $x_4=0$, before the particles of the standard model exist, "a pair of universes with MASSES ± M is created". To express this picture the notebook writes down one particular gravitational field, the metric that it calls MatrixMetric44. In this book we call it the **primordial field**.

This chapter studies that field from zero. It is a **prescribed background**: we do not solve an equation to find the metric. We take the notebook's metric as given, compute everything about its geometry exactly, and then ask two questions. First, what would gravity need as a source in order to produce exactly this metric? Second, how does the dirac16complex field of Chapters 6 and 7 behave in it? The answer to the first question is a surprise: in 8-dimensional Einstein gravity the field needs a negative energy density, for every choice of its free function. The chapter also records three errors (errata) that the project found while checking the notebook and its own specification, and it prepares the ground for Part IV: the static member of the family of fields, the hidden coordinate $y$, and a construction with two mirror copies of the field glued along a wall, the **Z2 brane**.

The chapter uses the tools of Chapter 4 (metric, Christoffel symbols, curvature, vielbein, spin connection) and the field equations and energy–momentum tensor of Chapter 7. Every formula that the repository verifies is derived here step by step, and the name of the machine check is given in typewriter type, for example `P_metric_detG_equals_plus_cos2z`. Checks whose names begin with `P_` belong to Stage 2; they are listed in `artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json` (WolframScript, 126 of 126 checks true) and are repeated by the independent Python checker `scripts/check_dirac16complex_primordial.py` (report `python-primordial-report.json` in the same folder, 16 of 16 check groups true). Checks whose names begin with `KS_` belong to the exact theory of Stage 4, recorded in `artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json` (125 of 125 true) and `artifacts/dirac16complex/kohn-sham/python-theory-report.json` (157 of 157 true). The main text sources are `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md` (the Stage-2 document; we cite its sections as §N) and `handoff/specs/STAGE4_SPEC.md` (its §1 and the errata §7 to §9).

Conventions are those of the whole book. Everything is counted from 0. The eight coordinates are $x_0,\dots,x_7$, written with a lower index as in the notebook, and $\partial_\mu=\partial/\partial x_\mu$. The coordinate $x_0$ is the **hidden space**, $x_1,x_2,x_3$ are ordinary **3-space**, $x_4$ is the **time** in which everything evolves, and $x_5,x_6,x_7$ are the three **extra times** (the notebook calls them "superluminal deflating time"). The flat (tangent) metric is $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$. A repeated index, one up and one down, is summed from 0 to 7 unless we say "no sum". The letter $i$ always runs over $\{1,2,3\}$ and the letter $j$ over $\{5,6,7\}$.

### 9.2 The metric MatrixMetric44

**Two abbreviations.** The notebook uses one constant $H>0$, an inverse length (a number with the unit 1/length), and the two combinations

$$
z=6Hx_0,\qquad t=Hx_4 .
$$

The coordinate $x_0$ is restricted so that $0<z<\pi/2$; in this range $\sin z$, $\cos z$, $\tan z$ and $\cot z=\cos z/\sin z$ are all positive. We write $s=\sin z$. The dimensionless time $t$ is the argument of the one free function of the metric, $a_4(t)$, an arbitrary smooth real function. Its derivatives are written with primes, and **primes always mean derivatives with respect to $t$**:

$$
a_4'=\frac{da_4}{dt},\qquad a_4''=\frac{d^2a_4}{dt^2},\qquad \partial_4a_4=\frac{\partial a_4(Hx_4)}{\partial x_4}=H\,a_4' ,
$$

the last by the chain rule. In the same way $\partial_0=6H\,\partial_z$ on any function of $z$.

**The line element.** A metric is a rule that assigns a squared length $ds^2=\sum_{\mu,\nu}g_{\mu\nu}\,dx_\mu\,dx_\nu$ to a small coordinate step $(dx_0,\dots,dx_7)$ (Chapter 4). The primordial field is **diagonal**: $g_{\mu\nu}=0$ for $\mu\ne\nu$. Its line element is

$$
\begin{aligned}
ds^2={}&\cot^2z\,dx_0^2+s^{1/3}e^{2a_4}\bigl(dx_1^2+dx_2^2+dx_3^2\bigr)-dx_4^2\\
&-s^{1/3}e^{-2a_4}\bigl(dx_5^2+dx_6^2+dx_7^2\bigr),
\end{aligned}
$$

that is,

$$
g=\mathrm{diag}\bigl(\cot^2z,\ s^{1/3}e^{2a_4},\ s^{1/3}e^{2a_4},\ s^{1/3}e^{2a_4},\ -1,\ -s^{1/3}e^{-2a_4},\ -s^{1/3}e^{-2a_4},\ -s^{1/3}e^{-2a_4}\bigr),
$$

with $z=6Hx_0$, $s=\sin(6Hx_0)$ and $a_4=a_4(Hx_4)$. This is the notebook's MatrixMetric44 (Stage-2 document §4.1). The metric depends on only two of the eight coordinates, $x_0$ and $x_4$.

**Signature.** For $0<z<\pi/2$ and real $a_4$ the four entries $g_{00},g_{11},g_{22},g_{33}$ are positive and the four entries $g_{44},\dots,g_{77}$ are negative. So the metric has the same sign pattern as $\eta$: signature (4,4), four space-like and four time-like directions (check `P_metric_signature44`).

**A worked example.** Take the point where $\sin z=3/5$. Then $\cos z=4/5$ (because $\sin^2z+\cos^2z=1$), $\cot z=4/3$ and $\tan z=3/4$. Take also $a_4=0$ there. The metric at that point is

$$
g=\mathrm{diag}\bigl(\tfrac{16}{9},\ (\tfrac35)^{1/3},\ (\tfrac35)^{1/3},\ (\tfrac35)^{1/3},\ -1,\ -(\tfrac35)^{1/3},\ -(\tfrac35)^{1/3},\ -(\tfrac35)^{1/3}\bigr),\qquad (\tfrac35)^{1/3}\approx0.8434 .
$$

Four positive and four negative entries, as claimed.

**The vielbein.** A vielbein (Chapter 4) is a matrix $e_\mu{}^a$ with $g_{\mu\nu}=e_\mu{}^a\,\eta_{ab}\,e_\nu{}^b$. For a diagonal metric the simplest choice is diagonal, $e_\mu{}^a=h_\mu\,\delta_\mu^a$ (no sum), with $h_\mu^2\,\eta_{\mu\mu}=g_{\mu\mu}$. Taking positive square roots,

$$
h=\bigl(\cot z,\ s^{1/6}e^{a_4},\ s^{1/6}e^{a_4},\ s^{1/6}e^{a_4},\ 1,\ s^{1/6}e^{-a_4},\ s^{1/6}e^{-a_4},\ s^{1/6}e^{-a_4}\bigr).
$$

Check one entry of each kind: $h_0^2\eta_{00}=\cot^2z$; $h_1^2\eta_{11}=s^{1/3}e^{2a_4}$; $h_4^2\eta_{44}=-1$; $h_5^2\eta_{55}=-s^{1/3}e^{-2a_4}$. All agree with $g$ (check `P_metric_vielbeinProduct`). The inverse vielbein is $e_a{}^\mu=\mathrm{diag}(1/h_\mu)$, and the curved gamma matrices of Chapter 4, $\gamma^{x_\mu}=e_a{}^\mu\gamma^a$ (no sum over $\mu$), are

$$
\gamma^{x_0}=\tan z\,\gamma^0,\qquad \gamma^{x_i}=s^{-1/6}e^{-a_4}\gamma^i,\qquad \gamma^{x_4}=\gamma^4,\qquad \gamma^{x_j}=s^{-1/6}e^{a_4}\gamma^j .
$$

Here $\gamma^0,\dots,\gamma^7$ are the constant 16 by 16 frame matrices of Chapter 2, with $\{\gamma^a,\gamma^b\}=2\eta^{ab}$. Keep the last formula in mind: the factor $s^{-1/6}e^{+a_4}$ of the extra-time gammas is exactly where the notebook made the error of Section 9.14.

### 9.3 Determinant, volume and the first erratum

**The determinant.** The determinant of a diagonal matrix is the product of its diagonal entries. Hence

$$
\det g=\cot^2z\cdot\bigl(s^{1/3}e^{2a_4}\bigr)^3\cdot(-1)\cdot\bigl(-s^{1/3}e^{-2a_4}\bigr)^3 .
$$

Work it out factor by factor. $(s^{1/3}e^{2a_4})^3=s\,e^{6a_4}$. $(-s^{1/3}e^{-2a_4})^3=-s\,e^{-6a_4}$. The two minus signs, one from $g_{44}=-1$ and one from the cube of the extra-time factor, multiply to $+1$. The exponentials cancel, $e^{6a_4}e^{-6a_4}=1$. What is left is

$$
\det g=\cot^2z\cdot s^2=\frac{\cos^2z}{\sin^2z}\,\sin^2z=+\cos^2z,\qquad \sqrt{\lvert g\rvert}=\cos z ,
$$

where $\lvert g\rvert$ is the absolute value of $\det g$ and $\cos z>0$ on the chart. The sign is $+$ for a simple reason: there are four negative diagonal entries, an even number (checks `P_metric_detG_equals_plus_cos2z` and `P_metric_sqrtAbsDetG_cosz`).

In the worked example $\sin z=3/5$: $\det g=\tfrac{16}{9}\cdot\tfrac{9}{25}=\tfrac{16}{25}=\cos^2z$, whatever $a_4$ is.

**Erratum 1 (the determinant).** The Stage-2 specification `handoff/specs/STAGE2_SPEC.md` had written $\det g=-\cos^2z$. That is wrong; the correct value is $+\cos^2z$, and the notebook itself has it right: its stored output of cell 1060 shows the same value (check `P_metric_notebookCell1060Det`). The error did not propagate, because only $\sqrt{\lvert g\rvert}=\cos z$ enters the physics, and that is the same for both signs (Stage-2 document §4.3; the report records the discrepancy under the key `specDiscrepancy_detG`).

**Volume.** The factor $\sqrt{\lvert g\rvert}$ converts coordinate volume into proper volume (Chapter 4). Because $g_{44}=-1$, the determinant of the seven remaining directions, $x_0,x_1,x_2,x_3,x_5,x_6,x_7$, equals $-\det g$ and has absolute value $\cos^2z$ as well. So the proper 7-volume of a region of fixed coordinate size is $\cos z$ times its coordinate volume. It does not depend on $x_4$. **The 7-volume is constant in time.** Remember this fact: it is the reason why the dirac16complex field is frozen in this background (Chapter 11, experiment EXP-1).

### 9.4 Inflating 3-space and deflating extra times

A coordinate interval $\Delta x_1$ along $x_1$ has the proper length $L=\sqrt{g_{11}}\,\Delta x_1=s^{1/6}e^{a_4}\,\Delta x_1$. The number that multiplies the coordinate interval is called the **scale factor** of that direction. Its logarithmic rate of change in the time $x_4$ is the **Hubble rate** of the direction:

$$
H_1=\frac{1}{L}\frac{\partial L}{\partial x_4}=\partial_4\ln\bigl(s^{1/6}e^{a_4}\bigr)=\partial_4a_4=H\,a_4' .
$$

The same holds for $x_2$ and $x_3$. For the extra times the proper length is $\sqrt{\lvert g_{55}\rvert}\,\Delta x_5=s^{1/6}e^{-a_4}\,\Delta x_5$ and the rate is $H_5=-H\,a_4'$. So whenever $a_4'>0$, ordinary 3-space expands and the three extra times shrink at the same rate. The hidden direction does not change with time ($g_{00}$ depends on $x_0$ only).

**The notebook's example.** For $a_4=t=Hx_4$ we have $a_4'=1$: 3-space grows like $e^{Hx_4}$, exponentially, at the constant rate $H$; the notebook calls this superluminal inflation. The extra times shrink like $e^{-Hx_4}$ (deflation).

**Why the 7-volume stays constant.** The six transverse scale factors multiply to

$$
\bigl(s^{1/6}e^{a_4}\bigr)^3\bigl(s^{1/6}e^{-a_4}\bigr)^3=s ,
$$

independent of $a_4$. The inflation of 3-space is exactly compensated by the deflation of the extra times. Together with $h_0=\cot z$ this gives $\prod_{\mu\ne4}h_\mu=\cot z\cdot s=\cos z=\sqrt{\lvert g\rvert}$, the result of Section 9.3.

### 9.5 The warped form and the hidden coordinate

The coefficient $\cot^2z$ of $dx_0^2$ makes the $x_0$ direction awkward. A better coordinate measures proper distance along the hidden direction. Define

$$
\zeta=\frac{\ln\sin z}{6H} .
$$

**Step 1: the range.** For $0<z<\pi/2$, $\sin z$ runs through $(0,1)$ and $\ln\sin z$ through $(-\infty,0)$. So $\zeta\in(-\infty,0)$, and $\zeta\to0$ as $z\to\pi/2$, $\zeta\to-\infty$ as $z\to0$ (check `P_zeta_range`).

**Step 2: the differential.** By the chain rule, with $dz/dx_0=6H$,

$$
\frac{d\zeta}{dx_0}=\frac{1}{6H}\,\frac{\cos z}{\sin z}\,6H=\cot z,\qquad d\zeta=\cot z\,dx_0,\qquad d\zeta^2=\cot^2z\,dx_0^2=g_{00}\,dx_0^2 .
$$

So in the coordinate $\zeta$ the hidden direction has the coefficient 1: $\zeta$ is proper distance (check `P_zeta_gZetaZetaIsOne`).

**Step 3: the warp factor.** Exponentiating the definition gives $e^{6H\zeta}=\sin z=s$, hence $s^{1/3}=e^{2H\zeta}$ and $s^{1/6}=e^{H\zeta}$ (check `P_zeta_warpFactor`).

**Step 4: the result.** Substituting Steps 2 and 3 into the line element of Section 9.2,

$$
ds^2=d\zeta^2-dx_4^2+e^{2H\zeta}\Bigl[e^{2a_4}\bigl(dx_1^2+dx_2^2+dx_3^2\bigr)-e^{-2a_4}\bigl(dx_5^2+dx_6^2+dx_7^2\bigr)\Bigr]
$$

(check `P_zeta_warpedMetric`). This is called a **warped** metric: the six transverse directions carry a common factor $e^{2H\zeta}$, the **warp factor**, that depends on the position in the hidden direction. In the coordinates $(\zeta,x_1,\dots,x_7)$ the volume factor is $\sqrt{\lvert g\rvert}=e^{6H\zeta}$: the old value $\cos z$ divided by $d\zeta/dx_0=\cot z$, which gives $\sin z=e^{6H\zeta}$.

**Where the chart ends.** At $\zeta=0$ (that is $z=\pi/2$) the $x_0$ description breaks down: $g_{00}=\cot^2z=0$ and $\sqrt{\lvert g\rvert}=\cos z=0$ there. The $\zeta$ form of the line element is perfectly regular at $\zeta=0$; the breakdown belongs to the coordinate $x_0$, not to the geometry (Section 9.16 continues this). As $\zeta\to-\infty$ the warp factor tends to 0 and the six transverse directions shrink to nothing; we call this end the **tip**.

**Worked example.** At $\sin z=3/5$ and $H=1$: $\zeta=\tfrac16\ln0.6=-0.08514$, and $e^{2\zeta}=e^{-0.17028}=0.8434=(0.6)^{1/3}$, the transverse coefficient of the example of Section 9.2.

### 9.6 Christoffel symbols of a diagonal metric

The Christoffel symbols (Chapter 4) are

$$
\Gamma^\rho{}_{\mu\nu}=\tfrac12\,g^{\rho\sigma}\bigl(\partial_\mu g_{\nu\sigma}+\partial_\nu g_{\mu\sigma}-\partial_\sigma g_{\mu\nu}\bigr).
$$

For a diagonal metric the inverse is diagonal too, $g^{\rho\rho}=1/g_{\rho\rho}$, so only $\sigma=\rho$ survives in the sum:

$$
\Gamma^\rho{}_{\mu\nu}=\frac{1}{2g_{\rho\rho}}\bigl(\partial_\mu g_{\nu\rho}+\partial_\nu g_{\mu\rho}-\partial_\rho g_{\mu\nu}\bigr)\qquad(\text{no sum over }\rho).
$$

Each of the three terms is nonzero only when its two metric indices are equal. Going through the possible coincidences of $\rho,\mu,\nu$ gives four rules.

- (C1) $\nu=\rho$, any $\mu$: only the first term survives, $\Gamma^\rho{}_{\mu\rho}=\Gamma^\rho{}_{\rho\mu}=\partial_\mu g_{\rho\rho}/(2g_{\rho\rho})=\tfrac12\partial_\mu\ln\lvert g_{\rho\rho}\rvert$.
- (C2) $\mu=\nu\ne\rho$: only the third term survives, $\Gamma^\rho{}_{\mu\mu}=-\partial_\rho g_{\mu\mu}/(2g_{\rho\rho})$.
- (C3) $\rho,\mu,\nu$ all different: every term has two different metric indices, so $\Gamma^\rho{}_{\mu\nu}=0$.
- (C4) The symbols are symmetric, $\Gamma^\rho{}_{\mu\nu}=\Gamma^\rho{}_{\nu\mu}$, because the formula is symmetric in $\mu$ and $\nu$.

**Which derivatives exist.** In the primordial field $g_{00}$ depends on $x_0$ only, $g_{44}=-1$ is constant, and the six transverse entries depend on $x_0$ and $x_4$. Their logarithmic derivatives are all we need. With $\partial_0=6H\partial_z$, $\partial_z\ln s=\cot z$ and $\partial_4a_4=Ha_4'$:

$$
\partial_0\ln g_{ii}=\partial_0\ln\lvert g_{jj}\rvert=6H\cdot\tfrac13\cot z=2H\cot z,\qquad \partial_4\ln g_{ii}=2Ha_4',\qquad \partial_4\ln\lvert g_{jj}\rvert=-2Ha_4' ,
$$

and $\partial_0\ln g_{00}=2\,\partial_0\ln\cot z=2\cdot6H\cdot\dfrac{-1/\sin^2z}{\cot z}=-\dfrac{12H}{\sin z\cos z}$.

**The symbols one by one.** Rule (C1) with $\rho=\mu=0$: $\Gamma^0{}_{00}=\tfrac12\partial_0\ln g_{00}=-6H/(\sin z\cos z)=-6H\,s^{-1}\sec z$. Rule (C1) with $\rho=i$: $\Gamma^i{}_{0i}=\tfrac12\cdot2H\cot z=H\cot z$ and $\Gamma^i{}_{4i}=\tfrac12\cdot2Ha_4'=Ha_4'$. Rule (C1) with $\rho=j$: $\Gamma^j{}_{0j}=H\cot z$ and $\Gamma^j{}_{4j}=-Ha_4'$. Rule (C2) with $\rho=0$: $\Gamma^0{}_{ii}=-\partial_0g_{ii}/(2g_{00})=-2H\cot z\,g_{ii}/(2\cot^2z)=-H\tan z\,g_{ii}$, and in the same way $\Gamma^0{}_{jj}=-H\tan z\,g_{jj}$. Rule (C2) with $\rho=4$ and $g_{44}=-1$: $\Gamma^4{}_{ii}=\partial_4g_{ii}/2=Ha_4'\,g_{ii}$ and $\Gamma^4{}_{jj}=\partial_4g_{jj}/2=-Ha_4'\,g_{jj}$. Inserting $g_{ii}=s^{1/3}e^{2a_4}$ and $g_{jj}=-s^{1/3}e^{-2a_4}$:

| Symbol | Closed form | How many |
| --- | --- | --- |
| $\Gamma^0{}_{00}$ | $-6H\,s^{-1}\sec z$ | 1 |
| $\Gamma^0{}_{ii}$ | $-H\tan z\,s^{1/3}e^{2a_4}$ | 3 |
| $\Gamma^0{}_{jj}$ | $+H\tan z\,s^{1/3}e^{-2a_4}$ | 3 |
| $\Gamma^4{}_{ii}$ | $H\,a_4'\,s^{1/3}e^{2a_4}$ | 3 |
| $\Gamma^4{}_{jj}$ | $H\,a_4'\,s^{1/3}e^{-2a_4}$ | 3 |
| $\Gamma^i{}_{0i}=\Gamma^i{}_{i0}$ | $H\cot z$ | 6 |
| $\Gamma^i{}_{4i}=\Gamma^i{}_{i4}$ | $H\,a_4'$ | 6 |
| $\Gamma^j{}_{0j}=\Gamma^j{}_{j0}$ | $H\cot z$ | 6 |
| $\Gamma^j{}_{4j}=\Gamma^j{}_{j4}$ | $-H\,a_4'$ | 6 |

**Everything else vanishes.** Nothing depends on $x_1,\dots,x_3,x_5,\dots,x_7$, so every rule that needs such a derivative gives 0; $g_{00}$ does not depend on $x_4$, so $\Gamma^0{}_{04}=\Gamma^4{}_{00}=0$; $g_{44}$ is constant, so every symbol with $\rho=4$ from rule (C1) vanishes. The count is $1+3+3+3+3+6+6+6+6=37$ nonzero symbols out of $8^3=512$ (25 of them with $\mu\le\nu$), each with at least one index 0 or 4 (checks `P_christoffel_closedForms512` and `P_christoffel_count`; the same table is in the Stage-2 document §5).

**Worked example.** At $\sin z=3/5$, $a_4=0$, $a_4'=1$, $H=1$: $\Gamma^0{}_{00}=-6/(\tfrac35\cdot\tfrac45)=-12.5$; $\Gamma^0{}_{11}=-\tfrac34(\tfrac35)^{1/3}=-0.6325$; $\Gamma^1{}_{01}=\tfrac43$; $\Gamma^5{}_{45}=-1$.

### 9.7 Curvature of a warped metric: one lemma for everything

Curvature needs second derivatives and products of Christoffel symbols; done by brute force it is long. The primordial field, its static member (Section 9.15) and the mirror construction (Section 9.16) all have the same structure, so we prove one lemma once and use it three times.

**Curvature convention.** We use the convention of the repository (Stage-2 document §7.3):

$$
R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma},\qquad R_{\sigma\nu}=R^\rho{}_{\sigma\rho\nu},\qquad R=g^{\sigma\nu}R_{\sigma\nu} .
$$

Setting $\mu=\rho$ and renaming, the Ricci tensor is

$$
R_{\mu\nu}=\partial_\rho\Gamma^\rho{}_{\mu\nu}-\partial_\nu\Gamma^\rho{}_{\rho\mu}+\Gamma^\rho{}_{\rho\lambda}\Gamma^\lambda{}_{\mu\nu}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\rho\mu} .
$$

With this convention a round sphere has positive $R$.

**Lemma 9.1 (Ricci tensor of a metric warped over a flat plane).** Split the eight coordinates into two **base** coordinates $y_A$, $A\in\{0,4\}$, and six **fibre** coordinates $x_p$, $p\in F=\{1,2,3,5,6,7\}$. Let

$$
ds^2=\epsilon_0\,dy_0^2+\epsilon_4\,dy_4^2+\sum_{p\in F}\epsilon_p\,e^{2f_p(y_0,y_4)}\,dx_p^2,
$$

where every $\epsilon$ is a constant sign $\pm1$ and the six functions $f_p$ depend on the base coordinates only. Write $\Theta_A=\sum_{p\in F}\partial_Af_p$. Then the only nonzero components of the Ricci tensor are

$$
R_{AB}=-\sum_{p\in F}\bigl(\partial_A\partial_Bf_p+\partial_Af_p\,\partial_Bf_p\bigr),\qquad R^p{}_p=-\sum_{A\in\{0,4\}}\epsilon_A\bigl(\partial_A^2f_p+\Theta_A\,\partial_Af_p\bigr)\quad(\text{no sum over }p),
$$

and $R_{Ap}=0$, $R_{pq}=0$ for $p\ne q$.

**Proof.** *Step 1: the Christoffel symbols.* The base entries $g_{AA}=\epsilon_A$ are constant and $1/\epsilon_A=\epsilon_A$. Rules (C1) to (C4) of Section 9.6 give exactly two kinds of nonzero symbols:

$$
\Gamma^A{}_{pp}=-\frac{\partial_A g_{pp}}{2g_{AA}}=-\epsilon_A\epsilon_p\,e^{2f_p}\,\partial_Af_p,\qquad \Gamma^p{}_{Ap}=\Gamma^p{}_{pA}=\tfrac12\partial_A\ln\lvert g_{pp}\rvert=\partial_Af_p .
$$

All others vanish: $\Gamma^A{}_{BC}=0$ and $\Gamma^A{}_{Bp}=0$ because the base entries are constant; $\Gamma^p{}_{AB}=0$ because $g_{AA}$ does not depend on $x_p$; and every symbol that needs a derivative along a fibre coordinate vanishes. The contracted symbols are therefore $\Gamma^\rho{}_{\rho A}=\sum_p\partial_Af_p=\Theta_A$ and $\Gamma^\rho{}_{\rho p}=0$.

*Step 2: $R_{AB}$.* Take the four terms of the Ricci formula in order. First term: $\Gamma^\rho{}_{AB}=0$ for every $\rho$, so it is 0. Second term: $-\partial_B\Gamma^\rho{}_{\rho A}=-\partial_B\Theta_A=-\sum_p\partial_A\partial_Bf_p$. Third term: contains $\Gamma^\lambda{}_{AB}=0$. Fourth term: $\Gamma^\lambda{}_{\rho A}$ is nonzero only for $\lambda=\rho=p$, where it is $\partial_Af_p$, and then $\Gamma^\rho{}_{B\lambda}=\Gamma^p{}_{Bp}=\partial_Bf_p$; so the fourth term is $-\sum_p\partial_Bf_p\,\partial_Af_p$. Adding gives the formula for $R_{AB}$.

*Step 3: $R_{pp}$.* First term: $\partial_\rho\Gamma^\rho{}_{pp}=\sum_A\partial_A\bigl(-\epsilon_A\epsilon_pe^{2f_p}\partial_Af_p\bigr)=-\epsilon_pe^{2f_p}\sum_A\epsilon_A\bigl(\partial_A^2f_p+2(\partial_Af_p)^2\bigr)$, by the product rule. Second term: $-\partial_p\Gamma^\rho{}_{\rho p}=0$. Third term: $\Gamma^\lambda{}_{pp}$ is nonzero only for $\lambda=A$, so the term is $\sum_A\Theta_A\Gamma^A{}_{pp}=-\epsilon_pe^{2f_p}\sum_A\epsilon_A\Theta_A\partial_Af_p$. Fourth term: $-\Gamma^\rho{}_{p\lambda}\Gamma^\lambda{}_{\rho p}$ has two kinds of nonzero products, $(\rho,\lambda)=(A,p)$, giving $\Gamma^A{}_{pp}\Gamma^p{}_{Ap}$, and $(\rho,\lambda)=(p,A)$, giving $\Gamma^p{}_{pA}\Gamma^A{}_{pp}$. Each equals $-\epsilon_A\epsilon_pe^{2f_p}(\partial_Af_p)^2$, so the fourth term is $+2\epsilon_pe^{2f_p}\sum_A\epsilon_A(\partial_Af_p)^2$. In the sum the terms $\pm2(\partial_Af_p)^2$ cancel:

$$
R_{pp}=-\epsilon_p\,e^{2f_p}\sum_A\epsilon_A\bigl(\partial_A^2f_p+\Theta_A\,\partial_Af_p\bigr).
$$

Raising one index with $g^{pp}=\epsilon_pe^{-2f_p}$ (and $\epsilon_p^2=1$) gives $R^p{}_p$ as stated.

*Step 4: the rest.* For $R_{Ap}$: the first term is $\partial_p\Gamma^p{}_{Ap}=0$ (no fibre dependence), the second is 0, the third needs $\Gamma^\rho{}_{\rho p}=0$, and the fourth needs $\Gamma^q{}_{pq}$ with $q$ a fibre index, which vanishes. For $R_{pq}$ with $p\ne q$: every term needs a symbol with two different fibre indices, such as $\Gamma^A{}_{pq}$ or $\Gamma^p{}_{qA}$, and all of those vanish. $\square$

### 9.8 The Ricci scalar and the Einstein tensor of the primordial field

**Applying the lemma.** The warped form of Section 9.5 is of the lemma's type, with base coordinates $y_0=\zeta$ ($\epsilon_0=+1$) and $y_4=x_4$ ($\epsilon_4=-1$), fibre signs $\epsilon_p=+1$ for $p=1,2,3$ and $-1$ for $p=5,6,7$, and

$$
f_p=H\zeta+\sigma_p\,a_4(Hx_4),\qquad \sigma_p=+1\ (p=1,2,3),\quad \sigma_p=-1\ (p=5,6,7).
$$

The derivatives we need are

$$
\partial_\zeta f_p=H,\qquad \partial_\zeta^2f_p=0,\qquad \partial_4f_p=\sigma_pHa_4',\qquad \partial_4^2f_p=\sigma_pH^2a_4'',\qquad \partial_\zeta\partial_4f_p=0,
$$

and the two sums $\Theta_\zeta=6H$ and $\Theta_4=Ha_4'\sum_p\sigma_p=0$. The last zero, three inflating directions balanced by three deflating ones, is the constancy of the 7-volume again.

**The Ricci tensor.** From the lemma:

$$
\begin{aligned}
R_{\zeta\zeta}&=-\sum_p H^2=-6H^2,\qquad R_{44}=-\sum_p\bigl(\sigma_pH^2a_4''+H^2a_4'^2\bigr)=-6H^2a_4'^2,\\
R_{\zeta4}&=-\sum_p\bigl(0+H\cdot\sigma_pHa_4'\bigr)=0,\\
R^p{}_p&=-\bigl[(+1)(0+6H\cdot H)+(-1)(\sigma_pH^2a_4''+0)\bigr]=-6H^2+\sigma_pH^2a_4'' ,
\end{aligned}
$$

where $\sum_p\sigma_p=0$ removed the $a_4''$ term from $R_{44}$. With $g^{\zeta\zeta}=1$ and $g^{44}=-1$ the mixed components are $R^\zeta{}_\zeta=-6H^2$ and $R^4{}_4=+6H^2a_4'^2$. All off-diagonal components vanish (check `P_einstein_offDiagonalZero`), and $R_{44}=-6H^2a_4'^2$ is check `P_einstein_R44`.

**The Ricci scalar.** The trace of the mixed Ricci tensor is

$$
R=R^\zeta{}_\zeta+R^4{}_4+\sum_pR^p{}_p=-6H^2+6H^2a_4'^2-36H^2+H^2a_4''\sum_p\sigma_p=6H^2\bigl(a_4'^2-7\bigr)
$$

(check `P_einstein_ricciScalar`).

**The Einstein tensor.** $G^\mu{}_\nu=R^\mu{}_\nu-\tfrac12\delta^\mu_\nu R$, with $-\tfrac12R=3H^2(7-a_4'^2)=21H^2-3H^2a_4'^2$. Adding this to each diagonal entry of the mixed Ricci tensor:

$$
\begin{aligned}
G^\zeta{}_\zeta&=-6H^2+21H^2-3H^2a_4'^2=-3H^2\bigl(a_4'^2-5\bigr),\\
G^i{}_i&=-6H^2+H^2a_4''+21H^2-3H^2a_4'^2=H^2\bigl(15-3a_4'^2+a_4''\bigr)\qquad(i=1,2,3),\\
G^4{}_4&=6H^2a_4'^2+21H^2-3H^2a_4'^2=3H^2\bigl(7+a_4'^2\bigr),\\
G^j{}_j&=-6H^2-H^2a_4''+21H^2-3H^2a_4'^2=H^2\bigl(15-3a_4'^2-a_4''\bigr)\qquad(j=5,6,7).
\end{aligned}
$$

**Back to the $x_0$ chart.** A tensor with one upper and one lower index transforms under a change of coordinates with one factor $\partial x'/\partial x$ and one factor $\partial x/\partial x'$ (Chapter 4). The change $x_0\to\zeta$ touches only one coordinate, so the two factors are $d\zeta/dx_0$ and $dx_0/d\zeta$, whose product is 1. Hence $G^0{}_0=G^\zeta{}_\zeta$, and every mixed component above is also the mixed component in the notebook's coordinates. These closed forms are check `P_einstein_GmixedClosedForms`. The Ricci scalar equals the notebook's stored cell-583 output, and the covariant tensor $G_{\mu\nu}=g_{\mu\rho}G^\rho{}_\nu$ equals the stored cell-584 output entry by entry (checks `P_einstein_notebookCell583` and `P_einstein_notebookCell584`; Stage-2 document §15.1). The notebook computed this much correctly. Nothing here depends on $x_0$.

**A consistency test: the Bianchi identity.** Every Einstein tensor satisfies $\nabla_\mu G^\mu{}_\nu=0$ identically (Chapter 4). For a diagonal $G$ this reads $\nabla_\mu G^\mu{}_\nu=\partial_\nu G^\nu{}_\nu+\Gamma^\mu{}_{\mu\nu}G^\nu{}_\nu-\sum_\mu\Gamma^\mu{}_{\mu\nu}G^\mu{}_\mu$ (no sum over $\nu$). Test it for $\nu=4$ in the $\zeta$ chart, where $\Gamma^p{}_{p4}=\sigma_pHa_4'$, $\Gamma^\zeta{}_{\zeta4}=\Gamma^4{}_{44}=0$ and hence $\Gamma^\mu{}_{\mu4}=\Theta_4=0$:

$$
\nabla_\mu G^\mu{}_4=\partial_4\bigl[3H^2(7+a_4'^2)\bigr]-Ha_4'\sum_p\sigma_pG^p{}_p=6H^3a_4'a_4''-Ha_4'\cdot6H^2a_4''=0 ,
$$

using $\partial_4(a_4'^2)=2a_4'a_4''\,H$ and $\sum_p\sigma_pG^p{}_p=3(G^i{}_i-G^j{}_j)=6H^2a_4''$. Exercise 9.4 does $\nu=\zeta$.

**Worked example: the notebook's $a_4=t$.** Then $a_4'=1$ and $a_4''=0$, and

$$
R=-36H^2,\qquad G^\mu{}_\nu=\mathrm{diag}(12,12,12,12,24,12,12,12)\,H^2 .
$$

### 9.9 Einstein and Einstein–Lovelock field equations

**Einstein's equations in eight dimensions.** Gravity is the metric; its field equations relate the curvature of the metric to the energy and momentum of matter. In $D$ dimensions Einstein's equations read

$$
G_{\mu\nu}=\kappa\,T_{\mu\nu},\qquad G_{\mu\nu}=R_{\mu\nu}-\tfrac12g_{\mu\nu}R ,
$$

where $T_{\mu\nu}$ is the energy–momentum tensor of the matter (Chapter 7) and $\kappa>0$ is the gravitational coupling (in four dimensions $\kappa=8\pi G_N$; in eight dimensions it is a new constant, $\kappa_8$, which we simply call $\kappa$). They follow from the Einstein–Hilbert action $\tfrac1{2\kappa}\int\sqrt{\lvert g\rvert}\,R\,d^Dx$ plus the matter action, with $T_{\mu\nu}=-(2/\sqrt{\lvert g\rvert})\,\delta I_{\mathrm{matter}}/\delta g^{\mu\nu}$, the sign convention of Chapter 7; we quote this standard variational result without deriving it here. Two consequences are used below.

1. **Conservation.** The left side obeys the Bianchi identity $\nabla_\mu G^\mu{}_\nu=0$ (Section 9.8 tested it), so the equations can only be solved by a source with $\nabla_\mu T^\mu{}_\nu=0$.
2. **Trace-reversed form.** Taking the trace, $G^\mu{}_\mu=R-\tfrac D2R=-\tfrac{D-2}{2}R=\kappa T$ with $T=T^\mu{}_\mu$, so $R=-2\kappa T/(D-2)$ and, substituting back, $R_{\mu\nu}=\kappa\bigl(T_{\mu\nu}-g_{\mu\nu}T/(D-2)\bigr)$. For $D=8$ the factor is $\tfrac16$; it is the $\tfrac16$ in the evolution equations of Chapter 11.

**Why Einstein–Lovelock.** Einstein's tensor is not the only possibility. David Lovelock proved in 1971 (we quote the theorem, we do not prove it) that in $D$ dimensions the most general symmetric tensor $E^\mu{}_\nu$ that is built from the metric and its first and second derivatives only, and that is divergence-free for every metric, is a sum

$$
E^\mu{}_\nu=\sum_{k\ge0}c_k\,E_{(k)}{}^\mu{}_\nu,\qquad E_{(k)}{}^\mu{}_\nu=-\frac{1}{2^{k+1}}\,\delta^{\mu\,\alpha_1\beta_1\cdots\alpha_k\beta_k}_{\nu\,\gamma_1\delta_1\cdots\gamma_k\delta_k}\,R^{\gamma_1\delta_1}{}_{\alpha_1\beta_1}\cdots R^{\gamma_k\delta_k}{}_{\alpha_k\beta_k},
$$

with constant coefficients $c_k$. Here $R^{\gamma\delta}{}_{\alpha\beta}=g^{\delta\sigma}R^\gamma{}_{\sigma\alpha\beta}$, and the **generalized Kronecker delta** $\delta^{\mu_1\cdots\mu_n}_{\nu_1\cdots\nu_n}$ is the determinant of the $n$ by $n$ matrix whose entry in row $r$ and column $c$ is $\delta^{\mu_r}_{\nu_c}$. For $n=2$, for example, $\delta^{\mu\nu}_{\alpha\beta}=\delta^\mu_\alpha\delta^\nu_\beta-\delta^\mu_\beta\delta^\nu_\alpha$. Such a determinant is zero whenever two of its upper (or two of its lower) indices are equal, because two rows (or columns) are then equal.

**Order 0 and order 1.** For $k=0$ the formula gives $E_{(0)}{}^\mu{}_\nu=-\tfrac12\delta^\mu_\nu$: a cosmological-constant term. For $k=1$ expand the 3 by 3 determinant along its first row:

$$
\delta^{\mu\alpha\beta}_{\nu\gamma\delta}=\delta^\mu_\nu\,\delta^{\alpha\beta}_{\gamma\delta}-\delta^\mu_\gamma\,\delta^{\alpha\beta}_{\nu\delta}+\delta^\mu_\delta\,\delta^{\alpha\beta}_{\nu\gamma}.
$$

Contract with $R^{\gamma\delta}{}_{\alpha\beta}$ and use $R^{\gamma\delta}{}_{\gamma\beta}=R^\delta{}_\beta$ (the Ricci tensor with one index raised) and the antisymmetry of the curvature in each pair. The first term gives $\delta^\mu_\nu(R^{\alpha\beta}{}_{\alpha\beta}-R^{\beta\alpha}{}_{\alpha\beta})=2R\,\delta^\mu_\nu$. The second gives $-(R^{\mu\delta}{}_{\nu\delta}-R^{\mu\delta}{}_{\delta\nu})=-2R^\mu{}_\nu$. The third gives $R^{\gamma\mu}{}_{\nu\gamma}-R^{\gamma\mu}{}_{\gamma\nu}=-2R^\mu{}_\nu$. Altogether

$$
E_{(1)}{}^\mu{}_\nu=-\tfrac14\bigl(2R\,\delta^\mu_\nu-4R^\mu{}_\nu\bigr)=R^\mu{}_\nu-\tfrac12\delta^\mu_\nu R=G^\mu{}_\nu :
$$

the order-1 Lovelock tensor is Einstein's tensor.

**Higher orders.** For $k=2$ the tensor is quadratic in the curvature; it comes from the Lagrangian $L_2=R^2-4R_{\mu\nu}R^{\mu\nu}+R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$, called the **Gauss–Bonnet** combination. It is the value of $\tfrac14\delta^{\mu_1\nu_1\mu_2\nu_2}_{\alpha_1\beta_1\alpha_2\beta_2}R^{\alpha_1\beta_1}{}_{\mu_1\nu_1}R^{\alpha_2\beta_2}{}_{\mu_2\nu_2}$; the 24 permutations in the determinant fall into three families: the 4 that keep the two index pairs separate give $4R^2$, the 4 that exchange the pairs give $4R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$, and each of the 16 that mix the pairs gives $-R^\mu{}_\nu R^\nu{}_\mu$ (Exercise 9.6 checks one of them). For $k=3$ the tensor is cubic. The generalized delta in $E_{(k)}$ has $2k+1$ upper indices; in $D$ dimensions two of them must coincide when $2k+1>D$, and then the delta is zero. So in $D=8$ only $k=0,1,2,3$ can contribute. This is the notebook's count "$m-1=8/2-1=3$" (cell 14, quoted from the survey `handoff/surveys/survey_notebook-physics.md`).

**The notebook's plan and what was done.** The notebook (cell 14) writes the vacuum Einstein–Lovelock equations as $0=-\Lambda+H^{-2}w_1\,\mathrm{Lovelock1}+H^{-4}w_2\,\mathrm{Lovelock2}+H^{-6}w_3\,\mathrm{Lovelock3}$ with pure numbers $w_1,w_2,w_3,\Lambda$. The powers of $H$ are there because $E_{(k)}$ has the unit $1/\mathrm{length}^{2k}$; the notebook calls $H$ "a fundamental inverse length" that exists because the Lovelock tensors have different units. According to the survey, **no code in the notebook defines Lovelock2 or Lovelock3**; its curvature code stops at the Einstein tensor (cells 583 and 584). The project does not compute them either (Stage-2 document §1, non-claim 4, and §20). Everything below uses **8-dimensional Einstein gravity only**, $c_1=1$ and all other $c_k=0$. What the order-2 and order-3 terms would change is an open problem (Chapter 18).

### 9.10 The source the field requires

Suppose the primordial field is produced by some matter through $G^\mu{}_\nu=\kappa T^\mu{}_\nu$. Then the matter must have $T^\mu{}_\nu=G^\mu{}_\nu/\kappa$. We read off its **energy density** and **pressures** for the observer who moves along $x_4$ (Chapter 7): $\rho=T_{44}=-T^4{}_4$ (because $g_{44}=-1$) and $p_{(\mu)}=T^\mu{}_\mu$ (no sum) for each of the seven transverse directions $\mu\ne4$. From Section 9.8:

$$
\begin{aligned}
\rho_{\mathrm{req}}&=-\frac{3H^2\bigl(7+a_4'^2\bigr)}{\kappa}, &\qquad p_{(0)}&=-\frac{3H^2\bigl(a_4'^2-5\bigr)}{\kappa},\\
p_{(1,2,3)}&=\frac{H^2\bigl(15-3a_4'^2+a_4''\bigr)}{\kappa}, &\qquad p_{(5,6,7)}&=\frac{H^2\bigl(15-3a_4'^2-a_4''\bigr)}{\kappa}
\end{aligned}
$$

(checks `P_einstein_requiredSource` and `P_einstein_rhoRequiredNegative`). Since $a_4'^2\ge0$,

$$
\rho_{\mathrm{req}}\le-\frac{21H^2}{\kappa}<0\qquad\text{for every function }a_4 .
$$

**The primordial field needs a negative energy density.** This is the main physical fact of the chapter, and it does not depend on any choice.

**Not a vacuum and not a cosmological constant.** A vacuum solution would need $G^\mu{}_\nu=0$, impossible because $G^4{}_4=3H^2(7+a_4'^2)>0$. A pure cosmological constant would need $G^\mu{}_\nu=-\Lambda\,\delta^\mu_\nu$, all eight diagonal entries equal; already $G^0{}_0=G^4{}_4$ would require $-3H^2(a_4'^2-5)=3H^2(7+a_4'^2)$, that is $-a_4'^2+5=7+a_4'^2$, that is $a_4'^2=-1$, impossible for real $a_4$ (Stage-2 document §3). So the notebook's hope, recorded in its cell 23 (survey), that the source tensor of its spinor field be $\Lambda g$ cannot be realized in Einstein gravity.

**Linear $a_4$.** If $a_4''=0$, so that $a_4=c\,t$ plus a constant, all seven pressures coincide, $p=H^2(15-3c^2)/\kappa$, and the equation of state $w=p/\rho$ is

$$
w=\frac{H^2(15-3c^2)}{-3H^2(7+c^2)}=\frac{c^2-5}{c^2+7}.
$$

For the notebook's $a_4=t$ ($c=1$): $\rho_{\mathrm{req}}=-24H^2/\kappa$, $p=12H^2/\kappa$ in all seven directions, $w=-\tfrac12$ (check `P_a4linear_values`). Note that $w<0$ here comes from $\rho<0$ with $p>0$, not from a negative pressure; the usual reading of $w$ (for example "$w<-1/3$ means acceleration") does not carry over.

**The slopes of the notebook's cell 150.** Cell 150 of the notebook lists, without derivation, the slopes $a_4'=\tfrac23(M-1)$ and $a_4'=\tfrac23(M+1)$ with $a_4''=0$ (survey). Write both as $a_4'=\tfrac23(M\mp1)$. Then $a_4'^2=\tfrac49(M\mp1)^2$ and

$$
\kappa\,\rho_{\mathrm{req}}=-3H^2\Bigl(7+\tfrac49(M\mp1)^2\Bigr)=-\tfrac13H^2\bigl(4M^2\mp8M+67\bigr)=-\tfrac13H^2\bigl(4(M\mp1)^2+63\bigr)<0
$$

for every real $M$ (check `P_a4linear_cell150AlternativesRhoNegative`).

**A picture.** Experiment EXP-1 of Stage 3 (Chapter 11) used a smooth window for $a_4'(t)$, rising from 0 to a plateau $A$ and falling back, and recorded $\rho_{\mathrm{req}}$ along the way. On the plateau $A=1$ the formula gives $-24$ and on $A=2$ it gives $-3(7+4)=-33$ (units $H=\kappa=1$); outside the window $-21$. The committed summary `artifacts/dirac16complex/numerics/exp1/summary.json` records the largest value over the whole run, $-21.000000000113$, still negative.

![EXP-1 background and Einstein requirement, from Stage 3. (a) the window $a_4'(t)$ for plateaus $A=1$ and $A=2$; (b) the 3-space factor $e^{a_4}$, the extra-time factor $e^{-a_4}$ and the constant 7-volume; (c) the required energy density $\rho_{\mathrm{req}}$ (between $-21$ and $-24$ for $A=1$, between $-21$ and $-33$ for $A=2$) beside the positive energy density of a free dirac16complex mode; (d) $w_{\mathrm{req}}=\bar p_{\mathrm{req}}/\rho_{\mathrm{req}}$.](artifacts/dirac16complex/numerics/figures/exp1_einstein_requirement.png)

### 9.11 Energy conditions

An **energy condition** is an inequality that ordinary matter is expected to satisfy. We evaluate them in the orthonormal frame of the vielbein, where the metric is $\eta$ and the components of $T$ are $T_{\hat4\hat4}=\rho$, $T_{\hat\mu\hat\mu}=p_{(\mu)}$ for a space-like $\mu\in\{0,1,2,3\}$ and $T_{\hat\mu\hat\mu}=-p_{(\mu)}$ for a time-like $\mu\in\{5,6,7\}$ (because $\eta_{\mu\mu}=-1$ there).

- **Weak energy condition (WEC)**: $T(u,u)\ge0$ for time-like $u$; for $u=e_4$ it is $\rho\ge0$.
- **Null energy condition (NEC)**: $T(k,k)\ge0$ for every null vector $k$ (one with $\eta(k,k)=0$). A null vector is formed from one time-like and one space-like frame vector, for example $k=e_4+e_0$, since $\eta(k,k)=-1+1=0$. Then $T(k,k)=T_{\hat4\hat4}+T_{\hat0\hat0}=\rho+p_{(0)}$. With a time-like $e_j$ instead of $e_4$, $T(e_j+e_0,e_j+e_0)=-p_{(j)}+p_{(0)}$.
- **Strong energy condition (SEC)**: in $D$ dimensions, $\bigl(T_{\mu\nu}-g_{\mu\nu}T/(D-2)\bigr)u^\mu u^\nu\ge0$; by the trace-reversed Einstein equations of Section 9.9 this is $R_{\mu\nu}u^\mu u^\nu\ge0$ (time-like convergence).
- **Dominant energy condition (DEC)**: WEC plus the requirement that energy does not flow faster than light; it needs $\rho\ge0$ in particular.

Inserting the required source:

| Condition | Quantity | Status |
| --- | --- | --- |
| WEC | $\rho=-\tfrac{3H^2}{\kappa}\bigl(7+a_4'^2\bigr)$ | violated for every $a_4$ |
| NEC, $k=e_4+e_0$ | $\rho+p_{(0)}=-\tfrac{6H^2}{\kappa}\bigl(1+a_4'^2\bigr)$ | violated for every $a_4$ |
| NEC, $k=e_4+e_i$ | $\rho+p_{(i)}=-\tfrac{H^2}{\kappa}\bigl(6+6a_4'^2-a_4''\bigr)$ | violated unless $a_4''\ge6(1+a_4'^2)$ |
| NEC, $k=e_j+e_0$ | $p_{(0)}-p_{(j)}=\tfrac{H^2}{\kappa}a_4''$ | holds if and only if $a_4''\ge0$ |
| NEC, $k=e_j+e_i$ | $p_{(i)}-p_{(j)}=\tfrac{2H^2}{\kappa}a_4''$ | holds if and only if $a_4''\ge0$ |
| SEC, $u=e_4$ | $R_{44}=-6H^2a_4'^2$ | violated whenever $a_4'\ne0$ |
| DEC | needs $\rho\ge0$ | violated |

Each line is two or three lines of algebra; for example $\rho+p_{(0)}=\tfrac{H^2}{\kappa}\bigl[-21-3a_4'^2-3a_4'^2+15\bigr]=-\tfrac{6H^2}{\kappa}(1+a_4'^2)$. The forms are check `P_einstein_energyConditionForms` (Stage-2 document §15.3). With the trace-reversed equation and $g_{44}=-1$, $T=-\rho+\sum_{\mu\ne4}p_{(\mu)}$ and $R_{44}=\kappa\bigl(\rho+T/6\bigr)$, so the strong condition can also be written $5\rho+\sum_{\mu\ne4}p_{(\mu)}=6R_{44}/\kappa=-36H^2a_4'^2/\kappa$. **Caution:** in signature (4,4) there are four time-like directions, so these are the conditions for the chosen observer and the chosen null vectors, not a complete classification.

### 9.12 Which dirac16complex states can be the source

Could the dirac16complex field itself be the negative-energy source? The Stage-2 document (§15.5) answers this for all states that depend on $x_0$ and $x_4$ only, with the bilinears read as ordinary numbers (the classical, mean-field reading of Chapter 7). We need three facts about the energy–momentum tensor of Chapter 7:

$$
T_{\mu\nu}=-\tfrac14\Bigl[\bar\Psi\gamma_\mu D_\nu\Psi+\bar\Psi\gamma_\nu D_\mu\Psi-(D_\mu\bar\Psi)\gamma_\nu\Psi-(D_\nu\bar\Psi)\gamma_\mu\Psi\Bigr]+g_{\mu\nu}\mathcal L_s ,
$$

where $\gamma_\mu=g_{\mu\nu}\gamma^{x_\nu}$ are the lowered curved gammas, $D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi$, $D_\mu\bar\Psi=\partial_\mu\bar\Psi-\bar\Psi\Omega_\mu$ with the spinor connection $\Omega_\mu$ of Section 9.13, and $\mathcal L_s$ is the Lagrangian divided by $\sqrt{\lvert g\rvert}$; on shell $\mathcal L_s=SU'(S)-U(S)$ with $S=\bar\Psi\Psi$ and $U(S)=\tfrac\lambda2S^2$.

**Proposition 9.2 (no source when $a_4''\ne0$).** No dirac16complex state that depends on $x_0$ and $x_4$ only satisfies $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ on an open set where $a_4''\ne0$.

**Proof.** Take a transverse direction $p\in\{1,2,3,5,6,7\}$. The state does not depend on $x_p$, so $D_p\Psi=\Omega_p\Psi$ and $D_p\bar\Psi=-\bar\Psi\Omega_p$, and the $pp$ component of $T$ is

$$
T_{pp}=-\tfrac14\bigl[2\bar\Psi\gamma_p\Omega_p\Psi+2\bar\Psi\Omega_p\gamma_p\Psi\bigr]+g_{pp}\mathcal L_s=-\tfrac12\bar\Psi\{\gamma_p,\Omega_p\}\Psi+g_{pp}\mathcal L_s .
$$

By Section 9.13, $\Omega_p$ is a combination of $S^{0p}$ and $S^{4p}$, and $\gamma_p$ is a multiple of $\gamma^p$. Now $S^{0p}=\tfrac12\gamma^0\gamma^p$ (because $\gamma^0$ and $\gamma^p$ anticommute), and $\{\gamma^p,\gamma^0\gamma^p\}=\gamma^p\gamma^0\gamma^p+\gamma^0\gamma^p\gamma^p=-\gamma^0(\gamma^p)^2+\gamma^0(\gamma^p)^2=0$; the same holds for $S^{4p}$. So $\{\gamma_p,\Omega_p\}=0$ and $T^p{}_p=g^{pp}T_{pp}=\mathcal L_s$ for all six transverse directions, off shell and for every $U$ (check `P_source_transversePressuresEqualForEveryX0X4State`). In particular $T^i{}_i-T^j{}_j=0$. But $G^i{}_i-G^j{}_j=2H^2a_4''$ by Section 9.8 (check `P_source_einsteinTransverseDifferenceIs2H2a4pp`). The equation $\kappa\cdot0=2H^2a_4''$ fails wherever $a_4''\ne0$. $\square$

**Proposition 9.3 (no real-$K$ plane wave).** A plane wave in the hidden coordinate, $\Psi=e^{-3H\zeta}e^{iK\zeta}u(x_4)=s^{-1/2+iK/(6H)}u(x_4)$ with real wave number $K$, is not a source for any $a_4$.

**Proof.** For real $K$ the modulus of the prefactor is $\lvert s^{-1/2+iK/(6H)}\rvert^2=s^{-1}$, so every bilinear $\bar\Psi X\Psi$ is a function of $x_4$ divided by $\sin z$. The energy density is then (Stage-2 document §15.5, check `P_source_realKDiagonalIsC1OverSPlusC2OverS2`)

$$
\rho=\frac{m\,u^\dagger Cu-iK\,u^\dagger C\gamma^0u}{\sin z}+\frac{\lambda\,(u^\dagger Cu)^2}{2\sin^2z},
$$

of the form $c_1/\sin z+c_2/\sin^2z$ at each $x_4$, while the required $\rho_{\mathrm{req}}$ is a nonzero constant in $z$. The three functions $1$, $1/\sin z$, $1/\sin^2z$ are linearly independent on $(0,\pi/2)$ (their Wronskian, the determinant of the functions and their first two derivatives, is $-2\cot^3z\,\csc^3z\ne0$), so $\rho=\rho_{\mathrm{req}}$ for all $z$ would force the constant coefficient to vanish: $3H^2(7+a_4'^2)=0$, impossible (check `P_source_realKPlaneWaveCannotSource`). $\square$

**Proposition 9.4 (an exact source for linear $a_4$).** Let $a_4=c\,t$ plus a constant. The state that does not depend on $x_0$, $\Psi=u(x_4)$ (the plane wave above with the imaginary value $K=-3iH$, which makes the prefactor equal to 1), solves the Dirac equation exactly for every $\lambda$ with a constant $S=u^\dagger Cu$ (check `P_source_x0IndependentStateSolvesDiracExactly`). Its energy–momentum tensor on shell has $T^4{}_4=-(mS+U)$ and $T^\mu{}_\mu=SU'-U$ for all seven $\mu\ne4$ (check `P_source_x0IndependentDiagonalOnShell`), and its off-diagonal components are multiples of 15 three-gamma bilinears (check `P_source_x0IndependentOffDiagonalAre15Bilinears`). It satisfies $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ in all 64 components if and only if (1) those bilinears vanish (for $c=0$ only 6 of them are needed), (2) $mS=-36H^2/\kappa$ and (3) $\lambda S^2=2H^2(15-3c^2)/\kappa$.

**Derivation of (2) and (3).** With $U=\tfrac\lambda2S^2$, $U'=\lambda S$ and $SU'-U=\tfrac\lambda2S^2$. The $\zeta\zeta$ equation, $G^0{}_0=\kappa T^0{}_0$, reads $-3H^2(c^2-5)=\kappa\tfrac\lambda2S^2$, that is $H^2(15-3c^2)=\tfrac\kappa2\lambda S^2$: condition (3). The $44$ equation, $G^4{}_4=\kappa T^4{}_4$, reads $3H^2(7+c^2)=-\kappa mS-\tfrac\kappa2\lambda S^2=-\kappa mS-H^2(15-3c^2)$, so $\kappa mS=-21H^2-3H^2c^2-15H^2+3H^2c^2=-36H^2$: condition (2). The six transverse equations read $H^2(15-3c^2\pm a_4'')=\tfrac\kappa2\lambda S^2=H^2(15-3c^2)$ and hold because $a_4''=0$ (check `P_source_x0IndependentSourceConditions`). The off-diagonal equations are condition (1), since $G$ is diagonal.

**The energy density is still negative.** For such a source $\rho=mS+\tfrac\lambda2S^2=\tfrac1\kappa\bigl[-36H^2+H^2(15-3c^2)\bigr]=-3H^2(7+c^2)/\kappa$, exactly $\rho_{\mathrm{req}}$. It is possible because $C$ has eigenvalues $+1$ and $-1$, so $S=u^\dagger Cu$ can have either sign.

**Two exact examples**, with the effective mass $M_{\mathrm{eff}}=m+\lambda S$ (units $H=\kappa=1$; check `P_source_x0IndependentExactExamples`, Stage-2 document §15.5):

| Case | $a_4$ | $m$ | $\lambda$ | $S$ | $M_{\mathrm{eff}}$ | $\rho$ | $p$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | $\sqrt5\,t$ | 5 | 0 | $-36/5$ | 5 | $-36$ | 0 |
| B | $t$ | $-15$ | $25/6$ | $12/5$ | $-5$ | $-24$ | 12 |

The equation of state is $w=p/\rho=0$ in Case A (dust of negative energy) and $w=-\tfrac12$ in Case B. Case B is the notebook's $a_4=t$. Check it with the conditions: $mS=-15\cdot\tfrac{12}{5}=-36$; $\lambda S^2=\tfrac{25}{6}\cdot\tfrac{144}{25}=24=2(15-3)$; $\rho=-36+12=-24$. So within Einstein gravity the dirac16complex field **can** be the source of the primordial field when $a_4$ is linear, but only as a state of negative energy density, and nothing here says that such a state is realized, stable or preferred (Stage-2 document §1, non-claim 2). For the static field ($c=0$) the conditions become $mS=-36H^2/\kappa$ and $\lambda S^2=30H^2/\kappa$ (so $\lambda>0$ and $mS<0$); whether a Kohn–Sham state can meet them is a question of Chapter 13 (`handoff/specs/STAGE4_SPEC.md`, erratum E4.1). The older statement of the project contract that a condensate "cannot" source this field is correct only for the real-$K$ plane waves of Proposition 9.3 and must not be repeated in general (erratum E4.1).

### 9.13 The spin connection and the Dirac operator in this field

**The spin connection of a diagonal vielbein.** Chapter 4 fixes the spin connection by the vielbein postulate:

$$
\omega_\mu{}^a{}_b=e_b{}^\nu\bigl(\Gamma^\rho{}_{\mu\nu}\,e_\rho{}^a-\partial_\mu e_\nu{}^a\bigr),\qquad \omega_{\mu ab}=\eta_{ac}\,\omega_\mu{}^c{}_b=-\omega_{\mu ba},
$$

and the spinor connection is $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$ with $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$, summed over all ordered pairs $(a,b)$. For the diagonal vielbein $e_\nu{}^a=h_\nu\delta_\nu^a$, with inverse $e_b{}^\nu=\delta_b^\nu/h_b$, the sums collapse (no sums below):

$$
\omega_\mu{}^a{}_b=\frac{1}{h_b}\bigl(h_a\,\Gamma^a{}_{\mu b}-\delta^a_b\,\partial_\mu h_b\bigr).
$$

*Case $a=b$.* By rule (C1), $\Gamma^a{}_{\mu a}=\tfrac12\partial_\mu\ln\lvert g_{aa}\rvert=\partial_\mu\ln h_a$, so $\omega_\mu{}^a{}_a=\partial_\mu\ln h_a-\partial_\mu\ln h_a=0$.

*Case $a\ne b$.* Then $\omega_\mu{}^a{}_b=(h_a/h_b)\Gamma^a{}_{\mu b}$, which by rule (C3) vanishes unless $\mu=a$ or $\mu=b$. For $\mu=b$ rule (C2) gives $\Gamma^a{}_{bb}=-\partial_ag_{bb}/(2g_{aa})=-\eta_{bb}h_b\,\partial_ah_b/(\eta_{aa}h_a^2)$, and lowering with $\eta_{aa}$:

$$
\omega_{b\,ab}=-\eta_{bb}\,\frac{\partial_ah_b}{h_a}\qquad(a\ne b,\ \text{no sums}).
$$

For $\mu=a$ the result is the antisymmetric partner of the same number, $\omega_{a\,ab}=\eta_{aa}\partial_bh_a/h_b=-\omega_{a\,ba}$. So a component is nonzero exactly when some scale factor $h_b$ depends on some other coordinate $x_a$.

**The 24 components.** In the primordial field $h_i=s^{1/6}e^{a_4}$ and $h_j=s^{1/6}e^{-a_4}$ depend on $x_0$ and $x_4$, and $h_0=\cot z$ depends on $x_0$ only (which gives nothing, since $a\ne b$ is required). With $\partial_0h_i=H\cot z\,h_i$, $\partial_4h_i=Ha_4'h_i$, $\partial_0h_j=H\cot z\,h_j$, $\partial_4h_j=-Ha_4'h_j$, $h_0=\cot z$ and $h_4=1$:

$$
\begin{aligned}
\omega_{i\,0i}&=-\omega_{i\,i0}=-H\,s^{1/6}e^{a_4}, &\qquad \omega_{i\,i4}&=-\omega_{i\,4i}=H\,s^{1/6}e^{a_4}\,a_4',\\
\omega_{j\,0j}&=-\omega_{j\,j0}=H\,s^{1/6}e^{-a_4}, &\qquad \omega_{j\,j4}&=-\omega_{j\,4j}=H\,s^{1/6}e^{-a_4}\,a_4'.
\end{aligned}
$$

For example $\omega_{1\,01}=-\eta_{11}\,\partial_0h_1/h_0=-H\cot z\,h_1/\cot z=-H\,s^{1/6}e^{a_4}$. That is $6\times2\times2=24$ nonzero components; $\omega_{0ab}=\omega_{4ab}=0$ (checks `P_spinconn_closedForms`, `P_spinconn_count24`, `P_spinconn_antisymmetry`; the vielbein postulate holds in all 512 components, check `P_spinconn_vielbeinPostulate512`; Stage-2 document §6). The mixed components $\omega_\mu{}^a{}_b$ are exactly the notebook's ωμIJ of cell 501 (check `P_spinconn_notebookCell501OmegaMuIJEqualsMixedOmega`).

**The spinor connection.** In the double sum $\tfrac12\omega_{\mu ab}S^{ab}$ every antisymmetric pair appears twice, once as $(a,b)$ and once as $(b,a)$, and both terms are equal because $\omega_{\mu ab}$ and $S^{ab}$ both change sign. Hence the spinor connection is a single sum over the pairs with $a<b$,

$$
\Omega_\mu=\sum_{a<b}\omega_{\mu ab}S^{ab},
$$

and inserting the 24 components (with $S^{i4}=-S^{4i}$ and $S^{j4}=-S^{4j}$) gives

$$
\Omega_0=\Omega_4=0,\qquad \Omega_i=-H\,s^{1/6}e^{a_4}\bigl(S^{0i}+a_4'S^{4i}\bigr),\qquad \Omega_j=H\,s^{1/6}e^{-a_4}\bigl(S^{0j}-a_4'S^{4j}\bigr)
$$

(check `P_Omega_closedForms`).

**The contraction $\gamma^\mu\Omega_\mu=3H\gamma^0$.** Only the Clifford relations $\{\gamma^a,\gamma^b\}=2\eta^{ab}$ are needed. For $a\ne b$ the matrices anticommute, so $S^{ab}=\tfrac12\gamma^a\gamma^b$, and

$$
\gamma^bS^{ab}=\tfrac12\gamma^b\gamma^a\gamma^b=-\tfrac12\gamma^a(\gamma^b)^2=-\tfrac12\eta^{bb}\gamma^a .
$$

Now use the curved gammas of Section 9.2. For $i=1,2,3$ ($\eta^{ii}=+1$):

$$
\gamma^{x_i}\Omega_i=s^{-1/6}e^{-a_4}\gamma^i\cdot\bigl(-Hs^{1/6}e^{a_4}\bigr)\bigl(S^{0i}+a_4'S^{4i}\bigr)=-H\Bigl(-\tfrac12\gamma^0-\tfrac12a_4'\gamma^4\Bigr)=\tfrac H2\bigl(\gamma^0+a_4'\gamma^4\bigr).
$$

For $j=5,6,7$ ($\eta^{jj}=-1$):

$$
\gamma^{x_j}\Omega_j=s^{-1/6}e^{a_4}\gamma^j\cdot Hs^{1/6}e^{-a_4}\bigl(S^{0j}-a_4'S^{4j}\bigr)=H\Bigl(\tfrac12\gamma^0-\tfrac12a_4'\gamma^4\Bigr)=\tfrac H2\bigl(\gamma^0-a_4'\gamma^4\bigr).
$$

Summing three of each,

$$
\gamma^\mu\Omega_\mu=\tfrac{3H}2\bigl(\gamma^0+a_4'\gamma^4\bigr)+\tfrac{3H}2\bigl(\gamma^0-a_4'\gamma^4\bigr)=3H\gamma^0 .
$$

**The free function $a_4$ cancels**: the inflating and the deflating directions contribute opposite $a_4'$ terms (checks `P_Omega_gammaSlash3Hgamma0` and `P_Omega_slashA4Independent`). In the other order, $S^{ab}\gamma^b=\tfrac12\gamma^a(\gamma^b)^2=+\tfrac12\eta^{bb}\gamma^a$, every term flips sign, so $\Omega_\mu\gamma^\mu=-3H\gamma^0$, $\{\gamma^\mu,\Omega_\mu\}=0$ and $[\gamma^\mu,\Omega_\mu]=6H\gamma^0$ (check `P_Omega_OmegaGammaAndAnticommutator`). The divergence identity of Chapter 7 can be checked directly: only $\mu=0$ contributes on the left, and

$$
\partial_\mu\bigl(\sqrt{\lvert g\rvert}\,\gamma^{x_\mu}\bigr)=\partial_0\bigl(\cos z\tan z\,\gamma^0\bigr)=\partial_0(\sin z)\,\gamma^0=6H\cos z\,\gamma^0=\sqrt{\lvert g\rvert}\,[\gamma^\mu,\Omega_\mu]
$$

(check `P_gammaConst_divergenceIdentity`). With this connection the gammas are covariantly constant, $D_\mu\gamma^\nu=0$ for all 64 pairs (check `P_gammaConst_DmuGammaNuZero64`).

**The Dirac equation in the primordial field.** The field equation of Chapter 7, $\gamma^\mu D_\mu\Psi=(m+\lambda S)\Psi$, becomes

$$
\tan z\,\gamma^0\partial_0\Psi+s^{-1/6}e^{-a_4}\sum_i\gamma^i\partial_i\Psi+\gamma^4\partial_4\Psi+s^{-1/6}e^{a_4}\sum_j\gamma^j\partial_j\Psi+3H\gamma^0\Psi=(m+\lambda S)\Psi .
$$

For a field that depends on $x_0$ and $x_4$ only, the $a_4$-dependent coefficients multiply vanishing derivatives, and

$$
\tan z\,\gamma^0\partial_0\Psi+\gamma^4\partial_4\Psi+3H\gamma^0\Psi=(m+\lambda S)\Psi .
$$

**No $a_4$ appears at all.** Multiplying by $-\gamma^4$ (note $(\gamma^4)^2=\eta^{44}=-1$) solves for the time derivative. Every row of every $\gamma^a$ has exactly one nonzero entry $\pm1$ (Chapter 2), so each equation links a component to exactly one other component through $\gamma^4\gamma^0$ and to one through $\gamma^4$. Following these links, the 16 equations split into four independent blocks of four components, $\{0,5,8,13\}$, $\{1,4,9,12\}$, $\{2,7,10,15\}$, $\{3,6,11,14\}$ (the notebook's coupling sets of cell 1089; checks `P_blocks_fourBlocksOfFour` and `P_blocks_matchNotebookSets`). For $\lambda\ne0$ the blocks are coupled only through the single number $S$, a bilinear in all 16 components; the linear part is block diagonal. In the variables $z,t$ ($\partial_0=6H\partial_z$, $\partial_4=H\partial_t$) the first block is (Stage-2 document §10.5)

$$
\begin{aligned}
H\,\partial_t\Psi_0&=-\bigl(6H\tan z\,\partial_z+3H\bigr)\Psi_5+(m+\lambda S)\Psi_{13},\\
H\,\partial_t\Psi_5&=-\bigl(6H\tan z\,\partial_z+3H\bigr)\Psi_0+(m+\lambda S)\Psi_8,\\
H\,\partial_t\Psi_8&=\bigl(6H\tan z\,\partial_z+3H\bigr)\Psi_{13}-(m+\lambda S)\Psi_5,\\
H\,\partial_t\Psi_{13}&=\bigl(6H\tan z\,\partial_z+3H\bigr)\Psi_8-(m+\lambda S)\Psi_0 ,
\end{aligned}
$$

and the other three blocks have the same shape with other signs.

**The notebook's contraction in this field.** The notebook builds its connection as $\Omega^{\mathrm{NB}}_\mu=\tfrac12\omega_\mu{}^a{}_b\,S^{ab}$, with the mixed $\omega$ contracted against $S^{ab}$ with both indices up; one factor $\eta$ is missing (Chapter 4). Since $\omega_\mu{}^a{}_b=\eta^{aa}\omega_{\mu ab}$ (no sum), the notebook's connection is $\tfrac12\sum_{a,b}\eta^{aa}\omega_{\mu ab}S^{ab}$, and its effect on a pair $(a,b)$ depends on the two signs. The two ordered terms of a pair are $\tfrac12\eta^{aa}\omega_{\mu ab}S^{ab}$ and $\tfrac12\eta^{bb}\omega_{\mu ba}S^{ba}$, and since $\omega_{\mu ba}S^{ba}=(-\omega_{\mu ab})(-S^{ab})=\omega_{\mu ab}S^{ab}$ their sum is $\tfrac12(\eta^{aa}+\eta^{bb})\,\omega_{\mu ab}S^{ab}$; the correct connection has $\tfrac12(1+1)\,\omega_{\mu ab}S^{ab}$ instead. So a pair of two space-like frame indices is unchanged, a pair of two time-like indices changes sign, and a mixed pair (one space-like, one time-like: a **boost**) cancels, because then $\eta^{bb}=-\eta^{aa}$. Applied to our field, $\Omega^{\mathrm{NB}}_i=-Hs^{1/6}e^{a_4}S^{0i}$ (the boost $S^{4i}$ is lost) and $\Omega^{\mathrm{NB}}_j=+Hs^{1/6}e^{-a_4}a_4'S^{4j}$ (the boost $S^{0j}$ is lost and the time-time term flips sign). Repeating the contraction above gives

$$
\gamma^\mu\Omega^{\mathrm{NB}}_\mu=\tfrac{3H}{2}\bigl(\gamma^0+a_4'\gamma^4\bigr)\ne3H\gamma^0 ,
$$

and $D_\mu\gamma^\nu=0$ fails in 15 of the 64 pairs, with 288 nonzero matrix entries in total. For example $D_1\gamma^4=H\,s^{1/6}e^{a_4}a_4'\,\gamma^1$ instead of zero. The failure is the check `P_gammaConst_notebookContractionFails`, and its closed forms are the check `P_gammaConst_notebookContractionClosedForms` (Stage-2 document §8.3). For commuting fields, which the notebook actually uses, this error drops out of the $(x_0,x_4)$ equations (Stage-2 document §11.3, fact 1); the error that does survive is the next one.

### 9.14 Errata 2 and 3: the cell-1058 rule and the q term

**The notebook's chain.** The notebook's production Lagrangian La[] (cell 1066) is built from commuting fields f16[k]$(x_0,x_4)$, the curved gamma matrices useT16 built in cell 1058, the mixed connection of cell 501 multiplied by a switch $Q_1$ (the notebook's book-keeping factor for the spin connection), and the mass term $HM\,\Psi_{16}^T\sigma_{16}\Psi_{16}$. Its Euler–Lagrange expressions are stored in cell 1079; cell 1096 multiplies them by $1/(2H)$ and changes to the variables $z,t$; cell 1111 relabels the components block by block into yZ$_0$ to yZ$_{15}$ (block $\{0,5,8,13\}$ becomes yZ$_0$ to yZ$_3$, and so on); and cell 1137 stores the equations solved for $\partial_t$ (Stage-2 document §11.1). The dictionary to our notation is $\Psi_k=\mathrm{f16}[k]$ and $m=-HM$.

**What the stored equations say.** For the first block the stored cell-1137 equations are (Stage-2 document §11.2)

$$
\begin{aligned}
\partial_t yZ_0&=q\,yZ_0-3\,yZ_1-M\,yZ_3-6\tan z\,\partial_z yZ_1,\\
\partial_t yZ_1&=-3\,yZ_0-q\,yZ_1-M\,yZ_2-6\tan z\,\partial_z yZ_0,\\
\partial_t yZ_2&=M\,yZ_1-q\,yZ_2+3\,yZ_3+6\tan z\,\partial_z yZ_3,\\
\partial_t yZ_3&=M\,yZ_0+3\,yZ_2+q\,yZ_3+6\tan z\,\partial_z yZ_2,
\end{aligned}
\qquad q=Q_1\sinh(a_4)\,a_4'\,e^{-a_4}.
$$

Compare with the correct first block of Section 9.13 for $\lambda=0$: divide it by $H$ and put $m/H=-M$, $yZ_0=\Psi_0$, $yZ_1=\Psi_5$, $yZ_2=\Psi_8$, $yZ_3=\Psi_{13}$. The first line becomes $\partial_tyZ_0=-3\,yZ_1-M\,yZ_3-6\tan z\,\partial_zyZ_1$. **The stored equations agree with the correct ones term by term, except for the terms $\pm q\,yZ_k$.** The same holds in all 16 rows; the $q$ terms occur only in the first two blocks, yZ$_0$ to yZ$_7$ (checks `P_notebookCompare_cell1137Reproduced16of16`, `P_notebookCompare_correctVsStoredDifferOnlyByQ`, `P_notebookCompare_qOnlyInYZ0to7`). Since the correct $(x_0,x_4)$ equations contain no $a_4$ at all (Section 9.13), the term $q$, and with it every $a_4$ dependence of the notebook's block equations, is spurious.

**Erratum 2: the substitution rule of cell 1058.** Cell 1058 contains the rule

```
1/Sqrt[Sin[6*H*x0]^(1/3)/E^(2*a4[H*x4])] -> 1/(E^a4[H*x4]*Sin[6*H*x0]^(1/6))
```

The left side is $1/\sqrt{s^{1/3}e^{-2a_4}}$. The square root is $s^{1/6}e^{-a_4}$ and its reciprocal is $s^{-1/6}e^{+a_4}$, so the correct rule is

```
1/Sqrt[Sin[6*H*x0]^(1/3)/E^(2*a4[H*x4])] -> E^a4[H*x4]/Sin[6*H*x0]^(1/6)
```

The rule as written puts $e^{-a_4}$ where $e^{+a_4}$ belongs. This quantity is precisely the coefficient $1/h_j=s^{-1/6}e^{a_4}$ of the extra-time curved gammas $\gamma^{x_5},\gamma^{x_6},\gamma^{x_7}$ of Section 9.2. **A numerical test** makes the error concrete: take $s=1/64$ and $a_4=\ln2$. Then $s^{1/3}=1/4$, $e^{2a_4}=4$, the left side is $1/\sqrt{1/16}=4$, the correct right side is $e^{a_4}/s^{1/6}=2/(1/2)=4$, and the notebook's right side is $1/(2\cdot\tfrac12)=1$.

**Erratum 3: how the q term arises (a reconstruction).** The notebook does not store the value of useT16, so the path from the rule to the $q$ term cannot be read off; it has to be reconstructed. Three facts are established by exact computation (Stage-2 document §11.3):

1. With Clifford-consistent curved gammas, every $Q_1$ term drops out of the commuting-field equations, for the notebook's contraction and for the correct one alike (check `P_notebookCompare_commutingQ1DropsOutCliffordGammas`).
2. The stored cell-1079 expressions, parsed from the committed notebook (check `P_notebookCompare_storedEla16`), contain $Q_1$ terms in exactly the 8 rows of the first two blocks (Stage-2 document §11.3, fact 2).
3. These terms are reproduced exactly, 16 of 16 rows with zero residual, if the extra-time curved gammas carry the wrong factor $s^{-1/6}e^{-a_4}$ on their $+1$ entries and the correct factor $s^{-1/6}e^{+a_4}$ on their $-1$ entries. The same reconstruction, carried through the notebook's own chain, reproduces the stored outputs of cells 1096, 1111 and 1137 exactly (checks `P_notebookCompare_reconstructionReproducesStoredEla`, `P_notebookCompare_eLaztCell1096`, `P_notebookCompare_relabelCell1111`).

In formulas the reconstructed gamma is

$$
\gamma'^{\,x_j}=s^{-1/6}\bigl(\cosh(a_4)\,\gamma^j-\sinh(a_4)\,\lvert\gamma^j\rvert\bigr)\qquad(j=5,6,7),
$$

where $\lvert\gamma^j\rvert$ is the matrix of absolute values of the entries. Check it entry by entry: where $\gamma^j$ has $+1$, the entry is $s^{-1/6}(\cosh a_4-\sinh a_4)=s^{-1/6}e^{-a_4}$ (wrong factor); where $\gamma^j$ has $-1$, it is $s^{-1/6}(-\cosh a_4-\sinh a_4)=-s^{-1/6}e^{a_4}$ (correct factor times $-1$) (check `P_notebookCompare_reconstructedGammaForm`).

**The reconstructed gamma is not in the Clifford algebra.** Write $\gamma^5$ as a signed permutation: row $r$ has its single entry $\epsilon_r=\pm1$ in column $\pi(r)$. Since $(\gamma^5)^2=\eta^{55}=-1$ is diagonal, $\pi(\pi(r))=r$, and since $\gamma^5$ is antisymmetric (Chapter 2), the entry in row $\pi(r)$, column $r$ is $-\epsilon_r$. The matrix $D=s^{1/6}\gamma'^{\,x_5}$ has, in row $r$, the entry $e^{-a_4}$ if $\epsilon_r=+1$ and $-e^{a_4}$ if $\epsilon_r=-1$. The diagonal entry $(D^2)_{rr}$ is the product of the entries at $(r,\pi(r))$ and $(\pi(r),r)$: for $\epsilon_r=+1$ it is $e^{-a_4}\cdot(-e^{a_4})=-1$, for $\epsilon_r=-1$ it is $(-e^{a_4})\cdot e^{-a_4}=-1$; the off-diagonal entries vanish because $\pi(\pi(r))=r$. Hence

$$
\bigl(\gamma'^{\,x_5}\bigr)^2=-s^{-1/3}\cdot1,\qquad\text{whereas the Clifford relation requires}\qquad \bigl(\gamma^{x_5}\bigr)^2=g^{55}=-s^{-1/3}e^{2a_4}.
$$

The two agree only when $a_4=0$ (check `P_notebookCompare_reconstructedGamma5NotClifford`; the report also records that $\gamma'^{\,x_5}$ anticommutes neither with $\gamma'^{\,x_6}$ nor with $\gamma^{x_0}$).

**The size of the spurious term.** Because $\gamma'^{\,x_j}$ is not Clifford, the product $\sigma_{16}\gamma'^{\,x_j}S^{4j}$ acquires a symmetric part, which commuting fields do not annihilate. Its size is the difference of the two factors, $s^{-1/6}(e^{a_4}-e^{-a_4})$, times the mixed connection component $\omega_j{}^4{}_j=H\,a_4'\,s^{1/6}e^{-a_4}$, times $Q_1$:

$$
s^{-1/6}\bigl(e^{a_4}-e^{-a_4}\bigr)\cdot Ha_4's^{1/6}e^{-a_4}\cdot Q_1=2H\,Q_1\sinh(a_4)\,a_4'\,e^{-a_4}=2Hq ,
$$

and the factor $1/(2H)$ of cell 1096 turns it into $q$. The origin of the term is the check `P_notebookCompare_qTermFromNonCliffordExtraTimeGammas`, and its size $2Hq$ in the normalisation of cell 1079 is the check `P_notebookCompare_qVectorIs2HqAtCell1079`. The identity $\sinh(a_4)e^{-a_4}=\tfrac12(1-e^{-2a_4})$ gives the equivalent form $q=\tfrac12Q_1a_4'(1-e^{-2a_4})$; for $a_4=t$, $q=\tfrac12Q_1(1-e^{-2t})$.

**What is established and what is reconstructed.** Established: the stored outputs of cells 1079, 1096, 1111 and 1137 are reproduced exactly, and the correct equations differ from the stored ones only by the $q$ terms. Reconstructed: that the rule of cell 1058 produced the reconstructed useT16 by acting on the $+1$ entries only. When cell 1058 is re-executed literally in the verifier's kernel (Mathematica 15.0.1), the wrong factor $e^{-a_4}$ is applied to all entries of the three extra-time gammas; the resulting equations then contain no $q$ term and differ from the stored ones by exactly the $q$ terms (check `P_notebookCompare_literalRebuildResidualIsExactlyQTerms`). The notebook's metadata indicate that the stored chain ran in one older kernel session (cell 1096 stores the date 2026-01-30), in which the simplified form of the $-1$ entries, and hence whether the rule matched them, may have differed. That explanation is a reconstruction as well (Stage-2 document §11.3 and §20, item 7).

**Consequences.** Later steps of the notebook that remove or use the $q$ term, a rescaling of the yZ components and an equation for $a_4$ built from the same coefficient (cells 100, 1157 and 1158 in the survey), have no counterpart in the correct equations. This last remark is a reading of the notebook's text, not a machine check (Stage-2 document §11.4). The correct statement is simple: **for fields of $(x_0,x_4)$ the dynamics does not see $a_4$ at all.**

### 9.15 The static member of the family

**Why a static field.** Part IV of this book looks for the ground state and the first excited state of many dirac16complex quanta (Chapter 13). A ground state is a state that does not change in time, and that needs a background that does not change in time either. The primordial family has exactly one such member: $a_4$ constant, $a_4=a_{4,0}$, so $a_4'=a_4''=0$ (`handoff/specs/STAGE4_SPEC.md` §1).

**The metric.** Stage 4 calls the hidden coordinate $y$; it is the $\zeta$ of Section 9.5, $y=\ln(\sin z)/(6H)$, now including the end point $y=0$ ($z=\pi/2$):

$$
ds^2=dy^2-dx_4^2+e^{2Hy}\Bigl[e^{2a_{4,0}}\bigl(dx_1^2+dx_2^2+dx_3^2\bigr)-e^{-2a_{4,0}}\bigl(dx_5^2+dx_6^2+dx_7^2\bigr)\Bigr],\qquad y\le0 .
$$

The warp factor is $W(y)=e^{Hy}$ and the volume factor is $\sqrt{\lvert g\rvert}=W^6=e^{6Hy}$ (checks `KS_geometry_sqrtDetG_W6`, `KS_geometry_signature44` and `KS_geometry_notebookChart`).

**The constant $a_{4,0}$ is a choice of units.** New coordinates $x_i'=e^{a_{4,0}}x_i$ and $x_j'=e^{-a_{4,0}}x_j$ remove $a_{4,0}$ from the line element. It returns only through quantities measured in the old coordinates; in the Kohn–Sham problem of Chapter 13 it rescales every 3-space momentum, $k\to k\,e^{-a_{4,0}}$ (check `KS_reduction_a4IsMomentumRescaling`).

**Curvature.** Lemma 9.1 with $f_p=Hy+\sigma_pa_{4,0}$ gives $\partial_yf_p=H$, all other derivatives zero, $\Theta_y=6H$, $\Theta_4=0$. So $R^y{}_y=-6H^2$, $R^4{}_4=0$, $R^p{}_p=-6H^2$ for the six fibre directions, and

$$
R=-42H^2,\qquad G^\mu{}_\nu=\mathrm{diag}(15,15,15,15,21,15,15,15)\,H^2
$$

in the order $(y,x_1,x_2,x_3,x_4,x_5,x_6,x_7)$. This is also the case $a_4'=a_4''=0$ of Section 9.8. The Stage-4 verifier checks the scalar in `KS_geometry_ricciScalarMinus42H2`, the Einstein tensor in `KS_geometry_einsteinMixedDiag` and the Ricci tensor in `KS_geometry_ricciMixed`. Only 18 Christoffel symbols are nonzero, namely $\Gamma^y{}_{pp}=-H\,g_{pp}$ and $\Gamma^p{}_{yp}=\Gamma^p{}_{py}=H$ (check `KS_geometry_christoffelCount18`). The exact theory of Stage 4 found more. The seven directions $(y,x_1,x_2,x_3,x_5,x_6,x_7)$ form a space of constant curvature $-H^2$, which means $R_{rsmn}=-H^2(g_{rm}g_{sn}-g_{rn}g_{sm})$ for those directions, and the time line $x_4$ is flat (check `KS_geometry_constantCurvatureSevenSpace`). For such a space in $n=7$ dimensions the Ricci tensor is $-(n-1)H^2g$ and $R=-n(n-1)H^2=-42H^2$, in agreement with the lemma, and the square of the curvature is $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=2n(n-1)H^4=84H^4$ (check `KS_geometry_kretschmannConstant`). Every curvature invariant is a constant: **nothing singular happens anywhere in $y$**, in particular not at $y=0$.

**The required source.** From $G^\mu{}_\nu=\kappa T^\mu{}_\nu$:

$$
\rho_{\mathrm{req}}=-\frac{21H^2}{\kappa}<0,\qquad p_{\mathrm{req}}=+\frac{15H^2}{\kappa}\quad\text{in all seven transverse directions},\qquad w_{\mathrm{req}}=-\frac57
$$

(checks `KS_geometry_requiredSource` and `KS_geometry_rhoRequiredNegative`). **Erratum 4.** The Stage-4 specification §1 had written $p_{\mathrm{req}}=-15H^2/\kappa$; the exact mixed components give $+15H^2/\kappa$ (erratum E4.3 of the same specification; the Wolfram report records it under `specDiscrepancy_pReqSign`). By Proposition 9.4 with $c=0$, an $x_0$-independent dirac16complex state is an exact source of the static field if and only if its three-gamma bilinears vanish, $mS=-36H^2/\kappa$ and $\lambda S^2=30H^2/\kappa$.

**Extrinsic curvature of the slices.** Each surface $y=\mathrm{const}$ is a 7-dimensional slice. Its **unit normal** is $n=\partial_y$ (a unit vector because $g_{yy}=1$). Its **extrinsic curvature** measures how the slice bends inside the 8-dimensional space: $K_{ab}=\nabla_an_b$ for directions $a,b$ along the slice. The lower components of the normal are $n_c=\delta_c^y$, so $K_{ab}=\partial_an_b-\Gamma^c{}_{ab}n_c=-\Gamma^y{}_{ab}$, and by rule (C2) with $g_{yy}=1$, $\Gamma^y{}_{ab}=-\tfrac12\partial_yg_{ab}$. Hence

$$
K_{ab}=\tfrac12\partial_yg_{ab},\qquad K^a{}_b=\tfrac12g^{ac}\partial_yg_{cb} .
$$

For the six warped directions $g_{pp}\propto e^{2Hy}$ and $K^p{}_p=H$; for $x_4$, $K^4{}_4=0$; the trace is $K=6H$ (check `KS_geometry_extrinsicCurvature`).

### 9.16 Beyond y = 0: the smooth extension and the Z2 brane

The notebook's chart ends at $y=0$, where its coordinate $x_0$ degenerates. The geometry itself does not end there. Stage 4 documents two ways to continue it (`handoff/specs/STAGE4_SPEC.md` §1).

**(E1) The smooth extension.** Keep $W=e^{Hy}$ for all real $y$. By Section 9.15 all curvature invariants are constant, so this is a regular homogeneous space with no special point at $y=0$. The tip $y\to-\infty$, where $W^6\to0$ and the transverse space pinches off, lies at infinite proper distance, because $y$ itself measures proper distance.

**(E2) The Z2 mirror.** Take two copies of the notebook's patch $y\le0$ and glue them along $y=0$, the second copy reflected. Equivalently, use the warp factor

$$
W(y)=e^{-H\lvert y\rvert}:\qquad W=e^{Hy}\ \text{for}\ y\le0,\qquad W=e^{-Hy}\ \text{for}\ y\ge0 .
$$

The name Z2 refers to the group with two elements, the identity and the reflection $y\to-y$, under which this geometry is symmetric. This is the construction that Stage 4 adopts as a model of the notebook's picture of a pair of universes; it is a **choice of model, not a result derived from any equation**. The price is a kink: $W$ is continuous at $y=0$, but its slope jumps from $+H$ to $-H$.

**A tool: the delta function.** The derivative of $\lvert y\rvert$ is the sign function, $\mathrm{sgn}(y)=-1$ for $y<0$ and $+1$ for $y>0$. The derivative of the sign function is zero everywhere except at $y=0$, where it jumps by 2. Physicists write it as $2\delta(y)$, where the **delta function** $\delta(y)$ is the limit of ever narrower spikes of total area 1. A concrete way to see this is to smooth the corner: $\lvert y\rvert\approx\sqrt{y^2+\varepsilon^2}$ for small $\varepsilon>0$. Its first derivative $y/\sqrt{y^2+\varepsilon^2}$ tends to $\mathrm{sgn}(y)$, and its second derivative $\varepsilon^2/(y^2+\varepsilon^2)^{3/2}$ is a spike of height $1/\varepsilon$ and total area 2 (Exercise 9.11). So for $f(y)=-H\lvert y\rvert$:

$$
f'(y)=-H\,\mathrm{sgn}(y),\qquad f'(y)^2=H^2\ (y\ne0),\qquad f''(y)=-2H\,\delta(y).
$$

**The Einstein tensor with a kink.** Use Lemma 9.1 once more, with the base coordinates $(y,x_4)$ and $f_p=f(y)+\sigma_pa_{4,0}$, so that $\partial_yf_p=f'$, $\partial_y^2f_p=f''$, $\Theta_y=6f'$ and all $x_4$ derivatives vanish:

$$
R^y{}_y=-6\bigl(f''+f'^2\bigr),\qquad R^4{}_4=0,\qquad R^p{}_p=-\bigl(f''+6f'^2\bigr),\qquad R=-12f''-42f'^2 ,
$$

and therefore

$$
G^y{}_y=15f'^2,\qquad G^4{}_4=6f''+21f'^2,\qquad G^p{}_p=5f''+15f'^2 .
$$

For $f=Hy$ this returns the static values $15H^2$, $21H^2$, $15H^2$. For the mirror, $f=-H\lvert y\rvert$:

$$
G^y{}_y=15H^2,\qquad G^4{}_4=21H^2-12H\,\delta(y),\qquad G^p{}_p=15H^2-10H\,\delta(y).
$$

**The brane.** Einstein's equations $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ now require, besides the bulk source $\rho_{\mathrm{req}}=-21H^2/\kappa$ of Section 9.15 on both sides, a source concentrated on the surface $y=0$: $T^\mu{}_\nu\supset S^\mu{}_\nu\,\delta(y)$ with

$$
S^y{}_y=0,\qquad S^4{}_4=-\frac{12H}{\kappa},\qquad S^p{}_p=-\frac{10H}{\kappa}\quad(p=1,2,3,5,6,7).
$$

A surface that carries energy and momentum of its own is called a **brane** (from "membrane"). Its surface energy density and surface pressure are

$$
\rho_{\mathrm{brane}}=-S^4{}_4=+\frac{12H}{\kappa}>0,\qquad p_{\mathrm{brane}}=S^p{}_p=-\frac{10H}{\kappa}
$$

(checks `KS_geometry_israelStress` and `KS_geometry_braneEnergyPositive`). The pressure is negative, like a stretched membrane, but it is not a pure tension, for which $\rho=-p$ would hold. The component $S^y{}_y=0$ says that nothing flows through the brane. The metric induced on the brane, $\mathrm{diag}(e^{2a_{4,0}},e^{2a_{4,0}},e^{2a_{4,0}},-1,-e^{-2a_{4,0}},-e^{-2a_{4,0}},-e^{-2a_{4,0}})$, is constant, so the brane itself is flat (check `KS_geometry_inducedMetricFlat`).

**The same result from the Israel junction conditions.** The general rule for a thin wall in Einstein gravity is the **Israel junction condition**. Let $[X]=X(0^+)-X(0^-)$ denote the jump of a quantity across the wall, let the normal be $n=+\partial_y$, pointing from $y<0$ to $y>0$, and let $K_{ab}=\tfrac12\partial_yg_{ab}$ be the extrinsic curvature on each side (Section 9.15). Then

$$
[K_{ab}]-h_{ab}[K]=-\kappa\,S_{ab},
$$

with $h_{ab}$ the induced metric. On the side $y<0$, $K^p{}_p=+H$; on the side $y>0$, where $g_{pp}\propto e^{-2Hy}$, $K^p{}_p=-H$; along $x_4$, $K^4{}_4=0$ on both sides. So $[K^p{}_p]=-2H$, $[K^4{}_4]=0$ and $[K]=-12H$, and with one index raised

$$
S^p{}_p=-\frac1\kappa\bigl(-2H+12H\bigr)=-\frac{10H}{\kappa},\qquad S^4{}_4=-\frac1\kappa\bigl(0+12H\bigr)=-\frac{12H}{\kappa},
$$

the same as before (check `KS_geometry_israelJump`). The sign convention is recorded in the report (`geometry_israelSignConvention` in `wolfram-kohn-sham-report.json`); with it, the brane of the Randall–Sundrum model, a well-known five-dimensional model with warp factor $e^{-k\lvert y\rvert}$, gets a positive tension $6k/\kappa$ (Exercise 9.9; check `KS_geometry_israelConventionRandallSundrum` of the Python theory checker).

**What the mirror construction does and does not say.** The brane and its stress are what the geometry requires; no matter computed in this project produces them. The bulk on each side still requires the negative energy density $-21H^2/\kappa$. A structural remark connects the construction to the notebook's hypothesis: the chirality map $\Psi\to\gamma^8\Psi$ sends the Lagrangian with mass $m$ and potential $U$ to minus the Lagrangian with $-m$ and $-U$ (erratum E2 of `handoff/specs/CONTRACT.md`), so a mirror copy that carries $\gamma^8\Psi$ has the mass $-m$: the notebook's $\pm M$ pair. In the reduced Kohn–Sham equation of Chapter 13 the reflection $\Psi(-y)=\pm\gamma^0\Psi(y)$ is a symmetry only if the mass function is odd, $M(-y)=-M(y)$, that is, if the mirror universe carries the opposite mass; for an even mass function the symmetry is a different matrix, $i\gamma^0\gamma^8$ (erratum E4.6 of `handoff/specs/STAGE4_SPEC.md`). These are statements about the structure of the equations. They do not describe a creation process at $x_4=0$, and they do not show that universes are created in pairs; Chapter 15 proves the exact pairing theorems and Chapter 16 states precisely what they establish.

### 9.17 What we proved and what we assumed

**Proved in this chapter** (each step derived above and verified by the named checks of the Stage-2 and Stage-4 verifiers): the notebook's MatrixMetric44 has signature (4,4), $\det g=+\cos^2z$ and a constant 7-volume; in the hidden proper coordinate it is a warped metric; it has exactly 37 nonzero Christoffel symbols; by Lemma 9.1 its Ricci scalar is $6H^2(a_4'^2-7)$ and its Einstein tensor is diagonal with the closed forms of Section 9.8, which agree with the notebook's stored outputs; in 8-dimensional Einstein gravity it requires $\rho_{\mathrm{req}}=-3H^2(7+a_4'^2)/\kappa<0$ for every $a_4$, so it is neither a vacuum nor a cosmological-constant solution, and the listed energy conditions fail; no dirac16complex state of $(x_0,x_4)$ can be its source when $a_4''\ne0$, no real-$K$ plane wave can be its source at all, and for linear $a_4$ an $x_0$-independent state is an exact source, necessarily of negative energy density; the spin connection has 24 nonzero components and $\gamma^\mu\Omega_\mu=3H\gamma^0$, so the equations of fields of $(x_0,x_4)$ contain no $a_4$; the notebook's cell-1058 rule is mathematically wrong, its stored block equations differ from the correct ones exactly by the $q$ terms, and the reconstructed curved gamma is not a Clifford element; the static member has $R=-42H^2$, $G=\mathrm{diag}(15,15,15,15,21,15,15,15)H^2$, $\rho_{\mathrm{req}}=-21H^2/\kappa$ and $p_{\mathrm{req}}=+15H^2/\kappa$; and the Z2 mirror geometry requires a flat brane with $\rho_{\mathrm{brane}}=12H/\kappa$ and $p_{\mathrm{brane}}=-10H/\kappa$. Four errata were recorded: the sign of $\det g$ in the Stage-2 specification, the rule of cell 1058, the $q$ term, and the sign of $p_{\mathrm{req}}$ in the Stage-4 specification.

**Assumed, quoted or open.** The metric is a prescribed background; nothing here derives it or its function $a_4$ from dynamics, and the slopes of cell 150 are tabulated, not derived. Only 8-dimensional Einstein gravity is used: Lovelock's theorem and the Einstein–Hilbert variational principle are quoted, and the Lovelock terms of order 2 and 3, which the notebook names, are computed neither by the notebook nor by the project. The energy–momentum tensor and field equations are taken from Chapter 7, and the source analysis reads the bilinears as ordinary numbers (mean field); the stability and quantum status of the negative-energy source are not examined. The attribution of the $q$ term to the rule of cell 1058 acting on the $+1$ entries only is a reconstruction. The Z2 mirror is a modelling choice of Stage 4, the brane stress it requires is not supplied by any computed matter, and the pairing of $\pm M$ under $\gamma^8$ is structural. The Randall–Sundrum comparison is quoted from the report.

### 9.18 Exercises

**Exercise 9.1.** At the point where $\sin z=3/5$, compute $\det g$ for an arbitrary value of $a_4$ and check that $\sqrt{\lvert g\rvert}=\cos z$.

**Exercise 9.2.** Let $H=1$. At which $\sin z$ is the hidden proper coordinate $\zeta=-1$? Check that the warp factor $e^{2H\zeta}$ equals $s^{1/3}$ there.

**Exercise 9.3.** Derive $\Gamma^j{}_{4j}=-Ha_4'$ and $\Gamma^4{}_{jj}=Ha_4'\,s^{1/3}e^{-2a_4}$ from the rules (C1) and (C2) of Section 9.6.

**Exercise 9.4.** Verify the Bianchi identity $\nabla_\mu G^\mu{}_\zeta=0$ for the Einstein tensor of Section 9.8 in the $\zeta$ chart.

**Exercise 9.5.** Take $a_4=2t$. Compute $R$, the mixed Einstein tensor, $\rho_{\mathrm{req}}$, the seven pressures and $w$, and compare $\rho_{\mathrm{req}}$ and $w$ with the plateau $A=2$ of the figure in Section 9.10.

**Exercise 9.6.** In the Gauss–Bonnet sum $\delta^{\mu_1\nu_1\mu_2\nu_2}_{\alpha_1\beta_1\alpha_2\beta_2}R^{\alpha_1\beta_1}{}_{\mu_1\nu_1}R^{\alpha_2\beta_2}{}_{\mu_2\nu_2}$, the determinant is a sum over permutations. Show that the permutation that exchanges the second and third lower positions contributes $-R^\mu{}_\nu R^\nu{}_\mu$.

**Exercise 9.7.** For the slopes $a_4'=\tfrac23(M\mp1)$ of cell 150, compute $R$ and show that $\rho_{\mathrm{req}}<0$ for every real $M$.

**Exercise 9.8.** Derive the NEC entries $\rho+p_{(i)}$ and $p_{(i)}-p_{(j)}$ of the table in Section 9.11.

**Exercise 9.9.** The Randall–Sundrum model has five coordinates $(y,x_0,x_1,x_2,x_3)$ with $x_0$ the time and $ds^2=dy^2+e^{-2k\lvert y\rvert}\bigl(-dx_0^2+dx_1^2+dx_2^2+dx_3^2\bigr)$. Use the Israel condition of Section 9.16 to find the brane stress $S^\mu{}_\nu$, its energy density and its pressure.

**Exercise 9.10.** Verify Case B of Proposition 9.4: with $H=\kappa=1$, $a_4=t$, $m=-15$, $\lambda=25/6$ and $S=12/5$, check conditions (2) and (3), and compute $M_{\mathrm{eff}}$, $\rho$, $p$ and $w$.

**Exercise 9.11.** Show that $\int_{-\infty}^{\infty}\varepsilon^2(y^2+\varepsilon^2)^{-3/2}\,dy=2$ for every $\varepsilon>0$, and that the integrand at $y=0$ equals $1/\varepsilon$.

**Exercise 9.12.** Test the rule of cell 1058 at $s=1/729$ and $a_4=\ln3$. Then take the 2 by 2 toy matrix $\gamma=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ (antisymmetric, $\gamma^2=-1$), form $\gamma'=\cosh(a)\,\gamma-\sinh(a)\,\lvert\gamma\rvert$, and compare $\gamma'^2$ with $(e^{a}\gamma)^2$.

### 9.19 Answers to the exercises

**Answer 9.1.** The determinant is the product of the diagonal entries, $\det g=\cot^2z\cdot s\,e^{6a_4}\cdot(-1)\cdot(-s\,e^{-6a_4})=\cot^2z\,s^2$; the exponentials cancel for every $a_4$. With $\sin z=3/5$: $\cos z=4/5$, $\cot^2z=16/9$, $s^2=9/25$, so $\det g=16/25=(4/5)^2=\cos^2z$ and $\sqrt{\lvert g\rvert}=4/5=\cos z$.

**Answer 9.2.** $\zeta=\ln(\sin z)/6=-1$ gives $\ln\sin z=-6$, so $\sin z=e^{-6}\approx0.00248$, a point close to the tip. There $e^{2H\zeta}=e^{-2}\approx0.1353$ and $s^{1/3}=(e^{-6})^{1/3}=e^{-2}$: the same number.

**Answer 9.3.** Rule (C1) with $\rho=j$ and $\mu=4$: $\Gamma^j{}_{4j}=\tfrac12\partial_4\ln\lvert g_{jj}\rvert=\tfrac12\partial_4\bigl(\tfrac13\ln s-2a_4\bigr)=\tfrac12(-2Ha_4')=-Ha_4'$, because $s$ does not depend on $x_4$ and $\partial_4a_4=Ha_4'$. Rule (C2) with $\rho=4$ and $\mu=j$: $\Gamma^4{}_{jj}=-\partial_4g_{jj}/(2g_{44})=\tfrac12\partial_4g_{jj}$. With $g_{jj}=-s^{1/3}e^{-2a_4}$, $\partial_4g_{jj}=-s^{1/3}e^{-2a_4}\cdot(-2Ha_4')=2Ha_4'\,s^{1/3}e^{-2a_4}$, and half of it is $Ha_4'\,s^{1/3}e^{-2a_4}$.

**Answer 9.4.** For diagonal $G$, $\nabla_\mu G^\mu{}_\zeta=\partial_\zeta G^\zeta{}_\zeta+\Gamma^\mu{}_{\mu\zeta}G^\zeta{}_\zeta-\sum_\mu\Gamma^\mu{}_{\mu\zeta}G^\mu{}_\mu$. In the $\zeta$ chart $G$ does not depend on $\zeta$, $\Gamma^\zeta{}_{\zeta\zeta}=\Gamma^4{}_{4\zeta}=0$ and $\Gamma^p{}_{p\zeta}=\partial_\zeta f_p=H$, so $\Gamma^\mu{}_{\mu\zeta}=6H$. Then

$$
\begin{aligned}
\nabla_\mu G^\mu{}_\zeta&=6H\bigl(-3H^2(a_4'^2-5)\bigr)-H\bigl[3H^2(15-3a_4'^2+a_4'')+3H^2(15-3a_4'^2-a_4'')\bigr]\\
&=(90-18a_4'^2)H^3-(90-18a_4'^2)H^3=0 .
\end{aligned}
$$

**Answer 9.5.** With $a_4'=2$ and $a_4''=0$: $R=6H^2(4-7)=-18H^2$; $G^0{}_0=-3H^2(4-5)=3H^2$; $G^i{}_i=H^2(15-12)=3H^2$; $G^4{}_4=3H^2(7+4)=33H^2$; $G^j{}_j=3H^2$. So $G^\mu{}_\nu=\mathrm{diag}(3,3,3,3,33,3,3,3)H^2$, $\rho_{\mathrm{req}}=-33H^2/\kappa$, all seven pressures $3H^2/\kappa$, and $w=3/(-33)=-1/11\approx-0.091$, in agreement with $w=(c^2-5)/(c^2+7)$ at $c=2$. On the plateau $A=2$ of the figure (units $H=\kappa=1$) panel (c) shows $\rho_{\mathrm{req}}=-33$ and panel (d) shows $w_{\mathrm{req}}\approx-0.09$.

**Answer 9.6.** Write the delta as the determinant of the matrix with entries $\delta^{u_r}_{l_c}$, upper list $u=(\mu_1,\nu_1,\mu_2,\nu_2)$ and lower list $l=(\alpha_1,\beta_1,\alpha_2,\beta_2)$. A determinant is the sum over permutations $\pi$ of $\mathrm{sgn}(\pi)\prod_r\delta^{u_r}_{l_{\pi(r)}}$. The permutation that exchanges positions 2 and 3 has sign $-1$ and sets $\alpha_1=\mu_1$, $\alpha_2=\nu_1$, $\beta_1=\mu_2$, $\beta_2=\nu_2$. Its term is $-R^{\mu_1\mu_2}{}_{\mu_1\nu_1}\,R^{\nu_1\nu_2}{}_{\mu_2\nu_2}$. In the first factor the first upper index is contracted with the first lower index, which gives the Ricci tensor $R^{\mu_2}{}_{\nu_1}$. In the second factor, reversing both pairs (two sign changes) gives $R^{\nu_2\nu_1}{}_{\nu_2\mu_2}=R^{\nu_1}{}_{\mu_2}$. The term is $-R^{\mu_2}{}_{\nu_1}R^{\nu_1}{}_{\mu_2}=-R^\mu{}_\nu R^\nu{}_\mu$.

**Answer 9.7.** $a_4'^2=\tfrac49(M\mp1)^2$ and $a_4''=0$. Then $R=6H^2\bigl(\tfrac49(M\mp1)^2-7\bigr)=\tfrac23H^2\bigl(4(M\mp1)^2-63\bigr)=\tfrac23H^2(4M^2\mp8M-59)$, and $\kappa\rho_{\mathrm{req}}=-3H^2\bigl(7+\tfrac49(M\mp1)^2\bigr)=-\tfrac13H^2\bigl(4(M\mp1)^2+63\bigr)$. A square is never negative, so the bracket is at least 63 and $\rho_{\mathrm{req}}<0$ for every real $M$. The common pressure is $\kappa p=H^2\bigl(15-\tfrac43(M\mp1)^2\bigr)=-\tfrac13H^2(4M^2\mp8M-41)$.

**Answer 9.8.** $\kappa(\rho+p_{(i)})=H^2\bigl[-3(7+a_4'^2)+15-3a_4'^2+a_4''\bigr]=H^2\bigl[-6-6a_4'^2+a_4''\bigr]$, which is negative unless $a_4''\ge6(1+a_4'^2)$. For the null vector $e_j+e_i$ the frame components are $T_{\hat j\hat j}=-p_{(j)}$ and $T_{\hat i\hat i}=p_{(i)}$, so $T(k,k)=p_{(i)}-p_{(j)}$, and $\kappa(p_{(i)}-p_{(j)})=H^2\bigl[(15-3a_4'^2+a_4'')-(15-3a_4'^2-a_4'')\bigr]=2H^2a_4''$.

**Answer 9.9.** Here all four directions along the brane are warped. For $y<0$, $g_{ab}=e^{2ky}\eta_{ab}$ and $K_{ab}=\tfrac12\partial_yg_{ab}=k\,g_{ab}$, so $K^a{}_b=k\,\delta^a_b$; for $y>0$, $K^a{}_b=-k\,\delta^a_b$. The jumps are $[K^a{}_b]=-2k\,\delta^a_b$ and $[K]=-8k$. The Israel condition gives $S^a{}_b=-\tfrac1\kappa\bigl(-2k+8k\bigr)\delta^a_b=-\tfrac{6k}{\kappa}\delta^a_b$. The energy density is $\rho=-S^0{}_0=6k/\kappa>0$ and every pressure is $p=S^i{}_i=-6k/\kappa=-\rho$: a pure positive tension $6k/\kappa$, as stated in Section 9.16.

**Answer 9.10.** Condition (2): $mS=-15\cdot\tfrac{12}{5}=-36=-36H^2/\kappa$. Condition (3): $\lambda S^2=\tfrac{25}{6}\cdot\tfrac{144}{25}=24$ and $2H^2(15-3c^2)/\kappa=2\cdot12=24$ for $c=1$. Then $M_{\mathrm{eff}}=-15+\tfrac{25}{6}\cdot\tfrac{12}{5}=-15+10=-5$, $\rho=mS+\tfrac\lambda2S^2=-36+12=-24$, $p=\tfrac\lambda2S^2=12$ and $w=12/(-24)=-\tfrac12$: exactly the required source of the notebook's $a_4=t$ in Section 9.10.

**Answer 9.11.** By the quotient rule, $\dfrac{d}{dy}\dfrac{y}{\sqrt{y^2+\varepsilon^2}}=\dfrac{\sqrt{y^2+\varepsilon^2}-y^2/\sqrt{y^2+\varepsilon^2}}{y^2+\varepsilon^2}=\dfrac{\varepsilon^2}{(y^2+\varepsilon^2)^{3/2}}$. So the integral is $\bigl[y/\sqrt{y^2+\varepsilon^2}\bigr]_{-\infty}^{\infty}=1-(-1)=2$, independent of $\varepsilon$. At $y=0$ the integrand is $\varepsilon^2/\varepsilon^3=1/\varepsilon$. As $\varepsilon\to0$ the spike becomes infinitely high and narrow with area 2: it tends to $2\delta(y)$, the second derivative of $\lvert y\rvert$.

**Answer 9.12.** $s=3^{-6}$ gives $s^{1/6}=1/3$ and $s^{1/3}=1/9$; $a_4=\ln3$ gives $e^{a_4}=3$ and $e^{2a_4}=9$. The left side is $1/\sqrt{(1/9)/9}=1/\sqrt{1/81}=9$; the correct right side is $e^{a_4}/s^{1/6}=3\cdot3=9$; the notebook's right side is $1/(3\cdot\tfrac13)=1$. For the toy matrix, $\lvert\gamma\rvert=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and

$$
\gamma'=\begin{pmatrix}0&\cosh a-\sinh a\\-\cosh a-\sinh a&0\end{pmatrix}=\begin{pmatrix}0&e^{-a}\\-e^{a}&0\end{pmatrix},\qquad \gamma'^2=\begin{pmatrix}-1&0\\0&-1\end{pmatrix},
$$

whereas $(e^{a}\gamma)^2=e^{2a}\gamma^2=-e^{2a}\cdot1$. They agree only for $a=0$. This is the 2 by 2 version of $(\gamma'^{\,x_5})^2=-s^{-1/3}$ against the required $-s^{-1/3}e^{2a_4}$ in Section 9.14.
