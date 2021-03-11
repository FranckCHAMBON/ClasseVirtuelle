""" 
Prologin: Entraînement 2003
Exercice: 8 - Puissance 4
https://prologin.org/train/2003/semifinal/puissance_4
"""
def Puissance_4(grille:list) -> int:
    """ Renvoie le gagnant 1 pour le joueur 1 ou 2 pour le joueur 2 si il arrive à aligné 4 pions identitique,sinon 0 en cas d'égalité
    >>> Puissance_4([[0, 0, 1, 0, 0, 0, 0], [0, 0, 2, 2, 0, 0, 0], [0, 1, 2, 1, 0, 0, 0], [0, 2, 2, 1, 0, 0, 0], [2, 2, 1, 2, 1, 0, 0], [1, 2, 1, 1, 2, 1, 0]])
    2
    """
    # Toutes les directions possibles 
    directions = [(1, 0), (0, 1), (1, 1), (1, -1),(-1,-1),(-1,1),(-1,0),(0,-1)]

    def est_possible(x:int, y:int) -> bool:
        """ Regarde si le déplacement est possible sur une grille 6*7
        >>> est_possible(3, 7)
        False
        >>> est_possible(2, 4)
        True
        """
        return (0 <= y < 6) and (0 <= x < 7)
    
    def recherche_gagnant(x:int, y:int, direction_y:int, direction_x:int) -> int:
        """ Recherche et affiche un joueur si il a réussi à aligné ses pions sur 4 cases à la suite dans chaque direction sinon il affiche 0
        >>> recherche_gagnant(5, 3, 1, 0)
        0
        """
        joueur = grille[y][x]
        for _ in range(1, 4):
            y += direction_y
            x += direction_x
            if not(est_possible(x, y)) or (grille[y][x] != joueur):
                    return 0
        return joueur

    for y in range(6):
        for x in range(7):
            if grille[y][x] != 0:
                for direction_y, direction_x in directions:
                    joueur = recherche_gagnant(x, y, direction_y, direction_x)
                    if joueur != 0:
                        return joueur
    return 0

# tests
import doctest
doctest.testmod()

# Entrée
grille = []
for x in range(6):
    grille.append(list(map(int,input())))

# Sortie
print(Puissance_4(grille))
                
                


