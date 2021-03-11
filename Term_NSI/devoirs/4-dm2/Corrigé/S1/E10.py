"""
Prologin: Entraînement 2003
Exercice 10 - Solitaire
https://prologin.org/train/2003/semifinal/solitaire
"""

# 0- Coeur du programme

def est_dans_le_plateau(i: int, j:int, plateau: list) -> bool:
    """ Renvoie True si le curseur i,j est dans le plateau (dans le bon intervalle 0 <= i,j < 7 et que le curseur ne cible pas un 2)
    >>> plateau = ["2201122", "2200122", "0011010", "0100000", "0010110", "2200022", "2201122"]
    >>> est_dans_le_plateau(0, 0, plateau)
    False
    >>> est_dans_le_plateau(4, 3, plateau)
    True
    """

    if 0 <= i <= 6 and 0 <= j <= 6:
        if plateau[i][j] != "2":
            return True
    return False

def nombre_de_coups(plateau: list) -> int:
    """ Détermine combien il existe de coups différents possibles, pour le prochain coup et renvoie le nombre.
    >>> plateau = ["2201122", "2200122", "0011010", "0100000", "0010110", "2200022", "2201122"]
    >>> nombre_de_coups(plateau)
    7
    """

    # Chaque combinaison correspond à une direction à tester, dans l'ordre on a : 
    # Droite, Bas, Gauche, Haut
    combinaison = [(0,1),(1,0),(0,-1),(-1,0)]
    compteur = 0                                                     # On initialise le compteur à 0
    for i in range(7):                                               # Ensuite, pour chaque case du plateau          
        for j in range(7):
            if plateau[i][j] == "1":                                 # ayant un pion (= 1)
                for x, y in combinaison:                             # on test pour chaque direction
                    if est_dans_le_plateau(i+x*2, j+y*2, plateau):   # s'il existe une case à 2 pîons de i,j , c'est à dire qui se trouve dans la grille
                                                                     # et si le premier pion dans la direction est un 1 et le second est un 0
                        if plateau[i+x][j+y] == "1" and plateau[i+x*2][j+y*2] == "0":
                            compteur += 1                            # Si oui, on ajoute 1 au compteur
    return compteur                                                  # Quand on a vérifié toutes les cases, on renvoie compteur

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture de l'entrée

plateau = [input() for _ in range(7)]

# 3- Appel de la fonction / Sortie

print(nombre_de_coups(plateau))