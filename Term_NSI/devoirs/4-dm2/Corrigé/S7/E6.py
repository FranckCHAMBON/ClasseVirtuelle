""" 
Prologin: Entraînement 2003
Exercice: 6 - nombres impairs
https://prologin.org/train/2003/semifinal/nombres_impairs
"""

def nombres_impairs(début : int , fin : int) -> list:
    """ Recherche sur un intervalle tout les nombres impairs et les renvoies de manière récursive
    >>> nombres_impairs(23,33)
    23 25 27 29 31 33 
    """
    if début > fin:
        return 
    if début % 2 == 1:
            print(début,end=" ")
            return nombres_impairs(début+1,fin)
    else:
        return nombres_impairs(début+1,fin)

# tests
import doctest
doctest.testmod()     

# Entrée
début,fin = map(int,input().split())

# Sortie
nombres_impairs(début,fin)



    