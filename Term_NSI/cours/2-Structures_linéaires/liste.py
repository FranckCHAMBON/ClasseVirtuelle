class Maillon:
    """Un maillon est donné par son élément et son maillon suivant à droite,
    éventuellement None."""

    def __init__(self, élément, droite):
        self.élément = élément
        self.droite = droite

    def __str__(self):
        return str(self.élément)


class Liste:
    "Une liste est donnée par son maillon de gauche"

    def __init__(self):
        self.maillon_gauche = None
    
    def est_vide(self):
        return self.maillon_gauche is None
    
    def ajout_gauche(self, élément):
        self.maillon_gauche = Maillon(élément, self.maillon_gauche)

    def extrait_gauche(self):
        if self.est_vide():
            raise ValueError("Liste vide")
        élément = self.maillon_gauche.élément
        self.maillon_gauche = self.maillon_gauche.droite
        return élément
    
    def __str__(self):
        affichage = "Contenu : "
        maillon = self.maillon_gauche
        while maillon is not None:
            affichage += str(maillon) + "::"
            maillon = maillon.droite
        affichage += " fin."
        return affichage
    
    def ajout_droite(self, élément):
        if self.est_vide():
            self.maillon_gauche = Maillon(élément, None)
        else:
            maillon = self.maillon_gauche
            while maillon.droite is not None:
                maillon = maillon.droite
            maillon.droite = Maillon(élément, None)
    
    def extrait_droite(self):
        if self.est_vide():
            raise ValueError("Liste vide")

        maillon = self.maillon_gauche

        if maillon.droite is None:
            élément = maillon.élément
            self.maillon_gauche = None
            return élément

        précédent = maillon
        maillon = maillon.droite
        while maillon.droite is not None:
            précédent = maillon
            maillon = maillon.droite
        élément = maillon.élément
        précédent.droite = None
        return élément

l = Liste()
for x in range(5):
    l.ajout_gauche(x)
print(l)
l.ajout_droite(10)
print(l)
l.extrait_droite()
print(l)