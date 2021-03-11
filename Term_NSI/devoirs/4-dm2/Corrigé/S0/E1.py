"""
Prologin: Entraînement 2003
Exercice: 1 - 42
https://prologin.org/train/2003/semifinal/42
"""

def réponse(question_universelle = 42) :
    """ Renvoie l'entier qui répond à la 'question_universelle'.

    >>> réponse(question_universelle = 42)
    42
    
    """
    return question_universelle

# tests
import doctest
doctest.testmod()

# Sortie
print (réponse(question_universelle = 42))