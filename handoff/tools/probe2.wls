ID4=IdentityMatrix[4]; ID8=IdentityMatrix[8]; ID16=IdentityMatrix[16];
eta=DiagonalMatrix[{1,1,1,1,-1,-1,-1,-1}];
Qa[h_,p_,q_]:=Signature[{h,p,q,4}]; Qb[h_,p_,q_]:=ID4[[p,4]] ID4[[q,h]]-ID4[[p,h]] ID4[[q,4]];
s4[h_]:=Table[Qa[h,p,q]-Qb[h,p,q],{p,4},{q,4}]; t4[h_]:=Table[Qa[h,p,q]+Qb[h,p,q],{p,4},{q,4}];
tau[0]=ID8; Do[tau[7-h]=ArrayFlatten[{{0,t4[h]},{-t4[h],0}}],{h,1,3}]; Do[tau[h]=ArrayFlatten[{{0,s4[h]},{s4[h],0}}],{h,1,3}];
tau[7]=tau[1].tau[2].tau[3].tau[4].tau[5].tau[6]; sig=ArrayFlatten[{{0,ID4},{ID4,0}}];
taub[0]=ID8; Do[taub[A]=sig.Transpose[tau[A]].sig,{A,1,7}];
T[A_]:=T[A]=ArrayFlatten[{{0,taub[A]},{tau[A],0}}]; sig16=ArrayFlatten[{{-sig,0},{0,sig}}];
S[a_,b_]:=S[a,b]=(T[a].T[b]-T[b].T[a])/4;
X={x0,x1,x2,x3,x4,x5,x6,x7};
s=Sin[6 H x0];
g=DiagonalMatrix[{Cot[6 H x0]^2, s^(1/3) E^(2 a4[H x4]), s^(1/3) E^(2 a4[H x4]), s^(1/3) E^(2 a4[H x4]), -1, -s^(1/3) E^(-2 a4[H x4]), -s^(1/3) E^(-2 a4[H x4]), -s^(1/3) E^(-2 a4[H x4])}];
assum = 0<6 H x0<Pi/2 && H>0;
ev=DiagonalMatrix[{Cot[6 H x0], s^(1/6) E^(a4[H x4]), s^(1/6) E^(a4[H x4]), s^(1/6) E^(a4[H x4]), 1, s^(1/6) E^(-a4[H x4]), s^(1/6) E^(-a4[H x4]), s^(1/6) E^(-a4[H x4])}]; (* e_mu^a, rows mu *)
Print["g==e eta e^T: ",FullSimplify[ev.eta.Transpose[ev]-g,assum]==ConstantArray[0,{8,8}]];
ginv=Inverse[g]; einv=Inverse[ev]; (* einv[[a,mu]] = e_a^mu *)
Gam=FullSimplify[Table[(1/2) Sum[ginv[[r,s1]] (D[g[[s1,m]],X[[n]]]+D[g[[s1,n]],X[[m]]]-D[g[[m,n]],X[[s1]]]),{s1,8}],{r,8},{m,8},{n,8}],assum];
(* omega_mu^a_b = e_b^nu (Gamma^rho_{mu nu} e_rho^a - d_mu e_nu^a) *)
om=FullSimplify[Table[Sum[einv[[b,n]] (Sum[Gam[[r,m,n]] ev[[r,a]],{r,8}]-D[ev[[n,a]],X[[m]]]),{n,8}],{m,8},{a,8},{b,8}],assum];
vp=FullSimplify[Table[D[ev[[n,a]],X[[m]]]-Sum[Gam[[r,m,n]] ev[[r,a]],{r,8}]+Sum[om[[m,a,b]] ev[[n,b]],{b,8}],{m,8},{n,8},{a,8}],assum];
Print["vielbein postulate zero: ",Union[Flatten[vp]]];
omL=Table[Sum[eta[[a,c]] om[[m,c,b]],{c,8}],{m,8},{a,8},{b,8}]; (* omega_{mu ab} *)
Print["omega_{mu ab} antisym: ",Union[Flatten[FullSimplify[omL+Transpose[omL,{1,3,2}],assum]]]];
Print["nonzero lowered components: ",Count[Flatten[omL],x_/;x=!=0]];
OmCorrect=Table[(1/2) Sum[omL[[m,a,b]] S[a-1,b-1],{a,8},{b,8}],{m,8}];
OmNB=Table[(1/2) Sum[om[[m,a,b]] S[a-1,b-1],{a,8},{b,8}],{m,8}];
Tcurv=Table[Sum[einv[[a,m]] T[a-1],{a,8}],{m,8}]; (* T^mu *)
DT[Om_]:=Table[D[Tcurv[[n]],X[[m]]]+Sum[Gam[[n,m,l]] Tcurv[[l]],{l,8}]+Om[[m]].Tcurv[[n]]-Tcurv[[n]].Om[[m]],{m,8},{n,8}];
Print["D_mu T^nu = 0 with CORRECT Omega: ",Union[Flatten[FullSimplify[DT[OmCorrect],assum]]]];
Print["D_mu T^nu = 0 with NOTEBOOK contraction: ",Union[Flatten[FullSimplify[DT[OmNB],assum]]]=={0}];
slash=FullSimplify[Sum[Tcurv[[m]].OmCorrect[[m]],{m,8}],assum];
Print["T^mu Omega_mu (correct) = c0 T^0 + c4 T^4 ?  c0,c4 = ",FullSimplify[{Tr[slash.T[0]]/16, -Tr[slash.T[4]]/16},assum]];
Print["residual: ",FullSimplify[slash-(Tr[slash.T[0]]/16) T[0]-(-Tr[slash.T[4]]/16) T[4],assum]==ConstantArray[0,{16,16}]];
slashNB=FullSimplify[Sum[Tcurv[[m]].OmNB[[m]],{m,8}],assum];
Print["T^mu Omega_mu (notebook contraction) coefficients: ",FullSimplify[{Tr[slashNB.T[0]]/16, -Tr[slashNB.T[4]]/16},assum]];
sq=FullSimplify[Sqrt[Abs[Det[g]]],assum]; Print["sqrt|g| = ",sq];
(* Einstein tensor *)
Ric=FullSimplify[Table[Sum[D[Gam[[r,m,n]],X[[r]]]-D[Gam[[r,m,r]],X[[n]]]+Sum[Gam[[r,r,l]] Gam[[l,m,n]]-Gam[[r,n,l]] Gam[[l,m,r]],{l,8}],{r,8}],{m,8},{n,8}],assum];
R=FullSimplify[Sum[ginv[[m,n]] Ric[[m,n]],{m,8},{n,8}],assum];
Print["Ricci scalar = ",R];
Gmix=FullSimplify[ginv.Ric - (R/2) ID8,assum];
Print["G^mu_nu diagonal = ",FullSimplify[Diagonal[Gmix],assum]];
Print["G^mu_nu offdiag = ",Union[Flatten[FullSimplify[Gmix-DiagonalMatrix[Diagonal[Gmix]],assum]]]];
