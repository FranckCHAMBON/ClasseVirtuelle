"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/qualification/cases_inaccessibles
"""

class Pile:
    def __init__(self):
        self.pile = []
    
    def est_vide(self):
        return self.pile == []
    
    def empile(self, x):
        self.pile.append(x)

    def dépile(self):
        if self.est_vide():
            raise ValueError("Pile vide")
        else:
            return self.pile.pop()

def nb_inaccessibles(nb_lignes: int, nb_colonnes: int, grille: list) -> int:
    """Renvoie le nombre de cases inaccessibles.
    * On part en haut à gauche.
    * On bouge 1 case horitalement ou verticalement,
        + si la valeur est inférieure ou égale.
    * Exemple : 5, 3,   6,   4   et   2  sont inaccessibles.

    >>> ligne_1 = [4, 5, 3]
    >>> ligne_2 = [3, 2, 6]
    >>> ligne_3 = [4, 1, 1]
    >>> ligne_4 = [0, 1, 2]
    >>> nb_inaccessibles(4, 3, [ligne_1, ligne_2, ligne_3, ligne_4])
    5

    """

    def est_valide(i: int, j: int) -> bool:
        """Renvoie la réponse : (i, j) est-elle une position valide sur la grille ?
        """
        return (0 <= i < nb_lignes) and (0 <= j < nb_colonnes)

    def sont_connectés(i: int, j: int, idi: int, jdj: int) -> bool:
        """Renvoie la réponse : Peut-on se déplacer de (i, j) vers (idi, jdj) ?
        """
        return grille[idi][jdj] <= grille[i][j]
    

    est_marqué = [[False for j in range(nb_colonnes)] for i in range(nb_lignes)]
    # est_marqué est une matrice de booléen, indiquant si la case (i, j) a été visitée, ou programmée.
    nb_accessibles = 0

    sommets_à_traiter = Pile()
    sommets_à_traiter.empile((0, 0))
    est_marqué[0][0] = True
    nb_accessibles += 1

    while not sommets_à_traiter.est_vide():
        (i, j) = sommets_à_traiter.dépile()
        for (di, dj) in [(0, +1), (0, -1), (+1, 0), (-1, 0)]:
            idi, jdj = i + di, j + dj
            if est_valide(idi, jdj) and sont_connectés(i, j, idi, jdj):
                if not est_marqué[idi][jdj]:
                    sommets_à_traiter.empile((idi, jdj))
                    est_marqué[idi][jdj] = True
                    nb_accessibles += 1

    return nb_lignes * nb_colonnes - nb_accessibles

import doctest
doctest.testmod()

nb_lignes, nb_colonnes  = map(int, input().split())
grille = [list(map(int, input().split())) for i in range(nb_lignes)]

print(nb_inaccessibles(nb_lignes, nb_colonnes, grille))
