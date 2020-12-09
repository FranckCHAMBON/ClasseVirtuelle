class Image:
    """objet Image en couleur '.' et 'a', 's', ...
    avec méthodes pour dessiner un rectangle et affichage.
    """

    def __init__(self, nb_lignes, nb_colonnes):
        """l'image sera blanche, pleine de '.'
        """
        self.__nb_lignes = nb_lignes
        self.__nb_colonnes = nb_colonnes
        self.__grille = [['.' for _ in range(nb_colonnes)]
                            for _ in range(nb_lignes)]
    
    def affiche(self):
        for ligne in self.__grille:
            print("".join(ligne))
    
    def remplit_rectangle(self, i1, j1, i2, j2, couleur: str):
        """Remplit l'image avec un rectangle
        + de sommets opposés (i1, j1) et (i2, j2),
        + avec la couleur donnée.
        """
        if not all(((0 <= i1 <= self.__nb_lignes),
                    (0 <= j1 <= self.__nb_colonnes),
                    (0 <= i2 <= self.__nb_lignes),
                    (0 <= j2 <= self.__nb_colonnes))):
            raise ValueError("Mauvais indice")
        if len(couleur) != 1:
            raise ValueError("couleur doit être un seul caractère")
                   
        for i in range(i1, i2+1):
            for j in range(j1, j2+1):
                self.__grille[i][j] = couleur


nb_lignes, nb_colonnes = map(int, input().split())
image = Image(nb_lignes, nb_colonnes)

nb_rectangles = int(input())
for _ in range(nb_rectangles):
    t_i1, t_j1, t_i2, t_j2, couleur = input().split()
    i1, j1, i2, j2 = map(int, [t_i1, t_j1, t_i2, t_j2])
    image.remplit_rectangle(i1, j1, i2, j2, couleur)

image.affiche()
