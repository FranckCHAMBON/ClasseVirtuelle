# Soirée orageuse

## Sujet

 Votre programme devra lire un décimal, le temps (en secondes) entre le moment où vous voyez l'éclair et le moment où vous entendez le tonnerre. Il devra calculer et afficher la distance entre vous et l'orage, arrondi au kilomètre près.

On supposera que la lumière se déplace instantanément. La vitesse du son dépend de paramètres comme l'altitude, la température... mais on supposera qu'en cette soirée elle vaut 340,29 mètres / seconde.

### Exemple

entrée :

    3.0

sortie :

    1

### Solution officielle

```python
from math import *

vitesseSon = 340.29
tempsParcours = float(input())
distanceKilometres = round((tempsParcours * vitesseSon) / 1000)
print(distanceKilometres)
```

### Solution alternative

```python
CONST_vitesse_son = 340.29 # en m/s
temps_parcours = float(input()) # en s
distance_m = CONST_vitesse_son * temps_parcours # en m
distance_arrondie_km = round(distance_m / 1000) # en km
print(distance_arrondie_km)
```

Il est inutile d'importer le module `math` pour disposer de la fonction `round`.

