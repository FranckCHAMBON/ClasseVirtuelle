"""
Prologin : Épreuve régionale 2003
Exercice : Initiales
https://prologin.org/train/2003/semifinal/initiales
"""

import string
def initiales(nb_caractère: int, chaine_caractère: str) -> str:
    """Cette fonction prend en paramètre une chaîne de caractère et affiche la première lettre de chacun de ces mots en majuscule.
    >>> 21
        rentre avec tes pieds
    RATP
    """
    chaine_finale = []
    string.capwords(chaine_caractère)
    for x in range(nb_caractère-1):
        if chaine_caractère[x] == " ":
            pass
        else:
            if chaine_caractère[x] == chaine_caractère[x].upper():
                chaine_finale.append(chaine_caractère[x])
            else:
                pass
    return chaine_finale

# Entrée
nb_caractère = int(input())
chaine_caractère = input()

# Sortie
print(initiales(nb_caractère, chaine_caractère))
