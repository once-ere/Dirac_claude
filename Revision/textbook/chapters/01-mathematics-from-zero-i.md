## 1. Mathematics from zero I: numbers, complex numbers, vectors, matrices, indices, determinants, the generalized Kronecker delta

This chapter builds, from school algebra, every piece of algebra that the rest of the course uses: exact and rounded numbers, powers and the exponential function, complex numbers, vectors and matrices, determinants, index notation with the summation convention, eigenvalues and the signature of a metric, and the generalized Kronecker delta with which the field equations of gravity are written. Every idea is put to work in a Jupyter notebook, and every notebook is applied to the objects of the author's theory as soon as possible.

### 1.1 What this chapter is for

**Why so much algebra.** The theory of this course lives in a universe with eight directions. The author names them $x_1, \dots, x_8$: the three directions $x_1, x_2, x_3$ of ordinary space, the time $x_4$, three further time-like directions $x_5, x_6, x_7$, called the **extra times**, and a hidden space direction $x_8$. The geometry of this universe is described by the author's **metric**, a list of eight expressions, one for each direction, which says how long a small step along that direction is (the word is explained fully in Sections 1.5 and 1.29):

$$
g = \mathrm{diag}\big(e^{2a_4} s,\ e^{2a_4} s,\ e^{2a_4} s,\ -1,\ -e^{-2a_4} s,\ -e^{-2a_4} s,\ -e^{-2a_4} s,\ \cot^2 z\big),
$$

with $s = \sin^{1/3} z$ and $z = 6 H x_8$. Here $H$ is a positive constant of the author's, $z$ lies between $0$ and $\pi/2$, and $a_4$ is a function of the time $x_4$; as $a_4$ grows, the entries of space grow like $e^{2a_4}$ and the entries of the three extra times shrink like $e^{-2a_4}$: space inflates and the extra times **deflate exponentially**. To read this one line you need powers, roots, the exponential function, the trigonometric functions and the idea of a list of numbers with a sign attached to each entry. The fields of the theory have sixteen complex components at every point, and they are acted on by eight real $16 \times 16$ matrices, the **gamma matrices**. To compute with them you need complex numbers, matrices and their products, determinants, eigenvalues, and a compact notation, index notation, in which one short line stands for dozens of equations. Finally the field equations of gravity in eight dimensions (Chapter 11) are written with the **generalized Kronecker delta**, a determinant of zeros and ones. This chapter teaches all of it.

**The seven notebooks.** The chapter has seven worked examples, each a complete Jupyter notebook, taken in this order:

| notebook | topic | sections |
| --- | --- | --- |
| 01f | whole numbers, fractions, real and floating-point numbers, powers, exponential, logarithm | Sections 1.2 to 1.9 |
| 01b | complex numbers, Euler's formula, rotations, boosts, oscillation and growth | Sections 1.10 to 1.17 |
| 01a | vectors, matrices, permutations, determinants, the gamma matrices and the metric | Sections 1.18 to 1.25 |
| 01e | index notation, the summation convention, the frame metric, the Clifford relation | Sections 1.26 to 1.33 |
| 01g | eigenvalues, eigenvectors, the signature (4,4), Sylvester's law | Sections 1.34 to 1.41 |
| 01c | the generalized Kronecker delta, its proof, its counts, its contractions | Sections 1.42 to 1.48 |
| 01d | binary numbers, a pseudo-random generator, the record's tests of the generalized delta reproduced exactly | Sections 1.49 to 1.54 |

Each notebook appears in three parts: a section "How to run Notebook 01x", which gives the complete instructions for running it on Windows, macOS or Linux; a section "Notebook 01x: complete text", which prints every cell, everything it printed and every figure it drew; and a section "Line-by-line walk-through of Notebook 01x", which explains every line of every code cell. The first code cell of every notebook, the **set-up cell**, is the same in all notebooks except for the notebook's name; it is explained line by line once, in Section 1.9, and the later walk-throughs refer back to that explanation.

**Counting from 1 and from 0.** In mathematics the rows and columns of a table are numbered $1, 2, 3, \dots$, and the author numbers his coordinates $x_1$ to $x_8$. The programming language Python numbers the entries of a list $0, 1, 2, \dots$. So the coordinate $x_1$ is entry 0 of a Python list, $x_8$ is entry 7, and the entry in row 1 and column 1 of a matrix `A` is `A[0, 0]`. Every walk-through says which numbering a line uses.

**The labels of every statement.** Every result in this chapter carries one of the labels of the book: PROVED (an exact derivation is written out here, line by line, and a notebook checks it), COMPUTED (a number found by a notebook, with the cell that prints it), ASSUMED (a standard fact used without proof here, said so where it is used). When a notebook reproduces a number of the **Revision record** (the folder Revision of the repository, in which every computation of the author's theory is done and checked), the text names the record file and the check, exactly as the notebook's PASS line does. The labels HYPOTHESIS (a scenario that is stated, not derived) and OPEN (a question that no record answers yet), used later in the book, do not occur in this chapter. Nothing in this chapter concerns pair creation or matter and antimatter; those questions are treated, with the exact scope of what is proved, in Chapters 18 to 21.

### 1.2 Whole numbers and fractions, exactly

**Whole numbers.** The **whole numbers** (or **integers**) are $\dots, -2, -1, 0, 1, 2, \dots$. Python computes with them exactly, however many digits they have: $2^{100} = 1267650600228229401496703205376$ has 31 digits, and every one of them is right. Another large whole number that the course meets is

$$
16! = 1 \cdot 2 \cdot 3 \cdots 16 = 20922789888000 ,
$$

the number of terms of the determinant of a $16 \times 16$ matrix (Section 1.21). The symbol $n!$, read "$n$ factorial", is the product of the whole numbers from 1 to $n$, with $0! = 1$.

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

(collect the powers of $e$ and of $\sin z$ with $a^p a^q = a^{p+q}$: $3a_4 - 3a_4 = 0$ and $6 \cdot \tfrac16 = 1$; then $\cot z = \cos z/\sin z$). The growth of space and the deflation of the extra times cancel exactly in the product, for every value of $a_4$. The Revision record stores this product as `sqrtAbsDetG` $= \sin z \cot z$ in `Revision/gkd_lovelock/results/curvature.json` and checks it in `python-lovelock-report.json`, check `sqrt_abs_det_g`; Notebook 01f, In [11], reads the metric from the record and reproduces both. (Section 1.21 shows that this product is the square root of the size of the determinant of $g$.)

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

This function saves a figure and shows it. `setdefault(name, value)` returns the number already stored for this figure name, or stores and returns `len(FIGURE_NUMBERS) + 1` (one more than the number of figures so far) for a new name; so the figures are numbered 1, 2, 3, ... and a cell run twice keeps the number of its figure. The file name is the notebook's name, the number and the figure's name, for example `01f_1_decimal_periods.png`. `fig.savefig` writes the picture as a PNG file with 150 dots per inch, cuts away the empty margin and stores no program name in the file, so that two runs write exactly the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time at the end of the cell. The caption is stored in `CAPTIONS`, and the whole dictionary is written into the captions file (`json.dumps` turns it into JSON text with one entry per line, the keys sorted). `display(Image(...))` shows the saved picture below the cell; the `metadata` entry tells the book's tools which file the picture is. The last line prints where the figure was saved, for example `Figure 01f.1 saved as Revision/textbook/figures/01f_1_decimal_periods.png`.

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

The two ends are turned into 50-digit numbers and printed with 20 significant digits, and $\sqrt 2$ itself with 30 digits:

```text
after 60 halvings: 1.4142135623730950483 < sqrt 2 < 1.4142135623730950492
sqrt 2 with 30 digits: 1.41421356237309504880168872421
```

Python allows chained comparisons, `a < b < c`, meaning $a < b$ and $b < c$. The check confirms with exact fractions that $\text{low}^2 < 2 < \text{high}^2$ and that the width is exactly $2^{-60}$, and with 50-digit numbers that $\sqrt 2$ lies between the ends.

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

`read_text` reads a file of the repository as text, and `json.loads` turns the JSON text into a Python dictionary. From the record file `curvature.json` the cell takes the list `metricDiagonal` (the eight diagonal entries as texts); from `gammas.json` it takes the list `eta` of the signs $+1$ or $-1$ of the eight directions (the **frame metric**, Section 1.27). `metric` is the list of the eight entries as sympy expressions. Multiplying each entry by its sign gives its size $|g_{\mu\mu}|$; the check asks sympy whether each size is positive (`.is_positive`), which it can decide because $S$, $C$ and $e^{\pm 2a_4}$ are positive.

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

### 1.10 Complex numbers: the rules of arithmetic

**Why a new kind of number.** The equation $x^2 = -1$ has no solution among the real numbers, because the square of a real number is never negative. Yet the course needs such a solution everywhere. The fields of the author's theory have sixteen components at every point, and these components are **complex numbers** (for the field dirac16complex they are complex anticommuting quantities, introduced in Chapter 7; for the field dirac16complex00 they are ordinary complex numbers). A wave that oscillates in the time $x_4$ is written with a factor $e^{-i\varepsilon x_4}$, and whether such a wave stays bounded or grows without limit is decided by a complex number. This section builds the complex numbers from school algebra; Sections 1.11 to 1.13 add the exponential function, rotations and boosts.

**Definition.** We introduce a new number $i$, the **imaginary unit**, with the single property

$$
i^2 = -1 ,
$$

and we compute with it by the ordinary rules of algebra (sums and products may be re-ordered and multiplied out as usual). A **complex number** is a number $z = a + ib$ with two real numbers $a$ and $b$. The number $a = \mathrm{Re}\,z$ is its **real part** and $b = \mathrm{Im}\,z$ its **imaginary part**. Two complex numbers are equal when both their real parts and their imaginary parts are equal. A real number $a$ is the complex number $a + i0$; a number $ib$ with real part 0 is called **purely imaginary**. Python writes the imaginary unit as `1j` (the letter j right after a number), and sympy as `I`.

**Sum and product (PROVED).** Sums are taken part by part: $(a + ib) + (c + id) = (a + c) + i(b + d)$ (collect the real terms and the terms with $i$). The product follows from multiplying out:

$$
(a + ib)(c + id) = ac + iad + ibc + i^2 bd
$$

(every term of the first bracket times every term of the second: the distributive law),

$$
= ac + i(ad + bc) - bd
$$

(replace $i^2$ by $-1$, and take out the factor $i$ from the two middle terms),

$$
= (ac - bd) + i(ad + bc)
$$

(group the two real terms). For example

$$
(1 + 2i)(3 - i) = 3 - i + 6i - 2i^2 = 3 + 5i + 2 = 5 + 5i
$$

(multiply out; collect $-i + 6i = 5i$ and replace $-2i^2$ by $+2$; add $3 + 2$). The formula for the product does not change when $(a, b)$ and $(c, d)$ are exchanged ($ac - bd$ and $ad + bc$ stay the same), so $zw = wz$: complex numbers **commute**. (Matrices, in Section 1.18, will not.)

**The conjugate and the modulus (PROVED).** The **complex conjugate** of $z = a + ib$ is $z^* = a - ib$: the sign of the imaginary part is changed and nothing else. Then

$$
z z^* = (a + ib)(a - ib) = a^2 - iab + iab - i^2 b^2 = a^2 + b^2
$$

(multiply out; the two middle terms cancel, and $-i^2 b^2 = +b^2$). This is a real number and never negative. Its positive square root $|z| = \sqrt{a^2 + b^2}$ is the **modulus** (or size) of $z$. A number $z \neq 0$ can be divided by: multiplying numerator and denominator of a quotient by the conjugate of the denominator makes the denominator real,

$$
\frac{1 + 2i}{3 - i} = \frac{(1 + 2i)(3 + i)}{(3 - i)(3 + i)} = \frac{3 + i + 6i + 2i^2}{9 + 1} = \frac{1 + 7i}{10}
$$

(multiply numerator and denominator by $3 + i$, which does not change the quotient; multiply out both, the denominator with $zz^* = a^2 + b^2$; then $3 + 2i^2 = 1$).

**Three rules (PROVED).** For all complex $z = a + ib$ and $w = c + id$:

1. $(zw)^* = z^* w^*$. Proof: by the product rule $zw = (ac - bd) + i(ad + bc)$, so $(zw)^* = (ac - bd) - i(ad + bc)$; and $z^* w^* = (a - ib)(c - id) = ac - iad - ibc + i^2 bd = (ac - bd) - i(ad + bc)$ (multiply out; $i^2 = -1$; group). The two results are equal.
2. $zz^* = a^2 + b^2 = |z|^2$ (shown above).
3. $|zw| = |z|\,|w|$. Proof: $|zw|^2 = (zw)(zw)^*$ (rule 2 for the number $zw$) $= zw\,z^*w^*$ (rule 1) $= (zz^*)(ww^*)$ (complex numbers commute) $= |z|^2 |w|^2$ (rule 2 twice); then take the positive square root of both sides.

Notebook 01b, In [2] and In [3], checks the examples with exact sympy arithmetic and the three rules with sympy symbols that stand for any real numbers $a, b, c, d$.

**The complex plane.** The complex number $z = a + ib$ is drawn as the point $(a, b)$ of a plane, or as the arrow from the origin to that point: the horizontal axis carries the real part, the vertical axis the imaginary part. The modulus $|z|$ is the length of the arrow (Pythagoras). Adding two complex numbers adds the arrows: put the arrow of $w$ at the tip of the arrow of $z$. The conjugate $z^*$ is the mirror image of $z$ in the real axis. Multiplying by $i$ turns an arrow by a right angle:

$$
i(a + ib) = ia + i^2 b = -b + ia
$$

(multiply out; $i^2 = -1$), so the point $(a, b)$ goes to the point $(-b, a)$, which has the same length $\sqrt{b^2 + a^2}$ and lies a quarter turn further counterclockwise. For $z = 1 + 2i$ this is $iz = -2 + i$. Figure 01b.1 draws these arrows.

### 1.11 The exponential series and Euler's formula

**The exponential series.** From calculus we take the series of the exponential function (Chapter 2 derives it from Taylor's theorem; here it is ASSUMED):

$$
e^x = \sum_{k = 0}^{\infty} \frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots .
$$

A **series** is an endless sum $t_0 + t_1 + t_2 + \cdots$; its **partial sum** $S_N = t_0 + \dots + t_N$ adds the terms up to number $N$, and the series **converges** to a number $S$ when the error $|S_N - S|$ becomes as small as we like for large $N$. In the same way (also ASSUMED from calculus) the sine and the cosine are

$$
\cos\theta = 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots ,\qquad \sin\theta = \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots ,
$$

with $\theta$ in **radians** (the angle measured as the length of the arc on the circle of radius 1; $\pi$ radians are 180 degrees).

**Euler's formula (PROVED from the assumed series).** We define $e^{i\theta}$ for a real $\theta$ by putting $x = i\theta$ into the exponential series. The powers of $i$ repeat with period 4:

$$
i^0 = 1,\quad i^1 = i,\quad i^2 = -1,\quad i^3 = i^2\, i = -i,\quad i^4 = (i^2)^2 = 1,
$$

(each power is the previous one times $i$, with $i^2 = -1$), and then $1, i, -1, -i$ again. So in $(i\theta)^k/k! = i^k\theta^k/k!$ the even terms $k = 2m$ carry $i^{2m} = (i^2)^m = (-1)^m$ and the odd terms $k = 2m + 1$ carry $i^{2m+1} = i\,(-1)^m$:

$$
e^{i\theta} = \Big(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots\Big) + i\Big(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots\Big)
$$

(the terms of the series sorted into the even ones and the odd ones, the factor $i$ of the odd ones taken out),

$$
e^{i\theta} = \cos\theta + i\sin\theta
$$

(the two brackets are the series of the cosine and the sine). This is **Euler's formula**. Notebook 01b, In [5], adds the terms one by one for $\theta = 2$: after 21 terms ($N = 20$) the partial sum differs from $\cos 2 + i\sin 2$ by $4.1 \times 10^{-14}$ (COMPUTED); In [7] repeats the formula with 50-digit arithmetic.

**How fast the series converges (PROVED).** For $\theta \geq 0$:

$$
|S_N - e^{i\theta}| = \Big|\sum_{k \geq N + 1} \frac{(i\theta)^k}{k!}\Big| \leq \sum_{k \geq N + 1} \frac{\theta^k}{k!}
$$

(the full series minus the partial sum is the sum of the terms left out; the size of a sum is at most the sum of the sizes of its terms, a fact about complex numbers called the triangle inequality, ASSUMED here; and $|i^k| = 1$). Write $k = N + 1 + m$ with $m = 0, 1, 2, \dots$. Since

$$
(N + 1 + m)! = (N + 1)! \cdot (N + 2)(N + 3)\cdots(N + 1 + m) \geq (N + 1)!\; m!
$$

(the factorial split after the factor $N + 1$; each of the $m$ remaining factors $N + 1 + j$ is at least $j$, so their product is at least $1 \cdot 2 \cdots m = m!$), every term obeys

$$
\frac{\theta^{N + 1 + m}}{(N + 1 + m)!} \leq \frac{\theta^{N + 1}}{(N + 1)!}\cdot\frac{\theta^m}{m!}
$$

(a larger denominator gives a smaller fraction; $\theta^{N+1+m} = \theta^{N+1}\theta^m$). Adding over $m$ and using $\sum_m \theta^m/m! = e^\theta$:

$$
|S_N - e^{i\theta}| \leq e^{\theta}\,\frac{\theta^{N + 1}}{(N + 1)!} .
$$

For $\theta = 2$ and $N = 20$ the bound is $e^2\, 2^{21}/21! \approx 3.0 \times 10^{-13}$, and the error found, $4.1 \times 10^{-14}$, lies below it. For large $N$ the error is about the size of the first term left out, $\theta^{N+1}/(N + 1)!$, because each later term is smaller than the one before by the factor $\theta/(k + 1)$, which is small once $k$ is much larger than $\theta$. Going from $N$ to $N + 1$ the first term left out changes from $\theta^{N+1}/(N + 1)!$ to $\theta^{N+2}/(N + 2)!$, a factor

$$
\frac{\theta^{N + 2}/(N + 2)!}{\theta^{N + 1}/(N + 1)!} = \frac{\theta}{N + 2}
$$

(divide the powers and the factorials; $(N + 2)! = (N + 2)\,(N + 1)!$). Notebook 01b, In [6], finds this factor within 10 per cent for $N = 10$ to 19 (COMPUTED; Figure 01b.2).

**The law of exponents (PROVED).** For real angles $\alpha$ and $\beta$:

$$
e^{i\alpha} e^{i\beta} = (\cos\alpha + i\sin\alpha)(\cos\beta + i\sin\beta)
$$

(Euler's formula twice),

$$
= \cos\alpha\cos\beta + i\cos\alpha\sin\beta + i\sin\alpha\cos\beta + i^2\sin\alpha\sin\beta
$$

(multiply out),

$$
= (\cos\alpha\cos\beta - \sin\alpha\sin\beta) + i(\sin\alpha\cos\beta + \cos\alpha\sin\beta)
$$

($i^2 = -1$; group the real and the imaginary terms),

$$
= \cos(\alpha + \beta) + i\sin(\alpha + \beta) = e^{i(\alpha + \beta)}
$$

(the addition theorems $\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$ and $\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$ of school trigonometry, ASSUMED; then Euler's formula backwards). So the rule $e^{p} e^{q} = e^{p + q}$ of real exponents (Section 1.5) holds for imaginary exponents too, which is why the notation $e^{i\theta}$ is justified. For a general complex exponent we define $e^{x + iy} = e^x e^{iy}$ with real $x$ and $y$; then $e^{z} e^{w} = e^{z + w}$ for all complex $z$ and $w$, by the two laws of exponents. Notebook 01b, In [7], proves the law with sympy for symbols $\alpha$ and $\beta$.

**Three consequences (PROVED).** First, $|e^{i\theta}|^2 = \cos^2\theta + \sin^2\theta = 1$ (the modulus of $a + ib$ with $a = \cos\theta$, $b = \sin\theta$; then $\cos^2 + \sin^2 = 1$): the number $e^{i\theta}$ lies on the circle of radius 1, the **unit circle**, at the angle $\theta$. Second,

$$
(e^{i\theta})^* = \cos\theta - i\sin\theta = \cos(-\theta) + i\sin(-\theta) = e^{-i\theta}
$$

(conjugate; the cosine does not change and the sine changes sign when the angle changes sign; Euler's formula for the angle $-\theta$). Third, $e^{i\pi} = \cos\pi + i\sin\pi = -1 + 0i = -1$. Notebook 01b, In [7], computes $e^{i\pi}$ with 50 significant digits: the real part is $-1$ and an imaginary part of size $1.0 \times 10^{-51}$ is left over, because the number $\pi$ itself is stored with 50 digits, not because the formula fails (COMPUTED).

**The polar form.** Every complex number $z \neq 0$ can be written as $z = r e^{i\varphi}$ with $r = |z|$ and a real angle $\varphi$, its **argument** (or **phase angle**): the point $(a/r, b/r)$ lies on the unit circle, so it is $(\cos\varphi, \sin\varphi)$ for some angle $\varphi$ (school trigonometry, ASSUMED), and then $z = r(\cos\varphi + i\sin\varphi) = re^{i\varphi}$. Python's `cmath.phase(z)` returns the argument.

### 1.12 Multiplication turns the plane; the real matrix of a complex number

**Multiplication is a turn and a stretch (PROVED).** Let $u = r e^{i\alpha}$ and let $p = \rho e^{i\varphi}$ be any point of the plane. Then

$$
u\,p = r\rho\, e^{i\alpha} e^{i\varphi} = r\rho\, e^{i(\alpha + \varphi)}
$$

(re-order the factors, which commute; the law of exponents). So multiplying every point of the plane by $u$ multiplies every length by $r$ and adds $\alpha$ to every angle: it turns the plane about the origin by the angle $\alpha$ and stretches it by $r$. For $r = 1$ it is a pure **rotation**, which keeps every length. A rotation never mirrors a figure: Figure 01b.3 shows the letter F turned by 60 and by 150 degrees and turned back a quarter while shrunk to 0.6; it is never seen in its mirror image.

**Matrices of size 2 by 2.** To write the same turn without complex numbers we need a tool that the next part of the chapter develops fully (Sections 1.18 to 1.20), here only for tables of four numbers. A **2 × 2 matrix** is a table of four numbers in two rows and two columns. It acts on a pair of numbers $(x, y)$, written as a column, by "row times column":

$$
\begin{pmatrix} p & q \\ r & s \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} px + qy \\ rx + sy \end{pmatrix}
$$

(the first row $(p, q)$ is multiplied entry by entry with the column $(x, y)$ and added, and so is the second row). The **product** $MN$ of two such matrices is the matrix that acts like "first $N$, then $M$"; its entry in row $i$ and column $k$ is row $i$ of $M$ times column $k$ of $N$, entry by entry, added. The **identity matrix** $I$ has the rows $(1, 0)$ and $(0, 1)$ and leaves every pair unchanged. The **determinant** of the matrix with rows $(a, b)$ and $(c, d)$ is the number $ad - bc$. The **transpose** $M^T$ exchanges rows and columns: the rows of $M^T$ are the columns of $M$.

**The matrix of a complex number (PROVED).** Multiplying $x + iy$ by $a + ib$ gives, by the product rule of Section 1.10 with $c = x$ and $d = y$,

$$
(a + ib)(x + iy) = (ax - by) + i(bx + ay),
$$

and written for the pair $(x, y)$ this is

$$
\begin{pmatrix} a & -b \\ b & a \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} ax - by \\ bx + ay \end{pmatrix}
$$

(row times column: $a\cdot x + (-b)\cdot y$ and $b \cdot x + a \cdot y$). So every complex number $a + ib$ has a real matrix $M(a + ib)$ with the rows $(a, -b)$ and $(b, a)$. Multiplying the matrices is the same as multiplying the numbers:

$$
M(a + ib)\,M(c + id) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}\begin{pmatrix} c & -d \\ d & c \end{pmatrix} = \begin{pmatrix} ac - bd & -ad - bc \\ bc + ad & -bd + ac \end{pmatrix}
$$

(row times column for each of the four entries),

$$
= \begin{pmatrix} ac - bd & -(ad + bc) \\ ad + bc & ac - bd \end{pmatrix} = M\big((ac - bd) + i(ad + bc)\big) = M\big((a + ib)(c + id)\big)
$$

(re-order and take out the sign; this is the pattern of $M$ with real part $ac - bd$ and imaginary part $ad + bc$; the product rule of Section 1.10). The number $1$ has the matrix $M(1) = I$, and the number $i$ has the matrix

$$
J = M(i) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},\qquad J J = \begin{pmatrix} 0\cdot 0 + (-1)\cdot 1 & 0\cdot(-1) + (-1)\cdot 0 \\ 1 \cdot 0 + 0 \cdot 1 & 1\cdot(-1) + 0\cdot 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I
$$

(row times column). A *real* matrix squares to minus the identity: it plays the role of the number $i$. This is the first appearance of an idea that runs through the whole course: the author's gamma matrices are real, and real matrices whose squares are $-I$ do the work that the imaginary unit does elsewhere. The determinant of $M(a + ib)$ is $a\cdot a - (-b)\cdot b = a^2 + b^2 = |a + ib|^2$.

**The rotation matrix (PROVED).** The matrix of $e^{i\alpha} = \cos\alpha + i\sin\alpha$ is the **rotation matrix**

$$
R(\alpha) = M(e^{i\alpha}) = \begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix}.
$$

It inherits three properties. (a) $R(\alpha)R(\beta) = M(e^{i\alpha})M(e^{i\beta}) = M(e^{i\alpha}e^{i\beta}) = M(e^{i(\alpha + \beta)}) = R(\alpha + \beta)$ (the product rule of the matrices $M$; the law of exponents): two turns make one turn by the sum of the angles. (b) $\det R(\alpha) = \cos^2\alpha + \sin^2\alpha = 1$ (the determinant of $M$ is the squared modulus, here $|e^{i\alpha}|^2 = 1$). (c) $R(\alpha)^T R(\alpha) = I$:

$$
\begin{pmatrix} \cos\alpha & \sin\alpha \\ -\sin\alpha & \cos\alpha \end{pmatrix}\begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix} = \begin{pmatrix} \cos^2\alpha + \sin^2\alpha & -\cos\alpha\sin\alpha + \sin\alpha\cos\alpha \\ -\sin\alpha\cos\alpha + \cos\alpha\sin\alpha & \sin^2\alpha + \cos^2\alpha \end{pmatrix} = I
$$

(the transpose has the columns of $R$ as rows; row times column; then $\cos^2 + \sin^2 = 1$ and the mixed terms cancel). Property (c) says that $R$ keeps the squared length $x^2 + y^2$; directly, with $c = \cos\alpha$ and $s = \sin\alpha$,

$$
(cx - sy)^2 + (sx + cy)^2 = c^2x^2 - 2csxy + s^2y^2 + s^2x^2 + 2scxy + c^2y^2 = (c^2 + s^2)(x^2 + y^2) = x^2 + y^2
$$

(the squares of the two components of $R(x, y)$, multiplied out with $(u \pm v)^2 = u^2 \pm 2uv + v^2$; the mixed terms cancel; collect; $c^2 + s^2 = 1$). Notebook 01b, In [9], checks all of this exactly and checks that $R(\pi/3)$ moves the corners of the letter F exactly as multiplication by $e^{i\pi/3}$ does.

**The roots of unity (PROVED).** For a whole number $n \geq 1$ the $n$ numbers

$$
z_k = e^{2\pi i k/n},\qquad k = 0, 1, \dots, n - 1,
$$

satisfy $z_k^n = e^{2\pi i k} = \cos(2\pi k) + i\sin(2\pi k) = 1$ (the law of exponents applied $n$ times adds the angle $2\pi k/n$ to itself $n$ times; Euler's formula; a whole number of full turns). They are the **roots of unity** of order $n$, the corners of a regular polygon with $n$ sides on the unit circle. For $n \geq 2$ their sum $S = z_0 + \dots + z_{n-1}$ is 0:

$$
z_1 S = z_1 z_0 + z_1 z_1 + \dots + z_1 z_{n-1} = z_1 + z_2 + \dots + z_{n-1} + z_0 = S
$$

(multiply out; $z_1 z_k = e^{2\pi i(k + 1)/n} = z_{k+1}$ by the law of exponents, and $z_1 z_{n-1} = e^{2\pi i} = 1 = z_0$, so the same numbers appear in another order). Hence $(z_1 - 1)S = 0$, and since $z_1 \neq 1$ for $n \geq 2$, $S = 0$ (divide by the nonzero number $z_1 - 1$). The eight eighth roots are $1$, $\frac{\sqrt 2}{2} + \frac{\sqrt 2}{2} i$, $i$, $-\frac{\sqrt 2}{2} + \frac{\sqrt 2}{2} i$, $-1$, $-\frac{\sqrt 2}{2} - \frac{\sqrt 2}{2} i$, $-i$, $\frac{\sqrt 2}{2} - \frac{\sqrt 2}{2} i$ (from $\cos(\pi/4) = \sin(\pi/4) = \sqrt 2/2$). Notebook 01b, In [10], checks this for $n = 3$ and $n = 8$ and draws the two polygons (Figure 01b.4).

**Conjugation and real numbers (PROVED).** Conjugation changes the sign of the imaginary part and nothing else. Hence: a real number, whose imaginary part is 0, is its own conjugate, $x^* = x$; a list of real numbers does not change at all when every entry is conjugated; conjugating twice gives back the original number, $(z^*)^* = z$; and $(e^{i\alpha})^* = e^{-i\alpha}$, so conjugation turns a rotation into the opposite rotation. The first of these facts has a consequence that the course uses again and again. The author's gamma matrices are real, and fields with real components occur throughout the course. On a real field, complex conjugation does nothing at all. Every operation of the course that does change such a field must therefore be built from a matrix acting on its sixteen components; Chapter 5 derives the charge-conjugation matrices of the theory in exactly this way. Notebook 01b, In [11], checks the four statements.

### 1.13 Boosts, hyperbolic functions, oscillation and growth

**Hyperbolic functions.** The **hyperbolic cosine** and **hyperbolic sine** are

$$
\cosh\varphi = \frac{e^{\varphi} + e^{-\varphi}}{2},\qquad \sinh\varphi = \frac{e^{\varphi} - e^{-\varphi}}{2} .
$$

They obey (PROVED):

$$
\cosh^2\varphi = \frac{e^{2\varphi} + 2 + e^{-2\varphi}}{4},\qquad \sinh^2\varphi = \frac{e^{2\varphi} - 2 + e^{-2\varphi}}{4}
$$

(square the definitions with $(u \pm v)^2 = u^2 \pm 2uv + v^2$, using $e^{\varphi}e^{-\varphi} = e^0 = 1$ and $(e^{\varphi})^2 = e^{2\varphi}$), so

$$
\cosh^2\varphi - \sinh^2\varphi = \frac{2 - (-2)}{4} = 1
$$

(subtract; the terms $e^{\pm 2\varphi}$ cancel). Adding and subtracting the two definitions gives

$$
\cosh\varphi + \sinh\varphi = e^{\varphi},\qquad \cosh\varphi - \sinh\varphi = e^{-\varphi} .
$$

**The addition theorems of cosh and sinh (PROVED).** With $c_1 = \cosh\varphi_1$ and so on,

$$
\cosh\varphi_1\cosh\varphi_2 + \sinh\varphi_1\sinh\varphi_2 = \frac{(e^{\varphi_1} + e^{-\varphi_1})(e^{\varphi_2} + e^{-\varphi_2}) + (e^{\varphi_1} - e^{-\varphi_1})(e^{\varphi_2} - e^{-\varphi_2})}{4}
$$

(the definitions inserted; both products have the denominator $2 \cdot 2$),

$$
= \frac{2e^{\varphi_1 + \varphi_2} + 2e^{-\varphi_1 - \varphi_2}}{4} = \cosh(\varphi_1 + \varphi_2)
$$

(multiplied out, the mixed terms $e^{\varphi_1 - \varphi_2}$ and $e^{-\varphi_1 + \varphi_2}$ appear once with $+$ and once with $-$ and cancel, while $e^{\varphi_1 + \varphi_2}$ and $e^{-\varphi_1 - \varphi_2}$ appear twice; then the definition of $\cosh$). In the same way, $\sinh\varphi_1\cosh\varphi_2 + \cosh\varphi_1\sinh\varphi_2 = \sinh(\varphi_1 + \varphi_2)$: multiplied out, the products give $(e^{\varphi_1 + \varphi_2} + e^{\varphi_1 - \varphi_2} - e^{-\varphi_1 + \varphi_2} - e^{-\varphi_1 - \varphi_2}) + (e^{\varphi_1 + \varphi_2} - e^{\varphi_1 - \varphi_2} + e^{-\varphi_1 + \varphi_2} - e^{-\varphi_1 - \varphi_2})$ over 4, and the mixed terms cancel again.

**Rotations and boosts.** In the author's spacetime there are directions of two kinds: four **space-like** ones, $x_1, x_2, x_3, x_8$, and four **time-like** ones, $x_4, x_5, x_6, x_7$ (Section 1.5; Section 1.27 makes the words exact). A transformation that mixes two directions of the same kind is a rotation, which keeps $x^2 + y^2$. A transformation that mixes a time-like coordinate $t$ with a space-like coordinate $x$ (for example $x_4$ with $x_8$) keeps instead the difference $x^2 - t^2$; it is a **boost**:

$$
\begin{pmatrix} t' \\ x' \end{pmatrix} = \Lambda(\varphi)\begin{pmatrix} t \\ x \end{pmatrix},\qquad \Lambda(\varphi) = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix} .
$$

The number $\varphi$ is the **rapidity** of the boost. Three properties (PROVED). (a) It keeps $-t^2 + x^2$: with $c = \cosh\varphi$ and $s = \sinh\varphi$, $t' = ct + sx$ and $x' = st + cx$ (row times column), and

$$
-t'^2 + x'^2 = -(c^2t^2 + 2cstx + s^2x^2) + (s^2t^2 + 2sctx + c^2x^2) = -(c^2 - s^2)t^2 + (c^2 - s^2)x^2 = -t^2 + x^2
$$

(square with $(u + v)^2 = u^2 + 2uv + v^2$; the mixed terms cancel; collect; $c^2 - s^2 = 1$). With the **frame metric** of this pair, $\eta = \mathrm{diag}(-1, +1)$ (the diagonal matrix with $-1$ for the time-like $t$ and $+1$ for the space-like $x$), this statement is written $\Lambda^T\eta\Lambda = \eta$; Section 1.27 explains this way of writing it. Its determinant is $c^2 - s^2 = 1$. (b) Rapidities add: $\Lambda(\varphi_1)\Lambda(\varphi_2) = \Lambda(\varphi_1 + \varphi_2)$; row times column gives the entries $c_1c_2 + s_1s_2$ and $s_1c_2 + c_1s_2$ (each twice), which are $\cosh(\varphi_1 + \varphi_2)$ and $\sinh(\varphi_1 + \varphi_2)$ by the addition theorems. (c) The two **light-like** directions $(t, x) = (1, 1)$ and $(1, -1)$, on which $-t^2 + x^2 = 0$, are only stretched:

$$
\Lambda(\varphi)\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} c + s \\ s + c \end{pmatrix} = e^{\varphi}\begin{pmatrix} 1 \\ 1 \end{pmatrix},\qquad \Lambda(\varphi)\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} c - s \\ s - c \end{pmatrix} = e^{-\varphi}\begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

