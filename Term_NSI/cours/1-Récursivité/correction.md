# Correction des exercices {ignore}

[TOC]

## Nombre de chiffres
Écrire une version récursive d'une fonction qui renvoie le nombre de chiffres d'un entier strictement positif.
> **Indice** : Quel est le nombre de chiffres de $n$, par rapport à celui de $n$ divisé par $10$ ?


### Solution

```python
def nb_chiffres(n: int) -> int:
    """Renvoie le nombre de chiffres de n.
    n écrit en base 10.

    >>> nb_chiffres(42)
    2
    >>> nb_chiffres(1337)
    4

    """
    if n < 10:
        return 1
    else:
        return 1 + nb_chiffres(n // 10)
```

Par exemple, `nb_chiffres(1337) = 1 + nb_chiffres(133) = 1 + 1 + nb_chiffres(13) = 1 + 1 + 1 + nb_chiffres(1) = 1 + 1 + 1 + 1 = 4`


## Nombre de bits égaux à 1
Écrire une version récursive d'une fonction qui renvoie le nombre de bits égaux à $1$ d'un entier strictement positif.
> **Indice** : S'inspirer de l'exercice précédent.

### Solution

```python
def nb_bits_à_1(n: int) -> int:
    """Renvoie le nombre de bits de n égaux à 1.
    n écrit en binaire.
    Exemples :
    * 7 = (111)_2 -> 3
    * 17 = (10001)_2 -> 2

    >>> nb_bits_à_1(7)
    3
    >>> nb_bits_à_1(17)
    2

    """
    if n < 2:
        return n
    else:
        bit_faible = n % 2
        return bit_faible + nb_bit_à_1(n // 2)
```

> Remarque, il existe des opérateurs basiques pour obtenir le bit de poids faible, et la division par deux d'un entier.

```python
def nb_bits_à_1(n: int) -> int:
    """Renvoie le nombre de bits de n égaux à 1.
    n écrit en binaire.
    Exemples :
    * 7 = (111)_2 -> 3
    * 17 = (10001)_2 -> 2

    >>> nb_bits_à_1(7)
    3
    >>> nb_bits_à_1(17)
    2

    """
    if n < 2:
        return n
    else:
        bit_faible = n & 1
        return bit_faible + nb_bit_à_1(n >> 1)
```

* `&` réalise un `et logique bit à bit`. Appliqué avec le masque `1`, on obtient le bit de poids faible.
* `>>` réalise un décalage à droite de l'écriture binaire, avec perte des bits de poids faible. Décaler de 1 revient à diviser par deux.


## Calcul de puissance
En partant du principe que :
* si $n$ est pair, alors $a^n = \left(a^{n/2}\right)^2$
* si $n$ est impair, alors $a^n = \left(a^{(n-1)/2}\right)^2×a$

> Exemples 
> 1. $a^{2021} = (a^{1010})^2×a$
> 2. $a^{1010} = (a^{505})^2$
> 3. ...

1. Écrire une fonction récursive `puissance(a, n)` qui renvoie $a^n$.
> **Indice** : Penser au cas de base !
2. Compter à la main le nombre d'appels récursifs pour `puissance(7, 20)`.

### Solution
```python
def puissance(a, n: int):
    """Renvoie `a` à la puissance `n`.

    >>> puissance(13, 0)
    1
    >>> puissance(3, 5)
    243
    
    """
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            # n est pair
            return puissance(a, n//2) ** 2
        else:
            # n est impair
            return puissance(a, n//2) ** 2 * a
```

Et une version un peu plus efficace, avec un code un peu factorisé.

```python
def puissance(a, n: int):
    """Renvoie `a` à la puissance `n`.

    >>> puissance(13, 0)
    1
    >>> puissance(3, 5)
    243
    
    """
    if n == 0:
        return 1
    else:
        a_demi_n = puissance(a, n >> 1)
        carré = a_demi_n * a_demi_n
        if n & 1 == 0: # n est pair
            return carré
        else:          # n est impair
            return carré * a
```


## Tours de Hanoï
Utiliser une fonction récursive pour résoudre [ce problème]() sur FranceIOI.

### Solution
Suivre ce [lien](https://franckchambon.github.io/ClasseVirtuelle/Term_NSI/N3/8-R%C3%A9cursivit%C3%A9/4-Tours_de_Hano%C3%AF.html).

## Arbre de Pythagore
## Flocon de Von Koch
## Triangle de Pascal
## Fonction d'Ackermann
## Récursions imbriquées

D'après John McCarthy :

$$
f_{91}(n)=
\begin{cases}
n-10, &\text{si } n > 100\\
f_{91}\left(f_{91}(n+11)\right), &\text{si } n \leqslant 100\\
\end{cases}
$$

1. Implémenter cette fonction en Python.
2. Donner un tableau de valeurs de $f_{91}(n)$, pour $n\in [\![0..100]\!]$.

### Solution

```python
def f_91(n: int) -> int:
    if n > 100:
        return n - 10
    else:
        return f_91(f_91(n + 11))

print([f_91(n) for n in range(101)])
```

```
[91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91]
```

On constate que la [fonction 91](https://fr.wikipedia.org/wiki/Fonction_91_de_McCarthy) est constante sur $[\![0..100]\!]$.

## Nombre de façons d'écrire comme une somme ==**Nouveau**==
On considère $f(n)$ : le nombre de façons d'écrire un entier $n>0$ comme somme d'entiers strictement positifs, sans tenir compte de l'ordre.

Par exemple, $5$ peut s'écrire de $f(5) = 7$ façons :
* $1+1+1+1+1$ ; la somme la plus longue,
* $2+2+1$,
* $1+3+1$,
* $2+3$,
* $5$ ; oui, une somme à un seul terme,
* $1+4$,
* $1+2+1+1$.

Écrire une fonction qui renvoie $f(n)$.