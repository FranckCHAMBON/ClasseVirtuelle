from math import exp

def f(x):
    return (x-2) * exp(x)

def g(x):
    return (2 * (x-1) * (x+3)) / 3 * exp(x/2)

def balayage(x, y):
    for i in range(x, y):
        diff = f(i) - g(i)
        print("Avec i =",i , "la différence est:", diff)

#balayage(1, 11)
# On sait qu'il y a une solution entre 3 et 4

def dichotomie(x, y):
    # au départ f(x) < g(x), avec x = 3
    # à la fin f(y) > g(y), avec y = 4
    diff_x_y = 1
    while diff_x_y > 0.000000000001:
        assert x < y
        z = (x + y) / 2
        if f(z) < g(z):
            x = z
        if f(z) > g(z):
            y = z
        if f(z) == g(z):
            return z
        diff_x_y = y - x
        assert x < y
    return z

x = dichotomie(3, 4)

print("Avec x =", x, "on a :")
print("f(x) =", f(x))
print("g(x) =", g(x))
print("f(x) - g(x) =", f(x) - g(x))
