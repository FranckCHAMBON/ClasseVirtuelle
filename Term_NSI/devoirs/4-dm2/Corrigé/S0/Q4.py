"""
Prologin: Qualification 2003
Exercice: 4 - Nombre de voyelles
https://prologin.org/train/2003/qualification/nombre_de_voyelles
"""

def nb_voyelles(texte : str) -> int :
    """ Renvoie le nombre de voyelles que la chaîne de caractères 'texte' contient.

    >>> nb_caractères = 8
    >>> texte = 'ProlOgiN'
    >>> nb_voyelles(texte)
    3

    """
    voyelles = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
    texte = list(texte)
    return sum(1 for lettre in texte if lettre in voyelles)

# tests
import doctest
doctest.testmod()

# Entrée
nb_caractères = int(input())
assert 1 <= nb_caractères <= 10000
texte = input()

# Sortie
print(nb_voyelles(texte))