"""
Prologin: Entraînement 2003
Exercice: 2 - Escalier
https://prologin.org/train/2003/semifinal/escalier
"""

nombre_marches = int(input())
escalier = ""

def donne_ligne(longueur: int) -> str:
    """
    Renvoie une chaîne de charactères correspondant à "X" fois  `longueur`
    et le rajout, à la fin de `\n`
    >>> donne_ligne(5)
    'XXXXX\n'
    >>> donne_ligne(0)
    ''
    """
    ligne = "".join("X" for _ in range(longueur))
    return ligne + "\n"

for hauteur in range(nombre_marches):
    escalier += donne_ligne(hauteur+1)

print(escalier)