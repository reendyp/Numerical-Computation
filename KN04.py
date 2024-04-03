# Metode Power

import numpy as np
# Deklarasi matriks percobaan
# Metode pangkat  = a*x dengan x adalah vektor eigen awal
a = np.array([[4.0,1.0,0.0],
              [0.0,2.0,1.0],
              [0.0,1.0,-1.0]],float)
x = np.array([[1],[1],[1]],float)
e = 1
eV0 = 0

for i in range(5):
    x = np.dot(a,x) # hasilnya vektor eigen, hasil ini akan diambil nilai max nya, kemudian elemen didalamnya akan dibagi dengan nilai maks
    maxX = np.max(x)
    x *= 1/maxX # hasil vektor eigen setelah dibagi dengan nilai maxX
    maxX0 = maxX
    ev0 = maxX
    e = abs(maxX-ev0) # cara nentuin error dari nilai eigen =>> problem
    print(f"vektor eigen = {x} \t eigen value = {maxX} \t error = {e}")
