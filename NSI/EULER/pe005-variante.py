from math import gcd

def ppcm(n, m):
    "Retourne le plus petit commun multiple de n et m"
    return n // gcd(n, m) * m # version efficace
    # return n * m // gcd(n, m) # version lente

def pe005(n=20):
    "Variante de solution au problème PE005"
    ans = 1
    for x in range(2, n+1):
        ans = ppcm(ans, x) # un exemple de programmation dynamique
    return ans

assert pe005(10) == 2520, "Le test avec 10 a échoué"

print(pe005(100))

