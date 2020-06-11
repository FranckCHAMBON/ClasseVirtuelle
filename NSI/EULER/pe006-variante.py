def pe006(n=100):
    """Solution au problème PE006
    S_1 = 1 + 2 + 3 + ... + n
    S_2 = 1² + 2² + 3² + ... + n²
    Calculer (S_1)² - S_2
    Complexité : ?????
    """
    S_1 = n * (n+1) // 2 #sum(i for i in range(n+1))
    
    S_2 = n * (n+1) * (2*n+1) // 6 #sum(i*i for i in range(n+1))
    
    return S_1 * S_1  -  S_2

assert pe006(10) == 2640, "Le test avec 10 a échoué"

print(pe006())
