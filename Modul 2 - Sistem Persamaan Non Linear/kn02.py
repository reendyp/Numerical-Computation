'''from math import exp
def fixPoint(a,f,e = 0.001):
    #error = 1
    n = 0
    while abs(error) > e:
        xNew = f(a)
        print(f"nilai x = {a:.4f} \t fx = {f(a):.4f} \t error = {abs(error):.5f}")
        error = xNew - a
        a = xNew
        n += 1
        if abs(error)<e:
            break
        print(f"Nilai fix x = {a} \t error = {abs(error)}")
        return a
        
f = lambda x: exp(-x)
a = float(input("Masukkan x tebakan : "))
xResult = fixPoint(a,f)
print(xResult)
'''

#Percobaan 1  Bisection Methods

a = float(input("Masukkan batas awal  : "))
b = float(input("Masukkan batas akhir : "))
e = 1.0
print(f"| Hasil Akprosimasi | \t Error \t| Iterasi |")
def bisc(a,b,f,e,n):
    xA = a
    xB = b
    e = 1.0
    if f(xA)*f(xB)>0:
        while True:
            xA = float(input("Masukkan batas awal kembali  : "))
            xB = float(input("Masukkan batas akhir kembali : "))
            if f(xA)*f(xB)<0:
                break
        return None
    n = 0
    
    while e > 0.0001:
        xMid = (xA+xB)*0.5
        n += 1
        e = xB - xMid
        if f(xA)*f(xB)<0:
            xB = xMid
        else:
            xA = xMid
        print(f"\t {xMid:.5f}\t {e:.5f}\t {n}")
    print(f"Hasil akar aproks = {xMid:.5f} \t Iterasi ke-{n} \t {e:.5f} \t interval {a} <=x<= {b}")
    return xMid
        

f = lambda x: x**2-3*x-10
x1 = bisc(a,b,f,e,0)
#print(f"x1 = {x1} \t iterasi ke-{n[:-1]}")
