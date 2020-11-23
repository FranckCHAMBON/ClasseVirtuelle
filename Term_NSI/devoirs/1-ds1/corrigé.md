# DS n°1 - correction

## Exercice 1

Une fonction récursive est une fonction qui s'appelle elle-même, un nombre fini de fois. Ou bien une parmi un groupe de fonctions qui s'appellent elles-mêmes, un nombre fini de fois.

## Exercice 2

```python
def fibonacci(n: int) -> int:
    """Renvoie le terme d'indice n de la suite de Fibonacci.
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(6)
    8
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

## Exercice 3

```python
def mystère1(x: int) −> int :
    """Renvoie 2 à la puissance x.
    >>> mystère1(0)
    1
    >>> mystère1(1)
    2
    >>> mystère1(5)
    32
    """
    assert x >= 0, "x doit être positif"
    if x == 0 :
        return 1
    else :
        return 2 * mystère1(x − 1)
```

```python
def mystère2(lst: list) −> int :
    """Renvoie la somme des éléments de lst.
    >>> mystère2([])
    0
    >>> mystère2([13])
    13
    >>> mystère2([1, 2, 3])
    6
    """
    # lst est une liste d'entiers, peut-être vide
    if lst != [] :
        return lst[0] + mystère2(lst[1:])
    else :
        return 0
```

```python
def mystère3(lst: list) −> bool :
    """Si lst est triée dans l'ordre croissant,
       alors renvoie True
       sinon renvoie False
    remarque, une liste vide ou à un élément est triée
    >>> mystère3([])
    True
    >>> mystère3([13])
    True
    >>> mystère3([13, 13])
    True
    >>> mystère3([10, 24, 32])
    True
    >>> mystère3([32, 24])
    False
    """
    # lst est une liste d'entiers, peut-être vide
    if len(lst) > 1 :
        if lst[0] > lst[1] :
            return False
        else :
            return mystère3(lst[1:])
    else :
        return True
```

## Exercice 4

```python
def fig_c(x: float, y: float, r: float, n: int):
    """Construit la figure avec n niveaux de profondeur de cercle.
    (x, y) : coordonnées du grand cercle
    r : rayon du grand cercle
    """
    if n == 0:
        return
    else:
        cercle(x, y, r)
        fig_c(x + 3*r/2, y,         r/2, n - 1)
        fig_c(x,         y - 3*r/2, r/2, n - 1)

fig_c(0.0, 0.0, 8.0, 4)
```