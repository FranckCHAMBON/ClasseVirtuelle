""" 
Prologin: Entraînement 2003
Exercice: 2 - Escalier
https://prologin.org/train/2003/semifinal/escalier
"""

def escalier(nb_marches : int):
    """ Prend un entier "nb_marches" et renvoie un escalier de "nb_marches", rempli du caractère "X" de manière récursive.
    """
    if nb_marches == 0:
        return ""
    else:
        return escalier(nb_marches -1) + "\n" + "X" * nb_marches

# tests
import doctest
doctest.testmod()

# Entrée
nb_marches = int(input())

# Sortie
print(escalier(nb_marches))
