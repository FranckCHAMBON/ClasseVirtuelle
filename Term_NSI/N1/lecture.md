# [Lecture de l'entrée](http://www.france-ioi.org/algo/chapter.php?idChapter=843)

> Correction alternative de certains problèmes

## Récoltes

### Sujet

Votre programme doit lire un entier, qui représente la longueur du côté d'un champ carré en mètres. Il doit ensuite afficher la masse que l'on pourra récolter de ce champ si l'on suppose que la production sera de 23 kg par mètre carré.

### Exemple

entrée :

    10

sortie :

    2300

### Solution officielle

```python
longueur = int(input())
print(longueur * longueur * 23)
```

### Solution alternative

Ici, on propose une solution plus longue, avec des variables explicites, et des commentaires pour les unités.

```python
côté = int(input()) # m
aire_du_carré = côté * côté # m²
rendement = 23 # kg / m²
production = rendement * aire_du_carré # kg
print(production)
```

## Graduation de thermomètres

### Sujet

Étant données deux températures entières `tempMin` et `tempMax`, votre programme doit afficher toutes les températures comprises entre les deux, bornes incluses.

### Exemple

entrée :

    9
    14

sortie :

    9
    10
    11
    12
    13
    14

### Solution officielle

```python
tempMin = int(input())
tempMax = int(input())
temperature = tempMin
for loop in range(tempMax - tempMin + 1):
   print(temperature)
   temperature = temperature + 1
```

### Solutions alternatives

Au lieu de calculer le nombre de tours de boucle, on peut utiliser une boucle `while`.

```python
temp_min = int(input())
temp_max = int(input())
température = temp_min
while température <= temp_max:
   print(température)
   température += 1
```

On peut aussi utiliser un `range` à deux paramètres.

```python
temp_min = int(input())
temp_max = int(input())
for température in range(temp_min, temp_max+1):
   print(température)
```

On peut aussi écrire une version récursive.

```python
def affiche(début: int, fin: int):
    """Affiche les nombres de `début` à `fin` inclus.

    >>> affiche(3, 5)
    3
    4
    5

    """
    assert début <= fin
    print(début)
    if début != fin:
        affiche(début+1, fin)


temp_min = int(input())
temp_max = int(input())
affiche(temp_min, temp_max)
```

## Socles pour statues

### Sujet

 Un socle est ainsi constitué d'étages, chaque étage ayant une hauteur égale à une unité et une base carrée. Le côté des carrés diminue de une unité à chaque étage.

Votre programme doit lire deux entiers, représentant respectivement la largeur du socle au niveau du sol et la largeur du socle au niveau de la face supérieure du socle. Il doit ensuite calculer et afficher le volume du socle.

### Exemple

entrée :

    7
    3

sortie :

    135

### Solution officielle

```python
largeurBas = int(input())
largeurHaut = int(input())
 
volume = 0
largeur = largeurHaut
for loop in range(largeurBas - largeurHaut + 1):
   volume = volume + largeur * largeur
   largeur = largeur + 1
 
print(volume)
```

### solutions alternatives

1. Avec une boucle `while`

```python
largeur_bas = int(input())
largeur_haut = int(input())

volume = 0
largeur = largeur_bas
while largeur <= largeur_haut:
    volume_étage = largeur * largeur * 1
    volume += volume_étage
    largeur -= 1

print(volume)
```

2. Avec une fonction récursive

```python
def volume_socle(largeur_bas: int, largeur_haut: int) -> int:
    """Renvoie le volume d'un socle avec des étages carrés.

    >>> volume_socle(7, 3)
    135

    """
    if largeur_bas < largeur_haut:
        return 0
    else:
        volume_base = largeur_bas * largeur_bas * 1
        return  volume_base + volume_socle(largeur_bas - 1, largeur_haut)


import doctest
doctest.testmod()

largeur_bas = int(input())
largeur_haut = int(input())
print(volume_socle(largeur_bas, largeur_haut))
```

