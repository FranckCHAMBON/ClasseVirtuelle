"""
Prologin:Entrainement 2003
Exercice:6 - Nombre impaire
Lien:https://prologin.org/train/2003/semifinal/nombres_impairs
"""
n1, n2 = map(int, input().split())
for x in range(n1, n2 + 1):
    if x % 2 !=0 :
        print (x, end=" ")
