# Correction de certains exercices
[TOC]

## La Pile

### Implémentation avec les listes dynamiques de Python

**Exercice 3** : Pour cet exercice, on supposera qu'on ne dispose **que** du constructeur d'une pile vide, ainsi que des méthodes `est_vide(self)`, `.empile(self, élément)` et `.dépile(self)`. 
* Question 1 : Que fait la méthode `mystère` suivante ? Donner un vrai nom et une *doctring*. On testera à la main sur l'exemple simple : 
    * sommet de la pile $\rightarrow 4, 6, 3, 9, 7 |$.

```python
    # suite de class Pile():
    def mystère(self) -> Pile:
        autre = Pile()
        while not self.est_vide():
            autre.empile(self.dépile())
        return autre
```

> Correction Question 1
```python
    # suite de class Pile():
    def renverse(self):# -> Pile:
        """Renvoie une version renversée de la pile self, tout en la vidant.
        """
        autre = Pile()
        while not self.est_vide():
            autre.empile(self.dépile())
        return autre
```


* Question 2 : Proposer alors une méthode `.hauteur(self)-> int` qui renvoie la hauteur d'une pile, en la laissant inchangée en fin de compte. *Rappel* : on ne dispose pas du détail d'implémentation, et on ne peut donc pas utiliser `len` ; d'ailleurs sur quel objet ?!?

> Correction question 2

On va renverser deux fois la pile, et compter lors d'un des deux renversements combien d'éléments sont présents.

```python
    # suite de class Pile():
    def hauteur(self) -> int:
        """Renvoie la hauteur de la pile,
        en la laissant intacte *in fine*.
        """
        h = 0
        autre = Pile()
        while not self.est_vide():
            autre.empile(self.dépile())
            h += 1
        while not autre.est_vide():
            self.empile(autre.dépile())
        return h
```


* Question 3 : Proposer une méthode `.max_pile(self, i: int) -> int` qui renvoie la (plus petite) position de l'élément maximal parmi les `i` derniers empilés. La position du sommet de la pile est, par convention ici, égale à $1$. La pile doit être inchangée en fin de compte.

> Correction question 3

```python
    # suite de class Pile():
    def max_pile(self, i: int) -> int:
        """Renvoie la (plus petite) position de l'élément maximal parmi
        les `i` derniers empilés.
        La position du sommet de la pile est,
        par convention ici, égale à $1$.
        """
        autre = Pile()
        pos = pos_max = 1
        maxi = self.dépile()
        autre.empile(maxi)
        for _ in range(i - 1):
            truc = self.dépile()
            pos += 1
            if truc > maxi:
                maxi = truc
                pos_max = pos
            autre.empile(truc)
        for _ in range(i):
            self.empile(autre.dépile())
        return pos_max
```



* Question 4 : Proposer une méthode `.retourner(self, i: int) -> None` qui modifie la pile en inversant l'ordre des `i` derniers éléments empilés. *On peut utiliser deux piles auxiliaires*.

> Correction question 4

On dépile $i$ éléments, que l'on inverse dans une seconde pile pour la remettre enfin dans `self`.

```python
    # suite de class Pile():
    def retourner(self, i: int) -> None:
        """Modifie la pile en inversant l'ordre des
        `i` derniers éléments empilés.
        """
        autre = Pile()
        for _ in range(i):
            autre.empile(self.dépile())
        autre_bis = Pile()
        for _ in range(i):
            autre_bis.empile(autre.dépile())
        for _ in range(i):
            self.empile(autre_bis.dépile())
```

### Implémentation de façon récursive

> Correction des exercices

```python
class Pile():
    def __init__(self, données=None):
        self.__données = données

    def est_vide(self):
        return self.__données is None

    def empile(self, élément):
        queue = self.__données
        tête = élément
        self.__données = (tête, queue)
    
    def dépile(self):
        if self.est_vide():
            raise ValueError('Pile vide')
        tête, queue = self.__données
        self.__données = queue
        return tête

    def hauteur(self):
        """Renvoie la hauteur de la pile"""
        if self.est_vide():
            return 0
        tête, queue = self.__données
        return 1 + Pile(queue).hauteur()

    # Exercice 1
    def somme(self):
        """Renvoie la somme des valeurs.
        On suppose qu'elles sont entières.
        """
        if self.est_vide():
            return 0
        tête, queue = self.__données
        return tête + Pile(queue).somme()

    # Exercice 2
    def contient_valeur(self, valeur):
        """ La pile contient-elle la valeur ?
        """
        if self.est_vide():
            return False
        tête, queue = self.__données
        return (tête == valeur) or Pile(queue).contient_valeur(valeur)
    
```

> **Remarque** : Cette façon de faire n'est pas idéale. On aimerait pouvoir obtenir une véritable pile dans `queue` et non juste ses données lorsqu'on fait :
```python
        tête, queue = self.__données
```
On est ensuite obligé de d'utiliser avec `Pile(queue)`.
Avec d'autres langages de programmation, comme Ocaml, il est possible avec du filtrage par motifs d'écrire cette abstraction de manière bien plus naturelle.

Essayons encore avec Python.

