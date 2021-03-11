"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/palindromes
"""

def distance_palindrome(m, n):
    """Renvoie le nombre minimum de lettre à supprimer
    pour obtenir un palindrome.
    On ne considère que la tranche mot[m:n]
    """
    if réponse[m][n] != None:
        # on a déjà calculé la réponse
        return réponse[m][n]

    if (n - m <= 1):
        # cas de base ; 0 ou 1 lettre => rien à supprimer.
        réponse[m][n] = 0
        return 0

    distance = min(
            1 + distance_palindrome(m+1, n),
            1 + distance_palindrome(m, n-1)
            )

    if mot[m] == mot[n-1]:
        distance = min(distance, distance_palindrome(m+1, n-1))

    réponse[m][n] = distance
    return distance

n = int(input())
mot = input()
assert n == len(mot), f"n={n}, or le mot est de longueur {len(mot)}"

réponse = [[None for _ in range(n+1)] for _ in range(n+1)]
print(distance_palindrome(0, n))


"""
TEST

entrée :

6
baobab

sortie :

1

"""
