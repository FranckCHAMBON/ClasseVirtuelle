""" 
Prologin: Entraînement 2003
Exercice: 1 - 42
https://prologin.org/train/2003/semifinal/42
"""
def réponse_universelle() -> int:
    """ Cette fonction renvoie la réponse à la question universelle, sur la vie, l'univers, qui est le nombre 42.
    >>> réponse_universelle()
    42
    """
    return 42


# tests
import doctest
doctest.testmod()

# Sortie
print(réponse_universelle())