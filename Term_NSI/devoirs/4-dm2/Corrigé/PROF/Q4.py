"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/qualification/nombre_de_voyelles
"""

def nb_voyelles(longueur: int, chaîne: str) -> int:
    """Renvoie le nombre de voyelles de la chaîne.

    >>> nb_voyelles(8, "ProlOgiN")
    3
    
    """
    voyelles = "aeiuoyAEIOUY"
    Q_voyelles = len(voyelles)
    réponse = 0
    for i in range(longueur):
        for j in range(Q_voyelles):
            if chaîne[i] == voyelles[j]:
                réponse += 1
    return réponse


import doctest
doctest.testmod()

longueur = int(input())
chaîne = input()

print(nb_voyelles(longueur, chaîne))
