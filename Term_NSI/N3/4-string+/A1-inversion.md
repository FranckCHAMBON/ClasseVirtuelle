# [Inversion d’une liste de livres](http://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2422)

## Sujet

Souhaitant améliorer ses connaissances scientifiques, votre jeune assistante Ada, vous a demandé de lui créer une liste de livres « à lire absolument », en les classant par ordre de priorité, selon l'intérêt de chaque livre. Un peu distrait(e), vous avez bien créé cette fiche mais en les classant dans l’ordre inverse, du moins intéressant au plus intéressant !

Afin d’éviter de devoir tout refaire, vous décidez d’écrire un petit programme pour inverser rapidement cette liste.

### Contraintes

Chaque titre de livre contient au plus 100 caractères.

### Entrée

* La première ligne contient un entier `nbLivres`, le nombre de livres.

Les `nbLivres` lignes suivantes contiennent chacune un titre de livre.

Les livres sont classés du moins intéressant au plus intéressant.

### Sortie

L’ensemble des titres de livres, un titre par ligne, triés du plus intéressant au moins intéressant.


### Exemple

---

entrée :

```
7
Germinal
Le petit prince
Le meilleur des mondes
L'ecume des jours
L'Odyssee
Les miserables
Crime et Chatiment
```

sortie :

```
Crime et Chatiment
Les miserables
L'Odyssee
L'ecume des jours
Le meilleur des mondes
Le petit prince
Germinal
```

---

## Solution

```python
nb_livres = int(input())
livres = [input() for _ in range(nb_livres)]

for i in range(nb_livres - 1, -1, -1):
    print(livres[i])
```

### Commentaire

Pour itérer sur une liste à l'envers, une bonne solution est de parcourir avec les indices de `longueur - 1` inclus, jusqu'à `0` inclus (donc `-1` exclu), par pas de `-1`.


