"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/escalier
"""

def affiche_escalier(nb_marches: int) -> None:
    """Affiche un escalier qui a `nb_marches`.

    >>> affiche_escalier(4)
    X
    XX
    XXX
    XXXX
    
    """
    for largeur in range(1, 1 + nb_marches):
        for _ in range(largeur):
            print("X", end="")
        print()

import doctest
doctest.testmod()

nb_marches = int(input())
assert 1 <= nb_marches <= 200, f"Erreur, il y a {nb_marches} marches"
affiche_escalier(nb_marches)
