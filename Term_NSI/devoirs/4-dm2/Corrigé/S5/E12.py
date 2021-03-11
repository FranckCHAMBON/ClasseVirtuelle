"""
Prologin: Entraînement 2003
Exercice: 12- Plan du métro
https://prologin.org/train/2003/semifinal/plages_du_pacifique
"""

nb_colonnes, nb_lignes = map(int, input().split(" "))

carte = []

vecteurs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for _ in range(nb_lignes):
    entrée = list(map(int, list(input())))
    carte.append(entrée)

def est_dans_la_carte(x,y):
    """
    """
    return (0<=x<nb_lignes) and (0<= y < nb_colonnes)

def liste_les_océans():
    """
    Renvoie un ensemble avec toutes les cases qui sont un océan
    >>> liste_les_océans()
    {(0,0),(0,1)(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)}
    """
    ensemble_océans = {(0, 0)}
    for x in range(nb_lignes):
        for y in range(nb_colonnes):
            for delta_x in [-1, 0 , 1]:
                for delta_y in [-1, 0, 1]:
                    if delta_x == 0 and delta_y == 0:
                        continue
                    else:
                        if not est_dans_la_carte(x+delta_x, y+delta_y):
                            continue
                        else:
                            if carte[delta_x+x][delta_y+y] == 0:
                                if (x+delta_x, y+delta_y) in ensemble_océans:
                                    if carte[x][y] == 0:
                                        ensemble_océans.add((x, y))
    return ensemble_océans

ensemble_océans = liste_les_océans()

ensemble_océans = sorted(ensemble_océans)

def liste_les_plages():
    """
    Renvoie un ensemble avec toutes les cases étant des plages
    >>> liste_les_plages()
    {(1,1),(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)}
    """
    ensemble_plages = set()
    for x in range(nb_lignes):
        for y in range(nb_colonnes):
            if carte[x][y] == 0:
                continue    
            for delta_x, delta_y in vecteurs:
                if (x+delta_x, y+delta_y) in ensemble_océans:
                    ensemble_plages.add((x, y))
                    continue
    return sorted(ensemble_plages)

ensemble_plages = liste_les_plages()
print(len(ensemble_plages))
