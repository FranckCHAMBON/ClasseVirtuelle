"""
Prologin : Épreuve régionale 2003
Exercice : Table de multiplication
https://prologin.org/train/2003/semifinal/table_de_multiplications
"""

def table_multiplication(nb: int) -> str:
    """Cette fonction prend en paramètre un chiffre entre 1 et 9 et affiche sa table de multiplication.
    >>> 3
    3x1=3
    3x2=6
    3x3=9
    3x4=12
    3x5=15
    3x6=18
    3x7=21
    3x8=24
    3x9=27
    """
    for x in range(1, 10):
        print(str(nb) + "x" + str(x) + "=" + str(nb*x))
    
# tests 
import doctest
doctest.testmod()

# Entrée
nb = int(input())

# Sortie
table_multiplication(nb)