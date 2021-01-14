from collections import deque

class Deque:
    def __init__(self):
        self.données = deque()
    
    def est_vide(self):
        return self.données == deque()
    
    def ajout_gauche(self, élément):
        self.données.appendleft(élément)

    def ajout_droite(self, élément):
        self.données.append(élément)

    def extrait_gauche(self):
        if self.est_vide():
            raise ValueError("Deque vide")
        élément_gauche = self.données.popleft()
        return élément_gauche

    def extrait_droite(self):
        if self.est_vide():
            raise ValueError("Deque vide")
        élément_droite = self.données.pop()
        return élément_droite

