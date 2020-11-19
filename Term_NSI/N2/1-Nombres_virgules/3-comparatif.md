# Comparatif de prix

## Sujet

 Votre programme doit d'abord lire le nombre de légumes mis en vente. Ensuite, pour chacun, il doit lire 3 nombres décimaux : son poids, son âge (en nombre de jours depuis la cueillette), et son prix de vente. Votre programme doit ensuite afficher pour chaque légume son prix au kg (au fur et à mesure que les légumes sont présentés).

### Exemple

entrée :

    2
    7.0
    5.0
    14.0
    9.5
    2.3
    7.6

sortie :

    2.0
    0.8

## Solution officielle

```python
nombreLegumes = int(input())
for loop in range(nombreLegumes):
   poids = float(input())
   age = float(input())
   prix = float(input())
   print(prix / poids)
```

## Solution alternative

Avec des commentaires pour les unités, c'est une bonne idée.

```python
nb_légumes = int(input())
for _ in range(nb_légumes):
   poids = float(input()) # en kg
   age = float(input())   # en j ; inutile
   prix = float(input())  # en €
   prix_au_kilo = prix / poids # €/kg
   print(prix_au_kilo)
```

