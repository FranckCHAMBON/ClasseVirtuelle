""" 
Prologin: Entraînement 2003
Exercice: 5 - Mot le plus long
https://prologin.org/train/2003/semifinal/mot_le_plus_long
"""

def recherche_mot_long(liste_mots : list) -> int:
    """ Renvoie la longueur du mot le plus long de la liste
    >>> recherche_mot_long(['bonjour','salutation','coucou'])
    10
    >>> recherche_mot_long(['ahahah','ok','voiture'])
    7
    """
    
    longeur_plus_longue = len(liste_mots[0])

    for x in range(1,len(liste_mots)):
        if len(liste_mots[x]) > longeur_plus_longue:
            longeur_plus_longue = len(liste_mots[x])
    return longeur_plus_longue

# tests
import doctest
doctest.testmod()

# Entrée
nb_caractère = int(input())
liste_mots = list(input().split())

# Sortie
print(recherche_mot_long(liste_mots))
