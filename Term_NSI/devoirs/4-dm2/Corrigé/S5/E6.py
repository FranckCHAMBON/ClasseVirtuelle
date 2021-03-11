"""
Prologin: Entraînement 2003
Exercice: 6 - Nombres impairs
https://prologin.org/train/2003/semifinal/nombres_impairs
"""

nombre_1, nombre_2 = map(int, input().split(" "))

if nombre_1 % 2 == 0:
    nombre_1 += 1

liste_nombres_impairs = [nombre_impair for nombre_impair in range(nombre_1, nombre_2+1, 2)]

print(" ".join(str(nombre) for nombre in liste_nombres_impairs))