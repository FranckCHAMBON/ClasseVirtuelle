"""
Prologin : Qualification 2003
Exercice : Nombre de voyelles
https://prologin.org/train/2003/qualification/nombre_de_voyelles
"""

def nombre_de_voyelles(nb_caractère: int, mot: str) -> int:
    """Cette fonction prend en paramètre une chaîne de caractères majuscules et minuscules sans accents et le nombre de caractère.
    Cette fonction renvoie le nombre de voyelles qu'elle contient.
    >>> 8
        ProlOgin
    3
    """
    mot = mot.lower()
    nombre_voyelles = 0
    liste_voyelles = ["a","e","i","o","u","y"] 
    for x in range(nb_caractère):
        if mot[x] in liste_voyelles:
            nombre_voyelles += 1
    return nombre_voyelles

# tests 
import doctest
doctest.testmod()

# Entrée
nb_caractère = int(input())
mot = input()

# Sortie
print(nombre_de_voyelles(nb_caractère, mot))