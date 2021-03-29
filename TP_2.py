from math import sin, cos, exp, log, acos, atan

def PointFixe (g, x0, epsilon, Nitermax) :
    xold = x0
    xnew = g0 (xold)
    n = 1
    while abs (xnew - xold) > epsilon and n < Nitermax :
        xold = xnew
        xnew = g(xold)
        n = n + 1
    return xnew, n

def g0 (x) :
    x = (1 + sin (x)) / 2
    return x

epsilon = 1e-10
Nitermax = 500

def g1 (x) :
    x = (9 - 3*x)**(1/4)
    return x

alpha1 = PointFixe (g1, 1, epsilon, Nitermax)
print (alpha1)

def g11 (x) :
    x = -(9 - 3*x)**(1/4)
    return x

alpha11 = PointFixe (g11, -2, epsilon, Nitermax)
print(alpha11)

def g2 (x) :
    x = acos ((x + 2)/3)
    return x

alpha2 = PointFixe (g2, -5, epsilon, Nitermax)
print ("alpha 2", alpha2)
def g22 (x) :
    x = -acos((-x+2)/3)
    return x

alpha22 = PointFixe (g22, -1, epsilon, Nitermax)
print (alpha22)


def g3 (x) :
    x = log(7/x)
    return x

alpha3 = PointFixe (g3, 1, epsilon, Nitermax)
print (alpha3)

def g4 (x) :
    x = exp(x) - 10
    return x

alpha4 = PointFixe (g4, -100, epsilon, Nitermax)
print (alpha4)

def g44 (x) :
    x = log(x + 10)
    return x

alpha44 = PointFixe (g44, 2, epsilon, Nitermax)
print (alpha44)

def g5 (x) :
    x = atan((x+5) / 2)
    return x

alpha5 = PointFixe (g5, 1.2, epsilon, Nitermax)
print ("alpha 5", alpha5)

def g6 (x) :
    x = log (x**2 + 3)
    return x

alpha6 = PointFixe (g6, 1.8, epsilon, Nitermax)
print (alpha6)

def g7 (x) :
    x = (7 - 4*log(x))/3
    return x

alpha7 = PointFixe (g7, 1.48, epsilon, Nitermax)
print (alpha7)

def g8 (x) :
    x = ((2*x**2 - 4*x + 17))**(1/4)
    return x

alpha8 = PointFixe (g8, 2, epsilon, Nitermax)
print (alpha8)

def g88 (x) :
    x = - ((2*x**2 - 4*x + 17))**(1/4)
    return x

alpha88 = PointFixe (g88, -2.8, epsilon, Nitermax)
print (alpha88)

def g9 (x) :
    x = log (2 * sin(x) + 7)
    return x

alpha9 = PointFixe (g9, 2, epsilon, Nitermax)
print (alpha9)

def g10 (x) :
    x = log (10 / (log(x**2 + 4)))
    return x

alpha10 = PointFixe (g10, 1.4, epsilon, Nitermax)
print (alpha10)