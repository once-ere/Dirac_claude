## 1. Mathematics from zero I: numbers, complex numbers, vectors, matrices, indices, determinants, the generalized Kronecker delta

This chapter builds, from school algebra, every piece of algebra that the rest of the course uses: exact and rounded numbers, powers and the exponential function, complex numbers, vectors and matrices, determinants, index notation with the summation convention, eigenvalues and the signature of a metric, and the generalized Kronecker delta with which the field equations of gravity are written. Every idea is put to work in a Jupyter notebook, and every notebook is applied to the objects of the author's theory as soon as possible.

### 1.1 What this chapter is for

**Why so much algebra.** The theory of this course lives in a universe with eight directions. The author names them $x_1, \dots, x_8$: the three directions $x_1, x_2, x_3$ of ordinary space, the time $x_4$, three further time-like directions $x_5, x_6, x_7$, called the **extra times**, and a hidden space direction $x_8$. The geometry of this universe is described by the author's **metric**, a list of eight expressions, one for each direction, which says how long a small step along that direction is (the word is explained fully in Section 1.5 and Section 1.1):

$$
g = \mathrm{diag}\big(e^{2a_4} s,\ e^{2a_4} s,\ e^{2a_4} s,\ -1,\ -e^{-2a_4} s,\ -e^{-2a_4} s,\ -e^{-2a_4} s,\ \cot^2 z\big),\qquad s = \sin^{1/3} z,\qquad z = 6 H x_8 .
$$

Here $H$ is a positive constant of the author's, $z = 6Hx_8$ lies between $0$ and $\pi/2$, and $a_4$ is a function of the time $x_4$; as $a_4$ grows, the entries of space grow like $e^{2a_4}$ and the entries of the three extra times shrink like $e^{-2a_4}$: space inflates and the extra times **deflate exponentially**. To read this one line you need powers, roots, the exponential function, the trigonometric functions and the idea of a list of numbers with a sign attached to each entry. The fields of the theory have sixteen complex components at every point, and they are acted on by eight real $16 \times 16$ matrices, the **gamma matrices**. To compute with them you need complex numbers, matrices and their products, determinants, eigenvalues, and a compact notation, index notation, in which one short line stands for dozens of equations. Finally the field equations of gravity in eight dimensions (Chapter 11) are written with the **generalized Kronecker delta**, a determinant of zeros and ones. This chapter teaches all of it.

**The seven notebooks.** The chapter has seven worked examples, each a complete Jupyter notebook, taken in this order:

| notebook | topic | sections |
| --- | --- | --- |
| 01f | whole numbers, fractions, real and floating-point numbers, powers, exponential, logarithm | Sections 1.2 to 1.9 |
| 01b | complex numbers, Euler's formula, rotations, boosts, oscillation and growth | Sections 1.1 to 1.1 |
| 01a | vectors, matrices, permutations, determinants, the gamma matrices and the metric | Sections 1.1 to 1.1 |
| 01e | index notation, the summation convention, the frame metric, the Clifford relation | Sections 1.1 to 1.1 |
| 01g | eigenvalues, eigenvectors, the signature (4,4), Sylvester's law | Sections 1.1 to 1.1 |
| 01c | the generalized Kronecker delta, its proof, its counts, its contractions | Sections 1.1 to 1.1 |
| 01d | reproducing the record's tests of the generalized delta exactly | Sections 1.1 to 1.1 |

Each notebook appears in three parts: a section "How to run Notebook 01x", which gives the complete instructions for running it on Windows, macOS or Linux; a section "Notebook 01x: complete text", which prints every cell, everything it printed and every figure it drew; and a section "Line-by-line walk-through of Notebook 01x", which explains every line of every code cell. The first code cell of every notebook, the **set-up cell**, is the same in all notebooks except for the notebook's name; it is explained line by line once, in Section 1.9, and the later walk-throughs refer back to that explanation.

**Counting from 1 and from 0.** In mathematics the rows and columns of a table are numbered $1, 2, 3, \dots$, and the author numbers his coordinates $x_1$ to $x_8$. The programming language Python numbers the entries of a list $0, 1, 2, \dots$. So the coordinate $x_1$ is entry 0 of a Python list, $x_8$ is entry 7, and the entry in row 1 and column 1 of a matrix `A` is `A[0, 0]`. Every walk-through says which numbering a line uses.

