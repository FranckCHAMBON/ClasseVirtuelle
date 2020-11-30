# 1. lecture de l'entrée
nb_points_vie = int(input())
nb_salles, nb_portes = map(int, input().split())

for _ in range(nb_portes):
    salle_a, salle_b = map(int, input().split())
    #...
    print("Il y a une porte entre la salle", salle_a, "et la salle", salle_b)
