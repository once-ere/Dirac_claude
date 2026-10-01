# DEFLATION SPEC — x5, x6, x7 are the three extra times that EXPONENTIALLY DEFLATE (binding; 2026-09-30)

## 0. The correction and what it changes

The user (2026-09-30, verbatim): "Your x5, x6, x7 are all wrong. x5, x6, x7 are the three
extra times that exponentially deflate. Fix this everywhere they appear, and fix your docs and
provenances."  Asked to choose, the user chose "Redo the physics": the models themselves must
keep x5, x6, x7 exponentially deflating for all time.

What was wrong: the coordinate ROLES were right everywhere (x5, x6, x7 time-like, eta = -1),
but several computations did not keep them deflating exponentially:
1. Stages 4 and 5 (Kohn-Sham) used the STATIC member a4 = const of the notebook's field: no
   deflation at all.
2. Stage 3 EXP-1 used a tanh WINDOW a4'(t) = A(1 + tanh((t-2)/0.5))(1 - tanh((t-7)/0.5))/4:
   deflation only during the window.
3. Stage 3 EXP-3 and EXP-4 assumed FROZEN extra times (b = c = 1); EXP-3's deflation was only a
   variant (c proportional to a^-gamma).
4. EXP-2 solves 8D Einstein gravity self-consistently; its extra times turn from deflation to
   expansion.  That is a computed RESULT of the dynamics, not an imposed assumption, and it stays
   a result (labelled), but its initial data must start from the notebook's deflation (D3).
5. EXP-5 already uses c = e^{-Ht}: correct, becomes the reference case.

## 1. The canonical deflating field (all stages)

The notebook's metric (Stage 2, MatrixMetric44), t = H x4, z = 6 H x0, s = sin z:

    ds^2 = cot^2 z dx0^2 + s^{1/3} e^{2 a4(t)} (dx1^2 + dx2^2 + dx3^2) - dx4^2
           - s^{1/3} e^{-2 a4(t)} (dx5^2 + dx6^2 + dx7^2)

EXPONENTIAL DEFLATION OF THE EXTRA TIMES means a4(t) = A t for ALL t of the computation, with
a constant A > 0 (canonical A = 1; second value A = 2, as the two amplitudes of the old EXP-1):
the extra-time scale factor is s^{1/6} e^{-A H x4} and 3-space inflates as s^{1/6} e^{+A H x4};
the 7-volume is constant.  This is also the late-time form of the notebook's own ProductLog
solution (a4 ~ M Sigma c t / Q1, survey_notebook-physics.md, cell 100 remark), so it is the
member the notebook's hypothesis ("superluminal inflation/deflation") refers to.  The static
member (a4 const) and the window are NOT canonical any more; they may appear only as clearly
labelled comparisons or as the instantaneous slice of D6.

Exact facts to use (Stage 2, verified): det g = +cos^2 z; gamma^mu Omega_mu = 3 H gamma^0,
independent of a4 (the time-derivative terms of the spin connection cancel because
Theta_4 = 3 A H - 3 A H = 0); the Einstein tensor and the required source for a4' = A, a4'' = 0:
rho_req = -3 H^2 (7 + A^2)/kappa (negative), the pressures from the Stage-2 formulas
(P_einstein_requiredSource); for linear a4 an x0-independent condensate is an exact source with
negative energy density (P_source_x0IndependentSourceConditions).  In the warped coordinate
y = ln(sin z)/(6H) the metric is dy^2 - dx4^2 + e^{2Hy}[e^{2 a4(t)} dx_i^2 - e^{-2 a4(t)} dx_j^2];
the Z2 brane construction is unchanged in form (its normal is d_y, so the extrinsic curvature and
the Israel stress are those of the static case at every instant), but the bulk Einstein tensor
now carries the a4' = A terms - recompute exactly (Wolfram + sympy).

## 2. Stage 2 (exact theory of the primordial field)

D1. Make a4 = A t (A = 1, 2) the canonical member in provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md
    and its reports: add exact checks for the linear member (curvature, Einstein tensor, required
    source, the x0-independent exact source, the warped y form with time-dependent a4, the bulk
    Einstein tensor of the Z2 extension with a4' = A) to wolfram/Dirac16ComplexPrimordial*.wl and
    the sympy checker; every statement about the static member is relabelled "the instantaneous
    slice" or moved to a comparison paragraph.  The general-a4 results stay (they include the
    linear member).

## 3. Stage 3 (numerical experiments)

D2. EXP-1: a4'(t) = A for all t (A = 1, 2), a4'' = 0, on the same time interval; the window code
    becomes a non-canonical option or is removed; recompute every observable (rho, p, w, the
    Lagrangian split, the required Einstein source, drifts) and the exact-solution checks.
D3. EXP-2: initial data with the notebook's deflation H_c(0) = -A H_a(0) (A = 1: H_a = 1,
    H_c = -1, H_b = 0).  The Hamiltonian constraint then demands
    kappa rho_0 = sum_{i<j} H_i H_j = 3 H_a^2 + 3 H_c^2 + 9 H_a H_c = -3 for A = 1 (negative):
    determine exactly which condensate states (x0 = lambda S_0/(2m) < -1, or other admissible
    data) satisfy it, run those, and report honestly whether the extra times KEEP deflating
    under the self-consistent dynamics (a result, never forced).  If no admissible matter
    satisfies the constraint, record that as the result.
