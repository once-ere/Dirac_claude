#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_scope.wls

   Exact WolframScript checks of the SCOPE of the statements of the field-theory record (Revision/SPEC.md
   sections 1-6) in the author's primordial metric: which values depend on the choice of frame and of field
   variables, what holds only up to boundary terms, and what the indefinite structures imply.  Written anew for
   Revision; it does not load Revision/theory/wolfram/RevisionFieldTheory.wl and shares no code with the sympy
   checker Revision/theory/python/check_scope.py.  Writes, deterministically (LF, no time stamps):
     Revision/theory/reports/wolfram-scope.json
   Usage:  wolframscript -file Revision/theory/wolfram/verify_scope.wls
   Exit code 0 if every check passes, 1 otherwise.

   Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the three extra times,
   which DEFLATE exponentially (scale factor e^-a4 sin^(1/6) z, a4 increasing); x8 = the hidden direction,
   z = 6 H x8 in (0, Pi/2).
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
eta = DiagonalMatrix[{1, 1, 1, -1, -1, -1, -1, 1}];
id16 = IdentityMatrix[16]; z16 = ConstantArray[0, {16, 16}];
sAB = Table[(g[[a]] . g[[b]] - g[[b]] . g[[a]])/4, {a, 8}, {b, 8}];
X = {x1, x2, x3, x4, x5, x6, x7, x8};
z = 6 H x8;
assum = H > 0 && 0 < x8 < Pi/(12 H) && Element[{beta, b0, m, lam, x4}, Reals];
zq[e_] := TrueQ[Simplify[TrigExpand[Together[e]], assum] == 0] || TrueQ[FullSimplify[e, assum] == 0];
mzq[M_] := AllTrue[Flatten[M], zq];
addCheck["fixture_gammas",
  And @@ Flatten[Table[g[[a]] . g[[b]] + g[[b]] . g[[a]] == 2 eta[[a, b]] id16, {a, 8}, {b, 8}]] &&
  Cm == g[[8]] . g[[1]] . g[[2]] . g[[3]] && Bm == -I Cm . g[[4]],
  "gammas.json: {gamma^a, gamma^b} = 2 eta^ab I16 (eta = diag(1,1,1,-1,-1,-1,-1,1), order x1..x8), C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3), B = -i C gamma^(x4)"];

(* ------------------------------------------------------------------ geometry of a vielbein e^a_mu (rows a) *)
fd = {E^a4[x4] Sin[z]^(1/6), E^a4[x4] Sin[z]^(1/6), E^a4[x4] Sin[z]^(1/6), 1,
      E^-a4[x4] Sin[z]^(1/6), E^-a4[x4] Sin[z]^(1/6), E^-a4[x4] Sin[z]^(1/6), Cot[z]};
gAuthor = DiagonalMatrix[Diagonal[eta] fd^2];
gInv = Inverse[gAuthor];
chr = Table[Simplify[Sum[gInv[[l, r]] (D[gAuthor[[r, n]], X[[mm]]] + D[gAuthor[[r, mm]], X[[n]]] - D[gAuthor[[mm, n]], X[[r]]])/2, {r, 8}], assum],
  {l, 8}, {mm, 8}, {n, 8}];
boostL[bb_] := ReplacePart[IdentityMatrix[8], {{4, 4} -> Cosh[bb], {4, 8} -> Sinh[bb], {8, 4} -> Sinh[bb], {8, 8} -> Cosh[bb]}];
frame[bb_] := Module[{e, Ei, om, omL, Om, gam},
  e = boostL[bb] . DiagonalMatrix[fd];
  Ei = Simplify[Inverse[e], assum];                         (* Ei[[mu, a]] = e_a^mu *)
  om = Table[Simplify[Sum[e[[a, nu]] (D[Ei[[nu, b]], X[[mu]]] + Sum[chr[[nu, mu, l]] Ei[[l, b]], {l, 8}]), {nu, 8}], assum],
    {mu, 8}, {a, 8}, {b, 8}];                                (* omega_mu^a_b *)
  omL = Table[eta[[a, a]] om[[mu, a, b]], {mu, 8}, {a, 8}, {b, 8}];
  Om = Table[Sum[omL[[mu, a, b]] sAB[[a, b]], {a, 8}, {b, a + 1, 8}], {mu, 8}];
  gam = Table[Sum[Ei[[mu, a]] g[[a]], {a, 8}], {mu, 8}];
  <|"e" -> e, "Ei" -> Ei, "om" -> om, "omL" -> omL, "Om" -> Om, "gam" -> gam|>];
