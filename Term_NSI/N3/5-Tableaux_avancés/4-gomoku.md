# [Gomoku](http://www.france-ioi.org/algo/task.php?idChapter=564&iOrder=4)


Le Gomoku est un jeu de plateau à deux joueurs, dans lequel pour gagner, chaque joueur doit réussir à aligner 5 pions sur des cases consécutives d'un plateau, horizontalement, verticalement ou en diagonale. Le plateau est une grille carrée, de dimension quelconque.

Écrivez un programme qui lit en entrée le contenu d'une partie de Gomoku, et détermine si l'un des joueurs a gagné.

## Contraintes

* $1 \leqslant N \leqslant 40$, où $N$ est le nombre de lignes/colonnes du plateau utilisé pour la partie.

## Entrée
* La première ligne de l'entrée contient un entier $N$ : le nombre de colonnes et de lignes du plateau de Gomoku.

* Chacune des $N$ lignes suivantes contient $N$ entiers, séparés par des espaces, correspondant au contenu des cases d'une ligne du plateau. L'entier vaut `0` si la case est vide, `1` si elle contient un pion du joueur `1`, et `2` pour un pion du joueur 2.

## Sortie
* Votre programme doit afficher une ligne contenant un entier : le numéro du joueur gagnant (`1` ou `2`), ou `0` si aucun des joueurs n'a aligné 5 pions.

## Exemple

---

entrée :

```
6
0 0 2 0 1 0
0 1 2 2 2 1
0 0 2 0 1 0
0 0 2 1 0 0
0 0 1 0 0 0
0 1 0 0 0 0
```

sortie :

```
1
```

## Solution

```python
def gomoku(n: int, grille:list) -> str:
    """Renvoie le vainqueur 1 ou 2, ou 0 sinon...
    """
    # vecteurs : vertical, horizontal, et 2 en diagonale
    vecteurs = [(1, 0), (0, 1), (1, 1), (1, -1)]
    def est_valide(i, j):
        return (0 <= i < n) and (0 <= j < n)
    
    def vérifie(i, j, di, dj):
        """Vérifie un gagnant en (i, j) et
         la direction (di, dj)
        """
        joueur = grille[i][j]
        for k in range(1, 5):
            i += di ; j += dj
            if (not est_valide(i, j)) or grille[i][j] != joueur:
                return 0
        return joueur
    for i in range(n):
        for j in range(n):
            if grille[i][j] != 0:
                for di, dj in vecteurs:
                    joueur = vérifie(i, j, di, dj)
                    if joueur != 0:
                        return joueur
    return 0
n = int(input())
grille = [list(map(int, input().split())) for _ in range(n)]
résultat = gomoku(n, grille)
print(résultat)
```

## Commentaires
* Bien dessiner les vecteurs pour comprendre comment fonctionnent `i` et `j`, et leur modifications.
* La complexité n'est pas très bonne, les cases sont souvent relues pour tester différents alignements... Nous verrons plus tard une solution par programmation dynamique, où chaque case n'est lue qu'une seule fois, et où la lecture de la grille peut se faire ligne par ligne, puis l'oublier ! L'empreinte mémoire est alors très bonne, en plus !