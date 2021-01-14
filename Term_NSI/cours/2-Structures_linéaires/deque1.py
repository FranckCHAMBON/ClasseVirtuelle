class Deque(taille_max):
    def __init__(self):
        self.taille_max = taille_max
        self.données = [None for _ in range(taille_max)]
        self.i_droite = 0
        self.i_gauche = 0
        self.taille = 0
    
    def est_vide(self):
        return self.taille == 0
    
    def ajout_droite(self, élément):
        if self.taille == self.taille_max:
            raise ValueError("Deque pleine")
        self.données[self.id_droite] = élément
        self.i_droite += 1
        if self.i_droite == self.taille_max:
            self.i_droite = 0
        self.taille += 1
    
    def ajout_gauche(self, élément):
        if self.taille == self.taille_max:
            raise ValueError("Deque pleine")
        self.données[self.i_gauche] = élément
        self.i_gauche -= 1
        if self.i_gauche == -1:
            self.i_gauche = self.taille_max - 1
        self.taille += 1

    def extrait_droite(self):
        if self.taille == 0:
            raise ValueError("Deque vide")
        self.i_droite -= 1
        if self.i_droite == -1:
            self.i_droite = self.taille_max - 1
        self.taille -= 1
        élément = self.données[self.i_droite]
        self.données[self.id_droite] = None # option ; sécurité
        return élément

    def extrait_gauche(self):
        if self.taille == 0:
            raise ValueError("Deque vide")
        self.i_gauche += 1
        if self.i_gauche == self.taille_max:
            self.i_gauche = 0
        self.taille -= 1
        élément = self.données[self.i_gauche]
        self.données[self.i_gauche] = None # option ; sécurité
        return élément

