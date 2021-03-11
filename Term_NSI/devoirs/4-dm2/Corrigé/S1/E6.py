"""
Prologin: Entraînement 2003
Exercice 6 - Nombres impairs
https://prologin.org/train/2003/semifinal/nombres_impairs
"""

# 0- Coeur du programme

def nombres_impairs_entre(nombre1: int, nombre2: int) -> str:
    """ Renvoie tous les nombres impairs se trouvant entre nombre1 et nombre2 dans l'ordre croissant.
    >>> nombres_impairs_entre(1, 3)
    '1 3'
    >>> nombres_impairs_entre(42, 51)
    '43 45 47 49 51'
    """

    entiers_impairs = ""
    if nombre1 % 2 == 1:
        # Si nombre1 est impair, on renvoie tous les nombres entre nombre1 et nombre2 inclus avec un pas de 2                    
        for x in range(nombre1, nombre2+1, 2):
            entiers_impairs += str(x) + " "
    else:
        # Si nombre1 est pair, on renvoie tous les nombres entre nombre1 exclus et nombre2 inclus avec un pas de 2    
        for x in range(nombre1+1, nombre2+1, 2):
            entiers_impairs += str(x) + " "
    return entiers_impairs.strip()

    #Variante:
    #entiers_impairs = [str(x) for x in range(nombre1,nombre2+1) if x%2 == 1]
    #return " ".join(entiers_impairs)

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture de l'entrée

nombre1, nombre2 = map(int,input().split())

# 3- Appel de la fonction / Sortie

print(nombres_impairs_entre(nombre1, nombre2))
