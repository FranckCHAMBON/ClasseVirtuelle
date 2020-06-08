def pe001(limit=1000):
    "Solution au problème PE001"
    def est_multiple(n, k):
        "Retourne si n est multiple de k"
        return n % k == 0
    
    return sum(n for n in range(1, limit)
     if est_multiple(n, 3) or est_multiple(n, 5) )


assert pe001(10) == 23, "Le test avec 10 a échoué"

print(pe001())
