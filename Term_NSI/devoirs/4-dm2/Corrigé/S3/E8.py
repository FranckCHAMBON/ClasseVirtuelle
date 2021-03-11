"""
Prologin:  Entraînement  2003
Exercice: 8 - Puissance 4 
https://prologin.org/train/2003/semifinal/puissance_4
"""
def puissance_4(matrice_jeu):
    """ trouve le gagnon 1 ou 2 si égaliter affiche 0"""
    cologne = 0
    gagnent_est = 0
    ligne = 0
    
    
    def lit_horizontalement(cologne: int, gagnent_est: int):
        """ sa lit horizantalement le jeu"""
        vérifie_gagnent = 0 # si vérifie_gagnant est égale a 3, on a un gagnent
        for z in range (5): #car il y a 6 cologne mais on va prendre un facteur +1 sur la matrice 
            if matrice_jeu[z][cologne] != 0 and matrice_jeu[z][cologne] == matrice_jeu[z + 1][cologne] :
                vérifie_gagnent += 1 
            else:
                vérifie_gagnent = 0
            if vérifie_gagnent == 3:
                gagnent_est = matrice_jeu[z][cologne]
        if gagnent_est == 1 or gagnent_est == 2:
            return gagnent_est
        else:
            if cologne < 5:
                return lit_horizontalement(cologne + 1 , gagnent_est)
            else :
                None
    

    def lit_verticalement(cologne: int, gagnent_est: int):
        vérifie_gagnent = 0 # si vérifie_gagnant est égale a 3, on a un gagnent
        for y in range(6)  : #car il y a 7 ligne mais on va prendre un facteur +1 sur la matrice 
            if matrice_jeu[cologne][y] != 0 and matrice_jeu[cologne][y] == matrice_jeu[cologne][y + 1]: # erreur out of range mais je comprend pas où car si la bouvle fait 4 tour il est quand meme out 
                vérifie_gagnent += 1
            else:
                vérifie_gagnent = 0
            if vérifie_gagnent == 3: 
                gagnent_est = matrice_jeu[cologne][y]
        if gagnent_est == 1 or gagnent_est == 2:
            return gagnent_est
        else:
            if cologne < 5 :
                return lit_verticalement(cologne + 1, gagnent_est)
            else:
                None

    """
    def lit_diagonalement(cologne: int, ligne: int, gagnent_est: int):
        est la je suis bloquer
    """
    lit_horizontalement(cologne, gagnent_est)
    if gagnent_est == 1 or gagnent_est == 2:
        return gagnent_est
    else:
        cologne = 0
        lit_verticalement(cologne, gagnent_est)
        if gagnent_est == 1 or gagnent_est == 2:
            return gagnent_est
        else:
            """
            cologne = 0
            lit_diagonalement(cologne, ligne)
            if gagnent_est == 1 or gagnent_est == 2:
                return gagnent_est
            else :
            """   
            return "0" 


matrice_jeu = [] 
for x in range(6):
    matrice_jeu.append(input())
print(puissance_4(matrice_jeu))
""" il se peut qu'il aurai un probleme de rapiditer et on plus je vois pas commen lire ma diagonal"""
