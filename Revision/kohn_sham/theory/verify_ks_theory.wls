#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_ks_theory.wls

   Revision Kohn-Sham theory for dirac16complex in the author's primordial field (Revision/SPEC.md,
   sections 1 and 7), exact derivation and verification in WolframScript.  Revision code only.
   Input:   Revision/algebra/gammas.json (the Revision algebra fixture, x1..x8 order)
   Package: Revision/kohn_sham/theory/KohnShamTheory.wl
   Writes, deterministically (LF, no time stamps):
     Revision/kohn_sham/reports/ks-theory-wolfram.json   every check with name, verdict, detail
     Revision/kohn_sham/ks-theory.json                   the formulas the Rust solver must implement
   Usage:  wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls
   The independent second engine is Revision/kohn_sham/theory/check_ks_theory.py (sympy).
   Exit code 0 if every check passes, 1 otherwise.
*)

$here = DirectoryName[$InputFileName];
$ks = FileNameJoin[{$here, ".."}];
$rev = FileNameJoin[{$ks, ".."}];
Get[FileNameJoin[{$here, "KohnShamTheory.wl"}]];
t0 = AbsoluteTime[];

checks = {};
addCheck[name_String, ok_, detail_String] := (
  AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS", "FAIL"], "  ", name, "  t=", Round[AbsoluteTime[] - t0, 0.1]]);
zeroQ[m_] := AllTrue[Flatten[{Simplify[m]}], # === 0 &];
num[x_, d_: 16] := ToString[NumberForm[N[x, 40], d, NumberFormat -> (If[#3 == "", #1, #1 <> "e" <> #3] &)]];

(* ---------------- A. gammas ---------------- *)
gpath = FileNameJoin[{$rev, "algebra", "gammas.json"}];
{g, etaM} = KSLoadGammas[gpath];
eta = Diagonal[etaM];
id16 = IdentityMatrix[16]; id2 = IdentityMatrix[2]; z16 = ConstantArray[0, {16, 16}];
{s1, s2, s3} = KSPauli;
{g1, g2, g3, g4, g5, g6, g7, g8} = g;
addCheck["fixture_input", Length[g] == 8,
  "gammas read from Revision/algebra/gammas.json (sha256 " <> IntegerString[FileHash[gpath, "SHA256"], 16, 64] <> ")"];
addCheck["clifford_relation",
  And @@ Flatten[Table[g[[a]].g[[b]] + g[[b]].g[[a]] == 2 KroneckerDelta[a, b] eta[[a]] id16, {a, 8}, {b, 8}]] &&
  eta == {1, 1, 1, -1, -1, -1, -1, 1},
  "{gamma^a, gamma^b} = 2 eta^ab, eta = diag(+1,+1,+1,-1,-1,-1,-1,+1) in x1..x8"];
C16 = g8.g1.g2.g3; B16 = -I C16.g4; Gam = g8.g1.g2.g3.g4.g5.g6.g7;
addCheck["C_B_Gamma",
  Transpose[C16] == C16 && C16.C16 == id16 && ConjugateTranspose[B16] == B16 && B16.B16 == id16 &&
  Gam == DiagonalMatrix[Join[ConstantArray[-1, 8], ConstantArray[1, 8]]] &&
  B16.C16 == -I g4 && C16.g4 == I B16 && C16.B16.C16 == B16,
  "C = g8 g1 g2 g3 (real symmetric, C^2 = 1), B = -i C g4 (Hermitian, B^2 = 1), Gamma = diag(-I8, I8); BC = -i g4, C g4 = i B, C B C = B"];

(* ---------------- B. geometry ---------------- *)
$Assumptions = {H > 0, y < 0, Vol > 0, ell > 0, vt > 0, Element[{x1, x2, x3, x4, x5, x6, x7, k, k1, k2, k3, eps, M, v, a0, lam, nn, SS, QQ, L},
    Reals], L > 0, 0 < x8 < Pi/(12 H)};
zOfy = ArcSin[Exp[6 H y]];
addCheck["geometry_hidden_coordinate",
  Simplify[Cot[zOfy]^2 D[zOfy/(6 H), y]^2 == 1] && Simplify[Sin[zOfy]^(1/3) == Exp[2 H y]] &&
  Simplify[D[Log[Sin[6 H x8]]/(6 H), x8] == Cot[6 H x8]],
  "y = Log[Sin[z]]/(6H), z = 6 H x8: dy = Cot[z] dx8, Cot[z]^2 dx8^2 = dy^2, Sin[z]^(1/3) = E^(2 H y); z in (0, Pi/2) <-> y in (-Infinity, 0)"];
gx8 = KSGeometryX8[a0];
addCheck["geometry_sqrt_det",
  Simplify[Abs[Det[gx8["g"]]] == Cos[6 H x8]^2, 0 < 6 H x8 < Pi/2],
  "|det g| = Cos[z]^2 in the author's chart (a4-independent); y chart: Sqrt|g| = W^6 = E^(6 H y)"];
geo = KSGeometryY[a4[x4]];
X = geo["coords"]; hv = geo["h"];
chr = KSChristoffel[geo["g"], X];
Om = KSSpinConnection[g, etaM, hv, chr, X];
addCheck["spin_connection_compatibility",
  And @@ Flatten[Table[zeroQ[D[g[[n]]/hv[[n]], X[[m]]] + Sum[chr[[n, m, l]] g[[l]]/hv[[l]], {l, 8}] +
      Om[[m]].(g[[n]]/hv[[n]]) - (g[[n]]/hv[[n]]).Om[[m]]], {m, 8}, {n, 8}]],
  "canonical spin connection (vielbein postulate), a4 = a4[x4]: nabla_mu gamma^nu = 0 for all 64 (mu, nu)"];
slash = Simplify[Sum[g[[m]].Om[[m]]/hv[[m]], {m, 8}]];
addCheck["spin_connection_slash_3H", zeroQ[slash - 3 H g8],
  "gamma^mu Omega_mu = 3 H gamma^(x8) exactly, no a4'[x4] term"];
sInfl = Simplify[Sum[g[[m]].Om[[m]]/hv[[m]], {m, 1, 3}] /. H -> 0];
sDefl = Simplify[Sum[g[[m]].Om[[m]]/hv[[m]], {m, 5, 7}] /. H -> 0];
addCheck["spin_connection_time_terms_cancel",
  zeroQ[sInfl - (3/2) a4'[x4] g4] && zeroQ[sDefl + (3/2) a4'[x4] g4] && zeroQ[Om[[4]]] && zeroQ[Om[[8]]],
  "coefficients " <> ToString[Simplify[{(sInfl.Inverse[g4])[[1, 1]], (sDefl.Inverse[g4])[[1, 1]]}], InputForm] <> "; time-direction pieces: sum over the 3 inflating directions = +(3/2) a4' gamma^(x4), over the 3 deflating ones = -(3/2) a4' gamma^(x4): they cancel; Omega_x4 = Omega_y = 0"];
chr8 = KSChristoffel[gx8["g"], gx8["coords"]];
Om8 = KSSpinConnection[g, etaM, gx8["h"], chr8, gx8["coords"]];
slash8 = Simplify[Sum[g[[m]].Om8[[m]]/gx8["h"][[m]], {m, 8}], 0 < 6 H x8 < Pi/2];
addCheck["spin_connection_slash_3H_x8_chart", zeroQ[slash8 - 3 H g8],
  "in the author's x8 chart: gamma^mu Omega_mu = 3 H gamma^(x8) as well"];

(* ---------------- C. ansatz ---------------- *)
chiF = Table[c[i][y, x4], {i, 16}];
W = Exp[H y]; kap = Exp[-H y - a4[x4]];
phase = Exp[I (k1 x1 + k2 x2 + k3 x3)];
dirac[Psi_] := Sum[g[[m]].(D[Psi, X[[m]]] + Om[[m]].Psi)/hv[[m]], {m, 8}];
red = g8.D[chiF, y] + g4.D[chiF, x4] + I kap (k1 g1 + k2 g2 + k3 g3).chiF;
addCheck["ansatz_removes_spin_connection", zeroQ[dirac[phase W^-3 chiF]/(phase W^-3) - red],
  "gamma^mu D_mu (e^{ik.x} W^-3 chi(y, x4)) = e^{ik.x} W^-3 [g8 d_y + g4 d_x4 + i kappa k.gamma] chi, kappa = E^(-H y - a4[x4]): exact for time-dependent a4"];
addCheck["ansatz_without_W3_term_survives", zeroQ[dirac[phase chiF]/phase - red - 3 H g8.chiF],
  "without W^-3 the term 3 H gamma^(x8) chi survives"];
addCheck["hamiltonian_16_hermitian",
  Transpose[g4.g8] == g4.g8 && ConjugateTranspose[-g4.g1] == -g4.g1 && ConjugateTranspose[-I g4] == -I g4,
  "i d_x4 chi = h chi with h = i g4 g8 d_y - kappa k_j g4 g^j + M(-i g4) + v: g4 g8 real symmetric, g4 g^j and -i g4 Hermitian"];

(* ---------------- D. blocks ---------------- *)
J = g8.g1.g4; K1 = g2.g3; K2 = g5.g6;
A0 = g8; A1 = g8.g1; A4 = g8.g4;
comm[a_, b_] := a.b - b.a;
addCheck["blocks_commuting_set",
  And @@ Flatten[Table[comm[P, Q] == z16, {P, {J, K1, K2}}, {Q, {A0, A1, A4, B16, C16, J, K1, K2}}]] &&
  J.J == id16 && K1.K1 == -id16 && K2.K2 == -id16,
  "J = g8 g1 g4, K1 = g2 g3, K2 = g5 g6 commute with each other and with g8, g8 g1, g8 g4, B, C"];
bb = KSBlockBasis[g];
labels = bb["labels"]; U = bb["U"]; V = U/(2 Sqrt[2]);
addCheck["blocks_basis_unitary",
  Simplify[ConjugateTranspose[V].V] == id16 && SubsetQ[{0, 1, -1, I, -I}, Union[Flatten[U]]],
  "V = U/(2 Sqrt[2]) unitary, U entries in {0, +-1, +-I}; seeds (0-based) " <> ToString[bb["seeds"]]];
expect = {
  {"gamma^(x8)", A0, s3 &}, {"gamma^(x8)gamma^(x1)", A1, -I s2 &}, {"gamma^(x8)gamma^(x4)", A4, #1 s1 &},
  {"B", B16, #1 #2 id2 &}, {"C", C16, #2 s2 &}, {"BC", B16.C16, #1 s2 &}, {"gamma^(x4)gamma^(x1)", g4.g1, -#1 s3 &},
  {"B gamma^(x8)", B16.g8, #1 #2 s3 &}, {"J", J, #1 id2 &}, {"K1", K1, I #2 id2 &}, {"K2", K2, I #3 id2 &}};
blockDiagQ[Xm_] := Module[{Y = Simplify[ConjugateTranspose[V].Xm.V]},
  And @@ Flatten[Table[If[a != b, Y[[2 a - 1 ;; 2 a, 2 b - 1 ;; 2 b]] == ConstantArray[0, {2, 2}], True], {a, 8}, {b, 8}]]];
okForms = And @@ Table[blockDiagQ[e[[2]]] && And @@ MapThread[#1 == e[[3]] @@ #2 &, {KSBlock[V, e[[2]]], labels}], {e, expect}];
addCheck["blocks_forms", okForms,
  "block (j,s2,s3): g8 = sigma3, g8 g1 = -i sigma2, g8 g4 = j sigma1, B = j s2, C = s2 sigma2, BC = j sigma2, g4 g1 = -j sigma3, B g8 = j s2 sigma3, J = j, K1 = i s2, K2 = i s3"];
YG = Simplify[ConjugateTranspose[V].Gam.V];
gamPairs = Select[Tuples[Range[8], 2], YG[[2 #[[1]] - 1 ;; 2 #[[1]], 2 #[[2]] - 1 ;; 2 #[[2]]]] =!= ConstantArray[0, {2, 2}] &];
addCheck["blocks_relation_to_Gamma",
  gamPairs == {{1, 5}, {2, 6}, {3, 7}, {4, 8}, {5, 1}, {6, 2}, {7, 3}, {8, 4}} &&
  And @@ Table[YG[[2 p[[1]] - 1 ;; 2 p[[1]], 2 p[[2]] - 1 ;; 2 p[[2]]]] == labels[[p[[1]], 2]] s2, {p, gamPairs}] &&
  Gam.J == -J.Gam && comm[Gam, K1] == z16 && comm[Gam, K2] == z16,
  "Gamma anticommutes with J, commutes with K1, K2: block (j,s2,s3) <-> (-j,s2,s3) with 2x2 entry s2 sigma2"];
okH = And @@ Flatten[Table[With[{Vb = V[[All, 2 b - 1 ;; 2 b]], j = labels[[b, 1]]},
    {Simplify[ConjugateTranspose[Vb].(I g4.g8).Vb] == -I j s1, Simplify[ConjugateTranspose[Vb].(-g4.g1).Vb] == j s3,
     Simplify[ConjugateTranspose[Vb].(-I g4).Vb] == j s2}], {b, 8}]];
addCheck["block_hamiltonian", okH,
  "h_j = j[-i sigma1 d_y + M sigma2 + kappa k sigma3] + v in every block of type j (k along x1)"];
Nm[j_, Mm_, kk_, e_, vv_, kp_] := Mm s3 - kp kk s2 + I j (e - vv) s1;
hj[j_, Mm_, kk_, vv_, kp_] := j (Mm s2 + kp kk s3) + vv id2;
addCheck["block_ode_equivalent",
  And @@ Table[Simplify[-I j s1.Nm[j, M, k, eps, v, kp] == eps id2 - hj[j, M, k, v, kp]], {j, {1, -1}}],
  "h_j chi = eps chi <=> chi' = N chi, N = M sigma3 - kappa k sigma2 + i j (eps - v) sigma1"];
addCheck["block_type_relation",
  Simplify[hj[-1, M, k, 0, kp] == -hj[1, M, k, 0, kp]] && Simplify[s3.hj[1, M, k, 0, kp].s3 == hj[-1, M, -k, 0, kp]] &&
  s3.(-I s1).s3 == I s1,
  "h_{-1} - v = -(h_{+1} - v); sigma3 h_j(k) sigma3 = h_{-j}(-k) (also for the derivative term): chi_{-j,-k} = sigma3 chi_{j,k}"];
addCheck["block_Gamma_map",
  Simplify[s2.hj[1, M, k, 0, kp].s2 == hj[-1, -M, k, 0, kp]] && s2.(-I s1).s2 == I s1,
  "sigma2 h_j(M, k) sigma2 = h_{-j}(-M, k): the block form of Gamma maps (j, M) -> (-j, -M) at the same k, eps; it swaps the brane parities chi2(0) = 0 <-> chi1(0) = 0"];
R12 = Cos[th/2] id16 + Sin[th/2] g1.g2;
addCheck["rotation_invariance",
  zeroQ[R12.(k g1).Inverse[R12] - k (Cos[th] g1 - Sin[th] g2)] && And @@ (comm[R12, #] == z16 & /@ {g8, g4, B16, C16}),
  "the spinor rotation Cos[th/2] + Sin[th/2] g1 g2 commutes with g8, g4, B, C and rotates k.gamma: spectra depend on |k|"];

(* ---------------- E. exchange ---------------- *)
hp = M (-I g4) - (p1 g4.g1 + p2 g4.g2 + p3 g4.g3 + p8 g4.g8);
addCheck["gas_mode_projector", Simplify[hp.hp == (M^2 + p1^2 + p2^2 + p3^2 + p8^2) id16],
  "flat good-sector modes: h_p^2 = (M^2 + p^2) 1, eps = +-E each 8-fold; G_p = (1 + h_p/E)/2"];
Gp = (id16 + hp/EE)/2;
rhoAng = Integrate[(Gp.B16 /. {p1 -> pr Sin[th] Cos[ph], p2 -> pr Sin[th] Sin[ph], p3 -> pr Cos[th], p8 -> 0}) Sin[th],
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
{nS, sS, qS, yS} = Simplify[{Tr[B16.rs], Tr[C16.rs], Tr[B16.g8.rs], Tr[B16.(-I C16.g8).rs]}];
exS = Expand[-(lam/2) Tr[C16.rs.C16.rs]];
addCheck["exchange_slab_exact_fock",
  Length[grp] == 48 && {nS, sS, qS} == {8 d0, 8 d2, 8 d3} && Simplify[exS + (lam/32) (nS^2 + sS^2 - qS^2 - 64 d1^2)] === 0,
  "closed-shell level (4 blocks of type +1 with D, 4 of type -1 with sigma3 D sigma3), averaged over the 48-element spinor octahedral group (" <>
  "End(16) carries spin 0 and 1 only, so this equals the full SO(3) average): n = 8 d0, S = 8 d2, Q = <Psi^dag B g8 Psi> = 8 d3; " <>
  "exact local Fock exchange -(lambda/32)(n^2 + S^2 - Q^2 - Y^2), Y = 8 d1 (y-current, 0 for eigen-orbitals)"];

(* ---------------- F. boundary conditions ---------------- *)
okPA = And @@ Table[Simplify[-s3.(Nm[j, Mf[-y], k, eps, vf[-y], Exp[H y - a0]]).s3 ==
      Nm[j, -Mf[-y], k, eps, vf[-y], Exp[H y - a0]]], {j, {1, -1}}];
addCheck["bc_mirror_map_PA", okPA,
  "P_A: chi(y) -> sigma3 chi(-y) maps (M(y), v(y), kappa(y)) to (-M(-y), v(-y), kappa(-y)); with the mirror warp W = E^(-H|y|) P_A is a symmetry iff M_eff is odd"];
addCheck["bc_mirror_parities_of_densities",
  {s3.id2.s3 == id2, s3.s2.s3 == -s2, s3.s3.s3 == s3, s3.s1.s3 == -s1} === {True, True, True, True},
  "under P_A: n, Q even; S, y-current odd => the mirror carries (-m, +lambda) (v_v even)"];
cur[ch_] := Conjugate[ch].s1.ch;
addCheck["bc_brane_parity_conditions",
  Simplify[ComplexExpand[cur[{ca + I cb, 0}]]] == 0 && Simplify[ComplexExpand[cur[{0, ca + I cb}]]] == 0,
  "ASSUMED Z2 mirror: (1 -+ gamma^(x8)) chi(0) = 0, i.e. chi2(0) = 0 (even) or chi1(0) = 0 (odd); both kill the y-current"];
hop[j_, w_] := j (-I s1.D[w, y] + Mf[y] s2.w + Exp[-H y - a0] k s3.w) + vf[y] w;
phiV = {ph1[y] + I ph2[y], ph3[y] + I ph4[y]}; chV = {f1[y] + I f2[y], f3[y] + I f4[y]};
okBT = And @@ Table[Simplify[ComplexExpand[Conjugate[phiV].hop[j, chV] - Conjugate[hop[j, phiV]].chV -
        D[-I j Conjugate[phiV].s1.chV, y]]] === 0, {j, {1, -1}}];
addCheck["bc_self_adjoint_boundary_term", okBT,
  "phi^dag h_j chi - (h_j phi)^dag chi = d/dy[-i j phi^dag sigma1 chi]: h_j self-adjoint with current-killing ends"];
Qt = Cos[tq] s3 + Sin[tq] s2;
addCheck["bc_tip_family", Simplify[Qt.Qt] == id2 && Simplify[Qt.s1 + s1.Qt] == ConstantArray[0, {2, 2}],
  "tip: (1 - Q(theta)) chi(-L) = 0, Q = Cos[theta] sigma3 + Sin[theta] sigma2, Q^2 = 1, {Q, sigma1} = 0; canonical theta = 0: chi2(-L) = 0"];
addCheck["bc_current_conserved_along_y",
  And @@ Table[Simplify[ComplexExpand[ConjugateTranspose[Nm[j, M, k, eps, v, kp]]].s1 + s1.Nm[j, M, k, eps, v, kp]] ==
      ConstantArray[0, {2, 2}], {j, {1, -1}}],
  "chi^dag sigma1 chi is constant in y on solutions (zero for eigen-orbitals)"];
(* exact k = 0 spectra by DSolve *)
solEven = DSolve[{a'[y] == M a[y] - j e b[y], b'[y] == j e a[y] - M b[y]}, {a, b}, y];
okK0 = Module[{bn, an, en = Sqrt[M^2 + (n Pi/L)^2]},
  bn = Sin[n Pi y/L]; an = (D[bn, y] + M bn)/(j en);
  And @@ Table[Simplify[(D[an, y] - (M an - j en bn)) /. j -> jv] === 0, {jv, {1, -1}}] &&
  Simplify[(bn /. y -> -L) == 0, Element[n, Integers]] &&
  Simplify[D[Exp[M y], y] == M Exp[M y]]];
okOdd = Module[{ao = Sin[pp y], eo = Sqrt[M^2 + pp^2], bo},
  bo = (M ao - D[ao, y])/eo; Simplify[D[bo, y] - (eo ao - M bo) == 0] &&
  Simplify[eo (bo /. y -> -L) == -M Sin[pp L] - pp Cos[pp L]]];
addCheck["bc_exact_k0_spectra", okK0 && okOdd && Length[solEven] == 1,
  "k = 0, constant M, v = 0, theta = 0: even parity: zero mode chi = (E^(M y), 0) and eps = +-Sqrt[M^2 + (n Pi/L)^2]; odd parity: eps^2 = M^2 + p^2 with Tan[p L] = -p/M"];
vdec = {1, -I};
addCheck["bc_tip_asymptotics", Simplify[(-kp k s2).vdec == kp k vdec] && s2.vdec == -vdec,
  "as y -> -Infinity N -> -kappa k sigma2: branches exp(+- k kappa/H) on the sigma2 = -+1 eigenvectors; for k != 0 the orbital is suppressed at the tip like exp(-|k|(kappa(-L) - kappa(y))/H)"];

(* ---------------- G. rescaling ---------------- *)
hfull[j_, kk_, aa_] := j (M s2 + Exp[-H y - aa] kk s3);
addCheck["rescaling_identity",
  And @@ Table[Simplify[hfull[j, k, aa] == hfull[j, k Exp[-aa], 0]], {j, {1, -1}}] &&
  Simplify[Exp[-6 H y]/(ell^3 vt) == Exp[-6 H y]/((ell Exp[aa])^3 (vt Exp[-3 aa]))],
  "KS(a4,0; Delta k, v_t, lambda) = KS(0; Delta k E^(-a4,0), v_t E^(-3 a4,0), lambda) exactly (same proper boxes); equivalently KS(0; Delta k E^(-a4,0), v_t, lambda E^(3 a4,0)) with proper densities times E^(-3 a4,0)"];

(* ---------------- H. EMT (16 components, ComplexExpand with real symbols) ---------------- *)
emtOK = True; emtDet = {};
Do[
  Module[{j = labels[[b, 1]], Vb = V[[All, 2 b - 1 ;; 2 b]], chi2, u, BC, Kd, Ko, sub, nc, sc, tc, cc, P, r1, r4, ry, r22, r55, r4y,
     Nn, dch},
    chi2 = {f1[y] + I f2[y], f3[y] + I f4[y]};
    u = Exp[-I eps x4 + I k x1] W^-3 Vb.chi2/Sqrt[Vol];
    BC = B16.C16;
    Kd[mu_] := Module[{gm = g[[mu]]/hv[[mu]], du = D[u, X[[mu]]]},
      Simplify[ComplexExpand[(Conjugate[u].BC.gm.(du + Om[[mu]].u) - Conjugate[du].BC.gm.u + Conjugate[u].BC.Om[[mu]].gm.u)/2]]];
    Ko[mu_, nu_] := Module[{gl, Dm2, dm2},
      gl[m_] := eta[[m]] hv[[m]] g[[m]]; Dm2[m_] := D[u, X[[m]]] + Om[[m]].u; dm2[m_] := D[u, X[[m]]];
      Simplify[ComplexExpand[Sum[Conjugate[u].BC.gl[pr[[1]]].Dm2[pr[[2]]] - Conjugate[dm2[pr[[2]]]].BC.gl[pr[[1]]].u +
           Conjugate[u].BC.Om[[pr[[2]]]].gl[pr[[1]]].u, {pr, {{mu, nu}, {nu, mu}}}]/4]]];
    Nn = M s3 - kap k s2 + I j (eps - v) s1;
    dch = ComplexExpand[Nn.chi2];
    sub = {f1'[y] -> ComplexExpand[Re[dch[[1]]]], f2'[y] -> ComplexExpand[Im[dch[[1]]]],
           f3'[y] -> ComplexExpand[Re[dch[[2]]]], f4'[y] -> ComplexExpand[Im[dch[[2]]]]};
    nc = ComplexExpand[Conjugate[chi2].chi2]; sc = ComplexExpand[Conjugate[chi2].(j s2).chi2];
    tc = ComplexExpand[Conjugate[chi2].(j s3).chi2]; cc = ComplexExpand[Conjugate[chi2].(j s1).chi2];
    P = Exp[-6 H y]/Vol;
    r1 = Simplify[-Kd[1] - P kap k tc];
    r4 = Simplify[Kd[4] - P eps nc];
    r22 = Simplify[Kd[2]]; r55 = Simplify[Kd[5]];
    ry = Simplify[-(Kd[8] /. sub) - P ((eps - v) nc - M sc - kap k tc)];
    r4y = Simplify[(Ko[4, 8] /. sub) - P (eps - v/2) cc];
    emtOK = emtOK && r1 === 0 && r4 === 0 && r22 === 0 && r55 === 0 && ry === 0 && r4y === 0;
    AppendTo[emtDet, "block " <> ToString[b - 1] <> ": " <> If[{r1, r4, r22, r55, ry, r4y} === {0, 0, 0, 0, 0, 0}, "all residuals 0",
      "residuals " <> ToString[{r1, r4, r22, r55, ry, r4y}, InputForm]]]],
  {b, {1, 6}}];
addCheck["emt_orbital_components", emtOK,
  "per orbital (expectation rule, a4 = a4[x4] general, spin connection drops out of the diagonal): -K^x1_x1 = P kappa k chi^dag j sigma3 chi, K^x4_x4 = P eps |chi|^2, K^x2_x2 = K^x5_x5 = 0, -K^y_y = P[(eps - v)|chi|^2 - M chi^dag j sigma2 chi - kappa k chi^dag j sigma3 chi], K_x4y = P (eps - v/2) chi^dag j sigma1 chi (= 0 for eigen-orbitals), P = E^(-6 H y)/(ell^3 v_t); " <>
  StringRiffle[emtDet, "; "]];
addCheck["emt_trace_identity", Simplify[(-kap k tt) + eps no + (M so + kap k tt - (eps - v) no) == M so + v no],
  "sum of the diagonal K = M_eff s + v_v n (on-shell trace); T^mu_nu = -<K^mu_nu> + delta^mu_nu e_int"];
Module[{chi2 = {f1[y] + I f2[y], f3[y] + I f4[y]}, Nn, dch, sub, nc, sc, tc, p8c},
  Nn = Mf[y] s3 - kap k s2 + I (eps - vf[y]) s1;
  dch = ComplexExpand[Nn.chi2];
  sub = {f1'[y] -> ComplexExpand[Re[dch[[1]]]], f2'[y] -> ComplexExpand[Im[dch[[1]]]],
         f3'[y] -> ComplexExpand[Re[dch[[2]]]], f4'[y] -> ComplexExpand[Im[dch[[2]]]]};
  nc = ComplexExpand[Conjugate[chi2].chi2]; sc = ComplexExpand[Conjugate[chi2].s2.chi2]; tc = ComplexExpand[Conjugate[chi2].s3.chi2];
  p8c = (eps - vf[y]) nc - Mf[y] sc - kap k tc;
  addCheck["emt_y_conservation_orbital",
    Simplify[(D[p8c, y] /. sub) - (H kap k tc - vf'[y] nc - Mf'[y] sc)] === 0,
    "one orbital (j = 1) in external M(y), v(y): d/dy[(eps - v) n_c - M s_c - kappa k t_c] = H kappa k t_c - v' n_c - M' s_c"]];
Tmix[r_, q3_, qt_, q8_] := DiagonalMatrix[{q3, q3, q3, -r, qt, qt, qt, q8}];
divT[T_, nu_] := Sum[D[T[[m, nu]], X[[m]]], {m, 8}] + Sum[chr[[m, m, l]] T[[l, nu]], {m, 8}, {l, 8}] -
   Sum[chr[[l, m, nu]] T[[m, l]], {m, 8}, {l, 8}];
Tf = Tmix[rh[y, x4], p3f[y, x4], ptf[y, x4], p8f[y, x4]];
eS = (15/32) lam Sf[y]^2 - lam nf[y]^2/32;
addCheck["emt_y_conservation_selfconsistent",
  Simplify[divT[Tf, 8] - (D[p8f[y, x4], y] + 6 H p8f[y, x4] - 3 H (p3f[y, x4] + ptf[y, x4]))] === 0 &&
  Simplify[-D[(15/16) lam Sf[y], y] Sf[y] - D[-lam nf[y]/16, y] nf[y] + D[eS, y]] === 0,
  "nabla_mu T^mu_y = p8' + 6H p8 - 3H(p3 + p_t); the force terms of the orbital identity cancel against e_int' for the self-consistent M_eff, v_v"];
addCheck["emt_x4_component",
  Simplify[divT[Tf, 4] - (-D[rh[y, x4], x4] - 3 a4'[x4] (p3f[y, x4] - ptf[y, x4]))] === 0,
  "nabla_mu T^mu_x4 = -d_x4 rho - 3 a4' (p3 - p_t) for diagonal T: dE/dx4 = -3 a4' Integral sqrt|g| (p3 - p_t)"];
addCheck["adiabatic_hellmann_feynman",
  Simplify[D[e0[k Exp[-aa]], aa] + k D[e0[k Exp[-aa]], k]] === 0 && Simplify[D[hfull[1, k, aa], aa] + k D[hfull[1, k, aa], k]] == ConstantArray[0, {2, 2}],
  "d_a h_j = -j kappa k sigma3 = -k d_k h_j; eps(k, a) = eps(k E^(-a), 0): d eps/da = -k d eps/dk (frozen potentials)"];
Module[{Hx = 2 {{Cos[al], Sin[al]}, {Sin[al], -Cos[al]}} + id2, va, vb},
  va = {Cos[al/2], Sin[al/2]}; vb = {-Sin[al/2], Cos[al/2]};
  addCheck["adiabatic_offdiagonal_identity",
    Simplify[Hx.va == 3 va] && Simplify[Hx.vb == -vb] && Simplify[va.D[Hx, al].vb == (-1 - 3) va.D[vb, al]],
    "<n| d_a h |m> = (eps_m - eps_n) <n| d_a m> (explicit family); Q_nm = A H |<n| d_a h_KS |m>|/(eps_n - eps_m)^2 along the history a4 = A H x4, a PRESCRIBED BACKGROUND (test field without back-reaction, not a solution of the a4 equations with the Kohn-Sham source)"]];

(* brane-band slope: exact formula and NDSolve shooting *)
cExact = Exp[-aa] (2 M/(2 M - H)) (1 - Exp[-(2 M - H) L])/(1 - Exp[-2 M L]);
cInt = Integrate[Exp[-H y - aa] Exp[2 M y], {y, -L, 0}]/Integrate[Exp[2 M y], {y, -L, 0}];
okCsym = Simplify[(cInt - cExact) /. {M -> 1, H -> 1, L -> 3}] === 0 && Simplify[(cExact /. {M -> 1, H -> 1, L -> 3, aa -> 0}) - 2/(1 + Exp[-3])] === 0;
shootB[e_?NumericQ, kk_?NumericQ, a_?NumericQ] := Module[{sol, ee = SetPrecision[e, 30]},
  sol = NDSolveValue[{aF'[yy] == aF[yy] - (Exp[-yy - a] kk + ee) bF[yy], bF'[yy] == (ee - Exp[-yy - a] kk) aF[yy] - bF[yy],
      aF[0] == 1, bF[0] == 0}, bF[-3], {yy, -3, 0}, WorkingPrecision -> 25, PrecisionGoal -> 18, AccuracyGoal -> 20,
      MaxSteps -> 10^6];
  sol];
zm[kk_, a_] := e /. FindRoot[shootB[e, kk, a], {e, SetPrecision[19/10 kk Exp[-a], 25]}, WorkingPrecision -> 25, AccuracyGoal -> 20, PrecisionGoal -> 18];
slopeNum[a_] := Module[{s2k, s1k},
  s2k = (zm[2*^-3, a] - zm[-2*^-3, a])/(4*^-3); s1k = (zm[1*^-3, a] - zm[-1*^-3, a])/(2*^-3);
  (4 s1k - s2k)/3];
sl0 = slopeNum[0]; sl5 = slopeNum[1/2];
cE0 = N[cExact /. {M -> 1, H -> 1, L -> 3, aa -> 0}, 25]; cE5 = N[cExact /. {M -> 1, H -> 1, L -> 3, aa -> 1/2}, 25];
addCheck["brane_band_slope", okCsym && Abs[sl0 - cE0] < 10^-8 && Abs[sl5 - cE5] < 10^-8,
  "d eps/dk at k = 0 = j c, c = E^(-a4,0) (2M/(2M-H)) (1 - E^(-(2M-H)L))/(1 - E^(-2ML)); M = H = 1, L = 3: c = 2/(1+E^-3) = " <>
  num[cE0] <> "; NDSolve shooting (WorkingPrecision 25, k = +-1e-3, +-2e-3, Richardson): " <> num[sl0, 12] <> " (a4,0 = 0), " <>
  num[sl5, 12] <> " (a4,0 = 1/2; exact " <> num[cE5, 12] <> ")"];

(* ---------------- ks-theory.json ---------------- *)
jsonTheory = <|
  "description" -> "Revision Kohn-Sham theory for dirac16complex in the author's primordial field (SPEC sections 1, 7): the exact reduction, functional, boundary conditions, rescaling identity, energy-momentum tensor and adiabaticity measure, i.e. the formulas the Rust solver Revision/kohn_sham/solver must implement. Every statement here is checked in Revision/kohn_sham/reports/ks-theory-wolfram.json and independently in ks-theory-python.json.",
  "producer" -> "Revision/kohn_sham/theory/verify_ks_theory.wls",
  "coordinates" -> "x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time; x5, x6, x7 = the three exponentially DEFLATING extra times (scale factor e^{-a4} sin^{1/6} z, a4 increasing); x8 = the hidden direction, z = 6 H x8 in (0, pi/2). Arrays index x1..x8 as 0..7. Gamma matrices: Revision/algebra/gammas.json (gamma^(x8) = T16[0], ...).",
  "units" -> "H = 1 in the solver unless stated; energies, momenta and temperatures in units of m (or H); lambda has dimension mass^-6 (Psi has dimension 7/2 in 8 dimensions).",
  "geometry" -> <|
    "hiddenCoordinate" -> "y = ln(sin z)/(6H) in (-inf, 0], sin z = e^{6Hy}, dy = cot z dx8; the patch end z = pi/2 is y = 0, the tip z -> 0 is y -> -inf",
    "lineElement" -> "ds^2 = e^{2Hy}[e^{2a4(x4)}(dx1^2+dx2^2+dx3^2) - e^{-2a4(x4)}(dx5^2+dx6^2+dx7^2)] - dx4^2 + dy^2",
    "warp" -> "W(y) = e^{Hy}",
    "sqrtDetG" -> "e^{6Hy} (= cos z in the x8 chart); independent of a4: the 7-volume is constant",
    "kappa" -> "kappa(y, x4) = e^{-Hy - a4(x4)} (the momentum weight)",
    "spinConnection" -> "gamma^mu Omega_mu = 3H gamma^(x8) for every a4(x4): the a4' pieces of the 3 inflating directions (+(3/2) a4' gamma^(x4)) and of the 3 deflating directions (-(3/2) a4' gamma^(x4)) cancel"|>,
  "sectorAndAnsatz" -> <|
    "sector" -> "good sector: no dependence on x5, x6, x7 (extra-time momenta zero); coordinate 3-torus of size ell, k in (2 pi/ell) Z^3 = Delta k Z^3; extra-time coordinate volume v_t",
    "exactReduction" -> "Psi = e^{i k.x} W^{-3} chi(y, x4) gives EXACTLY (a4 time-dependent) g8 d_y chi + g4 d_x4 chi + i kappa k.gamma chi = (M_eff - i v_v g4) chi, i.e. i d_x4 chi = h(x4) chi with h Hermitian in int dy chi^dag chi; the factor W^{-3} removes 3H gamma^(x8)",
    "instantaneousProblem" -> "at a fixed instant x4 the instantaneous (adiabatic) Kohn-Sham problem is h(a4,0) chi = eps chi with a4,0 = a4(x4): the stationary-slice ansatz Psi = e^{-i eps x4} e^{i k.x} W^{-3} V_beta chi(y)/sqrt(ell^3 v_t), normalised int_{-L}^{0} chi^dag chi dy = 1",
    "orbital16" -> "Psi_16 = e^{-i eps x4} e^{i k x1} e^{-3Hy} V[:, 2beta:2beta+2] chi(y)/sqrt(ell^3 v_t) for k = (k,0,0); other directions by the spinor rotation"|>,
  "blockBasis" -> <|
    "commutingSet" -> "J = g8 g1 g4 (J^2 = 1), K1 = g2 g3, K2 = g5 g6 (K^2 = -1)",
    "projectors" -> "P(j,s2,s3) = (1+jJ)/2 (1-i s2 K1)/2 (1-i s3 K2)/2",
    "construction" -> "v+ = 8 P(j,s2,s3)(1+g8)/2 e_c (first column c with nonzero image), v- = g8 g1 v+; V = [v+ v- ...]/(2 sqrt 2), unitary",
    "labels" -> (ToString /@ # & /@ labels),
    "labelOrder" -> "beta = 0..7 for (j,s2,s3) = (1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)",
    "seedColumns0Based" -> bb["seeds"],
    "unnormalisedColumns2Sqrt2V" -> Map[ToString, U, {2}],
    "rowsAre" -> "spinor components Psi_0..Psi_15; columns v+, v- of block 0, then block 1, ..."|>,
  "blockForms" -> <|
    "gamma^(x8)" -> "sigma3", "gamma^(x8)gamma^(x1)" -> "-i sigma2", "gamma^(x8)gamma^(x4)" -> "j sigma1",
    "B" -> "j s2 (a number)", "C" -> "s2 sigma2", "BC = -i gamma^(x4)" -> "j sigma2", "gamma^(x4)gamma^(x1)" -> "-j sigma3",
    "B gamma^(x8)" -> "j s2 sigma3", "J" -> "j", "K1" -> "i s2", "K2" -> "i s3",
    "Gamma" -> "anticommutes with J, commutes with K1, K2: maps block (j,s2,s3) onto (-j,s2,s3), 2x2 entry s2 sigma2; on the reduced problem sigma2 h_j(M,k) sigma2 = h_{-j}(-M,k) and the brane parities are exchanged (chi2(0)=0 <-> chi1(0)=0)"|>,
  "blockEquation" -> <|
    "hamiltonian" -> "h_j = j[-i sigma1 d/dy + M_eff(y) sigma2 + kappa(y) k sigma3] + v_v(y), k signed along x1",
    "ode" -> "chi' = N chi, N = M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1",
    "realForm" -> "chi = (a, i b), a, b real: a' = M_eff a - (kappa k + j(eps - v_v)) b, b' = (j(eps - v_v) - kappa k) a - M_eff b",
    "realFormDensities" -> "chi^dag chi = a^2 + b^2; chi^dag sigma2 chi = 2ab; chi^dag sigma3 chi = a^2 - b^2; chi^dag sigma1 chi = 0",
    "typeRelation" -> "h_{-1} - v = -(h_{+1} - v); sigma3 h_j(k) sigma3 = h_{-j}(-k): the (j,k) and (-j,-k) orbitals are degenerate with chi_{-j,-k} = sigma3 chi_{j,k}",
    "degeneracy" -> "for a lattice shell |k|^2 = Delta k^2 n2 with r3(n2) vectors: every level of h_j(|k|), j = +1 and j = -1 separately, is 4 r3(n2)-fold (4 blocks s2, s3 times the r3 directions); at k = 0 every level is 4-fold per j, 8-fold in total",
    "rotation" -> "spectra depend on |k| only (spinor rotation commutes with g8, g4, B, C)"|>,
  "exchange" -> <|
    "interaction" -> "U = (lambda/2) S^2, S = Psibar Psi = Psi^dag C Psi, normal ordered; lambda > 0 repulsive",
    "expectationRule" -> "<Psi^dag M Psi> = Tr(M rho), rho = sum_occ f u u^dagger B (SPEC section 6); quasi-free (Slater / Mermin) states",
    "wick" -> "<:S^2:> = (Tr C rho)^2 - Tr(C rho C rho)",
    "uniformGas" -> <|
      "result" -> "any p -> -p symmetric occupation of the 8-fold good-sector gas (any temperature): rho = (n B + S C)/16; e_H = (lambda/2) S^2, e_x = -(lambda/32)(n^2 + S^2)",
      "coefficient_n2" -> "-1/32", "coefficient_S2" -> "-1/32",
      "filledShellRatio" -> "E_x/E_H = -1/8 for one filled level at rest (n = S)"|>,
    "kohnShamPotentials" -> <|
      "e_int" -> "e_int(n, S) = (15/32) lambda S^2 - (1/32) lambda n^2 (proper densities)",
      "Meff" -> "M_eff(y) = m + (15/16) lambda S(y)", "Meff_coefficient_of_lambda_S" -> "15/16",
      "vv" -> "v_v(y) = -lambda n(y)/16 (added to h as v_v times the identity)", "vv_coefficient_of_lambda_n" -> "-1/16",
      "onShellLagrangian" -> "<L>/sqrt|g| = e_int (degree-2 homogeneity)",
      "correlation" -> "none (Hartree plus exchange only)"|>,
    "exactFockSlab" -> <|
      "result" -> "for closed shells (k -> -k symmetric), equal occupation of the 4 blocks of each type and of the (j,k)/(-j,-k) partners, the EXACT Fock exchange of the Kohn-Sham determinant is local: e_x^exact = -(lambda/32)(n^2 + S^2 - Q^2 - Y^2), Q = <Psi^dag B gamma^(x8) Psi> = sum over orbitals of w g f q_o, q_o = e^{-6Hy} chi^dag sigma3 chi/(ell^3 v_t) for every orbital of either type (= j t_o; (a^2 - b^2) P in the real form), Y = y-current (0)",
      "status" -> "DIAGNOSTIC: the canonical functional is the uniform-gas one (SPEC section 7); the solver should report Delta E_x = +(lambda/32) int sqrt|g| Q^2 (the part the uniform-gas exchange omits). An exact-exchange variant would add w_Q = +lambda Q/16 sigma3 (both block types) to h and +(lambda/32) Q^2 to e_int."|>|>,
  "densities" -> <|
    "perOrbital" -> "with P(y) = e^{-6Hy}/(ell^3 v_t): n_o = P chi^dag chi, s_o = P chi^dag j sigma2 chi, t_o = P chi^dag j sigma3 chi (current along k-hat), q_o = P chi^dag sigma3 chi (= j t_o), c_o = P chi^dag j sigma1 chi = 0",
    "total" -> "n(y) = sum_levels w g f n_o, S(y) = sum w g f s_o (same for t, q), g = 4 r3(n2), f the occupation, w = w_Z2 = 1/2: canonical convention = the doubled (universe + mirror image) system of the ASSUMED Z2 orbifold; its eigen-orbitals are the even- and odd-parity solutions, each normalised on the patch int_{-L}^{0} chi^dag chi dy = 1 (norm 2 on the doubled interval, hence w = 1/2 per patch); N = sum g f over both parities is the particle number of the doubled system (N/2 per copy)",
    "proper" -> "all densities are proper (per proper 7-volume); coordinate densities are e^{6Hy} times them"|>,
  "boundaryConditions" -> <|
    "brane" -> <|"status" -> "ASSUMED", "statement" -> "Z2 mirror (orbifold) at y = 0 under P_A: Psi(-y) = +-gamma^(x8) Psi(y) with the mirror warp W = e^{-H|y|}; continuity gives (1 -+ gamma^(x8)) chi(0) = 0: even parity chi2(0) = 0 (b(0) = 0), odd parity chi1(0) = 0 (a(0) = 0). P_A maps (M(y), v(y)) to (-M(-y), v(-y)): the doubled problem is P_A-symmetric iff M_eff is odd, i.e. the mirror copy carries (-m, +lambda) (S odd, n even). Both parities are the two P_A sectors of the doubled system and are solved and filled together. Both conditions kill the y-current."|>,
    "tip" -> <|"status" -> "chosen (regular tip)", "statement" -> "at y = -L: (1 - Q(theta)) chi(-L) = 0, Q = cos(theta) sigma3 + sin(theta) sigma2; canonical theta = 0: chi2(-L) = 0 (b(-L) = 0). For k = 0 it admits the regular brane-localised zero mode (e^{My}, 0) for every L and no tip-localised mode for M > 0; for k != 0 an orbital is suppressed toward the tip like exp(-|k|(kappa(-L) - kappa(y))/H) so the levels do not depend on theta up to that factor."|>,
    "selfAdjointness" -> "phi^dag h chi - (h phi)^dag chi = d/dy[-i j phi^dag sigma1 chi]; with current-killing ends h_j is self-adjoint, levels real, orbitals orthogonal",
    "exactK0Spectra" -> "constant M > 0, v = 0, theta = 0: even: eps = 0 with chi = (e^{My}, 0), and eps = +-sqrt(M^2 + (n pi/L)^2); odd: eps = +-sqrt(M^2 + p^2) with tan(pL) = -p/M"|>,
  "rescalingIdentity" -> "a4,0 enters only through kappa k = e^{-Hy}(k e^{-a4,0}): KS(a4,0; Delta k, v_t, lambda, N, T) = KS(0; Delta k e^{-a4,0}, v_t e^{-3 a4,0}, lambda, N, T) exactly (levels, orbitals, proper densities, EMT profiles); equivalently KS(0; Delta k e^{-a4,0}, v_t, lambda e^{3 a4,0}) with every proper density times e^{-3 a4,0} and the same levels. The 3-momenta redshift as k e^{-a4} while the proper box stays the same.",
  "thermodynamics" -> <|
    "fillingConvention" -> "CONVENTION (not derived here; SPEC section 6 fixes particles as positive-frequency modes of the normal-ordered good sector): particles occupy the positive branch, i.e. the levels with eps > 0 of the lambda = 0 problem together with the k = 0 brane zero modes (eps = 0 at v = 0), each followed continuously as lambda is switched on; the negative branch is the normal-ordered sea and contributes nothing to N, n, S or T. The zero modes are self-conjugate at k = 0, v = 0 (spectrum of h_{+1} - v is minus that of h_{-1} - v); counting them as particle levels is the stated convention, its justification is OPEN.",
    "occupation" -> "f = 1/(1 + exp((eps - mu)/T)), mu fixed by sum w_Z2 g f = N (Mermin)",
    "energy" -> "E_KS (doubled system) = sum g f eps - 2 Vol_7 int_{-L}^{0} e^{6Hy} e_int dy, Vol_7 = ell^3 v_t; per copy one half of it",
    "entropy" -> "S_ent = -sum g [f ln f + (1-f) ln(1-f)]",
    "grandPotential" -> "Omega = -T sum g ln(1 + exp(-(eps - mu)/T)) - 2 Vol_7 int_{-L}^{0} e^{6Hy} e_int dy (doubled system); F = Omega + mu N"|>,
  "emt" -> <|
    "definition" -> "T^mu_nu = -<K^mu_nu> + delta^mu_nu <L>/sqrt|g>, K_mu nu = (1/4)[Psibar g_(mu D_nu) Psi - D_(nu Psibar g_mu) Psi] (symmetrised), <L>/sqrt|g| = e_int on shell; rho = -T^x4_x4, p_mu = T^mu_mu (SPEC section 4; homogeneous classical limit rho = mS + U, p = S U' - U)",
    "rho" -> "rho(y) = sum w g f eps n_o - e_int",
    "p3" -> "p3(y) = sum w g f (kappa |k|/3) t_o + e_int (shell-averaged; exact for every k -> -k closed cubic shell)",
    "p_t" -> "p_t(y) = e_int (good sector: no extra-time kinetic pressure)",
    "p8" -> "p8(y) = sum w g f [(eps - v_v) n_o - M_eff s_o - kappa |k| t_o] + e_int",
    "offDiagonal" -> "T^x4_y = 0 for eigen-orbitals (K_x4y = P (eps - v/2) c_o, c_o = 0)",
    "trace" -> "sum of the diagonal kinetic parts = M_eff S + v_v n per point",
    "conservationY" -> "p8' + 6H p8 = 3H (p3 + p_t) for every self-consistent state (nabla_mu T^mu_y = 0): solver check",
    "energyChange" -> "nabla_mu T^mu_x4 = -d_x4 rho - 3 a4' (p3 - p_t): dE/da4 = -3 (2 Vol_7) int_{-L}^{0} e^{6Hy} (p3 - p_t) dy; Hellmann-Feynman with fixed occupations gives the same (solver check)",
    "integrated" -> "2 Vol_7 int_{-L}^{0} e^{6Hy} rho dy = E_KS; 2 Vol_7 int_{-L}^{0} e^{6Hy} 3 (p3 - e_int) dy = sum g f |k| d eps/d|k| (doubled system, w = 1/2 in the densities)"|>,
  "adiabaticity" -> <|
    "history" -> "a4 = A H x4 (A = 1 canonical), a4' = A H; slices a4,0 = a4(x4); PRESCRIBED BACKGROUND (see historyStatus)",
    "historyStatus" -> "PRESCRIBED BACKGROUND: the history a4 = A H x4 is prescribed, not solved for. The a4 equations of SPEC section 5 allow this linear member only with p3 = p_t = p8 and constant rho; the Kohn-Sham states along it violate these source conditions (p3 != p_t, rho changes with a4,0, the sources depend on x8: Revision/field_equations_a4/reports/ks-source-conditions.json). The Kohn-Sham gas is therefore a test field on a prescribed background without back-reaction, and quantities derived along this history (energies, pressures, equations of state) are not consequences of the coupled field equations.",
    "exactEvolution" -> "i d_x4 chi = h(a4(x4)) chi (mean field); k, the block and the brane parity are conserved; transitions only between levels of the same (k, j, block, parity)",
    "derivative" -> "d_a h_j = -j kappa k sigma3 (frozen potentials) + j (d_a M_eff) sigma2 + d_a v_v (self-consistent part, by finite differences between slices)",
    "measure" -> "Q_nm = A H |<n| d_a h |m>| / (eps_n - eps_m)^2 = A H |<n| d_a m>| / |eps_n - eps_m| for n occupied, m empty in the same sector; adiabatic iff max Q_nm << 1; leading-order transition probability ~ Q_nm^2",
    "hellmannFeynman" -> "d eps_n/da = <n| d_a h |n> = -k d eps_n/dk (frozen) ",
    "caveat" -> "adiabatic evolution conserves the occupation of every (k, j, block, parity, level); when levels of different k cross the Fermi level between slices, the instantaneous aufbau ground state differs from the adiabatically continued state: the solver should flag such crossings. The non-adiabatic (time-dependent) problem is OPEN."|>,
  "checksNumeric" -> <|
    "braneBandSlope_M1_H1_L3_a0" -> num[cE0, 17],
    "braneBandSlopeFormula" -> "c = e^{-a4,0} (2M/(2M-H)) (1 - e^{-(2M-H)L})/(1 - e^{-2ML}), d eps_0/dk = j c at k = 0 (even parity, theta = 0)"|>,
  "solverChecklist" -> {
    "free k = 0 spectra (even: 0, sqrt(M^2+(n pi/L)^2); odd: tan(pL) = -p/M)",
    "brane-band slope c at small k",
    "j-type mirror symmetry of the spectra (v = 0) and 4 r3(n2) degeneracy",
    "exact rescaling identity between slices (a4,0 vs Delta k e^{-a4,0}, v_t e^{-3a4,0})",
    "N conservation and the orbital normalisation",
    "y-conservation p8' + 6H p8 = 3H(p3 + p_t) of every self-consistent state",
    "trace identity and T^x4_y = 0 (zero y-current of every orbital)",
    "dE/da4 = -6 Vol_7 int_{-L}^{0} e^{6Hy}(p3 - p_t) dy (doubled system) by finite differences between slices (fixed occupations)",
    "exact-Fock diagnostic Delta E_x = (lambda/32) 2 Vol_7 int_{-L}^{0} e^{6Hy} Q^2 dy"}
|>;

ksJson = ExportString[jsonTheory, "RawJSON"];
ksJson2 = ExportString[jsonTheory, "RawJSON"];
writeLF[path_, text_String] := Module[{s = OpenWrite[path, BinaryFormat -> True, CharacterEncoding -> "UTF-8"]},
  BinaryWrite[s, ToCharacterCode[StringReplace[text, "\r\n" -> "\n"], "UTF-8"]]; Close[s]];
writeLF[FileNameJoin[{$ks, "ks-theory.json"}], If[StringEndsQ[ksJson, "\n"], ksJson, ksJson <> "\n"]];
back = Import[FileNameJoin[{$ks, "ks-theory.json"}], "RawJSON"];
addCheck["ks_theory_json_written",
  ksJson === ksJson2 && back["blockBasis"]["unnormalisedColumns2Sqrt2V"] == Map[ToString, U, {2}] &&
  ToExpression[back["exchange"]["uniformGas"]["coefficient_n2"]] == -1/32 &&
  StringStartsQ[back["adiabaticity"]["historyStatus"], "PRESCRIBED BACKGROUND"] &&
  StringContainsQ[back["adiabaticity"]["history"], "PRESCRIBED BACKGROUND"],
  "ks-theory.json written deterministically (two exports identical, LF) and re-imported: basis, coefficients and the label of the history a4 = A H x4 as a PRESCRIBED BACKGROUND (adiabaticity.history, adiabaticity.historyStatus) round-trip"];

(* ---------------- report ---------------- *)
jstr[s_String] := "\"" <> StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\""}] <> "\"";
nPass = Count[checks, c_ /; c["verdict"] == "PASS"]; nTot = Length[checks];
report = StringJoin[
  "{\n",
  "  \"report\": ", jstr["Revision Kohn-Sham theory (SPEC sections 1, 7): exact derivation and checks in WolframScript"], ",\n",
  "  \"producer\": ", jstr["Revision/kohn_sham/theory/verify_ks_theory.wls"], ",\n",
  "  \"package\": ", jstr["Revision/kohn_sham/theory/KohnShamTheory.wl"], ",\n",
  "  \"export\": ", jstr["Revision/kohn_sham/ks-theory.json"], ",\n",
  "  \"coordinates\": ", jstr["x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; x8 = the hidden direction (y = ln(sin 6Hx8)/(6H) <= 0)"], ",\n",
  "  \"summary\": {\"passed\": ", ToString[nPass], ", \"failed\": ", ToString[nTot - nPass], ", \"total\": ", ToString[nTot], "},\n",
  "  \"checks\": [\n",
  StringRiffle[("    {\"name\": " <> jstr[#["name"]] <> ", \"verdict\": " <> jstr[#["verdict"]] <> ", \"detail\": " <> jstr[#["detail"]] <> "}") & /@ checks, ",\n"],
  "\n  ]\n}\n"];
writeLF[FileNameJoin[{$ks, "reports", "ks-theory-wolfram.json"}], report];
Print[nPass, "/", nTot, " checks passed; time ", Round[AbsoluteTime[] - t0, 0.1], " s"];
Exit[If[nPass == nTot, 0, 1]];