**The labels of every statement.** Every result in this chapter carries one of the labels of the book: PROVED (an exact derivation is written out here, line by line, and a notebook checks it), COMPUTED (a number found by a notebook, with the cell that prints it), ASSUMED (a standard fact used without proof here, said so where it is used). When a notebook reproduces a number of the **Revision record** (the folder Revision of the repository, in which every computation of the author's theory is done and checked), the text names the record file and the check, exactly as the notebook's PASS line does. Nothing in this chapter concerns pair creation or matter and antimatter; those questions are treated, with the exact scope of what is proved, in Chapters 18 to 21.

### 1.2 Whole numbers and fractions, exactly

**Whole numbers.** The **whole numbers** (or **integers**) are $\dots, -2, -1, 0, 1, 2, \dots$. Python computes with them exactly, however many digits they have: $2^{100} = 1267650600228229401496703205376$ has 31 digits, and every one of them is right. Another large whole number that the course meets is

$$
16! = 1 \cdot 2 \cdot 3 \cdots 16 = 20922789888000 ,
$$

the number of terms of the determinant of a $16 \times 16$ matrix (Section 1.1). The symbol $n!$, read "$n$ factorial", is the product of the whole numbers from 1 to $n$, with $0! = 1$.

**Fractions.** A **fraction** (or **rational number**) is a quotient $p/q$ of two whole numbers with $q \neq 0$. The same fraction has many spellings, $1/2 = 2/4 = 3/6$, because multiplying numerator and denominator by the same number does not change the quotient. The spelling is in **lowest terms** when $p$ and $q$ have no common factor larger than 1. The **greatest common divisor** $\gcd(p, q)$ is the largest whole number that divides both; dividing $p$ and $q$ by it gives the lowest terms. For $84/126$:

$$
84 = 2 \cdot 42,\qquad 126 = 3 \cdot 42,\qquad\text{so}\qquad \frac{84}{126} = \frac{84/42}{126/42} = \frac{2}{3}
$$

(the first two equations factor out 42, which is $\gcd(84, 126)$ because 2 and 3 have no common factor; the third divides numerator and denominator by 42). Two fractions are added by bringing them to a common denominator:

$$
\frac13 + \frac16 = \frac26 + \frac16 = \frac36 = \frac12
$$

(first $1/3$ is written with the denominator 6 by multiplying numerator and denominator by 2; then the numerators are added over the common denominator; then the common factor 3 of 3 and 6 is cancelled). Python's module `fractions` computes with fractions exactly in this way, and Notebook 01f, In [2], checks these three examples.

**Long division.** The decimal digits of a fraction $p/q$ with $0 < p < q$ are produced by the school method of long division. Start with the **remainder** $r = p$. At every step multiply the remainder by 10; the whole part of the division of $10r$ by $q$ is the next digit, and what is left over is the new remainder. For $1/7$:

$$
10 = 1 \cdot 7 + 3,\quad 30 = 4 \cdot 7 + 2,\quad 20 = 2 \cdot 7 + 6,\quad 60 = 8 \cdot 7 + 4,\quad 40 = 5 \cdot 7 + 5,\quad 50 = 7 \cdot 7 + 1 .
$$

The digits are 1, 4, 2, 8, 5, 7, and the last remainder is 1, the remainder we started with. From here everything repeats, so $1/7 = 0.142857142857\dots$, written $0.(142857)$: the block in brackets repeats for ever. The length of the repeating block is the **period**; for $1/7$ it is 6.

**Theorem (PROVED).** The decimal digits of a fraction $p/q$ either end or, from some place on, repeat a block of at most $q - 1$ digits. *Proof.* Every remainder is one of the numbers $0, 1, \dots, q - 1$, because a remainder after division by $q$ is smaller than $q$. If a remainder is 0, the division ends: every further digit is 0. Otherwise every remainder is one of the $q - 1$ numbers $1, \dots, q - 1$. Among the first $q$ remainders two must therefore be equal (there are only $q - 1$ different values for $q$ remainders). Each step computes the next digit and remainder from the present remainder alone, so as soon as a remainder comes back, the digits from there on repeat the digits after its first appearance. The block between two equal remainders is at most $q - 1$ steps long.

**From the digits back to the fraction (PROVED).** Let $x = 0.(c_1 \dots c_m)$ be a repeating block of $m$ digits, and let $C$ be the whole number with the digits $c_1 \dots c_m$. Then

$$
10^m x = c_1 \dots c_m . (c_1 \dots c_m) = C + x
$$

(multiplying by $10^m$ moves the decimal point $m$ places to the right, so the first block stands before the point and the same repeating digits follow it),

$$
10^m x - x = C,\qquad x = \frac{C}{10^m - 1}
$$

(subtract $x$ from both sides; then take out the factor $x$ and divide by $10^m - 1$). For example $0.(142857) = 142857/999999 = 1/7$, because $7 \cdot 142857 = 999999$. If $k$ digits $d_1 \dots d_k$ (the whole number $D$) come before the repeating block, they are worth $D/10^k$, and the block is shifted $k$ places further right, which divides its value by $10^k$:

$$
0.d_1 \dots d_k (c_1 \dots c_m) = \frac{D}{10^k} + \frac{C}{10^k (10^m - 1)} .
$$

For example $5/12 = 0.41(6)$: $D = 41$, $k = 2$, $C = 6$, $m = 1$, and $41/100 + 6/(100 \cdot 9) = 369/900 + 6/900 = 375/900 = 5/12$. Notebook 01f, In [3], writes long division as a Python function and checks this formula on six fractions.

**Which fractions end (PROVED, using one ASSUMED fact).** A fraction $p/q$ in lowest terms has a decimal expansion that ends exactly when $q$ has no prime factor other than 2 and 5, that is $q = 2^a 5^b$. (A **prime number** is a whole number larger than 1 that only 1 and itself divide.) *Proof.* If $q = 2^a 5^b$ and $k$ is the larger of $a$ and $b$, then $10^k = 2^k 5^k$ is a multiple of $q$, say $10^k = q t$, and $p/q = pt/10^k$: a whole number divided by $10^k$, which has at most $k$ digits after the point. Conversely, if the digits end after $k$ places, then $p/q = N/10^k$ for a whole number $N$, so $p \cdot 10^k = N q$; $q$ divides $p \cdot 10^k$ and has no common factor with $p$, so it divides $10^k = 2^k 5^k$, and its prime factors are among 2 and 5. The last step uses the uniqueness of the factorisation of a whole number into primes, a standard theorem of arithmetic that we use without proof (ASSUMED). Notebook 01f, In [4], computes the period of $1/q$ for every $q$ from 2 to 300 and checks the theorem and the bound $q - 1$; 23 denominators reach the full period $q - 1$, the first of them 7, 17, 19, 23, 29, 47, 59, 61, 97 (COMPUTED).

### 1.3 Real numbers: the square root of 2 is not a fraction

The number line contains numbers that are not fractions. The most famous is $\sqrt 2$, the positive number whose square is 2, the length of the diagonal of a square with side 1.

**Theorem (PROVED).** No fraction $p/q$ has $(p/q)^2 = 2$. *Proof by contradiction.* Suppose $p/q$ is in lowest terms and $p^2/q^2 = 2$. Then:

- $p^2 = 2q^2$ (multiply both sides by $q^2$), so $p^2$ is even;
- $p$ is even, because the square of an odd number is odd: $(2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$ (multiply out; then take out the factor 2 from the first two terms); so $p = 2r$ for a whole number $r$;
- $(2r)^2 = 2q^2$, that is $4r^2 = 2q^2$, that is $q^2 = 2r^2$ (insert $p = 2r$; then divide by 2), so $q^2$ is even and, by the same argument, $q$ is even;
- so 2 divides both $p$ and $q$, and $p/q$ was not in lowest terms after all.

The assumption led to a contradiction, so it is false: $\sqrt 2$ is not a fraction. A number that is not a fraction is called **irrational**; its decimal digits never end and never repeat (by the formula of Section 1.2, a number whose digits end or repeat is a fraction). The **real numbers** are all the numbers of the number line, fractions and irrational numbers together.

**Fractions that come close (PROVED).** Start with $1/1$ and make new fractions by the rule $p' = p + 2q$, $q' = p + q$: this gives $3/2$, $7/5$, $17/12$, $41/29$, $99/70$, and so on. For each of them $p^2 - 2q^2$ is $+1$ or $-1$:

$$
p'^2 - 2q'^2 = (p + 2q)^2 - 2(p + q)^2 = p^2 + 4pq + 4q^2 - 2p^2 - 4pq - 2q^2 = -(p^2 - 2q^2)
$$

(insert the rule; multiply out both squares, $(u + v)^2 = u^2 + 2uv + v^2$; collect the terms: $4pq - 4pq = 0$, $p^2 - 2p^2 = -p^2$, $4q^2 - 2q^2 = 2q^2$). Every step changes the sign, and $1^2 - 2 \cdot 1^2 = -1$, so the values are $-1, +1, -1, \dots$. How far is $p/q$ from $\sqrt 2$? Multiply the difference by $p + q\sqrt 2$:

$$
\Big(\frac pq - \sqrt 2\Big)(p + q\sqrt 2) = \frac{p^2 + pq\sqrt 2 - pq\sqrt 2 - 2q^2}{q} = \frac{p^2 - 2q^2}{q},\qquad\text{so}\qquad \frac pq - \sqrt 2 = \frac{p^2 - 2q^2}{q(p + q\sqrt 2)}
$$

(multiply out the product; the middle terms cancel; then divide by $p + q\sqrt 2$). With $p^2 - 2q^2 = \pm 1$ and $p \approx q\sqrt 2$ the size of the error is about $1/(q \cdot 2q\sqrt 2) = 1/(2\sqrt 2\, q^2) \approx 0.35355/q^2$. Notebook 01f, In [5], computes twelve of these fractions with 50-digit arithmetic: for $19601/13860$ the error is $1.84 \times 10^{-9}$, and the error times $q^2$ is 0.353553 (COMPUTED). It also checks with exact whole numbers that $p^2 = 2q^2$ has no solution with $q \le 10000$.

**Bisection.** A real number can be pinned down by fractions alone. Because $1^2 < 2 < 2^2$, $\sqrt 2$ lies between 1 and 2. Take the middle $m$ of the interval: if $m^2 < 2$, the root lies in the right half, otherwise in the left half. Each step halves the width of the interval while both ends stay exact fractions; after 60 steps the width is $2^{-60} \approx 8.7 \times 10^{-19}$. This is **bisection**. Notebook 01f, In [6], finds $1.4142135623730950483 < \sqrt 2 < 1.4142135623730950492$ in this way (COMPUTED).

### 1.4 Floating-point numbers, rounding and cancellation

**How a computer stores a real number.** A computer does not store real numbers with infinitely many digits. It stores a **floating-point number**: a whole number $m$ of at most 53 binary digits (**bits**, the digits 0 and 1 of the base-2 system) times a power of two, $m \cdot 2^k$. Python's `float` and numpy's arrays use these numbers. A fraction whose denominator is a power of 2, such as $0.5 = 1/2$ or $0.375 = 3/8$, is stored exactly. A fraction such as $0.1 = 1/10$, whose denominator contains the prime factor 5, has an endless expansion in base 2 (by the argument of Section 1.2 with 2 in place of 10), so it is **rounded** to the nearest floating-point number. Notebook 01f, In [7], reads out the stored value: $0.1$ is stored as $3602879701896397/36028797018963968$, a fraction with the denominator $2^{55}$, slightly larger than $1/10$. That is why $0.1 + 0.2$ prints as 0.30000000000000004 and is not equal to the stored $0.3$.

**Machine epsilon.** The step from 1 to the next floating-point number is

$$
\varepsilon = 2^{-52} \approx 2.220446049250313 \times 10^{-16},
$$

called **machine epsilon**. So $1 + \varepsilon$ is stored, but $1 + \varepsilon/2$ lies halfway and is rounded back to 1. Above $2^{53} = 9007199254740992$ the step between neighbouring floating-point numbers is 2, so the odd number $2^{53} + 1$ cannot be stored at all: it is rounded to $2^{53}$.

**The step at every size (PROVED).** Write a positive number as $x = f \cdot 2^e$ with $\tfrac12 \le f < 1$ (every positive number can be written so, by choosing the power of two). The 53 bits of $m$ then cover the factor $f$, whose last bit is worth $2^{-53}$; so the step to the next floating-point number is $2^{-53} \cdot 2^e = 2^{e - 53}$. Divided by $x$:

$$
\frac{2^{e - 53}}{f \cdot 2^e} = \frac{2^{-53}}{f},\qquad\text{and}\qquad \tfrac12 \le f < 1\ \Rightarrow\ 2^{-53} < \frac{2^{-53}}{f} \le 2^{-52}
$$

(cancel $2^e$; then divide the inequalities for $f$ into $2^{-53}$, which reverses them). So the **relative** step always lies between $\varepsilon/2$ and $\varepsilon$: floating-point numbers have about 16 significant decimal digits at every size, and rounding a number to the nearest one changes it by at most $\varepsilon/2$ of its size. Notebook 01f, In [7], checks the formula $2^{e - 53}$ at 2301 numbers from $10^{-3}$ to $10^{20}$, and In [8] draws the step.

**Cancellation.** The function $f(x) = (1 - \cos x)/x^2$ tends to $\tfrac12$ as $x$ tends to 0 (because $\cos x \approx 1 - x^2/2$ for small $x$, a fact of calculus, the Taylor series of the cosine, ASSUMED here and confirmed by sympy in Notebook 01f, In [9]). Computed as written, it fails for small $x$. The computer's value of $\cos x$ is a floating-point number near 1, so it is wrong by up to the spacing of the floating-point numbers there, of the size of $\varepsilon$; the subtraction $1 - \cos x$ keeps this absolute error, while the true value $x^2/2$ is tiny. The relative error of the result is therefore of the size

$$
\frac{\varepsilon}{x^2/2} = \frac{2\varepsilon}{x^2}
$$

(absolute error divided by the size of the true value; the dashed line of Figure 01f.4). For $x = 10^{-8}$ the true value of $\cos x$ is $1 - 5 \times 10^{-17}$, which is nearer to 1 than to the floating-point number just below 1 (which is $1 - 2^{-53} \approx 1 - 1.1 \times 10^{-16}$), so $\cos x$ is rounded to exactly 1 and the formula returns 0: every digit is lost. This loss of digits when two nearly equal numbers are subtracted is called **cancellation**.

**The cure: rewrite the formula (PROVED).** From the addition theorem $\cos(2y) = \cos^2 y - \sin^2 y$ and $\cos^2 y = 1 - \sin^2 y$:

$$
\cos(2y) = 1 - \sin^2 y - \sin^2 y = 1 - 2\sin^2 y,\qquad\text{so with } y = x/2:\qquad 1 - \cos x = 2\sin^2(x/2)
$$

(insert the second identity into the first; collect; then put $y = x/2$ and move terms across). Hence $f(x) = 2\sin^2(x/2)/x^2$, a formula without a subtraction. Notebook 01f, In [9], compares both formulas with 50-digit arithmetic at 361 values of $x$ from $10^{-9}$ to 1: the rewritten formula has the largest relative error $4.4 \times 10^{-16}$, the formula as written $1.0$, that is 100 per cent (COMPUTED). Whenever a later notebook of the course rewrites a formula before computing it, this is the reason.

### 1.5 Powers, roots, the exponential function and the logarithm

**The laws of powers.** For positive numbers $a, b$ and any real numbers $p, q$:

$$
a^p a^q = a^{p + q},\qquad (a^p)^q = a^{pq},\qquad (ab)^p = a^p b^p,\qquad a^{-p} = \frac{1}{a^p},\qquad \sqrt a = a^{1/2},\qquad a^{1/n} = \sqrt[n]{a} .
$$

These are school algebra (ASSUMED here; Notebook 01f, In [10], confirms them with sympy for symbols declared positive). They need positive bases. For a negative number the law $(a^p)^q = a^{pq}$ can fail: $\sqrt{(-2)^2} = \sqrt 4 = 2$, not $-2$. In general $\sqrt{y^2} = |y|$, the **absolute value** of $y$ ($y$ without its sign).

**A worked example (PROVED).** For $s > 0$ and real $a$:

$$
\frac{1}{\sqrt{s^{1/3}/e^{2a}}} = \Big(\frac{s^{1/3}}{e^{2a}}\Big)^{-1/2} = \frac{(s^{1/3})^{-1/2}}{(e^{2a})^{-1/2}} = \frac{s^{-1/6}}{e^{-a}} = \frac{e^{a}}{s^{1/6}}
$$

(the root is the power $1/2$ and one over it the power $-1/2$; the power of a quotient is the quotient of the powers; $(a^p)^q = a^{pq}$ twice, with $\tfrac13 \cdot (-\tfrac12) = -\tfrac16$ and $2 \cdot (-\tfrac12) = -1$; one over $e^{-a}$ is $e^a$ and $s^{-1/6}$ is one over $s^{1/6}$).

**The length factors of the author's metric (PROVED).** The metric $g$ of Section 1.1 is **diagonal**: it has one entry $g_{\mu\mu}$ for each direction $x_\mu$ ($\mu = 1, \dots, 8$), and the squared length of a small step $dx_\mu$ along that one direction is $g_{\mu\mu}\, dx_\mu^2$. A negative entry marks a **time-like** direction ($x_4$ to $x_7$), a positive entry a **space-like** one ($x_1, x_2, x_3, x_8$). The **length factor** of a direction is $\sqrt{|g_{\mu\mu}|}$: the length of the step is the factor times $|dx_\mu|$. For $0 < z < \pi/2$ both $\sin z$ and $\cos z$ are positive, so the laws of powers apply and give

$$
\sqrt{e^{2a_4}\sin^{1/3} z} = e^{a_4}\sin^{1/6} z,\qquad \sqrt{e^{-2a_4}\sin^{1/3} z} = e^{-a_4}\sin^{1/6} z,\qquad \sqrt{1} = 1,\qquad \sqrt{\cot^2 z} = \cot z
$$

(the root of a product is the product of the roots; $\sqrt{e^{2a_4}} = e^{a_4}$ and $\sqrt{\sin^{1/3} z} = \sin^{1/6} z$ by $(a^p)^q = a^{pq}$; $\cot z > 0$). The three space directions have the factor $e^{a_4}\sin^{1/6} z$, which grows as $a_4$ grows; the three extra times have $e^{-a_4}\sin^{1/6} z$, which shrinks exponentially; the time has 1 and the hidden direction $\cot z$. The product of all eight factors is

$$
(e^{a_4}\sin^{1/6} z)^3 \cdot 1 \cdot (e^{-a_4}\sin^{1/6} z)^3 \cdot \cot z = e^{3a_4 - 3a_4}\,\sin^{6/6} z\,\cot z = \sin z\cot z = \cos z
$$

(collect the powers of $e$ and of $\sin z$ with $a^p a^q = a^{p+q}$: $3a_4 - 3a_4 = 0$ and $6 \cdot \tfrac16 = 1$; then $\cot z = \cos z/\sin z$). The growth of space and the deflation of the extra times cancel exactly in the product, for every value of $a_4$. The Revision record stores this product as `sqrtAbsDetG` $= \sin z \cot z$ in `Revision/gkd_lovelock/results/curvature.json` and checks it in `python-lovelock-report.json`, check `sqrt_abs_det_g`; Notebook 01f, In [11], reads the metric from the record and reproduces both. (Section 1.1 explains why this product is the square root of the size of the determinant of $g$.)

**The number e.** The number $e = 2.71828\dots$ is the limit of $(1 + 1/n)^n$ for ever larger $n$: the growth of one unit of money in a year at the interest rate of 100 per cent, paid in $n$ equal parts. How fast is the limit reached? With the natural logarithm $\ln$ (defined below) and the series $\ln(1 + u) = u - u^2/2 + u^3/3 - \dots$ for small $u$ (a Taylor series of calculus, ASSUMED here):

$$
\ln\Big(1 + \frac1n\Big)^n = n\ln\Big(1 + \frac1n\Big) = n\Big(\frac1n - \frac{1}{2n^2} + \dots\Big) = 1 - \frac{1}{2n} + \dots
$$

(the logarithm of a power is the power times the logarithm; insert the series with $u = 1/n$; multiply out), so

$$
\Big(1 + \frac1n\Big)^n = e^{1 - 1/(2n) + \dots} = e \cdot e^{-1/(2n) + \dots} \approx e\Big(1 - \frac{1}{2n}\Big),\qquad e - \Big(1 + \frac1n\Big)^n \approx \frac{e}{2n}
$$

(undo the logarithm with the exponential; split the power with $a^{p+q} = a^p a^q$; use $e^{-u} \approx 1 - u$ for small $u$; subtract from $e$). Notebook 01f, In [12], confirms the law $e/(2n)$ within 1 per cent for every $n = 10^3, \dots, 10^{16}$ with 50-digit arithmetic. With floating-point numbers the limit breaks down: $1 + 1/n$ is rounded by up to $\varepsilon/2$ of its size, and raising to the power $n$ multiplies this relative error by about $n$ (because $(1 + \delta)^n \approx 1 + n\delta$ for small $\delta$). For $n = 10^9$ the computed error is $2.2 \times 10^{-7}$ instead of $1.36 \times 10^{-9}$, and for $n = 10^{16}$ the number $1 + 10^{-16}$ is rounded to exactly 1, so the result is $1^n = 1$ and the error is $e - 1 = 1.7$ (COMPUTED, Notebook 01f, In [12]; Figure 01f.5).

**The exponential function and the logarithm.** The **exponential function** $e^t$ is defined for every real $t$, is always positive and grows; its inverse is the **natural logarithm** $\ln x$, defined for $x > 0$: $\ln(e^t) = t$ and $e^{\ln x} = x$. The logarithm turns products into sums (PROVED):

$$
e^{\ln x + \ln y} = e^{\ln x}\, e^{\ln y} = x y\qquad\Rightarrow\qquad \ln(x y) = \ln x + \ln y
$$

(the law $a^{p+q} = a^p a^q$ with $a = e$; then take the logarithm of both sides). For the author's metric this means: when $a_4$ grows by $\ln 2 \approx 0.693$, the space factor $e^{a_4}$ doubles and the extra-time factor halves,

$$
e^{-(a_4 + \ln 2)} = e^{-a_4}\, e^{-\ln 2} = e^{-a_4}\cdot\frac12
$$

(the law of powers; then $e^{-\ln 2} = 1/e^{\ln 2} = 1/2$). A growth of $a_4$ by 1 multiplies $e^{a_4}$ by $e$, one **e-fold**. To shrink the extra times by a factor 1000, $a_4$ must grow by $\ln 1000 = 6.9078$ (COMPUTED, Notebook 01f, In [12]). On a **logarithmic axis**, on which each equal step multiplies by the same factor, both $e^{a_4}$ and $e^{-a_4}$ are straight lines, one rising and one falling equally fast (Figure 01f.6).

### 1.6 Example: numbers, rounding and the length factors of the author's metric

Notebook 01f puts Sections 1.2 to 1.5 to work. It computes exactly with whole numbers and fractions; writes long division as a program and plots the periods of $1/q$; proves and checks that $\sqrt 2$ is not a fraction and pins it down by bisection and by the fractions $p/q$ with $p^2 - 2q^2 = \pm 1$; shows how floating-point numbers are spaced, why $0.1 + 0.2 \neq 0.3$ in a computer, and how cancellation destroys a formula and how rewriting cures it; checks the laws of powers and applies them to the author's metric as stored in the Revision record; and builds $e$ as a limit and draws the growth $e^{a_4}$ of space and the exponential deflation $e^{-a_4}$ of the extra times. It ends with the line ALL 26 CHECKS PASSED (notebook 01f).

<!-- NOTEBOOK 01f -->

### 1.9 Line-by-line walk-through of Notebook 01f

The notebook has fourteen code cells, In [1] to In [14]. This section explains every line of every one of them, in order. A line that starts with `#` is a **comment**: Python skips it; it is there for the reader. A comment may also stand at the end of a line of code, after the sign `#`. Where a quoted cell ends with a long figure caption, the remaining lines of the caption are replaced here by `...)`; every caption is printed in full under its figure in Section 1.8.

**In [1], the set-up cell.** Its first part repeats the complete run instructions of Section 1.7 as comment lines, so that the notebook file carries its own instructions. The code starts below the line of `=` signs that reads THE SET-UP. This code is the same in every notebook of the book except for one line, the notebook's name. It is explained here once; the walk-throughs of the other six notebooks of this chapter refer back to this explanation.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module** (a part of Python or of an installed package) so that the code can use it. `json` reads and writes the text format JSON, in which the Revision record stores its results as names and values; `os` gives access to the computer's environment; `textwrap` breaks long text into lines; `from pathlib import Path` takes the single name `Path` out of the module `pathlib`. A `Path` is the address of a file or folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

These lines load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python code), which show a picture file below a cell.

```python
NOTEBOOK_ID = "01f"  # this notebook: chapter 01, example f
```

A **variable** is a name for a value. This line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"01f"`. It is the only line of the set-up code that differs between notebooks; the figure files and the captions file are named after it.

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

`def` defines a **function**: a named piece of code that runs when it is called. The text in triple quotes under the `def` line is its **docstring**, a description for the reader. `Path.cwd()` is the folder in which the notebook runs, and `.resolve()` writes it as a complete address. `here.parents` is the parent folder, its parent, and so on up to the top of the disk; `[here, *here.parents]` is the list that starts with `here` and continues with all of them (the star unpacks the parents into the list). The `for` loop takes the folders of this list one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that contains `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If no folder qualifies, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The first code line calls the function and names its result `REPO`. The second chooses the folder below which the notebook writes its files. `os.environ` holds the **environment variables** of the running program (named texts that a program receives from the computer); `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and the default `str(REPO)` (the repository folder as a string) otherwise. When you run the notebook the variable is not set, so the files go into the repository; the book's checking tool sets it to a scratch folder, so that a check never changes the repository.

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

`repository_file("Revision/...")` gives the full path of a file of the repository, for reading. `output_file("Revision/...")` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates the folder that will hold it, together with any missing folder above it, and does nothing if the folder exists.

```python
def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters, so that every printed line fits the width of a page of the book; `textwrap.fill` breaks the text at blanks, and every line after the first starts with four blanks. `str(text)` turns any value into a string first.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

matplotlib reads personal settings from a file on your computer if you have one; `matplotlib.rcdefaults()` returns to the built-in settings, so that the figures are the same on every computer. `plt.rcParams.update({...})` then sets four settings for every figure: its size (7.0 inches wide, 4.2 inches high), the size of its letters (10 points), and a faint grid behind the curves (`grid.alpha` 0.3: 30 per cent opaque). The braces `{...}` make a **dictionary**: pairs of a key and a value, written `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/01f.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes the text `{}` and a line end into the captions file: an empty list of captions, which `save_figure` fills. `encoding="utf-8"` fixes how the letters are stored as bytes.

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

This function saves a figure and shows it. `setdefault(name, value)` returns the number already stored for this figure name, or stores and returns `len(FIGURE_NUMBERS) + 1` (one more than the number of figures so far) for a new name; so the figures are numbered 1, 2, 3, ... and a cell run twice keeps the number of its figure. The file name is the notebook's name, the number and the figure's name, for example `01f_1_decimal_periods.png`. `fig.savefig` writes the picture as a PNG file with 150 dots per inch, cuts away the empty margin and stores no program name in the file, so that two runs write exactly the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time at the end of the cell. The caption is stored in `CAPTIONS`, and the whole dictionary is written into the captions file (`json.dumps` turns it into JSON text with one entry per line, the keys sorted). `display(Image(...))` shows the saved picture below the cell; the `metadata` entry tells the book's tools which file the picture is. The last line prints where the figure was saved, for example Figure 01f.1 saved as Revision/textbook/figures/01f_1_decimal_periods.png.

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

`PASSED` is an empty **list** (an ordered collection, written with square brackets). `check` is the function behind every check of the book. `condition` is a statement that is either true (`True`) or false (`False`). If it is false, `raise AssertionError(...)` stops the notebook with an error that names the check. (Python's own statement `assert` would do the same, but Python started with the option that optimises the code skips every `assert`; an `if` statement is never skipped.) If it is true, the name is appended to `PASSED` and the line PASS followed by the name is printed. `record=None` makes the third argument optional: a check that reproduces a number of the Revision record passes the record's file and check name, and `check` prints them on a second line that starts with reproduces.

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

`report` prints a key number as a line that starts with RESULT; `(f" {unit}" if unit else "")` adds a blank and the unit when a unit is given and nothing otherwise. `all_checks_passed` prints the last line of every notebook; `len(PASSED)` is the number of checks that passed. The last statement prints the one output line of In [1]: Set-up of notebook 01f complete: repository folder found, helpers defined. (Two strings written next to each other, as here on two lines, are joined by Python into one.)

**In [2], whole numbers and fractions.**

```python
import fractions  # exact fractions p/q
import math  # factorial, gcd, isqrt, e, log

import mpmath  # numbers with many digits
import numpy as np  # arrays of floating-point numbers
import sympy as sp  # exact algebra with symbols
```

The module `fractions` (part of Python) computes with exact fractions; `math` holds functions of single numbers: `math.factorial`, `math.gcd` (the greatest common divisor), `math.isqrt` (the whole part of a square root, computed exactly), the number `math.e` and the logarithm `math.log`. The package mpmath computes with as many decimal digits as requested; numpy (short name `np`) computes with **arrays**, lists of floating-point numbers on which arithmetic acts entry by entry; sympy (short name `sp`) does exact algebra with symbols.

```python
big = 2 ** 100
say(f"2^100 = {big} ({len(str(big))} digits)")
say(f"16! = {math.factorial(16)}")
check(big == 1267650600228229401496703205376 and len(str(big)) == 31
      and math.factorial(16) == 20922789888000,
      "2^100 and 16! are computed exactly")
```

In Python `**` means "to the power", so `2 ** 100` is $2^{100}$. `str(big)` writes the number as a string of digits and `len(...)` counts them. The check compares both numbers with their exact values, digit for digit (the operator `==` tests equality, `and` requires both conditions). Output: 2^100 = 1267650600228229401496703205376 (31 digits), 16! = 20922789888000, and the PASS line.

```python
third, sixth = fractions.Fraction(1, 3), fractions.Fraction(1, 6)
say(f"1/3 + 1/6 = {third + sixth}")
check(third + sixth == fractions.Fraction(1, 2), "1/3 + 1/6 = 1/2 exactly")
```

`fractions.Fraction(1, 3)` is the exact number $1/3$; the first line names two fractions at once (Python assigns the values on the right to the names on the left in order). Their sum is computed exactly as in Section 1.2 and printed as `1/2`; the check confirms it.

```python
reduced = fractions.Fraction(84, 126)  # Fraction always cancels common factors
say(f"gcd(84, 126) = {math.gcd(84, 126)}, 84/126 = {reduced}")
check(math.gcd(84, 126) == 42 and reduced == fractions.Fraction(2, 3)
      and (reduced.numerator, reduced.denominator) == (2, 3),
      "84/126 = 2/3 in lowest terms, with gcd(84, 126) = 42")
```

A `Fraction` is always stored in lowest terms, so `Fraction(84, 126)` becomes $2/3$; `.numerator` and `.denominator` read its two parts. The check confirms $\gcd(84, 126) = 42$ and the lowest terms of Section 1.2. Output: gcd(84, 126) = 42, 84/126 = 2/3 and the PASS line.

**In [3], long division.**

```python
def decimal_digits(p, q):
    """The decimal digits of p/q (0 < p < q) by long division: the digits before
    the repeating block, and the repeating block (empty if the division ends)."""
    digits = []
    first_seen = {}  # remainder -> the place of the digit it produced first
    remainder = p
    while remainder != 0 and remainder not in first_seen:
        first_seen[remainder] = len(digits)
        remainder *= 10
        digits.append(remainder // q)  # the next digit
        remainder %= q  # what is left
    if remainder == 0:
        return digits, []
    start = first_seen[remainder]  # the remainder came back: the digits repeat
    return digits[:start], digits[start:]
```

This is long division exactly as in Section 1.2. `digits` collects the digits; the dictionary `first_seen` remembers, for each remainder met so far, the place of the digit that it produced. The `while` loop runs as long as its condition is true: the remainder is not 0 (`!=` means "is not equal to") and has not been seen before. Inside, the present remainder is recorded with its place, multiplied by 10 (`remainder *= 10` is short for `remainder = remainder * 10`), the whole part of the division by $q$ (`//`, division without the remainder) is appended as the next digit, and `remainder %= q` keeps what is left (`%` gives the remainder of a division). When the loop stops, either the remainder is 0 (the division has ended, and the function returns the digits and an empty block `[]`), or a remainder has come back; then the digits from its first place on repeat. `digits[:start]` is the part of the list before place `start`, `digits[start:]` the part from there on. The function returns both lists.

```python
def from_digits(head, block):
    """The fraction with the digits head followed by block repeated for ever."""
    k, m = len(head), len(block)
    D = int("".join(map(str, head)) or "0")
    value = fractions.Fraction(D, 10 ** k)
    if block:
        C = int("".join(map(str, block)))
        value += fractions.Fraction(C, 10 ** k * (10 ** m - 1))
    return value
```

This function turns the digits back into the fraction with the formula $D/10^k + C/(10^k(10^m - 1))$ of Section 1.2. `map(str, head)` turns every digit into a one-letter string, `"".join(...)` glues them into one string, and `int(...)` reads it as the whole number $D$; when there are no digits before the block, the empty string is replaced by `"0"` (`or` takes its right side when the left side is empty). `if block:` is true when the block is not empty; then the block's whole number $C$ is made the same way and its value is added.

```python
all_back = True
for p, q in [(1, 4), (1, 3), (1, 6), (1, 7), (5, 12), (1, 97)]:
    head, block = decimal_digits(p, q)
    head_text = "".join(map(str, head))
    block_text = "(" + "".join(map(str, block)) + ")" if block else ""
    text = "0." + head_text + block_text
    if len(text) > 40:  # 1/97 has a block of 96 digits: show its length only
        text = f"0.({len(block)} repeating digits)"
    say(f"{p}/{q} = {text}, period {len(block)}")
    all_back &= from_digits(head, block) == fractions.Fraction(p, q)
check(decimal_digits(1, 7) == ([], [1, 4, 2, 8, 5, 7]) and all_back,
      "1/7 = 0.(142857), and the digits of all six examples give the fractions back")
```

The loop takes six fractions. For each it computes the digits, writes them as text with the repeating block in brackets (`... if block else ""`: the bracketed block when there is one, nothing otherwise), and prints the result with its period, the length of the block. For $1/97$ the text would be too long for a line, so only the length 96 is printed. `all_back &= ...` is short for `all_back = all_back and ...`: it stays true only if every fraction is recovered from its digits. The check also compares the digits of $1/7$ with the hand calculation. Output: 1/4 = 0.25 (period 0), 1/3 = 0.(3), 1/6 = 0.1(6), 1/7 = 0.(142857) (period 6), 5/12 = 0.41(6), 1/97 with 96 repeating digits, and the PASS line.

**In [4], which fractions end, and the plot of the periods.**

```python
def only_twos_and_fives(q):
    """True if q has no prime factor other than 2 and 5."""
    for factor in (2, 5):
        while q % factor == 0:
            q //= factor
    return q == 1
```

The function divides $q$ by 2 as long as it can (`q % factor == 0`: the remainder is 0), then by 5 as long as it can; `q //= factor` is short for `q = q // factor`. If 1 is left, $q$ had no other prime factor.

```python
qs = list(range(2, 301))
periods = [len(decimal_digits(1, q)[1]) for q in qs]
check(all((period == 0) == only_twos_and_fives(q) for q, period in zip(qs, periods))
      and all(period <= q - 1 for q, period in zip(qs, periods)),
      "1/q ends exactly when q = 2^a 5^b, and the period is at most q - 1 "
      "(q = 2 to 300)")
```

`range(2, 301)` counts from 2 up to 300 (the end 301 is not included), and `list(...)` makes it a list. The second line is a **list comprehension**: for every $q$ it computes the digits of $1/q$, takes the block (entry `[1]` of the pair returned by `decimal_digits`) and its length. `zip(qs, periods)` pairs each $q$ with its period. `all(...)` is true when the condition holds for every pair: the period is 0 exactly when $q = 2^a 5^b$ (the theorem of Section 1.2), and it never exceeds $q - 1$.

```python
full = [q for q, period in zip(qs, periods) if period == q - 1]
say(f"q with the full period q - 1: {full[:12]} ... ({len(full)} of them)")
```

`full` collects the denominators with the largest possible period $q - 1$; the line prints the first twelve (`full[:12]`) and their number: 7, 17, 19, 23, 29, 47, 59, 61, 97, 109, 113, 131, ... (23 of them).

```python
fig, ax = plt.subplots(figsize=(8.0, 4.4))
ax.plot(qs, periods, ".", color="tab:blue", label="period of $1/q$")
ax.plot(full, [q - 1 for q in full], "o", color="tab:red", fillstyle="none",
        label="full period $q - 1$")
ax.plot([2, 300], [1, 299], "k:", lw=1, label="the largest possible: $q - 1$")
ax.set_xlabel("denominator $q$")
ax.set_ylabel("length of the repeating block")
ax.set_title("Decimal expansion of $1/q$: the period")
ax.legend(loc="upper left", fontsize=8);
save_figure(fig, "decimal_periods",
            "The length of the repeating block (the period) of the decimal digits "
            ...)
```

`plt.subplots(figsize=(8.0, 4.4))` makes a new figure `fig`, 8 inches wide and 4.4 high, with one pair of axes `ax`. `ax.plot(xs, ys, style)` draws the points with these coordinates: `"."` small dots (the periods), `"o"` with `fillstyle="none"` open red circles (the full periods), and `"k:"` a black (`k`) dotted (`:`) line of width 1 (`lw=1`) from $(2, 1)$ to $(300, 299)$, the line $q - 1$. `label=` names a curve in the legend; text between dollar signs is typeset as mathematics. The next three lines label the axes and set the title; `ax.legend(...)` draws the legend in the upper left corner with small letters. The semicolon at the end of that line keeps Jupyter from printing the value of the line (a description of the legend with a memory address, which would differ from run to run). `save_figure` saves Figure 01f.1 with its caption. What Figure 01f.1 shows: every dot lies on or below the dotted line, the dots at 0 are the denominators $2^a 5^b$, and the red circles are the primes that reach the bound $q - 1$.

**In [5], the square root of 2 is not a fraction; fractions that come close.**

```python
# isqrt(n) is the whole part of the square root of n, computed exactly:
no_solution = all(math.isqrt(2 * q * q) ** 2 != 2 * q * q for q in range(1, 10001))
check(no_solution, "p^2 = 2 q^2 has no solution in whole numbers with q <= 10000")
```

If $p^2 = 2q^2$ had a solution, $p$ would be the whole number $\mathrm{isqrt}(2q^2)$ and its square would equal $2q^2$. The line tests this for every $q$ from 1 to 10000 with exact whole numbers and finds no solution, as the proof of Section 1.3 says.

```python
mpmath.mp.dps = 50  # 50 significant digits
root2 = mpmath.sqrt(2)
convergents = [(1, 1)]
while len(convergents) < 12:
    p, q = convergents[-1]
    convergents.append((p + 2 * q, p + q))  # the rule p' = p + 2q, q' = p + q
```

`mpmath.mp.dps = 50` makes mpmath compute with 50 significant decimal digits (`dps`: decimal places), so `root2` is $\sqrt 2$ to 50 digits. The list `convergents` starts with the pair $(1, 1)$; the loop takes the last pair (`[-1]` is the last entry of a list), applies the rule of Section 1.3 and appends the new pair, until there are 12 pairs.

```python
for p, q in convergents:
    error = abs(mpmath.mpf(p) / q - root2)
    say(f"{p}/{q}: p^2 - 2 q^2 = {p * p - 2 * q * q:+d}, error "
        f"{mpmath.nstr(error, 3)}, error q^2 = {mpmath.nstr(error * q * q, 6)}")
```

For each fraction, `mpmath.mpf(p)` makes $p$ an mpmath number, so that $p/q$ is computed to 50 digits; `abs` is the absolute value. The printed line gives $p^2 - 2q^2$ with its sign (`:+d` prints a whole number with a sign), the error with 3 significant digits (`mpmath.nstr(x, 3)`) and the error times $q^2$ with 6. The output shows the signs $-1, +1, -1, \dots$ and the error times $q^2$ settling at 0.353553 from $577/408$ on.

```python
signs = [p * p - 2 * q * q for p, q in convergents]
check(signs == [(-1) ** (k + 1) for k in range(12)],
      "p^2 - 2 q^2 = -1, +1, -1, ... for the 12 fractions")
p, q = convergents[-1]
limit_value = 1 / (2 * root2)
check(abs(abs(mpmath.mpf(p) / q - root2) * q * q - limit_value) < mpmath.mpf("1e-6"),
      "the error of p/q times q^2 approaches 1/(2 sqrt 2) = 0.35355")
```

The first check compares the list of the values $p^2 - 2q^2$ with $(-1)^{k+1}$ for $k = 0, \dots, 11$, that is $-1, +1, -1, \dots$, as derived in Section 1.3. The second takes the last fraction, $19601/13860$, and checks that its error times $q^2$ differs from $1/(2\sqrt 2) = 0.35355\dots$ by less than $10^{-6}$ (`mpmath.mpf("1e-6")` is $10^{-6}$ as an mpmath number).

**In [6], bisection, and the best fractions with each denominator.**

```python
low, high = fractions.Fraction(1), fractions.Fraction(2)  # 1^2 < 2 < 2^2
widths = [high - low]
for step in range(60):
    middle = (low + high) / 2
    if middle * middle < 2:
        low = middle  # the root is in the right half
    else:
        high = middle  # the root is in the left half
    widths.append(high - low)
```

This is bisection as described in Section 1.3, with exact fractions: the interval starts as $[1, 2]$; each of the 60 passes computes the middle, keeps the half that contains $\sqrt 2$ (`if ... else` runs the first block when the condition is true and the second otherwise), and records the new width.

```python
low_mp = mpmath.mpf(low.numerator) / low.denominator
high_mp = mpmath.mpf(high.numerator) / high.denominator
say(f"after 60 halvings: {mpmath.nstr(low_mp, 20)} < sqrt 2 < "
    f"{mpmath.nstr(high_mp, 20)}")
say(f"sqrt 2 with 30 digits: {mpmath.nstr(root2, 30)}")
check(low * low < 2 < high * high and high - low == fractions.Fraction(1, 2 ** 60)
      and low_mp < root2 < high_mp,
      "60 halvings: exact fractions low < sqrt 2 < high with high - low = 2^(-60)")
```

The two ends are turned into 50-digit numbers for printing with 20 significant digits: 1.4142135623730950483 and 1.4142135623730950492; $\sqrt 2$ itself is printed with 30 digits, 1.41421356237309504880168872421. Python allows chained comparisons, `a < b < c`, meaning $a < b$ and $b < c$. The check confirms with exact fractions that $\text{low}^2 < 2 < \text{high}^2$ and that the width is exactly $2^{-60}$, and with 50-digit numbers that $\sqrt 2$ lies between the ends.

```python
denominators = np.arange(1, 1001)
best_p = np.rint(denominators * np.sqrt(2.0))  # the nearest numerator for each q
best_error = np.abs(best_p / denominators - np.sqrt(2.0))
```

`np.arange(1, 1001)` is the array of the whole numbers 1 to 1000. For each denominator $q$ the best numerator is the whole number nearest to $q\sqrt 2$ (`np.rint` rounds to the nearest whole number), and `best_error` is the array of the 1000 errors $|p/q - \sqrt 2|$, computed in floating point (good enough for a picture).

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.3))
left.semilogy(range(61), [float(w) for w in widths], "o-", ms=3)
left.set_xlabel("number of halvings")
left.set_ylabel("width of the interval (logarithmic scale)")
left.set_title("bisection: $\\sqrt{2}$ between two fractions")
```

`plt.subplots(1, 2, ...)` makes a figure with two pairs of axes side by side, named `left` and `right`. `semilogy` draws with a logarithmic vertical axis; the widths (turned into floating-point numbers with `float`) are drawn against the step number as dots joined by lines (`"o-"`, marker size `ms=3`). In a string in Python a backslash has a special meaning, so the LaTeX command `\sqrt` is written with two backslashes.

```python
right.loglog(denominators, best_error, ".", ms=3, color="0.6",
             label="best $p/q$ for each $q$")
