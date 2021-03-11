# DM de l'élève



## Épreuve régionale


### 42

@import "./E1.py"

#### Commentaires de correction

Tu aurais pu mettre aussi une fonction...



### Escalier

@import "./E2.py"

#### Commentaires de correction

Tu aurais pu mettre aussi une fonction...

`x` : nom de variable peu clair.

`hauteur_marche` : pourquoi ce nom de variable ?

`"X" * x` : style non recommandé, mais possible



### Grand écart

@import "./E3.py"

#### Commentaires de correction

C'est bien, il y a fonction avec *doctest* !!!

`effectif`, c'est mieux que `nb_de_nombres`

Pourquoi avoir une liste de *string* plutôt que de *integer* ???


### Initiales

@import "./E4.py"

#### Commentaires de correction

```python
>>>cherche_initiales([ # erreur
>>> cherche_initiales([ # OK
```


### Mot le plus long

@import "./E5.py"

#### Commentaires de correction

C'est bien, il y a fonction avec *doctest* !!!



### Nombres impairs

@import "./E6.py"

#### Commentaires de correction

C'est bien, il y a fonction avec *doctest* !!!



### Table de multiplication

@import "./E7.py"

#### Commentaires de correction

Ici le style n'est pas formidable, une liste de liste ne se justifie pas.

Les identifiants `x`, `y`, `z` ne sont pas clairs du tout...



### Puissance 4

@import "./E8.py"

#### Commentaires de correction

Ligne 17 : il vaut mieux mettre des parenthèses aux tests, pour confirmer les priorités opératoires.

Le code est peu clair, on ne comprend pas pourquoi il y a des appels récursifs (en particulier)...
Mais il a le mérite d'être découpé en fonctions ; c'est bien.



### Puzzle

@import "./E9.py"

#### Commentaires de correction

Le code est peu clair, on ne comprend pas pourquoi il y a des appels récursifs (en particulier)...
Mais il a le mérite d'être découpé en fonctions ; c'est bien.

Il y a beaucoup plus simple comme façon de faire !!!


### Solitaire

@import "./E10.py"

#### Commentaires de correction

Le code est peu clair, on ne comprend pas pourquoi il y a des appels récursifs (en particulier)...
Mais il a le mérite d'être découpé en fonctions ; c'est bien.

`y` : nom de variable peu clair. ???



### Anagrammes

@import "./E11.py"

#### Commentaires de correction

Le code est très peu clair, on ne comprend pas ce qu'il fait. ???




## Qualification


## Cases inaccessibles

@import "./Q1.py"

#### Commentaires de correction

Le code est très peu clair, on ne comprend pas ce que fait le code. ???

Ce n'est pas la bonne méthode pour le résoudre.



## Comparer des chaînes

@import "./Q2.py"

#### Commentaires de correction

Utiliser `.sort()` c'est comme utiliser `<=` ; c'est interdit aussi ici ;-)


## Les trois nombres

@import "./Q3.py"

#### Commentaires de correction

Il y a fonction et *doctest*, c'est bien.

Inutile de passer `somme` en paramètre.

Deuxième méthode sympa, mais il vaut mieux travailler avec les entiers plutôt qu'avec des chaînes de caractères.


## Nombre de voyelles

@import "./Q4.py"

#### Commentaires de correction

La liste de voyelles pourrait rester dans le corps de la fonction, inutile de la passer en paramètre...
