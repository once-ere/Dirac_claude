(* ::Package:: *)

(* RevisionPairing.wl

   Exact machinery for the pairing theorems of the Revision record (Revision/SPEC.md, section 9):
   T1 (the chirality map Gamma), T2 (Gamma combined with a Pin(4,4) reflection of character -1; the
   Z2 mirror across the patch end z = pi/2 of the hidden coordinate) and the quantum-level reading.
   Context RevisionPairing`.  Driven by Revision/pairing/wolfram/verify_pairing.wls.

   Inputs: ONLY the Revision fixture Revision/algebra/gammas.json (gamma^(x1..x8), C, Gamma, B, S in
   the author's coordinate order x1..x8; x1, x2, x3 = 3-space, x4 = time, x5, x6, x7 = the
   exponentially deflating extra times, x8 = the hidden direction).  Nothing is taken from an earlier
   stage of the repository.

   1. The field algebra.  Both statistics are handled by ONE code path:
        generators  RPpsi[A], RPpsis[A]            (Psi_A and Psi_A^dagger at the point x)
                    RPdpsi[A, mu], RPdpsis[A, mu]  (their first derivatives d_mu, mu = 1..8 = x1..x8)
      An element is an Association  {g1, ..., gk} -> coefficient  (a monomial in canonical order).
        commuting mode   (gr = False, dirac16complex00): monomials are sorted multisets;
        Grassmann mode   (gr = True,  dirac16complex):   all generators are odd; a product is
                         re-ordered with the sign of the permutation (Signature) and vanishes when a
                         generator repeats.
      Left / right derivatives with respect to a generator and the total derivative d_mu (the
      coefficient is differentiated and every undifferentiated generator is replaced by its
      first-derivative generator, in place) are implemented for both modes.

   2. The geometry.  RPGeometry[E, dE, sqrtg, simp] takes a vielbein matrix E[[a, mu]] = e^a_mu, the
      list dE[[rho]] = d_rho E (symbolic derivatives, or exact numbers at one point) and sqrt|g|, and
      returns the canonical (Levi-Civita) spin connection of SPEC section 3:
        g = E^T eta E,  Chr^nu_(mu lambda) = (1/2) g^(nu sigma)(d_mu g_(sigma lambda) + d_lambda g_(sigma mu) - d_sigma g_(mu lambda)),
        omega_mu^a_b = e^a_nu (d_mu e^nu_b + Chr^nu_(mu lambda) e^lambda_b),  omega_mu ab = eta_ac omega_mu^c_b,
        Omega_mu = (1/2) omega_mu ab S^ab,  gamma^mu = e^mu_a gamma^a,  gamma_mu = g_mu nu gamma^nu,
      with d_mu e^nu_b = -(E^-1 . d_mu E . E^-1)^nu_b.

   3. The bilinears (SPEC sections 3, 4), for given field jets f (a transformed field is passed as
      transformed jets):
        Psibar = Psi^dagger C,  D_mu Psi = d_mu Psi + Omega_mu Psi,  D_mu Psibar = d_mu Psibar - Psibar Omega_mu,
        K  = (1/2) sum_mu ( Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi ),   S = Psibar Psi,
        L_(m,lambda) = sqrt|g| ( K - m S - (lambda/2) S^2 ),
        T_mu nu = (1/4)( Psibar gamma_mu D_nu Psi + Psibar gamma_nu D_mu Psi - (D_mu Psibar) gamma_nu Psi
                         - (D_nu Psibar) gamma_mu Psi ) - g_mu nu ( K - m S - (lambda/2) S^2 ),
        J^mu = Psibar gamma^mu Psi,
        E_(m,lambda) = gamma^mu D_mu Psi - (m + lambda S) Psi   (the covariant field-equation operator).
      T_mu nu is the symmetric (Belinfante, vielbein-variation) form; any constant overall sign or
      normalisation convention of SPEC section 4 multiplies both sides of every identity below and
      does not affect them.
*)

BeginPackage["RevisionPairing`"];

RPLoadFixture::usage = "RPLoadFixture[path] reads Revision/algebra/gammas.json and sets RPgamma, RPeta, RPC, RPGamma, RPB, RPS.";
RPgamma::usage = "RPgamma[[a]] = gamma^(x_a), a = 1..8.";
RPeta::usage = "RPeta = diag(+1,+1,+1,-1,-1,-1,-1,+1).";
RPC::usage = "RPC: the charge matrix C of SPEC section 2.";
RPGamma::usage = "RPGamma: the chirality Gamma of SPEC section 2.";
RPB::usage = "RPB = -I C gamma^(x4).";
RPS::usage = "RPS[[a, b]] = S^ab.";
RPX::usage = "RPX = {x1, ..., x8} (coordinate symbols).";
RPH::usage = "RPH: the author's constant H.";
RPa4::usage = "RPa4: the metric function a4[x4].";
RPm::usage = "RPm: the mass parameter m.";
RPlam::usage = "RPlam: the coupling lambda of U(S) = (lambda/2) S^2.";
RPpsi::usage = "RPpsi[A]: generator Psi_A."; RPpsis::usage = "RPpsis[A]: generator Psi_A^dagger.";
RPdpsi::usage = "RPdpsi[A, mu]: generator d_mu Psi_A."; RPdpsis::usage = "RPdpsis[A, mu]: generator d_mu Psi_A^dagger.";
RPePlus::usage = "RPePlus[{e1, e2, ...}] adds field-algebra elements.";
RPeScale::usage = "RPeScale[c, e] multiplies an element by the coefficient c.";
RPeTimes::usage = "RPeTimes[gr, a, b]: product of elements (gr = True: Grassmann, False: commuting).";
RPeDiff::usage = "RPeDiff[a, b] = a - b.";
RPeZeroQ::usage = "RPeZeroQ[e, assumptions] is True when every coefficient of e simplifies to 0.";
RPeMapCoefficients::usage = "RPeMapCoefficients[f, e] applies f to every coefficient.";
RPeSubst::usage = "RPeSubst[gr, e, rule] replaces every generator q by the element rule[q] (products taken in monomial order).";
RPLeftD::usage = "RPLeftD[gr, e, q]: left derivative with respect to the generator q.";
RPRightD::usage = "RPRightD[gr, e, q]: right derivative with respect to the generator q.";
RPTotalD::usage = "RPTotalD[gr, e, mu]: total derivative d_mu (coefficients depend on RPX; generators of order 0 only).";
RPMatVec::usage = "RPMatVec[M, v]: matrix times a column of elements.";
RPRowMat::usage = "RPRowMat[r, M]: a row of elements times a matrix.";
RPDot::usage = "RPDot[gr, r, v]: row of elements times column of elements.";
RPvPlus::usage = "RPvPlus[v1, v2]: sum of two element vectors."; RPvScale::usage = "RPvScale[c, v].";
RPBaseFields::usage = "RPBaseFields[]: the jets of the field Psi (generators).";
RPTransformFields::usage = "RPTransformFields[f, M, jac]: the jets of Psi'(x') = M Psi(x) with d'_mu = jac[[mu, nu]] d_nu.";
RPGeometry::usage = "RPGeometry[E, dE, sqrtg, simp]: canonical spin connection and gammas (see the header).";
RPBilinears::usage = "RPBilinears[gr, geom, f, m, lam]: Association with Psibar, DPsi, DPsibar, K, S, L, T, J, Evec, ELexpected, ELbarExpected.";
RPDerivedEL::usage = "RPDerivedEL[gr, L]: {Euler-Lagrange expressions for the Psi^dagger variation (left derivatives), for the Psi variation (right derivatives)}.";
RPToExpr::usage = "RPToExpr[e]: an element of the commuting algebra as an ordinary polynomial.";

Begin["`Private`"];

(* ---------- 0. fixture ---------- *)
decodeRational[q_Integer] := q;
decodeRational[q_String] := ToExpression[q];
decodeMatrix[m_List] := Map[decodeRational, m, {2}];
decodeMatrix[m_Association] := decodeMatrix[m["re"]] + I decodeMatrix[m["im"]];

RPLoadFixture[path_String] := Module[{j = Import[path, "RawJSON"]},
  RPgamma = decodeMatrix /@ j["gamma"];
  RPeta = DiagonalMatrix[decodeRational /@ j["eta"]];
  RPC = decodeMatrix[j["C"]];
  RPGamma = decodeMatrix[j["Gamma"]];
  RPB = decodeMatrix[j["B"]];
  RPS = Map[decodeMatrix, j["S"], {2}];
  j];

RPX = {x1, x2, x3, x4, x5, x6, x7, x8};

(* ---------- 1. field algebra ---------- *)
canon[True, key_List] := If[DuplicateFreeQ[key], {Signature[key], Sort[key]}, Nothing];
canon[False, key_List] := {1, Sort[key]};

RPePlus[list_List] := DeleteCases[Merge[list, Total], 0];
RPeScale[c_, e_Association] := If[c === 0, <||>, DeleteCases[Map[c # &, e], 0]];
RPeDiff[a_Association, b_Association] := RPePlus[{a, RPeScale[-1, b]}];
RPeMapCoefficients[f_, e_Association] := DeleteCases[Map[f, e], 0];

RPeTimes[gr_, a_Association, b_Association] := Module[{rules},
  rules = Flatten[KeyValueMap[
    Function[{ka, ca}, KeyValueMap[
      Function[{kb, cb}, With[{c = canon[gr, Join[ka, kb]]},
        If[c === Nothing, Nothing, c[[2]] -> c[[1]] ca cb]]], b]], a]];
  If[rules === {}, <||>, DeleteCases[Merge[rules, Total], 0]]];

zeroCoefficientQ[c_, assum_] := Module[{t = Together[c]},
  t === 0 || Simplify[t, assum] === 0];
RPeZeroQ[e_Association, assum_ : {}] := AllTrue[Values[e], zeroCoefficientQ[#, assum] &];

gen[q_] := <|{q} -> 1|>;

RPeSubst[gr_, e_Association, rule_] := RPePlus[KeyValueMap[
  Function[{k, c}, RPeScale[c, Fold[RPeTimes[gr, #1, rule[#2]] &, <|{} -> 1|>, k]]], e]];

RPLeftD[gr_, e_Association, q_] := RPePlus[KeyValueMap[
  Function[{k, c}, Module[{pos = Flatten[Position[k, q, {1}]]},
    Which[
      pos === {}, Nothing,
      gr, <|Delete[k, First[pos]] -> (-1)^(First[pos] - 1) c|>,
      True, <|Delete[k, First[pos]] -> Length[pos] c|>]]], e]];

RPRightD[gr_, e_Association, q_] := RPePlus[KeyValueMap[
  Function[{k, c}, Module[{pos = Flatten[Position[k, q, {1}]]},
    Which[
      pos === {}, Nothing,
      gr, <|Delete[k, First[pos]] -> (-1)^(Length[k] - First[pos]) c|>,
      True, <|Delete[k, First[pos]] -> Length[pos] c|>]]], e]];

shiftGen[RPpsi[a_], mu_] := RPdpsi[a, mu];
shiftGen[RPpsis[a_], mu_] := RPdpsis[a, mu];
shiftGen[q_, mu_] := (Message[RPTotalD::order, q]; Abort[]);
RPTotalD::order = "Generator `1` is already differentiated; second derivatives are not implemented.";

RPTotalD[gr_, e_Association, mu_Integer] := RPePlus[KeyValueMap[
  Function[{k, c}, RPePlus[Join[
    {<|k -> D[c, RPX[[mu]]]|>},
    Table[With[{cc = canon[gr, ReplacePart[k, p -> shiftGen[k[[p]], mu]]]},
      If[cc === Nothing, <||>, <|cc[[2]] -> cc[[1]] c|>]], {p, Length[k]}]]]], e]];

RPMatVec[M_, v_List] := Table[RPePlus[Table[If[M[[A, B]] === 0, Nothing, RPeScale[M[[A, B]], v[[B]]]], {B, Length[v]}]], {A, Length[M]}];
RPRowMat[r_List, M_] := Table[RPePlus[Table[If[M[[B, A]] === 0, Nothing, RPeScale[M[[B, A]], r[[B]]]], {B, Length[r]}]], {A, Length[First[M]]}];
RPDot[gr_, r_List, v_List] := RPePlus[Table[RPeTimes[gr, r[[A]], v[[A]]], {A, Length[r]}]];
RPvPlus[v1_List, v2_List] := MapThread[RPePlus[{#1, #2}] &, {v1, v2}];
RPvScale[c_, v_List] := RPeScale[c, #] & /@ v;

RPToExpr[e_Association] := Total[KeyValueMap[#2 (Times @@ #1) &, e]];

RPBaseFields[] := <|
  "psi" -> Table[gen[RPpsi[A]], {A, 16}],
  "psis" -> Table[gen[RPpsis[A]], {A, 16}],
  "dpsi" -> Table[gen[RPdpsi[A, mu]], {mu, 8}, {A, 16}],
  "dpsis" -> Table[gen[RPdpsis[A, mu]], {mu, 8}, {A, 16}]|>;

(* Psi'(x') = M Psi(x), d'_mu = sum_nu jac[[mu, nu]] d_nu;  Psi'^dagger = Psi^dagger M^dagger *)
RPTransformFields[f_Association, M_, jac_] := Module[{Md = ConjugateTranspose[M]},
  <|"psi" -> RPMatVec[M, f["psi"]],
    "psis" -> RPRowMat[f["psis"], Md],
    "dpsi" -> Table[RPMatVec[M, Fold[RPvPlus, Table[RPvScale[jac[[mu, nu]], f["dpsi"][[nu]]], {nu, 8}]]], {mu, 8}],
    "dpsis" -> Table[RPRowMat[Fold[RPvPlus, Table[RPvScale[jac[[mu, nu]], f["dpsis"][[nu]]], {nu, 8}]], Md], {mu, 8}]|>];

(* ---------- 2. geometry ---------- *)
RPGeometry[E_, dE_List, sqrtg_, simp_] := Module[
  {Einv, g, dg, ginv, chr, dEinv, omUp, omDn, Om, gUp, gDn, dgUp, postulate},
  Einv = simp /@ Inverse[E];
  g = simp /@ (Transpose[E] . RPeta . E);
  dg = Table[simp /@ (Transpose[dE[[r]]] . RPeta . E + Transpose[E] . RPeta . dE[[r]]), {r, 8}];
  ginv = simp /@ Inverse[g];
  chr = Table[simp[(1/2) Sum[ginv[[nu, s]] (dg[[mu, s, la]] + dg[[la, s, mu]] - dg[[s, mu, la]]), {s, 8}]], {nu, 8}, {mu, 8}, {la, 8}];
  dEinv = Table[simp /@ (-Einv . dE[[mu]] . Einv), {mu, 8}];
  omUp = Table[simp[Sum[E[[a, nu]] (dEinv[[mu, nu, b]] + Sum[chr[[nu, mu, la]] Einv[[la, b]], {la, 8}]), {nu, 8}]], {mu, 8}, {a, 8}, {b, 8}];
  omDn = Table[simp /@ (RPeta . omUp[[mu]]), {mu, 8}];
  Om = Table[simp /@ ((1/2) Sum[omDn[[mu, a, b]] RPS[[a, b]], {a, 8}, {b, 8}]), {mu, 8}];
  gUp = Table[simp /@ Sum[Einv[[mu, a]] RPgamma[[a]], {a, 8}], {mu, 8}];
  gDn = Table[simp /@ Sum[g[[mu, nu]] gUp[[nu]], {nu, 8}], {mu, 8}];
  dgUp[mu_, nu_] := Sum[dEinv[[mu, nu, a]] RPgamma[[a]], {a, 8}];
  postulate = Table[simp /@ (dgUp[mu, nu] + Sum[chr[[nu, mu, la]] gUp[[la]], {la, 8}] + Om[[mu]] . gUp[[nu]] - gUp[[nu]] . Om[[mu]]), {mu, 8}, {nu, 8}];
  <|"E" -> E, "Einv" -> Einv, "g" -> g, "sqrtg" -> sqrtg, "chr" -> chr, "omegaDown" -> omDn, "Omega" -> Om,
    "gammaUp" -> gUp, "gammaDown" -> gDn,
    "omegaAntisymmetric" -> Table[simp /@ (omDn[[mu]] + Transpose[omDn[[mu]]]), {mu, 8}],
    "postulate" -> postulate|>];

(* ---------- 3. bilinears ---------- *)
RPBilinears[gr_, geo_Association, f_Association, m_, lam_] := Module[
  {C = RPC, psi = f["psi"], Pb, dPb, DPsi, DPb, K, S, SS, Lsc, L, T, J, Evec, ELexp, ELbarExp, gu = geo["gammaUp"], gd = geo["gammaDown"], Om = geo["Omega"], sg = geo["sqrtg"]},
  Pb = RPRowMat[f["psis"], C];
  dPb = Table[RPRowMat[f["dpsis"][[mu]], C], {mu, 8}];
  DPsi = Table[RPvPlus[f["dpsi"][[mu]], RPMatVec[Om[[mu]], psi]], {mu, 8}];
  DPb = Table[RPvPlus[dPb[[mu]], RPvScale[-1, RPRowMat[Pb, Om[[mu]]]]], {mu, 8}];
  K = RPeScale[1/2, RPePlus[Table[RPeDiff[RPDot[gr, RPRowMat[Pb, gu[[mu]]], DPsi[[mu]]], RPDot[gr, RPRowMat[DPb[[mu]], gu[[mu]]], psi]], {mu, 8}]]];
  S = RPDot[gr, Pb, psi];
  SS = RPeTimes[gr, S, S];
  Lsc = RPePlus[{K, RPeScale[-m, S], RPeScale[-lam/2, SS]}];
  L = RPeScale[sg, Lsc];
  T = Table[RPePlus[{RPeScale[1/4, RPePlus[{
        RPDot[gr, RPRowMat[Pb, gd[[mu]]], DPsi[[nu]]], RPDot[gr, RPRowMat[Pb, gd[[nu]]], DPsi[[mu]]],
        RPeScale[-1, RPDot[gr, RPRowMat[DPb[[mu]], gd[[nu]]], psi]], RPeScale[-1, RPDot[gr, RPRowMat[DPb[[nu]], gd[[mu]]], psi]]}]],
      RPeScale[-geo["g"][[mu, nu]], Lsc]}], {mu, 8}, {nu, 8}];
  J = Table[RPDot[gr, RPRowMat[Pb, gu[[mu]]], psi], {mu, 8}];
  Evec = RPvPlus[Fold[RPvPlus, Table[RPMatVec[gu[[mu]], DPsi[[mu]]], {mu, 8}]],
    RPvPlus[RPvScale[-m, psi], RPvScale[-lam, RPeTimes[gr, S, #] & /@ psi]]];
  ELexp = RPvScale[sg, RPMatVec[C, Evec]];
  ELbarExp = RPvScale[sg, RPvPlus[RPvScale[-1, Fold[RPvPlus, Table[RPRowMat[DPb[[mu]], gu[[mu]]], {mu, 8}]]],
    RPvPlus[RPvScale[-m, Pb], RPvScale[-lam, RPeTimes[gr, S, #] & /@ Pb]]]];
  <|"Psibar" -> Pb, "DPsi" -> DPsi, "DPsibar" -> DPb, "K" -> K, "S" -> S, "SS" -> SS, "Lscalar" -> Lsc, "L" -> L,
    "T" -> T, "J" -> J, "Evec" -> Evec, "ELexpected" -> ELexp, "ELbarExpected" -> ELbarExp|>];

(* Euler-Lagrange expressions of a first-order Lagrangian density L (an element):
     Psi^dagger variation:  d_L L / d Psi_A^dagger - d_mu ( d_L L / d (d_mu Psi_A^dagger) )
     Psi variation:         d_R L / d Psi_A        - d_mu ( d_R L / d (d_mu Psi_A) )            *)
RPDerivedEL[gr_, L_Association] := {
  Table[RPeDiff[RPLeftD[gr, L, RPpsis[A]], RPePlus[Table[RPTotalD[gr, RPLeftD[gr, L, RPdpsis[A, mu]], mu], {mu, 8}]]], {A, 16}],
  Table[RPeDiff[RPRightD[gr, L, RPpsi[A]], RPePlus[Table[RPTotalD[gr, RPRightD[gr, L, RPdpsi[A, mu]], mu], {mu, 8}]]], {A, 16}]};

End[];

(* the coordinate and parameter symbols live in this context *)
{RPH, RPa4, RPm, RPlam};

EndPackage[];
