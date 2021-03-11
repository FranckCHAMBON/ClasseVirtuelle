"""
Prologin: Entraînement 2003
Exercice: 10 - Anagrammes 
https://prologin.org/train/2003/semifinal/anagrammes
"""

def nb_anagramme(texte : str) :
    """ Renvoie le nombre de couples d'anagrammes formés à partir des mots de la chaîne.

    >>> texte = 'le chien marche vers sa niche et trouve une limace de chine nue pleine de malice qui lui fait du charme'
    >>> nb_anagramme(texte)
    6

    """
    stock = []
    parallèle = []
    for mot in texte :
        contenu = sorted(list(mot))
        stock.append(contenu)
    #écriture fonctionnelle syntaxiquement incorrecte mais intention :
    #compteur si couple anagramme = doublon de contenu du mot :
    #return sum(1 for élément in stock if élément in parallèle else parallèle.append(élément))
    somme = 0
    for élément in stock :
        if élément not in parallèle :
            parallèle.append(élément)
        else :
            somme += 1
    return somme

# tests
import doctest
doctest.testmod()

# Entrée
nb_caractères = int(input())
assert 1 <= nb_caractères <= 200
texte = input().split()

# Sortie
print (nb_anagramme(texte))