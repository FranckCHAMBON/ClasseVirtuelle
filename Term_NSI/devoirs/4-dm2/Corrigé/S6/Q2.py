"""
Prologin:Qualification 2003
Exercice:2-Comparer des chaînes
Lien:https://prologin.org/train/2003/qualification/comparer_des_chaines
"""
longueur_mot1 = int(input())
mot1 = input()
longueur_mot2 = int(input())
mot2 = input()

liste = [mot1, mot2]

liste.sort()

print liste[0]