(row times column; then $c \pm s = e^{\pm\varphi}$). A boost stretches one light-like direction by the growing exponential $e^{\varphi}$ and shrinks the other by the decaying exponential $e^{-\varphi}$; the product of the two factors is 1. The lengths along space and along the extra times in the author's metric carry the factors $e^{a_4}$ and $e^{-a_4}$, a pattern of the same form; only the form is the same, because $a_4$ is a function of the time $x_4$ and not the rapidity of a boost. Where a rotation moves a point around a circle $x^2 + y^2 = 1$, a boost moves it along a **hyperbola** $t^2 - x^2 = 1$ that never crosses the light-like lines $t = \pm x$ (Figure 01b.5). Notebook 01b, In [12] and In [13], checks (a) to (c) exactly and in numbers.

**Oscillation and growth (PROVED).** For a real number $\varepsilon$, the **frequency**, the wave

$$
e^{-i\varepsilon t} = \cos(\varepsilon t) - i\sin(\varepsilon t)
$$

(Euler's formula with the angle $-\varepsilon t$; the cosine is even, the sine odd) has the modulus 1 at every time $t$: its real and imaginary parts oscillate, and it stays bounded. If the frequency is imaginary, $\varepsilon = i\gamma$ with a real $\gamma$, the same formula gives

$$
e^{-i\varepsilon t} = e^{-i(i\gamma)t} = e^{-i^2\gamma t} = e^{\gamma t}
$$

(insert $\varepsilon = i\gamma$; $i \cdot i = i^2$; $-i^2 = 1$): no oscillation at all, but exponential growth for $\gamma > 0$ and exponential decay for $\gamma < 0$. A complex frequency $\varepsilon = 2 + 0.3i$ gives

$$
e^{-i(2 + 0.3i)t} = e^{-2it - 0.3 i^2 t} = e^{0.3t} e^{-2it}
$$

(multiply out the exponent; $-0.3i^2 = 0.3$; split the exponential with $e^{z + w} = e^z e^w$): an oscillation whose size $e^{0.3t}$ grows. An imaginary part of a frequency is the mathematical sign of an **instability**; Chapter 8 meets it in the waves along the extra times. Notebook 01b, In [14], checks the three cases at 501 times and draws them (Figure 01b.6).

### 1.14 Example: complex numbers, rotations and boosts

Notebook 01b puts Sections 1.10 to 1.13 to work. It computes with complex numbers in Python and exactly with sympy and checks the rules of the conjugate and the modulus for all complex numbers; draws complex numbers as arrows; adds up the exponential series at $i\theta$ term by term and measures how fast it reaches $\cos\theta + i\sin\theta$; confirms $e^{i\pi} = -1$ to 50 digits and proves the law of exponents; turns the letter F by multiplication and by the rotation matrix; checks $J^2 = -I$ and the rules of the rotation matrices; draws the roots of unity; checks that conjugation leaves real numbers unchanged; compares rotations, which keep circles, with boosts, which keep hyperbolas; and shows that a real frequency gives an oscillation and an imaginary one exponential growth. Every check is exact (sympy) or numerical with a stated tolerance; nothing in this notebook comes from the Revision record, and it reads no file. It ends with the line ALL 34 CHECKS PASSED (notebook 01b).

<!-- NOTEBOOK 01b -->

### 1.17 Line-by-line walk-through of Notebook 01b

The notebook has fifteen code cells, In [1] to In [15]. As in Section 1.9, a quoted line `...)` stands for the remaining lines of a figure caption, which Section 1.16 prints in full under its figure.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 1.15. Its code is, line for line, the set-up code of Notebook 01f explained in Section 1.9, with the single difference `NOTEBOOK_ID = "01b"`, so that the figures are named `01b_1_complex_plane.png` and so on and the captions file is `Revision/textbook/figures/01b.captions.json`. It prints one line, Set-up of notebook 01b complete: repository folder found, helpers defined.

**In [2], complex numbers in Python and in sympy.**

```python
import cmath  # functions of complex numbers: phase (the argument), exp
import math  # cos, sin, exp, factorial of real numbers

import mpmath  # numbers with as many digits as we ask for
import numpy as np  # arrays of numbers
import sympy as sp  # exact arithmetic
```

The module `cmath` (part of Python) holds the functions of complex numbers, among them `cmath.phase`, the argument of Section 1.11; `math` holds the same functions for real numbers. mpmath, numpy and sympy were introduced in Section 1.9.

```python
z = 1 + 2j  # Python writes the imaginary unit as j, right after a number
w = 3 - 1j
say(f"Python: z = {z}, w = {w}, z + w = {z + w}, z w = {z * w}")
```

`2j` is Python's spelling of $2i$, so `z` is $1 + 2i$ and `w` is $3 - i$ (`1j` is $i$; a lone `j` would be a variable name). These are floating-point complex numbers: two floating-point numbers, the real and the imaginary part. The line prints `Python: z = (1+2j), w = (3-1j), z + w = (4+1j), z w = (5+5j)`: Python writes a complex number in brackets.

```python
I = sp.I  # sympy's exact imaginary unit
z_exact = 1 + 2 * I
w_exact = 3 - I
product = sp.expand(z_exact * w_exact)  # multiply out, with I**2 = -1
quotient = sp.simplify(z_exact / w_exact)
say(f"sympy: z w = {product}, z / w = {quotient}")
```

`sp.I` is sympy's exact imaginary unit; the name `I` is given to it. `z_exact` and `w_exact` are the same two numbers in exact form. `sp.expand` multiplies out a product (and replaces $i^2$ by $-1$); `sp.simplify` brings the quotient into its simplest form, which for a complex number is real part plus imaginary part. Output: `sympy: z w = 5 + 5*I, z / w = 1/10 + 7*I/10`, the results of Section 1.10.

```python
check(I ** 2 == -1, "i^2 = -1")
check(product == 5 + 5 * I and complex(product) == z * w, "(1 + 2i)(3 - i) = 5 + 5i")
check(sp.simplify(quotient - (1 + 7 * I) / 10) == 0, "(1 + 2i)/(3 - i) = (1 + 7i)/10")
```

Three checks. The first confirms that sympy's unit squares to $-1$. The second compares the exact product with $5 + 5i$ and also with Python's floating-point product (`complex(...)` turns the exact number into a Python complex number). The third confirms the quotient by showing that its difference from $(1 + 7i)/10$ simplifies to 0. Three PASS lines.

**In [3], the rules of the conjugate and the modulus, for all complex numbers.**

```python
a, b, c, d = sp.symbols("a b c d", real=True)  # any real numbers
zz = a + b * I
ww = c + d * I
```

Four sympy symbols for real numbers; `zz` $= a + ib$ and `ww` $= c + id$ stand for any two complex numbers.

```python
check(sp.expand(sp.conjugate(zz * ww) - sp.conjugate(zz) * sp.conjugate(ww)) == 0,
      "(z w)* = z* w* for all complex z and w")
check(sp.expand(zz * sp.conjugate(zz)) == a ** 2 + b ** 2,
      "z z* = a^2 + b^2 = |z|^2 for every z = a + i b")
check(sp.expand(zz * ww * sp.conjugate(zz * ww)
                - (a ** 2 + b ** 2) * (c ** 2 + d ** 2)) == 0,
      "|z w|^2 = |z|^2 |w|^2 for all complex z and w")
```

`sp.conjugate` forms the conjugate. Each check multiplies out the difference of the two sides of one of the three rules of Section 1.10 and requires 0. Because the symbols stand for all real numbers, these are proofs, not tests of examples. Three PASS lines.

```python
say(f"|z| = {sp.Abs(z_exact)}, |w| = {sp.Abs(w_exact)}, "
    f"|z w| = {sp.Abs(product)}")
```

`sp.Abs` is the modulus. Output: `|z| = sqrt(5), |w| = sqrt(10), |z w| = 5*sqrt(2)`, and indeed $\sqrt 5 \cdot \sqrt{10} = \sqrt{50} = 5\sqrt 2$, rule 3.

**In [4], complex numbers as arrows.**

```python
def arrow(ax, number, color, label, start=0j, style="-"):
    """Draw the complex number as an arrow from start to start + number."""
    tip = start + number
    ax.annotate("", xy=(tip.real, tip.imag), xytext=(start.real, start.imag),
                arrowprops={"arrowstyle": "->", "color": color, "lw": 2,
                            "linestyle": style})
    ax.text(tip.real + 0.1, tip.imag + 0.1, label, color=color)
```

A helper that draws a complex number as an arrow. The arguments after the first ones have default values (`start=0j`: the arrow starts at the origin unless another start is given; `style="-"`: a solid line). `.real` and `.imag` are the real and imaginary parts of a Python complex number. `ax.annotate("", xy=..., xytext=...)` draws an arrow without text from the point `xytext` to the point `xy`; the dictionary `arrowprops` sets its look (an arrow head, the colour, the line width 2 and the line style). `ax.text` writes the label a little to the right of and above the tip.

```python
fig, ax = plt.subplots(figsize=(7.0, 5.2))
arrow(ax, z, "tab:blue", "$z = 1 + 2i$")
arrow(ax, w, "tab:red", "$w = 3 - i$")
arrow(ax, w, "tab:red", "", start=z, style="--")  # w moved to the tip of z
arrow(ax, z + w, "black", "$z + w$")
arrow(ax, z.conjugate(), "tab:green", "$z^* = 1 - 2i$")
arrow(ax, 1j * z, "tab:purple", "$iz = -2 + i$")
```

A figure with one pair of axes, then six arrows: $z$, $w$, the arrow $w$ again starting at the tip of $z$ (dashed, `style` set to a string of two hyphens), their sum, the conjugate (`.conjugate()` is Python's conjugate) and $iz$.

```python
ax.axhline(0, color="0.5", lw=0.8)  # the real axis
ax.axvline(0, color="0.5", lw=0.8)  # the imaginary axis
ax.set_xlim(-2.8, 5.0)
ax.set_ylim(-2.6, 3.4)
ax.set_aspect("equal")
ax.set_xlabel("real part Re")
ax.set_ylabel("imaginary part Im")
ax.set_title("Complex numbers as arrows")
save_figure(fig, "complex_plane",
            "Complex numbers as arrows in the complex plane; horizontal axis the "
            ...)
```

The two grey lines are the real and the imaginary axis. `set_xlim` and `set_ylim` fix the ranges; `set_aspect("equal")` makes one unit equally long on both axes, so that right angles look right. The labels, the title and `save_figure` follow. What Figure 01b.1 shows: the sum $z + w$ is the diagonal of the parallelogram spanned by $z$ and $w$; $z^*$ is $z$ mirrored in the real axis; $iz$ is $z$ turned by a right angle.

```python
turn = cmath.phase(1j * z) - cmath.phase(z)  # difference of the two arguments
check(abs(abs(1j * z) - abs(z)) < 1e-15 and abs(turn - math.pi / 2) < 1e-12,
      "multiplying by i keeps the length and turns by pi/2")
```

`cmath.phase` gives the argument in radians; `turn` is how much larger the argument of $iz$ is than that of $z$. `abs` of a Python complex number is its modulus. The check requires the same length to $10^{-15}$ and a turn of $\pi/2$ to $10^{-12}$, the statement of Section 1.10. The output is the figure line and the PASS line.

**In [5], Euler's formula from the exponential series.**

```python
theta = 2.0
target = complex(math.cos(theta), math.sin(theta))  # cos(theta) + i sin(theta)
partial_sums = []
total = 0j
term = 1 + 0j  # the term number 0: (i theta)^0 / 0! = 1
```

The angle $\theta = 2$; `target` is $\cos 2 + i\sin 2$ as a Python complex number (`complex(x, y)` is $x + iy$). The list `partial_sums` will hold $S_0, \dots, S_{20}$; `total` starts at 0 and `term` at the term number 0, which is 1.

```python
for k in range(21):
    total += term
    partial_sums.append(total)  # S_k
    term = term * 1j * theta / (k + 1)  # the next term
errors = [abs(s - target) for s in partial_sums]
```

The loop runs for $k = 0$ to 20: it adds the current term, stores the partial sum $S_k$, and makes the next term from the current one, $(i\theta)^{k+1}/(k+1)! = \frac{(i\theta)^k}{k!}\cdot\frac{i\theta}{k + 1}$ (one more factor $i\theta$ and one more factor $k + 1$ in the factorial). Making each term from the previous one avoids computing large powers and factorials. `errors` holds the 21 errors $|S_N - e^{2i}|$.

```python
bounds = [math.exp(theta) * theta ** (n + 1) / math.factorial(n + 1)
          for n in range(21)]
for n in (0, 1, 2, 5, 10, 15, 20):
    say(f"N = {n:2d}: S_N = {partial_sums[n].real:+.12f} {partial_sums[n].imag:+.12f} i,"
        f" error {errors[n]:.1e}")
say(f"cos 2 + i sin 2 = {target.real:+.12f} {target.imag:+.12f} i")
```

`bounds` holds the bound $e^\theta\theta^{N+1}/(N + 1)!$ of Section 1.11 for $N = 0$ to 20. Seven partial sums are printed with 12 digits after the point and a sign (`:+.12f`), with their errors. The output shows $S_0 = 1$, $S_1 = 1 + 2i$, $S_2 = -1 + 2i$, and then the partial sums settling: $S_{20} = -0.416146836547 + 0.909297426826\,i$, equal in all printed digits to $\cos 2 + i\sin 2$, with the error $4.1 \times 10^{-14}$; the errors are 1.7, 1.8, 1.2, 0.086, $5.1 \times 10^{-5}$, $3.1 \times 10^{-9}$, $4.1 \times 10^{-14}$. The first errors do not shrink, because for $k < \theta$ the terms still grow.

```python
check(all(e <= b + 1e-15 for e, b in zip(errors, bounds)),
      "the error of every partial sum is below e^theta theta^(N+1)/(N+1)!")
report("error of the series for e^(2i) after 21 terms", f"{errors[20]:.1e}")
check(errors[20] < 1e-12, "21 terms of the series give cos 2 + i sin 2 to 1e-12")
```

The first check compares every error with its bound (the extra $10^{-15}$ allows for the rounding of the floating-point numbers themselves). The RESULT line prints $4.1 \times 10^{-14}$, and the last check requires it to be below $10^{-12}$. Two PASS lines.

**In [6], the picture of the series.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.6))
circle = np.exp(1j * np.linspace(0.0, 2.0 * np.pi, 400))  # the unit circle
left.plot(circle.real, circle.imag, color="0.7", lw=1, label="unit circle")
```

Two panels side by side. `np.linspace(0.0, 2.0 * np.pi, 400)` gives 400 angles from 0 to $2\pi$; `np.exp(1j * ...)` turns them into the points $e^{i\theta}$ of the unit circle (numpy computes complex exponentials entry by entry); `.real` and `.imag` of a numpy array are the arrays of the real and imaginary parts. The circle is drawn in light grey.

```python
first = np.array(partial_sums[:11])
left.plot(first.real, first.imag, "o-", color="tab:blue",
          label="partial sums $S_0, \\dots, S_{10}$")
for n in range(5):  # number the first five points
    left.text(first[n].real + 0.06, first[n].imag + 0.06, f"$S_{n}$")
left.plot([target.real], [target.imag], "*", color="tab:red", ms=14,
          label="$e^{2i} = \\cos 2 + i \\sin 2$")
```

The first eleven partial sums as an array, drawn as points joined in order; the first five are labelled $S_0$ to $S_4$; the target $e^{2i}$ is a large red star (`"*"`, marker size 14).

```python
left.set_aspect("equal")
left.set_xlabel("real part")
left.set_ylabel("imaginary part")
left.set_title("Partial sums of the series of $e^{2i}$")
left.legend(loc="lower left", fontsize=8)
right.semilogy(range(21), errors, "o-", label="error $|S_N - e^{2i}|$")
right.semilogy(range(21), bounds, "--", label="bound $e^2 \\, 2^{N+1}/(N+1)!$")
right.set_xlabel("number $N$ of the last term")
right.set_ylabel("error (logarithmic scale)")
right.set_title("How fast the series converges")
right.legend()
fig.tight_layout()
save_figure(fig, "euler_series",
            "Left: the partial sums $S_N = \\sum_{k=0}^{N} (2i)^k/k!$ for $N = 0$ to "
            ...)
```

Labels for the left panel; on the right the 21 errors and the 21 bounds against $N$ with a logarithmic vertical axis (`semilogy`), the bound dashed (the style string of two hyphens). What Figure 01b.2 shows: on the left the partial sums turn around the origin and close in on the star; on the right the errors fall ever faster and stay below the dashed bound.

```python
step_ratios = [errors[n + 1] / errors[n] for n in range(10, 20)]
check(all(abs(ratio - theta / (n + 2)) < 0.1 * theta / (n + 2)
          for ratio, n in zip(step_ratios, range(10, 20))),
      "from N to N + 1 the error is multiplied by about theta/(N + 2) (N = 10 to 19)")
```

`step_ratios` are the ten ratios of the error at $N + 1$ to the error at $N$ for $N = 10$ to 19; the check requires each to lie within 10 per cent of $\theta/(N + 2)$, the factor derived in Section 1.11. One PASS line.

**In [7], 50 digits and the law of exponents.**

```python
mpmath.mp.dps = 50  # work with 50 significant digits
i_mp = mpmath.mpc(0, 1)  # the imaginary unit as an mpmath number
euler_gap = abs(mpmath.exp(i_mp * 2) - (mpmath.cos(2) + i_mp * mpmath.sin(2)))
pi_gap = abs(mpmath.exp(i_mp * mpmath.pi) + 1)
e_i_pi = mpmath.exp(i_mp * mpmath.pi)
```

`mpmath.mpc(0, 1)` is the complex number $0 + 1i$ in mpmath, computed with 50 digits. `euler_gap` is the size of $e^{2i} - (\cos 2 + i\sin 2)$, `pi_gap` the size of $e^{i\pi} + 1$, and `e_i_pi` the number $e^{i\pi}$ itself.

```python
# pi itself is stored with 50 digits, so a tiny imaginary part of about 1e-51 is
# left over: the rounding of pi, not a failure of the formula.
say(f"e^(i pi): real part {mpmath.nstr(e_i_pi.real, 30)}, imaginary part of size "
    f"{mpmath.nstr(abs(e_i_pi.imag), 2)}")
check(euler_gap < mpmath.mpf("1e-45") and pi_gap < mpmath.mpf("1e-45"),
      "mpmath, 50 digits: e^(2i) = cos 2 + i sin 2 and e^(i pi) = -1")
```

The comment explains the leftover imaginary part. The line prints e^(i pi): real part -1.0, imaginary part of size 1.0e-51 (`mpmath.nstr` writes a number with the given count of significant digits and drops needless zeros, so $-1$ appears as -1.0). The check requires both gaps to be below $10^{-45}$.

```python
alpha, beta = sp.symbols("alpha beta", real=True)
left_side = sp.expand((sp.cos(alpha) + I * sp.sin(alpha))
                      * (sp.cos(beta) + I * sp.sin(beta)))
right_side = sp.expand(sp.expand_trig(sp.cos(alpha + beta) + I * sp.sin(alpha + beta)))
check(sp.expand(left_side - right_side) == 0,
      "sympy: e^(i alpha) e^(i beta) = e^(i (alpha + beta)) for all real angles")
```

The proof of the law of exponents of Section 1.11 with sympy: `left_side` is $(\cos\alpha + i\sin\alpha)(\cos\beta + i\sin\beta)$ multiplied out; `sp.expand_trig` writes $\cos(\alpha + \beta)$ and $\sin(\alpha + \beta)$ with the addition theorems, and `right_side` is the result multiplied out. Their difference is 0 for all angles. The cell prints two PASS lines.

**In [8], multiplication turns the letter F.**

```python
letter_f = np.array([0, 2j, 1.2 + 2j, 1.2 + 1.6j, 0.4 + 1.6j, 0.4 + 1.1j, 1.0 + 1.1j,
                     1.0 + 0.7j, 0.4 + 0.7j, 0.4, 0]) + (0.3 + 0.2j)  # corners
```

The eleven corners of the outline of a letter F as complex numbers (the last one repeats the first, to close the outline); adding $0.3 + 0.2i$ to the array shifts every corner a little away from the origin, so that no corner is the origin itself.

```python
factors = [(1, "original", "black"),
           (np.exp(1j * np.pi / 3), "times $e^{i\\pi/3}$", "tab:blue"),
           (np.exp(5j * np.pi / 6), "times $e^{5i\\pi/6}$", "tab:red"),
           (0.6 * np.exp(-1j * np.pi / 2), "times $0.6\\,e^{-i\\pi/2}$", "tab:green")]
```

Four factors with their labels and colours: 1 (the original), $e^{i\pi/3}$ (a turn by 60 degrees), $e^{5i\pi/6}$ (150 degrees) and $0.6\,e^{-i\pi/2}$ (a quarter turn clockwise and a shrinking to 0.6).

```python
fig, ax = plt.subplots(figsize=(8.4, 6.0))
for factor, label, color in factors:
    image = factor * letter_f  # every corner multiplied by the factor
    ax.fill(image.real, image.imag, color=color, alpha=0.35, label=label)
    ax.plot(image.real, image.imag, color=color, lw=1)
ax.plot([0], [0], "k+", ms=12)  # the origin, the centre of the rotations
```

For each factor every corner is multiplied (numpy multiplies an array entry by entry), and `ax.fill` paints the inside of the outline, 35 per cent opaque (`alpha=0.35`), while `ax.plot` draws its edge. A black cross marks the origin.

```python
ax.set_aspect("equal")
ax.set_xlabel("real part")
ax.set_ylabel("imaginary part")
ax.set_title("Multiplication by a complex number")
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=9)
save_figure(fig, "rotation_by_multiplication",
            "The letter F (black) and its images after multiplying every corner by "
            ...)
```

The legend is placed outside the axes, to the right (`bbox_to_anchor=(1.02, 0.5)` names a point just right of the axes at half their height). What Figure 01b.3 shows: four copies of the letter, turned about the origin and once shrunk, never mirrored.

```python
rotations_ok = True
for alpha_value in (np.pi / 3, 5 * np.pi / 6):
    image = np.exp(1j * alpha_value) * letter_f
    rotations_ok &= bool(np.max(np.abs(np.abs(image) - np.abs(letter_f))) < 1e-14)
    turned = np.angle(image / letter_f)  # the change of every angle
    rotations_ok &= bool(np.max(np.abs(turned - alpha_value)) < 1e-12)
check(rotations_ok, "multiplying by e^(i alpha) keeps lengths and adds alpha to "
      "every angle")
```

For the two pure rotations: `np.abs` of a complex array is the array of the moduli, so the first condition requires every corner to keep its distance from the origin; `np.angle(image / letter_f)` is the argument of the quotient of each image corner and its original, which is the change of its angle, and the second condition requires it to be $\alpha$. One PASS line.

**In [9], the same turns as real 2 × 2 matrices.**

```python
def M(re_part, im_part):
    """The real 2 x 2 matrix of the complex number re_part + i im_part."""
    return sp.Matrix([[re_part, -im_part], [im_part, re_part]])


J = M(0, 1)  # the matrix of i
check(J * J == -sp.eye(2), "J J = -I: the real matrix J behaves like i")
```

`sp.Matrix([[...], [...]])` makes a sympy matrix from the list of its rows; `M` builds the matrix with the rows $(a, -b)$ and $(b, a)$ of Section 1.12. `J` is the matrix of $i$; `*` between sympy matrices is the matrix product, and `sp.eye(2)` is the $2 \times 2$ identity. The check is $J^2 = -I$.

```python
zw_re, zw_im = a * c - b * d, a * d + b * c  # z w = (ac - bd) + i (ad + bc)
check((M(a, b) * M(c, d) - M(zw_re, zw_im)).expand() == sp.zeros(2, 2),
      "M(z) M(w) = M(z w) for all complex z and w")
check(sp.expand(M(a, b).det()) == a ** 2 + b ** 2, "det M(a + i b) = a^2 + b^2")
```

With the real symbols $a, b, c, d$ of In [3]: the real and imaginary parts of $zw$; then the product rule $M(z)M(w) = M(zw)$ (`sp.zeros(2, 2)` is the $2 \times 2$ matrix of zeros) and the determinant $a^2 + b^2$ (`.det()` is sympy's determinant), both for all values of the symbols.

```python
def R(angle):
    """The rotation matrix of the angle: the matrix of e^(i angle)."""
    return M(sp.cos(angle), sp.sin(angle))


product_rule = (R(alpha) * R(beta) - R(alpha + beta)).applyfunc(sp.expand_trig)
check(product_rule.expand() == sp.zeros(2, 2), "R(alpha) R(beta) = R(alpha + beta)")
```

`R` builds the rotation matrix. `.applyfunc(f)` applies the function `f` to every entry of a matrix; here `sp.expand_trig` writes the entries of $R(\alpha + \beta)$ with the addition theorems, and after multiplying out every entry of the difference is 0: two turns make one.

```python
check(sp.simplify(R(alpha).det()) == 1 and
      (R(alpha).T * R(alpha)).applyfunc(sp.simplify) == sp.eye(2),
      "det R(alpha) = 1 and R(alpha)^T R(alpha) = I")
```

`.T` is the transpose. The check is properties (b) and (c) of Section 1.12.

```python
rotation = np.array(R(sp.pi / 3).evalf(), dtype=float)  # R(pi/3) as numbers
corners = np.array([letter_f.real, letter_f.imag])  # 2 rows: x and y of each corner
by_matrix = rotation @ corners
by_number = np.exp(1j * np.pi / 3) * letter_f
check(np.max(np.abs(by_matrix[0] + 1j * by_matrix[1] - by_number)) < 1e-14,
      "the rotation matrix R(pi/3) moves the corners exactly like e^(i pi/3)")
```

`.evalf()` turns the exact matrix $R(\pi/3)$ into decimal numbers, and `np.array(..., dtype=float)` into a numpy array of floating-point numbers. `corners` is a table with two rows, the $x$ and the $y$ coordinates of the eleven corners; `rotation @ corners` multiplies the matrix with every column at once (`@` is numpy's matrix product; Section 1.18 treats it in full). `by_matrix[0] + 1j * by_matrix[1]` turns the two rows back into complex numbers, which must agree with the corners multiplied by $e^{i\pi/3}$ to $10^{-14}$. The cell prints six PASS lines.

**In [10], the roots of unity.**

```python
for n in (3, 8):
    roots = np.exp(2j * np.pi * np.arange(n) / n)  # e^(2 pi i k/n), k = 0 ... n-1
    check(np.max(np.abs(roots ** n - 1)) < 1e-12 and abs(roots.sum()) < 1e-12,
          f"the {n} roots of unity of order {n}: z^{n} = 1 and their sum is 0")
```

For $n = 3$ and $n = 8$: `np.arange(n)` is $0, \dots, n - 1$, so `roots` holds the $n$ roots of unity; the check requires every $n$-th power to be 1 and the sum to be 0, both to $10^{-12}$. Two PASS lines, whose texts contain the value of `n` (an f-string).

```python
eighth = [sp.expand_complex(sp.exp(2 * sp.pi * I * k / 8)) for k in range(8)]
say("the eighth roots of unity, exactly: " + ", ".join(str(r) for r in eighth))
check(all(sp.simplify(r ** 8 - 1) == 0 for r in eighth) and
      sp.simplify(sum(eighth)) == 0,
      "sympy: each exact eighth root has eighth power 1, and they add up to 0")
```

The eight roots exactly: `sp.expand_complex` writes $e^{2\pi ik/8}$ as real part plus $i$ times imaginary part. They are printed (`", ".join(...)` joins the texts with a comma and a blank): `1, sqrt(2)/2 + sqrt(2)*I/2, I`, and so on, the list of Section 1.12. The check proves the two properties exactly.

```python
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.8))
for ax, n in zip(axes, (3, 8)):
    roots = np.exp(2j * np.pi * np.arange(n + 1) / n)  # the first root again at the end
    ax.plot(circle.real, circle.imag, color="0.75", lw=1)
    ax.plot(roots.real, roots.imag, "o-", color="tab:blue")
    for k in range(n):
        arrow(ax, roots[k], "tab:blue", f"$z_{k}$")
```

Two panels, one for $n = 3$ and one for $n = 8$. With `np.arange(n + 1)` the list ends with the first root again ($k = n$ gives $e^{2\pi i} = 1$), so that the line through the points closes the polygon. The unit circle of In [6] is drawn in grey, the polygon in blue, and each root as a labelled arrow from the origin, with the helper of In [4].

```python
    ax.set_aspect("equal")
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.35, 1.35)
    ax.set_xlabel("real part")
    ax.set_ylabel("imaginary part")
    ax.set_title(f"the {n} roots of $z^{n} = 1$")
fig.tight_layout()
save_figure(fig, "roots_of_unity",
            "The roots of unity $z_k = e^{2\\pi i k/n}$ for $n = 3$ (left) and "
            ...)
```

Equal scales, ranges, labels and a title on each panel; then the figure is saved. What Figure 01b.4 shows: a regular triangle and a regular octagon inscribed in the unit circle; the arrows of each picture add up to zero, as proved in Section 1.12. The cell prints three PASS lines, the exact roots and the figure line.

**In [11], conjugation and real numbers.**

```python
v_real = np.array([0.5, -2.0, 3.0])  # a list of real numbers
v_complex = np.array([1 + 2j, -1j, 4.0])  # a list with imaginary parts
check((v_real.conj() == v_real).all(),
      "conjugation leaves a list of real numbers unchanged")
check(not (v_complex.conj() == v_complex).all(),
      "conjugation changes a list whose imaginary parts are not all 0")
check((v_complex.conj().conj() == v_complex).all(),
      "conjugating twice gives back the original list")
check(abs(np.exp(0.7j).conjugate() - np.exp(-0.7j)) < 1e-15,
      "the conjugate of e^(i alpha) is e^(-i alpha)")
```

`.conj()` conjugates every entry of a numpy array; `==` between two arrays compares entry by entry, and `.all()` is true when every comparison is true. The four checks are the four statements of Section 1.12: a real list is unchanged; a list with imaginary parts changes (`not` turns true into false and back); conjugating twice restores the list; and $(e^{0.7i})^* = e^{-0.7i}$. Four PASS lines.

**In [12], boosts, exactly.**

```python
phi, phi1, phi2 = sp.symbols("phi phi1 phi2", real=True)


def boost(rapidity):
    """The boost matrix acting on the pair (t, x)."""
    return sp.Matrix([[sp.cosh(rapidity), sp.sinh(rapidity)],
                      [sp.sinh(rapidity), sp.cosh(rapidity)]])
```

Three real symbols for rapidities, and a function that builds the boost $\Lambda(\varphi)$ of Section 1.13.

```python
eta_tx = sp.diag(-1, 1)  # t time-like (-1), x space-like (+1)
L = boost(phi)
check((L.T * eta_tx * L - eta_tx).applyfunc(sp.simplify) == sp.zeros(2, 2) and
      sp.simplify(L.det()) == 1,
      "a boost keeps -t^2 + x^2 (Lambda^T eta Lambda = eta) and has det 1")
```

`sp.diag(-1, 1)` is the diagonal matrix $\eta = \mathrm{diag}(-1, +1)$. The check computes $\Lambda^T\eta\Lambda - \eta$, simplifies every entry (sympy knows $\cosh^2 - \sinh^2 = 1$) and requires the zero matrix, and requires $\det\Lambda = 1$: property (a).

```python
added = (boost(phi1) * boost(phi2) - boost(phi1 + phi2)).applyfunc(sp.expand_trig)
check(added.expand() == sp.zeros(2, 2), "rapidities add: boost(phi1) boost(phi2) = "
      "boost(phi1 + phi2)")
```

Property (b): `expand_trig` also knows the addition theorems of $\cosh$ and $\sinh$.

```python
light_plus = (L * sp.Matrix([1, 1]) - sp.exp(phi) * sp.Matrix([1, 1]))
light_minus = (L * sp.Matrix([1, -1]) - sp.exp(-phi) * sp.Matrix([1, -1]))
# rewrite(sp.exp) writes cosh and sinh with exponentials, then simplify:
check(light_plus.applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp)))
      == sp.zeros(2, 1) and
      light_minus.applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp)))
      == sp.zeros(2, 1),
      "the light-like directions are stretched by e^phi and by e^(-phi)")
```

Property (c): `sp.Matrix([1, 1])` is the column $(1, 1)$. `light_plus` is $\Lambda(1, 1) - e^{\varphi}(1, 1)$ and `light_minus` is $\Lambda(1, -1) - e^{-\varphi}(1, -1)$. A `lambda e: ...` is a function without a name, written in one line: it takes an entry `e`, rewrites $\cosh$ and $\sinh$ with exponentials (their definitions) and simplifies. Both differences must be zero columns (`sp.zeros(2, 1)`). The cell prints three PASS lines.

**In [13], circles and hyperbolas.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 5.0))
angles = np.linspace(0.0, 2.0 * np.pi, 400)
left.plot(np.cos(angles), np.sin(angles), color="tab:blue",
          label="rotations of $(1, 0)$")
marks = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
left.plot(np.cos(marks), np.sin(marks), "o", color="tab:blue")
for value in marks:
    left.text(1.06 * np.cos(value), 1.06 * np.sin(value), f"{value:+.1f}", fontsize=8)
```

The point $(1, 0)$ turned by an angle $\alpha$ is $R(\alpha)(1, 0) = (\cos\alpha, \sin\alpha)$; for 400 angles from 0 to $2\pi$ these points make the circle. Five angles $-1, -0.5, 0, 0.5, 1$ are marked with dots and labelled just outside the circle (the factor 1.06 moves the label outwards).

```python
left.set_aspect("equal")
left.set_xlim(-1.6, 1.6)
left.set_ylim(-1.6, 1.6)
left.set_xlabel("$x$")
left.set_ylabel("$y$")
left.set_title("rotation: $x^2 + y^2$ stays 1")
left.legend(loc="lower left", fontsize=8)
```

Equal scales, ranges, labels, title and legend of the left panel.

```python
rapidities = np.linspace(-2.0, 2.0, 400)
right.plot(np.sinh(rapidities), np.cosh(rapidities), color="tab:red",
           label="boosts of $(t, x) = (1, 0)$")
right.plot(np.sinh(marks), np.cosh(marks), "o", color="tab:red")
```

The event $(t, x) = (1, 0)$ boosted with rapidity $\varphi$ is $\Lambda(\varphi)(1, 0) = (\cosh\varphi, \sinh\varphi)$; it is drawn with $x = \sinh\varphi$ on the horizontal and $t = \cosh\varphi$ on the vertical axis, for 400 rapidities from $-2$ to 2, with dots at the five marked rapidities.

```python
for value in marks:  # labels left of the points on the left half, right otherwise
    shift = 0.12 if value >= 0 else -0.62
    right.text(np.sinh(value) + shift, np.cosh(value) + 0.12, f"{value:+.1f}",
               fontsize=8)
```

The labels of the dots are put to the right of the points on the right half and to the left on the left half, so that they do not cover the curve (`a if condition else b` takes `a` when the condition holds and `b` otherwise).

```python
edge = np.linspace(-3.8, 3.8, 2)
right.plot(edge, edge, "k--", lw=1, label="light-like lines $t = \\pm x$")
right.plot(edge, -edge, "k--", lw=1)
```

`edge` holds the two numbers $-3.8$ and 3.8; the two dashed black lines through $(-3.8, -3.8)$, $(3.8, 3.8)$ and through $(-3.8, 3.8)$, $(3.8, -3.8)$ are the light-like lines $t = x$ and $t = -x$.

```python
right.set_aspect("equal")
right.set_xlim(-3.8, 3.8)
right.set_ylim(-0.5, 3.9)
right.set_xlabel("space-like coordinate $x$")
right.set_ylabel("time-like coordinate $t$")
right.set_title("boost: $t^2 - x^2$ stays 1")
right.legend(loc="lower right", fontsize=8)
fig.tight_layout()
save_figure(fig, "rotations_and_boosts",
            "Left: the point $(1, 0)$ rotated by all angles from 0 to $2\\pi$ "
            ...)
```

