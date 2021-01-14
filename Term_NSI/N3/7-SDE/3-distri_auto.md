# [Distributeur automatique](http://www.france-ioi.org/algo/task.php?idChapter=527&idTask=357)

## Énoncé

Gérard est fatigué d'avoir à réordonner certaines piles de produits périssables assez rapidement et a donc décidé d'investir dans un système de distribution plus efficace. Avec ce système, dans lequel il place ses produits, les clients se servent automatiquement en bas de la pile et Gérard peut insérer les nouveaux produits tout en haut. Les clients prennent donc les produits dans l'ordre où Gérard les a placés.

Ce système réduit les chances qu'il reste des produits périmés, mais ne les supprime pas totalement. Il faut de temps en temps jeter quelques produits lorsqu'il est trop tard pour les vendre.

Gérard vous fournit la liste des opérations effectuées et vous demande d'écrire un programme capable de détecter la date d'expiration la plus ancienne parmi les produits restants.

### Contraintes

* $0 \leqslant N \leqslant 1000$, où $N$ est le nombre de produits à un moment donné.
* $0 \leqslant O \leqslant 300\,000$, où $O$ est le nombre d'opérations (achats ou ventes) à traiter.

### Entrée
* La première ligne de l'entrée contient un entier, $O$ : le nombre d'opérations effectuées.

* Chacune des $O$ lignes suivantes contient deux entiers, séparés par un espace et représente une opération. Celles-ci sont données dans l'ordre où les opérations sont effectuées.

* Le premier entier est la quantité de produits concernés par l'opération. Cette quantité est un entier positif lorsqu'il s'agit d'un achat par Gérard (ajout) et négatif lorsqu'il s'agit d'une vente (retrait).

* Le deuxième entier vaut 0 si l'opération est une vente (retrait). S'il s'agit d'un achat, cet entier représente la date de péremption du produit. L'entier correspond à la concaténation de l'année sur quatre chiffres, du mois sur deux chiffres et du jour sur deux chiffres.

### Sortie
* Vous devez afficher un entier sur la sortie : la date de péremption la plus petite parmi les produits restants, au même format que dans l'entrée.

> On vous garantit qu'il reste au moins un produit dans la file à la fin.

### Exemple

---

entrée :

    8
    3 20040810
    -1 0
    -1 0
    4 20040920
    -1 0
    3 20040916
    -3 0
    -2 0

sortie :

    20040916

---

### Commentaires
Huit opérations sont effectuées :

3 produits sont ajoutés, date de péremption le 10 août 2004
1 produit est retiré (date : 10 août 2004)
1 produit est retiré (date : 10 août 2004)
4 produits sont ajoutés (date : 20 septembre 2004)
1 produit est retiré (date : 10 août 2004)
3 produits sont ajoutés (date : 16 septembre 2004)
3 produits sont retirés (date : 20 septembre 2004)
2 produits sont retirés (dates : 20 et 16 septembre 2004)

Après ces opérations, il reste deux produits ayant pour date de péremption le 16 septembre 2004.

La date de péremption la plus ancienne parmi les produits restants est donc le 16 septembre 2004.

## Solution alternative

### File avec tableaux dynamiques
On construit ici une classe `File` basée sur les tableaux dynamiques de Python. **Ici**, ce n'est pas efficace.

```python
class File():
    def __init__(self):
        self.données = []

    def est_vide(self) -> bool:
        return self.données == []

    def enfile(self, valeur):
        self.données.append(valeur)
    
    def défile(self):
        if self.est_vide():
            raise ValueError('Pile vide')
        return self.données.pop(0) # ici, cette opération est lente !!!


nb_opérations = int(input())
stock = File()
for _ in range(nb_opérations):
    quantité, date_péremption = map(int, input().split())
    if quantité > 0:
        for _ in range(quantité):
            stock.enfile(date_péremption)
    else:
        for _ in range(-quantité):
            stock.défile()

# l'énoncé guarantit que la file est non vide ici
date_mini = stock.défile()

while not stock.est_vide():
    date = stock.défile()
    if date < date_mini:
        date_mini = date

print(date_mini)
```

> Le test 9 s'effectue en $1.83~\text{s}$, et le test 10 en plus de $2~\text{s}$ au-delà de la limite.
>> Échec !

