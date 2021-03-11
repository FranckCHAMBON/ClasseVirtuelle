"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/qualification/cases_inaccessibles
"""

def nb_inacessibles(nb_lignes: int, nb_colonnes: int, grille: list) -> int:
    """Renvoie le nombre de cases inaccessibles.
    * On part en haut à gauche.
    * On bouge 1 case horitalement ou verticalement,
        + si la valeur est inférieure ou égale.
    * Exemple : 5, 3,   6,   4   et   2  sont inaccessibles.

    >>> ligne_1 = [4, 5, 3]
    >>> ligne_2 = [3, 2, 6]
    >>> ligne_3 = [4, 1, 1]
    >>> ligne_4 = [0, 1, 2]
    >>> nb_inacessibles(4, 3, [ligne_1, ligne_2, ligne_3, ligne_4])
    5

    """

    def est_valide(i, j):
        return (0 <= i < nb_lignes) and (0 <= j < nb_colonnes)

    def sont_connectés(i, j, idi, jdj):
        return grille[idi][jdj] <= grille[i][j]

    vecteurs = [(0, +1), (0, -1), (+1, 0), (-1, 0)]
    est_vue = [[False for j in range(nb_colonnes)] for i in range(nb_lignes)]
    est_vue[0][0] = True
    réponse = nb_colonnes * nb_lignes - 1
    sommets_courants = [(0, 0)]

    while sommets_courants != []:
        sommets_suivants = []
        for (i, j) in sommets_courants:
            for (di, dj) in vecteurs:
                idi, jdj = i + di, j + dj
                if est_valide(idi, jdj) and sont_connectés(i, j, idi, jdj):
                    if not est_vue[idi][jdj]:
                        sommets_suivants.append((idi, jdj))
                        est_vue[idi][jdj] = True
                        réponse -= 1
        sommets_courants = sommets_suivants

    return réponse

import doctest
doctest.testmod()

nb_lignes, nb_colonnes  = map(int, input().split())
grille = [list(map(int, input().split())) for i in range(nb_lignes)]
for i in range(nb_lignes):
    assert len(grille[i]) == nb_colonnes, \
                f"Erreur ligne {i}, {len(grille[i])} ≠ {nb_colonnes}"

print(nb_inacessibles(nb_lignes, nb_colonnes, grille))
