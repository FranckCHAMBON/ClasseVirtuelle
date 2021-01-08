# Correction de certains exercices

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
