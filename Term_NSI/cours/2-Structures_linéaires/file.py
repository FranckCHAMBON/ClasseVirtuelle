class Maillon:
    """Un maillon est donné par son élément et son maillon suivant à droite,
    éventuellement None."""

    def __init__(self, élément, droite):
        self.élément = élément
        self.droite = droite

    def __str__(self):
        return str(self.élément)


class Liste:
    "Une liste est donnée par son maillon de gauche, et son maillon droite"

    def __init__(self):
        self.maillon_gauche = None
        self.maillon_droite = None
    
    def est_vide(self):
        return (self.maillon_gauche is None) and (self.maillon_droite is None)
    
    def ajout_droite(self, élément):
        maillon = Maillon(élément, None)
        if self.est_vide():
            self.maillon_gauche = maillon
            self.maillon_droite = maillon
        else:
            self.maillon_droite.droite = maillon
            self.maillon_droite = maillon

    def extrait_gauche(self):
        if self.est_vide():
            raise ValueError("Liste vide")
        élément = self.maillon_gauche.élément
        self.maillon_gauche = self.maillon_gauche.droite
        if self.maillon_gauche is None:
            self.maillon_droite = None
        return élément
    
    def __str__(self):
        affichage = "Contenu : "
        maillon = self.maillon_gauche
        while maillon is not None:
            affichage += str(maillon) + "::"
            maillon = maillon.droite
        affichage += " fin."
        return affichage
    
