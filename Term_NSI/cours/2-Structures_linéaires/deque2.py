import pile
class Pile():
    def __init__(self):
        self.données = []

    def __str__(self) -> str:
        return str(self.données)

    def est_vide(self) -> bool:
        return self.données == []

    def empile(self, valeur):
        self.données.append(valeur)
    
    def dépile(self):
        if self.est_vide():
            raise ValueError('Pile vide')
        return self.données.pop()

class Deque:
    def __init__(self):
        self.pile_gauche = pile.Pile()
        self.pile_droite = pile.Pile()
    
    def est_vide(self):
        return self.pile_gauche.est_vide() and self.pile_droite.est_vide()
    
    def ajout_gauche(self, élément):
        self.pile_gauche.empile(élément)

    def ajout_droite(self, élément):
        self.pile_droite.empile(élément)

    def extrait_gauche(self):
        if self.est_vide():
            raise ValueError("Deque vide")
        if self.pile_gauche.est_vide():
            while not self.pile_droite.est_vide():
                self.pile_gauche.empile(self.pile_droite.dépile())
        élément_gauche = self.pile_gauche.dépile()
        return élément_gauche

    def extrait_droite(self):
        if self.est_vide():
            raise ValueError("Deque vide")
        if self.pile_droite.est_vide():
            while not self.pile_gauche.est_vide():
                self.pile_droite.empile(self.pile_gauche.dépile())
        élément_droite = self.pile_droite.dépile()
        return élément_droite

