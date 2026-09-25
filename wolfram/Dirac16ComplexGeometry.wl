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
   reduced to the canonical basis {1, cs} (see D16GeoSetAlgebraic); the first-order
   (infinitesimal) local spin check uses exact dual numbers kappa^2 = 0.  Field jets
   (Psi, d Psi, d d Psi and the same for Psi^dagger) are independent exact numbers or,
   for the Euler-Lagrange, canonical-momentum and notebook-Lg checks, genuine Grassmann
   generators (a small exact Grassmann algebra with jet-valued coefficients is part of
   this package).

   Test geometries: G1 = general non-diagonal polynomial vielbein at three rational
   points; G2 = primordial field with arbitrary a4 at three exact points; G3 = homogeneous
   Bianchi-I (minisuperspace) frame for the tetrad variation of the action and the
   homogeneous reduction of T_{mu nu}.  D16GeoReport[] runs every check (43 checks).

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
D16GeoSetAlgebraic::usage = "D16GeoSetAlgebraic[None] or D16GeoSetAlgebraic[{{s, n, c}, ...}] selects exact reduction s^n -> c (c = 0: nilpotent parameter) for all subsequent jet arithmetic.";
D16GeoReduce::usage = "D16GeoReduce[x] reduces x to the canonical form of the current exact number field.";
D16GeoZeroQ::usage = "D16GeoZeroQ[x] is True iff every entry of x is exactly zero in the current exact number field.";
D16GeoSymbolicGeometry::usage = "D16GeoSymbolicGeometry[frame, coords] returns the symbolic metric, inverse metric, Christoffel symbols, omegaMixed, omegaLower, Omega, OmegaNotebook and curved gammas of the vielbein frame[[mu,a]] = e_mu^a.";
D16GeoSymbolicCovariantDerivative::usage = "D16GeoSymbolicCovariantDerivative[geo, psi, coords] is {D_mu psi} = {d_mu psi + Omega_mu psi} for a symbolic geometry from D16GeoSymbolicGeometry.";
D16GeoSymbolicCovariantDerivativeBar::usage = "D16GeoSymbolicCovariantDerivativeBar[geo, psibar, coords] is {d_mu psibar - psibar Omega_mu}.";
D16GeoSymbolicDirac::usage = "D16GeoSymbolicDirac[geo, psi, coords] is gamma^mu D_mu psi.";
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

(* $alg is None or a list of specs {s, n, c}: s is a symbol with s^n = c.  c =!= 0: s is the
   algebraic number c^(1/n) (x^n - c irreducible over Q, canonical basis 1, s, ..., s^(n-1));
   c === 0: s is a nilpotent (dual-number) parameter, used for exact first-order variations. *)
$alg = None;
D16GeoSetAlgebraic[spec_] := ($alg = spec);
red[x_] := If[$alg === None, x,
  Fold[Function[{acc, sp}, acc /. Power[sp[[1]], k_Integer] :> sp[[3]]^Floor[k/sp[[2]]] sp[[1]]^Mod[k, sp[[2]]]], Expand[x], $alg]];
