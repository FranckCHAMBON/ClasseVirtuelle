"""
Prologin: Entraînement 2003
Exercice 8 - Puissance 4
https://prologin.org/train/2003/semifinal/puissance_4
"""

# 0- Coeur du programme

def est_dans_la_grille(i: int, j: int) -> bool:
    """ Renvoie True si le curseur i,j est dans la grille
    >>> est_dans_la_grille(0, 0)
    True
    >>> est_dans_la_grille(-1, 7)
    False
    """

    #La grille à une taille de 6*7 
    if 0 <= i <= 5 and 0 <= j <= 6: 
        return True
    else:
        return False

def déterminer_gagnant(tableau: list) -> int:
    """ détermine si l'un des joueur a gagné la partie. Renvoie 1 ou 2 selon les pions gagnant et 0 si personne n'a gagné
    >>> déterminer_gagnant(["0000000", "0000000", "0000000", "0000000", "0000000", "0000000"])
    '0'
    >>> déterminer_gagnant(["0010000", "0022000", "0121000", "0221000", "2212100", "1211210"])
    '2'
    """

    # Chaque combinaison correspond à une direction à tester, dans l'ordre on a : 
    # Bas, Droite, Gauche, Haut, Diagonale(Bas/Droite), Diagonale(Haut/Gauche), Diagonale(Bas/Gauche), Diagonale(Haut/Droite)
    combinaison = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
    for i in range(6):                                  # Ensuite, pour chaque case de la grille
        for j in range(7):
            if tableau[i][j] != "0":                    # ayant un pion (!= 0)
                for x,y in combinaison:                 # on test pour chaque direction
                    if est_dans_la_grille(i+x*3,j+y*3): # s'il existe une case à 3 pîons de i,j , c'est à dire qui se trouve dans la grille
                                                        # et si cette ligne est constituée uniquement du même pion (1 ou 2)
                        if tableau[i][j] == tableau[i+x][j+y] == tableau[i+x*2][j+y*2] == tableau[i+x*3][j+y*3]:
                            return tableau[i][j]        # Si oui, on renvoie le numéro du gagnant
    return "0"                                          # Si, à la fin, on a trouvé aucunes combinaisons créant une ligne de 4 pions identiques, on renvoie 0

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture de l'entrée

grille = [input() for _ in range(6)]

# 3- Appel de la fonction / Sortie

print(déterminer_gagnant(grille))
