"""
Nom: PALAZON
Prénom: Anabel
Prologin: Qualification 2003
Exercice: 13 - Plan de métro
https://prologin.org/train/2003/semifinal/plan_de_metro
"""

def nb_intermédiaires (liste : list, nb_couples : int) -> int :
    """ Renvoie le nombre de stations intermédiaires par lesquelles il faut passer pour aller vers la station la plus éloignée.

    >>> nb_couples = 14
    >>> liste = [[1,3], [3,42], [42,57], [57,270], [42,566], [566,245], [245,556], \
                [556,924], [924,516], [556,432], [556,461], [461,640], [640,632], [432,589]]
    7

    """
    if nb_couples == 1 :
        return 1
    

# Entrée
départ = int(input())
nb_couples_stations = int(input())
assert 1 <= départ, nb_couples_stations <= 1000
liste_couples = map(int, input().split) for in range (nb_couples_stations)

# Sortie
print(nb_intermédiaires(liste, nb_couples))