Scales, ranges, labels and legend of the right panel, then the figure. What Figure 01b.5 shows: the rotated point runs around a circle; the boosted event runs along the upper branch of the hyperbola $t^2 - x^2 = 1$, which comes ever closer to the dashed light-like lines but never crosses them.

```python
on_hyperbola = np.cosh(rapidities) ** 2 - np.sinh(rapidities) ** 2
check(np.max(np.abs(on_hyperbola - 1)) < 1e-12,
      "numbers: cosh^2 - sinh^2 = 1 at 400 rapidities from -2 to 2")
```

The check computes $\cosh^2\varphi - \sinh^2\varphi$ at the 400 rapidities and requires 1 to $10^{-12}$. One PASS line.

**In [14], oscillation and growth.**

```python
t = np.linspace(0.0, 10.0, 501)
wave = np.exp(-1j * 2.0 * t)  # real frequency 2
growing = np.exp(-1j * (0.3j) * t)  # imaginary frequency 0.3 i
decaying = np.exp(-1j * (-0.3j) * t)  # imaginary frequency -0.3 i
mixed = np.exp(-1j * (2.0 + 0.3j) * t)  # complex frequency 2 + 0.3 i
```

501 times from 0 to 10, and the wave $e^{-i\varepsilon t}$ for the four frequencies of Section 1.13: 2, $0.3i$, $-0.3i$ and $2 + 0.3i$.

```python
check(np.max(np.abs(np.abs(wave) - 1.0)) < 1e-14,
      "real frequency: |e^(-i eps t)| = 1 at every time")
check(np.max(np.abs(growing - np.exp(0.3 * t))) < 1e-12 * np.exp(3.0),
      "imaginary frequency 0.3 i: e^(-i eps t) = e^(0.3 t), real and growing")
check(np.max(np.abs(np.abs(mixed) - np.exp(0.3 * t))) < 1e-12 * np.exp(3.0),
      "complex frequency 2 + 0.3 i: the size of the wave is e^(0.3 t)")
```

The three statements of Section 1.13: modulus 1 for the real frequency; $e^{0.3t}$ for the imaginary one; size $e^{0.3t}$ for the complex one. The tolerance $10^{-12}e^{3}$ is relative to the largest value $e^{0.3 \cdot 10} = e^3 \approx 20$. Three PASS lines.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.4))
left.plot(t, wave.real, label="real part $\\cos 2t$")
left.plot(t, wave.imag, "--", label="imaginary part $-\\sin 2t$")
left.plot(t, np.abs(wave), color="black", lw=2, label="modulus $= 1$")
left.set_xlabel("time $t$")
left.set_ylabel("value")
left.set_title("real frequency $\\varepsilon = 2$")
left.set_ylim(-1.75, 1.3)  # room below the curves for the legend
left.legend(loc="lower center", ncol=3, fontsize=8)
```

The left panel: the real part, the imaginary part (dashed) and the modulus (thick black) of the wave with the real frequency 2. The vertical range leaves room below the curves for a legend in three columns (`ncol=3`).

```python
right.plot(t, growing.real, color="tab:red", lw=2,
           label="$\\varepsilon = 0.3i$: $e^{0.3t}$")
right.plot(t, decaying.real, color="tab:blue", lw=2,
           label="$\\varepsilon = -0.3i$: $e^{-0.3t}$")
right.plot(t, mixed.real, color="tab:green",
           label="$\\varepsilon = 2 + 0.3i$: real part")
right.plot(t, -np.exp(0.3 * t), ":", color="tab:red")  # the lower envelope
right.set_xlabel("time $t$")
right.set_ylabel("value")
right.set_title("imaginary and complex frequencies")
right.legend(loc="upper left", fontsize=8)
fig.tight_layout()
save_figure(fig, "oscillation_and_growth",
            "Left: the wave $e^{-i\\varepsilon t}$ with the real frequency "
            ...)
```

The right panel: the growing and the decaying wave (both real), the real part of the wave with the complex frequency, and the dotted red curve $-e^{0.3t}$, which with the solid red curve $e^{0.3t}$ encloses the growing oscillation. What Figure 01b.6 shows: on the left a steady oscillation of constant size; on the right one curve growing, one decaying, and an oscillation whose swings grow between $\pm e^{0.3t}$.

**In [15], the last check.**

```python
figure_names = ["01b_1_complex_plane.png", "01b_2_euler_series.png",
                "01b_3_rotation_by_multiplication.png", "01b_4_roots_of_unity.png",
                "01b_5_rotations_and_boosts.png", "01b_6_oscillation_and_growth.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all 6 figure files of this notebook exist")
all_checks_passed()
```

As in Notebook 01f: the six figure files must exist, and the last line is printed, ALL 34 CHECKS PASSED (notebook 01b). The 34 checks are: 3 in In [2], 3 in In [3], 1 in In [4], 2 in In [5], 1 in In [6], 2 in In [7], 1 in In [8], 6 in In [9], 3 in In [10], 4 in In [11], 3 in In [12], 1 in In [13], 3 in In [14] and 1 in In [15].

### 1.18 Vectors and matrices; the matrix product

**Vectors.** A **vector** is an ordered list of numbers, such as $v = (1, 2, 0)$; the numbers are its **components**, and $v$ has three of them. The fields of the course have sixteen components at every point, so at each point a field is a vector with sixteen components. Vectors with the same number of components are added component by component, and a vector is multiplied by a number $c$ by multiplying every component:

$$
(v + w)_i = v_i + w_i,\qquad (cv)_i = c\, v_i .
$$

The **dot product** of two vectors with $n$ components is the number

$$
v \cdot w = \sum_{i = 1}^{n} v_i w_i = v_1 w_1 + v_2 w_2 + \dots + v_n w_n .
$$

The symbol $\sum$ (the capital Greek letter sigma) abbreviates a sum: $\sum_{i=1}^{n} t_i$ means $t_1 + t_2 + \dots + t_n$, and the letter $i$ under it, the **index** of the sum, runs through the whole numbers from 1 to $n$. For $v = (1, 2, 0)$ and $w = (0, 1, 1)$: $v + w = (1, 3, 1)$, $3v = (3, 6, 0)$ and $v \cdot w = 1 \cdot 0 + 2 \cdot 1 + 0 \cdot 1 = 2$.

**Matrices.** A **matrix** with $m$ rows and $n$ columns, an $m \times n$ matrix, is a rectangular table of numbers $A_{ij}$: the first index $i = 1, \dots, m$ numbers the row (counted downwards), the second $j = 1, \dots, n$ the column (counted to the right). It is **square** if $m = n$. Python counts from 0, so the entry $A_{23}$ in row 2 and column 3 is `A[1, 2]` in Python. A vector with $n$ components may be written as a column, an $n \times 1$ matrix.

**Matrix times vector.** An $m \times n$ matrix $A$ turns a vector $v$ with $n$ components into a vector $Av$ with $m$ components:

$$
(Av)_i = \sum_{j = 1}^{n} A_{ij} v_j ,
$$

component $i$ of $Av$ is row $i$ of $A$ times $v$, entry by entry, added up (the rule of Section 1.12 for $2 \times 2$ matrices). For the $3 \times 3$ matrix $A$ with the rows $(1, 2, 0)$, $(0, 1, 1)$, $(1, 3, 1)$ and $v = (1, 2, 0)$:

$$
Av = \begin{pmatrix} 1 \cdot 1 + 2 \cdot 2 + 0 \cdot 0 \\ 0 \cdot 1 + 1 \cdot 2 + 1 \cdot 0 \\ 1 \cdot 1 + 3 \cdot 2 + 1 \cdot 0 \end{pmatrix} = \begin{pmatrix} 5 \\ 2 \\ 7 \end{pmatrix}
$$

(each row times the column $v$). The map $v \mapsto Av$ is **linear**: $A(v + w) = Av + Aw$ and $A(cv) = c\,Av$, because $\sum_j A_{ij}(v_j + w_j) = \sum_j A_{ij}v_j + \sum_j A_{ij}w_j$ and $\sum_j A_{ij}(c v_j) = c\sum_j A_{ij}v_j$ (multiply out inside the sum; a common factor comes out of a sum).

**The matrix product (PROVED).** The product of an $m \times n$ matrix $A$ and an $n \times p$ matrix $B$ is the $m \times p$ matrix

$$
(AB)_{ik} = \sum_{j = 1}^{n} A_{ij} B_{jk} ,
$$

entry $(i, k)$ is row $i$ of $A$ times column $k$ of $B$. It is made so that $(AB)v = A(Bv)$ for every vector $v$:

$$
\big(A(Bv)\big)_i = \sum_j A_{ij}(Bv)_j = \sum_j A_{ij}\sum_k B_{jk}v_k = \sum_k\Big(\sum_j A_{ij}B_{jk}\Big)v_k = \big((AB)v\big)_i
$$

(the rule of matrix times vector, twice; the factor $A_{ij}$ moved into the inner sum and the two sums exchanged, which only re-orders the terms of a finite sum; the definition of $AB$). With the matrix $A$ above and $B$ with the rows $(0, 1, 0)$, $(1, 0, 2)$, $(0, 1, 1)$:

$$
AB = \begin{pmatrix} 2 & 1 & 4 \\ 1 & 1 & 3 \\ 3 & 2 & 7 \end{pmatrix},\qquad BA = \begin{pmatrix} 0 & 1 & 1 \\ 3 & 8 & 2 \\ 1 & 4 & 2 \end{pmatrix}
$$

(for example the entry in row 1, column 3 of $AB$ is $1 \cdot 0 + 2 \cdot 2 + 0 \cdot 1 = 4$, and that of $BA$ is $0 \cdot 0 + 1 \cdot 1 + 0 \cdot 1 = 1$). The two products differ: **matrix multiplication is not commutative**, $AB \neq BA$ in general. The order of the factors matters in every matrix formula of the course. The product is, however, **associative**, $(AB)C = A(BC)$, because both sides have the entries $\sum_j\sum_k A_{ij}B_{jk}C_{kl}$, and **distributive**, $A(B + C) = AB + AC$ (multiply out inside the sum).

**The summation convention, a first look.** In $(AB)_{ik} = \sum_j A_{ij}B_{jk}$ the index $j$ appears twice in the product and is summed; $i$ and $k$ appear once and are not summed. The course writes such sums without the sign $\sum$: an index that appears twice in one product is summed over all its values. So $A_{ij}B_{jk}$ means $\sum_j A_{ij}B_{jk}$. A summed index is called a **dummy** index (its name does not matter: $A_{ij}B_{jk} = A_{il}B_{lk}$), an index that is not summed a **free** index (the formula holds for each of its values). numpy's function `einsum` reads this convention literally: `np.einsum("ij,jk->ik", A, B)` says "the first factor has the indices $i, j$, the second $j, k$; $j$ appears twice and is summed; the result has the indices $i, k$". Section 1.26 develops the convention fully, with upper and lower indices.

**Identity, transpose and trace (PROVED).** The **identity matrix** $I$ is the square matrix with 1 on the diagonal and 0 elsewhere; its entries are the **Kronecker delta**, $\delta_{ij} = 1$ if $i = j$ and 0 otherwise, and $IA = AI = A$. The **transpose** $A^T$ has the rows and columns exchanged, $(A^T)_{ij} = A_{ji}$. The transpose of a product is the product of the transposes in the opposite order:

$$
\big((AB)^T\big)_{ki} = (AB)_{ik} = \sum_j A_{ij}B_{jk} = \sum_j (B^T)_{kj}(A^T)_{ji} = (B^TA^T)_{ki}
$$

(the definition of the transpose; the matrix product; each factor written with its transpose, re-ordered, since numbers commute; the matrix product of $B^T$ and $A^T$). The **trace** of a square matrix is the sum of its diagonal entries, $\mathrm{tr}\,A = \sum_i A_{ii}$. Although $AB \neq BA$, the two products have the same trace:

$$
\mathrm{tr}(AB) = \sum_i\sum_j A_{ij}B_{ji} = \sum_j\sum_i B_{ji}A_{ij} = \mathrm{tr}(BA)
$$

(the diagonal entries of $AB$, added; the order of the two sums and of the two factors exchanged; the diagonal entries of $BA$, added). In the example both traces are 10 ($2 + 1 + 7$ and $0 + 8 + 2$). Notebook 01a, In [2] to In [5], computes all of this three ways (with loops, with `einsum`, with numpy's operator `@`) and draws the four matrices as **heat maps**, pictures in which every entry is a coloured square (Figure 01a.1).

### 1.19 Permutations and their signs

**Permutations.** A **permutation** of $n$ objects is a re-ordering of them. We take the objects to be the numbers $0, 1, \dots, n - 1$ (as Python does; the book's formulas use $1, \dots, n$, which changes nothing): a permutation $\sigma$ is the list $(\sigma(0), \sigma(1), \dots, \sigma(n - 1))$ that contains each number exactly once. There are $n! = 1 \cdot 2 \cdots n$ permutations: the first place can hold any of the $n$ numbers, the second any of the $n - 1$ that are left, and so on, down to 1 choice for the last place, and the numbers of choices multiply.

**Inversions and the sign.** An **inversion** of a permutation is a pair of places $i < j$ whose entries stand in the wrong order, $\sigma(i) > \sigma(j)$. The **sign** of the permutation is

$$
\mathrm{sign}(\sigma) = (-1)^{\text{number of inversions}} ,
$$

$+1$ for an **even** and $-1$ for an **odd** permutation. The six permutations of $0, 1, 2$:

| permutation | inversions (pairs of entries in the wrong order) | number | sign |
| --- | --- | --- | --- |
| (0, 1, 2) | none | 0 | $+1$ |
| (0, 2, 1) | (2, 1) | 1 | $-1$ |
| (1, 0, 2) | (1, 0) | 1 | $-1$ |
| (1, 2, 0) | (1, 0), (2, 0) | 2 | $+1$ |
| (2, 0, 1) | (2, 0), (2, 1) | 2 | $+1$ |
| (2, 1, 0) | (2, 1), (2, 0), (1, 0) | 3 | $-1$ |

**Theorem: an exchange flips the sign (PROVED).** Exchanging the entries at two places of a permutation changes its sign. *Proof, step 1: neighbouring places.* Exchange the entries at the places $k$ and $k + 1$. A pair of places that contains neither $k$ nor $k + 1$ keeps its two entries and its order. For a place $p$ outside the two, the two pairs $(p, k)$ and $(p, k + 1)$ compare the entry at $p$ with the same two entries before and after the exchange, only in the other order of the pairs, so together they contain the same number of inversions. The pair $(k, k + 1)$ itself was an inversion exactly when it is not one after the exchange. So the number of inversions changes by exactly 1, and the sign flips. *Step 2: any two places $i < j$.* Move the entry at place $i$ to the right by $j - i$ exchanges of neighbours, until it stands at place $j$; the entry that stood at place $j$ is now at place $j - 1$. Move that entry to the left by $j - i - 1$ exchanges of neighbours, until it stands at place $i$. Every other entry is back at its place, and the two entries have traded places. That took $(j - i) + (j - i - 1) = 2(j - i) - 1$ exchanges of neighbours, an odd number; by step 1 each flips the sign, and an odd number of flips is a flip.

**Half of the permutations are even (PROVED).** For $n \geq 2$, exchanging the first two entries turns every even permutation into an odd one and every odd one into an even one (the theorem), and doing it twice gives back the original permutation. So it pairs the even permutations with the odd ones one to one, and there are $n!/2$ of each. Notebook 01a, In [6] and In [7], lists the six permutations of three objects with their inversions and checks the three statements (the count $n!$, half of them even, every exchange flips the sign) for every permutation of $n = 1$ to 6 objects.

**The inverse permutation has the same sign (PROVED).** The **inverse** $\sigma^{-1}$ undoes $\sigma$: $\sigma^{-1}(b) = i$ when $\sigma(i) = b$. If the places $i < j$ form an inversion of $\sigma$, put $a = \sigma(j)$ and $b = \sigma(i)$; then $a < b$ and $\sigma^{-1}(a) = j > i = \sigma^{-1}(b)$, so $(a, b)$ is an inversion of $\sigma^{-1}$; and every inversion of $\sigma^{-1}$ comes back to one of $\sigma$ in this way. So both have the same number of inversions and the same sign.

**Permutation matrices.** The **permutation matrix** $P_\sigma$ has a 1 in row $i$ and column $\sigma(i)$ for every $i$, and 0 elsewhere: exactly one 1 in every row and in every column. A **signed permutation matrix** may have $-1$ instead of 1 in some of these places. Figure 01a.2 shows the 24 permutation matrices of 4 objects.

### 1.20 Determinants: the Leibniz formula and its six rules

**Definition.** The **determinant** of a square $n \times n$ matrix $A$ is the number

$$
\det A = \sum_{\sigma} \mathrm{sign}(\sigma)\, A_{1\sigma(1)} A_{2\sigma(2)} \cdots A_{n\sigma(n)} ,
$$

the sum over all $n!$ permutations $\sigma$ of $1, \dots, n$ (the **Leibniz formula**). Each term takes exactly one entry from every row $i$, namely the one in column $\sigma(i)$, so it also takes exactly one entry from every column. For $n = 2$ the permutations $(1, 2)$ (sign $+1$) and $(2, 1)$ (sign $-1$) give

$$
\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc ,
$$

the formula of Section 1.12. For $n = 3$ the six permutations of the table of Section 1.19 (counted from 1 instead of 0) give

$$
\det A = A_{11}A_{22}A_{33} + A_{12}A_{23}A_{31} + A_{13}A_{21}A_{32} - A_{12}A_{21}A_{33} - A_{11}A_{23}A_{32} - A_{13}A_{22}A_{31} .
$$

For the matrix $A$ of Section 1.18 the six terms are $1 + 2 + 0 - 0 - 3 - 0 = 0$: the determinant vanishes, and indeed the third row $(1, 3, 1)$ is the sum of the first two.

**Three special matrices (PROVED).** (a) A **diagonal** matrix, whose entries off the diagonal are 0: every permutation other than the identity takes some entry off the diagonal, so only the term of the identity survives, and $\det\mathrm{diag}(d_1, \dots, d_n) = d_1 d_2 \cdots d_n$. (b) A permutation matrix $P_\sigma$: a term of a permutation $\tau \neq \sigma$ contains an entry $(i, \tau(i))$ with $\tau(i) \neq \sigma(i)$, which is 0; so only the term of $\sigma$ survives, and it is $\mathrm{sign}(\sigma)\cdot 1 \cdots 1$: $\det P_\sigma = \mathrm{sign}(\sigma)$. (c) A signed permutation matrix with the nonzero entries $s_1, \dots, s_n = \pm 1$ in the places of $\sigma$: by the same argument

$$
\det = \mathrm{sign}(\sigma)\, s_1 s_2 \cdots s_n .
$$

**The six rules of determinants.** Write $M$ for an $n \times n$ matrix.

1. $\det(MN) = \det M\,\det N$. For $2 \times 2$ matrices this is a direct computation (PROVED): with $M$ of rows $(a, b), (c, d)$ and $N$ of rows $(e, f), (g, h)$, $MN$ has the rows $(ae + bg, af + bh)$ and $(ce + dg, cf + dh)$, and
$$
\det(MN) = (ae + bg)(cf + dh) - (af + bh)(ce + dg) = aecf + aedh + bgcf + bgdh - afce - afdg - bhce - bhdg
$$
(the $2 \times 2$ formula; multiply out), in which $aecf$ cancels $afce$ and $bgdh$ cancels $bhdg$, leaving $adeh + bcfg - adfg - bceh = ad(eh - fg) - bc(eh - fg) = (ad - bc)(eh - fg)$ (re-order the factors; take out the common factors). For every $n$ the rule is a standard theorem of algebra, ASSUMED here; Notebook 01a, In [11], checks it exactly for two $4 \times 4$ matrices.
2. $\det(M^T) = \det M$ (PROVED). The term of $\sigma$ in $\det M^T$ is $\mathrm{sign}(\sigma)\prod_i (M^T)_{i\sigma(i)} = \mathrm{sign}(\sigma)\prod_i M_{\sigma(i)i}$. Re-ordering the factors by their row $j = \sigma(i)$ writes the product as $\prod_j M_{j\sigma^{-1}(j)}$, the term of $\sigma^{-1}$ in $\det M$, and $\mathrm{sign}(\sigma^{-1}) = \mathrm{sign}(\sigma)$ (Section 1.19). As $\sigma$ runs through all permutations, so does $\sigma^{-1}$, so the two sums have the same terms.
3. Exchanging two rows changes the sign (PROVED). Let $M'$ be $M$ with the rows $r$ and $s$ exchanged. The term of $\sigma$ in $\det M'$ has the factors $M'_{r\sigma(r)} = M_{s\sigma(r)}$ and $M'_{s\sigma(s)} = M_{r\sigma(s)}$, so its product of entries is that of the permutation $\tau$ that equals $\sigma$ with the entries at the places $r$ and $s$ exchanged; and $\mathrm{sign}(\tau) = -\mathrm{sign}(\sigma)$ (the theorem of Section 1.19). As $\sigma$ runs through all permutations so does $\tau$, so every term of $\det M$ appears in $\det M'$ with the opposite sign: $\det M' = -\det M$.
4. A matrix with two equal rows has determinant 0 (PROVED): exchanging the two equal rows changes nothing, yet by rule 3 it changes the sign, so $D = -D$, and $D = 0$.
5. Multiplying one row by a number $c$ multiplies the determinant by $c$ (PROVED): every term contains exactly one entry of that row, so every term is multiplied by $c$.
6. Adding $c$ times row $s$ to row $r$ (with $s \neq r$) does not change the determinant (PROVED). Every term contains exactly one entry of row $r$, which is now $M_{r\sigma(r)} + c\,M_{s\sigma(r)}$; multiplying out, the determinant splits into $\det M$ plus $c$ times the determinant of $M$ with row $r$ replaced by row $s$; that matrix has two equal rows, so the second part is 0 by rule 4.

**Determinants and inverses.** A square matrix $M$ is **invertible** if there is a matrix $M^{-1}$ with $MM^{-1} = M^{-1}M = I$; then the equation $Mv = w$ can be undone, $v = M^{-1}w$. For a $2 \times 2$ matrix with $ad - bc \neq 0$ the inverse is

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix},
$$

as multiplying out shows: the product of the two matrices has the entries $ad - bc$, $-ab + ba = 0$, $cd - dc = 0$ and $-cb + da$, so it is $(ad - bc)I$, and dividing by $ad - bc$ gives $I$. For every $n$ it is a standard theorem that $M$ is invertible exactly when $\det M \neq 0$ (ASSUMED here; one half follows from rule 1: if $M^{-1}$ exists, $\det M\,\det M^{-1} = \det I = 1$, so $\det M \neq 0$). The determinant is the one number that says whether a matrix can be undone.

### 1.21 What a determinant measures, what it costs, and two matrices of the course

**A signed area (PROVED).** A $2 \times 2$ matrix $M$ with rows $(a, b)$ and $(c, d)$ moves the corners $(0, 0)$, $(1, 0)$, $(1, 1)$, $(0, 1)$ of the unit square to the corners $(0, 0)$, $(a, c)$, $(a + b, c + d)$, $(b, d)$ of a parallelogram: the images $Me_1 = (a, c)$ and $Me_2 = (b, d)$ of $e_1 = (1, 0)$ and $e_2 = (0, 1)$ are the two columns of $M$. The **signed area** of a polygon with the corners $(x_1, y_1), \dots, (x_K, y_K)$, listed in order, is given by the **shoelace formula**

$$
\tfrac12\sum_{k = 1}^{K}\big(x_k y_{k+1} - x_{k+1} y_k\big)\qquad(\text{with } x_{K+1} = x_1,\ y_{K+1} = y_1),
$$

which equals the area when the corners are listed counterclockwise and minus the area when they are listed clockwise (a standard fact of plane geometry, ASSUMED here). For the parallelogram the four terms of the sum are

$$
0\cdot c - a \cdot 0 = 0,\quad a(c + d) - (a + b)c = ad - bc,\quad (a + b)d - b(c + d) = ad - bc,\quad b \cdot 0 - 0 \cdot d = 0
$$

(insert the corners in order; multiply out; $ac$ and $bd$ cancel), so the signed area is $\tfrac12 \cdot 2(ad - bc) = \det M$. The size of the determinant is the factor by which $M$ multiplies areas, and its sign says whether the order of the corners is kept ($\det M > 0$) or reversed, that is, whether the picture is mirrored ($\det M < 0$). A determinant 0 flattens the square onto a line, and such a matrix cannot be undone. Notebook 01a, In [12], checks this for three examples and 1000 random matrices (Figure 01a.3).

**What a determinant costs.** The Leibniz formula has $n!$ terms, each a product of $n$ entries. For the $16 \times 16$ gamma matrices of the course that would be

$$
16! = 20922789888000
$$

terms. Computers therefore use **elimination**: by rule 6 one may subtract multiples of rows from other rows without changing the determinant, and doing so step by step makes every entry below the diagonal zero, which needs about $n^3/3$ multiplications. For a matrix with zeros below the diagonal (a **triangular** matrix) only the term of the identity survives in the Leibniz formula, because every other permutation $\sigma$ has some row $i$ with $\sigma(i) < i$ (the numbers $\sigma(i) - i$ add up to 0 and are not all 0, so one of them is negative), and the entry $A_{i\sigma(i)}$ below the diagonal is 0. So the determinant of the triangular matrix is the product of its diagonal. For $n = 16$ elimination needs about $16^3/3 \approx 1365$ steps instead of $2.1 \times 10^{13}$ terms (Figure 01a.4).

**The gamma matrices of the Revision record.** The file `Revision/algebra/gammas.json` of the Revision record holds the eight real $16 \times 16$ gamma matrices $\gamma^{(x_1)}, \dots, \gamma^{(x_8)}$ of the author's theory, one for each coordinate, rebuilt in the record from the author's own formulas (Chapter 4 builds them step by step), and the diagonal of the frame metric $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in the order $x_1, \dots, x_8$. The record states, in its report `Revision/algebra/reports/python-algebra.json`, check `reality_signed_permutations`, that every gamma matrix is a real signed permutation matrix, and in its check `clifford_relation` that $\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}I$; with equal indices this says $(\gamma^a)^2 = \eta_{aa}I$: $+I$ for the space-like directions $x_1, x_2, x_3, x_8$ and $-I$ for the time-like directions $x_4, \dots, x_7$. Two consequences for the determinant (PROVED): by rule 1, $(\det\gamma^a)^2 = \det\big((\gamma^a)^2\big) = \det(\pm I) = (\pm 1)^{16} = 1$, so $\det\gamma^a = \pm 1$; and by the formula (c) for signed permutation matrices it is $\mathrm{sign}(\sigma)$ times the product of the sixteen signs, a computation of 16 numbers and one permutation instead of $16!$ terms. Notebook 01a, In [14] and In [15], reads the matrices, reproduces the two record checks and finds $\det\gamma^a = +1$ for all eight (COMPUTED): the permutation of each is even, and each has an even number of entries $-1$ (eight for $\gamma^{(x_1)}$ to $\gamma^{(x_7)}$, none for $\gamma^{(x_8)}$).

**The determinant of the author's metric (PROVED).** The author's metric (Section 1.1) is diagonal, so by (a) its determinant is the product of its eight diagonal entries:

$$
\det g = \big(e^{2a_4}s\big)^3\cdot(-1)\cdot\big(-e^{-2a_4}s\big)^3\cdot\cot^2 z
$$

(the determinant of a diagonal matrix; the three equal space entries give a cube, and so do the three equal extra-time entries),

$$
= e^{6a_4}s^3\cdot(-1)\cdot(-1)\,e^{-6a_4}s^3\cdot\cot^2 z
$$

(the power of a product is the product of the powers, $(e^{2a_4})^3 = e^{6a_4}$, and $(-x)^3 = -x^3$),

$$
= e^{6a_4 - 6a_4}\, s^6\,\cot^2 z = \sin^2 z\,\frac{\cos^2 z}{\sin^2 z} = \cos^2 z
$$

(the two signs give $(-1)(-1) = +1$ and the powers of $e$ are collected with $a^pa^q = a^{p+q}$; then $e^0 = 1$, $s^6 = (\sin^{1/3}z)^6 = \sin^2 z$ and $\cot z = \cos z/\sin z$; cancel $\sin^2 z$). The growth $e^{6a_4}$ of the three space directions and the shrinking $e^{-6a_4}$ of the three exponentially deflating extra times cancel exactly, for every value of $a_4$. The sign is $+$ because the metric has four negative entries, an even number. Since $\cos z > 0$ for $0 < z < \pi/2$,

$$
\sqrt{|\det g|} = \cos z = \sin z\cot z ,
$$

and this is the product of the eight length factors of Section 1.5 (the square root of a product of positive numbers is the product of their square roots, and $|\det g| = \prod_\mu |g_{\mu\mu}|$). The record stores it as `sqrtAbsDetG` $= \sin z\cot z$ in `Revision/gkd_lovelock/results/curvature.json` and checks it in `Revision/gkd_lovelock/results/python-lovelock-report.json`, check `sqrt_abs_det_g`; Notebook 01a, In [17] and In [18], reproduces both, exactly with sympy and in numbers at 900 points (Figure 01a.6).

### 1.22 Example: matrices, permutations and determinants

Notebook 01a puts Sections 1.18 to 1.21 to work. It computes the dot product, matrix times vector and the matrix product with loops, with `einsum` and with `@`, and shows with heat maps that $AB \neq BA$; lists the permutations of 3 objects with their inversions and signs, checks the exchange theorem for every permutation of up to 6 objects and draws the 24 permutation matrices of 4 objects; writes the Leibniz formula as a Python function and compares it with sympy and numpy; checks the six rules; draws signed areas; plots the cost of the Leibniz formula against elimination; reads the eight gamma matrices from the Revision record and checks that they are signed permutation matrices with determinant 1 whose squares are $\pm I$; and reads the author's metric from the record and proves that its determinant is $\cos^2 z$ for every $a_4$. It ends with the line ALL 30 CHECKS PASSED (notebook 01a).

<!-- NOTEBOOK 01a -->

### 1.25 Line-by-line walk-through of Notebook 01a

The notebook has nineteen code cells, In [1] to In [19]. As in Section 1.9, a quoted line `...)` stands for the remaining lines of a figure caption, which Section 1.24 prints in full under its figure.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 1.23. Its code is, line for line, the set-up code of Notebook 01f explained in Section 1.9, with the single difference `NOTEBOOK_ID = "01a"`. It prints Set-up of notebook 01a complete: repository folder found, helpers defined.

**In [2], vectors.**

```python
import itertools  # all orderings (permutations) of a list
import math  # factorials

import numpy as np  # arrays of numbers: vectors and matrices
import sympy as sp  # exact arithmetic with whole numbers, fractions and symbols
```

`itertools` (part of Python) produces, among other things, all permutations of a list (`itertools.permutations`); `math` gives the factorial `math.factorial` and the product `math.prod`; numpy and sympy as before.

```python
v = np.array([1, 2, 0])  # a vector with 3 components
w = np.array([0, 1, 1])
say(f"v = {v.tolist()}, w = {w.tolist()}")
say(f"v + w = {(v + w).tolist()}, 3 v = {(3 * v).tolist()}")
```

`np.array([1, 2, 0])` makes a numpy array, here of whole numbers. `+` adds two arrays entry by entry and `3 * v` multiplies every entry: exactly the rules of Section 1.18. `.tolist()` turns an array into a plain Python list for printing. Output: v = [1, 2, 0], w = [0, 1, 1] and v + w = [1, 3, 1], 3 v = [3, 6, 0].

```python
# The dot product as a sum over the index i = 0, 1, 2 (Python counts from 0):
dot_by_hand = sum(int(v[i]) * int(w[i]) for i in range(3))
say(f"v . w by the sum = {dot_by_hand}, with numpy's @ = {int(v @ w)}")
check(dot_by_hand == int(v @ w) == 2, "the dot product of v and w is 2")
```

`sum(... for i in range(3))` adds the products $v_i w_i$ for $i = 0, 1, 2$ (Python's numbering of the components 1, 2, 3); `int(...)` turns a numpy number into a plain Python whole number. For two vectors, numpy's operator `@` is the dot product. Both give 2, and the check confirms it. Output: v . w by the sum = 2, with numpy's @ = 2, and the PASS line.

**In [3], matrix times vector.**

```python
A = np.array([[1, 2, 0],
              [0, 1, 1],
              [1, 3, 1]])  # three rows, each a list of three entries
say(f"A has {A.shape[0]} rows and {A.shape[1]} columns")
# Python counts rows and columns from 0: A[1, 2] is row 2, column 3 of A.
say(f"the entry in row 2, column 3 of A is A[1, 2] = {A[1, 2]}")
```

A matrix is an array of rows. `A.shape` is the pair (number of rows, number of columns). The second line prints the entry $A_{23} = 1$ under its Python name `A[1, 2]`.

```python
# (A v)_i = sum over j of A_ij v_j, one number for each row i:
Av_by_hand = [sum(int(A[i, j]) * int(v[j]) for j in range(3)) for i in range(3)]
say(f"A v by the sum = {Av_by_hand}, with numpy = {(A @ v).tolist()}")
check(Av_by_hand == (A @ v).tolist() == [5, 2, 7],
      "A v computed with the sum rule is (5, 2, 7), the same as numpy's A @ v")
```

The list comprehension computes, for each row $i$, the sum over $j$ of $A_{ij}v_j$: the rule of Section 1.18. `A @ v` is numpy's matrix times vector. Both give $(5, 2, 7)$. Output: A has 3 rows and 3 columns, the entry line, A v by the sum = [5, 2, 7], with numpy = [5, 2, 7], and the PASS line.

**In [4], the matrix product, three ways.**

```python
B = np.array([[0, 1, 0],
              [1, 0, 2],
              [0, 1, 1]])
n = 3
AB_loops = np.zeros((n, n), dtype=int)  # a 3 x 3 matrix of zeros to fill in
for i in range(n):  # the row of the product (a free index)
    for k in range(n):  # the column of the product (a free index)
        for j in range(n):  # the summed (dummy) index
            AB_loops[i, k] += A[i, j] * B[j, k]
```

The second matrix $B$ of Section 1.18. `np.zeros((n, n), dtype=int)` is a $3 \times 3$ array of whole-number zeros. The three nested loops compute $(AB)_{ik} = \sum_j A_{ij}B_{jk}$: the two outer loops run over the free indices $i$ and $k$, the inner loop adds the terms of the dummy index $j$ (`+=` adds to the entry).

```python
AB_einsum = np.einsum("ij,jk->ik", A, B)  # j appears twice: it is summed
AB = A @ B
BA = B @ A
say(f"A B = {AB.tolist()}")
say(f"B A = {BA.tolist()}")
```

The same product with `einsum` (the summation convention of Section 1.18) and with `@`; then $BA$. Output: A B = [[2, 1, 4], [1, 1, 3], [3, 2, 7]] and B A = [[0, 1, 1], [3, 8, 2], [1, 4, 2]], the matrices of Section 1.18.

```python
check((AB_loops == AB).all() and (AB_einsum == AB).all(),
      "loops, einsum and @ give the same product A B")
check(not (AB == BA).all(), "A B is not equal to B A: the order matters")
check(((A @ B).T == B.T @ A.T).all(), "the transpose rule (A B)^T = B^T A^T")
check(np.trace(AB) == np.trace(BA), "A B and B A have the same trace")
```

Four checks: the three ways agree entry by entry; $AB \neq BA$; the transpose rule (`.T` is numpy's transpose); equal traces (`np.trace`). Four PASS lines.

**In [5], heat maps.**

```python
def heat_map(ax, matrix, title, labels=None, annotate=True, digits=0,
             skip_zeros=False):
    """Draw matrix on the axes ax: every entry a coloured square, red for
    positive, white for zero, blue for negative entries; when annotate is True
    the value is written in its square with the given number of digits (not
    for the zero entries when skip_zeros is True)."""
    m = np.asarray(matrix, dtype=float)
    limit = max(1.0, float(np.abs(m).max()))  # colours run from -limit to +limit
    image = ax.imshow(m, cmap="RdBu_r", vmin=-limit, vmax=limit)
