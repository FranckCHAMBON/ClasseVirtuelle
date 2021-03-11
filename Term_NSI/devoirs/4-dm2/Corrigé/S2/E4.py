"""
Prologin: Entraînement 2003
Exercice: 4 - Initiales
https://prologin.org/train/2003/semifinal/initiales
"""

def première_lettre(phrase):
    """ Cette fonction prend en paramètre une chaîne de caractères, et affiche la première lettre de chacun de ces mots, en majuscule.

    Je n'ai pas activer le test, car celui-ci faisait bugger le programme et je ne sais pas comment le rendre juste.
    #>>> première_lettre(rentre avec tes pieds)
    RATP

    """
    for lettre in liste:
        print(lettre[0].upper(), end="")

# tests
import doctest
doctest.testmod()

# Entrée
nb_caractères = int(input())  #cette variable n'a pas d'action dans le programme, elle est "passive".
phrase = input()
liste = phrase.split() 

# Sortie
première_lettre(phrase)
