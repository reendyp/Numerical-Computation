import numpy as np

# Flowchart

# Buat array berdasarkan persamaan yang akan dicari solusinya
A = np.array([[80,-50,-30,0],
            [-50,100,-10,-25],
            [30,-10,65,-20],
            [0,-25,-20,100]],float)
# Array hasil dari persamaan sebelumnya
Y = np.array([120,0,0,0],float)
# Array untuk hasil x1,x2,x3
x = np.array([0,0,0,0],float)

# inisiasi awal
itr = 0
e = 1

while e > 0.000001:
    solveA = []
    n = len(x)
    for i in range(n):
        sigma = 0
        for j in range(0,n):
            if j != i:
                sigma += A[i][j]*x[j]
        xNow = (Y[i]-sigma)/A[i][i]
        solveA.append(xNow) # diappend = biar array solveA kosong, dan bisa di input lagi dengan nilai baru
    e = abs(max(x)-max(solveA))
    x = np.array(solveA)
    itr += 1
    print(f"Matriks solusi I1,I2,I3,I4 = {x} \t iterasi = {itr}")
print("Perhitungan dengan Metode Jacobi")
print(f"Solusi I1 = {x[0]} I2 = {x[1]}; I3 = {x[2]}; I4 = {x[3]};")
