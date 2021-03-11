# DM de l'élève

Tous les *doctest* sont faux ; il faut revoir les méthodes.

Trop peu de travail dans l'ensemble.


## Épreuve régionale


### 42

@import "./E1.py"

#### Commentaires de correction

Ton *doctest* n'est pas activé.


### Escalier

@import "./E2.py"

#### Commentaires de correction

`nb_marches` avec un `s`.
Erreur du *doctest*.


### Grand écart

@import "./E3.py"

#### Commentaires de correction
```python
    for x in range(nb_tableau):
        if x == nb_tableau - 1:
            break
```
On n'aime pas les `break` ; ici il suffisait de faire un tour de moins à la boucle.


### Initiales

@import "./E4.py"

#### Commentaires de correction

`capwords` c'était tricher...


### Mot le plus long

@import "./E5.py"

#### Commentaires de correction

`split` était tricher ici aussi.
`mot` n'est pas le meilleur choix, c'est la longueur qu'il vaut mieux conserver et mettre à jour.



### Nombres impairs

@import "./E6.py"

#### Commentaires de correction

On préfère renvoyer ta liste, et faire l'affichage en dehors de la fonction.



### Table de multiplication

@import "./E7.py"

#### Commentaires de correction

Les *fstring* c'est mieux !!!



### Puissance 4

@import "./E8.py"

#### Commentaires de correction

Erreur d'indentation

### Puzzle

Non rendu.


### Solitaire

Non rendu.


### Anagrammes

Non rendu.


### Plages du Pacifique

Non rendu.


### Plan de métro

Non rendu.


## Qualification


## Cases inaccessibles

@import "./Q1.py"

#### Commentaires de correction

Quasi vide.

## Comparer des chaînes

@import "./Q2.py"

#### Commentaires de correction

```python
   for x in range(nb_caractère_min):
        if x + 1 == nb_caractère_min:
```
Ceci ne peut pas se produire !!!

## Les trois nombres

@import "./Q3.py"

#### Commentaires de correction

Ce code doit être factorisé.



## Nombre de voyelles

@import "./Q4.py"

#### Commentaires de correction

On aurait aimé ne pas voir ni `lower`, ni `upper`, ni `in` en test d'appartenance.