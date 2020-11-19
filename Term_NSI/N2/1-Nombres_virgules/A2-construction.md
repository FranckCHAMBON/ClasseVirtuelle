# Construction de maisons

## sujet

 Votre programme devra lire un nombre décimal, la quantité de ciment nécessaire pour les fondations de votre nouvelle maison, en kilos. Sachant que le ciment n'est vendu qu'en sacs de 60 kilos et que un sac coûte 45 euros, votre programme devra afficher le coût total du ciment.

### Exemple

entrée :

    145.8

sortie :

    135

## Solution officielle

```python
from math import *
 
quantiteCiment = float(input())
nbSacs = ceil(quantiteCiment / 60)
prix = nbSacs * 45
print(prix)
```

`from math import *` ; c'est mal, on n'importe que ce dont on a besoin !

## Solution alternative

```python
from math import ceil

CONST_masse_sac = 60 # en kg
CONST_prix_sac = 45 # en €
masse_ciment = float(input()) # en kg
nb_sacs = ceil(masse_ciment / CONST_masse_sac)
prix_ciment = nb_sacs * CONST_prix_sac # en €
print(prix_ciment)
```

* On définit les constantes utiles en début de programme.
* On utilise les commentaires pour indiquer les unités.
