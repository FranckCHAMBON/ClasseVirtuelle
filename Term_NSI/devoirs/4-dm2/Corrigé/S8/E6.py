"""
Prologin : Épreuve régionale 2003
Exercice : Nombres Impairs
https://prologin.org/train/2003/semifinal/nombres_impairs
"""

def nb_impairs(n: int, m: int) -> str:
    """Cette fonction prend en paramètre deux entiers et affiche dans un ordre croissant tous les nombres impairs se trouvant entre ces deux entiers inclus.
    >>> 42 51
    43 45 47 49 51
    """
    liste_nb_impairs = []
    for x in range(m - n + 1):
        if n % 2 == 0:
            pass
        else:
            liste_nb_impairs.append(n)
        n += 1
    formatage = " ".join([repr(x) for x in liste_nb_impairs])
    return formatage
    

# Entrée
n, m = map(int, input().split())

# Sortie
print(nb_impairs(n, m))