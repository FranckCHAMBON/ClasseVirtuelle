""" 
Prologin: Entraînement 2003
Exercice: 9 - Puzzle
https://prologin.org/train/2003/semifinal/puzzle
"""
def insertion_puzzle(petit_puzzle: list, grand_puzzle : list):
    """ Regarde si l'on peut insérer le petit puzzle 4*4 dans les emplacements vides du grand puzzle
    >>> insertion_puzzle([[0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 1, 1], [0, 0, 1, 1]],[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 0, 1, 1, 1, 0, 1], [1, 1, 0, 0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]])
    1
    """
    def début_petit_puzzle(petit_puzzle:list) -> tuple:
        """Renvoie les coordonnées de la première pièce du petit puzzle
        >>> début_petit_puzzle([[0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 1, 1], [0, 0, 1, 1]])
        (0,1)
        """
        for y in range(4):
            for x in range(4):
                if petit_puzzle[y][x] != 0:
                    return (y,x)

    début = début_petit_puzzle(petit_puzzle)
                    

    déplacements = []
    def recherche_déplacement(petit_puzzle: list,déplacements:list,début:tuple):
        """ Prend le positionnement de chaque piéce du puzzle par rapport à la première pièce et le met dans déplacements
        >>> recherche_déplacement([[0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 1, 1], [0, 0, 1, 1]],[],(0,1))
        """
        y,x = début
        for y_1 in range(4):
            for x_1 in range(4):
                if petit_puzzle[y_1][x_1] != 0:
                    déplacements.append((y_1-y,x_1-x))


            
    # On affecte chaque déplacement du petit puzzle dans déplacement
    recherche_déplacement(petit_puzzle,déplacements,début)
    
    def est_possible(y : int, x:int) -> bool:
        """ Regarde si le déplacement est possible
        >>> est_possible(8,9)
        True
        >>> est_possible(10,2)
        False
        """
        return (0 <= x < 10) and (0 <= y < 10)

    def recherche_emplacement(x:int, y:int, déplacements:list,grand_puzzle:list) -> int:
        """ Recherche si il est possible d'insérer le petit puzzle dans le grand puzzle et renvoie 1 sinon 0
        >>> recherche_emplacement(2,2,[(0, 1), (1, 0), (1, 1), (2, -1), (2, 0), (2, 1), (2, 2), (3, 1), (3, 2)],[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 0, 1, 1, 1, 0, 1], [1, 1, 0, 0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]])
        1
        """
        for déplacement_y,déplacement_x in déplacements:
            if not(est_possible(y + déplacement_y, x+  déplacement_x)) or (grand_puzzle[y+déplacement_y][x+ déplacement_x] != 0):
                return 0
        return 1

    for y in range(10):
        for x in range(10):
            if grand_puzzle[y][x] != 1:
                insertion_possible = recherche_emplacement(x, y,déplacements,grand_puzzle)
                if insertion_possible == 1:
                    return insertion_possible
    return 0

# tests
import doctest
doctest.testmod()

# Entrée
petit_puzzle = []
for x in range(4):
    petit_puzzle.append(list(map(int,input())))

grand_puzzle = []
for x in range(10):
    grand_puzzle.append(list(map(int,input())))

# Sortie
print(insertion_puzzle(petit_puzzle,grand_puzzle))