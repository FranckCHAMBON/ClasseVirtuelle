"""
Prologin: Entraînement 2003
Exercice: 3 - Grand écart
https://prologin.org/train/2003/semifinal/grand_ecart
"""

nombre_éléments = int(input())
liste_entiers = list(map(int, input().split()))

écart_maximal = 0

for x in range(nombre_éléments):
    if x == nombre_éléments-1:
        pass
    else:
        écart = abs(liste_entiers[x+1] - liste_entiers[x])
        if écart > écart_maximal:
            écart_maximal = écart

print(écart_maximal)