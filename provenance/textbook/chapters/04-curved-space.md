## 4. Curved space from zero

In Einstein's theory, gravity is not a force that acts inside space and time. It is the shape of space and time itself. A heavy body bends the geometry around it, and every other body moves along the straightest paths that the bent geometry allows. This chapter builds, from nothing, the geometry that the dirac16complex project uses. We start with coordinates on a space of eight dimensions and the metric, which measures lengths and time intervals. Then come the Christoffel symbols, which say how to differentiate when the coordinates are curved, the geodesics (the straightest paths), the curvature, and the field equations of gravity: the Einstein equations and their higher-order relatives, the Einstein-Lovelock equations. A spinor field such as dirac16complex needs more structure than a metric. It needs, at every point, a set of eight reference directions that are perpendicular to each other and of unit length. This set is the vielbein. It also needs a rule, the spin connection, that says how these directions turn from point to point. The vielbein postulate fixes that rule, and with it we build the covariant derivative of a spinor. At the end of the chapter we can say exactly why the contraction that the author's notebook uses for the spin connection is wrong, and we check the claim with small numbers.

### 4.1 What this chapter does, and what it needs

**What it delivers.** The chapter derives, step by step:

- the transformation rules of vectors, covectors and tensors, and the metric with its signature and volume element;
- the covariant derivative, and the unique Christoffel symbols of a metric (the Levi-Civita connection);
- the geodesic equation, solved completely in one worked example;
- the Riemann curvature tensor, its symmetries, the Ricci tensor, the scalar curvature, the Bianchi identities and the Einstein tensor;
- the Einstein equations and the Einstein-Lovelock equations, with an honest account of what the project computes with them;
- the vielbein, the spin connection, the vielbein postulate and its unique solution;
- the covariant derivative of a spinor, its behaviour under a change of frame, the curvature of the spinor connection, and the square of the Dirac operator;
- the error in the notebook's contraction of the spin connection.

Every general formula is tried on small examples (the flat plane in polar coordinates, the sphere, a two-dimensional spinor), and then on the primordial field of the author's notebook, whose Christoffel symbols and spin connection we derive completely.

**What it needs from Chapter 1.** Columns of numbers (vectors), matrices, the matrix product, the transpose, the inverse and the determinant; indices counted from 0; the Kronecker delta $\delta^\mu{}_\nu$, which is 1 if $\mu=\nu$ and 0 otherwise; partial derivatives and the chain rule in several variables. We repeat the chain rule because it is the engine of this chapter. If a function $f$ depends on variables $y^0,\dots,y^{n-1}$, and each $y^\nu$ depends on variables $x^0,\dots,x^{n-1}$, then

$$
\frac{\partial f}{\partial x^\mu}=\sum_{\nu=0}^{n-1}\frac{\partial f}{\partial y^\nu}\,\frac{\partial y^\nu}{\partial x^\mu}.
$$

For smooth functions (functions whose partial derivatives of every order exist and are continuous) mixed partial derivatives do not depend on the order: $\partial_\mu\partial_\nu f=\partial_\nu\partial_\mu f$, where $\partial_\mu$ is short for $\partial/\partial x^\mu$.

**The summation convention.** When an index appears twice in a product, once as an upper index and once as a lower index, it is summed over all its values. So $V^\mu W_\mu$ means $V^0W_0+V^1W_1+\dots+V^{n-1}W_{n-1}$, and $g_{\mu\nu}V^\nu$ means $\sum_\nu g_{\mu\nu}V^\nu$. An index that appears only once is free: an equation with a free index $\mu$ is $n$ equations, one for each value of $\mu$. Where we do not want a sum over a repeated index we write "(no sum)".

**Names of indices.** $n$ is the dimension of the space: $n=8$ for the project, $n=2$ in the small examples. Greek letters $\alpha,\beta,\lambda,\mu,\nu,\rho,\sigma$ are coordinate indices and run from 0 to $n-1$. Latin letters $a,b,c,d,e,f$ are frame indices (Section 4.10) and also run from 0 to $n-1$. We never use $\gamma$ as an index, because $\gamma$ names the gamma matrices.

**Coordinates.** The notebook and the Stage documents name the eight coordinates $x_0,\dots,x_7$. In formulas with indices we write them $x^\mu$, with the index up, because their small changes $dx^\mu$ are the components of a vector (Section 4.3). The names $x_4$ and $x^4$ denote the same coordinate, the evolution time; we never lower the index of a coordinate. The roles are those of the notebook: $x^0$ is a hidden space direction, $x^1,x^2,x^3$ are ordinary 3-space, $x^4$ is the evolution time, and $x^5,x^6,x^7$ are three extra time directions. The flat metric is

$$
\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1),
$$

so directions 0 to 3 are space-like and 4 to 7 are time-like: the signature is (4,4).

**What it needs from Chapter 2.** The eight real 16 by 16 gamma matrices $\gamma^0,\dots,\gamma^7$ of the notebook, with the Clifford relation $\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}\,1$; the 28 spin generators $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$, where $[A,B]=AB-BA$ is the commutator (and $\{A,B\}=AB+BA$ the anticommutator); the charge matrix $C=\gamma^0\gamma^1\gamma^2\gamma^3$; and three facts proved there and verified by the Stage-1 algebra reports:

- (F1) the only complex 16 by 16 matrices that commute with all eight $\gamma^a$ are the multiples of the identity (Stage 1, Result 4.1; check `ALG_pinIrreducibleComplex` in `wolfram-algebra-report.json` and `python-algebra-report.json`);
- (F2) the 256 ordered products $\gamma^{a_1}\cdots\gamma^{a_k}$ with $a_1<\dots<a_k$ (including the identity, $k=0$) are linearly independent; in particular the eight $\gamma^a$ are linearly independent, and so are the 28 matrices $S^{ab}=\tfrac12\gamma^a\gamma^b$ with $a<b$ (Stage 1, Result 3.2; check `ALG_faithful`);
- (F3) $(S^{ab})^TC=-CS^{ab}$ for all $a,b$ (Stage 1, Result 3.5; check `ALG_spinTransposeProperties`).

Section 4.12 also uses, from Chapter 2, the Dirac adjoint $\bar\Psi=\Psi^\dagger C$ (Section 2.9), the identity $R^TCR=C$ for an exponential $R=\exp(\theta S^{ab})$ (Section 2.11), and, from Section 2.14, the groups Pin(4,4) and Spin(4,4), their part $\mathrm{Spin}_0(4,4)$ connected to 1, the spinor norm (Theorem 2.8) and the vector action $\Lambda_{\mathrm u}$ (Theorem 2.9).

For the two-dimensional spinor examples we use the Pauli matrices $\sigma_x,\sigma_y,\sigma_z$ of Section 2.3 under their numbered names, defined there, $\sigma_1=\sigma_x$, $\sigma_2=\sigma_y$, $\sigma_3=\sigma_z$:

$$
\sigma_1=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\qquad \sigma_2=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\qquad \sigma_3=\begin{pmatrix}1&0\\ 0&-1\end{pmatrix},
$$

which satisfy $\sigma_k^2=1$, $\sigma_1\sigma_2=i\sigma_3$, $\sigma_2\sigma_3=i\sigma_1$, $\sigma_3\sigma_1=i\sigma_2$, and anticommute in pairs. Multiplying out the matrices checks each of these in a line.

### 4.2 Manifolds and coordinates

**The idea.** The surface of the Earth is curved, but a small piece of it looks flat, and on such a piece we can label every point by two numbers, for example latitude and longitude. A manifold is a space with this property: near each of its points it can be labelled by $n$ real numbers, and the labels of overlapping pieces are related by smooth formulas.

**Definition (chart, manifold).** A set $U$ of $\mathbb R^n$ is open if with each of its points it also contains a small ball around that point. A chart on a set $M$ is a part $U$ of $M$ together with a one-to-one map that assigns to each point $p$ of $U$ its $n$ coordinates $(x^0(p),\dots,x^{n-1}(p))$, such that the image is an open set of $\mathbb R^n$. A manifold of dimension $n$ is a set covered by charts such that, wherever two charts overlap, the coordinates of one chart are smooth functions of the coordinates of the other, and conversely. Such a pair of formulas $x'^\mu=x'^\mu(x)$, $x^\mu=x^\mu(x')$ is a change of coordinates.

**The Jacobian matrix.** For a change of coordinates the $n$ by $n$ matrices $\partial x'^\mu/\partial x^\nu$ and $\partial x^\mu/\partial x'^\nu$ are inverse to each other. To see this, apply the chain rule to the identity $x'^\mu(x(x'))=x'^\mu$ and differentiate with respect to $x'^\rho$:

$$
\frac{\partial x'^\mu}{\partial x^\nu}\,\frac{\partial x^\nu}{\partial x'^\rho}=\frac{\partial x'^\mu}{\partial x'^\rho}=\delta^\mu{}_\rho .
$$

The same argument with the primes exchanged gives $(\partial x^\mu/\partial x'^\nu)(\partial x'^\nu/\partial x^\rho)=\delta^\mu{}_\rho$.

**Example 1: the plane.** The Cartesian chart $(x,y)$ covers the whole plane. The polar chart $(r,\varphi)$ with $r>0$ and $0<\varphi<2\pi$ covers the plane without the half-line $y=0$, $x\ge0$; the change of coordinates is $x=r\cos\varphi$, $y=r\sin\varphi$. Its Jacobian matrix and determinant are

$$
\frac{\partial(x,y)}{\partial(r,\varphi)}=\begin{pmatrix}\cos\varphi&-r\sin\varphi\\ \sin\varphi&r\cos\varphi\end{pmatrix},\qquad \det=r\cos^2\varphi+r\sin^2\varphi=r>0 .
$$

At $r=0$ the determinant vanishes and the polar chart fails, although nothing is wrong with the plane there. This is our first example of a coordinate singularity: a failure of the labels, not of the space.

**Example 2: the sphere.** On the sphere of radius $a$ the chart $(\theta,\varphi)$ with $0<\theta<\pi$ and $0<\varphi<2\pi$ labels the point with Cartesian position $(a\sin\theta\cos\varphi,\ a\sin\theta\sin\varphi,\ a\cos\theta)$. It misses the two poles and one half-circle between them; a second chart covers those.

**Example 3: the project.** The project works on an 8-dimensional manifold $M$ with coordinates $x^0,\dots,x^7$. For the primordial field of the notebook (Chapter 9) the chart is described by $z=6Hx^0$ and $t=Hx^4$, where $H>0$ is the notebook's single inverse length, and $z$ runs over the interval $(0,\pi/2)$. At $z=\pi/2$ this chart ends: the metric component $g_{00}=\cot^2z$ of Section 4.4 vanishes there. In the coordinate $\zeta=\ln(\sin z)/(6H)$ the same metric (Section 4.4) is perfectly regular at $\zeta=0$, which corresponds to $z=\pi/2$. (The Stage-2 document, §4.4, verifies this form of the metric with the check `P_zeta_warpedMetric` in `wolfram-primordial-report.json` and records its regularity at $\zeta=0$ as an observation read off from it.) As in the plane, a formula that breaks down may be a failure of the chart, not of the space.

### 4.3 Vectors, covectors and tensors

**Tangent vectors.** A curve is a smooth map from an interval of a parameter $\lambda$ into the manifold, written in a chart as $x^\mu(\lambda)$. Its velocity at a point has the components $u^\mu=dx^\mu/d\lambda$. In another chart the same curve is $x'^\mu(\lambda)=x'^\mu(x(\lambda))$, and by the chain rule

$$
u'^\mu=\frac{dx'^\mu}{d\lambda}=\frac{\partial x'^\mu}{\partial x^\nu}\,\frac{dx^\nu}{d\lambda}=\frac{\partial x'^\mu}{\partial x^\nu}\,u^\nu .
$$

**Definition (vector).** A vector at a point $p$ is an assignment of $n$ numbers $V^\mu$ to every chart around $p$ such that the numbers of two charts are related by

$$
V'^\mu=\frac{\partial x'^\mu}{\partial x^\nu}\,V^\nu .
$$

The index of a vector is written up. A vector field assigns a vector to every point.

**Covectors.** The gradient of a function $f$ has the components $W_\mu=\partial_\mu f$. By the chain rule, $\partial f/\partial x'^\mu=(\partial x^\nu/\partial x'^\mu)\,\partial f/\partial x^\nu$. A covector at $p$ is an assignment of $n$ numbers $W_\mu$ to every chart such that

$$
W'_\mu=\frac{\partial x^\nu}{\partial x'^\mu}\,W_\nu .
$$

The index of a covector is written down. Note that the Jacobian matrix is the inverse one: $\partial x/\partial x'$ instead of $\partial x'/\partial x$.

**The contraction of an upper with a lower index is the same in every chart.** For a vector $V$ and a covector $W$,

$$
V'^\mu W'_\mu=\frac{\partial x'^\mu}{\partial x^\alpha}\,\frac{\partial x^\beta}{\partial x'^\mu}\,V^\alpha W_\beta=\delta^\beta{}_\alpha V^\alpha W_\beta=V^\alpha W_\alpha ,
$$

where we used the Jacobian identity of Section 4.2. In particular the rate of change of $f$ along a curve, $df/d\lambda=u^\mu\partial_\mu f$, does not depend on the chart, as it must not.

**Tensors.** A tensor with $p$ upper and $q$ lower indices has components that transform with one factor $\partial x'/\partial x$ for each upper index and one factor $\partial x/\partial x'$ for each lower index; for example

