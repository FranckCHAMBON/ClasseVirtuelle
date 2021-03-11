"""
Prologin: Qualification 2003
Exercice: 3 - Les trois nombres
https://prologin.org/train/2003/qualification/les_trois_nombres
"""

def trois_nb (nb1 : int, nb2 : int, nb3 : int) -> int :
    """ Si l'un des entier est égal à la somme des deux autres, 
    la fonction renvoie cet entier, 0 sinon.

    >>> nb1, nb2, nb3 = 18, 42, 24
    >>> trois_nb(nb1, nb2, nb3)
    42

    >>> nb1, nb2, nb3 = 11, 37, 18
    >>> trois_nb(nb1, nb2, nb3)
    0

    """
    sortie = 0
    somme1 = nb2 + nb3
    somme2 = nb1 + nb3
    somme3 = nb1 + nb2
    if somme1 == nb1 :
        sortie = nb1
    if somme2 == nb2 :
        sortie = nb2
    if somme3 == nb3 :
        sortie = nb3
    return sortie

# tests
import doctest
doctest.testmod()

# Entrée
entiers = list(map(int, input().split()))
nb1 = entiers[0]
nb2 = entiers[1]
nb3 = entiers[2]

# Sortie
print(trois_nb(nb1, nb2, nb3))