```python
class Pile():
    # Ce code est incorrect !!!
    def __init__(self):
        self.pile = None
    
    def est_vide(self):
        return self.pile is None
    
    def empile(self, élément):
        self.pile = (élément, self) # ici !!!
    
    def __str__(self):
        if self.est_vide():
            return ""
        tête, queue = self.pile
        return str(tête) + "::" + queue.__str__()
    
    def hauteur(self):
        if self.est_vide():
            return 0
        tête, queue = self.pile
        return 1 + queue.hauteur()
```

Ce code est incorrect ; à la ligne commentée `# ici !!!`, on a `self` qui fait référence à lui-même dans son état actuel mais aussi futur après l'affectation.

On verra comment contourner ce problème avec l'utilisation de deux classes. Ce sera une introduction aux listes chaînées.

Cependant cette construction se retrouve avec d'autres langages de programmation comme avec OCaml, où on retrouve du code comme :

```ocaml
let rec hauteur pile = match pile with
        | [] -> 0
        | tete :: queue  -> 1 + (hauteur queue)
```

Ce code se lit : 
> Définissons par récurrence, une fonction hauteur pour un paramètre pile par : suivant que pile est : 
>* soit une liste vide ; on renvoie zéro,
>* soit une tête suivie d'une queue ; on renvoie 1 (la hauteur de la tête), plus la hauteur de la queue déterminée par récurrence.

On voit là tout l'intérêt de pouvoir définir une structure de données récursive et d'utiliser le filtrage par motif.


## La *deque*

Une structure de données à la fois pile et file.

On va proposer ici une structure de données linéaires, agencée sur une ligne gauche-droite. On demande un cahier des charges :
* Constructeur
* Test pour être vide
* Ajout élément à gauche
* Extraction élément à gauche
* Ajout élément à droite
* Extraction élément à droite

### Première approche, liste dynamique

On utilise les facilités du langage Python (avec les listes dynamiques) pour construire la `class Deque`.

```python
class Deque():
    def __init__(self):
        self.données = []

    def est_vide(self):
        return self.données == []

    def ajout_gauche(self, élément):
        self.données = [élément] + self.données

    def ajout_droite(self, élément):
        self.données.append(élément)

    def extrait_gauche(self):
        if self.est_vide():
            raise ValueError("Liste vide")
        élément_gauche = self.données.pop(0)
        return élément_gauche

    def extrait_droite(self):
        if self.est_vide():
            raise ValueError("Liste vide")
        élément_droite = self.données.pop()
        return élément_droite

if __name__ == '__main__':
    def test_init_vide():
        """
        >>> test_init_vide()
        True
        """
        test = Deque()
        return test.est_vide()
    
    def test_droite():
        """
        >>> test_droite()
        (42, True)
        """
        test = Deque()
        test.ajout_droite(42)
        élément = test.extrait_droite()
        return (élément, test.est_vide())

    def test_gauche():
        """
        >>> test_gauche()
        (1337, True)
        """
        test = Deque()
        test.ajout_gauche(1337)
        élément = test.extrait_gauche()
        return (élément, test.est_vide())

    import doctest
    doctest.testmod()
```

Cette méthode n'est pas efficace pour l'ajout et l'extraction à gauche !

### Seconde approche, module *collections*

On utilise encore plus les facilité du langage Python, la structure de données *Deque* est incluse dans `collections`.

[Lire la documentation Python de la deque](https://docs.python.org/fr/3/library/collections.html#collections.deque)

Cette méthode est efficace, c'est celle qu'il faut utiliser avec le langage Python ; cependant elle n'est pas pédagogique. Voyons une façon de construire une implémentation efficace.

### Troisième approche, file à deux piles

Comme pour la file implémentée avec deux piles, on peut aussi implémenter la deque avec deux piles.

```python
import pile

class Deque:
    def __init__(self):
        self.pile_gauche = pile.Pile()
        self.pile_droite = pile.Pile()
    
    def est_vide(self):
        return self.pile_gauche.est_vide() and self.pile_droite.est_vide()
    
    def ajout_gauche(self, élément):
        self.pile_gauche.empile(élément)

    def ajout_droite(self, élément):
        self.pile_droite.empile(élément)

    def extrait_gauche(self):
        if self.est_vide():
            raise ValueError("Liste vide")
        if self.pile_gauche.est_vide():
            while not self.pile_droite.est_vide():
                self.pile_gauche.empile(self.pile_droite.dépile())
        élément_gauche = self.pile_gauche.dépile()
        return élément_gauche

    def extrait_droite(self):
        if self.est_vide():
            raise ValueError("Liste vide")
        if self.pile_droite.est_vide():
            while not self.pile_gauche.est_vide():
                self.pile_droite.empile(self.pile_gauche.dépile())
        élément_droite = self.pile_droite.dépile()
        return élément_droite
```

Cette construction est efficace sauf dans le cas où une des deux piles est vide et alternativement on extrait un élément à gauche puis à droite. Dans ce cas, les piles sont alternativement retournées...

Voyons une construction réellement efficace, ce sera une bonne introduction aux listes chaînées.

### Quatrième approche, introduction aux listes chaînées

