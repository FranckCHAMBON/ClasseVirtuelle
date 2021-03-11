"""
Prologin: Entrainement 2003
Exercice: 7 - Table de multiplication
https://prologin.org/train/2003/semifinal/table_de_multiplications
"""

def table_de_multiplications(chiffre: int) -> str:
    """Revoie la table de multiplication de l'entier demandé.
    >>> table_de_multiplications(3)
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
    for i in range(1,10): 
       print(chiffre, "x", i, "=", i*chiffre, sep="")

# Test
import doctest
doctest.testmod()

# Entrée       
chiffre = int(input())

if not (1<= chiffre <= 9):
    raise ValueError("Chiffre trop grand, il ne doit pas dépasser 9.")

# Sortie
table_de_multiplications(chiffre)