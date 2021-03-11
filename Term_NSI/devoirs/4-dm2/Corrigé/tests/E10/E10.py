"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/solitaire
"""

grille = [input() for _ in range(7)]

def est_valide(i: int, j: int) -> bool:
    if not((0 <= i < 7) and (0 <= j < 7)):
        # en dehors du grand rectangle
        return False
    # Est-on sur une des deux bandes ?
    return (2 <= i < 5) or (2 <= j < 5)

def est_occupée(i: int, j: int) -> bool:
    return est_valide(i, j) and (grille[i][j] == "1")

def est_libre(i: int, j: int) -> bool:
    return est_valide(i, j) and (grille[i][j] == "0")

réponse = 0
for i in range(7):
    for j in range(7):
        if est_occupée(i, j):
            for di, dj in [(0, +1), (0, -1), (+1, 0), (-1, 0)]:
                if est_occupée(i + di, j + dj):
                    if est_libre(i + 2*di, j + 2*dj):
                        réponse += 1
print(réponse)

"""
TEST
entrée :

2201122
2200122
0011010
0100000
0010110
2200022
2201122

sortie :

7

"""