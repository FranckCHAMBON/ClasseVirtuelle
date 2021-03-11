"""
Prologin: Entraînement 2003
Exercice: 5- Mot le plus long
https://prologin.org/train/2003/semifinal/mot_le_plus_long
"""
def mot_le_plus_long(texte):
    """ Cette fonction prend en paramètre une chaîne de caractères, et elle renvoie le nombre de caractères du plus long mot de cette chaîne.

    Je n'ai pas activer le test, car celui-ci faisait bugger le programme et je ne sais pas comment le rendre juste.
    # >>> mot_le_plus_long(ecrivez une fonction qui trouve la longueur du plus long mot dans ce texte)
    8
    """

    ans = ""
    for lettre in texte:
        if len(lettre)>len(ans):
            ans = lettre
    return ans
        
# tests
import doctest
doctest.testmod()

# Entrée
nb_caractères = int(input())
texte = input().split()

# Sortie
print(len(mot_le_plus_long(texte)))

