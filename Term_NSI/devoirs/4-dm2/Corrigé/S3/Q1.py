"""
Prologin: Qualification 2003
Exercice: 1 - Cases inaccessibles
https://prologin.org/train/2003/qualification/cases_inaccessibles
"""
def parcour_plateau(matrice, nb_ligne: int, nb_cologne: int):
    """ on parcour la matrice qui fait référence à 
    un plateau de jeu et on doit atteindre la dernier partie de la matrice 
    de plus on conte les casse qui sont inaccesible 
    >>> matrice = [['4', '5', '3'], ['3', '2', '6'], ['4', '1', '1'], ['0', '1', '2']]
    5
    >>> matrice = [['4', '5', '3'], ['5', '2', '6'], ['4', '1', '1'], ['0', '1', '2']]
    2
    """
    aller_droite = 0
    aller_bad = 0
    nb_inaccesible = 0
    while aller_droite < nb_cologne - 1 and aller_bad < nb_ligne - 1:
        if aller_droite < nb_cologne - 1:
            if matrice[aller_bad][aller_droite] < matrice[aller_bad][aller_droite + 1]:
                nb_inaccesible += 1
            else:
                if matrice[aller_bad][aller_droite] < matrice[aller_bad + 1][aller_droite]:
                    nb_inaccesible += 1
                    aller_droite += 1
                else:
                    aller_droite += 1
        if aller_bad < nb_ligne - 1: 
            if matrice[aller_bad][aller_droite] < matrice[aller_bad + 1][aller_droite]:
                nb_inaccesible += 1
            else:
                if matrice[aller_bad][aller_droite] < matrice[aller_bad][aller_droite + 1]:
                    nb_inaccesible += 1
                    aller_bad += 1
                else:
                    aller_bad += 1
    return nb_inaccesible

nb_ligne, nb_cologne = map(int, input().split())
matrice = [[[] for _ in range(nb_cologne)] for _ in range(nb_ligne)]
for x in range (nb_ligne):
    matrice[x] =  input().split()
print(parcour_plateau(matrice, nb_ligne, nb_cologne))
"""problème il est trop long"""

