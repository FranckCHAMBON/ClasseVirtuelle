"""
Prologin: Qualification 2003
Exercice: 3 - Les trois nombres
https://prologin.org/train/2003/qualification/les_trois_nombres
"""

nombre_1, nombre_2, nombre_3 = map(int, input().split(" "))

if nombre_1  + nombre_2 == nombre_3:
    print(nombre_3)
elif nombre_1 + nombre_3 == nombre_2:
    print(nombre_2)
elif nombre_2 + nombre_3 == nombre_1:
    print(nombre_1)
else:
    print(0)
