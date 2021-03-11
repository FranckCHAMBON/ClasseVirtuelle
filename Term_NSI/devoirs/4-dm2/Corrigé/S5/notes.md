# DM de l'élève



## Épreuve régionale


### 42

@import "./E1.py"

#### Commentaires de correction

On attend ici aussi une fonction.



### Escalier

@import "./E2.py"

#### Commentaires de correction

Une fonction pour l'escalier aurait été bien aussi.



### Grand écart

@import "./E3.py"

#### Commentaires de correction

Il valait mieux faire une boucle avec un tour de moins.



### Initiales

@import "./E4.py"

#### Commentaires de correction

On attend ici aussi fonction et *doctest*.



### Mot le plus long

@import "./E5.py"

#### Commentaires de correction

Style fonctionnel, c'est bien, tu pouvais condenser encore en deux lignes.

Mais on attendait une fonction avec *doctest*.



### Nombres impairs

@import "./E6.py"

#### Commentaires de correction

C'est bien, mais avec *doctest* c'est mieux.



### Table de multiplication

@import "./E7.py"

#### Commentaires de correction

`range(1, 10)` est mieux que `range(1,10)`

*doctest* ?



### Puissance 4

@import "./E8.py"

#### Commentaires de correction

> Retourne un booléen si...
Mieux : Retourne le booléen `True` si...

Le `break` peut presque toujours être évité en créant... **une fonction**.



### Puzzle

@import "./E9.py"

#### Commentaires de correction

1. Erreur
```python
            if not est_dans_le_puzzle(x_départ+delta_x, y_départ+delta_y):
                return False
```
Il vaut mieux
```python
            if (1 == pièce[delta_x][delta_y]) and (not est_dans_le_puzzle(x_départ+delta_x, y_départ+delta_y)):
                return False
```
En effet, si un zéro est en dehors du cadre, c'est pas grave...


2. Pas terrible
```python
        if puzzle_correct:
            break
```
il vaut mieux mettre cette section dans une fonction, et au lieu de `puzzle_correct = True`, faire un `return True`



### Solitaire

@import "./E10.py"

#### Commentaires de correction

Une fonction pour savoir si une bille est dans le jeu aurait été idéale...
Sinon, c'est bien.



### Anagrammes

@import "./E11.py"

#### Commentaires de correction

Cartouche manquant

Bonne idée, mais un peu long.



### Plages du Pacifique

@import "./E12.py"

#### Commentaires de correction

Ce code ne peut pas fonctionner.
On ne peut pas balayer lignes et colonnes...
Il faut le voir comme un problème de graphe avec un parcours à écrire.

Ton code ne peut pas voir les recoins en forme de S. Il "ne remonte pas" !!!


### Plan de métro

@import "./E13.py"


#### Commentaires de correction

Il y a un beau travail ici !!!

C'est un très bon début.
Bravo même s'il ne fonctionne pas.

Étudie le corrigé pour voir le détail qui manque.




## Qualification


## Cases inaccessibles

@import "./Q1.py"

#### Commentaires de correction

Bravo, très bien.



## Comparer des chaînes

@import "./Q2.py"

#### Commentaires de correction

Arghh, un `break` ; on peut l'éviter avec une fonction, et obtenir un *doctest* au passage.



## Les trois nombres

@import "./Q3.py"

#### Commentaires de correction

Une fonction, c'est beaucoup mieux, et on peut factoriser ; il n'y aurait qu'un seul `print`...




## Nombre de voyelles

@import "./Q4.py"

#### Commentaires de correction

Bien, mais mieux avec une fonction...
