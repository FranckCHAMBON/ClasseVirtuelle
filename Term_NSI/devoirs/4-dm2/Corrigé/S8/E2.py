"""
Prologin : Épreuve régionale 2003
Exercice : Escalier
https://prologin.org/train/2003/semifinal/escalier
"""

def escalier(nb_marche: int) -> str:
    """Cette fonction prend en paramètre un entier positif, et affiche un escalier, rempli du caractère X. 
    L'entier placé en paramètre indique donc le nombre de marches.
    >>> 4
    X
    XX
    XXX
    XXXX
    """
    for x in range(1, nb_marche + 1):
        print("X"*x)

# tests

# Entrée
nb_marche = int(input())

# Sortie
escalier(nb_marche)