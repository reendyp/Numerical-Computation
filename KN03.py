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

# Literatur :https://www.bing.com/ck/a?!&&p=f2504bb91e405cd6JmltdHM9MTcxMTQxMTIwMCZpZ3VpZD0yZWNmYmFmMC03MTcyLTY5NmEtMGRjOC1hYjYzNzAyNDY4ZTkmaW5zaWQ9NTI0OA&ptn=3&ver=2&hsh=3&fclid=2ecfbaf0-7172-696a-0dc8-ab63702468e9&psq=norm+pada+jacobi&u=a1aHR0cHM6Ly9vanMudW5tLmFjLmlkL2ptYXRoY29zL2FydGljbGUvZG93bmxvYWQvMTI0NDcvNzM1MA&ntb=1
# Literatur KN04 : https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://journal.unnes.ac.id/sju/ujm/article/view/30091/17361&ved=2ahUKEwibg7CHkKWFAxX0TWwGHXkrDMIQFnoECDcQAQ&usg=AOvVaw1sA_IhRUpOuNsG5hlVR7t4
