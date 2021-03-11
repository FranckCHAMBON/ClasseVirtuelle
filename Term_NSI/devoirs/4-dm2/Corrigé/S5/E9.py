"""
Prologin: Entraînement 2003
Exercice: 9 - Puzzle
https://prologin.org/train/2003/semifinal/puzzle
"""
nb_lignes_pièce = nb_colonnes_pièce = 4
nb_lignes_puzzle = nb_colonnes_puzzle = 10

pièce = []
puzzle = []

for ligne in range(nb_lignes_pièce):
    entrée = list(map(int, list(input())))
    pièce.append(entrée)

for ligne in range(nb_lignes_puzzle):
    entrée = list(map(int, list(input())))
    puzzle.append(entrée)

def est_dans_le_puzzle(x, y):
    """
    Renvoie si les coordonnées `x` et `y` sont dans les limites de la puzlle
    """
    return (0 <= x < nb_lignes_puzzle )and (0 <= y < nb_colonnes_puzzle)

def recherche_puzzle_correct(x_départ, y_départ):
    """
    Retourne un booléen si la pièce est compatible avec le puzzle à partir du coordonnées `x_départ` `y_départ`
    """
    for delta_x in range(4):
        for delta_y in range(4):
            if not est_dans_le_puzzle(x_départ+delta_x, y_départ+delta_y):
                return False
            if puzzle[x_départ+delta_x][y_départ+delta_y] == 1 and 1 == pièce[delta_x][delta_y]:
                return False
    return True

puzzle_correct = False

for ligne in range(nb_lignes_puzzle):
    for colonne in range(nb_lignes_puzzle):
        if puzzle_correct:
            break
        if puzzle[ligne][colonne] != puzzle[0][0]:
            if recherche_puzzle_correct(ligne, colonne):
                puzzle_correct = True
print(1 if puzzle_correct else 0)
