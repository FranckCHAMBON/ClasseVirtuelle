"""
Prologin: Entrainement 2003
Exercice: 6 - Nombres impairs
https://prologin.org/train/2003/semifinal
"""

def impairs(premier_entier: int, deuxieme_entier: int) -> int:
    """Renvoie les nombres impairs entre deux données.
    >>> impairs(42,51)
    43 45 47 49 51 
    """
    for x in range (premier_entier, deuxieme_entier+1):
        if x & 1 == 1:
            print(x, end=" ")

# Test
import doctest
doctest.testmod()

# Entrées
premier_entier, deuxieme_entier = map(int, input().split())

if not(1 <= premier_entier < deuxieme_entier <= 200):
    raise ValueError('Les nombres sont soit gros grand, soit le premier nombre et plus grand que le deuxième.')

# Sortie
impairs(premier_entier, deuxieme_entier)

