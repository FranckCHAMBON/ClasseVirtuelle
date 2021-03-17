# [Chocolats](https://prologin.org/train/2011/semifinal/chocolats)

> Niveau 1

## Énoncé

Joseph Marchand aime ses amis et il sait que ses amis aiment le chocolat. Il décide donc de leur offrir à tous des ballotins de chocolat faits maison. Seulement, s'y prenant au dernier moment, il n'a pas le temps de préparer tous les chocolats à temps. Il décide alors que seuls ses amis en couple recevront des chocolats ! Étant de nature curieuse, il aimerait bien connaître le nombre moyen de chocolats qu'il va offrir à ses amis. De plus, Joseph Marchand offre toujours un nombre impair de chocolats à ses amis (et donc un nombre pair à ses amis en couple).

Connaissant le tableau de toutes ses commandes prévues, vous devez renvoyer le nombre moyen de chocolats qu'il va offrir, **en ne prenant en compte que les couples !**

Dans l'exemple 1 ci-dessous, Joseph Marchand va préparer en moyenne (6 + 10 + 8)/3 chocolats.

### Entrée

* Sur la première ligne, l'entier $N$ correspondant au nombre d'amis auxquels il avait prévu d'offrir des chocolats.
* Sur la ligne suivante, le nombre de chocolats qu'il doit préparer.

### Sortie

* La moyenne (tronquée) des nombres de chocolats pairs.

### Contraintes

*  $1 \leqslant N \leqslant 10\,000$
*  Le nombre maximal de chocolats que Joseph offre par couple (et donc aussi par personne) est de $5\,000$.

### Exemple

Entrée

    5
    6 10 3 5 8

Sortie

    8

## Solution

```python
"""
auteur : Franck CHAMBON
Régional 2011 - Problème 2 - Chocolats
https://prologin.org/train/2011/semifinal/chocolats
"""
# 0. Cœur du problème
def moyenne_nombres_pairs(ma_liste: list[int]) -> int:
    """Renvoie la moyenne tronquée des nombres pairs de `ma_liste`
    >>> moyenne_nombres_pairs([1, 2, 3, 4])
    3
    >>> moyenne_nombres_pairs([12, 22, 3, 0])
    11
    """
    ma_liste_filtrée = [x for x in ma_liste if x % 2 == 0]
    moyenne_filtrée_tronquée = sum(ma_liste_filtrée) // len(ma_liste_filtrée)
    return moyenne_filtrée_tronquée

# import doctest
# doctest.testmod()
# exit(0)

# 1. Lecture
nb_chocolats = int(input())
chocolats = list(map(int, input().split()))

# 2. Écriture
print(moyenne_nombres_pairs(chocolats))
```

### Commentaire

Ceci était une version fonctionnelle, on peut écrire un code plus simple.

```python
nb_tours = int(input())
nb_chocolats = 0
nb_couples = 0
for x in map(int, input().split()):
    if x % 2 == 0:
        nb_couples += 1
        nb_chocolats += x
print(nb_chocolats // nb_couples)
```