"""
Prologin: Entraînement 2003
Exercice 5 - Mot le plus long
https://prologin.org/train/2003/semifinal/mot_le_plus_long
"""

# 0- Coeur du programme

def mot_le_plus_long(nb_lettres: int, chaîne_mots: list) -> int:
    """ Renvoie le nombre de caractère du plus long mot de chaîne_mots
    >>> mot_le_plus_long(11, ["Hello", "World"])
    5
    >>> mot_le_plus_long(74, ["ecrivez", "une", "fonction", "qui", "trouve", "la", "longueur", "du", "plus", "long", "mot", "dans", "ce", "texte"])
    8
    """

    plus_long = 0
    for mot in chaîne_mots:
        longueur_mot = len(mot)
        if longueur_mot > plus_long:
            plus_long = longueur_mot
    return plus_long
    
# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture des entrées

nb_lettres = int(input())
chaîne_mots = input().split()

# 3- Appel de la fonction / Sortie

print(mot_le_plus_long(nb_lettres, chaîne_mots))