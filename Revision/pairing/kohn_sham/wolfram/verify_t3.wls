#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_t3.wls

   Theorem T3 of Revision/SPEC.md section 9 (the Kohn-Sham level of the pairing of universes of masses
   {+m, -m}): the block map of the chirality Gamma, with the transformed boundary conditions, maps every
   self-consistent instantaneous Kohn-Sham state of dirac16complex with (m, lambda, tip angle theta) onto a
   self-consistent Kohn-Sham state with (-m, +lambda, tip angle Pi - theta), with equal levels, occupations,
   Kohn-Sham energies, grand potentials and energy-momentum profiles, and with S -> -S.

   The Kohn-Sham problem is the one recorded in Revision/kohn_sham/ks-theory.json (block equation, functional,
   densities, energy-momentum tensor, boundary conditions); this script re-derives every step of the proof by
   exact symbolic computation and reads ks-theory.json for the Kohn-Sham potentials (exchange.kohnShamPotentials:
   the coefficients of M_eff, v_v and e_int, with a consistency check, check T3_mean_field_map) and for the block
   basis V (to tie the 2 x 2 block map to the 16-component chirality Gamma of Revision/algebra/gammas.json).
   Written anew; no code shared with the sympy checker Revision/pairing/kohn_sham/python/check_t3.py or with the
   Kohn-Sham verifiers.

   Writes (deterministic, LF): Revision/pairing/kohn_sham/t3-theory.json and
   Revision/pairing/kohn_sham/reports/wolfram-t3.json.
   Usage: wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls      Exit 0 iff all checks pass.
   A missing or unreadable input (ks-theory.json, gammas.json, or Kohn-Sham potentials that are not exact numbers)
   stops the run before the first check with a line "ERROR  ..." and exit code 1 (nothing is written); an output
   file that cannot be written stops the run with "ERROR  cannot write ..." and exit code 1.

   Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially
   DEFLATING extra times; x8 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0] (brane y = 0, tip y = -L).
*)

