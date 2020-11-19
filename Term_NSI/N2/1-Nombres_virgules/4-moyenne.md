# Moyenne des notes

## Sujet

 Votre programme doit d'abord lire un premier entier, qui décrit le nombre de notes obtenues. Ensuite, il doit lire chacune de ces notes, qui sont également des nombres entiers. Enfin, il doit afficher la moyenne de toutes ces notes.

### Exemple

entrée :

    3
    10
    14
    15

sortie :

    13.0

## Solution officielle

```python
nombreNotes = int(input())
sommeNotes = 0
for loop in range(nombreNotes):
   note = int(input())
   sommeNotes = sommeNotes + note
print(sommeNotes / nombreNotes)
```

## Solution alternative

Avec un style un plus fonctionnel.

```python
nb_notes = int(input())
somme_notes = sum(int(input()) for _ in range(nb_notes))
print(somme_notes)
```

