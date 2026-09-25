(* ::Package:: *)

(* ::Title:: *)
(* Dirac16ComplexKohnSham.wl *)

(* ::Text:: *)
(* Stage 4 of dirac16complex: the exact theory behind the Kohn-Sham (Mermin
   finite-temperature) treatment of the interacting dirac16complex field in the
   STATIC primordial gravitational field (a4 constant), written in the proper
   hidden-space coordinate y = ln(sin z)/(6H) in (-infinity, 0].

   Conventions: CONTRACT.md (zero-based indices, eta = diag(+,+,+,+,-,-,-,-),
   gamma^a = [[0, taubar_a],[tau_a, 0]], C = sigma16, B = -i C gamma^4) and
   NUMERICS_CONTRACT.md (expectation-value rule <Psi^dagger M Psi> = u^dagger B M u
   for a Hilbert-normalised mode u; number density u^dagger u, scalar density
   u^dagger B C u).

   Sections (check-name prefixes):
     KS_fixture    gamma matrices rebuilt from the split-octonion recipe and
                   compared with the committed exact fixture.
     KS_geometry   warped form ds^2 = dy^2 - dx4^2 + e^{2Hy}[e^{2a}dx_{123}^2
                   - e^{-2a}dx_{567}^2]; W^6; R = -42H^2; G^mu_nu; required
                   Einstein source; extrinsic curvature K^i_j = H; the Z2 brane
                   (Israel junction, sign convention stated); the smooth
                   extension E1 (constant curvature invariants for all y).
     KS_reduction  the ansatz Psi = e^{-i eps x4} e^{i k x1} e^{-3Hy} chi(y)
                   removes gamma^mu Omega_mu = 3H gamma^0 exactly; the reduced
                   y-equation; exact simultaneous block diagonalisation of
                   gamma^0, gamma^0 gamma^1, gamma^0 gamma^4, B, C into eight
                   2x2 blocks in the common eigenbasis of J = gamma^0 gamma^1
                   gamma^4, K1 = gamma^2 gamma^3, K2 = gamma^5 gamma^6; the
                   explicit exact basis; the 2x2 matrices; block types; the
                   per-block density matrices; degeneracies; the k = 0 exact
                   box spectrum; rotational symmetry.
     KS_boundary   the y-current matrix; the Z2 parity conditions and the bag
                   condition in 2x2 form; proof that each kills the current;
                   the reflection symmetries of the reduced equation.
     KS_exchange   Hartree-Fock energy of U = (lambda/2) S^2 for a one-body
                   density matrix (fermionic Wick theorem verified on an exact
                   Fock-space model); filled-shell E_x = -E_H/8; the exact
                   spin-summed kernel; the uniform-gas exchange energy density
                   e_x = -(lambda/32)(n^2 + S^2); LDA potentials; T = 0
                   closed forms; the form of the KS equation.
     KS_functional the Mermin-Kohn-Sham free-energy functional, its
                   stationarity conditions (KS equation, Fermi-Dirac
                   occupations), the total-energy and Hellmann-Feynman
                   identities (verified on a discretised model).
     KS_emt        the Stage-2 energy-momentum tensor reduced to a KS orbital:
                   rho, p_y, p_(1,2,3), p_(5,6,7) and the off-diagonal
                   components in terms of the 2x2 block densities; the
                   proper-volume average; the Z2 parity of every density.

   Exactness: every scalar is a rational function of the symbols
   (H, m, k, eps, lambda, ...) and of wv = e^{Hy}, ea = e^{a4}; zero tests are
   exact (Together, numerator identically zero).  No floating point is used.

   Public entry point: D16KSRun[repoRoot].  It returns an Association with
   keys "checks", "measurements" and "theory" (the exact data exported to
   artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json). *)

BeginPackage["Dirac16ComplexKohnSham`"];

D16KSRun::usage = "D16KSRun[repoRoot] runs every Stage-4 exact Kohn-Sham theory check. It returns an Association with keys \"checks\" (name -> True|False), \"measurements\" (name -> value) and \"theory\" (exact data for kohn-sham-theory.json).";
D16KSGammas::usage = "D16KSGammas[] returns the list of the eight 16x16 gamma matrices gamma^0..gamma^7 (notebook split-octonion basis).";
D16KSBlockBasis::usage = "D16KSBlockBasis[] returns the unitary 16x16 matrix V (columns = the exact block basis, entries in {0, +-1, +-i}/(2 Sqrt[2])).";

Begin["`Private`"];

(* ================================================================== *)
(* 0. bookkeeping                                                      *)
(* ================================================================== *)

$checks = <||>; $meas = <||>; $theory = <||>;
addCheck[name_String, val_] := Module[{v = TrueQ[val]},
  $checks[name] = v;
  If[! v, Print["  CHECK FAILED: ", name]];
  v];
addMeas[name_String, val_] := ($meas[name] = val);
logT[msg__] := Print["[", DateString[{"Hour", ":", "Minute", ":", "Second"}], "] ", msg];
toStr[e_] := Block[{$Context = "Dirac16ComplexKohnSham`Private`",
    $ContextPath = {"System`", "Dirac16ComplexKohnSham`Private`"}},
  ToString[e, InputForm, PageWidth -> Infinity]];

(* exact JSON value printers: every number becomes a rational string, every
   complex number a pair [re, im] of rational strings *)
ratStr[x_Integer] := ToString[x];
ratStr[x_Rational] := ToString[Numerator[x]] <> "/" <> ToString[Denominator[x]];
ratStr[x_] := Throw[{"ratStr", x}, d16ksErr];
gq[x_] := Module[{r = Re[x], i = Im[x]}, {ratStr[r], ratStr[i]}];
gqMat[m_List] := Map[gq, m, {2}];
gqVec[v_List] := gq /@ v;
ratMat[m_List] := Map[ratStr, m, {2}];

(* ================================================================== *)
(* 1. gamma matrices (CONTRACT section 1)                              *)
(* ================================================================== *)

id2 = IdentityMatrix[2]; id4 = IdentityMatrix[4]; id8 = IdentityMatrix[8]; id16 = IdentityMatrix[16];
zero16 = ConstantArray[0, {16, 16}];
etaM = DiagonalMatrix[{1, 1, 1, 1, -1, -1, -1, -1}];
qa[h_, p_, q_] := Signature[{h, p, q, 4}];
qb[h_, p_, q_] := id4[[p, 4]] id4[[q, h]] - id4[[p, h]] id4[[q, 4]];
s4m[h_] := Table[qa[h, p, q] - qb[h, p, q], {p, 4}, {q, 4}];
t4m[h_] := Table[qa[h, p, q] + qb[h, p, q], {p, 4}, {q, 4}];
sig8 = ArrayFlatten[{{0, id4}, {id4, 0}}];
tauL = Module[{tt = ConstantArray[0, 8]},
   tt[[1]] = id8;
   Do[tt[[h + 1]] = ArrayFlatten[{{0, s4m[h]}, {s4m[h], 0}}], {h, 1, 3}];
   Do[tt[[7 - h + 1]] = ArrayFlatten[{{0, t4m[h]}, {-t4m[h], 0}}], {h, 1, 3}];
   tt[[8]] = tt[[2]].tt[[3]].tt[[4]].tt[[5]].tt[[6]].tt[[7]];
   tt];
taubL = Join[{id8}, Table[sig8.Transpose[tauL[[A + 1]]].sig8, {A, 1, 7}]];
gamL = Table[ArrayFlatten[{{0, taubL[[A + 1]]}, {tauL[[A + 1]], 0}}], {A, 0, 7}];
G[a_Integer] := gamL[[a + 1]];
C16 = ArrayFlatten[{{-sig8, 0}, {0, sig8}}];
Sab[a_Integer, b_Integer] := Sab[a, b] = (G[a].G[b] - G[b].G[a])/4;
g8 = Fold[Dot, id16, gamL];
Bm = -I C16.G[4];
BC = Bm.C16;
A0 = G[0]; A1 = G[0].G[1]; A4 = G[0].G[4];
Jop = G[0].G[1].G[4]; K1op = G[2].G[3]; K2op = G[5].G[6];
sig1 = {{0, 1}, {1, 0}}; sig2 = {{0, -I}, {I, 0}}; sig3 = {{1, 0}, {0, -1}};
herm[m_] := ConjugateTranspose[m];
D16KSGammas[] := gamL;

(* ================================================================== *)
(* 2. exact ring and zero tests                                        *)
(* ================================================================== *)

(* wv = e^{H y}, ea = e^{a4}; exponents must be integer combinations *)
ringExp[ex_] := Module[{e = Expand[ex], cy, ca, rest},
  cy = Coefficient[e, y]; ca = Coefficient[e, a4c];
  rest = Together[e - cy y - ca a4c];
  If[rest =!= 0, Throw[{"ringExp", ex}, d16ksErr]];
  cy = Together[cy/H];
  If[! IntegerQ[cy] || ! IntegerQ[ca], Throw[{"ringExpNonInteger", ex}, d16ksErr]];
  wv^cy ea^ca];
ringRules = {Power[E, ex_] :> ringExp[ex]};
fieldHeads = {ch, cb, uu, ub, Ps, Pb};
fpat = (hd_Symbol[_Integer])[___] /; MemberQ[fieldHeads, hd];
dpat = (Derivative[__][hd_Symbol[_Integer]])[___] /; MemberQ[fieldHeads, hd];
gpat = (hd_Symbol)[___] /; MemberQ[{Meff, vv, vs, Sp, np}, hd];
dgpat = (Derivative[__][hd_Symbol])[___] /; MemberQ[{Meff, vv, vs, Sp, np}, hd];
toRing[e_] := Module[{r = Expand[e] /. ringRules},
  If[! FreeQ[r /. {fpat :> 1, dpat :> 1, gpat :> 1, dgpat :> 1}, y | E | Exp | Log | Sin | Cos],
   Throw[{"ringIncomplete", Short[r, 5]}, d16ksErr]];
  r];
atomize[e_] := Module[{atoms = Union[Cases[{e}, fpat | dpat | gpat | dgpat, Infinity]]},
  If[atoms === {}, e, e /. Dispatch[Thread[atoms -> Array[vA, Length[atoms]]]]]];
ringZeroQ[r_] := Together[atomize[r]] === 0;
zeroQ[e_] := If[e === 0, True, ringZeroQ[toRing[e]]];
zeroMatQ[m_] := AllTrue[Flatten[{m}], zeroQ];
(* zero test for expressions without y-dependence (plain rational functions) *)
zeroR[e_] := Together[e] === 0;
zeroRMat[m_] := AllTrue[Flatten[{m}], zeroR];

(* ================================================================== *)
(* 3. the static primordial field in the y chart                       *)
(* ================================================================== *)

Yv = {y, x1, x2, x3, x4, x5, x6, x7};
d1[k_Integer, f_] := D[f, Yv[[k]]]; (* partial w.r.t. coordinate k-1 (1-based k) *)
Wf = E^(H y);
hhF = {1, Wf E^a4c, Wf E^a4c, Wf E^a4c, 1, Wf E^(-a4c), Wf E^(-a4c), Wf E^(-a4c)};
epsL = {1, 1, 1, 1, -1, -1, -1, -1};
gdF = hhF^2 epsL;
gF = DiagonalMatrix[gdF]; giF = DiagonalMatrix[1/gdF];
evF = DiagonalMatrix[hhF]; eiF = DiagonalMatrix[1/hhF];
sqrtgF = Wf^6;

buildGeometry[] := Module[{},
  GamF = Table[Together[(1/2) Sum[giF[[r, s]] (d1[m, gF[[s, n]]] + d1[n, gF[[s, m]]] - d1[s, gF[[m, n]]]), {s, 8}]], {r, 8}, {m, 8}, {n, 8}];
  RicF = Table[Together[Sum[d1[r, GamF[[r, m, n]]] - d1[n, GamF[[r, m, r]]] + Sum[GamF[[r, r, l]] GamF[[l, m, n]] - GamF[[r, n, l]] GamF[[l, m, r]], {l, 8}], {r, 8}]], {m, 8}, {n, 8}];
  RsF = Together[Sum[giF[[m, m]] RicF[[m, m]], {m, 8}]];
  GmixF = Together[giF.RicF - (RsF/2) id8];
  (* Riemann R^r_{s m n} *)
  RiemF = Table[Together[d1[m, GamF[[r, n, s]]] - d1[n, GamF[[r, m, s]]] + Sum[GamF[[r, m, l]] GamF[[l, n, s]] - GamF[[r, n, l]] GamF[[l, m, s]], {l, 8}]], {r, 8}, {s, 8}, {m, 8}, {n, 8}];
  omMixF = Table[Together[Sum[eiF[[b, n]] (Sum[GamF[[r, m, n]] evF[[r, a]], {r, 8}] - d1[m, evF[[n, a]]]), {n, 8}]], {m, 8}, {a, 8}, {b, 8}];
  omLF = Table[Sum[etaM[[a, c]] omMixF[[m, c, b]], {c, 8}], {m, 8}, {a, 8}, {b, 8}];
  OmF = Table[(1/2) Sum[omLF[[m, a, b]] Sab[a - 1, b - 1], {a, 8}, {b, 8}], {m, 8}];
  gUF = Table[Sum[eiF[[a, m]] G[a - 1], {a, 8}], {m, 8}];
  gDF = Table[Sum[gF[[m, n]] gUF[[n]], {n, 8}], {m, 8}];];

(* ---------------- KS_fixture ---------------- *)
checkFixture[fixFile_] := Module[{fx},
  fx = Import[fixFile, "RawJSON"];
  addCheck["KS_fixture_gammasMatchCommittedFixture", fx["gamma"] === gamL];
  addCheck["KS_fixture_CAndChiralityMatch", fx["C"] === C16 && fx["chirality"] === g8];
  addCheck["KS_fixture_cliffordAndC", AllTrue[Flatten[Table[G[a].G[b] + G[b].G[a] == 2 etaM[[a + 1, b + 1]] id16, {a, 0, 7}, {b, 0, 7}]], TrueQ] &&
    C16 === G[0].G[1].G[2].G[3] && g8 === DiagonalMatrix[Join[ConstantArray[-1, 8], ConstantArray[1, 8]]]];
  addCheck["KS_fixture_Bproperties", herm[Bm] === Bm && Bm.Bm === id16 && Sort[Eigenvalues[Bm]] === Join[ConstantArray[-1, 8], ConstantArray[1, 8]] &&
    C16.Bm === Bm.C16 && BC === -I G[4]];
  addCheck["KS_internal_zeroTestSanity", zeroQ[E^(2 H y) E^(-2 H y) - 1] && zeroQ[E^(H y + a4c) - E^(H y) E^(a4c)] && ! zeroQ[E^(H y) - 1] &&
    ! zeroQ[E^a4c - 1] && zeroQ[D[E^(-3 H y), y] + 3 H E^(-3 H y)] && ! zeroQ[ch[0][y] - cb[0][y]] && zeroQ[ch[0][y] - ch[0][y]]];];

