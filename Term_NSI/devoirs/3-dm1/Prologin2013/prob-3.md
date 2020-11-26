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

*À venir*