# [Structures avancées](http://www.france-ioi.org/algo/chapter.php?idChapter=647)

> Correction alternative de certains problèmes

## Planning de la journée

### Sujet

 Votre programme doit d'abord lire un entier décrivant votre position actuelle sur la route, sous la forme d'un nombre de kilomètres par rapport au début de la route. Ensuite, il doit lire un entier donnant le nombre de villages. Pour chaque village, il doit lire un entier décrivant la position de ce village le long de cette même route. Votre programme doit alors afficher le nombre de villages qui se trouvent à une distance inférieure ou égale à 50 km de votre position actuelle.

### Exemple

entrée :

    120
    5
    30
    113
    187
    145
    129

sortie :

    3

### Solution officielle

```python
posActuelle = int(input())
nbVillages = int(input())
nbAccessibles = 0
for loop in range(nbVillages):
   posVillage = int(input())
   ecart = posActuelle - posVillage
   if ecart < 0:
      ecart = -ecart
   if ecart <= 50:
      nbAccessibles = nbAccessibles + 1
print(nbAccessibles)
```

Remarque
: Un écart devrait toujours être positif. Ici, un meilleur nom de variable aurait été `différence`, puis ensuite
```python
if différence > 0:
    écart = différence
else:
    écart = - différence

```

### Solution alternative

```python
position_actuelle = int(input())
nb_villages = int(input())

nb_villages_proches = 0
for _ in range(nb_villages):
    position_village = int(input())
    if abs(position_actuelle - position_village) <= 50:
        nb_villages_proches += 1
print(nb_villages_proches)
```

Variante fonctionnelle

```python
position_actuelle = int(input())
nb_villages = int(input())
positions_villages = [int(input()) for _ in range(nb_villages)]

print(sum(1 for x in positions_villages if abs(position_actuelle - x) <= 50))
```

Remarque
: On fait la somme de $1$ pour les éléments d'une liste qui satisfont un critère ; c'est une bonne méthode pour les compter !

## Étape la plus longue

### Sujet

Votre programme doit d'abord lire un entier strictement positif, le nombre de jours de marche effectués jusqu'à présent. Il doit ensuite lire, pour chaque jour, la distance parcourue ce jour-là. Il doit alors afficher la distance maximale parcourue en une journée.

### Solution officielle

```python
nbJours = int(input())
distanceMax = 0
for loop in range(nbJours):
   distance = int(input())
   if distance > distanceMax:
      distanceMax = distance
print(distanceMax)
```

### Solution alternative

Une solution dans un style fonctionnel

```python
nb_jours = int(input())
distances = [int(input()) for _ in range(nb_jours)]

print(max(distances))
```