(* ---------------- KS_geometry ---------------- *)
checkGeometry[] := Module[{nzGam, exG, Kmix, Kplus, jump, trJump, Smix, rhoReq, pReq, kre, riemLow, riemUp, zz, gz, sz, brane, pt, wsub},
  addCheck["KS_geometry_sqrtDetG_W6", zeroQ[Det[gF] - Wf^12] && zeroQ[sqrtgF - E^(6 H y)]];
  addCheck["KS_geometry_signature44", (Sign /@ epsL) === {1, 1, 1, 1, -1, -1, -1, -1} && AllTrue[gdF, zeroQ[# - epsL[[Position[gdF, #][[1, 1]]]] hhF[[Position[gdF, #][[1, 1]]]]^2] &]];
  (* the y chart is the notebook chart with sin z = e^{6 H y}, dy = cot z dx0 *)
  (* g_yy = cot^2 z (dx0/dy)^2 = 1 with dy/dx0 = d[ln sin(6 H x0)/(6H)]/dx0 = cot z; s^{1/3} = (e^{6Hy})^{1/3} = e^{2Hy} (real exponents: PowerExpand) *)
  gz = Simplify[Cot[6 H x0]^2/D[Log[Sin[6 H x0]]/(6 H), x0]^2];
  sz = PowerExpand[(E^(6 H y))^(1/3)] - E^(2 H y);
  addCheck["KS_geometry_notebookChart", gz === 1 && sz === 0 && PowerExpand[(E^(6 H y))^(1/6)] === E^(H y)];
  nzGam = Count[Flatten[GamF], x_ /; ! zeroQ[x]];
  addMeas["geometry_christoffelNonzeroCount", nzGam];
  addCheck["KS_geometry_christoffelCount18", nzGam === 18];
  addCheck["KS_geometry_christoffelClosedForms", AllTrue[Range[2, 8], zeroQ[GamF[[1, #, #]] + If[# == 5, 0, H gdF[[#]]]] && zeroQ[GamF[[#, 1, #]] - If[# == 5, 0, H]] && zeroQ[GamF[[#, #, 1]] - If[# == 5, 0, H]] &] &&
    zeroQ[GamF[[1, 5, 5]]] && zeroQ[GamF[[1, 1, 1]]]];
  addCheck["KS_geometry_ricciScalarMinus42H2", zeroQ[RsF + 42 H^2]];
  exG = DiagonalMatrix[H^2 {15, 15, 15, 15, 21, 15, 15, 15}];
  addCheck["KS_geometry_einsteinMixedDiag", zeroMatQ[GmixF - exG]];
  addCheck["KS_geometry_ricciMixed", zeroMatQ[giF.RicF - DiagonalMatrix[H^2 {-6, -6, -6, -6, 0, -6, -6, -6}]]];
  (* Kretschmann and Ricci-square invariants: constants for every y (smooth extension E1 is regular) *)
  riemLow = Table[Sum[gF[[r, rr]] RiemF[[rr, s, m, n]], {rr, 8}], {r, 8}, {s, 8}, {m, 8}, {n, 8}];
  riemUp = Table[Sum[giF[[s, ss]] giF[[m, mm]] giF[[n, nn]] RiemF[[r, ss, mm, nn]], {ss, 8}, {mm, 8}, {nn, 8}], {r, 8}, {s, 8}, {m, 8}, {n, 8}];
  kre = Together[Sum[riemLow[[r, s, m, n]] riemUp[[r, s, m, n]], {r, 8}, {s, 8}, {m, 8}, {n, 8}]];
  addMeas["geometry_kretschmann", toStr[kre]];
  addCheck["KS_geometry_kretschmannConstant", zeroQ[kre - 84 H^4] && FreeQ[toRing[kre], wv | ea]];
  (* the seven directions (y, x1, x2, x3, x5, x6, x7) form a space of constant sectional curvature -H^2: R_{rsmn} = -H^2 (g_rm g_sn - g_rn g_sm); every component with an x4 index vanishes *)
  addCheck["KS_geometry_constantCurvatureSevenSpace", AllTrue[Flatten[Table[If[MemberQ[{r, s, m, n}, 5], zeroQ[riemLow[[r, s, m, n]]],
       zeroQ[riemLow[[r, s, m, n]] + H^2 (gF[[r, m]] gF[[s, n]] - gF[[r, n]] gF[[s, m]])]], {r, 8}, {s, 8}, {m, 8}, {n, 8}]], TrueQ]];
  addCheck["KS_geometry_ricciSquareConstant", zeroQ[Together[Sum[RicF[[m, n]] giF[[m, m]] giF[[n, n]] RicF[[m, n]], {m, 8}, {n, 8}]] - 252 H^4]];
  (* required 8D Einstein source: G^mu_nu = kappa T^mu_nu, rho = -T^4_4, p_i = T^i_i *)
  rhoReq = -GmixF[[5, 5]]/kap; pReq = Table[GmixF[[i, i]]/kap, {i, {1, 2, 3, 4, 6, 7, 8}}];
  addCheck["KS_geometry_requiredSource", zeroQ[rhoReq + 21 H^2/kap] && AllTrue[pReq, zeroQ[# - 15 H^2/kap] &]];
  addCheck["KS_geometry_rhoRequiredNegative", Simplify[rhoReq < 0, kap > 0 && H > 0] === True];
  addMeas["specDiscrepancy_pReqSign", "STAGE4_SPEC section 1 writes p_req = -15H^2/kappa; the exact mixed components give T^i_i = G^i_i/kappa = +15H^2/kappa for all seven transverse directions (y, x1, x2, x3, x5, x6, x7) and rho_req = -T^4_4 = -21H^2/kappa < 0."];
  (* extrinsic curvature of y = const, unit normal n = +partial_y: K_ij = (1/2) partial_y g_ij, K^i_j = (1/2) g^{ik} partial_y g_kj *)
  Kmix = Table[Together[giF[[i, i]] d1[1, gF[[i, i]]]/2], {i, 2, 8}];
  addCheck["KS_geometry_extrinsicCurvature", AllTrue[Range[7], zeroQ[Kmix[[#]] - If[# == 4, 0, H]] &]];
  (* Z2 mirror: y > 0 side has W = e^{-H y}: same formulas with H -> -H; jump [X] = X(0+) - X(0-) *)
  Kplus = Kmix /. H -> -H; jump = Together[Kplus - Kmix]; trJump = Together[Total[jump]];
  Smix = Together[-(jump - trJump)/kap];
  addCheck["KS_geometry_israelJump", AllTrue[Range[7], zeroQ[jump[[#]] + If[# == 4, 0, 2 H]] &] && zeroQ[trJump + 12 H]];
  addCheck["KS_geometry_israelStress", AllTrue[Range[7], zeroQ[Smix[[#]] + If[# == 4, 12, 10] H/kap] &]];
  addCheck["KS_geometry_braneEnergyPositive", zeroQ[-Smix[[4]] - 12 H/kap] && Simplify[-Smix[[4]] > 0, H > 0 && kap > 0] === True];
  (* the induced 7-metric at y = 0 is flat: its Christoffels vanish *)
  addCheck["KS_geometry_inducedMetricFlat", AllTrue[Flatten[Table[GamF[[r, m, n]] /. y -> 0, {r, 2, 8}, {m, 2, 8}, {n, 2, 8}]], zeroR]];
  addMeas["geometry_israelSignConvention", "[K_ij] - h_ij [K] = -kappa S_ij with [X] = X(0+) - X(0-), n = +partial_y pointing from y<0 to y>0, K_ij = h_i^mu h_j^nu nabla_mu n_nu = (1/2) partial_y g_ij; with W = e^{-H|y|} on both sides: K^i_j(0-) = +H, K^i_j(0+) = -H on the six warped directions, 0 on x4; [K] = -12H; S^i_j = -(10,10,10,12,10,10,10) H/kappa on (x1,x2,x3,x4,x5,x6,x7); rho_brane = -S^4_4 = +12H/kappa, p_brane = -10H/kappa (the same convention gives the Randall-Sundrum brane a positive tension 6k/kappa)."];
  $theory["geometry"] = <|
    "chart" -> <|"definition" -> "y = ln(sin z)/(6H), z = 6 H x0 in (0, pi/2), y in (-infinity, 0]; sin z = e^{6Hy}; dy = cot z dx0",
      "tex" -> "y=\\frac{\\ln\\sin z}{6H}\\in(-\\infty,0],\\quad e^{6Hy}=\\sin z"|>,
    "metric" -> <|"tex" -> "ds^2=dy^2-dx_4^2+e^{2Hy}\\bigl[e^{2a_4}(dx_1^2+dx_2^2+dx_3^2)-e^{-2a_4}(dx_5^2+dx_6^2+dx_7^2)\\bigr]",
      "diagonal" -> {"1", "e^{2Hy+2a_4}", "e^{2Hy+2a_4}", "e^{2Hy+2a_4}", "-1", "-e^{2Hy-2a_4}", "-e^{2Hy-2a_4}", "-e^{2Hy-2a_4}"},
      "vielbein" -> "h = (1, e^{Hy+a_4} (x3), 1, e^{Hy-a_4} (x3))", "a4" -> "constant (a4' = 0): the static member of the primordial family",
      "warp" -> "W(y) = e^{Hy}", "properVolumeElement" -> "sqrt|g| = W^6 = e^{6Hy} (per coordinate 7-volume; the transverse space pinches off at the tip y -> -infinity)",
      "coordinateOrder" -> "(y, x1, x2, x3, x4, x5, x6, x7)"|>,
    "christoffel" -> <|"nonzeroCount" -> nzGam,
      "closedForms" -> "Gamma^y_{ii} = -H g_ii (i != y, x4), Gamma^i_{yi} = Gamma^i_{iy} = H (i = 1,2,3,5,6,7); all others vanish"|>,
    "curvature" -> <|"ricciScalar" -> "R = -42 H^2", "ricciMixed" -> "R^mu_nu = diag(-6,-6,-6,-6,0,-6,-6,-6) H^2",
      "einsteinMixed" -> "G^mu_nu = diag(15,15,15,15,21,15,15,15) H^2", "einsteinMixedValues" -> ratMat[{{15, 15, 15, 15, 21, 15, 15, 15}}][[1]],
      "kretschmann" -> "R_{mu nu rho sigma} R^{mu nu rho sigma} = 84 H^4 = 2 n(n-1) H^4 with n = 7", "ricciSquare" -> "R_{mu nu} R^{mu nu} = 252 H^4 = n (n-1)^2 H^4",
      "structure" -> "the seven directions (y, x1, x2, x3, x5, x6, x7) form a space of constant sectional curvature -H^2 (R_{rsmn} = -H^2 (g_rm g_sn - g_rn g_sm), signature (4,3)), times the flat time line x4: R = -n(n-1) H^2 = -42 H^2, R_mu nu = -(n-1) H^2 g_mu nu on the seven directions and R_44 = 0",
      "note" -> "all invariants are y-independent: the smooth extension E1 (W = e^{Hy} for all real y) is a regular homogeneous space; the notebook patch y <= 0 ends at y = 0 only because the notebook chart does (cot z = 0), not because of a curvature singularity; the tip y -> -infinity is at infinite proper distance with W^6 -> 0"|>,
    "requiredSource" -> <|"convention" -> "G^mu_nu = kappa T^mu_nu, rho = -T^4_4, p_(i) = T^i_i",
      "rho" -> "rho_req = -21 H^2/kappa (negative)", "rhoValue" -> "-21", "p" -> "p_req = +15 H^2/kappa in all seven transverse directions (y, x1, x2, x3, x5, x6, x7)", "pValue" -> "15",
      "w" -> "w_req = p/rho = -5/7", "specNote" -> $meas["specDiscrepancy_pReqSign"]|>,
    "extrinsicCurvature" -> <|"convention" -> "unit normal n = +partial_y, K_ij = (1/2) partial_y g_ij, K^i_j = (1/2) g^{ik} partial_y g_kj",
      "value" -> "K^i_j = H delta^i_j on the six warped directions (x1,x2,x3,x5,x6,x7), 0 on x4; K = 6H", "values" -> ratStr /@ {1, 1, 1, 0, 1, 1, 1}|>,
    "extensions" -> <|
      "E1_smooth" -> "W = e^{Hy} for all y in R (the zeta chart of Stage 2 continued through y = 0); no brane; curvature invariants constant (see curvature.note)",
      "E2_Z2mirror" -> <|"warp" -> "W = e^{-H|y|}: two copies of the notebook patch glued at y = 0 (the notebook's pair of universes)",
        "israelConvention" -> $meas["geometry_israelSignConvention"],
        "jumpK" -> "[K^i_j] = -2H (six warped directions), 0 (x4); [K] = -12H",
        "braneStress" -> "S^i_j = -(10,10,10,12,10,10,10) H/kappa on (x1,x2,x3,x4,x5,x6,x7)", "braneStressValues" -> ratStr /@ {-10, -10, -10, -12, -10, -10, -10},
        "braneEnergyDensity" -> "rho_brane = -S^4_4 = +12 H/kappa", "branePressure" -> "p_brane = -10 H/kappa (not a pure tension: rho_brane != -p_brane)",
        "structuralRemark" -> "the gamma^8 map Psi -> gamma^8 Psi sends L_{m,U} to -L_{-m,-U} (CONTRACT errata E2); a mirror copy carrying gamma^8 Psi has mass -m: the notebook's +-M pair. This is a structural statement about the Lagrangian, not a physical claim."|>|>|>;];

(* ================================================================== *)
(* 4. KS_reduction                                                     *)
(* ================================================================== *)

(* block projectors and the exact basis (columns v+, v- = A1 v+ per block) *)
blockLabels = Flatten[Table[{s1, s2, s3}, {s1, {1, -1}}, {s2, {1, -1}}, {s3, {1, -1}}], 2];
blockProj[{s1_, s2_, s3_}] := ((id16 + s1 Jop)/2).((id16 - I s2 K1op)/2).((id16 - I s3 K2op)/2);
buildBlockBasis[] := Module[{},
  blockBasisData = Table[Module[{P = blockProj[b], Pp, col, vp, vm},
     Pp = P.((id16 + A0)/2);
     col = SelectFirst[Range[16], Pp[[All, #]] =!= ConstantArray[0, 16] &];
     vp = 8 Pp[[All, col]]; vm = A1.vp;  (* Gaussian-integer vectors, |v|^2 = 8 *)
     <|"labels" -> b, "column" -> col, "vp" -> vp, "vm" -> vm|>], {b, blockLabels}];
  Vint = Transpose[Flatten[Table[{d["vp"], d["vm"]}, {d, blockBasisData}], 1]];
  Vu = Vint/(2 Sqrt[2]);];
D16KSBlockBasis[] := Vu;
(* exact block extraction: V^dagger M V = Vint^dagger M Vint / 8 (no radicals) *)
blk[M_] := Module[{Y = Together[herm[Vint].M.Vint/8]}, Table[Y[[2 i - 1 ;; 2 i, 2 j - 1 ;; 2 j]], {i, 8}, {j, 8}]];
blockDiagQ[M_] := Module[{bb = blk[M]}, AllTrue[Flatten[Table[If[i == j, True, zeroMatQ[bb[[i, j]]]], {i, 8}, {j, 8}]], TrueQ]];
diagBlocks[M_] := Module[{bb = blk[M]}, Table[bb[[i, i]], {i, 8}]];
blockDirectSum[bl_List] := ArrayFlatten[Table[If[i == l, bl[[i]], ConstantArray[0, {2, 2}]], {i, 8}, {l, 8}]];

(* dimension of the algebra generated by a set of matrices (exact, span of products) *)
algebraDim[gens_] := Module[{basis = {Flatten[id16]}, frontier = {id16}, new, Mx, V},
  While[frontier =!= {},
   new = {};
   Do[Mx = Bm0.Gx;
    V = Append[basis, Flatten[Mx]];
    If[MatrixRank[V] > Length[basis], AppendTo[basis, Flatten[Mx]]; AppendTo[new, Mx]], {Bm0, frontier}, {Gx, gens}];
   frontier = new];
  Length[basis]];
commutantDim[mats_] := Module[{rows},
  rows = Join @@ Table[KroneckerProduct[Transpose[M], id16] - KroneckerProduct[id16, M], {M, mats}];
  256 - MatrixRank[rows]];
(* real-symbol conjugate transpose of a matrix whose entries are polynomials in real symbols and I *)
hermR[m_] := Transpose[m] /. Complex[a_, b_] :> Complex[a, -b];

Nfull := G[0].(Meff[y] id16 - I kk E^(-H y - a4c) G[1] + I (eps - vv[y]) G[4]);
Nblock[j_] := Meff[y] sig3 - E^(-H y - a4c) kk sig2 + I j (eps - vv[y]) sig1;

checkReduction[] := Module[{vp, nzOm, slash, chi, chib, Psi, dirac, red, target, d0, Psi0, dirP, redP, ok, types, typesFull, S12, rot, c0, HFc, kn, en, c2, r, chiR},
  (* spin connection in the y chart *)
  vp = Table[d1[m, evF[[n, a]]] - Sum[GamF[[r, m, n]] evF[[r, a]], {r, 8}] + Sum[omMixF[[m, a, b]] evF[[n, b]], {b, 8}], {m, 8}, {n, 8}, {a, 8}];
  addCheck["KS_reduction_vielbeinPostulate512", zeroMatQ[vp]];
  nzOm = Count[Flatten[omLF], x_ /; ! zeroQ[x]];
  addMeas["reduction_omegaNonzeroCount", nzOm];
  addCheck["KS_reduction_omegaCount12", nzOm === 12];
  addCheck["KS_reduction_OmegaClosedForms", zeroMatQ[OmF[[1]]] && zeroMatQ[OmF[[5]]] &&
    AllTrue[{2, 3, 4}, zeroMatQ[OmF[[#]] + H Wf E^a4c Sab[0, # - 1]] &] && AllTrue[{6, 7, 8}, zeroMatQ[OmF[[#]] - H Wf E^(-a4c) Sab[0, # - 1]] &]];
  slash = Sum[gUF[[mu]].OmF[[mu]], {mu, 8}];
  addCheck["KS_reduction_gammaSlashOmega3Hgamma0", zeroMatQ[slash - 3 H G[0]]];
  addCheck["KS_reduction_divergenceIdentity", zeroMatQ[Sum[d1[mu, sqrtgF gUF[[mu]]], {mu, 8}] - sqrtgF Sum[gUF[[mu]].OmF[[mu]] - OmF[[mu]].gUF[[mu]], {mu, 8}]]];
  (* the ansatz and the reduced equation *)
  chi = Table[ch[n][y], {n, 0, 15}];
  Psi = E^(-I eps x4) E^(I kk x1) E^(-3 H y) chi;
  dirac = Sum[gUF[[mu]].(d1[mu, Psi] + OmF[[mu]].Psi), {mu, 8}] - Meff[y] Psi;
  red = Expand[E^(I eps x4) E^(-I kk x1) E^(3 H y) dirac];
  target = G[0].D[chi, y] + I kk E^(-H y - a4c) G[1].chi - I eps G[4].chi - Meff[y] chi;
  addCheck["KS_reduction_ansatzRemoves3H", zeroMatQ[red - target]];
  addCheck["KS_reduction_reducedEquationODEForm", zeroMatQ[G[0].(target + Meff[y] chi + I eps G[4].chi - I kk E^(-H y - a4c) G[1].chi) - D[chi, y]] &&
    zeroMatQ[Nfull - G[0].(Meff[y] id16 - I kk E^(-H y - a4c) G[1] + I (eps - vv[y]) G[4])]];
  (* without the W^{-3} factor the 3H term survives *)
  Psi0 = E^(-I eps x4) E^(I kk x1) chi;
  d0 = Expand[E^(I eps x4) E^(-I kk x1) Sum[gUF[[mu]].(d1[mu, Psi0] + OmF[[mu]].Psi0), {mu, 8}]];
  addCheck["KS_reduction_withoutW3the3HTermSurvives", zeroMatQ[d0 - (G[0].D[chi, y] + 3 H G[0].chi + I kk E^(-H y - a4c) G[1].chi - I eps G[4].chi)]];
  (* measure: sqrt|g| Psi^dagger Psi = chi^dagger chi *)
  chib = Table[cb[n][y], {n, 0, 15}];
  addCheck["KS_reduction_flatMeasure", zeroQ[sqrtgF (E^(-3 H y) chib).(E^(-3 H y) chi) - chib.chi]];
  (* y > 0 patch of the Z2 geometry: W = e^{-Hy} (H -> -H in every geometric quantity), ansatz e^{+3Hy} chi *)
  Module[{gUFm = gUF /. H -> -H, OmFm = OmF /. H -> -H, PsiP = E^(-I eps x4) E^(I kk x1) E^(3 H y) chi},
   dirP = Sum[gUFm[[mu]].(d1[mu, PsiP] + OmFm[[mu]].PsiP), {mu, 8}];
   redP = Expand[E^(I eps x4) E^(-I kk x1) E^(-3 H y) dirP]];
  addCheck["KS_reduction_mirrorPatchSameForm", zeroMatQ[redP - (G[0].D[chi, y] + I kk E^(H y - a4c) G[1].chi - I eps G[4].chi)]];
  (* a4_0 enters only as k -> k e^{-a4_0} *)
  addCheck["KS_reduction_a4IsMomentumRescaling", zeroMatQ[(target /. kk -> kk E^(a4c)) - (target /. a4c -> 0)] && ! zeroMatQ[target - (target /. a4c -> 0)]];
  (* block structure *)
  buildBlockBasis[];
  addCheck["KS_reduction_JK1K2commute", Jop.Jop === id16 && K1op.K1op === -id16 && K2op.K2op === -id16 &&
    AllTrue[Flatten[Table[X.Y === Y.X, {X, {Jop, K1op, K2op}}, {Y, {A0, A1, A4, Bm, C16, Jop, K1op, K2op}}]], TrueQ]];
  addCheck["KS_reduction_projectorsRank2", AllTrue[blockLabels, Module[{P = blockProj[#]}, P.P === P && MatrixRank[P] === 2 && Tr[P] === 2 && herm[P] === P] &] &&
    Total[blockProj /@ blockLabels] === id16];
  addCheck["KS_reduction_basisUnitary", Together[herm[Vint].Vint/8] === id16 && AllTrue[Flatten[Vint], MemberQ[{0, 1, -1, I, -I}, #] &] &&
    AllTrue[Transpose[Vint], Conjugate[#].# === 8 &]];
  addCheck["KS_reduction_basisIsJointEigenbasis", AllTrue[Range[8], Module[{b = blockLabels[[#]], v1 = Vint[[All, 2 # - 1]], v2 = Vint[[All, 2 #]]},
      Jop.v1 === b[[1]] v1 && Jop.v2 === b[[1]] v2 && K1op.v1 === I b[[2]] v1 && K1op.v2 === I b[[2]] v2 && K2op.v1 === I b[[3]] v1 && K2op.v2 === I b[[3]] v2 && A0.v1 === v1 && A0.v2 === -v2 && A1.v1 === v2] &]];
  addCheck["KS_reduction_fiveMatricesBlockDiagonal", AllTrue[{A0, A1, A4, Bm, C16, BC, G[4].G[1], Jop, K1op, K2op}, blockDiagQ]];
  addCheck["KS_reduction_blocksA0A1A4", diagBlocks[A0] === ConstantArray[sig3, 8] && diagBlocks[A1] === ConstantArray[-I sig2, 8] &&
    diagBlocks[A4] === Table[b[[1]] sig1, {b, blockLabels}]];
  addCheck["KS_reduction_blocksBC", diagBlocks[Bm] === Table[b[[1]] b[[2]] id2, {b, blockLabels}] && diagBlocks[C16] === Table[b[[2]] sig2, {b, blockLabels}] &&
    diagBlocks[BC] === Table[b[[1]] sig2, {b, blockLabels}] && diagBlocks[G[4].G[1]] === Table[-b[[1]] sig3, {b, blockLabels}] &&
    diagBlocks[Jop] === Table[b[[1]] id2, {b, blockLabels}] && diagBlocks[K1op] === Table[I b[[2]] id2, {b, blockLabels}] && diagBlocks[K2op] === Table[I b[[3]] id2, {b, blockLabels}]];
  addCheck["KS_reduction_reconstructFromBlocks", AllTrue[{A0, A1, A4, Bm, C16}, Together[Vint.blockDirectSum[diagBlocks[#]].herm[Vint]/8] === # &]];
  addCheck["KS_reduction_gamma2gamma3NotBlockDiagonal", ! blockDiagQ[G[0].G[2]] && ! blockDiagQ[G[0].G[3]]];
  (* chirality and gamma^0 gamma^8 swap j -> -j *)
  addCheck["KS_reduction_gamma8SwapsJ", g8.Jop === -Jop.g8 && g8.K1op === K1op.g8 && g8.K2op === K2op.g8 && G[0].g8 === G[1].G[2].G[3].G[4].G[5].G[6].G[7]];
  addMeas["reduction_algebraDim_A0A1A4", algebraDim[{A0, A1, A4}]];
  addMeas["reduction_commutantDim_A0A1A4", commutantDim[{A0, A1, A4}]];
  addMeas["reduction_commutantDim_A0A1A4BC", commutantDim[{A0, A1, A4, Bm, C16}]];
  addCheck["KS_reduction_algebraDim8", $meas["reduction_algebraDim_A0A1A4"] === 8 && A0.A1 === -A1.A0 && A0.A4 === -A4.A0 && A1.A4 === -A4.A1 &&
    A0.A0 === id16 && A1.A1 === -id16 && A4.A4 === id16 && A0.A1.A4 === -Jop];
  addCheck["KS_reduction_commutantDims", $meas["reduction_commutantDim_A0A1A4"] === 32 && $meas["reduction_commutantDim_A0A1A4BC"] === 16];
  types = Union[Table[{diagBlocks[A0][[i]], diagBlocks[A1][[i]], diagBlocks[A4][[i]]}, {i, 8}]];
  typesFull = Union[Table[{diagBlocks[A0][[i]], diagBlocks[A1][[i]], diagBlocks[A4][[i]], diagBlocks[Bm][[i]], diagBlocks[C16][[i]]}, {i, 8}]];
  addMeas["reduction_inequivalentBlockTypes_yEquation", Length[types]];
  addMeas["reduction_inequivalentBlockTypes_withBandC", Length[typesFull]];
  addCheck["KS_reduction_blockTypes", Length[types] === 2 && Length[typesFull] === 4];
  (* the 2x2 y-equation: chi' = N chi with N = Meff s3 - kappa k s2 + i j (eps - vv) s1 *)
  addCheck["KS_reduction_blockODEMatrix", AllTrue[Range[8], zeroMatQ[diagBlocks[Nfull][[#]] - Nblock[blockLabels[[#, 1]]]] &] && blockDiagQ[Nfull]];
  (* block Hamiltonian h_j = j[-i s1 d_y + Meff s2 + kappa k s3] + vv;  h chi = eps chi  <=>  chi' = N chi *)
  c2 = {ch[0][y], ch[1][y]};
  addCheck["KS_reduction_blockHamiltonianEquivalentToODE", AllTrue[{1, -1}, Module[{j = #, hc},
      hc = j (-I sig1.D[c2, y] + Meff[y] sig2.c2 + E^(-H y - a4c) kk sig3.c2) + vv[y] c2 - eps c2;
      zeroMatQ[hc + I j sig1.(D[c2, y] - Nblock[j].c2)]] &]];
  addCheck["KS_reduction_hMinusEqualsMinusHPlus", zeroMatQ[Nblock[-1] - (Nblock[1] /. eps -> 2 vv[y] - eps)]];
  (* sigma3 conjugation: sigma3 N(k, j) sigma3 = N(-k, -j) at fixed eps; complex conjugation does the same *)
  addCheck["KS_reduction_sigma3ConjugationFlipsK", AllTrue[{1, -1}, zeroMatQ[sig3.Nblock[#].sig3 - (Nblock[-#] /. kk -> -kk)] && zeroMatQ[hermR[Transpose[Nblock[#]]] - (Nblock[-#] /. kk -> -kk)] &]];
  (* rotational symmetry: exp(theta S^{12}) rotates gamma^1 into gamma^2 and commutes with gamma^0, gamma^4, B, C *)
  S12 = Sab[1, 2];
  rot = Cos[th/2] id16 + 2 Sin[th/2] S12;
  addCheck["KS_reduction_rotationalSymmetry", (S12.G[1] - G[1].S12) === -G[2] && Simplify[rot.G[1].(Cos[th/2] id16 - 2 Sin[th/2] S12) - (Cos[th] G[1] - Sin[th] G[2])] === zero16 && S12.S12 === -id16/4 &&
    AllTrue[{A0, G[4], Bm, C16}, S12.# === #.S12 &] && Simplify[rot.(Cos[th/2] id16 - 2 Sin[th/2] S12)] === id16];
  (* exact k = 0 box spectrum for constant Meff = M, vv = 0, chi_2(0) = 0 and chi_2(-L) = 0 *)
  addCheck["KS_reduction_k0ZeroMode", Module[{cz = {E^(M y), 0}, NN0 = M sig3 + I j0 0 sig1}, Simplify[D[cz, y] - NN0.cz] === {0, 0} && (cz[[2]] /. y -> 0) === 0 &&
     Simplify[Integrate[E^(2 M y), {y, -Infinity, 0}, Assumptions -> M > 0] - 1/(2 M)] === 0]];
  kn = nn Pi/LL; en = Sqrt[M^2 + kn^2];
  c2 = {(M Sin[kn y] + kn Cos[kn y])/(I j0 en), Sin[kn y]};
  r = D[c2, y] - (M sig3 + I j0 en sig1).c2;
  addCheck["KS_reduction_k0MassiveLevels", Simplify[r /. j0 -> 1] === {0, 0} && Simplify[r /. j0 -> -1] === {0, 0} && (c2[[2]] /. y -> 0) === 0 &&
    Simplify[(c2[[2]] /. y -> -LL), Element[nn, Integers]] === 0];
  (* first-order splitting of the zero mode: d eps/dk at k = 0 = j <chi_0| kappa sigma3 |chi_0>, chi_0 = (e^{My}, 0) *)
  HFc = Integrate[E^(-H y - a4c) E^(2 M y), {y, -LL, 0}, Assumptions -> M > 0 && H > 0 && LL > 0 && 2 M > H]/Integrate[E^(2 M y), {y, -LL, 0}, Assumptions -> M > 0 && LL > 0];
  c0 = Simplify[HFc];
  addMeas["reduction_zeroModeSplittingCoefficient", toStr[c0]];
  Module[{c0e = c0 /. Power[E, ex_] :> YY^(Coefficient[Expand[ex], LL H]) XX^(Coefficient[Expand[ex], LL M]/2) ea^Coefficient[Expand[ex], a4c]},
   (* XX = e^{2ML} > YY = e^{HL} > 1 for 2M > H > 0 *)
   addCheck["KS_reduction_zeroModeSplitting", Simplify[c0 - E^(-a4c) (2 M/(2 M - H)) (1 - E^(-(2 M - H) LL))/(1 - E^(-2 M LL))] === 0 &&
     FreeQ[c0e, E] && Simplify[c0e > 0, XX > YY && YY > 1 && 2 M > H && H > 0 && ea > 0] === True]];
  $theory["reduction"] = <|
    "spinConnection" -> <|"nonzeroOmegaLowered" -> nzOm, "Omega" -> "Omega_y = Omega_4 = 0, Omega_i = -H e^{Hy+a_4} S^{0i} (i=1,2,3), Omega_j = +H e^{Hy-a_4} S^{0j} (j=5,6,7)",
      "gammaSlashOmega" -> "gamma^mu Omega_mu = 3 H gamma^0 (a_4-independent); divergence identity partial_mu(sqrt|g| gamma^mu) = sqrt|g| [gamma^mu, Omega_mu] holds"|>,
    "ansatz" -> <|"tex" -> "\\Psi=e^{-i\\varepsilon x_4}e^{i\\vec k\\cdot\\vec x}W(y)^{-3}\\chi(y),\\quad W^{-3}=e^{-3Hy}",
      "measure" -> "sqrt|g| Psi^dagger Psi d^8x = chi^dagger chi dy d^7x (flat in y)",
      "sector" -> "no dependence on x5,x6,x7 (q = 0, the good sector); 3-torus of size l, k in (2 pi/l) Z^3; k = (k,0,0) by rotational symmetry"|>,
    "reducedEquation" -> <|"tex" -> "\\gamma^0\\chi'+i\\kappa(y)k_j\\gamma^j\\chi-i\\varepsilon\\gamma^4\\chi=M_{\\mathrm{eff}}(y)\\chi,\\qquad \\kappa(y)=e^{-Hy-a_4}",
      "odeForm" -> "chi' = gamma^0 [ Meff chi - i kappa k_j gamma^j chi + i eps gamma^4 chi ]",
      "withExchange" -> "chi' = gamma^0 [ Meff chi - i kappa k_j gamma^j chi + i (eps - v_v(y)) gamma^4 chi ], Meff = m + lambda S_p + v_s",
      "mirrorPatch" -> "on the y > 0 side of the Z2 geometry (W = e^{-Hy}, ansatz factor e^{+3Hy}) the same equation holds with kappa(y) = e^{H y - a_4}: kappa is even in y",
      "a4Rescaling" -> "a_4 enters only through kappa: k -> k e^{-a_4}"|>,
    "blockDiagonalisation" -> <|
      "commutingOperators" -> "J = gamma^0 gamma^1 gamma^4 (J^2 = 1), K1 = gamma^2 gamma^3 (K1^2 = -1), K2 = gamma^5 gamma^6 (K2^2 = -1); they commute with each other and with gamma^0, gamma^0 gamma^1, gamma^0 gamma^4, B, C",
      "projector" -> "P(j,s2,s3) = (1 + j J)/2 (1 - i s2 K1)/2 (1 - i s3 K2)/2, rank 2 each, eight blocks, sum = 1",
      "basisConstruction" -> "v+ = 8 P(j,s2,s3) (1 + gamma^0)/2 e_c (first standard vector e_c with nonzero image; seedColumn = c, 0-based), v- = gamma^0 gamma^1 v+; entries in {0, +-1, +-i}, |v|^2 = 8; V = [v+ v- ...]/(2 sqrt 2) is unitary; chi_16 = V chi_block; block matrices are V^dagger M V",
      "matrixEntryFormat" -> "[re, im] pairs of rational strings 'n' or 'n/d'; basis columns are given unnormalised (Gaussian integers, columnNormSquared 8)",
      "columnNormSquared" -> "8",
      "blockOrder" -> "index = 4(1-j)/2 + 2(1-s2)/2 + (1-s3)/2: (j,s2,s3) = (1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)",
      "blocks" -> Table[<|"index" -> i - 1, "j" -> ratStr[blockLabels[[i, 1]]], "s2" -> ratStr[blockLabels[[i, 2]]], "s3" -> ratStr[blockLabels[[i, 3]]],
          "K1eigenvalue" -> gq[I blockLabels[[i, 2]]], "K2eigenvalue" -> gq[I blockLabels[[i, 3]]], "Beigenvalue" -> ratStr[blockLabels[[i, 1]] blockLabels[[i, 2]]],
          "seedColumn" -> blockBasisData[[i, "column"]] - 1,
          "vPlus" -> gqVec[Vint[[All, 2 i - 1]]], "vMinus" -> gqVec[Vint[[All, 2 i]]],
          "A0" -> gqMat[diagBlocks[A0][[i]]], "A1" -> gqMat[diagBlocks[A1][[i]]], "A4" -> gqMat[diagBlocks[A4][[i]]],
          "B" -> gqMat[diagBlocks[Bm][[i]]], "C" -> gqMat[diagBlocks[C16][[i]]], "BC" -> gqMat[diagBlocks[BC][[i]]],
          "gamma4gamma1" -> gqMat[diagBlocks[G[4].G[1]][[i]]],
          "numberDensityMatrix" -> gqMat[id2], "scalarDensityMatrix" -> gqMat[diagBlocks[BC][[i]]],
          "yCurrentMatrix" -> gqMat[diagBlocks[A4][[i]]], "kCurrentMatrix" -> gqMat[-diagBlocks[G[4].G[1]][[i]]]|>, {i, 8}],
      "basisMatrixUnnormalised" -> gqMat[Vint],
      "blockFormulas" -> <|"A0" -> "sigma3", "A1" -> "-i sigma2 = [[0,-1],[1,0]]", "A4" -> "j sigma1", "B" -> "j s2 (scalar)", "C" -> "s2 sigma2", "BC" -> "j sigma2", "gamma4gamma1" -> "-j sigma3", "J" -> "j", "K1" -> "i s2", "K2" -> "i s3"|>,
      "types" -> <|"yEquation" -> "2 inequivalent types for {gamma^0, gamma^0 gamma^1, gamma^0 gamma^4}: j = +1 (blocks 0-3) and j = -1 (blocks 4-7), 4 blocks each",
        "withBandC" -> "4 inequivalent types for {gamma^0, gamma^0 gamma^1, gamma^0 gamma^4, B, C}: (j, s2), 2 blocks each (s3 = +-1)",
        "algebraDim" -> $meas["reduction_algebraDim_A0A1A4"], "commutantDim" -> $meas["reduction_commutantDim_A0A1A4"], "commutantDimWithBC" -> $meas["reduction_commutantDim_A0A1A4BC"],
        "multiplicity" -> "eight 2x2 blocks: the 16-component equation is a 2x2 first-order system with an 8-fold block multiplicity; the two j-types have opposite block Hamiltonians"|>,
      "densityRule" -> "for a Hilbert-normalised block orbital chi (integral chi^dagger chi dy = 1): number density n = e^{-6Hy} chi^dagger chi / l^3, scalar density s = e^{-6Hy} chi^dagger (j sigma2) chi / l^3 (= u^dagger B C u), k-current density t = e^{-6Hy} chi^dagger (j sigma3) chi / l^3 (= u^dagger B (-gamma^4 gamma^1) u), y-current c = e^{-6Hy} chi^dagger (j sigma1) chi / l^3 (= u^dagger B (-i C gamma^0) u)",
      "chirality" -> "gamma^8 anticommutes with J and commutes with K1, K2: it maps block (j,s2,s3) onto block (-j,s2,s3); gamma^0 gamma^8 = gamma^1...gamma^7 does the same"|>,
    "blockODE" -> <|"N" -> "chi' = N chi, N = Meff(y) sigma3 - kappa(y) k sigma2 + i j (eps - v_v(y)) sigma1",
      "components" -> "chi_1' = Meff chi_1 + (i kappa k + i j (eps - v_v)) chi_2, chi_2' = -Meff chi_2 + (-i kappa k + i j (eps - v_v)) chi_1",
      "hamiltonian" -> "h_j = j [ -i sigma1 d/dy + Meff(y) sigma2 + kappa(y) k sigma3 ] + v_v(y); h_j chi = eps chi; h_{-1} - v_v = -(h_{+1} - v_v)",
      "spectrumRelations" -> "spec(h_{-1} - v_v) = -spec(h_{+1} - v_v); sigma3 N(k, j) sigma3 = N(-k, -j) at fixed eps, so |chi|^2 of the (k, j) and (-k, -j) orbitals coincide and their scalar densities agree; complex conjugation gives the same map (real structure)",
      "degeneracy" -> "at fixed k = (k,0,0): each level of h_{+1} is 4-fold (blocks 0-3), each level of h_{-1} 4-fold (blocks 4-7); the full spectrum at fixed k is symmetric under eps - v_v -> -(eps - v_v); 8-fold degeneracy of every level holds at k = 0 (exact spectrum below) and over a closed shell {k, -k}; whether spec(h_{+1}(k)) is itself symmetric for k != 0 is a numerical question (generically not: the zero mode splits linearly, see zeroMode)",
      "k0ExactSpectrum" -> <|"conditions" -> "k = 0, Meff = M constant, v_v = 0, chi_2(0) = 0 (even parity at the brane) and chi_2(-L) = 0 (bag theta = 0)",
        "zeroMode" -> "eps = 0, chi = (e^{My}, 0): normalisable on (-infinity, 0] for M > 0, localised at the brane, proper density n_p ~ e^{(2M - 6H) y}",
        "massiveLevels" -> "eps = +- sqrt(M^2 + (n pi/L)^2), n = 1, 2, ...; chi_2 = sin(n pi y/L), chi_1 = (M sin(k_n y) + k_n cos(k_n y))/(i j eps), k_n = n pi/L",
        "count" -> "each level 4-fold per j; with h_{-1} = -h_{+1}: 0 (8-fold), +-sqrt(M^2 + (n pi/L)^2) (8-fold each)"|>,
      "zeroMode" -> <|"splitting" -> "d eps_0/dk |_{k=0} = j c, c = integral_{-L}^0 e^{-Hy-a_4} e^{2My} dy / integral_{-L}^0 e^{2My} dy = e^{-a_4} (2M/(2M-H)) (1 - e^{-(2M-H)L})/(1 - e^{-2ML}) > 0 (Hellmann-Feynman, first order in k)",
        "cValue" -> toStr[c0], "consequence" -> "for k != 0 the zero-mode band is eps = +- c k + O(k^2): 4 states at +ck (j = +1) and 4 at -ck (j = -1) at the same k vector; the massless brane fermion of the orbifold"|>|>|>;];

(* ================================================================== *)
(* 5. KS_boundary                                                      *)
(* ================================================================== *)

checkBoundary[] := Module[{Jy, c2, cur, projE, projO, Q, chiE, bagOK, Ngen, PA, PB, pairs, ph, lhs},
  (* the y-current: J^y = -i Psibar gamma^y Psi = -i Psi^dagger C gamma^0 Psi (gamma^y = gamma^0 since h_y = 1);
     expectation rule -> u^dagger B (-i C gamma^0) u = u^dagger (gamma^0 gamma^4) u = u^dagger A4 u *)
  Jy = Bm.(-I C16.G[0]);
  addCheck["KS_boundary_currentMatrix", Jy === A4 && herm[A4] === A4 && Transpose[A4] === A4 && gUF[[1]] === G[0]];
  (* conservation along y: d/dy (chi^dagger A4 chi) = chi^dagger (N^dagger A4 + A4 N) chi = 0 for real eps, Meff, v_v *)
  addCheck["KS_boundary_currentConservedAlongY", zeroMatQ[hermR[Nfull].A4 + A4.Nfull]];
  (* the Hilbert norm is not conserved along y *)
  addCheck["KS_boundary_hilbertNormNotConservedAlongY", ! zeroMatQ[hermR[Nfull] + Nfull]];
  (* 2x2 form: current = j chi^dagger sigma1 chi = 2 j Re(chi_1^* chi_2) *)
  c2 = {ch[0][y], ch[1][y]};
  cur = {cb[0][y], cb[1][y]}.sig1.c2;
  addCheck["KS_boundary_currentBlockForm", diagBlocks[A4] === Table[b[[1]] sig1, {b, blockLabels}] && zeroR[cur - (cb[0][y] ch[1][y] + cb[1][y] ch[0][y])]];
  (* parity: Psi(-y) = +- gamma^0 Psi(y)  =>  (1 -+ gamma^0) chi(0) = 0  =>  chi_2(0) = 0 (even) or chi_1(0) = 0 (odd) *)
  projE = (id2 - sig3)/2; projO = (id2 + sig3)/2;
  addCheck["KS_boundary_parityProjectorsBlockForm", diagBlocks[(id16 - A0)/2] === ConstantArray[projE, 8] && diagBlocks[(id16 + A0)/2] === ConstantArray[projO, 8] &&
    projE.{u1, u2} === {0, u2} && projO.{u1, u2} === {u1, 0}];
  addCheck["KS_boundary_parityKillsCurrent", zeroR[cur /. {ch[1][y] -> 0, cb[1][y] -> 0}] && zeroR[cur /. {ch[0][y] -> 0, cb[0][y] -> 0}]];
  (* bag family at y = -L: (1 - Q(theta)) chi(-L) = 0, Q = cos(theta) sigma3 + sin(theta) sigma2 *)
  Q = Cos[th] sig3 + Sin[th] sig2;
  bagOK = Simplify[Q.Q] === id2 && Simplify[Transpose[Q] /. Complex[a_, b_] :> Complex[a, -b]] === Q && Simplify[Q.sig1 + sig1.Q] === ConstantArray[0, {2, 2}];
  chiE = {Cos[th/2], I Sin[th/2]};
  addCheck["KS_boundary_bagFamily", bagOK && Simplify[Q.chiE - chiE] === {0, 0} && Simplify[{Cos[th/2], -I Sin[th/2]}.sig1.chiE] === 0];
  addCheck["KS_boundary_bagThetaZeroIsEvenParity", (Q /. th -> 0) === sig3 && (chiE /. th -> 0) === {1, 0} && (Q /. th -> Pi/2) === sig2 && Simplify[(chiE /. th -> -Pi/2)/(chiE /. th -> -Pi/2)[[1]]] === {1, -I}];
  addCheck["KS_boundary_bagIn16", diagBlocks[Cos[th] A0 + I Sin[th] A1] === ConstantArray[Q, 8]];
  (* generic proof: for Q chi = chi, Q Hermitian, {Q, sigma1} = 0: chi^dagger sigma1 chi = chi^dagger sigma1 Q chi = -chi^dagger Q sigma1 chi = -chi^dagger sigma1 chi *)
  addCheck["KS_boundary_currentKilledByAnticommutingProjector", zeroR[Simplify[{w1, w2}.(sig1.Q + Q.sig1).{v1, v2}]]];
  (* self-adjointness: the derivative part of <phi|h chi> - <h phi|chi> is a total derivative of -i j phi^dagger sigma1 chi *)
  ph = {cb[0][y], cb[1][y]};
  lhs = ph.(-I sig1.D[c2, y]) - (I D[ph, y].sig1).c2;
  addCheck["KS_boundary_selfAdjointBoundaryTerm", zeroQ[lhs + I D[ph.sig1.c2, y]]];
  (* the tip asymptotics: for large kappa the equation is chi' = -kappa k sigma2 chi; eigenvector (1, -i) of sigma2 (eigenvalue -1) gives chi' = +kappa k chi, decaying toward the tip for k > 0 *)
  addCheck["KS_boundary_tipAsymptotics", sig2.{1, -I} === -{1, -I} && sig2.{1, I} === {1, I} && zeroRMat[(-kap0 kk sig2.{1, -I}) - kap0 kk {1, -I}]];
  (* reflection symmetries: chi_R(y) := R chi(-y) solves chi_R' = N_R chi_R with N_R(y) = -R N(-y) R^{-1}.
     With y-independent generic coefficients (kappa even on the Z2 geometry) the test is -R N R^{-1} =?= N with modified parameters *)
  Ngen = G[0].(mM id16 - I kp kk G[1] + I (eps - vV) G[4]);
  PA = A0; PB = I G[0].g8;
  addCheck["KS_boundary_parityA_symmetryIffMassOdd", zeroRMat[-PA.Ngen.PA - (Ngen /. mM -> -mM)] && ! zeroRMat[-PA.Ngen.PA - Ngen]];
  addCheck["KS_boundary_parityB_symmetryForEvenMass", zeroRMat[-PB.Ngen.PB - Ngen] && herm[PB] === PB && PB.PB === id16 && PB === I G[1].G[2].G[3].G[4].G[5].G[6].G[7]];
  addCheck["KS_boundary_parityB_couplesJBlocks", PB.Jop === -Jop.PB && ! blockDiagQ[PB] && PB.K1op === K1op.PB && PB.K2op === K2op.PB];
  addCheck["KS_boundary_parityOperatorsKillCurrent", PB.A4 === -A4.PB && PA.A4 === -A4.PA];
  (* scalar density odd under P_A (gamma^0 BC gamma^0 = -BC), even under P_B; number density even under both; k-current even under P_A, odd under P_B *)
  addCheck["KS_boundary_densityParities", PA.BC.PA === -BC && PB.BC.PB === BC && PA.(G[4].G[1]).PA === G[4].G[1] && PB.(G[4].G[1]).PB === G[4].G[1] && PA.A4.PA === -A4 && PB.A4.PB === -A4];
  (* 4x4 form of P_B on the block pair (j,s2,s3), (-j,s2,s3) *)
  pairs = Table[Module[{ip = Position[blockLabels, {-blockLabels[[i, 1]], blockLabels[[i, 2]], blockLabels[[i, 3]]}][[1, 1]]}, {i, ip, blk[PB][[i, ip]]}], {i, 8}];
  Module[{bbPB = blk[PB]},
   addCheck["KS_boundary_parityB_pairBlocks", AllTrue[pairs, MemberQ[{sig1, -sig1}, #[[3]]] &] &&
     AllTrue[Range[8], Function[i, AllTrue[Range[8], Function[l, l == pairs[[i, 2]] || zeroMatQ[bbPB[[i, l]]]]]]]]];
  $theory["boundary"] = <|
    "yCurrent" -> <|"operator" -> "J^y = -i Psibar gamma^y Psi = -i Psi^dagger C gamma^0 Psi (gamma^y = gamma^0 because h_y = 1)",
      "expectationRule" -> "u^dagger B(-i C gamma^0) u = u^dagger (gamma^0 gamma^4) u = u^dagger A4 u",
      "matrix16" -> "A4 = gamma^0 gamma^4 (real symmetric, Hermitian)", "blockForm" -> "j sigma1: J^y_mode = j (chi_1^* chi_2 + chi_2^* chi_1) e^{-6Hy}/l^3",
      "conservation" -> "d/dy (chi^dagger A4 chi) = 0 for every solution of the reduced equation with real eps, Meff, v_v (N^dagger A4 + A4 N = 0); the Hilbert norm chi^dagger chi is not conserved along y (N^dagger + N != 0)",
      "specNote" -> "STAGE4_SPEC section 4 writes 'chi^dagger (B gamma^4 gamma^0 or the correct current matrix) chi'; the correct matrix is A4 = gamma^0 gamma^4 = -gamma^4 gamma^0 (B is already absorbed by the expectation rule: B(-iC gamma^0) = -gamma^4 gamma^0)"|>,
    "parityConditions" -> <|"statement" -> "Psi(-y) = +- gamma^0 Psi(y): (1 -+ gamma^0) chi(0) = 0",
      "blockForm" -> "gamma^0 = sigma3 in every block: even parity chi_2(0) = 0, odd parity chi_1(0) = 0",
      "projectors" -> <|"even" -> gqMat[projE], "odd" -> gqMat[projO], "note" -> "the condition is P chi(0) = 0 with P = (1 -+ sigma3)/2"|>,
      "killsCurrent" -> "chi^dagger sigma1 chi = 2 Re(chi_1^* chi_2) vanishes when either component vanishes",
      "symmetry" -> "P_A: chi(y) -> gamma^0 chi(-y) maps solutions of the reduced equation with mass function M(y) onto solutions with -M(-y) (kappa is even on the Z2 geometry): it is a symmetry iff Meff is odd, i.e. the mirror universe carries the opposite mass (the notebook's +-M pair, CONTRACT errata E2: the mirror copy gamma^8 Psi has mass -m); the scalar density Psibar Psi is P_A-odd (gamma^0 BC gamma^0 = -BC), consistent with an odd Hartree shift lambda S_p; the number density is P_A-even; the k-current t is P_A-even; the y-current is P_A-odd",
      "alternative" -> "P_B: chi(y) -> i gamma^0 gamma^8 chi(-y) (i gamma^0 gamma^8 = i gamma^1...gamma^7, Hermitian, squares to 1) is the symmetry for an EVEN mass function (identical mirror universe); it also kills the current (anticommutes with A4) and leaves Psibar Psi and the k-current even, but it anticommutes with J: the condition (1 -+ P_B) chi(0) = 0 couples block (j,s2,s3) with block (-j,s2,s3) (P_B = +-sigma1 between the two blocks of the pair), so the KS problem would be a 4x4 system on block pairs",
      "used" -> "the KS problem uses P_A (STAGE4_SPEC), which is block diagonal (2x2)"|>,
    "bagCondition" -> <|"family" -> "(1 - Q(theta)) chi(-L) = 0, Q(theta) = cos(theta) sigma3 + sin(theta) sigma2; Q Hermitian, Q^2 = 1, {Q, sigma1} = 0",
      "eigenvector" -> "chi(-L) proportional to (cos(theta/2), i sin(theta/2))",
      "default" -> "theta = 0: chi_2(-L) = 0 (the even-parity condition at the tip; admits the k = 0 chiral zero mode e^{My} for every L)",
      "asymptotic" -> "theta = -pi/2 for k > 0 (chi(-L) proportional to (1, -i)), theta = +pi/2 for k < 0: the eigenvector of sigma2 with eigenvalue -sgn(k) is the solution that decays toward the tip when the confining term -kappa k sigma2 dominates",
      "proof" -> "chi^dagger sigma1 chi = chi^dagger sigma1 Q chi = -chi^dagger Q sigma1 chi = -chi^dagger sigma1 chi = 0 for Q chi = chi",
      "selfAdjointness" -> "the boundary term of <phi|h chi> - <h phi|chi> is -i j [phi^dagger sigma1 chi] between the two ends; it vanishes on the domain defined by any pair of current-killing conditions, so h is self-adjoint, eps is real and eigenfunctions of different eps are orthogonal in the flat y-measure",
      "in16" -> "Q(theta) = cos(theta) gamma^0 + i sin(theta) gamma^0 gamma^1 (chiral-bag family)"|>|>;];

(* ================================================================== *)
(* 6. KS_exchange                                                      *)
(* ================================================================== *)

(* exact Fock space of d fermionic modes (Jordan-Wigner) *)
jwOps[d_] := Module[{sz = {{1, 0}, {0, -1}}, sm = {{0, 1}, {0, 0}}, i2 = IdentityMatrix[2]},
  Table[KroneckerProduct @@ Join[ConstantArray[sz, a - 1], {sm}, ConstantArray[i2, d - a]], {a, d}]];

checkExchange[] := Module[{d = 4, cs, cds, dim, car, Mx, Mh, orbs, sets, vac, slater, Sop, S2n, ok, okNorm, hp, hq, Pp, Pq, Pqm, Kpp, Kpm, Kmm, pdq, ang, rho2, nkF, SkF, ekF, exkF, dex, ratio},
  cs = jwOps[d]; cds = ConjugateTranspose /@ cs; dim = 2^d;
  car = AllTrue[Flatten[Table[cs[[a]].cds[[b]] + cds[[b]].cs[[a]] === If[a == b, 1, 0] IdentityMatrix[dim] && cs[[a]].cs[[b]] + cs[[b]].cs[[a]] === 0 IdentityMatrix[dim], {a, d}, {b, d}]], TrueQ];
  addCheck["KS_exchange_fockModelCAR", car];
  (* a fixed Hermitian matrix with Gaussian-rational entries *)
  Mx = {{1, (1 + 2 I)/3, -1/2, I/5}, {0, -2/7, (3 - I)/4, 1/3}, {0, 0, 5/6, (-2 + 5 I)/9}, {0, 0, 0, -3/2}};
  Mh = Mx + ConjugateTranspose[Mx];
  Sop = Sum[Mh[[a, b]] cds[[a]].cs[[b]], {a, d}, {b, d}];
  (* normal-ordered square: :S^2: = sum M_ab M_cd c^dagger_a c^dagger_c c_d c_b *)
  S2n = Sum[Mh[[a, b]] Mh[[c, e]] cds[[a]].cds[[c]].cs[[e]].cs[[b]], {a, d}, {b, d}, {c, d}, {e, d}];
  orbs = {{3/5, 4/5, 0, 0}, {-4/5, 3/5, 0, 0}, {0, 0, 5/13, 12 I/13}};
  okNorm = AllTrue[Flatten[Table[Conjugate[orbs[[i]]].orbs[[j]] === If[i == j, 1, 0], {i, 3}, {j, 3}]], TrueQ];
  vac = UnitVector[dim, 1]; (* all modes empty: sm = {{0,1},{0,0}} annihilates (1,0) *)
  addCheck["KS_exchange_fockVacuum", AllTrue[cs, #.vac === ConstantArray[0, dim] &] && okNorm];
  sets = {{1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}};
  ok = AllTrue[sets, Module[{occ = #, st, rho, lhs, rhs, direct, ex},
      st = Fold[Sum[orbs[[#2, a]] cds[[a]], {a, d}].#1 &, vac, Reverse[occ]];
      rho = Sum[Outer[Times, orbs[[n]], Conjugate[orbs[[n]]]], {n, occ}]; (* rho = sum u u^dagger *)
      lhs = Conjugate[st].S2n.st/(Conjugate[st].st);
      direct = Tr[Mh.rho]; ex = Tr[Mh.rho.Mh.rho];
      rhs = direct^2 - ex;
      Simplify[lhs - rhs] === 0 && Simplify[Conjugate[st].Sop.st/(Conjugate[st].st) - direct] === 0 &&
       Simplify[Conjugate[st].Sop.Sop.st/(Conjugate[st].st) - (rhs + Tr[Mh.Mh.rho])] === 0] &];
  addCheck["KS_exchange_wickTheoremHF", ok];
  (* filled shell of the uniform gas at momentum p (4 spatial components: y, x1, x2, x3) *)
  hp = -I m G[4] - G[4].(p0 G[0] + p1 G[1] + p2 G[2] + p3 G[3]);
  hq = -I m G[4] - G[4].(q0 G[0] + q1 G[1] + q2 G[2] + q3 G[3]);
  addCheck["KS_exchange_modeHamiltonian", zeroRMat[hp.hp - (m^2 + p0^2 + p1^2 + p2^2 + p3^2) id16] && zeroRMat[hermR[hp] - hp] && Tr[hp] === 0];
  Pp = (id16 + hp/Ep)/2; Pq = (id16 + hq/Eq)/2; Pqm = (id16 - hq/Eq)/2;
  addCheck["KS_exchange_projectorRank8", zeroRMat[(Pp.Pp - Pp) /. Ep -> Sqrt[m^2 + p0^2 + p1^2 + p2^2 + p3^2]] && Simplify[Tr[Pp]] === 8];
  addCheck["KS_exchange_filledShellScalarDensity", zeroR[Tr[BC.Pp] - 8 m/Ep] && zeroR[Tr[Bm.Bm.Pp] - 8]];
  pdq = p0 q0 + p1 q1 + p2 q2 + p3 q3;
  Kpp = Tr[Pp.BC.Pq.BC]; Kpm = Tr[Pp.BC.Pqm.BC]; Kmm = Tr[((id16 - hp/Ep)/2).BC.Pqm.BC];
  addCheck["KS_exchange_kernelPlusPlus", zeroR[Kpp - 4 (1 + (m^2 - pdq)/(Ep Eq))]];
  addCheck["KS_exchange_kernelPlusMinus", zeroR[Kpm - 4 (1 - (m^2 - pdq)/(Ep Eq))] && zeroR[Kmm - Kpp]];
  ratio = Simplify[((Kpp /. {q0 -> p0, q1 -> p1, q2 -> p2, q3 -> p3, Eq -> Ep})/(Tr[BC.Pp])^2) /. Ep -> Sqrt[m^2 + p0^2 + p1^2 + p2^2 + p3^2]];
  addMeas["exchange_filledShellRatio", toStr[ratio]];
  addCheck["KS_exchange_filledShellOneEighth", ratio === 1/8];
  (* angular average of p.q over the 3-sphere vanishes: p^ = (cos psi, sin psi cos theta, sin psi sin theta cos phi, sin psi sin theta sin phi), q^ = (1,0,0,0) *)
  ang = Integrate[Cos[psi] Sin[psi]^2 Sin[theta], {psi, 0, Pi}, {theta, 0, Pi}, {phi, 0, 2 Pi}];
  addCheck["KS_exchange_angularAverageOfPdotQVanishes", ang === 0 && Integrate[Sin[psi]^2 Sin[theta], {psi, 0, Pi}, {theta, 0, Pi}, {phi, 0, 2 Pi}] === 2 Pi^2];
  (* block form of the exact Fock term: Tr(BC rho BC rho) = (1/2) sum_blocks (n^2 + s^2 - t^2 - c^2) for rho_block = (n + s sigma2 + t sigma3 + c sigma1)/2 *)
  rho2 = (nb id2 + sb sig2 + tb sig3 + cb0 sig1)/2;
  addCheck["KS_exchange_blockFormOfFockTerm", zeroR[Tr[sig2.rho2.sig2.rho2] - (nb^2 + sb^2 - tb^2 - cb0^2)/2] && zeroR[Tr[rho2] - nb] && zeroR[Tr[sig2.rho2] - sb] && zeroR[Tr[sig3.rho2] - tb] && zeroR[Tr[sig1.rho2] - cb0]];
  (* isotropic uniform gas: 8 blocks with n_beta = n/8, s_beta = S/8, t = c = 0: Tr(BC rho BC rho) = (n^2 + S^2)/16 *)
  addCheck["KS_exchange_uniformGasClosedForm", zeroR[8 ((n/8)^2 + (S/8)^2)/2 - (n^2 + S^2)/16] && zeroR[-(lam/2) (n^2 + S^2)/16 + (lam/32) (n^2 + S^2)]];
  (* kernel route: after angular averaging, integral integral f f K++ = 4[(int f)^2 + m^2 (int f/E)^2]; with antiparticles rho = rho_+ - rho_-: 4[(int(f+ - f-))^2 + m^2 (int (f+ + f-)/E)^2] = (n^2 + S^2)/16 *)
  addCheck["KS_exchange_antiparticleConvention", zeroR[4 ((fa - fb)^2 + (ga + gb)^2) - ((8 (fa - fb))^2 + (8 (ga + gb))^2)/16]];
  (* T = 0 closed forms in d = 4 spatial dimensions, degeneracy 8: n = 8 Vol(B^4(kF))/(2 pi)^4 *)
  nkF = 8 (Pi^2 kF^4/2)/(2 Pi)^4;
  SkF = 8 (2 Pi^2/(2 Pi)^4) Integrate[p^3 m/Sqrt[m^2 + p^2], {p, 0, kF}, Assumptions -> m > 0 && kF > 0];
  ekF = 8 (2 Pi^2/(2 Pi)^4) Integrate[p^3 Sqrt[m^2 + p^2], {p, 0, kF}, Assumptions -> m > 0 && kF > 0];
  addCheck["KS_exchange_T0_density", Simplify[nkF - kF^4/(4 Pi^2)] === 0];
  addCheck["KS_exchange_T0_scalarDensity", Simplify[SkF - (m/(3 Pi^2)) ((kF^2 - 2 m^2) Sqrt[m^2 + kF^2] + 2 m^3)] === 0];
  addCheck["KS_exchange_T0_kineticEnergyDensity", Simplify[ekF - (1/(15 Pi^2)) ((3 kF^2 - 2 m^2) (m^2 + kF^2)^(3/2) + 2 m^5)] === 0];
  addCheck["KS_exchange_T0_dSdn", Simplify[D[SkF, kF]/D[nkF, kF] - m/Sqrt[m^2 + kF^2]] === 0];
  exkF = -(lam/32) (nkF^2 + SkF^2);
  dex = D[exkF, kF]/D[nkF, kF];
  addCheck["KS_exchange_T0_vxTotalDerivative", Simplify[dex + (lam/16) (nkF + SkF m/Sqrt[m^2 + kF^2])] === 0];
  addCheck["KS_exchange_restGasLimit", Simplify[Limit[SkF/nkF, kF -> 0, Assumptions -> m > 0]] === 1 && Limit[exkF/((lam/2) SkF^2), kF -> 0, Assumptions -> m > 0 && lam > 0] === -1/8];
  (* nonrenormalisability: [Psi] = 7/2, [S^2] = 14, [lambda] = 8 - 14 = -6 *)
  addCheck["KS_exchange_couplingDimension", (8 - 1)/2 === 7/2 && 4 (7/2) === 14 && 8 - 14 === -6];
  $theory["exchange"] = <|
    "interaction" -> "U(S) = (lambda/2) S^2, S = Psibar Psi = Psi^dagger C Psi, normal ordered with respect to the free Dirac sea",
    "hartreeFock" -> <|"formula" -> "E_HF = (lambda/2) [ Tr(B C rho)^2 - Tr(B C rho B C rho) ] per unit volume for a one-body density matrix rho = sum_n f_n u_n u_n^dagger of Hilbert-normalised modes (expectation rule <Psi^dagger X Psi> = Tr(B X rho))",
      "derivation" -> "fermionic Wick theorem for the normal-ordered quartic: <:S^2:> = <S>^2 - (exchange); with the two-point function G_ab = <Psi_a^dagger Psi_b> = (rho B)_ba the exchange term is Tr(C G^T C G^T) = Tr(BC rho BC rho); verified exactly on a 4-mode Fock space for one-, two- and three-particle Slater determinants (KS_exchange_wickTheoremHF), where also <S^2> - <:S^2:> = Tr(M^2 rho)",
      "hartree" -> "E_H = (lambda/2) S_p^2 with S_p = Tr(BC rho) = e^{-6Hy} sum_n f_n chi_n^dagger (j sigma2) chi_n / l^3 (proper scalar density); mass shift M_H = lambda S_p",
      "exactFockLocal" -> "for the contact interaction the Fock term is exactly local in y: E_x^HF = -(lambda/2) integral dV_7 Tr(BC rho(y) BC rho(y)) = -(lambda/4) integral dV_7 sum_beta (n_beta^2 + s_beta^2 - t_beta^2 - c_beta^2), rho_beta = (n_beta + s_beta sigma2 + t_beta sigma3 + c_beta sigma1)/2 the 2x2 density matrix of block beta (n number, s scalar, t k-current, c y-current densities); c_beta = 0 for real-eps eigenstates; sum_beta t_beta = 0 over closed shells"|>,
    "filledShell" -> <|"statement" -> "8 positive-energy states at one momentum p (4 spatial components y, x1, x2, x3): Tr(BC P_+) = 8 m/E_p, Tr(BC P_+ BC P_+) = 8 m^2/E_p^2 = Tr(BC P_+)^2/8, hence E_x = -E_H/8", "ratio" -> "1/8"|>,
    "kernel" -> <|"definition" -> "K_{++}(p,q) = sum_{sigma sigma'} |u_{p sigma}^dagger B C u_{q sigma'}|^2 = Tr(P_+(p) BC P_+(q) BC), P_+(p) = (1 + h_p/E_p)/2, h_p = -i m gamma^4 - gamma^4 gamma^j p_j (j = y, 1, 2, 3), E_p = sqrt(m^2 + p^2)",
      "plusPlus" -> "K_{++}(p,q) = 4 [ 1 + (m^2 - p.q)/(E_p E_q) ]", "plusMinus" -> "K_{+-}(p,q) = Tr(P_+(p) BC P_-(q) BC) = 4 [ 1 - (m^2 - p.q)/(E_p E_q) ]", "minusMinus" -> "K_{--} = K_{++}",
      "numberKernel" -> "Tr(P_+(p) P_+(q)) = 4 [ 1 + (m^2 + p.q)/(E_p E_q) ]",
      "spinSummed" -> "the 'spin-summed |ubar_p u_q|^2' of the spec is this kernel with ubar u -> u^dagger B C u (expectation rule); it is an exact rational function of p, q, E_p, E_q"|>,
    "uniformGas" -> <|"setup" -> "8-fold degenerate relativistic gas in d = 4 spatial dimensions (y, x1, x2, x3), homogeneous in x5, x6, x7; densities per proper 7-volume; f_+(E) = 1/(e^{(E-mu)/T}+1) particles, f_-(E) = 1/(e^{(E+mu)/T}+1) antiparticles (holes of the sea, normal ordering)",
      "densities" -> <|"n" -> "n = 8 int d^4p/(2 pi)^4 (f_+ - f_-) = (1/pi^2) int_0^inf p^3 (f_+ - f_-) dp",
        "S" -> "S = 8 int d^4p/(2 pi)^4 (m/E_p)(f_+ + f_-) = (m/pi^2) int_0^inf p^3 (f_+ + f_-)/E_p dp",
        "eKin" -> "e_kin = (1/pi^2) int_0^inf p^3 E_p (f_+ + f_-) dp", "entropy" -> "s_ent = -(1/pi^2) int_0^inf p^3 sum_{+-} [f ln f + (1-f) ln(1-f)] dp"|>,
      "exchangeDoubleQuadrature" -> "e_x = -(lambda/2) integral integral d^4p d^4q/(2 pi)^8 [ f_+(p) f_+(q) K_{++} - 2 f_+(p) f_-(q) K_{+-} + f_-(p) f_-(q) K_{--} ]",
      "closedForm" -> "the p.q term averages to zero for isotropic occupations, so the double quadrature collapses EXACTLY: e_x(n, S) = -(lambda/32) (n^2 + S^2) for every T (and every isotropic occupation), n and S the vector and scalar densities above",
      "closedFormTex" -> "e_x=-\\frac{\\lambda}{32}\\bigl(n^2+S^2\\bigr),\\qquad e_H=\\frac{\\lambda}{2}S^2",
      "vectorScalarDecomposition" -> "e_x = e_x^{(v)} + e_x^{(s)}, e_x^{(v)} = -(lambda/32) n^2 (from Tr(P_+ P_+)-type overlaps), e_x^{(s)} = -(lambda/32) S^2",
      "restGas" -> "k_F -> 0: S = n, e_x = -(lambda/16) n^2 = -e_H/8 (filled-shell result)",
      "T0" -> <|"n" -> "n = k_F^4/(4 pi^2)", "S" -> "S = (m/(3 pi^2)) [ (k_F^2 - 2 m^2) sqrt(m^2 + k_F^2) + 2 m^3 ]",
        "eKin" -> "e_kin = (1/(15 pi^2)) [ (3 k_F^2 - 2 m^2)(m^2 + k_F^2)^{3/2} + 2 m^5 ]", "dSdn" -> "dS/dn = m/E_F, E_F = sqrt(m^2 + k_F^2)",
        "ex" -> "e_x(n, 0) = -(lambda/32) [ n^2 + S(k_F(n))^2 ], k_F = (4 pi^2 n)^{1/4}",
        "vxTotal" -> "de_x/dn |_{T=0} = -(lambda/16) [ n + S m/E_F ]"|>,
      "ldaPotentials" -> <|"v_v" -> "v_v = partial e_x/partial n |_S = -(lambda/16) n (potential-type, vector)", "v_s" -> "v_s = partial e_x/partial S |_n = -(lambda/16) S (mass-type, scalar)",
        "v_x_nOnly" -> "v_x = d e_x(n,T)/dn |_T = -(lambda/16) [ n + S_u(n,T) dS_u/dn ] with S_u the uniform-gas scalar density at (n, T) (T = 0: dS_u/dn = m/E_F)"|>|>,
    "ksEquationUsed" -> <|
      "VS" -> "KS-VS (the theory's equation; exact-HF-derived local pair): Meff(y) = m + lambda S_p(y) + v_s(y), v_v(y) = -(lambda/16) n_p(y), v_s(y) = -(lambda/16) S_p(y); gamma^0 chi' + i kappa k gamma^1 chi - i (eps - v_v(y)) gamma^4 chi = Meff(y) chi; the T-dependence enters only through the occupations",
      "V" -> "KS-V (STAGE4_SPEC recommendation): Meff(y) = m + lambda S_p(y) (exact Hartree mass shift only), v_x(y) = d e_x(n,T)/dn at (n_p(y), T) (n-only LDA with the uniform-gas S_u(n,T)), eps -> eps - v_x(y)",
      "exactHF" -> "exact-HF option for checks: matrix potential V_x(y) = -lambda BC rho(y) BC (block form -lambda sigma2 rho_beta sigma2) added to h; differs from KS-VS by the t_beta^2 terms and by block-resolved densities",
      "pseudoPotential" -> "the 'Kohn-Sham fermion-gas thermodynamics pseudo-potential' is the local pair (Meff(y), v_v(y)) built from the uniform-gas HF thermodynamics (Mermin functional F = E_KS - T S_ent + E_H + E_x^{LDA}) plus the gravitational terms (3H gamma^0 absorbed by W^{-3}, kappa(y) k gamma^1, the boundary conditions)",
      "noCorrelation" -> "no correlation term: [lambda] = mass^{-6} in 8D ([Psi] = 7/2), the contact interaction beyond Hartree-Fock is not renormalisable; the dimensionless coupling is lambda-hat = lambda m^6"|>|>;];

(* ================================================================== *)
(* 7. KS_functional                                                    *)
(* ================================================================== *)

(* Discretised model: Ny grid points with flat weight Delta y = 1, density conversion c_i = e^{-6 H y_i}/l^3,
   volume weight w_i = 1/c_i (so w_i c_i = 1); No orbitals in one block (j = +1, BC = sigma2);
   h0 = arbitrary Hermitian 2Ny x 2Ny matrix (kinetic + kappa k sigma3 part) + m (sigma2 on every point). *)
checkFunctional[] := Module[{Ny = 2, No = 2, dim, chiS, chbS, hKin, h0, fS, cS, wS, nI, SI, EH, EX, SE, Fm, lagr, vvI, vsI, MeffI, hKS, ok, okF, okE, okHF, okT, okM, epsExp, idx, sig2big, Ssum},
  dim = 2 Ny;
  idx[n_, i_, a_] := 2 (i - 1) + a; (* component a = 1,2 of point i *)
  chiS = Table[x[n, p], {n, No}, {p, dim}]; chbS = Table[xb[n, p], {n, No}, {p, dim}];
  hKin = Table[If[p <= q, hh[p, q], Conjugate[hh[q, p]]], {p, dim}, {q, dim}] /. Conjugate[hh[a_, b_]] :> hb[a, b];
  (* hh[p,p] real: replace hb[p,p] -> hh[p,p]; hb[a,b] plays the role of the conjugate of hh[a,b] *)
  hKin = hKin /. hb[a_, a_] :> hh[a, a];
  sig2big = ArrayFlatten[Table[If[i == l, sig2, ConstantArray[0, {2, 2}]], {i, Ny}, {l, Ny}]];
  h0 = hKin + m sig2big;
  fS = Table[f[n], {n, No}]; cS = Table[c[i], {i, Ny}]; wS = Table[1/c[i], {i, Ny}];
  nI = Table[cS[[i]] Sum[fS[[n]] (chbS[[n, idx[n, i, 1]]] chiS[[n, idx[n, i, 1]]] + chbS[[n, idx[n, i, 2]]] chiS[[n, idx[n, i, 2]]]), {n, No}], {i, Ny}];
  SI = Table[cS[[i]] Sum[fS[[n]] ({chbS[[n, idx[n, i, 1]]], chbS[[n, idx[n, i, 2]]]}.sig2.{chiS[[n, idx[n, i, 1]]], chiS[[n, idx[n, i, 2]]]}), {n, No}], {i, Ny}];
  EH = (lam/2) Sum[wS[[i]] SI[[i]]^2, {i, Ny}];
  EX = -(lam/32) Sum[wS[[i]] (nI[[i]]^2 + SI[[i]]^2), {i, Ny}];
  SE = -Sum[fS[[n]] Log[fS[[n]]] + (1 - fS[[n]]) Log[1 - fS[[n]]], {n, No}];
  Fm = Sum[fS[[n]] chbS[[n]].h0.chiS[[n]], {n, No}] - TT SE + EH + EX;
  lagr = Fm - Sum[ep[n] fS[[n]] (chbS[[n]].chiS[[n]] - 1), {n, No}] - mu (Sum[fS[[n]], {n, No}] - NN);
  vvI = -(lam/16) nI; vsI = -(lam/16) SI; MeffI = m + lam SI + vsI;
  (* KS operator on orbital n: (hKin + Meff_i sigma2 + vv_i) chi_n  -- pointwise potentials *)
  hKS = hKin + ArrayFlatten[Table[If[i == l, MeffI[[i]] sig2 + vvI[[i]] id2, ConstantArray[0, {2, 2}]], {i, Ny}, {l, Ny}]];
  (* stationarity w.r.t. chi_n^*: d lagr / d xb[n,p] = f_n [ (hKS chi_n)_p - ep_n chi_n,p ] *)
  ok = AllTrue[Flatten[Table[Together[D[lagr, xb[n, p]] - fS[[n]] ((hKS.chiS[[n]])[[p]] - ep[n] chiS[[n, p]])] === 0, {n, No}, {p, dim}]], TrueQ];
  addCheck["KS_functional_stationarityGivesKSEquation", ok];
  (* stationarity w.r.t. chi_n: the conjugate equation *)
  addCheck["KS_functional_stationarityConjugate", AllTrue[Flatten[Table[Together[D[lagr, x[n, p]] - fS[[n]] ((chbS[[n]].hKS)[[p]] - ep[n] chbS[[n, p]])] === 0, {n, No}, {p, dim}]], TrueQ]];
  (* stationarity w.r.t. f_n: chi_n^dagger hKS chi_n - ep_n (norm - 1) + T ln(f/(1-f)) - mu = 0 -> on the KS solution eps_n + T ln(f/(1-f)) = mu *)
  okF = AllTrue[Range[No], Together[D[lagr, f[#]] - (chbS[[#]].hKS.chiS[[#]] + TT (Log[f[#]] - Log[1 - f[#]]) - ep[#] (chbS[[#]].chiS[[#]] - 1) - mu)] === 0 &];
  (* f = 1/(e^{(eps-mu)/T}+1) solves eps + T (ln f - ln(1-f)) = mu; ln(f/(1-f)) = -(eps-mu)/T; the map f -> ln(f/(1-f)) is injective on (0,1) *)
  addCheck["KS_functional_fermiDiracOccupations", okF &&
    Simplify[PowerExpand[((ep0 + TT (Log[ff] - Log[1 - ff]) - mu) /. ff -> 1/(E^((ep0 - mu)/TT) + 1)) /. Log[a_] :> Log[Together[a]]]] === 0 &&
    Simplify[D[Log[ff] - Log[1 - ff], ff] > 0, 0 < ff < 1] === True];
  (* total energy: E = sum f <h0> + EH + EX = sum f eps - EH - EX with eps_n := <chi_n|hKS|chi_n> (polynomial identity) *)
  epsExp = Table[chbS[[n]].hKS.chiS[[n]], {n, No}];
  okE = Together[(Sum[fS[[n]] chbS[[n]].h0.chiS[[n]], {n, No}] + EH + EX) - (Sum[fS[[n]] epsExp[[n]], {n, No}] - EH - EX)] === 0;
  addCheck["KS_functional_totalEnergyDoubleCounting", okE];
  (* Hellmann-Feynman identities (explicit parameter derivatives of F at fixed orbitals and occupations) *)
  okHF = Together[D[Fm, lam] - (EH + EX)/lam] === 0;
  okT = Together[D[Fm, TT] + SE] === 0;
  okM = Together[D[Fm, m] - Sum[fS[[n]] chbS[[n]].sig2big.chiS[[n]], {n, No}]] === 0;
  addCheck["KS_functional_hellmannFeynmanLambda", okHF];
  addCheck["KS_functional_hellmannFeynmanTemperature", okT];
  addCheck["KS_functional_hellmannFeynmanMass", okM && Together[Sum[fS[[n]] chbS[[n]].sig2big.chiS[[n]], {n, No}] - Sum[wS[[i]] SI[[i]], {i, Ny}]] === 0];
  (* Mermin: F = E - T S_ent with E the internal energy; C_V = T dS/dT *)
  addCheck["KS_functional_merminStructure", Together[Fm - (Sum[fS[[n]] chbS[[n]].h0.chiS[[n]], {n, No}] + EH + EX - TT SE)] === 0];
  (* the V-only variant: functional with e_x(n) = -(lambda/32)(n^2 + Su(n)^2) gives v_x = e_x'(n) and no scalar term *)
  addCheck["KS_functional_variantV", Module[{EXv, lv, vx},
     EXv = -(lam/32) Sum[wS[[i]] (nI[[i]]^2 + Su[nI[[i]]]^2), {i, Ny}];
     lv = Sum[fS[[n]] chbS[[n]].h0.chiS[[n]], {n, No}] + EH + EXv - Sum[ep[n] fS[[n]] (chbS[[n]].chiS[[n]] - 1), {n, No}];
     vx = -(lam/16) (nI + Su /@ nI Su' /@ nI);
     AllTrue[Flatten[Table[Together[D[lv, xb[n, p]] - fS[[n]] (((hKin + ArrayFlatten[Table[If[i == l, (m + lam SI[[i]]) sig2 + vx[[i]] id2, ConstantArray[0, {2, 2}]], {i, Ny}, {l, Ny}]]).chiS[[n]])[[p]] - ep[n] chiS[[n, p]])] === 0, {n, No}, {p, dim}]], TrueQ]]];
  $theory["functional"] = <|
    "definition" -> "F[{chi_n}, {f_n}] = sum_n f_n <chi_n| h_0 |chi_n> - T S_ent[f] + E_H[S_p] + E_x[n_p, S_p], h_0 = j[-i sigma1 d/dy + m sigma2 + kappa(y) k sigma3] (block j, momentum k), S_ent = -sum_n [f_n ln f_n + (1 - f_n) ln(1 - f_n)], E_H = (lambda/2) integral dV_7 S_p^2, E_x = -(lambda/32) integral dV_7 (n_p^2 + S_p^2), dV_7 = e^{6Hy} l^3 dy (per unit extra-time coordinate volume), n_p = e^{-6Hy} sum_n f_n chi_n^dagger chi_n / l^3, S_p = e^{-6Hy} sum_n f_n chi_n^dagger (j sigma2) chi_n / l^3; constraints integral chi_n^dagger chi_n dy = 1 (multipliers eps_n), sum_n f_n = N (multiplier mu)",
    "stationarity" -> <|"orbitals" -> "delta F/delta chi_n^dagger = 0: [ h_0 + (lambda S_p + v_s)(j sigma2) + v_v ] chi_n = eps_n chi_n, i.e. j[-i sigma1 d/dy + Meff sigma2 + kappa k sigma3] chi_n + v_v chi_n = eps_n chi_n with Meff = m + lambda S_p + v_s, v_s = -(lambda/16) S_p, v_v = -(lambda/16) n_p (the e^{-6Hy} of the densities cancels the e^{6Hy} of dV_7: the equation is local with the flat y-measure)",
      "occupations" -> "partial F/partial f_n = eps_n + T ln(f_n/(1-f_n)) - mu = 0: f_n = 1/(exp((eps_n - mu)/T) + 1) (Fermi-Dirac), mu fixed by sum f_n = N",
      "firstOrderForm" -> "gamma^0 chi' + i kappa k gamma^1 chi - i (eps - v_v) gamma^4 chi = Meff chi, in the 2x2 block chi' = [Meff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1] chi"|>,
    "totalEnergy" -> "E = sum_n f_n <h_0>_n + E_H + E_x = sum_n f_n eps_n - E_H - E_x (double-counting correction); F = E - T S_ent; C_V = dE/dT",
    "hellmannFeynman" -> <|"lambda" -> "dF/d lambda = (E_H + E_x)/lambda = integral dV_7 [ S_p^2/2 - (n_p^2 + S_p^2)/32 ] at the self-consistent densities (envelope theorem: the implicit dependence through chi_n, f_n drops out at stationarity)",
      "mass" -> "dF/dm = integral dV_7 S_p = sum_n f_n integral chi_n^dagger (j sigma2) chi_n dy",
      "temperature" -> "dF/dT = -S_ent (Mermin)",
      "momentum" -> "d eps_n/dk = j integral kappa(y) chi_n^dagger sigma3 chi_n dy = l^3 integral e^{6Hy} kappa(y) t_n(y) dy at fixed potentials (first-order perturbation theory in the self-adjoint problem)",
      "numericalUse" -> "finite differences of the self-consistent F in lambda, m, T and of eps_n in k must reproduce these expectation values; together with N conservation (sum f_n = N), current conservation (chi^dagger A4 chi = 0 identically) and the double-counting identity they are the stationarity checks"|>,
    "variantV" -> "with E_x = integral dV_7 e_x(n_p, T) (n-only LDA, e_x = -(lambda/32)(n^2 + S_u(n,T)^2)) the stationarity gives Meff = m + lambda S_p (no scalar exchange term) and v_x = d e_x/dn = -(lambda/16)[n_p + S_u dS_u/dn] (verified symbolically with an abstract S_u)"|>;];

(* ================================================================== *)
(* 8. KS_emt                                                           *)
(* ================================================================== *)

(* Stage-2 energy-momentum tensor (lower indices) for a field psi with Psi^dagger -> psid (a row vector);
   one-body part only (U is added by hand as the HF value). *)
emtLower[psi_, psid_, mval_] := Module[{psibar, Dp, Db, Ls, T},
  psibar = psid.C16;
  Dp = Table[d1[mu, psi] + OmF[[mu]].psi, {mu, 8}];
  Db = Table[d1[mu, psibar] - psibar.OmF[[mu]], {mu, 8}];
  Ls = (1/2) Sum[psibar.gUF[[mu]].Dp[[mu]] - Db[[mu]].gUF[[mu]].psi, {mu, 8}] - mval psibar.psi;
  T = Table[-(1/4) (psibar.gDF[[mu]].Dp[[nu]] + psibar.gDF[[nu]].Dp[[mu]] - Db[[mu]].gDF[[nu]].psi - Db[[nu]].gDF[[mu]].psi) + gF[[mu, nu]] Ls, {mu, 8}, {nu, 8}];
  <|"T" -> T, "Ls" -> Ls, "psibar" -> psibar, "Dp" -> Dp, "Db" -> Db|>];

(* matrix X of a bilinear expression sum_ab cb[a] X_ab ch[b] (no derivatives left) *)
bilinearMatrix[expr_] := Table[D[expr, cb[a][y], ch[b][y]], {a, 0, 15}, {b, 0, 15}];

checkEMT[] := Module[{chi, chib, uvec, ubvec, Psi, Psid, e8, onRules, Tm, X, labels, paulis, basis32, decomp, coef, resid, tab, ok, nzA, A, rhoOne, pyOne, p1One, ptOne, tr, trOne, avg, LsOne, ubBC, ubT, ubJ, ubN, ph, wv6},
  (* the KS orbital: Psi = e^{-i eps x4} e^{i k x1} e^{-3Hy} u(y), Psi^dagger -> (ub) B e^{...} (expectation rule) *)
  chi = Table[ch[n][y], {n, 0, 15}]; chib = Table[cb[n][y], {n, 0, 15}];
  Psi = E^(-I eps x4) E^(I kk x1) E^(-3 H y) chi;
  Psid = E^(I eps x4) E^(-I kk x1) E^(-3 H y) (chib.Bm);
  e8 = emtLower[Psi, Psid, m];
  A = Table[gDF[[mu]].OmF[[nu]] + OmF[[nu]].gDF[[mu]] + gDF[[nu]].OmF[[mu]] + OmF[[mu]].gDF[[nu]], {mu, 8}, {nu, 8}];
  nzA = Select[Select[Tuples[Range[8], 2], #[[1]] <= #[[2]] &], ! zeroMatQ[A[[#[[1]], #[[2]]]]] &];
  addMeas["emt_anticommutatorNonzeroPairs", ToString[(# - 1) & /@ nzA]];
  addCheck["KS_emt_staticAnticommutators", Sort[nzA] === Sort[{{2, 5}, {3, 5}, {4, 5}, {5, 6}, {5, 7}, {5, 8}}] &&
    AllTrue[{2, 3, 4}, zeroMatQ[A[[#, 5]] - H Wf E^a4c G[0].G[# - 1].G[4]] &] && AllTrue[{6, 7, 8}, zeroMatQ[A[[5, #]] - H Wf E^(-a4c) G[0].G[4].G[# - 1]] &]];
  (* on-shell rules: u' = N u, ub' = ub N^dagger *)
  onRules = Join[Table[Derivative[1][ch[n]][y] -> (Nfull.chi)[[n + 1]], {n, 0, 15}], Table[Derivative[1][cb[n]][y] -> (chib.hermR[Nfull])[[n + 1]], {n, 0, 15}]];
  (* mixed components T^mu_nu = g^{mu mu} T_{mu nu}, times e^{6Hy} (the proper-density factor), on shell *)
  wv6 = E^(6 H y);
  Tm = Table[Expand[wv6 giF[[mu, mu]] e8["T"][[mu, nu]] /. onRules], {mu, 8}, {nu, 8}];
  addCheck["KS_emt_phasesCancel", AllTrue[Flatten[Tm], FreeQ[#, x4 | x1] &]];
  X = Table[bilinearMatrix[Tm[[mu, nu]]], {mu, 8}, {nu, 8}];
  addCheck["KS_emt_bilinearExtractionExact", AllTrue[Flatten[Table[zeroQ[Tm[[mu, nu]] - chib.X[[mu, nu]].chi], {mu, 8}, {nu, 8}]], TrueQ]];
  (* 32-element trace-orthogonal basis of the block-diagonal matrices: labels x Paulis *)
  labels = {id16, Jop, I K1op, I K2op, I Jop.K1op, I Jop.K2op, -K1op.K2op, Jop.K1op.K2op};
  paulis = {id16, Jop.A4, Jop.BC, -Jop.G[4].G[1]};
  addCheck["KS_emt_blockBasisOrthogonal", AllTrue[labels, herm[#] === # && #.# === id16 &] && AllTrue[paulis, herm[#] === # && #.# === id16 &] &&
    diagBlocks[paulis[[2]]] === ConstantArray[sig1, 8] && diagBlocks[paulis[[3]]] === ConstantArray[sig2, 8] && diagBlocks[paulis[[4]]] === ConstantArray[sig3, 8]];
  basis32 = Flatten[Table[l.p, {l, labels}, {p, paulis}], 1];
  addCheck["KS_emt_basis32TraceOrthogonal", AllTrue[Flatten[Table[Tr[basis32[[i]].basis32[[j]]] === If[i == j, 16, 0], {i, 32}, {j, 32}]], TrueQ]];
  decomp[Xm_] := Module[{cs = Table[Together[Tr[Xm.b]/16], {b, basis32}], rem},
    rem = Xm - Sum[cs[[i]] basis32[[i]], {i, 32}];
    <|"coefficients" -> cs, "blockDiagonal" -> zeroMatQ[rem]|>];
  tab = Table[decomp[X[[mu, nu]]], {mu, 8}, {nu, 8}];
  (* which components are block diagonal (nonzero on single-block orbitals) *)
  addCheck["KS_emt_offBlockComponentsVanishPerOrbital", AllTrue[Flatten[Table[If[MemberQ[{{1, 1}, {1, 5}, {5, 1}, {5, 5}, {1, 2}, {2, 1}, {2, 2}, {2, 5}, {5, 2}, {3, 3}, {4, 4}, {6, 6}, {7, 7}, {8, 8}}, {mu, nu}], True, ! tab[[mu, nu, "blockDiagonal"]] || zeroMatQ[X[[mu, nu]]]], {mu, 8}, {nu, 8}]], TrueQ]];
  addCheck["KS_emt_diagonalAndY1Y4X1ComponentsBlockDiagonal", AllTrue[{{1, 1}, {1, 5}, {5, 5}, {1, 2}, {2, 2}, {2, 5}, {3, 3}, {4, 4}, {6, 6}, {7, 7}, {8, 8}}, tab[[#[[1]], #[[2]], "blockDiagonal"]] &]];
  (* the diagonal components are combinations of the four physical densities only: 1 (n), J sigma1 = A4 (c), J sigma2 = BC (s), J sigma3 = -gamma^4 gamma^1 (t):
     basis32 index = 4 (label - 1) + pauli, physical set {1, 6, 7, 8} *)
  addCheck["KS_emt_diagonalComponentsPhysicalDensitiesOnly", AllTrue[{1, 2, 3, 4, 5, 6, 7, 8}, Function[mu, AllTrue[Delete[Range[32], {{1}, {6}, {7}, {8}}], zeroQ[tab[[mu, mu, "coefficients"]][[#]]] &]]]];
  (* per-orbital densities (times e^{6Hy} l^3): n = ub.u, s = ub.BC.u, t = ub.(-g4 g1).u, c = ub.A4.u *)
  ubN = chib.chi; ubBC = chib.BC.chi; ubT = chib.(-G[4].G[1]).chi; ubJ = chib.A4.chi;
  rhoOne = eps ubN - (Meff[y] - m) ubBC - vv[y] ubN;
  pyOne = eps ubN - m ubBC - E^(-H y - a4c) kk ubT;
  p1One = E^(-H y - a4c) kk ubT + (Meff[y] - m) ubBC + vv[y] ubN;
  ptOne = (Meff[y] - m) ubBC + vv[y] ubN;
  addCheck["KS_emt_rho", zeroQ[-Tm[[5, 5]] - rhoOne]];       (* T^4_4 = -rho *)
  addCheck["KS_emt_py", zeroQ[Tm[[1, 1]] - pyOne]];
  addCheck["KS_emt_p1", zeroQ[Tm[[2, 2]] - p1One]];
  addCheck["KS_emt_p2p3", zeroQ[Tm[[3, 3]] - ptOne] && zeroQ[Tm[[4, 4]] - ptOne]];
  addCheck["KS_emt_pt", AllTrue[{6, 7, 8}, zeroQ[Tm[[#, #]] - ptOne] &]];
  (* off-diagonal: T^y_4 and T^y_1 are proportional to the y-current; T^4_1 has the three block-diagonal pieces *)
  addCheck["KS_emt_Ty4ProportionalToCurrent", zeroQ[Tm[[1, 5]] - (2 eps - vv[y]) ubJ] || zeroQ[Tm[[1, 5]] - Tr[X[[1, 5]].A4]/16 ubJ]];
  addCheck["KS_emt_Ty1ProportionalToCurrent", zeroQ[Tm[[1, 2]] - Tr[X[[1, 2]].A4]/16 ubJ]];
  addMeas["emt_Ty4_coefficientOfCurrent", toStr[Together[Tr[X[[1, 5]].A4]/16]]];
  addMeas["emt_Ty1_coefficientOfCurrent", toStr[Together[Tr[X[[1, 2]].A4]/16]]];
  addMeas["emt_T41_coefficients_n_s_t_js", toStr[Together /@ {Tr[X[[5, 2]]]/16, Tr[X[[5, 2]].BC]/16, Tr[X[[5, 2]].(-G[4].G[1])]/16, Tr[X[[5, 2]].(Jop.BC)]/16}]];
  (* T^4_1 = c_n n + c_s s + c_t t + c_js (u^dagger J BC u), J BC = sigma2 in every block (= j s per block) *)
  addCheck["KS_emt_T41form", zeroQ[Tm[[5, 2]] - (Tr[X[[5, 2]]]/16 ubN + Tr[X[[5, 2]].BC]/16 ubBC + Tr[X[[5, 2]].(-G[4].G[1])]/16 ubT + Tr[X[[5, 2]].(Jop.BC)]/16 chib.(Jop.BC).chi)]];
  (* the closed-shell cancellation of T^4_1: under (k, j) -> (-k, -j) with chi -> sigma3 chi the n-term flips with k, the s- and t-terms flip sign *)
  addCheck["KS_emt_T41cancelsOverShell", Module[{cn = Together[Tr[X[[5, 2]]]/16], cs = Together[Tr[X[[5, 2]].BC]/16], ct = Together[Tr[X[[5, 2]].(-G[4].G[1])]/16], cjs = Together[Tr[X[[5, 2]].(Jop.BC)]/16]},
     zeroQ[cn + (cn /. kk -> -kk)] && zeroQ[cs - (cs /. kk -> -kk)] && zeroQ[ct - (ct /. kk -> -kk)] && zeroQ[cjs - (cjs /. kk -> -kk)] && zeroQ[cs] && ! zeroQ[cjs] &&
      (* s = chi^dagger (j sigma2) chi and t = chi^dagger (j sigma3) chi flip under chi -> sigma3 chi, j -> -j: s -> (-j) chi^dagger sigma3 sigma2 sigma3 chi = s; t -> (-j) chi^dagger sigma3 sigma3 sigma3 chi = -t *)
      sig3.sig2.sig3 === -sig2 && sig3.sig3.sig3 === sig3]];
  (* symmetry of T_{mu nu} and the trace *)
  addCheck["KS_emt_symmetric", AllTrue[Flatten[Table[zeroQ[e8["T"][[mu, nu]] - e8["T"][[nu, mu]]], {mu, 8}, {nu, 8}]], TrueQ]];
  trOne = Sum[Tm[[mu, mu]], {mu, 8}];
  addCheck["KS_emt_trace", zeroQ[trOne - (-m ubBC + 7 (Meff[y] - m) ubBC + 7 vv[y] ubN)]];
  (* rho = eps n - Ls^(1), Ls^(1) = (Meff - m) s + vv n (one-body on-shell Lagrangian density) *)
  LsOne = Expand[wv6 e8["Ls"] /. onRules];
  addCheck["KS_emt_onShellLagrangian", zeroQ[LsOne - ((Meff[y] - m) ubBC + vv[y] ubN)]];
  (* homogeneous rest-state sanity: k = 0, eps = Meff = m, vv = 0, s = n  ->  rho = m n, p = 0 *)
  addCheck["KS_emt_restStateDustExplicit", Module[{nn0 = 1, ss0 = 1}, Together[(eps nn0 - (Mv - m) ss0 - 0) /. {eps -> Mv}] === m && Together[(Mv nn0 - m ss0 - 0) - (Mv - m)] === 0]];
  (* parity of the densities under P_A (gamma^0) and P_B (i gamma^0 gamma^8) *)
  addCheck["KS_emt_densityParityTable", A0.Bm.Bm.A0 === id16 && A0.BC.A0 === -BC && A0.(-G[4].G[1]).A0 === -G[4].G[1] && A0.A4.A0 === -A4 &&
    (I G[0].g8).BC.(I G[0].g8) === BC && (I G[0].g8).(-G[4].G[1]).(I G[0].g8) === -G[4].G[1] && (I G[0].g8).A4.(I G[0].g8) === -A4];
  $theory["emt"] = <|
    "definition" -> "T_{mu nu} = -(1/4)[ Psibar gamma_mu D_nu Psi + Psibar gamma_nu D_mu Psi - (D_mu Psibar) gamma_nu Psi - (D_nu Psibar) gamma_mu Psi ] + g_{mu nu} L_s (Stage 2), evaluated on the KS orbital Psi = e^{-i eps x4} e^{i k x1} e^{-3Hy} u(y) with the expectation rule Psi^dagger -> u^dagger B; every bilinear is multiplied by e^{-6Hy}/l^3 (proper densities); the interaction enters through L_s = ... - U with <U> = e_H + e_x",
    "staticConnectionTerms" -> "with a_4 constant only A_{i4} = H e^{Hy+a_4} gamma^0 gamma^i gamma^4 (i = 1,2,3) and A_{4j} = H e^{Hy-a_4} gamma^0 gamma^4 gamma^j (j = 5,6,7) are nonzero (six of the Stage-2 21)",
    "perOrbitalDensities" -> "n = e^{-6Hy} u^dagger u / l^3, s = e^{-6Hy} u^dagger BC u / l^3, t = e^{-6Hy} u^dagger (-gamma^4 gamma^1) u / l^3, c = e^{-6Hy} u^dagger A4 u / l^3 (= 0 for eigenstates); in the block: n = |chi|^2, s = j chi^dagger sigma2 chi, t = j chi^dagger sigma3 chi, c = j chi^dagger sigma1 chi (times e^{-6Hy}/l^3)",
    "oneBody" -> <|"rho" -> "rho^(1) = eps n - (Meff - m) s - v_v n", "p_y" -> "p_y^(1) = T^y_y = eps n - m s - kappa k t",
      "p_1" -> "p_(1)^(1) = kappa k t + (Meff - m) s + v_v n (direction of k)", "p_2p_3" -> "p_(2)^(1) = p_(3)^(1) = (Meff - m) s + v_v n",
      "p_t" -> "p_(5,6,7)^(1) = (Meff - m) s + v_v n (extra times)", "Ls" -> "L_s^(1) = (Meff - m) s + v_v n (on shell, one body)",
      "trace" -> "T^mu_mu^(1) = -m s + 7 (Meff - m) s + 7 v_v n",
      "offDiagonal" -> <|"T_y4" -> "proportional to the y-current c (coefficient " <> $meas["emt_Ty4_coefficientOfCurrent"] <> "): vanishes for eigenstates",
        "T_y1" -> "proportional to the y-current c (coefficient " <> $meas["emt_Ty1_coefficientOfCurrent"] <> "): vanishes for eigenstates",
        "T_41" -> "T^4_1 = c_n n + c_s s + c_t t + c_js (j s) with (c_n, c_s, c_t, c_js) = " <> $meas["emt_T41_coefficients_n_s_t_js"] <> " (j s = e^{-6Hy} chi^dagger sigma2 chi / l^3; the last term comes from the connection term A_{14} = H e^{Hy+a_4} gamma^0 gamma^1 gamma^4); c_n is odd in k, c_t and c_js even, c_s = 0; under the block map (k, j) -> (-k, -j), chi -> sigma3 chi (same eps, same |chi|^2) t and j s flip sign, so T^4_1 cancels over every closed shell {k, -k} x 8 blocks",
        "others" -> "T_{y2}, T_{y3}, T_{yj}, T_{42}, T_{43}, T_{4j}, T_{12}, T_{13}, T_{1j}, T_{23}, T_{ij'} (i != j') vanish for every single-block orbital: their matrices have no diagonal 2x2 block (they contain gamma^2, gamma^3, gamma^5, gamma^6, gamma^7)"|>|>,
    "interactionPart" -> "<U> = e_H + e_x = (lambda/2) S_p^2 - (lambda/32)(n_p^2 + S_p^2) (KS-VS); it enters rho with +<U> and every p_(i) with -<U> for all seven transverse directions",
    "ksState" -> <|"rho" -> "rho(y) = sum_n f_n [ eps_n n_n - (Meff - m) s_n - v_v n_n ] + e_H + e_x = sum_n f_n (eps_n - v_v) n_n - (lambda/2) S_p^2 - v_s S_p + e_x",
      "p_y" -> "p_y(y) = sum_n f_n [ eps_n n_n - m s_n - kappa k_n t_n ] - e_H - e_x",
      "p_3" -> "p_3(y) = (1/3) sum_i p_(i) = sum_n f_n [ (1/3) kappa k_n t_n + (Meff - m) s_n + v_v n_n ] - e_H - e_x (rotational average over the shell)",
      "p_t" -> "p_t(y) = sum_n f_n [ (Meff - m) s_n + v_v n_n ] - e_H - e_x",
      "densities" -> "n_p = sum f_n n_n, S_p = sum f_n s_n; the k-current sum sum_n f_n k_n t_n is even in k and does not cancel; sum_n f_n t_n = 0 over closed shells"|>,
    "properVolumeAverage" -> "<X> = integral_{-L}^0 X(y) e^{6Hy} dy / integral_{-L}^0 e^{6Hy} dy, integral_{-L}^0 e^{6Hy} dy = (1 - e^{-6HL})/(6H); brane-localised fraction of the number density: integral_{-delta}^0 n_p e^{6Hy} dy / integral_{-L}^0 n_p e^{6Hy} dy",
    "Z2parity" -> <|"P_A" -> "n even, s odd, t even, c odd; rho even, p_y even, p_(i) even (the mirror universe with mass -m carries the same rho and p); the Hartree shift lambda S_p is odd like the bare mass function",
      "P_B" -> "n even, s even, t even, c odd",
      "sectors" -> "even-parity orbitals (chi_2(0) = 0) carry n(0) = |chi_1(0)|^2 on the brane and s(0) = t(0) = 0 there; odd-parity orbitals (chi_1(0) = 0) carry n(0) = |chi_2(0)|^2 and s(0) = t(0) = 0: on the brane itself only the number density is nonzero for either parity"|>,
    "comparison" -> "the field requires rho_req = -21 H^2/kappa < 0 and p_req = +15 H^2/kappa; the KS state has rho = sum f eps n + ... >= 0 for positive-energy occupations with eps > v_v and repulsive/weak coupling: the mismatch is at least |rho_req| + rho_KS; the numerics report the proper-volume averages <rho>, <p_y>, <p_3>, <p_t> and the ratios to the required source"|>;];

(* ================================================================== *)
(* 9. entry point                                                      *)
(* ================================================================== *)

D16KSRun[repoRoot_String] := Module[{fixFile, res, t0 = AbsoluteTime[], step},
  $checks = <||>; $meas = <||>; $theory = <||>;
  fixFile = FileNameJoin[{repoRoot, "artifacts", "dirac16complex", "arbitrary-field", "algebra-fixture.json"}];
  step[name_, body_] := (logT[name]; body);
  SetAttributes[step, HoldRest];
  $theory["conventions"] = <|
    "coordinates" -> "x0..x7 zero-based; proper hidden-space coordinate y = ln(sin z)/(6H) <= 0, z = 6 H x0; x4 = time; (x1,x2,x3) 3-space; (x5,x6,x7) extra times",
    "frame" -> "eta = diag(+1,+1,+1,+1,-1,-1,-1,-1); gamma^a = [[0, taubar_a],[tau_a, 0]] (notebook split-octonion basis, algebra-fixture.json); C = gamma^0 gamma^1 gamma^2 gamma^3; B = -i C gamma^4; BC = -i gamma^4; chirality gamma^8 = gamma^0...gamma^7",
    "expectationRule" -> "<Psi^dagger M Psi> = u^dagger B M u for a Hilbert-normalised one-particle mode u (NUMERICS_CONTRACT); number density u^dagger u, scalar density u^dagger B C u, y-current u^dagger gamma^0 gamma^4 u, k-current u^dagger (-gamma^4 gamma^1) u",
    "units" -> "H = 1 in the numerics; m/H, lambda-hat = lambda m^6, T/m dimensionless",
    "symbols" -> "eps = single-particle energy (x4-frequency), k = 3-momentum along x1, kappa(y) = e^{-Hy-a_4}, Meff = m + lambda S_p (+ v_s), v_v = vector exchange potential, n_p / S_p proper number / scalar densities, dV_7 = e^{6Hy} l^3 dy",
    "inputFormDictionary" -> "strings copied from Wolfram InputForm use: kk = k, eps = eps, vv[y] = v_v(y), Meff[y] = Meff(y), a4c = a_4, H = H, m = m, lam = lambda, kap = kappa (gravitational), LL = L (tip cutoff), M = constant Meff of the k = 0 box, nn = level index n, E^x = e^x",
    "matrixEntryFormat" -> "every matrix or vector entry is [re, im] with re, im rational strings 'n' or 'n/d' (exact); real scalars are rational strings"|>;
  res = Catch[
    step["fixture", checkFixture[fixFile]];
    step["geometry (y chart, a4 constant)", buildGeometry[]];
    step["KS_geometry", checkGeometry[]];
    step["KS_reduction", checkReduction[]];
    step["KS_boundary", checkBoundary[]];
    step["KS_exchange", checkExchange[]];
    step["KS_functional", checkFunctional[]];
    step["KS_emt", checkEMT[]];
    "ok", d16ksErr];
  If[res =!= "ok", Print["INTERNAL ERROR: ", res]; addCheck["KS_internal_noException", False], addCheck["KS_internal_noException", True]];
  logT["done in ", Round[AbsoluteTime[] - t0], " s"];
  <|"checks" -> $checks, "measurements" -> $meas, "theory" -> $theory|>];

End[];
EndPackage[];
