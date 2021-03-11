"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/qualification/nombre_de_voyelles
"""

def nb_voyelles(longueur: int, chaîne: str) -> int:
    """Renvoie le nombre de voyelles de la chaîne.

    >>> nb_voyelles(8, "ProlOgiN")
    3
    
    """
    # Deux versions proposées
    ## version simple
    voyelles = "aeiuoyAEIOUY"
    Q_voyelles = len(voyelles)
    réponse = 0
    for i in range(longueur):
        for j in range(Q_voyelles):
            if chaîne[i] == voyelles[j]:
                réponse += 1
    return réponse

    ## version fonctionnelle ; 1 ligne !
    #return sum(1 for c in chaîne if c in "aeiuoyAEIOUY")
    

import doctest
doctest.testmod()

longueur = int(input())
chaîne = input()
assert longueur == len(chaîne), f"Erreur {longueur} ≠ {len(chaîne)}"

print(nb_voyelles(longueur, chaîne))
