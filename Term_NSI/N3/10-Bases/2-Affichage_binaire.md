# [Affichage binaire](http://www.france-ioi.org/algo/task.php?idChapter=565&idTask=441)


Écrivez un programme qui lit un entier positif ou nul, puis l'affiche en base binaire.

## Contraintes

* `0 <= N <= 100 000 000`, où `N` est le nombre fourni en entrée.

### Exemples
#### Exemple 1

entrée :

    9

sortie :

    1001

#### Exemple 2

entrée :

    126

sortie :

    1111110

## Solution

```python
def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    binaire = []
    while n != 0:
        binaire.append(n&1)
        n >>= 1
    for x in binaire[::-1]:
        print(x, end="")
    print()
main()
```

### Commentaires
* Il ne faut pas oublier le cas $n = 0$.
* Pour obtenir le bit de poids faible de $n$, on peut faire `n&1` qui correspond à un 'et logique bit-à-bit' ; c'est plus rapide que faire `n%2` qui donne la même réponse.
* Pour obtenir les autres bits, on peut faire `n >>= 1` qui décale $n$ de 1 rang vers la droite ; c'est plus rapide que faire `n //= 2` qui donne la même réponse.

* Il existe une fonction incluse dans Python pour la conversion, il s'agit de `bin`, mais elle commence l'affichage par `0b` qu'il faut enlever pour notre problème.

```python
n = int(input())
print(bin(n)[2:])
```

* Si on n'enlève pas ces deux premiers caractères, on a par exemple :
```python
>>> bin(6)
0b110
```
* La fonction `bin` renvoie une chaîne de caractère, et on peut obtenir la tranche du 2ᵉ jusqu'à la fin avec `[2:]`
