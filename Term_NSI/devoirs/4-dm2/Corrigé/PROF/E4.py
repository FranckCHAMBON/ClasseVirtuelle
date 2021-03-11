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


def initiales(n: int, chaîne: str) -> str:
    """Renvoie les initiales de la chaîne, en majuscules.

    >>> initiales(21, "rentre avec tes pieds")
    'RATP'

    """

    sigle = [majuscule(chaîne[0])]
    for i in range(1, n):
        if chaîne[i - 1] == ' ':
            if chaîne[i] != ' ':
                sigle.append(majuscule(chaîne[i]))
    return "".join(sigle)


import doctest
doctest.testmod()

n = int(input())
chaîne = input()

print(initiales(n, chaîne))
