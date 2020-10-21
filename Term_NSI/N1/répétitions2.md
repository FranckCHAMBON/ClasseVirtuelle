# [Répétitions conditionnées](http://www.france-ioi.org/algo/chapter.php?idChapter=649)

> Correction alternative de certains problèmes

## Département de chimie : mélange explosif

### Sujet

Votre programme devra lire trois entiers : le nombre total de mesures envisagées ainsi que la température minimum et maximum autorisées. Les entiers suivants seront les différentes températures relevées au cours du temps.

Tant que les températures relevées restent dans le bon intervalle, votre programme devra écrire le texte « Rien à signaler », mais dès que la température n'est pas bonne il doit écrire le texte « Alerte !! » et s'arrêter.

### Exemples

#### Exemple 1

entrée :

    5
    10
    20
    15
    10
    20
    0
    15

sortie :

    Rien à signaler
    Rien à signaler
    Rien à signaler
    Alerte !!

#### Exemple 2

entrée :

    3
    0
    100
    15
    50
    75

sortie :

    Rien à signaler
    Rien à signaler
    Rien à signaler

### Solution officielle

```python
nbMesures = int(input())
tempMin = int(input())
tempMax = int(input())
numMesure = 0
tempValide = True
while numMesure < nbMesures and tempValide:
   température = int(input())
   tempValide = (tempMin <= température and température <= tempMax)
   if tempValide:
      print("Rien à signaler")
   else:
      print("Alerte !!")
   numMesure = numMesure + 1
```

### Solution alternative

On peut aussi utiliser un `break` pour sortir prématurément d'une boucle `for`.

```python
nb_mesures = int(input())
temp_min = int(input())
temp_max = int(input())
for _ in range(nb_mesures):
    temp = int(input())
    if temp_min <= temp <= temp_max:
        print("Rien à signaler")
    else:
        print("Alerte !!")
        break
```

 :warning: Attention, ce style n'est pas toujours apprécié, parfois oui.

 