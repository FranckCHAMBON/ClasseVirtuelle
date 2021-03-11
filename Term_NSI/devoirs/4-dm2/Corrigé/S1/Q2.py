"""
Prologin: Qualification 2003
Exercice 2 - Comparer des chaînes
https://prologin.org/train/2003/qualification/comparer_des_chaines
"""

# 0- Coeur du programme

def comparaison(longueur_1: int, chaîne_1: str, longueur_2: int, chaîne_2:str) -> str:
    """ Renvoie le premier mot entre chaîne_1 et chaîne_2 dans l'ordre lexicographique
    >>> comparaison(8, "prologin", 5, "prolo")
    'prolo'
    >>> comparaison(4, "toto", 4, "titi")
    'titi'
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"                     
    id_lettre = 0 
    while longueur_1 != id_lettre and longueur_2 != id_lettre:  # On continue tant que les chaînes ont encore des lettres .
        if chaîne_1[id_lettre] != chaîne_2[id_lettre]:          # Si, les 2 lettres des 2 chaînes sont différentes alors, 
            for lettre in alphabet:                             # On peut déterminer le premier avec l'ordre de l'alphabet.
                if chaîne_1[id_lettre] == lettre:              
                    return chaîne_1
                if chaîne_2[id_lettre] == lettre:
                    return chaîne_2
        id_lettre += 1
    if longueur_1 == id_lettre:                                 # Les 2 chaînes n'ont pas la même longueur
        return chaîne_1                                         # Donc,celui qui a arrêté la boucle est le premier et a une longueur égale à id_lettre
    else:
        return chaîne_2

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture des entrées

longueur_1 = int(input())
chaîne_1 = input()
longueur_2 = int(input())
chaîne_2 = input()

# 3- Appel de la fonction / Sortie

print(comparaison(longueur_1, chaîne_1, longueur_2, chaîne_2))