"""
Auteur: Franck CHAMBON
Problème: https://prologin.org/train/2003/semifinal/anagrammes
"""


class Nœud:
    def __init__(self, gauche, élément, droite):
        self.gauche = gauche
        self.élément = élément
        self.droite = droite


class ABR_1:
    """ABR sans doublon"""

    def __init__(self):
        self.racine = None
    
    def est_vide(self):
        return self.racine is None
    
    def ajoute(self, élément):
        "On ajoute sans dupliquer"
        if self.est_vide():
            self.racine = Nœud(ABR_1(), élément, ABR_1())
        elif élément < self.racine.élément:
            self.racine.gauche.ajoute(élément)
        elif élément > self.racine.élément:
            self.racine.droite.ajoute(élément)
        else:
            # en cas d'égalité, on ne fait rien ici
            pass
  
def parcours_profondeur(arbre) -> list:
    # parcours infixe
    liste_ordonnée = []
    if not arbre.est_vide():
        liste_ordonnée.extend(parcours_profondeur(arbre.racine.gauche))
        liste_ordonnée.append(arbre.racine.élément)
        liste_ordonnée.extend(parcours_profondeur(arbre.racine.droite))
    return liste_ordonnée

class ABR_2:
    """ABR qui gère les doublons en comptant les effectifs."""

    def __init__(self):
        self.racine = None
    
    def est_vide(self):
        return self.racine is None
    
    def ajoute(self, signe):
        """On ajoute en comptant les effectifs.
        - `self.racine.élément[0]` est la signature,
        - `self.racine.élément[1]` est l'effectif associé.
        """
        if self.est_vide():
            self.racine = Nœud(ABR_2(), [signe, 1], ABR_2())
        elif signe < self.racine.élément[0]:
            self.racine.gauche.ajoute(signe)
        elif signe > self.racine.élément[0]:
            self.racine.droite.ajoute(signe)
        else:
            # en cas d'égalité, on met à jour l'effectif
            self.racine.élément[1] += 1
    


# cœur du problème

def signature(mot: str) -> str:
    """ Renvoie la signature d'un mot.

    >>> signature('laval')
    'aallv'

    """
    ord_a = ord('a')
    signe = [0 for _ in range(26)]
    for lettre in mot:
        signe[ord(lettre) - ord_a] += 1

    lettres = []
    for i in range(26):
        if signe[i] != 0:
            lettres.append(chr(i + ord_a) * signe[i])
    return "".join(lettres)


def nb_couples_anagrammes(phrase: str) -> int:
    """Renvoie la réponse à notre problème

    >>> début_p = "le chien marche vers sa niche et trouve une limace "
    >>> fin_p = "de chine nue pleine de malice qui lui fait du charme"
    >>> phrase = début_p + fin_p
    >>> nb_couples_anagrammes(phrase)
    6

    """
    mots = phrase.split()

    arbre_mots_uniques = ABR_1() # sans doublon
    for mot in mots:
        arbre_mots_uniques.ajoute(mot)
    
    mots_uniques = parcours_profondeur(arbre_mots_uniques)

    effectif_anagrammes = ABR_2() # gère effectif
    for mot in mots_uniques:
        signe = signature(mot)
        effectif_anagrammes.ajoute(signe)
    
    liste_effectifs = parcours_profondeur(effectif_anagrammes)

    réponse = 0
    for signe, quantité in liste_effectifs:
        réponse += quantité * (quantité - 1) // 2
    return réponse


import doctest
doctest.testmod()

# lecture

nb_caractères = int(input())
phrase = input()


# écriture

print(nb_couples_anagrammes(phrase))

