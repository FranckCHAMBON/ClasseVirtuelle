"""
Prologin: Entraînement 2003
Exercice 9 - Puzzle
https://prologin.org/train/2003/semifinal/puzzle
"""

# 0- Coeur du programme

def emplacement_compatible(puzzle: list, pièce: list, i: int, j: int) -> bool:
    """ Détermine s'il est possible de placer la pièce dans la zone sélectionée du puzzle de (i,j) à (i+3,j+3).
    Renvoie True si oui, sinon False.
    >>> puzzle = ["0000000000", "0000000000", "0000000000", "0000000000", "0000000000", "0000000000", "0000000000", "0000000000", "0000000000", "0000000000"]
    >>> pièce = ["1111", "1111", "1111", "1111"]
    >>> emplacement_compatible(puzzle, pièce, 0, 0)
    True
    """

    for x in range(4):
        for y in range(4):
            if pièce[x][y] == "1" and puzzle[i+x][j+y] == "1":
                return False
    return True

def pièce_compatible_puzzle(puzzle: list, pièce: list) -> int:
    """ Pour chaque cases du puzzle entre 0 <= i,j < 7 (car sinon, on sort du puzzle), appel la fonction emplacemnt_compatible.
    Si elle renvoie True, alors la fonction renvoie 1, 
    mais si toutes les cases ont été parcourue sans trouver d'emplacement compatible, la fonction renvoie 0.
    >>> puzzle = ["1111111111", "1110111111", "1100111001", "1100111001", "1000011101", "1100011111", "1111011111", "1100100111", "1110110011", "1110111111"]
    >>> pièce = ["0110", "0110", "1111", "0011"]
    >>> pièce_compatible_puzzle(puzzle, pièce)
    1
    """

    for i in range(7):
        for j in range(7):
            if emplacement_compatible(puzzle, pièce, i, j):
                return 1
    return 0

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture des entrées

pièce = [input() for _ in range(4)]
puzzle = [input() for _ in range(10)]

# 3- Appel de la fonction / Sortie

print(pièce_compatible_puzzle(puzzle, pièce))