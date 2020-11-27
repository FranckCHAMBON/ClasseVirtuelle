# DS2 - Exercice 1
Écrire un script qui lit un entier `nb_notes` , puis `nb_notes` entiers (chacun sera une note) et affiche la moyenne des notes.
> Attention, certaines notes seront fausses, il ne faut compter que les notes de $0$ à $20$.

Exemple d’entrée :
```
        3
        10
        100
        16
```

La sortie attendue est ici la moyenne des deux notes $10$ et $16$ :
```
        13.0
```

Votre script devra être écrit soigneusement.

## Correction

### Une version avec beaucoup trop de commentaires

```python
nb_notes = int(input()) # un entier
nb_notes_valides = 0 # un entier
somme_notes_valides = 0.0 # un flottant ...
for _ in range(nb_notes):
    note = float(input()) # un flottant, oui une note peut être 12.5
    if (0.0 <= note) and (note <= 20.0): # tests entre flottants !
        nb_notes_valides = nb_notes_valides + 1 # addition entre entiers
        somme_notes_valides = somme_notes_valides + note # addition entre flottants

moyenne = somme_notes_valides / nb_notes_valides # quotient de flottants
print(moyenne)
```

### Même version avec peu de commentaires

```python
nb_notes = int(input())
nb_notes_valides = 0
somme_notes_valides = 0.0
for _ in range(nb_notes):
    note = float(input())
    if (0.0 <= note) and (note <= 20.0):
        # la note est valide ; elle compte !
        nb_notes_valides = nb_notes_valides + 1
        somme_notes_valides = somme_notes_valides + note

moyenne = somme_notes_valides / nb_notes_valides
print(moyenne)
```

### Même version avec un peu de sucre syntaxique

```python
nb_notes = int(input())
nb_notes_valides = 0
somme_notes_valides = 0.0
for _ in range(nb_notes):
    note = float(input())
    if 0.0 <= note <= 20.0:
        nb_notes_valides += 1
        somme_notes_valides += note

moyenne = somme_notes_valides / nb_notes_valides
print(moyenne)
```

Un code bien écrit n'a pas besoin de commentaires, les identifiants bien choisis et le style permettent d'avoir un code clair pour tout le monde.
