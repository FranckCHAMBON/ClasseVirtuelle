# [Pyramide](https://prologin.org/train/2011/semifinal/pyramide)

> Niveau 1

## Énoncé

Joseph Marchand se met à la construction de pyramides ! Aidez-le dans sa conception en lui affichant une miniature en fonction de la taille choisie.

Connaissant la hauteur de la pyramide, vous devez l'afficher.

### Entrée

* Sur la première ligne, la hauteur de la pyramide.

### Sortie

* La pyramide affichée.

### Contraintes

* $1 \leqslant N \leqslant 100$

#### Contraintes d'exécution

* Utilisation mémoire maximum : 512 kilo-octets
* Temps d'exécution maximum : 400 millisecondes

## Exemples d'entrée/sortie

---

Exemple d'entrée

    1

Exemple de sortie

    *

---

Exemple d'entrée

    3

Exemple de sortie

    *
    **
    ***

---

## Solution

```python
"""
auteur : Franck CHAMBON
Régional 2011 - Problème 4 - Pyramide
https://prologin.org/train/2011/semifinal/pyramide
"""

# 0. Cœur du problème
def affiche_pyramide(hauteur: int) -> None:
    """Affiche une pyramide de `hauteur` donnée.

    >>> affiche_pyramide(1)
    *

    >>> affiche_pyramide(3)
    *
    **
    ***

    """
    return print("\n".join("*" * h for h in range(1, hauteur + 1)))
    
import doctest
doctest.testmod()

    
# 1. Entrée
hauteur = int(input())

# 2. Sortie
affiche_pyramide(hauteur)
```

Une version simple serait :

```python
def affiche_pyramide(hauteur: int) -> None:
    for h in range(1, hauteur + 1):
        print("*" * h)
```

Une version sans la multiplication `str * int` serait :

```python
def affiche_pyramide(hauteur: int) -> None:
    for h in range(1, hauteur + 1):
        # Affiche une ligne de `h` étoiles
        for i in range(h):
            print("*", end="")
        print()
```
