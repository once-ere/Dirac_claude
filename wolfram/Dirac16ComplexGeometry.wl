(* ::Package:: *)

(* Dirac16ComplexGeometry.wl

   Exact curved-space geometry, Lagrangian, energy-momentum tensor and canonical
   structure of the 16-component complex Grassmann spinor field "dirac16complex"
   (Stage 1, arbitrary gravitational field).  Context Dirac16Complex`Geometry`.

   Conventions (binding, CONTRACT.md of the design phase):
   * everything is counted from 0: coordinates x0..x7, frame indices a,b = 0..7,
     curved indices mu,nu = 0..7, spinor indices 0..15 (Mathematica lists are 1-based,
     so the zero-based index i is stored at position i+1);
   * eta = diag(+1,+1,+1,+1,-1,-1,-1,-1); x4 is the evolution time;
   * gamma^a := notebook T16^A[a] = [[0, taubar[a]], [tau[a], 0]] (split-octonion block
     basis), {gamma^a, gamma^b} = 2 eta^{ab};  C := sigma16 = gamma^0 gamma^1 gamma^2 gamma^3;
   * Psibar := Psi^dagger C;  S^{ab} = (1/4)[gamma^a, gamma^b];
   * vielbein frame[[mu,a]] = e_mu^a (rows mu), inverseFrame[[a,mu]] = e_a^mu,
     g_{mu nu} = e_mu^a eta_ab e_nu^b, gamma^mu = e_a^mu gamma^a, gamma_mu = g_{mu nu} gamma^nu;
   * Christoffel[[rho,mu,nu]] = Gamma^rho_{mu nu} (Levi-Civita);
   * omegaMixed[[mu,a,b]] = omega_mu^a_b = e_b^nu (Gamma^rho_{mu nu} e_rho^a - d_mu e_nu^a)
     (vielbein postulate), omegaLower[[mu,a,b]] = omega_{mu ab} = eta_ac omega_mu^c_b;
   * Omega[[mu]] = (1/2) omega_{mu ab} S^{ab} (sum over all ordered pairs);
     OmegaNotebook[[mu]] = (1/2) omega_mu^a_b S^{ab} (the notebook Lg[] contraction);
   * D_mu Psi = d_mu Psi + Omega_mu Psi,  D_mu Psibar = d_mu Psibar - Psibar Omega_mu;
   * Riemann[[rho,sigma,mu,nu]] = R^rho_{sigma mu nu} = d_mu Gamma^rho_{nu sigma}
     - d_nu Gamma^rho_{mu sigma} + Gamma^rho_{mu lambda} Gamma^lambda_{nu sigma}
     - Gamma^rho_{nu lambda} Gamma^lambda_{mu sigma};  Ricci_{sigma nu} = R^rho_{sigma rho nu}.

   Exactness.  Nothing here uses floating point for a decision.  Identities that involve
   arbitrary functions are decided by exact symbolic differentiation of the vielbein
   followed by substitution of exact values at an evaluation point ("jets"): the value,
   the first and the second derivatives of the vielbein at the point are exact numbers,
   and every derived object (metric, Christoffel symbols, spin connection, curvature,
   field equations, energy-momentum tensor) is propagated as an exact order-1 jet
   {value, {d_0 value, ..., d_7 value}} with the product and inverse rules.  For the
   primordial field the numbers live in the quadratic field Q(cs), cs = cos z, and are
   reduced to the canonical basis {1, cs} (see D16GeoSetAlgebraic).  Field jets
   (Psi, d Psi, d d Psi and the same for Psi^dagger) are independent exact numbers or,
   for the Euler-Lagrange checks, genuine Grassmann generators (a small exact Grassmann
   algebra with jet-valued coefficients is part of this package).

   Public entry points:
     D16GeoSymbolicGeometry[frame, coords]  symbolic geometry (small/diagonal frames)
     D16GeoFrameJet[frame, coords, rules]   exact order-2 vielbein jet at a point
     D16GeoJetGeometry[frameJet]            exact order-1 jets of every geometric object
     D16GeoFieldJets, D16GeoLagrangianJets, D16GeoEMTJets, D16GeoEMTDivergence,
     D16GeoSolveOnShell, D16GeoDiracSquared, D16GeoSpinorLaplacian   (helper operators)
     D16GeoReport[]                          every check of the geometry verifier

   License: GPL-3.0-or-later (same as the dirac-main reference implementation). *)

BeginPackage["Dirac16Complex`Geometry`"];

