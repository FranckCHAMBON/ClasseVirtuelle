""" 
Prologin: Entraînement 2003
Exercice: 10 - Solitaire
https://prologin.org/train/2003/semifinal/solitaire
"""
def solitaire(grille:list) -> int:
    """ Prend une grille qui décrit des positions d'un jeu de solitaire puis recherche et renvoie le nombre de coup possible
    >>> solitaire([[2, 2, 0, 1, 1, 2, 2], [2, 2, 0, 0, 1, 2, 2], [0, 0, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0], [2, 2, 0, 0, 0, 2, 2], [2, 2, 0, 1, 1, 2, 2]])
    7
    """
    # Toutes les placements possibles d'une bille autour d'une autre 
    directions = [(1, 0),(0,1),(-1,0),(0,-1)]

    def est_possible(x:int, y:int) -> bool:
        """ Regarde si le déplacement est possible sur une grille 7*7
        >>> est_possible(3, 7)
        False
        >>> est_possible(2, 4)
        True
        """
        return (0 <= y < 7) and (0 <= x < 7) 
    
    def recherche_coup(x:int, y:int, direction_coup_y:int, direction_coup_x:int) -> int:
        """ Recherche et renvoie 1 si il est possible de faire un coup sachant qu'il y a une bille à cotè sinon 0
        """    
        y += direction_coup_y 
        x += direction_coup_x
        if not(est_possible(x, y)) or (grille[y][x] !=0):
            return 0
        return 1

    nb_coups = 0
    for y in range(7):
        for x in range(7):
            # Si on a une bille
            if grille[y][x] == 1:
                for direction_y, direction_x in directions:
                    # On regarde dans les 4 directions si il est possible de se déplacer et si il y a une bille
                    déplacement_x = x+direction_x
                    déplacement_y = y+direction_y
                    if est_possible(déplacement_y,déplacement_x) and grille[déplacement_y][déplacement_x] == 1:
                        # On regarde si le placement est possible après la bille qu'on saute
                        direction_x *= 2
                        direction_y *= 2
                        nb_coups += recherche_coup(x, y, direction_y, direction_x)
                           
    return nb_coups

# tests
import doctest
doctest.testmod()

# Entrée
grille = []
for x in range(7):
    grille.append(list(map(int,input())))

# Sortie
print(solitaire(grille))