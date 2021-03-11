"""
Prologin: Entrainement 2003
Qualification : 2 - Comparer des chaînes
https://prologin.org/train/2003/qualification/comparer_des_chaines
"""

def ordre(mot1, mot2):
    """ Renvoie le premier mot selon l'ordre lexicographique.
    >>> ordre('prologin', 'prolo')
    'prolo'
    """ 
    if mot1 < mot2:
        return mot1
    else:
        return mot2

# Test
import doctest
doctest.testmod()

# Entrées
nb1 = int(input())
mot1 = input()
nb2 = int(input())
mot2= input()

if not (1< len(mot1) < 1000):
    raise ValueError("Trop de lettres au premier mot")
if not (1< len(mot2) < 1000):
    raise ValueError("Trop de lettres au deuxième mot")

# Sortie
print(ordre(mot1, mot2))