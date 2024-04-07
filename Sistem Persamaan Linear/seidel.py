# SOR METHODS

import numpy as np
# buat matriks persamaan linear [x,y]
A = np.array([
            [20,-10,0,0,0],
            [-10,20,-10,0,0],
            [0,-10,15,-5,0],
            [0,0,-5,10,-5],
            [0,0,0,-5,5],
            ],float)
# matriks hasil persamaan linear
y = np.array([100,50,100,50,100],float)

# wadah kosong
x = np.array([0.0,0.0,0.0,0.0,0.0])

# inisiasi awal
e = 1
itr = 0

while e>1e-6:
    solutionAx = [] # wadah solusi x1 dan x2
    n = len(x)
    itr+=1
    for i in range(n):
        sigma = 0
        for j in range(0,i):
            sigma += A[i][j]*solutionAx[j]
        for j in range(i+1,n):
            sigma += A[i][j]*x[j]
        xn = (y[i]-sigma)/A[i][i]
        solutionAx.append(xn)
    e = abs(max(x)-max(solutionAx))    
    x = np.array(solutionAx)
    print(f"Hasil akar-akar = {x} iterasi - {itr} e = {e:.3f}")