conv_q = [q for _, q in convergents if q <= 1000]
conv_error = [float(abs(mpmath.mpf(p) / q - root2)) for p, q in convergents
              if q <= 1000]
right.loglog(conv_q, conv_error, "o", color="tab:red",
             label="$1/1, 3/2, 7/5, 17/12, \\dots$")
right.loglog(denominators, 1 / (2 * np.sqrt(2.0) * denominators ** 2.0), "k--",
             lw=1, label="$1/(2\\sqrt{2}\\,q^2)$")
right.set_xlabel("denominator $q$")
right.set_ylabel("error $|p/q - \\sqrt{2}|$")
right.set_title("the best fractions near $\\sqrt{2}$")
right.legend(fontsize=8, loc="lower left")
fig.tight_layout()
save_figure(fig, "square_root_of_two",
            "Left: the width of the interval between two fractions that contains "
            ...)
```

On the right panel, `loglog` makes both axes logarithmic. The 1000 best errors are drawn as grey dots (`color="0.6"` is a grey of brightness 60 per cent); the fractions of In [5] with $q \le 1000$ (the name `_` marks a value that is not used) as red circles; and the line $1/(2\sqrt 2\, q^2)$ as a black dashed line (the style string made of the letter k and two hyphens). `fig.tight_layout()` arranges the two panels so that their labels do not overlap. What Figure 01f.2 shows: on the left a straight falling line (each step halves the width); on the right no error is zero, and the red fractions lie on the dashed line, as close to $\sqrt 2$ as $1/q^2$ allows.

**In [7], floating-point numbers.**

```python
total = 0.1 + 0.2
stored = fractions.Fraction(0.1)  # the exact value of the floating-point number 0.1
say(f"0.1 + 0.2 = {total:.17f} (17 digits), and 0.3 = {0.3:.17f}")
say(f"0.1 is stored as {stored.numerator}/{stored.denominator}")
check(total != 0.3 and stored != fractions.Fraction(1, 10)
      and stored.denominator == 2 ** 55,
      "0.1 + 0.2 is not 0.3 in floating point, and 0.1 is stored as a fraction "
      "with the denominator 2^55")
