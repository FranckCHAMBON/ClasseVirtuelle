# Correction de certains exercices


## La *deque*

Une structure de données à la fois pile et file.

On va proposer ici une structure de données linéaires, agencée sur une ligne gauche-droite. On demande un cahier des charges :
* Constructeur
* Test pour être vide
* Ajout élément à gauche
* Extraction élément à gauche
* Ajout élément à droite
* Extraction élément à droite


Comme pour la file, on peut aussi proposer une implémentation via un tableau de taille donnée, ce qui limite la taille de la deque...

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

Cette méthode est efficace, c'est celle qu'il faut utiliser avec le langage Python ; cependant elle n'est pas pédagogique. Tentons une façon de construire une implémentation efficace.

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

Pour une construction réellement efficace, on utilisera des listes doublement chaînées.
