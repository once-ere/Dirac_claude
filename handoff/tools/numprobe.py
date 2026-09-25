import numpy as np, itertools
I4=np.eye(4); I8=np.eye(8)
def Qa(h,p,q):
    # Signature of permutation {h,p,q,4} (1-based values)
    lst=[h,p,q,4]
    if len(set(lst))<4: return 0
    s=1; l=lst[:]
    for i in range(4):
        for j in range(i+1,4):
            if l[i]>l[j]: s=-s
    return s
def Qb(h,p,q): return I4[p-1,3]*I4[q-1,h-1]-I4[p-1,h-1]*I4[q-1,3]
s4=lambda h: np.array([[Qa(h,p,q)-Qb(h,p,q) for q in range(1,5)] for p in range(1,5)])
t4=lambda h: np.array([[Qa(h,p,q)+Qb(h,p,q) for q in range(1,5)] for p in range(1,5)])
Z=np.zeros((4,4))
tau={0:I8}
for h in (1,2,3):
    tau[7-h]=np.block([[Z,t4(h)],[-t4(h),Z]]); tau[h]=np.block([[Z,s4(h)],[s4(h),Z]])
tau[7]=tau[1]@tau[2]@tau[3]@tau[4]@tau[5]@tau[6]
sig=np.block([[Z,I4],[I4,Z]])
taub={0:I8}; [taub.__setitem__(A,sig@tau[A].T@sig) for A in range(1,8)]
Z8=np.zeros((8,8))
g=[np.block([[Z8,taub[a]],[tau[a],Z8]]) for a in range(8)]
eta=np.diag([1,1,1,1,-1,-1,-1,-1.])
assert all(np.allclose(g[a]@g[b]+g[b]@g[a],2*eta[a,b]*np.eye(16)) for a in range(8) for b in range(8))
C=g[0]@g[1]@g[2]@g[3]; B=-1j*C@g[4]
m=1.0
def h(k):  # k dict j->k_j (flat), j != 4
    return -1j*m*g[4] - g[4]@sum((k[j]*g[j] for j in k), np.zeros((16,16)))
for k in [{1:0.3,2:-0.7,0:0.2},{5:0.4},{1:0.5,6:0.2}]:
    H=h(k); herm=np.allclose(H,H.conj().T); ev=np.linalg.eigvals(H)
    print("k",k,"Hermitian",herm,"eig(sorted real/imag)",np.round(sorted(ev,key=lambda z:(z.real,z.imag)),6)[[0,7,8,15]], "[h,B]=0",np.allclose(H@B,B@H))
H0=h({}); w,v=np.linalg.eigh(H0); up=v[:,w>0]
print("rest: positive-energy dim",up.shape[1])
s=[ (up[:,i].conj()@(-1j*g[4])@up[:,i]).real for i in range(8)]
uC=[ (up[:,i].conj()@C@up[:,i]) for i in range(8)]
print("scalar density s(u) on rest eigvecs", np.round(s,12)); print("u^dag C u on rest eigvecs", np.round(uC,12))
# B signature on positive-energy rest space
Bp=up.conj().T@B@up; print("B|pos-energy rest eigenvalues", np.round(np.linalg.eigvalsh(Bp),10))
# EXP-3 closed forms
for w0 in (-0.861,-0.764):
    x0=w0/(1-w0); dwda=-3*x0/(1+x0)**2
    print(f"w0={w0}: x0={x0:.6f}  tangent wa={-dwda:.4f}  rho=0 at a={abs(x0)**(1/3):.4f} (z={abs(x0)**(-1/3)-1:.4f})  w=-1 at a={(2*abs(x0))**(1/3):.4f} (z={(2*abs(x0))**(-1/3)-1:.4f})")
