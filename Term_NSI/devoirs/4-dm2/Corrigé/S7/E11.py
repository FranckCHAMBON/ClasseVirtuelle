""" 
Prologin: Entraînement 2003
Exercice: 11 - Anagrammes
https://prologin.org/train/2003/semifinal/anagrammes
"""

def Anagrammes(liste_mots:list) -> int:
    """ Prend une liste de mots puis recherche et renvoie le nombre de couple d'Anagramme sans compter les doublons
    >>> Anagrammes(['le', 'chien', 'marche', 'vers', 'sa', 'niche', 'et', 'trouve', 'une', 'limace', 'de', 'chine', 'nue', 'pleine', 'de', 'malice', 'qui', 'lui', 'fait', 'du', 'charme'])
    6
    """

    # On retire les doublons
    liste_mots = set(liste_mots)
    liste_mots = list(liste_mots)

    def Trie_mots(liste_mots:list) -> list:
        """ Prend chaque mot de la liste les transformes en liste et les trie dans l'odre alphabétique puis les remet dans la liste
        >>> Trie_mots(['le', 'chien', 'marche', 'vers', 'sa', 'niche', 'et', 'trouve', 'une', 'limace', 'de', 'chine', 'nue', 'pleine', 'de', 'malice', 'qui', 'lui', 'fait', 'du', 'charme'])
        [['e', 'l'], ['c', 'e', 'h', 'i', 'n'], ['a', 'c', 'e', 'h', 'm', 'r'], ['e', 'r', 's', 'v'], ['a', 's'], ['c', 'e', 'h', 'i', 'n'], ['e', 't'], ['e', 'o', 'r', 't', 'u', 'v'], ['e', 'n', 'u'], ['a', 'c', 'e', 'i', 'l', 'm'], ['d', 'e'], ['c', 'e', 'h', 'i', 'n'], ['e', 'n', 'u'], ['e', 'e', 'i', 'l', 'n', 'p'], ['d', 'e'], ['a', 'c', 'e', 'i' , 'l', 'm'], ['i', 'q', 'u'], ['i', 'l', 'u'], ['a', 'f', 'i', 't'], ['d', 'u'], ['a', 'c', 'e', 'h', 'm', 'r']]
        """
        liste_mots_trié = []
        for x in range(len(liste_mots)):
            # On transforme le mot en une liste afin de trier les lettres dans l'odre alphabétique
            mot_trié = list(liste_mots[x])
            mot_trié.sort()
            # On ajoute dans une liste la liste de mot trié 
            liste_mots_trié.append(mot_trié)
        return liste_mots_trié
  

    liste_mots_trié = Trie_mots(liste_mots)

    def comptage(liste_mots_trié:list) -> int:
        """ Prend une liste et compte le nombre de couple 
        >>> comptage([['e', 'l'], ['c', 'e', 'h', 'i', 'n'], ['a', 'c', 'e', 'h', 'm', 'r'], ['e', 'r', 's', 'v'], ['a', 's'], ['c', 'e', 'h', 'i', 'n'], ['e', 't'], ['e', 'o', 'r', 't', 'u', 'v'], ['e', 'n', 'u'], ['a', 'c', 'e', 'i', 'l', 'm'], ['d', 'e'], ['c', 'e', 'h', 'i', 'n'], ['e', 'n', 'u'], ['e', 'e', 'i', 'l', 'n', 'p'], ['d', 'e'], ['a', 'c', 'e', 'i' , 'l', 'm'], ['i', 'q', 'u'], ['i', 'l', 'u'], ['a', 'f', 'i', 't'], ['d', 'u'], ['a', 'c', 'e', 'h', 'm', 'r']])
        6
        """
        nb_Anagrammes = 0
        for x in range(len(liste_mots_trié)):
            mot = liste_mots_trié[x]
            for y in range(x + 1,len(liste_mots_trié)):
                if mot == liste_mots_trié[y]:
                    nb_Anagrammes += 1
                
        return nb_Anagrammes
    return comptage(liste_mots_trié)
    
# tests
import doctest
doctest.testmod()

# Entrée
nb_caractères = int(input())
liste_mots = list(input().split())

# Sortie
print(Anagrammes(liste_mots))
    
        