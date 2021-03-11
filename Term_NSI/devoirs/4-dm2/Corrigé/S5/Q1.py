"""
Prologin: Qualification 2003
Exercice: 1 - Cases inaccessibles
https://prologin.org/train/2003/qualification/cases_inaccessibles
"""
"""
4 3
4 5 3
3 2 6
4 1 1
0 1 2
"""

from collections import deque

# Entrée
nb_lignes, nb_colonnes = map(int, input().split())
cases = [list(map(int, input().split())) for _ in range(nb_lignes)]

dictionnaire_vecteurs = {"N": (-1, 0), "S": (1, 0), "O": (0, -1), "E": (0, 1)}

#J'utilise une `deque` comme implémentation de la file (celle-ci est plus efficace et plus rapide qu'une classe `File` en P.O.O)
file = deque()
enfile = file.append
défile = file.popleft

def est_dans_la_liste(x: int, y: int) -> bool:
    """
    Permet de renvoyer True si les coordonnées `x` et `y` sont dans le domaine de 
    définition de la liste `cases`
    >>> cases = [[1, 6, 3], [5, 9, 6], [7, 2, 0], [5, 4, 6]]
    >>> est_dans_la_liste(1,2)
    True
    >>> est_dans_la_liste(9, 5)
    False
    """
    return ((0 <= x < nb_lignes) and (0 <= y < nb_colonnes))

def est_déplaçable(élément: int, x: int, y: int) -> bool:
    """
    Permet de renvoyer True si la valeur situé aux coordonnées (`x`,`y`) est inférieure ou égale
    à `élément`
    >>> cases = [[1, 6, 3], [5, 9, 6], [7, 2, 0], [5, 4, 6]] 
    >>> est_déplaçable(cases[0][1], 0, 2)
    True
    >>> est_déplaçable(cases[0][0], 0, 1)
    False
    """
    return cases[x][y] <= élément

def donne_les_directions(x: int, y: int) -> list:
    """
    Renvoie la liste des directions où on peut se déplacer à partir des coordonnées(`x`, `y`)
    >>> cases = [[1, 6, 3], [5, 9, 6], [7, 2, 0], [5, 4, 6]] 
    >>> donne_les_directions(0, 0)
    ['S']
    >>> donne_les_directions(2, 1)
    ['S', 'E']
    """
    liste_directions = []
    for direction, tuple_delta in dictionnaire_vecteurs.items():
        delta_x, delta_y = tuple_delta
        x_temporaire = x + delta_x
        y_temporaire = y + delta_y
        if est_dans_la_liste(x_temporaire, y_temporaire):
            if est_déplaçable(cases[x][y],x_temporaire, y_temporaire):
                liste_directions.append(direction)
    return liste_directions

def donne_nb_cases_inaccessibles(x_départ: int, y_départ: int) -> int:
    """
    Cette fonction est le coeur du programme.
    Elle a pour paramètres des coordonnées (`x_départ`,`y_départ`) qui sont les coordonnées
    de départ du chemin dans `cases`
    Et elle renvoie le nombre de cases inaccessible
    >>> cases = [[4, 5, 3], [3, 2, 6], [4, 1, 1], [0, 1, 2]]
    >>> donne_nb_cases_inaccessibles(0,0)
    5
    """
    déja_vu = set()
    enfile((x_départ, y_départ))
    while len(file) != 0:
        x, y = défile()
        déja_vu.add((x, y))
        liste_directions = donne_les_directions(x, y)
        for direction in liste_directions:
            delta_x, delta_y = dictionnaire_vecteurs[direction]
            x_temp = x + delta_x
            y_temp = y + delta_y
            if (x_temp, y_temp) in déja_vu:
                pass
            else:
                enfile((x_temp, y_temp))
    return (nb_lignes*nb_colonnes) - len(déja_vu)    



# tests
import doctest
doctest.testmod()


# Sortie
print(donne_nb_cases_inaccessibles(0, 0))