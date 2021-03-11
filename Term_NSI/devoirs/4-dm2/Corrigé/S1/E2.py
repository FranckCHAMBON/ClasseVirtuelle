"""
Prologin: Entraînement 2003
Exercice 2 - Escalier
https://prologin.org/train/2003/semifinal/escalier
"""

# 0- Coeur du programme

def construire_escalier(nb_marches: int) -> str:
    """ Renvoie un escalier de hauteur nb_marches rempli du caractère "X".
    >>> construire_escalier(1)
    'X\\n'
    >>> construire_escalier(5)
    'X\\nXX\\nXXX\\nXXXX\\nXXXXX\\n'
    """

    if nb_marches == 1:
        return("X\n" )
    else:
        return(construire_escalier(nb_marches-1) + "X"*nb_marches + "\n")
        
# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture de l'entrée

nb_marches = int(input())

# 3- Appel de la fonction / Sortie

print(construire_escalier(nb_marches))