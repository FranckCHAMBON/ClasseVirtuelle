"""
Prologin: Entrainement 2003
Exercice: 3 - Grand Ecart
https://prologin.org/train/2003/semifinal/grand_ecart
"""

def plus_grand_ecart(liste, nb_entier):
    """Renvoie le plus grand ecart entre deux nombre d'une liste
    >>> plus_grand_ecart([4, 2, 3, 5, 10, 6, 4, 9, 1, 3,], 10 )
    8
    """
    i = 0
    maximum = 0
    while i < nb_entier-1:
        ecart = abs(liste[i] - liste[i+1])
        if ecart>maximum:
            maximum = ecart
        i += 1
    return maximum

# Test
import doctest
doctest.testmod()

# Entrées
nb_entier = int(input())
liste = input().split(" ")
liste_entier = []
 
for i in liste:
    liste_entier.append(int(i))

# Sortie
print(plus_grand_ecart(liste_entier, nb_entier))

