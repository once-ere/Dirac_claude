#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_ks_theory.wls

   Revision Kohn-Sham theory for dirac16complex in the author's primordial field (Revision/SPEC.md,
   sections 1 and 7), exact derivation and verification in WolframScript.  Revision code only.
   The metric is the corrected primordial metric of 2026-10-16 (version 2; SPEC section 1, Revision/metric_warped/):
   g = diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3)), z = 6 H x0 real; every
   statement is derived for general a4(x4) and b4(x4) > 0 and every real z; the numerical history of the solver is
   a4 = A H x4, b4 = b4(0) e^{beta A H x4}, beta = 4/3, b4(0) = 1 (SPEC section 1).  (Until 2026-10-16 this verifier
   used the metric of 2026-10-14, now withdrawn.)
   Input:   Revision/algebra/gammas.json (the Revision algebra fixture in the author's order x0..x7, gamma^(xk) = T16[k])
   Package: Revision/kohn_sham/theory/KohnShamTheory.wl
   Writes, deterministically (LF, no time stamps):
     Revision/kohn_sham/reports/ks-theory-wolfram.json   every check with name, verdict, detail
     Revision/kohn_sham/ks-theory.json                   the formulas the Rust solver must implement
   Usage:  wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls
   The independent second engine is Revision/kohn_sham/theory/check_ks_theory.py (sympy).
   Exit code 0 if every check passes and both files are written, 1 otherwise.  A missing input file
   (the package or gammas.json) or an output file that cannot be written stops the run at once with a
   line "ERROR  ..." and exit code 1 (writeLF creates a missing output folder).
*)

$here = DirectoryName[$InputFileName];
$ks = ExpandFileName[FileNameJoin[{$here, ".."}]]; (* NORMALISED: a ".." left in a path can push it past the Windows limit of 260 characters (MAX_PATH) *)
$rev = ExpandFileName[FileNameJoin[{$ks, ".."}]];
$pkg = FileNameJoin[{$here, "KohnShamTheory.wl"}];
If[! FileExistsQ[$pkg], Print["ERROR  input file not found: ", $pkg]; Exit[1]];
Get[$pkg];
t0 = AbsoluteTime[];

