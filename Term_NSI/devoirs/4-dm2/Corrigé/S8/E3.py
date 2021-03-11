"""
Prologin : Épreuve régionale 2003
Exercice : Grand écart
https://prologin.org/train/2003/semifinal/grand_ecart
"""

def ecart(nb_tableau: int, tableau: int) -> int:
    """Cette fonction prend en paramètre un tableau de nombres entiers, et qui recherche, dans ce tableau, la plus grande différence, 
    entre un élément et son successeur et renvoie cette différence.
    >>> 10
        [4, 2, 3, 5, 10, 6, 4, 9, 1, 3]
    8
    """
    grand_ecart = 0
    for x in range(nb_tableau):
        if x == nb_tableau - 1:
            break
        else:
            ecart = tableau[x] - tableau[x+1]
            if ecart > grand_ecart:
                grand_ecart = ecart
    return grand_ecart


# Entrée
nb_tableau = int(input())
tableau = list(map(int, input().split()))

# Sortie
print(ecart(nb_tableau, tableau))
