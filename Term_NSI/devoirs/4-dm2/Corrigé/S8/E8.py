"""
Prologin : Épreuve régionale 2003
Exercice : Puissance 4
https://prologin.org/train/2003/semifinal/puissance_4
"""

def puissance4(table_puissance4: list) -> int:
    """Cette fonction prend en paramètre un tableau d'entiers à deux dimensions contenant 42 cases
    (6 lignes, 7 colonnes). Une case de ce tableau contient soit 0 (case vide) soit 1 (pion jaune), soit 2 (pion rouge). 
    Et doit renvoyer 1 ou 2 s'il y a un alignement de 4 pions et 0 si personne n'a gagné.
    >>> 0010000
        0022000
        0121000
        0221000
        2212100
        1211210
    2
    """
    for x in range(6):
        for n in range(4):
            ## Vérif horizontale ##
            if table_puissance4[x][n] == table_puissance4[x][n+1] == table_puissance4[x][n+2] == table_puissance4[x][n+3]:
                if table_puissance4[x][n] == 0:
                    pass
                else:
                    return table_puissance4[x][n]
            ## Vérif verticale ##
            elif table_puissance4[n][x] == table_puissance4[n+1][x] == table_puissance4[n+2][x] == table_puissance4[n+3][x]:
                if table_puissance4[x][n] == 0:
                    pass
                else:
                    return table_puissance4[x][n]
                ## Vérif diagonale droite gauche ##
                elif table_puissance4[x][n] == table_puissance4[x+1][n+1] == table_puissance4[x+2][n+2] == table_puissance4[x+3][n+3]:
                    if table_puissance4[x][n] == 0:
                        pass
                    else:
                        return table_puissance4[x][n]
                ## Vérif diagonale gauche droite ##
                elif table_puissance4[x][6-n] == table_puissance4[x+1][5-n] == table_puissance4[x+2][4-n] == table_puissance4[x+3][3-n]:
                    if table_puissance4[x][n] == 0:
                        pass
                    else:
                        return table_puissance4[x][n]
                else:
                    return 0

# Entrée
table_puissance4 = [input() for _ in range(6)]

# Sortie
print(puissance4(table_puissance4))