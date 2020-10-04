from bisect import bisect_left
def main():
    affiches = []
    # les affiches visibles, liste d'entiers strictement croissante
    # de hauteurs négatives, exemple
    # -11, -4, -3

    nb_requetes = int(input())

    for _ in range(nb_requetes):
        ligne = input()
        if ligne == "Q":
            print(len(affiches))
        else:
            hauteur = -int(ligne.split()[1])
            # hauteur est négative
            if (affiches == []) or (affiches[0] >= hauteur):
                # il n'y avait pas d'affiches
                # ou elles sont toutes couvertes
                affiches = [hauteur]
            elif affiches[-1] < hauteur:
                affiches.append(hauteur)
            else:
                i = bisect_right(affiches, hauteur)
                affiches[i:] = [hauteur]
main()
