"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/plages_du_pacifique
"""

def main():
    def est_valide(i, j):
        return (0 <= i < nb_lignes) and (0 <= j < nb_colonnes)
    
    nb_colonnes, nb_lignes = map(int, input().split())
    grille = [list(input()) for _ in range(nb_lignes)]

    courant = set()
    # On place tout le tour de la grille dans l'océan.
    for i in range(nb_lignes):
        courant.add((i, 0))
        courant.add((i, nb_colonnes-1))
    for j in range(nb_colonnes):
        courant.add((0, j))
        courant.add((nb_lignes - 1, j))
    
    plages = set()
    while courant != set():
        suivant = set()
        for (i, j) in courant:
            grille[i][j] = "3" # marquage pour vu
            for di in (-1, 0, +1):
                idi = i + di
                for dj in (-1, 0, +1):
                    jdj = j + dj
                    if est_valide(idi, jdj):
                        if (grille[idi][jdj] == "0"):
                            # on prépare les cases voisines, tout autour !
                            suivant.add((idi, jdj))
                        if (grille[idi][jdj] == "1"):
                            if di * dj == 0:
                                # pas en diagonale
                                plages.add((idi, jdj))
        courant = suivant
    print(len(plages))

main()

"""
TEST

entrée :

7 5
0000000
0101110
0111010
0101100
0000000

sortie :

4
"""