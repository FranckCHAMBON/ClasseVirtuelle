def pe005(n=20):
    "Solution au problème PE005"
    
    nb_premiers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] #... voir ensuite
    
    def valuation(x, p):
        """Donne l'exposant e de p^e dans la
        décompsition en facteur premier de x"""
        e = 0
        while x % p == 0:
            x = x // p
            e = e + 1
        return e
    assert valuation(2, 2) == 1
    assert valuation(4, 2) == 2
    assert valuation(8, 2) == 3
    assert valuation(12, 2) == 2
    assert valuation(250, 5) == 3
    assert valuation(13, 5) == 0
    
    def valuation_réponse(n, p):
        ans = 0
        for x in range(1, n+1):
            e = valuation(x, p)
            if e > ans:
                ans = e
        return ans
    assert valuation_réponse(10, 2) == 3
    assert valuation_réponse(10, 3) == 2
    
    ans = 1
    for p in nb_premiers:
        e = valuation_réponse(n, p)
        ans = ans * p**e
    return ans

assert pe005(10) == 2520, "Le test avec 10 a échoué"

print(pe005(100))
