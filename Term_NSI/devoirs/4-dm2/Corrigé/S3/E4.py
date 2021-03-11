"""
Prologin:  Entraînement  2003
Exercice: 4 - Initiales
https://prologin.org/train/2003/semifinal/initiales
"""
def cherche_initiales(liste_phrase):
    """ cherche les initieles d'une phrase est l'affiche
    >>>cherche_initiales(['rentre', 'avec', 'tes', 'pieds'])
    RATP
    """
    initiale = []
    for x in liste_phrase:
        initiale.append(x[0].upper())
    return initiale

""" mon doctest ne marche pas 
import doctest
doctest.testmod()    
"""
nb_lettre = int(input())
liste_phrase = input().split()

print("".join(cherche_initiales(liste_phrase)))
