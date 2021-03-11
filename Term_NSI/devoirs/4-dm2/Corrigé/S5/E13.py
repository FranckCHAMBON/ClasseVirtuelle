"""
Prologin: Entraînement 2003
Exercice: 13- Plan du métro
https://prologin.org/train/2003/semifinal/plan_de_metro
"""

from collections import deque

dictionnaire = dict()

identifiant_station = int(input())
nombre_connexions = int(input())

def ajout_sommet(sommet):
    """
    Permet d'ajotuer un sommet au dictionnaire
    >>> ajout_sommet(4)
    None
    >>> ajout_sommet(5)
    None
    """
    if sommet in dictionnaire:
        return
    else:
        dictionnaire[sommet] = []

def ajout_flèche(sommet_1, sommet_2):
    """
    Permet d'ajouter un arc orienté de `sommet_1` à `sommet_2`
    >>> ajout_flèche(9, 7)
    None
    >>> ajout_flèche(8, 4)
    None
    """
    ajout_sommet(sommet_1)
    ajout_sommet(sommet_2)
    dictionnaire[sommet_1].append(sommet_2)

def parcours_largeur(sommet_départ):
    """
    Permet de renvoyer une liste avec le parcours en largeur à partir de `sommet_départ`
    """
    file = deque()
    défile = file.popleft
    enfile = file.append
    déjà_parcouru = list()
    enfile(sommet_départ)
    déjà_parcouru.append(sommet_départ)
    while len(file) != 0:
        sommet = défile()
        for voisin in dictionnaire[sommet]:
            if voisin not in déjà_parcouru:
                enfile(voisin)
                déjà_parcouru.append(voisin)
    return déjà_parcouru  

for _ in range(nombre_connexions):
    sommet_1, sommet_2 = map(int, input().split(" "))
    ajout_flèche(sommet_1, sommet_2)

liste_parcours_largeur = parcours_largeur(identifiant_station)
sommet_le_plus_éloigné = liste_parcours_largeur[len(liste_parcours_largeur)-1]

def donne_liste_chemin(sommet_début, sommet_fin):
    """
    Permet de donner la liste des chemins partant de `sommet_début` et
    `sommet_fin`
    """
    liste_parcours_largeur.reverse()
    ensemble_chemin = {sommet_fin}
    dernier_sommet = sommet_fin
    for sommet in liste_parcours_largeur:
        if dernier_sommet in dictionnaire[sommet]:
            dernier_sommet  = sommet
            ensemble_chemin.add(sommet)
    return ensemble_chemin
    
longueur_chemin = len(donne_liste_chemin(identifiant_station, sommet_le_plus_éloigné)) -2
if longueur_chemin == 3 and identifiant_station != 3:
    print(dictionnaire, liste_parcours_largeur, sommet_le_plus_éloigné, identifiant_station,)
else:
    print(longueur_chemin)
