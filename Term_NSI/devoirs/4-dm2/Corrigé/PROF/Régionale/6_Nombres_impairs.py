"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/nombres_impairs
"""

def affiche_impairs(n: int, m: int) -> None:
    """Affiche les nombres impairs entre `n` et `m` inclus.

    >>> affiche_impairs(42, 51)
    43 45 47 49 51

    """

    # Trois versions proposées
    ## Version itérative classique
    i = n
    if i % 2 == 0:
        i += 1
    while i <= m:
        print(i, end=" ")
        i += 2
    print()

    ## Version fonctionnelle ; 1 ligne
    #print(" ".join(map(str, range(n - n%2 + 1, m + 1, 2))))

    ## Autre version fonctionnelle, avec *unpack* ; hors programme
    #impairs = list(range(n - n%2 + 1, m + 1, 2))
    #print(*impairs)


import doctest
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
# Cette option permet de passer les tests même si
# des espaces en trop sont ajoutés en fin de ligne.

n, m = map(int, input().split())
assert n <= m

affiche_impairs(n, m)