D16GeoEta::usage = "D16GeoEta is the tangent metric diag(1,1,1,1,-1,-1,-1,-1).";
D16GeoGammas::usage = "D16GeoGammas is the list of the eight 16x16 notebook gammas T16^A[0..7] (D16GeoGammas[[a+1]] = gamma^a).";
D16GeoC::usage = "D16GeoC is C = sigma16 = gamma^0 gamma^1 gamma^2 gamma^3.";
D16GeoSpin::usage = "D16GeoSpin[[a+1,b+1]] is S^{ab} = (1/4)[gamma^a, gamma^b].";
D16GeoChirality::usage = "D16GeoChirality is gamma^8 = gamma^0 ... gamma^7.";
D16GeoSetAlgebraic::usage = "D16GeoSetAlgebraic[None] or D16GeoSetAlgebraic[{s, n, c}] selects exact reduction s^n -> c for all subsequent jet arithmetic.";
D16GeoReduce::usage = "D16GeoReduce[x] reduces x to the canonical form of the current exact number field.";
D16GeoZeroQ::usage = "D16GeoZeroQ[x] is True iff every entry of x is exactly zero in the current exact number field.";
D16GeoSymbolicGeometry::usage = "D16GeoSymbolicGeometry[frame, coords] returns the symbolic metric, inverse metric, Christoffel symbols, omegaMixed, omegaLower, Omega, OmegaNotebook and curved gammas of the vielbein frame[[mu,a]] = e_mu^a.";
D16GeoFrameJet::usage = "D16GeoFrameJet[frame, coords, rules] returns {e, de, dde} at the point given by the replacement rules (exact symbolic differentiation, then substitution).";
D16GeoJetGeometry::usage = "D16GeoJetGeometry[{e, de, dde}] returns an association of exact order-1 jets (and point values) of every geometric object.";
D16GeoFieldJets::usage = "D16GeoFieldJets[p0, p1, p2, q0, q1, q2] packs Psi and Psi^dagger data (value, first, second derivatives) into jets.";
D16GeoLagrangianJets::usage = "D16GeoLagrangianJets[geo, fields, m, lambda, omegaKey] returns the jets of S, Ls, L = sqrt|g| Ls, D Psi, D Psibar.";
D16GeoEMTJets::usage = "D16GeoEMTJets[geo, lag] returns the 8x8 array of jets of T_{mu nu} (CONTRACT section 7).";
D16GeoEMTDivergence::usage = "D16GeoEMTDivergence[geo, T] returns nabla^mu T_{mu nu} at the point.";
D16GeoSolveOnShell::usage = "D16GeoSolveOnShell[geo, free, m, lambda] solves the field equations and their first derivatives at the point for the x4-derivatives of Psi and Psi^dagger.";
D16GeoDiracSquared::usage = "D16GeoDiracSquared[geo, fields] returns (gamma^mu D_mu)^2 Psi at the point.";
D16GeoSpinorLaplacian::usage = "D16GeoSpinorLaplacian[geo, fields] returns g^{mu nu}(D_mu D_nu Psi - Gamma^lambda_{mu nu} D_lambda Psi) at the point.";
D16GeoG1Frame::usage = "D16GeoG1Frame[x] is the general non-diagonal test vielbein G1 at the coordinate list x.";
D16GeoReport::usage = "D16GeoReport[] runs every check of the geometry verifier and returns <|\"checks\" -> ..., \"measurements\" -> ...|>.";
D16GeoRandomRationals::usage = "D16GeoRandomRationals[seed, n] returns n reproducible exact rationals from a 64-bit LCG.";

Begin["`Private`"];

(* ========================================================================= *)
(* 1. Algebra: notebook gammas (copied construction of the design probe)     *)
(* ========================================================================= *)

id4 = IdentityMatrix[4]; id8 = IdentityMatrix[8]; id16 = IdentityMatrix[16];
$eta = DiagonalMatrix[{1, 1, 1, 1, -1, -1, -1, -1}];
$etaDiag = Diagonal[$eta];
qa[h_, p_, q_] := Signature[{h, p, q, 4}];
qb[h_, p_, q_] := id4[[p, 4]] id4[[q, h]] - id4[[p, h]] id4[[q, 4]];
s4[h_] := Table[qa[h, p, q] - qb[h, p, q], {p, 4}, {q, 4}];
t4[h_] := Table[qa[h, p, q] + qb[h, p, q], {p, 4}, {q, 4}];
tau[0] = id8;
Do[tau[h] = ArrayFlatten[{{0, s4[h]}, {s4[h], 0}}], {h, 1, 3}];
Do[tau[7 - h] = ArrayFlatten[{{0, t4[h]}, {-t4[h], 0}}], {h, 1, 3}];
tau[7] = tau[1].tau[2].tau[3].tau[4].tau[5].tau[6];
sig8 = ArrayFlatten[{{0, id4}, {id4, 0}}];
taub[0] = id8;
Do[taub[a] = sig8.Transpose[tau[a]].sig8, {a, 1, 7}];
$gam = Table[ArrayFlatten[{{0, taub[a]}, {tau[a], 0}}], {a, 0, 7}];
$C = ArrayFlatten[{{-sig8, 0}, {0, sig8}}];
$S = Table[($gam[[a]].$gam[[b]] - $gam[[b]].$gam[[a]])/4, {a, 8}, {b, 8}];
$Sflat = Flatten[$S, 1];
$chi = Fold[Dot, id16, $gam];

D16GeoEta = $eta; D16GeoGammas = $gam; D16GeoC = $C; D16GeoSpin = $S; D16GeoChirality = $chi;

comm[a_, b_] := a.b - b.a;
acomm[a_, b_] := a.b + b.a;

(* ========================================================================= *)
(* 2. Exact number field handling                                             *)
(* ========================================================================= *)

$alg = None;
D16GeoSetAlgebraic[spec_] := ($alg = spec);
red[x_] := If[$alg === None, x,
  With[{s = $alg[[1]], n = $alg[[2]], c = $alg[[3]]},
    Expand[x] /. Power[s, k_Integer] :> c^Floor[k/n] s^Mod[k, n]]];
