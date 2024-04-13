# SOR METHODS

import numpy as np
# buat matriks persamaan linear [x,y]
A = np.array([
            [1.0,3.0,-1.0,0.3],
            [0.0,1.0,-9.8,0.0],
            [3.0,-4.0,2.0,0.0],
            [1.4,0.0,-2.4,0.0]
            ])
# matriks hasil persamaan linear
y = np.array([28,12,-2,3])

# wadah kosong
x = np.array([0.0,0.0,0.0,0.0])

# inisiasi awal
e = 1
i = 0
w = 0.8
while e>1e-6:
    solutionAx = [] # wadah solusi x1 dan x2
    n = len(x)
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
    i+=1
print(f"Hasil akar-akar = {x} iterasi - {i}")
