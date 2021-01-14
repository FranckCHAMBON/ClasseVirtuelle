# Programmation Orientée Objet (POO) {ignore = true}

Auteur : Franck Chambon, Lycée Aubrac

## Sommaire {ignore = true}

[TOC]


## Introduction

Construisons par exemple une façon de travailler avec les fractions.

```python
# ancienne méthode pour travailler avec des fractions
frac1_numérateur = 5
frac1_dénominateur = 7
frac2_numérateur = 13
frac2_dénominateur = 8
```

Cette façon n'est pas pratique. La gestion des identifiants s'avère pénible dès que les objets sont complexes.
En particulier pour les fonctions et leur paramètres ; comparons :
* `frac3_numérateur, frac3_dénominateur = addition(frac1_numérateur, frac1_dénominateur, frac2_numérateur, frac2_dénominateur)`
* `frac3 = frac1.addition(frac2)`

La seconde est clairement plus lisible, il s'agit de POO.

## Définition de nouvelles classes d'objets

Le choix d'un nom de classe en Python est d'utiliser le *CamelCase*, la première lettre de chaque mot en majuscule, et pas de `_`.

### Première approche ; rudimentaire

Pour définir une classe `Fraction` :

```python
class Fraction:
    pass

f = Fraction()
f.numérateur = 5
f.dénominateur = 8

g = f
f.numérateur = 11
print(g.numérateur, "sur", g.dénominateur)
```

    11 sur 8

On constate que l'on peut travailler d'un coup avec tout l'objet. Ici, on n'a pas eu une copie indépendante, mais le **même objet** pointé par deux variables différentes.

> ⚠️ C'est mal de donner des attributs à un objet en dehors d'un constructeur. **Ne plus jamais refaire.**

### Deuxième approche ; attributs de classe

Les attributs ne sont définis que dans la classe : 

```python
class Fraction:
    numérateur = 5
    dénominateur = 8

f = Fraction()
h = Fraction()

g = f
f.numérateur = 11
print("Fraction g :", g.numérateur, "sur", g.dénominateur)
print("Fraction h :", h.numérateur, "sur", h.dénominateur)
```
    Fraction g : 11 sur 8
    Fraction h : 5 sur 8

> ⚠️ On aimerait un constructeur pour créer une fraction qui dépend de paramètres. D'autre part, c'est mal de lire ou modifier les attributs directement ; on préfère passer par des fonctions. C'est un aspect de la modularité. On utilisera donc des méthodes pour lire, et d'autres pour modifier.


### Troisième approche ; avec initialisation `__init__()`

```python
class Fraction:
    def __init__(self, a, b):
        self.__numérateur = a
        self.__dénominateur = b
    
    def donne_numérateur(self):
        return self.__numérateur

    def donne_dénominateur(self):
        return self.__dénominateur

    def modifie_numérateur(self, a):
        self.__numérateur = a

    def modifie_dénominateur(self, b):
        self.__dénominateur = b



f = Fraction(22, 5)
f.modifie_dénominateur(7)
print("Fraction f :", f.donne_numérateur(), "sur", f.donne_dénominateur())
```

    Fraction f : 22 sur 7


* Les attributs qui doivent être indiqués **privés** commencent par `__` (double *underscore*). Ce **n**'est **pas** qu'une indication en Python, et ils ne peuvent plus être lus ni modifiés à l'extérieur de la définition de la classe. Dans d'autres langages de programmation, la gestion public/privé est encore plus stricte.

* Les méthodes liées au fonctionnement interne sont encadrées de `__` ; ici `__init__()` est la méthode à redéfinir pour initialiser un objet après son constructeur. **On ne peut pas changer de nom !** Il existe automatiquement le constructeur `__new__` mais en pratique, on réécrit uniquement `__init__`.

* `self` indique l'objet même instancié par la classe. Lui-même (*self*). **On ne peut pas changer de nom !**

> ⚠️ On aimerait une méthode plus simple pour afficher le résultat. On va créer une méthode qui sera appelée par `print` ; une fonction de conversion vers le type `str` ; c'est la méthode `__str__()`. **On ne peut pas changer de nom !**
> On ajoute aussi une méthode `__repr__()` qui a pour rôle de fournir un affichage bien plus succinct, moins joli, mais pour le débogage. Elle est appelée par la fonction `repr`. C'est la méthode qui est utilisée en console lorsqu'on entre un objet.

