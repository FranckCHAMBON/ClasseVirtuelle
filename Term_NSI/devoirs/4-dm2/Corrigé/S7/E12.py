""" 
Prologin: Entraînement 2003
Exercice: 12 - Plages du Pacifique
https://prologin.org/train/2003/semifinal/plages_du_pacifique
"""

def Plages_Pacifique(nb_ligne:int,nb_colonne:int,grille:list):
    """ Renvoie le nombre de plage sur une île représentée par des 1, 0 représente la mer"""
    directions = [(1, 0), (0, 1),(-1,0),(0,-1)]

    def est_possible(i, j):
        """Regarde si le déplacement est possible"""
        return (0 <= i < nb_ligne) and (0 <= j < nb_colonne)        

    def vérifie(i, j, direction_y, direction_x):
        """ vérifie si il y a une case océan à proximité d'une case terre
        """
        i += direction_y
        j += direction_x
        if est_possible(i, j) and (grille[i][j] == 0):
            return 1
        return 0
    
    def plage(i:int,j:int,directions:list) -> int:
        """ Renvoie le nombre de plage disponible"""
        for direction_y, direction_x in directions:
            if vérifie(i, j, direction_y, direction_x) != 0: 
                return 1
        return 0
                       
            
    nb_plages = 0
    sortie = 0
    for i in range(nb_ligne):
        for j in range(nb_colonne):
            if grille[i][j] == 1:
                nb_plages += plage(i,j,directions)                                 
    return nb_plages

# tests
import doctest
doctest.testmod()

# Entrée
nb_colonne,nb_ligne= map(int,input().split())
grille = []
for x in range(nb_ligne):
    grille.append(list(map(int,input())))

# Sortie
print(Plages_Pacifique(nb_ligne,nb_colonne,grille))