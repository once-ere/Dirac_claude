#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_scope.wls

   Exact WolframScript checks of the SCOPE of the statements of the field-theory record (Revision/SPEC.md
   sections 1-6) in the CORRECTED primordial metric of 2026-10-16 (version 2; Revision/metric_warped/):
     g = diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3)),  z = 6 H x0 real,
   general a4(x4) and b4(x4) > 0, EVERY real z (the user's rules of 2026-10-16: -Infinity < z < Infinity,
   Sin[z]^(1/3) = (Sin[z]^2)^(1/6)): which values depend on the choice of frame and of field variables, what holds only
   up to boundary terms, and what the indefinite structures imply.  (Until 2026-10-16 this file treated the metric of
   2026-10-14 on 0 < z < Pi/2, withdrawn.)  Written anew for Revision; it does not load
   Revision/theory/wolfram/RevisionFieldTheory.wl and shares no code with the sympy checker
   Revision/theory/python/check_scope.py.  Writes, deterministically (LF, no time stamps):
     Revision/theory/reports/wolfram-scope.json
   Usage:  wolframscript -file Revision/theory/wolfram/verify_scope.wls
   Exit code 0 if every check passes, 1 otherwise.

   Coordinates as the author names them, in the author's order x0..x7 (Wolfram position k + 1 holds xk): x0 = the hidden,
   space-like direction; x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the three extra times, which DEFLATE
   (scale factor E^-a4 b4^(1/2) (Sin[z]^2)^(1/12); the hidden direction shares the factor E^-a4 b4^(1/2)).
   sqrt|g| = sgn E^-a4 b4^2 Cot[z] (Sin[z]^2)^(1/4), sgn = sign(Cot z) = +-1 (a symbol with sgn^2 = 1, constant between
   the degenerate points z = n Pi/2).

   Exact zero test (own code): Cosh and Sinh are written with exponentials; Sin[z] -> s1, Cos[z] -> c1 (signed),
   (Sin[z]^2)^k -> ww^(12 k) (ww = (Sin[z]^2)^(1/12) > 0); the numerator is reduced modulo c1^2 + s1^2 - 1,
   ww^12 - s1^2 and sgn^2 - 1 (a Groebner basis: the leading terms are coprime); real functions and complex
   conjugates are expanded with ComplexExpand where needed.
*)

