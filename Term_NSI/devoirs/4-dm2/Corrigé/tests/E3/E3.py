"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/grand_ecart
"""

def grand_écart(n: int, tableau: list):
    """Renvoie le plus grand écart entre un élément et son successeur.

    >>> grand_écart(10, [4, 2, 3, 5, 10, 6, 4, 9, 1, 3])
    8

    """
    écart_max = 0
    for i in range(n - 1):
        écart = abs(tableau[i] - tableau[i + 1])
        if écart_max < écart:
            écart_max = écart
    return écart_max


import doctest
doctest.testmod()

n = int(input())
tableau = list(map(int, input().split()))

print(grand_écart(n, tableau))
