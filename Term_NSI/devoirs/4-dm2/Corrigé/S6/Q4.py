"""
Prologin:Qualification 2003
Exercice:4 - Nombre de voyelles
Lien:https://prologin.org/train/2003/qualification/nombre_de_voyelles
"""
longueur_mot = int(input())
mot = input().upper()
voyelle = [" ","A","E","I","O","U","Y"]
A = 0
for lettre in mot:
    if lettre in voyelle:
        A += 1
print (A)
