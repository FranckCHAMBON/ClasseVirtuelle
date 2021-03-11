"""
Prologin: Entraînement 2003
Exercice: 2 - Escalier
https://prologin.org/train/2003/semifinal/escalier
"""

def triangle(nombre_marche):
    """ Cette fonction prend en paramètre un entier positif et elle affiche un escalier, rempli du caractère X.

    >>> triangle(4)
    X
    XX
    XXX
    XXXX

    """
    for i in range(1,nombre_marche+1,1):
        print(i*"X")

# tests
import doctest
doctest.testmod()

# Entrée
nombre_marche = int(input())

# Sortie
triangle(nombre_marche)
