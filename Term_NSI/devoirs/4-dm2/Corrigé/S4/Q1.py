"""
Prologin: Entrainement 2003
Qualification : 1 - Cases inaccessibles
https://prologin.org/train/2003/qualification/cases_inaccessibles
"""

def nb_cases_inaccessibles(nb_lignes: int, nb_colonnes: int, cases: list) -> int:
    """Renvoie le nombre de cases inaccessibles suivant l'énoncé.
    
    >>> nb_lignes, nb_colonnes = 4, 3
    >>> cases = [[4, 5, 3], [3, 2, 6], [4, 1, 1], [0, 1, 2]]
    >>> nb_cases_inaccessibles(nb_lignes, nb_colonnes, cases)
    5
    
    """
    nb_cases_possibles = 0
    sens = [(1, 0) (0, 1)]


# tests
import doctest
doctest.testmod()

# Entrée
nb_lignes, nb_colonnes = map(int, input().split())
cases = [list(map(int, input().split())) for _ in range(nb_lignes)]

# Sortie
print(nb_cases_inaccessibles(nb_lignes, nb_colonnes, cases))