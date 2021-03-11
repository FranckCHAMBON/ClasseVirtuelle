import time 
now = time.time()

"""
Nom: PALAZON
Prénom: Anabel
Prologin: Qualification 2003
Exercice: 9 - Puzzle
https://prologin.org/train/2003/semifinal/puzzle
"""

def puzzle_possible(pièce, puzzle) -> int :
    """ Renvoie 1 si le tableau 'pièce' de 4 lignes et 4 collones peut être placé dans le tableau 'puzzle',
    Chaque tableau est composé de '0' et de '1'.
    Il faut que tous les '1' de la 'pièce' puissent prendre la place des '0' dasn 'puzzle' aux mêmes endroits.
    Renvoie 0 si non. 
    
    >>> pièce = [[0110], [0110], [1111], [0011]]
    >>> puzzle = [[1111111111], [1110111111], [1100111001], [1100111001], [1000011101], \
                  [1100011111], [1111011111], [1100100111], [1110110011], [1110111111]]
    1
    
    """ 


# Entrée

    