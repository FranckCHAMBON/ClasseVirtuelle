"""
Nom: PALAZON
Prénom: Anabel
Prologin: Qualification 2003
Exercice: 1 - Cases inaccessibles
https://prologin.org/train/2003/qualification/cases_inaccessibles
"""

#je n'ai pas compris l'énoncé

def nb_cases_inaccessibles(nb_lignes: int, nb_colonnes: int, tableau: list) -> int:
    """Renvoie le nombre de cases inaccessibles suivant l'énoncé.
    
    >>> nb_lignes, nb_colonnes = 4, 3
    >>> tableau = [[4, 5, 3], [3, 2, 6], [4, 1, 1], [0, 1, 2]]
    >>> nb_cases_inaccessibles(nb_lignes, nb_colonnes, tableau)
    5
    
    """
    pos_actuelle = tableau[0][0]

    if tableau[0][1] <= pos_actuelle : #droite


    if tableau[0][-1] <= pos_actuelle : #gauche
    
    if tableau[1][0] <= pos_actuelle : #bas


    if tableau[-1][0] <= pos_actuelle : #haut


    for lignes in tableau :
        for case in lignes :
            if 





# Entrée
nb_lignes, nb_colonnes = map(int, input().split())
assert (1 <= nb_lignes, nb_colonnes <= 500)
cases = [list(map(int, input().split())) for _ in range(nb_lignes)]

# Sortie
print(nb_cases_inaccessibles(nb_lignes, nb_colonnes, cases))

