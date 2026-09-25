import sympy as sp
y,H,a=sp.symbols('y H a4',positive=True)
# one side y<0 : warp W=exp(H y); metric ds^2 = dy^2 - dx4^2 + W^2[e^{2a}(dx1^2+dx2^2+dx3^2) - e^{-2a}(dx5^2+dx6^2+dx7^2)], a4 const
W=sp.exp(H*y)
x=sp.symbols('x0:8'); coords=[y,x[1],x[2],x[3],x[4],x[5],x[6],x[7]]
gdiag=[1,W**2*sp.exp(2*a),W**2*sp.exp(2*a),W**2*sp.exp(2*a),-1,-W**2*sp.exp(-2*a),-W**2*sp.exp(-2*a),-W**2*sp.exp(-2*a)]
g=sp.diag(*gdiag); ginv=g.inv()
n=8
Gam=[[[sum(ginv[r,s]*(sp.diff(g[s,m],coords[nn])+sp.diff(g[s,nn],coords[m])-sp.diff(g[m,nn],coords[s])) for s in range(n))/2 for nn in range(n)] for m in range(n)] for r in range(n)]
Ric=sp.zeros(n)
for m in range(n):
    for nn in range(n):
        Ric[m,nn]=sp.simplify(sum(sp.diff(Gam[r][m][nn],coords[r])-sp.diff(Gam[r][m][r],coords[nn])+sum(Gam[r][r][l]*Gam[l][m][nn]-Gam[r][nn][l]*Gam[l][m][r] for l in range(n)) for r in range(n)))
R=sp.simplify(sum(ginv[m,nn]*Ric[m,nn] for m in range(n) for nn in range(n)))
G=sp.simplify(ginv*Ric - R/2*sp.eye(n))
print("R =",R); print("G^mu_nu diag =",[sp.simplify(G[i,i]) for i in range(n)])
# extrinsic curvature of the y=const hypersurface: K_ij = (1/2) d_y g_ij ; K^i_j = (1/2) g^{ik} d_y g_kj
Kmix=[sp.simplify(ginv[i,i]*sp.diff(g[i,i],y)/2) for i in range(n) if i!=0]
print("K^i_i (y<0 side, outward normal +y):",Kmix)
# Z2 mirror: the y>0 side has W=exp(-H y): K flips sign -> jump [K^i_j] = 2 K^i_j(0^-)... Israel: S_ij = -(1/kappa)([K_ij]-g_ij[K])
Ktr=sum(Kmix)
Sj=[sp.simplify(-(1/sp.Symbol('kappa'))*(2*Kmix[i]-2*Ktr)) for i in range(7)]  # jump = K(0+)-K(0-) = -2K(0-) with sign conventions -> magnitude
print("brane stress S^i_i (up to overall sign convention) :",Sj)
print("proper 7-volume element at y: W^6 =",sp.simplify(W**6))
