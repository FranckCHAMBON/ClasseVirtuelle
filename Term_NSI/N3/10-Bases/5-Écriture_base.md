# [Écriture dans une base quelconque ](http://www.france-ioi.org/algo/task.php?idChapter=565&idTask=1748)

Vous voulez créer un programme capable d'écrire un entier dans n'importe quelle base. Votre programme doit lire un entier positif `entierAConvertir` donné par son écriture décimale habituelle puis la base d'arrivée `baseArrivée`. Il doit ensuite afficher le nombre de chiffres de `entierAConvertir` dans cette base puis, sur la ligne suivante, chacun de ces chiffres dans l'ordre habituel de gauche à droite en terminant par le chiffre des unités. Attention ces chiffres étant peut-être des entiers supérieurs à 9, il peuvent avoir une écriture décimale elle même composée de plusieurs chiffres.

Le chiffre de gauche ne peut être 0 que si le nombre à afficher est 0 (on n'écrit pas de 0 à gauche).

## Contraintes

* `0 <= entierAConvertir<= 100 000 000`
* `2 <= baseArrivée <= 100`, la base d'arrivée.

### Entrée
Première ligne, deux entiers : `entierAConvertir` et `baseArrivée`.

### Sortie
* Première ligne, un entier : le nombre de chiffres dans la base d'arrivée
* Deuxième ligne : les chiffres, en écriture décimale, séparés par des espaces, dans l'ordre habituel (unités à droite).

### Exemples

#### Exemple 1

entrée :

    1234 100

sortie :

    2
    12 34

#### Exemple 2

entrée :

    254 16

sortie :

    2
    15 14

## Solution

```python
n, base = map(int, input().split())

chiffres = []
while n > 0:
    chiffre = n % base
    n = n // base
    chiffres.append(chiffre)

if chiffres == []:
    print(1) # un seul chiffre
    print(0) # le chiffre 0
else:
    print(len(chiffres))
    for chiffre in chiffres[::-1]:
        print(chiffre, end=" ")
    print()
```

### Commentaires

* Quand on a besoin simultanément de `x // n` et `x % n`, dont le coût est de deux divisions, il est plus rapide d'utiliser :
    * Ou bien, calculer le quotient `q = x // n`, et en déduire le reste `r = x - q*n` ; le coût de la multiplication étant inférieur à la division.
    * Ou bien, on utilise une facilité de Python qui offre les deux d'un coup avec `q, r = divmod(x, n)`. De sorte que les deux premières instructions de la boucle `while` deviennent :
```python
n, chiffre = divmod(n, base)
```

* À la fin, il est important d'afficher les chiffres dans l'ordre inverse de leur création dans la liste ; pour cela on itère sur `chiffres[::-1]` : de la fin, au début, par pas de $-1$.
* On peut donner une version avec un style fonctionnel de la dernière boucle :
```
print(" ".join(map(str, chiffres[::-1])))
```
* Dans cette version,
    * `chiffres[::-1]` est la liste d'entiers des chiffres lus à l'envers.
    * `map(str, ...)` applique la fonction `str` à tous ces entiers, on obtient alors la liste (presque) des chiffres au format chaîne de caractères.
    * Enfin, on recolle le tout avec une espace entre chaque chiffre avec `" ".join(...)`.
    * Oui, espace est féminin en typographie ; **une** espace.
