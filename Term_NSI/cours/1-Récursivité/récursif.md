# Récursivité {ignore=true}

## Sommaire {ignore=true}

[TOC]

> « Nous les hackers nous [...] avions aussi une tradition d'acronymes récursifs qui consiste à dire que le programme qu'on crée est similaire à un programme existant. »
> *Richard Stallman*

## Exemples
### Sigles récursifs
* **GNU** : *GNU's Not UNIX* (GNU n'est pas UNIX)
* **LAME** : *Lame Ain't an MP3 Encoder* (Lame n'est pas un encodeur mp3.)
* **PHP** : *PHP: Hypertext Preprocessor*. (Historiquement, ce sigle récursif était l'abréviation de Personal Home Page ; en 2008, le sigle récursif est le sens officiel de PHP)
* **HURD** : *Hird of Unix-Replacing Daemons* et **HIRD** : *Hurd of Interfaces Representing Depth2* ; exemple de paire de sigles mutuellement récursifs.

![](assets/MagrittePipe.jpg)
> *La Trahison des images*, René Magritte

### Images

Dans la nature, on trouve différents objets qui font preuve d'auto-similarité. On peut aussi les construire artificiellement.

![](assets/Fractal_Broccoli.jpg)

![](assets/Bransleys_fern.png)


## Définitions
(D'après [Wikipédia](https://fr.wikipedia.org/wiki/R%C3%A9cursivit%C3%A9))
La récursivité est une démarche qui fait référence à l'objet même de la démarche à un moment du processus. En d'autres termes, c'est une démarche dont la description mène à la répétition d'une même règle. Ainsi, les cas suivants constituent des cas concrets de récursivité :

1. Décrire un processus dépendant de données en faisant appel à ce même processus sur d'autres données plus « simples » ;
2. Montrer une image contenant des images similaires ;
3. Écrire un algorithme qui s'invoque lui-même ;
4. Définir une structure à partir de l'une au moins de ses sous-structures.

En NSI, nous abordons ces différents aspects.
1. Le concept «Diviser pour mieux régner » donne par exemple le principe de recherche par dichotomie dans un tableau trié.
2. Les [fractales](https://fr.wikipedia.org/wiki/Fractale), par exemple.
3. Nous allons voir de nombreux exemples de fonctions récursives !
4. Les structures arborescentes, arbres et graphes, par exemple.


## Fonctions récursives

Une **fonction récursive** est une fonction qui s'appelle elle-même. (Ou bien qui fait partie d'un ensemble de fonctions qui s'appellent mutuellement).

### Exemple, somme des premiers entiers

$$S_n = 1 + 2 + 3 + \cdots + (n-1) + n$$

On a :
* $S_0 = 0$, et
* $S_{n} = S_{n-1} + n$

#### Version itérative

```python
def somme_premiers_entiers(n):
    """Renvoie la somme 0 + 1 + ... + n

    >>> somme_premiers_entiers(5)
    15

    """
    somme = 0
    for i in range(1, n+1):
        somme += i
    return somme
```

#### Version récursive

```python
def somme_premiers_entiers(n):
    """Renvoie la somme 0 + 1 + ... + n

    >>> somme_premiers_entiers(5)
    15

    """
    if n == 0:
        return 0
    else:
        return somme_premiers_entiers(n-1) + n
```

Les appels récursifs sont stockés dans une pile d'appels.
> TODO : Faire un schéma d'appel.

⚠️ Attention, par défaut, Python limite à $1000$, la profondeur des appels récursifs. Cela peut se modifier.

### Différents types de fonctions récursives

#### Appels multiples

Voici, par exemple, une version naïve pour calculer un terme de la suite de Fibonacci.

> Rappel : $0, 1, 1, 2, 3, 5, 8, 13, 21, \cdots$ ; le terme suivant est la somme des deux précédents, on commence avec $0, 1$.

```python
def fibonacci(n):
    """Renvoie le terme d'indice n de la suite
    >>> fibonacci(6)
    8
    >>> fibonacci(0)
    0
    """
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

Cette version est naïve, en effet l'appel `fibonacci(5)` est effectué de nombreuses fois pour `fibonacci(8)` et le résultat n'est pas stocké, donc recalculé à chaque fois... On utilisera la **mémoïsation** pour améliorer cela.

```python
fib_dico = {0: 0, 1: 1} # valeurs initiales
def fibonacci(n):
    """Renvoie le terme d'indice n de la suite
    >>> fibonacci(6)
    8
    >>> fibonacci(0)
    0
    """
    if n in fib_dico:
        return fib_dico[n]
    else:
        fib_n = fibonacci(n-1) + fibonacci(n-2)
        fib_dico[n] = fib_n
        return fib_n
```

#### Appels croisés

```python
def fonction_A(x):
    ...
    ...
    ...fonction_B(...x...)
    ...
    return ...

def fonction_B(x):
    ...
    ...
    ...fonction_A(...x...)
    ...
    return ...
```

La `fonction_A` utilise la `fonction_B` qui utilise elle-même la `fonction_A`, *a priori* avec un paramètre qui dépend du paramètre donné en entrée...

⚠️ Faire des appels croisés est **légal**, cependant on veillera que cela fasse progresser le "calcul", donc sans rentrer dans une boucle infinie. On remarquera que ce principe est général, et que l'exemple simple suivant boucle à l'infini pour toute entrée `n` supérieure à `0`.

```python
def bizarre(n):
    if n == 0:
        return 9
    else:
        return bizarre(n + 1)
```


### Exercices concrets
#### Nombre de chiffres
Écrire une version récursive d'une fonction qui renvoie le nombre de chiffres d'un entier strictement positif.
> **Indice** : Quel est le nombre de chiffres de $n$, par rapport à celui de $n$ divisé par $10$ ?
#### Nombre de bits égaux à 1
Écrire une version récursive d'une fonction qui renvoie le nombre de bits égaux à $1$ d'un entier strictement positif.
> **Indice** : S'inspirer de l'exercice précédent.

#### Calcul de puissance
En partant du principe que :
* si $n$ est pair, alors $a^n = \left(a^{n/2}\right)^2$
* si $n$ est impair, alors $a^n = \left(a^{(n-1)/2}\right)^2×a$

1. Écrire une fonction récursive `puissance(a, n)` qui renvoie $a^n$.
> **Indice** : Penser au cas de base !
2. Compter à la main le nombre d'appels récursifs pour `puissance(7, 20)`.

#### Tours de Hanoï
Utiliser une fonction récursive pour résoudre [ce problème]() sur FranceIOI.

#### Arbre de Pythagore
#### Flocon de Von Koch
#### Triangle de Pascal
#### Fonction d'Ackermann
#### Récursions imbriquées

D'après John McCarthy :

$$
f_{91}(n)=
\begin{cases}
n-10, &\text{si } n > 100\\
f_{91}\left(f_{91}(n+1)\right), &\text{si } n \leqslant 100\\
\end{cases}
$$

1. Implémenter cette fonction en Python.
2. Donner un tableau de valeurs de $f_{91}(n)$, pour $n\in [\![0..100]\!]$.



