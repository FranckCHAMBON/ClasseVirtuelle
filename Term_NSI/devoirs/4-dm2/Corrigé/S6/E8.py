"""
Prologin: entrainement 2003
Exercice: 8 - Puiisance 4
Lien:https://prologin.org/train/2003/semifinal/puissance_4
"""
def Puissance4(nb_lignes: int, nb_colonnes: int, plateau:list) -> int:
    """Renvoie le vainqueur 1 ou 2, ou 0 sinon...
    """
    vecteurs = [(1, 0), (0, 1), (1, 1), (1, -1)]

    def dans_plateau(ligne, colonne):
        return (0 <= ligne < nb_lignes) and (0 <= colonne < nb_colonnes)

    def vérifie(ligne, colonne, diff_ligne, diff_colonne):
        
        pion = plateau[ligne][colonne]
        for _ in range(1, 4):
            ligne += diff_ligne
            colonne += diff_colonne
            if not(dans_plateau(ligne, colonne)) or (plateau[ligne][colonne] != pion):
                    return 0
        return pion

    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            if plateau[ligne][colonne] != 0:
                for diff_ligne, diff_colonne in vecteurs:
                    pion = vérifie(ligne, colonne, diff_ligne, diff_colonne)
                    if pion != 0:
                        return pion
    return ""

nb_lignes = 6
nb_colonnes = 7
plateau = [ list(map(int, input().split(" "))) for _ in range(nb_lignes)]

print(Puissance4(nb_lignes, nb_colonnes,plateau))
