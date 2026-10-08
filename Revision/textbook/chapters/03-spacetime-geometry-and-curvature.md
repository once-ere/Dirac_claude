## 3. Spacetime geometry and the author's metric; curvature

Gravity, in Einstein's theory, is not a force that acts inside space and time: it is the shape of space and time itself. This chapter builds, from nothing but school algebra and one-variable calculus, the language in which that shape is written down and measured: coordinates, the metric, its signature, scale factors and volumes, the Christoffel symbols, geodesics (the paths of free fall), and curvature in the form of the Riemann tensor, the Ricci tensor, the Ricci scalar, the Einstein tensor and the Kretschmann scalar. Every tool is tried first where we can picture it, on the flat plane and on a sphere, and then applied, completely and line by line, to the metric that the author wrote down for the primordial gravitational field. The chapter has four worked examples, Notebooks 03a, 03c, 03b and 03d (in the order in which the chapter uses them); each reproduces, number for number, the parts of the Revision record that it overlaps and says so in a PASS line.

### 3.1 What this chapter is for

Every later chapter of the book lives in the author's eight-dimensional spacetime. The spinor fields of Chapters 4 to 10 need its vielbein (the scale factors of Section 3.7); the energy-momentum tensor of Chapter 9 needs its Christoffel symbols (Section 3.22); the field equations of the metric function $a_4$ in Chapter 12 need its Einstein tensor (Section 3.24); the Kohn-Sham model of Chapters 14 to 17 is written in the hidden coordinate $y$ of Section 3.9. This chapter derives all of these from the metric itself.

The author's metric is the following diagonal $8 \times 8$ matrix, in the order of the author's coordinates $x_1, \dots, x_8$ (Section 3.5 reads it exactly as the author typed it):

$$
g = \mathrm{diag}\bigl(e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ -1,\ -e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ \cot^2 z\bigr),\qquad z = 6Hx_8 .
$$

The coordinates have fixed roles. $x_1, x_2, x_3$ are ordinary **3-space**; it inflates, with the scale factor $e^{a_4}\sin^{1/6}z$. $x_4$ is **the time**. $x_5, x_6, x_7$ are three **extra times**: they are time-like like $x_4$, and they **deflate exponentially**, with the scale factor $e^{-a_4}\sin^{1/6}z$, while $a_4$ grows. $x_8$ is the **hidden** space direction, with $z = 6Hx_8$ between $0$ and $\pi/2$ and $g_{88} = \cot^2 z$. $H > 0$ is a constant of the author, and $a_4(x_4)$ is a function of the time only, the **metric function**; a prime means its derivative with respect to $x_4$, $a_4' = da_4/dx_4$.

The four notebooks of the chapter are:

| notebook | what it computes | Revision records it reproduces |
| --- | --- | --- |
| 03a | reads the metric exactly as the author typed it; determinant, signature (4,4), vielbein, expansion rates, the deflating history, proper volumes, the hidden coordinate $y$ and the warped form; 7 figures, 29 checks | `Revision/gkd_lovelock/results/curvature.json`, `python-lovelock-report.json`, `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`, `Revision/kohn_sham/results/parameters.json`, `Revision/kohn_sham/ks-theory.json` |
| 03c | curvature where it can be pictured: the flat plane in polar coordinates and the sphere; parallel transport, geodesics, geodesic deviation, all with RK4; 5 figures, 16 checks | none (exact formulas only) |
| 03b | all Christoffel symbols, Riemann, Ricci and Einstein components and the Kretschmann scalar of the author's metric, exactly; finite differences; the curvature along the deflating history; the source Einstein's equations would require; a negative control; 7 figures, 39 checks | `curvature.json`, `python-lovelock-report.json`, `lovelock-report.json` (all three in `Revision/gkd_lovelock/results/`), `Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`, `Revision/field_equations_a4/a4-equations.json`, `Revision/field_equations_a4/reports/python-a4-report.json` |
| 03d | free fall in the author's metric: conserved momenta, redshift in 3-space, blueshift along the extra times, the push along the hidden direction, the turning point in $x_4$; RK4 paths with the record's Christoffel symbols; 5 figures, 23 checks | `curvature.json`, `parameters.json`, `ks-theory.json`, `Revision/theory/reports/python-scope.json` |

Every statement of the chapter carries one of the five labels of Chapter 0. **PROVED** means derived exactly here, line by line, and confirmed by an exact check of a notebook; where the Revision record proves the same, the record file and its check are named. **COMPUTED** means a number obtained numerically by a notebook, with its measured accuracy. **ASSUMED** marks two kinds of statements: standard theorems that we quote without proof (each is named where it is used), and the physical input that the history of the metric function is $a_4 = AHx_4$, which the Revision record itself calls a PRESCRIBED BACKGROUND (Section 3.8). One question is **OPEN** (Section 3.31): whether wave packets of the fields follow the free-fall paths computed here. No HYPOTHESIS enters this chapter. Nothing in this chapter concerns pairs of universes, their creation, or matter and antimatter; those questions belong to Chapters 18 to 21, which also state precisely what is and what is not proved about them.

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

**Reading it term by term.** A step $dx_1$ in 3-space has the true (proper) length $e^{a_4}\sin^{1/6}z\,dx_1$, the square root of its coefficient: when $a_4$ grows, 3-space **inflates**. A step $dx_5$ along an extra time has the proper duration $e^{-a_4}\sin^{1/6}z\,dx_5$: when $a_4$ grows, the three extra times **deflate exponentially**. A step $dx_4$ has $ds^2 = -dx_4^2$, so a clock at rest shows exactly $x_4$: the coordinate $x_4$ is the proper time of an observer at rest (Section 3.22 shows that such an observer is in free fall). The hidden direction has the coefficient $\cot^2 z$, which depends on $x_8$ only.

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

**Status: ASSUMED.** The history is not a solution of the coupled field equations. The Revision record says so in its own words (`Revision/kohn_sham/ks-theory.json`, key `adiabaticity.historyStatus`): "PRESCRIBED BACKGROUND: the history a4 = A H x4 is prescribed, not solved for." The reason, also stated there: the field equations of $a_4$ allow this linear member only for a source with equal pressures in all directions and a constant energy density, and the Kohn-Sham states computed along it do not have these properties (record `Revision/field_equations_a4/reports/ks-source-conditions.json`). Every formula of this chapter written with a general $a_4(x_4)$ is exact; only the pictures and the numbers along the history use the assumption. The book never uses a history with $A = 0$ (no deflation) or $A < 0$ (the extra times would inflate and 3-space deflate), because those are not the author's metric.

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

600 values of $z$ from $0.02$ to $\pi/2$ and the eight entries at $a_4 = 0.5$. `ax.plot(x, y, ...)` draws a curve; `lw` is the line width, `ls` the line style (`"-."` dash-dotted, `"--"` dashed, `":"` dotted) and `label` its text in the legend. Equal entries are drawn once: row 0 for 3-space, row 3 for the time, row 4 for the extra times, row 7 for the hidden direction; the black dotted curve is $\det g = \cos^2 z$.

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

**What Figure 03a.5 shows.** Left: from left to right the colour turns from grey to deeper and deeper red: 3-space grows at every height $z$. The black line is the factor $1$; left of it, near the tip, the small warp makes the factor smaller than $1$ although $a_4 > 0$. Right: the colour deepens to blue from left to right: the extra times shrink at every $z$, fastest where the warp is small as well.

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
