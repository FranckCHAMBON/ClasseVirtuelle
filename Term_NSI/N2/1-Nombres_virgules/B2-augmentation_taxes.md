# Augmentation des taxes

## Sujet

 Votre programme doit lire trois nombres décimaux : la valeur actuelle de la taxe sur les fruits et légumes (en pourcentage), la nouvelle valeur de la taxe (en pourcentage), puis le prix actuel d'un légume, taxes comprises, en euros. Il devra calculer et afficher le prix du légume avec la nouvelle valeur de la taxe, arrondi au centime près.

## Exemples

### Exemple 1

entrée :

    5.5
    19.6
    24.9

sortie :

    28.23

### Exemple 2

entrée :

    21.5
    21.5
    19.99

sortie :

    19.99

## Solution officielle

```python
from math import *
 
taxeActuelle = float(input())
taxeFuture = float(input())
prixLegume = float(input())
nouveauPrix = prixLegume / ( 1 + taxeActuelle / 100) * (1 + taxeFuture / 100)
nouveauPrix = round(nouveauPrix * 100) / 100
print(nouveauPrix)
```

Remarque
: Il est inutile d'importer le module `math` pour disposer de la fonction `round`.
: Il est mal de faire `from math import *`.

## Solution alternative

C'est essentiellement un problème de mathématiques.

On rappelle que :
* $t\%$ d'une quantité $Q$, c'est $Q×\dfrac t {100}$.
* Faire subir à $Q$ une variation de $t\%$, c'est obtenir 
$$Q + Q×\dfrac t {100} = Q×1 + Q×\dfrac t {100} = Q×\left(1+\dfrac t {100}\right)$$

> Ainsi faire varier une quantité $Q$ de $t\%$ revient à multiplier $Q$ par $\left(1+\dfrac t {100}\right)$. Et annuler une variation de $t%$ revient à diviser par ce même coefficient. Ceci étant valable avec $t$ positif ou négatif.

Pour notre problème, on a :
* $P_{\text{T}_1} = P_\text{HT} × \left(1+\dfrac {t_1} {100}\right)$
* $P_{\text{T}_2} = P_\text{HT} × \left(1+\dfrac {t_2} {100}\right)$
* et $P_{\text{T}_1}$, $t_1$ et $t_2$ qui sont connus, $P_\text{HT}$ désigne le prix hors taxe.

On déduit le code :

```python
t_1 = float(input())
t_2 = float(input())
prix_avec_taxe1 = float(input())

prix_hors_taxe = prix_avec_taxe1 / (1 + t_1 /100)
prix_avec_taxe2 = prix_hors_taxe * (1 + t_2 /100)

print(round(prix_avec_taxe2, 2))
```

### Commentaires

* `round(x, 2)` permet d'avoir un arrondi de `x` avec 2 chiffres après la virgule.

* Une autre possibilité pour cet arrondi est de calculer `round(100 * x) / 100`