# DM de l'élève



## Épreuve régionale


### 42

@import "./E1.py"

#### Commentaires de correction

Tu aurais pu mettre aussi une fonction...

`n` : choisir un meilleur nom de variable



### Escalier

@import "./E2.py"

#### Commentaires de correction

Tu aurais pu mettre aussi une fonction...

`x` : nom de variable peu clair.

`nb_marches` : à mettre au pluriel !

`"X" * x` : style non recommandé, mais possible



### Grand écart

@import "./E3.py"

#### Commentaires de correction

Tu aurais pu mettre aussi une fonction...

On attend des fonctions avec *doctest* !!!

Noms de variables peu clairs.



### Initiales

Non rendu.


### Mot le plus long

Non rendu.


### Nombres impairs

Non rendu.



### Table de multiplication

@import "./E7.py"

#### Commentaires de correction

Tu aurais pu mettre aussi une fonction...


PEP8 : mettre espace après virgule ; exemple :
```python
    print(chiffre, "x", y, "=", chiffre*y, sep="")
```

### Puissance 4

@import "./E8.py"

#### Commentaires de correction

Indiquer l'origine de l'inspiration quand du code est emprunté.
Style curieusement différent des exercices précédents...

On attend des fonctions avec *doctest* !!!

Ligne 31 : le `return ""` est inutile, et incohérent au niveau des types.



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

Non rendu.


## Comparer des chaînes

@import "./Q2.py"

#### Commentaires de correction

1. L'auteur de ce code fait du Python2, pas du Python3 ; ce n'est pas un élève en NSI.
2. L'esprit du problème est de ne pas utiliser les outils *builtin* comme `<` ou `.sort()`
3. On attend une fonction avec *doctest*
4. `mot_1` est plus clair que `mot1`



## Les trois nombres

@import "./Q3.py"

#### Commentaires de correction

On attend une fonction avec *doctest*

Cela permet, entre autres choses, de n'avoir qu'un seul `print` dans ce programme, or on veut un code factorisé !!!


## Nombre de voyelles

@import "./Q4.py"

#### Commentaires de correction

On attend une fonction avec *doctest*

`voyelle` : l'identifiant est mal choisi, car tu comptes l'espace aussi.

`A` : identifiant très mal choisi.

`print(A)` au lieu de `print (A)`

Contrairement à un problème de FranceIOI, ici on ne voulait pas compter l'espace... Il est donc faux ici !!!