# Convertisseur d'unités

## Sujet

 Écrivez un programme qui convertit des valeurs du système métrique en valeurs du système de mesure américain. On fournit des mesures à votre programme, en mètres, grammes ou degrés Celsius et vous devez les convertir respectivement en pieds, livres et degrés Fahrenheit.

Voici les règles de conversion à utiliser :

* 1 pied = 0,3048 mètres ;
* 1 gramme = 0,002205 livres ;
* température en degrés Fahrenheit = 32 + 1,8 × température en degrés Celsius.

On vous donne sur la première ligne le nombre de conversions à effectuer, puis sur les lignes suivantes la valeur à convertir, et son unité : `m`, `g` ou `c` (avec une espace entre les deux).

Affichez en sortie les valeurs converties, suivies d'une espace et de leur unité : `p`, `l` ou `f`.

Il n'est en fait pas judicieux d'écrire des fonctions pour résoudre cet exercice : le mieux est de définir des constantes. Vous pouvez aussi profiter de cet exercice pour expérimenter l'instruction « selon », switch dans certains langages.

## Exemple

entrée :

    4
    12.3 m
    1245.243 g
    37.2 c
    23 g

sortie :

    40.354331 p
    2.745761 l
    98.960000 f
    0.050715 l

## Solution

On va définir trois fonctions de conversions, et utiliser un dictionnaire pour appeler la bonne fonction.

```python
def mètres_vers_pieds(x):
    return (x/0.3048, "p")

def grammes_vers_livres(x):
    return (x*0.002205, "l")

def celsius_vers_fahrenheit(x):
    return (32 + 1.8*x, "f")

conversions = {'m':mètres_vers_pieds, 'g':grammes_vers_livres, 'c':celsius_vers_fahrenheit}

nb_conversions = int(input())
for _ in range(nb_conversions):
    nombre_en_chaîne, unité_origine = input().split()
    x = float(nombre_en_chaîne)
    y, unité_arrivée = conversions[unité_origine](x)
    print(y, unité_arrivée)
```