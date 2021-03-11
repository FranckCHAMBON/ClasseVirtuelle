"""
Prologin: Entraînement 2003
Exercice: 4 - Initiales
https://prologin.org/train/2003/semifinal/initiales
"""
nombre_caractères = int(input())
liste_mots = list(input().split(" "))

initiales_majuscules = "".join(mot[0].upper() for mot in liste_mots)

print(initiales_majuscules)