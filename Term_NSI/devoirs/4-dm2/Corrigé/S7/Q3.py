""" 
Prologin: Qualification 2003
Exercice: 3 - Les trois nombres
https://prologin.org/train/2003/qualification/les_trois_nombres
"""
def les_trois_nombres(liste_nombres:list) -> int:
    """ Recherche si une addition des 2 nombres de la liste font le troisième nombre  et renvoie le troisième nombre ou 0 si il n'y pas de combinaison
    >>> les_trois_nombres([18,42,24])
    42
    >>> les_trois_nombres([10,32,18])
    0
    """
    for x in range(3):
        for y in range(x,3):
            nombre = liste_nombres[x] + liste_nombres[y] 
            if nombre in liste_nombres:
                return nombre
    return 0

# tests
import doctest
doctest.testmod()

# Entrée
liste_nombres = list(map(int,input().split()))

# Sortie
print(les_trois_nombres(liste_nombres))