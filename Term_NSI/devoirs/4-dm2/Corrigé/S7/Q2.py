""" 
Prologin: Qualification 2003
Exercice: 2 - Comparer des chaînes 
https://prologin.org/train/2003/qualification/comparer_des_chaines
"""
import itertools 
def comparaison_lexicographique(chaîne1:str,chaîne2:str) -> str:
    """ Prend 2 chaînes de caractères en minuscule et renvoie la plus petite selon l'ordre lexicographique
    >>> comparaison_lexicographique('bonjour','hola')
    'bonjour'
    >>> comparaison_lexicographique('holaster','hola')
    'hola'
    """
    alphabet = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v','w','x', 'y', 'z']
    liste_chaîne1 = list(chaîne1)
    liste_chaîne2 = list(chaîne2)

    # On fait un tupple de chaque lettre de même rang dans chaque chaîne et puis on l'insère dans une liste,ça permet d'éviter les problèmes de taille
    liste_comparaison = list(zip(liste_chaîne1,liste_chaîne2))

    # On compare chaque lettre en regardant leurs positionnement dans la liste alphabet et renvoie la chaîne la plus petite
    for lettre_chaîne1,lettre_chaîne2 in liste_comparaison:
        # On prend le positionnement dans l'alphabet de chaque lettre à la même position dans les 2 chaînes de caractères
        positionnement_lettre_chaîne1 = alphabet.index(lettre_chaîne1)
        positionnement_lettre_chaîne2 = alphabet.index(lettre_chaîne2)

        # On cherche le plus petit selon l'odre léxicographique
        if positionnement_lettre_chaîne1 > positionnement_lettre_chaîne2:
            return chaîne2
        if positionnement_lettre_chaîne1 < positionnement_lettre_chaîne2:
            return chaîne1
    # Si il y a les mêmes lettres sur le même intervalle on renvoie la chaîne de caractère la plus courte
    if len(liste_chaîne1) > len(liste_chaîne2):
        return chaîne2
    else:
        return chaîne1


# tests
import doctest
doctest.testmod()

# Entrée
nb_caractères_chaîne1 = int(input())
chaîne1 = input()
nb_caractères_chaîne2 = int(input())
chaîne2 = input()

# Sortie
print(comparaison_lexicographique(chaîne1,chaîne2))

        


