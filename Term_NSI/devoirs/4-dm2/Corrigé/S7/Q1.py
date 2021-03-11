""" 
Prologin: Qualification 2003
Exercice: 1 - Cases inaccessibles
https://prologin.org/train/2003/qualification/cases_inaccessibles
"""
def nb_cases_inaccessibles(nb_lignes: int, nb_colonnes: int, cases: list) -> int:
    """
    Recherche et renvoie le nombre de case inaccesible 
    """
    # 4 directions possibles
    directions = [(1, 0),(0,1),(-1,0),(0,-1)]

    def est_possible(y:int, x:int) -> bool:
        """ Regarde si le déplacement est possible
        """
        return (0 <= y < nb_lignes) and (0 <= x < nb_colonnes) 

    def recherche_chemin(y:int, x:int, direction_y:int, direction_x:int) -> int:
        """ Recherche et renvoie 1 si on peut prendre le chemin sinon 0
        """    
        déplacement_y = y + direction_y 
        déplacement_x  = x + direction_x
        if not(est_possible(déplacement_y, déplacement_x)) and (cases[y][x] < cases[déplacement_y][déplacement_x]):
            return 0
        return 1

    départ = (0,0) 
    def nombre_pas(départ:tuple) -> int:
        """ Renvoie le nombre de case visité de manière récursive """
        # Fonctionne théoriquement mais pas à la pratique car il y a sois disant trop de récursion
        nb_pas = 0
        y,x = départ
        for direction_y, direction_x in directions:
            if recherche_chemin(y,x,direction_y,direction_x) != 0:
                déplacement_x = x + direction_x
                déplacement_y = y + direction_y
                nb_pas += 1 + nombre_pas((déplacement_y,déplacement_x))
                
        return nb_pas
    return nombre_pas(départ)


        
# tests
import doctest
doctest.testmod()

# Entrée
nb_lignes, nb_colonnes = map(int, input().split())
cases = [list(map(int, input().split())) for _ in range(nb_lignes)]

# Sortie
nombre_cases = nb_lignes * nb_colonnes
print(nombre_cases - nb_cases_inaccessibles(nb_lignes, nb_colonnes, cases))