```

A drawing helper used for every matrix picture of this notebook. `np.asarray(..., dtype=float)` makes a floating-point array of any table. `limit` is the largest size of an entry (at least 1). `ax.imshow` draws the table as coloured squares; the **colour map** `"RdBu_r"` runs from blue through white to red, and `vmin=-limit, vmax=limit` puts white exactly at 0, so that red means positive and blue negative.

```python
    ax.set_title(title)
    ax.grid(False)  # no grid lines across the coloured squares
    if labels is None:  # number rows and columns 1, 2, 3, ... as in mathematics
        labels = [str(k + 1) for k in range(m.shape[0])]
    ax.set_xticks(range(m.shape[1]), labels[:m.shape[1]])
    ax.set_yticks(range(m.shape[0]), labels[:m.shape[0]])
```

The title; no grid lines; if no labels are given, rows and columns are labelled 1, 2, 3, ... as in mathematics (Python's square number $k$ gets the label $k + 1$); `set_xticks` and `set_yticks` put the labels under the columns and beside the rows.

```python
    if annotate:
        for i in range(m.shape[0]):
            for j in range(m.shape[1]):
                if skip_zeros and m[i, j] == 0:
                    continue
                # white writing on dark squares, black writing on light ones
                ink = "white" if abs(m[i, j]) > 0.6 * limit else "black"
                ax.text(j, i, f"{m[i, j]:.{digits}f}", ha="center", va="center",
                        color=ink)
    return image
```

When `annotate` is true, the value of every entry is written in the middle of its square (`ha` and `va`: horizontal and vertical alignment), with `digits` digits after the point (the format inside the braces is itself built from `digits`); `continue` skips a zero entry when `skip_zeros` is true. Dark squares get white writing. The helper returns the picture, so that a colour bar can be added later.

```python
fig, axes = plt.subplots(1, 4, figsize=(11.0, 3.2))
for ax, matrix, title in zip(axes, [A, B, AB, BA], ["A", "B", "A B", "B A"]):
    heat_map(ax, matrix, title)
fig.tight_layout()
save_figure(fig, "matrix_product",
            "Heat maps of the $3 \\times 3$ matrices $A$, $B$ and of their products "
            ...)
```

Four panels in a row, one heat map in each. What Figure 01a.1 shows: $AB$ and $BA$ have different entries, for example 4 and 1 in row 1, column 3.

**In [6], permutations and their signs.**

```python
def inversions(order):
    """The number of pairs of places i < j whose entries stand in the wrong order."""
    return sum(1 for i in range(len(order)) for j in range(i + 1, len(order))
               if order[i] > order[j])


def sign(order):
    """+1 for an even number of inversions, -1 for an odd number."""
    return 1 if inversions(order) % 2 == 0 else -1
```

`inversions` counts the pairs of places $i < j$ (the inner range starts at $i + 1$) with `order[i] > order[j]`: it adds 1 for each such pair. `sign` returns $+1$ when that number is even (its remainder after division by 2 is 0) and $-1$ otherwise: the definition of Section 1.19.

```python
for order in itertools.permutations(range(3)):  # all 6 orderings of 0, 1, 2
    say(f"permutation {order}: number of inversions {inversions(order)}, "
        f"sign {sign(order):+d}")
signs_of_three = [sign(order) for order in itertools.permutations(range(3))]
check(signs_of_three.count(1) == 3 and signs_of_three.count(-1) == 3,
      "of the 6 permutations of 3 objects, 3 are even and 3 are odd")
```

`itertools.permutations(range(3))` produces the six orderings of 0, 1, 2 as tuples (lists in round brackets). The loop prints each with its inversions and sign; the output is the table of Section 1.19. `.count(1)` counts the entries equal to 1. The check: three even, three odd.

**In [7], the exchange theorem for up to 6 objects.**

```python
swap_rule_holds = True
for n in range(1, 7):
    orders = list(itertools.permutations(range(n)))
    even = sum(1 for order in orders if sign(order) == 1)
    say(f"n = {n}: n! = {len(orders):3d} permutations; even {even:3d}, "
        f"odd {len(orders) - even:3d}")
    swap_rule_holds &= len(orders) == math.factorial(n)
    swap_rule_holds &= (n == 1 or 2 * even == len(orders))
```

For $n = 1$ to 6: all permutations, the number of even ones, and a printed line; then two conditions are added to `swap_rule_holds` with `&=` (it stays true only if every condition holds): there are $n!$ permutations, and (for $n \geq 2$) exactly half are even. The output lines read n = 1: n! = 1 permutations; even 1, odd 0 up to n = 6: n! = 720 permutations; even 360, odd 360.

```python
    for order in orders:
        for i in range(n):
            for j in range(i + 1, n):
                swapped = list(order)
                swapped[i], swapped[j] = swapped[j], swapped[i]  # exchange two
                swap_rule_holds &= sign(swapped) == -sign(order)
check(swap_rule_holds, "n! permutations, half of them even (n >= 2), and every "
      "exchange of two entries flips the sign (n = 1 to 6)")
```

For every permutation and every pair of places $i < j$: a copy of the permutation with the two entries exchanged (`a, b = b, a` exchanges two values in Python) must have the opposite sign. With $n$ up to 6 this tests every exchange of every permutation, the theorem of Section 1.19. One PASS line.

**In [8], the permutation matrices of 4 objects.**

```python
def permutation_matrix(order):
    """The matrix with a 1 in row i, column order[i], and 0 elsewhere."""
    P = np.zeros((len(order), len(order)), dtype=int)
    for i, column in enumerate(order):
        P[i, column] = 1
    return P
```

`enumerate(order)` gives the pairs (place, entry), so row `i` gets a 1 in column `order[i]`: the permutation matrix of Section 1.19.

```python
fig, axes = plt.subplots(4, 6, figsize=(10.0, 7.4))
for ax, order in zip(axes.flat, itertools.permutations(range(4))):
    # Grey squares for the 1s; the title gives the permutation and its sign.
    ax.imshow(permutation_matrix(order), cmap="Greys", vmin=0, vmax=1.4)
    ax.set_title(f"{order}  {sign(order):+d}", fontsize=8)
    ax.set_xticks([])
    ax.set_yticks([])
fig.tight_layout()
save_figure(fig, "permutation_matrices",
            "The 24 permutation matrices of 4 objects; each small picture is a "
            ...)
```

A grid of 4 rows and 6 columns of small axes for the $4! = 24$ permutations; `axes.flat` runs through them one after the other. Each matrix is drawn with the grey colour map (`vmax=1.4` makes the 1s dark grey rather than black); the title gives the permutation and its sign; `set_xticks([])` removes the tick labels. What Figure 01a.2 shows: twelve signs $+1$ and twelve $-1$; the first picture is the identity; exchanging two rows of any picture gives a picture with the opposite sign.

**In [9], the Leibniz formula in Python.**

```python
def leibniz_det(M):
    """The determinant of the square matrix M (a list of rows, a numpy array or a
    sympy Matrix) by the Leibniz formula: for every permutation, the sign times
    one entry from every row, row i giving the entry in column order[i]."""
    rows = [list(row) for row in (M.tolist() if hasattr(M, "tolist") else M)]
    total = 0
    for order in itertools.permutations(range(len(rows))):
        term = sign(order)
        for i in range(len(rows)):
            term = term * rows[i][order[i]]
        total = total + term
    return total
```

The Leibniz formula of Section 1.20, literally. First the matrix is turned into a list of rows, whatever it is (`hasattr(M, "tolist")` asks whether `M` can turn itself into a list, as numpy arrays and sympy matrices can). Then, for every permutation, the term starts as the sign and is multiplied by the entry of row `i` in column `order[i]` for every row; the terms are added. Because Python and sympy add and multiply whole numbers and symbols exactly, the result is exact.

```python
a, b, c, d = sp.symbols("a b c d")  # four symbols: letters for any numbers
det_2 = leibniz_det([[a, b], [c, d]])
say(f"det of the 2 x 2 matrix with rows (a, b) and (c, d) = {det_2}")
check(sp.expand(det_2 - (a * d - b * c)) == 0, "Leibniz for 2 x 2: a d - b c")
```

With four symbols the formula gives `a*d - b*c`, the formula $ad - bc$.

```python
say(f"det A = {leibniz_det(A)} (row 3 of A is row 1 plus row 2)")
check(leibniz_det(A) == 0, "det A = 0 because the rows of A are dependent")
check(all(leibniz_det(permutation_matrix(order)) == sign(order)
          for order in itertools.permutations(range(4))),
      "the determinant of every permutation matrix of 4 objects is its sign")
```

$\det A = 0$, as computed in Section 1.20, and $\det P_\sigma = \mathrm{sign}(\sigma)$ for all 24 permutations of 4 objects, rule (b) of Section 1.20. Output: the two lines and three PASS lines.

**In [10], three ways of computing a determinant.**

```python
generator = np.random.default_rng(12345)  # random numbers with a fixed seed
all_agree = True
for n in range(1, 8):
    M = generator.integers(-5, 6, size=(n, n))  # whole numbers -5 ... 5
    exact = leibniz_det(M)
    by_sympy = sp.Matrix(M.tolist()).det()
    by_numpy = np.linalg.det(M)  # a floating-point number
```

`np.random.default_rng(12345)` makes a **random-number generator** with the fixed starting number (**seed**) 12345, so that every run on every computer gets the same numbers. `generator.integers(-5, 6, size=(n, n))` draws an $n \times n$ table of whole numbers from $-5$ to 5 (the end 6 is not included). For $n = 1$ to 7 the determinant is computed three ways: by `leibniz_det`, by sympy (exact, by elimination) and by numpy's `np.linalg.det` (floating point, by elimination).

```python
    say(f"n = {n}: Leibniz {exact}, sympy {by_sympy}, numpy {by_numpy:.6f} "
        f"(n! = {math.factorial(n)} Leibniz terms)")
    all_agree &= exact == by_sympy and abs(by_numpy - exact) < 1e-6 * max(1, abs(exact))
check(all_agree, "Leibniz, sympy and numpy agree on 7 random integer matrices")
```

Each line prints the three results and the number of Leibniz terms; the exact two must agree exactly, numpy's to a millionth of the size of the result. Output: the determinants 2, 15, $-35$, $-24$, 730, 15445 and 60109 for $n = 1$ to 7, the same three times each, with 1 to 5040 Leibniz terms; then the PASS line.

**In [11], the six rules.**

```python
M = sp.Matrix(generator.integers(-5, 6, size=(4, 4)).tolist())
N = sp.Matrix(generator.integers(-5, 6, size=(4, 4)).tolist())
say(f"det M = {M.det()}, det N = {N.det()}, det(M N) = {(M * N).det()}")
check((M * N).det() == M.det() * N.det(), "rule 1: det(M N) = det M det N")
check(M.T.det() == M.det(), "rule 2: det of the transpose = det")
```

Two random $4 \times 4$ integer matrices as exact sympy matrices (the generator continues where In [10] stopped). Output: det M = -192, det N = 128, det(M N) = -24576, and indeed $-192 \cdot 128 = -24576$. Rules 1 and 2 are checked exactly.

```python
swapped = M.copy()
swapped.row_swap(0, 2)  # exchange rows 1 and 3
check(swapped.det() == -M.det(), "rule 3: exchanging two rows flips the sign")
twin = M.copy()
twin[3, :] = M[1, :]  # make row 4 equal to row 2
check(twin.det() == 0, "rule 4: two equal rows give determinant 0")
```

`.copy()` makes an independent copy, so that `M` itself stays unchanged. `row_swap(0, 2)` exchanges rows 1 and 3 (Python's 0 and 2): rule 3. `twin[3, :] = M[1, :]` replaces row 4 by row 2 (`[3, :]` means row 3 in Python's numbering, all columns): rule 4.

```python
scaled = M.copy()
scaled[1, :] = 7 * M[1, :]  # multiply row 2 by 7
check(scaled.det() == 7 * M.det(), "rule 5: a row times 7 multiplies det by 7")
added = M.copy()
added[0, :] = M[0, :] + 5 * M[3, :]  # row 1 plus 5 times row 4
check(added.det() == M.det(), "rule 6: adding a multiple of a row keeps det")
D = sp.diag(2, -3, 5, 7)
check(D.det() == 2 * (-3) * 5 * 7, "a diagonal matrix: det = product of the diagonal")
```

Rule 5 (row 2 times 7), rule 6 (5 times row 4 added to row 1), and rule (a) for the diagonal matrix $\mathrm{diag}(2, -3, 5, 7)$. The cell prints seven PASS lines.

**In [12], signed areas.**

```python
def signed_area(corners):
    """The shoelace formula: positive for corners listed counterclockwise."""
    total = 0.0
    for k in range(len(corners)):
        x1, y1 = corners[k]
        x2, y2 = corners[(k + 1) % len(corners)]  # % len: after the last, the first
        total += x1 * y2 - x2 * y1
    return total / 2
```

The shoelace formula of Section 1.21. For each corner $k$ the next corner is number $(k + 1)$ modulo the number of corners, so that the last corner is followed by the first (the remainder `%` turns $K$ into 0).

```python
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)  # counterclockwise
examples = [np.array([[2.0, 1.0], [1.0, 1.5]]),
            np.array([[1.0, 2.0], [1.0, 0.5]]),
            np.array([[1.0, 2.0], [0.5, 1.0]])]
fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.9))
```

The unit square as four rows (corners) in counterclockwise order, three example matrices with the determinants $2 \cdot 1.5 - 1 \cdot 1 = 2$, $1 \cdot 0.5 - 2 \cdot 1 = -1.5$ and $1 \cdot 1 - 2 \cdot 0.5 = 0$, and a figure with three panels.

```python
for ax, Mx in zip(axes, examples):
    image = square @ Mx.T  # each corner (a row) multiplied by the matrix
    ax.fill(square[:, 0], square[:, 1], color="0.85", label="unit square")
    ax.fill(image[:, 0], image[:, 1], color="tab:orange", alpha=0.5,
            label="its image")
```

For each matrix: `square @ Mx.T` multiplies every corner by the matrix (a corner is a row here, and a row $r$ times $M^T$ is the transpose of $M$ times the column $r$, by the transpose rule). `square[:, 0]` is the column of the $x$ values, `square[:, 1]` that of the $y$ values. The square is filled light grey, its image orange and half transparent.

```python
    ax.annotate("", xy=Mx[:, 0], xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "color": "tab:blue", "lw": 2})
    ax.annotate("", xy=Mx[:, 1], xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "color": "tab:red", "lw": 2})
    ax.text(*(Mx[:, 0] * 1.05), "$M e_1$", color="tab:blue")
    ax.text(*(Mx[:, 1] * 1.05), "$M e_2$", color="tab:red")
```

The two columns of the matrix, $Me_1$ and $Me_2$, as a blue and a red arrow from the origin, each labelled a little beyond its tip (the star hands the two coordinates of the point to `ax.text` as its first two arguments).

```python
    ax.set_title(f"det M = {np.linalg.det(Mx):+.2f}, area {signed_area(image):+.2f}")
    ax.set_aspect("equal")
    ax.set_xlim(-0.3, 3.4)
    ax.set_ylim(-0.3, 2.9)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.legend(loc="upper left", fontsize=8)
fig.tight_layout()
save_figure(fig, "area_and_determinant",
            "The unit square (grey) and its image (orange) under three $2 \\times 2$ "
            ...)
```

The title of each panel shows the determinant and the signed area of the image, which agree. What Figure 01a.3 shows: the area doubled (left); an area 1.5 with the two arrows in exchanged order, a mirrored picture (middle); the square flattened onto a line (right).

```python
areas_match = all(abs(signed_area(square @ Mx.T) - np.linalg.det(Mx)) < 1e-12
                  for Mx in examples)
random_matrices = generator.normal(size=(1000, 2, 2))  # 1000 random 2 x 2 matrices
areas_match &= all(abs(signed_area(square @ Mx.T) - np.linalg.det(Mx)) < 1e-12
                   for Mx in random_matrices)
check(areas_match, "the signed area of the image of the unit square is det M "
      "(3 examples and 1000 random matrices)")
```

The signed area must equal the determinant to $10^{-12}$ for the three examples and for 1000 random $2 \times 2$ matrices (`generator.normal` draws **normal random numbers**, numbers around 0 with the bell-shaped distribution; `size=(1000, 2, 2)` gives 1000 matrices). One PASS line.

**In [13], the cost of a determinant.**

```python
sizes = np.arange(1, 17)
leibniz_terms = np.array([math.factorial(int(k)) for k in sizes], dtype=float)
elimination_steps = sizes.astype(float) ** 3 / 3
report("number of terms of the Leibniz formula for n = 16", math.factorial(16))
check(math.factorial(16) == 20922789888000, "16! = 20 922 789 888 000")
```

For $n = 1$ to 16: the $n!$ terms of the Leibniz formula and the $n^3/3$ steps of elimination (`astype(float)` turns the whole numbers into floating-point numbers). The RESULT line prints 20922789888000, and the check compares it with $16!$ written out.

```python
fig, ax = plt.subplots()
ax.semilogy(sizes, leibniz_terms, "o-", label="Leibniz formula: $n!$ terms")
ax.semilogy(sizes, elimination_steps, "s-", label="elimination: about $n^3/3$ steps")
ax.axvline(16, color="black", ls=":", label="$n = 16$: the gamma matrices")
ax.set_xlabel("size $n$ of the matrix")
ax.set_ylabel("number of terms or steps")
ax.set_title("The cost of a determinant")
ax.legend();
```

Both counts against $n$ with a logarithmic vertical axis, and a dotted vertical line at $n = 16$. The semicolon after `ax.legend()` keeps Jupyter from printing the value of the line (Section 1.9).

```python
# The two counts for n = 16, rounded, for the caption: 2.1e13 and 1365.
mantissa, exponent = f"{leibniz_terms[-1]:.1e}".split("e")
save_figure(fig, "determinant_cost",
            "The number of terms $n!$ of the Leibniz formula (circles) and the "
            ...)
```

The caption quotes the count for $n = 16$ as computed, not typed: `f"{x:.1e}"` writes $16!$ as the text 2.1e+13, and `.split("e")` cuts it at the letter e into the **mantissa** 2.1 and the **exponent** +13; the caption's later lines (among the lines abbreviated `...)`) insert them as $2.1 \times 10^{13}$, and insert the elimination count $16^3/3 \approx 1365$ (`elimination_steps[-1]`, the last entry) with no digits after the point. What Figure 01a.4 shows: up to $n = 4$ the two counts are similar; then $n!$ grows far faster than $n^3/3$.

**In [14], the gamma matrices of the record.**

```python
record = json.loads(repository_file("Revision/algebra/gammas.json")
                    .read_text(encoding="utf-8"))
names = record["coordinates"]  # ["x1", "x2", ..., "x8"]
eta = record["eta"]  # the diagonal of the frame metric, in the order x1 ... x8
gamma = [np.array(matrix, dtype=int) for matrix in record["gamma"]]
say(f"coordinates: {names}")
say(f"diagonal of eta: {eta}")
```

The record file is read as text and turned into a Python dictionary (`json.loads`, Section 1.9). Its entry `coordinates` holds the names x1 to x8, `eta` the diagonal of $\eta$, and `gamma` the eight matrices, each a list of 16 rows; they become numpy arrays of whole numbers. Output: coordinates: ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8'] and diagonal of eta: [1, 1, 1, -1, -1, -1, -1, 1].

```python
signed_permutation = True
for g_a in gamma:
    signed_permutation &= set(np.unique(g_a).tolist()) <= {-1, 0, 1}
    signed_permutation &= ((g_a != 0).sum(axis=1) == 1).all()  # one per row
    signed_permutation &= ((g_a != 0).sum(axis=0) == 1).all()  # one per column
```

For each matrix three conditions: `np.unique` lists the different entries, and `set(...) <= {-1, 0, 1}` asks whether they are among $-1, 0, 1$ (`<=` between sets means "is contained in"); `(g_a != 0)` is a table of True and False, and `.sum(axis=1)` counts the True values in each row (`axis=0`: in each column), which must be 1 everywhere. Together: a signed permutation matrix.

```python
check(len(gamma) == 8 and all(g_a.shape == (16, 16) for g_a in gamma),
      "the record holds eight 16 x 16 gamma matrices")
check(signed_permutation, "every gamma matrix is a real signed permutation matrix",
      record="Revision/algebra/reports/python-algebra.json, "
             "check reality_signed_permutations")
```

Two checks: eight matrices of size $16 \times 16$, and the signed-permutation property; the second reproduces the record's check `reality_signed_permutations`, so `check` prints a second line naming it. Two PASS lines.

**In [15], determinants and squares of the gamma matrices.**

```python
identity16 = np.eye(16, dtype=int)  # the 16 x 16 identity matrix
all_det_one = True
squares_right = True
for name, eta_aa, g_a in zip(names, eta, gamma):
    order = [int(np.flatnonzero(row)[0]) for row in g_a]  # column of each nonzero
    signs = [int(g_a[i, order[i]]) for i in range(16)]  # the nonzero entries
    det_by_structure = sign(order) * math.prod(signs)
```

`np.eye(16, dtype=int)` is the $16 \times 16$ identity. For each matrix: `np.flatnonzero(row)` lists the places of the nonzero entries of a row, and the first (only) one is its column, so `order` is the permutation $\sigma$; `signs` are the sixteen nonzero entries $s_i$; and the determinant is $\mathrm{sign}(\sigma)\,s_1\cdots s_{16}$ by formula (c) of Section 1.20 (`math.prod` multiplies the entries of a list).

```python
    det_exact = sp.Matrix(g_a.tolist()).det()
    det_numpy = np.linalg.det(g_a)
    say(f"gamma^({name}): eta {eta_aa:+d}, {signs.count(-1)} entries -1, "
        f"permutation sign {sign(order):+d}, det {det_by_structure:+d}, "
        f"sympy {det_exact}, numpy {det_numpy:.3f}")
    all_det_one &= det_by_structure == det_exact == 1 and abs(det_numpy - 1) < 1e-9
    squares_right &= (g_a @ g_a == eta_aa * identity16).all()
```

The same determinant exactly with sympy and in floating point with numpy; a line per matrix; then the two conditions: all three determinants equal 1, and $\gamma^a\gamma^a = \eta_{aa}I$. The output reads, for $\gamma^{(x_1)}$ to $\gamma^{(x_7)}$, 8 entries -1, permutation sign +1, det +1, sympy 1, numpy 1.000, and for $\gamma^{(x_8)}$ 0 entries -1 with the same determinants.

```python
check(all_det_one, "every gamma matrix has determinant 1 (three ways)")
check(squares_right, "gamma^a gamma^a = eta_aa times the identity for every a",
      record="Revision/algebra/reports/python-algebra.json, check "
             "clifford_relation (its 8 relations with equal indices)")
```

Two PASS lines; the second reproduces the part of the record's check `clifford_relation` with equal indices.

**In [16], heat maps of two gamma matrices.**

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
ticks = [str(k) for k in range(1, 17)]
pictures = [(gamma[0], "$\\gamma^{(x_1)}$"), (gamma[3], "$\\gamma^{(x_4)}$"),
            (gamma[3] @ gamma[3], "$\\gamma^{(x_4)} \\gamma^{(x_4)} = -I$")]
for ax, (matrix, title) in zip(axes, pictures):
    image = heat_map(ax, matrix, title, labels=ticks, annotate=False)
    ax.tick_params(labelsize=6)
```

