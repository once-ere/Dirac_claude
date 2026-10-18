## 3. Spacetime geometry and the author's metric; curvature

Gravity, in Einstein's theory, is not a force that acts inside space and time: it is the shape of space and time itself. This chapter builds, from nothing but school algebra and one-variable calculus, the language in which that shape is written down and measured: coordinates, the metric, its signature, scale factors and volumes, the Christoffel symbols, geodesics (the paths of free fall), and curvature in the form of the Riemann tensor, the Ricci tensor, the Ricci scalar, the Einstein tensor and the Kretschmann scalar. Every tool is tried first where we can picture it, on the flat plane and on a sphere, and then applied, completely and line by line, to the metric of the primordial gravitational field of the author's theory, in the corrected form that the Revision record uses. The chapter has four worked examples, Notebooks 03a, 03c, 03b and 03d (in the order in which the chapter uses them); each reproduces, number for number, the parts of the Revision record that it overlaps and says so in a PASS line.

### 3.1 What this chapter is for

Every later chapter of the book lives in the author's eight-dimensional spacetime. The spinor fields of Chapters 4 to 10 need its vielbein (the scale factors of Section 3.7); the energy-momentum tensor of Chapter 9 needs its Christoffel symbols (Section 3.23); the field equations of the metric functions $a_4$ and $b_4$ in Chapter 12 need its Einstein tensor (Section 3.25); the Kohn-Sham model of Chapters 14 to 17 (**Kohn-Sham**: an approximation of density functional theory that replaces many interacting particles by independent particles, each moving in one common effective potential; Chapter 13 teaches it from zero) is written in the hidden coordinate $y$ of Section 3.9. This chapter derives all of these from the metric itself, and it ends with what the metric does to a body that moves freely in it (Section 3.31).

The metric is the following diagonal $8 \times 8$ matrix, in the order of the author's coordinates $x_0, \dots, x_7$ (Section 3.5 reads it exactly as the Revision record stores it):

$$
\begin{aligned}
g = \mathrm{diag}\bigl(&e^{-2a_4}b_4\cot^2 z,\ e^{2a_4},\ e^{2a_4},\ e^{2a_4},\ -1,\\
&-e^{-2a_4}b_4(\sin^2 z)^{1/6},\ -e^{-2a_4}b_4(\sin^2 z)^{1/6},\ -e^{-2a_4}b_4(\sin^2 z)^{1/6}\bigr),\qquad z = 6Hx_0 .
\end{aligned}
$$

It is the **corrected metric** of 2026-10-16 (version 2), the metric of the Revision record (`Revision/SPEC.md`, section 1). The coordinates have fixed roles. $x_0$ is the **hidden** direction; it is space-like, and $z = 6Hx_0$ takes every real value. $x_1, x_2, x_3$ are ordinary **3-space**; it inflates, with the scale factor $e^{a_4}$, the same at every value of $z$. $x_4$ is **the time**. $x_5, x_6, x_7$ are three **extra times**: they are time-like like $x_4$, and they **deflate exponentially**, with the scale factor $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$; the hidden direction has the scale factor $e^{-a_4}b_4^{1/2}|\cot z|$ and shrinks together with them (on the history of Section 3.8 their common factor $e^{-a_4}b_4^{1/2}$ falls like $e^{-a_4/3}$). $H > 0$ is a constant of the author, and $a_4(x_4)$ and $b_4(x_4)$ are functions of the time only, the **metric functions**, with $b_4 > 0$; $b_4$ is never the constant 1. A prime means a derivative with respect to $x_4$, $a_4' = da_4/dx_4$ and $b_4' = db_4/dx_4$. The positive root $(\sin^2 z)^{1/6}$ is the author's $\sin^{1/3}z$, read on its positive branch so that it is defined for every real $z$. Every formula of this chapter is derived for general $a_4(x_4)$ and $b_4(x_4)$; the pictures and numbers along a history take the history of the Revision record, $a_4 = AHx_4$ and $b_4 = b_4(0)\,e^{\beta AHx_4}$ with $\beta = 4/3$, $b_4(0) = 1$, and say so (Section 3.8 gives the reasons).

The four notebooks of the chapter are:

| notebook | what it computes | Revision records it reproduces |
| --- | --- | --- |
| 03a | reads the corrected metric exactly as the record stores it; determinant, signature (4,4) for every real $z$ away from the degenerate points, the symmetries across the fold, vielbein, expansion rates, the deflating history, proper volumes, the hidden coordinate $y$ and the block form of the metric; 7 figures, 30 checks | `Revision/gkd_lovelock/results/curvature.json`, `python-lovelock-report.json` (same folder), `Revision/metric_warped/results/warped-metric.json`, `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`, `Revision/kohn_sham/results/parameters.json`, `Revision/kohn_sham/ks-theory.json` |
| 03c | curvature where it can be pictured: the flat plane in polar coordinates and the sphere; parallel transport, geodesics, geodesic deviation, all with RK4; 5 figures, 16 checks | none (exact formulas only) |
| 03b | all Christoffel symbols, Riemann, Ricci and Einstein components and the Kretschmann scalar of the corrected metric, exactly; finite differences; the curvature of every coordinate plane; the curvature along the deflating history; the source that Einstein's equations require; a negative control with the withdrawn metric of 2026-10-14; 7 figures, 43 checks | `curvature.json`, `python-lovelock-report.json`, `lovelock-report.json` (all three in `Revision/gkd_lovelock/results/`), `Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`, `warped-metric.json` and `python-warped-metric-report.json` (in `Revision/metric_warped/`), `Revision/field_equations_a4/a4-equations.json`, `Revision/field_equations_a4/reports/python-a4-report.json` |
| 03d | free fall in the corrected metric: conserved momenta, redshift in 3-space, blueshift along the extra times, the push of extra-time motion along the hidden direction, the law of the $x_4$ velocity; RK4 paths with the record's Christoffel symbols; 5 figures, 23 checks | `curvature.json`, `parameters.json`, `ks-theory.json`, `Revision/theory/reports/python-scope.json` |

Every statement of the chapter carries one of the five labels of Chapter 0. **PROVED** means derived exactly here, line by line, and confirmed by an exact check of a notebook (the few results that are derived only in the exercises say so); where the Revision record proves the same, the record file and its check are named. **COMPUTED** means a number obtained numerically by a notebook, with its measured accuracy. **ASSUMED** marks two kinds of statements: standard theorems that we quote without proof (each is named where it is used), and the physical inputs: that the history of the metric functions is $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{\beta AHx_4}$ with $\beta = 4/3$, which the Revision record itself calls a PRESCRIBED BACKGROUND (Section 3.8), and that the bodies of Section 3.31 are test particles, too small to change the metric. Two questions are **OPEN** (Section 3.31): whether wave packets of the fields follow the free-fall paths computed here, and what a path does when it reaches a point where the metric degenerates. No HYPOTHESIS enters this chapter. Nothing in this chapter concerns pairs of universes, their creation, or matter and antimatter; those questions belong to Chapters 18 to 21, which also state precisely what is and what is not proved about them.

### 3.2 Coordinates, indices and sums

**Coordinates.** A point of the author's spacetime is named by eight real numbers, its **coordinates** $x_0, x_1, \dots, x_7$. Their roles were listed in Section 3.1. In Python a list of eight numbers is counted from 0, and the author's names are counted from 0 too: position $k$ holds $x_k$, so position 0 is the hidden coordinate $x_0$ and position 4 the time $x_4$; every notebook says so where it matters.

**Indices.** A letter written as a small label, such as the $a$ in $x_a$, is an **index**: it stands for any one of the numbers $0, \dots, 7$. An equation with an index is eight equations, one for each value. Many objects of this chapter carry several indices: the metric $g_{ab}$ has two (it is a table with 64 entries), the Christoffel symbols $\Gamma^a{}_{bc}$ have three (512 entries), the Riemann tensor $R^a{}_{bcd}$ has four (4096 entries). An index may be written **up** or **down**; Section 3.14 explains why the position matters for vectors and tensors. For the coordinates themselves the position carries no meaning: $x_4$ and $x^4$ name the same coordinate, and we write $x_a$ in prose and $dx^a$ for a small step along $x_a$.

**Sums.** In this chapter every sum is written with the sign $\sum$; for example $\sum_{a=0}^{7} V^a W_a = V^0W_0 + V^1W_1 + \dots + V^7W_7$. When the range is the eight coordinates we write $\sum_a$. Where a formula repeats an index but does not sum over it we write "(no sum)".

**The Kronecker delta.** $\delta^a{}_b$ (also written $\delta_{ab}$) is $1$ when $a = b$ and $0$ otherwise. It is the table of the $8 \times 8$ unit matrix.

**Partial derivatives.** For a function $f(x_0, \dots, x_7)$ the **partial derivative** $\partial_a f = \partial f / \partial x_a$ is the ordinary derivative with respect to $x_a$ while the seven other coordinates are held fixed (Chapter 2 teaches it from zero). The author's metric depends on two coordinates only: on $x_4$ through $a_4(x_4)$ and $b_4(x_4)$, and on $x_0$ through $z = 6Hx_0$. By the **chain rule**, a function of $z$ has

$$
\partial_0 f = \frac{df}{dz}\,\frac{dz}{dx_0} = 6H\,\frac{df}{dz},
$$

(the derivative of a function of $z$ with respect to $x_0$ is its derivative with respect to $z$ times $dz/dx_0 = 6H$), and a function of $a_4$ and $b_4$ has $\partial_4 f = a_4'\, \partial f/\partial a_4 + b_4'\,\partial f/\partial b_4$ (the same rule for each of the two functions, with $da_4/dx_4 = a_4'$ and $db_4/dx_4 = b_4'$). Every other partial derivative of the metric is zero.

### 3.3 The metric: lengths from coordinate steps

**Pythagoras.** On a flat sheet of paper with perpendicular axes $x$ and $y$, a small step $dx$ to the right and $dy$ upwards has the squared length

$$
ds^2 = dx^2 + dy^2 .
$$

The coefficients of $dx^2$ and $dy^2$ are both $1$, and there is no term with $dx\,dy$.

**The same plane in polar coordinates.** Name a point instead by its distance $r$ from the origin and its angle $\varphi$ from the $x$ axis, so that $x = r\cos\varphi$ and $y = r\sin\varphi$. We compute $ds^2$ in these coordinates, line by line.

$$
dx = \cos\varphi\, dr - r\sin\varphi\, d\varphi, \qquad dy = \sin\varphi\, dr + r\cos\varphi\, d\varphi
$$

(the change of a function of two variables is the sum of its two partial derivatives times the two small changes: $dx = (\partial x/\partial r)\,dr + (\partial x/\partial\varphi)\,d\varphi$, and the same for $y$)

$$
dx^2 = \cos^2\varphi\, dr^2 - 2r\sin\varphi\cos\varphi\, dr\,d\varphi + r^2\sin^2\varphi\, d\varphi^2
$$

(the square of a difference, $(p - q)^2 = p^2 - 2pq + q^2$)

$$
dy^2 = \sin^2\varphi\, dr^2 + 2r\sin\varphi\cos\varphi\, dr\,d\varphi + r^2\cos^2\varphi\, d\varphi^2
$$

(the square of a sum, $(p + q)^2 = p^2 + 2pq + q^2$)

$$
ds^2 = dx^2 + dy^2 = dr^2 + r^2\, d\varphi^2
$$

(add the two lines: the mixed terms cancel, and $\cos^2\varphi + \sin^2\varphi = 1$ in both remaining pairs). The plane has not changed, but the coefficient of $d\varphi^2$ is now $r^2$, a number that depends on the point. A step $d\varphi$ in angle is a true length $r\,d\varphi$: the farther from the origin, the longer the arc.

**The metric.** In general coordinates $x_1, \dots, x_n$ of an $n$-dimensional space the squared length of a small step $dx^1, \dots, dx^n$ is a sum of products of two steps,

$$
ds^2 = \sum_{a=1}^{n}\sum_{b=1}^{n} g_{ab}\, dx^a dx^b ,
$$

with coefficients $g_{ab}$ that may depend on the point. The table $g_{ab}$ is the **metric**; we always take it **symmetric**, $g_{ab} = g_{ba}$ (the two products $dx^a dx^b$ and $dx^b dx^a$ are the same number, so only the sum $g_{ab} + g_{ba}$ matters, and we may share it equally). The formula for $ds^2$ is called the **line element**. A metric is **diagonal** when $g_{ab} = 0$ for $a \ne b$; then $ds^2 = \sum_a g_{aa}\,(dx^a)^2$. The plane in polar coordinates has the diagonal metric $g = \mathrm{diag}(1, r^2)$ in the order $(r, \varphi)$.

**The sphere.** On a sphere of radius $a$ name a point by the angle $\theta$ from the north pole and the angle $\varphi$ around the axis; in three dimensions it is $(a\sin\theta\cos\varphi,\ a\sin\theta\sin\varphi,\ a\cos\theta)$. A step $d\theta$ moves the point along a meridian, a circle of radius $a$, by the length $a\,d\theta$. A step $d\varphi$ moves it along the circle of latitude, whose radius is $a\sin\theta$, by the length $a\sin\theta\,d\varphi$. The two directions are perpendicular, so by Pythagoras

$$
ds^2 = a^2\, d\theta^2 + a^2\sin^2\theta\, d\varphi^2, \qquad g = \mathrm{diag}\bigl(a^2,\ a^2\sin^2\theta\bigr) .
$$

**The inverse metric.** The inverse matrix of $g_{ab}$ is written with upper indices, $g^{ab}$: $\sum_c g^{ac} g_{cb} = \delta^a{}_b$. For a diagonal metric it is diagonal too, with $g^{aa} = 1/g_{aa}$ (no sum), because the product of two diagonal matrices is the diagonal matrix of the products of their entries.

### 3.4 Signature: space-like and time-like directions

In the spacetime of special relativity with one space direction $x$ and the time $t$ (in units in which the speed of light is $1$) the line element is

$$
ds^2 = dx^2 - dt^2 .
$$

The coefficient of $dt^2$ is negative. A step $dt$ alone has $ds^2 = -dt^2 < 0$: it is not a length but a **duration**, and the time that a clock carried along the step shows, its **proper time**, is $d\tau = \sqrt{-ds^2} = dt$. A step with $dx = dt$ (one unit of distance per unit of time: a flash of light) has $ds^2 = 0$.

**Definitions.** A vector $V$ with components $V^1, \dots, V^n$ (Section 3.14 makes this precise) has the **squared length** $g(V, V) = \sum_{a,b} g_{ab} V^a V^b$. It is **space-like** if $g(V, V) > 0$, **time-like** if $g(V, V) < 0$ and **null** if $g(V, V) = 0$ but $V$ is not zero. For a diagonal metric a step along one coordinate $x_a$ is space-like when $g_{aa} > 0$ and time-like when $g_{aa} < 0$.

**Signature.** The **signature** $(p, q)$ of a metric at a point is the number $p$ of positive and the number $q$ of negative eigenvalues of the matrix $g_{ab}$. For a diagonal matrix the eigenvalues are the diagonal entries, so the signature counts the positive and the negative diagonal entries. A theorem of linear algebra, **Sylvester's law of inertia**, says that the signature does not depend on the coordinates (ASSUMED: quoted without proof). The flat metric with the signs of the author's metric is

$$
\eta = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)
$$

in the order $x_0, \dots, x_7$: four positive and four negative entries, the signature **(4,4)**. Four directions are space-like ($x_0, x_1, x_2, x_3$) and four are time-like ($x_4, x_5, x_6, x_7$). With four time-like directions one of them must be chosen as the time in which everything evolves; the author chooses $x_4$, and the other three are the extra times.

### 3.5 The author's metric

The Rust program `lovelock_gkd`, which computed the curvature of the metric for the Revision record, stored the text of the metric under the name `metricAsGiven` in its output file `Revision/gkd_lovelock/results/curvature.json`, followed by a note in brackets. Printed with one row of the matrix per line (Notebook 03a, In [3]):

```text
{{E^(-2 a4[x4]) b4[x4] Cot[6 H x0]^2,0,0,0,0,0,0,0},
{0,E^(2 a4[x4]),0,0,0,0,0,0},
{0,0,E^(2 a4[x4]),0,0,0,0,0},
{0,0,0,E^(2 a4[x4]),0,0,0,0},
{0,0,0,0,-1,0,0,0},
{0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6),0,0},
{0,0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6),0},
{0,0,0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6)}}
```

It is written in the notation of Mathematica: braces enclose a list (the matrix is a list of eight rows of eight entries, the rows and columns in the order $x_0, x_1, \dots, x_7$), `E^(...)` is $e$ to the power in brackets, `Sin` and `Cot` are the sine and the cotangent, `a4[x4]` and `b4[x4]` are the values of the functions $a_4$ and $b_4$ at $x_4$, and a blank between two factors means times. The note of the record says that this is the corrected primordial metric of 2026-10-16 (version 2) of `Revision/SPEC.md`, section 1, in the author's coordinates $x_0, \dots, x_7$, with $x_0$ space-like and $x_4$ the time, for every real $z = 6Hx_0$ with $\sin z\cos z \neq 0$, and with $(\sin^2 z)^{1/6}$ the positive branch. Only the eight diagonal entries are non-zero; the line element is therefore

$$
\begin{aligned}
ds^2 = {} & e^{-2a_4}b_4\cot^2 z\, dx_0^2 + e^{2a_4}\bigl(dx_1^2 + dx_2^2 + dx_3^2\bigr) - dx_4^2\\
& - e^{-2a_4}b_4(\sin^2 z)^{1/6}\bigl(dx_5^2 + dx_6^2 + dx_7^2\bigr) ,\qquad z = 6Hx_0 .
\end{aligned}
$$

**A dated note on the earlier metric.** The metric of 2026-10-14 had $\cot^2 z$ alone in the hidden entry and the factor $\sin^{1/3}z$ also on 3-space; its Einstein tensor has an off-diagonal component that no diagonal source can match unless $b_4$ is constant, and it was withdrawn on 2026-10-16 (`Revision/docs/METRIC_SELF_CONSISTENCY.md`). It appears in this chapter only once more, as the negative control of Notebook 03b.

**Reading it term by term.** A step $dx_1$ in 3-space has the true (proper) length $e^{a_4}\,dx_1$, the square root of its coefficient: when $a_4$ grows, 3-space **inflates**, and it does so at every value of $z$ alike (3-space has no factor that depends on $x_0$). A step $dx_5$ along an extra time has the proper duration $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}\,dx_5$, and a step $dx_0$ the proper length $e^{-a_4}b_4^{1/2}|\cot z|\,dx_0$. Both carry the common factor

$$
f = e^{-a_4}b_4^{1/2} ,
$$

the **hidden scale**. When $a_4$ grows faster than $\ln b_4^{1/2}$, $f$ shrinks: the three extra times and the hidden direction **deflate exponentially** together (their rate of change is $-a_4' + b_4'/(2b_4)$, Section 3.7; on the history of Section 3.8 it is $-a_4'/3$). A step $dx_4$ has $ds^2 = -dx_4^2$, so a clock at rest shows exactly $x_4$: the coordinate $x_4$ is the proper time of an observer at rest (Section 3.23 shows that such an observer is in free fall).

**Units.** $z = 6Hx_0$ is an angle (a pure number), so $H$ has the unit of an inverse length. In all numerical work of the chapter lengths and times are measured in units of $1/H$, which is the same as setting $H = 1$.

**Every real $z$: cells, halves, the fold and the tips.** The angle $z$ takes every real value, so $\sin z$ and $\cos z$ take both signs. The metric contains $z$ only through $\cot^2 z$ and $\sin^2 z$. Both repeat when $z$ grows by $\pi$, because $\cot(z + \pi) = \cot z$ and $\sin(z + \pi) = -\sin z$, whose square is $\sin^2 z$; and both are unchanged when $z$ is replaced by $\pi - z$, because $\cot(\pi - z) = -\cot z$ and $\sin(\pi - z) = \sin z$, and only squares enter. So the whole geometry is known once it is known on one **cell** $0 < z < \pi$ (PROVED; Notebook 03a checks both symmetries exactly, In [8]). The values of $z$ with $\sin z\cos z = 0$ are the **degenerate points**, where an entry of the metric vanishes or grows without bound; nothing in this chapter is computed there. They are of two kinds. Where $\cos z = 0$ ($z = \pi/2$ and its copies $\pi/2 + n\pi$), $\cot z = 0$ and so $g_{00} = 0$: this is the **fold**. It joins the two **halves** $0 < z < \pi/2$ and $\pi/2 < z < \pi$ of a cell, and the reflection $z \to \pi - z$ carries one half onto the other. Where $\sin z = 0$ ($z = 0$, $\pi$ and their copies), $\cot^2 z$ grows without bound and the extra-time entries vanish: these are the **tips**, the two ends of a cell. At the fold the matrix $g$ has no inverse, and the coordinate $x_0$ stops being a good label there (Section 3.9 introduces a coordinate that describes each half of a cell without this problem). How a field or a body continues through a degenerate point is not computed in this chapter (Section 3.31).

**The signature is (4,4) at every point with $\sin z\cos z \neq 0$, for every $a_4$ and every $b_4 > 0$** (PROVED). The proof is one line per sign: $e^{-2a_4} > 0$ and $e^{2a_4} > 0$ for every real $a_4$ (an exponential is positive), and $b_4 > 0$; where $\sin z \neq 0$ and $\cos z \neq 0$, $\cot z = \cos z/\sin z$ is defined and not zero, so $\cot^2 z > 0$ and $g_{00} > 0$; the three 3-space entries $e^{2a_4}$ are positive; $g_{44} = -1 < 0$; and where $\sin z \neq 0$, $(\sin^2 z)^{1/6}$ is the positive sixth root of a positive number, so the three extra-time entries, which carry a minus sign, are negative. So the signs are $(+,+,+,+,-,-,-,-)$, those of $\eta$ (record `Revision/metric_warped/reports/python-warped-metric-report.json`, check `corrected_metric_entries`). Notebook 03a confirms this on a grid of 800 values of $z$ across two cells, $-\pi < z < \pi$, 13 values of $a_4$ and three values of $b_4$ (In [8]); at $z = 0.7$, $a_4 = 0.5$ and $b_4 = e^{2/3}$ (the value on the history of Section 3.8 at $a_4 = 0.5$) it prints $g_{11} = 2.718282$ and $g_{55} = -0.618841$.

### 3.6 The determinant and proper volumes

**The volume of a small box.** In flat Cartesian coordinates a small box with edges $dx$, $dy$, $dz$ has the volume $dx\,dy\,dz$. In the plane in polar coordinates a small box with edges $dr$ and $d\varphi$ has the true edge lengths $dr$ and $r\,d\varphi$, so its area is $r\,dr\,d\varphi$. For any diagonal metric the same reasoning gives: a box with coordinate edges $dx^1, \dots, dx^n$ has the proper edge lengths $\sqrt{|g_{aa}|}\,dx^a$, and its proper volume is the product

$$
\prod_{a=1}^{n} \sqrt{|g_{aa}|}\;dx^1 \cdots dx^n = \sqrt{|\det g|}\;dx^1\cdots dx^n ,
$$

because the **determinant** of a diagonal matrix is the product of its diagonal entries, and the square root of a product of positive numbers is the product of their square roots. (For a metric that is not diagonal the volume factor is also $\sqrt{|\det g|}$; we quote this without proof, ASSUMED, and do not need it.) The factor $\sqrt{|\det g|}$ is the **volume factor**.

**The determinant of the author's metric.** We compute it line by line; after each line we name the rule that produced it.

$$
\det g = g_{00}\,g_{11}\,g_{22}\,g_{33}\,g_{44}\,g_{55}\,g_{66}\,g_{77}
$$

(the determinant of a diagonal matrix is the product of its diagonal entries)

$$
= e^{-2a_4}b_4\cot^2 z\cdot\bigl(e^{2a_4}\bigr)^3\cdot(-1)\cdot\bigl(-e^{-2a_4}b_4(\sin^2 z)^{1/6}\bigr)^3
$$

(the entries inserted; three equal factors written as a cube)

$$
= e^{-2a_4}b_4\cot^2 z\cdot e^{6a_4}\cdot(-1)\cdot\bigl(-e^{-6a_4}b_4^3(\sin^2 z)^{1/2}\bigr)
$$

(a power of a product is the product of the powers: $(e^{2a_4})^3 = e^{6a_4}$, $(e^{-2a_4})^3 = e^{-6a_4}$, $((\sin^2 z)^{1/6})^3 = (\sin^2 z)^{1/2}$; and an odd power keeps the minus sign, $(-1)^3 = -1$)

$$
= e^{-2a_4}b_4^4\cot^2 z\,(\sin^2 z)^{1/2}
$$

(the two minus signs multiply to $+1$; $e^{6a_4}e^{-6a_4} = e^0 = 1$; $b_4\cdot b_4^3 = b_4^4$)

$$
= e^{-2a_4}b_4^4\cot^2 z\,|\sin z|
$$

(the positive square root of $\sin^2 z$ is $|\sin z|$). Every factor is positive away from the degenerate points, so $|\det g| = \det g$, and

$$
\sqrt{|\det g|} = e^{-a_4}b_4^2\,|\cot z|\,(\sin^2 z)^{1/4}
$$

(the square root of a product of positive numbers is the product of the square roots: $\sqrt{e^{-2a_4}} = e^{-a_4}$, $\sqrt{b_4^4} = b_4^2$, $\sqrt{\cot^2 z} = |\cot z|$ and $\sqrt{|\sin z|} = (\sin^2 z)^{1/4}$). This is PROVED here and in the Revision record (`Revision/gkd_lovelock/results/python-lovelock-report.json`, check `sqrt_abs_det_g`; `curvature.json` stores $\sqrt{|\det g|}$ under the name `sqrtAbsDetG`, with $|\cot z|$ written as the cotangent times its sign, `Cot[6*H*x0]*Sign[Cot[6*H*x0]]`; the record of the corrected metric, `Revision/metric_warped/results/warped-metric.json`, key `sqrt_det_g_corrected`); Notebook 03a reproduces all three and compares numbers at eight points, two in each quarter of the period (In [7]). Since $|\cot z|(\sin^2 z)^{1/4} = (|\cos z|/|\sin z|)\,|\sin z|^{1/2} = |\cos z|/|\sin z|^{1/2}$, the volume factor vanishes at the fold and grows without bound towards each tip. The function $a_4$ does not drop out: the factor $e^{6a_4}$ of the three inflating 3-space directions and the factor $e^{-6a_4}$ of the three deflating extra times cancel, but the factor $e^{-2a_4}$ of the hidden direction is left over, because the hidden direction shrinks together with the extra times. Of the four factors $b_4$, three come from the extra times and one from the hidden direction.

**The volume of a slice of constant time.** The time $x_4$ is the time in which everything in this book evolves (it is the time shown by the clocks of observers at rest, Section 3.23). The natural volume is therefore that of a slice $x_4 = \mathrm{const}$, the whole space at one instant of $x_4$: a seven-dimensional space with the coordinates $x_0, x_1, x_2, x_3, x_5, x_6, x_7$. This 7-volume mixes kinds of steps: four of its edges are lengths (along $x_0, x_1, x_2, x_3$) and three are durations (along the extra times $x_5, x_6, x_7$, which are time-like, Section 3.4). Its volume factor is the product of the seven scale factors other than that of $x_4$, which is $\sqrt{|g_{44}|} = 1$; so it equals $\sqrt{|\det g|}$. Its rate of change in time is

$$
\partial_4\ln\sqrt{|\det g|} = \partial_4\bigl(-a_4 + 2\ln b_4 + \ln(|\cot z|(\sin^2 z)^{1/4})\bigr) = -a_4' + \frac{2b_4'}{b_4}
$$

(the logarithm of a product is the sum of the logarithms, $\ln e^{-a_4} = -a_4$ and $\ln b_4^2 = 2\ln b_4$; the last logarithm does not depend on $x_4$; the derivative of $\ln b_4$ is $b_4'/b_4$). On the history of Section 3.8, $b_4'/b_4 = \frac43 a_4'$, so the rate is $-a_4' + \frac83 a_4' = \frac53 a_4'$: **the proper 7-volume of a region with fixed coordinate ranges grows like $e^{5a_4/3}$**; the inflation of 3-space wins over the deflation of the four directions of the hidden direction and the extra times (PROVED; Notebook 03a, In [17] and In [18]).

**Three partial volumes.** Take a box with the coordinate edges $\Delta x_1 = \Delta x_2 = \Delta x_3 = 1$ (small enough that $z$ hardly changes along it, or at one value of $z$). Its proper 3-volume in 3-space is

$$
V_3 = \bigl(e^{a_4}\bigr)^3 = e^{3a_4}
$$

(the product of three equal scale factors). The same box in the three extra times has $V_t = \bigl(f(\sin^2 z)^{1/12}\bigr)^3 = b_4^{3/2}e^{-3a_4}(\sin^2 z)^{1/4}$ (with $f^3 = e^{-3a_4}b_4^{3/2}$ and $((\sin^2 z)^{1/12})^3 = (\sin^2 z)^{1/4}$), and $V_3V_t = b_4^{3/2}(\sin^2 z)^{1/4}$ (the exponentials cancel). What 3-space gains in volume through $a_4$, the extra times lose; the hidden scale factor $f|\cot z|$ then brings the factor $e^{-a_4}b_4^{1/2}|\cot z|$ that turns $V_3V_t$ into $\sqrt{|\det g|}$.

**The 7-volume of a half cell.** Per unit coordinate volume of the six directions $x_1, x_2, x_3, x_5, x_6, x_7$, the proper 7-volume of the half cell $0 < z < \pi/2$ is the integral of the volume factor over $x_0$ from $0$ to $\pi/(12H)$. The factor $e^{-a_4}b_4^2$ does not depend on $x_0$ and comes out of the integral, which leaves

$$
\int_0^{\pi/(12H)} \cot(6Hx_0)\,\sin^{1/2}(6Hx_0)\,dx_0
$$

(on the half cell $\cot z > 0$ and $\sin z > 0$, so $|\cot z| = \cot z$ and $(\sin^2 z)^{1/4} = \sin^{1/2}z$)

$$
= \frac{1}{6H}\int_0^{\pi/2}\frac{\cos z}{\sin z}\,\sin^{1/2}z\,dz = \frac{1}{6H}\int_0^{\pi/2}\cos z\,\sin^{-1/2}z\,dz
$$

(the substitution $z = 6Hx_0$, $dx_0 = dz/(6H)$, which turns the limits $0$ and $\pi/(12H)$ into $0$ and $\pi/2$; then $\sin^{1/2}z/\sin z = \sin^{-1/2}z$)

$$
= \frac{1}{6H}\int_0^1 s^{-1/2}\,ds = \frac{1}{6H}\Bigl[2s^{1/2}\Bigr]_0^1 = \frac{1}{3H}
$$

(the substitution $s = \sin z$, $ds = \cos z\,dz$, with the limits $\sin 0 = 0$ and $\sin(\pi/2) = 1$; an antiderivative of $s^{-1/2}$ is $2s^{1/2}$, as differentiating shows). So the 7-volume of a half cell is $e^{-a_4}b_4^2/(3H)$. The volume factor grows without bound at the tip, like $s^{-1/2}$, but its integral is finite. By the two symmetries of Section 3.5 every other half cell has the same 7-volume. PROVED; Notebook 03a computes the integral over $s$ with sympy (In [17]).

### 3.7 Scale factors, the vielbein and the rates of expansion

**Scale factors.** Write each diagonal entry as a sign times a square, $g_{aa} = \eta_{aa}\,h_a^2$ with a positive number $h_a$, the **scale factor** of the direction $x_a$: a coordinate interval $\Delta x_a$ over which $h_a$ does not change has the proper length (or, for a time-like direction, the proper duration) $h_a\,\Delta x_a$. For the corrected metric, with the hidden scale $f = e^{-a_4}b_4^{1/2}$ of Section 3.5,

$$
\begin{aligned}
h = \bigl(&f|\cot z|,\ e^{a_4},\ e^{a_4},\ e^{a_4},\ 1,\\
&f(\sin^2 z)^{1/12},\ f(\sin^2 z)^{1/12},\ f(\sin^2 z)^{1/12}\bigr)
\end{aligned}
$$

in the order $x_0, \dots, x_7$ (the positive square roots of the absolute values of the diagonal entries; the root of a product is the product of the roots: $\sqrt{e^{-2a_4}b_4\cot^2 z} = e^{-a_4}b_4^{1/2}|\cot z|$, $\sqrt{e^{2a_4}} = e^{a_4}$ and $\sqrt{e^{-2a_4}b_4(\sin^2 z)^{1/6}} = e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$). The factor $(\sin^2 z)^{1/12} = |\sin z|^{1/6}$ that the three extra times share is their **warp factor** $W$; their metric entries contain its square $W^2 = (\sin^2 z)^{1/6}$. 3-space has no warp factor, and the hidden direction has $|\cot z|$ instead.

**The vielbein.** At every point imagine eight measuring rods and clocks of unit proper length, one along each coordinate direction, all perpendicular to each other. Such a set is a **frame**, and the matrix $e^a{}_\mu$ that converts coordinate steps into frame components is the **vielbein** (German for "many legs"): the metric is

$$
g_{\mu\nu} = \sum_{a,b} e^a{}_\mu\,\eta_{ab}\,e^b{}_\nu .
$$

For a diagonal metric the diagonal vielbein $e^a{}_\mu = h_\mu\,\delta^a{}_\mu$ (no sum) does this: the double sum keeps only $a = b = \mu = \nu$ and gives $\eta_{\mu\mu} h_\mu^2 = g_{\mu\mu}$. The Revision record keeps the sign of $\cot z$ in the hidden entry, $e^0{}_0 = e^{-a_4}b_4^{1/2}\cot z$, which changes nothing in the metric because only its square enters (`Revision/metric_warped/results/warped-metric.json`, key `vielbein_corrected`). The spinor fields of the book need exactly this frame (Chapter 6). PROVED here. The Revision record also contains the **lead checks**: short, independent Python programs in the folder `Revision/lead_checks`, written from scratch by the coordinator of the Revision work (the "lead") without using any other Revision code, each of which writes a report listing its named checks and their verdicts. The lead's check `vielbein_reproduces_metric` of `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json` checks the same, and Notebook 03a reproduces it (In [11]).

**The rate of expansion.** A coordinate interval $\Delta x_a$ has the proper length $L = h_a\,\Delta x_a$. The fraction by which it grows per unit of time is

$$
\frac{1}{L}\frac{\partial L}{\partial x_4} = \frac{\partial_4 h_a}{h_a} = \partial_4 \ln h_a
$$

(the coordinate interval does not change; the derivative of $\ln u$ is $u'/u$). For 3-space,

$$
\ln h_1 = a_4 \quad\Rightarrow\quad \partial_4 \ln h_1 = a_4'
$$

($\ln e^{a_4} = a_4$). For an extra time,

$$
\ln h_5 = \tfrac12\ln b_4 - a_4 + \tfrac1{12}\ln\sin^2 z \quad\Rightarrow\quad \partial_4 \ln h_5 = -a_4' + \frac{b_4'}{2b_4} \equiv \alpha_t
$$

(the logarithm of a product is the sum of the logarithms, with $\ln b_4^{1/2} = \frac12\ln b_4$, whose derivative is $b_4'/(2b_4)$; the term with $z$ does not depend on $x_4$). For the hidden direction,

$$
\ln h_0 = \tfrac12\ln b_4 - a_4 + \ln|\cot z| \quad\Rightarrow\quad \partial_4 \ln h_0 = -a_4' + \frac{b_4'}{2b_4} = \alpha_t
$$

(the same rules). We call $\alpha_t$ the **rate of the hidden direction and the extra times**: they change at one common rate, because they share the factor $f$, whose logarithm has the derivative $\alpha_t$. $h_4 = 1$ does not depend on $x_4$, so its rate is $0$. On the history of Section 3.8, $b_4'/b_4 = \frac43 a_4'$ and so $\alpha_t = -a_4' + \frac23 a_4' = -\frac13 a_4'$: **3-space expands at the rate $a_4'$, and the hidden direction and the three extra times shrink at one third of that rate**. The six scale factors of $x_1, x_2, x_3, x_5, x_6, x_7$ multiply to

$$
h_1 h_2 h_3 h_5 h_6 h_7 = e^{3a_4}\cdot e^{-3a_4}b_4^{3/2}(\sin^2 z)^{1/4} = b_4^{3/2}(\sin^2 z)^{1/4} ,
$$

without $a_4$, and with the hidden factor $h_0 = f|\cot z|$ the seven give $\sqrt{|\det g|}$ of Section 3.6. All of this is PROVED and is checked exactly by Notebook 03a (In [12], with the check that the four scale factors of the hidden direction and the extra times are $f$ times functions of $z$ alone and that the 3-space factor does not depend on $z$).

### 3.8 The deflating history: a prescribed background

The metric does not fix the functions $a_4(x_4)$ and $b_4(x_4)$. The field equations of gravity relate them to the energy and the pressures of the matter in the spacetime; Chapter 12 derives them. In the corrected metric every choice of $a_4$ and $b_4$ gives field equations without off-diagonal components (Section 3.25), so the metric itself singles out no history. The Revision record keeps one history for all its calculations, for continuity with its earlier work (`Revision/SPEC.md`, section 1; `Revision/kohn_sham/ks-theory.json`, key `adiabaticity.historyBetaSource`), and this chapter uses it for all pictures and numbers: the **exponential history**

$$
a_4 = AHx_4, \quad a_4' = AH, \quad a_4'' = 0, \qquad b_4 = b_4(0)\,e^{\beta AHx_4}, \quad \frac{b_4'}{b_4} = \beta AH, \qquad \beta = \frac43 ,
$$

with a constant **slope** $A$ and $b_4(0) = 1$. The constant $b_4(0) > 0$ is the value of $b_4$ at $x_4 = 0$. In the corrected metric it is not a matter of units: $b_4$ stands in the hidden entry as well as in the extra-time entries, so a rescaling of the extra times no longer removes a constant factor of $b_4$, and $b_4$ enters the curvature through the combination $e^{2a_4}/b_4$ (Section 3.24); the record uses $b_4(0) = 1$ (`Revision/docs/METRIC_SELF_CONSISTENCY.md`, its section 3.3). With $A > 0$ the function $a_4$ increases, 3-space inflates like $e^{AHx_4}$, and the hidden scale

$$
f = e^{-a_4}b_4^{1/2} = b_4(0)^{1/2}\,e^{-(1 - \beta/2)AHx_4} = e^{-AHx_4/3}
$$

(the power of a product; $1 - \beta/2 = 1 - \frac23 = \frac13$; $b_4(0) = 1$) shrinks: the extra times and the hidden direction deflate exponentially, as the author requires, at one third of the rate at which 3-space inflates (their rate is $\alpha_t = -AH/3$, Section 3.7). The Revision Kohn-Sham work uses $A = 1$ and $H = 1$, and computes its states on five **slices** $a_4 = 0, 0.5, 1, 1.5, 2$ (record `Revision/kohn_sham/results/parameters.json`, keys `physics.H`, `physics.historyA`, `physics.historyBeta`, `physics.historyB4AtZero`, `physics.slicesA4`, and the rule `physics.hiddenScaleRule`, which states $f = e^{(\beta/2 - 1)a_4}$; Notebook 03a, In [13]). Between the first and the last slice, 3-space lengths grow by the factor $e^2 = 7.389056$ and the hidden scale shrinks by the factor $e^{-2/3} = 0.513417$ (Notebook 03a, In [14]); the product of the two factors grows like $e^{2a_4/3}$, to $e^{4/3} = 3.79$ at the last slice.

**Status: ASSUMED.** The history is not a solution of the coupled field equations. The Revision record says so in its own words (`Revision/kohn_sham/ks-theory.json`, key `adiabaticity.historyStatus`): "PRESCRIBED BACKGROUND: the history a4 = H x4, b4 = e^{(4/3) H x4} is prescribed, not solved for." The reason, also stated there: the field equations of $a_4$ and $b_4$ allow this history only with a diagonal source whose hidden pressure equals its extra-time pressure, $p_0 = p_t$, and that grows with $x_4$ (with the author's Lovelock weights: record `Revision/field_equations_a4/a4-equations.json`, key `exponentialHistory.authorWeights.historySource_kappaT_minus_Lam`; with Einstein's equations: Section 3.26 and `Revision/metric_warped/results/warped-metric.json`, key `history_source`). No Kohn-Sham state of the record supplies this source: every non-zero state depends on $x_0$ (record `Revision/field_equations_a4/reports/ks-source-conditions.json`, check `ks_profiles_depend_on_x0`, and its conclusion). Every formula of this chapter written with general $a_4(x_4)$ and $b_4(x_4)$ is exact; only the pictures and the numbers along the history use the assumption. The pictures and numbers of this chapter use only slopes $A > 0$, for which the extra times deflate, as the author requires; a slope $A = 0$ would freeze both $a_4$ and $b_4$ (a constant $b_4$, which the author excludes), and a slope $A < 0$ would make the extra times and the hidden direction inflate and 3-space deflate.

### 3.9 The hidden coordinate y and the block form of the metric

The entry $e^{-2a_4}b_4\cot^2 z$ makes the hidden direction awkward: it grows without bound at the tips and vanishes at the fold. The Revision Kohn-Sham work uses instead the coordinate

$$
y = \frac{\ln|\sin z|}{6H} = \frac{\ln(\sin^2 z)}{12H}, \qquad z = 6Hx_0 ,
$$

defined wherever $\sin z \neq 0$ (the two forms agree because $\ln\sin^2 z = \ln|\sin z|^2 = 2\ln|\sin z|$).

**A step $dy$ has the proper length $f\,dy$.** Line by line:

$$
\frac{dy}{dx_0} = \frac{1}{12H}\cdot\frac{2\sin z\cos z}{\sin^2 z}\cdot 6H
$$

(the chain rule: the derivative of $\ln u$ is $1/u$ times the derivative of $u$; the derivative of $\sin^2 z$ with respect to $z$ is $2\sin z\cos z$; and $dz/dx_0 = 6H$)

$$
= \frac{\cos z}{\sin z} = \cot z
$$

(the factors $12H$ and $2\cdot 6H$ cancel, and one $\sin z$ cancels). So $dy = \cot z\,dx_0$ for every real $z$ with $\sin z \neq 0$, $dy^2 = \cot^2 z\,dx_0^2$, and

$$
g_{00}\,dx_0^2 = e^{-2a_4}b_4\cot^2 z\,dx_0^2 = f^2\,dy^2 :
$$

a step $dy$ along the hidden direction has the proper length $f\,dy$ (record `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`, check `ks_coordinate_jacobian`; Notebook 03a, In [19]).

**The warp factor in $y$.** From the definition, $12Hy = \ln\sin^2 z$, so

$$
\sin^2 z = e^{12Hy}
$$

($e$ to the power of both sides; $e^{\ln u} = u$), and therefore

$$
W = (\sin^2 z)^{1/12} = \bigl(e^{12Hy}\bigr)^{1/12} = e^{Hy}, \qquad W^2 = (\sin^2 z)^{1/6} = e^{2Hy}
$$

(a power of a power multiplies the exponents). Inserting $f^2\,dy^2$ and $W^2$ into the line element of Section 3.5 gives the **block form**

$$
ds^2 = e^{2a_4}\bigl(dx_1^2 + dx_2^2 + dx_3^2\bigr) - dx_4^2 + f^2\Bigl[dy^2 - e^{2Hy}\bigl(dx_5^2 + dx_6^2 + dx_7^2\bigr)\Bigr], \qquad f = e^{-a_4}b_4^{1/2} .
$$

The hidden direction and the three extra times form one **block** with the common factor $f^2$: they shrink together. This is exactly the line element of the record (`Revision/kohn_sham/ks-theory.json`, keys `geometry.lineElement`, `geometry.hiddenScale` and `geometry.warp`, the last of which says that the warp acts on the extra times only and that 3-space has no warp); Notebook 03a writes the metric in $y$ on each of the four quarters of the period and checks the form entry by entry with sympy (In [19]). PROVED. The four-dimensional metric in the square bracket, $dy^2 - e^{2Hy}(dx_5^2 + dx_6^2 + dx_7^2)$, has the signature (1,3) and the same curvature $-H^2$ in each of its six coordinate planes, a **space of constant curvature** $-H^2$ (record `Revision/metric_warped/reports/python-warped-metric-report.json`, check `hidden_block_constant_curvature`; Section 3.24 computes it by hand). The corrected metric is therefore built from two pieces over the time line: flat 3-space with the scale factor $e^{a_4}$, and this block with the scale factor $f$.

**The range of $y$.** On the half cell $0 < z < \pi/2$, $|\sin z|$ runs from $0$ to $1$ and $\ln|\sin z|$ from $-\infty$ to $0$, so $y$ runs from $-\infty$ (the tip) to $0$ (the fold); $y$ grows steadily there, because $dy/dx_0 = \cot z > 0$. On the other half, $\pi/2 < z < \pi$, it falls from $0$ back to $-\infty$, because there $\cot z < 0$. So each half of a cell is the whole range $-\infty < y \le 0$, and the two halves meet at the fold $y = 0$: the record calls the two halves together the "doubled system" (key `geometry.hiddenCoordinate`). The tip lies at an infinite proper distance from every point of a half cell, because the proper distance from the fold is $f\,|y|$ and $|y|$ grows without bound as $z \to 0$ (PROVED; Notebook 03a, In [19]). On each half the coefficient of $dy^2$ stays $f^2$ up to the fold $y = 0$: in the coordinate $y$ the vanishing of $g_{00}$ disappears, because near the fold a step $dx_0$ has a proper length that shrinks to nothing. How the two halves join where they meet is not decided by this coordinate. The Revision record computes nothing at the degenerate points (`Revision/docs/LOVELOCK_GKD.md`, its section 12.2); what a field or a body does when it reaches the fold is not answered in this chapter (Section 3.31); and the boundary conditions that the Kohn-Sham work imposes at the fold are ASSUMED and are the subject of Chapter 14.

**The volume factor in $y$.** In the coordinates $(y, x_1, \dots, x_7)$ the scale factor of the hidden direction is $f$, so the volume factor is

$$
f\cdot e^{3a_4}\cdot\bigl(fe^{Hy}\bigr)^3 = e^{3a_4}f^4e^{3Hy} = e^{-a_4}b_4^2\,e^{3Hy}
$$

($f^4 = e^{-4a_4}b_4^2$ and $e^{3a_4}e^{-4a_4} = e^{-a_4}$), the record's key `geometry.sqrtDetG`: "e^{-a4} b4^2 e^{3Hy} (= e^{-a4} b4^2 |cot z| (sin^2 z)^{1/4} in the author's chart x0..x7)". The two volume factors describe the same volume: on a half cell where $\cot z > 0$, $dx_0 = dy/\cot z$, so $e^{-a_4}b_4^2\cot z\,(\sin^2 z)^{1/4}\,dx_0 = e^{-a_4}b_4^2(\sin^2 z)^{1/4}\,dy$, and $(\sin^2 z)^{1/4} = |\sin z|^{1/2} = e^{3Hy}$ (Notebook 03a checks the determinant in $y$, In [19]).

**The tip cut-off.** The Revision Kohn-Sham solver keeps only $-L \le y \le 0$ of each half cell, with $L = 3/H$ (record `parameters.json`, key `physics.L_tipCutoff`); its proper hidden length is $fL$ (key `geometry.hiddenScale`). The fraction of the 7-volume of a half cell that it leaves out is (the factor $e^{-a_4}b_4^2$ does not depend on $y$ and cancels in the ratio)

$$
\frac{\int_{-\infty}^{-L} e^{3Hy}\,dy}{\int_{-\infty}^{0} e^{3Hy}\,dy} = \frac{e^{-3HL}/(3H)}{1/(3H)} = e^{-3HL}
$$

(an antiderivative of $e^{3Hy}$ is $e^{3Hy}/(3H)$, which tends to $0$ as $y \to -\infty$), which for $L = 3/H$ is $e^{-9} = 1.2341\times 10^{-4}$. The cut-off lies at the tiny angle $z$ with $|\sin z| = e^{6Hy} = e^{-18}$, $z = \arcsin e^{-18} = 1.5230\times 10^{-8}$ (the fraction exact in sympy, both numbers COMPUTED in Notebook 03a, In [20]).

### 3.10 Example: the corrected metric, read and checked

Notebook 03a puts Sections 3.2 to 3.9 to work. It reads the corrected metric exactly as the record `curvature.json` stores it and turns the text into an exact sympy matrix; checks it against a second, hand-typed copy and against the record's diagonal entries; computes the determinant and the volume factor and compares them with three records; checks the signature on a grid of two cells and the two symmetries of every entry; builds the vielbein and the expansion rates; reads the history of the Revision Kohn-Sham work ($a_4 = AHx_4$ with $b_4 = b_4(0)\,e^{4AHx_4/3}$) and its status, and draws the scale factors along it; draws the functions of $z$ and maps of the scale factors over the time and the cell; computes the proper volumes; and checks the hidden coordinate $y$, the block form and the volume factor in $y$ against the record `ks-theory.json`. It needs no Rust, runs in about 15 seconds and ends with the line ALL 30 CHECKS PASSED (notebook 03a).

<!-- NOTEBOOK 03a -->

### 3.13 Line-by-line walk-through of Notebook 03a

The notebook has 21 code cells, In [1] to In [21]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted and then explained. A line that starts with `#` is a **comment**, which Python skips; it is there for the reader. In the quoted code a line `...` stands for the remaining lines of a long figure caption; every caption is printed in full under its figure in Section 3.12, and a paragraph "What Figure 03a.k shows" after the code says what to look for.

**In [1], the set-up cell.** Its first part is the complete run instructions of Section 3.11 again, as comment lines, so that the notebook file carries its own instructions. The code starts below the line that announces THE SET-UP. The set-up code is the same in every notebook of the book except for one line (the notebook's name); we explain it here once, and the walk-throughs of Notebooks 03c, 03b and 03d refer back to this explanation.

```python
# THE SET-UP (the same in every notebook of this book; it computes no physics)
# =======================================================================================
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module** (a part of Python or of an installed package) so that the code can use it. `json` reads and writes the text format JSON, in which the Revision record stores its results; `os` gives access to the computer's environment; `textwrap` breaks long text into lines; `from pathlib import Path` takes the single name `Path` out of the module `pathlib`. A `Path` is the address of a file or a folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell

NOTEBOOK_ID = "03a"  # this notebook: chapter 03, example a
```

These lines load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python), which show a picture file below a cell. A **variable** is a name for a value: the last line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"03a"`. It is the only line of the set-up code that differs between notebooks.

```python
def find_repository_root():
    """Return the repository folder (Dirac_claude).

    Jupyter runs a notebook in the folder that holds it.  Starting there, go up one
    folder at a time until a folder contains Revision/textbook/requirements.txt (the
    list of the book's packages); that folder is the repository."""
    here = Path.cwd().resolve()  # the folder in which this notebook runs
    for folder in [here, *here.parents]:  # this folder, its parent, its grandparent ...
        if (folder / "Revision" / "textbook" / "requirements.txt").is_file():
            return folder
    raise FileNotFoundError(
        "The repository folder was not found: open this notebook inside the folder "
        "Revision/textbook/notebooks of the repository Dirac_claude")
```

`def` defines a **function**: a named piece of code that runs when it is called. The text in triple quotes under the `def` line is its **docstring**, a description that Python stores but does not run. `Path.cwd()` is the folder in which the notebook runs and `.resolve()` writes it as a complete address. `here.parents` is the list of the folders above it; `[here, *here.parents]` is the list that starts with `here` and continues with all of them (the star unpacks one list into another). The `for` loop takes these folders one after the other; the operator `/` joins a folder and a name into a longer path; `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If none does, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

`REPO` is the repository folder. `os.environ` holds the **environment variables** of the running program (named texts that the computer hands to it); `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and otherwise the default, the repository folder written as a string. When you run the notebook the variable is not set, so the notebook writes into the repository; the book's checking tool sets it to a scratch folder.

```python
def repository_file(relative):
    """The path of the repository file relative, for READING (a Revision record)."""
    return REPO / relative


def output_file(relative):
    """The path at which to WRITE the repository file relative (its folder is made)."""
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

`repository_file("Revision/...")` gives the full path of a repository file, for reading a Revision record. `output_file("Revision/...")` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates the folder that will hold it (and any missing folder above it) and does nothing if it exists.

```python
def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))


matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`say` prints a text in lines of at most 89 characters; `textwrap.fill` breaks it at blanks, and every line after the first starts with four blanks. `matplotlib.rcdefaults()` returns to matplotlib's built-in settings, so that a personal settings file cannot change the figures. `plt.rcParams.update({...})` then sets, for every figure of the notebook, the size (7.0 by 4.2 inches), the size of the letters (10 points) and a faint grid (30 per cent opaque). The braces make a **dictionary**: pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/03a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty dictionary and a line end into the captions file; `encoding="utf-8"` fixes how letters are stored and `newline="\n"` stores the same line end on every system.

```python
def save_figure(fig, name, caption):
    """Save the figure fig as Revision/textbook/figures/<id>_<k>_<name>.png, record its
    caption in CAPTION_FILE, show the saved picture below the cell and close the figure.
    k counts the figures of the notebook 1, 2, 3, ...; a cell run again keeps its k."""
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
    # dpi=150: 150 dots per inch.  bbox_inches="tight": cut away the empty margin.
    # metadata={"Software": None}: no program name is stored in the PNG file, so that
    # every run writes exactly the same bytes.
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

`setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far; so the figures are numbered 1, 2, 3, and a cell that is run twice keeps its numbers. The file name joins the notebook id, the number and the name, for example `03a_1_metric_heat_map.png`. `fig.savefig` writes the PNG file with 150 dots per inch, without an empty margin and without the program's name, so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory. The caption is stored, and the whole dictionary of captions is written into the captions file (`json.dumps` turns it into JSON text with sorted keys). `display(Image(...))` shows the saved picture below the cell; its `metadata` tells the book's tools which file it is. The last line prints where the figure was saved.

```python
PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    """A check.  If condition is False, stop with an AssertionError that names the
    check (an if statement is used instead of assert, because python -O would skip an
    assert).  Otherwise print "PASS <name>" and, when the check reproduces a Revision
    record, a second line naming the record file and its check."""
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")
```

`PASSED` is an empty **list** (an ordered collection in square brackets). `check` is the function behind every check of the book. `condition` is either `True` or `False`; if it is false, `raise AssertionError(...)` stops the notebook with an error that names the check. Otherwise the name is appended to `PASSED` and the line PASS followed by the name is printed. `record=None` makes the third argument optional; a check that reproduces a Revision record passes the record's file and check name, and a second line names them.

```python
def report(label, value, unit=""):
    """Print a key number as a line "RESULT <label> = <value> <unit>"."""
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    """Print the last line of the notebook: how many checks passed."""
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a RESULT line; the expression in round brackets adds a blank and the unit when a unit is given and nothing otherwise. `all_checks_passed` prints the last line of the notebook; `len(PASSED)` is the number of checks that passed. The last statement prints the one output line of In [1].

**In [2], every result in one piece.** While a cell runs, Jupyter receives what it prints in pieces, about one piece every 0.2 seconds; where one piece ends depends on the speed of the computer. The book's tools read a PASS line together with the line under it that names the Revision record, and they read the two correctly only when both arrive in the same piece. This cell makes sure that they do.

```python
import contextlib  # redirect_stdout: send printed text into a buffer
import io  # StringIO: a text buffer in memory
import sys  # sys.stdout: the place where printed text goes
```

Three modules of Python: `contextlib` holds `redirect_stdout`, which sends everything that `print` writes to another place; `io` holds `StringIO`, a text buffer in memory; `sys.stdout` is the normal destination of printed text.

```python
def in_one_piece(helper):
    """A function that does what helper does, with all the lines that helper prints
    written in one piece."""
    def helper_in_one_piece(*arguments, **options):
        collected = io.StringIO()  # an empty text buffer
        with contextlib.redirect_stdout(collected):  # print() writes into it
            helper(*arguments, **options)  # a failing check stops here, as before
        sys.stdout.write(collected.getvalue())  # all the lines with one write
    return helper_in_one_piece
```

`in_one_piece` takes a function `helper` and returns a new function, `helper_in_one_piece`, defined inside it. The stars in `*arguments` and `**options` collect whatever values the new function is called with and pass all of them on to `helper` unchanged. Inside, `collected` is an empty buffer; the `with` block redirects printing into it while `helper` runs, so the PASS line and the record line land in the buffer; if the check fails, the `AssertionError` stops everything here exactly as before. After the block, `sys.stdout.write` writes the whole buffer at once, which reaches Jupyter as one piece.

```python
check = in_one_piece(check)  # a PASS line and its record line stay together
report = in_one_piece(report)  # a long RESULT line and its second line, too
say("From now on check and report print each of their results in one piece.")
```

The names `check` and `report` now stand for the wrapped functions. They print the same lines as before; only the timing of the printing changes. The last line prints the output of In [2].

**In [3], the record's text.**

```python
import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols
from sympy.parsing.sympy_parser import (implicit_multiplication, parse_expr,
                                        standard_transformations)
```

numpy (short name `np`) works with **arrays**, lists of numbers on which arithmetic acts entry by entry; sympy (short name `sp`) does exact algebra with symbols. `parse_expr` turns a text such as `"2*x + 1"` into a sympy expression; `standard_transformations` and `implicit_multiplication` are reading rules for it (explained at In [5]).

```python
def record_check(report_file, check_name, detail_part=""):
    """Return True when the Revision report report_file lists the check check_name
    as passed (and its detail contains detail_part); otherwise stop the notebook."""
    checks = json.loads(repository_file(report_file).read_text(encoding="utf-8"))
    checks = checks["checks"]  # a dictionary or a list, depending on the report
```

Several PASS lines of this notebook say that a result reproduces a named check of a Revision report. A **report** is a JSON file in which a program of the Revision record lists the checks it ran, each with its name, its verdict and a short detail text. The function `record_check` makes sure that such a check really exists and passed; without it, a PASS line could name a check that has since been renamed, removed or failed. Its three **parameters** (the names in brackets, which receive the values given in a call) are the report file, the name of the check and an optional piece of text `detail_part`; `=""` makes the empty text its default, used when a call gives only two values. The text in triple quotes under the `def` line is its docstring (In [1]). The first line of the body reads the report: `read_text` gives the file as text and `json.loads` turns the JSON text into a Python dictionary. The second keeps only its entry `"checks"`. The reports of the Revision record store their checks in one of two ways, and the function accepts both.

```python
    if isinstance(checks, dict):  # {name: {"passed": true, "detail": ...}}
        entry = checks.get(check_name, {})
        passed = entry.get("passed") is True
```

`isinstance(checks, dict)` is true when the checks form a dictionary whose keys are the check names (the Rust program writes them so). Then `checks.get(check_name, {})` is the entry of that name, or an empty dictionary `{}` if there is none, and the check counts as passed only if the entry's `"passed"` is exactly `True` (`is True` compares with the value `True` itself). For a missing entry, `entry.get("passed")` gives `None`, which is not `True`.

```python
    else:  # [{"name": ..., "verdict": "PASS", "detail": ...}, ...]
        entry = next((e for e in checks if e.get("name") == check_name), {})
        passed = entry.get("verdict") == "PASS"
```

Otherwise the checks form a list of dictionaries, each with its own `"name"` (the Python programs and the lead checks write them so). `(e for e in checks if ...)` runs through the list and keeps the entries with the wanted name; `next(..., {})` takes the first of them, or `{}` if there is none. The check counts as passed only if its `"verdict"` is the text `"PASS"`.

```python
    if not passed or detail_part not in entry.get("detail", ""):
        raise AssertionError(f"record check failed: {report_file} does not list "
                             f"{check_name} as passed")
    return True
```

If the check did not pass, or its detail text does not contain `detail_part`, `raise AssertionError(...)` stops the notebook with an error message that names the report and the check (every text contains the empty text, so without a `detail_part` only the verdict matters). Otherwise the function returns `True`. It prints nothing, so it adds no PASS line and does not change the number of checks; it only guarantees that each record line printed under a PASS line names a check that exists and passed. Notebook 03b uses the same function.

```python
CURVATURE_RECORD = "Revision/gkd_lovelock/results/curvature.json"
record = json.loads(repository_file(CURVATURE_RECORD).read_text(encoding="utf-8"))
# the metric exactly as the record stores it, then a note in brackets
author_text, note = record["metricAsGiven"].split("}} ", 1)
author_text += "}}"  # the two closing brackets that split removed
say(f"The metric as the record stores it ({len(author_text)} characters):")
for line in author_text.replace("},", "},\n").split("\n"):  # one row per line
    print(line)
say("The note of the record: " + note)
```

The first line names the record file. The second reads the file and turns it into a Python dictionary. `record["metricAsGiven"]` is the text of the metric followed by a note in brackets. `split("}} ", 1)` cuts this text once, at the first `}}` followed by a blank: `author_text` gets the matrix (without its two closing braces, which the split removed and `+= "}}"` puts back) and `note` the note. The matrix is 338 characters long, as the output shows (`len` counts the characters). The loop prints it with one row of the matrix per line: `replace("},", "},\n")` puts a line break (`\n`) after every row and `split("\n")` cuts the text at the breaks. The output is the matrix of Section 3.5, in the author's order $x_0, x_1, \dots, x_7$, with the two functions `a4[x4]` and `b4[x4]`; the last line prints the note, which says that this is the corrected metric of 2026-10-16 (version 2) for every real $z$ with $\sin z\cos z \neq 0$, and that the results of the withdrawn metric of 2026-10-14 are kept frozen in a separate folder.

**In [4], the symbols.**

```python
x0, x1, x2, x3, x4, x5, x6, x7 = sp.symbols("x0:8", real=True)  # 8 coordinates
COORDS = [x0, x1, x2, x3, x4, x5, x6, x7]
H = sp.symbols("H", positive=True)  # the constant of the author, H > 0
a4 = sp.Function("a4")(x4)  # the metric function a4: an unknown function of x4
b4 = sp.Function("b4", positive=True)(x4)  # the metric function b4 > 0 of x4
a4p, a4v = sp.symbols("a4p a4v", real=True)  # a4p = a4 prime, a4v = value of a4
b4p = sp.symbols("b4p", real=True)  # b4p = b4 prime
b4v = sp.symbols("b4v", positive=True)  # b4v = value of b4
z = sp.symbols("z", real=True)  # z = 6 H x0, any real number, for printing
```

`sp.symbols("x0:8", real=True)` makes the eight symbols `x0`, ..., `x7` (the range `0:8` means 0 to 7), declared real; `COORDS` is their list, in the author's order, so that `COORDS[k]` is $x_k$. `H` is declared positive, which lets sympy simplify, for example, $\sqrt{H^2} = H$. `sp.Function("a4")(x4)` is an unknown function of `x4`: sympy can differentiate it (giving $a_4'$) without knowing it. `b4` is the second metric function, declared positive (`positive=True`), so that sympy may write $\sqrt{b_4^4} = b_4^2$. `a4p`, `a4v`, `b4p`, `b4v` and `z` are plain symbols used only for printing; `z` is declared real but not positive, because $z$ takes every real value.

```python
def plain(expression):
    """Write the derivatives of a4 and b4 as a4p and b4p, their values as a4v and
    b4v, and 6 H x0 as z."""
    expression = expression.subs(sp.Derivative(a4, x4), a4p).subs(a4, a4v)
    expression = expression.subs(sp.Derivative(b4, x4), b4p).subs(b4, b4v)
    return expression.subs(x0, z / (6 * H))  # then 6*H*x0 becomes z


say("Symbols: x0 ... x7, H > 0, the functions a4(x4) and b4(x4), and a4p, a4v, b4p, "
    "b4v, z for printing.")
```

`plain` rewrites an expression for printing: `.subs(old, new)` replaces `old` by `new`, first the derivative $a_4'$ by `a4p`, then the function value by `a4v`, the same for $b_4$ (`b4p`, `b4v`); then $x_0$ by $z/(6H)$, so that $6Hx_0$ becomes $z$. The derivative is replaced before the value: otherwise the value inside the derivative would be replaced first and the derivative would no longer be recognised. The last line prints the output of In [4].

**In [5], the text becomes a matrix.**

```python
text = author_text
text = text.replace("exp^", "E^")  # e to the power ...
text = text.replace("Sin[6 H x0]", "sin(6 H x0)")  # Mathematica [ ] -> Python ( )
text = text.replace("Cot[6 H x0]", "cot(6 H x0)")
text = text.replace("a4[x4]", "a4")  # the value of the function a4 at x4
text = text.replace("b4[x4]", "b4")  # the value of the function b4 at x4
text = text.replace("{", "[").replace("}", "]")  # Mathematica lists -> Python lists
text = text.replace("^", "**")  # Mathematica power ^ -> Python power **
```

Eight replacements translate Mathematica into Python, one rule each: `exp^` becomes `E^` (sympy's `E` is the number $e = 2.718\ldots$; the record's text already writes `E^`, and the rule is kept so that a text written with `exp^` is read the same way); the square brackets of the sine and the cotangent become round brackets; `a4[x4]` becomes `a4` and `b4[x4]` becomes `b4`; the braces of lists become square brackets (a Python list); the power sign `^` becomes `**`. The order matters: the square brackets of the functions are translated before any other bracket. The positive root `(Sin[6 H x0]^2)^(1/6)` needs no rule of its own: after the replacements it reads `(sin(6 H x0)**2)**(1/6)`.

```python
names = {"E": sp.E, "a4": a4, "b4": b4, "H": H, "x0": x0, "sin": sp.sin,
         "cot": sp.cot, "sign": sp.sign}
rows = parse_expr(text, local_dict=names,
                  transformations=standard_transformations + (implicit_multiplication,))
g = sp.Matrix(rows)  # the corrected metric as an exact 8 x 8 sympy matrix
```

The dictionary `names` tells `parse_expr` what each name in the text means: `a4` and `b4` are the functions $a_4(x_4)$ and $b_4(x_4)$, `H` and `x0` the symbols, `sin`, `cot` and `sign` sympy's sine, cotangent and sign function (the sign is not in the metric text; it is needed for a record entry in In [6]). `implicit_multiplication` reads a blank between two factors as a product, as Mathematica does (`6 H x0` is $6 \cdot H \cdot x_0$). The result `rows` is a list of eight lists, and `sp.Matrix(rows)` makes the exact $8 \times 8$ matrix `g`. Because $x_0$ is declared real, sympy writes the positive sixth root $(\sin^2 z)^{1/6}$ at once as `Abs(sin(6*H*x0))**(1/3)`, that is $|\sin z|^{1/3}$: the positive branch, for every real $z$.

```python
say(f"The matrix has {g.rows} rows and {g.cols} columns. Its diagonal entries:")
for k in range(8):
    say(f"  g[x{k}, x{k}] = {g[k, k]}")
off_diagonal = [g[i, j] for i in range(8) for j in range(8) if i != j]
check(all(entry == 0 for entry in off_diagonal),
      "the 56 entries off the diagonal are zero: the metric is diagonal")
```

The loop prints the eight diagonal entries; `range(8)` runs over $k = 0, \dots, 7$ and `g[k, k]` is the entry in row $k$ and column $k$, printed with the author's name `x{k}` (row $k$ belongs to $x_k$). `off_diagonal` is a **list comprehension**, a list built by a loop inside square brackets: the $64 - 8 = 56$ entries with $i \ne j$. `all(...)` is true when every one of them is zero: the first PASS line. The output shows the diagonal of Section 3.5, written by sympy: `b4(x4)*exp(-2*a4(x4))*cot(6*H*x0)**2` is $e^{-2a_4}b_4\cot^2(6Hx_0)$, `exp(2*a4(x4))` is $e^{2a_4}$, and `-b4(x4)*exp(-2*a4(x4))*Abs(sin(6*H*x0))**(1/3)` is $-e^{-2a_4}b_4|\sin z|^{1/3}$.

**In [6], two independent checks of the reading.**

```python
f_hidden = sp.exp(-a4) * sp.sqrt(b4)  # f = e^(-a4) b4^(1/2), the hidden scale
warp_sq = (sp.sin(6 * H * x0) ** 2) ** sp.Rational(1, 6)  # (sin^2 z)^(1/6) > 0
typed = sp.diag(f_hidden ** 2 * sp.cot(6 * H * x0) ** 2,  # the order x0, x1, ..., x7
                sp.exp(2 * a4), sp.exp(2 * a4), sp.exp(2 * a4),
                -1,
                -f_hidden ** 2 * warp_sq, -f_hidden ** 2 * warp_sq,
                -f_hidden ** 2 * warp_sq)
difference = (g - typed).applyfunc(sp.simplify)  # simplify every entry
check(difference == sp.zeros(8, 8),
      "the text of the record equals the metric typed by hand from the formula")
```

`f_hidden` is the hidden scale $f = e^{-a_4}b_4^{1/2}$ of Section 3.5 (`sp.sqrt` is the square root). `sp.Rational(1, 6)` is the exact fraction $1/6$ (the Python number `1/6` would be rounded), so `warp_sq` is $(\sin^2 z)^{1/6}$, the square $W^2$ of the warp factor. `sp.diag(...)` builds the diagonal matrix of the formula of Section 3.5, typed by hand in the author's order: first the hidden entry $f^2\cot^2 z$, then the three 3-space entries $e^{2a_4}$, the time entry $-1$ and the three extra-time entries $-f^2W^2$. `applyfunc(sp.simplify)` simplifies every entry of the difference, and the check requires the $8 \times 8$ zero matrix `sp.zeros(8, 8)`: the reading of the text agrees with the formula.

```python
def from_mathematica(entry_text):
    """A record entry in Mathematica notation, as a sympy expression."""
    t = entry_text.replace("Sin[6*H*x0]", "sin(6*H*x0)")
    t = t.replace("Cot[6*H*x0]", "cot(6*H*x0)")
    t = t.replace("Sign[cot(6*H*x0)]", "sign(cot(6*H*x0))")  # the sign of cot z
    t = t.replace("a4[x4]", "a4").replace("b4[x4]", "b4").replace("^", "**")
    if "[" in t or "]" in t:  # a piece of notation that was not translated
        raise ValueError(f"cannot translate {entry_text}")
    return parse_expr(t, local_dict=names)
```

The record also stores the diagonal entries one by one (`metricDiagonal`), in Mathematica notation with explicit `*` signs, for example `E^(-2*a4[x4])*Cot[6*H*x0]^2*b4[x4]` and `-E^(-2*a4[x4])*(Sin[6*H*x0]^2)^(1/6)*b4[x4]`. `from_mathematica` translates such an entry with the same rules, and one more: `Sign[...]` of the cotangent (its sign, $+1$ or $-1$), which appears in the record's volume factor (In [7]), becomes sympy's `sign(...)`. The order of the rules matters here too: the cotangent is translated first, so that the third rule finds `Sign[cot(6*H*x0)]`. If a square bracket is left, some notation was not translated, and the function stops with a `ValueError` instead of misreading it silently.

```python
agree = [sp.simplify(g[k, k] - from_mathematica(entry)) == 0
         for k, entry in enumerate(record["metricDiagonal"])]
check(len(agree) == 8 and all(agree),
      "the 8 diagonal entries equal those of the Rust program lovelock_gkd",
      record=f"{CURVATURE_RECORD}, metricDiagonal")
```

`enumerate` hands out each record entry with its position $k$. For each, the difference between our entry and the translated record entry is simplified and compared with $0$. The check requires eight agreements and prints the PASS line with the record line under it.

**In [7], the determinant and the volume factor** (Section 3.6).

```python
det_g = g.det()  # the product of the diagonal entries
say(f"det g = {plain(det_g)}")
record_check("Revision/gkd_lovelock/results/python-lovelock-report.json",
             "sqrt_abs_det_g",
             "det g = e^(-2 a4) b4^4 cot^2(6 H x0) |sin(6 H x0)| exactly")  # or stop
check(sp.simplify(det_g - sp.exp(-2 * a4) * b4 ** 4 * sp.cot(6 * H * x0) ** 2
                  * sp.Abs(sp.sin(6 * H * x0))) == 0,
      "det g = e^(-2 a4) b4^4 cot(z)^2 |sin z|",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
             "check sqrt_abs_det_g")
```

`g.det()` is the determinant. It prints as `b4v**4*exp(-2*a4v)*cot(z)**2*Abs(sin(z))`, the last line of the derivation of Section 3.6 (sympy has already multiplied the eight entries and cancelled $e^{6a_4}e^{-6a_4}$ and the two minus signs). `record_check` then confirms that the independent verification of the record lists its check `sqrt_abs_det_g` as passed and that the detail of that check contains the text `det g = e^(-2 a4) b4^4 cot^2(6 H x0) |sin(6 H x0)| exactly`; otherwise the notebook stops here. The check confirms that our determinant equals $e^{-2a_4}b_4^4\cot^2 z\,|\sin z|$ (`sp.Abs` is the absolute value). The two strings of the `record=` argument are written next to each other, which Python joins into one string.

```python
# sqrt|det g| for every real z: |cot z| written as cot z times its sign
abs_cot = sp.cot(6 * H * x0) * sp.sign(sp.cot(6 * H * x0))
volume_factor = (sp.exp(-a4) * b4 ** 2 * abs_cot
                 * (sp.sin(6 * H * x0) ** 2) ** sp.Rational(1, 4))
check(sp.simplify(from_mathematica(record["sqrtAbsDetG"]) - volume_factor) == 0,
      "sqrt|det g| = e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4), as the record writes it",
      record=f"{CURVATURE_RECORD}, sqrtAbsDetG")
```

`abs_cot` is $|\cot z|$, written as the cotangent times its sign, exactly as the record writes it (`Cot[6*H*x0]*Sign[Cot[6*H*x0]]`): for a positive cotangent the sign is $+1$, for a negative one $-1$, and the product is the size. `volume_factor` is the formula $e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$ of Section 3.6. The record's entry `sqrtAbsDetG` is translated by `from_mathematica` (this is where its rule for `Sign` is needed), and the difference must simplify to $0$.

```python
WARPED_RECORD = "Revision/metric_warped/results/warped-metric.json"
warped = json.loads(repository_file(WARPED_RECORD).read_text(encoding="utf-8"))
say("record of the corrected metric, sqrt_det_g_corrected: "
    + warped["sqrt_det_g_corrected"])
```

The record of the corrected metric (folder `Revision/metric_warped`) states the volume factor once more, as a text in its key `sqrt_det_g_corrected`; the cell reads that record into the dictionary `warped` and prints the text: `E^(-a4) b4^2 |Cot[6 H x0]| (Sin[6 H x0]^2)^(1/4)` (the output breaks the long line).

```python
# numbers: sqrt(|det g|) at 8 points, two in each quarter, a4 = 0.3, b4 = 2
z_points = np.array([0.3, 1.2, 1.9, 2.8, 3.5, 4.4, 5.1, 6.0])
det_numbers = np.array([float(det_g.subs({a4: 0.3, b4: 2}).subs({H: 1, x0: zp / 6}))
                        for zp in z_points])
formula = (np.exp(-0.3) * 4.0 * np.abs(1 / np.tan(z_points))
           * np.abs(np.sin(z_points)) ** 0.5)
check(np.max(np.abs(np.sqrt(np.abs(det_numbers)) - formula)) < 1e-13
      and warped["sqrt_det_g_corrected"].startswith("E^(-a4) b4^2 |Cot[6 H x0]|"),
      "sqrt|det g| equals the formula at 8 points in all four quarters",
      record=f"{WARPED_RECORD}, sqrt_det_g_corrected")
```

A numerical check of the same fact, at $a_4 = 0.3$ and $b_4 = 2$ (any values would do), at eight values of $z$, two in each quarter of the period $0 < z < 2\pi$ (in each quarter $\sin z$ and $\cos z$ have a different pair of signs, so all sign cases are tested). For each, the exact determinant is evaluated (a dictionary in `subs` replaces several symbols at once; $H = 1$ and $x_0 = z/6$) and turned into a floating-point number with `float`. `formula` is $e^{-0.3}\cdot 2^2\cdot|\cot z|\cdot|\sin z|^{1/2}$ at the same points (`1 / np.tan` is the cotangent). The check requires $\sqrt{|\det g|}$ to differ from it by less than $10^{-13}$ at all eight points, and the record's text to start as expected.

**In [8], the signature and the two symmetries** (Section 3.5).

```python
ETA = np.array([1, 1, 1, 1, -1, -1, -1, -1])  # the flat metric diag(+,+,+,+,-,-,-,-)
B4_POINT = float(np.exp(2.0 / 3.0))  # b4 on the history at a4 = 0.5, b4(0) = 1
# the entries as functions of z, a4v and b4v
diagonal_z = [plain(g[k, k]) for k in range(8)]
functions = [sp.lambdify((z, a4v, b4v), entry, "numpy") for entry in diagonal_z]
```

`ETA` holds the eight signs of $\eta$, in the author's order: $+$ for $x_0, x_1, x_2, x_3$ and $-$ for $x_4, \dots, x_7$. `B4_POINT` is $e^{2/3} = 1.947734$, the value of $b_4$ on the history of Section 3.8 at $a_4 = 0.5$ ($b_4 = e^{4a_4/3}$ with $b_4(0) = 1$); `float(...)` turns the numpy number into an ordinary Python number. `diagonal_z` holds the eight entries written with `z`, `a4v` and `b4v`. `sp.lambdify((z, a4v, b4v), entry, "numpy")` turns an exact expression into a fast numerical Python function of the three arguments that works on whole numpy arrays.

```python
def diagonal_values(z_values, a4_value, b4_value=B4_POINT):
    """The 8 diagonal entries at the points z_values (one row per entry)."""
    return np.array([np.broadcast_to(f(z_values, a4_value, b4_value), z_values.shape)
                     for f in functions], dtype=float)
```

`diagonal_values` evaluates the eight functions at an array of values of $z$ for one value of $a_4$ and one of $b_4$ (`b4_value=B4_POINT` is a **default value**: a call that leaves out the third argument gets $b_4 = e^{2/3}$, the value at the slice $a_4 = 0.5$ that the pictures use) and returns a table with eight rows, row $k$ for $g_{kk}$. The entry $-1$ does not depend on $z$, so its function returns one number, and the 3-space entries do not depend on $z$ either; `np.broadcast_to` repeats such a number so that every row has the same length as `z_values`.

```python
z_grid = -np.pi + (np.arange(800) + 0.5) * (2 * np.pi / 800)  # 800 midpoints
patterns = set()
for b4_value in (0.5, 2.0, 4.0):
    for a4_value in np.linspace(-3.0, 3.0, 13):
        # +1 or -1 for each entry
        signs = np.sign(diagonal_values(z_grid, a4_value, b4_value))
        patterns.update(tuple(int(s) for s in column) for column in signs.T)
say(f"sign patterns found on the grid: {sorted(patterns)}")
check(patterns == {tuple(int(s) for s in ETA)},
      "on the whole grid -pi < z < pi the signs are (+,+,+,+,-,-,-,-): signature (4,4)")
```

The interval $-\pi < z < \pi$ (two cells) is cut into 800 equal steps of length $2\pi/800$; `np.arange(800)` is $0, 1, \dots, 799$, and adding $0.5$ before multiplying by the step puts each point in the middle of its step. No midpoint is a degenerate point (those are the multiples of $\pi/2$, which are step boundaries). A `set` is a collection without repetitions. For three values of $b_4$ ($0.5$, $2$, $4$) and 13 values of $a_4$ from $-3$ to $3$, `np.sign` replaces each entry by its sign; `signs.T` is the table turned on its side, so that each `column` holds the eight signs at one point; `tuple(...)` turns them into a fixed sequence that a set can store. At the end the set holds every sign pattern met anywhere on the grid. It is printed (sorted) and must be the single pattern of $\eta$. (The grid includes negative values of $a_4$ only to test the sign argument of Section 3.5, which holds for every real $a_4$ and every $b_4 > 0$.)

```python
step_x1 = diagonal_values(np.array([0.7]), 0.5)[1, 0]  # g11: step along x1
step_x5 = diagonal_values(np.array([0.7]), 0.5)[5, 0]  # g55: step along x5
say(f"at z = 0.7, a4 = 0.5, b4 = e^(2/3): g11 = {step_x1:.6f} (space-like), "
    f"g55 = {step_x5:.6f} (time-like)")
check(step_x1 > 0 > step_x5, "a step along x1 is space-like, along x5 time-like")
```

At the single point $z = 0.7$, $a_4 = 0.5$, $b_4 = e^{2/3}$ (the default): row 1 is $g_{11}$ and row 5 is $g_{55}$; the second index `0` picks the only column. The format `:.6f` prints six digits after the decimal point: $g_{11} = e^{1} = 2.718282$ and $g_{55} = -e^{-1/3}|\sin 0.7|^{1/3} = -0.618841$ (the output breaks the long line after "time-"). A unit step along $x_1$ has the squared length $g_{11} > 0$ (space-like), along $x_5$ the squared length $g_{55} < 0$ (time-like). Python reads `step_x1 > 0 > step_x5` as both comparisons at once.

```python
shift = {x0: x0 + sp.pi / (6 * H)}  # z -> z + pi
mirror = {x0: sp.pi / (6 * H) - x0}  # z -> pi - z, the reflection across the fold
check(all(sp.simplify(g[k, k].subs(shift) - g[k, k]) == 0
          and sp.simplify(g[k, k].subs(mirror) - g[k, k]) == 0 for k in range(8)),
      "every entry repeats with the period pi and is symmetric under z -> pi - z")
```

The two symmetries of Section 3.5, exactly. Replacing $x_0$ by $x_0 + \pi/(6H)$ replaces $z = 6Hx_0$ by $z + \pi$; replacing $x_0$ by $\pi/(6H) - x_0$ replaces $z$ by $\pi - z$, the reflection across the fold $z = \pi/2$. For each of the eight entries the difference between the shifted (or reflected) entry and the entry itself must simplify to $0$. Together with the signature this shows that every half cell carries the same geometry.

**In [9], the colours and the heat map of the metric.**

```python
from matplotlib.colors import LinearSegmentedColormap

BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
MAGENTA, GREEN, VIOLET, RED = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
GREY = "#f0efec"  # the neutral middle of the two-sided colour scale
DIVERGING = LinearSegmentedColormap.from_list("blue_grey_red", [BLUE, GREY, RED])
LABELS = [f"$x_{k}$" for k in range(8)]
```

Each colour is written as a **hex code**: `#` and three pairs of hexadecimal digits for the amounts of red, green and blue. The palette is chosen so that readers with a colour-vision deficiency can tell the colours apart; every figure also uses line styles and labels, so that it can be read in black and white. `DIVERGING` is a colour scale that runs from blue through grey to red; it will show negative numbers blue, zero grey and positive numbers red. `LABELS` holds the eight axis labels `$x_0$` to `$x_7$`, written in the math notation that matplotlib understands.

```python
z_point, a4_point = np.pi / 4, 0.5
values = np.zeros((8, 8))
values[np.diag_indices(8)] = diagonal_values(np.array([z_point]), a4_point)[:, 0]
fig, ax = plt.subplots(figsize=(6.4, 5.4))
image = ax.imshow(values, cmap=DIVERGING, vmin=-3.0, vmax=3.0)
```

At the point $z = \pi/4$, $a_4 = 0.5$ the table `values` starts as an $8 \times 8$ table of zeros, and its diagonal (`np.diag_indices(8)`) is filled with the eight entries of the metric. `plt.subplots` makes a figure `fig` with one drawing area `ax`; `ax.imshow` draws the table as coloured squares, with the colour scale running from $-3$ (blue) to $3$ (red).

```python
for i in range(8):
    for j in range(8):
        ax.text(j, i, f"{values[i, j]:.3f}" if i == j else "0", ha="center",
                va="center", fontsize=8)
ax.set_xticks(range(8), LABELS)
ax.set_yticks(range(8), LABELS)
ax.grid(False)  # no grid lines across the squares
ax.set_title("The metric $g_{\\mu\\nu}$ at $z = \\pi/4$, $a_4 = 0.5$, $b_4 = e^{2/3}$")
fig.colorbar(image, ax=ax, label="value of the entry (no unit)")
```

The double loop writes the value into each square: three decimals on the diagonal, a plain `0` elsewhere (`ha` and `va` centre the text). The two tick lines label the rows and the columns $x_0$ to $x_7$. In a Python string `\\` stands for one backslash, so the title reads $g_{\mu\nu}$ in math notation. `fig.colorbar` adds the colour scale with its label.

```python
save_figure(fig, "metric_heat_map",
            "The corrected metric $g_{\\mu\\nu}$ at the point $z = 6Hx_0 = \\pi/4$ "
            "with $a_4 = 0.5$ and $b_4 = e^{2/3}$ (the deflating history at "
            "$a_4 = 0.5$, $b_4(0) = 1$), drawn as a heat map: row $\\mu$ and "
            "column $\\nu$ run "
...
check(abs(values[0, 0] - np.exp(-1.0 / 3.0)) < 1e-12
      and abs(values[1, 1] - np.e) < 1e-12
      and abs(values[5, 5] + np.exp(-1.0 / 3.0) * 0.5 ** (1 / 6)) < 1e-12,
      "at z = pi/4, a4 = 0.5, b4 = e^(2/3): g00 = e^(-1/3), g11 = e and "
      "g55 = -e^(-1/3) (1/2)^(1/6)")
```

`save_figure` saves and shows the figure with its caption (printed in full under Figure 03a.1). The check compares three entries with their exact values. The entry `values[0, 0]` is $g_{00} = e^{-1}e^{2/3}\cot^2(\pi/4) = e^{-1/3}$, because $\cot(\pi/4) = 1$. The entry `values[1, 1]` is $g_{11} = e^{2\cdot 0.5} = e$. The entry `values[5, 5]` is $g_{55} = -e^{-1/3}(\sin^2(\pi/4))^{1/6}$, that is $-e^{-1/3}(1/2)^{1/6}$, because $\sin^2(\pi/4) = 1/2$; the check adds the expected value to the entry, so the sum must be $0$.

**What Figure 03a.1 shows.** An $8 \times 8$ table of coloured squares in which only the diagonal is coloured. In the author's order, the top-left square is the hidden one, $e^{-1/3} = 0.717$; then come the three red squares of 3-space with $e = 2.718$, the time square $-1$, and the three pale blue squares of the extra times with $-0.638$. Four positive and four negative entries: the signature (4,4) at a glance. The hidden entry and the size of an extra-time entry share the factor $f^2 = e^{-1/3}$; they differ only by $\cot^2(\pi/4) = 1$ against $(\sin^2(\pi/4))^{1/6} = 0.891$. The 3-space entries are larger than the extra-time entries by the factor $e^{2a_4}/(f^2W^2) = e/0.638 = 4.26$, because $a_4 = 0.5 > 0$ has already inflated 3-space and deflated the block.

**In [10], the diagonal entries across two cells.**

```python
cells = [np.linspace(-np.pi + 0.02, -0.02, 600), np.linspace(0.02, np.pi - 0.02, 600)]
fig, ax = plt.subplots()
for n, z_cell in enumerate(cells):  # one cell after the other: no line across a tip
    entries = diagonal_values(z_cell, 0.5)  # b4 = e^(2/3), the history at a4 = 0.5
    first = n == 0  # only the first cell gets the labels of the legend
```

The list `cells` holds two arrays of 600 values of $z$ each, one for the cell $-\pi < z < 0$ and one for the cell $0 < z < \pi$, each stopping $0.02$ short of the tips. Drawing each cell separately prevents a line from being drawn straight across the tip $z = 0$, where the hidden entry grows without bound. In the loop, `enumerate` hands out each cell with its number `n` (0, then 1); `entries` holds the eight entries at $a_4 = 0.5$ and $b_4 = e^{2/3}$ (the default of `diagonal_values`); `first` is true only for the first cell (`n == 0` compares and gives `True` or `False`).

```python
    ax.plot(z_cell, entries[0], color=AQUA, lw=1.8,
            label="$g_{00} = e^{-2a_4}b_4\\cot^2 z$" if first else None)
    ax.plot(z_cell, entries[1], color=RED, lw=1.8,
            label="$g_{11} = g_{22} = g_{33} = e^{2a_4}$" if first else None)
    ax.plot(z_cell, entries[4], color=VIOLET, lw=1.8, ls="-.",
            label="$g_{44} = -1$" if first else None)
    ax.plot(z_cell, entries[5], color=BLUE, lw=1.8, ls="--",
            label="$g_{55} = g_{66} = g_{77} = -e^{-2a_4}b_4(\\sin^2 z)^{1/6}$"
            if first else None)
    ax.plot(z_cell, np.cos(z_cell) ** 2 / np.abs(np.sin(z_cell)), color="black",
            lw=1.2, ls=":",
            label="$\\det g/(e^{-2a_4}b_4^4) = \\cos^2 z/|\\sin z|$" if first else None)
```

`ax.plot(x, y, ...)` draws a curve; `lw` is the line width, `ls` the line style (a dash and a dot mean dash-dotted, two dashes mean dashed, a colon means dotted) and `label` its text in the legend. The expression `"..." if first else None` gives the label for the first cell and `None` (no label) for the second, so that each curve appears in the legend once. Equal entries are drawn once: row 0 for the hidden direction, row 1 for 3-space, row 4 for the time, row 5 for the extra times. The black dotted curve is $\cos^2 z/|\sin z| = \cot^2 z\,|\sin z|$, the determinant divided by its factor $e^{-2a_4}b_4^4$ (Section 3.6).

```python
ax.axhline(0.0, color="black", lw=0.8)
for fold in (-np.pi / 2, np.pi / 2):
    ax.axvline(fold, color="grey", lw=0.8, ls=":")
    ax.text(fold + 0.05, 3.3, "fold", fontsize=9)
ax.set_ylim(-3.4, 3.6)  # room below the curves for the legend
ax.set_xlabel("$z = 6 H x_0$ (radians)")
ax.set_ylabel("entry of the metric (no unit)")
ax.set_title("The diagonal entries across two cells ($a_4 = 0.5$, $b_4 = e^{2/3}$)")
ax.legend(fontsize=7, loc="lower center", ncol=2)
```

`axhline` draws the horizontal line at height $0$; for each of the two folds $z = -\pi/2$ and $z = \pi/2$, `axvline` draws a dotted grey vertical line and `ax.text` writes the word "fold" next to it at the height $3.3$. `set_ylim` fixes the vertical range from $-3.4$ to $3.6$, which cuts off the hidden entry where it grows large near the tips and leaves room for the legend. The labels, the title and the legend (in two columns, `ncol=2`, at the bottom centre) follow.

```python
save_figure(fig, "diagonal_entries",
            "The diagonal entries of the corrected metric as functions of "
            "$z = 6Hx_0$ from $-\\pi$ to $\\pi$ (two cells, each made of two halves "
            "joined at a fold), for $a_4 = 0.5$ and $b_4 = e^{2/3}$ (the deflating "
...
values_all = np.concatenate([diagonal_values(c, 0.5) for c in cells], axis=1)
check(np.all(values_all[0] > 0) and np.all(values_all[1] == np.e)
      and np.cos(np.pi / 2) ** 2 < 1e-30,
      "g00 > 0 away from the folds, g11 = e at every z, det g = 0 at the fold")
```

`np.concatenate(..., axis=1)` joins the tables of the two cells side by side into one table of eight rows and 1200 columns. The check requires the hidden entry to be positive at every plotted point, every 3-space entry to equal $e$ exactly at $a_4 = 0.5$, and $\cos^2(\pi/2)$, the factor that makes the determinant vanish at the fold, to be smaller than $10^{-30}$ (the computer's $\cos(\pi/2)$ is not exactly $0$, because $\pi/2$ is rounded, but it is about $6 \times 10^{-17}$).

**What Figure 03a.2 shows.** Across two cells, $-\pi < z < \pi$: the red line of the three 3-space entries is flat at $e = 2.718$ (3-space has no warp); the dash-dotted time entry is flat at $-1$; the dashed extra-time entries stay negative, reach their largest size $f^2 = e^{-1/3} = 0.717$ at the folds and shrink towards $0$ at the tips; the aqua hidden entry is positive, grows without bound towards the tips and touches $0$ at the folds (dotted grey lines), where the black dotted determinant curve touches $0$ as well. Each cell is symmetric about its fold, and the second cell repeats the first.

**In [11], the vielbein** (Section 3.7).

```python
twelfth = (sp.sin(6 * H * x0) ** 2) ** sp.Rational(1, 12)  # (sin^2 z)^(1/12) > 0
# the author's order x0, x1, ..., x7
h = [f_hidden * sp.cot(6 * H * x0)] + [sp.exp(a4)] * 3 + [sp.Integer(1)] \
    + [f_hidden * twelfth] * 3
for k in range(8):
    say(f"  h[x{k}] = {plain(h[k])}")
```

`twelfth` is the warp factor $W = (\sin^2 z)^{1/12}$ of the extra times. The list `h` holds the eight scale factors in the author's order: the hidden one $f\cot z$, with the sign of $\cot z$ kept as in the record; three times $e^{a_4}$ for 3-space (`[...] * 3` repeats a list); the time's $1$ (`sp.Integer(1)`, an exact sympy one); and three times $fW$ for the extra times. A backslash at the end of a line continues the statement on the next line, and `+` joins lists. The loop prints them; sympy writes $W$ as `Abs(sin(z))**(1/6)`.

```python
say("record of the corrected metric, vielbein_corrected: "
    + warped["vielbein_corrected"])
LEAD_EMT = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
record_check(LEAD_EMT, "vielbein_reproduces_metric")  # stops if not passed
check(all(sp.simplify(int(ETA[k]) * h[k] ** 2 - g[k, k]) == 0 for k in range(8))
      and warped["vielbein_corrected"].startswith(
          "f0 = E^(-a4) b4^(1/2) Cot[6 H x0] (signed"),
      "eta times h squared reproduces every diagonal entry of the metric",
      record=f"{LEAD_EMT}, check vielbein_reproduces_metric")
```

The cell prints the record's own statement of the vielbein (key `vielbein_corrected` of the record of the corrected metric, read in In [7]), confirms with `record_check` that the lead's check `vielbein_reproduces_metric` passed, and checks $\eta_{kk}h_k^2 = g_{kk}$ for all eight directions (`int(ETA[k])` turns the numpy sign into an ordinary integer, which sympy multiplies exactly). The record's text must begin with the signed hidden entry, as printed.

**In [12], the expansion rates** (Section 3.7).

```python
rates = [sp.simplify(sp.diff(sp.log(h[k] ** 2) / 2, x4)) for k in range(8)]
for k in range(8):
    say(f"  expansion rate of x{k}: {plain(rates[k])}")
```

The rate of a direction is $\partial_4\ln h_k$. The cell differentiates $\frac12\ln h_k^2$ instead, which is the same number ($\ln h^2 = 2\ln|h|$) but needs no absolute value for the signed hidden factor. `sp.diff(..., x4)` differentiates with respect to $x_4$. The output: $-a_4' + b_4'/(2b_4)$ for $x_0$, $a_4'$ for $x_1, x_2, x_3$, $0$ for $x_4$, and for $x_5, x_6, x_7$ the same rate as for $x_0$, which sympy happens to print as `(-a4p*b4v + b4p/2)/b4v`.

```python
a4_prime, b4_prime = sp.Derivative(a4, x4), sp.Derivative(b4, x4)
shrink = -a4_prime + b4_prime / (2 * b4)  # the common rate of x0, x5, x6, x7
expected = [shrink] + [a4_prime] * 3 + [0] + [shrink] * 3  # the order x0, ..., x7
check([sp.simplify(r - e) == 0 for r, e in zip(rates, expected)] == [True] * 8,
      "3-space expands with rate a4p; x0 and the extra times change with rate "
      "-a4p + b4p/(2 b4)")
```

`shrink` is $\alpha_t = -a_4' + b_4'/(2b_4)$, the common rate of the hidden direction and the extra times; `expected` lists the eight rates of Section 3.7. `zip` pairs each computed rate with its expected value, and the list of the eight comparisons must be `[True] * 8`, eight times `True`.

```python
check(all(sp.diff(sp.simplify(h[k] / f_hidden), x4) == 0 for k in (0, 5, 6, 7))
      and all(not h[k].has(x0) for k in (1, 2, 3)),
      "x0 and the extra times share the factor f; 3-space has no z dependence")
```

Two structural facts: divided by $f$, the four scale factors of $x_0$ and the extra times no longer depend on $x_4$ (they are $f$ times a function of $z$ alone); and the three 3-space scale factors do not contain $x_0$ at all (`.has(x0)` is true when the symbol occurs): 3-space has no warp.

**In [13], the history of the Revision Kohn-Sham work** (Section 3.8).

```python
PARAMETERS = "Revision/kohn_sham/results/parameters.json"
parameters = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))
physics = parameters["physics"]
H_value, A_value = physics["H"], physics["historyA"]
beta = physics["historyBeta"]  # b4 = b4(0) e^(beta A H x4)
b4_start = physics["historyB4AtZero"]  # b4(0)
slices = physics["slicesA4"]  # the values of a4 at which the solver works
L_tip = physics["L_tipCutoff"]  # the tip cut-off, in units of 1/H
```

The cell reads the parameter file of the Revision Kohn-Sham solver and takes from its section `physics` the constant $H$, the slope $A$, the exponent $\beta$, the starting value $b_4(0)$, the five slices of $a_4$ and the tip cut-off $L$ (used in In [20]). A line `x, y = p, q` gives two names their values at once.

```python
say(f"H = {H_value}, A = {A_value}, beta = {beta:.6f}, b4(0) = {b4_start}, "
    f"slices a4 = {slices}, tip cut-off L = {L_tip}")
say("record, hiddenScaleRule: " + physics["hiddenScaleRule"])
check(H_value == 1.0 and A_value == 1.0 and abs(beta - 4.0 / 3.0) < 1e-15
      and b4_start == 1.0 and slices == [0.0, 0.5, 1.0, 1.5, 2.0],
      "the history of the record is a4 = x4, b4 = e^(4 x4/3) (A = 1, H = 1, "
      "beta = 4/3, b4(0) = 1) with slices 0 to 2")
```

The first line prints the values: $H = 1$, $A = 1$, $\beta = 1.333333$ (the record stores $4/3$ as a decimal number), $b_4(0) = 1$, the slices $0, 0.5, 1, 1.5, 2$ and $L = 3$. The second prints the record's rule for the hidden scale, $f(a_4) = e^{(\beta/2 - 1)a_4}$. The check confirms these values ($\beta$ to within $10^{-15}$, because $4/3$ is not exactly representable).

```python
KS_THEORY = "Revision/kohn_sham/ks-theory.json"
ks_theory = json.loads(repository_file(KS_THEORY).read_text(encoding="utf-8"))
status = ks_theory["adiabaticity"]["historyStatus"]  # the record's own statement
sentences = status.split(". ")  # the statement, cut into its sentences
say("status of the history (record): " + sentences[0] + ".")
say(sentences[-1])  # the last sentence already ends with a full stop
check(status.startswith("PRESCRIBED BACKGROUND") and "not solved for" in status,
      "the record states that the history is a prescribed background",
      record=f"{KS_THEORY}, adiabaticity.historyStatus")
```

The theory record of the Kohn-Sham work states the status of the history in its key `adiabaticity.historyStatus`. `split(". ")` cuts the statement at every full stop followed by a blank; the cell prints the first sentence ("PRESCRIBED BACKGROUND: the history a4 = H x4, b4 = e^{(4/3) H x4} is prescribed, not solved for.", with the full stop that the split removed put back) and the last ("The Kohn-Sham gas is therefore a test field on a prescribed background without back-reaction, ..."). The sentences in between, quoted in Section 3.8, give the reason. The check requires the statement to begin with PRESCRIBED BACKGROUND and to contain "not solved for".

**In [14], the scale factors along the history.**

```python
x4_line = np.linspace(0.0, 2.5, 251)
a4_line = A_value * H_value * x4_line  # the history a4 = A H x4
slice_x4 = np.array(slices) / (A_value * H_value)  # the times of the slices
rate_t = 1.0 - beta / 2.0  # f = e^(-a4) b4^(1/2) scales like e^(-(1 - beta/2) a4)
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
```

251 times from $0$ to $2.5$ and the values of $a_4 = AHx_4$ there; the times of the five slices ($x_4 = a_4/(AH)$); and `rate_t` $= 1 - \beta/2 = 1/3$, so that $f = e^{-\mathrm{rate\_t}\cdot a_4}$ (Section 3.8). The figure has two drawing areas side by side, `axes[0]` and `axes[1]`.

```python
for ax, scale in zip(axes, ["linear", "log"]):
    ax.plot(x4_line, np.exp(a4_line), color=RED, lw=1.8,
            label="3-space: $e^{a_4}$ (inflates)")
    ax.plot(x4_line, np.exp(-rate_t * a4_line), color=BLUE, lw=1.8, ls="--",
            label="$x_0$ and extra times: $f = e^{-a_4}b_4^{1/2} = e^{-a_4/3}$")
    ax.plot(x4_line, np.exp(a4_line) * np.exp(-rate_t * a4_line), color="black",
            lw=1.2, ls=":", label="product $= e^{2a_4/3}$")
    ax.plot(slice_x4, np.exp(slices), "o", color=RED, ms=6)
    ax.plot(slice_x4, np.exp(-rate_t * np.array(slices)), "s", color=BLUE, ms=6)
    ax.set_yscale(scale)
    ax.set_xlabel("time $x_4$ (unit $1/H$)")
    ax.set_ylabel("scale factor relative to $x_4 = 0$")
```

Both areas get the same three curves: the 3-space factor $e^{a_4}$ (solid red), the hidden scale $f = e^{-a_4/3}$ (dashed blue) and their product $e^{2a_4/3}$ (dotted black), and dots (`"o"`) and squares (`"s"`, marker size `ms=6`) at the five slices. The left area keeps an ordinary vertical axis, the right one gets a logarithmic axis (`set_yscale("log")`).

```python
axes[0].set_title("Ordinary vertical axis")
axes[1].set_title("Logarithmic vertical axis: straight lines")
axes[0].legend(fontsize=8)
save_figure(fig, "history_scale_factors",
            "The time dependence of the scale factors along the deflating history "
            "$a_4 = A H x_4$, $b_4 = b_4(0)\\,e^{\\beta A H x_4}$ with $A = 1$, "
...
report("3-space growth factor at the last slice a4 = 2", f"{np.exp(2.0):.6f}")
report("shrink factor f of x0 and the extra times at the last slice a4 = 2",
       f"{np.exp(-2.0 / 3.0):.6f}")
```

Titles, one legend (in the left area), and the figure is saved. The two `report` lines print the RESULT lines $e^2 = 7.389056$ and $e^{-2/3} = 0.513417$ of Section 3.8.

```python
product_last = np.exp(slices[-1]) * np.exp(-rate_t * slices[-1])
check(abs(product_last - np.exp(2.0 * slices[-1] / 3.0)) < 1e-14 and rate_t > 0,
      "x0 and the extra times deflate (rate 1/3 of a4'), the product grows like "
      "e^(2 a4/3)")
```

`slices[-1]` is the last slice, $a_4 = 2$. The product of the two factors there must equal $e^{4/3}$, and `rate_t` must be positive, which means that $f$ shrinks while $a_4$ grows: deflation.

**What Figure 03a.3 shows.** On the ordinary axis (left), 3-space grows from $1$ to $e^{2.5} = 12.2$ over the plotted time, while the hidden scale falls from $1$ to $e^{-2.5/3} = 0.43$; on the logarithmic axis (right) both are straight lines, with the slopes $+1$ and $-1/3$ of their rates (the logarithm of $e^{cx_4}$ is $cx_4$), and the product is a straight line of slope $2/3$. At the last slice, $x_4 = 2$, the factors are $7.39$ and $0.513$, and the product is $e^{4/3} = 3.79$.

**In [15], the functions of $z$.**

```python
z_line = -np.pi + (np.arange(1200) + 0.5) * (2 * np.pi / 1200)  # no degenerate point
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
axes[0].plot(z_line, np.abs(np.sin(z_line)) ** (1 / 6), color=RED, lw=1.8,
             label="warp factor $W = (\\sin^2 z)^{1/12}$")
axes[0].plot(z_line, np.abs(np.sin(z_line)) ** (1 / 3), color=ORANGE, lw=1.8,
             ls="--", label="$W^2 = (\\sin^2 z)^{1/6}$ (in $g_{55}$)")
axes[0].set_ylim(0.0, 1.25)
axes[0].set_title("The warp of the three extra times")
```

1200 midpoints across two cells, built like the grid of In [8], so that no point is degenerate. The left area shows the warp factor $W = |\sin z|^{1/6}$ (solid red) and its square $W^2 = |\sin z|^{1/3}$ (dashed orange), on a vertical range from $0$ to $1.25$.

```python
axes[1].plot(z_line, np.abs(1 / np.tan(z_line)), color=AQUA, lw=1.8,
             label="$|\\cot z|$ (in the scale factor of $x_0$)")
axes[1].plot(z_line, 1 / np.tan(z_line) ** 2, color=VIOLET, lw=1.8, ls="--",
             label="$\\cot^2 z$ (in $g_{00}$)")
axes[1].set_yscale("log")
axes[1].set_title("The hidden direction (logarithmic axis)")
for ax in axes:
    ax.set_xlabel("$z = 6 H x_0$ (radians)")
    ax.set_ylabel("value (no unit)")
    ax.legend(fontsize=8, loc="upper center")
```

The right area shows $|\cot z|$ (solid aqua) and $\cot^2 z$ (dashed violet) on a logarithmic axis, because they span many powers of ten. The loop gives both areas their labels and legends.

```python
save_figure(fig, "hidden_direction",
            "The functions of the hidden coordinate $z = 6Hx_0$ in the corrected "
            "metric, across two cells $-\\pi < z < \\pi$; horizontal axes $z$ in "
...
check(abs(np.abs(np.sin(np.pi / 2)) ** (1 / 6) - 1.0) < 1e-15
      and abs(np.abs(np.sin(-np.pi / 2)) ** (1 / 6) - 1.0) < 1e-15,
      "the warp factor equals 1 at the folds z = pi/2 and z = -pi/2")
```

The figure is saved; the check confirms that $W = 1$ at the two folds of the plot.

**What Figure 03a.4 shows.** Left: $W$ and $W^2$ rise from $0$ at each tip ($z = 0, \pm\pi$) to $1$ at each fold ($z = \pm\pi/2$); $W$ rises more steeply near the tips, because a sixth root of a small number is larger than a cube root. Right: $|\cot z|$ and $\cot^2 z$ fall from very large values at each tip to $0$ at each fold (on the logarithmic axis the curves plunge downwards there). All four curves repeat with the period $\pi$ and are symmetric about each fold, as Section 3.5 showed.

**In [16], maps of the two scale factors over time and $z$.**

```python
x4_grid, z_grid2 = np.meshgrid(np.linspace(0.0, 2.5, 251),
                               np.linspace(0.01, np.pi - 0.01, 300))
a4_grid = A_value * H_value * x4_grid
hidden_map = np.log10(np.exp(-rate_t * a4_grid) * np.abs(1 / np.tan(z_grid2)))
extra_map = np.log10(np.exp(-rate_t * a4_grid) * np.abs(np.sin(z_grid2)) ** (1 / 6))
```

`np.meshgrid` makes two tables of $300 \times 251$ numbers: in `x4_grid` each row holds the 251 times from $0$ to $2.5$, and in `z_grid2` each column holds the 300 values of $z$ from $0.01$ to $\pi - 0.01$ (one cell). `a4_grid` is $a_4 = AHx_4$ on the grid. `hidden_map` is $\log_{10}$ of the hidden scale factor $f|\cot z| = e^{-a_4/3}|\cot z|$ and `extra_map` is $\log_{10}$ of the extra-time scale factor $fW = e^{-a_4/3}|\sin z|^{1/6}$ (`np.log10` is the logarithm to base 10).

```python
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
for ax, data, title in zip(axes, [hidden_map, extra_map],
                           ["hidden: $e^{-a_4}b_4^{1/2}|\\cot z|$",
                            "extra time: $e^{-a_4}b_4^{1/2}(\\sin^2 z)^{1/12}$"]):
    mesh = ax.pcolormesh(x4_grid, z_grid2, data, cmap=DIVERGING, vmin=-1.5,
                         vmax=1.5, shading="auto")
    ax.contour(x4_grid, z_grid2, data, levels=[0.0], colors="black",
               linewidths=1.0)
    ax.axhline(np.pi / 2, color="black", lw=0.8, ls=":")  # the fold
    ax.set_title(title)
    ax.set_xlabel("time $x_4$ (unit $1/H$)")
    ax.grid(False)
axes[0].set_ylabel("$z = 6 H x_0$ (radians)")
fig.colorbar(mesh, ax=axes, label="$\\log_{10}$ of the scale factor")
```

Two areas side by side with a common vertical axis (`sharey=True`). For each map, `pcolormesh` colours every small rectangle of the grid by its value, on the two-sided colour scale from $-1.5$ (blue) to $1.5$ (red), with $0$ grey (`shading="auto"` centres each rectangle on its grid point); `contour(..., levels=[0.0])` draws the black line where the value is $0$, that is where the scale factor is $1$; `axhline` marks the fold $z = \pi/2$ with a dotted line. One colour bar serves both maps.

```python
save_figure(fig, "scale_factor_maps",
            "Maps of the logarithm to base 10 of the scale factor of the hidden "
            "direction $e^{-a_4}b_4^{1/2}|\\cot z| = e^{-a_4/3}|\\cot z|$ (left) and "
...
check(np.all(np.diff(hidden_map, axis=1) < 0) and np.all(np.diff(extra_map, axis=1) < 0),
      "along the history x0 and the extra times shrink at every z")
```

`np.diff(..., axis=1)` takes the differences between neighbouring times in every row (every value of $z$). All of them must be negative: at every $z$ both scale factors shrink with time (each step of $0.01$ in $x_4$ lowers both logarithms by $0.01/(3\ln 10) = 0.00145$).

**What Figure 03a.5 shows.** Left: the hidden scale factor is large (red) near the two tips and small (deep blue) along the fold; the black lines where it equals $1$ start at $z = \pi/4$ and $3\pi/4$ (where $|\cot z| = 1$) at $x_4 = 0$ and move towards the tips as time goes on, to $z = 0.41$ and $\pi - 0.41$ at $x_4 = 2.5$ (where $|\cot z| = e^{2.5/3} = 2.30$): the region where the factor is below $1$ widens, because $f$ shrinks. Right: the extra-time scale factor $f\,|\sin z|^{1/6}$ is below $1$ everywhere on the grid (pale blue), largest at the fold and at early times, and it darkens slowly as time goes on; the factor $1$ would be reached only at the fold at $x_4 = 0$, so no black line appears. Both maps are symmetric about the fold.

**In [17], the proper volumes** (Section 3.6).

```python
V3 = sp.simplify(h[1] * h[2] * h[3])  # proper 3-volume of a unit coordinate box
Vt = sp.simplify(h[5] * h[6] * h[7])  # the same in the three extra times
# the 7-volume: the sizes of every scale factor except h[4] = 1 of the time x4
V7 = f_hidden * abs_cot * V3 * Vt  # the size of h[0] is f |cot z|
say(f"V3 = {plain(V3)},  Vt = {plain(Vt)}")
```

`V3` is the product of the three 3-space scale factors, $e^{3a_4}$, and `Vt` that of the three extra-time ones, $b_4^{3/2}e^{-3a_4}|\sin z|^{1/2}$ (as printed: `b4v**(3/2)*exp(-3*a4v)*sqrt(Abs(sin(z)))`). `V7`, the volume factor of the slice $x_4 = \mathrm{const}$, multiplies them with the size $f|\cot z|$ of the hidden scale factor (`abs_cot` from In [7]).

```python
check(sp.simplify(V7 - volume_factor) == 0
      and sp.simplify(sp.diff(sp.log(V7), x4) - (-a4_prime + 2 * b4_prime / b4)) == 0,
      "the 7-volume density is sqrt|det g| and changes with the rate -a4p + 2 b4p/b4")
```

The check confirms both statements of Section 3.6: `V7` equals the volume factor $\sqrt{|\det g|}$ of In [7], and the derivative of its logarithm with respect to $x_4$ is $-a_4' + 2b_4'/b_4$.

```python
s = sp.symbols("s", positive=True)  # s = sin z on the half cell
half_cell = sp.integrate(s ** sp.Rational(-1, 2), (s, 0, 1)) / (6 * H)
say(f"proper 7-volume of a half cell per unit transverse coordinate volume = "
    f"e^(-a4) b4^2 times {half_cell}")
check(half_cell == 1 / (3 * H),
      "a half cell has the proper 7-volume e^(-a4) b4^2/(3H) per unit coordinate "
      "volume")
```

The last line of the integral of Section 3.6, $\frac{1}{6H}\int_0^1 s^{-1/2}\,ds$: `sp.integrate(expression, (s, 0, 1))` integrates exactly from $0$ to $1$ (sympy handles the growth of $s^{-1/2}$ at $s = 0$). The output is `1/(3*H)`, and the check compares it with $1/(3H)$.

**In [18], the proper volumes along the history.**

```python
z_fixed = np.pi / 3
f_line = np.exp(-rate_t * a4_line)  # f = e^(-a4/3) on the history
v3 = np.exp(3 * a4_line)
vt = f_line ** 3 * np.abs(np.sin(z_fixed)) ** 0.5
v7 = v3 * vt * f_line * np.abs(1 / np.tan(z_fixed))
```

At the fixed hidden position $z = \pi/3$, along the history: `f_line` is $f = e^{-a_4/3}$, `v3` is $V_3 = e^{3a_4}$, `vt` is $V_t = f^3|\sin z|^{1/2}$, and `v7` is the 7-volume density $V_3V_t\,f|\cot z|$.

```python
fig, ax = plt.subplots()
ax.plot(x4_line, v3, color=RED, lw=1.8, label="$V_3 = e^{3a_4}$")
ax.plot(x4_line, vt, color=BLUE, lw=1.8, ls="--",
        label="$V_t = f^3(\\sin^2 z)^{1/4}$")
ax.plot(x4_line, v3 * vt, color=ORANGE, lw=1.8, ls="-.",
        label="$V_3 V_t = e^{3a_4}f^3(\\sin^2 z)^{1/4}$")
ax.plot(x4_line, v7, color="black", lw=1.2, ls=":",
        label="7-volume density $e^{-a_4}b_4^2|\\cot z|(\\sin^2 z)^{1/4}$")
ax.set_yscale("log")
ax.set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$, "
              "$b_4 = e^{4x_4/3}$")
ax.set_ylabel("proper volume per unit coordinate volume")
ax.set_title("Proper volumes at $z = \\pi/3$")
ax.legend(fontsize=8)
```

Four curves on a logarithmic axis: $V_3$ (solid red), $V_t$ (dashed blue), their product (dash-dotted orange) and the 7-volume density (dotted black), with labels, title and legend.

```python
save_figure(fig, "proper_volumes",
            "Proper volumes per unit coordinate volume at the fixed hidden position "
            "$z = \\pi/3$ along the history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ "
...
at_start = 0.75 ** 0.25 / 3 ** 0.5  # (sin^2 z)^(1/4) |cot z| at z = pi/3
check(np.max(np.abs(v7 / (at_start * np.exp(5.0 * a4_line / 3.0)) - 1.0)) < 1e-12,
      "the 7-volume density at z = pi/3 grows like e^(5 a4/3) along the history")
```

At $z = \pi/3$, $\sin^2 z = 3/4$ and $|\cot z| = 1/\sqrt3$, so the density starts at `at_start` $= (3/4)^{1/4}/\sqrt3 = 0.537$. The check requires `v7` to equal $0.537\,e^{5a_4/3}$ at every plotted time, to a relative $10^{-12}$: the rate $\frac53 a_4'$ of Section 3.6.

**What Figure 03a.6 shows.** On the logarithmic axis all four curves are straight lines: $V_3$ rises with slope $3$, $V_t$ falls with slope $-1$ (on the history $f^3 = e^{-a_4}$), their product rises with slope $2$ from $(3/4)^{1/4} = 0.931$, and the 7-volume density rises with slope $5/3$ from $0.537$. The hidden factor $f|\cot z|$ pulls the 7-volume density below the product and makes it grow more slowly, by the factor $e^{-a_4/3}$.

**In [19], the hidden coordinate $y$ and the block form** (Section 3.9).

```python
geometry = ks_theory["geometry"]  # the statements of the record about the geometry
for key in ("hiddenCoordinate", "lineElement", "warp", "sqrtDetG"):
    say(f"record, {key}: {geometry[key]}")
```

The cell prints four statements of the section `geometry` of the Kohn-Sham theory record (read in In [13]): the definition of $y$ (with the fold at $y = 0$, the tip at $y \to -\infty$ and the two halves of a cell as the doubled system), the line element in the block form, the warp factor (on the extra times only; 3-space has no warp) and the volume factor in $y$.

```python
y_of_x0 = sp.log(sp.sin(6 * H * x0) ** 2) / (12 * H)  # y = ln|sin z|/(6H)
dy_dx0 = sp.diff(y_of_x0, x0)  # the chain rule, done by sympy
say(f"dy/dx0 = {plain(dy_dx0)}")
record_check(LEAD_EMT, "ks_coordinate_jacobian")  # stops if not passed
check(sp.simplify(dy_dx0 - sp.cot(6 * H * x0)) == 0,
      "dy/dx0 = cot z",
      record=f"{LEAD_EMT}, check ks_coordinate_jacobian")
```

`y_of_x0` is $y = \ln(\sin^2 z)/(12H)$, the form of $y$ that needs no absolute value. sympy differentiates it with respect to $x_0$ and prints `cos(z)/sin(z)`, the derivation of Section 3.9 line by line done by the computer. After `record_check` has confirmed the lead's check `ks_coordinate_jacobian`, the check compares the derivative with $\cot z$.

```python
check(sp.simplify(f_hidden ** 2 * dy_dx0 ** 2 - g[0, 0]) == 0,
      "g00 dx0^2 = f^2 dy^2: a step dy has the proper length f dy")
check(sp.simplify(sp.exp(H * y_of_x0) - twelfth) == 0,
      "the warp factor W = (sin^2 z)^(1/12) equals e^(H y)")
```

Two checks of Section 3.9: $f^2(dy/dx_0)^2 = g_{00}$, which says $g_{00}\,dx_0^2 = f^2\,dy^2$; and $e^{Hy} = (\sin^2 z)^{1/12} = W$.

```python
y = sp.symbols("y", negative=True)  # the hidden coordinate, y < 0 off the fold
arcsine = sp.asin(sp.exp(6 * H * y))
W = sp.exp(H * y)  # the warp factor in the coordinate y
block = sp.diag(*([f_hidden ** 2] + [sp.exp(2 * a4)] * 3 + [-1]
                  + [-f_hidden ** 2 * W ** 2] * 3))  # the form of the record
```

`y` is a new symbol, declared negative (every point off the fold has $y < 0$). On the first quarter of the period, $0 < z < \pi/2$, the relation $|\sin z| = e^{6Hy}$ is inverted by $z = \arcsin(e^{6Hy})$ (`sp.asin` is the inverse sine). `W` is the warp factor $e^{Hy}$, and `block` is the diagonal metric of the record's line element in the coordinates $(y, x_1, \dots, x_7)$: $f^2$, three times $e^{2a_4}$, $-1$, three times $-f^2e^{2Hy}$ (the star in `sp.diag(*[...])` hands the entries of the list to `sp.diag` one by one).

```python
same_form = []
for z_of_y in (arcsine, sp.pi - arcsine, sp.pi + arcsine, -arcsine):
    x0_of_y = z_of_y / (6 * H)  # the inverse on one quarter
    dx0_dy = sp.diff(x0_of_y, y)  # dx0/dy
    g_y = sp.diag(g[0, 0].subs(x0, x0_of_y) * dx0_dy ** 2,
                  *[g[k, k].subs(x0, x0_of_y) for k in range(1, 8)])
    same_form.append((g_y - block).applyfunc(sp.simplify) == sp.zeros(8, 8))
```

On each of the four quarters of the period the inverse relation is different: $z = \arcsin(e^{6Hy})$, $\pi - \arcsin(e^{6Hy})$, $\pi + \arcsin(e^{6Hy})$ and $-\arcsin(e^{6Hy})$ (each gives $|\sin z| = e^{6Hy}$, with the signs of $\sin z$ and $\cos z$ of its quarter). For each, the metric is written in the coordinate $y$: the hidden entry becomes $g_{00}(dx_0/dy)^2$, because $dx_0 = (dx_0/dy)\,dy$, and the seven other entries only need $x_0$ replaced by its expression in $y$. `same_form` collects, quarter by quarter, whether the result equals `block` entry by entry.

```python
for k in (0, 1, 4, 5):
    say(f"  in the coordinate y: g[{k}, {k}] = {plain(block[k, k])}")
check(all(same_form) and len(same_form) == 4
      and geometry["warp"].startswith("W(y) = e^{Hy} on the extra times only")
      and "f(x4)^2 [dy^2 - e^{2Hy} (dx5^2+dx6^2+dx7^2)]" in geometry["lineElement"],
      "on all four quarters the metric in y is the block form of the record, with "
      "f = e^(-a4) b4^(1/2) and W = e^(H y)",
      record="Revision/kohn_sham/ks-theory.json, geometry.lineElement and "
             "geometry.warp")
```

The cell prints four entries of the block form (`b4v*exp(-2*a4v)` is $f^2$, `-b4v*exp(-2*a4v)*exp(2*H*y)` is $-f^2e^{2Hy}$) and checks that all four quarters gave the block form and that the record still writes the warp and the line element in these words.

```python
root = sp.exp(-a4) * b4 ** 2 * sp.exp(3 * H * y)  # positive: compare the squares
check(sp.simplify(block.det() - root ** 2) == 0
      and geometry["sqrtDetG"].startswith("e^{-a4} b4^2 e^{3Hy}"),
      "in the coordinate y, sqrt|det g| is e^(-a4) b4^2 e^(3 H y), as the record "
      "states",
      record="Revision/kohn_sham/ks-theory.json, geometry.sqrtDetG")
```

The volume factor in $y$: the determinant of `block` must equal the square of $e^{-a_4}b_4^2e^{3Hy}$ (comparing squares avoids a square root; the root is positive, so the squares decide). The record's text must begin with the same formula.

```python
# the proper distance from the fold is f (0 - y); -y grows without bound at the tip
check(sp.limit(-y_of_x0, x0, 0, "+") == sp.oo,
      "the tip z -> 0 lies at y -> minus infinity: infinitely far from the fold")
```

`sp.limit(expression, x0, 0, "+")` is the limit as $x_0$ approaches $0$ from above; `sp.oo` is sympy's infinity. The limit of $-y$ is infinite, so the proper distance $f\,|y|$ of a point near the tip from the fold grows without bound: the tip is infinitely far away.

**In [20], the tip cut-off and the coordinate $y$** (Section 3.9).

```python
L_exact = sp.nsimplify(L_tip)  # the number 3.0 of the record as the exact integer 3
y_any = sp.symbols("y_any", real=True)  # y as a real variable of integration
fraction = sp.integrate(sp.exp(3 * H * y_any), (y_any, -sp.oo, -L_exact / H)) \
    / sp.integrate(sp.exp(3 * H * y_any), (y_any, -sp.oo, 0))
fraction = sp.simplify(fraction.subs(H, 1))
report("fraction of the 7-volume beyond the tip cut-off y = -3", sp.sstr(fraction),
       f"= {float(fraction):.4e}")
```

`sp.nsimplify` turns the decimal number $3.0$ of the record into the exact integer $3$. The fraction of Section 3.9 is computed exactly: the integral of the volume density $e^{3Hy}$ from $-\infty$ to $-L/H$ divided by the integral from $-\infty$ to $0$, then simplified at $H = 1$. The RESULT line prints it as `exp(-9)` and as the number $1.2341\times 10^{-4}$ (`sp.sstr` writes the exact expression as text; the third argument of `report` is printed after it).

```python
z_cut = float(sp.asin(sp.exp(-18)))  # the angle z of the cut-off, sin z = e^(-18)
report("angle z of the tip cut-off", f"{z_cut:.4e}", "radians")
say("record, hiddenScale: " + geometry["hiddenScale"])
```

At $y = -3$ (with $H = 1$), $|\sin z| = e^{6Hy} = e^{-18}$, so the cut-off angle is $\arcsin e^{-18} = 1.5230\times 10^{-8}$ radians. The last line prints the record's statement of the hidden scale: $f = e^{-a_4}b_4^{1/2}$, which on the history is $e^{-a_4/3}$, and the proper hidden length $fL$ of the cut-off half cell.

```python
z_line = np.logspace(-10, np.log10(np.pi / 2), 800)  # 1e-10 ... pi/2, evenly in log
y_line = np.log(np.sin(z_line)) / 6.0  # with H = 1
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
axes[0].plot(z_line, y_line, color=VIOLET, lw=1.8, label="$y(z)$")
axes[0].axhline(-L_tip, color="black", lw=1.0, ls="--",
                label=f"tip cut-off $y = -L = -{L_tip:g}$")
axes[0].plot([z_cut], [-L_tip], "o", color="black", ms=6)
axes[0].set_xscale("log")
axes[0].set_xlabel("$z = 6 H x_0$ (radians, logarithmic axis)")
axes[0].set_ylabel("$y = \\ln|\\sin z|/(6H)$ (unit $1/H$)")
axes[0].set_title("The hidden coordinate $y$ on a half cell")
axes[0].legend(fontsize=8)
```

`np.logspace(-10, np.log10(np.pi / 2), 800)` gives 800 values of $z$ from $10^{-10}$ to $\pi/2$, evenly spaced on a logarithmic scale, so that the region near the tip is visible. `y_line` is $y = \ln(\sin z)/6$ there ($H = 1$; on this half cell $\sin z > 0$). The left area draws $y(z)$ with a logarithmic $z$ axis, the dashed line of the cut-off $y = -3$ (the format `:g` prints $3.0$ as `3`) and a dot where the curve meets it.

```python
y_axis = np.linspace(-4.0, 0.0, 400)
axes[1].plot(y_axis, np.exp(y_axis), color=RED, lw=1.8,
             label="warp factor $W = e^{Hy} = (\\sin^2 z)^{1/12}$")
axes[1].plot(y_axis, np.exp(2 * y_axis), color=ORANGE, lw=1.8, ls="-.",
             label="$W^2 = e^{2Hy} = (\\sin^2 z)^{1/6}$")
axes[1].plot(y_axis, np.exp(3 * y_axis), color=AQUA, lw=1.8, ls="--",
             label="7-volume density per $e^{-a_4}b_4^2$: $e^{3Hy}$")
axes[1].axvspan(-4.0, -L_tip, color="grey", alpha=0.25,
                label="removed by the tip cut-off")
axes[1].set_xlabel("$y$ (unit $1/H$)")
axes[1].set_ylabel("value (no unit)")
axes[1].set_title("Warp and volume density in $y$")
axes[1].legend(fontsize=8, loc="upper left")
```

The right area draws, against $y$ from $-4$ to $0$, the warp factor $e^{y}$ (solid red), its square $e^{2y}$ (dash-dotted orange) and the 7-volume density $e^{3y}$ in the unit $e^{-a_4}b_4^2$ (dashed aqua), and shades the band beyond the cut-off (`axvspan`, 25 per cent opaque).

```python
save_figure(fig, "hidden_coordinate_y",
            "The hidden coordinate $y = \\ln|\\sin z|/(6H)$ with $H = 1$. Left: $y$ "
            "versus $z = 6Hx_0$ in radians on a logarithmic axis from $10^{-10}$ to "
...
check(fraction == sp.exp(-9), "the cut-off removes exactly the fraction e^(-9)")
```

The figure is saved; the check requires the exact fraction to be $e^{-9}$.

**What Figure 03a.7 shows.** Left: $y$ is $0$ at the fold $z = \pi/2$ and falls without bound towards the tip; on the logarithmic $z$ axis it becomes the straight line $y \approx \ln(z)/6$ near the tip (there $\sin z \approx z$), and it crosses the cut-off $y = -3$ at $z = 1.5\times 10^{-8}$. Right: the three exponentials fall from $1$ at the fold towards $0$, the faster the larger the exponent; the shaded band beyond $y = -3$ holds only the fraction $e^{-9} = 1.2\times 10^{-4}$ of the 7-volume of the half cell.

**In [21], the last check.**

```python
figure_names = ["metric_heat_map", "diagonal_entries", "history_scale_factors",
                "hidden_direction", "scale_factor_maps", "proper_volumes",
                "hidden_coordinate_y"]
files = [output_file(f"{FIGURE_FOLDER}/03a_{k}_{n}.png")
         for k, n in enumerate(figure_names, 1)]
check(all(path.is_file() for path in files), "all seven figure files exist")
all_checks_passed()
```

The seven figure names in their order; `enumerate(figure_names, 1)` numbers them from $1$, so `files` holds the seven paths `Revision/textbook/figures/03a_1_metric_heat_map.png` to `03a_7_hidden_coordinate_y.png` (below the folder in which the notebook writes, `output_file`). The check requires all seven files to exist, and `all_checks_passed()` prints the last line, ALL 30 CHECKS PASSED (notebook 03a). The 30 checks are: 1 in In [5], 2 in In [6], 3 in In [7], 3 in In [8], 1 each in In [9], In [10] and In [11], 2 each in In [12] and In [13], 1 each in In [14], In [15] and In [16], 2 in In [17], 1 in In [18], 6 in In [19], and 1 each in In [20] and In [21].

### 3.14 Vectors, covectors and tensors

The metric turns coordinate steps into lengths. To speak about curvature we must first say precisely what a vector is and why some indices are written up and others down. The idea is simple: the same arrow has different components in different coordinates, and the rule by which the components change decides where the index goes.

**A change of coordinates.** Suppose a second set of coordinates $x'^1, \dots, x'^n$ names the same points, each new coordinate being a function of the old ones, $x'^a = x'^a(x^1, \dots, x^n)$, and each old one a function of the new ones. The $n \times n$ table of partial derivatives $\partial x'^a/\partial x^b$ is the **Jacobian matrix** of the change. The two tables $\partial x'^a/\partial x^b$ and $\partial x^a/\partial x'^b$ are inverse matrices:

$$
\sum_{b=1}^{n} \frac{\partial x'^a}{\partial x^b}\,\frac{\partial x^b}{\partial x'^c} = \frac{\partial x'^a}{\partial x'^c} = \delta^a{}_c
$$

(the chain rule applied to the function $x'^a(x(x'))$, which is just $x'^a$; the derivative of a coordinate with respect to a coordinate of the same set is $1$ for the same one and $0$ for another).

**Vectors.** A **curve** is a point that moves with a parameter $\lambda$ (a time, or a length along the curve): $x^a(\lambda)$. Its **velocity** has the components $u^a = dx^a/d\lambda$. In the new coordinates the same curve is $x'^a(x(\lambda))$, and

$$
u'^a = \frac{dx'^a}{d\lambda} = \sum_b \frac{\partial x'^a}{\partial x^b}\,\frac{dx^b}{d\lambda} = \sum_b \frac{\partial x'^a}{\partial x^b}\,u^b
$$

(the chain rule for a function of several variables, each of which depends on $\lambda$). A **vector** at a point is a set of $n$ numbers $V^a$, one set for every system of coordinates, such that the sets of two systems are related by exactly this rule, $V'^a = \sum_b (\partial x'^a/\partial x^b)\,V^b$. Its index is written **up**. A small coordinate step $dx^a$ is a vector, which is why we write its index up.

**Covectors.** The **gradient** of a function $f$ has the components $W_a = \partial_a f$. In the new coordinates

$$
W'_a = \frac{\partial f}{\partial x'^a} = \sum_b \frac{\partial x^b}{\partial x'^a}\,\frac{\partial f}{\partial x^b} = \sum_b \frac{\partial x^b}{\partial x'^a}\,W_b
$$

(the chain rule again, now for $f(x(x'))$). A **covector** is a set of $n$ numbers $W_a$ for every system of coordinates that changes by this rule. Its index is written **down**. The table that converts it is the inverse Jacobian matrix, $\partial x/\partial x'$ instead of $\partial x'/\partial x$.

**An upper index summed with a lower index gives the same number in every system of coordinates.** For a vector $V$ and a covector $W$:

$$
\sum_a V'^a W'_a = \sum_a \Bigl(\sum_b \frac{\partial x'^a}{\partial x^b} V^b\Bigr)\Bigl(\sum_c \frac{\partial x^c}{\partial x'^a} W_c\Bigr)
$$

(the two rules inserted)

$$
= \sum_{b,c} \Bigl(\sum_a \frac{\partial x^c}{\partial x'^a}\,\frac{\partial x'^a}{\partial x^b}\Bigr) V^b W_c
$$

(the order of finite sums may be changed, and numbers may be multiplied in any order)

$$
= \sum_{b,c} \delta^c{}_b\, V^b W_c = \sum_b V^b W_b
$$

(the inverse-matrix identity above, with the roles of the two systems exchanged; then the Kronecker delta keeps only $c = b$). Such a sum is called a **contraction**. For example the rate of change of a function along a curve, $df/d\lambda = \sum_a u^a\,\partial_a f$ (the chain rule), is a contraction of a vector with a covector, so it does not depend on the coordinates, as it must not. A warning: summing an upper index with another upper index does NOT have this property. In one dimension, under the change $x' = 2x$ every vector is doubled, $V' = 2V$ and $W' = 2W$ for two vectors, so the product $V'W' = 4VW$ depends on the coordinates.

**Tensors.** A **tensor** with $p$ upper and $q$ lower indices is a table of $n^{p+q}$ numbers for every system of coordinates that changes with one factor $\partial x'/\partial x$ for every upper index and one factor $\partial x/\partial x'$ for every lower index. For example $T'^a{}_b = \sum_{c,d} (\partial x'^a/\partial x^c)(\partial x^d/\partial x'^b)\,T^c{}_d$. Three facts follow from the definition, by the computation just made: a contraction of one upper with one lower index of a tensor is again a tensor (with two fewer indices); a product of tensors is a tensor; and a quantity in which every index is contracted, an **invariant** (or scalar), has the same value in every system of coordinates. Moreover, if all the numbers of a tensor are zero in one system of coordinates, they are zero in every system, because each new number is a sum of old numbers times factors.

**The metric is a tensor with two lower indices.** The squared length of a small step is a property of the step, not of the coordinates in which we describe it. So

$$
\sum_{a,b} g_{ab}\, dx^a dx^b = \sum_{a,b} g_{ab} \Bigl(\sum_c \frac{\partial x^a}{\partial x'^c} dx'^c\Bigr)\Bigl(\sum_d \frac{\partial x^b}{\partial x'^d} dx'^d\Bigr)
$$

(each old step written with the new steps by the chain rule), and comparing with $\sum_{c,d} g'_{cd}\,dx'^c dx'^d$, the coefficients of the new metric are

$$
g'_{cd} = \sum_{a,b} \frac{\partial x^a}{\partial x'^c}\,\frac{\partial x^b}{\partial x'^d}\, g_{ab}
$$

(the coefficient of $dx'^c dx'^d$ collected from the double sum; we may compare coefficient by coefficient because both metrics are symmetric). Two lower indices, two factors $\partial x/\partial x'$. The inverse metric $g^{ab}$ is a tensor with two upper indices.

**Raising and lowering indices.** The metric turns a vector into a covector, $V_a = \sum_b g_{ab}V^b$, and the inverse metric turns a covector into a vector, $W^a = \sum_b g^{ab}W_b$; doing both returns the original, because $\sum_b g^{ab}g_{bc} = \delta^a{}_c$. The same rule raises or lowers any index of any tensor. The squared length of a vector is the invariant $g(V, V) = \sum_{a,b} g_{ab}V^aV^b = \sum_a V^aV_a$. For a diagonal metric raising or lowering only multiplies: $V_a = g_{aa}V^a$ (no sum).

**Example: a constant field in polar coordinates.** In the plane take the field $e_x$ that points one unit to the right everywhere: Cartesian components $(V^x, V^y) = (1, 0)$. With $r = \sqrt{x^2 + y^2}$ and the angle $\varphi$ (in the right half of the plane $\varphi = \arctan(y/x)$),

$$
\frac{\partial r}{\partial x} = \frac{x}{r} = \cos\varphi, \qquad \frac{\partial \varphi}{\partial x} = \frac{1}{1 + y^2/x^2}\cdot\Bigl(-\frac{y}{x^2}\Bigr) = -\frac{y}{x^2 + y^2} = -\frac{\sin\varphi}{r}
$$

(the chain rule: the derivative of $\sqrt{u}$ is $1/(2\sqrt u)$ times $du/dx = 2x$; the derivative of $\arctan u$ is $1/(1 + u^2)$ times $du/dx = -y/x^2$; then $x = r\cos\varphi$ and $y = r\sin\varphi$). The vector rule gives the polar components

$$
V^r = \frac{\partial r}{\partial x}\cdot 1 + \frac{\partial r}{\partial y}\cdot 0 = \cos\varphi, \qquad V^\varphi = \frac{\partial\varphi}{\partial x}\cdot 1 + \frac{\partial\varphi}{\partial y}\cdot 0 = -\frac{\sin\varphi}{r} .
$$

The field is constant, yet its polar components change from point to point. So the plain derivatives $\partial_b V^a$ of the components are not a good measure of how a vector field changes. The next section repairs this.

### 3.15 The covariant derivative and the Christoffel symbols

**The problem.** In the example of Section 3.14, $\partial_\varphi V^r = -\sin\varphi$ is not zero, although the field does not change at all: the derivative also records the turning of the coordinate directions. In general, differentiating the vector rule $V'^a = \sum_b (\partial x'^a/\partial x^b)V^b$ produces, besides the tensor rule, a term with the second derivatives $\partial^2 x'^a/\partial x^b\partial x^c$ of the change of coordinates, so $\partial_b V^a$ is not a tensor.

**Definition (covariant derivative).** We add a correction that is linear in $V$:

$$
\nabla_b V^a = \partial_b V^a + \sum_c \Gamma^a{}_{bc}\,V^c .
$$

The $n^3$ numbers $\Gamma^a{}_{bc}$ at each point are the **connection coefficients**; they are chosen so that $\nabla_b V^a$ is a tensor, which fixes how they change between systems of coordinates (we do not need that rule). For a function $f$ (a tensor without indices) we set $\nabla_b f = \partial_b f$.

**Covectors.** We require the product rule for the function $\sum_a V^aW_a$:

$$
\partial_b\Bigl(\sum_a V^aW_a\Bigr) = \sum_a (\nabla_b V^a)W_a + \sum_a V^a\,\nabla_b W_a .
$$

The left side is $\sum_a (\partial_b V^a)W_a + \sum_a V^a\,\partial_b W_a$ (the ordinary product rule). The first term on the right is $\sum_a (\partial_b V^a)W_a + \sum_{a,c}\Gamma^a{}_{bc}V^cW_a$ (the definition). Subtracting,

$$
\sum_a V^a\,\nabla_b W_a = \sum_a V^a\,\partial_b W_a - \sum_{a,c} \Gamma^a{}_{bc}V^cW_a = \sum_a V^a\Bigl(\partial_b W_a - \sum_c \Gamma^c{}_{ba}W_c\Bigr)
$$

(in the double sum the two summed letters $a$ and $c$ were renamed $c$ and $a$; a summed letter is only a name). This holds for every vector $V$, so

$$
\nabla_b W_a = \partial_b W_a - \sum_c \Gamma^c{}_{ba}\,W_c .
$$

**Tensors with two indices.** Again we require the product rule. Take first a product $T^a{}_b = V^aW_b$ of a vector and a covector (a tensor with one upper and one lower index, Section 3.14):

$$
\nabla_c\bigl(V^aW_b\bigr) = \bigl(\nabla_c V^a\bigr)W_b + V^a\,\nabla_c W_b
$$

(the product rule, required)

$$
= \Bigl(\partial_c V^a + \sum_e \Gamma^a{}_{ce}V^e\Bigr)W_b + V^a\Bigl(\partial_c W_b - \sum_e \Gamma^e{}_{cb}W_e\Bigr)
$$

(the two formulas just proved, with the letters $b, c$ of the vector formula renamed $c, e$ and the letters $b, a, c$ of the covector formula renamed $c, b, e$)

$$
= \partial_c\bigl(V^aW_b\bigr) + \sum_e \Gamma^a{}_{ce}\,\bigl(V^eW_b\bigr) - \sum_e \Gamma^e{}_{cb}\,\bigl(V^aW_e\bigr)
$$

(the ordinary product rule $\partial_c(V^aW_b) = (\partial_cV^a)W_b + V^a\,\partial_cW_b$ collects the two terms without $\Gamma$; in the other two terms the factors are regrouped). In the notation $T^a{}_b = V^aW_b$, so that $V^eW_b = T^e{}_b$ and $V^aW_e = T^a{}_e$, this reads

$$
\nabla_c T^a{}_b = \partial_c T^a{}_b + \sum_e \Gamma^a{}_{ce}\,T^e{}_b - \sum_e \Gamma^e{}_{cb}\,T^a{}_e .
$$

The same three steps for a product $T_{ab} = W_aU_b$ of two covectors give

$$
\nabla_c\bigl(W_aU_b\bigr) = \bigl(\nabla_c W_a\bigr)U_b + W_a\,\nabla_c U_b = \partial_c\bigl(W_aU_b\bigr) - \sum_e \Gamma^e{}_{ca}\,\bigl(W_eU_b\bigr) - \sum_e \Gamma^e{}_{cb}\,\bigl(W_aU_e\bigr)
$$

(the product rule; the covector formula twice; the ordinary product rule collects the terms without $\Gamma$). Every tensor with two indices is a sum of such products. For example, let $E_{(d)}$ be the vector field with the components $\delta^a{}_d$ (the unit step along $x_d$) and $\theta^{(f)}$ the covector field with the components $\delta^f{}_b$; then

$$
T^a{}_b = \sum_{d,f} T^d{}_f\,\delta^a{}_d\,\delta^f{}_b = \sum_{d,f} \bigl(T^d{}_f\,E_{(d)}\bigr)^a\,\bigl(\theta^{(f)}\bigr)_b
$$

(in the double sum only $d = a$ and $f = b$ give a non-zero product of deltas), a sum of products (64 of them in eight dimensions) of a vector (the field $E_{(d)}$ multiplied by the function $T^d{}_f$) and a covector. Both sides of the formula for $\nabla_c T^a{}_b$ are sums of terms each containing $T$ once, so the formula holds for a sum of products when it holds for each product; it therefore holds for every such tensor, and in the same way the formula for two lower indices holds for every tensor with two lower indices. With more indices the same steps, with more factors, give the general rule: **one term $+\sum_e\Gamma$ for every upper index and one term $-\sum_e\Gamma$ for every lower index**. For the metric (two lower indices):

$$
\nabla_c\, g_{ab} = \partial_c\, g_{ab} - \sum_e \Gamma^e{}_{ca}\,g_{eb} - \sum_e \Gamma^e{}_{cb}\,g_{ae} .
$$

**The two conditions of Levi-Civita.** A metric singles out one connection by two natural conditions:

1. no torsion: $\Gamma^a{}_{bc} = \Gamma^a{}_{cb}$ (symmetric in the two lower indices);
2. metric compatibility: $\nabla_c\, g_{ab} = 0$ (lengths and angles do not change when vectors are carried along without turning).

**Theorem (the Christoffel formula).** Exactly one connection satisfies both conditions:

$$
\Gamma^a{}_{bc} = \tfrac12 \sum_d g^{ad}\bigl(\partial_b\, g_{dc} + \partial_c\, g_{db} - \partial_d\, g_{bc}\bigr).
$$

These are the **Christoffel symbols**. Every Revision record and every notebook of the book uses this connection.

*Proof, line by line.* Lower the upper index: $\Gamma_{dbc} = \sum_a g_{da}\Gamma^a{}_{bc}$. Condition 1 says $\Gamma_{dbc} = \Gamma_{dcb}$. Condition 2, with the formula for $\nabla_c\, g_{ab}$, reads

$$
\partial_c\, g_{ab} = \Gamma_{bca} + \Gamma_{acb}
$$

(the two sums $\sum_e \Gamma^e{}_{ca}g_{eb}$ and $\sum_e \Gamma^e{}_{cb}g_{ae}$ are, by the definition of the lowered symbol and the symmetry of $g$, $\Gamma_{bca}$ and $\Gamma_{acb}$). Write this equation three times, with the three letters in the three cyclic orders:

$$
\partial_b\, g_{cd} = \Gamma_{dbc} + \Gamma_{cbd}, \qquad \partial_c\, g_{bd} = \Gamma_{dcb} + \Gamma_{bcd}, \qquad \partial_d\, g_{bc} = \Gamma_{cdb} + \Gamma_{bdc}
$$

(the previous equation with the letters renamed). Add the first two and subtract the third:

$$
\partial_b\, g_{cd} + \partial_c\, g_{bd} - \partial_d\, g_{bc} = \Gamma_{dbc} + \Gamma_{dcb} + (\Gamma_{cbd} - \Gamma_{cdb}) + (\Gamma_{bcd} - \Gamma_{bdc}) = 2\,\Gamma_{dbc}
$$

(by condition 1, $\Gamma_{cbd} = \Gamma_{cdb}$ and $\Gamma_{bcd} = \Gamma_{bdc}$, so the two brackets are zero, and $\Gamma_{dcb} = \Gamma_{dbc}$). Multiply by $\tfrac12 g^{ad}$ and sum over $d$:

$$
\Gamma^a{}_{bc} = \sum_d g^{ad}\,\Gamma_{dbc} = \tfrac12\sum_d g^{ad}\bigl(\partial_b\, g_{cd} + \partial_c\, g_{bd} - \partial_d\, g_{bc}\bigr)
$$

(the inverse metric undoes the lowering, because $\sum_d g^{ad}g_{de} = \delta^a{}_e$; and $g_{cd} = g_{dc}$, $g_{bd} = g_{db}$). So a connection with the two properties can only be this one. Conversely, the formula is symmetric in $b$ and $c$ (exchanging them exchanges the first two terms), and putting it into $\Gamma_{bca} + \Gamma_{acb}$ gives back $\partial_c\, g_{ab}$ (the four terms with derivatives of $g$ along other directions cancel in pairs), so it has both properties. (That the symbols computed in two systems of coordinates describe the same $\nabla$ is a standard fact that we quote, ASSUMED.) $\square$

**Diagonal metrics: four cases.** All metrics of this chapter are diagonal. Write $g_{aa} = \eta_{aa}h_a^2$ with the sign $\eta_{aa} = \pm1$ and the positive scale factor $h_a$ (Section 3.7), so that $g^{aa} = \eta_{aa}/h_a^2$ (no sum here and in the four cases). In the formula only $d = a$ survives, because $g^{ad} = 0$ for $d \ne a$:

$$
\Gamma^a{}_{bc} = \tfrac12\, g^{aa}\bigl(\partial_b\, g_{ac} + \partial_c\, g_{ab} - \partial_a\, g_{bc}\bigr) \quad\text{(no sum)} .
$$

(a) All three indices equal: $\Gamma^a{}_{aa} = \tfrac12 g^{aa}\,\partial_a g_{aa} = \tfrac12\,\frac{\eta_{aa}}{h_a^2}\,\eta_{aa}\,2h_a\,\partial_a h_a = \partial_a \ln h_a$ (two of the three terms cancel; the derivative of $h_a^2$ is $2h_a\,\partial_a h_a$; $\eta_{aa}^2 = 1$; and $\partial h/h = \partial \ln h$).

(b) One lower index equal to the upper one, $b \ne a$: $\Gamma^a{}_{ab} = \Gamma^a{}_{ba} = \tfrac12 g^{aa}\bigl(\partial_a g_{ab} + \partial_b g_{aa} - \partial_a g_{ab}\bigr) = \tfrac12 g^{aa}\,\partial_b\, g_{aa} = \partial_b \ln h_a$ (the first and the third terms cancel; the rest as in (a)).

(c) Two equal lower indices different from the upper one, $b \ne a$: $\Gamma^a{}_{bb} = \tfrac12 g^{aa}\bigl(2\,\partial_b\, g_{ab} - \partial_a\, g_{bb}\bigr) = -\tfrac12\, g^{aa}\,\partial_a\, g_{bb} = -\eta_{aa}\eta_{bb}\,\frac{h_b^2}{h_a^2}\,\partial_a \ln h_b$ (here $g_{ab} = 0$ because $a \ne b$; then $\partial_a g_{bb} = \eta_{bb}\,2h_b\,\partial_a h_b = 2\eta_{bb}h_b^2\,\partial_a\ln h_b$).

(d) Three different indices: $\Gamma^a{}_{bc} = 0$ (every metric entry in the bracket has two different indices and is zero).

**Example: the plane in polar coordinates.** $h_r = 1$, $h_\varphi = r$, both signs $+1$. Only $h_\varphi$ depends on a coordinate, on $r$. Case (b): $\Gamma^\varphi{}_{r\varphi} = \Gamma^\varphi{}_{\varphi r} = \partial_r \ln r = 1/r$. Case (c): $\Gamma^r{}_{\varphi\varphi} = -\frac{r^2}{1}\,\partial_r \ln r = -r$. All others are zero. Now the constant field $V^r = \cos\varphi$, $V^\varphi = -\sin\varphi/r$ of Section 3.14:

$$
\nabla_r V^r = \partial_r \cos\varphi + \Gamma^r{}_{rr}V^r + \Gamma^r{}_{r\varphi}V^\varphi = 0 + 0 + 0 = 0,
$$

$$
\nabla_\varphi V^r = \partial_\varphi \cos\varphi + \Gamma^r{}_{\varphi\varphi}V^\varphi = -\sin\varphi + (-r)\Bigl(-\frac{\sin\varphi}{r}\Bigr) = 0,
$$

$$
\nabla_r V^\varphi = \partial_r\Bigl(-\frac{\sin\varphi}{r}\Bigr) + \Gamma^\varphi{}_{r\varphi}V^\varphi = \frac{\sin\varphi}{r^2} + \frac1r\Bigl(-\frac{\sin\varphi}{r}\Bigr) = 0,
$$

$$
\nabla_\varphi V^\varphi = \partial_\varphi\Bigl(-\frac{\sin\varphi}{r}\Bigr) + \Gamma^\varphi{}_{\varphi r}V^r = -\frac{\cos\varphi}{r} + \frac1r\cos\varphi = 0
$$

(in each line the definition of $\nabla$, then the symbols just found, the others being zero). The covariant derivative of the constant field is zero, as it must be: the Christoffel terms remove exactly the change of the components that comes from the turning of the polar directions. Notebook 03c checks these four numbers (In [5]).

**Example: the sphere of radius $a$.** $h_\theta = a$, $h_\varphi = a\sin\theta$, both signs $+1$; only $h_\varphi$ depends on a coordinate, on $\theta$, with $\partial_\theta \ln(a\sin\theta) = \cos\theta/\sin\theta = \cot\theta$ (the logarithm of a product is the sum of the logarithms; the derivative of $\ln\sin\theta$ is $\cos\theta/\sin\theta$). Case (b): $\Gamma^\varphi{}_{\theta\varphi} = \Gamma^\varphi{}_{\varphi\theta} = \cot\theta$. Case (c): $\Gamma^\theta{}_{\varphi\varphi} = -\frac{a^2\sin^2\theta}{a^2}\cot\theta = -\sin\theta\cos\theta$. All others are zero.

**The contracted symbol and the volume factor.** For a diagonal metric, summing case (a) and case (b) over the upper index,

$$
\sum_a \Gamma^a{}_{ab} = \sum_a \partial_b \ln h_a = \partial_b \ln\Bigl(\prod_a h_a\Bigr) = \partial_b \ln\sqrt{|\det g|}
$$

(for $a = b$ case (a), for $a \ne b$ case (b), both give $\partial_b \ln h_a$; a sum of logarithms is the logarithm of the product; the product of the scale factors is the volume factor of Section 3.6). This identity is used for the author's metric in Section 3.23.

### 3.16 Parallel transport and geodesics

**The derivative along a curve.** Let $x^a(\lambda)$ be a curve with velocity $u^a = dx^a/d\lambda$, and $V^a(\lambda)$ a vector given at each point of the curve. If $V$ is the value of a vector field on the curve, then $dV^a/d\lambda = \sum_b u^b\,\partial_b V^a$ (the chain rule), and therefore

$$
\sum_b u^b\,\nabla_b V^a = \frac{dV^a}{d\lambda} + \sum_{b,c}\Gamma^a{}_{bc}\,u^bV^c =: \frac{DV^a}{d\lambda}
$$

(the definition of $\nabla$, multiplied by $u^b$ and summed). The right side needs $V$ only on the curve, so it defines the **covariant derivative along the curve** for any $V(\lambda)$. A vector is **parallel transported** along the curve when $DV^a/d\lambda = 0$: it is carried along without turning.

**Geodesics.** A **geodesic** is a curve whose velocity is parallel transported along itself:

$$
\frac{d^2x^a}{d\lambda^2} + \sum_{b,c}\Gamma^a{}_{bc}\,\frac{dx^b}{d\lambda}\,\frac{dx^c}{d\lambda} = 0 \qquad (a = 1, \dots, n).
$$

In flat space with Cartesian coordinates every $\Gamma$ is zero, and the equation says $d^2x^a/d\lambda^2 = 0$: straight lines, run through at constant speed. A geodesic is the straightest curve that a curved space allows. In Einstein's theory a body on which no force other than gravity acts (a body in **free fall**) moves on a time-like geodesic; this is the physical content of the equation, which we take from the theory of gravity (ASSUMED).

**The squared speed does not change along a geodesic.** Lower the first index of the Christoffel symbol: by the proof of Section 3.15, $2\Gamma_{abc} = \partial_b\, g_{ca} + \partial_c\, g_{ba} - \partial_a\, g_{bc}$. Then, along a geodesic,

$$
\frac{d}{d\lambda}\sum_{a,b} g_{ab}u^au^b = \sum_{a,b,c} (\partial_c\, g_{ab})\,u^cu^au^b + 2\sum_{a,b} g_{ab}\,u^a\,\frac{du^b}{d\lambda}
$$

(the product rule; the metric changes along the curve by the chain rule; the two terms with $du/d\lambda$ are equal because $g$ is symmetric)

$$
= \sum_{a,b,c} (\partial_c\, g_{ab})\,u^cu^au^b - 2\sum_{a,b,c} \Gamma_{abc}\,u^au^bu^c
$$

(the geodesic equation $du^b/d\lambda = -\sum \Gamma^b{}_{cd}u^cu^d$, and $\sum_b g_{ab}\Gamma^b{}_{cd} = \Gamma_{acd}$, with the summed letters renamed)

$$
= \sum_{a,b,c} (\partial_c\, g_{ab})\,u^cu^au^b - \sum_{a,b,c}\bigl(\partial_b\, g_{ca} + \partial_c\, g_{ba} - \partial_a\, g_{bc}\bigr)u^au^bu^c = 0
$$

(the formula for $2\Gamma_{abc}$; each of the three terms in the bracket, after renaming the summed letters, equals the first sum, with the signs $+$, $+$, $-$, so together they are exactly the first sum). So a geodesic that starts time-like stays time-like with the same $g(u, u)$. For a time-like geodesic we choose the parameter so that $g(u, u) = -1$; then $\lambda$ is the **proper time** $\tau$ of the body, the time shown by a clock carried along (since $d\tau^2 = -ds^2$, Section 3.4).

**A conserved momentum.** Suppose the diagonal metric does not depend on one coordinate $x_k$ at all. Then the **momentum** $p_k = g_{kk}u^k$ (no sum) does not change along a geodesic. Line by line:

$$
\frac{dp_k}{d\lambda} = \sum_c (\partial_c\, g_{kk})\,u^c\,u^k + g_{kk}\,\frac{du^k}{d\lambda}
$$

(the product rule and the chain rule).

$$
\frac{du^k}{d\lambda} = -\sum_{b,c}\Gamma^k{}_{bc}u^bu^c = -2\sum_{c \ne k}\Gamma^k{}_{kc}\,u^ku^c
$$

(of the four cases of Section 3.15, case (a) $\Gamma^k{}_{kk} = \partial_k\ln h_k$ and case (c) $\Gamma^k{}_{bb} = -\tfrac12 g^{kk}\partial_k g_{bb}$ are zero because nothing depends on $x_k$, case (d) is zero, and case (b) appears twice, as $\Gamma^k{}_{kc}$ and $\Gamma^k{}_{ck}$)

$$
= -2\sum_{c \ne k}\frac{\partial_c\, g_{kk}}{2\,g_{kk}}\,u^ku^c = -\frac{1}{g_{kk}}\sum_c (\partial_c\, g_{kk})\,u^cu^k
$$

(case (b) written as $\tfrac12 g^{kk}\partial_c g_{kk}$; the term $c = k$ may be added because $\partial_k g_{kk} = 0$). Inserting the last line into the first, the two terms cancel: $dp_k/d\lambda = 0$. **A metric that does not depend on a coordinate conserves the momentum of that coordinate.** In the plane in polar coordinates the metric does not depend on $\varphi$, and $p_\varphi = r^2\,d\varphi/d\lambda$ is the angular momentum of mechanics; on the sphere $p_\varphi = a^2\sin^2\theta\,d\varphi/d\lambda$ is conserved.

**The geodesics of the sphere.** With the two symbols of Section 3.15 ($\Gamma^\theta{}_{\varphi\varphi} = -\sin\theta\cos\theta$ and $\Gamma^\varphi{}_{\theta\varphi} = \Gamma^\varphi{}_{\varphi\theta} = \cot\theta$) and the length $s$ along the curve as parameter,

$$
\frac{d^2\theta}{ds^2} = \sin\theta\cos\theta\Bigl(\frac{d\varphi}{ds}\Bigr)^2, \qquad \frac{d^2\varphi}{ds^2} = -2\cot\theta\,\frac{d\theta}{ds}\,\frac{d\varphi}{ds}
$$

(the geodesic equation for $a = \theta$ has the single term $\Gamma^\theta{}_{\varphi\varphi}(d\varphi/ds)^2$ moved to the right; for $a = \varphi$ the two equal terms $\Gamma^\varphi{}_{\theta\varphi}$ and $\Gamma^\varphi{}_{\varphi\theta}$ give the factor 2). The **equator** $\theta = \pi/2$, $\varphi = s/a$ is a geodesic: $d^2\theta/ds^2 = 0$ and $\sin(\pi/2)\cos(\pi/2) = 0$, and $d^2\varphi/ds^2 = 0$ with $d\theta/ds = 0$. A **circle of latitude** $\theta = \theta_0$ with $0 < \theta_0 < \pi/2$, run through at unit speed, is NOT a geodesic: along it $d^2\theta/ds^2 = 0$, while the right side is $\sin\theta_0\cos\theta_0\,(d\varphi/ds)^2 = \sin\theta_0\cos\theta_0/(a^2\sin^2\theta_0) = \cot\theta_0/a^2 \ne 0$ (unit speed means $a\sin\theta_0\,d\varphi/ds = 1$). For $a = 1$ and $\theta_0 = \pi/3$ the missing acceleration is $\cot(\pi/3) = 1/\sqrt3 = 0.577350$, the number Notebook 03c prints (In [11]). The geodesics of the sphere are its **great circles**, the circles whose centre is the centre of the sphere (the equator, the meridians and all their rotations); Notebook 03c shows this numerically for three of them (In [11]).

**Parallel transport around a circle of latitude.** Carry a vector once around the circle $\theta = \theta_0$, using $\varphi$ as the parameter (so $d\theta/d\varphi = 0$ and $d\varphi/d\varphi = 1$). The transport equation $dV^a/d\varphi + \sum_c\Gamma^a{}_{\varphi c}V^c = 0$ has one term for each component:

$$
\frac{dV^\theta}{d\varphi} = \sin\theta_0\cos\theta_0\,V^\varphi, \qquad \frac{dV^\varphi}{d\varphi} = -\cot\theta_0\,V^\theta
$$

(for $a = \theta$ the only symbol is $\Gamma^\theta{}_{\varphi\varphi}$, for $a = \varphi$ the only one is $\Gamma^\varphi{}_{\varphi\theta}$). Measure the vector with the unit vectors pointing south and east: its lengths along them are $u = aV^\theta$ and $w = a\sin\theta_0\,V^\varphi$ (the scale factors $h_\theta = a$, $h_\varphi = a\sin\theta_0$). Multiplying the two equations by $a$ and by $a\sin\theta_0$,

$$
\frac{du}{d\varphi} = \cos\theta_0\, w, \qquad \frac{dw}{d\varphi} = -\cos\theta_0\, u
$$

(in the first, $a\sin\theta_0\cos\theta_0V^\varphi = \cos\theta_0\,w$; in the second, $a\sin\theta_0\cot\theta_0V^\theta = \cos\theta_0\,u$). Start with the unit vector pointing south, $u = 1$, $w = 0$. The solution is

$$
u = \cos(\varphi\cos\theta_0), \qquad w = -\sin(\varphi\cos\theta_0)
$$

(check: $du/d\varphi = -\cos\theta_0\sin(\varphi\cos\theta_0) = \cos\theta_0\,w$ and $dw/d\varphi = -\cos\theta_0\cos(\varphi\cos\theta_0) = -\cos\theta_0\,u$, and at $\varphi = 0$ the values are $1$ and $0$; the solution with given starting values is unique, a standard theorem that we quote, ASSUMED). The length $\sqrt{u^2 + w^2} = 1$ never changes, and relative to the local south and east directions the vector turns at the constant rate $\cos\theta_0$. After one round, $\varphi = 2\pi$, it has turned by $-2\pi\cos\theta_0$, which is the same direction as a turn by $2\pi - 2\pi\cos\theta_0 = 2\pi(1 - \cos\theta_0)$ (two angles that differ by a whole turn $2\pi$ give the same direction). At $\theta_0 = \pi/3$, $\cos\theta_0 = 1/2$: $u = \cos\pi = -1$, $w = -\sin\pi = 0$. The vector comes back pointing north, exactly reversed. On the plane the same walk would return the vector unchanged.

**The turning angle is the enclosed area times the curvature.** The cap north of the circle has the area

$$
\int_0^{\theta_0}\!\!\int_0^{2\pi} a^2\sin\theta\;d\varphi\,d\theta = 2\pi a^2\int_0^{\theta_0}\sin\theta\,d\theta = 2\pi a^2\bigl[-\cos\theta\bigr]_0^{\theta_0} = 2\pi a^2(1 - \cos\theta_0)
$$

(the area factor $\sqrt{\det g} = a\cdot a\sin\theta$ of Section 3.6; the inner integral gives $2\pi$; an antiderivative of $\sin\theta$ is $-\cos\theta$; $\cos 0 = 1$). So the turning angle $2\pi(1 - \cos\theta_0)$ equals the enclosed area divided by $a^2$. Section 3.18 shows that $1/a^2$ is the curvature of the sphere. Notebook 03c measures the turning angle for 15 circles with RK4 and finds it equal to the area divided by $a^2$ within $5.0 \times 10^{-12}$ radians (In [10]).

### 3.17 Curvature: the Riemann tensor and its contractions

**The idea.** On a flat sheet a vector carried around a closed loop without turning comes back unchanged; on the sphere it comes back turned (Section 3.16). For a very small loop the turning is measured by the difference between taking two covariant derivatives in one order and in the other order. In flat Cartesian coordinates $\nabla_c\nabla_d = \partial_c\partial_d$, and partial derivatives can be taken in either order; in a curved space covariant derivatives cannot.

**Theorem (the Riemann tensor).** For every vector field $V$,

$$
\nabla_c\nabla_d V^a - \nabla_d\nabla_c V^a = \sum_b R^a{}_{bcd}\,V^b, \qquad R^a{}_{bcd} = \partial_c\Gamma^a{}_{bd} - \partial_d\Gamma^a{}_{bc} + \sum_e\bigl(\Gamma^a{}_{ce}\Gamma^e{}_{bd} - \Gamma^a{}_{de}\Gamma^e{}_{bc}\bigr).
$$

This is the convention of the textbook of Misner, Thorne and Wheeler (MTW), used by every Revision record (`Revision/gkd_lovelock/results/python-lovelock-report.json`, key `conventions.riemann`).

*Proof, line by line.* $\nabla_d V^a$ has one upper index $a$ and one lower index $d$, so by the rule of Section 3.15

$$
\nabla_c(\nabla_d V^a) = \partial_c(\nabla_d V^a) + \sum_e\Gamma^a{}_{ce}\,\nabla_d V^e - \sum_e\Gamma^e{}_{cd}\,\nabla_e V^a
$$

(one $+\Gamma$ for the upper index, one $-\Gamma$ for the lower index). Insert $\nabla_d V^a = \partial_d V^a + \sum_b\Gamma^a{}_{db}V^b$:

$$
= \partial_c\partial_d V^a + \sum_b(\partial_c\Gamma^a{}_{db})V^b + \sum_b\Gamma^a{}_{db}\,\partial_c V^b + \sum_e\Gamma^a{}_{ce}\,\partial_d V^e + \sum_{e,b}\Gamma^a{}_{ce}\Gamma^e{}_{db}V^b - \sum_e\Gamma^e{}_{cd}\,\nabla_e V^a
$$

(the product rule for $\partial_c(\Gamma V)$). Now subtract the same expression with $c$ and $d$ exchanged. Three kinds of terms drop out: $\partial_c\partial_d V^a$ (partial derivatives can be taken in either order); the pair $\sum_b\Gamma^a{}_{db}\partial_c V^b + \sum_e\Gamma^a{}_{ce}\partial_d V^e$, which after renaming $e$ to $b$ is unchanged by the exchange of $c$ and $d$; and $\sum_e\Gamma^e{}_{cd}\nabla_e V^a$ (no torsion: $\Gamma^e{}_{cd} = \Gamma^e{}_{dc}$). What remains is

$$
\sum_b\Bigl(\partial_c\Gamma^a{}_{db} - \partial_d\Gamma^a{}_{cb} + \sum_e\Gamma^a{}_{ce}\Gamma^e{}_{db} - \sum_e\Gamma^a{}_{de}\Gamma^e{}_{cb}\Bigr)V^b ,
$$

which is $\sum_b R^a{}_{bcd}V^b$ because $\Gamma^a{}_{db} = \Gamma^a{}_{bd}$, $\Gamma^a{}_{cb} = \Gamma^a{}_{bc}$, $\Gamma^e{}_{db} = \Gamma^e{}_{bd}$ and $\Gamma^e{}_{cb} = \Gamma^e{}_{bc}$. $\square$

The left side is a tensor for every $V$ and contains no derivative of $V$, so $R^a{}_{bcd}$ is a tensor (one upper, three lower indices). Hence: **if it is zero in one system of coordinates, it is zero in every system** (Section 3.14). A space whose Riemann tensor is zero everywhere is **flat**; conversely, near each point of a space with zero Riemann tensor there are coordinates in which the metric is constant (a standard theorem, quoted, ASSUMED).

**Symmetries.** (S1) $R^a{}_{bcd} = -R^a{}_{bdc}$: exchanging $c$ and $d$ in the formula exchanges the two derivative terms with a sign change, and so for the two products. (S2) The **first Bianchi identity** $R^a{}_{bcd} + R^a{}_{cdb} + R^a{}_{dbc} = 0$. Proof: write the three terms with the formula. The six derivative terms are $\partial_c\Gamma^a{}_{bd} - \partial_d\Gamma^a{}_{bc} + \partial_d\Gamma^a{}_{cb} - \partial_b\Gamma^a{}_{cd} + \partial_b\Gamma^a{}_{dc} - \partial_c\Gamma^a{}_{db}$; they cancel in pairs because the symbols are symmetric in their lower indices. The six products are $\Gamma^a{}_{ce}\Gamma^e{}_{bd} - \Gamma^a{}_{de}\Gamma^e{}_{bc} + \Gamma^a{}_{de}\Gamma^e{}_{cb} - \Gamma^a{}_{be}\Gamma^e{}_{cd} + \Gamma^a{}_{be}\Gamma^e{}_{dc} - \Gamma^a{}_{ce}\Gamma^e{}_{db}$ (summed over $e$); they cancel in pairs for the same reason. $\square$ Two more symmetries hold for every metric; we quote them (ASSUMED as general theorems; Notebook 03b checks both exactly for the author's metric, In [14]): with the first index lowered, $R_{abcd} = \sum_e g_{ae}R^e{}_{bcd}$, (S3) $R_{abcd} = -R_{bacd}$ and (S4) $R_{abcd} = R_{cdab}$ (pair symmetry).

**The form with two upper indices.** The Revision records store the tensor as

$$
R^{ab}{}_{cd} = \sum_e g^{be}R^a{}_{ecd},
$$

which for a diagonal metric is $g^{bb}R^a{}_{bcd}$ (no sum). By (S1) and (S3) it is antisymmetric in $a, b$ and in $c, d$; with all indices down, for a diagonal metric, $R_{abcd} = g_{aa}g_{bb}R^{ab}{}_{cd}$ (no sum). For two different coordinates $x_a$ and $x_b$ the number

$$
\sigma(a, b) = R^{ab}{}_{ab} \quad\text{(no sum)}
$$

is the **curvature of the coordinate plane** of $x_a$ and $x_b$ (its **sectional curvature**; "plane" means here the plane of the two directions $x_a$ and $x_b$ at one point). We write it with the Greek letter $\sigma$ (sigma), because the letter $K$ is kept for the Kretschmann scalar below. What its sign means depends on the kind of directions:

- **Two space-like directions.** Then every step in the plane has a positive squared length, as on an ordinary surface, and $\sigma(a, b)$ is read like the curvature of a surface: positive for a plane curved like a sphere, negative for one curved like a saddle, zero for a flat one. Section 3.18 makes this precise: geodesics that start parallel in such a plane approach each other when $\sigma > 0$ and separate when $\sigma < 0$.
- **One space-like and one time-like direction.** There is no shape of this kind to picture. The sign is read from free fall instead: for two neighbouring free-fall paths that run along the time-like direction, the positive sign means that they accelerate APART, the opposite of the sphere. Section 3.18 states the rule and Section 3.24 verifies it by hand in the author's metric.
- **Two time-like directions.** Every step in the plane has a negative squared length. Replace $g$ by $-g$: the Christoffel symbols do not change (both factors of $\tfrac12 g^{ad}(\partial g + \partial g - \partial g)$ change sign), so $R^a{}_{bcd}$ does not change, but every $g^{bb}$ changes sign, so $\sigma(a, b) = g^{bb}R^a{}_{bab}$ (diagonal metric) changes sign. With $-g$ the plane has positive squared lengths, so its shape is that of the curvature $-\sigma(a, b)$: here a negative $\sigma$ means curved like a sphere, the reverse of the first case. The free-fall reading of the second case still holds, because free-fall paths along a time-like direction are involved.

By the two antisymmetries, $R^{ba}{}_{ba} = R^{ab}{}_{ab}$ and $R^{ab}{}_{ba} = R^{ba}{}_{ab} = -R^{ab}{}_{ab}$.

**Contractions.** The **Ricci tensor**, the **Ricci scalar**, the **Einstein tensor** and the **Kretschmann scalar** are

$$
R^a{}_b = \sum_c R^{ac}{}_{bc}, \qquad R = \sum_a R^a{}_a, \qquad G^a{}_b = R^a{}_b - \tfrac12\,\delta^a{}_b\,R, \qquad K = \sum_{a,b,c,d} R^{ab}{}_{cd}\,R^{cd}{}_{ab} .
$$

$R$ and $K$ have every index contracted: they are invariants, the same in every system of coordinates (Section 3.14). The Einstein tensor is the combination that enters Einstein's field equations (Section 3.26). Two consequences for the diagonal entries are used again and again:

$$
R^a{}_a = \sum_c R^{ac}{}_{ac} = \sum_{c \ne a} \sigma(a, c)
$$

(the definition with $b = a$; the term $c = a$ is $R^{aa}{}_{aa} = 0$ by the antisymmetry in the upper pair): **each diagonal entry of the Ricci tensor is the sum of the curvatures of the $n - 1$ coordinate planes that contain that direction**; and

$$
R = \sum_a\sum_{c \ne a} \sigma(a, c) = 2\sum_{a < c} \sigma(a, c)
$$

(every plane is counted twice, once as $(a, c)$ and once as $(c, a)$, with $\sigma(c, a) = \sigma(a, c)$).

**A surface.** A space of two dimensions has a single coordinate plane, and its curvature $\sigma(1, 2)$ is the **Gaussian curvature**. Then $R^1{}_1 = R^2{}_2 = \sigma(1, 2)$ and $R = 2\sigma(1, 2)$. The non-zero components $R^{ab}{}_{cd}$ are the four $R^{12}{}_{12} = R^{21}{}_{21} = \sigma(1, 2)$ and $R^{12}{}_{21} = R^{21}{}_{12} = -\sigma(1, 2)$, so the Kretschmann scalar is $K = 4\sigma(1, 2)^2$ (each of the four products $R^{ab}{}_{cd}R^{cd}{}_{ab}$ is $\sigma(1,2)^2$).

### 3.18 The curvature of the plane and of the sphere, by hand; geodesic deviation

**The plane in polar coordinates is flat.** With the symbols of Section 3.15:

$$
R^r{}_{\varphi r\varphi} = \partial_r\Gamma^r{}_{\varphi\varphi} - \partial_\varphi\Gamma^r{}_{\varphi r} + \sum_e\bigl(\Gamma^r{}_{re}\Gamma^e{}_{\varphi\varphi} - \Gamma^r{}_{\varphi e}\Gamma^e{}_{\varphi r}\bigr)
$$

(the formula with $a = r$, $b = \varphi$, $c = r$, $d = \varphi$)

$$
= \partial_r(-r) - 0 + 0 - \Gamma^r{}_{\varphi\varphi}\Gamma^\varphi{}_{\varphi r} = -1 - (-r)\cdot\frac1r = 0
$$

($\Gamma^r{}_{\varphi r} = 0$; every $\Gamma^r{}_{re}$ is zero; in the last sum only $e = \varphi$ survives). In two dimensions this is the only independent component, so the Riemann tensor of the plane is zero, although its polar Christoffel symbols are not. **Christoffel symbols describe the coordinates; the Riemann tensor describes the space.**

**The sphere of radius $a$.**

$$
R^\theta{}_{\varphi\theta\varphi} = \partial_\theta\Gamma^\theta{}_{\varphi\varphi} - \partial_\varphi\Gamma^\theta{}_{\varphi\theta} + \sum_e\bigl(\Gamma^\theta{}_{\theta e}\Gamma^e{}_{\varphi\varphi} - \Gamma^\theta{}_{\varphi e}\Gamma^e{}_{\varphi\theta}\bigr)
$$

(the formula with $a = \theta$, $b = \varphi$, $c = \theta$, $d = \varphi$)

$$
= \partial_\theta(-\sin\theta\cos\theta) - 0 + 0 - \Gamma^\theta{}_{\varphi\varphi}\Gamma^\varphi{}_{\varphi\theta} = -(\cos^2\theta - \sin^2\theta) - (-\sin\theta\cos\theta)\cot\theta
$$

(the product rule: the derivative of $\sin\theta\cos\theta$ is $\cos^2\theta - \sin^2\theta$; $\Gamma^\theta{}_{\varphi\theta} = 0$ and every $\Gamma^\theta{}_{\theta e} = 0$; in the last sum only $e = \varphi$ survives)

$$
= -\cos^2\theta + \sin^2\theta + \cos^2\theta = \sin^2\theta
$$

($\sin\theta\cos\theta\cot\theta = \cos^2\theta$). Raising the second index,

$$
\sigma(\theta, \varphi) = R^{\theta\varphi}{}_{\theta\varphi} = g^{\varphi\varphi}R^\theta{}_{\varphi\theta\varphi} = \frac{\sin^2\theta}{a^2\sin^2\theta} = \frac{1}{a^2}
$$

(Section 3.17; $g^{\varphi\varphi} = 1/(a^2\sin^2\theta)$). The Gaussian curvature of the sphere is $1/a^2$ at every point: a small sphere is strongly curved, a large one weakly. By Section 3.17, $R^\theta{}_\theta = R^\varphi{}_\varphi = 1/a^2$, the Ricci scalar is $R = 2/a^2$, and the Kretschmann scalar is $K = 4/a^4$. All PROVED here and computed exactly by Notebook 03c (In [7]). With Section 3.16: the turning angle $2\pi(1 - \cos\theta_0)$ of a vector carried around a circle of latitude is the enclosed area $2\pi a^2(1 - \cos\theta_0)$ times the Gaussian curvature $1/a^2$.

**Geodesic deviation.** Two meridians cross the equator at right angles, so they start out parallel. On a plane, lines that start parallel keep their distance for ever. On the sphere, after the length $s$ along the meridians from the equator ($\theta = \pi/2 - s/a$), two meridians a small angle $\Delta\varphi$ apart are separated along the circle of latitude by

$$
\xi(s) = a\sin\theta\,\Delta\varphi = a\sin\Bigl(\frac\pi2 - \frac sa\Bigr)\Delta\varphi = a\cos\Bigl(\frac sa\Bigr)\Delta\varphi
$$

(the length of an arc of the circle of latitude, whose radius is $a\sin\theta$; $\sin(\pi/2 - x) = \cos x$). Differentiating twice with respect to $s$,

$$
\frac{d^2\xi}{ds^2} = -\frac{1}{a^2}\,a\cos\Bigl(\frac sa\Bigr)\Delta\varphi = -\frac{1}{a^2}\,\xi
$$

(the chain rule: each derivative of $\cos(s/a)$ brings a factor $1/a$ and turns $\cos$ into $-\sin$ and $\sin$ into $\cos$). The distance shrinks, and it is zero at $s = \pi a/2$: the meridians meet at the pole. In general the distance $\xi(s)$ between two neighbouring geodesics of a surface obeys the **geodesic deviation equation** $d^2\xi/ds^2 = -\sigma\,\xi$ with the Gaussian curvature $\sigma = \sigma(1, 2)$ of Section 3.17 (a standard theorem, quoted, ASSUMED; on the sphere we have just verified it, with $\sigma = 1/a^2$). On a surface, where all lengths are positive, positive curvature focuses neighbouring geodesics, negative curvature drives them apart, zero curvature does neither. In a spacetime the same theorem also covers free-fall paths that run along a time-like direction (the paths of observers, with their proper time $\tau$ in place of the length $s$), and for them the sign is reversed: if two such paths are a small proper distance $\xi$ apart along the other direction of a coordinate plane with the curvature $\sigma$, then $d^2\xi/d\tau^2 = +\sigma\,\xi$ (quoted, ASSUMED in general; the reversal comes from the negative squared length of a time-like step). There a positive curvature drives the paths apart. Section 3.24 verifies this by hand for the observers at rest in the author's metric. Notebook 03c solves the equation with RK4 and finds it equal to the exact distance of two meridians within $8.0 \times 10^{-14}$ (In [13]).

### 3.19 Example: curvature where it can be pictured

Notebook 03c applies Sections 3.14 to 3.18 to the plane and the sphere. It defines general functions that compute the Christoffel symbols, the Riemann tensor, the tensor with two upper indices, the Ricci tensor and the Kretschmann scalar of any metric given as a sympy matrix; these are the same formulas that Notebook 03b later applies to the author's metric. It computes the polar Christoffel symbols of the plane and finds its Riemann tensor zero; checks that the constant field $e_x$ has zero covariant derivative; computes the curvature $1/a^2$, the Ricci scalar $2/a^2$ and the Kretschmann scalar $4/a^4$ of the sphere; carries a vector around circles of latitude with RK4 and compares the turning angle with the enclosed area; integrates three geodesics and finds great circles; and solves the geodesic deviation equation. It reads no Revision record (everything is exact mathematics), needs no Rust, runs in about 15 seconds and ends with the line ALL 16 CHECKS PASSED (notebook 03c).

<!-- NOTEBOOK 03c -->

### 3.22 Line-by-line walk-through of Notebook 03c

The notebook has 14 code cells, In [1] to In [14]. As in Section 3.13, a line or a small group of lines is quoted and then explained, and a line `...` in a quoted figure command stands for the remaining lines of the caption, which is printed in full under its figure in Section 3.21.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 3.20. Its code is, line for line, the set-up code of Notebook 03a explained in Section 3.13 under In [1], with the single difference `NOTEBOOK_ID = "03c"  # this notebook: chapter 03, example c`, so that the figures are named `03c_<k>_<name>.png` and the captions file is `Revision/textbook/figures/03c.captions.json`. It prints one line, Set-up of notebook 03c complete: repository folder found, helpers defined.

**In [2], every result in one piece.** The cell is, word for word, In [2] of Notebook 03a, explained in Section 3.13: it defines `in_one_piece` and replaces `check` and `report` by functions that write each of their results with one call of `sys.stdout.write`. It prints From now on check and report print each of their results in one piece.

**In [3], the curvature machinery for any metric.**

```python
import itertools  # loops over all index combinations

import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols
```

`itertools` is a module of Python with tools for loops; its function `product` runs through all combinations of indices. numpy (arrays of numbers) and sympy (exact algebra) are loaded under their usual short names.

```python
def christoffel(metric, coordinates):
    """All Christoffel symbols table[a][b][c] of a metric."""
    n = len(coordinates)
    inverse = metric.inv()
    d_metric = [metric.diff(c) for c in coordinates]  # d_metric[c][i, j] = d_c g_ij
    table = [[[0] * n for _ in range(n)] for _ in range(n)]
```

The function receives the metric as a sympy matrix and the list of its coordinates. `n` is the dimension (`len` counts the list). `metric.inv()` is the inverse matrix $g^{ab}$. `metric.diff(c)` differentiates every entry with respect to the coordinate `c`; the list `d_metric` holds one such matrix per coordinate, so `d_metric[c][i, j]` is $\partial_c\, g_{ij}$. `table` is a list of $n$ lists of $n$ lists of $n$ zeros, the empty table $\Gamma^a{}_{bc}$ (the name `_` is used for a loop counter that is not needed).

```python
    for a, b, c in itertools.product(range(n), repeat=3):
        table[a][b][c] = sp.simplify(sum(
            inverse[a, d] * (d_metric[b][d, c] + d_metric[c][d, b]
                             - d_metric[d][b, c]) for d in range(n)) / 2)
    return table
```

`itertools.product(range(n), repeat=3)` gives every list of three indices $(a, b, c)$, $n^3$ of them. For each, the formula of Section 3.15 is applied literally: the sum over $d$ of $g^{ad}(\partial_b\, g_{dc} + \partial_c\, g_{db} - \partial_d\, g_{bc})$, divided by 2 and simplified by `sp.simplify`. The finished table is returned.

```python
def riemann(table, coordinates):
    """The non-zero R^a_bcd (MTW convention) as a dictionary."""
    n = len(coordinates)
    result = {}
    for a, b, c, d in itertools.product(range(n), repeat=4):
        value = sp.simplify(
            sp.diff(table[a][b][d], coordinates[c])
            - sp.diff(table[a][b][c], coordinates[d])
            + sum(table[a][c][e] * table[e][b][d] - table[a][d][e] * table[e][b][c]
                  for e in range(n)))
        if value != 0:
            result[(a, b, c, d)] = value
    return result
```

For every list of four indices the formula of Section 3.17 is applied literally: $\partial_c\Gamma^a{}_{bd} - \partial_d\Gamma^a{}_{bc} + \sum_e(\Gamma^a{}_{ce}\Gamma^e{}_{bd} - \Gamma^a{}_{de}\Gamma^e{}_{bc})$, simplified. Only the components that are not zero are kept, in a **dictionary** whose keys are the index lists `(a, b, c, d)`; the zero ones are simply absent.

```python
def raise_second(riemann_table, metric):
    """The non-zero R^ab_cd = sum over e of g^(be) R^a_ecd."""
    inverse = metric.inv()
    result = {}
    for (a, e, c, d), value in riemann_table.items():
        for b in range(metric.rows):
            result[(a, b, c, d)] = result.get((a, b, c, d), 0) + inverse[b, e] * value
    return {k: sp.simplify(v) for k, v in result.items() if sp.simplify(v) != 0}
```

This raises the second index, $R^{ab}{}_{cd} = \sum_e g^{be}R^a{}_{ecd}$. `items()` hands out every key with its value; writing the key as `(a, e, c, d)` gives the four indices names. For each $b$ the product $g^{be}R^a{}_{ecd}$ is added to the entry `(a, b, c, d)`; `result.get(key, 0)` is the value collected so far, or 0 if there is none yet. The last line is a **dictionary comprehension**: it builds a new dictionary from the simplified values and keeps only those that are not zero.

```python
def ricci(mixed_table, n):
    """R^a_b = sum over c of R^ac_bc."""
    result = sp.zeros(n, n)
    for (a, c, b, d), value in mixed_table.items():
        if c == d:
            result[a, b] += value
    return result.applyfunc(sp.simplify)
```

The Ricci tensor $R^a{}_b = \sum_c R^{ac}{}_{bc}$ of Section 3.17. The key of the table is read as $(a, c, b, d)$: upper indices $a, c$ and lower indices $b, d$; a component contributes to $R^a{}_b$ exactly when its second upper index equals its second lower index, $c = d$. `+=` adds to the entry. Every entry of the result is simplified.

```python
def kretschmann(mixed_table):
    """K = sum of R^ab_cd R^cd_ab."""
    return sp.simplify(sum(v * mixed_table.get((c, d, a, b), 0)
                           for (a, b, c, d), v in mixed_table.items()))


say("Defined: christoffel, riemann, raise_second, ricci, kretschmann.")
```

The Kretschmann scalar $K = \sum R^{ab}{}_{cd}R^{cd}{}_{ab}$: each stored component is multiplied by its partner with the two pairs exchanged (0 if the partner is absent), and everything is summed. The last line prints the output of In [3].

**In [4], the flat plane in polar coordinates.**

```python
r, phi = sp.symbols("r varphi", positive=True)  # polar coordinates, r > 0
plane = sp.diag(1, r ** 2)  # ds^2 = dr^2 + r^2 dphi^2
POLAR = [r, phi]
POLAR_NAMES = ["r", "phi"]
plane_gamma = christoffel(plane, POLAR)
```

Two positive symbols, the distance $r$ and the angle $\varphi$ (sympy's name for it is `varphi`). `sp.diag(1, r ** 2)` is the metric $\mathrm{diag}(1, r^2)$ of Section 3.3. `POLAR` is the list of the coordinates and `POLAR_NAMES` their names for printing. The last line computes all $2^3 = 8$ Christoffel symbols.

```python
for a, b, c in itertools.product(range(2), repeat=3):
    if plane_gamma[a][b][c] != 0:
        say(f"  Gamma^{POLAR_NAMES[a]}_({POLAR_NAMES[b]} {POLAR_NAMES[c]}) = "
            f"{plane_gamma[a][b][c]}")
check(plane_gamma[0][1][1] == -r and plane_gamma[1][0][1] == 1 / r
      and plane_gamma[1][1][0] == 1 / r,
      "plane in polar coordinates: Gamma^r_(phi phi) = -r, Gamma^phi_(r phi) = 1/r")
```

The loop prints the symbols that are not zero: the output shows $\Gamma^r{}_{\varphi\varphi} = -r$ and $\Gamma^\varphi{}_{r\varphi} = \Gamma^\varphi{}_{\varphi r} = 1/r$, the values found by hand in Section 3.15. Position 0 is $r$ and position 1 is $\varphi$, so `plane_gamma[0][1][1]` is $\Gamma^r{}_{\varphi\varphi}$. The check confirms the three values.

```python
plane_riemann = riemann(plane_gamma, POLAR)
say(f"non-zero Riemann components of the plane: {len(plane_riemann)}")
check(plane_riemann == {},
      "the Riemann tensor of the plane is zero: the plane is flat")
```

The Riemann tensor of the plane has no non-zero component: the output prints 0 and the check requires the empty dictionary `{}` (Section 3.18).

**In [5], the constant field has zero covariant derivative.**

```python
V = [sp.cos(phi), -sp.sin(phi) / r]  # the constant field e_x in polar components
nabla = [[sp.simplify(sp.diff(V[a], POLAR[b])
                      + sum(plane_gamma[a][b][c] * V[c] for c in range(2)))
          for b in range(2)] for a in range(2)]
say(f"covariant derivative of e_x: {nabla}")
check(nabla == [[0, 0], [0, 0]],
      "the covariant derivative of the constant field e_x is zero")
```

`V` holds the polar components of $e_x$ found in Section 3.14. The nested list comprehension computes $\nabla_b V^a = \partial_b V^a + \sum_c\Gamma^a{}_{bc}V^c$ for $a = 0, 1$ (outer list) and $b = 0, 1$ (inner list), exactly the four lines of Section 3.15. The output prints `[[0, 0], [0, 0]]` and the check requires it.

**In [6], Figure 03c.1.**

```python
BLUE, ORANGE, AQUA, RED, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#e34948", "#4a3aa7"
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6))
fig.subplots_adjust(wspace=0.3)  # room for the label of the right vertical axis
ax = axes[0]
angles = np.linspace(0.0, 2 * np.pi, 400)
```

Five colours of the palette of Section 3.13 (In [9] of Notebook 03a). A figure with two panels side by side; `subplots_adjust(wspace=0.3)` widens the gap between them. `ax` names the left panel. `angles` holds 400 angles from $0$ to $2\pi$.

```python
for radius in (0.5, 1.0, 1.5, 2.0):  # circles of constant r
    ax.plot(radius * np.cos(angles), radius * np.sin(angles), color="grey", lw=0.6)
for ray in np.arange(12) * np.pi / 6:  # rays of constant phi
    ax.plot([0, 2.2 * np.cos(ray)], [0, 2.2 * np.sin(ray)], color="grey", lw=0.6)
```

The polar grid: four grey circles of constant $r$ (a circle is the curve $(r\cos\varphi, r\sin\varphi)$), and twelve grey rays of constant $\varphi$, one every $\pi/6$ (`np.arange(12)` is $0, 1, \dots, 11$), each a straight segment from the origin to the distance $2.2$.

```python
points = np.arange(12) * np.pi / 6 + np.pi / 12  # the angles of the 12 points
px, py = 1.5 * np.cos(points), 1.5 * np.sin(points)
ax.quiver(px, py, np.ones(12), np.zeros(12), color="black", scale=8, width=0.006,
          label="constant field $e_x$")
ax.quiver(px, py, np.cos(points), np.sin(points), color=RED, scale=12,
          width=0.005, label="unit vector $e_r$")
ax.quiver(px, py, -np.sin(points), np.cos(points), color=BLUE, scale=12,
          width=0.005, label="unit vector $e_\\varphi / r$")
```

Twelve points on the circle $r = 1.5$, halfway between the rays. `ax.quiver(x, y, dx, dy, ...)` draws an arrow at each point $(x, y)$ in the direction $(dx, dy)$; `scale` sets how long the arrows are drawn (a larger scale gives shorter arrows) and `width` their thickness. Black: the constant field, $(1, 0)$ everywhere. Red: the unit vector $e_r = (\cos\varphi, \sin\varphi)$, pointing away from the origin. Blue: the unit vector $e_\varphi/r = (-\sin\varphi, \cos\varphi)$, pointing around the circle.

```python
ax.set_aspect("equal")
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.4, 2.4)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("A constant field on the polar grid")
ax.legend(fontsize=7, loc="lower left")
```

Equal units on both axes (so circles look round), the ranges of both axes, their labels, the title and the legend in the lower left corner.

```python
ax = axes[1]
ax.plot(angles, np.cos(angles), color=RED, lw=1.8,
        label="component along $e_r$: $\\cos\\varphi$")
ax.plot(angles, -np.sin(angles), color=BLUE, lw=1.8, ls="--",
        label="component along $e_\\varphi/r$: $-\\sin\\varphi$")
ax.set_xlabel("$\\varphi$ (radians)")
ax.set_ylabel("component (no unit)")
ax.set_title("Its polar components change")
ax.legend(fontsize=8, loc="lower left")
```

The right panel: the components of $e_x$ along the two unit vectors, $\cos\varphi$ (solid) and $-\sin\varphi$ (dashed), against $\varphi$. (Along the unit vector $e_\varphi/r$ the component is $r V^\varphi = -\sin\varphi$.)

```python
save_figure(fig, "plane_polar_components",
            "The flat plane in polar coordinates. Left: the polar grid (grey circles "
...
check(np.allclose(np.cos(points) ** 2 + np.sin(points) ** 2, 1.0),
      "the components of the unit field e_x have length 1 at every point")
```

The figure is saved with its caption. The check is a simple consistency test of the drawing: at each of the twelve points the two components $\cos\varphi$ and $-\sin\varphi$ of the unit field $e_x$ along the two perpendicular unit vectors give the length $\sqrt{\cos^2\varphi + \sin^2\varphi} = 1$ (`np.allclose` compares arrays up to rounding).

**What Figure 03c.1 shows.** Left: all twelve black arrows are equal, while the red and blue unit vectors at the same points turn as one goes around the circle. Right: the two components of the constant field oscillate between $-1$ and $1$ as $\varphi$ runs once around. A derivative that only looked at components would call this field changing; the covariant derivative, with the Christoffel symbols, correctly says it does not change.

**In [7], the sphere of radius $a$.**

```python
theta = sp.symbols("theta", positive=True)
a = sp.symbols("a", positive=True)  # the radius of the sphere
sphere = sp.diag(a ** 2, a ** 2 * sp.sin(theta) ** 2)
ANGLES = [theta, phi]
ANGLE_NAMES = ["theta", "phi"]
sphere_gamma = christoffel(sphere, ANGLES)
```

The angle $\theta$ and the radius $a$ as positive symbols; the metric $\mathrm{diag}(a^2, a^2\sin^2\theta)$ of Section 3.3; the coordinates $(\theta, \varphi)$ (the symbol $\varphi$ of In [4] is reused) and their names; all eight Christoffel symbols.

```python
for i, j, k in itertools.product(range(2), repeat=3):
    if sphere_gamma[i][j][k] != 0:
        say(f"  Gamma^{ANGLE_NAMES[i]}_({ANGLE_NAMES[j]} {ANGLE_NAMES[k]}) = "
            f"{sphere_gamma[i][j][k]}")
sphere_riemann = riemann(sphere_gamma, ANGLES)
sphere_mixed = raise_second(sphere_riemann, sphere)
```

The loop prints the non-zero symbols. sympy writes $\Gamma^\theta{}_{\varphi\varphi} = -\sin\theta\cos\theta$ as `-sin(2*theta)/2`, the same number because $\sin 2\theta = 2\sin\theta\cos\theta$, and $\cot\theta$ as `1/tan(theta)`. Then the Riemann tensor and its form with two upper indices.

```python
for key, value in sorted(sphere_mixed.items()):
    say(f"  R^({ANGLE_NAMES[key[0]]} {ANGLE_NAMES[key[1]]})_"
        f"({ANGLE_NAMES[key[2]]} {ANGLE_NAMES[key[3]]}) = {value}")
sphere_ricci = ricci(sphere_mixed, 2)
sphere_R = sp.simplify(sphere_ricci.trace())
sphere_K = kretschmann(sphere_mixed)
say(f"Ricci tensor R^a_b = {sphere_ricci.tolist()}")
say(f"Ricci scalar R = {sphere_R},  Kretschmann scalar K = {sphere_K}")
```

`sorted` puts the components in a fixed order (by their index lists) before printing; `key[0]` to `key[3]` are the four indices. The output shows the four components of a surface (Section 3.17): $R^{\theta\varphi}{}_{\theta\varphi} = R^{\varphi\theta}{}_{\varphi\theta} = 1/a^2$ (written `a**(-2)`) and $R^{\theta\varphi}{}_{\varphi\theta} = R^{\varphi\theta}{}_{\theta\varphi} = -1/a^2$. `trace()` is the sum of the diagonal entries of the Ricci matrix, the Ricci scalar; `tolist()` writes a matrix as a list of rows for printing. The output: $R^a{}_b = \mathrm{diag}(1/a^2, 1/a^2)$, $R = 2/a^2$, $K = 4/a^4$.

```python
check(sp.simplify(sphere_gamma[0][1][1] + sp.sin(theta) * sp.cos(theta)) == 0
      and sp.simplify(sphere_gamma[1][0][1] - sp.cot(theta)) == 0,
      "sphere: Gamma^theta_(phi phi) = -sin cos, Gamma^phi_(theta phi) = cot theta")
check(sphere_mixed[(0, 1, 0, 1)] == 1 / a ** 2,
      "the Gaussian curvature of the sphere is 1/a^2 at every point")
check(sphere_R == 2 / a ** 2 and sphere_K == 4 / a ** 4,
      "Ricci scalar 2/a^2 and Kretschmann scalar 4/a^4")
```

Three checks of Section 3.18: the two Christoffel symbols found by hand (the difference with the hand result simplifies to zero), the Gaussian curvature $R^{\theta\varphi}{}_{\theta\varphi} = 1/a^2$ (key `(0, 1, 0, 1)`), and $R = 2/a^2$, $K = 4/a^4$.

**In [8], parallel transport around a circle of latitude.**

```python
def rk4(f, y0, t0, t1, steps):
    """Solve dy/dt = f(t, y) from t0 to t1 with the classical Runge-Kutta method in
    steps equal steps; return the times and the states (one row per time)."""
    h = (t1 - t0) / steps
    times = t0 + h * np.arange(steps + 1)
    states = np.zeros((steps + 1, len(y0)))
    states[0] = y0
```

The RK4 method of Chapter 2 for a system $dy/dt = f(t, y)$ of several equations. `h` is the step; `times` holds the $steps + 1$ times $t_0, t_0 + h, \dots, t_1$; `states` is a table with one row per time and one column per unknown, filled with zeros; its first row is the starting state `y0`.

```python
    for n in range(steps):
        t, y = times[n], states[n]
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h / 2 * k1)
        k3 = f(t + h / 2, y + h / 2 * k2)
        k4 = f(t + h, y + h * k3)
        states[n + 1] = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return times, states
```

One RK4 step per pass: four evaluations of the right side (at the start, twice at the middle, at the end of the step) and the weighted average $(k_1 + 2k_2 + 2k_3 + k_4)/6$ times $h$ added to the state. The function returns the times and the table of states.

```python
def transport(theta0, steps=2000):
    """Parallel transport of the unit south vector once around latitude theta0
    (a = 1): the components V^theta, V^phi as functions of phi."""
    def f(t, y):
        return np.array([np.sin(theta0) * np.cos(theta0) * y[1],
                         -np.cos(theta0) / np.sin(theta0) * y[0]])
    return rk4(f, np.array([1.0, 0.0]), 0.0, 2 * np.pi, steps)
```

The transport equations of Section 3.16 with $a = 1$: the state is $y = (V^\theta, V^\varphi)$, and `f` returns $(\sin\theta_0\cos\theta_0\,V^\varphi,\ -\cot\theta_0\,V^\theta)$. The parameter is $\varphi$, from $0$ to $2\pi$ in 2000 steps (the default value of `steps`). The start $(1, 0)$ is the unit vector pointing south ($u = aV^\theta = 1$, $w = 0$).

```python
def turning_angle(theta0):
    """The angle (0 to 2 pi) by which the vector comes back turned."""
    _, states = transport(theta0)
    u, w = states[-1, 0], np.sin(theta0) * states[-1, 1]  # lengths south, east
    return np.mod(np.arctan2(w, u), 2 * np.pi)
```

After one round (the last row, `states[-1]`) the lengths along south and east are $u = V^\theta$ and $w = \sin\theta_0\,V^\varphi$ (with $a = 1$). `np.arctan2(w, u)` is the angle of the arrow $(u, w)$ measured from the south direction towards the east, between $-\pi$ and $\pi$; `np.mod(..., 2 * np.pi)` adds $2\pi$ to a negative angle, so the result lies between $0$ and $2\pi$.

```python
theta0 = np.pi / 3
phis, states = transport(theta0)
lengths = np.sqrt(states[:, 0] ** 2 + (np.sin(theta0) * states[:, 1]) ** 2)
# round to 12 digits; adding 0.0 turns a rounded -0.0 into 0.0
say(f"start: V = {(states[0].round(12) + 0.0).tolist()},  end: V = "
    f"{(states[-1].round(12) + 0.0).tolist()}")
```

The transport around $\theta_0 = \pi/3$. `lengths` holds $\sqrt{u^2 + w^2}$ at all 2001 points (`states[:, 0]` is the first column, all rows). The start and end vectors are printed rounded to 12 digits; a tiny negative number rounds to $-0.0$, which would print as `-0.0`, and adding $0.0$ turns it into $0.0$. The output: start $[1.0, 0.0]$, end $[-1.0, 0.0]$.

```python
check(np.max(np.abs(lengths - 1.0)) < 1e-12,
      "parallel transport keeps the length of the vector")
check(np.max(np.abs(states[-1] - np.array([-1.0, 0.0]))) < 1e-10,
      "at theta0 = pi/3 the vector comes back exactly reversed")
```

Two checks: the length stays $1$ within $10^{-12}$ at every point, and the vector comes back reversed within $10^{-10}$, as derived in Section 3.16.

**In [9], Figure 03c.2: the transport drawn on the sphere.**

```python
def point(th, ph):
    """The point of the unit sphere at the angles th, ph."""
    return np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
```

The point $(\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$ of the unit sphere, as an array of its three coordinates $X$, $Y$, $Z$.

```python
def wire_sphere(ax):
    """Draw a light wire model of the unit sphere into the 3-D axes ax."""
    th, ph = np.meshgrid(np.linspace(0, np.pi, 13), np.linspace(0, 2 * np.pi, 25))
    ax.plot_wireframe(np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th),
                      color="grey", lw=0.3)
    ax.set_box_aspect((1, 1, 1), zoom=0.9)  # a little smaller: the labels fit
```

A helper that draws the sphere as a grey net of 13 circles of latitude and 25 meridians: `np.meshgrid` makes the grid of angles, and `plot_wireframe` connects the corresponding points. `set_box_aspect((1, 1, 1), zoom=0.9)` makes the three axes equally long and the box a little smaller, so that the labels fit in the picture.

```python
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.view_init(elev=25, azim=-60)
    for set_ticks in (ax.set_xticks, ax.set_yticks, ax.set_zticks):
        set_ticks([-1.0, 0.0, 1.0])  # three ticks per axis: labels do not overlap
    ax.tick_params(labelsize=8)
    ax.set_xlabel("$X$")
    ax.set_ylabel("$Y$")
    ax.set_zlabel("$Z$")
```

The ranges of the three axes; the point of view (25 degrees above the equator, turned by $-60$ degrees around the vertical axis); three tick marks per axis (the loop calls each of the three tick functions in turn); small tick labels; the axis names.

```python
fig = plt.figure(figsize=(6.4, 6.0))
ax = fig.add_subplot(projection="3d")
wire_sphere(ax)
circle = np.array([point(theta0, p) for p in np.linspace(0, 2 * np.pi, 200)])
ax.plot(circle[:, 0], circle[:, 1], circle[:, 2], color=VIOLET, lw=1.8)
```

A figure with one three-dimensional drawing area (`projection="3d"`), the wire sphere, and the circle of latitude $\theta_0 = \pi/3$ as 200 points joined by a violet line.

```python
for n in range(0, 2001, 125):  # 17 points, the last one equal to the first
    ph = phis[n]
    u, w = states[n, 0], np.sin(theta0) * states[n, 1]
    e_theta = np.array([np.cos(theta0) * np.cos(ph), np.cos(theta0) * np.sin(ph),
                        -np.sin(theta0)])
    e_phi = np.array([-np.sin(ph), np.cos(ph), 0.0])
```

`range(0, 2001, 125)` gives $n = 0, 125, \dots, 2000$: 17 steps of the transport, one every $2\pi \cdot 125/2000 = \pi/8$. At each, `ph` is the angle and $u$, $w$ the lengths south and east. `e_theta` is the unit vector pointing south at that point (the derivative of the point with respect to $\theta$), and `e_phi` the unit vector pointing east (the derivative with respect to $\varphi$, divided by $\sin\theta_0$).

```python
    arrow = 0.35 * (u * e_theta + w * e_phi)
    start = point(theta0, ph)
    colour = RED if n in (0, 2000) else BLUE
    ax.quiver(*start, *arrow, color=colour, lw=1.5, arrow_length_ratio=0.25)
ax.set_title("Parallel transport around the latitude $\\theta_0 = \\pi/3$")
```

The transported vector in three dimensions, $u\,e_\theta + w\,e_\varphi$, shortened to 0.35 for the drawing. It is drawn at its point on the circle, red at the start and the end, blue in between. In `ax.quiver(*start, *arrow, ...)` the stars unpack the three coordinates of the point and of the arrow into six arguments; `arrow_length_ratio` is the size of the arrow head.

```python
save_figure(fig, "parallel_transport_sphere",
            "Parallel transport on the unit sphere (wire model; axes $X$, $Y$, $Z$ "
...
check(abs(turning_angle(theta0) - np.pi) < 1e-10,
      "the turning angle at theta0 = pi/3 is pi")
```

The figure is saved; the check confirms that the turning angle at $\theta_0 = \pi/3$ is $\pi$ within $10^{-10}$.

**What Figure 03c.2 shows.** The violet circle of latitude on the grey wire sphere and the transported vector along it. At the start (red, on the right) it points south, down the sphere. The blue arrows turn steadily relative to the circle, and at the end (red again, at the same place) the vector points north, up the sphere: it has turned by $\pi$ although it was never turned along the way. On a flat sheet it would have come back unchanged.

**In [10], Figure 03c.3: the turning angle for 15 circles.**

```python
latitudes = np.linspace(0.1, 1.5, 15)
measured = np.array([turning_angle(t0) for t0 in latitudes])
curve = np.linspace(0.0, np.pi / 2, 300)
fig, ax = plt.subplots()
```

Fifteen circles of latitude, $\theta_0 = 0.1, 0.2, \dots, 1.5$; for each the turning angle measured by the transport of In [8]; 300 values of $\theta_0$ for the smooth curve.

```python
ax.plot(curve, 2 * np.pi * (1 - np.cos(curve)), color=VIOLET, lw=1.8,
        label="cap area / $a^2 = 2\\pi(1 - \\cos\\theta_0)$")
ax.plot(latitudes, measured, "o", color=ORANGE, ms=7,
        label="turning angle measured by parallel transport")
ax.plot(curve, np.zeros_like(curve), ":", color="black", lw=1.2,
        label="flat plane: no turning")
ax.set_xlabel("latitude angle $\\theta_0$ of the loop (radians from the pole)")
ax.set_ylabel("angle (radians)")
ax.set_title("Curvature turns vectors: angle = enclosed area $\\times$ $1/a^2$")
ax.legend(fontsize=8)
```

The violet line is the area of the cap divided by $a^2$ (Section 3.16), the orange dots are the measured angles, and the dotted line at zero is the flat plane (`np.zeros_like` makes an array of zeros of the same length). Labels, title and legend.

```python
deviation = np.max(np.abs(measured - 2 * np.pi * (1 - np.cos(latitudes))))
report("largest difference between the turning angle and area/a^2",
       f"{deviation:.1e}", "radians")
save_figure(fig, "turning_angle",
            "The turning angle of a vector carried once around a circle of latitude "
...
check(deviation < 1e-9, "the turning angle equals the enclosed area over a^2")
```

The largest difference between the measured angles and the formula is printed in a RESULT line: $5.0 \times 10^{-12}$ radians (the format `.1e` writes one digit after the point and a power of ten). The figure is saved, and the check requires the difference to be below $10^{-9}$.

**What Figure 03c.3 shows.** The fifteen orange dots lie exactly on the violet curve $2\pi(1 - \cos\theta_0)$: the larger the cap enclosed by the loop, the more the vector turns. The dotted line shows that on the flat plane every loop gives zero.

**In [11], geodesics are great circles.**

```python
def geodesic_rhs(s, y):
    """The geodesic equations of the unit sphere for y = (theta, phi, dtheta,
    dphi)."""
    th, ph, dth, dph = y
    return np.array([dth, dph, np.sin(th) * np.cos(th) * dph ** 2,
                     -2 * np.cos(th) / np.sin(th) * dth * dph])
```

The two second-order geodesic equations of Section 3.16 (with $a = 1$) written as four first-order equations for the state $(\theta, \varphi, d\theta/ds, d\varphi/ds)$: the derivatives of the first two are the last two, and the derivatives of the last two are the right sides $\sin\theta\cos\theta(d\varphi/ds)^2$ and $-2\cot\theta\,(d\theta/ds)(d\varphi/ds)$. The first line of the body unpacks the four numbers of `y`.

```python
geodesics = {}
for degrees in (20, 50, 80):
    alpha = np.radians(degrees)  # the direction, measured from east towards north
    # unit speed at the equator: dtheta/ds = -sin(alpha) (north), dphi/ds = cos(alpha)
    start = np.array([np.pi / 2, 0.0, -np.sin(alpha), np.cos(alpha)])
    _, path = rk4(geodesic_rhs, start, 0.0, 2 * np.pi, 4000)
    xyz = np.array([point(th, ph) for th, ph in path[:, :2]])
```

Three geodesics start at the point $\theta = \pi/2$, $\varphi = 0$ on the equator, in the directions 20, 50 and 80 degrees north of east (`np.radians` converts degrees to radians). Moving north decreases $\theta$ (the angle from the north pole), hence $d\theta/ds = -\sin\alpha$; moving east increases $\varphi$, $d\varphi/ds = \cos\alpha$. The speed is 1, because $(d\theta/ds)^2 + \sin^2\theta\,(d\varphi/ds)^2 = \sin^2\alpha + \cos^2\alpha = 1$ at the equator. RK4 integrates each path over the length $2\pi$ (once around a great circle) in 4000 steps, and `xyz` holds the path as points in three dimensions (`path[:, :2]` is the table of the first two columns, $\theta$ and $\varphi$).

```python
    # the starting direction in X, Y, Z: east is (0, 1, 0), north is (0, 0, 1)
    velocity0 = np.array([0.0, np.cos(alpha), np.sin(alpha)])
    normal = np.cross(xyz[0], velocity0)  # perpendicular to the expected plane
    geodesics[degrees] = (xyz, np.max(np.abs(xyz @ normal)))
```

A great circle lies in the plane through the centre of the sphere spanned by its starting point and its starting direction. `np.cross` is the cross product of two vectors in space, a vector perpendicular to both; it has length 1 here because the two are perpendicular unit vectors. The distance of a point from that plane is the size of its dot product with the perpendicular vector; `xyz @ normal` computes this dot product for every point of the path at once (`@` is the product of a matrix with a vector). The path and its largest distance from the plane are stored in the dictionary under the angle.

```python
    say(f"  direction {degrees:2d} degrees: largest distance from the plane "
        f"= {geodesics[degrees][1]:.1e}, end point back at start: "
        f"{np.allclose(xyz[-1], xyz[0], atol=1e-8)}")
check(all(distance < 1e-8 for _, distance in geodesics.values()),
      "the three geodesics stay in planes through the centre: great circles")
```

For each direction one line is printed: the largest distance ($1.2 \times 10^{-13}$, $6.2 \times 10^{-13}$ and $7.1 \times 10^{-11}$) and whether the end point equals the start within $10^{-8}$ (`True` for all three). The check requires all three distances to be below $10^{-8}$.

```python
theta_circle = np.pi / 3
residual = np.sin(theta_circle) * np.cos(theta_circle) * (1 / np.sin(theta_circle)) ** 2
report("geodesic equation of the latitude theta0 = pi/3: missing acceleration",
       f"{residual:.6f}")
check(residual > 0.5, "the circle of latitude theta0 = pi/3 is not a geodesic")
```

The circle of latitude $\theta_0 = \pi/3$ at unit speed has $d\varphi/ds = 1/\sin\theta_0$ and $d^2\theta/ds^2 = 0$; the right side of the first geodesic equation is then $\sin\theta_0\cos\theta_0/\sin^2\theta_0 = \cot\theta_0$, printed as $0.577350$ (Section 3.16). It is not zero, so the circle of latitude is not a geodesic.

**In [12], Figure 03c.4.**

```python
fig = plt.figure(figsize=(6.4, 6.0))
ax = fig.add_subplot(projection="3d")
wire_sphere(ax)
for (degrees, (xyz, _)), colour, style in zip(geodesics.items(),
                                              (RED, ORANGE, AQUA), ("-", "--", "-.")):
    ax.plot(xyz[:, 0], xyz[:, 1], xyz[:, 2], color=colour, ls=style, lw=1.8,
            label=f"geodesic leaving at {degrees} degrees")
```

The wire sphere again, and the three geodesics, each in its own colour and line style; `zip` walks through the stored geodesics, the colours and the styles together, and the pattern `(degrees, (xyz, _))` takes apart each dictionary entry (the stored distance is not needed).

```python
ax.plot(circle[:, 0], circle[:, 1], circle[:, 2], color=VIOLET, ls=":", lw=1.8,
        label="circle of latitude (not a geodesic)")
ax.scatter([1.0], [0.0], [0.0], color="black", s=30)
ax.set_title("Geodesics of the sphere from one point")
ax.legend(fontsize=7, loc="upper left")
```

The circle of latitude of In [9], dotted; the common starting point $(1, 0, 0)$ as a black dot (`scatter` draws points, `s` is their size); title and legend.

```python
save_figure(fig, "geodesics_sphere",
            "Three geodesics of the unit sphere (axes $X$, $Y$, $Z$ in units of the "
...
check(all(np.allclose(xyz[-1], xyz[0], atol=1e-8) for xyz, _ in geodesics.values()),
      "every geodesic returns to its start after the length 2 pi")
```

The figure is saved; the check requires each geodesic to come back to its start after the length $2\pi$, within $10^{-8}$.

**What Figure 03c.4 shows.** The three geodesics leave the black dot on the equator in three directions; each is a full circle around the sphere, centred at its centre (a great circle), tilted the more steeply the more northward it starts, and each passes through the opposite point $(-1, 0, 0)$. The dotted circle of latitude is smaller and is not centred at the centre of the sphere: a traveller following it would have to keep turning towards the pole.

**In [13], Figure 03c.5: geodesic deviation.**

```python
sigma = float(sphere_mixed[(0, 1, 0, 1)].subs(a, 1))  # the Gaussian curvature, a = 1
s_values, deviation_states = rk4(lambda s, y: np.array([y[1], -sigma * y[0]]),
                                 np.array([1.0, 0.0]), 0.0, np.pi / 2, 1000)
```

`sigma` is the Gaussian curvature $\sigma$ computed in In [7], $1/a^2$, with $a = 1$, as a floating-point number. The deviation equation $\xi'' = -\sigma\xi$ of Section 3.18 as two first-order equations for $(\xi, \xi')$; `lambda s, y: ...` is a short function without a name that returns $(\xi', -\sigma\xi)$. RK4 solves it from $\xi = 1$, $\xi' = 0$ (start parallel, distance 1) over the length $\pi/2$ in 1000 steps.

```python
d_phi = 1e-3  # the angle between the two meridians
chord = np.array([np.linalg.norm(point(np.pi / 2 - s, 0.0) - point(np.pi / 2 - s, d_phi))
                  for s in s_values]) / np.linalg.norm(point(np.pi / 2, 0.0)
                                                       - point(np.pi / 2, d_phi))
```

Two meridians $10^{-3}$ apart, followed from the equator northwards ($\theta = \pi/2 - s$). Their distance is measured as the length of the straight chord between the two points (`np.linalg.norm` is the length of a vector), divided by its value at the equator. The chord is $2\sin\theta\sin(\Delta\varphi/2)$, so the ratio is exactly $\sin\theta/\sin(\pi/2) = \cos s$, the result of Section 3.18 with $a = 1$.

```python
fig, ax = plt.subplots()
ax.plot(s_values, chord, color=BLUE, lw=3.0, alpha=0.6,
        label="two meridians $10^{-3}$ apart (exact)")
ax.plot(s_values, deviation_states[:, 0], "--", color=RED, lw=1.8,
        label="deviation equation $\\xi^{\\prime\\prime} = -\\xi/a^2$ (RK4)")
ax.plot(s_values, np.ones_like(s_values), ":", color="black", lw=1.2,
        label="flat plane: parallel lines keep their distance")
ax.set_xlabel("length $s$ along the geodesics (unit $a$)")
ax.set_ylabel("distance / starting distance")
ax.set_title("Initially parallel geodesics meet at the pole")
ax.legend(fontsize=8)
```

The exact distance as a thick, partly transparent blue line (`alpha=0.6`), the RK4 solution as a dashed red line on top of it, and the flat plane as a dotted line at $1$. Labels, title, legend.

```python
agreement = np.max(np.abs(chord - deviation_states[:, 0]))
report("largest difference between the meridians and the deviation equation",
       f"{agreement:.1e}")
save_figure(fig, "geodesic_deviation",
            "The distance between two neighbouring geodesics that start parallel, "
...
check(agreement < 1e-6,
      "the curvature 1/a^2 predicts how fast neighbouring geodesics approach")
```

The largest difference between the two curves is printed: $8.0 \times 10^{-14}$. The figure is saved; the check requires the difference to be below $10^{-6}$.

**What Figure 03c.5 shows.** The red dashed curve lies exactly on the blue one: both fall from $1$ like $\cos s$ and reach $0$ at $s = \pi/2$, the pole, where the meridians meet. The curvature $1/a^2$, computed from the Riemann tensor, predicts how fast two geodesics that start parallel approach each other. On the plane (dotted) the distance would stay $1$.

**In [14], the last check.**

```python
figure_names = ["plane_polar_components", "parallel_transport_sphere",
                "turning_angle", "geodesics_sphere", "geodesic_deviation"]
files = [output_file(f"{FIGURE_FOLDER}/03c_{k}_{n}.png")
         for k, n in enumerate(figure_names, 1)]
check(all(path.is_file() for path in files), "all five figure files exist")
all_checks_passed()
```

The names of the five figures, numbered from 1 by `enumerate(figure_names, 1)`; the check that all five files exist; and the last line, ALL 16 CHECKS PASSED (notebook 03c). The 16 checks are: 2 in In [4], 1 each in In [5] and In [6], 3 in In [7], 2 in In [8], 1 each in In [9] and In [10], 2 in In [11], and 1 each in In [12], In [13] and In [14].

### 3.23 The Christoffel symbols of the author's metric

Now the tools of Sections 3.15 to 3.17 are applied to the corrected metric, by hand and completely. Throughout, $i$ stands for any of the three 3-space directions $x_1, x_2, x_3$ and $j$ for any of the three extra times $x_5, x_6, x_7$; the four directions $x_0, x_5, x_6, x_7$ form the **block** of Section 3.9. The scale factors (Section 3.7) are $h_0 = f|\cot z|$, $h_i = e^{a_4}$, $h_4 = 1$, $h_j = fW$, with the hidden scale $f = e^{-a_4}b_4^{1/2}$, the warp factor $W = (\sin^2 z)^{1/12}$ and the signs $\eta = (+,+,+,+,-,-,-,-)$ in the order $x_0, \dots, x_7$.

**The logarithmic derivatives of the scale factors.** Only $x_4$ and $x_0$ appear in the metric, so only $\partial_4$ and $\partial_0$ can give something non-zero.

$$
\partial_4 \ln h_i = \partial_4 a_4 = a_4' \equiv \alpha, \qquad \partial_4 \ln h_j = \partial_4 \ln h_0 = \partial_4\bigl(\tfrac12\ln b_4 - a_4\bigr) = -a_4' + \frac{b_4'}{2b_4} \equiv \alpha_t
$$

(the logarithm of a product is the sum of the logarithms; $\ln e^{\pm a_4} = \pm a_4$; $\ln b_4^{1/2} = \frac12\ln b_4$, whose derivative is $b_4'/(2b_4)$; the factors $W$ and $|\cot z|$ do not depend on $x_4$). These are the two expansion rates of Section 3.7: $\alpha$ of 3-space and $\alpha_t$ of the block. On the history of Section 3.8, $b_4'/b_4 = \frac43 a_4'$ and so $\alpha_t = -\frac13\alpha$.

$$
\partial_0 \ln h_j = \partial_0\bigl(\tfrac1{12}\ln\sin^2 z\bigr) = \frac1{12}\cdot\frac{2\sin z\cos z}{\sin^2 z}\cdot 6H = H\cot z
$$

(the parts $a_4$ and $\ln b_4$ do not depend on $x_0$; the chain rule with $dz/dx_0 = 6H$, Section 3.2). For 3-space, $\partial_0\ln h_i = 0$: 3-space has no warp.

$$
\partial_0 \ln h_0 = \partial_0\ln|\cot z| = \frac{1}{\cot z}\cdot\Bigl(-\frac{1}{\sin^2 z}\Bigr)\cdot 6H = -\frac{\sin z}{\cos z}\cdot\frac{6H}{\sin^2 z} = -\frac{6H}{\sin z\cos z}
$$

(the derivative of $\ln|u|$ is $u'/u$ for either sign of $u$; the derivative of $\cot z$ is $-1/\sin^2 z$; the chain rule). Since $1 = \sin^2 z + \cos^2 z$, $\frac{1}{\sin z\cos z} = \frac{\sin^2 z + \cos^2 z}{\sin z\cos z} = \tan z + \cot z$, so $\partial_0\ln h_0 = -6H(\tan z + \cot z)$. Finally $h_4 = 1$ gives $\partial_4\ln h_4 = \partial_0\ln h_4 = 0$.

**The four cases of Section 3.15.** Case (a), $\Gamma^a{}_{aa} = \partial_a\ln h_a$: only $a = x_0$ gives a non-zero value,

$$
\Gamma^{x_0}{}_{x_0x_0} = -6H(\tan z + \cot z) = -\frac{6H}{\sin z\cos z} .
$$

Case (b), $\Gamma^a{}_{ab} = \Gamma^a{}_{ba} = \partial_b\ln h_a$ with $b \ne a$: with $b = x_4$,

$$
\Gamma^{x_i}{}_{x_ix_4} = \alpha = a_4', \qquad \Gamma^{x_j}{}_{x_jx_4} = \Gamma^{x_0}{}_{x_0x_4} = \alpha_t = -a_4' + \frac{b_4'}{2b_4} ,
$$

and with $b = x_0$, for the three extra times,

$$
\Gamma^{x_j}{}_{x_jx_0} = H\cot z
$$

(for 3-space $\Gamma^{x_i}{}_{x_ix_0} = \partial_0\ln h_i = 0$, and the pair $a = x_4$, $b = x_0$ gives zero because $h_4$ is constant). Case (c), $\Gamma^a{}_{bb} = -\eta_{aa}\eta_{bb}\,(h_b^2/h_a^2)\,\partial_a\ln h_b$ with $b \ne a$: it needs $\partial_a\ln h_b \ne 0$, so $a$ is $x_4$ or $x_0$. For $a = x_4$ ($\eta_{44} = -1$, $h_4 = 1$) it is $+\eta_{bb}\,h_b^2\,\partial_4\ln h_b$:

$$
\Gamma^{x_4}{}_{x_ix_i} = (+1)\,e^{2a_4}\,\alpha = a_4'\,e^{2a_4}, \qquad \Gamma^{x_4}{}_{x_jx_j} = (-1)\,f^2W^2\,\alpha_t = -\alpha_t\,e^{-2a_4}b_4(\sin^2 z)^{1/6},
$$

$$
\Gamma^{x_4}{}_{x_0x_0} = (+1)\,f^2\cot^2 z\,\alpha_t = \alpha_t\,e^{-2a_4}b_4\cot^2 z
$$

(with $h_j^2 = f^2W^2 = e^{-2a_4}b_4(\sin^2 z)^{1/6}$ and $h_0^2 = f^2\cot^2 z$). For $a = x_0$ ($\eta_{00} = +1$, $h_0^2 = f^2\cot^2 z$) only the extra times give something, because $\partial_0\ln h_i = \partial_0\ln h_4 = 0$:

$$
\Gamma^{x_0}{}_{x_jx_j} = -(-1)\,\frac{f^2W^2}{f^2\cot^2 z}\,H\cot z = H\,W^2\tan z = H\tan z\,(\sin^2 z)^{1/6}
$$

($\eta_{jj} = -1$; the factor $f^2$ cancels; $\cot z/\cot^2 z = 1/\cot z = \tan z$). Case (d) gives only zeros.

**The complete list.** With the lower indices ordered ($b \le c$, in the order $x_0, \dots, x_7$) there are $1 + 1 + 3 + 3 + 1 + 3 + 3 + 3 + 3 = 21$ non-zero symbols, and counting both orders of two different lower indices $31$ of the $8^3 = 512$:

| symbol ($b \le c$) | value | how many |
| --- | --- | --- |
| $\Gamma^{x_0}{}_{x_0x_0}$ | $-6H(\tan z + \cot z)$ | 1 |
| $\Gamma^{x_0}{}_{x_0x_4}$ | $\alpha_t = -a_4' + b_4'/(2b_4)$ | 1 |
| $\Gamma^{x_0}{}_{x_jx_j}$, $j = 5, 6, 7$ | $H\tan z\,(\sin^2 z)^{1/6}$ | 3 |
| $\Gamma^{x_i}{}_{x_ix_4}$, $i = 1, 2, 3$ | $a_4'$ | 3 |
| $\Gamma^{x_4}{}_{x_0x_0}$ | $\alpha_t\,e^{-2a_4}b_4\cot^2 z$ | 1 |
| $\Gamma^{x_4}{}_{x_ix_i}$ | $a_4'\,e^{2a_4}$ | 3 |
| $\Gamma^{x_4}{}_{x_jx_j}$ | $-\alpha_t\,e^{-2a_4}b_4(\sin^2 z)^{1/6}$ | 3 |
| $\Gamma^{x_j}{}_{x_0x_j}$ | $H\cot z$ | 3 |
| $\Gamma^{x_j}{}_{x_4x_j}$ | $\alpha_t$ | 3 |

This is exactly the list `christoffelNonzero_b_le_c` of the record `Revision/gkd_lovelock/results/curvature.json` (PROVED here by hand; Notebook 03b reproduces it symbol by symbol, In [7]; the independent verification of the record agrees, `python-lovelock-report.json`, check `rust_christoffels_agree`). The record writes $\tan z$ as `Cot[6*H*x0]^(-1)` and $\Gamma^{x_4}{}_{x_jx_j}$ as the sum `-(1/2)*E^(-2*a4[x4])*(Sin[6*H*x0]^2)^(1/6)*Derivative[1][b4][x4] + Derivative[1][a4][x4]*E^(-2*a4[x4])*(Sin[6*H*x0]^2)^(1/6)*b4[x4]`. Every symbol has at least one index $x_4$ or $x_0$, the two coordinates on which the metric depends, and no symbol has the pair $x_0$ and a 3-space index, because 3-space has no warp. The hidden direction behaves like an extra time: $\Gamma^{x_0}{}_{x_0x_4} = \Gamma^{x_j}{}_{x_jx_4} = \alpha_t$. On the history of Section 3.8 these symbols are $-a_4' + \frac23 a_4' = -\frac13 a_4'$, of the opposite sign of the 3-space ones (Notebook 03b checks the value $-1/3$ at $a_4' = 1$ and $\Gamma^{x_5}{}_{x_5x_0} = H\cot z = 1$ at $z = \pi/4$, In [9]). At the fold, $\cot z \to 0$ and $\tan z$ grows without bound, so $\Gamma^{x_0}{}_{x_0x_0}$ and $\Gamma^{x_0}{}_{x_jx_j}$ grow without bound there while $\Gamma^{x_j}{}_{x_0x_j}$ and $\Gamma^{x_4}{}_{x_0x_0}$ vanish; at a tip the roles are exchanged.

**Observers at rest fall freely.** No symbol has the lower pair $(x_4, x_4)$: case (a) with $a = x_4$ is $\partial_4\ln h_4 = 0$, and case (c) with $b = x_4$ contains $\partial_a\ln h_4 = 0$. So $\Gamma^a{}_{x_4x_4} = 0$ for every $a$, for all functions $a_4$ and $b_4$. An observer who keeps $x_0, x_1, x_2, x_3, x_5, x_6, x_7$ fixed while $x_4 = \tau$ runs has $u^a = dx^a/d\tau = 1$ for $a = x_4$ and $0$ otherwise, and $du^a/d\tau = 0$; the geodesic equation of Section 3.16 reads $0 + \Gamma^a{}_{x_4x_4}\cdot1\cdot1 = 0$, which holds. The squared speed is $g(u, u) = g_{44} = -1$, so $\tau = x_4$ is the observer's proper time. **Observers at rest are in free fall, and their clocks show $x_4$** (PROVED; Notebook 03b, In [12]).

**The contracted symbols.** By Section 3.15, $\sum_a\Gamma^a{}_{ab} = \partial_b\ln\sqrt{|\det g|}$, with $\sqrt{|\det g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$ (Section 3.6). We check this with the list. For $b = x_4$,

$$
\sum_a\Gamma^a{}_{a4} = \alpha_t + 3\alpha + 3\alpha_t = 3a_4' + 4\alpha_t = 3a_4' - 4a_4' + \frac{2b_4'}{b_4} = -a_4' + \frac{2b_4'}{b_4} ,
$$

the rate of Section 3.6. For $b = x_0$,

$$
\sum_a\Gamma^a{}_{a0} = -6H(\tan z + \cot z) + 3H\cot z = -6H\tan z - 3H\cot z ,
$$

and

$$
\partial_0\ln\bigl(|\cot z|(\sin^2 z)^{1/4}\bigr) = -6H(\tan z + \cot z) + \frac14\cdot 2\cot z\cdot 6H = -6H\tan z - 3H\cot z
$$

(the logarithmic derivatives above; $\partial_0\ln\sin^2 z = 2\cot z\cdot 6H$). Both agree (Notebook 03b, In [12]).

### 3.24 The curvature of the author's metric, by hand

**The curvature of every coordinate plane.** For a diagonal metric, Section 3.17 gives $\sigma(a, b) = R^{ab}{}_{ab} = g^{bb}R^a{}_{bab}$ (no sum), with

$$
R^a{}_{bab} = \partial_a\Gamma^a{}_{bb} - \partial_b\Gamma^a{}_{ba} + \sum_e\bigl(\Gamma^a{}_{ae}\Gamma^e{}_{bb} - \Gamma^a{}_{be}\Gamma^e{}_{ba}\bigr)
$$

(the formula of Section 3.17 with $c = a$ and $d = b$). The 28 coordinate planes fall into six kinds. We compute each kind once, with general labels, so that the computation holds for every plane of that kind; $c$ stands for any of the four block directions $x_0, x_5, x_6, x_7$. Two facts from the list of Section 3.23 are used again and again: a derivative $\partial_i$ or $\partial_j$ of anything is zero (nothing depends on $x_1, x_2, x_3, x_5, x_6, x_7$), and in the list $\Gamma^{x_4}{}_{cc} = \eta_{cc}\,\alpha_t\,h_c^2$ for every block direction.

(1) Two different 3-space directions $i$ and $i'$ (3 planes):

$$
R^i{}_{i'ii'} = 0 - 0 + \Gamma^i{}_{i4}\Gamma^4{}_{i'i'} - 0 = \alpha\cdot\alpha\,e^{2a_4} = \alpha^2 e^{2a_4}
$$

($\Gamma^i{}_{i'i'} = \Gamma^i{}_{i'i} = 0$ because $i' \ne i$; in $\sum_e\Gamma^i{}_{ie}\Gamma^e{}_{i'i'}$ only $e = x_4$ survives, because $\Gamma^i{}_{i0} = 0$; every $\Gamma^i{}_{i'e}$ is zero), so $\sigma(i, i') = g^{i'i'}\alpha^2e^{2a_4} = \alpha^2$ (with $g^{i'i'} = e^{-2a_4}$).

(2) A 3-space direction $i$ and the time $x_4$ (3 planes):

$$
R^i{}_{4i4} = \partial_i\Gamma^i{}_{44} - \partial_4\Gamma^i{}_{4i} + \sum_e\Gamma^i{}_{ie}\Gamma^e{}_{44} - \sum_e\Gamma^i{}_{4e}\Gamma^e{}_{4i} = 0 - \alpha' + 0 - \alpha^2
$$

($\partial_i$ gives zero; $\partial_4\alpha = \alpha' = a_4''$; every $\Gamma^e{}_{44}$ is zero, Section 3.23; in the last sum only $e = i$ survives), so $\sigma(i, 4) = g^{44}\bigl(-\alpha' - \alpha^2\bigr) = \alpha^2 + \alpha'$ (with $g^{44} = -1$).

(3) A 3-space direction $i$ and a block direction $c$ (12 planes):

$$
R^i{}_{cic} = 0 - 0 + \Gamma^i{}_{i4}\Gamma^4{}_{cc} - 0 = \alpha\cdot\eta_{cc}\alpha_th_c^2
$$

($\Gamma^i{}_{cc} = \Gamma^i{}_{ci} = 0$, so both derivative terms vanish; in $\sum_e\Gamma^i{}_{ie}\Gamma^e{}_{cc}$ only $e = x_4$ survives, because $\Gamma^i{}_{i0} = 0$; every $\Gamma^i{}_{ce}$ is zero), so $\sigma(i, c) = g^{cc}\,\alpha\,\eta_{cc}\alpha_th_c^2 = \alpha\alpha_t$ (with $g^{cc} = \eta_{cc}/h_c^2$ and $\eta_{cc}^2 = 1$).

(4) A block direction $c$ and the time $x_4$ (4 planes): the three steps of case (2) with $a = c$,

$$
R^c{}_{4c4} = 0 - \partial_4\Gamma^c{}_{4c} + 0 - \Gamma^c{}_{4c}\Gamma^c{}_{4c} = -\alpha_t' - \alpha_t^2
$$

($\Gamma^c{}_{44} = 0$ and every $\Gamma^e{}_{44} = 0$; in $\sum_e\Gamma^c{}_{4e}\Gamma^e{}_{4c}$ only $e = c$ survives, with $\Gamma^c{}_{4c} = \alpha_t$ for $c = x_0$ as well as for the extra times), so $\sigma(c, 4) = g^{44}(-\alpha_t' - \alpha_t^2) = \alpha_t^2 + \alpha_t'$, with the derivative of the block rate

$$
\alpha_t' = -a_4'' + \frac{b_4''}{2b_4} - \frac{b_4'^2}{2b_4^2}
$$

(the quotient rule for $b_4'/(2b_4)$).

(5) Two different extra times $j$ and $j'$ (3 planes):

$$
R^j{}_{j'jj'} = \Gamma^j{}_{j4}\Gamma^4{}_{j'j'} + \Gamma^j{}_{j0}\Gamma^0{}_{j'j'} = \alpha_t\cdot\bigl(-\alpha_tf^2W^2\bigr) + H\cot z\cdot H\tan z\,W^2 = \bigl(H^2 - \alpha_t^2f^2\bigr)W^2
$$

($\Gamma^j{}_{j'j'} = \Gamma^j{}_{j'j} = 0$ because $j' \ne j$, so both derivative terms vanish; in $\sum_e\Gamma^j{}_{je}\Gamma^e{}_{j'j'}$ only $e = x_4$ and $e = x_0$ survive; every $\Gamma^j{}_{j'e}$ is zero; $\cot z\tan z = 1$), so $\sigma(j, j') = g^{j'j'}\bigl(H^2 - \alpha_t^2f^2\bigr)W^2 = \alpha_t^2 - H^2/f^2$ (with $g^{j'j'} = -1/(f^2W^2)$).

(6) An extra time $j$ and the hidden direction $x_0$ (3 planes):

$$
R^j{}_{0j0} = \partial_j\Gamma^j{}_{00} - \partial_0\Gamma^j{}_{0j} + \Gamma^j{}_{j4}\Gamma^4{}_{00} + \Gamma^j{}_{j0}\Gamma^0{}_{00} - \Gamma^j{}_{0j}\Gamma^j{}_{0j}
$$

(in $\sum_e\Gamma^j{}_{je}\Gamma^e{}_{00}$ only $e = x_4$ and $e = x_0$ survive; in $\sum_e\Gamma^j{}_{0e}\Gamma^e{}_{0j}$ only $e = j$)

$$
= 0 + \frac{6H^2}{\sin^2 z} + \alpha_t\cdot\alpha_tf^2\cot^2 z + H\cot z\cdot\bigl(-6H(\tan z + \cot z)\bigr) - H^2\cot^2 z
$$

($\Gamma^j{}_{00} = 0$; $\partial_0(H\cot z) = H\cdot(-1/\sin^2 z)\cdot 6H$, so $-\partial_0\Gamma^j{}_{0j} = +6H^2/\sin^2 z$; the values of the list)

$$
= \frac{6H^2}{\sin^2 z} - 6H^2\bigl(1 + \cot^2 z\bigr) + \alpha_t^2f^2\cot^2 z - H^2\cot^2 z = \bigl(\alpha_t^2f^2 - H^2\bigr)\cot^2 z
$$

($\cot z\tan z = 1$; $1 + \cot^2 z = (\sin^2 z + \cos^2 z)/\sin^2 z = 1/\sin^2 z$, so the first two terms cancel). Hence $\sigma(j, 0) = g^{00}(\alpha_t^2f^2 - H^2)\cot^2 z = \alpha_t^2 - H^2/f^2$ (with $g^{00} = 1/(f^2\cot^2 z)$): the same value as inside the extra times.

**The block of constant curvature.** In all six planes of the block the curvature is $\alpha_t^2 - H^2/f^2 = \alpha_t^2 - H^2k$, where

$$
k = \frac{e^{2a_4}}{b_4} = \frac{1}{f^2}
$$

(with $f^2 = e^{-2a_4}b_4$). For the bracket $dy^2 - e^{2Hy}(dx_5^2 + dx_6^2 + dx_7^2)$ of Section 3.9 alone, which is the block with $f = 1$ and nothing depending on time ($\alpha_t = 0$), the same computation gives $-H^2$ in each of its six planes: it is the space of constant curvature $-H^2$ of Section 3.9 (record `Revision/metric_warped/reports/python-warped-metric-report.json`, check `hidden_block_constant_curvature`). The factor $f^2$ divides its curvature by $f^2$ (multiplying a metric by a positive constant leaves the Christoffel symbols and $R^a{}_{bcd}$ unchanged and divides every raised index by that constant), and the change of $f$ in time adds $\alpha_t^2$. As the block shrinks, $k = 1/f^2$ grows, and so does the size of its own curvature.

**The table of the plane curvatures** (PROVED; Notebook 03b computes all 28 and checks these formulas, In [16]), with $\alpha = a_4'$, $\alpha_t = -a_4' + b_4'/(2b_4)$ and $k = e^{2a_4}/b_4$:

| plane | how many | curvature $\sigma(a, b) = R^{ab}{}_{ab}$ | for $b_4 \propto e^{4a_4/3}$ |
| --- | --- | --- | --- |
| two 3-space directions | 3 | $\alpha^2$ | $a_4'^2$ |
| a 3-space direction and the time $x_4$ | 3 | $\alpha^2 + \alpha'$ | $a_4'^2 + a_4''$ |
| a 3-space direction and a block direction | 12 | $\alpha\alpha_t$ | $-\frac13 a_4'^2$ |
| a block direction and the time $x_4$ | 4 | $\alpha_t^2 + \alpha_t'$ | $\frac19 a_4'^2 - \frac13 a_4''$ |
| two block directions | 6 | $\alpha_t^2 - H^2k$ | $\frac19 a_4'^2 - H^2k$ |

None depends on $z$; only $H$, the rates $\alpha$ and $\alpha_t$, their derivatives and $k$ appear (and so $a_4'$, $a_4''$, $b_4'/b_4$, $b_4''/b_4$ and $e^{2a_4}/b_4$). The hidden direction behaves in every plane exactly like an extra time. These are the values of the record's 112 components (`curvature.json`, list `riemannMixedNonzero`, in the record's notation $(a_4' - u/2)^2 - H^2k$ for the block planes, with $u = b_4'/b_4$; `Revision/docs/LOVELOCK_GKD.md`, its section 6.1). The last column takes $b_4 = b_4(0)\,e^{\beta a_4}$ with $\beta = 4/3$, as on the history of Section 3.8, but with a general $a_4(x_4)$: then $b_4'/b_4 = \frac43 a_4'$, $\alpha_t = -\frac13 a_4'$ and $\alpha_t' = -\frac13 a_4''$. Along the history itself ($a_4' = AH$, $a_4'' = 0$, $k = e^{2a_4/3}$ with $b_4(0) = 1$) the planes inside 3-space and those of 3-space with $x_4$ have $A^2H^2$, the planes of 3-space with the block $-\frac13 A^2H^2$, the planes of the block with $x_4$ $\frac19 A^2H^2$, and the planes inside the block $(\frac19 A^2 - k)H^2$; on the first slice $a_4 = 0$ ($k = 1$) and at the canonical $A = 1$ the last is $-\frac89 H^2$.

**What the signs mean.** By Section 3.17 the sign of $\sigma(a, b)$ describes a shape only in the 6 planes of two space-like directions: the 3 planes inside 3-space ($\alpha^2 \ge 0$, sphere-like wherever $a_4' \ne 0$) and the 3 planes of a 3-space direction with $x_0$ ($\alpha\alpha_t$; along the history $-\frac13 A^2H^2$, saddle-like). In the 6 planes of two time-like directions (inside the extra times, and an extra time with $x_4$) the shape reading is reversed. The other 16 planes contain one space-like and one time-like direction; for them, and for every plane that contains $x_4$, the sign is read from free fall, $d^2\xi/d\tau^2 = +\sigma\,\xi$ (Section 3.18). We now verify this rule by hand where it can be seen most simply: for the observers at rest of Section 3.23, which fall freely along $x_4$ with the proper time $\tau = x_4$. Take two of them that differ only by a small coordinate distance $\Delta x_a$ along a direction $x_a$ other than $x_4$. Their proper distance is

$$
\xi = h_a\,\Delta x_a
$$

(Section 3.7; $\Delta x_a$ and $z$ do not change along the two paths). Differentiate twice with respect to $\tau = x_4$, with $\partial_4 h_a = \alpha_ah_a$, where $\alpha_a$ is the rate of $x_a$ ($\alpha$ for 3-space, $\alpha_t$ for the block):

$$
\frac{d\xi}{d\tau} = \alpha_a\,h_a\,\Delta x_a = \alpha_a\,\xi, \qquad \frac{d^2\xi}{d\tau^2} = \alpha_a'\,\xi + \alpha_a\,\frac{d\xi}{d\tau} = \bigl(\alpha_a^2 + \alpha_a'\bigr)\,\xi
$$

(the product rule). For $a = x_1$ the factor is exactly $\sigma(x_1, x_4) = \alpha^2 + \alpha'$ of case (2), and for $a = x_5$ and $a = x_0$ exactly $\sigma(x_5, x_4) = \sigma(x_0, x_4) = \alpha_t^2 + \alpha_t'$ of case (4): $d^2\xi/d\tau^2 = +\sigma\,\xi$. All three PROVED; Notebook 03b checks them exactly (In [16]). Along the history $\sigma(x_1, x_4) = A^2H^2$ and $\sigma(x_5, x_4) = \sigma(x_0, x_4) = A^2H^2/9$, both positive: a positive curvature, and yet the 3-space distance grows like $e^{AH\tau}$ and the block distances shrink like $e^{-AH\tau/3}$, ever more slowly, both with a positive second derivative. On the sphere of Section 3.18 a positive curvature pulls neighbouring geodesics together; here it drives them apart.

**No other component.** For a diagonal metric that depends only on $x_4$ and $x_0$, every component $R^{ab}{}_{cd}$ that is not a plane curvature is one of $R^{x_0c}{}_{x_4c}$, $R^{x_4c}{}_{x_0c}$ and their partners under the antisymmetries, with $c \ne x_0, x_4$ (a general fact of such metrics, stated with its derivation in `Revision/docs/METRIC_SELF_CONSISTENCY.md`, its section 2.1; we quote it, ASSUMED in general, and the record checks it for this metric). We compute both kinds. First, with $c = i$ in 3-space,

$$
R^0{}_{i4i} = \partial_4\Gamma^0{}_{ii} - \partial_i\Gamma^0{}_{i4} + \sum_e\Gamma^0{}_{4e}\Gamma^e{}_{ii} - \sum_e\Gamma^0{}_{ie}\Gamma^e{}_{i4} = 0 - 0 + \Gamma^0{}_{40}\Gamma^0{}_{ii} - 0 = 0
$$

(the formula with $a = x_0$, $b = i$, $c = x_4$, $d = i$; $\Gamma^0{}_{ii} = 0$ because 3-space has no warp; $\Gamma^0{}_{4e}$ is non-zero only for $e = x_0$; every $\Gamma^0{}_{ie}$ is zero), and with $c = j$ an extra time,

$$
R^0{}_{j4j} = \partial_4\Gamma^0{}_{jj} - 0 + \Gamma^0{}_{40}\Gamma^0{}_{jj} - \Gamma^0{}_{jj}\Gamma^j{}_{j4} = 0 + \alpha_t\,HW^2\tan z - HW^2\tan z\,\alpha_t = 0
$$

($\Gamma^0{}_{jj} = HW^2\tan z$ does not depend on $x_4$, because the factor $f^2$ cancelled in it; $\Gamma^0{}_{40} = \Gamma^j{}_{j4} = \alpha_t$). Second, with the upper index $x_4$:

$$
R^4{}_{i0i} = \partial_0\Gamma^4{}_{ii} - \partial_i\Gamma^4{}_{i0} + \sum_e\Gamma^4{}_{0e}\Gamma^e{}_{ii} - \sum_e\Gamma^4{}_{ie}\Gamma^e{}_{i0} = 0 - 0 + \Gamma^4{}_{00}\Gamma^0{}_{ii} - \Gamma^4{}_{ii}\Gamma^i{}_{i0} = 0
$$

($\Gamma^4{}_{ii} = a_4'e^{2a_4}$ does not depend on $x_0$; $\Gamma^0{}_{ii} = \Gamma^i{}_{i0} = 0$, no warp), and

$$
\begin{aligned}
R^4{}_{j0j} &= \partial_0\Gamma^4{}_{jj} + \Gamma^4{}_{00}\Gamma^0{}_{jj} - \Gamma^4{}_{jj}\Gamma^j{}_{j0}\\
&= -2\alpha_tf^2W^2H\cot z + \alpha_tf^2\cot^2 z\cdot HW^2\tan z + \alpha_tf^2W^2\cdot H\cot z = 0
\end{aligned}
$$

($\partial_0 W^2 = 2H\cot z\,W^2$, twice the logarithmic derivative of $W$; $\cot^2 z\tan z = \cot z$; the coefficients $-2 + 1 + 1$ add to zero). Both kinds vanish for two reasons that the corrected metric was built to have: the hidden direction changes in time at the rate of the extra times ($\Gamma^{x_0}{}_{x_0x_4} = \Gamma^{x_j}{}_{x_jx_4}$), and 3-space has no warp ($\Gamma^{x_0}{}_{x_ix_i} = \Gamma^{x_i}{}_{x_ix_0} = 0$). So **the only non-zero components are the plane curvatures** (PROVED; records `lovelock-report.json` and `python-lovelock-report.json`, check `mixed_riemann_only_sectional`; Notebook 03b, In [14]). Each of the 28 planes gives four components, $R^{ab}{}_{ab} = R^{ba}{}_{ba} = \sigma(a, b)$ and $R^{ab}{}_{ba} = R^{ba}{}_{ab} = -\sigma(a, b)$ (Section 3.17), and for general functions every $\sigma \ne 0$: $28 \times 4 = 112$ components, exactly the number that the Rust program of the record and Notebook 03b find (`Revision/gkd_lovelock/results/lovelock-report.json`, check `riemann_antisymmetry`: "112 nonzero entries"; Notebook 03b, In [13]). They take 10 different values, $\pm$ the five values of the table (In [15]). None of them depends on $z$ (check `mixed_riemann_free_of_x0` of both reports; In [14]): although many Christoffel symbols grow without bound at the fold or at the tips, the curvature itself is the same at every value of $z$.

### 3.25 Ricci, Einstein and Kretschmann of the author's metric; the contracted Bianchi identity

**The diagonal of the Ricci tensor.** By Section 3.17, $R^a{}_a$ is the sum of the curvatures of the seven planes that contain $x_a$. From the table of Section 3.24:

$$
R^i{}_i = 2\alpha^2 + (\alpha^2 + \alpha') + 4\alpha\alpha_t = 3\alpha^2 + \alpha' + 4\alpha\alpha_t
$$

(two planes with the other 3-space directions, one with $x_4$, four with the block);

$$
R^4{}_4 = 3(\alpha^2 + \alpha') + 4(\alpha_t^2 + \alpha_t')
$$

(three planes with 3-space, four with the block);

$$
R^0{}_0 = R^j{}_j = 3\alpha\alpha_t + (\alpha_t^2 + \alpha_t') + 3(\alpha_t^2 - H^2k) = 3\alpha\alpha_t + 4\alpha_t^2 + \alpha_t' - 3H^2k
$$

(for $x_0$ and for each extra time the same count: three planes with 3-space, one with $x_4$, three with the other block directions). We write the result with $u = b_4'/b_4$ and $v = u'$, so that $\alpha_t = -a_4' + u/2$, $\alpha_t' = -a_4'' + v/2$ and $b_4''/b_4 = v + u^2$ (the quotient rule): with $4\alpha\alpha_t = -4a_4'^2 + 2a_4'u$, $4\alpha_t^2 = 4a_4'^2 - 4a_4'u + u^2$ and $3\alpha\alpha_t = -3a_4'^2 + \frac32 a_4'u$ (the products multiplied out),

$$
R^i{}_i = -a_4'^2 + a_4'' + 2a_4'u, \qquad R^4{}_4 = 7a_4'^2 - a_4'' - 4a_4'u + u^2 + 2v ,
$$

$$
R^0{}_0 = R^j{}_j = a_4'^2 - a_4'' - \tfrac52 a_4'u + u^2 + \tfrac12 v - 3H^2k
$$

(collect equal terms: for example in $R^4{}_4$, $3a_4'^2 + 4a_4'^2 = 7a_4'^2$ and $3a_4'' - 4a_4'' = -a_4''$).

**No entries off the diagonal.** An entry $R^a{}_b = \sum_c R^{ac}{}_{bc}$ with $a \ne b$ needs a non-zero component whose upper pair $(a, c)$ and lower pair $(b, c)$ differ in one index. Every non-zero component of Section 3.24 has the same two indices up and down, so there is none: **the Ricci tensor is diagonal, for all functions $a_4$ and $b_4$ and every real $z$** (PROVED), and so is the Einstein tensor below.

**The Ricci scalar.** It is the sum of the diagonal, or twice the sum of the 28 plane curvatures (Section 3.17):

$$
R = 3R^i{}_i + R^4{}_4 + 4R^0{}_0 = 8a_4'^2 - 2a_4'' - 8a_4'u + 5u^2 + 4v - 12H^2k
$$

(collect: $-3 + 7 + 4 = 8$ times $a_4'^2$, $3 - 1 - 4 = -2$ times $a_4''$, $6 - 4 - 10 = -8$ times $a_4'u$, $1 + 4 = 5$ times $u^2$, $2 + 2 = 4$ times $v$, and $-12$ times $H^2k$). With $4v = 4b_4''/b_4 - 4u^2$ this is the record's `ricciScalar`, $8a_4'^2 - 2a_4'' - 8a_4'b_4'/b_4 + 4b_4''/b_4 + (b_4'/b_4)^2 - 12H^2e^{2a_4}/b_4$.

**The Einstein tensor: the planes that do not contain the direction.** $G^a{}_b = R^a{}_b - \tfrac12\delta^a{}_bR$. On the diagonal, $R^a{}_a$ is the sum of the planes that contain $x_a$ and $\tfrac12 R$ is the sum of all 28 planes, so

$$
G^a{}_a = \sum_{\text{planes through } x_a}\sigma - \sum_{\text{all planes}}\sigma = -\sum_{\text{planes without } x_a}\sigma
$$

(no sum over $a$; the planes through $x_a$ cancel). So:

$$
G^4{}_4 = -\bigl[3\alpha^2 + 12\alpha\alpha_t + 6(\alpha_t^2 - H^2k)\bigr] = 3a_4'^2 - \tfrac32 u^2 + 6H^2k
$$

(the 21 planes without $x_4$: three inside 3-space, twelve of 3-space with the block, six inside the block; with $-12\alpha\alpha_t = 12a_4'^2 - 6a_4'u$ and $-6\alpha_t^2 = -6a_4'^2 + 6a_4'u - \frac32 u^2$, the terms with $a_4'u$ cancel);

$$
G^i{}_i = -\bigl[\alpha^2 + 2(\alpha^2 + \alpha') + 8\alpha\alpha_t + 4(\alpha_t^2 + \alpha_t') + 6(\alpha_t^2 - H^2k)\bigr] = 2a_4'' - 5a_4'^2 + 6a_4'u - \tfrac52 u^2 - 2v + 6H^2k
$$

(the 21 planes without $x_i$: one inside 3-space, two of the other 3-space directions with $x_4$, eight of them with the block, four of the block with $x_4$, six inside the block; multiplied out with the same products, $-3 + 8 - 10 = -5$ times $a_4'^2$, $-4 + 10 = 6$ times $a_4'u$, $-2 + 4 = 2$ times $a_4''$);

$$
G^0{}_0 = -\bigl[3\alpha^2 + 3(\alpha^2 + \alpha') + 9\alpha\alpha_t + 3(\alpha_t^2 + \alpha_t') + 3(\alpha_t^2 - H^2k)\bigr] = -3a_4'^2 + \tfrac32 a_4'u - \tfrac32 u^2 - \tfrac32 v + 3H^2k
$$

(the 21 planes without $x_0$: three inside 3-space, three of 3-space with $x_4$, nine of 3-space with the extra times, three of the extra times with $x_4$, three inside the extra times; $-6 + 9 - 6 = -3$ times $a_4'^2$, $-\frac92 + 6 = \frac32$ times $a_4'u$, $-3 + 3 = 0$ times $a_4''$). The planes without an extra time $x_j$ are of the same five kinds and numbers as those without $x_0$ (exchange $x_0$ and $x_j$, both block directions), so

$$
G^j{}_j = G^0{}_0 .
$$

**The hidden component of the Einstein tensor equals the extra-time components** (PROVED). With $v + u^2 = b_4''/b_4$, the hidden component reads $G^0{}_0 = 3H^2e^{2a_4}/b_4 - 3a_4'^2 + \frac32 a_4'b_4'/b_4 - \frac32 b_4''/b_4$. These are exactly the entries `ricciMixed`, `ricciScalar` and `einsteinMixed` of the record `curvature.json` (PROVED here; Notebook 03b reproduces all 64 + 64 + 1 of them, In [17]; record check `rust_ricci_einstein_scalar_agree` of `python-lovelock-report.json`). They are also the key `einstein_diagonal` of the record `warped-metric.json` and the components of the record `a4-equations.json` (its report `Revision/field_equations_a4/reports/python-a4-report.json`, check `einstein_components`). The lead's independent check states the same properties for every $b_4$ (record `einstein-gauss-bonnet-a4.json`, checks `einstein_off_diagonal_vanish`, `einstein_diagonal_x0_independent` and `einstein_isotropy`): no entry off the diagonal, no diagonal entry depending on $x_0$, the three 3-space entries equal, and the hidden entry equal to the three extra-time entries (Notebook 03b, In [20]). $G^4{}_4$ contains no second derivative ($a_4''$ and $v$ cancelled): it will be a first-order condition on the history, the **constraint** of the field equations (`python-a4-report.json`, check `constraint_first_order`). Subtracting the $x_4$ entry from the hidden one,

$$
G^0{}_0 - G^4{}_4 = -6a_4'^2 + \tfrac32 a_4'u - \tfrac32 v - 3H^2k = -\tfrac32\bigl(2H^2k + 4a_4'^2 - a_4'u + v\bigr)
$$

(the terms $\pm\frac32 u^2$ cancel; then $-\frac32$ is taken out), which Section 3.26 uses (lead check `einstein_null_energy`; Notebook 03b, In [20]).

**On the history.** For $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{4AHx_4/3}$ ($a_4' = AH$, $a_4'' = 0$, $u = \frac43 AH$, $v = 0$, $k = e^{2a_4/3}$ with $b_4(0) = 1$):

$$
G^4{}_4 = \Bigl(6k + \frac13 A^2\Bigr)H^2, \qquad G^i{}_i = \Bigl(6k - \frac{13}{9}A^2\Bigr)H^2, \qquad G^0{}_0 = G^j{}_j = \Bigl(3k - \frac{11}{3}A^2\Bigr)H^2 ,
$$

$$
R = \Bigl(\frac{56}{9}A^2 - 12k\Bigr)H^2
$$

(each formula with the history put in; for example $G^0{}_0 = -3A^2 + \frac32 A\cdot\frac43 A - \frac32\cdot\frac{16}{9}A^2 + 3k = -3A^2 + 2A^2 - \frac83 A^2 + 3k$ times $H^2$, and $R = 8A^2 - \frac{32}{3}A^2 + \frac{80}{9}A^2 - 12k$ times $H^2$). Every entry grows with $k$, which grows along the history like $e^{2AHx_4/3}$: the curvature of the shrinking block. At the canonical slope $A = 1$ on the first slice ($k = 1$) the diagonal of $G$ is $(-\frac23, \frac{41}{9}, \frac{41}{9}, \frac{41}{9}, \frac{19}{3}, -\frac23, -\frac23, -\frac23)H^2$ in the order $x_0, \dots, x_7$ and $R = -\frac{52}{9}H^2$ (Notebook 03b, In [24] and In [25]).

**The Kretschmann scalar.** In $K = \sum_{a,b,c,d} R^{ab}{}_{cd}R^{cd}{}_{ab}$ each component is multiplied by its partner with the two pairs exchanged. The four components of a plane are their own partners or each other's, and each of the four products is $\sigma(a, b)^2$ (Section 3.17); there are no other components. Therefore

$$
K = 4\sum_{\text{planes}}\sigma(a, b)^2 = 4\Bigl[3\alpha^4 + 3(\alpha^2 + \alpha')^2 + 12\alpha^2\alpha_t^2 + 4(\alpha_t^2 + \alpha_t')^2 + 6(\alpha_t^2 - H^2k)^2\Bigr]
$$

(the table of Section 3.24, each kind of plane with its number). It does not depend on $z$, and it is a sum of squares: $K \ge 0$, and $K = 0$ exactly when all 28 plane curvatures vanish. That happens on the **flat member** $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ with a constant $c$: there $\alpha = \alpha' = 0$, $\alpha_t = b_4'/(2b_4) = 1/(x_4 - c)$, $\alpha_t' = -1/(x_4 - c)^2$, so $\alpha_t^2 + \alpha_t' = 0$, and $H^2k = H^2/b_4 = 1/(x_4 - c)^2 = \alpha_t^2$ (all 28 values zero; record `Revision/metric_warped/reports/python-warped-metric-report.json`, check `milne_flat_check`, and lead check `einstein_flat_vacuum`; Notebook 03b, In [20] and In [22]). It is flat eight-dimensional space written in unusual coordinates, a check of the formulas, not a physical history: 3-space does not expand. On the history ($\alpha = AH$, $\alpha' = 0$, $\alpha_t = -\frac13 AH$, $\alpha_t' = 0$), in units of $H^4$,

$$
K = 4\Bigl[3A^4 + 3A^4 + \frac{12}{9}A^4 + \frac{4}{81}A^4 + 6\Bigl(\frac{A^2}{9} - k\Bigr)^2\Bigr] = \frac{2416}{81}A^4 - \frac{16}{3}A^2k + 24k^2
$$

(the squares expanded: $6(\frac{A^2}{9} - k)^2 = \frac{6}{81}A^4 - \frac43 A^2k + 6k^2$; then $3 + 3 + \frac43 + \frac{4}{81} + \frac{6}{81} = \frac{604}{81}$, and $4 \cdot \frac{604}{81} = \frac{2416}{81}$). It is positive for every slope, because the block term $6(\frac{A^2}{9} - k)^2$ and the 3-space term $3A^4$ cannot vanish together when $k > 0$: **along the history the metric is curved everywhere** (PROVED; Notebook 03b computes $K$ a second time from the 112 components of the record, In [22], sums it numerically at 300 values of $z$, In [23], and evaluates it on the history, In [24]). For the canonical $A = 1$ on the first slice, $K = \frac{2416}{81} - \frac{16}{3} + 24 = 48.49$ in units of $H^4$.

**The contracted Bianchi identity.** For every metric the Einstein tensor has zero **divergence**, $\sum_\mu \nabla_\mu G^\mu{}_\nu = 0$ for each $\nu$ (the divergence is the covariant derivative with its index $\mu$ set equal to the upper index of $G$ and summed; a standard theorem, the **contracted Bianchi identity**; quoted, ASSUMED in general). For the corrected metric we prove it directly. By the rule of Section 3.15 (one $+\Gamma$ for the upper index, one $-\Gamma$ for the lower one, then the upper index contracted with the derivative),

$$
\sum_\mu \nabla_\mu G^\mu{}_\nu = \sum_\mu\partial_\mu G^\mu{}_\nu + \sum_{\mu,\lambda}\Gamma^\mu{}_{\mu\lambda}G^\lambda{}_\nu - \sum_{\mu,\lambda}\Gamma^\lambda{}_{\mu\nu}G^\mu{}_\lambda .
$$

$G$ is diagonal, so the first sum keeps $\mu = \nu$, the second $\lambda = \nu$ and the third $\lambda = \mu$:

$$
\sum_\mu \nabla_\mu G^\mu{}_\nu = \partial_\nu G^\nu{}_\nu + \sum_\mu\Gamma^\mu{}_{\mu\nu}\bigl(G^\nu{}_\nu - G^\mu{}_\mu\bigr)
$$

(no sum over $\nu$; the two sums over $\mu$ combined). For $\nu = x_0$: $G^0{}_0$ does not depend on $x_0$, and the symbols $\Gamma^\mu{}_{\mu0}$ are non-zero only for $\mu = x_0$ (with the factor $G^0{}_0 - G^0{}_0 = 0$) and for the extra times (with the factor $G^0{}_0 - G^j{}_j = 0$): the divergence vanishes because the hidden and the extra-time entries are equal. For $\nu$ one of $x_1, x_2, x_3, x_5, x_6, x_7$: nothing depends on $x_\nu$ and every $\Gamma^\mu{}_{\mu\nu}$ is zero (case (b) of Section 3.15 gives $\partial_\nu\ln h_\mu = 0$). For $\nu = x_4$, with $\Gamma^i{}_{i4} = \alpha$ and $\Gamma^0{}_{04} = \Gamma^j{}_{j4} = \alpha_t$ and $G^j{}_j = G^0{}_0$,

$$
\sum_\mu \nabla_\mu G^\mu{}_4 = \partial_4 G^4{}_4 + 3\alpha\bigl(G^4{}_4 - G^i{}_i\bigr) + 4\alpha_t\bigl(G^4{}_4 - G^0{}_0\bigr) .
$$

The three terms, line by line. First, with $\partial_4 k = k\,(2a_4' - u)$ (the derivative of $\ln k = 2a_4 - \ln b_4$) and $\partial_4 u = v$,

$$
\partial_4 G^4{}_4 = 6a_4'a_4'' - 3uv + 12H^2ka_4' - 6H^2ku
$$

(the chain rule on each term of $G^4{}_4 = 3a_4'^2 - \frac32 u^2 + 6H^2k$). Second, $G^4{}_4 - G^i{}_i = 8a_4'^2 - 2a_4'' - 6a_4'u + u^2 + 2v$ (the two entries subtracted; the terms $6H^2k$ cancel), so

$$
3\alpha\bigl(G^4{}_4 - G^i{}_i\bigr) = 24a_4'^3 - 6a_4'a_4'' - 18a_4'^2u + 3a_4'u^2 + 6a_4'v .
$$

Third, $G^4{}_4 - G^0{}_0 = \frac32(2H^2k + 4a_4'^2 - a_4'u + v)$ (above) and $4\alpha_t = -4a_4' + 2u$, so

$$
4\alpha_t\bigl(G^4{}_4 - G^0{}_0\bigr) = -24a_4'^3 + 18a_4'^2u - 3a_4'u^2 - 6a_4'v + 3uv - 12H^2ka_4' + 6H^2ku
$$

(the product multiplied out term by term). Adding the three lines, every term cancels against one of the opposite sign: $6a_4'a_4''$ against $-6a_4'a_4''$, $-3uv$ against $3uv$, $12H^2ka_4'$ against $-12H^2ka_4'$, $-6H^2ku$ against $6H^2ku$, $24a_4'^3$, $-18a_4'^2u$, $3a_4'u^2$ and $6a_4'v$ against their negatives. So $\sum_\mu \nabla_\mu G^\mu{}_\nu = 0$ for all eight $\nu$ and all functions $a_4(x_4)$, $b_4(x_4)$ (PROVED; Notebook 03b, In [21]; record `Revision/gkd_lovelock/results/lovelock-report.json`, checks `k1_equals_minus_4_einstein` and `k1_divergence_free`; `python-a4-report.json`, check `bianchi_x4`). The same computation for a diagonal energy-momentum tensor $T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ whose entries may depend on $x_4$ and $x_0$ gives

$$
\sum_\mu \nabla_\mu T^\mu{}_4 = -\partial_4\rho - 3a_4'(\rho + p_3) - 3\alpha_t(\rho + p_t) - \alpha_t(\rho + p_0), \qquad \sum_\mu \nabla_\mu T^\mu{}_0 = \partial_0 p_0 + 3H\cot z\,(p_0 - p_t)
$$

(the two formulas above with $G$ replaced by $T$, $T^4{}_4 = -\rho$; in the $x_0$ component $\partial_0 p_0$ stays and $p_0 - p_t$ need not vanish): each expanding or shrinking direction changes $\rho$ in proportion to $\rho$ plus its own pressure, at the rate $a_4'$ for 3-space and $\alpha_t$ for each block direction, and a source whose entries do not depend on $x_0$ is conserved along $x_0$ only if $p_0 = p_t$ (the lead's record `emt-divergence-and-spin-connection.json`, checks `divergence_x4_component` and `divergence_x0_component`, and the record `python-warped-metric-report.json`, check `divergence_of_diagonal_tensor`; Chapter 9 derives and uses them).

### 3.26 What Einstein's equations ask of the source

**Einstein's field equations.** In Einstein's theory of gravity the curvature is tied to the matter by

$$
G^\mu{}_\nu + \Lambda\,\delta^\mu{}_\nu = \kappa\,T^\mu{}_\nu ,
$$

with a positive constant $\kappa$ (the strength of gravity), a constant $\Lambda$ (the **cosmological constant**) and the **energy-momentum tensor** $T^\mu{}_\nu$ of the matter, whose diagonal for the sources of this book is $\mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ in the order $x_0, \dots, x_7$: the **energy density** $\rho$ and the **pressures** $p_0$ of the hidden direction, $p_3$ of 3-space and $p_t$ of the extra times. We take this form of the equations as given here (ASSUMED in this chapter); Chapter 9 derives $T$ for the fields of the book, and Chapter 12 derives the equations, together with their higher-order Lovelock companions, and solves them. (The **Lovelock tensors** are curvature tensors built from products of one, two or three Riemann tensors with the generalized Kronecker delta of Chapter 1; the first of them is a multiple of the Einstein tensor, $P_{(1)} = -4G$; Chapters 11 and 12 treat them in full.) Why does the left side have this form? The conservation of energy and momentum demands that the right side has zero divergence, $\sum_\mu \nabla_\mu T^\mu{}_\nu = 0$, so the left side must have zero divergence for every metric. The contracted Bianchi identity of Section 3.25 shows that the Einstein tensor has this property, and $\Lambda\,\delta^\mu{}_\nu$ has it too (its covariant derivative is zero, by the rule of Section 3.15 with constant entries, because the $+\Gamma$ and the $-\Gamma$ term cancel). The Einstein tensor is the simplest curvature tensor with zero divergence, but not the only one: in eight dimensions the second and the third Lovelock tensors also have zero divergence for every metric (record `Revision/gkd_lovelock/results/lovelock-report.json`, checks `k2_divergence_free` and `k3_divergence_free`), and the field equations of the Revision record use all three, $\sum_{k=1}^{3}\alpha_k E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu{}_\nu = \kappa\,T^\mu{}_\nu$ with $E_{(1)} = G$ (record `Revision/field_equations_a4/a4-equations.json`, key `conventions.fieldEquations`). This chapter uses only the simplest case, Einstein's equations ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$).

**A diagonal source suffices, and it needs $p_0 = p_t$.** The Einstein tensor of the corrected metric has no entry off the diagonal (Section 3.25), so the off-diagonal components of the equations read $0 = \kappa T^\mu{}_\nu$ for $\mu \ne \nu$: the source must be diagonal, and a diagonal source is enough. The same holds for all three Lovelock tensors (record `Revision/metric_warped/reports/python-warped-metric-report.json`, check `corrected_offdiagonal_all_orders`; `python-a4-report.json`, check `independent_components`). The hidden and the extra-time entries of $G$ are equal, so the $x_0$ and $x_5$ components give $\kappa p_0 = G^0{}_0 + \Lambda = G^5{}_5 + \Lambda = \kappa p_t$: **the hidden pressure must equal the extra-time pressure**; and no entry of $G$ depends on $x_0$, so neither may the source. These are the conditions under which the field equations become ordinary differential equations in $x_4$ (Chapter 12). (The metric of 2026-10-14 needed instead an off-diagonal source component, which is why it was withdrawn; Notebook 03b computes this as its negative control, In [27].)

**The equations for the corrected metric.** With the Einstein tensor of Section 3.25, written with $u = b_4'/b_4$ and $v = u'$, the three independent diagonal components are

$$
3a_4'^2 - \tfrac32 u^2 + 6H^2k + \Lambda = -\kappa\rho, \qquad 2a_4'' - 5a_4'^2 + 6a_4'u - \tfrac52 u^2 - 2v + 6H^2k + \Lambda = \kappa p_3,
$$

$$
-3a_4'^2 + \tfrac32 a_4'u - \tfrac32 u^2 - \tfrac32 v + 3H^2k + \Lambda = \kappa p_0 = \kappa p_t
$$

(the $x_4$ component uses $T^4{}_4 = -\rho$; the others $T^\mu{}_\mu = p_\mu$). These are the components `einstein.constraint_x4`, `einstein.space_x1` and `einstein.hidden_x0` of the record `a4-equations.json` (lead checks `einstein_constraint_x4`, `einstein_space_x1`, `einstein_hidden_x0`). The first contains only first derivatives (the constraint); the other two contain $a_4''$ and $v$, which they determine.

**What the history asks.** Subtracting the $x_4$ equation from the $x_0$ equation gives (Section 3.25)

$$
\kappa(\rho + p_0) = G^0{}_0 - G^4{}_4 = -\tfrac32\bigl(2H^2k + 4a_4'^2 - a_4'u + v\bigr)
$$

(record `python-a4-report.json`, check `einstein_null_combinations`; lead check `einstein_null_energy`). For $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{4AHx_4/3}$ ($a_4' = AH$, $a_4'' = 0$, $u = \frac43 AH$, $v = 0$) the three equations give, with the entries of Section 3.25,

$$
\kappa\rho = -\Bigl(6k + \frac{A^2}{3}\Bigr)H^2 - \Lambda, \qquad \kappa p_3 = \Bigl(6k - \frac{13}{9}A^2\Bigr)H^2 + \Lambda, \qquad \kappa p_0 = \kappa p_t = \Bigl(3k - \frac{11}{3}A^2\Bigr)H^2 + \Lambda
$$

(each equation solved for its source entry), with $k = e^{2AHx_4/3}$ ($b_4(0) = 1$). The source is diagonal, has $p_0 = p_t$, does not depend on $x_0$, and grows with $k$, the curvature of the shrinking block. These are the entries `rho`, `p3`, `p0` and `pt` of the key `exponentialHistory.requiredSource` of the record `Revision/field_equations_a4/a4-equations.json`, with the couplings of Einstein's equations ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$) and $\beta = 4/3$ put in, and for $A = 1$ the key `history_source.einstein_A1_beta43` of `Revision/metric_warped/results/warped-metric.json`, which writes them as functions of $x_4$: $-\kappa\rho - \Lambda = \frac13 H^2(18e^{2Hx_4/3} + 1)$, $\kappa p_3 - \Lambda = \frac19 H^2(54e^{2Hx_4/3} - 13)$, $\kappa p_0 - \Lambda = \kappa p_t - \Lambda = \frac13 H^2(9e^{2Hx_4/3} - 11)$ (PROVED here; Notebook 03b reads the texts of both records and checks them against its Einstein tensor, In [26]). The source is conserved: by Section 3.25 the divergence of $T$ is that of $(G + \Lambda\delta)/\kappa$, which vanishes (`Revision/metric_warped/reports/python-warped-metric-report.json`, check `history_source_conserved`). For the canonical $A = 1$, $H = 1$ on the first slice ($k = 1$): $\kappa\rho = -\frac{19}{3} - \Lambda$, $\kappa p_3 = \frac{41}{9} + \Lambda$ and $\kappa p_0 = \kappa p_t = -\frac23 + \Lambda$.

**No exponential history is empty.** Without matter, $T = 0$, every entry of $G + \Lambda\delta$ vanishes, so $G^4{}_4 = G^0{}_0$ and $G^4{}_4 = G^i{}_i$. On an exponential history with a general exponent $\beta$ ($u = \beta AH$, $v = 0$) the first condition reads $\frac32(2k + 4A^2 - \beta A^2)H^2 = 0$, that is $k = A^2(\beta - 4)/2$, which is negative for $\beta = 4/3$, while $k = e^{2a_4}/b_4 > 0$. So the history of this book is not a solution of Einstein's equations without matter, for any $\Lambda$ (PROVED; lead check `einstein_no_exponential_vacuum`, which treats every $\beta$; `python-a4-report.json`, check `einstein_no_exponential_vacuum`). The flat member of Section 3.25 is the empty solution with $\Lambda = 0$ (lead check `einstein_flat_vacuum`).

**What this means, with its status.** Ordinary matter (dust, radiation, a gas) has $\rho + p \ge 0$ for each of its pressures $p$; this is the **null energy condition** (a standard condition of physics, used here as the definition of "ordinary", ASSUMED). Within Einstein's equations, the deflating history needs $\kappa(\rho + p_0) = \kappa(\rho + p_t) = -(3k + 4A^2)H^2$ and $\kappa(\rho + p_3) = -\frac{16}{9}A^2H^2$ (the entries above added; $\Lambda$ cancels), both negative for every slope $A \ne 0$, every slice and every $\Lambda$: whatever fills such a spacetime, it is not ordinary matter (PROVED). Three things are NOT shown here: whether a field of this book can supply such a source (Chapters 9, 12 and 17 answer this; the Kohn-Sham states computed along the history cannot, `Revision/field_equations_a4/reports/ks-source-conditions.json`, which is why the history is a PRESCRIBED BACKGROUND, Section 3.8); what the higher-order Lovelock terms change (Chapter 12; with the author's weights the required source is again diagonal with $p_0 = p_t$ and grows with $k$, record `a4-equations.json`, key `exponentialHistory.authorWeights.historySource_kappaT_minus_Lam`); and anything about pairs of universes or about matter and antimatter, which this chapter does not touch.

### 3.27 Example: the curvature of the author's metric

Notebook 03b does Sections 3.23 to 3.26 by computer algebra, for general functions $a_4(x_4)$ and $b_4(x_4)$ and every real $z$. It reads the metric exactly as the record stores it, with the warp factor as a sympy function that knows its derivative; computes all 512 Christoffel symbols with the formula of Section 3.15 and compares the 21 non-zero ones with the record; draws them; checks them a second way by finite differences at the test point of the record's brute-force check; checks that observers at rest fall freely; computes the 112 non-zero Riemann components, checks their symmetries and the first Bianchi identity, shows that none depends on $z$ and that all are plane curvatures, and compares every one with the record; computes the 28 plane curvatures and the relative acceleration of observers at rest; computes the Ricci tensor, the Ricci scalar and the Einstein tensor and compares them with the record, with the first Lovelock scalar of the record of the field equations and with the lead's checks; compares 262 components with the record numerically with 30 digits at the record's five test points; checks the contracted Bianchi identity; computes the Kretschmann scalar; evaluates everything along the deflating history ($a_4 = AHx_4$, $b_4 = b_4(0)\,e^{4AHx_4/3}$); reproduces the source of Section 3.26 from two records; and repeats the curvature for the negative control, the withdrawn metric of 2026-10-14. It needs no Rust, runs in about 1 minute (the cells with the Riemann tensor and the negative control take up to half a minute each) and ends with the line ALL 43 CHECKS PASSED (notebook 03b).

<!-- NOTEBOOK 03b -->

### 3.30 Line-by-line walk-through of Notebook 03b

The notebook has 28 code cells, In [1] to In [28]. As before, a line or a small group of lines is quoted and then explained, and a line `...` in a quoted figure command stands for the remaining lines of the caption, printed in full under its figure in Section 3.29.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 3.28. Its code is, line for line, the set-up code of Notebook 03a explained in Section 3.13 under In [1], with the single difference `NOTEBOOK_ID = "03b"  # this notebook: chapter 03, example b`. It prints Set-up of notebook 03b complete: repository folder found, helpers defined.

**In [2], every result in one piece.** Word for word In [2] of Notebook 03a (Section 3.13). It prints From now on check and report print each of their results in one piece.

**In [3], packages, record, symbols and the warp factor.**

```python
import itertools  # loops over all index combinations

import mpmath  # numbers with many digits
import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols
from sympy.parsing.sympy_parser import (implicit_multiplication, parse_expr,
                                        standard_transformations)
```

The packages: `itertools` for loops over indices (Section 3.22), `mpmath` for numbers with many digits (used in In [19]), numpy, sympy, and the text reader `parse_expr` of sympy with its two reading rules (Section 3.13, In [3] and In [5]).

```python
CURVATURE_RECORD = "Revision/gkd_lovelock/results/curvature.json"
record = json.loads(repository_file(CURVATURE_RECORD).read_text(encoding="utf-8"))
PYTHON_REPORT = "Revision/gkd_lovelock/results/python-lovelock-report.json"  # sympy
RUST_REPORT = "Revision/gkd_lovelock/results/lovelock-report.json"  # the Rust checks
```

The record of the Rust program `lovelock_gkd` is read into the dictionary `record`. `PYTHON_REPORT` and `RUST_REPORT` are the names of two further Revision reports: the report of the independent sympy checker and the report of the Rust program's own checks.

```python
def record_check(report_file, check_name, detail_part=""):
    """Return True when the Revision report report_file lists the check check_name
    as passed (and its detail contains detail_part); otherwise stop the notebook."""
    checks = json.loads(repository_file(report_file).read_text(encoding="utf-8"))
    checks = checks["checks"]  # a dictionary or a list, depending on the report
    if isinstance(checks, dict):  # {name: {"passed": true, "detail": ...}}
        entry = checks.get(check_name, {})
        passed = entry.get("passed") is True
    else:  # [{"name": ..., "verdict": "PASS", "detail": ...}, ...]
        entry = next((e for e in checks if e.get("name") == check_name), {})
        passed = entry.get("verdict") == "PASS"
    if not passed or detail_part not in entry.get("detail", ""):
        raise AssertionError(f"record check failed: {report_file} does not list "
                             f"{check_name} as passed")
    return True
```

The function `record_check` is the one of Notebook 03a, explained line by line in Section 3.13 under In [3]: it reads a Revision report, finds the check `check_name` in either of the two layouts of the reports (a dictionary from names to entries with the key `passed`, or a list of entries with a `name` and a `verdict`), and stops the notebook with an `AssertionError` unless the check passed and, when `detail_part` is given, its detail contains that text. So whenever this notebook says that a number agrees with a Revision record, it also confirms, from the record itself, that the record's own check of that number passed.

```python
x0, x1, x2, x3, x4, x5, x6, x7 = sp.symbols("x0:8", real=True)
X = [x0, x1, x2, x3, x4, x5, x6, x7]  # the coordinates, counted 0 to 7 in Python
NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
H = sp.symbols("H", positive=True)  # the constant of the author
a4 = sp.Function("a4")(x4)  # the metric function a4, unknown
b4 = sp.Function("b4", positive=True)(x4)  # the metric function b4 > 0, unknown
```

The eight coordinates, their list `X` and their printed names `NAMES`, in the author's order, so that `X[k]` is $x_k$ and `NAMES[k]` is `"xk"`; the constant $H > 0$; and the unknown functions $a_4(x_4)$ and $b_4(x_4)$, the second declared positive.

```python
class W(sp.Function):
    """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

    def fdiff(self, argindex=1):
        """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
        return H * sp.cot(6 * H * self.args[0]) * self
```

The warp factor $W(x_0) = (\sin^2 z)^{1/12}$ is not written out with a sine; it is a new sympy **function class** named `W`. A **class** describes a kind of object; `class W(sp.Function):` makes a new kind of sympy function that behaves like every other one (sympy can multiply it, take powers of it, substitute into it), and the indented `def` inside the class adds one rule of its own. The method `fdiff` (the name sympy looks for) tells sympy the derivative of `W(x0)` with respect to its argument: `self` is the expression `W(x0)` itself and `self.args[0]` is its argument $x_0$, so the rule is $dW/dx_0 = H\cot(6Hx_0)\,W$, the formula of Section 3.23 ($\partial_0\ln W = H\cot z$). With this rule every derivative that the notebook takes is valid for every real $z$ with $\sin z \ne 0$ at once: sympy never has to decide the sign of $\sin z$.

```python
G = sp.symbols("G", real=True)  # the sign of cot z: +1 or -1, |cot z| = G cot z
a4p, a4pp, a4v = sp.symbols("a4p a4pp a4v", real=True)  # a4 prime, a4 two primes, a4
b4p, b4pp = sp.symbols("b4p b4pp", real=True)  # b4 prime, b4 two primes
b4v, w = sp.symbols("b4v w", positive=True)  # the value of b4, the warp factor
z = sp.symbols("z", real=True)  # z = 6 H x0, every real value, for printing
```

`G` stands for the sign of $\cot z$ ($+1$ or $-1$; $|\cot z| = G\cot z$), which appears in the record's volume factor; it is constant on each quarter of the period, so its derivatives are zero. Then the plain symbols used for printing: `a4p` for $a_4'$, `a4pp` for $a_4''$, `a4v` for the value of $a_4$, the same three for $b_4$, `w` for the warp factor (positive) and `z` for $6Hx_0$, declared real (it takes every real value).

```python
def symbolic(expression):
    """Write the derivatives of a4 and b4 as a4p, a4pp, b4p, b4pp and the values
    a4(x4), b4(x4) as a4v, b4v."""
    expression = expression.subs(sp.Derivative(a4, (x4, 2)), a4pp)  # second first
    expression = expression.subs(sp.Derivative(b4, (x4, 2)), b4pp)
    expression = expression.subs(sp.Derivative(a4, x4), a4p).subs(a4, a4v)
    return expression.subs(sp.Derivative(b4, x4), b4p).subs(b4, b4v)
```

`symbolic` replaces the second derivatives of $a_4$ and $b_4$ (written `sp.Derivative(a4, (x4, 2))` and `sp.Derivative(b4, (x4, 2))`) by `a4pp` and `b4pp`, then the first derivatives by `a4p` and `b4p`, then the functions themselves by `a4v` and `b4v`. The second derivative is replaced first, because replacing the first derivative first could also change the second one (which is the derivative of the first).

```python
def plain(expression):
    """As symbolic, with W(x0) written as w and 6 H x0 written as z."""
    return symbolic(expression).subs(W(x0), w).subs(x0, z / (6 * H))


say("Record read; symbols x0 ... x7, H, a4(x4), b4(x4), W(x0), G, a4p, a4pp, a4v, "
    "b4p, b4pp, b4v, w and z defined.")
```

`plain` does the same and also writes `W(x0)` as `w` and $6Hx_0$ as $z$; `symbolic` keeps $x_0$ and `W(x0)`, because the record writes its components with $x_0$. The last line prints the output of In [3].

**In [4], the metric from the record's text.**

```python
# the metric exactly as the record stores it, without the note in brackets after it
text = record["metricAsGiven"].split("}} ", 1)[0] + "}}"
text = text.replace("(Sin[6 H x0]^2)^(1/6)", "W(x0)^2")  # the warp factor squared
text = text.replace("exp^", "E^").replace("a4[x4]", "a4").replace("b4[x4]", "b4")
text = text.replace("Sin[6 H x0]", "sin(6 H x0)").replace("Cot[6 H x0]", "cot(6 H x0)")
text = text.replace("{", "[").replace("}", "]").replace("^", "**")
metric_names = {"E": sp.E, "a4": a4, "b4": b4, "H": H, "x0": x0, "sin": sp.sin,
                "cot": sp.cot, "W": W}
g = sp.Matrix(parse_expr(text, local_dict=metric_names, transformations=(
    standard_transformations + (implicit_multiplication,))))
```

The first line cuts the record's text at the first `}}` followed by a blank, as Notebook 03a does (Section 3.13, In [3]): `[0]` keeps the matrix, without the note in brackets, and `+ "}}"` puts back its two closing braces. The second line is the new rule, applied before all others: the positive root `(Sin[6 H x0]^2)^(1/6)` becomes `W(x0)^2`, the square of the warp factor. Then the same translation of the Mathematica text as in Notebook 03a (Section 3.13, In [5]): `exp^` becomes `E^`, `a4[x4]` becomes `a4` and `b4[x4]` becomes `b4`, the square brackets of the sine and the cotangent become round ones, the braces of lists become square brackets and `^` becomes `**`. The dictionary `metric_names` says what each name means (`W` is the function class of In [3]), and `parse_expr` with implicit multiplication reads the text; `sp.Matrix` makes the exact $8 \times 8$ matrix `g`.

```python
for k in range(8):
    say(f"  g[{NAMES[k]}, {NAMES[k]}] = {plain(g[k, k])}")
check(all(g[i, j] == 0 for i in range(8) for j in range(8) if i != j)
      and not any(g[k, k].has(sp.sin) for k in range(8)),
      "the metric read from the text of the record is diagonal, with the warp W")
```

The eight diagonal entries are printed with `plain`, in the order $x_0, \dots, x_7$. The first is `b4v*exp(-2*a4v)*cot(z)**2`, that is $e^{-2a_4}b_4\cot^2 z$; the next three are `exp(2*a4v)`, that is $e^{2a_4}$; then comes `-1`; the last three are `-b4v*w**2*exp(-2*a4v)`, that is $-e^{-2a_4}b_4W^2$. The check requires the 56 entries off the diagonal to be zero and no entry to contain a sine any more (`.has(sp.sin)`): the warp factor has replaced the root everywhere.

**In [5], reading the record's components.**

```python
record_names = {"a4p": a4p, "a4pp": a4pp, "a4v": a4v, "b4p": b4p, "b4pp": b4pp,
                "b4v": b4v, "H": H, "x0": x0, "E": sp.E, "sin": sp.sin, "cot": sp.cot,
                "W": W, "G": G}
ROOTS = {"(Sin[6*H*x0]^2)^(1/12)": "W(x0)", "(Sin[6*H*x0]^2)^(1/6)": "W(x0)^2",
         "(Sin[6*H*x0]^2)^(1/4)": "W(x0)^3", "Sign[Cot[6*H*x0]]": "G"}
```

The names that may occur in a translated component and what they mean, and the table `ROOTS` of the four pieces of notation that are replaced first: `(Sin[6*H*x0]^2)^(1/12)` is $W$, `^(1/6)` is $W^2$, `^(1/4)` is $W^3$ (these powers occur in the record), and `Sign[Cot[6*H*x0]]` is `G`.

```python
def from_mathematica(entry_text):
    """A component of the record (Mathematica notation) as a sympy expression."""
    t = entry_text
    for root, replacement in ROOTS.items():  # the roots of sin^2 and the sign first
        t = t.replace(root, replacement)
    t = t.replace("Derivative[1][a4][x4]", "a4p")
    t = t.replace("Derivative[2][a4][x4]", "a4pp").replace("a4[x4]", "a4v")
    t = t.replace("Derivative[1][b4][x4]", "b4p")
    t = t.replace("Derivative[2][b4][x4]", "b4pp").replace("b4[x4]", "b4v")
    t = t.replace("Sin[6*H*x0]", "sin(6*H*x0)").replace("Cot[6*H*x0]", "cot(6*H*x0)")
    t = t.replace("^", "**")
    if "[" in t or "]" in t:
        raise ValueError(f"cannot translate {entry_text}")
    return parse_expr(t, local_dict=record_names)
```

The record writes $a_4'$ as `Derivative[1][a4][x4]` and $a_4''$ as `Derivative[2][a4][x4]`, and the same for $b_4$. `from_mathematica` translates a component of the record into sympy: first the four entries of `ROOTS` (the loop `for root, replacement in ROOTS.items()` takes the pairs of the dictionary one after the other), then the two derivatives of $a_4$ become `a4p` and `a4pp` and `a4[x4]` becomes `a4v`, the same for $b_4$ (`b4p`, `b4pp`, `b4v`), the sine and the cotangent get round brackets, `^` becomes `**`. If a square bracket is left, some notation was not translated and the function stops with an error instead of misreading silently.

```python
def tidy(expression):
    """Simplify an expression.  It writes 6 H x0 as z (so that 12 H x0 becomes 2z),
    simplifies it twice, once as it is and once after writing sin(2z) as
    2 sin(z) cos(z) (expand_trig), keeps the shorter result (count_ops counts the
    operations), and writes z as 6 H x0 again."""
    expression = sp.sympify(expression).subs(x0, z / (6 * H))
    first = sp.simplify(expression)
    second = sp.simplify(sp.expand_trig(expression))
    best = second if sp.count_ops(second) < sp.count_ops(first) else first
    return best.subs(z, 6 * H * x0)
```

`tidy` is the simplifier of the notebook. `sp.sympify` turns a plain Python number into a sympy number (so that `.subs` works on it). It writes $6Hx_0$ as $z$, simplifies once directly and once after `sp.expand_trig`, which writes $\sin 2z$ as $2\sin z\cos z$, and keeps the result with fewer operations (`sp.count_ops` counts them); sympy sometimes reaches the simplest form only one of the two ways. At the end $z$ is written as $6Hx_0$ again. The line `best = second if ... else first` chooses one of two values by a condition.

```python
def vanishes(expression):
    """True when the expression simplifies to zero."""
    return tidy(expression) == 0


def same(mine, theirs):
    """True when mine (with the function a4) equals theirs (record symbols)."""
    return vanishes(symbolic(mine) - theirs)
```

`vanishes` is true when an expression simplifies to $0$; `same` compares one of our expressions (written with the functions $a_4$ and $b_4$) with one of the record (written with `a4p`, `a4pp`, `a4v`, `b4p`, `b4pp`, `b4v`): it rewrites ours with `symbolic` and asks whether the difference vanishes.

```python
example = next(e["value"] for e in record["christoffelNonzero_b_le_c"]
               if (e["a"], e["b"], e["c"]) == ("x4", "x5", "x5"))  # Gamma^x4_(x5 x5)
say(f"example of a record entry: {example}")
say(f"translated: {from_mathematica(example)}")
```

The entry of the record's Christoffel list with the indices `a = "x4"`, `b = "x5"`, `c = "x5"` serves as an example: `next(... for e in ... if ...)` runs through the list and takes the first entry whose three indices, compared as one tuple, are these. The output shows it in the record's notation and then its translation, `a4p*b4v*W(x0)**2*exp(-2*a4v) - b4p*W(x0)**2*exp(-2*a4v)/2`: the symbol $\Gamma^{x_4}{}_{x_5x_5} = -\alpha_t\,e^{-2a_4}b_4W^2$ of Section 3.23, the one in which both functions appear.

**In [6], the Christoffel symbols.**

```python
def christoffel(metric, coordinates):
    """All Christoffel symbols Gamma[a][b][c] of a metric, by the formula above."""
    n = len(coordinates)
    inverse = metric.inv()  # the inverse metric g^(ad)
    d_metric = [metric.diff(c) for c in coordinates]  # d_metric[c][i, j] = d_c g_ij
    table = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a, b, c in itertools.product(range(n), repeat=3):
        value = sum(inverse[a, d] * (d_metric[b][d, c] + d_metric[c][d, b]
                                     - d_metric[d][b, c]) for d in range(n)) / 2
        table[a][b][c] = tidy(value)
    return table
```

The same function as in Notebook 03c (Section 3.22, In [3]), with `tidy` instead of `sp.simplify`: the Christoffel formula of Section 3.15 applied to all $8^3 = 512$ index lists, without using the symmetry in $b$ and $c$ (so that the symmetry can be checked). `metric.inv()` is the inverse matrix, and `metric.diff(c)` the matrix of the derivatives of all entries with respect to the coordinate `c`; sympy differentiates `W(x0)` with the rule of In [3].

```python
Gamma = christoffel(g, X)
nonzero = [(a, b, c) for a, b, c in itertools.product(range(8), repeat=3)
           if Gamma[a][b][c] != 0]
upper_half = [(a, b, c) for a, b, c in nonzero if b <= c]
report("non-zero Christoffel symbols (all orders of b, c)", len(nonzero))
report("non-zero Christoffel symbols with b <= c", len(upper_half))
check(all(Gamma[a][b][c] == Gamma[a][c][b]
          for a, b, c in itertools.product(range(8), repeat=3)),
      "the Christoffel symbols are symmetric in their two lower indices")
```

`Gamma` holds the 512 symbols. `nonzero` lists the index triples with a non-zero symbol and `upper_half` those with $b \le c$. The RESULT lines print their numbers, 31 and 21 (Section 3.23), and the check confirms the symmetry in the two lower indices for all 512.

**In [7], the 21 symbols and the record.**

```python
for a, b, c in upper_half:
    say(f"  Gamma^{NAMES[a]}_({NAMES[b]} {NAMES[c]}) = {plain(Gamma[a][b][c])}")
```

The 21 symbols with $b \le c$ are printed, in the author's order of the upper index. sympy writes $\Gamma^{x_0}{}_{x_0x_0} = -6H/(\sin z\cos z)$ as `-12*H/sin(2*z)` (because $\sin 2z = 2\sin z\cos z$), $\Gamma^{x_0}{}_{x_jx_j}$ as `H*w**2*tan(z)`, $\Gamma^{x_4}{}_{x_0x_0}$ as `(-a4p*b4v + b4p/2)*exp(-2*a4v)*cot(z)**2`, and the extra-time and hidden rates as `-a4p + b4p/(2*b4v)`: the list of Section 3.23.

```python
record_gamma = {(NAMES.index(e["a"]), NAMES.index(e["b"]), NAMES.index(e["c"])):
                from_mathematica(e["value"])
                for e in record["christoffelNonzero_b_le_c"]}
check(sorted(record_gamma) == upper_half and len(upper_half) == 21,
      "the same 21 non-zero Christoffel symbols as the record")
```

`record_gamma` is a dictionary built in one expression (a **dictionary comprehension**): for every entry of the record's list it stores the index triple, turned from names into numbers with `NAMES.index`, together with the translated value. The first check requires the same 21 triples in both lists (`sorted` puts the record's keys in the order of `upper_half`).

```python
record_check(PYTHON_REPORT, "rust_christoffels_agree")  # stops if not passed
check(all(same(Gamma[a][b][c], value) for (a, b, c), value in record_gamma.items()),
      "every Christoffel symbol equals the record exactly",
      record=f"{CURVATURE_RECORD}, christoffelNonzero_b_le_c (and "
             "python-lovelock-report.json, check rust_christoffels_agree)")
```

After `record_check` has confirmed that the independent verification of the record passed its own comparison of the Christoffel symbols, the second check requires every one of the 21 symbols to equal the record's exactly (`same`).

**In [8], numerical functions and heat maps of the symbols.**

```python
from matplotlib.colors import LinearSegmentedColormap, SymLogNorm

BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
MAGENTA, GREEN, VIOLET, RED = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
DIVERGING = LinearSegmentedColormap.from_list("blue_grey_red", [BLUE, "#f0efec", RED])
LABELS = [f"$x_{k}$" for k in range(8)]
ARGS = (z, a4v, a4p, H, b4v, b4p)  # the arguments of the numerical functions
```

Two classes of matplotlib (a colour scale built from a list of colours, and the symmetric-logarithmic scale explained below), the palette of Notebook 03a (Section 3.13, In [9]), the two-sided colour scale `DIVERGING`, the axis labels, and the order `ARGS` of the six arguments of the numerical functions below: $z$, $a_4$, $a_4'$, $H$, $b_4$, $b_4'$.

```python
def numeric(expression):
    """A numerical function f(z, a4v, a4p, H, b4v, b4p) of an expression, with the
    warp factor w = |sin z|^(1/6)."""
    value = plain(expression).subs(w, sp.Abs(sp.sin(z)) ** sp.Rational(1, 6))
    return sp.lambdify(ARGS, value, "numpy")
```

`numeric` turns an exact expression into a fast numerical function of the six arguments: it writes the expression with `plain`, replaces the warp factor `w` by $|\sin z|^{1/6}$ (`sp.Abs` is the absolute value), and hands it to `sp.lambdify`.

```python
gamma_functions = {(a, b, c): numeric(Gamma[a][b][c]) for a, b, c in nonzero}
# z, a4, a4p, H, b4, b4p: the slice a4 = 0.5 of the history, b4 = e^(2/3),
# b4' = (4/3) b4 (beta = 4/3, A = 1, H = 1, b4(0) = 1)
B4_SLICE = float(np.exp(2.0 / 3.0))
POINT = (np.pi / 4, 0.5, 1.0, 1.0, B4_SLICE, 4.0 / 3.0 * B4_SLICE)
tables = np.zeros((8, 8, 8))
for (a, b, c), f in gamma_functions.items():
    tables[a, b, c] = f(*POINT)
```

`gamma_functions` holds one numerical function for each of the 31 non-zero symbols. `B4_SLICE` is $e^{2/3}$, the value of $b_4$ on the history at the slice $a_4 = 0.5$, and `POINT` the six arguments of the point of the pictures: $z = \pi/4$, $a_4 = 0.5$, $a_4' = 1$, $H = 1$, $b_4 = e^{2/3}$, $b_4' = \frac43 e^{2/3}$ (on the history $b_4' = \frac43 b_4$). `tables` is an $8 \times 8 \times 8$ array of zeros, filled with the values of the 31 symbols at this point (`f(*POINT)` hands the six numbers to the function one by one).

```python
fig, axes = plt.subplots(2, 4, figsize=(11.0, 5.4))
norm = SymLogNorm(linthresh=0.1, vmin=-15.0, vmax=15.0, base=10)
for a, ax in enumerate(axes.flat):
    image = ax.imshow(tables[a], cmap=DIVERGING, norm=norm)
    for b, c in itertools.product(range(8), repeat=2):
        if tables[a, b, c] != 0:
            ax.text(c, b, f"{tables[a, b, c]:.2f}", ha="center", va="center",
                    fontsize=6.0)
    ax.set_title(f"$\\Gamma^{{x_{a}}}{{}}_{{bc}}$", fontsize=10)
    ax.set_xticks(range(8), [str(k) for k in range(8)], fontsize=7)
    ax.set_yticks(range(8), [str(k) for k in range(8)], fontsize=7)
    ax.grid(False)
fig.colorbar(image, ax=axes, shrink=0.8, label="value (unit $H$)")
fig.suptitle("Christoffel symbols at $z = \\pi/4$, $a_4 = 0.5$, "
             "$a_4^{\\prime} = 1$, $b_4 = e^{2/3}$, $b_4^{\\prime}/b_4 = 4/3$, "
             "$H = 1$ (row $b$, column $c$)")
```

A figure with $2 \times 4$ drawing areas, one for each upper index. `SymLogNorm(linthresh=0.1, vmin=-15.0, vmax=15.0, base=10)` is the **symmetric-logarithmic** colour scale: between $-0.1$ and $0.1$ it is ordinary, beyond that equal steps of colour stand for equal factors (base 10), so that symbols of very different sizes are all visible. `axes.flat` runs through the eight areas; in area $a$, `imshow` draws the table $\Gamma^{x_a}{}_{bc}$ (row $b$, column $c$), and every non-zero value is written into its square with two decimals. The double braces in the f-string of the title produce single braces in the text (`{{` gives `{`), so that matplotlib reads $\Gamma^{x_a}{}_{bc}$. One colour bar and a title for the whole figure follow.

```python
save_figure(fig, "christoffel_heat_maps",
            "The 512 Christoffel symbols $\\Gamma^{a}{}_{bc}$ of the corrected metric "
            "at the point $z = \\pi/4$ on the slice $a_4 = 0.5$ of the history "
            "$a_4 = x_4$, $b_4 = e^{4x_4/3}$ ($a_4^{\\prime} = 1$, "
            "$b_4 = e^{2/3}$ and $b_4^{\\prime}/b_4 = 4/3$, $H = 1$), as eight heat "
            "maps, one "
            "for each upper index $a = x_0, \\dots, x_7$; in each map the row is $b$ "
            "and the column is $c$ (numbers $0$ to $7$ for $x_0$ to $x_7$), the "
...
check(np.allclose(tables, tables.transpose(0, 2, 1))
      and all(4 in key or 0 in key for key in nonzero)
      and not any(Gamma[k][k][0] != 0 for k in (1, 2, 3)),
      "the tables are symmetric in b, c; every non-zero symbol has an index x4 or x0; "
      "Gamma^xi_(xi x0) = 0 for 3-space")
```

The figure is saved with its caption. The check requires the tables to be symmetric in $b$ and $c$ (`transpose(0, 2, 1)` exchanges the last two indices; `np.allclose` compares with a tiny tolerance), every non-zero symbol to have an index $x_4$ or $x_0$, and the symbols $\Gamma^{x_i}{}_{x_ix_0}$ of 3-space to be zero (no warp).

**What Figure 03b.1 shows.** Eight small maps; 31 of the 512 squares are coloured. The map of $\Gamma^{x_0}{}_{bc}$ has the large negative corner entry $\Gamma^{x_0}{}_{x_0x_0} = -12$ (at $z = \pi/4$, $-6H/(\sin z\cos z) = -12H$), the entries $-0.33$ in row and column $x_4$ ($\alpha_t = -\frac13$), and the three extra-time entries $H W^2\tan z = 0.89$ on the diagonal; the 3-space maps hold only the two entries $a_4' = 1$ at $(x_1, x_4)$ and $(x_4, x_1)$; the map of $\Gamma^{x_4}{}_{bc}$ holds the diagonal entries of 3-space, $a_4'e^{2a_4} = e = 2.72$, of the extra times, $0.21$, and of $x_0$, $-0.24$; the extra-time maps hold $H\cot z = 1$ in row and column $x_0$ and $-0.33$ in row and column $x_4$. Every map is symmetric about its diagonal.

**In [9], the symbols across a cell.**

```python
z_line = np.linspace(0.01, np.pi - 0.01, 600)
z_line = z_line[np.abs(z_line - np.pi / 2) > 0.004]  # leave out the fold itself
```

600 values of $z$ across the cell $0 < z < \pi$, without the points within $0.004$ of the fold, where some symbols are infinite (a **boolean index** `z_line[condition]` keeps the entries for which the condition is true).

```python
chosen = [((5, 5, 0), RED, "-", "$\\Gamma^{x_5}{}_{x_5 x_0}$"),
          ((0, 0, 0), VIOLET, "--", "$\\Gamma^{x_0}{}_{x_0 x_0}$"),
          ((0, 5, 5), ORANGE, "-.", "$\\Gamma^{x_0}{}_{x_5 x_5}$"),
          ((4, 0, 0), BLUE, ":", "$\\Gamma^{x_4}{}_{x_0 x_0}$"),
          ((1, 1, 4), AQUA, "-", "$\\Gamma^{x_1}{}_{x_1 x_4}$")]
fig, ax = plt.subplots()
for index, colour, style, label in chosen:
    values = np.broadcast_to(gamma_functions[index](z_line, *POINT[1:]),
                             z_line.shape)
    ax.plot(z_line, np.abs(values), color=colour, ls=style, lw=1.8, label=label)
ax.axvline(np.pi / 2, color="grey", lw=0.8, ls=":")
ax.text(np.pi / 2 + 0.04, 1.5e-5, "fold", fontsize=9)
ax.set_yscale("log")
ax.set_xlabel("$z = 6 H x_0$ (radians)")
ax.set_ylabel("absolute value of the symbol (unit $H$)")
ax.set_title("Christoffel symbols across a cell "
             "($a_4 = 0.5$, $a_4^{\\prime} = 1$, $b_4 = e^{2/3}$, $H = 1$)")
ax.set_ylim(1e-5, 3e3)  # room below the curves for the legend
ax.legend(fontsize=8, loc="lower center", ncol=3)
```

Five symbols, each with its colour, line style and label (`chosen` is a list of such quadruples). For each, the numerical function is evaluated on the line with the point of the history (`POINT[1:]` drops the first entry, $z$, of `POINT`, and `z_line` takes its place); `np.broadcast_to` makes a symbol that does not depend on $z$, such as $a_4' = 1$, an array of the right length. The sizes are drawn on a logarithmic axis; a dotted line and the word "fold" mark $z = \pi/2$.

```python
save_figure(fig, "christoffel_versus_z",
            "The absolute values of five Christoffel symbols of the corrected metric "
            "across one cell $0 < z < \\pi$ (two halves joined at the fold "
...
check(abs(gamma_functions[(5, 5, 0)](*POINT) - 1.0) < 1e-14
      and abs(gamma_functions[(5, 4, 5)](*POINT) - (-1.0 / 3.0)) < 1e-14
      and abs(gamma_functions[(0, 0, 4)](*POINT) - (-1.0 / 3.0)) < 1e-14,
      "at z = pi/4, H = 1: Gamma^x5_(x5 x0) = H cot z = 1, and on the history "
      "Gamma^x5_(x4 x5) = Gamma^x0_(x0 x4) = -a4' + b4'/(2 b4) = -1/3")
```

The figure is saved. The check evaluates three symbols at the point of the pictures: $\Gamma^{x_5}{}_{x_5x_0} = H\cot(\pi/4) = 1$, and $\Gamma^{x_5}{}_{x_4x_5} = \Gamma^{x_0}{}_{x_0x_4} = \alpha_t = -1 + \frac12\cdot\frac43 = -\frac13$, each to within $10^{-14}$.

**What Figure 03b.2 shows.** On the logarithmic axis: $H\cot z$ (solid red) falls from large values at the tip $z \to 0$ to $0$ at the fold (it dives downwards there) and rises again towards the other tip; $|\Gamma^{x_0}{}_{x_0x_0}|$ (dashed violet) is large at both tips and at the fold, with its smallest value $12$ at $z = \pi/4$ and $3\pi/4$; $\Gamma^{x_0}{}_{x_5x_5}$ (dash-dotted orange) grows towards the fold and falls towards the tips; $|\Gamma^{x_4}{}_{x_0x_0}|$ (dotted blue) grows towards the tips and vanishes at the fold; $\Gamma^{x_1}{}_{x_1x_4} = 1$ (aqua) is a flat line. Every curve is symmetric about the fold.

**In [10], finite differences.**

```python
prime = chr(39)  # the apostrophe (character number 39): the record writes a4 prime so
point_text = (f"H = 0.23, a4 = 0.17, a4{prime} = 0.61, a4{prime}{prime} = -0.37, "
              f"b4 = 1.37, b4{prime} = 0.31, b4{prime}{prime} = -0.23, "
              "x0 = 0.41")  # the test point as the record writes it
check(record_check(RUST_REPORT, "k1_brute_force_numeric", point_text),
      "the test point is the one of the brute-force check of the Rust program")
```

`chr(39)` is the character with the number 39, the apostrophe; the record writes $a_4'$ as `a4'`, and building the text from `prime` avoids typing an apostrophe into the code (which the book would print as a curly quote). `point_text` is the test point exactly as the Rust report writes it, and `record_check` (with this text as `detail_part`) confirms that the report's check `k1_brute_force_numeric` passed and was made at this point: a PASS line.

```python
H_n, a0, a1, a2, x0_n = 0.23, 0.17, 0.61, -0.37, 0.41  # the test point
b0, b1, b2 = 1.37, 0.31, -0.23  # b4, b4' and b4'' at x4 = 0
```

The test point as numbers: $H = 0.23$, $a_4 = 0.17$, $a_4' = 0.61$, $a_4'' = -0.37$, $x_0 = 0.41$, and $b_4 = 1.37$, $b_4' = 0.31$, $b_4'' = -0.23$ at $x_4 = 0$.

```python
def metric_numbers(x):
    """The metric as an 8 x 8 numpy table at the point x (8 coordinates)."""
    a = a0 + a1 * x[4] + 0.5 * a2 * x[4] ** 2  # a4(x4) with a4(0) = 0.17, ...
    b = b0 + b1 * x[4] + 0.5 * b2 * x[4] ** 2  # b4(x4) with b4(0) = 1.37, ...
    f_squared = np.exp(-2 * a) * b  # f^2 = e^(-2 a4) b4
    warp_squared = np.abs(np.sin(6 * H_n * x[0])) ** (1 / 3)  # W^2 = |sin z|^(1/3)
    # the author's order x0, x1, ..., x7
    return np.diag([f_squared / np.tan(6 * H_n * x[0]) ** 2] + [np.exp(2 * a)] * 3
                   + [-1.0] + [-f_squared * warp_squared] * 3)
```

`metric_numbers(x)` is the corrected metric as a plain $8 \times 8$ numpy table at the point `x`, with the concrete functions $a_4(x_4) = 0.17 + 0.61x_4 - 0.185x_4^2$ and $b_4(x_4) = 1.37 + 0.31x_4 - 0.115x_4^2$ (`0.5 * a2` is $-0.185$), which have the values of the test point at $x_4 = 0$. `f_squared` is $f^2 = e^{-2a_4}b_4$ and `warp_squared` is $W^2 = |\sin z|^{1/3}$. `np.diag` builds the diagonal table from the list of the eight entries (lists joined with `+`).

```python
def christoffel_numbers(x, h):
    """All 512 Christoffel symbols at x from central differences with step h."""
    d_metric = np.zeros((8, 8, 8))  # d_metric[c] = derivative of g along x_c
    for c in range(8):
        step = np.zeros(8)
        step[c] = h
        d_metric[c] = (metric_numbers(x + step) - metric_numbers(x - step)) / (2 * h)
    inverse = np.linalg.inv(metric_numbers(x))
    table = np.zeros((8, 8, 8))
    for a, b, c in itertools.product(range(8), repeat=3):
        table[a, b, c] = 0.5 * sum(inverse[a, d] * (d_metric[b][d, c]
                                   + d_metric[c][d, b] - d_metric[d][b, c])
                                   for d in range(8))
    return table
```

`christoffel_numbers(x, h)` computes all 512 symbols with numbers only: for each coordinate $c$ it moves the point by $\pm h$ along $x_c$ (`step` is zero except in place $c$) and takes the central difference of the two metric tables; `np.linalg.inv` inverts the metric table; then the Christoffel formula, term by term.

```python
x_point = np.array([x0_n, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])  # x0 = 0.41, x4 = 0
exact = np.zeros((8, 8, 8))
for (a, b, c), f in gamma_functions.items():
    exact[a, b, c] = f(6 * H_n * x0_n, a0, a1, H_n, b0, b1)
```

The point $x_0 = 0.41$, $x_4 = 0$ (all other coordinates $0$; they do not matter), and the exact symbols there, from the functions of In [8] with $z = 6Hx_0$.

```python
steps = 10.0 ** -np.arange(1, 9)  # h = 0.1, 0.01, ..., 1e-8
errors = np.array([np.max(np.abs(christoffel_numbers(x_point, h) - exact))
                   for h in steps])
for h, e in zip(steps, errors):
    say(f"  h = {h:.0e}: largest error of the 512 symbols = {e:.2e}")
order = np.log10(errors[0] / errors[1])  # the slope between h = 0.1 and h = 0.01
report("measured order of the error between h = 0.1 and h = 0.01", f"{order:.3f}")
check(1.9 < order < 2.1 and errors.min() < 1e-8,
      "finite differences reproduce all 512 symbols; the error falls like h^2")
```

Eight step sizes $h = 10^{-1}, \dots, 10^{-8}$ (`np.arange(1, 9)` is $1, \dots, 8$); for each, the largest error among the 512 symbols. The printed table shows the error falling by a factor of about 100 for each factor 10 in $h$, from $4.01 \times 10^{-1}$ at $h = 0.1$ to $3.65 \times 10^{-9}$ at $h = 10^{-5}$, and then rising again. `order` is the slope between the first two steps on a logarithmic scale, $\log_{10}$ of the ratio of the errors: $2.040$. The check requires an order between $1.9$ and $2.1$ and a smallest error below $10^{-8}$.

**In [11], the figure of the finite differences.**

```python
fig, ax = plt.subplots()
ax.loglog(steps, errors, "o-", color=BLUE, lw=1.8, ms=7,
          label="largest error of the 512 symbols")
ax.loglog(steps, errors[0] * (steps / steps[0]) ** 2, "--", color="black", lw=1.2,
          label="slope 2: error proportional to $h^2$")
ax.set_xlabel("step $h$ of the central difference")
ax.set_ylabel("largest absolute error (unit $H$)")
ax.set_title("Christoffel symbols by finite differences")
ax.legend(fontsize=8)
best = int(np.argmin(errors))  # the position of the smallest error in the list
report("best step and its error", f"h = {steps[best]:.0e}, error {errors[best]:.1e}")
mantissa, exponent = f"{errors[best]:.1e}".split("e")  # e.g. "3.2" and "-10"
best_error = f"{mantissa} \\times 10^{{{int(exponent)}}}"  # 3.2 x 10^-10 in LaTeX
best_step = f"10^{{{round(np.log10(steps[best]))}}}"  # the step as a power of 10
```

The error against $h$ on logarithmic axes (`loglog`), with the reference line of slope 2 through the first point. `np.argmin` gives the position of the smallest error; the RESULT line prints it, $h = 10^{-6}$ with the error $1.5 \times 10^{-10}$. The last three lines turn this error into LaTeX for the caption: the f-string `f"{errors[best]:.1e}"` gives a text such as `1.5e-10`, `split("e")` cuts it into the mantissa `1.5` and the exponent `-10`, and the two are put together as $1.5 \times 10^{-10}$; the step is written as a power of 10 in the same way.

```python
save_figure(fig, "finite_differences",
            "The largest difference between the 512 Christoffel symbols computed "
            "numerically by central differences of the metric and the exact "
            "symbols, at the test point $H = 0.23$, $a_4 = 0.17$, "
...
check(errors[0] > errors[1] > errors[2] > errors[3],
      "the error shrinks as the step shrinks from 0.1 to 0.0001")
```

The figure is saved with the measured numbers in its caption, and the check requires the error to shrink at each of the first three refinements.

**What Figure 03b.3 shows.** The blue points fall along the dashed line of slope 2 from $h = 0.1$ to $h = 10^{-5}$ (each factor 10 in $h$ divides the error by 100), reach the smallest error $1.5 \times 10^{-10}$ at $h = 10^{-6}$, and rise again for smaller $h$, where the rounding errors of the computer, divided by $h$, take over.

**In [12], observers at rest and the contracted symbols.**

```python
check(all(Gamma[a][4][4] == 0 for a in range(8)),
      "Gamma^a_(x4 x4) = 0: observers at rest fall freely, x4 is their proper time")
volume = sp.exp(-a4) * b4 ** 2 * G * sp.cot(6 * H * x0) * W(x0) ** 3  # sqrt|det g|
contracted = [vanishes(sum(Gamma[a][a][b] for a in range(8))
                       - sp.diff(sp.log(volume), X[b]))
              for b in range(8)]
check(all(contracted),
      "sum over a of Gamma^a_(a b) equals the derivative of ln sqrt|det g|")
```

The first check: the eight symbols $\Gamma^a{}_{x_4x_4}$ are zero (Section 3.23). The second: for each $b$, $\sum_a\Gamma^a{}_{ab}$ minus the derivative of $\ln\sqrt{|\det g|}$ along $x_b$ vanishes, with the volume factor written as $e^{-a_4}b_4^2\,G\cot z\,W^3$ (Section 3.6; $|\cot z| = G\cot z$, and the constant $G$ drops out of the logarithmic derivative).

**In [13], the Riemann tensor.**

```python
def riemann(table, coordinates):
    """The non-zero R^a_bcd (MTW) as a dictionary {(a, b, c, d): value}."""
    n = len(coordinates)
    result = {}
    for a, b in itertools.product(range(n), repeat=2):
        for c, d in itertools.combinations(range(n), 2):  # all pairs c < d
            value = (sp.diff(table[a][b][d], coordinates[c])
                     - sp.diff(table[a][b][c], coordinates[d])
                     + sum(table[a][c][e] * table[e][b][d]
                           - table[a][d][e] * table[e][b][c] for e in range(n)))
            value = tidy(value)
            if value != 0:
                result[(a, b, c, d)] = value
                result[(a, b, d, c)] = -value  # antisymmetric in c and d
    return result
```

`riemann` computes $R^a{}_{bcd}$ with the formula of Section 3.17 for the index pairs $c < d$ only (`itertools.combinations(range(n), 2)` gives every pair once), and fills $c > d$ with the opposite sign, by the antisymmetry (S1). Only the non-zero components are stored, in a dictionary whose keys are the index lists. A backslash is not needed inside brackets: Python continues a statement as long as a bracket is open.

```python
def raise_second(riemann_table, metric):
    """R^ab_cd = sum over e of g^(be) R^a_ecd, the non-zero ones."""
    inverse = metric.inv()
    result = {}
    for (a, e, c, d), value in riemann_table.items():
        for b in range(metric.rows):
            if inverse[b, e] != 0:
                result[(a, b, c, d)] = result.get((a, b, c, d), 0) \
                    + inverse[b, e] * value
    result = {k: tidy(v) for k, v in result.items()}
    return {k: v for k, v in result.items() if v != 0}
```

`raise_second` raises the second index: $R^{ab}{}_{cd} = \sum_e g^{be}R^a{}_{ecd}$. It loops over the non-zero components and adds each, times the inverse metric, to the component with the new second index (`result.get(key, 0)` starts a new entry at $0$); the backslash continues the long line. The results are simplified and the zeros removed.

```python
R_down = riemann(Gamma, X)  # R^a_bcd
R_mixed = raise_second(R_down, g)  # R^ab_cd
report("non-zero components R^a_bcd", len(R_down))
report("non-zero components R^ab_cd", len(R_mixed))
record_check(RUST_REPORT, "riemann_antisymmetry", "112 nonzero entries")
check(len(R_mixed) == 112, "R^ab_cd has 112 non-zero components, as in the record",
      record="Revision/gkd_lovelock/results/lovelock-report.json, check "
             "riemann_antisymmetry (112 nonzero entries)")
```

Both forms are computed; the RESULT lines print 112 components each (Section 3.24). `record_check` confirms that the Rust report's check `riemann_antisymmetry` passed and that its detail mentions "112 nonzero entries", and the check compares our number with it.

**In [14], symmetries, the Bianchi identity, and two properties of the corrected metric.**

```python
def get(table, key):
    return table.get(key, 0)
```

`get(table, key)` returns a component, or $0$ when it is not among the stored non-zero ones.

```python
antisymmetric = all(vanishes(v + get(R_mixed, (b, a, c, d)))
                    and vanishes(v + get(R_mixed, (a, b, d, c)))
                    for (a, b, c, d), v in R_mixed.items())
lowered = {(a, b, c, d): g[a, a] * g[b, b] * v
           for (a, b, c, d), v in R_mixed.items()}
pair_symmetric = all(vanishes(v - get(lowered, (c, d, a, b)))
                     for (a, b, c, d), v in lowered.items())
record_check(PYTHON_REPORT, "riemann_antisymmetry_and_pair_symmetry")
check(antisymmetric and pair_symmetric,
      "R^ab_cd is antisymmetric in a, b and in c, d; R_abcd = R_cdab",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, check "
             "riemann_antisymmetry_and_pair_symmetry")
```

The antisymmetries in the upper and in the lower pair are tested on every stored component (the sum of a component and its partner with one pair exchanged must vanish). `lowered` holds $R_{abcd} = g_{aa}g_{bb}R^{ab}{}_{cd}$ for the diagonal metric, and `pair_symmetric` tests $R_{abcd} = R_{cdab}$. After `record_check`, the check prints a PASS line with the sympy checker's report as the record.

```python
bianchi = [vanishes(get(R_down, (a, b, c, d)) + get(R_down, (a, c, d, b))
                    + get(R_down, (a, d, b, c)))
           for a, b, c, d in itertools.product(range(8), repeat=4)]
record_check(RUST_REPORT, "riemann_first_bianchi")
check(all(bianchi) and len(bianchi) == 4096,
      "the first Bianchi identity holds for all 4096 index lists",
      record="Revision/gkd_lovelock/results/lovelock-report.json, check "
             "riemann_first_bianchi")
```

The first Bianchi identity for all $8^4 = 4096$ index lists (`itertools.product(range(8), repeat=4)`); the list `bianchi` holds one truth value per list, and the check requires all of them and their number.

```python
x0_free = all(not symbolic(v).has(x0) for v in R_mixed.values())
record_check(RUST_REPORT, "mixed_riemann_free_of_x0")
record_check(PYTHON_REPORT, "mixed_riemann_free_of_x0")
check(x0_free, "no R^ab_cd depends on x0: neither W nor any function of z is left",
      record="Revision/gkd_lovelock/results/lovelock-report.json and "
             "python-lovelock-report.json, check mixed_riemann_free_of_x0")
```

`symbolic(v).has(x0)` is true when $x_0$ still occurs in a component, inside the warp factor `W(x0)` or a function of $z$; no component may contain it. Both reports of the record state the same, as two `record_check` calls confirm.

```python
sectional = all({c, d} == {a, b} for a, b, c, d in R_mixed)
record_check(RUST_REPORT, "mixed_riemann_only_sectional")
record_check(PYTHON_REPORT, "mixed_riemann_only_sectional")
check(sectional, "every non-zero R^ab_cd has {c, d} = {a, b}: only plane curvatures",
      record="Revision/gkd_lovelock/results/lovelock-report.json and "
             "python-lovelock-report.json, check mixed_riemann_only_sectional")
```

`{c, d} == {a, b}` compares two **sets** (collections without order): every stored component must have the same two indices below as above, that is, be a plane curvature (Section 3.24).

**In [15], every component against the record.**

```python
record_riemann = {}
for entry in record["riemannMixedNonzero"]:
    key = tuple(NAMES.index(n) for n in entry["up"] + entry["down"])
    record_riemann[key] = from_mathematica(entry["value"])
check(sorted(record_riemann) == sorted(R_mixed),
      "the same 112 non-zero components R^ab_cd as the record")
```

The record lists each component with `up` ($a$, $b$) and `down` ($c$, $d$) as names; `entry["up"] + entry["down"]` joins the two lists, and the generator inside `tuple(...)` turns the four names into numbers. The first check requires the same 112 index lists.

```python
record_check(PYTHON_REPORT, "rust_riemann_agrees")
check(all(same(R_mixed[k], v) for k, v in record_riemann.items()),
      "every component R^ab_cd equals the record exactly",
      record=f"{CURVATURE_RECORD}, riemannMixedNonzero (and "
             "python-lovelock-report.json, check rust_riemann_agrees)")
```

The second check requires every component to equal the record's exactly.

```python
groups = {}
for key in sorted(R_mixed):
    # the value multiplied out: one value written in two ways counts once
    groups.setdefault(sp.sstr(sp.expand(plain(R_mixed[key]))), []).append(key)
for value_text in sorted(groups):
    a, b, c, d = groups[value_text][0]
    say(f"  {len(groups[value_text]):2d} x  {value_text}  e.g. "
        f"R^({NAMES[a]} {NAMES[b]})_({NAMES[c]} {NAMES[d]})")
report("different values among the 112 components", len(groups))
```

The components are grouped by their value: `sp.sstr(sp.expand(...))` writes the multiplied-out value as a text, which serves as the key of the dictionary `groups` (`setdefault` starts a new list for a new key). The output lists the ten different values, how often each occurs and one example: $\pm a_4'^2$ (6 times each), $\pm(a_4'^2 + a_4'')$ (6 each), $\pm(a_4'^2 - a_4'b_4'/(2b_4))$ (24 each; this is $\mp\alpha\alpha_t$), $\pm(\alpha_t^2 + \alpha_t')$ written out (8 each) and $\pm(\alpha_t^2 - H^2e^{2a_4}/b_4)$ written out (12 each).

**In [16], the plane curvatures.**

```python
plane = {(a, b): plain(sp.S(get(R_mixed, (a, b, a, b))))  # sp.S: 0 as a sympy 0
         for a, b in itertools.product(range(8), repeat=2) if a != b}
alpha_t = -a4p + b4p / (2 * b4v)  # the common rate of x0 and the extra times
alpha_t_prime = -a4pp + b4pp / (2 * b4v) - b4p ** 2 / (2 * b4v ** 2)  # its derivative
k_value = sp.exp(2 * a4v) / b4v  # k = e^(2 a4)/b4 = 1/f^2
```

`plane` holds the 28 values $\sigma(a, b) = R^{ab}{}_{ab}$ for all ordered pairs $a \ne b$ (`sp.S(0)` makes a missing component a sympy zero, so that `plain` can be applied). `alpha_t` is $\alpha_t$ written with the printing names, `alpha_t_prime` its derivative (Section 3.24), and `k_value` is $k = e^{2a_4}/b_4$.

```python
# the planes (row, column) in the author's order x0, x1, ..., x7
expected = {(1, 2): a4p ** 2, (1, 4): a4p ** 2 + a4pp,
            (1, 5): a4p * alpha_t, (1, 0): a4p * alpha_t,
            (4, 5): alpha_t ** 2 + alpha_t_prime, (4, 0): alpha_t ** 2 + alpha_t_prime,
            (5, 6): alpha_t ** 2 - H ** 2 * k_value,
            (5, 0): alpha_t ** 2 - H ** 2 * k_value}
for (a, b), formula in expected.items():
    say(f"  plane ({NAMES[a]}, {NAMES[b]}): R^ab_ab = {plane[(a, b)]}")
check(all(sp.simplify(plane[key] - formula) == 0 for key, formula in expected.items())
      and all(not v.has(z) for v in plane.values()),
      "the plane curvatures have the eight formulas and do not depend on z")
```

The eight expected formulas of the table of Section 3.24, for one plane of each kind (two kinds of planes with $x_4$ and two kinds inside the block appear twice, once with an extra time and once with $x_0$). The loop prints the eight computed values, for example `a4p**2` for the plane $(x_1, x_2)$ and `-H**2*exp(2*a4v)/b4v + a4p**2 - a4p*b4p/b4v + b4p**2/(4*b4v**2)` for the plane $(x_5, x_0)$; the check requires each to equal its formula and no plane value to contain $z$.

```python
apart = {1: sp.exp(a4), 5: sp.exp(-a4) * sp.sqrt(b4) * W(x0),
         0: sp.exp(-a4) * sp.sqrt(b4) * sp.cot(6 * H * x0)}  # h1, h5, h0
growth = {}  # (d^2 xi/d tau^2)/xi for observers at rest apart along x1, x5 or x0
for a, h_a in apart.items():  # xi = h_a times a fixed coordinate distance, tau = x4
    growth[a] = sp.expand(plain(sp.simplify(sp.diff(h_a, x4, 2) / h_a)))
    say(f"  at rest, apart along {NAMES[a]}: (d^2 xi/d tau^2)/xi = {growth[a]}")
check(sp.simplify(apart[1] ** 2 - g[1, 1]) == 0
      and sp.simplify(apart[5] ** 2 + g[5, 5]) == 0
      and sp.simplify(apart[0] ** 2 - g[0, 0]) == 0
      and all(sp.simplify(growth[a] - plane[(a, 4)]) == 0 for a in apart),
      "observers at rest: d^2 xi/d tau^2 = +R^ab_ab xi in the planes (x1, x4), "
      "(x5, x4) and (x0, x4)")
```

The relative acceleration of two observers at rest (Section 3.24): `apart` holds the scale factors $h_1 = e^{a_4}$, $h_5 = fW$ and $h_0 = f\cot z$, and `growth` the ratio $(\partial_4^2 h_a)/h_a$ for each, printed. The check confirms that the three scale factors reproduce the metric entries and that each ratio equals the plane curvature $\sigma(a, x_4)$.

```python
SLOPES = (0.5, 1.0, 2.0)  # three deflating histories, A > 0
BETA = sp.Rational(4, 3)  # b4 = b4(0) e^(beta A H x4) on the history


def history_values(slope, slice_a4=0):
    """a4p, a4pp, b4p, b4pp, a4v, b4v on the history with the slope A (H = 1,
    b4(0) = 1) at the slice a4 = slice_a4, where b4 = e^(beta a4)."""
    b4_slice = sp.exp(BETA * slice_a4)
    return {a4p: slope, a4pp: 0, H: 1, b4p: BETA * slope * b4_slice,
            b4pp: (BETA * slope) ** 2 * b4_slice, a4v: slice_a4, b4v: b4_slice}
```

Three slopes $A = 0.5, 1, 2$ of the history and the exponent $\beta = \frac43$ as an exact fraction. `history_values(slope, slice_a4)` returns the values that the printing names take on the history with the slope $A$ ($H = 1$, $b_4(0) = 1$) at a slice: $a_4' = A$, $a_4'' = 0$, $b_4 = e^{\beta a_4}$, $b_4' = \beta A\,b_4$, $b_4'' = (\beta A)^2b_4$. Without the second argument it is the first slice $a_4 = 0$.

```python
fig, axes = plt.subplots(1, 3, figsize=(15.0, 4.8))  # wide: room for 0.0278
for ax, slope in zip(axes, SLOPES):
    curv = np.full((8, 8), np.nan)  # NaN: an empty square on the diagonal
    for (a, b), value in plane.items():
        curv[a, b] = float(sp.simplify(value.subs(history_values(slope))))
    image = ax.imshow(curv, cmap=DIVERGING, vmin=-5.0, vmax=5.0)
    for a, b in plane:
        ax.text(b, a, f"{curv[a, b]:.3g}", ha="center", va="center", fontsize=6.0)
    ax.set_xticks(range(8), LABELS, fontsize=8)
    ax.set_yticks(range(8), LABELS, fontsize=8)
    ax.grid(False)
    ax.set_title(f"$A = {slope:g}$")
fig.colorbar(image, ax=axes, shrink=0.85, label="curvature (unit $H^2$)")
```

For each slope, `curv` is an $8 \times 8$ table that starts filled with `np.nan` ("not a number", drawn as an empty square), and every plane value is evaluated on the first slice of that history; the three tables are drawn as heat maps with the values written in, on a colour scale from $-5$ to $5$.

```python
save_figure(fig, "plane_curvatures",
            "The curvature $\\sigma(a, b) = R^{ab}{}_{ab}$ (no sum) of the plane of "
            "$x_a$ (row) and $x_b$ (column), unit $H^2$, on the first slice "
...
check([float(plane[(1, 2)].subs(history_values(s))) for s in SLOPES]
      == [0.25, 1.0, 4.0]
      and [sp.simplify(plane[(5, 6)].subs(history_values(s))) for s in (1, 2)]
      == [sp.Rational(-8, 9), sp.Rational(-5, 9)],
      "on the slice a4 = 0 the planes inside 3-space are 0.25, 1, 4 and inside the "
      "block -8/9, -5/9 (A = 1, 2)")
```

The figure is saved. The check compares the planes inside 3-space with $0.25$, $1$ and $4$ ($A^2$) and the planes inside the block at $A = 1$ and $A = 2$ with $\frac19 - 1 = -\frac89$ and $\frac49 - 1 = -\frac59$ exactly.

**What Figure 03b.4 shows.** Three $8 \times 8$ maps for $A = 0.5$, $1$, $2$ on the first slice. Each map has the same pattern: the 3-space rows and columns carry $A^2$ against 3-space and $x_4$ (red), $-A^2/3$ against the block (blue); the row and column of $x_4$ carry $A^2/9$ against the block (pale red); inside the block the values $A^2/9 - 1$ are negative ($-0.972$, $-0.889$, $-0.556$). The rows and columns of $x_0$ repeat those of the extra times exactly, and as $A$ grows the colours of the 3-space planes deepen.

**In [17], Ricci, Ricci scalar and Einstein tensor.**

```python
def ricci(mixed_table, n):
    """R^a_b = sum over c of R^ac_bc, as an n x n sympy matrix."""
    result = sp.zeros(n, n)
    for (a, c, b, d), value in mixed_table.items():
        if c == d:
            result[a, b] += value
    return result.applyfunc(tidy)
```

`ricci` adds up the components $R^{ac}{}_{bc}$ into the $8 \times 8$ matrix $R^a{}_b$ (only the stored components with equal second and fourth index contribute).

```python
Ric = ricci(R_mixed, 8)
R_scalar = tidy(Ric.trace())
G_mixed = (Ric - R_scalar / 2 * sp.eye(8)).applyfunc(tidy)
for k in range(8):
    say(f"  {NAMES[k]}: R^a_a = {plain(Ric[k, k])}")
    say(f"      G^a_a = {plain(G_mixed[k, k])}")
say(f"Ricci scalar R = {plain(R_scalar)}")
```

The Ricci tensor, its trace $R$ (`Ric.trace()`) and the Einstein tensor $G = \mathrm{Ric} - \frac12 R\cdot 1$ (`sp.eye(8)` is the unit matrix); the diagonal entries and $R$ are printed. The output shows the formulas of Section 3.25, for example $R^{x_1}{}_{x_1} = $ `-a4p**2 + 2*a4p*b4p/b4v + a4pp` and $G^{x_4}{}_{x_4} = $ `6*H**2*exp(2*a4v)/b4v + 3*a4p**2 - 3*b4p**2/(2*b4v**2)`, with the hidden and the three extra-time lines identical.

```python
ricci_ok = all(same(Ric[i, j], from_mathematica(
    record["ricciMixed"][f"{NAMES[i]},{NAMES[j]}"]["mathematica"]))
    for i in range(8) for j in range(8))
einstein_ok = all(same(G_mixed[i, j], from_mathematica(
    record["einsteinMixed"][f"{NAMES[i]},{NAMES[j]}"]["mathematica"]))
    for i in range(8) for j in range(8))
scalar_ok = same(R_scalar, from_mathematica(record["ricciScalar"]))
record_check(PYTHON_REPORT, "rust_ricci_einstein_scalar_agree")  # stops if not
check(ricci_ok and einstein_ok and scalar_ok,
      "all 64 Ricci, all 64 Einstein components and R equal the record",
      record=f"{CURVATURE_RECORD}, ricciMixed, einsteinMixed, ricciScalar (and "
             "python-lovelock-report.json, check rust_ricci_einstein_scalar_agree)")
```

All 64 Ricci components, all 64 Einstein components (each read from the record by its key, such as `"x0,x0"`) and the scalar are compared with the record exactly.

**In [18], the first Lovelock scalar.**

```python
A4_REPORT = "Revision/field_equations_a4/reports/python-a4-report.json"
a4_report = json.loads(repository_file(A4_REPORT).read_text(encoding="utf-8"))
# the report's checks form a list of dictionaries; take the one with this name
L1_entry = next(entry for entry in a4_report["checks"]
                if entry["name"] == "L1_equals_gkd_branch")
L1_detail, L1_verdict = L1_entry["detail"], L1_entry["verdict"]
```

The sympy report of the record of the field equations is read; `next(...)` takes its check `L1_equals_gkd_branch`, and its detail and verdict are kept.

```python
say(f"record: {L1_detail} ({L1_verdict})")
u_sym, v_sym, k_sym = sp.symbols("u v k", real=True)  # u = b4'/b4, v = u', k
L1_text = L1_detail.split("=")[1]  # the text after the equals sign
L1_record = parse_expr(L1_text, local_dict={"H": H, "ad1": a4p, "ad2": a4pp,
                                            "uu": u_sym, "vv": v_sym, "kk": k_sym})
record_check(PYTHON_REPORT, "L1_equals_2R", "L_(1) = 2 R exactly")  # stops if not
IN_UVK = {b4p: u_sym * b4v, b4pp: (v_sym + u_sym ** 2) * b4v}  # b4' and b4''
TO_K = {a4v: sp.log(k_sym * b4v) / 2}  # a4 = ln(k b4)/2, that is e^(2 a4) = k b4
R_in_uv = sp.expand(sp.simplify(plain(R_scalar).subs(IN_UVK).subs(
    TO_K)))  # b4v and a4v drop out
```

The detail is printed: `L_(1) = -24*H**2*kk + 16*ad1**2 - 16*ad1*uu - 4*ad2 + 10*uu**2 + 8*vv (PASS)`. `u_sym`, `v_sym`, `k_sym` are the symbols $u$, $v$, $k$; the text after the equals sign is read with the record's names (`ad1` for $a_4'$, `ad2` for $a_4''$, `uu`, `vv`, `kk`). `record_check` confirms the check `L1_equals_2R` of the curvature record. `IN_UVK` writes $b_4' = u\,b_4$ and $b_4'' = (v + u^2)\,b_4$, and `TO_K` writes $a_4 = \frac12\ln(k\,b_4)$, so that $e^{2a_4} = k\,b_4$; with these replacements our $R$ becomes `R_in_uv`, in which $b_4$ and $a_4$ cancel.

```python
say(f"our R in u, v and k: {R_in_uv}")
check(L1_verdict == "PASS" and not R_in_uv.has(b4v) and not R_in_uv.has(a4v)
      and sp.expand(L1_record - 2 * R_in_uv) == 0,
      "the first Lovelock scalar of the record is twice our Ricci scalar (in u, v, k)",
      record=f"{A4_REPORT}, check L1_equals_gkd_branch (with "
             "python-lovelock-report.json, check L1_equals_2R)")
```

The printed result is $R = -12H^2k + 8a_4'^2 - 8a_4'u - 2a_4'' + 5u^2 + 4v$ (Section 3.25), and the check requires the record's $L_{(1)}$ to be exactly twice it.

**In [19], all recorded components at five test points with 30 digits.**

```python
python_report = json.loads(repository_file(PYTHON_REPORT).read_text(encoding="utf-8"))
mpmath.mp.dps = 30  # mpmath works with 30 significant digits from now on


def exact(text):
    """A fraction such as 46/75 of the record as an mpmath number."""
    fraction = sp.Rational(text)
    return mpmath.mpf(fraction.p) / fraction.q  # numerator / denominator


def as_numbers(expression):
    """The expression with W(x0) = |sin z|^(1/6) and G = the sign of cot z."""
    return sp.S(expression).subs(W(x0), sp.Abs(sp.sin(6 * H * x0)) ** sp.Rational(
        1, 6)).subs(G, sp.sign(sp.cot(6 * H * x0)))


test_points = [[exact(p["H"]), exact(p["x0"]), exact(p["a4"]),
                exact(p["a4" + prime]), exact(p["a4" + prime + prime]),
                exact(p["b4"]), exact(p["b4" + prime]), exact(p["b4" + prime + prime])]
```

`mpmath.mp.dps = 30` sets the working precision of mpmath to 30 decimal digits. `exact` turns a fraction written as text, such as `46/75`, into an mpmath number: `sp.Rational` reads it exactly, and its numerator `.p` divided by its denominator `.q` in mpmath arithmetic keeps 30 digits. `as_numbers` replaces the warp factor by $|\sin z|^{1/6}$ and `G` by the sign of $\cot z$ (`sp.sign`). The list comprehension that begins in the last line reads the eight numbers of each of the five test points of the record (keys such as `"a4'"`, built with `prime`).

```python
               for p in python_report["randomPoints"]]
say("z = 6 H x0 at the five test points: "
    + ", ".join(mpmath.nstr(6 * p[0] * p[1], 4) for p in test_points))
```

The five points are printed by their values of $z = 6Hx_0$: $0.92$, $2.01$, $3.64$, $5.29$ and $-2.2$, one in each quarter of the period and one at negative $z$ (`mpmath.nstr(x, 4)` writes a number with four digits).

```python
pairs = [(Gamma[a][b][c], v) for (a, b, c), v in record_gamma.items()]
pairs += [(R_mixed[key], v) for key, v in record_riemann.items()]
pairs += [(Ric[i, j], from_mathematica(record["ricciMixed"][f"{NAMES[i]},{NAMES[j]}"]
                                       ["mathematica"]))
          for i in range(8) for j in range(8)]
pairs += [(G_mixed[i, j], from_mathematica(
    record["einsteinMixed"][f"{NAMES[i]},{NAMES[j]}"]["mathematica"]))
    for i in range(8) for j in range(8)]
pairs += [(R_scalar, from_mathematica(record["ricciScalar"]))]
```

`pairs` collects every component of the record next to ours: 21 Christoffel symbols, 112 Riemann components, 64 Ricci and 64 Einstein components and the scalar, 262 pairs.

```python
# the order of the eight numbers of a test point
ARGS30 = (H, x0, a4v, a4p, a4pp, b4v, b4p, b4pp)
largest, evaluations = mpmath.mpf(0), 0
for mine, theirs in pairs:
    f_mine = sp.lambdify(ARGS30, as_numbers(symbolic(sp.S(mine))), "mpmath")
    f_record = sp.lambdify(ARGS30, as_numbers(theirs), "mpmath")
    for point in test_points:
        ours, recorded = f_mine(*point), f_record(*point)
        largest = max(largest, abs(ours - recorded) / max(1, abs(recorded)))
        evaluations += 1
```

For each pair both expressions become mpmath functions of the eight numbers (`sp.lambdify(..., "mpmath")`), and at each test point the relative difference $|\mathrm{ours} - \mathrm{record}|/\max(1, |\mathrm{record}|)$ is computed; `largest` keeps the largest, and `evaluations` counts $262 \times 5 = 1310$.

```python
for name in ("rust_christoffels_agree", "rust_riemann_agrees",
             "rust_ricci_einstein_scalar_agree"):
    record_check(PYTHON_REPORT, name)  # stops unless the check passed
report("components compared numerically", len(pairs))
report("evaluations at the five test points", evaluations)
report("largest relative difference (30 digits)", mpmath.nstr(largest, 3))
check(len(test_points) == 5 and largest < mpmath.mpf(10) ** -25,
      "at the five test points every component agrees to more than 25 digits",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
             "randomPoints, checks rust_christoffels_agree, rust_riemann_agrees, "
             "rust_ricci_einstein_scalar_agree")
```

The three exact comparisons of the independent verification are confirmed passed, the numbers are reported (262 components, 1310 evaluations, the largest relative difference $4.93 \times 10^{-31}$, the level of the 30-digit arithmetic itself), and the check requires five points and a difference below $10^{-25}$.

**In [20], the properties of the Einstein tensor.**

```python
LEAD = "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json"
for name in ("einstein_off_diagonal_vanish", "einstein_diagonal_x0_independent",
             "einstein_isotropy", "einstein_null_energy", "einstein_flat_vacuum"):
    record_check(LEAD, name)  # stops unless the lead check passed
WARPED_REPORT = "Revision/metric_warped/reports/python-warped-metric-report.json"
for name in ("corrected_offdiagonal_all_orders", "milne_flat_check"):
    record_check(WARPED_REPORT, name)  # stops unless the check passed
record_check(PYTHON_REPORT, "k1_offdiagonal_vanishes")
record_check(PYTHON_REPORT, "k1_hidden_equals_extra_times")
```

Nine `record_check` calls confirm, before anything is computed, that the lead's checks and the checks of the record of the corrected metric and of the sympy checker that the PASS lines below name are listed as passed.

```python
off_diagonal = [(i, j) for i in range(8) for j in range(8)
                if i != j and (G_mixed[i, j] != 0 or Ric[i, j] != 0)]
check(off_diagonal == [],
      "all 56 off-diagonal components of the Einstein and Ricci tensors vanish",
      record=f"{LEAD}, check einstein_off_diagonal_vanish, and "
             "python-warped-metric-report.json, check corrected_offdiagonal_all_orders")
```

The first check: no component of the Einstein or the Ricci tensor off the diagonal is non-zero (the list `off_diagonal` of such index pairs must be empty).

```python
check(all(not symbolic(G_mixed[k, k]).has(x0) for k in range(8)),
      "no diagonal component of the Einstein tensor depends on x0",
      record=f"{LEAD}, check einstein_diagonal_x0_independent")
check(G_mixed[1, 1] == G_mixed[2, 2] == G_mixed[3, 3]
      and G_mixed[0, 0] == G_mixed[5, 5] == G_mixed[6, 6] == G_mixed[7, 7],
      "3-space components equal; the hidden component equals the extra-time ones",
      record=f"{LEAD}, check einstein_isotropy (and python-lovelock-report.json, "
             "check k1_hidden_equals_extra_times)")
```

The second and third checks: no diagonal entry depends on $x_0$; the three 3-space entries are equal, and the hidden entry equals the three extra-time entries (Python reads `a == b == c` as both equalities at once).

```python
gap = sp.simplify(plain(G_mixed[0, 0] - G_mixed[4, 4]).subs(IN_UVK).subs(TO_K))
say(f"G^x0_x0 - G^x4_x4 = {sp.expand(gap)}")
check(sp.expand(gap + sp.Rational(3, 2) * (2 * H ** 2 * k_sym + 4 * a4p ** 2
                                            - a4p * u_sym + v_sym)) == 0,
      "G^x0_x0 - G^x4_x4 = -(3/2)(2 H^2 k + 4 a4p^2 - a4p u + v)",
      record=f"{LEAD}, check einstein_null_energy")
```

`gap` is $G^{x_0}{}_{x_0} - G^{x_4}{}_{x_4}$ written in $u$, $v$ and $k$; it is printed, `-3*H**2*k - 6*a4p**2 + 3*a4p*u/2 - 3*v/2`, and the fourth check compares it with $-\frac32(2H^2k + 4a_4'^2 - a_4'u + v)$ (Section 3.25).

```python
c_shift = sp.symbols("c", real=True)  # the constant c of the flat member
flat = {sp.Derivative(a4, (x4, 2)): 0, sp.Derivative(a4, x4): 0, a4: 0,
        sp.Derivative(b4, (x4, 2)): 2 * H ** 2, sp.Derivative(b4, x4):
        2 * H ** 2 * (x4 - c_shift), b4: H ** 2 * (x4 - c_shift) ** 2}
check(all(sp.simplify(v.subs(flat)) == 0 for v in R_mixed.values()),
      "the member a4 = 0, b4 = H^2 (x4 - c)^2 is flat: all 112 components vanish",
      record=f"{LEAD}, check einstein_flat_vacuum, and "
             "python-warped-metric-report.json, check milne_flat_check")
```

The flat member: `flat` replaces $a_4$ and its derivatives by $0$ and $b_4$, $b_4'$, $b_4''$ by $H^2(x_4 - c)^2$, $2H^2(x_4 - c)$ and $2H^2$; every one of the 112 components must vanish (Section 3.25).

**In [21], the contracted Bianchi identity.**

```python
divergence = []
for nu in range(8):
    value = sum(sp.diff(G_mixed[mu, nu], X[mu]) for mu in range(8)) \
        + sum(Gamma[mu][mu][lam] * G_mixed[lam, nu]
              for mu in range(8) for lam in range(8)) \
        - sum(Gamma[lam][mu][nu] * G_mixed[mu, lam]
              for mu in range(8) for lam in range(8))
    divergence.append(vanishes(value))
```

For each $\nu$ the divergence of Section 3.25 is computed term by term with the function $a_4(x_4)$ (so that sympy can differentiate $a_4''$ and $b_4''$ once more), and `vanishes` decides whether it is zero.

```python
record_check(RUST_REPORT, "k1_equals_minus_4_einstein")  # stops if not passed
record_check(RUST_REPORT, "k1_divergence_free")
check(all(divergence),
      "the contracted Bianchi identity: the divergence of G vanishes",
      record="Revision/gkd_lovelock/results/lovelock-report.json, checks "
             "k1_equals_minus_4_einstein and k1_divergence_free")
```

After two `record_check` calls the check requires all eight divergences to vanish.

**In [22], the Kretschmann scalar.**

```python
K = sp.factor(sp.expand(symbolic(sum(v * get(R_mixed, (c, d, a, b))
                                     for (a, b, c, d), v in R_mixed.items()))))
K_record = sp.factor(sp.expand(sum(v * record_riemann.get((c, d, a, b), 0)
                                   for (a, b, c, d), v in record_riemann.items())))
ricci_square = sp.factor(sp.expand(symbolic(sum(Ric[i, j] * Ric[j, i]
                                                for i in range(8)
                                                for j in range(8)))))
say(f"Kretschmann scalar K = {K}")
say(f"sum of R^a_b R^b_a  = {ricci_square}")
```

$K = \sum R^{ab}{}_{cd}R^{cd}{}_{ab}$ from our components (each multiplied by its partner with the two pairs exchanged), the same from the record's 112 components alone, and $\sum R^a{}_bR^b{}_a$; `sp.factor(sp.expand(...))` writes each as one fraction. The two formulas are printed (long, over several lines).

```python
check(sp.simplify(K - K_record) == 0,
      "K from our components equals K from the 112 components of the record")
```

The first check: both ways give the same $K$.

```python
sum_of_squares = 4 * (3 * a4p ** 4 + 3 * (a4p ** 2 + a4pp) ** 2
                      + 12 * a4p ** 2 * alpha_t ** 2
                      + 4 * (alpha_t ** 2 + alpha_t_prime) ** 2
                      + 6 * (alpha_t ** 2 - H ** 2 * k_value) ** 2)
K_in_uvk = sp.expand(sp.simplify(K.subs(IN_UVK).subs(TO_K)))
check(not K.has(x0) and sp.simplify(K - sum_of_squares) == 0
      and not K_in_uvk.has(a4v) and not K_in_uvk.has(b4v),
      "K = 4 times the sum of the 28 squared plane curvatures; no z, and a4, b4 "
      "only through a4p, a4pp, u, v, k")
```

`sum_of_squares` is the formula $4\sum_{\mathrm{planes}}\sigma^2$ of Section 3.25; the second check requires $K$ to equal it, to be free of $x_0$, and in $u$, $v$, $k$ to contain neither $a_4$ nor $b_4$.

```python
check(sp.simplify(sp.factor(symbolic(sum(
    v * get(R_mixed, (c, d, a, b)) for (a, b, c, d), v in R_mixed.items())).subs(
    {a4pp: 0, a4p: 0, a4v: 0, b4pp: 2 * H ** 2, b4p: 2 * H ** 2 * (x4 - c_shift),
     b4v: H ** 2 * (x4 - c_shift) ** 2}))) == 0,
      "K = 0 on the flat member a4 = 0, b4 = H^2 (x4 - c)^2")
```

The third check: $K = 0$ on the flat member.

**In [23], pictures: the geometry does not see $z$.**

```python
# numerical functions of the 112 components on the history: a4pp = 0 and
# b4'' = b4'^2/b4 (v = (b4'/b4)' = 0); the second derivatives are replaced first
riemann_functions = {k: numeric(v.subs({sp.Derivative(a4, (x4, 2)): 0,
                                        sp.Derivative(b4, (x4, 2)):
                                        sp.Derivative(b4, x4) ** 2 / b4}))
                     for k, v in R_mixed.items()}
```

Numerical functions of the 112 components on the history, where $a_4'' = 0$ and $b_4'' = b_4'^2/b_4$ ($v = 0$); the second derivatives are replaced first, while the components are still written with the functions.

```python
def on_history(rate):
    """a4, a4p, H, b4, b4p at the slice a4 = 0.5 for the rate a4p = rate (H = 1):
    b4 = e^(2/3) and b4'/b4 = (4/3) a4p."""
    return (0.5, rate, 1.0, B4_SLICE, 4.0 / 3.0 * rate * B4_SLICE)
```

`on_history(rate)` gives the five arguments other than $z$ at the slice $a_4 = 0.5$ for the rate $a_4' = $ `rate`: $b_4 = e^{2/3}$ and $b_4' = \frac43\,\mathrm{rate}\cdot b_4$.

```python
def kretschmann_numbers(z_values, rate):
    """K at the points z_values, summed from the 112 numerical components."""
    total = np.zeros_like(z_values)
    for (a, b, c, d), f in riemann_functions.items():
        partner = riemann_functions.get((c, d, a, b))
        if partner is not None:
            total += (f(z_values, *on_history(rate))
                      * partner(z_values, *on_history(rate)))
    return total
```

`kretschmann_numbers` sums the 112 products numerically at an array of values of $z$ (each component times its partner, `riemann_functions.get((c, d, a, b))`).

```python
z_line = np.linspace(0.02, np.pi - 0.02, 300)
z_line = z_line[np.abs(z_line - np.pi / 2) > 0.01]  # leave out the fold itself
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
fig.subplots_adjust(wspace=0.32)  # room for the label of the right vertical axis
for index, colour, style, label in (
        ((0, 0, 0), VIOLET, "--", "$\\Gamma^{x_0}{}_{x_0x_0}$ (coordinates)"),
        ((5, 5, 0), RED, "-", "$\\Gamma^{x_5}{}_{x_5x_0}$ (coordinates)")):
    values = gamma_functions[index](z_line, *on_history(1.5))
    axes[0].plot(z_line, np.abs(values), color=colour, ls=style, lw=1.8, label=label)
for key, colour, style, label in (
        ((5, 6, 5, 6), BLUE, "-.", "$\\sigma(x_5, x_6)$ (geometry)"),
        ((1, 0, 1, 0), AQUA, ":", "$\\sigma(x_1, x_0)$ (geometry)")):
    values = np.broadcast_to(riemann_functions[key](z_line, *on_history(1.5)),
                             z_line.shape)
    axes[0].plot(z_line, np.abs(values), color=colour, ls=style, lw=2.0, label=label)
axes[0].set_yscale("log")
axes[0].set_xlabel("$z = 6 H x_0$ (radians)")
axes[0].set_ylabel("absolute value (unit $H$ or $H^2$)")
axes[0].set_title("Symbols and curvatures, $a_4^{\\prime} = 1.5$")
axes[0].legend(fontsize=7, loc="upper center")
```

300 values of $z$ across the cell without the fold; on the left, the sizes of two Christoffel symbols and of two plane curvatures at $a_4' = 1.5$, on a logarithmic axis.

```python
rates = (0.5, 1.0, 1.5, 2.0)  # four expansion rates a4p = A H (A > 0), unit H
for rate, colour, style in zip(rates, (VIOLET, AQUA, RED, ORANGE),
                               ("-", "--", "-.", ":")):
    axes[1].plot(z_line, kretschmann_numbers(z_line, rate), color=colour, ls=style,
                 lw=1.8, label=f"$a_4^{{\\prime}} = {rate:g}\\,H$")
axes[1].set_yscale("log")
axes[1].set_xlabel("$z = 6 H x_0$ (radians)")
axes[1].set_ylabel("$K$ (unit $H^4$)")
axes[1].set_title("Kretschmann scalar summed from 112 components")
axes[1].legend(fontsize=8)
# the values of the formula for K at the four rates on the history, for the caption
# and the check
K_values = [float(sp.simplify(K.subs({a4p: r, a4pp: 0, H: 1, a4v: 0.5,
                                      b4v: B4_SLICE,
                                      b4p: sp.Rational(4, 3) * r * B4_SLICE,
                                      b4pp: (sp.Rational(4, 3) * r) ** 2 * B4_SLICE})))
            for r in rates]
K_text = ", ".join(f"${k:.4g}$" for k in K_values)
```

On the right, $K$ summed at 300 values of $z$ for four rates $a_4' = 0.5, 1, 1.5, 2$. `K_values` holds the values of the formula $K$ at the same four rates on the history at the slice $a_4 = 0.5$, used in the caption and in the check.

```python
save_figure(fig, "riemann_and_kretschmann_z",
            "Left: across one cell $0 < z < \\pi$, the absolute values of the "
            "Christoffel symbols $\\Gamma^{x_0}{}_{x_0x_0}$ (dashed) and "
...
numbers = [kretschmann_numbers(z_line, r) for r in rates]
check(all(np.max(np.abs(n - k)) < 1e-9 * k for n, k in zip(numbers, K_values)),
      "summed numerically, K is the same at all values of z and equals the formula")
```

The figure is saved; the check requires the numerically summed $K$ to differ from the formula by less than $10^{-9}$ of its value at every $z$, for each rate.

**What Figure 03b.5 shows.** Left: the two Christoffel symbols rise steeply towards the tips (and $\Gamma^{x_0}{}_{x_0x_0}$ also towards the fold), while the two plane curvatures are flat lines: $|\sigma(x_5, x_6)|$ and $|\sigma(x_1, x_0)|$ are the same at every $z$. Right: four flat lines, one for each rate, at the values printed in the caption: summed from 112 components that are each independent of $z$, $K$ does not see $z$.

**In [24], the curvature scalars along the history.**

```python
A = sp.symbols("A", real=True)  # the slope of the history a4 = A H x4
on_history = {a4p: A * H, a4pp: 0, b4p: BETA * A * H * b4v,
              b4pp: (BETA * A * H) ** 2 * b4v}


def along_history(expression):
    """An expression on the history, written with A, k and H."""
    value = sp.simplify(symbolic(expression).subs(on_history).subs(TO_K))
    return sp.factor(sp.expand(value))
```

`A` is the slope, `on_history` (a new meaning of the name, now a dictionary) replaces $a_4'$, $a_4''$, $b_4'$, $b_4''$ by their values on the history, and `along_history` writes an expression with $A$, $k$ and $H$ (with `TO_K` of In [18]).

```python
R_A, K_A, RR_A = (along_history(e) for e in (R_scalar, K, ricci_square))
say(f"on the history: R = {R_A}")
say(f"  K = {sp.expand(K_A)}")
say(f"  R^a_b R^b_a = {sp.expand(RR_A)}")
check(all(sp.expand(f.subs(A, -A) - f) == 0 and not f.has(b4v) and not f.has(a4v)
          for f in (R_A, K_A, RR_A)),
      "on the history the curvature scalars are even in A and depend on A and k only")
```

The three scalars on the history are printed: $R = -4H^2(-14A^2 + 27k)/9 = (\frac{56}{9}A^2 - 12k)H^2$, $K = \frac{2416}{81}A^4H^4 - \frac{16}{3}A^2kH^4 + 24k^2H^4$ and $\sum R^a{}_bR^b{}_a = \frac{1736}{81}A^4H^4 + \frac{40}{3}A^2kH^4 + 36k^2H^4$. The check requires each to be unchanged when $A$ is replaced by $-A$ and to be free of $a_4$ and $b_4$.

```python
A_line = np.linspace(0.1, 3.0, 291)  # slopes 0.1, 0.11, ..., 3; A_line[90] = 1
SLICE_K = [(0, 1.0), (1, np.exp(2.0 / 3.0)), (2, np.exp(4.0 / 3.0))]  # (a4, k)
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
for (slice_a4, k_number), style in zip(SLICE_K, ("-", "--", ":")):
    on_slice = {H: 1, k_sym: k_number}
    R_numbers = sp.lambdify(A, R_A.subs(on_slice))(A_line)
    K_numbers = sp.lambdify(A, K_A.subs(on_slice))(A_line)
    RR_numbers = sp.lambdify(A, RR_A.subs(on_slice))(A_line)
    axes[0].plot(A_line, R_numbers, color=VIOLET, ls=style, lw=1.8,
                 label=f"$R$, slice $a_4 = {slice_a4}$")
    axes[1].plot(A_line, K_numbers, color=RED, ls=style, lw=1.8,
                 label=f"$K$, slice $a_4 = {slice_a4}$")
    axes[1].plot(A_line, RR_numbers, color=BLUE, ls=style, lw=1.2,
                 label=f"$\\sum R^a{{}}_b R^b{{}}_a$, slice $a_4 = {slice_a4}$")
```

291 slopes from $0.1$ to $3$, three slices with their values of $k$, and for each slice the three scalars as functions of $A$ (`sp.lambdify(A, ...)` with $H = 1$ and $k$ put in), drawn with one line style per slice.

```python
axes[0].axhline(0.0, color="black", lw=0.8)
axes[0].set_ylabel("Ricci scalar $R$ (unit $H^2$)")
axes[0].set_title("Ricci scalar $R = (56A^2/9 - 12k)H^2$")
axes[1].set_yscale("log")
axes[1].set_ylabel("value (unit $H^4$)")
axes[1].set_title("Squares of the curvature")
for ax in axes:
    ax.axvline(1.0, color="grey", lw=1.0, ls=":")  # the canonical slope A = 1
    ax.set_xlabel("slope $A$ of the deflating history $a_4 = A H x_4$")
    ax.legend(fontsize=7, loc="upper left")
R_canonical = [float(R_A.subs({A: 1, H: 1, k_sym: k_number}))
               for _, k_number in SLICE_K]
K_canonical = float(K_A.subs({A: 1, H: 1, k_sym: 1}))
```

Axes, labels and the dotted line at the canonical $A = 1$; `R_canonical` holds $R$ at $A = 1$ on the three slices and `K_canonical` the value of $K$ at $A = 1$ on the first slice, for the caption.

```python
save_figure(fig, "scalars_versus_a",
            "The curvature scalars of the corrected metric along the deflating "
            "history $a_4 = AHx_4$, $b_4 = e^{4AHx_4/3}$ "
...
check(sp.expand(R_A - (sp.Rational(56, 9) * A ** 2 - 12 * k_sym) * H ** 2) == 0
      and abs(R_canonical[0] - (-52.0 / 9.0)) < 1e-12,
      "on the history R = (56 A^2/9 - 12 k) H^2; at A = 1, a4 = 0: R = -52/9 H^2")
```

The figure is saved; the check confirms $R = (\frac{56}{9}A^2 - 12k)H^2$ and its value $-\frac{52}{9}$ at $A = 1$ on the first slice.

**What Figure 03b.6 shows.** Left: three parabolas $R = \frac{56}{9}A^2 - 12k$, the lower the later the slice: at $A = 1$, $R = -5.778$, $-17.15$ and $-39.3$ on the three slices. Right, logarithmic: $K$ (red) and $\sum R^a{}_bR^b{}_a$ (blue), both positive for every $A$; at small $A$ they are dominated by the block term ($24k^2$ and $36k^2$) and grow with $k$ from slice to slice; at large $A$ they grow like $A^4$.

**In [25], the Einstein tensor along the history.**

```python
G_A = [along_history(G_mixed[k, k]) for k in range(8)]
for k in (0, 1, 4, 5):
    say(f"  on the history: G^{NAMES[k]}_{NAMES[k]} = {sp.expand(G_A[k])}")
check(sp.expand(G_A[4] - (6 * k_sym + A ** 2 / 3) * H ** 2) == 0
      and sp.expand(G_A[1] - (6 * k_sym - sp.Rational(13, 9) * A ** 2) * H ** 2) == 0
      and sp.expand(G_A[0] - (3 * k_sym - sp.Rational(11, 3) * A ** 2) * H ** 2) == 0
      and G_A[0] == G_A[5],
      "on the history G^x4_x4 = 6k + A^2/3, G^x1_x1 = 6k - 13 A^2/9, "
      "G^x0_x0 = G^x5_x5 = 3k - 11 A^2/3 (unit H^2)")
```

The eight diagonal entries on the history; four of them are printed, and the check confirms the three formulas of Section 3.25 and the equality of the hidden and the extra-time entry.

```python
bars = {slice_a4: [G_A[k].subs({A: 1, H: 1, k_sym: k_number}) for k in range(8)]
        for slice_a4, k_number in ((0, 1), (2, sp.exp(sp.Rational(4, 3))))}
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
positions = np.arange(8)
axes[0].bar(positions - 0.2, [float(v) for v in bars[0]], width=0.38, color=RED,
            hatch="//", label="slice $a_4 = 0$ ($k = 1$)")
axes[0].bar(positions + 0.2, [float(v) for v in bars[2]], width=0.38, color=BLUE,
            label="slice $a_4 = 2$ ($k = e^{4/3}$)")
axes[0].axhline(0.0, color="black", lw=0.8)
axes[0].set_xticks(positions, [f"$G^{{x_{k}}}{{}}_{{x_{k}}}$" for k in range(8)],
                   fontsize=8)
axes[0].set_ylabel("component (unit $H^2$)")
axes[0].set_title("Diagonal of the Einstein tensor, $A = 1$")
axes[0].set_ylim(-2.0, 29.0)  # room above the bars for the legend
axes[0].legend(fontsize=8, loc="upper left")
```

`bars` holds the eight entries at $A = 1$ on the first slice ($k = 1$) and on the last slice ($k = e^{4/3}$, exact); they are drawn as pairs of bars, hatched (`hatch="//"`) for the first slice, side by side (`positions - 0.2` and `positions + 0.2`).

```python
x4_line = np.linspace(0.0, 2.5, 251)
k_line = np.exp(2.0 * x4_line / 3.0)  # k = e^(2 a4/3) on the canonical history
component = {k: sp.lambdify(k_sym, G_A[k].subs({A: 1, H: 1}))(k_line)
             for k in (0, 1, 4)}
axes[1].plot(x4_line, component[1], color=RED, lw=1.8, label="$G^{x_1}{}_{x_1}$")
axes[1].plot(x4_line, component[0], color=AQUA, lw=1.8, ls=":",
             label="$G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5}$")
axes[1].plot(x4_line, component[4], color=VIOLET, lw=1.8, ls="--",
             label="$G^{x_4}{}_{x_4}$")
axes[1].fill_between(x4_line, component[0], component[4], color="grey", alpha=0.2,
                     label="gap $(3k + 4)H^2 > 0$")
axes[1].axhline(0.0, color="black", lw=0.8)
axes[1].set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$, "
                   "$b_4 = e^{4x_4/3}$")
axes[1].set_ylabel("component (unit $H^2$)")
axes[1].set_title("Einstein tensor along the history ($A = 1$)")
axes[1].legend(fontsize=8, loc="upper left")
```

On the right, the three different entries along the canonical history against $x_4$, with $k = e^{2x_4/3}$, and the gap between the time and the hidden entry shaded (`fill_between`).

```python
save_figure(fig, "einstein_tensor",
            "The Einstein tensor $G^{\\mu}{}_{\\nu}$ of the corrected metric along "
            "the deflating history $a_4 = AHx_4$, $b_4 = e^{4AHx_4/3}$ with "
...
check(bars[0] == [sp.Rational(-2, 3)] + [sp.Rational(41, 9)] * 3 + [sp.Rational(19, 3)]
      + [sp.Rational(-2, 3)] * 3,
      "diagonal of G at A = 1, slice a4 = 0: (-2/3, 41/9 x3, 19/3, -2/3 x3), unit H^2")
```

The figure is saved; the check compares the eight entries on the first slice exactly with their values in units of $H^2$: $-\frac23$ for $x_0$, $\frac{41}{9}$ for each 3-space direction, $\frac{19}{3}$ for $x_4$ and $-\frac23$ for each extra time.

**What Figure 03b.7 shows.** Left: on the first slice the time entry $\frac{19}{3}$ is largest, the 3-space entries are $\frac{41}{9} = 4.56$ and the four block entries are slightly negative, $-\frac23$; on the last slice all entries are larger ($7.71$, $21.3$, $23.1$), and the hidden bar still equals the extra-time bars. Right: all three entries grow along the history like $k = e^{2x_4/3}$, and the shaded gap $(3k + 4)H^2$ between the time and the hidden entry widens.

**In [26], the source that Einstein's equations require.**

```python
A4_EQUATIONS = "Revision/field_equations_a4/a4-equations.json"
a4_equations = json.loads(repository_file(A4_EQUATIONS).read_text(encoding="utf-8"))
required = a4_equations["exponentialHistory"]["requiredSource"]  # any couplings
kappa = sp.symbols("kappa", positive=True)  # the constant of Einstein's equations
Lam = sp.symbols("Lam", real=True)  # the cosmological constant Lambda
alpha1, alpha2, alpha3, be = sp.symbols("alpha1 alpha2 alpha3 be", real=True)
source_names = {"AA": A, "H": H, "kappa": kappa, "Lam": Lam, "kk": k_sym, "be": be,
                "alpha1": alpha1, "alpha2": alpha2, "alpha3": alpha3}
EINSTEIN = {alpha1: 1, alpha2: 0, alpha3: 0, be: BETA}  # Einstein, beta = 4/3
```

The record of the field equations is read, and its entry `exponentialHistory.requiredSource` is kept in `required`. New symbols for $\kappa$, $\Lambda$ (`Lam`), the three couplings and $\beta$ (`be`); `source_names` connects the record's names to them (`AA` is $A$, `kk` is $k$); `EINSTEIN` puts in the couplings of Einstein's equations and $\beta = \frac43$.

```python
def source(key):
    """The record's text required[key] (Mathematica notation) as sympy, with the
    Einstein couplings and beta = 4/3 put in."""
    text = required[key]["input"].replace("^", "**")
    return sp.expand(parse_expr(text, local_dict=source_names).subs(EINSTEIN))
```

`source(key)` reads one of the four texts, writes `^` as `**`, and puts in the Einstein couplings and $\beta$.

```python
rho_record, p0_record = source("rho"), source("p0")
p3_record, pt_record = source("p3"), source("pt")
say(f"record: kappa rho = {sp.expand(kappa * rho_record)}")
say(f"record: kappa (p3, p_t, p0) = ({sp.expand(kappa * p3_record)}, "
    f"{sp.expand(kappa * pt_record)}, {sp.expand(kappa * p0_record)})")
record_check(A4_REPORT, "json_exponential_history")  # stops if not passed
record_check(LEAD, "einstein_exponential_source_alpha1")
```

The four entries are read and printed, $\kappa\rho = -\frac13A^2H^2 - 6H^2k - \Lambda$ and $\kappa(p_3, p_t, p_0) = (-\frac{13}{9}A^2H^2 + 6H^2k + \Lambda, -\frac{11}{3}A^2H^2 + 3H^2k + \Lambda, -\frac{11}{3}A^2H^2 + 3H^2k + \Lambda)$, and two `record_check` calls confirm the sympy verification of that record and the lead's check.

```python
check(sp.expand(kappa * rho_record - (-G_A[4] - Lam)) == 0,
      "kappa rho of the record equals -G^x4_x4 - Lambda",
      record=f"{A4_EQUATIONS}, exponentialHistory.requiredSource.rho (and "
             "python-a4-report.json, check json_exponential_history)")
check(all(sp.expand(kappa * p - (G_A[k] + Lam)) == 0
          for p, k in ((p3_record, 1), (pt_record, 5), (p0_record, 0)))
      and sp.expand(pt_record - p0_record) == 0,
      "kappa p3, kappa p_t, kappa p0 of the record equal G^x1_x1, G^x5_x5, G^x0_x0 "
      "plus Lambda, and p_t = p0",
      record=f"{A4_EQUATIONS}, exponentialHistory.requiredSource.p3, pt, p0")
```

The first check: $\kappa\rho = -G^{x_4}{}_{x_4} - \Lambda$. The second: $\kappa p_3$, $\kappa p_t$, $\kappa p_0$ equal $G^{x_1}{}_{x_1}$, $G^{x_5}{}_{x_5}$, $G^{x_0}{}_{x_0}$ plus $\Lambda$, and $p_t = p_0$.

```python
history_source = json.loads(repository_file(
    "Revision/metric_warped/results/warped-metric.json").read_text(
    encoding="utf-8"))["history_source"]["einstein_A1_beta43"]
on_canonical = {A: 1, k_sym: sp.exp(2 * H * x4 / 3)}  # k = e^(2 H x4/3) for A = 1
canonical_ok = all(sp.simplify(parse_expr(history_source[key], local_dict={
    "H": H, "x4": x4, "exp": sp.exp}) - G_A[k].subs(on_canonical)) == 0
    for key, k in (("-rho", 4), ("p3", 1), ("p0", 0), ("p_t", 5)))
check(canonical_ok
      and sp.expand(kappa * (rho_record + p0_record)
                    + (3 * k_sym + 4 * A ** 2) * H ** 2) == 0,
      "the record of the corrected metric gives the same source for A = 1, and "
      "kappa (rho + p0) = -(3k + 4 A^2) H^2 < 0",
      record="Revision/metric_warped/results/warped-metric.json, "
             "history_source.einstein_A1_beta43")
```

The record of the corrected metric writes the same source for $A = 1$ as functions of $x_4$; each of its four texts is read and compared with our entry with $k = e^{2Hx_4/3}$. The third check requires all four to agree and $\kappa(\rho + p_0) = -(3k + 4A^2)H^2$.

**In [27], the negative control.**

```python
cube_root = sp.sin(6 * H * x0) ** sp.Rational(1, 3)  # sin(z)^(1/3), sin z > 0 here
g_withdrawn = sp.diag(sp.cot(6 * H * x0) ** 2,
                      *[sp.exp(2 * a4) * cube_root] * 3, -1,
                      *[-b4 * sp.exp(-2 * a4) * cube_root] * 3)
Gamma_old = christoffel(g_withdrawn, X)
R_old = raise_second(riemann(Gamma_old, X), g_withdrawn)
Ric_old = ricci(R_old, 8)
G_old = (Ric_old - Ric_old.trace() / 2 * sp.eye(8)).applyfunc(tidy)
off = {(i, j): plain(G_old[i, j]) for i in range(8) for j in range(8)
       if i != j and G_old[i, j] != 0}
for (i, j), value in sorted(off.items()):
```

The withdrawn metric of 2026-10-14 is built as a sympy matrix (the cube root $\sin^{1/3}z$ is the ordinary one, because the control is used on the half cell $0 < z < \pi/2$, where $\sin z > 0$); its Christoffel symbols, Riemann tensor, Ricci tensor and Einstein tensor are computed with the same functions as above, and the non-zero entries off the diagonal are collected in `off`.

```python
    say(f"  withdrawn metric: G^{NAMES[i]}_{NAMES[j]} = {value}")
WARPED = "Revision/metric_warped/results/warped-metric.json"
old_record = json.loads(repository_file(WARPED).read_text(encoding="utf-8"))
old_text = old_record["metric_of_2026_10_14_offdiagonal"]["E1^x4_x0"]
say(f"record (metric of 2026-10-14): E1^x4_x0 = {old_text}")
old_value = parse_expr(old_text, local_dict={
    "H": H, "bd1": b4p, "bb": b4v, "cv": sp.cos(6 * H * x0), "sv": sp.sin(6 * H * x0)})
```

The output shows two entries off the diagonal: `G^x0_x4 = -3*H*b4p*tan(z)/(2*b4v)` and `G^x4_x0 = 3*H*b4p/(2*b4v*tan(z))`, that is $\frac32 H\cot z\,b_4'/b_4$. The record of the corrected metric keeps the second as dated history; its text, `3*H*bd1*cv/(2*bb*sv)`, is printed and read with its names (`bd1` for $b_4'$, `bb` for $b_4$, `cv` and `sv` for $\cos z$ and $\sin z$).

```python
record_check(WARPED_REPORT, "record_metric_offdiagonal_reproduced")
check(sorted(off) == [(0, 4), (4, 0)]
      and vanishes(symbolic(G_old[4, 0]) - old_value)
      and vanishes(symbolic(G_old[4, 0]) - sp.Rational(3, 2) * H
                   * sp.cot(6 * H * x0) * b4p / b4v),
      "negative control: the withdrawn metric has G^x4_x0 = (3/2) H cot z b4'/b4 "
      "and G^x0_x4 off the diagonal",
      record=f"{WARPED}, metric_of_2026_10_14_offdiagonal (and "
             "python-warped-metric-report.json, check "
             "record_metric_offdiagonal_reproduced)")
```

After `record_check`, the check requires exactly the two off-diagonal entries $(x_0, x_4)$ and $(x_4, x_0)$, and the second to equal both the record's text and $\frac32 H\cot z\,b_4'/b_4$. The same code finds no such entry in the corrected metric (In [20]).

**In [28], the last check.**

```python
figure_names = ["christoffel_heat_maps", "christoffel_versus_z",
                "finite_differences", "plane_curvatures",
                "riemann_and_kretschmann_z", "scalars_versus_a", "einstein_tensor"]
files = [output_file(f"{FIGURE_FOLDER}/03b_{k}_{n}.png")
         for k, n in enumerate(figure_names, 1)]
check(all(path.is_file() for path in files), "all seven figure files exist")
all_checks_passed()
```

The seven figure files must exist; the last line prints ALL 43 CHECKS PASSED (notebook 03b). The 43 checks are: 1 each in In [4] and In [6], 2 in In [7], 1 each in In [8] and In [9], 2 in In [10], 1 in In [11], 2 in In [12], 1 in In [13], 4 in In [14], 2 in In [15], 3 in In [16], 1 each in In [17], In [18] and In [19], 5 in In [20], 1 in In [21], 3 in In [22], 1 in In [23], 2 each in In [24] and In [25], 3 in In [26], and 1 each in In [27] and In [28].

### 3.31 Free fall in the author's metric

What does the corrected metric do to a body that moves in it with no force acting on it, only the geometry? This section answers with the geodesic equation of Section 3.16 and the Christoffel symbols of Section 3.23.

**Test particles in free fall.** A **test particle** is a body so small that it does not change the metric (ASSUMED: the particles of this section are test particles). In free fall it moves on a time-like geodesic (Section 3.16; ASSUMED from the theory of gravity), parametrised by its proper time $\tau$, with the velocity $u^a = dx^a/d\tau$ and $g(u, u) = -1$. We keep the labels of Section 3.23: $i$ for 3-space, $j$ for the extra times; the hidden direction $x_0$ and the extra times form the block.

**The geodesic equations.** $du^a/d\tau = -\sum_{b,c}\Gamma^a{}_{bc}u^bu^c$ with the 31 symbols of Section 3.23 (a symbol with two different lower indices appears twice, once in each order, hence the factors 2), with the rates $a_4'$ of 3-space and $\alpha_t = -a_4' + b_4'/(2b_4)$ of the block, $f = e^{-a_4}b_4^{1/2}$ and $W = (\sin^2 z)^{1/12}$:

$$
\frac{du^0}{d\tau} = 6H(\tan z + \cot z)(u^0)^2 - 2\alpha_t\,u^0u^4 - HW^2\tan z\sum_j(u^j)^2,
$$

$$
\frac{du^i}{d\tau} = -2a_4'\,u^iu^4, \qquad \frac{du^j}{d\tau} = -2H\cot z\,u^0u^j - 2\alpha_t\,u^4u^j,
$$

$$
\frac{du^4}{d\tau} = -\alpha_tf^2\cot^2 z\,(u^0)^2 - a_4'e^{2a_4}\sum_i(u^i)^2 + \alpha_tf^2W^2\sum_j(u^j)^2
$$

(for $u^0$ the symbols $\Gamma^0{}_{00} = -6H(\tan z + \cot z)$, $\Gamma^0{}_{04} = \alpha_t$ and $\Gamma^0{}_{jj} = HW^2\tan z$, and no symbol $\Gamma^0{}_{ii}$, because 3-space has no warp; for $u^i$ the symbol $\Gamma^i{}_{i4} = a_4'$ alone; for $u^j$ the symbols $\Gamma^j{}_{j0} = H\cot z$ and $\Gamma^j{}_{j4} = \alpha_t$; for $u^4$ the symbols $\Gamma^4{}_{00} = \alpha_tf^2\cot^2 z$, $\Gamma^4{}_{ii} = a_4'e^{2a_4}$ and $\Gamma^4{}_{jj} = -\alpha_tf^2W^2$; each moved to the right side with its minus sign). On the history of Section 3.8, $\alpha_t = -a_4'/3$. Together with $dx^a/d\tau = u^a$ these are 16 first-order equations for the 8 coordinates and the 8 velocities (Notebook 03d builds them from the record's symbols and prints the one for $u^5$, In [4]).

**Six conserved momenta.** The metric does not depend on the six coordinates $x_1, x_2, x_3, x_5, x_6, x_7$, so by Section 3.16 the six **momenta** $p_k = g_{kk}u^k$ (no sum) do not change during free fall:

$$
p_i = e^{2a_4}\,u^i, \qquad p_j = -f^2W^2\,u^j \qquad\text{(both constant)} .
$$

For $p_5$ we follow the proof of Section 3.16 once more, line by line. First, by the product rule and the chain rule ($g_{55}$ depends on $x_4$ and $x_0$ only),

$$
\frac{dp_5}{d\tau} = \bigl(\partial_4g_{55}\,u^4 + \partial_0g_{55}\,u^0\bigr)u^5 + g_{55}\,\frac{du^5}{d\tau} .
$$

Second, $g_{55} = -f^2W^2$ gives $\partial_4g_{55} = 2\alpha_t\,g_{55}$ and $\partial_0g_{55} = 2H\cot z\,g_{55}$ (the logarithmic derivatives $\partial_4\ln f = \alpha_t$ and $\partial_0\ln W = H\cot z$ of Section 3.23, each doubled for the square). Third, with the geodesic equation for $u^5$,

$$
\frac{dp_5}{d\tau} = 2\alpha_tg_{55}u^4u^5 + 2H\cot z\,g_{55}u^0u^5 - 2H\cot z\,g_{55}u^0u^5 - 2\alpha_tg_{55}u^4u^5 = 0 .
$$

For 3-space it is shorter: $\partial_4g_{11} = 2a_4'g_{11}$, $\partial_0g_{11} = 0$, and $dp_1/d\tau = 2a_4'g_{11}u^4u^1 + g_{11}(-2a_4'u^1u^4) = 0$. The squared length $g(u, u)$ is conserved as well (Section 3.16). PROVED for every diagonal metric that does not depend on $x_k$; Notebook 03d proves it again with sympy for all six momenta and for $g(u, u)$, for general $a_4(x_4)$ and $b_4(x_4)$ and every real $z$ (In [4]).

**Frame velocities: redshift in 3-space, blueshift along the extra times.** An observer at rest at the particle's place measures lengths and durations with the frame of Section 3.7. Per unit of the particle's proper time, the particle covers along $x_a$ the proper length (along an extra time, the proper duration) $\hat u^a = h_au^a$, its **frame velocity**. From the momenta, $p_i = h_i^2u^i$ and $p_j = -h_j^2u^j$, so

$$
\hat u^i = h_iu^i = \frac{p_i}{h_i} = p_i\,e^{-a_4}, \qquad \hat u^j = h_ju^j = -\frac{p_j}{h_j} = -\frac{p_j}{fW} = -p_j\,b_4^{-1/2}e^{a_4 - Hy}
$$

(divide the momentum by the scale factor; $1/h_i = e^{-a_4}$; $1/(fW) = e^{a_4}b_4^{-1/2}e^{-Hy}$ with $W = e^{Hy}$, Section 3.9). Along a deflating history ($a_4' > 0$ and $\alpha_t < 0$) the frame velocity in 3-space falls like $e^{-a_4}$, at every height in the hidden direction alike: motion in 3-space is **redshifted**, because 3-space inflates and stretches it out, and it does not care where in the hidden direction it happens, because 3-space has no warp. The frame velocity along an extra time grows like $1/f = b_4^{-1/2}e^{a_4} = e^{-\int\alpha_t\,dx_4}$, on the history of Section 3.8 like $e^{a_4/3}$: motion along the extra times is **blueshifted**, because they deflate; and at a lower height $y$ it is larger by the factor $e^{-Hy}$. The factor $e^{-a_4}$ is exactly the **momentum weight** $\kappa(x_4) = e^{-a_4(x_4)}$ that the Revision Kohn-Sham record uses to turn a conserved 3-space momentum into the momentum seen at time $x_4$ (`Revision/kohn_sham/ks-theory.json`, key `geometry.kappa`, which adds that it does not depend on $y$; this $\kappa(x_4)$, always written in this chapter with its argument, is a function and has nothing to do with the constant $\kappa$ of Einstein's equations in Section 3.26). PROVED here; Notebook 03d, In [5]. It contains neither $b_4$ nor $y$: the 3-space scale factors contain neither.

**The push along the hidden direction.** Write $S = \sum_i(\hat u^i)^2$ and $E = \sum_j(\hat u^j)^2$ for the squared frame velocities in 3-space and along the extra times. The frame velocity along the hidden direction is $\hat u^0 = h_0u^0 = f\cot z\,u^0$ (with the sign of $\cot z$ kept in $h_0$, as in the record's vielbein, Section 3.7), and it equals $f\,dy/d\tau$, because $dy/d\tau = (dy/dx_0)(dx_0/d\tau) = \cot z\,u^0$ (Section 3.9), in either half of a cell. The rate of change of $f\hat u^0 = f^2\cot z\,u^0$, line by line:

$$
\frac{d}{d\tau}\bigl(f^2\cot z\,u^0\bigr) = \partial_4(f^2)\,u^4\cot z\,u^0 + f^2\,\frac{d\cot z}{d\tau}\,u^0 + f^2\cot z\,\frac{du^0}{d\tau}
$$

(the product rule; $f$ depends on $x_4$ only)

$$
\begin{aligned}
= {} & 2\alpha_tf^2\cot z\,u^0u^4 - \frac{6Hf^2}{\sin^2 z}(u^0)^2\\
& + f^2\cot z\Bigl[6H(\tan z + \cot z)(u^0)^2 - 2\alpha_tu^0u^4 - HW^2\tan z\sum_j(u^j)^2\Bigr]
\end{aligned}
$$

($\partial_4 f^2 = 2\alpha_tf^2$; $d\cot z/d\tau = -\frac{1}{\sin^2 z}\cdot 6H\cdot u^0$ by the chain rule; the geodesic equation for $u^0$)

$$
= -\frac{6Hf^2}{\sin^2 z}(u^0)^2 + 6Hf^2\bigl(1 + \cot^2 z\bigr)(u^0)^2 - Hf^2W^2\sum_j(u^j)^2
$$

($\cot z\tan z = 1$; the two terms with $u^0u^4$ cancel)

$$
= -H\sum_j(\hat u^j)^2
$$

($1 + \cot^2 z = 1/\sin^2 z$, so the two terms with $(u^0)^2$ cancel; $f^2W^2(u^j)^2 = (h_ju^j)^2 = (\hat u^j)^2$). Hence

$$
\frac{d}{d\tau}\Bigl(f^2\,\frac{dy}{d\tau}\Bigr) = \frac{d}{d\tau}\bigl(f\,\hat u^0\bigr) = -H\sum_j(\hat u^j)^2 = -HE .
$$

Only motion along an extra time pushes the particle along the hidden direction, and always towards the tip, where $y \to -\infty$ in either half of a cell. Motion in 3-space does not push at all, because 3-space has no warp. Without extra-time motion $f^2\,dy/d\tau$ is conserved: a particle at rest in $y$ stays at its height, and a motion along $y$ is blueshifted like $1/f$, like a motion along an extra time, because the hidden direction belongs to the block. Neither $a_4$ nor $b_4$ appears on the right side (PROVED; Notebook 03d, In [6]).

**The law of the time $x_4$.** In the geodesic equation for $u^4$, $f^2\cot^2 z\,(u^0)^2 = (\hat u^0)^2$, $e^{2a_4}(u^i)^2 = (\hat u^i)^2$ and $f^2W^2(u^j)^2 = (\hat u^j)^2$ (each term is a scale factor squared times a velocity squared), so

$$
\frac{du^4}{d\tau} = -a_4'S - \alpha_t\bigl((\hat u^0)^2 - E\bigr) .
$$

Along a deflating history ($a_4' > 0$ and $\alpha_t < 0$; on the history of Section 3.8, $\alpha_t = -a_4'/3$) motion in 3-space and along the extra times lowers the $x_4$ velocity, and motion along the hidden direction raises it (PROVED; Notebook 03d, In [6]).

**The $x_4$ velocity from the squared length.** The squared length, written with frame velocities, is

$$
g(u, u) = h_0^2(u^0)^2 + \sum_i h_i^2(u^i)^2 - (u^4)^2 - \sum_j h_j^2(u^j)^2 = (\hat u^0)^2 + S - (u^4)^2 - E
$$

(the diagonal entries $+h_0^2$, $+h_i^2$, $-1$, $-h_j^2$ of the metric). Setting it equal to $-1$ and solving for $(u^4)^2$:

$$
(u^4)^2 = 1 + (\hat u^0)^2 + \sum_i(\hat u^i)^2 - \sum_j(\hat u^j)^2 = 1 + (\hat u^0)^2 + S - E
$$

(PROVED, for every $a_4$ and $b_4$; Notebook 03d, In [6]).

**A particle without 3-space motion: an exact law for $u^4$.** For $S = 0$ the last formula gives $(\hat u^0)^2 - E = (u^4)^2 - 1$, and the law of $x_4$ closes on $u^4$ alone: $du^4/d\tau = -\alpha_t\bigl((u^4)^2 - 1\bigr)$. On the history of Section 3.8 the rate $\alpha_t = -AH/3$ is constant, so $du^4/d\tau = \frac{AH}{3}\bigl((u^4)^2 - 1\bigr)$. With $q = (1 - u^4)/(1 + u^4)$:

$$
\frac{dq}{d\tau} = -\frac{2}{(1 + u^4)^2}\,\frac{du^4}{d\tau} = -\frac{2}{(1 + u^4)^2}\cdot\frac{AH}{3}\,(u^4 - 1)(u^4 + 1) = \frac{2AH}{3}\,\frac{1 - u^4}{1 + u^4} = \frac{2AH}{3}\,q
$$

(the quotient rule, $\frac{d}{du}\frac{1 - u}{1 + u} = \frac{-(1 + u) - (1 - u)}{(1 + u)^2} = -\frac{2}{(1 + u)^2}$; then $(u^4)^2 - 1 = (u^4 - 1)(u^4 + 1)$). Therefore

$$
q(\tau) = q(0)\,e^{2AH\tau/3}, \qquad u^4(\tau) = \frac{1 - q(\tau)}{1 + q(\tau)}
$$

(the derivative of $q(0)e^{2AH\tau/3}$ is $\frac{2AH}{3}$ times itself by the chain rule, and an initial-value problem has only one solution, Chapter 2; the second formula is the definition of $q$ solved for $u^4$). PROVED; Notebook 03d checks the computed $u^4$ against it at every step (In [11]). As $q$ grows, $u^4$ falls; the formula reaches $u^4 = 0$ at $q = 1$, that is at $\tau = \frac{3}{2AH}\ln\frac{1}{q(0)}$, if the path lasts that long.

**Turning points.** An instant at which $u^4$ passes through zero is a **turning point**: $x_4$ stops growing there. A particle without extra-time motion ($p_j = 0$, so $\hat u^j = 0$ for ever, because the momenta are conserved) has $(u^4)^2 = 1 + (\hat u^0)^2 + S \ge 1$: $u^4$ never reaches zero, keeps its sign, and $x_4$ keeps advancing; nothing pushes it towards the tip. With extra-time motion $(u^4)^2$ can fall towards zero. If a turning point is reached on a deflating history, the law of $x_4$ with $(\hat u^0)^2 - E = -1 - S$ (the formula for $(u^4)^2$ with $u^4 = 0$) gives

$$
\frac{du^4}{d\tau} = -a_4'S + \alpha_t(1 + S) = \alpha_t - (a_4' - \alpha_t)\,S < 0
$$

($\alpha_t < 0$ and $a_4' - \alpha_t > 0$): $u^4$ becomes negative and $x_4$ decreases afterwards. With four time-like directions, a time-like path need not keep advancing in the chosen time $x_4$ (PROVED). Whether a path reaches a turning point before it reaches the tip depends on the path (Exercise 10 (d) finds the condition for the simplest paths). The particle of Notebook 03d, started along $x_5$ with the frame velocity $0.2$, does not: its formula would give $u^4 = 0$ at $\tau = 6.877$, but it passes the tip cut-off of the Kohn-Sham solver already at $\tau = 2.694$ (In [11]), and Exercise 10 solves its path exactly and finds that it reaches the tip itself at $\tau = 2.814$, with $u^4 = 0.875$ (PROVED by hand there; no notebook computes the path beyond the cut-off). This does not contradict the infinite proper distance of the tip (Section 3.9): that distance is measured at fixed extra times, while this particle also moves along $x_5$, and in $g(u, u)$ the extra-time motion counts with the sign opposite to that of the motion along $y$. A particle that moves towards the fold without extra-time motion keeps $f^2\,dy/d\tau$ constant, so on a deflating history, where $f$ shrinks, its $dy/d\tau$ grows and it reaches the fold $y = 0$. What happens to a path at the tip or at the fold is not computed in this chapter: **OPEN** (Sections 3.5 and 3.9).

**The same quadratic form as the plane waves of the Revision record.** Multiply the formula for $(u^4)^2$ by $m^2$, the squared mass of the particle, and write $k_a = m\hat u^a$ for its frame momenta and $\mathcal E = m u^4$ for its energy:

$$
\mathcal E^2 = m^2 + k_0^2 + k_1^2 + k_2^2 + k_3^2 - k_5^2 - k_6^2 - k_7^2 .
$$

The Revision scope report finds exactly this expression for the squared frequency of plane waves of the fields of the book in flat 4+4 space (or with the coefficients of the field equation frozen at one instant): a wave with the momenta $k_a$ has $\mathcal E^2$ equal to it, and when the extra-time momentum is so large that $\mathcal E^2 < 0$ the frequency is imaginary and the wave grows exponentially in $x_4$, with a rate that has no upper bound (`Revision/theory/reports/python-scope.json`, check `extra_time_growth_rates_unbounded`; Chapter 8 studies this). The identity of the two quadratic forms is PROVED (Notebook 03d, In [7]). A particle can never be where $\mathcal E^2 < 0$, because $(u^4)^2 \ge 0$; where a plane wave would start to grow, the particle would instead reach a turning point. Whether wave packets of the fields follow these geodesics in the curved metric is NOT computed in this book: **OPEN**.

**The good sector.** The Revision Kohn-Sham work keeps only states that do not depend on $x_5, x_6, x_7$: their extra-time momenta are zero (`Revision/kohn_sham/ks-theory.json`, key `sectorAndAnsatz.sector`: "good sector: no dependence on x5, x6, x7 (extra-time momenta zero)"). The particle with the same property, $p_j = 0$, is the one that never turns and is never pushed towards the tip. The reason for this choice of the record comes from the quantum theory (Chapter 10).

**Numbers along the history (COMPUTED by Notebook 03d).** With the history of the record ($A = 1$, $H = 1$, $\beta = 4/3$ and $b_4(0) = 1$, so $a_4 = x_4$ and $b_4 = e^{4x_4/3}$; ASSUMED, a prescribed background, Section 3.8), RK4 with the step $\Delta\tau = 0.001$ ($0.00025$ for the particle that moves along an extra time, which moves ever faster near the tip), all particles starting at $x_4 = 0$ and $y = -1$ ($z = \arcsin e^{-6} = 0.002479$): a particle at rest stays at rest with $x_4 = \tau$ (In [9]). Three particles started along $x_1$ with the frame velocities $0.25$, $0.5$ and $1$ keep $p_1$ and $g(u, u)$ constant within a relative $10^{-9}$, their frame velocity equals $p_1\kappa(x_4) = p_1e^{-a_4}$ within $10^{-9}$, $u^4$ falls at every step, and their $x_0$ does not change at all; the fastest has at $\tau = 3$ the values $x_4 = 3.1878$, $\hat u^1 = 0.041263$, $u^4 = 1.000851$ and $y = -1.0000$: it has slowed down by the redshift and stayed at its height (In [10]; Exercise 8 derives its path exactly and reproduces the first three numbers). A particle started along $x_5$ with $\hat u^5 = 0.2$, so $u^4 = 0.980$, sinks towards the tip ever faster and passes the tip cut-off $y = -3$ at $\tau = 2.694$, where $x_4 = 2.5457$, $\hat u^5 = 3.4535$, $\hat u^0 = -3.4217$ and $u^4 = 0.884124$; its $u^4$ follows the exact formula within $10^{-9}$ at every step, and the formula puts the turning point at $\tau = 6.877$ (In [11]). Its blueshift alone, $0.2\,e^{a_4/3}$, would have raised $\hat u^5$ only to $0.2\,e^{2.5457/3} = 0.47$; the remaining factor $3.4535/0.47 = 7.4$ is $e^{-H(y - y_0)} \approx e^2$, the sinking from $y = -1$ to $y = -3$. The numerical rate of $f\hat u^0$ agrees with the push law within $4.3 \times 10^{-6}$ of the largest value of the law along the path (In [14]), and halving the RK4 step divides the error by 16.1 to 16.4, the order 4 of RK4 (In [16]).

### 3.32 Example: free fall in the author's metric

Notebook 03d reads the 21 Christoffel symbols of the record, builds the geodesic equations, and proves with sympy, for general $a_4(x_4)$ and $b_4(x_4)$ and every real $z$, the conservation of the six momenta and of $g(u, u)$, the momentum weight $\kappa(x_4) = e^{-a_4}$ of the Kohn-Sham record, the push law, the law of the $x_4$ velocity, the formula for $(u^4)^2$, and its identity with the quadratic form of the record's plane-wave check. Then it integrates five paths with RK4 along the history of the record ($a_4 = x_4$, $b_4 = e^{4x_4/3}$), checks every exact law on the computed paths, follows the particle that moves along an extra time until it passes the tip cut-off, compares its $x_4$ velocity with the exact formula, measures the order of RK4, and draws five figures. It needs no Rust, runs in about 50 seconds and ends with the line ALL 23 CHECKS PASSED (notebook 03d).

<!-- NOTEBOOK 03d -->

### 3.35 Line-by-line walk-through of Notebook 03d

The notebook has 17 code cells, In [1] to In [17]. The conventions of the earlier walk-throughs apply: a line or a small group of lines is quoted and then explained, and a line `...` in a quoted figure command stands for the remaining lines of the caption, printed in full under its figure in Section 3.34.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 3.33. Its code is, line for line, the set-up code of Notebook 03a explained in Section 3.13 under In [1], with the single difference `NOTEBOOK_ID = "03d"  # this notebook: chapter 03, example d`. It prints Set-up of notebook 03d complete: repository folder found, helpers defined.

**In [2], every result in one piece.** Word for word In [2] of Notebook 03a (Section 3.13). It prints From now on check and report print each of their results in one piece.

**In [3], the Christoffel symbols of the record.**

```python
import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols
from sympy.parsing.sympy_parser import parse_expr  # text -> sympy expression

CURVATURE_RECORD = "Revision/gkd_lovelock/results/curvature.json"
record = json.loads(repository_file(CURVATURE_RECORD).read_text(encoding="utf-8"))
NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
X = sp.symbols("x0:8", real=True)  # the coordinates x0 ... x7 (X[0] ... X[7])
x4, x0 = X[4], X[0]
```

The packages (numpy for arrays of numbers, sympy for exact algebra, and its text reader `parse_expr`), the record of the curvature computation, the names of the coordinates in the author's order, and the eight coordinates as the tuple `X` (a tuple is a list that cannot be changed); `x4` and `x0` name its entries 4 and 0.

```python
H = sp.symbols("H", positive=True)  # the constant of the author
a4 = sp.Function("a4")(x4)  # the metric function a4, any function of x4
b4 = sp.Function("b4", positive=True)(x4)  # the metric function b4 > 0
```

The constant $H > 0$ and the two metric functions $a_4(x_4)$ and $b_4(x_4)$, the second declared positive, both left completely general.

```python
class W(sp.Function):
    """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

    def fdiff(self, argindex=1):
        """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
        return H * sp.cot(6 * H * self.args[0]) * self
```

The warp factor $W(x_0) = (\sin^2 z)^{1/12}$ as a sympy function class, exactly as in Notebook 03b (Section 3.30, In [3]): its method `fdiff` gives sympy the derivative $dW/dx_0 = H\cot z\,W$, so that every derivative taken below holds for every real $z$ with $\sin z \ne 0$, without a decision about the sign of $\sin z$.

```python
a4p, a4v, b4p = sp.symbols("a4p a4v b4p", real=True)  # printing names
b4v = sp.symbols("b4v", positive=True)  # printing name of the value of b4
record_names = {"a4p": a4p, "a4v": a4v, "b4p": b4p, "b4v": b4v, "H": H, "x0": x0,
                "E": sp.E, "sin": sp.sin, "cot": sp.cot, "W": W}
```

The plain symbols that stand for $a_4'$, the value of $a_4$, $b_4'$ and the value of $b_4$ (the last one positive), and the dictionary of the names that may occur in a translated entry of the record, with `W` for the warp factor (as in Notebook 03b, Section 3.30, In [5]).

```python
def from_mathematica(entry_text):
    """A value of the record (Mathematica notation) as a sympy expression."""
    t = entry_text.replace("(Sin[6*H*x0]^2)^(1/6)", "W(x0)^2")  # the warp squared
    t = t.replace("Derivative[1][a4][x4]", "a4p").replace("a4[x4]", "a4v")
    t = t.replace("Derivative[1][b4][x4]", "b4p").replace("b4[x4]", "b4v")
    t = t.replace("Sin[6*H*x0]", "sin(6*H*x0)").replace("Cot[6*H*x0]", "cot(6*H*x0)")
    t = t.replace("^", "**")
    if "[" in t or "]" in t:  # a piece of notation that was not translated
        raise ValueError(f"cannot translate {entry_text}")
    return parse_expr(t, local_dict=record_names)
```

The translation of a record entry into sympy, the same as in Notebook 03b but without $a_4''$ and $b_4''$, which no Christoffel symbol contains. The first replacement turns the record's `(Sin[6*H*x0]^2)^(1/6)`, which is $W^2$, into `W(x0)^2`; the others turn the derivatives and the values of $a_4$ and $b_4$ into the four plain symbols, the square brackets of the sine and the cotangent into round ones, and `^` into `**`. A square bracket left over means a piece of notation that was not translated, and the function stops with an error instead of guessing.

```python
Gamma = {}  # (a, b, c) -> the value of Gamma^a_bc, with a4p, a4v, b4p, b4v
for entry in record["christoffelNonzero_b_le_c"]:
    a, b, c = (NAMES.index(entry[key]) for key in ("a", "b", "c"))
    Gamma[(a, b, c)] = from_mathematica(entry["value"])
    Gamma[(a, c, b)] = Gamma[(a, b, c)]  # the same symbol with b and c exchanged
```

The dictionary `Gamma` holds the symbols. For each of the 21 entries of the record, the three names of `a`, `b`, `c` become positions (the expression in round brackets produces three numbers, which are unpacked into `a, b, c`), the value is translated, and it is stored under both orders of the lower indices. For the 11 entries with $b = c$ both keys are the same, so the 21 entries give $11 + 2 \times 10 = 31$ keys (the list of Section 3.23).

```python
for key in [(1, 1, 4), (4, 5, 5), (0, 5, 5), (0, 0, 4)]:
    a, b, c = key
    say(f"  Gamma^{NAMES[a]}_({NAMES[b]} {NAMES[c]}) = {Gamma[key]}")
report("entries of the record (b <= c)", len(record["christoffelNonzero_b_le_c"]))
check(len(record["christoffelNonzero_b_le_c"]) == 21 and len(Gamma) == 31,
      "the 21 entries of the record give 31 non-zero Christoffel symbols",
      record=f"{CURVATURE_RECORD}, christoffelNonzero_b_le_c")
```

Four symbols are printed in the form in which the translation leaves them, because it does not simplify:

```text
  Gamma^x1_(x1 x4) = a4p
  Gamma^x4_(x5 x5) = a4p*b4v*W(x0)**2*exp(-2*a4v) - b4p*W(x0)**2*exp(-2*a4v)/2
  Gamma^x0_(x5 x5) = H*W(x0)**2/cot(6*H*x0)
  Gamma^x0_(x0 x4) = -a4p + b4p/(2*b4v)
```

They are $\Gamma^{x_1}{}_{x_1x_4} = a_4'$, $\Gamma^{x_4}{}_{x_5x_5} = \bigl(a_4'b_4 - \tfrac12 b_4'\bigr)e^{-2a_4}W^2 = -\alpha_t f^2W^2$, $\Gamma^{x_0}{}_{x_5x_5} = HW^2\tan z$ and $\Gamma^{x_0}{}_{x_0x_4} = \alpha_t$ (Section 3.23); the keys are positions in the author's order, `(1, 1, 4)` for $\Gamma^{x_1}{}_{x_1x_4}$ and `(0, 0, 4)` for $\Gamma^{x_0}{}_{x_0x_4}$. The RESULT line prints 21, and the check confirms the counts 21 and 31.

**In [4], what stays constant (exact).**

```python
u = sp.symbols("u0:8", real=True)  # the velocity components u^0 ... u^7
# back to the functions a4(x4) and b4(x4)
to_function = {a4p: sp.Derivative(a4, x4), a4v: a4, b4p: sp.Derivative(b4, x4),
               b4v: b4}
acceleration = [sp.S(0)] * 8  # du^a/dtau from the geodesic equation
for (a, b, c), value in Gamma.items():
    acceleration[a] -= value.subs(to_function) * u[b] * u[c]
```

The eight velocity components $u^0, \dots, u^7$ as symbols (`u[k]` is $u^k$). `to_function` turns the plain symbols back into the derivatives and the values of the functions $a_4(x_4)$ and $b_4(x_4)$, so that sympy can differentiate along the path. `acceleration` starts as eight zeros (`sp.S(0)` is sympy's zero); the loop subtracts $\Gamma^a{}_{bc}u^bu^c$ for every one of the 31 keys, which is the geodesic equation $du^a/d\tau = -\sum_{b,c}\Gamma^a{}_{bc}u^bu^c$ (both orders of two different lower indices are in the dictionary, so the factors 2 of Section 3.31 appear by themselves).

```python
def along_path(f):
    """The rate of change df/dtau of f(x, u) along a path of free fall."""
    return sum(sp.diff(f, X[k]) * u[k] + sp.diff(f, u[k]) * acceleration[k]
               for k in range(8))
```

The rate of change of a quantity $F(x, u)$ along a path of free fall, by the chain rule: $dF/d\tau = \sum_a(\partial F/\partial x^a)\,u^a + \sum_a(\partial F/\partial u^a)\,du^a/d\tau$, with $du^a/d\tau$ from the geodesic equation.

```python
f_hidden = sp.exp(-a4) * sp.sqrt(b4)  # f = e^(-a4) b4^(1/2), the hidden scale
# the eight scale factors h_a in the author's order x0, x1, ..., x7 (x0 with the
# sign of cot z, as in the record)
h = [f_hidden * sp.cot(6 * H * x0)] + [sp.exp(a4)] * 3 + [sp.Integer(1)] \
    + [f_hidden * W(x0)] * 3
ETA = [1, 1, 1, 1, -1, -1, -1, -1]  # the signs of the metric entries
g = [ETA[k] * h[k] ** 2 for k in range(8)]  # the diagonal of the metric
```

The hidden scale $f = e^{-a_4}b_4^{1/2}$, the eight scale factors in the author's order ($h_0 = f\cot z$ with the sign of $\cot z$, as in the record's vielbein, Section 3.7; then three times $e^{a_4}$, the $1$ of $x_4$, and three times $fW$), the signs, and the diagonal $g_{aa} = \eta_{aa}h_a^2$ (the sign of $h_0$ drops out in the square). The backslash `\` at the end of a line continues the statement on the next line.

```python
say(f"du5/dtau = {sp.factor(acceleration[5]).subs(sp.Derivative(a4, x4), a4p)}")
```

The geodesic equation for $u^5$ (`acceleration[5]`), factored, with $a_4'$ printed as `a4p`:

```text
du5/dtau = -u5*(2*H*u0*b4(x4)*cot(6*H*x0) - 2*a4p*u4*b4(x4) + u4*Derivative(b4(x4),
    x4))/b4(x4)
```

Divided out, this is $du^5/d\tau = -2H\cot z\,u^0u^5 - 2\bigl(-a_4' + b_4'/(2b_4)\bigr)u^4u^5 = -2H\cot z\,u^0u^5 - 2\alpha_tu^4u^5$, the equation for $u^j$ of Section 3.31.

```python
momenta = {k: g[k] * u[k] for k in (1, 2, 3, 5, 6, 7)}  # p_a = g_aa u^a
rates = [sp.simplify(along_path(p)) for p in momenta.values()]
check(rates == [0] * 6,
      "the six momenta of x1, x2, x3, x5, x6, x7 are conserved in free fall")
```

The six momenta $p_k = g_{kk}u^k$, at the positions 1, 2, 3, 5, 6, 7; their rates along the path simplify to zero (first check). This is the computation of Section 3.31 done by sympy for all six at once.

```python
squared_length = sum(g[k] * u[k] ** 2 for k in range(8))  # g(u, u)
check(sp.simplify(along_path(squared_length)) == 0,
      "the squared length g(u, u) of the velocity is conserved in free fall")
```

The squared length $g(u, u) = \sum_a g_{aa}(u^a)^2$ of the velocity; its rate simplifies to zero (second check). Both checks hold for all functions $a_4(x_4)$ and $b_4(x_4)$ and every real $z$.

**In [5], the momentum weight of the Kohn-Sham record.**

```python
KS_THEORY = "Revision/kohn_sham/ks-theory.json"
ks_theory = json.loads(repository_file(KS_THEORY).read_text(encoding="utf-8"))
say("record, geometry.kappa: " + ks_theory["geometry"]["kappa"])
y_of_x0 = sp.log(sp.sin(6 * H * x0) ** 2) / (12 * H)  # y = ln|sin z|/(6H)
kappa = sp.exp(-a4)  # the record's e^{-a4(x4)}
```

The Kohn-Sham theory record is read and its statement about the momentum weight printed: kappa(x4) = e^{-a4(x4)} (the momentum weight; it does not depend on y). Then the hidden coordinate $y = \ln(\sin^2 z)/(12H) = \ln|\sin z|/(6H)$ as a function of $x_0$ (Section 3.9; written with $\sin^2 z$, so that sympy needs no absolute value) and the weight $\kappa = e^{-a_4}$.

```python
check(sp.simplify(1 / h[1] - kappa) == 0 and not (1 / h[1]).has(x0)
      and "it does not depend on y" in ks_theory["geometry"]["kappa"],
      "1/h1 = e^(-a4) at every y: the frame velocity in 3-space is p1 times kappa",
      record=f"{KS_THEORY}, geometry.kappa")
```

The first check of Section 3.31: $1/h_1 - \kappa$ simplifies to zero, $1/h_1$ contains no $x_0$ at all (`.has(x0)` asks whether an expression contains a symbol), and the record's text says the same in words. So $\hat u^1 = p_1/h_1 = p_1\kappa$ at every height.

```python
W_in_y = (sp.sin(6 * H * x0) ** 2) ** sp.Rational(1, 12)  # W written out
check(sp.simplify(sp.exp(H * y_of_x0) - W_in_y) == 0
      and sp.simplify(1 / h[5] - sp.exp(a4) / sp.sqrt(b4) / W(x0)) == 0,
      "W = e^(H y) and 1/h5 = b4^(-1/2) e^(a4 - H y): the frame velocity along an "
      "extra time grows with a4")
```

The second check: $e^{Hy}$ equals the warp factor written out, $(\sin^2 z)^{1/12}$, and $1/h_5 = b_4^{-1/2}e^{a_4}/W$; together, $1/h_5 = b_4^{-1/2}e^{a_4 - Hy}$, so $\hat u^5 = -p_5b_4^{-1/2}e^{a_4 - Hy}$.

**In [6], the push, the law of $x_4$, and $(u^4)^2$ (exact).**

```python
frame = [h[k] * u[k] for k in range(8)]  # the frame velocities u-hat^a = h_a u^a
space_squared = sum(frame[k] ** 2 for k in (1, 2, 3))  # 3-space part
extra_squared = sum(frame[k] ** 2 for k in (5, 6, 7))  # extra-time part
push = along_path(f_hidden * frame[0]) + H * extra_squared
check(sp.simplify(push) == 0,
      "d(f u0 hat)/dtau = -H (extra-time frame velocities squared): only the extra "
      "times push along y")
```

The frame velocities $\hat u^a = h_au^a$, the sums $S$ (positions 1, 2, 3) and $E$ (positions 5, 6, 7) of Section 3.31, and the sum of the rate of $f\hat u^0$ along the path and $HE$, which simplifies to zero: $d(f\hat u^0)/d\tau = -HE$, the push law.

```python
alpha_t = -sp.diff(a4, x4) + sp.diff(b4, x4) / (2 * b4)  # the rate of x0, x5..x7
law_x4 = (along_path(u[4]) + sp.diff(a4, x4) * space_squared
          + alpha_t * (frame[0] ** 2 - extra_squared))
check(sp.simplify(law_x4) == 0,
      "du4/dtau = -a4' (3-space frame velocities squared) - alpha_t (u0 hat^2 - "
      "extra-time ones squared)")
```

`alpha_t` is the rate $\alpha_t = -a_4' + b_4'/(2b_4)$ of the block, written with the functions. The law $du^4/d\tau = -a_4'S - \alpha_t\bigl((\hat u^0)^2 - E\bigr)$ for the velocity `u[4]` is checked exactly.

```python
in_frame = frame[0] ** 2 + space_squared - u[4] ** 2 - extra_squared
check(sp.simplify(squared_length - in_frame) == 0,
      "g(u, u) written with the frame velocities")
```

$g(u, u) = (\hat u^0)^2 + S - (u^4)^2 - E$, checked exactly. All three checks of this cell hold for all functions $a_4$ and $b_4$.

**In [7], the quadratic form of the plane-wave check.**

```python
SCOPE = "Revision/theory/reports/python-scope.json"
scope = json.loads(repository_file(SCOPE).read_text(encoding="utf-8"))
growth = next(entry for entry in scope["checks"]
              if entry["name"] == "extra_time_growth_rates_unbounded")
form_text = growth["detail"].split("h_k^2 = (")[1].split(") I16")[0]  # the formula
say(f"record ({growth['verdict']}): E^2 = {form_text}")
```

The scope report is read and its check `extra_time_growth_rates_unbounded` taken from its list of checks (`next` returns the first entry of the list whose name matches). Its text contains the piece `h_k^2 = (` followed by the quadratic form and `) I16` (times the $16 \times 16$ unit matrix); the two `split` calls cut out the form between them. The output prints the verdict `PASS` and the form `k0**2 + k1**2 + k2**2 + k3**2 - k5**2 - k6**2 - k7**2 + m**2`, that is $k_0^2 + k_1^2 + k_2^2 + k_3^2 - k_5^2 - k_6^2 - k_7^2 + m^2$.

```python
k = sp.symbols("k0:8", real=True)  # frame momenta k0 ... k7 (k4 is not used)
m = sp.symbols("m", positive=True)  # the mass
form = parse_expr(form_text, local_dict={**{f"k{n}": k[n] for n in range(8)},
                                         "m": m})
U = sp.symbols("U0:8", real=True)  # the frame velocities as plain symbols
particle = m ** 2 * (1 + U[0] ** 2 + U[1] ** 2 + U[2] ** 2 + U[3] ** 2 - U[5] ** 2
                     - U[6] ** 2 - U[7] ** 2)  # m^2 (u^4)^2 from section 8
```

The form is read with the momenta $k_0, \dots, k_7$ and the mass $m$ as symbols (the name `k{n}` of the text means `k[n]`); `{**{...}, "m": m}` builds one dictionary from a dictionary comprehension (unpacked by `**`) and one more entry. `particle` is $m^2(u^4)^2$ from the formula of Section 3.31 (section 8 of the notebook), with the frame velocities as plain symbols $U_0, \dots, U_7$.

```python
same_form = sp.expand(form.subs({k[n]: m * U[n] for n in range(8)}) - particle)
check(growth["verdict"] == "PASS" and same_form == 0,
      "m^2 (u4)^2 of the particle is the plane-wave E^2 of the record",
      record=f"{SCOPE}, check extra_time_growth_rates_unbounded")
```

With $k_a = m\hat u^a$ put into the record's form, the difference from $m^2(u^4)^2$ multiplies out to zero; the check also requires the record's verdict PASS.

**In [8], the numerical tools.**

```python
import math  # sin, tan, exp, ... for single numbers (faster than numpy here)

PARAMETERS = "Revision/kohn_sham/results/parameters.json"
physics = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))
H_value, A_value = physics["physics"]["H"], physics["physics"]["historyA"]
beta = physics["physics"]["historyBeta"]  # b4 = b4(0) e^(beta A H x4)
status = ks_theory["adiabaticity"]["historyStatus"]
say(f"H = {H_value}, A = {A_value}, beta = {beta:.6f}, b4(0) = "
    f"{physics['physics']['historyB4AtZero']}; record: "
    + status.split(". ")[0] + ".")
```

The module `math` computes functions of single numbers, faster than numpy for one number at a time. The parameters of the Revision Kohn-Sham solver give $H = 1$, the slope $A = 1$, the exponent $\beta$ of $b_4$ and $b_4(0) = 1$; the printed line shows $\beta$ with six digits and the first sentence of the record's statement on the status of the history: H = 1.0, A = 1.0, beta = 1.333333, b4(0) = 1.0; record: PRESCRIBED BACKGROUND: the history a4 = H x4, b4 = e^{(4/3) H x4} is prescribed, not solved for.

```python
check(H_value == 1.0 and A_value == 1.0 and abs(beta - 4.0 / 3.0) < 1e-15
      and physics["physics"]["historyB4AtZero"] == 1.0
      and status.startswith("PRESCRIBED BACKGROUND"),
      "the history of the record: a4 = A H x4, b4 = b4(0) e^(beta A H x4) with A = 1, "
      "H = 1, beta = 4/3, b4(0) = 1, prescribed",
      record=f"{PARAMETERS}, physics.H, physics.historyA, physics.historyBeta and "
             f"physics.historyB4AtZero; {KS_THEORY}, adiabaticity.historyStatus")
```

The check confirms the history: $H$, $A$ and $b_4(0)$ equal to $1$, $\beta$ equal to $4/3$ up to the rounding of the last digit (the record stores $1.333333333333333$), and the status PRESCRIBED BACKGROUND.

```python
ARGUMENTS = (a4v, a4p, x0, H, b4v, b4p)
warp_numbers = {W(x0): sp.Abs(sp.sin(6 * H * x0)) ** sp.Rational(1, 6)}  # W = ...
gamma_numbers = [(a, b, c, sp.lambdify(ARGUMENTS, value.subs(warp_numbers), "math"))
                 for (a, b, c), value in sorted(Gamma.items())]
ETA_N = np.array(ETA, dtype=float)  # the signs as numbers
```

`gamma_numbers` is a list of the 31 symbols as fast numerical functions of $(a_4, a_4', x_0, H, b_4, b_4')$, each with its three indices (`sp.lambdify` with `"math"` makes functions of single numbers). Before that, the substitution `warp_numbers` writes the warp factor as $|\sin z|^{1/6}$, which equals $(\sin^2 z)^{1/12}$ and which the module `math` can compute. `ETA_N` holds the signs as floating-point numbers.

```python
def free_fall(state):
    """d state/d tau for state = (x0..x7, u0..u7) on the history a4 = A H x4,
    b4 = e^(beta a4) (b4(0) = 1)."""
    x, v = state[:8], state[8:]
    a4_now, rate = A_value * H_value * x[4], A_value * H_value  # a4 and a4'
    b4_now = math.exp(beta * a4_now)  # b4 on the history
    b4_rate = beta * rate * b4_now  # b4' = beta a4' b4
    change = np.zeros(8)
    for a, b, c, f in gamma_numbers:  # du^a/dtau = - sum Gamma^a_bc u^b u^c
        change[a] -= f(a4_now, rate, x[0], H_value, b4_now, b4_rate) * v[b] * v[c]
    return np.concatenate([v, change])
```

The right side of the 16 equations: the state holds the 8 coordinates (`state[:8]`, entry $k$ is $x^k$) and the 8 velocities (`state[8:]`, entry $8 + k$ of the state is $u^k$). On the history, $a_4 = AHx_4$ with $x_4$ = `x[4]`, $a_4' = AH$, $b_4 = e^{\beta a_4}$ (`b4_now`; `math.exp` is the exponential of one number) and $b_4' = \beta a_4'b_4$ (`b4_rate`). The accelerations are summed over the 31 symbols, and the function returns the derivatives of the state: the velocities, then the accelerations (`np.concatenate` joins two arrays).

```python
def rk4_path(state0, tau_end, steps):
    """RK4 from tau = 0 to tau_end; returns the times and the states (rows)."""
    dt = tau_end / steps
    states = np.zeros((steps + 1, 16))
    states[0] = state0
    for n in range(steps):
        s = states[n]
        k1 = free_fall(s)
        k2 = free_fall(s + dt / 2 * k1)
        k3 = free_fall(s + dt / 2 * k2)
        k4 = free_fall(s + dt * k3)
        states[n + 1] = s + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return np.linspace(0.0, tau_end, steps + 1), states
```

The RK4 method of Chapter 2 (the same as in Notebook 03c, Section 3.22, In [8]) for the 16 unknowns, from $\tau = 0$ to `tau_end` in `steps` equal steps; it returns the times and the table of states, one row per step.

```python
def scale_numbers(x):
    """The eight scale factors h_a at the point x on the history (numbers)."""
    a4_now, z_now = A_value * H_value * x[4], 6 * H_value * x[0]
    f_now = math.exp(-a4_now) * math.sqrt(math.exp(beta * a4_now))  # f
    w = abs(math.sin(z_now)) ** (1 / 6)  # the warp factor W
    return np.array([f_now / math.tan(z_now)] + [math.exp(a4_now)] * 3 + [1.0]
                    + [f_now * w] * 3)
```

The eight scale factors as numbers at a point on the history, in the author's order: $f = e^{-a_4}\sqrt{e^{\beta a_4}}$ (`math.sqrt` is the square root), $W = |\sin z|^{1/6}$, then $h_0 = f/\tan z$ (that is $f\cot z$, positive in the first half cell where all paths stay), three times $e^{a_4}$, the $1$ of $x_4$, and three times $fW$.

```python
def start(y0, frame_velocity):
    """The state at tau = 0: x4 = 0, y = y0, frame velocities as given (the entry
    for x4 is replaced by the value that makes g(u, u) = -1)."""
    x = np.zeros(8)
    x[0] = math.asin(math.exp(6 * H_value * y0)) / (6 * H_value)  # sin z = e^(6Hy)
    w = np.array(frame_velocity, dtype=float)
    w[4] = 0.0
    w[4] = math.sqrt(1.0 + np.sum(ETA_N * w ** 2))  # (u^4)^2 = 1 + sum eta w^2
    return np.concatenate([x, w / scale_numbers(x)])  # u^a = u-hat^a / h_a
```

The starting state: all coordinates zero except $x_0$, which is set from the height $y_0$ by $\sin z = e^{6Hy_0}$, with the angle $z = \arcsin e^{6Hy_0}$ between $0$ and $\pi/2$, in the first half cell. The frame velocities are given in the author's order; the entry for $x_4$ (`w[4]`) is first set to zero, and then to $\sqrt{1 + \sum_a\eta_{aa}(\hat u^a)^2}$, which is the formula $(u^4)^2 = 1 + (\hat u^0)^2 + S - E$ of Section 3.31, so that $g(u, u) = -1$. The velocities are $u^a = \hat u^a/h_a$.

```python
def describe(states):
    """Frame velocities (rows), the coordinate y, g(u, u) and the scale factors."""
    h_rows = np.array([scale_numbers(s[:8]) for s in states])
    frame_rows = h_rows * states[:, 8:]
    y_values = np.log(np.abs(np.sin(6 * H_value * states[:, 0]))) / (6 * H_value)
    lengths = np.sum(ETA_N * frame_rows ** 2, axis=1)  # g(u, u)
    return frame_rows, y_values, lengths, h_rows
```

For every computed state: the scale factors, the frame velocities $\hat u^a = h_au^a$ (a product of two tables entry by entry), the height $y = \ln|\sin z|/(6H)$ from $x_0$ (column 0), and $g(u, u) = \sum_a\eta_{aa}(\hat u^a)^2$ (`axis=1` sums along each row).

```python
Y0 = -1.0  # the starting height of every particle
say(f"start: y0 = {Y0}, z0 = {math.asin(math.exp(6 * Y0)):.6f}")
```

Every particle starts at $y = -1$, that is $z = \arcsin e^{-6}$, printed as start: y0 = -1.0, z0 = 0.002479.

**In [9], the particle at rest.**

```python
tau, rest = rk4_path(start(Y0, [0.0] * 8), 3.0, 3000)
others = [0, 1, 2, 3, 5, 6, 7]  # every coordinate except x4
moved = np.max(np.abs(rest[:, others] - rest[0, others]))
check(moved == 0.0 and np.max(np.abs(rest[:, 4] - tau)) < 1e-12
      and np.max(np.abs(rest[:, 12] - 1.0)) < 1e-12,
      "the particle at rest stays at rest and x4 equals its proper time")
```

A particle with all frame velocities zero (so $u^4 = 1$) is followed from $\tau = 0$ to $3$ in 3000 steps. `rest[:, others]` is the table of the seven other coordinates; their largest change is exactly zero, because every acceleration contains a factor $u^bu^c$ with a zero velocity (no symbol $\Gamma^a{}_{x_4x_4}$ exists, Section 3.23). The check also requires $x_4 = \tau$ (column 4) and $u^4 = 1$ (column 12 of a state is $u^4$: the 8 coordinates come first) within $10^{-12}$.

**In [10], three particles moving in 3-space.**

```python
SPEEDS = (0.25, 0.5, 1.0)  # starting frame velocities along x1
space_paths = {}
for speed in SPEEDS:
    tau, states = rk4_path(start(Y0, [0, speed, 0, 0, 0, 0, 0, 0]), 3.0, 3000)
    frame_rows, y_values, lengths, h_rows = describe(states)
    p1 = h_rows[:, 1] ** 2 * states[:, 9]  # p_1 = g_11 u^1 = h_1^2 u^1
    weight = np.exp(-A_value * H_value * states[:, 4])  # kappa = e^(-a4)
    space_paths[speed] = (states, frame_rows, y_values, lengths, p1)
```

For each starting frame velocity along $x_1$ (entry 1 of the list), the path from $\tau = 0$ to $3$ in 3000 steps, its description, the momentum $p_1 = h_1^2u^1$ along the path (column 9 of a state is $u^1$), and the momentum weight $\kappa = e^{-a_4}$; everything is stored under the speed.

```python
    check(np.max(np.abs(p1 / p1[0] - 1)) < 1e-9
          and np.max(np.abs(lengths + 1)) < 1e-9
          and np.max(np.abs(frame_rows[:, 1] - p1[0] * weight)) < 1e-9
          and np.all(np.diff(states[:, 12]) < 0)
          and np.all(states[:, 0] == states[0, 0]),
          f"3-space speed {speed}: p1 and g(u, u) conserved, frame velocity "
          "p1 kappa, u4 falls, x0 fixed")
```

One check per particle with five conditions: $p_1$ constant within a relative $10^{-9}$; $g(u, u) = -1$ within $10^{-9}$; the frame velocity equal to $p_1\kappa = p_1e^{-a_4}$ within $10^{-9}$; $u^4$ smaller at every step than at the one before (`np.diff` gives the differences of successive values); and $x_0$ exactly equal to its starting value at every step (`==` compares exactly). The last condition is the push law of Section 3.31 in its strictest form: with $u^0 = 0$ and no extra-time motion, every term of $du^0/d\tau$ contains a zero factor, so even the rounded RK4 steps never change $x_0$.

```python
states, frame_rows, y_values, lengths, p1 = space_paths[1.0]
report("fastest particle at tau = 3: x4", f"{states[-1, 4]:.4f}")
report("fastest particle at tau = 3: frame velocity along x1",
       f"{frame_rows[-1, 1]:.6f}")
report("fastest particle at tau = 3: u4", f"{states[-1, 12]:.6f}")
report("fastest particle at tau = 3: height y", f"{y_values[-1]:.4f}")
```

Four RESULT lines for the fastest particle at $\tau = 3$: $x_4 = 3.1878$ (its clock has run 3 while $x_4$ advanced by more), $\hat u^1 = 0.041263$ (down from $1$; it is $e^{-3.1878}$, the pure redshift), $u^4 = 1.000851$ (down from $\sqrt 2 = 1.414$; it is $\sqrt{1 + 0.041263^2}$), and $y = -1.0000$ (unchanged).

**In [11], the particle moving along an extra time.**

```python
L_tip = physics["physics"]["L_tipCutoff"]  # the tip cut-off of the record, 3/H
DT = 0.00025  # the step of RK4: a quarter of 0.001, for the accuracy near the tip
path = [start(Y0, [0, 0, 0, 0, 0, 0.2, 0, 0])]
while math.log(abs(math.sin(6 * H_value * path[-1][0]))) / (6 * H_value) > -L_tip:
    s = path[-1]  # one RK4 step, as in rk4_path
    k1 = free_fall(s)
    k2 = free_fall(s + DT / 2 * k1)
    k3 = free_fall(s + DT / 2 * k2)
    k4 = free_fall(s + DT * k3)
    path.append(s + DT / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
```

The tip cut-off $L = 3$ of the record (Section 3.9; with $H = 1$ the record's $3/H$ is the number 3) and the step `DT` of RK4, a quarter of the step $0.001$ used so far, because near the tip the symbols with the index $x_0$ grow like $\cot z$ and the particle moves ever faster. The path starts as a list with one state, the particle with $\hat u^5 = 0.2$ (entry 5 of the list of frame velocities), so $u^4 = \sqrt{1 - 0.04} = 0.980$. A `while` loop repeats its indented block as long as its condition is true: here, as long as the height $y = \ln|\sin z|/(6H)$ of the last state (`path[-1]` is the last element of the list) lies above $-L$. Each pass makes one RK4 step from the last state, with the same four stages as `rk4_path`, and appends the new state to the list. The loop ends with the first state at or below the cut-off.

```python
extra = np.array(path)  # the states, until the first one beyond the cut-off
tau_t = DT * np.arange(len(extra))  # their proper times
frame_t, y_t, lengths_t, h_t = describe(extra)
p5 = -h_t[:, 5] ** 2 * extra[:, 13]  # p_5 = g_55 u^5 = -h_5^2 u^5
```

The list of states becomes a table; `np.arange(len(extra))` counts $0, 1, 2, \dots$ up to the number of states minus one, and multiplied by `DT` it gives the proper times. Then the description of the path and the momentum $p_5 = -h_5^2u^5$ (column 13 of a state is $u^5$).

```python
q0 = (1 - extra[0, 12]) / (1 + extra[0, 12])  # q(0) of the exact law
q_line = q0 * np.exp(2 * A_value * H_value * tau_t / 3)
exact_u4 = (1 - q_line) / (1 + q_line)  # the exact solution for u4
```

The exact solution of Section 3.31 for $u^4$: $q(0) = (1 - u^4(0))/(1 + u^4(0))$ from the first state, $q = q(0)\,e^{2AH\tau/3}$ at every computed time, and $u^4 = (1 - q)/(1 + q)$.

```python
check(np.max(np.abs(p5 / p5[0] - 1)) < 1e-8 and np.max(np.abs(lengths_t + 1)) < 1e-8
      and np.all(np.diff(extra[:, 12]) < 0) and np.all(np.diff(y_t) < 0),
      "extra-time particle: p5 and g(u, u) conserved, u4 decreases, y falls")
```

The first check: $p_5$ constant within a relative $10^{-8}$, $g(u, u) = -1$ within $10^{-8}$, $u^4$ decreasing and $y$ falling at every step.

```python
check(np.max(np.abs(extra[:, 12] - exact_u4)) < 1e-9,
      "u4 follows the exact law (1 - q0 e^(2 tau/3))/(1 + q0 e^(2 tau/3)) on every step")
```

The second check: the computed $u^4$ (column 12) and the exact formula differ by less than $10^{-9}$ at every one of the computed states.

```python
tau_turn = 3 / (2 * A_value * H_value) * math.log(1 / q0)  # where u4 would be 0
report("tip cut-off y = -3 passed at the proper time tau", f"{tau_t[-1]:.3f}")
report("time x4 there", f"{extra[-1, 4]:.4f}")
report("frame velocity along x5 there", f"{frame_t[-1, 5]:.4f}")
report("frame velocity along y there", f"{frame_t[-1, 0]:.4f}")
report("u4 there", f"{extra[-1, 12]:.6f}")
report("turning point predicted by the exact law at tau", f"{tau_turn:.3f}")
```

The instant $\tau = \frac{3}{2AH}\ln\frac{1}{q(0)}$ at which the formula would give $u^4 = 0$, and six RESULT lines: the cut-off is passed at $\tau = 2.694$, where $x_4 = 2.5457$, $\hat u^5 = 3.4535$ (column 5 of `frame_t`), $\hat u^0 = -3.4217$ (column 0; negative, because $y$ falls) and $u^4 = 0.884124$; the formula puts the turning point at $\tau = 6.877$.

```python
say("record, sectorAndAnsatz.sector: " + ks_theory["sectorAndAnsatz"]["sector"])
check("extra-time momenta zero" in ks_theory["sectorAndAnsatz"]["sector"]
      and tau_t[-1] < tau_turn,
      "the good sector of the Kohn-Sham record has no extra-time momenta; the "
      "extra-time particle reaches the tip cut-off before any turning point",
      record=f"{KS_THEORY}, sectorAndAnsatz.sector")
```

The record's definition of the good sector is printed (good sector: no dependence on x5, x6, x7 (extra-time momenta zero); followed by the record's description of its 3-torus and its momenta), and the last check of the cell requires that it contains "extra-time momenta zero" and that the particle passes the cut-off before the instant of the turning point ($2.694 < 6.877$).

**In [12], Figure 03d.1: redshift and blueshift.**

```python
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
MAGENTA, GREEN, VIOLET, RED = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
COLOURS = {0.25: AQUA, 0.5: ORANGE, 1.0: RED}  # one colour per 3-space particle
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
fig.subplots_adjust(wspace=0.3)  # room for the label of the right vertical axis
```

The palette of the book, one colour per 3-space particle, and a figure with two panels; `subplots_adjust(wspace=0.3)` widens the gap between them.

```python
for speed in SPEEDS:
    states, frame_rows = space_paths[speed][0], space_paths[speed][1]
    axes[0].plot(states[:, 4], frame_rows[:, 1], color=COLOURS[speed], lw=1.8,
                 label=f"RK4, start {speed:g}")
    axes[0].plot(states[:, 4], speed * np.exp(-A_value * H_value * states[:, 4]),
                 ":", color="black", lw=1.2)
axes[0].plot([], [], ":", color="black", label="pure redshift $e^{-a_4}$")
```

For each 3-space particle its frame velocity $\hat u^1$ against $x_4$ (solid) and the pure redshift $\hat u^1(0)e^{-a_4}$ (dotted, black). `axes[0].plot([], [], ...)` draws nothing; it only adds one dotted entry to the legend for all three dotted lines.

```python
axes[0].set_yscale("log")
axes[0].set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$, "
                   "$b_4 = e^{4x_4/3}$")
axes[0].set_ylabel("frame velocity $\\hat u^1$ along $x_1$")
axes[0].set_title("3-space: redshift")
axes[0].legend(fontsize=8)
```

A logarithmic vertical axis, labels, title and legend of the left panel.

```python
axes[1].plot(extra[:, 4], frame_t[:, 5], color=VIOLET, lw=1.8,
             label="RK4: $\\hat u^5$, start 0.2")
axes[1].plot(extra[1:, 4], np.abs(frame_t[1:, 0]), color=AQUA, lw=1.8, ls="--",
             label="RK4: $|\\hat u^0|$, speed of the fall")
```

The right panel: $\hat u^5$ against $x_4$ (solid), and the speed of the fall $|\hat u^0|$ (dashed), from the second state on (`[1:]`), because at the start $\hat u^0 = 0$, which a logarithmic axis cannot show.

```python
blue_rate = (1 - beta / 2) * A_value * H_value  # b4^(-1/2) e^(a4) = e^(a4/3)
axes[1].plot(extra[:, 4], 0.2 * np.exp(blue_rate * extra[:, 4]),
             ":", color="black", lw=1.4, label="pure blueshift $0.2\\,e^{a_4/3}$")
```

`blue_rate` is $(1 - \beta/2)AH = AH/3$, the rate of the pure blueshift $b_4^{-1/2}e^{a_4} = e^{(1 - \beta/2)a_4} = e^{a_4/3}$ (Section 3.31); the dotted line is the pure blueshift $0.2\,e^{a_4/3}$ that the particle would have if it stayed at its height.

```python
axes[1].axvline(extra[-1, 4], color="grey", lw=1.0, ls="-.",
                label="tip cut-off $y = -3$ reached")
axes[1].set_yscale("log")
axes[1].set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$, "
                   "$b_4 = e^{4x_4/3}$")
axes[1].set_ylabel("frame velocity")
axes[1].set_title("Extra time: blueshift and fall")
axes[1].legend(fontsize=8, loc="upper left")
```

A dash-dotted vertical line at the last $x_4$ of the path, where the cut-off is passed; the logarithmic axis, labels, title and legend.

```python
save_figure(fig, "frame_velocities",
            "Frame velocities of freely falling test particles in the corrected "
...
            f"$x_4 = {extra[-1, 4]:.3f}$ (dash-dotted).")
check(np.all(frame_t[1:, 5] > 0.2 * np.exp(blue_rate * extra[1:, 4])),
      "the extra-time frame velocity grows faster than the pure blueshift")
```

The figure is saved; its caption contains the $x_4$ of the cut-off, $2.546$, through an f-string. The check: after the first state, $\hat u^5$ exceeds the pure blueshift at every step.

**What Figure 03d.1 shows.** Along the history with $b_4 = e^{4x_4/3}$. Left: on the logarithmic axis the three frame velocities fall like straight lines of slope $-1$ and lie exactly on the dotted lines of the pure redshift $e^{-a_4}$, because 3-space has no warp and the particles stay at their height (In [10] checks the agreement within $10^{-9}$). Right: the frame velocity along $x_5$ grows from $0.2$, at first like the pure blueshift $0.2\,e^{a_4/3}$, then much faster, because the particle sinks towards the tip where $e^{-Hy}$ is larger; when it passes the cut-off at $x_4 = 2.546$ it has $\hat u^5 = 3.45$, while the pure blueshift has only reached $0.2\,e^{2.5457/3} = 0.47$: the remaining factor, about $e^2 = 7.4$, is the factor $e^{-H(y - y_0)}$ of the sinking from $y = -1$ to $y = -3$. The speed of the fall $|\hat u^0|$ (dashed) grows from zero and approaches $\hat u^5$ near the cut-off, where $(\hat u^5)^2 - (\hat u^0)^2 = 1 - (u^4)^2$ is small compared with either square.

**In [13], Figure 03d.2: the $x_4$ velocity and the time $x_4$.**

```python
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
fig.subplots_adjust(wspace=0.3)
axes[0].plot(tau, rest[:, 12], color="black", lw=1.4, ls="--", label="at rest")
axes[1].plot(tau, rest[:, 4], color="black", lw=1.4, ls="--", label="at rest")
```

Two panels against the proper time $\tau$: $u^4$ on the left, $x_4$ on the right; first the particle at rest (dashed black).

```python
for speed in SPEEDS:
    states = space_paths[speed][0]
    axes[0].plot(tau, states[:, 12], color=COLOURS[speed], lw=1.8,
                 label=f"3-space, start {speed:g}")
    axes[1].plot(tau, states[:, 4], color=COLOURS[speed], lw=1.8,
                 label=f"3-space, start {speed:g}")
```

The three 3-space particles, the same in both panels.

```python
axes[0].plot(tau_t, extra[:, 12], color=VIOLET, lw=1.8, ls="-.",
             label="extra time, start 0.2")
axes[0].plot(tau_t[::800], exact_u4[::800], "o", color=VIOLET, ms=5,
             label="exact law of section 11")
axes[1].plot(tau_t, extra[:, 4], color=VIOLET, lw=1.8, ls="-.",
             label="extra time, start 0.2")
```

The extra-time particle (dash-dotted) in both panels, and in the left panel every 800th value of the exact formula for $u^4$ as a dot (`[::800]` takes every 800th element: one dot every $800 \times 0.00025 = 0.2$ in $\tau$).

```python
axes[0].set_ylabel("$x_4$ velocity $u^4 = dx_4/d\\tau$")
axes[1].set_ylabel("time $x_4$ (unit $1/H$)")
axes[0].set_title("The $x_4$ velocity")
axes[1].set_title("The time $x_4$ along each path")
for ax, place in zip(axes, ("upper right", "upper left")):  # legends off the lines
    ax.set_xlabel("proper time $\\tau$ of the particle (unit $1/H$)")
    ax.legend(fontsize=8, loc=place)
```

Labels and titles; the loop gives both panels their horizontal label and a legend placed where no curve runs (`zip` pairs each panel with its place).

```python
save_figure(fig, "x4_velocity",
            "The $x_4$ velocity $u^4 = dx_4/d\\tau$ (left) and the time $x_4$ "
...
            f"says (dots) until it passes the tip cut-off at $\\tau = {tau_t[-1]:.2f}$; "
            f"the formula puts its turning point at $\\tau = {tau_turn:.2f}$.")
check(np.all(np.diff(space_paths[1.0][0][:, 4]) > 0)
      and np.all(np.diff(extra[:, 4]) > 0),
      "every particle keeps advancing in x4 along the computed paths")
```

The figure is saved; the f-strings of its caption put in the proper time of the cut-off, $2.69$, and of the predicted turning point, $6.88$. The check: the fastest 3-space particle and the extra-time particle advance in $x_4$ at every step.

**What Figure 03d.2 shows.** Left: the particle at rest keeps $u^4 = 1$; the 3-space particles start at $\sqrt{1 + (\hat u^1)^2}$ ($1.031$, $1.118$ and $1.414$) and settle down towards $1$ as their motion is redshifted away; the extra-time particle starts at $0.980$ and its $u^4$ falls, slowly at first and then faster, to $0.884$ at the cut-off, with every dot of the exact formula on the computed curve. Right: $x_4$ grows along every path; the fastest 3-space particle runs ahead of the particle at rest ($x_4 = 3.1878$ at $\tau = 3$), the extra-time particle falls behind ($x_4 = 2.5457$ at $\tau = 2.694$), because its $u^4$ is below $1$.

**In [14], Figure 03d.3: the push along the hidden direction.**

```python
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
fig.subplots_adjust(wspace=0.3)
axes[0].plot(tau, np.full_like(tau, Y0), color="black", lw=1.4, ls="--",
             label="at rest and 3-space (all at $y = -1$)")
```

Two panels; in the left one the height of the particle at rest and of the three 3-space particles, which all stay at $y = -1$, drawn once as a dashed line (`np.full_like(tau, Y0)` is an array of the shape of `tau` filled with $-1$).

```python
axes[0].plot(tau_t, y_t, color=VIOLET, lw=1.8, ls="-.", label="extra time, start 0.2")
axes[0].axhline(0.0, color="grey", lw=1.0, label="fold $y = 0$")
axes[0].axhline(-L_tip, color="grey", lw=1.0, ls=":", label="tip cut-off $y = -3$")
axes[0].set_xlabel("proper time $\\tau$ (unit $1/H$)")
axes[0].set_ylabel("height $y$ in the hidden direction (unit $1/H$)")
axes[0].set_title("Only the extra-time motion pushes along $y$")
axes[0].set_ylim(-3.6, 0.4)
axes[0].legend(fontsize=7, loc="lower left")
```

The height of the extra-time particle (dash-dotted), horizontal lines at the fold $y = 0$ and at the tip cut-off $y = -3$, labels, title, the vertical range from $-3.6$ to $0.4$ (`set_ylim`), and the legend.

```python
f_numbers = np.exp(-(1 - beta / 2) * A_value * H_value * extra[:, 4])  # f on path
law = -H_value * np.sum(frame_t[:, 5:8] ** 2, axis=1)  # -H sum of squares
numeric = np.gradient(f_numbers * frame_t[:, 0], tau_t)  # d(f u0 hat)/dtau
largest_gap = float(np.max(np.abs(numeric - law)[1:-1]) / np.max(np.abs(law)))
space_push = max(float(np.max(np.abs(space_paths[s][2] - Y0))) for s in SPEEDS)
```

The hidden scale on the history, $f = e^{-a_4}b_4^{1/2} = e^{-(1 - \beta/2)a_4} = e^{-a_4/3}$, at every state of the extra-time path; the push law $-HE$ (`frame_t[:, 5:8]` are the three extra-time columns 5, 6, 7); and the rate $d(f\hat u^0)/d\tau$ obtained from the computed states by `np.gradient`, which takes central differences inside the path and one-sided differences at its two ends. `largest_gap` is the largest difference inside the path (`[1:-1]` leaves out the two ends, where the one-sided differences are less accurate), divided by the largest size of the law: near the cut-off the particle speeds up sharply, and the error of the central differences, of order $\Delta\tau^2$ times the third derivative, grows with it, so the comparison is made relative to the size of the push. `space_push` is the largest distance from $y = -1$ reached by any of the three 3-space particles (entry 2 of each stored tuple is the list of the heights $y$); it is exactly zero, because their $x_0$ never changes and the height computed from the starting $x_0$ is exactly $-1.0$ in floating point.

```python
axes[1].plot(tau_t, law, color=VIOLET, lw=1.8, label="law $-H\\sum_j(\\hat u^j)^2$")
axes[1].plot(tau_t[::400], numeric[::400], "o", color=VIOLET, ms=5,
             label="from RK4, numerical derivative")
axes[1].axhline(0.0, color="grey", lw=0.8)
axes[1].set_xlabel("proper time $\\tau$ (unit $1/H$)")
axes[1].set_ylabel("$d(f\\hat u^0)/d\\tau$ (unit $H$)")
axes[1].set_title("The push: $-H$ times the extra-time squares")
axes[1].legend(fontsize=7, loc="lower left")
```

The law as a line and every 400th numerical value as a dot (one dot every $0.1$ in $\tau$); the zero line, labels, title and legend.

```python
report("largest difference between the numerical rate and the law, relative to the "
       "largest value of the law", f"{largest_gap:.1e}")
```

The RESULT line prints $4.3 \times 10^{-6}$.

```python
save_figure(fig, "hidden_push",
            "The push along the hidden direction on freely falling test particles in "
...
check(largest_gap < 1e-4 and space_push == 0.0,
      "the computed rate agrees with the exact push law; 3-space motion does not "
      "change y")
```

The figure is saved; the check requires agreement within a relative $10^{-4}$ and no change of height for the 3-space particles.

**What Figure 03d.3 shows.** Left: the particle at rest and the 3-space particles stay at $y = -1$: motion in 3-space does not push. The extra-time particle sinks towards the tip, slowly at first and then ever faster, and passes the cut-off $y = -3$ at $\tau = 2.694$. Right: the dots computed from the path lie on the line of the exact law; the push starts at $-H(0.2)^2 = -0.04$ and grows in size with the blueshifted $(\hat u^5)^2$, to about $-3.4535^2 = -11.9$ at the cut-off.

**In [15], Figure 03d.4: the quadratic form as a map.**

```python
top5 = float(np.ceil(frame_t[:, 5].max())) + 0.5  # the plotted range of u5 hat
low0 = float(np.floor(frame_t[:, 0].min())) - 0.5  # the plotted range of u0 hat
grid5, grid0 = np.meshgrid(np.linspace(0.0, top5, 451), np.linspace(low0, 0.5, 501))
squared_u4 = 1 + grid0 ** 2 - grid5 ** 2  # (u^4)^2 over the plane
fig, ax = plt.subplots(figsize=(6.4, 5.2))
ax.contourf(grid5, grid0, squared_u4, levels=[-1000.0, 0.0], colors=["#d9d9d9"])
ax.contour(grid5, grid0, squared_u4, levels=[0.0], colors="black", linewidths=1.2)
```

The plotted ranges follow the path: $\hat u^5$ from $0$ to the next whole number above its largest value plus $0.5$ (`np.ceil` rounds up: $4 + 0.5 = 4.5$), $\hat u^0$ from the next whole number below its smallest value minus $0.5$ (`np.floor` rounds down: $-4 - 0.5 = -4.5$) to $0.5$. On a grid of $451 \times 501$ points the value $(u^4)^2 = 1 + (\hat u^0)^2 - (\hat u^5)^2$, the formula of Section 3.31 for a particle that moves only along $x_5$ and $y$. `contourf` with the levels $-1000$ and $0$ fills in grey the region where the value is negative (the smallest value on the grid, $1 - 4.5^2 = -19.25$, lies far above $-1000$); `contour` at the level $0$ draws the black boundary curve $(\hat u^5)^2 = 1 + (\hat u^0)^2$.

```python
ax.plot(frame_t[:, 5], frame_t[:, 0], color=VIOLET, lw=2.0,
        label="path of the extra-time particle")
ax.plot([frame_t[0, 5]], [frame_t[0, 0]], "s", color=VIOLET, ms=7, label="start")
ax.plot([frame_t[-1, 5]], [frame_t[-1, 0]], "o", color=VIOLET, ms=8,
        label="tip cut-off $y = -3$ passed")
ax.text(0.62 * top5, 0.35 * low0, "$(u^4)^2 < 0$:\nno particle;\nplane waves grow",
        fontsize=8)
ax.text(0.08 * top5, 0.75 * low0, "$(u^4)^2 > 0$", fontsize=9)
```

The path of the extra-time particle in this plane (columns 5 and 0 of `frame_t`), a square at its start, a dot where it passes the cut-off, and two labels written into the regions at fixed fractions of the plotted ranges (`\n` starts a new line of a label).

```python
ax.set_xlabel("frame velocity $\\hat u^5$ along the extra time $x_5$")
ax.set_ylabel("frame velocity $\\hat u^0 = f\\,dy/d\\tau$")
ax.set_title("The quadratic form $(u^4)^2 = 1 + (\\hat u^0)^2 - (\\hat u^5)^2$")
ax.grid(False)
ax.legend(fontsize=8, loc="lower left")
```

Labels, title, no grid lines, legend.

```python
save_figure(fig, "quadratic_form",
            "The squared $x_4$ velocity $(u^4)^2 = 1 + (\\hat u^0)^2 - (\\hat u^5)^2$ "
...
check(np.all(1 + frame_t[:, 0] ** 2 - frame_t[:, 5] ** 2 > 0.03),
      "the path stays in the region where (u4)^2 > 0, away from the curve")
```

The figure is saved; the check: along the whole path $(u^4)^2 > 0.03$, so the path keeps away from the curve.

**What Figure 03d.4 shows.** The violet path starts at $(0.2, 0)$, moves to the right (blueshift) and downwards (it falls towards the tip, $dy/d\tau < 0$), almost along a straight line parallel to the black curve, and ends at $(3.45, -3.42)$, where it passes the cut-off. It never comes close to the grey region: $(\hat u^5)^2 - (\hat u^0)^2 = 1 - (u^4)^2$ grows only from $0.04$ to $1 - 0.884124^2 = 0.22$, while the curve lies where it equals $1$. In the grey region the plane waves of the record's check would grow instead of oscillating; a particle cannot be there, and this one, within the computed path, does not even approach it.

**In [16], Figure 03d.5: how accurate the computation is.**

```python
from matplotlib.ticker import NullFormatter  # an empty label for minor ticks

p1_fast = space_paths[1.0][4]  # p_1 along the fastest 3-space path
drift = {"$p_1$, 3-space particle": (tau, np.abs(p1_fast / p1_fast[0] - 1)),
         "$g(u,u) + 1$, 3-space particle": (tau, np.abs(space_paths[1.0][3] + 1)),
         "$p_5$, extra-time particle": (tau_t, np.abs(p5 / p5[0] - 1)),
         "$g(u,u) + 1$, extra-time particle": (tau_t, np.abs(lengths_t + 1))}
```

`NullFormatter` is used below to suppress the labels of the small ticks. `drift` is a dictionary of four curves, each a label with its times and the drift of a conserved quantity from its starting value: $p_1$ and $g(u, u) + 1$ for the fastest 3-space particle, $p_5$ and $g(u, u) + 1$ for the extra-time particle.

```python
STEPS = (50, 100, 200, 400, 800, 1600)
differences = {}
for label, state0 in (("3-space, start 1", start(Y0, [0, 1, 0, 0, 0, 0, 0, 0])),
                      ("extra time, start 0.2", start(Y0, [0, 0, 0, 0, 0, 0.2, 0, 0]))):
    ends = [rk4_path(state0, 2.0, n)[1][-1] for n in STEPS]
    differences[label] = np.array([np.max(np.abs(ends[i] - ends[i + 1]))
                                   for i in range(len(STEPS) - 1)])
    ratios = differences[label][:-1] / differences[label][1:]
    say(f"  {label}: ratios of successive differences "
        + ", ".join(f"{r:.1f}" for r in ratios))
```

The order of RK4: each of the two particles is integrated from $\tau = 0$ to $2$ with 50, 100, 200, 400, 800 and 1600 steps; `ends` holds the six end states (`[1][-1]` is the last row of the table of states). `differences` holds the five largest differences between the end states of successive step counts, and `ratios` the four ratios of successive differences, printed: 16.4, 16.2, 16.1, 16.1 for the 3-space particle and 16.4, 16.3, 16.2, 16.1 for the extra-time particle. For a method of order 4 halving the step divides the error by about $2^4 = 16$ (Chapter 2).

```python
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
fig.subplots_adjust(wspace=0.3)
for (label, (t_values, values)), colour, style in zip(
        drift.items(), (RED, ORANGE, VIOLET, AQUA), ("-", "--", "-.", ":")):
    axes[0].semilogy(t_values[1:], np.maximum(values[1:], 1e-17), color=colour,
                     ls=style, lw=1.6, label=label)
axes[0].set_xlabel("proper time $\\tau$ (unit $1/H$)")
axes[0].set_ylabel("relative drift from the start")
axes[0].set_title("Conserved quantities (RK4 steps $0.001$ and $0.00025$)")
axes[0].legend(fontsize=7, loc="lower right")
```

The left panel draws the four drifts on a logarithmic axis (`semilogy`); the first point ($\tau = 0$, where the drift is exactly zero) is left out, and `np.maximum(values, 1e-17)` replaces any other exact zero by $10^{-17}$, because a logarithmic axis cannot show zero.

```python
dts = 2.0 / np.array(STEPS[:-1])  # the larger step of each pair
for (label, values), colour in zip(differences.items(), (RED, VIOLET)):
    axes[1].loglog(dts, values, "o-", color=colour, lw=1.6, label=label)
axes[1].loglog(dts, differences["extra time, start 0.2"][0] * (dts / dts[0]) ** 4,
               "--", color="black", lw=1.0, label="slope 4")
axes[1].set_xticks(dts, [f"{dt:g}" for dt in dts])  # the five steps as labels
axes[1].xaxis.set_minor_formatter(NullFormatter())  # no labels between them
```

The right panel: the differences against the larger step $\Delta\tau$ of each pair ($0.04$, $0.02$, $0.01$, $0.005$ and $0.0025$), on logarithmic axes, with a dashed reference line of slope 4 through the first point of the extra-time particle; the five steps are written at the ticks, and the small ticks between them get no labels.

```python
axes[1].set_xlabel("step $\\Delta\\tau$ of RK4")
axes[1].set_ylabel("difference of end states (step and half step)")
axes[1].set_title("RK4 is of order 4")
axes[1].legend(fontsize=8)
drift_largest = max(float(np.max(values)) for _, values in drift.values())
```

Labels, title, legend; `drift_largest` is the largest drift of the four curves.

```python
save_figure(fig, "accuracy",
            "The accuracy of the RK4 computation of free fall in the corrected "
...
all_ratios = np.concatenate([d[1:-1] / d[2:] for d in differences.values()])
check(np.all((all_ratios > 14) & (all_ratios < 18)) and drift_largest < 1e-8,
      "halving the RK4 step divides the error by 14 to 18: order 4; drifts below 1e-8")
```

The figure is saved. For the check, the coarsest pair (where the error is not yet in its final form) is left out: `d[1:-1] / d[2:]` gives the last three ratios of each particle, $16.2, 16.1, 16.1$ and $16.3, 16.2, 16.1$, and all six must lie between 14 and 18 (`&` combines the two conditions element by element); the largest drift must stay below $10^{-8}$.

**What Figure 03d.5 shows.** Left: the drifts of the conserved quantities of the 3-space particle stay far below those of the extra-time particle near the end; the drifts of the extra-time particle stay at the level of the rounding errors for most of the path and grow in its last part, where it approaches the cut-off and moves fastest, but all four stay below $10^{-8}$ (the check of the cell). Right: both sets of points lie on lines of slope 4: halving the step makes the error 16 times smaller. The computed paths are accurate far beyond the precision of any number quoted from them.

**In [17], the last check.**

```python
figure_names = ["frame_velocities", "x4_velocity", "hidden_push", "quadratic_form",
                "accuracy"]
files = [output_file(f"{FIGURE_FOLDER}/03d_{n}_{name}.png")
         for n, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in files), "all five figure files exist")
all_checks_passed()
```

The five figure files must exist; the last line prints ALL 23 CHECKS PASSED (notebook 03d). The 23 checks are: 1 in In [3], 2 each in In [4] and In [5], 3 in In [6], 1 each in In [7], In [8] and In [9], 3 each in In [10] and In [11], and 1 each in In [12] to In [17].

### 3.36 What we proved, what we computed, what we assumed

**PROVED in this chapter** (each derivation written out line by line; every one is also confirmed by an exact check of a notebook, and where a Revision record states the same, the record and its check are named in the section):

- the line elements of the plane in polar coordinates and of the sphere; the inverse of a diagonal metric (Section 3.3);
- for the corrected metric of 2026-10-16 (version 2), written in the author's coordinates $x_0, \dots, x_7$ with the two metric functions $a_4(x_4)$ and $b_4(x_4) > 0$ and every real $z = 6Hx_0$: every entry repeats with the period $\pi$ in $z$ and is unchanged under $z \to \pi - z$, so one cell $0 < z < \pi$, made of two halves joined at the fold and ended by the tips, holds the whole geometry; the signature (4,4) at every point with $\sin z\cos z \ne 0$, for every $a_4$ and every $b_4 > 0$ (record `python-warped-metric-report.json`, check `corrected_metric_entries`); $\det g = e^{-2a_4}b_4^4\cot^2 z\,|\sin z|$ and $\sqrt{|\det g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$ (record `python-lovelock-report.json`, check `sqrt_abs_det_g`; `curvature.json`, key `sqrtAbsDetG`; `warped-metric.json`, key `sqrt_det_g_corrected`); the proper 7-volume of a region with fixed coordinate ranges changes at the rate $-a_4' + 2b_4'/b_4$ (like $e^{5a_4/3}$ on the history of Section 3.8); the 7-volume $e^{-a_4}b_4^2/(3H)$ of a half cell per unit transverse coordinate volume; $V_3V_t = b_4^{3/2}(\sin^2 z)^{1/4}$ (Sections 3.5 and 3.6);
- the scale factors, the hidden scale $f = e^{-a_4}b_4^{1/2}$ shared by the hidden direction and the extra times, the warp factor $W = (\sin^2 z)^{1/12}$ of the extra times alone, and the diagonal vielbein (lead check `vielbein_reproduces_metric`; `warped-metric.json`, key `vielbein_corrected`); the expansion rates $a_4'$ of 3-space and $\alpha_t = -a_4' + b_4'/(2b_4)$ of the hidden direction and the extra times ($-a_4'/3$ on the history of Section 3.8) (Section 3.7);
- the hidden coordinate $y = \ln|\sin z|/(6H)$: $dy = \cot z\,dx_0$ (lead check `ks_coordinate_jacobian`), $W = e^{Hy}$, the block form of the line element, in which $dy^2$ and the three extra times share the factor $f^2$, and the volume factor $e^{-a_4}b_4^2e^{3Hy}$, those of the record `ks-theory.json`; each half of a cell is $-\infty < y \le 0$, with the tip at an infinite proper distance; the fraction $e^{-3HL}$ of a half cell beyond the tip cut-off (Section 3.9);
- the transformation rules of vectors, covectors and the metric; the invariance of contractions (Section 3.14); the covariant derivative of covectors and of tensors with two indices (one $+\Gamma$ term for every upper index, one $-\Gamma$ term for every lower index), in particular of the metric; the Christoffel formula as the only connection without torsion that is compatible with the metric; the four cases for a diagonal metric; the contracted symbol $\sum_a\Gamma^a{}_{ab} = \partial_b\ln\sqrt{|\det g|}$ (Section 3.15);
- along a geodesic the squared speed is constant, and a coordinate absent from a diagonal metric has a conserved momentum; the geodesic equations of the sphere; the equator is a geodesic and other circles of latitude are not; parallel transport around a circle of latitude turns a vector by $2\pi(1 - \cos\theta_0)$, the enclosed area divided by $a^2$ (Section 3.16);
- the commutator of covariant derivatives is the Riemann tensor (MTW convention); its antisymmetry in the last two indices and the first Bianchi identity; each diagonal entry of the Ricci tensor is the sum of the curvatures of the coordinate planes through that direction (Section 3.17);
- the plane is flat; the sphere has the Gaussian curvature $1/a^2$, $R = 2/a^2$, $K = 4/a^4$; two meridians approach as $a\cos(s/a)\Delta\varphi$ (Section 3.18);
- the 31 non-zero Christoffel symbols of the corrected metric (21 with $b \le c$, record `curvature.json`, key `christoffelNonzero_b_le_c`); observers at rest fall freely with proper time $x_4$, for all $a_4$ and $b_4$ (Section 3.23);
- the curvatures of the 28 coordinate planes, $a_4'^2$, $a_4'^2 + a_4''$, $a_4'\alpha_t$, $\alpha_t^2 + \alpha_t'$ and, in the six planes of the block, the constant curvature $\alpha_t^2 - H^2k$ with $k = e^{2a_4}/b_4 = 1/f^2$; what their signs mean (a shape only for two space-like directions, reversed for two time-like ones); for two observers at rest $d^2\xi/d\tau^2 = \sigma\,\xi$; the 112 non-zero components $R^{ab}{}_{cd}$, all of them plane curvatures, with 10 different values (record `lovelock-report.json`, check `riemann_antisymmetry`; check `mixed_riemann_only_sectional`), none depending on $z$ (Section 3.24);
- $R^a{}_a$, $R = 8a_4'^2 - 2a_4'' - 8a_4'u + 5u^2 + 4v - 12H^2k$ with $u = b_4'/b_4$ and $v = u'$, and the Einstein tensor (record `curvature.json`, keys `ricciMixed`, `ricciScalar`, `einsteinMixed`): both are diagonal for all $a_4$ and $b_4$ and every real $z$, no entry depends on $z$, $G^0{}_0 = G^j{}_j$, and $G^4{}_4 = 3a_4'^2 - \frac32 u^2 + 6H^2k$ contains no second derivative (lead checks `einstein_off_diagonal_vanish`, `einstein_diagonal_x0_independent`, `einstein_isotropy`); on the history of Section 3.8, $G^4{}_4 = (6k + \frac13 A^2)H^2$, $G^i{}_i = (6k - \frac{13}{9}A^2)H^2$, $G^0{}_0 = G^j{}_j = (3k - \frac{11}{3}A^2)H^2$ and $R = (\frac{56}{9}A^2 - 12k)H^2$; $K = 4\sum\sigma^2 \ge 0$, zero exactly on the flat member $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$; on the history $K = (\frac{2416}{81}A^4 - \frac{16}{3}A^2k + 24k^2)H^4 > 0$, $48.49H^4$ at $A = 1$ on the first slice; the contracted Bianchi identity for all $a_4(x_4)$ and $b_4(x_4)$ (record `lovelock-report.json`, checks `k1_equals_minus_4_einstein`, `k1_divergence_free`; `python-a4-report.json`, check `bianchi_x4`) (Section 3.25);
- within Einstein's equations: a diagonal source suffices, and it needs $p_0 = p_t$ and no dependence on $x_0$; no exponential history is empty (lead check `einstein_no_exponential_vacuum`); $\kappa(\rho + p_0) = -\frac32(2H^2k + 4a_4'^2 - a_4'u + v)$; along the history $\kappa\rho = -(6k + \frac13 A^2)H^2 - \Lambda$, $\kappa p_3 = (6k - \frac{13}{9}A^2)H^2 + \Lambda$ and $\kappa p_0 = \kappa p_t = (3k - \frac{11}{3}A^2)H^2 + \Lambda$ (record `a4-equations.json`, key `exponentialHistory.requiredSource`; `warped-metric.json`, key `history_source.einstein_A1_beta43`), with $\kappa(\rho + p_0) = -(3k + 4A^2)H^2 < 0$ and $\kappa(\rho + p_3) = -\frac{16}{9}A^2H^2 < 0$ (Section 3.26);
- in free fall: the six momenta and $g(u, u)$ are conserved; $\hat u^i = p_ie^{-a_4}$ at every height (the momentum weight $\kappa(x_4)$ of `ks-theory.json`) and $\hat u^j = -p_jb_4^{-1/2}e^{a_4 - Hy}$, so along a deflating history 3-space motion is redshifted and extra-time motion blueshifted (on the history of Section 3.8 like $e^{a_4/3}$); $d(f^2\,dy/d\tau)/d\tau = -H\sum_j(\hat u^j)^2$: only extra-time motion pushes along the hidden direction, towards the tip; $du^4/d\tau = -a_4'S - \alpha_t((\hat u^0)^2 - E)$; $(u^4)^2 = 1 + (\hat u^0)^2 + S - E$, which times $m^2$ is the quadratic form of the record's check `extra_time_growth_rates_unbounded`; without 3-space motion, on the history, $u^4 = (1 - q)/(1 + q)$ with $q = q(0)e^{2AH\tau/3}$; without extra-time motion a particle never turns in $x_4$ and is never pushed; after a turning point on a deflating history $x_4$ decreases (Section 3.31).

**PROVED by hand in the exercises** (not checked by a notebook; where a notebook prints the same number, the exercise compares it): along the histories of Section 3.8, $K \ge \frac{3588}{151}k^2H^4$ for every slope (Exercise 7); the exact path of a particle that moves in 3-space (Exercise 8); for every free particle $f^2((\hat u^0)^2 - E)$ is conserved, so that $u^4$ is a function of $x_4$ alone (Exercise 9); the exact path of the extra-time particle of Notebook 03d, which reaches the tip at the proper time $2.814$, before any turning point (Exercise 10).

**COMPUTED by the notebooks** (each number in the cell named; where a Revision record is reproduced, its file and key or check):

- Notebook 03a: $g_{11} = 2.718282$ and $g_{55} = -0.618841$ at $z = 0.7$, $a_4 = 0.5$, $b_4 = e^{2/3}$ (In [8]); the signs on a grid of 800 values of $z$ across two cells, 13 values of $a_4$ and 3 of $b_4$ (In [8]); the slices, $H = 1$, $A = 1$, $\beta = 4/3$ and $b_4(0) = 1$ (In [13]; `Revision/kohn_sham/results/parameters.json`); the growth and shrink factors $e^2 = 7.389056$ and $e^{-2/3} = 0.513417$ (In [14]); the fraction $e^{-9} = 1.2341 \times 10^{-4}$ of a half cell beyond the tip cut-off and the cut-off angle $1.5230 \times 10^{-8}$ radians (In [20]).
- Notebook 03c: the turning angles of 15 circles within $5.0 \times 10^{-12}$ radians of the area formula (In [10]); three geodesics within $1.2 \times 10^{-13}$, $6.2 \times 10^{-13}$ and $7.1 \times 10^{-11}$ of their planes (In [11]); the deviation equation within $8.0 \times 10^{-14}$ of two meridians (In [13]).
- Notebook 03b: the 512 Christoffel symbols by central differences, order $2.040$, best error $1.5 \times 10^{-10}$ at $h = 10^{-6}$, at the test point of the record's check `k1_brute_force_numeric` (with $b_4 = 1.37$, $b_4' = 0.31$; In [10], In [11]); 262 recorded components equal to ours at the five test points of `python-lovelock-report.json`, 1310 evaluations with 30 digits, to the relative $4.93 \times 10^{-31}$ (In [19]); $K$ summed from the 112 components equal to the formula at 300 values of $z$: $46.75$, $69.13$, $181$ and $494.2$ in units of $H^4$ for $a_4' = 0.5$, $1$, $1.5$, $2$ at the slice $a_4 = 0.5$ (In [23]); at $A = 1$ on the slices $a_4 = 0, 1, 2$ the Ricci scalar $R = -5.778$, $-17.15$, $-39.3$ in units of $H^2$, and $K = 48.49H^4$ on the first slice (In [24]).
- Notebook 03d: along the prescribed history ($a_4 = x_4$, $b_4 = e^{4x_4/3}$) with RK4, from $y = -1$: the particle at rest stays at rest (In [9]); the fastest 3-space particle at $\tau = 3$ has $x_4 = 3.1878$, $\hat u^1 = 0.041263$, $u^4 = 1.000851$ and $y = -1.0000$ (In [10]); the extra-time particle passes the tip cut-off at $\tau = 2.694$ with $x_4 = 2.5457$, $\hat u^5 = 3.4535$, $\hat u^0 = -3.4217$ and $u^4 = 0.884124$, its $u^4$ within $10^{-9}$ of the exact formula, whose turning point lies at $\tau = 6.877$ (In [11]); the push law within a relative $4.3 \times 10^{-6}$ (In [14]); RK4 ratios 16.1 to 16.4 (In [16]).

**ASSUMED** (used, not derived here):

- standard theorems quoted without proof: Sylvester's law of inertia (Section 3.4); the volume factor of a metric that is not diagonal (not needed); that the Christoffel symbols of two systems of coordinates describe the same covariant derivative (Section 3.15); that a space with zero Riemann tensor has constant metrics locally (Section 3.17); the symmetries (S3) and (S4) and the contracted Bianchi identity for a general metric (Sections 3.17 and 3.25; for the corrected metric all three are checked or proved); which components of the Riemann tensor a diagonal metric that depends on $x_4$ and $x_0$ can have (Section 3.24; for the corrected metric the record checks the result); the uniqueness of solutions of ordinary differential equations (Sections 3.16 and 3.31); the geodesic deviation equation of a general surface, and its form $d^2\xi/d\tau^2 = +\sigma\,\xi$ for free-fall paths along a time-like direction (Section 3.18; for the observers at rest in the corrected metric it is proved in Section 3.24);
- from physics: that a body in free fall moves on a time-like geodesic, and that the bodies of Section 3.31 are test particles; the form of Einstein's field equations and the null energy condition as the mark of ordinary matter (Section 3.26; derived and discussed in Chapters 9 and 12);
- the history $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{\beta AHx_4}$ with $A = 1$, $H = 1$, $\beta = 4/3$ and $b_4(0) = 1$, used for every picture and every number along the history: a PRESCRIBED BACKGROUND, not a solution of the field equations with a source of this book (key `adiabaticity.historyStatus` of `Revision/kohn_sham/ks-theory.json`, and `Revision/field_equations_a4/reports/ks-source-conditions.json`); the exponent $\beta = 4/3$ is the choice of the Revision record (`Revision/SPEC.md`, section 1; Section 3.8). Every formula written with general $a_4(x_4)$ and $b_4(x_4)$ is exact without it;
- the boundary conditions that the Kohn-Sham work imposes at the fold (Section 3.9; Chapter 14).

**HYPOTHESIS.** None enters this chapter.

**OPEN.** Whether wave packets of the fields of the book follow the free-fall paths of Section 3.31 in the curved metric is not computed (Section 3.31). What a field or a body does at the degenerate points of the metric, the fold $\cos z = 0$ and the tips $\sin z = 0$, is not computed either; the Revision record computes nothing there (Sections 3.5, 3.9 and 3.31).

This chapter says nothing about pairs of universes, their creation, or matter and antimatter; Chapters 18 to 21 treat these questions and state exactly what is and what is not proved about them.

### 3.37 Exercises

**Exercise 1.** In the plane, use the coordinates $u = x + y$ and $v = x - y$. Find the line element, the metric and its Christoffel symbols.

*Answer.* Solving for $x$ and $y$: $x = (u + v)/2$ and $y = (u - v)/2$ (add and subtract the two definitions). So $dx = (du + dv)/2$ and $dy = (du - dv)/2$ (each coefficient is constant), and

$$
ds^2 = dx^2 + dy^2 = \frac{(du + dv)^2 + (du - dv)^2}{4} = \frac{2\,du^2 + 2\,dv^2}{4} = \frac{du^2 + dv^2}{2}
$$

(the squares of a sum and of a difference; the mixed terms $\pm 2\,du\,dv$ cancel). The metric is $\mathrm{diag}(1/2, 1/2)$. It is constant, so all its derivatives vanish and every Christoffel symbol is zero (Section 3.15): in these coordinates straight lines are again $d^2u/d\lambda^2 = d^2v/d\lambda^2 = 0$.

**Exercise 2.** Figure 03a.1 shows the corrected metric at $z = \pi/4$, $a_4 = 0.5$, $b_4 = e^{2/3}$ with the entries $0.717$, $2.718$ (three times), $-1$ and $-0.638$ (three times), in the order $x_0, \dots, x_7$. Multiply them and compare with $\det g = e^{-2a_4}b_4^4\cot^2 z\,|\sin z|$. Then do the same exactly, and say how the product changes when $b_4$ doubles, and when $a_4$ grows by $\delta$ while $b_4$ stays fixed.

*Answer.* With the rounded numbers: $2.718^3 = 20.0793$ and $(-0.638)^3 = -0.259694$ (an odd power keeps the minus sign), so the product is $0.717 \times 20.0793 \times (-1) \times (-0.259694) = 3.7388$ (the two minus signs cancel). The formula gives $e^{-1}\cdot(e^{2/3})^4\cdot\cot^2(\pi/4)\cdot\sin(\pi/4) = e^{-1 + 8/3}/\sqrt2 = e^{5/3}/\sqrt2 = 3.7438$ ($\cot(\pi/4) = 1$, $\sin(\pi/4) = 1/\sqrt2$). Exactly, the entries are $e^{-1}e^{2/3} = e^{-1/3}$, $e^{2 \cdot 0.5} = e$, $-1$ and $-e^{-1/3}(\sin^2\frac{\pi}{4})^{1/6} = -e^{-1/3}2^{-1/6}$, and their product is $e^{-1/3}\cdot e^3\cdot(-1)\cdot\bigl(-e^{-1/3}2^{-1/6}\bigr)^3 = e^{-1/3 + 3 - 1}\,2^{-1/2} = e^{5/3}/\sqrt2$ (the powers multiplied out; $(2^{-1/6})^3 = 2^{-1/2}$). The difference $0.005$ comes only from rounding the entries to three decimals (they are $0.716531$ and $-0.638357$). When $b_4$ doubles, the hidden entry and each of the three extra-time entries double, so the product is multiplied by $2^4 = 16$, as $b_4^4$ says. When $a_4$ grows by $\delta$, the hidden entry is multiplied by $e^{-2\delta}$, each 3-space entry by $e^{2\delta}$ and each extra-time entry by $e^{-2\delta}$, so the product by $e^{-2\delta + 6\delta - 6\delta} = e^{-2\delta}$, as $e^{-2a_4}$ says: what the three 3-space directions gain, the three extra times lose, and the factor of the hidden direction is left over.

**Exercise 3.** Compute $\Gamma^{x_4}{}_{x_5x_5}$ and $\Gamma^{x_0}{}_{x_5x_5}$ of the corrected metric directly from the Christoffel formula, without the four cases.

*Answer.* The formula of Section 3.15 with $a = x_4$, $b = c = x_5$ keeps only $d = x_4$ (the metric is diagonal): $\Gamma^4{}_{55} = \tfrac12 g^{44}(\partial_5g_{45} + \partial_5g_{45} - \partial_4g_{55}) = \tfrac12(-1)(0 + 0 - \partial_4g_{55}) = \tfrac12\partial_4g_{55}$ ($g_{45} = 0$; $g^{44} = -1$). With $g_{55} = -e^{-2a_4}b_4W^2$, $\partial_4g_{55} = -\bigl(-2a_4'e^{-2a_4}b_4 + e^{-2a_4}b_4'\bigr)W^2 = (2a_4'b_4 - b_4')e^{-2a_4}W^2$ (the product rule for $e^{-2a_4}\cdot b_4$, the chain rule $\partial_4e^{-2a_4} = -2a_4'e^{-2a_4}$; $W^2$ does not depend on $x_4$), so $\Gamma^4{}_{55} = \bigl(a_4'b_4 - \tfrac12 b_4'\bigr)e^{-2a_4}W^2$. Since $\alpha_tf^2 = \bigl(-a_4' + \frac{b_4'}{2b_4}\bigr)e^{-2a_4}b_4 = \bigl(-a_4'b_4 + \frac12 b_4'\bigr)e^{-2a_4}$, this is $-\alpha_tf^2W^2$. For $\Gamma^0{}_{55}$ the formula with $a = x_0$, $b = c = x_5$ keeps only $d = x_0$, and the two terms with $g_{05} = 0$ vanish: $\Gamma^0{}_{55} = -\tfrac12 g^{00}\partial_0g_{55}$, with $g^{00} = 1/(f^2\cot^2 z)$ and

$$
\partial_0g_{55} = -f^2\,\partial_0(\sin^2 z)^{1/6} = -f^2\cdot\frac16(\sin^2 z)^{-5/6}\cdot 2\sin z\cos z\cdot 6H = -2Hf^2\cot z\,W^2
$$

(the power rule and the chain rule; $(\sin^2 z)^{-5/6}\sin z\cos z = (\sin^2 z)^{1/6}\cos z/\sin z$). So $\Gamma^0{}_{55} = -\frac12\cdot\frac{1}{f^2\cot^2 z}\cdot\bigl(-2Hf^2\cot z\,W^2\bigr) = HW^2\,\frac{\cot z}{\cot^2 z} = HW^2\tan z$. Both agree with the table of Section 3.23.

**Exercise 4.** (a) By what angle does a vector turn when it is carried once around the equator of a sphere? (b) Show that for a small circle around the pole, $\theta_0 \ll 1$, the turning angle is about $\pi\theta_0^2$, and explain this number.

*Answer.* (a) With $\theta_0 = \pi/2$, $\cos\theta_0 = 0$: the transport equations of Section 3.16 give $du/d\varphi = dw/d\varphi = 0$, so the vector does not turn at all relative to the south and east directions; the formula $2\pi(1 - \cos\theta_0) = 2\pi$ is one whole turn, the same direction. This fits: the cap is a hemisphere of area $2\pi a^2$, and the equator is a geodesic, along which a vector keeps its angle to the direction of travel. (b) For small $\theta_0$, $\cos\theta_0 \approx 1 - \theta_0^2/2$ (Taylor's formula, Chapter 2), so $2\pi(1 - \cos\theta_0) \approx 2\pi\cdot\theta_0^2/2 = \pi\theta_0^2$. A small cap is almost a flat disc of radius $a\theta_0$ (the distance from the pole along the sphere), with the area $\pi a^2\theta_0^2$; times the curvature $1/a^2$ this is $\pi\theta_0^2$. For $\theta_0 = 0.1$ the exact angle is $2\pi(1 - \cos 0.1) = 0.031390$ and the estimate $0.031416$; Figure 03c.3 shows the first dot at this height.

**Exercise 5.** Show that the Einstein tensor of every surface (two dimensions) is zero.

*Answer.* By Section 3.17 a surface has $R^1{}_1 = R^2{}_2 = \sigma(1, 2)$ and $R = 2\sigma(1, 2)$. The off-diagonal entries vanish: $R^1{}_2 = \sum_c R^{1c}{}_{2c} = R^{11}{}_{21} + R^{12}{}_{22} = 0$ (antisymmetry in the upper pair and in the lower pair). So $G^1{}_1 = \sigma(1, 2) - \tfrac12\cdot 2\sigma(1, 2) = 0$, likewise $G^2{}_2 = 0$, and $G^1{}_2 = G^2{}_1 = 0$. For the sphere, $1/a^2 - \tfrac12\cdot 2/a^2 = 0$. In two dimensions the Einstein tensor says nothing about the curvature; this is why gravity needs more dimensions.

**Exercise 6.** For the canonical slope $A = 1$ on the first slice of the history of Section 3.8 ($a_4 = 0$, so $k = 1$) and $\Lambda = 0$, find $\kappa\rho$, the three pressures $\kappa p_3$, $\kappa p_0$, $\kappa p_t$ and the ratios $w = p/\rho$ that Einstein's equations require. Which $\Lambda$ would make $\rho = 0$, and what are then the pressures?

*Answer.* From Section 3.26 with $A = 1$ and $k = 1$: $\kappa\rho = -(6 + \frac13)H^2 = -\frac{19}{3}H^2$, $\kappa p_3 = (6 - \frac{13}{9})H^2 = \frac{41}{9}H^2$ and $\kappa p_0 = \kappa p_t = (3 - \frac{11}{3})H^2 = -\frac23 H^2$, so $w_3 = \frac{41/9}{-19/3} = -\frac{41}{57} = -0.719$ and $w_0 = w_t = \frac{-2/3}{-19/3} = \frac{2}{19} = 0.105$; the energy density is negative. $\rho = 0$ needs $\Lambda = -(6k + \frac13 A^2)H^2 = -\frac{19}{3}H^2$, and then $\kappa p_3 = (\frac{41}{9} - \frac{19}{3})H^2 = -\frac{16}{9}H^2$ and $\kappa p_0 = \kappa p_t = (-\frac23 - \frac{19}{3})H^2 = -7H^2$. In both cases $\kappa(\rho + p_0) = \kappa(\rho + p_t) = -7H^2 = -(3k + 4A^2)H^2$ and $\kappa(\rho + p_3) = -\frac{16}{9}H^2$, as Section 3.26 says for every $\Lambda$: the cosmological constant cancels from $\rho + p$.

**Exercise 7.** Show that along the histories of Section 3.8 the Kretschmann scalar satisfies $K \ge \frac{3588}{151}k^2H^4$ for every slope $A$, and find the smallest value of $K$ and the slope at which it is reached on the three slices $a_4 = 0, 1, 2$ of Figure 03b.6.

*Answer.* $K = \bigl(\frac{2416}{81}A^4 - \frac{16}{3}A^2k + 24k^2\bigr)H^4$ (Section 3.25). With $t = A^2/k \ge 0$ (and $k > 0$) this is $K = k^2H^4\,p(t)$ with $p(t) = \frac{2416}{81}t^2 - \frac{16}{3}t + 24$ (each term divided by $k^2$ and the factor $k^2$ put in front). The parabola $p$ opens upwards; its derivative $\frac{4832}{81}t - \frac{16}{3}$ is zero at $t = \frac{16}{3}\cdot\frac{81}{4832} = \frac{1296}{14496} = \frac{27}{302}$, and there

$$
p = 24 - \frac{(16/3)^2}{4\cdot 2416/81} = 24 - \frac{256}{9}\cdot\frac{81}{9664} = 24 - \frac{2304}{9664} = 24 - \frac{36}{151} = \frac{3588}{151} = 23.762
$$

(the lowest value of $\alpha t^2 + \beta t + \gamma$ with $\alpha > 0$ is $\gamma - \beta^2/(4\alpha)$, by completing the square). So $K \ge 23.76\,k^2H^4 > 0$ for every slope, on every slice. On the slice $a_4 = 0$ ($k = 1$) the smallest value $23.76H^4$ is reached at $A = \sqrt{27/302} = 0.299$; on $a_4 = 1$ ($k = e^{2/3} = 1.948$) it is $23.762 \times 1.948^2 = 90.14H^4$ at $A = \sqrt{27/302 \times 1.948} = 0.417$; on $a_4 = 2$ ($k = e^{4/3} = 3.794$) it is $341.97H^4$ at $A = 0.582$. These are the low points of the three red curves of Figure 03b.6; for comparison, $A = 1$ on the first slice gives $48.49H^4$.

**Exercise 8.** A particle starts at $x_4 = 0$ with the frame velocity $w > 0$ along $x_1$ and no other motion, on the history $a_4 = AHx_4$ (with any $b_4$). (a) Show that it stays at its height $y$ and that $e^{AHx_4} = w\sinh\theta$ with $\theta = AH\tau + \operatorname{arsinh}(1/w)$, where $\operatorname{arsinh}$ is the inverse function of $\sinh$. (b) Express $\hat u^1$ and $u^4$ through $\theta$. (c) Evaluate everything for $w = 1$, $A = H = 1$ at $\tau = 3$ and compare with In [10] of Notebook 03d.

*Answer.* (a) Its extra-time momenta are zero, so $E = 0$ for ever, and the push law of Section 3.31 keeps $f^2\,dy/d\tau$ at its starting value $0$: $y$ does not change. Its momentum $p_1 = e^{2a_4}u^1 = e^{a_4}\hat u^1$ equals $w$ (at $x_4 = 0$, $a_4 = 0$), so $\hat u^1 = we^{-a_4}$, $S = w^2e^{-2a_4}$ and $(u^4)^2 = 1 + S$ (Section 3.31 with $\hat u^0 = 0$ and $E = 0$), so that $dx_4/d\tau = \sqrt{1 + w^2e^{-2AHx_4}}$ (the positive root: $x_4$ advances). For $s = e^{AHx_4}$,

$$
\frac{ds}{d\tau} = AH\,s\,\frac{dx_4}{d\tau} = AH\,s\sqrt{1 + \frac{w^2}{s^2}} = AH\sqrt{s^2 + w^2}
$$

(the chain rule). If $\theta = \operatorname{arsinh}u$, then $u = \sinh\theta$ and $du/d\theta = \cosh\theta = \sqrt{1 + \sinh^2\theta} = \sqrt{1 + u^2}$ (Chapter 1: $\cosh^2 - \sinh^2 = 1$, and $\cosh > 0$), so $d\theta/du = 1/\sqrt{1 + u^2}$. With $u = s/w$ and the chain rule, $\frac{d}{d\tau}\operatorname{arsinh}\frac{s}{w} = \frac{1}{\sqrt{1 + s^2/w^2}}\cdot\frac1w\cdot\frac{ds}{d\tau} = \frac{1}{\sqrt{w^2 + s^2}}\cdot\frac{ds}{d\tau} = AH$. A quantity with a constant rate grows linearly; with $s(0) = 1$, $\operatorname{arsinh}(s/w) = AH\tau + \operatorname{arsinh}(1/w) = \theta$, so $e^{AHx_4} = s = w\sinh\theta$. (b) $\hat u^1 = we^{-a_4} = w/s = 1/\sinh\theta$, and $u^4 = \sqrt{1 + 1/\sinh^2\theta} = \cosh\theta/\sinh\theta$. (c) $\operatorname{arsinh}1 = \ln(1 + \sqrt2) = 0.881374$ (solve $\sinh\theta = 1$, that is $e^{2\theta} - 2e^\theta - 1 = 0$, for $e^\theta$), so $\theta = 3.881374$, $\sinh\theta = 24.2351$ and $\cosh\theta = 24.2557$: $x_4 = \ln 24.2351 = 3.1878$, $\hat u^1 = 1/24.2351 = 0.041263$ and $u^4 = 24.2557/24.2351 = 1.000851$, the three RESULT lines of In [10]. For large $\tau$, $\sinh\theta \approx e^\theta/2$, so $x_4 \approx \tau + \ln\frac{1 + \sqrt2}{2} = \tau + 0.188$: the clock of the moving particle stays behind the time $x_4$ by a fixed amount.

**Exercise 9.** (a) Show that for every freely falling particle the quantity $f^2\bigl((\hat u^0)^2 - E\bigr)$ does not change. (Multiply the push law by $2f\hat u^0$.) (b) Deduce $(u^4)^2 = 1 + \sum_ip_i^2\,e^{-2a_4} + c\,e^{2a_4}/b_4$ with a constant $c$: the $x_4$ velocity of a free particle is a function of $x_4$ alone. (c) For the extra-time particle of Notebook 03d, find $c$, compute $u^4$ at the time $x_4 = 2.5457$ printed in In [11], and find the $x_4$ of its turning point if its path lasted that long.

*Answer.* (a) Write $P = f\hat u^0 = f^2\,dy/d\tau$. The push law is $dP/d\tau = -HE$, and $E = \sum_jp_j^2/(fW)^2 = \bigl(\sum_jp_j^2\bigr)e^{-2Hy}/f^2$ (Section 3.31: $\hat u^j = -p_j/(fW)$ and $W = e^{Hy}$). So

$$
\frac{d(P^2)}{d\tau} = 2P\,\frac{dP}{d\tau} = -2H\,f^2\frac{dy}{d\tau}\cdot\frac{e^{-2Hy}}{f^2}\sum_jp_j^2 = \frac{d}{d\tau}\Bigl(e^{-2Hy}\sum_jp_j^2\Bigr)
$$

(the factors $f^2$ cancel; the chain rule: along the path $e^{-2Hy}$ changes at the rate $-2He^{-2Hy}\,dy/d\tau$; the momenta are constant). Hence $P^2 - \sum_jp_j^2\,e^{-2Hy}$ does not change, and since $P^2 = f^2(\hat u^0)^2$ and $\sum_jp_j^2\,e^{-2Hy} = f^2E$, this is $f^2\bigl((\hat u^0)^2 - E\bigr) = c$. (b) $(u^4)^2 = 1 + (\hat u^0)^2 + S - E = 1 + S + c/f^2$ (Section 3.31), with $S = \sum_ip_i^2e^{-2a_4}$ (from $\hat u^i = p_ie^{-a_4}$) and $1/f^2 = e^{2a_4}/b_4 = k$. Only $x_4$ appears. (c) At the start $f = 1$ ($a_4 = 0$, $b_4(0) = 1$), $\hat u^0 = 0$ and $E = 0.2^2 = 0.04$, so $c = -0.04$, and $p_i = 0$. On the history $e^{2a_4}/b_4 = e^{2x_4/3}$, so $u^4 = \sqrt{1 - 0.04\,e^{2x_4/3}}$. At $x_4 = 2.5457$: $e^{1.69713} = 5.4583$ and $u^4 = \sqrt{1 - 0.21833} = 0.88412$, the printed $0.884124$ to the five digits that the rounded $x_4$ allows (an error of $0.00005$ in $x_4$ changes $u^4$ by about $0.000004$). The turning point $u^4 = 0$ lies at $e^{2x_4/3} = 25$, $x_4 = \frac32\ln 25 = 3\ln 5 = 4.828$: exactly where the pure blueshift $0.2\,e^{a_4/3}$ would reach $1$. The formula for $q$ of Section 3.31 gives the same: from $dx_4/d\tau = (1 - q)/(1 + q) = 1 - 2q/(1 + q)$ and $d\tau = 3\,dq/(2AHq)$ follows $x_4 = \tau - \frac{3}{AH}\ln\frac{1 + q}{1 + q(0)}$, which at $q = 1$, $\tau = 6.8773$ and $q(0) = 0.0102051$ is $6.8773 - 3\ln 1.979796 = 6.8773 - 2.0490 = 4.828$.

**Exercise 10.** The extra-time particle of Notebook 03d starts at $x_4 = 0$ and $y_0 = -1$ with $\hat u^5 = v = 0.2$, $\hat u^0 = 0$ and $u^4 = u_0 = \sqrt{1 - v^2} = 0.979796$, on the history with $A = H = 1$. Define $\sigma$ by $d\sigma/d\tau = 1/f^2$, $\sigma(0) = 0$. (a) Show that $W = e^{Hy} = W_0\cos(Hv\sigma)$, with $W_0 = e^{Hy_0}$, and $u^4 = u_0 - \frac{AHv^2}{3}\sigma$. (b) Where does the particle pass the tip cut-off $y = -3$? Compare with In [11]. (c) When does it reach the tip $W = 0$? (d) Does it turn inside its half cell? For which $v$ would a particle started in the same way turn before it reaches the tip?

*Answer.* (a) By Exercise 9, $P = f\hat u^0 = f^2\,dy/d\tau$ obeys $P^2 = p_5^2e^{-2Hy} + c$ with $c = -v^2$, and $p_5^2 = v^2W_0^2$ (at the start $|p_5| = h_5\hat u^5 = fW_0v$ with $f = 1$). So $P^2 = v^2W_0^2/W^2 - v^2 = (v^2/W^2)(W_0^2 - W^2)$. The push makes $P$ negative at once and keeps it negative ($dP/d\tau = -HE < 0$ and $P(0) = 0$). Since $dW/d\tau = HW\,dy/d\tau$, $P = (f^2/(HW))\,dW/d\tau$, and therefore

$$
f^2\,\frac{dW}{d\tau} = HW\,P = -Hv\sqrt{W_0^2 - W^2}, \qquad \frac{dW}{d\sigma} = -Hv\sqrt{W_0^2 - W^2}
$$

($d\sigma = d\tau/f^2$). The function $W_0\cos(Hv\sigma)$ equals $W_0$ at $\sigma = 0$, falls at once, and has the derivative $-HvW_0\sin(Hv\sigma) = -Hv\sqrt{W_0^2 - W_0^2\cos^2(Hv\sigma)}$ for $0 \le Hv\sigma \le \pi/2$: it is the solution (the equation also allows $W = W_0$ for ever, which is excluded because $W$ starts to fall at once; once $W < W_0$ the right side is smooth and the solution is unique, Chapter 2). For $u^4$: with $S = 0$, $(\hat u^0)^2 - E = c/f^2 = -v^2/f^2$, and the law of $x_4$ with $\alpha_t = -AH/3$ gives $du^4/d\tau = -\alpha_t\bigl((\hat u^0)^2 - E\bigr) = -\frac{AH}{3}\cdot\frac{v^2}{f^2}$, so $du^4/d\sigma = f^2\,du^4/d\tau = -AHv^2/3$ and $u^4 = u_0 - \frac{AHv^2}{3}\sigma$. (b) The cut-off is $W = e^{-3}$, so $\cos(0.2\sigma) = e^{-3}/e^{-1} = e^{-2} = 0.135335$, $0.2\sigma = 1.435044$ and $\sigma = 7.17522$. Then $u^4 = 0.979796 - \frac{0.04}{3}\times 7.17522 = 0.884126$; from Exercise 9, $e^{2x_4/3} = (1 - 0.884126^2)/0.04 = 5.45802$ and $x_4 = 1.5\ln 5.45802 = 2.54563$; and with $q = (1 - u^4)/(1 + u^4) = 0.061500$ and $q(0) = (1 - u_0)/(1 + u_0) = 0.0102051$, Section 3.31 gives $\tau = 1.5\ln(q/q(0)) = 2.69422$. In [11] prints $\tau = 2.694$, $x_4 = 2.5457$ and $u^4 = 0.884124$ for the first computed state at or below the cut-off, a fraction of one RK4 step later. (c) $W = 0$ at $0.2\sigma = \pi/2$, $\sigma = 2.5\pi = 7.85398$: $u^4 = 0.979796 - \frac{0.04}{3}\times 7.85398 = 0.875076$, $e^{2x_4/3} = (1 - 0.875076^2)/0.04 = 5.85604$, $x_4 = 2.65121$, $q = 0.066623$ and $\tau = 1.5\ln(0.066623/0.0102051) = 2.81424$. The particle reaches the tip at the proper time $2.814$, only $0.12$ after the cut-off. (d) No: at the tip $u^4 = 0.875 > 0$, and $u^4 = 0$ would need $\sigma = 3u_0/(AHv^2) = 73.5$, far beyond the tip at $\sigma = 7.85$. For a particle started in the same way (at $x_4 = 0$, at rest in $y$, moving only along $x_5$) the tip comes at $\sigma = \pi/(2Hv)$ and the turning point at $\sigma = 3u_0/(AHv^2)$, both independent of the starting height; the turning point comes first when $3u_0/(AHv^2) < \pi/(2Hv)$, that is $\sqrt{1 - v^2} < A\pi v/6$, which for $A = 1$ means $v > 1/\sqrt{1 + (\pi/6)^2} = 0.886$.

**Exercise 11.** What fraction of the 7-volume of a half cell, and at which angle $z$, would a tip cut-off $L = 2/H$ remove?

*Answer.* By Section 3.9 the fraction is $e^{-3HL} = e^{-6} = 2.479 \times 10^{-3}$, about $e^3 = 20$ times more than the $e^{-9} = 1.234 \times 10^{-4}$ of the record's $L = 3/H$. The cut-off lies at $|\sin z| = e^{6Hy} = e^{-12}$, so $z = \arcsin e^{-12} = 6.144 \times 10^{-6}$ (for small $u$, $\arcsin u \approx u$).
