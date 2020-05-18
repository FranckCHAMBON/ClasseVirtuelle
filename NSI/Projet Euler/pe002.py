def pe002(limit=4_000_000):
    "Rétourne la solution au problème PE002"
    a, b = 1, 2
    fib = [a]
    while b < limit:
        fib.append(b)
        a, b = b, a+b
    # on a la suite de Fibonacci, ...
    somme = 0
    for fib_n in fib:
        if fib_n % 2 == 0:
            somme = somme + fib_n
    return somme

print(pe002())