```

`fractions.Fraction(0.1)` reads the exact value of the floating-point number that Python stores for 0.1. `{total:.17f}` prints a number with 17 digits after the point. Output: 0.1 + 0.2 = 0.30000000000000004 and 0.3 = 0.29999999999999999 (the stored values, as Section 1.4 explains), and 0.1 is stored as 3602879701896397/36028797018963968, whose denominator is $2^{55}$. The check confirms all three statements.

```python
eps = float(np.finfo(float).eps)  # machine epsilon
say(f"machine epsilon = {eps!r} = 2^-52: {eps == 2.0 ** -52}")
check(eps == 2.0 ** -52 and 1.0 + eps != 1.0 and 1.0 + eps / 2 == 1.0,
      "1 + eps is the next number after 1; 1 + eps/2 is rounded back to 1")
check(float(2 ** 53 + 1) == float(2 ** 53) and float(2 ** 53 - 1) != float(2 ** 53),
      "2^53 + 1 cannot be stored: it is rounded to 2^53")
```

`np.finfo(float).eps` is machine epsilon as numpy knows it; `{eps!r}` prints it with all its digits, 2.220446049250313e-16 (the letter e followed by a number means "times ten to the power": `e-16` is $10^{-16}$), and the comparison with `2.0 ** -52` prints True. The first check is the statement of Section 1.4 about $1 + \varepsilon$ and $1 + \varepsilon/2$. The second converts the exact whole numbers $2^{53} + 1$ and $2^{53} - 1$ to floating point (`float(...)`): the first is rounded to $2^{53}$, the second is stored exactly.

```python
xs = np.logspace(-3, 20, 2301)  # 2301 numbers from 0.001 to 10^20
fraction_part, exponent = np.frexp(xs)  # xs = fraction_part * 2^exponent
predicted = np.ldexp(1.0, exponent - 53)  # 2^(exponent - 53)
check(bool(np.all(np.spacing(xs) == predicted))
      and bool(np.all(np.spacing(xs) <= eps * xs)),
      "the step after x is 2^(e - 53), never more than eps x (2301 values of x)")
