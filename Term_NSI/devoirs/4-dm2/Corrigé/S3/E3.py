"""
Prologin:  Entraînement  2003
Exercice: 3 - Grand écart
https://prologin.org/train/2003/semifinal/grand_ecart
"""
def cherche_plus_grande_diférence(nb_de_nombre: int, liste_nb):
    """cherche plus grande diférence entre deux nombre dans une liste
    >>> cherche_plus_grande_diférence(10, ['4', '2', '3', '5', '10', '6', '4', '9', '1', '3'])
    8
    """
    plus_grande_diférence = 0
    diférence = 0
    for x in range(nb_de_nombre- 1):
        if liste_nb[x] >= liste_nb[x + 1]:
            diférence = int(liste_nb[x]) - int(liste_nb[x + 1])
        else:
            diférence = int(liste_nb[x + 1]) - int(liste_nb[x])
        if diférence >= plus_grande_diférence:
            plus_grande_diférence = diférence
    return plus_grande_diférence

import doctest
doctest.testmod()

nb_de_nombre = int(input())
liste_nb = input().split()
print(cherche_plus_grande_diférence(nb_de_nombre, liste_nb))
