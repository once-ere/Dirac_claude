(* ::Package:: *)

(* ::Title:: *)
(* Dirac16ComplexPrimordial.wl *)

(* ::Text:: *)
(* Stage 2 of dirac16complex: the complex Grassmann 16-component spinor in the
   notebook's primordial (pair-creation) field MatrixMetric44.

   Conventions: CONTRACT.md sections 0-9 (zero-based indices x0..x7, frame
   indices 0..7, spinor indices 0..15, eta = diag(+,+,+,+,-,-,-,-),
   gamma^a = [[0, taubar_a],[tau_a, 0]] split-octonion basis, C = sigma16).

   The module is self-contained: gamma matrices are rebuilt from the
   split-octonion recipe (CONTRACT section 1) and compared with the committed
   exact fixture.  Geometry is written in the variables z = 6 H x0 and
   t = H x4 (partial_0 = 6H partial_z, partial_4 = H partial_t); the arbitrary
   function a4 = a4(t).

   Exactness strategy (no FullSimplify of 16x16 matrices):
   (A) every scalar is mapped to the rational-function ring
       Q(H, m, ...)[s^(1/6), cos z, e^a4, a4', a4'', ...] modulo
       cos^2 z + (s^(1/6))^12 - 1 = 0 (an exact, complete zero test for these
       expressions: a4 is arbitrary, so e^a4 and its derivatives are independent);
   (B) independent point checks: z = arcsin(3/5) and z = arcsin(5/13)
       (exact trig values, s^(1/6) kept as a radical) with rational jets of a4,
       zero-tested exactly (e^(1/6) treated as a transcendental, coefficients
       RootReduce'd).

   Public entry point: D16PRun[repoRoot]. *)

BeginPackage["Dirac16ComplexPrimordial`"];

D16PRun::usage = "D16PRun[repoRoot] runs every Stage-2 primordial-field check. It returns an Association with keys \"checks\" (name -> True|False), \"measurements\" (name -> value) and \"components\" (data for the LaTeX document).";
D16PGammas::usage = "D16PGammas[] returns the list of the eight 16x16 gamma matrices gamma^0..gamma^7 (notebook split-octonion basis).";

Begin["`Private`"];

(* ================================================================== *)
(* 0. bookkeeping                                                      *)
(* ================================================================== *)

$checks = <||>; $meas = <||>; $comp = <||>;
addCheck[name_String, val_] := Module[{v = TrueQ[val]},
  $checks[name] = v;
  If[! v, Print["  CHECK FAILED: ", name]];
  v];
addMeas[name_String, val_] := ($meas[name] = val);
logT[msg__] := Print["[", DateString[{"Hour", ":", "Minute", ":", "Second"}], "] ", msg];
toStr[e_] := Block[{$Context = "Dirac16ComplexPrimordial`Private`",
    $ContextPath = {"System`", "Dirac16ComplexPrimordial`Private`"}},
  ToString[e, InputForm, PageWidth -> Infinity]];
boolS[b_] := If[TrueQ[b], "true", "false"];

(* ================================================================== *)
(* 1. gamma matrices (CONTRACT section 1)                              *)
(* ================================================================== *)

id4 = IdentityMatrix[4]; id8 = IdentityMatrix[8]; id16 = IdentityMatrix[16];
etaM = DiagonalMatrix[{1, 1, 1, 1, -1, -1, -1, -1}];
epsL = {1, 1, 1, 1, -1, -1, -1, -1};
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
D16PGammas[] := gamL;

cliffSubsets = Subsets[Range[0, 7]];
cliffBasis = Table[Fold[Dot, id16, G /@ s], {s, cliffSubsets}];
cliffInvT = Transpose /@ (Inverse /@ cliffBasis);
(* coefficients c_I of M = Sum_I c_I Gamma_I, Gamma_I = gamma^{i1} gamma^{i2}... (i1<i2<...) *)
cliffDecompose[m_] := Module[{c},
  c = Table[Total[Flatten[m cliffInvT[[i]]]]/16, {i, 256}];
  Select[Transpose[{cliffSubsets, c}], ! TrueQ[zeroQ[#[[2]]]] &]];

(* each row of a signed-permutation matrix: {column (0-based), entry} *)
rowPartner[mat_, n_Integer] := Module[{pos = Flatten[Position[mat[[n + 1]], x_ /; x =!= 0, {1}, Heads -> False]]},
  If[Length[pos] =!= 1, Throw[{"rowPartner", n}, d16pErr]];
  {pos[[1]] - 1, mat[[n + 1, pos[[1]]]]}];

(* ================================================================== *)
(* 2. exact ring and zero tests                                        *)
(* ================================================================== *)

(* ring variables: sg = s^(1/6) (s = sin z), cc = cos z, ea = e^a4, ad[n] = a4^(n)(t) *)
ringPow[v_, p_] := If[IntegerQ[p], v^p, Throw[{"nonIntegerPower", v, p}, d16pErr]];
ringRules = {
   Power[Sin[z], p_] :> ringPow[sg, 6 p], Power[Cos[z], p_] :> ringPow[cc, p],
   Power[Tan[z], p_] :> ringPow[sg, 6 p] ringPow[cc, -p],
   Power[Cot[z], p_] :> ringPow[cc, p] ringPow[sg, -6 p],
   Power[Sec[z], p_] :> ringPow[cc, -p], Power[Csc[z], p_] :> ringPow[sg, -6 p],
   Sin[z] -> sg^6, Cos[z] -> cc, Tan[z] -> sg^6/cc, Cot[z] -> cc/sg^6, Sec[z] -> 1/cc,
   Csc[z] -> sg^-6,
   Power[E, k_. a4[t]] :> ea^k,
   Sinh[k_. a4[t]] :> (ea^k - ea^-k)/2, Cosh[k_. a4[t]] :> (ea^k + ea^-k)/2,
   Derivative[n_][a4][t] :> ad[n]};

fieldHeads = {Ps, Pb, uu, ub, Zf, Zb, f16, Z, yZ, Phi};
fpat = (hd_Symbol[_Integer])[___] /; MemberQ[fieldHeads, hd];
dpat = (Derivative[__][hd_Symbol[_Integer]])[___] /; MemberQ[fieldHeads, hd];

(* bilinears of plane waves s^(-1/2 +- i K/(6H)) combine to rational powers of sin z only after expansion *)
cplxSinPowQ[e_] := ! FreeQ[e, Power[Sin[z], p_] /; ! (IntegerQ[p] || Head[p] === Rational)];
toRing[e_] := Module[{r = If[cplxSinPowQ[e], Expand[e], e] /. ringRules},
  If[! FreeQ[r /. {fpat :> 1, dpat :> 1}, z | t | a4 | x0 | x4 | Sin | Cos | Tan | Cot | Sec | Csc | Sinh | Cosh | Log],
   Throw[{"ringIncomplete", Short[r, 5]}, d16pErr]];
  r];
toRingX[e_] := toRing[e /. {x0 -> z/(6 H), x4 -> t/H}];

atomize[e_] := Module[{atoms = Union[Cases[{e}, fpat | dpat, Infinity]]},
  If[atoms === {}, e, e /. Dispatch[Thread[atoms -> Array[vA, Length[atoms]]]]]];

ringZeroQ[r_] := Module[{num},
  num = Numerator[Together[atomize[r]]];
  Expand[PolynomialRemainder[num, cc^2 + sg^12 - 1, cc]] === 0];
zeroQ[e_] := If[e === 0, True, ringZeroQ[toRing[e]]];
zeroXQ[e_] := If[e === 0, True, ringZeroQ[toRingX[e]]];
zeroMatQ[m_] := AllTrue[Flatten[{m}], zeroQ];

(* canonical ring normal form (for presentation): reduce cc^2 -> 1 - sg^12 in the numerator *)
ringNormal[r_] := Module[{tg = Together[r], num, den},
  num = Expand[PolynomialRemainder[Numerator[tg], cc^2 + sg^12 - 1, cc]];
  den = Denominator[tg];
  Factor[num/den]];

(* point checks (method B) *)
ptZ = {ArcSin[3/5], ArcSin[5/13]};
ptJet = {{1/2, 2/3, -1/5, 3/7, 1/11}, {-1/3, 5/4, 2/9, -1/2, 3/5}};
ptEval[e_, k_] := (e /. z -> ptZ[[k]]) /. {Derivative[n_][a4][t] :> ptJet[[k, n + 1]], a4[t] -> ptJet[[k, 1]]};
ptZeroQ[e_, k_] := Module[{r, num, vars, coeffs},
  If[e === 0, Return[True]];
  r = atomize[ptEval[e, k]];
  r = r /. {Sinh[x_] :> (E^x - E^-x)/2, Cosh[x_] :> (E^x + E^-x)/2};
  r = PowerExpand[(r /. {Power[E, p_?NumericQ] :> eps6^(6 p)}) /. E -> eps6^6]; (* eps6 = e^(1/6) > 0 *)
  If[! FreeQ[r, a4 | z | t], Throw[{"pointIncomplete", Short[r, 3]}, d16pErr]];
  num = Numerator[Together[r]];
  vars = Variables[num];
  coeffs = If[vars === {}, {num}, Last /@ CoefficientRules[Expand[num], vars]];
  AllTrue[coeffs, RootReduce[#] === 0 &]];
ptZeroMatQ[m_, k_] := AllTrue[Flatten[{m}], ptZeroQ[#, k] &];

(* ================================================================== *)
(* 3. TeX and Python printers for ring expressions                     *)
(* ================================================================== *)

$texSym = <|H -> "H", mm -> "m", lam -> "\\lambda", SS -> "S", KK -> "K", M -> "M", Q1 -> "Q_1",
   kap -> "\\kappa", kq -> "k", qq -> "q", Meff -> "M_{\\mathrm{eff}}", K0s -> "K_0", K4s -> "K_4",
   Us -> "U", Ups -> "U'"|>;
$pySym = <|H -> "H", mm -> "m", lam -> "lam", SS -> "S", KK -> "K", M -> "M", Q1 -> "Q1",
   kap -> "kappa", kq -> "k", qq -> "q", Meff -> "Meff", K0s -> "K0", K4s -> "K4", Us -> "U", Ups -> "Up"|>;
fracTeX[r_] := Module[{n = Numerator[r], d = Denominator[r]}, If[d === 1, ToString[n], ToString[n] <> "/" <> ToString[d]]];
sPowTeX[p_] := Module[{r = p/6}, Which[r === 1, "s", True, "s^{" <> If[r < 0, "-" <> fracTeX[-r], fracTeX[r]] <> "}"]];
adTeX[n_] := "a_4" <> StringRepeat["'", n];
powTeX[base_String, k_] := If[k === 1, base, base <> "^{" <> fracTeX[k] <> "}"];

(* monomial (no numeric factor) given exponent association *)
monoParts[mono_] := Module[{ex = <||>, fl},
  fl = DeleteCases[If[Head[mono] === Times, List @@ mono, {mono}], 1];
  Do[Which[
     MatchQ[f, Power[_, _]], ex[f[[1]]] = Lookup[ex, f[[1]], 0] + f[[2]],
     True, ex[f] = Lookup[ex, f, 0] + 1], {f, fl}];
  ex];
monoTeX[ex_Association] := Module[{p = Lookup[ex, sg, 0], q = Lookup[ex, cc, 0], num = {}, den = {}, trig = "", keys, v, k},
  (* tan/cot extraction *)
  Which[
   q < 0 && p > 0, trig = If[q === -1, "\\tan z", "\\tan^{" <> ToString[-q] <> "} z"]; p = p - 6 (-q); q = 0,
   q > 0 && p < 0, trig = If[q === 1, "\\cot z", "\\cot^{" <> ToString[q] <> "} z"]; p = p + 6 q; q = 0];
  If[KeyExistsQ[ex, H], AppendTo[num, powTeX["H", ex[H]]]];
  If[trig =!= "", AppendTo[num, trig]];
  If[p =!= 0, AppendTo[num, sPowTeX[p]]];
  If[q > 0, AppendTo[num, If[q === 1, "\\cos z", "\\cos^{" <> ToString[q] <> "} z"]]];
  If[q < 0, AppendTo[num, If[q === -1, "\\sec z", "\\sec^{" <> ToString[-q] <> "} z"]]];
  If[KeyExistsQ[ex, ea], k = ex[ea]; AppendTo[num, Which[k === 1, "e^{a_4}", k === -1, "e^{-a_4}", True, "e^{" <> fracTeX[k] <> "a_4}"]]];
  Do[If[KeyExistsQ[ex, ad[n]], AppendTo[num, powTeX[adTeX[n], ex[ad[n]]]]], {n, 1, 5}];
  keys = Select[Keys[ex], ! MemberQ[{sg, cc, ea, H, ad[1], ad[2], ad[3], ad[4], ad[5]}, #] &];
  Do[v = ex[kk]; If[v > 0, AppendTo[num, powTeX[Lookup[$texSym, kk, ToString[kk]], v]],
     AppendTo[den, powTeX[Lookup[$texSym, kk, ToString[kk]], -v]]], {kk, SortBy[keys, ToString]}];
  {StringRiffle[num, "\\,"], StringRiffle[den, "\\,"]}];
(* a single term: numeric coefficient times monomial *)
termTeX[term_, first_] := Module[{c, mono, ex, nd, cs, sign, body, absC},
  {c, mono} = numMono[term];
  ex = monoParts[mono];
  nd = monoTeX[ex];
  sign = If[Re[c] < 0 || (Re[c] == 0 && Im[c] < 0), "-", If[first, "", "+"]];
  absC = If[Re[c] < 0 || (Re[c] == 0 && Im[c] < 0), -c, c];
  cs = Which[absC === 1, "", absC === I, "i", Head[absC] === Rational, "\\tfrac{" <> ToString[Numerator[absC]] <> "}{" <> ToString[Denominator[absC]] <> "}",
    Head[absC] === Complex, "(" <> ToString[absC, InputForm] <> ")", True, ToString[absC]];
  body = Which[
    nd[[2]] =!= "" && IntegerQ[absC] && absC =!= 1, (cs = ""; "\\frac{" <> ToString[absC] <> If[nd[[1]] === "", "", nd[[1]]] <> "}{" <> nd[[2]] <> "}"),
    nd[[2]] =!= "", "\\frac{" <> If[nd[[1]] === "", "1", nd[[1]]] <> "}{" <> nd[[2]] <> "}",
    True, nd[[1]]];
  If[body === "" && cs === "", body = "1"];
  sign <> cs <> If[cs =!= "" && body =!= "" && StringStartsQ[body, DigitCharacter], "\\cdot ", ""] <> body];
numMono[term_] := Module[{fl = If[Head[term] === Times, List @@ term, {term}], nums, rest},
  nums = Select[fl, NumericQ]; rest = Select[fl, ! NumericQ[#] &];
  {Times @@ nums, Times @@ rest}];
polyTeX[p_] := Module[{terms = If[Head[p] === Plus, List @@ p, {p}]},
  StringJoin[MapIndexed[termTeX[#1, #2[[1]] === 1] &, terms]]];
texR[e_] := Module[{f = ringNormal[e], fl, nums, monos, polys, c, s, num, den, ps},
  If[f === 0, Return["0"]];
  fl = If[Head[f] === Times, List @@ f, {f}];
  nums = Select[fl, NumericQ];
  polys = Select[fl, (! NumericQ[#]) && (Head[#] === Plus || (Head[#] === Power && Head[#[[1]]] === Plus)) &];
  monos = Complement[fl, nums, polys];
  c = Times @@ nums;
  s = termTeX[c (Times @@ monos), True];
  If[polys === {}, Return[s]];
  Module[{posP = Select[polys, ! (Head[#] === Power && #[[2]] < 0) &], negP = Select[polys, Head[#] === Power && #[[2]] < 0 &], fmt, num, den, sgn, core},
   fmt[p_] := If[Head[p] === Power && p[[2]] =!= 1, "\\bigl(" <> polyTeX[p[[1]]] <> "\\bigr)^{" <> ToString[p[[2]]] <> "}", "\\bigl(" <> polyTeX[p] <> "\\bigr)"];
   ps = StringJoin[fmt /@ posP];
   If[negP === {},
    Which[s === "1", ps, s === "-1", "-" <> ps, True, s <> ps],
    sgn = If[StringStartsQ[s, "-"], "-", ""]; core = If[sgn === "-", StringDrop[s, 1], s];
    num = Which[core === "1" && ps =!= "", ps, core === "1", "1", True, core <> ps];
    den = StringJoin[fmt /@ (#[[1]]^(-#[[2]]) & /@ negP)];
    sgn <> "\\frac{" <> num <> "}{" <> den <> "}"]]];

(* Python/sympy printer: z, H, a4, a4p, a4pp, ...; s^(1/6) -> sin(z)**(1/6) *)
pyR[e_] := pyS[ringNormal[e]];
pyS[x_Integer] := If[x < 0, "(" <> ToString[x] <> ")", ToString[x]];
pyS[x_Rational] := "(" <> ToString[Numerator[x]] <> "/" <> ToString[Denominator[x]] <> ")";
pyS[Complex[a_, b_]] := "(" <> pyS[a] <> "+" <> pyS[b] <> "*I)";
pyS[sg] := "sin(z)**(1/6)"; pyS[cc] := "cos(z)"; pyS[ea] := "exp(a4)";
pyS[ad[n_]] := "a4" <> StringRepeat["p", n];
pyS[Power[sg, k_]] := "sin(z)**(" <> fracTeX[k/6] <> ")";
pyS[Power[ea, k_]] := "exp(" <> pyS[k] <> "*a4)";
pyS[Power[b_, k_]] := "(" <> pyS[b] <> ")**(" <> If[IntegerQ[k], ToString[k], fracTeX[k]] <> ")";
pyS[x_Plus] := "(" <> StringRiffle[pyS /@ (List @@ x), " + "] <> ")";
pyS[x_Times] := StringRiffle[pyS /@ (List @@ x), "*"];
pyS[x_Symbol] := Lookup[$pySym, x, SymbolName[x]];
pyS[x_] := ToString[x, InputForm];
exprRec[e_] := <|"tex" -> texR[toRing[e]], "py" -> pyR[toRing[e]]|>;
exprRecR[r_] := <|"tex" -> texR[r], "py" -> pyR[r]|>;

(* greedy TeX line packer *)
packTeX[tokens_List, maxLen_: 70] := Module[{lines = {}, cur = ""},
  Do[If[StringLength[cur] + StringLength[tk] > maxLen && cur =!= "",
     AppendTo[lines, cur]; cur = "\\quad " <> tk, cur = cur <> tk], {tk, tokens}];
  If[cur =!= "", AppendTo[lines, cur]];
  lines];
alignedTeX[lines_List] := StringRiffle[("&" <> #) & /@ lines, " \\\\\n"];

(* ================================================================== *)
(* 4. the primordial field (CONTRACT section 9)                        *)
(* ================================================================== *)

Yv = {z, x1, x2, x3, t, x5, x6, x7};
jac = {6 H, 1, 1, 1, H, 1, 1, 1};
d1[k_Integer, f_] := jac[[k]] D[f, Yv[[k]]]; (* partial w.r.t. x^(k-1), 1-based k *)
sF = Sin[z];
hhF = {Cot[z], sF^(1/6) E^a4[t], sF^(1/6) E^a4[t], sF^(1/6) E^a4[t], 1, sF^(1/6) E^(-a4[t]), sF^(1/6) E^(-a4[t]), sF^(1/6) E^(-a4[t])};
(* metric as written in CONTRACT section 9 (independent of the vielbein) *)
gF = DiagonalMatrix[{Cot[z]^2, sF^(1/3) E^(2 a4[t]), sF^(1/3) E^(2 a4[t]), sF^(1/3) E^(2 a4[t]), -1,
    -sF^(1/3) E^(-2 a4[t]), -sF^(1/3) E^(-2 a4[t]), -sF^(1/3) E^(-2 a4[t])}];
giF = DiagonalMatrix[1/Diagonal[gF]];
evF = DiagonalMatrix[hhF]; (* e_mu^a, rows mu *)
eiF = DiagonalMatrix[1/hhF]; (* e_a^mu, rows a *)
sqrtgF = Cos[z];

buildGeometry[] := Module[{},
  GamF = Table[(1/2) Sum[giF[[r, s]] (d1[m, gF[[s, n]]] + d1[n, gF[[s, m]]] - d1[s, gF[[m, n]]]), {s, 8}], {r, 8}, {m, 8}, {n, 8}];
  omMixF = Table[Sum[eiF[[b, n]] (Sum[GamF[[r, m, n]] evF[[r, a]], {r, 8}] - d1[m, evF[[n, a]]]), {n, 8}], {m, 8}, {a, 8}, {b, 8}];
  omLF = Table[Sum[etaM[[a, c]] omMixF[[m, c, b]], {c, 8}], {m, 8}, {a, 8}, {b, 8}];
  OmF = Table[(1/2) Sum[omLF[[m, a, b]] Sab[a - 1, b - 1], {a, 8}, {b, 8}], {m, 8}];
  OmNBF = Table[(1/2) Sum[omMixF[[m, a, b]] Sab[a - 1, b - 1], {a, 8}, {b, 8}], {m, 8}];
  gUF = Table[Sum[eiF[[a, m]] G[a - 1], {a, 8}], {m, 8}];
  gDF = Table[Sum[gF[[m, n]] gUF[[n]], {n, 8}], {m, 8}];];

(* Dirac operator gamma^mu D_mu psi - (m + lambda S) psi for a field vector psi(Yv) *)
diracOp[psi_, Om_] := Sum[gUF[[mu]].(d1[mu, psi] + Om[[mu]].psi), {mu, 8}];
elOp[psi_, meff_] := diracOp[psi, OmF] - meff psi;

(* ================================================================== *)
(* 5. notebook reader (same cell enumeration as the survey dump)       *)
(* ================================================================== *)

nbStyles = {"Input", "Code", "Text", "Section", "Subsection", "Subsubsection", "Title", "Chapter", "Item",
   "Subtitle", "DisplayFormula", "ItemNumbered", "Program"};
nbAllStyles = Join[nbStyles, {"Output", "Print", "Message"}];
loadNotebookCells[nbFile_] := Module[{nb, cells, i = 0, inputs = <||>, outs = <||>},
  nb = Get[nbFile];
  cells = Cases[nb, Cell[_, style_String, ___] /; MemberQ[nbAllStyles, style], Infinity];
  Do[If[MemberQ[nbStyles, c[[2]]], i++; inputs[i] = c; outs[i] = {},
    If[i > 0, AppendTo[outs[i], c]]], {c, cells}];
  <|"count" -> i, "inputs" -> inputs, "outputs" -> outs,
    "frontEndVersion" -> First[Append[Cases[List @@ nb, (Rule | RuleDelayed)[FrontEndVersion, v_] :> v], "-"]]|>];
nbCtx = "D16PNotebookParse`";
parseBoxes[boxes_] := Block[{$Context = nbCtx, $ContextPath = {"System`"}},
  Quiet@TimeConstrained[Check[ToExpression[boxes, StandardForm, HoldComplete], $Failed], 60, $Failed]];
heldToString[h_] := Block[{$Context = nbCtx, $ContextPath = {"System`"}},
  StringReplace[ToString[h, InputForm, PageWidth -> Infinity], {StartOfString ~~ "HoldComplete[" -> "", "]" ~~ EndOfString -> ""}]];
nbInputString[nbd_, n_] := Module[{c = nbd["inputs"][n], h},
  h = parseBoxes[c[[1]]];
  If[h === $Failed, "", heldToString[h]]];
(* map notebook symbols to this package's formal symbols and release *)
nbRelease[h_] := ReleaseHold[h /. s_Symbol /; Context[s] === nbCtx :> Symbol["Dirac16ComplexPrimordial`Private`" <> SymbolName[s]]];
nbOutput[nbd_, n_, k_] := Module[{oc = Select[nbd["outputs"][n], #[[2]] === "Output" &], h},
  If[Length[oc] < k, Return[$Failed]];
  h = parseBoxes[oc[[k, 1]]];
  If[h === $Failed, $Failed, nbRelease[h]]];
noWS[s_String] := StringJoin[Map[If[First[ToCharacterCode[#]] > 127,
      FromCharacterCode[92] <> "[" <> StringReplace[Quiet[Check[CharacterName[#], "U" <> ToString[First[ToCharacterCode[#]]]]], "Micro" -> "Mu"] <> "]", #] &,
    Characters[StringDelete[s, WhitespaceCharacter]]]];

(* ================================================================== *)
(* 6. checks                                                           *)
(* ================================================================== *)

(* ---------------- fixture ---------------- *)
checkZeroTests[] := addCheck["P_internal_zeroTestSanity",
   zeroQ[Cos[z]^2 + Sin[z]^2 - 1] && zeroQ[Tan[z] Cos[z] - Sin[z]] && ! zeroQ[Sin[z]^(1/6) - Cos[z]] && ! zeroQ[E^a4[t] - 1] &&
    ! zeroQ[a4'[t] Ps[1][z, x1, x2, x3, t, x5, x6, x7]] && zeroQ[D[Sin[z]^(1/6) E^a4[t], t] - a4'[t] Sin[z]^(1/6) E^a4[t]] &&
    And @@ Table[ptZeroQ[Cos[z]^2 + Sin[z]^2 - 1, k] && ! ptZeroQ[Sin[z]^(1/6) - Cos[z], k] && ! ptZeroQ[E^a4[t] - 1, k] &&
       ! ptZeroQ[E^(2 a4[t]) - E^a4[t], k] && ptZeroQ[Sinh[a4[t]] - (E^a4[t] - E^(-a4[t]))/2, k], {k, 2}]];
checkFixture[fixFile_] := Module[{fx},
  fx = Import[fixFile, "RawJSON"];
  addCheck["P_fixture_gammasMatchCommittedFixture", fx["gamma"] === gamL];
  addCheck["P_fixture_CAndChiralityMatch", fx["C"] === C16 && fx["chirality"] === g8];
  addCheck["P_fixture_cliffordAndC", AllTrue[Flatten[Table[G[a].G[b] + G[b].G[a] == 2 etaM[[a + 1, b + 1]] id16, {a, 0, 7}, {b, 0, 7}]], TrueQ] &&
    C16 === G[0].G[1].G[2].G[3] && g8 === DiagonalMatrix[Join[ConstantArray[-1, 8], ConstantArray[1, 8]]]];
  addCheck["P_fixture_gammaRowsSignedPermutations", AllTrue[Flatten[Table[Count[G[a][[n]], x_ /; x != 0] == 1, {a, 0, 7}, {n, 16}]], TrueQ]];];

(* ---------------- P_metric ---------------- *)
checkMetric[nbd_] := Module[{det, signs, st},
  addCheck["P_metric_vielbeinProduct", zeroMatQ[evF.etaM.Transpose[evF] - gF]];
  signs = Table[Simplify[Sign[gF[[i, i]]], 0 < z < Pi/2 && Element[a4[t], Reals]], {i, 8}];
  addMeas["metricDiagonalSigns", signs];
  addCheck["P_metric_signature44", signs === {1, 1, 1, 1, -1, -1, -1, -1}];
  det = Det[gF];
  addCheck["P_metric_detG_equals_plus_cos2z", zeroQ[det - Cos[z]^2]];
  addCheck["P_metric_sqrtAbsDetG_cosz", zeroQ[det - sqrtgF^2] && Simplify[sqrtgF > 0, 0 < z < Pi/2]];
  addMeas["detG", "cos(z)^2 (positive: four negative diagonal entries)"];
  addMeas["specDiscrepancy_detG", "STAGE2_SPEC P_metric writes det g = -cos^2 z (...); the exact product of the eight diagonal entries is +cos^2 z (sign (-1)^4 = +1), as the notebook's own cell 1060 also shows; sqrt|g| = cos z is unaffected."];
  st = nbOutput[nbd, 1060, 1];
  addCheck["P_metric_notebookCell1060Det", st =!= $Failed && zeroXQ[st - (det /. {z -> 6 H x0, t -> H x4})]];
  addCheck["P_metric_pointCheck", And @@ Table[ptZeroQ[det - Cos[z]^2, k] && ptZeroMatQ[evF.etaM.Transpose[evF] - gF, k], {k, 2}]];];

(* ---------------- P_zeta ---------------- *)
checkZeta[] := Module[{zz, dx0, gz, g1, g5, lim0, ok},
  zz = ArcSin[E^(6 H zeta)];
  dx0 = D[zz, zeta]/(6 H);
  gz = Together[(Cot[z]^2 /. z -> zz) dx0^2];
  g1 = Simplify[(Sin[z]^(1/3) /. z -> zz) == E^(2 H zeta), Element[{H, zeta}, Reals] && H > 0];
  lim0 = Limit[Log[Sin[z]]/(6 H), z -> 0, Direction -> "FromAbove", Assumptions -> H > 0];
  addCheck["P_zeta_gZetaZetaIsOne", gz === 1];
  addCheck["P_zeta_warpFactor", TrueQ[g1] && Simplify[D[Log[Sin[6 H x0]]/(6 H), x0] == Cot[6 H x0]]];
  addCheck["P_zeta_range", lim0 === -Infinity && (Log[Sin[z]]/(6 H) /. z -> Pi/2) === 0 &&
    Simplify[D[Log[Sin[z]]/(6 H), z] > 0, 0 < z < Pi/2 && H > 0]];
  (* full warped metric: dzeta^2 - dx4^2 + e^{2 H zeta}(e^{2a4} dx_i^2 - e^{-2a4} dx_j^2) *)
  ok = Simplify[(Diagonal[gF] /. z -> zz) Join[{dx0^2}, ConstantArray[1, 7]] ==
      {1, E^(2 H zeta) E^(2 a4[t]), E^(2 H zeta) E^(2 a4[t]), E^(2 H zeta) E^(2 a4[t]), -1,
       -E^(2 H zeta) E^(-2 a4[t]), -E^(2 H zeta) E^(-2 a4[t]), -E^(2 H zeta) E^(-2 a4[t])},
    Element[{H, zeta}, Reals] && H > 0 && zeta < 0];
  addCheck["P_zeta_warpedMetric", TrueQ[ok]];
  $comp["zetaForm"] = <|"definition" -> "\\zeta=\\frac{\\ln\\sin z}{6H}\\in(-\\infty,0),\\quad e^{6H\\zeta}=s=\\sin z,\\quad d\\zeta=\\cot z\\,dx_0",
     "lineElement" -> "ds^2=d\\zeta^2-dx_4^2+e^{2H\\zeta}\\bigl[e^{2a_4}(dx_1^2+dx_2^2+dx_3^2)-e^{-2a_4}(dx_5^2+dx_6^2+dx_7^2)\\bigr]",
     "sqrtAbsDetG_zeta" -> "e^{6H\\zeta}"|>;];

(* ---------------- P_christoffel ---------------- *)
expectedChristoffel[] := Module[{e = ConstantArray[0, {8, 8, 8}], sp = {2, 3, 4}, tm = {6, 7, 8}},
  e[[1, 1, 1]] = -6 H/(Sin[z] Cos[z]);
  Do[e[[1, i, i]] = -H Sin[z]^(4/3) E^(2 a4[t])/Cos[z], {i, sp}];
  Do[e[[1, i, i]] = H Sin[z]^(4/3) E^(-2 a4[t])/Cos[z], {i, tm}];
  Do[e[[i, 1, i]] = e[[i, i, 1]] = H Cot[z], {i, Join[sp, tm]}];
  Do[e[[i, 5, i]] = e[[i, i, 5]] = H a4'[t], {i, sp}];
  Do[e[[i, 5, i]] = e[[i, i, 5]] = -H a4'[t], {i, tm}];
  Do[e[[5, i, i]] = H a4'[t] Sin[z]^(1/3) E^(2 a4[t]), {i, sp}];
  Do[e[[5, i, i]] = H a4'[t] Sin[z]^(1/3) E^(-2 a4[t]), {i, tm}];
  e];
checkChristoffel[] := Module[{ex = expectedChristoffel[], nz, nzInd, list},
  addCheck["P_christoffel_closedForms512", zeroMatQ[GamF - ex]];
  nz = Select[Tuples[Range[8], 3], ! zeroQ[GamF[[#[[1]], #[[2]], #[[3]]]]] &];
  nzInd = Select[nz, #[[2]] <= #[[3]] &];
  addMeas["christoffelNonzeroCount", Length[nz]];
  addMeas["christoffelNonzeroCountMuLeNu", Length[nzInd]];
  addCheck["P_christoffel_count", Length[nz] === 37 && Length[nzInd] === 25];
  addCheck["P_christoffel_pointCheck", And @@ Table[ptZeroMatQ[GamF - ex, k], {k, 2}]];
  list = Table[Join[<|"rho" -> i[[1]] - 1, "mu" -> i[[2]] - 1, "nu" -> i[[3]] - 1,
       "label" -> "\\Gamma^{" <> ToString[i[[1]] - 1] <> "}_{" <> ToString[i[[2]] - 1] <> ToString[i[[3]] - 1] <> "}"|>,
      exprRec[GamF[[i[[1]], i[[2]], i[[3]]]]]], {i, nzInd}];
  $comp["christoffel"] = <|"convention" -> "\\Gamma^{\\rho}_{\\mu\\nu}=\\tfrac12 g^{\\rho\\sigma}(\\partial_\\mu g_{\\nu\\sigma}+\\partial_\\nu g_{\\mu\\sigma}-\\partial_\\sigma g_{\\mu\\nu}), \\partial_\\mu=\\partial/\\partial x^\\mu, s=\\sin z, z=6Hx_0, a_4=a_4(Hx_4), a_4'=da_4/dt",
     "nonzeroCount" -> Length[nz], "nonzeroCountMuLeNu" -> Length[nzInd],
     "note" -> "entries with mu<=nu listed; Gamma^rho_{nu mu} = Gamma^rho_{mu nu}", "entries" -> list|>;];

(* ---------------- P_spinconn ---------------- *)
expectedOmegaLow[] := Module[{e = ConstantArray[0, {8, 8, 8}], v},
  Do[v = H Sin[z]^(1/6) E^a4[t];
   e[[i, 1, i]] = -v; e[[i, i, 1]] = v; e[[i, 5, i]] = -v a4'[t]; e[[i, i, 5]] = v a4'[t], {i, {2, 3, 4}}];
  Do[v = H Sin[z]^(1/6) E^(-a4[t]);
   e[[j, 1, j]] = v; e[[j, j, 1]] = -v; e[[j, 5, j]] = -v a4'[t]; e[[j, j, 5]] = v a4'[t], {j, {6, 7, 8}}];
  e];
checkSpinConnection[nbd_] := Module[{ex = expectedOmegaLow[], vp, nz, st, list, listMix, nzMix},
  vp = Table[d1[m, evF[[n, a]]] - Sum[GamF[[r, m, n]] evF[[r, a]], {r, 8}] + Sum[omMixF[[m, a, b]] evF[[n, b]], {b, 8}], {m, 8}, {n, 8}, {a, 8}];
  addCheck["P_spinconn_vielbeinPostulate512", zeroMatQ[vp]];
  addCheck["P_spinconn_antisymmetry", zeroMatQ[omLF + Transpose[omLF, {1, 3, 2}]]];
  addCheck["P_spinconn_closedForms", zeroMatQ[omLF - ex]];
  nz = Select[Tuples[Range[8], 3], ! zeroQ[omLF[[#[[1]], #[[2]], #[[3]]]]] &];
  addMeas["omegaLowNonzeroCount", Length[nz]];
  addCheck["P_spinconn_count24", Length[nz] === 24];
  nzMix = Select[Tuples[Range[8], 3], ! zeroQ[omMixF[[#[[1]], #[[2]], #[[3]]]]] &];
  addMeas["omegaMixedSymmetricPairs", Length[Select[nzMix, zeroQ[omMixF[[#[[1]], #[[2]], #[[3]]]] - omMixF[[#[[1]], #[[3]], #[[2]]]]] &]]];
  st = nbOutput[nbd, 501, 1];
  addCheck["P_spinconn_notebookCell501OmegaMuIJEqualsMixedOmega",
   st =!= $Failed && Dimensions[st] === {8, 8, 8} &&
    AllTrue[Flatten[st - (omMixF /. {z -> 6 H x0, t -> H x4})], zeroXQ]];
  addCheck["P_spinconn_pointCheck", And @@ Table[ptZeroMatQ[vp, k] && ptZeroMatQ[omLF - ex, k], {k, 2}]];
  list = Table[Join[<|"mu" -> i[[1]] - 1, "a" -> i[[2]] - 1, "b" -> i[[3]] - 1,
       "label" -> "\\omega_{" <> ToString[i[[1]] - 1] <> "\\," <> ToString[i[[2]] - 1] <> ToString[i[[3]] - 1] <> "}"|>,
      exprRec[omLF[[i[[1]], i[[2]], i[[3]]]]]], {i, nz}];
  listMix = Table[Join[<|"mu" -> i[[1]] - 1, "a" -> i[[2]] - 1, "b" -> i[[3]] - 1,
       "label" -> "\\omega_{" <> ToString[i[[1]] - 1] <> "}{}^{" <> ToString[i[[2]] - 1] <> "}{}_{" <> ToString[i[[3]] - 1] <> "}"|>,
      exprRec[omMixF[[i[[1]], i[[2]], i[[3]]]]]], {i, nzMix}];
  $comp["spinConnection"] = <|"convention" -> "\\omega_\\mu{}^a{}_b=e_b{}^\\nu(\\Gamma^\\rho_{\\mu\\nu}e_\\rho{}^a-\\partial_\\mu e_\\nu{}^a),\\ \\omega_{\\mu ab}=\\eta_{ac}\\omega_\\mu{}^c{}_b=-\\omega_{\\mu ba}",
     "nonzeroCount" -> Length[nz], "lowered" -> list,
     "mixedNotebookOmegaMuIJ" -> listMix,
     "note" -> "mixedNotebookOmegaMuIJ is the notebook's omegaMuIJ (cell 501) = omega_mu^a_b; for the pairs (4,i), i=1,2,3 and (0,j), j=5,6,7 (one space-like, one time-like frame index) it is SYMMETRIC in (a,b), so the notebook contraction (1/2) omega_mu^a_b S^{ab} deletes it"|>;];

(* ---------------- P_Omega ---------------- *)
expectedOmega[] := Module[{v},
  Join[{ConstantArray[0, {16, 16}]},
   Table[-H Sin[z]^(1/6) E^a4[t] (Sab[0, i] + a4'[t] Sab[4, i]), {i, 1, 3}],
   {ConstantArray[0, {16, 16}]},
   Table[H Sin[z]^(1/6) E^(-a4[t]) (Sab[0, j] - a4'[t] Sab[4, j]), {j, 5, 7}]]];
checkOmega[] := Module[{ex = expectedOmega[], slash, slashR, formula, entries, blocks},
  addCheck["P_Omega_closedForms", zeroMatQ[OmF - ex]];
  addCheck["P_Omega_zeroForX0X4", zeroMatQ[OmF[[1]]] && zeroMatQ[OmF[[5]]]];
  addCheck["P_Omega_blockDiagonalChirality", AllTrue[OmF, zeroMatQ[#[[1 ;; 8, 9 ;; 16]]] && zeroMatQ[#[[9 ;; 16, 1 ;; 8]]] &] &&
    AllTrue[OmF, zeroMatQ[#.g8 - g8.#] &]];
  slash = Sum[gUF[[mu]].OmF[[mu]], {mu, 8}];
  addCheck["P_Omega_gammaSlash3Hgamma0", zeroMatQ[slash - 3 H G[0]]];
  addCheck["P_Omega_OmegaGammaAndAnticommutator", zeroMatQ[Sum[OmF[[mu]].gUF[[mu]], {mu, 8}] + 3 H G[0]] &&
    zeroMatQ[Sum[gUF[[mu]].OmF[[mu]] + OmF[[mu]].gUF[[mu]], {mu, 8}]]];
  slashR = toRing /@ Flatten[slash];
  addCheck["P_Omega_slashA4Independent", FreeQ[slashR, ea | ad[_]]];
  formula = (1/2) Sum[(1/hhF[[b]]) d1[b, Log[Product[If[c == b, 1, hhF[[c]]], {c, 8}]]] G[b - 1], {b, 8}];
  addCheck["P_Omega_contractDiagonalFormula", zeroMatQ[slash - formula]];
  addCheck["P_Omega_pointCheck", And @@ Table[ptZeroMatQ[OmF - ex, k] && ptZeroMatQ[slash - 3 H G[0], k], {k, 2}]];
  entries = Table[<|"mu" -> mu - 1,
      "closedForm" -> Which[mu == 1 || mu == 5, "0",
        mu <= 4, "-H\\,s^{1/6}e^{a_4}\\bigl(S^{0" <> ToString[mu - 1] <> "}+a_4'\\,S^{4" <> ToString[mu - 1] <> "}\\bigr)",
        True, "H\\,s^{1/6}e^{-a_4}\\bigl(S^{0" <> ToString[mu - 1] <> "}-a_4'\\,S^{4" <> ToString[mu - 1] <> "}\\bigr)"],
      "entries" -> Flatten[Table[If[zeroQ[OmF[[mu, r, c]]], Nothing,
          Join[<|"row" -> r - 1, "col" -> c - 1|>, exprRec[OmF[[mu, r, c]]]]], {r, 16}, {c, 16}]]|>, {mu, 8}];
  $comp["Omega"] = <|"convention" -> "\\Omega_\\mu=\\tfrac12\\omega_{\\mu ab}S^{ab}=\\tfrac18\\omega_{\\mu ab}[\\gamma^a,\\gamma^b],\\ S^{ab}=\\tfrac14[\\gamma^a,\\gamma^b]=\\tfrac12\\gamma^a\\gamma^b\\ (a\\ne b)",
     "blockForm" -> "every \\Omega_\\mu is block diagonal, \\Omega_\\mu=\\mathrm{diag}(\\Omega_\\mu^{(-)},\\Omega_\\mu^{(+)}) on \\Psi_{0..7} (chirality -1) and \\Psi_{8..15} (chirality +1); upper block (1/2)\\omega_{\\mu ab}\\tfrac14(\\bar\\tau_a\\tau_b-\\bar\\tau_b\\tau_a), lower block (1/2)\\omega_{\\mu ab}\\tfrac14(\\tau_a\\bar\\tau_b-\\tau_b\\bar\\tau_a)",
     "gammaSlashOmega" -> "\\gamma^\\mu\\Omega_\\mu=3H\\gamma^0,\\quad \\Omega_\\mu\\gamma^\\mu=-3H\\gamma^0,\\quad \\{\\gamma^\\mu,\\Omega_\\mu\\}=0\\ (a_4\\text{ cancels})",
     "matrices" -> entries|>;];

(* ---------------- P_gammaConst ---------------- *)
covGamma[Om_] := Table[d1[m, gUF[[n]]] + Sum[GamF[[n, m, l]] gUF[[l]], {l, 8}] + Om[[m]].gUF[[n]] - gUF[[n]].Om[[m]], {m, 8}, {n, 8}];
checkGammaConst[] := Module[{dg, dgNB, badPairs, sample, lhs, rhs, rhsNB, entriesNB},
  dg = covGamma[OmF];
  addCheck["P_gammaConst_DmuGammaNuZero64", zeroMatQ[dg]];
  dgNB = covGamma[OmNBF];
  badPairs = Select[Tuples[Range[8], 2], ! zeroMatQ[dgNB[[#[[1]], #[[2]]]]] &];
  entriesNB = Count[Flatten[dgNB], x_ /; ! zeroQ[x]];
  addMeas["notebookContraction_DmuGammaNu_nonzeroPairs", Length[badPairs]];
  addMeas["notebookContraction_DmuGammaNu_nonzeroEntries", entriesNB];
  addMeas["notebookContraction_DmuGammaNu_pairs", ToString[(# - 1) & /@ badPairs]];
  sample = cliffDecompose[dgNB[[2, 5]]];
  addMeas["notebookContraction_sample_D1gamma4", StringRiffle[("(" <> texR[toRing[#[[2]]]] <> ")\\gamma^{" <> StringJoin[ToString /@ #[[1]]] <> "}") & /@ sample, " + "]];
  addCheck["P_gammaConst_notebookContractionFails", Length[badPairs] > 0];
  (* closed forms of the 15 nonzero D_mu gamma^nu of the notebook contraction (document Section 8.3), in frame gammas *)
  Module[{ex = ConstantArray[0 id16, {8, 8}]},
   Do[ex[[i, i]] = H a4'[t] G[4]; ex[[i, 5]] = H Sin[z]^(1/6) E^a4[t] a4'[t] G[i - 1], {i, {2, 3, 4}}];
   Do[ex[[j, 1]] = H Sin[z]^(7/6) E^(-a4[t]) Sec[z] G[j - 1]; ex[[j, 5]] = 2 H Sin[z]^(1/6) E^(-a4[t]) a4'[t] G[j - 1];
    ex[[j, j]] = H G[0] - 2 H a4'[t] G[4], {j, {6, 7, 8}}];
   addCheck["P_gammaConst_notebookContractionClosedForms", Length[badPairs] === 15 && entriesNB === 288 && zeroMatQ[dgNB - ex]];
   addMeas["notebookContraction_closedForms", "(i,i): H a4' gamma^4; (i,4): H s^{1/6} e^{a4} a4' gamma^i; (j,0): H s^{7/6} e^{-a4} sec z gamma^j; (j,4): 2H s^{1/6} e^{-a4} a4' gamma^j; (j,j): H gamma^0 - 2H a4' gamma^4 (i = 1,2,3; j = 5,6,7; all other pairs zero)"]];
  lhs =Sum[d1[mu, sqrtgF gUF[[mu]]], {mu, 8}];
  rhs = sqrtgF Sum[gUF[[mu]].OmF[[mu]] - OmF[[mu]].gUF[[mu]], {mu, 8}];
  rhsNB = sqrtgF Sum[gUF[[mu]].OmNBF[[mu]] - OmNBF[[mu]].gUF[[mu]], {mu, 8}];
  addCheck["P_gammaConst_divergenceIdentity", zeroMatQ[lhs - rhs]];
  addCheck["P_gammaConst_divergenceIdentityFailsNotebookContraction", ! zeroMatQ[lhs - rhsNB]];
  addMeas["divergenceIdentity_lhs", "\\partial_\\mu(\\sqrt{|g|}\\gamma^\\mu)=6H\\cos z\\,\\gamma^0 = \\sqrt{|g|}[\\gamma^\\mu,\\Omega_\\mu]"];
  addCheck["P_gammaConst_divergenceLhsValue", zeroMatQ[lhs - 6 H Cos[z] G[0]]];
  addCheck["P_gammaConst_pointCheck", And @@ Table[ptZeroMatQ[dg, k] && ptZeroMatQ[lhs - rhs, k], {k, 2}]];];

(* ---------------- P_EL ---------------- *)
coefTeXMain = {"\\tan z", "s^{-1/6}e^{-a_4}", "s^{-1/6}e^{-a_4}", "s^{-1/6}e^{-a_4}", "", "s^{-1/6}e^{a_4}", "s^{-1/6}e^{a_4}", "s^{-1/6}e^{a_4}"};
coefPyMain = {"tan(z)", "sin(z)**(-1/6)*exp(-a4)", "sin(z)**(-1/6)*exp(-a4)", "sin(z)**(-1/6)*exp(-a4)", "1",
   "sin(z)**(-1/6)*exp(a4)", "sin(z)**(-1/6)*exp(a4)", "sin(z)**(-1/6)*exp(a4)"};
sgnS[s_, first_] := If[s < 0, "-", If[first, "", "+"]];
psiTeX[k_] := "\\Psi_{" <> ToString[k] <> "}";
(* TeX lines of row n of gamma^mu D_mu Psi = M Psi in a given presentation *)
elTeX[n_, style_] := Module[{p, tok = {}, grp, k0, s0, k4, s4, pre, d},
  p = Table[rowPartner[G[mu], n], {mu, 0, 7}];
  {k0, s0} = p[[1]]; {k4, s4} = p[[5]];
  d[mu_] := Switch[style, "zeta", If[mu == 0, "\\partial_{\\zeta}", "\\partial_{" <> ToString[mu] <> "}"],
     "x0", "\\partial_{x_{" <> ToString[mu] <> "}}", "zt", Which[mu == 0, "\\partial_{z}", mu == 4, "\\partial_{t}", True, "\\partial_{" <> ToString[mu] <> "}"],
     _, "\\partial_{" <> ToString[mu] <> "}"];
  pre = Switch[style,
    "zeta", {"\\bigl(" <> d[0] <> "+3H\\bigr)", d[4], "e^{-H\\zeta-a_4}", "e^{-H\\zeta+a_4}"},
    "x0", {"\\bigl(\\tan(6Hx_0)\\," <> d[0] <> "+3H\\bigr)", d[4], "\\sin^{-1/6}(6Hx_0)\\,e^{-a_4(Hx_4)}", "\\sin^{-1/6}(6Hx_0)\\,e^{a_4(Hx_4)}"},
    "zt", {"\\bigl(6H\\tan z\\," <> d[0] <> "+3H\\bigr)", "H\\," <> d[4], "s^{-1/6}e^{-a_4}", "s^{-1/6}e^{a_4}"},
    _, {"\\bigl(\\tan z\\," <> d[0] <> "+3H\\bigr)", d[4], "s^{-1/6}e^{-a_4}", "s^{-1/6}e^{a_4}"}];
  AppendTo[tok, sgnS[s0, True] <> pre[[1]] <> psiTeX[k0]];
  AppendTo[tok, sgnS[s4, False] <> pre[[2]] <> psiTeX[k4]];
  AppendTo[tok, "+" <> pre[[3]] <> "\\bigl("];
  Do[AppendTo[tok, sgnS[p[[mu + 1, 2]], mu == 1] <> d[mu] <> psiTeX[p[[mu + 1, 1]]]], {mu, 1, 3}];
  AppendTo[tok, "\\bigr)"];
  AppendTo[tok, "+" <> pre[[4]] <> "\\bigl("];
  Do[AppendTo[tok, sgnS[p[[mu + 1, 2]], mu == 5] <> d[mu] <> psiTeX[p[[mu + 1, 1]]]], {mu, 5, 7}];
  AppendTo[tok, "\\bigr)"];
  AppendTo[tok, "=(m+\\lambda S)\\," <> psiTeX[n]];
  packTeX[tok, 70]];
(* evolution form: partial_4 Psi_n = sum_{mu != 4} c_mu (g4 g^mu)[n,k] partial_mu Psi_k + 3H (g4 g0)[n,k] Psi_k - Meff (g4)[n,k] Psi_k *)
evoTerms[n_] := Module[{terms = {}, k, s},
  Do[If[mu =!= 4, {k, s} = rowPartner[G[4].G[mu], n];
     AppendTo[terms, {k, mu, s/hhF[[mu + 1]]}]], {mu, 0, 7}];
  {k, s} = rowPartner[G[4].G[0], n]; AppendTo[terms, {k, "none", 3 H s}];
  {k, s} = rowPartner[G[4], n]; AppendTo[terms, {k, "none", -s (mm + lam SS)}];
  terms];
evoTeX[n_] := Module[{tok = {"\\partial_{4}" <> psiTeX[n] <> "="}, first = True, k, s},
  Do[If[mu =!= 4, {k, s} = rowPartner[G[4].G[mu], n];
     AppendTo[tok, sgnS[s, first] <> If[coefTeXMain[[mu + 1]] === "", "", coefTeXMain[[mu + 1]] <> "\\,"] <> "\\partial_{" <> ToString[mu] <> "}" <> psiTeX[k]];
     first = False], {mu, 0, 7}];
  {k, s} = rowPartner[G[4].G[0], n]; AppendTo[tok, sgnS[s, False] <> "3H\\," <> psiTeX[k]];
  {k, s} = rowPartner[G[4], n]; AppendTo[tok, sgnS[-s, False] <> "(m+\\lambda S)\\," <> psiTeX[k]];
  packTeX[tok, 70]];
termRec[{k_, mu_, c_}] := Module[{rec = Join[exprRec[c], <|"wl" -> toStr[c]|>], sg1},
  rec["tex"] = Which[
    mu =!= "none", sg1 = Together[c hhF[[mu + 1]]];
     If[! MemberQ[{1, -1}, sg1], Throw[{"termRec", c}, d16pErr]];
     If[sg1 === -1, "-", ""] <> If[coefTeXMain[[mu + 1]] === "", "1", coefTeXMain[[mu + 1]]],
    Together[c/(3 H)] === 1, "3H", Together[c/(3 H)] === -1, "-3H",
    Together[c/(mm + lam SS)] === 1, "m+\\lambda S", Together[c/(mm + lam SS)] === -1, "-(m+\\lambda S)",
    True, rec["tex"]];
  <|"component" -> k, "derivative" -> mu, "coefficient" -> rec|>];
checkEL[] := Module[{psi, psib, S0, op, recon, terms, okRows, okStruct, evo, ok3, Lag, Dpsi, Dpsib, ELb, ELp, tgtb, tgtp, pts, eqs},
  psi = Table[Ps[n] @@ Yv, {n, 0, 15}];
  op = elOp[psi, mm + lam SS];
  terms = Table[Join[
     Table[With[{pr = rowPartner[G[mu], n]}, {pr[[1]], mu, pr[[2]]/hhF[[mu + 1]]}], {mu, 0, 7}],
     {With[{pr = rowPartner[G[0], n]}, {pr[[1]], "none", 3 H pr[[2]]}]},
     {{n, "none", -(mm + lam SS)}}], {n, 0, 15}];
  recon = Table[Sum[tr[[3]] If[tr[[2]] === "none", Ps[tr[[1]]] @@ Yv, d1[tr[[2]] + 1, Ps[tr[[1]]] @@ Yv]], {tr, terms[[n + 1]]}], {n, 0, 15}];
  okRows = AllTrue[Range[16], zeroQ[op[[#]] - recon[[#]]] &];
  addCheck["P_EL_componentsMatchOperator", okRows];
  okStruct = AllTrue[terms, Length[#] === 10 &];
  addCheck["P_EL_tenTermsPerEquation", okStruct];
  addCheck["P_EL_pointCheck", And @@ Table[AllTrue[Range[16], ptZeroQ[op[[#]] - recon[[#]], k] &], {k, 2}]];
  (* evolution form *)
  evo = Table[Sum[tr[[3]] If[tr[[2]] === "none", Ps[tr[[1]]] @@ Yv, d1[tr[[2]] + 1, Ps[tr[[1]]] @@ Yv]], {tr, evoTerms[n]}], {n, 0, 15}];
  addCheck["P_EL_evolutionFormEquivalent", zeroMatQ[op - G[4].(d1[5, psi] - evo)]];
  (* derivation from the Lagrangian of CONTRACT section 5 (Psi^dagger varied independently) *)
  psib = Table[Pb[n] @@ Yv, {n, 0, 15}];
  S0 = psib.C16.psi;
  Dpsi = Table[d1[mu, psi] + OmF[[mu]].psi, {mu, 8}];
  Dpsib = Table[d1[mu, psib.C16] - psib.C16.OmF[[mu]], {mu, 8}];
  Lag = sqrtgF ((1/2) Sum[psib.C16.gUF[[mu]].Dpsi[[mu]] - Dpsib[[mu]].gUF[[mu]].psi, {mu, 8}] - mm S0 - (lam/2) S0^2);
  ELb = Table[D[Lag, Pb[a] @@ Yv] - Sum[D[D[Lag, D[Pb[a] @@ Yv, Yv[[k]]]], Yv[[k]]], {k, 8}], {a, 0, 15}];
  tgtb = sqrtgF C16.(elOp[psi, mm + lam S0]);
  addCheck["P_EL_fromLagrangianPsiDagger", AllTrue[Range[16], zeroQ[ELb[[#]] - tgtb[[#]]] &]];
  ELp = Table[D[Lag, Ps[a] @@ Yv] - Sum[D[D[Lag, D[Ps[a] @@ Yv, Yv[[k]]]], Yv[[k]]], {k, 8}], {a, 0, 15}];
  tgtp = -sqrtgF (Sum[Dpsib[[mu]].gUF[[mu]], {mu, 8}] + (mm + lam S0) psib.C16);
  addCheck["P_EL_fromLagrangianPsi", AllTrue[Range[16], zeroQ[ELp[[#]] - tgtp[[#]]] &]];
  (* zeta form: tan z d/dx0 = d/dzeta, s^(-1/6) = e^(-H zeta) *)
  addCheck["P_EL_zetaFormChainRule", Simplify[Cot[6 H x0] == D[Log[Sin[6 H x0]]/(6 H), x0]] &&
    Simplify[Exp[-H Log[Sin[z]]/(6 H)] == Sin[z]^(-1/6), 0 < z < Pi/2]];
  eqs = Table[<|"n" -> n,
      "terms" -> (termRec /@ terms[[n + 1]]),
      "texLines" -> elTeX[n, "main"], "tex" -> alignedTeX[elTeX[n, "main"]],
      "texLinesX0" -> elTeX[n, "x0"], "texLinesZeta" -> elTeX[n, "zeta"], "texLinesZT" -> elTeX[n, "zt"],
      "evolution" -> <|"terms" -> (termRec /@ evoTerms[n]), "texLines" -> evoTeX[n]|>|>, {n, 0, 15}];
  $comp["eulerLagrange"] = <|
    "equation" -> "\\gamma^\\mu D_\\mu\\Psi=(m+U'(S))\\Psi,\\ U=\\tfrac{\\lambda}{2}S^2,\\ S=\\bar\\Psi\\Psi",
    "explicit" -> "\\tan z\\,\\gamma^0\\partial_0\\Psi+s^{-1/6}e^{-a_4}\\gamma^i\\partial_i\\Psi+\\gamma^4\\partial_4\\Psi+s^{-1/6}e^{a_4}\\gamma^j\\partial_j\\Psi+3H\\gamma^0\\Psi=(m+\\lambda S)\\Psi\\ (i=1,2,3;\\ j=5,6,7)",
    "conventions" -> "row n of the matrix equation; \\partial_\\mu=\\partial/\\partial x^\\mu, z=6Hx_0, s=\\sin z, a_4=a_4(Hx_4); each gamma row has one entry \\pm1; terms: {component k, derivative index mu or none, coefficient}; the 'none' terms are 3H(gamma^0)_{nk} Psi_k and -(m+lambda S) Psi_n",
    "texConventions" -> "texLines: short math lines (no alignment marks); tex: the same lines prefixed with & and joined by \\\\ for an aligned environment; texLinesX0: explicit x0,x4 form; texLinesZeta: zeta form; texLinesZT: z,t form (partial_0=6H partial_z, partial_4=H partial_t)",
    "evolutionFormNote" -> "multiplying by -gamma^4 (gamma^4 gamma^4 = -1): partial_4 Psi = -(m+lambda S) gamma^4 Psi + 3H gamma^4 gamma^0 Psi + sum_{mu!=4} (1/h_mu) gamma^4 gamma^mu partial_mu Psi",
    "equations" -> eqs|>;];

(* ---------------- P_blocks ---------------- *)
nbSets = {{0, 5, 8, 13}, {1, 4, 9, 12}, {2, 7, 10, 15}, {3, 6, 11, 14}};
checkBlocks[] := Module[{adj, gr, comps, closed, blocksOut},
  adj = Table[Boole[G[0][[n, k]] != 0 || G[4][[n, k]] != 0 || n == k], {n, 16}, {k, 16}];
  comps = Sort[Sort /@ (ConnectedComponents[AdjacencyGraph[Sign[adj + Transpose[adj]]]] - 1)];
  addMeas["x0x4BlocksCorrectEquations", ToString[comps]];
  addCheck["P_blocks_fourBlocksOfFour", Length[comps] === 4 && AllTrue[comps, Length[#] === 4 &]];
  closed = AllTrue[comps, Function[bl, AllTrue[bl, Function[n, MemberQ[bl, rowPartner[G[0], n][[1]]] && MemberQ[bl, rowPartner[G[4], n][[1]]]]]]];
  addCheck["P_blocks_closedUnderCoupling", closed];
  addCheck["P_blocks_matchNotebookSets", comps === Sort[nbSets]];
  blocksOut = Table[<|"components" -> bl,
      "equationsZT" -> Table[<|"n" -> n, "texLines" -> packTeX[{
            "H\\,\\partial_{t}\\Psi_{" <> ToString[n] <> "}=",
            Module[{k, s}, {k, s} = rowPartner[G[4].G[0], n]; sgnS[s, True] <> "\\bigl(6H\\tan z\\,\\partial_{z}+3H\\bigr)\\Psi_{" <> ToString[k] <> "}"],
            Module[{k, s}, {k, s} = rowPartner[G[4], n]; If[s > 0, "-", "+"] <> "(m+\\lambda S)\\,\\Psi_{" <> ToString[k] <> "}"]}, 70]|>, {n, bl}]|>, {bl, comps}];
  $comp["blocksX0X4"] = <|"statement" -> "for Psi = Psi(x0,x4) the equations reduce to tan z gamma^0 partial_0 Psi + gamma^4 partial_4 Psi + 3H gamma^0 Psi = (m+lambda S) Psi; the coupling graph (gamma^0, gamma^4 partners) has four connected components of four components each",
     "blocks" -> blocksOut, "notebookCouplingSets" -> nbSets, "agreeWithNotebook" -> (comps === Sort[nbSets]),
     "note" -> "no a4 appears: gamma^mu Omega_mu = 3H gamma^0 is a4-independent and the a4-dependent coefficients multiply partial_1..3, partial_5..7 only"|>;];

(* ---------------- P_notebookCompare ---------------- *)
constraintVarsNB := Module[{},
  (x0 > 0 && x4 > 0 && H > 0 && 6*H*x0 > 0 && 3*H*x4 > 0 && a4[x4] > 0 && A4[t] > 0 && Q > 0 && z > 0 && t > 0 && M > 0 && K > 0 &&
     E^(-2*a4[H*x4]) > 0 && E^(-a4[H*x4]) > 0 && E^(2*a4[H*x4]) > 0 && E^a4[H*x4] > 0) &&
   (Sin[6*H*x0] > 0 && Cos[6*H*x0] > 0 && Csc[6*H*x0] > 0 && Sec[6*H*x0] > 0 && Tan[6*H*x0] > 0 && Cot[6*H*x0] > 0 && Sin[z] > 0 &&
     Sqrt[Sin[z]] > 0 && Sin[z]^(3/2) > 0 && Sin[z]^(1/2) > 0 && Sin[z]^(-3/2) > 0 && Sin[z]^(-2^(-1)) > 0 && Cot[z] > 0 && Sqrt[Cot[z]] > 0 &&
     Cot[z]^(3/2) > 0 && Cot[z]^(1/2) > 0 && Tan[z] > 0 && Sec[z] > 0 && Sqrt[Csc[z]] > 0 && Csc[z] > 0)];
posPart[m_] := Map[If[# === 1, 1, 0] &, m, {2}];
negPart[m_] := Map[If[# === -1, -1, 0] &, m, {2}];

nbExpectedSnippets = {
   {106, "\[CapitalPsi]16=(f16[#1][x0,x4]&)/@Range[0,15]"},
   {111, "f16[#1]->ToExpression[StringJoin[\"((Z[\",ToString[#1],\"][6*H*#1,H*#2])&)\"]]"},
   {386, "\[Sigma]16=(T16^A)[0].(T16^A)[1].(T16^A)[2].(T16^A)[3]"},
   {431, "SAB=Table[(1/4)*((T16^A)[A1].(T16^A)[B1]-(T16^A)[B1].(T16^A)[A1]),{A1,0,7},{B1,0,7}]"},
   {475, "(T16^\[Alpha])[\[Alpha]1-1]=Sum["},
   {499, "-Table[FullSimplify[Sum[D[eI\[Nu][[I1,\[Nu]1]],X[[\[Mu]1]]]*e\[Nu]I[[\[Nu]1,Jprime]],{\[Nu]1,1,Length[e\[Nu]I]}]-Sum[eI\[Nu][[I1,\[Rho]]]*\[CapitalGamma][[\[Rho],\[Mu]1,\[Nu]1]]*e\[Nu]I[[\[Nu]1,Jprime]]"},
   {501, "\[Omega]\[Mu]IJ[\[Mu]]=FullSimplify[-(D[Subscript[gtrye,\[Alpha]]^A,X[[\[Mu]]]].Subscript[gtrye,A]^\[Alpha]-Subscript[gtrye,\[Alpha]]^A.\[CapitalGamma][[All,\[Mu],All]].Subscript[gtrye,A]^\[Alpha])"},
   {1058, "1/Sqrt[Sin[6*H*x0]^(1/3)/E^(2*a4[H*x4])]->1/(E^a4[H*x4]*Sin[6*H*x0]^(1/6))"},
   {1061, "useDSQRT=Cos[6*H*x0]"},
   {1066, "La[]:=(Simplify[#1,constraintVars]&)[useDSQRT*(Transpose[\[CapitalPsi]16].\[Sigma]16.Sum[useT16[[\[Alpha]1]].(D[\[CapitalPsi]16,X[[\[Alpha]1]]]+(Q1/2)*Sum[\[Omega]\[Mu]IJ[\[Alpha]1][[A1,B1]]*SAB[[A1,B1]],{A1,1,8},{B1,1,8}].\[CapitalPsi]16),{\[Alpha]1,1,Length[X]}]+(H*M)*Transpose[\[CapitalPsi]16].\[Sigma]16.\[CapitalPsi]16)]"},
   {1075, "(1/detsqrt)*(D[L,f16[k][x0,x4]]-D[D[L,Derivative[1,0][f16[k]][x0,x4]],x0]-D[D[L,Derivative[0,1][f16[k]][x0,x4]],x4])"},
   {1078, "eLa=eL[La,useDSQRT]"},
   {1096, "eLazt=(FullSimplify[#1,constraintVars]&)[(1/(2*H))*eLa/.sf\[Psi]16Aa/.sx0x4]"},
   {1111, "sZtOyZ=Thread[(Z[#1]&)/@Flatten[eLaztCouplings]->(yZ[#1]&)/@Range[0,15]]"},
   {1137, "coupledyZeqs=Partition[%[[1]],4]"}};

(* the notebook rebuild, in the notebook's own coordinates x0..x7 *)
nbRebuild[] := Module[{X, hx, gx, gix, Gx, ex, eix, wNB, w499, wCorrect, psi, eL, uT, SAB, La, variants, zz, aa},
  X = {x0, x1, x2, x3, x4, x5, x6, x7};
  zz = 6 H x0; aa = a4[H x4];
  hx = {Cot[zz], Sin[zz]^(1/6) E^aa, Sin[zz]^(1/6) E^aa, Sin[zz]^(1/6) E^aa, 1, Sin[zz]^(1/6) E^-aa, Sin[zz]^(1/6) E^-aa, Sin[zz]^(1/6) E^-aa};
  gx = DiagonalMatrix[epsL hx^2]; gix = DiagonalMatrix[1/(epsL hx^2)];
  Gx = Table[(1/2) Sum[gix[[r, s]] (D[gx[[s, m]], X[[n]]] + D[gx[[s, n]], X[[m]]] - D[gx[[m, n]], X[[s]]]), {s, 8}], {r, 8}, {m, 8}, {n, 8}];
  ex = DiagonalMatrix[hx]; eix = DiagonalMatrix[1/hx];
  (* cell 501: omegaMuIJ[mu] = -(D[e, X[[mu]]].einv - e.Gamma[[All,mu,All]].einv) *)
  wNB = Table[-(D[ex, X[[m]]].eix - ex.Gx[[All, m, All]].eix), {m, 8}];
  (* cell 499 spinCoefficients[eI nu], literally: w[[mu1, I1, J']] = -(Sum_nu d_mu e[[I1,nu]] einv[[nu,J']] - Sum_{nu,rho} e[[I1,rho]] Gamma[[rho,mu1,nu]] einv[[nu,J']]) *)
  w499 = Table[-(Sum[D[ex[[I1, n1]], X[[m1]]] eix[[n1, J1]], {n1, 8}] - Sum[ex[[I1, r1]] Gx[[r1, m1, n1]] eix[[n1, J1]], {n1, 8}, {r1, 8}]), {m1, 8}, {I1, 8}, {J1, 8}];
  wCorrect = Table[etaM.wNB[[m]], {m, 8}];
  SAB = Table[Sab[a, b], {a, 0, 7}, {b, 0, 7}];
  psi = Table[f16[k][x0, x4], {k, 0, 15}];
  eL[L_] := Table[(1/Cos[zz]) (D[L, f16[k][x0, x4]] - D[D[L, Derivative[1, 0][f16[k]][x0, x4]], x0] -
        D[D[L, Derivative[0, 1][f16[k]][x0, x4]], x4]), {k, 0, 15}];
  La[uTT_, w_] := Cos[zz] (psi.C16.Sum[uTT[[m]].(D[psi, X[[m]]] + (Q1/2) Sum[w[[m, A, B]] SAB[[A, B]], {A, 8}, {B, 8}].psi), {m, 8}] + H M psi.C16.psi);
  <|"X" -> X, "hx" -> hx, "wNB" -> wNB, "w499" -> w499, "wCorrect" -> wCorrect, "psi" -> psi, "eL" -> eL, "La" -> La, "zz" -> zz, "aa" -> aa|>];

toZT[eLaList_] := Module[{r},
  r = (1/(2 H)) eLaList /. f16[k_] :> (Z[k][6 H #1, H #2] &);
  r /. {x0 -> z/(6 H), x4 -> t/H}];
dtSolve[eqs_, heads_] := Module[{vars = Table[Derivative[0, 1][heads[[j]]][z, t], {j, Length[heads]}], sol},
  sol = Solve[Thread[0 == eqs], vars];
  If[Length[sol] =!= 1, Throw[{"dtSolve", Length[sol]}, d16pErr]];
  vars /. sol[[1]]];

checkNotebookCompare[nbd_] := Module[{YS, rb, st1079, st1096, st1089, st1111, st1137, uTlit, cc1058, uTcorr, uTv3, eLit, eV1, eV3, eCorrOm, qvec,
    qFormula, Y, dz, couplings, sZ, relabel, dtZ, rel, dtY, recon, stEqs, okStored, corrZ, corrDt, corrY, diffs, qsym, diffInfo, ok,
    litPattern, gp, cellsOK, snips, rawSets, graph, sets, reconSets, v3sq, v3clifford, dq, perEq, dtZstored},
  (* provenance of the rebuilt code *)
  snips = Table[{s[[1]], StringContainsQ[noWS[nbInputString[nbd, s[[1]]]], noWS[s[[2]]]]}, {s, nbExpectedSnippets}];
  addMeas["notebookSourceCellsMatched", ToString[snips]];
  addCheck["P_notebookCompare_sourceCellsAsRebuilt", AllTrue[snips, #[[2]] &]];
  rb = nbRebuild[];
  addCheck["P_notebookCompare_spinCoefficientsCell499EqualsOmegaMuIJ", AllTrue[Flatten[rb["w499"] - rb["wNB"]], zeroXQ] &&
    nbOutput[nbd, 519, 1] === {0} && AllTrue[Flatten[rb["wNB"] - (omMixF /. {z -> 6 H x0, t -> H x4})], zeroXQ]];
  (* cell 1058 literally, with the notebook's constraintVars, in this kernel *)
  Module[{gsym, eAa, einv, T16al, ssg},
   eAa = DiagonalMatrix[{Sqrt[gg[0][0][x0, x4]], Sqrt[gg[1][1][x0, x4]], Sqrt[gg[2][2][x0, x4]], Sqrt[gg[3][3][x0, x4]],
      Sqrt[-gg[4][4][x0, x4]], Sqrt[-gg[5][5][x0, x4]], Sqrt[-gg[6][6][x0, x4]], Sqrt[-gg[7][7][x0, x4]]}];
   einv = Inverse[eAa];
   T16al = Table[Sum[einv[[a1, A1]] G[A1 - 1], {A1, 1, 8}], {a1, 1, 8}];
   ssg = {gg[0][0] -> (Cot[6*H*#1]^2 &), gg[1][1] -> (E^(2*a4[H*#2])*Sin[6*H*#1]^(1/3) &), gg[2][2] -> (E^(2*a4[H*#2])*Sin[6*H*#1]^(1/3) &),
     gg[3][3] -> (E^(2*a4[H*#2])*Sin[6*H*#1]^(1/3) &), gg[4][4] -> (-1 &), gg[5][5] -> ((-E^(-2*a4[H*#2]))*Sin[6*H*#1]^(1/3) &),
     gg[6][6] -> ((-E^(-2*a4[H*#2]))*Sin[6*H*#1]^(1/3) &), gg[7][7] -> ((-E^(-2*a4[H*#2]))*Sin[6*H*#1]^(1/3) &)};
   uTlit = Table[FullSimplify[T16al[[a1]] /. ssg, constraintVarsNB] /. {Sqrt[E^(-2*a4[H*x4])] -> E^(-a4[H*x4]),
         Sqrt[E^(2*a4[H*x4])*Sin[6*H*x0]^(1/3)] -> E^a4[H*x4]*Sin[6*H*x0]^(1/6),
         1/Sqrt[E^(2*a4[H*x4])*Sin[6*H*x0]^(1/3)] -> 1/(E^a4[H*x4]*Sin[6*H*x0]^(1/6))}, {a1, 1, 8}] /.
     {1/Sqrt[Sin[6*H*x0]^(1/3)/E^(2*a4[H*x4])] -> 1/(E^a4[H*x4]*Sin[6*H*x0]^(1/6)), Sqrt[E^(2*a4[H*x4])] -> E^a4[H*x4]}];
  uTcorr = Table[G[m - 1]/rb["hx"][[m]], {m, 8}];
  (* reconstruction V3: only the +1 entries of gamma^5,6,7 received the (wrong) factor e^{-a4} s^{-1/6} *)
  uTv3 = Table[If[m >= 6, E^rb["aa"] Sin[rb["zz"]]^(-1/6) negPart[G[m - 1]] + E^(-rb["aa"]) Sin[rb["zz"]]^(-1/6) posPart[G[m - 1]], G[m - 1]/rb["hx"][[m]]], {m, 8}];
  litPattern = Table[Module[{d = Union[Flatten[uTlit[[m]] - uTcorr[[m]]]]}, If[AllTrue[d, zeroXQ], "correct",
      Which[zeroMatQ[toRingX /@ (uTlit[[m]] - (E^(-2 rb["aa"])) uTcorr[[m]])], "uniform e^{-a4} (wrong)",
       True, "other"]]], {m, 8}];
  addMeas["cell1058LiteralThisKernel_curvedGammaStatus", ToString[litPattern]];
  addMeas["cell1058LiteralThisKernel_version", $Version];
  st1079 = nbOutput[nbd, 1079, 1];
  eLit = rb["eL"][rb["La"][uTlit, rb["wNB"]]];
  eV1 = rb["eL"][rb["La"][uTcorr, rb["wNB"]]];
  eV3 = rb["eL"][rb["La"][uTv3, rb["wNB"]]];
  eCorrOm = rb["eL"][rb["La"][uTcorr, rb["wCorrect"]]];
  addCheck["P_notebookCompare_storedEla16", st1079 =!= $Failed && Length[st1079] === 16];
  addCheck["P_notebookCompare_commutingQ1DropsOutCliffordGammas", FreeQ[Together[toRingX /@ eV1], Q1] && FreeQ[Together[toRingX /@ eCorrOm], Q1] &&
    AllTrue[Range[16], zeroXQ[eV1[[#]] - eCorrOm[[#]]] &]];
  qvec = st1079 - eV1;
  addMeas["notebookEla_minus_cliffordRebuild_nonzeroComponents", Count[qvec, x_ /; ! zeroXQ[x]]];
  addCheck["P_notebookCompare_reconstructionReproducesStoredEla", AllTrue[Range[16], zeroXQ[eV3[[#]] - st1079[[#]]] &]];
  ok = AllTrue[Range[16], zeroXQ[eLit[[#]] - st1079[[#]]] &];
  addMeas["cell1058LiteralThisKernel_reproducesStoredEla", boolS[ok]];
  addCheck["P_notebookCompare_literalRebuildResidualIsExactlyQTerms", ok || AllTrue[Range[16], zeroXQ[eLit[[#]] - st1079[[#]] + qvec[[#]]] &]];
  (* the q vector (stored eLa minus the Clifford-consistent rebuild, cell-1079 normalisation) from the non-Clifford
     gamma^{x5,x6,x7}: Q1 (sigma16 Y + (sigma16 Y)^T) Psi with Y = Sum_j (gamma'^{x_j} - gamma^{x_j}) OmegaNB_j,
     OmegaNB_j = (1/2) omega_j^A_B S^{AB}; equivalently (Q1/2)(...) with Y built from omega_j^A_B S^{AB} (YS below) *)
  YS = Sum[(uTv3[[m]] - uTcorr[[m]]).Sum[rb["wNB"][[m, A, B]] Sab[A - 1, B - 1], {A, 8}, {B, 8}], {m, 6, 8}];
  Y = Sum[(uTv3[[m]] - uTcorr[[m]]).((1/2) Sum[rb["wNB"][[m, A, B]] Sab[A - 1, B - 1], {A, 8}, {B, 8}]), {m, 6, 8}];
  qFormula = Q1 (C16.Y + Transpose[C16.Y]).rb["psi"];
  addCheck["P_notebookCompare_qTermFromNonCliffordExtraTimeGammas", AllTrue[Range[16], zeroXQ[qvec[[#]] - qFormula[[#]]] &] &&
    AllTrue[Range[16], zeroXQ[qvec[[#]] - ((Q1/2) (C16.YS + Transpose[C16.YS]).rb["psi"])[[#]]] &]];
  (* normalisation: at the eLa level (cell 1079) each nonzero row of the q vector is +-2H q Psi_k, i.e. +-q after the
     factor 1/(2H) of cell 1096; q = Q1 sinh(a4) a4' e^{-a4} *)
  Module[{qx = Q1 Sinh[rb["aa"]] Derivative[1][a4][H x4] E^(-rb["aa"]), rows},
   rows = Table[Module[{r = Together[toRingX[qvec[[k]]]], q2 = toRingX[2 H qx], at, c},
      at = Union[Cases[{r}, f16[_][__] | Derivative[__][f16[_]][__], Infinity]];
      Which[r === 0, {k - 1, 0},
       Length[at] === 1 && MatchQ[at[[1]], f16[_][__]], c = Together[Coefficient[r, at[[1]]]/q2];
        If[MemberQ[{1, -1}, c] && ringZeroQ[r - c q2 at[[1]]], {k - 1, c, at[[1, 0, 1]]}, {k - 1, "other"}],
       True, {k - 1, "other"}]], {k, 16}];
   addMeas["notebookEla_qVectorRows_sign_partner", ToString[rows]];
   addCheck["P_notebookCompare_qVectorIs2HqAtCell1079", Count[rows, {_, _Integer, _Integer}] === 8 && Count[rows, {_, 0}] === 8]];
  v3sq = uTv3[[6]].uTv3[[6]];
  v3clifford = zeroMatQ[toRingX /@ (v3sq - (1/(epsL[[6]] rb["hx"][[6]]^2)) id16)];
  addCheck["P_notebookCompare_reconstructedGamma5NotClifford", ! v3clifford];
  addMeas["reconstructedGammaX5Squared", "(gamma'^{x5})^2 = " <> StringRiffle[texR[#] & /@ Union[toRingX /@ Diagonal[v3sq]], ", "] <>
     " times 1 (off-diagonal zero: " <> boolS[zeroMatQ[toRingX /@ (v3sq - DiagonalMatrix[Diagonal[v3sq]])]] <> "); Clifford requires g^{55} = -s^{-1/3} e^{2a4}"];
  addMeas["reconstructedGammaX5_anticommutesWithGammaX6", boolS[zeroMatQ[toRingX /@ (uTv3[[6]].uTv3[[7]] + uTv3[[7]].uTv3[[6]])]]];
  addMeas["reconstructedGammaX5_anticommutesWithGammaX0", boolS[zeroMatQ[toRingX /@ (uTv3[[6]].uTv3[[1]] + uTv3[[1]].uTv3[[6]])]]];
  addMeas["reconstructedGammaX5_form", "gamma'^{x_j} = s^{-1/6}(cosh(a4) gamma^j - sinh(a4) |gamma^j|), |gamma^j| = entrywise absolute value (j = 5,6,7)"];
  addCheck["P_notebookCompare_reconstructedGammaForm", AllTrue[{6, 7, 8}, zeroMatQ[toRingX /@ (uTv3[[#]] - Sin[rb["zz"]]^(-1/6) (Cosh[rb["aa"]] G[# - 1] - Sinh[rb["aa"]] Abs[G[# - 1]]))] &]];
  (* transformation chain: eLazt (cell 1096) *)
  st1096 = nbOutput[nbd, 1096, 2];
  dz = toZT[eV3];
  addCheck["P_notebookCompare_eLaztCell1096", st1096 =!= $Failed && AllTrue[Range[16], zeroQ[dz[[#]] - st1096[[2, #]]] &]];
  (* couplings (cells 1085-1092) *)
  rawSets = Union /@ (Cases[#, f16[n_Integer][__] | Derivative[__][f16[n_Integer]][__] :> n, Infinity] & /@ st1079);
  graph = Graph[Range[0, 15], Flatten[Table[UndirectedEdge[rs[[1]], #] & /@ rs, {rs, rawSets}]]];
  sets = Sort[Sort /@ ConnectedComponents[graph]];
  st1089 = nbOutput[nbd, 1089, 1];
  addCheck["P_notebookCompare_couplingSetsCell1089", sets === Sort[nbSets] && st1089 === nbSets];
  (* relabelling (cell 1111) *)
  sZ = Thread[(Z /@ Flatten[nbSets]) -> (yZ /@ Range[0, 15])];
  st1111 = nbOutput[nbd, 1111, 1];
  addCheck["P_notebookCompare_relabelCell1111", st1111 === sZ];
  (* solve for d/dt (cells 1103-1137) *)
  dtZ = dtSolve[dz, Table[Z[k], {k, 0, 15}]];
  rel = Table[Derivative[0, 1][Z[k]][z, t] - dtZ[[k + 1]], {k, 0, 15}] /. sZ;
  dtY = dtSolve[rel, Table[yZ[j], {j, 0, 15}]];
  st1137 = nbOutput[nbd, 1137, 2];
  stEqs = If[st1137 === $Failed, {}, Flatten[st1137]];
  okStored = Length[stEqs] === 16 && AllTrue[Range[16], Function[j, stEqs[[j, 1]] === Derivative[0, 1][yZ[j - 1]][z, t] &&
        zeroQ[stEqs[[j, 2]] - dtY[[j]]]]];
  addCheck["P_notebookCompare_cell1137Reproduced16of16", okStored];
  (* correct equations (Grassmann-correct Lagrangian, m = -H M, U = 0) in the same variables *)
  corrZ = elOp[Table[Z[k][z, t], {k, 0, 15}], -H M];
  corrDt = dtSolve[corrZ, Table[Z[k], {k, 0, 15}]];
  corrY = dtSolve[Table[Derivative[0, 1][Z[k]][z, t] - corrDt[[k + 1]], {k, 0, 15}] /. sZ, Table[yZ[j], {j, 0, 15}]];
  qsym = Q1 Sinh[a4[t]] a4'[t] E^(-a4[t]);
  diffInfo = Table[Module[{d = stEqs[[j, 2]] - corrY[[j]], c},
      c = Together[toRing[Coefficient[Expand[d], yZ[j - 1][z, t]]]/toRing[qsym]];
      {j - 1, If[zeroQ[d], 0, c], zeroQ[d - c qsym yZ[j - 1][z, t]] && MemberQ[{-1, 0, 1}, c]}], {j, 16}];
  addCheck["P_notebookCompare_correctVsStoredDifferOnlyByQ", AllTrue[diffInfo, #[[3]] &]];
  addMeas["qTermSignsByYZ", ToString[diffInfo[[All, {1, 2}]]]];
  addCheck["P_notebookCompare_qOnlyInYZ0to7", (DeleteCases[diffInfo, {_, 0, _}][[All, 1]]) === Range[0, 7]];
  (* store comparison data *)
  perEq = Table[<|"yZ" -> j - 1, "Z" -> (Flatten[nbSets])[[j]], "Psi" -> (Flatten[nbSets])[[j]],
      "notebookStoredTeX" -> nbEqTeX[stEqs[[j]], j - 1], "correctTeX" -> nbEqTeX[Derivative[0, 1][yZ[j - 1]][z, t] == corrY[[j]], j - 1],
      "difference" -> If[diffInfo[[j, 2]] === 0, "none", If[diffInfo[[j, 2]] === 1, "+q\\,yZ_{" <> ToString[j - 1] <> "}", "-q\\,yZ_{" <> ToString[j - 1] <> "}"]]|>, {j, 16}];
  $comp["notebookComparison"] = <|
    "crossReference" -> Table[<|"Psi" -> k, "f16" -> k, "Z" -> k, "yZ" -> First[Flatten[Position[Flatten[nbSets], k]]] - 1|>, {k, 0, 15}],
    "variables" -> "notebook: f16[k](x0,x4) = Z[k](z,t) = Psi_k, z = 6Hx0, t = Hx4; yZ relabelling of cell 1111: yZ_{4b+i} = Z[(coupling set b)_i]",
    "q" -> "q=Q_1\\sinh(a_4)\\,a_4'\\,e^{-a_4}=\\tfrac12 Q_1a_4'(1-e^{-2a_4})",
    "rebuild" -> "La[] of cell 1066 rebuilt with commuting f16[k](x0,x4), useDSQRT = cos(6Hx0), omegaMuIJ of cell 501 (= omega_mu^a_b), (Q1/2) Sum omegaMuIJ[[A,B]] SAB[[A,B]], mass (H M) Psi^T sigma16 Psi, and the notebook's eL[] (cell 1075)",
    "findings" -> {
      "With Clifford-consistent curved gammas gamma^mu = e_a^mu gamma^a, every Q1 term drops out of the commuting-field Euler-Lagrange equations (sigma16 gamma^mu Omega_mu has no symmetric part for a diagonal vielbein), for the notebook contraction and for the correct Omega alike.",
      "The stored eLa (cell 1079) contains Q1 terms in the 8 rows of the coupling sets {0,5,8,13} and {1,4,9,12}. They are reproduced EXACTLY (16/16 rows, zero residual) by the reconstruction in which the curved gammas gamma^{x5}, gamma^{x6}, gamma^{x7} of useT16 (cell 1058) carry the factor e^{-a4} s^{-1/6} on their +1 entries and e^{+a4} s^{-1/6} on their -1 entries, i.e. gamma'^{x_j} = s^{-1/6}(cosh(a4) gamma^j - sinh(a4)|gamma^j|); the correct curved gamma is e^{+a4} s^{-1/6} gamma^j. No Clifford-consistent choice of curved gammas produces any Q1 term.",
      "Origin: cell 1058 contains the substitution rule 1/Sqrt[Sin[6Hx0]^(1/3)/E^(2a4)] -> 1/(E^a4 Sin[6Hx0]^(1/6)), which is mathematically wrong (the correct right-hand side is E^a4/Sin[6Hx0]^(1/6)). The stored eLa is consistent with this rule having hit only the +1 entries in the stored session. The notebook does not store the value of useT16, so the partial application, and hence the attribution of the q term to cell 1058, is a reconstruction; the exact 16/16 match confirms the reconstructed useT16, not the mechanism of the partial application. Such a gamma'^{x5..7} is not in the Clifford algebra, sigma16 gamma'^{x_j} S^{4j} acquires a symmetric part, and the commuting EL equations pick up the q vector (stored eLa minus the Clifford-consistent rebuild) = Q1 (sigma16 Y + (sigma16 Y)^T) Psi, Y = Sum_{j=5..7} (gamma'^{x_j} - gamma^{x_j}) OmegaNB_j, OmegaNB_j = (1/2) omega_j^A_B S^{AB}; its size is the difference of the two factors, s^{-1/6}(e^{a4}-e^{-a4}), times omega_j^4_j = H a4' s^{1/6} e^{-a4}, i.e. 2H q with q = Q1 sinh(a4) a4' e^{-a4} = Q1 a4'(e^{a4}-e^{-a4}) e^{-a4}/2 at the eLa level (cell 1079), and q after the factor 1/(2H) of cell 1096.",
      "In this kernel the literal re-execution of cell 1058 applies the wrong factor to all entries (uniform e^{-a4}); the EL equations then contain no q term and differ from the stored eLa by exactly the q terms.",
      "The correct equations (CONTRACT section 5, Grassmann fields, m = -H M, U = 0) in the same variables coincide with the stored cell-1137 blocks EXCEPT for the q terms: +-q yZ_j in the blocks {0,5,8,13} and {1,4,9,12} (yZ_0..yZ_7), nothing in the blocks {2,7,10,15} and {3,6,11,14} (yZ_8..yZ_15). In the correct theory no a4 dependence at all survives for fields of (x0,x4)."},
    "literalCell1058ThisKernel" -> ToString[litPattern],
    "equations" -> perEq|>;];
nbEqTeX[eq_, j_] := Module[{rhs = eq[[2]], atoms, tok = {}, c, first = True},
  atoms = Union[Cases[{rhs}, yZ[_][z, t] | Derivative[1, 0][yZ[_]][z, t], Infinity]];
  AppendTo[tok, "\\partial_t yZ_{" <> ToString[j] <> "}="];
  Do[c = Coefficient[Expand[rhs], a];
   AppendTo[tok, Module[{r = Module[{rq = Together[toRing[c]/toRing[Q1 Sinh[a4[t]] a4'[t] E^(-a4[t])]]},
         Which[rq === 1, "q", rq === -1, "-q", True, texR[toRing[c]]]], s},
      s = If[StringStartsQ[r, "-"], r, If[first, r, "+" <> r]];
      s = Which[s === "1", "", s === "+1", "+", s === "-1", "-", True, s <> "\\,"];
      s <> If[MatchQ[a, Derivative[1, 0][_][__]], "\\partial_z yZ_{" <> ToString[a[[0, 1, 1]]] <> "}", "yZ_{" <> ToString[a[[0, 1]]] <> "}"]]];
   first = False, {a, atoms}];
  packTeX[tok, 70]];

(* ---------------- P_EMT ---------------- *)
emtLower[psi_, psib_, meffLag_, uU_] := Module[{Dp, Db, psibar, Ls},
  psibar = psib.C16;
  Dp = Table[d1[mu, psi] + OmF[[mu]].psi, {mu, 8}];
  Db = Table[d1[mu, psibar] - psibar.OmF[[mu]], {mu, 8}];
  Ls = (1/2) Sum[psibar.gUF[[mu]].Dp[[mu]] - Db[[mu]].gUF[[mu]].psi, {mu, 8}] - meffLag (psibar.psi) - uU;
  <|"T" -> Table[-(1/4) (psibar.gDF[[mu]].Dp[[nu]] + psibar.gDF[[nu]].Dp[[mu]] - Db[[mu]].gDF[[nu]].psi - Db[[nu]].gDF[[mu]].psi) + gF[[mu, nu]] Ls, {mu, 8}, {nu, 8}],
    "Ls" -> Ls, "Dp" -> Dp, "Db" -> Db, "psibar" -> psibar|>];
checkEMT[] := Module[{A, nzA, Arec, psi, psib, e8, Tf, ok, psiH, psibH, eH, SH, K0H, K4H, rhoH, UH, onRules, onRules2, onRulesK0, r11, r02, Tup, div, gC,
    mixed, homog, offd, psiZ, psibZ, eZ, rhsZ, rhsZb, rules1, rules2, TupZ, divZ, zv, KEH, rhoOn},
  A = Table[gDF[[mu]].OmF[[nu]] + OmF[[nu]].gDF[[mu]] + gDF[[nu]].OmF[[mu]] + OmF[[mu]].gDF[[nu]], {mu, 8}, {nu, 8}];
  nzA = Select[Select[Tuples[Range[8], 2], #[[1]] <= #[[2]] &], ! zeroMatQ[A[[#[[1]], #[[2]]]]] &];
  addMeas["EMT_anticommutatorNonzeroPairsMuLeNu", Length[nzA]];
  Arec = Table[<|"mu" -> p[[1]] - 1, "nu" -> p[[2]] - 1,
      "clifford" -> Map[<|"gammaProduct" -> #[[1]], "tex" -> "\\gamma^{" <> StringRiffle[ToString /@ #[[1]], "}\\gamma^{"] <> "}",
          "coefficient" -> exprRec[#[[2]]]|> &, cliffDecompose[A[[p[[1]], p[[2]]]]]]|>, {p, nzA}];
  addCheck["P_EMT_anticommutatorsAreThreeGammaProducts", AllTrue[Arec, AllTrue[#["clifford"], Length[#["gammaProduct"]] === 3 &] &]];
  (* T_mu nu formula check (general Psi of all coordinates, off-shell): Omega-part = -(1/4) Psibar A Psi *)
  psi = Table[Ps[n] @@ Yv, {n, 0, 15}]; psib = Table[Pb[n] @@ Yv, {n, 0, 15}];
  e8 = emtLower[psi, psib, mm, (lam/2) (psib.C16.psi)^2];
  Tf = Table[-(1/4) (psib.C16.gDF[[mu]].d1[nu, psi] + psib.C16.gDF[[nu]].d1[mu, psi] - d1[mu, psib.C16].gDF[[nu]].psi - d1[nu, psib.C16].gDF[[mu]].psi) -
      (1/4) psib.C16.A[[mu, nu]].psi + gF[[mu, nu]] e8["Ls"], {mu, 8}, {nu, 8}];
  ok = AllTrue[Select[Tuples[Range[8], 2], #[[1]] <= #[[2]] &], zeroQ[e8["T"][[#[[1]], #[[2]]]] - Tf[[#[[1]], #[[2]]]]] &];
  addCheck["P_EMT_OmegaPartIsMinusQuarterPsibarAPsi", ok];
  addCheck["P_EMT_symmetric", zeroMatQ[e8["T"] - Transpose[e8["T"]]]];
  (* homogeneous sector: Psi = e^{-3 H zeta} e^{i K zeta} u(t) = s^{-1/2 + i K/(6H)} u(t) *)
  psiH = Table[Sin[z]^(-1/2 + I KK/(6 H)) uu[n][t], {n, 0, 15}];
  psibH = Table[Sin[z]^(-1/2 - I KK/(6 H)) ub[n][t], {n, 0, 15}];
  SH = psibH.C16.psiH;
  UH = Us;
  eH = emtLower[psiH, psibH, mm, UH];
  K0H = I KK psibH.C16.G[0].psiH;
  K4H = (1/2) (eH["psibar"].G[4].eH["Dp"][[5]] - eH["Db"][[5]].G[4].psiH);
  rhoH = eH["T"][[5, 5]];
  addCheck["P_EMT_homogeneous_rhoOffShell", zeroQ[rhoH - (mm SH + UH - K0H)]];
  addCheck["P_EMT_homogeneous_LsOffShell", zeroQ[eH["Ls"] - (K4H + K0H - mm SH - UH)]];
  mixed = Table[giF[[i, i]] eH["T"][[i, i]], {i, 8}];
  addCheck["P_EMT_homogeneous_pressuresOffShell", zeroQ[mixed[[1]] - (eH["Ls"] - K0H)] && AllTrue[{2, 3, 4, 6, 7, 8}, zeroQ[mixed[[#]] - eH["Ls"]] &]];
  KEH = -(1/2) Sum[If[mu == 5, 0, eH["psibar"].gUF[[mu]].eH["Dp"][[mu]] - eH["Db"][[mu]].gUF[[mu]].psiH], {mu, 8}];
  addCheck["P_EMT_homogeneous_KEH_equals_minusK0", zeroQ[KEH + K0H]];
  addCheck["P_EMT_T44equals_mSplusU_zeroMode", zeroQ[(rhoH /. KK -> 0) - (mm SH + UH /. KK -> 0)]];
  (* on shell: H du/dt = -gamma^4 (Meff - i K gamma^0) u, conjugate for ub (real gammas, real Meff) *)
  onRules = Join[
    Table[Derivative[1][uu[n]][t] -> (-(1/H) G[4].(Meff Table[uu[k][t], {k, 0, 15}] - I KK G[0].Table[uu[k][t], {k, 0, 15}]))[[n + 1]], {n, 0, 15}],
    Table[Derivative[1][ub[n]][t] -> (-(1/H) G[4].(Meff Table[ub[k][t], {k, 0, 15}] + I KK G[0].Table[ub[k][t], {k, 0, 15}]))[[n + 1]], {n, 0, 15}]];
  addCheck["P_EMT_homogeneous_onShell_K4plusK0_equals_MeffS", zeroQ[((K4H + K0H) /. onRules) - Meff SH]];
  onRules2 = Join[Table[Derivative[2][uu[n]][t] -> (D[Derivative[1][uu[n]][t] /. onRules, t] /. onRules), {n, 0, 15}],
    Table[Derivative[2][ub[n]][t] -> (D[Derivative[1][ub[n]][t] /. onRules, t] /. onRules), {n, 0, 15}]];
  addCheck["P_EMT_reductionSolvesDiracEquation", zeroMatQ[Expand[elOp[psiH, Meff] Sin[z]^(1/2 - I KK/(6 H))] /. onRules]];
  rhoOn = rhoH /. onRules;
  addCheck["P_EMT_homogeneous_frozenInX4", zeroQ[D[mm SH - K0H, t] /. onRules /. Meff -> mm] &&
    zeroQ[(D[SH, t] /. onRules) /. KK -> 0]];
  addCheck["P_EMT_homogeneous_a4Independent", FreeQ[toRing /@ {rhoH, eH["Ls"], K0H, K4H, SH, KEH}, ea | ad[_]]];
  (* conservation, homogeneous sector, lambda = 0 *)
  Tup = Table[giF[[mu, mu]] eH["T"][[mu, nu]], {mu, 8}, {nu, 8}] /. Us -> 0;
  div = Table[Sum[d1[mu, Tup[[mu, nu]]], {mu, 8}] + Sum[GamF[[mu, mu, l]] Tup[[l, nu]], {mu, 8}, {l, 8}] -
      Sum[GamF[[l, mu, nu]] Tup[[mu, l]], {mu, 8}, {l, 8}], {nu, 8}];
  addCheck["P_EMT_homogeneous_conservationOnShell", zeroMatQ[((div /. onRules2) /. onRules) /. Meff -> mm]];
  addCheck["P_EMT_homogeneous_conservationFailsOffShell", ! zeroMatQ[div]];
  offd = Select[Select[Tuples[Range[8], 2], #[[1]] < #[[2]] &], ! zeroQ[eH["T"][[#[[1]], #[[2]]]]] &];
  addMeas["EMT_homogeneous_offDiagonalNonzeroOffShell", ToString[(# - 1) & /@ offd]];
  addMeas["contractNote_homogeneousReduction", "Psi = e^{-3H zeta} e^{i K zeta} u(x4) solves the Dirac equation exactly iff M_eff is zeta-independent: exact for U = 0 (M_eff = m); for lambda != 0 the condensate S = u^dagger C u / sin z makes M_eff = m + lambda S depend on z, so NUMERICS_CONTRACT EXP-1's reduction gamma^4 u' = (M_eff - i K gamma^0) u holds pointwise with M_eff treated as given (mean field), not as an exact solution."];
  addMeas["contractNote_TiiHomogeneous", "CONTRACT section 7 'T_ii = g_ii (S U' - U) (isotropic)': in this field T^i_i = S U' - U holds exactly for the six transverse directions 1,2,3,5,6,7; along x0 (the direction of the plane wave) T^0_0 = S U' - U - K_0 with K_0 = i K Psibar gamma^0 Psi, so isotropy requires K = 0."];
  (* conservation in the full (x0,x4) sector, lambda = 0, general Psi(z,t) *)
  psiZ = Table[Zf[n][z, t], {n, 0, 15}]; psibZ = Table[Zb[n][z, t], {n, 0, 15}];
  eZ = emtLower[psiZ, psibZ, mm, 0];
  rhsZ = -(1/H) G[4].(mm psiZ - 3 H G[0].psiZ - 6 H Tan[z] G[0].D[psiZ, z]);
  rhsZb = -(1/H) G[4].(mm psibZ - 3 H G[0].psibZ - 6 H Tan[z] G[0].D[psibZ, z]);
  addCheck["P_EMT_x0x4EvolutionEquationIsEL", zeroMatQ[elOp[psiZ, mm] /. Table[Derivative[0, 1][Zf[n]][z, t] -> rhsZ[[n + 1]], {n, 0, 15}]]];
  rules1 = Join[Table[Derivative[0, 1][Zf[n]][z, t] -> rhsZ[[n + 1]], {n, 0, 15}], Table[Derivative[0, 1][Zb[n]][z, t] -> rhsZb[[n + 1]], {n, 0, 15}]];
  r11 = Join[Table[Derivative[1, 1][Zf[n]][z, t] -> D[rhsZ[[n + 1]], z], {n, 0, 15}], Table[Derivative[1, 1][Zb[n]][z, t] -> D[rhsZb[[n + 1]], z], {n, 0, 15}]];
  r02 = Join[Table[Derivative[0, 2][Zf[n]][z, t] -> ((D[rhsZ[[n + 1]], t] /. r11) /. rules1), {n, 0, 15}],
    Table[Derivative[0, 2][Zb[n]][z, t] -> ((D[rhsZb[[n + 1]], t] /. r11) /. rules1), {n, 0, 15}]];
  rules2 = Join[r11, r02];
  TupZ = Table[giF[[mu, mu]] eZ["T"][[mu, nu]], {mu, 8}, {nu, 8}];
  divZ = Table[Sum[d1[mu, TupZ[[mu, nu]]], {mu, 8}] + Sum[GamF[[mu, mu, l]] TupZ[[l, nu]], {mu, 8}, {l, 8}] -
      Sum[GamF[[l, mu, nu]] TupZ[[mu, l]], {mu, 8}, {l, 8}], {nu, 8}];
  addCheck["P_EMT_conservationOnShellX0X4Sector", zeroMatQ[((divZ /. rules2) /. rules1)]];
  addCheck["P_EMT_conservationFailsOffShellX0X4Sector", ! zeroMatQ[divZ]];
  (* off-diagonal transverse-transverse components in the homogeneous sector: Omega part only *)
  addCheck["P_EMT_homogeneous_offDiagonalTransverseFromA", AllTrue[Select[Tuples[{2, 3, 4, 6, 7, 8}, 2], #[[1]] < #[[2]] &],
     zeroQ[eH["T"][[#[[1]], #[[2]]]] + (1/4) eH["psibar"].A[[#[[1]], #[[2]]]].psiH] &] && zeroMatQ[A[[1, 5]]]];
  (* kept for the source analysis of checkSource[] (checks P_source_...) *)
  $emt = <|"A" -> A, "eH" -> eH, "SH" -> SH, "psiH" -> psiH, "psibH" -> psibH, "K0H" -> K0H, "psiZ" -> psiZ, "psibZ" -> psibZ|>;
  (* components for the document *)
  $comp["EMT"] = <|
    "definition" -> "T_{\\mu\\nu}=-\\tfrac14\\bigl[\\bar\\Psi\\gamma_\\mu D_\\nu\\Psi+\\bar\\Psi\\gamma_\\nu D_\\mu\\Psi-(D_\\mu\\bar\\Psi)\\gamma_\\nu\\Psi-(D_\\nu\\bar\\Psi)\\gamma_\\mu\\Psi\\bigr]+g_{\\mu\\nu}\\mathcal L_s",
    "inThisField" -> "T_{\\mu\\nu}=-\\tfrac14\\bigl[\\bar\\Psi\\gamma_\\mu\\partial_\\nu\\Psi+\\bar\\Psi\\gamma_\\nu\\partial_\\mu\\Psi-\\partial_\\mu\\bar\\Psi\\gamma_\\nu\\Psi-\\partial_\\nu\\bar\\Psi\\gamma_\\mu\\Psi\\bigr]-\\tfrac14\\bar\\Psi A_{\\mu\\nu}\\Psi+g_{\\mu\\nu}\\mathcal L_s,\\ A_{\\mu\\nu}=\\{\\gamma_\\mu,\\Omega_\\nu\\}+\\{\\gamma_\\nu,\\Omega_\\mu\\},\\ \\gamma_\\mu=g_{\\mu\\mu}\\gamma^\\mu=\\epsilon_\\mu h_\\mu\\gamma^{a=\\mu}",
    "lowerGammas" -> "\\gamma_0=\\cot z\\,\\gamma^0,\\ \\gamma_i=s^{1/6}e^{a_4}\\gamma^i,\\ \\gamma_4=-\\gamma^4,\\ \\gamma_j=-s^{1/6}e^{-a_4}\\gamma^j",
    "anticommutators" -> Arec,
    "homogeneousSector" -> <|
      "ansatz" -> "\\Psi=e^{-3H\\zeta}e^{iK\\zeta}u(x_4)=s^{-1/2+iK/(6H)}u(x_4),\\ k=q=0",
      "bilinears" -> "S=\\bar\\Psi\\Psi=s^{-1}u^\\dagger Cu,\\ K_0=iK\\,s^{-1}u^\\dagger C\\gamma^0u,\\ K_4=\\tfrac12(\\bar\\Psi\\gamma^4\\partial_4\\Psi-\\partial_4\\bar\\Psi\\gamma^4\\Psi)",
      "offShell" -> <|"rho" -> "\\rho=T_{44}=mS+U-K_0", "Ls" -> "\\mathcal L_s=K_4+K_0-mS-U",
        "p0" -> "p_{(0)}=T^0{}_0=\\mathcal L_s-K_0", "pTransverse" -> "p_{(i)}=T^i{}_i=\\mathcal L_s\\ (i=1,2,3,5,6,7)",
        "KE_L" -> "KE_L=\\tfrac12K_4", "PE_L" -> "PE_L=\\rho-KE_L", "KE_H" -> "KE_H=-\\tfrac12\\sum_{j\\ne4}(\\bar\\Psi\\gamma^jD_j\\Psi-D_j\\bar\\Psi\\gamma^j\\Psi)=-K_0", "PE_H" -> "PE_H=mS+U"|>,
      "onShell" -> <|"reduction" -> "\\gamma^4\\dot u=(M_{\\mathrm{eff}}-iK\\gamma^0)u,\\ \\dot u=du/dx_4,\\ M_{\\mathrm{eff}}=m+U'(S)",
        "Ls" -> "\\mathcal L_s=SU'-U", "rho" -> "\\rho=mS+U-K_0",
        "p0" -> "p_{(0)}=SU'-U-K_0", "pTransverse" -> "p_{(1,2,3,5,6,7)}=SU'-U",
        "KE_L" -> "KE_L=\\tfrac12\\bigl(S(m+U')-K_0\\bigr)", "PE_L" -> "PE_L=\\tfrac12\\bigl(mS+2U-SU'\\bigr)-\\tfrac12K_0",
        "KE_H" -> "KE_H=-K_0", "PE_H" -> "PE_H=mS+U",
        "K0isotropic" -> "K=0:\\ \\rho=mS+U,\\ p=SU'-U\\ (\\text{all seven transverse directions}),\\ w=\\frac{SU'-U}{mS+U}=\\frac{KE_L-PE_L}{KE_L+PE_L}",
        "freeMassive" -> "U=0,\\ K=0:\\ KE_L=PE_L=\\tfrac12mS,\\ p=0\\ (w=0)",
        "defaultU" -> "U=\\tfrac\\lambda2S^2,\\ K=0:\\ \\rho=mS+\\tfrac\\lambda2S^2,\\ p=\\tfrac\\lambda2S^2,\\ w=\\frac{\\lambda S}{2m+\\lambda S},\\ KE_L=\\tfrac12S(m+\\lambda S),\\ PE_L=\\tfrac12mS",
        "anisotropicK" -> "K\\ne0:\\ w_{(0)}=p_{(0)}/\\rho=(SU'-U-K_0)/(mS+U-K_0),\\ w_{(i)}=(SU'-U)/(mS+U-K_0)\\ (i\\ne0,4)"|>,
      "offDiagonal" -> "T_{ij}=-\\tfrac14\\bar\\Psi A_{ij}\\Psi for transverse i\\ne j (only pairs across the groups \\{1,2,3\\},\\{5,6,7\\} are nonzero); T_{0i}, T_{4i}, T_{04} contain in addition the vector bilinears K\\bar\\Psi\\gamma_i\\Psi-type derivative terms; a diagonal metric needs states with vanishing expectation values of these",
      "frozen" -> "for U=0 (any K) \\partial_4\\rho=0 on shell; for K=0 (any M_eff) \\partial_4 S=0; no a_4 appears anywhere",
      "zetaDependence" -> "every bilinear carries e^{-6H\\zeta}=1/\\sin z; for \\lambda\\ne0 the ansatz is exact only with M_eff treated as given (the condensate S\\propto1/\\sin z makes U'(S) z-dependent)",
      "offDiagonalOffShell" -> ToString[(# - 1) & /@ offd]|>|>;];

(* ---------------- P_modes ---------------- *)
checkModes[] := Module[{h, E2, ev, psiA, res, hl, keff, qeff, E2l, onset, ahh, herm},
  herm[m_] := Transpose[m] /. Complex[a_, b_] :> Complex[a, -b];
  h = -I Meff G[4] - KK G[4].G[0];
  addCheck["P_modes_dispersion", zeroMatQ[h.h - (Meff^2 + KK^2) id16] && herm[h] === h && Tr[h] === 0];
  ev = Eigenvalues[h /. {Meff -> 3, KK -> 4}];
  addCheck["P_modes_spectrumPlusMinusE8each", Sort[ev] === Join[ConstantArray[-5, 8], ConstantArray[5, 8]]];
  (* reduction: row equations with the ansatz and d/dx4 u = -gamma^4 (Meff - i K gamma^0) u *)
  psiA = Table[Sin[z]^(-1/2 + I KK/(6 H)) uu[n][t], {n, 0, 15}];
  res = Expand[elOp[psiA, Meff] Sin[z]^(1/2 - I KK/(6 H))] - (H G[4].D[Table[uu[n][t], {n, 0, 15}], t] + I KK G[0].Table[uu[n][t], {n, 0, 15}] - Meff Table[uu[n][t], {n, 0, 15}]);
  addCheck["P_modes_exactReduction", zeroMatQ[res]];
  (* k != 0 or q != 0: the reduced operator depends explicitly on z *)
  Module[{psiK, rK},
   psiK = Table[Sin[z]^(-1/2 + I KK/(6 H)) E^(I kq x1 + I qq x5) uu[n][t], {n, 0, 15}];
   rK = Expand[elOp[psiK, Meff] Sin[z]^(1/2 - I KK/(6 H)) E^(-I kq x1 - I qq x5)];
   addCheck["P_modes_kqNonzeroNotSeparable", ! FreeQ[Together[toRing /@ rK], sg] && FreeQ[Together[toRing /@ (rK /. {kq -> 0, qq -> 0})], sg | cc]]];
  keff = kq Sin[z]^(-1/6) E^(-a4[t]); qeff = qq Sin[z]^(-1/6) E^(a4[t]);
  hl = -I Meff G[4] - G[4].(KK G[0] + keff G[1] + qeff G[5]);
  E2l = Meff^2 + KK^2 + keff^2 - qeff^2;
  addCheck["P_modes_localWKBDispersion", zeroMatQ[hl.hl - E2l id16]];
  addCheck["P_modes_localHermitianIffQZero", zeroMatQ[herm[hl /. qq -> 0] - (hl /. qq -> 0)] && ! zeroMatQ[herm[hl] - hl] &&
    zeroMatQ[(hl - herm[hl]) + 2 qeff G[4].G[5]] && zeroMatQ[herm[G[4].G[5]] + G[4].G[5]]];
  addMeas["modes_hLocalMinusAdjoint", "h_loc - h_loc^dagger = -2 k5eff gamma^4 gamma^5 (gamma^4 gamma^5 anti-Hermitian), so the anti-Hermitian part (h_loc - h_loc^dagger)/2 is -k5eff gamma^4 gamma^5, k5eff = k5 s^(-1/6) e^(a4) = k5 e^(-H zeta + a4)"];
  (* onset for k = 0: q e^{-H zeta + a4} = sqrt(Meff^2 + K^2) *)
  onset = Log[Sqrt[Meff^2 + KK^2]/qq] + H zeta;
  addCheck["P_modes_instabilityOnset", Simplify[(Meff^2 + KK^2 - qq^2 E^(-2 H zeta + 2 a4v)) /. a4v -> onset, Meff > 0 && KK > 0 && qq > 0 && Element[{H, zeta}, Reals]] === 0];
  $comp["modes"] = <|
    "homogeneous" -> "\\Psi=e^{-3H\\zeta}e^{iK\\zeta}u(x_4):\\ \\gamma^4\\dot u=(M_{\\mathrm{eff}}-iK\\gamma^0)u,\\ i\\dot u=hu,\\ h=-iM_{\\mathrm{eff}}\\gamma^4-K\\gamma^4\\gamma^0,\\ h=h^\\dagger,\\ h^2=(M_{\\mathrm{eff}}^2+K^2)\\cdot1,\\ E=\\pm\\sqrt{M_{\\mathrm{eff}}^2+K^2}\\ (8\\text{ each})",
    "notSeparable" -> "for k_1\\ne0 (momentum along x_1) or k_5\\ne0 (along x_5) the coefficients k_1 e^{-H\\zeta}e^{-a_4(t)}, k_5 e^{-H\\zeta}e^{a_4(t)} multiply \\gamma^1, \\gamma^5, which anticommute with \\gamma^0 and \\gamma^4: the reduced equation keeps an explicit \\zeta dependence and no product ansatz separates it",
    "localDispersion" -> "E^2=M_{\\mathrm{eff}}^2+K^2+\\bigl(k_1\\,e^{-H\\zeta-a_4}\\bigr)^2-\\bigl(k_5\\,e^{-H\\zeta+a_4}\\bigr)^2\\ \\text{(local, frozen coefficients, WKB)}",
    "instability" -> "k_1=0,\\ k_5\\ne0: E^2<0 once a_4(t)>H\\zeta+\\ln\\bigl(\\sqrt{M_{\\mathrm{eff}}^2+K^2}/|k_5|\\bigr); an unboundedly growing a_4 (for example a_4=t: 3-space inflation, extra-time deflation) reaches it, a bounded one need not; for k_5\\ne0 the local h is not Hermitian: h_{\\mathrm{loc}}-h_{\\mathrm{loc}}^\\dagger=-2k_{5,\\mathrm{eff}}\\gamma^4\\gamma^5, so its anti-Hermitian part is -k_{5,\\mathrm{eff}}\\gamma^4\\gamma^5, k_{5,\\mathrm{eff}}=k_5e^{-H\\zeta+a_4}"|>;];

(* ---------------- P_einstein ---------------- *)
checkEinstein[nbd_] := Module[{Ric, R, Gmix, Gcov, exG, st584, st583, R4, rhoReq, pReq, ec, a1v, a2v, wr, lin},
  Ric = Table[Sum[d1[r, GamF[[r, m, n]]] - d1[n, GamF[[r, m, r]]] + Sum[GamF[[r, r, l]] GamF[[l, m, n]] - GamF[[r, n, l]] GamF[[l, m, r]], {l, 8}], {r, 8}], {m, 8}, {n, 8}];
  R = Sum[giF[[m, m]] Ric[[m, m]], {m, 8}];
  addCheck["P_einstein_ricciScalar", zeroQ[R - 6 H^2 (a4'[t]^2 - 7)]];
  Gmix = giF.Ric - (R/2) id8;
  exG = DiagonalMatrix[Join[{-3 H^2 (a4'[t]^2 - 5)}, ConstantArray[H^2 (15 - 3 a4'[t]^2 + a4''[t]), 3], {3 H^2 (7 + a4'[t]^2)},
      ConstantArray[H^2 (15 - 3 a4'[t]^2 - a4''[t]), 3]]];
  addCheck["P_einstein_GmixedClosedForms", zeroMatQ[Gmix - exG]];
  addCheck["P_einstein_offDiagonalZero", zeroMatQ[Gmix - DiagonalMatrix[Diagonal[Gmix]]] && zeroMatQ[Ric - DiagonalMatrix[Diagonal[Ric]]]];
  addCheck["P_einstein_pointCheck", And @@ Table[ptZeroMatQ[Gmix - exG, k] && ptZeroQ[R - 6 H^2 (a4'[t]^2 - 7), k], {k, 2}]];
  Gcov = Ric - (1/2) gF R;
  st584 = nbOutput[nbd, 584, 1]; st583 = nbOutput[nbd, 583, 1];
  addCheck["P_einstein_notebookCell584", st584 =!= $Failed && Dimensions[st584] === {8, 8} && AllTrue[Flatten[st584 - (Gcov /. {z -> 6 H x0, t -> H x4})], zeroXQ]];
  addCheck["P_einstein_notebookCell583", st583 =!= $Failed && zeroXQ[st583 - (R /. {z -> 6 H x0, t -> H x4})]];
  R4 = giF[[5, 5]] Ric[[5, 5]];
  addCheck["P_einstein_R44", zeroQ[Ric[[5, 5]] + 6 H^2 a4'[t]^2]];
  rhoReq = -3 H^2 (7 + a4'[t]^2)/kap;
  pReq = Diagonal[exG]/kap;
  addCheck["P_einstein_requiredSource", zeroQ[rhoReq + exG[[5, 5]]/kap] && zeroQ[rhoReq - (-3 H^2 (7 + a4'[t]^2)/kap)]];
  addCheck["P_einstein_rhoRequiredNegative", Simplify[rhoReq < 0, kap > 0 && H > 0 && Element[a4'[t], Reals]]];
  (* energy conditions (orthonormal frame, observer u = e_(4)) *)
  ec = <|
    "WEC_rho" -> <|"expr" -> texR[toRing[rhoReq]], "status" -> "violated for every a4 (rho_req < 0)"|>,
    "NEC_e4_plus_e0" -> <|"expr" -> texR[toRing[rhoReq + pReq[[1]]]], "status" -> "violated for every a4"|>,
    "NEC_e4_plus_ei_(i=1,2,3)" -> <|"expr" -> texR[toRing[rhoReq + pReq[[2]]]], "status" -> "violated unless a4'' >= 6(1+a4'^2)"|>,
    "NEC_ej_plus_e0_(j=5,6,7)" -> <|"expr" -> texR[toRing[pReq[[1]] - pReq[[6]]]], "status" -> "holds iff a4'' >= 0"|>,
    "NEC_ej_plus_ei" -> <|"expr" -> texR[toRing[pReq[[2]] - pReq[[6]]]], "status" -> "holds iff a4'' >= 0"|>,
    "SEC_timelikeConvergence_R44" -> <|"expr" -> texR[toRing[Ric[[5, 5]]]], "status" -> "R_44 = -6H^2 a4'^2 <= 0: violated whenever a4' != 0"|>,
    "DEC" -> <|"expr" -> "requires \\rho\\ge0", "status" -> "violated"|>|>;
  addCheck["P_einstein_energyConditionForms", zeroQ[rhoReq + pReq[[1]] + 6 H^2 (1 + a4'[t]^2)/kap] && zeroQ[rhoReq + pReq[[2]] - H^2 (a4''[t] - 6 - 6 a4'[t]^2)/kap] &&
    zeroQ[pReq[[1]] - pReq[[6]] - H^2 a4''[t]/kap] && zeroQ[pReq[[2]] - pReq[[6]] - 2 H^2 a4''[t]/kap]];
  (* whether dirac16complex can supply this source is decided in checkSource[] (checks P_source_...), which builds T^mu_nu *)
  $exG = exG;
  $comp["einstein"] = <|
    "ricciScalar" -> "R=6H^2(a_4'^2-7)",
    "GmixedDiagonal" -> Table[<|"mu" -> mu - 1, "value" -> exprRec[exG[[mu, mu]]],
        "texContract" -> Which[mu == 1, "-3H^2(a_4'^2-5)", mu <= 4, "H^2(15-3a_4'^2+a_4'')", mu == 5, "3H^2(7+a_4'^2)", True, "H^2(15-3a_4'^2-a_4'')"]|>, {mu, 8}],
    "offDiagonal" -> "all G^\\mu{}_\\nu with \\mu\\ne\\nu vanish",
    "notebookCell584" -> "the notebook's covariant EinsteinG (cell 584) equals R_{\\mu\\nu}-\\tfrac12g_{\\mu\\nu}R computed here, entry by entry",
    "requiredSource" -> <|"equation" -> "G^\\mu{}_\\nu=\\kappa T^\\mu{}_\\nu,\\ \\rho=-T^4{}_4,\\ p_{(i)}=T^i{}_i",
      "rho" -> "\\rho_{\\mathrm{req}}=-3H^2(7+a_4'^2)/\\kappa<0",
      "p0" -> "p_{0}=-3H^2(a_4'^2-5)/\\kappa", "p123" -> "p_{1,2,3}=H^2(15-3a_4'^2+a_4'')/\\kappa", "p567" -> "p_{5,6,7}=H^2(15-3a_4'^2-a_4'')/\\kappa"|>,
    "R44" -> "R_{44}=-6H^2a_4'^2",
    "energyConditions" -> ec,
    "sourceAnalysis" -> "see the component group source (checks P_source_*)"|>;];

(* ---------------- P_source: can a dirac16complex state supply G^mu_nu = kappa T^mu_nu ? ---------------- *)
(* the 15 off-diagonal bilinears Psibar X Psi of the x0-independent state (X = gamma product, Psibar = Psi^dagger C) *)
sourceBilinears = Join[Table[{"V" <> ToString[a], {0, a, 4}, G[0].G[a].G[4]}, {a, {1, 2, 3, 5, 6, 7}}],
   Flatten[Table[{"W" <> ToString[i] <> ToString[j], {i, 4, j}, G[i].G[4].G[j]}, {i, 1, 3}, {j, 5, 7}], 1]];
(* generators of the diagonal Spin(3) that rotates (x1,x2,x3) and (x5,x6,x7) together *)
diagSpin3 = {Sab[2, 3] - Sab[6, 7], Sab[3, 1] - Sab[7, 5], Sab[1, 2] - Sab[5, 6]};
(* exact examples, H = 1: Psi = e^{i omega x4} u0, u0 = sqrt(S / v^dagger C v) v *)
sourceExamples = {
   <|"label" -> "A", "m" -> 5, "lam" -> 0, "kappa" -> 1, "c" -> Sqrt[5], "S" -> -36/5, "Meff" -> 5, "omega" -> 4,
     "v" -> {3, -I, 0, 0, 3, I, 0, 0, 1, -3 I, 0, 0, 1, 3 I, 0, 0}|>,
   <|"label" -> "B", "m" -> -15, "lam" -> 25/6, "kappa" -> 1, "c" -> 1, "S" -> 12/5, "Meff" -> -5, "omega" -> 4,
     "v" -> {1, 3 I, 0, 0, 1, -3 I, 0, 0, -3, -I, 0, 0, -3, I, 0, 0}|>};
expectedOffProduct[{mu_, nu_}] := Which[
   {mu, nu} === {0, 4}, {},
   SubsetQ[{1, 2, 3}, {mu, nu}] || SubsetQ[{5, 6, 7}, {mu, nu}], {},
   mu === 0 || mu === 4 || nu === 4, {Sort[{0, If[mu === 0 || mu === 4, nu, mu], 4}]},
   True, {{mu, 4, nu}}];
checkSource[] := Module[{eZU, eH, SH, diagH, formQ, wr, uv, ubv, SX, onX, eX, TlowX, TmixX, offX, okOff, T44, Tt, sol, solOK,
    condOK, meffS, exRes, okEx, constr, nrm},
  (* (1) every state Psi(x0,x4): T^i_i = T^j_j = L_s off shell, for any U; but G^i_i - G^j_j = 2 H^2 a4'' *)
  eZU = emtLower[$emt["psiZ"], $emt["psibZ"], mm, Us];
  addCheck["P_source_transversePressuresEqualForEveryX0X4State", AllTrue[{2, 3, 4, 6, 7, 8}, zeroQ[giF[[#, #]] eZU["T"][[#, #]] - eZU["Ls"]] &]];
  addCheck["P_source_einsteinTransverseDifferenceIs2H2a4pp", zeroQ[$exG[[2, 2]] - $exG[[6, 6]] - 2 H^2 a4''[t]] && ! zeroQ[$exG[[2, 2]] - $exG[[6, 6]]]];
  (* (2) the zeta plane wave with REAL K: every diagonal T^mu_mu is c1(t)/sin z + c2(t)/sin^2 z (the off-diagonal mixed
     components are not, e.g. T^0_4); with the Wronskian of 1, 1/sin z, 1/sin^2 z this excludes it for every a4 *)
  eH = $emt["eH"]; SH = $emt["SH"];
  diagH = Table[giF[[mu, mu]] eH["T"][[mu, mu]] /. Us -> (lam/2) SH^2, {mu, 8}];
  formQ[e_] := zeroQ[D[D[Sin[z]^2 e, z]/Cos[z], z]];
  wr = Simplify[Det[{{1, 1/Sin[z], 1/Sin[z]^2}, D[{1, 1/Sin[z], 1/Sin[z]^2}, z], D[{1, 1/Sin[z], 1/Sin[z]^2}, {z, 2}]}]];
  addMeas["condensateWronskian_1_invS_invS2", toStr[wr]];
  addCheck["P_source_realKDiagonalIsC1OverSPlusC2OverS2", AllTrue[diagH, formQ] && ! formQ[giF[[1, 1]] eH["T"][[1, 5]]]];
  addCheck["P_source_realKPlaneWaveCannotSource", AllTrue[diagH, formQ] && ! zeroQ[wr] && ! zeroQ[$exG[[5, 5]]] &&
    FreeQ[toRing[$exG[[5, 5]]], sg | cc] && zeroQ[$exG[[5, 5]] - 3 H^2 (7 + a4'[t]^2)]];
  (* (3) the x0-independent state Psi = u(x4) (K = -3iH in s^{-1/2+iK/(6H)} u): on shell H du/dt = -gamma^4 (Meff - 3H gamma^0) u *)
  uv = Table[uu[n][t], {n, 0, 15}]; ubv = Table[ub[n][t], {n, 0, 15}];
  SX = ubv.C16.uv;
  onX = Join[
    Table[Derivative[1][uu[n]][t] -> (-(1/H) G[4].(Meff uv - 3 H G[0].uv))[[n + 1]], {n, 0, 15}],
    Table[Derivative[1][ub[n]][t] -> (-(1/H) G[4].(Meff ubv - 3 H G[0].ubv))[[n + 1]], {n, 0, 15}]];
  (* S is x0- and x4-independent on shell, so M_eff = m + lambda S is a constant and the solution is exact for every lambda *)
  addCheck["P_source_x0IndependentStateSolvesDiracExactly", zeroMatQ[elOp[uv, Meff] /. onX] && zeroQ[D[SX, t] /. onX] && FreeQ[toRing[SX], sg | cc]];
  eX = emtLower[uv, ubv, mm, Us];
  TlowX = eX["T"] /. onX;
  TmixX = Table[giF[[mu, mu]] TlowX[[mu, nu]], {mu, 8}, {nu, 8}];
  (* on shell (Meff = m + U'(S)): T^4_4 = -(m S + U), T^mu_mu = S U' - U for the seven mu != 4 *)
  addCheck["P_source_x0IndependentDiagonalOnShell", zeroQ[TmixX[[5, 5]] + mm SX + Us] &&
    AllTrue[{1, 2, 3, 4, 6, 7, 8}, zeroQ[TmixX[[#, #]] - ((Meff - mm) SX - Us)] &]];
  offX = Table[Module[{Q = Table[D[TlowX[[p[[1]], p[[2]]]], ub[a - 1][t], uu[b - 1][t]], {a, 16}, {b, 16}], dec},
      dec = cliffDecompose[C16.Q];
      <|"pair" -> p - 1, "bilinear" -> zeroQ[TlowX[[p[[1]], p[[2]]]] - ubv.Q.uv], "products" -> dec[[All, 1]], "dec" -> dec|>],
     {p, Select[Tuples[Range[8], 2], #[[1]] < #[[2]] &]}];
  okOff = AllTrue[offX, #["bilinear"] && #["products"] === expectedOffProduct[#["pair"]] &] &&
    Count[offX, r_ /; r["products"] =!= {}] === 21;
  addCheck["P_source_x0IndependentOffDiagonalAre15Bilinears", okOff];
  (* with the 15 bilinears zero: G^mu_nu = kappa T^mu_nu <=> a4'' = 0, m S = -36 H^2/kappa, lambda S^2 = 2 H^2 (15 - 3 a4'^2)/kappa *)
  T44 = -(mm SS + (lam/2) SS^2); Tt = (lam/2) SS^2;
  sol = Solve[{$exG[[5, 5]] == kap T44, $exG[[1, 1]] == kap Tt}, {mm, lam}];
  solOK = Length[sol] === 1 && zeroQ[(mm /. sol[[1]]) + 36 H^2/(kap SS)] && zeroQ[(lam /. sol[[1]]) - 2 H^2 (15 - 3 a4'[t]^2)/(kap SS^2)];
  condOK = solOK && AllTrue[Range[8], zeroQ[($exG[[#, #]] - kap If[# == 5, T44, Tt]) /. sol[[1]] /. a4''[t] -> 0] &] &&
    ! zeroQ[($exG[[2, 2]] - kap Tt) /. sol[[1]]];
  meffS = Together[(mm + lam SS) /. sol[[1]]];
  addCheck["P_source_x0IndependentSourceConditions", condOK && zeroQ[meffS + 6 H^2 (1 + a4'[t]^2)/(kap SS)]];
  addMeas["source_x0Independent_Meff", toStr[Factor[meffS]]];
  (* existence: the eigenspace of A = -gamma^4 (Meff - 3H gamma^0) for i omega, omega = sqrt(Meff^2 - 9H^2), meets the
     diagonal-Spin(3) singlets in a 2-dimensional space on which only W15 = W26 = W37 survive; explicit u0 (H = 1) *)
  exRes = Table[Module[{Am, w = ex["omega"], ns, Qm, forms, v = ex["v"], u0, Sv, psiE, psibE, S0, eE, TmE, Gl, res, resBad, dirac, rec},
     Am = -G[4].(ex["Meff"] id16 - 3 G[0]);
     ns = NullSpace[Join[diagSpin3[[1]], diagSpin3[[2]], diagSpin3[[3]], Am - I w id16]];
     Qm = Transpose[ns];
     forms = Table[{b[[1]], Simplify[ConjugateTranspose[Qm].C16.b[[3]].Qm]}, {b, sourceBilinears}];
     Sv = Simplify[Conjugate[v].C16.v];
     u0 = Sqrt[ex["S"]/Sv] v;
     psiE = E^(I w t/H) u0; psibE = E^(-I w t/H) Conjugate[u0];
     S0 = Simplify[Expand[psibE.C16.psiE]];
     dirac = zeroMatQ[Expand[(elOp[psiE, ex["m"] + ex["lam"] S0] /. H -> 1) E^(-I w t)]];
     eE = emtLower[psiE, psibE, ex["m"], (ex["lam"]/2) S0^2];
     TmE = Table[giF[[mu, mu]] eE["T"][[mu, nu]], {mu, 8}, {nu, 8}];
     Gl = $exG;
     res = Expand[((Gl - ex["kappa"] TmE) /. {Derivative[2][a4][t] -> 0} /. {Derivative[1][a4][t] -> ex["c"]}) /. H -> 1];
     rec = <|"label" -> ex["label"], "H" -> 1, "kappa" -> ex["kappa"], "m" -> ex["m"], "lambda" -> ex["lam"], "a4" -> toStr[ex["c"] t],
       "Meff" -> ex["Meff"], "omega" -> w, "S" -> S0, "u0" -> toStr[u0], "v" -> toStr[v], "u0NormFactorSquared" -> ex["S"]/Sv,
       "rho" -> ex["m"] S0 + (ex["lam"]/2) S0^2, "pTransverse" -> (ex["lam"]/2) S0^2,
       "w" -> Together[((ex["lam"]/2) S0^2)/(ex["m"] S0 + (ex["lam"]/2) S0^2)]|>;
     (* negative control: the same state does not source the field for the slope c + 1 *)
     resBad = Expand[((Gl - ex["kappa"] TmE) /. {Derivative[2][a4][t] -> 0} /. {Derivative[1][a4][t] -> ex["c"] + 1}) /. H -> 1];
     <|"rec" -> rec,
       "construction" -> (w^2 === ex["Meff"]^2 - 9 && Length[ns] === 2 &&
          Count[forms, f_ /; f[[2]] =!= ConstantArray[0, {2, 2}]] === 3 &&
          (Select[forms, #[[2]] =!= ConstantArray[0, {2, 2}] &][[All, 1]] === {"W15", "W26", "W37"}) &&
          Equal @@ Select[forms, #[[2]] =!= ConstantArray[0, {2, 2}] &][[All, 2]] && MatrixRank[Append[ns, v]] === 2),
       "example" -> (Am.v === I w v && AllTrue[sourceBilinears, Simplify[Conjugate[v].C16.#[[3]].v] === 0 &] &&
          S0 === ex["S"] && ex["m"] + ex["lam"] S0 === ex["Meff"] && ex["m"] ex["S"] === -36/ex["kappa"] &&
          Simplify[ex["lam"] ex["S"]^2 - 2 (15 - 3 ex["c"]^2)/ex["kappa"]] === 0 && dirac && zeroMatQ[res] && ! zeroMatQ[resBad] &&
          rec["rho"] === -3 (7 + ex["c"]^2)/ex["kappa"] && rec["pTransverse"] === (15 - 3 ex["c"]^2)/ex["kappa"])|>], {ex, sourceExamples}];
  addCheck["P_source_x0IndependentConstruction", AllTrue[exRes, #["construction"] &]];
  addCheck["P_source_x0IndependentExactExamples", AllTrue[exRes, #["example"] &]];
  addMeas["source_x0Independent_examples", ToString[#["rec"] & /@ exRes, InputForm]];
  (* normalizability in the canonical measure cos z dz: |u|^2 cos z is integrable, the real-K |Psi|^2 cos z ~ cot z is not *)
  nrm = Integrate[Cos[z], {z, 0, Pi/2}] === 1 &&
    Limit[Integrate[Cot[z], {z, ee, Pi/2}, Assumptions -> 0 < ee < Pi/2], ee -> 0, Direction -> "FromAbove"] === Infinity;
  addCheck["P_source_x0IndependentNormalizableRealKNot", nrm];
  addMeas["contractNote_condensateSource", "CONTRACT section 9 states that a homogeneous condensate cannot source this field because Psibar Psi ~ 1/sin z; that holds for the real-K zeta plane waves only (P_source_realKPlaneWaveCannotSource). The x0-independent state Psi = u(x4) (K = -3iH) has a constant Psibar Psi and is an exact source for a4'' = 0 (m S = -36 H^2/kappa, lambda S^2 = 2 H^2 (15 - 3 a4'^2)/kappa, 15 off-diagonal bilinears zero; P_source_x0IndependentExactExamples), with rho = -3 H^2 (7 + a4'^2)/kappa < 0; for a4'' != 0 no state of (x0, x4) is a source (P_source_transversePressuresEqualForEveryX0X4State)."];
  $comp["source"] = <|
    "question" -> "can a dirac16complex state (c-number/mean-field reading of the bilinears) satisfy G^\\mu{}_\\nu=\\kappa T^\\mu{}_\\nu in this field?",
    "everyX0X4State" -> "for every \\Psi(x_0,x_4), off shell and for every U: T^i{}_i=T^j{}_j=\\mathcal L_s (i=1,2,3,\\ j=5,6,7), while G^i{}_i-G^j{}_j=2H^2a_4''; hence a4''\\ne0 excludes every such state",
    "realK" -> "\\Psi=s^{-1/2+iK/(6H)}u(x_4),\\ K\\in\\mathbb R: every diagonal T^\\mu{}_\\mu=c_1(t)/\\sin z+c_2(t)/\\sin^2z (c_2\\propto\\lambda), while G^4{}_4=3H^2(7+a_4'^2) is z-independent and nonzero; W(1,1/\\sin z,1/\\sin^2z)\\ne0 excludes it for every a_4",
    "x0Independent" -> <|
      "ansatz" -> "\\Psi=u(x_4)\\ (K=-3iH),\\ \\gamma^4\\partial_4u=(M_{\\mathrm{eff}}-3H\\gamma^0)u,\\ S=u^\\dagger Cu\\ \\text{constant},\\ M_{\\mathrm{eff}}=m+\\lambda S",
      "diagonal" -> "T^4{}_4=-(mS+U),\\ T^\\mu{}_\\mu=SU'-U\\ (\\mu\\ne4)",
      "offDiagonal" -> Table[<|"mu" -> r["pair"][[1]], "nu" -> r["pair"][[2]],
          "gammaProduct" -> r["dec"][[1, 1]], "tex" -> "\\gamma^{" <> StringRiffle[ToString /@ r["dec"][[1, 1]], "}\\gamma^{"] <> "}",
          "coefficient" -> exprRec[r["dec"][[1, 2]]]|>, {r, Select[offX, #["products"] =!= {} &]}],
      "conditions" -> "a_4''=0,\\ mS=-36H^2/\\kappa,\\ \\lambda S^2=2H^2(15-3a_4'^2)/\\kappa,\\ M_{\\mathrm{eff}}=-6H^2(1+a_4'^2)/(\\kappa S),\\ \\text{15 bilinears zero}",
      "examples" -> (#["rec"] & /@ exRes)|>|>;];

(* ---------------- P_quant ---------------- *)
checkQuant[] := Module[{psi, psib, Lag, Lag2, PiM, Hd, HdClosed, dHd, evo, psiX, herm, A, B0, w, adjOK, badA, g8op, L8a, L8b, Dpsi, Dpsib, S0, ev},
  herm[m_] := Transpose[m] /. Complex[a_, b_] :> Complex[a, -b];
  addCheck["P_quant_Bproperties", herm[Bm] === Bm && Bm.Bm === id16 && Sort[Eigenvalues[Bm]] === Join[ConstantArray[-1, 8], ConstantArray[1, 8]] &&
    C16.Bm === Bm.C16 && Bm.C16 === -I G[4]];
  addCheck["P_quant_anticommutatorMatrix", I Inverse[C16.gUF[[5]]] === Bm && gUF[[5]] === G[4] && giF[[5, 5]] === -1 &&
    zeroMatQ[I G[4].C16/(giF[[5, 5]] sqrtgF) - Bm/Cos[z]]];
  psi = Table[Ps[n] @@ Yv, {n, 0, 15}]; psib = Table[Pb[n] @@ Yv, {n, 0, 15}];
  S0 = psib.C16.psi;
  Dpsi = Table[d1[mu, psi] + OmF[[mu]].psi, {mu, 8}];
  Dpsib = Table[d1[mu, psib.C16] - psib.C16.OmF[[mu]], {mu, 8}];
  Lag = sqrtgF ((1/2) Sum[psib.C16.gUF[[mu]].Dpsi[[mu]] - Dpsib[[mu]].gUF[[mu]].psi, {mu, 8}] - mm S0 - (lam/2) S0^2);
  Lag2 = Lag + (1/2) d1[5, sqrtgF psib.C16.G[4].psi];
  PiM = Table[D[Lag2, D[Ps[b] @@ Yv, t]]/H, {b, 0, 15}];
  addCheck["P_quant_momentum", zeroMatQ[PiM - sqrtgF psib.C16.G[4]] && AllTrue[Range[0, 15], zeroQ[D[Lag2, D[Pb[#] @@ Yv, t]]] &]];
  Hd = PiM.d1[5, psi] - Lag2;
  addCheck["P_quant_hamiltonianHasNoTimeDerivatives", AllTrue[Range[0, 15], zeroQ[D[Hd, D[Ps[#] @@ Yv, t]]] && zeroQ[D[Hd, D[Pb[#] @@ Yv, t]]] &]];
  HdClosed = sqrtgF (-(1/2) Sum[If[mu == 5, 0, (1/hhF[[mu]]) (psib.C16.G[mu - 1].d1[mu, psi] - d1[mu, psib].C16.G[mu - 1].psi)], {mu, 8}] + mm S0 + (lam/2) S0^2);
  addCheck["P_quant_hamiltonianDensityClosedForm", zeroQ[Hd - HdClosed]];
  (* Heisenberg / Hamilton: i d_4 Psi = B (1/sqrt g) dH/dPsi^dagger reproduces the Euler-Lagrange evolution *)
  dHd = Table[D[Hd, Pb[a] @@ Yv] - Sum[D[D[Hd, D[Pb[a] @@ Yv, Yv[[k]]]], Yv[[k]]], {k, 8}], {a, 0, 15}];
  evo = -G[4].((mm + lam S0) psi - Sum[If[mu == 5, 0, gUF[[mu]].Dpsi[[mu]]], {mu, 8}]);
  addCheck["P_quant_heisenbergReproducesEL", zeroMatQ[I evo - Bm.dHd/sqrtgF]];
  (* good sector: h = sum_mu A_mu d_mu + B0 Hermitian w.r.t. the weight sqrt g = cos z *)
  A = Table[If[mu == 5, 0 id16, I (1/hhF[[mu]]) G[4].G[mu - 1]], {mu, 8}];
  B0 = -I mm G[4] + 3 I H G[4].G[0];
  adjOK = AllTrue[{1, 2, 3, 4}, zeroMatQ[herm[A[[#]]] + A[[#]]] &] &&
    zeroMatQ[herm[B0] - Sum[d1[mu, sqrtgF herm[A[[mu]]]]/sqrtgF, {mu, {1, 2, 3, 4}}] - B0];
  addCheck["P_quant_goodSectorHermitian", adjOK];
  badA = AllTrue[{6, 7, 8}, ! zeroMatQ[herm[A[[#]]] + A[[#]]] &];
  addCheck["P_quant_extraTimeMomentaNonHermitian", badA];
  addCheck["P_quant_singleParticleOperatorMatchesEvolution", zeroMatQ[Sum[A[[mu]].d1[mu, psi], {mu, 8}] + B0.psi - I (evo /. lam -> 0)]];
  (* gamma^8 map: E_{m,lambda}[gamma^8 Psi] = -gamma^8 E_{-m,-lambda}[Psi]; L_{m,lambda}[gamma^8 Psi] = -L_{-m,-lambda}[Psi] *)
  g8op = elOp[g8.psi, mm + lam ((psib.g8).C16.(g8.psi))] + g8.elOp[psi, -mm - lam S0];
  addCheck["P_quant_gamma8MapsMtoMinusM", zeroMatQ[g8op] && zeroQ[(psib.g8).C16.(g8.psi) - S0]];
  L8a = Lag /. Join[Thread[(Ps /@ Range[0, 15]) -> (Function[Evaluate[Yv], #] & /@ (g8.psi))], Thread[(Pb /@ Range[0, 15]) -> (Function[Evaluate[Yv], #] & /@ (psib.g8))]];
  L8b = -(Lag /. {mm -> -mm, lam -> -lam});
  addCheck["P_quant_gamma8LagrangianSign", zeroQ[L8a - L8b] && ! zeroQ[L8a + (Lag /. mm -> -mm)]];
  addMeas["contractNote_gamma8Map", "Psi -> gamma^8 Psi maps L_{m,U} to -L_{-m,-U} (and solutions of (m,lambda) to solutions of (-m,-lambda)); CONTRACT section 5 states L_m -> -L_{-m}, which is exact only for U = 0."];
  $comp["quantization"] = <|
    "momentum" -> "\\Pi=\\partial\\mathcal L/\\partial(\\partial_4\\Psi)=\\sqrt{|g|}\\,\\Psi^\\dagger C\\gamma^4=\\cos z\\,\\Psi^\\dagger C\\gamma^4\\ (\\text{after }\\mathcal L\\to\\mathcal L+\\tfrac12\\partial_4(\\sqrt{|g|}\\bar\\Psi\\gamma^4\\Psi))",
    "anticommutator" -> "\\{\\Psi_a(x),\\Psi_b^\\dagger(y)\\}_{x^4=y^4}=i[(C\\gamma^4)^{-1}]_{ab}\\frac{\\delta^7(x-y)}{\\cos z}=B_{ab}\\frac{\\delta^7(x-y)}{\\cos z},\\ B=-iC\\gamma^4",
    "B" -> "B=B^\\dagger,\\ B^2=1,\\ \\mathrm{spec}\\,B=\\{+1^{(8)},-1^{(8)}\\},\\ [C,B]=0,\\ BC=-i\\gamma^4",
    "hamiltonianDensity" -> "\\mathcal H=\\cos z\\Bigl[-\\tfrac12\\sum_{\\mu\\ne4}h_\\mu^{-1}\\bigl(\\bar\\Psi\\gamma^\\mu\\partial_\\mu\\Psi-\\partial_\\mu\\bar\\Psi\\gamma^\\mu\\Psi\\bigr)+m\\bar\\Psi\\Psi+\\tfrac\\lambda2(\\bar\\Psi\\Psi)^2\\Bigr],\\ h=(\\cot z,s^{1/6}e^{a_4}(\\times3),1,s^{1/6}e^{-a_4}(\\times3))",
    "heisenberg" -> "i\\partial_4\\Psi=B\\,\\frac{1}{\\cos z}\\frac{\\delta H}{\\delta\\Psi^\\dagger}\\ \\text{reproduces}\\ \\partial_4\\Psi=-\\gamma^4\\bigl[(m+\\lambda S)\\Psi-\\sum_{\\mu\\ne4}\\gamma^\\mu D_\\mu\\Psi\\bigr]",
    "singleParticle" -> "k_5=0\\ (\\text{no }x_{5,6,7}\\text{ dependence}):\\ i\\partial_4\\Psi=h\\Psi,\\ h=-im\\gamma^4+3iH\\gamma^4\\gamma^0+i\\tan z\\,\\gamma^4\\gamma^0\\partial_0+i s^{-1/6}e^{-a_4}\\gamma^4\\gamma^i\\partial_i,\\ \\text{Hermitian w.r.t. }\\int\\cos z\\,\\Psi^\\dagger\\Phi\\,d^7x\\ (\\text{the }3H\\text{ term is exactly what the weight }\\cos z\\text{ requires});\\ \\text{the }x_{5,6,7}\\text{ terms }is^{-1/6}e^{a_4}\\gamma^4\\gamma^j\\partial_j\\text{ are anti-Hermitian}",
    "gamma8" -> "\\Psi\\to\\gamma^8\\Psi:\\ \\mathcal L_{m,\\lambda}\\to-\\mathcal L_{-m,-\\lambda},\\ \\text{solutions of }(m,\\lambda)\\to\\text{solutions of }(-m,-\\lambda)\\ (\\pm M\\text{ pair, structural only})"|>;];

(* ---------------- P_a4linear ---------------- *)
checkA4Linear[] := Module[{sub, R, Gd, rho, p, w, alt},
  sub[e_, a1_] := e /. {a4'[t] -> a1, a4''[t] -> 0};
  R = 6 H^2 (a4'[t]^2 - 7);
  Gd = {-3 H^2 (a4'[t]^2 - 5), H^2 (15 - 3 a4'[t]^2 + a4''[t]), H^2 (15 - 3 a4'[t]^2 + a4''[t]), H^2 (15 - 3 a4'[t]^2 + a4''[t]), 3 H^2 (7 + a4'[t]^2),
    H^2 (15 - 3 a4'[t]^2 - a4''[t]), H^2 (15 - 3 a4'[t]^2 - a4''[t]), H^2 (15 - 3 a4'[t]^2 - a4''[t])};
  rho = -Gd[[5]]/kap; p = Delete[Gd, 5]/kap;
  addCheck["P_a4linear_values", sub[R, 1] === -36 H^2 && sub[Gd, 1] === {12 H^2, 12 H^2, 12 H^2, 12 H^2, 24 H^2, 12 H^2, 12 H^2, 12 H^2} &&
    sub[rho, 1] === -24 H^2/kap && Union[sub[p, 1]] === {12 H^2/kap} && Simplify[sub[p[[1]]/rho, 1]] === -1/2];
  (* a4'' = 0: all seven transverse pressures coincide, w = (a4'^2 - 5)/(7 + a4'^2) *)
  addCheck["P_a4linear_isotropicWhenA4ppZero", Length[Union[Together /@ (p /. a4''[t] -> 0)]] === 1 &&
    Together[(p[[1]]/rho /. a4''[t] -> 0) - (a4'[t]^2 - 5)/(7 + a4'[t]^2)] === 0];
  alt = Table[<|"a4prime" -> exprRecR[a1], "R" -> exprRecR[Factor[sub[R, a1]]],
      "Gmixed" -> (exprRecR /@ (Factor /@ sub[Gd, a1])),
      "rhoReq" -> exprRecR[Factor[sub[rho, a1]]], "pReqIsotropic" -> exprRecR[Factor[sub[p[[1]], a1]]],
      "w" -> exprRecR[Factor[sub[p[[1]]/rho, a1]]]|>, {a1, {1, 2 (M - 1)/3, 2 (M + 1)/3}}];
  addCheck["P_a4linear_cell150AlternativesRhoNegative", AllTrue[{2 (M - 1)/3, 2 (M + 1)/3}, Simplify[sub[rho, #] < 0, kap > 0 && H > 0 && Element[M, Reals]] &]];
  $comp["a4linear"] = <|"a4" -> "a_4=t\\ (a_4'=1,\\ a_4''=0)",
     "values" -> <|"R" -> "-36H^2", "Gmixed" -> "\\mathrm{diag}(12,12,12,12,24,12,12,12)\\,H^2", "rhoReq" -> "-24H^2/\\kappa", "pReq" -> "12H^2/\\kappa\\ (\\text{all seven transverse directions})", "w" -> "-1/2",
       "notebookQ" -> "q=Q_1\\sinh t\\,e^{-t}=\\tfrac12Q_1(1-e^{-2t})"|>,
     "cell150Alternatives" -> alt,
     "linearGeneral" -> "a_4''=0:\\ p_{(i)}=H^2(15-3a_4'^2)/\\kappa\\ \\text{for all seven transverse }i,\\ w=\\frac{a_4'^2-5}{a_4'^2+7}",
     "note" -> "cell 150 lists a4' = 2(M-1)/3 and 2(M+1)/3 with a4'' = 0 without derivation; rho_req < 0 for every real M"|>;];

(* ================================================================== *)
(* 7. driver                                                           *)
(* ================================================================== *)

D16PRun[repoRoot_String] := Module[{nbFile, fixFile, nbd, res, t0 = AbsoluteTime[], step},
  $checks = <||>; $meas = <||>; $comp = <||>;
  nbFile = FileNameJoin[{repoRoot, "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb"}];
  fixFile = FileNameJoin[{repoRoot, "artifacts", "dirac16complex", "arbitrary-field", "algebra-fixture.json"}];
  step[name_, body_] := (logT[name]; body);
  SetAttributes[step, HoldRest];
  res = Catch[
    step["zero-test sanity", checkZeroTests[]];
    step["fixture", checkFixture[fixFile]];
    addMeas["storedOutputsSource", "stored notebook outputs are parsed from the committed .nb (Output cells following input cells 501, 583, 584, 1060, 1079, 1089, 1096, 1111, 1137 in the survey-dump numbering of non-Output cells)"];
    addMeas["exactnessMethod", "ring Q(params)[s^(1/6), cos z, e^a4, a4', a4'', ...] modulo cos^2 z + s^2 - 1 (complete zero test), plus exact point checks at sin z = 3/5 and 5/13 with rational a4 jets (e^(1/6) transcendental, coefficients RootReduce'd)"];
    step["loading notebook (read only)", nbd = loadNotebookCells[nbFile]];
    addMeas["notebookNonOutputCellCount", nbd["count"]];
    addMeas["notebookCellNumbering", "cell N = the N-th cell (1-based, file order) of the styles " <> StringRiffle[nbStyles, ", "] <>
      "; Output, Print and Message cells are not counted and belong to the preceding counted cell (loadNotebookCells)"];
    addMeas["notebookCitedCellLabels", StringRiffle[Table[Module[{c = nbd["inputs"][n], lab},
         lab[x_] := Module[{r = Cases[List @@ x, (Rule | RuleDelayed)[CellLabel, v_] :> v]}, If[r === {}, "-", StringTrim[StringReplace[First[r], ":=" | "=" -> ""]]]];
         ToString[n] <> ": " <> lab[c] <> " -> " <> StringRiffle[lab /@ Select[nbd["outputs"][n], #[[2]] === "Output" &], ", "]],
       {n, {501, 583, 584, 1058, 1060, 1066, 1075, 1078, 1079, 1089, 1096, 1111, 1137}}], "; "]];
    (* evidence on the session of the stored chain 1058..1137 (document Section 11.3) *)
    addMeas["notebookSessionEvidence", Module[{ct = Cases[List @@ nbd["inputs"][1058], (Rule | RuleDelayed)[CellChangeTimes, v_] :> v]},
       "cell 1096 stored date strings: " <> StringRiffle[Union[Select[Cases[nbd["outputs"][1096], _String, Infinity], StringMatchQ[#, ___ ~~ "2026" ~~ ___] && StringLength[#] > 4 &]], ", "] <>
        "; cell 1058 last CellChangeTimes: " <> If[ct === {}, "-", DateString[FromAbsoluteTime[Last[Flatten[{First[ct]}]]], {"Year", "-", "Month", "-", "Day"}]] <>
        "; notebook FrontEndVersion: " <> ToString[nbd["frontEndVersion"]] <> "; verifier kernel: " <> $Version]];
    step["geometry", buildGeometry[]];
    step["P_metric", checkMetric[nbd]];
    step["P_zeta", checkZeta[]];
    step["P_christoffel", checkChristoffel[]];
    step["P_spinconn", checkSpinConnection[nbd]];
    step["P_Omega", checkOmega[]];
    step["P_gammaConst", checkGammaConst[]];
    step["P_EL", checkEL[]];
    step["P_blocks", checkBlocks[]];
    step["P_notebookCompare", checkNotebookCompare[nbd]];
    step["P_EMT", checkEMT[]];
    step["P_modes", checkModes[]];
    step["P_einstein", checkEinstein[nbd]];
    step["P_source", checkSource[]];
    step["P_quant", checkQuant[]];
    step["P_a4linear", checkA4Linear[]];
    "ok", d16pErr];
  If[res =!= "ok", Print["INTERNAL ERROR: ", res]; addCheck["P_internal_noException", False], addCheck["P_internal_noException", True]];
  logT["done in ", Round[AbsoluteTime[] - t0], " s"];
  <|"checks" -> $checks, "measurements" -> $meas, "components" -> $comp|>];

End[];
EndPackage[];