Inclure le code dans une fonction `main` ou bien accélérer la lecture ne change rien ; la classe `file` est ici inefficace, pour défiler.

### File avec deque de `collections`

Python inclut la structure de données deque dans le module `collections` qui généralise la file. Utilisons cette structure pour une classe file efficace.

```python
from collections import deque

class File():
    def __init__(self):
        self.données = deque()

    def est_vide(self) -> bool:
        return self.données == deque()

    def enfile(self, valeur):
        self.données.append(valeur)
    
    def défile(self):
        if self.est_vide():
            raise ValueError('Pile vide')
        return self.données.popleft() # ici, cette opération est efficace !!!


nb_opérations = int(input())
stock = File()
for _ in range(nb_opérations):
    quantité, date_péremption = map(int, input().split())
    if quantité > 0:
        for _ in range(quantité):
            stock.enfile(date_péremption)
    else:
        for _ in range(-quantité):
            stock.défile()

# l'énoncé guarantit que la file est non vide ici
date_mini = stock.défile()

while not stock.est_vide():
    date = stock.défile()
    if date < date_mini:
        date_mini = date

print(date_mini)
```

Ce code s'avère à peine plus rapide. Accélérer la lecture reste insuffisant. Il faut travailler avec la structure deque, et reprendre l'idée du problème précédent. 


### Deque de collections

On travaille avec des couples d'entiers `(quantité, date)` pour le stock.
* On ajoute à droite le nouveau stock.
* On extrait à gauche tant que le client n'est pas satisfait.
* On ajoute à gauche pour remettre un reliquat que le client n'aurait pas pris.

```python
from collections import deque

class Deque:
    def __init__(self):
        self.données = deque()
    
    def est_vide(self):
        return self.données == deque()
    
    def ajout_gauche(self, élément):
        self.données.appendleft(élément)

    def ajout_droite(self, élément):
        self.données.append(élément)

    def extrait_gauche(self):
        if self.est_vide():
            raise ValueError("Deque vide")
        élément_gauche = self.données.popleft()
        return élément_gauche

    def extrait_droite(self):
        if self.est_vide():
            raise ValueError("Deque vide")
        élément_droite = self.données.pop()
        return élément_droite

nb_opérations = int(input())
stock = Deque()
for _ in range(nb_opérations):
    quantité, date_péremption = map(int, input().split())
    if quantité > 0:
        stock.ajout_droite((quantité, date_péremption))
    else:
        while -quantité > 0:
            x, date = stock.extrait_gauche()
            quantité += x
        if quantité != 0:
            stock.ajout_gauche((quantité, date))

# la deque est non vide, garanti par l'énoncé
_, date_mini = stock.extrait_gauche()

while not stock.est_vide():
    quantité, date = stock.extrait_gauche()
    if date < date_mini:
        date_mini = date

print(date_mini)
```

> Pour mémoire, 
>* le test 9 s'effectue en $0.73~\text{s}$, et
>* le test 10 en plus de $1.15~\text{s}$.
>> Validé.

### Deque avec deux piles

On peut construire soi-même une classe `Deque` sans utiliser `collections`, avec deux piles.

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

class Deque:
    def __init__(self):
        self.pile_gauche = Pile()
        self.pile_droite = Pile()
    
    def est_vide(self):
        return self.pile_gauche.est_vide() and self.pile_droite.est_vide()
    
    def ajout_gauche(self, élément):
        self.pile_gauche.empile(élément)

    def ajout_droite(self, élément):
        self.pile_droite.empile(élément)

    def extrait_gauche(self):
        if self.est_vide():
            raise ValueError("Deque vide")
        if self.pile_gauche.est_vide():
            while not self.pile_droite.est_vide():
                self.pile_gauche.empile(self.pile_droite.dépile())
        élément_gauche = self.pile_gauche.dépile()
        return élément_gauche

    def extrait_droite(self):
        if self.est_vide():
            raise ValueError("Deque vide")
        if self.pile_droite.est_vide():
            while not self.pile_gauche.est_vide():
                self.pile_droite.empile(self.pile_gauche.dépile())
        élément_droite = self.pile_droite.dépile()
        return élément_droite
