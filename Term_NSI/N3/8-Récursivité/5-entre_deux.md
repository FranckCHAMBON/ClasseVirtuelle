# [Entre deux](http://www.france-ioi.org/algo/task.php?idChapter=513&idTask=510)



Écrivez un programme qui lit deux entiers $N$ et $M$ en entrée avec $N \leqslant M$, et qui affiche dans l'ordre, tous les entiers de $N$ à $M$, séparés par des espaces.

**Votre programme doit impérativement utiliser une fonction récursive, et non une boucle.**

## Exemple

entrée :

    4 11

sortie :

    4 5 6 7 8 9 10 11

## Solution

```python
def entre_deux(n: int, m: int) -> str:
    """Renvoie les nombres entre n et m
    >>> entre_deux(4, 11)
    4 5 6 7 8 9 10 11
    """
    if n == m:
        return str(n)
    else:
        return str(n) + " " + entre_deux(n+1, m)

n, m = map(int, input().split())
print(entre_deux(n, m))
```

### Commentaires
* Pour le cas de base ($n = m$), il suffit de renvoyer $n$, en chaîne.
* Pour le cas général, on peut renvoyer
    * $n$ en chaîne, puis
    * une espace, puis
    * la chaîne des nombre entre $n+1$ et $m$ par récursivité.
