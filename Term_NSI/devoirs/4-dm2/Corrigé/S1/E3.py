"""
Prologin: Entraînement 2003
Exercice 3 - Grand écart
https://prologin.org/train/2003/semifinal/grand_ecart
"""

# 0- Coeur du programme

def plus_grand_écart(nb_éléments: int, liste_éléments: list) -> int:
    """ Renvoie la plus grande différence entre un élément et son successeur dans le tableau.
    >>> plus_grand_écart(2, [0,5])
    5
    >>> plus_grand_écart(10, [4, 2, 3, 5, 10, 6, 4, 9, 1, 3])
    8
    """

    écart_max = 0
    for i in range(nb_éléments-1):
        écart = abs(liste_éléments[i] - liste_éléments[i+1])
        if écart > écart_max:
            écart_max = écart
    return écart_max

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture des entrées

nb_éléments = int(input())
liste_éléments = list(map(int,input().split()))

# 3- Appel de la fonction / Sortie

print(plus_grand_écart(nb_éléments, liste_éléments))