```python
>>> a = 2.0 # un objet quelconque créé
>>> print(a) # str sera appelé
2.0
>>> a # repr sera appelé
2.0
```

Souvent `repr` et `str` sont identiques, mais ce n'est pas obligatoire. `repr` sera plus à destination d'un développeur et `str` pour l'utilisateur.

On ajoute dans la classe, juste après le `__init__()`

```python
    # suite de Fraction
    def __str__(self):
        return f"Fraction : {f.donne_numérateur()} sur {f.donne_dénominateur()}"

    def __repr__(self):
        return f"({f.donne_numérateur()}/{f.donne_dénominateur()})"
```

Et on teste
```python
>>> f = Fraction(22, 5)
>>> f.modifie_dénominateur(7)
>>> print(f)
Fraction : 22 sur 7
>>> f
(22/7)
```

C'est bien plus pratique à utiliser !

> ⚠️ Le code n'est pas encore satisfaisant, il manque toutes les *docstring*.

## Encapsulation

L'encapsulation est un des trois principes fondamentaux de la POO (avec l'héritage et le polymorphisme).
* On réunit avec une certaine unité les données et les méthodes ; avec toujours des fonctions.
* On *masque* à l'utilisateur externe les données ; il y accède uniquement via des méthodes qui contrôlent les données comme prévu en interne.
* Cela permet de pouvoir réécrire entièrement le moteur interne, de manière transparente pour l'utilisateur final, qui ne sait pas comment sont stockées les données *in fine*.

Il y a donc des méthodes particulières : 
* **accesseur** (*getter*) ; renvoie un attribut
* **mutateur** (*setter*) ; modifie un attribut

> On trouve de **nombreuses** méthodes qui commencent par `get_` ou par `set_`, comme :

```python
class Personne:
    """Classe représentant une personne"""

    def __init__(self, nom: str, prénom: str, âge: int):
        self.__nom = nom
        self.__prénom = prénom
        self.__âge = âge

    def get_name(self) -> str:
        return self.__nom

    def set_name(self, nom: str):
        self.__nom = nom
```

## Méthodes publiques

Ajoutons une méthode pour multiplier deux fractions.

```python
    # suite de Fraction
    def multiplie_par(self, fraction):
        self.__numérateur *= fraction.donne_numérateur()
        self.__dénominateur *= fraction.donne_dénominateur()


>>> f = Fraction(2, 3)
>>> g = Fraction(5, 7)
>>> f.multiplie_par(g)
>>> f
(10/21)
```

⚠️ On remarquera, que pour `self`, on peut travailler avec ses attributs privés, mais pour `fraction`, nous avons utilisé les méthodes définies avant.

## Exercices

On reprend le code précédent complet : 

```python
class Fraction:
    def __init__(self, a, b):
        self.__numérateur = a
        self.__dénominateur = b

    def __str__(self):
        return f"Fraction : {f.donne_numérateur()} sur {f.donne_dénominateur()}"

    def __repr__(self):
        return f"({f.donne_numérateur()}/{f.donne_dénominateur()})"

    def donne_numérateur(self):
        return self.__numérateur

    def donne_dénominateur(self):
        return self.__dénominateur

    def modifie_numérateur(self, a):
        self.__numérateur = a

    def modifie_dénominateur(self, b):
        self.__dénominateur = b
    
    def multiplie_par(self, fraction):
        self.__numérateur *= fraction.donne_numérateur()
        self.__dénominateur *= fraction.donne_dénominateur()


>>> f = Fraction(2, 3)
>>> g = Fraction(5, 7)
>>> f.multiplie_par(g)
>>> f
(10/21)
```

1. Ajouter les *docstring*
2. Ajouter une méthode `simplifier()`
3. Ajouter une méthode `ajouter(fraction)`

Pour la suite, on peut regarder : 
* ce [cours](1-POO.pdf) avec des notions hors programme, pour aller plus loin.
* ce [cours](https://nbviewer.jupyter.org/url/www.maths-info-lycee.fr/notebooks/tnsi_01_poo.ipynb) illustré ; attention le PEP-8 n'est pas respectée, et il y a quelques erreurs glissées dans les images.
* ce [cours](http://www.maths-info-lycee.fr/poo.html), avec de bons exercices.
