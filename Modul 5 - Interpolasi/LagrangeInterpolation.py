import numpy as np
import matplotlib.pyplot as plt
# Data
#coba bikin data input from user
x = np.array([1950.0,1960.0,1970.0,1980.0,1990.0,2000.0])
y = np.array([34704.0,69168.0,97115.0,148442.0,211707.0,264002.0])

degree = int(input("Masukkan tingkat derajat: "))
xx = float(input("Input tahun yang akan diprediksi: "))
def LagrangeInterpolation(x,y,xx):
    totalFx = 0
    n = degree
    for i in range(0,n+1):
        valueOfFx = y[i]
        for j in range(0,n+1):
            if j != i:
                valueOfFx *= ((xx-x[j])/(x[i]-x[j]))
        totalFx += valueOfFx
    return totalFx
callBack = LagrangeInterpolation(x,y,xx)
print(f"Perkiraan jumlah penduduk pada tahun {xx} sebesar = {callBack}")

plt.ylabel("Jumlah Penduduk")  
plt.xlabel("Tahun")
plt.title("Data Penduduk")            
plt.plot(x,y)
plt.show()