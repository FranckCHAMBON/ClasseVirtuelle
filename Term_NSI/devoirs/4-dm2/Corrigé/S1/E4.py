"""
Prologin: Entraînement 2003
Exercice 4 - Initiales
https://prologin.org/train/2003/semifinal/initiales
"""

# 0- Coeur du programme

def construire_initiales(nb_lettres: int, chaîne_mots: list) -> str:
    """ Renvoie la première lettre de chacun des mots de chaîne_mots
    >>> construire_initiales(11, ["Hello","World"])
    'HW'
    >>> construire_initiales(21, ["rentre", "avec", "tes", "pieds"])
    'RATP'
    """

    initiales = ""
    for mot in chaîne_mots:
        initiales += mot[0].upper()
    return initiales

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture des entrées

nb_lettres = int(input())
chaîne_mots = input().split()

# 3- Appel de la fonction / Sortie

print(construire_initiales(nb_lettres, chaîne_mots))
