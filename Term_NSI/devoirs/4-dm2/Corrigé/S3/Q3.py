"""
Prologin: Qualification 2003
Exercice: 3 - les trois nombre 
https://prologin.org/train/2003/qualification/les_trois_nombres
"""
def vérif_a_somme(nb_1, nb_2, nb_3, somme):
    """ vérifie si dans la liste(où il y a imparativemant que 3 chiffre) il existe une somme dans la lisste
    si on addicione les 2 autre nombre
    >>> vérif_a_somme(18, 24, 6, 0)
    24
    """ 
    if (nb_1 + nb_2) == nb_3:
        return nb_3
    elif (nb_2 + nb_3) == nb_1:
        return nb_1
    elif (nb_1 + nb_3) == nb_2:
        return nb_2
    else:
        return 0

import doctest
doctest.testmod()

nb_1, nb_2, nb_3 = map(int, input().split())
somme = 0
print(vérif_a_somme(nb_1, nb_2, nb_3, somme))



"""
"on peut faire aussi se code et sa marche aussi" 
def vérif_a_somme(liste_nb, somme: int):
    " vérifie si dans la liste(où il y a imparativemant que 3 chiffre) il existe une somme dans la lisste
    si on addicione les 2 autre nombre 
    >>> vérif_a_somme(['18', '42', '24'], 0)
    '42'
    >>> vérif_a_somme(['1', '100', '5'], 0)
    0
    " 
    liste_nb.sort()
    somme = int(liste_nb[0]) + int(liste_nb[1])
    if somme == int(liste_nb[2]):
        return liste_nb[2]
    else:
        return 0

import doctest
doctest.testmod()

liste_nb = list(map(int, input().split(" ")))
somme = 0
print(vérif_a_somme(liste_nb, somme))
"""
