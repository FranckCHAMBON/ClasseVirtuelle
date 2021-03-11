"""
Prologin: Qualification 2003
Exercice 4 - Nombre de voyelles
https://prologin.org/train/2003/qualification/nombre_de_voyelles
"""

# 0- Coeur du programme

def nombre_voyelles(nb_lettres: int, chaîne_mot: str) -> int:
    """ Renvoie le nombre de voyelles de chaîne_mot.
    >>> nombre_voyelles(11, "hello world")
    3
    >>> nombre_voyelles(8, "prologin")
    3
    """

    compteur = 0
    voyelles = ["a","e","i","o","u","y"]
    for lettre in chaîne_mot:               # On vérifie pour chaque lettre de chaîne_mot si elle se trouve dans voyelles
        if lettre in voyelles:
            compteur += 1                   # Si oui, on rajoute 1 au compteur
    return compteur                         # A la fin, on renvoie le compteur

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture des entrées

nb_lettres = int(input())
chaîne_mot = input().lower()

# 3- Appel de la fonction / Sortie

print(nombre_voyelles(nb_lettres, chaîne_mot))