```

`np.logspace(-3, 20, 2301)` makes 2301 numbers from $10^{-3}$ to $10^{20}$ that are equally spaced on a logarithmic axis. `np.frexp` writes each as $f \cdot 2^e$ with $\tfrac12 \le f < 1$ and returns the arrays of $f$ and $e$; `np.ldexp(1.0, e - 53)` computes $1 \cdot 2^{e - 53}$, the step predicted in Section 1.4. `np.spacing(x)` is the actual distance from $x$ to the next floating-point number. The check requires the two to agree exactly at all 2301 numbers, and the step never to exceed $\varepsilon x$. (`np.all` is numpy's version of `all`; `bool(...)` turns its answer into a plain True or False.)

**In [8], the picture of the spacing.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.4))
big_x = np.logspace(48, 57, 2000, base=2.0)  # from 2^48 to 2^57
left.loglog(big_x, np.spacing(big_x), color="tab:blue", lw=1.5, base=2,
            label="step to the next floating-point number")
left.axvline(2.0 ** 53, color="tab:red", lw=1, label="$x = 2^{53}$")
left.axhline(1.0, color="tab:red", ls=":", lw=1, label="step 1")
left.set_xlabel("number $x$ (logarithmic axis, base 2)")
left.set_ylabel("step size (logarithmic axis, base 2)")
left.set_title("the step doubles at every power of 2")
left.legend(fontsize=8, loc="upper left")
```

