""" 
Prologin: Entraînement 2003
Exercice: 4 - Initiales
https://prologin.org/train/2003/semifinal/initiales
"""
def initiales(chaîne_caractère : str) -> str:
    """ Renvoie les Initiales d'une chaîne de caractère
    >>> initiales("oui bonjour")
    'OB'
    >>> initiales("je suis pas là")
    'JSPL'
    """
    liste_chaîne = list(chaîne_caractère.split())
    initiale = ""

    for x in range(len(liste_chaîne)):
        initiale += liste_chaîne[x][0].upper()
    
    return initiale

# tests
import doctest
doctest.testmod()

# Entrée
nb_caractères = int(input())
chaîne_caractère = input()
# Sortie
print(initiales(chaîne_caractère))
