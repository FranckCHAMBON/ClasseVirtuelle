from random import randrange

largeur = 100
hauteur = 100

print(largeur, hauteur)

grille = [['0' for i in range(largeur)] for j in range(hauteur)]

for tour in range(1, 7):
    unité = '1' if tour % 2 == 1 else '0'
    r = min(largeur, hauteur) // 2**tour
    r2 = r**2
    for _ in range(2**tour):
        i_0 = randrange(0, hauteur)
        j_0 = randrange(0, largeur)
        for i in range(largeur):
            for j in range(hauteur):
                if (i_0 - i)**2 + (j_0 - j)**2 <= r2:
                    # (i, j) est dans le disque de centre (i_0, j_0) et de rayon r
                    grille[i][j] = unité

def redessine_les_cotés():
    """
    Redessine les cotés avec des "0" 
    """
    for j in range(largeur):
        grille[0][j] = "0"
        grille[hauteur-1][j] = "0"

    for i in range(hauteur):
        grille[i][0] = "0"
        grille[i][largeur-1] = "0"

redessine_les_cotés()                    

for ligne in grille:
    print(''.join(ligne))
