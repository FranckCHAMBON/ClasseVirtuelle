"""
Prologin: Qualification 2003
Exercice: 4 - Nombres de voyelles
https://prologin.org/train/2003/qualification/nombre_de_voyelles
"""


voyelles = "aeiouy"

nombre_caractères = int(input())
chaine_charactère = input()

print(sum(lettre.lower() in voyelles for lettre in chaine_charactère))
