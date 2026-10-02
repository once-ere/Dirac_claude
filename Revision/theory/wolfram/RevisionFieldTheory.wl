(* ::Package:: *)

(* RevisionFieldTheory.wl

   The field theory of the Revision record (Revision/SPEC.md, sections 1-4 and 6) for the two fields
   dirac16complex (16 complex ANTICOMMUTING components, an explicit Grassmann algebra) and
   dirac16complex00 (16 complex COMMUTING components), coupled to the author's primordial metric
   through the vielbein and the canonical spin connection.  Driven by
   Revision/theory/wolfram/verify_field_theory.wls.

   Nothing here is taken from an earlier stage of the repository (artifacts/, provenance/, studies/,
   scripts/, wolfram/, notebooks/); the only input is the Revision fixture Revision/algebra/gammas.json
   (decoded by its own reader below, independent of the algebra package).

   Names.  The package defines global symbols with the prefix rft (functions, data) and uses the
   global coordinate symbols x1 ... x8 (the author's names: x1, x2, x3 = 3-space, x4 = time,
   x5, x6, x7 = the exponentially deflating extra times, x8 = the hidden direction), the metric
   function a4[x4], the constant H > 0, the mass m, the coupling lam and z = 6 H x8 in (0, Pi/2).

   1. Geometry (SPEC section 1).  g = diag(f1^2, f2^2, f3^2, -1, -f5^2, -f6^2, -f7^2, f8^2) with
        f1 = f2 = f3 = E^a4 Sin[z]^(1/6),  f4 = 1,  f5 = f6 = f7 = E^-a4 Sin[z]^(1/6),  f8 = Cot[z];
      diagonal vielbein e^a_mu = f_a delta^a_mu (row a = frame, column mu = coordinate), inverse
      vielbein e_a^mu = delta / f_a; eta = diag(1,1,1,-1,-1,-1,-1,1); sqrt|g| = Cos[z].
      Christoffel Gamma^l_mn = (1/2) g^lr (d_m g_rn + d_n g_rm - d_r g_mn);
      Riemann R^r_smn = d_m Gamma^r_ns - d_n Gamma^r_ms + Gamma^r_ml Gamma^l_ns - Gamma^r_nl Gamma^l_ms,
      Ricci R_sn = R^r_srn, R = g^sn R_sn.

   2. Canonical spin connection (vielbein postulate d_mu e_b^nu + Gamma^nu_mu,l e_b^l - omega_mu^a_b e_a^nu = 0):
        omega_mu^a_b = e^a_nu (d_mu e_b^nu + Gamma^nu_mu,l e_b^l),   omega_mu,ab = eta_ac omega_mu^c_b,
        Omega_mu = (1/2) omega_mu,ab S^ab   (S^ab = (1/4)[gamma^a, gamma^b] from the fixture),
        gamma^mu = e_a^mu gamma^a,  D_mu Psi = d_mu Psi + Omega_mu Psi,  D_mu Psibar = d_mu Psibar - Psibar Omega_mu.

   3. Fields.  Commuting (dirac16complex00): Phi_A = ph[A][x1..x8], PhiConj_A = phc[A][x1..x8] (phc is the
      complex conjugate of ph; the reality checks swap ph <-> phc and conjugate numbers).
      Anticommuting (dirac16complex): an explicit Grassmann algebra with generators 1..N (theta_k) and
      N+1..2N (thetabar_k = conj(theta_k)), N = 2 by default; an element is an Association
      {sorted generator list} -> commuting coefficient; product with the sign of the sorting
      permutation; the involution conj is antilinear and reverses products: conj(theta_i theta_j) =
      thetabar_j thetabar_i.  Psi_A = sum_k ph[A,k][x] theta_k, PsiConj_A = sum_k phc[A,k][x] thetabar_k.
      With N = 2 the bilinear S = Psibar Psi is even and nilpotent with S^2 != 0 and S^3 = 0, so the
      most general potential is U = u1 S + (lam/2) S^2 (+ constant).

   4. Lagrangian density (SPEC section 3), the same expression for both statistics:
        L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m Psibar Psi - U(S) ],
      Psibar = Psi^dagger C, S = Psibar Psi.

   5. The energy-momentum tensor by vielbein variation: for the perturbation e^b_nu -> e^b_nu + eps h(x)
      the first-order Lagrangian L1 is computed exactly (first-order Christoffels, spin connection,
      sqrt|g| and gamma^mu) and T^nu_b = (1/sqrt|g|) (dL1/dh - d_l dL1/d(d_l h)).  T^nu_mu = T^nu_b e^b_mu.
