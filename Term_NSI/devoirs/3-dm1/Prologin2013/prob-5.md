# [Problème 5](https://prologin.org/train/2013/semifinal/gravity)
> Gravity

Niveau 2

## Énoncé

Joseph Marchand marche dans la rue. Il neige. En fin observateur, il remarque que plus la neige tombe, plus le niveau monte ! Ainsi, comme Newton 3 siècles avant lui, il s'interroge sur le mystérieux phénomène de la gravité (bien qu'il n'y ait pas de rapport avec le fait que le niveau de la neige monte).

Il décide donc de mener une petite expérience, à savoir placer plusieurs blocs dans une pièce non soumise à la gravité, puis de simuler la gravité afin d'obtenir le même résultat (la chute correcte des blocs) qu'avec la « vraie » gravité.

### Entrée

L'entrée standard contient $L + 1$ lignes :

+ Sur la première ligne, le nombre $L$ de lignes de la grille et le nombre $C$ de colonnes de la grille, séparés d'un espace.
+ Sur les $L$ lignes suivantes, le tableau de caractères $L × C$ représentant les blocs, le caractère `.` représentant une absence de bloc.

### Sortie

Vous devez écrire $L$ lignes sur la sortie standard : la même grille avec les blocs tombés en bas.

### Contraintes

+ $0 < L < 1000$ où $L$ est le nombre de lignes de la grille.
+ $0 < C < 500$ où $C$ est le nombre de colonnes de la grille.

#### Contraintes d'exécution

+ Utilisation mémoire maximum : 1000 kilo-octets
+ Temps d'exécution maximum : 2000 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    1 1
    a

Exemple de sortie

    a

---

Exemple d'entrée

    3 4
    tr..
    ...y
    .d..

Exemple de sortie

    ....
    .r..
    td.y

---

## Indices

Il sera judicieux de fabriquer une fonction qui prend une liste ou une chaîne de caractères et qui renvoie une liste ou une chaîne avec les `.` en tête. **Un peu comme** :
```python
>>> gravite('a.zer..ty')
'...azerty'
```

## Solution

*À venir*