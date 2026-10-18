#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 14b, "The free Kohn-Sham spectrum at zero 3-momentum: exact
formulas against numerical shooting" (textbook "Universes in Pairs", chapter 14).

The notebook Revision/textbook/notebooks/14b_free_spectra.ipynb is BUILT from this file
by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/14b_free_spectra.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/14b_free_spectra.py

The notebook works in the corrected metric of 2026-10-16 (version 2): the block
equation chi' = f N chi with the hidden scale f = exp(-a4) b4^(1/2), the fold
conditions of the doubled cell and the regular tip.  The shooting function is that of
the Revision Rust solver (Revision/kohn_sham/solver/src/shoot.rs: classical RK4 with
the coefficients multiplied by f, the Pruefer angle of atan2(b, a) unwrapped step by
step), written with numpy; its root finder is plain bisection (72 halvings of
[-20, 20]), where the solver's find_level uses a safeguarded Newton-bisection down to
the tolerance 1e-13.  The notebook's levels reproduce the solver's record
Revision/kohn_sham/results/spectrum/free-k0-analytic.csv (72 levels, four cases) to
better than 1e-11 (the measured difference is printed).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "14b",
    "name": "14b_free_spectra",
    "title": "The free Kohn-Sham spectrum at zero 3-momentum: exact formulas against "
             "numerical shooting",
    "purpose": (
        "For the free field (no interaction, constant mass M, zero 3-momentum) in the "
        "corrected metric of 2026-10-16 it writes the 2 x 2 block equation of "
        "dirac16complex in real form with the hidden scale f, derives its boundary "
        "conditions (the two fold conditions at the fold y = 0, where the two halves "
        "of a cell meet, both filled by the ASSUMED convention of the record, and the "
        "regular tip at y = -L) and their consequences, solves the equation exactly "
        "(the fold zero mode exp(f M y), the even levels plus or minus the square root "
        "of M^2 + (n pi/(f L))^2, the odd levels from tan(p f L) = -p/M), solves it "
        "again numerically with a fourth-order Runge-Kutta shooting method whose "
        "Pruefer angle gives every level an integer label, and compares the two: it "
        "reproduces the free spectra of four cases, the zero mode and the measured "
        "fourth-order convergence of the Revision Rust solver and draws six teaching "
        "figures."
    ),
    "records": [
        ["Revision/kohn_sham/ks-theory.json",
         "the exact Kohn-Sham theory: block equation, real form, boundary conditions "
         "and the exact k = 0 spectra (reproduced)"],
        ["Revision/kohn_sham/reports/ks-theory-python.json",
         "the sympy checks of the boundary conditions and of the exact spectra that "
         "this notebook reproduces"],
        ["Revision/kohn_sham/reports/ks-theory-wolfram.json",
         "the same checks in WolframScript (their verdicts are read)"],
        ["Revision/kohn_sham/results/spectrum/free-k0-analytic.csv",
         "the Rust solver's numerical and exact k = 0 levels of four cases "
         "(reproduced)"],
        ["Revision/kohn_sham/reports/ks-rust-solver.json",
         "the Rust solver's checks free_k0_analytic_spectra and free_zero_mode_exact "
         "(reproduced)"],
        ["Revision/kohn_sham/reports/ks-rust-determinism.json",
         "the Rust solver's check refined_free_spectra_convergence_order (reproduced)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 60,
    "timeout_seconds": 600,
    "files_written": [
        "Revision/textbook/figures/14b.captions.json",
        "Revision/textbook/figures/14b_1_odd_condition.png",
        "Revision/textbook/figures/14b_2_shooting_function.png",
        "Revision/textbook/figures/14b_3_spectrum_ladder.png",
        "Revision/textbook/figures/14b_4_rk4_convergence.png",
        "Revision/textbook/figures/14b_5_orbitals.png",
        "Revision/textbook/figures/14b_6_pruefer_angle.png",
    ],
    "final_lines": [
        "PASS all six figure files of this notebook exist",
        "ALL 20 CHECKS PASSED (notebook 14b)",
    ],
    "troubleshooting": [
        ["the cells of sections 9 and 10 run for 10 to 30 seconds each",
         "they integrate the equation for hundreds of energies at once, 72 times "
         "over; wait until the PASS lines appear."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    In the Kohn-Sham model of dirac16complex in the deflating primordial field (the
    corrected metric of 2026-10-16) every orbital is described by a pair of functions
    $\chi = (\chi_1, \chi_2)$ of the hidden coordinate $y$ between the tip cutoff
    $y = -L$ and the fold $y = 0$, where the two halves of a cell meet. This notebook
    studies the simplest case completely: no interaction ($v = 0$, constant mass
    $M$) and zero 3-momentum ($k = 0$). It

    - writes the $2\times2$ block equation $\chi' = fN\chi$ in real form, with the
      hidden scale $f = e^{-a_4}b_4^{1/2}$ of the slice, and checks it;
    - derives and checks the boundary conditions: the two fold conditions at
      $y = 0$ (both are solved and filled: an ASSUMED convention of the Revision
      record), the regular tip at $y = -L$ (a CHOSEN cutoff condition), and what they
      imply (no current through the ends, real levels);
    - solves the equation exactly: the fold zero mode $\varepsilon = 0$ with the
      orbital $(e^{fMy}, 0)$, the even levels $\pm\sqrt{M^2 + (n\pi/(fL))^2}$ and the
      odd levels from $\tan(pfL) = -p/M$ (figure 1);
    - solves it again numerically with the shooting function of the Revision Rust
      solver: fourth-order Runge-Kutta (RK4) shooting with a Pruefer angle that
      gives every level an integer label, the levels found by bisection
      (figures 2 and 6);
    - compares the two for the 72 levels of the record (four cases, among them one
      at the slice $a_{4,0} = 1.5$ of the history, where $f = e^{-1/2}$) and
      reproduces the Rust solver's numbers to about $10^{-14}$ (figure 3);
    - measures the fourth-order convergence of the method (figure 4) and draws the
      orbitals against the exact ones (figure 5).

    It prints a PASS line for every check (20 in all) and saves six figures.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Hidden coordinate $y$**: $y = \ln|\sin z|/(6H)$ with $z = 6Hx_0$; the fold
      is at $y = 0$, the tip cutoff at $y = -L$ (here $L = 3$, $2$).
    - **Cell, halves, fold**: one period $0 < z < \pi$ of the hidden direction; its
      two halves $z < \pi/2$ and $z > \pi/2$ meet at the fold $\cos z = 0$
      ($z = \pi/2$, $y = 0$). The doubled system is the whole cell.
    - **Hidden scale $f$**: $f = e^{-a_4}b_4^{1/2}$ at the slice; the proper
      length of the cut-off half is $fL$. On the history $f = e^{-a_{4,0}/3}$.
    - **Block equation**: in each of eight $2\times2$ blocks the Kohn-Sham
      equation is $h_j\chi = \varepsilon\chi$ with
      $h_j = j[-(i/f)\sigma_1\,d/dy + M\sigma_2 + \kappa k\,\sigma_3] + v$, where
      $j = \pm1$ is the block type, $M$ the (effective) mass, $\kappa = e^{-a_4}$ the
      momentum weight and $v$ the vector potential.
    - **Level, orbital**: an energy $\varepsilon$ for which a solution exists that
      satisfies both boundary conditions; that solution is the orbital.
    - **Real form**: writing $\chi = (a, ib)$ with real $a$, $b$ makes all
      coefficients real.
    - **Boundary condition**: a condition on the solution at an end of the interval.
    - **Fold conditions**: $\chi_2(0) = 0$ ($b(0) = 0$, called even, $\theta = 0$)
      and $\chi_1(0) = 0$ ($a(0) = 0$, called odd, $\theta = \pi$); the record
      solves and fills both (ASSUMED).
    - **Regular tip**: the chosen condition $b(-L) = 0$ at the cutoff.
    - **Current**: $\chi^\dagger\sigma_1\chi$, the flow of the U(1) charge along
      $y$; a good boundary condition makes it vanish at the ends.
    - **Self-adjoint**: the Hamiltonian satisfies $\int\varphi^\dagger h\chi\,dy =
      \int(h\varphi)^\dagger\chi\,dy$; then the levels are real.
    - **Shooting**: start the solution at one end with the condition there,
      integrate to the other end, and adjust $\varepsilon$ until the condition there
      holds too.
    - **RK4**: the classical fourth-order Runge-Kutta method for $u' = F(y, u)$ with
      step $h$: four slopes per step, error per unit length proportional to $h^4$.
    - **Pruefer angle** $\theta = \mathrm{atan2}(b, a)$: the angle of the point
      $(a, b)$ in the plane; counting its half-turns labels the levels.
    - **Bisection**: halve an interval that contains a root, keep the half where the
      function changes sign, repeat.
    - **Simpson's rule**: an integration rule with the weights $1, 4, 2, 4, \dots,
      4, 1$ times (step/3).
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The Revision theory (`Revision/kohn_sham/ks-theory.json`) reduces the Kohn-Sham
    equation exactly to the block equation $h_j\chi = \varepsilon\chi$ above. At the
    slice $a_{4,0}$, $b_{4,0}$ of the deflating history two constants enter: the
    momentum weight $\kappa = e^{-a_{4,0}}$, which multiplies the 3-momentum, and
    the hidden scale $f = e^{-a_{4,0}}b_{4,0}^{1/2}$, which divides the derivative
    along $y$. In this notebook $k = 0$, so $\kappa$ drops out; $f$ stays, and the
    spectrum depends on the slice through the proper length $fL$ of the cut-off half.
    $v = 0$ and $M$ is a constant. The equation is then simple enough to solve by
    hand, and these exact solutions are the first test of every numerical solver of
    the model: the Revision Rust solver checked itself against them (its record
    `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv`). Here we write the
    same numerical method with numpy, so that every step can be read, and we check
    that it gives the same numbers.

    Units: $H = 1$ and energies in units of the mass $m$ (the canonical runs use
    $m = 1$, $L = 3$); the record's four cases are $(m, L, a_{4,0}) = (1, 3, 0)$,
    $(1, 2, 0)$, $(2, 3, 0)$ with $f = 1$ and $(1, 3, 1.5)$ on the history, with
    $f = e^{-1/2}$.

    Status: the exact solutions are PROVED (and verified in the Revision record);
    the numerical levels are COMPUTED (error measured against the exact ones); that
    both fold conditions are filled is ASSUMED (the record's convention); the tip
    condition is a chosen cutoff condition.
    """),
    md(r"""
    ## 5. The block equation in real form

    The eigenvalue equation $h_j\chi = \varepsilon\chi$ is the same as the
    first-order system (Revision record, `blockEquation.ode`)

    $$\chi' = fN\chi,\qquad N = M\sigma_3 - \kappa k\,\sigma_2 + ij(\varepsilon - v)
    \sigma_1 .$$

    Write $\chi = (a, ib)$ with real functions $a$, $b$ and $K = \kappa k$. Then,
    multiplying out the Pauli matrices:

    $$a' = f\,[Ma - (K + j(\varepsilon - v))\,b],\qquad b' = f\,[(j(\varepsilon - v)
    - K)\,a - Mb] .$$

    All coefficients are real, so a real starting point gives a real solution. The
    next cell lets sympy multiply $fN$ with $(a, ib)$ and checks that the result is
    $(a', ib')$ with the two lines above.
    """),
    code(r'''
    import math  # exp, cos, sin of single numbers

    import numpy as np  # floating-point arrays
    import sympy as sp  # exact algebra with symbols

    PY_REPORT = "Revision/kohn_sham/reports/ks-theory-python.json"
    WL_REPORT = "Revision/kohn_sham/reports/ks-theory-wolfram.json"
    RUST_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"


    def record_check(name, reports=(PY_REPORT, WL_REPORT)):
        """True when the check called name is PASS in the first report and, if the
        other reports have a check of that name, PASS there too."""
        verdicts = []
        for report in reports:
            data = json.loads(repository_file(report).read_text(encoding="utf-8"))
            found = [c["verdict"] for c in data["checks"] if c["name"] == name]
            verdicts.append(found[0] if found else "absent")
        return verdicts[0] == "PASS" and all(v in ("PASS", "absent") for v in verdicts)


    s1 = sp.Matrix([[0, 1], [1, 0]])  # the Pauli matrices
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    I2 = sp.eye(2)
    a, b, M, K, e, v = sp.symbols("a b M K epsilon v", real=True)
    fs = sp.symbols("f", positive=True)  # the hidden scale of the slice
    ok_all = True
    for j in (1, -1):
        N = M * s3 - K * s2 + sp.I * j * (e - v) * s1  # the matrix of chi' = f N chi
        derivative = sp.expand(fs * N * sp.Matrix([a, sp.I * b]))  # f N times (a, i b)
        a_prime = fs * (M * a - (K + j * (e - v)) * b)  # the real form
        b_prime = fs * ((j * (e - v) - K) * a - M * b)
        ok = (sp.expand(derivative[0] - a_prime) == 0
              and sp.expand(derivative[1] - sp.I * b_prime) == 0)
        ok_all &= ok
        say(f"j = {j:+d}: d chi/dy = f N chi with chi = (a, i b) gives the real form: "
            f"{ok}")
    theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json")
                        .read_text(encoding="utf-8"))
    say("record: " + theory["blockEquation"]["realForm"])
    check(ok_all, "the real form da/dy = f[M a - (K + j(eps - v)) b], "
          "db/dy = f[(j(eps - v) - K) a - M b]")
    '''),
    md(r"""
    ## 6. The boundary conditions

    **The fold (two halves of a cell).** The fold $\cos z = 0$ ($z = \pi/2$, $y = 0$)
    joins the halves $z < \pi/2$ and $z > \pi/2$ of a cell. The reflection
    $z \to \pi - z$ keeps $|\sin z|$, hence $y$, and flips the sign of $\cot z$; on
    each half $dy = \cot z\,dx_0$ and the signed hidden vielbein is $f\cot z$, so the
    proper step is $f\cot z\,dx_0 = f\,dy$ on both halves; and the spin-connection
    term $\gamma^\mu\Omega_\mu = \frac32(H/f)\gamma^{(x_0)} + (b_4'/b_4 -
    \frac12a_4')\gamma^{(x_4)}$ (Notebook 14a) contains no $y$. So the reduced
    equation is the same on both halves, and a spinor continuous across the fold has
    the same $\chi(y)$ on both. Integrating by parts on one half,
    $\varphi^\dagger h_j\chi - (h_j\varphi)^\dagger\chi = \frac{d}{dy}[-(ij/f)\,
    \varphi^\dagger\sigma_1\chi]$; since $y$ increases toward the fold on BOTH
    halves, the boundary form of the whole cell at the fold is twice the end value,
    $2(-ij/f)\varphi^\dagger\sigma_1\chi(0)$. Self-adjointness needs a condition
    $(1 - Q(\theta))\chi(0) = 0$ with $Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta
    \,\sigma_2$; the Revision record solves and fills two of them together:
    $\theta = 0$, i.e. $\chi_2(0) = 0$ ($b(0) = 0$, called even), and $\theta = \pi$,
    i.e. $\chi_1(0) = 0$ ($a(0) = 0$, called odd). That both are filled is ASSUMED
    (the record's convention; the metric is degenerate at the fold and no junction
    condition is derived).

    **The tip (chosen).** At the cutoff $y = -L$ the family $(1 - Q(\theta))\chi(-L)
    = 0$ is allowed; $Q^\dagger = Q$, $Q^2 = 1$ and $Q\sigma_1 + \sigma_1Q = 0$, so
    every member kills the current. The canonical choice is $\theta = 0$: $b(-L) = 0$.

    **Consequences.** If both ends kill the current, the boundary terms vanish and
    $h_j$ is self-adjoint: the levels are real and orbitals of different levels are
    orthogonal. $\chi^\dagger\sigma_1\chi$ is constant in $y$ on every solution
    ($N^\dagger\sigma_1 + \sigma_1N = 0$), while $\chi^\dagger\chi$ is not. And
    $N^2 = (M^2 + \kappa^2k^2 - (\varepsilon - v)^2)\,1$: for constant $M$, $v$ the
    solutions are $e^{\pm f\Lambda y}$ with $\Lambda = \sqrt{M^2 + \kappa^2k^2 -
    (\varepsilon - v)^2}$; since $\kappa$ does not depend on $y$, nothing suppresses
    an orbital toward the tip, and the extended levels depend on the cutoff like
    those of a box of proper length $fL$.

    The next cell checks all of this with sympy, as the Revision record did. For
    the term $\gamma^\mu\Omega_\mu$ it uses the formula of the contribution of each
    direction (Notebook 14a, section 7): the coefficient of $\gamma^{(B)}$ is
    $\frac12\sum_{l \ne B}\partial_B\ln h_l/h_B$ with the scale factors
    $h = (f, e^{a_4}, e^{a_4}, e^{a_4}, 1, fe^{Hy}, fe^{Hy}, fe^{Hy})$.
    """),
    code(r'''
    y = sp.symbols("y", real=True)
    a0, k, H = sp.symbols("a0 k H", real=True)
    Mf = sp.Function("M", real=True)(y)  # a mass that depends on y
    vf = sp.Function("v", real=True)(y)  # a potential that depends on y
    kap = sp.exp(-a0)  # the momentum weight: the same at every y
    zeta, x4 = sp.symbols("zeta x4", real=True)
    a4 = sp.Function("a4", real=True)(x4)
    b4 = sp.Function("b4", positive=True)(x4)
    f_t = sp.exp(-a4) * sp.sqrt(b4)  # the hidden scale as a function of the time
    scale = [f_t] + [sp.exp(a4)] * 3 + [1] + [f_t * sp.exp(H * y)] * 3  # (y, x1..x7)
    coords = [y, None, None, None, x4, None, None, None]  # what the factors depend on
    slash = {}  # B -> coefficient of gamma^(B) in gamma^mu Omega_mu
    for B_ in (0, 4):  # only y and x4 appear in the scale factors
        slash[B_] = sp.simplify(sum(sp.diff(sp.log(scale[l]), coords[B_])
                                    for l in range(8) if l != B_) / (2 * scale[B_]))
    say(f"coefficient of gamma^(x0): {slash[0]}")
    say(f"coefficient of gamma^(x4): {slash[4]}")
    ok_fold = (sp.simplify(sp.sin(sp.pi - zeta) - sp.sin(zeta)) == 0
               and sp.simplify(sp.cot(sp.pi - zeta) + sp.cot(zeta)) == 0
               and sp.simplify(sp.diff(sp.log(sp.sin(zeta) ** 2) / 2, zeta)
                               - sp.cot(zeta)) == 0
               and sp.simplify(slash[0] - sp.Rational(3, 2) * H / f_t) == 0
               and sp.simplify(slash[4] - (sp.diff(b4, x4) / b4 - sp.diff(a4, x4) / 2))
               == 0 and not slash[0].has(y) and not slash[4].has(y))
    check(ok_fold and record_check("bc_fold_same_equation_on_both_halves"),
          "z -> pi - z keeps y, flips cot z; gamma^mu Omega_mu has no y: same chi(y)",
          record=f"{PY_REPORT}, check bc_fold_same_equation_on_both_halves")
    c1f, c2f = sp.Function("chi1")(y), sp.Function("chi2")(y)
    chi = sp.Matrix([c1f, c2f])
    current = sp.expand((chi.H * s1 * chi)[0])  # the current chi^dag sigma1 chi
    th = sp.symbols("theta", real=True)
    Q = sp.cos(th) * s3 + sp.sin(th) * s2  # the family of end conditions
    c_a, c_b = sp.symbols("c_a c_b", positive=True)  # a general end value (c_a, c_b)
    fold_ok = (Q.subs(th, 0) == s3 and Q.subs(th, sp.pi) == -s3  # (1 - Q) chi(0) = 0
               and sp.simplify(current.subs(c2f, 0)) == 0  # theta = 0: chi2(0) = 0
               and sp.simplify(current.subs(c1f, 0)) == 0  # theta = pi: chi1(0) = 0
               and sp.simplify(current.subs({c1f: c_a, c2f: c_b})) != 0)
    check(fold_ok and record_check("bc_fold_conditions"),
          "both fold conditions chi2(0) = 0 and chi1(0) = 0 kill the current",
          record=f"{PY_REPORT}, check bc_fold_conditions")
    phi = sp.Matrix([sp.Function("phi1")(y), sp.Function("phi2")(y)])
    ok_adjoint = True
    for j in (1, -1):
        def h_on(w, j=j):  # h_j applied to the column w
            return j * (-sp.I / fs * s1 * sp.diff(w, y) + Mf * s2 * w
                        + kap * k * s3 * w) + vf * w
        difference = (phi.H * h_on(chi))[0] - (h_on(phi).H * chi)[0]
        boundary = sp.diff(-sp.I * j / fs * (phi.H * s1 * chi)[0], y)
        ok_adjoint &= sp.simplify(sp.expand(difference - boundary)) == 0
    check(ok_adjoint and record_check("bc_self_adjoint_boundary_term"),
          "phi^dag h chi - (h phi)^dag chi = d/dy[-(i j/f) phi^dag sigma1 chi]",
          record=f"{PY_REPORT}, check bc_self_adjoint_boundary_term")
    check(sp.simplify(Q * Q - I2).is_zero_matrix and Q.H == Q
          and sp.simplify(Q * s1 + s1 * Q).is_zero_matrix and record_check("bc_tip_family"),
          "the tip family Q(theta): Q^dag = Q, Q^2 = 1, Q sigma1 = -sigma1 Q",
          record=f"{PY_REPORT}, check bc_tip_family")
    kp = sp.symbols("kappa", positive=True)
    ok_current, ok_square = True, True
    for j in (1, -1):
        Nn = M * s3 - kp * k * s2 + sp.I * j * (e - v) * s1
        ok_current &= sp.simplify(Nn.H * s1 + s1 * Nn).is_zero_matrix
        density_changes = not sp.simplify(Nn.H + Nn).is_zero_matrix
        ok_square &= sp.simplify(Nn * Nn - (M ** 2 + kp ** 2 * k ** 2 - (e - v) ** 2)
                                 * I2).is_zero_matrix
    check(ok_current and density_changes and record_check("bc_current_conserved_along_y"),
          "the current is constant along y on every solution, the density is not",
          record=f"{PY_REPORT}, check bc_current_conserved_along_y")
    check(ok_square and record_check("bc_tip_asymptotics"),
          "N^2 = (M^2 + kappa^2 k^2 - (eps - v)^2) 1: branches exp(+-f Lambda y)",
          record=f"{PY_REPORT}, check bc_tip_asymptotics")
    '''),
    md(r"""
    ## 7. The exact solutions at zero 3-momentum

    Take $k = 0$, $v = 0$ and a constant $M > 0$. The real form becomes
    $a' = f(Ma - j\varepsilon b)$, $b' = f(j\varepsilon a - Mb)$. Line by line:

    1. If $\varepsilon \ne 0$, solve the second equation for $a$:
       $a = (b'/f + Mb)/(j\varepsilon)$.
    2. Differentiate: $a' = (b''/f + Mb')/(j\varepsilon)$.
    3. Put 1 and 2 into the first equation and multiply by $j\varepsilon$ (with
       $j^2 = 1$): $b''/f + Mb' = M b' + fM^2b - f\varepsilon^2 b$, that is
       $b'' = f^2(M^2 - \varepsilon^2)\,b$.
    4. EVEN fold condition, $b(0) = 0$ and $b(-L) = 0$: a solution that vanishes at
       both ends needs $M^2 - \varepsilon^2 = -p^2 < 0$, $b = \sin(fpy)$, and
       $\sin(-fpL) = 0$, so $p = n\pi/(fL)$: $\varepsilon = \pm\sqrt{M^2 +
       (n\pi/(fL))^2}$, $n = 1, 2, \dots$; the orbital has $b = \sin(n\pi y/L)$.
    5. EVEN fold condition and $\varepsilon = 0$: the equations decouple,
       $a' = fMa$, $b' = -fMb$; $b = 0$ satisfies both conditions and $a = e^{fMy}$:
       the FOLD ZERO MODE, largest at the fold, for every $L$.
    6. ODD fold condition, $a(0) = 0$ and $b(-L) = 0$: $b = \sin(fp(y + L))$ and, by
       1, $a(0) = 0$ means $b'(0)/f + Mb(0) = 0$, i.e. $p\cos(pfL) + M\sin(pfL) = 0$,
       or $\tan(pfL) = -p/M$; then $\varepsilon = \pm\sqrt{M^2 + p^2}$. In each
       interval $(n + \frac12)\pi/(fL) < p < (n + 1)\pi/(fL)$ there is exactly one root
       $p_n$.

    Only the product $fL$, the proper length of the cut-off half, enters. Every
    level holds 4 states per block type (the four blocks of the same $j$), 8 in all.
    The next cell verifies 4 to 6 with sympy and computes the exact levels for the
    labels $-3, \dots, 5$ of both fold conditions and the four cases of the record,
    in the label convention of the Rust solver (even: label 0 the zero mode, label
    $n > 0$ the $n$-th positive level, $-n$ its negative; odd: label $l \ge 0$ the
    root $p_l$ with the plus sign, label $l \le -1$ the root $p_{-l-1}$ with the minus
    sign). The hidden scale of a slice is computed as the Rust solver does,
    $f = e^{(\beta/2 - 1)a_{4,0}}$ with $\beta = 4/3$ (that is $e^{-a_{4,0}}b_{4,0}^{1/2}$
    on the history). The odd roots are found by bisection in their intervals, as the
    Rust solver does. The exact levels must equal the column `eps_analytic` of the
    Rust solver's record.
    """),
    code(r'''
    Lc = sp.symbols("L", positive=True)
    n_int = sp.symbols("n", integer=True, positive=True)
    ok_exact = sp.simplify(sp.diff(sp.exp(fs * M * y), y)
                           - fs * M * sp.exp(fs * M * y)) == 0  # step 5
    for j in (1, -1):  # step 4: b = sin(n pi y/L), a = (b'/f + M b)/(j eps)
        p_n = n_int * sp.pi / (fs * Lc)
        eps_n = sp.sqrt(M ** 2 + p_n ** 2)
        b_n = sp.sin(n_int * sp.pi * y / Lc)
        a_n = (sp.diff(b_n, y) / fs + M * b_n) / (j * eps_n)
        ok_exact &= sp.simplify(sp.diff(a_n, y) - fs * (M * a_n - j * eps_n * b_n)) == 0
        ok_exact &= sp.simplify(sp.diff(b_n, y) - fs * (j * eps_n * a_n - M * b_n)) == 0
        ok_exact &= b_n.subs(y, 0) == 0 and sp.simplify(b_n.subs(y, -Lc)) == 0
    p = sp.symbols("p", positive=True)  # step 6 (j = +1)
    b_odd = sp.sin(fs * p * (y + Lc))
    eps_odd = sp.sqrt(M ** 2 + p ** 2)
    a_odd = (sp.diff(b_odd, y) / fs + M * b_odd) / eps_odd
    ok_exact &= sp.simplify(sp.diff(a_odd, y) - fs * (M * a_odd - eps_odd * b_odd)) == 0
    ok_exact &= sp.simplify(a_odd.subs(y, 0) * eps_odd
                            - (p * sp.cos(p * fs * Lc) + M * sp.sin(p * fs * Lc))) == 0
    check(ok_exact and record_check("bc_exact_k0_spectra"),
          "the zero mode e^(fMy), the even levels and the odd condition tan(pfL) = -p/M",
          record=f"{PY_REPORT}, check bc_exact_k0_spectra")
    BETA = 4.0 / 3.0  # the history b4 = b4(0) e^(beta a4) of the record


    def hidden_scale(a4_value):
        """f = e^((beta/2 - 1) a4,0) = e^(-a4,0) b4,0^(1/2) on the history."""
        return math.exp((0.5 * BETA - 1.0) * a4_value)


    def odd_roots(m, fL, count):
        """The first count roots p of m sin(p fL) + p cos(p fL) = 0, by bisection."""
        roots = []
        for n in range(count):
            lo, hi = (n + 0.5) * math.pi / fL, (n + 1.0) * math.pi / fL
            g_ = lambda q: m * math.sin(q * fL) + q * math.cos(q * fL)
            g_lo = g_(lo)
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if mid <= lo or mid >= hi:  # the interval cannot shrink any more
                    break
                if (g_(mid) > 0.0) == (g_lo > 0.0):
                    lo = mid
                else:
                    hi = mid
            roots.append(0.5 * (lo + hi))
        return roots


    def exact_level(m, L, a4_value, parity, label):
        """The exact k = 0 level with the given fold condition and label."""
        fL = hidden_scale(a4_value) * L  # the proper length of the cut-off half
        if parity == "even":
            if label == 0:
                return 0.0
            return math.copysign(math.sqrt(m * m + (label * math.pi / fL) ** 2), label)
        roots = odd_roots(m, fL, 6)
        if label >= 0:
            return math.sqrt(m * m + roots[label] ** 2)
        return -math.sqrt(m * m + roots[-label - 1] ** 2)


    CASES = [(1.0, 3.0, 0.0), (1.0, 2.0, 0.0), (2.0, 3.0, 0.0), (1.0, 3.0, 1.5)]
    LABELS = list(range(-3, 6))  # the labels -3 ... 5
    record_rows = repository_file(
        "Revision/kohn_sham/results/spectrum/free-k0-analytic.csv"
    ).read_text(encoding="utf-8").splitlines()
    header = record_rows[0].split(",")
    record = [dict(zip(header, row.split(","))) for row in record_rows[1:]]


    def key_of(row):
        """(m, L, a4, parity, label) of a record row."""
        return (float(row["m"]), float(row["L"]), float(row["a4"]), row["parity"],
                int(row["label"]))


    exact = {}  # (m, L, a4, parity, label) -> exact level
    for m_, L_, a_ in CASES:
        for label in LABELS:
            for parity in ("even", "odd"):
                exact[(m_, L_, a_, parity, label)] = exact_level(m_, L_, a_, parity,
                                                                 label)
    worst = max(abs(exact[key_of(r)] - float(r["eps_analytic"])) for r in record)
    for m_, L_, a_ in ((1.0, 3.0, 0.0), (1.0, 3.0, 1.5)):
        fL_ = hidden_scale(a_) * L_
        say(f"(m, L, a4,0) = ({m_:g}, {L_:g}, {a_:g}), fL = {fL_:.6f}: odd roots p = "
            + ", ".join(f"{q:.6f}" for q in odd_roots(m_, fL_, 3)) + ", ...")
    lowest_odd = exact[(1.0, 3.0, 0.0, "odd", 0)]  # the lowest odd level, m = 1, L = 3
    lowest_even = exact[(1.0, 3.0, 0.0, "even", 1)]  # the lowest positive even level
    report("lowest odd level for m = 1, L = 3, a4,0 = 0", f"{lowest_odd:.12f}", "m")
    report("lowest positive even level for m = 1, L = 3, a4,0 = 0",
           f"{lowest_even:.12f}", "m")
    report("lowest odd and even levels at a4,0 = 1.5 (f = e^(-1/2))",
           f"{exact[(1.0, 3.0, 1.5, 'odd', 0)]:.12f}, "
           f"{exact[(1.0, 3.0, 1.5, 'even', 1)]:.12f}", "m")
    check(len(record) == 72 and worst < 1e-12,
          "the 72 exact levels equal the column eps_analytic of the record",
          record="Revision/kohn_sham/results/spectrum/free-k0-analytic.csv, eps_analytic")
    '''),
    md(r"""
    The next cell draws the odd condition for $m = 1$, $L = 3$ at two slices: the
    function $g(p) = M\sin(pfL) + p\cos(pfL)$ for $p$ from 0 to 7, at the slice 0
    ($f = 1$) and at the slice $a_{4,0} = 1.5$ ($f = e^{-1/2}$), with their roots
    marked. Each root gives the level $\sqrt{M^2 + p_n^2}$. When the hidden
    direction shrinks ($f$ smaller), the roots move to larger $p$ and the odd levels
    rise.
    """),
    code(r'''
    p_values = np.linspace(0.0, 7.0, 1401)
    fig, ax = plt.subplots(figsize=(8.0, 4.0))
    for a_, color in ((0.0, "C0"), (1.5, "C1")):
        fL_ = hidden_scale(a_) * 3.0
        ax.plot(p_values, 1.0 * np.sin(fL_ * p_values) + p_values * np.cos(fL_ * p_values),
                color=color, label=f"$a_{{4,0}} = {a_}$: $fL = {fL_:.4f}$")
        roots_ = odd_roots(1.0, fL_, 6)
        ax.plot([q for q in roots_ if q < 7.0], [0.0] * sum(q < 7.0 for q in roots_), "o",
                color=color)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("$p$ (wave number along $y$ per unit proper length, units of $H$)")
    ax.set_ylabel("$g(p) = M\\sin(pfL) + p\\cos(pfL)$")
    ax.set_title("the odd fold condition $\\tan(pfL) = -p/M$ for $M = 1$, $L = 3$")
    ax.legend(fontsize=8, loc="lower left")
    save_figure(fig, "odd_condition",
                "The level condition of the odd fold condition for $M = 1$ and "
                "$L = 3$: the function $g(p) = M\\sin(pfL) + p\\cos(pfL)$ against the "
                "wave number $p$ (units of $H$) at the slice $a_{4,0} = 0$ ($f = 1$, "
                "blue) and at the slice $a_{4,0} = 1.5$ of the history "
                "($f = e^{-1/2}$, orange); its zeros (dots) solve $\\tan(pfL) = -p/M$, "
                "one in each interval from $(n + 1/2)\\pi/(fL)$ to "
                "$(n + 1)\\pi/(fL)$, and each gives the pair of levels "
                "$\\pm\\sqrt{M^2 + p^2}$; the first root $p_0 = 0.8185$ at the slice 0 "
                "gives the lowest odd level $1.2923\\,m$; at the later slice the "
                "proper length $fL$ of the half is shorter and the roots lie higher.")
    '''),
    md(r"""
    ## 8. The shooting method and the Pruefer angle

    Shooting: start at the tip with the tip condition, $(a, b) = (\cos\frac\theta2,
    \sin\frac\theta2)$ (for the canonical $\theta = 0$ this is $(1, 0)$, so
    $b(-L) = 0$), integrate the real form from $y = -L$ to $y = 0$ for a trial
    energy $\varepsilon$, and look at the end point. The level is the energy for
    which the fold condition holds.

    To count, use the Pruefer angle $\theta(y) = \mathrm{atan2}(b, a)$, followed
    continuously. Line by line:

    1. $a = r\cos\theta$, $b = r\sin\theta$, so $\theta' = (ab' - ba')/r^2$.
    2. Insert the real form: $ab' - ba' = f[j\varepsilon'(a^2 + b^2) - K(a^2 - b^2)
       - 2Mab]$ with $\varepsilon' = \varepsilon - v$.
    3. With $a^2 - b^2 = r^2\cos2\theta$ and $2ab = r^2\sin2\theta$:
       $\theta' = f[j(\varepsilon - v) - K\cos2\theta - M\sin2\theta]$.
    4. The derivative of the end angle with respect to the energy is
       $d\theta(0)/d\varepsilon = jf\int_{-L}^0 r^2\,dy\,/\,r(0)^2$; so
       $\Phi(\varepsilon) = j\,\theta(0)$ grows strictly with $\varepsilon$.

    The fold condition says: even, $b(0) = 0$, i.e. $\Phi = l\pi$; odd, $a(0) = 0$,
    i.e. $\Phi = \pi/2 + l\pi$, with an integer label $l$. Because $\Phi$ only grows,
    and $\Phi(\varepsilon) - f\varepsilon L$ stays bounded (so $\Phi$ runs from
    $-\infty$ to $+\infty$), each label has exactly one level, no level can be
    missed, and bisection on $\Phi(\varepsilon) - $ target always finds it.

    The next cell checks line 3 with sympy and defines the two numerical tools of
    the notebook: `shoot`, written exactly as in the Rust solver (classical RK4 with
    $G$ steps on $[-L, 0]$, the three coefficients $fM$, $f\kappa k$ and
    $fj\varepsilon$ formed first as the solver forms them, the angle unwrapped after
    every step), and `levels` (plain bisection, 72 halvings of the interval
    $[-20, 20]$, which reaches the resolution of floating-point numbers; the Rust
    solver finds the same root with a safeguarded Newton-bisection that stops at the
    tolerance $10^{-13}$). Both work on whole arrays of energies at once (numpy),
    which makes them fast. (In the free problem the coefficients do not depend on
    $y$; the Rust solver also stores them on a fine grid of nodes and step
    midpoints, for the self-consistent potentials, which is not needed here.)
    """),
    code(r'''
    r_s, t_s = sp.symbols("r t", positive=True)  # polar coordinates of (a, b)
    a_p = r_s * sp.cos(t_s)
    b_p = r_s * sp.sin(t_s)
    j_s = sp.symbols("j")
    num = (a_p * fs * ((j_s * e - K) * a_p - M * b_p)
           - b_p * fs * (M * a_p - (K + j_s * e) * b_p))  # a b' - b a'
    pruefer = fs * (j_s * e - K * sp.cos(2 * t_s) - M * sp.sin(2 * t_s))
    check(sp.simplify(num / r_s ** 2 - pruefer) == 0,
          "d theta/dy = f[j(eps - v) - K cos 2theta - M sin 2theta]")


    def shoot(eps, k=0.0, j=1.0, M=1.0, L=3.0, G=900, a4=0.0, tip=0.0, keep=False):
        """Integrate the real form from the tip to the fold for the energies eps.

        eps, k, j may be arrays (numpy combines them element by element).  Returns
        Phi = j theta(0); with keep=True also theta, a and b at the G + 1 nodes."""
        eps, k, j = np.broadcast_arrays(np.asarray(eps, dtype=float),
                                        np.asarray(k, dtype=float),
                                        np.asarray(j, dtype=float))
        f = hidden_scale(a4)  # the hidden scale of the slice
        kappa = math.exp(-a4)  # the momentum weight of the slice
        mass, K_, je = f * M, f * (k * kappa), f * j * eps  # the solver's coefficients
        h = L / G
        a_ = np.full(eps.shape, math.cos(0.5 * tip))  # the tip condition
        b_ = np.full(eps.shape, math.sin(0.5 * tip))
        theta = np.full(eps.shape, 0.5 * tip)
        raw = np.arctan2(b_, a_)
        path = [(theta, a_, b_)]
        for i in range(G):
            p1a, p1b = mass * a_ - (K_ + je) * b_, (je - K_) * a_ - mass * b_
            a2, b2 = a_ + 0.5 * h * p1a, b_ + 0.5 * h * p1b
            p2a, p2b = mass * a2 - (K_ + je) * b2, (je - K_) * a2 - mass * b2
            a3, b3 = a_ + 0.5 * h * p2a, b_ + 0.5 * h * p2b
            p3a, p3b = mass * a3 - (K_ + je) * b3, (je - K_) * a3 - mass * b3
            a4_, b4_ = a_ + h * p3a, b_ + h * p3b
            p4a, p4b = mass * a4_ - (K_ + je) * b4_, (je - K_) * a4_ - mass * b4_
            a_ = a_ + h / 6.0 * (p1a + 2.0 * p2a + 2.0 * p3a + p4a)
            b_ = b_ + h / 6.0 * (p1b + 2.0 * p2b + 2.0 * p3b + p4b)
            new = np.arctan2(b_, a_)
            step = new - raw  # the change of the angle, brought into (-pi, pi]
            step = np.where(step > np.pi, step - 2 * np.pi,
                            np.where(step <= -np.pi, step + 2 * np.pi, step))
            theta = theta + step
            raw = new
            if keep:
                path.append((theta, a_, b_))
        if keep:
            return j * theta, [np.array(q) for q in zip(*path)]
        return j * theta


    def target(parity, label):
        """Phi of the level: l pi (even) or pi/2 + l pi (odd)."""
        offset = np.where(np.asarray(parity) == "even", 0.0, 0.5 * np.pi)
        return offset + np.asarray(label, dtype=float) * np.pi


    def levels(k, j, parity, label, iterations=72, **options):
        """The levels with the given labels, by bisection on Phi(eps) - target."""
        k, j, parity, label = np.broadcast_arrays(
            np.asarray(k, dtype=float), np.asarray(j, dtype=float),
            np.asarray(parity), np.asarray(label))
        goal = target(parity, label)
        lo, hi = np.full(k.shape, -20.0), np.full(k.shape, 20.0)
        for _ in range(iterations):
            mid = 0.5 * (lo + hi)
            g = shoot(mid, k, j, **options) - goal
            lo = np.where(g <= 0.0, mid, lo)  # g = 0: an exact level
            hi = np.where(g >= 0.0, mid, hi)
        return 0.5 * (lo + hi)


    say("defined: shoot(eps, k, j, M, L, G, a4, ...) and levels(k, j, parity, label, ...)")
    '''),
    md(r"""
    The next cell computes the shooting function $\Phi(\varepsilon)$ for $m = 1$,
    $L = 3$, $k = 0$, $j = +1$ and 801 energies from $-4$ to $4$ at once, at the
    slices 0 and 1.5, checks that it grows strictly (line 4 of the derivation),
    checks the same for a nonzero momentum $k = 0.75$, both block types and both
    slices (the test of the Rust solver), and draws it with the targets $l\pi$ (even)
    and $\pi/2 + l\pi$ (odd): every crossing of a curve with one of its targets is a
    level.
    """),
    code(r'''
    trial = np.linspace(-4.0, 4.0, 801)  # 801 trial energies
    phi_curve = shoot(trial, 0.0, 1.0)  # Phi for k = 0, j = +1, slice 0
    phi_late = shoot(trial, 0.0, 1.0, a4=1.5)  # the same at the slice 1.5
    grows = bool(np.all(np.diff(phi_curve) > 0.0) and np.all(np.diff(phi_late) > 0.0))
    grows_k = all(bool(np.all(np.diff(shoot(np.linspace(-4.0, 3.96, 200), 0.75, jj,
                                            a4=aa)) > 0))
                  for jj in (1.0, -1.0) for aa in (0.0, 1.5))
    check(grows and grows_k,
          "Phi(eps) grows strictly with eps (k = 0 and 0.75, both block types, 2 slices)")
    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    ax.plot(trial, phi_curve / np.pi, color="C0",
            label="$\\Phi(\\varepsilon)/\\pi$, $a_{4,0} = 0$")
    ax.plot(trial, phi_late / np.pi, "--", color="C3",
            label="$\\Phi(\\varepsilon)/\\pi$, $a_{4,0} = 1.5$")
    for label in range(-3, 4):  # the targets in units of pi
        ax.axhline(label, color="C1", linewidth=0.7)
        ax.axhline(label + 0.5, color="C2", linewidth=0.7, linestyle="--")
    even_levels = [exact[(1.0, 3.0, 0.0, "even", l)] for l in range(-2, 3)]
    odd_levels = [exact[(1.0, 3.0, 0.0, "odd", l)] for l in range(-2, 2)]
    ax.plot(even_levels, range(-2, 3), "o", color="C1",
            label="even levels: $\\Phi = l\\pi$")
    ax.plot(odd_levels, [l + 0.5 for l in range(-2, 2)], "s", color="C2",
            label="odd levels: $\\Phi = \\pi/2 + l\\pi$")
    ax.set_xlabel("trial energy $\\varepsilon$ (units of $m$)")
    ax.set_ylabel("$\\Phi(\\varepsilon) / \\pi$")
    ax.set_title("the shooting function for $k = 0$, $j = +1$, $m = 1$, $L = 3$")
    ax.legend(fontsize=8, loc="upper left")
    save_figure(fig, "shooting_function",
                "The shooting function $\\Phi(\\varepsilon) = j\\,\\theta(0)$ (the "
                "Pruefer angle at the fold, in units of $\\pi$) against the trial "
                "energy $\\varepsilon$ (units of $m$) for $k = 0$, $j = +1$, $m = 1$, "
                "$L = 3$ at the slice 0 (solid) and at the slice $a_{4,0} = 1.5$ "
                "(dashed). The solid horizontal lines are the even targets $l\\pi$, "
                "the dashed ones the odd targets $\\pi/2 + l\\pi$; each curve rises "
                "steadily, so it crosses every target exactly once, and the crossings "
                "are the levels (circles even, squares odd, at the slice 0), "
                "including the zero mode at $\\varepsilon = 0$, $\\Phi = 0$; between "
                "$-1$ and $1$ the curves rise only a little, because no level lies "
                "there except the zero mode; at the later slice the curve rises more "
                "slowly ($\\Phi$ grows like $f\\varepsilon L$) and its levels lie "
                "farther apart.")
    '''),
    md(r"""
    ## 9. All 72 levels: numerical against exact

    The next cell computes the 72 levels of the record (labels $-3$ to $5$, both
    fold conditions, four cases) by shooting and bisection, with the step numbers of
    the Rust solver: $G = 900$ for $L = 3$ and $G = 600$ for $L = 2$ (the same step
    $h = 1/300$). It checks three things:

    - the numerical levels equal the Rust solver's column `eps_numeric` to
      $10^{-11}$ (both programs integrate the same RK4 discretisation and find the
      root of the same shooting function, this notebook by plain bisection down to
      the last digit, the Rust solver by a safeguarded Newton-bisection that stops
      at its tolerance $10^{-13}$ or sooner; the printed largest difference is of
      order $10^{-14}$);
    - the largest numerical errors $|\varepsilon_{\rm num} -
      \varepsilon_{\rm exact}|$, for $|\varepsilon| < 4m$ and above, equal the ones
      the Rust check `free_k0_analytic_spectra` measured (read from its record) and
      lie below its tolerances $5\times10^{-9}$ and $3\times10^{-7}$ (the RK4 error
      grows like $(fh\varepsilon)^4$);
    - the zero mode comes out as exactly 0 in all four cases.

    It prints the levels of the case $m = 1$, $L = 3$ at the slice 0 next to the
    exact ones, the largest difference from the Rust levels and the two largest
    errors.
    """),
    code(r'''
    numeric = {}  # (m, L, a4, parity, label) -> numerical level at the canonical step
    pars = np.array([p_ for l_ in LABELS for p_ in ("even", "odd")])
    labs = np.array([l_ for l_ in LABELS for p_ in ("even", "odd")])
    for m_, L_, a_ in CASES:
        found = levels(0.0, 1.0, pars, labs, M=m_, L=L_, G=round(900 * L_ / 3), a4=a_)
        for p_, l_, x in zip(pars, labs, found):
            numeric[(m_, L_, a_, str(p_), int(l_))] = float(x)
    say("m = 1, L = 3, a4,0 = 0:")
    heads = ["even (numerical)", "even (exact)", "odd (numerical)", "odd (exact)"]
    say("label  " + "  ".join(f"{text:>16}" for text in heads))
    for l_ in LABELS:
        row = [numeric[(1.0, 3.0, 0.0, "even", l_)], exact[(1.0, 3.0, 0.0, "even", l_)],
               numeric[(1.0, 3.0, 0.0, "odd", l_)], exact[(1.0, 3.0, 0.0, "odd", l_)]]
        say(f"{l_:+5d}  " + "  ".join(f"{x:16.10f}" for x in row))
    rust_diff = max(abs(numeric[key_of(r)] - float(r["eps_numeric"])) for r in record)
    report("largest difference from the Rust solver's levels", f"{rust_diff:.1e}", "m")
    check(rust_diff < 1e-11,
          "the 72 numerical levels equal those of the Rust solver",
          record="Revision/kohn_sham/results/spectrum/free-k0-analytic.csv, eps_numeric")
    errors = {key: abs(numeric[key] - exact[key]) for key in numeric}
    low = max(err for key, err in errors.items() if abs(exact[key]) < 4.0)
    high = max(err for key, err in errors.items() if abs(exact[key]) >= 4.0)
    report("largest error for |eps| < 4 m", f"{low:.2e}", "m")
    report("largest error for |eps| >= 4 m", f"{high:.2e}", "m")
    import re  # regular expressions: patterns that find numbers in a text


    def record_detail(name, report_file):
        """The detail text of the check called name in a Revision report."""
        data = json.loads(repository_file(report_file).read_text(encoding="utf-8"))
        return [c["detail"] for c in data["checks"] if c["name"] == name][0]


    detail = record_detail("free_k0_analytic_spectra", RUST_REPORT)
    rec_low, tol_low, rec_high, tol_high = re.findall(r"\d+(?:\.\d+)?e-\d+", detail)
    check(f"{low:.2e}" == f"{float(rec_low):.2e}"
          and f"{high:.2e}" == f"{float(rec_high):.2e}"
          and low < float(tol_low) and high < float(tol_high)
          and record_check("free_k0_analytic_spectra", (RUST_REPORT,)),
          f"largest errors {low:.2e} for |eps| < 4 m and {high:.2e} above, as in the "
          f"record, below its tolerances {tol_low} and {tol_high}",
          record=f"{RUST_REPORT}, check free_k0_analytic_spectra")
    check(all(numeric[(m_, L_, a_, "even", 0)] == 0.0 for m_, L_, a_ in CASES),
          "the fold zero mode comes out as exactly eps = 0 in all four cases")
    '''),
    md(r"""
    The next cell draws the four spectra as level ladders: for each case
    $(m, L, a_{4,0})$ the exact levels as short horizontal lines and the numerical
    ones as markers (even fold condition on the left of each ladder, odd on the
    right). The gap $(-M, M)$ around zero contains only the zero mode; a larger $m$
    widens it; a shorter proper length $fL$ (a shorter $L$, or the later slice with
    $f = e^{-1/2}$) spreads the levels, because the wave numbers $n\pi/(fL)$ grow.
    """),
    code(r'''
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    for position, (m_, L_, a_) in enumerate(CASES):
        x0 = 3.0 * position  # the horizontal place of this ladder
        for l_ in LABELS:
            for shift, parity, color, marker in ((0.0, "even", "C0", "o"),
                                                 (1.2, "odd", "C1", "s")):
                level = exact[(m_, L_, a_, parity, l_)]
                ax.plot([x0 + shift - 0.4, x0 + shift + 0.4], [level, level],
                        color=color, linewidth=1.5)
                ax.plot([x0 + shift], [numeric[(m_, L_, a_, parity, l_)]], marker,
                        color=color, markersize=4)
        ax.fill_between([x0 - 0.5, x0 + 1.7], -m_, m_, color="gray", alpha=0.12)
    ax.set_xlim(-0.6, 11.4)
    ax.set_ylim(-9.5, 10.5)
    ax.set_xticks([0.6, 3.6, 6.6, 9.6])
    ax.set_xticklabels(["$m = 1$, $L = 3$\n$a_{4,0} = 0$", "$m = 1$, $L = 2$\n$a_{4,0} = 0$",
                        "$m = 2$, $L = 3$\n$a_{4,0} = 0$",
                        "$m = 1$, $L = 3$\n$a_{4,0} = 1.5$"], fontsize=8)
    ax.plot([], [], "o-", color="C0", label="even (line exact, dot numerical)")
    ax.plot([], [], "s-", color="C1", label="odd (line exact, square numerical)")
    ax.set_ylabel("level $\\varepsilon$ (units of $H = 1$)")
    ax.set_title("the free $k = 0$ spectra, labels $-3$ to $5$")
    ax.legend(fontsize=8, loc="lower right")
    save_figure(fig, "spectrum_ladder",
                "The free $k = 0$ spectra for the four cases of the record "
                "$(m, L, a_{4,0}) = (1, 3, 0)$, $(1, 2, 0)$, $(2, 3, 0)$ and "
                "$(1, 3, 1.5)$, labels $-3$ to $5$: exact levels as short horizontal "
                "lines, numerical RK4 levels as markers on them (even fold condition "
                "left, odd right of each ladder); vertical axis the level in units "
                "of $H = 1$. The shaded band from $-m$ to $m$ contains only the even "
                "zero mode at $0$; a larger mass widens the gap, and a shorter proper "
                "length $fL$ of the half (a shorter $L$, or the later slice with "
                "$f = e^{-1/2}$) spreads the levels; on this scale the numerical and "
                "the exact levels cannot be told apart.")
    '''),
    md(r"""
    ## 10. Fourth-order convergence

    RK4 has an error proportional to $h^4$: halving the step should divide the error
    of every level by $2^4 = 16$. The Rust solver's refined run (the record
    `ks-rust-determinism.json`, check `refined_free_spectra_convergence_order`)
    doubled the step number ($G = 1800$ for $L = 3$, $1200$ for $L = 2$) and
    reported the median error ratio 16.00 over 39 levels whose canonical error
    exceeds $10^{-11}$, with the largest errors $5.050\times10^{-8}$ (canonical) and
    $3.157\times10^{-9}$ (refined). One detail of that record matters for the count:
    its comparison program (`Revision/kohn_sham/solver/tools/compare_runs.py`) keys
    the rows of `free-k0-analytic.csv` by $(m, L$, fold condition, label$)$ without
    the slice, so the 18 rows of the case $(1, 3, 1.5)$ replace those of the case
    $(1, 3, 0)$, and its 39 levels belong to the 54 levels of the cases $(1, 3, 1.5)$,
    $(1, 2, 0)$ and $(2, 3, 0)$. The next cell repeats the measurement in exactly that
    way and checks the four numbers of the record, and then measures it over all 72
    levels as well. It takes about 30 seconds.
    """),
    code(r'''
    refined = {}
    for m_, L_, a_ in CASES:
        found = levels(0.0, 1.0, pars, labs, M=m_, L=L_, G=round(1800 * L_ / 3), a4=a_)
        for p_, l_, x in zip(pars, labs, found):
            refined[(m_, L_, a_, str(p_), int(l_))] = float(x)
    refined_errors = {key: abs(refined[key] - exact[key]) for key in refined}
    as_in_record = {}  # keyed by (m, L, parity, label): later rows replace earlier ones
    for r in record:
        as_in_record[(r["m"], r["L"], r["parity"], r["label"])] = key_of(r)
    keys = list(as_in_record.values())


    def measurement(selected):
        """(count, median ratio, largest canonical error, largest refined error)."""
        ratios = sorted(errors[q] / refined_errors[q] for q in selected
                        if errors[q] > 1e-11 and refined_errors[q] > 0.0)
        return (len(ratios), ratios[len(ratios) // 2],
                max(errors[q] for q in selected), max(refined_errors[q] for q in selected))


    count, median, worst_c, worst_r = measurement(keys)
    count_all, median_all, _, _ = measurement(list(errors))
    report("levels compared as in the record", len(keys))
    report("number of levels with a canonical error above 1e-11", count)
    report("median error ratio canonical / refined", f"{median:.2f}")
    report("largest error, canonical step", f"{worst_c:.3e}", "m")
    report("largest error, refined step", f"{worst_r:.3e}", "m")
    report("over all 72 levels: levels above 1e-11, median ratio",
           f"{count_all}, {median_all:.2f}")
    DETERMINISM = "Revision/kohn_sham/reports/ks-rust-determinism.json"
    detail = record_detail("refined_free_spectra_convergence_order", DETERMINISM)
    rec_canonical, rec_refined = re.search(r"canonical (\S+), refined (\S+);",
                                           detail).groups()
    rec_median, rec_count = re.search(r"ratio (\S+) over (\d+) levels",
                                      detail).groups()
    check(len(keys) == 54 and count == int(rec_count) and f"{median:.2f}" == rec_median
          and f"{worst_c:.3e}" == rec_canonical and f"{worst_r:.3e}" == rec_refined
          and record_check("refined_free_spectra_convergence_order", (DETERMINISM,)),
          f"{count} levels, median error ratio {median:.2f}, largest errors "
          f"{worst_c:.3e} and {worst_r:.3e}",
          record=f"{DETERMINISM}, check refined_free_spectra_convergence_order")
    '''),
    md(r"""
    The next cell draws the convergence for four levels of the case $m = 1$,
    $L = 3$ at the slice 0 (even labels 1 and 3, odd labels 0 and 3), with the step
    numbers $G = 150, 300, 600, 900, 1800$: the error against the step $h = L/G$ on
    logarithmic axes, with a line of slope 4 for comparison.
    """),
    code(r'''
    chosen = [("even", 1), ("even", 3), ("odd", 0), ("odd", 3)]
    steps = [150, 300, 600, 900, 1800]
    curves = {key: [] for key in chosen}
    for G_ in steps:
        found = levels(0.0, 1.0, np.array([p_ for p_, l_ in chosen]),
                       np.array([l_ for p_, l_ in chosen]), M=1.0, L=3.0, G=G_)
        for key, x in zip(chosen, found):
            curves[key].append(abs(float(x) - exact[(1.0, 3.0, 0.0) + key]))
    h_values = np.array([3.0 / G_ for G_ in steps])
    fig, ax = plt.subplots(figsize=(7.0, 4.6))
    for (parity, label), errs in curves.items():
        ax.loglog(h_values, errs, "o-", label=f"{parity}, label {label}")
    ax.loglog(h_values, 3e-2 * h_values ** 4, ":", color="black",
              label="slope 4: error $\\propto h^4$")
    ax.set_xticks(h_values)  # one tick at each step used
    ax.set_xticklabels([f"{x:.4f}" for x in h_values], fontsize=8)
    ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())  # no extra ticks
    ax.set_xlabel("RK4 step $h = L/G$ (units of $1/H$)")
    ax.set_ylabel("$|\\varepsilon_{\\rm RK4} - \\varepsilon_{\\rm exact}|$ (units of $m$)")
    ax.set_title("fourth-order convergence of the shooting method ($m = 1$, $L = 3$)")
    ax.legend(fontsize=8)
    fourth = all(12.0 < errs[i] / errs[i + 1] < 20.0 for errs in curves.values()
                 for i in range(2))  # halving h from 0.02 to 0.005: ratios near 16
    check(fourth, "halving the step divides each error by about 16 (between 12 and 20)")
    save_figure(fig, "rk4_convergence",
                "The error of four numerical levels ($m = 1$, $L = 3$, slice 0; even "
                "labels 1 and 3, odd labels 0 and 3) against the RK4 step $h = L/G$ "
                "for $G = 150, 300, 600, 900, 1800$, on logarithmic axes (both in "
                "units of $m = H = 1$). The points fall on lines parallel to the "
                "dotted line of slope 4: halving the step divides the error by 16, "
                "the order of the classical Runge-Kutta method; higher levels have "
                "larger errors because their orbitals oscillate faster.")
    '''),
    md(r"""
    ## 11. The orbitals

    The orbital of a level is the solution $(a, b)$ itself, normalised so that
    $\int_{-L}^0(a^2 + b^2)\,dy = 1$ (on one half of the cell). The next cell defines
    `orbital`, again as in the Rust solver: it keeps $(a, b)$ at the nodes, fills the
    step midpoints by cubic Hermite interpolation (from the values and the
    derivatives at the two neighbouring nodes, error of order $h^4$), and normalises
    with Simpson's rule on the fine grid of nodes and midpoints. It then checks the
    fold zero mode against the exact $a = \sqrt{2fM/(1 - e^{-2fML})}\,e^{fMy}$,
    $b = 0$ at the slices 0 ($f = 1$) and 2 ($f = e^{-2/3}$) (the Rust check
    `free_zero_mode_exact`: $\varepsilon = 0$ exactly, $b = 0$ exactly, $a$ to
    $10^{-9}$), and the first even and odd orbitals at the slice 0 against the exact
    ones of section 7 (normalised the same way and with the sign that makes
    $a(-L) > 0$).
    """),
    code(r'''
    def orbital(eps, k=0.0, j=1.0, M=1.0, L=3.0, G=900, a4=0.0, tip=0.0):
        """The normalised orbital (y, a, b) and the Simpson weights on the fine grid."""
        _, (theta_n, a_n, b_n) = shoot(eps, k, j, M=M, L=L, G=G, a4=a4, tip=tip,
                                       keep=True)
        nf, h = 2 * G + 1, L / G
        y_fine = -L * ((nf - 1 - np.arange(nf)) / (nf - 1))
        f = hidden_scale(a4)
        mass, K_, je = f * M, f * (k * math.exp(-a4)), f * j * eps
        a_f, b_f = np.zeros(nf), np.zeros(nf)
        a_f[0::2], b_f[0::2] = a_n, b_n  # the node values
        da = mass * a_f - (K_ + je) * b_f  # the derivatives d/dy at the nodes
        db = (je - K_) * a_f - mass * b_f
        for i in range(1, nf, 2):  # cubic Hermite value at each midpoint
            a_f[i] = 0.5 * (a_f[i - 1] + a_f[i + 1]) + h / 8.0 * (da[i - 1] - da[i + 1])
            b_f[i] = 0.5 * (b_f[i - 1] + b_f[i + 1]) + h / 8.0 * (db[i - 1] - db[i + 1])
        weights = np.full(nf, 2.0)  # Simpson: 1, 4, 2, 4, ..., 4, 1 times (h/2)/3
        weights[1::2] = 4.0
        weights[0] = weights[-1] = 1.0
        weights *= 0.5 * h / 3.0
        norm = math.sqrt(float(np.sum(weights * (a_f ** 2 + b_f ** 2))))
        return y_fine, a_f / norm, b_f / norm, weights


    zero_modes, deviation = {}, 0.0
    for a_ in (0.0, 2.0):
        e0 = float(levels(0.0, 1.0, "even", 0, a4=a_))
        y_f, a_zero, b_zero, simpson = orbital(e0, a4=a_)
        fM = hidden_scale(a_) * 1.0
        a_exact = math.sqrt(2.0 * fM / (1.0 - math.exp(-2.0 * fM * 3.0))) * np.exp(fM * y_f)
        deviation = max(deviation, float(np.max(np.abs(a_zero - a_exact))))
        zero_modes[a_] = (e0, a_zero, b_zero, a_exact)
    report("largest deviation of the zero-mode orbital from the exact one",
           f"{deviation:.1e}")
    check(all(zero_modes[a_][0] == 0.0 and np.all(zero_modes[a_][2] == 0.0)
              for a_ in (0.0, 2.0))
          and deviation < 1e-9 and record_check("free_zero_mode_exact", (RUST_REPORT,)),
          "zero mode: eps = 0 and b = 0 exactly, a = sqrt(2fM/(1 - e^(-2fML))) e^(fMy)",
          record=f"{RUST_REPORT}, check free_zero_mode_exact")


    def exact_orbital(parity, label, m_=1.0, L_=3.0):
        """The exact orbital of section 7 (j = +1, slice 0), normalised with Simpson."""
        level = exact[(m_, L_, 0.0, parity, label)]
        p_ = math.sqrt(level ** 2 - m_ ** 2)
        if parity == "even":
            b_e = np.sin(p_ * y_f)
            a_e = (p_ * np.cos(p_ * y_f) + m_ * b_e) / level
        else:
            b_e = np.sin(p_ * (y_f + L_))
            a_e = (p_ * np.cos(p_ * (y_f + L_)) + m_ * b_e) / level
        sign = 1.0 if a_e[0] > 0 else -1.0  # the sign with a(-L) > 0
        norm = math.sqrt(float(np.sum(simpson * (a_e ** 2 + b_e ** 2))))
        return sign * a_e / norm, sign * b_e / norm


    shown = {}
    worst_orbital = 0.0
    for parity, label in (("even", 1), ("odd", 0)):
        _, a_num, b_num, _ = orbital(numeric[(1.0, 3.0, 0.0, parity, label)])
        a_ex, b_ex = exact_orbital(parity, label)
        worst_orbital = max(worst_orbital, float(np.max(np.abs(a_num - a_ex))),
                            float(np.max(np.abs(b_num - b_ex))))
        shown[(parity, label)] = (a_num, b_num, a_ex, b_ex)
    check(worst_orbital < 1e-8,
          "the even label 1 and odd label 0 orbitals equal the exact ones to 1e-8")
    '''),
    md(r"""
    The next cell draws the orbitals of $m = 1$, $L = 3$: on the left the zero mode
    at the slices 0 and 2 (largest at the fold, $b = 0$; at the later slice
    $f = e^{-2/3}$ and the orbital $e^{fMy}$ reaches farther toward the tip), in the
    middle the even level 1 and on the right the odd level 0 at the slice 0, each
    with its two components $a$ (solid) and $b$ (dashed), and the exact curves as
    dots on top.
    """),
    code(r'''
    fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.8), sharey=True)
    for a_, style in ((0.0, "-"), (2.0, "-.")):
        e0, a_zero, b_zero, a_exact = zero_modes[a_]
        axes[0].plot(y_f, a_zero, style, color="C0",
                     label=f"$a$, $a_{{4,0}} = {a_:g}$")
        axes[0].plot(y_f[::60], a_exact[::60], ".", color="black")
    axes[0].plot(y_f, zero_modes[0.0][2], "--", color="C1", label="$b = 0$")
    axes[0].set_title("zero mode, $\\varepsilon = 0$", fontsize=9)
    panels = [(f"even label 1, $\\varepsilon = {lowest_even:.4f}$",) + shown[("even", 1)],
              (f"odd label 0, $\\varepsilon = {lowest_odd:.4f}$",) + shown[("odd", 0)]]
    for ax, (title, a_num, b_num, a_ex, b_ex) in zip(axes[1:], panels):
        ax.plot(y_f, a_num, color="C0", label="$a$ (numerical)")
        ax.plot(y_f, b_num, "--", color="C1", label="$b$ (numerical)")
        ax.plot(y_f[::60], a_ex[::60], ".", color="black", label="exact")
        ax.plot(y_f[::60], b_ex[::60], ".", color="black")
        ax.set_title(title, fontsize=9)
    for ax in axes:
        ax.set_xlabel("$y$ (units of $1/H$)")
    axes[0].set_ylabel("orbital component (normalised)")
    axes[0].legend(fontsize=7, loc="upper left")
    axes[1].legend(fontsize=7, loc="upper left")
    save_figure(fig, "orbitals",
                "The normalised orbitals $\\chi = (a, ib)$ of free $k = 0$ levels for "
                "$m = 1$, $L = 3$ against $y$ from the tip cutoff $-3$ to the fold $0$ "
                "(units of $1/H$): left the fold zero mode "
                "$a = \\sqrt{2fM/(1 - e^{-2fML})}\\,e^{fMy}$, $b = 0$, at the slice 0 "
                "($f = 1$, solid) and at the slice 2 ($f = e^{-2/3}$, dash-dotted), "
                "concentrated at the fold and less so at the later slice; middle the "
                "even level 1 with $b(0) = b(-3) = 0$; right the odd level 0 with "
                "$a(0) = 0$ and $b(-3) = 0$ (both at the slice 0). Solid lines $a$, "
                "dashed lines $b$ from the RK4 shooting, black dots the exact "
                "solutions.")
    '''),
    md(r"""
    The next cell draws how the Pruefer angle counts. For the even levels with the
    labels 0 to 3 and the odd levels with the labels 0 to 2 ($m = 1$, $L = 3$,
    $k = 0$, $j = +1$, slice 0) it plots $\theta(y)/\pi$ along the hidden coordinate:
    every curve starts at 0 at the tip and ends exactly on its target $l$ (even) or
    $l + \frac12$ (odd) at the fold. The label is the number of half-turns the point
    $(a, b)$ makes on its way.
    """),
    code(r'''
    picks = [("even", l_) for l_ in range(4)] + [("odd", l_) for l_ in range(3)]
    energies = np.array([numeric[(1.0, 3.0, 0.0, p_, l_)] for p_, l_ in picks])
    _, (theta_path, _, _) = shoot(energies, 0.0, 1.0, keep=True)
    y_nodes = np.linspace(-3.0, 0.0, 901)
    end_values = theta_path[-1] / np.pi
    goals = np.array([l_ + (0.0 if p_ == "even" else 0.5) for p_, l_ in picks])
    check(np.max(np.abs(end_values - goals)) < 1e-9,
          "the Pruefer angle ends on its target l pi or (l + 1/2) pi for every level")
    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    for column, (p_, l_) in enumerate(picks):
        style = "-" if p_ == "even" else "--"
        ax.plot(y_nodes, theta_path[:, column] / np.pi, style,
                label=f"{p_}, label {l_}")
    ax.set_xlabel("$y$ (units of $1/H$; tip cutoff at $-3$, fold at $0$)")
    ax.set_ylabel("Pruefer angle $\\theta(y)/\\pi$")
    ax.set_title("the Pruefer angle counts the half-turns ($m = 1$, $L = 3$, $k = 0$)")
    ax.legend(fontsize=8, ncol=2, loc="upper left")
    save_figure(fig, "pruefer_angle",
                "The Pruefer angle $\\theta(y) = \\mathrm{atan2}(b, a)$ in units of "
                "$\\pi$ along the hidden coordinate $y$ (units of $1/H$) for the even "
                "levels with labels 0 to 3 (solid) and the odd levels with labels 0 "
                "to 2 (dashed), $m = 1$, $L = 3$, $k = 0$, $j = +1$, slice 0. Every "
                "curve starts at $0$ at the tip (the condition $b(-3) = 0$) and ends "
                "exactly at its target at the fold, $l$ for even and $l + 1/2$ for "
                "odd; the zero mode stays at $0$ all the way.")
    '''),
    md(r"""
    ## 12. The last check

    The last cell checks that the six figure files exist and prints the number of
    checks that passed.
    """),
    code(r'''
    figure_names = ["14b_1_odd_condition.png", "14b_2_shooting_function.png",
                    "14b_3_spectrum_ladder.png", "14b_4_rk4_convergence.png",
                    "14b_5_orbitals.png", "14b_6_pruefer_angle.png"]
    check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
          "all six figure files of this notebook exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 13. What this notebook showed

    - The block equation $\chi' = fN\chi$ of the Kohn-Sham model is real in the
      variables $\chi = (a, ib)$; the hidden scale $f$ multiplies every coefficient
      (PROVED).
    - The fold joins the two halves of a cell; the reduced equation and $\chi(y)$ are
      the same on both halves; self-adjointness of the doubled cell needs a fold
      condition; the record solves and fills both $b(0) = 0$ and $a(0) = 0$
      (ASSUMED); the chosen regular tip gives $b(-L) = 0$; both ends kill the current
      and make $h_j$ self-adjoint; and nothing suppresses an orbital toward the tip
      (PROVED; reproduces the Revision checks).
    - At $k = 0$ without interaction the levels are exactly $0$ (the fold zero mode
      $e^{fMy}$), $\pm\sqrt{M^2 + (n\pi/(fL))^2}$ (even) and $\pm\sqrt{M^2 + p^2}$ with
      $\tan(pfL) = -p/M$ (odd): only the proper length $fL$ enters; for $m = 1$,
      $L = 3$ at the slice 0 the lowest positive levels are $1.2922928281\,m$ (odd)
      and $1.4479719304\,m$ (even) (PROVED).
    - RK4 shooting with the Pruefer angle finds every level by its label; the 72
      numerical levels equal the Rust solver's to about $10^{-14}$, their errors are
      within the Rust tolerances, and halving the step divides the error by 16.00
      (median over 39 levels in the record's comparison, and over 52 levels when all
      72 are compared): the method is of fourth order (COMPUTED, error measured).
    - The numerical orbitals equal the exact ones; the zero mode is exactly
      $\varepsilon = 0$, $b = 0$ at every slice.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
