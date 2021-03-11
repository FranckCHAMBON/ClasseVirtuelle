"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/plan_de_metro
"""

def main():
    départ = int(input())

    nb_liens = int(input())
    graphe = dict()
    for _ in range(nb_liens):
        a, b = map(int, input().split())
        for x, y in [(a, b), (b, a)]:
            if x in graphe:
                graphe[x].append(y)
            else:
                graphe[x] = [y]
    
    vus = set()
    courant = {départ}
    distance = 0
    while courant != set():
        ajout = False
        suivant = set()
        for a in courant:
            vus.add(a)
            for b in graphe[a]:
                if b not in vus:
                    if b not in courant:
                        ajout = True
                        suivant.add(b)
        courant = suivant
        if ajout:
            distance += 1
    print(distance - 1)
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