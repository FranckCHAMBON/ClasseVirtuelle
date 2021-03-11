"""
Prologin: Entraînement 2003
Exercice: 6 - Nombres impairs
https://prologin.org/train/2003/semifinal/nombres_impairs
"""

def nb_impairs(début : int, fin : int) -> int :
    """ Renvoie, dans l'ordre croissant, 
    tous les entiers impairs se trouvant entre les nombres 'début' et 'fin'.
    
    >>> début, fin = 42 51
    >>> nb_impairs(début, fin)
    43 45 47 49 51
    
    """
    for nb in range (début, fin + 1) :
        if nb % 2 != 0 : #si nb est impair
            print(nb, end=" ")

# tests
import doctest
doctest.testmod()

# Entrée
début, fin = map(int, input().split())
assert 1 <= début < fin <= 200 

# Sortie
nb_impairs(début, fin)
