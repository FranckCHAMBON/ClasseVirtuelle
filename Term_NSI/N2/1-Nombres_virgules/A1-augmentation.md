# Augmentation de la population

## sujet

 Votre programme devra lire un entier, la population actuelle de la ville, puis un nombre décimal, la croissance prévue de la population, en pourcentage. Il devra alors afficher la nouvelle population de la ville sous la forme d'un nombre entier. On considérera, par convention, qu'une population de 31,4 habitants signifie qu'il y a 31 habitants, on ne compte donc que les habitants « entiers » !

### Exemples
#### Exemple 1

entrée :

    123
    7.0

sortie :

    131

#### Exemple 2

entrée :

    456
    -5.5

sortie :

    430

## Solution officielle

```python
from math import *
populationActuelle = int(input())
croissancePourcent = float(input())
populationFuture = floor( populationActuelle * (1 + croissancePourcent / 100) )
print(populationFuture)
```

Remarque
: On déconseille l'utilisation de `from math import *`, cela redéfinit la fonction `pow` en moins bien, il n'y a plus le troisième argument optionnel pour l'arithmétique modulaire.


Rappel
: Augmenter une quantité $Q$ de $t\%$, revient à multiplier $Q$ par $\left(1 + \dfrac t {100}\right)$

## Solution alternative

:warning: Pour les nombres positifs `int` et `floor` se comportent de la même manière. En revanche, pour les négatifs le résultat peut être différent.
* `int(+3.7) == +3`
* `floor(+3.7) == +3`
* `int(-3.7) == -3`
* `floor(-3.7) == -4` ; en effet $-4$ est l'entier inférieur ou égal à $-3.7$ le plus proche.

Ici, nous pouvons utiliser `int`.

```python
population_actuelle = float(input())
taux_croissance = float(input())
population_prévue = int(population * (1 + taux_croissance / 100))
print(population_prévue)
```



