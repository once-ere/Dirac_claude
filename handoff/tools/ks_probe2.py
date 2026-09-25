import numpy as np, json
np.set_printoptions(linewidth=220, precision=4, suppress=True)
fx=json.load(open(r'C:/Users/nsh/Developer/github/Dirac_claude/artifacts/dirac16complex/arbitrary-field/algebra-fixture.json'))
g=[np.array(m,dtype=float) for m in fx['gamma']]; C=np.array(fx['C'],dtype=float)
B=-1j*C@g[4]; g8=np.array(fx['chirality'],dtype=float)
A0=g[0]; A1=g[0]@g[1]; A4=g[0]@g[4]
# y-ODE: chi' = [M A0 - i k A1 + i E A4] chi  (from gamma^0 chi' + i k gamma^1 chi - i E gamma^4 chi = M chi)
print("A0 sym:",np.allclose(A0,A0.T)," A1 antisym:",np.allclose(A1,-A1.T)," A4 antisym:",np.allclose(A4,-A4.T))
print("A0^2=",np.allclose(A0@A0,np.eye(16)),"A1^2=",np.allclose(A1@A1,-np.eye(16)),"A4^2=",np.allclose(A4@A4,np.eye(16)))
print("A0A1+A1A0=0:",np.allclose(A0@A1+A1@A0,0),"A0A4+A4A0=0:",np.allclose(A0@A4+A4@A0,0),"A1A4+A4A1=0:",np.allclose(A1@A4+A4@A1,0))
# Casimir-like commuting operators: J = A0 A1 A4 commutes with all three?
J=A0@A1@A4
print("J commutes with A0,A1,A4:",all(np.allclose(J@X,X@J) for X in (A0,A1,A4)), " J^2=",np.allclose(J@J,np.eye(16)), np.allclose(J@J,-np.eye(16)))
# other commuting operators: g8 (chirality) and e.g. g2g3, g5g6 ...
cands={'g8':g8,'g2g3':g[2]@g[3],'g5g6':g[5]@g[6],'g6g7':g[6]@g[7],'g2g3g5g6':g[2]@g[3]@g[5]@g[6],'C':C,'B':B}
for n,X in cands.items():
    print(n,"commutes with A0,A1,A4:",all(np.allclose(X@Y,Y@X) for Y in (A0,A1,A4)))
# simultaneous eigenbasis of J, g2g3, g5g6 (mutually commuting?)
K1=g[2]@g[3]; K2=g[5]@g[6]
print("J,K1,K2 mutually commute:",np.allclose(J@K1,K1@J),np.allclose(J@K2,K2@J),np.allclose(K1@K2,K2@K1))
# block-diagonalize: eigen-decompose the Hermitian combination
Hc=1.0*(1j*J if np.allclose(J.T,-J) else J) + 2.0*(1j*K1 if np.allclose(K1.T,-K1) else K1)+4.0*(1j*K2 if np.allclose(K2.T,-K2) else K2)
Hc=(Hc+Hc.conj().T)/2
w,V=np.linalg.eigh(Hc); print("labels:",np.round(w,3))
for X,n in ((A0,'A0'),(A1,'A1'),(A4,'A4'),(C,'C'),(B,'B'),(g8,'g8')):
    Y=V.conj().T@X@V
    # block sizes: check off-block zeros for 2x2 blocks
    ok2=all(np.allclose(Y[i:i+2,j:j+2],0) for i in range(0,16,2) for j in range(0,16,2) if i!=j)
    print(n,"block-diag in 2x2 blocks:",ok2)
Y0=V.conj().T@A0@V; Y1=V.conj().T@A1@V; Y4=V.conj().T@A4@V
print("first 2x2 blocks: A0\n",Y0[:2,:2],"\nA1\n",Y1[:2,:2],"\nA4\n",Y4[:2,:2])
print("distinct A0 blocks:",{tuple(np.round(Y0[i:i+2,i:i+2].flatten(),3)) for i in range(0,16,2)})
print("distinct A1 blocks:",{tuple(np.round(Y1[i:i+2,i:i+2].flatten(),3)) for i in range(0,16,2)})
print("distinct A4 blocks:",{tuple(np.round(Y4[i:i+2,i:i+2].flatten(),3)) for i in range(0,16,2)})
YB=V.conj().T@B@V; YC=V.conj().T@C@V
print("B in this basis block-diag 2x2:",all(np.allclose(YB[i:i+2,j:j+2],0) for i in range(0,16,2) for j in range(0,16,2) if i!=j))
print("C in this basis block-diag 2x2:",all(np.allclose(YC[i:i+2,j:j+2],0) for i in range(0,16,2) for j in range(0,16,2) if i!=j))
print("C couples blocks (nonzero 2x2 off-blocks):",[(i//2,j//2) for i in range(0,16,2) for j in range(0,16,2) if i<j and not np.allclose(YC[i:i+2,j:j+2],0)][:12])
