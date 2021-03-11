"""
Prologin: Entraînement 2003
Exercice 7 - Table de multiplication
https://prologin.org/train/2003/semifinal/table_de_multiplications
"""

# 0- Coeur du programme

def construction_table_de_multiplication_de(chiffre: int) -> str:
    """ Renvoie la table de multiplication de chiffre.
    >>> construction_table_de_multiplication_de(1)
    '1x1=1\\n1x2=2\\n1x3=3\\n1x4=4\\n1x5=5\\n1x6=6\\n1x7=7\\n1x8=8\\n1x9=9\\n'
    >>> construction_table_de_multiplication_de(3)
    '3x1=3\\n3x2=6\\n3x3=9\\n3x4=12\\n3x5=15\\n3x6=18\\n3x7=21\\n3x8=24\\n3x9=27\\n'
    """

    table_de_multiplication = ""
    for multiplicateur in range(1,10):
        table_de_multiplication += str(chiffre) + "x" + str(multiplicateur) + "=" + str(chiffre * multiplicateur) + "\n"
    return table_de_multiplication

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture de l'entrée

chiffre = int(input())

# 3- Appel de la fonction / Sortie

print(construction_table_de_multiplication_de(chiffre))