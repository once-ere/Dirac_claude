## 3. Spacetime geometry and the author's metric; curvature

Gravity, in Einstein's theory, is not a force that acts inside space and time: it is the shape of space and time itself. This chapter builds, from nothing but school algebra and one-variable calculus, the language in which that shape is written down and measured: coordinates, the metric, its signature, scale factors and volumes, the Christoffel symbols, geodesics (the paths of free fall), and curvature in the form of the Riemann tensor, the Ricci tensor, the Ricci scalar, the Einstein tensor and the Kretschmann scalar. Every tool is tried first where we can picture it, on the flat plane and on a sphere, and then applied, completely and line by line, to the metric that the author wrote down for the primordial gravitational field. The chapter has four worked examples, Notebooks 03a, 03c, 03b and 03d (in the order in which the chapter uses them); each reproduces, number for number, the parts of the Revision record that it overlaps and says so in a PASS line.

### 3.1 What this chapter is for

Every later chapter of the book lives in the author's eight-dimensional spacetime. The spinor fields of Chapters 4 to 10 need its vielbein (the scale factors of Section 3.7); the energy-momentum tensor of Chapter 9 needs its Christoffel symbols (Section 3.23); the field equations of the metric function $a_4$ in Chapter 12 need its Einstein tensor (Section 3.25); the Kohn-Sham model of Chapters 14 to 17 is written in the hidden coordinate $y$ of Section 3.9. This chapter derives all of these from the metric itself, and it ends with what the metric does to a body that moves freely in it (Section 3.31).

The author's metric is the following diagonal $8 \times 8$ matrix, in the order of the author's coordinates $x_1, \dots, x_8$ (Section 3.5 reads it exactly as the author typed it):

$$
\begin{aligned}
g = \mathrm{diag}\bigl(&e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ -1,\\
&-e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ \cot^2 z\bigr),\qquad z = 6Hx_8 .
\end{aligned}
$$

The coordinates have fixed roles. $x_1, x_2, x_3$ are ordinary **3-space**; it inflates, with the scale factor $e^{a_4}\sin^{1/6}z$. $x_4$ is **the time**. $x_5, x_6, x_7$ are three **extra times**: they are time-like like $x_4$, and they **deflate exponentially**, with the scale factor $e^{-a_4}\sin^{1/6}z$, while $a_4$ grows. $x_8$ is the **hidden** space direction, with $z = 6Hx_8$ between $0$ and $\pi/2$ and $g_{88} = \cot^2 z$. $H > 0$ is a constant of the author, and $a_4(x_4)$ is a function of the time only, the **metric function**; a prime means its derivative with respect to $x_4$, $a_4' = da_4/dx_4$.

The four notebooks of the chapter are:

| notebook | what it computes | Revision records it reproduces |
| --- | --- | --- |
| 03a | reads the metric exactly as the author typed it; determinant, signature (4,4), vielbein, expansion rates, the deflating history, proper volumes, the hidden coordinate $y$ and the warped form; 7 figures, 29 checks | `Revision/gkd_lovelock/results/curvature.json`, `python-lovelock-report.json`, `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`, `Revision/kohn_sham/results/parameters.json`, `Revision/kohn_sham/ks-theory.json` |
| 03c | curvature where it can be pictured: the flat plane in polar coordinates and the sphere; parallel transport, geodesics, geodesic deviation, all with RK4; 5 figures, 16 checks | none (exact formulas only) |
| 03b | all Christoffel symbols, Riemann, Ricci and Einstein components and the Kretschmann scalar of the author's metric, exactly; finite differences; the curvature along the deflating history; the source Einstein's equations would require; a negative control; 7 figures, 39 checks | `curvature.json`, `python-lovelock-report.json`, `lovelock-report.json` (all three in `Revision/gkd_lovelock/results/`), `Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`, `Revision/field_equations_a4/a4-equations.json`, `Revision/field_equations_a4/reports/python-a4-report.json` |
| 03d | free fall in the author's metric: conserved momenta, redshift in 3-space, blueshift along the extra times, the push along the hidden direction, the turning point in $x_4$; RK4 paths with the record's Christoffel symbols; 5 figures, 23 checks | `curvature.json`, `parameters.json`, `ks-theory.json`, `Revision/theory/reports/python-scope.json` |

Every statement of the chapter carries one of the five labels of Chapter 0. **PROVED** means derived exactly here, line by line, and confirmed by an exact check of a notebook; where the Revision record proves the same, the record file and its check are named. **COMPUTED** means a number obtained numerically by a notebook, with its measured accuracy. **ASSUMED** marks two kinds of statements: standard theorems that we quote without proof (each is named where it is used), and the physical inputs: that the history of the metric function is $a_4 = AHx_4$, which the Revision record itself calls a PRESCRIBED BACKGROUND (Section 3.8), and that the bodies of Section 3.31 are test particles, too small to change the metric. One question is **OPEN** (Section 3.31): whether wave packets of the fields follow the free-fall paths computed here. No HYPOTHESIS enters this chapter. Nothing in this chapter concerns pairs of universes, their creation, or matter and antimatter; those questions belong to Chapters 18 to 21, which also state precisely what is and what is not proved about them.

### 3.2 Coordinates, indices and sums

**Coordinates.** A point of the author's spacetime is named by eight real numbers, its **coordinates** $x_1, x_2, \dots, x_8$. Their roles were listed in Section 3.1. In Python a list of eight numbers is counted from 0, so position 0 holds $x_1$, position 3 the time $x_4$ and position 7 the hidden coordinate $x_8$; every notebook says so where it matters.

**Indices.** A letter written as a small label, such as the $a$ in $x_a$, is an **index**: it stands for any one of the numbers $1, \dots, 8$. An equation with an index is eight equations, one for each value. Many objects of this chapter carry several indices: the metric $g_{ab}$ has two (it is a table with 64 entries), the Christoffel symbols $\Gamma^a{}_{bc}$ have three (512 entries), the Riemann tensor $R^a{}_{bcd}$ has four (4096 entries). An index may be written **up** or **down**; Section 3.14 explains why the position matters for vectors and tensors. For the coordinates themselves the position carries no meaning: $x_4$ and $x^4$ name the same coordinate, and we write $x_a$ in prose and $dx^a$ for a small step along $x_a$.

**Sums.** In this chapter every sum is written with the sign $\sum$; for example $\sum_{a=1}^{8} V^a W_a = V^1W_1 + V^2W_2 + \dots + V^8W_8$. When the range is the eight coordinates we write $\sum_a$. Where a formula repeats an index but does not sum over it we write "(no sum)".

**The Kronecker delta.** $\delta^a{}_b$ (also written $\delta_{ab}$) is $1$ when $a = b$ and $0$ otherwise. It is the table of the $8 \times 8$ unit matrix.

**Partial derivatives.** For a function $f(x_1, \dots, x_8)$ the **partial derivative** $\partial_a f = \partial f / \partial x_a$ is the ordinary derivative with respect to $x_a$ while the seven other coordinates are held fixed (Chapter 2 teaches it from zero). The author's metric depends on two coordinates only: on $x_4$ through $a_4(x_4)$ and on $x_8$ through $z = 6Hx_8$. By the **chain rule**, a function of $z$ has

$$
\partial_8 f = \frac{df}{dz}\,\frac{dz}{dx_8} = 6H\,\frac{df}{dz},
$$

(the derivative of a function of $z$ with respect to $x_8$ is its derivative with respect to $z$ times $dz/dx_8 = 6H$), and a function of $a_4$ has $\partial_4 f = a_4'\, df/da_4$ (the same rule with $da_4/dx_4 = a_4'$). Every other partial derivative of the metric is zero.

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
\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)
$$

in the order $x_1, \dots, x_8$: four positive and four negative entries, the signature **(4,4)**. Four directions are space-like ($x_1, x_2, x_3, x_8$) and four are time-like ($x_4, x_5, x_6, x_7$). With four time-like directions one of them must be chosen as the time in which everything evolves; the author chooses $x_4$, and the other three are the extra times.

### 3.5 The author's metric

The Rust program `lovelock_gkd`, which computed the curvature of the metric for the Revision record, stored the author's text of the metric under the name `metricAsGiven` in its output file `Revision/gkd_lovelock/results/curvature.json`. Printed with one row of the matrix per line (Notebook 03a, In [3]):

```text
{{exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0,0},
{0,exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0},
{0,0,exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0},
{0,0,0,-1,0,0,0,0},
{0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0},
{0,0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0},
{0,0,0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0},
{0,0,0,0,0,0,0,Cot[6 H x8]^2}}
```

It is written in the notation of Mathematica: braces enclose a list (the matrix is a list of eight rows of eight entries), `exp^(...)` is $e$ to the power in brackets, `Sin` and `Cot` are the sine and the cotangent, `a4[x4]` is the value of the function $a_4$ at $x_4$, and a blank between two factors means times. Only the eight diagonal entries are non-zero; the line element is therefore

$$
ds^2 = e^{2a_4}\sin^{1/3}z\,\bigl(dx_1^2 + dx_2^2 + dx_3^2\bigr) - dx_4^2 - e^{-2a_4}\sin^{1/3}z\,\bigl(dx_5^2 + dx_6^2 + dx_7^2\bigr) + \cot^2 z\, dx_8^2 ,\qquad z = 6Hx_8 .
$$

**Reading it term by term.** A step $dx_1$ in 3-space has the true (proper) length $e^{a_4}\sin^{1/6}z\,dx_1$, the square root of its coefficient: when $a_4$ grows, 3-space **inflates**. A step $dx_5$ along an extra time has the proper duration $e^{-a_4}\sin^{1/6}z\,dx_5$: when $a_4$ grows, the three extra times **deflate exponentially**. A step $dx_4$ has $ds^2 = -dx_4^2$, so a clock at rest shows exactly $x_4$: the coordinate $x_4$ is the proper time of an observer at rest (Section 3.23 shows that such an observer is in free fall). The hidden direction has the coefficient $\cot^2 z$, which depends on $x_8$ only.

**Units.** $z = 6Hx_8$ is an angle (a pure number), so $H$ has the unit of an inverse length. In all numerical work of the chapter lengths and times are measured in units of $1/H$, which is the same as setting $H = 1$.

**The patch.** The metric is used for $0 < z < \pi/2$, that is $0 < x_8 < \pi/(12H)$; we call this range the **patch**. Its end $z \to 0$ is the **tip** and its end $z = \pi/2$ the **patch end**. Inside the patch $\sin z > 0$, so the cube root $\sin^{1/3}z$ is a positive number, and $\cot z = \cos z/\sin z > 0$. At the patch end $\cot z = 0$, so $g_{88} = 0$ there and the matrix $g$ has no inverse: the coordinate $x_8$ stops being a good label there (Section 3.9 shows that another coordinate, $y$, has no such problem, just as polar coordinates fail at $r = 0$ while the plane is perfectly regular there).

**The signature is (4,4) at every point of the patch, for every $a_4$** (PROVED). The proof is one line per sign: $e^{2a_4} > 0$ and $e^{-2a_4} > 0$ for every real $a_4$ (an exponential is positive); $\sin^{1/3}z > 0$ inside the patch (shown above); hence the three 3-space entries are positive and the three extra-time entries, which carry a minus sign, are negative; $g_{44} = -1 < 0$; and $\cot^2 z > 0$ because $\cot z > 0$ inside the patch. So the signs are $(+,+,+,-,-,-,-,+)$, those of $\eta$. Notebook 03a confirms this on a grid of 400 values of $z$ and 13 values of $a_4$ (In [8]); at $z = 0.7$ and $a_4 = 0.5$ it prints $g_{11} = 2.347679$ and $g_{55} = -0.317724$.

### 3.6 The determinant and proper volumes

**The volume of a small box.** In flat Cartesian coordinates a small box with edges $dx$, $dy$, $dz$ has the volume $dx\,dy\,dz$. In the plane in polar coordinates a small box with edges $dr$ and $d\varphi$ has the true edge lengths $dr$ and $r\,d\varphi$, so its area is $r\,dr\,d\varphi$. For any diagonal metric the same reasoning gives: a box with coordinate edges $dx^1, \dots, dx^n$ has the proper edge lengths $\sqrt{|g_{aa}|}\,dx^a$, and its proper volume is the product

$$
\prod_{a=1}^{n} \sqrt{|g_{aa}|}\;dx^1 \cdots dx^n = \sqrt{|\det g|}\;dx^1\cdots dx^n ,
$$

because the **determinant** of a diagonal matrix is the product of its diagonal entries, and the square root of a product of positive numbers is the product of their square roots. (For a metric that is not diagonal the volume factor is also $\sqrt{|\det g|}$; we quote this without proof, ASSUMED, and do not need it.) The factor $\sqrt{|\det g|}$ is the **volume factor**.

**The determinant of the author's metric.** We compute it line by line; after each line we name the rule that produced it.

$$
\det g = g_{11}\,g_{22}\,g_{33}\,g_{44}\,g_{55}\,g_{66}\,g_{77}\,g_{88}
$$

(the determinant of a diagonal matrix is the product of its diagonal entries)

$$
= \bigl(e^{2a_4}\sin^{1/3}z\bigr)^3\cdot(-1)\cdot\bigl(-e^{-2a_4}\sin^{1/3}z\bigr)^3\cdot\cot^2 z
$$

(the entries inserted; three equal factors written as a cube)

$$
= e^{6a_4}\sin z\cdot(-1)\cdot\bigl(-e^{-6a_4}\sin z\bigr)\cdot\cot^2 z
$$

(a power of a product is the product of the powers: $(e^{2a_4})^3 = e^{6a_4}$, $(\sin^{1/3}z)^3 = \sin z$, and an odd power keeps the minus sign, $(-1)^3 = -1$)

$$
= e^{6a_4}e^{-6a_4}\,\sin^2 z\,\cot^2 z = \sin^2 z\,\cot^2 z
$$

(the two minus signs multiply to $+1$, and $e^{6a_4}e^{-6a_4} = e^{0} = 1$)

$$
= \sin^2 z\,\frac{\cos^2 z}{\sin^2 z} = \cos^2 z
$$

($\cot z = \cos z/\sin z$). Inside the patch $\cos z > 0$, so

$$
\sqrt{|\det g|} = \cos z .
$$

This is PROVED here and in the Revision record (`Revision/gkd_lovelock/results/python-lovelock-report.json`, check `sqrt_abs_det_g`; `curvature.json` stores $\sqrt{|\det g|}$ as `Sin[6*H*x8]*Cot[6*H*x8]` under the name `sqrtAbsDetG`); Notebook 03a reproduces both (In [7]). The function $a_4$ has dropped out in the fourth line: the factor $e^{6a_4}$ of the three inflating 3-space directions and the factor $e^{-6a_4}$ of the three deflating extra times cancel.

**The volume of a slice of constant time.** The eight-dimensional "volume" mixes lengths and durations. The meaningful volume is that of a slice $x_4 = \mathrm{const}$, a seven-dimensional space with the coordinates $x_1, x_2, x_3, x_5, x_6, x_7, x_8$. Its volume factor is the product of the seven scale factors other than that of $x_4$, which is $\sqrt{|g_{44}|} = 1$; so it equals $\sqrt{|\det g|} = \cos z$. It does not depend on $x_4$: **the proper 7-volume of a region with fixed coordinate ranges does not change in time** (PROVED; Notebook 03a, In [17]).

**Three partial volumes.** Take a box with the coordinate edges $\Delta x_1 = \Delta x_2 = \Delta x_3 = 1$ (small enough that $z$ hardly changes along it, or at one value of $z$). Its proper 3-volume in 3-space is

$$
V_3 = \bigl(e^{a_4}\sin^{1/6}z\bigr)^3 = e^{3a_4}\sin^{1/2}z
$$

(the product of three equal scale factors; a power of a product is the product of the powers). The same box in the three extra times has $V_t = (e^{-a_4}\sin^{1/6}z)^3 = e^{-3a_4}\sin^{1/2}z$, and $V_3 V_t = \sin z$ (the exponentials cancel and $\sin^{1/2}z\cdot\sin^{1/2}z = \sin z$). What 3-space gains in volume, the extra times lose.

**The 7-volume of the whole patch.** Per unit coordinate volume of the six directions $x_1, x_2, x_3, x_5, x_6, x_7$, the proper 7-volume of the patch is the integral of the volume factor over $x_8$:

$$
\int_0^{\pi/(12H)} \cos(6Hx_8)\,dx_8 = \Bigl[\frac{\sin(6Hx_8)}{6H}\Bigr]_0^{\pi/(12H)}
$$

(an antiderivative of $\cos(6Hx_8)$ is $\sin(6Hx_8)/(6H)$: differentiate it with the chain rule to check)

$$
= \frac{\sin(\pi/2) - \sin 0}{6H} = \frac{1}{6H}
$$

(insert the two limits; $6H\cdot\pi/(12H) = \pi/2$). PROVED; Notebook 03a computes the same integral with sympy (In [17]).

### 3.7 Scale factors, the vielbein and the rates of expansion

**Scale factors.** Write each diagonal entry as a sign times a square, $g_{aa} = \eta_{aa}\,h_a^2$ with a positive number $h_a$, the **scale factor** of the direction $x_a$: a coordinate interval $\Delta x_a$ over which $h_a$ does not change has the proper length (or, for a time-like direction, the proper duration) $h_a\,\Delta x_a$. For the author's metric, inside the patch,

$$
h = \bigl(e^{a_4}\sin^{1/6}z,\ e^{a_4}\sin^{1/6}z,\ e^{a_4}\sin^{1/6}z,\ 1,\ e^{-a_4}\sin^{1/6}z,\ e^{-a_4}\sin^{1/6}z,\ e^{-a_4}\sin^{1/6}z,\ \cot z\bigr)
$$

(the positive square roots of the absolute values of the diagonal entries: $\sqrt{e^{2a_4}\sin^{1/3}z} = e^{a_4}\sin^{1/6}z$, and $\sqrt{\cot^2 z} = \cot z$ because $\cot z > 0$ in the patch).

**The vielbein.** At every point imagine eight measuring rods and clocks of unit proper length, one along each coordinate direction, all perpendicular to each other. Such a set is a **frame**, and the matrix $e^a{}_\mu$ that converts coordinate steps into frame components is the **vielbein** (German for "many legs"): the metric is

$$
g_{\mu\nu} = \sum_{a,b} e^a{}_\mu\,\eta_{ab}\,e^b{}_\nu .
$$

For a diagonal metric the diagonal vielbein $e^a{}_\mu = h_\mu\,\delta^a{}_\mu$ (no sum) does this: the double sum keeps only $a = b = \mu = \nu$ and gives $\eta_{\mu\mu} h_\mu^2 = g_{\mu\mu}$. The spinor fields of the book need exactly this frame (Chapter 6). PROVED here; the lead's independent check `vielbein_reproduces_metric` of `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json` checks the same, and Notebook 03a reproduces it (In [11]).

**The rate of expansion.** A coordinate interval $\Delta x_a$ has the proper length $L = h_a\,\Delta x_a$. The fraction by which it grows per unit of time is

$$
\frac{1}{L}\frac{\partial L}{\partial x_4} = \frac{\partial_4 h_a}{h_a} = \partial_4 \ln h_a
$$

