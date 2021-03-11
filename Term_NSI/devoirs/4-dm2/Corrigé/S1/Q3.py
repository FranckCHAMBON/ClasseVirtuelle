"""
Prologin: Qualification 2003
Exercice 3 - Les trois nombres
https://prologin.org/train/2003/qualification/les_trois_nombres
"""

# 0- Coeur du programme

def détermine_somme(nombres: list) -> int:
    """ Détermine si l'un des nombres de la liste est égal à la somme des 2 autres.
    Si oui, renvboie ce nombre, sinon revoie 0.
    >>> détermine_somme([18,42,24])
    42
    >>> détermine_somme([11,37,18])
    0
    """

    combinaisons = [(0,1,2),(1,0,2),(2,0,1)]    # Correspond aux identifiants des nombres
    for x, y, z in combinaisons:                # Chaque nombre est une fois la somme et 2 fois l'un des nombres additionné
        somme = nombres[y] + nombres[z]
        if nombres[x] == somme:
            return somme                        # Si un nombre est la somme des 2 autres alors on renvoie la somme
    return 0                                    # Si aucun n'est la somme, on renvoie 0

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture des entrées

nombres = list(map(int,input().split()))

# 3- Appel de la fonction / Sortie

print(détermine_somme(nombres))