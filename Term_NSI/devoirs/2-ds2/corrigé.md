# Corrigé du DS n°2

On propose trois versions :
* une version sans dictionnaire, plus complexe à écrire...
* une version avec dictionnaire, très simple
* un code avec POO

## Première version sans dictionnaire

On va stocker dans un tableau `amis_noms` les noms des amis, chacun donc avec un indice entre $0$ et `nb_amis` exclus.
On stocke dans un autre tableau, avec les mêmes indices, les coordonnées associées.

Ensuite on boucle sur les lieux à visiter pour calculer la distance parcourue.

## Lecture de l'entrée

```python
nb_amis = int(input())
amis_noms = ["" for _ in range(nb_amis)]
amis_coord = [(0.0, 0.0) for _ in range(nb_amis)]
for i in range(nb_amis):
    nom, x_texte, y_texte = input().split()
    amis_noms[i] = nom
    amis_coord[i] = (float(x_texte), float(y_texte))

nb_lieux = int(input())
lieux = [input() for _ in range(nb_lieux)]
```

## Calcul d'une distance entre deux points

C'est un classique à connaître.

```python
from math import sqrt
def distance((x1, y1), (x2, y2)):
    dx = x2 - x1
    dy = y2 - y1
    return sqrt(dx*dx + dy*dy)
```

## Le cœur du problème

```python
def donne_indice(nom):
    for i in range(nb_lieux):
        if amis[i] == nom:
            return i

def distance_totale():
    if nb_lieux == 0:
        return 0.0
    i = donne_indice(lieux[0])
    x1, y1 = amis_coord(i)
    distance_trajet = 0.0
    for lieu in lieux[1:]:
        i = donne_indice(lieu)
        x2, y2 = amis_coord(i)
        distance_trajet += distance((x1, y1), (x2, y2))
        x1, y1 = x2, y2
    return distance_trajet

print(round(distance_totale(), 2))
```


## Version avec dictionnaire

L'objectif étant de ne plus avoir besoin de travailler avec l'indice, et également avoir une méthode intégrée, et plus efficace, de recherche de l'association `nom` - `coordonnées`.

## Lecture de l'entrée

La lecture de l'entrée change, on stocke les amis dans un dictionnaire. C'est plus simple

```python
nb_amis = int(input())
amis = dict()
for _ in range(nb_amis):
    nom, x_texte, y_texte = input().split()
    amis[nom] = (float(x_texte), float(y_texte))

nb_lieux = int(input())
lieux = [input() for _ in range(nb_lieux)]
```

On utilise la même fonction pour la distance entre deux points.

## Le cœur du problème

```python
def distance_totale():
    if nb_lieux == 0:
        return 0.0
    x1, y1 = amis[lieux[0]]
    distance_trajet = 0.0
    for lieu in lieux[1:]:
        x2, y2 = amis[lieu]
        distance_trajet += distance((x1, y1), (x2, y2))
        x1, y1 = x2, y2
    return distance_trajet

print(round(distance_totale(), 2))
```

## Version complète

```python
from math import sqrt
class Point():
    def __init__(self, abscisse, ordonnée):
        "Constructeur"
        self.x = abscisse
        self.y = ordonnée
    
    def distance(self, point):
        "Renvoie la distance de self à point"
        dx = self.x - point.x
        dy = self.y - point.y
        return sqrt(dx*dx + dy*dy)
    
nb_amis = int(input())
amis = dict()
for _ in range(nb_amis):
    nom, x_texte, y_texte = input().split()
    amis[nom] = Point(float(x_texte), float(y_texte))

nb_lieux = int(input())
lieux = [input() for _ in range(nb_lieux)]

def distance_totale():
    if nb_lieux == 0:
        return 0.0
    point_1 = amis[lieux[0]]
    distance_trajet = 0.0
    for lieu in lieux[1:]:
        point_2 = amis[lieu]
        distance_trajet += point_1.distance(point_2)
        point_1 = point_2
    return distance_trajet

print(round(distance_totale(), 2))
```