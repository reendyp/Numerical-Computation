import numpy as np

a = np.array([
            [3,-0.1,-0.2],
            [0.1,7,-0.3],
            [0.3,-0.2,10]
            ],float)

b = np.array([
            [7.85],
            [-19.3],
            [71.4]
            ],float)    

def LUCrout():
    U = np.array([
        [0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]
        ],float)

    L = np.array([
        [0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]
        ],float)
    d = np.array([[0.0],[0.0],[0.0]],float)
    # Start
    for i in range(len(L)):
        L[i][0]= a[i][0] #2
        for j in range(0,len(U)):
            if i==j: #3
                U[i][j] = 1.0
            else:
                U[0][j] = a[0][j]/L[0][0] #4
    
    for j in range(1,len(L)-1): #5
        for i in range(j,len(L),1):
            LUforLower = 0.0
            for k in range(0,j):
                LUforLower += L[i][k]*U[k][j]
            L[i][j] = a[i][j] - LUforLower
            
        for k in range(j+1, len(a),1):
            LUforUpper = 0.0
            for i in range(0,j):
                LUforUpper += L[j][i]*U[i][k]
            U[j][k] = (a[j][k] - LUforUpper)/L[j][j]
    
    
    for n in range(len(L)):
        sumofLU = 0.0
        for k in range(0,n-1):
            sumofLU += L[n][k]*U[k][n]
        L[n][n] = a[n][n] - sumofLU
        
    for i in range(0,len(d)):
        sumOFLD = 0.0
        for j in range(0,i):
            sumOFLD += L[i][j]*d[j]
        d[i] = (b[i] - sumOFLD)/L[i][i]
    print(f"Matriks Lower = \n{L}")
    print(f"Matriks Upper = \n{U}")
    print(f"Matriks D = \n{d}")
    
LUCrout()
