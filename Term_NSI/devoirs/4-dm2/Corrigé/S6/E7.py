"""
Prologin:Entrainement 2003
Exercice:7 - Table de multiplication
Lien:https://prologin.org/train/2003/semifinal/table_de_multiplications
"""
chiffre = int(input())
for y in range (1, 10):
    print(chiffre,"x",y,"=",chiffre*y, sep="")
