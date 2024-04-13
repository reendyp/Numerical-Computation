a = float(input("Masukkan batas awal  : "))
b = float(input("Masukkan batas akhir : "))
e = 1
def bisc(a,b,f,e):
    xA = a
    xB = b
    if f(xA)*f(xB)>0:
        while True:
            xA = float(input("Masukkan batas awal kembali  : "))
            xB = float(input("Masukkan batas akhir kembali : "))
            if f(xA)*f(xB)<0:
                break
        return None
    while abs(e) > 0.000001:
        xMid = (xA+xB)*0.5
        e = f(xMid) - f(xB)
        if f(xA)*f(xMid)<0:
            xB = xMid
        else:
            xA = xMid
    return xMid,e
        

f = lambda x: x**2-5*x+3
x1 = bisc(a,b,f,e)
print(f"x1 = {x1}")