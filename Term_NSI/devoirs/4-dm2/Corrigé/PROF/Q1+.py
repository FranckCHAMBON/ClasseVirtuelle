"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/qualification/cases_inaccessibles
"""

nb_lignes, nb_colonnes  = map(int, input().split())
grille = [list(map(int, input().split())) for i in range(nb_lignes)]

vu = [[False for _ in range(nb_colonnes)] for _ in range(nb_lignes)]

def est_valide(i: int, j: int) -> bool:
    """Renvoie la réponse : (i, j) est-elle une position valide sur la grille ?
    """
    return (0 <= i < nb_lignes) and (0 <= j < nb_colonnes)

def sont_connectés(i: int, j: int, idi: int, jdj: int) -> bool:
    """Renvoie la réponse : Peut-on se déplacer de (i, j) vers (idi, jdj) ?
    """
    return grille[idi][jdj] <= grille[i][j]

def visite(i: int, j: int) -> None:
    """Visite récursivement le graphe"""
    if vu[i][j] == False:
        vu[i][j] = True
        for (di, dj) in [(0, +1), (0, -1), (+1, 0), (-1, 0)]:
            idi, jdj = i + di, j + dj
            if est_valide(idi, jdj) and sont_connectés(i, j, idi, jdj):
                visite(idi, jdj)

visite(0, 0)
nb_inaccessibles = 0
for i in range(nb_lignes):
    for j in range(nb_colonnes):
        if vu[i][j] == False:
            nb_inaccessibles += 1
print(nb_inaccessibles)

