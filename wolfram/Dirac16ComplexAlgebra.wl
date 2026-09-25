(* ::Package:: *)

(* Dirac16ComplexAlgebra.wl

   Exact algebra of the 16-component complex Grassmann spinor field
   "dirac16complex" (Stage 1, arbitrary gravitational field).

   Conventions (binding, see CONTRACT.md of the design phase):
   * everything is counted from 0: frame indices a,b,c = 0..7, spinor indices 0..15;
   * tangent metric eta = diag(+1,+1,+1,+1,-1,-1,-1,-1) (the notebook's eta4488);
   * gamma^a := notebook T16^A[a] = [[0, taubar[a]], [tau[a], 0]] (split-octonion
     block basis), built from the notebook's Qa, Qb, s4by4, t4by4, tau, OverBar[tau];
   * C := sigma16 = gamma^0 gamma^1 gamma^2 gamma^3 = diag(-sigma, sigma);
   * Psibar := Psi^dagger C; S^{ab} = (1/4)[gamma^a, gamma^b];
   * gamma^8 := gamma^0 gamma^1 ... gamma^7 (chirality); P_-/+ = (I -/+ gamma^8)/2;
   * B := -I C gamma^4 (canonical equal-x4 anticommutator matrix, Gaussian normal gauge).

   Every statement verified here is decided by exact integer, rational, Gaussian
   rational or polynomial arithmetic.  No floating point number is used anywhere.
   Linear solution spaces (commutants, intertwiners, invariant forms) are computed as
   exact null spaces of integer coefficient matrices over Q; since the rank of a
   rational matrix does not change under field extension, the complex dimensions
   are the same numbers.

   Public entry points:
     D16AlgebraVerification[]      -> <|"checks" -> <|name -> bool|>, "measurements" -> <|...|>|>
     D16CompareFixture[json]       -> comparison of an independent JSON fixture with this construction
     D16JSONValue[expr]            -> JSON-ready form (exact rationals as "p/q" strings)

   License: GPL-3.0-or-later (same as the dirac-main reference implementation). *)

BeginPackage["Dirac16Complex`Algebra`"];

D16Eta::usage = "D16Eta is the tangent metric diag(1,1,1,1,-1,-1,-1,-1).";
D16Sigma8::usage = "D16Sigma8 is the notebook sigma = [[0,I4],[I4,0]].";
D16Tau::usage = "D16Tau is the list of the eight notebook 8x8 matrices tau[0..7] (zero-based: D16Tau[[a+1]] = tau[a]).";
D16TauBar::usage = "D16TauBar is the list of the eight notebook matrices OverBar[tau][0..7].";
D16Gammas::usage = "D16Gammas is the list of the eight 16x16 notebook gammas T16^A[0..7].";
D16Gamma::usage = "D16Gamma[a] is gamma^a (a = 0..7) and D16Gamma[8] the chirality gamma^8.";
D16C::usage = "D16C is the charge/adjoint matrix C = sigma16 = gamma^0 gamma^1 gamma^2 gamma^3.";
D16Chirality::usage = "D16Chirality is gamma^8 = gamma^0 gamma^1 ... gamma^7.";
D16Spin::usage = "D16Spin[a,b] is S^{ab} = (1/4)[gamma^a, gamma^b] (zero-based).";
D16ProjMinus::usage = "D16ProjMinus is P_- = (I - gamma^8)/2.";
D16ProjPlus::usage = "D16ProjPlus is P_+ = (I + gamma^8)/2.";
D16B::usage = "D16B is B = -I C gamma^4.";
D16Monomials::usage = "D16Monomials is the list of the 256 ordered monomials gamma^{i1}...gamma^{ik}, i1 < ... < ik, in Subsets[Range[0,7]] order.";
D16CliffordPictureGammas::usage = "D16CliffordPictureGammas are dirac-main's tensor-product gammas (g1+,..,g4+,g1-,..,g4-) = frame 0..7.";
D16CliffordPictureC::usage = "D16CliffordPictureC is C_dm = gammaHat_0 gammaHat_1 gammaHat_2 gammaHat_3.";
D16CliffordPictureVolume::usage = "D16CliffordPictureVolume is gammaHat_0 ... gammaHat_7.";
D16KClifford::usage = "D16KClifford is the primitive integer solution K of gammaHat^a K == K gamma^a.";
D16OctonionProduct::usage = "D16OctonionProduct[x,y] is the split-octonion product from the Zorn dot/cross formula in orthogonal coordinates x0..x7.";
D16OctonionConjugate::usage = "D16OctonionConjugate[x] is the split-octonion conjugate computed from the Zorn data.";
D16OctonionNorm::usage = "D16OctonionNorm[x] is the Zorn norm ab - u.v.";
D16OctonionLeft::usage = "D16OctonionLeft[x] is the 8x8 matrix of left multiplication y -> x y.";
D16OctonionRight::usage = "D16OctonionRight[x] is the 8x8 matrix of right multiplication y -> y x.";
D16OctonionGammas::usage = "D16OctonionGammas are Gamma(e_a) = [[0, L_{conj e_a}], [L_{e_a}, 0]], a = 0..7.";
D16KOctonion::usage = "D16KOctonion is the primitive integer solution K of gamma^a K == K Gamma(e_a) (octonion picture -> notebook picture).";
D16IntertwinerBasis::usage = "D16IntertwinerBasis[as, bs] is an exact basis of {X : as[[i]].X == X.bs[[i]] for all i}.";
D16PrimitiveInteger::usage = "D16PrimitiveInteger[v] rescales a rational vector or matrix to coprime integers with first nonzero entry positive.";
D16G1Vielbein::usage = "D16G1Vielbein[x] is the general non-diagonal test vielbein e_mu^a = delta + P(x) (rows mu, columns a) at the coordinate list x = {x0..x7}.";
D16G1Points::usage = "D16G1Points are the three exact rational evaluation points p1, p2, p3 of test geometry G1.";
D16RealSymmetricInertia::usage = "D16RealSymmetricInertia[m] is {n+, n-, n0} for an exact real symmetric matrix (Descartes rule on the characteristic polynomial, exact because all roots are real).";
D16NotebookExpression1::usage = "D16NotebookExpression1[] evaluates the literal notebook expression [1] with the notebook definitions.";
D16AlgebraVerification::usage = "D16AlgebraVerification[root] runs every exact algebra check (root = repository root, used to locate the read-only dirac-main reference fixtures) and returns <|\"checks\" -> ..., \"measurements\" -> ...|>.";
D16NamedMatrices::usage = "D16NamedMatrices[] is an association name -> exact matrix of every matrix constructed here.";
D16CompareFixture::usage = "D16CompareFixture[json] compares every matrix found in an imported JSON fixture with this construction.";
D16JSONValue::usage = "D16JSONValue[expr] converts an expression into a JSON-ready value (rationals and complex numbers as strings).";

Begin["`Private`"];

(* ------------------------------------------------------------------------- *)
(* 0. Small exact helpers                                                     *)
(* ------------------------------------------------------------------------- *)

id2 = IdentityMatrix[2];
id4 = IdentityMatrix[4];
id8 = IdentityMatrix[8];
id16 = IdentityMatrix[16];
zeroMatrix[n_Integer] := ConstantArray[0, {n, n}];

zeroQ[m_] := AllTrue[Flatten[{m}], TrueQ[Expand[#] === 0] &];
equalQ[a_, b_] := Dimensions[a] === Dimensions[b] && zeroQ[a - b];
comm[a_, b_] := a.b - b.a;
acomm[a_, b_] := a.b + b.a;
symmetricQ[m_] := equalQ[Transpose[m], m];
antisymmetricQ[m_] := equalQ[Transpose[m], -m];
hermitianQ[m_] := equalQ[ConjugateTranspose[m], m];

D16PrimitiveInteger[v_List] := Module[{flat, dims, scaled, g, first},
  dims = Dimensions[v];
  flat = Flatten[v];
  If[AllTrue[flat, # === 0 &], Return[v]];
  scaled = (LCM @@ (Denominator /@ flat)) flat;
  g = GCD @@ (Abs /@ Select[scaled, # =!= 0 &]);
  scaled = scaled/g;
  first = First[Select[scaled, # =!= 0 &]];
  If[first < 0, scaled = -scaled];
  ArrayReshape[scaled, dims]
];

(* Row-major vectorization: Flatten[A.X.B] == KroneckerProduct[A, Transpose[B]].Flatten[X].
   The linear map X -> A.X - X.B therefore has matrix vecOp[A, B]. *)
vecOp[a_, b_] := KroneckerProduct[a, IdentityMatrix[Length[b]]] -
  KroneckerProduct[IdentityMatrix[Length[a]], Transpose[b]];

(* X -> S^T.X + X.S (invariance of a bilinear form X under the generator S) *)
formOp[s_] := KroneckerProduct[Transpose[s], IdentityMatrix[Length[s]]] +
  KroneckerProduct[IdentityMatrix[Length[s]], Transpose[s]];

nullSpaceData[rows_List, columns_Integer] := Module[{mat, ns, rank},
  mat = SparseArray[rows];
  ns = Normal /@ NullSpace[mat];
  rank = MatrixRank[mat];
  <|"basis" -> ns, "rank" -> rank, "nullity" -> columns - rank,
    "consistent" -> (Length[ns] === columns - rank)|>
];

D16IntertwinerBasis[as_List, bs_List] := Module[{n, m, data},
  n = Length[First[as]]; m = Length[First[bs]];
  data = nullSpaceData[Join @@ MapThread[vecOp, {as, bs}], n m];
  Partition[#, m] & /@ data["basis"]
];

intertwinerData[as_List, bs_List] := Module[{n, m, data, basis, verified},
  n = Length[First[as]]; m = Length[First[bs]];
  data = nullSpaceData[Join @@ MapThread[vecOp, {as, bs}], n m];
  basis = Partition[#, m] & /@ data["basis"];
  verified = AllTrue[basis, Function[x, And @@ MapThread[equalQ[#1.x, x.#2] &, {as, bs}]]];
  <|"basis" -> basis, "dimension" -> data["nullity"],
    "consistent" -> data["consistent"], "basisVerified" -> verified|>
];

formData[ss_List] := Module[{n, data, basis, verified},
  n = Length[First[ss]];
  data = nullSpaceData[Join @@ (formOp /@ ss), n n];
  basis = Partition[#, n] & /@ data["basis"];
  verified = AllTrue[basis, Function[x, AllTrue[ss, equalQ[Transpose[#].x + x.#, 0 x] &]]];
  <|"basis" -> basis, "dimension" -> data["nullity"],
    "consistent" -> data["consistent"], "basisVerified" -> verified|>
];

(* exact inertia of a real symmetric matrix: the characteristic polynomial has only real
   roots, so Descartes' rule of signs counts the positive (and, via x -> -x, negative)
   roots exactly *)
signChanges[coeffs_List] := Module[{c = Select[coeffs, # =!= 0 &]},
  Count[Partition[Sign /@ c, 2, 1], {s1_, s2_} /; s1 s2 < 0]
];
D16RealSymmetricInertia[m_] := Module[{x, p, cl, zeroMult, reduced, pos, neg, n},
  n = Length[m];
  p = Expand[CharacteristicPolynomial[m, x]];
  cl = CoefficientList[p, x];
  zeroMult = LengthWhile[cl, # === 0 &];
  reduced = Drop[cl, zeroMult];
  pos = signChanges[reduced];
  neg = signChanges[MapIndexed[#1 (-1)^(#2[[1]] - 1) &, reduced]];
  {pos, neg, zeroMult}
];

vecCoefficients[m_, gammaList_List, etaDiag_List] :=
  Table[Tr[m.gammaList[[c]]]/(Length[m] etaDiag[[c]]), {c, 1, Length[gammaList]}];

matrixString[m_] := ToString[m, InputForm];

(* deterministic text of a polynomial in the (Module-local) variable v, printed in the variable x *)
polyString[p_, v_Symbol] := StringReplace[ToString[p /. v -> charPolyVariable, InputForm],
  {"Dirac16Complex`Algebra`Private`charPolyVariable" -> "x", "charPolyVariable" -> "x"}];

(* ------------------------------------------------------------------------- *)
(* 1. The notebook (split-octonion block) gammas                              *)
(* ------------------------------------------------------------------------- *)

D16Eta = DiagonalMatrix[{1, 1, 1, 1, -1, -1, -1, -1}];
etaDiagonal = Diagonal[D16Eta];

qa[h_, p_, q_] := Signature[{h, p, q, 4}];
qb[h_, p_, q_] := id4[[p, 4]] id4[[q, h]] - id4[[p, h]] id4[[q, 4]];
s4[h_] := Table[qa[h, p, q] - qb[h, p, q], {p, 1, 4}, {q, 1, 4}];
t4[h_] := Table[qa[h, p, q] + qb[h, p, q], {p, 1, 4}, {q, 1, 4}];

D16Sigma8 = ArrayFlatten[{{0, id4}, {id4, 0}}];

D16Tau = Module[{tau},
  tau[0] = id8;
  Do[tau[h] = ArrayFlatten[{{0, s4[h]}, {s4[h], 0}}], {h, 1, 3}];
  Do[tau[7 - h] = ArrayFlatten[{{0, t4[h]}, {-t4[h], 0}}], {h, 1, 3}];
  tau[7] = tau[1].tau[2].tau[3].tau[4].tau[5].tau[6];
  Table[tau[a], {a, 0, 7}]
];

D16TauBar = Join[{id8}, Table[D16Sigma8.Transpose[D16Tau[[a + 1]]].D16Sigma8, {a, 1, 7}]];

D16Gammas = Table[ArrayFlatten[{{0, D16TauBar[[a + 1]]}, {D16Tau[[a + 1]], 0}}], {a, 0, 7}];

D16C = D16Gammas[[1]].D16Gammas[[2]].D16Gammas[[3]].D16Gammas[[4]];
D16Chirality = Dot @@ D16Gammas;

D16Gamma[a_Integer /; 0 <= a <= 7] := D16Gammas[[a + 1]];
D16Gamma[8] := D16Chirality;

spinTable = Table[
  (D16Gammas[[a + 1]].D16Gammas[[b + 1]] - D16Gammas[[b + 1]].D16Gammas[[a + 1]])/4,
  {a, 0, 7}, {b, 0, 7}
];
D16Spin[a_Integer, b_Integer] := spinTable[[a + 1, b + 1]];
spinPairs = Subsets[Range[0, 7], {2}];
spinGenerators = D16Spin @@@ spinPairs;

D16ProjMinus = (id16 - D16Chirality)/2;
D16ProjPlus = (id16 + D16Chirality)/2;
D16B = -I D16C.D16Gamma[4];

monomialSubsets = Subsets[Range[0, 7]];
D16Monomials = Fold[Dot, id16, D16Gammas[[# + 1]]] & /@ monomialSubsets;

(* ------------------------------------------------------------------------- *)
(* 2. dirac-main tensor-product (Clifford) picture, Learn_dirac-triality 6.2  *)
(* ------------------------------------------------------------------------- *)

pBlock = {{0, 1}, {1, 0}};
nBlock = {{0, 1}, {-1, 0}};
gBlock = {{1, 0}, {0, -1}};
tensorGenerator[k_Integer, block_] := KroneckerProduct @@ Join[
  ConstantArray[gBlock, k - 1], {block}, ConstantArray[id2, 4 - k]
];
D16CliffordPictureGammas = Join[
  Table[tensorGenerator[k, pBlock], {k, 1, 4}],
  Table[tensorGenerator[k, nBlock], {k, 1, 4}]
];
D16CliffordPictureC = Dot @@ D16CliffordPictureGammas[[1 ;; 4]];
D16CliffordPictureVolume = Dot @@ D16CliffordPictureGammas;
ggggVolume = KroneckerProduct[gBlock, gBlock, gBlock, gBlock];

cliffordIntertwiner = intertwinerData[D16CliffordPictureGammas, D16Gammas];
D16KClifford = If[cliffordIntertwiner["dimension"] === 1,
  D16PrimitiveInteger[First[cliffordIntertwiner["basis"]]],
  Missing["IntertwinerNotOneDimensional"]
];

(* ------------------------------------------------------------------------- *)
(* 3. Split octonions from Zorn data (Learn_dirac-triality 10.1, 10.2)        *)
(* ------------------------------------------------------------------------- *)

(* orthogonal coordinates x = (x0,...,x7) -> Zorn data (a, u, v, b):
   a = x0 + x4, b = x0 - x4, u = (x1+x5, x2+x6, x3+x7), v = (-x1+x5, -x2+x6, -x3+x7) *)
toZorn[x_List] := {x[[1]] + x[[5]], x[[2 ;; 4]] + x[[6 ;; 8]], -x[[2 ;; 4]] + x[[6 ;; 8]], x[[1]] - x[[5]]};
fromZorn[{a_, u_List, v_List, b_}] := Join[{(a + b)/2}, (u - v)/2, {(a - b)/2}, (u + v)/2];
(* XY = (ac + u.w, a r + d u - v x w, c v + b w + u x r, v.r + b d) for X=(a,u,v,b), Y=(c,r,w,d) *)
zornProduct[{a_, u_List, v_List, b_}, {c_, r_List, w_List, d_}] := {
  a c + u.w,
  a r + d u - Cross[v, w],
  c v + b w + Cross[u, r],
  v.r + b d
};
zornConjugate[{a_, u_List, v_List, b_}] := {b, -u, -v, a};

D16OctonionProduct[x_List, y_List] := Expand[fromZorn[zornProduct[toZorn[x], toZorn[y]]]];
D16OctonionConjugate[x_List] := Expand[fromZorn[zornConjugate[toZorn[x]]]];
D16OctonionNorm[x_List] := With[{z = toZorn[x]}, Expand[z[[1]] z[[4]] - z[[2]].z[[3]]]];

octBasis = IdentityMatrix[8];
D16OctonionLeft[x_List] := Transpose[Table[D16OctonionProduct[x, octBasis[[j]]], {j, 1, 8}]];
D16OctonionRight[x_List] := Transpose[Table[D16OctonionProduct[octBasis[[j]], x], {j, 1, 8}]];

octLeft = Table[D16OctonionLeft[octBasis[[a + 1]]], {a, 0, 7}];
octLeftConj = Table[D16OctonionLeft[D16OctonionConjugate[octBasis[[a + 1]]]], {a, 0, 7}];
octRight = Table[D16OctonionRight[octBasis[[a + 1]]], {a, 0, 7}];
octRightConj = Table[D16OctonionRight[D16OctonionConjugate[octBasis[[a + 1]]]], {a, 0, 7}];
octMultiplicationTensor = Table[D16OctonionProduct[octBasis[[l]], octBasis[[r]]], {l, 1, 8}, {r, 1, 8}];

D16OctonionGammas = Table[ArrayFlatten[{{0, octLeftConj[[a + 1]]}, {octLeft[[a + 1]], 0}}], {a, 0, 7}];
octRightGammas = Table[ArrayFlatten[{{0, octRightConj[[a + 1]]}, {octRight[[a + 1]], 0}}], {a, 0, 7}];

octonionIntertwiner = intertwinerData[D16Gammas, D16OctonionGammas];
D16KOctonion = If[octonionIntertwiner["dimension"] === 1,
  D16PrimitiveInteger[First[octonionIntertwiner["basis"]]],
  Missing["IntertwinerNotOneDimensional"]
];

(* ------------------------------------------------------------------------- *)
(* 4. Test geometry G1 (general non-diagonal vielbein) - used in QNT checks   *)
(* ------------------------------------------------------------------------- *)

g1P[x_List, mu_Integer, a_Integer] := If[mu =!= a,
  (1/10) ((mu + 1) x[[a + 1]] - (a + 1) x[[mu + 1]]) + (1/20) x[[mu + 1]] x[[a + 1]] +
    (1/30) x[[Mod[mu + a, 8] + 1]]^2,
  (1/10) x[[mu + 1]]^2 + (1/40) x[[Mod[mu + 1, 8] + 1]]
];
D16G1Vielbein[x_List] := Table[KroneckerDelta[mu, a] + g1P[x, mu, a], {mu, 0, 7}, {a, 0, 7}];
D16G1Points = {
  {1/7, -2/9, 1/5, 3/11, -1/13, 2/17, -3/19, 1/23},
  {-1/3, 1/4, 2/7, -1/5, 1/6, -2/11, 1/9, 3/13},
  {2/9, 1/8, -1/7, 1/10, -3/14, 1/12, 2/15, -1/16}
};

(* ------------------------------------------------------------------------- *)
(* 5. The literal notebook expression [1]                                     *)
(* ------------------------------------------------------------------------- *)

(* Verbatim notebook input cells (Pair_Creation_of_Universes_...nb), in dependency order.
   In the notebook, OverBar[tau] and T16^A are Symbolize'd (Notation package) and therefore
   parse as atomic symbols.  Variant "symbolize" reproduces this by rewriting the two
   notation templates to atomic symbols before parsing (what Symbolize does at parse
   time).  Variant "powerUpValue" parses T16^A literally as Power[T16, A] and resolves it
   by an UpValue to one atomic symbol, so that the task's literal input string is used
   unchanged. *)
notebookDefinitionCells = {
  "ID4 = IdentityMatrix[4]; ID8 = IdentityMatrix[8];",
  "ID16 = IdentityMatrix[16];",
  "\[Eta]4488 = ArrayFlatten[{{IdentityMatrix[4], 0}, {0, -IdentityMatrix[4]}}];",
  "\[Sigma] = ArrayFlatten[{{ConstantArray[0, {4, 4}], IdentityMatrix[4]}, {IdentityMatrix[4], ConstantArray[0, {4, 4}]}}];",
  "Qa[h_, p_, q_] := Signature[{h, p, q, 4}]; Qb[h_, p_, q_] := ID4[[p,4]]*ID4[[q,h]] - ID4[[p,h]]*ID4[[q,4]]; SelfDualAntiSymmetric[h_, p_, q_] := Qa[h, p, q] - Qb[h, p, q]; AntiSelfDualAntiSymmetric[h_, p_, q_] := Qa[h, p, q] + Qb[h, p, q];",
  "Do[s4by4[h] = Table[Table[SelfDualAntiSymmetric[h, p, q], {q, 4}], {p, 4}], {h, 1, 3}];",
  "Do[t4by4[h] = Table[Table[AntiSelfDualAntiSymmetric[h, p, q], {q, 4}], {p, 4}], {h, 1, 3}];",
  "\[Tau][0] = ID8; Table[\[Tau][7 - h] = ArrayFlatten[{{0, t4by4[h]}, {-t4by4[h], 0}}], {h, 1, 3}]; Table[\[Tau][h] = ArrayFlatten[{{0, s4by4[h]}, {s4by4[h], 0}}], {h, 1, 3}]; \[Tau][7] = \[Tau][1] . \[Tau][2] . \[Tau][3] . \[Tau][4] . \[Tau][5] . \[Tau][6];",
  "OverBar[\[Tau]][0] = ID8; Do[{OverBar[\[Tau]][A] = FullSimplify[ExpandAll[\[Sigma] . Transpose[\[Tau][A]] . \[Sigma]]]}, {A, 1, 7}];",
  "Table[(T16^A)[A1] = ArrayFlatten[{{0, OverBar[\[Tau]][A1]}, {\[Tau][A1], 0}}], {A1, 0, 7}];",
  "\[Sigma]16 = (T16^A)[0] . (T16^A)[1] . (T16^A)[2] . (T16^A)[3];"
};
notebookExpression1Literal = "\[Sigma]16.(T16^A)[#]==-Transpose[\[Sigma]16.(T16^A)[#]]&/@Range[0,7]";

symbolizedTauBar = "\[Tau]\[UnderBracket]Overbar";
symbolizedT16A = "T16\[UnderBracket]Superscript\[UnderBracket]A";
symbolizeOverBar[s_String] := StringReplace[s, "OverBar[\[Tau]]" -> symbolizedTauBar];
symbolizeAll[s_String] := StringReplace[symbolizeOverBar[s], "(T16^A)" -> symbolizedT16A];

(* The emulation context is isolated ($ContextPath = {ctx, System`}), so a same-named symbol in
   another context (e.g. Global`p of a calling script) cannot interfere; the General::shdw
   warning about such coexisting names is therefore suppressed here and only here. *)
notebookEvaluate[ctx_String, s_String] :=
  Block[{$Context = ctx, $ContextPath = {ctx, "System`"}}, Quiet[ToExpression[s], {General::shdw}]];

notebookRun[variant_String] := Module[{ctx, cells, exprString, result, get, t16, tb, ok},
  ctx = "Dirac16Complex`NotebookEmulation`" <> variant <> "`";
  Quiet[Remove[Evaluate[ctx <> "*"]]];
  cells = Switch[variant,
    "Symbolize", symbolizeAll /@ notebookDefinitionCells,
    "PowerUpValue", Prepend[symbolizeOverBar /@ notebookDefinitionCells,
      "T16 /: Power[T16, A] = " <> symbolizedT16A <> ";"]
  ];
  exprString = Switch[variant,
    "Symbolize", symbolizeAll[notebookExpression1Literal],
    "PowerUpValue", notebookExpression1Literal
  ];
  Scan[notebookEvaluate[ctx, #] &, cells];
  result = notebookEvaluate[ctx, exprString];
  get[name_String] := notebookEvaluate[ctx, name];
  t16 = Table[notebookEvaluate[ctx, symbolizedT16A <> "[" <> ToString[a] <> "]"], {a, 0, 7}];
  tb = Table[notebookEvaluate[ctx, symbolizedTauBar <> "[" <> ToString[a] <> "]"], {a, 0, 7}];
  ok = <|
    "etaMatchesPackage" -> equalQ[get["\[Eta]4488"], D16Eta],
    "sigmaMatchesPackage" -> equalQ[get["\[Sigma]"], D16Sigma8],
    "tauMatchesPackage" -> And @@ Table[equalQ[notebookEvaluate[ctx, "\[Tau][" <> ToString[a] <> "]"], D16Tau[[a + 1]]], {a, 0, 7}],
    "tauBarMatchesPackage" -> And @@ MapThread[equalQ, {tb, D16TauBar}],
    "gammasMatchPackage" -> And @@ MapThread[equalQ, {t16, D16Gammas}],
    "sigma16MatchesPackage" -> equalQ[get["\[Sigma]16"], D16C]
  |>;
  Quiet[Remove[Evaluate[ctx <> "*"]]];
  <|"result" -> result, "evaluatedString" -> exprString, "consistency" -> ok|>
];

D16NotebookExpression1[] := <|
  "Symbolize" -> notebookRun["Symbolize"],
  "PowerUpValue" -> notebookRun["PowerUpValue"]
|>;

(* ------------------------------------------------------------------------- *)
(* 6. Individual checks                                                       *)
(* ------------------------------------------------------------------------- *)

g[a_] := D16Gamma[a];
cMat := D16C;
chir := D16Chirality;
bMat := D16B;

checkClifford[] := Module[{rel, ints, dims},
  rel = Table[equalQ[acomm[g[a], g[b]], 2 D16Eta[[a + 1, b + 1]] id16], {a, 0, 7}, {b, 0, 7}];
  ints = AllTrue[Flatten[D16Gammas], IntegerQ];
  dims = AllTrue[D16Gammas, Dimensions[#] === {16, 16} &];
  <|"pass" -> (And @@ Flatten[rel]) && ints && dims,
    "measurements" -> <|"pairsChecked" -> Length[Flatten[rel]],
      "pairsSatisfied" -> Count[Flatten[rel], True],
      "integerEntries" -> ints,
      "squares" -> Table[With[{sq = g[a].g[a]}, If[equalQ[sq, sq[[1, 1]] id16], sq[[1, 1]], "not scalar"]], {a, 0, 7}]|>|>
];

checkGammaTransposeSymmetry[] := Module[{res},
  res = Table[If[a < 4, symmetricQ[g[a]], antisymmetricQ[g[a]]], {a, 0, 7}];
  <|"pass" -> And @@ res,
    "measurements" -> <|"perGeneratorExpectedSymmetryHolds" -> res,
      "symmetryType" -> Table[Which[symmetricQ[g[a]], "symmetric", antisymmetricQ[g[a]], "antisymmetric", True, "neither"], {a, 0, 7}]|>|>
];

checkChargeMatrix[] := Module[{x, blockForm, prod, charPoly, inertia, eig},
  blockForm = ArrayFlatten[{{-D16Sigma8, 0}, {0, D16Sigma8}}];
  prod = g[0].g[1].g[2].g[3];
  charPoly = Expand[CharacteristicPolynomial[cMat, x]];
  inertia = D16RealSymmetricInertia[cMat];
  eig = Sort[Eigenvalues[cMat]];
  <|"pass" -> equalQ[cMat, prod] && equalQ[prod, blockForm] && symmetricQ[cMat] &&
      equalQ[cMat.cMat, id16] && inertia === {8, 8, 0} &&
      charPoly === Expand[(x - 1)^8 (x + 1)^8] && eig === Join[ConstantArray[-1, 8], ConstantArray[1, 8]],
    "measurements" -> <|"equalsGamma0123" -> equalQ[cMat, prod],
      "equalsBlockDiagMinusSigmaSigma" -> equalQ[prod, blockForm],
      "symmetric" -> symmetricQ[cMat], "squareIsIdentity" -> equalQ[cMat.cMat, id16],
      "signature" -> Take[inertia, 2], "zeroEigenvalues" -> inertia[[3]],
      "characteristicPolynomial" -> polyString[Factor[charPoly], x],
      "eigenvalues" -> eig|>|>
];

checkExpression1[] := Module[{direct, nb, sym, pow, symOK, powOK},
  direct = Table[equalQ[Transpose[cMat.g[a]], -cMat.g[a]], {a, 0, 7}];
  nb = D16NotebookExpression1[];
  sym = nb["Symbolize"]; pow = nb["PowerUpValue"];
  symOK = sym["result"] === ConstantArray[True, 8] && And @@ Values[sym["consistency"]];
  powOK = pow["result"] === ConstantArray[True, 8] && And @@ Values[pow["consistency"]];
  <|"pass" -> (direct === ConstantArray[True, 8]) && symOK && powOK,
    "measurements" -> <|
      "list" -> direct,
      "listWolframForm" -> ToString[direct, InputForm],
      "literalInput" -> notebookExpression1Literal,
      "literalResultSymbolizeEmulation" -> sym["result"],
      "literalEvaluatedStringSymbolizeEmulation" -> sym["evaluatedString"],
      "notebookDefinitionsMatchPackageSymbolizeEmulation" -> sym["consistency"],
      "literalResultPowerUpValue" -> pow["result"],
      "notebookDefinitionsMatchPackagePowerUpValue" -> pow["consistency"],
      "notebookCellsEvaluated" -> Length[notebookDefinitionCells],
      "note" -> "Notebook definition cells are evaluated verbatim in an isolated context. The notebook Symbolize's OverBar[tau] and T16^A (Notation package); variant Symbolize rewrites these templates to atomic symbols before parsing, variant PowerUpValue parses the task's literal string unchanged with T16^A = Power[T16,A] resolved by an UpValue to the same atomic symbol."
    |>|>
];

checkSpinTransposeProperties[] := Module[{p1, p2, p3, vecRel, lieRel},
  p1 = Table[antisymmetricQ[cMat.D16Spin[a, b]], {a, 0, 7}, {b, 0, 7}];
  p2 = Table[symmetricQ[cMat.acomm[g[c], D16Spin[a, b]]], {c, 0, 7}, {a, 0, 7}, {b, 0, 7}];
  p3 = Table[antisymmetricQ[cMat.comm[g[c], D16Spin[a, b]]], {c, 0, 7}, {a, 0, 7}, {b, 0, 7}];
  (* supplementary (recorded, not part of the pass condition): so(4,4) relations of S^{ab} *)
  vecRel = And @@ Flatten[Table[equalQ[comm[D16Spin[a, b], g[c]],
      D16Eta[[b + 1, c + 1]] g[a] - D16Eta[[a + 1, c + 1]] g[b]], {a, 0, 7}, {b, 0, 7}, {c, 0, 7}]];
  lieRel = And @@ Flatten[Table[equalQ[comm[D16Spin[a, b], D16Spin[c, d]],
      D16Eta[[b + 1, c + 1]] D16Spin[a, d] - D16Eta[[a + 1, c + 1]] D16Spin[b, d] -
      D16Eta[[b + 1, d + 1]] D16Spin[a, c] + D16Eta[[a + 1, d + 1]] D16Spin[b, c]],
    {a, 0, 7}, {b, 0, 7}, {c, 0, 7}, {d, 0, 7}]];
  <|"pass" -> (And @@ Flatten[p1]) && (And @@ Flatten[p2]) && (And @@ Flatten[p3]),
    "measurements" -> <|
      "cSpinAntisymmetricPairs" -> Count[Flatten[p1], True], "pairsChecked" -> Length[Flatten[p1]],
      "cAnticommutatorSymmetricTriples" -> Count[Flatten[p2], True],
      "cCommutatorAntisymmetricTriples" -> Count[Flatten[p3], True], "triplesChecked" -> Length[Flatten[p3]],
      "supplementarySpinVectorRelation" -> "[S^{ab}, gamma^c] = eta^{bc} gamma^a - eta^{ac} gamma^b",
      "supplementarySpinVectorRelationHolds" -> vecRel,
      "supplementaryLieRelationsHold" -> lieRel|>|>
];

checkChirality[] := Module[{expected, sq, anti, spinComm, cComm},
  expected = ArrayFlatten[{{-id8, 0}, {0, id8}}];
  sq = equalQ[chir.chir, id16];
  anti = Table[zeroQ[acomm[chir, g[a]]], {a, 0, 7}];
  spinComm = Table[zeroQ[comm[chir, D16Spin[a, b]]], {a, 0, 7}, {b, 0, 7}];
  cComm = zeroQ[comm[chir, cMat]];
  <|"pass" -> equalQ[chir, expected] && sq && (And @@ anti) && (And @@ Flatten[spinComm]) && cComm,
    "measurements" -> <|"equalsDiagMinusI8PlusI8" -> equalQ[chir, expected],
      "squareIsIdentity" -> sq, "anticommutesWithGammas" -> anti,
      "commutesWithAllSpin" -> And @@ Flatten[spinComm], "commutesWithC" -> cComm,
      "upperBlockChirality" -> Union[Diagonal[chir][[1 ;; 8]]], "lowerBlockChirality" -> Union[Diagonal[chir][[9 ;; 16]]]|>|>
];

checkFaithful[] := Module[{full, even, evenMon},
  full = MatrixRank[Flatten /@ D16Monomials];
  evenMon = Pick[D16Monomials, EvenQ[Length[#]] & /@ monomialSubsets];
  even = MatrixRank[Flatten /@ evenMon];
  <|"pass" -> Length[D16Monomials] === 256 && full === 256 && Length[evenMon] === 128 && even === 128,
    "measurements" -> <|"monomialCount" -> Length[D16Monomials], "fullRank" -> full,
      "evenMonomialCount" -> Length[evenMon], "evenRank" -> even|>|>
];

vecIdentityHolds[] := Module[{a, b, x, a8, b8, x8},
  a = g[0] + 2 g[5] + 3 g[2].g[7]; b = g[3].g[6] - g[1];
  x = Table[Mod[3 i + 5 j + i j, 7] - 3, {i, 1, 16}, {j, 1, 16}];
  a8 = D16Tau[[3]] + 2 D16TauBar[[6]]; b8 = D16Sigma8 - D16Tau[[8]];
  x8 = Table[Mod[2 i + 7 j + i j, 5] - 2, {i, 1, 8}, {j, 1, 8}];
  equalQ[Flatten[a.x.b], KroneckerProduct[a, Transpose[b]].Flatten[x]] &&
    equalQ[Flatten[a.x - x.b], vecOp[a, b].Flatten[x]] &&
    equalQ[Flatten[Transpose[b].x + x.b], formOp[b].Flatten[x]] &&
    equalQ[Flatten[a8.x8.b8], KroneckerProduct[a8, Transpose[b8]].Flatten[x8]]
];

checkPinIrreducibleComplex[] := Module[{data, basis, isId, vecOK},
  vecOK = vecIdentityHolds[];
  data = intertwinerData[D16Gammas, D16Gammas];
  basis = data["basis"];
  isId = data["dimension"] === 1 && Module[{m = First[basis]}, equalQ[m, m[[1, 1]] id16] && m[[1, 1]] =!= 0];
  <|"pass" -> vecOK && data["consistent"] && data["basisVerified"] && data["dimension"] === 1 && isId,
    "measurements" -> <|"commutantDimension" -> data["dimension"],
      "commutantIsScalars" -> isId, "linearizationIdentityVerified" -> vecOK,
      "field" -> "Q (exact rational null space of an integer coefficient matrix)",
      "complexificationNote" -> "The coefficient matrix is rational; its rank, hence the solution dimension, is unchanged by extension of scalars Q -> C, so the complex commutant of {gamma^a} in Mat16(C) is 1-dimensional (Schur: C^16 is an irreducible complex Pin(4,4)/Cl(4,4) module)."|>|>
];

checkSpinDecomposition[] := Module[{full, basisOK, blockDiag, minusSpin, plusSpin, cm, cp,
    evenMon, evenBlocksDiag, rankMinus, rankPlus, crossMP, crossPM},
  full = intertwinerData[spinGenerators, spinGenerators];
  basisOK = full["dimension"] === 2 &&
    MatrixRank[Join[Flatten /@ full["basis"], {Flatten[D16ProjMinus], Flatten[D16ProjPlus]}]] === 2;
  blockDiag = AllTrue[spinGenerators, zeroQ[#[[1 ;; 8, 9 ;; 16]]] && zeroQ[#[[9 ;; 16, 1 ;; 8]]] &];
  minusSpin = #[[1 ;; 8, 1 ;; 8]] & /@ spinGenerators;
  plusSpin = #[[9 ;; 16, 9 ;; 16]] & /@ spinGenerators;
  cm = intertwinerData[minusSpin, minusSpin];
  cp = intertwinerData[plusSpin, plusSpin];
  evenMon = Pick[D16Monomials, EvenQ[Length[#]] & /@ monomialSubsets];
  evenBlocksDiag = AllTrue[evenMon, zeroQ[#[[1 ;; 8, 9 ;; 16]]] && zeroQ[#[[9 ;; 16, 1 ;; 8]]] &];
  rankMinus = MatrixRank[Flatten[#[[1 ;; 8, 1 ;; 8]]] & /@ evenMon];
  rankPlus = MatrixRank[Flatten[#[[9 ;; 16, 9 ;; 16]]] & /@ evenMon];
  crossMP = intertwinerData[minusSpin, plusSpin];
  crossPM = intertwinerData[plusSpin, minusSpin];
  <|"pass" -> full["consistent"] && full["basisVerified"] && basisOK && blockDiag &&
      cm["dimension"] === 1 && cp["dimension"] === 1 && cm["basisVerified"] && cp["basisVerified"] &&
      evenBlocksDiag && rankMinus === 64 && rankPlus === 64 &&
      crossMP["dimension"] === 0 && crossPM["dimension"] === 0,
    "measurements" -> <|"spinCommutantDimension" -> full["dimension"],
      "spinCommutantSpannedByChiralProjectors" -> basisOK,
      "spinGeneratorsBlockDiagonal" -> blockDiag,
      "blockCommutantDimensions" -> {cm["dimension"], cp["dimension"]},
      "blockOrder" -> "{upper spinor indices 0..7 (chirality -1), lower spinor indices 8..15 (chirality +1)}",
      "evenAlgebraBlockDiagonal" -> evenBlocksDiag,
      "blockEvenAlgebraRanks" -> {rankMinus, rankPlus},
      "crossIntertwinerDimensions" -> {crossMP["dimension"], crossPM["dimension"]},
      "conclusion" -> "C^16 = C^8_- (+) C^8_+ as Spin(4,4) modules; each summand irreducible over C (commutant 1, even algebra = End(C^8)) and the two are inequivalent (cross intertwiners 0)."|>|>
];

diracMainFile[root_, name_] := FileNameJoin[{root, "dirac-main", "artifacts", "exact", name}];

checkCliffordPictureIntertwiner[root_] := Module[{rel, k, kInv, rankK, cOK, volTransformed,
    volSign, dmFile, dmData, dmAgree, dmVolAgree, coprime, firstPos, plusIdx, minusIdx, mapIdx},
  rel = And @@ Flatten[Table[equalQ[acomm[D16CliffordPictureGammas[[a + 1]], D16CliffordPictureGammas[[b + 1]]],
      2 D16Eta[[a + 1, b + 1]] id16], {a, 0, 7}, {b, 0, 7}]];
  k = D16KClifford;
  If[MissingQ[k],
    Return[<|"pass" -> False, "measurements" -> <|"intertwinerDimension" -> cliffordIntertwiner["dimension"]|>|>, Module]];
  rankK = MatrixRank[k];
  kInv = Inverse[k];
  cOK = equalQ[k.cMat.kInv, D16CliffordPictureC];
  volTransformed = k.chir.kInv;
  volSign = Which[equalQ[volTransformed, ggggVolume], 1, equalQ[volTransformed, -ggggVolume], -1, True, 0];
  coprime = (GCD @@ Flatten[k]) === 1;
  firstPos = First[Select[Flatten[k], # =!= 0 &]] > 0;
  dmFile = diracMainFile[root, "cl44-seed.json"];
  If[FileExistsQ[dmFile],
    dmData = Import[dmFile, "RawJSON"];
    dmAgree = dmData["generators"] === D16CliffordPictureGammas;
    dmVolAgree = dmData["volumeElement"] === D16CliffordPictureVolume,
    dmAgree = "not-run"; dmVolAgree = "not-run"
  ];
  plusIdx = Flatten[Position[Diagonal[D16CliffordPictureVolume], 1]] - 1;
  minusIdx = Flatten[Position[Diagonal[D16CliffordPictureVolume], -1]] - 1;
  (* image of the notebook chiral blocks under K: supports of K.P_- and K.P_+ columns *)
  mapIdx = {Union[Position[k.D16ProjMinus, x_ /; x =!= 0, {2}, Heads -> False][[All, 1]]] - 1,
    Union[Position[k.D16ProjPlus, x_ /; x =!= 0, {2}, Heads -> False][[All, 1]]] - 1};
  <|"pass" -> rel && cliffordIntertwiner["dimension"] === 1 && cliffordIntertwiner["consistent"] &&
      cliffordIntertwiner["basisVerified"] && rankK === 16 && coprime && firstPos &&
      (And @@ Table[equalQ[D16CliffordPictureGammas[[a + 1]].k, k.g[a]], {a, 0, 7}]) && cOK &&
      equalQ[D16CliffordPictureVolume, ggggVolume] && volSign =!= 0 &&
      (dmAgree === True || dmAgree === "not-run") && (dmVolAgree === True || dmVolAgree === "not-run"),
    "measurements" -> <|"cliffordRelationsTensorPicture" -> rel,
      "intertwinerDimension" -> cliffordIntertwiner["dimension"],
      "intertwinerEquation" -> "gammaHat^a . K == K . gamma^a (K maps the notebook picture to the dirac-main tensor picture)",
      "rank" -> rankK, "primitiveEntriesCoprime" -> coprime, "firstNonzeroPositive" -> firstPos,
      "KCKinverseEqualsCdm" -> cOK,
      "diracMainVolumeEqualsGGGG" -> equalQ[D16CliffordPictureVolume, ggggVolume],
      "volumeElementSign" -> volSign,
      "volumeElementStatement" -> "K.gamma8.Inverse[K] == (" <> ToString[volSign] <> ") G(x)G(x)G(x)G",
      "diracMainPlusIndicesZeroBased" -> plusIdx, "diracMainMinusIndicesZeroBased" -> minusIdx,
      "imageOfNotebookMinusAndPlusBlocks" -> mapIdx,
      "matchesDiracMainCl44SeedGenerators" -> dmAgree,
      "matchesDiracMainCl44SeedVolumeElement" -> dmVolAgree|>|>
];

scaledSignedPermutationQ[m_] := Module[{nz = Select[Flatten[m], # =!= 0 &]},
  Length[nz] === Length[m] && Length[Union[Abs /@ nz]] === 1 &&
    AllTrue[m, Count[#, x_ /; x =!= 0] === 1 &] && AllTrue[Transpose[m], Count[#, x_ /; x =!= 0] === 1 &]
];
signedPermutationDescription[m_] := Module[{s = First[Select[Flatten[m], # =!= 0 &]]},
  Table[With[{j = First[FirstPosition[m[[i]], x_ /; x =!= 0, Missing[], {1}, Heads -> False]]},
    {i - 1, j - 1, Sign[m[[i, j]]] Sign[s]}], {i, 1, Length[m]}]
];

checkOctonionPictureIntertwiner[root_] := Module[{e, xs, ys, xv, yv, unitOK, examples, assoc, normComp,
    normQuad, conjOK, conjRev, nonzeroSC, rel, k, rankK, kOK, dmFile, dmData, dmAgree, tauEqL, tauBarEqLc,
    tauEqR, blockType, qB, rB, qPerm, rPerm, qPropR, tauFromBlocks, octVol, relR, rightInt, findings,
    jsonGammasAgree, triFile, triData, triGammasAgree, triKAgree, triKIntertwines, composedK, rEqualsQ, qtq, qtq2,
    qsq, qsqFactor, tauConj, qAnalysis},
  e[i_] := octBasis[[i + 1]];
  xv = Array[xs, 8, 0]; yv = Array[ys, 8, 0];
  unitOK = AllTrue[Range[0, 7], D16OctonionProduct[e[0], e[#]] === e[#] && D16OctonionProduct[e[#], e[0]] === e[#] &];
  examples = <|
    "e1e1=-e0" -> (D16OctonionProduct[e[1], e[1]] === -e[0]),
    "e4e4=e0" -> (D16OctonionProduct[e[4], e[4]] === e[0]),
    "e1e2=-e3" -> (D16OctonionProduct[e[1], e[2]] === -e[3]),
    "e2e1=e3" -> (D16OctonionProduct[e[2], e[1]] === e[3]),
    "e1e4=-e5" -> (D16OctonionProduct[e[1], e[4]] === -e[5]),
    "e4e1=e5" -> (D16OctonionProduct[e[4], e[1]] === e[5])
  |>;
  assoc = D16OctonionProduct[D16OctonionProduct[e[1], e[2]], e[4]] - D16OctonionProduct[e[1], D16OctonionProduct[e[2], e[4]]];
  normQuad = Expand[D16OctonionNorm[xv] - xv.D16Eta.xv] === 0;
  normComp = Expand[D16OctonionNorm[D16OctonionProduct[xv, yv]] - D16OctonionNorm[xv] D16OctonionNorm[yv]] === 0;
  conjOK = Table[D16OctonionConjugate[e[a]], {a, 0, 7}] === Table[If[a == 0, 1, -1] e[a], {a, 0, 7}];
  conjRev = zeroQ[D16OctonionConjugate[D16OctonionProduct[xv, yv]] -
      D16OctonionProduct[D16OctonionConjugate[yv], D16OctonionConjugate[xv]]];
  nonzeroSC = Count[Flatten[octMultiplicationTensor], x_ /; x =!= 0];
  rel = And @@ Flatten[Table[equalQ[acomm[D16OctonionGammas[[a + 1]], D16OctonionGammas[[b + 1]]],
      2 D16Eta[[a + 1, b + 1]] id16], {a, 0, 7}, {b, 0, 7}]];
  dmFile = diracMainFile[root, "split-octonion.json"];
  dmAgree = If[FileExistsQ[dmFile],
    dmData = Import[dmFile, "RawJSON"];
    dmData["multiplicationTensor"] === octMultiplicationTensor,
    "not-run"];
  (* Gamma_a built directly from dirac-main's stored integer structure tensor *)
  jsonGammasAgree = If[FileExistsQ[dmFile],
    Module[{tensor = dmData["multiplicationTensor"], leftJ, conjSigns = {1, -1, -1, -1, -1, -1, -1, -1}},
      leftJ = Table[Transpose[Table[tensor[[a + 1, j]], {j, 1, 8}]], {a, 0, 7}];
      Table[ArrayFlatten[{{0, conjSigns[[a + 1]] leftJ[[a + 1]]}, {leftJ[[a + 1]], 0}}], {a, 0, 7}] === D16OctonionGammas],
    "not-run"];
  (* dirac-main's published octonion Clifford generators and octonion -> tensor intertwiner *)
  triFile = diracMainFile[root, "triality44.json"];
  If[FileExistsQ[triFile] && !MissingQ[D16KOctonion] && !MissingQ[D16KClifford],
    triData = Import[triFile, "RawJSON"];
    triGammasAgree = triData["octonionCliffordGenerators"] === D16OctonionGammas;
    composedK = D16PrimitiveInteger[D16KClifford.D16KOctonion];
    triKAgree = triData["canonicalCliffordIntertwiner"] === composedK;
    triKIntertwines = And @@ Table[equalQ[D16CliffordPictureGammas[[a + 1]].triData["canonicalCliffordIntertwiner"],
        triData["canonicalCliffordIntertwiner"].D16OctonionGammas[[a + 1]]], {a, 0, 7}],
    triGammasAgree = "not-run"; triKAgree = "not-run"; triKIntertwines = "not-run"
  ];
  k = D16KOctonion;
  If[MissingQ[k],
    rankK = 0; kOK = False; blockType = "none"; qPerm = False; rPerm = False; qPropR = False; tauFromBlocks = False,
    rankK = MatrixRank[k];
    kOK = And @@ Table[equalQ[g[a].k, k.D16OctonionGammas[[a + 1]]], {a, 0, 7}];
    blockType = Which[
      zeroQ[k[[1 ;; 8, 9 ;; 16]]] && zeroQ[k[[9 ;; 16, 1 ;; 8]]], "block-diagonal",
      zeroQ[k[[1 ;; 8, 1 ;; 8]]] && zeroQ[k[[9 ;; 16, 9 ;; 16]]], "block-antidiagonal",
      True, "mixed"];
    If[blockType === "block-diagonal",
      qB = k[[1 ;; 8, 1 ;; 8]]; rB = k[[9 ;; 16, 9 ;; 16]];
      qPerm = scaledSignedPermutationQ[qB]; rPerm = scaledSignedPermutationQ[rB];
      qPropR = MatrixRank[{Flatten[qB], Flatten[rB]}] === 1;
      tauFromBlocks = And @@ Table[equalQ[D16Tau[[a + 1]], rB.octLeft[[a + 1]].Inverse[qB]] &&
          equalQ[D16TauBar[[a + 1]], qB.octLeftConj[[a + 1]].Inverse[rB]], {a, 0, 7}];
      rEqualsQ = equalQ[rB, qB];
      tauConj = And @@ Table[equalQ[D16Tau[[a + 1]], qB.octLeft[[a + 1]].Inverse[qB]], {a, 0, 7}];
      qtq = Transpose[qB].qB;
      qtq2 = qB.Transpose[qB];
      qsq = Transpose[qB].D16Sigma8.qB;
      qsqFactor = If[qsq[[1, 1]] =!= 0 && equalQ[qsq, qsq[[1, 1]] D16Eta], qsq[[1, 1]], "not proportional to eta"];
      qAnalysis = <|
        "Q" -> qB, "RequalsQ" -> rEqualsQ, "tauEqualsQLQinv" -> tauConj,
        "nonzeroEntriesPerRowOfQ" -> Union[Count[#, x_ /; x =!= 0] & /@ qB],
        "QtransposeQ" -> If[equalQ[qtq, qtq[[1, 1]] id8], ToString[qtq[[1, 1]]] <> " I8", qtq],
        "QQtranspose" -> If[equalQ[qtq2, qtq2[[1, 1]] id8], ToString[qtq2[[1, 1]]] <> " I8", qtq2],
        "QtransposeSigmaQOverEta" -> qsqFactor,
        "interpretation" -> If[rEqualsQ && tauConj && !TrueQ[qPerm] && equalQ[qtq, 2 id8] && qsqFactor === 2 &&
            Union[Count[#, x_ /; x =!= 0] & /@ qB] === {2} && Union[Abs[Flatten[qB]]] === {0, 1},
          "tau[a] = Q L_{e_a} Q^-1 and taubar[a] = Q L_{conj e_a} Q^-1 with one and the same Q in both chiral blocks (K_octonion = diag(Q, Q)). Q is not a (scaled) signed permutation: it is a +-1 matrix with two nonzero entries per row and column, Q^T Q = 2 I8, and Q^T sigma Q = 2 eta, i.e. the notebook's 8-space basis is a null (light-cone) basis in which the split-octonion norm eta appears as sigma/2.",
          "see the computed fields (the expected light-cone structure was not found)"]
      |>,
      qPerm = False; rPerm = False; qPropR = False; tauFromBlocks = False; qAnalysis = "intertwiner not block-diagonal"
    ]
  ];
  octVol = Dot @@ D16OctonionGammas;
  tauEqL = Table[equalQ[D16Tau[[a + 1]], octLeft[[a + 1]]], {a, 0, 7}];
  tauBarEqLc = Table[equalQ[D16TauBar[[a + 1]], octLeftConj[[a + 1]]], {a, 0, 7}];
  tauEqR = Table[equalQ[D16Tau[[a + 1]], octRight[[a + 1]]], {a, 0, 7}];
  relR = And @@ Flatten[Table[equalQ[acomm[octRightGammas[[a + 1]], octRightGammas[[b + 1]]],
      2 D16Eta[[a + 1, b + 1]] id16], {a, 0, 7}, {b, 0, 7}]];
  rightInt = intertwinerData[D16Gammas, octRightGammas];
  findings = <|
    "tauEqualsLeftMultiplication" -> tauEqL,
    "notebookBasisChange" -> qAnalysis,
    "tauBarEqualsLeftMultiplicationByConjugate" -> tauBarEqLc,
    "tauEqualsRightMultiplication" -> tauEqR,
    "intertwinerBlockType" -> blockType,
    "upperBlockQIsScaledSignedPermutation" -> qPerm,
    "lowerBlockRIsScaledSignedPermutation" -> rPerm,
    "QProportionalToR" -> qPropR,
    "tauEqualsRLQinvAndTauBarEqualsQLbarRinv" -> tauFromBlocks,
    "signedPermutationQ" -> If[TrueQ[qPerm], signedPermutationDescription[qB], "not a signed permutation"],
    "signedPermutationR" -> If[TrueQ[rPerm], signedPermutationDescription[rB], "not a signed permutation"],
    "octonionPictureVolumeElementDiagonal" -> If[DiagonalMatrixQ[octVol], Diagonal[octVol], "not diagonal"],
    "rightMultiplicationPictureCliffordRelations" -> relR,
    "rightMultiplicationPictureIntertwinerDimension" -> rightInt["dimension"],
    "rightMultiplicationPictureIntertwinerRank" -> If[rightInt["dimension"] === 1, MatrixRank[First[rightInt["basis"]]], "n/a"]
  |>;
  <|"pass" -> unitOK && (And @@ Values[examples]) && assoc === 2 e[7] && normQuad && normComp && conjOK &&
      conjRev && nonzeroSC === 64 && rel && (dmAgree === True || dmAgree === "not-run") &&
      (jsonGammasAgree === True || jsonGammasAgree === "not-run") &&
      (triGammasAgree === True || triGammasAgree === "not-run") &&
      (triKAgree === True || triKAgree === "not-run") && (triKIntertwines === True || triKIntertwines === "not-run") &&
      octonionIntertwiner["dimension"] === 1 && octonionIntertwiner["consistent"] &&
      octonionIntertwiner["basisVerified"] && rankK === 16 && TrueQ[kOK],
    "measurements" -> Join[<|
      "unitLaw" -> unitOK, "workedExamplesW9" -> examples,
      "associatorE1E2E4" -> assoc, "associatorEquals2e7" -> (assoc === 2 e[7]),
      "normIsEtaQuadraticForm" -> normQuad, "normComposition" -> normComp,
      "conjugationFixesE0NegatesOthers" -> conjOK, "conjugationReversesProducts" -> conjRev,
      "nonzeroStructureConstants" -> nonzeroSC,
      "matchesDiracMainSplitOctonionMultiplicationTensor" -> dmAgree,
      "gammasFromDiracMainSplitOctonionJsonEqualRebuilt" -> jsonGammasAgree,
      "matchesDiracMainTriality44OctonionCliffordGenerators" -> triGammasAgree,
      "diracMainCanonicalIntertwinerEqualsPrimitiveKcliffordKoctonion" -> triKAgree,
      "diracMainCanonicalIntertwinerVerified" -> triKIntertwines,
      "cliffordRelationsSameEta" -> rel,
      "intertwinerEquation" -> "gamma^a . K == K . Gamma(e_a) (K maps the octonion picture to the notebook picture)",
      "intertwinerDimension" -> octonionIntertwiner["dimension"],
      "rank" -> rankK, "intertwinerVerified" -> kOK|>, findings]|>
];

checkChargeFormB[] := Module[{x, eig, cp},
  eig = Sort[Eigenvalues[bMat]];
  cp = Expand[CharacteristicPolynomial[bMat, x]];
  <|"pass" -> hermitianQ[bMat] && equalQ[bMat.bMat, id16] &&
      eig === Join[ConstantArray[-1, 8], ConstantArray[1, 8]] && cp === Expand[(x - 1)^8 (x + 1)^8] &&
      zeroQ[comm[cMat, bMat]] && equalQ[bMat.cMat, -I g[4]],
    "measurements" -> <|"hermitian" -> hermitianQ[bMat], "squareIsIdentity" -> equalQ[bMat.bMat, id16],
      "eigenvalues" -> eig, "characteristicPolynomial" -> polyString[Factor[cp], x],
      "commutesWithC" -> zeroQ[comm[cMat, bMat]], "BCEqualsMinusIGamma4" -> equalQ[bMat.cMat, -I g[4]]|>|>
];

checkInvariantForms[] := Module[{data, cpm, cpp, spanOK, blockDiag, al, be, a1, a2, b1, b2, c1, c2, hC, hDiff,
    hermOnlyReal, h, hg4, offDiag, z, similarToMinus, trZero, sqr, cc, mc, kk, mcOffDiag, mcSq, y, yInvertible,
    yOrth, kExpected, kConj, mcStructure},
  data = formData[spinGenerators];
  cpm = cMat.D16ProjMinus; cpp = cMat.D16ProjPlus;
  spanOK = data["dimension"] === 2 &&
    MatrixRank[Join[Flatten /@ data["basis"], {Flatten[cpm], Flatten[cpp]}]] === 2 &&
    AllTrue[{cpm, cpp}, Function[m, AllTrue[spinGenerators, equalQ[Transpose[#].m + m.#, 0 m] &]]];
  blockDiag = AllTrue[{cpm, cpp}, zeroQ[#[[1 ;; 8, 9 ;; 16]]] && zeroQ[#[[9 ;; 16, 1 ;; 8]]] &];
  (* general complex invariant sesquilinear form: generators are real, so S^dagger H + H S = 0
     is the same linear equation; H = alpha C.P- + beta C.P+ with alpha = a1 + I a2, beta = b1 + I b2 *)
  hC = (a1 + I a2) cpm + (b1 + I b2) cpp;
  hDiff = ComplexExpand[hC - ConjugateTranspose[hC]];
  hermOnlyReal = zeroQ[hDiff - 2 I (a2 cpm + b2 cpp)] &&
    MatrixRank[{Flatten[cpm], Flatten[cpp]}] === 2;
  (* Hermitian family: alpha, beta real *)
  h = al cpm + be cpp;
  hg4 = h.g[4];
  offDiag = zeroQ[hg4[[1 ;; 8, 1 ;; 8]]] && zeroQ[hg4[[9 ;; 16, 9 ;; 16]]];
  z = ArrayFlatten[{{id8, 0}, {0, -id8}}];
  similarToMinus = equalQ[z.hg4.z, -hg4];
  trZero = Expand[Tr[hg4]] === 0;
  sqr = equalQ[hg4.hg4, -al be id16];
  (* Hermitian density matrix of any phase c = c1 + I c2 times the form: Herm(c H gamma^4) *)
  cc = c1 + I c2;
  mc = ComplexExpand[(cc hg4 + ConjugateTranspose[cc hg4])/2];
  mcOffDiag = zeroQ[mc[[1 ;; 8, 1 ;; 8]]] && zeroQ[mc[[9 ;; 16, 9 ;; 16]]];
  y = Transpose[D16Tau[[5]]].D16Sigma8;
  kExpected = ((c1 - I c2) be - (c1 + I c2) al)/2;
  kConj = ComplexExpand[Conjugate[kExpected]];
  mcStructure = zeroQ[ComplexExpand[mc - ArrayFlatten[{{0, kExpected y}, {kConj Transpose[y], 0}}]]];
  yInvertible = MatrixRank[y] === 8;
  yOrth = equalQ[Transpose[y].y, id8];
  kk = ComplexExpand[kExpected kConj];
  mcSq = zeroQ[ComplexExpand[mc.mc] - Expand[kk] id16];
  <|"pass" -> data["consistent"] && data["basisVerified"] && spanOK && blockDiag && hermOnlyReal && offDiag &&
      similarToMinus && trZero && sqr && mcOffDiag && mcStructure && yInvertible && yOrth && mcSq &&
      zeroQ[ComplexExpand[Tr[mc]]],
    "measurements" -> <|"invariantBilinearFormDimension" -> data["dimension"],
      "basisIsCPminusCPplus" -> spanOK, "basisBlockDiagonalInChirality" -> blockDiag,
      "hermitianIffAlphaBetaReal" -> hermOnlyReal,
      "Hgamma4BlockOffDiagonal" -> offDiag, "Hgamma4SimilarToMinusItself" -> similarToMinus,
      "Hgamma4Traceless" -> trZero, "Hgamma4Squared" -> "-alpha beta I16",
      "Hgamma4SquaredVerified" -> sqr,
      "Hgamma4Eigenvalues" -> "for alpha beta != 0: (H gamma^4)^2 = -alpha beta I16 makes H gamma^4 diagonalizable with eigenvalues +-sqrt(-alpha beta); similarity to its negative (Z = diag(I8,-I8)) gives multiplicity 8 each",
      "hermitianDensityOffDiagonal" -> mcOffDiag,
      "hermitianDensityFormula" -> "Herm(c H gamma^4) = [[0, k Y], [conj(k) Y^T, 0]], Y = tau[4]^T sigma, k = (conj(c) beta - c alpha)/2",
      "hermitianDensityFormulaVerified" -> mcStructure,
      "YSignedOrthogonal" -> yOrth,
      "hermitianDensitySquare" -> "|k|^2 I16", "hermitianDensitySquareVerified" -> mcSq,
      "conclusion" -> "For every Spin(4,4)-invariant Hermitian form H = alpha C.P- + beta C.P+ (alpha, beta real) and every constant c, the charge-density matrix Herm(c H gamma^4) is traceless with square |k|^2 I16, hence has eigenvalues +|k| (x8) and -|k| (x8): signature (8,8), indefinite, unless it vanishes identically."|>|>
];

checkGamma8Map[] := Module[{adjOK, kinSigns, massSign, spinOK, cSpinOK, kin, mass, lam, s, m, lag, transformed, withU, freeOK},
  adjOK = equalQ[Transpose[chir].cMat, cMat.chir] && symmetricQ[chir];
  kinSigns = Table[Which[equalQ[Transpose[chir].cMat.g[a].chir, -cMat.g[a]], -1,
      equalQ[Transpose[chir].cMat.g[a].chir, cMat.g[a]], 1, True, 0], {a, 0, 7}];
  massSign = Which[equalQ[Transpose[chir].cMat.chir, cMat], 1, equalQ[Transpose[chir].cMat.chir, -cMat], -1, True, 0];
  spinOK = And @@ Flatten[Table[zeroQ[comm[chir, D16Spin[a, b]]], {a, 0, 7}, {b, 0, 7}]];
  cSpinOK = And @@ Flatten[Table[equalQ[Transpose[chir].cMat.D16Spin[a, b].chir, cMat.D16Spin[a, b]], {a, 0, 7}, {b, 0, 7}]];
  (* Lagrangian density L_{m,lambda} = K - m S - (lambda/2) S^2 with K the kinetic term and S = Psibar Psi.
     Psi -> gamma8 Psi multiplies K by the computed kinetic sign and S by the computed mass sign. *)
  lag[mm_, ll_][kk_, ss_] := kk - mm ss - (ll/2) ss^2;
  transformed = lag[m, lam][First[Union[kinSigns]] kin, massSign s];
  freeOK = Expand[(transformed /. lam -> 0) + (lag[-m, 0][kin, s])] === 0;
  withU = Expand[transformed + lag[-m, -lam][kin, s]] === 0;
  <|"pass" -> adjOK && Union[kinSigns] === {-1} && massSign === 1 && spinOK && cSpinOK && freeOK && withU,
    "measurements" -> <|"gamma8TransposeCEqualsCGamma8" -> adjOK,
      "PsibarTransformsTo" -> "Psibar gamma8",
      "kineticMatrixSigns" -> kinSigns, "massMatrixSign" -> massSign,
      "covariantDerivativeCommutes" -> spinOK, "spinConnectionBilinearInvariant" -> cSpinOK,
      "freeLagrangianMap" -> "L_m[gamma8 Psi] = -L_{-m}[Psi] (U = 0)", "freeLagrangianMapVerified" -> freeOK,
      "interactingLagrangianMap" -> "L_{m,U}[gamma8 Psi] = -L_{-m,-U}[Psi]; for U(S) = (lambda/2) S^2 the self-coupling sign also flips (lambda -> -lambda), so L_m -> -L_{-m} holds exactly only when U = 0",
      "interactingLagrangianMapVerified" -> withU|>|>
];

(* sign character of Pin(4,4) elements; u is a Clifford element given as a matrix, parity +1 (even) / -1 (odd) *)
pinAction[u_, parity_Integer] := Module[{uInv, lam, lamTw, recon, massSign, tPrime, tPrimeTw, kinSign, kinSignTw,
    eomOK, eomSignTw, orthOK},
  uInv = Inverse[u];
  (* Lambda^mu_nu from u^{-1} gamma^mu u = sum_nu Lambda^mu_nu gamma^nu (untwisted adjoint) *)
  lam = Table[vecCoefficients[uInv.g[mu].u, D16Gammas, etaDiagonal], {mu, 0, 7}];
  recon = And @@ Table[equalQ[uInv.g[mu].u, Sum[lam[[mu + 1, nu + 1]] g[nu], {nu, 0, 7}]], {mu, 0, 7}];
  lamTw = parity lam;
  orthOK = equalQ[lam.D16Eta.Transpose[lam], D16Eta];
  massSign = Which[equalQ[Transpose[u].cMat.u, cMat], 1, equalQ[Transpose[u].cMat.u, -cMat], -1, True, 0];
  (* kinetic tensor after Psi'(x') = u Psi(x), x' = Lambda x:  T'^nu = sum_mu u^T C gamma^mu u (Lambda^-1)^nu_mu *)
  tPrime[l_] := With[{li = Inverse[l]}, Table[Sum[Transpose[u].cMat.g[mu].u li[[nu + 1, mu + 1]], {mu, 0, 7}], {nu, 0, 7}]];
  kinSign[l_] := With[{tp = tPrime[l]}, Which[
    And @@ Table[equalQ[tp[[nu + 1]], cMat.g[nu]], {nu, 0, 7}], 1,
    And @@ Table[equalQ[tp[[nu + 1]], -cMat.g[nu]], {nu, 0, 7}], -1, True, 0]];
  (* Dirac operator covariance: sum_mu (u^-1 gamma^mu u) (Lambda^-1)^nu_mu == gamma^nu *)
  eomOK = With[{li = Inverse[lam]}, And @@ Table[equalQ[Sum[uInv.g[mu].u li[[nu + 1, mu + 1]], {mu, 0, 7}], g[nu]], {nu, 0, 7}]];
  eomSignTw = With[{li = Inverse[lamTw]}, Which[
    And @@ Table[equalQ[Sum[uInv.g[mu].u li[[nu + 1, mu + 1]], {mu, 0, 7}], g[nu]], {nu, 0, 7}], 1,
    And @@ Table[equalQ[Sum[uInv.g[mu].u li[[nu + 1, mu + 1]], {mu, 0, 7}], -g[nu]], {nu, 0, 7}], -1, True, 0]];
  <|"lambdaReconstructs" -> recon, "lambdaInO44" -> orthOK, "massSign" -> massSign,
    "kineticSignUntwisted" -> kinSign[lam], "kineticSignTwisted" -> kinSign[lamTw],
    "detLambdaUntwisted" -> Det[lam], "detLambdaTwisted" -> Det[lamTw],
    "diracOperatorCovariantUntwisted" -> eomOK, "diracOperatorSignTwisted" -> eomSignTw, "lambdaUntwisted" -> lam|>
];

checkPinLiftCharacter[] := Module[{vectors, vecResults, vecOK, prodResults, prodOK, sameSign, other,
    lag, lagOdd, kin, s, m, lam, cc, chiK, chiM, evenMap, evenMapNotSelf, oddMap},
  vectors = Join[
    Table[{"e" <> ToString[a], g[a], D16Eta[[a + 1, a + 1]]}, {a, 0, 7}],
    {{"e0+e1+e4", g[0] + g[1] + g[4], 1}, {"e0+e4+e5", g[0] + g[4] + g[5], -1}}
  ];
  vecResults = Association @@ Table[
    With[{name = v[[1]], u = v[[2]], n = v[[3]]},
      name -> Join[<|"norm" -> n, "normVerified" -> equalQ[u.u, n id16]|>, KeyDrop[pinAction[u, -1], "lambdaUntwisted"],
        If[StringMatchQ[name, "e" ~~ DigitCharacter], <|"lambdaUntwistedDiagonal" -> Diagonal[pinAction[u, -1]["lambdaUntwisted"]]|>, <||>]]],
    {v, vectors}];
  vecOK = AllTrue[Values[vecResults], #["normVerified"] && #["lambdaReconstructs"] && #["lambdaInO44"] &&
      #["diracOperatorCovariantUntwisted"] && #["massSign"] === -#["norm"] && #["kineticSignUntwisted"] === -#["norm"] &&
      #["kineticSignTwisted"] === #["norm"] && #["diracOperatorSignTwisted"] === -1 &];
  prodResults = Association @@ Flatten[Table[
    With[{r = pinAction[g[a].g[b], 1]},
      ("e" <> ToString[a] <> "e" <> ToString[b]) -> <|"spinorNorm" -> D16Eta[[a + 1, a + 1]] D16Eta[[b + 1, b + 1]],
        "massSign" -> r["massSign"], "kineticSign" -> r["kineticSignUntwisted"],
        "diracOperatorCovariant" -> r["diracOperatorCovariantUntwisted"]|>],
    {a, 0, 3}, {b, 4, 7}]];
  prodOK = AllTrue[Values[prodResults], #["spinorNorm"] === -1 && #["massSign"] === -1 && #["kineticSign"] === -1 && #["diracOperatorCovariant"] &];
  other = Association @@ Flatten[Table[
    With[{r = pinAction[g[a].g[b], 1]},
      ("e" <> ToString[a] <> "e" <> ToString[b]) -> <|"spinorNorm" -> D16Eta[[a + 1, a + 1]] D16Eta[[b + 1, b + 1]],
        "massSign" -> r["massSign"], "kineticSign" -> r["kineticSignUntwisted"]|>],
    {a, 0, 7}, {b, a + 1, 7}]];
  sameSign = AllTrue[Values[other], #["massSign"] === #["kineticSign"] === #["spinorNorm"] &];
  (* interaction term under a chi = -1 element: signs taken from the computed e0 row *)
  chiK = vecResults["e0"]["kineticSignUntwisted"]; chiM = vecResults["e0"]["massSign"];
  lag[mm_, ll_][kk_, ss_] := kk - mm ss - (ll/2) ss^2;
  lagOdd[mm_, c3_][kk_, ss_] := kk - mm ss - c3 ss^3;
  evenMap = Expand[lag[m, lam][chiK kin, chiM s] + lag[m, -lam][kin, s]] === 0;
  evenMapNotSelf = Expand[lag[m, lam][chiK kin, chiM s] + lag[m, lam][kin, s]] =!= 0;
  oddMap = Expand[lagOdd[m, cc][chiK kin, chiM s] + lagOdd[m, cc][kin, s]] === 0;
  <|"pass" -> vecOK && prodOK && sameSign && chiK === -1 && chiM === -1 && evenMap && evenMapNotSelf && oddMap,
    "measurements" -> <|"unitVectors" -> vecResults, "productsPositiveTimesNegative" -> prodResults,
      "allBivectorProductsSignEqualsSpinorNorm" -> sameSign,
      "character" -> "Psi -> u Psi (u unit vector): Psibar Psi -> -n(u) Psibar Psi; with the untwisted adjoint vector action the kinetic term also picks up -n(u) (same sign: free Lagrangian L -> -n(u) L, free field equations Pin(4,4)-covariant); with the twisted adjoint (reflection) the kinetic term picks up +n(u), opposite to the mass term. For g = u1 u2: sign = n(u1) n(u2) (spinor norm); n(u1)=+1, n(u2)=-1 gives -1.",
      "interactionMapLambdaFlipVerified" -> evenMap,
      "interactionMapIsNotMinusSelf" -> evenMapNotSelf,
      "oddPotentialGivesMinusSelfVerified" -> oddMap,
      "interactionCaveat" -> "U(Psibar Psi) -> U(chi Psibar Psi). For chi = -1 and U(S) = (lambda/2) S^2 the interaction term does not flip: L_{m,lambda} -> -L_{m,-lambda}; the interacting field equation gamma.D Psi = (m + U'(S)) Psi is mapped to the one with U'(S) -> -U'(-S) (lambda -> -lambda). Exact covariance of the interacting theory under chi = -1 elements requires U odd (U(-S) = -U(S))."|>|>
];

checkCurvedAnticommutatorMatrix[] := Module[{ee, ev, gam4, g44, lhs1, lhs2, symOK, antisym, g1Results, g1OK,
    sz, cz, a0, h, einv, gam4G2, g44G2, g2OK},
  ev = Array[ee, 8, 0];
  gam4 = Sum[ev[[a + 1]] g[a], {a, 0, 7}];
  g44 = Expand[Sum[ev[[a + 1]] ev[[b + 1]] D16Eta[[a + 1, b + 1]], {a, 0, 7}, {b, 0, 7}]];
  lhs1 = Expand[(cMat.gam4).(gam4.cMat)];
  lhs2 = Expand[(gam4.cMat).(cMat.gam4)];
  symOK = zeroQ[lhs1 - g44 id16] && zeroQ[lhs2 - g44 id16] && zeroQ[Expand[gam4.gam4] - g44 id16];
  antisym = zeroQ[Transpose[gam4.cMat] + gam4.cMat];
  (* concrete curved gamma^4 of test geometry G1 at p1, p2, p3 *)
  g1Results = Table[Module[{x = pt, vb, dt, einvLoc, gam, gmet, gup44, inert},
      vb = D16G1Vielbein[x];
      dt = Det[vb];
      einvLoc = Inverse[vb];        (* einvLoc[[a+1, mu+1]] = e_a^mu *)
      gmet = vb.D16Eta.Transpose[vb];
      inert = D16RealSymmetricInertia[gmet];
      gam = Sum[einvLoc[[a + 1, 5]] g[a], {a, 0, 7}];
      gup44 = Inverse[gmet][[5, 5]];
      <|"detVielbein" -> dt, "detNonzero" -> (dt =!= 0), "metricInertia" -> inert,
        "signature44" -> (inert === {4, 4, 0}), "gUpper44" -> gup44,
        "gUpper44FromVielbein" -> (Sum[einvLoc[[a + 1, 5]] einvLoc[[b + 1, 5]] D16Eta[[a + 1, b + 1]], {a, 0, 7}, {b, 0, 7}] === gup44),
        "inverseFormulaExact" -> equalQ[Inverse[cMat.gam], gam.cMat/gup44]|>],
    {pt, D16G1Points}];
  g1OK = AllTrue[g1Results, #["detNonzero"] && #["signature44"] && #["gUpper44FromVielbein"] && #["inverseFormulaExact"] &];
  (* primordial field G2: diagonal vielbein h = (cot z, s^(1/6) e^a4 (x3), 1, s^(1/6) e^-a4 (x3)); e_4^4 = 1 *)
  h = {cz/sz, sz^(1/6) Exp[a0], sz^(1/6) Exp[a0], sz^(1/6) Exp[a0], 1, sz^(1/6) Exp[-a0], sz^(1/6) Exp[-a0], sz^(1/6) Exp[-a0]};
  einv = DiagonalMatrix[1/h];
  gam4G2 = Sum[einv[[a + 1, 5]] g[a], {a, 0, 7}];
  g44G2 = Sum[einv[[a + 1, 5]] einv[[b + 1, 5]] D16Eta[[a + 1, b + 1]], {a, 0, 7}, {b, 0, 7}];
  g2OK = equalQ[gam4G2, g[4]] && g44G2 === -1 && equalQ[I gam4G2.cMat/g44G2, bMat];
  <|"pass" -> symOK && antisym && g1OK && g2OK,
    "measurements" -> <|"symbolicProductIdentity" -> symOK,
      "statement" -> "(C gamma^4)(gamma^4 C) = (gamma^4 C)(C gamma^4) = g^44 I16 for gamma^4 = e_a^4 gamma^a with symbolic e_a^4; hence (C gamma^4)^-1 = gamma^4 C / g^44 whenever g^44 != 0",
      "gamma4CAntisymmetric" -> antisym,
      "G1Points" -> g1Results, "G1AllPassed" -> g1OK,
      "G2GaussianNormalReducesToB" -> g2OK,
      "G2Statement" -> "primordial field (CONTRACT section 9) with cot z, sin z and the arbitrary function a4 kept as independent exact symbols (no numerical substitution is needed because e_4^4 = 1 exactly): gamma^4 = gamma^{a=4}, g^44 = -1, i (C gamma^4)^-1 = B",
      "G1Definition" -> "e_mu^a = delta_mu^a + P_mu^a(x), P_mu^a = (1/10)((mu+1) x_a - (a+1) x_mu) + (1/20) x_mu x_a + (1/30) x_((mu+a) mod 8)^2 (mu != a), P_mu^mu = (1/10) x_mu^2 + (1/40) x_((mu+1) mod 8); points p1, p2, p3 of the task; gamma^4 = e_a^4 gamma^a with e_a^mu = Inverse[e_mu^a]",
      "G1PointList" -> D16G1Points|>|>
];

checkFlatModeHamiltonian[] := Module[{m, k, kv, sum, h, hDag, anti, antiExpected, herm, hermExpected, antiSq,
    hSq, disp, com, comExpected, comSq, kIdx},
  kIdx = {0, 1, 2, 3, 5, 6, 7};
  kv = Association[Table[j -> k[j], {j, kIdx}]];
  sum = Sum[k[j] g[j], {j, kIdx}];
  h = -I m g[4] - g[4].sum;
  hDag = ComplexExpand[ConjugateTranspose[h]];
  anti = Expand[(h - hDag)/2];
  antiExpected = -g[4].Sum[k[j] g[j], {j, {5, 6, 7}}];
  herm = Expand[(h + hDag)/2];
  hermExpected = -I m g[4] - g[4].Sum[k[j] g[j], {j, {0, 1, 2, 3}}];
  antiSq = zeroQ[Expand[antiExpected.antiExpected] + (k[5]^2 + k[6]^2 + k[7]^2) id16];
  disp = m^2 + k[0]^2 + k[1]^2 + k[2]^2 + k[3]^2 - k[5]^2 - k[6]^2 - k[7]^2;
  hSq = zeroQ[Expand[h.h] - disp id16];
  com = Expand[comm[h, bMat]];
  comExpected = 2 I Sum[k[j] cMat.g[j], {j, {5, 6, 7}}];
  comSq = zeroQ[Expand[(cMat.Sum[k[j] g[j], {j, {5, 6, 7}}]).(cMat.Sum[k[j] g[j], {j, {5, 6, 7}}])] + (k[5]^2 + k[6]^2 + k[7]^2) id16];
  <|"pass" -> zeroQ[anti - antiExpected] && zeroQ[herm - hermExpected] && antiSq && hSq && zeroQ[com - comExpected] && comSq,
    "measurements" -> <|
      "hamiltonian" -> "h_k = -I m gamma^4 - gamma^4 sum_{j in {0,1,2,3,5,6,7}} k_j gamma^j (m, k_j real)",
      "antiHermitianPart" -> "-gamma^4 (k5 gamma^5 + k6 gamma^6 + k7 gamma^7)",
      "antiHermitianPartVerified" -> zeroQ[anti - antiExpected],
      "antiHermitianPartSquare" -> "-(k5^2 + k6^2 + k7^2) I16 (nonzero iff (k5,k6,k7) != 0)",
      "antiHermitianPartSquareVerified" -> antiSq,
      "hermitianPartVerified" -> zeroQ[herm - hermExpected],
      "hSquared" -> "(m^2 + k0^2 + k1^2 + k2^2 + k3^2 - k5^2 - k6^2 - k7^2) I16", "hSquaredVerified" -> hSq,
      "commutatorWithB" -> "[h_k, B] = 2 I (k5 C gamma^5 + k6 C gamma^6 + k7 C gamma^7)",
      "commutatorWithBVerified" -> zeroQ[com - comExpected],
      "commutatorSquareFactor" -> "(C sum_{j=5,6,7} k_j gamma^j)^2 = -(k5^2+k6^2+k7^2) I16 (so [h_k,B]=0 iff k5=k6=k7=0)",
      "commutatorSquareVerified" -> comSq|>|>
];

kreinData[h_, energy_] := Module[{vs, vm, gs, gb, mr, inv, tr, cp, x},
  vs = NullSpace[h - energy id16];
  vm = Transpose[vs];
  gs = ConjugateTranspose[vm].vm;
  inv = Inverse[gs];
  mr = Simplify[inv.ConjugateTranspose[vm].bMat.vm];
  tr = Simplify[Tr[mr]];
  cp = Expand[CharacteristicPolynomial[mr, x]];
  <|"dimension" -> Length[vs],
    "BPreservesSpace" -> equalQ[Simplify[bMat.vm], Simplify[vm.mr]],
    "restrictionSquaresToIdentity" -> equalQ[Simplify[mr.mr], IdentityMatrix[Length[vs]]],
    "signature" -> {(Length[vs] + tr)/2, (Length[vs] - tr)/2},
    "characteristicPolynomial" -> polyString[Factor[cp], x]|>
];

checkKreinSignature[] := Module[{rest, restNeg, good1, good1neg, good2, h1, h2, sq1, sq2},
  rest = kreinData[-I g[4], 1];
  restNeg = kreinData[-I g[4], -1];
  h1 = -I 1 g[4] - g[4].(1 g[0] + 1 g[1] + 2 g[2] + 3 g[3]);   (* m = 1, k = (1,1,2,3; 0,0,0), E = 4 *)
  h2 = -I 3 g[4] - g[4].(1 g[0] + 1 g[1] + 1 g[2] + 2 g[3]);   (* m = 3, k = (1,1,1,2; 0,0,0), E = 4 *)
  sq1 = equalQ[h1.h1, 16 id16]; sq2 = equalQ[h2.h2, 16 id16];
  good1 = kreinData[h1, 4]; good1neg = kreinData[h1, -4];
  good2 = kreinData[h2, 4];
  <|"pass" -> rest["dimension"] === 8 && rest["BPreservesSpace"] && rest["restrictionSquaresToIdentity"] &&
      rest["signature"] === {4, 4} && sq1 && sq2 && hermitianQ[h1] && hermitianQ[h2] &&
      AllTrue[{good1, good1neg, good2}, #["dimension"] === 8 && #["BPreservesSpace"] && #["restrictionSquaresToIdentity"] &],
    "measurements" -> <|
      "restPositiveFrequencySpace" -> "eigenspace of -I gamma^4 with eigenvalue +1 (h_0 = m(-I gamma^4), m > 0)",
      "restPositiveFrequency" -> rest, "restNegativeFrequency" -> restNeg,
      "goodSectorExample1" -> "m = 1, k = (1,1,2,3,0,0,0) over directions (0,1,2,3,5,6,7), E = 4",
      "goodSectorExample1Positive" -> good1, "goodSectorExample1Negative" -> good1neg,
      "goodSectorExample2" -> "m = 3, k = (1,1,1,2,0,0,0), E = 4",
      "goodSectorExample2Positive" -> good2,
      "hSquaredEquals16" -> {sq1, sq2},
      "method" -> "basis V of the eigenspace (exact Gaussian rationals); M = (V^dagger V)^-1 V^dagger B V is the matrix of B restricted (B V = V M verified); M^2 = I so the eigenvalues are +-1 and the signature of the B-form on the space is ((d + Tr M)/2, (d - Tr M)/2) with respect to the positive Hilbert product."|>|>
];

(* Canonical meaning (lead decision, CONTRACT.md section 11 erratum E1; identical in
   scripts/check_dirac16complex_algebra.py):
     (a) exactly 13 of the 28 S^{ab} commute with B: the 9 of so(4)+so(3) (a,b both in
         {0,1,2,3} or both in {5,6,7}) plus the 4 Hermitian boosts S^{b4}, b = 0..3;
     (b) exactly 9 both commute with B and are anti-Hermitian (unitary for Psi^dagger Psi):
         the unitarily implemented Spin(4) x Spin(3);
     (c) the 21 with a,b != 4 are Krein-unitary (S^dagger B + B S = 0), the 7 S^{4b} are not.
   The original literal claim "exactly 9 S^{ab} commute with B" is false; it is kept as the
   measurement literalClaimExactlyNineCommuteWithB (= False). *)
checkUnitaryAndKreinSubgroups[] := Module[{commB, compactSet, expectedComm, expectedBoosts, stab, stabOK, boosts,
    boostFail, antiHerm, commAndAnti, commAndStab, extraComm, extraHermitian, stabKreinList, extraAntiC, extraAntiG4,
    commOK, unitaryOK, kreinOK},
  commB = Select[spinPairs, zeroQ[comm[D16Spin @@ #, bMat]] &];
  compactSet = Join[Subsets[{0, 1, 2, 3}, {2}], Subsets[{5, 6, 7}, {2}]];     (* so(4) + so(3) *)
  expectedBoosts = Table[{b, 4}, {b, 0, 3}];                                  (* S^{b4}, b = 0..3 *)
  expectedComm = Join[compactSet, expectedBoosts];
  stab = Select[spinPairs, FreeQ[#, 4] &];
  boosts = Select[spinPairs, MemberQ[#, 4] &];
  stabKreinList = Select[spinPairs, zeroQ[ConjugateTranspose[D16Spin @@ #].bMat + bMat.(D16Spin @@ #)] &];
  stabOK = AllTrue[stab, MemberQ[stabKreinList, #] &];
  boostFail = AllTrue[boosts, !MemberQ[stabKreinList, #] &];
  antiHerm = Select[spinPairs, equalQ[ConjugateTranspose[D16Spin @@ #], -(D16Spin @@ #)] &];
  commAndAnti = Intersection[commB, antiHerm];
  commAndStab = Intersection[commB, stab];
  extraComm = Complement[commB, compactSet];
  extraHermitian = AllTrue[extraComm, hermitianQ[D16Spin @@ #] &];
  extraAntiC = AllTrue[extraComm, zeroQ[acomm[D16Spin @@ #, cMat]] &];
  extraAntiG4 = AllTrue[extraComm, zeroQ[acomm[D16Spin @@ #, g[4]]] &];
  commOK = Length[commB] === 13 && Sort[commB] === Sort[expectedComm] && Sort[extraComm] === Sort[expectedBoosts] &&
    extraHermitian && extraAntiC && extraAntiG4;
  unitaryOK = Length[commAndAnti] === 9 && Sort[commAndAnti] === Sort[compactSet] && Sort[commAndStab] === Sort[compactSet];
  kreinOK = Length[stabKreinList] === 21 && Sort[stabKreinList] === Sort[stab] && Length[stab] === 21 && stabOK &&
    Length[boosts] === 7 && boostFail;
  <|"pass" -> commOK && unitaryOK && kreinOK,
    "measurements" -> <|
      "meaning" -> "canonical meaning (CONTRACT.md section 11, E1): (a) exactly 13 of the 28 S^{ab} commute with B (so(4)+so(3) and the 4 Hermitian boosts S^{b4}, b=0..3); (b) exactly 9 commute with B and are anti-Hermitian (unitarily implemented Spin(4)xSpin(3)); (c) the 21 with a,b != 4 are Krein-unitary, the 7 S^{4b} are not",
      "expectedCommutingWithB" -> expectedComm, "expectedCountCommutingWithB" -> 13,
      "generatorsCommutingWithB" -> commB, "countCommutingWithB" -> Length[commB],
      "commutingWithBMatchesCanonical" -> commOK,
      "literalClaimExactlyNineCommuteWithB" -> (Length[commB] === 9),
      "compactGenerators" -> compactSet,
      "commutingWithBBeyondCompact" -> extraComm,
      "extraCommutingGeneratorsAreHermitian" -> extraHermitian,
      "extraCommutingGeneratorsAnticommuteWithC" -> extraAntiC,
      "extraCommutingGeneratorsAnticommuteWithGamma4" -> extraAntiG4,
      "commutingWithBAndAntiHermitian" -> commAndAnti, "countCommutingWithBAndAntiHermitian" -> Length[commAndAnti],
      "commutingWithBAndInStabilizer" -> commAndStab, "countCommutingWithBAndInStabilizer" -> Length[commAndStab],
      "compactSubgroupMatchesExpectation" -> unitaryOK,
      "kreinAntiHermitianGenerators" -> stabKreinList, "countKreinAntiHermitian" -> Length[stabKreinList],
      "stabilizerGeneratorCount" -> Length[stab], "kreinUnitaryOnStabilizer" -> stabOK,
      "boostGenerators" -> boosts, "kreinUnitarityFailsForAllBoosts" -> boostFail,
      "hilbertAntiHermitianGenerators" -> antiHerm, "countHilbertAntiHermitian" -> Length[antiHerm],
      "finding" -> "13 of the 28 S^{ab} commute with B = -I C gamma^4, not 9: the 6 generators of so(4) (a,b in {0,1,2,3}), the 3 of so(3) (a,b in {5,6,7}) AND the 4 boosts S^{b4}, b in {0,1,2,3} (S^{b4} anticommutes with C and with gamma^4, hence commutes with B; it is Hermitian, so exp(theta S^{b4}) is neither unitary for Psi^dagger Psi nor Krein-unitary). The unitarily implemented so(4)+so(3) is exactly (commuting with B) AND (anti-Hermitian), equivalently (commuting with B) AND (in the direction-4 stabilizer spin(4,3)). Krein: S^dagger B + B S = 0 exactly for the 21 generators with a,b != 4 and fails for all 7 S^{4b}. The literal claim 'exactly 9 commute with B' is false and is recorded as literalClaimExactlyNineCommuteWithB = false; the check tests the canonical meaning (a)-(c)."
    |>|>
];

checkCurrentHermiticity[] := Module[{herm},
  herm = Table[hermitianQ[-I cMat.g[mu]], {mu, 0, 7}];
  <|"pass" -> (And @@ herm) && equalQ[-I cMat.g[4], bMat],
    "measurements" -> <|"currentMatricesHermitian" -> herm, "J4MatrixEqualsB" -> equalQ[-I cMat.g[4], bMat]|>|>
];

(* ------------------------------------------------------------------------- *)
(* 7. Assembly                                                                *)
(* ------------------------------------------------------------------------- *)

D16AlgebraVerification[root_String] := Module[{results, checks, measurements, clif, oct},
  results = <|
    "ALG_clifford" -> checkClifford[],
    "ALG_gammaTransposeSymmetry" -> checkGammaTransposeSymmetry[],
    "ALG_chargeMatrix" -> checkChargeMatrix[],
    "ALG_expression1" -> checkExpression1[],
    "ALG_spinTransposeProperties" -> checkSpinTransposeProperties[],
    "ALG_chirality" -> checkChirality[],
    "ALG_faithful" -> checkFaithful[],
    "ALG_pinIrreducibleComplex" -> checkPinIrreducibleComplex[],
    "ALG_spinDecomposition" -> checkSpinDecomposition[],
    "ALG_cliffordPictureIntertwiner" -> checkCliffordPictureIntertwiner[root],
    "ALG_octonionPictureIntertwiner" -> checkOctonionPictureIntertwiner[root],
    "ALG_chargeFormB" -> checkChargeFormB[],
    "ALG_invariantForms" -> checkInvariantForms[],
    "ALG_gamma8Map" -> checkGamma8Map[],
    "ALG_pinLiftCharacter" -> checkPinLiftCharacter[],
    "QNT_curvedAnticommutatorMatrix" -> checkCurvedAnticommutatorMatrix[],
    "QNT_flatModeHamiltonian" -> checkFlatModeHamiltonian[],
    "QNT_kreinSignature" -> checkKreinSignature[],
    "QNT_unitaryAndKreinSubgroups" -> checkUnitaryAndKreinSubgroups[],
    "QNT_currentHermiticity" -> checkCurrentHermiticity[]
  |>;
  checks = TrueQ[#["pass"]] & /@ results;
  measurements = Association[Flatten[KeyValueMap[
    Function[{name, r}, KeyValueMap[(name <> "." <> #1) -> #2 &, r["measurements"]]], results], 1]];
  clif = results["ALG_cliffordPictureIntertwiner"]["measurements"];
  measurements = Join[<|
    "K_clifford" -> D16KClifford,
    "K_octonion" -> If[octonionIntertwiner["dimension"] === 1, D16KOctonion, "intertwiner dimension is not 1"],
    "volumeElementSign" -> Lookup[clif, "volumeElementSign", 0],
    "chiralityDiagonal" -> Diagonal[D16Chirality]
  |>, measurements];
  <|"checks" -> checks, "measurements" -> measurements|>
];
D16AlgebraVerification[] := D16AlgebraVerification[ParentDirectory[DirectoryName[$InputFileName]]];

(* ------------------------------------------------------------------------- *)
(* 8. Comparison with an independent JSON fixture                             *)
(* ------------------------------------------------------------------------- *)

D16NamedMatrices[] := Module[{named},
  named = Join[
    <|"eta" -> D16Eta, "sigma8" -> D16Sigma8, "I8" -> id8, "I16" -> id16,
      "C" -> D16C, "gamma8" -> D16Chirality, "B" -> D16B, "Pminus" -> D16ProjMinus, "Pplus" -> D16ProjPlus,
      "CPminus" -> D16C.D16ProjMinus, "CPplus" -> D16C.D16ProjPlus,
      "Cdm" -> D16CliffordPictureC, "volumeDm" -> D16CliffordPictureVolume|>,
    If[MissingQ[D16KClifford], <||>, <|"K_clifford" -> D16KClifford, "K_clifford_inverse" -> Inverse[D16KClifford]|>],
    If[MissingQ[D16KOctonion], <||>, <|"K_octonion" -> D16KOctonion, "K_octonion_inverse" -> Inverse[D16KOctonion]|>],
    Association[Table[("gamma" <> ToString[a]) -> D16Gammas[[a + 1]], {a, 0, 7}]],
    Association[Table[("tau" <> ToString[a]) -> D16Tau[[a + 1]], {a, 0, 7}]],
    Association[Table[("taubar" <> ToString[a]) -> D16TauBar[[a + 1]], {a, 0, 7}]],
    Association[Table[("Cgamma" <> ToString[a]) -> D16C.D16Gammas[[a + 1]], {a, 0, 7}]],
    Association[Table[("current" <> ToString[a]) -> -I D16C.D16Gammas[[a + 1]], {a, 0, 7}]],
    Association[Table[("gammaHat" <> ToString[a]) -> D16CliffordPictureGammas[[a + 1]], {a, 0, 7}]],
    Association[Table[("octonionGamma" <> ToString[a]) -> D16OctonionGammas[[a + 1]], {a, 0, 7}]],
    Association[Table[("octonionLeft" <> ToString[a]) -> octLeft[[a + 1]], {a, 0, 7}]],
    Association[Flatten[Table[("S" <> ToString[a] <> ToString[b]) -> D16Spin[a, b], {a, 0, 7}, {b, 0, 7}]]]
  ];
  named
];

normalizeKey[s_String] := ToLowerCase[StringDelete[s, Except[WordCharacter] | "_"]];

(* alias -> function(index) returning the expected matrix; index Missing[] for plain names *)
listAliases = <|
  "gamma" -> D16Gammas, "gammas" -> D16Gammas, "gammamatrices" -> D16Gammas, "notebookgammas" -> D16Gammas,
  "t16a" -> D16Gammas, "flatgammas" -> D16Gammas, "gammaflat" -> D16Gammas, "gammaa" -> D16Gammas,
  "tau" -> D16Tau, "taus" -> D16Tau, "taubar" -> D16TauBar, "taubars" -> D16TauBar, "overbartau" -> D16TauBar,
  "gammahat" -> D16CliffordPictureGammas, "gammahats" -> D16CliffordPictureGammas,
  "gammaclifford" -> D16CliffordPictureGammas, "cliffordgamma" -> D16CliffordPictureGammas,
  "cliffordpicturegammas" -> D16CliffordPictureGammas, "diracmaingammas" -> D16CliffordPictureGammas,
  "tensorgammas" -> D16CliffordPictureGammas, "cliffordgammas" -> D16CliffordPictureGammas,
  "cl44generators" -> D16CliffordPictureGammas,
  "octoniongammas" -> D16OctonionGammas, "gammaoctonion" -> D16OctonionGammas,
  "octonionleft" -> octLeft, "leftmultiplication" -> octLeft, "octonionleftmatrices" -> octLeft,
  "cgamma" -> (D16C.# & /@ D16Gammas), "kinetic" -> (D16C.# & /@ D16Gammas),
  "kineticmatrices" -> (D16C.# & /@ D16Gammas), "currentmatrices" -> (-I D16C.# & /@ D16Gammas)
|>;
plainAliases := <|
  "eta" -> D16Eta, "metric" -> D16Eta, "eta4488" -> D16Eta, "tangentmetric" -> D16Eta,
  "sigma" -> D16Sigma8, "sigma8" -> D16Sigma8,
  "c" -> D16C, "charge" -> D16C, "chargematrix" -> D16C, "sigma16" -> D16C, "cmatrix" -> D16C,
  "adjointmatrix" -> D16C, "chargeconjugation" -> D16C,
  "gamma8" -> D16Chirality, "chirality" -> D16Chirality, "chiralitymatrix" -> D16Chirality, "g8" -> D16Chirality,
  "volumeelement" -> D16Chirality, "t16a8" -> D16Chirality,
  "b" -> D16B, "bmatrix" -> D16B, "krein" -> D16B, "kreinmetric" -> D16B, "fundamentalsymmetry" -> D16B,
  "pminus" -> D16ProjMinus, "projminus" -> D16ProjMinus, "projectorminus" -> D16ProjMinus,
  "pplus" -> D16ProjPlus, "projplus" -> D16ProjPlus, "projectorplus" -> D16ProjPlus,
  "cdm" -> D16CliffordPictureC, "cliffordpicturec" -> D16CliffordPictureC,
  "kclifford" -> D16KClifford, "cliffordintertwiner" -> D16KClifford, "intertwinerclifford" -> D16KClifford,
  "koctonion" -> D16KOctonion, "octonionintertwiner" -> D16KOctonion, "intertwineroctonion" -> D16KOctonion,
  "chiralitydiagonal" -> Diagonal[D16Chirality], "identity16" -> id16, "i16" -> id16
|>;

parseScalar[x_Integer] := x;
parseScalar[x_Real] := x;
parseScalar[True] := $Failed;
parseScalar[False] := $Failed;
parseScalar[s_String] := Module[{t, v},
  t = StringDelete[s, WhitespaceCharacter];
  t = StringReplace[t, {RegularExpression["(?<=[0-9)])[ij]$"] -> "*I", RegularExpression["^([+-]?)[ij]$"] -> "$1I",
    RegularExpression["(?<=[+-])[ij]$"] -> "I", "j" -> "I", "i" -> "I"}];
  If[t === "" || !StringMatchQ[t, RegularExpression["[0-9/+\\-*I()]+"]], Return[$Failed]];
  v = Quiet[Check[ToExpression[t], $Failed]];
  If[ExactNumberQ[v], v, $Failed]
];
parseScalar[a_Association] := Module[{re, im},
  re = Lookup[a, "re", Lookup[a, "real", Missing[]]];
  im = Lookup[a, "im", Lookup[a, "imag", Missing[]]];
  If[MissingQ[re] || MissingQ[im] || Length[a] =!= 2, Return[$Failed]];
  re = parseScalar[re]; im = parseScalar[im];
  If[re === $Failed || im === $Failed, $Failed, re + I im]
];
parseScalar[_] := $Failed;

(* numeric array (vector or matrix) or $Failed *)
parseArray[v_List] := Module[{p},
  If[v === {}, Return[$Failed]];
  If[VectorQ[v, !ListQ[#] &],
    p = parseScalar /@ v; Return[If[MemberQ[p, $Failed], $Failed, p]]];
  If[AllTrue[v, ListQ] && Length[Union[Length /@ v]] === 1 && AllTrue[v, VectorQ[#, !ListQ[#] &] &],
    p = Map[parseScalar, v, {2}]; Return[If[MemberQ[Flatten[p], $Failed], $Failed, p]]];
  $Failed
];
parseArray[a_Association] := Module[{keys = Keys[a], re, im},
  If[Length[a] =!= 2, Return[$Failed]];
  re = Lookup[a, "re", Lookup[a, "real", Missing[]]];
  im = Lookup[a, "im", Lookup[a, "imag", Missing[]]];
  If[MissingQ[re] || MissingQ[im] || !ListQ[re] || !ListQ[im], Return[$Failed]];
  re = parseArray[re]; im = parseArray[im];
  If[re === $Failed || im === $Failed || Dimensions[re] =!= Dimensions[im], $Failed, re + I im]
];
parseArray[_] := $Failed;

splitIndexKey[key_String] := Module[{n = normalizeKey[key], m},
  m = StringCases[n, RegularExpression["^([a-z0-9]*?[a-z])([0-9]+)$"] -> {"$1", "$2"}];
  If[m === {}, {n, Missing[]}, {m[[1, 1]], ToExpression[m[[1, 2]]]}]
];

(* expected value for a path (list of keys / indices), or Missing *)
expectedForPath[path_List] := Module[{keys, last, parent, n, base, idx, lastIdx},
  keys = Select[path, StringQ];
  If[keys === {}, Return[Missing[]]];
  last = Last[path];
  lastIdx = If[IntegerQ[last], last, If[StringQ[last] && StringMatchQ[last, DigitCharacter ..], ToExpression[last], Missing[]]];
  (* case 1: last key is a plain alias *)
  n = normalizeKey[Last[keys]];
  If[StringQ[last] && KeyExistsQ[plainAliases, n], Return[plainAliases[n]]];
  (* case 2: key with trailing index, e.g. gamma4, tau7, S01 *)
  If[StringQ[last],
    {base, idx} = splitIndexKey[last];
    If[base === "gamma" && idx === 8, Return[D16Chirality]];
    If[KeyExistsQ[listAliases, base] && IntegerQ[idx] && 0 <= idx < Length[listAliases[base]], Return[listAliases[base][[idx + 1]]]];
    If[MemberQ[{"s", "spin", "sab"}, base] && IntegerQ[idx] && 0 <= idx <= 77 && Length[IntegerDigits[idx, 10, 2]] === 2,
      With[{d = IntegerDigits[idx, 10, 2]}, If[Max[d] <= 7, Return[D16Spin @@ d]]]]
  ];
  (* case 3: element of a list-valued alias: path ... "gamma", i *)
  If[IntegerQ[lastIdx] && Length[path] >= 2,
    parent = path[[-2]];
    If[StringQ[parent],
      n = normalizeKey[parent];
      If[n === "gamma" || n === "gammas" || n === "gammamatrices", If[lastIdx === 8, Return[D16Chirality]]];
      If[KeyExistsQ[listAliases, n] && 0 <= lastIdx < Length[listAliases[n]], Return[listAliases[n][[lastIdx + 1]]]];
      If[MemberQ[{"s", "spin", "sab", "spingenerators"}, n] && 0 <= lastIdx < 28, Return[D16Spin @@ spinPairs[[lastIdx + 1]]]]
    ];
    (* S[a][b] nested 8x8 *)
    If[Length[path] >= 3 && StringQ[path[[-3]]] && MemberQ[{"s", "spin", "sab", "spinmatrix", "spinmatrices"}, normalizeKey[path[[-3]]]],
      With[{ia = path[[-2]], ib = lastIdx},
        If[IntegerQ[ia] && 0 <= ia <= 7 && 0 <= ib <= 7, Return[D16Spin[ia, ib]]]]]
  ];
  Missing[]
];

walkFixture[value_, path_List] := Module[{arr},
  arr = parseArray[value];
  If[arr =!= $Failed && Length[path] > 0, Return[{{path, arr}}, Module]];
  Which[
    AssociationQ[value], Join @@ KeyValueMap[walkFixture[#2, Append[path, #1]] &, value],
    ListQ[value], Join @@ MapIndexed[walkFixture[#1, Append[path, #2[[1]] - 1]] &, value],
    True, {}
  ]
];

fetchPath[data_, {}] := data;
fetchPath[data_Association, {k_String, rest___}] := If[KeyExistsQ[data, k], fetchPath[data[k], {rest}], Missing[]];
fetchPath[data_List, {i_Integer, rest___}] := If[0 <= i < Length[data], fetchPath[data[[i + 1]], {rest}], Missing[]];
fetchPath[_, _] := Missing[];

D16CompareFixture[json_] := Module[{leaves, named, rows, nameMismatch, unmatched, compared,
    skippedVectors, spinLabelled},
  leaves = walkFixture[json, {}];
  (* entries of the form {..., "S": [ {"a": a, "b": b, "matrix": M}, ... ]} are matched by their
     own a, b labels *)
  spinLabelled[path_List] := Module[{parent},
    If[Length[path] < 3 || !StringQ[Last[path]] || normalizeKey[Last[path]] =!= "matrix", Return[Missing[], Module]];
    parent = fetchPath[json, Most[path]];
    If[AssociationQ[parent] && IntegerQ[Lookup[parent, "a", None]] && IntegerQ[Lookup[parent, "b", None]] &&
        StringQ[path[[-3]]] && MemberQ[{"s", "spin", "sab", "spingenerators", "spinmatrices"}, normalizeKey[path[[-3]]]] &&
        0 <= parent["a"] <= 7 && 0 <= parent["b"] <= 7,
      D16Spin[parent["a"], parent["b"]], Missing[]]
  ];
  named = D16NamedMatrices[];
  rows = Map[Function[leaf, Module[{path = leaf[[1]], arr = leaf[[2]], exp, byValue, pathString, inexact},
      pathString = StringRiffle[ToString /@ path, "/"];
      exp = spinLabelled[path];
      If[MissingQ[exp], exp = expectedForPath[path]];
      byValue = If[MatrixQ[arr], Keys[Select[named, Dimensions[#] === Dimensions[arr] && equalQ[#, arr] &]], {}];
      inexact = !FreeQ[arr, _Real];
      Which[
        !MissingQ[exp] && Dimensions[exp] === Dimensions[arr] && equalQ[exp, arr],
          <|"path" -> pathString, "status" -> "agree-by-name", "valueMatches" -> byValue, "inexactEntries" -> inexact|>,
        !MissingQ[exp],
          <|"path" -> pathString, "status" -> "DISAGREE-by-name", "valueMatches" -> byValue, "inexactEntries" -> inexact,
            "proportional" -> (Dimensions[exp] === Dimensions[arr] && MatrixQ[arr] && MatrixRank[{Flatten[exp], Flatten[arr]}] === 1)|>,
        MatrixQ[arr] && byValue =!= {},
          <|"path" -> pathString, "status" -> "agree-by-value", "valueMatches" -> byValue, "inexactEntries" -> inexact|>,
        MatrixQ[arr],
          <|"path" -> pathString, "status" -> "UNMATCHED-matrix", "dimensions" -> Dimensions[arr], "inexactEntries" -> inexact|>,
        True,
          <|"path" -> pathString, "status" -> "vector-not-compared", "dimensions" -> Dimensions[arr]|>
      ]]], leaves];
  nameMismatch = Select[rows, #["status"] === "DISAGREE-by-name" &];
  unmatched = Select[rows, #["status"] === "UNMATCHED-matrix" &];
  compared = Select[rows, MemberQ[{"agree-by-name", "agree-by-value", "DISAGREE-by-name", "UNMATCHED-matrix"}, #["status"]] &];
  skippedVectors = Select[rows, #["status"] === "vector-not-compared" &];
  <|"agree" -> (Length[compared] > 0 && nameMismatch === {} && unmatched === {}),
    "matricesFound" -> Count[rows, r_ /; r["status"] =!= "vector-not-compared"],
    "agreeByName" -> Count[rows, r_ /; r["status"] === "agree-by-name"],
    "agreeByValue" -> Count[rows, r_ /; r["status"] === "agree-by-value"],
    "disagreeByName" -> Length[nameMismatch], "unmatched" -> Length[unmatched],
    "vectorsNotCompared" -> Length[skippedVectors],
    "details" -> rows|>
];

(* ------------------------------------------------------------------------- *)
(* 9. JSON conversion                                                         *)
(* ------------------------------------------------------------------------- *)

D16JSONValue[x_Integer] := x;
D16JSONValue[x_Rational] := ToString[Numerator[x]] <> "/" <> ToString[Denominator[x]];
D16JSONValue[True] := True;
D16JSONValue[False] := False;
asciiString[s_String] := StringJoin[If[# < 128, FromCharacterCode[#],
    StringTake[ToString[FromCharacterCode[#], InputForm, CharacterEncoding -> "ASCII"], {2, -2}]] & /@ ToCharacterCode[s]];
D16JSONValue[x_String] := asciiString[x];
D16JSONValue[x_List] := D16JSONValue /@ x;
D16JSONValue[x_Association] := Association[KeyValueMap[(asciiString[If[StringQ[#1], #1, ToString[#1, InputForm]]] -> D16JSONValue[#2]) &, x]];
D16JSONValue[x_Missing] := asciiString[ToString[x, InputForm]];
D16JSONValue[x_] := asciiString[ToString[x, InputForm]];

End[];
EndPackage[];
