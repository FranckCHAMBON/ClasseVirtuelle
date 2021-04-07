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
    
    def extrait_min(self):
        if self.est_vide():
            raise ValueError("ABR vide")
        if self.racine.gauche.est_vide():
            return self.racine.élément
        return self.racine.gauche.extrait_min()
    
    def est_présent(self, élément):
        if self.est_vide():
            return False
        elif élément < self.racine.élément:
            return self.racine.gauche.est_présent(élément)
        elif élément > self.racine.élément:
            return self.racine.droite.est_présent(élément)
        else:
            # Cas d'égalité
            return True


class ABR_2:
    """ABR qui gère les doublons en comptant les effectifs"""

    def __init__(self):
        self.racine = None
    
    def est_vide(self):
        return self.racine is None
    
    def ajoute(self, signe):
        """On ajoute en comptant les effectifs.
        + self.racine.élément[0] est la signature,
        + self.racine.élément[1] est l'effectif associé.
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
    
    def extrait_min(self):
        if self.est_vide():
            raise ValueError("ABR vide")
        if self.racine.gauche.est_vide():
            return self.racine.élément
        return self.racine.gauche.extrait_min()
    
    def est_présent(self, élément):
        if self.est_vide():
            return False
        elif élément < self.racine.élément:
            return self.racine.gauche.est_présent(élément)
        elif élément > self.racine.élément:
            return self.racine.droite.est_présent(élément)
        else:
            # Cas d'égalité
            return True



# coeur du problème


def signature(mot: str) -> list:
    ord_a = ord('a')
    signe = [0 for _ in range(26)]
    for lettre in mot:
        signe[ord(lettre) - ord_a] += 1
    return signe

def nb_couples_anagrammes(phrase: str) -> int:
    """Renvoie le ...

    doctest...

    """
    mots = phrase.split()

    mots_uniques = ABR_1() # sans doublon
    for mot in mots:
        mots_uniques.ajoute(mot)
    
    effectif_anagrammes = ABR_2() # gère effectif
    while not mots_uniques.est_vide():
        mot = mots_uniques.extrait_min()
        signe = signature(mot)
        effectif_anagrammes.ajoute(signe)
    
    réponse = 0
    while not effectif_anagrammes.est_vide():
        signe, quantité = effectif_anagrammes.extrait_min()
        réponse += quantité * (quantité - 1) // 2

    return réponse




# lecture

nb_caractères = int(input())
phrase = input()


# écriture

print(nb_couples_anagrammes(phrase))