Three panels: $\gamma^{(x_1)}$ (Python's `gamma[0]`), $\gamma^{(x_4)}$ (`gamma[3]`) and its square, drawn with the helper of In [5] without written values; the row and column labels 1 to 16 are made small.

```python
fig.colorbar(image, ax=axes, shrink=0.75, label="entry", ticks=[-1, 0, 1])
save_figure(fig, "gamma_matrices",
            "Heat maps of two of the eight real $16 \\times 16$ gamma matrices of "
            ...)
```

`fig.colorbar` adds a bar that explains the colours, shared by the three panels (`ax=axes`), 75 per cent as tall as them, with the marks $-1$, 0, 1. What Figure 01a.5 shows: in every row and every column of a gamma matrix exactly one coloured square; the square of the time-like $\gamma^{(x_4)}$ has blue squares ($-1$) on the diagonal and nothing else: $-I$.

**In [17], the author's metric and its determinant, from the record.**

```python
a4 = sp.Symbol("a4", real=True)  # the value of the function a4(x4) at one time
z = sp.Symbol("z", positive=True)  # z = 6 H x8, between 0 and pi/2
s = sp.sin(z) ** sp.Rational(1, 3)  # sin(z) to the power 1/3
g_typed = ([sp.exp(2 * a4) * s] * 3 + [sp.Integer(-1)]
           + [-sp.exp(-2 * a4) * s] * 3 + [sp.cot(z) ** 2])
```

Symbols for the value of $a_4$ (any real number) and for $z$ (positive), $s = \sin^{1/3}z$, and the author's metric typed as the list of its eight diagonal entries, as in Section 1.1 (`sp.Integer(-1)` is the exact whole number $-1$).

```python
curvature = json.loads(repository_file("Revision/gkd_lovelock/results/curvature.json")
                       .read_text(encoding="utf-8"))


def from_record(text):
    """The record's Mathematica text as a sympy expression."""
    text = text.replace("a4[x4]", "a4").replace("Sin[6*H*x8]", "sin(z)")
    text = text.replace("Cot[6*H*x8]", "cot(z)").replace("^", "**")
    return sp.sympify(text, locals={"a4": a4, "z": z, "E": sp.E})
```

The record file, and the translation of its Mathematica texts into sympy, as in Notebook 01f, In [11] (Section 1.9), except that here $\sin(6Hx_8)$ becomes `sin(z)` and $\cot(6Hx_8)$ becomes `cot(z)` with the symbol $z$.

```python
g_record = [from_record(text) for text in curvature["metricDiagonal"]]
check(all(sp.simplify(x - y) == 0 for x, y in zip(g_record, g_typed)),
      "the record's metric diagonal equals the author's metric typed here")
det_g = sp.Mul(*g_typed)  # the product of the 8 diagonal entries
say(f"product of the diagonal entries, as sympy writes it: {det_g}")
```

The record's eight entries are compared one by one with the typed ones. `det_g` is the product of the diagonal, the determinant by rule (a). Output: sympy writes it `sin(z)**2*cot(z)**2`, already without $a_4$.

```python
check(sp.simplify(det_g - sp.cos(z) ** 2) == 0,
      "det g = cos(z)^2 for every a4: the e^(6 a4) of space and the e^(-6 a4) of "
      "the extra times cancel",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, check "
             "sqrt_abs_det_g")
root_record = from_record(curvature["sqrtAbsDetG"])
say(f"the record's square root of |det g|: {root_record}")
check(sp.simplify(root_record - sp.cos(z)) == 0 and
      sp.simplify(root_record ** 2 - det_g) == 0,
      "the record's sqrtAbsDetG = sin z cot z = cos z, and its square is det g",
      record="Revision/gkd_lovelock/results/curvature.json, sqrtAbsDetG")
```

The check $\det g = \cos^2 z$ (Section 1.21), which reproduces the record's check `sqrt_abs_det_g`; then the record's `sqrtAbsDetG`, printed as `sin(z)*cot(z)`, which must simplify to $\cos z$ and square to $\det g$. Three PASS lines, two with a second line naming the record.

**In [18], the metric in numbers.**

```python
metric_numbers = sp.lambdify((a4, z), g_typed, "numpy")  # a4, z -> 8 numbers
z_values = np.linspace(0.01, np.pi / 2 - 0.01, 300)  # inside (0, pi/2)
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.6))
g_point = np.diag(np.array(metric_numbers(0.5, 0.9), dtype=float))
coordinate_labels = [f"$x_{k}$" for k in range(1, 9)]  # x with subscripts 1 ... 8
heat_map(left, g_point, "metric $g$ at $a_4 = 0.5$, $z = 0.9$",
         labels=coordinate_labels, digits=2, skip_zeros=True)
left.tick_params(labelsize=8)
```

`sp.lambdify` turns the exact list of formulas into a fast numpy function of $a_4$ and $z$ that returns the eight numbers. `z_values` are 300 values inside $(0, \pi/2)$. On the left, the $8 \times 8$ metric at $a_4 = 0.5$, $z = 0.9$ (`np.diag` of a list builds the diagonal matrix) is drawn as a heat map with the coordinate names as labels and two digits, the zero entries left blank.

```python
largest_error = 0.0
for a4_value, style in [(-1.0, "-"), (0.0, "--"), (1.0, ":")]:
    dets = np.array([np.linalg.det(np.diag(np.array(metric_numbers(a4_value, zv),
                                                    dtype=float)))
                     for zv in z_values])
    largest_error = max(largest_error, float(np.max(np.abs(dets - np.cos(z_values)
                                                           ** 2))))
    right.plot(z_values, dets, style, lw=2, label=f"det g, $a_4 = {a4_value:+.0f}$")
```

For $a_4 = -1$, 0 and 1 (solid, dashed and dotted lines): at each of the 300 values of $z$ the $8 \times 8$ matrix is built and its determinant computed by numpy's elimination; `largest_error` keeps the largest difference from $\cos^2 z$; the 300 determinants are drawn against $z$.

```python
right.plot(z_values, np.cos(z_values) ** 2, color="black", lw=0.8,
           label="$\\cos^2 z$")
right.set_xlabel("$z = 6 H x_8$")
right.set_ylabel("$\\det g$")
right.set_title("The determinant does not depend on $a_4$")
right.legend()
fig.tight_layout()
save_figure(fig, "metric_and_determinant",
            "Left: heat map of the author's $8 \\times 8$ metric at $a_4 = 0.5$ and "
            ...)
```

The curve $\cos^2 z$ as a thin black line, labels, and the figure. What Figure 01a.6 shows: on the left only the diagonal is coloured, red for $x_1, x_2, x_3, x_8$ and blue for $x_4$ to $x_7$; on the right the three determinant curves and $\cos^2 z$ lie on top of each other.

```python
report("largest difference between det g and cos(z)^2 at 900 points",
       f"{largest_error:.1e}")
check(largest_error < 1e-12, "numpy: det g = cos(z)^2 at 300 values of z for "
      "each of a4 = -1, 0, 1")
```

The RESULT line prints $3.1 \times 10^{-15}$, rounding errors only, and the check requires less than $10^{-12}$ (COMPUTED).

**In [19], the last check.**

```python
figure_names = ["01a_1_matrix_product.png", "01a_2_permutation_matrices.png",
                "01a_3_area_and_determinant.png", "01a_4_determinant_cost.png",
                "01a_5_gamma_matrices.png", "01a_6_metric_and_determinant.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all 6 figure files of this notebook exist")
all_checks_passed()
```

The six figure files must exist; the last line is ALL 30 CHECKS PASSED (notebook 01a). The 30 checks are: 1 in In [2], 1 in In [3], 4 in In [4], 1 in In [6], 1 in In [7], 3 in In [9], 1 in In [10], 7 in In [11], 1 in In [12], 1 in In [13], 2 in In [14], 2 in In [15], 3 in In [17], 1 in In [18] and 1 in In [19].

### 1.26 Index notation and the summation convention

**Why indices.** Every formula of the theory involves the eight coordinates at once. The field equation of the Revision record, $\gamma^\mu D_\mu\Psi = (m + U'(S))\Psi$ (Chapter 7), is a sum of eight terms, one for each coordinate; the Clifford relation of the gamma matrices is one line that stands for 64 equations between $16 \times 16$ matrices. **Index notation** writes such formulas compactly: a letter stands for each of the coordinates, and a rule says which letters are summed.

**Indices and their positions.** An **index** is a letter that stands for any one of the eight coordinates $x_1, \dots, x_8$. The course uses the Latin letters $a, b, c, d$ for the directions of the frame (the eight directions with the frame metric $\eta$, below) and the Greek letters $\mu, \nu, \lambda$ for the coordinates themselves; both run over the eight values 1 to 8. A vector $v$ has the components $v^1, \dots, v^8$, written with an **upper index**: the component of $v$ along $x_3$ is $v^3$, which Python stores as `v[2]`. An upper index is a label, not a power: $v^3$ is a component, and its square is written $(v^3)^2$. A second list of eight numbers that belongs to the same vector, $v_1, \dots, v_8$, carries a **lower index**; Section 1.27 says how one list is made from the other. In index formulas the coordinates themselves are written $x^\mu$ with an upper index, and a small step along them $dx^\mu$; the author's names $x_1, \dots, x_8$ denote the same coordinates (the lower number is part of the name, as in Section 1.1), and the index of a coordinate is never lowered with a metric.

**Free and dummy indices.** Take a table $M^a{}_b$ (row $a$, column $b$) and a vector $v^b$. In

$$
w^a = M^a{}_b v^b = \sum_{b} M^a{}_b v^b
$$

the index $a$ is **free**: it appears once in every term, and the formula holds for each of its values, one equation for each $a$. The index $b$ is a **dummy**: it appears twice in one term, once up and once down, and it is summed over all its values. The **summation convention** (introduced by Einstein) is the rule that such a repeated pair is summed without writing $\sum$. A dummy index may be renamed, $M^a{}_b v^b = M^a{}_c v^c$, because the name of the letter in a sum does not change its value; a free index may not. In a correct equation every term has the same free indices in the same positions. A formula with $k$ free indices over eight coordinates stands for $8^k$ equations: 1, 8, 64, 512 for $k = 0, 1, 2, 3$.

**An example (PROVED by arithmetic).** With the table $M$ of rows $(1, 2, 0)$, $(0, 1, 1)$, $(1, 3, 1)$ and $v = (2, -1, 3)$ (three index values only, to keep it small):

$$
w^1 = 1\cdot 2 + 2\cdot(-1) + 0\cdot 3 = 0,\quad w^2 = 0\cdot 2 + 1\cdot(-1) + 1\cdot 3 = 2,\quad w^3 = 1\cdot 2 + 3\cdot(-1) + 1\cdot 3 = 2
$$

(for each free value $a$, the sum over the dummy $b$). Two numbers without any free index: the **trace** $M^a{}_a = M^1{}_1 + M^2{}_2 + M^3{}_3 = 1 + 1 + 1 = 3$, and, with $u_a = (1, 0, 2)$, the number $u_a M^a{}_b v^b = u_a w^a = 1\cdot 0 + 0\cdot 2 + 2\cdot 2 = 4$ (two dummy pairs, summed; first over $b$, which gives $w^a$, then over $a$). Setting an upper and a lower index equal and summing over it is called a **contraction**; it removes two free indices.

**The Kronecker delta.** With one upper and one lower index, $\delta^a{}_b$ (also written $\delta^a_b$) is 1 if $a = b$ and 0 otherwise; as a table it is the identity matrix. Three rules (PROVED):

$$
\delta^a{}_b v^b = v^a,\qquad \delta^a{}_b\,\delta^b{}_c = \delta^a{}_c,\qquad \delta^a{}_a = 8
$$

(in $\sum_b \delta^a{}_b v^b$ only the term $b = a$ is not zero, and it is $1 \cdot v^a$; the second rule is the first with the vector replaced by the column $c$ of $\delta$; the third adds $\delta^1{}_1 + \dots + \delta^8{}_8 = 1 + \dots + 1$, eight ones). Contracting with $\delta$ renames an index.

### 1.27 The frame metric: lowering, raising and squared lengths

**The frame metric.** The **frame metric** of the author's spacetime is the diagonal table

$$
\eta_{ab} = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)\quad\text{in the order } x_1, \dots, x_8 .
$$

It records only which directions are space-like ($+1$: $x_1, x_2, x_3$ and the hidden $x_8$) and which are time-like ($-1$: the time $x_4$ and the three extra times $x_5, x_6, x_7$). The Revision record stores it in `Revision/algebra/gammas.json` and states it in the report `Revision/algebra/reports/python-algebra.json`, check `coordinate_map`. Its inverse, written with upper indices $\eta^{ab}$, is the diagonal table of the inverse entries, $1/(+1) = +1$ and $1/(-1) = -1$: the same entries. Hence (PROVED)

$$
\eta^{ab}\eta_{bc} = \delta^a{}_c
$$

(the product of two diagonal tables is the diagonal table of the products of their entries, and each product is $(\pm 1)(\pm 1) = 1$).

**Lowering and raising (PROVED).** The lower list of a vector is made with $\eta$:

$$
v_a = \eta_{ab}v^b = \eta_{aa}v^a\quad(\text{no sum in the last expression})
$$

(only the term $b = a$ of the sum survives, because $\eta$ is diagonal). So **lowering** an index keeps the four space-like components and changes the sign of the four time-like ones: for $v^a = (1, 2, \dots, 8)$, $v_a = (1, 2, 3, -4, -5, -6, -7, 8)$. **Raising** with $\eta^{ab}$ undoes it: $\eta^{ab}v_b = \eta^{ab}\eta_{bc}v^c = \delta^a{}_c v^c = v^a$ (insert the lowered list; the inverse rule; the delta renames).

**The squared length.** The **squared length** of a vector is

$$
Q(v) = \eta_{ab}v^a v^b = v^a v_a = (v^1)^2 + (v^2)^2 + (v^3)^2 - (v^4)^2 - (v^5)^2 - (v^6)^2 - (v^7)^2 + (v^8)^2
$$

(the sum over $b$ is the lowered list; in the double sum only the terms $a = b$ survive because $\eta$ is diagonal). A vector $v \neq 0$ is **space-like** if $Q(v) > 0$, **time-like** if $Q(v) < 0$ and **light-like** (or **null**) if $Q(v) = 0$. Five examples (PROVED by arithmetic): the unit vector along $x_1$ has $Q = +1$ (space-like); the unit vector along $x_5$ has $Q = -1$ (time-like); their sum has $Q = 1 - 1 = 0$ (light-like although it is not zero); $(1, 1, \dots, 1)$ has $Q = 4 - 4 = 0$ (light-like); and $v = (1, 2, \dots, 8)$ has

$$
Q = (1 + 4 + 9 + 64) - (16 + 25 + 36 + 49) = 78 - 126 = -48
$$

(the squares of the space-like components $v^1, v^2, v^3, v^8$ minus those of the time-like components $v^4, \dots, v^7$): time-like. The **signature** of $\eta$ is $(4, 4)$: four entries $+1$ and four entries $-1$ (Section 1.36 gives the general definition). The boost of Section 1.13 keeps the squared length of the pair $(t, x)$ with $\eta = \mathrm{diag}(-1, +1)$; written with tables, the squared length of $\Lambda v$ is $(\Lambda v)^T\eta(\Lambda v) = v^T(\Lambda^T\eta\Lambda)v$ (the transpose rule of Section 1.18), so $\Lambda^T\eta\Lambda = \eta$ says that it equals $v^T\eta v$ for every $v$.

**Half of all random vectors are space-like (PROVED, with one ASSUMED fact of probability).** Draw the eight components of a vector as independent **normal random numbers** (numbers around 0 whose histogram is the bell curve $e^{-x^2/2}/\sqrt{2\pi}$). Exchange its four space-like components $(v^1, v^2, v^3, v^8)$ with its four time-like components $(v^4, v^5, v^6, v^7)$. The new vector $v'$ has

$$
Q(v') = (v^4)^2 + (v^5)^2 + (v^6)^2 + (v^7)^2 - (v^1)^2 - (v^2)^2 - (v^3)^2 - (v^8)^2 = -Q(v)
$$

(every square that was added is now subtracted and every square that was subtracted is now added). Because all eight components are drawn in the same way, the exchanged vector is exactly as likely as the original one; so $Q > 0$ and $Q < 0$ are equally likely, and $Q = 0$ exactly has probability 0 (ASSUMED from probability theory). Therefore, **in the signature (4,4) exactly half of all random vectors are space-like.** In ordinary spacetime with three space directions and one time, signature (3,1), $Q = (v^1)^2 + (v^2)^2 + (v^3)^2 - (v^4)^2$ adds three squares and subtracts one, and most random vectors are space-like; integral calculus (not shown here, ASSUMED) gives the fraction $1/2 + 1/\pi \approx 0.818$. Notebook 01e, In [6], draws 200,000 random vectors and measures the fractions 0.5031 and 0.8177 (COMPUTED). A measured fraction $p$ from $N$ tries is expected to scatter around the true value by about one **standard deviation** $\sqrt{p(1-p)/N}$ (ASSUMED from probability), here $\sqrt{0.25/200000} \approx 0.0011$ for the first; both measurements lie within 4 standard deviations of $1/2$ and of $1/2 + 1/\pi$ (Figure 01e.2).

### 1.28 Symmetric and antisymmetric arrays; commutators; the Clifford relation

**The symmetric and the antisymmetric part.** A square array is **symmetric** if $S_{ab} = S_{ba}$ and **antisymmetric** if $A_{ab} = -A_{ba}$; the diagonal of an antisymmetric array is 0, because $A_{aa} = -A_{aa}$ forces $A_{aa} = 0$. Every square array is the sum of a symmetric and an antisymmetric part:

$$
M_{ab} = S_{ab} + A_{ab},\qquad S_{ab} = \tfrac12(M_{ab} + M_{ba}),\qquad A_{ab} = \tfrac12(M_{ab} - M_{ba})
$$

(adding the two parts gives back $M_{ab}$, because the terms $M_{ba}$ cancel; exchanging $a$ and $b$ leaves $S$ unchanged and changes the sign of $A$).

**Theorem (PROVED).** If $S_{ab} = S_{ba}$ and $A^{ab} = -A^{ba}$, then $S_{ab}A^{ab} = 0$. *Proof*, line by line:

$$
S_{ab}A^{ab} = S_{ba}A^{ba}
$$

(both sides are the same double sum over all pairs; only the names of the two dummy indices were exchanged, which does not change a sum),

$$
S_{ba}A^{ba} = S_{ab}\,(-A^{ab})
$$

(the symmetry of $S$ and the antisymmetry of $A$), so $S_{ab}A^{ab} = -S_{ab}A^{ab}$, and a number that equals its own negative is 0. In words: the term $(a, b)$ and the term $(b, a)$ cancel, and the diagonal terms are 0. Raising both indices keeps an array antisymmetric: $A^{ab} = \eta^{ac}\eta^{bd}A_{cd}$, and $A^{ba} = \eta^{bc}\eta^{ad}A_{cd} = \eta^{ac}\eta^{bd}A_{dc} = -\eta^{ac}\eta^{bd}A_{cd} = -A^{ab}$ (the definition with $a$ and $b$ exchanged; the dummies $c$ and $d$ renamed into each other and the factors re-ordered; the antisymmetry of $A_{cd}$).

**A consequence used again and again (PROVED).** For a vector with ordinary (**commuting**) components, $v^a v^b = v^b v^a$ is symmetric in $a$ and $b$, so by the theorem $v^a v^b A_{ab} = 0$ for every antisymmetric $A$, and $v^a v^b M_{ab} = v^a v^b S_{ab}$: only the symmetric part of an array counts in a squared expression. Later in the course (Chapter 7) the components of the field dirac16complex **anticommute**, $\theta_a\theta_b = -\theta_b\theta_a$; then the products are antisymmetric, and only the antisymmetric part of an array counts.

**Commutators and anticommutators.** For two square matrices $P$ and $R$ the **commutator** and the **anticommutator** are

$$
[P, R] = PR - RP,\qquad \{P, R\} = PR + RP .
$$

They split a product into two parts, $PR = \tfrac12[P, R] + \tfrac12\{P, R\}$ (the two halves add up to $\tfrac12(PR - RP + PR + RP) = PR$), and directly from the definitions $[R, P] = -[P, R]$ and $\{R, P\} = \{P, R\}$. $P$ and $R$ **commute** if $[P, R] = 0$ and **anticommute** if $\{P, R\} = 0$, that is $PR = -RP$.

**The Clifford relation.** The eight gamma matrices of the Revision record obey

$$
\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}I\qquad(a, b = x_1, \dots, x_8),
$$

the **Clifford relation** (record `Revision/algebra/reports/python-algebra.json`, check `clifford_relation`; Chapter 4 derives it). With two free indices it stands for $8 \cdot 8 = 64$ matrix equations. For $a = b$ it says $(\gamma^a)^2 = \eta^{aa}I$, $+I$ for a space-like and $-I$ for a time-like direction (Section 1.21). For $a \neq b$ it says $\{\gamma^a, \gamma^b\} = 0$: different gamma matrices anticommute, and their commutator is $[\gamma^a, \gamma^b] = \gamma^a\gamma^b - \gamma^b\gamma^a = 2\gamma^a\gamma^b$. The product of two signed permutation matrices is again a signed permutation matrix (each row of the product picks one row of the second factor, with a sign), so this commutator has exactly 16 nonzero entries, $\pm 2$.

**Symmetric and antisymmetric gamma matrices (PROVED).** A real matrix $O$ with $O^TO = I$ is called **orthogonal**; then $O^T = O^{-1}$. Every signed permutation matrix is orthogonal: the entry $(j, k)$ of $O^TO$ is $\sum_i O_{ij}O_{ik}$, the "dot product" of the columns $j$ and $k$; for $j = k$ it is the square of the one nonzero entry $\pm 1$ of the column, which is 1; for $j \neq k$ the nonzero entries of the two columns lie in different rows (a row holds only one nonzero entry), so every product $O_{ij}O_{ik}$ is 0. For a gamma matrix, $(\gamma^a)^2 = \eta^{aa}I$ says $\gamma^a(\eta^{aa}\gamma^a) = I$ (multiply by the number $\eta^{aa} = \pm 1$, whose square is 1), so $(\gamma^a)^{-1} = \eta^{aa}\gamma^a$. Together:

$$
(\gamma^a)^T = (\gamma^a)^{-1} = \eta_{aa}\gamma^a\quad(\text{no sum}),
$$

the gamma matrices of the space-like directions $x_1, x_2, x_3, x_8$ are **symmetric** and those of the time-like directions $x_4, \dots, x_7$ are **antisymmetric**. The record states this in its check `symmetry_pattern`.

**Three contractions (PROVED).** Lowering the index of the gamma matrices gives $\gamma_a = \eta_{ab}\gamma^b$, which is $+\gamma^a$ for a space-like and $-\gamma^a$ for a time-like direction. *First*, $\gamma^a\gamma_a = 8I$:

$$
\gamma^a\gamma_a = \sum_a\gamma^a\eta_{ab}\gamma^b = \sum_a\eta_{aa}(\gamma^a)^2
$$

(insert $\gamma_a$; only $b = a$ survives because $\eta$ is diagonal),

$$
\sum_a\eta_{aa}(\gamma^a)^2 = \sum_a\eta_{aa}\eta^{aa}I = \sum_a 1\cdot I = 8I
$$

(the Clifford relation with $a = b$; then $\eta_{aa}\eta^{aa} = (\pm 1)^2 = 1$ for each of the eight values of $a$). Each time-like direction contributes $(\gamma^a)^2 = -I$, but its $\eta_{aa} = -1$ turns the contribution into $+I$. *Second*, $\gamma^a\gamma^b\gamma_a = -6\gamma^b$. First lower one index of the Clifford relation: multiplying $\gamma^b\gamma^c + \gamma^c\gamma^b = 2\eta^{bc}I$ by $\eta_{ca}$ and summing over $c$ gives

$$
\gamma^b\gamma_a + \gamma_a\gamma^b = 2\delta^b{}_a I,\qquad\text{that is}\qquad \gamma^b\gamma_a = -\gamma_a\gamma^b + 2\delta^b{}_a I
$$

($\gamma^c\eta_{ca} = \gamma_a$ by the definition of lowering, and $\eta^{bc}\eta_{ca} = \delta^b{}_a$; then move one term to the other side). Then

$$
\gamma^a\gamma^b\gamma_a = \gamma^a\big(-\gamma_a\gamma^b + 2\delta^b{}_a I\big) = -(\gamma^a\gamma_a)\gamma^b + 2\gamma^b = -8\gamma^b + 2\gamma^b = -6\gamma^b
$$

(insert the lowered relation; multiply out, where $\gamma^a\delta^b{}_a = \gamma^b$ because only $a = b$ survives; the first contraction; collect). In $n$ dimensions the same steps give $(2 - n)\gamma^b$. *Third*, $\mathrm{tr}(\gamma^a\gamma^b) = 16\eta^{ab}$: since $\mathrm{tr}(\gamma^a\gamma^b) = \mathrm{tr}(\gamma^b\gamma^a)$ (Section 1.18), $\mathrm{tr}(\gamma^a\gamma^b) = \tfrac12\mathrm{tr}(\gamma^a\gamma^b + \gamma^b\gamma^a) = \tfrac12\cdot 2\eta^{ab}\,\mathrm{tr}\,I = 16\eta^{ab}$ (the average of two equal numbers; the Clifford relation; $\mathrm{tr}\,I = 16$ for the $16 \times 16$ identity). Notebook 01e, In [10] to In [13], checks all of this with the matrices of the record (Figures 01e.4 and 01e.5).

### 1.29 The author's metric in index notation

**The metric and its inverse.** The author's metric $g_{\mu\nu}$ is the diagonal table of Section 1.1, with the entries $g_{11} = g_{22} = g_{33} = e^{2a_4}s$, $g_{44} = -1$, $g_{55} = g_{66} = g_{77} = -e^{-2a_4}s$ and $g_{88} = \cot^2 z$, where $s = \sin^{1/3}z$ and $z = 6Hx_8$; the record stores it in `Revision/gkd_lovelock/results/curvature.json`, key `metricDiagonal`. Its inverse $g^{\mu\nu}$ is the diagonal table with the entries $g^{\mu\mu} = 1/g_{\mu\mu}$, and $g^{\mu\nu}g_{\nu\lambda} = \delta^\mu{}_\lambda$ (PROVED: the product of two diagonal tables, with $(1/g_{\mu\mu})\,g_{\mu\mu} = 1$); the record checks it in `Revision/gkd_lovelock/results/python-lovelock-report.json`, check `metric_inverse`. The metric lowers and raises coordinate indices as $\eta$ does for frame indices: $dx_\mu = g_{\mu\nu}dx^\nu$.

**The line element (PROVED).** The squared length of a small step $dx^\mu$ in the coordinates is the **line element**

$$
ds^2 = g_{\mu\nu}\,dx^\mu dx^\nu = \sum_\mu g_{\mu\mu}\,(dx^\mu)^2 = dx^\mu dx_\mu
$$

(a double sum, in which only the terms $\nu = \mu$ survive because $g$ is diagonal; the sum over $\nu$ is the lowered list). For the step with the same small size $\epsilon$ in all eight coordinates, $dx^\mu = \epsilon$:

$$
ds^2 = \epsilon^2\big(3e^{2a_4}s - 1 - 3e^{-2a_4}s + \cot^2 z\big)
$$

(the eight diagonal entries, each times $\epsilon^2$: three equal space entries, the time, three equal extra-time entries, the hidden direction),

$$
= \epsilon^2\big(3s\,(e^{2a_4} - e^{-2a_4}) - 1 + \cot^2 z\big) = \epsilon^2\big(6s\sinh(2a_4) - 1 + \cot^2 z\big)
$$

(take out the common factor $3s$; then $e^{x} - e^{-x} = 2\sinh x$ with $x = 2a_4$, the definition of Section 1.13). As $a_4$ grows, the term of the three space directions grows like $e^{2a_4}$ and the term of the three exponentially deflating extra times shrinks towards 0 like $e^{-2a_4}$.

**Where the step changes its kind (PROVED).** For fixed $z$, $ds^2$ grows when $a_4$ grows, because $6s > 0$ and $\sinh$ is an increasing function (its derivative $\cosh$ is positive; the derivative of $6s\sinh(2a_4)$ with respect to $a_4$ is $12s\cosh(2a_4) > 0$). Since $\sinh$ takes every real value exactly once, its inverse function $\mathrm{arcsinh}$ exists, and $ds^2 = 0$ exactly at

$$
a_4^{\ast}(z) = \tfrac12\,\mathrm{arcsinh}\Big(\frac{1 - \cot^2 z}{6s}\Big)
$$

(set $ds^2 = 0$; solve for $\sinh(2a_4) = (1 - \cot^2 z)/(6s)$; apply $\mathrm{arcsinh}$; divide by 2). For $a_4 < a_4^{\ast}(z)$ the step is time-like, for $a_4 > a_4^{\ast}(z)$ space-like: as space inflates and the extra times deflate, the same coordinate step turns from time-like to space-like. Notebook 01e, In [14] and In [15], checks the formula exactly and the sign change on a grid of $301 \times 300$ points (Figure 01e.6; COMPUTED).

### 1.30 Example: index notation in the author's spacetime

Notebook 01e puts Sections 1.26 to 1.29 to work. It computes sums with free and dummy indices with loops and with `einsum`; reads $\eta$ from the Revision record, lowers and raises an index and checks $\eta^{ab}\eta_{bc} = \delta^a{}_c$ and $\delta^a{}_a = 8$; sorts vectors into space-like, time-like and light-like ones and measures with 200,000 random vectors that half of them are space-like in the signature (4,4) but about 82 per cent in the signature (3,1); checks the theorem on symmetric and antisymmetric arrays exactly with whole numbers; checks all 64 Clifford relations of the record's gamma matrices, their symmetry pattern and the three contractions; and writes the author's line element as a sum over indices and shows how the inflation of space and the deflation of the extra times change it. It ends with the line ALL 25 CHECKS PASSED (notebook 01e).

<!-- NOTEBOOK 01e -->

### 1.33 Line-by-line walk-through of Notebook 01e

The notebook has sixteen code cells, In [1] to In [16]. As in Section 1.9, a quoted line `...)` stands for the remaining lines of a figure caption, which Section 1.32 prints in full under its figure.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 1.31; its code is the set-up code explained in Section 1.9, with `NOTEBOOK_ID = "01e"`. It prints Set-up of notebook 01e complete: repository folder found, helpers defined.

**In [2], free and dummy indices.**

```python
import itertools  # all pairs (a, b) of indices
import math  # pi and square roots of plain numbers

import numpy as np  # arrays and einsum
import sympy as sp  # exact algebra with symbols
```

The modules of this notebook: `itertools.product` will produce all pairs of indices, `math` gives $\pi$ and square roots of single numbers.

```python
M = np.array([[1, 2, 0],
              [0, 1, 1],
              [1, 3, 1]])  # the entries M^a_b: row a, column b
v = np.array([2, -1, 3])  # the components v^b
u = np.array([1, 0, 2])  # the components u_a of a second vector
```

The table $M^a{}_b$, the vector $v^b$ and the lower list $u_a$ of the example of Section 1.26.

```python
# w^a = M^a_b v^b: the free index a is kept, the dummy index b is summed.
w_loops = [sum(int(M[a, b]) * int(v[b]) for b in range(3)) for a in range(3)]
w_einsum = np.einsum("ab,b->a", M, v)  # "b" appears twice: it is summed
w_renamed = np.einsum("ac,c->a", M, v)  # the dummy renamed to c: the same sum
```

$w^a$ three ways: with loops (for each free value $a$, the sum over the dummy $b$); with `einsum`, whose text `"ab,b->a"` lists the indices of each factor and of the result (the letter b appears in both factors and not in the result, so it is summed); and with the dummy renamed to c.

```python
say(f"w = M v by loops {w_loops}, by einsum {w_einsum.tolist()}, with the dummy "
    f"renamed {w_renamed.tolist()}")
check(w_loops == w_einsum.tolist() == w_renamed.tolist() == (M @ v).tolist()
      == [0, 2, 2],
      "loops, einsum and @ give w = (0, 2, 2); renaming the dummy changes nothing")
```

The three results are printed, each `[0, 2, 2]`, and checked against each other, against `M @ v` and against the hand calculation.

```python
trace = int(np.einsum("aa->", M))  # M^a_a: the repeated index a is summed
full = int(np.einsum("a,ab,b->", u, M, v))  # u_a M^a_b v^b: two dummies, no free
say(f"M^a_a = {trace}, u_a M^a_b v^b = {full}")
check(trace == int(np.trace(M)) == 3 and full == int(u @ M @ v) == 4,
      "the trace M^a_a = 3 and the number u_a M^a_b v^b = 4")
```

`"aa->"` contracts the two indices of one table: the trace. `"a,ab,b->"` contracts two pairs and keeps no index (nothing after the arrow): a single number. Output: `M^a_a = 3, u_a M^a_b v^b = 4`, and the PASS line.

```python
for free in range(4):
    word = "equation" if free == 0 else "equations"  # 8^0 = 1 equation
    say(f"{free} free indices over the 8 coordinates: 8^{free} = {8 ** free} {word}")
```

Four lines: a formula with 0, 1, 2, 3 free indices stands for 1, 8, 64, 512 equations (the singular "equation" for 1). The cell prints two PASS lines in all.

**In [3], the frame metric from the record.**

```python
algebra = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
names = algebra["coordinates"]  # ["x1", "x2", ..., "x8"]
eta_diagonal = algebra["eta"]  # the diagonal of eta in the order x1 ... x8
```

The record file of the gamma matrices, read as in Notebook 01a; its coordinate names and the diagonal of $\eta$.

```python
algebra_report = json.loads(repository_file(
    "Revision/algebra/reports/python-algebra.json").read_text(encoding="utf-8"))
verdicts = {c["name"]: c["verdict"] for c in algebra_report["checks"]}
map_verdict = verdicts["coordinate_map"]  # "pass" in the record
say(f"coordinates {names}")
say(f"diagonal of eta {eta_diagonal}; record check coordinate_map: {map_verdict}")
```

The record's report: its list of checks is turned into a dictionary from the check names to their verdicts (this report writes the verdict in small letters, `pass`). Output: the eight names, the diagonal `[1, 1, 1, -1, -1, -1, -1, 1]` and the record's verdict pass.

```python
check(eta_diagonal == [1, 1, 1, -1, -1, -1, -1, 1]
      and verdicts["coordinate_map"] == "pass",
      "eta = diag(+1, +1, +1, -1, -1, -1, -1, +1) in the order x1 ... x8",
      record="Revision/algebra/reports/python-algebra.json, check coordinate_map")
```

The diagonal of Section 1.27 and the record's verdict; this check reproduces the record's check `coordinate_map`.

```python
eta_lower = np.diag(eta_diagonal)  # eta_ab as an 8 x 8 matrix
eta_upper = np.diag([1 // e for e in eta_diagonal])  # eta^ab: 1/(+1) = 1, 1/(-1) = -1
delta = np.einsum("ab,bc->ac", eta_upper, eta_lower)  # eta^ab eta_bc
check((delta == np.eye(8, dtype=int)).all() and int(np.einsum("aa->", delta)) == 8,
      "eta^ab eta_bc = delta^a_c, and the contraction delta^a_a = 8")
```

$\eta_{ab}$ and $\eta^{ab}$ as $8 \times 8$ tables; the inverse entries are computed with the whole-number division `//`, which gives $1 // 1 = 1$ and $1 // (-1) = -1$ exactly. The contraction $\eta^{ab}\eta_{bc}$ must be the identity, and $\delta^a{}_a$ must be 8.

```python
v_up = np.arange(1, 9)  # v^a = 1, 2, ..., 8
v_down = np.einsum("ab,b->a", eta_lower, v_up)  # v_a = eta_ab v^b
v_back = np.einsum("ab,b->a", eta_upper, v_down)  # eta^ab v_b
flipped = [names[a] for a in range(8) if v_down[a] != v_up[a]]
say(f"v^a = {v_up.tolist()}")
say(f"v_a = {v_down.tolist()}; the components that changed sign: {flipped}")
check(flipped == ["x4", "x5", "x6", "x7"] and (v_back == v_up).all(),
      "lowering flips the signs of the time-like x4 ... x7; raising undoes it")
```

$v^a = (1, \dots, 8)$, lowered and raised again with `einsum`; `flipped` lists the names of the components that changed. Output: `v_a = [1, 2, 3, -4, -5, -6, -7, 8]`, the changed components x4 to x7, and the PASS line; the cell prints three PASS lines in all.

**In [4], the first heat maps.**

```python
labels = [f"$x_{k}$" for k in range(1, 9)]  # x with the subscripts 1 ... 8


def heat_map(ax, matrix, title, ticks=labels, annotate=True, size=7.0):
    """Draw matrix on the axes ax: red positive, white zero, blue negative; with
    annotate the value is written in its square (%g: no needless digits)."""
    m = np.asarray(matrix, dtype=float)
    limit = max(1.0, float(np.abs(m).max()))  # colours from -limit to +limit
    ax.imshow(m, cmap="RdBu_r", vmin=-limit, vmax=limit)
    ax.grid(False)  # no grid lines across the coloured squares
    ax.set_xticks(range(m.shape[1]), ticks[:m.shape[1]], fontsize=7)
    ax.set_yticks(range(m.shape[0]), ticks[:m.shape[0]], fontsize=7)
    ax.set_title(title, fontsize=10)
```

The labels $x_1, \dots, x_8$ for the axes, and a heat-map helper like the one of Notebook 01a (Section 1.25), with the coordinate names as default labels (`ticks=labels`) and an adjustable size of the written values.

```python
    if annotate:
        for i in range(m.shape[0]):
            for j in range(m.shape[1]):
                ink = "white" if abs(m[i, j]) > 0.6 * limit else "black"
                ax.text(j, i, f"{m[i, j]:g}", ha="center", va="center",
                        fontsize=size, color=ink)
```

The value of every entry is written in its square with the format `:g`, which drops needless digits (1.0 is written 1).

```python
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.0))
heat_map(axes[0], eta_lower, "$\\eta_{ab}$ (row $a$, column $b$)")
heat_map(axes[1], delta, "$\\eta^{ab}\\eta_{bc} = \\delta^a_c$ (row $a$, column $c$)")
positions = np.arange(8)
axes[2].bar(positions - 0.2, v_up, width=0.4, label="$v^a$ (upper index)")
axes[2].bar(positions + 0.2, v_down, width=0.4, label="$v_a = \\eta_{ab} v^b$")
```

Three panels: the heat maps of $\eta_{ab}$ and of $\eta^{ab}\eta_{bc}$, and a bar chart of the two lists $v^a$ and $v_a$ side by side (`ax.bar(positions, heights, width=...)` draws bars; shifting the positions by $\mp 0.2$ puts the two bars of each coordinate next to each other).

```python
axes[2].axhline(0, color="black", lw=0.8)
axes[2].set_xticks(positions, labels)
axes[2].set_ylabel("component")
axes[2].set_title("lowering the index of $v$", fontsize=10)
axes[2].legend(fontsize=8, loc="lower left")
fig.tight_layout()
save_figure(fig, "eta_and_delta",
            "Left: the frame metric $\\eta_{ab}$ of the author's coordinates as a "
            ...)
```

A zero line, labels and the figure. What Figure 01e.1 shows: $\eta$ red ($+1$) for $x_1, x_2, x_3, x_8$ and blue ($-1$) for $x_4$ to $x_7$; the contraction is the identity; the orange bars of $v_a$ point down exactly at the four time-like coordinates.

**In [5], squared lengths of five vectors.**

```python
def squared_length(vectors, metric_diagonal):
    """eta_ab v^a v^b for every row v of the array vectors (a and b are summed;
    the index n, which numbers the rows, is kept)."""
    metric = np.diag(metric_diagonal)
    return np.einsum("na,ab,nb->n", vectors, metric, vectors)
```

$Q(v) = \eta_{ab}v^av^b$ for many vectors at once: the array `vectors` has one vector per row, numbered by `n`; in `"na,ab,nb->n"` the letters a and b appear twice and are summed, while n is kept, so the result is one number per vector.

```python
unit = np.eye(8, dtype=int)  # row k is the unit vector along x_(k+1)
examples = {"e(x1)": unit[0], "e(x5)": unit[4], "e(x1) + e(x5)": unit[0] + unit[4],
            "(1, 1, 1, 1, 1, 1, 1, 1)": np.ones(8, dtype=int),
            "(1, 2, 3, 4, 5, 6, 7, 8)": v_up}
kinds = []
```

The rows of the identity are the unit vectors; the dictionary holds the five examples of Section 1.27 with their names (`np.ones(8)` is the vector of eight ones).

```python
for name, vector in examples.items():
    q = int(squared_length(vector[None, :], eta_diagonal)[0])  # one row
    kind = "space-like" if q > 0 else ("time-like" if q < 0 else "light-like")
    kinds.append(kind)
    q_text = f"{q:+d}" if q != 0 else "0"  # a sign in front of nonzero values only
    say(f"v = {name}: eta_ab v^a v^b = {q_text}, {kind}")
```

For each example: `vector[None, :]` makes the vector a table with one row, as `squared_length` expects, and `[0]` takes the one result. The kind follows from the sign of $Q$ (two nested `a if condition else b`). Output: +1 space-like, -1 time-like, 0 light-like, 0 light-like, -48 time-like.

```python
check(kinds == ["space-like", "time-like", "light-like", "light-like", "time-like"]
      and int(squared_length(v_up[None, :], eta_diagonal)[0]) == int(v_up @ v_down)
      == -48,
      "the five examples are sorted correctly, and eta_ab v^a v^b = v^a v_a = -48")
```

The sorting, and $\eta_{ab}v^av^b = v^av_a = -48$ for the last example, with the lowered list of In [3]. One PASS line.

**In [6], how many vectors are space-like.**

```python
generator = np.random.default_rng(12345)  # random numbers with a fixed seed
samples = generator.normal(size=(200000, 8))  # 200,000 vectors of 8 components
q44 = squared_length(samples, eta_diagonal)  # signature (4,4)
space_part, time_part = [0, 1, 2, 7], [3, 4, 5, 6]  # x1 x2 x3 x8, and x4 ... x7
exchanged = samples.copy()
exchanged[:, space_part] = samples[:, time_part]  # time components -> space slots
exchanged[:, time_part] = samples[:, space_part]  # space components -> time slots
```

200,000 vectors of eight normal random numbers (seed 12345) and their squared lengths. `space_part` and `time_part` are Python's places of the space-like and the time-like components. `exchanged` is a copy in which the four time-like components are written into the space-like places and the four space-like ones into the time-like places (`[:, space_part]` selects these columns in every row).

```python
check(np.allclose(squared_length(exchanged, eta_diagonal), -q44, rtol=0, atol=1e-9),
      "exchanging the space-like and the time-like components turns Q into -Q "
      "(all 200000 vectors)")
```

The exchange rule $Q(v') = -Q(v)$ of Section 1.27 for every one of the vectors (`np.allclose` compares two arrays entry by entry with the stated tolerances: `rtol=0`, no relative tolerance, `atol=1e-9`, an absolute one of $10^{-9}$).

```python
fraction44 = float(np.mean(q44 > 0))  # the fraction of space-like vectors
q31 = squared_length(samples[:, :4], [1, 1, 1, -1])  # 3 space, 1 time direction
fraction31 = float(np.mean(q31 > 0))
exact31 = 0.5 + 1 / math.pi
sd44 = math.sqrt(0.5 * 0.5 / 200000)  # one standard deviation of a fraction
sd31 = math.sqrt(exact31 * (1 - exact31) / 200000)
```

`np.mean(q44 > 0)` is the mean of a table of True (counted as 1) and False (0): the fraction of space-like vectors. For the signature (3,1) the first four components of each vector are used with the metric $\mathrm{diag}(1, 1, 1, -1)$. `exact31` is $1/2 + 1/\pi$, and `sd44`, `sd31` are the standard deviations $\sqrt{p(1-p)/N}$ of Section 1.27.

```python
report("fraction of space-like random vectors, signature (4,4)", f"{fraction44:.4f}")
report("fraction of space-like random vectors, signature (3,1)", f"{fraction31:.4f}")
check(abs(fraction44 - 0.5) < 4 * sd44,
      "signature (4,4): half of the random vectors are space-like")
check(abs(fraction31 - exact31) < 4 * sd31,
      "signature (3,1): the fraction is 1/2 + 1/pi = 0.818 (within 4 standard "
      "deviations)")
```

The RESULT lines print 0.5031 and 0.8177; the checks require each to lie within 4 standard deviations of its expected value. The cell prints three PASS lines.

**In [7], the two histograms.**

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2), sharey=True)
bins = np.linspace(-15.0, 15.0, 121)  # 120 intervals of width 0.25
for ax, values, fraction, title, color in (
        (axes[0], q44, fraction44, "signature (4,4): 4 space-like, 4 time-like",
         "tab:purple"),
        (axes[1], q31, fraction31, "signature (3,1): 3 space-like, 1 time-like",
         "tab:green")):
    ax.hist(values, bins=bins, density=True, color=color, alpha=0.75)
    ax.axvline(0.0, color="black", lw=1)
```

Two panels with a shared vertical axis (`sharey=True`). The 121 edges `bins` cut the range $-15$ to 15 into 120 intervals; `ax.hist` counts how many values fall into each interval and draws the counts as bars, scaled (`density=True`) so that the bars show the fraction of vectors per unit of $Q$. A black line marks $Q = 0$.

```python
    ax.text(0.97, 0.95, f"space-like: {fraction:.3f}", transform=ax.transAxes,
            ha="right", va="top")
    ax.text(0.03, 0.95, f"time-like: {1 - fraction:.3f}", transform=ax.transAxes,
            ha="left", va="top")
    ax.set_xlabel("squared length $Q = \\eta_{ab} v^a v^b$")
    ax.set_title(title, fontsize=10)
axes[0].set_ylabel("fraction of vectors per unit of $Q$")
fig.tight_layout()
save_figure(fig, "squared_lengths",
            "Histograms of the squared length $Q = \\eta_{ab} v^a v^b$ of 200,000 "
            ...)
```

The measured fractions are written into the upper corners (`transform=ax.transAxes` measures the position in fractions of the panel, 0 to 1, instead of in data units). What Figure 01e.2 shows: on the left a histogram that is the same on both sides of 0 (half space-like, half time-like); on the right one that leans to the positive side (82 per cent space-like).

**In [8], symmetric times antisymmetric, exactly.**

```python
M8 = generator.integers(-5, 6, size=(8, 8))  # a random 8 x 8 array, entries -5 ... 5
S2 = M8 + M8.T  # twice the symmetric part
A2 = M8 - M8.T  # twice the antisymmetric part
check((S2 == S2.T).all() and (A2 == -A2.T).all() and (S2 + A2 == 2 * M8).all(),
      "M = S + A with S = (M + M^T)/2 symmetric and A = (M - M^T)/2 antisymmetric")
```

A random $8 \times 8$ array of whole numbers. The cell works with $2S$ and $2A$, which are whole numbers, so that every computation is exact. The check: $2S$ is symmetric, $2A$ antisymmetric, and $2S + 2A = 2M$.

```python
A2_up = np.einsum("ac,bd,cd->ab", eta_upper, eta_upper, A2)  # A^ab (times 2)
terms = S2 * A2_up  # the 64 terms S_ab A^ab (times 4), before the sum
total = int(np.einsum("ab,ab->", S2, A2_up))  # the full contraction (times 4)
say(f"4 S_ab A^ab = {total}; the largest single term is "
    f"{int(np.abs(terms).max())}")
