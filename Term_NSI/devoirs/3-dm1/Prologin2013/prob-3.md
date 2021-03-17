# [Problème 3](https://prologin.org/train/2013/semifinal/xor)
> XOR

Niveau 1

## Énoncé

On vous donne une liste de nombres. Tous sont présents en double sauf un, qui n'apparaît une seule fois. Vous devez déterminer lequel.

### Entrée

+ Sur la première ligne, le nombre $N$ de nombres de la liste.
+ Sur la deuxième ligne, la liste des nombres $a_i$.

### Sortie

Un entier, représentant l'unique nombre présent une seule fois dans la liste.

### Contraintes

+ $1 \leqslant N \leqslant 1000$
+ $0 \leqslant a_i < 1\,000\,000$

#### Contraintes d'exécution

+ Utilisation mémoire maximum : 1000 kilo-octets
+ Temps d'exécution maximum : 100 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    3
    18 42 18

Exemple de sortie

    42

---

Exemple d'entrée

    5
    1 2 3 3 2

Exemple de sortie

    1

---

## Indices

Nous verrons plusieurs méthodes de résolution, avec différentes complexités.
+ La meilleure utilise l'opérateur `XOR`, le ou exclusif bit-à-bit ; difficile à inventer vous-même.
+ Cependant vous trouverez une méthode facile en triant le tableau des nombres...

## Solution

### Basique

```python
"""
auteur : Franck CHAMBON
Régional 2013 - Problème 3 - XOR
https://prologin.org/train/2013/semifinal/xor
"""

def unique(nombres: list[int]) -> int:
    """Renvoie l'élément unique d'une liste de `nombres`,
       quand les autres sont en double.

    >>> unique([18, 42, 18])
    42

    >>> unique([1, 18, 42, 18, 1])
    42

    """
    nb_triés = sorted(nombres) # une copie triée
    nb_triés.append(1_000_001) # on ajoute un dernier pour avoir un nombre pair
    # 1,1,  3,3,  5,5,  7,8,  8,9,  9,10,  10,10 ...
    # le premier couple distinct indique l'élément unique ; à gauche
    n = len(nb_triés)
    for i in range(0, n, 2):
        if nb_triés[i] != nb_triés[i+1]:
            return nb_triés[i]


import doctest
doctest.testmod()

effectif = int(input())
nombres = list(map(int, input().split()))

print(unique(nombres))
```

### *Smart*

On utilise la propriété de `XOR`, le ou exclusif bit-à-bit.

Cet opérateur binaire est :
+ commutatif : $a \text{ XOR } b = b \text{ XOR } a$
+ associatif : $(a \text{ XOR } b) \text{ XOR } c = a \text{ XOR } (b \text{ XOR } c)$
+ et on a : $a \text{ XOR } a = 0$
+ et aussi : $a \text{ XOR } 0 = a$

De sorte que dans une liste où tous les nombres sont en doublon, un $\text{XOR}$ de tous les nombres conduit à zéro, en effet on $\text{XOR}$ dans l'ordre que l'on veut, le résultat.

Le dernier nombre seul, en appliquant le dernier $\text{XOR}$ avec zéro reste inchangé.

D'après les propriétés de $\text{XOR}$, on peut faire les opérations dans l'ordre de la liste.


```python
effectif = int(input())
nombres = map(int, input().split()) 

unique = 0
for n in nombres:
    unique = unique ^ n
    # unique ^= n # équivalent

print(unique)
```


Et avec un style fonctionnel, on a :
```python
from functools import reduce
from operator import xor

effectif = int(input())
nombres = map(int, input().split())

unique = reduce(xor, nombres)

print(unique)
```

On pourrait même remplacer les trois dernières lignes par :

```python
print(reduce(xor, map(int, input().split())))
```

Mais le code est plus lisible sur trois lignes, et tout aussi efficace.
