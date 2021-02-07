# Types avancés : listes dynamiques, ensembles, dictionnaires

## Les listes dynamiques

On a déjà évoqué que la structure de données élémentaire, dans presque tous les langages de programmation, utilisée pour stocker en ligne des éléments de même nature est le **tableau**.

Un tableau : 
* a une taille fixe définie à la création,
* a ses éléments de même nature, modifiables.

Le type `list` de Python permet de travailler de cette manière, mais offre en plus les possibilités : 
* de faire varier la taille de la liste, en n'importe quel endroit,
* d'avoir des éléments de nature différente, mais nous ne le **recommandons pas**.

Les méthodes dynamiques utilisent la notation de la programmation orientée objet, avec un `.` qui indique à gauche le parent et à droite la filiation.

### Ajout d'élément à une liste

À **une liste**, on peut **ajouter** un **élément**.

```python
>>> une_liste = [2, 3, 5, 7]
>>> une_liste.append(11)
>>> une_liste
[2, 3, 5, 7, 11]
```

`.append()` sert à ajouter à la liste citée juste avant le `.` qui indique la filiation.

Avant la programmation orientée objet, on utilisait une écriture du genre `ajoute(élément, ma_liste)` ou alors `ajoute(ma_liste, élément)` ; aucune des deux n'est satisfaisante, et les choses se compliquent lorsqu'on travaille avec des méthodes plus complexes encore...

#### Exemple d'utilisation

Voici un programme qui : 
1. Crée une liste vide `mes_carrés`,
2. lit un entier `nb_lignes`,
3. lit `nb_lignes` lignes contenant un entier `nombre`,
4. pour chaque `nombre` lu, ajoute son carré à la liste uniquement s'il est pair.

```python
nb_lignes = int(input())
mes_carrés = list() # variante de ma_liste = [] pour une liste vide
for _ in range(nb_lignes):
    nombre = int(input())
    carré = nombre * nombre
    if carré % 2 == 0:
        mes_carrés.append(carré)
```

On rappelle qu'on préfère les listes en compréhension avec le code suivant : 

```python
nb_lignes = int(input())
ma_liste_lue = [int(input()) for _ in range(nb_lignes)]
mes_carrés = [nombre * nombre for nombre in ma_liste_lue if nombre * nombre % 2 == 0]
```

Cependant, on constate qu'avec les listes en compréhension, on fait deux fois le calcul `nombre * nombre` pour chaque cas validé ; cela pourrait être gênant et lent, d'autre part le code n'est pas factorisé...

> La méthode `.append()` est parfois très utile.

### Autres méthodes d'une liste

* `ma_liste.sort()` trie **en place** la liste `ma_liste`
* `ma_liste.reverse()` renverse en place `ma_liste`
* `ma_liste.index(élément)` renvoie l'indice de `élément` dans `ma_liste` ; s'il est absent, une erreur survient.
* `ma_liste.extend(autre_liste)` prolonge `ma_liste` avec `autre_liste`
* `ma_liste.remove(élément)` enlève `élément` (le premier trouvé) de `ma_liste`
* `ma_liste.insert(élément, indice)` ajoute `élément` à l'`indice` précisé
* `ma_liste.pop()` renvoie en supprimant le dernier élément de `ma_liste`

> Pour découvrir toutes les méthodes d'un `objet` python, on utilise `dir(objet)`, et ensuite pour avoir de l'aide sur une `méthode` on entre `help(objet.méthode)`

