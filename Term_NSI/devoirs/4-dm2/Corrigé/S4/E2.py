"""
Prologin: Entrainement 2003
Exercice: 2 - escalier
https://prologin.org/train/2003/semifinal/escalier
"""

def triangle(nb_marches : int): 
    """Renvoie un triangle rectangle à la hauteur demandé.
    >>> triangle(4)
    X 
    XX 
    XXX 
    XXXX 
    """
    if nb_marches == 0:
        return ""
    else:
        return triangle(nb_marches-1) + "\n" + "X"*nb_marches

# Test (Ne fonctionne pas)
#import doctest
#doctest.testmod() 

# Entrée
nb_marches = int(input())

# Sortie
print(triangle(nb_marches))

