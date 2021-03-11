"""
Prologin: Qualification 2003
Exercice: 2 - Comparer des chaînes
https://prologin.org/train/2003/qualification/comparer_des_chaines
"""

def première_chaîne(nb_caracteres_1 : int, chaîne_1 : str, nb_caracteres_2 : int, chaîne_2 : str,) -> str :
    """ Renvoie la première chaîne de caractère selon l'ordre lexicographique
    entre 'chaîne_1' et 'chaîne_2'.
    >>> nb_caracteres_1 = 8
    >>> chaîne_1 = prologin
    >>> nb_caracteres_2 = 5
    >>> chaîne_2 = prolo
    prolo
    """
    longueur_max = max(len(chaîne_1), len(chaîne_2))
    mot1, mot2 = list(chaîne_1), list(chaîne_2)
    sortie = ''
    for lettre in range (longueur_max) :
        if mot1[lettre] > mot2[lettre] :
            sortie.append(chaîne_2) 
            break
        if mot1[lettre] < mot2[lettre] :
            sortie.append(chaîne_1) 
            break
        if mot1[lettre] == ' ' :
            sortie.append(chaîne_1) 
            break
        if mot2[lettre] == ' ' :
            sortie.append(chaîne_2) 
            break
        return sortie

# tests
import doctest
doctest.testmod()

# Entrée
nb_caracteres_1 = int(input())
chaîne_1 = input()
nb_caracteres_2 = int(input())
chaîne_2 = input()

# Sortie
print(première_chaîne(nb_caracteres_1, chaîne_2, nb_caracteres_2, chaîne_2))