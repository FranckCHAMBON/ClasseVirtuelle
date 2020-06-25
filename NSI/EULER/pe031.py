UK_coins = [1, 2, 5, 10, 20, 50, 100, 200]

def pe031(pièces=UK_coins, valeur=200):
    """
    Retourne le nombre de façons de rendre "valeur"
    en utilisant autants de "pièces" que l'on veut,
    chacune autant de fois que l'on veut.
    >>> pe031([1, 2, 5], 10)
    10
    """
    
    nb_façons = [1, 1, 2, 2, 3, 4] #, (???)]
    # à reflechir
    

assert pe031([1, 2, 5], 10) == 10

print(pe031())


# notre petit test
nos_pièces = [1, 2, 5]
valeur = [10]
façons = [
    "5+5",
    "5+2+2+1",
    "5+2+1+1+1",
    "5+1+1+1+1+1",
    "2+2+2+2+2",
    "2+2+2+2+1+1",
    "2+2+2+1+1+1+1",
    "2+2+1+1+1+1+1+1",
    "2+1+1+1+1+1+1+1+1",
    "1+1+1+1+1+1+1+1+1+1",
    ]
assert len(façons) == 10