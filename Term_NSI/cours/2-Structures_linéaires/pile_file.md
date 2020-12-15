# 🚛 Structures linéaires

## Rappels sur le tableau

> Exemple d'un tableau, le début des nombres premiers.

|Indice | $0$ | $1$ | $2$ | $3$ |
|-------|-----|-----|-----|-----|
|Élément| $2$ | $3$ | $5$ | $7$ |

Un tableau `table` est une structure de données, abstraite et élémentaire :
* avec des éléments de même type, et de même taille `taille_élément`,
* un nombre d'éléments fixé à la création ; `nb_éléments`,
* rangés de façon continue en mémoire, indicés de `0` **inclus** à `nb_éléments` **exclu**.

> En interne, on accède, en pratique, à un élément d'indice `i` du tableau par son adresse mémoire qui est égale à `adresse_tableau + i * taille_élément`.

On peut lire et modifier un élément d'indice `i`, avec un langage de programmation, on note très souvent `table[i]` cet élément de `table` d'indice `i`.

Avec cette structure de données, on a déjà résolu de nombreux problèmes, mais on peut aussi construire de nouvelles structures de données.

Concrètement, on retrouve des implémentations de cette structure abstraite, le tableau, dans la plupart des langages de programmation. Une limitation évidente est la taille d'un tableau, limitée par la capacité de mémoire disponible ; sinon, c'est assez simple.

* Le cours de première est toujours [accessible ici](https://franckchambon.github.io/ClasseVirtuelle/NSI/nsi-accueil.html).

## La pile

Pour une version simple (éléments de même taille).

On utilisera les notations de la POO.

* C'est une structure abstraite de donnée linéaire (agencée en ligne en mémoire).
* Les éléments sont de même type et de même taille.
* On dispose de méthodes :
    * Le constructeur `Pile()`, via la méthode `.__init__(self)` qui initialise une pile vide.
    * `.est_vide(self)` renvoie un booléen, `True` pour une pile vide.
    * `.empile(self, élément)` ajoute un `élément` au sommet de la pile.
    * `.dépile(self)` enlève l'élément au sommet de la pile, et le renvoie.
    * Éventuellement d'autres méthodes...

![](Stack_(data_structure)_LIFO.svg.png)
> Image : [wikipedia, la pile](https://fr.wikipedia.org/wiki/Pile_%28informatique%29)

### Implémentation avec tableau

On propose ici, en Python, une implémentation qui utilise en arrière-plan une structure de type `list` de Python, **mais** en limitant volontairement l'usage, comme **un tableau**, sans méthode dynamique. Ainsi l'implémentation pourrait être réalisée dans de nombreux langages de programmation avec de rares ajustements.

```python
class Pile():
    """
    Une classe "pile d'entiers", de taille maximale 'taille_max',
    implémentée avec les données dans un tableau.
    """

    def __init__(self, taille_max: int):
        self.taille_max = taille_max
        self.données = [0 for _ in range(taille)] # un tableau
        self.hauteur = 0

    def est_vide(self) -> bool:
        return self.hauteur == 0

    def empile(self, élément):
        """Ajoute `élément` au sommet de la pile"""
        if self.hauteur == self.taille_max:
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

On pourrait ajouter une méthode `.__str__(self)`.

```python
    def __str__(self) -> str:
        "Pour usage interne, tests"
        ans = "[Début de pile] "
        for i in range(self.hauteur):
            ans += str(self.données[i])
            ans += ", "
        ans += " [Fin de pile.]"
        return ans
```

Idéalement, il faudrait écrire les attributs `taille_max`, `hauteur` et `données` en les préfixant de `__` pour les rendre privés. **Exercice 1** : faire cela et justifier ce choix.

**Exercice 2** : Ajouter une méthode accesseur `.hauteur(self)`. Cela donne une raison de plus d'avoir préfixé l'attribut !

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


### Implémentation avec les listes dynamiques de Python
On peut facilement implémenter une pile de taille arbitraire avec le type `list` de Python et ses méthodes `.append(self, élément)` et `.pop(self)`. Tous les langages de programmation ne le permettent pas aussi facilement...

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

> On remarque que nous n'avons pas ici (besoin) de méthode ni d'attribut `hauteur`... Pour le type abstrait pile, on travaille parfois sans l'avoir disponible au départ.

**Exercice 1** : rendre l'attribut `données` privé et ajouter une méthode `.hauteur(self)`.
Refaire les tests vus précédemment.

**Exercice 2** : Résoudre le problème [Dates de péremption](http://www.france-ioi.org/algo/task.php?idChapter=527&idTask=356) sur France-IOI.

**Exercice 3** : Pour cet exercice, on supposera qu'on ne dispose **que** du constructeur d'une pile vide, ainsi que des méthodes `est_vide(self)`, `.empile(self, élément)` et `.dépile(self)`. 
* Question 1 : Que fait la méthode suivante ? Donner un vrai nom et une *doctring* et un exemple simple l'illustrant (pas un *doctest* non plus).

```python
    # suite de class Pile():
    def mystère(self) -> Pile:
        autre = Pile()
        while not self.est_vide():
            autre.empile(self.dépile())
        return autre
```

* Question 2 : Proposer alors une méthode `.hauteur(self)-> int` qui renvoie la hauteur d'une pile, en la laissant inchangée en fin de compte.

* Question 3 : Proposer une méthode `.max_pile(self, i: int) -> int` qui renvoie la position de l'élément maximal parmi les `i` derniers empilés. La position du sommet de la pile est, par convention ici, égale à $1$. La pile doit être inchangée en fin de compte.

* Question 4 : Proposer une méthode `.retourner(self, i: int) -> None` qui modifie la pile en inversant l'ordre des `i` derniers éléments empilés. *On peut utiliser deux piles auxiliaires*.


## La file

* Le principe de la pile est : *LIFO : Last In, First Out*, (dernier entré, premier sorti).
* Le principe de la file est : *FIFO : First In, First Out*, (premier entré, premier sorti).

**Exercice 1** : En s'inspirant de la **première** implémentation de la pile, donner une implémentation d'une file d'une certaine taille maximale. On proposera le constructeur ainsi que les méthodes `.est_vide(self)`, `.enfile(self, élément)` et `.défile(self)` analogues au cas de la pile.

**Exercice 2** : Résoudre le problème [Distributeur automatique](http://www.france-ioi.org/algo/task.php?idChapter=527&iOrder=2) sur France-IOI.


> **Conseil** : on peut résoudre les problèmes dans un premier temps sans l'écriture avec style POO. Cependant, on demande alors une seconde écriture. Pourquoi ?
> * Le jour où on dispose d'une meilleure structure de données, il suffit de remplacer uniquement le bout de code de la classe, le problème restant intact. Sans POO, il faut souvent réécrire tout le problème pour utiliser les nouvelles idées... L'écriture avec le stye POO permet de s'affranchir presque totalement de la manière dont est écrit la classe. Il faut en revanche **toujours** garder à l'esprit : quel est le coût algorithmique de chaque méthode ?