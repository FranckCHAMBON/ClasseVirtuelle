"""
Prologin: Entrainement 2003
Exercice: 8 - Puissance 4
https://prologin.org/train/2003/semifinal/puissance_4
"""

def puissance_4(nb_lignes: int, nb_colonnes: int , grille: list) -> int:
    """Renvoie le vainqueur ou non du puissance 4.
    >>> puissance_4(6, 7, [[0, 0, 1, 0, 0, 0, 0], [0, 0, 2, 2, 0, 0, 0], [0, 1, 2, 1, 0, 0, 0], [0, 2, 2, 1, 0, 0, 0], [2, 2, 1, 2, 1, 0, 0], [1, 2, 1, 1, 2, 1, 0]])
    2
    """
    sens = [(1, 0), (0, 1), (1, 1), (1, -1)]

    def dans_grille(lig, col):
        return (0 <= lig < nb_lignes) and (0 <= col < nb_colonnes)
    
    def vérifie(lig, col, diff_lig, diff_col):
        pions = grille[lig][col]
        for _ in range(1, 4):
            lig += diff_lig
            col += diff_col
            if not(dans_grille(lig, col)) or (grille[lig][col] != pions):
                    return 0
        return pions

    for lig in range(nb_lignes):
        for col in range(nb_colonnes):
            if grille[lig][col] != 0:
                for diff_lig, diff_col in sens:
                    pions = vérifie(lig, col, diff_lig, diff_col)
                    if pions != 0:
                        return pions
    return ""

# Test
import doctest
doctest.testmod()

# Entrée
nb_colonnes = 7
nb_lignes = 6
grille = [list(map(int, input())) for _ in range(6)]

# Sortie 
print(puissance_4(nb_lignes, nb_colonnes, grille))