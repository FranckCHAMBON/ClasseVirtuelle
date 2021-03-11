"""
Prologin: Entraînement 2003
Exercice: 8 - Puissance 4
https://prologin.org/train/2003/semifinal/puissance_4
"""

nb_lignes = 6
nb_colonnes = 7

plateau = [[0 for _ in range(nb_colonnes)] for _ in range(nb_lignes)]

for ligne in range(nb_lignes):
    entrée_str = list(input())
    entrée = list(map(int, entrée_str))
    for colonne in range(nb_colonnes):
        plateau[ligne][colonne] = entrée[colonne]

directions = [(-1,1),(0,1),(1,1),(1,0)]

def est_dans_le_plateau(ligne, colonne):
    """
    Retourne un booléen si les coordonnées (`ligne`,`colonne`) est
    dans le plateau
    """
    if (ligne < 0) or (ligne >= nb_lignes) or (colonne < 0) or (colonne >= nb_colonnes):
        return False
    return True

gagnant = 0

for ligne in range(nb_lignes):
    for colonne in range(nb_colonnes):
        if gagnant != 0:
            break
        joueur = plateau[ligne][colonne]
        if joueur != 0:
            for direction in directions:
                ligne_temporaire = ligne
                colonne_temporaire = colonne
                alignés = 1
                for _ in range(3):
                    ligne_temporaire += direction[0]
                    colonne_temporaire += direction[1]
                    if est_dans_le_plateau(ligne_temporaire, colonne_temporaire):
                        if(plateau[ligne_temporaire][colonne_temporaire] == joueur):
                            alignés += 1
                if alignés == 4:
                    gagnant = joueur
print(gagnant)