postulateFailures[fr_] := Count[Flatten[Table[
    zq[D[fr["e"][[a, nu]], X[[mu]]] - Sum[chr[[l, mu, nu]] fr["e"][[a, l]], {l, 8}] + Sum[fr["om"][[mu, a, b]] fr["e"][[b, nu]], {b, 8}]],
    {a, 8}, {mu, 8}, {nu, 8}]], False];
gammaOmega[fr_] := Map[Simplify[#, assum] &, Sum[fr["gam"][[mu]] . fr["Om"][[mu]], {mu, 8}], {2}];

(* ================================================================== 1. frame dependence *)
frB = frame[beta x4 + b0];
addCheck["boosted_frame_reproduces_metric",
  mzq[Transpose[frB["e"]] . eta . frB["e"] - gAuthor] && mzq[frB["e"] . frB["Ei"] - IdentityMatrix[8]],
  "frame boosted in the (x4, x8) plane with rapidity b = beta x4 + b0: e'^(x4) = Cosh[b] e^(x4) + Sinh[b] e^(x8), e'^(x8) = Sinh[b] e^(x4) + Cosh[b] e^(x8), the other e'^(a) = e^(a) of the diagonal vielbein; e'^T eta e' equals the author's metric for all 64 entries"];
nPost = postulateFailures[frB];
addCheck["boosted_frame_canonical_connection",
  nPost == 0 && AllTrue[Flatten[Table[zq[frB["omL"][[mu, a, b]] + frB["omL"][[mu, b, a]]], {mu, 8}, {a, 8}, {b, 8}]], TrueQ],
  "canonical spin connection of the boosted frame (Christoffel symbols computed here from the author's metric): the vielbein postulate d_mu e'^a_nu - Gamma^lam_mu,nu e'^a_lam + omega_mu^a_b e'^b_nu = 0 holds for all 512 components (" <> ToString[nPost] <> " failures), omega_mu ab antisymmetric"];
totB = gammaOmega[frB];
addCheck["boosted_frame_gammaOmega_formula",
  mzq[totB - (6 H - beta)/2 (Cosh[beta x4 + b0] g[[8]] - Sinh[beta x4 + b0] g[[4]])] &&
  mzq[gammaOmega[frame[0]] - 3 H g[[8]]],
  "gamma'^mu Omega'_mu = ((6 H - beta)/2) (Cosh[b] gamma^(x8) - Sinh[b] gamma^(x4)) exactly for symbolic a4[x4], H, beta, b0; control: the same code for the unboosted (diagonal) frame gives 3 H gamma^(x8)"];
frZ = frame[6 H x4 + b0];
totZ = gammaOmega[frZ];
nzOm = Select[Range[8], ! mzq[frZ["Om"][[#]]] &];
addCheck["boosted_frame_gammaOmega_vanishes",
  mzq[totZ] && nzOm == {1, 2, 3, 4, 5, 6, 7} && postulateFailures[frZ] == 0,
  "rapidity b = 6 H x4 + b0: gamma'^mu Omega'_mu = 0 identically for every H > 0 and every a4[x4] (exact), in the author's curved metric; the value 3 H gamma^(x8) is a property of the diagonal vielbein, not of the field equation. Omega'_mu is nonzero for mu = " <>
  StringRiffle[("x" <> ToString[#]) & /@ nzOm, ", "] <> " and zero for x8"];
F18 = Map[Simplify[#, assum] &, D[frZ["Om"][[8]], x1] - D[frZ["Om"][[1]], x8] + frZ["Om"][[1]] . frZ["Om"][[8]] - frZ["Om"][[8]] . frZ["Om"][[1]], {2}];
addCheck["boosted_frame_curvature_nonzero",
  ! mzq[F18],
  "in the boosted frame (b = 6 H x4 + b0) the spinor curvature F'_x1x8 = d_x1 Omega'_x8 - d_x8 Omega'_x1 + [Omega'_x1, Omega'_x8] is nonzero: Omega' does not vanish; no frame can make Omega vanish, because its curvature is (1/2) R_ab,mu,nu S^ab and the metric is curved"];

(* ================================================================== 2. diagonal frame *)
frD = frame[0];
totD = gammaOmega[frD];
w = Sin[z]^(-1/2);
resc = Map[Simplify[#, assum] &, Sum[frD["gam"][[mu]] D[w, X[[mu]]], {mu, 8}] + w totD, {2}];
chiF = Table[cf[A] @@ X, {A, 16}];
lhsResc = Sum[frD["gam"][[mu]] . (D[w chiF, X[[mu]]] + frD["Om"][[mu]] . (w chiF)), {mu, 8}] - w Sum[frD["gam"][[mu]] . D[chiF, X[[mu]]], {mu, 8}];
addCheck["rescaling_removes_the_connection_term",
  mzq[totD - 3 H g[[8]]] && mzq[resc] && AllTrue[lhsResc, zq],
  "diagonal frame: gamma^mu Omega_mu = 3 H gamma^(x8); for Psi = Sin[z]^(-1/2) chi with 16 arbitrary functions chi_A(x1, ..., x8), gamma^mu D_mu Psi - Sin[z]^(-1/2) gamma^mu d_mu chi = 0 component by component (computed on the functions themselves): in the variables chi the field equation has no spin-connection term"];
St = Symbol["St"];
addCheck["rescaled_equation_quadratic_potential",
  zq[lam (w^2 St) - lam St/Sin[z]] && TrueQ[Simplify[w > 0, assum]],
  "U = (lambda/2) S^2: S[Sin[z]^(-1/2) chi] = Sin[z]^(-1) S[chi] (the factor is real), so U'(S) Psi = Sin[z]^(-1/2) (lambda S[chi]/Sin[z]) chi and the rescaled equation is gamma^mu d_mu chi = (m + lambda S[chi]/Sin[z]) chi: the 3 H term is removed completely for U = 0 and becomes an x8-dependent coupling for U != 0"];
riem[r_, s_, mu_, nu_] := D[chr[[r, nu, s]], X[[mu]]] - D[chr[[r, mu, s]], X[[nu]]] + Sum[chr[[r, mu, l]] chr[[l, nu, s]] - chr[[r, nu, l]] chr[[l, mu, s]], {l, 8}];
ricMixed[a_] := Simplify[Sum[riem[r, a, r, a], {r, 8}] gInv[[a, a]], assum];
{r44, r11, r88} = ricMixed /@ {4, 1, 8};
addCheck["gammaOmega_blind_to_the_deflation",
  FreeQ[totD, a4] && zq[r44 - 6 a4'[x4]^2] && zq[r11 - (a4''[x4] - 6 H^2)] && zq[r88 + 6 H^2],
  "diagonal frame: gamma^mu Omega_mu = 3 H gamma^(x8) does not contain a4 (nor a4', a4''), while R^x4_x4 = " <> ToString[r44, InputForm] <> ", R^x1_x1 = " <> ToString[r11, InputForm] <>
  ", R^x8_x8 = " <> ToString[r88, InputForm] <> " (Riemann computed here from the metric): the deflation of the extra times is curvature that the term gamma^mu Omega_mu does not see; it enters the field equation through the frame factors E^(-+a4) Sin[z]^(-1/6)"];
sqrtg = Times @@ fd;
addCheck["connection_free_lagrangian_same_equations",
  AllTrue[Range[8], mzq[frD["gam"][[#]] . frD["Om"][[#]] + frD["Om"][[#]] . frD["gam"][[#]]] &] &&
  mzq[Sum[D[sqrtg frD["gam"][[mu]], X[[mu]]], {mu, 8}]/(2 sqrtg) - totD],
  "diagonal frame: {gamma^mu, Omega_mu} = 0 for each mu, so the canonical spin connection drops out of the symmetrised Lagrangian (L(Omega) = L(Omega = 0)) and the Euler-Lagrange equations are those of the connection-free symmetric Lagrangian; (1/(2 sqrt|g|)) d_mu(sqrt|g| gamma^mu) = gamma^mu Omega_mu = 3 H gamma^(x8): the half-density term"];
dK = (frD["gam"][[4]] . frD["Om"][[1]] + frD["Om"][[1]] . frD["gam"][[4]])/2;
addCheck["spin_connection_in_the_energy_momentum_tensor",
  mzq[dK - E^a4[x4] Sin[z]^(1/6) H g[[4]] . g[[1]] . g[[8]]/2] && Cm . g[[4]] . g[[1]] . g[[8]] != z16,
  "homogeneous configuration Phi(x4), diagonal frame: the connection part of K^x4_x1 = (1/2)(Phibar gamma^x4 D_x1 Phi - D_x1 Phibar gamma^x4 Phi) is (1/2) Phibar {gamma^x4, Omega_x1} Phi = (1/2) E^a4 Sin[z]^(1/6) H Phibar gamma^(x4) gamma^(x1) gamma^(x8) Phi, not identically zero: the canonical spin connection reaches the energy-momentum tensor"];

(* ================================================================== 3. Hermiticity only up to the brane flux *)
uF = Table[ur[A][x8] + I ui[A][x8], {A, 16}]; vF = Table[vr[A][x8] + I vi[A][x8], {A, 16}];
cj[vec_] := ComplexExpand[Conjugate[vec]];
hOp[vec_] := -I m g[[4]] . vec + I g[[4]] . g[[8]] . (Tan[z] D[vec, x8] + 3 H vec);
M8 = I g[[4]] . g[[8]];
lhsH = Cos[z] (cj[uF] . hOp[vF] - cj[hOp[uF]] . vF) - D[Sin[z] cj[uF] . M8 . vF, x8];
u0 = First[NullSpace[g[[4]] . g[[8]] - id16]];
flux = Simplify[Conjugate[u0] . M8 . u0];
addCheck["good_sector_hermiticity_up_to_the_brane_flux",
  zq[ComplexExpand[lhsH]] && flux =!= 0,
  "curved good-sector mode operator at k = 0, h = -i m gamma^(x4) + i gamma^(x4) gamma^(x8) (Tan[z] d_x8 + 3 H): for arbitrary complex u(x8), v(x8) (32 real functions) Cos[z] (u^dagger h v - (h u)^dagger v) = d_x8 (Sin[z] u^dagger M8 v), M8 = i gamma^(x4) gamma^(x8), exactly; the boundary term vanishes at the tip but not at z = Pi/2 (Sin[z] = 1): for gamma^(x4) gamma^(x8) u = u, u^dagger M8 u = " <> ToString[flux, InputForm] <> " (|u|^2 = " <> ToString[Conjugate[u0] . u0, InputForm] <> "). Symmetry of h for Integrate[Cos[z] u^dagger v] holds only with boundary conditions at the patch end"];
Aop = -I m g[[4]] + 3 I H g[[4]] . g[[8]];
evA = Sort[Eigenvalues[Aop /. {m -> 1, H -> 1}], (Im[#1] < Im[#2]) &];
normInt = Integrate[Cos[6 H y], {y, 0, Pi/(12 H)}, Assumptions -> H > 0];
addCheck["good_sector_x8_independent_modes_without_boundary_condition",
  Expand[Aop . Aop - (m^2 - 9 H^2) id16] == z16 && Aop =!= ConjugateTranspose[Aop] &&
  evA == Join[ConstantArray[-2 Sqrt[2] I, 8], ConstantArray[2 Sqrt[2] I, 8]] && normInt == 1/(6 H),
  "on x8-independent good-sector functions (finite norm: Integrate[Cos[6 H x8], {x8, 0, Pi/(12 H)}] = " <> ToString[normInt, InputForm] <>
  ") the curved mode operator is the matrix A = -i m gamma^(x4) + 3 i H gamma^(x4) gamma^(x8): not Hermitian, A^2 = (m^2 - 9 H^2) I16; at m = H = 1 its eigenvalues are -2 Sqrt[2] i and 2 Sqrt[2] i, 8 each (modes growing like E^(2 Sqrt[2] x4)): without a boundary condition at z = Pi/2 the good sector contains complex frequencies whenever m^2 < 9 H^2"];

(* ================================================================== 4. extra-time growth *)
kk = Table[Symbol["k" <> ToString[a]], {a, 8}];
hk = -I m g[[4]] - Sum[If[a == 4, z16, kk[[a]] g[[4]] . g[[a]]], {a, 8}];
e2 = m^2 + kk[[1]]^2 + kk[[2]]^2 + kk[[3]]^2 + kk[[8]]^2 - kk[[5]]^2 - kk[[6]]^2 - kk[[7]]^2;
growth = Sqrt[-(e2 /. {kk[[5]] -> K5, kk[[6]] -> 0, kk[[7]] -> 0})];
addCheck["extra_time_growth_rates_unbounded",
  Expand[hk . hk - e2 id16] == z16 && Limit[growth, K5 -> Infinity] === Infinity,
  "flat 4+4 space (or frozen coefficients): h_k = -i m gamma^(x4) - gamma^(x4) Sum[k_a gamma^(a)] has h_k^2 = (" <> ToString[e2, InputForm] <>
  ") I16; with k5 = K5 the growth rate " <> ToString[growth, InputForm] <> " is unbounded as K5 -> Infinity: the Cauchy problem for data depending on x5, x6, x7 is not well posed in Hadamard's sense, although the slices x4 = const are non-characteristic"];

(* ================================================================== 5. classical energy of dirac16complex00 *)
kv = {1, 2, 0, 0, 0, 0, 0, 4}; mv = 2; ev = 5;
hs = hk /. Thread[kk -> kv] /. m -> mv;
Vp = NullSpace[hs - ev id16];
neg = Select[(Bm - id16) . # & /@ Vp, # =!= ConstantArray[0, 16] &];
pos = Select[(Bm + id16) . # & /@ Vp, # =!= ConstantArray[0, 16] &];
nrm[v_] := v/Sqrt[Simplify[Conjugate[v] . v]];
{uN, uP} = nrm /@ {First[neg], First[pos]};
Y = Table[Symbol["y" <> ToString[a]], {a, 8}];
energyAndCharge[u_] := Module[{ph, Phi, Phib, K, S, rho, eq, q},
  ph = Exp[I (Sum[If[a == 4, 0, kv[[a]] Y[[a]]], {a, 8}] - ev Y[[4]])];
  Phi = cc u ph;
  Phib = ComplexExpand[Conjugate[Phi]] . Cm;
  K = Table[(Phib . g[[a]] . D[Phi, Y[[a]]] - (ComplexExpand[Conjugate[D[Phi, Y[[a]]]]] . Cm) . g[[a]] . Phi)/2, {a, 8}];
  S = Phib . Phi;
  rho = Simplify[ComplexExpand[-Total[Delete[K, 4]] + mv S], cc > 0];
  eq = Simplify[Sum[g[[a]] . D[Phi, Y[[a]]], {a, 8}] - mv Phi];
  q = Simplify[ComplexExpand[ComplexExpand[Conjugate[Phi]] . Bm . Phi], cc > 0];
  {rho, eq === ConstantArray[0, 16], q}];
{rN, okN, qN} = energyAndCharge[uN];
{rP, okP, qP} = energyAndCharge[uP];
inertia = Module[{V = Transpose[Vp], ev2}, ev2 = Eigenvalues[ConjugateTranspose[V] . Bm . V]; {Count[ev2, _?Positive], Count[ev2, _?Negative]}];
addCheck["commuting_field_energy_unbounded_below",
  Expand[Bm . hs - hs . Bm] == z16 && Length[Vp] == 8 && inertia == {4, 4} && okN && okP &&
  Simplify[rN + 5 cc^2] === 0 && Simplify[rP - 5 cc^2] === 0 && Simplify[qN + cc^2] === 0 && Simplify[qP - cc^2] === 0,
  "dirac16complex00, flat frame, good sector, U = 0, m = 2, (k1, k2, k3, k8) = (1, 2, 0, 4), E = 5: [B, h_k] = 0; the E = 5 eigenspace has dimension 8 and the form u^dagger B u on it has inertia " <> ToString[inertia] <>
  "; the positive-frequency solutions Phi = c u E^(i (k.x - 5 x4)) (field equation verified) with B u = -u and B u = +u, |u| = 1, have energy density rho = -T^x4_x4 = " <> ToString[rN, InputForm] <> " and " <> ToString[rP, InputForm] <>
  " and charge density Phi^dagger B Phi = " <> ToString[qN, InputForm] <> " and " <> ToString[qP, InputForm] <> " (cc = |c|): the classical energy is unbounded below already for U = 0, and the U(1) charge is indefinite (only its local law d_mu (Cos[z] J^mu) = 0 is proved; " <>
  "the total charge is constant in x4 only if no charge flows through the boundary of the slice x4 = const, which at the brane z = Pi/2 is an ASSUMED no-flux condition)"];

(* ------------------------------------------------------------------ report *)
jstr[s_String] := "\"" <> StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\""}] <> "\"";
nPass = Count[checks, c_ /; c["verdict"] == "PASS"]; nTot = Length[checks];
report = StringJoin[
  "{\n",
  "  \"report\": ", jstr["Revision/theory/reports/wolfram-scope.json"], ",\n",
  "  \"producer\": ", jstr["Revision/theory/wolfram/verify_scope.wls (WolframScript, exact; no shared code with the sympy checker or with RevisionFieldTheory.wl)"], ",\n",
  "  \"spec\": ", jstr["Revision/SPEC.md sections 1-6: scope of the non-triviality, quantisation and energy statements"], ",\n",
  "  \"fixture\": ", jstr["Revision/algebra/gammas.json"], ",\n",
  "  \"coordinates\": ", jstr["x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; x8 = the hidden direction, z = 6 H x8 in (0, Pi/2)"], ",\n",
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
