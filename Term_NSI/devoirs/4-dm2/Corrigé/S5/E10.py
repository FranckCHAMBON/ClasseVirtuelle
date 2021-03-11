"""
Prologin: Entraînement 2003
Exercice: 10 - Solitaire
https://prologin.org/train/2003/semifinal/solitaire
"""

plateau = []

liste_billes = []

for ligne in range(7):
    entrée = list(input())
    plateau.append(entrée)
    for colonne in range(7):
        if entrée[colonne] == "1":
            liste_billes.append((ligne, colonne))

def est_déplaçable(x, y):
    """
    Retourne le nombre de déplacements possibles à partir de (`x`,`y`)
    """
    nombre_déplacements = 0


    if 0 <= x+2 < 7 and 0 <= y < 7:
        if plateau[x+1][y] == "1":
            if plateau[x+2][y] == "0":
                nombre_déplacements += 1

    if 0 <= x < 7 and 0 <= y+2 < 7:
        if plateau[x][y+1] == "1":
            if plateau[x][y+2] == "0":
                nombre_déplacements += 1

    if 0 <= x-2 < 7 and 0 <= y < 7:
        if plateau[x-1][y] == "1":
            if plateau[x-2][y] == "0":
                nombre_déplacements += 1

    if 0 <= x < 7 and 0 <= y-2 < 7:
        if plateau[x][y-1] == "1":
            if plateau[x][y-2] == "0":
                nombre_déplacements += 1

    return nombre_déplacements

somme_déplacements = sum(est_déplaçable(x_bille, y_bille) for x_bille, y_bille in liste_billes)

print(somme_déplacements)