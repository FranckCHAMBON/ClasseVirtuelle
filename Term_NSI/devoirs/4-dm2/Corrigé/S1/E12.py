"""
Prologin: Entraînement 2003
Exercice 12 - Plage du pacifique
https://prologin.org/train/2003/semifinal/plages_du_pacifique
"""

# 0- Coeur du programme

def est_dans_le_tableau(largeur: int, hauteur: int, coord_x: int, coord_y:int, x: int, y: int) -> bool:
    """ Renvoie True si le curseur i+x,j+y est dans le tableau
    >>> est_dans_le_tableau(4, 3, 1, 1, 1, 1)
    True
    >>> est_dans_le_tableau(5, 5, 4, 4, 1, 0)
    False
    """
    if 0 <= coord_x+x <= hauteur-1 and 0 <= coord_y+y <= largeur-1:
        return True
    else:
        return False

def déterminer_départ(largeur: int, hauteur: int, tableau: list) -> tuple:
    """ Détermine les coordonnées de la première case d'eau(0) à gauche d'une case de Terre(1).
    >>> déterminer_départ(5, 5, ["00000", "01110", "01110", "01110", "00000"])
    (1, 0)
    """

    for x in range(0,hauteur-1):
        for y in range(0,largeur-1): 
            if tableau[x][y+1] == "1":
                return (x,y)

def déterminer_direction(largeur: int, hauteur: int, tableau: list, coord_x: int, coord_y: int, dernière_direction: int) -> tuple:
    """ Détermine la direction à prendre pour le prochain déplacement et renvoie x,y et le numéro de la direction(entre 1 et 8)
    >>> déterminer_direction(5, 5, ["00000", "01110", "01110", "01110", "00000"], 0, 1, 3)
    (0, 1, 2)
    """

    combinaisons = [(1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0)]
    # Chaque combinaison correspond à une direction à tester, il faut les faire dans un ordre précis!
    # Il s'agit d'un cercle qui doit toujours commencer par la case derière à droite du dernier déplacement, numéroté de 1 à 8
    dernière_direction = dernière_direction-4 if dernière_direction-4 >= 0 else dernière_direction+4 # On inverse alors le dernier déplacement pour que ce soit la case derière nous qu'il vise
    for id_combinaisons in range(-7+dernière_direction, dernière_direction):                         # On commence ainsi par le déplacement derrière à droite
        x, y = combinaisons[id_combinaisons]                                                         
        if est_dans_le_tableau(largeur, hauteur, coord_x, coord_y, x, y):                            # On vérifie si le déplacement est dans le tableau
            if tableau[coord_x+x][coord_y+y] == "0":                                                 # On vérifie que l'on aille bien sur une case de mer(qui sera donc juste à côté d'une case de Terre)
                dernière_direction = id_combinaisons+1 if id_combinaisons+1 >= 0 else id_combinaisons+9 # On met dans dernière_direction , le numéro de la direction que l'on vient de prendre
                return (x,y, dernière_direction)                                                        # (c'est à dire, l'identifiant de id_combinaison +1 ou +9 )

def nombre_de_plages(largeur: int, hauteur: int, tableau: list) -> int:
    """ Calcule le nombre de plage de l'ile, le nombre de case de terre (1) qui touche une case océan (0).
    >>> nombre_de_plages(5, 5, ["00000", "01110", "01110", "01110", "00000"])
    8
    """

    # Mise en place des variables
    emplacements_plages = list()                                          # On crée une liste des plages afin de les recenser et de ne pas en compter une 2 fois
    emplacement_de_départ = déterminer_départ(largeur, hauteur, tableau)  # Recherche de la première zone d'eau(0) à côté de Terre (1)
    coord_x, coord_y = emplacement_de_départ
    coord_x_départ, coord_y_départ = emplacement_de_départ
    emplacements_plages.append((coord_x, coord_y+1))
    coord_x -= 1                                                          # Le premier déplacement est toujours en diagonale(Haut/Droite)
    coord_y += 1
    dernière_direction = 3                                                # D'après les combinaisons dans la fonction déterminer_direction,
                                                                          # il s'agit de la 3ème direction (on commence à 1)
    # Début des déplacemennt
    while coord_x != coord_x_départ or coord_y != coord_y_départ:   # La fonction s'arrêtera lorsque nous seront revenu à notre point de départ

        # On souhaite déterminer la bonne combinaison pour continuer à avancer au bord de la plage
        x, y, dernière_direction = déterminer_direction(largeur, hauteur, tableau, coord_x, coord_y, dernière_direction) 
        coord_x += x
        coord_y += y
        combinaisons = [(1,0), (0,1), (-1,0), (0,-1)]
        # Chaque combinaison correspond à une direction à tester pour les zones de Terre(1), dans l'ordre on a : 
        # Bas, Droite, Haut, Gauche
        for x, y in combinaisons:
            if est_dans_le_tableau(largeur, hauteur, coord_x, coord_y, x, y):   # On vérifie si le déplacement est dans le tableau
                if tableau[coord_x+x][coord_y+y] == "1" and (coord_x+x, coord_y+y) not in emplacements_plages: # On vérifie s'il s'agit d'un plage et si elle n'est pas déjà répertoriée dans emplacements_plages
                    emplacements_plages.append((coord_x+x, coord_y+y)) # S'il s'agit d'une plage non répertoriée, alor son l'ajoute à la liste

    return len(emplacements_plages) # Pour finir, on renvoie le nombre de plages dans emplacements_plages

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture des entrées

largeur, hauteur = map(int,input().split())
tableau = [input() for _ in range(hauteur)]

# 3- Appel de la fonction / Sortie

print(nombre_de_plages(largeur, hauteur, tableau)) 