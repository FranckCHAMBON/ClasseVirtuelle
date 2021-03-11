"""
Prologin: Entrainement 2003
Qualification : 4 - Nombre de voyelles 
https://prologin.org/train/2003/qualification/nombre_de_voyelles
"""

def voyelles(mot):
    """ Renvoie le nom de voyelle dans une chaîne de caractère.
    >>> voyelles("Prologin")
    3
    """
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    nb_voyelles = sum(1 for lettre in mot if lettre in voyelles )
    return nb_voyelles

# Test
import doctest
doctest.testmod()

# Entrées
nb_lettre = int(input())
mot = input().lower()

if not (0 <= nb_lettre <= 10000):
    raise ValueError("Trop de caractères")

# Sortie
print(voyelles(mot))