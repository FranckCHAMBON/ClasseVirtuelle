# DM de l'élève



## Épreuve régionale


### 42

@import "./E1.py"

#### Commentaires de correction

TB.



### Escalier

@import "./E2.py"

#### Commentaires de correction

TB, mais où est le doctest ?



### Grand écart

@import "./E3.py"

#### Commentaires de correction

Ceci est inutile
```python
        else: 
            pass
```

Revoir PEP8, et espace après virugule.



### Initiales

@import "./E4.py"

#### Commentaires de correction


Il vaut mieux accumuler dans une liste (muable), plutôt que sur des chaînes (immuables) elles sont recopiées à chaque fois, et c'est lent !!!
À la fin, tu colles avec un `"".join(...)`



### Mot le plus long

@import "./E5.py"

#### Commentaires de correction

TB.

`nb_caractères` : mieux avec un `s` à la fin...



### Nombres impairs

@import "./E6.py"

#### Commentaires de correction

TB, mais le `print` dans la fonction, c'est pas top.



### Table de multiplication

@import "./E7.py"

#### Commentaires de correction

TB, ici le doctest était pénible, et inutile...




### Puissance 4

@import "./E8.py"

#### Commentaires de correction

Vraiment TB !!!



### Puzzle

@import "./E9.py"

#### Commentaires de correction

Bien, mais trop long.



### Solitaire

@import "./E10.py"

#### Commentaires de correction

TB.



### Anagrammes

@import "./E11.py"

#### Commentaires de correction

TB.



### Plages du Pacifique

@import "./E12.py"

#### Commentaires de correction

On ne peut pas le résoudre par balayage, un balayage évite les méandres...
Il faut le voir comme un garphe.

### Plan de métro

Non rendu.


## Qualification


## Cases inaccessibles

@import "./Q1.py"

#### Commentaires de correction

`recherche_chemin` devrait renvoyer un booléen. Le style du code est ici d'un codeur en C.

L'algorithme n'est pas efficace, il faut mémoriser les cases déjà visitées.



## Comparer des chaînes

@import "./Q2.py"

#### Commentaires de correction

On peut faire bien plus simple. Voir corrigé.


## Les trois nombres

@import "./Q3.py"

#### Commentaires de correction

> **Erreur**
```python
        for y in range(x,3):
```
Devrait être 
```python
        for y in range(x + 1, 3):
```
Ton programme échouerait avec `10 20 30`.

Sinon, c'est une bonne idée.

## Nombre de voyelles

@import "./Q4.py"

#### Commentaires de correction

TB.
