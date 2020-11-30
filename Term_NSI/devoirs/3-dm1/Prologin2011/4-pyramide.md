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
def pyramide(hauteur: int) -> str:
    """Renvoie une pyramide de hauteur
    >>> pyramide(1)
    '*'
    >>> pyramide(3)
    '*\\n**\\n***'
    """
    return "\n".join("*" * h for h in range(1, 1+hauteur))
    
# import doctest
# doctest.testmod()
# exit(0)

    
# 1. Entrée
hauteur = int(input())

# 2. Sortie
print(pyramide(hauteur))
```