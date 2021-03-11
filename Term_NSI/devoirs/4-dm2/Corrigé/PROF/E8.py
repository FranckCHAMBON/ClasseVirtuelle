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
    def est_dans_grille(i: int, j: int) -> bool:
        return (0 <= i < 6) and (0 <= j < 7)
    
    def teste_en(i: int, j: int) -> str:
        """Renvoie "1" ou "2" si un gagnant est trouvé en partant de (i, j),
        sinon renvoie "0".
        """
        if grille[i][j] == "0":
            return "0"
        vecteurs = [
                    (0, 1), # horizontal
                    (1, 0), # vertical
                    (1, 1), # diagonal 1
                    (1, -1) # diagonal 2
                ]
        for di, dj in vecteurs:
            if est_dans_grille(i + 3*di, j + 3*dj):
                if (grille[i][j] == grille[i + di][j + dj] ==
                    grille[i + 2*di][j + 2*dj] == grille[i + 3*di][j + 3*dj]):
                        return grille[i][j]
        return "0"
    
    for i in range(6):
        for j in range(7):
            candidat = teste_en(i, j)
            if candidat != "0":
                return candidat
    return "0"


import doctest
doctest.testmod()

grille = [input() for _ in range(6)]

print(gagnant_puiss4(grille))
