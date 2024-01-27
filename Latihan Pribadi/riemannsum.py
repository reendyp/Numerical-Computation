import math as m
import os
os.system("cls")

# ini merupakan kalkulator sederhana untuk menghitung integral riemann. Ada 3 metode yaitu riemann kanan, kiri dan tengah.

# f_x = f(x) yang dapat anda ubah
# a,b = batas bawah, batas atas
# n = banyaknya partisi
# partition = subinterval = delta x = (b-a)/n

# prinsip dari kalkulator ini adalah menghitung f(x_i) sebagai tinggi dan partition sebagai alas, sehingga didapat zigma f(x_i)*deltaX = hasil riemann sum

# dapat disadari bahwa zigma f(x_i)*deltaX adalah luas persegi panjang 


def left_riemann(f_x,a,b,n):
    partition = (b-a)/n
    total = 0
    y = 0
    for i in range(1,n+1):
        x = a + partition*(i-1)
        #print(x,end=" ")
        y = f_x(x)*partition
        #print(y,end="\n")
        #print(y, end="\n")
        total += y
    return total

f_x =lambda x: m.tan(x)
hasil = left_riemann(f_x,0,1,10)
print(f"hasil left riemann sum dari x^3+1 = {hasil:.4f}")

def right_riemann(f_x,a,b,n):
    partition = (b-a)/n
    total = 0
    y = 0
    for i in range(1,n+1):
        x = a + partition*(i)
        #print(x,end=" ")
        y = f_x(x)*partition
        #print(y,end="\n")
        #print(y, end="\n")
        total += y
    return total

hasil = right_riemann(f_x,0,1,10)
print(f"hasil right riemann sum dari x^3+1 = {hasil:.4f}")

def mid_riemann(f_x,a,b,n):
    partition = (b-a)/n
    total = 0
    y = 0
    x = 0
    for i in range(1,n+1):
        x = a+partition*(i-1)
        x_i = x+partition/2
        #print(x_i,end=" ")
        y = f_x(x_i)*partition
        #print(y,end="\n")
        #print(y, end="\n")
        total += y
    return total

#f_x = lambda x: (x**3)+1
hasil = mid_riemann(f_x,0,1,10)
print(f"hasil midpoint riemann dari x^3+1 = {hasil:.4f}")
