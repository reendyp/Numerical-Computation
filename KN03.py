# Jacobi Methods
import numpy as np
# buat matriks persamaan linear [x,y]
A = np.array([[2.0,3.0],
             [1.0,-6.0]])
# matriks hasil dari persamaan linear
Y = np.array([5.0,9.0])

#matriks kosong untuk menempatkan hasil solusi
x = np.array([0.0,0.0])
# iterasi dimulai dari 0
i = 0 
# pengondisian true pada while
e = 1

while e > 1e-6:

    solAB = [] # wadah solusi untuk variabel x dan y pada persamaan linear
    n = len(x)
    for i in range(n):
        sigma = 0 
        for j in range(0,n):
            if j != i:
                sigma += A[i][j]*x[j]
        xn = (Y[i]-sigma)/A[i][j]
        solAB.append(xn)
    e = abs(max(x)-max(solAB))
    x = np.array(solAB)

    i += 1
print(f"akar persamaan {x} \t iterasi - {i}")

# Gauss-Seidel Methods
import numpy as np
# buat matriks persamaan linear [x,y]
A = np.array([[2.0,3.0],
             [1.0,-6.0]])
# matriks hasil persamaan linear
y = np.array([5.0,9.0])

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

# wadah kosong
x = np.array([0.0,0.0])

# inisiasi awal
e = 1
i = 0

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
