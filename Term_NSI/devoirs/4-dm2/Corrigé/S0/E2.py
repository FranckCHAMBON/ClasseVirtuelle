"""
Prologin: Entraînement 2003
Exercice: 2 - Escalier
https://prologin.org/train/2003/semifinal/escalier
"""

def escalier(nb_marches : int) -> str : 
    """ Renvoie 'nb_marches' lignes avec sur chaque ligne 
    le même nombre de caractere "X" que la nième ligne.

    >>> nb_marches = 4
    >>> escalier(nb_marches)
    X
    XX
    XXX
    XXXX
    
    """    
    assert 1 < nb_marches < 200
    for marche in range (nb_marches):
        print ('X' * (marche + 1))

# tests
import doctest
doctest.testmod()

# Entrée
nb_marches = int(input())

# Sortie
escalier(nb_marches)
