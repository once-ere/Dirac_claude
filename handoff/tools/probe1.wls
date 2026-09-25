(* ---- notebook construction ---- *)
ID4=IdentityMatrix[4]; ID8=IdentityMatrix[8]; ID16=IdentityMatrix[16];
eta=DiagonalMatrix[{1,1,1,1,-1,-1,-1,-1}];
Qa[h_,p_,q_]:=Signature[{h,p,q,4}]; Qb[h_,p_,q_]:=ID4[[p,4]] ID4[[q,h]]-ID4[[p,h]] ID4[[q,4]];
s4[h_]:=Table[Qa[h,p,q]-Qb[h,p,q],{p,4},{q,4}]; t4[h_]:=Table[Qa[h,p,q]+Qb[h,p,q],{p,4},{q,4}];
tau[0]=ID8; Do[tau[7-h]=ArrayFlatten[{{0,t4[h]},{-t4[h],0}}],{h,1,3}]; Do[tau[h]=ArrayFlatten[{{0,s4[h]},{s4[h],0}}],{h,1,3}];
tau[7]=tau[1].tau[2].tau[3].tau[4].tau[5].tau[6];
sig=ArrayFlatten[{{0,ID4},{ID4,0}}];
taub[0]=ID8; Do[taub[A]=sig.Transpose[tau[A]].sig,{A,1,7}];
T[A_]:=T[A]=ArrayFlatten[{{0,taub[A]},{tau[A],0}}];
sig16=ArrayFlatten[{{-sig,0},{0,sig}}];
Print["tau-clifford: ",And@@Flatten@Table[(tau[A].taub[B]+tau[B].taub[A])/2==eta[[A+1,B+1]] ID8,{A,0,7},{B,0,7}]];
Print["T16 clifford: ",And@@Flatten@Table[(T[A].T[B]+T[B].T[A])/2==eta[[A+1,B+1]] ID16,{A,0,7},{B,0,7}]];
Print["sig16==T0T1T2T3: ",sig16==T[0].T[1].T[2].T[3]];
Print["[1] sig16.T antisym: ",Table[sig16.T[A]==-Transpose[sig16.T[A]],{A,0,7}]];
Print["sig16 symmetric: ",sig16==Transpose[sig16], "  sig16^2==1: ",sig16.sig16==ID16];
S[a_,b_]:=(T[a].T[b]-T[b].T[a])/4;
Print["sig16.S antisym all: ",And@@Flatten@Table[sig16.S[a,b]==-Transpose[sig16.S[a,b]],{a,0,7},{b,0,7}]];
T3[c_,a_,b_]:=T[c].S[a,b]+S[a,b].T[c];
Print["sig16.{T,S} symmetric all: ",And@@Flatten@Table[sig16.T3[c,a,b]==Transpose[sig16.T3[c,a,b]],{c,0,7},{a,0,7},{b,0,7}]];
Print["sig16.[T,S] antisym all: ",And@@Flatten@Table[sig16.(T[c].S[a,b]-S[a,b].T[c])==-Transpose[sig16.(T[c].S[a,b]-S[a,b].T[c])],{c,0,7},{a,0,7},{b,0,7}]];
chi=Fold[Dot,ID16,Table[T[A],{A,0,7}]];
Print["chirality block-diag: ",chi==ArrayFlatten[{{chi[[1;;8,1;;8]],0},{0,chi[[9;;16,9;;16]]}}], " diag=",Diagonal[chi]];
(* ---- dirac-main construction ---- *)
P={{0,1},{1,0}};N2={{0,1},{-1,0}};G={{1,0},{0,-1}};I2=IdentityMatrix[2];
kron[l_]:=Fold[KroneckerProduct,First[l],Rest[l]];
gp[k_]:=kron[Join[ConstantArray[G,k-1],{P},ConstantArray[I2,4-k]]]; gm[k_]:=kron[Join[ConstantArray[G,k-1],{N2},ConstantArray[I2,4-k]]];
gam=Join[Table[gp[k],{k,4}],Table[gm[k],{k,4}]];
Cdm=gam[[1]].gam[[2]].gam[[3]].gam[[4]];
Kv=Array[k,{16,16}];
eqs=Flatten[Table[gam[[a+1]].Kv-Kv.T[a],{a,0,7}]];
sol=Solve[Thread[eqs==0],Flatten[Kv]];
Ksol=Kv/.sol[[1]]; free=Variables[Ksol];
Print["intertwiner free params: ",Length[free]];
K1=Ksol/.Thread[free->ConstantArray[1,Length[free]]];
Print["rank K: ",MatrixRank[K1]];
Print["K sig16 K^-1 == C_dm ? ",Simplify[K1.sig16.Inverse[K1]]==Cdm, "   == -C_dm ? ", Simplify[K1.sig16.Inverse[K1]]==-Cdm];
Print["K^T C_dm K proportional to sig16: ", Simplify[Transpose[K1].Cdm.K1]/Transpose[K1].Cdm.K1[[1,1]] ];
(* ---- complex irreducibility ---- *)
Cv=Array[c,{16,16}];
commPin=Solve[Thread[Flatten[Table[T[a].Cv-Cv.T[a],{a,0,7}]]==0],Flatten[Cv]];
Print["Pin commutant dim (over C): ",Length[Variables[Cv/.commPin[[1]]]]];
commSpin=Solve[Thread[Flatten[Table[S[a,b].Cv-Cv.S[a,b],{a,0,6},{b,a+1,7}]]==0],Flatten[Cv]];
Print["Spin commutant dim (over C): ",Length[Variables[Cv/.commSpin[[1]]]]];
(* ---- B = -I sig16 T4 ---- *)
B=-I sig16.T[4];
Print["B hermitian: ",B==ConjugateTranspose[B], " B^2==1: ",B.B==ID16, " eigen: ",Sort[Eigenvalues[B]]];
Print["[sig16,B]==0: ",sig16.B==B.sig16, " Bsig16 == -I T4: ", B.sig16==-I T[4]];
Print["T symmetric (A<4)/antisym(A>=4): ",Table[If[A<4,T[A]==Transpose[T[A]],T[A]==-Transpose[T[A]]],{A,0,7}]];
