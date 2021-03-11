"""
Prologin:Qualification 2003
Exercice:3 - Les trois nombres
Lien:https://prologin.org/train/2003/qualification/les_trois_nombres
"""
n1, n2, n3 = map (int, input().split())
if n1 + n2 == n3:
    print(n3)
elif n1 + n3 == n2:
    print(n2)
elif n2 + n3 == n1:
    print(n1)
else:
    print(0)
