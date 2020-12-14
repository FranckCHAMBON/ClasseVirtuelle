# Structures linéaires

## Rappels sur le tableau

Un tableau `table` est une structure abstraite de données élémentaire :
* avec des éléments de même type, et de même taille `taille_élément`,
* un nombre d'éléments fixé à la création ; `nb_éléments`,
* rangés de façon continue en mémoire, indicés de `0` inclus à `nb_éléments` exclu.

> En interne, on accède, en pratique, à un élément d'indice `i` du tableau par son adresse mémoire qui est égale à `adresse_tableau + i * taille_élément`.

On peut lire et modifier un élément d'indice `i` avec `table[i]`.

Avec cette structure de données, on peut résoudre de nombreux problèmes, et comme nous allons le voir, on peut construire de nouvelles structures de données.

Concrètement, on retrouve des implémentations de cette structure abstraite dans la plupart des langages de programmation. Une limitation évidente est la taille d'un tableau, limitée par la capacité de mémoire disponible ; sinon, c'est assez simple.

## La pile

Pour une version simple (éléments de même taille).

On utilisera les notations de la POO.

* C'est une structure abstraite de donnée linéaire (agencée en ligne en mémoire).
* Les éléments sont de même type et de même taille.
* On dispose de méthodes :
    * `Pile()` pour construire et initialiser une pile vide.
    * `.est_vide()` renvoie un booléen, `True` pour une pile vide.
    * `.empile(élément)` ajoute un `élément` au sommet de la pile.
    * `.dépile()` enlève l'élément au sommet de la pile, et le renvoie.
    * Éventuellement d'autres méthodes...

### Implémentation sans sucre syntaxique

On propose ici, en Python, une implémentation qui utilise en arrière-plan une structure de type `list` de Python, en limitant volontairement l'usage, comme un tableau. Ainsi l'implémentation pourrait être réalisée dans de nombreux langages de programmation avec de rares ajustements.

```python
class Pile():
    """
    Construit une classe "pile d'entiers", de taille 'taille',
    sans sucre syntaxique, sauf pour la méthode __str__ à usage interne.
    """

    def __init__(self, taille: int):
        self.taille = taille
        self.données = [0 for _ in range(taille)] # un tableau
        self.hauteur = 0

    def est_vide(self) -> bool:
        return self.hauteur == 0

    def empile(self, élément):
        """Ajoute `élément` au sommet de la pile"""
        if self.hauteur == self.taille:
            raise ValueError('Pile pleine')
        self.données[self.hauteur] = élément
        self.hauteur += 1
    
    def dépile(self):
        """Enlève et renvoie l' `élément` au sommet de la pile.
        """
        if self.est_vide():
            raise ValueError('Pile vide')
        self.hauteur -= 1
        élément = self.données[self.hauteur]
        #self.données[self.hauteur] = 0 # optionnel
        return élément
```

On peut ajouter une méthode `__str__` avec du sucre syntaxique uniquement pour un usage interne ou de tests.

```python
    def __str__(self) -> str:
        "avec sucre... usage interne, pour nous seulement"
        ans = "[Début de pile] "
        for i in range(self.hauteur):
            ans += str(self.données[i])
            ans += ", "
        ans += " [Fin de pile.]"
        return ans
```

Idéalement, il faudrait écrire les attributs `hauteur` et `données` en les préfixant de `__` pour les rendre privés. **Exercice 1** : faire cela et justifier ce choix.

**Exercice 2** : Ajouter une méthode accesseur `.hauteur()`.

**Exercice 3** : Vérifier l'utilisation avec le code suivant.

```python
ma_pile = Pile(100)
for x in range(20):
    ma_pile.empile(x*x + 2)
print(ma_pile)

for i in range(11):
    print("valeur dépilée :", ma_pile.dépile())

print("Et ensuite")

print(ma_pile)

ma_pile.empile(1337)

print(ma_pile)

print(dir(ma_pile))
```

* Tester `2000` au lieu de `20`.
* Tester `31` au lieu de `11`.
* Repérer, et justifier, où dans le code on gère ces erreurs.


### Implémentation avec sucre
On peut facilement implémenter une pile de taille arbitraire avec le type `list` de Python et les méthodes `.append(élément)` et `.pop()`.

```python
class Pile():
    def __init__(self):
        self.données = []

    def __str__(self) -> str:
        return str(self.données)

    def est_vide(self) -> bool:
        return self.données == []

    def empile(self, valeur):
        self.données.append(valeur)
    
    def dépile(self):
        if self.est_vide():
            raise ValueError('Pile vide')
        return self.données.pop()
```

**Exercice 1** : rendre l'attribut `données` privé et ajouter une méthode `.hauteur()`.
Refaire les tests vus précédemment.

**Exercice 2** : Résoudre le problème [Dates de péremption](http://www.france-ioi.org/algo/task.php?idChapter=527&idTask=356) sur France-IOI.

## La file

* Le principe de la pile est : *FILO : First In, Last Out*, (premier entré, dernier sorti).
* Le principe de la file est : *FIFO : First In, First Out*, (premier entré, premier sorti).

**Exercice 1** : En s'inspirant de la **première** implémentation de la pile, donner une implémentation d'une file d'une certaine taille maximale. On proposera les méthodes de constructions ainsi que `.est_vide()`, `.enfile(élément)` et `.défile()` analogues au cas de la pile.

**Exercice 2** : Résoudre le problème [Distributeur automatique](http://www.france-ioi.org/algo/task.php?idChapter=527&iOrder=2) sur France-IOI.


> **Conseil** : on peut résoudre les problèmes dans un premier temps sans l'écriture avec style POO. Cependant, on demande alors une seconde écriture. Pourquoi ?
> * Le jour où on dispose d'une meilleure structure de données, il suffit de remplacer uniquement le bout de code de la classe, le problème restant intact. Sans POO, il faut réécrire tout le problème pour utiliser les nouvelles idées... L'écriture avec le stye POO permet de s'affranchir presque totalement de la manière dont est écrit la classe. Il faut en revanche **toujours** garder à l'esprit : quel est le coût algorithmique de chaque méthode ?