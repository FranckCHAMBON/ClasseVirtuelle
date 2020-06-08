def pe003(n=600851475143):
    "retourne le plus grand facteur premier de n"
    assert n > 1, f"n={n} ne possède pas de facteur premier"
    facteur = []
    p = 2
    while n > 1:
        while n % p == 0:
            n = n // p
            facteur.append(p)
        p = p + 1
    return facteur[-1]


assert pe003(13195) == 29, "Échec au test"
assert pe003(2) == 2, "Échec au test"
assert pe003(3) == 3, "Échec au test"
assert pe003(4) == 2, "Échec au test"
assert pe003(6) == 3, "Échec au test"
assert pe003(49) == 7, "Échec au test"

print(pe003())