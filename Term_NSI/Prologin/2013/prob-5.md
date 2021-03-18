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

```python
"""
auteur : Franck CHAMBON
Régional 2013 - Problème 5 - Gravity
https://prologin.org/train/2013/semifinal/gravity
"""

def gravite(chaîne):
    """Renvoie la chaîne avec les '.' au début.

    >>> gravite('a.zer..ty')
    '...azerty'

    """
    # on construit une liste sans les '.'
    chute = []
    for x in chaîne:
        if x != '.':
            chute.append(x)
    # variante fonctionnelle des 4 lignes précédentes
    chute = [x for x in chaîne if x != '.']
    
    # n : la quantité de '.' manquants
    n = len(chaîne) - len(chute)
    # on ajoute au début les '.' manquants
    chute = ['.' for _ in range(n)] + chute
    # join : pour obtenir une chaîne collée
    return "".join(chute)

# 1. Test des fonctions
import doctest
doctest.testmod()

# 2. Lecture de l'entrée
nb_lignes, nb_colonnes = map(int, input().split())
grille = [list(input()) for _ in range(nb_lignes)]

# 3. Résolution
grille_sortie = [['.' for _ in range(nb_colonnes)] for _ in range(nb_lignes)]
for j in range(nb_colonnes):
    colonne_j = [grille[i][j] for i in range(nb_lignes)]
    # la colonne_j va subir la gravité
    colonne_j = gravite(colonne_j)
    for i in range(nb_lignes):
        grille_sortie[i][j] = colonne_j[i]

# 4. Écriture de la sortie
for ligne in grille_sortie:
    print("".join(ligne))
```
