"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/qualification/cases_inaccessibles
"""

def plus_petite(l_1: int, chaîne_1: str, l_2: int, chaîne_2: str) -> str:
    """Renvoie la plus petite des deux chaînes.
    En suivant l'ordre lexicographique,
    et sans utiliser la fonction de la bibliothèque interne.

    >>> plus_petite(8, "prologin", 5, "prolo")
    'prolo'

    >>> plus_petite(4, "toto", 4, "titi")
    'titi'

    """
    l = min(l_1, l_2)
    for i in range(l):
        c_1 = chaîne_1[i]
        c_2 = chaîne_2[i]
        if c_1 < c_2:
            return chaîne_1
        if c_2 < c_1:
            return chaîne_2
    if l_1 < l_2:
        return chaîne_1
    if l_2 < l_1:
        return chaîne_2
    # ici on a 
    assert chaîne_1 == chaîne_2, f"Erreur curieuse"
    return chaîne_1

import doctest
doctest.testmod()

l_1 = int(input())
chaîne_1 = input()
assert l_1 == len(chaîne_1), f"Erreur {l_1} ≠ {len(chaîne_1)}"
l_2 = int(input())
chaîne_2 = input()
assert l_2 == len(chaîne_2), f"Erreur {l_2} ≠ {len(chaîne_2)}"

print(plus_petite(l_1, chaîne_1, l_2, chaîne_2))

