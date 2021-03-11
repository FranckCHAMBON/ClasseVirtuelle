"""
Prologin: Entraînement 2003
Exercice: 5 - Mot le plus long
https://prologin.org/train/2003/semifinal/mot_le_plus_long
"""

def longueur_max_mot(texte : str) -> int :
    """ Renvoie l'entier correspondant à la longueur du plus long mot 
    de la chaîne de caractère 'texte'. 
    
    >>> texte = 'ecrivez une fonction qui trouve la longueur du plus long mot dans ce texte'
    >>> longueur_max_mot(texte)
    8
    
    """ 
    max = 0
    for mot in texte :
        if len(mot) > max :
            max = len(mot)
    return max

# tests
import doctest
doctest.testmod()

# Entrée
nb_caractères = int(input())
assert 1 <= nb_caractères <= 200
texte = input().split()

# Sortie
print(longueur_max_mot(texte))