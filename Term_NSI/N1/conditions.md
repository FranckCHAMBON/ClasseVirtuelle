# [Conditions avancées, opérateurs booléens](http://www.france-ioi.org/algo/chapter.php?idChapter=648)

> Correction alternative de certains problèmes

## Sujet

On vous donne un intervalle de temps pendant lequel on sait qu'un espion est arrivé, puis la date d'arrivée d'un certain nombre de personnes. Déterminez combien de ces personnes peuvent être cet espion.

Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de l'intervalle pendant lequel on sait que l'espion est arrivé en ville. Il doit ensuite lire un entier nbEntrées, le nombre total de personnes entrées dans la ville, puis les nbEntrées nombres suivants qui représentent les dates d'entrée (non triées) des différentes personnes.

Votre programme doit afficher le nombre de personnes entrées entre les deux dates données, incluses.

### Exemple

entrée :

    6
    10
    5
    7
    11
    8
    3
    6

sortie :

    3

### Solution officielle

```python
dateDébut = int(input())
dateFin = int(input())
nbEntrées = int(input())
nbPersonnes = 0
for loop in range(nbEntrées):
   date = int(input())
   if dateDébut <= date and date <= dateFin:
      nbPersonnes = nbPersonnes + 1
print(nbPersonnes)
```

### Solution alternative

```python
date_début = int(input())
date_fin = int(input())
nb_entrées = int(input())
dates = iter(int(input()) for _ in range(nb_entrées))

nb_suspects = sum(1 for date in dates if date_début <= date <= date_fin)
print(nb_suspects)
```

On peut aussi écrire avec un style encore plus fonctionnel.

```python
est_suspect = lambda date: date_début <= date <= date_fin
nb_suspects = sum(1 for _ in filter(est_suspect, dates))
```