*)

(* ------------------------------------------------------------------ coordinates and metric *)
rftX = {x1, x2, x3, x4, x5, x6, x7, x8};
rftZ = 6 H x8;
rftCoordNames = {"x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"};
rftEta = DiagonalMatrix[{1, 1, 1, -1, -1, -1, -1, 1}];
rftEtaD = {1, 1, 1, -1, -1, -1, -1, 1};
rftF = {E^a4[x4] Sin[rftZ]^(1/6), E^a4[x4] Sin[rftZ]^(1/6), E^a4[x4] Sin[rftZ]^(1/6), 1,
        E^(-a4[x4]) Sin[rftZ]^(1/6), E^(-a4[x4]) Sin[rftZ]^(1/6), E^(-a4[x4]) Sin[rftZ]^(1/6), Cot[rftZ]};
(* the author's metric, typed as in SPEC section 1 *)
rftMetricAuthor = {{E^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0,0},{0,E^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0},
  {0,0,E^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0},{0,0,0,-1,0,0,0,0},
  {0,0,0,0,-E^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0},{0,0,0,0,0,-E^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0},
  {0,0,0,0,0,0,-E^(-2 a4[x4]) Sin[6 H x8]^(1/3),0},{0,0,0,0,0,0,0,Cot[6 H x8]^2}};
rftAssumptions = {H > 0, 0 < 6 H x8 < Pi/2, Element[a4[x4], Reals], Element[x4, Reals]};

rftE0 = DiagonalMatrix[rftF];                (* e^a_mu: row a (frame), column mu (coordinate) *)
rftEinv0 = DiagonalMatrix[1/rftF];           (* e_a^mu stored as [[mu, a]] *)
rftG0 = Transpose[rftE0] . rftEta . rftE0;
rftGinv0 = Inverse[rftG0];
rftSqrtG0 = Cos[rftZ];

(* ------------------------------------------------------------------ exact zero test *)
(* Sin z -> w^6 (w > 0), Cos z -> cw, cw^2 -> 1 - w^12 after clearing denominators. *)
rftTrigRules = {Sin[6 H x8] -> rftw^6, Cos[6 H x8] -> rftcw, Cot[6 H x8] -> rftcw/rftw^6,
  Tan[6 H x8] -> rftw^6/rftcw, Csc[6 H x8] -> 1/rftw^6, Sec[6 H x8] -> 1/rftcw};
rftReduceCos[p_] := Expand[p /. rftcw^n_Integer /; n >= 2 :> (1 - rftw^12)^Quotient[n, 2] rftcw^Mod[n, 2]];
rftNormal[e_] := Module[{t},
  t = PowerExpand[e /. rftTrigRules];
  t = Together[t];
  rftReduceCos[Numerator[t]]/Denominator[t]];
(* rftZeroQ: exact and sound.  The field functions (and every U[..], U'[..] of a field expression, each
   replaced by its own symbol) are treated as independent polynomial variables; the expression is zero if
   every coefficient (a rational function of Sin z, Cos z, E^a4, a4', ... ) reduces to 0 with
   Cos^2 = 1 - Sin^2.  Treating U-expressions as independent can only make the test stricter. *)
rftFieldHeadPattern = ph | phc | qv | phr | rfth | pf | qf;
rftZeroQ[e_] := Module[{t, uexp, urules, vars, coefs},
  t = Expand[PowerExpand[e /. rftTrigRules]];
  If[t === 0, Return[True]];
  uexp = Union[Cases[t, (U | Derivative[_][U])[_], {0, Infinity}]];
  urules = Thread[uexp -> Array[rftUsym, Length[uexp]]];
  t = Expand[t /. urules];
  (* field calls: compound heads such as ph[3][x1, ..., x8] or Derivative[..][phc[3, 1]][x1, ..., x8],
     the scalar test functions pf[x8], qf[x8] and their derivatives, and the constants cA[..], cAc[..] *)
  vars = Union[Cases[t, (hh_[__] /; (!AtomQ[hh] && !FreeQ[hh, rftFieldHeadPattern])) | (pf | qf)[_] | (cA | cAc)[__], {0, Infinity}]];
  coefs = If[vars === {}, {t}, Last /@ CoefficientRules[t, vars]];
  And @@ (rftReduceCos[Expand[Numerator[Together[#]]]] === 0 & /@ coefs)];
rftZeroQ[e_List] := And @@ (rftZeroQ /@ Flatten[e]);
(* a canonical simplified form for the formula file *)
rftSimp[e_] := FullSimplify[e, rftAssumptions];

(* ------------------------------------------------------------------ the fixture *)
rftDecodeRational[q_Integer] := q;
rftDecodeRational[q_String] := Module[{p = StringSplit[q, "/"]},
  If[Length[p] == 2, ToExpression[p[[1]]]/ToExpression[p[[2]]], Abort[]]];
rftDecodeMatrix[m_List] := Map[rftDecodeRational, m, {2}];
rftDecodeMatrix[m_Association] := rftDecodeMatrix[m["re"]] + I rftDecodeMatrix[m["im"]];
rftLoadFixture[path_String] := Module[{j = Import[path, "RawJSON"]},
  rftFixtureRaw = j;
  rftGam = rftDecodeMatrix /@ j["gamma"];
  rftC = rftDecodeMatrix[j["C"]];
  rftChir = rftDecodeMatrix[j["Gamma"]];
  rftB = rftDecodeMatrix[j["B"]];
  rftS = Table[rftDecodeMatrix[j["S"][[a, b]]], {a, 8}, {b, 8}];
  rftEtaFixture = j["eta"];
  rftI16 = IdentityMatrix[16];
  rftZ16 = ConstantArray[0, {16, 16}];
];

(* ------------------------------------------------------------------ Christoffel, Riemann, spin connection *)
rftChristoffel[g_, ginv_] := Table[
  (1/2) Sum[ginv[[l, r]] (D[g[[r, n]], rftX[[mm]]] + D[g[[r, mm]], rftX[[n]]] - D[g[[mm, n]], rftX[[r]]]), {r, 8}],
  {l, 8}, {mm, 8}, {n, 8}];   (* [[l, m, n]] = Gamma^l_mn *)
rftRiemann[Gm_] := Table[
  D[Gm[[r, n, s]], rftX[[mm]]] - D[Gm[[r, mm, s]], rftX[[n]]] +
  Sum[Gm[[r, mm, l]] Gm[[l, n, s]] - Gm[[r, n, l]] Gm[[l, mm, s]], {l, 8}],
  {r, 8}, {s, 8}, {mm, 8}, {n, 8}];   (* [[r, s, m, n]] = R^r_smn *)

(* omega[[mu, a, b]] = omega_mu^a_b for a vielbein e ([[a, mu]]) with inverse einv ([[mu, a]]) *)
rftOmegaMixed[e_, einv_, Gm_] := Table[
  Sum[e[[a, n]] (D[einv[[n, b]], rftX[[mm]]] + Sum[Gm[[n, mm, l]] einv[[l, b]], {l, 8}]), {n, 8}],
  {mm, 8}, {a, 8}, {b, 8}];
rftLower[om_] := Table[Sum[rftEta[[a, c]] om[[mm, c, b]], {c, 8}], {mm, 8}, {a, 8}, {b, 8}];
rftSpinorConnection[omLow_] := Table[(1/2) Sum[omLow[[mm, a, b]] rftS[[a, b]], {a, 8}, {b, 8}], {mm, 8}];
rftGammaUp[einv_] := Table[Sum[einv[[mm, a]] rftGam[[a]], {a, 8}], {mm, 8}];

rftBuildGeometry[] := Module[{},
  rftGamma0 = rftChristoffel[rftG0, rftGinv0];
  rftOmegaMix0 = rftOmegaMixed[rftE0, rftEinv0, rftGamma0];
  rftOmegaLow0 = rftLower[rftOmegaMix0];
  rftOm0 = rftSpinorConnection[rftOmegaLow0];
  rftGup0 = rftGammaUp[rftEinv0];
  rftGeo0 = <|"sqrtg" -> rftSqrtG0, "gup" -> rftGup0, "Om" -> rftOm0|>;
];

(* ------------------------------------------------------------------ explicit Grassmann algebra *)
(* element: Association[sorted list of generator ids -> coefficient]; ids 1..N theta, N+1..2N thetabar *)
rftGN = 2;
gClean[a_Association] := Select[a, # =!= 0 &];
gAdd[l_List] := gClean[Merge[l, Total]];
gScal[c_, a_Association] := gClean[(c #) & /@ a];
gMul[a_Association, b_Association] := Module[{out = {}},
  KeyValueMap[Function[{ka, ca},
    KeyValueMap[Function[{kb, cb},
      If[!IntersectingQ[ka, kb],
        AppendTo[out, <|Sort[Join[ka, kb]] -> Signature[Join[ka, kb]] ca cb|>]]], b]], a];
  gAdd[out]];
gD[a_Association, x_] := gClean[D[#, x] & /@ a];
gMapCoeff[f_, a_Association] := gClean[f /@ a];
gPartner[k_Integer] := If[k <= rftGN, k + rftGN, k - rftGN];
rftCConj[e_] := (e /. {ph -> phc, phc -> ph, cA -> cAc, cAc -> cA}) /. Complex[re_, im_] :> Complex[re, -im];
gConj[a_Association] := gAdd[KeyValueMap[Function[{k, c},
  Module[{nk = Reverse[gPartner /@ k]}, <|Sort[nk] -> Signature[nk] rftCConj[c]|>]], a]];
gZeroQ[a_Association] := And @@ (rftZeroQ /@ Values[a]);
gTheta[k_] := <|{k} -> 1|>;
gThetaBar[k_] := <|{k + rftGN} -> 1|>;
gScalar[c_] := If[c === 0, <||>, <|{} -> c|>];

(* ------------------------------------------------------------------ statistics-generic spinor algebra *)
(* stat = "C" (commuting, plain expressions) or "G" (Grassmann elements) *)
sAdd["C", l_List] := Total[l];  sAdd["G", l_List] := gAdd[l];
sScal["C", c_, a_] := c a;      sScal["G", c_, a_] := gScal[c, a];
sMul["C", a_, b_] := a b;       sMul["G", a_, b_] := gMul[a, b];
sD["C", a_, x_] := D[a, x];     sD["G", a_, x_] := gD[a, x];
sZero["C"] := 0;                sZero["G"] := <||>;
sZeroQ["C", a_] := rftZeroQ[a]; sZeroQ["G", a_] := gZeroQ[a];
sConj["C", a_] := rftCConj[a];  sConj["G", a_] := gConj[a];
sMap["C", f_, a_] := f[a];      sMap["G", f_, a_] := gMapCoeff[f, a];

matVec[st_, M_, v_List] := Table[sAdd[st, Table[If[M[[A, B]] === 0, sZero[st], sScal[st, M[[A, B]], v[[B]]]], {B, 16}]], {A, 16}];
vecMat[st_, v_List, M_] := Table[sAdd[st, Table[If[M[[A, B]] === 0, sZero[st], sScal[st, M[[A, B]], v[[A]]]], {A, 16}]], {B, 16}];
sDot[st_, row_List, col_List] := sAdd[st, MapThread[sMul[st, #1, #2] &, {row, col}]];
vAdd[st_, vs__] := MapThread[sAdd[st, {##}] &, {vs}];
vScal[st_, c_, v_List] := sScal[st, c, #] & /@ v;
vD[st_, v_List, x_] := sD[st, #, x] & /@ v;

(* fields *)
rftField["C"] := Table[ph[A] @@ rftX, {A, 16}];
rftFieldC["C"] := Table[phc[A] @@ rftX, {A, 16}];
rftField["G"] := Table[gAdd[Table[<|{k} -> ph[A, k] @@ rftX|>, {k, rftGN}]], {A, 16}];
rftFieldC["G"] := Table[gAdd[Table[<|{k + rftGN} -> phc[A, k] @@ rftX|>, {k, rftGN}]], {A, 16}];
rftFieldHeads["C"] := Table[ph[A], {A, 16}];
rftFieldHeads["G"] := Flatten[Table[ph[A, k], {A, 16}, {k, rftGN}]];
rftFieldCHeads["C"] := Table[phc[A], {A, 16}];
rftFieldCHeads["G"] := Flatten[Table[phc[A, k], {A, 16}, {k, rftGN}]];

(* potential: commuting -> general function U; Grassmann -> u1 S + (lam/2) S^2 (general for N = 2) *)
rftPot["C", S_] := U[S];
rftPotPrime["C", S_] := U'[S];
rftPot["G", S_] := sAdd["G", {gScal[u1, S], gScal[lam/2, gMul[S, S]]}];
rftPotPrime["G", S_] := sAdd["G", {gScalar[u1], gScal[lam, S]}];
(* V Psi = (m + U'(S)) Psi as a spinor *)
rftVPsi["C", S_, Psi_] := (m + U'[S]) Psi;
rftVPsi["G", S_, Psi_] := Module[{V = sAdd["G", {gScalar[m + u1], gScal[lam, S]}]}, sMul["G", V, #] & /@ Psi];
rftVRow["C", S_, row_] := (m + U'[S]) row;
rftVRow["G", S_, row_] := Module[{V = sAdd["G", {gScalar[m + u1], gScal[lam, S]}]}, sMul["G", V, #] & /@ row];

(* ------------------------------------------------------------------ Lagrangian pieces *)
rftPsibar[st_, Psic_] := vecMat[st, Psic, rftC];
rftDPsi[st_, geo_, Psi_, mu_] := vAdd[st, vD[st, Psi, rftX[[mu]]], matVec[st, geo["Om"][[mu]], Psi]];
rftDPsibar[st_, geo_, Psic_, mu_] := Module[{pb = rftPsibar[st, Psic]},
  vAdd[st, vD[st, pb, rftX[[mu]]], vScal[st, -1, vecMat[st, pb, geo["Om"][[mu]]]]]];
rftSbil[st_, Psi_, Psic_] := sDot[st, rftPsibar[st, Psic], Psi];

(* the kinetic bilinear (1/2) sum_mu (Psibar gamma^mu D_mu Psi - D_mu Psibar gamma^mu Psi), no sqrt g *)
rftKin[st_, geo_, Psi_, Psic_] := Module[{pb = rftPsibar[st, Psic]},
  sAdd[st, Table[sAdd[st, {
      sScal[st, 1/2, sDot[st, vecMat[st, pb, geo["gup"][[mu]]], rftDPsi[st, geo, Psi, mu]]],
      sScal[st, -1/2, sDot[st, vecMat[st, rftDPsibar[st, geo, Psic, mu], geo["gup"][[mu]]], Psi]]}], {mu, 8}]]];
rftL0[st_, geo_, Psi_, Psic_] := Module[{S = rftSbil[st, Psi, Psic]},
  sAdd[st, {rftKin[st, geo, Psi, Psic], sScal[st, -m, S], sScal[st, -1, rftPot[st, S]]}]];
rftLag[st_, geo_, Psi_, Psic_] := sScal[st, geo["sqrtg"], rftL0[st, geo, Psi, Psic]];
(* the unsymmetrised form sqrt g [Psibar gamma^mu D_mu Psi - m S - U] *)
rftLagUnsym[st_, geo_, Psi_, Psic_] := Module[{pb = rftPsibar[st, Psic], S = rftSbil[st, Psi, Psic]},
  sScal[st, geo["sqrtg"], sAdd[st, {
    sAdd[st, Table[sDot[st, vecMat[st, pb, geo["gup"][[mu]]], rftDPsi[st, geo, Psi, mu]], {mu, 8}]],
    sScal[st, -m, S], sScal[st, -1, rftPot[st, S]]}]]];

(* the Dirac operator gamma^mu D_mu Psi, the field-equation residual E and its adjoint Ebar *)
rftDirac[st_, geo_, Psi_] := Fold[vAdd[st, #1, #2] &, Table[matVec[st, geo["gup"][[mu]], rftDPsi[st, geo, Psi, mu]], {mu, 8}]];
rftE[st_, geo_, Psi_, Psic_] := Module[{S = rftSbil[st, Psi, Psic]},
  vAdd[st, rftDirac[st, geo, Psi], vScal[st, -1, rftVPsi[st, S, Psi]]]];
rftEbar[st_, geo_, Psi_, Psic_] := Module[{S = rftSbil[st, Psi, Psic]},
  vAdd[st, Fold[vAdd[st, #1, #2] &, Table[vecMat[st, rftDPsibar[st, geo, Psic, mu], geo["gup"][[mu]]], {mu, 8}]],
    rftVRow[st, S, rftPsibar[st, Psic]]]];

(* ------------------------------------------------------------------ Euler-Lagrange (functional) derivative *)
(* for a coefficient function head f (e.g. phc[3, 1]) appearing with at most first derivatives *)
rftUnitDeriv[mu_] := Derivative @@ UnitVector[8, mu];
rftVarDerExpr[c_, f_] := Module[{rules, inv, cc, s0, sd, res},
  rules = Join[{f @@ rftX -> s0}, Table[rftUnitDeriv[mu][f] @@ rftX -> sd[mu], {mu, 8}]];
  inv = Join[{s0 -> f @@ rftX}, Table[sd[mu] -> rftUnitDeriv[mu][f] @@ rftX, {mu, 8}]];
  cc = c /. rules;
  res = (D[cc, s0] /. inv) - Sum[D[D[cc, sd[mu]] /. inv, rftX[[mu]]], {mu, 8}];
  res];
rftVarDer["C", L_, f_] := rftVarDerExpr[L, f];
rftVarDer["G", L_Association, f_] := gClean[rftVarDerExpr[#, f] & /@ L];
(* partial derivative with respect to d_mu f (canonical momentum) *)
rftPartialD[c_, f_, mu_] := Module[{sd},
  D[c /. rftUnitDeriv[mu][f] @@ rftX -> sd, sd] /. sd -> rftUnitDeriv[mu][f] @@ rftX];
rftPartialD["C", L_, f_, mu_] := rftPartialD[L, f, mu];
rftPartialD["G", L_Association, f_, mu_] := gClean[rftPartialD[#, f, mu] & /@ L];

(* ------------------------------------------------------------------ vielbein variation *)
(* first-order geometry for e^b_nu -> e^b_nu + eps h(x) *)
rftUnitMatrix[b_, nu_] := ReplacePart[ConstantArray[0, {8, 8}], {b, nu} -> 1];
rftGeo1[b_, nu_, h_] := Module[{e1, einv1, g1, ginv1, Gm1, om1, omLow1, Om1, gup1, sqrtg1},
  e1 = h rftUnitMatrix[b, nu];
  einv1 = -rftEinv0 . e1 . rftEinv0;   (* [[mu, a]] *)
  g1 = Transpose[e1] . rftEta . rftE0 + Transpose[rftE0] . rftEta . e1;
  ginv1 = -rftGinv0 . g1 . rftGinv0;
  Gm1 = Table[(1/2) Sum[
      ginv1[[l, r]] (D[rftG0[[r, n]], rftX[[mm]]] + D[rftG0[[r, mm]], rftX[[n]]] - D[rftG0[[mm, n]], rftX[[r]]]) +
      rftGinv0[[l, r]] (D[g1[[r, n]], rftX[[mm]]] + D[g1[[r, mm]], rftX[[n]]] - D[g1[[mm, n]], rftX[[r]]]), {r, 8}],
    {l, 8}, {mm, 8}, {n, 8}];
  om1 = Table[Sum[
      e1[[a, n]] (D[rftEinv0[[n, bb]], rftX[[mm]]] + Sum[rftGamma0[[n, mm, l]] rftEinv0[[l, bb]], {l, 8}]) +
      rftE0[[a, n]] (D[einv1[[n, bb]], rftX[[mm]]] + Sum[Gm1[[n, mm, l]] rftEinv0[[l, bb]] + rftGamma0[[n, mm, l]] einv1[[l, bb]], {l, 8}]),
      {n, 8}], {mm, 8}, {a, 8}, {bb, 8}];
  omLow1 = rftLower[om1];
  Om1 = rftSpinorConnection[omLow1];
  gup1 = rftGammaUp[einv1];
  sqrtg1 = rftSqrtG0 Tr[rftEinv0 . e1];
  <|"sqrtg" -> sqrtg1, "gup" -> gup1, "Om" -> Om1, "omLow" -> omLow1|>];

(* first-order Lagrangian: L(geo0 + eps geo1) to first order in eps; L0 = the zeroth-order L/sqrt g *)
rftLag1[st_, geo1_, Psi_, Psic_, L0_] := Module[{pb = rftPsibar[st, Psic], kin1},
  (* (1/2)[Psibar gamma1 D0 Psi - D0 Psibar gamma1 Psi] + (1/2)[Psibar gamma0 Om1 Psi + Psibar Om1 gamma0 Psi] *)
  kin1 = sAdd[st, Table[sAdd[st, {
      sScal[st, 1/2, sDot[st, vecMat[st, pb, geo1["gup"][[mu]]], rftDPsi[st, rftGeo0, Psi, mu]]],
      sScal[st, -1/2, sDot[st, vecMat[st, rftDPsibar[st, rftGeo0, Psic, mu], geo1["gup"][[mu]]], Psi]],
      sScal[st, 1/2, sDot[st, pb, matVec[st, rftGup0[[mu]] . geo1["Om"][[mu]] + geo1["Om"][[mu]] . rftGup0[[mu]], Psi]]]
    }], {mu, 8}]];
  sAdd[st, {sScal[st, geo1["sqrtg"], L0], sScal[st, rftSqrtG0, kin1]}]];

(* T^nu_b (one vielbein component) for the field (Psi, Psic): (1/sqrt g) delta S / delta e^b_nu *)
rftTvar[st_, b_, nu_, Psi_, Psic_, L0_] := Module[{geo1, L1},
  geo1 = rftGeo1[b, nu, rfth @@ rftX];
  L1 = rftLag1[st, geo1, Psi, Psic, L0];
  sScal[st, 1/rftSqrtG0, If[st === "C", rftVarDerExpr[L1, rfth], gClean[rftVarDerExpr[#, rfth] & /@ L1]]]];

Print["RevisionFieldTheory.wl loaded"];
