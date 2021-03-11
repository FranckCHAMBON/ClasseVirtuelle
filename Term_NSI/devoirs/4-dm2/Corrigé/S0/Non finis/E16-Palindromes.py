"""
Nom: PALAZON
Prénom: Anabel
Prologin: Qualification 2003
Exercice: 16 - Palindromes
https://prologin.org/train/2003/semifinal/palindromes
"""

def supp_palindrome (texte : str, nb_caractères : int) -> int :
    """ Renvoie le nombre minimum de caractères à supprimer 
    pour transformer la chaîne 'texte' en palindrome.

    >>> nb_caractères = 6
    >>> texte = baobab
    1

    """
    if nb_caractères == 1:
        return 0
    if ch[0] == ch[-1]:
        return sup_palindrome(texte[1: nb_caractères-1])

# tests
import doctest
doctest.testmod()

# Entrée
nb_caractères = int(input())
assert 1 <= nb_caractères <= 200
texte = input()

# Sortie
print(supp_palindrome(texte, nb_caractères))

new_now = time.time()
print("\nTemps total d'execution : ", new_now - now)