```

$A^{ab} = \eta^{ac}\eta^{bd}A_{cd}$ (both indices raised; `einsum` with two summed pairs), the 64 single products $S_{ab}A^{ab}$ (`*` between arrays multiplies entry by entry) and their sum. Output: `4 S_ab A^ab = 0; the largest single term is 24`: the terms are not zero, but they cancel in pairs.

```python
check((A2_up == -A2_up.T).all() and (terms == -terms.T).all() and total == 0,
      "A^ab is antisymmetric, the terms (a, b) and (b, a) cancel, S_ab A^ab = 0")
```

The three statements of Section 1.28: raising keeps antisymmetry; the term $(a, b)$ is minus the term $(b, a)$; the sum is 0.

```python
all_zero = True
for _ in range(100):  # 100 more random pairs of arrays
    X = generator.integers(-9, 10, size=(8, 8))
    Y = generator.integers(-9, 10, size=(8, 8))
    all_zero &= int(np.einsum("ab,ac,bd,cd->", X + X.T, eta_upper, eta_upper,
                              Y - Y.T)) == 0
check(all_zero, "S_ab A^ab = 0 for 100 more random pairs of arrays")
```

The theorem for 100 more random pairs: $X + X^T$ is symmetric, $Y - Y^T$ antisymmetric, and the contraction with both indices of the second raised is computed in one `einsum` (the loop variable `_` is not used).

```python
squares_ok = True
for _ in range(100):  # 100 random vectors with whole-number components
    w8 = generator.integers(-9, 10, size=8)
    squares_ok &= int(np.einsum("a,b,ab->", w8, w8, A2)) == 0
    squares_ok &= (int(np.einsum("a,b,ab->", w8, w8, 2 * M8))
                   == int(np.einsum("a,b,ab->", w8, w8, S2)))
check(squares_ok, "v^a v^b A_ab = 0 and v^a v^b M_ab = v^a v^b S_ab (100 random "
      "vectors with commuting components)")
```

The consequence for commuting components: for 100 random vectors $v^av^bA_{ab} = 0$ and $v^av^b(2M_{ab}) = v^av^b(2S_{ab})$. The cell prints four PASS lines.

**In [9], the picture of the cancellation.**

```python
fig, axes = plt.subplots(1, 4, figsize=(13.0, 3.7))
heat_map(axes[0], M8, "$M_{ab}$", size=6.0)
heat_map(axes[1], S2 / 2, "symmetric part $S_{ab}$", size=5.5)
heat_map(axes[2], A2 / 2, "antisymmetric part $A_{ab}$", size=5.5)
heat_map(axes[3], terms / 4, "terms $S_{ab} A^{ab}$ (sum 0)", annotate=False)
fig.tight_layout()
save_figure(fig, "symmetric_antisymmetric",
            "A random $8 \\times 8$ array $M_{ab}$ of whole numbers (left), its "
            ...)
```

Four heat maps: $M$, $S$, $A$ (the doubled arrays divided by 2) and the 64 terms (divided by 4), the last without written values. What Figure 01e.3 shows: $S$ looks the same mirrored in the diagonal; $A$ changes colour under the mirror and has a white diagonal; in the right panel every coloured square has a square of the opposite colour at its mirror place.

**In [10], commutators and the Clifford relation of the record.**

```python
P = generator.integers(-3, 4, size=(4, 4))
R = generator.integers(-3, 4, size=(4, 4))
commutator = P @ R - R @ P
anticommutator = P @ R + R @ P
check((2 * (P @ R) == commutator + anticommutator).all()
      and (R @ P - P @ R == -commutator).all()
      and (R @ P + P @ R == anticommutator).all(),
      "P R = [P, R]/2 + {P, R}/2, [R, P] = -[P, R] and {R, P} = {P, R}")
```

Two random $4 \times 4$ integer matrices, their commutator and anticommutator, and the three rules of Section 1.28 (the first written as $2PR = [P, R] + \{P, R\}$ to stay with whole numbers).

```python
gamma = [np.array(matrix, dtype=int) for matrix in algebra["gamma"]]  # gamma^a
identity16 = np.eye(16, dtype=int)
anti_table = np.zeros((8, 8), dtype=int)  # {gamma^a, gamma^b} = anti_table[a, b] I
commutator_size = np.zeros((8, 8), dtype=int)  # nonzero entries of the commutator
clifford_holds = True
```

The eight gamma matrices of the record; two $8 \times 8$ tables to be filled: the number $c_{ab}$ in $\{\gamma^a, \gamma^b\} = c_{ab}I$, and the number of nonzero entries of each commutator.

```python
for a, b in itertools.product(range(8), repeat=2):  # all 64 ordered pairs
    anti = gamma[a] @ gamma[b] + gamma[b] @ gamma[a]
    anti_table[a, b] = anti[0, 0]  # the number in front of I
    clifford_holds &= bool((anti == 2 * eta_upper[a, b] * identity16).all())
    commutator_size[a, b] = np.count_nonzero(gamma[a] @ gamma[b]
                                             - gamma[b] @ gamma[a])
```

`itertools.product(range(8), repeat=2)` produces all 64 ordered pairs $(a, b)$. For each: the anticommutator; its top-left entry (if it is $c_{ab}I$, every diagonal entry is $c_{ab}$); the exact comparison with $2\eta^{ab}I$; and `np.count_nonzero` of the commutator.

```python
check(clifford_holds and verdicts["clifford_relation"] == "pass",
      "{gamma^a, gamma^b} = 2 eta^ab I for all 64 ordered pairs (a, b)",
      record="Revision/algebra/reports/python-algebra.json, check "
             "clifford_relation")
```

All 64 relations hold, and the record's verdict is pass: this reproduces the record's check `clifford_relation`.

```python
orthogonal = all((g.T @ g == identity16).all() for g in gamma)
transpose_sign = [1 if (g.T == g).all() else (-1 if (g.T == -g).all() else 0)
                  for g in gamma]  # +1 symmetric, -1 antisymmetric
say("symmetric: " + ", ".join(names[a] for a in range(8) if transpose_sign[a] == 1)
    + "; antisymmetric: "
    + ", ".join(names[a] for a in range(8) if transpose_sign[a] == -1))
```

Each gamma matrix is tested for $O^TO = I$, and `transpose_sign` records $+1$ for a symmetric matrix, $-1$ for an antisymmetric one (and 0 for neither, which does not occur). Output: symmetric: x1, x2, x3, x8; antisymmetric: x4, x5, x6, x7.

```python
check(orthogonal and transpose_sign == eta_diagonal
      and verdicts["symmetry_pattern"] == "pass",
      "each gamma^a is orthogonal and (gamma^a)^T = eta_aa gamma^a: symmetric "
      "for x1, x2, x3, x8, antisymmetric for x4 ... x7",
      record="Revision/algebra/reports/python-algebra.json, check "
             "symmetry_pattern")
```

The theorem $(\gamma^a)^T = \eta_{aa}\gamma^a$ of Section 1.28 (the list of signs equals the diagonal of $\eta$), reproducing the record's check `symmetry_pattern`. The cell prints three PASS lines.

**In [11], the Clifford tables as pictures.**

```python
fig, axes = plt.subplots(1, 3, figsize=(12.5, 4.0),
                         gridspec_kw={"width_ratios": [1, 1, 1.2]})
heat_map(axes[0], anti_table, "$\\{\\gamma^a, \\gamma^b\\} = c_{ab} I$: $c_{ab}$")
heat_map(axes[1], commutator_size,
         "nonzero entries of $[\\gamma^a, \\gamma^b]$", size=6.0)
```

Three panels, the third a little wider (`width_ratios`). The table $c_{ab}$ and the table of commutator sizes as heat maps.

```python
axes[2].bar(positions - 0.2, transpose_sign, width=0.4, color="tab:blue",
            label="$s_a$ in $(\\gamma^a)^T = s_a \\gamma^a$")
axes[2].bar(positions + 0.2, eta_diagonal, width=0.4, color="tab:orange",
            label="$\\eta_{aa}$")
axes[2].axhline(0, color="black", lw=0.8)
axes[2].set_xticks(positions, labels)
axes[2].set_ylim(-1.6, 1.6)
axes[2].set_title("symmetric ($+1$) or antisymmetric ($-1$)", fontsize=10)
axes[2].legend(fontsize=8, loc="lower left")
fig.tight_layout()
save_figure(fig, "clifford_tables",
            "The Clifford relation of the eight real $16 \\times 16$ gamma matrices "
            ...)
```

The third panel draws, for each coordinate, the transpose sign next to $\eta_{aa}$. What Figure 01e.4 shows: $c_{ab}$ is $\pm 2$ on the diagonal and 0 elsewhere; every commutator of two different gamma matrices has 16 nonzero entries and the diagonal (a matrix with itself) has none; the blue and orange bars are equal for every coordinate.

**In [12], the three contractions.**

```python
gamma_lower = [sum(eta_lower[a, b] * gamma[b] for b in range(8)) for a in range(8)]
contraction = sum(gamma[a] @ gamma_lower[a] for a in range(8))  # gamma^a gamma_a
check((contraction == 8 * identity16).all(), "gamma^a gamma_a = 8 I")
```

$\gamma_a = \eta_{ab}\gamma^b$ as a list of eight matrices (the sum over $b$ written out), then $\gamma^a\gamma_a$ (the sum over $a$) and the first contraction, $8I$.

```python
lowered_ok = all((gamma[b] @ gamma_lower[a] + gamma_lower[a] @ gamma[b]
                  == 2 * int(a == b) * identity16).all()
                 for a, b in itertools.product(range(8), repeat=2))
sandwich = [sum(gamma[a] @ gamma[b] @ gamma_lower[a] for a in range(8))
            for b in range(8)]  # gamma^a gamma^b gamma_a for each b
