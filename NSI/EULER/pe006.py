def pe006_brute(n=100):
    """Solution au problème PE006
    S_1 = 1 + 2 + 3 + ... + n
    S_2 = 1² + 2² + 3² + ... + n²
    Calculer (S_1)² - S_2
    Complexité : linéaire, O(n)
    """
    S_1 = 0
    for i in range(n+1):
        S_1 = S_1 + i
    # variante fonctionnelle
    #S_1 = sum(i for i in range(n+1))
    
    S_2 = 0
    for i in range(n+1):
        S_2 = S_2 + i*i
    # variante fonctionnelle
    #S_2 = sum(i*i for i in range(n+1))
    
    return S_1 * S_1  -  S_2

def pe006(n=100):
    """Solution au problème PE006
    S_1 = 1 + 2 + 3 + ... + n
    S_2 = 1² + 2² + 3² + ... + n²
    Calculer (S_1)² - S_2
    Complexité : coût constant O(1), en nombre de multiplications
    """
    S_1 = n * (n+1) // 2 #sum(i for i in range(n+1))
    
    S_2 = n * (n+1) * (2*n+1) // 6 #sum(i*i for i in range(n+1))
    
    return S_1 * S_1  -  S_2


assert pe006(10) == 2640, "Le test avec 10 a échoué"

for n in range(1000):
    assert pe006(n) == pe006_brute(n), f"échec au test pour n = {n}"

print(pe006())

from time import time
t0 = time()
pe006_brute(10**8)
t1 = time()
print(f"le temps pris pour la force brute est {t1-t0}")

t0 = time()
pe006(10**8)
t1 = time()
print(f"le temps pris pour la nouvelle version est {t1-t0}")

