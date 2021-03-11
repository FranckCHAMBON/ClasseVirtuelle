"""
Prologin: Qualification 2003
Exercice: 2 - Comparer des chaînes
https://prologin.org/train/2003/qualification/comparer_des_chaines
"""
longueur_premier_mot = int(input())
premier_mot = input()
longueur_second_mot = int(input())
second_mot = input()
mot_final = None

for i in range(min(longueur_premier_mot, longueur_second_mot)):
    lettre_1 = premier_mot[i]
    lettre_2 = second_mot[i]
    if ord(lettre_1) < ord(lettre_2):
        mot_final = premier_mot
        break
    elif ord(lettre_2) < ord(lettre_1):
        mot_final = second_mot
        break

if mot_final is None:
    mot_final = premier_mot if longueur_premier_mot < longueur_second_mot else second_mot

print(mot_final)