"""
Prologin: Entraînement 2003
Exercice: 4 - Initiales
https://prologin.org/train/2003/semifinal/initiales
"""

def initiales(texte : str) -> str :
    """ Renvoie la première lettre de chaque mot, en majuscule, dans la chaîne de caractère 'texte'.
    
    >>> texte = 'rentre avec tes pieds'
    >>> initiales(texte)
    RATP
    
    """
    for mot in texte :
        print(mot[0].upper(), end="") #mot[0] = initiale 

# tests
import doctest
doctest.testmod()

# Entrée
nb_caracteres = int(input())
assert 1 <= nb_caracteres <= 200
texte = input().split()

# Sortie
initiales(texte)
