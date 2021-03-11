"""
Prologin: Qualification 2003
Exercice 1 - Cases inaccessibles
https://prologin.org/train/2003/qualification/cases_inaccessibles
"""

# 0- Coeur du programme

def est_dans_le_tableau(nb_lignes: int, nb_colonnes: int, i: int, j: int) -> bool:
    """ Renvoie True si le curseur i,j est dans le tableau
    >>> est_dans_le_tableau(4, 3, 0, 0)
    True
    >>> est_dans_le_tableau(10, 10, 10, 10)
    False
    """
    if 0 <= i < nb_lignes and 0 <= j < nb_colonnes:
        return True
    else:
        return False

def déterminer_accessibilité(nb_lignes: int, nb_colonnes: int, tableau:list, est_accessible: list, i: int, j: int) -> list: 
    """ Fonction récursive renvoyant est_accessible, la liste des cases accessibles ou non du tableau.
    >>> tableau = [[4,5,3], [3,2,6], [4,1,1], [0,1,2]]
    >>> est_accessible = [[False, False, False], [False, False, False], [False, False, False], [False, False, False]]
    >>> déterminer_accessibilité(4, 3, tableau, est_accessible, 0, 0)
    [[True, False, False], [True, True, False], [False, True, True], [True, True, False]]
    """
    est_accessible[i][j] = True
    # Chaque combinaison correspond à une direction à tester, dans l'ordre on a : 
    # Droite, Gauche, Bas , Haut
    combinaisons = [(0,1), (0,-1), (1,0), (-1,0)]
    for x,y in combinaisons:                                            # Pour chaque combinaisons, 
        if est_dans_le_tableau(nb_lignes, nb_colonnes, i+x, j+y) :      # - On vérifie si le point se trouve dans le tableau
            if tableau[i+x][j+y] <= tableau[i][j]:                      # - Que le tableau de ce point soit plus petit que le précedent
                if est_accessible[i+x][j+y] == False :                  # - Que l'on est pas déjà passé par ce point (on évite de boucler)
                    est_accessible = déterminer_accessibilité(nb_lignes, nb_colonnes, tableau, est_accessible, i+x, j+y)
    return est_accessible
                

def nb_cases_inaccessibles(nb_lignes: int, nb_colonnes: int, tableau: list) -> int:
    """Renvoie le nombre de cases inaccessibles
    >>> nb_cases_inaccessibles(2, 2, [[1,2], [1,0]])
    1
    >>> nb_cases_inaccessibles(4, 3, [[4,5,3], [3,2,6], [4,1,1], [0,1,2]])
    5
    """
    est_accessible = [[False for _ in range(nb_colonnes)] for _ in range(nb_lignes)]
    déterminer_accessibilité(nb_lignes, nb_colonnes, tableau, est_accessible, 0, 0)
    compteur = 0
    for ligne in est_accessible:
        for x in ligne:
            if x is False:
                compteur += 1
    return compteur

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture des entrées

import sys
nb_lignes, nb_colonnes = map(int,input().split())
sys.setrecursionlimit(1000000)

# 3- Appel de la fonction / Sortie

tableau = [list(map(int,input().split())) for _ in range(nb_lignes)]
print(nb_cases_inaccessibles(nb_lignes, nb_colonnes, tableau))
