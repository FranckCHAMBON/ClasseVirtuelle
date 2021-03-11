"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/mot_le_plus_long
"""

def longueur_plus_long_mot(n: int, chaîne: str) -> int:
    """Renvoie la longueur du mot le plus long.
    
    >>> longueur_plus_long_mot(74, \
"ecrivez une fonction qui trouve la longueur du plus long mot dans ce texte")
    8

    """
    # Deux versions proposées

    ## Version itérative classique
    longueur_max = 0
    longueur = 0
    for i in range(n + 1): # Oui, n+1.
        if (i == n) or (chaîne[i] == ' '):
            # ce test permet de tester aussi le dernier mot
            # tout en factorisant le code
            if longueur_max < longueur:
                longueur_max = longueur
            longueur = 0
        else:
            longueur += 1

    return longueur_max

    ## version fonctionnelle ; 1 ligne
    #return max(map(len, chaîne.split()))


import doctest
doctest.testmod()

n = int(input())
chaîne = input()
assert n == len(chaîne), f"Erreur {n} ≠ {len(chaîne)}"

print(longueur_plus_long_mot(n, chaîne))

