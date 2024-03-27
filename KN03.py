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
            if j != 1:
                sigma += A[i][j]*x[j]
        xn = (Y[i]-sigma)/A[i][j]
        solAB.append(xn)
    e = abs(max(x)-max(solAB))
    x = np.array(solAB)

    i += 1
print(f"akar persamaan {x} \t iterasi - {i}")
