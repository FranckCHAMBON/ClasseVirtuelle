# [Calculs et découverte des variables](http://www.france-ioi.org/algo/chapter.php?idChapter=644)

> Correction alternative de certains problèmes


## L'algoréathon

### Sujet

 L'algoréathlon se constitue de trois étapes à effectuer chaque jour : 2 km de natation, 34 km de cyclisme et 6 km de course à pied.

Sachant qu'un sportif répète ces trois étapes pendant 3 jours de suite, vous devez afficher la distance totale qu'il a parcourue à la fin du 1er jour, à la fin du 2e jour, puis à la fin de l'algoréathlon complet.

Afin de rendre l'affichage convivial sur l'écran du robot, vous souhaitez mettre les trois valeurs sur une même ligne, avec une espace entre chaque valeur et la suivante.

### Solution officielle

```python
distJour = 2 + 34 + 6
print(distJour, end = " ")
print(distJour * 2, end = " ")
print(distJour * 3)
```

### Solutions alternatives

On peut utiliser un seul `print`, par défaut le séparateur entre plusieurs objets à imprimer est **une** espace. Oui, espace est féminin en typographie.

```python
distance_1jour = 2 + 34 + 6
print(distance_1jour, distance_1jour * 2, distance_1jour * 3)
```

On peut aussi utiliser les *f-string* à partir de Python 3.6, mais pas sur FranceIOI.

```python
d = 2 + 34 + 6
print(f"{d} {d*2} {d*3}")
```

## Une partie de cache-cache

### Sujet

 Le robot devra compter jusqu'à 100, c'est à dire afficher les entiers de 1 à 100, un par ligne, et ensuite afficher « J'arrive ! ». Ainsi, s'il ne devait compter que jusqu'à 3 au lieu de 100, votre robot devrait afficher :

    1
    2
    3
    J'arrive !

### Solution officielle

```python
compte = 1
for loop in range(100):
   print(compte)
   compte = compte + 1
print("J'arrive !")
```

### Solution alternative

On peut utiliser la variable de boucle, et `range` avec deux paramètres.

```python
for compteur in range(1, 101):
   print(compteur)
print("J'arrive !")
```

Remarque
: `range(1, 101)` se lit : de 1 inclus à 101 exclu. Il y aura $101-1 = 100$ tours de boucle.

## Décollage de fusée

### Sujet

 Votre programme devra lancer le décompte en partant de 100 puis annoncer le décollage, c'est-à-dire afficher une séquence d'annonces de la forme :

    100
    99
    ...
    2
    1
    0
    Décollage ! 

en remplaçant `...` par toutes les valeurs intermédiaires. 

### Solution officielle

```python
compte = 100
for loop in range(101):
   print(compte)
   compte = compte - 1
print("Décollage !")
```

### Solution alternative

On peut utiliser la variable de boucle, et `range` avec trois paramètres.

```python
for compteur in range(100, -1, -1):
   print(compteur)
print("Décollage !")
```

`range(100, -1, -1)` se lit : de 100 inclus à -1 exclu, par pas de -1. Il y aura $(-1-(100))/(-1) = 101$ tours de boucle.

## Construction de pyramide

### Sujet

L'objectif est de construire une tour à l'aide de petits cubes en bois, sachant que la forme de cette tour consiste en un ensemble de grands cubes placés les uns au-dessus des autres. La base de la tour est un cube de taille 17×17×17, c'est-à-dire composé de 17×17×17 = 4 913 petits cubes. Sur ce cube est posé un autre cube de taille 15×15×15. Au-dessus de ce dernier se trouve un cube de 13×13×13. La tour continue ainsi jusqu'à atteindre le sommet, qui consiste en un cube de taille 1×1×1.
Dessin de la tour

Votre programme doit calculer et afficher le nombre total de petits cubes nécessaires pour construire la pyramide. Effectuez les calculs dans le programme en y intégrant une boucle. 

### Solution officielle

```python
nbCubes = 0
largeurArête = 1
for loop in range(9):
   nbCubes = nbCubes + largeurArête * largeurArête * largeurArête
   largeurArête = largeurArête + 2
print(nbCubes)
```

### Solution alternative

On utilise `range` à trois paramètres et une variable de boucle.

```python
nb_cubes = 0
for côté in range(1, 18, 2):
    nb_cubes += côté ** 3
print(nb_cubes)
```

On peut même l'avoir en une ligne avec un style fonctionnel :

```python
print(sum(côté**3 for côté in range(1, 18, 2)))
```

On a créé un objet en compréhension, dont on fait la somme.

