"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/table_de_multiplications
"""

def affiche_table(nombre: int) -> None:
    """Affiche la table de multiplication de `nombre`

    >>> affiche_table(3)
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
    for k in range(1, 10):
        ## Version classique
        #print(nombre, "x", k, "=", k * nombre, sep="")

        ## Version f-string ; recommandée
        print(f"{nombre}x{k}={k * nombre}")


import doctest
doctest.testmod()

nombre = int(input())
assert 1 <= nombre <= 9, f"Erreur, {nombre=}"

affiche_table(nombre)
