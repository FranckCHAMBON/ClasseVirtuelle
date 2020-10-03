# [Nombre d'amour](http://www.france-ioi.org/algo/task.php?idChapter=566&idTask=2415)

Le dimanche, de nombreux enfants sont présents au sein de la bibliothèque avec leurs parents. La grande mode ces derniers temps chez les enfants est de calculer leur « nombre d’amour » pour savoir s’ils sont amoureux (ou pas) d’un autre enfant. Si deux enfants ont le même nombre alors ils sont amoureux.

Intrigué, vous décidez d’écrire un programme permettant de calculer rapidement le « nombre d’amour » correspondant à un prénom donné.

Pour calculer ce nombre, on commence par convertir chaque lettre du prénom en un nombre (A vaut 0, B vaut 1...) puis on calcule la somme de ces nombres. Si le résultat est strictement plus petit que 10, alors on a trouvé le « nombre d’amour ». Sinon, on remplace le nombre par la somme de ses chiffres. On continue ainsi tant que le résultat est plus grand ou égal à 10.

## Contraintes

Les prénoms font au plus 50 caractères.

### Entrée

Les prénoms des deux enfants (en majuscules), séparés par un espace.

### Sortie

Sur une seule ligne, les nombres d’amour de chacun des deux enfants.

### Exemple

entrée :

    ADA GWOAG

sortie :

    3 3

## Solution

```python
def valeur(mot: str) -> int:
    """Renvoie la somme totale d'un mot où chaque lettre est remplacée par un nombre.
    A par 0, B par 1, ..., Z par 25.
    >>> valeur("ABCD")
    6
    >>> valeur("ZZ")
    50
    """
    total = 0
    for lettre in mot:
        total += ord(lettre) - ord('A')
    return total

def nombre_amour(n: int) -> int:
    """Renvoie la somme des chiffres de l'entier n.
    Si le résultat est supérieur ou égal à 10, on recommence...
    >>> nombre_amour(5)
    5
    >>> nombre_amour(123)
    6
    >>> nombre_amour(77777)
    8
    """
    amour = 0
    while n > 0:
        unité = n % 10
        amour += unité
        n = n // 10
    if amour < 10:
        return amour
    else:
        return nombre_amour(amour)

prénom1, prénom2 = input().split()
print(nombre_amour(valeur(prénom1)), nombre_amour(valeur(prénom2)))
```


### Commentaires
* On peut réécrire la fonction `valeur` avec une seule instruction :
    * `    return sum(ord(lettre) - ord('A') for lettre in mot)`
    * La fonction `sum` renvoie la somme des valeurs de l'objet en paramètre. C'est un style de programmation plus **fonctionnel**.
* La fonction `nombre_amour` est ici donnée en version récursive.
* Une version très courte (mais un peu technique, et peu lisible) pour ce problème peut s'écrire :
```python
def f(x):
    return sum(ord(c) - ord('A') for c in x)

def g(x):
    return x if x<10 else g(x//10 + x%10)

a, b = input().split()
print(g(f(a)), g(f(b)))
```
