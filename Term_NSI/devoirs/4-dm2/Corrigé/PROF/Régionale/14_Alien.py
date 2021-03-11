"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/alien
"""

def main():
    nb_munitions = int(input())
    temps_disponible = int(input())
    nb_pièces = int(input())
    temps_pris = [0 for _ in range(nb_munitions + 1)]
    for _ in range(nb_pièces):
        nb_aliens, durée = map(int, input().split())
        temps_pris = [
            min(durée + temps_pris[i], temps_pris[i - nb_aliens])
            if i >= nb_aliens else durée + temps_pris[i]
            for i in range(nb_munitions+1)
            ]
    print("1" if temps_pris[-1] <= temps_disponible else "0")
main()

"""
TEST

entrée :

10
10
3
5 15
15 11
5 15

sortie :

0

"""
