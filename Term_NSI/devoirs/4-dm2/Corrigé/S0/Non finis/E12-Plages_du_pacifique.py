"""
Nom: PALAZON
Prénom: Anabel
Prologin: Qualification 2003
Exercice: 12 - Plages du pacifique
https://prologin.org/train/2003/semifinal/plages_du_pacifique
"""

def nb_plages(tableau : list, largeur : int, longueur : int) -> int :
    """ Renvoie le nombre total de cases contenant '1' au contact d'une autre contenant '0'.

    >>> largeur, hauteur = 5 5
    >>> tableau = [[00000], [01110], [01110], [01110], [00000]]
    8

    """

# tests
import doctest
doctest.testmod()

# Entrée
largeur, hauteur = map(int, input().split())
assert 1 <= largeur, hauteur <= 100
tableau = [list(map(int, input().split())) for _ in range (hauteur)]

# Sortie
print(nb_plages(tableau, largeur, hauteur))