$$
T'^\mu{}_\nu=\frac{\partial x'^\mu}{\partial x^\alpha}\,\frac{\partial x^\beta}{\partial x'^\nu}\,T^\alpha{}_\beta .
$$

Five rules follow directly from the definition. (i) Sums of tensors of the same type are tensors. (ii) Products of tensors are tensors (the factors simply multiply). (iii) Contracting one upper index with one lower index of a tensor gives a tensor; the proof is the computation just made for $V^\mu W_\mu$. (iv) The Kronecker delta is a tensor with the same components in every chart: $(\partial x'^\mu/\partial x^\alpha)(\partial x^\beta/\partial x'^\nu)\delta^\alpha{}_\beta=\delta^\mu{}_\nu$ by the Jacobian identity. (v) If a tensor equation $A=B$ holds in one chart, it holds in every chart, because both sides transform by the same linear rule; in particular a tensor that vanishes at a point in one chart vanishes there in every chart. Rule (v) is used again and again: to prove a tensor identity at a point it is enough to prove it in one well-chosen chart.

**A warning about index positions.** Summing an upper index with another upper index does not give a chart-independent result. The smallest example has one dimension: under the change $x'=2x$ two vectors $V$ and $W$ become $V'=2V$ and $W'=2W$, so the "sum" $V'W'=4VW$ depends on the chart. Section 4.14 shows that the notebook makes exactly this kind of error with the frame indices of the spin connection.

**Worked example: a constant vector in polar coordinates.** In the plane, take the vector field $V$ that points along the $x$-axis with unit length everywhere: Cartesian components $(V^x,V^y)=(1,0)$. With $r=\sqrt{x^2+y^2}$ and $\varphi$ the polar angle, $\partial r/\partial x=x/r=\cos\varphi$ and $\partial\varphi/\partial x=-y/r^2=-\sin\varphi/r$. The polar components are therefore

$$
V^r=\frac{\partial r}{\partial x}\cdot1+\frac{\partial r}{\partial y}\cdot0=\cos\varphi,\qquad V^\varphi=\frac{\partial\varphi}{\partial x}\cdot1+\frac{\partial\varphi}{\partial y}\cdot0=-\frac{\sin\varphi}{r}.
$$

At the point $(x,y)=(0,1)$, where $r=1$ and $\varphi=\pi/2$, this gives $V^r=0$ and $V^\varphi=-1$: moving along $+x$ from that point decreases the polar angle, as a sketch shows. The field is constant, yet its polar components change from point to point. The plain derivative $\partial_\mu V^\nu$ is therefore not a good measure of how a vector field changes. Section 4.5 repairs this.

### 4.4 The metric

**Lengths.** In the flat plane with Cartesian coordinates, Pythagoras gives the squared length of a small step: $ds^2=dx^2+dy^2$. In general coordinates, and in a curved space, the squared length of a small step $dx^\mu$ is a quadratic expression

$$
ds^2=g_{\mu\nu}(x)\,dx^\mu dx^\nu ,
$$

with coefficients $g_{\mu\nu}=g_{\nu\mu}$ that may depend on the point. The symmetric matrix $(g_{\mu\nu})$ is the metric. We require it to be invertible at every point, and we write $g^{\mu\nu}$ for the entries of its inverse: $g^{\mu\lambda}g_{\lambda\nu}=\delta^\mu{}_\nu$.

**The metric is a tensor with two lower indices.** The squared length of a step is a property of the step, not of the chart. With $dx^\alpha=(\partial x^\alpha/\partial x'^\mu)\,dx'^\mu$,

$$
g_{\alpha\beta}\,dx^\alpha dx^\beta=g_{\alpha\beta}\frac{\partial x^\alpha}{\partial x'^\mu}\frac{\partial x^\beta}{\partial x'^\nu}\,dx'^\mu dx'^\nu ,
\qquad\text{hence}\qquad
g'_{\mu\nu}=\frac{\partial x^\alpha}{\partial x'^\mu}\frac{\partial x^\beta}{\partial x'^\nu}\,g_{\alpha\beta}.
$$

(The coefficients of a quadratic form are fixed once we require them to be symmetric, so the two sides can be compared term by term.) This is the transformation law of a tensor with two lower indices. The inverse $g^{\mu\nu}$ is then a tensor with two upper indices: the inverse of the transformed matrix is the transformed inverse, as one checks by multiplying.

**Worked example: the plane in polar coordinates.** From $x=r\cos\varphi$, $y=r\sin\varphi$: $dx=\cos\varphi\,dr-r\sin\varphi\,d\varphi$ and $dy=\sin\varphi\,dr+r\cos\varphi\,d\varphi$. Squaring and adding, the cross terms $\mp2r\sin\varphi\cos\varphi\,dr\,d\varphi$ cancel and

$$
ds^2=dr^2+r^2d\varphi^2,\qquad g=\begin{pmatrix}1&0\\ 0&r^2\end{pmatrix},\qquad g^{-1}=\begin{pmatrix}1&0\\ 0&r^{-2}\end{pmatrix}.
$$

**Worked example: the sphere.** The point $(X,Y,Z)=(a\sin\theta\cos\varphi,\ a\sin\theta\sin\varphi,\ a\cos\theta)$ moves by $dX=a(\cos\theta\cos\varphi\,d\theta-\sin\theta\sin\varphi\,d\varphi)$, $dY=a(\cos\theta\sin\varphi\,d\theta+\sin\theta\cos\varphi\,d\varphi)$, $dZ=-a\sin\theta\,d\theta$. In $dX^2+dY^2$ the cross terms cancel, and $\cos^2\theta\,d\theta^2+\sin^2\theta\,d\theta^2=d\theta^2$ gives

$$
ds^2=a^2\bigl(d\theta^2+\sin^2\theta\,d\varphi^2\bigr).
$$

**Raising and lowering indices.** The metric turns a vector into a covector, $V_\mu:=g_{\mu\nu}V^\nu$, and the inverse metric turns a covector into a vector, $W^\mu:=g^{\mu\nu}W_\nu$. Doing both returns the original, because $g^{\mu\lambda}g_{\lambda\nu}=\delta^\mu{}_\nu$. The same rule raises or lowers any index of any tensor. The squared length of a vector is $g(V,V)=g_{\mu\nu}V^\mu V^\nu=V^\mu V_\mu$.

**Signature.** At a point, the symmetric matrix $(g_{\mu\nu})$ has real eigenvalues. The numbers of positive and of negative eigenvalues form the signature. A theorem of linear algebra, Sylvester's law of inertia, says that the signature does not depend on the chart; we quote it without proof. The flat space of the project has, in Cartesian coordinates, $g_{\mu\nu}=\eta_{\mu\nu}$: signature (4,4). A vector is called space-like if $g(V,V)>0$, time-like if $g(V,V)<0$ and null if $g(V,V)=0$ but $V\ne0$. In signature (4,4) there are four mutually perpendicular time-like directions, and null vectors are easy to write down: in flat space the vector with components $V^0=V^4=1$ and all others 0 has $g(V,V)=1-1=0$. The project chooses $x^4$ as the time in which everything evolves; the other three time directions are the extra times. Chapter 8 shows what this choice costs in the quantum theory.

**Worked example: the primordial field.** The notebook's metric MatrixMetric44 (Stage-2 document, §4) is diagonal:

$$
\begin{aligned}
ds^2={}&\cot^2z\,(dx^0)^2+s^{1/3}e^{2a_4}\bigl((dx^1)^2+(dx^2)^2+(dx^3)^2\bigr)-(dx^4)^2\\
&-s^{1/3}e^{-2a_4}\bigl((dx^5)^2+(dx^6)^2+(dx^7)^2\bigr),\qquad z=6Hx^0,\quad t=Hx^4,\quad s=\sin z,
\end{aligned}
$$

where $a_4(t)$ is an arbitrary smooth real function and a prime means $d/dt$, so that $\partial_4a_4=Ha_4'$. For $z$ in $(0,\pi/2)$ the diagonal entries have the signs $(+,+,+,+,-,-,-,-)$, so the signature is (4,4) (check `P_metric_signature44` in `wolfram-primordial-report.json`). Three-space expands with the scale factor $s^{1/6}e^{a_4}$ when $a_4$ grows, and the three extra times contract with the scale factor $s^{1/6}e^{-a_4}$. Chapter 9 discusses this field in detail; here it serves as the running example.

**Worked example: a change of coordinates in the primordial field.** Put $\zeta=\ln(\sin z)/(6H)$, which runs over $(-\infty,0)$ when $z$ runs over $(0,\pi/2)$. Then $d\zeta=\frac{1}{6H}\,\frac{\cos z}{\sin z}\,dz=\cot z\,dx^0$, because $dz=6H\,dx^0$. So $\cot^2z\,(dx^0)^2=d\zeta^2$. Also $\sin z=e^{6H\zeta}$, so $s^{1/3}=e^{2H\zeta}$, and the metric becomes the warped form

$$
ds^2=d\zeta^2-(dx^4)^2+e^{2H\zeta}\Bigl[e^{2a_4}\bigl((dx^1)^2+(dx^2)^2+(dx^3)^2\bigr)-e^{-2a_4}\bigl((dx^5)^2+(dx^6)^2+(dx^7)^2\bigr)\Bigr]
$$

(Stage-2 document, §4.4; check `P_zeta_warpedMetric`). All six transverse directions share the warp factor $e^{2H\zeta}$.

**The volume element.** Take determinants in the transformation law of the metric: $\det g'=(\det J)^2\det g$ with $J=(\partial x^\alpha/\partial x'^\mu)$. Hence $\sqrt{\lvert\det g'\rvert}=\lvert\det J\rvert\sqrt{\lvert\det g\rvert}$. The change-of-variables rule of integral calculus says $d^nx=\lvert\det J\rvert\,d^nx'$ for the coordinate volume elements. Together,

$$
\sqrt{\lvert g'\rvert}\;d^nx'=\sqrt{\lvert g\rvert}\;d^nx,\qquad \lvert g\rvert:=\lvert\det(g_{\mu\nu})\rvert :
$$

$\sqrt{\lvert g\rvert}\,d^nx$ is the invariant volume element. In polar coordinates $\sqrt{\lvert g\rvert}=r$, giving the familiar area element $r\,dr\,d\varphi$. On the sphere $\sqrt{\lvert g\rvert}=a^2\sin\theta$, and the total area is $\int_0^\pi\int_0^{2\pi}a^2\sin\theta\,d\varphi\,d\theta=4\pi a^2$.

**Worked example: the determinant of the primordial field.** The determinant of a diagonal matrix is the product of its diagonal entries:

$$
\det g=\cot^2z\cdot\bigl(s^{1/3}e^{2a_4}\bigr)^3\cdot(-1)\cdot\bigl(-s^{1/3}e^{-2a_4}\bigr)^3=\cot^2z\cdot s^2\cdot(-1)(-1)^3=\cos^2z .
$$

The sign is $+$ because there are four negative entries. So $\sqrt{\lvert g\rvert}=\cos z$ on $(0,\pi/2)$ (checks `P_metric_detG_equals_plus_cos2z` and `P_metric_sqrtAbsDetG_cosz`). The Stage-2 specification had written $\det g=-\cos^2z$; the exact computation corrected it. Since $\sqrt{\lvert g\rvert}$ does not depend on $x^4$, the growth of 3-space is exactly compensated by the shrinking of the extra times. To say this precisely, take a region with fixed coordinate ranges in the seven directions other than $x^4$ (a comoving region: its points keep their coordinates while $x^4$ runs, like the freely falling observers of Section 4.6). Delete the row and the column of $x^4$ from the metric. What remains is the 7 by 7 block that measures lengths within a slice $x^4=$ constant. Since $g$ is diagonal, this block is diagonal too, and its diagonal entries are the seven diagonal entries of $g$ other than $g_{44}=-1$. The determinant of a diagonal matrix is the product of its diagonal entries (Section 1.4), so $\det g=g_{44}\times(\text{product of the other seven diagonal entries})=-1\times\det(\text{block})$. So the absolute value of the determinant of the block equals $\lvert g\rvert=\cos^2z$, and the invariant volume element of the block is $\sqrt{\cos^2z}\,d^7x=\cos z\,d^7x$. The 7-volume of the region is its integral, $\int\cos z\,d^7x$ over the seven coordinates other than $x^4$, and it does not change with $x^4$.

### 4.5 The covariant derivative and the Christoffel symbols

**The problem.** Differentiate the transformation law of a vector field, $V'^\mu=(\partial x'^\mu/\partial x^\alpha)V^\alpha$, with respect to $x'^\nu$, using the chain rule $\partial/\partial x'^\nu=(\partial x^\beta/\partial x'^\nu)\,\partial/\partial x^\beta$:

$$
\partial'_\nu V'^\mu=\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x^\beta}{\partial x'^\nu}\,\partial_\beta V^\alpha+\frac{\partial x^\beta}{\partial x'^\nu}\,\frac{\partial^2x'^\mu}{\partial x^\beta\partial x^\alpha}\,V^\alpha .
$$

The first term is the transformation law of a tensor; the second term, with second derivatives of the coordinate change, spoils it. So $\partial_\nu V^\mu$ is not a tensor, as the polar example of Section 4.3 showed.

**Definition (covariant derivative).** We add a correction that is linear in $V$:

$$
\nabla_\nu V^\mu:=\partial_\nu V^\mu+\Gamma^\mu{}_{\nu\lambda}V^\lambda .
$$

The $n^3$ numbers $\Gamma^\mu{}_{\nu\lambda}$ at each point are the connection coefficients. They are chosen so that $\nabla_\nu V^\mu$ is a tensor. Requiring $\nabla'_\nu V'^\mu=(\partial x'^\mu/\partial x^\alpha)(\partial x^\beta/\partial x'^\nu)\nabla_\beta V^\alpha$ for every $V$ and inserting the formula above gives the rule by which the $\Gamma$ must change between charts:

$$
\Gamma'^\mu{}_{\nu\lambda}=\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x^\beta}{\partial x'^\nu}\frac{\partial x^\sigma}{\partial x'^\lambda}\,\Gamma^\alpha{}_{\beta\sigma}-\frac{\partial x^\beta}{\partial x'^\nu}\frac{\partial x^\sigma}{\partial x'^\lambda}\,\frac{\partial^2x'^\mu}{\partial x^\beta\partial x^\sigma}.
$$

(To obtain it, write $\Gamma'^\mu{}_{\nu\lambda}V'^\lambda$ with $V'^\lambda=(\partial x'^\lambda/\partial x^\sigma)V^\sigma$, collect the coefficient of $V^\sigma$, and multiply by $\partial x^\sigma/\partial x'^\lambda$.) The last term is the inhomogeneous part; it is what cancels the unwanted term of $\partial'_\nu V'^\mu$. Because of it, the $\Gamma$ are not the components of a tensor. The inhomogeneous part is symmetric in $\nu$ and $\lambda$, because second partial derivatives do not depend on the order.

**Covectors and general tensors.** For a scalar function $f$ (a tensor without indices) we set $\nabla_\nu f=\partial_\nu f$. We require the product rule $\nabla_\nu(V^\mu W_\mu)=(\nabla_\nu V^\mu)W_\mu+V^\mu\nabla_\nu W_\mu$. The left side is $\partial_\nu(V^\mu W_\mu)=(\partial_\nu V^\mu)W_\mu+V^\mu\partial_\nu W_\mu$. Subtracting $(\nabla_\nu V^\mu)W_\mu=(\partial_\nu V^\mu)W_\mu+\Gamma^\mu{}_{\nu\lambda}V^\lambda W_\mu$ leaves, for every $V$,

$$
\nabla_\nu W_\mu=\partial_\nu W_\mu-\Gamma^\lambda{}_{\nu\mu}W_\lambda .
$$

A tensor with several indices gets one term $+\Gamma$ for each upper index and one term $-\Gamma$ for each lower index; for the metric, for example,

$$
\nabla_\rho g_{\mu\nu}=\partial_\rho g_{\mu\nu}-\Gamma^\lambda{}_{\rho\mu}g_{\lambda\nu}-\Gamma^\lambda{}_{\rho\nu}g_{\mu\lambda}.
$$

With this rule the product rule holds for all products and contractions.

**The two conditions of Levi-Civita.** A metric singles out one connection by two natural conditions.

1. No torsion: $\Gamma^\mu{}_{\nu\lambda}=\Gamma^\mu{}_{\lambda\nu}$. (The difference $\Gamma^\mu{}_{\nu\lambda}-\Gamma^\mu{}_{\lambda\nu}$ is a tensor, because the inhomogeneous part is symmetric, so this condition does not depend on the chart.)
2. Metric compatibility: $\nabla_\rho g_{\mu\nu}=0$. Lengths and angles are preserved when vectors are carried along.

**Theorem (Christoffel formula).** Exactly one connection satisfies both conditions, namely

$$
\Gamma^\rho{}_{\mu\nu}=\tfrac12\,g^{\rho\sigma}\bigl(\partial_\mu g_{\nu\sigma}+\partial_\nu g_{\mu\sigma}-\partial_\sigma g_{\mu\nu}\bigr).
$$

These are the Christoffel symbols (of the Levi-Civita connection); the project uses only this connection (Stage 1, §5.1).

*Proof.* Lower the upper index, $\Gamma_{\sigma\mu\nu}:=g_{\sigma\rho}\Gamma^\rho{}_{\mu\nu}$; condition 1 says $\Gamma_{\sigma\mu\nu}=\Gamma_{\sigma\nu\mu}$. Condition 2 reads $\partial_\rho g_{\mu\nu}=\Gamma_{\nu\rho\mu}+\Gamma_{\mu\rho\nu}$. Write it three times with the indices permuted cyclically:

$$
\partial_\mu g_{\nu\rho}=\Gamma_{\rho\mu\nu}+\Gamma_{\nu\mu\rho},\qquad
\partial_\nu g_{\mu\rho}=\Gamma_{\rho\nu\mu}+\Gamma_{\mu\nu\rho},\qquad
\partial_\rho g_{\mu\nu}=\Gamma_{\nu\rho\mu}+\Gamma_{\mu\rho\nu}.
$$

Add the first two and subtract the third. By the symmetry in the last two indices, $\Gamma_{\nu\mu\rho}=\Gamma_{\nu\rho\mu}$ and $\Gamma_{\mu\nu\rho}=\Gamma_{\mu\rho\nu}$ cancel against the third line, and $\Gamma_{\rho\nu\mu}=\Gamma_{\rho\mu\nu}$, so

$$
\partial_\mu g_{\nu\rho}+\partial_\nu g_{\mu\rho}-\partial_\rho g_{\mu\nu}=2\,\Gamma_{\rho\mu\nu}.
$$

Raising the index $\rho$ with $g^{\sigma\rho}$ gives the formula. So any connection with the two properties is this one (uniqueness). Conversely, the formula is symmetric in $\mu,\nu$, and adding $\Gamma_{\nu\rho\mu}+\Gamma_{\mu\rho\nu}$ computed from it gives back $\partial_\rho g_{\mu\nu}$, so it has both properties in the chart where it was computed. It remains to see that the formulas computed in two different charts describe the same $\nabla$. Take the connection computed in the chart $x$, and transform its coefficients to the chart $x'$ with the transformation rule above. The result defines the same operator $\nabla$ in the new chart, so it is still free of torsion and compatible with the metric (both conditions are tensor equations, rule (v) of Section 4.3). By uniqueness in the chart $x'$ it equals the Christoffel formula computed from $g'$. $\square$

**Lemma (derivative of a determinant).** For an invertible matrix $A(x)$ with entries depending on $x$, $\partial_\mu\ln\lvert\det A\rvert=\mathrm{tr}\bigl(A^{-1}\partial_\mu A\bigr)$.

*Proof.* Write $O(\epsilon^2)$ for terms that are at most a constant times $\epsilon^2$ for small $\epsilon$. For a small number $\epsilon$ and a matrix $Y$, $\det(1+\epsilon Y)$ is a sum over permutations of products of entries of $1+\epsilon Y$. The identity permutation gives $\prod_i(1+\epsilon Y_{ii})=1+\epsilon\,\mathrm{tr}\,Y+O(\epsilon^2)$. Every other permutation moves at least two indices and therefore picks at least two off-diagonal entries, each of size $\epsilon$; it contributes $O(\epsilon^2)$. So $\det(1+\epsilon Y)=1+\epsilon\,\mathrm{tr}\,Y+O(\epsilon^2)$. Let $A_\epsilon$ be the value of $A$ at the point where the coordinate $x^\mu$ is increased by $\epsilon$. Then $A_\epsilon=A+\epsilon\,\partial_\mu A+O(\epsilon^2)=A\bigl(1+\epsilon A^{-1}\partial_\mu A+O(\epsilon^2)\bigr)$, and since the determinant of a product is the product of the determinants, $\det A_\epsilon=\det A\,\bigl(1+\epsilon\,\mathrm{tr}(A^{-1}\partial_\mu A)+O(\epsilon^2)\bigr)$. Hence $\ln\lvert\det A_\epsilon\rvert-\ln\lvert\det A\rvert=\epsilon\,\mathrm{tr}(A^{-1}\partial_\mu A)+O(\epsilon^2)$; divide by $\epsilon$ and let $\epsilon\to0$. $\square$

**Consequence: the contracted Christoffel symbol and the divergence.** Contract $\rho$ with $\mu$ in the Christoffel formula:

$$
\Gamma^\rho{}_{\rho\nu}=\tfrac12g^{\rho\sigma}\bigl(\partial_\rho g_{\nu\sigma}+\partial_\nu g_{\rho\sigma}-\partial_\sigma g_{\rho\nu}\bigr)=\tfrac12g^{\rho\sigma}\partial_\nu g_{\rho\sigma}=\partial_\nu\ln\sqrt{\lvert g\rvert},
$$

because $g^{\rho\sigma}\partial_\rho g_{\nu\sigma}$ and $g^{\rho\sigma}\partial_\sigma g_{\rho\nu}$ are equal (rename $\rho\leftrightarrow\sigma$ and use the symmetry of $g$), and $\tfrac12g^{\rho\sigma}\partial_\nu g_{\rho\sigma}=\tfrac12\mathrm{tr}(g^{-1}\partial_\nu g)=\tfrac12\partial_\nu\ln\lvert g\rvert$ by the lemma. Hence the divergence of a vector field is

$$
\nabla_\mu V^\mu=\partial_\mu V^\mu+\Gamma^\mu{}_{\mu\lambda}V^\lambda=\frac{1}{\sqrt{\lvert g\rvert}}\,\partial_\mu\bigl(\sqrt{\lvert g\rvert}\,V^\mu\bigr).
$$

**Diagonal metrics.** All metrics of the project's examples are diagonal: $g_{\mu\nu}=0$ for $\mu\ne\nu$. We write the diagonal entries as $g_{\mu\mu}=\eta_{\mu\mu}h_\mu^2$ (no sum), with positive functions $h_\mu$ (the scale factors) and the signs $\eta_{\mu\mu}=\pm1$. Then $g^{\mu\mu}=\eta_{\mu\mu}/h_\mu^2$. Insert this into the Christoffel formula; only terms with $\sigma=\rho$ survive, and there are four cases (in each, the repeated index $\mu$ is not summed):

$$
\begin{aligned}
&\text{(a)}\quad \Gamma^\mu{}_{\mu\mu}=\tfrac12g^{\mu\mu}\partial_\mu g_{\mu\mu}=\partial_\mu\ln h_\mu ,\\
&\text{(b)}\quad \Gamma^\mu{}_{\mu\nu}=\Gamma^\mu{}_{\nu\mu}=\tfrac12g^{\mu\mu}\partial_\nu g_{\mu\mu}=\partial_\nu\ln h_\mu\qquad(\nu\ne\mu),\\
&\text{(c)}\quad \Gamma^\mu{}_{\nu\nu}=-\tfrac12g^{\mu\mu}\partial_\mu g_{\nu\nu}=-\eta_{\mu\mu}\eta_{\nu\nu}\,\frac{h_\nu}{h_\mu^2}\,\partial_\mu h_\nu\qquad(\nu\ne\mu),\\
&\text{(d)}\quad \Gamma^\mu{}_{\nu\lambda}=0\qquad(\mu,\nu,\lambda\ \text{all different}).
\end{aligned}
$$

For (b): in $\tfrac12g^{\mu\mu}(\partial_\mu g_{\nu\mu}+\partial_\nu g_{\mu\mu}-\partial_\mu g_{\mu\nu})$ the first and last terms vanish because $g_{\nu\mu}=0$ for $\nu\ne\mu$. For (c): $\tfrac12g^{\mu\mu}(2\partial_\nu g_{\nu\mu}-\partial_\mu g_{\nu\nu})$, and $g_{\nu\mu}=0$. For (d): every metric entry that appears has two different indices.

**Worked example: polar coordinates.** With $h_r=1$, $h_\varphi=r$ and both signs $+1$: case (b) gives $\Gamma^\varphi{}_{r\varphi}=\Gamma^\varphi{}_{\varphi r}=\partial_r\ln r=1/r$; case (c) gives $\Gamma^r{}_{\varphi\varphi}=-(r/1)\,\partial_r r=-r$; all others vanish. Now return to the constant field $V^r=\cos\varphi$, $V^\varphi=-\sin\varphi/r$ of Section 4.3:

$$
\begin{aligned}
\nabla_rV^r&=\partial_r\cos\varphi=0,\\
\nabla_\varphi V^r&=\partial_\varphi\cos\varphi+\Gamma^r{}_{\varphi\varphi}V^\varphi=-\sin\varphi+(-r)\Bigl(-\frac{\sin\varphi}{r}\Bigr)=0,\\
\nabla_rV^\varphi&=\partial_r\Bigl(-\frac{\sin\varphi}{r}\Bigr)+\Gamma^\varphi{}_{r\varphi}V^\varphi=\frac{\sin\varphi}{r^2}+\frac1r\Bigl(-\frac{\sin\varphi}{r}\Bigr)=0,\\
\nabla_\varphi V^\varphi&=\partial_\varphi\Bigl(-\frac{\sin\varphi}{r}\Bigr)+\Gamma^\varphi{}_{\varphi r}V^r=-\frac{\cos\varphi}{r}+\frac1r\cos\varphi=0 .
\end{aligned}
$$

The covariant derivative of the constant field vanishes, as it should: the Christoffel terms exactly remove the change of the polar components that comes from the turning of the coordinate lines.

**Worked example: the 37 Christoffel symbols of the primordial field.** The scale factors are $h=(\cot z,\ s^{1/6}e^{a_4}\ (\times3),\ 1,\ s^{1/6}e^{-a_4}\ (\times3))$ with the signs of $\eta$, and they depend on $x^0$ and $x^4$ only. With $\partial_0=6H\,d/dz$ and $\partial_4=H\,d/dt$ the logarithmic derivatives are

$$
\begin{aligned}
&\partial_0\ln\cot z=-\frac{6H}{\sin z\cos z},\qquad \partial_0\ln h_k=H\cot z,\\
&\partial_4\ln h_i=Ha_4',\qquad \partial_4\ln h_j=-Ha_4',
\end{aligned}
$$

for $k\in\{1,2,3,5,6,7\}$, $i\in\{1,2,3\}$ and $j\in\{5,6,7\}$. (For the first: $\frac{d}{dz}\ln\cot z=-\frac{1}{\sin^2z}\cdot\frac{\sin z}{\cos z}$. For the second: $\ln h_k=\tfrac16\ln\sin z\pm a_4$, and $\frac{d}{dz}\tfrac16\ln\sin z=\tfrac16\cot z$.) Now apply the four cases. Case (a) gives only $\Gamma^0{}_{00}$, since $h_0$ is the only scale factor that depends on its own coordinate. Case (b) gives $\Gamma^k{}_{k0}=\Gamma^k{}_{0k}=H\cot z$ and $\Gamma^k{}_{k4}=\Gamma^k{}_{4k}=\pm Ha_4'$. Case (c) with $\mu=0$ gives $\Gamma^0{}_{kk}=-\eta_{kk}\,h_k^2\,\tan^2z\,\partial_0\ln h_k=-\eta_{kk}H\tan z\,h_k^2$, and with $\mu=4$ it gives $\Gamma^4{}_{kk}=\eta_{kk}h_k^2\,\partial_4\ln h_k$. Nothing depends on $x^1,x^2,x^3,x^5,x^6,x^7$, so case (c) with those values of $\mu$ gives zero. The complete list:

| Symbol | Value | Number |
| --- | --- | --- |
| $\Gamma^0{}_{00}$ | $-6H/(\sin z\cos z)$ | 1 |
| $\Gamma^k{}_{0k}=\Gamma^k{}_{k0}$, $k\in\{1,2,3,5,6,7\}$ | $H\cot z$ | 12 |
| $\Gamma^i{}_{4i}=\Gamma^i{}_{i4}$, $i\in\{1,2,3\}$ | $Ha_4'$ | 6 |
| $\Gamma^j{}_{4j}=\Gamma^j{}_{j4}$, $j\in\{5,6,7\}$ | $-Ha_4'$ | 6 |
| $\Gamma^0{}_{ii}$ | $-H\tan z\,s^{1/3}e^{2a_4}$ | 3 |
| $\Gamma^0{}_{jj}$ | $H\tan z\,s^{1/3}e^{-2a_4}$ | 3 |
| $\Gamma^4{}_{ii}$ | $Ha_4'\,s^{1/3}e^{2a_4}$ | 3 |
| $\Gamma^4{}_{jj}$ | $Ha_4'\,s^{1/3}e^{-2a_4}$ | 3 |

In total $1+12+6+6+3+3+3+3=37$ of the $8^3=512$ symbols are nonzero. This is exactly the count and the closed forms that the Stage-2 verifiers found (measurement `christoffelNonzeroCount` = 37 and checks `P_christoffel_count` and `P_christoffel_closedForms512` in `wolfram-primordial-report.json`; `nonzeroOrderedCount` = 37 and check `P_christoffel` in `python-primordial-report.json`; the table of the Stage-2 document, §5, lists the same values with $\sec z/\sin z$ written for $1/(\sin z\cos z)$). As a check of the contracted formula $\Gamma^\rho{}_{\rho\nu}=\partial_\nu\ln\sqrt{\lvert g\rvert}$ with $\sqrt{\lvert g\rvert}=\cos z$:

$$
\sum_\rho\Gamma^\rho{}_{\rho0}=-\frac{6H}{\sin z\cos z}+6H\frac{\cos z}{\sin z}=\frac{6H(\cos^2z-1)}{\sin z\cos z}=-6H\tan z=\partial_0\ln\cos z,
$$

and $\sum_\rho\Gamma^\rho{}_{\rho4}=3Ha_4'-3Ha_4'=0=\partial_4\ln\cos z$.

### 4.6 Geodesics, with one worked example

**Derivative along a curve.** Let $x^\mu(\lambda)$ be a curve with velocity $u^\mu=dx^\mu/d\lambda$, and let $V^\mu(\lambda)$ be a vector given at each point of the curve. If $V$ is the restriction of a vector field, the chain rule gives $dV^\mu/d\lambda=u^\alpha\partial_\alpha V^\mu$, and so

$$
u^\alpha\nabla_\alpha V^\mu=\frac{dV^\mu}{d\lambda}+\Gamma^\mu{}_{\alpha\beta}\,u^\alpha V^\beta=:\frac{DV^\mu}{d\lambda}.
$$

The right-hand side uses only the values of $V$ on the curve, so it defines the covariant derivative along the curve for any $V(\lambda)$. $V$ is parallel transported along the curve if $DV^\mu/d\lambda=0$.

**Definition (geodesic).** A geodesic is a curve whose velocity is parallel transported along itself:

$$
\frac{d^2x^\mu}{d\lambda^2}+\Gamma^\mu{}_{\alpha\beta}\,\frac{dx^\alpha}{d\lambda}\frac{dx^\beta}{d\lambda}=0 .
$$

In flat space with Cartesian coordinates all $\Gamma$ vanish, and the equation says $d^2x^\mu/d\lambda^2=0$: straight lines traversed at constant speed. A geodesic is the curved-space version of a straight line. (Geodesics can also be characterized as curves of stationary length; that needs the calculus of variations of Chapter 5, and we do not use it.) In general relativity, a body on which no force other than gravity acts moves on a time-like geodesic.

**The squared speed is constant along a geodesic.** Differentiate $g_{\mu\nu}u^\mu u^\nu$ along the curve and use the geodesic equation:

$$
\frac{d}{d\lambda}\bigl(g_{\mu\nu}u^\mu u^\nu\bigr)=u^\rho u^\mu u^\nu\,\partial_\rho g_{\mu\nu}+2g_{\mu\nu}u^\mu\frac{du^\nu}{d\lambda}=u^\rho u^\mu u^\nu\,\partial_\rho g_{\mu\nu}-2\Gamma_{\mu\alpha\beta}\,u^\mu u^\alpha u^\beta ,
$$

with $\Gamma_{\mu\alpha\beta}=g_{\mu\nu}\Gamma^\nu{}_{\alpha\beta}$. By the proof of the Christoffel formula, $2\Gamma_{\mu\alpha\beta}=\partial_\alpha g_{\beta\mu}+\partial_\beta g_{\alpha\mu}-\partial_\mu g_{\alpha\beta}$. Contracted with the symmetric product $u^\mu u^\alpha u^\beta$, each of the three terms equals $u^\rho u^\mu u^\nu\partial_\rho g_{\mu\nu}$ after renaming the summed indices, with the signs $+,+,-$. So $2\Gamma_{\mu\alpha\beta}u^\mu u^\alpha u^\beta=u^\rho u^\mu u^\nu\partial_\rho g_{\mu\nu}$, and the derivative is zero. A geodesic that starts time-like stays time-like, and so on.

**Worked example: the straight lines of the plane in polar coordinates.** With the polar Christoffel symbols ($\Gamma^r{}_{\varphi\varphi}=-r$, $\Gamma^\varphi{}_{r\varphi}=\Gamma^\varphi{}_{\varphi r}=1/r$) the geodesic equations are, with a prime meaning $d/d\lambda$ in this example,

$$
r''-r\,\varphi'^2=0,\qquad \varphi''+\frac2r\,r'\varphi'=0 .
$$

The factor 2 in the second equation comes from the two equal terms $\Gamma^\varphi{}_{r\varphi}r'\varphi'$ and $\Gamma^\varphi{}_{\varphi r}\varphi'r'$. We solve them completely.

*Step 1: a conserved quantity.* $\frac{d}{d\lambda}(r^2\varphi')=2rr'\varphi'+r^2\varphi''=r^2\bigl(\varphi''+\tfrac2rr'\varphi'\bigr)=0$. So $r^2\varphi'=L$ is constant (in mechanics, the angular momentum).

*Step 2: the speed.* By the result just proved, $g(u,u)=r'^2+r^2\varphi'^2$ is constant; choose the parameter so that it equals 1 (unit speed, $\lambda$ is then the length along the curve). With $\varphi'=L/r^2$ this reads $r'^2=1-L^2/r^2$.

*Step 3: solve for $r$.* Take $L>0$. (If $L=0$, then $\varphi'=0$, so $\varphi$ is constant, and Step 2 gives $r'^2=1$, in agreement with the first equation, which becomes $r''=0$. So $r=\lambda-\lambda_0$ for $\lambda>\lambda_0$, or $r=\lambda_0-\lambda$ for $\lambda<\lambda_0$: in both cases $r=\lvert\lambda-\lambda_0\rvert$, a radial half-line, the part of a straight line through the origin that the polar chart sees, since the chart excludes $r=0$. If $L<0$, replace $\varphi$ by $-\varphi$ (mod $2\pi$). This leaves the two geodesic equations unchanged, because each term of the second contains exactly one factor $\varphi'$ or $\varphi''$ and the first contains $\varphi'^2$, and it flips the sign of $L$. So the solutions with $L<0$ are the mirror images of those found below: Steps 3 to 5 hold with $\lvert L\rvert$ in place of $L$ and $\varphi$ replaced by $-\varphi$, which gives the straight lines $r\cos(\varphi-\varphi_0)=\lvert L\rvert$ traversed in the opposite sense.) Since $r'^2\ge0$, $r\ge L$. Where $r'>0$, $\frac{d}{d\lambda}\sqrt{r^2-L^2}=\frac{rr'}{\sqrt{r^2-L^2}}=\frac{r}{\sqrt{r^2-L^2}}\sqrt{1-\frac{L^2}{r^2}}=1$. So $\sqrt{r^2-L^2}=\lambda-\lambda_0$ for $\lambda>\lambda_0$, and with the other sign of $r'$ for $\lambda<\lambda_0$: in both cases

$$
r(\lambda)^2=L^2+(\lambda-\lambda_0)^2 .
$$

*Step 4: solve for $\varphi$.* $\varphi'=L/r^2=L/(L^2+(\lambda-\lambda_0)^2)$, whose antiderivative is $\arctan((\lambda-\lambda_0)/L)$. So $\varphi(\lambda)=\varphi_0+\arctan((\lambda-\lambda_0)/L)$.

*Step 5: recognize the curve.* From step 4, $\cos(\varphi-\varphi_0)=L/\sqrt{L^2+(\lambda-\lambda_0)^2}=L/r$, so

$$
r\cos(\varphi-\varphi_0)=L ,
$$

which is the straight line at distance $L$ from the origin, perpendicular to the direction $\varphi_0$. The geodesics of the plane are its straight lines, now derived in coordinates in which they look nothing like straight lines.

*A check with small numbers.* Take $L=1$, $\varphi_0=0$, $\lambda_0=0$: $r=\sqrt{1+\lambda^2}$ and $\varphi=\arctan\lambda$, so $x=r\cos\varphi=1$ and $y=r\sin\varphi=\lambda$: the vertical line $x=1$, traversed at unit speed. At $\lambda=1$: $r=\sqrt2$, $\varphi=\pi/4$, $r'=\lambda/\sqrt{1+\lambda^2}=1/\sqrt2$, $\varphi'=1/(1+\lambda^2)=1/2$, $r''=(1+\lambda^2)^{-3/2}=1/(2\sqrt2)$ and $\varphi''=-2\lambda/(1+\lambda^2)^2=-1/2$. Then $r''-r\varphi'^2=\frac{1}{2\sqrt2}-\frac{\sqrt2}{4}=0$, $\varphi''+\frac2rr'\varphi'=-\frac12+\frac{2}{\sqrt2}\cdot\frac{1}{\sqrt2}\cdot\frac12=0$, and $r'^2+r^2\varphi'^2=\frac12+2\cdot\frac14=1$.

**Geodesics in the primordial field.** Exercise 4.3 shows that the curves on which only $x^4$ changes, $x^\mu(\lambda)=(c^0,c^1,c^2,c^3,\lambda,c^5,c^6,c^7)$ with constants $c$, are time-like geodesics for every function $a_4$. The proper time along a time-like curve is $\tau=\int\sqrt{-g_{\mu\nu}u^\mu u^\nu}\,d\lambda$, the time shown by a clock carried along it (the time-like analogue of the length of Exercise 4.1(b)). For these curves $u^\mu=\delta^\mu{}_4$ and $g_{44}=-1$, so $d\tau/d\lambda=1$, and the proper time counted from $x^4=0$ is $\tau=\lambda=x^4$. Observers at fixed $x^0,\dots,x^3,x^5,\dots,x^7$ are therefore freely falling, and $x^4$ is their proper time. A chart with this property ($g_{44}=-1$ and $g_{4\mu}=0$ for $\mu\ne4$) is called Gaussian normal; the project uses it whenever it speaks of the energy density $\rho=T_{44}$ (Chapter 7).

### 4.7 Curvature

**The idea.** On a flat sheet of paper, a vector carried around a closed loop by parallel transport comes back unchanged. On a sphere it does not: carry a vector from the north pole down to the equator, a quarter of the way along the equator, and back up to the pole, keeping it parallel all the time, and it returns turned by a right angle. Curvature measures this failure. For a very small loop it is measured by the commutator of two covariant derivatives: in flat Cartesian coordinates $\nabla_\mu\nabla_\nu=\partial_\mu\partial_\nu$, and partial derivatives commute; in a curved space covariant derivatives do not.

**Theorem (the Riemann tensor).** For every vector field $V$,

$$
\nabla_\mu\nabla_\nu V^\rho-\nabla_\nu\nabla_\mu V^\rho=R^\rho{}_{\sigma\mu\nu}V^\sigma ,\qquad
R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}.
$$

This is the convention of the whole project (Stage 1, §5.5; measurement `convention.curvature` of `wolfram-geometry-report.json`).

*Proof.* $\nabla_\nu V^\rho$ has one lower index $\nu$ and one upper index $\rho$, so by the rule of Section 4.5

$$
\nabla_\mu\nabla_\nu V^\rho=\partial_\mu\bigl(\partial_\nu V^\rho+\Gamma^\rho{}_{\nu\sigma}V^\sigma\bigr)+\Gamma^\rho{}_{\mu\lambda}\bigl(\partial_\nu V^\lambda+\Gamma^\lambda{}_{\nu\sigma}V^\sigma\bigr)-\Gamma^\lambda{}_{\mu\nu}\nabla_\lambda V^\rho .
$$

Expand and subtract the same expression with $\mu$ and $\nu$ exchanged. Three kinds of terms drop out because they are symmetric in $\mu,\nu$: $\partial_\mu\partial_\nu V^\rho$ (partial derivatives commute); $\Gamma^\rho{}_{\nu\sigma}\partial_\mu V^\sigma+\Gamma^\rho{}_{\mu\sigma}\partial_\nu V^\sigma$ (after renaming $\lambda$ to $\sigma$); and $\Gamma^\lambda{}_{\mu\nu}\nabla_\lambda V^\rho$ (no torsion). What remains is $(\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma})V^\sigma$. $\square$

The left-hand side is a tensor for every $V$ and depends linearly on $V$ with no derivatives of $V$; therefore $R^\rho{}_{\sigma\mu\nu}$ transforms as a tensor with one upper and three lower indices (write the transformation law of both sides and compare the coefficients of $V^\sigma$).

**Other tensors.** For a function $f$, $\nabla_\mu\nabla_\nu f-\nabla_\nu\nabla_\mu f=-(\Gamma^\lambda{}_{\mu\nu}-\Gamma^\lambda{}_{\nu\mu})\partial_\lambda f=0$. For a covector, apply the commutator to the function $V^\rho W_\rho$. By the product rule, $\nabla_\mu\nabla_\nu(V^\rho W_\rho)$ has four terms; the two mixed ones, $(\nabla_\mu V^\rho)(\nabla_\nu W_\rho)+(\nabla_\nu V^\rho)(\nabla_\mu W_\rho)$, are symmetric in $\mu,\nu$ and cancel in the commutator. So $0=(R^\rho{}_{\sigma\mu\nu}V^\sigma)W_\rho+V^\rho[\nabla_\mu,\nabla_\nu]W_\rho$ for all $V$, that is

$$
[\nabla_\mu,\nabla_\nu]W_\sigma=-R^\rho{}_{\sigma\mu\nu}W_\rho .
$$

Every tensor is a sum of products of vectors and covectors (expand it in a basis), so for a general tensor the commutator gives one term $+R$ for each upper index and one term $-R$ for each lower index.

**Symmetries.** Lower the first index, $R_{\rho\sigma\mu\nu}:=g_{\rho\lambda}R^\lambda{}_{\sigma\mu\nu}$.

- (S1) $R_{\rho\sigma\mu\nu}=-R_{\rho\sigma\nu\mu}$. This is visible in the definition.
- (S2) $R_{\rho\sigma\mu\nu}=-R_{\sigma\rho\mu\nu}$. Proof: since $\nabla g=0$, $0=[\nabla_\mu,\nabla_\nu]g_{\rho\sigma}=-R^\lambda{}_{\rho\mu\nu}g_{\lambda\sigma}-R^\lambda{}_{\sigma\mu\nu}g_{\rho\lambda}=-R_{\sigma\rho\mu\nu}-R_{\rho\sigma\mu\nu}$.
- (S3) First Bianchi identity: $R^\rho{}_{\sigma\mu\nu}+R^\rho{}_{\mu\nu\sigma}+R^\rho{}_{\nu\sigma\mu}=0$. Proof: write the three terms with the formula. The six derivative terms cancel in pairs, for example $\partial_\mu\Gamma^\rho{}_{\nu\sigma}$ from the first term against $-\partial_\mu\Gamma^\rho{}_{\sigma\nu}$ from the third, because $\Gamma$ is symmetric in its lower indices; the six products of two $\Gamma$ cancel in pairs in the same way.
- (S4) Pair symmetry: $R_{\alpha\nu\beta\mu}=R_{\beta\mu\alpha\nu}$. Proof: write (S3) with the first index lowered four times,

$$
\begin{aligned}
&R_{\alpha\beta\mu\nu}+R_{\alpha\mu\nu\beta}+R_{\alpha\nu\beta\mu}=0, &\qquad &R_{\beta\mu\nu\alpha}+R_{\beta\nu\alpha\mu}+R_{\beta\alpha\mu\nu}=0,\\
&R_{\mu\nu\alpha\beta}+R_{\mu\alpha\beta\nu}+R_{\mu\beta\nu\alpha}=0, &\qquad &R_{\nu\alpha\beta\mu}+R_{\nu\beta\mu\alpha}+R_{\nu\mu\alpha\beta}=0 .
\end{aligned}
$$

Add the first two: by (S2) $R_{\alpha\beta\mu\nu}+R_{\beta\alpha\mu\nu}=0$, so $R_{\alpha\mu\nu\beta}+R_{\alpha\nu\beta\mu}+R_{\beta\mu\nu\alpha}+R_{\beta\nu\alpha\mu}=0$. Add the last two: $R_{\mu\nu\alpha\beta}+R_{\nu\mu\alpha\beta}=0$, so $R_{\mu\alpha\beta\nu}+R_{\mu\beta\nu\alpha}+R_{\nu\alpha\beta\mu}+R_{\nu\beta\mu\alpha}=0$. With (S1) and (S2), $R_{\mu\alpha\beta\nu}=R_{\alpha\mu\nu\beta}$, $R_{\mu\beta\nu\alpha}=-R_{\beta\mu\nu\alpha}$, $R_{\nu\alpha\beta\mu}=-R_{\alpha\nu\beta\mu}$ and $R_{\nu\beta\mu\alpha}=R_{\beta\nu\alpha\mu}$, so the second sum reads $R_{\alpha\mu\nu\beta}-R_{\beta\mu\nu\alpha}-R_{\alpha\nu\beta\mu}+R_{\beta\nu\alpha\mu}=0$. Subtracting it from the first sum leaves $2R_{\alpha\nu\beta\mu}+2R_{\beta\mu\nu\alpha}=0$, and $-R_{\beta\mu\nu\alpha}=R_{\beta\mu\alpha\nu}$ by (S1).

**Ricci tensor and scalar curvature.** The Ricci tensor and the scalar curvature are the contractions

$$
R_{\sigma\nu}:=R^\rho{}_{\sigma\rho\nu},\qquad R:=g^{\sigma\nu}R_{\sigma\nu}.
$$

The Ricci tensor is symmetric: $R_{\sigma\nu}=g^{\rho\alpha}R_{\alpha\sigma\rho\nu}=g^{\rho\alpha}R_{\rho\nu\alpha\sigma}=R^\alpha{}_{\nu\alpha\sigma}=R_{\nu\sigma}$, by (S4) in the middle step.

**Worked example: the sphere.** With $h_\theta=a$ and $h_\varphi=a\sin\theta$ the diagonal formulas give $\Gamma^\theta{}_{\varphi\varphi}=-\frac{a\sin\theta}{a^2}\,a\cos\theta=-\sin\theta\cos\theta$ and $\Gamma^\varphi{}_{\theta\varphi}=\Gamma^\varphi{}_{\varphi\theta}=\partial_\theta\ln(a\sin\theta)=\cot\theta$; all others vanish. Then

$$
\begin{aligned}
R^\theta{}_{\varphi\theta\varphi}&=\partial_\theta\Gamma^\theta{}_{\varphi\varphi}-\partial_\varphi\Gamma^\theta{}_{\theta\varphi}+\Gamma^\theta{}_{\theta\lambda}\Gamma^\lambda{}_{\varphi\varphi}-\Gamma^\theta{}_{\varphi\lambda}\Gamma^\lambda{}_{\theta\varphi}\\
&=(\sin^2\theta-\cos^2\theta)-0+0-(-\sin\theta\cos\theta)\cot\theta=\sin^2\theta ,\\
R^\varphi{}_{\theta\varphi\theta}&=\partial_\varphi\Gamma^\varphi{}_{\theta\theta}-\partial_\theta\Gamma^\varphi{}_{\varphi\theta}+\Gamma^\varphi{}_{\varphi\lambda}\Gamma^\lambda{}_{\theta\theta}-\Gamma^\varphi{}_{\theta\lambda}\Gamma^\lambda{}_{\varphi\theta}\\
&=0+\frac{1}{\sin^2\theta}+0-\cot^2\theta=1 .
\end{aligned}
$$

So $R_{\varphi\varphi}=R^\theta{}_{\varphi\theta\varphi}=\sin^2\theta$, $R_{\theta\theta}=R^\varphi{}_{\theta\varphi\theta}=1$, $R_{\theta\varphi}=0$, and

$$
R=g^{\theta\theta}R_{\theta\theta}+g^{\varphi\varphi}R_{\varphi\varphi}=\frac1{a^2}+\frac{\sin^2\theta}{a^2\sin^2\theta}=\frac{2}{a^2}>0 .
$$

A small sphere is strongly curved, a large one weakly. For the plane in polar coordinates the same computation gives $R^r{}_{\varphi r\varphi}=\partial_r(-r)-\Gamma^r{}_{\varphi\varphi}\Gamma^\varphi{}_{r\varphi}=-1-(-r)\frac1r=0$: the plane is flat, whatever coordinates we use.

**Flat spaces.** If there is a chart in which $g_{\mu\nu}$ is constant, all $\Gamma$ vanish in it, so the Riemann tensor vanishes there and hence (rule (v)) in every chart. The converse is also true: if the Riemann tensor vanishes on a region, then near each point there is a chart in which $g_{\mu\nu}=\eta_{\mu\nu}$. We quote this standard theorem without proof; the book uses it only in Section 4.13.

**Worked example: $R_{44}$ of the primordial field.** From the table of Section 4.5, no Christoffel symbol has the lower index pair $(4,4)$, so $\Gamma^\lambda{}_{44}=0$ for every $\lambda$, and $\sum_\rho\Gamma^\rho{}_{\rho4}=0$. Hence

$$
R_{44}=R^\rho{}_{4\rho4}=\partial_\rho\Gamma^\rho{}_{44}-\partial_4\Gamma^\rho{}_{\rho4}+\Gamma^\rho{}_{\rho\lambda}\Gamma^\lambda{}_{44}-\Gamma^\rho{}_{4\lambda}\Gamma^\lambda{}_{\rho4}=-\sum_{\rho,\lambda}\Gamma^\rho{}_{4\lambda}\Gamma^\lambda{}_{\rho4}.
$$

The only nonzero $\Gamma^\rho{}_{4\lambda}$ are $\Gamma^k{}_{4k}=\pm Ha_4'$ for $k\in\{1,2,3,5,6,7\}$, so the double sum is $\sum_k(\Gamma^k{}_{4k})^2=6H^2a_4'^2$ and

$$
R_{44}=-6H^2a_4'^2 ,
$$

in agreement with the Stage-2 verifier (check `P_einstein_R44`; Stage-2 document, §15.1). The same method, applied to all components, gives the scalar curvature

$$
R=6H^2\bigl(a_4'^2-7\bigr)
$$

(check `P_einstein_ricciScalar` in `wolfram-primordial-report.json`; measurement `P_einstein.ricciScalar` in `python-primordial-report.json`; it also equals the notebook's own stored output of cell 583, check `P_einstein_notebookCell583`). Section 4.15 gives a short program that reproduces it. *Numbers.* At the first exact test point of Stage 1, $H=2/3$ and $a_4'=3/7$, so $R=6\cdot\frac49\cdot\bigl(\frac{9}{49}-7\bigr)=\frac83\cdot\frac{-334}{49}=-\frac{2672}{147}$, the value recorded as `G2.p1.scalarCurvature` in `wolfram-geometry-report.json`. The Riemann tensor of the primordial field vanishes nowhere: where $a_4'\ne0$ we have $R_{44}\ne0$, and where $a_4'=0$ we have $R=-42H^2\ne0$. The primordial field is curved everywhere.

**The second Bianchi identity.** For every metric,

$$
\nabla_\lambda R^\rho{}_{\sigma\mu\nu}+\nabla_\mu R^\rho{}_{\sigma\nu\lambda}+\nabla_\nu R^\rho{}_{\sigma\lambda\mu}=0 .
$$

*Proof.* First we show that around any point $p$ there is a chart in which all $\Gamma^\rho{}_{\mu\nu}(p)=0$. Start from any chart with $x(p)=0$ and define new coordinates $x'^\rho=x^\rho+\tfrac12\Gamma^\rho{}_{\alpha\beta}(p)\,x^\alpha x^\beta$. At $p$, $\partial x'^\rho/\partial x^\alpha=\delta^\rho{}_\alpha$ (so near $p$ this is an allowed change of coordinates, by the inverse function theorem of calculus, which we quote) and $\partial^2x'^\rho/\partial x^\alpha\partial x^\beta=\Gamma^\rho{}_{\alpha\beta}(p)$, because $\Gamma$ is symmetric. The transformation rule of Section 4.5 then gives $\Gamma'^\rho{}_{\mu\nu}(p)=\Gamma^\rho{}_{\mu\nu}(p)-\Gamma^\rho{}_{\mu\nu}(p)=0$. In this chart, at $p$, a covariant derivative is a plain derivative, and the derivative of a product of two $\Gamma$ vanishes at $p$ because each term contains an undifferentiated $\Gamma(p)=0$. So at $p$

$$
\nabla_\lambda R^\rho{}_{\sigma\mu\nu}=\partial_\lambda\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\lambda\partial_\nu\Gamma^\rho{}_{\mu\sigma}.
$$

Add the three cyclic permutations of $(\lambda,\mu,\nu)$: the six terms are $\partial_\lambda\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\lambda\partial_\nu\Gamma^\rho{}_{\mu\sigma}+\partial_\mu\partial_\nu\Gamma^\rho{}_{\lambda\sigma}-\partial_\mu\partial_\lambda\Gamma^\rho{}_{\nu\sigma}+\partial_\nu\partial_\lambda\Gamma^\rho{}_{\mu\sigma}-\partial_\nu\partial_\mu\Gamma^\rho{}_{\lambda\sigma}$, and they cancel in pairs because partial derivatives commute. The left-hand side of the identity is a tensor that vanishes at $p$ in one chart, so it vanishes at $p$ in every chart (rule (v)), and $p$ was arbitrary. $\square$

### 4.8 The Einstein equations

**The contracted Bianchi identity.** First a small fact: the inverse metric is also covariantly constant. Differentiate $g^{\mu\lambda}g_{\lambda\nu}=\delta^\mu{}_\nu$ with the product rule; since $\nabla\delta=0$ and $\nabla g=0$, we get $(\nabla_\rho g^{\mu\lambda})g_{\lambda\nu}=0$, and multiplying by $g^{\nu\sigma}$ gives $\nabla_\rho g^{\mu\sigma}=0$. So $g$ and $g^{-1}$ can be moved through $\nabla$ freely. Now contract the second Bianchi identity over $\rho$ and $\mu$:

$$
\nabla_\lambda R^\rho{}_{\sigma\rho\nu}+\nabla_\rho R^\rho{}_{\sigma\nu\lambda}+\nabla_\nu R^\rho{}_{\sigma\lambda\rho}=0 .
$$

The first term is $\nabla_\lambda R_{\sigma\nu}$; by (S1) the third is $-\nabla_\nu R_{\sigma\lambda}$. Multiply by $g^{\sigma\nu}$. The first term becomes $\nabla_\lambda R$ and the third $-\nabla_\nu R^\nu{}_\lambda$. In the middle term, by (S2),

$$
g^{\sigma\nu}R^\rho{}_{\sigma\nu\lambda}=g^{\rho\alpha}g^{\sigma\nu}R_{\alpha\sigma\nu\lambda}=-g^{\rho\alpha}g^{\sigma\nu}R_{\sigma\alpha\nu\lambda}=-g^{\rho\alpha}R^\nu{}_{\alpha\nu\lambda}=-g^{\rho\alpha}R_{\alpha\lambda}=-R^\rho{}_\lambda .
$$

So $\nabla_\lambda R-2\nabla_\rho R^\rho{}_\lambda=0$. Since $\nabla_\rho(\delta^\rho{}_\lambda R)=\nabla_\lambda R$, this is

$$
\nabla_\rho G^\rho{}_\lambda=0,\qquad G_{\mu\nu}:=R_{\mu\nu}-\tfrac12\,g_{\mu\nu}R .
$$

$G_{\mu\nu}$ is the Einstein tensor. It is symmetric, it is built from the metric and its first and second derivatives, and its divergence vanishes identically, for every metric.

**Why the Einstein equations have this form.** Matter is described by its energy-momentum tensor $T_{\mu\nu}$, a symmetric tensor whose components are the densities and currents of energy and momentum; Chapter 7 derives it for the fields of this book. Conservation of energy and momentum is the statement $\nabla_\mu T^\mu{}_\nu=0$. Einstein's idea is that matter curves the geometry, with a proportionality: a tensor built from the metric equals a constant times $T$. For this to be consistent with conservation, the geometric side must have zero divergence for every metric. $G$ has this property, and so does $g$ itself (because $\nabla g=0$). The Einstein equations are

$$
G_{\mu\nu}+\Lambda\,g_{\mu\nu}=\kappa\,T_{\mu\nu},
$$

with a constant $\kappa$ and a cosmological constant $\Lambda$. In four dimensions, with $\kappa=8\pi G_{\mathrm N}/c^4$ where $G_{\mathrm N}$ is Newton's constant, these equations reproduce Newton's law of gravitation for slow bodies in weak fields (a standard result that we quote). In eight dimensions $\kappa$ is a free constant; the project's worked examples set $\kappa=1$ (Stage-2 document, §15.5, with $H=\kappa=1$ in the primordial field; the Stage-3 experiments EXP-1, with $H=\kappa=1$ and the mass of the field equal to 1, in the primordial field, and EXP-2, with $\kappa=1$, written $\kappa_8$ there, and the mass equal to 1; `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md`, §3.1). The project writes the equations without $\Lambda$ and in the mixed form

$$
G^\mu{}_\nu=\kappa\,T^\mu{}_\nu
$$

(Stage-2 document, §15.2). For an observer moving along $x^4$ in a Gaussian normal chart, the energy density is $\rho=T_{44}$ (Chapter 7), and because $g^{44}=-1$ the mixed component is $T^4{}_4=g^{44}T_{44}=-\rho$. The transverse pressures are $p_{(\mu)}=T^\mu{}_\mu$ (no sum, $\mu\ne4$).

**The trace-reversed form.** Take the trace of $G_{\mu\nu}=\kappa T_{\mu\nu}$ with $g^{\mu\nu}$. Since $g^{\mu\nu}g_{\mu\nu}=\delta^\mu{}_\mu=n$, we get $R-\tfrac n2R=\kappa T$ with $T:=T^\mu{}_\mu$, so $R=-2\kappa T/(n-2)$. Inserting this back,

$$
R_{\mu\nu}=\kappa\Bigl(T_{\mu\nu}-\frac{1}{n-2}\,T\,g_{\mu\nu}\Bigr)\qquad\bigl(\text{for }n=8:\ R_{\mu\nu}=\kappa\bigl(T_{\mu\nu}-\tfrac16Tg_{\mu\nu}\bigr)\bigr).
$$

The factor $\tfrac16=\tfrac1{n-2}$ is the one that appears in the evolution equations of the Stage-3 experiment EXP-2. Without matter ($T_{\mu\nu}=0$) the equations say $R_{\mu\nu}=0$: a vacuum solution has vanishing Ricci tensor.

**Worked example: what the primordial field would need as a source.** The primordial field is a prescribed metric, not a solution of the vacuum equations: $R_{44}=-6H^2a_4'^2$ is not zero unless $a_4$ is constant, and we will see that $G^4{}_4$ is never zero. Its mixed Einstein tensor is diagonal, with (Stage-2 document, §15.1; checks `P_einstein_GmixedClosedForms` and `P_einstein_offDiagonalZero` in `wolfram-primordial-report.json`, measurement `P_einstein.einsteinMixedDiagonal` in `python-primordial-report.json`)

$$
\begin{aligned}
G^0{}_0&=-3H^2\bigl(a_4'^2-5\bigr), &\qquad G^i{}_i&=H^2\bigl(15-3a_4'^2+a_4''\bigr)\quad(i=1,2,3),\\
G^4{}_4&=3H^2\bigl(7+a_4'^2\bigr), &\qquad G^j{}_j&=H^2\bigl(15-3a_4'^2-a_4''\bigr)\quad(j=5,6,7).
\end{aligned}
$$

The component $G^4{}_4$ follows from our two results: $G^4{}_4=g^{44}R_{44}-\tfrac12R=6H^2a_4'^2-3H^2(a_4'^2-7)=3H^2(7+a_4'^2)$. The Python verifier also checks the contracted Bianchi identity $\nabla_\mu G^\mu{}_\nu=0$ for all eight values of $\nu$ (measurement `P_einstein.contractedBianchi`). If the field obeyed the 8-dimensional Einstein equations, its source would need the energy density

$$
\rho_{\mathrm{req}}=-T^4{}_4=-\frac{G^4{}_4}{\kappa}=-\frac{3H^2\bigl(7+a_4'^2\bigr)}{\kappa}\le-\frac{21H^2}{\kappa}<0
$$

for every $a_4$. This negative energy density is the Stage-2 result checked as `P_einstein_rhoRequiredNegative`.

For the notebook's choice $a_4=t$ ($a_4'=1$, $a_4''=0$) the formulas give $R=-36H^2$, $G^\mu{}_\nu=\mathrm{diag}(12,12,12,12,24,12,12,12)\,H^2$, $\rho_{\mathrm{req}}=-24H^2/\kappa$ and the equal pressures $p=12H^2/\kappa$ in all seven transverse directions, so $w=p/\rho=-\tfrac12$ (`python-primordial-report.json`, measurement `P_a4linear`, row "a4 = t"). A cosmological constant cannot supply this: $\Lambda$ contributes equally to all diagonal components, but $G^0{}_0=G^4{}_4$ would require $-3H^2(a_4'^2-5)=3H^2(7+a_4'^2)$, that is $a_4'^2=-1$, which no real $a_4$ satisfies. Chapter 9 discusses which states of dirac16complex can supply such a source.

### 4.9 The Einstein-Lovelock equations

**The question.** Is $G_{\mu\nu}$ the only possible left-hand side? Lovelock answered this in 1971 (D. Lovelock, J. Math. Phys. 12, 498 (1971)). The notebook's title and its cell 14 refer to his result, in the form of equation (4.38) of the book by Lovelock and Rund, *Tensors, Differential Forms, and Variational Principles* (`handoff/surveys/survey_notebook-physics.md`, item 1). We define the objects and prove what can be proved at this level; the rest is quoted.

**Generalized Kronecker delta.** For $2p$ indices,

$$
\delta^{\mu_1\cdots\mu_p}{}_{\nu_1\cdots\nu_p}:=\det\begin{pmatrix}\delta^{\mu_1}{}_{\nu_1}&\cdots&\delta^{\mu_1}{}_{\nu_p}\\ \vdots&&\vdots\\ \delta^{\mu_p}{}_{\nu_1}&\cdots&\delta^{\mu_p}{}_{\nu_p}\end{pmatrix}.
$$

It equals $+1$ if the upper indices are distinct and are an even rearrangement of the lower ones, $-1$ for an odd rearrangement, and 0 otherwise. Exchanging two upper indices exchanges two rows and flips the sign. Hence it vanishes whenever two upper indices are equal, and therefore it vanishes identically when $p>n$: among more than $n$ indices, each running over $n$ values, two must be equal. For $p=2$, $\delta^{\alpha\beta}{}_{\mu\nu}=\delta^\alpha{}_\mu\delta^\beta{}_\nu-\delta^\alpha{}_\nu\delta^\beta{}_\mu$.

**Lovelock scalars and tensors.** Write $R^{\alpha\beta}{}_{\mu\nu}:=g^{\beta\lambda}R^\alpha{}_{\lambda\mu\nu}$; it is antisymmetric in $\alpha,\beta$ by (S2) and in $\mu,\nu$ by (S1). For $k=0,1,2,\dots$ define

$$
\begin{aligned}
L_k&=\frac{1}{2^k}\,\delta^{\mu_1\nu_1\cdots\mu_k\nu_k}{}_{\alpha_1\beta_1\cdots\alpha_k\beta_k}\,R^{\alpha_1\beta_1}{}_{\mu_1\nu_1}\cdots R^{\alpha_k\beta_k}{}_{\mu_k\nu_k},\\
E^{(k)\mu}{}_\nu&=-\frac{1}{2^{k+1}}\,\delta^{\mu\,\mu_1\nu_1\cdots\mu_k\nu_k}{}_{\nu\,\alpha_1\beta_1\cdots\alpha_k\beta_k}\,R^{\alpha_1\beta_1}{}_{\mu_1\nu_1}\cdots R^{\alpha_k\beta_k}{}_{\mu_k\nu_k}.
\end{aligned}
$$

Normalizations differ between books; any other choice is absorbed into the coefficients below. For $k=0$: $L_0=1$ and $E^{(0)\mu}{}_\nu=-\tfrac12\delta^\mu{}_\nu$.

**Order 1 is Einstein.** For $k=1$, $L_1=\tfrac12\delta^{\mu\nu}{}_{\alpha\beta}R^{\alpha\beta}{}_{\mu\nu}=\tfrac12\bigl(R^{\mu\nu}{}_{\mu\nu}-R^{\nu\mu}{}_{\mu\nu}\bigr)=R^{\mu\nu}{}_{\mu\nu}=R$. For the tensor we need the expansion of a 3 by 3 determinant along its first row. Group the six terms of the 3 by 3 formula of Section 1.4 by their entry from row 0:

$$
\det A=A_{00}\bigl(A_{11}A_{22}-A_{12}A_{21}\bigr)-A_{01}\bigl(A_{10}A_{22}-A_{12}A_{20}\bigr)+A_{02}\bigl(A_{10}A_{21}-A_{11}A_{20}\bigr).
$$

Each bracket is the 2 by 2 determinant of the entries that remain when row 0 and the column of the entry in front are deleted. (Only this 3 by 3 case is needed, here and in Section 9.9.) For each fixed choice of the six index values the entries of $\delta^{\mu\alpha\beta}{}_{\nu\sigma\lambda}$ are numbers, 0 or 1, so the expansion applies, and with the $p=2$ formula above each bracket is a generalized delta with two upper indices:

$$
\delta^{\mu\alpha\beta}{}_{\nu\sigma\lambda}=\delta^\mu{}_\nu\,\delta^{\alpha\beta}{}_{\sigma\lambda}-\delta^\mu{}_\sigma\,\delta^{\alpha\beta}{}_{\nu\lambda}+\delta^\mu{}_\lambda\,\delta^{\alpha\beta}{}_{\nu\sigma}.
$$

Contract with $R^{\sigma\lambda}{}_{\alpha\beta}$. The first term gives $\delta^\mu{}_\nu\cdot2R$. The second gives $-\delta^{\alpha\beta}{}_{\nu\lambda}R^{\mu\lambda}{}_{\alpha\beta}=-2R^{\mu\lambda}{}_{\nu\lambda}=-2R^\mu{}_\nu$; here $R^{\mu\lambda}{}_{\nu\lambda}=g^{\mu\alpha}g^{\lambda\beta}R_{\alpha\beta\nu\lambda}=g^{\mu\alpha}g^{\lambda\beta}R_{\beta\alpha\lambda\nu}=g^{\mu\alpha}R_{\alpha\nu}$ by (S1) and (S2). The third gives $\delta^{\alpha\beta}{}_{\nu\sigma}R^{\sigma\mu}{}_{\alpha\beta}=2R^{\sigma\mu}{}_{\nu\sigma}=-2R^{\mu\sigma}{}_{\nu\sigma}=-2R^\mu{}_\nu$. So

$$
E^{(1)\mu}{}_\nu=-\tfrac14\bigl(2R\,\delta^\mu{}_\nu-4R^\mu{}_\nu\bigr)=R^\mu{}_\nu-\tfrac12R\,\delta^\mu{}_\nu=G^\mu{}_\nu .
$$

**Lovelock's theorem (quoted, not proved here).** Each $E^{(k)}$ is symmetric (with both indices lowered) and has identically vanishing divergence, and, up to a constant factor, it is what one obtains from $\int\sqrt{\lvert g\rvert}\,L_k\,d^nx$ by varying the metric. Conversely, every symmetric tensor with identically vanishing divergence that is built from the metric and its first and second derivatives is a combination of the $E^{(k)}$. The Einstein-Lovelock field equations are therefore

$$
\sum_{k\ge0}\alpha_k\,E^{(k)\mu}{}_\nu=\kappa\,T^\mu{}_\nu ,
$$

with constants $\alpha_k$; the choice $\alpha_0=-2\Lambda$, $\alpha_1=1$ and all others zero gives back $G^\mu{}_\nu+\Lambda\delta^\mu{}_\nu=\kappa T^\mu{}_\nu$. For $k=1$ we have proved the divergence property ourselves (the contracted Bianchi identity).

**Which orders can exist (the vanishing is proved).** $E^{(k)}$ contains the generalized delta with $p=2k+1$ upper indices, so it vanishes identically when $2k+1>n$. In $n=4$ only $k=0$ and $k=1$ can contribute, so by Lovelock's theorem (quoted) Einstein's equations with a cosmological constant are the only choice in four dimensions. In $n=8$ only $k=0,1,2,3$ can contribute; $E^{(0)\mu}{}_\nu=-\tfrac12\delta^\mu{}_\nu$ and $E^{(1)}=G$ are visibly nonzero (Section 4.8 gives a metric with $G^4{}_4\ne0$), and that $E^{(2)}$ and $E^{(3)}$ do not vanish identically is quoted. The order-2 scalar is the Gauss-Bonnet combination $L_2=R^2-4R_{\mu\nu}R^{\mu\nu}+R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ (a standard expansion of the definition that we quote; this book does not use it). Each order has a different power of length: $R$ has the dimension $1/\text{length}^2$, so $L_k$ has $1/\text{length}^{2k}$.

**The notebook and the project.** The notebook's cell 14 states "m-1 = 8/2 - 1 = 3", keeps the orders 1, 2 and 3, and writes the vacuum equations as $0=-\Lambda+H^{-2}w_1\,\mathrm{Lovelock1}+H^{-4}w_2\,\mathrm{Lovelock2}+H^{-6}w_3\,\mathrm{Lovelock3}$ with pure numbers $w_1,w_2,w_3,\Lambda$. The inverse length $H$ is introduced exactly to make the orders, which have different dimensions, comparable (`survey_notebook-physics.md`, item 1). This agrees with the counting above: orders higher than 3 vanish identically in eight dimensions. But no code of the notebook defines Lovelock2 or Lovelock3, and its curvature code stops at the Einstein tensor (cells 583 and 584, which the Stage-2 verifier reproduces exactly: checks `P_einstein_notebookCell583` and `P_einstein_notebookCell584`). The project does not compute the orders 2 and 3 either (Stage-2 document, §1, non-claim 4). Every gravitational statement in this book therefore uses the 8-dimensional Einstein equations only. Whether the Lovelock terms change the picture is an open problem (Chapter 18).

### 4.10 The vielbein

**Why a spinor needs more than a metric.** Chapter 2 built spinors from gamma matrices with the constant relation $\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}$. In a curved space the metric $g_{\mu\nu}(x)$ changes from point to point and is not $\eta$. The way out is to describe every point with its own set of $n$ reference directions that are perpendicular to each other and of unit length. In such a frame the metric looks like $\eta$, and the constant gamma matrices of Chapter 2 can be used unchanged. The spinor components are always measured with respect to such a frame.

**Definition (vielbein).** At every point choose $n$ vectors $E_0,\dots,E_{n-1}$ with

$$
g(E_a,E_b)=\eta_{ab}\qquad(a,b=0,\dots,n-1).
$$

Their components are written $E_a{}^\mu=:e_a{}^\mu$, the inverse vielbein. The matrix $(e_a{}^\mu)$ is invertible (orthonormal vectors are linearly independent), and its inverse is the vielbein $e_\mu{}^a$ ("viel Beine", German for "many legs"; in four dimensions it is called a vierbein or tetrad, and the notebook calls its eight-legged version an octad, cell 281). As in the project we write $e_\mu{}^a$ with row index $\mu$ and column index $a$ (Stage 1, §5.1). By definition of the inverse,

$$
e_\mu{}^a\,e_a{}^\nu=\delta_\mu{}^\nu,\qquad e_a{}^\mu\,e_\mu{}^b=\delta_a{}^b .
$$

**The metric from the vielbein.** The orthonormality condition reads $g_{\mu\nu}e_a{}^\mu e_b{}^\nu=\eta_{ab}$. Multiply by $e_\rho{}^a e_\sigma{}^b$ and sum over $a$ and $b$; with $e_a{}^\mu e_\rho{}^a=\delta^\mu{}_\rho$ this gives

$$
g_{\rho\sigma}=e_\rho{}^a\,\eta_{ab}\,e_\sigma{}^b,\qquad g^{\mu\nu}=e_a{}^\mu\,\eta^{ab}\,e_b{}^\nu .
$$

For the second formula, multiply the candidate $e_c{}^\nu\eta^{cd}e_d{}^\rho$ by $g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b$: using $e_\nu{}^be_c{}^\nu=\delta^b{}_c$ and $\eta_{ab}\eta^{bd}=\delta_a{}^d$ the product is $e_\mu{}^de_d{}^\rho=\delta_\mu{}^\rho$. In matrix language $g=e\,\eta\,e^T$, so $\det g=(\det e)^2\det\eta$. For signature (4,4), $\det\eta=(-1)^4=+1$, hence $\det g=(\det e)^2>0$ and $\sqrt{\lvert g\rvert}=\lvert\det e\rvert$. This is why the primordial field has $\det g=+\cos^2z$.

**Frame components.** A vector $V$ has frame components $V^a:=e_\mu{}^aV^\mu$, and $V^\mu=e_a{}^\mu V^a$. Then $g(V,W)=g_{\mu\nu}e_a{}^\mu e_b{}^\nu V^aW^b=\eta_{ab}V^aW^b$: in frame components, lengths are computed with $\eta$. Frame indices are raised and lowered with $\eta$: $V_a=\eta_{ab}V^b$. Frame components do not change when the coordinates change, because $e_\mu{}^a$ is a covector for each fixed $a$; they change when the frame is turned.

**Existence and freedom.** Near every point of a manifold with a metric such frames exist (orthonormalize any basis step by step; we quote this standard fact, and for all metrics of the book we write the frame down explicitly). They are not unique. If $\Lambda(x)$ is, at each point, a matrix with $\Lambda^T\eta\Lambda=\eta$ (an element of the group O(4,4) of Chapter 2), then $e'_\mu{}^a=\Lambda^a{}_b\,e_\mu{}^b$ is another vielbein for the same metric:

$$
e'_\mu{}^a\eta_{ab}e'_\nu{}^b=e_\mu{}^c\bigl(\Lambda^a{}_c\,\eta_{ab}\,\Lambda^b{}_d\bigr)e_\nu{}^d=e_\mu{}^c\,(\Lambda^T\eta\Lambda)_{cd}\,e_\nu{}^d=e_\mu{}^c\eta_{cd}e_\nu{}^d=g_{\mu\nu}.
$$

Such a point-dependent turning of the frame is a local frame rotation (local Lorentz transformation). Physics must not depend on the choice of frame; for spinors this requirement is local spin invariance (Section 4.12).

**Two letters with two meanings.** From here on $\Lambda$, written $\Lambda(x)$ or with frame indices $\Lambda^a{}_b$, is a frame rotation. It is not the cosmological constant $\Lambda$ of Sections 4.8 and 4.9, which does not appear again in this chapter. Likewise, from Section 4.12 on, $R$ or $R(x)$ without indices, a 16 by 16 matrix that acts on spinors, is a spin transformation, as in Chapter 2. $R$ with indices is the Riemann tensor or the Ricci tensor, and $R$ alone in a curvature formula, such as the Lichnerowicz formula of Section 4.13, is the scalar curvature. In the one theorem where both meanings of $R$ would meet, the theorem of Section 4.13 that the spin connection cannot be removed in a curved field, the spin transformation is called $U(x)$ instead.

**Curved gamma matrices.** With the frame gammas $\gamma^a$ of Chapter 2 define

$$
\gamma^\mu:=e_a{}^\mu\gamma^a,\qquad \gamma_\mu:=g_{\mu\nu}\gamma^\nu=e_\mu{}^a\eta_{ab}\gamma^b .
$$

They obey the curved Clifford relation: $\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=e_a{}^\mu e_b{}^\nu(\gamma^a\gamma^b+\gamma^b\gamma^a)=2e_a{}^\mu\eta^{ab}e_b{}^\nu=2g^{\mu\nu}$. As in the Stage documents, a gamma matrix with a numeric upper index, $\gamma^0,\dots,\gamma^7$, is always the constant frame matrix; a curved gamma with a numeric label is written $\gamma^{x_0},\dots,\gamma^{x_7}$.

**Worked example: the polar plane.** The unit radial vector $E_0$ has polar components $(1,0)$ and the unit angular vector $E_1$ has $(0,1/r)$, because $g(E_1,E_1)=r^2(1/r)^2=1$. So $e_a{}^\mu=\mathrm{diag}(1,1/r)$ and $e_\mu{}^a=\mathrm{diag}(1,r)$, with frame indices $a=0$ (radial) and $a=1$ (angular). The plane is Euclidean, $\eta=\mathrm{diag}(1,1)$, and a two-dimensional Clifford algebra is given by $\gamma^0=\sigma_1$, $\gamma^1=\sigma_2$. The curved gammas are $\gamma^r=\sigma_1$ and $\gamma^\varphi=\sigma_2/r$; for example $\gamma^\varphi\gamma^\varphi+\gamma^\varphi\gamma^\varphi=2\sigma_2^2/r^2=2/r^2=2g^{\varphi\varphi}$.

**Worked example: the primordial field.** A diagonal metric $g_{\mu\mu}=\eta_{\mu\mu}h_\mu^2$ has the diagonal vielbein $e_\mu{}^a=h_\mu\,\delta_\mu{}^a$ (no sum), since then $e\,\eta\,e^T=\mathrm{diag}(\eta_{\mu\mu}h_\mu^2)$. For the primordial field (Stage-2 document, §4.2; check `P_metric_vielbeinProduct`)

$$
e_\mu{}^a=\mathrm{diag}\bigl(\cot z,\ s^{1/6}e^{a_4}\ (\times3),\ 1,\ s^{1/6}e^{-a_4}\ (\times3)\bigr),
$$

and the curved gammas are

$$
\begin{aligned}
&\gamma^{x_0}=\tan z\,\gamma^0,\qquad \gamma^{x_i}=s^{-1/6}e^{-a_4}\gamma^i\ \ (i=1,2,3),\\
&\gamma^{x_4}=\gamma^4,\qquad \gamma^{x_j}=s^{-1/6}e^{a_4}\gamma^j\ \ (j=5,6,7).
\end{aligned}
$$

In the notebook these are the matrices `(T16^α)` of cell 475, built from its diagonal octad (cells 279, 283 and 302).

### 4.11 The spin connection and the vielbein postulate

**The problem.** We want to differentiate the frame components $V^a=e_\mu{}^aV^\mu$ of a vector field. The frame turns from point to point, so $\partial_\mu V^a$ mixes the change of $V$ with the turning of the frame, just as $\partial_\mu V^\nu$ mixed the change of $V$ with the turning of the coordinate lines. The cure is the same: a correction, linear in $V$,

$$
\nabla_\mu V^a:=\partial_\mu V^a+\omega_\mu{}^a{}_b\,V^b ,
$$

with coefficients $\omega_\mu{}^a{}_b(x)$, the spin connection. We fix them by one natural requirement: the frame components of the covariant derivative must be the covariant derivative of the frame components,

$$
e_\nu{}^a\,\nabla_\mu V^\nu=\nabla_\mu V^a\qquad\text{for every vector field }V .
$$

**Derivation of the vielbein postulate.** Write out both sides. The left is $e_\nu{}^a(\partial_\mu V^\nu+\Gamma^\nu{}_{\mu\lambda}V^\lambda)$. The right is $\partial_\mu(e_\lambda{}^aV^\lambda)+\omega_\mu{}^a{}_be_\lambda{}^bV^\lambda=(\partial_\mu e_\lambda{}^a)V^\lambda+e_\lambda{}^a\partial_\mu V^\lambda+\omega_\mu{}^a{}_be_\lambda{}^bV^\lambda$. The terms with $\partial_\mu V$ agree, and what remains is

$$
\bigl(\partial_\mu e_\lambda{}^a-\Gamma^\nu{}_{\mu\lambda}e_\nu{}^a+\omega_\mu{}^a{}_b\,e_\lambda{}^b\bigr)V^\lambda=0 .
$$

Since this holds for every $V$, the bracket vanishes. Renaming the indices, this is the vielbein postulate (Stage 1, §5.2):

$$
\nabla_\mu e_\nu{}^a:=\partial_\mu e_\nu{}^a-\Gamma^\rho{}_{\mu\nu}\,e_\rho{}^a+\omega_\mu{}^a{}_b\,e_\nu{}^b=0 .
$$

In words: the total covariant derivative of the vielbein, with the Christoffel symbols acting on its curved index and the spin connection acting on its frame index, vanishes.

**Theorem (the canonical spin connection).** The vielbein postulate has exactly one solution,

$$
\omega_\mu{}^a{}_b=e_b{}^\nu\bigl(\Gamma^\rho{}_{\mu\nu}\,e_\rho{}^a-\partial_\mu e_\nu{}^a\bigr),
$$

and the lowered connection $\omega_{\mu ab}:=\eta_{ac}\,\omega_\mu{}^c{}_b$ is antisymmetric: $\omega_{\mu ab}=-\omega_{\mu ba}$.

*Proof of the formula.* Multiply the postulate by $e_b{}^\nu$ and sum over $\nu$. The last term becomes $\omega_\mu{}^a{}_c\,e_\nu{}^ce_b{}^\nu=\omega_\mu{}^a{}_c\,\delta^c{}_b=\omega_\mu{}^a{}_b$, and solving for it gives the formula. Conversely, inserting the formula back into the postulate and using $e_\nu{}^be_b{}^\sigma=\delta_\nu{}^\sigma$ makes it an identity, so the formula is a solution, and the derivation shows it is the only one.

*Proof of the antisymmetry.* With $e_{\rho a}:=\eta_{ac}e_\rho{}^c=g_{\rho\sigma}e_a{}^\sigma$ (the second form follows from $g_{\rho\sigma}=e_\rho{}^c\eta_{cd}e_\sigma{}^d$) and $\Gamma_{\sigma\mu\nu}=g_{\sigma\rho}\Gamma^\rho{}_{\mu\nu}$,

$$
\omega_{\mu ab}=e_a{}^\sigma e_b{}^\nu\,\Gamma_{\sigma\mu\nu}-\eta_{ac}\,e_b{}^\nu\,\partial_\mu e_\nu{}^c .
$$

Add the same expression with $a$ and $b$ exchanged. In the first terms, $\Gamma_{\sigma\mu\nu}+\Gamma_{\nu\mu\sigma}=\partial_\mu g_{\nu\sigma}$, as one sees by adding the two Christoffel formulas; so they give $e_a{}^\sigma e_b{}^\nu\,\partial_\mu g_{\sigma\nu}$. Differentiating $g_{\sigma\nu}=e_\sigma{}^c\eta_{cd}e_\nu{}^d$ with the product rule,

$$
e_a{}^\sigma e_b{}^\nu\,\partial_\mu g_{\sigma\nu}=\eta_{cb}\,e_a{}^\sigma\partial_\mu e_\sigma{}^c+\eta_{ad}\,e_b{}^\nu\partial_\mu e_\nu{}^d ,
$$

which is exactly the sum of the two second terms with the opposite sign. Hence $\omega_{\mu ab}+\omega_{\mu ba}=0$. $\square$

For each $\mu$ the antisymmetric $\omega_{\mu ab}$ has $n(n-1)/2$ independent components, 28 for $n=8$: one for each of the 28 generators $S^{ab}$ ($a<b$) of Chapter 2. So for each $\mu$ the matrix $A=(\omega_\mu{}^a{}_b)$ satisfies $A^T\eta=-\eta A$, because $\eta A=(\omega_{\mu ab})$ is antisymmetric and $\eta$ is symmetric. This is the condition for $1+\epsilon A$ to lie in O(4,4) to first order in a small number $\epsilon$: $(1+\epsilon A)^T\eta(1+\epsilon A)=\eta+\epsilon(A^T\eta+\eta A)+\epsilon^2A^T\eta A=\eta+O(\epsilon^2)$. So $\omega_\mu$ is an infinitesimal frame rotation (the set of such matrices is called so(4,4)).

**The inverse vielbein postulate.** Differentiate $e_a{}^\nu e_\nu{}^b=\delta_a{}^b$ and replace $\partial_\mu e_\nu{}^b$ by $\Gamma^\rho{}_{\mu\nu}e_\rho{}^b-\omega_\mu{}^b{}_ce_\nu{}^c$ from the postulate: $(\partial_\mu e_a{}^\nu)e_\nu{}^b+e_a{}^\nu\Gamma^\rho{}_{\mu\nu}e_\rho{}^b-\omega_\mu{}^b{}_a=0$. Multiplying by $e_b{}^\sigma$ gives

$$
\partial_\mu e_a{}^\sigma+\Gamma^\sigma{}_{\mu\nu}\,e_a{}^\nu-\omega_\mu{}^b{}_a\,e_b{}^\sigma=0 .
$$

**Behaviour under a frame rotation.** Write the postulate as a statement about the column $e_\nu=(e_\nu{}^a)_a$ and the matrices $\omega_\mu=(\omega_\mu{}^a{}_b)$: $\partial_\mu e_\nu-\Gamma^\rho{}_{\mu\nu}e_\rho+\omega_\mu e_\nu=0$. For the rotated frame $e'_\nu=\Lambda e_\nu$ (same metric, so the same $\Gamma$),

$$
\partial_\mu(\Lambda e_\nu)-\Gamma^\rho{}_{\mu\nu}\Lambda e_\rho+\omega'_\mu\Lambda e_\nu=(\partial_\mu\Lambda)e_\nu-\Lambda\omega_\mu e_\nu+\omega'_\mu\Lambda e_\nu .
$$

This vanishes for all $\nu$, and the columns $e_\nu$ span all columns, so

$$
\omega'_\mu=\Lambda\,\omega_\mu\,\Lambda^{-1}-(\partial_\mu\Lambda)\,\Lambda^{-1}.
$$

The second term shows that $\omega$ is not a tensor in its frame indices: it contains the rate at which the frame is turned.

**Worked example: the polar plane.** With $e_\mu{}^a=\mathrm{diag}(1,r)$, $e_a{}^\mu=\mathrm{diag}(1,1/r)$ and the Christoffel symbols of Section 4.5, the formula gives, for $\mu=\varphi$,

$$
\omega_\varphi{}^0{}_1=e_1{}^\varphi\bigl(\Gamma^r{}_{\varphi\varphi}e_r{}^0-\partial_\varphi e_\varphi{}^0\bigr)=\frac1r(-r)(1)=-1,\qquad
\omega_\varphi{}^1{}_0=e_0{}^r\bigl(\Gamma^\varphi{}_{\varphi r}e_\varphi{}^1-\partial_\varphi e_r{}^1\bigr)=1\cdot\frac1r\cdot r=1,
$$

and $\omega_\varphi{}^0{}_0=\omega_\varphi{}^1{}_1=0$. For $\mu=r$: $\omega_r{}^1{}_1=e_1{}^\varphi(\Gamma^\varphi{}_{r\varphi}e_\varphi{}^1-\partial_re_\varphi{}^1)=\frac1r(\frac1r\cdot r-1)=0$, and the other three vanish as well. Since $\eta=1$ here, $\omega_{\varphi01}=-1=-\omega_{\varphi10}$: antisymmetric, as the theorem says. The meaning is simple. The radial and angular unit vectors at the angle $\varphi$ are the Cartesian unit vectors turned by the angle $\varphi$; moving in $\varphi$ turns the frame at the rate $d\varphi/d\varphi=1$, and the spin connection records this rate.

**Diagonal vielbeins.** For $e_\mu{}^a=h_\mu\delta_\mu{}^a$ (no sum) the formula gives $\omega_\mu{}^a{}_b=\frac{1}{h_b}\bigl(\Gamma^a{}_{\mu b}h_a-\partial_\mu(h_b\delta_b{}^a)\bigr)$. For $a=b$ this is $\Gamma^a{}_{\mu a}-\partial_\mu\ln h_a=0$ by cases (a) and (b) of Section 4.5. For $a\ne b$ it is $\frac{h_a}{h_b}\Gamma^a{}_{\mu b}$, which by cases (b), (c) and (d) is nonzero only for $\mu=a$ or $\mu=b$. Lowering with $\eta$:

$$
\omega_{\mu\mu b}=\eta_{\mu\mu}\,\frac{\partial_bh_\mu}{h_b},\qquad \omega_{\mu b\mu}=-\omega_{\mu\mu b}\qquad(b\ne\mu,\ \text{no sum}),
$$

and all other components vanish. (For $\mu=a$: $\omega_a{}^a{}_b=\frac{h_a}{h_b}\partial_b\ln h_a$. For $\mu=b$: $\omega_b{}^a{}_b=\frac{h_a}{h_b}\bigl(-\eta_{aa}\eta_{bb}\frac{h_b}{h_a^2}\partial_ah_b\bigr)=-\eta_{aa}\eta_{bb}\frac{\partial_ah_b}{h_a}$, and $\eta_{aa}$ times this is $-\eta_{bb}\partial_ah_b/h_a$, the antisymmetric partner.) Here $\partial_b$ is the derivative with respect to the coordinate whose number equals the frame index $b$.

**Worked example: the 24 components of the primordial field.** Write $\alpha_i=H\,s^{1/6}e^{a_4}$ for $i=1,2,3$ and $\alpha_j=H\,s^{1/6}e^{-a_4}$ for $j=5,6,7$. The scale factors $h_k$ ($k\ne0,4$) depend on $x^0$ and $x^4$, with $\partial_0h_k=H\cot z\,h_k$, $\partial_4h_i=Ha_4'h_i$ and $\partial_4h_j=-Ha_4'h_j$; $h_0$ depends on $x^0$ only and $h_4=1$. So the nonzero components have $\mu=k\in\{1,2,3,5,6,7\}$ and $b\in\{0,4\}$:

| Component | Formula | Value |
| --- | --- | --- |
| $\omega_{i\,i0}=-\omega_{i\,0i}$ | $\eta_{ii}\,\partial_0h_i/h_0$ | $H\cot z\,h_i\tan z=\alpha_i$ |
| $\omega_{i\,i4}=-\omega_{i\,4i}$ | $\eta_{ii}\,\partial_4h_i/h_4$ | $Ha_4'h_i=\alpha_ia_4'$ |
| $\omega_{j\,j0}=-\omega_{j\,0j}$ | $\eta_{jj}\,\partial_0h_j/h_0$ | $-H\cot z\,h_j\tan z=-\alpha_j$ |
| $\omega_{j\,j4}=-\omega_{j\,4j}$ | $\eta_{jj}\,\partial_4h_j/h_4$ | $-(-Ha_4'h_j)=\alpha_ja_4'$ |

That is $6\times2\times2=24$ nonzero components, and $\omega_{0ab}=\omega_{4ab}=0$. In the notation of the Stage-2 document (§6): $\omega_{i\,0i}=-H s^{1/6}e^{a_4}$, $\omega_{i\,i4}=Hs^{1/6}e^{a_4}a_4'$, $\omega_{j\,0j}=Hs^{1/6}e^{-a_4}$, $\omega_{j\,j4}=Hs^{1/6}e^{-a_4}a_4'$. The Stage-2 verifiers find the same: the vielbein postulate holds in all 512 components, exactly 24 components are nonzero, with these closed forms (checks `P_spinconn_vielbeinPostulate512`, `P_spinconn_count24`, `P_spinconn_antisymmetry` and `P_spinconn_closedForms` in `wolfram-primordial-report.json`; `nonzeroCount` = 24 and check `P_spinconn` in `python-primordial-report.json`).

**The mixed components and the space-time pairs.** Since $\omega_{\mu ab}=\eta_{aa}\omega_\mu{}^a{}_b$ (no sum, $\eta_{aa}=\pm1$),

$$
\omega_\mu{}^b{}_a=\eta_{bb}\,\omega_{\mu ba}=-\eta_{bb}\,\omega_{\mu ab}=-\eta_{aa}\eta_{bb}\,\omega_\mu{}^a{}_b\qquad(\text{no sum}).
$$

For a pair of two space-like or two time-like frame directions, $\eta_{aa}\eta_{bb}=+1$ and the mixed components are antisymmetric in $(a,b)$, like the lowered ones. For a space-time pair, one space-like and one time-like direction (a boost pair), $\eta_{aa}\eta_{bb}=-1$ and the mixed components are symmetric: $\omega_\mu{}^b{}_a=+\omega_\mu{}^a{}_b$. In the primordial field the 12 components of the pairs $(i,4)$ for $\mu=i$ and $(0,j)$ for $\mu=j$ are of this kind; for example $\omega_1{}^1{}_4=\omega_1{}^4{}_1=Hs^{1/6}e^{a_4}a_4'$ (Stage-2 document, §6; measurement `G2.p1.nonzeroOmegaMixedSymmetricPart` = 12 in `wolfram-geometry-report.json`). The notebook's own stored mixed connection (the output of its cell 501) equals the correct $\omega_\mu{}^a{}_b$ entry by entry (check `P_spinconn_notebookCell501OmegaMuIJEqualsMixedOmega`): the notebook computes $\omega$ correctly. Its error, which Section 4.14 explains, is in how it contracts $\omega$ with $S^{ab}$.

**An arbitrary gravitational field.** The general statements of this section are proved above for every vielbein. Stage 1 also tested them with exact rational arithmetic in a generic non-diagonal vielbein, the test geometry G1, $e_\mu{}^a=\delta_\mu{}^a+P_\mu{}^a(x)$ with polynomial entries $P$, at three rational points (Stage 1, §5.7). There all 512 components of the vielbein postulate vanish together with their 4096 first derivatives, $\omega_{\mu ab}=-\omega_{\mu ba}$, and 448 of the 512 components $\omega_{\mu ab}$ are nonzero at each point; in the primordial field G2 the count is 24 (Stage 1, Result 5.1; checks `GEO_vielbeinPostulate_G1`, `GEO_vielbeinPostulate_G2`, `GEO_omegaAntisymmetry_G1` and `GEO_omegaAntisymmetry_G2` in `wolfram-geometry-report.json` and `python-geometry-report.json`). The Python checker computes $\omega$ in two independent ways, from the Christoffel symbols as above and from the derivatives of the vielbein alone (the anholonomy route), and the two agree.

### 4.12 The covariant derivative of a spinor

**How a pair of spinors gives a vector.** A spinor field $\Psi(x)$ has 16 components measured in the local frame. When the frame is turned by a local rotation, the components change by a spin transformation $R(x)$ (Chapter 2): $\Psi\to R\Psi$. Before we can say how such a field is differentiated, we need to know how the simplest vectors built from two spinors change under $R$. Let $R$ be an element of $\mathrm{Spin}_0(4,4)$, the part of $\mathrm{Spin}(4,4)$ connected to 1, that is, a product of exponentials $\exp(\theta S^{ab})$ (Section 2.14). Such an $R$ can be reached continuously from no rotation at all: replace every $\theta$ in the product by $t\theta$ and let $t$ run from 0 to 1. Three facts of Chapter 2 are needed.

*(i) $R$ covers a frame rotation.* Theorem 2.9 (Section 2.14) states $g\,\gamma(v)\,g^{-1}=\gamma(\Lambda_{\mathrm u}(g)v)$ for every $g$ in Pin(4,4), with $\gamma(v)=\sum_av_a\gamma^a$. For $g=R^{-1}$ and $v$ the $a$-th unit vector it says $R^{-1}\gamma^aR=\sum_b\Lambda_{\mathrm u}(R^{-1})_{ba}\gamma^b$. So, with $\Lambda^a{}_b:=\Lambda_{\mathrm u}(R^{-1})_{ba}$,

$$
R^{-1}\gamma^aR=\Lambda^a{}_b\,\gamma^b .
$$

We say that $R$ covers $\Lambda$; this is the convention of the whole section. The matrix $\Lambda=(\Lambda^a{}_b)$ lies in O(4,4). Indeed $\Lambda_{\mathrm u}$ is a homomorphism, so $\Lambda_{\mathrm u}(R^{-1})=\Lambda_{\mathrm u}(R)^{-1}$, and every $M$ in O(4,4) has $M^{-1}=\eta M^T\eta$ (multiply $M^T\eta M=\eta$ by $\eta$ on the left and use $\eta^2=1$). Hence $\Lambda^a{}_b=(\eta\,\Lambda_{\mathrm u}(R)\,\eta)_{ab}$, a product of three elements of O(4,4), because $\eta$ itself lies in O(4,4) ($\eta^T\eta\eta=\eta$). Fact (i) holds for every element of Pin(4,4), not only for those of $\mathrm{Spin}_0(4,4)$.

*(ii) $R$ is real.* Each factor $\exp(\theta S^{ab})$ is $\cos\tfrac\theta2+\gamma^a\gamma^b\sin\tfrac\theta2$ or $\cosh\tfrac\theta2+\gamma^a\gamma^b\sinh\tfrac\theta2$ (Section 2.11, for $a\ne b$; for $a=b$ it is 1), and the gammas are real. So $(R\Psi)^\dagger=\Psi^\dagger R^T$.

*(iii) $R^TCR=C$.* Section 2.11 proves it for one exponential. For a product it follows factor by factor: if $R_1^TCR_1=C$ and $R_2^TCR_2=C$, then $(R_1R_2)^TC(R_1R_2)=R_2^T(R_1^TCR_1)R_2=R_2^TCR_2=C$. (Equivalently, it is Theorem 2.8 with an even number $k$ of factors and the spinor norm $N(R)=+1$.) Multiplying by $R^{-1}$ on the right gives $R^TC=CR^{-1}$.

For two spinor fields $\Psi$ and $\Phi$ (here ordinary columns of complex functions) and the Dirac adjoint $\bar\Psi=\Psi^\dagger C$ (Section 2.9), the 8 bilinears $v^a:=\bar\Psi\gamma^a\Phi$ therefore change as

$$
(R\Psi)^\dagger C\gamma^a(R\Phi)=\Psi^\dagger R^TC\gamma^aR\,\Phi=\Psi^\dagger CR^{-1}\gamma^aR\,\Phi=\Lambda^a{}_b\,\bar\Psi\gamma^b\Phi ,
$$

by (ii), (iii) and (i) in turn. This is exactly how the frame components of a vector change, $V^a\to\Lambda^a{}_bV^b$, when the frame is rotated, $e'_\mu{}^a=\Lambda^a{}_be_\mu{}^b$ (Section 4.10). Here the restriction to $\mathrm{Spin}_0(4,4)$ is needed: an element $R$ of $\mathrm{Spin}(4,4)$ with spinor norm $N(R)=-1$, such as $R=\gamma^0\gamma^4$, has $R^TCR=-C$ by Theorem 2.8, and then $v^a\to-\Lambda^a{}_bv^b$. (Section 6.3 repeats this computation when it builds the Lagrangian.)

**The requirement.** We look for a derivative of the form

$$
D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi ,
$$

with 16 by 16 matrices $\Omega_\mu(x)$, the spinor connection. It must be compatible with the frame connection in the following precise sense: the derivative of the spinors must induce the frame derivative of the vector $v^a=\bar\Psi\gamma^a\Phi$ of the previous paragraph,

$$
\partial_\mu v^a+\omega_\mu{}^a{}_b\,v^b=(D_\mu\bar\Psi)\gamma^a\Phi+\bar\Psi\gamma^aD_\mu\Phi ,\qquad D_\mu\bar\Psi:=\partial_\mu\bar\Psi-\bar\Psi\,\Omega_\mu .
$$

(The rule for $D_\mu\bar\Psi$ is the one that makes $\bar\Psi\Phi$ behave like a scalar: $(D_\mu\bar\Psi)\Phi+\bar\Psi D_\mu\Phi=\partial_\mu(\bar\Psi\Phi)$. We check below that it agrees with conjugating $D_\mu\Psi$.) Expanding the right-hand side gives $\partial_\mu v^a+\bar\Psi[\gamma^a,\Omega_\mu]\Phi$, so the requirement is, for all $\Psi$ and $\Phi$, $\bar\Psi[\gamma^a,\Omega_\mu]\Phi=\omega_\mu{}^a{}_b\bar\Psi\gamma^b\Phi$, that is

$$
[\Omega_\mu,\gamma^a]=-\omega_\mu{}^a{}_b\,\gamma^b .
$$

**A commutator identity.** From the Clifford relation, for all $a,c,d$:

$$
[S^{cd},\gamma^a]=\eta^{da}\gamma^c-\eta^{ca}\gamma^d .
$$

*Proof.* For $c=d$ both sides vanish. For $c\ne d$, $S^{cd}=\tfrac14(\gamma^c\gamma^d-\gamma^d\gamma^c)=\tfrac12\gamma^c\gamma^d$, because $\gamma^d\gamma^c=-\gamma^c\gamma^d$. Moving $\gamma^a$ through step by step with $\gamma^d\gamma^a=2\eta^{da}-\gamma^a\gamma^d$ and $\gamma^c\gamma^a=2\eta^{ca}-\gamma^a\gamma^c$:

$$
\gamma^c\gamma^d\gamma^a-\gamma^a\gamma^c\gamma^d=\gamma^c(2\eta^{da}-\gamma^a\gamma^d)-\gamma^a\gamma^c\gamma^d=2\eta^{da}\gamma^c-(2\eta^{ca}-\gamma^a\gamma^c)\gamma^d-\gamma^a\gamma^c\gamma^d=2\eta^{da}\gamma^c-2\eta^{ca}\gamma^d .
$$

Divide by 2. $\square$ (This is Stage 1, Result 3.5, checked in all 512 cases: check `ALG_SabGammaCommutator` in `python-geometry-report.json`.)

**Theorem (the spinor connection).** The matrices

$$
\Omega_\mu=\tfrac12\,\omega_{\mu ab}\,S^{ab}=\tfrac18\,\omega_{\mu ab}\,[\gamma^a,\gamma^b]
$$

(summed over all ordered pairs $(a,b)$; summed over $a<b$ only, the coefficient of $[\gamma^a,\gamma^b]$ is $\tfrac14$) satisfy $[\Omega_\mu,\gamma^a]=-\omega_\mu{}^a{}_b\gamma^b$. Every other solution differs from this one by a multiple of the identity matrix, and this one is the only traceless solution.

*Proof.* By the identity,

$$
[\Omega_\mu,\gamma^a]=\tfrac12\,\omega_{\mu cd}\bigl(\eta^{da}\gamma^c-\eta^{ca}\gamma^d\bigr)=\tfrac12\,\omega_{\mu c}{}^{a}\gamma^c-\tfrac12\,\omega_\mu{}^a{}_d\,\gamma^d ,
$$

where $\omega_{\mu c}{}^a:=\omega_{\mu cd}\eta^{da}$. By the antisymmetry, $\omega_{\mu c}{}^a=-\eta^{ad}\omega_{\mu dc}=-\omega_\mu{}^a{}_c$, so both terms equal $-\tfrac12\omega_\mu{}^a{}_c\gamma^c$ and the sum is $-\omega_\mu{}^a{}_c\gamma^c$. If $\Omega'_\mu$ is another solution, $X=\Omega'_\mu-\Omega_\mu$ commutes with all eight $\gamma^a$, so by fact (F1) of Section 4.1 it is a multiple of the identity. Every $S^{ab}$ is traceless (it is a multiple of a commutator, and $\mathrm{tr}(AB)=\mathrm{tr}(BA)$), so $\Omega_\mu$ is traceless, and a traceless multiple of the identity is zero. $\square$

A multiple of the identity, $\Omega'_\mu=\Omega_\mu+iA_\mu\,1$, would be an additional electromagnetic-type field, not part of gravity; the canonical choice of the project has none (Stage 1, §5.3).

**The derivative of the Dirac adjoint.** The matrices $S^{ab}$ are real, and $(S^{ab})^TC=-CS^{ab}$ by fact (F3). Hence $\Omega_\mu$ is real with $\Omega_\mu^TC=-C\Omega_\mu$, and the conjugate transpose of $D_\mu\Psi$, multiplied by $C$, is

$$
(D_\mu\Psi)^\dagger C=\partial_\mu\Psi^\dagger C+\Psi^\dagger\Omega_\mu^TC=\partial_\mu\bar\Psi-\bar\Psi\,\Omega_\mu=D_\mu\bar\Psi ,
$$

consistent with the rule used above.

**Theorem (local spin covariance).** Let the frame be rotated, $e'_\mu{}^a=\Lambda^a{}_b(x)e_\mu{}^b$, and let $R(x)$ be a spin transformation that covers $\Lambda$ in the sense $R^{-1}\gamma^aR=\Lambda^a{}_b\gamma^b$, with $\det R=1$. (This is fact (i) at the beginning of this section, with $\Lambda^a{}_b=\Lambda_{\mathrm u}(R^{-1})_{ba}=(\eta\,\Lambda_{\mathrm u}(R)\,\eta)_{ab}$. For $R$ in Spin(4,4), $\Lambda_{\mathrm u}=\Lambda_{\mathrm t}$. For a rotation in a space-space or time-time plane this $\Lambda$ is the vector image of $R$; for a boost it is its inverse. That every element of Pin(4,4) has determinant 1 as a 16 by 16 matrix is proved in Chapter 2, Section 2.14, and derived in Stage 1, §4.2.) Then the spinor connection of the rotated frame is

$$
\Omega'_\mu=R\,\Omega_\mu R^{-1}-(\partial_\mu R)R^{-1},\qquad\text{and}\qquad D'_\mu(R\Psi)=R\,D_\mu\Psi .
$$

*Proof.* By the uniqueness part of the previous theorem it suffices to show that the right-hand side, call it $X_\mu$, is traceless and satisfies $[X_\mu,\gamma^a]=-\omega'_\mu{}^a{}_b\gamma^b$ with $\omega'_\mu=\Lambda\omega_\mu\Lambda^{-1}-(\partial_\mu\Lambda)\Lambda^{-1}$ (Section 4.11). First, $[R\Omega_\mu R^{-1},\gamma^a]=R\,[\Omega_\mu,R^{-1}\gamma^aR]\,R^{-1}=\Lambda^a{}_bR[\Omega_\mu,\gamma^b]R^{-1}=-\Lambda^a{}_b\,\omega_\mu{}^b{}_c\,R\gamma^cR^{-1}$, and $R\gamma^cR^{-1}=(\Lambda^{-1})^c{}_d\gamma^d$ (invert the covering relation), so this term is $-(\Lambda\omega_\mu\Lambda^{-1})^a{}_d\gamma^d$. Second, differentiate $R^{-1}\gamma^aR=\Lambda^a{}_b\gamma^b$, using $\partial_\mu(R^{-1})=-R^{-1}(\partial_\mu R)R^{-1}$, and multiply by $R$ on the left and $R^{-1}$ on the right:

$$
-(\partial_\mu R)R^{-1}\gamma^a+\gamma^a(\partial_\mu R)R^{-1}=(\partial_\mu\Lambda^a{}_b)\,R\gamma^bR^{-1}=\bigl((\partial_\mu\Lambda)\Lambda^{-1}\bigr)^a{}_d\,\gamma^d .
$$

The left side is $-[(\partial_\mu R)R^{-1},\gamma^a]$. Adding the two parts, $[X_\mu,\gamma^a]=-(\Lambda\omega_\mu\Lambda^{-1}-(\partial_\mu\Lambda)\Lambda^{-1})^a{}_d\gamma^d$, as required. Traces: $\mathrm{tr}(R\Omega_\mu R^{-1})=\mathrm{tr}\,\Omega_\mu=0$, and $\mathrm{tr}((\partial_\mu R)R^{-1})=\mathrm{tr}(R^{-1}\partial_\mu R)=(\partial_\mu\det R)/\det R=0$, because $\det R=1$ is constant (the middle step is the determinant lemma of Section 4.5, whose proof works unchanged for complex matrices). Finally $D'_\mu(R\Psi)=(\partial_\mu R)\Psi+R\partial_\mu\Psi+R\Omega_\mu\Psi-(\partial_\mu R)\Psi=R\,D_\mu\Psi$. $\square$

Stage 1 tested this with finite, point-dependent products of two reflections built from exact rational vector fields: recomputing $\Omega$ from the rotated frame gives exactly $R\Omega R^{-1}-(\partial R)R^{-1}$ and $\gamma'^\mu=R\gamma^\mu R^{-1}$ (Stage 1, Result 5.4; checks `LAG_localSpinInvariance_G1` and `LAG_localSpinInvariance_G2` in `wolfram-geometry-report.json`).

**Theorem (the gammas are covariantly constant).** With the canonical connection,

$$
D_\mu\gamma^\nu:=\partial_\mu\gamma^\nu+\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda+[\Omega_\mu,\gamma^\nu]=0\qquad\text{for all }\mu,\nu ,
$$

and this statement is equivalent to the vielbein postulate.

*Proof.* Insert $\gamma^\nu=e_a{}^\nu\gamma^a$ and use the defining property: $e_a{}^\nu[\Omega_\mu,\gamma^a]=-e_a{}^\nu\,\omega_\mu{}^a{}_c\,\gamma^c=-\omega_\mu{}^b{}_a\,e_b{}^\nu\,\gamma^a$ (in the last step the summed indices were renamed, $a\to b$ and $c\to a$). So

$$
D_\mu\gamma^\nu=\bigl(\partial_\mu e_a{}^\nu+\Gamma^\nu{}_{\mu\lambda}e_a{}^\lambda-\omega_\mu{}^b{}_a\,e_b{}^\nu\bigr)\gamma^a ,
$$

and the bracket is the inverse vielbein postulate of Section 4.11, which vanishes. Conversely, if $D_\mu\gamma^\nu=0$, the bracket vanishes because the eight $\gamma^a$ are linearly independent (fact (F2)), which gives back the inverse postulate and hence the postulate. $\square$

This is Stage 1, Result 5.2, verified in all 64 pairs $(\mu,\nu)$ in G1 and G2 (checks `GEO_gammaCovariantConstancy_G1` and `GEO_gammaCovariantConstancy_G2`), and in the primordial field by the Stage-2 check `P_gammaConst_DmuGammaNuZero64`.

**The divergence identity.** Contract $\mu$ with $\nu$ in $D_\mu\gamma^\nu=0$ and use $\Gamma^\mu{}_{\mu\lambda}=\partial_\lambda\ln\sqrt{\lvert g\rvert}$ (Section 4.5):

$$
\partial_\mu\gamma^\mu+\bigl(\partial_\lambda\ln\sqrt{\lvert g\rvert}\bigr)\gamma^\lambda=-[\Omega_\mu,\gamma^\mu]
\qquad\Longleftrightarrow\qquad
\partial_\mu\bigl(\sqrt{\lvert g\rvert}\,\gamma^\mu\bigr)=\sqrt{\lvert g\rvert}\,[\gamma^\mu,\Omega_\mu].
$$

(Stage 1, Result 5.3; checks `GEO_divergenceIdentity_G1` and `GEO_divergenceIdentity_G2`.) This identity is used in Chapter 5, to show that the notebook's Lagrangian carries no dynamics for a Grassmann field, and in Chapter 7, to derive the field equations.

**Diagonal vielbeins: the contraction $\gamma^\mu\Omega_\mu$.** For $e_\mu{}^a=h_\mu\delta_\mu{}^a$ the field equations of Chapter 7 need only the combination $\gamma^\mu\Omega_\mu$ (summed over $\mu$). We show

$$
\gamma^\mu\Omega_\mu=\frac12\sum_{b=0}^{n-1}\frac{1}{h_b}\,\partial_b\ln\Bigl(\prod_{c\ne b}h_c\Bigr)\gamma^b ,\qquad \{\gamma^\mu,\Omega_\mu\}=0 .
$$

*Proof.* Here $\gamma^\mu=\gamma^\mu_{\text{frame}}/h_\mu$, where $\gamma^\mu_{\text{frame}}$ is the frame matrix with the same number, and $S^{ab}=\tfrac12\gamma^a\gamma^b$ for $a\ne b$. By Section 4.11 only $\omega_{\mu\mu b}=-\omega_{\mu b\mu}$ with $b\ne\mu$ are nonzero, so $\Omega_\mu=\omega_{\mu\mu b}S^{\mu b}$ summed over $b\ne\mu$ (the two orders of each pair give equal terms, which cancels the $\tfrac12$). Then

$$
\gamma^\mu\Omega_\mu=\sum_\mu\sum_{b\ne\mu}\frac{1}{h_\mu}\,\eta_{\mu\mu}\frac{\partial_bh_\mu}{h_b}\cdot\tfrac12\gamma^\mu\gamma^\mu\gamma^b=\frac12\sum_b\frac1{h_b}\sum_{\mu\ne b}\frac{\partial_bh_\mu}{h_\mu}\,\gamma^b ,
$$

because $\gamma^\mu\gamma^\mu=\eta^{\mu\mu}$ for a frame matrix and $\eta_{\mu\mu}\eta^{\mu\mu}=1$. The inner sum is $\partial_b\ln\prod_{c\ne b}h_c$. For the anticommutator: $\gamma^\mu S^{\mu b}=\tfrac12\eta^{\mu\mu}\gamma^b$ and $S^{\mu b}\gamma^\mu=\tfrac12\gamma^\mu\gamma^b\gamma^\mu=-\tfrac12\eta^{\mu\mu}\gamma^b$, so every term of $\{\gamma^\mu,\Omega_\mu\}$ cancels. $\square$

This is the formula of Stage 1, §8.5 (checks `GEO_diagonalSlashFormula_G2` and `GEO_diagonalSlashFormula_G3`; `GEO_anticommutatorGammaOmegaVanishesDiagonal_G2` for the anticommutator).

**Worked example: the polar plane.** Only $\omega_{\varphi01}=-1=-\omega_{\varphi10}$ is nonzero, so $\Omega_r=0$ and $\Omega_\varphi=\omega_{\varphi01}S^{01}=-\tfrac12\gamma^0\gamma^1=-\tfrac12\sigma_1\sigma_2=-\tfrac i2\sigma_3$. Directly,

$$
\gamma^\mu\Omega_\mu=\frac{\sigma_2}{r}\Bigl(-\frac i2\sigma_3\Bigr)=-\frac{i}{2r}\,\sigma_2\sigma_3=-\frac{i}{2r}\,i\sigma_1=\frac{1}{2r}\,\sigma_1 ,
$$

in agreement with the formula: only $b=0$ contributes, $\frac12\cdot\frac11\cdot\partial_r\ln r\,\gamma^0=\frac1{2r}\sigma_1$. The Dirac operator of the plane in polar coordinates is therefore

$$
\gamma^\mu D_\mu=\sigma_1\Bigl(\partial_r+\frac{1}{2r}\Bigr)+\frac{\sigma_2}{r}\,\partial_\varphi .
$$

The term $1/(2r)$ is exactly what the turning polar frame requires; Exercise 4.8 shows where it comes from.

**Worked example: the primordial field.** With the 24 components of Section 4.11 (only the pairs $(i,0)$, $(i,4)$ for $\mu=i$ and $(j,0)$, $(j,4)$ for $\mu=j$), each $\Omega_\mu$ has two terms:

$$
\begin{aligned}
\Omega_0&=\Omega_4=0,\\
\Omega_i&=\omega_{i\,i0}S^{i0}+\omega_{i\,i4}S^{i4}=-\alpha_i\bigl(S^{0i}+a_4'S^{4i}\bigr)\qquad(i=1,2,3),\\
\Omega_j&=\omega_{j\,j0}S^{j0}+\omega_{j\,j4}S^{j4}=\alpha_j\bigl(S^{0j}-a_4'S^{4j}\bigr)\qquad(j=5,6,7),
\end{aligned}
$$

using $S^{ba}=-S^{ab}$ (Stage-2 document, §7.1; check `P_Omega_closedForms`). Now contract with $\gamma^{x_i}=\gamma^i/h_i$ and $\gamma^{x_j}=\gamma^j/h_j$; note $\alpha_i/h_i=\alpha_j/h_j=H$. With $S^{0i}=\tfrac12\gamma^0\gamma^i$ and $\gamma^i\gamma^0\gamma^i=-\gamma^0(\gamma^i)^2=-\gamma^0$, $\gamma^i\gamma^4\gamma^i=-\gamma^4$ (since $(\gamma^i)^2=+1$), and, since $(\gamma^j)^2=-1$, $\gamma^j\gamma^0\gamma^j=\gamma^0$, $\gamma^j\gamma^4\gamma^j=\gamma^4$:

$$
\begin{aligned}
\gamma^{x_i}\Omega_i&=-\tfrac H2\bigl(\gamma^i\gamma^0\gamma^i+a_4'\gamma^i\gamma^4\gamma^i\bigr)=\tfrac H2\bigl(\gamma^0+a_4'\gamma^4\bigr),\\
\gamma^{x_j}\Omega_j&=\tfrac H2\bigl(\gamma^j\gamma^0\gamma^j-a_4'\gamma^j\gamma^4\gamma^j\bigr)=\tfrac H2\bigl(\gamma^0-a_4'\gamma^4\bigr).
\end{aligned}
$$

Summing over the three $i$ and the three $j$,

$$
\gamma^\mu\Omega_\mu=\tfrac{3H}2\bigl(\gamma^0+a_4'\gamma^4\bigr)+\tfrac{3H}2\bigl(\gamma^0-a_4'\gamma^4\bigr)=3H\gamma^0 .
$$

The free function $a_4$ cancels: the boosts of 3-space and the rotations of the extra times contribute opposite amounts. The general formula agrees: only $b=0$ contributes, because $\prod_{c\ne0}h_c=s^{1/2}e^{3a_4}\cdot1\cdot s^{1/2}e^{-3a_4}=s$ gives $\frac12\tan z\,\partial_0\ln s=\frac12\tan z\cdot6H\cot z=3H$, while $\prod_{c\ne4}h_c=\cot z\cdot s=\cos z$ does not depend on $x^4$. In words, $a_4$ cancels because the 7-volume of a comoving region is constant (Section 4.4; Stage-2 document, §8.1; checks `P_Omega_gammaSlash3Hgamma0` and `P_Omega_contractDiagonalFormula`; Stage-1 check `GEO_primordialInvariants_G2`). With $\{\gamma^\mu,\Omega_\mu\}=0$ we get $[\gamma^\mu,\Omega_\mu]=6H\gamma^0$, and the divergence identity can be checked by hand: $\partial_\mu(\sqrt{\lvert g\rvert}\gamma^\mu)=\partial_0(\cos z\tan z\,\gamma^0)=\partial_0(\sin z)\gamma^0=6H\cos z\,\gamma^0=\sqrt{\lvert g\rvert}\cdot6H\gamma^0$ (check `P_gammaConst_divergenceIdentity`).

### 4.13 The curvature of the spinor connection

**Definition.** The curvature of the spinor connection is the commutator of two spinor covariant derivatives. For a spinor field $\Psi$ (no curved index),

$$
D_\mu(D_\nu\Psi)-D_\nu(D_\mu\Psi)=F_{\mu\nu}\Psi,\qquad F_{\mu\nu}:=\partial_\mu\Omega_\nu-\partial_\nu\Omega_\mu+[\Omega_\mu,\Omega_\nu],
$$

where here $D_\mu$ acts on $D_\nu\Psi$ as on a spinor, $D_\mu(D_\nu\Psi)=\partial_\mu(D_\nu\Psi)+\Omega_\mu D_\nu\Psi$. (Expand: the terms $\partial_\mu\partial_\nu\Psi$ and $\Omega_\nu\partial_\mu\Psi+\Omega_\mu\partial_\nu\Psi$ are symmetric in $\mu,\nu$ and cancel; what remains is $(\partial_\mu\Omega_\nu)\Psi+\Omega_\mu\Omega_\nu\Psi$ minus the same with $\mu\leftrightarrow\nu$.)

**Lemma ($\Omega$ respects commutators).** For two antisymmetric arrays $A_{ab}$ and $B_{ab}$ put $\Omega(A)=\tfrac12A_{ab}S^{ab}$, and regard $A^a{}_b=\eta^{ac}A_{cb}$ as a matrix. Then

$$
[\Omega(A),\Omega(B)]=\Omega\bigl([A,B]\bigr),
$$

where $[A,B]$ is the matrix commutator, lowered with $\eta$.

*Proof.* First, $[A,B]$ is again antisymmetric after lowering. In matrix form, "$\eta A$ is antisymmetric" means $A^T\eta=-\eta A$. Then $(AB)^T\eta=B^TA^T\eta=-B^T\eta A=\eta BA$, so $[A,B]^T\eta=\eta BA-\eta AB=-\eta[A,B]$. Second, by the theorem of Section 4.12, $[\Omega(A),\gamma^e]=-A^e{}_f\gamma^f$ for any such $A$. The Jacobi identity $[[X,Y],Z]=[X,[Y,Z]]-[Y,[X,Z]]$, which one checks by expanding all commutators, gives

$$
[[\Omega(A),\Omega(B)],\gamma^e]=[\Omega(A),-B^e{}_f\gamma^f]-[\Omega(B),-A^e{}_f\gamma^f]=B^e{}_fA^f{}_g\gamma^g-A^e{}_fB^f{}_g\gamma^g=-[A,B]^e{}_g\gamma^g .
$$

So $[\Omega(A),\Omega(B)]$ and $\Omega([A,B])$ have the same commutator with every $\gamma^e$. Their difference commutes with all $\gamma^e$ and is traceless (a commutator has zero trace, and so has every $S^{ab}$), hence it is zero by fact (F1). $\square$

**Lemma (frame curvature).** Define the curvature of the frame connection,

$$
R(\omega)^a{}_{b\mu\nu}:=\partial_\mu\omega_\nu{}^a{}_b-\partial_\nu\omega_\mu{}^a{}_b+\omega_\mu{}^a{}_c\,\omega_\nu{}^c{}_b-\omega_\nu{}^a{}_c\,\omega_\mu{}^c{}_b .
$$

Then $R(\omega)^a{}_{b\mu\nu}=e_\rho{}^a\,R^\rho{}_{\sigma\mu\nu}\,e_b{}^\sigma$: it is the Riemann tensor written with two frame indices.

*Proof.* For a vector field with frame components $V^a$, let the total covariant derivative act with $\omega$ on frame indices and $\Gamma$ on curved indices: $\nabla_\nu V^a=\partial_\nu V^a+\omega_\nu{}^a{}_bV^b$ and $\nabla_\mu(\nabla_\nu V^a)=\partial_\mu(\nabla_\nu V^a)+\omega_\mu{}^a{}_c\nabla_\nu V^c-\Gamma^\lambda{}_{\mu\nu}\nabla_\lambda V^a$. Exactly as in the proof of the Riemann formula (Section 4.7), the commutator is $[\nabla_\mu,\nabla_\nu]V^a=R(\omega)^a{}_{b\mu\nu}V^b$: the $\Gamma$ term drops out by the symmetry of $\Gamma$, the second derivatives and the mixed first-derivative terms drop out by symmetry. On the other hand, frame components of covariant derivatives are covariant derivatives of frame components, and this stays true one step further. For $V$ itself it is the requirement that defined $\omega$ in Section 4.11: $\nabla_\nu V^a=e_\rho{}^a\nabla_\nu V^\rho$. The object $T^\rho{}_\nu:=\nabla_\nu V^\rho$ carries one extra lower curved index, which the total covariant derivative treats with $\Gamma$, both in $T^\rho{}_\nu$ and in its frame components $e_\rho{}^aT^\rho{}_\nu=\nabla_\nu V^a$. By the product rule,

$$
\begin{aligned}
\nabla_\mu\bigl(e_\rho{}^aT^\rho{}_\nu\bigr)&=\partial_\mu\bigl(e_\rho{}^aT^\rho{}_\nu\bigr)+\omega_\mu{}^a{}_b\,e_\rho{}^bT^\rho{}_\nu-\Gamma^\lambda{}_{\mu\nu}\,e_\rho{}^aT^\rho{}_\lambda\\
&=\bigl(\partial_\mu e_\rho{}^a+\omega_\mu{}^a{}_b\,e_\rho{}^b\bigr)T^\rho{}_\nu+e_\rho{}^a\partial_\mu T^\rho{}_\nu-\Gamma^\lambda{}_{\mu\nu}\,e_\rho{}^aT^\rho{}_\lambda .
\end{aligned}
$$

By the vielbein postulate $\partial_\mu e_\rho{}^a+\omega_\mu{}^a{}_b\,e_\rho{}^b=\Gamma^\lambda{}_{\mu\rho}\,e_\lambda{}^a$, so, after renaming summed indices, this equals

$$
e_\lambda{}^a\bigl(\partial_\mu T^\lambda{}_\nu+\Gamma^\lambda{}_{\mu\rho}T^\rho{}_\nu-\Gamma^\rho{}_{\mu\nu}T^\lambda{}_\rho\bigr)=e_\lambda{}^a\,\nabla_\mu T^\lambda{}_\nu .
$$

So $\nabla_\mu(\nabla_\nu V^a)=e_\lambda{}^a\nabla_\mu\nabla_\nu V^\lambda$, and hence $[\nabla_\mu,\nabla_\nu]V^a=e_\rho{}^a[\nabla_\mu,\nabla_\nu]V^\rho=e_\rho{}^aR^\rho{}_{\sigma\mu\nu}V^\sigma=e_\rho{}^aR^\rho{}_{\sigma\mu\nu}e_b{}^\sigma V^b$. Both results hold for every $V$. $\square$

**Theorem (spinor curvature).** $F_{\mu\nu}=\tfrac12\,R_{ab\mu\nu}\,S^{ab}$ with $R_{ab\mu\nu}:=\eta_{ac}\,e_\rho{}^c\,R^\rho{}_{\sigma\mu\nu}\,e_b{}^\sigma$.

*Proof.* $\Omega_\mu=\Omega(\omega_\mu)$ is linear in $\omega$, so $\partial_\mu\Omega_\nu-\partial_\nu\Omega_\mu=\Omega(\partial_\mu\omega_\nu-\partial_\nu\omega_\mu)$, and by the first lemma $[\Omega_\mu,\Omega_\nu]=\Omega([\omega_\mu,\omega_\nu])$. So $F_{\mu\nu}=\Omega(R(\omega)_{\mu\nu})$, and the second lemma identifies $R(\omega)$. $\square$

The sign and the placement of $\eta$ matter. Stage 1 verified the form with $+\tfrac12$ and the lowered first index at all six Wolfram points and at the Python points; the forms with $-\tfrac12$ and without $\eta$ (mixed indices) fail there (Stage 1, Result 5.5; checks `GEO_curvature_G1` and `GEO_curvature_G2`; measurements `G1.p1.curvatureCandidate.plusHalfLowered` = true, `minusHalfLowered` = false and `plusHalfMixedNoEta` = false in `wolfram-geometry-report.json`).

**Theorem (the spin connection cannot be removed in a curved field).** Near a point, the spinor connection is pure gauge, $\Omega_\mu=-(\partial_\mu U)U^{-1}$ for some spin transformation $U(x)$, if and only if the Riemann tensor vanishes there. (The spin transformation is called $U$ here, not $R$, because the proof also uses the Riemann tensor $R_{ab\mu\nu}$.)

*Proof.* If $\Omega_\mu=-(\partial_\mu U)U^{-1}$, then, with $\partial_\mu(U^{-1})=-U^{-1}(\partial_\mu U)U^{-1}$,

$$
\partial_\mu\Omega_\nu-\partial_\nu\Omega_\mu=(\partial_\nu U)U^{-1}(\partial_\mu U)U^{-1}-(\partial_\mu U)U^{-1}(\partial_\nu U)U^{-1}=-[\Omega_\mu,\Omega_\nu],
$$

because the second derivatives $\partial_\mu\partial_\nu U$ cancel. So $F_{\mu\nu}=0$. By the theorem above $R_{ab\mu\nu}S^{ab}=2\sum_{a<b}R_{ab\mu\nu}S^{ab}=0$; the 28 matrices $S^{ab}$ with $a<b$ are linearly independent (fact (F2)), so every $R_{ab\mu\nu}=0$, and since the vielbein is invertible the Riemann tensor vanishes. Conversely, if the Riemann tensor vanishes near the point, the flatness theorem quoted in Section 4.7 gives a chart with $g_{\mu\nu}=\eta_{\mu\nu}$; in it the frame $e_\mu{}^a=\delta_\mu{}^a$ has $\Gamma=0$, $\omega=0$ and $\Omega=0$. Any other frame is a rotation of this one by some $\Lambda(x)$. Let $U(x)$ cover $\Lambda(x)$; the covariance theorem of Section 4.12, with $U$ in the role of $R$ there, gives the spinor connection $U\cdot0\cdot U^{-1}-(\partial_\mu U)U^{-1}=-(\partial_\mu U)U^{-1}$. (That a smooth frame rotation $\Lambda(x)$ has a smooth covering $U(x)$ near a point is a standard fact that we quote.) $\square$

Since the primordial field is curved everywhere (Section 4.7), its spin connection cannot be removed by any choice of frame (Stage-2 document, §7.3).

**The square of the Dirac operator.** The Dirac operator is $\gamma^\mu D_\mu$. For an object with one curved index and one spinor index, such as $D_\nu\Psi$, the full covariant derivative is $\nabla_\mu(D_\nu\Psi)=\partial_\mu(D_\nu\Psi)+\Omega_\mu D_\nu\Psi-\Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi$.

**Theorem (Lichnerowicz formula).**

$$
(\gamma^\mu D_\mu)^2\Psi=g^{\mu\nu}\bigl(D_\mu D_\nu\Psi-\Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi\bigr)-\tfrac14\,R\,\Psi .
$$

*Proof.* Step 1. $(\gamma^\mu D_\mu)(\gamma^\nu D_\nu\Psi)=\gamma^\mu\bigl[\partial_\mu(\gamma^\nu D_\nu\Psi)+\Omega_\mu\gamma^\nu D_\nu\Psi\bigr]$. Replace $\partial_\mu\gamma^\nu$ by $-\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda-[\Omega_\mu,\gamma^\nu]$ (covariant constancy of the gammas). The two terms $\mp\Omega_\mu\gamma^\nu D_\nu\Psi$ cancel, and

$$
(\gamma^\mu D_\mu)^2\Psi=\gamma^\mu\gamma^\nu\bigl(\partial_\mu D_\nu\Psi+\Omega_\mu D_\nu\Psi\bigr)-\gamma^\mu\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda D_\nu\Psi=\gamma^\mu\gamma^\nu\,\nabla_\mu(D_\nu\Psi),
$$

after renaming $\lambda\leftrightarrow\nu$ in the last term. Step 2. Split $\gamma^\mu\gamma^\nu=g^{\mu\nu}+\tfrac12[\gamma^\mu,\gamma^\nu]$ (the curved Clifford relation). The first part, $g^{\mu\nu}\nabla_\mu(D_\nu\Psi)$, is the first term of the formula. The second part is $\tfrac12[\gamma^\mu,\gamma^\nu]\nabla_\mu(D_\nu\Psi)$. Since $[\gamma^\mu,\gamma^\nu]$ is antisymmetric in $\mu,\nu$, only the antisymmetric part of $\nabla_\mu(D_\nu\Psi)$ contributes, and that is $\tfrac12\bigl(\nabla_\mu(D_\nu\Psi)-\nabla_\nu(D_\mu\Psi)\bigr)=\tfrac12F_{\mu\nu}\Psi$ (the $\Gamma$ terms cancel because $\Gamma$ is symmetric). So the second part is $\tfrac14[\gamma^\mu,\gamma^\nu]F_{\mu\nu}\Psi=\tfrac12\gamma^\mu\gamma^\nu F_{\mu\nu}\Psi$, where the last step uses $\gamma^\nu\gamma^\mu F_{\mu\nu}=-\gamma^\nu\gamma^\mu F_{\nu\mu}=-\gamma^\mu\gamma^\nu F_{\mu\nu}$ (rename the summed indices). Step 3. In frame components, $\gamma^\mu\gamma^\nu F_{\mu\nu}=\gamma^c\gamma^dF_{cd}$ with $F_{cd}=\tfrac12R_{abcd}S^{ab}=\tfrac14R_{abcd}\gamma^a\gamma^b$ (the terms with $a=b$ vanish, and $S^{ab}=\tfrac12\gamma^a\gamma^b$ otherwise). The symmetries (S1) to (S4) hold equally for the frame components $R_{abcd}$, which are obtained from $R_{\rho\sigma\mu\nu}$ by multiplying with inverse vielbeins. By pair symmetry (S4), $R_{abcd}\gamma^c\gamma^d\gamma^a\gamma^b=R_{cdab}\gamma^c\gamma^d\gamma^a\gamma^b$, which after renaming the summed indices is $R_{abcd}\gamma^a\gamma^b\gamma^c\gamma^d$. Step 4. For three frame gammas,

$$
\gamma^b\gamma^c\gamma^d=\gamma^{[bcd]}+\eta^{bc}\gamma^d-\eta^{bd}\gamma^c+\eta^{cd}\gamma^b ,
$$

where $\gamma^{[bcd]}$ is totally antisymmetric in $b,c,d$ (it equals $\gamma^b\gamma^c\gamma^d$ when the three are different and is zero otherwise). To check it, try the five cases: all different; $b=c\ne d$; $b=d\ne c$; $c=d\ne b$; all equal. For example for $b=d\ne c$ the left side is $\gamma^b\gamma^c\gamma^b=-\eta^{bb}\gamma^c$ and the right side is $-\eta^{bb}\gamma^c$. Contract with $R_{abcd}$. The antisymmetric part gives zero by the first Bianchi identity (S3) in the last three indices, which for frame components reads $R_{abcd}+R_{acdb}+R_{adbc}=0$. Because $\gamma^{[bcd]}$ is unchanged by a cyclic permutation of $(b,c,d)$ (a cyclic permutation of three indices is an even rearrangement), renaming the summed indices gives $R_{abcd}\gamma^{[bcd]}=R_{acdb}\gamma^{[bcd]}=R_{adbc}\gamma^{[bcd]}$; for example, in $R_{acdb}\gamma^{[bcd]}$ rename $c\to b$, $d\to c$, $b\to d$ to get $R_{abcd}\gamma^{[dbc]}=R_{abcd}\gamma^{[bcd]}$. Hence $3R_{abcd}\gamma^{[bcd]}=(R_{abcd}+R_{acdb}+R_{adbc})\gamma^{[bcd]}=0$. The three other terms give $\eta^{bc}R_{abcd}\gamma^d=-R_{ad}\gamma^d$, $-\eta^{bd}R_{abcd}\gamma^c=-R_{ac}\gamma^c$ and $\eta^{cd}R_{abcd}\gamma^b=0$, where we used (S1), (S2) and the frame Ricci tensor $R_{bd}=\eta^{ac}R_{abcd}$ with its symmetry. Hence $R_{abcd}\gamma^b\gamma^c\gamma^d=-2R_{ad}\gamma^d$ and

$$
R_{abcd}\gamma^a\gamma^b\gamma^c\gamma^d=-2R_{ad}\gamma^a\gamma^d=-2R_{ad}\,\eta^{ad}=-2R ,
$$

because $R_{ad}$ is symmetric and $\tfrac12(\gamma^a\gamma^d+\gamma^d\gamma^a)=\eta^{ad}$. Step 5. The second part of Step 2 is $\tfrac12\cdot\tfrac14\cdot(-2R)\Psi=-\tfrac14R\Psi$. $\square$

The constant $-\tfrac14$ is exactly the value that Stage 1 measured at all its test points: `lichnerowiczC` = -1/4 at the three G1 points and the three Wolfram G2 points, with $+\tfrac14$ failing (Stage 1, Result 8.2; checks `GEO_lichnerowicz_G1`, `GEO_lichnerowicz_G2` and `GEO_lichnerowiczConstantSameG1G2`). In the primordial field, with $R=6H^2(a_4'^2-7)$, the curvature term is $-\tfrac R4\Psi=\tfrac32H^2(7-a_4'^2)\Psi$, which is $9H^2\Psi$ for $a_4=t$ (Stage-2 document, §7.3). Because of this term, curvature enters the second-order form of the field equations explicitly (Chapter 7).

### 4.14 Why the notebook's contraction is wrong

**What the notebook does.** The notebook's Lagrangian Lg[] (cell 1064, In[1034]) is quoted verbatim in the Stage-1 document (§6.1; line breaks only for the page width):

```
Lg[]:=Sqrt[detgg] *( Transpose[\[CapitalPsi]16].\[Sigma]16.
Sum[FullSimplify[((T16^\[Alpha])[\[Alpha]1-1]/.sg),constraintVars].
(D[ \[CapitalPsi]16,X[[\[Alpha]1]]]+(Q1/2)*Sum[\[Omega]mat[[\[Alpha]1,a,b]]*SAB[[a,
b]].\[CapitalPsi]16,{a,1,8},{b,1,8}]),{\[Alpha]1,1,Length[X]}]+
(H*M)*Transpose[\[CapitalPsi]16].\[Sigma]16.\[CapitalPsi]16)//Simplify[#,
constraintVars]&
```

Mathematica lists count from 1, so `ωmat[[μ+1,a+1,b+1]]` is our $\omega_\mu{}^a{}_b$, the mixed spin connection with the first frame index up, and `SAB[[a+1,b+1]]` is $S^{ab}$, with both indices up. `Q1` (written $Q_1$ below) is the notebook's book-keeping switch for the spin connection; the notebook keeps it as a symbol (cell 1063; `handoff/surveys/survey_notebook-physics.md`, item 4), and setting it to 1, as Stage 1 does, switches the connection on. So, with $Q_1=1$, the notebook's spinor connection is

$$
\Omega^{\mathrm{nb}}_\mu=\tfrac12\,\omega_\mu{}^a{}_b\,S^{ab}\qquad\text{instead of}\qquad \Omega_\mu=\tfrac12\,\omega_{\mu ab}\,S^{ab}.
$$

The factor $\tfrac12$ is right. What is wrong is the index placement: the contraction pairs the upper index $a$ of $\omega$ with the upper index $a$ of $S^{ab}$. One $\eta$ is missing. Section 4.3 warned that summing two upper indices does not give a frame-independent result; here is what it does.

**What the missing $\eta$ deletes.** Since $\omega_\mu{}^a{}_b=\eta^{aa}\omega_{\mu ab}$ (no sum, $\eta^{aa}=\pm1$),

$$
\Omega^{\mathrm{nb}}_\mu=\tfrac12\sum_{a,b}\eta^{aa}\,\omega_{\mu ab}\,S^{ab}.
$$

Sort the pairs $(a,b)$ into three kinds.

- Both space-like ($a,b\in\{0,1,2,3\}$): $\eta^{aa}=+1$, the term is the same as in $\Omega_\mu$.
- Both time-like ($a,b\in\{4,5,6,7\}$): $\eta^{aa}=-1$, the term has the wrong sign.
- One space-like and one time-like (a boost pair): the two orders give $\eta^{aa}\omega_{\mu ab}S^{ab}+\eta^{bb}\omega_{\mu ba}S^{ba}=(\eta^{aa}+\eta^{bb})\,\omega_{\mu ab}S^{ab}=0$, because $\omega_{\mu ba}S^{ba}=\omega_{\mu ab}S^{ab}$ and $\eta^{aa}+\eta^{bb}=0$.

So, writing $\Omega_\mu=\Omega^{\mathrm{ss}}_\mu+\Omega^{\mathrm{tt}}_\mu+\Omega^{\mathrm{st}}_\mu$ for the space-space, time-time and boost parts,

$$
\Omega^{\mathrm{nb}}_\mu=\Omega^{\mathrm{ss}}_\mu-\Omega^{\mathrm{tt}}_\mu,\qquad \Omega^{\mathrm{nb}}_\mu-\Omega_\mu=-\Omega^{\mathrm{st}}_\mu-2\,\Omega^{\mathrm{tt}}_\mu .
$$

Of the 28 pairs $a<b$ in signature (4,4), 6 are space-space, 6 are time-time and $4\times4=16$ are boost pairs: for each $\mu$, the notebook's contraction deletes 16 of the 28 independent components of the connection and reverses the sign of 6 more. (This is the index argument of Stage 1, §5.6, and of `handoff/specs/CONTRACT.md`, §3, item 4.) In a positive-definite space, such as the polar plane or the sphere, all $\eta^{aa}=+1$ and the two contractions coincide. The mistake is therefore invisible in every textbook example with a positive metric; it appears only with an indefinite metric.

**Consequence: the gammas are no longer covariantly constant.** With $\Omega^{\mathrm{nb}}$ in place of $\Omega$ the covariant derivative of the gammas is, by the theorem of Section 4.12,

$$
D^{\mathrm{nb}}_\mu\gamma^\nu=\partial_\mu\gamma^\nu+\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda+[\Omega^{\mathrm{nb}}_\mu,\gamma^\nu]=[\Omega^{\mathrm{nb}}_\mu-\Omega_\mu,\gamma^\nu].
$$

The difference $X_\mu=\Omega^{\mathrm{nb}}_\mu-\Omega_\mu$ is a combination of the $S^{ab}$, hence traceless. If it commuted with all $\gamma^\nu$, it would be a multiple of the identity by fact (F1), hence zero. So $D^{\mathrm{nb}}_\mu\gamma^\nu=0$ for all $\nu$ holds only if the boost and time-time parts of $\omega_\mu$ vanish, which is not the case in a generic field. Everything that the book derives from $D_\mu\gamma^\nu=0$, or from the defining property $[\Omega_\mu,\gamma^a]=-\omega_\mu{}^a{}_b\gamma^b$, then fails: the divergence identity, the Lichnerowicz formula, local spin covariance, and the derivation of the field equations in Chapter 7.

**Worked example: the primordial field.** From Section 4.12, $\Omega_i=-\alpha_i(S^{0i}+a_4'S^{4i})$ and $\Omega_j=\alpha_j(S^{0j}-a_4'S^{4j})$. The pair $(0,i)$ is space-space, $(4,i)$ is a boost, $(0,j)$ is a boost and $(4,j)$ is time-time. So

$$
\Omega^{\mathrm{nb}}_i=-\alpha_i\,S^{0i},\qquad \Omega^{\mathrm{nb}}_j=+\alpha_j\,a_4'\,S^{4j}.
$$

Repeat the computation of Section 4.12 with these: $\gamma^{x_i}\Omega^{\mathrm{nb}}_i=-\tfrac H2\gamma^i\gamma^0\gamma^i=\tfrac H2\gamma^0$ and $\gamma^{x_j}\Omega^{\mathrm{nb}}_j=\tfrac{Ha_4'}{2}\gamma^j\gamma^4\gamma^j=\tfrac{Ha_4'}2\gamma^4$. Summing,

$$
\gamma^\mu\Omega^{\mathrm{nb}}_\mu=\tfrac{3H}{2}\bigl(\gamma^0+a_4'\gamma^4\bigr)\qquad\text{instead of the correct}\qquad \gamma^\mu\Omega_\mu=3H\gamma^0 .
$$

Half of the $\gamma^0$ term is lost, and the $a_4'$ terms no longer cancel. *Numbers.* At the three exact G2 test points of Stage 1, $(H,a_4')=(2/3,3/7)$, $(1/5,-4/9)$ and $(5/7,6/5)$, this gives $\gamma^0+\tfrac37\gamma^4$, $\tfrac3{10}\gamma^0-\tfrac2{15}\gamma^4$ and $\tfrac{15}{14}\gamma^0+\tfrac97\gamma^4$, exactly the values recorded as `G2.p1.notebookSlash`, `G2.p2.notebookSlash` and `G2.p3.notebookSlash` in `wolfram-geometry-report.json`; the correct values are $2\gamma^0$, $\tfrac35\gamma^0$ and $\tfrac{15}7\gamma^0$.

**Worked example: one component of $D_\mu\gamma^\nu$.** Take $\mu=1$, $\nu=4$. Since $\gamma^{x_4}=\gamma^4$ is constant, $\partial_1\gamma^{x_4}=0$. The only nonzero $\Gamma^4{}_{1\lambda}$ is $\Gamma^4{}_{11}=Ha_4's^{1/3}e^{2a_4}$, so $\Gamma^4{}_{1\lambda}\gamma^{x_\lambda}=Ha_4's^{1/3}e^{2a_4}\cdot s^{-1/6}e^{-a_4}\gamma^1=\alpha_1a_4'\gamma^1$. For the commutator we need $[S^{01},\gamma^4]=0$ ($\gamma^4$ anticommutes with both $\gamma^0$ and $\gamma^1$, so it commutes with their product) and $[S^{41},\gamma^4]=\eta^{14}\gamma^4-\eta^{44}\gamma^1=\gamma^1$ (the identity of Section 4.12). With the correct connection,

$$
D_1\gamma^{x_4}=\alpha_1a_4'\gamma^1-\alpha_1\bigl([S^{01},\gamma^4]+a_4'[S^{41},\gamma^4]\bigr)=\alpha_1a_4'\gamma^1-\alpha_1a_4'\gamma^1=0 .
$$

With the notebook's connection the boost term is missing, and

$$
D^{\mathrm{nb}}_1\gamma^{x_4}=\alpha_1a_4'\gamma^1-\alpha_1[S^{01},\gamma^4]=H\,s^{1/6}e^{a_4}a_4'\,\gamma^1\ne0 ,
$$

which is the entry "$(i,4)$" of the table in the Stage-2 document, §8.3 (check `P_gammaConst_notebookContractionClosedForms`).

**What the verifiers measured.** In the primordial field the notebook's contraction violates $D_\mu\gamma^\nu=0$ in 15 of the 64 pairs $(\mu,\nu)$, with 288 nonzero matrix entries; in the generic test geometry G1 it violates it in all 64 pairs, with 4096 nonzero entries. The largest violation is $2/3$, $1/5$ and $9/5$ at the three G2 points and approximately 1.46822, 1.52979 and 1.68937 at the three G1 points. The symmetric part of $\omega_\mu{}^a{}_b$ that the contraction deletes has 12 nonzero entries in G2 and 256 at each G1 point (in G1 every boost pair is populated: 8 values of $\mu$, 16 pairs, 2 orders). Replacing $\Omega$ by $\Omega^{\mathrm{nb}}$ makes all eleven connection-sensitive G2 checks fail, and it breaks local spin invariance already at first order. (Stage 1, Result 5.6; checks `GEO_notebookContractionFails_G1`, `GEO_notebookContractionFails_G2` and `NEG_notebookConnectionDetected_G2`; Stage-2 checks `P_gammaConst_notebookContractionFails` and `P_gammaConst_divergenceIdentityFailsNotebookContraction`; measurements `notebookDGammaMaxAbs`, `notebookDGammaNonzeroEntries` and `nonzeroOmegaMixedSymmetricPart` in `wolfram-geometry-report.json`.)

**The repair.** Lower the index first, $\omega_{\mu ab}=\eta_{ac}\omega_\mu{}^c{}_b$, and contract that with $S^{ab}$. In WolframScript, with the notebook's own names (Stage-1 document, §7.2):

```
(* lowered spin connection omega_{mu ab} = eta_{ac} omega_mu^c_b *)
\[Omega]low = Table[Sum[\[Eta]4488[[a, c]] \[Omega]mat[[\[Alpha]1, c, b]], {c, 1, 8}],
   {\[Alpha]1, 1, 8}, {a, 1, 8}, {b, 1, 8}];
\[CapitalOmega]16[\[Alpha]1_] := (1/2) Sum[\[Omega]low[[\[Alpha]1, a, b]] SAB[[a, b]],
   {a, 1, 8}, {b, 1, 8}];
```

The notebook has two further problems, separate from this one. First, for an anticommuting (Grassmann) field Lg[] carries no dynamics at all, whichever contraction is used (Chapter 5). Second, the extra term $q$ in the field equations that the notebook stores (from its evaluation form La[] with commuting fields, cell 1066) is not caused by the contraction error: with curved gammas that obey the Clifford relation, every $Q_1$ term drops out of those equations, for the notebook's contraction and for the correct one alike (Chapter 9). Chapter 9 shows that the stored $q$ term is reproduced exactly by extra-time curved gammas that violate the Clifford relation; it enters through the spin-connection term, multiplied by the switch $Q_1$. Chapter 9 attributes these non-Clifford gammas to a wrong substitution rule of cell 1058; that attribution is a reconstruction, labelled a HYPOTHESIS in ledger row L20 of Chapter 0, because the notebook does not store the gammas it used and a literal re-execution of cell 1058 gives no $q$ term.

### 4.15 Where the computations live in the repository

**The objects and their checks.** The formulas of Sections 4.4 to 4.14 that the project uses in eight dimensions are verified by exact computer algebra, most of them twice and independently: in Wolfram Language and in Python. (The two-dimensional examples and the Lovelock tensors of orders 2 and 3 are not part of any verifier.) The reports are JSON files; each check is a named entry that is either true or false, and each measurement a named value.

In the list below, "Stage 1" names checks of the arbitrary-field geometry reports and "Stage 2" checks of `wolfram-primordial-report.json`; the numbers in parentheses are the sections of this chapter.

```
metric from the vielbein, det g (4.4, 4.10)
    Stage 1: GEO_frameNondegenerate_G1, GEO_sqrtgSquaredEqualsDetg_G1
    Stage 2: P_metric_vielbeinProduct, P_metric_detG_equals_plus_cos2z
Christoffel symbols (4.5)
    Stage 2: P_christoffel_count, P_christoffel_closedForms512
Riemann tensor, Ricci tensor, R, Einstein tensor (4.7, 4.8)
    Stage 1: GEO_curvature_G1, GEO_curvature_G2
    Stage 2: P_einstein_ricciScalar, P_einstein_GmixedClosedForms, P_einstein_R44
vielbein postulate, spin connection (4.11)
    Stage 1: GEO_vielbeinPostulate_G1, GEO_vielbeinPostulate_G2,
             GEO_omegaAntisymmetry_G1, GEO_omegaAntisymmetry_G2
    Stage 2: P_spinconn_vielbeinPostulate512, P_spinconn_count24,
             P_spinconn_closedForms
spinor connection, gamma^mu Omega_mu (4.12)
    Stage 1: GEO_diagonalSlashFormula_G2, GEO_primordialInvariants_G2
    Stage 2: P_Omega_closedForms, P_Omega_gammaSlash3Hgamma0
covariant constancy of the gammas, divergence identity (4.12)
    Stage 1: GEO_gammaCovariantConstancy_G1, GEO_gammaCovariantConstancy_G2,
             GEO_divergenceIdentity_G1, GEO_divergenceIdentity_G2
    Stage 2: P_gammaConst_DmuGammaNuZero64, P_gammaConst_divergenceIdentity
local spin covariance (4.12)
    Stage 1: LAG_localSpinInvariance_G1, LAG_localSpinInvariance_G2
spinor curvature, Lichnerowicz formula (4.13)
    Stage 1: GEO_curvature_G1, GEO_curvature_G2, GEO_lichnerowicz_G1,
             GEO_lichnerowicz_G2, GEO_lichnerowiczConstantSameG1G2
the notebook's contraction (4.14)
    Stage 1: GEO_notebookContractionFails_G1, GEO_notebookContractionFails_G2,
             NEG_notebookConnectionDetected_G2
    Stage 2: P_gammaConst_notebookContractionFails,
             P_gammaConst_notebookContractionClosedForms
```

The reports, with the number of true checks (Stage-1 document, §11; Stage-2 document, abstract), and the programs that write them:

```
artifacts/dirac16complex/arbitrary-field/
    wolfram-geometry-report.json     43 of 43 true
    python-geometry-report.json      52 of 52 true
artifacts/dirac16complex/primordial-field/
    wolfram-primordial-report.json   126 of 126 true
    python-primordial-report.json    16 of 16 true

Stage 1, Wolfram:  wolfram/Dirac16ComplexGeometry.wl
                   scripts/verify_dirac16complex_geometry.wls
Stage 1, Python:   scripts/d16c_geometry_sympy.py
                   scripts/check_dirac16complex_geometry.py
Stage 2, Wolfram:  wolfram/Dirac16ComplexPrimordial.wl
                   scripts/verify_dirac16complex_primordial.wls
Stage 2, Python:   scripts/check_dirac16complex_primordial.py
```

Chapter 19 gives the commands that rerun them and the lines they print.

**How the Python checker computes the geometry.** The class Geometry in `scripts/d16c_geometry_sympy.py` follows Sections 4.4 to 4.12 line by line. Its arrays are exact "jets": the value and the derivatives of every quantity at one point. The function jein(spec, A, B) is a sum over repeated indices, written in the letter notation of numpy's einsum (for example "rs,smn->rmn" means $\sum_s A_{rs}B_{smn}$). An excerpt of lines 705-735, without the indentation, without three comment lines and without the fourteen lines 719-732 of the anholonomy route mentioned below, and with one comment shortened:

```
self.einv = jinv(e, dom)                                    # [a, mu] = e_a^mu
self.g = jein("mb,nb->mn", jein("ma,ab->mb", e, ETA), e)   # g = e eta e^T
self.ginv = jinv(self.g, dom)
dg = self.g.grad()                                           # [l, m, n] = d_l g_mn
t1 = dg.map(lambda a: np.einsum("mns->smn", a))              # d_m g_ns
t2 = dg.map(lambda a: np.einsum("nms->smn", a))              # d_n g_ms
gam1 = (t1 + t2 - dg).scale(half)                            # Gamma_{s m n}
self.Gamma = jein("rs,smn->rmn", self.ginv, gam1)           # Gamma^r_{mn}
self.de = e.grad()                                           # [m, n, a] = d_m e_n^a
inner = jein("rmn,ra->mna", self.Gamma, e) - self.de
self.omega_mixed = jein("bn,mna->mab", self.einv, inner)    # omega_mu^a_b
self.omega_low = jein("ac,mcb->mab", ETA, self.omega_mixed)  # omega_{mu a b}
self.Omega = jein("mab,abij->mij", self.omega_low, gd.S).scale(half)
self.Omega_nb = jein("mab,abij->mij", self.omega_mixed, gd.S).scale(half)
```

Read it against the formulas: gam1 is $\Gamma_{\sigma\mu\nu}=\tfrac12(\partial_\mu g_{\nu\sigma}+\partial_\nu g_{\mu\sigma}-\partial_\sigma g_{\mu\nu})$, self.Gamma raises its first index, inner is $\Gamma^\rho{}_{\mu\nu}e_\rho{}^a-\partial_\mu e_\nu{}^a$, and self.omega_mixed multiplies by $e_b{}^\nu$: the solution of the vielbein postulate. The last two lines are the correct contraction, with the lowered $\omega_{\mu ab}$, and the notebook's contraction, with the mixed $\omega_\mu{}^a{}_b$; gd.S holds the 64 matrices $S^{ab}$. The same class also computes $\omega$ by a second, independent route from the derivatives of the vielbein alone (the anholonomy route) and compares the two.

**Try it yourself.** The following short program (not part of the repository; it needs Python with sympy, see Chapter 19) computes the Christoffel symbols and the scalar curvature of the primordial metric from the formulas of Sections 4.5 and 4.7. Save it as `curvature.py` and run `python curvature.py`; it takes a few seconds.

```
import sympy as sp

H = sp.symbols("H", positive=True)
x = sp.symbols("x0:8")
a4 = sp.Function("a4")(x[4])        # a4 as a function of x4
z = 6 * H * x[0]
s = sp.sin(z)
third = sp.Rational(1, 3)
g = sp.diag(sp.cot(z)**2, *[s**third * sp.exp(2 * a4)] * 3, -1,
            *[-s**third * sp.exp(-2 * a4)] * 3)
n = 8
gi = g.inv()


def christoffel(r, m, b):           # Gamma^r_{m b}
    total = 0
    for q in range(n):
        total += gi[r, q] * (sp.diff(g[b, q], x[m]) + sp.diff(g[m, q], x[b])
                             - sp.diff(g[m, b], x[q]))
    return sp.simplify(total / 2)


Gam = [[[christoffel(r, m, b) for b in range(n)] for m in range(n)]
       for r in range(n)]
count = sum(1 for r in range(n) for m in range(n) for b in range(n)
            if Gam[r][m][b] != 0)
print("nonzero Christoffel symbols:", count)


def riemann(r, q, m, b):            # R^r_{q m b}
    val = sp.diff(Gam[r][b][q], x[m]) - sp.diff(Gam[r][m][q], x[b])
    val += sum(Gam[r][m][l] * Gam[l][b][q] - Gam[r][b][l] * Gam[l][m][q]
               for l in range(n))
    return val


ricci = [sum(riemann(r, q, r, q) for r in range(n)) for q in range(n)]
R = sum(gi[q, q] * ricci[q] for q in range(n))     # g is diagonal
A1 = sp.Symbol("A1")                # A1 stands for d a4 / d t
zs = sp.Symbol("z", positive=True)
R = R.subs(sp.Derivative(a4, x[4]), H * A1).subs(x[0], zs / (6 * H))
R = sp.simplify(sp.expand_trig(sp.simplify(R)))
print("R =", sp.factor(R))
```

It prints

```
nonzero Christoffel symbols: 37
R = 6*H**2*(A1**2 - 7)
```

that is, 37 nonzero symbols and $R=6H^2(a_4'^2-7)$ (the sum for R uses only the diagonal of $g^{-1}$ because the metric is diagonal). These are the numbers of Sections 4.5 and 4.7; the authoritative values are the ones in the committed reports cited there.

### 4.16 What we proved and what we assumed

**Proved in this chapter** (complete derivations): the transformation rules of vectors, covectors, tensors and the metric, and the invariance of $\sqrt{\lvert g\rvert}\,d^nx$; $\det g=+\cos^2z$ and the constant 7-volume of a comoving region of the primordial field; the transformation rule of the connection coefficients; existence and uniqueness of the Levi-Civita connection (the Christoffel formula); the derivative of a determinant and $\Gamma^\rho{}_{\rho\nu}=\partial_\nu\ln\sqrt{\lvert g\rvert}$; the Christoffel symbols of diagonal metrics and the 37 symbols of the primordial field; the constancy of $g(u,u)$ along geodesics and the complete solution of the geodesic equation in polar coordinates (all values of the constant $L$); the Riemann formula, the symmetries (S1) to (S4), the symmetry of the Ricci tensor, the curvature of the sphere, $R_{44}=-6H^2a_4'^2$ and $G^4{}_4=3H^2(7+a_4'^2)$ in the primordial field (using the quoted $R$); both Bianchi identities and $\nabla_\mu G^\mu{}_\nu=0$; the trace-reversed Einstein equations; the expansion of a 3 by 3 determinant along its first row, $E^{(1)}=G$ and the vanishing of $E^{(k)}$ for $2k+1>n$; the vielbein relations and $\det g=(\det e)^2$ in signature (4,4); the vielbein postulate as a consequence of a natural requirement, its unique solution and the antisymmetry of $\omega_{\mu ab}$; the transformation of $\omega$ under frame rotations; the 24 components of $\omega$ in the primordial field; that the bilinears $\bar\Psi\gamma^a\Phi$ change like the frame components of a vector under $\mathrm{Spin}_0(4,4)$, while an element of Spin(4,4) of spinor norm $-1$ adds a factor $-1$; the spinor connection $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$ as the only traceless solution of its defining property; local spin covariance; $D_\mu\gamma^\nu=0$ and its equivalence with the vielbein postulate; the divergence identity; the formula for $\gamma^\mu\Omega_\mu$ with a diagonal vielbein and $\gamma^\mu\Omega_\mu=3H\gamma^0$ in the primordial field; $F_{\mu\nu}=\tfrac12R_{ab\mu\nu}S^{ab}$; the Lichnerowicz formula with the constant $-\tfrac14$; and the analysis of the notebook's contraction (it deletes the 16 boost components, reverses the 6 time-time components, and gives $\gamma^\mu\Omega^{\mathrm{nb}}_\mu=\tfrac{3H}2(\gamma^0+a_4'\gamma^4)$ and $D^{\mathrm{nb}}_1\gamma^{x_4}\ne0$ in the primordial field).

**Computed by the verifiers and quoted here:** the full scalar curvature $R=6H^2(a_4'^2-7)$ and the other components of the Einstein tensor of the primordial field, and all numbers at the test points (counts of nonzero components, curvature values, sizes of the violations), each with its report and check.

**Assumed or quoted without proof:** that spacetime is a smooth manifold with a smooth metric of signature (4,4) and admits a spin structure (Stage 1, §4.5, assumes the latter); the standard theorems we named (Sylvester's law of inertia, the change-of-variables rule for integrals, the inverse function theorem, the flatness theorem, the local existence of orthonormal frames and of smooth spin coverings of frame rotations, Newton's limit of Einstein's equations, the Gauss-Bonnet expansion, and Lovelock's theorem, together with the fact that $E^{(2)}$ and $E^{(3)}$ do not vanish identically in eight dimensions); the facts (F1) to (F3) about the gamma matrices, Theorems 2.8 and 2.9, the identity $R^TCR=C$ for one exponential $\exp(\theta S^{ab})$, and the determinant 1 of the elements of Pin(4,4) as 16 by 16 matrices, all of which Chapter 2 proves; and two choices of the project: the connection is the torsion-free Levi-Civita connection, and the law of gravity is the 8-dimensional Einstein equation $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ without the Lovelock terms of order 2 and 3, which neither the notebook nor the project computes. The Stage-1 test-point checks do not replace the general proofs: they test them exactly at three points of one generic vielbein, in the primordial family and in homogeneous frames, not symbolically for every vielbein (Stage-1 document, §13, limitation 1).

### 4.17 Exercises

**Exercise 4.1.** *The polar plane.* (a) Write down $g^{\mu\nu}$ for $ds^2=dr^2+r^2d\varphi^2$. (b) The length of a curve is $\int\sqrt{g_{\mu\nu}u^\mu u^\nu}\,d\lambda$. Compute the length of the circle $r=2$, $\varphi=\lambda$, $0\le\lambda\le2\pi$. (c) Lower the index of the constant field $V^r=\cos\varphi$, $V^\varphi=-\sin\varphi/r$ and check that $g(V,V)=1$.

**Exercise 4.2.** *Geodesics of the sphere.* (a) With the Christoffel symbols of the sphere (Section 4.7), write the two geodesic equations. (b) Show that the equator, $\theta=\pi/2$, $\varphi=\lambda/a$, is a geodesic, and compute $g(u,u)$. (c) Show that the circle of latitude $\theta=\pi/3$, traversed as $\varphi=\lambda/(a\sin(\pi/3))$, is not a geodesic.

**Exercise 4.3.** *Freely falling observers in the primordial field.* Show that for every constant $c^0,\dots,c^3,c^5,\dots,c^7$ and every function $a_4$, the curve $x^\mu(\lambda)=(c^0,c^1,c^2,c^3,\lambda,c^5,c^6,c^7)$ is a geodesic of the primordial field, and compute $g(u,u)$.

**Exercise 4.4.** *A space of constant negative curvature.* Take the two-dimensional metric $ds^2=dy^2+e^{2Hy}dw^2$ with coordinates $(y,w)$ and a constant $H>0$. Compute its Christoffel symbols, $R^y{}_{wyw}$, the Ricci tensor and the scalar curvature.

**Exercise 4.5.** *The static primordial field.* Put $a_4$ equal to a constant. Using the formulas of Sections 4.7 and 4.8, compute $R$, $G^\mu{}_\nu$, the required energy density $\rho_{\mathrm{req}}$, the required pressures and $w=p/\rho$.

**Exercise 4.6.** *Einstein's tensor in two dimensions.* (a) Show that $G_{\mu\nu}=0$ for the sphere. (b) Explain why $G_{\mu\nu}=0$ for every two-dimensional metric.

**Exercise 4.7.** *Lovelock orders.* For $n=4,5,6,8,10$, list the orders $k$ that can contribute, that is, the orders for which $E^{(k)}$ is not identically zero. Compare with the notebook's rule "m-1 = n/2 - 1" for the highest order in even dimension $n$.

**Exercise 4.8.** *A spinor in the polar frame.* In the plane, use $\gamma^0=\sigma_1$, $\gamma^1=\sigma_2$ in every orthonormal frame. In the Cartesian frame $\Omega=0$. The polar frame is the Cartesian frame turned by the angle $\varphi$. Let $R(\varphi)=\exp(i\varphi\sigma_3/2)$. (a) Show that $R=\mathrm{diag}(e^{i\varphi/2},e^{-i\varphi/2})$ and $R\,(\cos\varphi\,\sigma_1+\sin\varphi\,\sigma_2)\,R^{-1}=\sigma_1$. (The left side contains the curved gamma $\gamma^r$ built with the Cartesian frame.) (b) Show that $-(\partial_\varphi R)R^{-1}$ is the spinor connection $\Omega_\varphi$ of Section 4.12. (c) Compute $R(2\pi)$ and interpret it. (d) Where does the term $1/(2r)$ in the polar Dirac operator come from?

**Exercise 4.9.** *Homogeneous frames.* For $ds^2=-dt^2+\sum_{j\ne4}\eta_{jj}h_j(t)^2(dx^j)^2$ with $t=x^4$, show that $\gamma^\mu\Omega_\mu=\tfrac12\Theta\gamma^4$ with $\Theta=\sum_{j\ne4}\dot h_j/h_j$, where a dot is $d/dt$.

**Exercise 4.10.** *Counting what the notebook deletes.* (a) In signature (4,4), how many of the 28 pairs $a<b$ are space-space, time-time and boost pairs? (b) The same question in four dimensions with three space directions and one time direction. (c) For a generic vielbein in eight dimensions, how many nonzero entries does the symmetric part of $\omega_\mu{}^a{}_b$ have, and how many nonzero components does $\omega_{\mu ab}$ have? Compare with the G1 measurements of Section 4.14.

**Exercise 4.11.** *The notebook's contraction at a test point.* At the first G2 test point of Stage 1, $H=2/3$ and $a_4'=3/7$. Compute $\gamma^\mu\Omega_\mu$, $\gamma^\mu\Omega^{\mathrm{nb}}_\mu$, and $D_5\gamma^{x_5}$ with both connections.

**Exercise 4.12.** *A consistency check with a trace.* (a) Show that in $n=8$ dimensions $G^\mu{}_\mu=-3R$. (b) Check this for the primordial field with $a_4=t$, using the values of Section 4.8.

### 4.18 Answers to the exercises

**Answer 4.1.** (a) The inverse of a diagonal matrix is diagonal with the reciprocal entries: $g^{rr}=1$, $g^{\varphi\varphi}=1/r^2$, $g^{r\varphi}=0$. (b) Along the circle $u^r=0$ and $u^\varphi=1$, so $\sqrt{g_{\varphi\varphi}}=r=2$ and the length is $\int_0^{2\pi}2\,d\lambda=4\pi$. (c) $V_r=g_{rr}V^r=\cos\varphi$ and $V_\varphi=g_{\varphi\varphi}V^\varphi=r^2(-\sin\varphi/r)=-r\sin\varphi$. Then $g(V,V)=V^rV_r+V^\varphi V_\varphi=\cos^2\varphi+(-\sin\varphi/r)(-r\sin\varphi)=\cos^2\varphi+\sin^2\varphi=1$.

**Answer 4.2.** (a) With $\Gamma^\theta{}_{\varphi\varphi}=-\sin\theta\cos\theta$ and $\Gamma^\varphi{}_{\theta\varphi}=\Gamma^\varphi{}_{\varphi\theta}=\cot\theta$ (primes are $d/d\lambda$): $\theta''-\sin\theta\cos\theta\,\varphi'^2=0$ and $\varphi''+2\cot\theta\,\theta'\varphi'=0$. (b) On the equator $\theta'=\theta''=0$, $\varphi'=1/a$ and $\varphi''=0$. The first equation holds because $\cos(\pi/2)=0$; the second because $\theta'=0$. $g(u,u)=a^2(\theta'^2+\sin^2\theta\,\varphi'^2)=a^2\cdot\frac1{a^2}=1$. (c) Now $\theta'=\theta''=0$ and $\varphi'=\frac{1}{a\sin(\pi/3)}=\frac{2}{\sqrt3\,a}$, so $\varphi'^2=\frac{4}{3a^2}$, while $\sin\theta\cos\theta=\frac{\sqrt3}2\cdot\frac12=\frac{\sqrt3}4$. The first equation gives $0-\frac{\sqrt3}{4}\cdot\frac{4}{3a^2}=-\frac{1}{\sqrt3\,a^2}\ne0$. Circles of latitude other than the equator are not geodesics; the geodesics of the sphere are its great circles, which is why long-distance flights do not follow lines of constant latitude.

**Answer 4.3.** The velocity is $u^\mu=\delta^\mu{}_4$ (only $u^4=1$), so $du^\mu/d\lambda=0$ and the geodesic equation reduces to $\Gamma^\mu{}_{44}=0$ for every $\mu$. By the diagonal formulas of Section 4.5: $\Gamma^4{}_{44}=\partial_4\ln h_4=0$ because $h_4=1$, and for $\mu\ne4$, $\Gamma^\mu{}_{44}=-\eta_{\mu\mu}\eta_{44}\frac{h_4}{h_\mu^2}\partial_\mu h_4=0$, again because $h_4=1$ is constant. (The table of the 37 symbols contains no symbol with the lower pair $(4,4)$.) So the curve is a geodesic for every $a_4$, and $g(u,u)=g_{44}=-1$: it is time-like, and by the definition of proper time in Section 4.6, $\tau=\int\sqrt{-g_{44}}\,d\lambda=\lambda=x^4$ (counted from $x^4=0$) is its proper time.

**Answer 4.4.** Here $h_y=1$ and $h_w=e^{Hy}$, both signs $+1$. By the diagonal formulas: $\Gamma^w{}_{yw}=\Gamma^w{}_{wy}=\partial_y\ln e^{Hy}=H$ and $\Gamma^y{}_{ww}=-\frac{h_w}{h_y^2}\partial_yh_w=-He^{2Hy}$; all others vanish (in particular $\Gamma^\lambda{}_{yy}=0$). Then

$$
R^y{}_{wyw}=\partial_y\Gamma^y{}_{ww}-\partial_w\Gamma^y{}_{yw}+\Gamma^y{}_{y\lambda}\Gamma^\lambda{}_{ww}-\Gamma^y{}_{w\lambda}\Gamma^\lambda{}_{yw}=-2H^2e^{2Hy}-0+0-(-He^{2Hy})H=-H^2e^{2Hy}.
$$

So $R_{ww}=R^y{}_{wyw}=-H^2e^{2Hy}$. For $R_{yy}=R^w{}_{ywy}=\partial_w\Gamma^w{}_{yy}-\partial_y\Gamma^w{}_{wy}+\Gamma^w{}_{w\lambda}\Gamma^\lambda{}_{yy}-\Gamma^w{}_{y\lambda}\Gamma^\lambda{}_{wy}=0-0+0-H\cdot H=-H^2$. $R_{yw}=0$. Finally $R=g^{yy}R_{yy}+g^{ww}R_{ww}=-H^2+e^{-2Hy}(-H^2e^{2Hy})=-2H^2$: constant and negative, a space of constant negative curvature (the hyperbolic plane). The warped form of the primordial field (Section 4.4) has the same kind of warp factor, $e^{2H\zeta}$, in each of its six transverse directions.

**Answer 4.5.** With $a_4'=a_4''=0$: $R=6H^2(0-7)=-42H^2$; $G^0{}_0=-3H^2(0-5)=15H^2$, $G^i{}_i=15H^2$, $G^4{}_4=21H^2$, $G^j{}_j=15H^2$, so $G^\mu{}_\nu=\mathrm{diag}(15,15,15,15,21,15,15,15)\,H^2$. The required source has $\rho_{\mathrm{req}}=-G^4{}_4/\kappa=-21H^2/\kappa$ and the equal pressures $p=15H^2/\kappa$ in all seven transverse directions, so $w=-15/21=-5/7$. These are the values of the Stage-4 exact theory for the static field (checks `KS_geometry_ricciScalarMinus42H2`, `KS_geometry_einsteinMixedDiag` and `KS_geometry_requiredSource` in `artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json`; `handoff/specs/STAGE4_SPEC.md`, erratum E4.3, for the sign of $p$), and $w=-5/7$ is the value of the Stage-2 formula $w=(c^2-5)/(c^2+7)$ at $c=0$ (Stage-2 document, §15.4).

**Answer 4.6.** (a) $G_{\theta\theta}=R_{\theta\theta}-\tfrac12g_{\theta\theta}R=1-\tfrac12a^2\cdot\tfrac2{a^2}=0$, $G_{\varphi\varphi}=\sin^2\theta-\tfrac12a^2\sin^2\theta\cdot\tfrac{2}{a^2}=0$ and $G_{\theta\varphi}=0$. (b) By Section 4.9, $G^\mu{}_\nu=E^{(1)\mu}{}_\nu$ is a contraction of the generalized delta with $2k+1=3$ upper indices. In two dimensions each index takes only two values, so two of the three upper indices are always equal and the delta vanishes. Hence $G_{\mu\nu}=0$ for every two-dimensional metric, and Einstein's equations in two dimensions would force $T_{\mu\nu}=0$.

**Answer 4.7.** $E^{(k)}$ vanishes identically when $2k+1>n$ (that the lower orders do not vanish identically is quoted, Section 4.9). So: $n=4$: $k=0,1$; $n=5$: $k=0,1,2$; $n=6$: $k=0,1,2$; $n=8$: $k=0,1,2,3$; $n=10$: $k=0,\dots,4$. For even $n$ the highest order is $n/2-1$: 1, 2, 3 and 4 for $n=4,6,8,10$, in agreement with the notebook's rule ($m=n/2$).

**Answer 4.8.** (a) $\sigma_3^2=1$, so the exponential series splits into even and odd powers: $\exp(i\varphi\sigma_3/2)=\cos(\varphi/2)+i\sigma_3\sin(\varphi/2)=\mathrm{diag}(e^{i\varphi/2},e^{-i\varphi/2})$. Since $\sigma_3$ anticommutes with $\sigma_1$ and $\sigma_2$, moving $\sigma_1$ through $R$ reverses the sign of the exponent: $R\sigma_1=\sigma_1R^{-1}$. Hence $R\sigma_1R^{-1}=\sigma_1R^{-2}=\sigma_1(\cos\varphi-i\sigma_3\sin\varphi)=\cos\varphi\,\sigma_1-\sin\varphi\,\sigma_2$, using $\sigma_1\sigma_3=-i\sigma_2$. In the same way $R\sigma_2R^{-1}=\sigma_2(\cos\varphi-i\sigma_3\sin\varphi)=\cos\varphi\,\sigma_2+\sin\varphi\,\sigma_1$, using $\sigma_2\sigma_3=i\sigma_1$. Therefore $R(\cos\varphi\,\sigma_1+\sin\varphi\,\sigma_2)R^{-1}=(\cos^2\varphi+\sin^2\varphi)\sigma_1+(-\cos\varphi\sin\varphi+\sin\varphi\cos\varphi)\sigma_2=\sigma_1$: the curved gamma $\gamma^r$ of the Cartesian frame, transformed with $R$, is the curved gamma $\gamma^r=\sigma_1$ of the polar frame, as the covariance theorem of Section 4.12 requires. (b) $\partial_\varphi R=\tfrac i2\sigma_3R$, so $-(\partial_\varphi R)R^{-1}=-\tfrac i2\sigma_3$, which is $\Omega_\varphi$ of Section 4.12. By the covariance theorem the polar connection is $R\cdot0\cdot R^{-1}-(\partial_\varphi R)R^{-1}$, and the two computations agree. (c) $R(2\pi)=\mathrm{diag}(e^{i\pi},e^{-i\pi})=-1$. After one full turn around the origin the polar frame is back where it started, but the spin transformation that connects it with the Cartesian frame has become $-1$. So the polar-frame components $R\Psi$ of a smooth spinor field change sign after a full turn. This is the sign of Chapter 2: a rotation by $2\pi$ acts on spinors as $-1$. (d) From $\gamma^\varphi\Omega_\varphi=\frac{\sigma_2}{r}\bigl(-\frac i2\sigma_3\bigr)=\frac{1}{2r}\sigma_1$: it is the spinor connection of the turning polar frame. By covariance, $\gamma^\mu D_\mu(R\Psi)=R\,(\sigma_1\partial_x+\sigma_2\partial_y)\Psi$, so the term $1/(2r)$ is exactly what is needed for the polar form to describe the same flat-space Dirac operator.

**Answer 4.9.** Use the diagonal formula of Section 4.12. The scale factors depend on $t=x^4$ only, so only $b=4$ contributes; $h_4=1$, and $\prod_{c\ne4}h_c=V$ is the 7-volume of a comoving region with unit coordinate ranges (Section 4.4: here the 7 by 7 block is diagonal with the entries $\eta_{jj}h_j^2$, so the square root of the absolute value of its determinant is $V$). So $\gamma^\mu\Omega_\mu=\tfrac12\,\partial_t\ln V\,\gamma^4=\tfrac12\sum_{j\ne4}\frac{\dot h_j}{h_j}\,\gamma^4=\tfrac12\Theta\gamma^4$. This is the one line of geometry that the Stage-3 experiments EXP-2 to EXP-5 need (student guide, §6.6; check `GEO_diagonalSlashFormula_G3` in `python-geometry-report.json`).

**Answer 4.10.** (a) Space-space: choose 2 of the 4 space-like directions, $\binom42=6$; time-time: likewise 6; boost pairs: $4\times4=16$; total $6+6+16=28$. (b) With three space directions and one time direction: space-space $\binom32=3$, time-time 0, boosts $3\times1=3$. The same mistake in ordinary four-dimensional spacetime would delete all three boost components of the connection. (c) The symmetric part of $\omega_\mu{}^a{}_b$ is the boost part: for each of the 8 values of $\mu$, 16 pairs in 2 orders, $8\times16\times2=256$ entries. $\omega_{\mu ab}$ has, for each $\mu$, $8\times7=56$ ordered pairs with $a\ne b$, in total $8\times56=448$. Both numbers are exactly the measurements `nonzeroOmegaMixedSymmetricPart` = 256 and `nonzeroOmegaLower` = 448 at each G1 point in `wolfram-geometry-report.json`: the generic vielbein G1 populates every component.

**Answer 4.11.** Correct: $\gamma^\mu\Omega_\mu=3H\gamma^0=2\gamma^0$. Notebook: $\tfrac{3H}{2}(\gamma^0+a_4'\gamma^4)=\gamma^0+\tfrac37\gamma^4$, the value `G2.p1.notebookSlash` of `wolfram-geometry-report.json`. For $D_5\gamma^{x_5}$: $\gamma^{x_5}=\gamma^5/h_5$ does not depend on $x^5$, so $\partial_5\gamma^{x_5}=0$. The nonzero $\Gamma^5{}_{5\lambda}$ are $\Gamma^5{}_{50}=H\cot z$ and $\Gamma^5{}_{54}=-Ha_4'$, so $\Gamma^5{}_{5\lambda}\gamma^{x_\lambda}=H\cot z\tan z\,\gamma^0-Ha_4'\gamma^4=H\gamma^0-Ha_4'\gamma^4$. With the identity of Section 4.12, $[S^{05},\gamma^5]=\eta^{55}\gamma^0-\eta^{05}\gamma^5=-\gamma^0$ and $[S^{45},\gamma^5]=\eta^{55}\gamma^4-\eta^{45}\gamma^5=-\gamma^4$. With $\Omega_5=\alpha_5(S^{05}-a_4'S^{45})$ and $\alpha_5/h_5=H$: $[\Omega_5,\gamma^{x_5}]=H(-\gamma^0+a_4'\gamma^4)$, and $D_5\gamma^{x_5}=0$. With $\Omega^{\mathrm{nb}}_5=\alpha_5a_4'S^{45}$: $[\Omega^{\mathrm{nb}}_5,\gamma^{x_5}]=-Ha_4'\gamma^4$, and $D^{\mathrm{nb}}_5\gamma^{x_5}=H\gamma^0-2Ha_4'\gamma^4=\tfrac23\gamma^0-\tfrac47\gamma^4$. This is the entry "$(j,j)$" of the table of the Stage-2 document, §8.3.

**Answer 4.12.** (a) $G^\mu{}_\mu=R^\mu{}_\mu-\tfrac12\delta^\mu{}_\mu R=R-\tfrac82R=-3R$. (b) With $a_4=t$, $G^\mu{}_\mu=(7\cdot12+24)H^2=108H^2$ and $-3R=-3(-36H^2)=108H^2$. The two values of Section 4.8 are consistent.
