# fock_quartic: the energy-momentum tensor operator of dirac16complex for lambda != 0 in a finite Fock space

Question (SPEC sections 4 and 6; `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` sections 12 and 15). For
U(S) = (lambda/2) S^2, lambda != 0: does the operator form of the on-shell identity
sum_mu <:K_mu:> = <:(m + U'(S)) S:>, and with it rho = m S + U and p = S U' - U, hold as an operator
identity, only on solutions of the operator field equation, or only in expectation values for a class of
states? The theory record verified the operator statements only for lambda = 0.

Answer: it holds as an exact operator identity on every state of the model, for the solutions of the
interacting operator field equation, if and only if the potential and the energy-momentum tensor are both
Wick (normal) ordered. With any other tested ordering it fails, already in expectation values. Details are
below. Everything here is proved only for the finite model described next, not for the field on a whole slice.

## Construction (exact)

* Clifford data: the author's T16 gammas from `Revision/algebra/gammas.json`, C, B = -i C gamma^(x4). The
  checker verifies that beta = B C = -i gamma^(x4) is Hermitian with beta^2 = 1, so Psibar = Psi^dagger C =
  chi beta, S = chi beta psi and Psibar gamma^(x4) = i chi.
* Field: one good-sector plane-wave mode set with frozen coefficients (flat frame, volume V = 1):
  Psi(x) = e^{i k.x} psi(x4), psi = U a. The columns of U are 16 orthonormal eigenvectors of
  h_k = m beta + sum_a k_a alpha^a (8 with energy +E, 8 with -E), and a_j = b_j (j < 8) or d_(j-8)^dagger
  (j >= 8). Psi^dagger = chi B, where chi is the Hilbert adjoint (the record's positive realisation).
  This gives {psi_A, Psi^dagger_C} = B_AC, which is the record's canonical anticommutator with delta^7
  replaced by its projection on the mode set. U is built as (1 +- h/E)(1 +- beta) e_A / sqrt(nsq), and only
  the Gaussian-rational matrices U^dagger M U enter, so no square roots appear.
* Fock space: the CAR algebra of the 16 modes b, d, using its own exact engine with normal-ordered monomials
  and Gaussian-rational coefficients. The symbols lambda (and m) are carried as exponents. This basis is
  faithful on the 2^16-dimensional positive Fock space, so an operator is zero if and only if it vanishes on
  every state. The engine is tested against the Jordan-Wigner action on states.
* Mode sets: M0 is the rest frame k = 0 with symbolic m > 0. It is homogeneous: K_(a != x4) = 0 and S is
  x-independent. M1 has m = 3, k = (4, 0, 0, 0) along x1 and E = 5, which is the record's Wolfram example.
* Dynamics: H = :chi h psi: + U_W. The Heisenberg derivative is d4 Psi = i[H, Psi], and K_4 is computed
  from the matrices as (1/2)(Psibar gamma^(x4) d4 Psi - d4 Psibar gamma^(x4) Psi). The spatial terms are
  K_a = i k_a Psibar gamma^a Psi.
* Four orderings of the potential are tested:
  * plain: U = (lambda/2) S.S, the operator square of S = Psibar Psi.
  * nsq: (lambda/2) :S:.:S:.
  * wick: (lambda/2) :S S:, the Wick ordering of the classical S^2.
  * field: beta beta Psi^+ Psi^+ Psi Psi, with all Psi^+ to the left.
* Two definitions of the left-hand side ":sum K:":
  * N1: the Heisenberg operator minus its vacuum value.
  * N2: the Wick product of Psibar and the normal-ordered operator d4 Psi, with no contractions between the
    factors.
* Two right-hand sides:
  * R1 = :(m + U')S: = m :S: + lambda :S S:.
  * R2 = m :S: + lambda :S:^2.

## Results (report `reports/fock-quartic.json`, 21/21 PASS)

1. Control at lambda = 0 (`control_record_Fock_example`, `control_trace_identity_lam0`,
   `control_homogeneous_lam0`). The record's Fock example is reproduced exactly on M1:
   * the vacuum value of chi h psi is -40;
   * the normal-ordered energy is +5 for b_0^+|0> and for d_0^+|0>;
   * the charge is +1 and -1;
   * the expectation-value rule holds for C, -i C gamma^(x4), -i C gamma^(x1), C gamma^(x2) gamma^(x3) and
     the dense integer matrix.

   On M0 and M1, sum_mu K_mu = m S is an operator identity (including the constant), and N1 = N2 = m :S:.
   On M0, rho = m :S: and p = 0.
2. Orderings (`orderings_of_S2_*`). The four orderings differ only by one-body operators and constants:
   * field = S.S - Q exactly;
   * on M0, :S:.:S: - :SS: = N_b + N_d;
   * on M0, S.S - :SS: = 64 - 15 (N_b + N_d).
3. Which operator field equation the Heisenberg field solves (`heisenberg_field_equation_ordering`). Seven
   orderings were tested; for every W, exactly one of them matches, on both mode sets:

   | U ordering | Heisenberg field solves gamma^mu d_mu Psi = m Psi + lambda O with O = |
   | --- | --- |
   | plain | (1/2){S, Psi} |
   | nsq | (1/2){:S:, Psi} |
   | wick | :S Psi: (the Wick-ordered classical U'(S) Psi) |
   | field | S Psi |
4. Exact operator theorem for every ordering (`kinetic_sum_operator_theorem`):
   sum_mu K_mu = m S + lambda S.S - (lambda/2) Q + (U_W - (lambda/2) S.S) + c_W 1.
   So the plain operator sum K equals (m + U')S = m S + lambda S.S only up to a one-body operator. For the
   field ordering, sum K = m S + 2 U_W.
5. **Positive result** (`trace_identity_operator_identity_wick`). Take W = wick, with
   H = :chi h psi: + (lambda/2) :S S:, which is checked to equal the integrated normal-ordered energy density
   :(-sum_(a != x4) K_a + m S + U):. Define K_mu by Wick products (N2). Then
   :sum_mu K_mu: = :(m + U'(S)) S: = m :S: + lambda :S S: holds exactly as an operator identity on the whole
   Fock space, on both mode sets, with symbolic lambda (and symbolic m on M0).
6. **Failures** (`trace_identity_fails_for_every_other_combination`, `expectation_classes_M0`,
   `expectation_values_M1`). All 30 other combinations of mode set, ordering, LHS and RHS fail. In each case
   the difference is a nonzero one-body operator (sometimes plus a constant) that is linear in lambda.
   * On M0 every difference is lambda (alpha N_b + beta N_d), with alpha and beta nonzero and of the same
     sign. Its expectation value therefore vanishes only in the vacuum of the mode set.
   * The most important case is the Wick potential with N1 (vacuum subtraction): the difference is
     -lambda (8 N_b + 7 N_d). The 8 is the number of sea modes.
   * On M1 every difference is nonzero in b_0^+|0> or d_0^+|0>, and the differences also contain pair terms.
7. **Homogeneous rho and p** (M0; `homogeneous_rho_p_operator_identities_wick`,
   `homogeneous_expectation_values_are_not_U_of_expectation`, `homogeneous_p_vacuum_subtraction_fails`).
   In the Wick sense these are exact operator identities:
   * rho = :H: = m :S: + (lambda/2) :S S: = :m S + U:;
   * p3 = p_t = p8 = :K_4: - :m S + U: = (lambda/2) :S S: = :S U' - U:;
   * [H, S] = 0, so S is conserved;
   * :S: = N_b + N_d = n, and :S S: = n^2 - n.

   On occupation states, rho = m n + (lambda/2) n(n - 1) and p = (lambda/2) n(n - 1). So <:U(S):> is not
   U(<:S:>): one quantum gives p = 0, not lambda/2. With N1, p is off by -lambda (8 N_b + 7 N_d).
8. **Negative control** (`negative_control_free_dynamics`). If d4 Psi is generated by the free H while the
   right-hand side keeps U' = lambda S, the checker finds a difference of -lambda :S S: on both mode sets.
   The identity therefore depends on the interacting operator field equation; it does not hold for an
   arbitrary d4 Psi.

## What is established, and what is not

Established, exactly, in the finite model above (one frozen-coefficient good-sector mode set, flat frame,
V = 1, 16 modes, 2^16 states):

* The answer to the question. The identity holds as an operator identity on every state, for solutions of
  the operator field equation (the Heisenberg field), under one condition: the potential in H and the
  products in T are both Wick (normal) ordered.
* With that ordering, the homogeneous values rho = :m S + U: and p = :S U' - U: are operator identities.
* The identity fails for the plain, nsq and field orderings and for vacuum subtraction. In those cases it
  fails even in expectation values, except in the vacuum (k = 0).

Not established:

* The field on a whole slice (many momenta), the curved x8 dependence and its boundary term at z = pi/2,
  and the extra-time sector with its growing modes.
* Renormalisation. The one-body discrepancies of the other orderings scale with the number of sea modes,
  and in the continuum they would diverge. This is a remark; it was not computed.
* Any numerical expectation value for a physical many-fermion state.
* <:U(S):> = U(<:S:>), which is false.

## Command and run time

```text
python Revision/theory/fock_quartic/check_fock_quartic.py
```

Run from the repository root with Python 3.14.5 and sympy 1.14.0. It writes `reports/fock-quartic.json` and
exits with 0 when all checks pass. Measured on 2026-10-08 (Windows 11): 6.7 s wall clock (8.0 s on the first
run). Two runs, and a run with a different PYTHONHASHSEED, gave byte-identical reports
(sha256 4170ef3ef948902553b86dfe7c86866dc9403cfc4ca1a7a895e8468931c94aa9).
