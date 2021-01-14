# [État du stock](http://www.france-ioi.org/algo/task.php?idChapter=527&idTask=355)

## Énoncé

Gérard s'est débarrassé des vieilles caisses enregistreuses et dispose maintenant de tout un système moderne, avec lecteurs de code-barres. Un passage rapide d'un produit devant le lecteur et le nom du produit s'affiche instantanément à l'écran à côté de son prix.

Votre ami souhaite utiliser ce système pour maintenir un état complet de son stock de produits et préparer ses commandes en évitant d'avoir à faire l'inventaire toutes les semaines.

Lors de chaque achat ou vente d'un produit, l'opération est stockée dans un fichier, accompagnée du numéro du produit.

Vous devez écrire un programme qui analyse le contenu de ce fichier et détermine la quantité restante de chacun des produits du magasin.

### Contraintes

* $1 \leqslant P \leqslant 10\,000$, où $P$ est le nombre de types de produits du magasin.
* $0 \leqslant N_k \leqslant 1000$, où $N_k$ est le nombre de produits de type $k$ disponibles dans le magasin à un moment donné.
* $0 \leqslant O \leqslant 300\,000$, où $O$ est le nombre d'opérations (achats ou ventes) à traiter.

### Entrée
Les données du fichier sont transmises à votre programme sur l'entrée standard.

* La première ligne de l'entrée contient un entier $P$ : le nombre de types de produits du magasin.

* La deuxième ligne de l'entrée contient $P$ entiers séparés par des espaces : le nombre de produits de chaque type disponible dans le magasin, dans l'ordre du type, avant que les achats et ventes décrits dans le fichier n'aient été effectués.

* La troisième ligne de l'entrée contient un entier $O$ : le nombre d'opérations d'achat ou de vente à traiter.

* Chacune des $O$ lignes suivantes représente une opération et contient deux entiers, séparés par un espace : le numéro du type de produit qui a été acheté ou vendu, et la quantité de produits concernée. Cette quantité est un entier positif lorsqu'il s'agit d'un achat par Gérard, et négatif lorsqu'il s'agit d'une vente.

### Sortie
* Vous devez afficher une ligne sur la sortie, contenant $P$ entiers, séparés par des espaces : le nombre de produits de chaque type disponible dans le magasin, après les achats et ventes décrits dans l'entrée.

### Exemple

---

entrée :

    4
    5 10 0 4
    8
    1 1
    2 -2
    4 2
    3 5
    3 -2
    3 -1
    1 4
    1 -5

sortie :

    5 8 2 6

---

### Commentaires
Gérard dispose au départ de 5 produits de type 1, 10 produits de type 2, aucun produit de type 3 et de 4 produits de type 4.

8 opérations sont effectuées :

1 produit de type 1 est acheté (il y en a alors 6)
2 produits de type 2 sont vendus (il en reste 8)
2 produits de type 4 sont achetés (il y en a alors 6)
5 produits de type 3 sont achetés (il y en a alors 5)
2 produits de type 3 sont vendus (il en reste 3)
1 produit de type 3 est vendu (il en reste 2)
4 produits de type 1 sont achetés (il en a alors 10)
5 produits de type 1 sont vendus (il en reste 5)

Au final, il reste donc :

5 produits de type 1
8 produits de type 2
2 produits de type 3
6 produits de type 4

## Solution alternative

```python
nb_produits = int(input())
stock = list(map(int, input().split()))

nb_opérations = int(input())
for _ in range(nb_opérations):
    i_produit, variation = map(int, input().split())
    stock[i_produit - 1] += variation

for quantité in stock:
    print(quantité, end=" ")
```

### Remarques

* On utilise `i_produit - 1` pour passer d'une numérotation à partir de $1$, à une numérotation à partir de $0$.
* Ce code nature, finit en $0.86~\text{s}$ sur le test 11 ; le plus long.
* Placé dans une fonction `main`, il finit à peine plus vite en $0.81~\text{s}$.
* En revanche, changer la méthode de lecture s'avère **ici** très utile pour ce problème de complexité linéaire. La partie lecture prend proportionnellement beaucoup de temps. En ajoutant `input=sys.stdin.readline`, on passe à $0.45~\text{s}$.

```python
import sys
def main(input=sys.stdin.readline):
    nb_produits = int(input())
    stock = list(map(int, input().split()))
    
    nb_opérations = int(input())
    for _ in range(nb_opérations):
        i_produit, variation = map(int, input().split())
        stock[i_produit - 1] += variation
    
    for quantité in stock:
        print(quantité, end=" ")
main()
```