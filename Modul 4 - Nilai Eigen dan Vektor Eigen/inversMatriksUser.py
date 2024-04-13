import numpy as np
import copy

# Input matriks dari user
a = np.array([
            [0,0,0],
            [0,0,0],
            [0,0,0]
            ],float)
for i in range(len(a)):
    for j in range(len(a)):
        a[i][j] = float(input(f"Masukkan nilai untuk posisi {i+1},{j+1} = "))
print(f"Matriks input = {a}")

# Determinan matriks kofaktor == ambil baris pertama
def determinant(a):
    det = 0
    for i in range(0,len(a)):
        if i > 0: # menggunakan elemen baris ke-0 atau pertama
            break
        for j in range(0,len(a)):
            if j == 0:
                det += a[i][j]*(a[i+1][j+1]*a[i+2][j+2]-a[i+1][j+2]*a[i+2][j+1])*(-1)**(i+j)
            if j == 1: # i = 0 j = 1
                det += a[i][j]*(a[i+1][j-1]*a[i+2][j+1]-a[i+1][j+1]*a[i+2][j-1])*(-1)**(i+j)
            if j == 2: # i = 0 j = 2
                det += a[i][j]*(a[i+2][j-1]*a[i+2][j-2]-a[i+2][j-2]*a[i+2][j])*(-1)**(i+j)
    return det
detA = determinant(a)

# menentukan konjugasi matriks a
def Conjugate(aC):
    # array kosong sebagai wadah
    aC = np.array([
            [0,0,0],
            [0,0,0],
            [0,0,0]
            ],float)
    for i in range(0,3):
        if i == 0: # menghitung berdasarkan kolom
            for j in range(0,3):
                if j == 0: # i = 0 # kolom ke-0 atau pertama
                    aC[i][j] = (-1)**(i+j)*(a[i+1][j+1]*a[i+2][j+2]-a[i+2][j+1]*a[i+1][j+2]) # a00 = a11a22-a21a12
                    aC[i+1][j] = (-1)**(i+1+j)*(a[i+2][j+2]*a[i][j+1]-a[i+2][j+1]*a[i][j+2]) # a10 = a22a01-a21a02
                    aC[i+2][j] = (-1)**(i+2+j)*(a[i+1][j+2]*a[i][j+1]-a[i+1][j+1]*a[i][j+2]) # a= 20 = a12a01-a11a02
                if j == 1: # kolom ke-1 atau kedua
                    aC[i][j] = (-1)**(i+j)*(a[i+2][j+1]*a[i+1][j-1]-a[i+2][j-1]*a[i+1][j+1]) #a22a10-a20a12
                    aC[i+1][j] = (-1)**(i+1+j)*(a[i+2][j+1]*a[i][j-1]-a[i+2][j-1]*a[i][j+1]) # a22a00-a20a02
                    aC[i+2][j] = (-1)**(i+2+j)*(a[i+1][j+1]*a[i][j-1]-a[i+1][j-1]*a[i][j+1]) # a12a00-a10a02
                if j == 2: # kolom ke-2 atau ketiga
                    aC[i][j] = (-1)**(i+j)*(a[i+2][j-1]*a[i+1][j-2]-a[i+2][j-2]*a[i+1][j-1]) # a21a10-a20a11
                    aC[i+1][j] = (-1)**(i+1+j)*(a[i+2][j-1]*a[i][j-2]-a[i+2][j-2]*a[i][j-1]) # a21a00-a20a01
                    aC[i+2][j] = (-1)**(i+2+j)*(a[i+1][j-1]*a[i][j-2]-a[i+1][j-2]*a[i][j-1]) # a11a00-a10a01
    return aC
aCnew = Conjugate(a)
print(f"Matriks Konjugasi dari {a}={aCnew}")

aCT = copy.deepcopy(aCnew) # melakukan copy setiap elemen yang ada didalam matriks
def transposeConjugate(aT):
    # wadah kosong
    aT = np.array([
            [0,0,0],
            [0,0,0],
            [0,0,0]
            ],float)
    for i in range(len(aT)):
        for j in range(len(aT)):
            aT[i][j] = aCT[j][i] # melakukan proses transpose dari matriks aCT
    return aT
print(f"Matriks Transpose Konjugasi dari {aCT}={transposeConjugate(aCT)}")
matrixTranspose = transposeConjugate(aCT)
def invers():
    invMatrix = matrixTranspose/detA # Melakukan proses invers
    return invMatrix

inversMatrix = invers()
print(f"Hasil invers matriks {a} = {inversMatrix} dengan determinan = {detA}")