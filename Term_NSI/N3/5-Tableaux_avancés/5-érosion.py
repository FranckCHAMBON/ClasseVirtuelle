class Image:
    """objet Image en noir et blanc '#' et '.'
    avec méthodes pour noircir une case, d'érosion et d'affichage.
    """

    def __init__(self, nb_lignes, nb_colonnes, grille=None):
        """Si `grille` est absent, l'image sera blanche"""
        self.__nb_lignes = nb_lignes
        self.__nb_colonnes = nb_colonnes
        if grille is not None:
            self.__grille = grille
        else:
            self.__grille = [['.' for _ in range(nb_colonnes)]
                            for _ in range(nb_lignes)]
    
    def affiche(self):
        for ligne in self.__grille:
            print("".join(ligne))
    
    def noircir(self, i, j):
        self.__grille[i][j] = '#'

    def érosion(self):
        """Renvoie une nouvelle image érodée"""
        érodée = Image(self.__nb_lignes, self.__nb_colonnes)
        for i in range(1, self.__nb_lignes - 1):
            for j in range(1, self.__nb_colonnes - 1):
                if self.__grille[i][j] == '#' and all(
                    self.__grille[i+di][j+dj] == '#' 
                    for di,dj in [(-1, 0), (+1, 0), (0, -1), (0, +1)]):
                        érodée.noircir(i, j)
        return érodée


nb_érosion = int(input())
nb_lignes, nb_colonnes = map(int, input().split())
grille = [list(input()) for _ in range(nb_lignes)]
image = Image(nb_lignes, nb_colonnes, grille)
for _ in range(nb_érosion):
    image = image.érosion()
image.affiche()
