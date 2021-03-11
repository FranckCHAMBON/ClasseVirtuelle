"""
Prologin:  Entraînement  2003
Exercice: 6 - Nombre inpairs 
https://prologin.org/train/2003/semifinal/nombres_impairs
"""
def cherche_impair_entre_nb(premier_entier: int, deuxième_entier: int):
    """ cherche des nombre impair entre deux nombre et 
    affiche la liste de c'est nombre nombre trouver 
    >>> cherche_impair_entre_nb(42, 51)
    [43, 45, 47, 49, 51]
    """
    if premier_entier > deuxième_entier:
        raise ValueError("il faux que la première entré < deuxième entré")
    else:
        liste_impair = []
        for x in range(premier_entier, deuxième_entier + 1): #deuxième_entier + 1 car il est inclu
            if x%2 == 0:
                None
            else:
                liste_impair.append(x)
    return liste_impair

import doctest
doctest.testmod()

premier_entier, deuxième_entier = map(int, input().split())
"""
on sait que le premier indise est toujour inférieur au deuxième 
donc on sera pas oubliger de faire un test pour voir si c'est vrai 
mais la on va quand même le faire
"""
for v in cherche_impair_entre_nb(premier_entier, deuxième_entier):
    print(v, end=' ')
