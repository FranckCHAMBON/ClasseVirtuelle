"""
Prologin: Entrainement 2003
Qualification : 3 - Les trois nombres
https://prologin.org/train/2003/qualification/les_trois_nombres
"""

def verifie(nb_1, nb_2, nb_3):
    """ Renvoie un nombre si la somme des deux autres sont égal. Sinon cela renvoie 0.
    >>> verifie(18, 42, 24)
    42
    >>> verifie(11, 37, 18)
    0
    """
    if nb_1 + nb_2 == nb_3:
        return nb_3
    elif nb_1 + nb_3 == nb_2:
        return nb_2
    elif nb_2 + nb_3 == nb_1:
        return nb_1
    else:
        return 0

# Test
import doctest
doctest.testmod()

# Entrées
nb_1, nb_2, nb_3 = map(int, input().split())

# Sortie
print(verifie(nb_1, nb_2, nb_3))