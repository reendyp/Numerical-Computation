# SOR METHODS
import numpy as np
# buat matriks persamaan linear [x,y]
A = np.array([[2.0,3.0],
            [1.0,-6.0]])
# matriks hasil persamaan linear
y = np.array([5.0,9.0])

# wadah kosong
x = np.array([0.0,0.0])

# inisiasi awal
e = 1
i = 0
w = 0.8
while e>1e-6:
    n = len(x)
    solutionAx = []

    for i in range(n):
        sigma = 0
        for j in range(0,i):
            sigma += A[i][j]*solutionAx[j]
        for j in range(i+1,n):
            sigma += A[i][j]*x[j]
        xn = (1-w)*x[i]+(w/A[i][i])*(y[i]-sigma)
        solutionAx.append(xn)
    e = abs(max(x)-max(solutionAx))
    x = np.array(solutionAx)
    i += 1
print(f"Nilai solusi x1 dan x2 menggunakan Metode Seidel = {x} \t iterasi = {i}")
