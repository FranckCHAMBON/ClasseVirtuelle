# [Équilibre](https://prologin.org/train/2011/semifinal/equilibre)

> Niveau 2

## Énoncé

Joseph Marchand est à bout. Pour la 3<sup>e</sup> fois cette semaine, il a renversé son plateau au fast food. Afin d'éviter à l'avenir cette inconvenance, notre compère souhaite concevoir un plateau intelligent. Celui-ci sera capable de préciser une fois chargé où Joseph Marchand doit placer sa main afin que le plateau tienne en équilibre.

On considère un plateau de $300~\text{mm}$ de longueur et $250~\text{mm}$ de largeur. Avec la liste des $N$ objets à placer sur le plateau, leur position ($x$ et $y$ en millimètres en comptant à partir de l'angle supérieur gauche) et leur poids (en grammes), déterminez la position $(x, y)$ sous le plateau à laquelle Joseph Marchand doit placer sa main pour tenir le plateau en équilibre. Il suffit de trouver une position telle que le poids soit réparti équitablement de chaque côté du point de support.

### Entrée

+ Sur la première ligne, le nombre $N$ d'objets posés sur le plateau. $N$ est entier et supérieur strictement à zéro.
+ Sur les $N$ lignes suivantes, la position en $X$, $Y$ et le poids $W$ des objets séparés par des espaces. $X$, respectivement $Y$, est un nombre décimal compris entre $0$ et la longueur, respectivement la largeur. $W$ est un décimal strictement supérieur à zéro.

### Sortie

Sur une seule ligne, la position en $X$ et en $Y$ du point où Joseph Marchand doit placer sa main, $X$ et $Y$ étant des nombres entiers tronqués.

### Contraintes

* $1 \leqslant N \leqslant 10\,000$
* $0 \leqslant X \leqslant 300$
* $0 \leqslant Y \leqslant 250$
* $0 \leqslant W \leqslant 10\,000$
* La somme des poids $(W)$ est supérieure strictement à $0$.

#### Contraintes d'exécution

+ Utilisation mémoire maximum : 1000 kilo-octets
+ Temps d'exécution maximum : 100 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    2
    203 138 27
    147 177 22

Exemple de sortie

    177 155

---

Exemple d'entrée

    6
    45 169 29
    31 130 5
    139 85 4
    205 220 6
    205 76 2
    293 8 1

Exemple de sortie

    84 156

---

## Solution

```python
"""
auteur : Franck CHAMBON
Régional 2011 - Problème 8 - Équilibre
https://prologin.org/train/2011/semifinal/equilibre
"""

# 0. Initialisation
somme_pondérée_x = 0.0
somme_pondérée_y = 0.0
somme_poids = 0.0

# 1. Lecture et cumul
nb_objets = int(input())
for i in range(nb_objets):
    x, y, poids = map(float, input().split())
    somme_pondérée_x += x * poids
    somme_pondérée_y += y * poids
    somme_poids      += poids

# 2. Calcul et écriture
centre_gravité_x = somme_pondérée_x / somme_poids
centre_gravité_y = somme_pondérée_y / somme_poids
print(int(centre_gravité_x), int(centre_gravité_y))
```
