# [Changement de base](http://www.france-ioi.org/algo/task.php?idChapter=565&idTask=368)


Alice et Bob sont lassés des capacités trop limitées de leur calculatrice et ont décidé d'en programmer une eux-mêmes.

Pour eux, la première étape consiste à écrire un programme capable de convertir un nombre d'une base donnée en une autre.

Référez-vous a l'introduction de l'épreuve pour plus de détails sur la notation des nombres en base quelconque.

## Contraintes

* `2 <= B <= 256`, où `B` est la base dans laquelle est représenté un nombre.
* `0 <= N < 100 000 000`, le nombre à convertir d'une base à l'autre.

### Entrée

La première ligne de l'entrée contient trois entiers : `B1`, `B2`, et `C`, respectivement la base de départ, la base d'arrivée et la taille du nombre (en nombre de chiffres) dans la base de départ.

La seconde ligne contient l'entier `N` à convertir, dans sa base de départ, sous la forme de `C` entiers représentant chacun un chiffre.

### Sortie

Le nombre exprimé dans la base d'arrivée (si le nombre est non-nul, il ne doit pas commencer pas un chiffre nul). Ce nombre doit être fourni au même format que celui de l'entrée, comme indiqué dans l'introduction de l'épreuve.

### Exemples

#### Exemple 1

entrée :

    10 2 2
    4 2

sortie :

    1 0 1 0 1 0

#### Exemple 2

entrée :

    100 10 3
    2 20 3

sortie :

    2 2 0 0 3

### Commentaires

Dans l'exemple 1, le nombre de 2 chiffres fourni en entrée est 42 en base décimale et s'écrit `101010` en base binaire.

Faites attention aux deux « 0 » successifs. Par exemple dans l'exemple 2, « 2 20 3 en base 100 » $= 2 × 100^2 + 20 × 100 + 3 = 2 × 10^4 + 2 * 10^3 + 3 = $ « 22003 en base 10 ».

## Solution

```python
def lire_base(base: int, chiffres: list) -> int:
    """Renvoie la valeur du nombre, avec ses 'chiffres' donnés en 'base'.
    >>> lire_base(12, [3, 11])
    47
    """
    résultat = 0
    for chiffre in chiffres:
        résultat *= base
        résultat += chiffre
    return résultat

def écrire_base(n: int, base: int) -> None:
    """Écrit l'entier 'n', dans la 'base'.
    >>> écrire_base(1234, 100)
    12 34
    """
    chiffres = []
    while n > 0:
        chiffre = n % base
        n = n // base
        chiffres.append(chiffre)

    if chiffres == []:
        print(0) # le chiffre 0
    else:
        for chiffre in chiffres[::-1]:
            print(chiffre, end=" ")
        print()

b1, b2, c = map(int, input().split())
chiffres = map(int, input().split())
écrire_base(lire_base(chiffres, b1), b2)
```