The left panel uses 2000 numbers from $2^{48}$ to $2^{57}$ (`base=2.0`: equally spaced on a logarithmic axis of base 2) and draws the step against $x$ with both axes logarithmic in base 2. `axvline` draws a vertical line at $x = 2^{53}$, `axhline` a horizontal dotted line (`ls=":"`) at the step 1.

```python
right.semilogx(xs, np.spacing(xs) / xs, color="tab:blue", lw=1,
               label="step divided by $x$")
right.axhline(eps, color="black", ls="--", lw=1, label="$\\varepsilon = 2^{-52}$")
right.axhline(eps / 2, color="black", ls=":", lw=1, label="$\\varepsilon/2$")
right.set_ylim(0.0, 1.35 * eps)
right.set_xlabel("number $x$")
right.set_ylabel("relative step")
right.set_title("the relative step is the same at every size")
right.legend(fontsize=8, loc="lower right")
fig.tight_layout()
save_figure(fig, "float_spacing",
            "How far apart floating-point numbers are. Left: the distance from a "
            ...)
```

The right panel draws the relative step, step divided by $x$, for the 2301 numbers of In [7] with a logarithmic horizontal axis (`semilogx`), and the two horizontal lines $\varepsilon$ (dashed) and $\varepsilon/2$ (dotted). `set_ylim` fixes the vertical range from 0 to $1.35\,\varepsilon$. What Figure 01f.3 shows: on the left a staircase that doubles at every power of 2 and reaches the step 2 right of $x = 2^{53}$; on the right a sawtooth that always stays between $\varepsilon/2$ and $\varepsilon$, the bounds proved in Section 1.4.

**In [9], cancellation and its cure.**

```python
x = sp.Symbol("x", positive=True)
limit_at_zero = sp.limit((1 - sp.cos(x)) / x ** 2, x, 0)
say(f"sympy: the limit of (1 - cos x)/x^2 at x = 0 is {limit_at_zero}")
check(limit_at_zero == sp.Rational(1, 2)
      and sp.simplify(1 - sp.cos(x) - 2 * sp.sin(x / 2) ** 2) == 0,
      "the limit is 1/2, and 1 - cos x = 2 sin(x/2)^2 exactly")
```

