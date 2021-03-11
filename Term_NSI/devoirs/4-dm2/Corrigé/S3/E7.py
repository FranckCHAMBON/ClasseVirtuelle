"""
Prologin:  Entraînement  2003
Exercice: 7 - Table de multiplication 
https://prologin.org/train/2003/semifinal/table_de_multiplications
"""

nb_à_multiplier = int(input())
liste_tableu= [0] * 9
resulta = 0
for y in range(1, 10): #10 est eclue dans la boucle va de 1 à 9
    resulta = nb_à_multiplier * y
    liste_tableu[y - 1] = [nb_à_multiplier, "x", y, "=", resulta]
for x in liste_tableu:
    for z in x:
        print(z, end="")
    print()

