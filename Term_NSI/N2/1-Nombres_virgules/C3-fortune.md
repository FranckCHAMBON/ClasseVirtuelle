# La roue de la fortune

## Sujet

 Votre programme doit commencer par lire un entier nbZones. Sachant que la roue va tourner de nbZones zones, vous devez calculer (puis afficher) sur quelle zone le curseur va arriver.

Ainsi, si la route tourne de +2 zones alors le curseur arrive sur la zone 2, et si la roue tourne de -2 zones, alors le curseur arrive sur la zone 22.

> Il y a 24 zones différentes.

### Exemples

#### Exemple 1

entrée :

    25

sortie :

    1

#### Exemple 2

entrée :

    -50

sortie :

    22

### Solution officielle

```python
nbZones = int(input())
print(nbZones % 24)
```

### Solution alternative

```python
CONST_total_zones = 24
nb_zones = int(input())
zone = nb_zones % CONST_total_zones
# résultat modulo 24, entre 0 inclus et 24 exclu.
print(zone)
```
