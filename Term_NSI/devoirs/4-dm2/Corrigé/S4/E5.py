"""
Prologin: Entrainement 2003
Exercice: 5 - Mot le plus long
https://prologin.org/train/2003/semifinal/mot_le_plus_long
"""

def mot_le_plus_long(phrase : str) -> int:
    """Renvoie la longueur du plus long mot.
    >>> mot_le_plus_long('ecrivez une fonction qui trouve la longueur du plus long mot dans ce texte')
    8
    """
    liste = phrase.split()
    plus_grand_mot = ""
    for i in liste:
        if (len(plus_grand_mot) < len(i)):
            plus_grand_mot = i
    print(len(plus_grand_mot))

# Test
import doctest
doctest.testmod()

# Entrées
nb_lettres = int(input())
phrase = input()
if not (0 <= nb_lettres <= 200):
    raise ValueError("Trop de lettres")

# Sortie
mot_le_plus_long(phrase)