D16GeoReduce[x_] := red[x];
zeroQ[x_] := AllTrue[Flatten[{red[x]}], (Expand[#] === 0) &];
D16GeoZeroQ[x_] := zeroQ[x];
(* exact value of a canonical element (algebraic symbols -> radicals, nilpotent parameters -> 0) *)
exactValue[x_] := If[$alg === None, x, red[x] /. (If[#[[3]] === 0, #[[1]] -> 0, #[[1]] -> #[[3]]^(1/#[[2]])] & /@ $alg)];
numValue[x_] := N[exactValue[x], 30];
(* the entry of largest absolute value, returned exactly (canonical form) with a positive sign *)
maxAbsEntry[x_] := Module[{flat = Select[Flatten[{red[x]}], ! (Expand[#] === 0) &], vals, pos},
  If[flat === {}, Return[0]];
  vals = Abs[numValue /@ flat]; pos = First[Ordering[vals, -1]];
  red[If[numValue[flat[[pos]]] < 0, -flat[[pos]], flat[[pos]]]]];
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

D16GeoSymbolicCovariantDerivative[geo_Association, psi_List, coords_List] :=
  Table[D[psi, coords[[mu]]] + geo["Omega"][[mu]].psi, {mu, Length[coords]}];
D16GeoSymbolicCovariantDerivativeBar[geo_Association, bar_List, coords_List] :=
  Table[D[bar, coords[[mu]]] - bar.geo["Omega"][[mu]], {mu, Length[coords]}];
D16GeoSymbolicDirac[geo_Association, psi_List, coords_List] := With[{dp = D16GeoSymbolicCovariantDerivative[geo, psi, coords]},
  Sum[geo["curvedGammas"][[mu]].dp[[mu]], {mu, Length[coords]}]];

(* ========================================================================= *)
(* 5. Vielbein jets and jet geometry                                          *)
(* ========================================================================= *)

D16GeoFrameJet[frame_, coords_, rules_] := Module[{e1, e2},
  e1 = Table[D[frame, coords[[l]]], {l, 8}];
  e2 = Table[D[e1[[l]], coords[[k]]], {l, 8}, {k, 8}];
  red[{frame, e1, e2} /. rules]
];

Options[D16GeoJetGeometry] = {"SqrtSign" -> Automatic, "Curvature" -> True};
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
  If[TrueQ[OptionValue["Curvature"]],
    riem = red[Table[Gd[[m, r, nn, s]] - Gd[[nn, r, m, s]] + Sum[Gv[[r, m, l]] Gv[[l, nn, s]] - Gv[[r, nn, l]] Gv[[l, m, s]], {l, 8}],
      {r, 8}, {s, 8}, {m, 8}, {nn, 8}]];
    ricci = red[Table[Sum[riem[[r, s, r, nn]], {r, 8}], {s, 8}, {nn, 8}]];
    rs = red[Sum[ginvJ[[1, s, nn]] ricci[[s, nn]], {s, 8}, {nn, 8}]];
    einstein = red[ginvJ[[1]].ricci - (rs/2) id8],
    riem = ricci = rs = einstein = Missing["NotComputed"]];
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
gEulerLagrangeIdentity[L_Association, gen0_, gen1_, side_] := Module[{L0 = gVal[L], Lmu, der},
  der = If[side === "left", gLeftD, gRightD];
  Lmu = Table[gTotalDValue[L, mu], {mu, 0, 7}];
  Table[gAdd[gScaleNum[9, der[L0, gen0[a]]], gNeg[gSum[Table[der[Lmu[[mu + 1]], gen1[mu, a]], {mu, 0, 7}]]]], {a, 0, 15}]
];
(* direct form: dL/du_a - Sum_mu d_mu (dL/du_{mu a}), the inner derivative keeps the jet
   coefficients so that the total derivative d_mu acts on coefficients and generators *)
gEulerLagrange[L_Association, gen0_, gen1_, side_] := Module[{der = If[side === "left", gLeftD, gRightD]},
  Table[gAdd[gVal[der[L, gen0[a]]], gNeg[gSum[Table[gTotalDValue[der[L, gen1[mu, a]], mu], {mu, 0, 7}]]]], {a, 0, 15}]
];
gSameVectorQ[u_List, v_List] := Length[u] === Length[v] && AllTrue[Range[Length[u]], gZeroQ[gAdd[gVal[u[[#]]], gNeg[gVal[v[[#]]]]]] &];

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
g2Alg[pt_] := {{cs, 2, 1 - (pt["w"]^6)^2}};

(* G3: homogeneous diagonal (Bianchi-I type) Gaussian-normal vielbein h_i(x4), h_4 = 1:
   h_i = 1 + x4^2/(i+2), evaluated at x4 in {1/3, -2/5, 3/7}, other coordinates 0. *)
g3Frame[x_List] := DiagonalMatrix[Table[If[i == 4, 1, 1 + x[[5]]^2/(i + 2)], {i, 0, 7}]];
g3Points = {1/3, -2/5, 3/7};

(* model parameters per evaluation point (k = 1, 2, 3) *)
$mList = {3/7, -2/5, 5/9};          (* Dirac mass m *)
$lamList = {5/11, 7/13, -3/8};      (* U(S) = (lambda/2) S^2 *)
$hmList = {2/3, -5/7, 4/9};         (* notebook H M in Lg[] *)

(* ========================================================================= *)
(* 10. Value-only helpers (probe fields give coefficient matrices directly)   *)
(* ========================================================================= *)

lagValue[geo_, p0_, p1_, q0_, q1_, m_, lam_, omKey_: "Omega"] := Module[
  {Om = geo[omKey][[1]], gam = geo["gamma"][[1]], bar, Dpsi, Dbar, S, kin, Ls},
  bar = q0.$C;
  Dpsi = Table[p1[[mu]] + Om[[mu]].p0, {mu, 8}];
  Dbar = Table[q1[[mu]].$C - bar.Om[[mu]], {mu, 8}];
  S = bar.p0;
  kin = (1/2) Sum[bar.gam[[mu]].Dpsi[[mu]] - Dbar[[mu]].gam[[mu]].p0, {mu, 8}];
  Ls = red[kin - m S - If[lam === 0, 0, (lam/2) S^2]];
  <|"bar" -> bar, "Dpsi" -> Dpsi, "Dbar" -> Dbar, "S" -> S, "Ls" -> Ls, "psi" -> p0|>
];
emtValue[geo_, lv_] := Module[{gl = geo["gammaLower"][[1]], g = geo["g"][[1]], A, B},
  A = Table[lv["bar"].gl[[mu]].lv["Dpsi"][[nu]], {mu, 8}, {nu, 8}];
  B = Table[lv["Dbar"][[mu]].gl[[nu]].lv["psi"], {mu, 8}, {nu, 8}];
  red[Table[-(1/4) (A[[mu, nu]] + A[[nu, mu]] - B[[mu, nu]] - B[[nu, mu]]) + g[[mu, nu]] lv["Ls"], {mu, 8}, {nu, 8}]]
];
hermConj[mat_] := Transpose[mat] /. Complex[a_, b_] :> Complex[a, -b];   (* all symbols here are real *)
inertia[mat_] := Module[{x, cl, cln, ch},
  ch[l_] := Count[Partition[Sign[l], 2, 1], {s1_, s2_} /; s1 =!= s2];
  cl = Select[CoefficientList[CharacteristicPolynomial[mat, x], x], # =!= 0 &];
  cln = Select[CoefficientList[CharacteristicPolynomial[mat, x] /. x -> -x, x], # =!= 0 &];
  {ch[cl], ch[cln], Length[mat] - ch[cl] - ch[cln]}];
decimalString[x_] := ToString[CForm[N[exactValue[x], 20]]];
boolString[b_] := If[TrueQ[b], "true", "false"];
zp1 = ConstantArray[0, {8, 16}]; zp2 = ConstantArray[0, {8, 8, 16}];
zm16 = ConstantArray[0, {16, 16}]; zm1 = ConstantArray[0, {8, 16, 16}];
unitSlot[l_] := ReplacePart[zm1, l -> id16];

(* ========================================================================= *)
(* 11. Finite local Spin(4,4) transformation with exact rational unit fields  *)
(* ========================================================================= *)
(* n(y) = e_A - 2 <e_A,k(y)>/<k(y),k(y)> k(y) is the reflection of the unit vector e_A in the
   hyperplane orthogonal to the polynomial field k(y), so <n,n> = <e_A,e_A> = +-1 exactly and
   n is rational in y = x - point.  R = nslash mslash is an exact local Spin(4,4) field with
   R^{-1} = mslash nslash/(<n,n><m,m>), and R gamma^a R^{-1} = Lambda^c_a gamma^c with
   Lambda = P_n P_m, P_u[[c,a]] = delta_ca - 2 u_c eta_aa u_a/<u,u>. *)
ys = Table[Symbol["Dirac16Complex`Geometry`Private`y" <> ToString[k]], {k, 0, 7}];
ip[u_, v_] := Sum[$etaDiag[[a]] u[[a]] v[[a]], {a, 8}];
unitField[base_Integer, k0_List, seed_Integer] := Module[{r1, r2, k, eA = UnitVector[8, base + 1]},
  r1 = Partition[D16GeoRandomRationals[seed, 64], 8];
  r2 = Partition[Partition[D16GeoRandomRationals[seed + 1, 512], 8], 8];
  k = Table[k0[[a]] + Sum[r1[[a, b]] ys[[b]], {b, 8}] + (1/2) Sum[r2[[a, b, c]] ys[[b]] ys[[c]], {b, 8}, {c, 8}], {a, 8}];
  eA - 2 ip[eA, k]/ip[k, k] k];
vectorJet2[v_] := Module[{d1 = Table[D[v, ys[[l]]], {l, 8}]},
  {v /. Thread[ys -> 0], d1 /. Thread[ys -> 0], Table[D[d1[[l]], ys[[kk]]], {l, 8}, {kk, 8}] /. Thread[ys -> 0]}];
(* first-order (infinitesimal) family: n_kappa = reflection of the unit field m in k = m + kappa w.
   With <m,m> = 1:  n_kappa = -m + kappa (2 <m,w> m - 2 w) + O(kappa^2), so
   R_kappa = n_kappa mslash = -1 + kappa [mslash, wslash] + O(kappa^2): a local spin(4,4) generator
   epsilon(x) = [mslash, wslash] with nonzero derivatives.  kappa^2 = 0 exactly (dual numbers). *)
kappa = Symbol["Dirac16Complex`Geometry`Private`kappa"];
infinitesimalW[seed_Integer] := Module[{r0, r1},
  r0 = D16GeoRandomRationals[seed, 8];
  r1 = Partition[D16GeoRandomRationals[seed + 1, 64], 8];
  Table[r0[[a]] + Sum[r1[[a, b]] ys[[b]], {b, 8}], {a, 8}]];
infinitesimalJet[mJ_, wJ_] := Module[{aJ = j2Mul[ip, mJ, wJ]},
  -mJ + kappa (2 j2Mul[Times, aJ, mJ] - 2 wJ)];
reflectionJet2[uJ_, norm_] := Module[{outer},
  outer = j2Mul[Function[{u, v}, Outer[Times, u, $etaDiag v]], uJ, uJ];
  {id8 - (2/norm) outer[[1]], -(2/norm) outer[[2]], -(2/norm) outer[[3]]}];

spinInvariance[geo_, fj_, data_, m_, lam_, seed_] := Module[
  {n, mv, mt, nn, mm, mtt, nJ, mJ, mtJ, res = <||>, transform, fld, lagRef, lagRefNB},
  n = unitField[0, {2, 1, -1, 1, 1, -1, 1, 1}, seed];
  mv = unitField[1, {1, 3, 1, -1, 2, 1, -1, 1}, seed + 2];
  mt = unitField[4, {1, 1, 2, -1, 3, 1, 1, -1}, seed + 4];
  nn = Together[ip[n, n]]; mm = Together[ip[mv, mv]]; mtt = Together[ip[mt, mt]];
  res["unitNorms"] = (nn === 1 && mm === 1 && mtt === -1);
  nJ = vectorJet2[n]; mJ = vectorJet2[mv]; mtJ = vectorJet2[mt];
  fld = D16GeoFieldJets @@ data;
  (* with Psi^dagger -> Psi^dagger R^T one has Psibar -> sigma Psibar R^-1, sigma = <n,n><m,m>, hence
     S -> sigma S and L[m, lambda] -> sigma L[m, sigma lambda] (kinetic and mass terms flip with sigma,
     the even self-interaction U = lambda S^2/2 does not). *)
  transform[uJ_, vJ_, sigma_] := Module[{usl, vsl, RJ, RinvJ, LamJ, frameP, geoP, psiP, psbP, fldP, lagP, lagPNB, out = <||>},
    lagRef = D16GeoLagrangianJets[geo, fld, m, sigma lam];
    lagRefNB = D16GeoLagrangianJets[geo, fld, m, sigma lam, "OmegaNotebook"];
    usl = j2Lin[#.$gam &, uJ]; vsl = j2Lin[#.$gam &, vJ];
    RJ = j2Mul[Dot, usl, vsl];
    RinvJ = j2Mul[Dot, vsl, usl]/sigma;
    LamJ = j2Mul[Dot, reflectionJet2[uJ, 1], reflectionJet2[vJ, sigma]];
    out["RinverseValue"] = zeroQ[RJ[[1]].RinvJ[[1]] - id16];
    out["LambdaInO44"] = zeroQ[Transpose[LamJ[[1]]].$eta.LamJ[[1]] - $eta];
    out["adjointAction"] = zeroQ[Table[RJ[[1]].$gam[[a]].RinvJ[[1]] - Sum[LamJ[[1, c, a]] $gam[[c]], {c, 8}], {a, 8}]];
    frameP = j2Mul[Dot, fj, j2Lin[$eta.Transpose[#].$eta &, LamJ]];
    geoP = D16GeoJetGeometry[frameP, "Curvature" -> False];
    out["metricInvariant"] = zeroQ[geoP["g"] - geo["g"]];
    out["gammaCovariant"] = zeroQ[Table[geoP["gamma"][[1, mu]] - RJ[[1]].geo["gamma"][[1, mu]].RinvJ[[1]], {mu, 8}]];
    out["connectionTransformation"] = zeroQ[Table[geoP["Omega"][[1, mu]] -
        (RJ[[1]].geo["Omega"][[1, mu]].RinvJ[[1]] - RJ[[2, mu]].RinvJ[[1]]), {mu, 8}]];
    psiP = j2Mul[Dot, RJ, {data[[1]], data[[2]], data[[3]]}];
    psbP = j2Mul[Dot, {data[[4]], data[[5]], data[[6]]}, j2Lin[Transpose, RJ]];
    fldP = D16GeoFieldJets[psiP[[1]], psiP[[2]], psiP[[3]], psbP[[1]], psbP[[2]], psbP[[3]]];
    lagP = D16GeoLagrangianJets[geoP, fldP, m, lam];
    lagPNB = D16GeoLagrangianJets[geoP, fldP, m, lam, "OmegaNotebook"];
    out["lagrangianRatio"] = sigma;
    out["notebookFirstOrderChange"] = maxAbsEntry[Coefficient[red[lagPNB["L"][[1]] - sigma lagRefNB["L"][[1]]], kappa]];
    out["generatorFirstOrderPart"] = maxAbsEntry[Coefficient[RJ[[1]], kappa]];
    out["lagrangianTransforms"] = zeroQ[lagP["L"] - sigma lagRef["L"]];
    out["naiveSignFlipFailsForLambda"] = If[sigma === 1, True,
      ! zeroQ[lagP["L"] - sigma D16GeoLagrangianJets[geo, fld, m, lam]["L"]]];
    out["notebookLagrangianDifference"] = maxAbsEntry[lagPNB["L"][[1]] - sigma lagRefNB["L"][[1]]];
    out];
  res["spinZero"] = transform[nJ, mJ, 1];
  res["spinMixed"] = transform[nJ, mtJ, -1];
  Block[{$alg = Join[If[$alg === None, {}, $alg], {{kappa, 2, 0}}], nkJ},
    nkJ = red[infinitesimalJet[mJ, vectorJet2[infinitesimalW[seed + 6]]]];
    res["infinitesimalUnitNorm"] = zeroQ[j2Mul[ip, nkJ, nkJ] - {1, ConstantArray[0, 8], ConstantArray[0, {8, 8}]}];
    res["infinitesimal"] = transform[nkJ, mJ, 1];
  ];
  res
];

(* ========================================================================= *)
(* 12. Checks on one geometry at one evaluation point                        *)
(* ========================================================================= *)

runGeometry[gl_String, k_Integer, geo_, fj_, pars_Association] := Module[
  {c = <||>, ms = <||>, add, mm, pre = gl <> ".p" <> ToString[k] <> ".", sfx = "_" <> gl,
   m = $mList[[k]], lam = $lamList[[k]], hm = $hmList[[k]], seed = pars["seed"],
   e0, g0, ginv0, inert, vp, omL, Gv, gam, gamL, Om, OmNB, sq, dGam, DG, DGnb, div, jac, riem, F, RF, RFmixed, spinFromR,
   cPlus, cMinus, cMixed, offData, fldOff, dsq, box, delta, rs, k0, cL, K, Kl, Ll, matLevel, dens,
   lagG, ELb, ELp, tvec, tgt, rvec, tgtp, okb, okp, Bq, Lp, Pi, PiT, noQdot, piOK, Kq, Qq, g44, gauss, Bm,
   nbLg, nbC, nbN, Xexp, onData, okOS, fldOn, lagOn, Ton, divOn, lagOff, Toff, divOff, S0, tr, expTr,
   symOK, Kt, Ktl, Ltl, herm, inv, gm, gamRows, DbarRows},
  add[name_, v_] := (c[name <> sfx] = TrueQ[Lookup[c, name <> sfx, True]] && TrueQ[v]);
  mm[name_, v_] := (ms[pre <> name] = v);
  e0 = geo["e"][[1]]; g0 = geo["g"][[1]]; ginv0 = geo["ginv"][[1]];
  Gv = geo["christoffel"][[1]]; gam = geo["gamma"]; gamL = geo["gammaLower"];
  Om = geo["Omega"]; OmNB = geo["OmegaNotebook"]; sq = geo["sqrtg"]; rs = geo["scalarCurvature"];

  (* --- nondegeneracy of the frame at the point --- *)
  inert = If[FreeQ[g0, cs], inertia[g0], {-1, -1, -1}];
  add["GEO_frameNondegenerate", ! zeroQ[geo["detFrame"]] && inert === {4, 4, 0} && ! zeroQ[ginv0[[5, 5]]]];
  mm["detFrame", exactString[geo["detFrame"]]];
  mm["detFrameDecimal", decimalString[geo["detFrame"]]];
  mm["metricInertia", ToString[inert]];
  mm["inverseMetric44", exactString[ginv0[[5, 5]]]];
  mm["sqrtAbsG", exactString[sq[[1]]]];
  mm["scalarCurvature", exactString[rs]];
  mm["scalarCurvatureDecimal", decimalString[rs]];

  (* --- vielbein postulate and omega --- *)
  vp = geo["vielbeinPostulate"];
  add["GEO_vielbeinPostulate", Dimensions[vp[[1]]] === {8, 8, 8} && zeroQ[vp[[1]]] && zeroQ[vp[[2]]]];
  mm["vielbeinPostulateComponentsZero", "512 values and 4096 first derivatives"];
  omL = geo["omegaLower"];
  add["GEO_omegaAntisymmetry", zeroQ[jLin[# + Transpose[#, {1, 3, 2}] &, omL]]];
  mm["nonzeroOmegaLower", Count[Flatten[omL[[1]]], x_ /; ! zeroQ[x]]];
  mm["nonzeroOmegaMixedSymmetricPart", Count[Flatten[geo["omegaMixed"][[1]] + Transpose[geo["omegaMixed"][[1]], {1, 3, 2}]], x_ /; ! zeroQ[x]]];

  (* --- D_mu gamma^nu --- *)
  dGam[OmJ_] := red[Table[gam[[2, mu, nu]] + Sum[Gv[[nu, mu, l]] gam[[1, l]], {l, 8}] + comm[OmJ[[1, mu]], gam[[1, nu]]], {mu, 8}, {nu, 8}]];
  DG = dGam[Om]; DGnb = dGam[OmNB];
  add["GEO_gammaCovariantConstancy", zeroQ[DG]];
  add["GEO_notebookContractionFails", ! zeroQ[DGnb]];
  mm["notebookDGammaMaxAbs", exactString[maxAbsEntry[DGnb]]];
  mm["notebookDGammaMaxAbsDecimal", decimalString[maxAbsEntry[DGnb]]];
  mm["notebookDGammaNonzeroEntries", Count[Flatten[DGnb], x_ /; ! zeroQ[x]]];

  (* --- divergence identity d_mu(sqrt|g| gamma^mu) = sqrt|g| [gamma^mu, Omega_mu] --- *)
  div = red[Sum[sq[[2, mu]] gam[[1, mu]] + sq[[1]] gam[[2, mu, mu]], {mu, 8}] - sq[[1]] Sum[comm[gam[[1, mu]], Om[[1, mu]]], {mu, 8}]];
  jac = red[Table[sq[[2, mu]] - sq[[1]] Sum[Gv[[r, r, mu]], {r, 8}], {mu, 8}]];
  add["GEO_divergenceIdentity", zeroQ[div] && zeroQ[jac]];
  mm["divergenceLhsMaxAbs", exactString[maxAbsEntry[Sum[sq[[2, mu]] gam[[1, mu]] + sq[[1]] gam[[2, mu, mu]], {mu, 8}]]]];

  (* --- curvature of the spin connection --- *)
  riem = geo["riemann"];
  F = red[Table[Om[[2, mu, nu]] - Om[[2, nu, mu]] + comm[Om[[1, mu]], Om[[1, nu]]], {mu, 8}, {nu, 8}]];
  RF = red[Table[$eta.Transpose[e0].riem[[All, All, mu, nu]].Transpose[geo["einv"][[1]]], {mu, 8}, {nu, 8}]];
  RFmixed = red[Table[Transpose[e0].riem[[All, All, mu, nu]].Transpose[geo["einv"][[1]]], {mu, 8}, {nu, 8}]];
  spinFromR[X_] := (1/2) Flatten[X].$Sflat;
  cPlus = zeroQ[F - Map[spinFromR, RF, {2}]];
  cMinus = zeroQ[F + Map[spinFromR, RF, {2}]];
  cMixed = zeroQ[F - Map[spinFromR, RFmixed, {2}]];
  add["GEO_curvature", cPlus && ! cMinus && ! cMixed && ! zeroQ[F]];
  mm["curvatureCandidate.plusHalfLowered", boolString[cPlus]];
  mm["curvatureCandidate.minusHalfLowered", boolString[cMinus]];
  mm["curvatureCandidate.plusHalfMixedNoEta", boolString[cMixed]];
  mm["curvatureFMaxAbs", exactString[maxAbsEntry[F]]];

  (* --- Lichnerowicz --- *)
  offData = randomFieldData[seed];
  fldOff = D16GeoFieldJets @@ offData;
  dsq = D16GeoDiracSquared[geo, fldOff]; box = D16GeoSpinorLaplacian[geo, fldOff];
  delta = red[dsq - box];
  k0 = First[Select[Range[16], offData[[1, #]] =!= 0 &]];
  cL = If[zeroQ[rs], Indeterminate, red[delta[[k0]]/(rs offData[[1, k0]])]];
  add["GEO_lichnerowicz", ! zeroQ[rs] && zeroQ[delta - cL rs offData[[1]]] && cL === -1/4 && ! zeroQ[delta - (1/4) rs offData[[1]]]];
  mm["lichnerowiczC", exactString[cL]];
  mm["lichnerowiczPlusQuarterHolds", boolString[zeroQ[delta - (1/4) rs offData[[1]]]]];

  (* --- Hermiticity of the Lagrangian (matrix level and coefficient level) --- *)
  matLevel = AllTrue[Range[8], zeroQ[hermConj[$C.$gam[[#]]] + $C.$gam[[#]]] &] && zeroQ[hermConj[$C] - $C];
  K = lagValue[geo, id16, zm1, id16, zm1, m, 0]["Ls"];
  Kl = Table[lagValue[geo, zm16, unitSlot[l], id16, zm1, m, 0]["Ls"], {l, 8}];
  Ll = Table[lagValue[geo, id16, zm1, zm16, unitSlot[l], m, 0]["Ls"], {l, 8}];
  dens = zeroQ[K - hermConj[K]] && AllTrue[Range[8], zeroQ[Ll[[#]] - hermConj[Kl[[#]]]] &];
  add["LAG_hermiticity", matLevel && dens];
  mm["hermiticity", "(C gamma^a)^dagger = -C gamma^a, C^dagger = C; Ls = psb K psi + psb K^mu d_mu psi + d_mu psb L^mu psi - (lambda/2) S^2 with K = K^dagger and L^mu = (K^mu)^dagger (Grassmann conjugation (theta1 theta2)^* = theta2^* theta1^*)"];

  (* --- Grassmann Euler-Lagrange equations of the complex Lagrangian --- *)
  lagG = gComplexLagrangian[geo, m, lam];
  gamRows = Table[gMatVec[jPart[gam, mu], lagG["Dpsi"][[mu]]], {mu, 8}];
  tvec = Table[gAdd[gSum[Table[gamRows[[mu, a]], {mu, 8}]], gScaleNum[-m, lagG["psi"][[a]]],
      gScaleNum[-lam, gMul[lagG["S"], lagG["psi"][[a]]]]], {a, 16}];
  tgt = gVal /@ (gScaleJet[cjScalar[sq], #] & /@ gMatVec[jConst[$C], tvec]);
  ELb = gEulerLagrange[lagG["L"], gQ0, gQ1, "left"];
  okb = AllTrue[Range[16], gZeroQ[gAdd[gVal[ELb[[#]]], gNeg[tgt[[#]]]]] &] && AllTrue[tgt, Length[#] > 0 &] &&
    gSameVectorQ[ELb, gEulerLagrangeIdentity[lagG["L"], gQ0, gQ1, "left"]];
  add["LAG_eulerLagrangePsibar", okb];
  mm["grassmannLagrangianMonomials", Length[lagG["L"]]];
  mm["grassmannELPsibarMonomials", Total[Length /@ ELb]];
  DbarRows = Table[gRowMat[lagG["Dbar"][[mu]], jPart[gam, mu]], {mu, 8}];
  rvec = Table[gAdd[gSum[Table[DbarRows[[mu, a]], {mu, 8}]], gScaleNum[m, lagG["bar"][[a]]],
      gScaleNum[lam, gMul[lagG["S"], lagG["bar"][[a]]]]], {a, 16}];
  tgtp = gVal /@ (gScaleJet[cjScalar[sq], gNeg[#]] & /@ rvec);
  ELp = gEulerLagrange[lagG["L"], gP0, gP1, "right"];
  okp = AllTrue[Range[16], gZeroQ[gAdd[gVal[ELp[[#]]], gNeg[tgtp[[#]]]]] &] && AllTrue[tgtp, Length[#] > 0 &] &&
    gSameVectorQ[ELp, gEulerLagrangeIdentity[lagG["L"], gP0, gP1, "right"]];
  add["LAG_eulerLagrangePsi", okp];
  mm["grassmannELPsiMonomials", Total[Length /@ ELp]];

  (* --- canonical momentum and anticommutator --- *)
  Bq = gScaleJet[cjScalar[sq], gDot[lagG["bar"], gMatVec[jPart[gam, 5], lagG["psi"]]]];
  Lp = gAdd[gVal[lagG["L"]], gScaleNum[1/2, gTotalDValue[Bq, 4]]];
  Pi = Table[gRightD[Lp, gP1[4, a]], {a, 0, 15}];
  PiT = gVal /@ (gScaleJet[cjScalar[sq], #] & /@ gRowMat[lagG["bar"], jPart[gam, 5]]);
  piOK = AllTrue[Range[16], gZeroQ[gAdd[Pi[[#]], gNeg[PiT[[#]]]]] &] && AllTrue[PiT, Length[#] > 0 &];
  noQdot = AllTrue[Range[0, 15], gZeroQ[gLeftD[Lp, gQ1[4, #]]] &];
  g44 = ginv0[[5, 5]];
  Kq = red[sq[[1]] $C.gam[[1, 5]]];
  Qq = red[I gam[[1, 5]].$C/(g44 sq[[1]])];
  gauss = If[gl === "G2",
    Bm = -I $C.$gam[[5]];
    zeroQ[g44 + 1] && zeroQ[gam[[1, 5]] - $gam[[5]]] && zeroQ[Qq - red[Bm/sq[[1]]]] && zeroQ[Bm - hermConj[Bm]] &&
      zeroQ[Bm.Bm - id16] && Tr[Bm] === 0 && zeroQ[comm[$C, Bm]] && zeroQ[Bm.$C + I $gam[[5]]],
    True];
  add["QNT_canonicalMomentum", piOK && noQdot && zeroQ[Kq.Qq - I id16] && zeroQ[Qq - hermConj[Qq]] && gauss];
  mm["canonicalMomentum", "Pi_a = dR L'/d(d_4 Psi_a) = sqrt|g| (Psi^dagger C gamma^4)_a (right derivative), L' = L + (1/2) d_4(sqrt|g| Psibar gamma^4 Psi); {Psi, Psi^dagger} = i (sqrt|g| C gamma^4)^(-1) = i gamma^4 C/(g^44 sqrt|g|)"];

  (* --- the notebook Lg[] for a real Grassmann Psi16 --- *)
  nbLg[omKey_] := Module[{psi = gGenVec[gP0], dpsi = Table[gGenVec[gP1[mu, #] &], {mu, 0, 7}], rowC, rows, inner, mass, Lg, E, MJ, A, X, N0, Ef, OmK = geo[omKey]},
    rowC = gRowMat[psi, jConst[$C]];
    rows = Table[gMatVec[jPart[gam, al], gVecAdd[dpsi[[al]], gMatVec[jPart[OmK, al], psi]]], {al, 8}];
    inner = Table[gSum[Table[rows[[al, a]], {al, 8}]], {a, 16}];
    mass = gDot[rowC, psi];
    Lg = gScaleJet[cjScalar[sq], gAdd[gDot[rowC, inner], gScaleNum[hm, mass]]];
    E = gEulerLagrange[Lg, gP0, gP1, "left"];
    MJ = Table[jMul[Times, sq, jLin[$C.# &, jPart[gam, al]]], {al, 8}];
    A = Table[red[MJ[[al, 1]] + Transpose[MJ[[al, 1]]]], {al, 8}];
    N0 = red[sq[[1]] ($C.Sum[gam[[1, al]].OmK[[1, al]], {al, 8}] + hm $C)];
    X = red[Sum[Transpose[MJ[[al, 2, al]]], {al, 8}] + N0 - Transpose[N0]];
    Ef = Table[gAdd[gSum[Table[gMatVec[jConst[A[[al]]], dpsi[[al]]][[a]], {al, 8}]], gMatVec[jConst[X], psi][[a]]], {a, 16}];
    <|"massZero" -> gZeroQ[mass], "E" -> (gVal /@ E), "A" -> A, "X" -> X, "Lterms" -> Length[Lg],
      "identityAgree" -> gSameVectorQ[E, gEulerLagrangeIdentity[Lg, gP0, gP1, "left"]],
      "agree" -> AllTrue[Range[16], gZeroQ[gAdd[gVal[E[[#]]], gNeg[gVal[Ef[[#]]]]]] &],
      "Ezero" -> AllTrue[E, gZeroQ[gVal[#]] &]|>];
  nbC = nbLg["Omega"]; nbN = nbLg["OmegaNotebook"];
  Xexp = red[sq[[1]] $C.Sum[comm[gam[[1, al]], OmNB[[1, al]] - Om[[1, al]]], {al, 8}]];
  add["LAG_notebookLgGrassmannTrivial", nbC["identityAgree"] && nbN["identityAgree"] && nbC["massZero"] && nbC["agree"] && nbC["Ezero"] && zeroQ[nbC["A"]] && zeroQ[nbC["X"]] &&
    nbN["massZero"] && nbN["agree"] && zeroQ[nbN["A"]] && ! zeroQ[nbN["X"]] && zeroQ[nbN["X"] - Xexp] &&
    gIsLinearIn[nbN["E"], Table[gP0[a], {a, 0, 15}]] && zeroQ[gLinearMatrix[nbN["E"], Table[gP0[a], {a, 0, 15}]] - nbN["X"]]];
  mm["notebookLgMonomials", nbC["Lterms"]];
  mm["notebookLgResidualXMaxAbs", exactString[maxAbsEntry[nbN["X"]]]];
  mm["notebookLgResidualXMaxAbsDecimal", decimalString[maxAbsEntry[nbN["X"]]]];
  mm["notebookLgResidualXRank", MatrixRank[exactValue[nbN["X"]]]];
  mm["notebookLgResidualX", "X = sqrt|g| C Sum_alpha [gamma^alpha, OmegaNotebook_alpha - Omega_alpha] (E = X Psi, no derivative terms)"];

  (* --- energy-momentum tensor --- *)
  {onData, okOS} = D16GeoSolveOnShell[geo, randomFieldData[seed + 10], m, lam];
  fldOn = D16GeoFieldJets @@ onData;
  lagOn = D16GeoLagrangianJets[geo, fldOn, m, lam];
  Ton = D16GeoEMTJets[geo, lagOn];
  divOn = D16GeoEMTDivergence[geo, Ton];
  lagOff = D16GeoLagrangianJets[geo, fldOff, m, lam];
  Toff = D16GeoEMTJets[geo, lagOff];
  divOff = D16GeoEMTDivergence[geo, Toff];
  add["EMT_conservation", okOS && zeroQ[divOn] && ! zeroQ[divOff]];
  mm["emtDivergenceOffShellMaxAbs", exactString[maxAbsEntry[divOff]]];
  mm["onShellJetsResidualZero", boolString[okOS]];
  S0 = lagOn["S"][[1]];
  tr = red[Sum[ginv0[[mu, nu]] Ton[[mu, nu, 1]], {mu, 8}, {nu, 8}]];
  expTr = red[-m S0 + 7 S0 (lam S0) - 8 (lam/2) S0^2];
  add["EMT_trace", zeroQ[tr - expTr] && ! zeroQ[S0]];
  mm["emtTraceOnShell", exactString[tr]];
  symOK = zeroQ[Table[Toff[[mu, nu]] - Toff[[nu, mu]], {mu, 8}, {nu, 8}]];
  Kt = emtValue[geo, lagValue[geo, id16, zm1, id16, zm1, m, 0]];
  Ktl = Table[emtValue[geo, lagValue[geo, zm16, unitSlot[l], id16, zm1, m, 0]], {l, 8}];
  Ltl = Table[emtValue[geo, lagValue[geo, id16, zm1, zm16, unitSlot[l], m, 0]], {l, 8}];
  herm = AllTrue[Flatten[Table[zeroQ[Kt[[mu, nu]] - hermConj[Kt[[mu, nu]]]], {mu, 8}, {nu, 8}]], TrueQ] &&
    AllTrue[Flatten[Table[zeroQ[Ltl[[l, mu, nu]] - hermConj[Ktl[[l, mu, nu]]]], {l, 8}, {mu, 8}, {nu, 8}]], TrueQ];
  add["EMT_symmetricHermitian", symOK && herm && matLevel];

  (* --- finite local Spin(4,4) invariance --- *)
  inv = spinInvariance[geo, fj, randomFieldData[seed + 20], m, lam, seed + 30];
  add["LAG_localSpinInvariance", inv["unitNorms"] && inv["infinitesimalUnitNorm"] &&
    And @@ Values[KeyDrop[inv["spinZero"], {"lagrangianRatio", "notebookLagrangianDifference", "notebookFirstOrderChange", "generatorFirstOrderPart"}]] &&
    And @@ Values[KeyDrop[inv["spinMixed"], {"lagrangianRatio", "notebookLagrangianDifference", "notebookFirstOrderChange", "generatorFirstOrderPart"}]] &&
    And @@ Values[KeyDrop[inv["infinitesimal"], {"lagrangianRatio", "notebookLagrangianDifference", "notebookFirstOrderChange", "generatorFirstOrderPart"}]] &&
    inv["infinitesimal"]["generatorFirstOrderPart"] =!= 0 && inv["infinitesimal"]["notebookFirstOrderChange"] =!= 0];
  mm["spinInvariance.identityComponent.LprimeOverL", exactString[inv["spinZero"]["lagrangianRatio"]]];
  mm["spinInvariance.spacelikeTimelikePair.LprimeOverL", exactString[inv["spinMixed"]["lagrangianRatio"]]];
  mm["spinInvariance.notebookContractionLagrangianChangeMaxAbs", exactString[inv["spinZero"]["notebookLagrangianDifference"]]];
  mm["spinInvariance.infinitesimal.notebookContractionFirstOrderChangeMaxAbs", exactString[inv["infinitesimal"]["notebookFirstOrderChange"]]];
  mm["spinInvariance.infinitesimal.generatorMaxAbs", exactString[inv["infinitesimal"]["generatorFirstOrderPart"]]];
  mm["spinInvariance.details", ToString[{inv["unitNorms"], inv["infinitesimalUnitNorm"],
    KeyDrop[inv["spinZero"], {"notebookLagrangianDifference", "notebookFirstOrderChange", "generatorFirstOrderPart"}], KeyDrop[inv["spinMixed"], {"notebookLagrangianDifference", "notebookFirstOrderChange", "generatorFirstOrderPart"}],
    KeyDrop[inv["infinitesimal"], {"notebookLagrangianDifference", "notebookFirstOrderChange", "generatorFirstOrderPart"}]}, InputForm]];

  (* --- primordial-field specific checks --- *)
  If[gl === "G2",
    Module[{H = pars["H"], A1 = pars["A1"], A2 = pars["A2"], h, dh, formula, slash, slashNB, symG, subst, agree, c0, c4, einsteinExp},
      h = Diagonal[e0]; dh = Table[Diagonal[fj[[2, b]]], {b, 8}];
      formula = red[(1/2) Sum[(1/h[[b]]) Sum[If[cc == b, 0, dh[[b, cc]]/h[[cc]]], {cc, 8}] $gam[[b]], {b, 8}]];
      slash = red[Sum[gam[[1, mu]].Om[[1, mu]], {mu, 8}]];
      add["GEO_diagonalSlashFormula", zeroQ[slash - formula] && zeroQ[slash - 3 H $gam[[1]]]];
      slashNB = red[Sum[gam[[1, mu]].OmNB[[1, mu]], {mu, 8}]];
      c0 = red[Tr[slashNB.$gam[[1]]]/16]; c4 = red[-Tr[slashNB.$gam[[5]]]/16];
      mm["notebookSlash", "gamma^mu OmegaNotebook_mu = (" <> exactString[c0] <> ") gamma^0 + (" <> exactString[c4] <> ") gamma^4, residual zero: " <>
        boolString[zeroQ[slashNB - c0 $gam[[1]] - c4 $gam[[5]]]]];
      mm["notebookSlashEqualsThreeHalfHTimesGamma0PlusA1Gamma4", boolString[zeroQ[slashNB - (3 H/2) ($gam[[1]] + A1 $gam[[5]])]]];
      einsteinExp = DiagonalMatrix[Join[{-3 H^2 (A1^2 - 5)}, ConstantArray[H^2 (15 - 3 A1^2 + A2), 3], {3 H^2 (7 + A1^2)}, ConstantArray[H^2 (15 - 3 A1^2 - A2), 3]]];
      add["GEO_primordialInvariants", zeroQ[sq[[1]] - cs] && zeroQ[sq[[2, 5]]] && zeroQ[rs - 6 H^2 (A1^2 - 7)] &&
        zeroQ[geo["einsteinMixed"] - einsteinExp] && Count[Flatten[omL[[1]]], x_ /; ! zeroQ[x]] === 24 && zeroQ[slash - 3 H $gam[[1]]]];
      symG = D16GeoSymbolicGeometry[g2FrameSymbolic[H], xs];
      subst[x_] := red[x /. g2Rules[pars]];
      agree = zeroQ[subst[symG["metric"]] - g0] && zeroQ[subst[symG["inverseMetric"]] - ginv0] &&
        zeroQ[subst[symG["christoffel"]] - Gv] && zeroQ[subst[symG["omegaMixed"]] - geo["omegaMixed"][[1]]] &&
        zeroQ[subst[symG["omegaLower"]] - omL[[1]]] && zeroQ[subst[symG["Omega"]] - Om[[1]]] &&
        zeroQ[subst[symG["OmegaNotebook"]] - OmNB[[1]]] && zeroQ[subst[symG["curvedGammas"]] - gam[[1]]] &&
        zeroQ[subst[symG["loweredGammas"]] - gamL[[1]]] && zeroQ[subst[symG["frameDeterminant"]] - geo["detFrame"]] &&
        FreeQ[subst[symG["Omega"]], xs[[1]] | xs[[5]] | a4 | Sin | Cos];
      add["GEO_symbolicJetAgreement", agree];
    ]];
  {c, ms}
];

(* ========================================================================= *)
(* 13. Minisuperspace (G3): EMT from the tetrad variation, homogeneous reduction *)
(* ========================================================================= *)

hS = Table[Symbol["Dirac16Complex`Geometry`Private`hS" <> ToString[i]], {i, 0, 7}];
hdS = Table[Symbol["Dirac16Complex`Geometry`Private`hdS" <> ToString[i]], {i, 0, 7}];
hddS = Table[Symbol["Dirac16Complex`Geometry`Private`hddS" <> ToString[i]], {i, 0, 7}];
(* hS[[5]] = N(t) (lapse), hdS[[5]] = N'(t) *)
minisuperspaceJet = {DiagonalMatrix[hS], Table[If[l == 5, DiagonalMatrix[hdS], ConstantArray[0, {8, 8}]], {l, 8}],
   Table[If[l == 5 && kk == 5, DiagonalMatrix[hddS], ConstantArray[0, {8, 8}]], {l, 8}, {kk, 8}]};

runMinisuperspace[k_Integer, geoS_] := Module[
  {c = <||>, ms = <||>, add, mm, pre = "G3.p" <> ToString[k] <> ".", t = g3Points[[k]], m = $mList[[k]], lam = $lamList[[k]],
   seed = 30000 + 100 k, fj3, geo3, hv, hdv, vals, base, p0, q0, offData, onData, okOS, homog, sqv, variation, results = {},
   ginv, gl, gam, Hh, trans},
  add[name_, v_] := (c[name] = TrueQ[Lookup[c, name, True]] && TrueQ[v]);
  mm[name_, v_] := (ms[pre <> name] = v);
  fj3 = D16GeoFrameJet[g3Frame[xs], xs, Thread[xs -> {0, 0, 0, 0, t, 0, 0, 0}]];
  geo3 = D16GeoJetGeometry[fj3];
  ginv = geo3["ginv"][[1]]; gl = geo3["gammaLower"][[1]]; gam = geo3["gamma"][[1]];
  hv = Diagonal[fj3[[1]]]; hdv = Diagonal[fj3[[2, 5]]];
  Hh = hdv/hv; trans = Delete[Range[8], 5];
  vals = Join[Thread[hS -> hv], Thread[hdS -> hdv]];
  sqv = geo3["sqrtg"][[1]];
  base = randomFieldData[seed];
  p0 = base[[1]]; q0 = base[[4]];
  offData = {p0, ReplacePart[zp1, 5 -> base[[2, 5]]], ReplacePart[zp2, {5, 5} -> base[[3, 5, 5]]],
    q0, ReplacePart[zp1, 5 -> base[[5, 5]]], ReplacePart[zp2, {5, 5} -> base[[6, 5, 5]]]};
  {onData, okOS} = D16GeoSolveOnShell[geo3, {p0, zp1, zp2, q0, zp1, zp2}, m, lam];
  homog = zeroQ[Delete[onData[[2]], 5]] && zeroQ[Delete[onData[[5]], 5]] &&
    zeroQ[ReplacePart[onData[[3]], {5, 5} -> ConstantArray[0, 16]]] && zeroQ[ReplacePart[onData[[6]], {5, 5} -> ConstantArray[0, 16]]];
  mm["frame", "h_i = 1 + x4^2/(i+2) (i != 4), h_4 = N = 1, x4 = " <> ToString[t, InputForm]];
  mm["onShellHomogeneous", boolString[okOS && homog]];
  (* reduced action L(N, h, h', N'; Psi(t), Psi^dagger(t)) and its variation *)
  variation[data_, label_] := Module[{L0, lag, T, S0, U, Up, rhoVar, tiiVar, rhoCov, tiiCov, indep, ok},
    L0 = D16GeoLagrangianJets[geoS, D16GeoFieldJets @@ data, m, lam]["L"][[1]];
    indep = Together[D[L0, hdS[[5]]]] === 0 && AllTrue[trans, Together[D[L0, hdS[[#]]]] === 0 &];
    rhoVar = Together[(-D[L0, hS[[5]]]/sqv) /. vals];
    tiiVar = Table[Together[(hv[[i]] D[L0, hS[[i]]]/sqv) /. vals], {i, trans}];
    lag = D16GeoLagrangianJets[geo3, D16GeoFieldJets @@ data, m, lam];
    T = D16GeoEMTJets[geo3, lag];
    rhoCov = red[-ginv[[5, 5]] T[[5, 5, 1]]];
    tiiCov = red[Table[ginv[[i, i]] T[[i, i, 1]], {i, trans}]];
    S0 = lag["S"][[1]]; U = (lam/2) S0^2; Up = lam S0;
    ok = indep && zeroQ[rhoVar - rhoCov] && zeroQ[tiiVar - tiiCov] && zeroQ[rhoVar - (m S0 + U)] &&
      If[label === "onShell", zeroQ[tiiVar - ConstantArray[S0 Up - U, 7]], zeroQ[tiiVar - ConstantArray[lag["Ls"][[1]], 7]]];
    mm["variation." <> label <> ".rho", exactString[rhoVar]];
    mm["variation." <> label <> ".p0", exactString[tiiVar[[1]]]];
    ok];
  add["EMT_variation_G3", okOS && homog && variation[offData, "offShell"] && variation[onData, "onShell"]];
  (* homogeneous reduction *)
  Module[{lag, T, S0, U, Up, rho, pis, KE, PE, Tij, T4i, lagOffH, Toff, drho, theta, bil, fldOn, fldOffH, ok1, ok2, ok3, ok4, ok5, ok6, ok7, ok8, ok9, ok10},
    fldOn = D16GeoFieldJets @@ onData; fldOffH = D16GeoFieldJets @@ offData;
    lag = D16GeoLagrangianJets[geo3, fldOn, m, lam]; T = D16GeoEMTJets[geo3, lag];
    lagOffH = D16GeoLagrangianJets[geo3, fldOffH, m, lam]; Toff = D16GeoEMTJets[geo3, lagOffH];
    S0 = lag["S"][[1]]; U = (lam/2) S0^2; Up = lam S0;
    rho = T[[5, 5, 1]];
    pis = Table[red[ginv[[i, i]] T[[i, i, 1]]], {i, trans}];
    KE = lag["KE"][[1]]; PE = red[rho - KE];
    ok1 = zeroQ[rho - (m S0 + U)] && zeroQ[Toff[[5, 5, 1]] - (m lagOffH["S"][[1]] + (lam/2) lagOffH["S"][[1]]^2)];
    ok2 = zeroQ[pis - ConstantArray[S0 Up - U, 7]] &&
      zeroQ[Table[ginv[[i, i]] Toff[[i, i, 1]], {i, trans}] - ConstantArray[lagOffH["Ls"][[1]], 7]];
    ok3 = zeroQ[KE - (1/2) S0 (m + Up)];
    ok4 = zeroQ[PE - (1/2) (m S0 + 2 U - S0 Up)];
    Tij[TT_, lg_] := Table[If[i == j, 0, red[TT[[i, j, 1]] - (1/4) (Hh[[i]] - Hh[[j]]) lg["bar"][[1]].gl[[i]].gl[[j]].gam[[5]].lg["psi"][[1]]]], {i, trans}, {j, trans}];
    ok5 = zeroQ[Tij[T, lag]] && zeroQ[Tij[Toff, lagOffH]] &&
      AnyTrue[Flatten[Table[If[i == j, 0, T[[i, j, 1]]], {i, trans}, {j, trans}]], ! zeroQ[#] &];
    T4i[TT_, dat_] := Table[red[TT[[5, i, 1]] + (1/4) (dat[[4]].$C.gl[[i]].dat[[2, 5]] - dat[[5, 5]].$C.gl[[i]].dat[[1]])], {i, trans}];
    ok6 = zeroQ[T4i[Toff, offData]] && zeroQ[Table[T[[5, i, 1]], {i, trans}]] && AnyTrue[Table[Toff[[5, i, 1]], {i, trans}], ! zeroQ[#] &];
    drho = T[[5, 5, 2, 5]];
    ok7 = zeroQ[drho + Sum[Hh[[i]] (rho + ginv[[i, i]] T[[i, i, 1]]), {i, trans}]];
    ok8 = zeroQ[D16GeoEMTDivergence[geo3, T]];
    theta = Total[Hh[[trans]]];
    ok9 = AllTrue[Flatten[Table[If[i < j,
        bil = jMul[Dot, lag["bar"], jLin[($gam[[i]].$gam[[j]].$gam[[5]]).# &, lag["psi"]]];
        zeroQ[bil[[2, 5]] + theta bil[[1]]], True], {i, trans}, {j, trans}]], TrueQ];
    ok10 = zeroQ[red[Sum[ginv[[mu, nu]] T[[mu, nu, 1]], {mu, 8}, {nu, 8}]] - (-m S0 + 7 S0 Up - 8 U)];
    add["EMT_homogeneousReduction_G3", okOS && homog && ok1 && ok2 && ok3 && ok4 && ok5 && ok6 && ok7 && ok8 && ok9 && ok10];
    mm["homogeneous.subchecks", ToString[{ok1, ok2, ok3, ok4, ok5, ok6, ok7, ok8, ok9, ok10}]];
    mm["homogeneous.rho", exactString[rho]]; mm["homogeneous.KE", exactString[KE]]; mm["homogeneous.PE", exactString[PE]];
    mm["homogeneous.p1", exactString[pis[[2]]]];
  ];
  {c, ms}
];

(* ========================================================================= *)
(* 14. Report                                                                 *)
(* ========================================================================= *)

D16GeoReport[] := Module[{checks = <||>, meas = <||>, merge, algebra, res, pt, fj, geo, geoS, grass, t0},
  merge[{cc_, mm_}] := (Scan[(checks[#] = TrueQ[Lookup[checks, #, True]] && TrueQ[cc[#]]) &, Keys[cc]]; meas = Join[meas, mm]);
  $alg = None;

  (* algebra sanity *)
  checks["ALG_cliffordRelations"] = And @@ Flatten[Table[$gam[[a]].$gam[[b]] + $gam[[b]].$gam[[a]] == 2 $eta[[a, b]] id16, {a, 8}, {b, 8}]] &&
    AllTrue[Range[8], If[# <= 4, $gam[[#]] == Transpose[$gam[[#]]], $gam[[#]] == -Transpose[$gam[[#]]]] &];
  checks["ALG_chargeMatrix"] = $C == $gam[[1]].$gam[[2]].$gam[[3]].$gam[[4]] && $C == Transpose[$C] && $C.$C == id16 &&
    AllTrue[Range[8], Transpose[$C.$gam[[#]]] == -$C.$gam[[#]] &] &&
    AllTrue[Flatten[Table[Transpose[$C.$S[[a, b]]] == -$C.$S[[a, b]], {a, 8}, {b, 8}]], TrueQ] &&
    $chi == DiagonalMatrix[Join[ConstantArray[-1, 8], ConstantArray[1, 8]]];
  (* Grassmann lemma: left/right derivatives of the quartic term, S even *)
  grass = Module[{psb = gGenVec[gQ0], psi = gGenVec[gP0], bar, S, S2, Cpsi},
    bar = gRowMat[psb, jConst[$C]]; S = gDot[bar, psi]; S2 = gScaleNum[1/2, gMul[S, S]];
    Cpsi = gMatVec[jConst[$C], psi];
    Length[S2] > 0 &&
      AllTrue[Range[0, 15], gZeroQ[gAdd[gLeftD[S2, gQ0[#]], gNeg[gMul[S, Cpsi[[# + 1]]]]]] &] &&
      AllTrue[Range[0, 15], gZeroQ[gAdd[gRightD[S2, gP0[#]], gNeg[gMul[S, bar[[# + 1]]]]]] &] &&
      AllTrue[Range[16], gZeroQ[gAdd[gMul[S, psi[[#]]], gNeg[gMul[psi[[#]], S]]]] &] &&
      gZeroQ[gDot[gRowMat[psi, jConst[$C]], psi]] && ! gZeroQ[gDot[gRowMat[psi, jConst[$C.$gam[[1]]]], psi]]];
  checks["ALG_grassmannLemmas"] = grass;
  meas["convention.grassmann"] = "Psi_a, Psi^dagger_a are independent odd generators (Psi_a Psi_b = -Psi_b Psi_a, Psi_a Psi^dagger_b = -Psi^dagger_b Psi_a), (theta1 theta2)^* = theta2^* theta1^*; Euler-Lagrange: left derivatives for Psi^dagger, right derivatives for Psi; checked: dL(lambda S^2/2)/dPsi^dagger_a = lambda S (C Psi)_a, dR(lambda S^2/2)/dPsi_a = lambda S Psibar_a, S even, Psi^T C Psi = 0 for real Grassmann Psi";
  meas["convention.eulerLagrangeJetIdentity"] = "EL_a = dL0/du_a - Sum_mu d_mu(dL/du_{mu a}) = 9 dL0/du_a - Sum_mu dL_mu/du_{mu a}, L_mu = total x^mu derivative of L at the point (exact Grassmann identity [dL/du_{mu a}, d_lam] = delta_{lam mu} dL/du_a)";
  meas["convention.fieldJets"] = "Psi, d_mu Psi, d_mu d_nu Psi and the same for Psi^dagger at the point: independent exact rationals from D16GeoRandomRationals (64-bit LCG, state' = (6364136223846793005 state + 1442695040888963407) mod 2^64, value = (floor(state/2^33) mod 19 - 9)/(floor(state/2^13) mod 9 + 1)); seeds 10000*geometry + 100*point (+10 on-shell free data, +20 spin-invariance fields, +30.. unit vector fields)";
  meas["convention.commutingEvaluation"] = "EMT, Lichnerowicz, on-shell and invariance checks evaluate bilinears with commuting exact numbers (Psi^dagger always leftmost, Psi rightmost: exact for bilinears); quartic terms enter only through the even scalar S = Psibar Psi, all manipulations keep each bilinear intact. The Euler-Lagrange, canonical-momentum and notebook-Lg checks use the genuine Grassmann algebra.";
  meas["convention.onShellJets"] = "at the point: free data Psi, d_mu Psi (mu != 4), d_mu d_nu Psi (mu,nu != 4) and the same for Psi^dagger; the field equations gamma^mu D_mu Psi = (m + lambda S) Psi, (D_mu Psibar) gamma^mu = -(m + lambda S) Psibar and their first derivatives are solved exactly (linear systems with matrix gamma^4) for d_4 Psi, d_4 d_nu Psi, d_4 Psi^dagger, d_4 d_nu Psi^dagger; residuals (value and all 8 first derivatives) verified exactly zero";
  meas["convention.parameters"] = "m = {3/7, -2/5, 5/9}, lambda = {5/11, 7/13, -3/8}, notebook H M = {2/3, -5/7, 4/9} at points p1, p2, p3 of each geometry; U(S) = (lambda/2) S^2";
  meas["convention.curvature"] = "F_{mu nu} = d_mu Omega_nu - d_nu Omega_mu + [Omega_mu, Omega_nu] = +(1/2) R_{mu nu a b} S^{ab} with R_{mu nu a b} := eta_{ac} e_rho^c R^rho_{sigma mu nu} e_b^sigma and R^rho_{sigma mu nu} = d_mu Gamma^rho_{nu sigma} - d_nu Gamma^rho_{mu sigma} + Gamma^rho_{mu lambda} Gamma^lambda_{nu sigma} - Gamma^rho_{nu lambda} Gamma^lambda_{mu sigma}";
  meas["convention.lichnerowicz"] = "(gamma^mu D_mu)^2 Psi = g^{mu nu}(D_mu D_nu Psi - Gamma^lambda_{mu nu} D_lambda Psi) + c R Psi with c = -1/4, R = g^{sigma nu} R^rho_{sigma rho nu} ({gamma^a, gamma^b} = +2 eta^{ab})";
  meas["convention.localSpinInvariance"] = "(i) finite local transformation: R(x) = nslash(x) mslash(x), n, m exact rational unit vector fields (reflections of e_0, e_1 in polynomial fields); frame e_a^mu -> Lambda_a^c e_c^mu with R gamma^a R^-1 = Lambda^c_a gamma^c, Psi -> R Psi, Psi^dagger -> Psi^dagger R^T; Omega recomputed from the rotated frame; checked Omega' = R Omega R^-1 - (d R) R^-1, gamma'^mu = R gamma^mu R^-1, g' = g and L' = L (value and first derivatives); (ii) for a spacelike/timelike pair (<n,n><m,m> = -1, spinor norm -1): Psibar -> -Psibar R^-1, S -> -S and L[m, lambda] -> -L[m, -lambda] (the naive L -> -L fails for lambda != 0: kinetic and mass terms flip, U(S) = lambda S^2/2 does not); (iii) first-order infinitesimal: R_kappa = n_kappa mslash = -1 + kappa epsilon(x) + O(kappa^2), epsilon = [mslash, wslash] in spin(4,4), exact dual-number arithmetic kappa^2 = 0: the kappa^1 part of L' - L (value and first derivatives) vanishes; the notebook contraction gives a nonzero first-order change";
  meas["G1.definition"] = "e_mu^a = delta_mu^a + P_mu^a(x), P_mu^a = (1/10)((mu+1) x_a - (a+1) x_mu) + (1/20) x_mu x_a + (1/30) x_((mu+a) mod 8)^2 (mu != a), P_mu^mu = (1/10) x_mu^2 + (1/40) x_((mu+1) mod 8)";
  meas["G2.definition"] = "primordial vielbein diag(cot z, s^(1/6) e^a4 (x3), 1, s^(1/6) e^-a4 (x3)), z = 6 H x0, t = H x4, s = sin z; exact point data w = s^(1/6) rational, sin z = w^6, cos z = cs with cs^2 = 1 - w^12 (arithmetic in Q(cs), basis {1, cs}), exp(a4(t)) = ea rational (a4(t) = Log[ea]), a4', a4'', a4''' rational (a4''' never enters: second-order vielbein jets suffice)";
  meas["G3.definition"] = "minisuperspace/Bianchi-I: ds^2 = -N(t)^2 dt^2 + Sum_{i != 4} eps_i h_i(t)^2 dx_i^2, t = x4, eps = eta; covariant side at N = 1 with h_i = 1 + x4^2/(i+2); variation side: symbolic N, h_i, N', h_i' in the reduced Lagrangian sqrt|g| Ls with homogeneous Psi(t), Psi^dagger(t) held fixed";

  (* G1 *)
  Do[
    $alg = None;
    fj = D16GeoFrameJet[D16GeoG1Frame[xs], xs, Thread[xs -> g1Points[[k]]]];
    geo = D16GeoJetGeometry[fj];
    meas["G1.p" <> ToString[k] <> ".coordinates"] = ToString[g1Points[[k]], InputForm];
    merge[runGeometry["G1", k, geo, fj, <|"seed" -> 10000 + 100 k|>]],
    {k, 3}];
  (* G2 *)
  Do[
    pt = g2Points[[k]];
    $alg = g2Alg[pt];
    fj = D16GeoFrameJet[g2FrameSymbolic[pt["H"]], xs, g2Rules[pt]];
    geo = D16GeoJetGeometry[fj];
    meas["G2.p" <> ToString[k] <> ".point"] = "w = " <> ToString[pt["w"], InputForm] <> ", sin z = " <> ToString[pt["w"]^6, InputForm] <>
      ", cos z = " <> ToString[Sqrt[1 - pt["w"]^12], InputForm] <> ", H = " <> ToString[pt["H"], InputForm] <>
      ", a4(t) = Log[" <> ToString[pt["ea"], InputForm] <> "], a4'(t) = " <> ToString[pt["A1"], InputForm] <>
      ", a4''(t) = " <> ToString[pt["A2"], InputForm] <> ", a4'''(t) = " <> ToString[pt["A3"], InputForm];
    merge[runGeometry["G2", k, geo, fj, Join[pt, <|"seed" -> 20000 + 100 k|>]]];
    (* negative control at G2 p1: the same checks with Omega replaced by the notebook contraction *)
    If[k == 1, Module[{geoBad = geo, bad, sensitive},
      geoBad["Omega"] = geo["OmegaNotebook"];
      bad = First[runGeometry["G2", k, geoBad, fj, Join[pt, <|"seed" -> 20000 + 100 k|>]]];
      sensitive = {"GEO_gammaCovariantConstancy_G2", "GEO_divergenceIdentity_G2", "GEO_curvature_G2", "GEO_lichnerowicz_G2",
        "LAG_eulerLagrangePsibar_G2", "LAG_eulerLagrangePsi_G2", "LAG_notebookLgGrassmannTrivial_G2", "EMT_conservation_G2",
        "LAG_localSpinInvariance_G2", "GEO_diagonalSlashFormula_G2", "GEO_primordialInvariants_G2"};
      checks["NEG_notebookConnectionDetected_G2"] = AllTrue[sensitive, bad[#] === False &];
      meas["G2.p1.negativeControl"] = "Omega := OmegaNotebook, every check recomputed; results: " <>
        ToString[Normal[bad /. {True -> "true", False -> "false"}], InputForm];
    ]],
    {k, 3}];
  $alg = None;
  (* G3 minisuperspace *)
  geoS = D16GeoJetGeometry[minisuperspaceJet, "SqrtSign" -> 1];
  Do[merge[runMinisuperspace[k, geoS]], {k, 3}];
  meas["emt.signConvention"] = If[TrueQ[checks["EMT_variation_G3"]],
    "CONTRACT section 7 sign confirmed: T_{mu nu} = -(2/sqrt|g|) dS/dg^{mu nu} (rho = -(1/sqrt|g|) dS/dN at N = 1, T^i_i = (h_i/sqrt|g|) dS/dh_i) equals the covariant formula, T_44 = rho = m S + U",
    "CONTRACT section 7 formula does NOT agree with the tetrad variation (see G3 measurements)"];
  meas["emt.offDiagonalHomogeneous"] = "Bianchi-I, homogeneous Psi(t): T_ij = (1/4)(H_i - H_j) Psibar gamma_i gamma_j gamma^4 Psi (curved gammas, gamma_i = g_ii gamma^i; equivalently c_ij = g_ii g_jj/4 with upper curved gammas), off- and on-shell; T_4i = -(1/4)(Psibar gamma_i d_4 Psi - d_4 Psibar gamma_i Psi) off-shell and T_4i = 0 identically on-shell; d/dt(Psibar gamma^i gamma^j gamma^4 Psi) = -(Sum_k H_k) Psibar gamma^i gamma^j gamma^4 Psi (flat gammas, on-shell), so zero initial data stay zero";
  meas["emt.trace"] = "on-shell T^mu_mu = -m S + 7 S U'(S) - 8 U(S) = -m S + 3 lambda S^2";
  $alg = None;
  <|"checks" -> KeySort[checks] // Association, "measurements" -> meas|>
];

End[];
EndPackage[];
