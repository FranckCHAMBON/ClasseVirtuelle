# Conversions de distances

## Sujet

 Écrivez un programme qui lit un nombre décimal (un nombre à virgule) représentant un nombre de lieues et affiche le nombre de kilomètres correspondant. Un kilomètre vaut exactement 0.707 lieues.

### Exemple

entrée :

    10.5

sortie :

    14.8514851485

## Solution officielle

```python
lieues = float(input())
kilometres = lieues / 0.707
print(kilometres)
```

## Solution alternative

Avec de meilleurs noms de variable, et une constante définie au début du programme.

```python
CONST_km_par_lieue = 0.707
distance_en_lieue = float(input())
distance_en_km = distance_en_lieue / CONST_km_par_lieue
print(distance_en_km)
```