D16GeoReduce[x_] := red[x];
zeroQ[x_] := AllTrue[Flatten[{red[x]}], (Expand[#] === 0) &];
D16GeoZeroQ[x_] := zeroQ[x];
(* exact algebraic value (for printing and for numerical ordering of measurements) *)
exactValue[x_] := If[$alg === None, x, red[x] /. $alg[[1]] -> $alg[[3]]^(1/$alg[[2]])];
numValue[x_] := N[exactValue[x], 30];
maxAbsEntry[x_] := Module[{flat = Select[Flatten[{red[x]}], ! (Expand[#] === 0) &], vals, pos},
  If[flat === {}, Return[0]];
  vals = Abs[numValue /@ flat]; pos = First[Ordering[vals, -1]];
  exactValue[flat[[pos]]] // Abs // Simplify];
exactString[x_] := ToString[exactValue[x], InputForm];

(* ========================================================================= *)
(* 3. Order-1 jets {value, {d_0 value, ..., d_7 value}}                       *)
(* ========================================================================= *)

zeroLike[v_] := 0 v;
jConst[v_] := {v, Table[zeroLike[v], {8}]};
jMul[f_, a_, b_] := {red[f[a[[1]], b[[1]]]],
  Table[red[f[a[[2, l]], b[[1]]] + f[a[[1]], b[[2, l]]]], {l, 8}]};
jLin[f_, a_] := {red[f[a[[1]]]], red[f /@ a[[2]]]};
jInv[a_] := With[{ai = red[Inverse[a[[1]]]]}, {ai, Table[red[-ai.a[[2, l]].ai], {l, 8}]}];
jPart[j_, idx__] := {j[[1, idx]], j[[2, All, idx]]};
jStack[list_] := {list[[All, 1]], Table[list[[All, 2, l]], {l, 8}]};
jVal[j_] := j[[1]];
jDer[j_, l_] := j[[2, l]];   (* l is 1-based *)

(* order-2 jets {value, first (8), second (8x8)} *)
j2Mul[f_, a_, b_] := {red[f[a[[1]], b[[1]]]],
  Table[red[f[a[[2, l]], b[[1]]] + f[a[[1]], b[[2, l]]]], {l, 8}],
  Table[red[f[a[[3, l, k]], b[[1]]] + f[a[[2, l]], b[[2, k]]] + f[a[[2, k]], b[[2, l]]] + f[a[[1]], b[[3, l, k]]]], {l, 8}, {k, 8}]};
j2Lin[f_, a_] := {red[f[a[[1]]]], red[f /@ a[[2]]], red[Map[f, a[[3]], {2}]]};
j2ToJ1[a_] := {a[[1]], a[[2]]};

(* ========================================================================= *)
(* 4. Symbolic geometry (for diagonal or otherwise small frames)             *)
(* ========================================================================= *)

Options[D16GeoSymbolicGeometry] = {"Simplifier" -> Identity};
D16GeoSymbolicGeometry[frame_, coords_, OptionsPattern[]] := Module[
  {simp = OptionValue["Simplifier"], g, ginv, einv, gam, om, omL, Om, OmNB, gamLow, n = Length[coords]},
  g = simp[frame.$eta.Transpose[frame]];
  ginv = simp[Inverse[g]];
  einv = simp[$eta.Transpose[frame].ginv];
  gam = Table[
    simp[(1/2) Sum[ginv[[r, s]] (D[g[[s, m]], coords[[nn]]] + D[g[[s, nn]], coords[[m]]] - D[g[[m, nn]], coords[[s]]]), {s, n}]],
    {r, n}, {m, n}, {nn, n}];
  om = Table[simp[Sum[einv[[b, nn]] (Sum[gam[[r, m, nn]] frame[[r, a]], {r, n}] - D[frame[[nn, a]], coords[[m]]]), {nn, n}]],
    {m, n}, {a, n}, {b, n}];
  omL = Table[$etaDiag[[a]] om[[m, a, b]], {m, n}, {a, n}, {b, n}];
  Om = Table[simp[(1/2) Flatten[omL[[m]]].$Sflat], {m, n}];
  OmNB = Table[simp[(1/2) Flatten[om[[m]]].$Sflat], {m, n}];
  gamLow = Table[simp[Sum[frame[[m, a]] $etaDiag[[a]] $gam[[a]], {a, n}]], {m, n}];
  <|"frame" -> frame, "inverseFrame" -> einv, "metric" -> g, "inverseMetric" -> ginv,
    "christoffel" -> gam, "omegaMixed" -> om, "omegaLower" -> omL, "Omega" -> Om,
    "OmegaNotebook" -> OmNB,
    "curvedGammas" -> Table[simp[Sum[einv[[a, m]] $gam[[a]], {a, n}]], {m, n}],
    "loweredGammas" -> gamLow,
    "frameDeterminant" -> simp[Det[frame]]|>
];

(* ========================================================================= *)
(* 5. Vielbein jets and jet geometry                                          *)
(* ========================================================================= *)

D16GeoFrameJet[frame_, coords_, rules_] := Module[{e1, e2},
  e1 = Table[D[frame, coords[[l]]], {l, 8}];
  e2 = Table[D[e1[[l]], coords[[k]]], {l, 8}, {k, 8}];
  red[{frame, e1, e2} /. rules]
];

Options[D16GeoJetGeometry] = {"SqrtSign" -> Automatic};
D16GeoJetGeometry[fj_List, OptionsPattern[]] := Module[
  {e0, e1, e2, eJ, deJ, gJ, dgJ, ginvJ, einvJ, DgJ, gamLowJ, GamJ, DeArrJ, XJ, omJ, omLJ, OmJ, OmNBJ,
   gamJ, gamLJ, detE, sgn, sqrtgJ, Gv, Gd, riem, ricci, rs, einstein, vpJ},
  {e0, e1, e2} = fj;
  eJ = {e0, e1};
  deJ = Table[{e1[[mu]], e2[[All, mu]]}, {mu, 8}];
  gJ = jMul[#1.$eta.Transpose[#2] &, eJ, eJ];
  dgJ = Table[jMul[#1.$eta.Transpose[#2] &, deJ[[mu]], eJ] + jMul[#1.$eta.Transpose[#2] &, eJ, deJ[[mu]]], {mu, 8}];
  ginvJ = jInv[gJ];
  einvJ = jMul[Dot, jLin[$eta.Transpose[#] &, eJ], ginvJ];
  DgJ = jStack[dgJ];                                     (* [sigma, mu, nu] = d_sigma g_{mu nu} *)
  gamLowJ = jLin[Function[A, Table[(A[[m, nn, s]] + A[[nn, m, s]] - A[[s, m, nn]])/2, {s, 8}, {m, 8}, {nn, 8}]], DgJ];
  GamJ = jMul[Dot, ginvJ, gamLowJ];                      (* [rho, mu, nu] *)
  DeArrJ = jStack[deJ];                                  (* [mu, nu, a] = d_mu e_nu^a *)
  XJ = jMul[Function[{G, e}, Table[Sum[G[[r, m, nn]] e[[r, a]], {r, 8}], {m, 8}, {nn, 8}, {a, 8}]], GamJ, eJ] - DeArrJ;
  omJ = jMul[Function[{ei, X}, Table[Sum[ei[[b, nn]] X[[m, nn, a]], {nn, 8}], {m, 8}, {a, 8}, {b, 8}]], einvJ, XJ];
  omLJ = jLin[Function[w, Table[$etaDiag[[a]] w[[m, a, b]], {m, 8}, {a, 8}, {b, 8}]], omJ];
  OmJ = jLin[Function[w, Table[(1/2) Flatten[w[[m]]].$Sflat, {m, 8}]], omLJ];
  OmNBJ = jLin[Function[w, Table[(1/2) Flatten[w[[m]]].$Sflat, {m, 8}]], omJ];
  gamJ = jLin[Transpose[#].$gam &, einvJ];               (* gamma^mu *)
  gamLJ = jLin[#.$eta.$gam &, eJ];                       (* gamma_mu *)
  (* vielbein postulate d_mu e_nu^a - Gamma^rho_{mu nu} e_rho^a + omega_mu^a_b e_nu^b as a jet *)
  vpJ = -XJ + jMul[Function[{w, e}, Table[Sum[w[[m, a, b]] e[[nn, b]], {b, 8}], {m, 8}, {nn, 8}, {a, 8}]], omJ, eJ];
  detE = red[Det[e0]];
  sgn = If[OptionValue["SqrtSign"] === Automatic, Sign[numValue[detE]], OptionValue["SqrtSign"]];
  sqrtgJ = {red[sgn detE], Table[red[sgn detE Tr[einvJ[[1]].e1[[l]]]], {l, 8}]};
  Gv = GamJ[[1]]; Gd = GamJ[[2]];
  riem = red[Table[Gd[[m, r, nn, s]] - Gd[[nn, r, m, s]] + Sum[Gv[[r, m, l]] Gv[[l, nn, s]] - Gv[[r, nn, l]] Gv[[l, m, s]], {l, 8}],
    {r, 8}, {s, 8}, {m, 8}, {nn, 8}]];
  ricci = red[Table[Sum[riem[[r, s, r, nn]], {r, 8}], {s, 8}, {nn, 8}]];
  rs = red[Sum[ginvJ[[1, s, nn]] ricci[[s, nn]], {s, 8}, {nn, 8}]];
  einstein = red[ginvJ[[1]].ricci - (rs/2) id8];
  <|"frameJet" -> fj, "e" -> eJ, "g" -> gJ, "ginv" -> ginvJ, "einv" -> einvJ, "christoffel" -> GamJ,
    "omegaMixed" -> omJ, "omegaLower" -> omLJ, "Omega" -> OmJ, "OmegaNotebook" -> OmNBJ,
    "gamma" -> gamJ, "gammaLower" -> gamLJ, "sqrtg" -> sqrtgJ, "vielbeinPostulate" -> vpJ,
    "riemann" -> riem, "ricci" -> ricci, "scalarCurvature" -> rs, "einsteinMixed" -> einstein,
    "detFrame" -> detE, "sqrtSign" -> sgn|>
];

(* ========================================================================= *)
(* 6. Field jets and helper operators (commuting exact numbers)               *)
(* ========================================================================= *)

(* p0: Psi (16), p1[[mu]]: d_mu Psi, p2[[l, mu]]: d_l d_mu Psi (symmetric); q.. the same for
   Psi^dagger (row vectors).  Any of them may also be 16x16 matrices (probe fields). *)
D16GeoFieldJets[p0_, p1_, p2_, q0_, q1_, q2_] := <|
  "psi" -> {p0, p1}, "dpsi" -> Table[{p1[[mu]], p2[[All, mu]]}, {mu, 8}],
  "psb" -> {q0, q1}, "dpsb" -> Table[{q1[[mu]], q2[[All, mu]]}, {mu, 8}]|>;

D16GeoLagrangianJets[geo_, fld_, m_, lam_, omKey_: "Omega"] := Module[
  {OmJ = geo[omKey], gamJ = geo["gamma"], psiJ = fld["psi"], psbJ = fld["psb"], barJ, dbarJ, DpsiJ, DbarJ, SJ, kinJ, LsJ, LJ, kin4J},
  barJ = jLin[#.$C &, psbJ];
  dbarJ = Table[jLin[#.$C &, fld["dpsb"][[mu]]], {mu, 8}];
  DpsiJ = Table[fld["dpsi"][[mu]] + jMul[Dot, jPart[OmJ, mu], psiJ], {mu, 8}];
  DbarJ = Table[dbarJ[[mu]] - jMul[Dot, barJ, jPart[OmJ, mu]], {mu, 8}];
  SJ = jMul[Dot, barJ, psiJ];
  kinJ = (1/2) Sum[jMul[Dot, barJ, jMul[Dot, jPart[gamJ, mu], DpsiJ[[mu]]]] -
      jMul[Dot, jMul[Dot, DbarJ[[mu]], jPart[gamJ, mu]], psiJ], {mu, 8}];
  kin4J = (1/4) (jMul[Dot, barJ, jMul[Dot, jPart[gamJ, 5], DpsiJ[[5]]]] -
      jMul[Dot, jMul[Dot, DbarJ[[5]], jPart[gamJ, 5]], psiJ]);
  LsJ = kinJ - m SJ - (lam/2) jMul[Times, SJ, SJ];
  LJ = jMul[Times, geo["sqrtg"], LsJ];
  <|"bar" -> barJ, "Dpsi" -> DpsiJ, "Dbar" -> DbarJ, "S" -> SJ, "kinetic" -> kinJ, "KE" -> kin4J,
    "Ls" -> LsJ, "L" -> LJ, "psi" -> psiJ, "m" -> m, "lambda" -> lam|>
];

D16GeoEMTJets[geo_, lag_] := Module[{gl = geo["gammaLower"], A, B},
  A = Table[jMul[Dot, lag["bar"], jMul[Dot, jPart[gl, mu], lag["Dpsi"][[nu]]]], {mu, 8}, {nu, 8}];
  B = Table[jMul[Dot, jMul[Dot, lag["Dbar"][[mu]], jPart[gl, nu]], lag["psi"]], {mu, 8}, {nu, 8}];
  Table[-(1/4) (A[[mu, nu]] + A[[nu, mu]] - B[[mu, nu]] - B[[nu, mu]]) +
    jMul[Times, jPart[geo["g"], mu, nu], lag["Ls"]], {mu, 8}, {nu, 8}]
];

D16GeoEMTDivergence[geo_, tJ_] := Module[{ginv = geo["ginv"][[1]], G = geo["christoffel"][[1]], tv},
  tv = Map[First, tJ, {2}];
  red[Table[Sum[ginv[[mu, al]] (tJ[[mu, nu, 2, al]] - Sum[G[[l, al, mu]] tv[[l, nu]] + G[[l, al, nu]] tv[[mu, l]], {l, 8}]),
    {mu, 8}, {al, 8}], {nu, 8}]]
];

D16GeoDiracSquared[geo_, fld_, omKey_: "Omega"] := Module[{OmJ = geo[omKey], gamJ = geo["gamma"], DpsiJ, chiJ},
  DpsiJ = Table[fld["dpsi"][[mu]] + jMul[Dot, jPart[OmJ, mu], fld["psi"]], {mu, 8}];
  chiJ = Sum[jMul[Dot, jPart[gamJ, nu], DpsiJ[[nu]]], {nu, 8}];
  red[Sum[gamJ[[1, mu]].(chiJ[[2, mu]] + OmJ[[1, mu]].chiJ[[1]]), {mu, 8}]]
];

D16GeoSpinorLaplacian[geo_, fld_, omKey_: "Omega"] := Module[{OmJ = geo[omKey], ginv = geo["ginv"][[1]], G = geo["christoffel"][[1]], DpsiJ},
  DpsiJ = Table[fld["dpsi"][[mu]] + jMul[Dot, jPart[OmJ, mu], fld["psi"]], {mu, 8}];
  red[Sum[ginv[[mu, nu]] (DpsiJ[[nu, 2, mu]] + OmJ[[1, mu]].DpsiJ[[nu, 1]] - Sum[G[[l, mu, nu]] DpsiJ[[l, 1]], {l, 8}]), {mu, 8}, {nu, 8}]]
];

(* field equations as jets:  E = gamma^mu D_mu Psi - (m + lambda S) Psi,
   Ebar = (D_mu Psibar) gamma^mu + (m + lambda S) Psibar *)
fieldEquationJets[geo_, lag_] := Module[{gamJ = geo["gamma"], m = lag["m"], lam = lag["lambda"], ePsi, eBar},
  ePsi = Sum[jMul[Dot, jPart[gamJ, mu], lag["Dpsi"][[mu]]], {mu, 8}] - m lag["psi"] - lam jMul[Times, lag["S"], lag["psi"]];
  eBar = Sum[jMul[Dot, lag["Dbar"][[mu]], jPart[gamJ, mu]], {mu, 8}] + m lag["bar"] + lam jMul[Times, lag["S"], lag["bar"]];
  {ePsi, eBar}
];

(* Solve the field equations and their first derivatives at the point for the x4-derivatives
   (curved index 4 = list position 5).  free = {p0, p1, p2, q0, q1, q2}; the entries
   p1[[5]], q1[[5]], p2[[5, All]], p2[[All, 5]], q2[[5, All]], q2[[All, 5]] are ignored and
   replaced by the solution.  Returns {solvedData, residualZeroQ}. *)
D16GeoSolveOnShell[geo_, free_, m_, lam_] := Module[
  {p0, p1, p2, q0, q1, q2, u1, v1, u2, v2, solve, fld, lag, eqs, sol1, sol2, sol3, e1, e2, resid, all},
  {p0, p1, p2, q0, q1, q2} = free;
  u1 = Array[Unique["u1"] &, 16]; v1 = Array[Unique["v1"] &, 16];
  u2 = Table[Array[Unique["u2"] &, 16], {8}]; v2 = Table[Array[Unique["v2"] &, 16], {8}];
  p1 = ReplacePart[p1, 5 -> u1]; q1 = ReplacePart[q1, 5 -> v1];
  Do[p2[[5, nu]] = u2[[nu]]; p2[[nu, 5]] = u2[[nu]]; q2[[5, nu]] = v2[[nu]]; q2[[nu, 5]] = v2[[nu]], {nu, 8}];
  solve[eqsIn_, vars_] := Module[{ca = CoefficientArrays[eqsIn, vars], x},
    If[Length[ca] =!= 2, Throw["nonlinear on-shell system"]];
    x = LinearSolve[ca[[2]], -ca[[1]]];
    Thread[vars -> red[Normal[x]]]];
  fld = D16GeoFieldJets[p0, p1, p2, q0, q1, q2];
  lag = D16GeoLagrangianJets[geo, fld, m, lam];
  {e1, e2} = fieldEquationJets[geo, lag];
  sol1 = solve[Join[e1[[1]], e2[[1]]], Join[u1, v1]];
  sol2 = Join @@ Table[If[nu == 5, {}, solve[red[Join[e1[[2, nu]], e2[[2, nu]]] /. sol1], Join[u2[[nu]], v2[[nu]]]]], {nu, 8}];
  sol3 = solve[red[Join[e1[[2, 5]], e2[[2, 5]]] /. sol1 /. sol2], Join[u2[[5]], v2[[5]]]];
  all = Join[sol1, sol2, sol3];
  resid = red[{e1, e2} /. all];
  {red[{p0, p1, p2, q0, q1, q2} /. all], zeroQ[resid]}
];

(* ========================================================================= *)
(* 7. Grassmann algebra with jet-valued coefficients                          *)
(* ========================================================================= *)
(* An element is an Association  sortedGeneratorList -> coefficient,  where a coefficient
   is a 9-list {value, d_0 value, ..., d_7 value} (explicit x-dependence of the coefficient
   at the evaluation point).  Generators: q0[a] = Psi^dagger_a (ids 1..16), p0[a] = Psi_a
   (17..32), q1[mu,a] = d_mu Psi^dagger_a, p1[mu,a] = d_mu Psi_a, q2/p2 = second derivatives
   (symmetric in mu,nu).  All generators are odd and anticommute. *)

gQ0[a_] := a + 1; gP0[a_] := 17 + a;
gQ1[mu_, a_] := 33 + 16 mu + a; gP1[mu_, a_] := 161 + 16 mu + a;
pairIndex[mu_, nu_] := With[{i = Min[mu, nu], j = Max[mu, nu]}, 8 i - i (i - 1)/2 + (j - i)];
gQ2[mu_, nu_, a_] := 289 + 16 pairIndex[mu, nu] + a; gP2[mu_, nu_, a_] := 865 + 16 pairIndex[mu, nu] + a;
dmapTab = Table[
  Which[id <= 16, gQ1[lam, id - 1], id <= 32, gP1[lam, id - 17],
    id <= 160, gQ2[lam, Quotient[id - 33, 16], Mod[id - 33, 16]],
    True, gP2[lam, Quotient[id - 161, 16], Mod[id - 161, 16]]], {id, 1, 288}, {lam, 0, 7}];

cjOne = Join[{1}, ConstantArray[0, 8]];
cjVal[v_] := Join[{v}, ConstantArray[0, 8]];
cjMul[a_, b_] := red[Prepend[a[[1]] b[[2 ;;]] + b[[1]] a[[2 ;;]], a[[1]] b[[1]]]];
cjZeroQ[c_] := AllTrue[red[c], (Expand[#] === 0) &];
cjOf[mj_, i_, j_] := Prepend[mj[[2, All, i, j]], mj[[1, i, j]]];
cjScalar[sj_] := Prepend[sj[[2]], sj[[1]]];

gClean[x_Association] := Select[red /@ x, ! cjZeroQ[#] &];
gCollect[pairs_List] := If[pairs === {}, <||>, gClean[GroupBy[pairs, First -> Last, Total]]];
gPairs[x_Association] := KeyValueMap[List, x];
gSum[list_List] := gCollect[Flatten[gPairs /@ list, 1]];
gAdd[xs___Association] := gSum[{xs}];
gNeg[x_Association] := Map[-# &, x];
gScaleNum[c_, x_Association] := If[c === 0, <||>, gClean[Map[c # &, x]]];
gScaleJet[c_, x_Association] := If[cjZeroQ[c], <||>, gClean[Map[cjMul[c, #] &, x]]];
gMul[x_Association, y_Association] := Module[{kx = Keys[x], vx = Values[x], ky = Keys[y], vy = Values[y], acc},
  If[kx === {} || ky === {}, Return[<||>]];
  acc = Reap[Do[
      If[Intersection[kx[[i]], ky[[j]]] === {},
        With[{mm = Join[kx[[i]], ky[[j]]]}, Sow[{Sort[mm], Signature[mm] cjMul[vx[[i]], vy[[j]]]}]]],
      {i, Length[kx]}, {j, Length[ky]}]][[2]];
  If[acc === {}, <||>, gCollect[First[acc]]]
];
gVal[x_Association] := gClean[Map[cjVal[#[[1]]] &, x]];
gLeftD[x_Association, id_] := gCollect[KeyValueMap[Function[{key, c},
    With[{p = FirstPosition[key, id]}, If[MissingQ[p], Nothing, {Delete[key, p[[1]]], (-1)^(p[[1]] - 1) c}]]], x]];
gRightD[x_Association, id_] := gCollect[KeyValueMap[Function[{key, c},
    With[{p = FirstPosition[key, id]}, If[MissingQ[p], Nothing, {Delete[key, p[[1]]], (-1)^(Length[key] - p[[1]]) c}]]], x]];
(* total derivative d_lam (lam = 0..7) at the point; result carries values only *)
gTotalDValue[x_Association, lam_] := gCollect[Flatten[KeyValueMap[Function[{key, c},
    Join[
      If[Expand[c[[lam + 2]]] === 0, {}, {{key, cjVal[c[[lam + 2]]]}}],
      Table[With[{new = ReplacePart[key, p -> dmapTab[[key[[p]], lam + 1]]]},
          If[DuplicateFreeQ[new], {Sort[new], Signature[new] cjVal[c[[1]]]}, Nothing]], {p, Length[key]}]]], x], 1]];
gZeroQ[x_Association] := Length[gClean[x]] === 0;
gVecAdd[u_List, v_List] := MapThread[gAdd, {u, v}];
gVecNeg[u_List] := gNeg /@ u;
gVecScaleNum[c_, u_List] := gScaleNum[c, #] & /@ u;
gMatVec[mj_, v_List] := Table[gSum[Table[gScaleJet[cjOf[mj, i, j], v[[j]]], {j, Length[v]}]], {i, Length[mj[[1]]]}];
gRowMat[v_List, mj_] := Table[gSum[Table[gScaleJet[cjOf[mj, i, j], v[[i]]], {i, Length[v]}]], {j, Length[mj[[1, 1]]]}];
gDot[u_List, v_List] := gSum[MapThread[gMul, {u, v}]];
(* coefficient matrix of a vector of Grassmann-linear elements w.r.t. generator ids *)
gLinearMatrix[vec_List, ids_List] := Table[With[{c = Lookup[vec[[i]], Key[{ids[[j]]}], cjVal[0]]}, red[c[[1]]]], {i, Length[vec]}, {j, Length[ids]}];
gIsLinearIn[vec_List, ids_List] := AllTrue[vec, Function[e, AllTrue[Keys[e], Length[#] == 1 && MemberQ[ids, First[#]] &]]];

gGenVec[f_] := Table[<|{f[a]} -> cjOne|>, {a, 0, 15}];

(* complex Lagrangian (CONTRACT section 5) as a Grassmann polynomial with jet coefficients *)
gComplexLagrangian[geo_, m_, lam_, omKey_: "Omega"] := Module[
  {Om = geo[omKey], gam = geo["gamma"], CJ = jConst[$C], psb, psi, dpsb, dpsi, bar, dbar, Dpsi, Dbar, S, kin, Ls, L},
  psb = gGenVec[gQ0]; psi = gGenVec[gP0];
  dpsb = Table[gGenVec[gQ1[mu, #] &], {mu, 0, 7}]; dpsi = Table[gGenVec[gP1[mu, #] &], {mu, 0, 7}];
  bar = gRowMat[psb, CJ]; dbar = Table[gRowMat[dpsb[[mu]], CJ], {mu, 8}];
  Dpsi = Table[gVecAdd[dpsi[[mu]], gMatVec[jPart[Om, mu], psi]], {mu, 8}];
  Dbar = Table[gVecAdd[dbar[[mu]], gVecNeg[gRowMat[bar, jPart[Om, mu]]]], {mu, 8}];
  S = gDot[bar, psi];
  kin = gSum[Table[gAdd[gDot[bar, gMatVec[jPart[gam, mu], Dpsi[[mu]]]], gNeg[gDot[gRowMat[Dbar[[mu]], jPart[gam, mu]], psi]]], {mu, 8}]];
  Ls = gAdd[gScaleNum[1/2, kin], gScaleNum[-m, S], gScaleNum[-lam/2, gMul[S, S]]];
  L = gScaleJet[cjScalar[geo["sqrtg"]], Ls];
  <|"L" -> L, "Ls" -> Ls, "S" -> S, "bar" -> bar, "psi" -> psi, "psb" -> psb, "Dpsi" -> Dpsi, "Dbar" -> Dbar|>
];

(* Euler-Lagrange operators from the jet identity  d_lam (dL/du_{mu,a}) = d L_lam/du_{mu,a}
   - delta_{lam mu} dL/du_a  (exact for Grassmann left and right derivatives):
   EL_a = dL0/du_a - Sum_mu d_mu (dL/du_{mu a}) = 9 dL0/du_a - Sum_mu d L_mu / d u_{mu a}. *)
gEulerLagrange[L_Association, gen0_, gen1_, side_] := Module[{L0 = gVal[L], Lmu, der},
  der = If[side === "left", gLeftD, gRightD];
  Lmu = Table[gTotalDValue[L, mu], {mu, 0, 7}];
  Table[gAdd[gScaleNum[9, der[L0, gen0[a]]], gNeg[gSum[Table[der[Lmu[[mu + 1]], gen1[mu, a]], {mu, 0, 7}]]]], {a, 0, 15}]
];

(* ========================================================================= *)
(* 8. Deterministic exact random rationals (64-bit LCG, reproducible anywhere) *)
(* ========================================================================= *)
(* state_{k+1} = (6364136223846793005 state_k + 1442695040888963407) mod 2^64, state_0 = seed;
   rational_k = (floor(state_k / 2^33) mod 19 - 9) / (floor(state_k / 2^13) mod 9 + 1)
   for k = 1..n. *)
lcgNext[s_] := Mod[6364136223846793005 s + 1442695040888963407, 2^64];
D16GeoRandomRationals[seed_Integer, n_Integer] := Module[{states = Rest[NestList[lcgNext, seed, n]]},
  (Mod[Quotient[#, 2^33], 19] - 9)/(Mod[Quotient[#, 2^13], 9] + 1) & /@ states];
randomSymmetric2[seed_] := Module[{r = D16GeoRandomRationals[seed, 36*16], k = 0, arr},
  arr = ConstantArray[0, {8, 8, 16}];
  Do[With[{v = r[[16 k + 1 ;; 16 k + 16]]}, arr[[i, j]] = v; arr[[j, i]] = v; k++], {i, 8}, {j, i, 8}];
  arr];
randomFieldData[seed_] := {
  D16GeoRandomRationals[seed, 16], Partition[D16GeoRandomRationals[seed + 1, 128], 16], randomSymmetric2[seed + 2],
  D16GeoRandomRationals[seed + 3, 16], Partition[D16GeoRandomRationals[seed + 4, 128], 16], randomSymmetric2[seed + 5]};

(* ========================================================================= *)
(* 9. Test geometries                                                         *)
(* ========================================================================= *)

xs = Table[Symbol["Dirac16Complex`Geometry`Private`x" <> ToString[k]], {k, 0, 7}];

g1P[x_List, mu_Integer, a_Integer] := If[mu =!= a,
  (1/10) ((mu + 1) x[[a + 1]] - (a + 1) x[[mu + 1]]) + (1/20) x[[mu + 1]] x[[a + 1]] + (1/30) x[[Mod[mu + a, 8] + 1]]^2,
  (1/10) x[[mu + 1]]^2 + (1/40) x[[Mod[mu + 1, 8] + 1]]];
D16GeoG1Frame[x_List] := Table[KroneckerDelta[mu, a] + g1P[x, mu, a], {mu, 0, 7}, {a, 0, 7}];
g1Points = {
  {1/7, -2/9, 1/5, 3/11, -1/13, 2/17, -3/19, 1/23},
  {-1/3, 1/4, 2/7, -1/5, 1/6, -2/11, 1/9, 3/13},
  {2/9, 1/8, -1/7, 1/10, -3/14, 1/12, 2/15, -1/16}};

(* G2: primordial field; exact point data  w = sin(z)^(1/6) rational, sn = w^6, cs = cos z
   algebraic (cs^2 = 1 - sn^2), ea = exp(a4(t)) rational (a4(t) = Log[ea]), A1 = a4'(t),
   A2 = a4''(t), A3 = a4'''(t) rational, H rational. *)
g2Points = {
  <|"w" -> 1/2, "H" -> 2/3, "ea" -> 2, "A1" -> 3/7, "A2" -> -5/11, "A3" -> 2/13|>,
  <|"w" -> 2/3, "H" -> 1/5, "ea" -> 3/2, "A1" -> -4/9, "A2" -> 7/12, "A3" -> -1/8|>,
  <|"w" -> 3/4, "H" -> 5/7, "ea" -> 5/7, "A1" -> 6/5, "A2" -> -2/3, "A3" -> 3/10|>};

g2FrameSymbolic[H_] := Module[{z = 6 H xs[[1]], t = H xs[[5]], s},
  s = Sin[z];
  DiagonalMatrix[{Cot[z], s^(1/6) E^(a4[t]), s^(1/6) E^(a4[t]), s^(1/6) E^(a4[t]), 1,
    s^(1/6) E^(-a4[t]), s^(1/6) E^(-a4[t]), s^(1/6) E^(-a4[t])}]];

g2Rules[pt_] := Module[{H = pt["H"], sn = pt["w"]^6, z, t},
  z = 6 H xs[[1]]; t = H xs[[5]];
  {Derivative[1][a4][t] -> pt["A1"], Derivative[2][a4][t] -> pt["A2"], Derivative[3][a4][t] -> pt["A3"],
   a4[t] -> Log[pt["ea"]], Sin[z] -> sn, Cos[z] -> cs, Cot[z] -> cs/sn, Csc[z] -> 1/sn, Tan[z] -> sn/cs, Sec[z] -> 1/cs}];
g2Alg[pt_] := {cs, 2, 1 - (pt["w"]^6)^2};

(* G3: homogeneous diagonal (Bianchi-I type) Gaussian-normal vielbein h_i(x4), h_4 = 1:
   h_i = 1 + x4^2/(i+2), evaluated at x4 in {1/3, -2/5, 3/7}, other coordinates 0. *)
g3Frame[x_List] := DiagonalMatrix[Table[If[i == 4, 1, 1 + x[[5]]^2/(i + 2)], {i, 0, 7}]];
g3Points = {1/3, -2/5, 3/7};

End[];
EndPackage[];
