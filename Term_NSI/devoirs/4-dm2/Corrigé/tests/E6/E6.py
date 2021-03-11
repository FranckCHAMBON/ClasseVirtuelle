"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/nombres_impairs
"""

def nombres_impairs(n: int, m: int) -> list:
    """Renvoie la liste des nombres impairs entre `n` et `m` inclus.

    >>> nombres_impairs(42, 51)
    [43, 45, 47, 49, 51]

    """

    liste = []
    i = n
    if i % 2 == 0:
        i += 1
    while i <= m:
        liste.append(i)
        i += 2
    return liste


import doctest
doctest.testmod()

n, m = map(int, input().split())

impairs = nombres_impairs(n, m)
print(" ".join(map(str, impairs)))
