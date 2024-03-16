import math as mt
import numpy as np

approx = 0
n = 0
x = np.sin(np.radians(90))


while True:
    approx += (((-1)**n)*(x**(2*n+1))/mt.factorial(2*n+1))
    error = abs(approx - x)
    n += 1
    if n == 8:
        break
    print(f"approx = {approx} \t error = {error}")                  