```python
>>> ma_liste = [2, 3, 5, 7]`
>>> dir(ma_liste)
['__add__', '__class__', '__contains__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', 
'__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', 
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', 
'__subclasshook__',
 'append', 'clear', 'copy', 'count', 'extend', 'index',
 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(ma_liste.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.
```

* On découvre qu'il y a de nombreuses méthodes **privées**, celles dont le nom est entouré de `__`.
* On découvre l'aide sur `.count()` : renvoie le nombre d'occurrences d'une valeur.

> *More about [Python list](https://www.programiz.com/python-programming/list)* ; en anglais

## Les ensembles

Un ensemble (*set* de type `set`) est un objet Python **muable** qui possède des éléments sans doublon, et sans ordre.
* On ne peut pas dire qui est l'élément d'indice `i` donné.
* Si on ajoute un élément déjà présent, il n'est pas ajouté une seconde fois.
* Les éléments d'un ensemble doivent être **immuables**, par exemple on peut avoir des nombres, ou des chaînes de caractères, ou bien des tuples, mais pas de listes ni d'ensembles.

L'utilisation des ensembles ressemble à celle des listes dynamiques, avec des méthodes de programmation orientée objet.

> Remarque (hors programme) : il est possible de créer un ensemble figé, donc immuable, avec `frozenset`. Ainsi les listes et les ensembles ont leur version immuable : tuple et frozenset.

> *More about [Python set](https://www.programiz.com/python-programming/set)* ; en anglais

### Construction

* `set()` pour un ensemble vide
* `set(i*i%10 for i in range(10))` définition en compréhension, ou bien `{i*i%10 for i in range(10)}`
* `set(ma_liste)` pour renvoyer une version sans doublon, ni ordre, d'une liste. La fonction `set()` essaie de transformer son argument en ensemble.

> ⚠️ l'ensemble vide se définit avec `set()`, mais s'affiche comme `{}`, or définir avec `{}` donne un dictionnaire vide ; **danger**, c'est différent.

#### Exemples

```python
>>> {n*n%10 for n in range(100)}
{0, 1, 4, 5, 6, 9}
>>> set("Bonjour")
{'r', 'j', 'B', 'u', 'o', 'n'}
```

* Les éléments ne sont pas, *a priori*, triés.
* Il n'y a pas de doublon.

### Les méthodes des ensembles

Donnons seulement les principales, pour les autres, voir `dir(set())`

On suppose que `truc` est un ensemble Python
* `truc.add(élément)` ajoute l'`élément` à truc, sans doublon, ni ordre.
* `truc.remove(élément)` enlève `élément` à `truc` ; provoque une erreur si absent.

### Les fonctions sur les ensembles

Comme pour les listes, on a les fonctions suivantes pour `truc` un ensemble (de type `set` donc) : 
* `len(truc)` renvoie le nombre d'éléments de `truc`
* `x in truc` renvoie un booléen, `True` si `x` est dans `truc`, sinon `False`
* `max(truc)` renvoie le maximum de `truc` s'il est non vide
* `min(truc)` renvoie le minimum de `truc` s'il est non vide
* `sum(truc)` renvoie la somme des éléments de `truc` ; erreur si `truc` contient des éléments non numériques.

## Les dictionnaires

Le principe d'un dictionnaire est de créer, comme pour un tableau, une association entre des **clés** et des **valeurs**.

* Dans un tableau `tab` de taille $n$, les clés sont les indices `i` de $0$ inclus à $n$ exclus. On note `tab[i]` la valeur associée à l'indice `i`.
* Dans un dictionnaire `dico`, les clés peuvent être tout objet `clé`, et la valeur associée est référencée avec `dico[clé]`, avec le même style que pour les tableaux, donc.

### Utilisations simples

* Pour créer un dictionnaire vide, on entre `mon_dico = dict()`
    * On pourrait aussi utiliser `mon_dico = {}`, mais cela peut donner une confusion avec l'ensemble vide...
* Pour ajouter, ou modifier une association clé-valeur, on entre `mon_dico[ma_clé] = ma_valeur`.
* Pour créer un dictionnaire non vide, on peut faire comme l'exemple ci-dessous.

```python
# codé en dur
longueur_mot = {'pour': 4, 'créer': 5, 'un': 2, 'dictionnaire': 12}

# avec une boucle
phrase = "pour créer un dictionnaire"
longueur_mot = dict()
for mot in phase.split():
    longueur_mot[mot] = len(mot)

# avec une compréhension
phrase = "pour créer un dictionnaire"
longueur_mot = {mot: len(mot) for mot in phrase.split()}
```

### Exemples de dictionnaires
#### Pour traduire des mots
```python
>>> traduction_fr_en = {'mot': 'word', 'virgule' : 'coma', 'phrase' : 'sentence', 'point': 'point'}
>>> traduction_fr_en['phrase']
'sentence'
>>> traduction_fr_en['lettre']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'lettre'
```

#### Pour stocker des numéros

Voici un script qui enregistre des numéros de cartes pour une classe.

```python
def inscrire_élèves(nb_élèves):
    num_carte = dict()
    for _ in range(nb_élèves):
        nom = input('Quel est votre nom ?')
        numéro = input('Quel est votre numéro de carte ?')
        num_carte[nom] = numéro
    return num_carte
```

#### Pour mémoriser des résultats

On suppose que l'on a une fonction `f` dont le calcul coûte cher pour certaines entrées que l'on appelle souvent.
* Si les entrées sont des petits entiers alors un tableau est idéal pour stocker les valeurs associées à l'entrée qui sera l'indice du tableau. On peut initialiser le tableau rempli de `None` pour désigner le fait que la fonction n'a pas encore été calculée.
* Sinon, on peut utiliser un dictionnaire.


> Version avec un tableau

```python
# on suppose f est une fonction à un paramètre entier x

# On va utiliser un tableau pour stocker certaines valeurs

tab_taille = 10000
f_tab = [None for _ in range(tab_taille)]

def f_mem(x):
    if 0 <= x < tab_taille:
        if f_tab[x] is None:
            f_tab[x] = f(x)
        return f_tab[x]
    else:
        return f(x)
```


> Version avec un dictionnaire

```python
# on suppose f est une fonction à un paramètre entier x

# On va utiliser un dictionnaire pour stocker certaines valeurs

f_dico = dict()

def f_mem(x):
    if not(x in f_dico):
        f_dico[x] = f(x)
    return f_dico[x]
```

> Le code est bien plus simple, inutile de faire des suppositions sur l'entrée. C'est une excellente pratique. On la trouve souvent avec la dénomination de **mémoïsation**.


### Itérer avec un dictionnaire
On fera comme s'il n'y avait pas d'ordre pour les clés, et que l'on peut itérer sur les différentes clés d'un dictionnaire avec le code :

```python
for une_clé in mon_dico:
    ma_fonction(mon_dico[une_clé])
```
