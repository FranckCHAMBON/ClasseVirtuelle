# Correction du BAC blanc

## Exercice 1

1. `mystère` est une fonction **récursive**.
2. Les étapes sont :
    * `mystère(3, 5)` appelle `mystère(3, 2)` qui appelle `mystère(3, 1)` qui appelle `mystère(3, 0)` qui renvoie `1`.
    * Ensuite, comme `1%2 == 0` est faux, `mystère(3, 1)` renvoie `1 * 1 * 3`, donc `3`.
    * Ensuite, comme `2%2 == 0` est vrai, `mystère(3, 2)` renvoie `3 * 3`, donc `9`.
    * Ensuite, comme `5%2 == 0` est faux, `mystère(3, 5)` renvoie `9 * 9 * 3`, donc `243`.
3. Une `docstring` avec `doctest` serait donc :
```python
def mystère(a: int, b: int) -> int:
    """ Renvoie `a` à la puissance `b`.

    >>> mystère(7, 0)
    1
    >>> mystère(3, 5)
    243
    
    """
    ...
```
4. On propose :
```python
def mystère_force_brute(a: int, b: int) -> int:
    """ Renvoie `a` à la puissance `b`.

    >>> mystère_force_brute(7, 0)
    1
    >>> mystère_force_brute(3, 5)
    243
    
    """
    puissance = 1
    for _ in range(b):
        puissance = puissance * a
    return puissance
```
`mystère_force_brute(3, 1000)` effectue $1000$ tours de boucle avec une multiplication à chaque fois.
5. `mystère(a, b)` fait des appels récursifs jusqu'à ce que `b` soit nul, en faisant une ou deux multiplications à chaque fois. Le nombre d'appels récursifs est le nombre de fois que `b` peut être divisé par deux avant de devenir nul ; (c'est presque le logarithme en base de deux de `b`) ; c'est presque le nombre de chiffres en binaire de `b`. Le coût est donc presque proportionnel au nombre de chiffres de `b`.

* Pour `mystère(3, 1000)`, il y a $1$ multiplication, plus le calcul de `mystère(3, 500)` ;
* Pour `mystère(3, 500)`, il y a $1$ multiplication, plus le calcul de `mystère(3, 250)` ;
* Pour `mystère(3, 250)`, il y a $1$ multiplication, plus le calcul de `mystère(3, 125)` ;
* Pour `mystère(3, 125)`, il y a $2$ multiplications, plus le calcul de `mystère(3, 62)` ;
* Pour `mystère(3, 62)`, il y a $1$ multiplication, plus le calcul de `mystère(3, 31)` ;
* Pour `mystère(3, 31)`, il y a $2$ multiplications, plus le calcul de `mystère(3, 15)` ;
* Pour `mystère(3, 15)`, il y a $2$ multiplications, plus le calcul de `mystère(3, 7)` ;
* Pour `mystère(3, 7)`, il y a $2$ multiplications, plus le calcul de `mystère(3, 3)` ;
* Pour `mystère(3, 3)`, il y a $2$ multiplications, plus le calcul de `mystère(3, 1)` ;
* Pour `mystère(3, 1)`, il y a $2$ multiplications, plus le calcul de `mystère(3, 0)` ;
* Pour `mystère(3, 0)`, il y a $0$ multiplication, le résultat est renvoyé directement.
* **Le total est de $16$ multiplications**, ce qui est nettement mieux que $1000$ avec la force brute.

6. Alors,
    * Quand on multiplie des entiers plus grands que $1$, le résultat augmente, et en gros le nombre de chiffres est la somme de ceux des opérandes. Les multiplications deviennent très vite entre des grands nombres, et la multiplication prend alors plus de temps, ce n'est donc pas à coût constant.
    * En calcul modulaire, on conserve un résultat intermédiaire inférieur au modulo, et donc nous n'avons pas d'augmentation significative de la taille du résultat, et donc le coût de la multiplication modulaire reste constant (en première approximation).

## Exercice 2
1. `tableau` est une liste Python.
2. Oui, on peut définir `f` après `tableau_valeurs`. Ce qui compte c'est de la définir **avant** de s'en servir effectivement.
3. Il y avait plusieurs erreurs. `f = lambda t: 10 // (t - 2)`
4.
    * `f(2)` provoque une erreur de division par zéro.
    * `f(4)` renvoie `10 // 2`, soit $5$.
    * `f(8)` renvoie `10 // 6`, soit $1$.
    * `f(16)` renvoie `10 // 14`, soit $0$.
5. * `tableau_valeurs(f, -2, 4)` essaie de calculer `f(x)` pour `x` de `-2` inclus à `4` exclu.
    * Tous les essais réussissent, sauf pour `x` qui vaut `2`, dans ce cas, l'erreur de division par zéro est capturée, puis ignorée (`pass`).
    * `tableau` prend alors les valeurs successives :
        * `[]`
        * `[(-2, -3)]`
        * `[(-2, -3), (-1, -4)]`
        * `[(-2, -3), (-1, -4), (0, -5)]`
        * `[(-2, -3), (-1, -4), (0, -5), (1, -10)]`
        * `[(-2, -3), (-1, -4), (0, -5), (1, -10), (3, 10)]`

## Exercice 3

1. `donne_taille` et `donne_liste` sont des méthodes **accesseurs**, en anglais des *getter*.
2. Préfixer de `__` permet de rendre les attributs **privés**.
3. Code
```python
class ListeCroissante:
    def __init__(self):
        self.__liste = []
        self.__taille = 0

    def donne_taille(self):
        return self.__taille

    def donne_liste(self):
        """
        Renvoie la liste dans l'ordre croissant.
        """
        return self.__liste

    def ajoute(self, x):
        """Ajoute l'élément x dans la liste à une place qui maintient l'ordre croissant,
        en décalant le reste de la liste si nécessaire.
        """
        i = 0
        while (i < self.__taille) and (__liste[i] < x):
            i += 1
        while (i < self.__taille):
            y = self.__liste[i]
            self.__liste[i] = x
            x = y
        self.__liste.append(x)
        self.__taille += 1

    def contient(self, x):
        """Renvoie True si x est dans la liste.
        """
        for i in range(self.__taille):
            if self.__liste[i] == x:
                return True
            #optionnel, retour prématuré
            if self.__liste[i] > x:
                # les suivants seront encore plus grands
                return False
        return False


    def extrait(self, x):
        i = 0
        while (i < self.__taille) and (__liste[i] < x):
            i += 1
        if (i == self.__taille) or (self.__liste[i] != x):
            raise ValueError("x absent de la liste")
        while (i+1 < self.__taille):
            self.__liste[i] = self.__liste[i+1]
        self.__liste.pop()
        self.__taille -= 1
```

## Exercice 4
1. L'état de la pile est :
    * `[]`, on va empiler `1`,
    * `[1]`, on va empiler `2`,
    * `[1, 2]`, on va empiler `3`,
    * `[1, 2, 3]`, on va appliquer l'opération `*`,
    * `[1, 6]`, on va appliquer l'opération `+`,
    * `[7]`, on va empiler `4`,
    * `[7, 4]`, on va appliquer l'opération `*`,
    * `[28]`, on a fini !
2. code
```python
def calcule_RPN(expression: str) -> int:
    pile = []
    taille = 0
    for argument in expression.split(" "):
        if argument == '+':
            if taille < 2:
                raise ValueError("mauvaise expression")
            entier_2 = pile.pop()
            entier_1 = pile.pop()
            pile.append(entier_1 + entier_2)
            taille -= 1
        elif argument == '-':
            if taille < 2:
                raise ValueError("mauvaise expression")
            entier_2 = pile.pop()
            entier_1 = pile.pop()
            pile.append(entier_1 - entier_2)
            taille -= 1
        elif argument == '*':
            if taille < 2:
                raise ValueError("mauvaise expression")
            entier_2 = pile.pop()
            entier_1 = pile.pop()
            pile.append(entier_1 * entier_2)
            taille -= 1
        elif argument == '/':
            if taille < 2:
                raise ValueError("mauvaise expression")
            entier_2 = pile.pop()
            entier_1 = pile.pop()
            pile.append(entier_1 // entier_2)
            taille -= 1
        else:
            # argument devrait être un entier
            try:
                un_entier = int(argument)
            except:
                raise ValueError("mauvaise expression")
            pile.append(un_entier)
            taille += 1
    if taille != 1:
        raise ValueError("mauvaise expression")
    return pile[0]
```

## Exercice 6
1. En prenant `True` à $1$ et `False` à $0$, on a :
$$f ([\text{True}, \text{True}, \text{False}, \text{True}]) = 2^4 + 1×2^3 + 1×2^2 + 0×2^1 + 1×2^0$$
$$f ([\text{True}, \text{True}, \text{False}, \text{True}]) = 16 + 8 + 4 + 0 + 1$$
$$f ([\text{True}, \text{True}, \text{False}, \text{True}]) = 29$$
2. $42 = 32+8+2 = (101010)_2$, ainsi $$f ([\text{False}, \text{True}, \text{False}, \text{True}, \text{False}]) = 42$$
3. Pour une liste de $n$ booléens, $b$ prendrait $8n$ octets, soit $64n$ bits. Alors que $f(b)$ prend $n+1$ bits. C'est bien mieux !
4. Code
```python
class PileBool:
    def __init__(self):
        self.pile = 1
    
    def est_vide(self):
        return self.pile == 1
    
    def empile(self, x: bool):
        self.pile *= 2
        if x:
            self.pile += 1
    
    def dépile(self):
        x = self.pile % 2
        self.pile //= 2
        return x == 1
```

## Exercice 7
1.  * À l'étape $0$, on dispose de `"b"`.
    * À l'étape $1$, on dispose donc de `"abb"` en plus de `"b"`.
    * À l'étape $2$, on dispose donc de `"a"+"b"+"abb"`, `"a"+"abb"+"b"` et `"a"+"abb"+"abb"`, en plus,
        * c'est-à-dire `"ababb", "aabbb", "aabbabb"`.
2. 
    * À l'étape $3$, on dispose de nouveaux mots :
        * Avec `"ababb"` seul en nouveau :
            * `"a"+"ababb"+"b"`, soit `"aababbb"`
            * `"a"+"ababb"+"abb"`, soit `"aababbabb"`
            * `"a"+"b"+"ababb"`, soit `"abababb"`
            * `"a"+"abb"+"ababb"`, soit `"aabbababb"`
        * Avec `"aabbb"` seul en nouveau :
            * `"a"+"aabbb"+"b"`, soit `"aaabbbb"`
            * `"a"+"aabbb"+"abb"`, soit `"aaabbbabb"`
            * `"a"+"b"+"aabbb"`, soit `"abaabbb"`
            * `"a"+"abb"+"aabbb"`, soit `"aabbaabbb"`
        * Avec `"aabbabb"` seul en nouveau :
            * `"a"+"aabbabb"+"b"`, soit `"aaabbabbb"`
            * `"a"+"aabbabb"+"abb"`, soit `"aaabbabbabb"`
            * `"a"+"b"+"aabbabb"`, soit `"abaabbabb"`
            * `"a"+"abb"+"aabbabb"`, soit `"aabbaabbabb"`
        * Avec `"ababb"` et `"aabbb"`
            * ...
        * Avec `"ababb"` et `"aabbb"`
            * ...
        * ...
3.  * À l'étape $0$, tous les mots (il n'y en a qu'un) vérifie la propriété ; il y a un `b`, un de plus que de `a` (zéro).
    * À chaque nouveau mot, il est construit avec `"a"+ mot_1 + mot_2`, 
        * le nombre de `a` est **un plus** celui de `mot_1` plus celui de `mot_2`.
        * On note `#mot_a = 1 + #mot_1_a + #mot_2_a`
        * On a aussi `#mot_b = 0 + #mot_1_b + #mot_2_b`
    * Mais on avait
        * `#mot_1_b = 1 + #mot_1_a`, et 
        * `#mot_2_b = 1 + #mot_2_a`, et 
    * Donc `#mot_b = 0 + (1+#mot_1_a) + (1+#mot_2_a)`
    * D'où `#mot_b = 1 + (1 + #mot_1_a + #mot_2_a)`
    * D'où `#mot_b = 1 + #mot_a`
    * D'où la propriété qui reste vraie à chaque nouveau mot.
