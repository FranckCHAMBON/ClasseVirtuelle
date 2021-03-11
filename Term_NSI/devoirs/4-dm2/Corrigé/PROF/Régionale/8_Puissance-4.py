"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/puissance_4
"""

def gagnant_puiss4(grille: list) -> str:
    """Renvoie le gagnant au jeu de Puissance 4.
    * '0' désigne une case vide, et aussi un match nul.
    
    >>> l_1 = "0010000"
    >>> l_2 = "0022000"
    >>> l_3 = "0121000"
    >>> l_4 = "0221000"
    >>> l_5 = "2212100"
    >>> l_6 = "1211210"
    >>> grille = [l_1, l_2, l_3, l_4, l_5, l_6]
    >>> gagnant_puiss4(grille)
    '2'

    """
    #test horizontal
    for i in range(6):
        for j in range(7-4):
            if grille[i][j] != "0":
                if all(grille[i][j+k] == grille[i][j] for k in range(1, 4)):
                    return grille[i][j]
    #test vertical
    for i in range(6-4):
        for j in range(7):
            if grille[i][j] != "0":
                if all(grille[i+k][j] == grille[i][j] for k in range(1, 4)):
                    return grille[i][j]
    #test diagonal1
    for i in range(6-4):
        for j in range(7-4):
            if grille[i][j] != "0":
                if all(grille[i+k][j+k] == grille[i][j] for k in range(1, 4)):
                    return grille[i][j]
    #test diagonal2
    for i in range(4, 6):
        for j in range(7-4):
            if grille[i][j] != "0":
                if all(grille[i-k][j+k] == grille[i][j] for k in range(1, 4)):
                    return grille[i][j]
    #sinon, c'est perdu
    return "0"


import doctest
doctest.testmod()

grille = [input() for _ in range(6)]
for i in range(6):
    assert len(grille[i]) == 7, f"Erreur ligne{i} : {grille[i]}"

print(gagnant_puiss4(grille))
