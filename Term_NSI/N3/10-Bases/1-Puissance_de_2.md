# [Puissance de 2](http://www.france-ioi.org/algo/task.php?idChapter=565&idTask=440)

Écrivez un programme qui lit un entier et affiche la valeur de la plus grande puissance de 2 qui soit inférieure ou égale à ce nombre.

## Contraintes

* `1 <= N <= 100 000 000`, où `N` est le nombre fourni en entrée.

### Exemple

entrée :

    73

sortie :

    64

### Commentaires

$2^6$ vaut en effet $64$, qui est inférieur à $73$. La puissance de $2$ suivante, $2^7$ vaut $128$ et est donc supérieure à $73$.

## Solution

```python
def main():
    n = int(input())
    puissance = 1
    while puissance <= n:
        puissance <<= 1
    puissance >>= 1
    print(puissance)
main()
```

### Commentaires

* On part de $1 = 2^0$, et on boucle tant que la puissance est inférieure ou égale à $n$. En sortie de boucle, on a `puissance > n`.
* On revient une étape en arrière, et `puissance` est le plus grand possible avec `puissance <= n`.