D4. EXP-3: canonical background with exponentially deflating extra times c(t) = e^{-H_c t}
    (cosmic time t = x4, constant H_c > 0) instead of frozen ones; the condensate then obeys
    S proportional to 1/(a^3 c^3) (hidden space static, b = 1).  Canonical rates H_c / H_0 in
    {0.1, 0.5, 1} plus the notebook's tie c = 1/a (the old variant with gamma = 1, constant
    7-volume, S constant).  Recompute the (w0, wa) analysis, the energy-exchange term, the
    distances and every honesty item (negative 8D energy density, varying G_N, 4D energy
    non-conservation).  The frozen case stays only as a labelled comparison.
D5. EXP-4: thermal gas and gravitational pair creation with exponentially deflating extra times:
    during inflation c = e^{-H_inf t} = 1/a (the notebook's primordial phase), and afterwards
    c continues as e^{-H_inf t} (deflation for all time).  In the good sector the mode equation
    involves c only through the 7-volume, so per-mode results (w(a), |beta_k|^2) are expected to
    be unchanged and number densities to rescale by c^-3: VERIFY this by rerunning, do not
    assume it; report the densities per 3-volume and per 7-volume.
D6'. EXP-5 (c = e^{-Ht}) is already canonical; keep; cross-reference D7.
D7. Everything downstream of Stage 3 outputs is regenerated: the Rust tree
    artifacts/dirac16complex/numerics/, the five Python checkers, the Jupyter and Mathematica
    notebooks, the figures, provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md and
    provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md (with their PDFs re-registered), the Stage-3 gate
    (both twins, from a fresh clone at the end).

## 4. Stages 4 and 5 (Kohn-Sham) in the deflating field

D8. Physics.  In a time-dependent background a stationary Kohn-Sham ground state does not exist.
    The honest replacement is the ADIABATIC (instantaneous) Kohn-Sham problem: at each time x4
    the single-particle operator is the static one with a4,0 = a4(x4) = A H x4 (exact, because
    gamma^mu Omega_mu does not depend on a4), and the instantaneous ground and first excited
    states are computed along the history.  By the exact rescaling of STAGE4_SPEC E4.10 the
    slice a4,0 equals the a4,0 = 0 problem with Delta k e^{-a4,0}, l e^{a4,0} and lambda e^{3 a4,0}:
    the comoving 3-space momenta redshift as 3-space inflates while the extra times deflate.
    Required: (a) the instantaneous states on a grid of a4 values (canonical 0, 0.5, 1, 1.5, 2;
    A = 1, i.e. x4 = a4/H) for N in {8, N_mid, N_large} and the five couplings, ground and first
    excited (KS gap, Delta-SCF, particle-hole), thermodynamics at T in {0.1, 0.3, 1} m on the
    same slices, the energy-momentum tensor and the comparison with the deflating field's
    required source (rho_req = -3H^2 (7 + A^2)/kappa, NOT the static -21 H^2/kappa); (b) the
    adiabaticity measure along the history: |d eps_n / d x4| / gap^2 (and the Landau-Zener-type
    criterion) for the HOMO-LUMO pair, computed from the slice spectra by exact differentiation
    of the rescaling or by finite differences with an error estimate; the regime where the
    instantaneous states are a valid approximation stated in numbers; (c) the non-adiabatic,
    fully time-dependent Kohn-Sham (TDDFT) problem is OPEN and is said so.
D9. Code.  studies/dirac16complex_kohn_sham: a new subcommand (e.g. `deflating`) that runs the
    slice series and the adiabaticity analysis, with its own checks (the E4.10 rescaling identity
    between slice a4,0 and its rescaled a4,0 = 0 partner to solver precision; monotone redshift of
    the 3-space levels; N conservation; EMT identities), repeat byte-identical, refined run;
    scripts/ks_reference_solver.py: the same slices for the cross-check (a subset is enough where
    the full matrix is too long: state exactly which); scripts/check_dirac16complex_kohn_sham.py:
    the deflating comparisons; exact theory additions (Wolfram + sympy): the reduced block
    operator with time-dependent a4 (the d_x4 term, the a4-dependence only through kappa(y, t)),
    the bulk Einstein tensor and required source of the Z2 extension with a4' = A.
D10. Stage 4 documents (provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.md and its student
    guide), notebooks and gate: rewritten for the deflating field (the static results become the
    a4,0 = 0 slice, labelled).
D11. Stage 5: T1 and T2 are proved for every gravitational field and hold unchanged; T3 holds on
    every instantaneous slice (the block map does not involve a4) - state and verify it for the
    slice series; the Kohn-Sham pair numerics run on the slice series; the Stage-5 documents
    are written for the deflating field.  The Stage-5 correction of the T1krein reading
    (HANDOFF.md section 0.4 C) is applied at the same time.

## 5. Documents, textbook, honesty

D12. Every document, report and textbook chapter that mentions x5, x6, x7, the extra times, the
    static member, the window or frozen extra times is updated: the extra times are "the three
    extra times x5, x6, x7, which deflate exponentially (scale factor e^{-A H x4})"; every place
    where a model departs from that (EXP-2's computed reversal, the frozen comparison of EXP-3,
    the instantaneous approximation of Stages 4/5) says so explicitly.  The textbook (chapters
    0, 4, 8, 9, 11, 13-16, 18-20 at least) and its PDF are rebuilt and re-registered.
D13. Honesty: numbers only from regenerated committed files; never force a result (EXP-2); the
    adiabatic approximation is an APPROXIMATION (status ASSUMED where used); TDDFT OPEN.
D14. Order of work: (1) this spec reviewed; (2) Stage 2 exact additions and Stage 3 redo in
    parallel with the Stage 4 exact additions and the `deflating` subcommand; (3) Stage 4
    reference cross-check and documents; (4) Stage 5 on the slice series and its documents;
    (5) the textbook update; (6) gates from fresh clones; push after every milestone.
