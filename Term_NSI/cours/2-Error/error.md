# Gestion des erreurs {ignore}

Python propose plusieurs mécanismes pour écrire un code sûr.
* La vérification de condition avec `assert`.
* Les informations données suite à une erreur.
* La création de jeux de tests des fonctions avec `doctest`

## Sommaire {ignore}

[TOC]

## Python et le typage dynamique

Python est un langage à typage dynamique, cela signifie qu'une variable peut légalement changer de type au cours d'un programme, cela simplifie souvent le code **mais** peut engendrer des erreurs sournoises difficiles à détecter.

> En NSI, on s'interdira de changer le type d'une variable, à deux exceptions :
* Pour la valeur `None` que l'on qualifiera de tout type, même si pour Python elle du type `NoneType`. `None` signifie l'absence de valeur. Nous nous en servirons souvent.
* Pour un autre type numérique, mais dans ce cas, on préfèrera une conversion explicite, plutôt qu'implicite.

```python
def mon_minimum(ma_liste):
    longueur = len(ma_liste)
    if longueur == 0:
        return None
        # une liste vide ne possède pas de minimum
    else:
        mini = ma_liste[0]
        for i in range(1, longueur):
            if mini < ma_liste[i]:
                mini = ma_liste[i]
        return mini
```

```python
>>> x = mon_minimum([])
>>> type(x)
<class 'NoneType'>
>>> x = mon_minimum([1337, 42, 200])
>>> type(x)
<class 'int'>
>>> x += 0.0     # bof,   conversion implicite
>>> x = float(x) # mieux, conversion explicite
>>> type(x)
<class 'float'>
```

De nombreux langages interdisent ces pratiques, et vérifient mieux le code ; Python est permissif. Cependant, il existe des outils externes qui peuvent vérifier le code comme si le typage était statique. 
> Après la première phase d'apprentissage, **une bonne pratique est de faire comme si le typage était statique**. (Sauf les deux exceptions mentionnées plus haut.)


## Annotation de type des fonctions

> En NSI, on indiquera les types des paramètres lorsqu'ils sont élémentaires : `int, float, bool, str, list`. On ne le fera pas dans les cas complexes.

On suivra le modèle :

```python
def ont_même_parité(n: int, m: int) -> bool:
    return n % 2 == m % 2
```

Utilisation :
```python
>>> ont_même_parité(42, 1337)
False
>>> ont_même_parité(2021, 1337)
True
>>> ont_même_parité(202, 42)
True
```

* Chaque paramètre est suivi d'un `:` collé à gauche, puis, après une espace, son type.
* Les paramètres sont séparés par une virgule suivie d'une espace.
* Le type de retour est indiqué collé avant le `:` final, et précédé de `->` avec des espaces de chaque côté.

## `assert` pour vérifier une condition

* Les assertions permettent de vérifier une condition en cours d'exécution.
    * Si elle est vérifiée, le programme continue normalement.
    * Sinon, une exception est levée.
        * Si cette exception n'est pas attrapée, alors le programme est arrêté et une trace des derniers appels est donnée.

* On peut aussi vérifier des pré-conditions à l'entrée d'une fonction.

### Exemple simple

```python
def est_voyelle(lettre: str) -> bool:
    assert len(lettre) == 1, "La chaîne `lettre` ne devrait contenir qu'un seul caractère"
    return lettre in "AEIOUYaeiouy"
```

```python
>>> est_voyelle("z")
False
>>> est_voyelle("A")
True
>>> est_voyelle("Azerty")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in est_voyelle
AssertionError: La chaîne `lettre` ne devrait contenir qu'un seul caractère
```

### Utilisation utile

Le modèle à utiliser est :
`assert <condition_à_vérifier>, <message à transmettre en cas d'erreur>`

* Le message à transmettre est facultatif, cependant, il est utile de le rendre le plus complet et dense possible. Dans l'exemple précédent, on aurait pu écrire plutôt :

```python
assert len(lettre) == 1, ("Mauvaise longueur de la chaîne `lettre`", len(lettre), lettre)
```

Cela permet à l'utilisateur de disposer d'éléments pour apprécier l'erreur de manière plus précise. **C'est au développeur de choisir les informations à transmettre, en fonction de la situation.**

## Générer de meilleurs messages d'erreurs

Nous allons apprendre, avec la POO, à créer nos propres objets, qui ont leurs propres méthodes. Par exemple la méthode `min` qui renvoie le minimum d'une liste, d'un ensemble... Et bientôt de notre objet... Mais s'il est non vide !

```python
>>> ensemble_vide = set()
>>> min(ensemble_vide)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: min() arg is an empty sequence
```

Une erreur de type `ValueError` est levée, nous pouvons le faire aussi dans notre propre fonction :

```python
raise ValueError("Notre objet est vide")
```

Il peut être utile de comprendre, ou de lever l'[une de ces exceptions](https://docs.python.org/fr/3/library/exceptions.html#bltin-exceptions) suivant la situation :
* `AssertionError`, levée par `assert` comme l'a déjà vu.
* `EOFError`, levée quand on essaie de lire alors qu'on est arrivé au bout du fichier (_**E**nd **O**f **F**ile_, fin du fichier).
* `IndexError`, pour un mauvais indice.
* `KeyError`, pour une clé (de dictionnaire) non trouvée.
* `RuntimeError`, pour une erreur autre que celles détaillées.
* `SyntaxError`, levée par l'interpréteur, le code possède une erreur de syntaxe, souvent une parenthèse manquante... Penser à vérifier la ligne précédente que celle indiquée !
* `IndentationError`, problème d'indentation.
* `TypeError`, mauvais type utilisé pour une opération ou une fonction.
* `ValueError`, le type est bon, mais valeur inappropriée. Comme objet vide pour extraire un élément...


Pour en savoir plus : [la documentation](https://docs.python.org/fr/3/tutorial/errors.html)

## `doctest` pour chaque fonction

En terminale NSI, on documentera chaque fonction avec une `docstring`, que l'on complètera le plus souvent possible en `doctest`.