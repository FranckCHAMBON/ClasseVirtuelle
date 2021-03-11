""" 
Prologin: Entraînement 2003
Exercice: 7 - Table de Multiplication
https://prologin.org/train/2003/semifinal/table_de_multiplications
"""

def table_de_multiplication(chiffre:int):
    """Renvoie la table de multiplication du chiffre donné partant de 1 jusqu'à 9 dans une liste
    >>> table_de_multiplication(4)
    ['4x1=4', '4x2=8', '4x3=12', '4x4=16', '4x5=20', '4x6=24', '4x7=28', '4x8=32', '4x9=36']
    >>> table_de_multiplication(8)
    ['8x1=8', '8x2=16', '8x3=24', '8x4=32', '8x5=40', '8x6=48', '8x7=56', '8x8=64', '8x9=72']

    """
    affichage = []
    for x in range(1,10):    
        affichage.append(f'{chiffre}x{x}={chiffre * x}')
    return affichage

# tests
import doctest
doctest.testmod()

# Entrée
chiffre = int(input())

# Sortie
affichage = table_de_multiplication(chiffre)
for multiplication in affichage:
    print(multiplication)

