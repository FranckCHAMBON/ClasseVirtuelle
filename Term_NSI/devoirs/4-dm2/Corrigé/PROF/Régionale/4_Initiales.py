"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/initiales
"""

def majuscule(lettre: str) -> str:
    """Renvoie la version majuscule de lettre,
    lettre est donnée en minuscule.

    >>> majuscule('r')
    'R'

    """
    id_lettre = ord(lettre) - ord('a')
    lettre_maj = chr(ord('A') + id_lettre)
    return lettre_maj

def affiche_initiales(n: int, chaîne: str):
    """Affiche les initiales de la chaîne, en majuscules.

    >>> affiche_initiales(21, "rentre avec tes pieds")
    RATP

    """

    espace = True # indique si le caractère précédent est espace
    for i in range(n):
        c = chaîne[i]
        if c == ' ':
            espace = True
        elif espace:
            # `c` est une initiale
            print(majuscule(c), end="")
            espace = False
        else:
            # ni espace, ni initiale
            pass
    print()

import doctest
doctest.testmod()

n = int(input())
chaîne = input()
assert n == len(chaîne), f"Erreur {n} ≠ {len(chaîne)}"

affiche_initiales(n, chaîne)
