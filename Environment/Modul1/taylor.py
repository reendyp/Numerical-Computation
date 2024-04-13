# Tentukan faktorial sebagai pembagi
from sympy import *
import math as mt
def factorial(x):
    if x==1:
        return 1
    elif x==0:
        return 1
    else:
        return x*factorial(x-1) 

x = symbols('x')
fx = sin(x)
exactValue = 0.0 # sin(0) =0
# error = nilai eksak - nilai pendekatan (x-a)
a = 0.0000001 
n = 0.0 # n suku,

exactValue1 = fx.subs(x,exactValue)
NumericResult = 0.0

while True:
    NumericResult += (((exactValue-a)**n)/factorial(n))*diff(fx.subs(x,exactValue))
    E = abs(NumericResult-exactValue)
    n += 1
    if n == 8:
        break
    print(f"{NumericResult}")
