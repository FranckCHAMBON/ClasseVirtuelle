class Maillon:
    """Un maillon est donné par son élément et ses maillons à gauche et à droite,
    éventuellement None."""

    def __init__(self, gauche, élément, droite):
        self.gauche = gauche
        self.élément = élément
        self.droite = droite

    def __str__(self):
        return str(self.élément)


class Liste:
    """Une liste est donnée par ses maillons
    de gauche et de droite."""

    def __init__(self):
        self.maillon_gauche = None
        self.maillon_droite = None
    
    def est_vide(self):
        return (self.maillon_gauche is None) or \
               (self.maillon_droite is None)
    
    def ajout_gauche(self, élément):
        if self.est_vide():
            self.maillon_gauche = self.maillon_droite = Maillon(None, élément, None)
        else:
            self.maillon_gauche = Maillon(None, élément, self.maillon_gauche)
            self.maillon_gauche.droite.gauche = self.maillon_gauche

    def ajout_droite(self, élément):
        if self.est_vide():
            self.maillon_gauche = self.maillon_droite = Maillon(None, élément, None)
        else:
            self.maillon_droite = Maillon(self.maillon_droite, élément, None)
            self.maillon_droite.gauche.droite = self.maillon_droite

    def extrait_droite(self):
        if self.est_vide():
            raise ValueError("Liste vide")
        élément = self.maillon_droite.élément
        self.maillon_droite = self.maillon_droite.gauche
        if self.maillon_droite is not None:
            self.maillon_droite.droite = None
        return élément

    def extrait_gauche(self):
        if self.est_vide():
            raise ValueError("Liste vide")
        élément = self.maillon_gauche.élément
        self.maillon_gauche = self.maillon_gauche.droite
        if self.maillon_gauche is not None:
            self.maillon_gauche.gauche = None
        return élément
    
    def __str__(self):
        affichage = "Contenu : "
        maillon = self.maillon_gauche
        while maillon is not None:
            affichage += str(maillon) + "::"
            maillon = maillon.droite
        affichage += " fin."
        return affichage

l = Liste()
for x in range(5):
    l.ajout_gauche(x)
print(l)
l.ajout_droite(10)
print(l)
l.extrait_droite()
print(l)
