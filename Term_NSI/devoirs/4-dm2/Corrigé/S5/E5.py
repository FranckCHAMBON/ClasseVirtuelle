"""
Prologin: Entraînement 2003
Exercice: 5 - Mot le plus long
https://prologin.org/train/2003/semifinal/mot_le_plus_long
"""
nombre_caractères = int(input())

liste_mots = input().split(" ")

# On crée une liste où, à la place d'avoir les mots, on a leur longueur en utilisant `map`
liste_longueur_mots = list(map(len, liste_mots))

# Et on affiche la plus grande longueur de la liste des longueurs de mots
print(max(liste_longueur_mots))