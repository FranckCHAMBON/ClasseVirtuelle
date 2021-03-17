# [Tetris](https://prologin.org/train/2011/semifinal/tetris)

> Niveau 2

## Énoncé

Joseph Marchand est un grand fan du célèbre jeu Tetris. Il a ainsi adapté ce grand classique du jeu vidéo à sa cafetière (Joseph Marchand est un grand bricoleur). Seulement, les capacités de Joseph Marchand en programmation sont limitées, et il ne sait pas comment implémenter la suppression des lignes.

Afin d'aider Joseph Marchand, et connaissant l'état actuel de l'écran de jeu, écrivez une fonction renvoyant le nombre de lignes qui doivent être supprimées, c'est-à-dire qui ne contiennent que des `1`.

### Entrée

+ Sur la première ligne, l'entier $N$ correspondant au nombre de lignes du Tetris.
+ Sur la deuxième ligne, l'entier $M$ correspondant au nombre de colonnes du Tetris.
+ Sur les $N$ lignes suivantes, $M$ entiers (`0` ou `1`). Les `0` représentent les trous et les `1` les blocs.

### Sortie

Le nombre de lignes qui doivent être supprimées.

### Contraintes

+ $1 \leqslant N \leqslant 1000$
+ $1 \leqslant M \leqslant 100$

#### Contraintes d'exécution

+ Utilisation mémoire maximum : 2048 kilo-octets
+ Temps d'exécution maximum : 400 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    3
    5
    0 0 0 0 0
    1 1 1 1 1
    1 1 0 1 1

Exemple de sortie

    1 

---

Exemple d'entrée

    7
    10
    0 0 1 1 0 1 0 1 0 1
    1 0 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 0 1 1 1 1 1 0 1 1

Exemple de sortie

    3 

---

## Solution

```python
"""
auteur : Franck CHAMBON
Régional 2011 - Problème 7 - Tetris
https://prologin.org/train/2011/semifinal/tetris
"""

# 0. Cœur du problème
def nb_suppressions(tetris: list[int]) -> int:
    """Renvoie le nombre de lignes que l'on peut supprimer dans
    un Tetris, un tableau 2D rempli de 0 et 1.

    >>> nb_suppression([[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1]])
    1

    Astuce : si la somme d'une ligne est égale à nb_colonnes,
             alors on peut la supprimer.
    """
    if len(tetris) == 0:
        return 0 # Tetris vide
    nb_colonnes = len(tetris[0])

    # version fonctionnelle
    return sum(1 for ligne in tetris if sum(ligne) == nb_colonnes)
    
    # version itérative
    nb_lignes_pleines = 0
    for ligne in tetris:
        if sum(ligne) == nb_colonnes:
            nb_lignes_pleines += 1
    return nb_lignes_pleines
    

# 1. Lecture
nb_lignes = int(input())
nb_colonnes = int(input())
tetris = [list(map(int, input().split())) for _ in range(nb_lignes)]

# 2. Écriture
print(nb_suppressions(tetris))
```