```

> Pour mémoire, 
>* le test 9 s'effectue en $0.84~\text{s}$, et
>* le test 10 en plus de $1.39~\text{s}$.
>> Validé.

**Attention**, cette classe n'est pas très efficace lorsqu'une pile est vide et qu'on extrait alternativement à gauche et à droite ; les piles sont retournées à chaque étape. **Lent**.

### Deque avec un tableau

```python
class Deque():
    def __init__(self, taille_max):
        self.taille_max = taille_max
        self.données = [None for _ in range(taille_max)]
        self.i_droite = 0
        self.i_gauche = taille_max - 1
        self.taille = 0
    
    def est_vide(self):
        return self.taille == 0
    
    def ajout_droite(self, élément):
        if self.taille == self.taille_max:
            raise ValueError("Deque pleine")
        self.données[self.i_droite] = élément
        self.i_droite += 1
        if self.i_droite == self.taille_max:
            self.i_droite = 0
        self.taille += 1
    
    def ajout_gauche(self, élément):
        if self.taille == self.taille_max:
            raise ValueError("Deque pleine")
        self.données[self.i_gauche] = élément
        self.i_gauche -= 1
        if self.i_gauche == -1:
            self.i_gauche = self.taille_max - 1
        self.taille += 1

    def extrait_droite(self):
        if self.taille == 0:
            raise ValueError("Deque vide")
        self.i_droite -= 1
        if self.i_droite == -1:
            self.i_droite = self.taille_max - 1
        self.taille -= 1
        élément = self.données[self.i_droite]
        #self.données[self.i_droite] = None # facultatif
        return élément

    def extrait_gauche(self):
        if self.taille == 0:
            raise ValueError("Deque vide")
        self.i_gauche += 1
        if self.i_gauche == self.taille_max:
            self.i_gauche = 0
        self.taille -= 1
        élément = self.données[self.i_gauche]
        #self.données[self.i_gauche] = None # facultatif
        return élément
```

> Pour mémoire, 
>* le test 9 s'effectue en $0.76~\text{s}$, et
>* le test 10 en plus de $1.21~\text{s}$.
>> Validé.

**Attention**, le corps du programme change un peu, il faut spécifier la taille maximale de la deque, l'énoncé précise que $1000$ est suffisant.

```python
nb_opérations = int(input())
stock = Deque(1000) # <<<==== Important
for _ in range(nb_opérations):
    quantité, date_péremption = map(int, input().split())
...
```

## Conclusion

On retiendra qu'avec Python, il vaut mieux utiliser les structures déjà proposées qui sont bien codées et efficaces.

D'un point de vue pédagogique, on retiendra les différentes implémentations, en particulier celle avec le tableau que l'on peut facilement adapter à presque tout langage de programmation.

On retiendra aussi que la POO ralentit le code, et qu'on pouvait le résoudre avec juste l'utilisation d'une file via une deque avec le code sans POO :

```python
import collections

stock = collections.deque()
enfile = stock.append
défile = stock.popleft

nb_opérations = int(input())
for _ in range(nb_opérations):
    variation, date = map(int, input().split())
    if variation > 0:
        for _ in range(variation):
            enfile(date)
    else:
        for _ in range(-variation):
            défile()

mini = stock.pop()
while stock:
    date = défile()
    if date < mini:
        mini = date

print(mini)
```

Enfin, placé dans une fonction `main` et avec une lecture rapide des entiers, cette méthode (enfiler/défiler une date à la fois) termine les tests 9 et 10 en $0.42\,\text{s}$ et $0.65\,\text{s}$.

Avec la méthode où on enfile/défile un couple, on finit en $0.27\,\text{s}$ et $0.41\,\text{s}$, avec le code suivant :

```python
import collections, sys

def main(input=sys.stdin.readline):
    stock = collections.deque()
    ajout_droite = stock.append
    ajout_gauche = stock.appendleft
    extrait_droite = stock.pop
    extrait_gauche = stock.popleft
    
    nb_opérations = int(input())
    for _ in range(nb_opérations):
        quantité, date = map(int, input().split())
        if quantité > 0:
            ajout_droite((quantité, date))
        else:
            while quantité < 0:
                q, date = extrait_gauche()
                quantité += q
            if quantité != 0:
                ajout_gauche((quantité, date))

    _, mini = extrait_droite()
    while stock:
        _, date = extrait_droite()
        if date < mini:
            mini = date

    print(mini)

main()
```