$here = DirectoryName[$InputFileName];
$t3Dir = ExpandFileName[FileNameJoin[{$here, ".."}]]; (* NORMALISED: a ".." left in a path can push it past the Windows limit of 260 characters (MAX_PATH) *)
$revDir = ExpandFileName[FileNameJoin[{$t3Dir, "..", ".."}]];
t0 = AbsoluteTime[];
checks = {};
addCheck[name_String, ok_, detail_String] := (
  AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS  ", "FAIL  "], name]);

(* inputs (read only): a missing or unreadable input stops the run here, before any check, and nothing is written *)
readInput[p_String] := Module[{r},
  If[! FileExistsQ[p], Print["ERROR  input file not found: ", p]; Exit[1]];
  r = Quiet[Import[p, "RawJSON"]];
  If[! AssociationQ[r], Print["ERROR  input file is not a JSON object: ", p]; Exit[1]];
  r];
ksPath = FileNameJoin[{$revDir, "kohn_sham", "ks-theory.json"}];
ks = readInput[ksPath];
fx = readInput[FileNameJoin[{$revDir, "algebra", "gammas.json"}]];
(* the Kohn-Sham potentials of hypothesis H2, READ from ks-theory.json exchange.kohnShamPotentials: the coefficients
   of M_eff = m + cMeff lambda S and v_v = cVv lambda n, and e_int = cES lambda S^2 + cEn lambda n^2 parsed from the
   stated formula; they are compared with H2 and with each other in check T3_mean_field_map *)
pots = Lookup[Lookup[ks, "exchange", <||>], "kohnShamPotentials", <||>];
exactNum[s_String] := Module[{e = Quiet[ToExpression[s]]}, If[MatchQ[e, _Integer | _Rational], e, $Failed]];
exactNum[_] := $Failed;
cMeff = exactNum[Lookup[pots, "Meff_coefficient_of_lambda_S", None]];
cVv = exactNum[Lookup[pots, "vv_coefficient_of_lambda_n", None]];
eIntText = Lookup[pots, "e_int", None];
eCoef = If[StringQ[eIntText],
  StringCases[eIntText, "(" ~~ p : (DigitCharacter .. ~~ "/" ~~ DigitCharacter ..) ~~ ") lambda S^2 - (" ~~
    q : (DigitCharacter .. ~~ "/" ~~ DigitCharacter ..) ~~ ") lambda n^2" :> {exactNum[p], -exactNum[q]}, 1], {}];
{cES, cEn} = If[Length[eCoef] == 1, eCoef[[1]], {$Failed, $Failed}];
If[! AllTrue[{cMeff, cVv, cES, cEn}, MatchQ[#, _Integer | _Rational] &],
  Print["ERROR  cannot read the Kohn-Sham potentials (exchange.kohnShamPotentials: Meff_coefficient_of_lambda_S, vv_coefficient_of_lambda_n, e_int) as exact numbers from ", ksPath]; Exit[1]];

s1 = {{0, 1}, {1, 0}}; s2 = {{0, -I}, {I, 0}}; s3 = {{1, 0}, {0, -1}}; id2 = IdentityMatrix[2]; z2 = {{0, 0}, {0, 0}};
zeroQ[e_] := TrueQ[Simplify[ComplexExpand[e]] == 0];
vzeroQ[v_] := AllTrue[Flatten[{v}], zeroQ];

(* the block Hamiltonian of ks-theory.json blockEquation: h_j = j[-i sigma1 d_y + M sigma2 + kappa k sigma3] + v *)
hBlock[j_, M_, k_, chi_] := j (-I s1 . D[chi, y] + M[y] s2 . chi + kap[y] k s3 . chi) + vv[y] chi;
chi = {c1[y], c2[y]};
negM[y_] := -Mf[y];
lhs = hBlock[-j, negM, k, s2 . chi];
rhs = s2 . hBlock[j, Mf, k, chi];
addCheck["T3_block_hamiltonian_map",
  vzeroQ[(lhs - rhs) /. j -> 1] && vzeroQ[(lhs - rhs) /. j -> -1] && ! vzeroQ[(hBlock[-j, Mf, k, s2 . chi] - rhs) /. j -> 1],
  "for arbitrary functions M(y), kappa(y), v(y), any k and both block types j = +-1: h_(-j)(-M, k, v) (sigma2 chi) = sigma2 h_j(M, k, v) chi as differential operators (chi = (c1(y), c2(y)) arbitrary); so h_j(M) chi = eps chi iff h_(-j)(-M) (sigma2 chi) = eps (sigma2 chi): equal eigenvalue eps, same k, same potential v. Control: without M -> -M the identity fails"];

nOde[j_, M_, k_, eps_] := M s3 - kap k s2 + I j (eps - vv) s1;
addCheck["T3_ode_map",
  Simplify[s2 . nOde[j, M, k, eps] . s2 - nOde[-j, -M, k, eps]] == z2,
  "the shooting form chi' = N chi with N = M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1 (ks-theory.json blockEquation.ode): sigma2 N_j(M, k, eps) sigma2 = N_(-j)(-M, k, eps) exactly, so sigma2 maps solutions of the block-j ODE with M onto solutions of the block-(-j) ODE with -M at the same eps"];

qTip[th_] := Cos[th] s3 + Sin[th] s2;
addCheck["T3_tip_condition_map",
  Simplify[s2 . qTip[th] . s2 - qTip[Pi - th]] == z2 &&
  ((id2 - qTip[0]) . {1, 0} == {0, 0}) && ((id2 - qTip[0]) . (s2 . {1, 0}) != {0, 0}) && ((id2 - qTip[Pi]) . (s2 . {1, 0}) == {0, 0}),
  "tip condition (1 - Q(theta)) chi(-L) = 0, Q(theta) = Cos[theta] sigma3 + Sin[theta] sigma2 (ks-theory.json boundaryConditions.tip): sigma2 Q(theta) sigma2 = Q(Pi - theta), so chi obeys the tip condition with theta iff sigma2 chi obeys it with Pi - theta; the canonical theta = 0 (chi2(-L) = 0) goes to theta = Pi (chi1(-L) = 0). Negative control: the image of (1, 0) violates the UNtransformed condition theta = 0"];

jCur[j_, ph_, ch_] := -I j Conjugate[ph] . s1 . ch;
ph = {pa + I pb, pc + I pd}; ch = {qa + I qb, qc + I qd};
addCheck["T3_brane_parities_exchanged",
  (s2 . {1, 0})[[2]] =!= 0 && (s2 . {1, 0})[[1]] === 0 && (s2 . {0, 1})[[2]] === 0 &&
  Simplify[s2 . (id2 - s3) . s2 - (id2 + s3)] == z2 &&
  zeroQ[jCur[-j, s2 . ph, s2 . ch] - jCur[j, ph, ch]] && zeroQ[Conjugate[s2 . ch] . (s2 . ch) - Conjugate[ch] . ch],
  "brane (ASSUMED Z2 orbifold, ks-theory.json boundaryConditions.brane): even parity chi2(0) = 0 and odd parity chi1(0) = 0, i.e. (1 -+ gamma^(x8)) chi(0) = 0 with gamma^(x8) = sigma3 in every block; sigma2 (1 - sigma3) sigma2 = 1 + sigma3, so the map exchanges the two parities (both are solved and filled together in the Kohn-Sham record, so the set of boundary problems is mapped onto itself); the boundary current -i j phi^dagger sigma1 chi (selfAdjointness) and the norm chi^dagger chi are invariant under (chi, j) -> (sigma2 chi, -j): current-killing ends stay current-killing, the image block operator is self-adjoint with real levels"];

(* per-orbital densities of ks-theory.json densities.perOrbital (P = e^(-6 H y)/(ell^3 v_t) cancels) *)
chiC = {a1 + I b1, a2 + I b2};
dens[j_, c_] := ComplexExpand[{Conjugate[c] . c, j Conjugate[c] . s2 . c, j Conjugate[c] . s3 . c, Conjugate[c] . s3 . c, j Conjugate[c] . s1 . c}];
dO = dens[j, chiC] /. j -> 1; dI = dens[-j, s2 . chiC] /. j -> 1;
dO2 = dens[j, chiC] /. j -> -1; dI2 = dens[-j, s2 . chiC] /. j -> -1;
addCheck["T3_orbital_densities",
  Simplify[dI - {1, -1, 1, -1, 1} dO] === {0, 0, 0, 0, 0} && Simplify[dI2 - {1, -1, 1, -1, 1} dO2] === {0, 0, 0, 0, 0},
  "per orbital (ks-theory.json densities.perOrbital): n_o = chi^dagger chi, s_o = chi^dagger j sigma2 chi, t_o = chi^dagger j sigma3 chi (current along k-hat), q_o = chi^dagger sigma3 chi, c_o = chi^dagger j sigma1 chi; under (chi, j) -> (sigma2 chi, -j) at the same k: n_o -> n_o, s_o -> -s_o, t_o -> t_o, q_o -> -q_o, c_o -> c_o (exact for arbitrary complex chi, both j); hence n(y) and t(y) are even, S(y) and Q(y) odd under the map"];

(* the potentials read from ks-theory.json (top of the script).  v_v is written as a function of all four arguments
   (m, lambda, n, S) of the self-consistency loop, so that the map clause compares its values at DIFFERENT arguments:
   the image arguments (-m, +lambda, n, -S) against (m, lambda, n, S), and the control (-m, -lambda, n, -S) *)
meff[mm_, ll_, ss_] := mm + cMeff ll ss; vvf[mm_, ll_, nn_, ss_] := cVv ll nn; eint[ll_, nn_, ss_] := cES ll ss^2 + cEn ll nn^2;
mfH2 = {cMeff, cVv, cES, cEn} === {15/16, -1/16, 15/32, -1/32};
mfText = StringQ[Lookup[pots, "Meff", None]] && StringContainsQ[pots["Meff"], "M_eff(y) = m + (" <> ToString[cMeff, InputForm] <> ") lambda S(y)"] &&
  StringQ[Lookup[pots, "vv", None]] && cVv =!= 0 &&
  StringContainsQ[pots["vv"], "v_v(y) = " <> If[cVv < 0, "-", ""] <> "lambda n(y)/" <> ToString[1/Abs[cVv], InputForm]];
mfConsistent = Simplify[D[eint[lam, n, S], S] - (meff[m, lam, S] - m)] === 0 && Simplify[D[eint[lam, n, S], n] - vvf[m, lam, n, S]] === 0;
mfMap = Simplify[meff[-m, lam, -S] + meff[m, lam, S]] === 0 && Simplify[vvf[-m, lam, n, -S] - vvf[m, lam, n, S]] === 0 &&
  Simplify[eint[lam, n, -S] - eint[lam, n, S]] === 0;
mfControl = Simplify[meff[-m, -lam, -S] + meff[m, lam, S]] =!= 0 && Simplify[vvf[-m, -lam, n, -S] - vvf[m, lam, n, S]] =!= 0;
addCheck["T3_mean_field_map",
  mfH2 && mfText && mfConsistent && mfMap && mfControl,
  "Kohn-Sham potentials READ from ks-theory.json exchange.kohnShamPotentials (Hartree plus the exact uniform-gas exchange): M_eff = m + c_M lambda S, v_v = c_v lambda n, e_int = c_S lambda S^2 + c_n lambda n^2 with c_M = " <>
  ToString[cMeff, InputForm] <> " (Meff_coefficient_of_lambda_S), c_v = " <> ToString[cVv, InputForm] <> " (vv_coefficient_of_lambda_n), c_S = " <>
  ToString[cES, InputForm] <> " and c_n = " <> ToString[cEn, InputForm] <> " (parsed from the stated formula e_int). Consistency: these are the values of hypothesis H2 (15/16, -1/16, 15/32, -1/32); the two coefficients agree with the stated formulas Meff and vv of the same record; M_eff - m = d e_int/dS and v_v = d e_int/dn. Map (S -> -S, n -> n), with v_v written as a function v_v(m, lambda, n, S) of the four arguments of the self-consistency loop: M_eff[-m, +lambda, -S] = -M_eff[m, lambda, S], v_v(-m, +lambda, n, -S) = v_v(m, lambda, n, S) (its value at the image arguments equals its value at the original ones), e_int[lambda, n, -S] = e_int[lambda, n, S]. So the self-consistency loop commutes with the map exactly when the image carries (-m, +lambda). Control with (-m, -lambda): M_eff[-m, -lambda, -S] differs from -M_eff[m, lambda, S] (by 2 c_M lambda S) and v_v(-m, -lambda, n, -S) differs from v_v(m, lambda, n, S) (by -2 c_v lambda n)"];

(* energies and EMT profiles: two orbitals of opposite block type with general data, then the map *)
orbit[o_] := <|"j" -> If[o == 1, 1, -1], "chi" -> {ar[o] + I br[o], cr[o] + I dr[o]}, "eps" -> ep[o], "f" -> fo[o], "g" -> go[o], "k" -> kk[o]|>;
orbs = orbit /@ {1, 2};
imgOrb[ob_] := <|"j" -> -ob["j"], "chi" -> s2 . ob["chi"], "eps" -> ob["eps"], "f" -> ob["f"], "g" -> ob["g"], "k" -> ob["k"]|>;
dsum[obs_, idx_] := Sum[w2 ob["g"] ob["f"] dens[ob["j"], ob["chi"]][[idx]], {ob, obs}];
profiles[obs_, mm_, ll_] := Module[{nn = dsum[obs, 1], ss = dsum[obs, 2], me, ve, ei},
  me = meff[mm, ll, ss]; ve = vvf[mm, ll, nn, ss]; ei = eint[ll, nn, ss];
  {Sum[w2 ob["g"] ob["f"] ob["eps"] dens[ob["j"], ob["chi"]][[1]], {ob, obs}] - ei,
   Sum[w2 ob["g"] ob["f"] (kap Abs[ob["k"]]/3) dens[ob["j"], ob["chi"]][[3]], {ob, obs}] + ei,
   ei,
   Sum[w2 ob["g"] ob["f"] ((ob["eps"] - ve) dens[ob["j"], ob["chi"]][[1]] - me dens[ob["j"], ob["chi"]][[2]] - kap Abs[ob["k"]] dens[ob["j"], ob["chi"]][[3]]), {ob, obs}] + ei,
   Sum[ob["g"] ob["f"] ob["eps"], {ob, obs}] - ei,
   Sum[-tT ob["g"] (ob["f"] Log[ob["f"]] + (1 - ob["f"]) Log[1 - ob["f"]]), {ob, obs}],
   ei + lam/32 dsum[obs, 4]^2,
   ss, dsum[obs, 4]}];
pO = profiles[orbs, m, lam]; pI = profiles[imgOrb /@ orbs, -m, lam]; pC = profiles[imgOrb /@ orbs, -m, -lam];
addCheck["T3_energies_and_emt_profiles_equal",
  Simplify[ComplexExpand[pI[[1 ;; 7]] - pO[[1 ;; 7]]]] === ConstantArray[0, 7] && Simplify[ComplexExpand[pI[[8]] + pO[[8]]]] === 0 &&
  Simplify[ComplexExpand[pI[[9]] + pO[[9]]]] === 0 && Simplify[ComplexExpand[pC[[5]] - pO[[5]]]] =!= 0,
  "for arbitrary occupied orbitals of both block types (general complex chi, eps, occupation f, degeneracy g, momentum k, weight w = w_Z2) the pointwise energy density rho = sum w g f eps n_o - e_int, the pressures p3 = sum w g f (kappa |k|/3) t_o + e_int, p_t = e_int, p8 = sum w g f [(eps - v_v) n_o - M_eff s_o - kappa |k| t_o] + e_int (ks-theory.json emt), the integrand of E_KS = sum g f eps - 2 Vol_7 int e^(6Hy) e_int, the entropy terms and the exact-Fock diagnostic e_int + (lambda/32) Q^2 are EQUAL for the image state with (-m, +lambda), while S and Q change sign (control: with (-m, -lambda) the E_KS integrand differs). Levels eps and occupations f are carried over unchanged, so the Mermin chemical potential, N, the entropy, the grand potential Omega = -T sum g ln(1 + e^(-(eps - mu)/T)) - 2 Vol_7 int e^(6Hy) e_int and F = Omega + mu N are equal too"];

(* exact k = 0 spectra with constant M: characteristic functions *)
nk0[j_, M_] := M s3 + I j eps s1;
prop[j_, M_] := Module[{p = Sqrt[M^2 - eps^2]}, Cosh[p yy] id2 + Sinh[p yy]/p nk0[j, M]];
dEven0 = (prop[jj, MM] . {1, 0})[[2]] /. yy -> -LL;                  (* (M, j, even, theta = 0): chi2(-L) = 0 *)
dOddPi = (prop[-jj, -MM] . {0, 1})[[1]] /. yy -> -LL;                (* image: (-M, -j, odd, theta = Pi): chi1(-L) = 0 *)
dOdd0 = (prop[jj, MM] . {0, 1})[[2]] /. yy -> -LL;                   (* (M, j, odd, theta = 0) *)
dEvenPi = (prop[-jj, -MM] . {1, 0})[[1]] /. yy -> -LL;               (* image: (-M, -j, even, theta = Pi) *)
dCtl = (prop[-jj, -MM] . {0, 1})[[2]] /. yy -> -LL;                  (* control: image with the UNtransformed tip theta = 0 *)
okK0 = And @@ Table[Simplify[(dEven0 + dOddPi) /. jj -> jv] === 0 && Simplify[(dOdd0 - dEvenPi) /. jj -> jv] === 0, {jv, {1, -1}}];
ctl = ! TrueQ[Simplify[(dCtl - dEven0) /. jj -> 1] == 0] && ! TrueQ[Simplify[(dCtl + dEven0) /. jj -> 1] == 0];
zeroModeOk = Simplify[D[{0, I E^(MM y)}, y] - nOde[-1, -MM, 0, 0] . {0, I E^(MM y)} /. {kap -> 0, vv -> 0}] === {0, 0};
addCheck["T3_exact_k0_spectra",
  okK0 && ctl && zeroModeOk,
  "k = 0, v = 0, constant M (ks-theory.json boundaryConditions.exactK0Spectra): with chi(y) = exp(N y) chi(0), N = M sigma3 + i j eps sigma1, N^2 = (M^2 - eps^2) I, the characteristic function of (M, j, even parity, theta = 0) is minus that of (-M, -j, odd parity, theta = Pi), and that of (M, j, odd, theta = 0) equals that of (-M, -j, even, theta = Pi), identically in eps, M, L (both j): the two problems have the same spectrum level by level (even: eps = 0 and eps^2 = M^2 + (n Pi/L)^2; odd: tan(p L) = -p/M). The zero mode (E^(M y), 0) goes to (0, i E^(M y)), the zero mode of the image problem. Control: the image with the UNtransformed tip theta = 0 has a different characteristic function (Cosh[p L] + M Sinh[p L]/p type), i.e. a different spectrum"];

(* the 16-component chirality Gamma is this block map (block basis V of ks-theory.json) *)
num[x_String] := ToExpression[x]; num[x_] := x;
dec[x_Association] := Map[num, x["re"], {2}] + I Map[num, x["im"], {2}];
dec[x_List] := Map[num, x, {2}];
gm = dec /@ fx["gamma"]; chir = dec[fx["Gamma"]];
vRows = Map[ToExpression, ks["blockBasis"]["unnormalisedColumns2Sqrt2V"], {2}]/(2 Sqrt[2]);   (* rows = spinor components *)
labels = Map[ToExpression, ks["blockBasis"]["labels"], {2}];
vb[b_] := vRows[[All, 2 b + 1 ;; 2 b + 2]];
unit = Simplify[ConjugateTranspose[vRows] . vRows] == IdentityMatrix[16];
gmap = And @@ Table[Module[{jv = labels[[b + 1, 1]], s2v = labels[[b + 1, 2]], s3v = labels[[b + 1, 3]], bp},
    bp = First[FirstPosition[labels, {-jv, s2v, s3v}]] - 1;
    Simplify[chir . vb[b] - vb[bp] . (s2v s2)] == ConstantArray[0, {16, 2}]], {b, 0, 7}];
forms = And @@ Table[Simplify[ConjugateTranspose[vb[b]] . gm[[8]] . vb[b]] == s3 &&
    Simplify[ConjugateTranspose[vb[b]] . gm[[8]] . gm[[4]] . vb[b]] == labels[[b + 1, 1]] s1, {b, 0, 7}];
addCheck["T3_Gamma_is_the_block_map",
  unit && gmap && forms && chir == DiagonalMatrix[Join[ConstantArray[-1, 8], ConstantArray[1, 8]]],
  "with the unitary block basis V of ks-theory.json (rows = spinor components Psi_0..Psi_15) and Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) = diag(-I8, I8) of gammas.json: Gamma V_(j,s2,s3) = V_(-j,s2,s3) (s2 sigma2) for all 8 blocks, and in every block gamma^(x8) = sigma3, gamma^(x8) gamma^(x4) = j sigma1: the 2 x 2 map (chi, j) -> (sigma2 chi, -j) of T3 is the chirality Gamma of the 16-component Kohn-Sham orbital Psi_16 = e^(-i eps x4) e^(i k x1) e^(-3 H y) V_beta chi(y)/sqrt(ell^3 v_t) (up to the phase s2), applied at the same point"];

(* the ASSUMED Z2 orbifold: P_A chi(y) = sigma3 chi(-y) *)
chiY = {u1[y], u2[y]};
hPA[M_, K_, V_, c_] := (-I s1 . D[c, y] + M s2 . c + K kk0 s3 . c) + V c;
lhsPA = hPA[-Mf[-y], kap[-y], vv[-y], s3 . (chiY /. y -> -y)];
rhsPA = s3 . ((hPA[Mf[y], kap[y], vv[y], chiY]) /. y -> -y);
addCheck["T3_z2_mirror_copy_carries_minus_m_plus_lambda",
  vzeroQ[lhsPA - rhsPA] && Simplify[meff[m, lam, -S] + meff[-m, lam, S]] === 0,
  "the ASSUMED Z2 mirror of the Kohn-Sham record: P_A chi(y) = sigma3 chi(-y) satisfies h(-M(-y), kappa(-y), v(-y)) P_A chi = P_A h(M, kappa, v) chi (general functions), so the doubled (universe + mirror image) problem is P_A-symmetric iff M_eff is odd in y; with n even and S odd under P_A (n_o, s_o of sigma3 chi: sigma3 commutes with 1 and anticommutes with sigma2), M_eff(-y) = -M_eff(y) holds iff the mirror copy carries (-m, +lambda): m + (15/16) lambda S on the patch and -m + (15/16) lambda S(-y) = -(m + (15/16) lambda S(y)) on the mirror patch"];

(* ------------------------------------------------------------------ theorem record *)
nPass = Count[checks, c_ /; c["verdict"] == "PASS"]; nTot = Length[checks];
jstr[s_String] := "\"" <> StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\""}] <> "\"";
toJ[x_String, ind_] := jstr[x];
toJ[x_Integer, ind_] := ToString[x];
toJ[x_List, ind_] := If[x === {}, "[]", "[\n" <> StringRiffle[(ind <> "  " <> toJ[#, ind <> "  "]) & /@ x, ",\n"] <> "\n" <> ind <> "]"];
toJ[x_Association, ind_] := "{\n" <> StringRiffle[KeyValueMap[(ind <> "  " <> jstr[#1] <> ": " <> toJ[#2, ind <> "  "]) &, x], ",\n"] <> "\n" <> ind <> "}";
theory = <|
  "document" -> "Theorem T3 of Revision/SPEC.md section 9: the Kohn-Sham level of the pairing of universes of masses {+m, -m} for dirac16complex in the author's primordial field",
  "producer" -> "Revision/pairing/kohn_sham/wolfram/verify_t3.wls",
  "report" -> "Revision/pairing/kohn_sham/reports/wolfram-t3.json",
  "inputs" -> {"Revision/kohn_sham/ks-theory.json (block equation, functional, densities, energy-momentum tensor, boundary conditions, block basis V)", "Revision/algebra/gammas.json"},
  "status" -> If[nPass == nTot, "all checks of the report passed", "SOME CHECKS FAILED - see the report"],
  "coordinates" -> "x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; x8 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0] (brane y = 0, tip y = -L)",
  "hypotheses" -> {
    "H1 (the problem): the instantaneous Kohn-Sham problem of Revision/kohn_sham/ks-theory.json at a fixed slice a4,0 = a4(x4) of the author's metric: good sector (no extra-time momentum), 3-torus lattice of momenta k, block Hamiltonians h_j = j[-i sigma1 d_y + M_eff(y) sigma2 + kappa(y) k sigma3] + v_v(y) on y in [-L, 0], j = +-1, four blocks (s2, s3) per j",
    "H2 (the functional): Hartree plus the exact uniform-gas exchange, M_eff = m + (15/16) lambda S, v_v = -lambda n/16, e_int = (15/32) lambda S^2 - (1/32) lambda n^2 (no correlation); the energy-momentum tensor of ks-theory.json emt",
    "H3 (the brane, ASSUMED): the Z2 mirror (orbifold) construction at y = 0 of ks-theory.json boundaryConditions.brane; both brane parities (chi2(0) = 0 and chi1(0) = 0) are solved and filled together with the weight w_Z2 = 1/2",
    "H4 (the tip, chosen): (1 - Q(theta)) chi(-L) = 0, Q(theta) = Cos[theta] sigma3 + Sin[theta] sigma2 (canonical theta = 0)",
    "H5 (occupation): Mermin occupations f = 1/(1 + e^((eps - mu)/T)) with the particle number N fixed, and the filling CONVENTION of ks-theory.json thermodynamics (positive branch of the lambda = 0 problem plus the k = 0 zero modes, followed continuously in lambda)",
    "H6 (same remaining data): the same H, L, a4,0, lattice, extra-time volume, N and T for both members; mean-field (quasi-free) Kohn-Sham states only"},
  "statement" -> {
    "S1: (chi, j) -> (sigma2 chi, -j) at the same k, i.e. Psi_16 -> Gamma Psi_16 (the chirality, up to the phase s2 per block), maps every eigen-orbital of h_j with (M_eff, v_v) onto an eigen-orbital of h_(-j) with (-M_eff, v_v) at the SAME level eps, and exchanges the brane parities",
    "S2: the tip condition with angle theta goes into the tip condition with angle Pi - theta (canonical theta = 0 -> theta = Pi); with the untransformed tip the spectra differ (control)",
    "S3: the densities transform as n -> n, S -> -S, t -> t, Q -> -Q; hence M_eff -> -M_eff and v_v -> v_v exactly when (m, lambda) -> (-m, +lambda): every self-consistent Kohn-Sham state with (m, lambda, theta) is mapped onto a self-consistent Kohn-Sham state with (-m, +lambda, Pi - theta), and conversely (the map is an involution)",
    "S4: EQUAL Kohn-Sham levels with their degeneracies, occupations, chemical potential, particle number, entropy, Kohn-Sham energy E_KS, grand potential Omega and free energy F, and equal energy-momentum profiles rho(y), p3(y), p_t(y), p8(y) (also for the exact-Fock diagnostic); S(y) and Q(y) change sign",
    "S5: inside the ASSUMED Z2 orbifold the mirror copy of a self-consistent state carries (-m, +lambda) (P_A symmetry of the doubled problem), consistent with S3"},
  "proof" -> {
    "sigma2 h_j(M, k, v) sigma2 = h_(-j)(-M, k, v) and sigma2 N_j sigma2 = N_(-j)(-M) (checks T3_block_hamiltonian_map, T3_ode_map)",
    "sigma2 Q(theta) sigma2 = Q(Pi - theta), sigma2 (1 - sigma3) sigma2 = 1 + sigma3; the boundary current and the norm are invariant (T3_tip_condition_map, T3_brane_parities_exchanged)",
    "per orbital n_o, t_o even and s_o, q_o odd (T3_orbital_densities); M_eff[-m, lambda, -S] = -M_eff[m, lambda, S], v_v and e_int even in S (T3_mean_field_map)",
    "the map is a bijection between the eigen-orbitals of the two problems with equal eps (both j and both parities are part of each problem), so the occupations, mu, N and the entropy are equal; every term of E_KS, Omega, F and of the energy-momentum profiles is a sum over orbitals of even densities, or of M_eff s_o (product of two odd factors), plus e_int (even): equal (T3_energies_and_emt_profiles_equal)",
    "independent confirmation on exactly solvable data: equal k = 0 spectra level by level, and a different spectrum for the untransformed tip (T3_exact_k0_spectra); the 2 x 2 map is the 16-component chirality Gamma in the block basis (T3_Gamma_is_the_block_map); the Z2 mirror copy (T3_z2_mirror_copy_carries_minus_m_plus_lambda)"},
  "relation_to_T1_T2" -> "Interpretation (labelled, not a theorem): the 16-component matrix is the chirality Gamma of T1, but at the Kohn-Sham level the expectation values are taken with the fixed Krein metric B of the canonical quantisation (rho = sum f u u^dagger B), under which Gamma flips B (Gamma B Gamma = -B); the result is a pairing (m, lambda) -> (-m, +lambda) at EQUAL energies, of the T2 type in its parameters, not the T1 pairing (m, lambda) -> (-m, -lambda) with opposite energy-momentum",
  "verification" -> (#["name"] & /@ checks),
  "numerical_confirmation" -> "Revision/kohn_sham/reports/ks-rust-solver.json check t3_block_map_solver_selftest: (m, lambda, theta = 0) and (-m, lambda, theta = Pi) solved independently by the Rust Kohn-Sham solver give the same levels, occupations, E_KS and energy-momentum integrals and opposite S (a numerical test, not part of the proof)",
  "not_established" -> {
    "No creation process, rate or amplitude: T3 maps self-consistent Kohn-Sham states to self-consistent Kohn-Sham states of a second parameter set; it does not produce a pair of universes and does not force the partner to exist.",
    "Instantaneous (adiabatic) states only: the non-adiabatic, time-dependent Kohn-Sham problem along the history with the extra times deflating is OPEN; T3 holds slice by slice.",
    "The brane: the Z2 mirror construction at y = 0 is ASSUMED (ks-theory.json); the tip condition is a choice, and T3 needs the transformed tip angle Pi - theta.",
    "Mean-field level only: Hartree plus uniform-gas exchange without correlation, quasi-free states, the filling convention of ks-theory.json (its justification is OPEN).",
    "Not a statement about two independently quantised universes; the pairing is between Kohn-Sham problems with (m, lambda) and (-m, +lambda), not (-m, -lambda).",
    "No back-reaction: the Kohn-Sham energy-momentum tensor is not a source that satisfies the a4 equations of SPEC section 5 (it depends on x8), see Revision/field_equations_a4/reports/ks-source-conditions.json."}|>;
theoryText = toJ[theory, ""] <> "\n";
writeLF[path_, text_String] := Module[{st = Quiet[OpenWrite[path, BinaryFormat -> True]]},
  If[Head[st] =!= OutputStream, Print["ERROR  cannot write ", path]; Exit[1]];
  If[BinaryWrite[st, ToCharacterCode[text, "UTF-8"]] === $Failed, Close[st]; Print["ERROR  cannot write ", path]; Exit[1]];
  Close[st]];
If[! DirectoryQ[FileNameJoin[{$t3Dir, "reports"}]], CreateDirectory[FileNameJoin[{$t3Dir, "reports"}]]];
writeLF[FileNameJoin[{$t3Dir, "t3-theory.json"}], theoryText];
report = StringJoin[
  "{\n",
  "  \"report\": ", jstr["Revision pairing theorem T3 (SPEC section 9, the Kohn-Sham level), verified exactly in WolframScript"], ",\n",
  "  \"producer\": ", jstr["Revision/pairing/kohn_sham/wolfram/verify_t3.wls"], ",\n",
  "  \"theory\": ", jstr["Revision/pairing/kohn_sham/t3-theory.json"], ",\n",
  "  \"inputs\": ", jstr["Revision/kohn_sham/ks-theory.json, Revision/algebra/gammas.json"], ",\n",
  "  \"summary\": {\"passed\": ", ToString[nPass], ", \"failed\": ", ToString[nTot - nPass], ", \"total\": ", ToString[nTot], "},\n",
  "  \"checks\": [\n",
  StringRiffle[("    {\"name\": " <> jstr[#["name"]] <> ", \"verdict\": " <> jstr[#["verdict"]] <> ", \"detail\": " <> jstr[#["detail"]] <> "}") & /@ checks, ",\n"],
  "\n  ]\n}\n"];
writeLF[FileNameJoin[{$t3Dir, "reports", "wolfram-t3.json"}], report];
Print[nPass, "/", nTot, " checks passed; time ", Round[AbsoluteTime[] - t0, 0.1], " s"];
Exit[If[nPass == nTot, 0, 1]];
