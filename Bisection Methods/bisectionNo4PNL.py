a = float(input("Masukkan batas awal perkiraan: "))
b = float(input("Masukkan batas awal perkiraan: "))
H = 0.075
h0 = 0.6
Q = 1.2
g = 9.81
z = 1.8
def bisectionMethod(a,b,f):
    xA = a
    xB = b
    if f(a)*f(b)>0:
        while True:
            print("Maaf interval terlalu besar terkecil sehingga tidak dapat dilakukan perhitungan")
            
            xA = float(input("Masukkan interval awal baru: "))
            xB = float(input("Masukkan interval akhir baru: "))
            
            if f(xA)*f(xB)<0: # Syarat terpenuhi lanjut ke program titik tengah
                break
        return None
    
    for i in range(0,200):
        c = (xA+xB)*0.5
        print(f"Nilai h adalah {abs(f(c))}")
        if abs(b-a)<(10**-7):
            return c
        
        if f(xA)*f(c)<0:
            xB = c
        else:
            xA = c
        return c

f = lambda h: (h**3+(H-h0-(Q**2)/(2*g*(z**2)*(h0**2)))*(h**2) + (Q**2)/(2*g*(z**2)))# =b(h)=h^(3)-0.5879 h^(2)+0.02265
#f = lambda h: h**3-(0.5879)*(h**2)+0.02265
x = float((bisectionMethod(a,b,f)))
print(f'tinggi h pertama = {abs(x)}') # masih miss beberapa koma