`sp.Symbol("x", positive=True)` makes a sympy symbol, a letter that stands for any positive number. `sp.limit(f, x, 0)` computes the limit of the expression as $x$ tends to 0 exactly: $1/2$ (`sp.Rational(1, 2)` is sympy's exact fraction). `sp.simplify(...) == 0` asks sympy to prove that $1 - \cos x - 2\sin^2(x/2)$ is zero for every $x$: the identity derived in Section 1.4.

```python
x_values = np.logspace(-9, 0, 361)
naive = (1 - np.cos(x_values)) / x_values ** 2
stable = 2 * np.sin(x_values / 2) ** 2 / x_values ** 2
mpmath.mp.dps = 50
exact = np.array([float((1 - mpmath.cos(mpmath.mpf(v))) / mpmath.mpf(v) ** 2)
                  for v in x_values.tolist()])  # mpf(v) is the stored value of v
error_naive = np.abs(naive - exact) / exact
error_stable = np.abs(stable - exact) / exact
```

361 values of $x$ from $10^{-9}$ to 1. `naive` is the formula as written, `stable` the rewritten one, both in floating point. `exact` computes the same function with 50 digits for each value (`x_values.tolist()` turns the array into a plain list; `mpmath.mpf(v)` takes the stored floating-point value exactly, so that all three use the same $x$) and rounds the result to a floating-point number. The last two lines are the relative errors.

```python
report("largest relative error of 2 sin(x/2)^2/x^2", f"{error_stable.max():.1e}")
report("largest relative error of (1 - cos x)/x^2", f"{error_naive.max():.1e}")
check(float(error_stable.max()) < 1e-15,
      "the rewritten formula is correct to 1e-15 at all 361 values of x")
check((1 - math.cos(1e-8)) / 1e-8 ** 2 == 0.0
      and float(error_naive[x_values <= 1e-4].max()) > 1e-3,
      "the formula as written gives 0 at x = 1e-8: cancellation destroyed every digit")
```

The two RESULT lines print the largest relative errors with two significant digits (`.1e`: one digit after the point, in the e-notation): 4.4e-16 for the rewritten formula and 1.0e+00 for the formula as written. The first check requires the rewritten formula to be right to $10^{-15}$ everywhere. The second confirms that the formula as written gives exactly 0 at $x = 10^{-8}$ (`1e-8` is $10^{-8}$) and that its error exceeds $10^{-3}$ somewhere among the values $x \le 10^{-4}$ (`error_naive[x_values <= 1e-4]` keeps only the errors at these values).

```python
fig, ax = plt.subplots(figsize=(8.0, 4.6))
floor = 1e-18  # an error 0 is drawn at the bottom of the axis
ax.loglog(x_values, np.maximum(error_naive, floor), ".", ms=3, color="tab:red",
          label="$(1 - \\cos x)/x^2$ as written")
ax.loglog(x_values, np.maximum(error_stable, floor), ".", ms=3, color="tab:blue",
          label="$2\\sin^2(x/2)/x^2$")
ax.loglog(x_values, 2 * eps / x_values ** 2, "k--", lw=1,
          label="$2\\varepsilon/x^2$")
ax.set_ylim(0.5 * floor, 10.0)
ax.set_xlabel("$x$")
ax.set_ylabel("relative error")
ax.set_title("Cancellation and its cure")
ax.legend(fontsize=8, loc="upper right");
save_figure(fig, "cancellation",
            "The relative error of two formulas for $(1 - \\cos x)/x^2$ against $x$ "
            ...)
```

A logarithmic axis cannot show the value 0, so `np.maximum(error, floor)` replaces every error below $10^{-18}$ by $10^{-18}$, which puts exact results at the bottom of the axis. The two error curves and the estimate $2\varepsilon/x^2$ of Section 1.4 are drawn on logarithmic axes. What Figure 01f.4 shows: the red dots follow the dashed line upwards as $x$ shrinks and reach an error of 100 per cent below about $x = 10^{-8}$; the blue dots stay at the rounding level of about $10^{-16}$.

**In [10], the laws of powers.**

```python
a, b = sp.symbols("a b", positive=True)
p_sym, q_sym = sp.symbols("p q", real=True)
laws = [a ** p_sym * a ** q_sym - a ** (p_sym + q_sym),
        (a ** p_sym) ** q_sym - a ** (p_sym * q_sym),
        (a * b) ** p_sym - a ** p_sym * b ** p_sym,
        a ** (-p_sym) - 1 / a ** p_sym,
        sp.sqrt(a) - a ** sp.Rational(1, 2)]
check(all(sp.simplify(law) == 0 for law in laws),
      "the five laws of powers hold for positive a, b and real p, q")
```

`sp.symbols("a b", positive=True)` makes two symbols for positive numbers, the next line two for real numbers. Each entry of the list `laws` is the difference of the two sides of one law of Section 1.5; the check asks sympy to simplify each difference to 0. Because sympy knows that $a$ and $b$ are positive, it may use the laws; it would refuse for symbols of unknown sign.

```python
y = sp.Symbol("y", real=True)  # a real number of either sign
say(f"sympy: sqrt(y^2) = {sp.sqrt(y ** 2)}; numbers: sqrt((-2)^2) = "
    f"{((-2.0) ** 2) ** 0.5}")
check(sp.sqrt(y ** 2) == sp.Abs(y) and ((-2.0) ** 2) ** 0.5 == 2.0,
      "sqrt(y^2) = |y|: for negative numbers the law (a^p)^q = a^(pq) fails")
```

For a real symbol of either sign sympy writes $\sqrt{y^2}$ as `Abs(y)`, the absolute value; the number example computes $((-2)^2)^{1/2} = 2$, not $(-2)^{2 \cdot 1/2} = -2$. Output: sympy: sqrt(y^2) = Abs(y); numbers: sqrt((-2)^2) = 2.0, and the PASS line.

```python
s_pos, a_real = sp.Symbol("s", positive=True), sp.Symbol("a", real=True)
example = 1 / sp.sqrt(s_pos ** sp.Rational(1, 3) / sp.exp(2 * a_real))
check(sp.simplify(example - sp.exp(a_real) / s_pos ** sp.Rational(1, 6)) == 0,
      "1/sqrt(s^(1/3)/e^(2a)) = e^a/s^(1/6)")
```

The worked example of Section 1.5, with $s > 0$ and real $a$; `sp.exp` is the exponential function. sympy confirms the result $e^a/s^{1/6}$.

**In [11], the length factors of the author's metric, from the record.**

```python
S, C = sp.symbols("S C", positive=True)  # S = sin z, C = cos z, both > 0
a4 = sp.Symbol("a4", real=True)  # the value of a4(x4) at one time
```

Two positive symbols stand for $\sin z$ and $\cos z$ (both are positive for $0 < z < \pi/2$), and a real symbol for the value of $a_4$ at one time.

```python
def from_record(text):
    """The record's Mathematica text as sympy, with sin z = S and cot z = C/S."""
    text = text.replace("a4[x4]", "a4").replace("Sin[6*H*x8]", "S")
    text = text.replace("Cot[6*H*x8]", "(C/S)").replace("^", "**")
    return sp.sympify(text, locals={"a4": a4, "S": S, "C": C, "E": sp.E})
```

The Revision record stores the metric as text in the notation of the program Mathematica, for example `E^(2*a4[x4])*Sin[6*H*x8]^(1/3)`. `from_record` translates such a text into a sympy expression: `.replace(old, new)` replaces every occurrence of a piece of text, here the function value `a4[x4]` by the symbol name `a4`, $\sin(6Hx_8)$ by `S`, $\cot(6Hx_8)$ by `(C/S)`, and Mathematica's power sign `^` by Python's `**`. `sp.sympify` then reads the text as a sympy expression; `locals` tells it which symbol each name means (`E` is the number $e$).

```python
curvature = json.loads(repository_file("Revision/gkd_lovelock/results/curvature.json")
                       .read_text(encoding="utf-8"))
eta = json.loads(repository_file("Revision/algebra/gammas.json")
                 .read_text(encoding="utf-8"))["eta"]  # +1 or -1 for x1 ... x8
metric = [from_record(text) for text in curvature["metricDiagonal"]]
sizes = [eta[mu] * metric[mu] for mu in range(8)]  # |g_mu mu| = eta_mu mu g_mu mu
check(all(size.is_positive for size in sizes),
      "every entry of the metric has the sign of eta: eta_mu mu g_mu mu > 0")
```

`read_text` reads a file of the repository as text, and `json.loads` turns the JSON text into a Python dictionary. From the record file `curvature.json` the cell takes the list `metricDiagonal` (the eight diagonal entries as texts); from `gammas.json` it takes the list `eta` of the signs $+1$ or $-1$ of the eight directions (the **frame metric**, Section 1.1). `metric` is the list of the eight entries as sympy expressions. Multiplying each entry by its sign gives its size $|g_{\mu\mu}|$; the check asks sympy whether each size is positive (`.is_positive`), which it can decide because $S$, $C$ and $e^{\pm 2a_4}$ are positive.

```python
factors = [sp.sqrt(size) for size in sizes]  # the length factors
expected = ([sp.exp(a4) * S ** sp.Rational(1, 6)] * 3 + [sp.Integer(1)]
            + [sp.exp(-a4) * S ** sp.Rational(1, 6)] * 3 + [C / S])
for mu in range(8):
    say(f"x{mu + 1}: g = {metric[mu]}, length factor {factors[mu]}")
check(all(sp.simplify(f - e) == 0 for f, e in zip(factors, expected)),
      "the length factors: e^a4 S^(1/6) for x1 to x3, 1 for x4, e^(-a4) S^(1/6) "
      "for x5 to x7, cot z = C/S for x8")
```

`factors` are the eight square roots. `expected` is the list of Section 1.5: a list multiplied by 3 repeats its entry three times, and `+` joins lists. The loop prints, for each direction ($x_{\mu+1}$, because Python counts from 0), the entry and its factor; sympy writes $e^{a_4}$ as `exp(a4)` and $S^{1/6}$ as `S**(1/6)`. The check confirms the eight factors.

```python
product = sp.simplify(sp.Mul(*factors))
record_root = sp.simplify(from_record(curvature["sqrtAbsDetG"]))
say(f"product of the eight factors = {product}; the record's sqrtAbsDetG = "
    f"{record_root}")
lovelock_report = json.loads(repository_file(
    "Revision/gkd_lovelock/results/python-lovelock-report.json")
    .read_text(encoding="utf-8"))
root_verdict = {c["name"]: c["verdict"]
                for c in lovelock_report["checks"]}["sqrt_abs_det_g"]
check(product == C and record_root == C and root_verdict == "PASS",
      "the product of the length factors is cos z, the record's sqrt|det g| = "
      "sin z cot z, for every a4",
      record="Revision/gkd_lovelock/results/curvature.json, sqrtAbsDetG; "
             "python-lovelock-report.json, check sqrt_abs_det_g")
```

`sp.Mul(*factors)` multiplies the eight factors (the star hands the list's entries to `Mul` one by one), and `simplify` reduces the product to `C`, that is $\cos z$, as derived in Section 1.5. The record's text `Sin[6*H*x8]*Cot[6*H*x8]` becomes $S \cdot C/S = C$ as well. The report `python-lovelock-report.json` holds a list of checks, each with a name and a verdict; the **dictionary comprehension** `{c["name"]: c["verdict"] for c in ...}` makes a dictionary from names to verdicts, and `["sqrt_abs_det_g"]` looks up the verdict of the record's check, `PASS`. The check reproduces the record and prints the two record names.

**In [12], the limit that defines e, and the logarithm.**

```python
mpmath.mp.dps = 50
n_values = [10 ** k for k in range(17)]
error_exact = [abs((1 + mpmath.mpf(1) / n) ** n - mpmath.e) for n in n_values]
error_float = [abs((1.0 + 1.0 / n) ** n - math.e) for n in n_values]
for k in (0, 3, 6, 9, 12, 16):
    say(f"n = 10^{k:2d}: 50 digits: error {mpmath.nstr(error_exact[k], 3):>8}; "
        f"floating point: error {error_float[k]:.1e}")
```

`n_values` are $1, 10, 100, \dots, 10^{16}$. For each the error of $(1 + 1/n)^n$ is computed twice: with 50 digits (`mpmath.e` is $e$ to 50 digits) and with floating-point numbers (`math.e` is $e$ as a float). Six of them are printed; `{k:2d}` prints $k$ in two places and `{...:>8}` puts the text at the right end of 8 places, so that the columns line up. Output: with 50 digits the errors 0.718, 0.00136, 1.36e-6, 1.36e-9, 1.36e-12, 1.36e-16; in floating point 7.2e-01, 1.4e-03, 1.4e-06, 2.2e-07, 2.4e-04, 1.7e+00.

```python
ratios = [error_exact[k] * n_values[k] / (mpmath.e / 2) for k in range(3, 17)]
check(all(abs(r - 1) < mpmath.mpf("0.01") for r in ratios),
      "50 digits: the error of (1 + 1/n)^n is e/(2n) within 1 per cent for n >= 1000")
check(error_float[16] == math.e - 1 and error_float[16] > 1e3 * error_float[6],
      "floating point: for n = 10^16, 1 + 1/n is rounded to 1, and the error grows "
      "to e - 1")
```

Each ratio divides the error by the estimate $e/(2n)$ of Section 1.5; the first check requires every ratio for $n \ge 1000$ to be within 1 per cent of 1. The second confirms that for $n = 10^{16}$ the floating-point error is exactly $e - 1$ (the result was $1^n = 1$) and that it is more than 1000 times the error at $n = 10^6$.

```python
t_sym = sp.Symbol("t", real=True)
u, w = sp.symbols("u w", positive=True)
check(sp.log(sp.exp(t_sym)) == t_sym
      and sp.expand_log(sp.log(u * w)) == sp.log(u) + sp.log(w)
      and sp.simplify(sp.exp(-(a4 + sp.log(2))) - sp.exp(-a4) / 2) == 0,
      "ln(e^t) = t, ln(u w) = ln u + ln w, and e^(-(a4 + ln 2)) = e^(-a4)/2")
report("growth of a4 that shrinks the extra times by a factor 1000",
       f"{math.log(1000):.4f}")
```

`sp.log` is the natural logarithm. The check confirms the three laws of Section 1.5; `sp.expand_log` splits the logarithm of a product of positive symbols into a sum. The RESULT line prints $\ln 1000 = 6.9078$ (`.4f`: four digits after the point).

**In [13], the figures of e and of growth and deflation.**

```python
fig, ax = plt.subplots(figsize=(8.0, 4.6))
ax.loglog(n_values, [float(e) for e in error_exact], "o-", color="tab:blue",
          label="50-digit arithmetic")
ax.loglog(n_values, error_float, "s-", color="tab:red", ms=5,
          label="floating point")
ax.loglog(n_values, [math.e / (2 * n) for n in n_values], "k--", lw=1,
          label="$e/(2n)$")
ax.set_xlabel("$n$")
ax.set_ylabel("error $|(1 + 1/n)^n - e|$")
ax.set_title("The limit that defines $e$")
ax.legend(fontsize=8, loc="lower left");
save_figure(fig, "limit_for_e",
            "The error of $(1 + 1/n)^n$ as an approximation of $e$ for $n = 1$ to "
            ...)
```

The two error lists of In [12] are drawn against $n$ on logarithmic axes, the 50-digit errors as blue circles joined by lines, the floating-point errors as red squares (`"s-"`), together with the estimate $e/(2n)$ as a dashed line. What Figure 01f.5 shows: the blue points lie on the dashed line all the way to $10^{16}$; the red points follow it only up to about $n = 10^8$, then rise again, because the rounding error multiplied by $n$ takes over.

```python
a4_values = np.linspace(0.0, 4.0, 401)
marks = np.log(2.0) * np.arange(6)  # a4 = 0, ln 2, 2 ln 2, ..., 5 ln 2
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.3))
for ax in (left, right):
    ax.plot(a4_values, np.exp(a4_values), color="tab:red",
            label="$e^{a_4}$: space $x_1, x_2, x_3$")
    ax.plot(a4_values, np.exp(-a4_values), color="tab:blue",
            label="$e^{-a_4}$: extra times $x_5, x_6, x_7$")
    ax.plot(marks, np.exp(marks), "o", color="tab:red", ms=4)
    ax.plot(marks, np.exp(-marks), "o", color="tab:blue", ms=4)
    ax.set_xlabel("$a_4$")
```

`np.linspace(0.0, 4.0, 401)` makes 401 equally spaced values of $a_4$ from 0 to 4. `marks` are the six values $0, \ln 2, \dots, 5\ln 2$ (`np.log` is the natural logarithm). The loop draws the same four things on both panels: the curves $e^{a_4}$ (red, the factor of space) and $e^{-a_4}$ (blue, the factor of the extra times), and dots at the marks, where the factors have doubled or halved once more.

```python
left.set_ylabel("factor (ordinary axis)")
left.set_title("ordinary vertical axis")
left.legend(fontsize=8, loc="upper left")
right.set_yscale("log")
right.set_ylabel("factor (logarithmic axis)")
right.set_title("logarithmic vertical axis: straight lines")
for k in range(1, 6):
    right.text(marks[k], np.exp(-marks[k]) * 0.55, f"$2^{{-{k}}}$", ha="center",
               fontsize=8, color="tab:blue")
fig.tight_layout()
save_figure(fig, "growth_and_deflation",
            "The factors $e^{a_4}$ (red), which multiply the lengths along the three "
            ...)
```

The left panel keeps an ordinary vertical axis; the right panel gets a logarithmic one (`set_yscale("log")`). `right.text(x, y, text)` writes a label below each blue dot: $2^{-1}, \dots, 2^{-5}$ (in an f-string, double braces `{{` and `}}` stand for single braces in the text, so that LaTeX receives `2^{-1}`; `ha="center"` centres the text on the point). What Figure 01f.6 shows: on the ordinary axis one curve shoots up and the other creeps towards 0; on the logarithmic axis both are straight lines with opposite slopes, and the blue dots halve at every step $\ln 2$: the extra times deflate exponentially as $a_4$ grows.

**In [14], the last check.**

```python
figure_names = ["01f_1_decimal_periods.png", "01f_2_square_root_of_two.png",
                "01f_3_float_spacing.png", "01f_4_cancellation.png",
                "01f_5_limit_for_e.png", "01f_6_growth_and_deflation.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all 6 figure files of this notebook exist")
all_checks_passed()
```

The list holds the names of the six figure files; the check confirms that each exists in the folder `Revision/textbook/figures` (below the output folder). `all_checks_passed()` prints the last line, ALL 26 CHECKS PASSED (notebook 01f). The 26 checks are: 3 in In [2], 1 in In [3], 1 in In [4], 3 in In [5], 1 in In [6], 4 in In [7], 3 in In [9], 3 in In [10], 3 in In [11], 3 in In [12] and 1 in In [14].
