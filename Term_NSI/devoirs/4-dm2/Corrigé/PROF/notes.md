# Corrigé du professeur



## Épreuve régionale


### 42

@import "./E1.py"

#### Commentaires

Ici une fonction est bienvenue, par principe.
En revanche, le *doctest* est inutile.



### Escalier

@import "./E2.py"

#### Commentaires
Ici, exceptionnellement on intègre l'affichage dans la fonction. Cela rend le *doctest* plus simple.
Un saut de ligne en trop au début peut rendre le *doctest* faux.
Utiliser la multiplication de chaînes comme `x * "X"` est un peu de la triche ; ici on attendait une double boucle. De manière générale, pour un problème simple, on demande de n'utiliser que des outils basiques.



### Grand écart

@import "./E3.py"

#### Commentaires

On essaie de bien respecter le PEP-8 ; sauf les accents pour coder en français.
> Quand on code en milieu professionnel, c'est très souvent en anglais, et sans accents.



### Initiales

@import "./E4.py"

#### Commentaires

On évite d'utiliser `split` qui serait tricher.
* On place la première lettre, puis
* pour chaque nouvelle lettre, si avant c'est une espace, et pas elle,
* alors c'est une initiale que l'on ajoute au sigle en version majuscule.



### Mot le plus long

@import "./E5.py"

#### Commentaires

Encore une fois, on évite d'utiliser `split` qui serait tricher.
* On met à jour `longueur` à zéro à chaque fois qu'un caractère est une espace.
* Mais avant cela, on met à jour le record du mot le plus long.
* **Attention**, pour prendre en compte aussi le dernier mot, il faut, soit ajouter une espace en fin de phrase, soit faire un test plus élaboré.

> Variante fonctionnelle (et en trichant avec `split`) ; 1 ligne.

```python
def longueur_plus_long_mot(n: int, chaîne: str) -> int:
    return max(map(len, chaîne.split()))
```


### Nombres impairs

@import "./E6.py"

#### Commentaires

Version fonctionnelle ; 1 ligne.
```python
def nombres_impairs(n: int, m: int) -> list:
    return list(range(n - (n&1) + 1, m + 1, 2))
```

Variante de l'affichage, avec *unpack* ; **hors programme**.
```python
print(*impairs)
```


### Table de multiplication

@import "./E7.py"

#### Commentaires

Ici, on réalise l'affichage dans la fonction.
* Cela rend le *doctest* plus simple à écrire.
* D'autre part, le résultat n'est pas utile, à part pour l'afficher ; on ne va pas en faire un post traitement, comme on pourrait le faire avec des nombres impairs que l'on peut utiliser autrement que pour les afficher.
* Bref, ici on peut afficher dans la fonction !



### Puissance 4

@import "./E8.py"

#### Commentaires
Pour factoriser le code, on utilise une liste de 4 vecteurs.
* Depuis un point $(i, j)$ non vide,
* pour chaque direction,
* on teste si le quatrième serait encore dans la grille,
* puis on teste l'égalité des quatre places.


### Puzzle

@import "./E9.py"

#### Commentaires

Ici le *doctest* serait pénible.
Un test est proposé à copier/coller en console.

### Solitaire

@import "./E10.py"

#### Commentaires

Ici encore le *doctest* serait pénible.
Un test est proposé à copier/coller en console.


### Anagrammes

@import "./E11.py"

#### Commentaires

On compte ici les couple d'anagrammes de manières efficace.
On utilise une formule mathématique : le nombre de façons de choisir 2 objets parmi $q$ est $\dfrac{q(q-1)} 2$.


### Plages du Pacifique

@import "./E12.py"

#### Commentaires
On construit l'ensemble des cases de l'océan et des plages, étape par étape avec un parcours en largeur du graphe.
Pour cela, l'océan a une partie actuelle connue : `courant` qui se fait étudier au cours du tour de boucle ; et `suivant` qui constitue la partie découverte d'océan qui sera étudié au tour suivant.

Pour les plages, on exclut les cases en diagonales d'une case de l'océan, d'où le test `(di == 0) or (dj == 0)`.

**Exercice** : réécrire ce code avec un style POO.

### Plan de métro

@import "./E13.py"


#### Commentaires

Il suffit de construire le graphe, et d'en faire un parcours en largeur depuis `départ`.

**Exercice** : réécrire ce code avec un style POO.


## Qualification


## Cases inaccessibles
> Deux méthodes proposées.

> 1. Une avec parcours de graphe itératif.

@import "./Q1.py"

> 2. Une avec parcours de graphe récursif.

@import "./Q1+.py"



## Comparer des chaînes

@import "./Q2.py"

#### Commentaires

On n'utilise pas `<` sur la chaîne de caractères entières, ni `.sort()` qui revient à l'utiliser.
On s'autorise `<` sur un caractère, mais sinon, on l'obtient en comparant `ord(caractère)` à la place.


## Les trois nombres

@import "./Q3.py"

#### Commentaires

Si la somme de deux nombres est égale au troisième, alors (et c'est équivalent) la somme des trois est égale au double du troisième.



## Nombre de voyelles

@import "./Q4.py"

#### Commentaires

Une version fonctionnelle de `nb_voyelles` en une ligne !

```python
def nb_voyelles(longueur: int, chaîne: str) -> int:
    return sum(1 for c in chaîne if c in "aeiuoyAEIOUY")
```