(the coordinate interval does not change; the derivative of $\ln u$ is $u'/u$). For 3-space,

$$
\ln h_1 = a_4 + \tfrac16 \ln\sin z \quad\Rightarrow\quad \partial_4 \ln h_1 = a_4'
$$

(the logarithm of a product is the sum of the logarithms, $\ln e^{a_4} = a_4$, $\ln \sin^{1/6} z = \frac16\ln\sin z$; only $a_4$ depends on $x_4$). For an extra time,

$$
\ln h_5 = -a_4 + \tfrac16 \ln\sin z \quad\Rightarrow\quad \partial_4 \ln h_5 = -a_4'
$$

(the same rules). $h_4 = 1$ and $h_8 = \cot z$ do not depend on $x_4$, so their rates are $0$. When $a_4' > 0$, **3-space expands at the rate $a_4'$ and the three extra times shrink at the same rate**. The six **transverse** scale factors (those of $x_1, x_2, x_3, x_5, x_6, x_7$) multiply to

$$
h_1 h_2 h_3 h_5 h_6 h_7 = e^{3a_4}\sin^{1/2}z\cdot e^{-3a_4}\sin^{1/2}z = \sin z ,
$$

without $a_4$. All of this is PROVED and is checked exactly by Notebook 03a (In [12]). The factor $\sin^{1/6}z$ that the six transverse scale factors share is the **warp factor** $W = \sin^{1/6}z$; the six transverse metric entries contain its square $W^2 = \sin^{1/3}z$.

### 3.8 The deflating history: a prescribed background

The metric does not fix the function $a_4(x_4)$. The field equations of gravity relate it to the energy and the pressures of the matter in the spacetime; Chapter 12 derives them. For pictures and numbers this chapter uses the simplest member of the family, the **linear history**

$$
a_4 = AHx_4, \qquad a_4' = AH, \qquad a_4'' = 0,
$$

with a constant **slope** $A$. With $A > 0$ the function $a_4$ increases, 3-space inflates like $e^{AHx_4}$ and the extra times deflate like $e^{-AHx_4}$: exponential deflation, as the author requires. The Revision Kohn-Sham work uses $A = 1$ and $H = 1$, and computes its states on five **slices** $a_4 = 0, 0.5, 1, 1.5, 2$ (record `Revision/kohn_sham/results/parameters.json`, keys `physics.H`, `physics.historyA`, `physics.slicesA4`; Notebook 03a, In [13]). Between the first and the last slice, 3-space lengths grow by the factor $e^2 = 7.389056$ and extra-time durations shrink by the factor $e^{-2} = 0.135335$ (Notebook 03a, In [14]); the product of the two factors stays $1$.

**Status: ASSUMED.** The history is not a solution of the coupled field equations. The Revision record says so in its own words (`Revision/kohn_sham/ks-theory.json`, key `adiabaticity.historyStatus`): "PRESCRIBED BACKGROUND: the history a4 = A H x4 is prescribed, not solved for." The reason, also stated there: the field equations of $a_4$ allow this linear member only for a source with equal pressures in all directions and a constant energy density, and the Kohn-Sham states computed along it do not have these properties (record `Revision/field_equations_a4/reports/ks-source-conditions.json`). Every formula of this chapter written with a general $a_4(x_4)$ is exact; only the pictures and the numbers along the history use the assumption. The pictures and numbers of this chapter use only slopes $A > 0$, for which the extra times deflate, as the author requires; a slope $A = 0$ would freeze the extra times and a slope $A < 0$ would make them inflate and 3-space deflate.

### 3.9 The hidden coordinate y and the warped form of the metric

The entry $\cot^2 z$ makes the hidden direction awkward: it grows without bound at the tip and vanishes at the patch end. The Revision Kohn-Sham work uses instead the coordinate

$$
y = \frac{\ln(\sin z)}{6H}, \qquad z = 6Hx_8 .
$$

**It measures proper distance.** Line by line:

$$
\frac{dy}{dx_8} = \frac{1}{6H}\cdot\frac{\cos z}{\sin z}\cdot 6H
$$

(the chain rule: the derivative of $\ln u$ is $1/u$, the derivative of $\sin z$ is $\cos z$, and $dz/dx_8 = 6H$)

$$
= \cot z
$$

(the factors $6H$ cancel, and $\cos z/\sin z = \cot z$). So $dy = \cot z\,dx_8$ and $dy^2 = \cot^2 z\,dx_8^2 = g_{88}\,dx_8^2$: a step $dy$ is a step of proper length $dy$ along the hidden direction. (Record: `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`, check `ks_coordinate_jacobian`; Notebook 03a, In [19].)

**The warp factor in $y$.** From the definition, $6Hy = \ln\sin z$, so

$$
\sin z = e^{6Hy}
$$

($e$ to the power of both sides; $e^{\ln u} = u$), and therefore

$$
W = \sin^{1/6}z = \bigl(e^{6Hy}\bigr)^{1/6} = e^{Hy}, \qquad W^2 = \sin^{1/3}z = e^{2Hy}
$$

(a power of a power multiplies the exponents). Inserting $dy^2$ and $W^2$ into the line element of Section 3.5 gives the **warped form**

$$
ds^2 = dy^2 - dx_4^2 + W^2\Bigl[e^{2a_4}\bigl(dx_1^2 + dx_2^2 + dx_3^2\bigr) - e^{-2a_4}\bigl(dx_5^2 + dx_6^2 + dx_7^2\bigr)\Bigr], \qquad W = e^{Hy} .
$$

This is exactly the line element of the record (`Revision/kohn_sham/ks-theory.json`, keys `geometry.lineElement` and `geometry.warp`); Notebook 03a checks it entry by entry with sympy (In [19]). PROVED.

**The range of $y$.** As $z$ runs from $0$ to $\pi/2$, $\sin z$ runs from $0$ to $1$ and $\ln\sin z$ from $-\infty$ to $0$. So $y$ runs from $-\infty$ (the tip) to $0$ (the patch end). The tip lies at an infinite proper distance from every point of the patch (PROVED; Notebook 03a, In [19]). At the patch end $y = 0$ nothing goes wrong in the warped form: the coefficient of $dy^2$ is $1$. The failure of $g_{88}$ there was a failure of the coordinate $x_8$, not of the geometry.

**The volume factor in $y$.** In the coordinates $(x_1, \dots, x_7, y)$ the scale factor of the hidden direction is $1$, so the volume factor is the product of the six transverse scale factors, $W^6 = e^{6Hy} = \sin z$ (record key `geometry.sqrtDetG`: "e^{6Hy} (= cos z in the x8 chart)"). The two volume factors $\sin z$ (in $y$) and $\cos z$ (in $x_8$) describe the same volume, because $\cos z\,dx_8 = \cos z\,\tan z\,dy = \sin z\,dy$ (from $dx_8 = dy/\cot z = \tan z\,dy$).

**The tip cut-off.** The Revision Kohn-Sham solver keeps only $-L \le y \le 0$ with $L = 3/H$ (record key `physics.L_tipCutoff`). The fraction of the 7-volume that it leaves out is

$$
\frac{\int_{-\infty}^{-L} e^{6Hy}\,dy}{\int_{-\infty}^{0} e^{6Hy}\,dy} = \frac{e^{-6HL}/(6H)}{1/(6H)} = e^{-6HL}
$$

(an antiderivative of $e^{6Hy}$ is $e^{6Hy}/(6H)$, which tends to $0$ as $y \to -\infty$), which for $L = 3/H$ is $e^{-18} = 1.5230\times 10^{-8}$. The cut-off lies at the tiny angle $z = \arcsin e^{-18} = 1.5230\times 10^{-8}$ (both COMPUTED in Notebook 03a, In [20]; the fraction is exact).

### 3.10 Example: the author's metric, read and checked

Notebook 03a puts Sections 3.2 to 3.9 to work. It reads the metric exactly as the author typed it from the record `curvature.json` and turns the text into an exact sympy matrix; checks it against a second, hand-typed copy and against the record's diagonal entries; computes the determinant and the volume factor; checks the signature on a grid; builds the vielbein and the expansion rates; reads the history of the Revision Kohn-Sham work and draws the scale factors along it; computes the proper volumes; and checks the hidden coordinate $y$, the warped form and the volume factor in $y$ against the record `ks-theory.json`. It needs no Rust, runs in about 15 seconds and ends with the line ALL 29 CHECKS PASSED (notebook 03a).

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

**In [3], the author's text.**

```python
import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols
from sympy.parsing.sympy_parser import (implicit_multiplication, parse_expr,
                                        standard_transformations)
```

numpy (short name `np`) works with **arrays**, lists of numbers on which arithmetic acts entry by entry; sympy (short name `sp`) does exact algebra with symbols. `parse_expr` turns a text such as `"2*x + 1"` into a sympy expression; `standard_transformations` and `implicit_multiplication` are reading rules for it (explained at In [5]).

```python
CURVATURE_RECORD = "Revision/gkd_lovelock/results/curvature.json"
record = json.loads(repository_file(CURVATURE_RECORD).read_text(encoding="utf-8"))
author_text = record["metricAsGiven"]  # the metric exactly as the author typed it
say(f"The metric as the author wrote it ({len(author_text)} characters):")
for line in author_text.replace("},", "},\n").split("\n"):  # one row per line
    print(line)
```

The first line names the record file. The second reads the file as text (`read_text`) and turns the JSON text into a Python dictionary (`json.loads`). `record["metricAsGiven"]` is the author's text of the metric, 350 characters long, as the output shows. The loop prints it with one row of the matrix per line: `replace("},", "},\n")` puts a line break (`\n`) after every row and `split("\n")` cuts the text at the breaks. The output is the matrix of Section 3.5.

**In [4], the symbols.**

```python
x1, x2, x3, x4, x5, x6, x7, x8 = sp.symbols("x1:9", real=True)  # 8 coordinates
COORDS = [x1, x2, x3, x4, x5, x6, x7, x8]
H = sp.symbols("H", positive=True)  # the constant of the author, H > 0
a4 = sp.Function("a4")(x4)  # the metric function: an unknown function of x4
a4p, a4v = sp.symbols("a4p a4v", real=True)  # a4p = a4 prime, a4v = value of a4
z = sp.symbols("z", positive=True)  # z = 6 H x8, for printing
```

`sp.symbols("x1:9", real=True)` makes the eight symbols `x1`, ..., `x8` (the range `1:9` means 1 to 8), declared real; `COORDS` is their list. `H` is declared positive, which lets sympy simplify, for example, $\sqrt{H^2} = H$. `sp.Function("a4")(x4)` is an unknown function of `x4`: sympy can differentiate it (giving $a_4'$) without knowing it. `a4p`, `a4v` and `z` are plain symbols used only for printing.

```python
def plain(expression):
    """Write the derivative of a4 as a4p, the value a4(x4) as a4v, 6 H x8 as z."""
    expression = expression.subs(sp.Derivative(a4, x4), a4p).subs(a4, a4v)
    return expression.subs(x8, z / (6 * H))  # then 6*H*x8 becomes z


say("Symbols: x1 ... x8, H > 0, the function a4(x4), and a4p, a4v, z for printing.")
```

`plain` rewrites an expression for printing: `.subs(old, new)` replaces `old` by `new`, first the derivative $a_4'$ by `a4p`, then the function value by `a4v`; then $x_8$ by $z/(6H)$, so that $6Hx_8$ becomes $z$. The last line prints the output of In [4].

**In [5], the text becomes a matrix.**

```python
text = author_text
text = text.replace("exp^", "E^")  # e to the power ...
text = text.replace("Sin[6 H x8]", "sin(6 H x8)")  # Mathematica [ ] -> Python ( )
text = text.replace("Cot[6 H x8]", "cot(6 H x8)")
text = text.replace("a4[x4]", "a4")  # the value of the function a4 at x4
text = text.replace("{", "[").replace("}", "]")  # Mathematica lists -> Python lists
text = text.replace("^", "**")  # Mathematica power ^ -> Python power **
```

Seven replacements translate Mathematica into Python, one rule each: `exp^` becomes `E^` (sympy's `E` is the number $e = 2.718\ldots$); the square brackets of the sine and the cotangent become round brackets; `a4[x4]` becomes `a4`; the braces of lists become square brackets (a Python list); the power sign `^` becomes `**`. The order matters: the square brackets of the functions are translated before any other bracket.

```python
names = {"E": sp.E, "a4": a4, "H": H, "x8": x8, "sin": sp.sin, "cot": sp.cot}
rows = parse_expr(text, local_dict=names,
                  transformations=standard_transformations + (implicit_multiplication,))
g = sp.Matrix(rows)  # the metric of the author as an exact 8 x 8 sympy matrix
```

The dictionary `names` tells `parse_expr` what each name in the text means: `a4` is the function $a_4(x_4)$, `H` and `x8` the symbols, `sin` and `cot` sympy's functions. `implicit_multiplication` reads a blank between two factors as a product, as Mathematica does (`6 H x8` is $6 \cdot H \cdot x_8$). The result `rows` is a list of eight lists, and `sp.Matrix(rows)` makes the exact $8 \times 8$ matrix `g`.

```python
say(f"The matrix has {g.rows} rows and {g.cols} columns. Its diagonal entries:")
for k in range(8):
    say(f"  g[x{k + 1}, x{k + 1}] = {g[k, k]}")
off_diagonal = [g[i, j] for i in range(8) for j in range(8) if i != j]
check(all(entry == 0 for entry in off_diagonal),
      "the 56 entries off the diagonal are zero: the metric is diagonal")
```

The loop prints the eight diagonal entries; `range(8)` runs over $k = 0, \dots, 7$ and `g[k, k]` is the entry in row $k$ and column $k$, printed with the author's name `x{k + 1}`. `off_diagonal` is a **list comprehension**, a list built by a loop inside square brackets: the $64 - 8 = 56$ entries with $i \ne j$. `all(...)` is true when every one of them is zero: the first PASS line. The output shows the diagonal of Section 3.5, written by sympy (`exp(2*a4(x4))*sin(6*H*x8)**(1/3)` is $e^{2a_4}\sin^{1/3}(6Hx_8)$).

**In [6], two independent checks of the reading.**

```python
warp = sp.sin(6 * H * x8) ** sp.Rational(1, 3)  # sin(z)^(1/3), Rational: exact 1/3
typed = sp.diag(sp.exp(2 * a4) * warp, sp.exp(2 * a4) * warp, sp.exp(2 * a4) * warp,
                -1,
                -sp.exp(-2 * a4) * warp, -sp.exp(-2 * a4) * warp,
                -sp.exp(-2 * a4) * warp,
                sp.cot(6 * H * x8) ** 2)
difference = (g - typed).applyfunc(sp.simplify)  # simplify every entry
check(difference == sp.zeros(8, 8),
      "the text of the author equals the metric typed by hand from the formula")
```

`sp.Rational(1, 3)` is the exact fraction $1/3$ (the Python number `1/3` would be rounded). `warp` is $\sin^{1/3}z$, the square $W^2$ of the warp factor. `sp.diag(...)` builds the diagonal matrix of the formula of Section 3.5, typed by hand. `applyfunc(sp.simplify)` simplifies every entry of the difference, and the check requires the $8 \times 8$ zero matrix `sp.zeros(8, 8)`: the reading of the text agrees with the formula.

```python
def from_mathematica(entry_text):
    """A record entry in Mathematica notation, as a sympy expression."""
    t = entry_text.replace("Sin[6*H*x8]", "sin(6*H*x8)")
    t = t.replace("Cot[6*H*x8]", "cot(6*H*x8)")
    t = t.replace("a4[x4]", "a4").replace("^", "**")
    if "[" in t or "]" in t:  # a piece of notation that was not translated
        raise ValueError(f"cannot translate {entry_text}")
    return parse_expr(t, local_dict=names)
```

The record also stores the diagonal entries one by one (`metricDiagonal`), in Mathematica notation with explicit `*` signs, for example `E^(2*a4[x4])*Sin[6*H*x8]^(1/3)`. `from_mathematica` translates such an entry with the same rules. If a square bracket is left, some notation was not translated, and the function stops with a `ValueError` instead of misreading it silently.

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
det_g = g.det()  # the product of the diagonal entries; sympy cancels exp(6 a4)
say(f"det g = {plain(det_g)}")
check(sp.simplify(det_g - sp.cos(6 * H * x8) ** 2) == 0,
      "det g = cos(z)^2: the function a4 drops out",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
             "check sqrt_abs_det_g")
```

`g.det()` is the determinant. It prints as `sin(z)**2*cot(z)**2`, the fourth line of the derivation of Section 3.6, and the check confirms that it equals $\cos^2 z$. The function $a_4$ is gone. The two strings of the `record=` argument are written next to each other, which Python joins into one string.

```python
volume_factor = sp.cos(6 * H * x8)  # sqrt|det g| on the patch, where cos z > 0
check(sp.simplify(from_mathematica(record["sqrtAbsDetG"]) - volume_factor) == 0,
      "sqrt|det g| = sin(z) cot(z) = cos(z)",
      record=f"{CURVATURE_RECORD}, sqrtAbsDetG")
```

The record writes the volume factor as `Sin[6*H*x8]*Cot[6*H*x8]`; translated and simplified, it equals $\cos z$.

```python
# numbers: sqrt(|det g|) at 7 points of the patch, compared with cos z
z_points = np.linspace(0.1, 1.5, 7)
det_numbers = np.array([float(det_g.subs({H: 1, x8: zp / 6})) for zp in z_points])
check(np.max(np.abs(np.sqrt(np.abs(det_numbers)) - np.cos(z_points))) < 1e-14,
      "sqrt|det g| equals cos z at 7 points of the patch")
```

A numerical check of the same fact. `np.linspace(0.1, 1.5, 7)` gives seven equally spaced values of $z$ from $0.1$ to $1.5$. For each, the exact determinant is evaluated with $H = 1$ and $x_8 = z/6$ (a dictionary in `subs` replaces several symbols at once) and turned into a floating-point number with `float`. The check requires $\sqrt{|\det g|}$ to differ from $\cos z$ by less than $10^{-14}$ at all seven points.

**In [8], the signature** (Section 3.5).

```python
ETA = np.array([1, 1, 1, -1, -1, -1, -1, 1])  # the flat metric diag(+,+,+,-,-,-,-,+)
diagonal_z = [plain(g[k, k]) for k in range(8)]  # the entries as functions of z, a4v
functions = [sp.lambdify((z, a4v), entry, "numpy") for entry in diagonal_z]
```

`ETA` holds the eight signs of $\eta$. `diagonal_z` holds the eight entries written with `z` and `a4v`. `sp.lambdify((z, a4v), entry, "numpy")` turns an exact expression into a fast numerical Python function of the two arguments that works on whole numpy arrays.

```python
def diagonal_values(z_values, a4_value):
    """The 8 diagonal entries at the points z_values (one row per entry)."""
    return np.array([np.broadcast_to(f(z_values, a4_value), z_values.shape)
                     for f in functions], dtype=float)
```

`diagonal_values` evaluates the eight functions at an array of values of $z$ for one value of $a_4$ and returns a table with eight rows. The entry $-1$ does not depend on $z$, so its function returns one number; `np.broadcast_to` repeats it so that every row has the same length as `z_values`.

```python
z_grid = np.linspace(0.0, np.pi / 2, 402)[1:-1]  # 400 points strictly inside
patterns = set()
for a4_value in np.linspace(-3.0, 3.0, 13):
    signs = np.sign(diagonal_values(z_grid, a4_value))  # +1 or -1 for each entry
    patterns.update(tuple(int(s) for s in column) for column in signs.T)
say(f"sign patterns found on the grid: {sorted(patterns)}")
check(patterns == {tuple(int(s) for s in ETA)},
      "on the whole grid the signs are (+,+,+,-,-,-,-,+): signature (4,4)")
```

`np.linspace(0.0, np.pi / 2, 402)` gives 402 points from $0$ to $\pi/2$; `[1:-1]` drops the first and the last, leaving 400 points strictly inside the patch. A `set` is a collection without repetitions. For 13 values of $a_4$ from $-3$ to $3$, `np.sign` replaces each entry by its sign; `signs.T` is the table turned on its side, so that each `column` holds the eight signs at one point; `tuple(...)` turns them into a fixed sequence that a set can store. At the end the set holds every sign pattern met anywhere on the grid. It is printed (sorted) and must be the single pattern of $\eta$. (The grid includes negative values of $a_4$ only to test the sign argument of Section 3.5, which holds for every real $a_4$.)

```python
step_x1 = diagonal_values(np.array([0.7]), 0.5)[0, 0]  # g11: step along x1
step_x5 = diagonal_values(np.array([0.7]), 0.5)[4, 0]  # g55: step along x5
say(f"at z = 0.7, a4 = 0.5: g11 = {step_x1:.6f} (space-like), "
    f"g55 = {step_x5:.6f} (time-like)")
check(step_x1 > 0 > step_x5, "a step along x1 is space-like, along x5 time-like")
```

At the single point $z = 0.7$, $a_4 = 0.5$: row 0 is $g_{11}$ and row 4 is $g_{55}$. The format `:.6f` prints six digits after the decimal point: $g_{11} = 2.347679$ and $g_{55} = -0.317724$. A unit step along $x_1$ has the squared length $g_{11} > 0$ (space-like), along $x_5$ the squared length $g_{55} < 0$ (time-like). Python reads `step_x1 > 0 > step_x5` as both comparisons at once.

**In [9], the colours and the heat map of the metric.**

```python
from matplotlib.colors import LinearSegmentedColormap

BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
MAGENTA, GREEN, VIOLET, RED = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
GREY = "#f0efec"  # the neutral middle of the two-sided colour scale
DIVERGING = LinearSegmentedColormap.from_list("blue_grey_red", [BLUE, GREY, RED])
LABELS = [f"$x_{k}$" for k in range(1, 9)]
```

Each colour is written as a **hex code**: `#` and three pairs of hexadecimal digits for the amounts of red, green and blue. The palette is chosen so that readers with a colour-vision deficiency can tell the colours apart; every figure also uses line styles and labels, so that it can be read in black and white. `DIVERGING` is a colour scale that runs from blue through grey to red; it will show negative numbers blue, zero grey and positive numbers red. `LABELS` holds the eight axis labels `$x_1$` to `$x_8$`, written in the math notation that matplotlib understands.

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
ax.set_title("The metric $g_{\\mu\\nu}$ at $z = \\pi/4$, $a_4 = 0.5$")
fig.colorbar(image, ax=ax, label="value of the entry (no unit)")
```

The double loop writes the value into each square: three decimals on the diagonal, a plain `0` elsewhere (`ha` and `va` centre the text). The two tick lines label the rows and the columns $x_1$ to $x_8$. In a Python string `\\` stands for one backslash, so the title reads $g_{\mu\nu}$ in math notation. `fig.colorbar` adds the colour scale with its label.

```python
save_figure(fig, "metric_heat_map",
            "The author's metric $g_{\\mu\\nu}$ at the point $z = 6Hx_8 = \\pi/4$ "
...
check(abs(values[0, 0] - np.e * np.sin(np.pi / 4) ** (1 / 3)) < 1e-12,
      "g11 at z = pi/4, a4 = 0.5 equals e times (sin pi/4)^(1/3)")
```

`save_figure` saves and shows the figure with its caption (printed in full under Figure 03a.1). The check compares the first diagonal entry with $e^{2 \cdot 0.5}(\sin\pi/4)^{1/3} = e\,(\sin\pi/4)^{1/3}$.

**What Figure 03a.1 shows.** An $8 \times 8$ table of coloured squares: only the diagonal is coloured. The three red squares of 3-space hold $2.422$, the time square $-1$, the three pale blue squares of the extra times $-0.328$, and the hidden square $\cot^2(\pi/4) = 1$. Four positive and four negative entries: the signature (4,4) at a glance. The 3-space entries are larger than the extra-time entries by the factor $e^{4a_4} = e^2$, because $a_4 = 0.5 > 0$ has already inflated 3-space and deflated the extra times.

**In [10], the diagonal entries across the patch.**

```python
z_line = np.linspace(0.02, np.pi / 2, 600)
entries = diagonal_values(z_line, 0.5)
fig, ax = plt.subplots()
ax.plot(z_line, entries[0], color=RED, lw=1.8,
        label="$g_{11} = g_{22} = g_{33} = e^{2a_4}\\sin^{1/3}z$")
ax.plot(z_line, entries[3], color=VIOLET, lw=1.8, ls="-.", label="$g_{44} = -1$")
ax.plot(z_line, entries[4], color=BLUE, lw=1.8, ls="--",
        label="$g_{55} = g_{66} = g_{77} = -e^{-2a_4}\\sin^{1/3}z$")
ax.plot(z_line, entries[7], color=AQUA, lw=1.8, label="$g_{88} = \\cot^2 z$")
ax.plot(z_line, np.cos(z_line) ** 2, color="black", lw=1.2, ls=":",
        label="$\\det g = \\cos^2 z$")
```

600 values of $z$ from $0.02$ to $\pi/2$ and the eight entries at $a_4 = 0.5$. `ax.plot(x, y, ...)` draws a curve; `lw` is the line width, `ls` the line style (a dash and a dot mean dash-dotted, two dashes mean dashed, a colon means dotted) and `label` its text in the legend. Equal entries are drawn once: row 0 for 3-space, row 3 for the time, row 4 for the extra times, row 7 for the hidden direction; the black dotted curve is $\det g = \cos^2 z$.

```python
ax.axhline(0.0, color="black", lw=0.8)
ax.axvline(np.pi / 2, color="grey", lw=0.8, ls=":")
ax.text(np.pi / 2 - 0.02, 3.3, "patch end", ha="right", fontsize=9)
ax.text(0.05, 3.3, "towards the tip", fontsize=9)
ax.set_ylim(-3.4, 3.6)  # room below the curves for the legend
ax.set_xlabel("$z = 6 H x_8$ (radians)")
ax.set_ylabel("entry of the metric (no unit)")
ax.set_title("The diagonal entries of the metric across the patch ($a_4 = 0.5$)")
ax.legend(fontsize=8, loc="lower center", ncol=2)
```

A horizontal line at $0$ (`axhline`), a vertical dotted line at the patch end (`axvline`), two labels written into the drawing (`ax.text(x, y, text)`), the range of the vertical axis, the two axis labels, the title and the legend in two columns at the bottom.

```python
save_figure(fig, "diagonal_entries",
            "The diagonal entries of the author's metric as functions of "
...
check(np.all(entries[7] > 0) and np.cos(np.pi / 2) ** 2 < 1e-30,
      "g88 > 0 inside the patch and det g = 0 at the patch end")
```

The figure is saved with its caption. The check: $g_{88} > 0$ at all 600 points, and $\cos^2(\pi/2)$ is zero up to rounding (the computer's $\cos(\pi/2)$ is about $6 \times 10^{-17}$, whose square is below $10^{-30}$).

**What Figure 03a.2 shows.** The red 3-space curve stays above zero and the blue extra-time curve and the violet time line stay below it across the whole patch: the signature never changes. The aqua curve $\cot^2 z$ rises steeply towards the tip and reaches $0$ at the patch end, where the black dotted determinant $\cos^2 z$ also reaches $0$: there the coordinate $x_8$ fails (Section 3.9). The 3-space entry falls towards the tip because the warp $\sin^{1/3}z$ goes to $0$ there.

**In [11], the vielbein** (Section 3.7).

```python
sixth = sp.sin(6 * H * x8) ** sp.Rational(1, 6)  # sin(z)^(1/6)
h = [sp.exp(a4) * sixth] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * sixth] * 3 \
    + [sp.cot(6 * H * x8)]
```

`sixth` is the warp factor $W = \sin^{1/6}z$. The list `h` holds the eight scale factors: `[...] * 3` repeats a one-element list three times, `+` joins lists, and a backslash at the end of a line continues the statement on the next line. `sp.Integer(1)` is the exact number $1$.

```python
for k in range(8):
    say(f"  h[x{k + 1}] = {plain(h[k])}")
check(all(sp.simplify(int(ETA[k]) * h[k] ** 2 - g[k, k]) == 0 for k in range(8)),
      "eta times h squared reproduces every diagonal entry of the metric",
      record="Revision/lead_checks/reports/emt-divergence-and-spin-connection.json, "
             "check vielbein_reproduces_metric")
```

The loop prints the eight scale factors (the output lists them; `exp(a4v)*sin(z)**(1/6)` is $e^{a_4}\sin^{1/6}z$). The check is $\eta_{kk}h_k^2 = g_{kk}$ for all eight $k$, the diagonal vielbein reproducing the metric, as in the lead's check.

**In [12], the expansion rates.**

```python
rates = [sp.simplify(sp.diff(sp.log(h[k]), x4)) for k in range(8)]
for k in range(8):
    say(f"  expansion rate of x{k + 1}: {plain(rates[k])}")
a4_prime = sp.Derivative(a4, x4)
check([sp.simplify(r - c * a4_prime) == 0 for r, c in
       zip(rates, [1, 1, 1, 0, -1, -1, -1, 0])] == [True] * 8,
      "3-space expands with rate a4p, the extra times shrink with rate -a4p")
```

`sp.diff(sp.log(h[k]), x4)` is $\partial_4 \ln h_k$, the rate of Section 3.7. The output prints `a4p` for 3-space, `-a4p` for the extra times and `0` for $x_4$ and $x_8$. `zip` pairs each rate with the expected coefficient ($1, 1, 1, 0, -1, -1, -1, 0$), and the check requires all eight differences to vanish.

```python
transverse = sp.simplify(h[0] * h[1] * h[2] * h[4] * h[5] * h[6])
say(f"product of the six transverse scale factors = {plain(transverse)}")
check(sp.simplify(transverse - sp.sin(6 * H * x8)) == 0,
      "the six transverse scale factors multiply to sin z, without a4")
```

The product of the six transverse scale factors (positions 0, 1, 2 and 4, 5, 6) prints as `sin(z)`: what 3-space gains, the extra times lose.

**In [13], the history of the Revision Kohn-Sham work** (Section 3.8).

```python
PARAMETERS = "Revision/kohn_sham/results/parameters.json"
parameters = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))
physics = parameters["physics"]
H_value, A_value = physics["H"], physics["historyA"]
slices = physics["slicesA4"]  # the values of a4 at which the solver works
L_tip = physics["L_tipCutoff"]  # the tip cut-off, in units of 1/H
say(f"H = {H_value}, A = {A_value}, slices a4 = {slices}, tip cut-off L = {L_tip}")
check(H_value == 1.0 and A_value == 1.0 and slices == [0.0, 0.5, 1.0, 1.5, 2.0],
      "the history of the record is a4 = x4 (A = 1, H = 1) with slices 0 to 2")
```

The record of the Revision Kohn-Sham solver is read, and from its part `physics` the constant $H$, the slope $A$, the five slices and the tip cut-off $L$. A line `a, b = c, d` gives two names at once. The output prints $H = 1$, $A = 1$, the slices $0, 0.5, 1, 1.5, 2$ and $L = 3$, and the check confirms them.

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

The theory record of the Kohn-Sham work is read and its statement about the status of the history is cut into sentences at every full stop followed by a blank. The first and the last sentence are printed (`sentences[-1]` is the last element of a list). The check requires the statement to start with PRESCRIBED BACKGROUND and to contain "not solved for": the record itself labels the history an assumption.

**In [14], the scale factors along the history.**

```python
x4_line = np.linspace(0.0, 2.5, 251)
a4_line = A_value * H_value * x4_line  # the history a4 = A H x4
slice_x4 = np.array(slices) / (A_value * H_value)  # the times of the slices
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
```

251 times from $0$ to $2.5$ (in units of $1/H$), the history $a_4 = AHx_4$ at those times, and the times $x_4 = a_4/(AH)$ of the five slices. `plt.subplots(1, 2, ...)` makes a figure with two drawing areas side by side, `axes[0]` and `axes[1]`.

```python
for ax, scale in zip(axes, ["linear", "log"]):
    ax.plot(x4_line, np.exp(a4_line), color=RED, lw=1.8,
            label="3-space: $e^{a_4}$ (inflates)")
    ax.plot(x4_line, np.exp(-a4_line), color=BLUE, lw=1.8, ls="--",
            label="extra times: $e^{-a_4}$ (deflate)")
    ax.plot(x4_line, np.exp(a4_line) * np.exp(-a4_line), color="black", lw=1.2,
            ls=":", label="product $= 1$")
    ax.plot(slice_x4, np.exp(slices), "o", color=RED, ms=6)
    ax.plot(slice_x4, np.exp(-np.array(slices)), "s", color=BLUE, ms=6)
    ax.set_yscale(scale)
    ax.set_xlabel("time $x_4$ (unit $1/H$)")
    ax.set_ylabel("scale factor relative to $x_4 = 0$")
```

The loop draws the same picture twice, once with an ordinary and once with a logarithmic vertical axis (`set_yscale`). In each: $e^{a_4}$ (red), $e^{-a_4}$ (blue dashed), their product (black dotted), and the five slices as dots (`"o"`) and squares (`"s"`) of size `ms=6`.

```python
axes[0].set_title("Ordinary vertical axis")
axes[1].set_title("Logarithmic vertical axis: straight lines")
axes[0].legend(fontsize=8)
save_figure(fig, "history_scale_factors",
            "The time dependence of the scale factors along the deflating history "
...
report("3-space growth factor at the last slice a4 = 2", f"{np.exp(2.0):.6f}")
report("extra-time shrink factor at the last slice a4 = 2", f"{np.exp(-2.0):.6f}")
check(abs(np.exp(slices[-1]) * np.exp(-slices[-1]) - 1.0) < 1e-15,
      "at every slice the two factors multiply to 1")
```

Titles, legend, the saved figure, two RESULT lines ($e^2 = 7.389056$ and $e^{-2} = 0.135335$) and a check that the two factors multiply to $1$ at the last slice (and so, since $e^{a}e^{-a} = 1$ for every $a$, at every slice).

**What Figure 03a.3 shows.** On the ordinary axis (left) the red curve of 3-space bends upwards to $7.39$ at $x_4 = 2$ and the blue extra-time curve falls towards $0$; on the logarithmic axis (right) both are straight lines, rising and falling with slopes $+1$ and $-1$: that is what exponential growth and exponential deflation look like. The product stays exactly $1$. The dots and squares mark the five slices on which the Revision Kohn-Sham states are computed.

**In [15], the functions of $z$.**

```python
z_line = np.linspace(0.005, np.pi / 2 - 0.005, 600)
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
axes[0].plot(z_line, np.sin(z_line) ** (1 / 6), color=RED, lw=1.8,
             label="warp factor $W = \\sin^{1/6} z$")
axes[0].plot(z_line, np.sin(z_line) ** (1 / 3), color=ORANGE, lw=1.8, ls="--",
             label="$W^2 = \\sin^{1/3} z$ (in the entries of $g$)")
axes[0].set_ylim(0.0, 1.05)
axes[0].set_title("The warp of the six transverse directions")
```

600 values strictly inside the patch. The left panel shows the warp factor $W = \sin^{1/6}z$ and its square $W^2 = \sin^{1/3}z$, which stands in the six transverse metric entries; the vertical axis runs from $0$ to $1.05$.

```python
axes[1].plot(z_line, 1 / np.tan(z_line), color=AQUA, lw=1.8,
             label="$\\cot z$ (scale factor of $x_8$)")
axes[1].plot(z_line, 1 / np.tan(z_line) ** 2, color=VIOLET, lw=1.8, ls="--",
             label="$\\cot^2 z$ (entry $g_{88}$)")
axes[1].set_yscale("log")
axes[1].set_title("The hidden direction (logarithmic axis)")
for ax in axes:
    ax.set_xlabel("$z = 6 H x_8$ (radians)")
    ax.set_ylabel("value (no unit)")
    ax.legend(fontsize=8)
```

The right panel shows $\cot z = 1/\tan z$ and $\cot^2 z$ on a logarithmic axis. The loop gives both panels their axis labels and legends.

```python
save_figure(fig, "hidden_direction",
            "The functions of the hidden coordinate $z = 6Hx_8$ in the author's "
...
check(abs(np.sin(np.pi / 2) ** (1 / 6) - 1.0) < 1e-15,
      "the warp factor equals 1 at the patch end z = pi/2")
```

The figure is saved; the check confirms $W = 1$ at the patch end.

**What Figure 03a.4 shows.** Left: both warp curves rise from $0$ at the tip to $1$ at the patch end; $W = \sin^{1/6}z$ rises very steeply near the tip (a sixth root of a small number is not small: $(10^{-6})^{1/6} = 0.1$). Right: $\cot z$ and $\cot^2 z$ fall over many powers of ten from the tip to the patch end, where they reach $0$ (off the bottom of the logarithmic axis).

**In [16], maps of the scale factors over time and $z$.**

```python
x4_grid, z_grid2 = np.meshgrid(np.linspace(0.0, 2.5, 251),
                               np.linspace(0.01, np.pi / 2, 200))
a4_grid = A_value * H_value * x4_grid
space_map = np.log10(np.exp(a4_grid) * np.sin(z_grid2) ** (1 / 6))
extra_map = np.log10(np.exp(-a4_grid) * np.sin(z_grid2) ** (1 / 6))
```

`np.meshgrid` makes two tables of the same shape (200 rows for $z$, 251 columns for $x_4$) that hold, at every grid point, its $x_4$ and its $z$. Along the history $a_4 = AHx_4$, the two maps hold the logarithm to base 10 of the scale factor of 3-space and of an extra time at every grid point.

```python
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
for ax, data, title in zip(axes, [space_map, extra_map],
                           ["3-space: $e^{a_4}\\sin^{1/6}z$",
                            "extra time: $e^{-a_4}\\sin^{1/6}z$"]):
    mesh = ax.pcolormesh(x4_grid, z_grid2, data, cmap=DIVERGING, vmin=-1.3,
                         vmax=1.3, shading="auto")
    ax.contour(x4_grid, z_grid2, data, levels=[0.0], colors="black",
               linewidths=1.0)
    ax.set_title(title)
    ax.set_xlabel("time $x_4$ (unit $1/H$)")
    ax.grid(False)
axes[0].set_ylabel("$z = 6 H x_8$ (radians)")
fig.colorbar(mesh, ax=axes, label="$\\log_{10}$ of the scale factor")
```

Two panels that share their vertical axis (`sharey=True`). `pcolormesh` colours every grid cell by its value on the blue-grey-red scale from $-1.3$ to $1.3$; `contour(..., levels=[0.0])` draws the black line on which the value is $0$, the factor $1$. One colour scale serves both panels.

```python
save_figure(fig, "scale_factor_maps",
            "Maps of the logarithm to base 10 of the scale factor of 3-space "
...
check(np.all(np.diff(space_map, axis=1) > 0) and np.all(np.diff(extra_map, axis=1) < 0),
      "along the history 3-space grows and the extra times shrink at every z")
```

`np.diff(..., axis=1)` is the difference between neighbouring columns, that is between successive times. The check: at every $z$, the 3-space map increases and the extra-time map decreases from each time to the next.

**What Figure 03a.5 shows.** Left: from left to right the colour turns from grey to deeper and deeper red: 3-space grows at every height $z$. The black line is the factor $1$; left of it, near the tip, the small warp makes the factor smaller than $1$ although $a_4 > 0$. Right: the colour deepens to blue from left to right: the extra times shrink at every $z$ at the same rate, and their scale factor is smallest near the tip, where the small warp makes it smaller still.

**In [17], proper volumes** (Section 3.6).

```python
V3 = sp.simplify(h[0] * h[1] * h[2])  # proper 3-volume of a unit coordinate box
Vt = sp.simplify(h[4] * h[5] * h[6])  # the same in the three extra times
V7 = sp.simplify(h[0] * h[1] * h[2] * h[4] * h[5] * h[6] * h[7])  # the 7-volume
say(f"V3 = {plain(V3)},  Vt = {plain(Vt)},  V7 density = {plain(V7)}")
check(sp.simplify(V7 - sp.cos(6 * H * x8)) == 0 and sp.diff(V7, x4) == 0,
      "the 7-volume density is cos z and does not change with the time x4")
```

The three products of scale factors of Section 3.6. The output: `exp(3*a4v)*sqrt(sin(z))`, `exp(-3*a4v)*sqrt(sin(z))` and `cos(z)`. The check: the 7-volume density is $\cos z$, and its derivative with respect to $x_4$ is zero.

```python
patch_volume = sp.integrate(sp.cos(6 * H * x8), (x8, 0, sp.pi / (12 * H)))
say(f"proper 7-volume of the patch per unit transverse coordinate volume = "
    f"{patch_volume}")
check(sp.simplify(patch_volume - 1 / (6 * H)) == 0,
      "the whole patch has the proper 7-volume 1/(6H) per unit coordinate volume")
```

`sp.integrate(f, (x8, 0, upper))` is the exact definite integral of Section 3.6; it prints `1/(6*H)`.

**In [18], the volumes along the history.**

```python
z_fixed = np.pi / 3
v3 = np.exp(3 * a4_line) * np.sin(z_fixed) ** 0.5
vt = np.exp(-3 * a4_line) * np.sin(z_fixed) ** 0.5
fig, ax = plt.subplots()
ax.plot(x4_line, v3, color=RED, lw=1.8, label="$V_3 = e^{3a_4}\\sin^{1/2}z$")
ax.plot(x4_line, vt, color=BLUE, lw=1.8, ls="--",
        label="$V_t = e^{-3a_4}\\sin^{1/2}z$")
ax.plot(x4_line, v3 * vt, color=ORANGE, lw=1.8, ls="-.",
        label="$V_3 V_t = \\sin z$")
ax.plot(x4_line, np.full_like(x4_line, np.cos(z_fixed)), color="black", lw=1.2,
        ls=":", label="7-volume density $\\cos z$")
```

At the fixed height $z = \pi/3$ ($\sin z = 0.866$, $\cos z = 0.5$) the numbers $V_3$ and $V_t$ along the history, their product, and the constant 7-volume density (`np.full_like` makes an array of the same length filled with one number).

```python
ax.set_yscale("log")
ax.set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$")
ax.set_ylabel("proper volume per unit coordinate volume")
ax.set_title("Proper volumes at $z = \\pi/3$")
ax.legend(fontsize=8)
save_figure(fig, "proper_volumes",
            "Proper volumes per unit coordinate volume at the fixed hidden position "
...
check(np.max(np.abs(v3 * vt - np.sin(z_fixed))) < 1e-12,
      "V3 times Vt stays equal to sin z along the history")
```

A logarithmic vertical axis, labels, title, legend, the saved figure and the check that $V_3V_t = \sin z$ at all 251 times.

**What Figure 03a.6 shows.** On the logarithmic axis $V_3$ is a straight line rising with slope $3$ (it grows like $e^{3x_4}$) and $V_t$ a straight line falling with slope $-3$; their product and the 7-volume density are flat lines. The inflation of 3-space is exactly compensated by the deflation of the extra times.

**In [19], the hidden coordinate $y$ and the warped form** (Section 3.9).

```python
geometry = ks_theory["geometry"]  # the statements of the record about the geometry
for key in ("hiddenCoordinate", "lineElement", "warp", "sqrtDetG"):
    say(f"record, {key}: {geometry[key]}")
```

Four statements of the record `ks-theory.json` are printed: the definition of $y$, the line element in $y$, the warp factor and the volume factor (the output shows them).

```python
y_of_x8 = sp.log(sp.sin(6 * H * x8)) / (6 * H)  # y = ln(sin z)/(6H)
dy_dx8 = sp.diff(y_of_x8, x8)  # the chain rule, done by sympy
say(f"dy/dx8 = {plain(dy_dx8)}")
check(sp.simplify(dy_dx8 - sp.cot(6 * H * x8)) == 0,
      "dy/dx8 = cot z",
      record="Revision/lead_checks/reports/emt-divergence-and-spin-connection.json, "
             "check ks_coordinate_jacobian")
check(sp.simplify(dy_dx8 ** 2 - g[7, 7]) == 0,
      "dy^2 = g88 dx8^2: y measures proper distance along x8")
check(sp.simplify(sp.exp(H * y_of_x8) - sixth) == 0,
      "the warp factor W = sin(z)^(1/6) equals e^(H y)")
```

$y$ as a function of $x_8$ and its derivative, which prints as `cos(z)/sin(z)`. Three checks: $dy/dx_8 = \cot z$ (the lead's check), $(dy/dx_8)^2 = g_{88}$, and $e^{Hy} = \sin^{1/6}z$.

```python
y = sp.symbols("y", real=True)  # the hidden coordinate as a symbol of its own
x8_of_y = sp.asin(sp.exp(6 * H * y)) / (6 * H)  # the inverse: sin z = e^(6 H y)
dx8_dy = sp.diff(x8_of_y, y)  # dx8/dy
g_y = sp.diag(*[g[k, k].subs(x8, x8_of_y) for k in range(7)],
              g[7, 7].subs(x8, x8_of_y) * dx8_dy ** 2)  # the metric in x1..x7, y
```

To write the metric in the coordinate $y$, the notebook needs $x_8$ as a function of $y$: from $\sin z = e^{6Hy}$, $x_8 = \arcsin(e^{6Hy})/(6H)$ (`sp.asin` is the inverse sine). The first seven entries only need this put in. The hidden entry becomes $g_{88}\,(dx_8/dy)^2$, because $dx_8 = (dx_8/dy)\,dy$ turns $g_{88}\,dx_8^2$ into $g_{88}(dx_8/dy)^2\,dy^2$. The star in `sp.diag(*[...], ...)` unpacks the list of seven entries into seven separate arguments.

```python
W = sp.exp(H * y)  # the warp factor in the coordinate y
warped = sp.diag(*([W ** 2 * sp.exp(2 * a4)] * 3 + [-1]
                   + [-W ** 2 * sp.exp(-2 * a4)] * 3 + [1]))  # the warped form
for k in (0, 3, 4, 7):
    say(f"  in the coordinate y: g[{k + 1}, {k + 1}] = {plain(g_y[k, k])}")
check((g_y - warped).applyfunc(sp.simplify) == sp.zeros(8, 8),
      "in the coordinate y the metric is the warped form with W = e^(H y)",
      record="Revision/kohn_sham/ks-theory.json, geometry.lineElement and "
             "geometry.warp")
```

`warped` is the warped form of Section 3.9 typed from the record, with $W = e^{Hy}$. Four entries of the transformed metric are printed: $e^{2a_4}e^{2Hy}$, $-1$, $-e^{-2a_4}e^{2Hy}$ and $1$. The check requires the transformed metric to equal the warped form entry by entry.

```python
check(sp.simplify(g_y.det() - sp.exp(12 * H * y)) == 0,
      "in the coordinate y the volume factor sqrt|det g| is e^(6 H y) = sin z",
      record="Revision/kohn_sham/ks-theory.json, geometry.sqrtDetG")
distance_to_end = -y_of_x8  # proper distance from the point to the patch end
check(sp.limit(distance_to_end, x8, 0, "+") == sp.oo,
      "the tip z -> 0 lies at an infinite proper distance (y -> minus infinity)")
```

The determinant in $y$ is $e^{12Hy}$, so the volume factor is $e^{6Hy}$ (the record's statement). Since $y$ measures proper distance and the patch end is $y = 0$, the proper distance from a point to the patch end is $-y$; `sp.limit(f, x8, 0, "+")` is the limit as $x_8$ tends to $0$ from above, and `sp.oo` is infinity: the tip is infinitely far away.

**In [20], the tip cut-off and the coordinate $y$ in pictures.**

```python
L_exact = sp.nsimplify(L_tip)  # the number 3.0 of the record as the exact integer 3
fraction = sp.integrate(sp.exp(6 * H * y), (y, -sp.oo, -L_exact / H)) \
    / sp.integrate(sp.exp(6 * H * y), (y, -sp.oo, 0))  # y: the symbol made above
fraction = sp.simplify(fraction.subs(H, 1))
report("fraction of the 7-volume beyond the tip cut-off y = -3", sp.sstr(fraction),
       f"= {float(fraction):.4e}")
z_cut = float(sp.asin(sp.exp(-18)))  # the angle z of the cut-off, sin z = e^(-18)
report("angle z of the tip cut-off", f"{z_cut:.4e}", "radians")
```

`sp.nsimplify(3.0)` gives the exact integer $3$. The fraction of Section 3.9 is computed as a ratio of two exact integrals and simplified with $H = 1$; it is `exp(-18)`, and the RESULT line prints it also as $1.5230 \times 10^{-8}$ (the format `.4e` writes four digits after the point and a power of ten). The angle of the cut-off, $\arcsin e^{-18}$, is $1.5230 \times 10^{-8}$ radians too, because $\arcsin u \approx u$ for small $u$.

```python
z_line = np.logspace(-10, np.log10(np.pi / 2), 800)  # 1e-10 ... pi/2, evenly in log
y_line = np.log(np.sin(z_line)) / 6.0  # with H = 1
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
axes[0].plot(z_line, y_line, color=VIOLET, lw=1.8, label="$y(z)$")
axes[0].axhline(-L_tip, color="black", lw=1.0, ls="--",
                label=f"tip cut-off $y = -L = -{L_tip:g}$")
axes[0].plot([z_cut], [-L_tip], "o", color="black", ms=6)
axes[0].set_xscale("log")
axes[0].set_xlabel("$z = 6 H x_8$ (radians, logarithmic axis)")
axes[0].set_ylabel("$y = \\ln(\\sin z)/(6H)$ (unit $1/H$)")
axes[0].set_title("The hidden coordinate $y$")
axes[0].legend(fontsize=8)
```

`np.logspace(-10, np.log10(np.pi / 2), 800)` gives 800 values of $z$ spread evenly on a logarithmic scale from $10^{-10}$ to $\pi/2$, so that the region near the tip is visible. The left panel draws $y(z)$ with $H = 1$, the cut-off line $y = -3$ (the format `:g` prints `3.0` as `3`) and a black dot at the cut-off, with a logarithmic horizontal axis.

```python
y_axis = np.linspace(-4.0, 0.0, 400)
axes[1].plot(y_axis, np.exp(y_axis), color=RED, lw=1.8,
             label="warp factor $W = e^{Hy} = \\sin^{1/6} z$")
axes[1].plot(y_axis, np.exp(2 * y_axis), color=ORANGE, lw=1.8, ls="-.",
             label="$W^2 = e^{2Hy} = \\sin^{1/3} z$")
axes[1].plot(y_axis, np.exp(6 * y_axis), color=AQUA, lw=1.8, ls="--",
             label="7-volume density $W^6 = e^{6Hy} = \\sin z$")
axes[1].axvspan(-4.0, -L_tip, color="grey", alpha=0.25,
                label="removed by the tip cut-off")
axes[1].set_xlabel("$y$ (unit $1/H$)")
axes[1].set_ylabel("value (no unit)")
axes[1].set_title("Warp and volume density in $y$")
axes[1].legend(fontsize=8, loc="upper left")
```

The right panel draws $W$, $W^2$ and $W^6$ as functions of $y$ from $-4$ to $0$, and shades (`axvspan`) the band beyond the cut-off.

```python
save_figure(fig, "hidden_coordinate_y",
            "The hidden coordinate $y = \\ln(\\sin z)/(6H)$ with $H = 1$. Left: $y$ "
...
check(fraction == sp.exp(-18), "the cut-off removes exactly the fraction e^(-18)")
```

The figure is saved, and the check confirms that the fraction is exactly $e^{-18}$.

**What Figure 03a.7 shows.** Left: on the logarithmic $z$ axis, $y$ is a straight line near the tip, because there $\sin z \approx z$ and $y \approx \ln(z)/6$; it bends over to $0$ at the patch end. The cut-off $y = -3$ sits at $z = 1.5 \times 10^{-8}$. Right: the warp factor and its powers fall towards $0$ as $y$ decreases; the volume density $e^{6y}$ is already tiny at $y = -1$, and the grey band beyond the cut-off holds only the fraction $e^{-18}$ of the 7-volume.

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

The names of the seven figures; `enumerate(figure_names, 1)` numbers them from 1, giving the file names `03a_1_metric_heat_map.png` to `03a_7_hidden_coordinate_y.png`. The check requires all seven files to exist, and `all_checks_passed()` prints the last line, ALL 29 CHECKS PASSED (notebook 03a). The 29 checks are: 1 in In [5], 2 in In [6], 3 in In [7], 2 in In [8], 1 each in In [9] and In [10], 1 in In [11], 2 in In [12], 2 in In [13], 1 each in In [14], In [15] and In [16], 2 in In [17], 1 in In [18], 6 in In [19], 1 in In [20] and 1 in In [21].

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

A tensor with several indices gets one term $+\Gamma$ for every upper index and one term $-\Gamma$ for every lower index (apply the same argument to products of vectors and covectors). For the metric:

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
K(a, b) = R^{ab}{}_{ab} \quad\text{(no sum)}
$$

is the **curvature of the coordinate plane** of $x_a$ and $x_b$ (its **sectional curvature**): positive for a plane curved like a sphere, negative for one curved like a saddle, zero for a flat one. By the two antisymmetries, $R^{ba}{}_{ba} = R^{ab}{}_{ab}$ and $R^{ab}{}_{ba} = R^{ba}{}_{ab} = -R^{ab}{}_{ab}$.

**Contractions.** The **Ricci tensor**, the **Ricci scalar**, the **Einstein tensor** and the **Kretschmann scalar** are

$$
R^a{}_b = \sum_c R^{ac}{}_{bc}, \qquad R = \sum_a R^a{}_a, \qquad G^a{}_b = R^a{}_b - \tfrac12\,\delta^a{}_b\,R, \qquad K = \sum_{a,b,c,d} R^{ab}{}_{cd}\,R^{cd}{}_{ab} .
$$

$R$ and $K$ have every index contracted: they are invariants, the same in every system of coordinates (Section 3.14). The Einstein tensor is the combination that enters Einstein's field equations (Section 3.26). Two consequences for the diagonal entries are used again and again:

$$
R^a{}_a = \sum_c R^{ac}{}_{ac} = \sum_{c \ne a} K(a, c)
$$

(the definition with $b = a$; the term $c = a$ is $R^{aa}{}_{aa} = 0$ by the antisymmetry in the upper pair): **each diagonal entry of the Ricci tensor is the sum of the curvatures of the $n - 1$ coordinate planes that contain that direction**; and

$$
R = \sum_a\sum_{c \ne a} K(a, c) = 2\sum_{a < c} K(a, c)
$$

(every plane is counted twice, once as $(a, c)$ and once as $(c, a)$, with $K(c, a) = K(a, c)$).

**A surface.** A space of two dimensions has a single coordinate plane, and its curvature $K(1, 2)$ is the **Gaussian curvature**. Then $R^1{}_1 = R^2{}_2 = K(1, 2)$ and $R = 2K(1, 2)$. The non-zero components $R^{ab}{}_{cd}$ are the four $R^{12}{}_{12} = R^{21}{}_{21} = K(1, 2)$ and $R^{12}{}_{21} = R^{21}{}_{12} = -K(1, 2)$, so the Kretschmann scalar is $K = 4K(1, 2)^2$ (each of the four products $R^{ab}{}_{cd}R^{cd}{}_{ab}$ is $K(1,2)^2$).

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
K(\theta, \varphi) = R^{\theta\varphi}{}_{\theta\varphi} = g^{\varphi\varphi}R^\theta{}_{\varphi\theta\varphi} = \frac{\sin^2\theta}{a^2\sin^2\theta} = \frac{1}{a^2}
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

(the chain rule: each derivative of $\cos(s/a)$ brings a factor $1/a$ and turns $\cos$ into $-\sin$ and $\sin$ into $\cos$). The distance shrinks, and it is zero at $s = \pi a/2$: the meridians meet at the pole. In general the distance $\xi(s)$ between two neighbouring geodesics of a surface obeys the **geodesic deviation equation** $d^2\xi/ds^2 = -\kappa\,\xi$ with the Gaussian curvature $\kappa$ (a standard theorem, quoted, ASSUMED; on the sphere we have just verified it, with $\kappa = 1/a^2$). Positive curvature focuses neighbouring geodesics, negative curvature drives them apart, zero curvature does neither. Notebook 03c solves the equation with RK4 and finds it equal to the exact distance of two meridians within $8.0 \times 10^{-14}$ (In [13]).

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
kappa = float(sphere_mixed[(0, 1, 0, 1)].subs(a, 1))  # the Gaussian curvature, a = 1
s_values, deviation_states = rk4(lambda s, y: np.array([y[1], -kappa * y[0]]),
                                 np.array([1.0, 0.0]), 0.0, np.pi / 2, 1000)
```

The Gaussian curvature computed in In [7], $1/a^2$, with $a = 1$, as a floating-point number. The deviation equation $\xi'' = -\kappa\xi$ of Section 3.18 as two first-order equations for $(\xi, \xi')$; `lambda s, y: ...` is a short function without a name that returns $(\xi', -\kappa\xi)$. RK4 solves it from $\xi = 1$, $\xi' = 0$ (start parallel, distance 1) over the length $\pi/2$ in 1000 steps.

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

Now the tools of Sections 3.15 to 3.17 are applied to the author's metric, by hand and completely. Throughout, $i$ stands for any of the three 3-space directions $x_1, x_2, x_3$, $j$ for any of the three extra times $x_5, x_6, x_7$, and $k$ for any of the six **transverse** directions ($i$ or $j$). The scale factors (Section 3.7) are $h_i = e^{a_4}\sin^{1/6}z$, $h_4 = 1$, $h_j = e^{-a_4}\sin^{1/6}z$, $h_8 = \cot z$, with the signs $\eta = (+,+,+,-,-,-,-,+)$.

**The logarithmic derivatives of the scale factors.** Only $x_4$ and $x_8$ appear in the metric, so only $\partial_4$ and $\partial_8$ can give something non-zero.

$$
\partial_4 \ln h_i = \partial_4\bigl(a_4 + \tfrac16\ln\sin z\bigr) = a_4', \qquad \partial_4 \ln h_j = \partial_4\bigl(-a_4 + \tfrac16\ln\sin z\bigr) = -a_4'
$$

(the logarithm of a product is the sum of the logarithms; $\ln e^{\pm a_4} = \pm a_4$; $z$ does not depend on $x_4$).

$$
\partial_8 \ln h_k = \tfrac16\,\frac{\cos z}{\sin z}\cdot 6H = H\cot z
$$

(for every transverse $k$, the part $\pm a_4$ does not depend on $x_8$; the chain rule with $dz/dx_8 = 6H$, Section 3.2).

$$
\partial_8 \ln h_8 = \frac{1}{\cot z}\cdot\Bigl(-\frac{1}{\sin^2 z}\Bigr)\cdot 6H = -\frac{\sin z}{\cos z}\cdot\frac{6H}{\sin^2 z} = -\frac{6H}{\sin z\cos z}
$$

(the derivative of $\ln u$ is $u'/u$; the derivative of $\cot z$ is $-1/\sin^2 z$; the chain rule). Since $1 = \sin^2 z + \cos^2 z$, $\frac{1}{\sin z\cos z} = \frac{\sin^2 z + \cos^2 z}{\sin z\cos z} = \tan z + \cot z$, so $\partial_8\ln h_8 = -6H(\tan z + \cot z)$. Finally $h_4 = 1$ gives $\partial_4\ln h_4 = \partial_8\ln h_4 = 0$, and $h_8$ does not depend on $x_4$.

**The four cases of Section 3.15.** Case (a), $\Gamma^a{}_{aa} = \partial_a\ln h_a$: only $a = 8$ gives a non-zero value,

$$
\Gamma^{x_8}{}_{x_8x_8} = -6H(\tan z + \cot z) = -\frac{6H}{\sin z\cos z} .
$$

Case (b), $\Gamma^a{}_{ab} = \Gamma^a{}_{ba} = \partial_b\ln h_a$ with $b \ne a$: with $b = x_4$,

$$
\Gamma^{x_i}{}_{x_ix_4} = a_4', \qquad \Gamma^{x_j}{}_{x_jx_4} = -a_4' ,
$$

and with $b = x_8$, for all six transverse directions,

$$
\Gamma^{x_k}{}_{x_kx_8} = H\cot z
$$

(the pairs $a = x_4$, $b = x_8$ and $a = x_8$, $b = x_4$ give zero, because $h_4$ is constant and $h_8$ does not depend on $x_4$). Case (c), $\Gamma^a{}_{bb} = -\eta_{aa}\eta_{bb}\,(h_b^2/h_a^2)\,\partial_a\ln h_b$ with $b \ne a$: it needs $\partial_a\ln h_b \ne 0$, so $a$ is $x_4$ or $x_8$. For $a = x_4$ ($\eta_{44} = -1$, $h_4 = 1$) it is $+\eta_{bb}\,h_b^2\,\partial_4\ln h_b$:

$$
\Gamma^{x_4}{}_{x_ix_i} = (+1)\,h_i^2\,a_4' = a_4'\,e^{2a_4}\sin^{1/3}z, \qquad \Gamma^{x_4}{}_{x_jx_j} = (-1)\,h_j^2\,(-a_4') = a_4'\,e^{-2a_4}\sin^{1/3}z
$$

(the two minus signs of the extra times, from $\eta_{jj}$ and from the deflation, multiply to $+1$). For $a = x_8$ ($\eta_{88} = +1$, $h_8^2 = \cot^2 z$) it is $-\eta_{bb}\,(h_b^2/\cot^2 z)\,H\cot z = -\eta_{bb}\,H\tan z\,h_b^2$:

$$
\Gamma^{x_8}{}_{x_ix_i} = -H\tan z\; e^{2a_4}\sin^{1/3}z, \qquad \Gamma^{x_8}{}_{x_jx_j} = +H\tan z\; e^{-2a_4}\sin^{1/3}z
$$

($\cot z/\cot^2 z = 1/\cot z = \tan z$). Case (d) gives only zeros.

**The complete list.** Counting both orders of the lower indices: case (a) 1 symbol; case (b) $2 \times 6$ with $x_4$ and $2 \times 6$ with $x_8$; case (c) 6 with upper $x_4$ and 6 with upper $x_8$: $1 + 12 + 12 + 6 + 6 = 37$ non-zero symbols of the $8^3 = 512$. With the lower indices ordered ($b \le c$) there are $1 + 6 + 6 + 6 + 6 = 25$:

| symbol ($b \le c$) | value | how many |
| --- | --- | --- |
| $\Gamma^{x_i}{}_{x_ix_4}$, $i = 1, 2, 3$ | $a_4'$ | 3 |
| $\Gamma^{x_j}{}_{x_4x_j}$, $j = 5, 6, 7$ | $-a_4'$ | 3 |
| $\Gamma^{x_k}{}_{x_kx_8}$, $k = 1, 2, 3, 5, 6, 7$ | $H\cot z$ | 6 |
| $\Gamma^{x_4}{}_{x_ix_i}$ | $a_4'\,e^{2a_4}\sin^{1/3}z$ | 3 |
| $\Gamma^{x_4}{}_{x_jx_j}$ | $a_4'\,e^{-2a_4}\sin^{1/3}z$ | 3 |
| $\Gamma^{x_8}{}_{x_ix_i}$ | $-H\tan z\,e^{2a_4}\sin^{1/3}z$ | 3 |
| $\Gamma^{x_8}{}_{x_jx_j}$ | $H\tan z\,e^{-2a_4}\sin^{1/3}z$ | 3 |
| $\Gamma^{x_8}{}_{x_8x_8}$ | $-6H(\tan z + \cot z)$ | 1 |

This is exactly the list `christoffelNonzero_b_le_c` of the record `Revision/gkd_lovelock/results/curvature.json` (PROVED here by hand; Notebook 03b reproduces it symbol by symbol, In [7]; the independent verification of the record agrees, `python-lovelock-report.json`, check `rust_christoffels_agree`). The record writes $\tan z$ as `Cot[6*H*x8]^(-1)`. Every symbol has at least one index $x_4$ or $x_8$, the two coordinates on which the metric depends. The deflation is visible in the second row: the extra-time symbols $\Gamma^{x_j}{}_{x_4x_j} = -a_4'$ have the opposite sign of the 3-space ones.

**Observers at rest fall freely.** No symbol has the lower pair $(x_4, x_4)$: case (a) with $a = x_4$ is $\partial_4\ln h_4 = 0$, and case (c) with $b = x_4$ contains $\partial_a\ln h_4 = 0$. So $\Gamma^a{}_{x_4x_4} = 0$ for every $a$. An observer who keeps $x_1, x_2, x_3, x_5, x_6, x_7, x_8$ fixed while $x_4 = \tau$ runs has $u^a = dx^a/d\tau = 1$ for $a = x_4$ and $0$ otherwise, and $du^a/d\tau = 0$; the geodesic equation of Section 3.16 reads $0 + \Gamma^a{}_{x_4x_4}\cdot1\cdot1 = 0$, which holds. The squared speed is $g(u, u) = g_{44} = -1$, so $\tau = x_4$ is the observer's proper time. **Observers at rest are in free fall, and their clocks show $x_4$** (PROVED; Notebook 03b, In [12]).

**The contracted symbols.** By Section 3.15, $\sum_a\Gamma^a{}_{ab} = \partial_b\ln\sqrt{|\det g|} = \partial_b\ln\cos z$. Check with the list: for $b = x_4$, $\sum_a\Gamma^a{}_{a4} = 3a_4' + 3(-a_4') = 0$, and $\partial_4\ln\cos z = 0$; for $b = x_8$, $\sum_a\Gamma^a{}_{a8} = 6H\cot z - 6H(\tan z + \cot z) = -6H\tan z$, and $\partial_8\ln\cos z = -\frac{\sin z}{\cos z}\cdot 6H = -6H\tan z$. Both agree (Notebook 03b, In [12]). Once more the three inflating and the three deflating directions cancel in the $x_4$ sum.

### 3.24 The curvature of the author's metric, by hand

**The curvature of every coordinate plane.** For a diagonal metric, Section 3.17 gives $K(a, b) = R^{ab}{}_{ab} = g^{bb}R^a{}_{bab}$ (no sum), with

$$
R^a{}_{bab} = \partial_a\Gamma^a{}_{bb} - \partial_b\Gamma^a{}_{ba} + \sum_e\bigl(\Gamma^a{}_{ae}\Gamma^e{}_{bb} - \Gamma^a{}_{be}\Gamma^e{}_{ba}\bigr)
$$

(the formula of Section 3.17 with $c = a$ and $d = b$). The 28 coordinate planes fall into seven kinds. We compute each kind once, with general labels, so that the computation holds for every plane of that kind. Two facts from the list of Section 3.23 are used again and again: a derivative $\partial_i$, $\partial_j$ of anything is zero (nothing depends on the transverse coordinates), and the only non-zero symbols with the upper index $x_k$ are $\Gamma^{x_k}{}_{x_kx_4}$, $\Gamma^{x_k}{}_{x_4x_k}$, $\Gamma^{x_k}{}_{x_kx_8}$ and $\Gamma^{x_k}{}_{x_8x_k}$.

(1) Two different 3-space directions $i$ and $i'$ (3 planes):

$$
R^i{}_{i'ii'} = 0 - 0 + \Gamma^i{}_{i4}\Gamma^4{}_{i'i'} + \Gamma^i{}_{i8}\Gamma^8{}_{i'i'} - 0 = a_4'\cdot a_4'h_{i'}^2 + H\cot z\cdot\bigl(-H\tan z\,h_{i'}^2\bigr) = (a_4'^2 - H^2)\,h_{i'}^2
$$

($\Gamma^i{}_{i'i'} = \Gamma^i{}_{i'i} = 0$ because $i' \ne i$; in $\sum_e\Gamma^i{}_{ie}\Gamma^e{}_{i'i'}$ only $e = x_4$ and $e = x_8$ survive; every $\Gamma^i{}_{i'e}$ is zero; $\cot z\tan z = 1$), so $K(i, i') = g^{i'i'}(a_4'^2 - H^2)h_{i'}^2 = a_4'^2 - H^2$ (with $g^{i'i'} = 1/h_{i'}^2$).

(2) Two different extra times $j$ and $j'$ (3 planes):

$$
R^j{}_{j'jj'} = \Gamma^j{}_{j4}\Gamma^4{}_{j'j'} + \Gamma^j{}_{j8}\Gamma^8{}_{j'j'} = (-a_4')\cdot a_4'h_{j'}^2 + H\cot z\cdot H\tan z\,h_{j'}^2 = (H^2 - a_4'^2)\,h_{j'}^2
$$

($\Gamma^j{}_{j'j'} = \Gamma^j{}_{j'j} = 0$ because $j' \ne j$, so both derivative terms vanish; in $\sum_e\Gamma^j{}_{je}\Gamma^e{}_{j'j'}$ only $e = x_4$ and $e = x_8$ survive; every $\Gamma^j{}_{j'e}$ is zero; $\cot z\tan z = 1$), so $K(j, j') = g^{j'j'}(H^2 - a_4'^2)h_{j'}^2 = a_4'^2 - H^2$ (with $g^{j'j'} = -1/h_{j'}^2$).

(3) A 3-space direction $i$ and an extra time $j$ (9 planes):

$$
R^i{}_{jij} = \Gamma^i{}_{i4}\Gamma^4{}_{jj} + \Gamma^i{}_{i8}\Gamma^8{}_{jj} = a_4'\cdot a_4'h_j^2 + H\cot z\cdot H\tan z\,h_j^2 = (a_4'^2 + H^2)\,h_j^2 ,
$$

($\Gamma^i{}_{jj} = \Gamma^i{}_{ji} = 0$, so both derivative terms vanish; in $\sum_e\Gamma^i{}_{ie}\Gamma^e{}_{jj}$ only $e = x_4$ and $e = x_8$ survive; every $\Gamma^i{}_{je}$ is zero; $\cot z\tan z = 1$), so $K(i, j) = g^{jj}(a_4'^2 + H^2)h_j^2 = -(a_4'^2 + H^2)$ (with $g^{jj} = -1/h_j^2$).

(4) A 3-space direction $i$ and the time $x_4$ (3 planes):

$$
R^i{}_{4i4} = \partial_i\Gamma^i{}_{44} - \partial_4\Gamma^i{}_{4i} + \sum_e\Gamma^i{}_{ie}\Gamma^e{}_{44} - \sum_e\Gamma^i{}_{4e}\Gamma^e{}_{4i} = 0 - a_4'' + 0 - (a_4')^2
$$

($\partial_i$ gives zero; $\partial_4 a_4' = a_4''$; every $\Gamma^e{}_{44}$ is zero, Section 3.23; in the last sum only $e = i$ survives), so $K(i, 4) = g^{44}\bigl(-a_4'' - a_4'^2\bigr) = a_4'^2 + a_4''$ (with $g^{44} = -1$).

(5) An extra time $j$ and the time $x_4$ (3 planes):

$$
R^j{}_{4j4} = -\partial_4\Gamma^j{}_{4j} - (\Gamma^j{}_{4j})^2 = -\partial_4(-a_4') - (-a_4')^2 = a_4'' - a_4'^2
$$

(the formula with $a = j$, $b = x_4$: $\partial_j\Gamma^j{}_{44} = 0$; every $\Gamma^e{}_{44}$ is zero; in the last sum only $e = j$ survives; $\partial_4(-a_4') = -a_4''$), so $K(j, 4) = g^{44}(a_4'' - a_4'^2) = a_4'^2 - a_4''$ (with $g^{44} = -1$).

(6) A transverse direction $k$ and the hidden direction $x_8$ (6 planes):

$$
R^k{}_{8k8} = \partial_k\Gamma^k{}_{88} - \partial_8\Gamma^k{}_{8k} + \Gamma^k{}_{k8}\Gamma^8{}_{88} - \Gamma^k{}_{8k}\Gamma^k{}_{8k}
$$

(in $\sum_e\Gamma^k{}_{ke}\Gamma^e{}_{88}$ only $e = x_8$ survives, because $\Gamma^e{}_{88}$ is non-zero only for $e = x_8$; in $\sum_e\Gamma^k{}_{8e}\Gamma^e{}_{8k}$ only $e = k$)

$$
= 0 + \frac{6H^2}{\sin^2 z} + H\cot z\cdot\bigl(-6H(\tan z + \cot z)\bigr) - H^2\cot^2 z = \frac{6H^2}{\sin^2 z} - 6H^2(1 + \cot^2 z) - H^2\cot^2 z
$$

($\partial_8(H\cot z) = H\cdot(-1/\sin^2 z)\cdot 6H$, so $-\partial_8\Gamma^k{}_{8k} = +6H^2/\sin^2 z$; $\cot z\tan z = 1$)

$$
= -H^2\cot^2 z
$$

($1 + \cot^2 z = (\sin^2 z + \cos^2 z)/\sin^2 z = 1/\sin^2 z$, so the first two terms cancel). Hence $K(k, 8) = g^{88}(-H^2\cot^2 z) = \tan^2 z\cdot(-H^2\cot^2 z) = -H^2$.

(7) The time $x_4$ and the hidden direction $x_8$ (1 plane):

$$
R^4{}_{848} = \partial_4\Gamma^4{}_{88} - \partial_8\Gamma^4{}_{84} + \sum_e\Gamma^4{}_{4e}\Gamma^e{}_{88} - \sum_e\Gamma^4{}_{8e}\Gamma^e{}_{84} = 0
$$

(the only non-zero symbols with upper index $x_4$ are $\Gamma^4{}_{kk}$, and none of $\Gamma^4{}_{88}$, $\Gamma^4{}_{84}$, $\Gamma^4{}_{4e}$, $\Gamma^4{}_{8e}$ is of that form), so $K(4, 8) = 0$: this plane is flat.

**The table of the plane curvatures** (PROVED; Notebook 03b computes all 28 and finds these six formulas, In [16]):

| plane | how many | curvature $K(a, b) = R^{ab}{}_{ab}$ |
| --- | --- | --- |
| two 3-space directions | 3 | $a_4'^2 - H^2$ |
| two extra times | 3 | $a_4'^2 - H^2$ |
| a 3-space direction and an extra time | 9 | $-(a_4'^2 + H^2)$ |
| a 3-space direction and the time $x_4$ | 3 | $a_4'^2 + a_4''$ |
| an extra time and the time $x_4$ | 3 | $a_4'^2 - a_4''$ |
| a transverse direction and the hidden $x_8$ | 6 | $-H^2$ |
| the time $x_4$ and the hidden $x_8$ | 1 | $0$ |

None depends on $z$ or on the value of $a_4$; only $H$, the rate $a_4'$ and $a_4''$ appear. Along the history $a_4 = AHx_4$ ($a_4' = AH$, $a_4'' = 0$) the planes inside 3-space and inside the extra times have $H^2(A^2 - 1)$: negative (saddle-like) for $A < 1$, zero for the canonical $A = 1$, positive for $A > 1$. The planes that mix 3-space and the extra times are always saddle-like, $-H^2(A^2 + 1)$.

**The components that are not plane curvatures.** Each plane with $K \ne 0$ gives four non-zero components, $R^{ab}{}_{ab} = R^{ba}{}_{ba} = K(a, b)$ and $R^{ab}{}_{ba} = R^{ba}{}_{ab} = -K(a, b)$ (Section 3.17): $27 \times 4 = 108$ components. The other non-zero components connect the planes $(x_4, x_k)$ and $(x_8, x_k)$. First

$$
R^4{}_{k8k} = \partial_8\Gamma^4{}_{kk} - \partial_k\Gamma^4{}_{k8} + \sum_e\Gamma^4{}_{8e}\Gamma^e{}_{kk} - \sum_e\Gamma^4{}_{ke}\Gamma^e{}_{k8} = \partial_8\Gamma^4{}_{kk} - \Gamma^4{}_{kk}\Gamma^k{}_{k8}
$$

(the formula with $a = x_4$, $b = k$, $c = x_8$, $d = k$; $\Gamma^4{}_{k8} = 0$ and every $\Gamma^4{}_{8e} = 0$; in the last sum only $e = k$). With $\Gamma^4{}_{kk} = a_4'h_k^2$ for both kinds of $k$ (Section 3.23) and $\partial_8 h_k^2 = 2H\cot z\,h_k^2$ (twice the logarithmic derivative),

$$
R^4{}_{k8k} = 2a_4'H\cot z\,h_k^2 - a_4'h_k^2\,H\cot z = a_4'H\cot z\,h_k^2 ,
$$

and raising the second index, $R^{4k}{}_{8k} = g^{kk}R^4{}_{k8k}$:

$$
R^{4i}{}_{8i} = +Ha_4'\cot z, \qquad R^{4j}{}_{8j} = -Ha_4'\cot z
$$

(with $g^{ii} = +1/h_i^2$ and $g^{jj} = -1/h_j^2$). Next, the components with the upper index $x_8$:

$$
R^8{}_{k4k} = \partial_4\Gamma^8{}_{kk} - \partial_k\Gamma^8{}_{k4} + \sum_e\Gamma^8{}_{4e}\Gamma^e{}_{kk} - \sum_e\Gamma^8{}_{ke}\Gamma^e{}_{k4} = \partial_4\Gamma^8{}_{kk} - \Gamma^8{}_{kk}\Gamma^k{}_{k4}
$$

(the formula with $a = x_8$, $b = k$, $c = x_4$, $d = k$; $\Gamma^8{}_{k4} = 0$, every $\Gamma^8{}_{4e} = 0$; in the last sum only $e = k$). For $k = i$: $\Gamma^8{}_{ii} = -H\tan z\,h_i^2$ with $\partial_4 h_i^2 = 2a_4'h_i^2$, so $R^8{}_{i4i} = -2Ha_4'\tan z\,h_i^2 + H\tan z\,h_i^2\,a_4' = -Ha_4'\tan z\,h_i^2$ and $R^{8i}{}_{4i} = -Ha_4'\tan z$. For $k = j$: $\Gamma^8{}_{jj} = +H\tan z\,h_j^2$ with $\partial_4 h_j^2 = -2a_4'h_j^2$ and $\Gamma^j{}_{j4} = -a_4'$, so $R^8{}_{j4j} = -2Ha_4'\tan z\,h_j^2 + H\tan z\,h_j^2\,a_4' = -Ha_4'\tan z\,h_j^2$ and $R^{8j}{}_{4j} = g^{jj}R^8{}_{j4j} = +Ha_4'\tan z$. For each of the six transverse $k$, the antisymmetries give four components of each of these two kinds: $6 \times 8 = 48$ components, all of size $Ha_4'\cot z$ or $Ha_4'\tan z$. Together $108 + 48 = 156$, exactly the number of non-zero components $R^{ab}{}_{cd}$ that the Rust program of the record and Notebook 03b find (`Revision/gkd_lovelock/results/lovelock-report.json`, check `riemann_antisymmetry`: "156 nonzero entries"); so the list is complete. These 48 components depend on $z$, and they grow without bound at one end of the patch or the other. This is an effect of the coordinate $x_8$, not of the geometry. Measured with the rulers and clocks of the frame of Section 3.7, an upper index $a$ is multiplied by its scale factor $h_a$ (a step $dx^a$ has the proper length $h_a\,dx^a$), and a lower index is divided by it (so that a contraction keeps its value, Section 3.14). The frame component of $R^{4k}{}_{8k}$ is therefore $\frac{h_4h_k}{h_8h_k}R^{4k}{}_{8k} = \tan z\cdot(\pm Ha_4'\cot z) = \pm Ha_4'$, and that of $R^{8k}{}_{4k}$ is $\cot z\cdot(\mp Ha_4'\tan z) = \mp Ha_4'$: constants. The plane curvatures keep their values, because there the factors cancel.

**Where the deflation shows.** Two of the seven kinds of plane differ between 3-space and the extra times only through the sign of $a_4''$, and in the 48 components the 3-space and the extra-time members have opposite signs. The next section shows that these opposite signs make the Ricci tensor diagonal.

### 3.25 Ricci, Einstein and Kretschmann of the author's metric; the contracted Bianchi identity

**The diagonal of the Ricci tensor.** By Section 3.17, $R^a{}_a$ is the sum of the curvatures of the seven planes that contain $x_a$. From the table of Section 3.24:

$$
R^i{}_i = 2(a_4'^2 - H^2) - 3(a_4'^2 + H^2) + (a_4'^2 + a_4'') - H^2 = a_4'' - 6H^2
$$

(two planes with the other 3-space directions, three with the extra times, one with $x_4$, one with $x_8$; then collect: $2 - 3 + 1 = 0$ times $a_4'^2$, and $-2 - 3 - 1 = -6$ times $H^2$);

$$
R^4{}_4 = 3(a_4'^2 + a_4'') + 3(a_4'^2 - a_4'') + 0 = 6a_4'^2
$$

(three planes with 3-space, three with the extra times, one with $x_8$; the terms $\pm 3a_4''$ cancel);

$$
R^j{}_j = -3(a_4'^2 + H^2) + 2(a_4'^2 - H^2) + (a_4'^2 - a_4'') - H^2 = -a_4'' - 6H^2
$$

(three planes with 3-space, two with the other extra times, one with $x_4$, one with $x_8$);

$$
R^8{}_8 = 6\cdot(-H^2) + 0 = -6H^2
$$

(six planes with the transverse directions, one with $x_4$). The Ricci scalar is the sum of the diagonal:

$$
R = 3(a_4'' - 6H^2) + 6a_4'^2 + 3(-a_4'' - 6H^2) - 6H^2 = 6a_4'^2 - 42H^2
$$

($3a_4'' - 3a_4'' = 0$ and $-18 - 18 - 6 = -42$).

**The Ricci tensor has no entry off the diagonal.** An entry $R^a{}_b = \sum_c R^{ac}{}_{bc}$ with $a \ne b$ needs a non-zero component whose upper pair $(a, c)$ and lower pair $(b, c)$ differ in one index. The 108 plane components have the same two indices up and down, so they give nothing. The 48 others have the pairs $\{x_4, x_k\}$ and $\{x_8, x_k\}$, so the only candidates are $R^4{}_8$ and $R^8{}_4$:

$$
\begin{aligned}
R^4{}_8 &= \sum_i R^{4i}{}_{8i} + \sum_j R^{4j}{}_{8j} = 3Ha_4'\cot z - 3Ha_4'\cot z = 0,\\
R^8{}_4 &= \sum_i R^{8i}{}_{4i} + \sum_j R^{8j}{}_{4j} = -3Ha_4'\tan z + 3Ha_4'\tan z = 0
\end{aligned}
$$

(Section 3.24; the terms $c = x_4$ and $c = x_8$ vanish by the antisymmetries). The three inflating and the three deflating directions cancel exactly. If the extra times inflated instead, $g_{jj} = -e^{2a_4}\sin^{1/3}z$, the symbol $\Gamma^4{}_{jj}$ would change sign, the extra-time terms would have the same sign as the 3-space terms, and $R^4{}_8$ would be $6Ha_4'\cot z \ne 0$: Notebook 03b computes exactly this negative control (In [27]) and finds $G^{x_4}{}_{x_8} = 6Ha_4'\cot z$ and $G^{x_8}{}_{x_4} = -6Ha_4'\tan z$.

**The Einstein tensor.** $G^a{}_b = R^a{}_b - \tfrac12\delta^a{}_bR$, with $\tfrac12 R = 3a_4'^2 - 21H^2$:

$$
G^i{}_i = a_4'' - 3a_4'^2 + 15H^2, \qquad G^4{}_4 = 3a_4'^2 + 21H^2, \qquad G^j{}_j = -a_4'' - 3a_4'^2 + 15H^2, \qquad G^8{}_8 = 15H^2 - 3a_4'^2
$$

(each diagonal entry of the Ricci tensor minus $3a_4'^2 - 21H^2$), and every entry off the diagonal is zero. These are exactly the entries `ricciMixed`, `ricciScalar` and `einsteinMixed` of `Revision/gkd_lovelock/results/curvature.json` (PROVED here; Notebook 03b reproduces all 64 + 64 + 1 of them, In [17]; record check `rust_ricci_einstein_scalar_agree` of `python-lovelock-report.json`). The lead's independent check states the same properties (`Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`, checks `einstein_off_diagonal_zero`, `einstein_x8_independent`, `einstein_isotropy`): $G$ is diagonal, no entry depends on $x_8$, and the three 3-space entries are equal, as are the three extra-time entries. Moreover

$$
G^4{}_4 - G^8{}_8 = 3a_4'^2 + 21H^2 - 15H^2 + 3a_4'^2 = 6\bigl(a_4'^2 + H^2\bigr) > 0 \quad\text{for } H > 0
$$

(record check `no_vacuum_for_H_positive`), a fact used in Section 3.26.

**The Kretschmann scalar.** In $K = \sum R^{ab}{}_{cd}R^{cd}{}_{ab}$ each component is multiplied by its partner with the two pairs exchanged. The four components of a plane are their own partners or each other's, and each of the four products is $K(a, b)^2$ (Section 3.17), so the planes contribute $4\sum_{\text{planes}}K(a, b)^2$. Each of the 48 other components is paired with one of the other kind, for example $R^{4i}{}_{8i}R^{8i}{}_{4i} = (Ha_4'\cot z)(-Ha_4'\tan z) = -H^2a_4'^2$; the sign changes of the antisymmetries act on both factors, and for an extra time both factors change sign, so all 48 products equal $-H^2a_4'^2$. The sum over the planes is

$$
\sum K^2 = 6(a_4'^2 - H^2)^2 + 9(a_4'^2 + H^2)^2 + 3(a_4'^2 + a_4'')^2 + 3(a_4'^2 - a_4'')^2 + 6H^4
$$

(the table of Section 3.24)

$$
= \bigl(6a_4'^4 - 12a_4'^2H^2 + 6H^4\bigr) + \bigl(9a_4'^4 + 18a_4'^2H^2 + 9H^4\bigr) + \bigl(6a_4'^4 + 6a_4''^2\bigr) + 6H^4 = 21a_4'^4 + 6a_4'^2H^2 + 21H^4 + 6a_4''^2
$$

(the squares expanded; in $3(p + q)^2 + 3(p - q)^2 = 6p^2 + 6q^2$ the mixed terms cancel). Therefore

$$
K = 4\bigl(21a_4'^4 + 6a_4'^2H^2 + 21H^4 + 6a_4''^2\bigr) - 48H^2a_4'^2 = 12\bigl(7H^4 - 2H^2a_4'^2 + 7a_4'^4 + 2a_4''^2\bigr)
$$

($24 - 48 = -24$ times $a_4'^2H^2$; then $12$ taken out). Although 48 components depend on $z$ and grow without bound at the ends of the patch, the invariant $K$ does not depend on $z$: in every product $\cot z$ meets $\tan z$. Completing the square,

$$
\frac{K}{12} = 7\Bigl(a_4'^2 - \frac{H^2}{7}\Bigr)^2 + \frac{48}{7}H^4 + 2a_4''^2
$$

(expand: $7a_4'^4 - 2H^2a_4'^2 + H^4/7$, and $H^4/7 + 48H^4/7 = 7H^4$), so $K \ge \frac{576}{7}H^4 > 0$ for every history: **the author's metric is curved everywhere, for every function $a_4(x_4)$ and every $H > 0$** (PROVED; Notebook 03b checks the formula and computes $K$ a second time from the 156 components of the record, In [22]). Along the history $a_4 = AHx_4$: $R = 6H^2(A^2 - 7)$ and $K = 12H^4(7A^4 - 2A^2 + 7)$; for the canonical $A = 1$, $R = -36H^2$ and $K = 144H^4$.

**The contracted Bianchi identity.** For every metric the Einstein tensor has zero divergence, $\nabla_\mu G^\mu{}_\nu = 0$ (a standard theorem, the **contracted Bianchi identity**; quoted, ASSUMED in general). For the author's metric we prove it directly. By the rule of Section 3.15 (one $+\Gamma$ for the upper index, one $-\Gamma$ for the lower one, then the upper index contracted with the derivative),

$$
\nabla_\mu G^\mu{}_\nu = \sum_\mu\partial_\mu G^\mu{}_\nu + \sum_{\mu,\lambda}\Gamma^\mu{}_{\mu\lambda}G^\lambda{}_\nu - \sum_{\mu,\lambda}\Gamma^\lambda{}_{\mu\nu}G^\mu{}_\lambda .
$$

For a diagonal $G$ the first sum keeps $\mu = \nu$, the second $\lambda = \nu$ and the third $\lambda = \mu$:

$$
\nabla_\mu G^\mu{}_\nu = \partial_\nu G^\nu{}_\nu + \sum_\mu\Gamma^\mu{}_{\mu\nu}\bigl(G^\nu{}_\nu - G^\mu{}_\mu\bigr) \quad\text{(no sum over } \nu).
$$

For $\nu = x_4$: $\partial_4 G^4{}_4 = \partial_4(3a_4'^2 + 21H^2) = 6a_4'a_4''$ (the chain rule), and the sum has $\Gamma^i{}_{i4} = a_4'$ and $\Gamma^j{}_{j4} = -a_4'$:

$$
\nabla_\mu G^\mu{}_4 = 6a_4'a_4'' + 3a_4'\bigl(G^4{}_4 - G^i{}_i\bigr) - 3a_4'\bigl(G^4{}_4 - G^j{}_j\bigr) = 6a_4'a_4'' + 3a_4'\bigl(G^j{}_j - G^i{}_i\bigr) = 6a_4'a_4'' + 3a_4'(-2a_4'') = 0 .
$$

For $\nu = x_8$: $\partial_8 G^8{}_8 = 0$, and the sum has $\Gamma^k{}_{k8} = H\cot z$ for the six transverse $k$ (the term $\mu = x_8$ has the factor $G^8{}_8 - G^8{}_8 = 0$):

$$
\nabla_\mu G^\mu{}_8 = H\cot z\bigl[3(G^8{}_8 - G^i{}_i) + 3(G^8{}_8 - G^j{}_j)\bigr] = H\cot z\bigl[3(-a_4'') + 3a_4''\bigr] = 0 .
$$

For $\nu$ a transverse direction: $\partial_\nu G^\nu{}_\nu = 0$ and every $\Gamma^\mu{}_{\mu\nu}$ is zero (case (b) of Section 3.15 gives $\partial_\nu\ln h_\mu = 0$). So $\nabla_\mu G^\mu{}_\nu = 0$ for all eight $\nu$ and every $a_4(x_4)$ (PROVED; Notebook 03b, In [21]; record `Revision/gkd_lovelock/results/lovelock-report.json`, checks `k1_equals_minus_4_einstein` and `k1_divergence_free`). The same computation for an energy-momentum tensor $T = \mathrm{diag}(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8)$ gives $\nabla_\mu T^\mu{}_4 = -\partial_4\rho - 3a_4'(p_3 - p_t)$: energy flows between 3-space and the extra times when their pressures differ (record `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`, check `divergence_x4_component`; Chapter 9 derives and uses it).

### 3.26 What Einstein's equations would ask of the source

**Einstein's field equations.** In Einstein's theory of gravity the curvature is tied to the matter by

$$
G^\mu{}_\nu + \Lambda\,\delta^\mu{}_\nu = \kappa\,T^\mu{}_\nu ,
$$

with a positive constant $\kappa$ (the strength of gravity), a constant $\Lambda$ (the **cosmological constant**) and the **energy-momentum tensor** $T^\mu{}_\nu$ of the matter, whose diagonal for the sources of this book is $T = \mathrm{diag}(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8)$: the **energy density** $\rho$ and the **pressures** $p_3$ of 3-space, $p_t$ of the extra times and $p_8$ of the hidden direction (record `Revision/field_equations_a4/a4-equations.json`, key `conventions.source`). We take this form of the equations as given here (ASSUMED in this chapter); Chapter 9 derives $T$ for the fields of the book, and Chapter 12 derives the equations, together with their higher-order Lovelock companions, and solves them. The contracted Bianchi identity of Section 3.25 is the reason why the left side must be the Einstein tensor: its divergence is zero for every metric, as the conservation of energy and momentum demands of the right side.

**The equations for the author's metric.** With the Einstein tensor of Section 3.25 the four independent components are

$$
3a_4'^2 + 21H^2 + \Lambda = -\kappa\rho, \qquad -3a_4'^2 + a_4'' + 15H^2 + \Lambda = \kappa p_3,
$$

$$
-3a_4'^2 - a_4'' + 15H^2 + \Lambda = \kappa p_t, \qquad -3a_4'^2 + 15H^2 + \Lambda = \kappa p_8
$$

(the $x_4$ component uses $T^4{}_4 = -\rho$; the others $T^\mu{}_\mu = p_\mu$). These are the four equations `einstein.constraint_x4`, `einstein.space_x1`, `einstein.extraTime_x5` and `einstein.hidden_x8` of the record `a4-equations.json`. Subtracting the third from the second gives $2a_4'' = \kappa(p_3 - p_t)$, the **evolution equation** of the record (`einstein.evolution`): the acceleration $a_4''$ of the metric function is driven by the difference between the pressure of 3-space and that of the extra times. The record also states that every twice-differentiable function $a_4(x_4)$ is allowed, with the source then fixed by these equations (`einstein.allowedA4`).

**No empty spacetime has this metric.** Without matter, $T = 0$, the $x_4$ and $x_8$ components would give $G^4{}_4 + \Lambda = 0$ and $G^8{}_8 + \Lambda = 0$, hence $G^4{}_4 = G^8{}_8$; but $G^4{}_4 - G^8{}_8 = 6(a_4'^2 + H^2) > 0$ (Section 3.25). So for $H > 0$ the author's metric is not a solution of Einstein's equations without matter, for any $\Lambda$ (PROVED; record `a4-equations.json`, key `einstein.noVacuum`; lead check `no_vacuum_for_H_positive`). Subtracting the $x_8$ equation from the $x_4$ equation also gives $\kappa(\rho + p_8) = -6(a_4'^2 + H^2) < 0$ for every history (record key `einstein.nullEnergy`; lead check `einstein_null_energy`).

**The source along the deflating history.** For $a_4 = AHx_4$ ($a_4' = AH$, $a_4'' = 0$) the evolution equation forces $p_3 = p_t$, and the three space-like and extra-time equations have the same left side, so all three pressures are one number $p$:

$$
\kappa\rho = -3H^2(7 + A^2) - \Lambda, \qquad \kappa p = 3H^2(5 - A^2) + \Lambda, \qquad \kappa(\rho + p) = -6H^2(A^2 + 1)
$$

(the $x_4$ equation solved for $\kappa\rho$; the $x_1$ equation with $a_4'' = 0$; the sum of the two, in which $\Lambda$ cancels). These are the entries `rhoEinstein`, `pEinstein` and `rhoPlusPEinstein` of the key `linearMember` of the record `Revision/field_equations_a4/a4-equations.json` (PROVED here; Notebook 03b reads the three texts of the record and checks them against its Einstein tensor, In [26]). For the canonical $A = 1$, $H = 1$: $G = \mathrm{diag}(12, 12, 12, 24, 12, 12, 12, 12)$, $\kappa\rho = -24 - \Lambda$ and $\kappa p = 12 + \Lambda$.

**What this means, with its status.** Ordinary matter (dust, radiation, a gas) has $\rho + p \ge 0$; this is the **null energy condition** (a standard condition of physics, used here as the definition of "ordinary", ASSUMED). Within Einstein's equations, the deflating history needs $\kappa(\rho + p) = -6H^2(A^2 + 1) < 0$ for every slope $A$ and every $\Lambda$: whatever fills such a spacetime, it is not ordinary matter (PROVED). Three things are NOT shown here: whether a field of this book can supply such a source (Chapters 9, 12 and 17 answer this; the Kohn-Sham states computed along the history cannot, `Revision/field_equations_a4/reports/ks-source-conditions.json`, which is why the history is a PRESCRIBED BACKGROUND, Section 3.8); what the higher-order Lovelock terms change (Chapter 12); and anything about pairs of universes or about matter and antimatter, which this chapter does not touch.

### 3.27 Example: the curvature of the author's metric

Notebook 03b does Sections 3.23 to 3.26 by computer algebra, for a general function $a_4(x_4)$. It reads the metric exactly as the author typed it; computes all 512 Christoffel symbols with the formula of Section 3.15 and compares the 25 non-zero ones with the record; draws them; checks them a second way by finite differences at the test point of the record's brute-force check; checks that observers at rest fall freely; computes the 156 non-zero Riemann components, checks their symmetries and the first Bianchi identity and compares every one with the record; computes the 28 plane curvatures, the Ricci tensor, the Ricci scalar and the Einstein tensor and compares them with the record and with the lead's checks; compares 310 components with the record numerically with 30 digits at the record's five test points; checks the contracted Bianchi identity; computes the Kretschmann scalar; evaluates everything along the deflating history; reproduces the source of Section 3.26 from the record; and repeats the curvature for the negative control with inflating extra times. It needs no Rust, runs in about 1 minute (the cells with the Riemann tensor and the negative control take up to half a minute each) and ends with the line ALL 39 CHECKS PASSED (notebook 03b).

<!-- NOTEBOOK 03b -->

### 3.30 Line-by-line walk-through of Notebook 03b

The notebook has 28 code cells, In [1] to In [28]. As before, a line or a small group of lines is quoted and then explained, and a line `...` in a quoted figure command stands for the remaining lines of the caption, printed in full under its figure in Section 3.29.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 3.28. Its code is, line for line, the set-up code of Notebook 03a explained in Section 3.13 under In [1], with the single difference `NOTEBOOK_ID = "03b"  # this notebook: chapter 03, example b`. It prints Set-up of notebook 03b complete: repository folder found, helpers defined.

**In [2], every result in one piece.** Word for word In [2] of Notebook 03a (Section 3.13). It prints From now on check and report print each of their results in one piece.

**In [3], packages, record and symbols.**

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


def record_check(report_file, check_name, detail_part=""):
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


x1, x2, x3, x4, x5, x6, x7, x8 = sp.symbols("x1:9", real=True)
X = [x1, x2, x3, x4, x5, x6, x7, x8]  # the coordinates, counted 0 to 7 in Python
NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
H = sp.symbols("H", positive=True)  # the constant of the author
a4 = sp.Function("a4")(x4)  # the metric function, unknown
a4p, a4pp, a4v = sp.symbols("a4p a4pp a4v", real=True)  # a4 prime, a4 two primes, a4
z = sp.symbols("z", positive=True)  # z = 6 H x8, for printing
```

The record of the Rust program `lovelock_gkd` is read into the dictionary `record`. `PYTHON_REPORT` and `RUST_REPORT` are the names of two further Revision reports: the report of the independent sympy checker and the report of the Rust program's own checks. The function `record_check` reads such a report and requires that it lists the check `check_name` as passed. The reports come in two layouts: in one, `checks` is a dictionary from each check name to an entry with the key `passed`; in the other, it is a list of entries, each with a `name` and a `verdict`. `isinstance(checks, dict)` asks which layout this report has; `checks.get(check_name, {})` gives the entry or an empty dictionary when the name is missing, and `next(..., {})` finds the entry with that name in the list (or the empty dictionary). The entry must say passed (the value `True`, or the verdict `"PASS"`), and, when `detail_part` is given, its `detail` text must contain that piece; otherwise `raise AssertionError(...)` stops the notebook with a message that names the report and the check. So whenever this notebook says that a number agrees with a Revision record, it also confirms, from the record itself, that the record's own check of that number passed. Then the eight coordinates, their list `X` and their printed names `NAMES`; the constant $H > 0$; the unknown function $a_4(x_4)$; and four plain symbols for printing: `a4p` for $a_4'$, `a4pp` for $a_4''$, `a4v` for the value of $a_4$, and `z` for $6Hx_8$.

```python
def symbolic(expression):
    """Write the derivatives of a4 as a4p and a4pp and the value a4(x4) as a4v."""
    expression = expression.subs(sp.Derivative(a4, (x4, 2)), a4pp)  # second first
    return expression.subs(sp.Derivative(a4, x4), a4p).subs(a4, a4v)


def plain(expression):
    """As symbolic, and 6 H x8 written as z."""
    return symbolic(expression).subs(x8, z / (6 * H))


say("Record read; symbols x1 ... x8, H, a4(x4), a4p, a4pp, a4v and z defined.")
```

`symbolic` replaces the second derivative of $a_4$ (written `sp.Derivative(a4, (x4, 2))`) by `a4pp`, then the first derivative by `a4p`, then the function itself by `a4v`. The second derivative is replaced first, because replacing the first derivative first could also change the second one (which is the derivative of the first). `plain` does the same and also writes $6Hx_8$ as $z$. The last line prints the output of In [3].

**In [4], the metric from the author's text.**

```python
text = record["metricAsGiven"]  # the metric exactly as the author typed it
text = text.replace("exp^", "E^").replace("a4[x4]", "a4")
text = text.replace("Sin[6 H x8]", "sin(6 H x8)").replace("Cot[6 H x8]", "cot(6 H x8)")
text = text.replace("{", "[").replace("}", "]").replace("^", "**")
metric_names = {"E": sp.E, "a4": a4, "H": H, "x8": x8, "sin": sp.sin, "cot": sp.cot}
g = sp.Matrix(parse_expr(text, local_dict=metric_names, transformations=(
    standard_transformations + (implicit_multiplication,))))
```

The same translation of the author's Mathematica text as in Notebook 03a (Section 3.13, In [5]), with two replacements per line: `exp^` becomes `E^`, `a4[x4]` becomes `a4`, the square brackets of the sine and the cotangent become round ones, the braces of lists become square brackets and `^` becomes `**`. The dictionary `metric_names` says what each name means, and `parse_expr` with implicit multiplication reads the text; `sp.Matrix` makes the exact $8 \times 8$ matrix `g`.

```python
for k in range(8):
    say(f"  g[{NAMES[k]}, {NAMES[k]}] = {plain(g[k, k])}")
check(all(g[i, j] == 0 for i in range(8) for j in range(8) if i != j),
      "the metric read from the text of the author is diagonal")
```

The eight diagonal entries are printed with `plain`, for example `exp(2*a4v)*sin(z)**(1/3)` for $e^{2a_4}\sin^{1/3}z$, and the check requires the 56 entries off the diagonal to be zero.

**In [5], reading the record's components.**

```python
record_names = {"a4p": a4p, "a4pp": a4pp, "a4v": a4v, "H": H, "x8": x8, "E": sp.E,
                "sin": sp.sin, "cot": sp.cot}


def from_mathematica(entry_text):
    """A component of the record (Mathematica notation) as a sympy expression."""
    t = entry_text.replace("Derivative[1][a4][x4]", "a4p")
    t = t.replace("Derivative[2][a4][x4]", "a4pp").replace("a4[x4]", "a4v")
    t = t.replace("Sin[6*H*x8]", "sin(6*H*x8)").replace("Cot[6*H*x8]", "cot(6*H*x8)")
    t = t.replace("^", "**")
    if "[" in t or "]" in t:
        raise ValueError(f"cannot translate {entry_text}")
    return parse_expr(t, local_dict=record_names)
```

The record writes $a_4'$ as `Derivative[1][a4][x4]` and $a_4''$ as `Derivative[2][a4][x4]`. `from_mathematica` translates a component of the record into sympy: the two derivatives become `a4p` and `a4pp`, `a4[x4]` becomes `a4v`, the functions get round brackets, `^` becomes `**`. If a square bracket is left, some notation was not translated and the function stops with an error instead of misreading silently. The dictionary `record_names` says what the names in the translated text mean.

```python
def tidy(expression):
    """Simplify an expression.  It writes 6 H x8 as z (so that 12 H x8 becomes 2z),
    simplifies it twice, once as it is and once after writing sin(2z) as
    2 sin(z) cos(z) (expand_trig), keeps the shorter result (count_ops counts the
    operations), and writes z as 6 H x8 again."""
    expression = sp.sympify(expression).subs(x8, z / (6 * H))
    first = sp.simplify(expression)
    second = sp.simplify(sp.expand_trig(expression))
    best = second if sp.count_ops(second) < sp.count_ops(first) else first
    return best.subs(z, 6 * H * x8)
```

`tidy` is the simplifier of the notebook. `sp.sympify` turns a plain Python number into a sympy number (so that `.subs` works on it). It writes $6Hx_8$ as $z$, simplifies once directly and once after `sp.expand_trig`, which writes $\sin 2z$ as $2\sin z\cos z$, and keeps the result with fewer operations (`sp.count_ops` counts them); sympy sometimes reaches the simplest form only one of the two ways. At the end $z$ is written as $6Hx_8$ again. The line `best = second if ... else first` chooses one of two values by a condition.

```python
def vanishes(expression):
    """True when the expression simplifies to zero."""
    return tidy(expression) == 0


def same(mine, theirs):
    """True when mine (with the function a4) equals theirs (record symbols)."""
    return vanishes(symbolic(mine) - theirs)
```

`vanishes` is true when an expression simplifies to $0$; `same` compares one of our expressions (written with the function $a_4$) with one of the record (written with `a4p`, `a4pp`, `a4v`): it rewrites ours with `symbolic` and asks whether the difference vanishes.

```python
example = record["christoffelNonzero_b_le_c"][6]["value"]
say(f"example of a record entry: {example}")
say(f"translated: {from_mathematica(example)}")
```

The seventh entry (position 6) of the record's Christoffel list serves as an example. The output shows it in the record's notation and then its translation:

```text
Derivative[1][a4][x4]*E^(2*a4[x4])*Sin[6*H*x8]^(1/3)
a4p*exp(2*a4v)*sin(6*H*x8)**(1/3)
```

This is the symbol $\Gamma^{x_4}{}_{x_1x_1} = a_4'e^{2a_4}\sin^{1/3}z$ of Section 3.23.

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

The same function as in Notebook 03c (Section 3.22, In [3]), with `tidy` instead of `sp.simplify`: the Christoffel formula of Section 3.15 applied to all $8^3 = 512$ index lists, without using the symmetry in $b$ and $c$ (so that the symmetry can be checked).

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

`Gamma` is the table of the author's metric. `nonzero` lists the index lists of the non-zero symbols and `upper_half` those with $b \le c$. The two RESULT lines print 37 and 25, the counts of Section 3.23, and the check confirms the symmetry $\Gamma^a{}_{bc} = \Gamma^a{}_{cb}$ for all 512.

**In [7], comparison with the record.**

```python
for a, b, c in upper_half:
    say(f"  Gamma^{NAMES[a]}_({NAMES[b]} {NAMES[c]}) = {plain(Gamma[a][b][c])}")
```

The 25 symbols are printed: they are the table of Section 3.23, in sympy's way of writing. It writes $H\cot z$ as `H/tan(z)`, $-H\tan z\,e^{2a_4}\sin^{1/3}z$ as `-H*exp(2*a4v)*sin(z)**(4/3)/cos(z)` (because $\sin^{1/3}z\tan z = \sin^{4/3}z/\cos z$), and $-6H(\tan z + \cot z) = -6H/(\sin z\cos z)$ as `-12*H/sin(2*z)` (because $\sin 2z = 2\sin z\cos z$).

```python
record_gamma = {(NAMES.index(e["a"]), NAMES.index(e["b"]), NAMES.index(e["c"])):
                from_mathematica(e["value"])
                for e in record["christoffelNonzero_b_le_c"]}
check(sorted(record_gamma) == upper_half and len(upper_half) == 25,
      "the same 25 non-zero Christoffel symbols as the record")
record_check(PYTHON_REPORT, "rust_christoffels_agree")  # stops if not passed
check(all(same(Gamma[a][b][c], value) for (a, b, c), value in record_gamma.items()),
      "every Christoffel symbol equals the record exactly",
      record=f"{CURVATURE_RECORD}, christoffelNonzero_b_le_c (and "
             "python-lovelock-report.json, check rust_christoffels_agree)")
```

The line `record_check(PYTHON_REPORT, "rust_christoffels_agree")` confirms that the sympy checker of the Revision record found every Christoffel symbol of the Rust program correct; the notebook stops there if that check had not passed.

`record_gamma` is a dictionary built from the record's list: the key is the index list (`NAMES.index("x4")` is 3, the position of a name in the list) and the value is the translated symbol. The first check requires the record and the notebook to name the same 25 index lists (`sorted` turns the keys into an ordered list); the second requires every value to agree exactly. The PASS line names the record and its independent verification.

**In [8], Figure 03b.1: the Christoffel symbols as heat maps.**

```python
from matplotlib.colors import LinearSegmentedColormap, SymLogNorm

BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
MAGENTA, GREEN, VIOLET, RED = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
DIVERGING = LinearSegmentedColormap.from_list("blue_grey_red", [BLUE, "#f0efec", RED])
LABELS = [f"$x_{k}$" for k in range(1, 9)]
ARGS = (z, a4v, a4p, H)  # the arguments of the numerical functions
```

The colour palette and the blue-grey-red colour scale of Notebook 03a (Section 3.13, In [9]); `SymLogNorm` is a colour scale that is logarithmic on both sides of zero. `LABELS` are the axis labels. `ARGS` lists the four arguments of the numerical functions made next: $z$, $a_4$, $a_4'$, $H$.

```python
def numeric(expression):
    """A numerical function f(z, a4v, a4p, H) of an expression."""
    return sp.lambdify(ARGS, plain(expression), "numpy")


gamma_functions = {(a, b, c): numeric(Gamma[a][b][c]) for a, b, c in nonzero}
POINT = (np.pi / 4, 0.5, 1.0, 1.0)  # z, a4, a4p, H: the canonical slice a4 = 0.5
tables = np.zeros((8, 8, 8))
for (a, b, c), f in gamma_functions.items():
    tables[a, b, c] = f(*POINT)
```

`numeric` turns an exact expression into a fast numerical function (`sp.lambdify`, Section 3.13, In [8]). `gamma_functions` holds one such function for each of the 37 non-zero symbols. `POINT` is the point $z = \pi/4$ on the slice $a_4 = 0.5$ of the history $a_4 = x_4$ (so $a_4' = 1$), with $H = 1$; `f(*POINT)` calls a function with the four numbers. The $8 \times 8 \times 8$ array `tables` holds the 512 numbers (zero where the symbol is zero).

```python
fig, axes = plt.subplots(2, 4, figsize=(11.0, 5.4))
norm = SymLogNorm(linthresh=0.1, vmin=-15.0, vmax=15.0, base=10)
for a, ax in enumerate(axes.flat):
    image = ax.imshow(tables[a], cmap=DIVERGING, norm=norm)
    for b, c in itertools.product(range(8), repeat=2):
        if tables[a, b, c] != 0:
            ax.text(c, b, f"{tables[a, b, c]:.2f}", ha="center", va="center",
                    fontsize=6.0)
```

Eight panels in two rows of four, one for each upper index $a$ (`axes.flat` runs through them in order). The colour scale is ordinary between $-0.1$ and $0.1$ and logarithmic beyond, up to $\pm 15$, so that small and large symbols are both visible. In each panel the $8 \times 8$ table $\Gamma^a{}_{bc}$ is drawn with row $b$ and column $c$, and every non-zero value is written into its square with two decimals.

```python
    ax.set_title(f"$\\Gamma^{{x_{a + 1}}}{{}}_{{bc}}$", fontsize=10)
    ax.set_xticks(range(8), [str(k) for k in range(1, 9)], fontsize=7)
    ax.set_yticks(range(8), [str(k) for k in range(1, 9)], fontsize=7)
    ax.grid(False)
fig.colorbar(image, ax=axes, shrink=0.8, label="value (unit $H$)")
fig.suptitle("Christoffel symbols at $z = \\pi/4$, $a_4 = 0.5$, "
             "$a_4^{\\prime} = 1$, $H = 1$ (row $b$, column $c$)")
```

Each panel gets the title $\Gamma^{x_a}{}_{bc}$ (in an f-string a doubled brace `{{` prints one brace, so that the braces of the math notation survive) and the tick labels 1 to 8. One colour bar serves all panels; `suptitle` is the title of the whole figure.

```python
save_figure(fig, "christoffel_heat_maps",
            "The 512 Christoffel symbols $\\Gamma^{a}{}_{bc}$ of the author's metric "
...
check(np.allclose(tables, tables.transpose(0, 2, 1))
      and all(3 in key or 7 in key for key in nonzero),
      "the tables are symmetric in b, c; every non-zero symbol has an index x4 or x8")
```

The figure is saved. The check: `tables.transpose(0, 2, 1)` exchanges the second and the third index, so the first condition is $\Gamma^a{}_{bc} = \Gamma^a{}_{cb}$ as numbers; the second requires every non-zero index list to contain position 3 ($x_4$) or position 7 ($x_8$).

**What Figure 03b.1 shows.** Only 37 of the 512 squares are coloured. In the panels of 3-space ($\Gamma^{x_1}$, $\Gamma^{x_2}$, $\Gamma^{x_3}$) the value $1.00$ appears four times, at the positions $(x_k, x_4)$, $(x_4, x_k)$, $(x_k, x_8)$, $(x_8, x_k)$: here both $a_4' = 1$ and $H\cot(\pi/4) = 1$. In the panels of the extra times the squares with $x_4$ are blue, $-1.00$: the deflation. The panel $\Gamma^{x_4}$ has $2.42$ on the 3-space diagonal and $0.33$ on the extra-time diagonal; the panel $\Gamma^{x_8}$ has $-2.42$, $0.33$ and the largest value, $\Gamma^{x_8}{}_{x_8x_8} = -12$. Each panel is symmetric about its diagonal.

**In [9], Figure 03b.2: the symbols across the patch.**

```python
z_line = np.linspace(0.01, np.pi / 2 - 0.01, 500)
chosen = [((0, 0, 7), RED, "-", "$\\Gamma^{x_1}{}_{x_1 x_8}$"),
          ((7, 7, 7), VIOLET, "--", "$\\Gamma^{x_8}{}_{x_8 x_8}$"),
          ((7, 0, 0), ORANGE, "-.", "$\\Gamma^{x_8}{}_{x_1 x_1}$"),
          ((7, 4, 4), BLUE, ":", "$\\Gamma^{x_8}{}_{x_5 x_5}$"),
          ((0, 0, 3), AQUA, "-", "$\\Gamma^{x_1}{}_{x_1 x_4}$")]
fig, ax = plt.subplots()
```

500 values of $z$ inside the patch, and five chosen symbols, each with its index list, colour, line style and label.

```python
for index, colour, style, label in chosen:
    values = np.broadcast_to(gamma_functions[index](z_line, 0.5, 1.0, 1.0),
                             z_line.shape)
    sign = "+" if values[len(values) // 2] > 0 else "minus"
    ax.plot(z_line, np.abs(values), color=colour, ls=style, lw=1.8,
            label=f"{label} (sign {sign})")
```

For each symbol the values at the 500 points ($a_4 = 0.5$, $a_4' = 1$, $H = 1$); `np.broadcast_to` repeats a constant (the symbol $a_4'$ does not depend on $z$, and its function returns one number). The sign is read at the middle point (`//` divides and rounds down), and the absolute value is drawn, because a logarithmic axis can only show positive numbers.

```python
ax.set_yscale("log")
ax.set_xlabel("$z = 6 H x_8$ (radians)")
ax.set_ylabel("absolute value of the symbol (unit $H$)")
ax.set_title("Christoffel symbols across the patch "
             "($a_4 = 0.5$, $a_4^{\\prime} = 1$, $H = 1$)")
ax.set_ylim(1e-5, 3e3)  # room below the curves for the legend
ax.legend(fontsize=8, loc="lower center", ncol=2)
save_figure(fig, "christoffel_versus_z",
            "The absolute values of five Christoffel symbols of the author's metric "
...
check(abs(gamma_functions[(0, 0, 7)](np.pi / 4, 0.5, 1.0, 1.0) - 1.0) < 1e-14,
      "Gamma^x1_(x1 x8) = H cot z equals 1 at z = pi/4, H = 1")
```

A logarithmic vertical axis, labels, title, the range of the axis and the legend; the figure is saved; the check confirms $H\cot(\pi/4) = 1$.

**What Figure 03b.2 shows.** $\Gamma^{x_1}{}_{x_1x_8} = H\cot z$ (red) falls from about $100$ near the tip to almost $0$ at the patch end; $\Gamma^{x_8}{}_{x_8x_8}$ (violet dashed) is large at both ends and smallest, $12$, at $z = \pi/4$; $\Gamma^{x_8}{}_{x_1x_1}$ and $\Gamma^{x_8}{}_{x_5x_5}$ grow towards the patch end, where $\tan z$ grows without bound; $\Gamma^{x_1}{}_{x_1x_4} = a_4' = 1$ (aqua) is flat. Large Christoffel symbols belong to the coordinates; whether the geometry itself is extreme is decided by an invariant, the Kretschmann scalar of In [22].

**In [10], a second check by finite differences.**

```python
prime = chr(39)  # the apostrophe (character number 39): the record writes a4 prime so
point_text = (f"H = 0.23, a4 = 0.17, a4{prime} = 0.61, a4{prime}{prime} = -0.37, "
              "x8 = 0.41")  # the test point as the record writes it
check(record_check(RUST_REPORT, "k1_brute_force_numeric", point_text),
      "the test point is the one of the brute-force check of the Rust program")
H_n, a0, a1, a2, x8_n = 0.23, 0.17, 0.61, -0.37, 0.41  # the test point
```

The Rust program's check `k1_brute_force_numeric` names its test point in a text that writes $H = 0.23$, $a_4 = 0.17$, $a_4' = 0.61$, $a_4'' = -0.37$ and $x_8 = 0.41$, with one apostrophe for each prime (the line `point_text` builds exactly this text). `chr(39)` is the character number 39, the apostrophe, and the f-string puts it after `a4` once for $a_4'$ and twice for $a_4''$ (the comment at the end of the line says so; the book prints a straight apostrophe in code as a curly one, and the character number makes plain which character is meant). `record_check(RUST_REPORT, "k1_brute_force_numeric", point_text)` (In [3]) confirms that this check of the record passed and that its detail contains exactly this text; `check` prints the PASS line. The five numbers are then named.

```python
def metric_numbers(x):
    """The metric as an 8 x 8 numpy table at the point x (8 coordinates)."""
    a = a0 + a1 * x[3] + 0.5 * a2 * x[3] ** 2  # a4(x4) with a4(0) = 0.17, ...
    warp_n = np.sin(6 * H_n * x[7]) ** (1 / 3)
    return np.diag([np.exp(2 * a) * warp_n] * 3 + [-1.0]
                   + [-np.exp(-2 * a) * warp_n] * 3
                   + [1 / np.tan(6 * H_n * x[7]) ** 2])
```

The metric as a plain table of numbers at a point `x` (a list of eight coordinates, `x[3]` is $x_4$ and `x[7]` is $x_8$), for the concrete function $a_4(x_4) = 0.17 + 0.61x_4 - 0.185x_4^2$, which has at $x_4 = 0$ the value $0.17$, the slope $0.61$ and the second derivative $-0.37$ of the test point. `np.diag` makes the diagonal matrix.

```python
def christoffel_numbers(x, h):
    """All 512 Christoffel symbols at x from central differences with step h."""
    d_metric = np.zeros((8, 8, 8))  # d_metric[c] = derivative of g along x_c
    for c in range(8):
        step = np.zeros(8)
        step[c] = h
        d_metric[c] = (metric_numbers(x + step) - metric_numbers(x - step)) / (2 * h)
```

The derivatives of the metric without any algebra: for each coordinate $c$ the point is moved by $\pm h$ along $x_c$ (`step` is zero except at position $c$), and the **central difference** $(g(x + he_c) - g(x - he_c))/(2h)$ approximates $\partial_c g$ (Chapter 2).

```python
    inverse = np.linalg.inv(metric_numbers(x))
    table = np.zeros((8, 8, 8))
    for a, b, c in itertools.product(range(8), repeat=3):
        table[a, b, c] = 0.5 * sum(inverse[a, d] * (d_metric[b][d, c]
                                   + d_metric[c][d, b] - d_metric[d][b, c])
                                   for d in range(8))
    return table
```

The inverse metric as numbers (`np.linalg.inv`) and the Christoffel formula of Section 3.15, now with numbers.

```python
x_point = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, x8_n])
exact = np.zeros((8, 8, 8))
for (a, b, c), f in gamma_functions.items():
    exact[a, b, c] = f(6 * H_n * x8_n, a0, a1, H_n)
steps = 10.0 ** -np.arange(1, 9)  # h = 0.1, 0.01, ..., 1e-8
errors = np.array([np.max(np.abs(christoffel_numbers(x_point, h) - exact))
                   for h in steps])
for h, e in zip(steps, errors):
    say(f"  h = {h:.0e}: largest error of the 512 symbols = {e:.2e}")
```

The test point (only $x_8 = 0.41$ matters, with $x_4 = 0$); the exact symbols there from the functions of In [8], with $z = 6 \cdot 0.23 \cdot 0.41$, $a_4 = 0.17$, $a_4' = 0.61$, $H = 0.23$; eight steps $h = 10^{-1}, \dots, 10^{-8}$ (`10.0 ** -np.arange(1, 9)` raises 10 to the powers $-1$ to $-8$); for each the largest difference between the 512 numerical and exact symbols. The eight output lines show the errors $4.01 \times 10^{-1}$, $3.66 \times 10^{-3}$, $3.65 \times 10^{-5}$, $3.65 \times 10^{-7}$, $3.66 \times 10^{-9}$, $5.36 \times 10^{-11}$, $8.46 \times 10^{-10}$, $9.00 \times 10^{-9}$.

```python
order = np.log10(errors[0] / errors[1])  # the slope between h = 0.1 and h = 0.01
report("measured order of the error between h = 0.1 and h = 0.01", f"{order:.3f}")
check(1.9 < order < 2.1 and errors.min() < 1e-8,
      "finite differences reproduce all 512 symbols; the error falls like h^2")
```

When $h$ shrinks tenfold, an error $Ch^p$ shrinks by $10^p$, so $p = \log_{10}$ of the ratio of the errors. The RESULT line prints $2.040$: the central difference has order 2 (Chapter 2). The check requires the order between 1.9 and 2.1 and the best error below $10^{-8}$.

**In [11], Figure 03b.3.**

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
```

`ax.loglog` draws with logarithmic scales on both axes: the errors as dots joined by lines, and a reference line proportional to $h^2$ that starts at the first error. Labels, title, legend.

```python
best = int(np.argmin(errors))  # the position of the smallest error in the list
report("best step and its error", f"h = {steps[best]:.0e}, error {errors[best]:.1e}")
mantissa, exponent = f"{errors[best]:.1e}".split("e")  # e.g. "3.2" and "-10"
best_error = f"{mantissa} \\times 10^{{{int(exponent)}}}"  # 3.2 x 10^-10 in LaTeX
best_step = f"10^{{{round(np.log10(steps[best]))}}}"  # the step as a power of 10
```

`np.argmin` gives the position of the smallest error; the RESULT line prints h = 1e-06, error 5.4e-11. The next three lines write the best error and step in math notation for the caption: the text `5.4e-11` is split at the letter e into `5.4` and `-11`, and the caption receives $5.4 \times 10^{-11}$ and $10^{-6}$ (a tripled brace in an f-string gives one literal brace around the inserted value).

```python
save_figure(fig, "finite_differences",
            "The largest difference between the 512 Christoffel symbols computed "
...
check(errors[0] > errors[1] > errors[2] > errors[3],
      "the error shrinks as the step shrinks from 0.1 to 0.0001")
```

The figure is saved; its caption is assembled from pieces, two of which are the f-strings just made. The check requires the error to decrease over the first four steps.

**What Figure 03b.3 shows.** From $h = 10^{-1}$ to $h = 10^{-6}$ the blue dots lie on the dashed line of slope 2: each tenfold smaller step gives a hundredfold smaller error. Below $h = 10^{-6}$ the error grows again: the rounding errors of the computer, about $10^{-16}$ of each number, are divided by $h$ in the difference quotient. The best step, $10^{-6}$, gives $5.4 \times 10^{-11}$. Numbers computed without any algebra agree with the exact symbols.

**In [12], free fall along $x_4$ and the contracted symbols.**

```python
check(all(Gamma[a][3][3] == 0 for a in range(8)),
      "Gamma^a_(x4 x4) = 0: observers at rest fall freely, x4 is their proper time")
contracted = [vanishes(sum(Gamma[a][a][b] for a in range(8))
                       - sp.diff(sp.log(sp.cos(6 * H * x8)), X[b]))
              for b in range(8)]
check(all(contracted),
      "sum over a of Gamma^a_(a b) equals the derivative of ln cos z")
```

The first check: the eight symbols $\Gamma^a{}_{x_4x_4}$ (lower positions 3 and 3) are zero, so observers at rest fall freely (Section 3.23). The second: for each $b$, $\sum_a\Gamma^a{}_{ab} - \partial_b\ln\cos z$ vanishes (Sections 3.15 and 3.23).

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

The formula of Section 3.17, as in Notebook 03c, but with less work: `itertools.combinations(range(n), 2)` gives only the pairs $c < d$ (28 of them); the component with $c$ and $d$ exchanged is stored with the opposite sign (symmetry (S1)), and those with $c = d$ are zero. Non-zero values are kept in a dictionary.

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

The same as in Notebook 03c, except that products with a zero entry of the inverse metric are skipped (for a diagonal metric only $b = e$ remains), and the results are simplified with `tidy`.

```python
R_down = riemann(Gamma, X)  # R^a_bcd
R_mixed = raise_second(R_down, g)  # R^ab_cd
report("non-zero components R^a_bcd", len(R_down))
report("non-zero components R^ab_cd", len(R_mixed))
record_check(RUST_REPORT, "riemann_antisymmetry", "156 nonzero entries")
check(len(R_mixed) == 156, "R^ab_cd has 156 non-zero components, as in the record",
      record="Revision/gkd_lovelock/results/lovelock-report.json, check "
             "riemann_antisymmetry (156 nonzero entries)")
```

The call of `record_check` with `RUST_REPORT`, the check name `riemann_antisymmetry` and the text `156 nonzero entries` confirms that the Rust program's own check passed and that its detail text reports the same 156 non-zero components.

The two forms of the tensor for the author's metric; both have 156 non-zero components (two RESULT lines), the number found by hand in Section 3.24 and by the Rust program. This cell takes a few seconds.

**In [14], the symmetries.**

```python
def get(table, key):
    return table.get(key, 0)


antisymmetric = all(vanishes(v + get(R_mixed, (b, a, c, d)))
                    and vanishes(v + get(R_mixed, (a, b, d, c)))
                    for (a, b, c, d), v in R_mixed.items())
```

`get` returns a component, or 0 if it is absent. `antisymmetric` is true when every component plus the component with the upper pair exchanged vanishes, and the same for the lower pair: $R^{ab}{}_{cd} = -R^{ba}{}_{cd} = -R^{ab}{}_{dc}$.

```python
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

`record_check(PYTHON_REPORT, "riemann_antisymmetry_and_pair_symmetry")` confirms that the sympy checker's check of the same symmetries passed.

All indices lowered, $R_{abcd} = g_{aa}g_{bb}R^{ab}{}_{cd}$ (Section 3.17), and the pair symmetry $R_{abcd} = R_{cdab}$ (S4) checked for every component. One check for both, naming the record's check.

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

`record_check(RUST_REPORT, "riemann_first_bianchi")` confirms that the Rust program's check of the same identity passed.

The first Bianchi identity (S2) for all $8^4 = 4096$ index lists.

```python
warp_free = all(not symbolic(v).has(a4v) and not any(
    isinstance(p, sp.Pow) and p.base == sp.sin(6 * H * x8) and not p.exp.is_integer
    for p in sp.preorder_traversal(symbolic(v))) for v in R_mixed.values())
record_check(RUST_REPORT, "mixed_riemann_free_of_sin_third")
record_check(PYTHON_REPORT, "mixed_riemann_free_of_warp_and_exponential")
check(warp_free, "no R^ab_cd contains sin(z)^(1/3) or e^(a4): the warp cancels",
      record="Revision/gkd_lovelock/results/lovelock-report.json, check "
             "mixed_riemann_free_of_sin_third, and python-lovelock-report.json, "
             "check mixed_riemann_free_of_warp_and_exponential")
```

The two `record_check` lines confirm that both records' checks of the same two properties passed: the Rust program's `mixed_riemann_free_of_sin_third` and the sympy checker's `mixed_riemann_free_of_warp_and_exponential`.

`sp.preorder_traversal` walks through every piece of an expression (its sums, products, powers and their parts). The condition says: no component contains the value $a_4$ (only its derivatives), and no piece is a power of $\sin z$ with an exponent that is not a whole number (`p.base` and `p.exp` are the base and the exponent of a power `p`; `isinstance(p, sp.Pow)` asks whether `p` is a power). So the warp $\sin^{1/3}z$ and the exponentials $e^{\pm 2a_4}$ of the metric entries cancel in every $R^{ab}{}_{cd}$, as found by hand in Section 3.24.

**In [15], comparison with the record's 156 components.**

```python
record_riemann = {}
for entry in record["riemannMixedNonzero"]:
    key = tuple(NAMES.index(n) for n in entry["up"] + entry["down"])
    record_riemann[key] = from_mathematica(entry["value"])
check(sorted(record_riemann) == sorted(R_mixed),
      "the same 156 non-zero components R^ab_cd as the record")
record_check(PYTHON_REPORT, "rust_riemann_agrees")
check(all(same(R_mixed[k], v) for k, v in record_riemann.items()),
      "every component R^ab_cd equals the record exactly",
      record=f"{CURVATURE_RECORD}, riemannMixedNonzero (and "
             "python-lovelock-report.json, check rust_riemann_agrees)")
```

`record_check(PYTHON_REPORT, "rust_riemann_agrees")` confirms that the sympy checker of the Revision record found all 156 components of the Rust program correct.

Each entry of the record's list `riemannMixedNonzero` has the upper indices `up`, the lower indices `down` and the value; `entry["up"] + entry["down"]` joins the two lists of names, and `tuple(...)` turns their positions into a key. Two checks: the same 156 index lists, and every value equal exactly.

```python
groups = {}
for key in sorted(R_mixed):
    groups.setdefault(sp.sstr(plain(R_mixed[key])), []).append(key)
for value_text in sorted(groups):
    a, b, c, d = groups[value_text][0]
    say(f"  {len(groups[value_text]):2d} x  {value_text:30s}  e.g. "
        f"R^({NAMES[a]} {NAMES[b]})_({NAMES[c]} {NAMES[d]})")
report("different values among the 156 components", len(groups))
```

The components are grouped by their value written as text (`sp.sstr`): `setdefault` starts an empty list for a new value, and `append` adds the index list. For each of the 14 different values the number of components, the value (padded to 30 characters by `:30s`) and one example are printed. The output is the result of Section 3.24 in numbers: the plane values $\pm(a_4'^2 - H^2)$ 12 times each, $\pm(a_4'^2 + H^2)$ 18 times each, $\pm(a_4'^2 + a_4'')$ and $\pm(a_4'^2 - a_4'')$ 6 times each, $\pm H^2$ 12 times each, and the 48 components $\pm Ha_4'\cot z$ and $\pm Ha_4'\tan z$, 12 times each.

**In [16], Figure 03b.4: the curvature of every coordinate plane.**

```python
plane = {(a, b): plain(sp.S(get(R_mixed, (a, b, a, b))))  # sp.S: 0 as a sympy 0
         for a, b in itertools.product(range(8), repeat=2) if a != b}
expected = {(0, 1): a4p ** 2 - H ** 2, (4, 5): a4p ** 2 - H ** 2,
            (0, 4): -(a4p ** 2 + H ** 2), (0, 3): a4p ** 2 + a4pp,
            (3, 4): a4p ** 2 - a4pp, (0, 7): -H ** 2, (4, 7): -H ** 2, (3, 7): 0}
for (a, b), formula in expected.items():
    say(f"  plane ({NAMES[a]}, {NAMES[b]}): R^ab_ab = {plane[(a, b)]}")
```

`plane` holds the curvature $K(a, b) = R^{ab}{}_{ab}$ of all 56 ordered pairs of different coordinates (`sp.S` turns the Python number 0 into a sympy zero, which understands `.has` below). `expected` lists one plane of each of the seven kinds of Section 3.24 (two for the transverse-hidden kind) with its formula; the loop prints them.

```python
check(all(sp.expand(plane[key] - formula) == 0 for key, formula in expected.items())
      and all(not v.has(z) and not v.has(a4v) for v in plane.values()),
      "the plane curvatures have the six formulas and do not depend on z or a4")
```

The check: the printed planes have the formulas of Section 3.24 (`sp.expand` multiplies out, so equal polynomials give a zero difference), and no plane curvature depends on $z$ or on the value of $a_4$.

```python
SLOPES = (0.5, 1.0, 2.0)  # three deflating histories, A > 0
fig, axes = plt.subplots(1, 3, figsize=(14.0, 4.8))  # wide: room for -1.25
for ax, slope in zip(axes, SLOPES):
    curv = np.full((8, 8), np.nan)  # NaN: an empty square on the diagonal
    for (a, b), value in plane.items():
        curv[a, b] = float(value.subs({a4p: slope, a4pp: 0, H: 1}))
    image = ax.imshow(curv, cmap=DIVERGING, vmin=-5.0, vmax=5.0)
```

Three panels for the slopes $A = 0.5$, $1$ and $2$ of the history $a_4 = AHx_4$, with $H = 1$, $a_4' = A$ and $a_4'' = 0$. `np.full((8, 8), np.nan)` is an $8 \times 8$ table of NaN ("not a number"), which matplotlib leaves blank: the diagonal stays empty. The other squares receive the plane curvatures, and the table is drawn with the colour scale from $-5$ to $5$.

```python
    for a, b in plane:
        ax.text(b, a, f"{curv[a, b]:g}", ha="center", va="center", fontsize=6.5)
    ax.set_xticks(range(8), LABELS, fontsize=8)
    ax.set_yticks(range(8), LABELS, fontsize=8)
    ax.grid(False)
    ax.set_title(f"$A = {slope:g}$")
fig.colorbar(image, ax=axes, shrink=0.85, label="curvature (unit $H^2$)")
```

The value written into each square (`:g` writes a number without needless digits), the labels $x_1$ to $x_8$, the title with the slope, and one colour bar.

```python
save_figure(fig, "plane_curvatures",
            "The curvature $R^{ab}{}_{ab}$ (no sum) of the coordinate plane of "
...
check([float(plane[(0, 1)].subs({a4p: s, H: 1})) for s in SLOPES] == [-0.75, 0.0, 3.0],
      "the planes inside 3-space: -0.75, 0 and 3 for A = 0.5, 1 and 2")
```

The figure is saved; the check confirms $a_4'^2 - H^2 = -0.75$, $0$, $3$ for the three slopes.

**What Figure 03b.4 shows.** Three symmetric tables. The blocks inside 3-space and inside the extra times change from pale blue ($-0.75$ at $A = 0.5$) through grey ($0$ at $A = 1$) to red ($3$ at $A = 2$). The blocks that mix 3-space with the extra times are always blue and deepen: $-1.25$, $-2$, $-5$. The row and column of $x_4$ are red, $A^2$: $0.25$, $1$, $4$. The row and column of $x_8$ are $-1$ everywhere, except the flat plane of $x_4$ and $x_8$, which is $0$.

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

The function of Notebook 03c (Section 3.22, In [3]), with `tidy` as the simplifier.

```python
Ric = ricci(R_mixed, 8)
R_scalar = tidy(Ric.trace())
G = (Ric - R_scalar / 2 * sp.eye(8)).applyfunc(tidy)
for k in range(8):
    say(f"  {NAMES[k]}: R^a_a = {sp.sstr(plain(Ric[k, k])):18s} "
        f"G^a_a = {plain(G[k, k])}")
say(f"Ricci scalar R = {plain(R_scalar)}")
```

The Ricci tensor, its trace (the Ricci scalar) and the Einstein tensor $G = \mathrm{Ric} - \frac{R}{2}\,\mathbb 1$ (`sp.eye(8)` is the $8 \times 8$ unit matrix). The loop prints the diagonal of both tensors (`:18s` pads the text to 18 characters, so that the columns line up), and the last line the scalar. The output is the result of Section 3.25: $R^a{}_a = a_4'' - 6H^2$ (3-space), $6a_4'^2$, $-a_4'' - 6H^2$ (extra times), $-6H^2$; $G^4{}_4 = 21H^2 + 3a_4'^2$; $R = 6a_4'^2 - 42H^2$.

```python
ricci_ok = all(same(Ric[i, j], from_mathematica(
    record["ricciMixed"][f"{NAMES[i]},{NAMES[j]}"]["mathematica"]))
    for i in range(8) for j in range(8))
einstein_ok = all(same(G[i, j], from_mathematica(
    record["einsteinMixed"][f"{NAMES[i]},{NAMES[j]}"]["mathematica"]))
    for i in range(8) for j in range(8))
scalar_ok = same(R_scalar, from_mathematica(record["ricciScalar"]))
check(ricci_ok and einstein_ok and scalar_ok,
      "all 64 Ricci, all 64 Einstein components and R equal the record",
      record=f"{CURVATURE_RECORD}, ricciMixed, einsteinMixed, ricciScalar (and "
             "python-lovelock-report.json, check rust_ricci_einstein_scalar_agree)")
```

The record stores each of the 64 components under a key such as `"x1,x4"`, with its Mathematica text under `"mathematica"`. All 64 Ricci and all 64 Einstein components and the scalar are compared exactly, in one check.

**In [18], the first Lovelock scalar of the record of the field equations.**

```python
A4_REPORT = "Revision/field_equations_a4/reports/python-a4-report.json"
a4_report = json.loads(repository_file(A4_REPORT).read_text(encoding="utf-8"))
# the report's checks form a list of dictionaries; take the one with this name
L1_entry = next(entry for entry in a4_report["checks"]
                if entry["name"] == "L1_equals_gkd_branch")
L1_detail, L1_verdict = L1_entry["detail"], L1_entry["verdict"]
say(f"record: {L1_detail} ({L1_verdict})")
```

The sympy verification of the record of the field equations of $a_4$ is read. Its checks form a list; `next(...)` takes the first entry whose name is `L1_equals_gkd_branch`. The output prints its text and verdict: $L_{(1)} = -84H^2 + 12\,ad1^2$ (PASS), where `ad1` is the record's name for $a_4'$. $L_{(1)}$ is the first Lovelock scalar of Chapter 11.

```python
L1_text = L1_detail.split("=")[1]  # the text after the equals sign
L1_record = parse_expr(L1_text, local_dict={"H": H, "ad1": a4p})
check(L1_verdict == "PASS" and sp.expand(L1_record - 2 * plain(R_scalar)) == 0,
      "the first Lovelock scalar of the record is twice our Ricci scalar",
      record=f"{A4_REPORT}, check L1_equals_gkd_branch (with "
             "python-lovelock-report.json, check L1_equals_2R)")
```

The text after the equals sign is read as a sympy expression, with `ad1` meaning $a_4'$. The check: the record marks the check as passed, and $L_{(1)} = 2R$ with our $R$ ($2(6a_4'^2 - 42H^2) = 12a_4'^2 - 84H^2$).

**In [19], all 310 components at five test points with 30 digits.**

```python
PYTHON_REPORT = "Revision/gkd_lovelock/results/python-lovelock-report.json"
python_report = json.loads(repository_file(PYTHON_REPORT).read_text(encoding="utf-8"))
mpmath.mp.dps = 30  # mpmath works with 30 significant digits from now on


def exact(text):
    """A fraction such as 46/75 of the record as an mpmath number."""
    fraction = sp.Rational(text)
    return mpmath.mpf(fraction.p) / fraction.q  # numerator / denominator
```

The independent verification of the record lists five test points (`randomPoints`), each a set of exact fractions written as texts such as `"46/75"`. `mpmath.mp.dps = 30` makes mpmath compute with 30 significant digits. `exact` reads such a text as an exact fraction (`sp.Rational`) and divides its numerator `p` by its denominator `q` with 30 digits.

```python
test_points = [[exact(p["H"]), exact(p["x8"]), exact(p["a4"]),
                exact(p["a4" + prime]), exact(p["a4" + prime + prime])]
               for p in python_report["randomPoints"]]
pairs = [(Gamma[a][b][c], v) for (a, b, c), v in record_gamma.items()]
pairs += [(R_mixed[key], v) for key, v in record_riemann.items()]
```

Each test point becomes the five numbers $H$, $x_8$, $a_4$, $a_4'$, $a_4''$ (the record's keys contain the apostrophe, built from `prime` of In [10]). `pairs` collects pairs (our expression, the record's expression): first the 25 Christoffel symbols, then (`+=` appends a list) the 156 Riemann components.

```python
pairs += [(Ric[i, j], from_mathematica(record["ricciMixed"][f"{NAMES[i]},{NAMES[j]}"]
                                       ["mathematica"]))
          for i in range(8) for j in range(8)]
pairs += [(G[i, j], from_mathematica(record["einsteinMixed"][f"{NAMES[i]},{NAMES[j]}"]
                                     ["mathematica"]))
          for i in range(8) for j in range(8)]
pairs += [(R_scalar, from_mathematica(record["ricciScalar"]))]
ARGS30 = (H, x8, a4v, a4p, a4pp)  # the order of the five numbers of a test point
largest, evaluations = mpmath.mpf(0), 0
```

Then the 64 Ricci and 64 Einstein components and the scalar: $25 + 156 + 64 + 64 + 1 = 310$ pairs. `ARGS30` names the five arguments in the order of a test point. The largest relative difference starts at zero and the count of evaluations at 0.

```python
for mine, theirs in pairs:
    f_mine = sp.lambdify(ARGS30, symbolic(sp.S(mine)), "mpmath")
    f_record = sp.lambdify(ARGS30, sp.S(theirs), "mpmath")
    for point in test_points:
        ours, recorded = f_mine(*point), f_record(*point)
        largest = max(largest, abs(ours - recorded) / max(1, abs(recorded)))
        evaluations += 1
```

For each pair, both expressions become functions that compute with mpmath's 30 digits (`"mpmath"` instead of `"numpy"`); at each of the five points both are evaluated, and the relative difference $|\mathrm{ours} - \mathrm{record}|/\max(1, |\mathrm{record}|)$ updates the largest one so far (`max(1, ...)` avoids dividing by a tiny number when a value is close to zero).

```python
report("components compared numerically", len(pairs))
report("evaluations at the five test points", evaluations)
report("largest relative difference (30 digits)", mpmath.nstr(largest, 3))
check(len(test_points) == 5 and largest < mpmath.mpf(10) ** -25,
      "at the five test points every component agrees to more than 25 digits",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
             "randomPoints, checks rust_christoffels_agree, rust_riemann_agrees, "
             "rust_ricci_einstein_scalar_agree")
```

Three RESULT lines: 310 components, 1550 evaluations, and the largest relative difference $1.48 \times 10^{-31}$ (`mpmath.nstr` writes an mpmath number with 3 digits), which is the rounding of the last of the 30 digits. The check requires more than 25 agreeing digits. This is a second, purely numerical confirmation of the exact agreement of In [7], In [15] and In [17].

**In [20], the lead's four properties of the Einstein tensor.**

```python
LEAD = "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json"
check(all(G[i, j] == 0 for i in range(8) for j in range(8) if i != j),
      "the Einstein tensor is diagonal",
      record=f"{LEAD}, check einstein_off_diagonal_zero")
check(all(sp.diff(G[i, i], x8) == 0 for i in range(8)),
      "no component of the Einstein tensor depends on x8",
      record=f"{LEAD}, check einstein_x8_independent")
check(G[0, 0] == G[1, 1] == G[2, 2] and G[4, 4] == G[5, 5] == G[6, 6],
      "3-space components equal, extra-time components equal",
      record=f"{LEAD}, check einstein_isotropy")
```

Three checks of Section 3.25, each naming the check of the lead's independent report: no entry off the diagonal, no dependence on $x_8$, equal 3-space entries and equal extra-time entries.

```python
gap = sp.simplify(symbolic(G[3, 3] - G[7, 7]))
say(f"G^x4_x4 - G^x8_x8 = {sp.factor(gap)}")
check(sp.simplify(gap - 6 * (a4p ** 2 + H ** 2)) == 0,
      "G^x4_x4 - G^x8_x8 = 6 (a4p^2 + H^2) > 0",
      record=f"{LEAD}, check no_vacuum_for_H_positive")
```

The difference $G^{x_4}{}_{x_4} - G^{x_8}{}_{x_8}$, printed in factored form (`sp.factor`) as `6*(H**2 + a4p**2)`, and the check of Section 3.25 behind the statement that no empty spacetime has this metric (Section 3.26).

**In [21], the contracted Bianchi identity.**

```python
divergence = []
for nu in range(8):
    value = sum(sp.diff(G[mu, nu], X[mu]) for mu in range(8)) \
        + sum(Gamma[mu][mu][lam] * G[lam, nu] for mu in range(8) for lam in range(8)) \
        - sum(Gamma[lam][mu][nu] * G[mu, lam] for mu in range(8) for lam in range(8))
    divergence.append(vanishes(value))
check(all(divergence),
      "the contracted Bianchi identity: the divergence of G vanishes",
      record="Revision/gkd_lovelock/results/lovelock-report.json, checks "
             "k1_equals_minus_4_einstein and k1_divergence_free")
```

For each $\nu$ the three sums of the divergence formula of Section 3.25 are computed with the function $a_4(x_4)$ itself (so that sympy can differentiate $a_4''$ into $a_4'''$; the backslashes continue the statement), and the list `divergence` records whether each simplifies to zero. The check requires all eight. The record's Rust program checked the same for its tensor $P_{(1)} = -4G$ (Chapter 11).

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

$K = \sum R^{ab}{}_{cd}R^{cd}{}_{ab}$ from our 156 components, then a second time from the record's 156 components alone, and $\sum_{a,b}R^a{}_bR^b{}_a$; each is multiplied out (`sp.expand`) and factored (`sp.factor`). The output: `12*(7*H**4 - 2*H**2*a4p**2 + 7*a4p**4 + 2*a4pp**2)`, the result of Section 3.25, and $\sum R^a{}_bR^b{}_a = 6(42H^4 + 6a_4'^4 + a_4''^2)$ (the sum of the squares of the four kinds of diagonal entries, three, one, three and one of them).

```python
check(sp.simplify(K - K_record) == 0,
      "K from our components equals K from the 156 components of the record")
check(not K.has(x8) and not K.has(a4v),
      "K depends only on H, a4p and a4pp, not on z and not on a4")
square_form = 7 * (a4p ** 2 - H ** 2 / 7) ** 2 + sp.Rational(48, 7) * H ** 4 \
    + 2 * a4pp ** 2
check(sp.expand(K / 12 - square_form) == 0,
      "K/12 = 7 (a4p^2 - H^2/7)^2 + 48 H^4/7 + 2 a4pp^2, so K > 0 for H > 0")
report("smallest possible K (at a4p^2 = H^2/7, a4pp = 0)",
       sp.sstr(sp.Rational(576, 7) * H ** 4))
```

Three checks: our $K$ equals the record's; $K$ contains neither $x_8$ nor the value of $a_4$; and the completed square of Section 3.25 is exactly $K/12$. The RESULT line prints the smallest possible value $576H^4/7$.

**In [23], Figure 03b.5: components that see $z$ and an invariant that does not.**

```python
# numerical functions of the 156 components with a4pp = 0 (true on the history
# a4 = A H x4); the second derivative of a4 is replaced by 0 before lambdify
riemann_functions = {k: numeric(v.subs(sp.Derivative(a4, (x4, 2)), 0))
                     for k, v in R_mixed.items()}
```

The 156 components as numerical functions of $(z, a_4, a_4', H)$, with $a_4'' = 0$, which holds on every linear history.

```python
def kretschmann_numbers(z_values, rate):
    """K at the points z_values, summed from the 156 numerical components."""
    total = np.zeros_like(z_values)
    for (a, b, c, d), f in riemann_functions.items():
        partner = riemann_functions.get((c, d, a, b))
        if partner is not None:
            total += f(z_values, 0.5, rate, 1.0) * partner(z_values, 0.5, rate, 1.0)
    return total
```

$K$ summed numerically at many values of $z$ at once, for a given rate $a_4'$ (with $a_4 = 0.5$, $H = 1$): each component times its partner with the pairs exchanged (`None` means that no partner was found; every component has one).

```python
z_line = np.linspace(0.02, np.pi / 2 - 0.02, 300)
cot_part = riemann_functions[(0, 3, 0, 7)](z_line, 0.5, 1.5, 1.0)  # a4p = 1.5
tan_part = riemann_functions[(0, 7, 0, 3)](z_line, 0.5, 1.5, 1.0)
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
fig.subplots_adjust(wspace=0.32)  # room for the label of the right vertical axis
```

300 values of $z$; the two components $R^{x_1x_4}{}_{x_1x_8} = Ha_4'\cot z$ (key `(0, 3, 0, 7)`) and $R^{x_1x_8}{}_{x_1x_4} = -Ha_4'\tan z$ (key `(0, 7, 0, 3)`) at $a_4' = 1.5$; a figure with two panels.

```python
axes[0].plot(z_line, np.abs(cot_part), color=RED, lw=1.8,
             label="$R^{x_1x_4}{}_{x_1x_8} = Ha_4^{\\prime}\\cot z$")
axes[0].plot(z_line, np.abs(tan_part), color=BLUE, lw=1.8, ls="--",
             label="minus $R^{x_1x_8}{}_{x_1x_4} = Ha_4^{\\prime}\\tan z$")
axes[0].plot(z_line, np.abs(cot_part * tan_part), color="black", lw=1.2, ls=":",
             label="minus their product $= H^2 a_4^{\\prime 2}$")
axes[0].plot(z_line, np.abs(np.broadcast_to(
    riemann_functions[(0, 7, 0, 7)](z_line, 0.5, 1.5, 1.0), z_line.shape)),
    color=AQUA, lw=1.8, ls="-.", label="minus $R^{x_1x_8}{}_{x_1x_8} = H^2$")
```

The left panel: the sizes of the two components, of their product, and of the constant plane component $R^{x_1x_8}{}_{x_1x_8} = -H^2$ (repeated to the length of `z_line` by `np.broadcast_to`).

```python
axes[0].set_yscale("log")
axes[0].set_xlabel("$z = 6 H x_8$ (radians)")
axes[0].set_ylabel("absolute value (unit $H^2$)")
axes[0].set_title("Riemann components, $a_4^{\\prime} = 1.5$")
axes[0].legend(fontsize=8)
rates = (0.5, 1.0, 1.5, 2.0)  # four expansion rates a4p = A H (A > 0), unit H
for rate, colour, style in zip(rates, (VIOLET, AQUA, RED, ORANGE),
                               ("-", "--", "-.", ":")):
    axes[1].plot(z_line, kretschmann_numbers(z_line, rate), color=colour, ls=style,
                 lw=1.8, label=f"$a_4^{{\\prime}} = {rate:g}\\,H$")
```

A logarithmic axis, labels, title and legend for the left panel. The right panel: $K$ summed numerically at the 300 points for four rates $a_4' = 0.5, 1, 1.5, 2$ (in units of $H$), each with its colour and line style.

```python
axes[1].set_yscale("log")
axes[1].set_xlabel("$z = 6 H x_8$ (radians)")
axes[1].set_ylabel("$K$ (unit $H^4$)")
axes[1].set_title("Kretschmann scalar summed from 156 components")
axes[1].legend(fontsize=8)
# the values of the formula for K at the four rates, for the caption and the check
K_values = [float(K.subs({a4p: r, a4pp: 0, H: 1})) for r in rates]
K_text = ", ".join(f"${k:g}$" for k in K_values)
```

The right panel's axis, labels, title and legend. `K_values` are the values of the formula for $K$ at the four rates, and `K_text` joins them with commas for the caption: $83.25$, $144$, $455.25$, $1332$ (from $12(7 - 2r^2 + 7r^4)$ with $H = 1$).

```python
save_figure(fig, "riemann_and_kretschmann_z",
            "Left: the absolute values of the Riemann components "
...
numbers = [kretschmann_numbers(z_line, r) for r in rates]
check(all(np.max(np.abs(n - k)) < 1e-9 * k for n, k in zip(numbers, K_values)),
      "summed numerically, K is the same at all 300 values of z and equals the "
      "formula")
```

The figure is saved; the check requires the numerical sum to equal the formula at all 300 points within a relative $10^{-9}$, for all four rates.

**What Figure 03b.5 shows.** Left: the red curve $Ha_4'\cot z$ falls by more than three powers of ten across the patch, the blue dashed curve $Ha_4'\tan z$ rises by as much; their product (dotted) is the constant $H^2a_4'^2 = 2.25$, and the plane component $H^2 = 1$ (dash-dotted) is constant too. Right: the four values of $K$ are four flat lines, $83.25$, $144$, $455.25$ and $1332$: although single components blow up at the ends of the patch, the invariant is the same at every $z$. The Kretschmann scalar therefore gives no sign of a singularity anywhere in the patch: the large components are an effect of the coordinates.

**In [24], Figure 03b.6: the curvature scalars along the history.**

```python
A = sp.symbols("A", real=True)  # the slope of the history a4 = A H x4
on_history = {a4p: A * H, a4pp: 0}
R_A = sp.factor(symbolic(R_scalar).subs(on_history))
K_A = sp.factor(K.subs(on_history))
RR_A = sp.factor(ricci_square.subs(on_history))
say(f"on the history: R = {R_A},  K = {K_A},  R^a_b R^b_a = {RR_A}")
check(all(sp.expand(f.subs(A, -A) - f) == 0 for f in (R_A, K_A, RR_A)),
      "the curvature scalars are even in A")
```

The slope $A$ as a symbol and the history $a_4' = AH$, $a_4'' = 0$ put into the three scalars. The output: $R = 6H^2(A^2 - 7)$, $K = 12H^4(7A^4 - 2A^2 + 7)$, $\sum R^a{}_bR^b{}_a = 36H^4(A^4 + 7)$. The check: all three are **even** in $A$ (replacing $A$ by $-A$ changes nothing), because they contain only $A^2$. These three numbers therefore cannot tell which of the two families of directions deflates; the metric and the components of the curvature can (Section 3.24).

```python
A_line = np.linspace(0.1, 3.0, 291)  # slopes 0.1, 0.11, ..., 3; A_line[90] = 1
R_numbers = sp.lambdify(A, R_A.subs(H, 1))(A_line)
K_numbers = sp.lambdify(A, K_A.subs(H, 1))(A_line)
RR_numbers = sp.lambdify(A, RR_A.subs(H, 1))(A_line)
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
```

291 slopes from $0.1$ to $3$ in steps of $0.01$ (position 90 is $A = 1$), all positive, so every history drawn deflates the extra times; the three scalars at these slopes with $H = 1$; a figure with two panels.

```python
axes[0].plot(A_line, R_numbers, color=VIOLET, lw=1.8, label="$R = 6H^2(A^2 - 7)$")
axes[0].axhline(0.0, color="black", lw=0.8)
axes[0].plot([np.sqrt(7)], [0.0], "o", color=VIOLET, ms=7)  # the zero of R
axes[0].set_ylabel("Ricci scalar $R$ (unit $H^2$)")
axes[0].set_title("Ricci scalar")
axes[1].plot(A_line, K_numbers, color=RED, lw=1.8, label="Kretschmann $K$")
axes[1].plot(A_line, RR_numbers, color=BLUE, lw=1.8, ls="--",
             label="$\\sum R^a{}_b R^b{}_a$")
axes[1].set_yscale("log")
axes[1].set_ylabel("value (unit $H^4$)")
axes[1].set_title("Squares of the curvature")
```

Left: $R$ against $A$, the zero line, and a dot at the zero $A = \sqrt 7$. Right, on a logarithmic axis: $K$ and $\sum R^a{}_bR^b{}_a$.

```python
for ax in axes:
    ax.axvline(1.0, color="grey", lw=1.0, ls=":")  # the canonical slope A = 1
    ax.set_xlabel("slope $A$ of the deflating history $a_4 = A H x_4$")
    ax.legend(fontsize=8, loc="upper left")
axes[0].text(1.05, -40, "$A = 1$", fontsize=9)
save_figure(fig, "scalars_versus_a",
            "The curvature scalars of the author's metric along the deflating "
...
check(abs(R_numbers[90] - (-36.0)) < 1e-9 and abs(K_numbers[90] - 144.0) < 1e-9,
      "at A = 1: R = -36 H^2 and K = 144 H^4")
```

A dotted vertical line at the canonical $A = 1$ in both panels, the axis label and legend, a label at the line; the figure is saved; the check confirms $R = -36$ and $K = 144$ at $A = 1$ (Section 3.25).

**What Figure 03b.6 shows.** Left: the Ricci scalar rises from $-42$ near $A = 0$ through $-36$ at $A = 1$ and crosses zero at $A = \sqrt 7 = 2.65$ (the dot). Right: $K$ (red) is smallest, $576/7 = 82.3$, near $A = 1/\sqrt 7 = 0.38$ and grows like $84A^4$ for large slopes; $\sum R^a{}_bR^b{}_a$ (blue dashed) starts at $252$ and grows like $36A^4$. Both stay far above zero: every deflating history is curved.

**In [25], Figure 03b.7: the Einstein tensor along the history.**

```python
G_A = [sp.factor(symbolic(G[k, k]).subs(on_history)) for k in range(8)]
for k in (0, 3, 4, 7):
    say(f"  on the history: G^{NAMES[k]}_{NAMES[k]} = {G_A[k]}")
bars = {value: [float(G_A[k].subs({A: value, H: 1})) for k in range(8)]
        for value in (1, 2)}
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
positions = np.arange(8)
```

The eight diagonal entries of $G$ on the history, factored; four of them are printed: $G^{x_1}{}_{x_1} = G^{x_5}{}_{x_5} = G^{x_8}{}_{x_8} = -3H^2(A^2 - 5)$ and $G^{x_4}{}_{x_4} = 3H^2(A^2 + 7)$. `bars` holds their values for $A = 1$ and $A = 2$ with $H = 1$.

```python
axes[0].bar(positions - 0.2, bars[1], width=0.38, color=RED, hatch="//",
            label="$A = 1$")
axes[0].bar(positions + 0.2, bars[2], width=0.38, color=BLUE, label="$A = 2$")
axes[0].set_xticks(positions, [f"$G^{{x_{k}}}{{}}_{{x_{k}}}$" for k in range(1, 9)],
                   fontsize=8)
axes[0].set_ylabel("component (unit $H^2$)")
axes[0].set_title("Diagonal of the Einstein tensor")
axes[0].legend(fontsize=8)
```

The left panel is a bar chart: `ax.bar(x, heights, width=...)` draws bars; the bars of $A = 1$ are shifted left by $0.2$ and hatched (`hatch="//"`), those of $A = 2$ shifted right, so that each pair stands side by side. The tick labels name the eight components.

```python
space_numbers = sp.lambdify(A, G_A[0].subs(H, 1))(A_line)
time_numbers = sp.lambdify(A, G_A[3].subs(H, 1))(A_line)
axes[1].plot(A_line, space_numbers, color=RED, lw=1.8,
             label="$G^{x_1}{}_{x_1} = G^{x_5}{}_{x_5} = G^{x_8}{}_{x_8}$")
axes[1].plot(A_line, time_numbers, color=VIOLET, lw=1.8, ls="--",
             label="$G^{x_4}{}_{x_4}$")
axes[1].fill_between(A_line, space_numbers, time_numbers, color="grey", alpha=0.2,
                     label="gap $6H^2(A^2 + 1) > 0$")
```

The right panel: the common 3-space, extra-time and hidden entry and the time entry against $A$; `fill_between` shades the gap between the two curves.

```python
axes[1].axhline(0.0, color="black", lw=0.8)
axes[1].axvline(1.0, color="grey", lw=1.0, ls=":")  # the canonical slope A = 1
axes[1].set_xlabel("slope $A$ of the deflating history $a_4 = A H x_4$")
axes[1].set_ylabel("component (unit $H^2$)")
axes[1].set_title("Einstein tensor versus $A$")
axes[1].legend(fontsize=8, loc="lower left")
save_figure(fig, "einstein_tensor",
            "The Einstein tensor $G^{\\mu}{}_{\\nu}$ of the author's metric along "
...
check(bars[1] == [12.0, 12.0, 12.0, 24.0, 12.0, 12.0, 12.0, 12.0]
      and bars[2] == [3.0, 3.0, 3.0, 33.0, 3.0, 3.0, 3.0, 3.0],
      "diagonal of G: 12 (24 for x4) at A = 1 and 3 (33 for x4) at A = 2, unit H^2")
```

The zero line, the line at $A = 1$, labels, title, legend; the figure is saved; the check confirms the two rows of bar heights.

**What Figure 03b.7 shows.** Left: for $A = 1$ seven bars of height $12$ and the time bar $24$; for $A = 2$ seven bars of height $3$ and the time bar $33$. Right: the common entry $3H^2(5 - A^2)$ falls and becomes negative beyond $A = \sqrt5 = 2.24$, the time entry $3H^2(7 + A^2)$ rises, and the shaded gap $6H^2(A^2 + 1)$ never closes: no cosmological constant, which adds the same number to every entry, can make all of them zero (Section 3.26).

**In [26], the source required by Einstein's equations, from the record.**

```python
A4_EQUATIONS = "Revision/field_equations_a4/a4-equations.json"
a4_equations = json.loads(repository_file(A4_EQUATIONS).read_text(encoding="utf-8"))
linear = a4_equations["linearMember"]  # the entry of the linear history
kappa = sp.symbols("kappa", positive=True)  # the constant of Einstein's equations
Lam = sp.symbols("Lam", real=True)  # the cosmological constant Lambda
source_names = {"AA": A, "H": H, "kappa": kappa, "Lam": Lam}
```

The record of the field equations of $a_4$ is read and its entry `linearMember` taken. $\kappa$ and $\Lambda$ become symbols; the dictionary says that the record's names `AA` and `Lam` mean $A$ and $\Lambda$.

```python
def source(key):
    """The record's text linear[key] (Mathematica notation) as sympy."""
    return parse_expr(linear[key]["input"].replace("^", "**"),
                      local_dict=source_names)


rho_record, p_record = source("rhoEinstein"), source("pEinstein")
sum_record = source("rhoPlusPEinstein")  # rho + p
say(f"record: kappa rho       = {sp.expand(kappa * rho_record)}")
say(f"record: kappa p         = {sp.expand(kappa * p_record)}")
say(f"record: kappa (rho + p) = {sp.factor(kappa * sum_record)}")
```

`source` reads the Mathematica text (key `"input"`) of an entry as a sympy expression. The three texts are read and printed multiplied by $\kappa$: $\kappa\rho = -3A^2H^2 - 21H^2 - \Lambda$, $\kappa p = -3A^2H^2 + 15H^2 + \Lambda$, $\kappa(\rho + p) = -6H^2(A^2 + 1)$.

```python
check(sp.expand(kappa * rho_record - (-G_A[3] - Lam)) == 0,
      "kappa rho of the record equals -G^x4_x4 - Lambda",
      record=f"{A4_EQUATIONS}, linearMember.rhoEinstein (and "
             "python-a4-report.json, check json_linear_member)")
check(all(sp.expand(kappa * p_record - (G_A[k] + Lam)) == 0 for k in (0, 4, 7)),
      "kappa p of the record equals G^x1_x1, G^x5_x5 and G^x8_x8 plus Lambda",
      record=f"{A4_EQUATIONS}, linearMember.pEinstein")
check(sp.expand(kappa * sum_record - (G_A[0] - G_A[3])) == 0,
      "kappa (rho + p) of the record equals G^x1_x1 - G^x4_x4 = -6 (A^2 + 1) H^2",
      record=f"{A4_EQUATIONS}, linearMember.rhoPlusPEinstein")
```

Three checks, the three lines of Section 3.26: $\kappa\rho = -G^{x_4}{}_{x_4} - \Lambda$; $\kappa p = G^{x_1}{}_{x_1} + \Lambda = G^{x_5}{}_{x_5} + \Lambda = G^{x_8}{}_{x_8} + \Lambda$; and $\kappa(\rho + p) = G^{x_1}{}_{x_1} - G^{x_4}{}_{x_4}$.

**In [27], the negative control.**

```python
g_control = g.copy()
for k in (4, 5, 6):  # the three extra times, now inflating
    g_control[k, k] = -sp.exp(2 * a4) * sp.sin(6 * H * x8) ** sp.Rational(1, 3)
Gamma_control = christoffel(g_control, X)
R_control = raise_second(riemann(Gamma_control, X), g_control)
Ric_control = ricci(R_control, 8)
G_control = (Ric_control - Ric_control.trace() / 2 * sp.eye(8)).applyfunc(tidy)
```

A check that cannot fail teaches nothing, so the metric is changed on purpose: `g.copy()` is a copy of the author's metric, and its three extra-time entries are replaced by $-e^{+2a_4}\sin^{1/3}z$, extra times that INFLATE like 3-space. This is NOT the author's metric. The curvature is computed again with the same functions, up to the Einstein tensor. This cell runs for up to half a minute.

```python
off = {(i, j): plain(G_control[i, j]) for i in range(8) for j in range(8)
       if i != j and G_control[i, j] != 0}
for (i, j), value in sorted(off.items()):
    say(f"  control: G^{NAMES[i]}_{NAMES[j]} = {value}")
check(sorted(off) == [(3, 7), (7, 3)] and all(v.has(z) for v in off.values()),
      "negative control: with inflating extra times G^x4_x8 and G^x8_x4 are not "
      "zero and depend on z")
```

The entries off the diagonal that are not zero are collected and printed: $G^{x_4}{}_{x_8} = 6Ha_4'/\tan z$ and $G^{x_8}{}_{x_4} = -6Ha_4'\tan z$, exactly as derived by hand in Section 3.25. The check requires these two and only these two, and that both depend on $z$. With the author's deflating extra times they are zero (In [20]): the deflation of the extra times is what makes the Einstein tensor of the author's metric diagonal.

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

The seven figure files must exist; the last line prints ALL 39 CHECKS PASSED (notebook 03b). The 39 checks are: 1 in In [4], 1 in In [6], 2 in In [7], 1 each in In [8] and In [9], 2 in In [10], 1 in In [11], 2 in In [12], 1 in In [13], 3 in In [14], 2 each in In [15] and In [16], 1 each in In [17], In [18] and In [19], 4 in In [20], 1 in In [21], 3 in In [22], 1 in In [23], 2 in In [24], 1 in In [25], 3 in In [26], and 1 each in In [27] and In [28].

### 3.31 Free fall in the author's metric

What does the author's metric do to a body that moves in it with no force acting on it, only the geometry? This section answers with the geodesic equation of Section 3.16 and the Christoffel symbols of Section 3.23.

**Test particles in free fall.** A **test particle** is a body so small that it does not change the metric (ASSUMED: the particles of this section are test particles). In free fall it moves on a time-like geodesic (Section 3.16; ASSUMED from the theory of gravity), parametrised by its proper time $\tau$, with the velocity $u^a = dx^a/d\tau$ and $g(u, u) = -1$. We keep the labels of Section 3.23: $i$ for 3-space, $j$ for the extra times, $k$ for any of these six transverse directions.

**The geodesic equations.** $du^a/d\tau = -\sum_{b,c}\Gamma^a{}_{bc}u^bu^c$ with the 37 symbols of Section 3.23 (a symbol with two different lower indices appears twice, once in each order, hence the factors 2):

$$
\frac{du^i}{d\tau} = -2a_4'\,u^iu^4 - 2H\cot z\,u^iu^8, \qquad \frac{du^j}{d\tau} = +2a_4'\,u^ju^4 - 2H\cot z\,u^ju^8,
$$

$$
\begin{aligned}
\frac{du^4}{d\tau} &= -a_4'\sum_i h_i^2(u^i)^2 - a_4'\sum_j h_j^2(u^j)^2,\\
\frac{du^8}{d\tau} &= H\tan z\sum_i h_i^2(u^i)^2 - H\tan z\sum_j h_j^2(u^j)^2 + 6H(\tan z + \cot z)(u^8)^2
\end{aligned}
$$

(for $u^i$ the symbols $\Gamma^i{}_{i4} = a_4'$ and $\Gamma^i{}_{i8} = H\cot z$; for $u^j$ the symbols $\Gamma^j{}_{j4} = -a_4'$ and $\Gamma^j{}_{j8} = H\cot z$; for $u^4$ the symbols $\Gamma^4{}_{kk} = a_4'h_k^2$; for $u^8$ the symbols $\Gamma^8{}_{ii} = -H\tan z\,h_i^2$, $\Gamma^8{}_{jj} = +H\tan z\,h_j^2$ and $\Gamma^8{}_{88} = -6H(\tan z + \cot z)$; each moved to the right side with its minus sign). Together with $dx^a/d\tau = u^a$ these are 16 first-order equations for the 8 coordinates and the 8 velocities.

**Six conserved momenta.** The metric does not depend on the six transverse coordinates, so by Section 3.16 the six **momenta** $p_k = g_{kk}u^k$ (no sum) do not change during free fall:

$$
p_i = h_i^2\,u^i, \qquad p_j = -h_j^2\,u^j \qquad\text{(both constant)}
$$

(PROVED in Section 3.16 for every diagonal metric that does not depend on $x_k$; Notebook 03d proves it again with sympy for all six, for a general $a_4(x_4)$, In [4]). The squared speed $g(u, u)$ is conserved too (Section 3.16).

**Frame velocities: redshift in 3-space, blueshift along the extra times.** An observer at rest at the particle's place measures lengths and durations with the frame of Section 3.7. Per unit of the particle's proper time, the particle covers along $x_a$ the proper length (along an extra time, the proper duration) $\hat u^a = h_au^a$, its **frame velocity**. From the momenta:

$$
\hat u^i = h_iu^i = \frac{p_i}{h_i} = p_i\,e^{-a_4}\sin^{-1/6}z, \qquad \hat u^j = h_ju^j = -\frac{p_j}{h_j} = -p_j\,e^{a_4}\sin^{-1/6}z
$$

(divide the momentum by the scale factor; $1/h_i = e^{-a_4}\sin^{-1/6}z$ and $1/h_j = e^{a_4}\sin^{-1/6}z$). With $\sin^{1/6}z = e^{Hy}$ (Section 3.9):

$$
\hat u^i = p_i\,e^{-Hy - a_4}, \qquad \hat u^j = -p_j\,e^{a_4 - Hy} .
$$

At a fixed height $y$, along a deflating history ($a_4$ increasing), the frame velocity in 3-space falls like $e^{-a_4}$: motion in 3-space is **redshifted**, because 3-space inflates and stretches it out. The frame velocity along an extra time grows like $e^{a_4}$: motion along the extra times is **blueshifted**, because they deflate. The factor $e^{-Hy - a_4}$ is exactly the **momentum weight** $\kappa(y, x_4) = e^{-Hy - a_4(x_4)}$ that the Revision Kohn-Sham record uses to turn a conserved 3-space momentum into the momentum seen at height $y$ and time $x_4$ (`Revision/kohn_sham/ks-theory.json`, key `geometry.kappa`; PROVED here; Notebook 03d, In [5]).

**The push along the hidden direction.** Write $S = \sum_i(\hat u^i)^2$ and $E = \sum_j(\hat u^j)^2$ for the squared frame velocities in 3-space and along the extra times. The frame velocity along the hidden direction is $\hat u^8 = h_8u^8 = \cot z\,u^8$, and it equals $dy/d\tau$, because $dy/d\tau = (dy/dx_8)(dx_8/d\tau) = \cot z\,u^8$ (Section 3.9). Its rate of change, line by line:

$$
\frac{d\hat u^8}{d\tau} = \frac{d\cot z}{d\tau}\,u^8 + \cot z\,\frac{du^8}{d\tau}
$$

(the product rule)

$$
= -\frac{6H}{\sin^2 z}\,(u^8)^2 + \cot z\Bigl[H\tan z\,(S - E) + 6H(\tan z + \cot z)(u^8)^2\Bigr]
$$

($d\cot z/d\tau = -\frac{1}{\sin^2 z}\cdot 6H\cdot u^8$ by the chain rule; the geodesic equation for $u^8$ with $h_i^2(u^i)^2 = (\hat u^i)^2$ and $h_j^2(u^j)^2 = (\hat u^j)^2$)

$$
= -\frac{6H}{\sin^2 z}(u^8)^2 + H(S - E) + 6H\bigl(1 + \cot^2 z\bigr)(u^8)^2 = H(S - E)
$$

($\cot z\tan z = 1$; $1 + \cot^2 z = 1/\sin^2 z$, so the two terms with $(u^8)^2$ cancel). Hence

$$
\frac{d^2y}{d\tau^2} = H\Bigl(\sum_i(\hat u^i)^2 - \sum_j(\hat u^j)^2\Bigr) .
$$

Motion in 3-space pushes the particle towards the patch end ($y$ grows); motion along an extra time pushes it towards the tip ($y$ falls). A particle at rest feels no push (PROVED; Notebook 03d, In [6]).

**The slowing of $x_4$.** The geodesic equation for $u^4$, written with frame velocities, is

$$
\frac{du^4}{d\tau} = -a_4'\Bigl(\sum_i(\hat u^i)^2 + \sum_j(\hat u^j)^2\Bigr) = -a_4'(S + E)
$$

(again $h_k^2(u^k)^2 = (\hat u^k)^2$). Along a deflating history, $a_4' > 0$, the $x_4$ velocity can never increase, and it decreases whenever the particle moves in a transverse direction (PROVED; Notebook 03d, In [6]).

**The $x_4$ velocity from the squared speed.** The squared speed, written with frame velocities, is

$$
g(u, u) = \sum_i h_i^2(u^i)^2 - (u^4)^2 - \sum_j h_j^2(u^j)^2 + h_8^2(u^8)^2 = S - (u^4)^2 - E + (\hat u^8)^2
$$

(the diagonal entries $+h_i^2$, $-1$, $-h_j^2$, $+h_8^2$ of the metric). Setting it equal to $-1$ and solving for $(u^4)^2$:

$$
(u^4)^2 = 1 + \sum_i(\hat u^i)^2 - \sum_j(\hat u^j)^2 + (\hat u^8)^2 = 1 + S - E + (\hat u^8)^2
$$

(PROVED; Notebook 03d, In [6]).

**No turning without extra-time motion; turning with it.** A particle with no extra-time motion at the start has $p_j = 0$, so $\hat u^j = 0$ for ever (the momenta are conserved), and $(u^4)^2 = 1 + S + (\hat u^8)^2 \ge 1$: $u^4$ never reaches zero, keeps its sign, and $x_4$ keeps advancing. A particle that moves along an extra time is different: its $E$ grows by the blueshift, and $(u^4)^2$ can reach zero. There $u^4 = 0$, the **turning point**; since $du^4/d\tau = -a_4'(S + E) < 0$ there, $u^4$ becomes negative and $x_4$ decreases afterwards. With four time-like directions, a time-like path need not keep advancing in the chosen time $x_4$ (PROVED; computed in Notebook 03d, In [11]). At the turning point of a particle that moves only along $x_5$ and $y$, the formula gives $(\hat u^5)^2 - (\hat u^8)^2 = 1$.

**The same quadratic form as the plane waves of the Revision record.** Multiply the last formula by $m^2$, the squared mass of the particle, and write $k_a = m\hat u^a$ for its frame momenta and $\mathcal E = m u^4$ for its energy:

$$
\mathcal E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 - k_5^2 - k_6^2 - k_7^2 + k_8^2 .
$$

The Revision scope report finds exactly this expression for the squared frequency of plane waves of the fields of the book in flat 4+4 space (or with the coefficients of the field equation frozen at one instant): a wave with the momenta $k_a$ has $\mathcal E^2$ equal to it, and when the extra-time momentum is so large that $\mathcal E^2 < 0$ the frequency is imaginary and the wave grows exponentially in $x_4$, with a rate that has no upper bound (`Revision/theory/reports/python-scope.json`, check `extra_time_growth_rates_unbounded`; Chapter 8 studies this). The identity of the two quadratic forms is PROVED (Notebook 03d, In [7]). A particle can never be where $\mathcal E^2 < 0$, because $(u^4)^2 \ge 0$; where a plane wave would start to grow, the particle reaches its turning point instead. Whether wave packets of the fields follow these geodesics in the curved metric is NOT computed in this book: **OPEN**.

**The good sector.** The Revision Kohn-Sham work keeps only states that do not depend on $x_5, x_6, x_7$: their extra-time momenta are zero (`Revision/kohn_sham/ks-theory.json`, key `sectorAndAnsatz.sector`: "good sector: no dependence on x5, x6, x7 (extra-time momenta zero)"). The particle with the same property, $p_j = 0$, is the one that never turns. The reason for this choice of the record comes from the quantum theory (Chapter 10).

**Numbers along the history (COMPUTED by Notebook 03d).** With the history of the record ($A = 1$, $H = 1$, so $a_4 = x_4$; ASSUMED, a prescribed background, Section 3.8), RK4 with the step $\Delta\tau = 0.001$, all particles starting at $x_4 = 0$ and $y = -1$ ($z = \arcsin e^{-6} = 0.002479$): a particle at rest stays at rest with $x_4 = \tau$ (In [9]). Three particles started along $x_1$ with the frame velocities $0.25$, $0.5$ and $1$ keep $p_1$ and $g(u, u)$ constant within a relative $10^{-9}$, their frame velocity equals $p_1\kappa(y, x_4)$ within $10^{-9}$, and $u^4$ falls at every step; the fastest has at $\tau = 3$ the values $x_4 = 3.3070$, $\hat u^1 = 0.014370$, $u^4 = 1.060733$ and $y = -0.0643$: it has slowed down by redshift and risen towards the patch end (In [10]). A particle started along $x_5$ with $\hat u^5 = 0.2$ reaches its turning point at $\tau = 1.987$, where $x_4$ is largest, $1.4864$, with $\hat u^5 = 1.4013$ and $\hat u^8 = -0.9817$ (it has sunk towards the tip), and $x_4$ decreases afterwards (In [11]). The numerical acceleration of $y$ agrees with the push law within $3.4 \times 10^{-6}$ (In [14]), and halving the RK4 step divides the error by 16.2 to 17.2, the order 4 of RK4 (In [16]).

### 3.32 Example: free fall in the author's metric

Notebook 03d reads the 25 Christoffel symbols of the record, builds the geodesic equations, and proves with sympy, for a general $a_4(x_4)$, the conservation of the six momenta and of $g(u, u)$, the momentum weight $\kappa$ of the Kohn-Sham record, the push law, the slowing of $x_4$, the formula for $(u^4)^2$, and its identity with the quadratic form of the record's plane-wave check. Then it integrates five paths with RK4 along the history of the record, checks every exact law on the computed paths, finds the turning point of the particle that moves along an extra time, measures the order of RK4, and draws five figures. It needs no Rust, runs in about 50 seconds and ends with the line ALL 23 CHECKS PASSED (notebook 03d).

<!-- NOTEBOOK 03d -->

### 3.35 Line-by-line walk-through of Notebook 03d

The notebook has 17 code cells, In [1] to In [17]. The conventions of the earlier walk-throughs apply (a line `...` in a quoted figure command stands for the rest of the caption, printed in full in Section 3.34).

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 3.33. Its code is, line for line, the set-up code of Notebook 03a explained in Section 3.13 under In [1], with the single difference `NOTEBOOK_ID = "03d"  # this notebook: chapter 03, example d`. It prints Set-up of notebook 03d complete: repository folder found, helpers defined.

**In [2], every result in one piece.** Word for word In [2] of Notebook 03a (Section 3.13). It prints From now on check and report print each of their results in one piece.

**In [3], the Christoffel symbols of the record.**

```python
import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols
from sympy.parsing.sympy_parser import parse_expr  # text -> sympy expression

CURVATURE_RECORD = "Revision/gkd_lovelock/results/curvature.json"
record = json.loads(repository_file(CURVATURE_RECORD).read_text(encoding="utf-8"))
NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
X = sp.symbols("x1:9", real=True)  # the coordinates x1 ... x8 (X[0] ... X[7])
x4, x8 = X[3], X[7]
```

The packages, the record of the curvature computation, the names of the coordinates, and the eight coordinates as the tuple `X` (a tuple is a list that cannot be changed); `x4` and `x8` name its positions 3 and 7.

```python
H = sp.symbols("H", positive=True)  # the constant of the author
a4 = sp.Function("a4")(x4)  # the metric function, any function of x4
a4p, a4v = sp.symbols("a4p a4v", real=True)  # printing names: a4 prime, a4
record_names = {"a4p": a4p, "a4v": a4v, "H": H, "x8": x8, "E": sp.E,
                "sin": sp.sin, "cot": sp.cot}
```

$H > 0$, the function $a_4(x_4)$, the plain symbols `a4p` and `a4v`, and the dictionary of names for reading the record (as in Notebook 03b, Section 3.30, In [5]).

```python
def from_mathematica(entry_text):
    """A value of the record (Mathematica notation) as a sympy expression."""
    t = entry_text.replace("Derivative[1][a4][x4]", "a4p").replace("a4[x4]", "a4v")
    t = t.replace("Sin[6*H*x8]", "sin(6*H*x8)").replace("Cot[6*H*x8]", "cot(6*H*x8)")
    t = t.replace("^", "**")
    if "[" in t or "]" in t:  # a piece of notation that was not translated
        raise ValueError(f"cannot translate {entry_text}")
    return parse_expr(t, local_dict=record_names)
```

The translation of a record entry into sympy, the same as in Notebook 03b but without $a_4''$, which no Christoffel symbol contains.

```python
Gamma = {}  # (a, b, c) -> the value of Gamma^a_bc, with a4p and a4v
for entry in record["christoffelNonzero_b_le_c"]:
    a, b, c = (NAMES.index(entry[key]) for key in ("a", "b", "c"))
    Gamma[(a, b, c)] = from_mathematica(entry["value"])
    Gamma[(a, c, b)] = Gamma[(a, b, c)]  # the same symbol with b and c exchanged
```

The dictionary `Gamma` holds the symbols. For each of the 25 entries of the record, the three names of `a`, `b`, `c` become positions (the expression in round brackets produces three numbers, which are unpacked into `a, b, c`), the value is translated, and it is stored under both orders of the lower indices. For the 13 entries with $b = c$ both keys are the same, so the 25 entries give $13 + 2 \times 12 = 37$ keys.

```python
for key in [(0, 0, 3), (3, 4, 4), (7, 0, 0), (7, 7, 7)]:
    a, b, c = key
    say(f"  Gamma^{NAMES[a]}_({NAMES[b]} {NAMES[c]}) = {Gamma[key]}")
report("entries of the record (b <= c)", len(record["christoffelNonzero_b_le_c"]))
check(len(record["christoffelNonzero_b_le_c"]) == 25 and len(Gamma) == 37,
      "the 25 entries of the record give 37 non-zero Christoffel symbols",
      record=f"{CURVATURE_RECORD}, christoffelNonzero_b_le_c")
```

Four symbols are printed in the record's own form, because the translation does not simplify:

```text
a4p
a4p*exp(-2*a4v)*sin(6*H*x8)**(1/3)
-H*exp(2*a4v)*sin(6*H*x8)**(1/3)/cot(6*H*x8)
-6*H*cot(6*H*x8) - 6*H/cot(6*H*x8)
```

They are $\Gamma^{x_1}{}_{x_1x_4} = a_4'$, $\Gamma^{x_4}{}_{x_5x_5} = a_4'e^{-2a_4}\sin^{1/3}z$, $\Gamma^{x_8}{}_{x_1x_1} = -H\tan z\,e^{2a_4}\sin^{1/3}z$ and $\Gamma^{x_8}{}_{x_8x_8} = -6H(\cot z + \tan z)$ (Section 3.23). The RESULT line prints 25, and the check confirms the counts 25 and 37.

**In [4], what stays constant (exact).**

```python
u = sp.symbols("u1:9", real=True)  # the velocity components u^1 ... u^8
to_function = {a4p: sp.Derivative(a4, x4), a4v: a4}  # back to the function a4(x4)
acceleration = [sp.S(0)] * 8  # du^a/dtau from the geodesic equation
for (a, b, c), value in Gamma.items():
    acceleration[a] -= value.subs(to_function) * u[b] * u[c]
```

The eight velocity components $u^1, \dots, u^8$ as symbols. `to_function` turns the plain symbols back into the derivative and the value of the function $a_4(x_4)$, so that sympy can differentiate along the path. `acceleration` starts as eight zeros (`sp.S(0)` is sympy's zero); the loop subtracts $\Gamma^a{}_{bc}u^bu^c$ for every one of the 37 keys, which is the geodesic equation $du^a/d\tau = -\sum_{b,c}\Gamma^a{}_{bc}u^bu^c$ (the two orders of the lower indices are both in the dictionary, so the factors 2 of Section 3.31 appear by themselves).

```python
def along_path(f):
    """The rate of change df/dtau of f(x, u) along a path of free fall."""
    return sum(sp.diff(f, X[k]) * u[k] + sp.diff(f, u[k]) * acceleration[k]
               for k in range(8))
```

The rate of change of a quantity $f(x, u)$ along a path of free fall, by the chain rule: $df/d\tau = \sum_a(\partial f/\partial x^a)\,u^a + \sum_a(\partial f/\partial u^a)\,du^a/d\tau$, with $du^a/d\tau$ from the geodesic equation.

```python
warp = sp.sin(6 * H * x8) ** sp.Rational(1, 6)  # sin(z)^(1/6), z = 6 H x8
h = [sp.exp(a4) * warp] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * warp] * 3 \
    + [sp.cot(6 * H * x8)]  # the eight scale factors h_a
ETA = [1, 1, 1, -1, -1, -1, -1, 1]  # the signs of the metric entries
g = [ETA[k] * h[k] ** 2 for k in range(8)]  # the diagonal of the metric
say(f"du1/dtau = {sp.factor(acceleration[0]).subs(sp.Derivative(a4, x4), a4p)}")
```

The warp factor, the eight scale factors (Section 3.7), the signs, and the diagonal $g_{aa} = \eta_{aa}h_a^2$. The printed line is the geodesic equation for $u^1$, factored: `-2*u1*(H*u8*cot(6*H*x8) + a4p*u4)`, the first equation of Section 3.31.

```python
momenta = {k: g[k] * u[k] for k in (0, 1, 2, 4, 5, 6)}  # p_a = g_aa u^a
rates = [sp.simplify(along_path(p)) for p in momenta.values()]
check(rates == [0] * 6,
      "the six momenta of x1, x2, x3, x5, x6, x7 are conserved in free fall")
squared_length = sum(g[k] * u[k] ** 2 for k in range(8))  # g(u, u)
check(sp.simplify(along_path(squared_length)) == 0,
      "the squared length g(u, u) of the velocity is conserved in free fall")
```

The six momenta $p_k = g_{kk}u^k$; their rates along the path simplify to zero (first check). The squared speed $g(u, u) = \sum_a g_{aa}(u^a)^2$; its rate simplifies to zero (second check). Both hold for every function $a_4(x_4)$.

**In [5], the momentum weight of the Kohn-Sham record.**

```python
KS_THEORY = "Revision/kohn_sham/ks-theory.json"
ks_theory = json.loads(repository_file(KS_THEORY).read_text(encoding="utf-8"))
say("record, geometry.kappa: " + ks_theory["geometry"]["kappa"])
y_of_x8 = sp.log(sp.sin(6 * H * x8)) / (6 * H)  # the hidden coordinate y
kappa = sp.exp(-H * y_of_x8 - a4)  # the record's e^{-Hy - a4(x4)}
```

The Kohn-Sham theory record is read and its statement about the momentum weight printed: kappa(y, x4) = e^{-Hy - a4(x4)} (the momentum weight). Then $y$ as a function of $x_8$ (Section 3.9) and the weight $\kappa = e^{-Hy - a_4}$.

```python
check(sp.simplify(1 / h[0] - kappa) == 0,
      "1/h1 = e^(-H y - a4): the frame velocity in 3-space is p1 times kappa",
      record=f"{KS_THEORY}, geometry.kappa")
check(sp.simplify(1 / h[4] - sp.exp(a4 - H * y_of_x8)) == 0,
      "1/h5 = e^(a4 - H y): the frame velocity along an extra time grows with a4")
```

Two checks of Section 3.31: $1/h_1 = \kappa$, so $\hat u^1 = p_1/h_1 = p_1\kappa$; and $1/h_5 = e^{a_4 - Hy}$, so $\hat u^5 = -p_5e^{a_4 - Hy}$.

**In [6], the push, the slowing, and $(u^4)^2$ (exact).**

```python
frame = [h[k] * u[k] for k in range(8)]  # the frame velocities u-hat^a = h_a u^a
space_squared = sum(frame[k] ** 2 for k in (0, 1, 2))  # 3-space part
extra_squared = sum(frame[k] ** 2 for k in (4, 5, 6))  # extra-time part
push = along_path(frame[7]) - H * (space_squared - extra_squared)
check(sp.simplify(push) == 0,
      "d^2y/dtau^2 = H (3-space frame velocity squared - extra-time one squared)")
```

The frame velocities $\hat u^a = h_au^a$, the sums $S$ and $E$ of Section 3.31, and the difference between the rate of $\hat u^8 = dy/d\tau$ and the push law $H(S - E)$, which simplifies to zero.

```python
slowing = along_path(u[3]) + sp.diff(a4, x4) * (space_squared + extra_squared)
check(sp.simplify(slowing) == 0,
      "du4/dtau = -a4' times the sum of the six transverse frame velocities squared")
in_frame = space_squared - u[3] ** 2 - extra_squared + frame[7] ** 2
check(sp.simplify(squared_length - in_frame) == 0,
      "g(u, u) written with the frame velocities")
```

The law $du^4/d\tau = -a_4'(S + E)$, and $g(u, u) = S - (u^4)^2 - E + (\hat u^8)^2$, both checked exactly.

**In [7], the quadratic form of the plane-wave check.**

```python
SCOPE = "Revision/theory/reports/python-scope.json"
scope = json.loads(repository_file(SCOPE).read_text(encoding="utf-8"))
growth = next(entry for entry in scope["checks"]
              if entry["name"] == "extra_time_growth_rates_unbounded")
form_text = growth["detail"].split("h_k^2 = (")[1].split(") I16")[0]  # the formula
say(f"record ({growth['verdict']}): E^2 = {form_text}")
```

The scope report is read and its check `extra_time_growth_rates_unbounded` taken from its list of checks. Its text contains the piece `h_k^2 = (` followed by the quadratic form and `) I16` (times the $16 \times 16$ unit matrix); the two `split` calls cut out the form between them. The output prints `PASS` and the form $k_1^2 + k_2^2 + k_3^2 - k_5^2 - k_6^2 - k_7^2 + k_8^2 + m^2$.

```python
k = sp.symbols("k1:9", real=True)  # frame momenta k1 ... k8 (k4 is not used)
m = sp.symbols("m", positive=True)  # the mass
form = parse_expr(form_text, local_dict={**{f"k{n}": k[n - 1] for n in range(1, 9)},
                                         "m": m})
U = sp.symbols("U1:9", real=True)  # the frame velocities as plain symbols
particle = m ** 2 * (1 + U[0] ** 2 + U[1] ** 2 + U[2] ** 2 - U[4] ** 2 - U[5] ** 2
                     - U[6] ** 2 + U[7] ** 2)  # m^2 (u^4)^2 from section 8
```

The form is read with the momenta $k_1, \dots, k_8$ and the mass $m$ as symbols; `{**{...}, "m": m}` builds one dictionary from a dictionary comprehension (unpacked by `**`) and one more entry. `particle` is $m^2(u^4)^2$ from the formula of Section 3.31, with the frame velocities as plain symbols $U$.

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
status = ks_theory["adiabaticity"]["historyStatus"]
say(f"H = {H_value}, A = {A_value}; record: " + status.split(". ")[0] + ".")
```

The module `math` computes functions of single numbers, faster than numpy for one number at a time. The parameters of the Revision Kohn-Sham solver give $H = 1$ and the slope $A = 1$; the first sentence of the record's statement on the status of the history is printed: PRESCRIBED BACKGROUND: the history a4 = A H x4 is prescribed, not solved for.

```python
check(H_value == 1.0 and A_value == 1.0 and status.startswith("PRESCRIBED BACKGROUND"),
      "the history of the record: a4 = A H x4 with A = 1, H = 1, prescribed",
      record=f"{PARAMETERS}, physics.H and physics.historyA; {KS_THEORY}, "
             "adiabaticity.historyStatus")
ARGUMENTS = (a4v, a4p, x8, H)
gamma_numbers = [(a, b, c, sp.lambdify(ARGUMENTS, value, "math"))
                 for (a, b, c), value in sorted(Gamma.items())]
ETA_N = np.array(ETA, dtype=float)  # the signs as numbers
```

The check confirms the history and its status. `gamma_numbers` is a list of the 37 symbols as fast numerical functions of $(a_4, a_4', x_8, H)$, each with its three indices (`"math"` makes functions of single numbers). `ETA_N` holds the signs as floating-point numbers.

```python
def free_fall(state):
    """d state/d tau for state = (x1..x8, u1..u8) on the history a4 = A H x4."""
    x, v = state[:8], state[8:]
    a4_now, rate = A_value * H_value * x[3], A_value * H_value  # a4 and a4'
    change = np.zeros(8)
    for a, b, c, f in gamma_numbers:  # du^a/dtau = - sum Gamma^a_bc u^b u^c
        change[a] -= f(a4_now, rate, x[7], H_value) * v[b] * v[c]
    return np.concatenate([v, change])
```

The right side of the 16 equations: the state holds the 8 coordinates (`state[:8]`) and the 8 velocities (`state[8:]`). On the history, $a_4 = AHx_4$ and $a_4' = AH$. The accelerations are summed over the 37 symbols, and the function returns the derivatives of the state: the velocities, then the accelerations (`np.concatenate` joins two arrays).

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

The RK4 method of Chapter 2 (the same as in Notebook 03c, Section 3.22, In [8]) for the 16 unknowns, from $\tau = 0$ to `tau_end` in `steps` equal steps; it returns the times and the table of states.

```python
def scale_numbers(x):
    """The eight scale factors h_a at the point x on the history (numbers)."""
    a4_now, z_now = A_value * H_value * x[3], 6 * H_value * x[7]
    w = math.sin(z_now) ** (1 / 6)  # the warp factor sin(z)^(1/6)
    return np.array([math.exp(a4_now) * w] * 3 + [1.0]
                    + [math.exp(-a4_now) * w] * 3 + [1 / math.tan(z_now)])
```

The eight scale factors as numbers at a point on the history.

```python
def start(y0, frame_velocity):
    """The state at tau = 0: x4 = 0, y = y0, frame velocities as given (the entry
    for x4 is replaced by the value that makes g(u, u) = -1)."""
    x = np.zeros(8)
    x[7] = math.asin(math.exp(6 * H_value * y0)) / (6 * H_value)  # sin z = e^(6Hy)
    w = np.array(frame_velocity, dtype=float)
    w[3] = 0.0
    w[3] = math.sqrt(1.0 + np.sum(ETA_N * w ** 2))  # (u^4)^2 = 1 + sum eta w^2
    return np.concatenate([x, w / scale_numbers(x)])  # u^a = u-hat^a / h_a
```

The starting state: all coordinates zero except $x_8$, which is set from the height $y_0$ by $\sin z = e^{6Hy_0}$. The frame velocities are given; the entry for $x_4$ is first set to zero, and then to $\sqrt{1 + \sum_a\eta_{aa}(\hat u^a)^2}$, which is the formula $(u^4)^2 = 1 + S - E + (\hat u^8)^2$ of Section 3.31, so that $g(u, u) = -1$. The velocities are $u^a = \hat u^a/h_a$.

```python
def describe(states):
    """Frame velocities (rows), the coordinate y and g(u, u) along a path."""
    h_rows = np.array([scale_numbers(s[:8]) for s in states])
    frame_rows = h_rows * states[:, 8:]
    y_values = np.log(np.sin(6 * H_value * states[:, 7])) / (6 * H_value)
    lengths = np.sum(ETA_N * frame_rows ** 2, axis=1)  # g(u, u)
    return frame_rows, y_values, lengths, h_rows
```

For every computed state: the scale factors, the frame velocities $\hat u^a = h_au^a$ (a product of two tables entry by entry), the height $y$, and $g(u, u) = \sum_a\eta_{aa}(\hat u^a)^2$ (`axis=1` sums along each row).

```python
Y0 = -1.0  # the starting height of every particle
say(f"start: y0 = {Y0}, z0 = {math.asin(math.exp(6 * Y0)):.6f}")
```

Every particle starts at $y = -1$, that is $z = \arcsin e^{-6} = 0.002479$, as printed.

**In [9], the particle at rest.**

```python
tau, rest = rk4_path(start(Y0, [0.0] * 8), 3.0, 3000)
others = [0, 1, 2, 4, 5, 6, 7]  # every coordinate except x4
moved = np.max(np.abs(rest[:, others] - rest[0, others]))
check(moved == 0.0 and np.max(np.abs(rest[:, 3] - tau)) < 1e-12
      and np.max(np.abs(rest[:, 11] - 1.0)) < 1e-12,
      "the particle at rest stays at rest and x4 equals its proper time")
```

A particle with all frame velocities zero (so $u^4 = 1$) is followed from $\tau = 0$ to $3$ in 3000 steps. `rest[:, others]` is the table of the seven other coordinates; their largest change is exactly zero, because every acceleration contains a factor $u^bu^c$ with a zero velocity (no symbol $\Gamma^a{}_{x_4x_4}$ exists, Section 3.23). The check also requires $x_4 = \tau$ and $u^4 = 1$ (column 11 of a state is $u^4$: 8 coordinates come first) within $10^{-12}$.

**In [10], three particles moving in 3-space.**

```python
SPEEDS = (0.25, 0.5, 1.0)  # starting frame velocities along x1
space_paths = {}
for speed in SPEEDS:
    tau, states = rk4_path(start(Y0, [speed, 0, 0, 0, 0, 0, 0, 0]), 3.0, 3000)
    frame_rows, y_values, lengths, h_rows = describe(states)
    p1 = h_rows[:, 0] ** 2 * states[:, 8]  # p_1 = g_11 u^1 = h_1^2 u^1
    weight = np.exp(-H_value * y_values - A_value * H_value * states[:, 3])  # kappa
    space_paths[speed] = (states, frame_rows, y_values, lengths, p1)
```

For each starting frame velocity along $x_1$ the path from $\tau = 0$ to $3$ in 3000 steps, its description, the momentum $p_1 = h_1^2u^1$ along the path (column 8 is $u^1$), and the momentum weight $\kappa = e^{-Hy - a_4}$; everything is stored under the speed.

```python
    check(np.max(np.abs(p1 / p1[0] - 1)) < 1e-9
          and np.max(np.abs(lengths + 1)) < 1e-9
          and np.max(np.abs(frame_rows[:, 0] - p1[0] * weight)) < 1e-9
          and np.all(np.diff(states[:, 11]) < 0) and np.all(y_values < 0),
          f"3-space speed {speed}: p1 and g(u, u) conserved, frame velocity "
          "p1 kappa, u4 falls")
```

One check per particle with five conditions: $p_1$ constant within a relative $10^{-9}$; $g(u, u) = -1$ within $10^{-9}$; the frame velocity equals $p_1\kappa$ within $10^{-9}$; $u^4$ decreases at every step (`np.diff` gives the differences of successive values); the particle stays inside the patch ($y < 0$).

```python
states, frame_rows, y_values, lengths, p1 = space_paths[1.0]
report("fastest particle at tau = 3: x4", f"{states[-1, 3]:.4f}")
report("fastest particle at tau = 3: frame velocity along x1",
       f"{frame_rows[-1, 0]:.6f}")
report("fastest particle at tau = 3: u4", f"{states[-1, 11]:.6f}")
report("fastest particle at tau = 3: height y", f"{y_values[-1]:.4f}")
```

Four RESULT lines for the fastest particle at $\tau = 3$: $x_4 = 3.3070$ (its clock has run 3 while $x_4$ advanced by more), $\hat u^1 = 0.014370$ (down from $1$), $u^4 = 1.060733$ (down from $\sqrt 2 = 1.414$), $y = -0.0643$ (risen from $-1$ almost to the patch end).

**In [11], the particle moving along an extra time.**

```python
tau_t, extra = rk4_path(start(Y0, [0, 0, 0, 0, 0.2, 0, 0, 0]), 2.5, 2500)
frame_t, y_t, lengths_t, h_t = describe(extra)
p5 = -h_t[:, 4] ** 2 * extra[:, 12]  # p_5 = g_55 u^5 = -h_5^2 u^5
check(np.max(np.abs(p5 / p5[0] - 1)) < 1e-8 and np.max(np.abs(lengths_t + 1)) < 1e-7
      and np.all(np.diff(extra[:, 11]) < 0),
      "extra-time particle: p5 and g(u, u) conserved, u4 decreases at every step")
```

A particle started with $\hat u^5 = 0.2$, so $u^4 = \sqrt{1 - 0.04} = 0.980$, followed from $\tau = 0$ to $2.5$ in 2500 steps. Its momentum $p_5 = -h_5^2u^5$ (column 12 is $u^5$) stays constant within a relative $10^{-8}$, $g(u, u)$ stays $-1$ within $10^{-7}$, and $u^4$ decreases at every step.

```python
n_turn = int(np.argmax(extra[:, 11] < 0))  # the first step with u4 < 0
x4_max = float(np.max(extra[:, 3]))  # the largest x4 of the path
report("turning point: proper time tau", f"{tau_t[n_turn]:.3f}")
report("turning point: largest x4 reached", f"{x4_max:.4f}")
report("turning point: frame velocity along x5", f"{frame_t[n_turn, 4]:.4f}")
report("turning point: frame velocity along y", f"{frame_t[n_turn, 7]:.4f}")
```

`extra[:, 11] < 0` is a list of `True` and `False`, one per step; `np.argmax` of it is the position of the first `True`, the first step with $u^4 < 0$: the turning point, to within one step. Four RESULT lines: $\tau = 1.987$, the largest $x_4 = 1.4864$, $\hat u^5 = 1.4013$, $\hat u^8 = -0.9817$.

```python
balance = frame_t[n_turn, 4] ** 2 - frame_t[n_turn, 7] ** 2 - 1  # 0 when u4 = 0
check(0 < n_turn and abs(balance) < 1e-4 and extra[-1, 3] < x4_max,
      "at the turning point (u5 hat)^2 - (u8 hat)^2 = 1, and x4 decreases afterwards")
say("record, sectorAndAnsatz.sector: " + ks_theory["sectorAndAnsatz"]["sector"])
check("extra-time momenta zero" in ks_theory["sectorAndAnsatz"]["sector"],
      "the good sector of the Kohn-Sham record has no extra-time momenta",
      record=f"{KS_THEORY}, sectorAndAnsatz.sector")
```

At the turning point $(\hat u^5)^2 - (\hat u^8)^2 = 1$ (Section 3.31; within $10^{-4}$, because the step found is the first after the sign change), and the last $x_4$ of the path is smaller than the largest. Then the record's definition of the good sector is printed and checked to contain "extra-time momenta zero" (Section 3.31).

**In [12], Figure 03d.1: redshift and blueshift.**

```python
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
MAGENTA, GREEN, VIOLET, RED = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
COLOURS = {0.25: AQUA, 0.5: ORANGE, 1.0: RED}  # one colour per 3-space particle
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
fig.subplots_adjust(wspace=0.3)  # room for the label of the right vertical axis
```

The palette, one colour per 3-space particle, and a figure with two panels.

```python
for speed in SPEEDS:
    states, frame_rows = space_paths[speed][0], space_paths[speed][1]
    axes[0].plot(states[:, 3], frame_rows[:, 0], color=COLOURS[speed], lw=1.8,
                 label=f"RK4, start {speed:g}")
    axes[0].plot(states[:, 3], speed * np.exp(-A_value * H_value * states[:, 3]),
                 ":", color=COLOURS[speed], lw=1.4)
axes[0].plot([], [], ":", color="grey", label="pure redshift $e^{-a_4}$")
```

For each 3-space particle its frame velocity $\hat u^1$ against $x_4$ (solid) and the pure redshift $\hat u^1(0)e^{-a_4}$ that it would have at a fixed height (dotted). `axes[0].plot([], [], ...)` draws nothing; it only adds one grey dotted entry to the legend for all three dotted lines.

```python
axes[0].set_yscale("log")
axes[0].set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$")
axes[0].set_ylabel("frame velocity $\\hat u^1$ along $x_1$")
axes[0].set_title("3-space: redshift")
axes[0].legend(fontsize=8)
before = slice(0, n_turn)  # the states before the turning point
axes[1].plot(extra[before, 3], frame_t[before, 4], color=VIOLET, lw=1.8,
             label="RK4, start 0.2")
axes[1].plot(extra[before, 3], 0.2 * np.exp(A_value * H_value * extra[before, 3]),
             ":", color=VIOLET, lw=1.4, label="pure blueshift $0.2\\,e^{a_4}$")
```

A logarithmic axis and labels for the left panel. `slice(0, n_turn)` selects the rows before the turning point (after it $x_4$ runs backwards, and the curve would fold back). The right panel: $\hat u^5$ against $x_4$ and the pure blueshift $0.2e^{a_4}$.

```python
axes[1].axvline(x4_max, color="grey", lw=1.0, ls="--", label="turning point")
axes[1].set_yscale("log")
axes[1].set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$")
axes[1].set_ylabel("frame velocity $\\hat u^5$ along $x_5$")
axes[1].set_title("Extra time: blueshift")
axes[1].legend(fontsize=8, loc="upper left")
save_figure(fig, "frame_velocities",
            "Frame velocities of freely falling test particles in the author's metric "
...
check(frame_t[n_turn - 1, 4] > 0.2 * math.exp(extra[n_turn - 1, 3]),
      "the extra-time frame velocity grows faster than the pure blueshift")
```

A dashed line at the largest $x_4$, the logarithmic axis, labels and legend; the figure is saved (its caption contains the turning point $x_4 = 1.486$ through an f-string). The check: just before the turning point, $\hat u^5$ exceeds the pure blueshift.

**What Figure 03d.1 shows.** Left: on the logarithmic axis the three frame velocities fall almost like straight lines of slope $-1$, the redshift $e^{-a_4}$; they fall a little faster than the dotted lines, most visibly for the fastest particle, because the particles rise towards the patch end where the warp factor $e^{Hy}$ is larger and $\kappa = e^{-Hy - a_4}$ smaller. Right: the frame velocity along $x_5$ grows from $0.2$, first like the pure blueshift $0.2e^{a_4}$, then faster, because the particle sinks towards the tip where $e^{-Hy}$ is larger; at the dashed line it reaches its turning point.

**In [13], Figure 03d.2: the $x_4$ velocity and the time $x_4$.**

```python
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
fig.subplots_adjust(wspace=0.3)
axes[0].plot(tau, rest[:, 11], color="black", lw=1.4, ls="--", label="at rest")
axes[1].plot(tau, rest[:, 3], color="black", lw=1.4, ls="--", label="at rest")
for speed in SPEEDS:
    states = space_paths[speed][0]
    axes[0].plot(tau, states[:, 11], color=COLOURS[speed], lw=1.8,
                 label=f"3-space, start {speed:g}")
    axes[1].plot(tau, states[:, 3], color=COLOURS[speed], lw=1.8,
                 label=f"3-space, start {speed:g}")
```

Two panels against the proper time $\tau$: $u^4$ on the left, $x_4$ on the right; first the particle at rest (dashed black), then the three 3-space particles.

```python
axes[0].plot(tau_t, extra[:, 11], color=VIOLET, lw=1.8, ls="-.",
             label="extra time, start 0.2")
axes[1].plot(tau_t, extra[:, 3], color=VIOLET, lw=1.8, ls="-.",
             label="extra time, start 0.2")
axes[0].axhline(0.0, color="grey", lw=0.8)
axes[0].plot([tau_t[n_turn]], [0.0], "o", color=VIOLET, ms=7)  # the turning point
axes[1].plot([tau_t[n_turn]], [x4_max], "o", color=VIOLET, ms=7)
```

The extra-time particle (dash-dotted), the zero line, and a dot at the turning point in each panel.

```python
axes[0].set_ylabel("$x_4$ velocity $u^4 = dx_4/d\\tau$")
axes[1].set_ylabel("time $x_4$ (unit $1/H$)")
axes[0].set_title("The $x_4$ velocity can only decrease")
axes[1].set_title("The time $x_4$ along each path")
for ax, place in zip(axes, ("lower left", "upper left")):  # legends off the lines
    ax.set_xlabel("proper time $\\tau$ of the particle (unit $1/H$)")
    ax.legend(fontsize=8, loc=place)
save_figure(fig, "x4_velocity",
            "The $x_4$ velocity $u^4 = dx_4/d\\tau$ (left) and the time $x_4$ "
...
check(np.all(np.diff(space_paths[1.0][0][:, 3]) > 0),
      "the particles in 3-space keep advancing in x4")
```

Labels and titles; the loop gives both panels their horizontal label and a legend placed where no curve runs. The figure is saved; the check confirms that the fastest 3-space particle advances in $x_4$ at every step.

**What Figure 03d.2 shows.** Left: the particle at rest keeps $u^4 = 1$; the 3-space particles start above $1$ and settle down towards $1$ as their motion is redshifted away; the extra-time particle starts at $0.98$ and its $u^4$ falls ever faster, through zero at the dot ($\tau = 1.99$) and on to negative values. Right: $x_4$ grows steadily for the first four particles, while for the extra-time particle it reaches a largest value, $1.486$, and then decreases.

**In [14], Figure 03d.3: the push along the hidden direction.**

```python
L_tip = physics["physics"]["L_tipCutoff"]  # the tip cut-off of the record, 3/H
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
fig.subplots_adjust(wspace=0.3)
axes[0].plot(tau, np.full_like(tau, Y0), color="black", lw=1.4, ls="--",
             label="at rest")
for speed in SPEEDS:
    axes[0].plot(tau, space_paths[speed][2], color=COLOURS[speed], lw=1.8,
                 label=f"3-space, start {speed:g}")
axes[0].plot(tau_t, y_t, color=VIOLET, lw=1.8, ls="-.", label="extra time, start 0.2")
```

The tip cut-off $L = 3$ of the record (Section 3.9), a figure with two panels, and in the left panel the height $y$ of every particle against $\tau$ (the particle at rest stays at $y = -1$, drawn with `np.full_like`).

```python
axes[0].axhline(0.0, color="grey", lw=1.0, label="patch end $y = 0$")
axes[0].axhline(-L_tip, color="grey", lw=1.0, ls=":", label="tip cut-off $y = -3$")
axes[0].set_xlabel("proper time $\\tau$ (unit $1/H$)")
axes[0].set_ylabel("height $y$ in the hidden direction (unit $1/H$)")
axes[0].set_title("Rising and sinking along $y$")
axes[0].legend(fontsize=7, loc="lower left")
largest_gap = 0.0
```

Horizontal lines at the patch end and at the tip cut-off, labels, title and legend. `largest_gap` will collect the largest disagreement found below.

```python
for (t_values, frame_rows), colour, label in (
        ((tau, space_paths[1.0][1]), RED, "3-space, start 1"),
        ((tau_t, frame_t), VIOLET, "extra time, start 0.2")):
    law = H_value * (np.sum(frame_rows[:, 0:3] ** 2, axis=1)
                     - np.sum(frame_rows[:, 4:7] ** 2, axis=1))
    numeric = np.gradient(frame_rows[:, 7], t_values)  # d(u8 hat)/dtau
    largest_gap = max(largest_gap, float(np.max(np.abs(numeric - law)[1:-1])))
```

For the fastest 3-space particle and the extra-time particle: the push law $H(S - E)$ at every computed state (`frame_rows[:, 0:3]` are the three 3-space columns, `frame_rows[:, 4:7]` the three extra-time columns), and the acceleration $d\hat u^8/d\tau$ obtained from the computed states by `np.gradient`, which takes central differences inside the path and one-sided differences at its two ends. The largest difference inside the path (`[1:-1]` leaves out the two ends, where the one-sided differences are less accurate) is kept.

```python
    axes[1].plot(t_values, law, color=colour, lw=1.8, label=f"law, {label}")
    axes[1].plot(t_values[::100], numeric[::100], "o", color=colour, ms=5,
                 label=f"from RK4, {label}")
axes[1].axhline(0.0, color="grey", lw=0.8)
axes[1].set_xlabel("proper time $\\tau$ (unit $1/H$)")
axes[1].set_ylabel("$d^2y/d\\tau^2$ (unit $H$)")
axes[1].set_title("The push: $H$ times the difference of squares")
axes[1].legend(fontsize=7, loc="lower left")
```

The law as a line and every hundredth numerical value as a dot (`[::100]` takes every hundredth element); the zero line, labels, title and legend.

```python
report("largest difference between the numerical acceleration and the law",
       f"{largest_gap:.1e}")
save_figure(fig, "hidden_push",
            "The push along the hidden direction on freely falling test particles in "
...
check(largest_gap < 1e-4,
      "the computed acceleration of y agrees with the exact push law")
```

The RESULT line prints $3.4 \times 10^{-6}$, the error of the numerical derivative; the figure is saved, and the check requires agreement within $10^{-4}$.

**What Figure 03d.3 shows.** Left: the 3-space particles rise towards the patch end $y = 0$, the faster the higher (the fastest reaches $-0.06$); the particle at rest stays at $y = -1$; the extra-time particle sinks towards the tip, ever faster, to about $-2.3$ at $\tau = 2.5$, still above the cut-off $y = -3$. Right: the dots computed from the paths lie on the lines of the exact law; the push is positive and dies away for the 3-space particle (its frame velocity is redshifted), negative and growing for the extra-time particle (its frame velocity is blueshifted).

**In [15], Figure 03d.4: the quadratic form as a map.**

```python
grid5, grid8 = np.meshgrid(np.linspace(0.0, 3.0, 301), np.linspace(-3.0, 0.5, 351))
squared_u4 = 1 - grid5 ** 2 + grid8 ** 2  # (u^4)^2 over the plane
fig, ax = plt.subplots(figsize=(6.4, 5.2))
ax.contourf(grid5, grid8, squared_u4, levels=[-100.0, 0.0], colors=["#d9d9d9"])
ax.contour(grid5, grid8, squared_u4, levels=[0.0], colors="black", linewidths=1.2)
```

A grid of frame velocities, $\hat u^5$ from $0$ to $3$ and $\hat u^8$ from $-3$ to $0.5$, and on it $(u^4)^2 = 1 - (\hat u^5)^2 + (\hat u^8)^2$, the formula of Section 3.31 for a particle that moves only along $x_5$ and $y$. `contourf` with the levels $-100$ and $0$ fills in grey the region where the value is negative; `contour` at the level $0$ draws the black boundary curve $(\hat u^5)^2 = 1 + (\hat u^8)^2$.

```python
ax.plot(frame_t[:, 4], frame_t[:, 7], color=VIOLET, lw=2.0,
        label="path of the extra-time particle")
ax.plot([frame_t[0, 4]], [frame_t[0, 7]], "s", color=VIOLET, ms=7, label="start")
ax.plot([frame_t[n_turn, 4]], [frame_t[n_turn, 7]], "o", color=VIOLET, ms=8,
        label="turning point, $u^4 = 0$")
ax.text(2.05, 0.15, "$(u^4)^2 < 0$:\nno particle;\nplane waves grow", fontsize=8)
ax.text(0.3, -1.2, "$(u^4)^2 > 0$", fontsize=9)
```

The path of the extra-time particle in this plane, a square at its start, a dot at its turning point, and two labels written into the regions (`\n` starts a new line of the label).

```python
ax.set_xlabel("frame velocity $\\hat u^5$ along the extra time $x_5$")
ax.set_ylabel("frame velocity $\\hat u^8 = dy/d\\tau$")
ax.set_title("The quadratic form $(u^4)^2 = 1 - (\\hat u^5)^2 + (\\hat u^8)^2$")
ax.grid(False)
ax.legend(fontsize=8, loc="lower left")
save_figure(fig, "quadratic_form",
            "The squared $x_4$ velocity $(u^4)^2 = 1 - (\\hat u^5)^2 + (\\hat u^8)^2$ "
...
check(np.all(1 - frame_t[:, 4] ** 2 + frame_t[:, 7] ** 2 > -1e-6),
      "the path never enters the region where (u4)^2 < 0")
```

Labels, title, no grid lines, legend; the figure is saved; the check: along the whole path $(u^4)^2 > -10^{-6}$ (zero up to rounding at the turning point).

**What Figure 03d.4 shows.** The violet path starts at $(0.2, 0)$, moves to the right (blueshift) and downwards (it sinks, $dy/d\tau < 0$), touches the black curve at the turning point and then runs back into the white region, without ever entering the grey one. In the grey region the plane waves of the record's check would grow instead of oscillating; the particle avoids it by turning in $x_4$.

**In [16], Figure 03d.5: how accurate the computation is.**

```python
from matplotlib.ticker import NullFormatter  # an empty label for minor ticks

p1_fast = space_paths[1.0][4]  # p_1 along the fastest 3-space path
drift = {"$p_1$, 3-space particle": (tau, np.abs(p1_fast / p1_fast[0] - 1)),
         "$g(u,u) + 1$, 3-space particle": (tau, np.abs(space_paths[1.0][3] + 1)),
         "$p_5$, extra-time particle": (tau_t, np.abs(p5 / p5[0] - 1)),
         "$g(u,u) + 1$, extra-time particle": (tau_t, np.abs(lengths_t + 1))}
```

`NullFormatter` is used below to suppress the labels of small ticks. `drift` is a dictionary of four curves, each a label with its times and the drift of a conserved quantity from its starting value: $p_1$ and $g(u, u) + 1$ for the fastest 3-space particle, $p_5$ and $g(u, u) + 1$ for the extra-time particle.

```python
STEPS = (50, 100, 200, 400, 800, 1600)
differences = {}
for label, state0 in (("3-space, start 1", start(Y0, [1, 0, 0, 0, 0, 0, 0, 0])),
                      ("extra time, start 0.2", start(Y0, [0, 0, 0, 0, 0.2, 0, 0, 0]))):
    ends = [rk4_path(state0, 2.0, n)[1][-1] for n in STEPS]
    differences[label] = np.array([np.max(np.abs(ends[i] - ends[i + 1]))
                                   for i in range(len(STEPS) - 1)])
    ratios = differences[label][:-1] / differences[label][1:]
    say(f"  {label}: ratios of successive differences "
        + ", ".join(f"{r:.1f}" for r in ratios))
```

The order of RK4: each of the two particles is integrated from $\tau = 0$ to $2$ with 50, 100, 200, 400, 800 and 1600 steps; `ends` holds the six end states (`[1][-1]` is the last row of the table of states). `differences` holds the five largest differences between the end states of successive step counts, and `ratios` the four ratios of successive differences, printed: 17.1, 16.6, 16.3, 16.2 and 17.2, 16.7, 16.3, 16.2. For a method of order 4 halving the step divides the error by about $2^4 = 16$ (Chapter 2).

```python
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
fig.subplots_adjust(wspace=0.3)
for (label, (t_values, values)), colour, style in zip(
        drift.items(), (RED, ORANGE, VIOLET, AQUA), ("-", "--", "-.", ":")):
    axes[0].semilogy(t_values[1:], np.maximum(values[1:], 1e-17), color=colour,
                     ls=style, lw=1.6, label=label)
axes[0].set_xlabel("proper time $\\tau$ (unit $1/H$)")
axes[0].set_ylabel("relative drift from the start")
axes[0].set_title("Conserved quantities, RK4 with step $0.001$")
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

The right panel: the differences against the larger step $\Delta\tau$ of each pair ($0.04$, $0.02$, $0.01$, $0.005$ and $0.0025$), on logarithmic axes, with a dashed reference line of slope 4; the five steps are written at the ticks, and the small ticks between them get no labels.

```python
axes[1].set_xlabel("step $\\Delta\\tau$ of RK4")
axes[1].set_ylabel("difference of end states (step and half step)")
axes[1].set_title("RK4 is of order 4")
axes[1].legend(fontsize=8)
save_figure(fig, "accuracy",
            "The accuracy of the RK4 computation of free fall in the author's metric "
...
all_ratios = np.concatenate([d[1:-1] / d[2:] for d in differences.values()])
check(np.all((all_ratios > 14) & (all_ratios < 18)),
      "halving the RK4 step divides the error by 14 to 18: order 4")
```

Labels, title, legend; the figure is saved. For the check, the coarsest pair (where the error is not yet in its final form) is left out: `d[1:-1] / d[2:]` gives the last three ratios of each particle, $16.6, 16.3, 16.2$ and $16.7, 16.3, 16.2$, and all six must lie between 14 and 18 (`&` combines the two conditions element by element).

**What Figure 03d.5 shows.** Left: the conserved quantities drift by at most about $10^{-8}$ (the squared speed of the extra-time particle at the end, when its velocities have grown large), the 3-space quantities by less than $10^{-11}$. Right: both sets of points lie on lines of slope 4: halving the step makes the error 16 times smaller. The computed paths are accurate far beyond the precision of any number quoted from them.

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
- for the author's metric: the signature (4,4) at every point of the patch and for every $a_4$; $\det g = \cos^2 z$ and $\sqrt{|\det g|} = \cos z$, without $a_4$ (record `python-lovelock-report.json`, check `sqrt_abs_det_g`; `curvature.json`, key `sqrtAbsDetG`); the constant 7-volume density and the 7-volume $1/(6H)$ of the patch per unit transverse coordinate volume; $V_3V_t = \sin z$ (Sections 3.5 and 3.6);
- the scale factors and the diagonal vielbein (lead check `vielbein_reproduces_metric`); the expansion rates $+a_4'$ of 3-space and $-a_4'$ of the extra times; the transverse product $\sin z$ (Section 3.7);
- the hidden coordinate $y$: $dy = \cot z\,dx_8$ (lead check `ks_coordinate_jacobian`), $W = \sin^{1/6}z = e^{Hy}$, the warped form and the volume factor $e^{6Hy}$ of the record `ks-theory.json`; the tip at infinite proper distance; the fraction $e^{-6HL}$ beyond the tip cut-off (Section 3.9);
- the transformation rules of vectors, covectors and the metric; the invariance of contractions (Section 3.14); the covariant derivative of covectors and of the metric; the Christoffel formula as the only connection without torsion that is compatible with the metric; the four cases for a diagonal metric; the contracted symbol $\sum_a\Gamma^a{}_{ab} = \partial_b\ln\sqrt{|\det g|}$ (Section 3.15);
- along a geodesic the squared speed is constant, and a coordinate absent from a diagonal metric has a conserved momentum; the geodesic equations of the sphere; the equator is a geodesic and other circles of latitude are not; parallel transport around a circle of latitude turns a vector by $2\pi(1 - \cos\theta_0)$, the enclosed area divided by $a^2$ (Section 3.16);
- the commutator of covariant derivatives is the Riemann tensor (MTW convention); its antisymmetry in the last two indices and the first Bianchi identity; each diagonal entry of the Ricci tensor is the sum of the curvatures of the coordinate planes through that direction (Section 3.17);
- the plane is flat; the sphere has the Gaussian curvature $1/a^2$, $R = 2/a^2$, $K = 4/a^4$; two meridians approach as $a\cos(s/a)\Delta\varphi$ (Section 3.18);
- the 37 non-zero Christoffel symbols of the author's metric (25 with $b \le c$, record `curvature.json`, key `christoffelNonzero_b_le_c`); observers at rest fall freely with proper time $x_4$ (Section 3.23);
- the curvatures of the 28 coordinate planes; the 156 non-zero components $R^{ab}{}_{cd}$ (record `lovelock-report.json`, check `riemann_antisymmetry`); their frame values are constants (Section 3.24);
- $R^a{}_a$, $R = 6a_4'^2 - 42H^2$ and the Einstein tensor (record `curvature.json`, keys `ricciMixed`, `ricciScalar`, `einsteinMixed`); the Ricci and Einstein tensors are diagonal because the three inflating and the three deflating directions cancel (with inflating extra times they would not be); $G^4{}_4 - G^8{}_8 = 6(a_4'^2 + H^2) > 0$; $K = 12(7H^4 - 2H^2a_4'^2 + 7a_4'^4 + 2a_4''^2) \ge 576H^4/7 > 0$, so the metric is curved for every history; the contracted Bianchi identity for every $a_4(x_4)$ (record `lovelock-report.json`, checks `k1_equals_minus_4_einstein`, `k1_divergence_free`) (Section 3.25);
- within Einstein's equations: no empty spacetime has this metric; $\kappa(\rho + p_8) = -6(a_4'^2 + H^2) < 0$; along $a_4 = AHx_4$ the required source $\kappa\rho = -3H^2(7 + A^2) - \Lambda$, $\kappa p = 3H^2(5 - A^2) + \Lambda$, $\kappa(\rho + p) = -6H^2(A^2 + 1) < 0$ (record `a4-equations.json`, keys `einstein` and `linearMember`) (Section 3.26);
- in free fall: the six momenta and $g(u, u)$ are conserved; $\hat u^i = p_ie^{-Hy - a_4}$ (the momentum weight $\kappa$ of `ks-theory.json`) and $\hat u^j = -p_je^{a_4 - Hy}$, so 3-space motion is redshifted and extra-time motion blueshifted; $d^2y/d\tau^2 = H(S - E)$; $du^4/d\tau = -a_4'(S + E)$; $(u^4)^2 = 1 + S - E + (\hat u^8)^2$, which times $m^2$ is the quadratic form of the record's check `extra_time_growth_rates_unbounded`; without extra-time motion a particle never turns in $x_4$ (Section 3.31).

**COMPUTED by the notebooks** (each number in the cell named; where a Revision record is reproduced, its file and key or check):

- Notebook 03a: $g_{11} = 2.347679$ and $g_{55} = -0.317724$ at $z = 0.7$, $a_4 = 0.5$ (In [8]); the signs on a grid of 400 values of $z$ and 13 of $a_4$ (In [8]); the slices, $H = 1$, $A = 1$ and $L = 3$ (In [13]; `Revision/kohn_sham/results/parameters.json`); the growth and shrink factors $e^2 = 7.389056$ and $e^{-2} = 0.135335$ (In [14]); the cut-off fraction $e^{-18} = 1.5230 \times 10^{-8}$ and the cut-off angle $1.5230 \times 10^{-8}$ radians (In [20]).
- Notebook 03c: the turning angles of 15 circles within $5.0 \times 10^{-12}$ radians of the area formula (In [10]); three geodesics within $1.2 \times 10^{-13}$, $6.2 \times 10^{-13}$ and $7.1 \times 10^{-11}$ of their planes (In [11]); the deviation equation within $8.0 \times 10^{-14}$ of two meridians (In [13]).
- Notebook 03b: the 512 Christoffel symbols by central differences, order $2.040$, best error $5.4 \times 10^{-11}$ at $h = 10^{-6}$ at the test point of the record's check `k1_brute_force_numeric` (In [10], In [11]); all 310 recorded components equal to ours at the five test points of `python-lovelock-report.json` to the relative $1.48 \times 10^{-31}$ with 30 digits (In [19]); $K$ summed from the 156 components equal to the formula at 300 values of $z$ (In [23]).
- Notebook 03d: along the prescribed history with RK4 and the step $0.001$, from $y = -1$: the particle at rest stays at rest (In [9]); the fastest 3-space particle at $\tau = 3$ has $x_4 = 3.3070$, $\hat u^1 = 0.014370$, $u^4 = 1.060733$, $y = -0.0643$ (In [10]); the extra-time particle turns at $\tau = 1.987$ with the largest $x_4 = 1.4864$, $\hat u^5 = 1.4013$, $\hat u^8 = -0.9817$ (In [11]); the push law within $3.4 \times 10^{-6}$ (In [14]); RK4 ratios 16.2 to 17.2 (In [16]).

**ASSUMED** (used, not derived here):

- standard theorems quoted without proof: Sylvester's law of inertia (Section 3.4); the volume factor of a metric that is not diagonal (not needed); that the Christoffel symbols of two systems of coordinates describe the same covariant derivative (Section 3.15); that a space with zero Riemann tensor has constant metrics locally (Section 3.17); the symmetries (S3) and (S4) and the contracted Bianchi identity for a general metric (Sections 3.17 and 3.25; for the author's metric all three are checked or proved); the uniqueness of solutions of ordinary differential equations (Section 3.16); the geodesic deviation equation of a general surface (Section 3.18);
- from physics: that a body in free fall moves on a time-like geodesic, and that the bodies of Section 3.31 are test particles; the form of Einstein's field equations and the null energy condition as the mark of ordinary matter (Section 3.26; derived and discussed in Chapters 9 and 12);
- the history $a_4 = AHx_4$ with $A = 1$ and $H = 1$, used for every picture and every number along the history: a PRESCRIBED BACKGROUND, not a solution of the field equations with a source of this book (`Revision/kohn_sham/ks-theory.json`, key `adiabaticity.historyStatus`; `Revision/field_equations_a4/reports/ks-source-conditions.json`). Every formula written with a general $a_4(x_4)$ is exact without it.

**HYPOTHESIS.** None enters this chapter.

**OPEN.** Whether wave packets of the fields of the book follow the free-fall paths of Section 3.31 in the curved metric is not computed (Section 3.31).

This chapter says nothing about pairs of universes, their creation, or matter and antimatter; Chapters 18 to 21 treat these questions and state exactly what is and what is not proved about them.

### 3.37 Exercises

**Exercise 1.** In the plane, use the coordinates $u = x + y$ and $v = x - y$. Find the line element, the metric and its Christoffel symbols.

*Answer.* Solving for $x$ and $y$: $x = (u + v)/2$ and $y = (u - v)/2$ (add and subtract the two definitions). So $dx = (du + dv)/2$ and $dy = (du - dv)/2$ (each coefficient is constant), and

$$
ds^2 = dx^2 + dy^2 = \frac{(du + dv)^2 + (du - dv)^2}{4} = \frac{2\,du^2 + 2\,dv^2}{4} = \frac{du^2 + dv^2}{2}
$$

(the squares of a sum and of a difference; the mixed terms $\pm 2\,du\,dv$ cancel). The metric is $\mathrm{diag}(1/2, 1/2)$. It is constant, so all its derivatives vanish and every Christoffel symbol is zero (Section 3.15): in these coordinates straight lines are again $d^2u/d\lambda^2 = d^2v/d\lambda^2 = 0$.

**Exercise 2.** Figure 03a.1 shows the author's metric at $z = \pi/4$, $a_4 = 0.5$ with the entries $2.422$ (three times), $-1$, $-0.328$ (three times) and $1$. Multiply them and compare with $\det g = \cos^2 z$. Then do the same exactly.

*Answer.* With the rounded numbers: $2.422 \times 0.328 = 0.794416$, and $(0.794416)^3 = 0.5013$; the product of the eight entries is $2.422^3\cdot(-1)\cdot(-0.328)^3\cdot 1 = (2.422 \times 0.328)^3 = 0.5013$ (an odd power keeps the minus sign, and the two minus signs cancel). $\cos^2(\pi/4) = 1/2$. Exactly: the entries are $e\,s$ and $-e^{-1}s$ with $s = (\sin\pi/4)^{1/3}$, so the product is $(e\,s)^3\cdot(-1)\cdot(-e^{-1}s)^3\cdot\cot^2(\pi/4) = s^6 = \sin^2(\pi/4) = 1/2$ ($e^3e^{-3} = 1$; $\cot(\pi/4) = 1$). The difference $0.0013$ comes only from rounding the entries to three decimals.

**Exercise 3.** Compute $\Gamma^{x_4}{}_{x_5x_5}$ and $\Gamma^{x_8}{}_{x_5x_5}$ of the author's metric directly from the Christoffel formula, without the four cases.

*Answer.* The formula of Section 3.15 with $a = x_4$, $b = c = x_5$ keeps only $d = x_4$ (the metric is diagonal): $\Gamma^4{}_{55} = \tfrac12 g^{44}(\partial_5 g_{45} + \partial_5 g_{45} - \partial_4 g_{55}) = \tfrac12(-1)(0 + 0 - \partial_4 g_{55}) = \tfrac12\partial_4\bigl(-e^{-2a_4}\sin^{1/3}z\bigr) = \tfrac12\cdot 2a_4'\,e^{-2a_4}\sin^{1/3}z = a_4'\,e^{-2a_4}\sin^{1/3}z$ ($g_{45} = 0$; $g^{44} = -1$; the chain rule, $\partial_4 e^{-2a_4} = -2a_4'e^{-2a_4}$). For $\Gamma^8{}_{55}$ the formula with $a = x_8$, $b = c = x_5$ keeps only $d = x_8$, and the two terms with $g_{85} = 0$ vanish: $\Gamma^8{}_{55} = -\tfrac12 g^{88}\partial_8 g_{55} = -\tfrac12\tan^2 z\cdot\bigl(-e^{-2a_4}\bigr)\cdot\tfrac13\sin^{-2/3}z\cos z\cdot 6H = H\tan^2 z\,e^{-2a_4}\sin^{-2/3}z\cos z$ ($g^{88} = 1/\cot^2 z = \tan^2 z$; the power rule and the chain rule for $\sin^{1/3}(6Hx_8)$). Since $\tan^2 z\cos z\sin^{-2/3}z = \tan z\cdot\frac{\sin z}{\cos z}\cos z\sin^{-2/3}z = \tan z\sin^{1/3}z$, this is $H\tan z\,e^{-2a_4}\sin^{1/3}z$. Both agree with the table of Section 3.23.

**Exercise 4.** (a) By what angle does a vector turn when it is carried once around the equator of a sphere? (b) Show that for a small circle around the pole, $\theta_0 \ll 1$, the turning angle is about $\pi\theta_0^2$, and explain this number.

*Answer.* (a) With $\theta_0 = \pi/2$, $\cos\theta_0 = 0$: the transport equations of Section 3.16 give $du/d\varphi = dw/d\varphi = 0$, so the vector does not turn at all relative to the south and east directions; the formula $2\pi(1 - \cos\theta_0) = 2\pi$ is one whole turn, the same direction. This fits: the cap is a hemisphere of area $2\pi a^2$, and the equator is a geodesic, along which a vector keeps its angle to the direction of travel. (b) For small $\theta_0$, $\cos\theta_0 \approx 1 - \theta_0^2/2$ (Taylor's formula, Chapter 2), so $2\pi(1 - \cos\theta_0) \approx 2\pi\cdot\theta_0^2/2 = \pi\theta_0^2$. A small cap is almost a flat disc of radius $a\theta_0$ (the distance from the pole along the sphere), with the area $\pi a^2\theta_0^2$; times the curvature $1/a^2$ this is $\pi\theta_0^2$. For $\theta_0 = 0.1$ the exact angle is $2\pi(1 - \cos 0.1) = 0.031390$ and the estimate $0.031416$; Figure 03c.3 shows the first dot at this height.

**Exercise 5.** Show that the Einstein tensor of every surface (two dimensions) is zero.

*Answer.* By Section 3.17 a surface has $R^1{}_1 = R^2{}_2 = K(1, 2)$ and $R = 2K(1, 2)$. The off-diagonal entries vanish: $R^1{}_2 = \sum_c R^{1c}{}_{2c} = R^{11}{}_{21} + R^{12}{}_{22} = 0$ (antisymmetry in the upper pair and in the lower pair). So $G^1{}_1 = K(1, 2) - \tfrac12\cdot 2K(1, 2) = 0$, likewise $G^2{}_2 = 0$, and $G^1{}_2 = G^2{}_1 = 0$. For the sphere, $1/a^2 - \tfrac12\cdot 2/a^2 = 0$. In two dimensions the Einstein tensor says nothing about the curvature; this is why gravity needs more dimensions.

**Exercise 6.** For the canonical history $A = 1$ and $\Lambda = 0$, find $\kappa\rho$, $\kappa p$ and the ratio $w = p/\rho$ that Einstein's equations require. Which $\Lambda$ would make $\rho = 0$, and what is then $\kappa p$?

*Answer.* From Section 3.26: $\kappa\rho = -3H^2(7 + 1) - 0 = -24H^2$ and $\kappa p = 3H^2(5 - 1) + 0 = 12H^2$, so $w = p/\rho = 12/(-24) = -1/2$; the energy density is negative. $\rho = 0$ needs $\Lambda = -3H^2(7 + A^2) = -24H^2$, and then $\kappa p = 12H^2 - 24H^2 = -12H^2$. In both cases $\kappa(\rho + p) = -12H^2 < 0$, as Section 3.26 says for every $\Lambda$: the cosmological constant cancels from $\rho + p$.

**Exercise 7.** Find the smallest value of the Kretschmann scalar of the author's metric for histories with $a_4'' = 0$, and the slope $A$ at which it is reached.

*Answer.* With $a_4'' = 0$ and $s = a_4'^2 \ge 0$, $K = 12(7s^2 - 2H^2s + 7H^4)$ (Section 3.25). Its derivative with respect to $s$ is $12(14s - 2H^2)$, zero at $s = H^2/7$; there $K = 12H^4(7/49 - 2/7 + 7) = 12H^4(1/7 - 2/7 + 49/7) = 12H^4\cdot 48/7 = 576H^4/7 = 82.29H^4$, a minimum because the parabola $7s^2 - \dots$ opens upwards. With $a_4' = AH$: $A^2 = 1/7$, $A = 1/\sqrt7 = 0.378$. This is the low point of the red curve of Figure 03b.6, and the value $576H^4/7$ printed by Notebook 03b, In [22].

**Exercise 8.** The extra-time particle of Notebook 03d starts at $y = -1$ with $\hat u^5 = 0.2$. (a) If it stayed at $y = -1$ and never moved along $y$, at which $x_4$ would it turn? (b) Use the printed turning-point values $x_4 = 1.4864$ and $\hat u^5 = 1.4013$ and the conserved momentum $p_5$ to find the height $y$ of the turning point.

*Answer.* (a) At fixed $y$, $\hat u^5 = 0.2\,e^{a_4}$ (pure blueshift, Section 3.31) and $\hat u^8 = 0$; the turning condition $(\hat u^5)^2 = 1 + (\hat u^8)^2$ becomes $0.2\,e^{a_4} = 1$, so $a_4 = \ln 5 = 1.609$, that is $x_4 = 1.609$ on the history $a_4 = x_4$. (b) From $\hat u^5 = -p_5e^{a_4 - Hy}$ and the start ($a_4 = 0$, $y = -1$, $H = 1$): $-p_5 = 0.2\,e^{-1}$, so $\hat u^5 = 0.2\,e^{a_4 - (y + 1)}$. At the turning point $1.4013 = 0.2\,e^{1.4864 - (y + 1)}$, so $1.4864 - (y + 1) = \ln 7.0065 = 1.9468$ and $y = -1.460$. The particle has sunk by $0.46$ towards the tip, which raised its frame velocity by the factor $e^{0.46} = 1.585$ beyond the pure blueshift, and it turned earlier ($x_4 = 1.486$) than the estimate (a), although its motion along $y$, $\hat u^8 = -0.98$, made the turning condition harder to reach ($(\hat u^5)^2 = 1.96$ instead of $1$). Figure 03d.3 shows the particle near $y = -1.46$ at $\tau \approx 2$.

**Exercise 9.** What fraction of the 7-volume of the patch, and at which angle $z$, would a tip cut-off $L = 2/H$ remove?

*Answer.* By Section 3.9 the fraction is $e^{-6HL} = e^{-12} = 6.144 \times 10^{-6}$, about 400 times more than the $e^{-18} = 1.523 \times 10^{-8}$ of the record's $L = 3/H$ ($e^{6} = 403$). The cut-off lies at $\sin z = e^{6Hy} = e^{-12}$, so $z = \arcsin e^{-12} = 6.144 \times 10^{-6}$ (for small $u$, $\arcsin u \approx u$).
