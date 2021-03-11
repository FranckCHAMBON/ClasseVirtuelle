"""
Nom: PALAZON
Prénom: Anabel
Prologin: Qualification 2003
Exercice: 1 - Cases inaccessibles
https://prologin.org/train/2003/semifinal/escalier
"""

def nb_coups(tableau : list) -> int:
    """ Renvpie le nombre de coups possibles

    >>> tableau = [[2201122], [2200122], [0011010], [0100000], [0010110], [2200022], [2201122]]
    >>> nb_coups(tableau)
    7

    """
    nb_colonnes = len(lignes)
    for lignes in tableau :
        for nb in range (nb_colonnes) :
            if nb == 1 :
                if  

# tests
import doctest
doctest.testmod()

# Entrée
nb_lignes = 7
tableau = [list(map(int, input().split())) for _ in range (nb_lignes)]

# Sortie
print(nb_coups(tableau))

