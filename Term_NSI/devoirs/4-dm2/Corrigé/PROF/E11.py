"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/anagrammes
"""

def signature(mot: str) -> str:
    """Renvoie le mot avec les lettres rangées
    dans l'ordre alphabétique.
    Ainsi deux anagrammes ont la même signature.

    >>> signature("azeerty")
    'aeertyz'

    """
    mot = list(mot)
    mot.sort()
    return "".join(mot)

def nb_couples_anagrammes(n: int, phrase: str) -> int:
    """Renvoie le nombre de couples d'anagrammes formés
    à partir des mots de la chaîne.

    >>> p_début = "le chien marche vers sa niche et trouve une limace d"
    >>> p_fin = "e chine nue pleine de malice qui lui fait du charme"
    >>> phrase = p_début + p_fin
    >>> nb_couples_anagrammes(103, phrase)
    6

    """
    mots = list(set(phrase.split()))

    anagrammes = dict()
    for mot in mots:
        signe = signature(mot)
        if signe in anagrammes:
            anagrammes[signe] += 1
        else:
            anagrammes[signe] = 1

    nb_couples = 0
    for signe in anagrammes:
        q = anagrammes[signe] # q comme quantité
        nb_couples += q * (q-1) // 2
        # on ajoute le nombre de façons de choisir 2 éléments parmi q.
    return nb_couples


import doctest
doctest.testmod()

n = int(input())
phrase = input()

print(nb_couples_anagrammes(n, phrase))
