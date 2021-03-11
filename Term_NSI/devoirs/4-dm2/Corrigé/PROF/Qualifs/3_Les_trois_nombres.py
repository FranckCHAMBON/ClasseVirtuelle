"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/qualification/les_trois_nombres
"""

def égal_somme_deux_autres(n_1: int, n_2: int, n_3: int) -> int:
    """Renvoie le nombre si égal à la somme des autres,
    sinon renvoie 0.

    >>> égal_somme_deux_autres(18, 42, 24)
    42

    >>> égal_somme_deux_autres(11, 37, 18)
    0

    """
    liste = [n_1, n_2, n_3]
    total = sum(liste)
    for n in liste:
        if n == total - n:
            return n
    return 0

n_1, n_2, n_3 = map(int, input().split())
print(égal_somme_deux_autres(n_1, n_2, n_3))
