def gomoku(n: int, grille:list) -> str:
    """Renvoie le vainqueur 1 ou 2, ou 0 sinon...
    """
    # vecteurs : vertical, horizontal, et 2 en diagonale
    vecteurs = [(1, 0), (0, 1), (1, 1), (1, -1)]

    def est_valide(i, j):
        return (0 <= i < n) and (0 <= j < n)
    
    def vérifie(i, j, di, dj):
        """Vérifie un gagnant en (i, j) et
         la direction (di, dj)
        """
        joueur = grille[i][j]
        for k in range(1, 5):
            i2 = i + k*di
            j2 = j + k*dj
            if est_valide(i2, j2):
                if grille[i2][j2] != joueur:
                    return 0
            else:
                return 0
        return joueur

    for i in range(n):
        for j in range(n):
            if grille[i][j] != 0:
                for di, dj in vecteurs:
                    joueur = vérifie(i, j, di, dj)
                    if joueur != 0:
                        return joueur
    return 0

n = int(input())
grille = [list(map(int, input().split())) for _ in range(n)]
résultat = gomoku(n, grille)
print(résultat)
