"""
Prologin: Entraînement 2003
Exercice: 7 - Table de multiplication
https://prologin.org/train/2003/semifinal/table_de_multiplications
"""

# Fonction avec multiplication
def table_multiplication(nb_réf : int) -> str :
    """ Renvoie la table de multiplication du 'nb_réf' (de 1 jusqu'à 9)'.
    
    >>> chiffre = 3
    >>> table_multiplication(chiffre)
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
    longueur_table = 9
    début, fin = 1, 9
    for nb in range (début, fin+1) :
        résultat = nb_réf * nb
        structure = [str(nb_réf), "x", str(nb), "=", str(résultat)]
        print("".join(structure))

# OU avec addition
"""
    longueur_table = 9
    résultat = nb_réf
    multiplication = "x"
    égal = "="
    début, fin = 1, 9
    for nb in range (début, fin+1) :
        structure = [str(nb_réf), multiplication, str(nb), égal, str(résultat)]
        print("".join(structure))
        résultat += nb_réf
"""

# tests
import doctest
doctest.testmod()

# Entrée
chiffre = int(input())
assert 1 <= chiffre <= 9

# Sortie
table_multiplication(chiffre)