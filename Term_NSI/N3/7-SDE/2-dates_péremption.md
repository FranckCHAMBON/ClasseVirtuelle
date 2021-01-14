# [Dates de péremption](http://www.france-ioi.org/algo/task.php?idChapter=527&idTask=356)

## Énoncé

Dans son épicerie, Gérard vend de nombreux produits alimentaires et doit porter une attention particulière aux dates de péremption de certains d'entre eux. Il ne voudrait surtout pas que ses clients tombent malades après avoir consommé ses conserves.

Gérard n'a pas beaucoup de place, mais beaucoup de produits à vendre. Il entasse donc les produits d'un même type les uns sur les autres. Lorsqu'un client achète un produit, il prend toujours celui du haut de la pile. Quand Gérard renouvelle son stock, il n'a en général pas beaucoup de temps et place les nouveaux produits juste au-dessus de ceux qui sont déjà en rayon.

Avec ce système, les produits du bas de la pile risquent cependant d'y rester très (trop) longtemps. Gérard doit donc régulièrement faire le tour de son magasin, pour vérifier si les produits en bas des piles n'y sont pas depuis trop longtemps, puis les placer sur le dessus, ou les jeter s'ils sont périmés

Votre ami vous demande de l'aider à éviter cette tâche fastidieuse, en lui écrivant un programme qui détecte automatiquement, pour une pile de produits donnée, la date de péremption la plus ancienne parmi les produits de la pile.

Il vous fournit pour cela une liste des opérations effectuées sur cette pile (qui est vide au départ) : les achats et ventes de produits de cette pile, accompagnés des dates d'expiration.

### Contraintes

* $0 \leqslant N \leqslant 1000$, où $N$ est le nombre de produits de la pile à un moment donné.
* $0 \leqslant O \leqslant 300\,000$, où $O$ est le nombre d'opérations (achats ou ventes) à traiter pour cette pile.
* $1000 \leqslant A \leqslant 9\,999$, où $A$ est l'année de la date d'expiration.

### Entrée

* La première ligne de l'entrée contient un entier, $O$ : le nombre d'opérations effectuées sur la pile.

* Chacune des $O$ lignes suivantes contient deux entiers, séparés par un espace et représente une opération. Celles-ci sont données dans l'ordre où les opérations sont effectuées.

    * Le premier entier est la quantité de produits concernés par l'opération. Cette quantité est un entier positif lorsqu'il s'agit d'un achat par Gérard (ajout sur la pile), et négatif lorsqu'il s'agit d'une vente (retrait).

    * Le deuxième entier vaut 0 si l'opération est une vente (retrait). S'il s'agit d'un achat, cet entier représente la date de péremption du produit. L'entier correspond à la concaténation de l'année sur quatre chiffres, du mois sur deux chiffres et du jour sur deux chiffres.

### Sortie
* Vous devez afficher un entier sur la sortie : la date de péremption la plus petite parmi les produits de la pile, au même format que dans l'entrée.

> On vous garantit qu'il reste toujours au moins un produit dans la pile après le traitement des opérations.

### Exemple

---

entrée :

    8
    3 20040810
    -1 0
    -1 0
    3 20040920
    -1 0
    4 20040916
    -3 0
    -2 0

sortie :

    20040810

---

### Commentaires
Huit opérations sont effectuées sur la pile, qui est vide au départ :

3 produits sont ajoutés, date de péremption le 10 août 2004
1 produit est retiré (date : 10 août 2004)
1 produit est retiré (date : 10 août 2004)
3 produits sont ajoutés (date : 20 septembre 2004)
1 produit est retiré (date : 20 septembre 2004)
4 produits sont ajoutés (date : 16 septembre 2004)
3 produits sont retirés (date : 16 septembre 2004)
2 produits sont retirés (dates : 16 et 20 septembre 2004)

Après ces opérations, la pile contient deux produits. De haut en bas :

Un produit ayant pour date de péremption le 20 septembre 2004.
Un produit ayant pour date de péremption le 10 août 2004.

La date de péremption la plus ancienne parmi les produits restants est donc le 10 août 2004.

## Solution alternative

On utilise ici la POO pour présenter notre solution, la POO apporte un gain en clarté dans le code, mais le ralentit ici de plus de $15\%$.

On construit ici une classe `Pile` basée sur les tableaux dynamiques de Python. **Ici**, c'est efficace.

```python
class Pile():
    def __init__(self):
        self.données = []

    def est_vide(self) -> bool:
        return self.données == []

    def empile(self, valeur):
        self.données.append(valeur)
    
    def dépile(self):
        if self.est_vide():
            raise ValueError('Pile vide')
        return self.données.pop()


nb_opérations = int(input())
stock = Pile()
for _ in range(nb_opérations):
    quantité, date_péremption = map(int, input().split())
    if quantité > 0:
        for _ in range(quantité):
            stock.empile(date_péremption)
    else:
        for _ in range(-quantité):
            stock.dépile()

# l'énoncé guarantit que la pile est non vide ici
date_mini = stock.dépile()

while not stock.est_vide():
    date = stock.dépile()
    if date < date_mini:
        date_mini = date

print(date_mini)
```

Ici, on a empilé/dépilé autant de fois que `quantité` l'indiquait.

On peut écrire une version où on empile/dépile des couples d'entiers `(quantité, date)`.

```python
class Pile():
    def __init__(self):
        self.données = []

    def est_vide(self) -> bool:
        return self.données == []
        
    def empile(self, valeur):
        self.données.append(valeur)
    
    def dépile(self):
        if self.est_vide():
            raise ValueError('Pile vide')
        return self.données.pop()

nb_opérations = int(input())
stock = Pile()
for _ in range(nb_opérations):
    quantité, date_péremption = map(int, input().split())
    if quantité > 0:
        stock.empile((quantité, date_péremption))
    else:
        while quantité < 0:
            x, date = stock.dépile()
            quantité += x
        if quantité != 0:
            stock.empile((quantité, date))

# la pile est non vide, garanti par l'énoncé
_, date_mini = stock.dépile()

while not stock.est_vide():
    quantité, date = stock.dépile()
    if date < date_mini:
        date_mini = date

print(date_mini)
```