$here = DirectoryName[$InputFileName];
$revDir = ExpandFileName[FileNameJoin[{$here, "..", ".."}]];
t0 = AbsoluteTime[];
checks = {};
addCheck[name_String, ok_, detail_String] := (
  AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS  ", "FAIL  "], name, "  [", Round[AbsoluteTime[] - t0, 0.1], " s]"]);

(* ------------------------------------------------------------------ the gammas of Revision/algebra/gammas.json *)
fx = Import[FileNameJoin[{$revDir, "algebra", "gammas.json"}], "RawJSON"];
num[x_String] := ToExpression[x]; num[x_] := x;
dec[x_Association] := Map[num, x["re"], {2}] + I Map[num, x["im"], {2}];
dec[x_List] := Map[num, x, {2}];
g = dec /@ fx["gamma"]; Cm = dec[fx["C"]]; Bm = dec[fx["B"]];
eta = DiagonalMatrix[{1, 1, 1, 1, -1, -1, -1, -1}];
id16 = IdentityMatrix[16]; z16 = ConstantArray[0, {16, 16}];
sAB = Table[(g[[a]] . g[[b]] - g[[b]] . g[[a]])/4, {a, 8}, {b, 8}];
X = {x0, x1, x2, x3, x4, x5, x6, x7};   (* positions: x0 = 1, x4 = 5 *)
z = 6 H x0;
bu = Derivative[1][b4][x4]/b4[x4];   (* b4'/b4 *)
a4p = Derivative[1][a4][x4];
cg = (3/2) H E^a4[x4]/Sqrt[b4[x4]];  (* the gamma^(x0) coefficient of gamma^mu Omega_mu in the diagonal frame *)
vg = bu - a4p/2;                     (* its gamma^(x4) coefficient *)

(* ------------------------------------------------------------------ exact zero test (every real z) *)
hyp = {Cosh[a_] :> (E^a + E^-a)/2, Sinh[a_] :> (E^a - E^-a)/2};
trig = {(Sin[6 H x0]^2)^k_ :> ww^(12 k), Sin[6 H x0] -> s1, Cos[6 H x0] -> c1, Cot[6 H x0] -> c1/s1, Tan[6 H x0] -> s1/c1,
  Csc[6 H x0] -> 1/s1, Sec[6 H x0] -> 1/c1, Sin[12 H x0] -> 2 s1 c1, Cos[12 H x0] -> c1^2 - s1^2};
gb = {c1^2 + s1^2 - 1, ww^12 - s1^2, sgn^2 - 1};
zq[e_] := Module[{t = Together[(e /. hyp) /. trig], nm},
  nm = Expand[Numerator[t]];
  nm === 0 || Last[PolynomialReduce[nm, gb, {c1, ww, sgn, s1}]] === 0];
mzq[M_] := AllTrue[Flatten[M], zq];
addCheck["zero_test_controls",
  zq[Sin[z]^2 + Cos[z]^2 - 1] && !zq[(Sin[z]^2)^(1/2) - Sin[z]] && zq[((Sin[z]^2)^(1/12))^12 - Sin[z]^2] && zq[sgn^2 - 1] && !zq[sgn - 1] &&
  zq[Cosh[bb]^2 - Sinh[bb]^2 - 1] && !zq[Cosh[bb] - 1],
  "the exact zero test of this file returns True on identities and False on nonzero expressions: (Sin z^2)^(1/2) - Sin z is not zero (no sign of Sin z is assumed), w^12 - Sin^2, sgn^2 - 1, Cosh^2 - Sinh^2 - 1 are zero, sgn - 1 and Cosh - 1 are not"];
addCheck["fixture_gammas",
  And @@ Flatten[Table[g[[a]] . g[[b]] + g[[b]] . g[[a]] == 2 eta[[a, b]] id16, {a, 8}, {b, 8}]] &&
  Cm == g[[1]] . g[[2]] . g[[3]] . g[[4]] && Bm == -I Cm . g[[5]],
  "gammas.json: {gamma^a, gamma^b} = 2 eta^ab I16 (eta = diag(1,1,1,1,-1,-1,-1,-1), order x0..x7), C = gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3), B = -i C gamma^(x4)"];

(* ------------------------------------------------------------------ geometry of a vielbein e^a_mu (rows a) *)
sb = E^-a4[x4] Sqrt[b4[x4]];
w12 = (Sin[z]^2)^(1/12);
fd = {sb Cot[z], E^a4[x4], E^a4[x4], E^a4[x4], 1, sb w12, sb w12, sb w12};
gMetric = DiagonalMatrix[Diagonal[eta] fd^2];
gInv = DiagonalMatrix[1/Diagonal[gMetric]];
chr = Table[Together[Sum[gInv[[l, r]] (D[gMetric[[r, n]], X[[mm]]] + D[gMetric[[r, mm]], X[[n]]] - D[gMetric[[mm, n]], X[[r]]])/2, {r, 8}]],
  {l, 8}, {mm, 8}, {n, 8}];
(* boost of the frame in the (x4, x0) plane: frame positions x4 = 5, x0 = 1 *)
boostL[bb_] := ReplacePart[IdentityMatrix[8], {{5, 5} -> Cosh[bb], {5, 1} -> Sinh[bb], {1, 5} -> Sinh[bb], {1, 1} -> Cosh[bb]}];
frame[bb_] := Module[{e, Ei, om, omL, Om, gam},
  e = boostL[bb] . DiagonalMatrix[fd];
  Ei = DiagonalMatrix[1/fd] . Inverse[boostL[bb]] /. {Cosh[x_]^2 - Sinh[x_]^2 -> 1};   (* Ei[[mu, a]] = e_a^mu *)
  Ei = Map[Simplify[# /. hyp] &, Ei, {2}];
  om = Table[Together[Sum[e[[a, nu]] (D[Ei[[nu, b]], X[[mu]]] + Sum[chr[[nu, mu, l]] Ei[[l, b]], {l, 8}]), {nu, 8}] /. hyp],
    {mu, 8}, {a, 8}, {b, 8}];                                (* omega_mu^a_b *)
  omL = Table[eta[[a, a]] om[[mu, a, b]], {mu, 8}, {a, 8}, {b, 8}];
  Om = Table[Sum[omL[[mu, a, b]] sAB[[a, b]], {a, 8}, {b, a + 1, 8}], {mu, 8}];
  gam = Table[Sum[Ei[[mu, a]] g[[a]], {a, 8}], {mu, 8}];
  <|"e" -> e, "Ei" -> Ei, "om" -> om, "omL" -> omL, "Om" -> Om, "gam" -> gam|>];
postulateFailures[fr_] := Count[Flatten[Table[
    zq[D[fr["e"][[a, nu]], X[[mu]]] - Sum[chr[[l, mu, nu]] fr["e"][[a, l]], {l, 8}] + Sum[fr["om"][[mu, a, b]] fr["e"][[b, nu]], {b, 8}]],
    {a, 8}, {mu, 8}, {nu, 8}]], False];
gammaOmega[fr_] := Sum[fr["gam"][[mu]] . fr["Om"][[mu]], {mu, 8}];
coef[M_, a_] := Together[Tr[g[[a]] . M]/(16 eta[[a, a]])];

(* ================================================================== 1. frame dependence *)
frB = frame[beta x4 + b0];
addCheck["boosted_frame_reproduces_metric",
  mzq[Transpose[frB["e"]] . eta . frB["e"] - gMetric] && mzq[frB["e"] . frB["Ei"] - IdentityMatrix[8]],
  "frame boosted in the (x4, x0) plane with rapidity b = beta x4 + b0: e'^(x4) = Cosh[b] e^(x4) + Sinh[b] e^(x0), e'^(x0) = Sinh[b] e^(x4) + Cosh[b] e^(x0), the other e'^(a) = e^(a) of the diagonal vielbein " <>
  "(f0 = E^-a4 b4^(1/2) Cot z, f_i = E^a4, f_t = E^-a4 b4^(1/2) (Sin z^2)^(1/12)); e'^T eta e' equals the corrected metric for all 64 entries and every real z"];
nPost = postulateFailures[frB];
addCheck["boosted_frame_canonical_connection",
  nPost == 0 && AllTrue[Flatten[Table[zq[frB["omL"][[mu, a, b]] + frB["omL"][[mu, b, a]]], {mu, 8}, {a, 8}, {b, 8}]], TrueQ],
  "canonical spin connection of the boosted frame (Christoffel symbols computed here from the corrected metric): the vielbein postulate d_mu e'^a_nu - Gamma^lam_mu,nu e'^a_lam + omega_mu^a_b e'^b_nu = 0 holds for all 512 components (" <> ToString[nPost] <> " failures), omega_mu ab antisymmetric"];
totB = gammaOmega[frB];
addCheck["boosted_frame_gammaOmega_formula",
  mzq[totB - ((cg - beta/2) (Cosh[beta x4 + b0] g[[1]] - Sinh[beta x4 + b0] g[[5]]) + vg (Cosh[beta x4 + b0] g[[5]] - Sinh[beta x4 + b0] g[[1]]))] &&
  mzq[gammaOmega[frame[0]] - (cg g[[1]] + vg g[[5]])],
  "gamma'^mu Omega'_mu = (cg - beta/2) (Cosh[b] gamma^(x0) - Sinh[b] gamma^(x4)) + vg (Cosh[b] gamma^(x4) - Sinh[b] gamma^(x0)) exactly for symbolic a4[x4], b4[x4], H, beta, b0, every real z, " <>
  "cg = (3/2) H E^a4 b4^(-1/2), vg = b4'/b4 - a4'/2; control: the same code for the unboosted (diagonal) frame gives cg gamma^(x0) + vg gamma^(x4)"];
(* a general rapidity function bf[x4]: gamma'^mu Omega'_mu = c0 gamma^(x0) + c4 gamma^(x4) with Cosh[b] c4 + Sinh[b] c0 = vg;
   the rapidity bz with bz' = 2 cg removes the cg part (its derivative is substituted) *)
totF = gammaOmega[frame[bf[x4]]];
cF0 = coef[totF, 1]; cF4 = coef[totF, 5];
frZ = frame[bz[x4]];
rZ = {Derivative[2][bz][x4] -> D[2 cg, x4], Derivative[1][bz][x4] -> 2 cg};
totZ = (gammaOmega[frZ] /. rZ) /. rZ;
nzOm = Select[Range[8], ! mzq[(frZ["Om"][[#]] /. rZ)] &];
addCheck["boosted_frame_removes_only_the_H_term",
  mzq[totF - cF0 g[[1]] - cF4 g[[5]]] && zq[Cosh[bf[x4]] cF4 + Sinh[bf[x4]] cF0 - vg] &&
  mzq[totZ - vg (Cosh[bz[x4]] g[[5]] - Sinh[bz[x4]] g[[1]])] && nzOm =!= {} && postulateFailures[frZ] == 0,
  "for a frame boosted in the (x4, x0) plane with ANY rapidity function b(x4): gamma'^mu Omega'_mu = c0 gamma^(x0) + c4 gamma^(x4) with Cosh[b] c4 + Sinh[b] c0 = vg = b4'/b4 - a4'/2 exactly, " <>
  "so gamma'^mu Omega'_mu = 0 forces b4'/b4 = a4'/2 (b4 proportional to E^(a4/2)): for general a4, b4 no boost in this plane removes the spin-connection term. " <>
  "The rapidity with b' = 2 cg = 3 H E^a4 b4^(-1/2) removes the cg part: gamma'^mu Omega'_mu = vg (Cosh[b] gamma^(x4) - Sinh[b] gamma^(x0)) for every H > 0, a4[x4], b4[x4] (exact; b given by its derivative); " <>
  "the value cg gamma^(x0) + vg gamma^(x4) is a property of the diagonal vielbein, its cg part is not a frame-independent part of the field equation. Omega'_mu is nonzero for mu = " <>
  StringRiffle[("x" <> ToString[# - 1]) & /@ nzOm, ", "]];
(* F'_x5x0 in the boosted frame: positions x5 = 6, x0 = 1 *)
F50 = (D[frZ["Om"][[1]], x5] - D[frZ["Om"][[6]], x0] + frZ["Om"][[6]] . frZ["Om"][[1]] - frZ["Om"][[1]] . frZ["Om"][[6]]) /. rZ;
addCheck["boosted_frame_curvature_nonzero",
  ! mzq[F50],
  "in the boosted frame (b' = 2 cg) the spinor curvature F'_x5x0 = d_x5 Omega'_x0 - d_x0 Omega'_x5 + [Omega'_x5, Omega'_x0] is nonzero for general a4, b4: Omega' does not vanish; no frame can make Omega vanish where the metric is curved, " <>
  "because the curvature of the spin connection is (1/2) R_ab,mu,nu S^ab (the corrected metric is flat only for special a4, b4, such as a4 = 0, b4 = H^2 x4^2)"];

(* ================================================================== 2. diagonal frame *)
frD = frame[0];
totD = gammaOmega[frD];
w = E^(a4[x4]/2)/b4[x4] (Sin[z]^2)^(-1/8);
resc = Sum[frD["gam"][[mu]] D[w, X[[mu]]], {mu, 8}] + w totD;
chiF = Table[cf[A] @@ X, {A, 16}];
lhsResc = Sum[frD["gam"][[mu]] . (D[w chiF, X[[mu]]] + frD["Om"][[mu]] . (w chiF)), {mu, 8}] - w Sum[frD["gam"][[mu]] . D[chiF, X[[mu]]], {mu, 8}];
addCheck["rescaling_removes_the_connection_term",
  mzq[totD - (cg g[[1]] + vg g[[5]])] && mzq[resc] && AllTrue[lhsResc, zq],
  "diagonal frame: gamma^mu Omega_mu = cg gamma^(x0) + vg gamma^(x4); for Psi = E^(a4/2) b4^(-1) (Sin z^2)^(-1/8) chi with 16 arbitrary functions chi_A(x0, ..., x7), gamma^mu D_mu Psi - E^(a4/2) b4^(-1) (Sin z^2)^(-1/8) gamma^mu d_mu chi = 0 " <>
  "component by component (computed on the functions themselves, every real z): in the variables chi the field equation has no spin-connection term"];
St = Symbol["St"];
addCheck["rescaled_equation_quadratic_potential",
  zq[lam (w^2 St) - lam St E^a4[x4]/(b4[x4]^2 (Sin[z]^2)^(1/4))],
  "U = (lambda/2) S^2: S[E^(a4/2) b4^(-1) (Sin z^2)^(-1/8) chi] = E^a4 b4^(-2) |Sin z|^(-1/2) S[chi] (the factor is real and positive), so the rescaled equation is gamma^mu d_mu chi = (m + lambda E^a4 S[chi]/(b4^2 |Sin z|^(1/2))) chi: " <>
  "the spin-connection term is removed completely for U = 0 and becomes an x0- and x4-dependent coupling for U != 0"];
riem[r_, s_, mu_, nu_] := D[chr[[r, nu, s]], X[[mu]]] - D[chr[[r, mu, s]], X[[nu]]] + Sum[chr[[r, mu, l]] chr[[l, nu, s]] - chr[[r, nu, l]] chr[[l, mu, s]], {l, 8}];
ricMixed[a_] := Together[Sum[riem[r, a, r, a], {r, 8}] gInv[[a, a]]];
{r44, r11, r00, r55} = ricMixed /@ {5, 2, 1, 6};   (* positions of x4, x1, x0, x5 *)
Cb = H^2 E^(2 a4[x4])/b4[x4];
addCheck["gammaOmega_sees_the_hidden_block",
  !FreeQ[totD, a4] && zq[r44 - (7 a4p^2 - a4''[x4] - 4 a4p bu + 2 b4''[x4]/b4[x4] - bu^2)] && zq[r11 - (-a4p^2 + a4''[x4] + 2 a4p bu)] &&
  zq[r00 - (-3 Cb + a4p^2 - a4''[x4] - (5/2) a4p bu + (1/2) b4''[x4]/b4[x4] + (1/2) bu^2)] && zq[r55 - r00],
  "diagonal frame: gamma^mu Omega_mu = (3/2) H E^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) contains a4 (unlike the metric of 2026-10-14, where it was 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4)): " <>
  "its gamma^(x0) coefficient is (3/2) H times the inverse scale factor E^a4 b4^(-1/2) of the hidden block, which grows as the block deflates; Riemann computed here from the metric: " <>
  "R^x4_x4 = 7 a4'^2 - a4'' - 4 a4' b4'/b4 + 2 b4''/b4 - (b4'/b4)^2, R^x1_x1 = -a4'^2 + a4'' + 2 a4' b4'/b4, R^x0_x0 = R^x5_x5 = -3 Cb + a4'^2 - a4'' - (5/2) a4' b4'/b4 + (1/2) b4''/b4 + (1/2)(b4'/b4)^2, Cb = H^2 E^(2 a4)/b4"];
sqrtg = sgn Times @@ fd;
addCheck["connection_free_lagrangian_same_equations",
  AllTrue[Range[8], mzq[frD["gam"][[#]] . frD["Om"][[#]] + frD["Om"][[#]] . frD["gam"][[#]]] &] &&
  mzq[Sum[D[sqrtg frD["gam"][[mu]], X[[mu]]], {mu, 8}]/(2 sqrtg) - totD],
  "diagonal frame: {gamma^mu, Omega_mu} = 0 for each mu, so the canonical spin connection drops out of the symmetrised Lagrangian (L(Omega) = L(Omega = 0)) and the Euler-Lagrange equations are those of the connection-free symmetric Lagrangian; " <>
  "(1/(2 sqrt|g|)) d_mu(sqrt|g| gamma^mu) = gamma^mu Omega_mu = cg gamma^(x0) + vg gamma^(x4) (sqrt|g| = sgn E^-a4 b4^2 Cot z (Sin z^2)^(1/4)): the half-density term"];
(* positions: x4 = 5, x1 = 2, x5 = 6, x0 = 1 *)
dK1 = (frD["gam"][[5]] . frD["Om"][[2]] + frD["Om"][[2]] . frD["gam"][[5]])/2;
dK5 = (frD["gam"][[5]] . frD["Om"][[6]] + frD["Om"][[6]] . frD["gam"][[5]])/2;
addCheck["spin_connection_in_the_energy_momentum_tensor",
  mzq[dK1] && mzq[dK5 - H w12 g[[5]] . g[[1]] . g[[6]]/2] && Cm . g[[5]] . g[[1]] . g[[6]] != z16,
  "homogeneous configuration Phi(x4), diagonal frame: the connection part of K^x4_x1 = (1/2)(Phibar gamma^x4 D_x1 Phi - D_x1 Phibar gamma^x4 Phi) is (1/2) Phibar {gamma^x4, Omega_x1} Phi = 0 " <>
  "(3-space does not depend on x0 in the corrected metric), but that of K^x4_x5 is (1/2) Phibar {gamma^x4, Omega_x5} Phi = (1/2) H (Sin z^2)^(1/12) Phibar gamma^(x4) gamma^(x0) gamma^(x5) Phi, not identically zero: " <>
  "the canonical spin connection reaches the energy-momentum tensor through the extra times"];

(* ================================================================== 3. Hermiticity only up to the boundary flux *)
uF = Table[ur[A][x0] + I ui[A][x0], {A, 16}]; vF = Table[vr[A][x0] + I vi[A][x0], {A, 16}];
cj[vec_] := ComplexExpand[Conjugate[vec]];
(* positions: x4 = 5, x0 = 1; at k = 0 the mode operator acts on functions of x0 *)
hOp[vec_] := -I m g[[5]] . vec + I g[[5]] . g[[1]] . (E^a4[x4]/Sqrt[b4[x4]] (Tan[z] D[vec, x0] + (3/2) H vec)) - I vg vec;
(* the complex conjugate of h u, written with the conjugated matrices (the coefficient functions are real; ComplexExpand
   is applied to the field components only, so that Sqrt[b4] is not expanded for a b4 of unknown sign) *)
hOpCj[vecc_] := I m Conjugate[g[[5]]] . vecc - I Conjugate[g[[5]] . g[[1]]] . (E^a4[x4]/Sqrt[b4[x4]] (Tan[z] D[vecc, x0] + (3/2) H vecc)) + I vg vecc;
M0 = I g[[5]] . g[[1]];
msr = sqrtg;   (* sqrt|g| *)
lhsH = msr (cj[uF] . hOp[vF] - hOpCj[cj[uF]] . vF) - D[sgn b4[x4]^(3/2) (Sin[z]^2)^(1/4) cj[uF] . M0 . vF, x0] + I D[msr, x4] cj[uF] . vF;
u0 = First[NullSpace[g[[5]] . g[[1]] - id16]];
flux = Simplify[Conjugate[u0] . M0 . u0];
addCheck["good_sector_hermiticity_up_to_the_brane_flux",
  zq[lhsH] && flux =!= 0 && zq[D[msr, x4] - 2 vg msr],
  "curved good-sector mode operator at k = 0, h = -i m gamma^(x4) + i gamma^(x4) gamma^(x0) E^a4 b4^(-1/2) (Tan[z] d_x0 + (3/2) H) - i vg: for arbitrary complex u(x0), v(x0) (32 real functions) and every real z, " <>
  "sqrt|g| (u^dagger h v - (h u)^dagger v) = d_x0 (sgn b4^(3/2) (Sin z^2)^(1/4) u^dagger M0 v) - i (d_x4 sqrt|g|) u^dagger v, M0 = i gamma^(x4) gamma^(x0), exactly; d_x4 sqrt|g| = 2 vg sqrt|g| " <>
  "(the anti-Hermitian term -i vg compensates the x4 dependence of the measure, so d/dx4 Integrate[sqrt|g| u^dagger v] = the x0 boundary term for solutions); the boundary term vanishes where Sin z = 0 but not where Cos z = 0 " <>
  "(|Sin z| = 1, the degenerate points z = Pi/2 + n Pi of g00): for gamma^(x4) gamma^(x0) u = u, u^dagger M0 u = " <> ToString[flux, InputForm] <> " (|u|^2 = " <> ToString[Conjugate[u0] . u0, InputForm] <>
  "). The conservation (symmetry of h for Integrate[sqrt|g| u^dagger v]) holds only with boundary conditions at the degenerate points"];
Aop = -I m g[[5]] + I cg g[[5]] . g[[1]];
AopB = Aop - I vg id16;   (* the mode operator of Psi on x0-independent functions *)
normInt = Integrate[Cot[6 H y] Sqrt[Sin[6 H y]], {y, 0, Pi/(12 H)}, Assumptions -> H > 0];
addCheck["good_sector_x0_independent_modes_without_boundary_condition",
  mzq[Aop . Aop - (m^2 - cg^2) id16] && ! mzq[Aop - ConjugateTranspose[Aop /. Complex[re_, im_] :> Complex[re, -im]]] && normInt == 1/(3 H) &&
  AllTrue[Module[{cv = Table[chf[A][x4], {A, 16}]},
    (I D[E^(a4[x4]/2)/b4[x4] cv, x4] - AopB . (E^(a4[x4]/2)/b4[x4] cv)) /. Table[Derivative[1][chf[A]][x4] -> (-I Aop . cv)[[A]], {A, 16}]], zq],
  "on x0-independent good-sector functions (finite norm on each interval between degenerate points: Integrate[Cot[6 H x0] Sin[6 H x0]^(1/2), {x0, 0, Pi/(12 H)}] = " <> ToString[normInt, InputForm] <>
  ") the curved mode operator of Psi is A - i vg with the matrix A(x4) = -i m gamma^(x4) + i cg gamma^(x4) gamma^(x0), so Psi = E^(a4/2) b4^(-1) chi where chi evolves with A alone (i d4 chi = A chi): " <>
  "A is not Hermitian, A^2 = (m^2 - cg^2) I16 with cg = (3/2) H E^a4 b4^(-1/2): wherever m^2 < cg^2 the instantaneous frequencies are imaginary; on the record's history a4 = H x4, b4 = E^(4 H x4/3) " <>
  "cg = (3/2) H E^(H x4/3) grows, so every mass falls below it at late x4: without a boundary condition at the degenerate points the good sector contains growing modes"];

(* ================================================================== 4. extra-time growth *)
(* kk[[a]] = k_(a-1), the momentum along x(a-1): positions x0 = 1, x4 = 5, x5, x6, x7 = 6, 7, 8 *)
kk = Table[Symbol["k" <> ToString[a - 1]], {a, 8}];
hk = -I m g[[5]] - Sum[If[a == 5, z16, kk[[a]] g[[5]] . g[[a]]], {a, 8}];
e2 = m^2 + kk[[1]]^2 + kk[[2]]^2 + kk[[3]]^2 + kk[[4]]^2 - kk[[6]]^2 - kk[[7]]^2 - kk[[8]]^2;
growth = Sqrt[-(e2 /. {kk[[6]] -> K5, kk[[7]] -> 0, kk[[8]] -> 0})];
addCheck["extra_time_growth_rates_unbounded",
  Expand[hk . hk - e2 id16] == z16 && Limit[growth, K5 -> Infinity] === Infinity,
  "flat 4+4 space (or frozen coefficients): h_k = -i m gamma^(x4) - gamma^(x4) Sum[k_a gamma^(a)] has h_k^2 = (" <> ToString[e2, InputForm] <>
  ") I16; with k5 = K5 the growth rate " <> ToString[growth, InputForm] <> " is unbounded as K5 -> Infinity: the Cauchy problem for data depending on x5, x6, x7 is not well posed in Hadamard's sense, although the slices x4 = const are non-characteristic"];

(* ================================================================== 5. classical energy of dirac16complex00 *)
kv = {4, 1, 2, 0, 0, 0, 0, 0}; mv = 2; ev = 5;   (* (k0, k1, ..., k7) *)
hs = hk /. Thread[kk -> kv] /. m -> mv;
Vp = NullSpace[hs - ev id16];
neg = Select[(Bm - id16) . # & /@ Vp, # =!= ConstantArray[0, 16] &];
pos = Select[(Bm + id16) . # & /@ Vp, # =!= ConstantArray[0, 16] &];
nrm[v_] := v/Sqrt[Simplify[Conjugate[v] . v]];
{uN, uP} = nrm /@ {First[neg], First[pos]};
Y = Table[Symbol["y" <> ToString[a - 1]], {a, 8}];   (* flat coordinates y0..y7; y4 = the time *)
energyAndCharge[u_] := Module[{ph, Phi, Phib, K, S, rho, eq, q},
  ph = Exp[I (Sum[If[a == 5, 0, kv[[a]] Y[[a]]], {a, 8}] - ev Y[[5]])];
  Phi = cc u ph;
  Phib = ComplexExpand[Conjugate[Phi]] . Cm;
  K = Table[(Phib . g[[a]] . D[Phi, Y[[a]]] - (ComplexExpand[Conjugate[D[Phi, Y[[a]]]]] . Cm) . g[[a]] . Phi)/2, {a, 8}];
  S = Phib . Phi;
  rho = Simplify[ComplexExpand[-Total[Delete[K, 5]] + mv S], cc > 0];
  eq = Simplify[Sum[g[[a]] . D[Phi, Y[[a]]], {a, 8}] - mv Phi];
  q = Simplify[ComplexExpand[ComplexExpand[Conjugate[Phi]] . Bm . Phi], cc > 0];
  {rho, eq === ConstantArray[0, 16], q}];
{rN, okN, qN} = energyAndCharge[uN];
{rP, okP, qP} = energyAndCharge[uP];
inertia = Module[{V = Transpose[Vp], ev2}, ev2 = Eigenvalues[ConjugateTranspose[V] . Bm . V]; {Count[ev2, _?Positive], Count[ev2, _?Negative]}];
addCheck["commuting_field_energy_unbounded_below",
  Expand[Bm . hs - hs . Bm] == z16 && Length[Vp] == 8 && inertia == {4, 4} && okN && okP &&
  Simplify[rN + 5 cc^2] === 0 && Simplify[rP - 5 cc^2] === 0 && Simplify[qN + cc^2] === 0 && Simplify[qP - cc^2] === 0,
  "dirac16complex00, flat frame, good sector, U = 0, m = 2, (k0, k1, k2, k3) = (4, 1, 2, 0), E = 5: [B, h_k] = 0; the E = 5 eigenspace has dimension 8 and the form u^dagger B u on it has inertia " <> ToString[inertia] <>
  "; the positive-frequency solutions Phi = c u E^(i (k.x - 5 x4)) (field equation verified) with B u = -u and B u = +u, |u| = 1, have energy density rho = -T^x4_x4 = " <> ToString[rN, InputForm] <> " and " <> ToString[rP, InputForm] <>
  " and charge density Phi^dagger B Phi = " <> ToString[qN, InputForm] <> " and " <> ToString[qP, InputForm] <> " (cc = |c|): the classical energy is unbounded below already for U = 0, and the U(1) charge is indefinite (only its local law d_mu (sqrt|g| J^mu) = 0 is proved; " <>
  "the total charge is constant in x4 only if no charge flows through the boundary of the slice x4 = const, which at the degenerate points z = n Pi/2 is an ASSUMED no-flux condition)"];

(* ------------------------------------------------------------------ report *)
jstr[s_String] := "\"" <> StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\""}] <> "\"";
nPass = Count[checks, c_ /; c["verdict"] == "PASS"]; nTot = Length[checks];
report = StringJoin[
  "{\n",
  "  \"report\": ", jstr["Revision/theory/reports/wolfram-scope.json"], ",\n",
  "  \"producer\": ", jstr["Revision/theory/wolfram/verify_scope.wls (WolframScript, exact; no shared code with the sympy checker or with RevisionFieldTheory.wl)"], ",\n",
  "  \"spec\": ", jstr["Revision/SPEC.md sections 1-6: scope of the non-triviality, quantisation and energy statements"], ",\n",
  "  \"fixture\": ", jstr["Revision/algebra/gammas.json"], ",\n",
  "  \"metric\": ", jstr["the corrected metric of 2026-10-16: diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3)), z = 6 H x0 real"], ",\n",
  "  \"coordinates\": ", jstr["the author's coordinates x0..x7: x0 = the hidden, space-like direction, z = 6 H x0 real (-Infinity < z < Infinity); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times"], ",\n",
  "  \"summary\": {\"passed\": ", ToString[nPass], ", \"failed\": ", ToString[nTot - nPass], ", \"total\": ", ToString[nTot], "},\n",
  "  \"checks\": [\n",
  StringRiffle[("    {\"name\": " <> jstr[#["name"]] <> ", \"verdict\": " <> jstr[#["verdict"]] <> ", \"detail\": " <> jstr[#["detail"]] <> "}") & /@ checks, ",\n"],
  "\n  ]\n}\n"];
outPath = FileNameJoin[{$revDir, "theory", "reports", "wolfram-scope.json"}];
If[!DirectoryQ[DirectoryName[outPath]], CreateDirectory[DirectoryName[outPath]]];
strm = OpenWrite[outPath, BinaryFormat -> True];
If[strm === $Failed, Print["cannot write ", outPath]; Exit[2]];
BinaryWrite[strm, ToCharacterCode[report, "UTF-8"]]; Close[strm];
Print[nPass, "/", nTot, " checks passed; time ", Round[AbsoluteTime[] - t0, 0.1], " s"];
Exit[If[nPass == nTot, 0, 1]];
