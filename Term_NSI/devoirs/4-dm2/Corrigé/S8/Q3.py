"""
Prologin : Qualification 2003
Exercice : Les trois nombres
https://prologin.org/train/2003/qualification/les_trois_nombres
"""

def somme(nb1: int, nb2: int, nb3: int) -> int:
    """Cette fonction prend en paramètre 3 entiers non nuls. Cette fonctionne doit déterminer si l'un d'eux est égal à la
    somme des deux autres, sinon la fonction renvoie 0.
    >>> 18 42 24
    42
    >>> 11 37 18
    0
    """
    for x in range(3):
        if nb1 + nb2 == nb3:
            return nb3
        elif nb2 + nb3 == nb1:
            return nb1
        elif nb1 + nb3 == nb2: 
            return nb2
        else: 
            return 0

# Entrée
nb1, nb2, nb3 = map(int, input().split())

# Sortie
print(somme(nb1, nb2, nb3))