class Nœud:
    def __init__(self, gauche, élément, droite):
        self.gauche = gauche
        self.élément = élément
        self.droite = droite


class ABR:
    def __init__(self, éléments=None):
        self.racine = None
        for élément in éléments:
            self.ajoute(élément)
    
    def est_vide(self):
        return self.racine is None
    
    def ajoute(self, élément):
        "On ajoute sans dupliquer"
        if self.est_vide():
            self.racine = Nœud(ABR(), élément, ABR())
        elif élément < self.racine.élément:
            self.racine.gauche.ajoute(élément)
        elif élément > self.racine.élément:
            self.racine.droite.ajoute(élément)
        else:
            pass
            # en cas d'égalité, on ne fait rien ici
    
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
            self.racine.droite.est_présent(élément)
        else:
            return True
            # Cas d'égalité