# notebook-physics

## summary
Cell numbers below follow the numbering in nb_clean.txt / nb_cells.txt (1279 non-Output cells). Those dumps contained no Output cells, so I made a new dump with the same numbering plus every Output/Print/Message cell (830 of them), labelled "OUT after CELL n": scratchpad/nb_with_outputs.txt, and a copy with base64 lines stripped: scratchpad/nbo2.txt. I also rendered the image-bearing cells to PNG (scratchpad/img/cellN.png) so the formulas could be read.

1. EINSTEIN-LOVELOCK EQUATIONS AND a4
- Cell 14 is a Section cell titled "The Einstein-Lovelock vacuum field equations are A_a^b = 0, where". It embeds an image of Lovelock & Rund, Eq. (4.38): A^{lh} = sqrt(g) Sum_{k=1}^{m-1} alpha_(k) g^{jl} delta^{h h1..h2k}_{j j1..j2k} R^{j1j2}_{h1h2} ... R^{j2k-1 j2k}_{h2k-1 h2k} + lambda sqrt(g) g^{lh}, with m = n/2 for even n.
- Cell 14 then states "m-1 = 8/2 - 1 = 3", so Lovelock orders 1, 2 and 3 are used. It continues "Let {w1, w2, w3, Λ} be pure numbers; then by Eq. [4.38] the vacuum equations are 0 == -Λ + H^-2 w1 Lovelock1 + H^-4 w2 Lovelock2 + H^-6 w3 Lovelock3".
- H is described as "a fundamental inverse length that exists in virtue of the fact that the Einstein-Lovelock tensors have different dimensions". The author says he does not attempt to link H to the Planck length or the Lemaitre-Hubble parameter.
- No code anywhere defines Lovelock2 or Lovelock3, and w1, w2, w3, Λ never appear in code. Only the Einstein tensor is computed: rt[] in cell 248, run as rt[gtry] with gtry = MatrixMetric44 in cells 262/265.
  - Cell 583 output: RS = 6*H^2*(-7 + Derivative[1][a4][H*x4]^2).
  - Cell 584 output, EinsteinG (covariant, diagonal):
    - G00 = -3*H^2*Cot[6*H*x0]^2*(-5 + a4'^2)
    - G11 = G22 = G33 = -E^(2*a4)*H^2*Sin[6*H*x0]^(1/3)*(-15 + 3*a4'^2 - a4'')
    - G44 = -3*H^2*(7 + a4'^2)
    - G55 = G66 = G77 = H^2*Sin[6*H*x0]^(1/3)*(-15 + 3*a4'^2 + a4'')/E^(2*a4)
    - Here a4 and its derivatives are evaluated at H*x4.
  - My own derivation from this output (not in the notebook): G^4_4 = 3H^2(7 + a4'^2) is never zero for real a4. Requiring G^mu_nu = const*delta forces a4'' = 0 and then a4'^2 = -1. So MatrixMetric44 solves neither vacuum Einstein nor Einstein+Λ for real a4.
- The notebook never claims MatrixMetric44 is a vacuum solution. Cells 24/25/28 say "Universe sources for gαβ; be sure to append these to the Einstein and/or Einstein-Lovelock field equations." The source TU is only hoped to be Λ g (point 2).
- a4 is never obtained from field equations. It enters as follows:
  - Cell 151 defines β3 = Exp[2*a4[H*x4]], with commented-out alternatives:
    - (*β3=Exp[2 H x4 Sqrt[K^2-M^2]];*)
    - (*β3=Exp[2*a4[3*H*x4]];*)
    - (*/.{a4->(((K1*2(1+M)/3 + K2*2/3(-1+M))#)&)}*)
  - Cell 150 is a pasted Text cell with no derivation shown: "6*H*x0 == z && H*x4 == t, {{Derivative[2][a4][t] -> 0, Derivative[1][a4][t] -> (2/3)*(-1 + M)}, {Derivative[2][a4][t] -> 0, Derivative[1][a4][t] -> (2*(1 + M))/3}}". This gives linear a4 with slope 2(M-1)/3 or 2(M+1)/3.
  - Cell 100 (Text): DSolve[0 == (-M)*(c[0]+c[1]+...+c[7]) + (Q1 - Q1/E^(2*a4[t]))*Derivative[1][a4][t], a4[t], t].
  - Cell 99 gives its solution: {{a4[t] -> (M*t*(c[0]+...+c[7]))/Q1 + C[1] + (1/2)*ProductLog[-E^(-((2*M*t*(c[0]+...+c[7]))/Q1) - 2*C[1])]}}.
  - Cell 1157 solves the spinor-rescaling equation: DSolve[0 == Q1*Sinh[a4[t]]*a4'[t]/E^a4[t] - BY'[t]] gives BY[t] -> (1/2)*Q1*(1/2/E^(2*a4[t]) + a4[t]) + C[1].
  - In the Maple results a4 appears as the arbitrary function A4[t].
- EQ1/EQ2/EQ2L9i/EQ3/EQ4 are not gravity equations. They are Maple solutions of the spinor Euler-Lagrange blocks (point 3).

2. SOURCE TENSOR TU
- Cell 22 (Section): "The Euler-Lagrange equations for Ψ16 must have 'solutions' such that all off-diagonal terms of TU^μν ARE ZERO."
- Cell 23, read from the rendered image:
  - Definition: (1/κ) TU^μν ≡ (1/Sqrt[Det[g_αβ]]) ∂/∂g_μν ( Sqrt[Det[g_αβ]] LagrangianΨ16 ).
  - The hope: "(hope that TU^μν = Λ g^μν, and H = some function of M, where Universe(s) of masses ± M created in pairs at time x4 = 0 ...)".
  - Lagrangian used: Sqrt[Det g]*Lg[] = Sqrt[Det g]*( Transpose[Ψ16].σ16.Sum[T16^α[α1-1].{1_16x16 ∂/∂x^(α1-1) - Γ_(α1-1)}.Ψ16, {α1,1,Length[X]}] + (mASs/2)*Transpose[Ψ16].σ16.Ψ16 ).
  - Derivation: TU/κ = Lg[]*[(1/√Det) ∂√Det/∂g_μν] + ∂Lg[]/∂g_μν. The first term is dropped because Lg = 0 on-shell (written "0?*"). The result is "= Transpose[Ψ16].σ16.Sum[∂/∂g_μν (T16^α[α1-1]) . Ψ16,α1-1 ...] = Ψ16~ .σ16. T16^A . Ψ16,α ∂/∂g_μν (e^α_(A))".
  - Method notes in the same cell: ∂(g^-1)/∂q = -g^-1.∂g/∂q.g^-1; ∂e^α_(A)/∂g_μν = -Inverse[e].∂e/∂g_μν.Inverse[e]; "In metric matrix g, we must replace element g_μν with (g_νμ + g_μν)/2, and then differentiate".
- Cells 25 and 28 repeat this with Tα = {T16α[0], T16α[4]} (only x0 and x4 derivatives) and the mass term mASs*Transpose[Ψ16].symm16[[134,1]].Ψ16. They add "Let j = 134, σ16.(mass Matrix) = T16α[5].T16α[6].T16α[7]", and "usingLagrangianF16massive = 0, as shown below".
- No code cell computes TU or any off-diagonal component; the derivation exists only in text. It varies only the vierbein inside T16^α. The metric dependence of ω/Γ, and of √g in the off-shell term, is not carried through.

3. MASS EIGENVALUE, "PAIR OF UNIVERSES ±M", AND Ψ16 SOLUTIONS
- Cell 6: "HYPOTHESIS: If, employing the Einstein eqs (or Einstein-Lovelock eqs), superluminal inflation/deflation exists, then at time x4 = 0 ... a pair of universes with MASSES ± M is created". The same cell says the author is "ONLY looking for superluminal inflation or deflation type solutions, and NOT solutions that are even/odd functions of t (like Cos[ν[j]'[0] * t], Sin[...], Sech[...], Tanh[...])".
- Cell 17: "M is the mass of the Ψ16 field"; "TODO: prove Universe(s) of masses ±M are created in pairs!"
- Cell 101: "M c[j] = (j+1)st Energy Eigenvalue for Transpose[cayZ].Ψ16, j= 0, ..., 7". No code defines c[j]. In the current run cayZ2 is only the permutation Z→yZ (cell 1116 shows the identity in yZ order).
- Production Lagrangian is La[] (cell 1066): Cos[6Hx0]*(Transpose[Ψ16].σ16.Sum[useT16[[α1]].(D[Ψ16,X[[α1]]] + (Q1/2)*Sum[ωμIJ[α1][[A1,B1]]*SAB[[A1,B1]]].Ψ16)] + (H*M)*Transpose[Ψ16].σ16.Ψ16). Here Cos[6Hx0] = √Det (cells 1060/1061), and ωμIJ[1] is identically 0 (cell 1065).
- Chain: eLa (cell 1078) → eLazt (cell 1096) = FullSimplify[(1/(2H)) eLa /. sfψ16Aa /. sx0x4], with f16[k][x0,x4] -> Z[k][6Hx0, Hx4] (cell 111).
- Coupling sets (cells 1089/1092): {{0,5,8,13},{1,4,9,12},{2,7,10,15},{3,6,11,14}}.
- Relabelling sZtOyZ (cell 1111): Z0→yZ0, Z5→yZ1, Z8→yZ2, Z13→yZ3, Z1→yZ4, Z4→yZ5, Z9→yZ6, Z12→yZ7, Z2→yZ8, Z7→yZ9, Z10→yZ10, Z15→yZ11, Z3→yZ12, Z6→yZ13, Z11→yZ14, Z14→yZ15.
- Separated equations, coupledyZeqs (cell 1137 output; primes are d/dt on a4[t]). Write q ≡ Q1*Sinh[a4[t]]*a4'[t]/E^a4[t].
  - Block 1:
    - ∂t yZ0 = -3yZ1 - M yZ3 + q yZ0 - 6Tan[z]∂z yZ1
    - ∂t yZ1 = -3yZ0 - M yZ2 - q yZ1 - 6Tan[z]∂z yZ0
    - ∂t yZ2 = M yZ1 + 3yZ3 - q yZ2 + 6Tan[z]∂z yZ3
    - ∂t yZ3 = M yZ0 + 3yZ2 + q yZ3 + 6Tan[z]∂z yZ2
  - Block 2 (yZ4..7): the same pattern with signs flipped.
  - Block 3 (no Q1):
    - ∂t yZ8 = 3yZ9 + M yZ11 + 6Tan[z]∂z yZ9
    - ∂t yZ9 = 3yZ8 + M yZ10 + 6Tan[z]∂z yZ8
    - ∂t yZ10 = -M yZ9 - 3(yZ11 + 2Tan[z]∂z yZ11)
    - ∂t yZ11 = -M yZ8 - 3(yZ10 + 2Tan[z]∂z yZ10)
  - Block 4 (yZ12..15): analogous to block 3.
- Rescaling (cells 1158/1189): yZk = xyZk*Exp[(1/2)*Q1*(1/2/E^(2*a4) + a4)] for k = 0..7. After it (cell 1160):
  - ∂t xyZ0 = -3xyZ1 - M xyZ3 - 6Tan[z]∂z xyZ1
  - ∂t xyZ1 = -3xyZ0 - M xyZ2 + (-1 + E^(-2a4))Q1 a4' xyZ1 - 6Tan[z]∂z xyZ0
  - xyZ2 and xyZ5, xyZ6 keep a similar (-1+E^(-2a4))Q1 a4' term; xyZ0, 3, 4, 7 lose it.
  - My interpretation, not stated in the notebook: cell 100's DSolve makes that leftover coefficient Q1(1 - E^(-2a4))a4' equal the constant M*Σc, which is where the "M c[j] eigenvalue" and the ProductLog a4 come from. At late times a4 ≈ M Σc t/Q1, so e^(2a4) inflates g11..g33 while e^(-2a4) deflates g55..g77.
- DSolve on each block returns unevaluated (cells 1142, 1145, 1146, 1148, 1149, 1161, 1162), so the author moved to Maple.
- Maple results:
  - (a) Cell 257 string `sta`: nZ10(z,t) = (c2C7*sin(C2Q1*t) + c2C8*cos(C2Q1*t))*(c2C5*sin(z)^(sqrt(-C2Q1^2+M^2)/6) + c2C6*sin(z)^(-sqrt(-C2Q1^2+M^2)/6)). nZ11 has the same form with c2C1..c2C4. nZ8 and nZ9 are combinations that also contain cos(M*t), sin(M*t) (c2C9, c2C10) divided by sqrt(M^2 - C2Q1^2). Cell 259 `sti` is the same but with unevaluated Int().
  - (b) Cell 1203, maplestringEQ3 (block yZ8..11), converted in cell 1205: yZ10 = (c37 sin(sqrt(M^2-36C3-9)t) + c38 cos(...))(c36 sin(z)^(-sqrt(1+4C3)/2) + c35 sin(z)^(sqrt(1+4C3)/2))/sqrt(sin z). yZ11 is analogous. yZ8 and yZ9 are combinations divided by M sqrt(sin z).
  - (c) Cell 1204, maplestringEQ4: the same structure for yZ12..15 with C4, c41..c48.
  - I checked numerically in Mathematica that both the EQ3 and EQ4 solutions satisfy the cell-1137 block-3 and block-4 equations (scratchpad/verify_eq3.wls, verify_eq4.wls).
  - With nZ = sqrt(sin z)*yZ and C2Q1^2 = M^2 - 36C - 9, the exponent becomes sqrt(M^2 - C2Q1^2)/6, i.e. the `sta` form.
  - The t-dependence is oscillatory when M^2 > 36C+9 and hyperbolic otherwise.
  - My observation: the equations are invariant under M → -M together with (yZ8,yZ9) → -(yZ8,yZ9); the notebook does not state this.
  - (d) solvedEQ1, solvedEQ2, solvedEQ2L9i (cells 1195-1198 and outputs of cells 1209-1211), read from thinkpad_stringEQ1.txt, thinkpad_stringEQ2.txt and stringSEQ2_2026_01_23_xyZ_2sets_L9i.txt. They are not closed forms: XyZ0, XyZ1, XyZ2 are given in terms of XyZ3, which obeys a residual Derivative[0,4][XyZ3] == ... equation. They contain nested Integrate and A4[t], with constants c11, c12 (EQ1) and c21, c22 (EQ2). Cell 1200: "too long to load".

4. CONSTANTS AND COORDINATES
- Cell 58: Protect[DIM8, M, K, H]. None of these is ever given a numeric value.
- Cell 71 (constraintX) assumes H > 0, M > 0, K > 0, Q > 0, z > 0, t > 0, a4[x4] > 0, among others. Cell 68, constraintTrig ("hacks (a.k.a., lies)"), assumes Sin/Cos/Tan/Cot[6Hx0] > 0 and Sin[z] > 0.
- Cell 17: "K is used to track spin coefficients; K == 1; set K→1 to employ [total] covariant derivative of spinors; put K→0 to ignore". In the current code the spin-connection coefficient is Q1/2 (cells 4, 1064, 1066; the Q12 in cell 4 of the old dump is Q1/2).
- Cell 1063: "Q2 = 0; Protect[Q1, Q2]". Q1 stays symbolic and Q2 is never used elsewhere.
- K0 and K4 appear only in Lj[j] (cell 1072), as separate coefficients (K0/2, K4/2) of the x0 and x4 spin-connection terms.
- M: mass of Ψ16, entering as (H*M) Ψ^T σ16 Ψ. H: the Lovelock inverse length (cell 14).
- Cell 76: 6*H*x0 == z && H*x4 == t, giving szt and sx0x4 = {x0 -> z/(6*H), x4 -> t/H} (cell 1132 output).
- Cell 59, coordinate roles: x0 "hidden space", x1..x3 "3-space", x4 "time", x5..x7 "superluminal deflating time".
- Cells 37/38 print "g_αβ(x0,x4) = diag{g00(x0), g11, g11, g11, -1, g77, g77, g77}" and "where g77(x0,x4) = g11(x0,-x4)".
- Other separation constants: C2Q1 (cell 257), C3/C4 (cells 1203/1204), C[1] (cells 99, 1157), and K1, K2 (cell 151 comment).

5. base16 / symm16 / j=134 / covariantDiffMatrix
- base16 (cell 594) holds the 256 ordered products T16^A[j]T16^A[k]... (cells 592 and 588-590 confirm the count of 256). Each entry is {matrix, index list}.
- Cell 596: Tr[M.M/16] = ±1. Cells 597-599: 136 entries with positive Tr[M.M], 120 with negative.
- antisymm16 has 120 entries (cell 608) and symm16 has 136 (cell 609).
- σ16 = base16[[93]] = symm16[[49]] = T0T1T2T3 (cells 612-615).
- symm16[[134]] = base16[[250]], index list {0,1,2,3,5,6,7} (cells 616/617). Cell 619: σ16.T16A[5].T16A[6].T16A[7] == symm16[[134]][[1]] → True. So mass matrix T5T6T7 gives a symmetric bilinear σ16.T5T6T7.
- T16A[8] = base16[[255]] = symm16[[135]] (cells 620/621).
- covariantDiffMatrix = T16A[5].T16A[6].T16A[7] (cell 396, also named in the cell 384 Section title). It equals base16[[92]] (index {5,6,7}, cell 611). Cell 397: σ16.covariantDiffMatrix is symmetric (True).
- Roles:
  - (i) An alternative mass term mASs*Ψ^T.symm16[[j,1]].Ψ with j = 134 (text cells 23/25/28 only; never coded).
  - (ii) Lj[j] (cell 1072) inserts base16[[j,1]] after SAB in the K0/K4 spin-connection terms. Lj[92] (cell 1073) was evaluated: its output has no ω/K terms, only derivative terms plus 2HM mass terms.
  - (iii) Cells 982-1052: candidate complex structures J with J.J = -ID16 and J^T σ16 J = σ16. There are 56 candidates (cells 984/985). T16A[4] is one of them, and Jcomplement is built from base16[[222..224]] with angles Q7, Q8.
  - (iv) linTrans (cells 627-643) is a Z-reordering permutation. It is expanded in base16: 10 symmetric and 6 antisymmetric components.

6. GRASSMANN / FERMION / QUANTIZATION
- A case-insensitive search of the full dump and the raw .nb finds no Grassmann, anticommuting, fermion, quantization, Dirac sea, second quantization or canonical anticommutator. Everything is classical, commuting and real: eL[] differentiates with respect to f16[k][x0,x4].
- The closest related material:
  - Cells 2/3 and 395: σ16.T16^A is antisymmetric, so Ψ^T σ16 T^A Ψ = 0 for commuting Ψ.
  - Cell 976: "want ψcc.σ16.?.Ψ16 = Ψ16.J.σ16.?.Ψ16 ≠ 0". Cell 977: "x0 has periodic fns; use x4".
  - The Complex Structure section (cells 921-1055) looks for such a J.
  - Cells 1218-1277 build Dirac-spinor wavefunctions in u^a: DDξ[f] := -I D[f,#] over U1by4, Σ^2, j0, c_op, ψnj0ss3 with LaguerreL × WignerD. These are single-particle eigenfunction checks, with no field quantization.

7. SECTION STRUCTURE (cell: level, title)
- 1: Title, "Scratch work of Author"
- 5: Section, NOTES
- 7: Section, "Bigger Bang: Question: Are Universe (s) of masses ± M created in pairs at time x4 = 0 (before the particles of the standard model exist) ?"
- 14: Section, "The Einstein-Lovelock vacuum field equations are Aab = 0, where" (plus image)
- 22: Section, "WARNING: Universes Ψ16 source gαβ; The Euler-Lagrange equations for Ψ16 must have 'solutions' such that all off-diagonal terms of TUμν ARE ZERO."
- 24: Section, "I copied and pasted too often; however, I am going to leave this here. Universe sources for gαβ ..."
- 25: Section, the same plus the j=134 derivation
- 34: Section, Begin
- 98: Section, "defs; some Symbols; metric"
- 183: Section, constants
- 196: Section, "some function definitions :"
- 251: Section, "Mathematica Lexer and Parser for Maple - like Syntax ..."
- 261: Section, "gtry and Γ and ..."
- 281: Section, "OCTAD eα ← spacetime(A)⟵ Lorentz :"
- 282: Subsection, "eα(A)=eα(A)=eAa"
- 308: Section, "For Spin(4,4); τ tau;T16;OCTAD:Nash; Introduce the wave function, Ψ16, for this Universe::"
- 309: Section, "O(4,4); evalues, evecs of σ"
- 317: Section, "SO(4), γ; M8, {0..7}, {+,+,+,+,-,-,-,-}, {x0..x7}"
- 345: Section, "SO(4,4), Spin(4,4) = SO(4,4)_e, τ ; if using xact: M8, ..."
- 384: Section, "(image); O(4,4): SAB ; covariantDiffMatrix=T16A[5].T16A[6].T16A[7] S=(abcd)... block formula"
- 430: Section, "SAB=Table[1/4 (T16A[A1].T16A[B1]-T16A[B1].T16A[A1]), ...]"
- 472: Section, T16α
- 478: Section, "CHECK Table[T16α[α1-1]= Sum[(e(A)α[[α1,A1]]) T16A[A1-1],...]; and...:"
- 497: Section, "metric compatibility condition for the Octad"
- 561: Subsection, CHECK
- 587: Section, "BASIS of 16 × 16 matrices :"
- 622: Subsubsection, "similarly :"
- 644: Section, "BASIS of 8 × 8 matrices :"
- 669: Section, "For the split orthogonal group Spin(4,4) ... three fundamentally equivalent 8-dimensional representations: 1. The vector representation V 2. The type-1 spinor representation S+ ..."
- 694: Section, "Killing Vector Fields"
- 707: Section, "44 Dirac γ matrices :"
- 741: Section, "S44αβ commutation relations; misc:"
- 773: Section, "BASIS of 4 × 4 matrices :"
- 805: Section, "O(4,4); evalues, evecs of σ"
- 837: Section, "split octonions; evalues, evecs of σ"
- 890: Section, (empty)
- 891: Section, "split octonion multiplication constants :" (image)
- 921: Section, "Complex Structure"
- 1056: Section, "Spinor Lagrangian"
- 1076: Section, eLa
- 1094: Section, eLazt
- 1150: Section, "change of vars :"
- 1163: Title, "TRY MAPLE :"
- 1180: Title, "\"Solution\" by Maple"
- 1212: Title, image only; same image as cell 13 ("A new spin-1/2 wave equation", Nash)
- 1218: Section, "Dirac spinor with components uª, a = 1, 2, 3, 4; irrep, and DDξ, ..."
- 1259: Section, ψnj0ss3

## key_files
- C:/Users/nsh/Developer/github/Dirac_claude/Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb :: Original notebook, 24 MB, 1610 Output-cell references. Only read, never modified.
- C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/nb_with_outputs.txt :: New dump that keeps the nb_clean.txt cell numbering and adds Output/Print/Message cells after their input as 'OUT after CELL n [Output] Out[k]='. Includes CellLabels. Text cells made of BoxData are converted to InputForm, so fractions survive. Lines capped at 4000 chars.
- C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/nbo2.txt :: nb_with_outputs.txt with base64 lines removed, Image[NumericArray..] collapsed to <<IMAGE>>, and lines capped at 2500 chars. About 575 KB, the easiest version to grep.
- C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/img/ :: Rendered PNGs of cells 8-14, 16-18, 20, 22, 23, 25-27, 99-101, 150. The key ones are cell14.png (Lovelock-Rund Eq. 4.38 and the w1/w2/w3 vacuum equation), cell23.png and cell25.png (TU derivation with proper fractions and square roots), and cell17.png.
- C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/cell_index.txt :: Line numbers of every '===== CELL n' header in the 648 MB nb_cells.txt, used by getcell.sh.

## commands
- wolframscript -file C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/extract_out.wls  -- writes nb_with_outputs.txt in about 4 s. It uses ToExpression[boxes, StandardForm, HoldComplete] with TimeConstrained 20 s per cell, and skips cells containing GraphicsBox/RasterBox/DynamicModuleBox.
- grep -a -v -E '^[A-Za-z0-9+/=]{40,}$' nb_with_outputs.txt > nbo_clean.txt; awk '{ if ($0 ~ /NumericArray\[\{\{\{/) print "<<IMAGE>>"; else if (length($0)>2500) print substr($0,1,2500) " ...[LINE CUT]"; else print }' nbo_clean.txt > nbo2.txt
- awk '/^===== CELL 1096 /,/^===== CELL 1097 /' nbo2.txt  -- prints one cell together with its outputs (run in the scratchpad directory)
- wolframscript -file scratchpad/raster.wls 14 23 25  -- renders the listed cells (dump numbering) to scratchpad/img/cellN.png through UsingFrontEnd[Rasterize[Notebook[{cell}]]] in about 10 s. A harmless RegisterFormat::interr message is printed.
- wolframscript -file scratchpad/verify_eq3.wls ; wolframscript -file scratchpad/verify_eq4.wls  -- confirmed that the Maple EQ3 and EQ4 solutions satisfy the cell-1137 block-3 and block-4 equations; residuals are {0,0,0,0} symbolically and numerically.
- ./scratchpad/getcell.sh N  -- prints full cell N from the 648 MB nb_cells.txt with base64 lines filtered, using cell_index.txt.

## reusable_code
- C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/extract_out.wls :: Notebook-to-text extractor that includes Output cells and CellLabels and keeps the same cell numbering as nb_clean.txt :: Edit nbFile/out at the top. Output cells are listed after the input cell they follow, labelled 'OUT after CELL n'.
- C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/raster.wls :: Renders chosen notebook cells (by dump index) to PNG through the front end :: Run wolframscript -file raster.wls <n1> <n2> ...; the PNGs land in scratchpad/img/. Use it for any Text cell whose fractions, roots or inline images the text dump garbles.
- C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/verify_eq3.wls :: Symbolic and numeric check that the Maple yZ8..yZ11 solution (maplestringEQ3, cell 1203) solves coupledyZeqs block 3 (cell 1137); verify_eq4.wls does the same for yZ12..15 :: Edit the Y* definitions or equations to test other candidate solutions, for example the nZ strings in cell 257.
- C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad/solved2.wls :: Inspects the large solvedEQ1/2/2L9i outputs (Out[1348..1350]) with MakeExpression, without evaluating them: equation left-hand sides, unknown functions, constants :: Use MakeExpression, not ToExpression with ReleaseHold. ReleaseHold triggers the embedded Integrate calls and did not finish within 600 s.

## pitfalls
- The earlier nb_clean.txt / nb_cells.txt dumps contain no Output cells, so every result (EinsteinG, RS, eLazt, the coupled equations, the Maple conversions) is missing from them. Use nb_with_outputs.txt / nbo2.txt instead.
- The old text dump flattens Text cells written as BoxData and loses fractions, square roots and E. For example cell 4 'Q12' is Q1/2, cell 150 'a4′[t]23 (-1+M)' is (2/3)(-1+M), and cell 99's ProductLog argument is -E^(...). Cell 23 '1κTUμν ≡ 1Det[gαβ]' is (1/κ)TU ≡ (1/Sqrt[Det g]).
- In[] numbers are non-monotonic and outputs come from different sessions: cell 265 printed 'Fri 25 Sep 2026 06:11', while cell 1096 shows a DateObject from 2026-01-30. The .mx names differ as well: header '2026-01-30-...-L9i-' versus loaded '2026-01-29-...-mmM4pro-'. The outputs may not form one consistent evaluation.
- External inputs are absent from the repo: thinkpad_stringEQ1.txt, thinkpad_stringEQ2.txt, stringSEQ2_2026_01_23_xyZ_2sets_L9i.txt, the *.mx dumps, and ConvertMapleToMathematicaV2.m. Cell 41 shows Get::noopen for the latter at C:/Users/nsh/Documents/8-dim/2026-02-09-Eternal-DEFLATION-Inflation-M4-MAX/.
- Lj[j] (cell 1072) adds 'Transpose[Ψ16].σ16.useT16[[5]].D[Ψ16,X[[5]]]' twice, so the x4-derivative terms in the Lj[92] output carry a spurious factor of 2 relative to the x0 terms. The production Euler-Lagrange chain uses La[] (cell 1066), not Lj.
- Cell 1122 says 'BUT NOT ORTHOGONAL O(8,8) SIMILARITY TRANSFORMATION', yet cell 1123 (cayZ2.σ16.Transpose[cayZ2] === σ16) outputs True, and cayZ2 is just the Z→yZ permutation. Cell 1124 says 'Not a Direct Sum', but cells 1125/1126 both output True.
- Cell 25's 'σ16.(mass Matrix)=T16α[5].T16α[6].T16α[7]' is loose. Code (cell 619) shows symm16[[134]] = σ16.T16^A[5].T16^A[6].T16^A[7], so the mass matrix is T5T6T7 = covariantDiffMatrix, using flat T16^A rather than curved T16^α.
- ReleaseHold/ToExpression on the solvedEQ outputs evaluates the embedded Integrate calls and hangs (it timed out after 600 s). Use MakeExpression or keep HoldComplete.
- The TU derivation (cells 23/25) varies only the vierbein inside T16^α. The metric dependence of ω/Γ and the √g term are dropped, and TU is never computed in code.
- Cell 6 and some Wikipedia screenshots (cells 26, 27) are not physics results. Cells 8-13 and 30-33 are reference title images (Dirac 1963, Nash papers, Nuovo Cimento 1990).

## open_questions
- Where do cell 150's a4'[t] = 2(M-1)/3 or 2(M+1)/3 (with a4'' = 0) come from? No derivation appears; they look pasted from an earlier version, perhaps a Lovelock or source-balance condition.
- No code computes Lovelock2/Lovelock3 or fixes w1, w2, w3, Λ, H. Is there a companion notebook or Maple worksheet with the Einstein-Lovelock tensors for MatrixMetric44?
- c[j] in cells 99-101 ('M c[j] = (j+1)st Energy Eigenvalue for Transpose[cayZ].Ψ16') is never defined. In the current run cayZ2 is only a permutation, so the eigenvalue claim seems to come from an older version of the equations.
- The nZ solutions in cell 257 (with C2Q1 and cos(M t) terms in nZ8, nZ9) do not obviously correspond to the current coupledyZeqs; snewfψ16Aa, the nZ/Sqrt[Sin] substitution, is defined in cell 113 but never applied. nZ10 and nZ11 do match EQ3's yZ10 and yZ11 under nZ = sqrt(sin z) yZ with C2Q1^2 = M^2-36C3-9.
- The text files behind solvedEQ1/2/2L9i (thinkpad_*.txt, stringSEQ2_*.txt) and ConvertMapleToMathematicaV2.m are not in the repo; only the stored outputs remain.
