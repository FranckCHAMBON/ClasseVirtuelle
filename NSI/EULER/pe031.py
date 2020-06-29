UK_coins = [1, 2, 5, 10, 20, 50, 100, 200]

def travail(pièces=UK_coins, valeur=200):
    # si on a aucune pièce !!!!
    nb_façons_0 = [1, 0, 0, 0, 0, 0] # ... que des 0 ensuite

    # si on a des pièces de 1
    nb_façons_1 = [1, 1, 1, 1, 1, 1, 1, 1] # ... que des 1

    # si on a des pièces de 1 et de 2
    nb_façons_2 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5] # etc...
    # 4 = 1+1+1+1 = 1+1+2 = 2+2
    # 5 = 2 + (3) # 2 façons (avec au moins une pièce de 2)
    # 5 = 1+1+1+1+1 # 1 façon (sans pièce de 2)

    # si on a des pièces de 1, de 2 et de 5
    nb_façons_3 = [1, 1, 2, 2, 3, 4, 5, 6] # ?
    # 5€ = 5€ + (0€) -> 1 façon
    # 5€ -> il y a 3 façons, (avec des pièces de 1 et 2)
    # d'après ce qui précède.

    # 6€ = 5€ + (1€) -> 1 façon
    # 6€ -> il y a 4 façons avec des pièces de 1 et 2

    # 7€ = 5€ + (2€) -> 2 façons
    # 7€ -> il y a 4 façons avec des pièces de 1 et 2

    #...
    # n€ = 5€ + (n-5)€ -> nb_façons_3[n-5] façons avec au moins une pièce de 5
    # n€ -> il y a nb_façons_2[n] façons avec des pièces de 1 et 2 (sans pièce de 5)
    # n€ -> total = nb_façons_3[n-5] + nb_façons_2[n] façons

    facon_prev = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    # facon_prev[n] le nombre de façon de rendre n€ sans pièce de 5

    # on ajoute la possibilité d'une pièce de p€

    facon_next = [] # à compléter
    # facon_next[n]  le nombre de façon de rendre n€ avec éventuellement pièce de p€
    facon_next = facon_prev[:p]
    for n in range(p, 20):
        facon_next.append(facon_next[n-p] + facon_prev[n])


def pe031(pièces=UK_coins, valeur=200):
    """
    Retourne le nombre de façons de rendre "valeur"
    en utilisant autants de "pièces" que l'on veut,
    chacune autant de fois que l'on veut.
    >>> pe031([1, 2, 5], 10)
    10
    """
    
    l = valeur+1 # nb de valeurs
    facon_prev = [1] + [0]*(l-1) # on a l valeurs

    for p in pièces:
        facon_next = facon_prev[:p]
        for n in range(p, l):
            facon_next.append(facon_next[n-p] + facon_prev[n])
        facon_prev = facon_next

    return facon_next[valeur]



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



