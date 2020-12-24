# Bonnes pratiques de codage

## Définitions
### PEP
PEP signifie _**P**ython **E**nhancement **P**roposal_, et il y en a plusieurs. Un PEP est un document qui décrit les nouvelles fonctionnalités proposées pour Python et documente les aspects de Python, comme la conception et le style, pour la communauté.

### Tiret bas
Connu en anglais comme *underscore*, on trouve ce caractère avec la touche du clavier <kbd>8_\\</kbd>

### *snake_case*
Le [*snake case*](https://fr.wikipedia.org/wiki/Snake_case) est une convention typographique en informatique consistant à écrire des ensembles de mots, généralement, en minuscules en les séparant par des tirets bas.

### *camel case*
Le *camel case* consiste à mettre en majuscule les premières lettres de chaque mot, sans séparer par un tiret bas.


## PEP 8
PEP 8, parfois orthographié PEP8 ou PEP-8, est un document qui fournit des directives et des meilleures pratiques sur la façon d’écrire du code Python. Il a été écrit en 2001 par Guido van Rossum, Barry Varsovie et Nick Coghlan. L’objectif principal de PEP 8 est d’améliorer la lisibilité et la cohérence du code Python.

### Les identifiants

1. On utilisera le *snake_case* pour toutes les variables, sauf :
    + pour les `class` que l'on nomme en *camel case*,
    + pour les constantes, en majuscule.

2. On donne des identifiants qui ont un sens.

```python
# mal
x = 'Jean Dupont'
y, z = x.split()
print(y, z, sep=', ')

# mieux
texte = 'Jean Dupont'
prénom, nom = texte.split()
print(prénom, nom, sep=', ')
```


### Aération du code

* L'indentation doit être de **4** espaces.
* Une ligne vide après une définition de fonction.
* Deux lignes vides après une définition de classe.
* Une ligne vide pour séparer deux étapes marquées d'un groupe d'instructions.
* Maximum 79 caractères de code par ligne.
    * Une ligne trop longue peut être coupée sans problème **à l'intérieur** de parenthèses, crochets ou accolades ; on parle de continuation implicite.
    * Sinon, on peut toujours couper une ligne avec `\`.
    * La continuation implicite est **à privilégier** dès que possible !

```python
def ma_fonction(argument_1,
                argument_2, argument_3, argument_4):
    pass

ma_fonction(22, 23, 24, 25) + \
    ma_fonction(34, 35, 36, 37)
```

### Aération des opérateurs

On met de l'espace autour des opérateurs binaires, sauf
+ pour les paramètres par défaut des fonctions,
+ pour les opérations prioritaires
+ pour `:` dans les définitions de tranches

```python
# Mal
x = a*b+c
if x > 5 and x % 2 == 0:
    print('x est plus grand que 5 et divisible par 2.')

# moyen
x = a * b + c
if x>5 and x%2==0:
        print('x est plus grand que 5 et divisible par 2.')

# bien
x = a*b + c
if (x > 5) and (x % 2 == 0):
        print('x est plus grand que 5 et divisible par 2.')
```

On met une espace : 
* juste après une virgule
```python
mon_tuple = (4, 11, 25)
```

On **ne met pas** d'espace
* juste après une parenthèse ouvrante (ou crochet, ou accolade)
* juste avant une parenthèse fermante (idem).

On ne place jamais d'espace en fin de ligne.

### Un peu plus encore
Inspiré de ce [document](https://www.codeflow.site/fr/article/python-pep8), vous retrouverez plus de détails. Une recommandation y est faite, elle fait débat. Les deux exemples suivant utilisent du transtypage implicite ; en NSI nous préférons ne pas en voir ! Nous montrons ensuite la bonne pratique.

```python
# Not recommended
my_list = []
if not len(my_list):
    print('my_list is empty!')
```

En Python, toute liste, chaîne ou tuple **vide** est transypée implicitement à `False`. Nous pouvons donc proposer une alternative plus simple à ce qui précède :

```python
# Recommended
my_list = []
if not my_list:
    print('my_list is empty!')
```

Alors que les deux exemples afficheront que la liste est vide (en anglais), la deuxième option est plus simple, donc PEP 8 l’encourage.

> ⚠️ Contrairement au PEP 8, en NSI nous préférons interdire le transtypage implicite, donc **une autre méthode est recommandée**. Les deux précédentes sont donc incorrectes pour nous.

```python
# La bonne méthode
if ma_liste == []:
    print("ma_liste est vide !")

# ou alors
if ma_liste != []:
    print("ma_liste n'est pas vide !")
```
