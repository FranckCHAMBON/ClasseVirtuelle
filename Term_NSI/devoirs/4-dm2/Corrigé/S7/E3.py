""" 
Prologin: Entraînement 2003
Exercice: 3 - Grand écart
https://prologin.org/train/2003/semifinal/grand_ecart
"""

def Plus_grand_écart(nb_nombres : int,liste_nombres : list) -> int:
    """
    Prend en paramètre le nombre de nombres "nb_nombres" et une liste de nombres "liste_nombres" puis, 
    la fonction recherche et renvoie, la plus grande différence (en valeur absolue),
    entre un élément et son successeur (l'élément suivant dans le tableau).
    >>> Plus_grand_écart(10,[4,2,3,5,10,6,4,9,1,3])
    8
    >>> Plus_grand_écart(7,[17,5,3,5,10,6,9])
    12
    """
    écart_max = 0
    for x in range(nb_nombres-1):
        écart = abs(liste_nombres[x] - liste_nombres[x+1]) 

        if écart > écart_max:
            écart_max = écart
        else: 
            pass
    return écart_max

# tests
import doctest
doctest.testmod()

# Entrée
nb_nombres = int(input())
liste_nombres = list(map(int,input().split()))
# Sortie
print(Plus_grand_écart(nb_nombres,liste_nombres))



