"""
Prologin: Entraînement 2003
Exercice 11 - Anagrammes
https://prologin.org/train/2003/semifinal/anagrammes
"""

# 0- Coeur du programme

def nombres_anagrammes(nb_caractères: int, chaîne_mots: str) -> int:
    """ Détermine combien de couples d'anagrammes on peut former à partir des mots de chaîne_mot et renvoie le nombre
    >>> nombres_anagrammes(11, ["Hello", "World"])
    0
    >>> nombres_anagrammes(103, ["le", "chien", "marche", "vers", "sa", "niche", "et", "trouve", "une", "limace", "de", "chine", "nue", "pleine", "de", "malice", "qui", "lui", "fait", "du", "charme"])
    6
    """

    liste_mots = list()
    compteur = 0                            # On initialise le compteur à 0
    for mot in chaîne_mots:                 # On retire les doublons de la chaîne et plaçons les mots dans liste_mots
        if mot not in liste_mots:
            liste_mots.append(mot)
    longueur_liste = len(liste_mots)
    for x in range(longueur_liste):         # Pour chaque mot de liste_mot, on converti le mot en un dictionnaire de lettres
        mot = liste_mots[x]
        dico = dict()
        for lettre in mot:                  # Pour chaque lettre, on crée la lettre (initialisé à 1) si elle n'existe pas, sinon, on rajoute 1 au dictionnaire de la lettre
            dico[lettre] = 1 if lettre not in dico else dico[lettre] + 1
        liste_mots[x] = dico                # Puis, on met le dictionnaire dans liste_mots à la place du mot 
    for x in range(longueur_liste):         # Enfin, pour chaque dictionnaire, on regarde, si un autre est identique
        for y in range(x+1, longueur_liste):
            if liste_mots[x] == liste_mots[y]:
                compteur += 1               # Si oui, on ajoute 1 au compteur (on ne compte pas 2 fois les mêmes anagrammes)
    return compteur                         # On renvoie le compteur

# 1- Tests

import doctest
doctest.testmod()

# 2- Lecture des entrées

nb_caractères = int(input())
chaîne_mots = input().split()

# 3- Appel de la fonction / Sortie

print(nombres_anagrammes(nb_caractères, chaîne_mots))