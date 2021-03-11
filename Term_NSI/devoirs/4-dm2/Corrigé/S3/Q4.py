"""
Prologin: Qualification 2003
Exercice: 4 - Nombre de voyelle
https://prologin.org/train/2003/qualification/nombre_de_voyelles
"""
def cherche_nb_voyelle(chaine_caractère, liste_voyelle, nb_voyelle: int):
    """ cherche le nombre de voyelle dans un mots ou phrase
    >>> cherche_nb_voyelle('prologin', ['a', 'o', 'u', 'y', 'e', 'i'], 0)
    3
    """
    for x in chaine_caractère: 
        for y in liste_voyelle:
            if x == y :
                nb_voyelle += 1
    return nb_voyelle

import doctest
doctest.testmod()

nb_caractère = int(input())
chaine_caractère = input().lower()
nb_voyelle = 0
liste_voyelle = ['a', 'o', 'u', 'y', 'e', 'i']
print(cherche_nb_voyelle(chaine_caractère, liste_voyelle, nb_voyelle))