```

`lowered_ok` tests the lowered Clifford relation $\gamma^b\gamma_a + \gamma_a\gamma^b = 2\delta^b{}_aI$ for all 64 pairs (`int(a == b)` is 1 for equal indices and 0 otherwise: the Kronecker delta). `sandwich` holds $\gamma^a\gamma^b\gamma_a$ for each $b$.

```python
factors = [int(sandwich[b][np.nonzero(gamma[b])][0]
               // gamma[b][np.nonzero(gamma[b])][0]) for b in range(8)]
say(f"gamma^a gamma^b gamma_a = c gamma^b with c = {factors} for b = x1 ... x8")
check(lowered_ok and all((sandwich[b] == -6 * gamma[b]).all() for b in range(8)),
      "gamma^b gamma_a + gamma_a gamma^b = 2 delta^b_a I, and gamma^a gamma^b "
      "gamma_a = -6 gamma^b for every b")
```

To find the factor $c$ in $\gamma^a\gamma^b\gamma_a = c\,\gamma^b$, the first nonzero entry of $\gamma^b$ (`np.nonzero` gives the places of the nonzero entries) and the entry of the sandwich at the same place are divided. Output: c = [-6, -6, -6, -6, -6, -6, -6, -6]. The check requires the lowered relation and the exact equality with $-6\gamma^b$.

```python
traces = np.array([[int(np.trace(gamma[a] @ gamma[b])) for b in range(8)]
                   for a in range(8)])
check((traces == 16 * eta_upper).all(), "tr(gamma^a gamma^b) = 16 eta^ab")
```

The table of the 64 traces must be $16\eta^{ab}$, the third contraction. The cell prints three PASS lines.

**In [13], the contractions as pictures.**

```python
square_sign = [int(np.trace(g @ g)) // 16 for g in gamma]  # (gamma^a)^2 = +-I
term_sign = [eta_diagonal[a] * square_sign[a] for a in range(8)]  # eta_aa (gamma^a)^2
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
```

The sign of $(\gamma^a)^2 = \pm I$ is read from its trace ($\pm 16$, divided by 16), and `term_sign` is the sign of the term $\eta_{aa}(\gamma^a)^2$ of the first contraction.

```python
left.bar(positions - 0.27, square_sign, width=0.27, color="tab:blue",
         label="$(\\gamma^a)^2 = \\pm I$: the sign")
left.bar(positions, eta_diagonal, width=0.27, color="tab:orange",
         label="$\\eta_{aa}$")
left.bar(positions + 0.27, term_sign, width=0.27, color="tab:green",
         label="term $\\eta_{aa}(\\gamma^a)^2 = +I$")
left.plot(positions, np.cumsum(term_sign) / 8, "k.--", lw=1,
          label="running sum / 8")
```

Three bars per coordinate: the sign of the square, $\eta_{aa}$ and their product; and the **running sum** of the terms (`np.cumsum` adds the entries one after the other: 1, 2, ..., 8), divided by 8, as a dashed black line with dots (the style string made of a dot and two hyphens).

```python
left.axhline(0, color="black", lw=0.8)
left.set_xticks(positions, labels)
left.set_ylim(-1.5, 1.9)
left.set_title("$\\gamma^a\\gamma_a$: eight terms, each $+I$, sum $8I$",
               fontsize=10)
left.legend(fontsize=7, loc="lower left", ncol=2)
```

Zero line, labels, range, title and a two-column legend.

```python
right.plot(positions, factors, "o", color="tab:red", ms=9,
           label="$c$ in $\\gamma^a\\gamma^b\\gamma_a = c\\,\\gamma^b$")
right.axhline(2 - 8, color="black", ls=":", label="$2 - n$ for $n = 8$")
right.set_xticks(positions, [f"$b = x_{k}$" for k in range(1, 9)], fontsize=8)
right.set_ylim(-8.0, 0.5)
right.set_ylabel("factor $c$")
right.set_title("$\\gamma^a\\gamma^b\\gamma_a = -6\\gamma^b$ for every $b$",
                fontsize=10)
right.legend(fontsize=8, loc="upper right")
fig.tight_layout()
save_figure(fig, "gamma_contractions",
            "Left: the contraction $\\gamma^a\\gamma_a$ term by term for $a = x_1$ "
            ...)
```

On the right the eight factors $c$ as red dots and the dotted line $2 - n = -6$. What Figure 01e.5 shows: the blue and orange bars are both negative exactly for $x_4$ to $x_7$, so every green bar is $+1$ and the running sum climbs to 1 (that is, $8I$); all eight red dots sit on the line $-6$.

**In [14], the author's metric in index notation.**

```python
a4 = sp.Symbol("a4", real=True)  # the value of a4(x4) at one time
z = sp.Symbol("z", positive=True)  # z = 6 H x8, between 0 and pi/2
s = sp.sin(z) ** sp.Rational(1, 3)
g_typed = ([sp.exp(2 * a4) * s] * 3 + [sp.Integer(-1)]
           + [-sp.exp(-2 * a4) * s] * 3 + [sp.cot(z) ** 2])
curvature = json.loads(repository_file("Revision/gkd_lovelock/results/curvature.json")
                       .read_text(encoding="utf-8"))
```

The symbols, the typed metric and the record file, exactly as in Notebook 01a, In [17] (Section 1.25).

```python
def from_record(text):
    """The record's Mathematica text as a sympy expression."""
    text = text.replace("a4[x4]", "a4").replace("Sin[6*H*x8]", "sin(z)")
    text = text.replace("Cot[6*H*x8]", "cot(z)").replace("^", "**")
    return sp.sympify(text, locals={"a4": a4, "z": z, "E": sp.E})


g_record = [from_record(text) for text in curvature["metricDiagonal"]]
check(all(sp.simplify(x - y) == 0 for x, y in zip(g_record, g_typed)),
      "the record's metric diagonal is the author's metric of section 4",
      record="Revision/gkd_lovelock/results/curvature.json, metricDiagonal")
```

The same translation function and the comparison with the typed metric (the "section 4" of the check's name is section 4 of the notebook, which states the metric); this check reproduces the record's key `metricDiagonal`.

```python
g_lower = sp.diag(*g_record)  # g_mu nu
g_upper = sp.diag(*[1 / entry for entry in g_record])  # g^mu nu
lovelock_report = json.loads(repository_file(
    "Revision/gkd_lovelock/results/python-lovelock-report.json")
    .read_text(encoding="utf-8"))
lovelock_verdicts = {c["name"]: c["verdict"] for c in lovelock_report["checks"]}
```

$g_{\mu\nu}$ and $g^{\mu\nu}$ as diagonal sympy matrices (the star hands the eight entries to `sp.diag` one by one), and the verdicts of the record's report (this one writes them in capitals, PASS).

```python
check((g_upper * g_lower).applyfunc(sp.simplify) == sp.eye(8)
      and lovelock_verdicts["metric_inverse"] == "PASS",
      "g^mu nu g_nu lambda = delta^mu_lambda",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, check "
             "metric_inverse")
```

$g^{\mu\nu}g_{\nu\lambda} = \delta^\mu{}_\lambda$, reproducing the record's check `metric_inverse`.

```python
step = sp.Matrix([1] * 8)  # dx^mu = 1 for every mu (units with epsilon = 1)
ds2 = (step.T * g_lower * step)[0, 0]  # g_mu nu dx^mu dx^nu
step_lower = g_lower * step  # dx_mu = g_mu nu dx^nu
ds2_contracted = (step.T * step_lower)[0, 0]  # dx^mu dx_mu
closed_form = 6 * s * sp.sinh(2 * a4) - 1 + sp.cot(z) ** 2
say(f"ds^2 for dx^mu = 1: {ds2}")
```

The step $dx^\mu = 1$ (that is, $\epsilon = 1$) as a column of eight ones. `step.T * g_lower * step` is the row times the table times the column, a $1 \times 1$ matrix whose one entry `[0, 0]` is $g_{\mu\nu}dx^\mu dx^\nu$. The lowered step and the contraction $dx^\mu dx_\mu$; the closed form of Section 1.29. Output: `3*exp(2*a4)*sin(z)**(1/3) + cot(z)**2 - 1 - 3*exp(-2*a4)*sin(z)**(1/3)`, the first line of the derivation.

```python
check(sp.expand((ds2 - closed_form).rewrite(sp.exp)) == 0
      and sp.expand(ds2_contracted - ds2) == 0,
      "ds^2 = 6 s sinh(2 a4) - 1 + cot(z)^2 for the step dx^mu = 1, and dx^mu dx_mu "
      "gives the same")
```

The difference from the closed form, with $\sinh$ written as exponentials, multiplies out to 0; and both ways of contracting agree. The cell prints three PASS lines.

**In [15], where the step changes its kind.**

```python
ds2_numbers = sp.lambdify((a4, z), closed_form, "numpy")  # a formula -> a function
a4_values = np.linspace(-1.5, 1.5, 301)
z_values = np.linspace(0.15, np.pi / 2 - 0.005, 300)
A4_grid, Z_grid = np.meshgrid(a4_values, z_values)  # rows: z, columns: a4
values = ds2_numbers(A4_grid, Z_grid)
```

The closed form as a numpy function; 301 values of $a_4$ and 300 values of $z$. `np.meshgrid` makes two tables of the same shape, one holding $a_4$ and one holding $z$ at every grid point (a row for each $z$, a column for each $a_4$), so that `values` holds $ds^2/\epsilon^2$ at all $301 \cdot 300$ points.

```python
threshold = 0.5 * np.arcsinh((1 - 1 / np.tan(z_values) ** 2)
                             / (6 * np.sin(z_values) ** (1 / 3)))
check(bool((np.diff(values, axis=1) > 0).all()),
      "on every row of the grid, ds^2 grows as a4 grows")
away = np.abs(A4_grid - threshold[:, None]) > 1e-9  # leave out points on the curve
check(bool(((values > 0) == (A4_grid > threshold[:, None]))[away].all()),
      "ds^2 > 0 exactly to the right of the curve a4*(z)")
```

`threshold` is $a_4^{\ast}(z)$ for each $z$ ($\cot z = 1/\tan z$). `np.diff(values, axis=1)` takes the differences of neighbours along each row; all positive means that $ds^2$ grows with $a_4$. `threshold[:, None]` turns the list into a column so that it is compared with every column of the grid; at every point not within $10^{-9}$ of the curve, $ds^2 > 0$ must hold exactly when $a_4 > a_4^{\ast}(z)$. Two PASS lines.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.5, 4.5))
image = left.imshow(np.tanh(values), origin="lower", aspect="auto", cmap="RdBu_r",
                    vmin=-1, vmax=1, extent=(a4_values[0], a4_values[-1],
                                             z_values[0], z_values[-1]))
left.plot(threshold, z_values, color="black", lw=1.5, label="$ds^2 = 0$")
left.set_xlim(a4_values[0], a4_values[-1])
left.grid(False)  # no grid lines across the coloured map
```

The left panel shows the whole grid as a coloured map. $\tanh$ squeezes every value into the range $-1$ to 1 while keeping its sign, so that red means space-like and blue time-like. `origin="lower"` puts the first row at the bottom, `extent` gives the map the coordinates of $a_4$ and $z$, and `aspect="auto"` lets it fill the panel. The black curve is $a_4^{\ast}(z)$.

```python
left.text(0.75, 0.4, "space-like\n$ds^2 > 0$", ha="center", color="white")
left.text(-0.9, 1.2, "time-like\n$ds^2 < 0$", ha="center", color="white")
left.set_xlabel("$a_4$")
left.set_ylabel("$z = 6 H x_8$")
left.set_title("sign of $ds^2$ for the step $dx^\\mu = \\epsilon$", fontsize=10)
left.legend(loc="upper right", fontsize=8)
fig.colorbar(image, ax=left, label="$\\tanh(ds^2/\\epsilon^2)$")
```

Two white labels (`\n` in a string starts a new line), the axis labels, the title, the legend and a colour bar.

```python
z_fixed = 0.9
s_fixed = np.sin(z_fixed) ** (1 / 3)
space_term = 3 * np.exp(2 * a4_values) * s_fixed  # x1, x2, x3
extra_term = -3 * np.exp(-2 * a4_values) * s_fixed  # x5, x6, x7 (deflating)
hidden_term = np.full_like(a4_values, 1 / np.tan(z_fixed) ** 2)  # x8
```

On the right, at $z = 0.9$, the four kinds of terms of the sum against $a_4$: the three space directions, the three deflating extra times, and the hidden direction (`np.full_like` makes an array of the same length filled with one value).

```python
right.plot(a4_values, space_term, color="tab:red", label="space $x_1, x_2, x_3$")
right.plot(a4_values, np.full_like(a4_values, -1.0), color="tab:gray",
           label="time $x_4$")
right.plot(a4_values, extra_term, color="tab:blue",
           label="extra times $x_5, x_6, x_7$")
right.plot(a4_values, hidden_term, color="tab:green", label="hidden $x_8$")
right.plot(a4_values, space_term - 1 + extra_term + hidden_term, "k", lw=2.5,
           label="sum $ds^2/\\epsilon^2$")
```

The four terms (the time term is the constant $-1$) and their sum as a thick black line.

```python
right.axhline(0, color="black", lw=0.8)
right.set_ylim(-12, 12)
right.set_xlabel("$a_4$")
right.set_ylabel("contribution to $ds^2/\\epsilon^2$")
right.set_title(f"the terms of $g_{{\\mu\\nu}} dx^\\mu dx^\\nu$ at $z = {z_fixed}$",
                fontsize=10)
right.legend(fontsize=8, loc="lower right")
fig.tight_layout()
save_figure(fig, "step_length",
            "The squared length $ds^2 = g_{\\mu\\nu} dx^\\mu dx^\\nu$ of the "
            ...)
```

The title is an f-string, so the braces of the LaTeX subscript are doubled. What Figure 01e.6 shows: on the left a blue (time-like) region to the left of the black curve and a red (space-like) region to its right; on the right the red space term climbing, the blue extra-time term rising from very negative values towards 0 as the extra times deflate, and the black sum crossing zero.

**In [16], the last check.**

```python
figure_names = ["01e_1_eta_and_delta.png", "01e_2_squared_lengths.png",
                "01e_3_symmetric_antisymmetric.png", "01e_4_clifford_tables.png",
                "01e_5_gamma_contractions.png", "01e_6_step_length.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all 6 figure files of this notebook exist")
all_checks_passed()
```

The last line is ALL 25 CHECKS PASSED (notebook 01e). The 25 checks are: 2 in In [2], 3 in In [3], 1 in In [5], 3 in In [6], 4 in In [8], 3 in In [10], 3 in In [12], 3 in In [14], 2 in In [15] and 1 in In [16].

### 1.34 Eigenvalues and eigenvectors; the characteristic polynomial

**Directions that are only stretched.** A square matrix $M$ usually turns a vector into a vector that points somewhere else. A few special directions are only stretched (or shrunk, or reversed):

$$
Mv = \lambda v,\qquad v \neq 0 .
$$

The number $\lambda$ (the Greek letter lambda) is an **eigenvalue** of $M$ and $v$ an **eigenvector** belonging to it. Any multiple $cv$ with $c \neq 0$ is an eigenvector too ($M(cv) = cMv = c\lambda v = \lambda(cv)$), so only the direction of $v$ matters. The list of all eigenvalues is the **spectrum** of $M$. Eigenvalues are everywhere in the course: the signature (4,4) of the author's spacetime is a count of positive and negative eigenvalues of its metric (Section 1.36); the gamma matrices are known by their eigenvalues (Section 1.37); and the energies of quantum states are eigenvalues (Chapters 10, 14 and 15).

**Why a determinant decides.** $Mv = \lambda v$ can be written

$$
(M - \lambda I)v = 0
$$

(move $\lambda v = \lambda Iv$ to the left side and take out $v$). If $\det(M - \lambda I) \neq 0$, the matrix $M - \lambda I$ can be undone (Section 1.20), and undoing it on both sides gives $v = 0$: no eigenvector. Conversely, if $\det(M - \lambda I) = 0$, the equation has a solution $v \neq 0$ (a standard theorem of linear algebra, ASSUMED). So the eigenvalues are exactly the numbers with

$$
p(\lambda) = \det(M - \lambda I) = 0 .
$$

$p$ is the **characteristic polynomial** of $M$. By the Leibniz formula every term of $\det(M - \lambda I)$ is a product of $n$ entries, of which at most $n$ (the diagonal ones) contain $\lambda$; so $p$ is a **polynomial** (a sum of powers of $\lambda$ with number coefficients) of degree $n$. A **root** of a polynomial is a number at which it is 0. The **fundamental theorem of algebra** (ASSUMED) says that a polynomial of degree $n$ has exactly $n$ roots $\lambda_1, \dots, \lambda_n$ when complex numbers are allowed and a repeated root is counted as often as it appears, its **multiplicity**. So an $n \times n$ matrix has $n$ eigenvalues, some of which may be complex or repeated.

**The eigenvalues add up to the trace and multiply to the determinant (PROVED).** A polynomial of degree $n$ whose highest term is $(-\lambda)^n$ and whose roots are $\lambda_1, \dots, \lambda_n$ is

$$
p(\lambda) = (\lambda_1 - \lambda)(\lambda_2 - \lambda)\cdots(\lambda_n - \lambda)
$$

(the factored form; the highest term of $\det(M - \lambda I)$ is the product of the $n$ diagonal terms $-\lambda$, which is $(-\lambda)^n$). Setting $\lambda = 0$:

$$
p(0) = \det M = \lambda_1\lambda_2\cdots\lambda_n
$$

(at $\lambda = 0$ the matrix $M - \lambda I$ is $M$): the determinant is the **product** of the eigenvalues. Multiplying out the factored form, the terms with $\lambda^{n-1}$ take $-\lambda$ from all brackets but one and $\lambda_i$ from that one, so they add up to $(-1)^{n-1}(\lambda_1 + \dots + \lambda_n)\lambda^{n-1}$. In the Leibniz formula only the product of the diagonal entries, $(M_{11} - \lambda)\cdots(M_{nn} - \lambda)$, contains $\lambda^{n-1}$ (every other term misses at least two diagonal entries, so it has at most $n - 2$ factors with $\lambda$), and in the same way its $\lambda^{n-1}$ terms are $(-1)^{n-1}(M_{11} + \dots + M_{nn})\lambda^{n-1}$. Comparing the two: the **sum** of the eigenvalues is the trace.

**A 2 × 2 example by hand (PROVED).** Take $M$ with the rows $(2, 1)$ and $(1, 2)$. Line by line:

$$
\det(M - \lambda I) = (2 - \lambda)(2 - \lambda) - 1\cdot 1
$$

(the determinant $ad - bc$ of the matrix with the rows $(2 - \lambda, 1)$ and $(1, 2 - \lambda)$),

$$
= \lambda^2 - 4\lambda + 4 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3)
$$

(multiply out; collect; two numbers whose product is 3 and whose sum is 4). So the eigenvalues are 1 and 3. For $\lambda = 3$ the equation $(M - 3I)v = 0$ has the rows $-v_1 + v_2 = 0$ and $v_1 - v_2 = 0$, which say the same, so $v = (1, 1)$; for $\lambda = 1$ it reads $v_1 + v_2 = 0$, so $v = (1, -1)$. Check: $3 + 1 = 4 = \mathrm{tr}\,M$ and $3 \cdot 1 = 3 = 2 \cdot 2 - 1 \cdot 1 = \det M$.

**What the example means (PROVED).** Take the vectors of length 1, $x = (\cos t, \sin t)$, which run around the unit circle as the angle $t$ runs from 0 to $2\pi$. Their images are $Mx = (2\cos t + \sin t, \cos t + 2\sin t)$, with the squared length

$$
(2\cos t + \sin t)^2 + (\cos t + 2\sin t)^2 = 4\cos^2 t + 4\cos t\sin t + \sin^2 t + \cos^2 t + 4\cos t\sin t + 4\sin^2 t = 5 + 8\cos t\sin t = 5 + 4\sin 2t
$$

(multiply out both squares; collect, with $\cos^2 t + \sin^2 t = 1$; the double-angle formula $2\sin t\cos t = \sin 2t$ of school trigonometry, ASSUMED). It is largest, $5 + 4 = 9$, where $\sin 2t = 1$, at $t = \pi/4$, the direction $(1, 1)/\sqrt 2$; and smallest, $5 - 4 = 1$, at $t = -\pi/4$, the direction $(1, -1)/\sqrt 2$. So the unit circle becomes an **ellipse** whose longest and shortest half-axes have the lengths $\sqrt 9 = 3$ and $\sqrt 1 = 1$, the two eigenvalues, and lie along the two eigenvectors (Figure 01g.1).

**The chain matrix of size 3 (PROVED).** The $3 \times 3$ **chain matrix** $T_3$ has 2 on the diagonal, $-1$ just above and just below it, and 0 elsewhere. With the six-term formula of Section 1.20 (the entries $a_{11} = a_{22} = a_{33} = 2 - \lambda$, $a_{12} = a_{21} = a_{23} = a_{32} = -1$, $a_{13} = a_{31} = 0$):

$$
\det(T_3 - \lambda I) = (2 - \lambda)^3 + 0 + 0 - (-1)(-1)(2 - \lambda) - (2 - \lambda)(-1)(-1) - 0
$$

(the six terms in the order of Section 1.20; the second, third and sixth contain $a_{13}$ or $a_{31}$, which are 0),

$$
= (2 - \lambda)^3 - 2(2 - \lambda) = (2 - \lambda)\big[(2 - \lambda)^2 - 2\big]
$$

(collect the two equal terms; take out the factor $2 - \lambda$). The roots are $\lambda = 2$ and $(2 - \lambda)^2 = 2$, that is $\lambda = 2 \pm \sqrt 2$. Multiplied out, $p(\lambda) = -\lambda^3 + 6\lambda^2 - 10\lambda + 4$ (from $(2 - \lambda)^3 = 8 - 12\lambda + 6\lambda^2 - \lambda^3$ and $-2(2 - \lambda) = -4 + 2\lambda$). The sum of the roots is $6 = \mathrm{tr}\,T_3$, and their product is $(2 - \sqrt 2)\cdot 2\cdot(2 + \sqrt 2) = 2(4 - 2) = 4 = p(0) = \det T_3$ (Figure 01g.2).

### 1.35 The chain matrix of any size; rotations and boosts; conjugate pairs

**The chain matrix $T_n$ (PROVED).** Row $j$ of $T_n v$ is $-v_{j-1} + 2v_j - v_{j+1}$, where we put $v_0 = v_{n+1} = 0$ (the first and the last row have only one neighbour; a missing neighbour counts as 0). Try $v_j = \sin(j\theta)$ for an angle $\theta$:

$$
\sin((j - 1)\theta) + \sin((j + 1)\theta) = 2\sin(j\theta)\cos\theta
$$

(the addition theorems $\sin(x \pm y) = \sin x\cos y \pm \cos x\sin y$ with $x = j\theta$ and $y = \theta$, added; the terms $\cos x\sin y$ cancel), so

$$
-v_{j-1} + 2v_j - v_{j+1} = 2\sin(j\theta) - 2\sin(j\theta)\cos\theta = (2 - 2\cos\theta)\sin(j\theta)
$$

(insert; take out the common factor). This is $\lambda v_j$ with $\lambda = 2 - 2\cos\theta$, provided the two end conditions hold. The start $v_0 = \sin 0 = 0$ holds for every $\theta$. The end $v_{n+1} = \sin((n + 1)\theta) = 0$ holds when $(n + 1)\theta$ is a whole multiple of $\pi$, $\theta = k\pi/(n + 1)$. For $k = 1, \dots, n$ this gives $n$ different eigenvalues

$$
\lambda_k = 2 - 2\cos\frac{k\pi}{n + 1},\qquad k = 1, \dots, n
$$

(different because the cosine decreases between 0 and $\pi$), with the eigenvectors $v_j = \sin(jk\pi/(n + 1))$: sine waves sampled at the points $j = 1, \dots, n$, with $k$ half waves along the chain. For $n = 3$ they are $2 - 2\cos(\pi/4) = 2 - \sqrt 2$, $2 - 2\cos(\pi/2) = 2$ and $2 - 2\cos(3\pi/4) = 2 + \sqrt 2$, as found above. This matrix comes back whenever a second derivative is computed on a grid of points (Chapter 2): then the sine waves are the shapes of a vibrating string or of a quantum particle in a box. Notebook 01g, In [5], checks the formula for $n = 10$: numpy's eigenvalues differ from it by at most $8.9 \times 10^{-16}$ (COMPUTED; Figure 01g.3).

**Rotations have complex eigenvalues (PROVED).** The rotation matrix $R(\alpha)$ of Section 1.12 turns every vector, so for $0 < \alpha < \pi$ no real direction is kept. Its characteristic polynomial is

$$
(\cos\alpha - \lambda)^2 + \sin^2\alpha = \lambda^2 - 2\cos\alpha\,\lambda + 1
$$

(the determinant $ad - bc$ of the matrix with the rows $(\cos\alpha - \lambda, -\sin\alpha)$ and $(\sin\alpha, \cos\alpha - \lambda)$; multiply out and use $\cos^2\alpha + \sin^2\alpha = 1$). By the formula for the roots of a quadratic $\lambda^2 + p\lambda + q$, $\lambda = -p/2 \pm \sqrt{p^2/4 - q}$ (school algebra, ASSUMED),

$$
\lambda = \cos\alpha \pm \sqrt{\cos^2\alpha - 1} = \cos\alpha \pm \sqrt{-\sin^2\alpha} = \cos\alpha \pm i\sin\alpha = e^{\pm i\alpha}
$$

(insert $p = -2\cos\alpha$, $q = 1$; $\cos^2 - 1 = -\sin^2$; a square root of $-x^2$ is $ix$, because $(ix)^2 = -x^2$; Euler's formula): two complex numbers of modulus 1. The eigenvectors are $(1, \mp i)$: $R(\alpha)(1, -i) = (\cos\alpha + i\sin\alpha, \sin\alpha - i\cos\alpha) = e^{i\alpha}(1, -i)$, because $e^{i\alpha}\cdot(-i) = -i\cos\alpha + \sin\alpha$ (row times column; multiply out). For $\alpha = \pi/2$, $R$ is the matrix $J$ of Section 1.12, whose eigenvalues are $\pm i$: the real matrix that plays the role of $i$ has the eigenvalues $\pm i$.

**Boosts have real eigenvalues.** The boost $\Lambda(\varphi)$ of Section 1.13 has the characteristic polynomial $(\cosh\varphi - \lambda)^2 - \sinh^2\varphi = \lambda^2 - 2\cosh\varphi\,\lambda + 1$ (now with $\cosh^2 - \sinh^2 = 1$), whose roots are $\cosh\varphi \pm \sqrt{\cosh^2\varphi - 1} = \cosh\varphi \pm \sinh\varphi = e^{\pm\varphi}$ (for $\varphi \geq 0$, where $\sinh\varphi \geq 0$), with the eigenvectors $(1, \pm 1)$, the two light-like directions found in Section 1.13 (PROVED). Their product is 1 (Figure 01g.4).

**Complex eigenvalues of a real matrix come in pairs (PROVED).** If $M$ is real and $Mv = \lambda v$, conjugating every entry gives $M^* v^* = \lambda^* v^*$, and $M^* = M$; so $Mv^* = \lambda^* v^*$: $\lambda^*$ is an eigenvalue too, with the eigenvector $v^*$. Notebook 01g, In [6], checks this on 200 random real $5 \times 5$ matrices.

### 1.36 Symmetric and Hermitian matrices; the signature and Sylvester's law

**Words.** The **conjugate transpose** of a matrix is $M^\dagger = (M^*)^T$: conjugate every entry, then exchange rows and columns; for a column $v$, $v^\dagger$ is the row of the conjugated components, and $v^\dagger v = \sum_i |v_i|^2$, which is positive for $v \neq 0$. Like the transpose it reverses products, $(AB)^\dagger = B^\dagger A^\dagger$ (the conjugate of a product of matrices is the product of the conjugates, entry by entry, by rule 1 of Section 1.10; then the transpose rule of Section 1.18). A matrix is **Hermitian** if $H^\dagger = H$; a real Hermitian matrix is a symmetric matrix. The **length** of a real vector is $|v| = \sqrt{v_1^2 + \dots + v_n^2}$; two real vectors are **perpendicular** (or orthogonal) if $u^Tw = \sum_i u_iw_i = 0$.

**Theorem 1: a symmetric matrix has only real eigenvalues (PROVED).** Let $S$ be real and symmetric, and $Sv = \lambda v$ with a column $v \neq 0$ that may be complex.

- Conjugate and transpose both sides: $v^\dagger S^\dagger = \lambda^* v^\dagger$ (the product rule of $\dagger$; a number only gets conjugated), and $S^\dagger = S$ because $S$ is real ($S^* = S$) and symmetric ($S^T = S$); so $v^\dagger S = \lambda^* v^\dagger$.
- Multiply $Sv = \lambda v$ from the left by $v^\dagger$: $v^\dagger Sv = \lambda\,v^\dagger v$.
- Multiply $v^\dagger S = \lambda^* v^\dagger$ from the right by $v$: $v^\dagger Sv = \lambda^*\,v^\dagger v$.
- Subtract the two lines: $0 = (\lambda - \lambda^*)\,v^\dagger v$.
- $v^\dagger v = |v_1|^2 + \dots + |v_n|^2 > 0$, so $\lambda - \lambda^* = 0$: $\lambda$ equals its conjugate, so it is real.

The same lines, with $S^\dagger = S$ as the only property used, prove it for a complex Hermitian matrix.

**Theorem 2: eigenvectors with different eigenvalues are perpendicular (PROVED).** Let $Su = \lambda u$ and $Sw = \mu w$ with $\lambda \neq \mu$ (real vectors, real eigenvalues). Then $u^TSw = \mu\,u^Tw$ (insert $Sw$), and also $u^TSw = (S^Tu)^Tw = (Su)^Tw = \lambda\,u^Tw$ (the transpose rule; $S^T = S$; insert $Su$). Subtracting: $(\lambda - \mu)\,u^Tw = 0$, so $u^Tw = 0$.

**The spectral theorem (ASSUMED).** A standard theorem of linear algebra, used here without proof, says that also when eigenvalues repeat, a real symmetric $n \times n$ matrix has $n$ perpendicular eigenvectors of length 1, and that, with these eigenvectors as the columns of a matrix $O$,

$$
S = O\Lambda O^T ,\qquad O^TO = I,
$$

with the eigenvalues on the diagonal of the diagonal matrix $\Lambda$ ($O$ is orthogonal, Section 1.28). One can see that both sides do the same to every eigenvector: $O^Tu_i = e_i$, the $i$-th unit vector, because the columns of $O$ are perpendicular and of length 1; so $O\Lambda O^Tu_i = O\Lambda e_i = \lambda_iOe_i = \lambda_iu_i = Su_i$. Notebook 01g, In [8], checks this for 300 random symmetric $8 \times 8$ matrices $S = A + A^T$: every eigenvalue is real (the largest imaginary part found by the general eigenvalue program is 0.0) and $O\Lambda O^T = S$ to $10^{-12}$; the 300 non-symmetric matrices $A$ have 67.7 per cent complex eigenvalues (COMPUTED; Figure 01g.5).

**The quadratic form and the signature.** A symmetric matrix $S$ defines the **quadratic form** $Q(v) = v^TSv = S_{ab}v^av^b$; for the frame metric it is the squared length of Section 1.27. In the eigenvector coordinates $v = Ow$:

$$
Q = (Ow)^TS(Ow) = w^T(O^TSO)w = w^T\Lambda w = \lambda_1w_1^2 + \dots + \lambda_nw_n^2
$$

(insert; the transpose rule $(Ow)^T = w^TO^T$; $O^TSO = O^TO\Lambda O^TO = \Lambda$; a diagonal matrix in a quadratic form gives a sum of squares). So the **signature** $(p, q)$ of a symmetric matrix, the numbers of its positive and its negative eigenvalues, says in how many perpendicular directions $Q$ is positive and in how many it is negative. An eigenvalue 0 would be a direction in which $Q$ vanishes; the metrics of the course have none (their determinants, the products of the eigenvalues, are not 0).

**Sylvester's law of inertia (PROVED from one ASSUMED fact).** A change of coordinates $v = Pw$ with an invertible matrix $P$ gives $Q = w^T(P^TSP)w$: the matrix of the form becomes $P^TSP$. Its eigenvalues are different, but its signature is the same. We use one fact of linear algebra without proof (ASSUMED): more than $n$ vectors with $n$ components are **linearly dependent**, that is, some combination $c_1u_1 + c_2u_2 + \cdots$ with numbers $c_i$ not all 0 gives the zero vector. *Proof.* Let $S$ have $p$ positive eigenvalues with perpendicular unit eigenvectors $u_1, \dots, u_p$, and let $S' = P^TSP$ have $p'$ positive eigenvalues; suppose $p' < p$.

- On every combination $x = \sum_i c_iu_i$ with not all $c_i = 0$: $Q(x) = \sum_i\sum_j c_ic_j\,u_i^TSu_j = \sum_i\lambda_ic_i^2 > 0$ (multiply out; $Su_j = \lambda_ju_j$ and $u_i^Tu_j = \delta_{ij}$ by Theorem 2 and the length 1; every $\lambda_i > 0$).
- Let $u'_1, \dots, u'_{n-p'}$ be perpendicular unit eigenvectors of $S'$ with eigenvalues $\leq 0$. On every combination $y = \sum_k d_ku'_k$: $y^TS'y = \sum_k\lambda'_kd_k^2 \leq 0$ (the same computation), and $y^TS'y = (Py)^TS(Py) = Q(Py)$ (the definition of $S'$; the transpose rule).
- The $p + (n - p') > n$ vectors $u_1, \dots, u_p, Pu'_1, \dots, Pu'_{n-p'}$ are linearly dependent: $\sum_i c_iu_i + \sum_k d_kPu'_k = 0$ with numbers not all 0. Put $x = \sum_i c_iu_i$ and $y = -\sum_k d_ku'_k$, so $x = Py$. If all $c_i$ were 0, then $P\sum_k d_ku'_k = 0$, hence $\sum_k d_ku'_k = 0$ ($P$ can be undone), hence all $d_k = 0$ (multiply by $u'^T_l$ and use the perpendicularity); so some $c_i \neq 0$.
- Then $Q(x) > 0$ by the first line, but $Q(x) = Q(Py) \leq 0$ by the second: impossible.

So $p' \geq p$. The same argument with the roles exchanged ($S = (P^{-1})^TS'P^{-1}$) gives $p \geq p'$, and the argument for $-S$ counts the negative eigenvalues. So **the signature is a property of the form, not of the coordinates used to describe it.** Notebook 01g, In [10], checks the law on 2000 random matrices $P$: every $P^T\eta P$ has the signature (4,4), with eigenvalues of sizes from $1.2 \times 10^{-8}$ to 37.1, all far enough from 0 that rounding cannot change their signs (COMPUTED; Figure 01g.6, left).

**The signature of the author's spacetime (PROVED).** The eigenvalues of a diagonal matrix are its diagonal entries (each unit vector $e_i$ is an eigenvector: $De_i = d_ie_i$). So $\eta$ has the eigenvalues $+1$ (four times) and $-1$ (four times): the signature (4,4) (record `Revision/algebra/reports/python-algebra.json`, check `coordinate_map`, which states $\eta$). The author's metric $g$ has the eigenvalues $e^{2a_4}s > 0$ (three times), $-1$, $-e^{-2a_4}s < 0$ (three times) and $\cot^2 z > 0$, for every $a_4$ and every $0 < z < \pi/2$: again four positive and four negative. As $a_4$ grows the three extra-time eigenvalues $-e^{-2a_4}s$ shrink towards 0, the exponential deflation of the extra times, but they never change sign; and their product with the others is $\det g = \cos^2 z > 0$ (Section 1.21). Notebook 01g, In [11], checks the signs at $61 \times 50 = 3050$ grid points $(a_4, z)$ and the product to $10^{-12}$ (COMPUTED; Figure 01g.6, right).

### 1.37 The eigenvalues of the gamma matrices and of B; power iteration

**The gamma matrices (PROVED).** The gamma matrices obey $(\gamma^a)^2 = \eta^{aa}I$ (Section 1.28). If $\gamma^av = \lambda v$ with $v \neq 0$, then

$$
(\gamma^a)^2v = \gamma^a(\lambda v) = \lambda\,\gamma^av = \lambda^2v
$$

(apply $\gamma^a$ twice; a number can be moved in front of a matrix), and also $(\gamma^a)^2v = \eta^{aa}v$. So $\lambda^2 = \eta^{aa}$: $\lambda = \pm 1$ for the space-like directions $x_1, x_2, x_3, x_8$ and $\lambda = \pm i$ for the time-like directions $x_4, \dots, x_7$. How many of each? The trace of a gamma matrix is 0: for any $b \neq a$,

$$
\mathrm{tr}\,\gamma^a = \eta^{bb}\,\mathrm{tr}(\gamma^b\gamma^b\gamma^a) = \eta^{bb}\,\mathrm{tr}(\gamma^b\gamma^a\gamma^b) = -\eta^{bb}\,\mathrm{tr}(\gamma^b\gamma^b\gamma^a) = -\mathrm{tr}\,\gamma^a
$$

(insert $\eta^{bb}(\gamma^b)^2 = \eta^{bb}\eta^{bb}I = I$; the trace does not change when the first factor is moved to the end, $\mathrm{tr}(XY) = \mathrm{tr}(YX)$ with $X = \gamma^b$; the anticommutation $\gamma^a\gamma^b = -\gamma^b\gamma^a$ for $a \neq b$; the first step backwards), and a number equal to its own negative is 0. The trace is the sum of the 16 eigenvalues (Section 1.34), so $+1$ and $-1$ (or $+i$ and $-i$) occur 8 times each, and the characteristic polynomial is $(\lambda - 1)^8(\lambda + 1)^8 = (\lambda^2 - 1)^8$ for a space-like and $(\lambda - i)^8(\lambda + i)^8 = (\lambda^2 + 1)^8$ for a time-like direction, in one formula $(\lambda^2 - \eta_{aa})^8$. (sympy's `charpoly` computes $\det(\lambda I - M)$, which for a $16 \times 16$ matrix equals $\det(M - \lambda I)$, because changing the sign of all 16 rows multiplies the determinant by $(-1)^{16} = 1$, rule 5 of Section 1.20.) Notebook 01g, In [13], checks this exactly for the eight matrices of the record (Figure 01g.7, left).

**The gamma matrix of a vector (PROVED).** For a vector $v$ the matrix $\gamma(v) = v_a\gamma^a$ (with $v_a = \eta_{ab}v^b$) squares to

$$
\gamma(v)^2 = v_av_b\,\gamma^a\gamma^b = \tfrac12v_av_b\big(\gamma^a\gamma^b + \gamma^b\gamma^a\big) = v_av_b\,\eta^{ab}I = Q(v)\,I
$$

(multiply out the two sums; the numbers $v_av_b$ are symmetric in $a$ and $b$, so only the symmetric part of $\gamma^a\gamma^b$ counts, by the argument of Section 1.28 applied entry by entry; the Clifford relation; $v_av_b\eta^{ab} = v_av^a = Q(v)$). So, as above, its eigenvalues are $\pm\sqrt{Q(v)}$: real for a space-like, imaginary for a time-like $v$ (eight of each sign, because $\mathrm{tr}\,\gamma(v) = v_a\,\mathrm{tr}\,\gamma^a = 0$). For a light-like $v \neq 0$, $\gamma(v)$ is not the zero matrix, because $\mathrm{tr}(\gamma(v)\gamma^b) = v_a\,\mathrm{tr}(\gamma^a\gamma^b) = 16\,v_a\eta^{ab} = 16\,v^b$ (the third contraction of Section 1.28; raising the index) is not 0 for a component $v^b \neq 0$; but $\gamma(v)^2 = 0$: a matrix with a power equal to 0 is called **nilpotent**, and all its eigenvalues are 0 ($\lambda^2v = \gamma(v)^2v = 0$ gives $\lambda = 0$); its characteristic polynomial is $\lambda^{16}$. Notebook 01g, In [14], checks $\gamma(v)^2 = Q(v)I$ exactly for four examples and 100 random vectors (Figure 01g.7, right).

**The Hermitian matrix B and its signature (8,8).** The Revision record stores, in `Revision/algebra/gammas.json`, the real matrix $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$ and the matrix $B = -i\,C\gamma^{(x_4)}$. $B$ is complex: its real part is 0 and its imaginary part is a real $16 \times 16$ matrix of entries $-1$, 0, 1. In the theory of the course $B$ gives the charge density $J^{(x_4)} = \Psi^\dagger B\Psi$ of the fields (Chapters 7 and 10). Its properties:

- $B$ is Hermitian. For a matrix $iA$ with real $A$, $(iA)^\dagger = i^*A^T = -iA^T$ (conjugate the number $i$; a real matrix only gets transposed), so $(iA)^\dagger = iA$ means $A^T = -A$: $B$ is Hermitian exactly when its imaginary part is antisymmetric. By Theorem 1 its eigenvalues are real.
- $B^2 = I$, so, as for the gamma matrices, every eigenvalue has $\lambda^2 = 1$: $\lambda = \pm 1$.
- $\mathrm{tr}\,B = 0$, so $+1$ and $-1$ occur 8 times each: the signature (8,8), and the characteristic polynomial is $(\lambda - 1)^8(\lambda + 1)^8$.

The record checks these properties in `Revision/algebra/reports/python-algebra.json`, check `B_hermitian_involution_signature`, and in `Revision/theory/reports/python-field-theory.json`, check `B_properties`; Notebook 01g, In [16], reproduces them exactly from the record's matrices (PROVED by exact computation; Figure 01g.8). Because half of the eigenvalues of $B$ are negative, the charge $\Psi^\dagger B\Psi$ can be positive or negative: the record calls it an **indefinite** form, and its quantisation entry reads "B Hermitian, B^2 = 1, signature (8,8): indefinite (Krein) state space". Chapter 10 explains what this means for the quantised field.

**Power iteration (PROVED).** A computer does not find eigenvalues as the roots of $\det(M - \lambda I)$ (that polynomial is very sensitive to rounding for large matrices); it transforms the matrix step by step. The simplest such method is **power iteration**. Write a starting vector as a sum of eigenvectors, $x_0 = c_1u_1 + c_2u_2 + \cdots$, with $|\lambda_1| > |\lambda_2| \geq \cdots$ and $c_1 \neq 0$. Multiplying by $M$ $k$ times gives

$$
M^kx_0 = c_1\lambda_1^ku_1 + c_2\lambda_2^ku_2 + \cdots = \lambda_1^k\Big(c_1u_1 + c_2\Big(\frac{\lambda_2}{\lambda_1}\Big)^ku_2 + \cdots\Big)
$$

(each eigenvector is only multiplied by its eigenvalue, once per step; then $\lambda_1^k$ is taken out). The ratios $(\lambda_j/\lambda_1)^k$ shrink to 0, so the direction of $M^kx_0$ approaches $u_1$, and the leftover error shrinks by the factor $|\lambda_2/\lambda_1|$ in each step. Rescaling the vector to length 1 after each step keeps its numbers from growing without changing its direction. For the matrix $M$ of Section 1.34 the factor is $1/3$; for $T_3$ it is

$$
\frac{2}{2 + \sqrt 2} = \frac{2(2 - \sqrt 2)}{(2 + \sqrt 2)(2 - \sqrt 2)} = \frac{2(2 - \sqrt 2)}{2} = 2 - \sqrt 2 \approx 0.586
$$

(multiply numerator and denominator by $2 - \sqrt 2$; $(2 + \sqrt 2)(2 - \sqrt 2) = 4 - 2$). Notebook 01g, In [18], measures 0.333333 and 0.585786 to 0.585789 (COMPUTED; Figure 01g.9).

### 1.38 Example: eigenvalues, eigenvectors and the signature (4,4)

Notebook 01g puts Sections 1.34 to 1.37 to work. It finds the eigenvalues of a $2 \times 2$ matrix by hand and with sympy and numpy and draws how the matrix turns the unit circle into an ellipse; computes the characteristic polynomial of the chain matrix and checks its exact eigenvalues and sine-wave eigenvectors; checks the complex eigenvalues of rotations and the real eigenvalues of boosts; checks on random matrices that symmetric matrices have real eigenvalues and perpendicular eigenvectors; reads $\eta$ and the author's metric from the Revision record, counts their positive and negative eigenvalues and checks Sylvester's law on 2000 random coordinate changes; derives and checks the eigenvalues of the eight gamma matrices and of $\gamma(v)$; finds the signature (8,8) of the record's matrix $B$; and runs power iteration. It ends with the line ALL 30 CHECKS PASSED (notebook 01g).

<!-- NOTEBOOK 01g -->

### 1.41 Line-by-line walk-through of Notebook 01g

The notebook has nineteen code cells, In [1] to In [19]. As in Section 1.9, a quoted line `...)` stands for the remaining lines of a figure caption, which Section 1.40 prints in full under its figure.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 1.39; its code is the set-up code explained in Section 1.9, with `NOTEBOOK_ID = "01g"`. It prints Set-up of notebook 01g complete: repository folder found, helpers defined.

**In [2], a 2 × 2 example.**

```python
import math  # square roots and pi

import numpy as np  # arrays and numerical linear algebra
import sympy as sp  # exact algebra
```

The modules: `math` for square roots and $\pi$, numpy for numerical linear algebra (its sub-module `np.linalg` holds the eigenvalue programs), sympy for exact algebra.

```python
lam = sp.Symbol("lambda")  # the unknown eigenvalue
M = sp.Matrix([[2, 1], [1, 2]])
char_poly = sp.expand((M - lam * sp.eye(2)).det())  # det(M - lambda I)
say(f"det(M - lambda I) = {char_poly} = {sp.factor(char_poly)}")
```

A symbol for $\lambda$ (named `lam`, because `lambda` is a reserved word of Python), the matrix $M$, and its characteristic polynomial $\det(M - \lambda I)$, multiplied out. `sp.factor` writes it as a product. Output: `det(M - lambda I) = lambda**2 - 4*lambda + 3 = (lambda - 3)*(lambda - 1)`.

```python
eigenvalues = sorted(sp.solve(char_poly, lam))  # the roots
check(eigenvalues == [1, 3], "the eigenvalues of M are 1 and 3")
v3, v1 = sp.Matrix([1, 1]), sp.Matrix([1, -1])
check(M * v3 == 3 * v3 and M * v1 == 1 * v1,
      "M (1, 1) = 3 (1, 1) and M (1, -1) = 1 (1, -1)")
check(sum(eigenvalues) == M.trace() == 4 and eigenvalues[0] * eigenvalues[1]
      == M.det() == 3, "sum of the eigenvalues = trace = 4, product = det = 3")
```

`sp.solve(p, lam)` returns the roots of $p$, and `sorted` puts them in increasing order. Three exact checks: the eigenvalues 1 and 3, the two eigenvector equations $Mv = \lambda v$, and the sum and product rules of Section 1.34.

```python
values, vectors = np.linalg.eigh(np.array(M.tolist(), dtype=float))
# The sign of an eigenvector is free (v and -v are both eigenvectors), and
# different computers may return either; make the first entry of each column
# positive so that every computer prints the same.
vectors = vectors * np.sign(vectors[0])
```

`np.linalg.eigh` is numpy's eigenvalue program for symmetric (and Hermitian) matrices; it returns the eigenvalues from the smallest up and the eigenvectors, of length 1, as the columns of a matrix. Because $v$ and $-v$ are both eigenvectors, the program may return either; `np.sign(vectors[0])` is the sign of the first entry of each column, and multiplying each column by it makes that entry positive, so that every computer prints the same.

```python
say(f"numpy eigh: eigenvalues {values.round(12).tolist()}")
say(f"            eigenvectors (columns) {vectors.round(6).tolist()}")
check(np.allclose(values, [1.0, 3.0], atol=1e-12) and
      abs(abs(vectors[:, 1] @ np.array([1.0, 1.0])) - math.sqrt(2)) < 1e-12,
      "numpy finds the eigenvalues 1, 3 and the direction (1, 1) for 3")
```

The results, rounded (`.round(12)`: 12 digits after the point), printed as `[1.0, 3.0]` and the columns `[[0.707107, 0.707107], [-0.707107, 0.707107]]` (the rows of the matrix are printed; its first column is $(1, -1)/\sqrt 2$, its second $(1, 1)/\sqrt 2$, and $1/\sqrt 2 = 0.707107$). The check: the eigenvalues, and the second column has the dot product $\pm\sqrt 2$ with $(1, 1)$, so it is $\pm(1, 1)/\sqrt 2$. The cell prints four PASS lines.

**In [3], the unit circle becomes an ellipse.**

```python
angles = np.linspace(0.0, 2.0 * np.pi, 721)  # every half degree
circle = np.array([np.cos(angles), np.sin(angles)])  # 2 rows: x and y
M_numbers = np.array(M.tolist(), dtype=float)
ellipse = M_numbers @ circle  # every point of the circle multiplied by M
lengths = np.sqrt((ellipse ** 2).sum(axis=0))  # length of every image
say(f"longest image {lengths.max():.6f}, shortest image {lengths.min():.6f}")
check(abs(lengths.max() - 3) < 1e-9 and abs(lengths.min() - 1) < 1e-4,
      "the unit circle becomes an ellipse with half-axes 3 and 1")
```

721 points of the unit circle (every half degree) as a table with two rows; their images under $M$; the length of every image (square the entries, add the two rows with `.sum(axis=0)`, take the root). Output: longest image 3.000000, shortest image 1.000000, the half-axes of Section 1.34. The check uses a tight tolerance for the longest and a looser one, $10^{-4}$, for the shortest length; the printed values show that both are met with room to spare.

```python
fig, ax = plt.subplots(figsize=(6.6, 6.0))
ax.plot(circle[0], circle[1], color="0.6", label="unit circle")
ax.plot(ellipse[0], ellipse[1], color="black", label="its image under $M$")
arrows = [(np.array([1.0, 1.0]) / math.sqrt(2), "tab:red", "eigenvector, 3"),
          (np.array([1.0, -1.0]) / math.sqrt(2), "tab:blue", "eigenvector, 1"),
          (np.array([1.0, 0.0]), "tab:green", "u = (1, 0)")]
```

The circle in grey and the ellipse in black; a list of three vectors of length 1 with colours and names: the two eigenvectors and $u = (1, 0)$.

```python
for vector, color, name in arrows:
    image = M_numbers @ vector
    # the image first: thick, dashed and see-through, so that the vector drawn
    # on top of it stays visible where the two coincide
    ax.annotate("", xy=image, xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "color": color, "lw": 5,
                            "linestyle": "--", "alpha": 0.4})
    ax.annotate("", xy=vector, xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
    ax.plot([], [], color=color, lw=2, label=f"{name} (dashed: its image)")
```

For each vector its image is drawn first as a thick, dashed, see-through arrow, then the vector itself as a thin solid arrow on top. `ax.plot([], [], ...)` draws nothing (empty lists) but makes an entry for the legend.

```python
ax.set_aspect("equal")
ax.set_xlim(-3.3, 3.3)
ax.set_ylim(-3.3, 3.3)
ax.set_xlabel("first component")
ax.set_ylabel("second component")
ax.set_title("$M$ with rows (2, 1), (1, 2) acting on the plane")
ax.legend(loc="lower right", fontsize=8)
save_figure(fig, "circle_to_ellipse",
            "The unit circle (grey) and its image under the matrix $M$ with rows "
            ...)
```

What Figure 01g.1 shows: the red eigenvector and its image point the same way, the image three times as long; the blue eigenvector's image lies on top of it (eigenvalue 1); the green $u$ is turned to $(2, 1)$; the ellipse's long axis lies along the red, its short axis along the blue direction.

**In [4], the characteristic polynomial of the chain matrix.**

```python
T3 = sp.Matrix([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
p3 = sp.expand((T3 - lam * sp.eye(3)).det())
say(f"det(T3 - lambda I) = {p3} = {sp.factor(p3)}")
roots3 = sorted(sp.roots(p3, lam).keys(), key=lambda r: float(r))  # small first
say(f"roots: {roots3}")
```

The chain matrix $T_3$ and its characteristic polynomial, multiplied out and factored: `-lambda**3 + 6*lambda**2 - 10*lambda + 4 = -(lambda - 2)*(lambda**2 - 4*lambda + 2)`, as derived in Section 1.34. `sp.roots` returns a dictionary from the roots to their multiplicities; its keys are sorted by their numerical value (`key=lambda r: float(r)` tells `sorted` to compare the roots as decimal numbers). Output: `roots: [2 - sqrt(2), 2, sqrt(2) + 2]`.

```python
check(roots3 == [2 - sp.sqrt(2), 2, 2 + sp.sqrt(2)],
      "the eigenvalues of T3 are 2 - sqrt 2, 2 and 2 + sqrt 2")
check(sp.simplify(sum(roots3) - T3.trace()) == 0 and
      sp.simplify(roots3[0] * roots3[1] * roots3[2] - T3.det()) == 0,
      "sum of the eigenvalues = trace = 6, product = det = 4")
```

The exact roots and the sum and product rules. Two PASS lines.

```python
p3_numbers = sp.lambdify(lam, p3, "numpy")  # the polynomial as a numpy function
grid = np.linspace(-0.2, 4.2, 400)
fig, ax = plt.subplots(figsize=(7.2, 4.2))
ax.plot(grid, p3_numbers(grid), color="black", label="$p(\\lambda)$")
ax.axhline(0.0, color="0.5", lw=0.8)
root_values = [float(r) for r in roots3]
ax.plot(root_values, [0.0, 0.0, 0.0], "o", color="tab:red", ms=8,
        label="roots = eigenvalues")
```

The polynomial as a numpy function, drawn for 400 values of $\lambda$ from $-0.2$ to 4.2, a grey zero line, and the three roots as red dots on it.

```python
for r_text, r_value in zip(["$2 - \\sqrt{2}$", "$2$", "$2 + \\sqrt{2}$"],
                           root_values):
    ax.text(r_value, 0.6, r_text, ha="center", color="tab:red")
ax.set_xlabel("$\\lambda$")
ax.set_ylabel("$p(\\lambda) = \\det(T_3 - \\lambda I)$")
ax.set_title("The characteristic polynomial of the chain matrix $T_3$")
ax.set_ylim(-3.0, 5.0)
ax.legend(loc="upper right");
save_figure(fig, "characteristic_polynomial",
            "The characteristic polynomial $p(\\lambda) = \\det(T_3 - \\lambda I) "
            ...)
```

Each root labelled above its dot, axis labels, title, range, legend (with the semicolon of Section 1.9). What Figure 01g.2 shows: the cubic curve crosses zero exactly at $2 - \sqrt 2$, 2 and $2 + \sqrt 2$, and meets the vertical axis at $p(0) = 4 = \det T_3$.

**In [5], the chain matrix of size 10.**

```python
n = 10
T = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)  # k=1: just above the diagonal
values_T, vectors_T = np.linalg.eigh(T)  # eigenvalues from the smallest up
k = np.arange(1, n + 1)
formula = 2 - 2 * np.cos(k * np.pi / (n + 1))
say(f"largest difference eigh - formula: {np.max(np.abs(values_T - formula)):.1e}")
check(np.allclose(values_T, formula, rtol=0, atol=1e-12),
      "T_10 has the eigenvalues 2 - 2 cos(k pi/11), k = 1 ... 10")
```

`np.eye(n, k=1)` has ones just above the diagonal and `k=-1` just below, so `T` is $T_{10}$. Its eigenvalues from numpy are compared with the formula $2 - 2\cos(k\pi/11)$ of Section 1.35 (which is increasing in $k$, the same order). Output: largest difference eigh - formula: 8.9e-16.

```python
j = np.arange(1, n + 1)  # the points of the chain
sines = np.array([np.sin(j * kk * np.pi / (n + 1)) for kk in k]).T  # columns
sines = sines / np.sqrt((sines ** 2).sum(axis=0))  # length 1
overlaps = np.abs((vectors_T * sines).sum(axis=0))  # |cos of the angle|, column-wise
check(np.allclose(overlaps, 1.0, rtol=0, atol=1e-12),
      "every eigenvector of T_10 is a sampled sine wave sin(j k pi/11)")
```

The sampled sine waves $\sin(jk\pi/11)$, one column for each $k$ (`.T` turns the rows into columns), scaled to length 1. For two vectors of length 1 the dot product is the cosine of the angle between them; it is $\pm 1$ exactly when they point along the same line. `(vectors_T * sines).sum(axis=0)` computes the dot product of each numpy eigenvector with its sine wave, column by column; all ten must be $\pm 1$. Two PASS lines.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
fine = np.linspace(0, n + 1, 400)  # the sine curves between the points
for kk, color in zip((1, 2, 3), ("tab:blue", "tab:orange", "tab:green")):
    column = vectors_T[:, kk - 1] * np.sign(vectors_T[0, kk - 1])  # first entry > 0
    scale = column[0] / math.sin(kk * math.pi / (n + 1))
    left.plot(fine, scale * np.sin(fine * kk * math.pi / (n + 1)), color=color, lw=1)
    left.plot(j, column, "o", color=color, label=f"$k = {kk}$")
```

For the three smallest eigenvalues ($k = 1, 2, 3$): the eigenvector, with the sign chosen so that its first entry is positive, is drawn as dots at the points $j = 1, \dots, 10$; through them the continuous sine curve, scaled to pass through the first dot (`scale`), drawn at 400 points from 0 to 11.

```python
left.axhline(0, color="0.5", lw=0.8)
left.set_xlabel("point $j$ of the chain")
left.set_ylabel("entry $v_j$ of the eigenvector")
left.set_title("the first three eigenvectors of $T_{10}$")
left.legend(fontsize=8)
fine_k = np.linspace(0, n + 1, 400)
right.plot(fine_k, 2 - 2 * np.cos(fine_k * np.pi / (n + 1)), color="black", lw=1,
           label="$2 - 2\\cos(k\\pi/11)$")
right.plot(k, values_T, "o", color="tab:red", label="eigenvalues from numpy")
right.set_xlabel("number $k$")
right.set_ylabel("eigenvalue $\\lambda_k$")
right.set_title("the ten eigenvalues of $T_{10}$")
right.legend(fontsize=8, loc="upper left")
fig.tight_layout()
save_figure(fig, "chain_matrix",
            "The $10 \\times 10$ chain matrix $T_{10}$ (2 on the diagonal, $-1$ "
            ...)
```

Labels of the left panel; on the right the curve $2 - 2\cos(k\pi/11)$ for continuous $k$ and the ten numpy eigenvalues as red dots. What Figure 01g.3 shows: the dots of the eigenvectors lie on half a sine wave ($k = 1$), a full wave ($k = 2$) and one and a half waves ($k = 3$), each vanishing at $j = 0$ and $j = 11$; the ten eigenvalues lie on the cosine curve.

**In [6], rotations, boosts and conjugate pairs.**

```python
alpha, phi = sp.symbols("alpha phi", real=True)
R = sp.Matrix([[sp.cos(alpha), -sp.sin(alpha)], [sp.sin(alpha), sp.cos(alpha)]])
p_rot = sp.expand((R - lam * sp.eye(2)).det())
check(sp.simplify(p_rot - (lam ** 2 - 2 * sp.cos(alpha) * lam + 1)) == 0,
      "det(R - lambda I) = lambda^2 - 2 cos(alpha) lambda + 1")
```

The rotation matrix with a symbolic angle, and its characteristic polynomial, which must simplify to $\lambda^2 - 2\cos\alpha\,\lambda + 1$ (Section 1.35).

```python
rot_ok = True
for sign_value in (1, -1):  # the eigenvalue e^(+-i alpha), eigenvector (1, -+i)
    eigen = sp.exp(sign_value * sp.I * alpha)
    vector = sp.Matrix([1, -sign_value * sp.I])
    gap = (R * vector - eigen * vector).applyfunc(
        lambda e: sp.simplify(sp.expand_complex(e)))
    rot_ok &= gap == sp.zeros(2, 1)
check(rot_ok, "R(alpha) (1, -+i) = e^(+-i alpha) (1, -+i) for every angle alpha")
```

For both signs: the eigenvalue $e^{\pm i\alpha}$ and the eigenvector $(1, \mp i)$; `gap` is $Rv - \lambda v$ with every entry written as real part plus $i$ times imaginary part (`expand_complex` uses Euler's formula) and simplified; it must be the zero column, for every angle.

```python
J = R.subs(alpha, sp.pi / 2)  # the matrix of i
say(f"J = {J.tolist()}, eigenvalues {sorted(J.eigenvals().keys(), key=str)}")
check(set(J.eigenvals().keys()) == {sp.I, -sp.I}, "the eigenvalues of J are +i, -i")
```

`.subs(alpha, sp.pi / 2)` puts $\alpha = \pi/2$ into the matrix, which gives $J$. `.eigenvals()` returns sympy's exact eigenvalues as a dictionary (eigenvalue: multiplicity); they are printed sorted by their text (`key=str`), so that the order is the same on every computer. Output: `J = [[0, -1], [1, 0]], eigenvalues [-I, I]`.

```python
boost = sp.Matrix([[sp.cosh(phi), sp.sinh(phi)], [sp.sinh(phi), sp.cosh(phi)]])
boost_ok = True
for sign_value in (1, -1):  # the eigenvalue e^(+-phi), eigenvector (1, +-1)
    vector = sp.Matrix([1, sign_value])
    gap = (boost * vector - sp.exp(sign_value * phi) * vector).applyfunc(
        lambda e: sp.simplify(e.rewrite(sp.exp)))
    boost_ok &= gap == sp.zeros(2, 1)
check(boost_ok, "a boost has the real eigenvalues e^(+-phi) with the light-like "
      "eigenvectors (1, +-1)")
```

The boost and its two eigenvalue equations, checked as in Notebook 01b, In [12] (Section 1.17).

```python
generator = np.random.default_rng(12345)  # random numbers with a fixed seed
pairs_ok = True
for _ in range(200):  # 200 random real 5 x 5 matrices
    found = np.linalg.eigvals(generator.normal(size=(5, 5)))
    pairs_ok &= np.allclose(np.sort_complex(found), np.sort_complex(found.conj()))
check(pairs_ok, "the complex eigenvalues of 200 random real 5 x 5 matrices come "
      "in conjugate pairs")
```

`np.linalg.eigvals` is numpy's eigenvalue program for any square matrix; it returns complex numbers. For each of 200 random real $5 \times 5$ matrices the list of eigenvalues, sorted (`np.sort_complex` sorts by real part, then imaginary part), must equal the sorted list of their conjugates: the conjugate-pair theorem of Section 1.35. The cell prints five PASS lines.

**In [7], the eigenvalues of rotations and boosts as pictures.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.6))
circle_line = np.exp(1j * np.linspace(0, 2 * np.pi, 400))
left.plot(circle_line.real, circle_line.imag, color="0.75", lw=1)
colors = plt.cm.viridis(np.linspace(0.0, 0.9, 6))  # six colours from a colour map
```

The unit circle of the complex plane in light grey, and six colours taken from the colour map viridis (`plt.cm.viridis(x)` gives the colour at the position $x$ between 0 and 1).

```python
for step, color in zip(range(1, 7), colors):
    angle = step * np.pi / 6
    eig = np.linalg.eigvals(np.array([[np.cos(angle), -np.sin(angle)],
                                      [np.sin(angle), np.cos(angle)]]))
    left.plot(eig.real, eig.imag, "o", color=color, ms=8,
              label=f"$\\alpha = {30 * step}$ degrees")
```

For the angles $\pi/6, 2\pi/6, \dots, \pi$ (30 to 180 degrees) the two eigenvalues of the rotation matrix, computed by numpy, are drawn in the complex plane.

```python
left.annotate("$+i$ (the matrix $J$)", xy=(0, 1), xytext=(0.25, 1.25), fontsize=8,
              arrowprops={"arrowstyle": "->"})
left.set_aspect("equal")
left.set_xlim(-1.5, 1.5)
left.set_ylim(-1.5, 1.5)
left.set_xlabel("real part")
left.set_ylabel("imaginary part")
left.set_title("rotations: $e^{\\pm i\\alpha}$")
left.legend(fontsize=7, loc="lower left")
```

An arrow with a label points at $+i$, the eigenvalue of $J$ (90 degrees); scales, labels, title and legend.

```python
rapidity = np.linspace(0.0, 1.5, 200)
right.plot(rapidity, np.exp(rapidity), color="tab:red", label="$e^{\\varphi}$")
right.plot(rapidity, np.exp(-rapidity), color="tab:blue", label="$e^{-\\varphi}$")
right.plot(rapidity, np.exp(rapidity) * np.exp(-rapidity), "k--", lw=1,
           label="their product = 1")
right.set_xlabel("rapidity $\\varphi$")
right.set_ylabel("eigenvalue")
right.set_title("boosts: real eigenvalues $e^{\\pm\\varphi}$")
right.legend(fontsize=8)
fig.tight_layout()
save_figure(fig, "rotation_and_boost",
            "Left: the eigenvalues $e^{\\pm i\\alpha}$ of the real rotation "
            ...)
```

On the right the two eigenvalues of a boost and their product against the rapidity. What Figure 01g.4 shows: on the left each pair of dots lies on the unit circle, mirror-symmetric in the real axis, the pair moving from near 1 (30 degrees) to $-1$ (180 degrees, where the two coincide); on the right one growing and one decaying exponential whose product stays 1.

**In [8], symmetric matrices, on random examples.**

```python
symmetric_spectra, general_spectra = [], []
largest_imaginary = 0.0
decomposition_error = 0.0
for _ in range(300):
    A = generator.normal(size=(8, 8))  # a random real 8 x 8 matrix
    S = A + A.T  # its symmetric part, doubled
    found = np.linalg.eigvals(S)  # the general program: complex results allowed
    largest_imaginary = max(largest_imaginary, float(np.max(np.abs(found.imag))))
    symmetric_spectra.append(found.real)
    general_spectra.append(np.linalg.eigvals(A))
```

For 300 random $8 \times 8$ matrices $A$: the symmetric matrix $S = A + A^T$, its eigenvalues found by the general program `eigvals`, which would report complex values if there were any, and the largest imaginary part found so far; the real parts are kept for the picture, and so are the eigenvalues of $A$ itself.

```python
    w, O = np.linalg.eigh(S)  # eigenvalues w and eigenvectors (columns of O)
    decomposition_error = max(
        decomposition_error,
        float(np.max(np.abs(O.T @ O - np.eye(8)))),  # O^T O = I
        float(np.max(np.abs(O @ np.diag(w) @ O.T - S))))  # O Lambda O^T = S
```

`eigh` gives the eigenvalues `w` and the matrix `O` of eigenvectors; the largest deviation from $O^TO = I$ and from $O\Lambda O^T = S$ (with $\Lambda$ = `np.diag(w)`) is kept: the spectral theorem of Section 1.36.

```python
general_all = np.concatenate(general_spectra)
complex_share = float(np.mean(np.abs(general_all.imag) > 1e-9))
say(f"symmetric: largest imaginary part {largest_imaginary:.1e}; "
    f"non-symmetric: share of complex eigenvalues {complex_share:.3f}")
```

`np.concatenate` joins the 300 lists into one of 2400 eigenvalues; `complex_share` is the fraction with an imaginary part larger than $10^{-9}$. Output: largest imaginary part 0.0e+00; share of complex eigenvalues 0.677.

```python
check(largest_imaginary < 1e-9, "300 random symmetric matrices: every eigenvalue "
      "is real")
check(decomposition_error < 1e-12,
      "S = O Lambda O^T with O^T O = I for all 300 symmetric matrices")
check(complex_share > 0.3, "the non-symmetric matrices have many complex "
      "eigenvalues")
report("share of complex eigenvalues of 300 random 8 x 8 matrices",
       f"{complex_share:.3f}")
```

Three PASS lines and the RESULT line 0.677 (COMPUTED).

**In [9], all 2400 eigenvalues of each kind.**

```python
symmetric_all = np.concatenate(symmetric_spectra)
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.4), sharey=True)
left.plot(symmetric_all, np.zeros_like(symmetric_all), "|", color="tab:blue",
          ms=14, alpha=0.3)
left.set_title("symmetric $S = A + A^T$: all on the real axis")
right.plot(general_all.real, general_all.imag, ".", color="tab:red", ms=3,
           alpha=0.5)
right.set_title("non-symmetric $A$: conjugate pairs")
```

On the left the 2400 real eigenvalues of the symmetric matrices as short vertical strokes (`"|"`) on the real axis (imaginary part 0, `np.zeros_like`); on the right the 2400 eigenvalues of the non-symmetric matrices as small red dots in the complex plane.

```python
for ax in (left, right):
    ax.axhline(0.0, color="0.5", lw=0.8)
    ax.set_xlabel("real part")
left.set_ylabel("imaginary part")
fig.tight_layout()
save_figure(fig, "random_spectra",
            "The eigenvalues of 300 random real $8 \\times 8$ matrices in the "
            ...)
```

What Figure 01g.5 shows: on the left everything lies on the real axis; on the right a cloud of dots that is mirror-symmetric in the real axis, with a band of real eigenvalues on it.

**In [10], the signature of eta and Sylvester's law.**

```python
algebra = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
names = algebra["coordinates"]  # ["x1", ..., "x8"]
eta = algebra["eta"]  # the diagonal of the frame metric
eta_matrix = np.diag(np.array(eta, dtype=float))
eta_values = np.linalg.eigvalsh(eta_matrix)  # eigenvalues from the smallest up
signature = (int((eta_values > 0).sum()), int((eta_values < 0).sum()))
say(f"eigenvalues of eta: {eta_values.tolist()}; signature {signature}")
```

$\eta$ from the record, as an $8 \times 8$ matrix; `eigvalsh` returns only the eigenvalues of a symmetric matrix. The signature is the pair of the counts of positive and of negative eigenvalues. Output: eight eigenvalues, four $-1.0$ and four $1.0$, signature (4, 4).

```python
algebra_report = json.loads(repository_file(
    "Revision/algebra/reports/python-algebra.json").read_text(encoding="utf-8"))
verdicts = {c["name"]: c["verdict"] for c in algebra_report["checks"]}
check(signature == (4, 4) and verdicts["coordinate_map"] == "pass",
      "eta has 4 positive and 4 negative eigenvalues: the signature (4,4)",
      record="Revision/algebra/reports/python-algebra.json, check coordinate_map")
```

The verdicts of the record's report, and the check of the signature, which reproduces the record's check `coordinate_map`.

```python
sylvester_counts = set()
smallest_size, largest_size = np.inf, 0.0
transformed_spectra = []
for trial in range(2000):
    P = generator.normal(size=(8, 8))  # a random matrix (invertible: det != 0)
    changed = np.linalg.eigvalsh(P.T @ eta_matrix @ P)
    sylvester_counts.add((int((changed > 0).sum()), int((changed < 0).sum())))
    smallest_size = min(smallest_size, float(np.min(np.abs(changed))))
    largest_size = max(largest_size, float(np.max(np.abs(changed))))
    if trial < 40:
        transformed_spectra.append(changed)
```

For 2000 random matrices $P$ (a random matrix has a determinant that is not 0, except in cases of probability 0): the eigenvalues of $P^T\eta P$, the signature found (collected in a **set**, which keeps each different value once), and the smallest and largest size of an eigenvalue seen (`np.inf` is infinity, a start value larger than any number). The spectra of the first 40 are kept for the picture.

```python
say(f"signatures of P^T eta P found: {sorted(sylvester_counts)}; eigenvalue "
    f"sizes from {smallest_size:.1e} to {largest_size:.1f}")
# Rounding changes an eigenvalue by about 2.2e-16 times the largest size; the
# signs are reliable if the smallest size is far above that.
reliable = smallest_size > 1000 * 2.2e-16 * largest_size
check(sylvester_counts == {(4, 4)} and reliable, "Sylvester: P^T eta P has the "
      "signature (4,4) for all 2000 random P, although its eigenvalues change")
```

Output: signatures found [(4, 4)]; eigenvalue sizes from 1.2e-08 to 37.1. A computed eigenvalue can be off by about machine epsilon ($2.2 \times 10^{-16}$, Section 1.4) times the largest size; the signs can be trusted if the smallest size is more than 1000 times that, here $1.2 \times 10^{-8}$ against $8.2 \times 10^{-12}$. The check: only the signature (4,4) occurred, and the signs are reliable. Two PASS lines.

**In [11], the signature of the author's metric.**

```python
a4 = sp.Symbol("a4", real=True)  # the value of a4(x4) at one time
z = sp.Symbol("z", positive=True)  # z = 6 H x8, between 0 and pi/2
curvature = json.loads(repository_file("Revision/gkd_lovelock/results/curvature.json")
                       .read_text(encoding="utf-8"))


def from_record(text):
    """The record's Mathematica text as a sympy expression."""
    text = text.replace("a4[x4]", "a4").replace("Sin[6*H*x8]", "sin(z)")
    text = text.replace("Cot[6*H*x8]", "cot(z)").replace("^", "**")
    return sp.sympify(text, locals={"a4": a4, "z": z, "E": sp.E})
```

The symbols, the record file and the translation function, exactly as in Notebook 01a, In [17] (Section 1.25).

```python
g_record = [from_record(text) for text in curvature["metricDiagonal"]]
metric_numbers = sp.lambdify((a4, z), g_record, "numpy")  # a4, z -> 8 numbers
signs_ok, product_error = True, 0.0
for a4_value in np.linspace(-3.0, 3.0, 61):
    for z_value in np.linspace(0.05, np.pi / 2 - 0.05, 50):
        g_values = np.linalg.eigvalsh(np.diag(np.array(
            metric_numbers(a4_value, z_value), dtype=float)))
        signs_ok &= (int((g_values > 0).sum()), int((g_values < 0).sum())) == (4, 4)
        product_error = max(product_error,
                            abs(np.prod(g_values) - np.cos(z_value) ** 2))
```

The record's metric as a numpy function; then, at 61 values of $a_4$ from $-3$ to 3 and 50 values of $z$ inside $(0, \pi/2)$, the eight eigenvalues of the $8 \times 8$ metric (computed by numpy, although for a diagonal matrix they are its entries), their signs and the distance of their product (`np.prod`) from $\cos^2 z$.

```python
check(signs_ok, "the author's metric has the signature (4,4) at all 3050 grid "
      "points (a4, z)")
lovelock_report = json.loads(repository_file(
    "Revision/gkd_lovelock/results/python-lovelock-report.json")
    .read_text(encoding="utf-8"))
root_verdict = {c["name"]: c["verdict"]
                for c in lovelock_report["checks"]}["sqrt_abs_det_g"]
check(product_error < 1e-12 and root_verdict == "PASS",
      "the product of the eight eigenvalues is det g = cos(z)^2 at every grid point",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, check "
             "sqrt_abs_det_g")
```

Two checks: the signature at all 3050 points, and the product of the eigenvalues equal to $\det g = \cos^2 z$ to $10^{-12}$, together with the record's verdict PASS of the check `sqrt_abs_det_g`. Two PASS lines.

**In [12], the picture of the signatures.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.5, 4.6))
for column, spectrum in enumerate(transformed_spectra):
    colors_column = ["tab:red" if value > 0 else "tab:blue" for value in spectrum]
    left.scatter(np.full(8, column + 1), spectrum, c=colors_column, s=12)
left.axhline(0.0, color="black", lw=0.8)
left.set_yscale("symlog", linthresh=0.001)  # linear between -0.001 and 0.001
left.set_xlabel("random matrix $P$ (number)")
left.set_ylabel("eigenvalues of $P^T \\eta P$")
left.set_title("always 4 positive (red) and 4 negative (blue)")
```

On the left, for each of the first 40 matrices $P$, its eight eigenvalues as a column of dots at the horizontal position $1, \dots, 40$ (`np.full(8, column + 1)` is a list of eight equal positions; `scatter` draws dots with one colour each, red for positive and blue for negative). The vertical axis is **symmetric logarithmic** (`"symlog"`): linear between $-0.001$ and 0.001 and logarithmic outside, so that large and small values of both signs fit.

```python
a4_line = np.linspace(-3.0, 3.0, 301)
curves = np.array([metric_numbers(value, 0.9) for value in a4_line], dtype=float)
styles = [("tab:red", "space $x_1, x_2, x_3$", 0), ("tab:gray", "time $x_4$", 3),
          ("tab:blue", "extra times $x_5, x_6, x_7$", 4),
          ("tab:green", "hidden $x_8$", 7)]
for color, label, index in styles:
    right.plot(a4_line, curves[:, index], color=color, lw=2, label=label)
```

On the right the eight diagonal entries of the metric (its eigenvalues) at $z = 0.9$ for 301 values of $a_4$, as a table with one column per entry; one curve is drawn for each kind of direction (Python's column 0 for space, 3 for the time, 4 for the extra times, 7 for the hidden direction).

```python
right.axhline(0.0, color="black", lw=0.8)
right.set_yscale("symlog", linthresh=0.1)
right.set_xlabel("$a_4$")
right.set_ylabel("eigenvalues of $g$ at $z = 0.9$")
right.set_title("the signs never change: signature (4,4)")
right.legend(fontsize=8, loc="upper left")
fig.tight_layout()
```

A symmetric logarithmic axis linear between $-0.1$ and 0.1, labels and legend.

```python
# how many of the 320 drawn eigenvalues are smaller than 0.001 in size
tiny = sum(int((np.abs(spectrum) < 0.001).sum()) for spectrum in transformed_spectra)
tiny_text = "the one eigenvalue" if tiny == 1 else f"the {tiny} eigenvalues"
tiny_verb = "sits" if tiny == 1 else "sit"  # singular or plural
save_figure(fig, "signature",
            "Left: the eight eigenvalues of $P^T \\eta P$ for 40 random matrices "
            ...)
```

The caption is written from the data: it counts how many of the $40 \cdot 8 = 320$ drawn eigenvalues are smaller than 0.001 in size (they appear on the zero line of the left panel) and chooses the singular or the plural wording; the caption's later lines insert `tiny_text` and `tiny_verb`. What Figure 01g.6 shows: on the left every column has four red and four blue dots although the values change from column to column; on the right the blue extra-time curve (the three equal extra-time eigenvalues) rises towards 0 as $a_4$ grows, the deflation, without ever crossing it, while the red space curve grows and the grey and green curves stay constant.

**In [13], the eigenvalues of the gamma matrices.**

```python
gamma = [np.array(matrix, dtype=int) for matrix in algebra["gamma"]]  # gamma^a
polynomials_ok, traces_ok, numeric_ok = True, True, True
for name, eta_aa, g_a in zip(names, eta, gamma):
    poly = sp.Matrix(g_a.tolist()).charpoly(lam).as_expr()  # det(lambda I - g_a)
    polynomials_ok &= sp.expand(poly - (lam ** 2 - eta_aa) ** 8) == 0
    traces_ok &= int(np.trace(g_a)) == 0
    found = np.linalg.eigvals(g_a.astype(float))
```

For each gamma matrix: its exact characteristic polynomial (`charpoly(lam)` gives $\det(\lambda I - \gamma^a)$ as a polynomial object, `.as_expr()` as an ordinary sympy expression), compared with $(\lambda^2 - \eta_{aa})^8$; its trace, which must be 0; and its eigenvalues from numpy.

```python
    if eta_aa == 1:  # space-like: +1 and -1, eight times each
        numeric_ok &= bool(np.allclose(np.sort(found.real), [-1] * 8 + [1] * 8)
                           and np.allclose(found.imag, 0))
    else:  # time-like: +i and -i, eight times each
        numeric_ok &= bool(np.allclose(found.real, 0)
                           and np.allclose(np.sort(found.imag), [-1] * 8 + [1] * 8))
    say(f"gamma^({name}): eta {eta_aa:+d}, trace {int(np.trace(g_a))}, "
        f"characteristic polynomial {sp.factor(poly)}")
```

For a space-like direction the sorted real parts must be eight $-1$ followed by eight $+1$ (`[-1] * 8 + [1] * 8`) and the imaginary parts 0; for a time-like direction the real parts 0 and the sorted imaginary parts eight $-1$ and eight $+1$. One line per matrix with its factored polynomial: `(lambda - 1)**8*(lambda + 1)**8` for x1, x2, x3, x8 and `(lambda**2 + 1)**8` for x4 to x7.

```python
check(traces_ok and polynomials_ok,
      "every gamma^a has trace 0 and the characteristic polynomial "
      "(lambda^2 - eta_aa)^8", record="Revision/algebra/reports/python-algebra.json, "
      "check clifford_relation (the relations with equal indices)")
check(numeric_ok and verdicts["symmetry_pattern"] == "pass",
      "numpy: +1 and -1 (x1, x2, x3, x8: symmetric matrices) or +i and -i "
      "(x4 ... x7: antisymmetric matrices), 8 times each",
      record="Revision/algebra/reports/python-algebra.json, check symmetry_pattern")
```

Two PASS lines, each with the record check it rests on: the eigenvalues follow from the relations with equal indices of `clifford_relation`, and the symmetric (real eigenvalues) or antisymmetric (imaginary eigenvalues) pattern is the record's `symmetry_pattern`.

**In [14], the gamma matrix of a vector.**

```python
def gamma_of(vector):
    """gamma(v) = v_a gamma^a with v_a = eta_ab v^b (whole numbers)."""
    lowered = [eta[a] * int(vector[a]) for a in range(8)]
    return sum(lowered[a] * gamma[a] for a in range(8))


def squared_length(vector):
    """Q(v) = eta_ab v^a v^b."""
    return sum(eta[a] * int(vector[a]) ** 2 for a in range(8))
```

`gamma_of` lowers the index of the vector and forms $v_a\gamma^a$, a $16 \times 16$ matrix of whole numbers; `squared_length` is $Q(v)$, written out for the diagonal $\eta$.

```python
unit = np.eye(8, dtype=int)
examples = [("e(x1)", unit[0]), ("e(x5)", unit[4]), ("e(x1) + e(x5)", unit[0] + unit[4]),
            ("(1, 2, ..., 8)", np.arange(1, 9))]
example_spectra = {}
squares_ok, nilpotent_ok = True, True
```

The four example vectors of Section 1.27 with their names; a dictionary for their spectra.

```python
for label, vector in examples:
    matrix = gamma_of(vector)
    q = squared_length(vector)
    squares_ok &= bool((matrix @ matrix == q * np.eye(16, dtype=int)).all())
    if q == 0:  # light-like: exact answer from sympy
        poly = sp.Matrix(matrix.tolist()).charpoly(lam).as_expr()
        nilpotent_ok &= poly == lam ** 16 and bool(np.count_nonzero(matrix) > 0)
        example_spectra[label] = np.zeros(16, dtype=complex)
```

For each example: $\gamma(v)$, $Q(v)$, and the exact check $\gamma(v)^2 = Q(v)I$. For the light-like vector the characteristic polynomial is computed exactly; it must be $\lambda^{16}$, and the matrix must have nonzero entries: nilpotent, not zero. Its spectrum, sixteen zeros, is stored for the picture. (numpy is not reliable for a nilpotent matrix, whose eigenvectors do not fill the space; the exact computation is.)

```python
    else:
        example_spectra[label] = np.linalg.eigvals(matrix.astype(float))
        target = np.sqrt(complex(q))  # sqrt(Q), imaginary for Q < 0
        # count the eigenvalues within 1e-9 of +sqrt(Q) and of -sqrt(Q)
        near_plus = int((np.abs(example_spectra[label] - target) < 1e-9).sum())
        near_minus = int((np.abs(example_spectra[label] + target) < 1e-9).sum())
        squares_ok &= near_plus == 8 and near_minus == 8
    say(f"v = {label}: Q(v) = {q}, gamma(v)^2 = Q(v) I")
```

Otherwise numpy's eigenvalues are compared with $\pm\sqrt{Q}$ (`np.sqrt(complex(q))` is imaginary for a negative $Q$): exactly eight must lie within $10^{-9}$ of each. One line per example: Q(v) = 1, -1, 0 and -48.

```python
for _ in range(100):  # random vectors with whole-number components -5 ... 5
    vector = generator.integers(-5, 6, size=8)
    matrix = gamma_of(vector)
    squares_ok &= bool((matrix @ matrix
                        == squared_length(vector) * np.eye(16, dtype=int)).all())
check(squares_ok, "gamma(v)^2 = Q(v) I exactly and the eigenvalues are +-sqrt(Q(v)) "
      "(4 examples and 100 random vectors)")
check(nilpotent_ok, "a light-like v gives a nilpotent gamma(v): not zero, square "
      "zero, characteristic polynomial lambda^16")
```

The square rule for 100 random whole-number vectors, exactly; then the two checks. Two PASS lines.

**In [15], the eigenvalues as pictures.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.8))
for name, eta_aa, g_a in zip(names, eta, gamma):
    found = np.linalg.eigvals(g_a.astype(float))
    color = "tab:red" if eta_aa == 1 else "tab:blue"
    left.plot(found.real, found.imag, "o", color=color, ms=10, alpha=0.3)
```

On the left the 16 eigenvalues of each gamma matrix in the complex plane, red for space-like and blue for time-like directions, see-through (`alpha=0.3`), so that the many dots on top of each other show as a darker colour.

```python
left.text(1.0, 0.18, "$+1$: 8 times\n($x_1, x_2, x_3, x_8$)", ha="center",
          fontsize=8)
left.text(-1.0, 0.18, "$-1$: 8 times", ha="center", fontsize=8)
left.text(0.08, 1.0, "$+i$: 8 times ($x_4 \\dots x_7$)", fontsize=8)
left.text(0.08, -1.05, "$-i$: 8 times", fontsize=8)
left.set_xlim(-1.6, 1.9)
left.set_ylim(-1.5, 1.5)
left.set_title("the eight gamma matrices")
```

Four labels at the four points $\pm 1$, $\pm i$, the ranges and the title.

```python
markers = {"e(x1)": ("s", "tab:red"), "e(x5)": ("D", "tab:blue"),
           "e(x1) + e(x5)": ("*", "black"), "(1, 2, ..., 8)": ("o", "tab:purple")}
for label, spectrum in example_spectra.items():
    shape, color = markers[label]
    right.plot(spectrum.real, spectrum.imag, shape, color=color, ms=10,
               label=f"$v$ = {label}, $Q = {squared_length(dict(examples)[label])}$")
right.set_xlim(-3.0, 3.0)
right.set_ylim(-8.0, 8.0)
right.set_title("$\\gamma(v) = v_a \\gamma^a$: eigenvalues $\\pm\\sqrt{Q(v)}$")
right.legend(fontsize=8, loc="lower right")
```

On the right the spectra of the four matrices $\gamma(v)$, each with its own marker shape (square, diamond, star, circle); `dict(examples)[label]` looks up the vector of a name, to print its $Q$ in the legend.

```python
for ax in (left, right):
    ax.axhline(0.0, color="0.5", lw=0.8)
    ax.axvline(0.0, color="0.5", lw=0.8)
    ax.set_xlabel("real part")
    ax.set_ylabel("imaginary part")
fig.tight_layout()
save_figure(fig, "gamma_eigenvalues",
            "Eigenvalues in the complex plane (horizontal axis real part, vertical "
            ...)
```

Axes and labels on both panels. What Figure 01g.7 shows: on the left the dots sit only at $\pm 1$ and $\pm i$; on the right $\pm 1$, $\pm i$, a single point at 0 for the light-like vector, and $\pm i\sqrt{48} \approx \pm 6.93i$.

**In [16], the Hermitian matrix B of the record.**

```python
B = sp.Matrix(algebra["B"]["re"]) + sp.I * sp.Matrix(algebra["B"]["im"])
C = sp.Matrix(algebra["C"])
check(B == -sp.I * C * sp.Matrix(algebra["gamma"][3]),
      "the record's B equals -i C gamma^(x4) computed from its C and gamma^(x4)")
```

The record stores $B$ as its real part `re` and its imaginary part `im`; the exact sympy matrix is built from them. $C$ is read as well, and the check confirms $B = -iC\gamma^{(x_4)}$ exactly ($\gamma^{(x_4)}$ is entry 3 of the list in Python's numbering).

```python
poly_B = sp.factor(B.charpoly(lam).as_expr())
real_part_zero = sp.Matrix(algebra["B"]["re"]).is_zero_matrix  # True or False
say(f"B: real part zero {real_part_zero}, trace {B.trace()}, characteristic "
    f"polynomial {poly_B}")
```

The factored characteristic polynomial of $B$, and whether its real part is the zero matrix. Output: `B: real part zero True, trace 0, characteristic polynomial (lambda - 1)**8*(lambda + 1)**8`.

```python
check(B.H == B and B * B == sp.eye(16) and B.trace() == 0
      and sp.expand(poly_B - (lam - 1) ** 8 * (lam + 1) ** 8) == 0,
      "B is Hermitian, B^2 = I, tr B = 0, characteristic polynomial "
      "(lambda - 1)^8 (lambda + 1)^8: the signature (8,8)",
      record="Revision/algebra/reports/python-algebra.json, check "
             "B_hermitian_involution_signature")
```

`B.H` is sympy's conjugate transpose $B^\dagger$. The four properties of Section 1.37, exactly; this reproduces the record's check `B_hermitian_involution_signature`.

```python
B_numbers = np.array(B.tolist(), dtype=complex)
values_B, vectors_B = np.linalg.eigh(B_numbers)
unitary_error = float(np.max(np.abs(vectors_B.conj().T @ vectors_B - np.eye(16))))
say(f"numpy eigh: eigenvalues {values_B.round(12).tolist()}")
```

$B$ as a complex numpy array; `eigh` works for Hermitian matrices too. `vectors_B.conj().T` is the conjugate transpose of the eigenvector matrix; its product with the eigenvector matrix must be $I$ (eigenvectors perpendicular in the sense $u^\dagger w = 0$, of length 1). Output: eight $-1.0$ and eight $1.0$.

```python
theory = json.loads(repository_file(
    "Revision/theory/reports/python-field-theory.json").read_text(encoding="utf-8"))
theory_verdict = {c["name"]: c["verdict"] for c in theory["checks"]}["B_properties"]
krein_entry = theory["formulas"]["quantisation"]["krein"]  # a sentence of the record
say(f"the record's quantisation entry: {krein_entry}")
```

A second record, the theory report: the verdict of its check `B_properties` and its entry `formulas`, `quantisation`, `krein`, a sentence that is printed: B Hermitian, B^2 = 1, signature (8,8): indefinite (Krein) state space.

```python
check(np.allclose(values_B, [-1.0] * 8 + [1.0] * 8, rtol=0, atol=1e-12)
      and unitary_error < 1e-12 and theory_verdict == "pass",
      "numpy: eight eigenvalues -1 and eight +1, perpendicular eigenvectors",
      record="Revision/theory/reports/python-field-theory.json, check B_properties")
```

The numerical eigenvalues, the perpendicular eigenvectors and the record's verdict; this reproduces the check `B_properties`. The cell prints three PASS lines.

**In [17], the picture of B.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.6),
                                  gridspec_kw={"width_ratios": [1.1, 1]})
image = left.imshow(B_numbers.imag, cmap="RdBu_r", vmin=-1, vmax=1)
left.grid(False)
ticks = range(0, 16, 3)
left.set_xticks(ticks, [str(t + 1) for t in ticks])
left.set_yticks(ticks, [str(t + 1) for t in ticks])
left.set_xlabel("column")
left.set_ylabel("row")
left.set_title("imaginary part of $B$ (the real part is 0)")
fig.colorbar(image, ax=left, shrink=0.8, ticks=[-1, 0, 1])
```

The imaginary part of $B$ as a heat map, with labels at every third row and column (`range(0, 16, 3)` is 0, 3, 6, 9, 12, 15, labelled 1, 4, 7, 10, 13, 16), and a colour bar.

```python
right.bar(np.arange(1, 17), values_B,
          color=["tab:blue" if value < 0 else "tab:red" for value in values_B])
right.axhline(0.0, color="black", lw=0.8)
right.set_xticks(range(1, 17, 3))
right.set_ylim(-1.4, 1.4)
right.set_xlabel("eigenvalue number (from the smallest up)")
right.set_ylabel("eigenvalue of $B$")
right.set_title("eight $-1$ and eight $+1$: signature (8,8)")
fig.tight_layout()
save_figure(fig, "hermitian_b",
            "Left: heat map of the imaginary part of the Hermitian matrix "
            ...)
```

On the right the 16 eigenvalues as bars, blue for negative and red for positive. What Figure 01g.8 shows: on the left a pattern of red and blue squares whose mirror image in the diagonal has the opposite colours (antisymmetric imaginary part); on the right eight bars down and eight up.

**In [18], power iteration.**

```python
def power_iteration(matrix, start, steps):
    """Multiply by matrix and rescale to length 1, steps times; return the
    distances to the eigenvector of the largest eigenvalue after each step."""
    values_m, vectors_m = np.linalg.eigh(matrix)
    top = vectors_m[:, -1]  # the eigenvector of the largest eigenvalue
    x = np.array(start, dtype=float)
    distances = []
```

The function first finds the true answer with `eigh` (the last column belongs to the largest eigenvalue), to measure the error of the iteration; `x` is the starting vector.

```python
    for _ in range(steps):
        x = matrix @ x
        x = x / np.sqrt(x @ x)  # rescale to length 1
        aligned = top if x @ top > 0 else -top  # the sign of an eigenvector is free
        distances.append(float(np.sqrt(((x - aligned) ** 2).sum())))
    return np.array(distances), abs(values_m[-2] / values_m[-1])
```

Each step multiplies by the matrix and divides by the length (`x @ x` is the squared length). The true eigenvector is taken with the sign that points the same way as `x`, and the distance between the two is recorded. The function returns the distances and the factor $|\lambda_2/\lambda_1|$ of Section 1.37 (the second-largest eigenvalue divided by the largest).

```python
runs = {"M (2 x 2)": power_iteration(M_numbers, [1, 0], 40),
        "T3 (3 x 3)": power_iteration(np.array(T3.tolist(), dtype=float),
                                      [1, 0, 0], 40)}
factors_ok = True
for label, (distances, ratio) in runs.items():
    measured = distances[11:21] / distances[10:20]  # steps 11 to 20
    say(f"{label}: |lambda2/lambda1| = {ratio:.6f}, measured factors "
        f"{measured.min():.6f} to {measured.max():.6f}")
    factors_ok &= bool(np.all(np.abs(measured - ratio) < 1e-3))
check(factors_ok, "power iteration: each step shrinks the error by |lambda2/lambda1|"
      " (1/3 for M, 2 - sqrt 2 for T3)")
```

40 steps for $M$ from $(1, 0)$ and for $T_3$ from $(1, 0, 0)$. The measured factors are the ratios of consecutive distances for the steps 11 to 20 (`distances[11:21] / distances[10:20]` divides each distance by the one before); they must agree with $|\lambda_2/\lambda_1|$ to $10^{-3}$. Output: M (2 x 2): |lambda2/lambda1| = 0.333333, measured factors 0.333333 to 0.333333, and T3 (3 x 3): 0.585786, measured 0.585786 to 0.585789, and the PASS line.

```python
fig, ax = plt.subplots(figsize=(7.5, 4.4))
steps_axis = np.arange(1, 41)
for (label, (distances, ratio)), color in zip(runs.items(), ("tab:red", "tab:blue")):
    # a distance 0 (exact agreement) is drawn at 1e-17, the bottom of the axis
    ax.semilogy(steps_axis, np.maximum(distances, 1e-17), "o", color=color, ms=4,
                label=label)
    ax.semilogy(steps_axis, distances[0] * ratio ** (steps_axis - 1), "-",
                color=color, lw=1, label=f"factor {ratio:.3f} per step")
```

For both runs: the 40 distances as dots on a logarithmic axis (a distance that is exactly 0 is drawn at $10^{-17}$), and the straight line $|\lambda_2/\lambda_1|^{k-1}$ times the first distance.

```python
ax.set_ylim(1e-17, 2.0)
ax.set_xlabel("step $k$")
ax.set_ylabel("distance to the eigenvector")
ax.set_title("Power iteration")
ax.legend(fontsize=8);
save_figure(fig, "power_iteration",
            "Power iteration: the distance between the rescaled vector "
            ...)
```

What Figure 01g.9 shows: the red dots ($M$) fall fast, by the factor $1/3$ per step, along their straight line until they reach the rounding level of floating-point numbers, about $10^{-16}$; the blue dots ($T_3$) fall more slowly, by 0.586 per step, along theirs.

**In [19], the last check.**

```python
figure_names = [f"01g_{k}_{name}.png" for k, name in enumerate(
    ["circle_to_ellipse", "characteristic_polynomial", "chain_matrix",
     "rotation_and_boost", "random_spectra", "signature", "gamma_eigenvalues",
     "hermitian_b", "power_iteration"], start=1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all 9 figure files of this notebook exist")
all_checks_passed()
```

The nine file names are built from their numbers and names (`enumerate(..., start=1)` numbers the list from 1). The last line is ALL 30 CHECKS PASSED (notebook 01g). The 30 checks are: 4 in In [2], 1 in In [3], 2 in In [4], 2 in In [5], 5 in In [6], 3 in In [8], 2 in In [10], 2 in In [11], 2 in In [13], 2 in In [14], 3 in In [16], 1 in In [18] and 1 in In [19].
