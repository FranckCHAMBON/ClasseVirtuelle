"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/plan_de_metro
"""

def main():
    départ = int(input())

    nb_liens = int(input())
    # construction du graphe
    graphe = dict()
    for _ in range(nb_liens):
        station_a, station_b = map(int, input().split())
        for station_x, station_y in [(station_a, station_b), (station_b, station_a)]:
            if station_x not in graphe:
                graphe[station_x] = [station_y]
            else:
                graphe[station_x].append(station_y)
    
    # parcours en largeur en partant de départ,
    # avec calcul de la distance maximale atteinte
    courant = {départ}
    vus = {départ}
    distance = 0
    while courant != set():
        suivant = set()
        for station_a in courant:
            for station_b in graphe[station_a]:
                if station_b not in vus:
                    suivant.add(station_b)
                    vus.add(station_b)
        courant = suivant
        distance += 1
    print(distance - 2)
    # on enlève 2.
    # 1 pour le dernier ajout de 1 à vide,
    # 1 autre pour le nombre de station intermédiaire au lieu de la distance.
main()

"""
TEST1

entrée :

1
3
1 2
2 3
1 3

sortie :

0


TEST2

entrée :

1
14
1 3
3 42
42 57
57 270
42 566
566 245
245 556
556 924
924 516
556 432
556 461
461 640
640 632
432 589

sortie :

7

"""