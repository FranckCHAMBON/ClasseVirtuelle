"""
Prologin: Entraînement 2003
Exercice 1 - 42
https://prologin.org/train/2003/semifinal/42
"""

# 0- Coeur du programme

def réponse_universelle() -> int:
    """ Renvoie la réponse à la question universelle, sur la vie, l'univers, et le reste, c'est à dire 42.
    >>> réponse_universelle()
    42
    """
    return 42

# 1- Tests

import doctest
doctest.testmod()

# 2- Appel de la fonction / Sortie

print(réponse_universelle())