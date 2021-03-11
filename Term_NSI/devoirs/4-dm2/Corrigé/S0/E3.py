"""
Prologin: Entraînement 2003
Exercice: 3 - Grand écart
https://prologin.org/train/2003/semifinal/grand_ecart
"""

def écart_max (tableau : list) -> int :
    """ Renvoie un entier qui est le plus grand écart 
    entre une paire d'entier qui se succèdent dans une liste.

    >>> tableau = [4, 2, 3, 5, 10, 6, 4, 9, 1, 3]
    >>> écart_max(tableau)
    8
    
    """
    max = 0
    for élément in range (len(tableau)-1) :
        écart = abs(tableau[élément] - tableau[élément + 1])
        if max < écart :
            max = écart
    return max

# tests
import doctest
doctest.testmod()

# Entrée 
nb_éléments = int(input())
assert 2 <= nb_éléments <= 300
tableau = list(map(int, input().split()))

# Sortie
print (écart_max(tableau))