checks = {};
addCheck[name_String, ok_, detail_String] := (
  AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS", "FAIL"], "  ", name, "  t=", Round[AbsoluteTime[] - t0, 0.1]]);
zeroQ[m_] := AllTrue[Flatten[{Simplify[m]}], # === 0 &];
num[x_, d_: 16] := ToString[NumberForm[N[x, 40], d, NumberFormat -> (If[#3 == "", #1, #1 <> "e" <> #3] &)]];

(* ---------------- A. gammas ---------------- *)
gpath = FileNameJoin[{$rev, "algebra", "gammas.json"}];
If[! FileExistsQ[gpath], Print["ERROR  input file not found: ", gpath]; Exit[1]];
{g, etaM} = KSLoadGammas[gpath];
eta = Diagonal[etaM];
id16 = IdentityMatrix[16]; id2 = IdentityMatrix[2]; z16 = ConstantArray[0, {16, 16}];
{s1, s2, s3} = KSPauli;
{g0, g1, g2, g3, g4, g5, g6, g7} = g;
addCheck["fixture_input", Length[g] == 8,
  "gammas read from Revision/algebra/gammas.json (sha256 " <> IntegerString[FileHash[gpath, "SHA256"], 16, 64] <> ")"];
addCheck["clifford_relation",
  And @@ Flatten[Table[g[[a]].g[[b]] + g[[b]].g[[a]] == 2 KroneckerDelta[a, b] eta[[a]] id16, {a, 8}, {b, 8}]] &&
  eta == {1, 1, 1, 1, -1, -1, -1, -1},
  "{gamma^a, gamma^b} = 2 eta^ab, eta = diag(+1,+1,+1,+1,-1,-1,-1,-1) in x0..x7"];
C16 = g0.g1.g2.g3; B16 = -I C16.g4; Gam = g0.g1.g2.g3.g4.g5.g6.g7;
addCheck["C_B_Gamma",
  Transpose[C16] == C16 && C16.C16 == id16 && ConjugateTranspose[B16] == B16 && B16.B16 == id16 &&
  Gam == DiagonalMatrix[Join[ConstantArray[-1, 8], ConstantArray[1, 8]]] &&
  B16.C16 == -I g4 && C16.g4 == I B16 && C16.B16.C16 == B16,
  "C = g0 g1 g2 g3 (real symmetric, C^2 = 1), B = -i C g4 (Hermitian, B^2 = 1), Gamma = diag(-I8, I8); BC = -i g4, C g4 = i B, C B C = B"];
(* ---------------- B. geometry (the corrected metric of 2026-10-16, version 2) ---------------- *)
$Assumptions = {H > 0, y < 0, Vol > 0, ell > 0, vt > 0, b0 > 0, bb0 > 0, cc > 0, AA > 0, ff > 0,
   Element[{x1, x2, x3, x4, x5, x6, x7, k, k1, k2, k3, eps, M, v, a0, lam, nn, SS, QQ, L, aa, bet}, Reals], L > 0};
zOfy = ArcSin[Exp[6 H y]];
addCheck["geometry_hidden_coordinate",
  Simplify[Cot[zOfy]^2 D[zOfy/(6 H), y]^2 == 1] && Simplify[(Sin[zOfy]^2)^(1/6) == Exp[2 H y]] &&
  KSZeroX0Q[D[Log[Sin[6 H x0]^2]/(12 H), x0] - Cot[6 H x0]],
  "y = Log[Sin[z]^2]/(12 H) = Log[|Sin z|]/(6H), z = 6 H x0 real: dy = Cot[z] dx0 for EVERY real z with Sin z Cos z != 0 (exact zero test), Cot[z]^2 dx0^2 = dy^2, (Sin[z]^2)^(1/6) = E^(2 H y); each quarter of the period of z is y in (-Infinity, 0) (the fold Cos z = 0 is y = 0, the tip Sin z -> 0 is y -> -Infinity)"];
gx0 = KSGeometryX0[a0, b0]; gyc = KSGeometryY[a0, b0];
addCheck["geometry_line_element",
  KSZeroX0Q[gx0["h"][[1]]^2 - gyc["h"][[1]]^2 Cot[6 H x0]^2] &&
  And @@ Table[KSZeroX0Q[gx0["h"][[a]] - (gyc["h"][[a]] /. y -> Log[Sin[6 H x0]^2]/(12 H))], {a, 2, 8}],
  "the y chart reproduces the corrected metric on every quarter: e^y = f dy with f = E^(-a4) b4^(1/2) (e^y dy = e^x0 dx0, e^x0 = f Cot[z] signed), e^xi = E^a4, e^x4 = 1, e^xt = f E^(H y) = f (Sin[z]^2)^(1/12): ds^2 = E^(2 a4) dx_i^2 - dx4^2 + f^2 (dy^2 - E^(2 H y) dx_t^2)"];
addCheck["geometry_sqrt_det",
  KSZeroX0Q[Det[gx0["g"]] - E^(-2 a0) b0^4 Cot[6 H x0]^2 (Sin[6 H x0]^2)^(1/2)] &&
  Simplify[Abs[Det[gyc["g"]]] == E^(-2 a0) b0^4 E^(6 H y)],
  "det g = E^(-2 a4) b4^4 Cot[z]^2 (Sin[z]^2)^(1/2) in the author's chart (every real z): sqrt|g| = E^(-a4) b4^2 |Cot z| (Sin z^2)^(1/4); y chart: sqrt|g| = E^(-a4) b4^2 E^(3 H y) = E^(3 a4) f^4 E^(3 H y)"];
geo = KSGeometryY[a4[x4], b4[x4]];
X = geo["coords"]; hv = geo["h"];
chr = KSChristoffel[geo["g"], X];
Om = KSSpinConnection[g, etaM, hv, chr, X];
addCheck["spin_connection_compatibility",
  And @@ Flatten[Table[zeroQ[D[g[[n]]/hv[[n]], X[[m]]] + Sum[chr[[n, m, l]] g[[l]]/hv[[l]], {l, 8}] +
      Om[[m]].(g[[n]]/hv[[n]]) - (g[[n]]/hv[[n]]).Om[[m]]], {m, 8}, {n, 8}]],
  "canonical spin connection (vielbein postulate), a4 = a4[x4], b4 = b4[x4]: nabla_mu gamma^nu = 0 for all 64 (mu, nu)"];
fF = Exp[-a4[x4]] Sqrt[b4[x4]];
cgF = (3/2) H/fF; vgF = b4'[x4]/b4[x4] - a4'[x4]/2;
slash = Simplify[Sum[g[[m]].Om[[m]]/hv[[m]], {m, 8}]];
addCheck["spin_connection_slash", zeroQ[slash - cgF g0 - vgF g4],
  "gamma^mu Omega_mu = (3/2) (H/f) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) exactly, f = E^(-a4) b4^(1/2) (= (3/2) H E^a4 b4^(-1/2) gamma^(x0) + ...: the field-theory record)"];
sY = Simplify[g[[1]].Om[[1]]/hv[[1]]];
sInfl = Simplify[Sum[g[[m]].Om[[m]]/hv[[m]], {m, 2, 4}]];
sDefl = Simplify[Sum[g[[m]].Om[[m]]/hv[[m]], {m, 6, 8}]];
hF = b4'[x4]/(2 b4[x4]) - a4'[x4];
addCheck["spin_connection_time_terms",
  zeroQ[sY - (1/2) hF g4] && zeroQ[sInfl - (3/2) a4'[x4] g4] && zeroQ[sDefl - (3/2) hF g4 - cgF g0] && zeroQ[Om[[5]]] && ! zeroQ[Om[[1]]],
  "per direction: the hidden direction gives (1/2) h4 gamma^(x4), the 3-space (3/2) a4' gamma^(x4), the extra times (3/2) h4 gamma^(x4) + (3/2)(H/f) gamma^(x0) (h4 = b4'/(2 b4) - a4', the rate of f): (1/2) h4 + (3/2) a4' + (3/2) h4 = b4'/b4 - a4'/2; Omega_x4 = 0, Omega_y != 0 (f depends on x4)"];
gx0t = KSGeometryX0[a4[x4], b4[x4]];
chr0 = KSChristoffel[gx0t["g"], gx0t["coords"]];
Om0 = KSSpinConnection[g, etaM, gx0t["h"], chr0, gx0t["coords"]];
slash0 = Sum[g[[m]].Om0[[m]]/gx0t["h"][[m]], {m, 8}];
addCheck["spin_connection_slash_x0_chart", And @@ (KSZeroX0Q /@ Flatten[slash0 - cgF g0 - vgF g4]),
  "in the author's chart (x0..x7), a4 = a4[x4], b4 = b4[x4]: gamma^mu Omega_mu = (3/2) H E^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) for every real z (exact zero test)"];

(* ---------------- C. ansatz ---------------- *)
chiF = Table[c[i][y, x4], {i, 16}];
kap = Exp[-a4[x4]];
phase = Exp[I (k1 x1 + k2 x2 + k3 x3)];
dirac[Psi_] := Sum[g[[m]].(D[Psi, X[[m]]] + Om[[m]].Psi)/hv[[m]], {m, 8}];
red = g0.D[chiF, y]/fF + g4.D[chiF, x4] + I kap (k1 g1 + k2 g2 + k3 g3).chiF;
fW = Exp[-(3/2) H y]; fab = Exp[a4[x4]/2]/b4[x4];
addCheck["ansatz_removes_spin_connection", zeroQ[dirac[phase fW fab chiF]/(phase fW fab) - red],
  "gamma^mu D_mu (e^{ik.x} E^(-(3/2) H y) E^(a4/2) b4^(-1) chi(y, x4)) = e^{ik.x} E^(-(3/2) H y) E^(a4/2) b4^(-1) [(1/f) g0 d_y + g4 d_x4 + i kappa k.gamma] chi, kappa = E^(-a4) (no dependence on y), f = E^(-a4) b4^(1/2): exact for time-dependent a4 and b4"];
addCheck["ansatz_without_y_factor_term_survives", zeroQ[dirac[phase fab chiF]/(phase fab) - red - cgF g0.chiF],
  "without E^(-(3/2) H y) the term (3/2)(H/f) gamma^(x0) chi survives"];
addCheck["ansatz_without_x4_factor_term_survives", zeroQ[dirac[phase fW chiF]/(phase fW) - red - vgF g4.chiF],
  "without E^(a4/2) b4^(-1) the term (b4'/b4 - a4'/2) gamma^(x4) chi survives: E^(a4/2) b4^(-1) E^(-(3/2) H y) is the half-density of sqrt|g| = E^(-a4) b4^2 E^(3 H y)"];
addCheck["ansatz_norm", Simplify[E^(-a4[x4]) b4[x4]^2 Exp[3 H y] (fW fab)^2 == 1, b4[x4] > 0],
  "sqrt|g| (E^(-(3/2) H y) E^(a4/2) b4^(-1))^2 = 1 in the y chart: int sqrt|g| Psi^dag Psi over the hidden direction = int chi^dag chi dy for every a4 and b4 (the Hilbert norm of the reduced problem)"];
addCheck["hamiltonian_16_hermitian",
  Transpose[g4.g0] == g4.g0 && ConjugateTranspose[-g4.g1] == -g4.g1 && ConjugateTranspose[-I g4] == -I g4,
  "i d_x4 chi = h chi with h = (i/f) g4 g0 d_y - kappa k_j g4 g^j + M(-i g4) + v: g4 g0 real symmetric, g4 g^j and -i g4 Hermitian"];

(* ---------------- D. blocks ---------------- *)
J = g0.g1.g4; K1 = g2.g3; K2 = g5.g6;
A0 = g0; A1 = g0.g1; A4 = g0.g4;
comm[a_, b_] := a.b - b.a;
addCheck["blocks_commuting_set",
  And @@ Flatten[Table[comm[P, Q] == z16, {P, {J, K1, K2}}, {Q, {A0, A1, A4, B16, C16, J, K1, K2}}]] &&
  J.J == id16 && K1.K1 == -id16 && K2.K2 == -id16,
  "J = g0 g1 g4, K1 = g2 g3, K2 = g5 g6 commute with each other and with g0, g0 g1, g0 g4, B, C"];
bb = KSBlockBasis[g];
labels = bb["labels"]; U = bb["U"]; V = U/(2 Sqrt[2]);
addCheck["blocks_basis_unitary",
  Simplify[ConjugateTranspose[V].V] == id16 && SubsetQ[{0, 1, -1, I, -I}, Union[Flatten[U]]],
  "V = U/(2 Sqrt[2]) unitary, U entries in {0, +-1, +-I}; seeds (0-based) " <> ToString[bb["seeds"]]];
expect = {
  {"gamma^(x0)", A0, s3 &}, {"gamma^(x0)gamma^(x1)", A1, -I s2 &}, {"gamma^(x0)gamma^(x4)", A4, #1 s1 &},
  {"B", B16, #1 #2 id2 &}, {"C", C16, #2 s2 &}, {"BC", B16.C16, #1 s2 &}, {"gamma^(x4)gamma^(x1)", g4.g1, -#1 s3 &},
  {"B gamma^(x0)", B16.g0, #1 #2 s3 &}, {"J", J, #1 id2 &}, {"K1", K1, I #2 id2 &}, {"K2", K2, I #3 id2 &}};
blockDiagQ[Xm_] := Module[{Y = Simplify[ConjugateTranspose[V].Xm.V]},
  And @@ Flatten[Table[If[a != b, Y[[2 a - 1 ;; 2 a, 2 b - 1 ;; 2 b]] == ConstantArray[0, {2, 2}], True], {a, 8}, {b, 8}]]];
okForms = And @@ Table[blockDiagQ[e[[2]]] && And @@ MapThread[#1 == e[[3]] @@ #2 &, {KSBlock[V, e[[2]]], labels}], {e, expect}];
addCheck["blocks_forms", okForms,
  "block (j,s2,s3): g0 = sigma3, g0 g1 = -i sigma2, g0 g4 = j sigma1, B = j s2, C = s2 sigma2, BC = j sigma2, g4 g1 = -j sigma3, B g0 = j s2 sigma3, J = j, K1 = i s2, K2 = i s3"];
YG = Simplify[ConjugateTranspose[V].Gam.V];
gamPairs = Select[Tuples[Range[8], 2], YG[[2 #[[1]] - 1 ;; 2 #[[1]], 2 #[[2]] - 1 ;; 2 #[[2]]]] =!= ConstantArray[0, {2, 2}] &];
addCheck["blocks_relation_to_Gamma",
  gamPairs == {{1, 5}, {2, 6}, {3, 7}, {4, 8}, {5, 1}, {6, 2}, {7, 3}, {8, 4}} &&
  And @@ Table[YG[[2 p[[1]] - 1 ;; 2 p[[1]], 2 p[[2]] - 1 ;; 2 p[[2]]]] == labels[[p[[1]], 2]] s2, {p, gamPairs}] &&
  Gam.J == -J.Gam && comm[Gam, K1] == z16 && comm[Gam, K2] == z16,
  "Gamma anticommutes with J, commutes with K1, K2: block (j,s2,s3) <-> (-j,s2,s3) with 2x2 entry s2 sigma2"];
okH = And @@ Flatten[Table[With[{Vb = V[[All, 2 b - 1 ;; 2 b]], j = labels[[b, 1]]},
    {Simplify[ConjugateTranspose[Vb].(I g4.g0).Vb] == -I j s1, Simplify[ConjugateTranspose[Vb].(-g4.g1).Vb] == j s3,
     Simplify[ConjugateTranspose[Vb].(-I g4).Vb] == j s2}], {b, 8}]];
addCheck["block_hamiltonian", okH,
  "h_j = j[-(i/f) sigma1 d_y + M sigma2 + kappa k sigma3] + v in every block of type j (k along x1; kappa = E^(-a4), f = E^(-a4) b4^(1/2))"];
Nm[j_, Mm_, kk_, e_, vv_, kp_] := Mm s3 - kp kk s2 + I j (e - vv) s1;
hj[j_, Mm_, kk_, vv_, kp_] := j (Mm s2 + kp kk s3) + vv id2;
addCheck["block_ode_equivalent",
  And @@ Table[Simplify[-I j s1.Nm[j, M, k, eps, v, kp] == eps id2 - hj[j, M, k, v, kp]], {j, {1, -1}}],
  "h_j chi = eps chi <=> chi' = f N chi, N = M sigma3 - kappa k sigma2 + i j (eps - v) sigma1 (the factor f multiplies both sides)"];
addCheck["block_type_relation",
  Simplify[hj[-1, M, k, 0, kp] == -hj[1, M, k, 0, kp]] && Simplify[s3.hj[1, M, k, 0, kp].s3 == hj[-1, M, -k, 0, kp]] &&
  s3.(-I s1).s3 == I s1,
  "h_{-1} - v = -(h_{+1} - v); sigma3 h_j(k) sigma3 = h_{-j}(-k) (also for the derivative term): chi_{-j,-k} = sigma3 chi_{j,k}"];
addCheck["block_Gamma_map",
  Simplify[s2.hj[1, M, k, 0, kp].s2 == hj[-1, -M, k, 0, kp]] && s2.(-I s1).s2 == I s1,
  "sigma2 h_j(M, k) sigma2 = h_{-j}(-M, k): the block form of Gamma maps (j, M) -> (-j, -M) at the same k, eps; it swaps the brane parities chi2(0) = 0 <-> chi1(0) = 0"];
R12 = Cos[th/2] id16 + Sin[th/2] g1.g2;
addCheck["rotation_invariance",
  zeroQ[R12.(k g1).Inverse[R12] - k (Cos[th] g1 - Sin[th] g2)] && And @@ (comm[R12, #] == z16 & /@ {g0, g4, B16, C16}),
  "the spinor rotation Cos[th/2] + Sin[th/2] g1 g2 commutes with g0, g4, B, C and rotates k.gamma: spectra depend on |k|"];

(* ---------------- E. exchange ---------------- *)
hp = M (-I g4) - (p1 g4.g1 + p2 g4.g2 + p3 g4.g3 + p0 g4.g0);
addCheck["gas_mode_projector", Simplify[hp.hp == (M^2 + p1^2 + p2^2 + p3^2 + p0^2) id16],
  "flat good-sector modes: h_p^2 = (M^2 + p^2) 1, eps = +-E each 8-fold; G_p = (1 + h_p/E)/2"];
Gp = (id16 + hp/EE)/2;
rhoAng = Integrate[(Gp.B16 /. {p1 -> pr Sin[th] Cos[ph], p2 -> pr Sin[th] Sin[ph], p3 -> pr Cos[th], p0 -> 0}) Sin[th],
    {th, 0, Pi}, {ph, 0, 2 Pi}]/(4 Pi);
addCheck["gas_angular_average", zeroQ[rhoAng - (B16 + (M/EE) C16)/2],
  "explicit S^2 average of the 8-mode one-body matrix G_p B: (B + (M/E) C)/2 (linear terms vanish; only p -> -p symmetry used)"];
rho = (nn B16 + SS C16)/16;
addCheck["gas_densities", Simplify[Tr[B16.rho]] == nn && Simplify[Tr[C16.rho]] == SS,
  "rho = sum_occ f u u^dagger B: n = Tr(B rho), S = Tr(C rho); any p -> -p symmetric occupation (any T) gives rho = (nB + SC)/16"];
ex = Factor[-(lam/2) Tr[C16.rho.C16.rho]];
addCheck["exchange_uniform_gas", Simplify[ex == -(lam/32) (nn^2 + SS^2)],
  "Hartree-Fock: <:S^2:> = (Tr C rho)^2 - Tr(C rho C rho); e_x = -(lambda/2) Tr(C rho C rho) = " <> ToString[ex, InputForm] <> " (exact, every temperature)"];
eint = (lam/2) SS^2 + ex;
addCheck["ks_potentials", Simplify[D[eint, SS] == (15/16) lam SS] && Simplify[D[eint, nn] == -lam nn/16],
  "e_int = (15/32) lambda S^2 - (1/32) lambda n^2; M_eff = m + (15/16) lambda S; v_v = -lambda n/16"];
addCheck["ks_onshell_lagrangian", Simplify[SS D[eint, SS] + nn D[eint, nn] - eint == eint],
  "on shell <L>/sqrt|g| = M_eff S + v_v n - m S - e_int = e_int"];
(* slab: exact Fock exchange, octahedral-group average (method independent of the Python commutant projection) *)
Dm = (d0 id2 + d1 s1 + d2 s2 + d3 s3)/2;
Gsl = Sum[With[{Vb = V[[All, 2 b - 1 ;; 2 b]]}, Vb.If[labels[[b, 1]] == 1, Dm, s3.Dm.s3].ConjugateTranspose[Vb]], {b, 8}];
gens = {(id16 + g2.g3)/Sqrt[2], (id16 + g3.g1)/Sqrt[2]};
grp = FixedPoint[Union[Join[#, Flatten[Table[Simplify[a.b], {a, #}, {b, gens}], 1]]] &, {id16}];
Gav = Simplify[Total[(#.Gsl.Inverse[#]) & /@ grp]/Length[grp]];
rs = Gav.B16;
{nS, sS, qS, yS} = Simplify[{Tr[B16.rs], Tr[C16.rs], Tr[B16.g0.rs], Tr[B16.(-I C16.g0).rs]}];
exS = Expand[-(lam/2) Tr[C16.rs.C16.rs]];
addCheck["exchange_slab_exact_fock",
  Length[grp] == 48 && {nS, sS, qS} == {8 d0, 8 d2, 8 d3} && Simplify[exS + (lam/32) (nS^2 + sS^2 - qS^2 - 64 d1^2)] === 0,
  "closed-shell level (4 blocks of type +1 with D, 4 of type -1 with sigma3 D sigma3), averaged over the 48-element spinor octahedral group (" <>
  "End(16) carries spin 0 and 1 only, so this equals the full SO(3) average): n = 8 d0, S = 8 d2, Q = <Psi^dag B g0 Psi> = 8 d3; " <>
  "exact local Fock exchange -(lambda/32)(n^2 + S^2 - Q^2 - Y^2), Y = 8 d1 (y-current, 0 for eigen-orbitals)"];

(* ---------------- F. boundary conditions ---------------- *)
addCheck["bc_fold_same_equation_on_both_halves",
  Simplify[Sin[Pi - zz] == Sin[zz]] && Simplify[Cot[Pi - zz] == -Cot[zz]] &&
  Simplify[Log[Sin[Pi - zz]^2] == Log[Sin[zz]^2]] && Simplify[D[Log[Sin[zz]^2]/2, zz] == Cot[zz]] &&
  zeroQ[D[slash, y]],
  "the fold Cos z = 0 (z = Pi/2, y = 0) joins the two halves z < Pi/2 and z > Pi/2 of a cell: z -> Pi - z keeps y = Log[|Sin z|]/(6H) and flips Cot z, so e^x0 dx0 = f Cot z dx0 = f dy on both halves; gamma^mu Omega_mu is free of x0 (and of y): the reduced equation in y is the same on both halves, so a spinor that is continuous across the fold has the same chi(y) on both halves (one first-order equation, one value at y = 0)"];
cur[ch_] := Conjugate[ch].s1.ch;
addCheck["bc_fold_conditions",
  Simplify[ComplexExpand[cur[{ca + I cb, 0}]]] == 0 && Simplify[ComplexExpand[cur[{0, ca + I cb}]]] == 0 &&
  Simplify[ComplexExpand[cur[{ca + I cb, cc2 + I cd}]]] =!= 0,
  "on the doubled cell the boundary form at the fold is the sum of the two halves, 2 (-i j/f) phi^dag sigma1 chi(0), because the y direction points to the fold on both halves: self-adjointness needs chi(0) in a line with chi^dag sigma1 chi = 0, i.e. (1 - Q(theta)) chi(0) = 0, Q = Cos[theta] sigma3 + Sin[theta] sigma2; theta = 0: chi2(0) = 0 (even), theta = Pi: chi1(0) = 0 (odd); a general chi(0) carries a current into the fold. ASSUMED (the convention of the record, kept from 2026-10-14): both conditions are solved and filled together, each orbital normalised on one half with the weight w = 1/2"];
hop[j_, w_] := j (-I s1.D[w, y]/ff + Mf[y] s2.w + Exp[-a0] k s3.w) + vf[y] w;
phiV = {ph1[y] + I ph2[y], ph3[y] + I ph4[y]}; chV = {f1[y] + I f2[y], f3[y] + I f4[y]};
okBT = And @@ Table[Simplify[ComplexExpand[Conjugate[phiV].hop[j, chV] - Conjugate[hop[j, phiV]].chV -
        D[-I j Conjugate[phiV].s1.chV/ff, y]]] === 0, {j, {1, -1}}];
addCheck["bc_self_adjoint_boundary_term", okBT,
  "phi^dag h_j chi - (h_j phi)^dag chi = d/dy[-(i j/f) phi^dag sigma1 chi]: h_j self-adjoint with current-killing ends (f > 0 constant in y)"];
Qt = Cos[tq] s3 + Sin[tq] s2;
addCheck["bc_tip_family", Simplify[Qt.Qt] == id2 && Simplify[Qt.s1 + s1.Qt] == ConstantArray[0, {2, 2}],
  "tip: (1 - Q(theta)) chi(-L) = 0, Q = Cos[theta] sigma3 + Sin[theta] sigma2, Q^2 = 1, {Q, sigma1} = 0; canonical theta = 0: chi2(-L) = 0"];
Nm[j_, Mm_, kk_, e_, vv_, kp_] := Mm s3 - kp kk s2 + I j (e - vv) s1;
addCheck["bc_current_conserved_along_y",
  And @@ Table[Simplify[ComplexExpand[ConjugateTranspose[Nm[j, M, k, eps, v, kp]]].s1 + s1.Nm[j, M, k, eps, v, kp]] ==
      ConstantArray[0, {2, 2}], {j, {1, -1}}],
  "chi' = f N chi: chi^dag sigma1 chi is constant in y on solutions (zero for eigen-orbitals)"];
(* exact k = 0 spectra: chi' = f N chi *)
okK0 = Module[{bn, an, en = Sqrt[M^2 + (n Pi/(ff L))^2]},
  bn = Sin[n Pi y/L]; an = (D[bn, y]/ff + M bn)/(j en);
  And @@ Table[Simplify[(D[an, y] - ff (M an - j en bn)) /. j -> jv] === 0 && Simplify[(D[bn, y] - ff (j en an - M bn)) /. j -> jv] === 0, {jv, {1, -1}}] &&
  Simplify[(bn /. y -> -L) == 0, Element[n, Integers]] &&
  Simplify[D[Exp[ff M y], y] == ff M Exp[ff M y]]];
okOdd = Module[{ao = Sin[pp ff y], eo = Sqrt[M^2 + pp^2], bo},
  bo = (M ao - D[ao, y]/ff)/eo; Simplify[D[bo, y] - ff (eo ao - M bo) == 0] &&
  Simplify[eo (bo /. y -> -L) == -M Sin[pp ff L] - pp Cos[pp ff L]]];
addCheck["bc_exact_k0_spectra", okK0 && okOdd,
  "k = 0, constant M, v = 0, theta = 0 (chi' = f N chi): even: zero mode chi = (E^(f M y), 0) and eps = +-Sqrt[M^2 + (n Pi/(f L))^2]; odd: eps^2 = M^2 + p^2 with Tan[p f L] = -p/M (the proper hidden length is f L)"];
addCheck["bc_tip_asymptotics",
  And @@ Table[Simplify[Nm[j, M, k, eps, v, kp].Nm[j, M, k, eps, v, kp] == (M^2 + kp^2 k^2 - (eps - v)^2) id2], {j, {1, -1}}],
  "N^2 = (M^2 + kappa^2 k^2 - (eps - v)^2) 1 (anticommuting Pauli terms): for constant M, v the branches are E^(+- f lambda y), lambda = Sqrt[M^2 + kappa^2 k^2 - (eps - v)^2], kappa = E^(-a4) constant: unlike the metric of 2026-10-14 (kappa = E^(-H y - a4) grew toward the tip) nothing suppresses an orbital toward the tip; the levels of the extended orbitals depend on the cut-off L like a box of proper length f L"];

(* ---------------- G. rescaling ---------------- *)
hscal[j_, aa_, f_, kk_, w_] := j (-I s1.D[w, y]/f + M s2.w + Exp[-aa] kk s3.w);
hY[j_, kk_, w_] := j (-I s1.D[w, Y] + M s2.w + kk s3.w);
okOp = And @@ Table[Simplify[(hscal[j, aa, ff, k, {wa[y], wb[y]}] /. y -> Y/ff) == hY[j, k Exp[-aa], {wa[Y/ff], wb[Y/ff]}]], {j, {1, -1}}];
Pslice[aa_, b_, HH_, l_, w_, yy_] := Exp[-3 HH yy] Exp[aa]/(l^3 w b^2);
okDens = Simplify[Pslice[aa, b0, H, ell, vt, y] == Pslice[0, 1, H/ff, ell Exp[aa], vt Exp[-3 aa] b0^(3/2), ff y]/ff /. ff -> Exp[-aa] Sqrt[b0]];
okHist = Simplify[(Exp[-aa] Sqrt[bb0 Exp[bet aa]] /. {bb0 -> 1, bet -> 4/3}) == Exp[-aa/3]];
addCheck["rescaling_identity", okOp && okDens && okHist,
  "the slice problem KS(a4,0, b4,0; H, L, Delta k, v_t, lambda) is the slice a4 = 0, b4 = 1 of KS(0, 1; H/f0, f0 L, Delta k E^(-a4,0), v_t E^(-3 a4,0) b4,0^(3/2), lambda) in the proper hidden coordinate Y = f0 y (f0 = E^(-a4,0) b4,0^(1/2)): h_j = j[-(i/f0) sigma1 d_y + M sigma2 + E^(-a4,0) k sigma3] = j[-i sigma1 d_Y + M sigma2 + (k E^(-a4,0)) sigma3], E^(-3 H y) = E^(-3 (H/f0) Y), chi_Y = chi/Sqrt[f0] and the proper density factors agree; on the history b4 = E^((4/3) a4) (b4(0) = 1): f0 = E^(-a4,0/3)"];
addCheck["ks_coupling_volume_scaling",
  Module[{eV},
    eV[l_, VV_] := VV ((15/32) l (SS/VV)^2 - (1/32) l (nn/VV)^2);
    Simplify[eV[cc lam, cc Vol] == eV[lam, Vol]] && Simplify[(15/16) cc lam SS/(cc Vol) == (15/16) lam SS/Vol] &&
    Simplify[-cc lam nn/(16 cc Vol) == -lam nn/(16 Vol)]],
  "with every density = (orbital sum)/Vol: M_eff - m = (15/16) lambda S, v_v = -lambda n/16 and the interaction energy Vol e_int are invariant under (lambda, Vol) -> (c lambda, c Vol): a Kohn-Sham state depends on the coupling and the cell volume only through lambda/Vol"];
Module[{bsl = bb0 Exp[bet aa], Pp, Ps, lamh = lam bb0^(-2)},
  Pp = Exp[-3 H y] Exp[aa]/(ell^3 vt bsl^2);
  Ps = Exp[-3 H y]/(ell^3 vt Exp[(2 bet - 1) aa]);
  addCheck["history_solver_units",
    Simplify[lam Pp == lamh Ps] && Simplify[Pp == bb0^(-2) Ps] &&
    Simplify[(lamh Ps) == (lamh Exp[-(2 bet - 1) aa]) Exp[-3 H y]/(ell^3 vt)] &&
    Simplify[((2 bet - 1) /. bet -> 4/3) == 5/3] && Simplify[(Exp[-aa] Sqrt[bsl] /. bet -> 4/3) == Sqrt[bb0] Exp[-aa/3]],
    "on the history b4 = b4(0) E^(beta a4) the proper density factor is P = E^(-3 H y) E^(a4,0)/(ell^3 v_t b4,0^2) = b4(0)^(-2) E^(-3 H y)/Vol_7(a4,0), Vol_7 = ell^3 v_t E^((2 beta - 1) a4,0) (beta = 4/3: E^((5/3) a4,0)); the solver uses lambda_hat = lambda b4(0)^(-2) and densities per Vol_7 (the proper densities times b4(0)^2), so lambda n_proper = lambda_hat n_solver; unlike the metric of 2026-10-14, b4(0) also enters h through f0 = b4(0)^(1/2) E^((beta/2 - 1) a4,0): the record uses b4(0) = 1 (SPEC section 1), f0 = E^(-a4,0/3)"]];

(* ---------------- H. EMT (16 components, ComplexExpand with real symbols; b4 = E^(2 q)) ---------------- *)
emtOK = True; emtDet = {};
hvE = Simplify[hv /. b4 -> (Exp[2 q[#]] &)] /. Power[Power[E, 2 q[x4]], 1/2] -> Power[E, q[x4]];
OmE = Simplify[Om /. b4 -> (Exp[2 q[#]] &)] /. Power[Power[E, 2 q[x4]], 1/2] -> Power[E, q[x4]];
fE = Exp[-a4[x4] + q[x4]];
Do[
  Module[{j = labels[[b, 1]], Vb = V[[All, 2 b - 1 ;; 2 b]], chi2, u, BC, Kd, Ko, sub, nc, sc, tc, ccb, P, r1, r4, ry, r22, r55, r4y,
     Nn, dch},
    chi2 = {f1[y] + I f2[y], f3[y] + I f4[y]};
    u = Exp[-I eps x4 + I k x1] Exp[-(3/2) H y] Exp[a4[x4]/2] Exp[-2 q[x4]] Vb.chi2/Sqrt[Vol];
    BC = B16.C16;
    Kd[mu_] := Module[{gm = g[[mu]]/hvE[[mu]], du = D[u, X[[mu]]]},
      Simplify[ComplexExpand[(Conjugate[u].BC.gm.(du + OmE[[mu]].u) - Conjugate[du].BC.gm.u + Conjugate[u].BC.OmE[[mu]].gm.u)/2]]];
    Ko[mu_, nu_] := Module[{gl, Dm2, dm2},
      gl[m_] := eta[[m]] hvE[[m]] g[[m]]; Dm2[m_] := D[u, X[[m]]] + OmE[[m]].u; dm2[m_] := D[u, X[[m]]];
      Simplify[ComplexExpand[Sum[Conjugate[u].BC.gl[pr[[1]]].Dm2[pr[[2]]] - Conjugate[dm2[pr[[2]]]].BC.gl[pr[[1]]].u +
           Conjugate[u].BC.OmE[[pr[[2]]]].gl[pr[[1]]].u, {pr, {{mu, nu}, {nu, mu}}}]/4]]];
    Nn = M s3 - kap k s2 + I j (eps - v) s1;
    dch = ComplexExpand[fE Nn.chi2];
    sub = {f1'[y] -> ComplexExpand[Re[dch[[1]]]], f2'[y] -> ComplexExpand[Im[dch[[1]]]],
           f3'[y] -> ComplexExpand[Re[dch[[2]]]], f4'[y] -> ComplexExpand[Im[dch[[2]]]]};
    nc = ComplexExpand[Conjugate[chi2].chi2]; sc = ComplexExpand[Conjugate[chi2].(j s2).chi2];
    tc = ComplexExpand[Conjugate[chi2].(j s3).chi2]; ccb = ComplexExpand[Conjugate[chi2].(j s1).chi2];
    P = Exp[-3 H y + a4[x4] - 4 q[x4]]/Vol;
    r1 = Simplify[-Kd[2] - P kap k tc];
    r4 = Simplify[Kd[5] - P eps nc];
    r22 = Simplify[Kd[3]]; r55 = Simplify[Kd[6]];
    ry = Simplify[-(Kd[1] /. sub) - P ((eps - v) nc - M sc - kap k tc)];
    r4y = Simplify[(Ko[5, 1] /. sub) - fE P (eps - v/2) ccb];
    emtOK = emtOK && r1 === 0 && r4 === 0 && r22 === 0 && r55 === 0 && ry === 0 && r4y === 0;
    AppendTo[emtDet, "block " <> ToString[b - 1] <> ": " <> If[{r1, r4, r22, r55, ry, r4y} === {0, 0, 0, 0, 0, 0}, "all residuals 0",
      "residuals " <> ToString[{r1, r4, r22, r55, ry, r4y}, InputForm]]]],
  {b, {1, 6}}];
addCheck["emt_orbital_components", emtOK,
  "per orbital Psi = e^{-i eps x4 + i k x1} E^(-(3/2) H y) E^(a4/2) b4^(-1) V_beta chi/sqrt(ell^3 v_t) (expectation rule, a4 = a4[x4] and b4 = b4[x4] = E^(2 q[x4]) general; the spin connection drops out of the diagonal): -K^x1_x1 = P kappa k chi^dag j sigma3 chi, K^x4_x4 = P eps |chi|^2, K^x2_x2 = K^x5_x5 = 0, -K^y_y = P[(eps - v)|chi|^2 - M chi^dag j sigma2 chi - kappa k chi^dag j sigma3 chi], K_x4y = f P (eps - v/2) chi^dag j sigma1 chi (= 0 for eigen-orbitals), P = E^(-3 H y) E^(a4) b4^(-2)/(ell^3 v_t) (per proper 7-volume), kappa = E^(-a4), f = E^(-a4) b4^(1/2); " <>
  StringRiffle[emtDet, "; "]];
addCheck["emt_trace_identity", Simplify[(-kap k tt) + eps no + (M so + kap k tt - (eps - v) no) == M so + v no],
  "sum of the diagonal K = M_eff s + v_v n (on-shell trace); T^mu_nu = -<K^mu_nu> + delta^mu_nu e_int"];
Module[{chi2 = {f1[y] + I f2[y], f3[y] + I f4[y]}, Nn, dch, sub, nc, sc, tc, p0c},
  Nn = Mf[y] s3 - kap k s2 + I (eps - vf[y]) s1;
  dch = ComplexExpand[ff Nn.chi2];
  sub = {f1'[y] -> ComplexExpand[Re[dch[[1]]]], f2'[y] -> ComplexExpand[Im[dch[[1]]]],
         f3'[y] -> ComplexExpand[Re[dch[[2]]]], f4'[y] -> ComplexExpand[Im[dch[[2]]]]};
  nc = ComplexExpand[Conjugate[chi2].chi2]; sc = ComplexExpand[Conjugate[chi2].s2.chi2]; tc = ComplexExpand[Conjugate[chi2].s3.chi2];
  p0c = (eps - vf[y]) nc - Mf[y] sc - kap k tc;
  addCheck["emt_y_conservation_orbital",
    Simplify[(D[p0c, y] /. sub) - (-vf'[y] nc - Mf'[y] sc)] === 0,
    "one orbital (j = 1) in external M(y), v(y), chi' = f N chi: d/dy[(eps - v) n_c - M s_c - kappa k t_c] = -v' n_c - M' s_c (kappa is constant in y)"]];
Tmix[r_, q3_, qt_, q0_] := DiagonalMatrix[{q0, q3, q3, q3, -r, qt, qt, qt}];
divT[T_, nu_] := Sum[D[T[[m, nu]], X[[m]]], {m, 8}] + Sum[chr[[m, m, l]] T[[l, nu]], {m, 8}, {l, 8}] -
   Sum[chr[[l, m, nu]] T[[m, l]], {m, 8}, {l, 8}];
Tf = Tmix[rh[y, x4], p3f[y, x4], ptf[y, x4], p0f[y, x4]];
eS = (15/32) lam Sf[y]^2 - lam nf[y]^2/32;
addCheck["emt_y_conservation_selfconsistent",
  Simplify[divT[Tf, 1] - (D[p0f[y, x4], y] + 3 H p0f[y, x4] - 3 H ptf[y, x4])] === 0 &&
  Simplify[-D[(15/16) lam Sf[y], y] Sf[y] - D[-lam nf[y]/16, y] nf[y] + D[eS, y]] === 0,
  "nabla_mu T^mu_y = p0' + 3H (p0 - p_t) (p3 does not enter: 3-space has no warp along y); the force terms of the orbital identity cancel against e_int' for the self-consistent M_eff, v_v, so every self-consistent state has p0' = -3H (p0 - e_int) = -3H (p0 - p_t)"];
addCheck["emt_x4_component",
  Simplify[divT[Tf, 5] - (-D[rh[y, x4], x4] - 3 a4'[x4] (rh[y, x4] + p3f[y, x4]) - 3 hF (rh[y, x4] + ptf[y, x4]) - hF (rh[y, x4] + p0f[y, x4]))] === 0,
  "nabla_mu T^mu_x4 = -d_x4 rho - 3 a4' (rho + p3) - 3 h4 (rho + p_t) - h4 (rho + p0), h4 = b4'/(2 b4) - a4' (the field-theory and a4 records)"];
Module[{rr = rh[y, x4], dE, hist},
  dE = D[E^(-a4[x4]) b4[x4]^2 rr, x4] /. Derivative[0, 1][rh][y, x4] -> (-3 a4'[x4] (rr + p3f[y, x4]) - 3 hF (rr + ptf[y, x4]) - hF (rr + p0f[y, x4]));
  hist = {a4 -> (AA H # &), b4 -> (bb0 Exp[bet AA H #] &)};
  addCheck["emt_energy_change_history",
    Simplify[dE - E^(-a4[x4]) b4[x4]^2 (-3 a4'[x4] p3f[y, x4] - 3 hF ptf[y, x4] - hF p0f[y, x4]), b4[x4] > 0] === 0 &&
    Simplify[(dE /. hist)/(AA H) - (E^(-AA H x4) (bb0 Exp[bet AA H x4])^2) (-3 p3f[y, x4] - 3 (bet/2 - 1) ptf[y, x4] - (bet/2 - 1) p0f[y, x4])] === 0,
    "with sqrt|g| = E^(-a4) b4^2 E^(3 H y) and the conservation law: d_x4 (E^(-a4) b4^2 rho) = E^(-a4) b4^2 (-3 a4' p3 - 3 h4 p_t - h4 p0) (+ the y-flux, zero for eigen-orbitals); on the history a4 = A H x4, b4 = b4(0) E^(beta A H x4): dE/da4 = -3 P3 - 3 (beta/2 - 1) P_t - (beta/2 - 1) P0, P = 2 Vol_7(a4,0) int E^(3 H y) p dy, the solver check (beta = 4/3: -3 P3 + P_t + P0/3)"]];
Module[{fa = Sqrt[bb0] Exp[(bet/2 - 1) aa], hA, w = {wa[y], wb[y]}},
  hA[j_] := j (-I s1.D[w, y]/fa + M s2.w + Exp[-aa] k s3.w) + v w;
  addCheck["adiabatic_hellmann_feynman",
    And @@ Table[Simplify[D[hA[j], aa] - (-j Exp[-aa] k s3.w + (1 - bet/2) j (-I s1.D[w, y]/fa))] === {0, 0}, {j, {1, -1}}],
    "along the history (b4 = b4(0) E^(beta a4), f = b4(0)^(1/2) E^((beta/2 - 1) a4)) with frozen potentials: d_a h_j = -j kappa k sigma3 + (1 - beta/2) j (-(i/f) sigma1 d_y) (beta = 4/3: + (1/3) times the kinetic term); d eps_n/da = <n| d_a h_j |n> (Hellmann-Feynman)"]];
Module[{Hx = 2 {{Cos[al], Sin[al]}, {Sin[al], -Cos[al]}} + id2, va, vb},
  va = {Cos[al/2], Sin[al/2]}; vb = {-Sin[al/2], Cos[al/2]};
  addCheck["adiabatic_offdiagonal_identity",
    Simplify[Hx.va == 3 va] && Simplify[Hx.vb == -vb] && Simplify[va.D[Hx, al].vb == (-1 - 3) va.D[vb, al]],
    "<n| d_a h |m> = (eps_m - eps_n) <n| d_a m> (explicit family); Q_nm = A H |<n| d_a h_KS |m>|/(eps_n - eps_m)^2 along the history a4 = A H x4, b4 = b4(0) E^(beta A H x4), a PRESCRIBED BACKGROUND (test field without back-reaction, not a solution of the a4 and b4 equations with the Kohn-Sham source)"]];

(* brane-band slope: first-order perturbation of the even zero mode, and NDSolve shooting *)
okCsym = Module[{z0 = {Exp[ff M y], 0}},
  Simplify[Integrate[z0.(s3.z0), {y, -L, 0}]/Integrate[z0.z0, {y, -L, 0}] == 1]];
shootB[e_?NumericQ, kk_?NumericQ, a_?NumericQ, f_?NumericQ] := Module[{sol, ee = SetPrecision[e, 30]},
  sol = NDSolveValue[{aF'[yy] == f (aF[yy] - (Exp[-a] kk + ee) bF[yy]), bF'[yy] == f ((ee - Exp[-a] kk) aF[yy] - bF[yy]),
      aF[0] == 1, bF[0] == 0}, bF[-3], {yy, -3, 0}, WorkingPrecision -> 25, PrecisionGoal -> 18, AccuracyGoal -> 20,
      MaxSteps -> 10^6];
  sol];
zm[kk_, a_, f_] := e /. FindRoot[shootB[e, kk, a, f], {e, SetPrecision[kk Exp[-a], 25]}, WorkingPrecision -> 25, AccuracyGoal -> 20, PrecisionGoal -> 18];
slopeNum[a_, f_] := Module[{s2k, s1k},
  s2k = (zm[2*^-3, a, f] - zm[-2*^-3, a, f])/(4*^-3); s1k = (zm[1*^-3, a, f] - zm[-1*^-3, a, f])/(2*^-3);
  (4 s1k - s2k)/3];
sl0 = slopeNum[0, 1]; sl5 = slopeNum[1/2, Exp[-1/6]];
addCheck["brane_band_slope", okCsym && Abs[sl0 - 1] < 10^-8 && Abs[sl5 - Exp[-1/2]] < 10^-8,
  "d eps/dk at k = 0 = j c with c = E^(-a4,0) exactly (first-order perturbation of the even zero mode (E^(f M y), 0): <sigma3> = 1; kappa does not depend on y), for every M, L, f; NDSolve shooting (M = 1, L = 3, WorkingPrecision 25, k = +-1e-3, +-2e-3, Richardson): " <>
  num[sl0, 12] <> " (a4,0 = 0, f = 1), " <> num[sl5, 12] <> " (a4,0 = 1/2, f = E^(-1/6) (the history); exact E^(-1/2) = " <> num[Exp[-1/2], 12] <> ")"];

(* ---------------- ks-theory.json ---------------- *)
jsonTheory = <|
  "description" -> "Revision Kohn-Sham theory for dirac16complex in the corrected primordial metric of 2026-10-16 (version 2; SPEC sections 1, 7): the exact reduction, functional, boundary conditions, rescaling identity, energy-momentum tensor, the history and the adiabaticity measure, i.e. the formulas the Rust solver Revision/kohn_sham/solver must implement, for general a4(x4), b4(x4) > 0 and every real z. Every statement here is checked in Revision/kohn_sham/reports/ks-theory-wolfram.json and independently in ks-theory-python.json. (The metric of 2026-10-14 is withdrawn.)",
  "producer" -> "Revision/kohn_sham/theory/verify_ks_theory.wls",
  "coordinates" -> "the author's coordinates {x0, x1, ..., x7}: x0 = the hidden direction, space-like, z = 6 H x0 takes every real value; x1, x2, x3 = 3-space (scale factor e^{a4}); x4 = time; x5, x6, x7 = the three extra times (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}; on the history e^{-a4/3}); the hidden direction has the scale factor f = e^{-a4} b4^{1/2} |cot z|. Arrays index x0..x7 as 0..7 (xk at index k). Gamma matrices: Revision/algebra/gammas.json (gamma^(xk) = T16[k]).",
  "units" -> "H = 1 in the solver unless stated; energies, momenta and temperatures in units of m (or H); lambda has dimension mass^-6 (Psi has dimension 7/2 in 8 dimensions).",
  "geometry" -> <|
    "metric" -> "g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real (SPEC section 1, version 2)",
    "hiddenCoordinate" -> "y = ln|sin z|/(6H) in (-inf, 0] on every quarter of the period of z, |sin z| = e^{6Hy}, dy = cot z dx0; the fold cos z = 0 (z = pi/2) is y = 0, the tip sin z -> 0 is y -> -inf; the two halves z < pi/2 and z > pi/2 of a cell (0, pi) are the doubled system",
    "lineElement" -> "ds^2 = e^{2a4(x4)}(dx1^2+dx2^2+dx3^2) - dx4^2 + f(x4)^2 [dy^2 - e^{2Hy} (dx5^2+dx6^2+dx7^2)], f = e^{-a4} b4^{1/2}",
    "hiddenScale" -> "f(x4) = e^{-a4(x4)} b4(x4)^{1/2} (the hidden direction and the extra times shrink together; on the history b4 = b4(0) e^{(4/3) a4}, b4(0) = 1: f = e^{-a4/3}); the proper hidden length of the cut-off cell [-L, 0] is f L",
    "warp" -> "W(y) = e^{Hy} on the extra times only (3-space has no warp)",
    "sqrtDetG" -> "e^{-a4} b4^2 e^{3Hy} (= e^{-a4} b4^2 |cot z| (sin^2 z)^{1/4} in the author's chart x0..x7) = e^{3 a4} f^4 e^{3Hy}",
    "kappa" -> "kappa(x4) = e^{-a4(x4)} (the momentum weight; it does not depend on y)",
    "spinConnection" -> "gamma^mu Omega_mu = (3/2)(H/f) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) for every a4(x4), b4(x4) (= (3/2) H e^{a4} b4^{-1/2} gamma^(x0) + ...): the hidden direction gives (1/2) h4 gamma^(x4), 3-space (3/2) a4' gamma^(x4), the extra times (3/2) h4 gamma^(x4) + (3/2)(H/f) gamma^(x0), h4 = b4'/(2 b4) - a4'"|>,
  "sectorAndAnsatz" -> <|
    "sector" -> "good sector: no dependence on x5, x6, x7 (extra-time momenta zero); coordinate 3-torus of size ell, k in (2 pi/ell) Z^3 = Delta k Z^3; extra-time coordinate volume v_t",
    "exactReduction" -> "Psi = e^{i k.x} e^{-(3/2) H y} e^{a4/2} b4^{-1} chi(y, x4) gives EXACTLY (a4 and b4 time-dependent) (1/f) g0 d_y chi + g4 d_x4 chi + i kappa k.gamma chi = (M_eff - i v_v g4) chi, kappa = e^{-a4}, i.e. i d_x4 chi = h(x4) chi with h Hermitian in int dy chi^dag chi = int sqrt|g| Psi^dag Psi over the hidden direction; the factor e^{-(3/2) H y} removes (3/2)(H/f) gamma^(x0), the factor e^{a4/2} b4^{-1} removes (b4'/b4 - a4'/2) gamma^(x4); b4 enters h only through f",
    "instantaneousProblem" -> "at a fixed instant x4 the instantaneous (adiabatic) Kohn-Sham problem is h(a4,0, f0) chi = eps chi with a4,0 = a4(x4), f0 = f(x4): the stationary-slice ansatz Psi = e^{-i eps x4} e^{i k.x} e^{-(3/2) H y} e^{a4,0/2} b4,0^{-1} V_beta chi(y)/sqrt(ell^3 v_t), normalised int_{-L}^{0} chi^dag chi dy = 1",
    "orbital16" -> "Psi_16 = e^{-i eps x4} e^{i k x1} e^{-(3/2) H y} e^{a4/2} b4^{-1} V[:, 2beta:2beta+2] chi(y)/sqrt(ell^3 v_t) for k = (k,0,0); other directions by the spinor rotation"|>,
  "blockBasis" -> <|
    "commutingSet" -> "J = g0 g1 g4 (J^2 = 1), K1 = g2 g3, K2 = g5 g6 (K^2 = -1)",
    "projectors" -> "P(j,s2,s3) = (1+jJ)/2 (1-i s2 K1)/2 (1-i s3 K2)/2",
    "construction" -> "v+ = 8 P(j,s2,s3)(1+g0)/2 e_c (first column c with nonzero image), v- = g0 g1 v+; V = [v+ v- ...]/(2 sqrt 2), unitary",
    "labels" -> (ToString /@ # & /@ labels),
    "labelOrder" -> "beta = 0..7 for (j,s2,s3) = (1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)",
    "seedColumns0Based" -> bb["seeds"],
    "unnormalisedColumns2Sqrt2V" -> Map[ToString, U, {2}],
    "rowsAre" -> "spinor components Psi_0..Psi_15; columns v+, v- of block 0, then block 1, ..."|>,
  "blockForms" -> <|
    "gamma^(x0)" -> "sigma3", "gamma^(x0)gamma^(x1)" -> "-i sigma2", "gamma^(x0)gamma^(x4)" -> "j sigma1",
    "B" -> "j s2 (a number)", "C" -> "s2 sigma2", "BC = -i gamma^(x4)" -> "j sigma2", "gamma^(x4)gamma^(x1)" -> "-j sigma3",
    "B gamma^(x0)" -> "j s2 sigma3", "J" -> "j", "K1" -> "i s2", "K2" -> "i s3",
    "Gamma" -> "anticommutes with J, commutes with K1, K2: maps block (j,s2,s3) onto (-j,s2,s3), 2x2 entry s2 sigma2; on the reduced problem sigma2 h_j(M,k) sigma2 = h_{-j}(-M,k) and the fold parities are exchanged (chi2(0)=0 <-> chi1(0)=0)"|>,
  "blockEquation" -> <|
    "hamiltonian" -> "h_j = j[-(i/f) sigma1 d/dy + M_eff(y) sigma2 + kappa k sigma3] + v_v(y), kappa = e^{-a4}, f = e^{-a4} b4^{1/2}, k signed along x1",
    "ode" -> "chi' = f N chi, N = M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1",
    "realForm" -> "chi = (a, i b), a, b real: a' = f [M_eff a - (kappa k + j(eps - v_v)) b], b' = f [(j(eps - v_v) - kappa k) a - M_eff b]",
    "realFormDensities" -> "chi^dag chi = a^2 + b^2; chi^dag sigma2 chi = 2ab; chi^dag sigma3 chi = a^2 - b^2; chi^dag sigma1 chi = 0",
    "typeRelation" -> "h_{-1} - v = -(h_{+1} - v); sigma3 h_j(k) sigma3 = h_{-j}(-k): the (j,k) and (-j,-k) orbitals are degenerate with chi_{-j,-k} = sigma3 chi_{j,k}",
    "degeneracy" -> "for a lattice shell |k|^2 = Delta k^2 n2 with r3(n2) vectors: every level of h_j(|k|), j = +1 and j = -1 separately, is 4 r3(n2)-fold (4 blocks s2, s3 times the r3 directions); at k = 0 every level is 4-fold per j, 8-fold in total",
    "rotation" -> "spectra depend on |k| only (spinor rotation commutes with g0, g4, B, C)"|>,
  "exchange" -> <|
    "interaction" -> "U = (lambda/2) S^2, S = Psibar Psi = Psi^dag C Psi, normal ordered; lambda > 0 repulsive",
    "expectationRule" -> "<Psi^dag M Psi> = Tr(M rho), rho = sum_occ f u u^dagger B (SPEC section 6); quasi-free (Slater / Mermin) states",
    "wick" -> "<:S^2:> = (Tr C rho)^2 - Tr(C rho C rho)",
    "uniformGas" -> <|
      "result" -> "any p -> -p symmetric occupation of the 8-fold good-sector gas (any temperature): rho = (n B + S C)/16; e_H = (lambda/2) S^2, e_x = -(lambda/32)(n^2 + S^2)",
      "coefficient_n2" -> "-1/32", "coefficient_S2" -> "-1/32",
      "filledShellRatio" -> "E_x/E_H = -1/8 for one filled level at rest (n = S)"|>,
    "kohnShamPotentials" -> <|
      "e_int" -> "e_int(n, S) = (15/32) lambda S^2 - (1/32) lambda n^2 (proper densities; in the solver's units lambda -> lambda_hat and every density times b4(0)^2, see densities.proper)",
      "Meff" -> "M_eff(y) = m + (15/16) lambda S(y)", "Meff_coefficient_of_lambda_S" -> "15/16",
      "vv" -> "v_v(y) = -lambda n(y)/16 (added to h as v_v times the identity)", "vv_coefficient_of_lambda_n" -> "-1/16",
      "onShellLagrangian" -> "<L>/sqrt|g| = e_int (degree-2 homogeneity)",
      "correlation" -> "none (Hartree plus exchange only)"|>,
    "exactFockSlab" -> <|
      "result" -> "for closed shells (k -> -k symmetric), equal occupation of the 4 blocks of each type and of the (j,k)/(-j,-k) partners, the EXACT Fock exchange of the Kohn-Sham determinant is local: e_x^exact = -(lambda/32)(n^2 + S^2 - Q^2 - Y^2), Q = <Psi^dag B gamma^(x0) Psi> = sum over orbitals of w g f q_o, q_o = P chi^dag sigma3 chi for every orbital of either type (= j t_o; (a^2 - b^2) P in the real form), Y = y-current (0)",
      "status" -> "DIAGNOSTIC: the canonical functional is the uniform-gas one (SPEC section 7); the solver should report Delta E_x = +(lambda/32) int sqrt|g| Q^2 (the part the uniform-gas exchange omits). An exact-exchange variant would add w_Q = +lambda Q/16 sigma3 (both block types) to h and +(lambda/32) Q^2 to e_int."|>|>,
  "densities" -> <|
    "perOrbital" -> "with P(y) = e^{-3Hy}/Vol_7, Vol_7 = ell^3 v_t e^{-a4,0} (b4,0/b4(0))^2 (= ell^3 v_t e^{(2 beta - 1) a4,0} = ell^3 v_t e^{(5/3) a4,0} on the history; the proper factor is e^{-3Hy} e^{a4,0}/(ell^3 v_t b4,0^2)): n_o = P chi^dag chi, s_o = P chi^dag j sigma2 chi, t_o = P chi^dag j sigma3 chi (current along k-hat), q_o = P chi^dag sigma3 chi (= j t_o), c_o = P chi^dag j sigma1 chi = 0",
    "total" -> "n(y) = sum_levels w g f n_o, S(y) = sum w g f s_o (same for t, q), g = 4 r3(n2), f the occupation, w = 1/2: canonical convention = the doubled system (the two halves of a cell, joined at the fold); its eigen-orbitals are the solutions with the two fold conditions chi2(0) = 0 and chi1(0) = 0, each normalised on one half int_{-L}^{0} chi^dag chi dy = 1 (norm 2 on the cell, hence w = 1/2 per half); N = sum g f over both fold conditions is the particle number of the cell (N/2 per half)",
    "proper" -> "the solver's densities are the proper densities (per proper 7-volume, P = e^{-3Hy} e^{a4,0}/(ell^3 v_t b4,0^2)) times b4(0)^2, and its coupling is lambda_hat = lambda b4(0)^{-2}: lambda n_proper = lambda_hat n; b4(0) also enters f0 = b4(0)^{1/2} e^{(beta/2 - 1) a4,0}, and the record uses b4(0) = 1 (SPEC section 1)",
    "couplingVolumeScaling" -> "a Kohn-Sham state depends on the coupling and the cell volume only through lambda/Vol (check ks_coupling_volume_scaling): the slice state at (lambda_hat, Vol_7(a4,0)) equals the state of the coordinate cell ell^3 v_t at lambda_eff = lambda_hat e^{-(2 beta - 1) a4,0} = lambda_hat e^{-(5/3) a4,0} (beta = 4/3), at the same f0 and kappa"|>,
  "boundaryConditions" -> <|
    "fold" -> <|"status" -> "derived up to the parameter theta; filling both theta = 0 and theta = pi is ASSUMED (the record's convention)", "statement" -> "the fold cos z = 0 joins the two halves of a cell; the reduced equation is the same on both halves (dy = cot z dx0, e^x0 dx0 = f dy, gamma^mu Omega_mu free of x0), so a spinor continuous across the fold has the same chi(y) on both halves; the boundary form of the doubled cell at the fold is 2(-i j/f) phi^dag sigma1 chi(0) (the y direction points to the fold on both halves), so self-adjointness needs (1 - Q(theta)) chi(0) = 0, Q = cos(theta) sigma3 + sin(theta) sigma2. theta = 0: chi2(0) = 0 (b(0) = 0, even); theta = pi: chi1(0) = 0 (a(0) = 0, odd). The record solves and fills both together (w = 1/2). Both kill the y-current. (Until 2026-10-16 this was the ASSUMED Z2 orbifold of the metric of 2026-10-14, with a mirror copy carrying -m.)"|>,
    "tip" -> <|"status" -> "chosen (regular tip)", "statement" -> "at y = -L: (1 - Q(theta)) chi(-L) = 0, Q = cos(theta) sigma3 + sin(theta) sigma2; canonical theta = 0: chi2(-L) = 0 (b(-L) = 0). For k = 0 it admits the regular fold-localised zero mode (e^{f M y}, 0) for every L and no tip-localised mode for M > 0. For constant M, v the branches are e^{+- f lambda y}, lambda = sqrt(M^2 + kappa^2 k^2 - (eps - v)^2): nothing suppresses an orbital toward the tip (kappa does not depend on y), so the extended levels depend on L like those of a box of proper length f L; only the fold-localised states have an L-independent limit."|>,
    "selfAdjointness" -> "phi^dag h chi - (h phi)^dag chi = d/dy[-(i j/f) phi^dag sigma1 chi]; with current-killing ends h_j is self-adjoint, levels real, orbitals orthogonal",
    "exactK0Spectra" -> "constant M > 0, v = 0, theta = 0: even: eps = 0 with chi = (e^{f M y}, 0), and eps = +-sqrt(M^2 + (n pi/(f L))^2); odd: eps = +-sqrt(M^2 + p^2) with tan(p f L) = -p/M"|>,
  "rescalingIdentity" -> "with the proper hidden coordinate Y = f0 y, f0 = e^{-a4,0} b4,0^{1/2}: KS(a4,0, b4,0; H, L, Delta k, v_t, lambda, N, T) = KS(0, 1; H/f0, f0 L, Delta k e^{-a4,0}, v_t e^{-3 a4,0} b4,0^{3/2}, lambda, N, T) exactly (levels; orbitals chi_Y = chi/sqrt(f0); proper densities). On the history b4 = e^{(4/3) a4} (b4(0) = 1): f0 = e^{-a4,0/3}. The 3-momenta redshift as k e^{-a4}; the hidden direction and the extra times shrink as e^{-a4/3}; the proper 7-volume factor e^{-a4} b4^2 grows as e^{(5/3) a4}.",
  "thermodynamics" -> <|
    "fillingConvention" -> "CONVENTION (not derived here; SPEC section 6 fixes particles as positive-frequency modes of the normal-ordered good sector): particles occupy the positive branch, i.e. the levels with eps > 0 of the lambda = 0 problem together with the k = 0 fold zero modes (eps = 0 at v = 0), each followed continuously as lambda is switched on; the negative branch is the normal-ordered sea and contributes nothing to N, n, S or T. The zero modes are self-conjugate at k = 0, v = 0 (spectrum of h_{+1} - v is minus that of h_{-1} - v); counting them as particle levels is the stated convention, its justification is OPEN.",
    "occupation" -> "f = 1/(1 + exp((eps - mu)/T)), mu fixed by sum w g f = N (Mermin)",
    "energy" -> "E_KS (doubled system) = sum g f eps - 2 Vol_7 int_{-L}^{0} e^{3Hy} e_int dy, Vol_7 = ell^3 v_t e^{(5/3) a4,0} (densities.perOrbital); per half one half of it",
    "entropy" -> "S_ent = -sum g [f ln f + (1-f) ln(1-f)]",
    "grandPotential" -> "Omega = -T sum g ln(1 + exp(-(eps - mu)/T)) - 2 Vol_7 int_{-L}^{0} e^{3Hy} e_int dy (doubled system); F = Omega + mu N"|>,
  "emt" -> <|
    "definition" -> "T^mu_nu = -<K^mu_nu> + delta^mu_nu <L>/sqrt|g>, K_mu nu = (1/4)[Psibar g_(mu D_nu) Psi - D_(nu Psibar g_mu) Psi] (symmetrised), <L>/sqrt|g| = e_int on shell; rho = -T^x4_x4, p_mu = T^mu_mu (SPEC section 4; homogeneous classical limit rho = mS + U, p = S U' - U)",
    "rho" -> "rho(y) = sum w g f eps n_o - e_int",
    "p3" -> "p3(y) = sum w g f (kappa |k|/3) t_o + e_int (shell-averaged; exact for every k -> -k closed cubic shell)",
    "p_t" -> "p_t(y) = e_int (good sector: no extra-time kinetic pressure)",
    "p0" -> "p0(y) = sum w g f [(eps - v_v) n_o - M_eff s_o - kappa |k| t_o] + e_int",
    "offDiagonal" -> "T^x4_y = 0 for eigen-orbitals (K_x4y = f P (eps - v/2) c_o, c_o = 0)",
    "trace" -> "sum of the diagonal kinetic parts = M_eff S + v_v n per point",
    "conservationY" -> "p0' + 3H (p0 - p_t) = 0 for every self-consistent state (nabla_mu T^mu_y = 0; p3 does not enter): solver check",
    "energyChange" -> "nabla_mu T^mu_x4 = -d_x4 rho - 3 a4' (rho + p3) - 3 h4 (rho + p_t) - h4 (rho + p0), h4 = b4'/(2 b4) - a4'; with sqrt|g| = e^{-a4} b4^2 e^{3Hy} on the history (b4'/b4 = beta a4'): dE/da4 = -3 P3 - 3 (beta/2 - 1) P_t - (beta/2 - 1) P0, P = 2 Vol_7 int_{-L}^{0} e^{3Hy} p dy (beta = 4/3: -3 P3 + P_t + P0/3); Hellmann-Feynman with fixed occupations gives the same (solver check)",
    "integrated" -> "2 Vol_7 int_{-L}^{0} e^{3Hy} rho dy = E_KS; 2 Vol_7 int_{-L}^{0} e^{3Hy} 3 (p3 - e_int) dy = sum g f |k| d eps/d|k| (doubled system, w = 1/2 in the densities)",
    "fieldEquationCondition" -> "the field equations of the corrected metric need p0 = p_t (Revision/field_equations_a4/a4-equations.json, generalSource.hiddenEqualsExtraTimes); a Kohn-Sham state has p0 - p_t = sum w g f [(eps - v_v) n_o - M_eff s_o - kappa |k| t_o], the kinetic pressure along the hidden direction (evaluated in Revision/field_equations_a4/reports/ks-source-conditions.json)"|>,
  "adiabaticity" -> <|
    "history" -> "a4 = A H x4 (A = 1 canonical), b4 = b4(0) e^{beta A H x4} (beta = 4/3, b4(0) = 1), a4' = A H, b4'/b4 = beta A H, f = e^{(beta/2 - 1) a4} = e^{-a4/3}; slices a4,0 = a4(x4), b4,0 = e^{beta a4,0}; PRESCRIBED BACKGROUND (see historyStatus)",
    "historyBeta" -> "4/3",
    "historyBetaSource" -> "SPEC section 1: the record keeps the history a4 = H x4, b4 = b4(0) e^{(4/3) H x4} of 2026-10-15 for continuity; in the corrected metric it needs the diagonal, x0-independent source of Revision/metric_warped/results/warped-metric.json (history_source) and Revision/field_equations_a4/a4-equations.json (exponentialHistory.authorWeights)",
    "historyStatus" -> "PRESCRIBED BACKGROUND: the history a4 = H x4, b4 = e^{(4/3) H x4} is prescribed, not solved for. With the author's Lovelock weights the a4 and b4 equations of SPEC section 5 allow it only with a diagonal source with p0 = p_t that grows with x4 (Revision/field_equations_a4/a4-equations.json, exponentialHistory.authorWeights.historySource_kappaT_minus_Lam); whether the Kohn-Sham states along it supply this source is evaluated in Revision/field_equations_a4/reports/ks-source-conditions.json. The Kohn-Sham gas is therefore a test field on a prescribed background without back-reaction, and quantities derived along this history (energies, pressures, equations of state) are not consequences of the coupled field equations.",
    "exactEvolution" -> "i d_x4 chi = h(a4(x4), f(x4)) chi (mean field); k, the block and the fold condition are conserved; transitions only between levels of the same (k, j, block, fold condition)",
    "derivative" -> "d_a h_j = -j kappa k sigma3 + (1 - beta/2) j (-(i/f) sigma1 d_y) (frozen potentials; beta = 4/3: + (1/3) times the kinetic term) + j (d_a M_eff) sigma2 + d_a v_v (self-consistent part, by finite differences between slices; it contains the change of the effective coupling lambda_hat/Vol_7(a4,0) ~ e^{-(5/3) a4,0})",
    "measure" -> "Q_nm = A H |<n| d_a h |m>| / (eps_n - eps_m)^2 = A H |<n| d_a m>| / |eps_n - eps_m| for n occupied, m empty in the same sector; adiabatic iff max Q_nm << 1; leading-order transition probability ~ Q_nm^2",
    "hellmannFeynman" -> "d eps_n/da = <n| d_a h |n>",
    "caveat" -> "adiabatic evolution conserves the occupation of every (k, j, block, fold condition, level); when levels of different k cross the Fermi level between slices, the instantaneous aufbau ground state differs from the adiabatically continued state: the solver should flag such crossings. The non-adiabatic (time-dependent) problem is OPEN."|>,
  "checksNumeric" -> <|
    "braneBandSlope_a0" -> num[sl0, 17],
    "braneBandSlope_a0_half_history" -> num[sl5, 17],
    "braneBandSlopeFormula" -> "c = e^{-a4,0}, d eps_0/dk = j c at k = 0 (even fold condition, theta = 0), for every M, L, f"|>,
  "solverChecklist" -> {
    "free k = 0 spectra (even: 0, sqrt(M^2+(n pi/(f L))^2); odd: tan(p f L) = -p/M)",
    "brane-band slope c = e^{-a4,0} at small k",
    "j-type mirror symmetry of the spectra (v = 0) and 4 r3(n2) degeneracy",
    "exact rescaling identity between slices (a4,0, f0 vs a4 = 0, f = 1 with H/f0, f0 L, Delta k e^{-a4,0}, v_t e^{-3 a4,0} b4,0^{3/2})",
    "N conservation and the orbital normalisation",
    "y-conservation p0' + 3H (p0 - p_t) = 0 of every self-consistent state",
    "trace identity and T^x4_y = 0 (zero y-current of every orbital)",
    "dE/da4 = -3 P3 + P_t + P0/3 (beta = 4/3), P = 2 Vol_7 int_{-L}^{0} e^{3Hy} p dy (doubled system), by finite differences between slices (fixed occupations)",
    "exact-Fock diagnostic Delta E_x = (lambda/32) 2 Vol_7 int_{-L}^{0} e^{3Hy} Q^2 dy"}
|>;

ksJson = ExportString[jsonTheory, "RawJSON"];
ksJson2 = ExportString[jsonTheory, "RawJSON"];
writeLF[path_, text_String] := Module[{dir = DirectoryName[path], s},
  If[! DirectoryQ[dir], CreateDirectory[dir, CreateIntermediateDirectories -> True]];
  s = OpenWrite[path, BinaryFormat -> True, CharacterEncoding -> "UTF-8"];
  If[Head[s] =!= OutputStream, Print["ERROR  cannot write ", path]; Exit[1]];
  BinaryWrite[s, ToCharacterCode[StringReplace[text, "\r\n" -> "\n"], "UTF-8"]]; Close[s]];
writeLF[FileNameJoin[{$ks, "ks-theory.json"}], If[StringEndsQ[ksJson, "\n"], ksJson, ksJson <> "\n"]];
back = Import[FileNameJoin[{$ks, "ks-theory.json"}], "RawJSON"];
addCheck["ks_theory_json_written",
  ksJson === ksJson2 && back["blockBasis"]["unnormalisedColumns2Sqrt2V"] == Map[ToString, U, {2}] &&
  ToExpression[back["exchange"]["uniformGas"]["coefficient_n2"]] == -1/32 &&
  StringStartsQ[back["adiabaticity"]["historyStatus"], "PRESCRIBED BACKGROUND"] &&
  StringContainsQ[back["adiabaticity"]["history"], "PRESCRIBED BACKGROUND"] && back["adiabaticity"]["historyBeta"] === "4/3",
  "ks-theory.json written deterministically (two exports identical, LF) and re-imported: basis, coefficients, beta = 4/3 and the label of the history a4 = A H x4, b4 = b4(0) e^{beta A H x4} as a PRESCRIBED BACKGROUND (adiabaticity.history, adiabaticity.historyStatus) round-trip"];

(* ---------------- report ---------------- *)
jstr[s_String] := "\"" <> StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\""}] <> "\"";
nPass = Count[checks, c_ /; c["verdict"] == "PASS"]; nTot = Length[checks];
report = StringJoin[
  "{\n",
  "  \"report\": ", jstr["Revision Kohn-Sham theory (SPEC sections 1, 7): exact derivation and checks in WolframScript"], ",\n",
  "  \"producer\": ", jstr["Revision/kohn_sham/theory/verify_ks_theory.wls"], ",\n",
  "  \"package\": ", jstr["Revision/kohn_sham/theory/KohnShamTheory.wl"], ",\n",
  "  \"export\": ", jstr["Revision/kohn_sham/ks-theory.json"], ",\n",
  "  \"coordinates\": ", jstr["the author's coordinates {x0, ..., x7}: x0 = the hidden direction (y = ln|sin 6Hx0|/(6H) <= 0 on every quarter); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the extra times; the corrected metric of 2026-10-16 (version 2), general a4(x4), b4(x4) > 0, every real z"], ",\n",
  "  \"summary\": {\"passed\": ", ToString[nPass], ", \"failed\": ", ToString[nTot - nPass], ", \"total\": ", ToString[nTot], "},\n",
  "  \"checks\": [\n",
  StringRiffle[("    {\"name\": " <> jstr[#["name"]] <> ", \"verdict\": " <> jstr[#["verdict"]] <> ", \"detail\": " <> jstr[#["detail"]] <> "}") & /@ checks, ",\n"],
  "\n  ]\n}\n"];
writeLF[FileNameJoin[{$ks, "reports", "ks-theory-wolfram.json"}], report];
Print[nPass, "/", nTot, " checks passed; time ", Round[AbsoluteTime[] - t0, 0.1], " s"];
Exit[If[nPass == nTot, 0, 1]];
