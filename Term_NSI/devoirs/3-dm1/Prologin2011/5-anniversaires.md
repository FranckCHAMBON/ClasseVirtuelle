# [Anniversaires](https://prologin.org/train/2011/semifinal/anniversaires)

> Niveau 2 

## Énoncé

Joseph Marchand produit des ballons de baudruche. Pour monétiser au mieux son activité, il regarde régulièrement sur VisageLivre™ les anniversaires de ses amis afin de leur vendre des ballons. Cependant, Joseph Marchand est fainéant et veut donc produire tous ses ballons en une fois pour être tranquille ensuite. Il veut évidemment aussi en produire le nombre minimal.

Pour chaque anniversaire, un nombre $B$ de ballons est nécessaire. À la fin de l'anniversaire, $B/2$ ballons sont craqués et les autres $B/2$ ballons sont encore en bon état. Radin comme il est, Joseph les récupère pour les anniversaires suivants.

En supposant que vous ayez la liste des $N$ prochains anniversaires, déterminez le nombre de ballons à produire au départ pour en avoir suffisamment pour tous les anniversaires.

### Entrée

* Sur la première ligne, l'entier $N$.
* Sur la seconde ligne, le nombre $B$ de ballons nécessaire pour chaque anniversaire.

### Sortie

* Le nombre minimal de ballons à produire au départ pour satisfaire le besoin de tous les anniversaires.

### Contraintes

* $1 \leqslant N \leqslant 10\,000$
* $2 \leqslant B \leqslant 10\,000$
* $B$ pair.

#### Contraintes d'exécution

* Utilisation mémoire maximum : 2048 kilo-octets
* Temps d'exécution maximum : 400 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    2
    20 20

Exemple de sortie

    30

---

Exemple d'entrée

    4
    10 20 30 40

Exemple de sortie

    70

---

Exemple d'entrée

    3
    80 10 80

Exemple de sortie

    125
---

## Solution

```python
"""
auteur : Franck CHAMBON
Régional 2011 - Problème 5 - Anniversaires
https://prologin.org/train/2011/semifinal/anniversaires
"""

# 0. Cœur du problème
def nb_ballons(ma_liste: list) -> int:
    """Renvoie le nombre de ballons nécessaires suivant l'énoncé.
    >>> nb_ballons([20, 20])
    30
    >>> nb_ballons([10, 20, 30, 40])
    70
    >>> nb_ballons([80, 10, 80])
    125
    """
    stock = 0
    besoin_total = 0
    for x in ma_liste:
        if x > stock:
            besoin_total += x - stock
            stock = x // 2
        else:
            stock -= x // 2
    return besoin_total

# import doctest
# doctest.testmod()
# exit(0)


# 1. Lecture
nb_anniversaires = int(input())
anniversaires = list(map(int, input().split()))

# 2. Écriture
print(nb_ballons(anniversaires))
```

### Commentaire

    Si on prend en entrée ces 3 anniversaires : 80, 10 et 80.
    On voit qu'il faut :

        80 ballons pour le premier, j'en ai 0, il m'en faut 80, il m'en reste 0 + 80/2 = 40 ;
        10 ballons pour le second, j'en ai 40, il m'en faut 0, il m'en reste 30 + 10/2 = 35 ;
        80 ballons pour le dernier, j'en ai 35, il m'en faut 45, et on se fiche du reste.

    Il me faut alors au total : 80 + 0 + 45 ballons, soit 125.