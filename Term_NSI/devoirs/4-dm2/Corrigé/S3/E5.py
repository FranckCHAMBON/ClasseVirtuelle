"""
Prologin:  Entraînement  2003
Exercice: 5 - mot le plus long
https://prologin.org/train/2003/semifinal/mot_le_plus_long
"""
def cherche_mot_long(nb_caractère: int, phrase):
    """ trouve le mot le plus long dans la phrase 
    et renvoie le nombre du plus grand caractère 
    >>> cherche_mot_long(74, ['ecrivez', 'une', 'fonction', 'qui', 'trouve', 'la', 'longueur', 'du', 'plus', 'long', 'mot', 'dans', 'ce', 'texte'])
    8
    """
    if nb_caractère > 200:
        raise ValueError("nombre de caractère trop grand")
    else:
        longeur_mot = len(phrase[0])
        for x in phrase:
            if len(x) >= longeur_mot:
                longeur_mot = len(x)
        return longeur_mot
        
import doctest
doctest.testmod()

nb_caractère = int(input())
phrase = input().split()
print(cherche_mot_long(nb_caractère, phrase))
