a = float(input('Masukkan nilai a= '))
b = float(input('Masukkan nilai b= '))
error = 1

def bsc(a, b, f, error, n):
    while (error)> 0.001:
        c = (a+b)*0.5 
        n += 1
        error = ((b-c))
        if f(a)*f(c)<0:
            b = c
        else:
            a = c
        print('Iterasi ke-%d \t%f\t%f' % (n,c,error))
    print ('Solusi dari persamaan tersebut = %f\nGalat = %f' %(c, error))
    return c

f = lambda x : x**2-3*x-10
x1 = bsc(a, b, f, error, 0) 
