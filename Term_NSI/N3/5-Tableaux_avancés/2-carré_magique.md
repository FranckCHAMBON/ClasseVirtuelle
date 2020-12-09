# [Carré magique](http://www.france-ioi.org/algo/task.php?idChapter=564&idTask=469)

 Un carré magique est une grille carrée dans laquelle des nombres sont placés de telle sorte que la somme des nombres de chaque colonne, chaque ligne et de chacune des deux diagonales soit la même. De plus, Le carré doit contenir une fois chaque nombre, de 1 au nombre de cases de la grille.

Écrivez un programme qui vérifie si une grille de nombres est un carré magique.


## Contraintes

* $1 \leqslant N \leqslant 20$, où $N$ est le nombre de lignes et de colonnes de la grille.

## Entrée
La première ligne de l'entrée contient un entier $N$ : le nombre de cases du côté de la grille de nombres.

Chacune des $N$ lignes suivantes contient $N$ entiers séparés par des espaces : les nombres d'une ligne de la grille.

## Sortie
Vous devez afficher une ligne sur la sortie, contenant le mot `yes` si le carré fourni est un carré magique, et `no` sinon.

## Exemple

---

entrée :

```
3
6 1 8
7 5 3
2 9 4
```

sortie :

```
yes
```

---

## Commentaires
Chacun des chiffres de $1$ à $9$ apparaît exactement une fois dans la grille. De plus, toutes les colonnes, lignes et les deux diagonales de cette grille ont pour somme $15$. En effet :

Lignes :
* $6 + 1 + 8 = 15$
* $7 + 5 + 3 = 15$
* $2 + 9 + 4 = 15$

Colonnes :
* $6 + 7 + 2 = 15$
* $1 + 5 + 9 = 15$
* $8 + 3 + 4 = 15$

Diagonales :
* $6 + 5 + 4 = 15$
* $8 + 5 + 2 = 15$

## Solution

```python
def est_magique(n: int, grille: list) -> bool:
    """Une grille de taille n est-elle magique ?
    """
    somme = sum(grille[0]) # la somme de la première ligne
    # les autres lignes ?
    if any(sum(ligne) != somme
            for ligne in grille):
        return False
    # les autres colonnes ?
    if any(sum(grille[i][j] for i in range(n)) != somme
            for j in range(n)):
        return False
    # les diagonales ?
    if sum(grille[i][i] for i in range(n)) != somme:
        return False
    if sum(grille[i][-i-1] for i in range(n)) != somme:
        return False
    # tous les nombres de 1 à n² sont-ils présents ?
    # On enlève 1, pour un indice dans un tableau
    n_carré = n * n
    déjà_vu = [False for _ in range(n_carré)]
    for i in range(n):
        for j in range(n):
            if 0 < grille[i][j] <= n_carré:
                if déjà_vu[grille[i][j] - 1]:
                    return False
                déjà_vu[grille[i][j] - 1] = True
            else:
                return False
    # Alors tout est bon, le carré est magique
    return True

n = int(input())
grille = [list(map(int, input().split())) for _ in range(n)]
print('yes' if est_magique(n, grille) else 'no')
```
